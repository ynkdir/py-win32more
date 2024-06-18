from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WindowsWebServices
import win32more.Windows.Win32.Security.Authentication.Identity
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
WEBAUTHN_API_VERSION_1: UInt32 = 1
WEBAUTHN_API_VERSION_2: UInt32 = 2
WEBAUTHN_API_VERSION_3: UInt32 = 3
WEBAUTHN_API_VERSION_4: UInt32 = 4
WEBAUTHN_API_VERSION_5: UInt32 = 5
WEBAUTHN_API_VERSION_6: UInt32 = 6
WEBAUTHN_API_VERSION_7: UInt32 = 7
WEBAUTHN_API_CURRENT_VERSION: UInt32 = 7
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
WEBAUTHN_CTAP_TRANSPORT_HYBRID: UInt32 = 32
WEBAUTHN_CTAP_TRANSPORT_FLAGS_MASK: UInt32 = 63
WEBAUTHN_CREDENTIAL_EX_CURRENT_VERSION: UInt32 = 1
CTAPCBOR_HYBRID_STORAGE_LINKED_DATA_VERSION_1: UInt32 = 1
CTAPCBOR_HYBRID_STORAGE_LINKED_DATA_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_1: UInt32 = 1
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_2: UInt32 = 2
WEBAUTHN_CREDENTIAL_DETAILS_CURRENT_VERSION: UInt32 = 2
WEBAUTHN_GET_CREDENTIALS_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_GET_CREDENTIALS_OPTIONS_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAP_ONE_HMAC_SECRET_LENGTH: UInt32 = 32
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
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_5: UInt32 = 5
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_6: UInt32 = 6
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_7: UInt32 = 7
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_CURRENT_VERSION: UInt32 = 7
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_NONE: UInt32 = 0
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_GET: UInt32 = 1
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_SET: UInt32 = 2
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_DELETE: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_2: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_3: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_4: UInt32 = 4
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_5: UInt32 = 5
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_6: UInt32 = 6
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_7: UInt32 = 7
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_CURRENT_VERSION: UInt32 = 7
WEBAUTHN_AUTHENTICATOR_HMAC_SECRET_VALUES_FLAG: UInt32 = 1048576
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
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_5: UInt32 = 5
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_6: UInt32 = 6
WEBAUTHN_CREDENTIAL_ATTESTATION_CURRENT_VERSION: UInt32 = 6
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
WEBAUTHN_ASSERTION_VERSION_3: UInt32 = 3
WEBAUTHN_ASSERTION_VERSION_4: UInt32 = 4
WEBAUTHN_ASSERTION_VERSION_5: UInt32 = 5
WEBAUTHN_ASSERTION_CURRENT_VERSION: UInt32 = 5
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
def WsStartReaderCanonicalization(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: VoidPtr, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEndReaderCanonicalization(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsStartWriterCanonicalization(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: VoidPtr, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEndWriterCanonicalization(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateXmlBuffer(heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY), propertyCount: UInt32, buffer: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveNode(nodePosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateReader(properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY), propertyCount: UInt32, reader: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetInput(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), encoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING), input: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetInputToBuffer(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), buffer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeReader(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetReaderProperty(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetReaderNode(xmlReader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), node: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFillReader(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), minSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadStartElement(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadToStartElement(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), found: POINTER(win32more.Windows.Win32.Foundation.BOOL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadStartAttribute(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), attributeIndex: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndAttribute(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadNode(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSkipNode(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndElement(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFindAttribute(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), required: win32more.Windows.Win32.Foundation.BOOL, attributeIndex: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadValue(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadChars(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), chars: win32more.Windows.Win32.Foundation.PWSTR, maxCharCount: UInt32, actualCharCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadCharsUtf8(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), bytes: POINTER(Byte), maxByteCount: UInt32, actualByteCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadBytes(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), bytes: VoidPtr, maxByteCount: UInt32, actualByteCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadArray(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, array: VoidPtr, arraySize: UInt32, itemOffset: UInt32, itemCount: UInt32, actualItemCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetReaderPosition(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), nodePosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetReaderPosition(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), nodePosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMoveReader(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), moveTo: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO, found: POINTER(win32more.Windows.Win32.Foundation.BOOL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateWriter(properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY), propertyCount: UInt32, writer: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeWriter(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER)) -> Void: ...
@winfunctype('webservices.dll')
def WsSetOutput(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), encoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING), output: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetOutputToBuffer(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), buffer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY), propertyCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetWriterProperty(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFlushWriter(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), minSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartElement(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndStartElement(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlnsAttribute(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), singleQuote: win32more.Windows.Win32.Foundation.BOOL, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartAttribute(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), singleQuote: win32more.Windows.Win32.Foundation.BOOL, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndAttribute(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteValue(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlBuffer(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), xmlBuffer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadXmlBuffer(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), xmlBuffer: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteXmlBufferToBytes(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), xmlBuffer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), encoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY), propertyCount: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), bytes: POINTER(VoidPtr), byteCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadXmlBufferFromBytes(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), encoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY), propertyCount: UInt32, bytes: VoidPtr, byteCount: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), xmlBuffer: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteArray(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE, array: VoidPtr, arraySize: UInt32, itemOffset: UInt32, itemCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteQualifiedName(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteChars(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), chars: win32more.Windows.Win32.Foundation.PWSTR, charCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteCharsUtf8(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), bytes: POINTER(Byte), byteCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteBytes(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), bytes: VoidPtr, byteCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsPushBytes(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PUSH_BYTES_CALLBACK, callbackState: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsPullBytes(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PULL_BYTES_CALLBACK, callbackState: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndElement(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteText(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), text: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteStartCData(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEndCData(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteNode(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), node: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPrefixFromNamespace(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), required: win32more.Windows.Win32.Foundation.BOOL, prefix: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetWriterPosition(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), nodePosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetWriterPosition(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), nodePosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMoveWriter(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), moveTo: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO, found: POINTER(win32more.Windows.Win32.Foundation.BOOL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsTrimXmlWhitespace(chars: win32more.Windows.Win32.Foundation.PWSTR, charCount: UInt32, trimmedChars: POINTER(POINTER(UInt16)), trimmedCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsVerifyXmlNCName(ncNameChars: win32more.Windows.Win32.Foundation.PWSTR, ncNameCharCount: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsXmlStringEquals(string1: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), string2: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetNamespaceFromPrefix(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), required: win32more.Windows.Win32.Foundation.BOOL, ns: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadQualifiedName(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetXmlAttribute(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), valueChars: POINTER(POINTER(UInt16)), valueCharCount: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCopyNode(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAsyncExecute(asyncState: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_STATE), operation: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_FUNCTION, callbackModel: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateChannel(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY), propertyCount: UInt32, securityDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION), channel: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), endpointAddress: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendMessage(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), messageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, bodyValue: VoidPtr, bodyValueSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReceiveMessage(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), messageDescriptions: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION)), messageDescriptionCount: UInt32, receiveOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_RECEIVE_OPTION, readBodyOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, index: POINTER(UInt32), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRequestReply(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), requestMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), requestMessageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, requestBodyValue: VoidPtr, requestBodyValueSize: UInt32, replyMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), replyMessageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION), readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendReplyMessage(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), replyMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), replyMessageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, replyBodyValue: VoidPtr, replyBodyValueSize: UInt32, requestMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSendFaultMessageForError(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), replyMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), faultError: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), faultErrorCode: win32more.Windows.Win32.Foundation.HRESULT, faultDisclosure: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE, requestMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetChannelProperty(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetChannelProperty(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteMessageStart(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteMessageEnd(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMessageStart(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMessageEnd(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbandonMessage(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsShutdownSessionChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetOperationContextProperty(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetDictionary(encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING, dictionary: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEndpointAddressExtension(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), endpointAddress: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), extensionType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_EXTENSION_TYPE, readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateError(properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY), propertyCount: UInt32, error: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddErrorString(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), string: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetErrorString(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), index: UInt32, string: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCopyError(source: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), destination: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetErrorProperty(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID, buffer: VoidPtr, bufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetErrorProperty(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID, value: VoidPtr, valueSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetError(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeError(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetFaultErrorProperty(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID, buffer: VoidPtr, bufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetFaultErrorProperty(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID, value: VoidPtr, valueSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateFaultFromError(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), faultErrorCode: win32more.Windows.Win32.Foundation.HRESULT, faultDisclosure: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), fault: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetFaultErrorDetail(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), faultDetailDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetFaultErrorDetail(error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR), faultDetailDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION), readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateHeap(maxSize: UIntPtr, trimSize: UIntPtr, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY), propertyCount: UInt32, heap: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAlloc(heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), size: UIntPtr, ptr: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetHeapProperty(heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetHeap(heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeHeap(heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP)) -> Void: ...
@winfunctype('webservices.dll')
def WsCreateListener(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY), propertyCount: UInt32, securityDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION), listener: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), url: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAcceptChannel(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetListenerProperty(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetListenerProperty(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateChannelForListener(listener: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY), propertyCount: UInt32, channel: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMessage(envelopeVersion: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION, addressingVersion: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY), propertyCount: UInt32, message: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMessageForChannel(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY), propertyCount: UInt32, message: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsInitializeMessage(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), initialization: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION, sourceMessage: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsResetMessage(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeMessage(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE)) -> Void: ...
@winfunctype('webservices.dll')
def WsGetHeaderAttributes(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), headerAttributes: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetCustomHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), customHeaderDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), repeatingOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION, headerIndex: UInt32, readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, headerAttributes: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE, valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveCustomHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), headerNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddCustomHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, headerAttributes: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddMappedHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRemoveMappedHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMappedHeader(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), repeatingOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION, headerIndex: UInt32, valueType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteBody(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), bodyDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadBody(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), bodyDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEnvelopeStart(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), doneCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK, doneCallbackState: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteEnvelopeEnd(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEnvelopeStart(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), doneCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK, doneCallbackState: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadEnvelopeEnd(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMessageProperty(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsSetMessageProperty(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAddressMessage(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), address: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCheckMustUnderstandHeaders(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMarkHeaderAsUnderstood(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), headerPosition: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_POSITION), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFillBody(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), minSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFlushBody(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), minSize: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRequestSecurityToken(channel: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY), propertyCount: UInt32, token: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN)), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetSecurityTokenProperty(securityToken: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateXmlSecurityToken(tokenXml: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), tokenKey: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY), propertyCount: UInt32, token: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeSecurityToken(token: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN)) -> Void: ...
@winfunctype('webservices.dll')
def WsRevokeSecurityContext(securityContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetSecurityContextProperty(securityContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadElement(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), elementDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadAttribute(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), attributeDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION), readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadType(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), typeMapping: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, typeDescription: VoidPtr, readOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteElement(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), elementDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteAttribute(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), attributeDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION), writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsWriteType(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), typeMapping: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE, typeDescription: VoidPtr, writeOption: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsRegisterOperationForCancel(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), cancelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CANCEL_CALLBACK, freestateCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_FREE_STATE_CALLBACK, userState: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetServiceHostProperty(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceHost(endpoints: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT)), endpointCount: UInt16, serviceProperties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY), servicePropertyCount: UInt32, serviceHost: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenServiceHost(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseServiceHost(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortServiceHost(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeServiceHost(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetServiceHost(serviceHost: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetServiceProxyProperty(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceProxy(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING, securityDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION), properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY), propertyCount: UInt32, channelProperties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY), channelPropertyCount: UInt32, serviceProxy: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsOpenServiceProxy(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), address: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCloseServiceProxy(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbortServiceProxy(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeServiceProxy(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetServiceProxy(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsAbandonCall(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), callId: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCall(serviceProxy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY), operation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION), arguments: POINTER(VoidPtr), heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), callProperties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY), callPropertyCount: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsDecodeUrl(url: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), flags: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), outUrl: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsEncodeUrl(url: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL), flags: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), outUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCombineUrl(baseUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), referenceUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), flags: UInt32, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), resultUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsDateTimeToFileTime(dateTime: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME), fileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFileTimeToDateTime(fileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), dateTime: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateMetadata(properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY), propertyCount: UInt32, metadata: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsReadMetadata(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA), reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), url: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsFreeMetadata(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA)) -> Void: ...
@winfunctype('webservices.dll')
def WsResetMetadata(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMetadataProperty(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMissingMetadataDocumentAddress(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA), address: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetMetadataEndpoints(metadata: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA), endpoints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_ENDPOINTS), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsMatchPolicyAlternative(policy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY), alternativeIndex: UInt32, policyConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_CONSTRAINTS), matchRequired: win32more.Windows.Win32.Foundation.BOOL, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPolicyProperty(policy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY), id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsGetPolicyAlternativeCount(policy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY), count: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceProxyFromTemplate(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY), propertyCount: UInt32, templateType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE, templateValue: VoidPtr, templateSize: UInt32, templateDescription: VoidPtr, templateDescriptionSize: UInt32, serviceProxy: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webservices.dll')
def WsCreateServiceEndpointFromTemplate(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY), propertyCount: UInt32, addressUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), contract: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CONTRACT), authorizationCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), templateType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE, templateValue: VoidPtr, templateSize: UInt32, templateDescription: VoidPtr, templateDescriptionSize: UInt32, serviceEndpoint: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetApiVersionNumber() -> UInt32: ...
@winfunctype('webauthn.dll')
def WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable(pbIsUserVerifyingPlatformAuthenticatorAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorMakeCredential(hWnd: win32more.Windows.Win32.Foundation.HWND, pRpInformation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_RP_ENTITY_INFORMATION), pUserInformation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_USER_ENTITY_INFORMATION), pPubKeyCredParams: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS), pWebAuthNClientData: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA), pWebAuthNMakeCredentialOptions: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS), ppWebAuthNCredentialAttestation: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorGetAssertion(hWnd: win32more.Windows.Win32.Foundation.HWND, pwszRpId: win32more.Windows.Win32.Foundation.PWSTR, pWebAuthNClientData: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA), pWebAuthNGetAssertionOptions: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS), ppWebAuthNAssertion: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_ASSERTION))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeCredentialAttestation(pWebAuthNCredentialAttestation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeAssertion(pWebAuthNAssertion: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_ASSERTION)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNGetCancellationId(pCancellationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNCancelCurrentOperation(pCancellationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetPlatformCredentialList(pGetCredentialsOptions: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_GET_CREDENTIALS_OPTIONS), ppCredentialDetailsList: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_DETAILS_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreePlatformCredentialList(pCredentialDetailsList: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_DETAILS_LIST)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNDeletePlatformCredential(cbCredentialId: UInt32, pbCredentialId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetErrorName(hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('webauthn.dll')
def WebAuthNGetW3CExceptionDOMError(hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class CTAPCBOR_HYBRID_STORAGE_LINKED_DATA(Structure):
    dwVersion: UInt32
    cbContactId: UInt32
    pbContactId: POINTER(Byte)
    cbLinkId: UInt32
    pbLinkId: POINTER(Byte)
    cbLinkSecret: UInt32
    pbLinkSecret: POINTER(Byte)
    cbPublicKey: UInt32
    pbPublicKey: POINTER(Byte)
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    wEncodedTunnelServerDomain: UInt16
class IContentPrefetcherTaskTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1b35a14a-6094-4799-a60e-e474e15d4dc9}')
    @commethod(6)
    def TriggerContentPrefetcherTask(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsRegisteredForContentPrefetch(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, isRegistered: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WEBAUTHN_ASSERTION(Structure):
    dwVersion: UInt32
    cbAuthenticatorData: UInt32
    pbAuthenticatorData: POINTER(Byte)
    cbSignature: UInt32
    pbSignature: POINTER(Byte)
    Credential: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL
    cbUserId: UInt32
    pbUserId: POINTER(Byte)
    Extensions: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: POINTER(Byte)
    dwCredLargeBlobStatus: UInt32
    pHmacSecret: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_HMAC_SECRET_SALT)
    dwUsedTransport: UInt32
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
class WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS
    Extensions: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    dwUserVerificationRequirement: UInt32
    dwFlags: UInt32
    pwszU2fAppId: win32more.Windows.Win32.Foundation.PWSTR
    pbU2fAppId: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pCancellationId: POINTER(Guid)
    pAllowCredentialList: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST)
    dwCredLargeBlobOperation: UInt32
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: POINTER(Byte)
    pHmacSecretSaltValues: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_HMAC_SECRET_SALT_VALUES)
    bBrowserInPrivateMode: win32more.Windows.Win32.Foundation.BOOL
    pLinkedDevice: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.CTAPCBOR_HYBRID_STORAGE_LINKED_DATA)
    bAutoFill: win32more.Windows.Win32.Foundation.BOOL
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS
    Extensions: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    bRequireResidentKey: win32more.Windows.Win32.Foundation.BOOL
    dwUserVerificationRequirement: UInt32
    dwAttestationConveyancePreference: UInt32
    dwFlags: UInt32
    pCancellationId: POINTER(Guid)
    pExcludeCredentialList: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST)
    dwEnterpriseAttestation: UInt32
    dwLargeBlobSupport: UInt32
    bPreferResidentKey: win32more.Windows.Win32.Foundation.BOOL
    bBrowserInPrivateMode: win32more.Windows.Win32.Foundation.BOOL
    bEnablePrf: win32more.Windows.Win32.Foundation.BOOL
    pLinkedDevice: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.CTAPCBOR_HYBRID_STORAGE_LINKED_DATA)
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class WEBAUTHN_CLIENT_DATA(Structure):
    dwVersion: UInt32
    cbClientDataJSON: UInt32
    pbClientDataJSON: POINTER(Byte)
    pwszHashAlgId: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_COMMON_ATTESTATION(Structure):
    dwVersion: UInt32
    pwszAlg: win32more.Windows.Win32.Foundation.PWSTR
    lAlg: Int32
    cbSignature: UInt32
    pbSignature: POINTER(Byte)
    cX5c: UInt32
    pX5c: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_X5C)
    pwszVer: win32more.Windows.Win32.Foundation.PWSTR
    cbCertInfo: UInt32
    pbCertInfo: POINTER(Byte)
    cbPubArea: UInt32
    pbPubArea: POINTER(Byte)
class WEBAUTHN_COSE_CREDENTIAL_PARAMETER(Structure):
    dwVersion: UInt32
    pwszCredentialType: win32more.Windows.Win32.Foundation.PWSTR
    lAlg: Int32
class WEBAUTHN_COSE_CREDENTIAL_PARAMETERS(Structure):
    cCredentialParameters: UInt32
    pCredentialParameters: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETER)
class WEBAUTHN_CREDENTIAL(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: POINTER(Byte)
    pwszCredentialType: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_CREDENTIALS(Structure):
    cCredentials: UInt32
    pCredentials: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL)
class WEBAUTHN_CREDENTIAL_ATTESTATION(Structure):
    dwVersion: UInt32
    pwszFormatType: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorData: UInt32
    pbAuthenticatorData: POINTER(Byte)
    cbAttestation: UInt32
    pbAttestation: POINTER(Byte)
    dwAttestationDecodeType: UInt32
    pvAttestationDecode: VoidPtr
    cbAttestationObject: UInt32
    pbAttestationObject: POINTER(Byte)
    cbCredentialId: UInt32
    pbCredentialId: POINTER(Byte)
    Extensions: win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS
    dwUsedTransport: UInt32
    bEpAtt: win32more.Windows.Win32.Foundation.BOOL
    bLargeBlobSupported: win32more.Windows.Win32.Foundation.BOOL
    bResidentKey: win32more.Windows.Win32.Foundation.BOOL
    bPrfEnabled: win32more.Windows.Win32.Foundation.BOOL
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
class WEBAUTHN_CREDENTIAL_DETAILS(Structure):
    dwVersion: UInt32
    cbCredentialID: UInt32
    pbCredentialID: POINTER(Byte)
    pRpInformation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_RP_ENTITY_INFORMATION)
    pUserInformation: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_USER_ENTITY_INFORMATION)
    bRemovable: win32more.Windows.Win32.Foundation.BOOL
    bBackedUp: win32more.Windows.Win32.Foundation.BOOL
class WEBAUTHN_CREDENTIAL_DETAILS_LIST(Structure):
    cCredentialDetails: UInt32
    ppCredentialDetails: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_DETAILS))
class WEBAUTHN_CREDENTIAL_EX(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: POINTER(Byte)
    pwszCredentialType: win32more.Windows.Win32.Foundation.PWSTR
    dwTransports: UInt32
class WEBAUTHN_CREDENTIAL_LIST(Structure):
    cCredentials: UInt32
    ppCredentials: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_EX))
class WEBAUTHN_CRED_BLOB_EXTENSION(Structure):
    cbCredBlob: UInt32
    pbCredBlob: POINTER(Byte)
class WEBAUTHN_CRED_PROTECT_EXTENSION_IN(Structure):
    dwCredProtect: UInt32
    bRequireCredProtect: win32more.Windows.Win32.Foundation.BOOL
class WEBAUTHN_CRED_WITH_HMAC_SECRET_SALT(Structure):
    cbCredID: UInt32
    pbCredID: POINTER(Byte)
    pHmacSecretSalt: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_HMAC_SECRET_SALT)
class WEBAUTHN_EXTENSION(Structure):
    pwszExtensionIdentifier: win32more.Windows.Win32.Foundation.PWSTR
    cbExtension: UInt32
    pvExtension: VoidPtr
class WEBAUTHN_EXTENSIONS(Structure):
    cExtensions: UInt32
    pExtensions: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_EXTENSION)
class WEBAUTHN_GET_CREDENTIALS_OPTIONS(Structure):
    dwVersion: UInt32
    pwszRpId: win32more.Windows.Win32.Foundation.PWSTR
    bBrowserInPrivateMode: win32more.Windows.Win32.Foundation.BOOL
class WEBAUTHN_HMAC_SECRET_SALT(Structure):
    cbFirst: UInt32
    pbFirst: POINTER(Byte)
    cbSecond: UInt32
    pbSecond: POINTER(Byte)
class WEBAUTHN_HMAC_SECRET_SALT_VALUES(Structure):
    pGlobalHmacSalt: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_HMAC_SECRET_SALT)
    cCredWithHmacSecretSaltList: UInt32
    pCredWithHmacSecretSaltList: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WEBAUTHN_CRED_WITH_HMAC_SECRET_SALT)
class WEBAUTHN_RP_ENTITY_INFORMATION(Structure):
    dwVersion: UInt32
    pwszId: win32more.Windows.Win32.Foundation.PWSTR
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    pwszIcon: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_USER_ENTITY_INFORMATION(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: POINTER(Byte)
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    pwszIcon: win32more.Windows.Win32.Foundation.PWSTR
    pwszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_X5C(Structure):
    cbData: UInt32
    pbData: POINTER(Byte)
@winfunctype_pointer
def WS_ABANDON_MESSAGE_CALLBACK(channelInstance: VoidPtr, message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ABORT_CHANNEL_CALLBACK(channelInstance: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ABORT_LISTENER_CALLBACK(listenerInstance: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ACCEPT_CHANNEL_CALLBACK(listenerInstance: VoidPtr, channelInstance: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_ADDRESSING_VERSION = Int32
WS_ADDRESSING_VERSION_0_9: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION = 1
WS_ADDRESSING_VERSION_1_0: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION = 2
WS_ADDRESSING_VERSION_TRANSPORT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION = 3
class WS_ANY_ATTRIBUTE(Structure):
    localName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    ns: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    value: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT)
class WS_ANY_ATTRIBUTES(Structure):
    attributes: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ANY_ATTRIBUTE)
    attributeCount: UInt32
@winfunctype_pointer
def WS_ASYNC_CALLBACK(errorCode: win32more.Windows.Win32.Foundation.HRESULT, callbackModel: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: VoidPtr) -> Void: ...
class WS_ASYNC_CONTEXT(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CALLBACK
    callbackState: VoidPtr
@winfunctype_pointer
def WS_ASYNC_FUNCTION(hr: win32more.Windows.Win32.Foundation.HRESULT, callbackModel: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL, callbackState: VoidPtr, next: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_OPERATION), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_ASYNC_OPERATION(Structure):
    function: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_FUNCTION
class WS_ASYNC_STATE(Structure):
    internal0: VoidPtr
    internal1: VoidPtr
    internal2: VoidPtr
    internal3: VoidPtr
    internal4: VoidPtr
class WS_ATTRIBUTE_DESCRIPTION(Structure):
    attributeLocalName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    attributeNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: VoidPtr
WS_BINDING_TEMPLATE_TYPE = Int32
WS_HTTP_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 0
WS_HTTP_SSL_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 1
WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 2
WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 3
WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 4
WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 5
WS_TCP_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 6
WS_TCP_SSPI_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 7
WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 8
WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 9
WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 10
WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 11
WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 12
WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE = 13
class WS_BOOL_DESCRIPTION(Structure):
    value: win32more.Windows.Win32.Foundation.BOOL
class WS_BUFFERS(Structure):
    bufferCount: UInt32
    buffers: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES)
class WS_BYTES(Structure):
    length: UInt32
    bytes: POINTER(Byte)
class WS_BYTES_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
class WS_BYTE_ARRAY_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
WS_CALLBACK_MODEL = Int32
WS_SHORT_CALLBACK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL = 0
WS_LONG_CALLBACK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALLBACK_MODEL = 1
class WS_CALL_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_CALL_PROPERTY_ID = Int32
WS_CALL_PROPERTY_CHECK_MUST_UNDERSTAND: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID = 0
WS_CALL_PROPERTY_SEND_MESSAGE_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID = 1
WS_CALL_PROPERTY_RECEIVE_MESSAGE_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID = 2
WS_CALL_PROPERTY_CALL_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID = 3
class WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    provider: UIntPtr
    keySpec: UInt32
@winfunctype_pointer
def WS_CERTIFICATE_VALIDATION_CALLBACK(certContext: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), state: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERTIFICATE_VALIDATION_CALLBACK
    state: VoidPtr
class WS_CERT_CREDENTIAL(Structure):
    credentialType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE
WS_CERT_CREDENTIAL_TYPE = Int32
WS_SUBJECT_NAME_CERT_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE = 1
WS_THUMBPRINT_CERT_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE = 2
WS_CUSTOM_CERT_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE = 3
class WS_CERT_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    rawCertificateData: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES
@winfunctype_pointer
def WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK(certIssuerListNotificationCallbackState: VoidPtr, issuerList: POINTER(win32more.Windows.Win32.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_CERT_SIGNED_SAML_AUTHENTICATOR(Structure):
    authenticator: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR
    trustedIssuerCerts: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    trustedIssuerCertCount: UInt32
    decryptionCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)
    samlValidator: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_SAML_CALLBACK
    samlValidatorCallbackState: VoidPtr
WS_CHANNEL = IntPtr
WS_CHANNEL_BINDING = Int32
WS_HTTP_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING = 0
WS_TCP_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING = 1
WS_UDP_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING = 2
WS_CUSTOM_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING = 3
WS_NAMEDPIPE_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING = 4
class WS_CHANNEL_DECODER(Structure):
    createContext: VoidPtr
    createDecoderCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CREATE_DECODER_CALLBACK
    decoderGetContentTypeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DECODER_GET_CONTENT_TYPE_CALLBACK
    decoderStartCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DECODER_START_CALLBACK
    decoderDecodeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DECODER_DECODE_CALLBACK
    decoderEndCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DECODER_END_CALLBACK
    freeDecoderCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FREE_DECODER_CALLBACK
class WS_CHANNEL_ENCODER(Structure):
    createContext: VoidPtr
    createEncoderCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CREATE_ENCODER_CALLBACK
    encoderGetContentTypeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_GET_CONTENT_TYPE_CALLBACK
    encoderStartCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_START_CALLBACK
    encoderEncodeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_ENCODE_CALLBACK
    encoderEndCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODER_END_CALLBACK
    freeEncoderCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FREE_ENCODER_CALLBACK
class WS_CHANNEL_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY)
    propertyCount: UInt32
class WS_CHANNEL_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
class WS_CHANNEL_PROPERTY_CONSTRAINT(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID
    allowedValues: VoidPtr
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        channelProperty: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY
WS_CHANNEL_PROPERTY_ID = Int32
WS_CHANNEL_PROPERTY_MAX_BUFFERED_MESSAGE_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 0
WS_CHANNEL_PROPERTY_MAX_STREAMED_MESSAGE_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 1
WS_CHANNEL_PROPERTY_MAX_STREAMED_START_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 2
WS_CHANNEL_PROPERTY_MAX_STREAMED_FLUSH_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 3
WS_CHANNEL_PROPERTY_ENCODING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 4
WS_CHANNEL_PROPERTY_ENVELOPE_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 5
WS_CHANNEL_PROPERTY_ADDRESSING_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 6
WS_CHANNEL_PROPERTY_MAX_SESSION_DICTIONARY_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 7
WS_CHANNEL_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 8
WS_CHANNEL_PROPERTY_ASYNC_CALLBACK_MODEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 9
WS_CHANNEL_PROPERTY_IP_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 10
WS_CHANNEL_PROPERTY_RESOLVE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 11
WS_CHANNEL_PROPERTY_CONNECT_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 12
WS_CHANNEL_PROPERTY_SEND_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 13
WS_CHANNEL_PROPERTY_RECEIVE_RESPONSE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 14
WS_CHANNEL_PROPERTY_RECEIVE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 15
WS_CHANNEL_PROPERTY_CLOSE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 16
WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 17
WS_CHANNEL_PROPERTY_TRANSFER_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 18
WS_CHANNEL_PROPERTY_MULTICAST_INTERFACE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 19
WS_CHANNEL_PROPERTY_MULTICAST_HOPS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 20
WS_CHANNEL_PROPERTY_REMOTE_ADDRESS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 21
WS_CHANNEL_PROPERTY_REMOTE_IP_ADDRESS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 22
WS_CHANNEL_PROPERTY_HTTP_CONNECTION_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 23
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_CALLBACKS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 24
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 25
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_INSTANCE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 26
WS_CHANNEL_PROPERTY_TRANSPORT_URL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 27
WS_CHANNEL_PROPERTY_NO_DELAY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 28
WS_CHANNEL_PROPERTY_SEND_KEEP_ALIVES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 29
WS_CHANNEL_PROPERTY_KEEP_ALIVE_TIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 30
WS_CHANNEL_PROPERTY_KEEP_ALIVE_INTERVAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 31
WS_CHANNEL_PROPERTY_MAX_HTTP_SERVER_CONNECTIONS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 32
WS_CHANNEL_PROPERTY_IS_SESSION_SHUT_DOWN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 33
WS_CHANNEL_PROPERTY_CHANNEL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 34
WS_CHANNEL_PROPERTY_TRIM_BUFFERED_MESSAGE_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 35
WS_CHANNEL_PROPERTY_ENCODER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 36
WS_CHANNEL_PROPERTY_DECODER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 37
WS_CHANNEL_PROPERTY_PROTECTION_LEVEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 38
WS_CHANNEL_PROPERTY_COOKIE_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 39
WS_CHANNEL_PROPERTY_HTTP_PROXY_SETTING_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 40
WS_CHANNEL_PROPERTY_CUSTOM_HTTP_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 41
WS_CHANNEL_PROPERTY_HTTP_MESSAGE_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 42
WS_CHANNEL_PROPERTY_ENABLE_HTTP_REDIRECT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 43
WS_CHANNEL_PROPERTY_HTTP_REDIRECT_CALLBACK_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 44
WS_CHANNEL_PROPERTY_FAULTS_AS_ERRORS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 45
WS_CHANNEL_PROPERTY_ALLOW_UNSECURED_FAULTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 46
WS_CHANNEL_PROPERTY_HTTP_SERVER_SPN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 47
WS_CHANNEL_PROPERTY_HTTP_PROXY_SPN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 48
WS_CHANNEL_PROPERTY_MAX_HTTP_REQUEST_HEADERS_BUFFER_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID = 49
WS_CHANNEL_STATE = Int32
WS_CHANNEL_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 0
WS_CHANNEL_STATE_OPENING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 1
WS_CHANNEL_STATE_ACCEPTING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 2
WS_CHANNEL_STATE_OPEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 3
WS_CHANNEL_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 4
WS_CHANNEL_STATE_CLOSING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 5
WS_CHANNEL_STATE_CLOSED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_STATE = 6
WS_CHANNEL_TYPE = Int32
WS_CHANNEL_TYPE_INPUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 1
WS_CHANNEL_TYPE_OUTPUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 2
WS_CHANNEL_TYPE_SESSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 4
WS_CHANNEL_TYPE_INPUT_SESSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 5
WS_CHANNEL_TYPE_OUTPUT_SESSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 6
WS_CHANNEL_TYPE_DUPLEX: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 3
WS_CHANNEL_TYPE_DUPLEX_SESSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 7
WS_CHANNEL_TYPE_REQUEST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 8
WS_CHANNEL_TYPE_REPLY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE = 16
WS_CHARSET = Int32
WS_CHARSET_AUTO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET = 0
WS_CHARSET_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET = 1
WS_CHARSET_UTF16LE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET = 2
WS_CHARSET_UTF16BE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET = 3
class WS_CHAR_ARRAY_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
@winfunctype_pointer
def WS_CLOSE_CHANNEL_CALLBACK(channelInstance: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CLOSE_LISTENER_CALLBACK(listenerInstance: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_CONTRACT_DESCRIPTION(Structure):
    operationCount: UInt32
    operations: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION))
WS_COOKIE_MODE = Int32
WS_MANUAL_COOKIE_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_COOKIE_MODE = 1
WS_AUTO_COOKIE_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_COOKIE_MODE = 2
@winfunctype_pointer
def WS_CREATE_CHANNEL_CALLBACK(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, channelParameters: VoidPtr, channelParametersSize: UInt32, channelInstance: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK(listenerInstance: VoidPtr, channelParameters: VoidPtr, channelParametersSize: UInt32, channelInstance: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_DECODER_CALLBACK(createContext: VoidPtr, readCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_CALLBACK, readContext: VoidPtr, decoderContext: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_ENCODER_CALLBACK(createContext: VoidPtr, writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeContext: VoidPtr, encoderContext: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_CREATE_LISTENER_CALLBACK(channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE, listenerParameters: VoidPtr, listenerParametersSize: UInt32, listenerInstance: POINTER(VoidPtr), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_CUSTOM_CERT_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    getCertCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_GET_CERT_CALLBACK
    getCertCallbackState: VoidPtr
    certIssuerListNotificationCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK
    certIssuerListNotificationCallbackState: VoidPtr
class WS_CUSTOM_CHANNEL_CALLBACKS(Structure):
    createChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CREATE_CHANNEL_CALLBACK
    freeChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FREE_CHANNEL_CALLBACK
    resetChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_RESET_CHANNEL_CALLBACK
    openChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPEN_CHANNEL_CALLBACK
    closeChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CLOSE_CHANNEL_CALLBACK
    abortChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ABORT_CHANNEL_CALLBACK
    getChannelPropertyCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_GET_CHANNEL_PROPERTY_CALLBACK
    setChannelPropertyCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SET_CHANNEL_PROPERTY_CALLBACK
    writeMessageStartCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_MESSAGE_START_CALLBACK
    writeMessageEndCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_MESSAGE_END_CALLBACK
    readMessageStartCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_MESSAGE_START_CALLBACK
    readMessageEndCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_MESSAGE_END_CALLBACK
    abandonMessageCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ABANDON_MESSAGE_CALLBACK
    shutdownSessionChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK
class WS_CUSTOM_HTTP_PROXY(Structure):
    servers: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    bypass: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_CUSTOM_LISTENER_CALLBACKS(Structure):
    createListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CREATE_LISTENER_CALLBACK
    freeListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FREE_LISTENER_CALLBACK
    resetListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_RESET_LISTENER_CALLBACK
    openListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPEN_LISTENER_CALLBACK
    closeListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CLOSE_LISTENER_CALLBACK
    abortListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ABORT_LISTENER_CALLBACK
    getListenerPropertyCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_GET_LISTENER_PROPERTY_CALLBACK
    setListenerPropertyCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SET_LISTENER_PROPERTY_CALLBACK
    createChannelForListenerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK
    acceptChannelCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ACCEPT_CHANNEL_CALLBACK
class WS_CUSTOM_TYPE_DESCRIPTION(Structure):
    size: UInt32
    alignment: UInt32
    readCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_TYPE_CALLBACK
    writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_TYPE_CALLBACK
    descriptionData: VoidPtr
    isDefaultValueCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_IS_DEFAULT_VALUE_CALLBACK
class WS_DATETIME(Structure):
    ticks: UInt64
    format: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_FORMAT
class WS_DATETIME_DESCRIPTION(Structure):
    minValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
    maxValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
WS_DATETIME_FORMAT = Int32
WS_DATETIME_FORMAT_UTC: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_FORMAT = 0
WS_DATETIME_FORMAT_LOCAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_FORMAT = 1
WS_DATETIME_FORMAT_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME_FORMAT = 2
class WS_DECIMAL_DESCRIPTION(Structure):
    minValue: win32more.Windows.Win32.Foundation.DECIMAL
    maxValue: win32more.Windows.Win32.Foundation.DECIMAL
@winfunctype_pointer
def WS_DECODER_DECODE_CALLBACK(encoderContext: VoidPtr, buffer: VoidPtr, maxLength: UInt32, length: POINTER(UInt32), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_END_CALLBACK(encoderContext: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_GET_CONTENT_TYPE_CALLBACK(decoderContext: VoidPtr, contentType: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), contentEncoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), newContentType: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_DECODER_START_CALLBACK(encoderContext: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_DEFAULT_VALUE(Structure):
    value: VoidPtr
    valueSize: UInt32
class WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
class WS_DISALLOWED_USER_AGENT_SUBSTRINGS(Structure):
    subStringCount: UInt32
    subStrings: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING))
class WS_DNS_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    dns: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_DOUBLE_DESCRIPTION(Structure):
    minValue: Double
    maxValue: Double
class WS_DURATION(Structure):
    negative: win32more.Windows.Win32.Foundation.BOOL
    years: UInt32
    months: UInt32
    days: UInt32
    hours: UInt32
    minutes: UInt32
    seconds: UInt32
    milliseconds: UInt32
    ticks: UInt32
@winfunctype_pointer
def WS_DURATION_COMPARISON_CALLBACK(duration1: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_DURATION), duration2: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_DURATION), result: POINTER(Int32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_DURATION_DESCRIPTION(Structure):
    minValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DURATION
    maxValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DURATION
    comparer: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DURATION_COMPARISON_CALLBACK
@winfunctype_pointer
def WS_DYNAMIC_STRING_CALLBACK(callbackState: VoidPtr, string: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING), found: POINTER(win32more.Windows.Win32.Foundation.BOOL), id: POINTER(UInt32), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_ELEMENT_DESCRIPTION(Structure):
    elementLocalName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    elementNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: VoidPtr
@winfunctype_pointer
def WS_ENCODER_ENCODE_CALLBACK(encoderContext: VoidPtr, buffers: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES), count: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_END_CALLBACK(encoderContext: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_GET_CONTENT_TYPE_CALLBACK(encoderContext: VoidPtr, contentType: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), newContentType: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), contentEncoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_ENCODER_START_CALLBACK(encoderContext: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_ENCODING = Int32
WS_ENCODING_XML_BINARY_1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 0
WS_ENCODING_XML_BINARY_SESSION_1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 1
WS_ENCODING_XML_MTOM_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 2
WS_ENCODING_XML_MTOM_UTF16BE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 3
WS_ENCODING_XML_MTOM_UTF16LE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 4
WS_ENCODING_XML_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 5
WS_ENCODING_XML_UTF16BE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 6
WS_ENCODING_XML_UTF16LE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 7
WS_ENCODING_RAW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENCODING = 8
class WS_ENDPOINT_ADDRESS(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    headers: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
    extensions: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
    identity: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY)
class WS_ENDPOINT_ADDRESS_DESCRIPTION(Structure):
    addressingVersion: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ADDRESSING_VERSION
WS_ENDPOINT_ADDRESS_EXTENSION_TYPE = Int32
WS_ENDPOINT_ADDRESS_EXTENSION_METADATA_ADDRESS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_EXTENSION_TYPE = 1
class WS_ENDPOINT_IDENTITY(Structure):
    identityType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE
WS_ENDPOINT_IDENTITY_TYPE = Int32
WS_DNS_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 1
WS_UPN_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 2
WS_SPN_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 3
WS_RSA_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 4
WS_CERT_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 5
WS_UNKNOWN_ENDPOINT_IDENTITY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE = 6
class WS_ENDPOINT_POLICY_EXTENSION(Structure):
    policyExtension: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION
    assertionName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    assertionNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        assertionValue: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
class WS_ENUM_DESCRIPTION(Structure):
    values: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENUM_VALUE)
    valueCount: UInt32
    maxByteCount: UInt32
    nameIndices: POINTER(UInt32)
class WS_ENUM_VALUE(Structure):
    value: Int32
    name: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
WS_ENVELOPE_VERSION = Int32
WS_ENVELOPE_VERSION_SOAP_1_1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION = 1
WS_ENVELOPE_VERSION_SOAP_1_2: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION = 2
WS_ENVELOPE_VERSION_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION = 3
WS_ERROR = IntPtr
class WS_ERROR_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_ERROR_PROPERTY_ID = Int32
WS_ERROR_PROPERTY_STRING_COUNT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID = 0
WS_ERROR_PROPERTY_ORIGINAL_ERROR_CODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID = 1
WS_ERROR_PROPERTY_LANGID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID = 2
WS_EXCEPTION_CODE = Int32
WS_EXCEPTION_CODE_USAGE_FAILURE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXCEPTION_CODE = -1069744128
WS_EXCEPTION_CODE_INTERNAL_FAILURE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXCEPTION_CODE = -1069744127
WS_EXTENDED_PROTECTION_POLICY = Int32
WS_EXTENDED_PROTECTION_POLICY_NEVER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXTENDED_PROTECTION_POLICY = 1
WS_EXTENDED_PROTECTION_POLICY_WHEN_SUPPORTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXTENDED_PROTECTION_POLICY = 2
WS_EXTENDED_PROTECTION_POLICY_ALWAYS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXTENDED_PROTECTION_POLICY = 3
WS_EXTENDED_PROTECTION_SCENARIO = Int32
WS_EXTENDED_PROTECTION_SCENARIO_BOUND_SERVER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXTENDED_PROTECTION_SCENARIO = 1
WS_EXTENDED_PROTECTION_SCENARIO_TERMINATED_SSL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_EXTENDED_PROTECTION_SCENARIO = 2
class WS_FAULT(Structure):
    code: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_CODE)
    reasons: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_REASON)
    reasonCount: UInt32
    actor: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    node: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    detail: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
class WS_FAULT_CODE(Structure):
    value: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_QNAME
    subCode: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_CODE)
class WS_FAULT_DESCRIPTION(Structure):
    envelopeVersion: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENVELOPE_VERSION
class WS_FAULT_DETAIL_DESCRIPTION(Structure):
    action: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    detailElementDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION)
WS_FAULT_DISCLOSURE = Int32
WS_MINIMAL_FAULT_DISCLOSURE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE = 0
WS_FULL_FAULT_DISCLOSURE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE = 1
WS_FAULT_ERROR_PROPERTY_ID = Int32
WS_FAULT_ERROR_PROPERTY_FAULT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID = 0
WS_FAULT_ERROR_PROPERTY_ACTION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID = 1
WS_FAULT_ERROR_PROPERTY_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID = 2
class WS_FAULT_REASON(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    lang: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_FIELD_DESCRIPTION(Structure):
    mapping: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING
    localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE
    typeDescription: VoidPtr
    offset: UInt32
    options: UInt32
    defaultValue: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_DEFAULT_VALUE)
    countOffset: UInt32
    itemLocalName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    itemNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    itemRange: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ITEM_RANGE)
WS_FIELD_MAPPING = Int32
WS_TYPE_ATTRIBUTE_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 0
WS_ATTRIBUTE_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 1
WS_ELEMENT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 2
WS_REPEATING_ELEMENT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 3
WS_TEXT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 4
WS_NO_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 5
WS_XML_ATTRIBUTE_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 6
WS_ELEMENT_CHOICE_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 7
WS_REPEATING_ELEMENT_CHOICE_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 8
WS_ANY_ELEMENT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 9
WS_REPEATING_ANY_ELEMENT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 10
WS_ANY_CONTENT_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 11
WS_ANY_ATTRIBUTES_FIELD_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_MAPPING = 12
class WS_FLOAT_DESCRIPTION(Structure):
    minValue: Single
    maxValue: Single
@winfunctype_pointer
def WS_FREE_CHANNEL_CALLBACK(channelInstance: VoidPtr) -> Void: ...
@winfunctype_pointer
def WS_FREE_DECODER_CALLBACK(decoderContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def WS_FREE_ENCODER_CALLBACK(encoderContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def WS_FREE_LISTENER_CALLBACK(listenerInstance: VoidPtr) -> Void: ...
@winfunctype_pointer
def WS_GET_CERT_CALLBACK(getCertCallbackState: VoidPtr, targetAddress: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), viaUri: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), cert: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT)), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_GET_CHANNEL_PROPERTY_CALLBACK(channelInstance: VoidPtr, id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_GET_LISTENER_PROPERTY_CALLBACK(listenerInstance: VoidPtr, id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_GUID_DESCRIPTION(Structure):
    value: Guid
WS_HEADER_TYPE = Int32
WS_ACTION_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 1
WS_TO_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 2
WS_MESSAGE_ID_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 3
WS_RELATES_TO_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 4
WS_FROM_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 5
WS_REPLY_TO_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 6
WS_FAULT_TO_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEADER_TYPE = 7
WS_HEAP = IntPtr
class WS_HEAP_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY)
    propertyCount: UInt32
class WS_HEAP_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_HEAP_PROPERTY_ID = Int32
WS_HEAP_PROPERTY_MAX_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID = 0
WS_HEAP_PROPERTY_TRIM_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID = 1
WS_HEAP_PROPERTY_REQUESTED_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID = 2
WS_HEAP_PROPERTY_ACTUAL_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID = 3
class WS_HOST_NAMES(Structure):
    hostNames: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)
    hostNameCount: UInt32
class WS_HTTPS_URL(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_HTTP_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    httpHeaderAuthSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
class WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    httpHeaderAuthSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
WS_HTTP_HEADER_AUTH_TARGET = Int32
WS_HTTP_HEADER_AUTH_TARGET_SERVICE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_TARGET = 1
WS_HTTP_HEADER_AUTH_TARGET_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_TARGET = 2
class WS_HTTP_HEADER_MAPPING(Structure):
    headerName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    headerMappingOptions: UInt32
class WS_HTTP_MESSAGE_MAPPING(Structure):
    requestMappingOptions: UInt32
    responseMappingOptions: UInt32
    requestHeaderMappings: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING))
    requestHeaderMappingCount: UInt32
    responseHeaderMappings: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING))
    responseHeaderMappingCount: UInt32
class WS_HTTP_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
WS_HTTP_PROXY_SETTING_MODE = Int32
WS_HTTP_PROXY_SETTING_MODE_AUTO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_PROXY_SETTING_MODE = 1
WS_HTTP_PROXY_SETTING_MODE_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_PROXY_SETTING_MODE = 2
WS_HTTP_PROXY_SETTING_MODE_CUSTOM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_PROXY_SETTING_MODE = 3
@winfunctype_pointer
def WS_HTTP_REDIRECT_CALLBACK(state: VoidPtr, originalUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), newUrl: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_HTTP_REDIRECT_CALLBACK_CONTEXT(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_REDIRECT_CALLBACK
    state: VoidPtr
class WS_HTTP_SSL_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    httpHeaderAuthSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    httpHeaderAuthSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sslTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_HTTP_URL(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
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
    minValue: win32more.Windows.Win32.Foundation.CHAR
    maxValue: win32more.Windows.Win32.Foundation.CHAR
WS_IP_VERSION = Int32
WS_IP_VERSION_4: win32more.Windows.Win32.Networking.WindowsWebServices.WS_IP_VERSION = 1
WS_IP_VERSION_6: win32more.Windows.Win32.Networking.WindowsWebServices.WS_IP_VERSION = 2
WS_IP_VERSION_AUTO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_IP_VERSION = 3
class WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    claimConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    claimConstraintCount: UInt32
    requestSecurityTokenPropertyConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT)
    requestSecurityTokenPropertyConstraintCount: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        issuerAddress: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS)
        requestSecurityTokenTemplate: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
@winfunctype_pointer
def WS_IS_DEFAULT_VALUE_CALLBACK(descriptionData: VoidPtr, value: VoidPtr, defaultValue: VoidPtr, valueSize: UInt32, isDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_ITEM_RANGE(Structure):
    minItemCount: UInt32
    maxItemCount: UInt32
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
WS_LISTENER = IntPtr
class WS_LISTENER_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY)
    propertyCount: UInt32
class WS_LISTENER_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_LISTENER_PROPERTY_ID = Int32
WS_LISTENER_PROPERTY_LISTEN_BACKLOG: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 0
WS_LISTENER_PROPERTY_IP_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 1
WS_LISTENER_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 2
WS_LISTENER_PROPERTY_ASYNC_CALLBACK_MODEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 3
WS_LISTENER_PROPERTY_CHANNEL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 4
WS_LISTENER_PROPERTY_CHANNEL_BINDING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 5
WS_LISTENER_PROPERTY_CONNECT_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 6
WS_LISTENER_PROPERTY_IS_MULTICAST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 7
WS_LISTENER_PROPERTY_MULTICAST_INTERFACES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 8
WS_LISTENER_PROPERTY_MULTICAST_LOOPBACK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 9
WS_LISTENER_PROPERTY_CLOSE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 10
WS_LISTENER_PROPERTY_TO_HEADER_MATCHING_OPTIONS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 11
WS_LISTENER_PROPERTY_TRANSPORT_URL_MATCHING_OPTIONS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 12
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_CALLBACKS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 13
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_PARAMETERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 14
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_INSTANCE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 15
WS_LISTENER_PROPERTY_DISALLOWED_USER_AGENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID = 16
WS_LISTENER_STATE = Int32
WS_LISTENER_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 0
WS_LISTENER_STATE_OPENING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 1
WS_LISTENER_STATE_OPEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 2
WS_LISTENER_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 3
WS_LISTENER_STATE_CLOSING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 4
WS_LISTENER_STATE_CLOSED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_STATE = 5
WS_MESSAGE = IntPtr
class WS_MESSAGE_DESCRIPTION(Structure):
    action: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    bodyElementDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION)
@winfunctype_pointer
def WS_MESSAGE_DONE_CALLBACK(doneCallbackState: VoidPtr) -> Void: ...
WS_MESSAGE_INITIALIZATION = Int32
WS_BLANK_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION = 0
WS_DUPLICATE_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION = 1
WS_REQUEST_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION = 2
WS_REPLY_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION = 3
WS_FAULT_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION = 4
class WS_MESSAGE_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY)
    propertyCount: UInt32
class WS_MESSAGE_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_MESSAGE_PROPERTY_ID = Int32
WS_MESSAGE_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 0
WS_MESSAGE_PROPERTY_HEAP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 1
WS_MESSAGE_PROPERTY_ENVELOPE_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 2
WS_MESSAGE_PROPERTY_ADDRESSING_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 3
WS_MESSAGE_PROPERTY_HEADER_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 4
WS_MESSAGE_PROPERTY_HEADER_POSITION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 5
WS_MESSAGE_PROPERTY_BODY_READER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 6
WS_MESSAGE_PROPERTY_BODY_WRITER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 7
WS_MESSAGE_PROPERTY_IS_ADDRESSED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 8
WS_MESSAGE_PROPERTY_HEAP_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 9
WS_MESSAGE_PROPERTY_XML_READER_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 10
WS_MESSAGE_PROPERTY_XML_WRITER_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 11
WS_MESSAGE_PROPERTY_IS_FAULT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 12
WS_MESSAGE_PROPERTY_MAX_PROCESSED_HEADERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 13
WS_MESSAGE_PROPERTY_USERNAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 14
WS_MESSAGE_PROPERTY_ENCODED_CERT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 15
WS_MESSAGE_PROPERTY_TRANSPORT_SECURITY_WINDOWS_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 16
WS_MESSAGE_PROPERTY_HTTP_HEADER_AUTH_WINDOWS_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 17
WS_MESSAGE_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 18
WS_MESSAGE_PROPERTY_SAML_ASSERTION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 19
WS_MESSAGE_PROPERTY_SECURITY_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 20
WS_MESSAGE_PROPERTY_PROTECTION_LEVEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID = 21
WS_MESSAGE_SECURITY_USAGE = Int32
WS_SUPPORTING_MESSAGE_SECURITY_USAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE = 1
WS_MESSAGE_STATE = Int32
WS_MESSAGE_STATE_EMPTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_STATE = 1
WS_MESSAGE_STATE_INITIALIZED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_STATE = 2
WS_MESSAGE_STATE_READING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_STATE = 3
WS_MESSAGE_STATE_WRITING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_STATE = 4
WS_MESSAGE_STATE_DONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_STATE = 5
WS_METADATA = IntPtr
class WS_METADATA_ENDPOINT(Structure):
    endpointAddress: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS
    endpointPolicy: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY)
    portName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    serviceName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    serviceNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    bindingName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    bindingNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    portTypeName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    portTypeNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
class WS_METADATA_ENDPOINTS(Structure):
    endpoints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_ENDPOINT)
    endpointCount: UInt32
WS_METADATA_EXCHANGE_TYPE = Int32
WS_METADATA_EXCHANGE_TYPE_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_EXCHANGE_TYPE = 0
WS_METADATA_EXCHANGE_TYPE_MEX: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_EXCHANGE_TYPE = 1
WS_METADATA_EXCHANGE_TYPE_HTTP_GET: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_EXCHANGE_TYPE = 2
class WS_METADATA_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_METADATA_PROPERTY_ID = Int32
WS_METADATA_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 1
WS_METADATA_PROPERTY_HEAP_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 2
WS_METADATA_PROPERTY_POLICY_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 3
WS_METADATA_PROPERTY_HEAP_REQUESTED_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 4
WS_METADATA_PROPERTY_MAX_DOCUMENTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 5
WS_METADATA_PROPERTY_HOST_NAMES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 6
WS_METADATA_PROPERTY_VERIFY_HOST_NAMES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID = 7
WS_METADATA_STATE = Int32
WS_METADATA_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_STATE = 1
WS_METADATA_STATE_RESOLVED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_STATE = 2
WS_METADATA_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_METADATA_STATE = 3
WS_MOVE_TO = Int32
WS_MOVE_TO_ROOT_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 0
WS_MOVE_TO_NEXT_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 1
WS_MOVE_TO_PREVIOUS_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 2
WS_MOVE_TO_CHILD_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 3
WS_MOVE_TO_END_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 4
WS_MOVE_TO_PARENT_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 5
WS_MOVE_TO_NEXT_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 6
WS_MOVE_TO_PREVIOUS_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 7
WS_MOVE_TO_FIRST_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 8
WS_MOVE_TO_BOF: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 9
WS_MOVE_TO_EOF: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 10
WS_MOVE_TO_CHILD_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MOVE_TO = 11
class WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
class WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    asymmetricKey: win32more.Windows.Win32.Security.Cryptography.NCRYPT_KEY_HANDLE
class WS_NETPIPE_URL(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_NETTCP_URL(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
    opaqueAuthIdentity: VoidPtr
@winfunctype_pointer
def WS_OPEN_CHANNEL_CALLBACK(channelInstance: VoidPtr, endpointAddress: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_OPEN_LISTENER_CALLBACK(listenerInstance: VoidPtr, url: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_OPERATION_CANCEL_CALLBACK(reason: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CANCEL_REASON, state: VoidPtr) -> Void: ...
WS_OPERATION_CONTEXT = IntPtr
WS_OPERATION_CONTEXT_PROPERTY_ID = Int32
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 0
WS_OPERATION_CONTEXT_PROPERTY_CONTRACT_DESCRIPTION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 1
WS_OPERATION_CONTEXT_PROPERTY_HOST_USER_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 2
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 3
WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 4
WS_OPERATION_CONTEXT_PROPERTY_OUTPUT_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 5
WS_OPERATION_CONTEXT_PROPERTY_HEAP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 6
WS_OPERATION_CONTEXT_PROPERTY_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 7
WS_OPERATION_CONTEXT_PROPERTY_ENDPOINT_ADDRESS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID = 8
class WS_OPERATION_DESCRIPTION(Structure):
    versionInfo: UInt32
    inputMessageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION)
    outputMessageDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION)
    inputMessageOptions: UInt32
    outputMessageOptions: UInt32
    parameterCount: UInt16
    parameterDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_DESCRIPTION)
    stubCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_STUB_CALLBACK
    style: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_STYLE
@winfunctype_pointer
def WS_OPERATION_FREE_STATE_CALLBACK(state: VoidPtr) -> Void: ...
WS_OPERATION_STYLE = Int32
WS_NON_RPC_LITERAL_OPERATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_STYLE = 0
WS_RPC_LITERAL_OPERATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_STYLE = 1
class WS_PARAMETER_DESCRIPTION(Structure):
    parameterType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE
    inputMessageIndex: UInt16
    outputMessageIndex: UInt16
WS_PARAMETER_TYPE = Int32
WS_PARAMETER_TYPE_NORMAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE = 0
WS_PARAMETER_TYPE_ARRAY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE = 1
WS_PARAMETER_TYPE_ARRAY_COUNT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE = 2
WS_PARAMETER_TYPE_MESSAGES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PARAMETER_TYPE = 3
WS_POLICY = IntPtr
class WS_POLICY_CONSTRAINTS(Structure):
    channelBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING
    channelPropertyConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_CONSTRAINT)
    channelPropertyConstraintCount: UInt32
    securityConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS)
    policyExtensions: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION))
    policyExtensionCount: UInt32
class WS_POLICY_EXTENSION(Structure):
    type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION_TYPE
WS_POLICY_EXTENSION_TYPE = Int32
WS_ENDPOINT_POLICY_EXTENSION_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_EXTENSION_TYPE = 1
class WS_POLICY_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY)
    propertyCount: UInt32
class WS_POLICY_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_POLICY_PROPERTY_ID = Int32
WS_POLICY_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID = 1
WS_POLICY_PROPERTY_MAX_ALTERNATIVES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID = 2
WS_POLICY_PROPERTY_MAX_DEPTH: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID = 3
WS_POLICY_PROPERTY_MAX_EXTENSIONS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID = 4
WS_POLICY_STATE = Int32
WS_POLICY_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_STATE = 1
WS_POLICY_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_POLICY_STATE = 2
WS_PROTECTION_LEVEL = Int32
WS_PROTECTION_LEVEL_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROTECTION_LEVEL = 1
WS_PROTECTION_LEVEL_SIGN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROTECTION_LEVEL = 2
WS_PROTECTION_LEVEL_SIGN_AND_ENCRYPT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROTECTION_LEVEL = 3
@winfunctype_pointer
def WS_PROXY_MESSAGE_CALLBACK(message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), state: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_PROXY_MESSAGE_CALLBACK_CONTEXT(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_MESSAGE_CALLBACK
    state: VoidPtr
class WS_PROXY_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_PROXY_PROPERTY_ID = Int32
WS_PROXY_PROPERTY_CALL_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 0
WS_PROXY_PROPERTY_MESSAGE_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 1
WS_PROXY_PROPERTY_MAX_CALL_POOL_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 2
WS_PROXY_PROPERTY_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 3
WS_PROXY_PROPERTY_MAX_PENDING_CALLS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 4
WS_PROXY_PROPERTY_MAX_CLOSE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 5
WS_PROXY_FAULT_LANG_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID = 6
@winfunctype_pointer
def WS_PULL_BYTES_CALLBACK(callbackState: VoidPtr, bytes: VoidPtr, maxSize: UInt32, actualSize: POINTER(UInt32), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_PUSH_BYTES_CALLBACK(callbackState: VoidPtr, writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK, writeCallbackState: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE(Structure):
    keyHandle: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE
    rawKeyBytes: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES
@winfunctype_pointer
def WS_READ_CALLBACK(callbackState: VoidPtr, bytes: VoidPtr, maxSize: UInt32, actualSize: POINTER(UInt32), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_READ_MESSAGE_END_CALLBACK(channelInstance: VoidPtr, message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_READ_MESSAGE_START_CALLBACK(channelInstance: VoidPtr, message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_READ_OPTION = Int32
WS_READ_REQUIRED_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION = 1
WS_READ_REQUIRED_POINTER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION = 2
WS_READ_OPTIONAL_POINTER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION = 3
WS_READ_NILLABLE_POINTER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION = 4
WS_READ_NILLABLE_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_OPTION = 5
@winfunctype_pointer
def WS_READ_TYPE_CALLBACK(reader: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER), typeMapping: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, descriptionData: VoidPtr, heap: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_HEAP), value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_RECEIVE_OPTION = Int32
WS_RECEIVE_REQUIRED_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_RECEIVE_OPTION = 1
WS_RECEIVE_OPTIONAL_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_RECEIVE_OPTION = 2
WS_REPEATING_HEADER_OPTION = Int32
WS_REPEATING_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION = 1
WS_SINGLETON_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION = 2
WS_REQUEST_SECURITY_TOKEN_ACTION = Int32
WS_REQUEST_SECURITY_TOKEN_ACTION_ISSUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_ACTION = 1
WS_REQUEST_SECURITY_TOKEN_ACTION_NEW_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_ACTION = 2
WS_REQUEST_SECURITY_TOKEN_ACTION_RENEW_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_ACTION = 3
class WS_REQUEST_SECURITY_TOKEN_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
class WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID
    allowedValues: VoidPtr
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        requestSecurityTokenProperty: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_REQUEST_SECURITY_TOKEN_PROPERTY_APPLIES_TO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 1
WS_REQUEST_SECURITY_TOKEN_PROPERTY_TRUST_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 2
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SECURE_CONVERSATION_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 3
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 4
WS_REQUEST_SECURITY_TOKEN_PROPERTY_REQUEST_ACTION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 5
WS_REQUEST_SECURITY_TOKEN_PROPERTY_EXISTING_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 6
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 7
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 8
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_ENTROPY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 9
WS_REQUEST_SECURITY_TOKEN_PROPERTY_LOCAL_REQUEST_PARAMETERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 10
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SERVICE_REQUEST_PARAMETERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 11
WS_REQUEST_SECURITY_TOKEN_PROPERTY_MESSAGE_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 12
WS_REQUEST_SECURITY_TOKEN_PROPERTY_BEARER_KEY_TYPE_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = 13
@winfunctype_pointer
def WS_RESET_CHANNEL_CALLBACK(channelInstance: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_RESET_LISTENER_CALLBACK(listenerInstance: VoidPtr, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_RSA_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    modulus: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES
    exponent: win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES
class WS_SAML_AUTHENTICATOR(Structure):
    authenticatorType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_TYPE
WS_SAML_AUTHENTICATOR_TYPE = Int32
WS_CERT_SIGNED_SAML_AUTHENTICATOR_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_TYPE = 1
class WS_SAML_MESSAGE_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    authenticator: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR)
WS_SECURE_CONVERSATION_VERSION = Int32
WS_SECURE_CONVERSATION_VERSION_FEBRUARY_2005: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_CONVERSATION_VERSION = 1
WS_SECURE_CONVERSATION_VERSION_1_3: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_CONVERSATION_VERSION = 2
WS_SECURE_PROTOCOL = Int32
WS_SECURE_PROTOCOL_SSL2: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_PROTOCOL = 1
WS_SECURE_PROTOCOL_SSL3: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_PROTOCOL = 2
WS_SECURE_PROTOCOL_TLS1_0: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_PROTOCOL = 4
WS_SECURE_PROTOCOL_TLS1_1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_PROTOCOL = 8
WS_SECURE_PROTOCOL_TLS1_2: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURE_PROTOCOL = 16
WS_SECURITY_ALGORITHM_ID = Int32
WS_SECURITY_ALGORITHM_DEFAULT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 0
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 1
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE_WITH_COMMENTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 2
WS_SECURITY_ALGORITHM_DIGEST_SHA1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 3
WS_SECURITY_ALGORITHM_DIGEST_SHA_256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 4
WS_SECURITY_ALGORITHM_DIGEST_SHA_384: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 5
WS_SECURITY_ALGORITHM_DIGEST_SHA_512: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 6
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 7
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 8
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_384: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 9
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_512: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 10
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 11
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_DSA_SHA1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 12
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 13
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_384: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 14
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_512: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 15
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_1_5: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 16
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_OAEP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 17
WS_SECURITY_ALGORITHM_KEY_DERIVATION_P_SHA1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID = 18
class WS_SECURITY_ALGORITHM_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_SECURITY_ALGORITHM_PROPERTY_ID = Int32
class WS_SECURITY_ALGORITHM_SUITE(Structure):
    canonicalizationAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    digestAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    symmetricSignatureAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    asymmetricSignatureAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    encryptionAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    keyDerivationAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    symmetricKeyWrapAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    asymmetricKeyWrapAlgorithm: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID
    minSymmetricKeyLength: UInt32
    maxSymmetricKeyLength: UInt32
    minAsymmetricKeyLength: UInt32
    maxAsymmetricKeyLength: UInt32
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY)
    propertyCount: UInt32
WS_SECURITY_ALGORITHM_SUITE_NAME = Int32
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 1
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 2
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 3
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 4
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 5
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 6
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 7
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 8
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 9
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 10
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 11
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256_RSA15: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_NAME = 12
WS_SECURITY_BEARER_KEY_TYPE_VERSION = Int32
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SPECIFICATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BEARER_KEY_TYPE_VERSION = 1
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SCHEMA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BEARER_KEY_TYPE_VERSION = 2
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ERRATA_01: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BEARER_KEY_TYPE_VERSION = 3
class WS_SECURITY_BINDING(Structure):
    bindingType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY)
    propertyCount: UInt32
class WS_SECURITY_BINDING_CONSTRAINT(Structure):
    type: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE
    propertyConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_CONSTRAINT)
    propertyConstraintCount: UInt32
WS_SECURITY_BINDING_CONSTRAINT_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 5
WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 6
WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE = 8
class WS_SECURITY_BINDING_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY)
    propertyCount: UInt32
class WS_SECURITY_BINDING_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
class WS_SECURITY_BINDING_PROPERTY_CONSTRAINT(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID
    allowedValues: VoidPtr
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        securityBindingProperty: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY
WS_SECURITY_BINDING_PROPERTY_ID = Int32
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SSL_CLIENT_CERT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 1
WS_SECURITY_BINDING_PROPERTY_WINDOWS_INTEGRATED_AUTH_PACKAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 2
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 3
WS_SECURITY_BINDING_PROPERTY_ALLOW_ANONYMOUS_CLIENTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 4
WS_SECURITY_BINDING_PROPERTY_ALLOWED_IMPERSONATION_LEVEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 5
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_SCHEME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 6
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_TARGET: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 7
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_BASIC_REALM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 8
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_REALM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 9
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_DOMAIN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 10
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 11
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_ENTROPY_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 12
WS_SECURITY_BINDING_PROPERTY_MESSAGE_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 13
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_PENDING_CONTEXTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 14
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_ACTIVE_CONTEXTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 15
WS_SECURITY_BINDING_PROPERTY_SECURE_CONVERSATION_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 16
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_SUPPORT_RENEW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 17
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_RENEWAL_INTERVAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 18
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_ROLLOVER_INTERVAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 19
WS_SECURITY_BINDING_PROPERTY_CERT_FAILURES_TO_IGNORE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 20
WS_SECURITY_BINDING_PROPERTY_DISABLE_CERT_REVOCATION_CHECK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 21
WS_SECURITY_BINDING_PROPERTY_DISALLOWED_SECURE_PROTOCOLS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 22
WS_SECURITY_BINDING_PROPERTY_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID = 23
WS_SECURITY_BINDING_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 5
WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 6
WS_SAML_MESSAGE_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 8
WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE = 9
class WS_SECURITY_CONSTRAINTS(Structure):
    securityPropertyConstraints: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_CONSTRAINT)
    securityPropertyConstraintCount: UInt32
    securityBindingConstraints: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT))
    securityBindingConstraintCount: UInt32
WS_SECURITY_CONTEXT = IntPtr
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    bootstrapSecurityDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION)
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    bootstrapSecurityConstraint: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS)
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_SECURITY_CONTEXT_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_SECURITY_CONTEXT_PROPERTY_ID = Int32
WS_SECURITY_CONTEXT_PROPERTY_IDENTIFIER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID = 1
WS_SECURITY_CONTEXT_PROPERTY_USERNAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID = 2
WS_SECURITY_CONTEXT_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID = 3
WS_SECURITY_CONTEXT_PROPERTY_SAML_ASSERTION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID = 4
class WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityContextMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
class WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE(Structure):
    securityContextMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
class WS_SECURITY_DESCRIPTION(Structure):
    securityBindings: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING))
    securityBindingCount: UInt32
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY)
    propertyCount: UInt32
WS_SECURITY_HEADER_LAYOUT = Int32
WS_SECURITY_HEADER_LAYOUT_STRICT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_LAYOUT = 1
WS_SECURITY_HEADER_LAYOUT_LAX: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_LAYOUT = 2
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_FIRST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_LAYOUT = 3
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_LAST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_LAYOUT = 4
WS_SECURITY_HEADER_VERSION = Int32
WS_SECURITY_HEADER_VERSION_1_0: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_VERSION = 1
WS_SECURITY_HEADER_VERSION_1_1: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_HEADER_VERSION = 2
WS_SECURITY_KEY_ENTROPY_MODE = Int32
WS_SECURITY_KEY_ENTROPY_MODE_CLIENT_ONLY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_ENTROPY_MODE = 1
WS_SECURITY_KEY_ENTROPY_MODE_SERVER_ONLY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_ENTROPY_MODE = 2
WS_SECURITY_KEY_ENTROPY_MODE_COMBINED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_ENTROPY_MODE = 3
class WS_SECURITY_KEY_HANDLE(Structure):
    keyHandleType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE
WS_SECURITY_KEY_HANDLE_TYPE = Int32
WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE = 1
WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE = 2
WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE = 3
WS_SECURITY_KEY_TYPE = Int32
WS_SECURITY_KEY_TYPE_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_TYPE = 1
WS_SECURITY_KEY_TYPE_SYMMETRIC: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_TYPE = 2
WS_SECURITY_KEY_TYPE_ASYMMETRIC: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_KEY_TYPE = 3
class WS_SECURITY_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY)
    propertyCount: UInt32
class WS_SECURITY_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
class WS_SECURITY_PROPERTY_CONSTRAINT(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID
    allowedValues: VoidPtr
    allowedValuesSize: UInt32
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        securityProperty: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY
WS_SECURITY_PROPERTY_ID = Int32
WS_SECURITY_PROPERTY_TRANSPORT_PROTECTION_LEVEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 1
WS_SECURITY_PROPERTY_ALGORITHM_SUITE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 2
WS_SECURITY_PROPERTY_ALGORITHM_SUITE_NAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 3
WS_SECURITY_PROPERTY_MAX_ALLOWED_LATENCY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 4
WS_SECURITY_PROPERTY_TIMESTAMP_VALIDITY_DURATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 5
WS_SECURITY_PROPERTY_MAX_ALLOWED_CLOCK_SKEW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 6
WS_SECURITY_PROPERTY_TIMESTAMP_USAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 7
WS_SECURITY_PROPERTY_SECURITY_HEADER_LAYOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 8
WS_SECURITY_PROPERTY_SECURITY_HEADER_VERSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 9
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_POLICY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 10
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_SCENARIO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 11
WS_SECURITY_PROPERTY_SERVICE_IDENTITIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID = 12
WS_SECURITY_TIMESTAMP_USAGE = Int32
WS_SECURITY_TIMESTAMP_USAGE_ALWAYS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TIMESTAMP_USAGE = 1
WS_SECURITY_TIMESTAMP_USAGE_NEVER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TIMESTAMP_USAGE = 2
WS_SECURITY_TIMESTAMP_USAGE_REQUESTS_ONLY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TIMESTAMP_USAGE = 3
WS_SECURITY_TOKEN = IntPtr
WS_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_SECURITY_TOKEN_PROPERTY_KEY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 1
WS_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 2
WS_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 3
WS_SECURITY_TOKEN_PROPERTY_SERIALIZED_XML: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 4
WS_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE_XML: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 5
WS_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE_XML: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 6
WS_SECURITY_TOKEN_PROPERTY_SYMMETRIC_KEY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID = 7
WS_SECURITY_TOKEN_REFERENCE_MODE = Int32
WS_SECURITY_TOKEN_REFERENCE_MODE_LOCAL_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_REFERENCE_MODE = 1
WS_SECURITY_TOKEN_REFERENCE_MODE_XML_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_REFERENCE_MODE = 2
WS_SECURITY_TOKEN_REFERENCE_MODE_CERT_THUMBPRINT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_REFERENCE_MODE = 3
WS_SECURITY_TOKEN_REFERENCE_MODE_SECURITY_CONTEXT_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_REFERENCE_MODE = 4
WS_SECURITY_TOKEN_REFERENCE_MODE_SAML_ASSERTION_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN_REFERENCE_MODE = 5
@winfunctype_pointer
def WS_SERVICE_ACCEPT_CHANNEL_CALLBACK(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), channelState: POINTER(VoidPtr), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_SERVICE_CANCEL_REASON = Int32
WS_SERVICE_HOST_ABORT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CANCEL_REASON = 0
WS_SERVICE_CHANNEL_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CANCEL_REASON = 1
@winfunctype_pointer
def WS_SERVICE_CLOSE_CHANNEL_CALLBACK(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_CONTRACT(Structure):
    contractDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CONTRACT_DESCRIPTION)
    defaultMessageHandlerCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_MESSAGE_RECEIVE_CALLBACK
    methodTable: VoidPtr
class WS_SERVICE_ENDPOINT(Structure):
    address: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS
    channelBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_BINDING
    channelType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_TYPE
    securityDescription: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION)
    contract: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CONTRACT)
    authorizationCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY)
    propertyCount: UInt32
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_SERVICE_ENDPOINT_METADATA(Structure):
    portName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    bindingName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    bindingNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
class WS_SERVICE_ENDPOINT_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_SERVICE_ENDPOINT_PROPERTY_ID = Int32
WS_SERVICE_ENDPOINT_PROPERTY_ACCEPT_CHANNEL_CALLBACK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 0
WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 1
WS_SERVICE_ENDPOINT_PROPERTY_MAX_ACCEPTING_CHANNELS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 2
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CONCURRENCY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 3
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_MAX_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 4
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_TRIM_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 5
WS_SERVICE_ENDPOINT_PROPERTY_MESSAGE_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 6
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CALL_POOL_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 7
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNEL_POOL_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 8
WS_SERVICE_ENDPOINT_PROPERTY_LISTENER_PROPERTIES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 9
WS_SERVICE_ENDPOINT_PROPERTY_CHECK_MUST_UNDERSTAND: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 10
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 11
WS_SERVICE_ENDPOINT_PROPERTY_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 12
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 13
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNELS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID = 14
WS_SERVICE_HOST = IntPtr
WS_SERVICE_HOST_STATE = Int32
WS_SERVICE_HOST_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 0
WS_SERVICE_HOST_STATE_OPENING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 1
WS_SERVICE_HOST_STATE_OPEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 2
WS_SERVICE_HOST_STATE_CLOSING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 3
WS_SERVICE_HOST_STATE_CLOSED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 4
WS_SERVICE_HOST_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_HOST_STATE = 5
@winfunctype_pointer
def WS_SERVICE_MESSAGE_RECEIVE_CALLBACK(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_METADATA(Structure):
    documentCount: UInt32
    documents: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_METADATA_DOCUMENT))
    serviceName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    serviceNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
class WS_SERVICE_METADATA_DOCUMENT(Structure):
    content: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    name: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)
class WS_SERVICE_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
class WS_SERVICE_PROPERTY_ACCEPT_CALLBACK(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_ACCEPT_CHANNEL_CALLBACK
class WS_SERVICE_PROPERTY_CLOSE_CALLBACK(Structure):
    callback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_CLOSE_CHANNEL_CALLBACK
WS_SERVICE_PROPERTY_ID = Int32
WS_SERVICE_PROPERTY_HOST_USER_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 0
WS_SERVICE_PROPERTY_FAULT_DISCLOSURE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 1
WS_SERVICE_PROPERTY_FAULT_LANGID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 2
WS_SERVICE_PROPERTY_HOST_STATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 3
WS_SERVICE_PROPERTY_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 4
WS_SERVICE_PROPERTY_CLOSE_TIMEOUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID = 5
WS_SERVICE_PROXY = IntPtr
WS_SERVICE_PROXY_STATE = Int32
WS_SERVICE_PROXY_STATE_CREATED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 0
WS_SERVICE_PROXY_STATE_OPENING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 1
WS_SERVICE_PROXY_STATE_OPEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 2
WS_SERVICE_PROXY_STATE_CLOSING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 3
WS_SERVICE_PROXY_STATE_CLOSED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 4
WS_SERVICE_PROXY_STATE_FAULTED: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SERVICE_PROXY_STATE = 5
@winfunctype_pointer
def WS_SERVICE_SECURITY_CALLBACK(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), authorized: POINTER(win32more.Windows.Win32.Foundation.BOOL), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_SERVICE_SECURITY_IDENTITIES(Structure):
    serviceIdentities: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING)
    serviceIdentityCount: UInt32
@winfunctype_pointer
def WS_SERVICE_STUB_CALLBACK(context: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_OPERATION_CONTEXT), frame: VoidPtr, callback: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SET_CHANNEL_PROPERTY_CALLBACK(channelInstance: VoidPtr, id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SET_LISTENER_PROPERTY_CALLBACK(listenerInstance: VoidPtr, id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK(channelInstance: VoidPtr, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_SOAPUDP_URL(Structure):
    url: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL
    host: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    port: UInt16
    portAsString: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    path: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    query: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    fragment: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_SPN_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    spn: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_SSL_TRANSPORT_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    localCertCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL)
class WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    out: _out_e__Struct
    class _out_e__Struct(Structure):
        clientCertCredentialRequired: win32more.Windows.Win32.Foundation.BOOL
class WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    localCertCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL)
class WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
class WS_STRING(Structure):
    length: UInt32
    chars: win32more.Windows.Win32.Foundation.PWSTR
class WS_STRING_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_STRING_USERNAME_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL
    username: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    password: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
    username: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    password: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    domain: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_STRUCT_DESCRIPTION(Structure):
    size: UInt32
    alignment: UInt32
    fields: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION))
    fieldCount: UInt32
    typeLocalName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    typeNs: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    parentType: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION)
    subTypes: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION))
    subTypeCount: UInt32
    structOptions: UInt32
class WS_SUBJECT_NAME_CERT_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    storeLocation: UInt32
    storeName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    subjectName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_TCP_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_TCP_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
class WS_TCP_SSPI_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    kerberosApreqMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL)
class WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
    channelProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES
    securityProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES
    sspiTransportSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
    usernameMessageSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
    securityContextSecurityBinding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
class WS_THUMBPRINT_CERT_CREDENTIAL(Structure):
    credential: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CERT_CREDENTIAL
    storeLocation: UInt32
    storeName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    thumbprint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_TIMESPAN(Structure):
    ticks: Int64
class WS_TIMESPAN_DESCRIPTION(Structure):
    minValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
    maxValue: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
WS_TRACE_API = Int32
WS_TRACE_API_NONE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = -1
WS_TRACE_API_START_READER_CANONICALIZATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 0
WS_TRACE_API_END_READER_CANONICALIZATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 1
WS_TRACE_API_START_WRITER_CANONICALIZATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 2
WS_TRACE_API_END_WRITER_CANONICALIZATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 3
WS_TRACE_API_CREATE_XML_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 4
WS_TRACE_API_REMOVE_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 5
WS_TRACE_API_CREATE_READER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 6
WS_TRACE_API_SET_INPUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 7
WS_TRACE_API_SET_INPUT_TO_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 8
WS_TRACE_API_FREE_XML_READER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 9
WS_TRACE_API_GET_READER_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 10
WS_TRACE_API_GET_READER_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 11
WS_TRACE_API_FILL_READER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 12
WS_TRACE_API_READ_START_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 13
WS_TRACE_API_READ_TO_START_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 14
WS_TRACE_API_READ_START_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 15
WS_TRACE_API_READ_END_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 16
WS_TRACE_API_READ_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 17
WS_TRACE_API_SKIP_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 18
WS_TRACE_API_READ_END_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 19
WS_TRACE_API_FIND_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 20
WS_TRACE_API_READ_ELEMENT_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 21
WS_TRACE_API_READ_CHARS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 22
WS_TRACE_API_READ_CHARS_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 23
WS_TRACE_API_READ_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 24
WS_TRACE_API_READ_ARRAY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 25
WS_TRACE_API_GET_READER_POSITION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 26
WS_TRACE_API_SET_READER_POSITION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 27
WS_TRACE_API_MOVE_READER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 28
WS_TRACE_API_CREATE_WRITER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 29
WS_TRACE_API_FREE_XML_WRITER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 30
WS_TRACE_API_SET_OUTPUT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 31
WS_TRACE_API_SET_OUTPUT_TO_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 32
WS_TRACE_API_GET_WRITER_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 33
WS_TRACE_API_FLUSH_WRITER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 34
WS_TRACE_API_WRITE_START_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 35
WS_TRACE_API_WRITE_END_START_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 36
WS_TRACE_API_WRITE_XMLNS_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 37
WS_TRACE_API_WRITE_START_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 38
WS_TRACE_API_WRITE_END_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 39
WS_TRACE_API_WRITE_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 40
WS_TRACE_API_WRITE_XML_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 41
WS_TRACE_API_READ_XML_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 42
WS_TRACE_API_WRITE_XML_BUFFER_TO_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 43
WS_TRACE_API_READ_XML_BUFFER_FROM_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 44
WS_TRACE_API_WRITE_ARRAY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 45
WS_TRACE_API_WRITE_QUALIFIED_NAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 46
WS_TRACE_API_WRITE_CHARS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 47
WS_TRACE_API_WRITE_CHARS_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 48
WS_TRACE_API_WRITE_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 49
WS_TRACE_API_PUSH_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 50
WS_TRACE_API_PULL_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 51
WS_TRACE_API_WRITE_END_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 52
WS_TRACE_API_WRITE_TEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 53
WS_TRACE_API_WRITE_START_CDATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 54
WS_TRACE_API_WRITE_END_CDATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 55
WS_TRACE_API_WRITE_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 56
WS_TRACE_API_PREFIX_FROM_NAMESPACE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 57
WS_TRACE_API_GET_WRITER_POSITION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 58
WS_TRACE_API_SET_WRITER_POSITION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 59
WS_TRACE_API_MOVE_WRITER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 60
WS_TRACE_API_TRIM_XML_WHITESPACE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 61
WS_TRACE_API_VERIFY_XML_NCNAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 62
WS_TRACE_API_XML_STRING_EQUALS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 63
WS_TRACE_API_NAMESPACE_FROM_PREFIX: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 64
WS_TRACE_API_READ_QUALIFIED_NAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 65
WS_TRACE_API_GET_XML_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 66
WS_TRACE_API_COPY_NODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 67
WS_TRACE_API_ASYNC_EXECUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 68
WS_TRACE_API_CREATE_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 69
WS_TRACE_API_OPEN_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 70
WS_TRACE_API_SEND_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 71
WS_TRACE_API_RECEIVE_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 72
WS_TRACE_API_REQUEST_REPLY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 73
WS_TRACE_API_SEND_REPLY_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 74
WS_TRACE_API_SEND_FAULT_MESSAGE_FOR_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 75
WS_TRACE_API_GET_CHANNEL_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 76
WS_TRACE_API_SET_CHANNEL_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 77
WS_TRACE_API_WRITE_MESSAGE_START: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 78
WS_TRACE_API_WRITE_MESSAGE_END: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 79
WS_TRACE_API_READ_MESSAGE_START: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 80
WS_TRACE_API_READ_MESSAGE_END: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 81
WS_TRACE_API_CLOSE_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 82
WS_TRACE_API_ABORT_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 83
WS_TRACE_API_FREE_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 84
WS_TRACE_API_RESET_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 85
WS_TRACE_API_ABANDON_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 86
WS_TRACE_API_SHUTDOWN_SESSION_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 87
WS_TRACE_API_GET_CONTEXT_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 88
WS_TRACE_API_GET_DICTIONARY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 89
WS_TRACE_API_READ_ENDPOINT_ADDRESS_EXTENSION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 90
WS_TRACE_API_CREATE_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 91
WS_TRACE_API_ADD_ERROR_STRING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 92
WS_TRACE_API_GET_ERROR_STRING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 93
WS_TRACE_API_COPY_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 94
WS_TRACE_API_GET_ERROR_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 95
WS_TRACE_API_SET_ERROR_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 96
WS_TRACE_API_RESET_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 97
WS_TRACE_API_FREE_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 98
WS_TRACE_API_GET_FAULT_ERROR_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 99
WS_TRACE_API_SET_FAULT_ERROR_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 100
WS_TRACE_API_CREATE_FAULT_FROM_ERROR: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 101
WS_TRACE_API_SET_FAULT_ERROR_DETAIL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 102
WS_TRACE_API_GET_FAULT_ERROR_DETAIL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 103
WS_TRACE_API_CREATE_HEAP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 104
WS_TRACE_API_ALLOC: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 105
WS_TRACE_API_GET_HEAP_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 106
WS_TRACE_API_RESET_HEAP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 107
WS_TRACE_API_FREE_HEAP: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 108
WS_TRACE_API_CREATE_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 109
WS_TRACE_API_OPEN_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 110
WS_TRACE_API_ACCEPT_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 111
WS_TRACE_API_CLOSE_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 112
WS_TRACE_API_ABORT_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 113
WS_TRACE_API_RESET_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 114
WS_TRACE_API_FREE_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 115
WS_TRACE_API_GET_LISTENER_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 116
WS_TRACE_API_SET_LISTENER_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 117
WS_TRACE_API_CREATE_CHANNEL_FOR_LISTENER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 118
WS_TRACE_API_CREATE_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 119
WS_TRACE_API_CREATE_MESSAGE_FOR_CHANNEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 120
WS_TRACE_API_INITIALIZE_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 121
WS_TRACE_API_RESET_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 122
WS_TRACE_API_FREE_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 123
WS_TRACE_API_GET_HEADER_ATTRIBUTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 124
WS_TRACE_API_GET_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 125
WS_TRACE_API_GET_CUSTOM_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 126
WS_TRACE_API_REMOVE_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 127
WS_TRACE_API_SET_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 128
WS_TRACE_API_REMOVE_CUSTOM_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 129
WS_TRACE_API_ADD_CUSTOM_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 130
WS_TRACE_API_ADD_MAPPED_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 131
WS_TRACE_API_REMOVE_MAPPED_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 132
WS_TRACE_API_GET_MAPPED_HEADER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 133
WS_TRACE_API_WRITE_BODY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 134
WS_TRACE_API_READ_BODY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 135
WS_TRACE_API_WRITE_ENVELOPE_START: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 136
WS_TRACE_API_WRITE_ENVELOPE_END: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 137
WS_TRACE_API_READ_ENVELOPE_START: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 138
WS_TRACE_API_READ_ENVELOPE_END: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 139
WS_TRACE_API_GET_MESSAGE_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 140
WS_TRACE_API_SET_MESSAGE_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 141
WS_TRACE_API_ADDRESS_MESSAGE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 142
WS_TRACE_API_CHECK_MUST_UNDERSTAND_HEADERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 143
WS_TRACE_API_MARK_HEADER_AS_UNDERSTOOD: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 144
WS_TRACE_API_FILL_BODY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 145
WS_TRACE_API_FLUSH_BODY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 146
WS_TRACE_API_REQUEST_SECURITY_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 147
WS_TRACE_API_GET_SECURITY_TOKEN_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 148
WS_TRACE_API_CREATE_XML_SECURITY_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 149
WS_TRACE_API_FREE_SECURITY_TOKEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 150
WS_TRACE_API_REVOKE_SECURITY_CONTEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 151
WS_TRACE_API_GET_SECURITY_CONTEXT_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 152
WS_TRACE_API_READ_ELEMENT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 153
WS_TRACE_API_READ_ATTRIBUTE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 154
WS_TRACE_API_READ_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 155
WS_TRACE_API_WRITE_ELEMENT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 156
WS_TRACE_API_WRITE_ATTRIBUTE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 157
WS_TRACE_API_WRITE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 158
WS_TRACE_API_SERVICE_REGISTER_FOR_CANCEL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 159
WS_TRACE_API_GET_SERVICE_HOST_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 160
WS_TRACE_API_CREATE_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 161
WS_TRACE_API_OPEN_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 162
WS_TRACE_API_CLOSE_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 163
WS_TRACE_API_ABORT_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 164
WS_TRACE_API_FREE_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 165
WS_TRACE_API_RESET_SERVICE_HOST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 166
WS_TRACE_API_GET_SERVICE_PROXY_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 167
WS_TRACE_API_CREATE_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 168
WS_TRACE_API_OPEN_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 169
WS_TRACE_API_CLOSE_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 170
WS_TRACE_API_ABORT_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 171
WS_TRACE_API_FREE_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 172
WS_TRACE_API_RESET_SERVICE_PROXY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 173
WS_TRACE_API_ABORT_CALL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 174
WS_TRACE_API_CALL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 175
WS_TRACE_API_DECODE_URL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 176
WS_TRACE_API_ENCODE_URL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 177
WS_TRACE_API_COMBINE_URL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 178
WS_TRACE_API_DATETIME_TO_FILETIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 179
WS_TRACE_API_FILETIME_TO_DATETIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 180
WS_TRACE_API_DUMP_MEMORY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 181
WS_TRACE_API_SET_AUTOFAIL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 182
WS_TRACE_API_CREATE_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 183
WS_TRACE_API_READ_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 184
WS_TRACE_API_FREE_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 185
WS_TRACE_API_RESET_METADATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 186
WS_TRACE_API_GET_METADATA_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 187
WS_TRACE_API_GET_MISSING_METADATA_DOCUMENT_ADDRESS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 188
WS_TRACE_API_GET_METADATA_ENDPOINTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 189
WS_TRACE_API_MATCH_POLICY_ALTERNATIVE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 190
WS_TRACE_API_GET_POLICY_PROPERTY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 191
WS_TRACE_API_GET_POLICY_ALTERNATIVE_COUNT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 192
WS_TRACE_API_WS_CREATE_SERVICE_PROXY_FROM_TEMPLATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 193
WS_TRACE_API_WS_CREATE_SERVICE_HOST_FROM_TEMPLATE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRACE_API = 194
WS_TRANSFER_MODE = Int32
WS_STREAMED_INPUT_TRANSFER_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRANSFER_MODE = 1
WS_STREAMED_OUTPUT_TRANSFER_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRANSFER_MODE = 2
WS_BUFFERED_TRANSFER_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRANSFER_MODE = 0
WS_STREAMED_TRANSFER_MODE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRANSFER_MODE = 3
WS_TRUST_VERSION = Int32
WS_TRUST_VERSION_FEBRUARY_2005: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRUST_VERSION = 1
WS_TRUST_VERSION_1_3: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TRUST_VERSION = 2
WS_TYPE = Int32
WS_BOOL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 0
WS_INT8_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 1
WS_INT16_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 2
WS_INT32_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 3
WS_INT64_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 4
WS_UINT8_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 5
WS_UINT16_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 6
WS_UINT32_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 7
WS_UINT64_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 8
WS_FLOAT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 9
WS_DOUBLE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 10
WS_DECIMAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 11
WS_DATETIME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 12
WS_TIMESPAN_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 13
WS_GUID_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 14
WS_UNIQUE_ID_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 15
WS_STRING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 16
WS_WSZ_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 17
WS_BYTES_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 18
WS_XML_STRING_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 19
WS_XML_QNAME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 20
WS_XML_BUFFER_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 21
WS_CHAR_ARRAY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 22
WS_UTF8_ARRAY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 23
WS_BYTE_ARRAY_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 24
WS_DESCRIPTION_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 25
WS_STRUCT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 26
WS_CUSTOM_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 27
WS_ENDPOINT_ADDRESS_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 28
WS_FAULT_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 29
WS_VOID_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 30
WS_ENUM_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 31
WS_DURATION_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 32
WS_UNION_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 33
WS_ANY_ATTRIBUTES_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE = 34
WS_TYPE_MAPPING = Int32
WS_ELEMENT_TYPE_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING = 1
WS_ATTRIBUTE_TYPE_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING = 2
WS_ELEMENT_CONTENT_TYPE_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING = 3
WS_ANY_ELEMENT_TYPE_MAPPING: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING = 4
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
    fields: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_UNION_FIELD_DESCRIPTION))
    fieldCount: UInt32
    enumOffset: UInt32
    noneEnumValue: Int32
    valueIndices: POINTER(UInt32)
class WS_UNION_FIELD_DESCRIPTION(Structure):
    value: Int32
    field: win32more.Windows.Win32.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION
class WS_UNIQUE_ID(Structure):
    uri: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    guid: Guid
class WS_UNIQUE_ID_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_UNKNOWN_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    element: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
class WS_UPN_ENDPOINT_IDENTITY(Structure):
    identity: win32more.Windows.Win32.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY
    upn: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_URL(Structure):
    scheme: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE
WS_URL_SCHEME_TYPE = Int32
WS_URL_HTTP_SCHEME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE = 0
WS_URL_HTTPS_SCHEME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE = 1
WS_URL_NETTCP_SCHEME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE = 2
WS_URL_SOAPUDP_SCHEME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE = 3
WS_URL_NETPIPE_SCHEME_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE = 4
class WS_USERNAME_CREDENTIAL(Structure):
    credentialType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_TYPE
WS_USERNAME_CREDENTIAL_TYPE = Int32
WS_STRING_USERNAME_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_TYPE = 1
class WS_USERNAME_MESSAGE_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL)
    passwordValidator: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK
    passwordValidatorCallbackState: VoidPtr
class WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
    bindingConstraint: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
class WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
    securityBindingProperties: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES
    clientCredential: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL)
    passwordValidator: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK
    passwordValidatorCallbackState: VoidPtr
class WS_UTF8_ARRAY_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
@winfunctype_pointer
def WS_VALIDATE_PASSWORD_CALLBACK(passwordValidatorCallbackState: VoidPtr, username: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), password: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_VALIDATE_SAML_CALLBACK(samlValidatorCallbackState: VoidPtr, samlAssertion: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_VALUE_TYPE = Int32
WS_BOOL_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 0
WS_INT8_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 1
WS_INT16_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 2
WS_INT32_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 3
WS_INT64_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 4
WS_UINT8_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 5
WS_UINT16_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 6
WS_UINT32_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 7
WS_UINT64_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 8
WS_FLOAT_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 9
WS_DOUBLE_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 10
WS_DECIMAL_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 11
WS_DATETIME_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 12
WS_TIMESPAN_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 13
WS_GUID_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 14
WS_DURATION_VALUE_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_VALUE_TYPE = 15
class WS_VOID_DESCRIPTION(Structure):
    size: UInt32
class WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
    credentialType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE
WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = Int32
WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 1
WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 2
WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 3
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = Int32
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_KERBEROS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 1
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_NTLM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 2
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_SPNEGO: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = 3
@winfunctype_pointer
def WS_WRITE_CALLBACK(callbackState: VoidPtr, buffers: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_BYTES), count: UInt32, asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_WRITE_MESSAGE_END_CALLBACK(channelInstance: VoidPtr, message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WS_WRITE_MESSAGE_START_CALLBACK(channelInstance: VoidPtr, message: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE), asyncContext: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ASYNC_CONTEXT), error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WS_WRITE_OPTION = Int32
WS_WRITE_REQUIRED_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION = 1
WS_WRITE_REQUIRED_POINTER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION = 2
WS_WRITE_NILLABLE_VALUE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION = 3
WS_WRITE_NILLABLE_POINTER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_OPTION = 4
@winfunctype_pointer
def WS_WRITE_TYPE_CALLBACK(writer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER), typeMapping: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TYPE_MAPPING, descriptionData: VoidPtr, value: VoidPtr, valueSize: UInt32, error: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_ERROR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WS_WSZ_DESCRIPTION(Structure):
    minCharCount: UInt32
    maxCharCount: UInt32
class WS_XML_ATTRIBUTE(Structure):
    singleQuote: Byte
    isXmlNs: Byte
    prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    value: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT)
class WS_XML_BASE64_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    bytes: POINTER(Byte)
    length: UInt32
class WS_XML_BOOL_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: win32more.Windows.Win32.Foundation.BOOL
WS_XML_BUFFER = IntPtr
class WS_XML_BUFFER_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_XML_BUFFER_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_ALGORITHM = Int32
WS_EXCLUSIVE_XML_CANONICALIZATION_ALGORITHM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_ALGORITHM = 0
WS_EXCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_ALGORITHM = 1
WS_INCLUSIVE_XML_CANONICALIZATION_ALGORITHM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_ALGORITHM = 2
WS_INCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_ALGORITHM = 3
class WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES(Structure):
    prefixCount: UInt32
    prefixes: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
class WS_XML_CANONICALIZATION_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_XML_CANONICALIZATION_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_PROPERTY_ALGORITHM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID = 0
WS_XML_CANONICALIZATION_PROPERTY_INCLUSIVE_PREFIXES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID = 1
WS_XML_CANONICALIZATION_PROPERTY_OMITTED_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID = 2
WS_XML_CANONICALIZATION_PROPERTY_OUTPUT_BUFFER_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID = 3
class WS_XML_COMMENT_NODE(Structure):
    node: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    value: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
class WS_XML_DATETIME_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DATETIME
class WS_XML_DECIMAL_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: win32more.Windows.Win32.Foundation.DECIMAL
class WS_XML_DICTIONARY(Structure):
    guid: Guid
    strings: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    stringCount: UInt32
    isConst: win32more.Windows.Win32.Foundation.BOOL
class WS_XML_DOUBLE_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Double
class WS_XML_ELEMENT_NODE(Structure):
    node: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    attributeCount: UInt32
    attributes: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_ATTRIBUTE))
    isEmpty: win32more.Windows.Win32.Foundation.BOOL
class WS_XML_FLOAT_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Single
class WS_XML_GUID_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Guid
class WS_XML_INT32_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Int32
class WS_XML_INT64_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Int64
class WS_XML_LIST_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    itemCount: UInt32
    items: POINTER(POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT))
class WS_XML_NODE(Structure):
    nodeType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE
class WS_XML_NODE_POSITION(Structure):
    buffer: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_BUFFER)
    node: VoidPtr
WS_XML_NODE_TYPE = Int32
WS_XML_NODE_TYPE_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 1
WS_XML_NODE_TYPE_TEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 2
WS_XML_NODE_TYPE_END_ELEMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 3
WS_XML_NODE_TYPE_COMMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 4
WS_XML_NODE_TYPE_CDATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 6
WS_XML_NODE_TYPE_END_CDATA: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 7
WS_XML_NODE_TYPE_EOF: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 8
WS_XML_NODE_TYPE_BOF: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE_TYPE = 9
class WS_XML_QNAME(Structure):
    localName: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
    ns: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
class WS_XML_QNAME_DESCRIPTION(Structure):
    minLocalNameByteCount: UInt32
    maxLocalNameByteCount: UInt32
    minNsByteCount: UInt32
    maxNsByteCount: UInt32
class WS_XML_QNAME_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    prefix: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    localName: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
    ns: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING)
WS_XML_READER = IntPtr
class WS_XML_READER_BINARY_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    staticDictionary: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY)
    dynamicDictionary: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY)
class WS_XML_READER_BUFFER_INPUT(Structure):
    input: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT
    encodedData: VoidPtr
    encodedDataSize: UInt32
class WS_XML_READER_ENCODING(Structure):
    encodingType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE
WS_XML_READER_ENCODING_TYPE = Int32
WS_XML_READER_ENCODING_TYPE_TEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE = 1
WS_XML_READER_ENCODING_TYPE_BINARY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE = 2
WS_XML_READER_ENCODING_TYPE_MTOM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE = 3
WS_XML_READER_ENCODING_TYPE_RAW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE = 4
class WS_XML_READER_INPUT(Structure):
    inputType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT_TYPE
WS_XML_READER_INPUT_TYPE = Int32
WS_XML_READER_INPUT_TYPE_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT_TYPE = 1
WS_XML_READER_INPUT_TYPE_STREAM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT_TYPE = 2
class WS_XML_READER_MTOM_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    textEncoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING)
    readMimeHeader: win32more.Windows.Win32.Foundation.BOOL
    startInfo: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    boundary: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startUri: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
class WS_XML_READER_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY)
    propertyCount: UInt32
class WS_XML_READER_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_XML_READER_PROPERTY_ID = Int32
WS_XML_READER_PROPERTY_MAX_DEPTH: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 0
WS_XML_READER_PROPERTY_ALLOW_FRAGMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 1
WS_XML_READER_PROPERTY_MAX_ATTRIBUTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 2
WS_XML_READER_PROPERTY_READ_DECLARATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 3
WS_XML_READER_PROPERTY_CHARSET: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 4
WS_XML_READER_PROPERTY_ROW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 5
WS_XML_READER_PROPERTY_COLUMN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 6
WS_XML_READER_PROPERTY_UTF8_TRIM_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 7
WS_XML_READER_PROPERTY_STREAM_BUFFER_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 8
WS_XML_READER_PROPERTY_IN_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 9
WS_XML_READER_PROPERTY_STREAM_MAX_ROOT_MIME_PART_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 10
WS_XML_READER_PROPERTY_STREAM_MAX_MIME_HEADERS_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 11
WS_XML_READER_PROPERTY_MAX_MIME_PARTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 12
WS_XML_READER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 13
WS_XML_READER_PROPERTY_MAX_NAMESPACES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID = 14
class WS_XML_READER_RAW_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
class WS_XML_READER_STREAM_INPUT(Structure):
    input: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_INPUT
    readCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_READ_CALLBACK
    readCallbackState: VoidPtr
class WS_XML_READER_TEXT_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_READER_ENCODING
    charSet: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET
class WS_XML_SECURITY_TOKEN_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_XML_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_XML_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID = 1
WS_XML_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID = 2
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID = 3
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID = 4
class WS_XML_STRING(Structure):
    length: UInt32
    bytes: POINTER(Byte)
    dictionary: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY)
    id: UInt32
class WS_XML_STRING_DESCRIPTION(Structure):
    minByteCount: UInt32
    maxByteCount: UInt32
class WS_XML_TEXT(Structure):
    textType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE
class WS_XML_TEXT_NODE(Structure):
    node: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_NODE
    text: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT)
WS_XML_TEXT_TYPE = Int32
WS_XML_TEXT_TYPE_UTF8: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 1
WS_XML_TEXT_TYPE_UTF16: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 2
WS_XML_TEXT_TYPE_BASE64: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 3
WS_XML_TEXT_TYPE_BOOL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 4
WS_XML_TEXT_TYPE_INT32: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 5
WS_XML_TEXT_TYPE_INT64: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 6
WS_XML_TEXT_TYPE_UINT64: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 7
WS_XML_TEXT_TYPE_FLOAT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 8
WS_XML_TEXT_TYPE_DOUBLE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 9
WS_XML_TEXT_TYPE_DECIMAL: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 10
WS_XML_TEXT_TYPE_GUID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 11
WS_XML_TEXT_TYPE_UNIQUE_ID: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 12
WS_XML_TEXT_TYPE_DATETIME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 13
WS_XML_TEXT_TYPE_TIMESPAN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 14
WS_XML_TEXT_TYPE_QNAME: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 15
WS_XML_TEXT_TYPE_LIST: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT_TYPE = 16
class WS_XML_TIMESPAN_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: win32more.Windows.Win32.Networking.WindowsWebServices.WS_TIMESPAN
class WS_XML_TOKEN_MESSAGE_SECURITY_BINDING(Structure):
    binding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_BINDING
    bindingUsage: win32more.Windows.Win32.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE
    xmlToken: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_SECURITY_TOKEN)
class WS_XML_UINT64_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: UInt64
class WS_XML_UNIQUE_ID_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: Guid
class WS_XML_UTF16_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    bytes: POINTER(Byte)
    byteCount: UInt32
class WS_XML_UTF8_TEXT(Structure):
    text: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_TEXT
    value: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_STRING
WS_XML_WRITER = IntPtr
class WS_XML_WRITER_BINARY_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    staticDictionary: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_DICTIONARY)
    dynamicStringCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_DYNAMIC_STRING_CALLBACK
    dynamicStringCallbackState: VoidPtr
class WS_XML_WRITER_BUFFER_OUTPUT(Structure):
    output: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT
class WS_XML_WRITER_ENCODING(Structure):
    encodingType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE
WS_XML_WRITER_ENCODING_TYPE = Int32
WS_XML_WRITER_ENCODING_TYPE_TEXT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE = 1
WS_XML_WRITER_ENCODING_TYPE_BINARY: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE = 2
WS_XML_WRITER_ENCODING_TYPE_MTOM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE = 3
WS_XML_WRITER_ENCODING_TYPE_RAW: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE = 4
class WS_XML_WRITER_MTOM_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    textEncoding: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING)
    writeMimeHeader: win32more.Windows.Win32.Foundation.BOOL
    boundary: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startInfo: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    startUri: win32more.Windows.Win32.Networking.WindowsWebServices.WS_STRING
    maxInlineByteCount: UInt32
class WS_XML_WRITER_OUTPUT(Structure):
    outputType: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_TYPE
WS_XML_WRITER_OUTPUT_TYPE = Int32
WS_XML_WRITER_OUTPUT_TYPE_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_TYPE = 1
WS_XML_WRITER_OUTPUT_TYPE_STREAM: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_TYPE = 2
class WS_XML_WRITER_PROPERTIES(Structure):
    properties: POINTER(win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY)
    propertyCount: UInt32
class WS_XML_WRITER_PROPERTY(Structure):
    id: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID
    value: VoidPtr
    valueSize: UInt32
WS_XML_WRITER_PROPERTY_ID = Int32
WS_XML_WRITER_PROPERTY_MAX_DEPTH: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 0
WS_XML_WRITER_PROPERTY_ALLOW_FRAGMENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 1
WS_XML_WRITER_PROPERTY_MAX_ATTRIBUTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 2
WS_XML_WRITER_PROPERTY_WRITE_DECLARATION: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 3
WS_XML_WRITER_PROPERTY_INDENT: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 4
WS_XML_WRITER_PROPERTY_BUFFER_TRIM_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 5
WS_XML_WRITER_PROPERTY_CHARSET: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 6
WS_XML_WRITER_PROPERTY_BUFFERS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 7
WS_XML_WRITER_PROPERTY_BUFFER_MAX_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 8
WS_XML_WRITER_PROPERTY_BYTES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 9
WS_XML_WRITER_PROPERTY_IN_ATTRIBUTE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 10
WS_XML_WRITER_PROPERTY_MAX_MIME_PARTS_BUFFER_SIZE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 11
WS_XML_WRITER_PROPERTY_INITIAL_BUFFER: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 12
WS_XML_WRITER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 13
WS_XML_WRITER_PROPERTY_MAX_NAMESPACES: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 14
WS_XML_WRITER_PROPERTY_BYTES_WRITTEN: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 15
WS_XML_WRITER_PROPERTY_BYTES_TO_CLOSE: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 16
WS_XML_WRITER_PROPERTY_COMPRESS_EMPTY_ELEMENTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 17
WS_XML_WRITER_PROPERTY_EMIT_UNCOMPRESSED_EMPTY_ELEMENTS: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID = 18
class WS_XML_WRITER_RAW_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
class WS_XML_WRITER_STREAM_OUTPUT(Structure):
    output: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT
    writeCallback: win32more.Windows.Win32.Networking.WindowsWebServices.WS_WRITE_CALLBACK
    writeCallbackState: VoidPtr
class WS_XML_WRITER_TEXT_ENCODING(Structure):
    encoding: win32more.Windows.Win32.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING
    charSet: win32more.Windows.Win32.Networking.WindowsWebServices.WS_CHARSET


make_ready(__name__)
