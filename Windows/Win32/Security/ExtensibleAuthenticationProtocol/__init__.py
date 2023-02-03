from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Data.Xml.MsXml
import Windows.Win32.Foundation
import Windows.Win32.Security.Cryptography
import Windows.Win32.Security.ExtensibleAuthenticationProtocol
import Windows.Win32.System.Com
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
FACILITY_EAP_MESSAGE: UInt32 = 2114
EAP_GROUP_MASK: Int32 = 65280
EAP_E_EAPHOST_FIRST: Int32 = -2143158272
EAP_E_EAPHOST_LAST: Int32 = -2143158017
EAP_I_EAPHOST_FIRST: Int32 = -2143158272
EAP_I_EAPHOST_LAST: Int32 = -2143158017
EAP_E_CERT_STORE_INACCESSIBLE: UInt32 = 2151809040
EAP_E_EAPHOST_METHOD_NOT_INSTALLED: UInt32 = 2151809041
EAP_E_EAPHOST_THIRDPARTY_METHOD_HOST_RESET: UInt32 = 2151809042
EAP_E_EAPHOST_EAPQEC_INACCESSIBLE: UInt32 = 2151809043
EAP_E_EAPHOST_IDENTITY_UNKNOWN: UInt32 = 2151809044
EAP_E_AUTHENTICATION_FAILED: UInt32 = 2151809045
EAP_I_EAPHOST_EAP_NEGOTIATION_FAILED: UInt32 = 1078067222
EAP_E_EAPHOST_METHOD_INVALID_PACKET: UInt32 = 2151809047
EAP_E_EAPHOST_REMOTE_INVALID_PACKET: UInt32 = 2151809048
EAP_E_EAPHOST_XML_MALFORMED: UInt32 = 2151809049
EAP_E_METHOD_CONFIG_DOES_NOT_SUPPORT_SSO: UInt32 = 2151809050
EAP_E_EAPHOST_METHOD_OPERATION_NOT_SUPPORTED: UInt32 = 2151809056
EAP_E_USER_FIRST: Int32 = -2143158016
EAP_E_USER_LAST: Int32 = -2143157761
EAP_I_USER_FIRST: Int32 = 1078067456
EAP_I_USER_LAST: Int32 = 1078067711
EAP_E_USER_CERT_NOT_FOUND: UInt32 = 2151809280
EAP_E_USER_CERT_INVALID: UInt32 = 2151809281
EAP_E_USER_CERT_EXPIRED: UInt32 = 2151809282
EAP_E_USER_CERT_REVOKED: UInt32 = 2151809283
EAP_E_USER_CERT_OTHER_ERROR: UInt32 = 2151809284
EAP_E_USER_CERT_REJECTED: UInt32 = 2151809285
EAP_I_USER_ACCOUNT_OTHER_ERROR: UInt32 = 1078067472
EAP_E_USER_CREDENTIALS_REJECTED: UInt32 = 2151809297
EAP_E_USER_NAME_PASSWORD_REJECTED: UInt32 = 2151809298
EAP_E_NO_SMART_CARD_READER: UInt32 = 2151809299
EAP_E_SERVER_FIRST: Int32 = -2143157760
EAP_E_SERVER_LAST: Int32 = -2143157505
EAP_E_SERVER_CERT_NOT_FOUND: UInt32 = 2151809536
EAP_E_SERVER_CERT_INVALID: UInt32 = 2151809537
EAP_E_SERVER_CERT_EXPIRED: UInt32 = 2151809538
EAP_E_SERVER_CERT_REVOKED: UInt32 = 2151809539
EAP_E_SERVER_CERT_OTHER_ERROR: UInt32 = 2151809540
EAP_E_USER_ROOT_CERT_FIRST: Int32 = -2143157504
EAP_E_USER_ROOT_CERT_LAST: Int32 = -2143157249
EAP_E_USER_ROOT_CERT_NOT_FOUND: UInt32 = 2151809792
EAP_E_USER_ROOT_CERT_INVALID: UInt32 = 2151809793
EAP_E_USER_ROOT_CERT_EXPIRED: UInt32 = 2151809794
EAP_E_SERVER_ROOT_CERT_FIRST: Int32 = -2143157248
EAP_E_SERVER_ROOT_CERT_LAST: Int32 = -2143156993
EAP_E_SERVER_ROOT_CERT_NOT_FOUND: UInt32 = 2151810048
EAP_E_SERVER_ROOT_CERT_INVALID: UInt32 = 2151810049
EAP_E_SERVER_ROOT_CERT_NAME_REQUIRED: UInt32 = 2151810054
EAP_E_SIM_NOT_VALID: UInt32 = 2151810304
EAP_METHOD_INVALID_PACKET: UInt32 = 2151809047
EAP_INVALID_PACKET: UInt32 = 2151809048
EAP_PEER_FLAG_GUEST_ACCESS: UInt32 = 64
eapPropCipherSuiteNegotiation: UInt32 = 1
eapPropMutualAuth: UInt32 = 2
eapPropIntegrity: UInt32 = 4
eapPropReplayProtection: UInt32 = 8
eapPropConfidentiality: UInt32 = 16
eapPropKeyDerivation: UInt32 = 32
eapPropKeyStrength64: UInt32 = 64
eapPropKeyStrength128: UInt32 = 128
eapPropKeyStrength256: UInt32 = 256
eapPropKeyStrength512: UInt32 = 512
eapPropKeyStrength1024: UInt32 = 1024
eapPropDictionaryAttackResistance: UInt32 = 2048
eapPropFastReconnect: UInt32 = 4096
eapPropCryptoBinding: UInt32 = 8192
eapPropSessionIndependence: UInt32 = 16384
eapPropFragmentation: UInt32 = 32768
eapPropChannelBinding: UInt32 = 65536
eapPropNap: UInt32 = 131072
eapPropStandalone: UInt32 = 262144
eapPropMppeEncryption: UInt32 = 524288
eapPropTunnelMethod: UInt32 = 1048576
eapPropSupportsConfig: UInt32 = 2097152
eapPropCertifiedMethod: UInt32 = 4194304
eapPropHiddenMethod: UInt32 = 8388608
eapPropMachineAuth: UInt32 = 16777216
eapPropUserAuth: UInt32 = 33554432
eapPropIdentityPrivacy: UInt32 = 67108864
eapPropMethodChaining: UInt32 = 134217728
eapPropSharedStateEquivalence: UInt32 = 268435456
eapPropReserved: UInt32 = 2147483648
EAP_VALUENAME_PROPERTIES: String = 'Properties'
EAP_FLAG_Reserved1: UInt32 = 1
EAP_FLAG_NON_INTERACTIVE: UInt32 = 2
EAP_FLAG_LOGON: UInt32 = 4
EAP_FLAG_PREVIEW: UInt32 = 8
EAP_FLAG_Reserved2: UInt32 = 16
EAP_FLAG_MACHINE_AUTH: UInt32 = 32
EAP_FLAG_GUEST_ACCESS: UInt32 = 64
EAP_FLAG_Reserved3: UInt32 = 128
EAP_FLAG_Reserved4: UInt32 = 256
EAP_FLAG_RESUME_FROM_HIBERNATE: UInt32 = 512
EAP_FLAG_Reserved5: UInt32 = 1024
EAP_FLAG_Reserved6: UInt32 = 2048
EAP_FLAG_FULL_AUTH: UInt32 = 4096
EAP_FLAG_PREFER_ALT_CREDENTIALS: UInt32 = 8192
EAP_FLAG_Reserved7: UInt32 = 16384
EAP_PEER_FLAG_HEALTH_STATE_CHANGE: UInt32 = 32768
EAP_FLAG_SUPRESS_UI: UInt32 = 65536
EAP_FLAG_PRE_LOGON: UInt32 = 131072
EAP_FLAG_USER_AUTH: UInt32 = 262144
EAP_FLAG_CONFG_READONLY: UInt32 = 524288
EAP_FLAG_Reserved8: UInt32 = 1048576
EAP_FLAG_Reserved9: UInt32 = 4194304
EAP_FLAG_VPN: UInt32 = 8388608
EAP_FLAG_ONLY_EAP_TLS: UInt32 = 16777216
EAP_FLAG_SERVER_VALIDATION_REQUIRED: UInt32 = 33554432
EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT: UInt32 = 0
EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE: UInt32 = 1
EAP_CONFIG_INPUT_FIELD_PROPS_NON_PERSIST: UInt32 = 2
EAP_UI_INPUT_FIELD_PROPS_DEFAULT: UInt32 = 0
EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE: UInt32 = 1
EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST: UInt32 = 2
EAP_UI_INPUT_FIELD_PROPS_READ_ONLY: UInt32 = 4
EAP_CREDENTIAL_VERSION: UInt32 = 1
EAP_INTERACTIVE_UI_DATA_VERSION: UInt32 = 1
EAPHOST_PEER_API_VERSION: UInt32 = 1
EAPHOST_METHOD_API_VERSION: UInt32 = 1
MAX_EAP_CONFIG_INPUT_FIELD_LENGTH: UInt32 = 256
MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH: UInt32 = 1024
CERTIFICATE_HASH_LENGTH: UInt32 = 20
NCRYPT_PIN_CACHE_PIN_BYTE_LENGTH: UInt32 = 90
EAP_REGISTRY_LOCATION: String = 'System\\CurrentControlSet\\Services\\EapHost\\Methods'
EAP_PEER_VALUENAME_DLL_PATH: String = 'PeerDllPath'
EAP_PEER_VALUENAME_FRIENDLY_NAME: String = 'PeerFriendlyName'
EAP_PEER_VALUENAME_CONFIGUI: String = 'PeerConfigUIPath'
EAP_PEER_VALUENAME_REQUIRE_CONFIGUI: String = 'PeerRequireConfigUI'
EAP_PEER_VALUENAME_IDENTITY: String = 'PeerIdentityPath'
EAP_PEER_VALUENAME_INTERACTIVEUI: String = 'PeerInteractiveUIPath'
EAP_PEER_VALUENAME_INVOKE_NAMEDLG: String = 'PeerInvokeUsernameDialog'
EAP_PEER_VALUENAME_INVOKE_PWDDLG: String = 'PeerInvokePasswordDialog'
EAP_PEER_VALUENAME_PROPERTIES: String = 'Properties'
EAP_AUTHENTICATOR_VALUENAME_DLL_PATH: String = 'AuthenticatorDllPath'
EAP_AUTHENTICATOR_VALUENAME_FRIENDLY_NAME: String = 'AuthenticatorFriendlyName'
EAP_AUTHENTICATOR_VALUENAME_PROPERTIES: String = 'Properties'
EAP_AUTHENTICATOR_VALUENAME_CONFIGUI: String = 'AuthenticatorConfigUIPath'
EAP_METHOD_AUTHENTICATOR_CONFIG_IS_IDENTITY_PRIVACY: UInt32 = 1
RAS_EAP_REGISTRY_LOCATION: String = 'System\\CurrentControlSet\\Services\\Rasman\\PPP\\EAP'
RAS_EAP_VALUENAME_PATH: String = 'Path'
RAS_EAP_VALUENAME_CONFIGUI: String = 'ConfigUIPath'
RAS_EAP_VALUENAME_INTERACTIVEUI: String = 'InteractiveUIPath'
RAS_EAP_VALUENAME_IDENTITY: String = 'IdentityPath'
RAS_EAP_VALUENAME_FRIENDLY_NAME: String = 'FriendlyName'
RAS_EAP_VALUENAME_DEFAULT_DATA: String = 'ConfigData'
RAS_EAP_VALUENAME_REQUIRE_CONFIGUI: String = 'RequireConfigUI'
RAS_EAP_VALUENAME_ENCRYPTION: String = 'MPPEEncryptionSupported'
RAS_EAP_VALUENAME_INVOKE_NAMEDLG: String = 'InvokeUsernameDialog'
RAS_EAP_VALUENAME_INVOKE_PWDDLG: String = 'InvokePasswordDialog'
RAS_EAP_VALUENAME_CONFIG_CLSID: String = 'ConfigCLSID'
RAS_EAP_VALUENAME_STANDALONE_SUPPORTED: String = 'StandaloneSupported'
RAS_EAP_VALUENAME_ROLES_SUPPORTED: String = 'RolesSupported'
RAS_EAP_VALUENAME_PER_POLICY_CONFIG: String = 'PerPolicyConfig'
RAS_EAP_VALUENAME_ISTUNNEL_METHOD: String = 'IsTunnelMethod'
RAS_EAP_VALUENAME_FILTER_INNERMETHODS: String = 'FilterInnerMethods'
RAS_EAP_ROLE_AUTHENTICATOR: UInt32 = 1
RAS_EAP_ROLE_AUTHENTICATEE: UInt32 = 2
RAS_EAP_ROLE_EXCLUDE_IN_EAP: UInt32 = 4
RAS_EAP_ROLE_EXCLUDE_IN_PEAP: UInt32 = 8
RAS_EAP_ROLE_EXCLUDE_IN_VPN: UInt32 = 16
raatARAPChallenge: UInt32 = 33
raatARAPOldPassword: UInt32 = 19
raatARAPNewPassword: UInt32 = 20
raatARAPPasswordChangeReason: UInt32 = 21
EAPCODE_Request: UInt32 = 1
EAPCODE_Response: UInt32 = 2
EAPCODE_Success: UInt32 = 3
EAPCODE_Failure: UInt32 = 4
MAXEAPCODE: UInt32 = 4
RAS_EAP_FLAG_ROUTER: UInt32 = 1
RAS_EAP_FLAG_NON_INTERACTIVE: UInt32 = 2
RAS_EAP_FLAG_LOGON: UInt32 = 4
RAS_EAP_FLAG_PREVIEW: UInt32 = 8
RAS_EAP_FLAG_FIRST_LINK: UInt32 = 16
RAS_EAP_FLAG_MACHINE_AUTH: UInt32 = 32
RAS_EAP_FLAG_GUEST_ACCESS: UInt32 = 64
RAS_EAP_FLAG_8021X_AUTH: UInt32 = 128
RAS_EAP_FLAG_HOSTED_IN_PEAP: UInt32 = 256
RAS_EAP_FLAG_RESUME_FROM_HIBERNATE: UInt32 = 512
RAS_EAP_FLAG_PEAP_UPFRONT: UInt32 = 1024
RAS_EAP_FLAG_ALTERNATIVE_USER_DB: UInt32 = 2048
RAS_EAP_FLAG_PEAP_FORCE_FULL_AUTH: UInt32 = 4096
RAS_EAP_FLAG_PRE_LOGON: UInt32 = 131072
RAS_EAP_FLAG_CONFG_READONLY: UInt32 = 524288
RAS_EAP_FLAG_RESERVED: UInt32 = 1048576
RAS_EAP_FLAG_SAVE_CREDMAN: UInt32 = 2097152
RAS_EAP_FLAG_SERVER_VALIDATION_REQUIRED: UInt32 = 33554432
GUID_EapHost_Default: Guid = Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
GUID_EapHost_Cause_MethodDLLNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-01')
GUID_EapHost_Repair_ContactSysadmin: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-02')
GUID_EapHost_Cause_CertStoreInaccessible: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-04')
GUID_EapHost_Cause_Generic_AuthFailure: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-04')
GUID_EapHost_Cause_IdentityUnknown: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-04')
GUID_EapHost_Cause_SimNotValid: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-03-04')
GUID_EapHost_Cause_Server_CertExpired: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-05')
GUID_EapHost_Cause_Server_CertInvalid: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-06')
GUID_EapHost_Cause_Server_CertNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-07')
GUID_EapHost_Cause_Server_CertRevoked: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-08')
GUID_EapHost_Cause_Server_CertOtherError: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-08')
GUID_EapHost_Cause_User_CertExpired: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-09')
GUID_EapHost_Cause_User_CertInvalid: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0a')
GUID_EapHost_Cause_User_CertNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0b')
GUID_EapHost_Cause_User_CertOtherError: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0c')
GUID_EapHost_Cause_User_CertRejected: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0d')
GUID_EapHost_Cause_User_CertRevoked: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0e')
GUID_EapHost_Cause_User_Account_OtherProblem: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-0e')
GUID_EapHost_Cause_User_CredsRejected: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-0e')
GUID_EapHost_Cause_User_Root_CertExpired: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0f')
GUID_EapHost_Cause_User_Root_CertInvalid: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-10')
GUID_EapHost_Cause_User_Root_CertNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-11')
GUID_EapHost_Cause_Server_Root_CertNameRequired: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-12')
GUID_EapHost_Cause_Server_Root_CertNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-12')
GUID_EapHost_Cause_ThirdPartyMethod_Host_Reset: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-12')
GUID_EapHost_Cause_EapQecInaccessible: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-03-12')
GUID_EapHost_Repair_Server_ClientSelectServerCert: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-18')
GUID_EapHost_Repair_User_AuthFailure: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-19')
GUID_EapHost_Repair_User_GetNewCert: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1a')
GUID_EapHost_Repair_User_SelectValidCert: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1b')
GUID_EapHost_Repair_Retry_Authentication: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-1b')
GUID_EapHost_Cause_EapNegotiationFailed: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1c')
GUID_EapHost_Cause_XmlMalformed: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1d')
GUID_EapHost_Cause_MethodDoesNotSupportOperation: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1e')
GUID_EapHost_Repair_ContactAdmin_AuthFailure: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1f')
GUID_EapHost_Repair_ContactAdmin_IdentityUnknown: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-20')
GUID_EapHost_Repair_ContactAdmin_NegotiationFailed: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-21')
GUID_EapHost_Repair_ContactAdmin_MethodNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-22')
GUID_EapHost_Repair_RestartNap: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-23')
GUID_EapHost_Repair_ContactAdmin_CertStoreInaccessible: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-24')
GUID_EapHost_Repair_ContactAdmin_InvalidUserAccount: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-25')
GUID_EapHost_Repair_ContactAdmin_RootCertInvalid: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-26')
GUID_EapHost_Repair_ContactAdmin_RootCertNotFound: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-27')
GUID_EapHost_Repair_ContactAdmin_RootExpired: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-28')
GUID_EapHost_Repair_ContactAdmin_CertNameAbsent: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-29')
GUID_EapHost_Repair_ContactAdmin_NoSmartCardReader: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2a')
GUID_EapHost_Cause_No_SmartCardReader_Found: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2b')
GUID_EapHost_Repair_ContactAdmin_InvalidUserCert: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2c')
GUID_EapHost_Repair_Method_Not_Support_Sso: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2d')
GUID_EapHost_Repair_No_ValidSim_Found: Guid = Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2e')
GUID_EapHost_Help_ObtainingCerts: Guid = Guid('f535eea3-1bdd-46ca-a2-fc-a6-65-59-39-b7-e8')
GUID_EapHost_Help_Troubleshooting: Guid = Guid('33307acf-0698-41ba-b0-14-ea-0a-2e-b8-d0-a8')
GUID_EapHost_Cause_Method_Config_Does_Not_Support_Sso: Guid = Guid('da18bd32-004f-41fa-ae-08-0b-c8-5e-58-45-ac')
@winfunctype('eappcfg.dll')
def EapHostPeerGetMethods(pEapMethodInfoArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerGetMethodProperties(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, hUserImpersonationToken: Windows.Win32.Foundation.HANDLE, dwEapConnDataSize: UInt32, pbEapConnData: c_char_p_no, dwUserDataSize: UInt32, pbUserData: c_char_p_no, pMethodPropertyArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_ARRAY_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeConfigUI(hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: c_char_p_no, pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryCredentialInputFields(hUserImpersonationToken: Windows.Win32.Foundation.HANDLE, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: c_char_p_no, pEapConfigInputFieldArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUserBlobFromCredentialInputFields(hUserImpersonationToken: Windows.Win32.Foundation.HANDLE, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: c_char_p_no, pEapConfigInputFieldArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head), pdwUserBlobSize: POINTER(UInt32), ppbUserBlob: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeIdentityUI(dwVersion: UInt32, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, hwndParent: Windows.Win32.Foundation.HWND, dwSizeofConnectionData: UInt32, pConnectionData: c_char_p_no, dwSizeofUserData: UInt32, pUserData: c_char_p_no, pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(c_char_p_no), ppwszIdentity: POINTER(Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeInteractiveUI(hwndParent: Windows.Win32.Foundation.HWND, dwSizeofUIContextData: UInt32, pUIContextData: c_char_p_no, pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: c_char_p_no, pEapInteractiveUIData: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUIBlobFromInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: c_char_p_no, pEapInteractiveUIData: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head), pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigXml2Blob(dwFlags: UInt32, pConfigDoc: Windows.Win32.Data.Xml.MsXml.IXMLDOMNode_head, pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(c_char_p_no), pEapMethodType: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerCredentialsXml2Blob(dwFlags: UInt32, pCredentialsDoc: Windows.Win32.Data.Xml.MsXml.IXMLDOMNode_head, dwSizeOfConfigIn: UInt32, pConfigIn: c_char_p_no, pdwSizeOfCredentialsOut: POINTER(UInt32), ppCredentialsOut: POINTER(c_char_p_no), pEapMethodType: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigBlob2Xml(dwFlags: UInt32, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: c_char_p_no, ppConfigDoc: POINTER(Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument2_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeMemory(pData: c_char_p_no) -> Void: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeErrorMemory(pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerInitialize() -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerUninitialize() -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerBeginSession(dwFlags: UInt32, eapType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, pAttributeArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), hTokenImpersonateUser: Windows.Win32.Foundation.HANDLE, dwSizeofConnectionData: UInt32, pConnectionData: c_char_p_no, dwSizeofUserData: UInt32, pUserData: c_char_p_no, dwMaxSendPacketSize: UInt32, pConnectionId: POINTER(Guid), func: Windows.Win32.Security.ExtensibleAuthenticationProtocol.NotificationHandler, pContextData: c_void_p, pSessionId: POINTER(UInt32), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerProcessReceivedPacket(sessionHandle: UInt32, cbReceivePacket: UInt32, pReceivePacket: c_char_p_no, pEapOutput: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetSendPacket(sessionHandle: UInt32, pcbSendPacket: POINTER(UInt32), ppSendPacket: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResult(sessionHandle: UInt32, reason: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason, ppResult: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResult_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetUIContext(sessionHandle: UInt32, pdwSizeOfUIContextData: POINTER(UInt32), ppUIContextData: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetUIContext(sessionHandle: UInt32, dwSizeOfUIContextData: UInt32, pUIContextData: c_char_p_no, pEapOutput: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), pEapOutput: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetAuthStatus(sessionHandle: UInt32, authParam: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams, pcbAuthData: POINTER(UInt32), ppAuthData: POINTER(c_char_p_no), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerEndSession(sessionHandle: UInt32, ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetDataToUnplumbCredentials(pConnectionIdThatLastSavedCreds: POINTER(Guid), phCredentialImpersonationToken: POINTER(IntPtr), sessionHandle: UInt32, ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), fSaveToCredMan: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerClearConnection(pConnectionId: POINTER(Guid), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeEapError(pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetIdentity(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeofConnectionData: UInt32, pConnectionData: c_char_p_no, dwSizeofUserData: UInt32, pUserData: c_char_p_no, hTokenImpersonateUser: Windows.Win32.Foundation.HANDLE, pfInvokeUI: POINTER(Windows.Win32.Foundation.BOOL), pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(c_char_p_no), ppwszIdentity: POINTER(Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(c_char_p_no)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetEncryptedPassword(dwSizeofPassword: UInt32, szPassword: Windows.Win32.Foundation.PWSTR, ppszEncPassword: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeRuntimeMemory(pData: c_char_p_no) -> Void: ...
class EAPHOST_AUTH_INFO(Structure):
    status: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS
    dwErrorCode: UInt32
    dwReasonCode: UInt32
EAPHOST_AUTH_STATUS = Int32
EAPHOST_AUTH_STATUS_EapHostInvalidSession: EAPHOST_AUTH_STATUS = 0
EAPHOST_AUTH_STATUS_EapHostAuthNotStarted: EAPHOST_AUTH_STATUS = 1
EAPHOST_AUTH_STATUS_EapHostAuthIdentityExchange: EAPHOST_AUTH_STATUS = 2
EAPHOST_AUTH_STATUS_EapHostAuthNegotiatingType: EAPHOST_AUTH_STATUS = 3
EAPHOST_AUTH_STATUS_EapHostAuthInProgress: EAPHOST_AUTH_STATUS = 4
EAPHOST_AUTH_STATUS_EapHostAuthSucceeded: EAPHOST_AUTH_STATUS = 5
EAPHOST_AUTH_STATUS_EapHostAuthFailed: EAPHOST_AUTH_STATUS = 6
class EAPHOST_IDENTITY_UI_PARAMS(Structure):
    eapMethodType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    dwFlags: UInt32
    dwSizeofConnectionData: UInt32
    pConnectionData: c_char_p_no
    dwSizeofUserData: UInt32
    pUserData: c_char_p_no
    dwSizeofUserDataOut: UInt32
    pUserDataOut: c_char_p_no
    pwszIdentity: Windows.Win32.Foundation.PWSTR
    dwError: UInt32
    pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
class EAPHOST_INTERACTIVE_UI_PARAMS(Structure):
    dwSizeofContextData: UInt32
    pContextData: c_char_p_no
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: c_char_p_no
    dwError: UInt32
    pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
class EAP_ATTRIBUTE(Structure):
    eaType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE
    dwLength: UInt32
    pValue: c_char_p_no
class EAP_ATTRIBUTES(Structure):
    dwNumberOfAttributes: UInt32
    pAttribs: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_head)
EAP_ATTRIBUTE_TYPE = Int32
EAP_ATTRIBUTE_TYPE_eatMinimum: EAP_ATTRIBUTE_TYPE = 0
EAP_ATTRIBUTE_TYPE_eatUserName: EAP_ATTRIBUTE_TYPE = 1
EAP_ATTRIBUTE_TYPE_eatUserPassword: EAP_ATTRIBUTE_TYPE = 2
EAP_ATTRIBUTE_TYPE_eatMD5CHAPPassword: EAP_ATTRIBUTE_TYPE = 3
EAP_ATTRIBUTE_TYPE_eatNASIPAddress: EAP_ATTRIBUTE_TYPE = 4
EAP_ATTRIBUTE_TYPE_eatNASPort: EAP_ATTRIBUTE_TYPE = 5
EAP_ATTRIBUTE_TYPE_eatServiceType: EAP_ATTRIBUTE_TYPE = 6
EAP_ATTRIBUTE_TYPE_eatFramedProtocol: EAP_ATTRIBUTE_TYPE = 7
EAP_ATTRIBUTE_TYPE_eatFramedIPAddress: EAP_ATTRIBUTE_TYPE = 8
EAP_ATTRIBUTE_TYPE_eatFramedIPNetmask: EAP_ATTRIBUTE_TYPE = 9
EAP_ATTRIBUTE_TYPE_eatFramedRouting: EAP_ATTRIBUTE_TYPE = 10
EAP_ATTRIBUTE_TYPE_eatFilterId: EAP_ATTRIBUTE_TYPE = 11
EAP_ATTRIBUTE_TYPE_eatFramedMTU: EAP_ATTRIBUTE_TYPE = 12
EAP_ATTRIBUTE_TYPE_eatFramedCompression: EAP_ATTRIBUTE_TYPE = 13
EAP_ATTRIBUTE_TYPE_eatLoginIPHost: EAP_ATTRIBUTE_TYPE = 14
EAP_ATTRIBUTE_TYPE_eatLoginService: EAP_ATTRIBUTE_TYPE = 15
EAP_ATTRIBUTE_TYPE_eatLoginTCPPort: EAP_ATTRIBUTE_TYPE = 16
EAP_ATTRIBUTE_TYPE_eatUnassigned17: EAP_ATTRIBUTE_TYPE = 17
EAP_ATTRIBUTE_TYPE_eatReplyMessage: EAP_ATTRIBUTE_TYPE = 18
EAP_ATTRIBUTE_TYPE_eatCallbackNumber: EAP_ATTRIBUTE_TYPE = 19
EAP_ATTRIBUTE_TYPE_eatCallbackId: EAP_ATTRIBUTE_TYPE = 20
EAP_ATTRIBUTE_TYPE_eatUnassigned21: EAP_ATTRIBUTE_TYPE = 21
EAP_ATTRIBUTE_TYPE_eatFramedRoute: EAP_ATTRIBUTE_TYPE = 22
EAP_ATTRIBUTE_TYPE_eatFramedIPXNetwork: EAP_ATTRIBUTE_TYPE = 23
EAP_ATTRIBUTE_TYPE_eatState: EAP_ATTRIBUTE_TYPE = 24
EAP_ATTRIBUTE_TYPE_eatClass: EAP_ATTRIBUTE_TYPE = 25
EAP_ATTRIBUTE_TYPE_eatVendorSpecific: EAP_ATTRIBUTE_TYPE = 26
EAP_ATTRIBUTE_TYPE_eatSessionTimeout: EAP_ATTRIBUTE_TYPE = 27
EAP_ATTRIBUTE_TYPE_eatIdleTimeout: EAP_ATTRIBUTE_TYPE = 28
EAP_ATTRIBUTE_TYPE_eatTerminationAction: EAP_ATTRIBUTE_TYPE = 29
EAP_ATTRIBUTE_TYPE_eatCalledStationId: EAP_ATTRIBUTE_TYPE = 30
EAP_ATTRIBUTE_TYPE_eatCallingStationId: EAP_ATTRIBUTE_TYPE = 31
EAP_ATTRIBUTE_TYPE_eatNASIdentifier: EAP_ATTRIBUTE_TYPE = 32
EAP_ATTRIBUTE_TYPE_eatProxyState: EAP_ATTRIBUTE_TYPE = 33
EAP_ATTRIBUTE_TYPE_eatLoginLATService: EAP_ATTRIBUTE_TYPE = 34
EAP_ATTRIBUTE_TYPE_eatLoginLATNode: EAP_ATTRIBUTE_TYPE = 35
EAP_ATTRIBUTE_TYPE_eatLoginLATGroup: EAP_ATTRIBUTE_TYPE = 36
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkLink: EAP_ATTRIBUTE_TYPE = 37
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkNetwork: EAP_ATTRIBUTE_TYPE = 38
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkZone: EAP_ATTRIBUTE_TYPE = 39
EAP_ATTRIBUTE_TYPE_eatAcctStatusType: EAP_ATTRIBUTE_TYPE = 40
EAP_ATTRIBUTE_TYPE_eatAcctDelayTime: EAP_ATTRIBUTE_TYPE = 41
EAP_ATTRIBUTE_TYPE_eatAcctInputOctets: EAP_ATTRIBUTE_TYPE = 42
EAP_ATTRIBUTE_TYPE_eatAcctOutputOctets: EAP_ATTRIBUTE_TYPE = 43
EAP_ATTRIBUTE_TYPE_eatAcctSessionId: EAP_ATTRIBUTE_TYPE = 44
EAP_ATTRIBUTE_TYPE_eatAcctAuthentic: EAP_ATTRIBUTE_TYPE = 45
EAP_ATTRIBUTE_TYPE_eatAcctSessionTime: EAP_ATTRIBUTE_TYPE = 46
EAP_ATTRIBUTE_TYPE_eatAcctInputPackets: EAP_ATTRIBUTE_TYPE = 47
EAP_ATTRIBUTE_TYPE_eatAcctOutputPackets: EAP_ATTRIBUTE_TYPE = 48
EAP_ATTRIBUTE_TYPE_eatAcctTerminateCause: EAP_ATTRIBUTE_TYPE = 49
EAP_ATTRIBUTE_TYPE_eatAcctMultiSessionId: EAP_ATTRIBUTE_TYPE = 50
EAP_ATTRIBUTE_TYPE_eatAcctLinkCount: EAP_ATTRIBUTE_TYPE = 51
EAP_ATTRIBUTE_TYPE_eatAcctEventTimeStamp: EAP_ATTRIBUTE_TYPE = 55
EAP_ATTRIBUTE_TYPE_eatMD5CHAPChallenge: EAP_ATTRIBUTE_TYPE = 60
EAP_ATTRIBUTE_TYPE_eatNASPortType: EAP_ATTRIBUTE_TYPE = 61
EAP_ATTRIBUTE_TYPE_eatPortLimit: EAP_ATTRIBUTE_TYPE = 62
EAP_ATTRIBUTE_TYPE_eatLoginLATPort: EAP_ATTRIBUTE_TYPE = 63
EAP_ATTRIBUTE_TYPE_eatTunnelType: EAP_ATTRIBUTE_TYPE = 64
EAP_ATTRIBUTE_TYPE_eatTunnelMediumType: EAP_ATTRIBUTE_TYPE = 65
EAP_ATTRIBUTE_TYPE_eatTunnelClientEndpoint: EAP_ATTRIBUTE_TYPE = 66
EAP_ATTRIBUTE_TYPE_eatTunnelServerEndpoint: EAP_ATTRIBUTE_TYPE = 67
EAP_ATTRIBUTE_TYPE_eatARAPPassword: EAP_ATTRIBUTE_TYPE = 70
EAP_ATTRIBUTE_TYPE_eatARAPFeatures: EAP_ATTRIBUTE_TYPE = 71
EAP_ATTRIBUTE_TYPE_eatARAPZoneAccess: EAP_ATTRIBUTE_TYPE = 72
EAP_ATTRIBUTE_TYPE_eatARAPSecurity: EAP_ATTRIBUTE_TYPE = 73
EAP_ATTRIBUTE_TYPE_eatARAPSecurityData: EAP_ATTRIBUTE_TYPE = 74
EAP_ATTRIBUTE_TYPE_eatPasswordRetry: EAP_ATTRIBUTE_TYPE = 75
EAP_ATTRIBUTE_TYPE_eatPrompt: EAP_ATTRIBUTE_TYPE = 76
EAP_ATTRIBUTE_TYPE_eatConnectInfo: EAP_ATTRIBUTE_TYPE = 77
EAP_ATTRIBUTE_TYPE_eatConfigurationToken: EAP_ATTRIBUTE_TYPE = 78
EAP_ATTRIBUTE_TYPE_eatEAPMessage: EAP_ATTRIBUTE_TYPE = 79
EAP_ATTRIBUTE_TYPE_eatSignature: EAP_ATTRIBUTE_TYPE = 80
EAP_ATTRIBUTE_TYPE_eatARAPChallengeResponse: EAP_ATTRIBUTE_TYPE = 84
EAP_ATTRIBUTE_TYPE_eatAcctInterimInterval: EAP_ATTRIBUTE_TYPE = 85
EAP_ATTRIBUTE_TYPE_eatNASIPv6Address: EAP_ATTRIBUTE_TYPE = 95
EAP_ATTRIBUTE_TYPE_eatFramedInterfaceId: EAP_ATTRIBUTE_TYPE = 96
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Prefix: EAP_ATTRIBUTE_TYPE = 97
EAP_ATTRIBUTE_TYPE_eatLoginIPv6Host: EAP_ATTRIBUTE_TYPE = 98
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Route: EAP_ATTRIBUTE_TYPE = 99
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Pool: EAP_ATTRIBUTE_TYPE = 100
EAP_ATTRIBUTE_TYPE_eatARAPGuestLogon: EAP_ATTRIBUTE_TYPE = 8096
EAP_ATTRIBUTE_TYPE_eatCertificateOID: EAP_ATTRIBUTE_TYPE = 8097
EAP_ATTRIBUTE_TYPE_eatEAPConfiguration: EAP_ATTRIBUTE_TYPE = 8098
EAP_ATTRIBUTE_TYPE_eatPEAPEmbeddedEAPTypeId: EAP_ATTRIBUTE_TYPE = 8099
EAP_ATTRIBUTE_TYPE_eatPEAPFastRoamedSession: EAP_ATTRIBUTE_TYPE = 8100
EAP_ATTRIBUTE_TYPE_eatFastRoamedSession: EAP_ATTRIBUTE_TYPE = 8100
EAP_ATTRIBUTE_TYPE_eatEAPTLV: EAP_ATTRIBUTE_TYPE = 8102
EAP_ATTRIBUTE_TYPE_eatCredentialsChanged: EAP_ATTRIBUTE_TYPE = 8103
EAP_ATTRIBUTE_TYPE_eatInnerEapMethodType: EAP_ATTRIBUTE_TYPE = 8104
EAP_ATTRIBUTE_TYPE_eatClearTextPassword: EAP_ATTRIBUTE_TYPE = 8107
EAP_ATTRIBUTE_TYPE_eatQuarantineSoH: EAP_ATTRIBUTE_TYPE = 8150
EAP_ATTRIBUTE_TYPE_eatCertificateThumbprint: EAP_ATTRIBUTE_TYPE = 8250
EAP_ATTRIBUTE_TYPE_eatPeerId: EAP_ATTRIBUTE_TYPE = 9000
EAP_ATTRIBUTE_TYPE_eatServerId: EAP_ATTRIBUTE_TYPE = 9001
EAP_ATTRIBUTE_TYPE_eatMethodId: EAP_ATTRIBUTE_TYPE = 9002
EAP_ATTRIBUTE_TYPE_eatEMSK: EAP_ATTRIBUTE_TYPE = 9003
EAP_ATTRIBUTE_TYPE_eatSessionId: EAP_ATTRIBUTE_TYPE = 9004
EAP_ATTRIBUTE_TYPE_eatReserved: EAP_ATTRIBUTE_TYPE = -1
class EAP_AUTHENTICATOR_METHOD_ROUTINES(Structure):
    dwSizeInBytes: UInt32
    pEapType: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head)
    EapMethodAuthenticatorInitialize: IntPtr
    EapMethodAuthenticatorBeginSession: IntPtr
    EapMethodAuthenticatorUpdateInnerMethodParams: IntPtr
    EapMethodAuthenticatorReceivePacket: IntPtr
    EapMethodAuthenticatorSendPacket: IntPtr
    EapMethodAuthenticatorGetAttributes: IntPtr
    EapMethodAuthenticatorSetAttributes: IntPtr
    EapMethodAuthenticatorGetResult: IntPtr
    EapMethodAuthenticatorEndSession: IntPtr
    EapMethodAuthenticatorShutdown: IntPtr
EAP_AUTHENTICATOR_SEND_TIMEOUT = Int32
EAP_AUTHENTICATOR_SEND_TIMEOUT_NONE: EAP_AUTHENTICATOR_SEND_TIMEOUT = 0
EAP_AUTHENTICATOR_SEND_TIMEOUT_BASIC: EAP_AUTHENTICATOR_SEND_TIMEOUT = 1
EAP_AUTHENTICATOR_SEND_TIMEOUT_INTERACTIVE: EAP_AUTHENTICATOR_SEND_TIMEOUT = 2
class EAP_CONFIG_INPUT_FIELD_ARRAY(Structure):
    dwVersion: UInt32
    dwNumberOfFields: UInt32
    pFields: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_DATA_head)
class EAP_CONFIG_INPUT_FIELD_DATA(Structure):
    dwSize: UInt32
    Type: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE
    dwFlagProps: UInt32
    pwszLabel: Windows.Win32.Foundation.PWSTR
    pwszData: Windows.Win32.Foundation.PWSTR
    dwMinDataLength: UInt32
    dwMaxDataLength: UInt32
EAP_CONFIG_INPUT_FIELD_TYPE = Int32
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputUsername: EAP_CONFIG_INPUT_FIELD_TYPE = 0
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPassword: EAP_CONFIG_INPUT_FIELD_TYPE = 1
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkUsername: EAP_CONFIG_INPUT_FIELD_TYPE = 2
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkPassword: EAP_CONFIG_INPUT_FIELD_TYPE = 3
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPin: EAP_CONFIG_INPUT_FIELD_TYPE = 4
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPSK: EAP_CONFIG_INPUT_FIELD_TYPE = 5
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputEdit: EAP_CONFIG_INPUT_FIELD_TYPE = 6
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardUsername: EAP_CONFIG_INPUT_FIELD_TYPE = 7
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardError: EAP_CONFIG_INPUT_FIELD_TYPE = 8
class EAP_CRED_EXPIRY_REQ(Structure):
    curCreds: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
    newCreds: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
class EAP_ERROR(Structure):
    dwWinError: UInt32
    type: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    dwReasonCode: UInt32
    rootCauseGuid: Guid
    repairGuid: Guid
    helpLinkGuid: Guid
    pRootCauseString: Windows.Win32.Foundation.PWSTR
    pRepairString: Windows.Win32.Foundation.PWSTR
class EAP_INTERACTIVE_UI_DATA(Structure):
    dwVersion: UInt32
    dwSize: UInt32
    dwDataType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE
    cbUiData: UInt32
    pbUiData: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_UI_DATA_FORMAT
EAP_INTERACTIVE_UI_DATA_TYPE = Int32
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredReq: EAP_INTERACTIVE_UI_DATA_TYPE = 0
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredResp: EAP_INTERACTIVE_UI_DATA_TYPE = 1
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryReq: EAP_INTERACTIVE_UI_DATA_TYPE = 2
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryResp: EAP_INTERACTIVE_UI_DATA_TYPE = 3
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonReq: EAP_INTERACTIVE_UI_DATA_TYPE = 4
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonResp: EAP_INTERACTIVE_UI_DATA_TYPE = 5
EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = Int32
EAP_METHOD_AUTHENTICATOR_RESPONSE_DISCARD: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 0
EAP_METHOD_AUTHENTICATOR_RESPONSE_SEND: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 1
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESULT: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 2
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESPOND: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 3
EAP_METHOD_AUTHENTICATOR_RESPONSE_AUTHENTICATE: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 4
EAP_METHOD_AUTHENTICATOR_RESPONSE_HANDLE_IDENTITY: EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 5
class EAP_METHOD_AUTHENTICATOR_RESULT(Structure):
    fIsSuccess: Windows.Win32.Foundation.BOOL
    dwFailureReason: UInt32
    pAuthAttribs: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
class EAP_METHOD_INFO(Structure):
    eaptype: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfo: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
class EAP_METHOD_INFO_ARRAY(Structure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
class EAP_METHOD_INFO_ARRAY_EX(Structure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_EX_head)
class EAP_METHOD_INFO_EX(Structure):
    eaptype: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfoArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_EX_head)
class EAP_METHOD_PROPERTY(Structure):
    eapMethodPropertyType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE
    eapMethodPropertyValueType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE
    eapMethodPropertyValue: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE
class EAP_METHOD_PROPERTY_ARRAY(Structure):
    dwNumberOfProperties: UInt32
    pMethodProperty: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_head)
EAP_METHOD_PROPERTY_TYPE = Int32
EAP_METHOD_PROPERTY_TYPE_emptPropCipherSuiteNegotiation: EAP_METHOD_PROPERTY_TYPE = 0
EAP_METHOD_PROPERTY_TYPE_emptPropMutualAuth: EAP_METHOD_PROPERTY_TYPE = 1
EAP_METHOD_PROPERTY_TYPE_emptPropIntegrity: EAP_METHOD_PROPERTY_TYPE = 2
EAP_METHOD_PROPERTY_TYPE_emptPropReplayProtection: EAP_METHOD_PROPERTY_TYPE = 3
EAP_METHOD_PROPERTY_TYPE_emptPropConfidentiality: EAP_METHOD_PROPERTY_TYPE = 4
EAP_METHOD_PROPERTY_TYPE_emptPropKeyDerivation: EAP_METHOD_PROPERTY_TYPE = 5
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength64: EAP_METHOD_PROPERTY_TYPE = 6
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength128: EAP_METHOD_PROPERTY_TYPE = 7
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength256: EAP_METHOD_PROPERTY_TYPE = 8
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength512: EAP_METHOD_PROPERTY_TYPE = 9
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength1024: EAP_METHOD_PROPERTY_TYPE = 10
EAP_METHOD_PROPERTY_TYPE_emptPropDictionaryAttackResistance: EAP_METHOD_PROPERTY_TYPE = 11
EAP_METHOD_PROPERTY_TYPE_emptPropFastReconnect: EAP_METHOD_PROPERTY_TYPE = 12
EAP_METHOD_PROPERTY_TYPE_emptPropCryptoBinding: EAP_METHOD_PROPERTY_TYPE = 13
EAP_METHOD_PROPERTY_TYPE_emptPropSessionIndependence: EAP_METHOD_PROPERTY_TYPE = 14
EAP_METHOD_PROPERTY_TYPE_emptPropFragmentation: EAP_METHOD_PROPERTY_TYPE = 15
EAP_METHOD_PROPERTY_TYPE_emptPropChannelBinding: EAP_METHOD_PROPERTY_TYPE = 16
EAP_METHOD_PROPERTY_TYPE_emptPropNap: EAP_METHOD_PROPERTY_TYPE = 17
EAP_METHOD_PROPERTY_TYPE_emptPropStandalone: EAP_METHOD_PROPERTY_TYPE = 18
EAP_METHOD_PROPERTY_TYPE_emptPropMppeEncryption: EAP_METHOD_PROPERTY_TYPE = 19
EAP_METHOD_PROPERTY_TYPE_emptPropTunnelMethod: EAP_METHOD_PROPERTY_TYPE = 20
EAP_METHOD_PROPERTY_TYPE_emptPropSupportsConfig: EAP_METHOD_PROPERTY_TYPE = 21
EAP_METHOD_PROPERTY_TYPE_emptPropCertifiedMethod: EAP_METHOD_PROPERTY_TYPE = 22
EAP_METHOD_PROPERTY_TYPE_emptPropHiddenMethod: EAP_METHOD_PROPERTY_TYPE = 23
EAP_METHOD_PROPERTY_TYPE_emptPropMachineAuth: EAP_METHOD_PROPERTY_TYPE = 24
EAP_METHOD_PROPERTY_TYPE_emptPropUserAuth: EAP_METHOD_PROPERTY_TYPE = 25
EAP_METHOD_PROPERTY_TYPE_emptPropIdentityPrivacy: EAP_METHOD_PROPERTY_TYPE = 26
EAP_METHOD_PROPERTY_TYPE_emptPropMethodChaining: EAP_METHOD_PROPERTY_TYPE = 27
EAP_METHOD_PROPERTY_TYPE_emptPropSharedStateEquivalence: EAP_METHOD_PROPERTY_TYPE = 28
EAP_METHOD_PROPERTY_TYPE_emptLegacyMethodPropertyFlag: EAP_METHOD_PROPERTY_TYPE = 31
EAP_METHOD_PROPERTY_TYPE_emptPropVendorSpecific: EAP_METHOD_PROPERTY_TYPE = 255
class EAP_METHOD_PROPERTY_VALUE(Union):
    empvBool: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_BOOL
    empvDword: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_DWORD
    empvString: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_STRING
class EAP_METHOD_PROPERTY_VALUE_BOOL(Structure):
    length: UInt32
    value: Windows.Win32.Foundation.BOOL
class EAP_METHOD_PROPERTY_VALUE_DWORD(Structure):
    length: UInt32
    value: UInt32
class EAP_METHOD_PROPERTY_VALUE_STRING(Structure):
    length: UInt32
    value: c_char_p_no
EAP_METHOD_PROPERTY_VALUE_TYPE = Int32
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtBool: EAP_METHOD_PROPERTY_VALUE_TYPE = 0
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtDword: EAP_METHOD_PROPERTY_VALUE_TYPE = 1
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtString: EAP_METHOD_PROPERTY_VALUE_TYPE = 2
class EAP_METHOD_TYPE(Structure):
    eapType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE
    dwAuthorId: UInt32
class EAP_PEER_METHOD_ROUTINES(Structure):
    dwVersion: UInt32
    pEapType: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE_head)
    EapPeerInitialize: IntPtr
    EapPeerGetIdentity: IntPtr
    EapPeerBeginSession: IntPtr
    EapPeerSetCredentials: IntPtr
    EapPeerProcessRequestPacket: IntPtr
    EapPeerGetResponsePacket: IntPtr
    EapPeerGetResult: IntPtr
    EapPeerGetUIContext: IntPtr
    EapPeerSetUIContext: IntPtr
    EapPeerGetResponseAttributes: IntPtr
    EapPeerSetResponseAttributes: IntPtr
    EapPeerEndSession: IntPtr
    EapPeerShutdown: IntPtr
class EAP_TYPE(Structure):
    type: Byte
    dwVendorId: UInt32
    dwVendorType: UInt32
class EAP_UI_DATA_FORMAT(Union):
    credData: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)
    credExpiryData: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CRED_EXPIRY_REQ_head)
    credLogonData: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)
class EapCertificateCredential(Structure):
    certHash: Byte * 20
    password: Windows.Win32.Foundation.PWSTR
EapCode = Int32
EapCode_EapCodeMinimum: EapCode = 1
EapCode_EapCodeRequest: EapCode = 1
EapCode_EapCodeResponse: EapCode = 2
EapCode_EapCodeSuccess: EapCode = 3
EapCode_EapCodeFailure: EapCode = 4
EapCode_EapCodeMaximum: EapCode = 4
class EapCredential(Structure):
    credType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType
    credData: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialTypeData
EapCredentialType = Int32
EAP_EMPTY_CREDENTIAL: EapCredentialType = 0
EAP_USERNAME_PASSWORD_CREDENTIAL: EapCredentialType = 1
EAP_WINLOGON_CREDENTIAL: EapCredentialType = 2
EAP_CERTIFICATE_CREDENTIAL: EapCredentialType = 3
EAP_SIM_CREDENTIAL: EapCredentialType = 4
class EapCredentialTypeData(Union):
    username_password: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapUsernamePasswordCredential
    certificate: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCertificateCredential
    sim: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapSimCredential
EapHostPeerAuthParams = Int32
EapHostPeerAuthParams_EapHostPeerAuthStatus: EapHostPeerAuthParams = 1
EapHostPeerAuthParams_EapHostPeerIdentity: EapHostPeerAuthParams = 2
EapHostPeerAuthParams_EapHostPeerIdentityExtendedInfo: EapHostPeerAuthParams = 3
EapHostPeerAuthParams_EapHostNapInfo: EapHostPeerAuthParams = 4
class EapHostPeerMethodResult(Structure):
    fIsSuccess: Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: c_char_p_no
    fSaveUserData: Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: c_char_p_no
    pAttribArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
    isolationState: Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE
    pEapMethodInfo: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
    pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
EapHostPeerMethodResultReason = Int32
EapHostPeerMethodResultReason_EapHostPeerMethodResultAltSuccessReceived: EapHostPeerMethodResultReason = 1
EapHostPeerMethodResultReason_EapHostPeerMethodResultTimeout: EapHostPeerMethodResultReason = 2
EapHostPeerMethodResultReason_EapHostPeerMethodResultFromMethod: EapHostPeerMethodResultReason = 3
EapHostPeerResponseAction = Int32
EapHostPeerResponseAction_EapHostPeerResponseDiscard: EapHostPeerResponseAction = 0
EapHostPeerResponseAction_EapHostPeerResponseSend: EapHostPeerResponseAction = 1
EapHostPeerResponseAction_EapHostPeerResponseResult: EapHostPeerResponseAction = 2
EapHostPeerResponseAction_EapHostPeerResponseInvokeUi: EapHostPeerResponseAction = 3
EapHostPeerResponseAction_EapHostPeerResponseRespond: EapHostPeerResponseAction = 4
EapHostPeerResponseAction_EapHostPeerResponseStartAuthentication: EapHostPeerResponseAction = 5
EapHostPeerResponseAction_EapHostPeerResponseNone: EapHostPeerResponseAction = 6
class EapPacket(Structure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class EapPeerMethodOutput(Structure):
    action: Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction
    fAllowNotifications: Windows.Win32.Foundation.BOOL
EapPeerMethodResponseAction = Int32
EapPeerMethodResponseAction_EapPeerMethodResponseActionDiscard: EapPeerMethodResponseAction = 0
EapPeerMethodResponseAction_EapPeerMethodResponseActionSend: EapPeerMethodResponseAction = 1
EapPeerMethodResponseAction_EapPeerMethodResponseActionResult: EapPeerMethodResponseAction = 2
EapPeerMethodResponseAction_EapPeerMethodResponseActionInvokeUI: EapPeerMethodResponseAction = 3
EapPeerMethodResponseAction_EapPeerMethodResponseActionRespond: EapPeerMethodResponseAction = 4
EapPeerMethodResponseAction_EapPeerMethodResponseActionNone: EapPeerMethodResponseAction = 5
class EapPeerMethodResult(Structure):
    fIsSuccess: Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: c_char_p_no
    fSaveUserData: Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: c_char_p_no
    pAttribArray: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
    pEapError: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
    pNgcKerbTicket: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)
    fSaveToCredMan: Windows.Win32.Foundation.BOOL
EapPeerMethodResultReason = Int32
EapPeerMethodResultReason_EapPeerMethodResultUnknown: EapPeerMethodResultReason = 1
EapPeerMethodResultReason_EapPeerMethodResultSuccess: EapPeerMethodResultReason = 2
EapPeerMethodResultReason_EapPeerMethodResultFailure: EapPeerMethodResultReason = 3
class EapSimCredential(Structure):
    iccID: Windows.Win32.Foundation.PWSTR
class EapUsernamePasswordCredential(Structure):
    username: Windows.Win32.Foundation.PWSTR
    password: Windows.Win32.Foundation.PWSTR
class IAccountingProviderConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('66a2db18-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    @commethod(3)
    def Initialize(pszMachineName: Windows.Win32.Foundation.PWSTR, puConnectionParam: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(uConnectionParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(uConnectionParam: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IAuthenticationProviderConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('66a2db17-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    @commethod(3)
    def Initialize(pszMachineName: Windows.Win32.Foundation.PWSTR, puConnectionParam: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(uConnectionParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(uConnectionParam: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('66a2db19-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    @commethod(3)
    def Initialize(pszMachineName: Windows.Win32.Foundation.PWSTR, dwEapTypeId: UInt32, puConnectionParam: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(dwEapTypeId: UInt32, uConnectionParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ServerInvokeConfigUI(dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, uReserved1: UIntPtr, uReserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RouterInvokeConfigUI(dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, pConnectionDataIn: c_char_p_no, dwSizeOfConnectionDataIn: UInt32, ppConnectionDataOut: POINTER(c_char_p_no), pdwSizeOfConnectionDataOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RouterInvokeCredentialsUI(dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, pConnectionDataIn: c_char_p_no, dwSizeOfConnectionDataIn: UInt32, pUserDataIn: c_char_p_no, dwSizeOfUserDataIn: UInt32, ppUserDataOut: POINTER(c_char_p_no), pdwSizeOfUserDataOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig2(c_void_p):
    extends: Windows.Win32.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig
    Guid = Guid('d565917a-85c4-4466-85-6e-67-1c-37-42-ea-9a')
    @commethod(8)
    def ServerInvokeConfigUI2(dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, pConfigDataIn: c_char_p_no, dwSizeOfConfigDataIn: UInt32, ppConfigDataOut: POINTER(c_char_p_no), pdwSizeOfConfigDataOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGlobalConfig(dwEapTypeId: UInt32, ppConfigDataOut: POINTER(c_char_p_no), pdwSizeOfConfigDataOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig3(c_void_p):
    extends: Windows.Win32.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig2
    Guid = Guid('b78ecd12-68bb-4f86-9b-f0-84-38-dd-3b-e9-82')
    @commethod(10)
    def ServerInvokeCertificateConfigUI(dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: Windows.Win32.Foundation.HWND, pConfigDataIn: c_char_p_no, dwSizeOfConfigDataIn: UInt32, ppConfigDataOut: POINTER(c_char_p_no), pdwSizeOfConfigDataOut: POINTER(UInt32), uReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IRouterProtocolConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('66a2db16-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    @commethod(3)
    def AddProtocol(pszMachineName: Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: Windows.Win32.System.Com.IUnknown_head, uReserved1: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveProtocol(pszMachineName: Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: Windows.Win32.System.Com.IUnknown_head, uReserved1: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
ISOLATION_STATE = Int32
ISOLATION_STATE_UNKNOWN: ISOLATION_STATE = 0
ISOLATION_STATE_NOT_RESTRICTED: ISOLATION_STATE = 1
ISOLATION_STATE_IN_PROBATION: ISOLATION_STATE = 2
ISOLATION_STATE_RESTRICTED_ACCESS: ISOLATION_STATE = 3
class LEGACY_IDENTITY_UI_PARAMS(Structure):
    eapType: UInt32
    dwFlags: UInt32
    dwSizeofConnectionData: UInt32
    pConnectionData: c_char_p_no
    dwSizeofUserData: UInt32
    pUserData: c_char_p_no
    dwSizeofUserDataOut: UInt32
    pUserDataOut: c_char_p_no
    pwszIdentity: Windows.Win32.Foundation.PWSTR
    dwError: UInt32
class LEGACY_INTERACTIVE_UI_PARAMS(Structure):
    eapType: UInt32
    dwSizeofContextData: UInt32
    pContextData: c_char_p_no
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: c_char_p_no
    dwError: UInt32
class NgcTicketContext(Structure):
    wszTicket: Char * 45
    hKey: Windows.Win32.Security.Cryptography.NCRYPT_KEY_HANDLE
    hImpersonateToken: Windows.Win32.Foundation.HANDLE
@winfunctype_pointer
def NotificationHandler(connectionId: Guid, pContextData: c_void_p) -> Void: ...
PPP_EAP_ACTION = Int32
EAPACTION_NoAction: PPP_EAP_ACTION = 0
EAPACTION_Authenticate: PPP_EAP_ACTION = 1
EAPACTION_Done: PPP_EAP_ACTION = 2
EAPACTION_SendAndDone: PPP_EAP_ACTION = 3
EAPACTION_Send: PPP_EAP_ACTION = 4
EAPACTION_SendWithTimeout: PPP_EAP_ACTION = 5
EAPACTION_SendWithTimeoutInteractive: PPP_EAP_ACTION = 6
EAPACTION_IndicateTLV: PPP_EAP_ACTION = 7
EAPACTION_IndicateIdentity: PPP_EAP_ACTION = 8
class PPP_EAP_INFO(Structure):
    dwSizeInBytes: UInt32
    dwEapTypeId: UInt32
    RasEapInitialize: IntPtr
    RasEapBegin: IntPtr
    RasEapEnd: IntPtr
    RasEapMakeMessage: IntPtr
class PPP_EAP_INPUT(Structure):
    dwSizeInBytes: UInt32
    fFlags: UInt32
    fAuthenticator: Windows.Win32.Foundation.BOOL
    pwszIdentity: Windows.Win32.Foundation.PWSTR
    pwszPassword: Windows.Win32.Foundation.PWSTR
    bInitialId: Byte
    pUserAttributes: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)
    fAuthenticationComplete: Windows.Win32.Foundation.BOOL
    dwAuthResultCode: UInt32
    hTokenImpersonateUser: Windows.Win32.Foundation.HANDLE
    fSuccessPacketReceived: Windows.Win32.Foundation.BOOL
    fDataReceivedFromInteractiveUI: Windows.Win32.Foundation.BOOL
    pDataFromInteractiveUI: c_char_p_no
    dwSizeOfDataFromInteractiveUI: UInt32
    pConnectionData: c_char_p_no
    dwSizeOfConnectionData: UInt32
    pUserData: c_char_p_no
    dwSizeOfUserData: UInt32
    hReserved: Windows.Win32.Foundation.HANDLE
    guidConnectionId: Guid
    isVpn: Windows.Win32.Foundation.BOOL
class PPP_EAP_OUTPUT(Structure):
    dwSizeInBytes: UInt32
    Action: Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION
    dwAuthResultCode: UInt32
    pUserAttributes: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)
    fInvokeInteractiveUI: Windows.Win32.Foundation.BOOL
    pUIContextData: c_char_p_no
    dwSizeOfUIContextData: UInt32
    fSaveConnectionData: Windows.Win32.Foundation.BOOL
    pConnectionData: c_char_p_no
    dwSizeOfConnectionData: UInt32
    fSaveUserData: Windows.Win32.Foundation.BOOL
    pUserData: c_char_p_no
    dwSizeOfUserData: UInt32
    pNgcKerbTicket: POINTER(Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)
    fSaveToCredMan: Windows.Win32.Foundation.BOOL
class PPP_EAP_PACKET(Structure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class RAS_AUTH_ATTRIBUTE(Structure):
    raaType: Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE
    dwLength: UInt32
    Value: c_void_p
RAS_AUTH_ATTRIBUTE_TYPE = Int32
RAS_AUTH_ATTRIBUTE_TYPE_raatMinimum: RAS_AUTH_ATTRIBUTE_TYPE = 0
RAS_AUTH_ATTRIBUTE_TYPE_raatUserName: RAS_AUTH_ATTRIBUTE_TYPE = 1
RAS_AUTH_ATTRIBUTE_TYPE_raatUserPassword: RAS_AUTH_ATTRIBUTE_TYPE = 2
RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPPassword: RAS_AUTH_ATTRIBUTE_TYPE = 3
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPAddress: RAS_AUTH_ATTRIBUTE_TYPE = 4
RAS_AUTH_ATTRIBUTE_TYPE_raatNASPort: RAS_AUTH_ATTRIBUTE_TYPE = 5
RAS_AUTH_ATTRIBUTE_TYPE_raatServiceType: RAS_AUTH_ATTRIBUTE_TYPE = 6
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedProtocol: RAS_AUTH_ATTRIBUTE_TYPE = 7
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPAddress: RAS_AUTH_ATTRIBUTE_TYPE = 8
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPNetmask: RAS_AUTH_ATTRIBUTE_TYPE = 9
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRouting: RAS_AUTH_ATTRIBUTE_TYPE = 10
RAS_AUTH_ATTRIBUTE_TYPE_raatFilterId: RAS_AUTH_ATTRIBUTE_TYPE = 11
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedMTU: RAS_AUTH_ATTRIBUTE_TYPE = 12
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedCompression: RAS_AUTH_ATTRIBUTE_TYPE = 13
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPHost: RAS_AUTH_ATTRIBUTE_TYPE = 14
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginService: RAS_AUTH_ATTRIBUTE_TYPE = 15
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginTCPPort: RAS_AUTH_ATTRIBUTE_TYPE = 16
RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned17: RAS_AUTH_ATTRIBUTE_TYPE = 17
RAS_AUTH_ATTRIBUTE_TYPE_raatReplyMessage: RAS_AUTH_ATTRIBUTE_TYPE = 18
RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackNumber: RAS_AUTH_ATTRIBUTE_TYPE = 19
RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackId: RAS_AUTH_ATTRIBUTE_TYPE = 20
RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned21: RAS_AUTH_ATTRIBUTE_TYPE = 21
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRoute: RAS_AUTH_ATTRIBUTE_TYPE = 22
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPXNetwork: RAS_AUTH_ATTRIBUTE_TYPE = 23
RAS_AUTH_ATTRIBUTE_TYPE_raatState: RAS_AUTH_ATTRIBUTE_TYPE = 24
RAS_AUTH_ATTRIBUTE_TYPE_raatClass: RAS_AUTH_ATTRIBUTE_TYPE = 25
RAS_AUTH_ATTRIBUTE_TYPE_raatVendorSpecific: RAS_AUTH_ATTRIBUTE_TYPE = 26
RAS_AUTH_ATTRIBUTE_TYPE_raatSessionTimeout: RAS_AUTH_ATTRIBUTE_TYPE = 27
RAS_AUTH_ATTRIBUTE_TYPE_raatIdleTimeout: RAS_AUTH_ATTRIBUTE_TYPE = 28
RAS_AUTH_ATTRIBUTE_TYPE_raatTerminationAction: RAS_AUTH_ATTRIBUTE_TYPE = 29
RAS_AUTH_ATTRIBUTE_TYPE_raatCalledStationId: RAS_AUTH_ATTRIBUTE_TYPE = 30
RAS_AUTH_ATTRIBUTE_TYPE_raatCallingStationId: RAS_AUTH_ATTRIBUTE_TYPE = 31
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIdentifier: RAS_AUTH_ATTRIBUTE_TYPE = 32
RAS_AUTH_ATTRIBUTE_TYPE_raatProxyState: RAS_AUTH_ATTRIBUTE_TYPE = 33
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATService: RAS_AUTH_ATTRIBUTE_TYPE = 34
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATNode: RAS_AUTH_ATTRIBUTE_TYPE = 35
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATGroup: RAS_AUTH_ATTRIBUTE_TYPE = 36
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkLink: RAS_AUTH_ATTRIBUTE_TYPE = 37
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkNetwork: RAS_AUTH_ATTRIBUTE_TYPE = 38
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkZone: RAS_AUTH_ATTRIBUTE_TYPE = 39
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctStatusType: RAS_AUTH_ATTRIBUTE_TYPE = 40
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctDelayTime: RAS_AUTH_ATTRIBUTE_TYPE = 41
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputOctets: RAS_AUTH_ATTRIBUTE_TYPE = 42
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputOctets: RAS_AUTH_ATTRIBUTE_TYPE = 43
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionId: RAS_AUTH_ATTRIBUTE_TYPE = 44
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctAuthentic: RAS_AUTH_ATTRIBUTE_TYPE = 45
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionTime: RAS_AUTH_ATTRIBUTE_TYPE = 46
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputPackets: RAS_AUTH_ATTRIBUTE_TYPE = 47
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputPackets: RAS_AUTH_ATTRIBUTE_TYPE = 48
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctTerminateCause: RAS_AUTH_ATTRIBUTE_TYPE = 49
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctMultiSessionId: RAS_AUTH_ATTRIBUTE_TYPE = 50
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctLinkCount: RAS_AUTH_ATTRIBUTE_TYPE = 51
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctEventTimeStamp: RAS_AUTH_ATTRIBUTE_TYPE = 55
RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPChallenge: RAS_AUTH_ATTRIBUTE_TYPE = 60
RAS_AUTH_ATTRIBUTE_TYPE_raatNASPortType: RAS_AUTH_ATTRIBUTE_TYPE = 61
RAS_AUTH_ATTRIBUTE_TYPE_raatPortLimit: RAS_AUTH_ATTRIBUTE_TYPE = 62
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATPort: RAS_AUTH_ATTRIBUTE_TYPE = 63
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelType: RAS_AUTH_ATTRIBUTE_TYPE = 64
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelMediumType: RAS_AUTH_ATTRIBUTE_TYPE = 65
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelClientEndpoint: RAS_AUTH_ATTRIBUTE_TYPE = 66
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelServerEndpoint: RAS_AUTH_ATTRIBUTE_TYPE = 67
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPPassword: RAS_AUTH_ATTRIBUTE_TYPE = 70
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPFeatures: RAS_AUTH_ATTRIBUTE_TYPE = 71
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPZoneAccess: RAS_AUTH_ATTRIBUTE_TYPE = 72
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurity: RAS_AUTH_ATTRIBUTE_TYPE = 73
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurityData: RAS_AUTH_ATTRIBUTE_TYPE = 74
RAS_AUTH_ATTRIBUTE_TYPE_raatPasswordRetry: RAS_AUTH_ATTRIBUTE_TYPE = 75
RAS_AUTH_ATTRIBUTE_TYPE_raatPrompt: RAS_AUTH_ATTRIBUTE_TYPE = 76
RAS_AUTH_ATTRIBUTE_TYPE_raatConnectInfo: RAS_AUTH_ATTRIBUTE_TYPE = 77
RAS_AUTH_ATTRIBUTE_TYPE_raatConfigurationToken: RAS_AUTH_ATTRIBUTE_TYPE = 78
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPMessage: RAS_AUTH_ATTRIBUTE_TYPE = 79
RAS_AUTH_ATTRIBUTE_TYPE_raatSignature: RAS_AUTH_ATTRIBUTE_TYPE = 80
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPChallengeResponse: RAS_AUTH_ATTRIBUTE_TYPE = 84
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInterimInterval: RAS_AUTH_ATTRIBUTE_TYPE = 85
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPv6Address: RAS_AUTH_ATTRIBUTE_TYPE = 95
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedInterfaceId: RAS_AUTH_ATTRIBUTE_TYPE = 96
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Prefix: RAS_AUTH_ATTRIBUTE_TYPE = 97
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPv6Host: RAS_AUTH_ATTRIBUTE_TYPE = 98
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Route: RAS_AUTH_ATTRIBUTE_TYPE = 99
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Pool: RAS_AUTH_ATTRIBUTE_TYPE = 100
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPGuestLogon: RAS_AUTH_ATTRIBUTE_TYPE = 8096
RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateOID: RAS_AUTH_ATTRIBUTE_TYPE = 8097
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPConfiguration: RAS_AUTH_ATTRIBUTE_TYPE = 8098
RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPEmbeddedEAPTypeId: RAS_AUTH_ATTRIBUTE_TYPE = 8099
RAS_AUTH_ATTRIBUTE_TYPE_raatInnerEAPTypeId: RAS_AUTH_ATTRIBUTE_TYPE = 8099
RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPFastRoamedSession: RAS_AUTH_ATTRIBUTE_TYPE = 8100
RAS_AUTH_ATTRIBUTE_TYPE_raatFastRoamedSession: RAS_AUTH_ATTRIBUTE_TYPE = 8100
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPTLV: RAS_AUTH_ATTRIBUTE_TYPE = 8102
RAS_AUTH_ATTRIBUTE_TYPE_raatCredentialsChanged: RAS_AUTH_ATTRIBUTE_TYPE = 8103
RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateThumbprint: RAS_AUTH_ATTRIBUTE_TYPE = 8250
RAS_AUTH_ATTRIBUTE_TYPE_raatPeerId: RAS_AUTH_ATTRIBUTE_TYPE = 9000
RAS_AUTH_ATTRIBUTE_TYPE_raatServerId: RAS_AUTH_ATTRIBUTE_TYPE = 9001
RAS_AUTH_ATTRIBUTE_TYPE_raatMethodId: RAS_AUTH_ATTRIBUTE_TYPE = 9002
RAS_AUTH_ATTRIBUTE_TYPE_raatEMSK: RAS_AUTH_ATTRIBUTE_TYPE = 9003
RAS_AUTH_ATTRIBUTE_TYPE_raatSessionId: RAS_AUTH_ATTRIBUTE_TYPE = 9004
RAS_AUTH_ATTRIBUTE_TYPE_raatReserved: RAS_AUTH_ATTRIBUTE_TYPE = -1
make_head(_module, 'EAPHOST_AUTH_INFO')
make_head(_module, 'EAPHOST_IDENTITY_UI_PARAMS')
make_head(_module, 'EAPHOST_INTERACTIVE_UI_PARAMS')
make_head(_module, 'EAP_ATTRIBUTE')
make_head(_module, 'EAP_ATTRIBUTES')
make_head(_module, 'EAP_AUTHENTICATOR_METHOD_ROUTINES')
make_head(_module, 'EAP_CONFIG_INPUT_FIELD_ARRAY')
make_head(_module, 'EAP_CONFIG_INPUT_FIELD_DATA')
make_head(_module, 'EAP_CRED_EXPIRY_REQ')
make_head(_module, 'EAP_ERROR')
make_head(_module, 'EAP_INTERACTIVE_UI_DATA')
make_head(_module, 'EAP_METHOD_AUTHENTICATOR_RESULT')
make_head(_module, 'EAP_METHOD_INFO')
make_head(_module, 'EAP_METHOD_INFO_ARRAY')
make_head(_module, 'EAP_METHOD_INFO_ARRAY_EX')
make_head(_module, 'EAP_METHOD_INFO_EX')
make_head(_module, 'EAP_METHOD_PROPERTY')
make_head(_module, 'EAP_METHOD_PROPERTY_ARRAY')
make_head(_module, 'EAP_METHOD_PROPERTY_VALUE')
make_head(_module, 'EAP_METHOD_PROPERTY_VALUE_BOOL')
make_head(_module, 'EAP_METHOD_PROPERTY_VALUE_DWORD')
make_head(_module, 'EAP_METHOD_PROPERTY_VALUE_STRING')
make_head(_module, 'EAP_METHOD_TYPE')
make_head(_module, 'EAP_PEER_METHOD_ROUTINES')
make_head(_module, 'EAP_TYPE')
make_head(_module, 'EAP_UI_DATA_FORMAT')
make_head(_module, 'EapCertificateCredential')
make_head(_module, 'EapCredential')
make_head(_module, 'EapCredentialTypeData')
make_head(_module, 'EapHostPeerMethodResult')
make_head(_module, 'EapPacket')
make_head(_module, 'EapPeerMethodOutput')
make_head(_module, 'EapPeerMethodResult')
make_head(_module, 'EapSimCredential')
make_head(_module, 'EapUsernamePasswordCredential')
make_head(_module, 'IAccountingProviderConfig')
make_head(_module, 'IAuthenticationProviderConfig')
make_head(_module, 'IEAPProviderConfig')
make_head(_module, 'IEAPProviderConfig2')
make_head(_module, 'IEAPProviderConfig3')
make_head(_module, 'IRouterProtocolConfig')
make_head(_module, 'LEGACY_IDENTITY_UI_PARAMS')
make_head(_module, 'LEGACY_INTERACTIVE_UI_PARAMS')
make_head(_module, 'NgcTicketContext')
make_head(_module, 'NotificationHandler')
make_head(_module, 'PPP_EAP_INFO')
make_head(_module, 'PPP_EAP_INPUT')
make_head(_module, 'PPP_EAP_OUTPUT')
make_head(_module, 'PPP_EAP_PACKET')
make_head(_module, 'RAS_AUTH_ATTRIBUTE')
__all__ = [
    "CERTIFICATE_HASH_LENGTH",
    "EAPACTION_Authenticate",
    "EAPACTION_Done",
    "EAPACTION_IndicateIdentity",
    "EAPACTION_IndicateTLV",
    "EAPACTION_NoAction",
    "EAPACTION_Send",
    "EAPACTION_SendAndDone",
    "EAPACTION_SendWithTimeout",
    "EAPACTION_SendWithTimeoutInteractive",
    "EAPCODE_Failure",
    "EAPCODE_Request",
    "EAPCODE_Response",
    "EAPCODE_Success",
    "EAPHOST_AUTH_INFO",
    "EAPHOST_AUTH_STATUS",
    "EAPHOST_AUTH_STATUS_EapHostAuthFailed",
    "EAPHOST_AUTH_STATUS_EapHostAuthIdentityExchange",
    "EAPHOST_AUTH_STATUS_EapHostAuthInProgress",
    "EAPHOST_AUTH_STATUS_EapHostAuthNegotiatingType",
    "EAPHOST_AUTH_STATUS_EapHostAuthNotStarted",
    "EAPHOST_AUTH_STATUS_EapHostAuthSucceeded",
    "EAPHOST_AUTH_STATUS_EapHostInvalidSession",
    "EAPHOST_IDENTITY_UI_PARAMS",
    "EAPHOST_INTERACTIVE_UI_PARAMS",
    "EAPHOST_METHOD_API_VERSION",
    "EAPHOST_PEER_API_VERSION",
    "EAP_ATTRIBUTE",
    "EAP_ATTRIBUTES",
    "EAP_ATTRIBUTE_TYPE",
    "EAP_ATTRIBUTE_TYPE_eatARAPChallengeResponse",
    "EAP_ATTRIBUTE_TYPE_eatARAPFeatures",
    "EAP_ATTRIBUTE_TYPE_eatARAPGuestLogon",
    "EAP_ATTRIBUTE_TYPE_eatARAPPassword",
    "EAP_ATTRIBUTE_TYPE_eatARAPSecurity",
    "EAP_ATTRIBUTE_TYPE_eatARAPSecurityData",
    "EAP_ATTRIBUTE_TYPE_eatARAPZoneAccess",
    "EAP_ATTRIBUTE_TYPE_eatAcctAuthentic",
    "EAP_ATTRIBUTE_TYPE_eatAcctDelayTime",
    "EAP_ATTRIBUTE_TYPE_eatAcctEventTimeStamp",
    "EAP_ATTRIBUTE_TYPE_eatAcctInputOctets",
    "EAP_ATTRIBUTE_TYPE_eatAcctInputPackets",
    "EAP_ATTRIBUTE_TYPE_eatAcctInterimInterval",
    "EAP_ATTRIBUTE_TYPE_eatAcctLinkCount",
    "EAP_ATTRIBUTE_TYPE_eatAcctMultiSessionId",
    "EAP_ATTRIBUTE_TYPE_eatAcctOutputOctets",
    "EAP_ATTRIBUTE_TYPE_eatAcctOutputPackets",
    "EAP_ATTRIBUTE_TYPE_eatAcctSessionId",
    "EAP_ATTRIBUTE_TYPE_eatAcctSessionTime",
    "EAP_ATTRIBUTE_TYPE_eatAcctStatusType",
    "EAP_ATTRIBUTE_TYPE_eatAcctTerminateCause",
    "EAP_ATTRIBUTE_TYPE_eatCallbackId",
    "EAP_ATTRIBUTE_TYPE_eatCallbackNumber",
    "EAP_ATTRIBUTE_TYPE_eatCalledStationId",
    "EAP_ATTRIBUTE_TYPE_eatCallingStationId",
    "EAP_ATTRIBUTE_TYPE_eatCertificateOID",
    "EAP_ATTRIBUTE_TYPE_eatCertificateThumbprint",
    "EAP_ATTRIBUTE_TYPE_eatClass",
    "EAP_ATTRIBUTE_TYPE_eatClearTextPassword",
    "EAP_ATTRIBUTE_TYPE_eatConfigurationToken",
    "EAP_ATTRIBUTE_TYPE_eatConnectInfo",
    "EAP_ATTRIBUTE_TYPE_eatCredentialsChanged",
    "EAP_ATTRIBUTE_TYPE_eatEAPConfiguration",
    "EAP_ATTRIBUTE_TYPE_eatEAPMessage",
    "EAP_ATTRIBUTE_TYPE_eatEAPTLV",
    "EAP_ATTRIBUTE_TYPE_eatEMSK",
    "EAP_ATTRIBUTE_TYPE_eatFastRoamedSession",
    "EAP_ATTRIBUTE_TYPE_eatFilterId",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkLink",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkNetwork",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkZone",
    "EAP_ATTRIBUTE_TYPE_eatFramedCompression",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPAddress",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPNetmask",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPXNetwork",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Pool",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Prefix",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Route",
    "EAP_ATTRIBUTE_TYPE_eatFramedInterfaceId",
    "EAP_ATTRIBUTE_TYPE_eatFramedMTU",
    "EAP_ATTRIBUTE_TYPE_eatFramedProtocol",
    "EAP_ATTRIBUTE_TYPE_eatFramedRoute",
    "EAP_ATTRIBUTE_TYPE_eatFramedRouting",
    "EAP_ATTRIBUTE_TYPE_eatIdleTimeout",
    "EAP_ATTRIBUTE_TYPE_eatInnerEapMethodType",
    "EAP_ATTRIBUTE_TYPE_eatLoginIPHost",
    "EAP_ATTRIBUTE_TYPE_eatLoginIPv6Host",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATGroup",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATNode",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATPort",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATService",
    "EAP_ATTRIBUTE_TYPE_eatLoginService",
    "EAP_ATTRIBUTE_TYPE_eatLoginTCPPort",
    "EAP_ATTRIBUTE_TYPE_eatMD5CHAPChallenge",
    "EAP_ATTRIBUTE_TYPE_eatMD5CHAPPassword",
    "EAP_ATTRIBUTE_TYPE_eatMethodId",
    "EAP_ATTRIBUTE_TYPE_eatMinimum",
    "EAP_ATTRIBUTE_TYPE_eatNASIPAddress",
    "EAP_ATTRIBUTE_TYPE_eatNASIPv6Address",
    "EAP_ATTRIBUTE_TYPE_eatNASIdentifier",
    "EAP_ATTRIBUTE_TYPE_eatNASPort",
    "EAP_ATTRIBUTE_TYPE_eatNASPortType",
    "EAP_ATTRIBUTE_TYPE_eatPEAPEmbeddedEAPTypeId",
    "EAP_ATTRIBUTE_TYPE_eatPEAPFastRoamedSession",
    "EAP_ATTRIBUTE_TYPE_eatPasswordRetry",
    "EAP_ATTRIBUTE_TYPE_eatPeerId",
    "EAP_ATTRIBUTE_TYPE_eatPortLimit",
    "EAP_ATTRIBUTE_TYPE_eatPrompt",
    "EAP_ATTRIBUTE_TYPE_eatProxyState",
    "EAP_ATTRIBUTE_TYPE_eatQuarantineSoH",
    "EAP_ATTRIBUTE_TYPE_eatReplyMessage",
    "EAP_ATTRIBUTE_TYPE_eatReserved",
    "EAP_ATTRIBUTE_TYPE_eatServerId",
    "EAP_ATTRIBUTE_TYPE_eatServiceType",
    "EAP_ATTRIBUTE_TYPE_eatSessionId",
    "EAP_ATTRIBUTE_TYPE_eatSessionTimeout",
    "EAP_ATTRIBUTE_TYPE_eatSignature",
    "EAP_ATTRIBUTE_TYPE_eatState",
    "EAP_ATTRIBUTE_TYPE_eatTerminationAction",
    "EAP_ATTRIBUTE_TYPE_eatTunnelClientEndpoint",
    "EAP_ATTRIBUTE_TYPE_eatTunnelMediumType",
    "EAP_ATTRIBUTE_TYPE_eatTunnelServerEndpoint",
    "EAP_ATTRIBUTE_TYPE_eatTunnelType",
    "EAP_ATTRIBUTE_TYPE_eatUnassigned17",
    "EAP_ATTRIBUTE_TYPE_eatUnassigned21",
    "EAP_ATTRIBUTE_TYPE_eatUserName",
    "EAP_ATTRIBUTE_TYPE_eatUserPassword",
    "EAP_ATTRIBUTE_TYPE_eatVendorSpecific",
    "EAP_AUTHENTICATOR_METHOD_ROUTINES",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_BASIC",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_INTERACTIVE",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_NONE",
    "EAP_AUTHENTICATOR_VALUENAME_CONFIGUI",
    "EAP_AUTHENTICATOR_VALUENAME_DLL_PATH",
    "EAP_AUTHENTICATOR_VALUENAME_FRIENDLY_NAME",
    "EAP_AUTHENTICATOR_VALUENAME_PROPERTIES",
    "EAP_CERTIFICATE_CREDENTIAL",
    "EAP_CONFIG_INPUT_FIELD_ARRAY",
    "EAP_CONFIG_INPUT_FIELD_DATA",
    "EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT",
    "EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE",
    "EAP_CONFIG_INPUT_FIELD_PROPS_NON_PERSIST",
    "EAP_CONFIG_INPUT_FIELD_TYPE",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputEdit",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkPassword",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkUsername",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPSK",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPassword",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPin",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputUsername",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardError",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardUsername",
    "EAP_CREDENTIAL_VERSION",
    "EAP_CRED_EXPIRY_REQ",
    "EAP_EMPTY_CREDENTIAL",
    "EAP_ERROR",
    "EAP_E_AUTHENTICATION_FAILED",
    "EAP_E_CERT_STORE_INACCESSIBLE",
    "EAP_E_EAPHOST_EAPQEC_INACCESSIBLE",
    "EAP_E_EAPHOST_FIRST",
    "EAP_E_EAPHOST_IDENTITY_UNKNOWN",
    "EAP_E_EAPHOST_LAST",
    "EAP_E_EAPHOST_METHOD_INVALID_PACKET",
    "EAP_E_EAPHOST_METHOD_NOT_INSTALLED",
    "EAP_E_EAPHOST_METHOD_OPERATION_NOT_SUPPORTED",
    "EAP_E_EAPHOST_REMOTE_INVALID_PACKET",
    "EAP_E_EAPHOST_THIRDPARTY_METHOD_HOST_RESET",
    "EAP_E_EAPHOST_XML_MALFORMED",
    "EAP_E_METHOD_CONFIG_DOES_NOT_SUPPORT_SSO",
    "EAP_E_NO_SMART_CARD_READER",
    "EAP_E_SERVER_CERT_EXPIRED",
    "EAP_E_SERVER_CERT_INVALID",
    "EAP_E_SERVER_CERT_NOT_FOUND",
    "EAP_E_SERVER_CERT_OTHER_ERROR",
    "EAP_E_SERVER_CERT_REVOKED",
    "EAP_E_SERVER_FIRST",
    "EAP_E_SERVER_LAST",
    "EAP_E_SERVER_ROOT_CERT_FIRST",
    "EAP_E_SERVER_ROOT_CERT_INVALID",
    "EAP_E_SERVER_ROOT_CERT_LAST",
    "EAP_E_SERVER_ROOT_CERT_NAME_REQUIRED",
    "EAP_E_SERVER_ROOT_CERT_NOT_FOUND",
    "EAP_E_SIM_NOT_VALID",
    "EAP_E_USER_CERT_EXPIRED",
    "EAP_E_USER_CERT_INVALID",
    "EAP_E_USER_CERT_NOT_FOUND",
    "EAP_E_USER_CERT_OTHER_ERROR",
    "EAP_E_USER_CERT_REJECTED",
    "EAP_E_USER_CERT_REVOKED",
    "EAP_E_USER_CREDENTIALS_REJECTED",
    "EAP_E_USER_FIRST",
    "EAP_E_USER_LAST",
    "EAP_E_USER_NAME_PASSWORD_REJECTED",
    "EAP_E_USER_ROOT_CERT_EXPIRED",
    "EAP_E_USER_ROOT_CERT_FIRST",
    "EAP_E_USER_ROOT_CERT_INVALID",
    "EAP_E_USER_ROOT_CERT_LAST",
    "EAP_E_USER_ROOT_CERT_NOT_FOUND",
    "EAP_FLAG_CONFG_READONLY",
    "EAP_FLAG_FULL_AUTH",
    "EAP_FLAG_GUEST_ACCESS",
    "EAP_FLAG_LOGON",
    "EAP_FLAG_MACHINE_AUTH",
    "EAP_FLAG_NON_INTERACTIVE",
    "EAP_FLAG_ONLY_EAP_TLS",
    "EAP_FLAG_PREFER_ALT_CREDENTIALS",
    "EAP_FLAG_PREVIEW",
    "EAP_FLAG_PRE_LOGON",
    "EAP_FLAG_RESUME_FROM_HIBERNATE",
    "EAP_FLAG_Reserved1",
    "EAP_FLAG_Reserved2",
    "EAP_FLAG_Reserved3",
    "EAP_FLAG_Reserved4",
    "EAP_FLAG_Reserved5",
    "EAP_FLAG_Reserved6",
    "EAP_FLAG_Reserved7",
    "EAP_FLAG_Reserved8",
    "EAP_FLAG_Reserved9",
    "EAP_FLAG_SERVER_VALIDATION_REQUIRED",
    "EAP_FLAG_SUPRESS_UI",
    "EAP_FLAG_USER_AUTH",
    "EAP_FLAG_VPN",
    "EAP_GROUP_MASK",
    "EAP_INTERACTIVE_UI_DATA",
    "EAP_INTERACTIVE_UI_DATA_TYPE",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryResp",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonResp",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredResp",
    "EAP_INTERACTIVE_UI_DATA_VERSION",
    "EAP_INVALID_PACKET",
    "EAP_I_EAPHOST_EAP_NEGOTIATION_FAILED",
    "EAP_I_EAPHOST_FIRST",
    "EAP_I_EAPHOST_LAST",
    "EAP_I_USER_ACCOUNT_OTHER_ERROR",
    "EAP_I_USER_FIRST",
    "EAP_I_USER_LAST",
    "EAP_METHOD_AUTHENTICATOR_CONFIG_IS_IDENTITY_PRIVACY",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_AUTHENTICATE",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_DISCARD",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_HANDLE_IDENTITY",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_RESPOND",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_RESULT",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_SEND",
    "EAP_METHOD_AUTHENTICATOR_RESULT",
    "EAP_METHOD_INFO",
    "EAP_METHOD_INFO_ARRAY",
    "EAP_METHOD_INFO_ARRAY_EX",
    "EAP_METHOD_INFO_EX",
    "EAP_METHOD_INVALID_PACKET",
    "EAP_METHOD_PROPERTY",
    "EAP_METHOD_PROPERTY_ARRAY",
    "EAP_METHOD_PROPERTY_TYPE",
    "EAP_METHOD_PROPERTY_TYPE_emptLegacyMethodPropertyFlag",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCertifiedMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropChannelBinding",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCipherSuiteNegotiation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropConfidentiality",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCryptoBinding",
    "EAP_METHOD_PROPERTY_TYPE_emptPropDictionaryAttackResistance",
    "EAP_METHOD_PROPERTY_TYPE_emptPropFastReconnect",
    "EAP_METHOD_PROPERTY_TYPE_emptPropFragmentation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropHiddenMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropIdentityPrivacy",
    "EAP_METHOD_PROPERTY_TYPE_emptPropIntegrity",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyDerivation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength1024",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength128",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength256",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength512",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength64",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMachineAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMethodChaining",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMppeEncryption",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMutualAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropNap",
    "EAP_METHOD_PROPERTY_TYPE_emptPropReplayProtection",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSessionIndependence",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSharedStateEquivalence",
    "EAP_METHOD_PROPERTY_TYPE_emptPropStandalone",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSupportsConfig",
    "EAP_METHOD_PROPERTY_TYPE_emptPropTunnelMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropUserAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropVendorSpecific",
    "EAP_METHOD_PROPERTY_VALUE",
    "EAP_METHOD_PROPERTY_VALUE_BOOL",
    "EAP_METHOD_PROPERTY_VALUE_DWORD",
    "EAP_METHOD_PROPERTY_VALUE_STRING",
    "EAP_METHOD_PROPERTY_VALUE_TYPE",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtBool",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtDword",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtString",
    "EAP_METHOD_TYPE",
    "EAP_PEER_FLAG_GUEST_ACCESS",
    "EAP_PEER_FLAG_HEALTH_STATE_CHANGE",
    "EAP_PEER_METHOD_ROUTINES",
    "EAP_PEER_VALUENAME_CONFIGUI",
    "EAP_PEER_VALUENAME_DLL_PATH",
    "EAP_PEER_VALUENAME_FRIENDLY_NAME",
    "EAP_PEER_VALUENAME_IDENTITY",
    "EAP_PEER_VALUENAME_INTERACTIVEUI",
    "EAP_PEER_VALUENAME_INVOKE_NAMEDLG",
    "EAP_PEER_VALUENAME_INVOKE_PWDDLG",
    "EAP_PEER_VALUENAME_PROPERTIES",
    "EAP_PEER_VALUENAME_REQUIRE_CONFIGUI",
    "EAP_REGISTRY_LOCATION",
    "EAP_SIM_CREDENTIAL",
    "EAP_TYPE",
    "EAP_UI_DATA_FORMAT",
    "EAP_UI_INPUT_FIELD_PROPS_DEFAULT",
    "EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE",
    "EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST",
    "EAP_UI_INPUT_FIELD_PROPS_READ_ONLY",
    "EAP_USERNAME_PASSWORD_CREDENTIAL",
    "EAP_VALUENAME_PROPERTIES",
    "EAP_WINLOGON_CREDENTIAL",
    "EapCertificateCredential",
    "EapCode",
    "EapCode_EapCodeFailure",
    "EapCode_EapCodeMaximum",
    "EapCode_EapCodeMinimum",
    "EapCode_EapCodeRequest",
    "EapCode_EapCodeResponse",
    "EapCode_EapCodeSuccess",
    "EapCredential",
    "EapCredentialType",
    "EapCredentialTypeData",
    "EapHostPeerAuthParams",
    "EapHostPeerAuthParams_EapHostNapInfo",
    "EapHostPeerAuthParams_EapHostPeerAuthStatus",
    "EapHostPeerAuthParams_EapHostPeerIdentity",
    "EapHostPeerAuthParams_EapHostPeerIdentityExtendedInfo",
    "EapHostPeerBeginSession",
    "EapHostPeerClearConnection",
    "EapHostPeerConfigBlob2Xml",
    "EapHostPeerConfigXml2Blob",
    "EapHostPeerCredentialsXml2Blob",
    "EapHostPeerEndSession",
    "EapHostPeerFreeEapError",
    "EapHostPeerFreeErrorMemory",
    "EapHostPeerFreeMemory",
    "EapHostPeerFreeRuntimeMemory",
    "EapHostPeerGetAuthStatus",
    "EapHostPeerGetDataToUnplumbCredentials",
    "EapHostPeerGetEncryptedPassword",
    "EapHostPeerGetIdentity",
    "EapHostPeerGetMethodProperties",
    "EapHostPeerGetMethods",
    "EapHostPeerGetResponseAttributes",
    "EapHostPeerGetResult",
    "EapHostPeerGetSendPacket",
    "EapHostPeerGetUIContext",
    "EapHostPeerInitialize",
    "EapHostPeerInvokeConfigUI",
    "EapHostPeerInvokeIdentityUI",
    "EapHostPeerInvokeInteractiveUI",
    "EapHostPeerMethodResult",
    "EapHostPeerMethodResultReason",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultAltSuccessReceived",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultFromMethod",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultTimeout",
    "EapHostPeerProcessReceivedPacket",
    "EapHostPeerQueryCredentialInputFields",
    "EapHostPeerQueryInteractiveUIInputFields",
    "EapHostPeerQueryUIBlobFromInteractiveUIInputFields",
    "EapHostPeerQueryUserBlobFromCredentialInputFields",
    "EapHostPeerResponseAction",
    "EapHostPeerResponseAction_EapHostPeerResponseDiscard",
    "EapHostPeerResponseAction_EapHostPeerResponseInvokeUi",
    "EapHostPeerResponseAction_EapHostPeerResponseNone",
    "EapHostPeerResponseAction_EapHostPeerResponseRespond",
    "EapHostPeerResponseAction_EapHostPeerResponseResult",
    "EapHostPeerResponseAction_EapHostPeerResponseSend",
    "EapHostPeerResponseAction_EapHostPeerResponseStartAuthentication",
    "EapHostPeerSetResponseAttributes",
    "EapHostPeerSetUIContext",
    "EapHostPeerUninitialize",
    "EapPacket",
    "EapPeerMethodOutput",
    "EapPeerMethodResponseAction",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionDiscard",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionInvokeUI",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionNone",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionRespond",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionResult",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionSend",
    "EapPeerMethodResult",
    "EapPeerMethodResultReason",
    "EapPeerMethodResultReason_EapPeerMethodResultFailure",
    "EapPeerMethodResultReason_EapPeerMethodResultSuccess",
    "EapPeerMethodResultReason_EapPeerMethodResultUnknown",
    "EapSimCredential",
    "EapUsernamePasswordCredential",
    "FACILITY_EAP_MESSAGE",
    "GUID_EapHost_Cause_CertStoreInaccessible",
    "GUID_EapHost_Cause_EapNegotiationFailed",
    "GUID_EapHost_Cause_EapQecInaccessible",
    "GUID_EapHost_Cause_Generic_AuthFailure",
    "GUID_EapHost_Cause_IdentityUnknown",
    "GUID_EapHost_Cause_MethodDLLNotFound",
    "GUID_EapHost_Cause_MethodDoesNotSupportOperation",
    "GUID_EapHost_Cause_Method_Config_Does_Not_Support_Sso",
    "GUID_EapHost_Cause_No_SmartCardReader_Found",
    "GUID_EapHost_Cause_Server_CertExpired",
    "GUID_EapHost_Cause_Server_CertInvalid",
    "GUID_EapHost_Cause_Server_CertNotFound",
    "GUID_EapHost_Cause_Server_CertOtherError",
    "GUID_EapHost_Cause_Server_CertRevoked",
    "GUID_EapHost_Cause_Server_Root_CertNameRequired",
    "GUID_EapHost_Cause_Server_Root_CertNotFound",
    "GUID_EapHost_Cause_SimNotValid",
    "GUID_EapHost_Cause_ThirdPartyMethod_Host_Reset",
    "GUID_EapHost_Cause_User_Account_OtherProblem",
    "GUID_EapHost_Cause_User_CertExpired",
    "GUID_EapHost_Cause_User_CertInvalid",
    "GUID_EapHost_Cause_User_CertNotFound",
    "GUID_EapHost_Cause_User_CertOtherError",
    "GUID_EapHost_Cause_User_CertRejected",
    "GUID_EapHost_Cause_User_CertRevoked",
    "GUID_EapHost_Cause_User_CredsRejected",
    "GUID_EapHost_Cause_User_Root_CertExpired",
    "GUID_EapHost_Cause_User_Root_CertInvalid",
    "GUID_EapHost_Cause_User_Root_CertNotFound",
    "GUID_EapHost_Cause_XmlMalformed",
    "GUID_EapHost_Default",
    "GUID_EapHost_Help_ObtainingCerts",
    "GUID_EapHost_Help_Troubleshooting",
    "GUID_EapHost_Repair_ContactAdmin_AuthFailure",
    "GUID_EapHost_Repair_ContactAdmin_CertNameAbsent",
    "GUID_EapHost_Repair_ContactAdmin_CertStoreInaccessible",
    "GUID_EapHost_Repair_ContactAdmin_IdentityUnknown",
    "GUID_EapHost_Repair_ContactAdmin_InvalidUserAccount",
    "GUID_EapHost_Repair_ContactAdmin_InvalidUserCert",
    "GUID_EapHost_Repair_ContactAdmin_MethodNotFound",
    "GUID_EapHost_Repair_ContactAdmin_NegotiationFailed",
    "GUID_EapHost_Repair_ContactAdmin_NoSmartCardReader",
    "GUID_EapHost_Repair_ContactAdmin_RootCertInvalid",
    "GUID_EapHost_Repair_ContactAdmin_RootCertNotFound",
    "GUID_EapHost_Repair_ContactAdmin_RootExpired",
    "GUID_EapHost_Repair_ContactSysadmin",
    "GUID_EapHost_Repair_Method_Not_Support_Sso",
    "GUID_EapHost_Repair_No_ValidSim_Found",
    "GUID_EapHost_Repair_RestartNap",
    "GUID_EapHost_Repair_Retry_Authentication",
    "GUID_EapHost_Repair_Server_ClientSelectServerCert",
    "GUID_EapHost_Repair_User_AuthFailure",
    "GUID_EapHost_Repair_User_GetNewCert",
    "GUID_EapHost_Repair_User_SelectValidCert",
    "IAccountingProviderConfig",
    "IAuthenticationProviderConfig",
    "IEAPProviderConfig",
    "IEAPProviderConfig2",
    "IEAPProviderConfig3",
    "IRouterProtocolConfig",
    "ISOLATION_STATE",
    "ISOLATION_STATE_IN_PROBATION",
    "ISOLATION_STATE_NOT_RESTRICTED",
    "ISOLATION_STATE_RESTRICTED_ACCESS",
    "ISOLATION_STATE_UNKNOWN",
    "LEGACY_IDENTITY_UI_PARAMS",
    "LEGACY_INTERACTIVE_UI_PARAMS",
    "MAXEAPCODE",
    "MAX_EAP_CONFIG_INPUT_FIELD_LENGTH",
    "MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH",
    "NCRYPT_PIN_CACHE_PIN_BYTE_LENGTH",
    "NgcTicketContext",
    "NotificationHandler",
    "PPP_EAP_ACTION",
    "PPP_EAP_INFO",
    "PPP_EAP_INPUT",
    "PPP_EAP_OUTPUT",
    "PPP_EAP_PACKET",
    "RAS_AUTH_ATTRIBUTE",
    "RAS_AUTH_ATTRIBUTE_TYPE",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPChallengeResponse",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPFeatures",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPGuestLogon",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurity",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurityData",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPZoneAccess",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctAuthentic",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctDelayTime",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctEventTimeStamp",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputOctets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputPackets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInterimInterval",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctLinkCount",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctMultiSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputOctets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputPackets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionTime",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctStatusType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctTerminateCause",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackNumber",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCalledStationId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallingStationId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateOID",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateThumbprint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatClass",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatConfigurationToken",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatConnectInfo",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCredentialsChanged",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPConfiguration",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPMessage",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPTLV",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEMSK",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFastRoamedSession",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFilterId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkLink",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkNetwork",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkZone",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedCompression",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPAddress",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPNetmask",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPXNetwork",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Pool",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Prefix",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Route",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedInterfaceId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedMTU",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedProtocol",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRoute",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRouting",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatIdleTimeout",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatInnerEAPTypeId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPHost",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPv6Host",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATGroup",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATNode",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATService",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginService",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginTCPPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPChallenge",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMethodId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMinimum",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPAddress",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPv6Address",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIdentifier",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASPortType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPEmbeddedEAPTypeId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPFastRoamedSession",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPasswordRetry",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPeerId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPortLimit",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPrompt",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatProxyState",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatReplyMessage",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatReserved",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatServerId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatServiceType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSessionTimeout",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSignature",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatState",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTerminationAction",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelClientEndpoint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelMediumType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelServerEndpoint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned17",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned21",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUserName",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUserPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatVendorSpecific",
    "RAS_EAP_FLAG_8021X_AUTH",
    "RAS_EAP_FLAG_ALTERNATIVE_USER_DB",
    "RAS_EAP_FLAG_CONFG_READONLY",
    "RAS_EAP_FLAG_FIRST_LINK",
    "RAS_EAP_FLAG_GUEST_ACCESS",
    "RAS_EAP_FLAG_HOSTED_IN_PEAP",
    "RAS_EAP_FLAG_LOGON",
    "RAS_EAP_FLAG_MACHINE_AUTH",
    "RAS_EAP_FLAG_NON_INTERACTIVE",
    "RAS_EAP_FLAG_PEAP_FORCE_FULL_AUTH",
    "RAS_EAP_FLAG_PEAP_UPFRONT",
    "RAS_EAP_FLAG_PREVIEW",
    "RAS_EAP_FLAG_PRE_LOGON",
    "RAS_EAP_FLAG_RESERVED",
    "RAS_EAP_FLAG_RESUME_FROM_HIBERNATE",
    "RAS_EAP_FLAG_ROUTER",
    "RAS_EAP_FLAG_SAVE_CREDMAN",
    "RAS_EAP_FLAG_SERVER_VALIDATION_REQUIRED",
    "RAS_EAP_REGISTRY_LOCATION",
    "RAS_EAP_ROLE_AUTHENTICATEE",
    "RAS_EAP_ROLE_AUTHENTICATOR",
    "RAS_EAP_ROLE_EXCLUDE_IN_EAP",
    "RAS_EAP_ROLE_EXCLUDE_IN_PEAP",
    "RAS_EAP_ROLE_EXCLUDE_IN_VPN",
    "RAS_EAP_VALUENAME_CONFIGUI",
    "RAS_EAP_VALUENAME_CONFIG_CLSID",
    "RAS_EAP_VALUENAME_DEFAULT_DATA",
    "RAS_EAP_VALUENAME_ENCRYPTION",
    "RAS_EAP_VALUENAME_FILTER_INNERMETHODS",
    "RAS_EAP_VALUENAME_FRIENDLY_NAME",
    "RAS_EAP_VALUENAME_IDENTITY",
    "RAS_EAP_VALUENAME_INTERACTIVEUI",
    "RAS_EAP_VALUENAME_INVOKE_NAMEDLG",
    "RAS_EAP_VALUENAME_INVOKE_PWDDLG",
    "RAS_EAP_VALUENAME_ISTUNNEL_METHOD",
    "RAS_EAP_VALUENAME_PATH",
    "RAS_EAP_VALUENAME_PER_POLICY_CONFIG",
    "RAS_EAP_VALUENAME_REQUIRE_CONFIGUI",
    "RAS_EAP_VALUENAME_ROLES_SUPPORTED",
    "RAS_EAP_VALUENAME_STANDALONE_SUPPORTED",
    "eapPropCertifiedMethod",
    "eapPropChannelBinding",
    "eapPropCipherSuiteNegotiation",
    "eapPropConfidentiality",
    "eapPropCryptoBinding",
    "eapPropDictionaryAttackResistance",
    "eapPropFastReconnect",
    "eapPropFragmentation",
    "eapPropHiddenMethod",
    "eapPropIdentityPrivacy",
    "eapPropIntegrity",
    "eapPropKeyDerivation",
    "eapPropKeyStrength1024",
    "eapPropKeyStrength128",
    "eapPropKeyStrength256",
    "eapPropKeyStrength512",
    "eapPropKeyStrength64",
    "eapPropMachineAuth",
    "eapPropMethodChaining",
    "eapPropMppeEncryption",
    "eapPropMutualAuth",
    "eapPropNap",
    "eapPropReplayProtection",
    "eapPropReserved",
    "eapPropSessionIndependence",
    "eapPropSharedStateEquivalence",
    "eapPropStandalone",
    "eapPropSupportsConfig",
    "eapPropTunnelMethod",
    "eapPropUserAuth",
    "raatARAPChallenge",
    "raatARAPNewPassword",
    "raatARAPOldPassword",
    "raatARAPPasswordChangeReason",
]
_arch_optional = [
]
