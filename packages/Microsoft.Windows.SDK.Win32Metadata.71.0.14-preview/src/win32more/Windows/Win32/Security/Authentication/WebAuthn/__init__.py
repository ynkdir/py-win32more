from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Authentication.WebAuthn
import win32more.Windows.Win32.System.Com
AUTHENTICATOR_STATE = Int32
AuthenticatorState_Disabled: win32more.Windows.Win32.Security.Authentication.WebAuthn.AUTHENTICATOR_STATE = 0
AuthenticatorState_Enabled: win32more.Windows.Win32.Security.Authentication.WebAuthn.AUTHENTICATOR_STATE = 1
WEBAUTHN_API_VERSION_1: UInt32 = 1
WEBAUTHN_API_VERSION_2: UInt32 = 2
WEBAUTHN_API_VERSION_3: UInt32 = 3
WEBAUTHN_API_VERSION_4: UInt32 = 4
WEBAUTHN_API_VERSION_5: UInt32 = 5
WEBAUTHN_API_VERSION_6: UInt32 = 6
WEBAUTHN_API_VERSION_7: UInt32 = 7
WEBAUTHN_API_VERSION_8: UInt32 = 8
WEBAUTHN_API_VERSION_9: UInt32 = 9
WEBAUTHN_API_CURRENT_VERSION: UInt32 = 9
WEBAUTHN_RP_ENTITY_INFORMATION_VERSION_1: UInt32 = 1
WEBAUTHN_RP_ENTITY_INFORMATION_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_MAX_USER_ID_LENGTH: UInt32 = 64
WEBAUTHN_USER_ENTITY_INFORMATION_VERSION_1: UInt32 = 1
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
WEBAUTHN_CTAP_TRANSPORT_SMART_CARD: UInt32 = 64
WEBAUTHN_CTAP_TRANSPORT_FLAGS_MASK: UInt32 = 127
WEBAUTHN_CTAP_TRANSPORT_USB_STRING: String = 'usb'
WEBAUTHN_CTAP_TRANSPORT_NFC_STRING: String = 'nfc'
WEBAUTHN_CTAP_TRANSPORT_BLE_STRING: String = 'ble'
WEBAUTHN_CTAP_TRANSPORT_SMART_CARD_STRING: String = 'smart-card'
WEBAUTHN_CTAP_TRANSPORT_HYBRID_STRING: String = 'hybrid'
WEBAUTHN_CTAP_TRANSPORT_INTERNAL_STRING: String = 'internal'
WEBAUTHN_CREDENTIAL_EX_CURRENT_VERSION: UInt32 = 1
CTAPCBOR_HYBRID_STORAGE_LINKED_DATA_VERSION_1: UInt32 = 1
CTAPCBOR_HYBRID_STORAGE_LINKED_DATA_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_DETAILS_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_DETAILS_OPTIONS_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_DETAILS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_DETAILS_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_1: UInt32 = 1
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_2: UInt32 = 2
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_3: UInt32 = 3
WEBAUTHN_CREDENTIAL_DETAILS_VERSION_4: UInt32 = 4
WEBAUTHN_CREDENTIAL_DETAILS_CURRENT_VERSION: UInt32 = 4
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
WEBAUTHN_CREDENTIAL_HINT_SECURITY_KEY: String = 'security-key'
WEBAUTHN_CREDENTIAL_HINT_CLIENT_DEVICE: String = 'client-device'
WEBAUTHN_CREDENTIAL_HINT_HYBRID: String = 'hybrid'
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_2: UInt32 = 2
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_3: UInt32 = 3
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_4: UInt32 = 4
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_5: UInt32 = 5
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_6: UInt32 = 6
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_7: UInt32 = 7
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_8: UInt32 = 8
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_9: UInt32 = 9
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_CURRENT_VERSION: UInt32 = 9
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
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_8: UInt32 = 8
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_9: UInt32 = 9
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_CURRENT_VERSION: UInt32 = 9
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
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_7: UInt32 = 7
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_8: UInt32 = 8
WEBAUTHN_CREDENTIAL_ATTESTATION_CURRENT_VERSION: UInt32 = 8
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
WEBAUTHN_ASSERTION_VERSION_6: UInt32 = 6
WEBAUTHN_ASSERTION_CURRENT_VERSION: UInt32 = 6
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS_VERSION_1: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS_CURRENT_VERSION: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY_VERSION_1: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY_CURRENT_VERSION: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION_VERSION_1: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION_CURRENT_VERSION: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST_VERSION_1: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST_CURRENT_VERSION: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST_VERSION_1: UInt32 = 1
EXPERIMENTAL_WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS_VERSION_1: UInt32 = 1
WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY_VERSION_1: UInt32 = 1
WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION_VERSION_1: UInt32 = 1
WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST_VERSION_1: UInt32 = 1
WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST_CURRENT_VERSION: UInt32 = 1
WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST_VERSION_1: UInt32 = 1
WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST_CURRENT_VERSION: UInt32 = 1
@winfunctype('webauthn.dll')
def WebAuthNGetApiVersionNumber() -> UInt32: ...
@winfunctype('webauthn.dll')
def WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable(pbIsUserVerifyingPlatformAuthenticatorAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorMakeCredential(hWnd: win32more.Windows.Win32.Foundation.HWND, pRpInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_RP_ENTITY_INFORMATION), pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION), pPubKeyCredParams: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS), pWebAuthNClientData: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CLIENT_DATA), pWebAuthNMakeCredentialOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS), ppWebAuthNCredentialAttestation: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_ATTESTATION))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNAuthenticatorGetAssertion(hWnd: win32more.Windows.Win32.Foundation.HWND, pwszRpId: win32more.Windows.Win32.Foundation.PWSTR, pWebAuthNClientData: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CLIENT_DATA), pWebAuthNGetAssertionOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS), ppWebAuthNAssertion: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_ASSERTION))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeCredentialAttestation(pWebAuthNCredentialAttestation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_ATTESTATION)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeAssertion(pWebAuthNAssertion: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_ASSERTION)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNGetCancellationId(pCancellationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNCancelCurrentOperation(pCancellationId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetPlatformCredentialList(pGetCredentialsOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_GET_CREDENTIALS_OPTIONS), ppCredentialDetailsList: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_DETAILS_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreePlatformCredentialList(pCredentialDetailsList: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_DETAILS_LIST)) -> Void: ...
@winfunctype('webauthn.dll')
def WebAuthNDeletePlatformCredential(cbCredentialId: UInt32, pbCredentialId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNGetAuthenticatorList(pWebAuthNGetAuthenticatorListOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_DETAILS_OPTIONS), ppAuthenticatorDetailsList: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_DETAILS_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('webauthn.dll')
def WebAuthNFreeAuthenticatorList(pAuthenticatorDetailsList: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_DETAILS_LIST)) -> Void: ...
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
class EXPERIMENTAL_IPluginAuthenticator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6466e9a-b2f3-47c5-b88d-89bc14a8d998}')
    @commethod(3)
    def EXPERIMENTAL_PluginMakeCredential(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_REQUEST), response: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_RESPONSE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EXPERIMENTAL_PluginGetAssertion(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_REQUEST), response: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_RESPONSE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EXPERIMENTAL_PluginCancelOperation(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_CANCEL_OPERATION_REQUEST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
EXPERIMENTAL_PLUGIN_AUTHENTICATOR_STATE = Int32
PluginAuthenticatorState_Unknown: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_PLUGIN_AUTHENTICATOR_STATE = 0
PluginAuthenticatorState_Disabled: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_PLUGIN_AUTHENTICATOR_STATE = 1
PluginAuthenticatorState_Enabled: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_PLUGIN_AUTHENTICATOR_STATE = 2
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS(Structure):
    dwVersion: UInt32
    lUp: Int32
    lUv: Int32
    lRequireResidentKey: Int32
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY(Structure):
    dwVersion: UInt32
    lKty: Int32
    lAlg: Int32
    lCrv: Int32
    cbX: UInt32
    pbX: POINTER(Byte)
    cbY: UInt32
    pbY: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST(Structure):
    dwVersion: UInt32
    pwszRpId: win32more.Windows.Win32.Foundation.PWSTR
    cbRpId: UInt32
    pbRpId: POINTER(Byte)
    cbClientDataHash: UInt32
    pbClientDataHash: POINTER(Byte)
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST
    cbCborExtensionsMap: UInt32
    pbCborExtensionsMap: POINTER(Byte)
    pAuthenticatorOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS)
    fEmptyPinAuth: win32more.Windows.Win32.Foundation.BOOL
    cbPinAuth: UInt32
    pbPinAuth: POINTER(Byte)
    pHmacSaltExtension: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION)
    cbHmacSecretSaltValues: UInt32
    pbHmacSecretSaltValues: POINTER(Byte)
    dwPinProtocol: UInt32
    lCredBlobExt: Int32
    lLargeBlobKeyExt: Int32
    dwCredLargeBlobOperation: UInt32
    cbCredLargeBlobCompressed: UInt32
    pbCredLargeBlobCompressed: POINTER(Byte)
    dwCredLargeBlobOriginalSize: UInt32
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_GET_ASSERTION_RESPONSE(Structure):
    WebAuthNAssertion: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_ASSERTION
    pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION)
    dwNumberOfCredentials: UInt32
    lUserSelected: Int32
    cbLargeBlobKey: UInt32
    pbLargeBlobKey: POINTER(Byte)
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION(Structure):
    dwVersion: UInt32
    pKeyAgreement: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY)
    cbEncryptedSalt: UInt32
    pbEncryptedSalt: POINTER(Byte)
    cbSaltAuth: UInt32
    pbSaltAuth: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST(Structure):
    dwVersion: UInt32
    cbRpId: UInt32
    pbRpId: POINTER(Byte)
    cbClientDataHash: UInt32
    pbClientDataHash: POINTER(Byte)
    pRpInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_RP_ENTITY_INFORMATION)
    pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION)
    WebAuthNCredentialParameters: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST
    cbCborExtensionsMap: UInt32
    pbCborExtensionsMap: POINTER(Byte)
    pAuthenticatorOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS)
    fEmptyPinAuth: win32more.Windows.Win32.Foundation.BOOL
    cbPinAuth: UInt32
    pbPinAuth: POINTER(Byte)
    lHmacSecretExt: Int32
    pHmacSecretMcExtension: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION)
    lPrfExt: Int32
    cbHmacSecretSaltValues: UInt32
    pbHmacSecretSaltValues: POINTER(Byte)
    dwCredProtect: UInt32
    dwPinProtocol: UInt32
    dwEnterpriseAttestation: UInt32
    cbCredBlobExt: UInt32
    pbCredBlobExt: POINTER(Byte)
    lLargeBlobKeyExt: Int32
    dwLargeBlobSupport: UInt32
    lMinPinLengthExt: Int32
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_ADD_AUTHENTICATOR_OPTIONS(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszPluginClsId: win32more.Windows.Win32.Foundation.PWSTR
    pwszPluginRpId: win32more.Windows.Win32.Foundation.PWSTR
    pwszLightThemeLogo: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogo: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_ADD_AUTHENTICATOR_OPTIONS_2(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    pClsid: POINTER(Guid)
    pwszPluginRpId: win32more.Windows.Win32.Foundation.PWSTR
    pwszLightThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
    cSupportedRpIds: UInt32
    ppwszSupportedRpIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    pwszUserVerificationKeyName: win32more.Windows.Win32.Foundation.PWSTR
class EXPERIMENTAL_WEBAUTHN_PLUGIN_ADD_AUTHENTICATOR_RESPONSE(Structure):
    cbOpSignPubKey: UInt32
    pbOpSignPubKey: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_CANCEL_OPERATION_REQUEST(Structure):
    transactionId: Guid
    cbRequestSignature: UInt32
    pbRequestSignature: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_CREDENTIAL_DETAILS(Structure):
    cbCredentialId: UInt32
    pbCredentialId: POINTER(Byte)
    pwszRpId: win32more.Windows.Win32.Foundation.PWSTR
    pwszRpName: win32more.Windows.Win32.Foundation.PWSTR
    cbUserId: UInt32
    pbUserId: POINTER(Byte)
    pwszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pwszUserDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class EXPERIMENTAL_WEBAUTHN_PLUGIN_CREDENTIAL_DETAILS_LIST(Structure):
    pwszPluginClsId: win32more.Windows.Win32.Foundation.PWSTR
    cCredentialDetails: UInt32
    pCredentialDetails: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_CREDENTIAL_DETAILS))
class EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_REQUEST(Structure):
    hWnd: win32more.Windows.Win32.Foundation.HWND
    transactionId: Guid
    cbRequestSignature: UInt32
    pbRequestSignature: POINTER(Byte)
    cbEncodedRequest: UInt32
    pbEncodedRequest: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_OPERATION_RESPONSE(Structure):
    cbEncodedResponse: UInt32
    pbEncodedResponse: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    transactionId: POINTER(Guid)
    type: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE
    pwszUsername: win32more.Windows.Win32.Foundation.PWSTR
    pwszContext: win32more.Windows.Win32.Foundation.PWSTR
EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = Int32
PerformUv: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 1
GetUvCount: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 2
GetPubKey: win32more.Windows.Win32.Security.Authentication.WebAuthn.EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 3
class EXPERIMENTAL_WEBAUTHN_PLUGIN_PERFORM_UV_RESPONSE(Structure):
    cbResponse: UInt32
    pbResponse: POINTER(Byte)
@winfunctype_pointer
def EXPERIMENTAL_WEBAUTHN_PLUGIN_STATUS_CHANGE_CALLBACK(context: VoidPtr) -> Void: ...
class EXPERIMENTAL_WEBAUTHN_PLUGIN_UPDATE_AUTHENTICATOR_DETAILS(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszPluginClsId: win32more.Windows.Win32.Foundation.PWSTR
    pwszNewPluginClsId: win32more.Windows.Win32.Foundation.PWSTR
    pwszLightThemeLogo: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogo: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
class EXPERIMENTAL_WEBAUTHN_PLUGIN_UPDATE_AUTHENTICATOR_DETAILS_2(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    pClsid: POINTER(Guid)
    pClsidNew: POINTER(Guid)
    pwszLightThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
    cSupportedRpIds: UInt32
    ppwszSupportedRpIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    pwszUserVerificationKeyName: win32more.Windows.Win32.Foundation.PWSTR
class EXPERIMENTAL_WEBAUTHN_PLUGIN_USER_VERIFICATION_REQUEST_2(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    pGuidTransactionId: POINTER(Guid)
    pwszUsername: win32more.Windows.Win32.Foundation.PWSTR
    pwszDisplayHint: win32more.Windows.Win32.Foundation.PWSTR
    cbBufferToSign: UInt32
    pbBufferToSign: POINTER(Byte)
class IPluginAuthenticator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d26bcf6f-b54c-43ff-9f06-d5bf148625f7}')
    @commethod(3)
    def MakeCredential(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_OPERATION_REQUEST), response: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_OPERATION_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAssertion(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_OPERATION_REQUEST), response: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_OPERATION_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelOperation(self, request: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_CANCEL_OPERATION_REQUEST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLockStatus(self, lockStatus: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.PLUGIN_LOCK_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PLUGIN_LOCK_STATUS = Int32
PluginLocked: win32more.Windows.Win32.Security.Authentication.WebAuthn.PLUGIN_LOCK_STATUS = 0
PluginUnlocked: win32more.Windows.Win32.Security.Authentication.WebAuthn.PLUGIN_LOCK_STATUS = 1
class WEBAUTHN_ASSERTION(Structure):
    dwVersion: UInt32
    cbAuthenticatorData: UInt32
    pbAuthenticatorData: POINTER(Byte)
    cbSignature: UInt32
    pbSignature: POINTER(Byte)
    Credential: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL
    cbUserId: UInt32
    pbUserId: POINTER(Byte)
    Extensions: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_EXTENSIONS
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: POINTER(Byte)
    dwCredLargeBlobStatus: UInt32
    pHmacSecret: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT)
    dwUsedTransport: UInt32
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
    cbClientDataJSON: UInt32
    pbClientDataJSON: POINTER(Byte)
    cbAuthenticationResponseJSON: UInt32
    pbAuthenticationResponseJSON: POINTER(Byte)
class WEBAUTHN_AUTHENTICATOR_DETAILS(Structure):
    dwVersion: UInt32
    cbAuthenticatorId: UInt32
    pbAuthenticatorId: POINTER(Byte)
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorLogo: UInt32
    pbAuthenticatorLogo: POINTER(Byte)
    bLocked: win32more.Windows.Win32.Foundation.BOOL
class WEBAUTHN_AUTHENTICATOR_DETAILS_LIST(Structure):
    cAuthenticatorDetails: UInt32
    ppAuthenticatorDetails: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_AUTHENTICATOR_DETAILS))
class WEBAUTHN_AUTHENTICATOR_DETAILS_OPTIONS(Structure):
    dwVersion: UInt32
class WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIALS
    Extensions: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    dwUserVerificationRequirement: UInt32
    dwFlags: UInt32
    pwszU2fAppId: win32more.Windows.Win32.Foundation.PWSTR
    pbU2fAppId: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    pCancellationId: POINTER(Guid)
    pAllowCredentialList: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST)
    dwCredLargeBlobOperation: UInt32
    cbCredLargeBlob: UInt32
    pbCredLargeBlob: POINTER(Byte)
    pHmacSecretSaltValues: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT_VALUES)
    bBrowserInPrivateMode: win32more.Windows.Win32.Foundation.BOOL
    pLinkedDevice: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.CTAPCBOR_HYBRID_STORAGE_LINKED_DATA)
    bAutoFill: win32more.Windows.Win32.Foundation.BOOL
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
    cCredentialHints: UInt32
    ppwszCredentialHints: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    pwszRemoteWebOrigin: win32more.Windows.Win32.Foundation.PWSTR
    cbPublicKeyCredentialRequestOptionsJSON: UInt32
    pbPublicKeyCredentialRequestOptionsJSON: POINTER(Byte)
    cbAuthenticatorId: UInt32
    pbAuthenticatorId: POINTER(Byte)
class WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS(Structure):
    dwVersion: UInt32
    dwTimeoutMilliseconds: UInt32
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIALS
    Extensions: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_EXTENSIONS
    dwAuthenticatorAttachment: UInt32
    bRequireResidentKey: win32more.Windows.Win32.Foundation.BOOL
    dwUserVerificationRequirement: UInt32
    dwAttestationConveyancePreference: UInt32
    dwFlags: UInt32
    pCancellationId: POINTER(Guid)
    pExcludeCredentialList: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST)
    dwEnterpriseAttestation: UInt32
    dwLargeBlobSupport: UInt32
    bPreferResidentKey: win32more.Windows.Win32.Foundation.BOOL
    bBrowserInPrivateMode: win32more.Windows.Win32.Foundation.BOOL
    bEnablePrf: win32more.Windows.Win32.Foundation.BOOL
    pLinkedDevice: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.CTAPCBOR_HYBRID_STORAGE_LINKED_DATA)
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
    pPRFGlobalEval: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT)
    cCredentialHints: UInt32
    ppwszCredentialHints: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    bThirdPartyPayment: win32more.Windows.Win32.Foundation.BOOL
    pwszRemoteWebOrigin: win32more.Windows.Win32.Foundation.PWSTR
    cbPublicKeyCredentialCreationOptionsJSON: UInt32
    pbPublicKeyCredentialCreationOptionsJSON: POINTER(Byte)
    cbAuthenticatorId: UInt32
    pbAuthenticatorId: POINTER(Byte)
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
    pX5c: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_X5C)
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
    pCredentialParameters: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_COSE_CREDENTIAL_PARAMETER)
class WEBAUTHN_CREDENTIAL(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: POINTER(Byte)
    pwszCredentialType: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_CREDENTIALS(Structure):
    cCredentials: UInt32
    pCredentials: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL)
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
    Extensions: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_EXTENSIONS
    dwUsedTransport: UInt32
    bEpAtt: win32more.Windows.Win32.Foundation.BOOL
    bLargeBlobSupported: win32more.Windows.Win32.Foundation.BOOL
    bResidentKey: win32more.Windows.Win32.Foundation.BOOL
    bPrfEnabled: win32more.Windows.Win32.Foundation.BOOL
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
    pHmacSecret: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT)
    bThirdPartyPayment: win32more.Windows.Win32.Foundation.BOOL
    dwTransports: UInt32
    cbClientDataJSON: UInt32
    pbClientDataJSON: POINTER(Byte)
    cbRegistrationResponseJSON: UInt32
    pbRegistrationResponseJSON: POINTER(Byte)
class WEBAUTHN_CREDENTIAL_DETAILS(Structure):
    dwVersion: UInt32
    cbCredentialID: UInt32
    pbCredentialID: POINTER(Byte)
    pRpInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_RP_ENTITY_INFORMATION)
    pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION)
    bRemovable: win32more.Windows.Win32.Foundation.BOOL
    bBackedUp: win32more.Windows.Win32.Foundation.BOOL
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorLogo: UInt32
    pbAuthenticatorLogo: POINTER(Byte)
    bThirdPartyPayment: win32more.Windows.Win32.Foundation.BOOL
    dwTransports: UInt32
class WEBAUTHN_CREDENTIAL_DETAILS_LIST(Structure):
    cCredentialDetails: UInt32
    ppCredentialDetails: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_DETAILS))
class WEBAUTHN_CREDENTIAL_EX(Structure):
    dwVersion: UInt32
    cbId: UInt32
    pbId: POINTER(Byte)
    pwszCredentialType: win32more.Windows.Win32.Foundation.PWSTR
    dwTransports: UInt32
class WEBAUTHN_CREDENTIAL_LIST(Structure):
    cCredentials: UInt32
    ppCredentials: POINTER(POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_EX))
class WEBAUTHN_CRED_BLOB_EXTENSION(Structure):
    cbCredBlob: UInt32
    pbCredBlob: POINTER(Byte)
class WEBAUTHN_CRED_PROTECT_EXTENSION_IN(Structure):
    dwCredProtect: UInt32
    bRequireCredProtect: win32more.Windows.Win32.Foundation.BOOL
class WEBAUTHN_CRED_WITH_HMAC_SECRET_SALT(Structure):
    cbCredID: UInt32
    pbCredID: POINTER(Byte)
    pHmacSecretSalt: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT)
class WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS(Structure):
    dwVersion: UInt32
    lUp: Int32
    lUv: Int32
    lRequireResidentKey: Int32
class WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY(Structure):
    dwVersion: UInt32
    lKty: Int32
    lAlg: Int32
    lCrv: Int32
    cbX: UInt32
    pbX: POINTER(Byte)
    cbY: UInt32
    pbY: POINTER(Byte)
class WEBAUTHN_CTAPCBOR_GET_ASSERTION_REQUEST(Structure):
    dwVersion: UInt32
    pwszRpId: win32more.Windows.Win32.Foundation.PWSTR
    cbRpId: UInt32
    pbRpId: POINTER(Byte)
    cbClientDataHash: UInt32
    pbClientDataHash: POINTER(Byte)
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST
    cbCborExtensionsMap: UInt32
    pbCborExtensionsMap: POINTER(Byte)
    pAuthenticatorOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS)
    fEmptyPinAuth: win32more.Windows.Win32.Foundation.BOOL
    cbPinAuth: UInt32
    pbPinAuth: POINTER(Byte)
    pHmacSaltExtension: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION)
    cbHmacSecretSaltValues: UInt32
    pbHmacSecretSaltValues: POINTER(Byte)
    dwPinProtocol: UInt32
    lCredBlobExt: Int32
    lLargeBlobKeyExt: Int32
    dwCredLargeBlobOperation: UInt32
    cbCredLargeBlobCompressed: UInt32
    pbCredLargeBlobCompressed: POINTER(Byte)
    dwCredLargeBlobOriginalSize: UInt32
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class WEBAUTHN_CTAPCBOR_GET_ASSERTION_RESPONSE(Structure):
    WebAuthNAssertion: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_ASSERTION
    pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION)
    dwNumberOfCredentials: UInt32
    lUserSelected: Int32
    cbLargeBlobKey: UInt32
    pbLargeBlobKey: POINTER(Byte)
    cbUnsignedExtensionOutputs: UInt32
    pbUnsignedExtensionOutputs: POINTER(Byte)
class WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION(Structure):
    dwVersion: UInt32
    pKeyAgreement: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CTAPCBOR_ECC_PUBLIC_KEY)
    cbEncryptedSalt: UInt32
    pbEncryptedSalt: POINTER(Byte)
    cbSaltAuth: UInt32
    pbSaltAuth: POINTER(Byte)
class WEBAUTHN_CTAPCBOR_MAKE_CREDENTIAL_REQUEST(Structure):
    dwVersion: UInt32
    cbRpId: UInt32
    pbRpId: POINTER(Byte)
    cbClientDataHash: UInt32
    pbClientDataHash: POINTER(Byte)
    pRpInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_RP_ENTITY_INFORMATION)
    pUserInformation: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_USER_ENTITY_INFORMATION)
    WebAuthNCredentialParameters: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS
    CredentialList: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CREDENTIAL_LIST
    cbCborExtensionsMap: UInt32
    pbCborExtensionsMap: POINTER(Byte)
    pAuthenticatorOptions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CTAPCBOR_AUTHENTICATOR_OPTIONS)
    fEmptyPinAuth: win32more.Windows.Win32.Foundation.BOOL
    cbPinAuth: UInt32
    pbPinAuth: POINTER(Byte)
    lHmacSecretExt: Int32
    pHmacSecretMcExtension: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CTAPCBOR_HMAC_SALT_EXTENSION)
    lPrfExt: Int32
    cbHmacSecretSaltValues: UInt32
    pbHmacSecretSaltValues: POINTER(Byte)
    dwCredProtect: UInt32
    dwPinProtocol: UInt32
    dwEnterpriseAttestation: UInt32
    cbCredBlobExt: UInt32
    pbCredBlobExt: POINTER(Byte)
    lLargeBlobKeyExt: Int32
    dwLargeBlobSupport: UInt32
    lMinPinLengthExt: Int32
    cbJsonExt: UInt32
    pbJsonExt: POINTER(Byte)
class WEBAUTHN_EXTENSION(Structure):
    pwszExtensionIdentifier: win32more.Windows.Win32.Foundation.PWSTR
    cbExtension: UInt32
    pvExtension: VoidPtr
class WEBAUTHN_EXTENSIONS(Structure):
    cExtensions: UInt32
    pExtensions: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_EXTENSION)
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
    pGlobalHmacSalt: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_HMAC_SECRET_SALT)
    cCredWithHmacSecretSaltList: UInt32
    pCredWithHmacSecretSaltList: POINTER(win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_CRED_WITH_HMAC_SECRET_SALT)
class WEBAUTHN_PLUGIN_ADD_AUTHENTICATOR_OPTIONS(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    rclsid: POINTER(Guid)
    pwszPluginRpId: win32more.Windows.Win32.Foundation.PWSTR
    pwszLightThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
    cSupportedRpIds: UInt32
    ppwszSupportedRpIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class WEBAUTHN_PLUGIN_ADD_AUTHENTICATOR_RESPONSE(Structure):
    cbOpSignPubKey: UInt32
    pbOpSignPubKey: POINTER(Byte)
class WEBAUTHN_PLUGIN_CANCEL_OPERATION_REQUEST(Structure):
    transactionId: Guid
    cbRequestSignature: UInt32
    pbRequestSignature: POINTER(Byte)
class WEBAUTHN_PLUGIN_CREDENTIAL_DETAILS(Structure):
    cbCredentialId: UInt32
    pbCredentialId: POINTER(Byte)
    pwszRpId: win32more.Windows.Win32.Foundation.PWSTR
    pwszRpName: win32more.Windows.Win32.Foundation.PWSTR
    cbUserId: UInt32
    pbUserId: POINTER(Byte)
    pwszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pwszUserDisplayName: win32more.Windows.Win32.Foundation.PWSTR
class WEBAUTHN_PLUGIN_OPERATION_REQUEST(Structure):
    hWnd: win32more.Windows.Win32.Foundation.HWND
    transactionId: Guid
    cbRequestSignature: UInt32
    pbRequestSignature: POINTER(Byte)
    requestType: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_REQUEST_TYPE
    cbEncodedRequest: UInt32
    pbEncodedRequest: POINTER(Byte)
class WEBAUTHN_PLUGIN_OPERATION_RESPONSE(Structure):
    cbEncodedResponse: UInt32
    pbEncodedResponse: POINTER(Byte)
WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = Int32
PerformUserVerification: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 1
GetUserVerificationCount: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 2
GetPublicKey: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_PERFORM_UV_OPERATION_TYPE = 3
WEBAUTHN_PLUGIN_REQUEST_TYPE = Int32
WEBAUTHN_PLUGIN_REQUEST_TYPE_CTAP2_CBOR: win32more.Windows.Win32.Security.Authentication.WebAuthn.WEBAUTHN_PLUGIN_REQUEST_TYPE = 1
@winfunctype_pointer
def WEBAUTHN_PLUGIN_STATUS_CHANGE_CALLBACK(context: VoidPtr) -> Void: ...
class WEBAUTHN_PLUGIN_UPDATE_AUTHENTICATOR_DETAILS(Structure):
    pwszAuthenticatorName: win32more.Windows.Win32.Foundation.PWSTR
    rclsid: POINTER(Guid)
    rclsidNew: POINTER(Guid)
    pwszLightThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    pwszDarkThemeLogoSvg: win32more.Windows.Win32.Foundation.PWSTR
    cbAuthenticatorInfo: UInt32
    pbAuthenticatorInfo: POINTER(Byte)
    cSupportedRpIds: UInt32
    ppwszSupportedRpIds: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class WEBAUTHN_PLUGIN_USER_VERIFICATION_REQUEST(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    rguidTransactionId: POINTER(Guid)
    pwszUsername: win32more.Windows.Win32.Foundation.PWSTR
    pwszDisplayHint: win32more.Windows.Win32.Foundation.PWSTR
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


make_ready(__name__)
