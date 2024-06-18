from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security.Credentials
import win32more.Windows.Win32.UI.WindowsAndMessaging
CRED_MAX_CREDENTIAL_BLOB_SIZE: UInt32 = 2560
CRED_MAX_USERNAME_LENGTH: UInt32 = 513
CRED_MAX_DOMAIN_TARGET_NAME_LENGTH: UInt32 = 337
FILE_DEVICE_SMARTCARD: UInt32 = 49
GUID_DEVINTERFACE_SMARTCARD_READER: Guid = Guid('{50dd5230-ba8a-11d1-bf5d-0000f805f530}')
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
STATUS_LOGON_FAILURE: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741715
STATUS_WRONG_PASSWORD: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741718
STATUS_PASSWORD_EXPIRED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741711
STATUS_PASSWORD_MUST_CHANGE: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741276
STATUS_DOWNGRADE_DETECTED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073740920
STATUS_AUTHENTICATION_FIREWALL_FAILED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073740781
STATUS_ACCOUNT_DISABLED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741710
STATUS_ACCOUNT_RESTRICTION: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741714
STATUS_ACCOUNT_LOCKED_OUT: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741260
STATUS_ACCOUNT_EXPIRED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741421
STATUS_LOGON_TYPE_NOT_GRANTED: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741477
STATUS_NO_SUCH_LOGON_SESSION: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741729
STATUS_NO_SUCH_USER: win32more.Windows.Win32.Foundation.NTSTATUS = -1073741724
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
def KeyCredentialManagerGetOperationErrorStates(keyCredentialManagerOperationType: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType, isReady: POINTER(win32more.Windows.Win32.Foundation.BOOL), keyCredentialManagerOperationErrorStates: POINTER(win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerShowUIOperation(hWndOwner: win32more.Windows.Win32.Foundation.HWND, keyCredentialManagerOperationType: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerGetInformation(keyCredentialManagerInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerInfo))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KeyCredMgr.dll')
def KeyCredentialManagerFreeInformation(keyCredentialManagerInfo: POINTER(win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerInfo)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def CredWriteW(Credential: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredWrite = UnicodeAlias('CredWriteW')
@winfunctype('ADVAPI32.dll')
def CredWriteA(Credential: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32, Credential: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredRead = UnicodeAlias('CredReadW')
@winfunctype('ADVAPI32.dll')
def CredReadA(TargetName: win32more.Windows.Win32.Foundation.PSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32, Credential: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredEnumerateW(Filter: win32more.Windows.Win32.Foundation.PWSTR, Flags: win32more.Windows.Win32.Security.Credentials.CRED_ENUMERATE_FLAGS, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW)))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredEnumerate = UnicodeAlias('CredEnumerateW')
@winfunctype('ADVAPI32.dll')
def CredEnumerateA(Filter: win32more.Windows.Win32.Foundation.PSTR, Flags: win32more.Windows.Win32.Security.Credentials.CRED_ENUMERATE_FLAGS, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA)))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredWriteDomainCredentialsW(TargetInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW), Credential: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredWriteDomainCredentials = UnicodeAlias('CredWriteDomainCredentialsW')
@winfunctype('ADVAPI32.dll')
def CredWriteDomainCredentialsA(TargetInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA), Credential: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredReadDomainCredentialsW(TargetInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW), Flags: UInt32, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW)))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredReadDomainCredentials = UnicodeAlias('CredReadDomainCredentialsW')
@winfunctype('ADVAPI32.dll')
def CredReadDomainCredentialsA(TargetInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA), Flags: UInt32, Count: POINTER(UInt32), Credential: POINTER(POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA)))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredDeleteW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredDelete = UnicodeAlias('CredDeleteW')
@winfunctype('ADVAPI32.dll')
def CredDeleteA(TargetName: win32more.Windows.Win32.Foundation.PSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredRenameW(OldTargetName: win32more.Windows.Win32.Foundation.PWSTR, NewTargetName: win32more.Windows.Win32.Foundation.PWSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredRename = UnicodeAlias('CredRenameW')
@winfunctype('ADVAPI32.dll')
def CredRenameA(OldTargetName: win32more.Windows.Win32.Foundation.PSTR, NewTargetName: win32more.Windows.Win32.Foundation.PSTR, Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredGetTargetInfoW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, TargetInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredGetTargetInfo = UnicodeAlias('CredGetTargetInfoW')
@winfunctype('ADVAPI32.dll')
def CredGetTargetInfoA(TargetName: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32, TargetInfo: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredMarshalCredentialW(CredType: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE, Credential: VoidPtr, MarshaledCredential: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredMarshalCredential = UnicodeAlias('CredMarshalCredentialW')
@winfunctype('ADVAPI32.dll')
def CredMarshalCredentialA(CredType: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE, Credential: VoidPtr, MarshaledCredential: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnmarshalCredentialW(MarshaledCredential: win32more.Windows.Win32.Foundation.PWSTR, CredType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE), Credential: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredUnmarshalCredential = UnicodeAlias('CredUnmarshalCredentialW')
@winfunctype('ADVAPI32.dll')
def CredUnmarshalCredentialA(MarshaledCredential: win32more.Windows.Win32.Foundation.PSTR, CredType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE), Credential: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsMarshaledCredentialW(MarshaledCredential: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredIsMarshaledCredential = UnicodeAlias('CredIsMarshaledCredentialW')
@winfunctype('ADVAPI32.dll')
def CredIsMarshaledCredentialA(MarshaledCredential: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredUnPackAuthenticationBufferW(dwFlags: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, pcchMaxUserName: POINTER(UInt32), pszDomainName: win32more.Windows.Win32.Foundation.PWSTR, pcchMaxDomainName: POINTER(UInt32), pszPassword: win32more.Windows.Win32.Foundation.PWSTR, pcchMaxPassword: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredUnPackAuthenticationBuffer = UnicodeAlias('CredUnPackAuthenticationBufferW')
@winfunctype('credui.dll')
def CredUnPackAuthenticationBufferA(dwFlags: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, pszUserName: win32more.Windows.Win32.Foundation.PSTR, pcchlMaxUserName: POINTER(UInt32), pszDomainName: win32more.Windows.Win32.Foundation.PSTR, pcchMaxDomainName: POINTER(UInt32), pszPassword: win32more.Windows.Win32.Foundation.PSTR, pcchMaxPassword: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('credui.dll')
def CredPackAuthenticationBufferW(dwFlags: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, pPackedCredentials: POINTER(Byte), pcbPackedCredentials: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredPackAuthenticationBuffer = UnicodeAlias('CredPackAuthenticationBufferW')
@winfunctype('credui.dll')
def CredPackAuthenticationBufferA(dwFlags: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS, pszUserName: win32more.Windows.Win32.Foundation.PSTR, pszPassword: win32more.Windows.Win32.Foundation.PSTR, pPackedCredentials: POINTER(Byte), pcbPackedCredentials: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredProtectW(fAsSelf: win32more.Windows.Win32.Foundation.BOOL, pszCredentials: win32more.Windows.Win32.Foundation.PWSTR, cchCredentials: UInt32, pszProtectedCredentials: win32more.Windows.Win32.Foundation.PWSTR, pcchMaxChars: POINTER(UInt32), ProtectionType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredProtect = UnicodeAlias('CredProtectW')
@winfunctype('ADVAPI32.dll')
def CredProtectA(fAsSelf: win32more.Windows.Win32.Foundation.BOOL, pszCredentials: win32more.Windows.Win32.Foundation.PSTR, cchCredentials: UInt32, pszProtectedCredentials: win32more.Windows.Win32.Foundation.PSTR, pcchMaxChars: POINTER(UInt32), ProtectionType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredUnprotectW(fAsSelf: win32more.Windows.Win32.Foundation.BOOL, pszProtectedCredentials: win32more.Windows.Win32.Foundation.PWSTR, cchProtectedCredentials: UInt32, pszCredentials: win32more.Windows.Win32.Foundation.PWSTR, pcchMaxChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredUnprotect = UnicodeAlias('CredUnprotectW')
@winfunctype('ADVAPI32.dll')
def CredUnprotectA(fAsSelf: win32more.Windows.Win32.Foundation.BOOL, pszProtectedCredentials: win32more.Windows.Win32.Foundation.PSTR, cchProtectedCredentials: UInt32, pszCredentials: win32more.Windows.Win32.Foundation.PSTR, pcchMaxChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredIsProtectedW(pszProtectedCredentials: win32more.Windows.Win32.Foundation.PWSTR, pProtectionType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredIsProtected = UnicodeAlias('CredIsProtectedW')
@winfunctype('ADVAPI32.dll')
def CredIsProtectedA(pszProtectedCredentials: win32more.Windows.Win32.Foundation.PSTR, pProtectionType: POINTER(win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredFindBestCredentialW(TargetName: win32more.Windows.Win32.Foundation.PWSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALW))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CredFindBestCredential = UnicodeAlias('CredFindBestCredentialW')
@winfunctype('ADVAPI32.dll')
def CredFindBestCredentialA(TargetName: win32more.Windows.Win32.Foundation.PSTR, Type: UInt32, Flags: UInt32, Credential: POINTER(POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIALA))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredGetSessionTypes(MaximumPersistCount: UInt32, MaximumPersist: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CredFree(Buffer: VoidPtr) -> Void: ...
@winfunctype('credui.dll')
def CredUIPromptForCredentialsW(pUiInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDUI_INFOW), pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, pContext: POINTER(win32more.Windows.Win32.Security.Credentials.SecHandle), dwAuthError: UInt32, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, ulUserNameBufferSize: UInt32, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, ulPasswordBufferSize: UInt32, save: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
CredUIPromptForCredentials = UnicodeAlias('CredUIPromptForCredentialsW')
@winfunctype('credui.dll')
def CredUIPromptForCredentialsA(pUiInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDUI_INFOA), pszTargetName: win32more.Windows.Win32.Foundation.PSTR, pContext: POINTER(win32more.Windows.Win32.Security.Credentials.SecHandle), dwAuthError: UInt32, pszUserName: win32more.Windows.Win32.Foundation.PSTR, ulUserNameBufferSize: UInt32, pszPassword: win32more.Windows.Win32.Foundation.PSTR, ulPasswordBufferSize: UInt32, save: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('credui.dll')
def CredUIPromptForWindowsCredentialsW(pUiInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDUI_INFOW), dwAuthError: UInt32, pulAuthPackage: POINTER(UInt32), pvInAuthBuffer: VoidPtr, ulInAuthBufferSize: UInt32, ppvOutAuthBuffer: POINTER(VoidPtr), pulOutAuthBufferSize: POINTER(UInt32), pfSave: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS) -> UInt32: ...
CredUIPromptForWindowsCredentials = UnicodeAlias('CredUIPromptForWindowsCredentialsW')
@winfunctype('credui.dll')
def CredUIPromptForWindowsCredentialsA(pUiInfo: POINTER(win32more.Windows.Win32.Security.Credentials.CREDUI_INFOA), dwAuthError: UInt32, pulAuthPackage: POINTER(UInt32), pvInAuthBuffer: VoidPtr, ulInAuthBufferSize: UInt32, ppvOutAuthBuffer: POINTER(VoidPtr), pulOutAuthBufferSize: POINTER(UInt32), pfSave: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIParseUserNameW(UserName: win32more.Windows.Win32.Foundation.PWSTR, user: win32more.Windows.Win32.Foundation.PWSTR, userBufferSize: UInt32, domain: win32more.Windows.Win32.Foundation.PWSTR, domainBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
CredUIParseUserName = UnicodeAlias('CredUIParseUserNameW')
@winfunctype('credui.dll')
def CredUIParseUserNameA(userName: win32more.Windows.Win32.Foundation.PSTR, user: win32more.Windows.Win32.Foundation.PSTR, userBufferSize: UInt32, domain: win32more.Windows.Win32.Foundation.PSTR, domainBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('credui.dll')
def CredUICmdLinePromptForCredentialsW(pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, pContext: POINTER(win32more.Windows.Win32.Security.Credentials.SecHandle), dwAuthError: UInt32, UserName: win32more.Windows.Win32.Foundation.PWSTR, ulUserBufferSize: UInt32, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, ulPasswordBufferSize: UInt32, pfSave: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
CredUICmdLinePromptForCredentials = UnicodeAlias('CredUICmdLinePromptForCredentialsW')
@winfunctype('credui.dll')
def CredUICmdLinePromptForCredentialsA(pszTargetName: win32more.Windows.Win32.Foundation.PSTR, pContext: POINTER(win32more.Windows.Win32.Security.Credentials.SecHandle), dwAuthError: UInt32, UserName: win32more.Windows.Win32.Foundation.PSTR, ulUserBufferSize: UInt32, pszPassword: win32more.Windows.Win32.Foundation.PSTR, ulPasswordBufferSize: UInt32, pfSave: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIConfirmCredentialsW(pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, bConfirm: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
CredUIConfirmCredentials = UnicodeAlias('CredUIConfirmCredentialsW')
@winfunctype('credui.dll')
def CredUIConfirmCredentialsA(pszTargetName: win32more.Windows.Win32.Foundation.PSTR, bConfirm: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIStoreSSOCredW(pszRealm: win32more.Windows.Win32.Foundation.PWSTR, pszUsername: win32more.Windows.Win32.Foundation.PWSTR, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, bPersist: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('credui.dll')
def CredUIReadSSOCredW(pszRealm: win32more.Windows.Win32.Foundation.PWSTR, ppszUsername: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('WinSCard.dll')
def SCardEstablishContext(dwScope: win32more.Windows.Win32.Security.Credentials.SCARD_SCOPE, pvReserved1: VoidPtr, pvReserved2: VoidPtr, phContext: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReleaseContext(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIsValidContext(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReaderGroupsA(hContext: UIntPtr, mszGroups: win32more.Windows.Win32.Foundation.PSTR, pcchGroups: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReaderGroupsW(hContext: UIntPtr, mszGroups: win32more.Windows.Win32.Foundation.PWSTR, pcchGroups: POINTER(UInt32)) -> Int32: ...
SCardListReaderGroups = UnicodeAlias('SCardListReaderGroupsW')
@winfunctype('WinSCard.dll')
def SCardListReadersA(hContext: UIntPtr, mszGroups: win32more.Windows.Win32.Foundation.PSTR, mszReaders: win32more.Windows.Win32.Foundation.PSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersW(hContext: UIntPtr, mszGroups: win32more.Windows.Win32.Foundation.PWSTR, mszReaders: win32more.Windows.Win32.Foundation.PWSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
SCardListReaders = UnicodeAlias('SCardListReadersW')
@winfunctype('WinSCard.dll')
def SCardListCardsA(hContext: UIntPtr, pbAtr: POINTER(Byte), rgquidInterfaces: POINTER(Guid), cguidInterfaceCount: UInt32, mszCards: win32more.Windows.Win32.Foundation.PSTR, pcchCards: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListCardsW(hContext: UIntPtr, pbAtr: POINTER(Byte), rgquidInterfaces: POINTER(Guid), cguidInterfaceCount: UInt32, mszCards: win32more.Windows.Win32.Foundation.PWSTR, pcchCards: POINTER(UInt32)) -> Int32: ...
SCardListCards = UnicodeAlias('SCardListCardsW')
@winfunctype('WinSCard.dll')
def SCardListInterfacesA(hContext: UIntPtr, szCard: win32more.Windows.Win32.Foundation.PSTR, pguidInterfaces: POINTER(Guid), pcguidInterfaces: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListInterfacesW(hContext: UIntPtr, szCard: win32more.Windows.Win32.Foundation.PWSTR, pguidInterfaces: POINTER(Guid), pcguidInterfaces: POINTER(UInt32)) -> Int32: ...
SCardListInterfaces = UnicodeAlias('SCardListInterfacesW')
@winfunctype('WinSCard.dll')
def SCardGetProviderIdA(hContext: UIntPtr, szCard: win32more.Windows.Win32.Foundation.PSTR, pguidProviderId: POINTER(Guid)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetProviderIdW(hContext: UIntPtr, szCard: win32more.Windows.Win32.Foundation.PWSTR, pguidProviderId: POINTER(Guid)) -> Int32: ...
SCardGetProviderId = UnicodeAlias('SCardGetProviderIdW')
@winfunctype('WinSCard.dll')
def SCardGetCardTypeProviderNameA(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PSTR, dwProviderId: UInt32, szProvider: win32more.Windows.Win32.Foundation.PSTR, pcchProvider: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetCardTypeProviderNameW(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PWSTR, dwProviderId: UInt32, szProvider: win32more.Windows.Win32.Foundation.PWSTR, pcchProvider: POINTER(UInt32)) -> Int32: ...
SCardGetCardTypeProviderName = UnicodeAlias('SCardGetCardTypeProviderNameW')
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderGroupA(hContext: UIntPtr, szGroupName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderGroupW(hContext: UIntPtr, szGroupName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardIntroduceReaderGroup = UnicodeAlias('SCardIntroduceReaderGroupW')
@winfunctype('WinSCard.dll')
def SCardForgetReaderGroupA(hContext: UIntPtr, szGroupName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderGroupW(hContext: UIntPtr, szGroupName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardForgetReaderGroup = UnicodeAlias('SCardForgetReaderGroupW')
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, szDeviceName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceReaderW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, szDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardIntroduceReader = UnicodeAlias('SCardIntroduceReaderW')
@winfunctype('WinSCard.dll')
def SCardForgetReaderA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetReaderW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardForgetReader = UnicodeAlias('SCardForgetReaderW')
@winfunctype('WinSCard.dll')
def SCardAddReaderToGroupA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, szGroupName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAddReaderToGroupW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, szGroupName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardAddReaderToGroup = UnicodeAlias('SCardAddReaderToGroupW')
@winfunctype('WinSCard.dll')
def SCardRemoveReaderFromGroupA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, szGroupName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardRemoveReaderFromGroupW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, szGroupName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardRemoveReaderFromGroup = UnicodeAlias('SCardRemoveReaderFromGroupW')
@winfunctype('WinSCard.dll')
def SCardIntroduceCardTypeA(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PSTR, pguidPrimaryProvider: POINTER(Guid), rgguidInterfaces: POINTER(Guid), dwInterfaceCount: UInt32, pbAtr: POINTER(Byte), pbAtrMask: POINTER(Byte), cbAtrLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardIntroduceCardTypeW(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PWSTR, pguidPrimaryProvider: POINTER(Guid), rgguidInterfaces: POINTER(Guid), dwInterfaceCount: UInt32, pbAtr: POINTER(Byte), pbAtrMask: POINTER(Byte), cbAtrLen: UInt32) -> Int32: ...
SCardIntroduceCardType = UnicodeAlias('SCardIntroduceCardTypeW')
@winfunctype('WinSCard.dll')
def SCardSetCardTypeProviderNameA(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PSTR, dwProviderId: UInt32, szProvider: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardSetCardTypeProviderNameW(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PWSTR, dwProviderId: UInt32, szProvider: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardSetCardTypeProviderName = UnicodeAlias('SCardSetCardTypeProviderNameW')
@winfunctype('WinSCard.dll')
def SCardForgetCardTypeA(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardForgetCardTypeW(hContext: UIntPtr, szCardName: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SCardForgetCardType = UnicodeAlias('SCardForgetCardTypeW')
@winfunctype('WinSCard.dll')
def SCardFreeMemory(hContext: UIntPtr, pvMem: VoidPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardAccessStartedEvent() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WinSCard.dll')
def SCardReleaseStartedEvent() -> Void: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsA(hContext: UIntPtr, mszCards: win32more.Windows.Win32.Foundation.PSTR, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEA), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsW(hContext: UIntPtr, mszCards: win32more.Windows.Win32.Foundation.PWSTR, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEW), cReaders: UInt32) -> Int32: ...
SCardLocateCards = UnicodeAlias('SCardLocateCardsW')
@winfunctype('WinSCard.dll')
def SCardLocateCardsByATRA(hContext: UIntPtr, rgAtrMasks: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_ATRMASK), cAtrs: UInt32, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEA), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardLocateCardsByATRW(hContext: UIntPtr, rgAtrMasks: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_ATRMASK), cAtrs: UInt32, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEW), cReaders: UInt32) -> Int32: ...
SCardLocateCardsByATR = UnicodeAlias('SCardLocateCardsByATRW')
@winfunctype('WinSCard.dll')
def SCardGetStatusChangeA(hContext: UIntPtr, dwTimeout: UInt32, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEA), cReaders: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetStatusChangeW(hContext: UIntPtr, dwTimeout: UInt32, rgReaderStates: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_READERSTATEW), cReaders: UInt32) -> Int32: ...
SCardGetStatusChange = UnicodeAlias('SCardGetStatusChangeW')
@winfunctype('WinSCard.dll')
def SCardCancel(hContext: UIntPtr) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardConnectA(hContext: UIntPtr, szReader: win32more.Windows.Win32.Foundation.PSTR, dwShareMode: UInt32, dwPreferredProtocols: UInt32, phCard: POINTER(UIntPtr), pdwActiveProtocol: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardConnectW(hContext: UIntPtr, szReader: win32more.Windows.Win32.Foundation.PWSTR, dwShareMode: UInt32, dwPreferredProtocols: UInt32, phCard: POINTER(UIntPtr), pdwActiveProtocol: POINTER(UInt32)) -> Int32: ...
SCardConnect = UnicodeAlias('SCardConnectW')
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
def SCardStatusA(hCard: UIntPtr, mszReaderNames: win32more.Windows.Win32.Foundation.PSTR, pcchReaderLen: POINTER(UInt32), pdwState: POINTER(UInt32), pdwProtocol: POINTER(UInt32), pbAtr: POINTER(Byte), pcbAtrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardStatusW(hCard: UIntPtr, mszReaderNames: win32more.Windows.Win32.Foundation.PWSTR, pcchReaderLen: POINTER(UInt32), pdwState: POINTER(UInt32), pdwProtocol: POINTER(UInt32), pbAtr: POINTER(Byte), pcbAtrLen: POINTER(UInt32)) -> Int32: ...
SCardStatus = UnicodeAlias('SCardStatusW')
@winfunctype('WinSCard.dll')
def SCardTransmit(hCard: UIntPtr, pioSendPci: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_IO_REQUEST), pbSendBuffer: POINTER(Byte), cbSendLength: UInt32, pioRecvPci: POINTER(win32more.Windows.Win32.Security.Credentials.SCARD_IO_REQUEST), pbRecvBuffer: POINTER(Byte), pcbRecvLength: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetTransmitCount(hCard: UIntPtr, pcTransmitCount: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardControl(hCard: UIntPtr, dwControlCode: UInt32, lpInBuffer: VoidPtr, cbInBufferSize: UInt32, lpOutBuffer: VoidPtr, cbOutBufferSize: UInt32, lpBytesReturned: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetAttrib(hCard: UIntPtr, dwAttrId: UInt32, pbAttr: POINTER(Byte), pcbAttrLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardSetAttrib(hCard: UIntPtr, dwAttrId: UInt32, pbAttr: POINTER(Byte), cbAttrLen: UInt32) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def SCardUIDlgSelectCardA(param0: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARDNAME_EXA)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def SCardUIDlgSelectCardW(param0: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARDNAME_EXW)) -> Int32: ...
SCardUIDlgSelectCard = UnicodeAlias('SCardUIDlgSelectCardW')
@winfunctype('SCARDDLG.dll')
def GetOpenCardNameA(param0: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARDNAMEA)) -> Int32: ...
@winfunctype('SCARDDLG.dll')
def GetOpenCardNameW(param0: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARDNAMEW)) -> Int32: ...
GetOpenCardName = UnicodeAlias('GetOpenCardNameW')
@winfunctype('SCARDDLG.dll')
def SCardDlgExtendedError() -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReadCacheA(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(Byte), DataLen: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardReadCacheW(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(Byte), DataLen: POINTER(UInt32)) -> Int32: ...
SCardReadCache = UnicodeAlias('SCardReadCacheW')
@winfunctype('WinSCard.dll')
def SCardWriteCacheA(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: win32more.Windows.Win32.Foundation.PSTR, Data: POINTER(Byte), DataLen: UInt32) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardWriteCacheW(hContext: UIntPtr, CardIdentifier: POINTER(Guid), FreshnessCounter: UInt32, LookupName: win32more.Windows.Win32.Foundation.PWSTR, Data: POINTER(Byte), DataLen: UInt32) -> Int32: ...
SCardWriteCache = UnicodeAlias('SCardWriteCacheW')
@winfunctype('WinSCard.dll')
def SCardGetReaderIconA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, pbIcon: POINTER(Byte), pcbIcon: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderIconW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, pbIcon: POINTER(Byte), pcbIcon: POINTER(UInt32)) -> Int32: ...
SCardGetReaderIcon = UnicodeAlias('SCardGetReaderIconW')
@winfunctype('WinSCard.dll')
def SCardGetDeviceTypeIdA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, pdwDeviceTypeId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetDeviceTypeIdW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, pdwDeviceTypeId: POINTER(UInt32)) -> Int32: ...
SCardGetDeviceTypeId = UnicodeAlias('SCardGetDeviceTypeIdW')
@winfunctype('WinSCard.dll')
def SCardGetReaderDeviceInstanceIdA(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PSTR, szDeviceInstanceId: win32more.Windows.Win32.Foundation.PSTR, pcchDeviceInstanceId: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardGetReaderDeviceInstanceIdW(hContext: UIntPtr, szReaderName: win32more.Windows.Win32.Foundation.PWSTR, szDeviceInstanceId: win32more.Windows.Win32.Foundation.PWSTR, pcchDeviceInstanceId: POINTER(UInt32)) -> Int32: ...
SCardGetReaderDeviceInstanceId = UnicodeAlias('SCardGetReaderDeviceInstanceIdW')
@winfunctype('WinSCard.dll')
def SCardListReadersWithDeviceInstanceIdA(hContext: UIntPtr, szDeviceInstanceId: win32more.Windows.Win32.Foundation.PSTR, mszReaders: win32more.Windows.Win32.Foundation.PSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
@winfunctype('WinSCard.dll')
def SCardListReadersWithDeviceInstanceIdW(hContext: UIntPtr, szDeviceInstanceId: win32more.Windows.Win32.Foundation.PWSTR, mszReaders: win32more.Windows.Win32.Foundation.PWSTR, pcchReaders: POINTER(UInt32)) -> Int32: ...
SCardListReadersWithDeviceInstanceId = UnicodeAlias('SCardListReadersWithDeviceInstanceIdW')
@winfunctype('WinSCard.dll')
def SCardAudit(hContext: UIntPtr, dwEvent: UInt32) -> Int32: ...
class BINARY_BLOB_CREDENTIAL_INFO(Structure):
    cbBlob: UInt32
    pbBlob: POINTER(Byte)
class CERT_CREDENTIAL_INFO(Structure):
    cbSize: UInt32
    rgbHashOfCert: Byte * 20
class CREDENTIALA(Structure):
    Flags: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS
    Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE
    TargetName: win32more.Windows.Win32.Foundation.PSTR
    Comment: win32more.Windows.Win32.Foundation.PSTR
    LastWritten: win32more.Windows.Win32.Foundation.FILETIME
    CredentialBlobSize: UInt32
    CredentialBlob: POINTER(Byte)
    Persist: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST
    AttributeCount: UInt32
    Attributes: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_ATTRIBUTEA)
    TargetAlias: win32more.Windows.Win32.Foundation.PSTR
    UserName: win32more.Windows.Win32.Foundation.PSTR
class CREDENTIALW(Structure):
    Flags: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS
    Type: win32more.Windows.Win32.Security.Credentials.CRED_TYPE
    TargetName: win32more.Windows.Win32.Foundation.PWSTR
    Comment: win32more.Windows.Win32.Foundation.PWSTR
    LastWritten: win32more.Windows.Win32.Foundation.FILETIME
    CredentialBlobSize: UInt32
    CredentialBlob: POINTER(Byte)
    Persist: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST
    AttributeCount: UInt32
    Attributes: POINTER(win32more.Windows.Win32.Security.Credentials.CREDENTIAL_ATTRIBUTEW)
    TargetAlias: win32more.Windows.Win32.Foundation.PWSTR
    UserName: win32more.Windows.Win32.Foundation.PWSTR
CREDENTIAL = UnicodeAlias('CREDENTIALW')
class CREDENTIAL_ATTRIBUTEA(Structure):
    Keyword: win32more.Windows.Win32.Foundation.PSTR
    Flags: UInt32
    ValueSize: UInt32
    Value: POINTER(Byte)
class CREDENTIAL_ATTRIBUTEW(Structure):
    Keyword: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    ValueSize: UInt32
    Value: POINTER(Byte)
CREDENTIAL_ATTRIBUTE = UnicodeAlias('CREDENTIAL_ATTRIBUTEW')
class CREDENTIAL_TARGET_INFORMATIONA(Structure):
    TargetName: win32more.Windows.Win32.Foundation.PSTR
    NetbiosServerName: win32more.Windows.Win32.Foundation.PSTR
    DnsServerName: win32more.Windows.Win32.Foundation.PSTR
    NetbiosDomainName: win32more.Windows.Win32.Foundation.PSTR
    DnsDomainName: win32more.Windows.Win32.Foundation.PSTR
    DnsTreeName: win32more.Windows.Win32.Foundation.PSTR
    PackageName: win32more.Windows.Win32.Foundation.PSTR
    Flags: UInt32
    CredTypeCount: UInt32
    CredTypes: POINTER(UInt32)
class CREDENTIAL_TARGET_INFORMATIONW(Structure):
    TargetName: win32more.Windows.Win32.Foundation.PWSTR
    NetbiosServerName: win32more.Windows.Win32.Foundation.PWSTR
    DnsServerName: win32more.Windows.Win32.Foundation.PWSTR
    NetbiosDomainName: win32more.Windows.Win32.Foundation.PWSTR
    DnsDomainName: win32more.Windows.Win32.Foundation.PWSTR
    DnsTreeName: win32more.Windows.Win32.Foundation.PWSTR
    PackageName: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    CredTypeCount: UInt32
    CredTypes: POINTER(UInt32)
CREDENTIAL_TARGET_INFORMATION = UnicodeAlias('CREDENTIAL_TARGET_INFORMATIONW')
CREDSPP_SUBMIT_TYPE = Int32
CredsspPasswordCreds: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 2
CredsspSchannelCreds: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 4
CredsspCertificateCreds: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 13
CredsspSubmitBufferBoth: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 50
CredsspSubmitBufferBothOld: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 51
CredsspCredEx: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE = 100
class CREDSSP_CRED(Structure):
    Type: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE
    pSchannelCred: VoidPtr
    pSpnegoCred: VoidPtr
class CREDSSP_CRED_EX(Structure):
    Type: win32more.Windows.Win32.Security.Credentials.CREDSPP_SUBMIT_TYPE
    Version: UInt32
    Flags: UInt32
    Reserved: UInt32
    Cred: win32more.Windows.Win32.Security.Credentials.CREDSSP_CRED
CREDUIWIN_FLAGS = UInt32
CREDUIWIN_GENERIC: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 1
CREDUIWIN_CHECKBOX: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 2
CREDUIWIN_AUTHPACKAGE_ONLY: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 16
CREDUIWIN_IN_CRED_ONLY: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 32
CREDUIWIN_ENUMERATE_ADMINS: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 256
CREDUIWIN_ENUMERATE_CURRENT_USER: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 512
CREDUIWIN_SECURE_PROMPT: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 4096
CREDUIWIN_PREPROMPTING: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 8192
CREDUIWIN_PACK_32_WOW: win32more.Windows.Win32.Security.Credentials.CREDUIWIN_FLAGS = 268435456
CREDUI_FLAGS = UInt32
CREDUI_FLAGS_ALWAYS_SHOW_UI: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 128
CREDUI_FLAGS_COMPLETE_USERNAME: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 2048
CREDUI_FLAGS_DO_NOT_PERSIST: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 2
CREDUI_FLAGS_EXCLUDE_CERTIFICATES: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 8
CREDUI_FLAGS_EXPECT_CONFIRMATION: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 131072
CREDUI_FLAGS_GENERIC_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 262144
CREDUI_FLAGS_INCORRECT_PASSWORD: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 1
CREDUI_FLAGS_KEEP_USERNAME: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 1048576
CREDUI_FLAGS_PASSWORD_ONLY_OK: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 512
CREDUI_FLAGS_PERSIST: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 4096
CREDUI_FLAGS_REQUEST_ADMINISTRATOR: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 4
CREDUI_FLAGS_REQUIRE_CERTIFICATE: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 16
CREDUI_FLAGS_REQUIRE_SMARTCARD: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 256
CREDUI_FLAGS_SERVER_CREDENTIAL: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 16384
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 64
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 524288
CREDUI_FLAGS_VALIDATE_USERNAME: win32more.Windows.Win32.Security.Credentials.CREDUI_FLAGS = 1024
class CREDUI_INFOA(Structure):
    cbSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    pszMessageText: win32more.Windows.Win32.Foundation.PSTR
    pszCaptionText: win32more.Windows.Win32.Foundation.PSTR
    hbmBanner: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
class CREDUI_INFOW(Structure):
    cbSize: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    pszMessageText: win32more.Windows.Win32.Foundation.PWSTR
    pszCaptionText: win32more.Windows.Win32.Foundation.PWSTR
    hbmBanner: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
CREDUI_INFO = UnicodeAlias('CREDUI_INFOW')
CRED_ENUMERATE_FLAGS = UInt32
CRED_ENUMERATE_ALL_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CRED_ENUMERATE_FLAGS = 1
CRED_FLAGS = UInt32
CRED_FLAGS_PASSWORD_FOR_CERT: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 1
CRED_FLAGS_PROMPT_NOW: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 2
CRED_FLAGS_USERNAME_TARGET: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 4
CRED_FLAGS_OWF_CRED_BLOB: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 8
CRED_FLAGS_REQUIRE_CONFIRMATION: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 16
CRED_FLAGS_WILDCARD_MATCH: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 32
CRED_FLAGS_VSM_PROTECTED: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 64
CRED_FLAGS_NGC_CERT: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 128
CRED_FLAGS_VALID_FLAGS: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 61695
CRED_FLAGS_VALID_INPUT_FLAGS: win32more.Windows.Win32.Security.Credentials.CRED_FLAGS = 61599
CRED_MARSHAL_TYPE = Int32
CertCredential: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE = 1
UsernameTargetCredential: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE = 2
BinaryBlobCredential: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE = 3
UsernameForPackedCredentials: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE = 4
BinaryBlobForSystem: win32more.Windows.Win32.Security.Credentials.CRED_MARSHAL_TYPE = 5
CRED_PACK_FLAGS = UInt32
CRED_PACK_PROTECTED_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS = 1
CRED_PACK_WOW_BUFFER: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS = 2
CRED_PACK_GENERIC_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS = 4
CRED_PACK_ID_PROVIDER_CREDENTIALS: win32more.Windows.Win32.Security.Credentials.CRED_PACK_FLAGS = 8
CRED_PERSIST = UInt32
CRED_PERSIST_NONE: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST = 0
CRED_PERSIST_SESSION: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST = 1
CRED_PERSIST_LOCAL_MACHINE: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST = 2
CRED_PERSIST_ENTERPRISE: win32more.Windows.Win32.Security.Credentials.CRED_PERSIST = 3
CRED_PROTECTION_TYPE = Int32
CredUnprotected: win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE = 0
CredUserProtection: win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE = 1
CredTrustedProtection: win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE = 2
CredForSystemProtection: win32more.Windows.Win32.Security.Credentials.CRED_PROTECTION_TYPE = 3
CRED_TYPE = UInt32
CRED_TYPE_GENERIC: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 1
CRED_TYPE_DOMAIN_PASSWORD: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 2
CRED_TYPE_DOMAIN_CERTIFICATE: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 3
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 4
CRED_TYPE_GENERIC_CERTIFICATE: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 5
CRED_TYPE_DOMAIN_EXTENDED: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 6
CRED_TYPE_MAXIMUM: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 7
CRED_TYPE_MAXIMUM_EX: win32more.Windows.Win32.Security.Credentials.CRED_TYPE = 1007
class KeyCredentialManagerInfo(Structure):
    containerId: Guid
KeyCredentialManagerOperationErrorStates = Int32
KeyCredentialManagerOperationErrorStateNone: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 0
KeyCredentialManagerOperationErrorStateDeviceJoinFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 1
KeyCredentialManagerOperationErrorStateTokenFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 2
KeyCredentialManagerOperationErrorStateCertificateFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 4
KeyCredentialManagerOperationErrorStateRemoteSessionFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 8
KeyCredentialManagerOperationErrorStatePolicyFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 16
KeyCredentialManagerOperationErrorStateHardwareFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 32
KeyCredentialManagerOperationErrorStatePinExistsFailure: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationErrorStates = 64
KeyCredentialManagerOperationType = Int32
KeyCredentialManagerProvisioning: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType = 0
KeyCredentialManagerPinChange: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType = 1
KeyCredentialManagerPinReset: win32more.Windows.Win32.Security.Credentials.KeyCredentialManagerOperationType = 2
@winfunctype_pointer
def LPOCNCHKPROC(param0: UIntPtr, param1: UIntPtr, param2: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPOCNCONNPROCA(param0: UIntPtr, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: VoidPtr) -> UIntPtr: ...
@winfunctype_pointer
def LPOCNCONNPROCW(param0: UIntPtr, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: VoidPtr) -> UIntPtr: ...
LPOCNCONNPROC = UnicodeAlias('LPOCNCONNPROCW')
@winfunctype_pointer
def LPOCNDSCPROC(param0: UIntPtr, param1: UIntPtr, param2: VoidPtr) -> Void: ...
class OPENCARDNAMEA(Structure):
    dwStructSize: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    hSCardContext: UIntPtr
    lpstrGroupNames: win32more.Windows.Win32.Foundation.PSTR
    nMaxGroupNames: UInt32
    lpstrCardNames: win32more.Windows.Win32.Foundation.PSTR
    nMaxCardNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrRdr: win32more.Windows.Win32.Foundation.PSTR
    nMaxRdr: UInt32
    lpstrCard: win32more.Windows.Win32.Foundation.PSTR
    nMaxCard: UInt32
    lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
    dwFlags: UInt32
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    dwActiveProtocol: UInt32
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    lpfnCheck: win32more.Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnDisconnect: win32more.Windows.Win32.Security.Credentials.LPOCNDSCPROC
    hCardHandle: UIntPtr
class OPENCARDNAMEW(Structure):
    dwStructSize: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    hSCardContext: UIntPtr
    lpstrGroupNames: win32more.Windows.Win32.Foundation.PWSTR
    nMaxGroupNames: UInt32
    lpstrCardNames: win32more.Windows.Win32.Foundation.PWSTR
    nMaxCardNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrRdr: win32more.Windows.Win32.Foundation.PWSTR
    nMaxRdr: UInt32
    lpstrCard: win32more.Windows.Win32.Foundation.PWSTR
    nMaxCard: UInt32
    lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    dwActiveProtocol: UInt32
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    lpfnCheck: win32more.Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnDisconnect: win32more.Windows.Win32.Security.Credentials.LPOCNDSCPROC
    hCardHandle: UIntPtr
OPENCARDNAME = UnicodeAlias('OPENCARDNAMEW')
class OPENCARDNAME_EXA(Structure):
    dwStructSize: UInt32
    hSCardContext: UIntPtr
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
    lpstrSearchDesc: win32more.Windows.Win32.Foundation.PSTR
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    pOpenCardSearchCriteria: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARD_SEARCH_CRITERIAA)
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    lpstrRdr: win32more.Windows.Win32.Foundation.PSTR
    nMaxRdr: UInt32
    lpstrCard: win32more.Windows.Win32.Foundation.PSTR
    nMaxCard: UInt32
    dwActiveProtocol: UInt32
    hCardHandle: UIntPtr
class OPENCARDNAME_EXW(Structure):
    dwStructSize: UInt32
    hSCardContext: UIntPtr
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    dwFlags: UInt32
    lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
    lpstrSearchDesc: win32more.Windows.Win32.Foundation.PWSTR
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    pOpenCardSearchCriteria: POINTER(win32more.Windows.Win32.Security.Credentials.OPENCARD_SEARCH_CRITERIAW)
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    lpstrRdr: win32more.Windows.Win32.Foundation.PWSTR
    nMaxRdr: UInt32
    lpstrCard: win32more.Windows.Win32.Foundation.PWSTR
    nMaxCard: UInt32
    dwActiveProtocol: UInt32
    hCardHandle: UIntPtr
OPENCARDNAME_EX = UnicodeAlias('OPENCARDNAME_EXW')
class OPENCARD_SEARCH_CRITERIAA(Structure):
    dwStructSize: UInt32
    lpstrGroupNames: win32more.Windows.Win32.Foundation.PSTR
    nMaxGroupNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrCardNames: win32more.Windows.Win32.Foundation.PSTR
    nMaxCardNames: UInt32
    lpfnCheck: win32more.Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCA
    lpfnDisconnect: win32more.Windows.Win32.Security.Credentials.LPOCNDSCPROC
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
class OPENCARD_SEARCH_CRITERIAW(Structure):
    dwStructSize: UInt32
    lpstrGroupNames: win32more.Windows.Win32.Foundation.PWSTR
    nMaxGroupNames: UInt32
    rgguidInterfaces: POINTER(Guid)
    cguidInterfaces: UInt32
    lpstrCardNames: win32more.Windows.Win32.Foundation.PWSTR
    nMaxCardNames: UInt32
    lpfnCheck: win32more.Windows.Win32.Security.Credentials.LPOCNCHKPROC
    lpfnConnect: win32more.Windows.Win32.Security.Credentials.LPOCNCONNPROCW
    lpfnDisconnect: win32more.Windows.Win32.Security.Credentials.LPOCNDSCPROC
    pvUserData: VoidPtr
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
OPENCARD_SEARCH_CRITERIA = UnicodeAlias('OPENCARD_SEARCH_CRITERIAW')
class READER_SEL_REQUEST(Structure):
    dwShareMode: UInt32
    dwPreferredProtocols: UInt32
    MatchType: win32more.Windows.Win32.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ReaderAndContainerParameter: _ReaderAndContainerParameter_e__Struct
        SerialNumberParameter: _SerialNumberParameter_e__Struct
        class _ReaderAndContainerParameter_e__Struct(Structure):
            cbReaderNameOffset: UInt32
            cchReaderNameLength: UInt32
            cbContainerNameOffset: UInt32
            cchContainerNameLength: UInt32
            dwDesiredCardModuleVersion: UInt32
            dwCspFlags: UInt32
        class _SerialNumberParameter_e__Struct(Structure):
            cbSerialNumberOffset: UInt32
            cbSerialNumberLength: UInt32
            dwDesiredCardModuleVersion: UInt32
READER_SEL_REQUEST_MATCH_TYPE = Int32
RSR_MATCH_TYPE_READER_AND_CONTAINER: win32more.Windows.Win32.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE = 1
RSR_MATCH_TYPE_SERIAL_NUMBER: win32more.Windows.Win32.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE = 2
RSR_MATCH_TYPE_ALL_CARDS: win32more.Windows.Win32.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE = 3
class READER_SEL_RESPONSE(Structure):
    cbReaderNameOffset: UInt32
    cchReaderNameLength: UInt32
    cbCardNameOffset: UInt32
    cchCardNameLength: UInt32
class SCARD_ATRMASK(Structure):
    cbAtr: UInt32
    rgbAtr: Byte * 36
    rgbMask: Byte * 36
class SCARD_IO_REQUEST(Structure):
    dwProtocol: UInt32
    cbPciLength: UInt32
class SCARD_READERSTATEA(Structure):
    szReader: win32more.Windows.Win32.Foundation.PSTR
    pvUserData: VoidPtr
    dwCurrentState: win32more.Windows.Win32.Security.Credentials.SCARD_STATE
    dwEventState: win32more.Windows.Win32.Security.Credentials.SCARD_STATE
    cbAtr: UInt32
    rgbAtr: Byte * 36
class SCARD_READERSTATEW(Structure):
    szReader: win32more.Windows.Win32.Foundation.PWSTR
    pvUserData: VoidPtr
    dwCurrentState: win32more.Windows.Win32.Security.Credentials.SCARD_STATE
    dwEventState: win32more.Windows.Win32.Security.Credentials.SCARD_STATE
    cbAtr: UInt32
    rgbAtr: Byte * 36
SCARD_READERSTATE = UnicodeAlias('SCARD_READERSTATEW')
SCARD_SCOPE = UInt32
SCARD_SCOPE_USER: win32more.Windows.Win32.Security.Credentials.SCARD_SCOPE = 0
SCARD_SCOPE_SYSTEM: win32more.Windows.Win32.Security.Credentials.SCARD_SCOPE = 2
SCARD_STATE = UInt32
SCARD_STATE_UNAWARE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 0
SCARD_STATE_IGNORE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 1
SCARD_STATE_UNAVAILABLE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 8
SCARD_STATE_EMPTY: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 16
SCARD_STATE_PRESENT: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 32
SCARD_STATE_ATRMATCH: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 64
SCARD_STATE_EXCLUSIVE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 128
SCARD_STATE_INUSE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 256
SCARD_STATE_MUTE: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 512
SCARD_STATE_CHANGED: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 2
SCARD_STATE_UNKNOWN: win32more.Windows.Win32.Security.Credentials.SCARD_STATE = 4
class SCARD_T0_COMMAND(Structure):
    bCla: Byte
    bIns: Byte
    bP1: Byte
    bP2: Byte
    bP3: Byte
class SCARD_T0_REQUEST(Structure):
    ioRequest: win32more.Windows.Win32.Security.Credentials.SCARD_IO_REQUEST
    bSw1: Byte
    bSw2: Byte
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        CmdBytes: win32more.Windows.Win32.Security.Credentials.SCARD_T0_COMMAND
        rgbHeader: Byte * 5
class SCARD_T1_REQUEST(Structure):
    ioRequest: win32more.Windows.Win32.Security.Credentials.SCARD_IO_REQUEST
class SecHandle(Structure):
    dwLower: UIntPtr
    dwUpper: UIntPtr
class SecPkgContext_ClientCreds(Structure):
    AuthBufferLen: UInt32
    AuthBuffer: POINTER(Byte)
class USERNAME_TARGET_CREDENTIAL_INFO(Structure):
    UserName: win32more.Windows.Win32.Foundation.PWSTR


make_ready(__name__)
