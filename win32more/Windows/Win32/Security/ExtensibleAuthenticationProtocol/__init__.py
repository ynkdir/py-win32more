from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol
import win32more.Windows.Win32.System.Com
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
def EapHostPeerGetMethods(pEapMethodInfoArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerGetMethodProperties(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), dwUserDataSize: UInt32, pbUserData: POINTER(Byte), pMethodPropertyArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_ARRAY), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeConfigUI(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryCredentialInputFields(hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), pEapConfigInputFieldArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUserBlobFromCredentialInputFields(hUserImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, dwEapConnDataSize: UInt32, pbEapConnData: POINTER(Byte), pEapConfigInputFieldArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY), pdwUserBlobSize: POINTER(UInt32), ppbUserBlob: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeIdentityUI(dwVersion: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwFlags: UInt32, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(POINTER(Byte)), ppwszIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerInvokeInteractiveUI(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapInteractiveUIData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerQueryUIBlobFromInteractiveUIInputFields(dwVersion: UInt32, dwFlags: UInt32, dwSizeofUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapInteractiveUIData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA), pdwSizeOfDataFromInteractiveUI: POINTER(UInt32), ppDataFromInteractiveUI: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)), ppvReserved: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigXml2Blob(dwFlags: UInt32, pConfigDoc: win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNode, pdwSizeOfConfigOut: POINTER(UInt32), ppConfigOut: POINTER(POINTER(Byte)), pEapMethodType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerCredentialsXml2Blob(dwFlags: UInt32, pCredentialsDoc: win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNode, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), pdwSizeOfCredentialsOut: POINTER(UInt32), ppCredentialsOut: POINTER(POINTER(Byte)), pEapMethodType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerConfigBlob2Xml(dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeOfConfigIn: UInt32, pConfigIn: POINTER(Byte), ppConfigDoc: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument2), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeMemory(pData: POINTER(Byte)) -> Void: ...
@winfunctype('eappcfg.dll')
def EapHostPeerFreeErrorMemory(pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerInitialize() -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerUninitialize() -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerBeginSession(dwFlags: UInt32, eapType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, pAttributeArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES), hTokenImpersonateUser: win32more.Windows.Win32.Foundation.HANDLE, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), dwMaxSendPacketSize: UInt32, pConnectionId: POINTER(Guid), func: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NotificationHandler, pContextData: VoidPtr, pSessionId: POINTER(UInt32), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerProcessReceivedPacket(sessionHandle: UInt32, cbReceivePacket: UInt32, pReceivePacket: POINTER(Byte), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetSendPacket(sessionHandle: UInt32, pcbSendPacket: POINTER(UInt32), ppSendPacket: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResult(sessionHandle: UInt32, reason: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason, ppResult: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResult), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetUIContext(sessionHandle: UInt32, pdwSizeOfUIContextData: POINTER(UInt32), ppUIContextData: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetUIContext(sessionHandle: UInt32, dwSizeOfUIContextData: UInt32, pUIContextData: POINTER(Byte), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerSetResponseAttributes(sessionHandle: UInt32, pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES), pEapOutput: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetAuthStatus(sessionHandle: UInt32, authParam: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams, pcbAuthData: POINTER(UInt32), ppAuthData: POINTER(POINTER(Byte)), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerEndSession(sessionHandle: UInt32, ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetDataToUnplumbCredentials(pConnectionIdThatLastSavedCreds: POINTER(Guid), phCredentialImpersonationToken: POINTER(IntPtr), sessionHandle: UInt32, ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)), fSaveToCredMan: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerClearConnection(pConnectionId: POINTER(Guid), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeEapError(pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)) -> Void: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetIdentity(dwVersion: UInt32, dwFlags: UInt32, eapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE, dwSizeofConnectionData: UInt32, pConnectionData: POINTER(Byte), dwSizeofUserData: UInt32, pUserData: POINTER(Byte), hTokenImpersonateUser: win32more.Windows.Win32.Foundation.HANDLE, pfInvokeUI: POINTER(win32more.Windows.Win32.Foundation.BOOL), pdwSizeOfUserDataOut: POINTER(UInt32), ppUserDataOut: POINTER(POINTER(Byte)), ppwszIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppEapError: POINTER(POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)), ppvReserved: POINTER(POINTER(Byte))) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerGetEncryptedPassword(dwSizeofPassword: UInt32, szPassword: win32more.Windows.Win32.Foundation.PWSTR, ppszEncPassword: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('eappprxy.dll')
def EapHostPeerFreeRuntimeMemory(pData: POINTER(Byte)) -> Void: ...
class EAPHOST_AUTH_INFO(Structure):
    status: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS
    dwErrorCode: UInt32
    dwReasonCode: UInt32
EAPHOST_AUTH_STATUS = Int32
EapHostInvalidSession: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 0
EapHostAuthNotStarted: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 1
EapHostAuthIdentityExchange: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 2
EapHostAuthNegotiatingType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 3
EapHostAuthInProgress: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 4
EapHostAuthSucceeded: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 5
EapHostAuthFailed: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS = 6
class EAPHOST_IDENTITY_UI_PARAMS(Structure):
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
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)
class EAPHOST_INTERACTIVE_UI_PARAMS(Structure):
    dwSizeofContextData: UInt32
    pContextData: POINTER(Byte)
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: POINTER(Byte)
    dwError: UInt32
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)
class EAP_ATTRIBUTE(Structure):
    eaType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE
    dwLength: UInt32
    pValue: POINTER(Byte)
class EAP_ATTRIBUTES(Structure):
    dwNumberOfAttributes: UInt32
    pAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE)
EAP_ATTRIBUTE_TYPE = Int32
eatMinimum: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 0
eatUserName: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 1
eatUserPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 2
eatMD5CHAPPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 3
eatNASIPAddress: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 4
eatNASPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 5
eatServiceType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 6
eatFramedProtocol: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 7
eatFramedIPAddress: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8
eatFramedIPNetmask: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9
eatFramedRouting: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 10
eatFilterId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 11
eatFramedMTU: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 12
eatFramedCompression: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 13
eatLoginIPHost: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 14
eatLoginService: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 15
eatLoginTCPPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 16
eatUnassigned17: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 17
eatReplyMessage: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 18
eatCallbackNumber: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 19
eatCallbackId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 20
eatUnassigned21: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 21
eatFramedRoute: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 22
eatFramedIPXNetwork: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 23
eatState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 24
eatClass: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 25
eatVendorSpecific: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 26
eatSessionTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 27
eatIdleTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 28
eatTerminationAction: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 29
eatCalledStationId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 30
eatCallingStationId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 31
eatNASIdentifier: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 32
eatProxyState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 33
eatLoginLATService: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 34
eatLoginLATNode: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 35
eatLoginLATGroup: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 36
eatFramedAppleTalkLink: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 37
eatFramedAppleTalkNetwork: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 38
eatFramedAppleTalkZone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 39
eatAcctStatusType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 40
eatAcctDelayTime: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 41
eatAcctInputOctets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 42
eatAcctOutputOctets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 43
eatAcctSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 44
eatAcctAuthentic: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 45
eatAcctSessionTime: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 46
eatAcctInputPackets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 47
eatAcctOutputPackets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 48
eatAcctTerminateCause: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 49
eatAcctMultiSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 50
eatAcctLinkCount: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 51
eatAcctEventTimeStamp: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 55
eatMD5CHAPChallenge: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 60
eatNASPortType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 61
eatPortLimit: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 62
eatLoginLATPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 63
eatTunnelType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 64
eatTunnelMediumType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 65
eatTunnelClientEndpoint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 66
eatTunnelServerEndpoint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 67
eatARAPPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 70
eatARAPFeatures: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 71
eatARAPZoneAccess: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 72
eatARAPSecurity: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 73
eatARAPSecurityData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 74
eatPasswordRetry: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 75
eatPrompt: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 76
eatConnectInfo: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 77
eatConfigurationToken: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 78
eatEAPMessage: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 79
eatSignature: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 80
eatARAPChallengeResponse: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 84
eatAcctInterimInterval: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 85
eatNASIPv6Address: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 95
eatFramedInterfaceId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 96
eatFramedIPv6Prefix: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 97
eatLoginIPv6Host: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 98
eatFramedIPv6Route: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 99
eatFramedIPv6Pool: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 100
eatARAPGuestLogon: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8096
eatCertificateOID: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8097
eatEAPConfiguration: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8098
eatPEAPEmbeddedEAPTypeId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8099
eatPEAPFastRoamedSession: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8100
eatFastRoamedSession: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8100
eatEAPTLV: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8102
eatCredentialsChanged: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8103
eatInnerEapMethodType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8104
eatClearTextPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8107
eatQuarantineSoH: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8150
eatCertificateThumbprint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 8250
eatPeerId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9000
eatServerId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9001
eatMethodId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9002
eatEMSK: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9003
eatSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = 9004
eatReserved: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE = -1
class EAP_AUTHENTICATOR_METHOD_ROUTINES(Structure):
    dwSizeInBytes: UInt32
    pEapType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE)
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
EAP_AUTHENTICATOR_SEND_TIMEOUT_NONE: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_AUTHENTICATOR_SEND_TIMEOUT = 0
EAP_AUTHENTICATOR_SEND_TIMEOUT_BASIC: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_AUTHENTICATOR_SEND_TIMEOUT = 1
EAP_AUTHENTICATOR_SEND_TIMEOUT_INTERACTIVE: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_AUTHENTICATOR_SEND_TIMEOUT = 2
class EAP_CONFIG_INPUT_FIELD_ARRAY(Structure):
    dwVersion: UInt32
    dwNumberOfFields: UInt32
    pFields: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_DATA)
class EAP_CONFIG_INPUT_FIELD_DATA(Structure):
    dwSize: UInt32
    Type: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE
    dwFlagProps: UInt32
    pwszLabel: win32more.Windows.Win32.Foundation.PWSTR
    pwszData: win32more.Windows.Win32.Foundation.PWSTR
    dwMinDataLength: UInt32
    dwMaxDataLength: UInt32
EAP_CONFIG_INPUT_FIELD_TYPE = Int32
EapConfigInputUsername: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 0
EapConfigInputPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 1
EapConfigInputNetworkUsername: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 2
EapConfigInputNetworkPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 3
EapConfigInputPin: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 4
EapConfigInputPSK: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 5
EapConfigInputEdit: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 6
EapConfigSmartCardUsername: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 7
EapConfigSmartCardError: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE = 8
class EAP_CRED_EXPIRY_REQ(Structure):
    curCreds: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
    newCreds: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY
class EAP_ERROR(Structure):
    dwWinError: UInt32
    type: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    dwReasonCode: UInt32
    rootCauseGuid: Guid
    repairGuid: Guid
    helpLinkGuid: Guid
    pRootCauseString: win32more.Windows.Win32.Foundation.PWSTR
    pRepairString: win32more.Windows.Win32.Foundation.PWSTR
class EAP_INTERACTIVE_UI_DATA(Structure):
    dwVersion: UInt32
    dwSize: UInt32
    dwDataType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE
    cbUiData: UInt32
    pbUiData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_UI_DATA_FORMAT
EAP_INTERACTIVE_UI_DATA_TYPE = Int32
EapCredReq: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 0
EapCredResp: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 1
EapCredExpiryReq: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 2
EapCredExpiryResp: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 3
EapCredLogonReq: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 4
EapCredLogonResp: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE = 5
EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = Int32
EAP_METHOD_AUTHENTICATOR_RESPONSE_DISCARD: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 0
EAP_METHOD_AUTHENTICATOR_RESPONSE_SEND: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 1
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESULT: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 2
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESPOND: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 3
EAP_METHOD_AUTHENTICATOR_RESPONSE_AUTHENTICATE: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 4
EAP_METHOD_AUTHENTICATOR_RESPONSE_HANDLE_IDENTITY: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = 5
class EAP_METHOD_AUTHENTICATOR_RESULT(Structure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReason: UInt32
    pAuthAttribs: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES)
class EAP_METHOD_INFO(Structure):
    eaptype: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfo: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO)
class EAP_METHOD_INFO_ARRAY(Structure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO)
class EAP_METHOD_INFO_ARRAY_EX(Structure):
    dwNumberOfMethods: UInt32
    pEapMethods: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_EX)
class EAP_METHOD_INFO_EX(Structure):
    eaptype: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE
    pwszAuthorName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    eapProperties: UInt32
    pInnerMethodInfoArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_EX)
class EAP_METHOD_PROPERTY(Structure):
    eapMethodPropertyType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE
    eapMethodPropertyValueType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE
    eapMethodPropertyValue: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE
class EAP_METHOD_PROPERTY_ARRAY(Structure):
    dwNumberOfProperties: UInt32
    pMethodProperty: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY)
EAP_METHOD_PROPERTY_TYPE = Int32
emptPropCipherSuiteNegotiation: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 0
emptPropMutualAuth: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 1
emptPropIntegrity: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 2
emptPropReplayProtection: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 3
emptPropConfidentiality: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 4
emptPropKeyDerivation: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 5
emptPropKeyStrength64: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 6
emptPropKeyStrength128: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 7
emptPropKeyStrength256: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 8
emptPropKeyStrength512: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 9
emptPropKeyStrength1024: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 10
emptPropDictionaryAttackResistance: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 11
emptPropFastReconnect: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 12
emptPropCryptoBinding: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 13
emptPropSessionIndependence: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 14
emptPropFragmentation: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 15
emptPropChannelBinding: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 16
emptPropNap: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 17
emptPropStandalone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 18
emptPropMppeEncryption: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 19
emptPropTunnelMethod: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 20
emptPropSupportsConfig: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 21
emptPropCertifiedMethod: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 22
emptPropHiddenMethod: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 23
emptPropMachineAuth: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 24
emptPropUserAuth: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 25
emptPropIdentityPrivacy: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 26
emptPropMethodChaining: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 27
emptPropSharedStateEquivalence: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 28
emptLegacyMethodPropertyFlag: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 31
emptPropVendorSpecific: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE = 255
class EAP_METHOD_PROPERTY_VALUE(Union):
    empvBool: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_BOOL
    empvDword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_DWORD
    empvString: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_STRING
class EAP_METHOD_PROPERTY_VALUE_BOOL(Structure):
    length: UInt32
    value: win32more.Windows.Win32.Foundation.BOOL
class EAP_METHOD_PROPERTY_VALUE_DWORD(Structure):
    length: UInt32
    value: UInt32
class EAP_METHOD_PROPERTY_VALUE_STRING(Structure):
    length: UInt32
    value: POINTER(Byte)
EAP_METHOD_PROPERTY_VALUE_TYPE = Int32
empvtBool: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE = 0
empvtDword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE = 1
empvtString: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE = 2
class EAP_METHOD_TYPE(Structure):
    eapType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE
    dwAuthorId: UInt32
class EAP_PEER_METHOD_ROUTINES(Structure):
    dwVersion: UInt32
    pEapType: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_TYPE)
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
    credData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY)
    credExpiryData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CRED_EXPIRY_REQ)
    credLogonData: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY)
class EapCertificateCredential(Structure):
    certHash: Byte * 20
    password: win32more.Windows.Win32.Foundation.PWSTR
EapCode = Int32
EapCodeMinimum: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 1
EapCodeRequest: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 1
EapCodeResponse: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 2
EapCodeSuccess: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 3
EapCodeFailure: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 4
EapCodeMaximum: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCode = 4
class EapCredential(Structure):
    credType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType
    credData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialTypeData
EapCredentialType = Int32
EAP_EMPTY_CREDENTIAL: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType = 0
EAP_USERNAME_PASSWORD_CREDENTIAL: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType = 1
EAP_WINLOGON_CREDENTIAL: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType = 2
EAP_CERTIFICATE_CREDENTIAL: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType = 3
EAP_SIM_CREDENTIAL: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCredentialType = 4
class EapCredentialTypeData(Union):
    username_password: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapUsernamePasswordCredential
    certificate: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapCertificateCredential
    sim: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapSimCredential
EapHostPeerAuthParams = Int32
EapHostPeerAuthStatus: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams = 1
EapHostPeerIdentity: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams = 2
EapHostPeerIdentityExtendedInfo: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams = 3
EapHostNapInfo: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams = 4
class EapHostPeerMethodResult(Structure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    pAttribArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES)
    isolationState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE
    pEapMethodInfo: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO)
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)
EapHostPeerMethodResultReason = Int32
EapHostPeerMethodResultAltSuccessReceived: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason = 1
EapHostPeerMethodResultTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason = 2
EapHostPeerMethodResultFromMethod: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason = 3
EapHostPeerResponseAction = Int32
EapHostPeerResponseDiscard: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 0
EapHostPeerResponseSend: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 1
EapHostPeerResponseResult: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 2
EapHostPeerResponseInvokeUi: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 3
EapHostPeerResponseRespond: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 4
EapHostPeerResponseStartAuthentication: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 5
EapHostPeerResponseNone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction = 6
class EapPacket(Structure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class EapPeerMethodOutput(Structure):
    action: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction
    fAllowNotifications: win32more.Windows.Win32.Foundation.BOOL
EapPeerMethodResponseAction = Int32
EapPeerMethodResponseActionDiscard: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 0
EapPeerMethodResponseActionSend: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 1
EapPeerMethodResponseActionResult: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 2
EapPeerMethodResponseActionInvokeUI: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 3
EapPeerMethodResponseActionRespond: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 4
EapPeerMethodResponseActionNone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction = 5
class EapPeerMethodResult(Structure):
    fIsSuccess: win32more.Windows.Win32.Foundation.BOOL
    dwFailureReasonCode: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofConnectionData: UInt32
    pConnectionData: POINTER(Byte)
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    dwSizeofUserData: UInt32
    pUserData: POINTER(Byte)
    pAttribArray: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES)
    pEapError: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EAP_ERROR)
    pNgcKerbTicket: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext)
    fSaveToCredMan: win32more.Windows.Win32.Foundation.BOOL
EapPeerMethodResultReason = Int32
EapPeerMethodResultUnknown: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResultReason = 1
EapPeerMethodResultSuccess: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResultReason = 2
EapPeerMethodResultFailure: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResultReason = 3
class EapSimCredential(Structure):
    iccID: win32more.Windows.Win32.Foundation.PWSTR
class EapUsernamePasswordCredential(Structure):
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
    def AddProtocol(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: win32more.Windows.Win32.System.Com.IUnknown, uReserved1: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveProtocol(self, pszMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwTransportId: UInt32, dwProtocolId: UInt32, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pRouter: win32more.Windows.Win32.System.Com.IUnknown, uReserved1: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ISOLATION_STATE = Int32
ISOLATION_STATE_UNKNOWN: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE = 0
ISOLATION_STATE_NOT_RESTRICTED: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE = 1
ISOLATION_STATE_IN_PROBATION: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE = 2
ISOLATION_STATE_RESTRICTED_ACCESS: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE = 3
class LEGACY_IDENTITY_UI_PARAMS(Structure):
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
class LEGACY_INTERACTIVE_UI_PARAMS(Structure):
    eapType: UInt32
    dwSizeofContextData: UInt32
    pContextData: POINTER(Byte)
    dwSizeofInteractiveUIData: UInt32
    pInteractiveUIData: POINTER(Byte)
    dwError: UInt32
class NgcTicketContext(Structure):
    wszTicket: Char * 45
    hKey: win32more.Windows.Win32.Security.Cryptography.NCRYPT_KEY_HANDLE
    hImpersonateToken: win32more.Windows.Win32.Foundation.HANDLE
@winfunctype_pointer
def NotificationHandler(connectionId: Guid, pContextData: VoidPtr) -> Void: ...
PPP_EAP_ACTION = Int32
EAPACTION_NoAction: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 0
EAPACTION_Authenticate: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 1
EAPACTION_Done: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 2
EAPACTION_SendAndDone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 3
EAPACTION_Send: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 4
EAPACTION_SendWithTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 5
EAPACTION_SendWithTimeoutInteractive: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 6
EAPACTION_IndicateTLV: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 7
EAPACTION_IndicateIdentity: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION = 8
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
    fAuthenticator: win32more.Windows.Win32.Foundation.BOOL
    pwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    pwszPassword: win32more.Windows.Win32.Foundation.PWSTR
    bInitialId: Byte
    pUserAttributes: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE)
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
class PPP_EAP_OUTPUT(Structure):
    dwSizeInBytes: UInt32
    Action: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION
    dwAuthResultCode: UInt32
    pUserAttributes: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE)
    fInvokeInteractiveUI: win32more.Windows.Win32.Foundation.BOOL
    pUIContextData: POINTER(Byte)
    dwSizeOfUIContextData: UInt32
    fSaveConnectionData: win32more.Windows.Win32.Foundation.BOOL
    pConnectionData: POINTER(Byte)
    dwSizeOfConnectionData: UInt32
    fSaveUserData: win32more.Windows.Win32.Foundation.BOOL
    pUserData: POINTER(Byte)
    dwSizeOfUserData: UInt32
    pNgcKerbTicket: POINTER(win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.NgcTicketContext)
    fSaveToCredMan: win32more.Windows.Win32.Foundation.BOOL
class PPP_EAP_PACKET(Structure):
    Code: Byte
    Id: Byte
    Length: Byte * 2
    Data: Byte * 1
class RAS_AUTH_ATTRIBUTE(Structure):
    raaType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE
    dwLength: UInt32
    Value: VoidPtr
RAS_AUTH_ATTRIBUTE_TYPE = Int32
raatMinimum: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 0
raatUserName: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 1
raatUserPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 2
raatMD5CHAPPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 3
raatNASIPAddress: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 4
raatNASPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 5
raatServiceType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 6
raatFramedProtocol: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 7
raatFramedIPAddress: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8
raatFramedIPNetmask: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9
raatFramedRouting: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 10
raatFilterId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 11
raatFramedMTU: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 12
raatFramedCompression: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 13
raatLoginIPHost: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 14
raatLoginService: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 15
raatLoginTCPPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 16
raatUnassigned17: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 17
raatReplyMessage: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 18
raatCallbackNumber: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 19
raatCallbackId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 20
raatUnassigned21: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 21
raatFramedRoute: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 22
raatFramedIPXNetwork: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 23
raatState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 24
raatClass: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 25
raatVendorSpecific: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 26
raatSessionTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 27
raatIdleTimeout: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 28
raatTerminationAction: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 29
raatCalledStationId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 30
raatCallingStationId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 31
raatNASIdentifier: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 32
raatProxyState: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 33
raatLoginLATService: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 34
raatLoginLATNode: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 35
raatLoginLATGroup: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 36
raatFramedAppleTalkLink: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 37
raatFramedAppleTalkNetwork: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 38
raatFramedAppleTalkZone: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 39
raatAcctStatusType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 40
raatAcctDelayTime: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 41
raatAcctInputOctets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 42
raatAcctOutputOctets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 43
raatAcctSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 44
raatAcctAuthentic: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 45
raatAcctSessionTime: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 46
raatAcctInputPackets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 47
raatAcctOutputPackets: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 48
raatAcctTerminateCause: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 49
raatAcctMultiSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 50
raatAcctLinkCount: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 51
raatAcctEventTimeStamp: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 55
raatMD5CHAPChallenge: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 60
raatNASPortType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 61
raatPortLimit: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 62
raatLoginLATPort: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 63
raatTunnelType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 64
raatTunnelMediumType: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 65
raatTunnelClientEndpoint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 66
raatTunnelServerEndpoint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 67
raatARAPPassword: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 70
raatARAPFeatures: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 71
raatARAPZoneAccess: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 72
raatARAPSecurity: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 73
raatARAPSecurityData: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 74
raatPasswordRetry: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 75
raatPrompt: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 76
raatConnectInfo: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 77
raatConfigurationToken: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 78
raatEAPMessage: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 79
raatSignature: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 80
raatARAPChallengeResponse: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 84
raatAcctInterimInterval: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 85
raatNASIPv6Address: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 95
raatFramedInterfaceId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 96
raatFramedIPv6Prefix: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 97
raatLoginIPv6Host: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 98
raatFramedIPv6Route: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 99
raatFramedIPv6Pool: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 100
raatARAPGuestLogon: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8096
raatCertificateOID: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8097
raatEAPConfiguration: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8098
raatPEAPEmbeddedEAPTypeId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8099
raatInnerEAPTypeId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8099
raatPEAPFastRoamedSession: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8100
raatFastRoamedSession: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8100
raatEAPTLV: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8102
raatCredentialsChanged: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8103
raatCertificateThumbprint: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 8250
raatPeerId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9000
raatServerId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9001
raatMethodId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9002
raatEMSK: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9003
raatSessionId: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = 9004
raatReserved: win32more.Windows.Win32.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE = -1


make_ready(__name__)
