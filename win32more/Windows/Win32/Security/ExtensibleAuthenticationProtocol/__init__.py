from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol
import win32more.Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
GUID_EapHost_Default: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
GUID_EapHost_Cause_MethodDLLNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000001}')
GUID_EapHost_Repair_ContactSysadmin: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000002}')
GUID_EapHost_Cause_CertStoreInaccessible: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000004}')
GUID_EapHost_Cause_Generic_AuthFailure: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000104}')
GUID_EapHost_Cause_IdentityUnknown: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000204}')
GUID_EapHost_Cause_SimNotValid: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000304}')
GUID_EapHost_Cause_Server_CertExpired: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000005}')
GUID_EapHost_Cause_Server_CertInvalid: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000006}')
GUID_EapHost_Cause_Server_CertNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000007}')
GUID_EapHost_Cause_Server_CertRevoked: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000008}')
GUID_EapHost_Cause_Server_CertOtherError: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000108}')
GUID_EapHost_Cause_User_CertExpired: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000009}')
GUID_EapHost_Cause_User_CertInvalid: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000a}')
GUID_EapHost_Cause_User_CertNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000b}')
GUID_EapHost_Cause_User_CertOtherError: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000c}')
GUID_EapHost_Cause_User_CertRejected: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000d}')
GUID_EapHost_Cause_User_CertRevoked: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000e}')
GUID_EapHost_Cause_User_Account_OtherProblem: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000010e}')
GUID_EapHost_Cause_User_CredsRejected: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000020e}')
GUID_EapHost_Cause_User_Root_CertExpired: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000000f}')
GUID_EapHost_Cause_User_Root_CertInvalid: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000010}')
GUID_EapHost_Cause_User_Root_CertNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000011}')
GUID_EapHost_Cause_Server_Root_CertNameRequired: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000012}')
GUID_EapHost_Cause_Server_Root_CertNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000112}')
GUID_EapHost_Cause_ThirdPartyMethod_Host_Reset: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000212}')
GUID_EapHost_Cause_EapQecInaccessible: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000312}')
GUID_EapHost_Repair_Server_ClientSelectServerCert: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000018}')
GUID_EapHost_Repair_User_AuthFailure: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000019}')
GUID_EapHost_Repair_User_GetNewCert: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001a}')
GUID_EapHost_Repair_User_SelectValidCert: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001b}')
GUID_EapHost_Repair_Retry_Authentication: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000011b}')
GUID_EapHost_Cause_EapNegotiationFailed: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001c}')
GUID_EapHost_Cause_XmlMalformed: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001d}')
GUID_EapHost_Cause_MethodDoesNotSupportOperation: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001e}')
GUID_EapHost_Repair_ContactAdmin_AuthFailure: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000001f}')
GUID_EapHost_Repair_ContactAdmin_IdentityUnknown: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000020}')
GUID_EapHost_Repair_ContactAdmin_NegotiationFailed: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000021}')
GUID_EapHost_Repair_ContactAdmin_MethodNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000022}')
GUID_EapHost_Repair_RestartNap: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000023}')
GUID_EapHost_Repair_ContactAdmin_CertStoreInaccessible: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000024}')
GUID_EapHost_Repair_ContactAdmin_InvalidUserAccount: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000025}')
GUID_EapHost_Repair_ContactAdmin_RootCertInvalid: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000026}')
GUID_EapHost_Repair_ContactAdmin_RootCertNotFound: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000027}')
GUID_EapHost_Repair_ContactAdmin_RootExpired: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000028}')
GUID_EapHost_Repair_ContactAdmin_CertNameAbsent: Guid = Guid('{9612fc67-6150-4209-a85e-a8d800000029}')
GUID_EapHost_Repair_ContactAdmin_NoSmartCardReader: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000002a}')
GUID_EapHost_Cause_No_SmartCardReader_Found: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000002b}')
GUID_EapHost_Repair_ContactAdmin_InvalidUserCert: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000002c}')
GUID_EapHost_Repair_Method_Not_Support_Sso: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000002d}')
GUID_EapHost_Repair_No_ValidSim_Found: Guid = Guid('{9612fc67-6150-4209-a85e-a8d80000002e}')
GUID_EapHost_Help_ObtainingCerts: Guid = Guid('{f535eea3-1bdd-46ca-a2fc-a6655939b7e8}')
GUID_EapHost_Help_Troubleshooting: Guid = Guid('{33307acf-0698-41ba-b014-ea0a2eb8d0a8}')
GUID_EapHost_Cause_Method_Config_Does_Not_Support_Sso: Guid = Guid('{da18bd32-004f-41fa-ae08-0bc85e5845ac}')
@winfunctype('eappcfg.dll')
def EapHostPeerGetMethods(pEapMethodInfoArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerGetMethodProperties(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), dwUserDataSize: UInt32, pbUserData: POINTER(Byte), pMethodPropertyArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_ARRAY_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeConfigUI(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryCredentialInputFields(hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), pEapConfigInputFieldArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUserBlobFromCredentialInputFields(hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), pEapConfigInputFieldArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head), pdwUserBlobSize: POINTER(UInt32), ppbUserBlob: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeIdentityUI(dwVersion: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(POINTER(Byte)), ppwszIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeInteractiveUI(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapInteractiveUIData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUIBlobFromInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapInteractiveUIData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head), pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigXml2Blob(dwFlags: UInt32, pConfigDoc: win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNode_head, pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(POINTER(Byte)), pEapMethodType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerCredentialsXml2Blob(dwFlags: UInt32, pCredentialsDoc: win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNode_head, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), pdwSizeOfCredentialsOut: POINTER(UInt32), ppCredentialsOut: POINTER(POINTER(Byte)), pEapMethodType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigBlob2Xml(dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), ppConfigDoc: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument2_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeMemory(pData: POINTER(Byte)) -> Void: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeErrorMemory(pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerInitialize() -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerUninitialize() -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerBeginSession(dwFlags: UInt32, eapType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, pAttributeArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), hTokenImpersonateUser: win32more.Windows.Win32.Foundation.HANDLE, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), dwMaxSendPacketSize: UInt32, pConnectionId: POINTER(Guid), func: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NotificationHandler, pContextData: VoidPtr, pSessionId: POINTER(UInt32), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerProcessReceivedPacket(sessionHandle: UInt32, cbReceivePacket: UInt32, pReceivePacket: POINTER(Byte), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetSendPacket(sessionHandle: UInt32, pcbSendPacket: POINTER(UInt32), ppSendPacket: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResult(sessionHandle: UInt32, reason: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason, ppResult: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResult_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetUIContext(sessionHandle: UInt32, pdwSizeOfUIContextData: POINTER(UInt32), ppUIContextData: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetUIContext(sessionHandle: UInt32, dwSizeOfUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetAuthStatus(sessionHandle: UInt32, authParam: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams, pcbAuthData: POINTER(UInt32), ppAuthData: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerEndSession(sessionHandle: UInt32, ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetDataToUnplumbCredentials(pConnectionIdThatLastSavedCreds: POINTER(Guid), phCredentialImpersonationToken: POINTER(IntPtr), sessionHandle: UInt32, ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), fSaveToCredMan: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerClearConnection(pConnectionId: POINTER(Guid), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeEapError(pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetIdentity(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), hTokenImpersonateUser: win32more.Windows.Win32.Foundation.HANDLE, pfInvokeUI: POINTER(win32more.Windows.Win32.Foundation.BOOL), pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(POINTER(Byte)), ppwszIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)), ppvReserved: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetEncryptedPassword(dwSizeofPassword: UInt32, szPassword: win32more.Windows.Win32.Foundation.PWSTR, ppszEncPassword: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeRuntimeMemory(pData: POINTER(Byte)) -> Void: ...
class EAPHOST_AUTH_INFO(EasyCastStructure):
    status: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS
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
class EAPHOST_IDENTITY_UI_PARAMS(EasyCastStructure):
    eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    dwFlags: UInt32
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    dwSizeofUserDataOut: UInt32
    pUserDataOut: POINTER(Byte)
    pwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    dwError: UInt32
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
class EAPHOST_INTERACTIVE_UI_PARAMS(EasyCastStructure):
    dwSizeofContextData: UInt32
    pContextData: POINTER(Byte)
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: POINTER(Byte)
    dwError: UInt32
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
class EAP_ATTRIBUTE(EasyCastStructure):
    eaType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE
    dwLength: UInt32
    pValue: POINTER(Byte)
class EAP_ATTRIBUTES(EasyCastStructure):
    dwNumberOfAttributes: UInt32
    pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_head)
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
class EAP_AUTHENTICATOR_METHOD_ROUTINES(EasyCastStructure):
    dwSizeInBytes: UInt32
    pEapType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head)
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
class EAP_CONFIG_INPUT_FIELD_ARRAY(EasyCastStructure):
    dwVersion: UInt32
    dwNumberOfFields: UInt32
    pFields: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_DATA_head)
class EAP_CONFIG_INPUT_FIELD_DATA(EasyCastStructure):
    dwSize: UInt32
    Type: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE
    dwFlagProps: UInt32
    pwszLabel: win32more.Windows.Win32.Foundation.PWSTR
    pwszData: win32more.Windows.Win32.Foundation.PWSTR
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
class EAP_CRED_EXPIRY_REQ(EasyCastStructure):
    curCreds: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
    newCreds: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
class EAP_ERROR(EasyCastStructure):
    dwWinError: UInt32
    type: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    dwReasonCode: UInt32
    rootCauseGuid: Guid
    repairGuid: Guid
    helpLinkGuid: Guid
    pRootCauseString: win32more.Windows.Win32.Foundation.PWSTR
    pRepairString: win32more.Windows.Win32.Foundation.PWSTR
class EAP_INTERACTIVE_UI_DATA(EasyCastStructure):
    dwVersion: UInt32
    dwSize: UInt32
    dwDataType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE
    cbUiData: UInt32
    pbUiData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_UI_DATA_FORMAT
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
class EAP_METHOD_AUTHENTICATOR_RESULT(EasyCastStructure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReason: UInt32
    pAuthAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
class EAP_METHOD_INFO(EasyCastStructure):
    eaptype: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfo: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
class EAP_METHOD_INFO_ARRAY(EasyCastStructure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
class EAP_METHOD_INFO_ARRAY_EX(EasyCastStructure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_EX_head)
class EAP_METHOD_INFO_EX(EasyCastStructure):
    eaptype: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfoArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_EX_head)
class EAP_METHOD_PROPERTY(EasyCastStructure):
    eapMethodPropertyType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE
    eapMethodPropertyValueType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE
    eapMethodPropertyValue: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE
class EAP_METHOD_PROPERTY_ARRAY(EasyCastStructure):
    dwNumberOfProperties: UInt32
    pMethodProperty: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_head)
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
class EAP_METHOD_PROPERTY_VALUE(EasyCastUnion):
    empvBool: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_BOOL
    empvDword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_DWORD
    empvString: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_STRING
class EAP_METHOD_PROPERTY_VALUE_BOOL(EasyCastStructure):
    length: UInt32
    value: win32more.Windows.Win32.Foundation.BOOL
class EAP_METHOD_PROPERTY_VALUE_DWORD(EasyCastStructure):
    length: UInt32
    value: UInt32
class EAP_METHOD_PROPERTY_VALUE_STRING(EasyCastStructure):
    length: UInt32
    value: POINTER(Byte)
EAP_METHOD_PROPERTY_VALUE_TYPE = Int32
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtBool: EAP_METHOD_PROPERTY_VALUE_TYPE = 0
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtDword: EAP_METHOD_PROPERTY_VALUE_TYPE = 1
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtString: EAP_METHOD_PROPERTY_VALUE_TYPE = 2
class EAP_METHOD_TYPE(EasyCastStructure):
    eapType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE
    dwAuthorId: UInt32
class EAP_PEER_METHOD_ROUTINES(EasyCastStructure):
    dwVersion: UInt32
    pEapType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE_head)
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
class EAP_TYPE(EasyCastStructure):
    type: Byte
    dwVendorId: UInt32
    dwVendorType: UInt32
class EAP_UI_DATA_FORMAT(EasyCastUnion):
    credData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)
    credExpiryData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CRED_EXPIRY_REQ_head)
    credLogonData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)
class EapCertificateCredential(EasyCastStructure):
    certHash: Byte * 20
    password: win32more.Windows.Win32.Foundation.PWSTR
EapCode = Int32
EapCode_EapCodeMinimum: EapCode = 1
EapCode_EapCodeRequest: EapCode = 1
EapCode_EapCodeResponse: EapCode = 2
EapCode_EapCodeSuccess: EapCode = 3
EapCode_EapCodeFailure: EapCode = 4
EapCode_EapCodeMaximum: EapCode = 4
class EapCredential(EasyCastStructure):
    credType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType
    credData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialTypeData
EapCredentialType = Int32
EAP_EMPTY_CREDENTIAL: EapCredentialType = 0
EAP_USERNAME_PASSWORD_CREDENTIAL: EapCredentialType = 1
EAP_WINLOGON_CREDENTIAL: EapCredentialType = 2
EAP_CERTIFICATE_CREDENTIAL: EapCredentialType = 3
EAP_SIM_CREDENTIAL: EapCredentialType = 4
class EapCredentialTypeData(EasyCastUnion):
    username_password: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapUsernamePasswordCredential
    certificate: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCertificateCredential
    sim: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapSimCredential
EapHostPeerAuthParams = Int32
EapHostPeerAuthParams_EapHostPeerAuthStatus: EapHostPeerAuthParams = 1
EapHostPeerAuthParams_EapHostPeerIdentity: EapHostPeerAuthParams = 2
EapHostPeerAuthParams_EapHostPeerIdentityExtendedInfo: EapHostPeerAuthParams = 3
EapHostPeerAuthParams_EapHostNapInfo: EapHostPeerAuthParams = 4
class EapHostPeerMethodResult(EasyCastStructure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    pAttribArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
    isolationState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE
    pEapMethodInfo: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
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
class EapPacket(EasyCastStructure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class EapPeerMethodOutput(EasyCastStructure):
    action: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction
    fAllowNotifications: win32more.Windows.Win32.Foundation.BOOL
EapPeerMethodResponseAction = Int32
EapPeerMethodResponseAction_EapPeerMethodResponseActionDiscard: EapPeerMethodResponseAction = 0
EapPeerMethodResponseAction_EapPeerMethodResponseActionSend: EapPeerMethodResponseAction = 1
EapPeerMethodResponseAction_EapPeerMethodResponseActionResult: EapPeerMethodResponseAction = 2
EapPeerMethodResponseAction_EapPeerMethodResponseActionInvokeUI: EapPeerMethodResponseAction = 3
EapPeerMethodResponseAction_EapPeerMethodResponseActionRespond: EapPeerMethodResponseAction = 4
EapPeerMethodResponseAction_EapPeerMethodResponseActionNone: EapPeerMethodResponseAction = 5
class EapPeerMethodResult(EasyCastStructure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    pAttribArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)
    pNgcKerbTicket: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)
    fSaveToCredMan: win32more.Windows.Win32.Foundation.BOOL
EapPeerMethodResultReason = Int32
EapPeerMethodResultReason_EapPeerMethodResultUnknown: EapPeerMethodResultReason = 1
EapPeerMethodResultReason_EapPeerMethodResultSuccess: EapPeerMethodResultReason = 2
EapPeerMethodResultReason_EapPeerMethodResultFailure: EapPeerMethodResultReason = 3
class EapSimCredential(EasyCastStructure):
    iccID: win32more.Windows.Win32.Foundation.PWSTR
class EapUsernamePasswordCredential(EasyCastStructure):
    username: win32more.Windows.Win32.Foundation.PWSTR
    password: win32more.Windows.Win32.Foundation.PWSTR
class IAccountingProviderConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a2db18-d706-11d0-a37b-00c04fc9da04}')
    @commethod(3)
    def Initialize(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, puConnectionParam: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self, uConnectionParam: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(self, uConnectionParam: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(self, uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(self, uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAuthenticationProviderConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a2db17-d706-11d0-a37b-00c04fc9da04}')
    @commethod(3)
    def Initialize(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, puConnectionParam: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self, uConnectionParam: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(self, uConnectionParam: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(self, uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(self, uConnectionParam: UIntPtr, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a2db19-d706-11d0-a37b-00c04fc9da04}')
    @commethod(3)
    def Initialize(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwEapTypeId: UInt32, puConnectionParam: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uninitialize(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ServerInvokeConfigUI(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, uReserved1: UIntPtr, uReserved2: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RouterInvokeConfigUI(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pConnectionDataIn: POINTER(Byte), dwSizeOfConnectionDataIn: UInt32, ppConnectionDataOut: POINTER(POINTER(Byte)), pdwSizeOfConnectionDataOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RouterInvokeCredentialsUI(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pConnectionDataIn: POINTER(Byte), dwSizeOfConnectionDataIn: UInt32, pUserDataIn: POINTER(Byte), dwSizeOfUserDataIn: UInt32, ppUserDataOut: POINTER(POINTER(Byte)), pdwSizeOfUserDataOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig2(ComPtr):
    extends: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig
    _iid_ = Guid('{d565917a-85c4-4466-856e-671c3742ea9a}')
    @commethod(8)
    def ServerInvokeConfigUI2(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, pConfigDataIn: POINTER(Byte), dwSizeOfConfigDataIn: UInt32, ppConfigDataOut: POINTER(POINTER(Byte)), pdwSizeOfConfigDataOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGlobalConfig(self, dwEapTypeId: UInt32, ppConfigDataOut: POINTER(POINTER(Byte)), pdwSizeOfConfigDataOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEAPProviderConfig3(ComPtr):
    extends: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig2
    _iid_ = Guid('{b78ecd12-68bb-4f86-9bf0-8438dd3be982}')
    @commethod(10)
    def ServerInvokeCertificateConfigUI(self, dwEapTypeId: UInt32, uConnectionParam: UIntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, pConfigDataIn: POINTER(Byte), dwSizeOfConfigDataIn: UInt32, ppConfigDataOut: POINTER(POINTER(Byte)), pdwSizeOfConfigDataOut: POINTER(UInt32), uReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRouterProtocolConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a2db16-d706-11d0-a37b-00c04fc9da04}')
    @commethod(3)
    def AddProtocol(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: win32more.Windows.Win32.System.Com.IUnknown_head, uReserved1: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveProtocol(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: win32more.Windows.Win32.System.Com.IUnknown_head, uReserved1: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ISOLATION_STATE = Int32
ISOLATION_STATE_UNKNOWN: ISOLATION_STATE = 0
ISOLATION_STATE_NOT_RESTRICTED: ISOLATION_STATE = 1
ISOLATION_STATE_IN_PROBATION: ISOLATION_STATE = 2
ISOLATION_STATE_RESTRICTED_ACCESS: ISOLATION_STATE = 3
class LEGACY_IDENTITY_UI_PARAMS(EasyCastStructure):
    eapType: UInt32
    dwFlags: UInt32
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    dwSizeofUserDataOut: UInt32
    pUserDataOut: POINTER(Byte)
    pwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    dwError: UInt32
class LEGACY_INTERACTIVE_UI_PARAMS(EasyCastStructure):
    eapType: UInt32
    dwSizeofContextData: UInt32
    pContextData: POINTER(Byte)
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: POINTER(Byte)
    dwError: UInt32
class NgcTicketContext(EasyCastStructure):
    wszTicket: Char * 45
    hKey: win32more.Windows.Win32.Security.Cryptography.NCRYPT_KEY_HANDLE
    hImpersonateToken: win32more.Windows.Win32.Foundation.HANDLE
@winfunctype_pointer
def NotificationHandler(connectionId: Guid, pContextData: VoidPtr) -> Void: ...
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
class PPP_EAP_INFO(EasyCastStructure):
    dwSizeInBytes: UInt32
    dwEapTypeId: UInt32
    RasEapInitialize: IntPtr
    RasEapBegin: IntPtr
    RasEapEnd: IntPtr
    RasEapMakeMessage: IntPtr
class PPP_EAP_INPUT(EasyCastStructure):
    dwSizeInBytes: UInt32
    fFlags: UInt32
    fAuthenticator: win32more.Windows.Win32.Foundation.BOOL
    pwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    pwszPassword: win32more.Windows.Win32.Foundation.PWSTR
    bInitialId: Byte
    pUserAttributes: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)
    fAuthenticationComplete: win32more.Windows.Win32.Foundation.BOOL
    dwAuthResultCode: UInt32
    hTokenImpersonateUser: win32more.Windows.Win32.Foundation.HANDLE
    fSuccessPacketReceived: win32more.Windows.Win32.Foundation.BOOL
    fDataReceivedFromInteractiveUI: win32more.Windows.Win32.Foundation.BOOL
    pDataFromInteractiveUI: POINTER(Byte)
    dwSizeOfDataFromInteractiveUI: UInt32
    pConnectionData: POINTER(Byte)
    dwSizeOfConnectionData: UInt32
    pUserData: POINTER(Byte)
    dwSizeOfUserData: UInt32
    hReserved: win32more.Windows.Win32.Foundation.HANDLE
    guidConnectionId: Guid
    isVpn: win32more.Windows.Win32.Foundation.BOOL
class PPP_EAP_OUTPUT(EasyCastStructure):
    dwSizeInBytes: UInt32
    Action: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION
    dwAuthResultCode: UInt32
    pUserAttributes: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)
    fInvokeInteractiveUI: win32more.Windows.Win32.Foundation.BOOL
    pUIContextData: POINTER(Byte)
    dwSizeOfUIContextData: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    pConnectionData: POINTER(Byte)
    dwSizeOfConnectionData: UInt32
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    pUserData: POINTER(Byte)
    dwSizeOfUserData: UInt32
    pNgcKerbTicket: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)
    fSaveToCredMan: win32more.Windows.Win32.Foundation.BOOL
class PPP_EAP_PACKET(EasyCastStructure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class RAS_AUTH_ATTRIBUTE(EasyCastStructure):
    raaType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE
    dwLength: UInt32
    Value: VoidPtr
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
