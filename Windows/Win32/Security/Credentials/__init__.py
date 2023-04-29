from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security.Credentials
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CRED_MAX_CREDENTIAL_BLOB_SIZE: UInt32 = 2560
CRED_MAX_USERNAME_LENGTH: UInt32 = 513
CRED_MAX_DOMAIN_TARGET_NAME_LENGTH: UInt32 = 337
FILE_DEVICE_SMARTCARD: UInt32 = 49
GUID_DEVINTERFACE_SMARTCARD_READER: Guid = Guid('50dd5230-ba8a-11d1-bf-5d-00-00-f8-05-f5-30')
SCARD_ATR_LENGTH: UInt32 = 33
SCARD_PROTOCOL_UNDEFINED: UInt32 = 0
SCARD_PROTOCOL_T0: UInt32 = 1
SCARD_PROTOCOL_T1: UInt32 = 2
SCARD_PROTOCOL_RAW: UInt32 = 65536
SCARD_PROTOCOL_DEFAULT: UInt32 = 2147483648
SCARD_PROTOCOL_OPTIMAL: UInt32 = 0
SCARD_POWER_DOWN: UInt32 = 0
SCARD_COLD_RESET: UInt32 = 1
SCARD_WARM_RESET: UInt32 = 2
MAXIMUM_ATTR_STRING_LENGTH: UInt32 = 32
MAXIMUM_SMARTCARD_READERS: UInt32 = 10
SCARD_CLASS_VENDOR_INFO: UInt32 = 1
SCARD_CLASS_COMMUNICATIONS: UInt32 = 2
SCARD_CLASS_PROTOCOL: UInt32 = 3
SCARD_CLASS_POWER_MGMT: UInt32 = 4
SCARD_CLASS_SECURITY: UInt32 = 5
SCARD_CLASS_MECHANICAL: UInt32 = 6
SCARD_CLASS_VENDOR_DEFINED: UInt32 = 7
SCARD_CLASS_IFD_PROTOCOL: UInt32 = 8
SCARD_CLASS_ICC_STATE: UInt32 = 9
SCARD_CLASS_PERF: UInt32 = 32766
SCARD_CLASS_SYSTEM: UInt32 = 32767
SCARD_T0_HEADER_LENGTH: UInt32 = 7
SCARD_T0_CMD_LENGTH: UInt32 = 5
SCARD_T1_PROLOGUE_LENGTH: UInt32 = 3
SCARD_T1_EPILOGUE_LENGTH: UInt32 = 2
SCARD_T1_EPILOGUE_LENGTH_LRC: UInt32 = 1
SCARD_T1_MAX_IFS: UInt32 = 254
SCARD_UNKNOWN: UInt32 = 0
SCARD_ABSENT: UInt32 = 1
SCARD_PRESENT: UInt32 = 2
SCARD_SWALLOWED: UInt32 = 3
SCARD_POWERED: UInt32 = 4
SCARD_NEGOTIABLE: UInt32 = 5
SCARD_SPECIFIC: UInt32 = 6
SCARD_READER_SWALLOWS: UInt32 = 1
SCARD_READER_EJECTS: UInt32 = 2
SCARD_READER_CONFISCATES: UInt32 = 4
SCARD_READER_CONTACTLESS: UInt32 = 8
SCARD_READER_TYPE_SERIAL: UInt32 = 1
SCARD_READER_TYPE_PARALELL: UInt32 = 2
SCARD_READER_TYPE_KEYBOARD: UInt32 = 4
SCARD_READER_TYPE_SCSI: UInt32 = 8
SCARD_READER_TYPE_IDE: UInt32 = 16
SCARD_READER_TYPE_USB: UInt32 = 32
SCARD_READER_TYPE_PCMCIA: UInt32 = 64
SCARD_READER_TYPE_TPM: UInt32 = 128
SCARD_READER_TYPE_NFC: UInt32 = 256
SCARD_READER_TYPE_UICC: UInt32 = 512
SCARD_READER_TYPE_NGC: UInt32 = 1024
SCARD_READER_TYPE_EMBEDDEDSE: UInt32 = 2048
SCARD_READER_TYPE_VENDOR: UInt32 = 240
STATUS_LOGON_FAILURE: Windows.Win32.Foundation.NTSTATUS = -1073741715
STATUS_WRONG_PASSWORD: Windows.Win32.Foundation.NTSTATUS = -1073741718
STATUS_PASSWORD_EXPIRED: Windows.Win32.Foundation.NTSTATUS = -1073741711
STATUS_PASSWORD_MUST_CHANGE: Windows.Win32.Foundation.NTSTATUS = -1073741276
STATUS_DOWNGRADE_DETECTED: Windows.Win32.Foundation.NTSTATUS = -1073740920
STATUS_AUTHENTICATION_FIREWALL_FAILED: Windows.Win32.Foundation.NTSTATUS = -1073740781
STATUS_ACCOUNT_DISABLED: Windows.Win32.Foundation.NTSTATUS = -1073741710
STATUS_ACCOUNT_RESTRICTION: Windows.Win32.Foundation.NTSTATUS = -1073741714
STATUS_ACCOUNT_LOCKED_OUT: Windows.Win32.Foundation.NTSTATUS = -1073741260
STATUS_ACCOUNT_EXPIRED: Windows.Win32.Foundation.NTSTATUS = -1073741421
STATUS_LOGON_TYPE_NOT_GRANTED: Windows.Win32.Foundation.NTSTATUS = -1073741477
STATUS_NO_SUCH_LOGON_SESSION: Windows.Win32.Foundation.NTSTATUS = -1073741729
STATUS_NO_SUCH_USER: Windows.Win32.Foundation.NTSTATUS = -1073741724
CRED_MAX_STRING_LENGTH: UInt32 = 256
CRED_MAX_GENERIC_TARGET_NAME_LENGTH: UInt32 = 32767
CRED_MAX_TARGETNAME_NAMESPACE_LENGTH: UInt32 = 256
CRED_MAX_TARGETNAME_ATTRIBUTE_LENGTH: UInt32 = 256
CRED_MAX_VALUE_SIZE: UInt32 = 256
CRED_MAX_ATTRIBUTES: UInt32 = 64
CRED_SESSION_WILDCARD_NAME_W: String = '*Session'
CRED_SESSION_WILDCARD_NAME_A: String = '*Session'
CRED_TARGETNAME_DOMAIN_NAMESPACE_W: String = 'Domain'
CRED_TARGETNAME_DOMAIN_NAMESPACE_A: String = 'Domain'
CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_W: String = 'LegacyGeneric'
CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_A: String = 'LegacyGeneric'
CRED_TARGETNAME_ATTRIBUTE_TARGET_W: String = 'target'
CRED_TARGETNAME_ATTRIBUTE_TARGET_A: String = 'target'
CRED_TARGETNAME_ATTRIBUTE_NAME_W: String = 'name'
CRED_TARGETNAME_ATTRIBUTE_NAME_A: String = 'name'
CRED_TARGETNAME_ATTRIBUTE_BATCH_W: String = 'batch'
CRED_TARGETNAME_ATTRIBUTE_BATCH_A: String = 'batch'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_W: String = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_A: String = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_SERVICE_W: String = 'service'
CRED_TARGETNAME_ATTRIBUTE_SERVICE_A: String = 'service'
CRED_TARGETNAME_ATTRIBUTE_NETWORK_W: String = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORK_A: String = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_W: String = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_A: String = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_W: String = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_A: String = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_W: String = 'cachedinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_A: String = 'cachedinteractive'
CRED_SESSION_WILDCARD_NAME: String = '*Session'
CRED_TARGETNAME_DOMAIN_NAMESPACE: String = 'Domain'
CRED_TARGETNAME_ATTRIBUTE_NAME: String = 'name'
CRED_TARGETNAME_ATTRIBUTE_TARGET: String = 'target'
CRED_TARGETNAME_ATTRIBUTE_BATCH: String = 'batch'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE: String = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_SERVICE: String = 'service'
CRED_TARGETNAME_ATTRIBUTE_NETWORK: String = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT: String = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE: String = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE: String = 'cachedinteractive'
CRED_LOGON_TYPES_MASK: UInt32 = 61440
CRED_TI_SERVER_FORMAT_UNKNOWN: UInt32 = 1
CRED_TI_DOMAIN_FORMAT_UNKNOWN: UInt32 = 2
CRED_TI_ONLY_PASSWORD_REQUIRED: UInt32 = 4
CRED_TI_USERNAME_TARGET: UInt32 = 8
CRED_TI_CREATE_EXPLICIT_CRED: UInt32 = 16
CRED_TI_WORKGROUP_MEMBER: UInt32 = 32
CRED_TI_DNSTREE_IS_DFS_SERVER: UInt32 = 64
CRED_TI_VALID_FLAGS: UInt32 = 61567
CERT_HASH_LENGTH: UInt32 = 20
CREDUI_MAX_MESSAGE_LENGTH: UInt32 = 1024
CREDUI_MAX_CAPTION_LENGTH: UInt32 = 128
CREDUI_MAX_GENERIC_TARGET_LENGTH: UInt32 = 32767
CREDUI_MAX_DOMAIN_TARGET_LENGTH: UInt32 = 337
CREDUI_MAX_USERNAME_LENGTH: UInt32 = 513
CREDUIWIN_IGNORE_CLOUDAUTHORITY_NAME: UInt32 = 262144
CREDUIWIN_DOWNLEVEL_HELLO_AS_SMART_CARD: UInt32 = 2147483648
CRED_PRESERVE_CREDENTIAL_BLOB: UInt32 = 1
CRED_CACHE_TARGET_INFORMATION: UInt32 = 1
CRED_ALLOW_NAME_RESOLUTION: UInt32 = 1
CRED_PROTECT_AS_SELF: UInt32 = 1
CRED_PROTECT_TO_SYSTEM: UInt32 = 2
CRED_UNPROTECT_AS_SELF: UInt32 = 1
CRED_UNPROTECT_ALLOW_TO_SYSTEM: UInt32 = 2
SCARD_SCOPE_TERMINAL: UInt32 = 1
SCARD_ALL_READERS: String = 'SCard$AllReaders\x0000'
SCARD_DEFAULT_READERS: String = 'SCard$DefaultReaders\x0000'
SCARD_LOCAL_READERS: String = 'SCard$LocalReaders\x0000'
SCARD_SYSTEM_READERS: String = 'SCard$SystemReaders\x0000'
SCARD_PROVIDER_PRIMARY: UInt32 = 1
SCARD_PROVIDER_CSP: UInt32 = 2
SCARD_PROVIDER_KSP: UInt32 = 3
SCARD_STATE_UNPOWERED: UInt32 = 1024
SCARD_SHARE_EXCLUSIVE: UInt32 = 1
SCARD_SHARE_SHARED: UInt32 = 2
SCARD_SHARE_DIRECT: UInt32 = 3
SCARD_LEAVE_CARD: UInt32 = 0
SCARD_RESET_CARD: UInt32 = 1
SCARD_UNPOWER_CARD: UInt32 = 2
SCARD_EJECT_CARD: UInt32 = 3
SC_DLG_MINIMAL_UI: UInt32 = 1
SC_DLG_NO_UI: UInt32 = 2
SC_DLG_FORCE_UI: UInt32 = 4
SCERR_NOCARDNAME: UInt32 = 16384
SCERR_NOGUIDS: UInt32 = 32768
SCARD_AUDIT_CHV_FAILURE: UInt32 = 0
SCARD_AUDIT_CHV_SUCCESS: UInt32 = 1
CREDSSP_NAME: String = 'CREDSSP'
TS_SSP_NAME_A: String = 'TSSSP'
TS_SSP_NAME: String = 'TSSSP'
szOID_TS_KP_TS_SERVER_AUTH: String = '1.3.6.1.4.1.311.54.1.2'
CREDSSP_SERVER_AUTH_NEGOTIATE: UInt32 = 1
CREDSSP_SERVER_AUTH_CERTIFICATE: UInt32 = 2
CREDSSP_SERVER_AUTH_LOOPBACK: UInt32 = 4
SECPKG_ALT_ATTR: UInt32 = 2147483648
SECPKG_ATTR_C_FULL_IDENT_TOKEN: UInt32 = 2147483781
CREDSSP_CRED_EX_VERSION: UInt32 = 0
CREDSSP_FLAG_REDIRECT: UInt32 = 1
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerGetOperationErrorStates(keyCredentialManagerOperationType: Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType, isReady: POINTER(Windows.Win32.Foundation.BOOL), keyCredentialManagerOperationErrorStates: POINTER(Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerShowUIOperation(hWndOwner: Windows.Win32.Foundation.HWND, keyCredentialManagerOperationType: Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerGetInformation(keyCredentialManagerInfo: POINTER(POINTER(Windows.Win32.Security.Credentials.KeyCredentialManagerInfo_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerFreeInformation(keyCredentialManagerInfo: POINTER(Windows.Win32.Security.Credentials.KeyCredentialManagerInfo_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def CredWriteW(Credential: POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredWriteA(Credential: POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadW(TargetName: Windows.Win32.Foundation.PWSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadA(TargetName: Windows.Win32.Foundation.PSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredEnumerateW(Filter: Windows.Win32.Foundation.PWSTR, Flags: Windows.Win32.Security.Credentials.CRED_ENUMERATE_FLAGS, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head)))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredEnumerateA(Filter: Windows.Win32.Foundation.PSTR, Flags: Windows.Win32.Security.Credentials.CRED_ENUMERATE_FLAGS, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head)))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredWriteDomainCredentialsW(TargetInfo: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head), Credential: POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredWriteDomainCredentialsA(TargetInfo: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head), Credential: POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadDomainCredentialsW(TargetInfo: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head), Flags: UInt32, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head)))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadDomainCredentialsA(TargetInfo: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head), Flags: UInt32, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head)))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredDeleteW(TargetName: Windows.Win32.Foundation.PWSTR, Type: UInt32, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredDeleteA(TargetName: Windows.Win32.Foundation.PSTR, Type: UInt32, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredRenameW(OldTargetName: Windows.Win32.Foundation.PWSTR, NewTargetName: Windows.Win32.Foundation.PWSTR, Type: UInt32, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredRenameA(OldTargetName: Windows.Win32.Foundation.PSTR, NewTargetName: Windows.Win32.Foundation.PSTR, Type: UInt32, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredGetTargetInfoW(TargetName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, TargetInfo: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredGetTargetInfoA(TargetName: Windows.Win32.Foundation.PSTR, Flags: UInt32, TargetInfo: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredMarshalCredentialW(CredType: Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE, Credential: c_void_p, MarshaledCredential: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredMarshalCredentialA(CredType: Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE, Credential: c_void_p, MarshaledCredential: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnmarshalCredentialW(MarshaledCredential: Windows.Win32.Foundation.PWSTR, CredType: POINTER(Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE), Credential: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnmarshalCredentialA(MarshaledCredential: Windows.Win32.Foundation.PSTR, CredType: POINTER(Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE), Credential: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsMarshaledCredentialW(MarshaledCredential: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsMarshaledCredentialA(MarshaledCredential: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredUnPackAuthenticationBufferW(dwFlags: Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, pszUserName: Windows.Win32.Foundation.PWSTR, pcchMaxUserName: POINTER(UInt32), pszDomainName: Windows.Win32.Foundation.PWSTR, pcchMaxDomainName: POINTER(UInt32), pszPassword: Windows.Win32.Foundation.PWSTR, pcchMaxPassword: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredUnPackAuthenticationBufferA(dwFlags: Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, pszUserName: Windows.Win32.Foundation.PSTR, pcchlMaxUserName: POINTER(UInt32), pszDomainName: Windows.Win32.Foundation.PSTR, pcchMaxDomainName: POINTER(UInt32), pszPassword: Windows.Win32.Foundation.PSTR, pcchMaxPassword: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredPackAuthenticationBufferW(dwFlags: Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pszUserName: Windows.Win32.Foundation.PWSTR, pszPassword: Windows.Win32.Foundation.PWSTR, pPackedCredentials: POINTER(Byte), pcbPackedCredentials: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredPackAuthenticationBufferA(dwFlags: Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pszUserName: Windows.Win32.Foundation.PSTR, pszPassword: Windows.Win32.Foundation.PSTR, pPackedCredentials: POINTER(Byte), pcbPackedCredentials: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredProtectW(fAsSelf: Windows.Win32.Foundation.BOOL, pszCredentials: Windows.Win32.Foundation.PWSTR, cchCredentials: UInt32, pszProtectedCredentials: Windows.Win32.Foundation.PWSTR, pcchMaxChars: POINTER(UInt32), ProtectionType: POINTER(Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredProtectA(fAsSelf: Windows.Win32.Foundation.BOOL, pszCredentials: Windows.Win32.Foundation.PSTR, cchCredentials: UInt32, pszProtectedCredentials: Windows.Win32.Foundation.PSTR, pcchMaxChars: POINTER(UInt32), ProtectionType: POINTER(Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnprotectW(fAsSelf: Windows.Win32.Foundation.BOOL, pszProtectedCredentials: Windows.Win32.Foundation.PWSTR, cchProtectedCredentials: UInt32, pszCredentials: Windows.Win32.Foundation.PWSTR, pcchMaxChars: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnprotectA(fAsSelf: Windows.Win32.Foundation.BOOL, pszProtectedCredentials: Windows.Win32.Foundation.PSTR, cchProtectedCredentials: UInt32, pszCredentials: Windows.Win32.Foundation.PSTR, pcchMaxChars: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsProtectedW(pszProtectedCredentials: Windows.Win32.Foundation.PWSTR, pProtectionType: POINTER(Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsProtectedA(pszProtectedCredentials: Windows.Win32.Foundation.PSTR, pProtectionType: POINTER(Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredFindBestCredentialW(TargetName: Windows.Win32.Foundation.PWSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALW_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredFindBestCredentialA(TargetName: Windows.Win32.Foundation.PSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(Windows.Win32.Security.Credentials.CREDENTIALA_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredGetSessionTypes(MaximumPersistCount: UInt32, MaximumPersist: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredFree(Buffer: c_void_p) -> Void: ...
@winfunctype('credui.dll')
def CredUIPromptForCredentialsW(pUiInfo: POINTER(Windows.Win32.Security.Credentials.CREDUI_INFOW_head), pszTargetName: Windows.Win32.Foundation.PWSTR, pContext: POINTER(Windows.Win32.Security.Credentials.SecHandle_head), dwAuthError: UInt32, pszUserName: Windows.Win32.Foundation.PWSTR, ulUserNameBufferSize: UInt32, pszPassword: Windows.Win32.Foundation.PWSTR, ulPasswordBufferSize: UInt32, save: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIPromptForCredentialsA(pUiInfo: POINTER(Windows.Win32.Security.Credentials.CREDUI_INFOA_head), pszTargetName: Windows.Win32.Foundation.PSTR, pContext: POINTER(Windows.Win32.Security.Credentials.SecHandle_head), dwAuthError: UInt32, pszUserName: Windows.Win32.Foundation.PSTR, ulUserNameBufferSize: UInt32, pszPassword: Windows.Win32.Foundation.PSTR, ulPasswordBufferSize: UInt32, save: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIPromptForWindowsCredentialsW(pUiInfo: POINTER(Windows.Win32.Security.Credentials.CREDUI_INFOW_head), dwAuthError: UInt32, pulAuthPackage: POINTER(UInt32), pvInAuthBuffer: c_void_p, ulInAuthBufferSize: UInt32, ppvOutAuthBuffer: POINTER(c_void_p), pulOutAuthBufferSize: POINTER(UInt32), pfSave: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIPromptForWindowsCredentialsA(pUiInfo: POINTER(Windows.Win32.Security.Credentials.CREDUI_INFOA_head), dwAuthError: UInt32, pulAuthPackage: POINTER(UInt32), pvInAuthBuffer: c_void_p, ulInAuthBufferSize: UInt32, ppvOutAuthBuffer: POINTER(c_void_p), pulOutAuthBufferSize: POINTER(UInt32), pfSave: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIParseUserNameW(UserName: Windows.Win32.Foundation.PWSTR, user: Windows.Win32.Foundation.PWSTR, userBufferSize: UInt32, domain: Windows.Win32.Foundation.PWSTR, domainBufferSize: UInt32) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIParseUserNameA(userName: Windows.Win32.Foundation.PSTR, user: Windows.Win32.Foundation.PSTR, userBufferSize: UInt32, domain: Windows.Win32.Foundation.PSTR, domainBufferSize: UInt32) -> UInt32: ...
@winfunctype('credui.dll')
def CredUICmdLinePromptForCredentialsW(pszTargetName: Windows.Win32.Foundation.PWSTR, pContext: POINTER(Windows.Win32.Security.Credentials.SecHandle_head), dwAuthError: UInt32, UserName: Windows.Win32.Foundation.PWSTR, ulUserBufferSize: UInt32, pszPassword: Windows.Win32.Foundation.PWSTR, ulPasswordBufferSize: UInt32, pfSave: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUICmdLinePromptForCredentialsA(pszTargetName: Windows.Win32.Foundation.PSTR, pContext: POINTER(Windows.Win32.Security.Credentials.SecHandle_head), dwAuthError: UInt32, UserName: Windows.Win32.Foundation.PSTR, ulUserBufferSize: UInt32, pszPassword: Windows.Win32.Foundation.PSTR, ulPasswordBufferSize: UInt32, pfSave: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIConfirmCredentialsW(pszTargetName: Windows.Win32.Foundation.PWSTR, bConfirm: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIConfirmCredentialsA(pszTargetName: Windows.Win32.Foundation.PSTR, bConfirm: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIStoreSSOCredW(pszRealm: Windows.Win32.Foundation.PWSTR, pszUsername: Windows.Win32.Foundation.PWSTR, pszPassword: Windows.Win32.Foundation.PWSTR, bPersist: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIReadSSOCredW(pszRealm: Windows.Win32.Foundation.PWSTR, ppszUsername: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('WinSCard.dll')
def SCardEstablishContext(dwScope: Windows.Win32.Security.Credentials.SCARD_SCOPE, pvReserved1: c_void_p, pvReserved2: c_void_p, phContext: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReleaseContext(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIsValidContext(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReaderGroupsA(hContext: UIntPtr, mszGroups: Windows.Win32.Foundation.PSTR, pcchGroups: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReaderGroupsW(hContext: UIntPtr, mszGroups: Windows.Win32.Foundation.PWSTR, pcchGroups: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersA(hContext: UIntPtr, mszGroups: Windows.Win32.Foundation.PSTR, mszReaders: Windows.Win32.Foundation.PSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersW(hContext: UIntPtr, mszGroups: Windows.Win32.Foundation.PWSTR, mszReaders: Windows.Win32.Foundation.PWSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListCardsA(hContext: UIntPtr, pbAtr: POINTER(Byte), rgquidInterfaces: POINTER(Guid), cguidInterfaceCount: UInt32, mszCards: Windows.Win32.Foundation.PSTR, pcchCards: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListCardsW(hContext: UIntPtr, pbAtr: POINTER(Byte), rgquidInterfaces: POINTER(Guid), cguidInterfaceCount: UInt32, mszCards: Windows.Win32.Foundation.PWSTR, pcchCards: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListInterfacesA(hContext: UIntPtr, szCard: Windows.Win32.Foundation.PSTR, pguidInterfaces: POINTER(Guid), pcguidInterfaces: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListInterfacesW(hContext: UIntPtr, szCard: Windows.Win32.Foundation.PWSTR, pguidInterfaces: POINTER(Guid), pcguidInterfaces: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetProviderIdA(hContext: UIntPtr, szCard: Windows.Win32.Foundation.PSTR, pguidProviderId: POINTER(Guid)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetProviderIdW(hContext: UIntPtr, szCard: Windows.Win32.Foundation.PWSTR, pguidProviderId: POINTER(Guid)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetCardTypeProviderNameA(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PSTR, dwProviderId: UInt32, szProvider: Windows.Win32.Foundation.PSTR, pcchProvider: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetCardTypeProviderNameW(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PWSTR, dwProviderId: UInt32, szProvider: Windows.Win32.Foundation.PWSTR, pcchProvider: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderGroupA(hContext: UIntPtr, szGroupName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderGroupW(hContext: UIntPtr, szGroupName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderGroupA(hContext: UIntPtr, szGroupName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderGroupW(hContext: UIntPtr, szGroupName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, szDeviceName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, szDeviceName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAddReaderToGroupA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, szGroupName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAddReaderToGroupW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, szGroupName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardRemoveReaderFromGroupA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, szGroupName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardRemoveReaderFromGroupW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, szGroupName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceCardTypeA(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PSTR, pguidPrimaryProvider: POINTER(Guid), rgguidInterfaces: POINTER(Guid), dwInterfaceCount: UInt32, pbAtr: POINTER(Byte), pbAtrMask: POINTER(Byte), cbAtrLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceCardTypeW(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PWSTR, pguidPrimaryProvider: POINTER(Guid), rgguidInterfaces: POINTER(Guid), dwInterfaceCount: UInt32, pbAtr: POINTER(Byte), pbAtrMask: POINTER(Byte), cbAtrLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardSetCardTypeProviderNameA(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PSTR, dwProviderId: UInt32, szProvider: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardSetCardTypeProviderNameW(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PWSTR, dwProviderId: UInt32, szProvider: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetCardTypeA(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetCardTypeW(hContext: UIntPtr, szCardName: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardFreeMemory(hContext: UIntPtr, pvMem: c_void_p) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAccessStartedEvent() -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WinSCard.dll')
def SCardReleaseStartedEvent() -> Void: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsA(hContext: UIntPtr, mszCards: Windows.Win32.Foundation.PSTR, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEA_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsW(hContext: UIntPtr, mszCards: Windows.Win32.Foundation.PWSTR, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEW_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsByATRA(hContext: UIntPtr, rgAtrMasks: POINTER(Windows.Win32.Security.Credentials.SCARD_ATRMASK_head), cAtrs: UInt32, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEA_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsByATRW(hContext: UIntPtr, rgAtrMasks: POINTER(Windows.Win32.Security.Credentials.SCARD_ATRMASK_head), cAtrs: UInt32, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEW_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetStatusChangeA(hContext: UIntPtr, dwTimeout: UInt32, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEA_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetStatusChangeW(hContext: UIntPtr, dwTimeout: UInt32, rgReaderStates: POINTER(Windows.Win32.Security.Credentials.SCARD_READERSTATEW_head), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardCancel(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardConnectA(hContext: UIntPtr, szReader: Windows.Win32.Foundation.PSTR, dwShareMode: UInt32, dwPreferredProtocols: UInt32, phCard: POINTER(UIntPtr), pdwActiveProtocol: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardConnectW(hContext: UIntPtr, szReader: Windows.Win32.Foundation.PWSTR, dwShareMode: UInt32, dwPreferredProtocols: UInt32, phCard: POINTER(UIntPtr), pdwActiveProtocol: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReconnect(hCard: UIntPtr, dwShareMode: UInt32, dwPreferredProtocols: UInt32, dwInitialization: UInt32, pdwActiveProtocol: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardDisconnect(hCard: UIntPtr, dwDisposition: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardBeginTransaction(hCard: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardEndTransaction(hCard: UIntPtr, dwDisposition: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardState(hCard: UIntPtr, pdwState: POINTER(UInt32), pdwProtocol: POINTER(UInt32), pbAtr: POINTER(Byte), pcbAtrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardStatusA(hCard: UIntPtr, mszReaderNames: Windows.Win32.Foundation.PSTR, pcchReaderLen: POINTER(UInt32), pdwState: POINTER(UInt32), pdwProtocol: POINTER(UInt32), pbAtr: POINTER(Byte), pcbAtrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardStatusW(hCard: UIntPtr, mszReaderNames: Windows.Win32.Foundation.PWSTR, pcchReaderLen: POINTER(UInt32), pdwState: POINTER(UInt32), pdwProtocol: POINTER(UInt32), pbAtr: POINTER(Byte), pcbAtrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardTransmit(hCard: UIntPtr, pioSendPci: POINTER(Windows.Win32.Security.Credentials.SCARD_IO_REQUEST_head), pbSendBuffer: POINTER(Byte), cbSendLength: UInt32, pioRecvPci: POINTER(Windows.Win32.Security.Credentials.SCARD_IO_REQUEST_head), pbRecvBuffer: POINTER(Byte), pcbRecvLength: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetTransmitCount(hCard: UIntPtr, pcTransmitCount: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardControl(hCard: UIntPtr, dwControlCode: UInt32, lpInBuffer: c_void_p, cbInBufferSize: UInt32, lpOutBuffer: c_void_p, cbOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetAttrib(hCard: UIntPtr, dwAttrId: UInt32, pbAttr: POINTER(Byte), pcbAttrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardSetAttrib(hCard: UIntPtr, dwAttrId: UInt32, pbAttr: POINTER(Byte), cbAttrLen: UInt32) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def SCardUIDlgSelectCardA(param0: POINTER(Windows.Win32.Security.Credentials.OPENCARDNAME_EXA_head)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def SCardUIDlgSelectCardW(param0: POINTER(Windows.Win32.Security.Credentials.OPENCARDNAME_EXW_head)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def GetOpenCardNameA(param0: POINTER(Windows.Win32.Security.Credentials.OPENCARDNAMEA_head)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def GetOpenCardNameW(param0: POINTER(Windows.Win32.Security.Credentials.OPENCARDNAMEW_head)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def SCardDlgExtendedError() -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReadCacheA(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: Windows.Win32.Foundation.PSTR, Data: POINTER(Byte), DataLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReadCacheW(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: Windows.Win32.Foundation.PWSTR, Data: POINTER(Byte), DataLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardWriteCacheA(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: Windows.Win32.Foundation.PSTR, Data: POINTER(Byte), DataLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardWriteCacheW(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: Windows.Win32.Foundation.PWSTR, Data: POINTER(Byte), DataLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderIconA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, pbIcon: POINTER(Byte), pcbIcon: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderIconW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, pbIcon: POINTER(Byte), pcbIcon: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetDeviceTypeIdA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, pdwDeviceTypeId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetDeviceTypeIdW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, pdwDeviceTypeId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderDeviceInstanceIdA(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PSTR, szDeviceInstanceId: Windows.Win32.Foundation.PSTR, pcchDeviceInstanceId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderDeviceInstanceIdW(hContext: UIntPtr, szReaderName: Windows.Win32.Foundation.PWSTR, szDeviceInstanceId: Windows.Win32.Foundation.PWSTR, pcchDeviceInstanceId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersWithDeviceInstanceIdA(hContext: UIntPtr, szDeviceInstanceId: Windows.Win32.Foundation.PSTR, mszReaders: Windows.Win32.Foundation.PSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersWithDeviceInstanceIdW(hContext: UIntPtr, szDeviceInstanceId: Windows.Win32.Foundation.PWSTR, mszReaders: Windows.Win32.Foundation.PWSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAudit(hContext: UIntPtr, dwEvent: UInt32) -> Int32: ...
class BINARY_BLOB_CREDENTIAL_INFO(EasyCastStructure):
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
class CERT_CREDENTIAL_INFO(EasyCastStructure):
    cbSize: UInt32
    rgbHashOfCert: Byte * 20
class CREDENTIALA(EasyCastStructure):
    Flags: Windows.Win32.Security.Credentials.CRED_FLAGS
    Type: Windows.Win32.Security.Credentials.CRED_TYPE
    TargetName: Windows.Win32.Foundation.PSTR
    Comment: Windows.Win32.Foundation.PSTR
    LastWritten: Windows.Win32.Foundation.FILETIME
    CredentialBlobSize: UInt32
    CredentialBlob: POINTER(Byte)
    Persist: Windows.Win32.Security.Credentials.CRED_PERSIST
    AttributeCount: UInt32
    Attributes: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_ATTRIBUTEA_head)
    TargetAlias: Windows.Win32.Foundation.PSTR
    UserName: Windows.Win32.Foundation.PSTR
class CREDENTIALW(EasyCastStructure):
    Flags: Windows.Win32.Security.Credentials.CRED_FLAGS
    Type: Windows.Win32.Security.Credentials.CRED_TYPE
    TargetName: Windows.Win32.Foundation.PWSTR
    Comment: Windows.Win32.Foundation.PWSTR
    LastWritten: Windows.Win32.Foundation.FILETIME
    CredentialBlobSize: UInt32
    CredentialBlob: POINTER(Byte)
    Persist: Windows.Win32.Security.Credentials.CRED_PERSIST
    AttributeCount: UInt32
    Attributes: POINTER(Windows.Win32.Security.Credentials.CREDENTIAL_ATTRIBUTEW_head)
    TargetAlias: Windows.Win32.Foundation.PWSTR
    UserName: Windows.Win32.Foundation.PWSTR
class CREDENTIAL_ATTRIBUTEA(EasyCastStructure):
    Keyword: Windows.Win32.Foundation.PSTR
    Flags: UInt32
    ValueSize: UInt32
    Value: POINTER(Byte)
class CREDENTIAL_ATTRIBUTEW(EasyCastStructure):
    Keyword: Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    ValueSize: UInt32
    Value: POINTER(Byte)
class CREDENTIAL_TARGET_INFORMATIONA(EasyCastStructure):
    TargetName: Windows.Win32.Foundation.PSTR
    NetbiosServerName: Windows.Win32.Foundation.PSTR
    DnsServerName: Windows.Win32.Foundation.PSTR
    NetbiosDomainName: Windows.Win32.Foundation.PSTR
    DnsDomainName: Windows.Win32.Foundation.PSTR
    DnsTreeName: Windows.Win32.Foundation.PSTR
    PackageName: Windows.Win32.Foundation.PSTR
    Flags: UInt32
    CredTypeCount: UInt32
    CredTypes: POINTER(UInt32)
class CREDENTIAL_TARGET_INFORMATIONW(EasyCastStructure):
    TargetName: Windows.Win32.Foundation.PWSTR
    NetbiosServerName: Windows.Win32.Foundation.PWSTR
    DnsServerName: Windows.Win32.Foundation.PWSTR
    NetbiosDomainName: Windows.Win32.Foundation.PWSTR
    DnsDomainName: Windows.Win32.Foundation.PWSTR
    DnsTreeName: Windows.Win32.Foundation.PWSTR
    PackageName: Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    CredTypeCount: UInt32
    CredTypes: POINTER(UInt32)
CREDSPP_SUBMIT_TYPE = Int32
CREDSPP_SUBMIT_TYPE_CredsspPasswordCreds: CREDSPP_SUBMIT_TYPE = 2
CREDSPP_SUBMIT_TYPE_CredsspSchannelCreds: CREDSPP_SUBMIT_TYPE = 4
CREDSPP_SUBMIT_TYPE_CredsspCertificateCreds: CREDSPP_SUBMIT_TYPE = 13
CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBoth: CREDSPP_SUBMIT_TYPE = 50
CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBothOld: CREDSPP_SUBMIT_TYPE = 51
CREDSPP_SUBMIT_TYPE_CredsspCredEx: CREDSPP_SUBMIT_TYPE = 100
class CREDSSP_CRED(EasyCastStructure):
    Type: Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE
    pSchannelCred: c_void_p
    pSpnegoCred: c_void_p
class CREDSSP_CRED_EX(EasyCastStructure):
    Type: Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE
    Version: UInt32
    Flags: UInt32
    Reserved: UInt32
    Cred: Windows.Win32.Security.Credentials.CREDSSP_CRED
CREDUIWIN_FLAGS = UInt32
CREDUIWIN_GENERIC: CREDUIWIN_FLAGS = 1
CREDUIWIN_CHECKBOX: CREDUIWIN_FLAGS = 2
CREDUIWIN_AUTHPACKAGE_ONLY: CREDUIWIN_FLAGS = 16
CREDUIWIN_IN_CRED_ONLY: CREDUIWIN_FLAGS = 32
CREDUIWIN_ENUMERATE_ADMINS: CREDUIWIN_FLAGS = 256
CREDUIWIN_ENUMERATE_CURRENT_USER: CREDUIWIN_FLAGS = 512
CREDUIWIN_SECURE_PROMPT: CREDUIWIN_FLAGS = 4096
CREDUIWIN_PREPROMPTING: CREDUIWIN_FLAGS = 8192
CREDUIWIN_PACK_32_WOW: CREDUIWIN_FLAGS = 268435456
CREDUI_FLAGS = UInt32
CREDUI_FLAGS_ALWAYS_SHOW_UI: CREDUI_FLAGS = 128
CREDUI_FLAGS_COMPLETE_USERNAME: CREDUI_FLAGS = 2048
CREDUI_FLAGS_DO_NOT_PERSIST: CREDUI_FLAGS = 2
CREDUI_FLAGS_EXCLUDE_CERTIFICATES: CREDUI_FLAGS = 8
CREDUI_FLAGS_EXPECT_CONFIRMATION: CREDUI_FLAGS = 131072
CREDUI_FLAGS_GENERIC_CREDENTIALS: CREDUI_FLAGS = 262144
CREDUI_FLAGS_INCORRECT_PASSWORD: CREDUI_FLAGS = 1
CREDUI_FLAGS_KEEP_USERNAME: CREDUI_FLAGS = 1048576
CREDUI_FLAGS_PASSWORD_ONLY_OK: CREDUI_FLAGS = 512
CREDUI_FLAGS_PERSIST: CREDUI_FLAGS = 4096
CREDUI_FLAGS_REQUEST_ADMINISTRATOR: CREDUI_FLAGS = 4
CREDUI_FLAGS_REQUIRE_CERTIFICATE: CREDUI_FLAGS = 16
CREDUI_FLAGS_REQUIRE_SMARTCARD: CREDUI_FLAGS = 256
CREDUI_FLAGS_SERVER_CREDENTIAL: CREDUI_FLAGS = 16384
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX: CREDUI_FLAGS = 64
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS: CREDUI_FLAGS = 524288
CREDUI_FLAGS_VALIDATE_USERNAME: CREDUI_FLAGS = 1024
class CREDUI_INFOA(EasyCastStructure):
    cbSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    pszMessageText: Windows.Win32.Foundation.PSTR
    pszCaptionText: Windows.Win32.Foundation.PSTR
    hbmBanner: Windows.Win32.Graphics.Gdi.HBITMAP
class CREDUI_INFOW(EasyCastStructure):
    cbSize: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    pszMessageText: Windows.Win32.Foundation.PWSTR
    pszCaptionText: Windows.Win32.Foundation.PWSTR
    hbmBanner: Windows.Win32.Graphics.Gdi.HBITMAP
CRED_ENUMERATE_FLAGS = UInt32
CRED_ENUMERATE_ALL_CREDENTIALS: CRED_ENUMERATE_FLAGS = 1
CRED_FLAGS = UInt32
CRED_FLAGS_PASSWORD_FOR_CERT: CRED_FLAGS = 1
CRED_FLAGS_PROMPT_NOW: CRED_FLAGS = 2
CRED_FLAGS_USERNAME_TARGET: CRED_FLAGS = 4
CRED_FLAGS_OWF_CRED_BLOB: CRED_FLAGS = 8
CRED_FLAGS_REQUIRE_CONFIRMATION: CRED_FLAGS = 16
CRED_FLAGS_WILDCARD_MATCH: CRED_FLAGS = 32
CRED_FLAGS_VSM_PROTECTED: CRED_FLAGS = 64
CRED_FLAGS_NGC_CERT: CRED_FLAGS = 128
CRED_FLAGS_VALID_FLAGS: CRED_FLAGS = 61695
CRED_FLAGS_VALID_INPUT_FLAGS: CRED_FLAGS = 61599
CRED_MARSHAL_TYPE = Int32
CRED_MARSHAL_TYPE_CertCredential: CRED_MARSHAL_TYPE = 1
CRED_MARSHAL_TYPE_UsernameTargetCredential: CRED_MARSHAL_TYPE = 2
CRED_MARSHAL_TYPE_BinaryBlobCredential: CRED_MARSHAL_TYPE = 3
CRED_MARSHAL_TYPE_UsernameForPackedCredentials: CRED_MARSHAL_TYPE = 4
CRED_MARSHAL_TYPE_BinaryBlobForSystem: CRED_MARSHAL_TYPE = 5
CRED_PACK_FLAGS = UInt32
CRED_PACK_PROTECTED_CREDENTIALS: CRED_PACK_FLAGS = 1
CRED_PACK_WOW_BUFFER: CRED_PACK_FLAGS = 2
CRED_PACK_GENERIC_CREDENTIALS: CRED_PACK_FLAGS = 4
CRED_PACK_ID_PROVIDER_CREDENTIALS: CRED_PACK_FLAGS = 8
CRED_PERSIST = UInt32
CRED_PERSIST_NONE: CRED_PERSIST = 0
CRED_PERSIST_SESSION: CRED_PERSIST = 1
CRED_PERSIST_LOCAL_MACHINE: CRED_PERSIST = 2
CRED_PERSIST_ENTERPRISE: CRED_PERSIST = 3
CRED_PROTECTION_TYPE = Int32
CRED_PROTECTION_TYPE_CredUnprotected: CRED_PROTECTION_TYPE = 0
CRED_PROTECTION_TYPE_CredUserProtection: CRED_PROTECTION_TYPE = 1
CRED_PROTECTION_TYPE_CredTrustedProtection: CRED_PROTECTION_TYPE = 2
CRED_PROTECTION_TYPE_CredForSystemProtection: CRED_PROTECTION_TYPE = 3
CRED_TYPE = UInt32
CRED_TYPE_GENERIC: CRED_TYPE = 1
CRED_TYPE_DOMAIN_PASSWORD: CRED_TYPE = 2
CRED_TYPE_DOMAIN_CERTIFICATE: CRED_TYPE = 3
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD: CRED_TYPE = 4
CRED_TYPE_GENERIC_CERTIFICATE: CRED_TYPE = 5
CRED_TYPE_DOMAIN_EXTENDED: CRED_TYPE = 6
CRED_TYPE_MAXIMUM: CRED_TYPE = 7
CRED_TYPE_MAXIMUM_EX: CRED_TYPE = 1007
class KeyCredentialManagerInfo(EasyCastStructure):
    containerId: Guid
KeyCredentialManagerOperationErrorStates = Int32
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateNone: KeyCredentialManagerOperationErrorStates = 0
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateDeviceJoinFailure: KeyCredentialManagerOperationErrorStates = 1
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateTokenFailure: KeyCredentialManagerOperationErrorStates = 2
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateCertificateFailure: KeyCredentialManagerOperationErrorStates = 4
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateRemoteSessionFailure: KeyCredentialManagerOperationErrorStates = 8
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePolicyFailure: KeyCredentialManagerOperationErrorStates = 16
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateHardwareFailure: KeyCredentialManagerOperationErrorStates = 32
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePinExistsFailure: KeyCredentialManagerOperationErrorStates = 64
KeyCredentialManagerOperationType = Int32
KeyCredentialManagerOperationType_KeyCredentialManagerProvisioning: KeyCredentialManagerOperationType = 0
KeyCredentialManagerOperationType_KeyCredentialManagerPinChange: KeyCredentialManagerOperationType = 1
KeyCredentialManagerOperationType_KeyCredentialManagerPinReset: KeyCredentialManagerOperationType = 2
@winfunctype_pointer
def LPOCNCHKPROC(param0: UIntPtr, param1: UIntPtr, param2: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPOCNCONNPROCA(param0: UIntPtr, param1: Windows.Win32.Foundation.PSTR, param2: Windows.Win32.Foundation.PSTR, param3: c_void_p) -> UIntPtr: ...
@winfunctype_pointer
def LPOCNCONNPROCW(param0: UIntPtr, param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, param3: c_void_p) -> UIntPtr: ...
@winfunctype_pointer
def LPOCNDSCPROC(param0: UIntPtr, param1: UIntPtr, param2: c_void_p) -> Void: ...
class OPENCARDNAMEA(EasyCastStructure):
    dwStructSize: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    hSCardContext: UIntPtr
    lpstrGroupNames: Windows.Win32.Foundation.PSTR
    nMaxGroupNames: UInt32
    lpstrCardNames: Windows.Win32.Foundation.PSTR
    nMaxCardNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrRdr: Windows.Win32.Foundation.PSTR
    nMaxRdr: UInt32
    lpstrCard: Windows.Win32.Foundation.PSTR
    nMaxCard: UInt32
    lpstrTitle: Windows.Win32.Foundation.PSTR
    dwFlags: UInt32
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    dwActiveProtocol: UInt32
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    lpfnCheck: Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnDisconnect: Windows.Win32.Security.Credentials.LPOCNDSCPROC
    hCardHandle: UIntPtr
class OPENCARDNAMEW(EasyCastStructure):
    dwStructSize: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    hSCardContext: UIntPtr
    lpstrGroupNames: Windows.Win32.Foundation.PWSTR
    nMaxGroupNames: UInt32
    lpstrCardNames: Windows.Win32.Foundation.PWSTR
    nMaxCardNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrRdr: Windows.Win32.Foundation.PWSTR
    nMaxRdr: UInt32
    lpstrCard: Windows.Win32.Foundation.PWSTR
    nMaxCard: UInt32
    lpstrTitle: Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    dwActiveProtocol: UInt32
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    lpfnCheck: Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnDisconnect: Windows.Win32.Security.Credentials.LPOCNDSCPROC
    hCardHandle: UIntPtr
class OPENCARDNAME_EXA(EasyCastStructure):
    dwStructSize: UInt32
    hSCardContext: UIntPtr
    hwndOwner: Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    lpstrTitle: Windows.Win32.Foundation.PSTR
    lpstrSearchDesc: Windows.Win32.Foundation.PSTR
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    pOpenCardSearchCriteria: POINTER(Windows.Win32.Security.Credentials.OPENCARD_SEARCH_CRITERIAA_head)
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    lpstrRdr: Windows.Win32.Foundation.PSTR
    nMaxRdr: UInt32
    lpstrCard: Windows.Win32.Foundation.PSTR
    nMaxCard: UInt32
    dwActiveProtocol: UInt32
    hCardHandle: UIntPtr
class OPENCARDNAME_EXW(EasyCastStructure):
    dwStructSize: UInt32
    hSCardContext: UIntPtr
    hwndOwner: Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    lpstrTitle: Windows.Win32.Foundation.PWSTR
    lpstrSearchDesc: Windows.Win32.Foundation.PWSTR
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    pOpenCardSearchCriteria: POINTER(Windows.Win32.Security.Credentials.OPENCARD_SEARCH_CRITERIAW_head)
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    lpstrRdr: Windows.Win32.Foundation.PWSTR
    nMaxRdr: UInt32
    lpstrCard: Windows.Win32.Foundation.PWSTR
    nMaxCard: UInt32
    dwActiveProtocol: UInt32
    hCardHandle: UIntPtr
class OPENCARD_SEARCH_CRITERIAA(EasyCastStructure):
    dwStructSize: UInt32
    lpstrGroupNames: Windows.Win32.Foundation.PSTR
    nMaxGroupNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrCardNames: Windows.Win32.Foundation.PSTR
    nMaxCardNames: UInt32
    lpfnCheck: Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    lpfnDisconnect: Windows.Win32.Security.Credentials.LPOCNDSCPROC
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
class OPENCARD_SEARCH_CRITERIAW(EasyCastStructure):
    dwStructSize: UInt32
    lpstrGroupNames: Windows.Win32.Foundation.PWSTR
    nMaxGroupNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrCardNames: Windows.Win32.Foundation.PWSTR
    nMaxCardNames: UInt32
    lpfnCheck: Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnConnect: Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    lpfnDisconnect: Windows.Win32.Security.Credentials.LPOCNDSCPROC
    pvUserData: c_void_p
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
class READER_SEL_REQUEST(EasyCastStructure):
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    MatchType: Windows.Win32.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        ReaderAndContainerParameter: _ReaderAndContainerParameter_e__Struct
        SerialNumberParameter: _SerialNumberParameter_e__Struct
        class _ReaderAndContainerParameter_e__Struct(EasyCastStructure):
            cbReaderNameOffset: UInt32
            cchReaderNameLength: UInt32
            cbContainerNameOffset: UInt32
            cchContainerNameLength: UInt32
            dwDesiredCardModuleVersion: UInt32
            dwCspFlags: UInt32
        class _SerialNumberParameter_e__Struct(EasyCastStructure):
            cbSerialNumberOffset: UInt32
            cbSerialNumberLength: UInt32
            dwDesiredCardModuleVersion: UInt32
READER_SEL_REQUEST_MATCH_TYPE = Int32
RSR_MATCH_TYPE_READER_AND_CONTAINER: READER_SEL_REQUEST_MATCH_TYPE = 1
RSR_MATCH_TYPE_SERIAL_NUMBER: READER_SEL_REQUEST_MATCH_TYPE = 2
RSR_MATCH_TYPE_ALL_CARDS: READER_SEL_REQUEST_MATCH_TYPE = 3
class READER_SEL_RESPONSE(EasyCastStructure):
    cbReaderNameOffset: UInt32
    cchReaderNameLength: UInt32
    cbCardNameOffset: UInt32
    cchCardNameLength: UInt32
class SCARD_ATRMASK(EasyCastStructure):
    cbAtr: UInt32
    rgbAtr: Byte * 36
    rgbMask: Byte * 36
class SCARD_IO_REQUEST(EasyCastStructure):
    dwProtocol: UInt32
    cbPciLength: UInt32
class SCARD_READERSTATEA(EasyCastStructure):
    szReader: Windows.Win32.Foundation.PSTR
    pvUserData: c_void_p
    dwCurrentState: Windows.Win32.Security.Credentials.SCARD_STATE
    dwEventState: Windows.Win32.Security.Credentials.SCARD_STATE
    cbAtr: UInt32
    rgbAtr: Byte * 36
class SCARD_READERSTATEW(EasyCastStructure):
    szReader: Windows.Win32.Foundation.PWSTR
    pvUserData: c_void_p
    dwCurrentState: Windows.Win32.Security.Credentials.SCARD_STATE
    dwEventState: Windows.Win32.Security.Credentials.SCARD_STATE
    cbAtr: UInt32
    rgbAtr: Byte * 36
SCARD_SCOPE = UInt32
SCARD_SCOPE_USER: SCARD_SCOPE = 0
SCARD_SCOPE_SYSTEM: SCARD_SCOPE = 2
SCARD_STATE = UInt32
SCARD_STATE_UNAWARE: SCARD_STATE = 0
SCARD_STATE_IGNORE: SCARD_STATE = 1
SCARD_STATE_UNAVAILABLE: SCARD_STATE = 8
SCARD_STATE_EMPTY: SCARD_STATE = 16
SCARD_STATE_PRESENT: SCARD_STATE = 32
SCARD_STATE_ATRMATCH: SCARD_STATE = 64
SCARD_STATE_EXCLUSIVE: SCARD_STATE = 128
SCARD_STATE_INUSE: SCARD_STATE = 256
SCARD_STATE_MUTE: SCARD_STATE = 512
SCARD_STATE_CHANGED: SCARD_STATE = 2
SCARD_STATE_UNKNOWN: SCARD_STATE = 4
class SCARD_T0_COMMAND(EasyCastStructure):
    bCla: Byte
    bIns: Byte
    bP1: Byte
    bP2: Byte
    bP3: Byte
class SCARD_T0_REQUEST(EasyCastStructure):
    ioRequest: Windows.Win32.Security.Credentials.SCARD_IO_REQUEST
    bSw1: Byte
    bSw2: Byte
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        CmdBytes: Windows.Win32.Security.Credentials.SCARD_T0_COMMAND
        rgbHeader: Byte * 5
class SCARD_T1_REQUEST(EasyCastStructure):
    ioRequest: Windows.Win32.Security.Credentials.SCARD_IO_REQUEST
class SecHandle(EasyCastStructure):
    dwLower: UIntPtr
    dwUpper: UIntPtr
class SecPkgContext_ClientCreds(EasyCastStructure):
    AuthBufferLen: UInt32
    AuthBuffer: POINTER(Byte)
class USERNAME_TARGET_CREDENTIAL_INFO(EasyCastStructure):
    UserName: Windows.Win32.Foundation.PWSTR
make_head(_module, 'BINARY_BLOB_CREDENTIAL_INFO')
make_head(_module, 'CERT_CREDENTIAL_INFO')
make_head(_module, 'CREDENTIALA')
make_head(_module, 'CREDENTIALW')
make_head(_module, 'CREDENTIAL_ATTRIBUTEA')
make_head(_module, 'CREDENTIAL_ATTRIBUTEW')
make_head(_module, 'CREDENTIAL_TARGET_INFORMATIONA')
make_head(_module, 'CREDENTIAL_TARGET_INFORMATIONW')
make_head(_module, 'CREDSSP_CRED')
make_head(_module, 'CREDSSP_CRED_EX')
make_head(_module, 'CREDUI_INFOA')
make_head(_module, 'CREDUI_INFOW')
make_head(_module, 'KeyCredentialManagerInfo')
make_head(_module, 'LPOCNCHKPROC')
make_head(_module, 'LPOCNCONNPROCA')
make_head(_module, 'LPOCNCONNPROCW')
make_head(_module, 'LPOCNDSCPROC')
make_head(_module, 'OPENCARDNAMEA')
make_head(_module, 'OPENCARDNAMEW')
make_head(_module, 'OPENCARDNAME_EXA')
make_head(_module, 'OPENCARDNAME_EXW')
make_head(_module, 'OPENCARD_SEARCH_CRITERIAA')
make_head(_module, 'OPENCARD_SEARCH_CRITERIAW')
make_head(_module, 'READER_SEL_REQUEST')
make_head(_module, 'READER_SEL_RESPONSE')
make_head(_module, 'SCARD_ATRMASK')
make_head(_module, 'SCARD_IO_REQUEST')
make_head(_module, 'SCARD_READERSTATEA')
make_head(_module, 'SCARD_READERSTATEW')
make_head(_module, 'SCARD_T0_COMMAND')
make_head(_module, 'SCARD_T0_REQUEST')
make_head(_module, 'SCARD_T1_REQUEST')
make_head(_module, 'SecHandle')
make_head(_module, 'SecPkgContext_ClientCreds')
make_head(_module, 'USERNAME_TARGET_CREDENTIAL_INFO')
