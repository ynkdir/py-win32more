from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Networking.WindowsWebServices
import Windows.Win32.Security.Authentication.Identity
import Windows.Win32.Security.Cryptography
import Windows.Win32.System.WinRT
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
WEBAUTHN_API_VERSION_1: UInt32 = 1
WEBAUTHN_API_VERSION_2: UInt32 = 2
WEBAUTHN_API_VERSION_3: UInt32 = 3
WEBAUTHN_API_CURRENT_VERSION: UInt32 = 3
WEBAUTHN_RP_ENTITY_INFORMATION_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_MAX_USER_ID_LENGTH: UInt32 = 64
WEBAUTHN_USER_ENTITY_INFORMATION_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_HASH_ALGORITHM_SHA_256: String = 'SHA-256'
WEBAUTHN_HASH_ALGORITHM_SHA_384: String = 'SHA-384'
WEBAUTHN_HASH_ALGORITHM_SHA_512: String = 'SHA-512'
WEBAUTHN_CLIENT_DATA_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CREDENTIAL_TYPE_PUBLIC_KEY: String = 'public-key'
WEBAUTHN_COSE_ALGORITHM_ECDSA_P256_WITH_SHA256: Int32 = -7
WEBAUTHN_COSE_ALGORITHM_ECDSA_P384_WITH_SHA384: Int32 = -35
WEBAUTHN_COSE_ALGORITHM_ECDSA_P521_WITH_SHA512: Int32 = -36
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA256: Int32 = -257
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA384: Int32 = -258
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA512: Int32 = -259
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA256: Int32 = -37
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA384: Int32 = -38
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA512: Int32 = -39
WEBAUTHN_COSE_CREDENTIAL_PARAMETER_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CREDENTIAL_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAP_TRANSPORT_USB: UInt32 = 1
WEBAUTHN_CTAP_TRANSPORT_NFC: UInt32 = 2
WEBAUTHN_CTAP_TRANSPORT_BLE: UInt32 = 4
WEBAUTHN_CTAP_TRANSPORT_TEST: UInt32 = 8
WEBAUTHN_CTAP_TRANSPORT_INTERNAL: UInt32 = 16
WEBAUTHN_CTAP_TRANSPORT_FLAGS_MASK: UInt32 = 31
WEBAUTHN_CREDENTIAL_EX_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_EXTENSIONS_IDENTIFIER_HMAC_SECRET: String = 'hmac-secret'
WEBAUTHN_USER_VERIFICATION_ANY: UInt32 = 0
WEBAUTHN_USER_VERIFICATION_OPTIONAL: UInt32 = 1
WEBAUTHN_USER_VERIFICATION_OPTIONAL_WITH_CREDENTIAL_ID_LIST: UInt32 = 2
WEBAUTHN_USER_VERIFICATION_REQUIRED: UInt32 = 3
WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_PROTECT: String = 'credProtect'
WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_BLOB: String = 'credBlob'
WEBAUTHN_EXTENSIONS_IDENTIFIER_MIN_PIN_LENGTH: String = 'minPinLength'
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_ANY: UInt32 = 0
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_PLATFORM: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM_U2F_V2: UInt32 = 3
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_ANY: UInt32 = 0
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_REQUIRED: UInt32 = 1
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_PREFERRED: UInt32 = 2
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_DISCOURAGED: UInt32 = 3
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_ANY: UInt32 = 0
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_NONE: UInt32 = 1
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_INDIRECT: UInt32 = 2
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_DIRECT: UInt32 = 3
WEBAUTHN_ENTERPRISE_ATTESTATION_NONE: UInt32 = 0
WEBAUTHN_ENTERPRISE_ATTESTATION_VENDOR_FACILITATED: UInt32 = 1
WEBAUTHN_ENTERPRISE_ATTESTATION_PLATFORM_MANAGED: UInt32 = 2
WEBAUTHN_LARGE_BLOB_SUPPORT_NONE: UInt32 = 0
WEBAUTHN_LARGE_BLOB_SUPPORT_REQUIRED: UInt32 = 1
WEBAUTHN_LARGE_BLOB_SUPPORT_PREFERRED: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_2: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_3: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_4: UInt32 = 4
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_CURRENT_VERSION: UInt32 = 4
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_NONE: UInt32 = 0
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_GET: UInt32 = 1
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_SET: UInt32 = 2
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_DELETE: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_2: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_3: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_4: UInt32 = 4
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_5: UInt32 = 5
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_CURRENT_VERSION: UInt32 = 5
WEBAUTHN_ATTESTATION_DECODE_NONE: UInt32 = 0
WEBAUTHN_ATTESTATION_DECODE_COMMON: UInt32 = 1
WEBAUTHN_ATTESTATION_VER_TPM_2_0: String = '2.0'
WEBAUTHN_COMMON_ATTESTATION_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_ATTESTATION_TYPE_PACKED: String = 'packed'
WEBAUTHN_ATTESTATION_TYPE_U2F: String = 'fido-u2f'
WEBAUTHN_ATTESTATION_TYPE_TPM: String = 'tpm'
WEBAUTHN_ATTESTATION_TYPE_NONE: String = 'none'
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_1: UInt32 = 1
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_2: UInt32 = 2
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_3: UInt32 = 3
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_4: UInt32 = 4
WEBAUTHN_CREDENTIAL_ATTESTATION_CURRENT_VERSION: UInt32 = 4
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NONE: UInt32 = 0
WEBAUTHN_CRED_LARGE_BLOB_STATUS_SUCCESS: UInt32 = 1
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_SUPPORTED: UInt32 = 2
WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_DATA: UInt32 = 3
WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_PARAMETER: UInt32 = 4
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_FOUND: UInt32 = 5
WEBAUTHN_CRED_LARGE_BLOB_STATUS_MULTIPLE_CREDENTIALS: UInt32 = 6
WEBAUTHN_CRED_LARGE_BLOB_STATUS_LACK_OF_SPACE: UInt32 = 7
WEBAUTHN_CRED_LARGE_BLOB_STATUS_PLATFORM_ERROR: UInt32 = 8
WEBAUTHN_CRED_LARGE_BLOB_STATUS_AUTHENTICATOR_ERROR: UInt32 = 9
WEBAUTHN_ASSERTION_VERSION_1: UInt32 = 1
WEBAUTHN_ASSERTION_VERSION_2: UInt32 = 2
WEBAUTHN_ASSERTION_CURRENT_VERSION: UInt32 = 2
WS_HTTP_HEADER_MAPPING_COMMA_SEPARATOR: Int32 = 1
WS_HTTP_HEADER_MAPPING_SEMICOLON_SEPARATOR: Int32 = 2
WS_HTTP_HEADER_MAPPING_QUOTED_VALUE: Int32 = 4
WS_HTTP_RESPONSE_MAPPING_STATUS_CODE: Int32 = 1
WS_HTTP_RESPONSE_MAPPING_STATUS_TEXT: Int32 = 2
WS_HTTP_REQUEST_MAPPING_VERB: Int32 = 2
WS_MATCH_URL_DNS_HOST: Int32 = 1
WS_MATCH_URL_DNS_FULLY_QUALIFIED_HOST: Int32 = 2
WS_MATCH_URL_NETBIOS_HOST: Int32 = 4
WS_MATCH_URL_LOCAL_HOST: Int32 = 8
WS_MATCH_URL_HOST_ADDRESSES: Int32 = 16
WS_MATCH_URL_THIS_HOST: Int32 = 31
WS_MATCH_URL_PORT: Int32 = 32
WS_MATCH_URL_EXACT_PATH: Int32 = 64
WS_MATCH_URL_PREFIX_PATH: Int32 = 128
WS_MATCH_URL_NO_QUERY: Int32 = 256
WS_MUST_UNDERSTAND_HEADER_ATTRIBUTE: Int32 = 1
WS_RELAY_HEADER_ATTRIBUTE: Int32 = 2
WS_HTTP_HEADER_AUTH_SCHEME_NONE: Int32 = 1
WS_HTTP_HEADER_AUTH_SCHEME_BASIC: Int32 = 2
WS_HTTP_HEADER_AUTH_SCHEME_DIGEST: Int32 = 4
WS_HTTP_HEADER_AUTH_SCHEME_NTLM: Int32 = 8
WS_HTTP_HEADER_AUTH_SCHEME_NEGOTIATE: Int32 = 16
WS_HTTP_HEADER_AUTH_SCHEME_PASSPORT: Int32 = 32
WS_CERT_FAILURE_CN_MISMATCH: Int32 = 1
WS_CERT_FAILURE_INVALID_DATE: Int32 = 2
WS_CERT_FAILURE_UNTRUSTED_ROOT: Int32 = 4
WS_CERT_FAILURE_WRONG_USAGE: Int32 = 8
WS_CERT_FAILURE_REVOCATION_OFFLINE: Int32 = 16
WS_STRUCT_ABSTRACT: Int32 = 1
WS_STRUCT_IGNORE_TRAILING_ELEMENT_CONTENT: Int32 = 2
WS_STRUCT_IGNORE_UNHANDLED_ATTRIBUTES: Int32 = 4
WS_FIELD_POINTER: Int32 = 1
WS_FIELD_OPTIONAL: Int32 = 2
WS_FIELD_NILLABLE: Int32 = 4
WS_FIELD_NILLABLE_ITEM: Int32 = 8
WS_FIELD_OTHER_NAMESPACE: Int32 = 16
WS_SERVICE_OPERATION_MESSAGE_NILLABLE_ELEMENT: Int32 = 1
WS_URL_FLAGS_ALLOW_HOST_WILDCARDS: Int32 = 1
WS_URL_FLAGS_NO_PATH_COLLAPSE: Int32 = 2
WS_URL_FLAGS_ZERO_TERMINATE: Int32 = 4
@winfunctype('webservices.dll')
def WsStartReaderCanonicalization(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: c_void_p, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEndReaderCanonicalization(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsStartWriterCanonicalization(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: c_void_p, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEndWriterCanonicalization(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateXmlBuffer(heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_head), propertyCount: UInt32, buffer: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveNode(nodePosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateReader(properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head), propertyCount: UInt32, reader: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetInput(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), encoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head), input: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetInputToBuffer(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), buffer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeReader(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetReaderProperty(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), id: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetReaderNode(xmlReader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), node: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFillReader(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), minSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadStartElement(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadToStartElement(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), found: POINTER(Windows.Win32.Foundation.BOOL), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadStartAttribute(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), attributeIndex: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndAttribute(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadNode(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSkipNode(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndElement(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFindAttribute(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), required: Windows.Win32.Foundation.BOOL, attributeIndex: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadValue(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), valueType: Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadChars(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), chars: Windows.Win32.Foundation.PWSTR, maxCharCount: UInt32, actualCharCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadCharsUtf8(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), bytes: c_char_p_no, maxByteCount: UInt32, actualByteCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadBytes(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), bytes: c_void_p, maxByteCount: UInt32, actualByteCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadArray(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), valueType: Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, array: c_void_p, arraySize: UInt32, itemOffset: UInt32, itemCount: UInt32, actualItemCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetReaderPosition(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), nodePosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetReaderPosition(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), nodePosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMoveReader(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), moveTo: Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO, found: POINTER(Windows.Win32.Foundation.BOOL), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateWriter(properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head), propertyCount: UInt32, writer: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeWriter(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsSetOutput(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), encoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head), output: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetOutputToBuffer(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), buffer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head), propertyCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetWriterProperty(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), id: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFlushWriter(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), minSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartElement(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndStartElement(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlnsAttribute(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), singleQuote: Windows.Win32.Foundation.BOOL, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartAttribute(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), singleQuote: Windows.Win32.Foundation.BOOL, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndAttribute(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteValue(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), valueType: Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlBuffer(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), xmlBuffer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadXmlBuffer(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), xmlBuffer: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlBufferToBytes(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), xmlBuffer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), encoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head), propertyCount: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), bytes: POINTER(c_void_p), byteCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadXmlBufferFromBytes(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), encoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head), propertyCount: UInt32, bytes: c_void_p, byteCount: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), xmlBuffer: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteArray(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), valueType: Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, array: c_void_p, arraySize: UInt32, itemOffset: UInt32, itemCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteQualifiedName(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteChars(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), chars: Windows.Win32.Foundation.PWSTR, charCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteCharsUtf8(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), bytes: c_char_p_no, byteCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteBytes(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), bytes: c_void_p, byteCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsPushBytes(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), callback: Windows.Win32.Networking.WindowsWebServices.WS_PUSH_BYTES_CALLBACK, callbackState: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsPullBytes(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), callback: Windows.Win32.Networking.WindowsWebServices.WS_PULL_BYTES_CALLBACK, callbackState: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndElement(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteText(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), text: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartCData(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndCData(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteNode(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), node: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPrefixFromNamespace(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), required: Windows.Win32.Foundation.BOOL, prefix: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetWriterPosition(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), nodePosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetWriterPosition(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), nodePosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMoveWriter(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), moveTo: Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO, found: POINTER(Windows.Win32.Foundation.BOOL), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsTrimXmlWhitespace(chars: Windows.Win32.Foundation.PWSTR, charCount: UInt32, trimmedChars: POINTER(POINTER(UInt16)), trimmedCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsVerifyXmlNCName(ncNameChars: Windows.Win32.Foundation.PWSTR, ncNameCharCount: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsXmlStringEquals(string1: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), string2: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetNamespaceFromPrefix(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), required: Windows.Win32.Foundation.BOOL, ns: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadQualifiedName(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetXmlAttribute(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), valueChars: POINTER(POINTER(UInt16)), valueCharCount: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCopyNode(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAsyncExecute(asyncState: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_STATE_head), operation: Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_FUNCTION, callbackModel: Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateChannel(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head), propertyCount: UInt32, securityDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head), channel: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), endpointAddress: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendMessage(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), messageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, bodyValue: c_void_p, bodyValueSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReceiveMessage(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), messageDescriptions: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)), messageDescriptionCount: UInt32, receiveOption: Windows.Win32.Networking.WindowsWebServices.WS_RECEIVE_OPTION, readBodyOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, index: POINTER(UInt32), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRequestReply(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), requestMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), requestMessageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, requestBodyValue: c_void_p, requestBodyValueSize: UInt32, replyMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), replyMessageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head), readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendReplyMessage(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), replyMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), replyMessageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, replyBodyValue: c_void_p, replyBodyValueSize: UInt32, requestMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendFaultMessageForError(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), replyMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), faultError: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), faultErrorCode: Windows.Win32.Foundation.HRESULT, faultDisclosure: Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE, requestMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetChannelProperty(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetChannelProperty(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteMessageStart(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteMessageEnd(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMessageStart(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMessageEnd(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbandonMessage(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsShutdownSessionChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetOperationContextProperty(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), id: Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetDictionary(encoding: Windows.Win32.Networking.WindowsWebServices.WS_ENCODING, dictionary: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndpointAddressExtension(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), endpointAddress: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), extensionType: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_EXTENSION_TYPE, readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateError(properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_head), propertyCount: UInt32, error: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddErrorString(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), string: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetErrorString(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), index: UInt32, string: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCopyError(source: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), destination: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetErrorProperty(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), id: Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID, buffer: c_void_p, bufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetErrorProperty(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), id: Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID, value: c_void_p, valueSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetError(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeError(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetFaultErrorProperty(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), id: Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID, buffer: c_void_p, bufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetFaultErrorProperty(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), id: Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID, value: c_void_p, valueSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateFaultFromError(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), faultErrorCode: Windows.Win32.Foundation.HRESULT, faultDisclosure: Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), fault: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetFaultErrorDetail(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), faultDetailDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetFaultErrorDetail(error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head), faultDetailDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION_head), readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateHeap(maxSize: UIntPtr, trimSize: UIntPtr, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_head), propertyCount: UInt32, heap: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAlloc(heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), size: UIntPtr, ptr: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetHeapProperty(heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), id: Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetHeap(heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeHeap(heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsCreateListener(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_head), propertyCount: UInt32, securityDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head), listener: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), url: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAcceptChannel(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetListenerProperty(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), id: Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetListenerProperty(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), id: Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateChannelForListener(listener: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head), propertyCount: UInt32, channel: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMessage(envelopeVersion: Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION, addressingVersion: Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head), propertyCount: UInt32, message: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMessageForChannel(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head), propertyCount: UInt32, message: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsInitializeMessage(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), initialization: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION, sourceMessage: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetMessage(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeMessage(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetHeaderAttributes(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), headerAttributes: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerType: Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, valueType: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetCustomHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), customHeaderDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), repeatingOption: Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION, headerIndex: UInt32, readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, headerAttributes: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerType: Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerType: Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, valueType: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveCustomHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), headerNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddCustomHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, headerAttributes: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddMappedHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), valueType: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveMappedHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMappedHeader(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), repeatingOption: Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION, headerIndex: UInt32, valueType: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteBody(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), bodyDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadBody(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), bodyDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEnvelopeStart(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), doneCallback: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK, doneCallbackState: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEnvelopeEnd(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEnvelopeStart(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), doneCallback: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK, doneCallbackState: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEnvelopeEnd(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMessageProperty(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), id: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetMessageProperty(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), id: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddressMessage(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), address: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCheckMustUnderstandHeaders(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMarkHeaderAsUnderstood(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), headerPosition: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFillBody(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), minSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFlushBody(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), minSize: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRequestSecurityToken(channel: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_head), propertyCount: UInt32, token: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetSecurityTokenProperty(securityToken: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head), id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID, value: c_void_p, valueSize: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateXmlSecurityToken(tokenXml: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), tokenKey: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_head), propertyCount: UInt32, token: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeSecurityToken(token: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsRevokeSecurityContext(securityContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetSecurityContextProperty(securityContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_head), id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadElement(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), elementDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadAttribute(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), attributeDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION_head), readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadType(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), typeMapping: Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, type: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, typeDescription: c_void_p, readOption: Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteElement(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), elementDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteAttribute(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), attributeDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION_head), writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteType(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), typeMapping: Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, type: Windows.Win32.Networking.WindowsWebServices.WS_TYPE, typeDescription: c_void_p, writeOption: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRegisterOperationForCancel(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), cancelCallback: Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CANCEL_CALLBACK, freestateCallback: Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_FREE_STATE_CALLBACK, userState: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetServiceHostProperty(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head), id: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceHost(endpoints: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_head)), endpointCount: UInt16, serviceProperties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_head), servicePropertyCount: UInt32, serviceHost: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenServiceHost(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseServiceHost(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortServiceHost(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeServiceHost(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetServiceHost(serviceHost: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetServiceProxyProperty(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), id: Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceProxy(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, securityDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head), properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_head), propertyCount: UInt32, channelProperties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head), channelPropertyCount: UInt32, serviceProxy: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenServiceProxy(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), address: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseServiceProxy(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortServiceProxy(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeServiceProxy(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetServiceProxy(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbandonCall(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), callId: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCall(serviceProxy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head), operation: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION_head), arguments: POINTER(c_void_p), heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), callProperties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_head), callPropertyCount: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsDecodeUrl(url: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), flags: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), outUrl: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_URL_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEncodeUrl(url: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_URL_head), flags: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), outUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCombineUrl(baseUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), referenceUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), flags: UInt32, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), resultUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsDateTimeToFileTime(dateTime: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_head), fileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFileTimeToDateTime(fileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), dateTime: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMetadata(properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_head), propertyCount: UInt32, metadata: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMetadata(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head), reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), url: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeMetadata(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetMetadata(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMetadataProperty(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head), id: Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMissingMetadataDocumentAddress(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head), address: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMetadataEndpoints(metadata: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_head), endpoints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_ENDPOINTS_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMatchPolicyAlternative(policy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_head), alternativeIndex: UInt32, policyConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_CONSTRAINTS_head), matchRequired: Windows.Win32.Foundation.BOOL, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPolicyProperty(policy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_head), id: Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPolicyAlternativeCount(policy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_head), count: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceProxyFromTemplate(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_head), propertyCount: UInt32, templateType: Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE, templateValue: c_void_p, templateSize: UInt32, templateDescription: c_void_p, templateDescriptionSize: UInt32, serviceProxy: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceEndpointFromTemplate(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_head), propertyCount: UInt32, addressUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), contract: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CONTRACT_head), authorizationCallback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), templateType: Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE, templateValue: c_void_p, templateSize: UInt32, templateDescription: c_void_p, templateDescriptionSize: UInt32, serviceEndpoint: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetApiVersionNumber() -> UInt32: ...
@winfunctype('webauthn.dll')
def WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable(pbIsUserVerifyingPlatformAuthenticatorAvailable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorMakeCredential(hWnd: Windows.Win32.Foundation.HWND, pRpInformation: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_RP_ENTITY_INFORMATION_head), pUserInformation: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_USER_ENTITY_INFORMATION_head), pPubKeyCredParams: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS_head), pWebAuthNClientData: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA_head), pWebAuthNMakeCredentialOptions: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_head), ppWebAuthNCredentialAttestation: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorGetAssertion(hWnd: Windows.Win32.Foundation.HWND, pwszRpId: Windows.Win32.Foundation.PWSTR, pWebAuthNClientData: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA_head), pWebAuthNGetAssertionOptions: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_head), ppWebAuthNAssertion: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_ASSERTION_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeCredentialAttestation(pWebAuthNCredentialAttestation: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION_head)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeAssertion(pWebAuthNAssertion: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_ASSERTION_head)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNGetCancellationId(pCancellationId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNCancelCurrentOperation(pCancellationId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetErrorName(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('webauthn.dll')
def WebAuthNGetW3CExceptionDOMError(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IContentPrefetcherTaskTrigger(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b35a14a-6094-4799-a6-0e-e4-74-e1-5d-4d-c9')
    @commethod(6)
    def TriggerContentPrefetcherTask(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsRegisteredForContentPrefetch(packageFullName: Windows.Win32.Foundation.PWSTR, isRegistered: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
class WEBAUTHN_ASSERTION(Structure):
    dwVersion: UInt32
    cbAuthenticatorData: UInt32
    pbAuthenticatorData: c_char_p_no
    cbSignature: UInt32
    pbSignature: c_char_p_no
    Credential: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL
    cbUserId: UInt32
    pbUserId: c_char_p_no
    Extensions: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: c_char_p_no
    dwCredLargeBlobStatus: UInt32
class WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS
    Extensions: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    dwUserVerificationRequirement: UInt32
    dwFlags: UInt32
    pwszU2fAppId: Windows.Win32.Foundation.PWSTR
    pbU2fAppId: POINTER(Windows.Win32.Foundation.BOOL)
    pCancellationId: POINTER(Guid)
    pAllowCredentialList: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST_head)
    dwCredLargeBlobOperation: UInt32
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: c_char_p_no
class WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS
    Extensions: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    bRequireResidentKey: Windows.Win32.Foundation.BOOL
    dwUserVerificationRequirement: UInt32
    dwAttestationConveyancePreference: UInt32
    dwFlags: UInt32
    pCancellationId: POINTER(Guid)
    pExcludeCredentialList: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST_head)
    dwEnterpriseAttestation: UInt32
    dwLargeBlobSupport: UInt32
    bPreferResidentKey: Windows.Win32.Foundation.BOOL
class WEBAUTHN_CLIENT_DATA(Structure):
    dwVersion: UInt32
    cbClientDataJSON: UInt32
    pbClientDataJSON: c_char_p_no
    pwszHashAlgId: Windows.Win32.Foundation.PWSTR
class WEBAUTHN_COMMON_ATTESTATION(Structure):
    dwVersion: UInt32
    pwszAlg: Windows.Win32.Foundation.PWSTR
    lAlg: Int32
    cbSignature: UInt32
    pbSignature: c_char_p_no
    cX5c: UInt32
    pX5c: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_X5C_head)
    pwszVer: Windows.Win32.Foundation.PWSTR
    cbCertInfo: UInt32
    pbCertInfo: c_char_p_no
    cbPubArea: UInt32
    pbPubArea: c_char_p_no
class WEBAUTHN_COSE_CREDENTIAL_PARAMETER(Structure):
    dwVersion: UInt32
    pwszCredentialType: Windows.Win32.Foundation.PWSTR
    lAlg: Int32
class WEBAUTHN_COSE_CREDENTIAL_PARAMETERS(Structure):
    cCredentialParameters: UInt32
    pCredentialParameters: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETER_head)
class WEBAUTHN_CREDENTIAL(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: c_char_p_no
    pwszCredentialType: Windows.Win32.Foundation.PWSTR
class WEBAUTHN_CREDENTIALS(Structure):
    cCredentials: UInt32
    pCredentials: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_head)
class WEBAUTHN_CREDENTIAL_ATTESTATION(Structure):
    dwVersion: UInt32
    pwszFormatType: Windows.Win32.Foundation.PWSTR
    cbAuthenticatorData: UInt32
    pbAuthenticatorData: c_char_p_no
    cbAttestation: UInt32
    pbAttestation: c_char_p_no
    dwAttestationDecodeType: UInt32
    pvAttestationDecode: c_void_p
    cbAttestationObject: UInt32
    pbAttestationObject: c_char_p_no
    cbCredentialId: UInt32
    pbCredentialId: c_char_p_no
    Extensions: Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwUsedTransport: UInt32
    bEpAtt: Windows.Win32.Foundation.BOOL
    bLargeBlobSupported: Windows.Win32.Foundation.BOOL
    bResidentKey: Windows.Win32.Foundation.BOOL
class WEBAUTHN_CREDENTIAL_EX(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: c_char_p_no
    pwszCredentialType: Windows.Win32.Foundation.PWSTR
    dwTransports: UInt32
class WEBAUTHN_CREDENTIAL_LIST(Structure):
    cCredentials: UInt32
    ppCredentials: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_EX_head))
class WEBAUTHN_CRED_BLOB_EXTENSION(Structure):
    cbCredBlob: UInt32
    pbCredBlob: c_char_p_no
class WEBAUTHN_CRED_PROTECT_EXTENSION_IN(Structure):
    dwCredProtect: UInt32
    bRequireCredProtect: Windows.Win32.Foundation.BOOL
class WEBAUTHN_EXTENSION(Structure):
    pwszExtensionIdentifier: Windows.Win32.Foundation.PWSTR
    cbExtension: UInt32
    pvExtension: c_void_p
class WEBAUTHN_EXTENSIONS(Structure):
    cExtensions: UInt32
    pExtensions: POINTER(Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSION_head)
class WEBAUTHN_RP_ENTITY_INFORMATION(Structure):
    dwVersion: UInt32
    pwszId: Windows.Win32.Foundation.PWSTR
    pwszName: Windows.Win32.Foundation.PWSTR
    pwszIcon: Windows.Win32.Foundation.PWSTR
class WEBAUTHN_USER_ENTITY_INFORMATION(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: c_char_p_no
    pwszName: Windows.Win32.Foundation.PWSTR
    pwszIcon: Windows.Win32.Foundation.PWSTR
    pwszDisplayName: Windows.Win32.Foundation.PWSTR
class WEBAUTHN_X5C(Structure):
    cbData: UInt32
    pbData: c_char_p_no
@winfunctype_pointer
def WS_ABANDON_MESSAGE_CALLBACK(channelInstance: c_void_p, message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ABORT_CHANNEL_CALLBACK(channelInstance: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ABORT_LISTENER_CALLBACK(listenerInstance: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ACCEPT_CHANNEL_CALLBACK(listenerInstance: c_void_p, channelInstance: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_ADDRESSING_VERSION = Int32
WS_ADDRESSING_VERSION_0_9: WS_ADDRESSING_VERSION = 1
WS_ADDRESSING_VERSION_1_0: WS_ADDRESSING_VERSION = 2
WS_ADDRESSING_VERSION_TRANSPORT: WS_ADDRESSING_VERSION = 3
class WS_ANY_ATTRIBUTE(Structure):
    localName: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    ns: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    value: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_head)
class WS_ANY_ATTRIBUTES(Structure):
    attributes: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ANY_ATTRIBUTE_head)
    attributeCount: UInt32
@winfunctype_pointer
def WS_ASYNC_CALLBACK(errorCode: Windows.Win32.Foundation.HRESULT, callbackModel: Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: c_void_p) -> Void: ...
class WS_ASYNC_CONTEXT(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CALLBACK
    callbackState: c_void_p
@winfunctype_pointer
def WS_ASYNC_FUNCTION(hr: Windows.Win32.Foundation.HRESULT, callbackModel: Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: c_void_p, next: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_OPERATION_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_ASYNC_OPERATION(Structure):
    function: Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_FUNCTION
class WS_ASYNC_STATE(Structure):
    internal0: c_void_p
    internal1: c_void_p
    internal2: c_void_p
    internal3: c_void_p
    internal4: c_void_p
class WS_ATTRIBUTE_DESCRIPTION(Structure):
    attributeLocalName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    attributeNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    type: Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: c_void_p
WS_BINDING_TEMPLATE_TYPE = Int32
WS_HTTP_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 0
WS_HTTP_SSL_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 1
WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 2
WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 3
WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 4
WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 5
WS_TCP_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 6
WS_TCP_SSPI_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 7
WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 8
WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 9
WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 10
WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 11
WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 12
WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: WS_BINDING_TEMPLATE_TYPE = 13
class WS_BOOL_DESCRIPTION(Structure):
    value: Windows.Win32.Foundation.BOOL
class WS_BUFFERS(Structure):
    bufferCount: UInt32
    buffers: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_BYTES_head)
class WS_BYTES(Structure):
    length: UInt32
    bytes: c_char_p_no
class WS_BYTES_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
class WS_BYTE_ARRAY_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
WS_CALLBACK_MODEL = Int32
WS_SHORT_CALLBACK: WS_CALLBACK_MODEL = 0
WS_LONG_CALLBACK: WS_CALLBACK_MODEL = 1
class WS_CALL_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_CALL_PROPERTY_ID = Int32
WS_CALL_PROPERTY_CHECK_MUST_UNDERSTAND: WS_CALL_PROPERTY_ID = 0
WS_CALL_PROPERTY_SEND_MESSAGE_CONTEXT: WS_CALL_PROPERTY_ID = 1
WS_CALL_PROPERTY_RECEIVE_MESSAGE_CONTEXT: WS_CALL_PROPERTY_ID = 2
WS_CALL_PROPERTY_CALL_ID: WS_CALL_PROPERTY_ID = 3
class WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    provider: UIntPtr
    keySpec: UInt32
@winfunctype_pointer
def WS_CERTIFICATE_VALIDATION_CALLBACK(certContext: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), state: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_CERTIFICATE_VALIDATION_CALLBACK
    state: c_void_p
class WS_CERT_CREDENTIAL(Structure):
    credentialType: Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE
WS_CERT_CREDENTIAL_TYPE = Int32
WS_SUBJECT_NAME_CERT_CREDENTIAL_TYPE: WS_CERT_CREDENTIAL_TYPE = 1
WS_THUMBPRINT_CERT_CREDENTIAL_TYPE: WS_CERT_CREDENTIAL_TYPE = 2
WS_CUSTOM_CERT_CREDENTIAL_TYPE: WS_CERT_CREDENTIAL_TYPE = 3
class WS_CERT_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    rawCertificateData: Windows.Win32.Networking.WindowsWebServices.WS_BYTES
@winfunctype_pointer
def WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK(certIssuerListNotificationCallbackState: c_void_p, issuerList: POINTER(Windows.Win32.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_CERT_SIGNED_SAML_AUTHENTICATOR(Structure):
    authenticator: Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR
    trustedIssuerCerts: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    trustedIssuerCertCount: UInt32
    decryptionCert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)
    samlValidator: Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_SAML_CALLBACK
    samlValidatorCallbackState: c_void_p
class WS_CHANNEL(Structure):
    pass
WS_CHANNEL_BINDING = Int32
WS_HTTP_CHANNEL_BINDING: WS_CHANNEL_BINDING = 0
WS_TCP_CHANNEL_BINDING: WS_CHANNEL_BINDING = 1
WS_UDP_CHANNEL_BINDING: WS_CHANNEL_BINDING = 2
WS_CUSTOM_CHANNEL_BINDING: WS_CHANNEL_BINDING = 3
WS_NAMEDPIPE_CHANNEL_BINDING: WS_CHANNEL_BINDING = 4
class WS_CHANNEL_DECODER(Structure):
    createContext: c_void_p
    createDecoderCallback: Windows.Win32.Networking.WindowsWebServices.WS_CREATE_DECODER_CALLBACK
    decoderGetContentTypeCallback: Windows.Win32.Networking.WindowsWebServices.WS_DECODER_GET_CONTENT_TYPE_CALLBACK
    decoderStartCallback: Windows.Win32.Networking.WindowsWebServices.WS_DECODER_START_CALLBACK
    decoderDecodeCallback: Windows.Win32.Networking.WindowsWebServices.WS_DECODER_DECODE_CALLBACK
    decoderEndCallback: Windows.Win32.Networking.WindowsWebServices.WS_DECODER_END_CALLBACK
    freeDecoderCallback: Windows.Win32.Networking.WindowsWebServices.WS_FREE_DECODER_CALLBACK
class WS_CHANNEL_ENCODER(Structure):
    createContext: c_void_p
    createEncoderCallback: Windows.Win32.Networking.WindowsWebServices.WS_CREATE_ENCODER_CALLBACK
    encoderGetContentTypeCallback: Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_GET_CONTENT_TYPE_CALLBACK
    encoderStartCallback: Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_START_CALLBACK
    encoderEncodeCallback: Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_ENCODE_CALLBACK
    encoderEndCallback: Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_END_CALLBACK
    freeEncoderCallback: Windows.Win32.Networking.WindowsWebServices.WS_FREE_ENCODER_CALLBACK
class WS_CHANNEL_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head)
    propertyCount: UInt32
class WS_CHANNEL_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
class WS_CHANNEL_PROPERTY_CONSTRAINT(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID
    allowedValues: c_void_p
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        channelProperty: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY
WS_CHANNEL_PROPERTY_ID = Int32
WS_CHANNEL_PROPERTY_MAX_BUFFERED_MESSAGE_SIZE: WS_CHANNEL_PROPERTY_ID = 0
WS_CHANNEL_PROPERTY_MAX_STREAMED_MESSAGE_SIZE: WS_CHANNEL_PROPERTY_ID = 1
WS_CHANNEL_PROPERTY_MAX_STREAMED_START_SIZE: WS_CHANNEL_PROPERTY_ID = 2
WS_CHANNEL_PROPERTY_MAX_STREAMED_FLUSH_SIZE: WS_CHANNEL_PROPERTY_ID = 3
WS_CHANNEL_PROPERTY_ENCODING: WS_CHANNEL_PROPERTY_ID = 4
WS_CHANNEL_PROPERTY_ENVELOPE_VERSION: WS_CHANNEL_PROPERTY_ID = 5
WS_CHANNEL_PROPERTY_ADDRESSING_VERSION: WS_CHANNEL_PROPERTY_ID = 6
WS_CHANNEL_PROPERTY_MAX_SESSION_DICTIONARY_SIZE: WS_CHANNEL_PROPERTY_ID = 7
WS_CHANNEL_PROPERTY_STATE: WS_CHANNEL_PROPERTY_ID = 8
WS_CHANNEL_PROPERTY_ASYNC_CALLBACK_MODEL: WS_CHANNEL_PROPERTY_ID = 9
WS_CHANNEL_PROPERTY_IP_VERSION: WS_CHANNEL_PROPERTY_ID = 10
WS_CHANNEL_PROPERTY_RESOLVE_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 11
WS_CHANNEL_PROPERTY_CONNECT_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 12
WS_CHANNEL_PROPERTY_SEND_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 13
WS_CHANNEL_PROPERTY_RECEIVE_RESPONSE_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 14
WS_CHANNEL_PROPERTY_RECEIVE_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 15
WS_CHANNEL_PROPERTY_CLOSE_TIMEOUT: WS_CHANNEL_PROPERTY_ID = 16
WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS: WS_CHANNEL_PROPERTY_ID = 17
WS_CHANNEL_PROPERTY_TRANSFER_MODE: WS_CHANNEL_PROPERTY_ID = 18
WS_CHANNEL_PROPERTY_MULTICAST_INTERFACE: WS_CHANNEL_PROPERTY_ID = 19
WS_CHANNEL_PROPERTY_MULTICAST_HOPS: WS_CHANNEL_PROPERTY_ID = 20
WS_CHANNEL_PROPERTY_REMOTE_ADDRESS: WS_CHANNEL_PROPERTY_ID = 21
WS_CHANNEL_PROPERTY_REMOTE_IP_ADDRESS: WS_CHANNEL_PROPERTY_ID = 22
WS_CHANNEL_PROPERTY_HTTP_CONNECTION_ID: WS_CHANNEL_PROPERTY_ID = 23
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_CALLBACKS: WS_CHANNEL_PROPERTY_ID = 24
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS: WS_CHANNEL_PROPERTY_ID = 25
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_INSTANCE: WS_CHANNEL_PROPERTY_ID = 26
WS_CHANNEL_PROPERTY_TRANSPORT_URL: WS_CHANNEL_PROPERTY_ID = 27
WS_CHANNEL_PROPERTY_NO_DELAY: WS_CHANNEL_PROPERTY_ID = 28
WS_CHANNEL_PROPERTY_SEND_KEEP_ALIVES: WS_CHANNEL_PROPERTY_ID = 29
WS_CHANNEL_PROPERTY_KEEP_ALIVE_TIME: WS_CHANNEL_PROPERTY_ID = 30
WS_CHANNEL_PROPERTY_KEEP_ALIVE_INTERVAL: WS_CHANNEL_PROPERTY_ID = 31
WS_CHANNEL_PROPERTY_MAX_HTTP_SERVER_CONNECTIONS: WS_CHANNEL_PROPERTY_ID = 32
WS_CHANNEL_PROPERTY_IS_SESSION_SHUT_DOWN: WS_CHANNEL_PROPERTY_ID = 33
WS_CHANNEL_PROPERTY_CHANNEL_TYPE: WS_CHANNEL_PROPERTY_ID = 34
WS_CHANNEL_PROPERTY_TRIM_BUFFERED_MESSAGE_SIZE: WS_CHANNEL_PROPERTY_ID = 35
WS_CHANNEL_PROPERTY_ENCODER: WS_CHANNEL_PROPERTY_ID = 36
WS_CHANNEL_PROPERTY_DECODER: WS_CHANNEL_PROPERTY_ID = 37
WS_CHANNEL_PROPERTY_PROTECTION_LEVEL: WS_CHANNEL_PROPERTY_ID = 38
WS_CHANNEL_PROPERTY_COOKIE_MODE: WS_CHANNEL_PROPERTY_ID = 39
WS_CHANNEL_PROPERTY_HTTP_PROXY_SETTING_MODE: WS_CHANNEL_PROPERTY_ID = 40
WS_CHANNEL_PROPERTY_CUSTOM_HTTP_PROXY: WS_CHANNEL_PROPERTY_ID = 41
WS_CHANNEL_PROPERTY_HTTP_MESSAGE_MAPPING: WS_CHANNEL_PROPERTY_ID = 42
WS_CHANNEL_PROPERTY_ENABLE_HTTP_REDIRECT: WS_CHANNEL_PROPERTY_ID = 43
WS_CHANNEL_PROPERTY_HTTP_REDIRECT_CALLBACK_CONTEXT: WS_CHANNEL_PROPERTY_ID = 44
WS_CHANNEL_PROPERTY_FAULTS_AS_ERRORS: WS_CHANNEL_PROPERTY_ID = 45
WS_CHANNEL_PROPERTY_ALLOW_UNSECURED_FAULTS: WS_CHANNEL_PROPERTY_ID = 46
WS_CHANNEL_PROPERTY_HTTP_SERVER_SPN: WS_CHANNEL_PROPERTY_ID = 47
WS_CHANNEL_PROPERTY_HTTP_PROXY_SPN: WS_CHANNEL_PROPERTY_ID = 48
WS_CHANNEL_PROPERTY_MAX_HTTP_REQUEST_HEADERS_BUFFER_SIZE: WS_CHANNEL_PROPERTY_ID = 49
WS_CHANNEL_STATE = Int32
WS_CHANNEL_STATE_CREATED: WS_CHANNEL_STATE = 0
WS_CHANNEL_STATE_OPENING: WS_CHANNEL_STATE = 1
WS_CHANNEL_STATE_ACCEPTING: WS_CHANNEL_STATE = 2
WS_CHANNEL_STATE_OPEN: WS_CHANNEL_STATE = 3
WS_CHANNEL_STATE_FAULTED: WS_CHANNEL_STATE = 4
WS_CHANNEL_STATE_CLOSING: WS_CHANNEL_STATE = 5
WS_CHANNEL_STATE_CLOSED: WS_CHANNEL_STATE = 6
WS_CHANNEL_TYPE = Int32
WS_CHANNEL_TYPE_INPUT: WS_CHANNEL_TYPE = 1
WS_CHANNEL_TYPE_OUTPUT: WS_CHANNEL_TYPE = 2
WS_CHANNEL_TYPE_SESSION: WS_CHANNEL_TYPE = 4
WS_CHANNEL_TYPE_INPUT_SESSION: WS_CHANNEL_TYPE = 5
WS_CHANNEL_TYPE_OUTPUT_SESSION: WS_CHANNEL_TYPE = 6
WS_CHANNEL_TYPE_DUPLEX: WS_CHANNEL_TYPE = 3
WS_CHANNEL_TYPE_DUPLEX_SESSION: WS_CHANNEL_TYPE = 7
WS_CHANNEL_TYPE_REQUEST: WS_CHANNEL_TYPE = 8
WS_CHANNEL_TYPE_REPLY: WS_CHANNEL_TYPE = 16
WS_CHARSET = Int32
WS_CHARSET_AUTO: WS_CHARSET = 0
WS_CHARSET_UTF8: WS_CHARSET = 1
WS_CHARSET_UTF16LE: WS_CHARSET = 2
WS_CHARSET_UTF16BE: WS_CHARSET = 3
class WS_CHAR_ARRAY_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
@winfunctype_pointer
def WS_CLOSE_CHANNEL_CALLBACK(channelInstance: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CLOSE_LISTENER_CALLBACK(listenerInstance: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_CONTRACT_DESCRIPTION(Structure):
    operationCount: UInt32
    operations: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION_head))
WS_COOKIE_MODE = Int32
WS_MANUAL_COOKIE_MODE: WS_COOKIE_MODE = 1
WS_AUTO_COOKIE_MODE: WS_COOKIE_MODE = 2
@winfunctype_pointer
def WS_CREATE_CHANNEL_CALLBACK(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelParameters: c_void_p, channelParametersSize: UInt32, channelInstance: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK(listenerInstance: c_void_p, channelParameters: c_void_p, channelParametersSize: UInt32, channelInstance: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_DECODER_CALLBACK(createContext: c_void_p, readCallback: Windows.Win32.Networking.WindowsWebServices.WS_READ_CALLBACK, readContext: c_void_p, decoderContext: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_ENCODER_CALLBACK(createContext: c_void_p, writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeContext: c_void_p, encoderContext: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_LISTENER_CALLBACK(channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, listenerParameters: c_void_p, listenerParametersSize: UInt32, listenerInstance: POINTER(c_void_p), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_CUSTOM_CERT_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    getCertCallback: Windows.Win32.Networking.WindowsWebServices.WS_GET_CERT_CALLBACK
    getCertCallbackState: c_void_p
    certIssuerListNotificationCallback: Windows.Win32.Networking.WindowsWebServices.WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK
    certIssuerListNotificationCallbackState: c_void_p
class WS_CUSTOM_CHANNEL_CALLBACKS(Structure):
    createChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_CREATE_CHANNEL_CALLBACK
    freeChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_FREE_CHANNEL_CALLBACK
    resetChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_RESET_CHANNEL_CALLBACK
    openChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_OPEN_CHANNEL_CALLBACK
    closeChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_CLOSE_CHANNEL_CALLBACK
    abortChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_ABORT_CHANNEL_CALLBACK
    getChannelPropertyCallback: Windows.Win32.Networking.WindowsWebServices.WS_GET_CHANNEL_PROPERTY_CALLBACK
    setChannelPropertyCallback: Windows.Win32.Networking.WindowsWebServices.WS_SET_CHANNEL_PROPERTY_CALLBACK
    writeMessageStartCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_MESSAGE_START_CALLBACK
    writeMessageEndCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_MESSAGE_END_CALLBACK
    readMessageStartCallback: Windows.Win32.Networking.WindowsWebServices.WS_READ_MESSAGE_START_CALLBACK
    readMessageEndCallback: Windows.Win32.Networking.WindowsWebServices.WS_READ_MESSAGE_END_CALLBACK
    abandonMessageCallback: Windows.Win32.Networking.WindowsWebServices.WS_ABANDON_MESSAGE_CALLBACK
    shutdownSessionChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK
class WS_CUSTOM_HTTP_PROXY(Structure):
    servers: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    bypass: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_CUSTOM_LISTENER_CALLBACKS(Structure):
    createListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_CREATE_LISTENER_CALLBACK
    freeListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_FREE_LISTENER_CALLBACK
    resetListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_RESET_LISTENER_CALLBACK
    openListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_OPEN_LISTENER_CALLBACK
    closeListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_CLOSE_LISTENER_CALLBACK
    abortListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_ABORT_LISTENER_CALLBACK
    getListenerPropertyCallback: Windows.Win32.Networking.WindowsWebServices.WS_GET_LISTENER_PROPERTY_CALLBACK
    setListenerPropertyCallback: Windows.Win32.Networking.WindowsWebServices.WS_SET_LISTENER_PROPERTY_CALLBACK
    createChannelForListenerCallback: Windows.Win32.Networking.WindowsWebServices.WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK
    acceptChannelCallback: Windows.Win32.Networking.WindowsWebServices.WS_ACCEPT_CHANNEL_CALLBACK
class WS_CUSTOM_TYPE_DESCRIPTION(Structure):
    size: UInt32
    alignment: UInt32
    readCallback: Windows.Win32.Networking.WindowsWebServices.WS_READ_TYPE_CALLBACK
    writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_TYPE_CALLBACK
    descriptionData: c_void_p
    isDefaultValueCallback: Windows.Win32.Networking.WindowsWebServices.WS_IS_DEFAULT_VALUE_CALLBACK
class WS_DATETIME(Structure):
    ticks: UInt64
    format: Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_FORMAT
class WS_DATETIME_DESCRIPTION(Structure):
    minValue: Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
    maxValue: Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
WS_DATETIME_FORMAT = Int32
WS_DATETIME_FORMAT_UTC: WS_DATETIME_FORMAT = 0
WS_DATETIME_FORMAT_LOCAL: WS_DATETIME_FORMAT = 1
WS_DATETIME_FORMAT_NONE: WS_DATETIME_FORMAT = 2
class WS_DECIMAL_DESCRIPTION(Structure):
    minValue: Windows.Win32.Foundation.DECIMAL
    maxValue: Windows.Win32.Foundation.DECIMAL
@winfunctype_pointer
def WS_DECODER_DECODE_CALLBACK(encoderContext: c_void_p, buffer: c_void_p, maxLength: UInt32, length: POINTER(UInt32), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_END_CALLBACK(encoderContext: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_GET_CONTENT_TYPE_CALLBACK(decoderContext: c_void_p, contentType: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), contentEncoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), newContentType: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_START_CALLBACK(encoderContext: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_DEFAULT_VALUE(Structure):
    value: c_void_p
    valueSize: UInt32
class WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
class WS_DISALLOWED_USER_AGENT_SUBSTRINGS(Structure):
    subStringCount: UInt32
    subStrings: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head))
class WS_DNS_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    dns: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_DOUBLE_DESCRIPTION(Structure):
    minValue: Double
    maxValue: Double
class WS_DURATION(Structure):
    negative: Windows.Win32.Foundation.BOOL
    years: UInt32
    months: UInt32
    days: UInt32
    hours: UInt32
    minutes: UInt32
    seconds: UInt32
    milliseconds: UInt32
    ticks: UInt32
@winfunctype_pointer
def WS_DURATION_COMPARISON_CALLBACK(duration1: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_DURATION_head), duration2: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_DURATION_head), result: POINTER(Int32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_DURATION_DESCRIPTION(Structure):
    minValue: Windows.Win32.Networking.WindowsWebServices.WS_DURATION
    maxValue: Windows.Win32.Networking.WindowsWebServices.WS_DURATION
    comparer: Windows.Win32.Networking.WindowsWebServices.WS_DURATION_COMPARISON_CALLBACK
@winfunctype_pointer
def WS_DYNAMIC_STRING_CALLBACK(callbackState: c_void_p, string: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head), found: POINTER(Windows.Win32.Foundation.BOOL), id: POINTER(UInt32), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_ELEMENT_DESCRIPTION(Structure):
    elementLocalName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    elementNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    type: Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: c_void_p
@winfunctype_pointer
def WS_ENCODER_ENCODE_CALLBACK(encoderContext: c_void_p, buffers: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_BYTES_head), count: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_END_CALLBACK(encoderContext: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_GET_CONTENT_TYPE_CALLBACK(encoderContext: c_void_p, contentType: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), newContentType: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), contentEncoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_START_CALLBACK(encoderContext: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_ENCODING = Int32
WS_ENCODING_XML_BINARY_1: WS_ENCODING = 0
WS_ENCODING_XML_BINARY_SESSION_1: WS_ENCODING = 1
WS_ENCODING_XML_MTOM_UTF8: WS_ENCODING = 2
WS_ENCODING_XML_MTOM_UTF16BE: WS_ENCODING = 3
WS_ENCODING_XML_MTOM_UTF16LE: WS_ENCODING = 4
WS_ENCODING_XML_UTF8: WS_ENCODING = 5
WS_ENCODING_XML_UTF16BE: WS_ENCODING = 6
WS_ENCODING_XML_UTF16LE: WS_ENCODING = 7
WS_ENCODING_RAW: WS_ENCODING = 8
class WS_ENDPOINT_ADDRESS(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    headers: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
    extensions: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
    identity: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_head)
class WS_ENDPOINT_ADDRESS_DESCRIPTION(Structure):
    addressingVersion: Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION
WS_ENDPOINT_ADDRESS_EXTENSION_TYPE = Int32
WS_ENDPOINT_ADDRESS_EXTENSION_METADATA_ADDRESS: WS_ENDPOINT_ADDRESS_EXTENSION_TYPE = 1
class WS_ENDPOINT_IDENTITY(Structure):
    identityType: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE
WS_ENDPOINT_IDENTITY_TYPE = Int32
WS_DNS_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 1
WS_UPN_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 2
WS_SPN_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 3
WS_RSA_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 4
WS_CERT_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 5
WS_UNKNOWN_ENDPOINT_IDENTITY_TYPE: WS_ENDPOINT_IDENTITY_TYPE = 6
class WS_ENDPOINT_POLICY_EXTENSION(Structure):
    policyExtension: Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION
    assertionName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    assertionNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        assertionValue: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
class WS_ENUM_DESCRIPTION(Structure):
    values: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENUM_VALUE_head)
    valueCount: UInt32
    maxByteCount: UInt32
    nameIndices: POINTER(UInt32)
class WS_ENUM_VALUE(Structure):
    value: Int32
    name: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
WS_ENVELOPE_VERSION = Int32
WS_ENVELOPE_VERSION_SOAP_1_1: WS_ENVELOPE_VERSION = 1
WS_ENVELOPE_VERSION_SOAP_1_2: WS_ENVELOPE_VERSION = 2
WS_ENVELOPE_VERSION_NONE: WS_ENVELOPE_VERSION = 3
class WS_ERROR(Structure):
    pass
class WS_ERROR_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_ERROR_PROPERTY_ID = Int32
WS_ERROR_PROPERTY_STRING_COUNT: WS_ERROR_PROPERTY_ID = 0
WS_ERROR_PROPERTY_ORIGINAL_ERROR_CODE: WS_ERROR_PROPERTY_ID = 1
WS_ERROR_PROPERTY_LANGID: WS_ERROR_PROPERTY_ID = 2
WS_EXCEPTION_CODE = Int32
WS_EXCEPTION_CODE_USAGE_FAILURE: WS_EXCEPTION_CODE = -1069744128
WS_EXCEPTION_CODE_INTERNAL_FAILURE: WS_EXCEPTION_CODE = -1069744127
WS_EXTENDED_PROTECTION_POLICY = Int32
WS_EXTENDED_PROTECTION_POLICY_NEVER: WS_EXTENDED_PROTECTION_POLICY = 1
WS_EXTENDED_PROTECTION_POLICY_WHEN_SUPPORTED: WS_EXTENDED_PROTECTION_POLICY = 2
WS_EXTENDED_PROTECTION_POLICY_ALWAYS: WS_EXTENDED_PROTECTION_POLICY = 3
WS_EXTENDED_PROTECTION_SCENARIO = Int32
WS_EXTENDED_PROTECTION_SCENARIO_BOUND_SERVER: WS_EXTENDED_PROTECTION_SCENARIO = 1
WS_EXTENDED_PROTECTION_SCENARIO_TERMINATED_SSL: WS_EXTENDED_PROTECTION_SCENARIO = 2
class WS_FAULT(Structure):
    code: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_CODE_head)
    reasons: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_REASON_head)
    reasonCount: UInt32
    actor: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    node: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    detail: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
class WS_FAULT_CODE(Structure):
    value: Windows.Win32.Networking.WindowsWebServices.WS_XML_QNAME
    subCode: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FAULT_CODE_head)
class WS_FAULT_DESCRIPTION(Structure):
    envelopeVersion: Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION
class WS_FAULT_DETAIL_DESCRIPTION(Structure):
    action: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    detailElementDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head)
WS_FAULT_DISCLOSURE = Int32
WS_MINIMAL_FAULT_DISCLOSURE: WS_FAULT_DISCLOSURE = 0
WS_FULL_FAULT_DISCLOSURE: WS_FAULT_DISCLOSURE = 1
WS_FAULT_ERROR_PROPERTY_ID = Int32
WS_FAULT_ERROR_PROPERTY_FAULT: WS_FAULT_ERROR_PROPERTY_ID = 0
WS_FAULT_ERROR_PROPERTY_ACTION: WS_FAULT_ERROR_PROPERTY_ID = 1
WS_FAULT_ERROR_PROPERTY_HEADER: WS_FAULT_ERROR_PROPERTY_ID = 2
class WS_FAULT_REASON(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    lang: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_FIELD_DESCRIPTION(Structure):
    mapping: Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING
    localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    type: Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: c_void_p
    offset: UInt32
    options: UInt32
    defaultValue: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_DEFAULT_VALUE_head)
    countOffset: UInt32
    itemLocalName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    itemNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    itemRange: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ITEM_RANGE_head)
WS_FIELD_MAPPING = Int32
WS_TYPE_ATTRIBUTE_FIELD_MAPPING: WS_FIELD_MAPPING = 0
WS_ATTRIBUTE_FIELD_MAPPING: WS_FIELD_MAPPING = 1
WS_ELEMENT_FIELD_MAPPING: WS_FIELD_MAPPING = 2
WS_REPEATING_ELEMENT_FIELD_MAPPING: WS_FIELD_MAPPING = 3
WS_TEXT_FIELD_MAPPING: WS_FIELD_MAPPING = 4
WS_NO_FIELD_MAPPING: WS_FIELD_MAPPING = 5
WS_XML_ATTRIBUTE_FIELD_MAPPING: WS_FIELD_MAPPING = 6
WS_ELEMENT_CHOICE_FIELD_MAPPING: WS_FIELD_MAPPING = 7
WS_REPEATING_ELEMENT_CHOICE_FIELD_MAPPING: WS_FIELD_MAPPING = 8
WS_ANY_ELEMENT_FIELD_MAPPING: WS_FIELD_MAPPING = 9
WS_REPEATING_ANY_ELEMENT_FIELD_MAPPING: WS_FIELD_MAPPING = 10
WS_ANY_CONTENT_FIELD_MAPPING: WS_FIELD_MAPPING = 11
WS_ANY_ATTRIBUTES_FIELD_MAPPING: WS_FIELD_MAPPING = 12
class WS_FLOAT_DESCRIPTION(Structure):
    minValue: Single
    maxValue: Single
@winfunctype_pointer
def WS_FREE_CHANNEL_CALLBACK(channelInstance: c_void_p) -> Void: ...
@winfunctype_pointer
def WS_FREE_DECODER_CALLBACK(decoderContext: c_void_p) -> Void: ...
@winfunctype_pointer
def WS_FREE_ENCODER_CALLBACK(encoderContext: c_void_p) -> Void: ...
@winfunctype_pointer
def WS_FREE_LISTENER_CALLBACK(listenerInstance: c_void_p) -> Void: ...
@winfunctype_pointer
def WS_GET_CERT_CALLBACK(getCertCallbackState: c_void_p, targetAddress: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), viaUri: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), cert: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head)), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_GET_CHANNEL_PROPERTY_CALLBACK(channelInstance: c_void_p, id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_GET_LISTENER_PROPERTY_CALLBACK(listenerInstance: c_void_p, id: Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_GUID_DESCRIPTION(Structure):
    value: Guid
WS_HEADER_TYPE = Int32
WS_ACTION_HEADER: WS_HEADER_TYPE = 1
WS_TO_HEADER: WS_HEADER_TYPE = 2
WS_MESSAGE_ID_HEADER: WS_HEADER_TYPE = 3
WS_RELATES_TO_HEADER: WS_HEADER_TYPE = 4
WS_FROM_HEADER: WS_HEADER_TYPE = 5
WS_REPLY_TO_HEADER: WS_HEADER_TYPE = 6
WS_FAULT_TO_HEADER: WS_HEADER_TYPE = 7
class WS_HEAP(Structure):
    pass
class WS_HEAP_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_head)
    propertyCount: UInt32
class WS_HEAP_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_HEAP_PROPERTY_ID = Int32
WS_HEAP_PROPERTY_MAX_SIZE: WS_HEAP_PROPERTY_ID = 0
WS_HEAP_PROPERTY_TRIM_SIZE: WS_HEAP_PROPERTY_ID = 1
WS_HEAP_PROPERTY_REQUESTED_SIZE: WS_HEAP_PROPERTY_ID = 2
WS_HEAP_PROPERTY_ACTUAL_SIZE: WS_HEAP_PROPERTY_ID = 3
class WS_HOST_NAMES(Structure):
    hostNames: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)
    hostNameCount: UInt32
class WS_HTTPS_URL(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_HTTP_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    httpHeaderAuthSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
class WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    httpHeaderAuthSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
WS_HTTP_HEADER_AUTH_TARGET = Int32
WS_HTTP_HEADER_AUTH_TARGET_SERVICE: WS_HTTP_HEADER_AUTH_TARGET = 1
WS_HTTP_HEADER_AUTH_TARGET_PROXY: WS_HTTP_HEADER_AUTH_TARGET = 2
class WS_HTTP_HEADER_MAPPING(Structure):
    headerName: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    headerMappingOptions: UInt32
class WS_HTTP_MESSAGE_MAPPING(Structure):
    requestMappingOptions: UInt32
    responseMappingOptions: UInt32
    requestHeaderMappings: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING_head))
    requestHeaderMappingCount: UInt32
    responseHeaderMappings: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING_head))
    responseHeaderMappingCount: UInt32
class WS_HTTP_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
WS_HTTP_PROXY_SETTING_MODE = Int32
WS_HTTP_PROXY_SETTING_MODE_AUTO: WS_HTTP_PROXY_SETTING_MODE = 1
WS_HTTP_PROXY_SETTING_MODE_NONE: WS_HTTP_PROXY_SETTING_MODE = 2
WS_HTTP_PROXY_SETTING_MODE_CUSTOM: WS_HTTP_PROXY_SETTING_MODE = 3
@winfunctype_pointer
def WS_HTTP_REDIRECT_CALLBACK(state: c_void_p, originalUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), newUrl: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_HTTP_REDIRECT_CALLBACK_CONTEXT(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_HTTP_REDIRECT_CALLBACK
    state: c_void_p
class WS_HTTP_SSL_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    httpHeaderAuthSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    httpHeaderAuthSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_URL(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_INT16_DESCRIPTION(Structure):
    minValue: Int16
    maxValue: Int16
class WS_INT32_DESCRIPTION(Structure):
    minValue: Int32
    maxValue: Int32
class WS_INT64_DESCRIPTION(Structure):
    minValue: Int64
    maxValue: Int64
class WS_INT8_DESCRIPTION(Structure):
    minValue: Windows.Win32.Foundation.CHAR
    maxValue: Windows.Win32.Foundation.CHAR
WS_IP_VERSION = Int32
WS_IP_VERSION_4: WS_IP_VERSION = 1
WS_IP_VERSION_6: WS_IP_VERSION = 2
WS_IP_VERSION_AUTO: WS_IP_VERSION = 3
class WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    claimConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    claimConstraintCount: UInt32
    requestSecurityTokenPropertyConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT_head)
    requestSecurityTokenPropertyConstraintCount: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        issuerAddress: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head)
        requestSecurityTokenTemplate: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
@winfunctype_pointer
def WS_IS_DEFAULT_VALUE_CALLBACK(descriptionData: c_void_p, value: c_void_p, defaultValue: c_void_p, valueSize: UInt32, isDefault: POINTER(Windows.Win32.Foundation.BOOL), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_ITEM_RANGE(Structure):
    minItemCount: UInt32
    maxItemCount: UInt32
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_LISTENER(Structure):
    pass
class WS_LISTENER_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_head)
    propertyCount: UInt32
class WS_LISTENER_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_LISTENER_PROPERTY_ID = Int32
WS_LISTENER_PROPERTY_LISTEN_BACKLOG: WS_LISTENER_PROPERTY_ID = 0
WS_LISTENER_PROPERTY_IP_VERSION: WS_LISTENER_PROPERTY_ID = 1
WS_LISTENER_PROPERTY_STATE: WS_LISTENER_PROPERTY_ID = 2
WS_LISTENER_PROPERTY_ASYNC_CALLBACK_MODEL: WS_LISTENER_PROPERTY_ID = 3
WS_LISTENER_PROPERTY_CHANNEL_TYPE: WS_LISTENER_PROPERTY_ID = 4
WS_LISTENER_PROPERTY_CHANNEL_BINDING: WS_LISTENER_PROPERTY_ID = 5
WS_LISTENER_PROPERTY_CONNECT_TIMEOUT: WS_LISTENER_PROPERTY_ID = 6
WS_LISTENER_PROPERTY_IS_MULTICAST: WS_LISTENER_PROPERTY_ID = 7
WS_LISTENER_PROPERTY_MULTICAST_INTERFACES: WS_LISTENER_PROPERTY_ID = 8
WS_LISTENER_PROPERTY_MULTICAST_LOOPBACK: WS_LISTENER_PROPERTY_ID = 9
WS_LISTENER_PROPERTY_CLOSE_TIMEOUT: WS_LISTENER_PROPERTY_ID = 10
WS_LISTENER_PROPERTY_TO_HEADER_MATCHING_OPTIONS: WS_LISTENER_PROPERTY_ID = 11
WS_LISTENER_PROPERTY_TRANSPORT_URL_MATCHING_OPTIONS: WS_LISTENER_PROPERTY_ID = 12
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_CALLBACKS: WS_LISTENER_PROPERTY_ID = 13
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_PARAMETERS: WS_LISTENER_PROPERTY_ID = 14
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_INSTANCE: WS_LISTENER_PROPERTY_ID = 15
WS_LISTENER_PROPERTY_DISALLOWED_USER_AGENT: WS_LISTENER_PROPERTY_ID = 16
WS_LISTENER_STATE = Int32
WS_LISTENER_STATE_CREATED: WS_LISTENER_STATE = 0
WS_LISTENER_STATE_OPENING: WS_LISTENER_STATE = 1
WS_LISTENER_STATE_OPEN: WS_LISTENER_STATE = 2
WS_LISTENER_STATE_FAULTED: WS_LISTENER_STATE = 3
WS_LISTENER_STATE_CLOSING: WS_LISTENER_STATE = 4
WS_LISTENER_STATE_CLOSED: WS_LISTENER_STATE = 5
class WS_MESSAGE(Structure):
    pass
class WS_MESSAGE_DESCRIPTION(Structure):
    action: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    bodyElementDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head)
@winfunctype_pointer
def WS_MESSAGE_DONE_CALLBACK(doneCallbackState: c_void_p) -> Void: ...
WS_MESSAGE_INITIALIZATION = Int32
WS_BLANK_MESSAGE: WS_MESSAGE_INITIALIZATION = 0
WS_DUPLICATE_MESSAGE: WS_MESSAGE_INITIALIZATION = 1
WS_REQUEST_MESSAGE: WS_MESSAGE_INITIALIZATION = 2
WS_REPLY_MESSAGE: WS_MESSAGE_INITIALIZATION = 3
WS_FAULT_MESSAGE: WS_MESSAGE_INITIALIZATION = 4
class WS_MESSAGE_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head)
    propertyCount: UInt32
class WS_MESSAGE_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_MESSAGE_PROPERTY_ID = Int32
WS_MESSAGE_PROPERTY_STATE: WS_MESSAGE_PROPERTY_ID = 0
WS_MESSAGE_PROPERTY_HEAP: WS_MESSAGE_PROPERTY_ID = 1
WS_MESSAGE_PROPERTY_ENVELOPE_VERSION: WS_MESSAGE_PROPERTY_ID = 2
WS_MESSAGE_PROPERTY_ADDRESSING_VERSION: WS_MESSAGE_PROPERTY_ID = 3
WS_MESSAGE_PROPERTY_HEADER_BUFFER: WS_MESSAGE_PROPERTY_ID = 4
WS_MESSAGE_PROPERTY_HEADER_POSITION: WS_MESSAGE_PROPERTY_ID = 5
WS_MESSAGE_PROPERTY_BODY_READER: WS_MESSAGE_PROPERTY_ID = 6
WS_MESSAGE_PROPERTY_BODY_WRITER: WS_MESSAGE_PROPERTY_ID = 7
WS_MESSAGE_PROPERTY_IS_ADDRESSED: WS_MESSAGE_PROPERTY_ID = 8
WS_MESSAGE_PROPERTY_HEAP_PROPERTIES: WS_MESSAGE_PROPERTY_ID = 9
WS_MESSAGE_PROPERTY_XML_READER_PROPERTIES: WS_MESSAGE_PROPERTY_ID = 10
WS_MESSAGE_PROPERTY_XML_WRITER_PROPERTIES: WS_MESSAGE_PROPERTY_ID = 11
WS_MESSAGE_PROPERTY_IS_FAULT: WS_MESSAGE_PROPERTY_ID = 12
WS_MESSAGE_PROPERTY_MAX_PROCESSED_HEADERS: WS_MESSAGE_PROPERTY_ID = 13
WS_MESSAGE_PROPERTY_USERNAME: WS_MESSAGE_PROPERTY_ID = 14
WS_MESSAGE_PROPERTY_ENCODED_CERT: WS_MESSAGE_PROPERTY_ID = 15
WS_MESSAGE_PROPERTY_TRANSPORT_SECURITY_WINDOWS_TOKEN: WS_MESSAGE_PROPERTY_ID = 16
WS_MESSAGE_PROPERTY_HTTP_HEADER_AUTH_WINDOWS_TOKEN: WS_MESSAGE_PROPERTY_ID = 17
WS_MESSAGE_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN: WS_MESSAGE_PROPERTY_ID = 18
WS_MESSAGE_PROPERTY_SAML_ASSERTION: WS_MESSAGE_PROPERTY_ID = 19
WS_MESSAGE_PROPERTY_SECURITY_CONTEXT: WS_MESSAGE_PROPERTY_ID = 20
WS_MESSAGE_PROPERTY_PROTECTION_LEVEL: WS_MESSAGE_PROPERTY_ID = 21
WS_MESSAGE_SECURITY_USAGE = Int32
WS_SUPPORTING_MESSAGE_SECURITY_USAGE: WS_MESSAGE_SECURITY_USAGE = 1
WS_MESSAGE_STATE = Int32
WS_MESSAGE_STATE_EMPTY: WS_MESSAGE_STATE = 1
WS_MESSAGE_STATE_INITIALIZED: WS_MESSAGE_STATE = 2
WS_MESSAGE_STATE_READING: WS_MESSAGE_STATE = 3
WS_MESSAGE_STATE_WRITING: WS_MESSAGE_STATE = 4
WS_MESSAGE_STATE_DONE: WS_MESSAGE_STATE = 5
class WS_METADATA(Structure):
    pass
class WS_METADATA_ENDPOINT(Structure):
    endpointAddress: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS
    endpointPolicy: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_head)
    portName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    serviceName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    serviceNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    bindingName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    bindingNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    portTypeName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    portTypeNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
class WS_METADATA_ENDPOINTS(Structure):
    endpoints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_METADATA_ENDPOINT_head)
    endpointCount: UInt32
WS_METADATA_EXCHANGE_TYPE = Int32
WS_METADATA_EXCHANGE_TYPE_NONE: WS_METADATA_EXCHANGE_TYPE = 0
WS_METADATA_EXCHANGE_TYPE_MEX: WS_METADATA_EXCHANGE_TYPE = 1
WS_METADATA_EXCHANGE_TYPE_HTTP_GET: WS_METADATA_EXCHANGE_TYPE = 2
class WS_METADATA_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_METADATA_PROPERTY_ID = Int32
WS_METADATA_PROPERTY_STATE: WS_METADATA_PROPERTY_ID = 1
WS_METADATA_PROPERTY_HEAP_PROPERTIES: WS_METADATA_PROPERTY_ID = 2
WS_METADATA_PROPERTY_POLICY_PROPERTIES: WS_METADATA_PROPERTY_ID = 3
WS_METADATA_PROPERTY_HEAP_REQUESTED_SIZE: WS_METADATA_PROPERTY_ID = 4
WS_METADATA_PROPERTY_MAX_DOCUMENTS: WS_METADATA_PROPERTY_ID = 5
WS_METADATA_PROPERTY_HOST_NAMES: WS_METADATA_PROPERTY_ID = 6
WS_METADATA_PROPERTY_VERIFY_HOST_NAMES: WS_METADATA_PROPERTY_ID = 7
WS_METADATA_STATE = Int32
WS_METADATA_STATE_CREATED: WS_METADATA_STATE = 1
WS_METADATA_STATE_RESOLVED: WS_METADATA_STATE = 2
WS_METADATA_STATE_FAULTED: WS_METADATA_STATE = 3
WS_MOVE_TO = Int32
WS_MOVE_TO_ROOT_ELEMENT: WS_MOVE_TO = 0
WS_MOVE_TO_NEXT_ELEMENT: WS_MOVE_TO = 1
WS_MOVE_TO_PREVIOUS_ELEMENT: WS_MOVE_TO = 2
WS_MOVE_TO_CHILD_ELEMENT: WS_MOVE_TO = 3
WS_MOVE_TO_END_ELEMENT: WS_MOVE_TO = 4
WS_MOVE_TO_PARENT_ELEMENT: WS_MOVE_TO = 5
WS_MOVE_TO_NEXT_NODE: WS_MOVE_TO = 6
WS_MOVE_TO_PREVIOUS_NODE: WS_MOVE_TO = 7
WS_MOVE_TO_FIRST_NODE: WS_MOVE_TO = 8
WS_MOVE_TO_BOF: WS_MOVE_TO = 9
WS_MOVE_TO_EOF: WS_MOVE_TO = 10
WS_MOVE_TO_CHILD_NODE: WS_MOVE_TO = 11
class WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    asymmetricKey: Windows.Win32.Security.Cryptography.NCRYPT_KEY_HANDLE
class WS_NETPIPE_URL(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_NETTCP_URL(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
    opaqueAuthIdentity: c_void_p
@winfunctype_pointer
def WS_OPEN_CHANNEL_CALLBACK(channelInstance: c_void_p, endpointAddress: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_OPEN_LISTENER_CALLBACK(listenerInstance: c_void_p, url: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_OPERATION_CANCEL_CALLBACK(reason: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CANCEL_REASON, state: c_void_p) -> Void: ...
class WS_OPERATION_CONTEXT(Structure):
    pass
WS_OPERATION_CONTEXT_PROPERTY_ID = Int32
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL: WS_OPERATION_CONTEXT_PROPERTY_ID = 0
WS_OPERATION_CONTEXT_PROPERTY_CONTRACT_DESCRIPTION: WS_OPERATION_CONTEXT_PROPERTY_ID = 1
WS_OPERATION_CONTEXT_PROPERTY_HOST_USER_STATE: WS_OPERATION_CONTEXT_PROPERTY_ID = 2
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE: WS_OPERATION_CONTEXT_PROPERTY_ID = 3
WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE: WS_OPERATION_CONTEXT_PROPERTY_ID = 4
WS_OPERATION_CONTEXT_PROPERTY_OUTPUT_MESSAGE: WS_OPERATION_CONTEXT_PROPERTY_ID = 5
WS_OPERATION_CONTEXT_PROPERTY_HEAP: WS_OPERATION_CONTEXT_PROPERTY_ID = 6
WS_OPERATION_CONTEXT_PROPERTY_LISTENER: WS_OPERATION_CONTEXT_PROPERTY_ID = 7
WS_OPERATION_CONTEXT_PROPERTY_ENDPOINT_ADDRESS: WS_OPERATION_CONTEXT_PROPERTY_ID = 8
class WS_OPERATION_DESCRIPTION(Structure):
    versionInfo: UInt32
    inputMessageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)
    outputMessageDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)
    inputMessageOptions: UInt32
    outputMessageOptions: UInt32
    parameterCount: UInt16
    parameterDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_DESCRIPTION_head)
    stubCallback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_STUB_CALLBACK
    style: Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_STYLE
@winfunctype_pointer
def WS_OPERATION_FREE_STATE_CALLBACK(state: c_void_p) -> Void: ...
WS_OPERATION_STYLE = Int32
WS_NON_RPC_LITERAL_OPERATION: WS_OPERATION_STYLE = 0
WS_RPC_LITERAL_OPERATION: WS_OPERATION_STYLE = 1
class WS_PARAMETER_DESCRIPTION(Structure):
    parameterType: Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE
    inputMessageIndex: UInt16
    outputMessageIndex: UInt16
WS_PARAMETER_TYPE = Int32
WS_PARAMETER_TYPE_NORMAL: WS_PARAMETER_TYPE = 0
WS_PARAMETER_TYPE_ARRAY: WS_PARAMETER_TYPE = 1
WS_PARAMETER_TYPE_ARRAY_COUNT: WS_PARAMETER_TYPE = 2
WS_PARAMETER_TYPE_MESSAGES: WS_PARAMETER_TYPE = 3
class WS_POLICY(Structure):
    pass
class WS_POLICY_CONSTRAINTS(Structure):
    channelBinding: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING
    channelPropertyConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_CONSTRAINT_head)
    channelPropertyConstraintCount: UInt32
    securityConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS_head)
    policyExtensions: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION_head))
    policyExtensionCount: UInt32
class WS_POLICY_EXTENSION(Structure):
    type: Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION_TYPE
WS_POLICY_EXTENSION_TYPE = Int32
WS_ENDPOINT_POLICY_EXTENSION_TYPE: WS_POLICY_EXTENSION_TYPE = 1
class WS_POLICY_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_head)
    propertyCount: UInt32
class WS_POLICY_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_POLICY_PROPERTY_ID = Int32
WS_POLICY_PROPERTY_STATE: WS_POLICY_PROPERTY_ID = 1
WS_POLICY_PROPERTY_MAX_ALTERNATIVES: WS_POLICY_PROPERTY_ID = 2
WS_POLICY_PROPERTY_MAX_DEPTH: WS_POLICY_PROPERTY_ID = 3
WS_POLICY_PROPERTY_MAX_EXTENSIONS: WS_POLICY_PROPERTY_ID = 4
WS_POLICY_STATE = Int32
WS_POLICY_STATE_CREATED: WS_POLICY_STATE = 1
WS_POLICY_STATE_FAULTED: WS_POLICY_STATE = 2
WS_PROTECTION_LEVEL = Int32
WS_PROTECTION_LEVEL_NONE: WS_PROTECTION_LEVEL = 1
WS_PROTECTION_LEVEL_SIGN: WS_PROTECTION_LEVEL = 2
WS_PROTECTION_LEVEL_SIGN_AND_ENCRYPT: WS_PROTECTION_LEVEL = 3
@winfunctype_pointer
def WS_PROXY_MESSAGE_CALLBACK(message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), state: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_PROXY_MESSAGE_CALLBACK_CONTEXT(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_PROXY_MESSAGE_CALLBACK
    state: c_void_p
class WS_PROXY_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_PROXY_PROPERTY_ID = Int32
WS_PROXY_PROPERTY_CALL_TIMEOUT: WS_PROXY_PROPERTY_ID = 0
WS_PROXY_PROPERTY_MESSAGE_PROPERTIES: WS_PROXY_PROPERTY_ID = 1
WS_PROXY_PROPERTY_MAX_CALL_POOL_SIZE: WS_PROXY_PROPERTY_ID = 2
WS_PROXY_PROPERTY_STATE: WS_PROXY_PROPERTY_ID = 3
WS_PROXY_PROPERTY_MAX_PENDING_CALLS: WS_PROXY_PROPERTY_ID = 4
WS_PROXY_PROPERTY_MAX_CLOSE_TIMEOUT: WS_PROXY_PROPERTY_ID = 5
WS_PROXY_FAULT_LANG_ID: WS_PROXY_PROPERTY_ID = 6
@winfunctype_pointer
def WS_PULL_BYTES_CALLBACK(callbackState: c_void_p, bytes: c_void_p, maxSize: UInt32, actualSize: POINTER(UInt32), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_PUSH_BYTES_CALLBACK(callbackState: c_void_p, writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    rawKeyBytes: Windows.Win32.Networking.WindowsWebServices.WS_BYTES
@winfunctype_pointer
def WS_READ_CALLBACK(callbackState: c_void_p, bytes: c_void_p, maxSize: UInt32, actualSize: POINTER(UInt32), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_READ_MESSAGE_END_CALLBACK(channelInstance: c_void_p, message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_READ_MESSAGE_START_CALLBACK(channelInstance: c_void_p, message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_READ_OPTION = Int32
WS_READ_REQUIRED_VALUE: WS_READ_OPTION = 1
WS_READ_REQUIRED_POINTER: WS_READ_OPTION = 2
WS_READ_OPTIONAL_POINTER: WS_READ_OPTION = 3
WS_READ_NILLABLE_POINTER: WS_READ_OPTION = 4
WS_READ_NILLABLE_VALUE: WS_READ_OPTION = 5
@winfunctype_pointer
def WS_READ_TYPE_CALLBACK(reader: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_head), typeMapping: Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, descriptionData: c_void_p, heap: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_HEAP_head), value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_RECEIVE_OPTION = Int32
WS_RECEIVE_REQUIRED_MESSAGE: WS_RECEIVE_OPTION = 1
WS_RECEIVE_OPTIONAL_MESSAGE: WS_RECEIVE_OPTION = 2
WS_REPEATING_HEADER_OPTION = Int32
WS_REPEATING_HEADER: WS_REPEATING_HEADER_OPTION = 1
WS_SINGLETON_HEADER: WS_REPEATING_HEADER_OPTION = 2
WS_REQUEST_SECURITY_TOKEN_ACTION = Int32
WS_REQUEST_SECURITY_TOKEN_ACTION_ISSUE: WS_REQUEST_SECURITY_TOKEN_ACTION = 1
WS_REQUEST_SECURITY_TOKEN_ACTION_NEW_CONTEXT: WS_REQUEST_SECURITY_TOKEN_ACTION = 2
WS_REQUEST_SECURITY_TOKEN_ACTION_RENEW_CONTEXT: WS_REQUEST_SECURITY_TOKEN_ACTION = 3
class WS_REQUEST_SECURITY_TOKEN_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
class WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID
    allowedValues: c_void_p
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        requestSecurityTokenProperty: Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_REQUEST_SECURITY_TOKEN_PROPERTY_APPLIES_TO: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 1
WS_REQUEST_SECURITY_TOKEN_PROPERTY_TRUST_VERSION: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 2
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SECURE_CONVERSATION_VERSION: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 3
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_TYPE: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 4
WS_REQUEST_SECURITY_TOKEN_PROPERTY_REQUEST_ACTION: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 5
WS_REQUEST_SECURITY_TOKEN_PROPERTY_EXISTING_TOKEN: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 6
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_TYPE: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 7
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_SIZE: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 8
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_ENTROPY: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 9
WS_REQUEST_SECURITY_TOKEN_PROPERTY_LOCAL_REQUEST_PARAMETERS: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 10
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SERVICE_REQUEST_PARAMETERS: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 11
WS_REQUEST_SECURITY_TOKEN_PROPERTY_MESSAGE_PROPERTIES: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 12
WS_REQUEST_SECURITY_TOKEN_PROPERTY_BEARER_KEY_TYPE_VERSION: WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 13
@winfunctype_pointer
def WS_RESET_CHANNEL_CALLBACK(channelInstance: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_RESET_LISTENER_CALLBACK(listenerInstance: c_void_p, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_RSA_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    modulus: Windows.Win32.Networking.WindowsWebServices.WS_BYTES
    exponent: Windows.Win32.Networking.WindowsWebServices.WS_BYTES
class WS_SAML_AUTHENTICATOR(Structure):
    authenticatorType: Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_TYPE
WS_SAML_AUTHENTICATOR_TYPE = Int32
WS_CERT_SIGNED_SAML_AUTHENTICATOR_TYPE: WS_SAML_AUTHENTICATOR_TYPE = 1
class WS_SAML_MESSAGE_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    authenticator: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_head)
WS_SECURE_CONVERSATION_VERSION = Int32
WS_SECURE_CONVERSATION_VERSION_FEBRUARY_2005: WS_SECURE_CONVERSATION_VERSION = 1
WS_SECURE_CONVERSATION_VERSION_1_3: WS_SECURE_CONVERSATION_VERSION = 2
WS_SECURE_PROTOCOL = Int32
WS_SECURE_PROTOCOL_SSL2: WS_SECURE_PROTOCOL = 1
WS_SECURE_PROTOCOL_SSL3: WS_SECURE_PROTOCOL = 2
WS_SECURE_PROTOCOL_TLS1_0: WS_SECURE_PROTOCOL = 4
WS_SECURE_PROTOCOL_TLS1_1: WS_SECURE_PROTOCOL = 8
WS_SECURE_PROTOCOL_TLS1_2: WS_SECURE_PROTOCOL = 16
WS_SECURITY_ALGORITHM_ID = Int32
WS_SECURITY_ALGORITHM_DEFAULT: WS_SECURITY_ALGORITHM_ID = 0
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE: WS_SECURITY_ALGORITHM_ID = 1
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE_WITH_COMMENTS: WS_SECURITY_ALGORITHM_ID = 2
WS_SECURITY_ALGORITHM_DIGEST_SHA1: WS_SECURITY_ALGORITHM_ID = 3
WS_SECURITY_ALGORITHM_DIGEST_SHA_256: WS_SECURITY_ALGORITHM_ID = 4
WS_SECURITY_ALGORITHM_DIGEST_SHA_384: WS_SECURITY_ALGORITHM_ID = 5
WS_SECURITY_ALGORITHM_DIGEST_SHA_512: WS_SECURITY_ALGORITHM_ID = 6
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA1: WS_SECURITY_ALGORITHM_ID = 7
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_256: WS_SECURITY_ALGORITHM_ID = 8
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_384: WS_SECURITY_ALGORITHM_ID = 9
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_512: WS_SECURITY_ALGORITHM_ID = 10
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA1: WS_SECURITY_ALGORITHM_ID = 11
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_DSA_SHA1: WS_SECURITY_ALGORITHM_ID = 12
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_256: WS_SECURITY_ALGORITHM_ID = 13
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_384: WS_SECURITY_ALGORITHM_ID = 14
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_512: WS_SECURITY_ALGORITHM_ID = 15
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_1_5: WS_SECURITY_ALGORITHM_ID = 16
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_OAEP: WS_SECURITY_ALGORITHM_ID = 17
WS_SECURITY_ALGORITHM_KEY_DERIVATION_P_SHA1: WS_SECURITY_ALGORITHM_ID = 18
class WS_SECURITY_ALGORITHM_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_SECURITY_ALGORITHM_PROPERTY_ID = Int32
class WS_SECURITY_ALGORITHM_SUITE(Structure):
    canonicalizationAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    digestAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    symmetricSignatureAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    asymmetricSignatureAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    encryptionAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    keyDerivationAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    symmetricKeyWrapAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    asymmetricKeyWrapAlgorithm: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    minSymmetricKeyLength: UInt32
    maxSymmetricKeyLength: UInt32
    minAsymmetricKeyLength: UInt32
    maxAsymmetricKeyLength: UInt32
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_head)
    propertyCount: UInt32
WS_SECURITY_ALGORITHM_SUITE_NAME = Int32
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256: WS_SECURITY_ALGORITHM_SUITE_NAME = 1
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192: WS_SECURITY_ALGORITHM_SUITE_NAME = 2
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128: WS_SECURITY_ALGORITHM_SUITE_NAME = 3
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 4
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 5
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 6
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256: WS_SECURITY_ALGORITHM_SUITE_NAME = 7
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256: WS_SECURITY_ALGORITHM_SUITE_NAME = 8
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256: WS_SECURITY_ALGORITHM_SUITE_NAME = 9
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 10
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 11
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256_RSA15: WS_SECURITY_ALGORITHM_SUITE_NAME = 12
WS_SECURITY_BEARER_KEY_TYPE_VERSION = Int32
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SPECIFICATION: WS_SECURITY_BEARER_KEY_TYPE_VERSION = 1
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SCHEMA: WS_SECURITY_BEARER_KEY_TYPE_VERSION = 2
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ERRATA_01: WS_SECURITY_BEARER_KEY_TYPE_VERSION = 3
class WS_SECURITY_BINDING(Structure):
    bindingType: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_head)
    propertyCount: UInt32
class WS_SECURITY_BINDING_CONSTRAINT(Structure):
    type: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE
    propertyConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_CONSTRAINT_head)
    propertyConstraintCount: UInt32
WS_SECURITY_BINDING_CONSTRAINT_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 5
WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 6
WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: WS_SECURITY_BINDING_CONSTRAINT_TYPE = 8
class WS_SECURITY_BINDING_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_head)
    propertyCount: UInt32
class WS_SECURITY_BINDING_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
class WS_SECURITY_BINDING_PROPERTY_CONSTRAINT(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID
    allowedValues: c_void_p
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        securityBindingProperty: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY
WS_SECURITY_BINDING_PROPERTY_ID = Int32
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SSL_CLIENT_CERT: WS_SECURITY_BINDING_PROPERTY_ID = 1
WS_SECURITY_BINDING_PROPERTY_WINDOWS_INTEGRATED_AUTH_PACKAGE: WS_SECURITY_BINDING_PROPERTY_ID = 2
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH: WS_SECURITY_BINDING_PROPERTY_ID = 3
WS_SECURITY_BINDING_PROPERTY_ALLOW_ANONYMOUS_CLIENTS: WS_SECURITY_BINDING_PROPERTY_ID = 4
WS_SECURITY_BINDING_PROPERTY_ALLOWED_IMPERSONATION_LEVEL: WS_SECURITY_BINDING_PROPERTY_ID = 5
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_SCHEME: WS_SECURITY_BINDING_PROPERTY_ID = 6
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_TARGET: WS_SECURITY_BINDING_PROPERTY_ID = 7
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_BASIC_REALM: WS_SECURITY_BINDING_PROPERTY_ID = 8
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_REALM: WS_SECURITY_BINDING_PROPERTY_ID = 9
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_DOMAIN: WS_SECURITY_BINDING_PROPERTY_ID = 10
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_SIZE: WS_SECURITY_BINDING_PROPERTY_ID = 11
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_ENTROPY_MODE: WS_SECURITY_BINDING_PROPERTY_ID = 12
WS_SECURITY_BINDING_PROPERTY_MESSAGE_PROPERTIES: WS_SECURITY_BINDING_PROPERTY_ID = 13
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_PENDING_CONTEXTS: WS_SECURITY_BINDING_PROPERTY_ID = 14
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_ACTIVE_CONTEXTS: WS_SECURITY_BINDING_PROPERTY_ID = 15
WS_SECURITY_BINDING_PROPERTY_SECURE_CONVERSATION_VERSION: WS_SECURITY_BINDING_PROPERTY_ID = 16
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_SUPPORT_RENEW: WS_SECURITY_BINDING_PROPERTY_ID = 17
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_RENEWAL_INTERVAL: WS_SECURITY_BINDING_PROPERTY_ID = 18
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_ROLLOVER_INTERVAL: WS_SECURITY_BINDING_PROPERTY_ID = 19
WS_SECURITY_BINDING_PROPERTY_CERT_FAILURES_TO_IGNORE: WS_SECURITY_BINDING_PROPERTY_ID = 20
WS_SECURITY_BINDING_PROPERTY_DISABLE_CERT_REVOCATION_CHECK: WS_SECURITY_BINDING_PROPERTY_ID = 21
WS_SECURITY_BINDING_PROPERTY_DISALLOWED_SECURE_PROTOCOLS: WS_SECURITY_BINDING_PROPERTY_ID = 22
WS_SECURITY_BINDING_PROPERTY_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT: WS_SECURITY_BINDING_PROPERTY_ID = 23
WS_SECURITY_BINDING_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 5
WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 6
WS_SAML_MESSAGE_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 8
WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_TYPE: WS_SECURITY_BINDING_TYPE = 9
class WS_SECURITY_CONSTRAINTS(Structure):
    securityPropertyConstraints: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_CONSTRAINT_head)
    securityPropertyConstraintCount: UInt32
    securityBindingConstraints: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_head))
    securityBindingConstraintCount: UInt32
class WS_SECURITY_CONTEXT(Structure):
    pass
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    bootstrapSecurityDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head)
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    bootstrapSecurityConstraint: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS_head)
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_SECURITY_CONTEXT_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_SECURITY_CONTEXT_PROPERTY_ID = Int32
WS_SECURITY_CONTEXT_PROPERTY_IDENTIFIER: WS_SECURITY_CONTEXT_PROPERTY_ID = 1
WS_SECURITY_CONTEXT_PROPERTY_USERNAME: WS_SECURITY_CONTEXT_PROPERTY_ID = 2
WS_SECURITY_CONTEXT_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN: WS_SECURITY_CONTEXT_PROPERTY_ID = 3
WS_SECURITY_CONTEXT_PROPERTY_SAML_ASSERTION: WS_SECURITY_CONTEXT_PROPERTY_ID = 4
class WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityContextMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
class WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE(Structure):
    securityContextMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
class WS_SECURITY_DESCRIPTION(Structure):
    securityBindings: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_head))
    securityBindingCount: UInt32
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_head)
    propertyCount: UInt32
WS_SECURITY_HEADER_LAYOUT = Int32
WS_SECURITY_HEADER_LAYOUT_STRICT: WS_SECURITY_HEADER_LAYOUT = 1
WS_SECURITY_HEADER_LAYOUT_LAX: WS_SECURITY_HEADER_LAYOUT = 2
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_FIRST: WS_SECURITY_HEADER_LAYOUT = 3
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_LAST: WS_SECURITY_HEADER_LAYOUT = 4
WS_SECURITY_HEADER_VERSION = Int32
WS_SECURITY_HEADER_VERSION_1_0: WS_SECURITY_HEADER_VERSION = 1
WS_SECURITY_HEADER_VERSION_1_1: WS_SECURITY_HEADER_VERSION = 2
WS_SECURITY_KEY_ENTROPY_MODE = Int32
WS_SECURITY_KEY_ENTROPY_MODE_CLIENT_ONLY: WS_SECURITY_KEY_ENTROPY_MODE = 1
WS_SECURITY_KEY_ENTROPY_MODE_SERVER_ONLY: WS_SECURITY_KEY_ENTROPY_MODE = 2
WS_SECURITY_KEY_ENTROPY_MODE_COMBINED: WS_SECURITY_KEY_ENTROPY_MODE = 3
class WS_SECURITY_KEY_HANDLE(Structure):
    keyHandleType: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE
WS_SECURITY_KEY_HANDLE_TYPE = Int32
WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_TYPE: WS_SECURITY_KEY_HANDLE_TYPE = 1
WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE: WS_SECURITY_KEY_HANDLE_TYPE = 2
WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE: WS_SECURITY_KEY_HANDLE_TYPE = 3
WS_SECURITY_KEY_TYPE = Int32
WS_SECURITY_KEY_TYPE_NONE: WS_SECURITY_KEY_TYPE = 1
WS_SECURITY_KEY_TYPE_SYMMETRIC: WS_SECURITY_KEY_TYPE = 2
WS_SECURITY_KEY_TYPE_ASYMMETRIC: WS_SECURITY_KEY_TYPE = 3
class WS_SECURITY_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_head)
    propertyCount: UInt32
class WS_SECURITY_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
class WS_SECURITY_PROPERTY_CONSTRAINT(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID
    allowedValues: c_void_p
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        securityProperty: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY
WS_SECURITY_PROPERTY_ID = Int32
WS_SECURITY_PROPERTY_TRANSPORT_PROTECTION_LEVEL: WS_SECURITY_PROPERTY_ID = 1
WS_SECURITY_PROPERTY_ALGORITHM_SUITE: WS_SECURITY_PROPERTY_ID = 2
WS_SECURITY_PROPERTY_ALGORITHM_SUITE_NAME: WS_SECURITY_PROPERTY_ID = 3
WS_SECURITY_PROPERTY_MAX_ALLOWED_LATENCY: WS_SECURITY_PROPERTY_ID = 4
WS_SECURITY_PROPERTY_TIMESTAMP_VALIDITY_DURATION: WS_SECURITY_PROPERTY_ID = 5
WS_SECURITY_PROPERTY_MAX_ALLOWED_CLOCK_SKEW: WS_SECURITY_PROPERTY_ID = 6
WS_SECURITY_PROPERTY_TIMESTAMP_USAGE: WS_SECURITY_PROPERTY_ID = 7
WS_SECURITY_PROPERTY_SECURITY_HEADER_LAYOUT: WS_SECURITY_PROPERTY_ID = 8
WS_SECURITY_PROPERTY_SECURITY_HEADER_VERSION: WS_SECURITY_PROPERTY_ID = 9
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_POLICY: WS_SECURITY_PROPERTY_ID = 10
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_SCENARIO: WS_SECURITY_PROPERTY_ID = 11
WS_SECURITY_PROPERTY_SERVICE_IDENTITIES: WS_SECURITY_PROPERTY_ID = 12
WS_SECURITY_TIMESTAMP_USAGE = Int32
WS_SECURITY_TIMESTAMP_USAGE_ALWAYS: WS_SECURITY_TIMESTAMP_USAGE = 1
WS_SECURITY_TIMESTAMP_USAGE_NEVER: WS_SECURITY_TIMESTAMP_USAGE = 2
WS_SECURITY_TIMESTAMP_USAGE_REQUESTS_ONLY: WS_SECURITY_TIMESTAMP_USAGE = 3
class WS_SECURITY_TOKEN(Structure):
    pass
WS_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_SECURITY_TOKEN_PROPERTY_KEY_TYPE: WS_SECURITY_TOKEN_PROPERTY_ID = 1
WS_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME: WS_SECURITY_TOKEN_PROPERTY_ID = 2
WS_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME: WS_SECURITY_TOKEN_PROPERTY_ID = 3
WS_SECURITY_TOKEN_PROPERTY_SERIALIZED_XML: WS_SECURITY_TOKEN_PROPERTY_ID = 4
WS_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE_XML: WS_SECURITY_TOKEN_PROPERTY_ID = 5
WS_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE_XML: WS_SECURITY_TOKEN_PROPERTY_ID = 6
WS_SECURITY_TOKEN_PROPERTY_SYMMETRIC_KEY: WS_SECURITY_TOKEN_PROPERTY_ID = 7
WS_SECURITY_TOKEN_REFERENCE_MODE = Int32
WS_SECURITY_TOKEN_REFERENCE_MODE_LOCAL_ID: WS_SECURITY_TOKEN_REFERENCE_MODE = 1
WS_SECURITY_TOKEN_REFERENCE_MODE_XML_BUFFER: WS_SECURITY_TOKEN_REFERENCE_MODE = 2
WS_SECURITY_TOKEN_REFERENCE_MODE_CERT_THUMBPRINT: WS_SECURITY_TOKEN_REFERENCE_MODE = 3
WS_SECURITY_TOKEN_REFERENCE_MODE_SECURITY_CONTEXT_ID: WS_SECURITY_TOKEN_REFERENCE_MODE = 4
WS_SECURITY_TOKEN_REFERENCE_MODE_SAML_ASSERTION_ID: WS_SECURITY_TOKEN_REFERENCE_MODE = 5
@winfunctype_pointer
def WS_SERVICE_ACCEPT_CHANNEL_CALLBACK(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), channelState: POINTER(c_void_p), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_SERVICE_CANCEL_REASON = Int32
WS_SERVICE_HOST_ABORT: WS_SERVICE_CANCEL_REASON = 0
WS_SERVICE_CHANNEL_FAULTED: WS_SERVICE_CANCEL_REASON = 1
@winfunctype_pointer
def WS_SERVICE_CLOSE_CHANNEL_CALLBACK(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_CONTRACT(Structure):
    contractDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CONTRACT_DESCRIPTION_head)
    defaultMessageHandlerCallback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_MESSAGE_RECEIVE_CALLBACK
    methodTable: c_void_p
class WS_SERVICE_ENDPOINT(Structure):
    address: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS
    channelBinding: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING
    channelType: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE
    securityDescription: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head)
    contract: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CONTRACT_head)
    authorizationCallback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_head)
    propertyCount: UInt32
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_SERVICE_ENDPOINT_METADATA(Structure):
    portName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    bindingName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    bindingNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
class WS_SERVICE_ENDPOINT_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_SERVICE_ENDPOINT_PROPERTY_ID = Int32
WS_SERVICE_ENDPOINT_PROPERTY_ACCEPT_CHANNEL_CALLBACK: WS_SERVICE_ENDPOINT_PROPERTY_ID = 0
WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK: WS_SERVICE_ENDPOINT_PROPERTY_ID = 1
WS_SERVICE_ENDPOINT_PROPERTY_MAX_ACCEPTING_CHANNELS: WS_SERVICE_ENDPOINT_PROPERTY_ID = 2
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CONCURRENCY: WS_SERVICE_ENDPOINT_PROPERTY_ID = 3
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_MAX_SIZE: WS_SERVICE_ENDPOINT_PROPERTY_ID = 4
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_TRIM_SIZE: WS_SERVICE_ENDPOINT_PROPERTY_ID = 5
WS_SERVICE_ENDPOINT_PROPERTY_MESSAGE_PROPERTIES: WS_SERVICE_ENDPOINT_PROPERTY_ID = 6
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CALL_POOL_SIZE: WS_SERVICE_ENDPOINT_PROPERTY_ID = 7
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNEL_POOL_SIZE: WS_SERVICE_ENDPOINT_PROPERTY_ID = 8
WS_SERVICE_ENDPOINT_PROPERTY_LISTENER_PROPERTIES: WS_SERVICE_ENDPOINT_PROPERTY_ID = 9
WS_SERVICE_ENDPOINT_PROPERTY_CHECK_MUST_UNDERSTAND: WS_SERVICE_ENDPOINT_PROPERTY_ID = 10
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE: WS_SERVICE_ENDPOINT_PROPERTY_ID = 11
WS_SERVICE_ENDPOINT_PROPERTY_METADATA: WS_SERVICE_ENDPOINT_PROPERTY_ID = 12
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX: WS_SERVICE_ENDPOINT_PROPERTY_ID = 13
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNELS: WS_SERVICE_ENDPOINT_PROPERTY_ID = 14
class WS_SERVICE_HOST(Structure):
    pass
WS_SERVICE_HOST_STATE = Int32
WS_SERVICE_HOST_STATE_CREATED: WS_SERVICE_HOST_STATE = 0
WS_SERVICE_HOST_STATE_OPENING: WS_SERVICE_HOST_STATE = 1
WS_SERVICE_HOST_STATE_OPEN: WS_SERVICE_HOST_STATE = 2
WS_SERVICE_HOST_STATE_CLOSING: WS_SERVICE_HOST_STATE = 3
WS_SERVICE_HOST_STATE_CLOSED: WS_SERVICE_HOST_STATE = 4
WS_SERVICE_HOST_STATE_FAULTED: WS_SERVICE_HOST_STATE = 5
@winfunctype_pointer
def WS_SERVICE_MESSAGE_RECEIVE_CALLBACK(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_METADATA(Structure):
    documentCount: UInt32
    documents: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_METADATA_DOCUMENT_head))
    serviceName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    serviceNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
class WS_SERVICE_METADATA_DOCUMENT(Structure):
    content: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    name: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)
class WS_SERVICE_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
class WS_SERVICE_PROPERTY_ACCEPT_CALLBACK(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ACCEPT_CHANNEL_CALLBACK
class WS_SERVICE_PROPERTY_CLOSE_CALLBACK(Structure):
    callback: Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CLOSE_CHANNEL_CALLBACK
WS_SERVICE_PROPERTY_ID = Int32
WS_SERVICE_PROPERTY_HOST_USER_STATE: WS_SERVICE_PROPERTY_ID = 0
WS_SERVICE_PROPERTY_FAULT_DISCLOSURE: WS_SERVICE_PROPERTY_ID = 1
WS_SERVICE_PROPERTY_FAULT_LANGID: WS_SERVICE_PROPERTY_ID = 2
WS_SERVICE_PROPERTY_HOST_STATE: WS_SERVICE_PROPERTY_ID = 3
WS_SERVICE_PROPERTY_METADATA: WS_SERVICE_PROPERTY_ID = 4
WS_SERVICE_PROPERTY_CLOSE_TIMEOUT: WS_SERVICE_PROPERTY_ID = 5
class WS_SERVICE_PROXY(Structure):
    pass
WS_SERVICE_PROXY_STATE = Int32
WS_SERVICE_PROXY_STATE_CREATED: WS_SERVICE_PROXY_STATE = 0
WS_SERVICE_PROXY_STATE_OPENING: WS_SERVICE_PROXY_STATE = 1
WS_SERVICE_PROXY_STATE_OPEN: WS_SERVICE_PROXY_STATE = 2
WS_SERVICE_PROXY_STATE_CLOSING: WS_SERVICE_PROXY_STATE = 3
WS_SERVICE_PROXY_STATE_CLOSED: WS_SERVICE_PROXY_STATE = 4
WS_SERVICE_PROXY_STATE_FAULTED: WS_SERVICE_PROXY_STATE = 5
@winfunctype_pointer
def WS_SERVICE_SECURITY_CALLBACK(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), authorized: POINTER(Windows.Win32.Foundation.BOOL), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_SECURITY_IDENTITIES(Structure):
    serviceIdentities: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head)
    serviceIdentityCount: UInt32
@winfunctype_pointer
def WS_SERVICE_STUB_CALLBACK(context: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head), frame: c_void_p, callback: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SET_CHANNEL_PROPERTY_CALLBACK(channelInstance: c_void_p, id: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SET_LISTENER_PROPERTY_CALLBACK(listenerInstance: c_void_p, id: Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK(channelInstance: c_void_p, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_SOAPUDP_URL(Structure):
    url: Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_SPN_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    spn: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_SSL_TRANSPORT_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    localCertCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_head)
class WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        clientCertCredentialRequired: Windows.Win32.Foundation.BOOL
class WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    localCertCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_head)
class WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_STRING(Structure):
    length: UInt32
    chars: Windows.Win32.Foundation.PWSTR
class WS_STRING_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_STRING_USERNAME_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL
    username: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    password: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
    username: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    password: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    domain: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_STRUCT_DESCRIPTION(Structure):
    size: UInt32
    alignment: UInt32
    fields: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION_head))
    fieldCount: UInt32
    typeLocalName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    typeNs: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    parentType: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION_head)
    subTypes: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION_head))
    subTypeCount: UInt32
    structOptions: UInt32
class WS_SUBJECT_NAME_CERT_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    storeLocation: UInt32
    storeName: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    subjectName: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_TCP_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_TCP_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_TCP_SSPI_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)
class WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_THUMBPRINT_CERT_CREDENTIAL(Structure):
    credential: Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    storeLocation: UInt32
    storeName: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    thumbprint: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_TIMESPAN(Structure):
    ticks: Int64
class WS_TIMESPAN_DESCRIPTION(Structure):
    minValue: Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
    maxValue: Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
WS_TRACE_API = Int32
WS_TRACE_API_NONE: WS_TRACE_API = -1
WS_TRACE_API_START_READER_CANONICALIZATION: WS_TRACE_API = 0
WS_TRACE_API_END_READER_CANONICALIZATION: WS_TRACE_API = 1
WS_TRACE_API_START_WRITER_CANONICALIZATION: WS_TRACE_API = 2
WS_TRACE_API_END_WRITER_CANONICALIZATION: WS_TRACE_API = 3
WS_TRACE_API_CREATE_XML_BUFFER: WS_TRACE_API = 4
WS_TRACE_API_REMOVE_NODE: WS_TRACE_API = 5
WS_TRACE_API_CREATE_READER: WS_TRACE_API = 6
WS_TRACE_API_SET_INPUT: WS_TRACE_API = 7
WS_TRACE_API_SET_INPUT_TO_BUFFER: WS_TRACE_API = 8
WS_TRACE_API_FREE_XML_READER: WS_TRACE_API = 9
WS_TRACE_API_GET_READER_PROPERTY: WS_TRACE_API = 10
WS_TRACE_API_GET_READER_NODE: WS_TRACE_API = 11
WS_TRACE_API_FILL_READER: WS_TRACE_API = 12
WS_TRACE_API_READ_START_ELEMENT: WS_TRACE_API = 13
WS_TRACE_API_READ_TO_START_ELEMENT: WS_TRACE_API = 14
WS_TRACE_API_READ_START_ATTRIBUTE: WS_TRACE_API = 15
WS_TRACE_API_READ_END_ATTRIBUTE: WS_TRACE_API = 16
WS_TRACE_API_READ_NODE: WS_TRACE_API = 17
WS_TRACE_API_SKIP_NODE: WS_TRACE_API = 18
WS_TRACE_API_READ_END_ELEMENT: WS_TRACE_API = 19
WS_TRACE_API_FIND_ATTRIBUTE: WS_TRACE_API = 20
WS_TRACE_API_READ_ELEMENT_VALUE: WS_TRACE_API = 21
WS_TRACE_API_READ_CHARS: WS_TRACE_API = 22
WS_TRACE_API_READ_CHARS_UTF8: WS_TRACE_API = 23
WS_TRACE_API_READ_BYTES: WS_TRACE_API = 24
WS_TRACE_API_READ_ARRAY: WS_TRACE_API = 25
WS_TRACE_API_GET_READER_POSITION: WS_TRACE_API = 26
WS_TRACE_API_SET_READER_POSITION: WS_TRACE_API = 27
WS_TRACE_API_MOVE_READER: WS_TRACE_API = 28
WS_TRACE_API_CREATE_WRITER: WS_TRACE_API = 29
WS_TRACE_API_FREE_XML_WRITER: WS_TRACE_API = 30
WS_TRACE_API_SET_OUTPUT: WS_TRACE_API = 31
WS_TRACE_API_SET_OUTPUT_TO_BUFFER: WS_TRACE_API = 32
WS_TRACE_API_GET_WRITER_PROPERTY: WS_TRACE_API = 33
WS_TRACE_API_FLUSH_WRITER: WS_TRACE_API = 34
WS_TRACE_API_WRITE_START_ELEMENT: WS_TRACE_API = 35
WS_TRACE_API_WRITE_END_START_ELEMENT: WS_TRACE_API = 36
WS_TRACE_API_WRITE_XMLNS_ATTRIBUTE: WS_TRACE_API = 37
WS_TRACE_API_WRITE_START_ATTRIBUTE: WS_TRACE_API = 38
WS_TRACE_API_WRITE_END_ATTRIBUTE: WS_TRACE_API = 39
WS_TRACE_API_WRITE_VALUE: WS_TRACE_API = 40
WS_TRACE_API_WRITE_XML_BUFFER: WS_TRACE_API = 41
WS_TRACE_API_READ_XML_BUFFER: WS_TRACE_API = 42
WS_TRACE_API_WRITE_XML_BUFFER_TO_BYTES: WS_TRACE_API = 43
WS_TRACE_API_READ_XML_BUFFER_FROM_BYTES: WS_TRACE_API = 44
WS_TRACE_API_WRITE_ARRAY: WS_TRACE_API = 45
WS_TRACE_API_WRITE_QUALIFIED_NAME: WS_TRACE_API = 46
WS_TRACE_API_WRITE_CHARS: WS_TRACE_API = 47
WS_TRACE_API_WRITE_CHARS_UTF8: WS_TRACE_API = 48
WS_TRACE_API_WRITE_BYTES: WS_TRACE_API = 49
WS_TRACE_API_PUSH_BYTES: WS_TRACE_API = 50
WS_TRACE_API_PULL_BYTES: WS_TRACE_API = 51
WS_TRACE_API_WRITE_END_ELEMENT: WS_TRACE_API = 52
WS_TRACE_API_WRITE_TEXT: WS_TRACE_API = 53
WS_TRACE_API_WRITE_START_CDATA: WS_TRACE_API = 54
WS_TRACE_API_WRITE_END_CDATA: WS_TRACE_API = 55
WS_TRACE_API_WRITE_NODE: WS_TRACE_API = 56
WS_TRACE_API_PREFIX_FROM_NAMESPACE: WS_TRACE_API = 57
WS_TRACE_API_GET_WRITER_POSITION: WS_TRACE_API = 58
WS_TRACE_API_SET_WRITER_POSITION: WS_TRACE_API = 59
WS_TRACE_API_MOVE_WRITER: WS_TRACE_API = 60
WS_TRACE_API_TRIM_XML_WHITESPACE: WS_TRACE_API = 61
WS_TRACE_API_VERIFY_XML_NCNAME: WS_TRACE_API = 62
WS_TRACE_API_XML_STRING_EQUALS: WS_TRACE_API = 63
WS_TRACE_API_NAMESPACE_FROM_PREFIX: WS_TRACE_API = 64
WS_TRACE_API_READ_QUALIFIED_NAME: WS_TRACE_API = 65
WS_TRACE_API_GET_XML_ATTRIBUTE: WS_TRACE_API = 66
WS_TRACE_API_COPY_NODE: WS_TRACE_API = 67
WS_TRACE_API_ASYNC_EXECUTE: WS_TRACE_API = 68
WS_TRACE_API_CREATE_CHANNEL: WS_TRACE_API = 69
WS_TRACE_API_OPEN_CHANNEL: WS_TRACE_API = 70
WS_TRACE_API_SEND_MESSAGE: WS_TRACE_API = 71
WS_TRACE_API_RECEIVE_MESSAGE: WS_TRACE_API = 72
WS_TRACE_API_REQUEST_REPLY: WS_TRACE_API = 73
WS_TRACE_API_SEND_REPLY_MESSAGE: WS_TRACE_API = 74
WS_TRACE_API_SEND_FAULT_MESSAGE_FOR_ERROR: WS_TRACE_API = 75
WS_TRACE_API_GET_CHANNEL_PROPERTY: WS_TRACE_API = 76
WS_TRACE_API_SET_CHANNEL_PROPERTY: WS_TRACE_API = 77
WS_TRACE_API_WRITE_MESSAGE_START: WS_TRACE_API = 78
WS_TRACE_API_WRITE_MESSAGE_END: WS_TRACE_API = 79
WS_TRACE_API_READ_MESSAGE_START: WS_TRACE_API = 80
WS_TRACE_API_READ_MESSAGE_END: WS_TRACE_API = 81
WS_TRACE_API_CLOSE_CHANNEL: WS_TRACE_API = 82
WS_TRACE_API_ABORT_CHANNEL: WS_TRACE_API = 83
WS_TRACE_API_FREE_CHANNEL: WS_TRACE_API = 84
WS_TRACE_API_RESET_CHANNEL: WS_TRACE_API = 85
WS_TRACE_API_ABANDON_MESSAGE: WS_TRACE_API = 86
WS_TRACE_API_SHUTDOWN_SESSION_CHANNEL: WS_TRACE_API = 87
WS_TRACE_API_GET_CONTEXT_PROPERTY: WS_TRACE_API = 88
WS_TRACE_API_GET_DICTIONARY: WS_TRACE_API = 89
WS_TRACE_API_READ_ENDPOINT_ADDRESS_EXTENSION: WS_TRACE_API = 90
WS_TRACE_API_CREATE_ERROR: WS_TRACE_API = 91
WS_TRACE_API_ADD_ERROR_STRING: WS_TRACE_API = 92
WS_TRACE_API_GET_ERROR_STRING: WS_TRACE_API = 93
WS_TRACE_API_COPY_ERROR: WS_TRACE_API = 94
WS_TRACE_API_GET_ERROR_PROPERTY: WS_TRACE_API = 95
WS_TRACE_API_SET_ERROR_PROPERTY: WS_TRACE_API = 96
WS_TRACE_API_RESET_ERROR: WS_TRACE_API = 97
WS_TRACE_API_FREE_ERROR: WS_TRACE_API = 98
WS_TRACE_API_GET_FAULT_ERROR_PROPERTY: WS_TRACE_API = 99
WS_TRACE_API_SET_FAULT_ERROR_PROPERTY: WS_TRACE_API = 100
WS_TRACE_API_CREATE_FAULT_FROM_ERROR: WS_TRACE_API = 101
WS_TRACE_API_SET_FAULT_ERROR_DETAIL: WS_TRACE_API = 102
WS_TRACE_API_GET_FAULT_ERROR_DETAIL: WS_TRACE_API = 103
WS_TRACE_API_CREATE_HEAP: WS_TRACE_API = 104
WS_TRACE_API_ALLOC: WS_TRACE_API = 105
WS_TRACE_API_GET_HEAP_PROPERTY: WS_TRACE_API = 106
WS_TRACE_API_RESET_HEAP: WS_TRACE_API = 107
WS_TRACE_API_FREE_HEAP: WS_TRACE_API = 108
WS_TRACE_API_CREATE_LISTENER: WS_TRACE_API = 109
WS_TRACE_API_OPEN_LISTENER: WS_TRACE_API = 110
WS_TRACE_API_ACCEPT_CHANNEL: WS_TRACE_API = 111
WS_TRACE_API_CLOSE_LISTENER: WS_TRACE_API = 112
WS_TRACE_API_ABORT_LISTENER: WS_TRACE_API = 113
WS_TRACE_API_RESET_LISTENER: WS_TRACE_API = 114
WS_TRACE_API_FREE_LISTENER: WS_TRACE_API = 115
WS_TRACE_API_GET_LISTENER_PROPERTY: WS_TRACE_API = 116
WS_TRACE_API_SET_LISTENER_PROPERTY: WS_TRACE_API = 117
WS_TRACE_API_CREATE_CHANNEL_FOR_LISTENER: WS_TRACE_API = 118
WS_TRACE_API_CREATE_MESSAGE: WS_TRACE_API = 119
WS_TRACE_API_CREATE_MESSAGE_FOR_CHANNEL: WS_TRACE_API = 120
WS_TRACE_API_INITIALIZE_MESSAGE: WS_TRACE_API = 121
WS_TRACE_API_RESET_MESSAGE: WS_TRACE_API = 122
WS_TRACE_API_FREE_MESSAGE: WS_TRACE_API = 123
WS_TRACE_API_GET_HEADER_ATTRIBUTES: WS_TRACE_API = 124
WS_TRACE_API_GET_HEADER: WS_TRACE_API = 125
WS_TRACE_API_GET_CUSTOM_HEADER: WS_TRACE_API = 126
WS_TRACE_API_REMOVE_HEADER: WS_TRACE_API = 127
WS_TRACE_API_SET_HEADER: WS_TRACE_API = 128
WS_TRACE_API_REMOVE_CUSTOM_HEADER: WS_TRACE_API = 129
WS_TRACE_API_ADD_CUSTOM_HEADER: WS_TRACE_API = 130
WS_TRACE_API_ADD_MAPPED_HEADER: WS_TRACE_API = 131
WS_TRACE_API_REMOVE_MAPPED_HEADER: WS_TRACE_API = 132
WS_TRACE_API_GET_MAPPED_HEADER: WS_TRACE_API = 133
WS_TRACE_API_WRITE_BODY: WS_TRACE_API = 134
WS_TRACE_API_READ_BODY: WS_TRACE_API = 135
WS_TRACE_API_WRITE_ENVELOPE_START: WS_TRACE_API = 136
WS_TRACE_API_WRITE_ENVELOPE_END: WS_TRACE_API = 137
WS_TRACE_API_READ_ENVELOPE_START: WS_TRACE_API = 138
WS_TRACE_API_READ_ENVELOPE_END: WS_TRACE_API = 139
WS_TRACE_API_GET_MESSAGE_PROPERTY: WS_TRACE_API = 140
WS_TRACE_API_SET_MESSAGE_PROPERTY: WS_TRACE_API = 141
WS_TRACE_API_ADDRESS_MESSAGE: WS_TRACE_API = 142
WS_TRACE_API_CHECK_MUST_UNDERSTAND_HEADERS: WS_TRACE_API = 143
WS_TRACE_API_MARK_HEADER_AS_UNDERSTOOD: WS_TRACE_API = 144
WS_TRACE_API_FILL_BODY: WS_TRACE_API = 145
WS_TRACE_API_FLUSH_BODY: WS_TRACE_API = 146
WS_TRACE_API_REQUEST_SECURITY_TOKEN: WS_TRACE_API = 147
WS_TRACE_API_GET_SECURITY_TOKEN_PROPERTY: WS_TRACE_API = 148
WS_TRACE_API_CREATE_XML_SECURITY_TOKEN: WS_TRACE_API = 149
WS_TRACE_API_FREE_SECURITY_TOKEN: WS_TRACE_API = 150
WS_TRACE_API_REVOKE_SECURITY_CONTEXT: WS_TRACE_API = 151
WS_TRACE_API_GET_SECURITY_CONTEXT_PROPERTY: WS_TRACE_API = 152
WS_TRACE_API_READ_ELEMENT_TYPE: WS_TRACE_API = 153
WS_TRACE_API_READ_ATTRIBUTE_TYPE: WS_TRACE_API = 154
WS_TRACE_API_READ_TYPE: WS_TRACE_API = 155
WS_TRACE_API_WRITE_ELEMENT_TYPE: WS_TRACE_API = 156
WS_TRACE_API_WRITE_ATTRIBUTE_TYPE: WS_TRACE_API = 157
WS_TRACE_API_WRITE_TYPE: WS_TRACE_API = 158
WS_TRACE_API_SERVICE_REGISTER_FOR_CANCEL: WS_TRACE_API = 159
WS_TRACE_API_GET_SERVICE_HOST_PROPERTY: WS_TRACE_API = 160
WS_TRACE_API_CREATE_SERVICE_HOST: WS_TRACE_API = 161
WS_TRACE_API_OPEN_SERVICE_HOST: WS_TRACE_API = 162
WS_TRACE_API_CLOSE_SERVICE_HOST: WS_TRACE_API = 163
WS_TRACE_API_ABORT_SERVICE_HOST: WS_TRACE_API = 164
WS_TRACE_API_FREE_SERVICE_HOST: WS_TRACE_API = 165
WS_TRACE_API_RESET_SERVICE_HOST: WS_TRACE_API = 166
WS_TRACE_API_GET_SERVICE_PROXY_PROPERTY: WS_TRACE_API = 167
WS_TRACE_API_CREATE_SERVICE_PROXY: WS_TRACE_API = 168
WS_TRACE_API_OPEN_SERVICE_PROXY: WS_TRACE_API = 169
WS_TRACE_API_CLOSE_SERVICE_PROXY: WS_TRACE_API = 170
WS_TRACE_API_ABORT_SERVICE_PROXY: WS_TRACE_API = 171
WS_TRACE_API_FREE_SERVICE_PROXY: WS_TRACE_API = 172
WS_TRACE_API_RESET_SERVICE_PROXY: WS_TRACE_API = 173
WS_TRACE_API_ABORT_CALL: WS_TRACE_API = 174
WS_TRACE_API_CALL: WS_TRACE_API = 175
WS_TRACE_API_DECODE_URL: WS_TRACE_API = 176
WS_TRACE_API_ENCODE_URL: WS_TRACE_API = 177
WS_TRACE_API_COMBINE_URL: WS_TRACE_API = 178
WS_TRACE_API_DATETIME_TO_FILETIME: WS_TRACE_API = 179
WS_TRACE_API_FILETIME_TO_DATETIME: WS_TRACE_API = 180
WS_TRACE_API_DUMP_MEMORY: WS_TRACE_API = 181
WS_TRACE_API_SET_AUTOFAIL: WS_TRACE_API = 182
WS_TRACE_API_CREATE_METADATA: WS_TRACE_API = 183
WS_TRACE_API_READ_METADATA: WS_TRACE_API = 184
WS_TRACE_API_FREE_METADATA: WS_TRACE_API = 185
WS_TRACE_API_RESET_METADATA: WS_TRACE_API = 186
WS_TRACE_API_GET_METADATA_PROPERTY: WS_TRACE_API = 187
WS_TRACE_API_GET_MISSING_METADATA_DOCUMENT_ADDRESS: WS_TRACE_API = 188
WS_TRACE_API_GET_METADATA_ENDPOINTS: WS_TRACE_API = 189
WS_TRACE_API_MATCH_POLICY_ALTERNATIVE: WS_TRACE_API = 190
WS_TRACE_API_GET_POLICY_PROPERTY: WS_TRACE_API = 191
WS_TRACE_API_GET_POLICY_ALTERNATIVE_COUNT: WS_TRACE_API = 192
WS_TRACE_API_WS_CREATE_SERVICE_PROXY_FROM_TEMPLATE: WS_TRACE_API = 193
WS_TRACE_API_WS_CREATE_SERVICE_HOST_FROM_TEMPLATE: WS_TRACE_API = 194
WS_TRANSFER_MODE = Int32
WS_STREAMED_INPUT_TRANSFER_MODE: WS_TRANSFER_MODE = 1
WS_STREAMED_OUTPUT_TRANSFER_MODE: WS_TRANSFER_MODE = 2
WS_BUFFERED_TRANSFER_MODE: WS_TRANSFER_MODE = 0
WS_STREAMED_TRANSFER_MODE: WS_TRANSFER_MODE = 3
WS_TRUST_VERSION = Int32
WS_TRUST_VERSION_FEBRUARY_2005: WS_TRUST_VERSION = 1
WS_TRUST_VERSION_1_3: WS_TRUST_VERSION = 2
WS_TYPE = Int32
WS_BOOL_TYPE: WS_TYPE = 0
WS_INT8_TYPE: WS_TYPE = 1
WS_INT16_TYPE: WS_TYPE = 2
WS_INT32_TYPE: WS_TYPE = 3
WS_INT64_TYPE: WS_TYPE = 4
WS_UINT8_TYPE: WS_TYPE = 5
WS_UINT16_TYPE: WS_TYPE = 6
WS_UINT32_TYPE: WS_TYPE = 7
WS_UINT64_TYPE: WS_TYPE = 8
WS_FLOAT_TYPE: WS_TYPE = 9
WS_DOUBLE_TYPE: WS_TYPE = 10
WS_DECIMAL_TYPE: WS_TYPE = 11
WS_DATETIME_TYPE: WS_TYPE = 12
WS_TIMESPAN_TYPE: WS_TYPE = 13
WS_GUID_TYPE: WS_TYPE = 14
WS_UNIQUE_ID_TYPE: WS_TYPE = 15
WS_STRING_TYPE: WS_TYPE = 16
WS_WSZ_TYPE: WS_TYPE = 17
WS_BYTES_TYPE: WS_TYPE = 18
WS_XML_STRING_TYPE: WS_TYPE = 19
WS_XML_QNAME_TYPE: WS_TYPE = 20
WS_XML_BUFFER_TYPE: WS_TYPE = 21
WS_CHAR_ARRAY_TYPE: WS_TYPE = 22
WS_UTF8_ARRAY_TYPE: WS_TYPE = 23
WS_BYTE_ARRAY_TYPE: WS_TYPE = 24
WS_DESCRIPTION_TYPE: WS_TYPE = 25
WS_STRUCT_TYPE: WS_TYPE = 26
WS_CUSTOM_TYPE: WS_TYPE = 27
WS_ENDPOINT_ADDRESS_TYPE: WS_TYPE = 28
WS_FAULT_TYPE: WS_TYPE = 29
WS_VOID_TYPE: WS_TYPE = 30
WS_ENUM_TYPE: WS_TYPE = 31
WS_DURATION_TYPE: WS_TYPE = 32
WS_UNION_TYPE: WS_TYPE = 33
WS_ANY_ATTRIBUTES_TYPE: WS_TYPE = 34
WS_TYPE_MAPPING = Int32
WS_ELEMENT_TYPE_MAPPING: WS_TYPE_MAPPING = 1
WS_ATTRIBUTE_TYPE_MAPPING: WS_TYPE_MAPPING = 2
WS_ELEMENT_CONTENT_TYPE_MAPPING: WS_TYPE_MAPPING = 3
WS_ANY_ELEMENT_TYPE_MAPPING: WS_TYPE_MAPPING = 4
class WS_UINT16_DESCRIPTION(Structure):
    minValue: UInt16
    maxValue: UInt16
class WS_UINT32_DESCRIPTION(Structure):
    minValue: UInt32
    maxValue: UInt32
class WS_UINT64_DESCRIPTION(Structure):
    minValue: UInt64
    maxValue: UInt64
class WS_UINT8_DESCRIPTION(Structure):
    minValue: Byte
    maxValue: Byte
class WS_UNION_DESCRIPTION(Structure):
    size: UInt32
    alignment: UInt32
    fields: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_UNION_FIELD_DESCRIPTION_head))
    fieldCount: UInt32
    enumOffset: UInt32
    noneEnumValue: Int32
    valueIndices: POINTER(UInt32)
class WS_UNION_FIELD_DESCRIPTION(Structure):
    value: Int32
    field: Windows.Win32.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION
class WS_UNIQUE_ID(Structure):
    uri: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    guid: Guid
class WS_UNIQUE_ID_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_UNKNOWN_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    element: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
class WS_UPN_ENDPOINT_IDENTITY(Structure):
    identity: Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    upn: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_URL(Structure):
    scheme: Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE
WS_URL_SCHEME_TYPE = Int32
WS_URL_HTTP_SCHEME_TYPE: WS_URL_SCHEME_TYPE = 0
WS_URL_HTTPS_SCHEME_TYPE: WS_URL_SCHEME_TYPE = 1
WS_URL_NETTCP_SCHEME_TYPE: WS_URL_SCHEME_TYPE = 2
WS_URL_SOAPUDP_SCHEME_TYPE: WS_URL_SCHEME_TYPE = 3
WS_URL_NETPIPE_SCHEME_TYPE: WS_URL_SCHEME_TYPE = 4
class WS_USERNAME_CREDENTIAL(Structure):
    credentialType: Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_TYPE
WS_USERNAME_CREDENTIAL_TYPE = Int32
WS_STRING_USERNAME_CREDENTIAL_TYPE: WS_USERNAME_CREDENTIAL_TYPE = 1
class WS_USERNAME_MESSAGE_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_head)
    passwordValidator: Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK
    passwordValidatorCallbackState: c_void_p
class WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_head)
    passwordValidator: Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK
    passwordValidatorCallbackState: c_void_p
class WS_UTF8_ARRAY_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
@winfunctype_pointer
def WS_VALIDATE_PASSWORD_CALLBACK(passwordValidatorCallbackState: c_void_p, username: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), password: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_STRING_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_VALIDATE_SAML_CALLBACK(samlValidatorCallbackState: c_void_p, samlAssertion: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_VALUE_TYPE = Int32
WS_BOOL_VALUE_TYPE: WS_VALUE_TYPE = 0
WS_INT8_VALUE_TYPE: WS_VALUE_TYPE = 1
WS_INT16_VALUE_TYPE: WS_VALUE_TYPE = 2
WS_INT32_VALUE_TYPE: WS_VALUE_TYPE = 3
WS_INT64_VALUE_TYPE: WS_VALUE_TYPE = 4
WS_UINT8_VALUE_TYPE: WS_VALUE_TYPE = 5
WS_UINT16_VALUE_TYPE: WS_VALUE_TYPE = 6
WS_UINT32_VALUE_TYPE: WS_VALUE_TYPE = 7
WS_UINT64_VALUE_TYPE: WS_VALUE_TYPE = 8
WS_FLOAT_VALUE_TYPE: WS_VALUE_TYPE = 9
WS_DOUBLE_VALUE_TYPE: WS_VALUE_TYPE = 10
WS_DECIMAL_VALUE_TYPE: WS_VALUE_TYPE = 11
WS_DATETIME_VALUE_TYPE: WS_VALUE_TYPE = 12
WS_TIMESPAN_VALUE_TYPE: WS_VALUE_TYPE = 13
WS_GUID_VALUE_TYPE: WS_VALUE_TYPE = 14
WS_DURATION_VALUE_TYPE: WS_VALUE_TYPE = 15
class WS_VOID_DESCRIPTION(Structure):
    size: UInt32
class WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credentialType: Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE
WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = Int32
WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 1
WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 2
WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 3
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = Int32
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_KERBEROS: WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 1
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_NTLM: WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 2
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_SPNEGO: WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 3
@winfunctype_pointer
def WS_WRITE_CALLBACK(callbackState: c_void_p, buffers: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_BYTES_head), count: UInt32, asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_WRITE_MESSAGE_END_CALLBACK(channelInstance: c_void_p, message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_WRITE_MESSAGE_START_CALLBACK(channelInstance: c_void_p, message: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_head), asyncContext: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head), error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
WS_WRITE_OPTION = Int32
WS_WRITE_REQUIRED_VALUE: WS_WRITE_OPTION = 1
WS_WRITE_REQUIRED_POINTER: WS_WRITE_OPTION = 2
WS_WRITE_NILLABLE_VALUE: WS_WRITE_OPTION = 3
WS_WRITE_NILLABLE_POINTER: WS_WRITE_OPTION = 4
@winfunctype_pointer
def WS_WRITE_TYPE_CALLBACK(writer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_head), typeMapping: Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, descriptionData: c_void_p, value: c_void_p, valueSize: UInt32, error: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_ERROR_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WS_WSZ_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_XML_ATTRIBUTE(Structure):
    singleQuote: Byte
    isXmlNs: Byte
    prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    value: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_head)
class WS_XML_BASE64_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    bytes: c_char_p_no
    length: UInt32
class WS_XML_BOOL_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Windows.Win32.Foundation.BOOL
class WS_XML_BUFFER(Structure):
    pass
class WS_XML_BUFFER_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_XML_BUFFER_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_ALGORITHM = Int32
WS_EXCLUSIVE_XML_CANONICALIZATION_ALGORITHM: WS_XML_CANONICALIZATION_ALGORITHM = 0
WS_EXCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM: WS_XML_CANONICALIZATION_ALGORITHM = 1
WS_INCLUSIVE_XML_CANONICALIZATION_ALGORITHM: WS_XML_CANONICALIZATION_ALGORITHM = 2
WS_INCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM: WS_XML_CANONICALIZATION_ALGORITHM = 3
class WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES(Structure):
    prefixCount: UInt32
    prefixes: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
class WS_XML_CANONICALIZATION_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_XML_CANONICALIZATION_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_PROPERTY_ALGORITHM: WS_XML_CANONICALIZATION_PROPERTY_ID = 0
WS_XML_CANONICALIZATION_PROPERTY_INCLUSIVE_PREFIXES: WS_XML_CANONICALIZATION_PROPERTY_ID = 1
WS_XML_CANONICALIZATION_PROPERTY_OMITTED_ELEMENT: WS_XML_CANONICALIZATION_PROPERTY_ID = 2
WS_XML_CANONICALIZATION_PROPERTY_OUTPUT_BUFFER_SIZE: WS_XML_CANONICALIZATION_PROPERTY_ID = 3
class WS_XML_COMMENT_NODE(Structure):
    node: Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    value: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
class WS_XML_DATETIME_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
class WS_XML_DECIMAL_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Windows.Win32.Foundation.DECIMAL
class WS_XML_DICTIONARY(Structure):
    guid: Guid
    strings: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    stringCount: UInt32
    isConst: Windows.Win32.Foundation.BOOL
class WS_XML_DOUBLE_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Double
class WS_XML_ELEMENT_NODE(Structure):
    node: Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    attributeCount: UInt32
    attributes: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_ATTRIBUTE_head))
    isEmpty: Windows.Win32.Foundation.BOOL
class WS_XML_FLOAT_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Single
class WS_XML_GUID_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Guid
class WS_XML_INT32_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Int32
class WS_XML_INT64_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Int64
class WS_XML_LIST_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    itemCount: UInt32
    items: POINTER(POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_head))
class WS_XML_NODE(Structure):
    nodeType: Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE
class WS_XML_NODE_POSITION(Structure):
    buffer: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_head)
    node: c_void_p
WS_XML_NODE_TYPE = Int32
WS_XML_NODE_TYPE_ELEMENT: WS_XML_NODE_TYPE = 1
WS_XML_NODE_TYPE_TEXT: WS_XML_NODE_TYPE = 2
WS_XML_NODE_TYPE_END_ELEMENT: WS_XML_NODE_TYPE = 3
WS_XML_NODE_TYPE_COMMENT: WS_XML_NODE_TYPE = 4
WS_XML_NODE_TYPE_CDATA: WS_XML_NODE_TYPE = 6
WS_XML_NODE_TYPE_END_CDATA: WS_XML_NODE_TYPE = 7
WS_XML_NODE_TYPE_EOF: WS_XML_NODE_TYPE = 8
WS_XML_NODE_TYPE_BOF: WS_XML_NODE_TYPE = 9
class WS_XML_QNAME(Structure):
    localName: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    ns: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
class WS_XML_QNAME_DESCRIPTION(Structure):
    minLocalNameByteCount: UInt32
    maxLocalNameByteCount: UInt32
    minNsByteCount: UInt32
    maxNsByteCount: UInt32
class WS_XML_QNAME_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    prefix: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    localName: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
    ns: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING_head)
class WS_XML_READER(Structure):
    pass
class WS_XML_READER_BINARY_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    staticDictionary: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)
    dynamicDictionary: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)
class WS_XML_READER_BUFFER_INPUT(Structure):
    input: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT
    encodedData: c_void_p
    encodedDataSize: UInt32
class WS_XML_READER_ENCODING(Structure):
    encodingType: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE
WS_XML_READER_ENCODING_TYPE = Int32
WS_XML_READER_ENCODING_TYPE_TEXT: WS_XML_READER_ENCODING_TYPE = 1
WS_XML_READER_ENCODING_TYPE_BINARY: WS_XML_READER_ENCODING_TYPE = 2
WS_XML_READER_ENCODING_TYPE_MTOM: WS_XML_READER_ENCODING_TYPE = 3
WS_XML_READER_ENCODING_TYPE_RAW: WS_XML_READER_ENCODING_TYPE = 4
class WS_XML_READER_INPUT(Structure):
    inputType: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT_TYPE
WS_XML_READER_INPUT_TYPE = Int32
WS_XML_READER_INPUT_TYPE_BUFFER: WS_XML_READER_INPUT_TYPE = 1
WS_XML_READER_INPUT_TYPE_STREAM: WS_XML_READER_INPUT_TYPE = 2
class WS_XML_READER_MTOM_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    textEncoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head)
    readMimeHeader: Windows.Win32.Foundation.BOOL
    startInfo: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    boundary: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startUri: Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_XML_READER_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head)
    propertyCount: UInt32
class WS_XML_READER_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_XML_READER_PROPERTY_ID = Int32
WS_XML_READER_PROPERTY_MAX_DEPTH: WS_XML_READER_PROPERTY_ID = 0
WS_XML_READER_PROPERTY_ALLOW_FRAGMENT: WS_XML_READER_PROPERTY_ID = 1
WS_XML_READER_PROPERTY_MAX_ATTRIBUTES: WS_XML_READER_PROPERTY_ID = 2
WS_XML_READER_PROPERTY_READ_DECLARATION: WS_XML_READER_PROPERTY_ID = 3
WS_XML_READER_PROPERTY_CHARSET: WS_XML_READER_PROPERTY_ID = 4
WS_XML_READER_PROPERTY_ROW: WS_XML_READER_PROPERTY_ID = 5
WS_XML_READER_PROPERTY_COLUMN: WS_XML_READER_PROPERTY_ID = 6
WS_XML_READER_PROPERTY_UTF8_TRIM_SIZE: WS_XML_READER_PROPERTY_ID = 7
WS_XML_READER_PROPERTY_STREAM_BUFFER_SIZE: WS_XML_READER_PROPERTY_ID = 8
WS_XML_READER_PROPERTY_IN_ATTRIBUTE: WS_XML_READER_PROPERTY_ID = 9
WS_XML_READER_PROPERTY_STREAM_MAX_ROOT_MIME_PART_SIZE: WS_XML_READER_PROPERTY_ID = 10
WS_XML_READER_PROPERTY_STREAM_MAX_MIME_HEADERS_SIZE: WS_XML_READER_PROPERTY_ID = 11
WS_XML_READER_PROPERTY_MAX_MIME_PARTS: WS_XML_READER_PROPERTY_ID = 12
WS_XML_READER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES: WS_XML_READER_PROPERTY_ID = 13
WS_XML_READER_PROPERTY_MAX_NAMESPACES: WS_XML_READER_PROPERTY_ID = 14
class WS_XML_READER_RAW_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
class WS_XML_READER_STREAM_INPUT(Structure):
    input: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT
    readCallback: Windows.Win32.Networking.WindowsWebServices.WS_READ_CALLBACK
    readCallbackState: c_void_p
class WS_XML_READER_TEXT_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    charSet: Windows.Win32.Networking.WindowsWebServices.WS_CHARSET
class WS_XML_SECURITY_TOKEN_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_XML_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_XML_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE: WS_XML_SECURITY_TOKEN_PROPERTY_ID = 1
WS_XML_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE: WS_XML_SECURITY_TOKEN_PROPERTY_ID = 2
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME: WS_XML_SECURITY_TOKEN_PROPERTY_ID = 3
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME: WS_XML_SECURITY_TOKEN_PROPERTY_ID = 4
class WS_XML_STRING(Structure):
    length: UInt32
    bytes: c_char_p_no
    dictionary: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)
    id: UInt32
class WS_XML_STRING_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
class WS_XML_TEXT(Structure):
    textType: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE
class WS_XML_TEXT_NODE(Structure):
    node: Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    text: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_head)
WS_XML_TEXT_TYPE = Int32
WS_XML_TEXT_TYPE_UTF8: WS_XML_TEXT_TYPE = 1
WS_XML_TEXT_TYPE_UTF16: WS_XML_TEXT_TYPE = 2
WS_XML_TEXT_TYPE_BASE64: WS_XML_TEXT_TYPE = 3
WS_XML_TEXT_TYPE_BOOL: WS_XML_TEXT_TYPE = 4
WS_XML_TEXT_TYPE_INT32: WS_XML_TEXT_TYPE = 5
WS_XML_TEXT_TYPE_INT64: WS_XML_TEXT_TYPE = 6
WS_XML_TEXT_TYPE_UINT64: WS_XML_TEXT_TYPE = 7
WS_XML_TEXT_TYPE_FLOAT: WS_XML_TEXT_TYPE = 8
WS_XML_TEXT_TYPE_DOUBLE: WS_XML_TEXT_TYPE = 9
WS_XML_TEXT_TYPE_DECIMAL: WS_XML_TEXT_TYPE = 10
WS_XML_TEXT_TYPE_GUID: WS_XML_TEXT_TYPE = 11
WS_XML_TEXT_TYPE_UNIQUE_ID: WS_XML_TEXT_TYPE = 12
WS_XML_TEXT_TYPE_DATETIME: WS_XML_TEXT_TYPE = 13
WS_XML_TEXT_TYPE_TIMESPAN: WS_XML_TEXT_TYPE = 14
WS_XML_TEXT_TYPE_QNAME: WS_XML_TEXT_TYPE = 15
WS_XML_TEXT_TYPE_LIST: WS_XML_TEXT_TYPE = 16
class WS_XML_TIMESPAN_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
class WS_XML_TOKEN_MESSAGE_SECURITY_BINDING(Structure):
    binding: Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    xmlToken: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)
class WS_XML_UINT64_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: UInt64
class WS_XML_UNIQUE_ID_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Guid
class WS_XML_UTF16_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    bytes: c_char_p_no
    byteCount: UInt32
class WS_XML_UTF8_TEXT(Structure):
    text: Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
class WS_XML_WRITER(Structure):
    pass
class WS_XML_WRITER_BINARY_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    staticDictionary: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)
    dynamicStringCallback: Windows.Win32.Networking.WindowsWebServices.WS_DYNAMIC_STRING_CALLBACK
    dynamicStringCallbackState: c_void_p
class WS_XML_WRITER_BUFFER_OUTPUT(Structure):
    output: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT
class WS_XML_WRITER_ENCODING(Structure):
    encodingType: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE
WS_XML_WRITER_ENCODING_TYPE = Int32
WS_XML_WRITER_ENCODING_TYPE_TEXT: WS_XML_WRITER_ENCODING_TYPE = 1
WS_XML_WRITER_ENCODING_TYPE_BINARY: WS_XML_WRITER_ENCODING_TYPE = 2
WS_XML_WRITER_ENCODING_TYPE_MTOM: WS_XML_WRITER_ENCODING_TYPE = 3
WS_XML_WRITER_ENCODING_TYPE_RAW: WS_XML_WRITER_ENCODING_TYPE = 4
class WS_XML_WRITER_MTOM_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    textEncoding: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head)
    writeMimeHeader: Windows.Win32.Foundation.BOOL
    boundary: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startInfo: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startUri: Windows.Win32.Networking.WindowsWebServices.WS_STRING
    maxInlineByteCount: UInt32
class WS_XML_WRITER_OUTPUT(Structure):
    outputType: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_TYPE
WS_XML_WRITER_OUTPUT_TYPE = Int32
WS_XML_WRITER_OUTPUT_TYPE_BUFFER: WS_XML_WRITER_OUTPUT_TYPE = 1
WS_XML_WRITER_OUTPUT_TYPE_STREAM: WS_XML_WRITER_OUTPUT_TYPE = 2
class WS_XML_WRITER_PROPERTIES(Structure):
    properties: POINTER(Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head)
    propertyCount: UInt32
class WS_XML_WRITER_PROPERTY(Structure):
    id: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID
    value: c_void_p
    valueSize: UInt32
WS_XML_WRITER_PROPERTY_ID = Int32
WS_XML_WRITER_PROPERTY_MAX_DEPTH: WS_XML_WRITER_PROPERTY_ID = 0
WS_XML_WRITER_PROPERTY_ALLOW_FRAGMENT: WS_XML_WRITER_PROPERTY_ID = 1
WS_XML_WRITER_PROPERTY_MAX_ATTRIBUTES: WS_XML_WRITER_PROPERTY_ID = 2
WS_XML_WRITER_PROPERTY_WRITE_DECLARATION: WS_XML_WRITER_PROPERTY_ID = 3
WS_XML_WRITER_PROPERTY_INDENT: WS_XML_WRITER_PROPERTY_ID = 4
WS_XML_WRITER_PROPERTY_BUFFER_TRIM_SIZE: WS_XML_WRITER_PROPERTY_ID = 5
WS_XML_WRITER_PROPERTY_CHARSET: WS_XML_WRITER_PROPERTY_ID = 6
WS_XML_WRITER_PROPERTY_BUFFERS: WS_XML_WRITER_PROPERTY_ID = 7
WS_XML_WRITER_PROPERTY_BUFFER_MAX_SIZE: WS_XML_WRITER_PROPERTY_ID = 8
WS_XML_WRITER_PROPERTY_BYTES: WS_XML_WRITER_PROPERTY_ID = 9
WS_XML_WRITER_PROPERTY_IN_ATTRIBUTE: WS_XML_WRITER_PROPERTY_ID = 10
WS_XML_WRITER_PROPERTY_MAX_MIME_PARTS_BUFFER_SIZE: WS_XML_WRITER_PROPERTY_ID = 11
WS_XML_WRITER_PROPERTY_INITIAL_BUFFER: WS_XML_WRITER_PROPERTY_ID = 12
WS_XML_WRITER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES: WS_XML_WRITER_PROPERTY_ID = 13
WS_XML_WRITER_PROPERTY_MAX_NAMESPACES: WS_XML_WRITER_PROPERTY_ID = 14
WS_XML_WRITER_PROPERTY_BYTES_WRITTEN: WS_XML_WRITER_PROPERTY_ID = 15
WS_XML_WRITER_PROPERTY_BYTES_TO_CLOSE: WS_XML_WRITER_PROPERTY_ID = 16
WS_XML_WRITER_PROPERTY_COMPRESS_EMPTY_ELEMENTS: WS_XML_WRITER_PROPERTY_ID = 17
WS_XML_WRITER_PROPERTY_EMIT_UNCOMPRESSED_EMPTY_ELEMENTS: WS_XML_WRITER_PROPERTY_ID = 18
class WS_XML_WRITER_RAW_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
class WS_XML_WRITER_STREAM_OUTPUT(Structure):
    output: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT
    writeCallback: Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK
    writeCallbackState: c_void_p
class WS_XML_WRITER_TEXT_ENCODING(Structure):
    encoding: Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    charSet: Windows.Win32.Networking.WindowsWebServices.WS_CHARSET
make_head(_module, 'IContentPrefetcherTaskTrigger')
make_head(_module, 'WEBAUTHN_ASSERTION')
make_head(_module, 'WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS')
make_head(_module, 'WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS')
make_head(_module, 'WEBAUTHN_CLIENT_DATA')
make_head(_module, 'WEBAUTHN_COMMON_ATTESTATION')
make_head(_module, 'WEBAUTHN_COSE_CREDENTIAL_PARAMETER')
make_head(_module, 'WEBAUTHN_COSE_CREDENTIAL_PARAMETERS')
make_head(_module, 'WEBAUTHN_CREDENTIAL')
make_head(_module, 'WEBAUTHN_CREDENTIALS')
make_head(_module, 'WEBAUTHN_CREDENTIAL_ATTESTATION')
make_head(_module, 'WEBAUTHN_CREDENTIAL_EX')
make_head(_module, 'WEBAUTHN_CREDENTIAL_LIST')
make_head(_module, 'WEBAUTHN_CRED_BLOB_EXTENSION')
make_head(_module, 'WEBAUTHN_CRED_PROTECT_EXTENSION_IN')
make_head(_module, 'WEBAUTHN_EXTENSION')
make_head(_module, 'WEBAUTHN_EXTENSIONS')
make_head(_module, 'WEBAUTHN_RP_ENTITY_INFORMATION')
make_head(_module, 'WEBAUTHN_USER_ENTITY_INFORMATION')
make_head(_module, 'WEBAUTHN_X5C')
make_head(_module, 'WS_ABANDON_MESSAGE_CALLBACK')
make_head(_module, 'WS_ABORT_CHANNEL_CALLBACK')
make_head(_module, 'WS_ABORT_LISTENER_CALLBACK')
make_head(_module, 'WS_ACCEPT_CHANNEL_CALLBACK')
make_head(_module, 'WS_ANY_ATTRIBUTE')
make_head(_module, 'WS_ANY_ATTRIBUTES')
make_head(_module, 'WS_ASYNC_CALLBACK')
make_head(_module, 'WS_ASYNC_CONTEXT')
make_head(_module, 'WS_ASYNC_FUNCTION')
make_head(_module, 'WS_ASYNC_OPERATION')
make_head(_module, 'WS_ASYNC_STATE')
make_head(_module, 'WS_ATTRIBUTE_DESCRIPTION')
make_head(_module, 'WS_BOOL_DESCRIPTION')
make_head(_module, 'WS_BUFFERS')
make_head(_module, 'WS_BYTES')
make_head(_module, 'WS_BYTES_DESCRIPTION')
make_head(_module, 'WS_BYTE_ARRAY_DESCRIPTION')
make_head(_module, 'WS_CALL_PROPERTY')
make_head(_module, 'WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE')
make_head(_module, 'WS_CERTIFICATE_VALIDATION_CALLBACK')
make_head(_module, 'WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT')
make_head(_module, 'WS_CERT_CREDENTIAL')
make_head(_module, 'WS_CERT_ENDPOINT_IDENTITY')
make_head(_module, 'WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK')
make_head(_module, 'WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_CERT_SIGNED_SAML_AUTHENTICATOR')
make_head(_module, 'WS_CHANNEL')
make_head(_module, 'WS_CHANNEL_DECODER')
make_head(_module, 'WS_CHANNEL_ENCODER')
make_head(_module, 'WS_CHANNEL_PROPERTIES')
make_head(_module, 'WS_CHANNEL_PROPERTY')
make_head(_module, 'WS_CHANNEL_PROPERTY_CONSTRAINT')
make_head(_module, 'WS_CHAR_ARRAY_DESCRIPTION')
make_head(_module, 'WS_CLOSE_CHANNEL_CALLBACK')
make_head(_module, 'WS_CLOSE_LISTENER_CALLBACK')
make_head(_module, 'WS_CONTRACT_DESCRIPTION')
make_head(_module, 'WS_CREATE_CHANNEL_CALLBACK')
make_head(_module, 'WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK')
make_head(_module, 'WS_CREATE_DECODER_CALLBACK')
make_head(_module, 'WS_CREATE_ENCODER_CALLBACK')
make_head(_module, 'WS_CREATE_LISTENER_CALLBACK')
make_head(_module, 'WS_CUSTOM_CERT_CREDENTIAL')
make_head(_module, 'WS_CUSTOM_CHANNEL_CALLBACKS')
make_head(_module, 'WS_CUSTOM_HTTP_PROXY')
make_head(_module, 'WS_CUSTOM_LISTENER_CALLBACKS')
make_head(_module, 'WS_CUSTOM_TYPE_DESCRIPTION')
make_head(_module, 'WS_DATETIME')
make_head(_module, 'WS_DATETIME_DESCRIPTION')
make_head(_module, 'WS_DECIMAL_DESCRIPTION')
make_head(_module, 'WS_DECODER_DECODE_CALLBACK')
make_head(_module, 'WS_DECODER_END_CALLBACK')
make_head(_module, 'WS_DECODER_GET_CONTENT_TYPE_CALLBACK')
make_head(_module, 'WS_DECODER_START_CALLBACK')
make_head(_module, 'WS_DEFAULT_VALUE')
make_head(_module, 'WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL')
make_head(_module, 'WS_DISALLOWED_USER_AGENT_SUBSTRINGS')
make_head(_module, 'WS_DNS_ENDPOINT_IDENTITY')
make_head(_module, 'WS_DOUBLE_DESCRIPTION')
make_head(_module, 'WS_DURATION')
make_head(_module, 'WS_DURATION_COMPARISON_CALLBACK')
make_head(_module, 'WS_DURATION_DESCRIPTION')
make_head(_module, 'WS_DYNAMIC_STRING_CALLBACK')
make_head(_module, 'WS_ELEMENT_DESCRIPTION')
make_head(_module, 'WS_ENCODER_ENCODE_CALLBACK')
make_head(_module, 'WS_ENCODER_END_CALLBACK')
make_head(_module, 'WS_ENCODER_GET_CONTENT_TYPE_CALLBACK')
make_head(_module, 'WS_ENCODER_START_CALLBACK')
make_head(_module, 'WS_ENDPOINT_ADDRESS')
make_head(_module, 'WS_ENDPOINT_ADDRESS_DESCRIPTION')
make_head(_module, 'WS_ENDPOINT_IDENTITY')
make_head(_module, 'WS_ENDPOINT_POLICY_EXTENSION')
make_head(_module, 'WS_ENUM_DESCRIPTION')
make_head(_module, 'WS_ENUM_VALUE')
make_head(_module, 'WS_ERROR')
make_head(_module, 'WS_ERROR_PROPERTY')
make_head(_module, 'WS_FAULT')
make_head(_module, 'WS_FAULT_CODE')
make_head(_module, 'WS_FAULT_DESCRIPTION')
make_head(_module, 'WS_FAULT_DETAIL_DESCRIPTION')
make_head(_module, 'WS_FAULT_REASON')
make_head(_module, 'WS_FIELD_DESCRIPTION')
make_head(_module, 'WS_FLOAT_DESCRIPTION')
make_head(_module, 'WS_FREE_CHANNEL_CALLBACK')
make_head(_module, 'WS_FREE_DECODER_CALLBACK')
make_head(_module, 'WS_FREE_ENCODER_CALLBACK')
make_head(_module, 'WS_FREE_LISTENER_CALLBACK')
make_head(_module, 'WS_GET_CERT_CALLBACK')
make_head(_module, 'WS_GET_CHANNEL_PROPERTY_CALLBACK')
make_head(_module, 'WS_GET_LISTENER_PROPERTY_CALLBACK')
make_head(_module, 'WS_GUID_DESCRIPTION')
make_head(_module, 'WS_HEAP')
make_head(_module, 'WS_HEAP_PROPERTIES')
make_head(_module, 'WS_HEAP_PROPERTY')
make_head(_module, 'WS_HOST_NAMES')
make_head(_module, 'WS_HTTPS_URL')
make_head(_module, 'WS_HTTP_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_HEADER_AUTH_SECURITY_BINDING')
make_head(_module, 'WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_HEADER_MAPPING')
make_head(_module, 'WS_HTTP_MESSAGE_MAPPING')
make_head(_module, 'WS_HTTP_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_REDIRECT_CALLBACK')
make_head(_module, 'WS_HTTP_REDIRECT_CALLBACK_CONTEXT')
make_head(_module, 'WS_HTTP_SSL_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_SSL_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE')
make_head(_module, 'WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION')
make_head(_module, 'WS_HTTP_URL')
make_head(_module, 'WS_INT16_DESCRIPTION')
make_head(_module, 'WS_INT32_DESCRIPTION')
make_head(_module, 'WS_INT64_DESCRIPTION')
make_head(_module, 'WS_INT8_DESCRIPTION')
make_head(_module, 'WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_IS_DEFAULT_VALUE_CALLBACK')
make_head(_module, 'WS_ITEM_RANGE')
make_head(_module, 'WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING')
make_head(_module, 'WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_LISTENER')
make_head(_module, 'WS_LISTENER_PROPERTIES')
make_head(_module, 'WS_LISTENER_PROPERTY')
make_head(_module, 'WS_MESSAGE')
make_head(_module, 'WS_MESSAGE_DESCRIPTION')
make_head(_module, 'WS_MESSAGE_DONE_CALLBACK')
make_head(_module, 'WS_MESSAGE_PROPERTIES')
make_head(_module, 'WS_MESSAGE_PROPERTY')
make_head(_module, 'WS_METADATA')
make_head(_module, 'WS_METADATA_ENDPOINT')
make_head(_module, 'WS_METADATA_ENDPOINTS')
make_head(_module, 'WS_METADATA_PROPERTY')
make_head(_module, 'WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING')
make_head(_module, 'WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE')
make_head(_module, 'WS_NETPIPE_URL')
make_head(_module, 'WS_NETTCP_URL')
make_head(_module, 'WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL')
make_head(_module, 'WS_OPEN_CHANNEL_CALLBACK')
make_head(_module, 'WS_OPEN_LISTENER_CALLBACK')
make_head(_module, 'WS_OPERATION_CANCEL_CALLBACK')
make_head(_module, 'WS_OPERATION_CONTEXT')
make_head(_module, 'WS_OPERATION_DESCRIPTION')
make_head(_module, 'WS_OPERATION_FREE_STATE_CALLBACK')
make_head(_module, 'WS_PARAMETER_DESCRIPTION')
make_head(_module, 'WS_POLICY')
make_head(_module, 'WS_POLICY_CONSTRAINTS')
make_head(_module, 'WS_POLICY_EXTENSION')
make_head(_module, 'WS_POLICY_PROPERTIES')
make_head(_module, 'WS_POLICY_PROPERTY')
make_head(_module, 'WS_PROXY_MESSAGE_CALLBACK')
make_head(_module, 'WS_PROXY_MESSAGE_CALLBACK_CONTEXT')
make_head(_module, 'WS_PROXY_PROPERTY')
make_head(_module, 'WS_PULL_BYTES_CALLBACK')
make_head(_module, 'WS_PUSH_BYTES_CALLBACK')
make_head(_module, 'WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE')
make_head(_module, 'WS_READ_CALLBACK')
make_head(_module, 'WS_READ_MESSAGE_END_CALLBACK')
make_head(_module, 'WS_READ_MESSAGE_START_CALLBACK')
make_head(_module, 'WS_READ_TYPE_CALLBACK')
make_head(_module, 'WS_REQUEST_SECURITY_TOKEN_PROPERTY')
make_head(_module, 'WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT')
make_head(_module, 'WS_RESET_CHANNEL_CALLBACK')
make_head(_module, 'WS_RESET_LISTENER_CALLBACK')
make_head(_module, 'WS_RSA_ENDPOINT_IDENTITY')
make_head(_module, 'WS_SAML_AUTHENTICATOR')
make_head(_module, 'WS_SAML_MESSAGE_SECURITY_BINDING')
make_head(_module, 'WS_SECURITY_ALGORITHM_PROPERTY')
make_head(_module, 'WS_SECURITY_ALGORITHM_SUITE')
make_head(_module, 'WS_SECURITY_BINDING')
make_head(_module, 'WS_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_SECURITY_BINDING_PROPERTIES')
make_head(_module, 'WS_SECURITY_BINDING_PROPERTY')
make_head(_module, 'WS_SECURITY_BINDING_PROPERTY_CONSTRAINT')
make_head(_module, 'WS_SECURITY_CONSTRAINTS')
make_head(_module, 'WS_SECURITY_CONTEXT')
make_head(_module, 'WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING')
make_head(_module, 'WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_SECURITY_CONTEXT_PROPERTY')
make_head(_module, 'WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_SECURITY_DESCRIPTION')
make_head(_module, 'WS_SECURITY_KEY_HANDLE')
make_head(_module, 'WS_SECURITY_PROPERTIES')
make_head(_module, 'WS_SECURITY_PROPERTY')
make_head(_module, 'WS_SECURITY_PROPERTY_CONSTRAINT')
make_head(_module, 'WS_SECURITY_TOKEN')
make_head(_module, 'WS_SERVICE_ACCEPT_CHANNEL_CALLBACK')
make_head(_module, 'WS_SERVICE_CLOSE_CHANNEL_CALLBACK')
make_head(_module, 'WS_SERVICE_CONTRACT')
make_head(_module, 'WS_SERVICE_ENDPOINT')
make_head(_module, 'WS_SERVICE_ENDPOINT_METADATA')
make_head(_module, 'WS_SERVICE_ENDPOINT_PROPERTY')
make_head(_module, 'WS_SERVICE_HOST')
make_head(_module, 'WS_SERVICE_MESSAGE_RECEIVE_CALLBACK')
make_head(_module, 'WS_SERVICE_METADATA')
make_head(_module, 'WS_SERVICE_METADATA_DOCUMENT')
make_head(_module, 'WS_SERVICE_PROPERTY')
make_head(_module, 'WS_SERVICE_PROPERTY_ACCEPT_CALLBACK')
make_head(_module, 'WS_SERVICE_PROPERTY_CLOSE_CALLBACK')
make_head(_module, 'WS_SERVICE_PROXY')
make_head(_module, 'WS_SERVICE_SECURITY_CALLBACK')
make_head(_module, 'WS_SERVICE_SECURITY_IDENTITIES')
make_head(_module, 'WS_SERVICE_STUB_CALLBACK')
make_head(_module, 'WS_SET_CHANNEL_PROPERTY_CALLBACK')
make_head(_module, 'WS_SET_LISTENER_PROPERTY_CALLBACK')
make_head(_module, 'WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK')
make_head(_module, 'WS_SOAPUDP_URL')
make_head(_module, 'WS_SPN_ENDPOINT_IDENTITY')
make_head(_module, 'WS_SSL_TRANSPORT_SECURITY_BINDING')
make_head(_module, 'WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_STRING')
make_head(_module, 'WS_STRING_DESCRIPTION')
make_head(_module, 'WS_STRING_USERNAME_CREDENTIAL')
make_head(_module, 'WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL')
make_head(_module, 'WS_STRUCT_DESCRIPTION')
make_head(_module, 'WS_SUBJECT_NAME_CERT_CREDENTIAL')
make_head(_module, 'WS_TCP_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_POLICY_DESCRIPTION')
make_head(_module, 'WS_TCP_SSPI_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION')
make_head(_module, 'WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION')
make_head(_module, 'WS_TCP_SSPI_POLICY_DESCRIPTION')
make_head(_module, 'WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING')
make_head(_module, 'WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION')
make_head(_module, 'WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE')
make_head(_module, 'WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION')
make_head(_module, 'WS_THUMBPRINT_CERT_CREDENTIAL')
make_head(_module, 'WS_TIMESPAN')
make_head(_module, 'WS_TIMESPAN_DESCRIPTION')
make_head(_module, 'WS_UINT16_DESCRIPTION')
make_head(_module, 'WS_UINT32_DESCRIPTION')
make_head(_module, 'WS_UINT64_DESCRIPTION')
make_head(_module, 'WS_UINT8_DESCRIPTION')
make_head(_module, 'WS_UNION_DESCRIPTION')
make_head(_module, 'WS_UNION_FIELD_DESCRIPTION')
make_head(_module, 'WS_UNIQUE_ID')
make_head(_module, 'WS_UNIQUE_ID_DESCRIPTION')
make_head(_module, 'WS_UNKNOWN_ENDPOINT_IDENTITY')
make_head(_module, 'WS_UPN_ENDPOINT_IDENTITY')
make_head(_module, 'WS_URL')
make_head(_module, 'WS_USERNAME_CREDENTIAL')
make_head(_module, 'WS_USERNAME_MESSAGE_SECURITY_BINDING')
make_head(_module, 'WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT')
make_head(_module, 'WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION')
make_head(_module, 'WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE')
make_head(_module, 'WS_UTF8_ARRAY_DESCRIPTION')
make_head(_module, 'WS_VALIDATE_PASSWORD_CALLBACK')
make_head(_module, 'WS_VALIDATE_SAML_CALLBACK')
make_head(_module, 'WS_VOID_DESCRIPTION')
make_head(_module, 'WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL')
make_head(_module, 'WS_WRITE_CALLBACK')
make_head(_module, 'WS_WRITE_MESSAGE_END_CALLBACK')
make_head(_module, 'WS_WRITE_MESSAGE_START_CALLBACK')
make_head(_module, 'WS_WRITE_TYPE_CALLBACK')
make_head(_module, 'WS_WSZ_DESCRIPTION')
make_head(_module, 'WS_XML_ATTRIBUTE')
make_head(_module, 'WS_XML_BASE64_TEXT')
make_head(_module, 'WS_XML_BOOL_TEXT')
make_head(_module, 'WS_XML_BUFFER')
make_head(_module, 'WS_XML_BUFFER_PROPERTY')
make_head(_module, 'WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES')
make_head(_module, 'WS_XML_CANONICALIZATION_PROPERTY')
make_head(_module, 'WS_XML_COMMENT_NODE')
make_head(_module, 'WS_XML_DATETIME_TEXT')
make_head(_module, 'WS_XML_DECIMAL_TEXT')
make_head(_module, 'WS_XML_DICTIONARY')
make_head(_module, 'WS_XML_DOUBLE_TEXT')
make_head(_module, 'WS_XML_ELEMENT_NODE')
make_head(_module, 'WS_XML_FLOAT_TEXT')
make_head(_module, 'WS_XML_GUID_TEXT')
make_head(_module, 'WS_XML_INT32_TEXT')
make_head(_module, 'WS_XML_INT64_TEXT')
make_head(_module, 'WS_XML_LIST_TEXT')
make_head(_module, 'WS_XML_NODE')
make_head(_module, 'WS_XML_NODE_POSITION')
make_head(_module, 'WS_XML_QNAME')
make_head(_module, 'WS_XML_QNAME_DESCRIPTION')
make_head(_module, 'WS_XML_QNAME_TEXT')
make_head(_module, 'WS_XML_READER')
make_head(_module, 'WS_XML_READER_BINARY_ENCODING')
make_head(_module, 'WS_XML_READER_BUFFER_INPUT')
make_head(_module, 'WS_XML_READER_ENCODING')
make_head(_module, 'WS_XML_READER_INPUT')
make_head(_module, 'WS_XML_READER_MTOM_ENCODING')
make_head(_module, 'WS_XML_READER_PROPERTIES')
make_head(_module, 'WS_XML_READER_PROPERTY')
make_head(_module, 'WS_XML_READER_RAW_ENCODING')
make_head(_module, 'WS_XML_READER_STREAM_INPUT')
make_head(_module, 'WS_XML_READER_TEXT_ENCODING')
make_head(_module, 'WS_XML_SECURITY_TOKEN_PROPERTY')
make_head(_module, 'WS_XML_STRING')
make_head(_module, 'WS_XML_STRING_DESCRIPTION')
make_head(_module, 'WS_XML_TEXT')
make_head(_module, 'WS_XML_TEXT_NODE')
make_head(_module, 'WS_XML_TIMESPAN_TEXT')
make_head(_module, 'WS_XML_TOKEN_MESSAGE_SECURITY_BINDING')
make_head(_module, 'WS_XML_UINT64_TEXT')
make_head(_module, 'WS_XML_UNIQUE_ID_TEXT')
make_head(_module, 'WS_XML_UTF16_TEXT')
make_head(_module, 'WS_XML_UTF8_TEXT')
make_head(_module, 'WS_XML_WRITER')
make_head(_module, 'WS_XML_WRITER_BINARY_ENCODING')
make_head(_module, 'WS_XML_WRITER_BUFFER_OUTPUT')
make_head(_module, 'WS_XML_WRITER_ENCODING')
make_head(_module, 'WS_XML_WRITER_MTOM_ENCODING')
make_head(_module, 'WS_XML_WRITER_OUTPUT')
make_head(_module, 'WS_XML_WRITER_PROPERTIES')
make_head(_module, 'WS_XML_WRITER_PROPERTY')
make_head(_module, 'WS_XML_WRITER_RAW_ENCODING')
make_head(_module, 'WS_XML_WRITER_STREAM_OUTPUT')
make_head(_module, 'WS_XML_WRITER_TEXT_ENCODING')
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
_arch_optional = [
]
