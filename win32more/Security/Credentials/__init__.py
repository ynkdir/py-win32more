from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security.Credentials
import win32more.UI.WindowsAndMessaging
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
CRED_MAX_CREDENTIAL_BLOB_SIZE = 2560
CRED_MAX_USERNAME_LENGTH = 513
CRED_MAX_DOMAIN_TARGET_NAME_LENGTH = 337
FILE_DEVICE_SMARTCARD = 49
def _define_GUID_DEVINTERFACE_SMARTCARD_READER():
    return Guid('50dd5230-ba8a-11d1-bf-5d-00-00-f8-05-f5-30')
SCARD_ATR_LENGTH = 33
SCARD_PROTOCOL_UNDEFINED = 0
SCARD_PROTOCOL_T0 = 1
SCARD_PROTOCOL_T1 = 2
SCARD_PROTOCOL_RAW = 65536
SCARD_PROTOCOL_DEFAULT = 2147483648
SCARD_PROTOCOL_OPTIMAL = 0
SCARD_POWER_DOWN = 0
SCARD_COLD_RESET = 1
SCARD_WARM_RESET = 2
MAXIMUM_ATTR_STRING_LENGTH = 32
MAXIMUM_SMARTCARD_READERS = 10
SCARD_CLASS_VENDOR_INFO = 1
SCARD_CLASS_COMMUNICATIONS = 2
SCARD_CLASS_PROTOCOL = 3
SCARD_CLASS_POWER_MGMT = 4
SCARD_CLASS_SECURITY = 5
SCARD_CLASS_MECHANICAL = 6
SCARD_CLASS_VENDOR_DEFINED = 7
SCARD_CLASS_IFD_PROTOCOL = 8
SCARD_CLASS_ICC_STATE = 9
SCARD_CLASS_PERF = 32766
SCARD_CLASS_SYSTEM = 32767
SCARD_T0_HEADER_LENGTH = 7
SCARD_T0_CMD_LENGTH = 5
SCARD_T1_PROLOGUE_LENGTH = 3
SCARD_T1_EPILOGUE_LENGTH = 2
SCARD_T1_EPILOGUE_LENGTH_LRC = 1
SCARD_T1_MAX_IFS = 254
SCARD_UNKNOWN = 0
SCARD_ABSENT = 1
SCARD_PRESENT = 2
SCARD_SWALLOWED = 3
SCARD_POWERED = 4
SCARD_NEGOTIABLE = 5
SCARD_SPECIFIC = 6
SCARD_READER_SWALLOWS = 1
SCARD_READER_EJECTS = 2
SCARD_READER_CONFISCATES = 4
SCARD_READER_CONTACTLESS = 8
SCARD_READER_TYPE_SERIAL = 1
SCARD_READER_TYPE_PARALELL = 2
SCARD_READER_TYPE_KEYBOARD = 4
SCARD_READER_TYPE_SCSI = 8
SCARD_READER_TYPE_IDE = 16
SCARD_READER_TYPE_USB = 32
SCARD_READER_TYPE_PCMCIA = 64
SCARD_READER_TYPE_TPM = 128
SCARD_READER_TYPE_NFC = 256
SCARD_READER_TYPE_UICC = 512
SCARD_READER_TYPE_NGC = 1024
SCARD_READER_TYPE_EMBEDDEDSE = 2048
SCARD_READER_TYPE_VENDOR = 240
STATUS_LOGON_FAILURE = -1073741715
STATUS_WRONG_PASSWORD = -1073741718
STATUS_PASSWORD_EXPIRED = -1073741711
STATUS_PASSWORD_MUST_CHANGE = -1073741276
STATUS_DOWNGRADE_DETECTED = -1073740920
STATUS_AUTHENTICATION_FIREWALL_FAILED = -1073740781
STATUS_ACCOUNT_DISABLED = -1073741710
STATUS_ACCOUNT_RESTRICTION = -1073741714
STATUS_ACCOUNT_LOCKED_OUT = -1073741260
STATUS_ACCOUNT_EXPIRED = -1073741421
STATUS_LOGON_TYPE_NOT_GRANTED = -1073741477
STATUS_NO_SUCH_LOGON_SESSION = -1073741729
STATUS_NO_SUCH_USER = -1073741724
CRED_MAX_STRING_LENGTH = 256
CRED_MAX_GENERIC_TARGET_NAME_LENGTH = 32767
CRED_MAX_TARGETNAME_NAMESPACE_LENGTH = 256
CRED_MAX_TARGETNAME_ATTRIBUTE_LENGTH = 256
CRED_MAX_VALUE_SIZE = 256
CRED_MAX_ATTRIBUTES = 64
CRED_SESSION_WILDCARD_NAME_W = '*Session'
CRED_SESSION_WILDCARD_NAME_A = '*Session'
CRED_TARGETNAME_DOMAIN_NAMESPACE_W = 'Domain'
CRED_TARGETNAME_DOMAIN_NAMESPACE_A = 'Domain'
CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_W = 'LegacyGeneric'
CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_A = 'LegacyGeneric'
CRED_TARGETNAME_ATTRIBUTE_TARGET_W = 'target'
CRED_TARGETNAME_ATTRIBUTE_TARGET_A = 'target'
CRED_TARGETNAME_ATTRIBUTE_NAME_W = 'name'
CRED_TARGETNAME_ATTRIBUTE_NAME_A = 'name'
CRED_TARGETNAME_ATTRIBUTE_BATCH_W = 'batch'
CRED_TARGETNAME_ATTRIBUTE_BATCH_A = 'batch'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_W = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_A = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_SERVICE_W = 'service'
CRED_TARGETNAME_ATTRIBUTE_SERVICE_A = 'service'
CRED_TARGETNAME_ATTRIBUTE_NETWORK_W = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORK_A = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_W = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_A = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_W = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_A = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_W = 'cachedinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_A = 'cachedinteractive'
CRED_SESSION_WILDCARD_NAME = '*Session'
CRED_TARGETNAME_DOMAIN_NAMESPACE = 'Domain'
CRED_TARGETNAME_ATTRIBUTE_NAME = 'name'
CRED_TARGETNAME_ATTRIBUTE_TARGET = 'target'
CRED_TARGETNAME_ATTRIBUTE_BATCH = 'batch'
CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE = 'interactive'
CRED_TARGETNAME_ATTRIBUTE_SERVICE = 'service'
CRED_TARGETNAME_ATTRIBUTE_NETWORK = 'network'
CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT = 'networkcleartext'
CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE = 'remoteinteractive'
CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE = 'cachedinteractive'
CRED_LOGON_TYPES_MASK = 61440
CRED_TI_SERVER_FORMAT_UNKNOWN = 1
CRED_TI_DOMAIN_FORMAT_UNKNOWN = 2
CRED_TI_ONLY_PASSWORD_REQUIRED = 4
CRED_TI_USERNAME_TARGET = 8
CRED_TI_CREATE_EXPLICIT_CRED = 16
CRED_TI_WORKGROUP_MEMBER = 32
CRED_TI_DNSTREE_IS_DFS_SERVER = 64
CRED_TI_VALID_FLAGS = 61567
CERT_HASH_LENGTH = 20
CREDUI_MAX_MESSAGE_LENGTH = 1024
CREDUI_MAX_CAPTION_LENGTH = 128
CREDUI_MAX_GENERIC_TARGET_LENGTH = 32767
CREDUI_MAX_DOMAIN_TARGET_LENGTH = 337
CREDUI_MAX_USERNAME_LENGTH = 513
CREDUIWIN_IGNORE_CLOUDAUTHORITY_NAME = 262144
CREDUIWIN_DOWNLEVEL_HELLO_AS_SMART_CARD = 2147483648
CRED_PRESERVE_CREDENTIAL_BLOB = 1
CRED_CACHE_TARGET_INFORMATION = 1
CRED_ALLOW_NAME_RESOLUTION = 1
CRED_PROTECT_AS_SELF = 1
CRED_PROTECT_TO_SYSTEM = 2
CRED_UNPROTECT_AS_SELF = 1
CRED_UNPROTECT_ALLOW_TO_SYSTEM = 2
SCARD_SCOPE_TERMINAL = 1
SCARD_ALL_READERS = 'SCard$AllReaders\x0000'
SCARD_DEFAULT_READERS = 'SCard$DefaultReaders\x0000'
SCARD_LOCAL_READERS = 'SCard$LocalReaders\x0000'
SCARD_SYSTEM_READERS = 'SCard$SystemReaders\x0000'
SCARD_PROVIDER_PRIMARY = 1
SCARD_PROVIDER_CSP = 2
SCARD_PROVIDER_KSP = 3
SCARD_STATE_UNPOWERED = 1024
SCARD_SHARE_EXCLUSIVE = 1
SCARD_SHARE_SHARED = 2
SCARD_SHARE_DIRECT = 3
SCARD_LEAVE_CARD = 0
SCARD_RESET_CARD = 1
SCARD_UNPOWER_CARD = 2
SCARD_EJECT_CARD = 3
SC_DLG_MINIMAL_UI = 1
SC_DLG_NO_UI = 2
SC_DLG_FORCE_UI = 4
SCERR_NOCARDNAME = 16384
SCERR_NOGUIDS = 32768
SCARD_AUDIT_CHV_FAILURE = 0
SCARD_AUDIT_CHV_SUCCESS = 1
CREDSSP_NAME = 'CREDSSP'
TS_SSP_NAME_A = 'TSSSP'
TS_SSP_NAME = 'TSSSP'
szOID_TS_KP_TS_SERVER_AUTH = '1.3.6.1.4.1.311.54.1.2'
CREDSSP_SERVER_AUTH_NEGOTIATE = 1
CREDSSP_SERVER_AUTH_CERTIFICATE = 2
CREDSSP_SERVER_AUTH_LOOPBACK = 4
SECPKG_ALT_ATTR = 2147483648
SECPKG_ATTR_C_FULL_IDENT_TOKEN = 2147483781
CREDSSP_CRED_EX_VERSION = 0
CREDSSP_FLAG_REDIRECT = 1
def _define_KeyCredentialManagerGetOperationErrorStates():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Credentials.KeyCredentialManagerOperationType,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Security.Credentials.KeyCredentialManagerOperationErrorStates))(('KeyCredentialManagerGetOperationErrorStates', windll['KeyCredMgr.dll']), ((1, 'keyCredentialManagerOperationType'),(1, 'isReady'),(1, 'keyCredentialManagerOperationErrorStates'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_KeyCredentialManagerShowUIOperation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Security.Credentials.KeyCredentialManagerOperationType)(('KeyCredentialManagerShowUIOperation', windll['KeyCredMgr.dll']), ((1, 'hWndOwner'),(1, 'keyCredentialManagerOperationType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_KeyCredentialManagerGetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Credentials.KeyCredentialManagerInfo_head)))(('KeyCredentialManagerGetInformation', windll['KeyCredMgr.dll']), ((1, 'keyCredentialManagerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_KeyCredentialManagerFreeInformation():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Credentials.KeyCredentialManagerInfo_head))(('KeyCredentialManagerFreeInformation', windll['KeyCredMgr.dll']), ((1, 'keyCredentialManagerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredWriteW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIALW_head),UInt32)(('CredWriteW', windll['ADVAPI32.dll']), ((1, 'Credential'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredWriteA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIALA_head),UInt32)(('CredWriteA', windll['ADVAPI32.dll']), ((1, 'Credential'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredReadW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIALW_head)))(('CredReadW', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredReadA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIALA_head)))(('CredReadA', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredEnumerateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Security.Credentials.CRED_ENUMERATE_FLAGS,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Credentials.CREDENTIALW_head))))(('CredEnumerateW', windll['ADVAPI32.dll']), ((1, 'Filter'),(1, 'Flags'),(1, 'Count'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredEnumerateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Security.Credentials.CRED_ENUMERATE_FLAGS,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Credentials.CREDENTIALA_head))))(('CredEnumerateA', windll['ADVAPI32.dll']), ((1, 'Filter'),(1, 'Flags'),(1, 'Count'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredWriteDomainCredentialsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head),POINTER(win32more.Security.Credentials.CREDENTIALW_head),UInt32)(('CredWriteDomainCredentialsW', windll['ADVAPI32.dll']), ((1, 'TargetInfo'),(1, 'Credential'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredWriteDomainCredentialsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head),POINTER(win32more.Security.Credentials.CREDENTIALA_head),UInt32)(('CredWriteDomainCredentialsA', windll['ADVAPI32.dll']), ((1, 'TargetInfo'),(1, 'Credential'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredReadDomainCredentialsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head),UInt32,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Credentials.CREDENTIALW_head))))(('CredReadDomainCredentialsW', windll['ADVAPI32.dll']), ((1, 'TargetInfo'),(1, 'Flags'),(1, 'Count'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredReadDomainCredentialsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head),UInt32,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.Security.Credentials.CREDENTIALA_head))))(('CredReadDomainCredentialsA', windll['ADVAPI32.dll']), ((1, 'TargetInfo'),(1, 'Flags'),(1, 'Count'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredDeleteW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32)(('CredDeleteW', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredDeleteA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,UInt32)(('CredDeleteA', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredRenameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32)(('CredRenameW', windll['ADVAPI32.dll']), ((1, 'OldTargetName'),(1, 'NewTargetName'),(1, 'Type'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredRenameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32)(('CredRenameA', windll['ADVAPI32.dll']), ((1, 'OldTargetName'),(1, 'NewTargetName'),(1, 'Type'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredGetTargetInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head)))(('CredGetTargetInfoW', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Flags'),(1, 'TargetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredGetTargetInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head)))(('CredGetTargetInfoA', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Flags'),(1, 'TargetInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredMarshalCredentialW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_MARSHAL_TYPE,c_void_p,POINTER(win32more.Foundation.PWSTR))(('CredMarshalCredentialW', windll['ADVAPI32.dll']), ((1, 'CredType'),(1, 'Credential'),(1, 'MarshaledCredential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredMarshalCredentialA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_MARSHAL_TYPE,c_void_p,POINTER(win32more.Foundation.PSTR))(('CredMarshalCredentialA', windll['ADVAPI32.dll']), ((1, 'CredType'),(1, 'Credential'),(1, 'MarshaledCredential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnmarshalCredentialW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Security.Credentials.CRED_MARSHAL_TYPE),POINTER(c_void_p))(('CredUnmarshalCredentialW', windll['ADVAPI32.dll']), ((1, 'MarshaledCredential'),(1, 'CredType'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnmarshalCredentialA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.Credentials.CRED_MARSHAL_TYPE),POINTER(c_void_p))(('CredUnmarshalCredentialA', windll['ADVAPI32.dll']), ((1, 'MarshaledCredential'),(1, 'CredType'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredIsMarshaledCredentialW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('CredIsMarshaledCredentialW', windll['ADVAPI32.dll']), ((1, 'MarshaledCredential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredIsMarshaledCredentialA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('CredIsMarshaledCredentialA', windll['ADVAPI32.dll']), ((1, 'MarshaledCredential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnPackAuthenticationBufferW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_PACK_FLAGS,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32))(('CredUnPackAuthenticationBufferW', windll['credui.dll']), ((1, 'dwFlags'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'pszUserName'),(1, 'pcchMaxUserName'),(1, 'pszDomainName'),(1, 'pcchMaxDomainName'),(1, 'pszPassword'),(1, 'pcchMaxPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnPackAuthenticationBufferA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_PACK_FLAGS,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32))(('CredUnPackAuthenticationBufferA', windll['credui.dll']), ((1, 'dwFlags'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'pszUserName'),(1, 'pcchlMaxUserName'),(1, 'pszDomainName'),(1, 'pcchMaxDomainName'),(1, 'pszPassword'),(1, 'pcchMaxPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredPackAuthenticationBufferW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_PACK_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32))(('CredPackAuthenticationBufferW', windll['credui.dll']), ((1, 'dwFlags'),(1, 'pszUserName'),(1, 'pszPassword'),(1, 'pPackedCredentials'),(1, 'pcbPackedCredentials'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredPackAuthenticationBufferA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Credentials.CRED_PACK_FLAGS,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_char_p_no,POINTER(UInt32))(('CredPackAuthenticationBufferA', windll['credui.dll']), ((1, 'dwFlags'),(1, 'pszUserName'),(1, 'pszPassword'),(1, 'pPackedCredentials'),(1, 'pcbPackedCredentials'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredProtectW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Security.Credentials.CRED_PROTECTION_TYPE))(('CredProtectW', windll['ADVAPI32.dll']), ((1, 'fAsSelf'),(1, 'pszCredentials'),(1, 'cchCredentials'),(1, 'pszProtectedCredentials'),(1, 'pcchMaxChars'),(1, 'ProtectionType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredProtectA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(win32more.Security.Credentials.CRED_PROTECTION_TYPE))(('CredProtectA', windll['ADVAPI32.dll']), ((1, 'fAsSelf'),(1, 'pszCredentials'),(1, 'cchCredentials'),(1, 'pszProtectedCredentials'),(1, 'pcchMaxChars'),(1, 'ProtectionType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnprotectW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('CredUnprotectW', windll['ADVAPI32.dll']), ((1, 'fAsSelf'),(1, 'pszProtectedCredentials'),(1, 'cchProtectedCredentials'),(1, 'pszCredentials'),(1, 'pcchMaxChars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUnprotectA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(UInt32))(('CredUnprotectA', windll['ADVAPI32.dll']), ((1, 'fAsSelf'),(1, 'pszProtectedCredentials'),(1, 'cchProtectedCredentials'),(1, 'pszCredentials'),(1, 'pcchMaxChars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredIsProtectedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Security.Credentials.CRED_PROTECTION_TYPE))(('CredIsProtectedW', windll['ADVAPI32.dll']), ((1, 'pszProtectedCredentials'),(1, 'pProtectionType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredIsProtectedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.Credentials.CRED_PROTECTION_TYPE))(('CredIsProtectedA', windll['ADVAPI32.dll']), ((1, 'pszProtectedCredentials'),(1, 'pProtectionType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredFindBestCredentialW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIALW_head)))(('CredFindBestCredentialW', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredFindBestCredentialA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(POINTER(win32more.Security.Credentials.CREDENTIALA_head)))(('CredFindBestCredentialA', windll['ADVAPI32.dll']), ((1, 'TargetName'),(1, 'Type'),(1, 'Flags'),(1, 'Credential'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredGetSessionTypes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32))(('CredGetSessionTypes', windll['ADVAPI32.dll']), ((1, 'MaximumPersistCount'),(1, 'MaximumPersist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('CredFree', windll['ADVAPI32.dll']), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIPromptForCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Credentials.CREDUI_INFOW_head),win32more.Foundation.PWSTR,POINTER(win32more.Security.Credentials.SecHandle_head),UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUI_FLAGS)(('CredUIPromptForCredentialsW', windll['credui.dll']), ((1, 'pUiInfo'),(1, 'pszTargetName'),(1, 'pContext'),(1, 'dwAuthError'),(1, 'pszUserName'),(1, 'ulUserNameBufferSize'),(1, 'pszPassword'),(1, 'ulPasswordBufferSize'),(1, 'save'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIPromptForCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Credentials.CREDUI_INFOA_head),win32more.Foundation.PSTR,POINTER(win32more.Security.Credentials.SecHandle_head),UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUI_FLAGS)(('CredUIPromptForCredentialsA', windll['credui.dll']), ((1, 'pUiInfo'),(1, 'pszTargetName'),(1, 'pContext'),(1, 'dwAuthError'),(1, 'pszUserName'),(1, 'ulUserNameBufferSize'),(1, 'pszPassword'),(1, 'ulPasswordBufferSize'),(1, 'save'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIPromptForWindowsCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Credentials.CREDUI_INFOW_head),UInt32,POINTER(UInt32),c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUIWIN_FLAGS)(('CredUIPromptForWindowsCredentialsW', windll['credui.dll']), ((1, 'pUiInfo'),(1, 'dwAuthError'),(1, 'pulAuthPackage'),(1, 'pvInAuthBuffer'),(1, 'ulInAuthBufferSize'),(1, 'ppvOutAuthBuffer'),(1, 'pulOutAuthBufferSize'),(1, 'pfSave'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIPromptForWindowsCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Credentials.CREDUI_INFOA_head),UInt32,POINTER(UInt32),c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUIWIN_FLAGS)(('CredUIPromptForWindowsCredentialsA', windll['credui.dll']), ((1, 'pUiInfo'),(1, 'dwAuthError'),(1, 'pulAuthPackage'),(1, 'pvInAuthBuffer'),(1, 'ulInAuthBufferSize'),(1, 'ppvOutAuthBuffer'),(1, 'pulOutAuthBufferSize'),(1, 'pfSave'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIParseUserNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32)(('CredUIParseUserNameW', windll['credui.dll']), ((1, 'UserName'),(1, 'user'),(1, 'userBufferSize'),(1, 'domain'),(1, 'domainBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIParseUserNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32)(('CredUIParseUserNameA', windll['credui.dll']), ((1, 'userName'),(1, 'user'),(1, 'userBufferSize'),(1, 'domain'),(1, 'domainBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUICmdLinePromptForCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Security.Credentials.SecHandle_head),UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUI_FLAGS)(('CredUICmdLinePromptForCredentialsW', windll['credui.dll']), ((1, 'pszTargetName'),(1, 'pContext'),(1, 'dwAuthError'),(1, 'UserName'),(1, 'ulUserBufferSize'),(1, 'pszPassword'),(1, 'ulPasswordBufferSize'),(1, 'pfSave'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUICmdLinePromptForCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.Security.Credentials.SecHandle_head),UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.BOOL),win32more.Security.Credentials.CREDUI_FLAGS)(('CredUICmdLinePromptForCredentialsA', windll['credui.dll']), ((1, 'pszTargetName'),(1, 'pContext'),(1, 'dwAuthError'),(1, 'UserName'),(1, 'ulUserBufferSize'),(1, 'pszPassword'),(1, 'ulPasswordBufferSize'),(1, 'pfSave'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIConfirmCredentialsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CredUIConfirmCredentialsW', windll['credui.dll']), ((1, 'pszTargetName'),(1, 'bConfirm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIConfirmCredentialsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOL)(('CredUIConfirmCredentialsA', windll['credui.dll']), ((1, 'pszTargetName'),(1, 'bConfirm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIStoreSSOCredW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CredUIStoreSSOCredW', windll['credui.dll']), ((1, 'pszRealm'),(1, 'pszUsername'),(1, 'pszPassword'),(1, 'bPersist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CredUIReadSSOCredW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('CredUIReadSSOCredW', windll['credui.dll']), ((1, 'pszRealm'),(1, 'ppszUsername'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardEstablishContext():
    try:
        return WINFUNCTYPE(Int32,win32more.Security.Credentials.SCARD_SCOPE,c_void_p,c_void_p,POINTER(UIntPtr))(('SCardEstablishContext', windll['WinSCard.dll']), ((1, 'dwScope'),(1, 'pvReserved1'),(1, 'pvReserved2'),(1, 'phContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardReleaseContext():
    try:
        return WINFUNCTYPE(Int32,UIntPtr)(('SCardReleaseContext', windll['WinSCard.dll']), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIsValidContext():
    try:
        return WINFUNCTYPE(Int32,UIntPtr)(('SCardIsValidContext', windll['WinSCard.dll']), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReaderGroupsA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardListReaderGroupsA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszGroups'),(1, 'pcchGroups'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReaderGroupsW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardListReaderGroupsW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszGroups'),(1, 'pcchGroups'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReadersA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardListReadersA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszGroups'),(1, 'mszReaders'),(1, 'pcchReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReadersW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardListReadersW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszGroups'),(1, 'mszReaders'),(1, 'pcchReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListCardsA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,c_char_p_no,POINTER(Guid),UInt32,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardListCardsA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'pbAtr'),(1, 'rgquidInterfaces'),(1, 'cguidInterfaceCount'),(1, 'mszCards'),(1, 'pcchCards'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListCardsW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,c_char_p_no,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardListCardsW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'pbAtr'),(1, 'rgquidInterfaces'),(1, 'cguidInterfaceCount'),(1, 'mszCards'),(1, 'pcchCards'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListInterfacesA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(Guid),POINTER(UInt32))(('SCardListInterfacesA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCard'),(1, 'pguidInterfaces'),(1, 'pcguidInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListInterfacesW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(UInt32))(('SCardListInterfacesW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCard'),(1, 'pguidInterfaces'),(1, 'pcguidInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetProviderIdA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(Guid))(('SCardGetProviderIdA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCard'),(1, 'pguidProviderId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetProviderIdW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(Guid))(('SCardGetProviderIdW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCard'),(1, 'pguidProviderId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetCardTypeProviderNameA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardGetCardTypeProviderNameA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'dwProviderId'),(1, 'szProvider'),(1, 'pcchProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetCardTypeProviderNameW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardGetCardTypeProviderNameW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'dwProviderId'),(1, 'szProvider'),(1, 'pcchProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceReaderGroupA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR)(('SCardIntroduceReaderGroupA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceReaderGroupW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR)(('SCardIntroduceReaderGroupW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetReaderGroupA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR)(('SCardForgetReaderGroupA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetReaderGroupW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR)(('SCardForgetReaderGroupW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceReaderA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SCardIntroduceReaderA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceReaderW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SCardIntroduceReaderW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetReaderA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR)(('SCardForgetReaderA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetReaderW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR)(('SCardForgetReaderW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardAddReaderToGroupA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SCardAddReaderToGroupA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardAddReaderToGroupW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SCardAddReaderToGroupW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardRemoveReaderFromGroupA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SCardRemoveReaderFromGroupA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardRemoveReaderFromGroupW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SCardRemoveReaderFromGroupW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szGroupName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceCardTypeA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,c_char_p_no,UInt32)(('SCardIntroduceCardTypeA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'pguidPrimaryProvider'),(1, 'rgguidInterfaces'),(1, 'dwInterfaceCount'),(1, 'pbAtr'),(1, 'pbAtrMask'),(1, 'cbAtrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardIntroduceCardTypeW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(Guid),UInt32,c_char_p_no,c_char_p_no,UInt32)(('SCardIntroduceCardTypeW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'pguidPrimaryProvider'),(1, 'rgguidInterfaces'),(1, 'dwInterfaceCount'),(1, 'pbAtr'),(1, 'pbAtrMask'),(1, 'cbAtrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardSetCardTypeProviderNameA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('SCardSetCardTypeProviderNameA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'dwProviderId'),(1, 'szProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardSetCardTypeProviderNameW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('SCardSetCardTypeProviderNameW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),(1, 'dwProviderId'),(1, 'szProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetCardTypeA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR)(('SCardForgetCardTypeA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardForgetCardTypeW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR)(('SCardForgetCardTypeW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szCardName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardFreeMemory():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,c_void_p)(('SCardFreeMemory', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'pvMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardAccessStartedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,)(('SCardAccessStartedEvent', windll['WinSCard.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardReleaseStartedEvent():
    try:
        return WINFUNCTYPE(Void,)(('SCardReleaseStartedEvent', windll['WinSCard.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardLocateCardsA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Security.Credentials.SCARD_READERSTATEA_head),UInt32)(('SCardLocateCardsA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszCards'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardLocateCardsW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(win32more.Security.Credentials.SCARD_READERSTATEW_head),UInt32)(('SCardLocateCardsW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'mszCards'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardLocateCardsByATRA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(win32more.Security.Credentials.SCARD_ATRMASK_head),UInt32,POINTER(win32more.Security.Credentials.SCARD_READERSTATEA_head),UInt32)(('SCardLocateCardsByATRA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'rgAtrMasks'),(1, 'cAtrs'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardLocateCardsByATRW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(win32more.Security.Credentials.SCARD_ATRMASK_head),UInt32,POINTER(win32more.Security.Credentials.SCARD_READERSTATEW_head),UInt32)(('SCardLocateCardsByATRW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'rgAtrMasks'),(1, 'cAtrs'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetStatusChangeA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,POINTER(win32more.Security.Credentials.SCARD_READERSTATEA_head),UInt32)(('SCardGetStatusChangeA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'dwTimeout'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetStatusChangeW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,POINTER(win32more.Security.Credentials.SCARD_READERSTATEW_head),UInt32)(('SCardGetStatusChangeW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'dwTimeout'),(1, 'rgReaderStates'),(1, 'cReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardCancel():
    try:
        return WINFUNCTYPE(Int32,UIntPtr)(('SCardCancel', windll['WinSCard.dll']), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardConnectA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(UIntPtr),POINTER(UInt32))(('SCardConnectA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReader'),(1, 'dwShareMode'),(1, 'dwPreferredProtocols'),(1, 'phCard'),(1, 'pdwActiveProtocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardConnectW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UIntPtr),POINTER(UInt32))(('SCardConnectW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReader'),(1, 'dwShareMode'),(1, 'dwPreferredProtocols'),(1, 'phCard'),(1, 'pdwActiveProtocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardReconnect():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,UInt32,UInt32,POINTER(UInt32))(('SCardReconnect', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwShareMode'),(1, 'dwPreferredProtocols'),(1, 'dwInitialization'),(1, 'pdwActiveProtocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardDisconnect():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32)(('SCardDisconnect', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwDisposition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardBeginTransaction():
    try:
        return WINFUNCTYPE(Int32,UIntPtr)(('SCardBeginTransaction', windll['WinSCard.dll']), ((1, 'hCard'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardEndTransaction():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32)(('SCardEndTransaction', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwDisposition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardState():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32))(('SCardState', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'pdwState'),(1, 'pdwProtocol'),(1, 'pbAtr'),(1, 'pcbAtrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardStatusA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32))(('SCardStatusA', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'mszReaderNames'),(1, 'pcchReaderLen'),(1, 'pdwState'),(1, 'pdwProtocol'),(1, 'pbAtr'),(1, 'pcbAtrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardStatusW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32))(('SCardStatusW', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'mszReaderNames'),(1, 'pcchReaderLen'),(1, 'pdwState'),(1, 'pdwProtocol'),(1, 'pbAtr'),(1, 'pcbAtrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardTransmit():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(win32more.Security.Credentials.SCARD_IO_REQUEST_head),c_char_p_no,UInt32,POINTER(win32more.Security.Credentials.SCARD_IO_REQUEST_head),c_char_p_no,POINTER(UInt32))(('SCardTransmit', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'pioSendPci'),(1, 'pbSendBuffer'),(1, 'cbSendLength'),(1, 'pioRecvPci'),(1, 'pbRecvBuffer'),(1, 'pcbRecvLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetTransmitCount():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(UInt32))(('SCardGetTransmitCount', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'pcTransmitCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardControl():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(('SCardControl', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwControlCode'),(1, 'lpInBuffer'),(1, 'cbInBufferSize'),(1, 'lpOutBuffer'),(1, 'cbOutBufferSize'),(1, 'lpBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetAttrib():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,c_char_p_no,POINTER(UInt32))(('SCardGetAttrib', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwAttrId'),(1, 'pbAttr'),(1, 'pcbAttrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardSetAttrib():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32,c_char_p_no,UInt32)(('SCardSetAttrib', windll['WinSCard.dll']), ((1, 'hCard'),(1, 'dwAttrId'),(1, 'pbAttr'),(1, 'cbAttrLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardUIDlgSelectCardA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Security.Credentials.OPENCARDNAME_EXA_head))(('SCardUIDlgSelectCardA', windll['SCARDDLG.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardUIDlgSelectCardW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Security.Credentials.OPENCARDNAME_EXW_head))(('SCardUIDlgSelectCardW', windll['SCARDDLG.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOpenCardNameA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Security.Credentials.OPENCARDNAMEA_head))(('GetOpenCardNameA', windll['SCARDDLG.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOpenCardNameW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Security.Credentials.OPENCARDNAMEW_head))(('GetOpenCardNameW', windll['SCARDDLG.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardDlgExtendedError():
    try:
        return WINFUNCTYPE(Int32,)(('SCardDlgExtendedError', windll['SCARDDLG.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardReadCacheA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(Guid),UInt32,win32more.Foundation.PSTR,c_char_p_no,POINTER(UInt32))(('SCardReadCacheA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'CardIdentifier'),(1, 'FreshnessCounter'),(1, 'LookupName'),(1, 'Data'),(1, 'DataLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardReadCacheW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32))(('SCardReadCacheW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'CardIdentifier'),(1, 'FreshnessCounter'),(1, 'LookupName'),(1, 'Data'),(1, 'DataLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardWriteCacheA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(Guid),UInt32,win32more.Foundation.PSTR,c_char_p_no,UInt32)(('SCardWriteCacheA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'CardIdentifier'),(1, 'FreshnessCounter'),(1, 'LookupName'),(1, 'Data'),(1, 'DataLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardWriteCacheW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32)(('SCardWriteCacheW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'CardIdentifier'),(1, 'FreshnessCounter'),(1, 'LookupName'),(1, 'Data'),(1, 'DataLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetReaderIconA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,c_char_p_no,POINTER(UInt32))(('SCardGetReaderIconA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'pbIcon'),(1, 'pcbIcon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetReaderIconW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,c_char_p_no,POINTER(UInt32))(('SCardGetReaderIconW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'pbIcon'),(1, 'pcbIcon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetDeviceTypeIdA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardGetDeviceTypeIdA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'pdwDeviceTypeId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetDeviceTypeIdW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardGetDeviceTypeIdW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'pdwDeviceTypeId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetReaderDeviceInstanceIdA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardGetReaderDeviceInstanceIdA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szDeviceInstanceId'),(1, 'pcchDeviceInstanceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardGetReaderDeviceInstanceIdW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardGetReaderDeviceInstanceIdW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szReaderName'),(1, 'szDeviceInstanceId'),(1, 'pcchDeviceInstanceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReadersWithDeviceInstanceIdA():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('SCardListReadersWithDeviceInstanceIdA', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szDeviceInstanceId'),(1, 'mszReaders'),(1, 'pcchReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardListReadersWithDeviceInstanceIdW():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('SCardListReadersWithDeviceInstanceIdW', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'szDeviceInstanceId'),(1, 'mszReaders'),(1, 'pcchReaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SCardAudit():
    try:
        return WINFUNCTYPE(Int32,UIntPtr,UInt32)(('SCardAudit', windll['WinSCard.dll']), ((1, 'hContext'),(1, 'dwEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BINARY_BLOB_CREDENTIAL_INFO_head():
    class BINARY_BLOB_CREDENTIAL_INFO(Structure):
        pass
    return BINARY_BLOB_CREDENTIAL_INFO
def _define_BINARY_BLOB_CREDENTIAL_INFO():
    BINARY_BLOB_CREDENTIAL_INFO = win32more.Security.Credentials.BINARY_BLOB_CREDENTIAL_INFO_head
    BINARY_BLOB_CREDENTIAL_INFO._fields_ = [
        ('cbBlob', UInt32),
        ('pbBlob', c_char_p_no),
    ]
    return BINARY_BLOB_CREDENTIAL_INFO
def _define_CERT_CREDENTIAL_INFO_head():
    class CERT_CREDENTIAL_INFO(Structure):
        pass
    return CERT_CREDENTIAL_INFO
def _define_CERT_CREDENTIAL_INFO():
    CERT_CREDENTIAL_INFO = win32more.Security.Credentials.CERT_CREDENTIAL_INFO_head
    CERT_CREDENTIAL_INFO._fields_ = [
        ('cbSize', UInt32),
        ('rgbHashOfCert', Byte * 20),
    ]
    return CERT_CREDENTIAL_INFO
CRED_ENUMERATE_FLAGS = UInt32
CRED_ENUMERATE_ALL_CREDENTIALS = 1
CRED_FLAGS = UInt32
CRED_FLAGS_PASSWORD_FOR_CERT = 1
CRED_FLAGS_PROMPT_NOW = 2
CRED_FLAGS_USERNAME_TARGET = 4
CRED_FLAGS_OWF_CRED_BLOB = 8
CRED_FLAGS_REQUIRE_CONFIRMATION = 16
CRED_FLAGS_WILDCARD_MATCH = 32
CRED_FLAGS_VSM_PROTECTED = 64
CRED_FLAGS_NGC_CERT = 128
CRED_FLAGS_VALID_FLAGS = 61695
CRED_FLAGS_VALID_INPUT_FLAGS = 61599
CRED_MARSHAL_TYPE = Int32
CRED_MARSHAL_TYPE_CertCredential = 1
CRED_MARSHAL_TYPE_UsernameTargetCredential = 2
CRED_MARSHAL_TYPE_BinaryBlobCredential = 3
CRED_MARSHAL_TYPE_UsernameForPackedCredentials = 4
CRED_MARSHAL_TYPE_BinaryBlobForSystem = 5
CRED_PACK_FLAGS = UInt32
CRED_PACK_PROTECTED_CREDENTIALS = 1
CRED_PACK_WOW_BUFFER = 2
CRED_PACK_GENERIC_CREDENTIALS = 4
CRED_PACK_ID_PROVIDER_CREDENTIALS = 8
CRED_PERSIST = UInt32
CRED_PERSIST_NONE = 0
CRED_PERSIST_SESSION = 1
CRED_PERSIST_LOCAL_MACHINE = 2
CRED_PERSIST_ENTERPRISE = 3
CRED_PROTECTION_TYPE = Int32
CRED_PROTECTION_TYPE_CredUnprotected = 0
CRED_PROTECTION_TYPE_CredUserProtection = 1
CRED_PROTECTION_TYPE_CredTrustedProtection = 2
CRED_PROTECTION_TYPE_CredForSystemProtection = 3
CRED_TYPE = UInt32
CRED_TYPE_GENERIC = 1
CRED_TYPE_DOMAIN_PASSWORD = 2
CRED_TYPE_DOMAIN_CERTIFICATE = 3
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD = 4
CRED_TYPE_GENERIC_CERTIFICATE = 5
CRED_TYPE_DOMAIN_EXTENDED = 6
CRED_TYPE_MAXIMUM = 7
CRED_TYPE_MAXIMUM_EX = 1007
def _define_CREDENTIAL_ATTRIBUTEA_head():
    class CREDENTIAL_ATTRIBUTEA(Structure):
        pass
    return CREDENTIAL_ATTRIBUTEA
def _define_CREDENTIAL_ATTRIBUTEA():
    CREDENTIAL_ATTRIBUTEA = win32more.Security.Credentials.CREDENTIAL_ATTRIBUTEA_head
    CREDENTIAL_ATTRIBUTEA._fields_ = [
        ('Keyword', win32more.Foundation.PSTR),
        ('Flags', UInt32),
        ('ValueSize', UInt32),
        ('Value', c_char_p_no),
    ]
    return CREDENTIAL_ATTRIBUTEA
def _define_CREDENTIAL_ATTRIBUTEW_head():
    class CREDENTIAL_ATTRIBUTEW(Structure):
        pass
    return CREDENTIAL_ATTRIBUTEW
def _define_CREDENTIAL_ATTRIBUTEW():
    CREDENTIAL_ATTRIBUTEW = win32more.Security.Credentials.CREDENTIAL_ATTRIBUTEW_head
    CREDENTIAL_ATTRIBUTEW._fields_ = [
        ('Keyword', win32more.Foundation.PWSTR),
        ('Flags', UInt32),
        ('ValueSize', UInt32),
        ('Value', c_char_p_no),
    ]
    return CREDENTIAL_ATTRIBUTEW
def _define_CREDENTIAL_TARGET_INFORMATIONA_head():
    class CREDENTIAL_TARGET_INFORMATIONA(Structure):
        pass
    return CREDENTIAL_TARGET_INFORMATIONA
def _define_CREDENTIAL_TARGET_INFORMATIONA():
    CREDENTIAL_TARGET_INFORMATIONA = win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONA_head
    CREDENTIAL_TARGET_INFORMATIONA._fields_ = [
        ('TargetName', win32more.Foundation.PSTR),
        ('NetbiosServerName', win32more.Foundation.PSTR),
        ('DnsServerName', win32more.Foundation.PSTR),
        ('NetbiosDomainName', win32more.Foundation.PSTR),
        ('DnsDomainName', win32more.Foundation.PSTR),
        ('DnsTreeName', win32more.Foundation.PSTR),
        ('PackageName', win32more.Foundation.PSTR),
        ('Flags', UInt32),
        ('CredTypeCount', UInt32),
        ('CredTypes', POINTER(UInt32)),
    ]
    return CREDENTIAL_TARGET_INFORMATIONA
def _define_CREDENTIAL_TARGET_INFORMATIONW_head():
    class CREDENTIAL_TARGET_INFORMATIONW(Structure):
        pass
    return CREDENTIAL_TARGET_INFORMATIONW
def _define_CREDENTIAL_TARGET_INFORMATIONW():
    CREDENTIAL_TARGET_INFORMATIONW = win32more.Security.Credentials.CREDENTIAL_TARGET_INFORMATIONW_head
    CREDENTIAL_TARGET_INFORMATIONW._fields_ = [
        ('TargetName', win32more.Foundation.PWSTR),
        ('NetbiosServerName', win32more.Foundation.PWSTR),
        ('DnsServerName', win32more.Foundation.PWSTR),
        ('NetbiosDomainName', win32more.Foundation.PWSTR),
        ('DnsDomainName', win32more.Foundation.PWSTR),
        ('DnsTreeName', win32more.Foundation.PWSTR),
        ('PackageName', win32more.Foundation.PWSTR),
        ('Flags', UInt32),
        ('CredTypeCount', UInt32),
        ('CredTypes', POINTER(UInt32)),
    ]
    return CREDENTIAL_TARGET_INFORMATIONW
def _define_CREDENTIALA_head():
    class CREDENTIALA(Structure):
        pass
    return CREDENTIALA
def _define_CREDENTIALA():
    CREDENTIALA = win32more.Security.Credentials.CREDENTIALA_head
    CREDENTIALA._fields_ = [
        ('Flags', win32more.Security.Credentials.CRED_FLAGS),
        ('Type', win32more.Security.Credentials.CRED_TYPE),
        ('TargetName', win32more.Foundation.PSTR),
        ('Comment', win32more.Foundation.PSTR),
        ('LastWritten', win32more.Foundation.FILETIME),
        ('CredentialBlobSize', UInt32),
        ('CredentialBlob', c_char_p_no),
        ('Persist', win32more.Security.Credentials.CRED_PERSIST),
        ('AttributeCount', UInt32),
        ('Attributes', POINTER(win32more.Security.Credentials.CREDENTIAL_ATTRIBUTEA_head)),
        ('TargetAlias', win32more.Foundation.PSTR),
        ('UserName', win32more.Foundation.PSTR),
    ]
    return CREDENTIALA
def _define_CREDENTIALW_head():
    class CREDENTIALW(Structure):
        pass
    return CREDENTIALW
def _define_CREDENTIALW():
    CREDENTIALW = win32more.Security.Credentials.CREDENTIALW_head
    CREDENTIALW._fields_ = [
        ('Flags', win32more.Security.Credentials.CRED_FLAGS),
        ('Type', win32more.Security.Credentials.CRED_TYPE),
        ('TargetName', win32more.Foundation.PWSTR),
        ('Comment', win32more.Foundation.PWSTR),
        ('LastWritten', win32more.Foundation.FILETIME),
        ('CredentialBlobSize', UInt32),
        ('CredentialBlob', c_char_p_no),
        ('Persist', win32more.Security.Credentials.CRED_PERSIST),
        ('AttributeCount', UInt32),
        ('Attributes', POINTER(win32more.Security.Credentials.CREDENTIAL_ATTRIBUTEW_head)),
        ('TargetAlias', win32more.Foundation.PWSTR),
        ('UserName', win32more.Foundation.PWSTR),
    ]
    return CREDENTIALW
CREDSPP_SUBMIT_TYPE = Int32
CREDSPP_SUBMIT_TYPE_CredsspPasswordCreds = 2
CREDSPP_SUBMIT_TYPE_CredsspSchannelCreds = 4
CREDSPP_SUBMIT_TYPE_CredsspCertificateCreds = 13
CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBoth = 50
CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBothOld = 51
CREDSPP_SUBMIT_TYPE_CredsspCredEx = 100
def _define_CREDSSP_CRED_head():
    class CREDSSP_CRED(Structure):
        pass
    return CREDSSP_CRED
def _define_CREDSSP_CRED():
    CREDSSP_CRED = win32more.Security.Credentials.CREDSSP_CRED_head
    CREDSSP_CRED._fields_ = [
        ('Type', win32more.Security.Credentials.CREDSPP_SUBMIT_TYPE),
        ('pSchannelCred', c_void_p),
        ('pSpnegoCred', c_void_p),
    ]
    return CREDSSP_CRED
def _define_CREDSSP_CRED_EX_head():
    class CREDSSP_CRED_EX(Structure):
        pass
    return CREDSSP_CRED_EX
def _define_CREDSSP_CRED_EX():
    CREDSSP_CRED_EX = win32more.Security.Credentials.CREDSSP_CRED_EX_head
    CREDSSP_CRED_EX._fields_ = [
        ('Type', win32more.Security.Credentials.CREDSPP_SUBMIT_TYPE),
        ('Version', UInt32),
        ('Flags', UInt32),
        ('Reserved', UInt32),
        ('Cred', win32more.Security.Credentials.CREDSSP_CRED),
    ]
    return CREDSSP_CRED_EX
CREDUI_FLAGS = UInt32
CREDUI_FLAGS_ALWAYS_SHOW_UI = 128
CREDUI_FLAGS_COMPLETE_USERNAME = 2048
CREDUI_FLAGS_DO_NOT_PERSIST = 2
CREDUI_FLAGS_EXCLUDE_CERTIFICATES = 8
CREDUI_FLAGS_EXPECT_CONFIRMATION = 131072
CREDUI_FLAGS_GENERIC_CREDENTIALS = 262144
CREDUI_FLAGS_INCORRECT_PASSWORD = 1
CREDUI_FLAGS_KEEP_USERNAME = 1048576
CREDUI_FLAGS_PASSWORD_ONLY_OK = 512
CREDUI_FLAGS_PERSIST = 4096
CREDUI_FLAGS_REQUEST_ADMINISTRATOR = 4
CREDUI_FLAGS_REQUIRE_CERTIFICATE = 16
CREDUI_FLAGS_REQUIRE_SMARTCARD = 256
CREDUI_FLAGS_SERVER_CREDENTIAL = 16384
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX = 64
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS = 524288
CREDUI_FLAGS_VALIDATE_USERNAME = 1024
def _define_CREDUI_INFOA_head():
    class CREDUI_INFOA(Structure):
        pass
    return CREDUI_INFOA
def _define_CREDUI_INFOA():
    CREDUI_INFOA = win32more.Security.Credentials.CREDUI_INFOA_head
    CREDUI_INFOA._fields_ = [
        ('cbSize', UInt32),
        ('hwndParent', win32more.Foundation.HWND),
        ('pszMessageText', win32more.Foundation.PSTR),
        ('pszCaptionText', win32more.Foundation.PSTR),
        ('hbmBanner', win32more.Graphics.Gdi.HBITMAP),
    ]
    return CREDUI_INFOA
def _define_CREDUI_INFOW_head():
    class CREDUI_INFOW(Structure):
        pass
    return CREDUI_INFOW
def _define_CREDUI_INFOW():
    CREDUI_INFOW = win32more.Security.Credentials.CREDUI_INFOW_head
    CREDUI_INFOW._fields_ = [
        ('cbSize', UInt32),
        ('hwndParent', win32more.Foundation.HWND),
        ('pszMessageText', win32more.Foundation.PWSTR),
        ('pszCaptionText', win32more.Foundation.PWSTR),
        ('hbmBanner', win32more.Graphics.Gdi.HBITMAP),
    ]
    return CREDUI_INFOW
CREDUIWIN_FLAGS = UInt32
CREDUIWIN_GENERIC = 1
CREDUIWIN_CHECKBOX = 2
CREDUIWIN_AUTHPACKAGE_ONLY = 16
CREDUIWIN_IN_CRED_ONLY = 32
CREDUIWIN_ENUMERATE_ADMINS = 256
CREDUIWIN_ENUMERATE_CURRENT_USER = 512
CREDUIWIN_SECURE_PROMPT = 4096
CREDUIWIN_PREPROMPTING = 8192
CREDUIWIN_PACK_32_WOW = 268435456
def _define_KeyCredentialManagerInfo_head():
    class KeyCredentialManagerInfo(Structure):
        pass
    return KeyCredentialManagerInfo
def _define_KeyCredentialManagerInfo():
    KeyCredentialManagerInfo = win32more.Security.Credentials.KeyCredentialManagerInfo_head
    KeyCredentialManagerInfo._fields_ = [
        ('containerId', Guid),
    ]
    return KeyCredentialManagerInfo
KeyCredentialManagerOperationErrorStates = UInt32
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateNone = 0
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateDeviceJoinFailure = 1
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateTokenFailure = 2
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateCertificateFailure = 4
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateRemoteSessionFailure = 8
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePolicyFailure = 16
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateHardwareFailure = 32
KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePinExistsFailure = 64
KeyCredentialManagerOperationType = Int32
KeyCredentialManagerOperationType_KeyCredentialManagerProvisioning = 0
KeyCredentialManagerOperationType_KeyCredentialManagerPinChange = 1
KeyCredentialManagerOperationType_KeyCredentialManagerPinReset = 2
def _define_LPOCNCHKPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UIntPtr,UIntPtr,c_void_p)
def _define_LPOCNCONNPROCA():
    return WINFUNCTYPE(UIntPtr,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,c_void_p)
def _define_LPOCNCONNPROCW():
    return WINFUNCTYPE(UIntPtr,UIntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p)
def _define_LPOCNDSCPROC():
    return WINFUNCTYPE(Void,UIntPtr,UIntPtr,c_void_p)
def _define_OPENCARD_SEARCH_CRITERIAA_head():
    class OPENCARD_SEARCH_CRITERIAA(Structure):
        pass
    return OPENCARD_SEARCH_CRITERIAA
def _define_OPENCARD_SEARCH_CRITERIAA():
    OPENCARD_SEARCH_CRITERIAA = win32more.Security.Credentials.OPENCARD_SEARCH_CRITERIAA_head
    OPENCARD_SEARCH_CRITERIAA._fields_ = [
        ('dwStructSize', UInt32),
        ('lpstrGroupNames', win32more.Foundation.PSTR),
        ('nMaxGroupNames', UInt32),
        ('rgguidInterfaces', POINTER(Guid)),
        ('cguidInterfaces', UInt32),
        ('lpstrCardNames', win32more.Foundation.PSTR),
        ('nMaxCardNames', UInt32),
        ('lpfnCheck', win32more.Security.Credentials.LPOCNCHKPROC),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCA),
        ('lpfnDisconnect', win32more.Security.Credentials.LPOCNDSCPROC),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
    ]
    return OPENCARD_SEARCH_CRITERIAA
def _define_OPENCARD_SEARCH_CRITERIAW_head():
    class OPENCARD_SEARCH_CRITERIAW(Structure):
        pass
    return OPENCARD_SEARCH_CRITERIAW
def _define_OPENCARD_SEARCH_CRITERIAW():
    OPENCARD_SEARCH_CRITERIAW = win32more.Security.Credentials.OPENCARD_SEARCH_CRITERIAW_head
    OPENCARD_SEARCH_CRITERIAW._fields_ = [
        ('dwStructSize', UInt32),
        ('lpstrGroupNames', win32more.Foundation.PWSTR),
        ('nMaxGroupNames', UInt32),
        ('rgguidInterfaces', POINTER(Guid)),
        ('cguidInterfaces', UInt32),
        ('lpstrCardNames', win32more.Foundation.PWSTR),
        ('nMaxCardNames', UInt32),
        ('lpfnCheck', win32more.Security.Credentials.LPOCNCHKPROC),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCW),
        ('lpfnDisconnect', win32more.Security.Credentials.LPOCNDSCPROC),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
    ]
    return OPENCARD_SEARCH_CRITERIAW
def _define_OPENCARDNAME_EXA_head():
    class OPENCARDNAME_EXA(Structure):
        pass
    return OPENCARDNAME_EXA
def _define_OPENCARDNAME_EXA():
    OPENCARDNAME_EXA = win32more.Security.Credentials.OPENCARDNAME_EXA_head
    OPENCARDNAME_EXA._fields_ = [
        ('dwStructSize', UInt32),
        ('hSCardContext', UIntPtr),
        ('hwndOwner', win32more.Foundation.HWND),
        ('dwFlags', UInt32),
        ('lpstrTitle', win32more.Foundation.PSTR),
        ('lpstrSearchDesc', win32more.Foundation.PSTR),
        ('hIcon', win32more.UI.WindowsAndMessaging.HICON),
        ('pOpenCardSearchCriteria', POINTER(win32more.Security.Credentials.OPENCARD_SEARCH_CRITERIAA_head)),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCA),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
        ('lpstrRdr', win32more.Foundation.PSTR),
        ('nMaxRdr', UInt32),
        ('lpstrCard', win32more.Foundation.PSTR),
        ('nMaxCard', UInt32),
        ('dwActiveProtocol', UInt32),
        ('hCardHandle', UIntPtr),
    ]
    return OPENCARDNAME_EXA
def _define_OPENCARDNAME_EXW_head():
    class OPENCARDNAME_EXW(Structure):
        pass
    return OPENCARDNAME_EXW
def _define_OPENCARDNAME_EXW():
    OPENCARDNAME_EXW = win32more.Security.Credentials.OPENCARDNAME_EXW_head
    OPENCARDNAME_EXW._fields_ = [
        ('dwStructSize', UInt32),
        ('hSCardContext', UIntPtr),
        ('hwndOwner', win32more.Foundation.HWND),
        ('dwFlags', UInt32),
        ('lpstrTitle', win32more.Foundation.PWSTR),
        ('lpstrSearchDesc', win32more.Foundation.PWSTR),
        ('hIcon', win32more.UI.WindowsAndMessaging.HICON),
        ('pOpenCardSearchCriteria', POINTER(win32more.Security.Credentials.OPENCARD_SEARCH_CRITERIAW_head)),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCW),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
        ('lpstrRdr', win32more.Foundation.PWSTR),
        ('nMaxRdr', UInt32),
        ('lpstrCard', win32more.Foundation.PWSTR),
        ('nMaxCard', UInt32),
        ('dwActiveProtocol', UInt32),
        ('hCardHandle', UIntPtr),
    ]
    return OPENCARDNAME_EXW
def _define_OPENCARDNAMEA_head():
    class OPENCARDNAMEA(Structure):
        pass
    return OPENCARDNAMEA
def _define_OPENCARDNAMEA():
    OPENCARDNAMEA = win32more.Security.Credentials.OPENCARDNAMEA_head
    OPENCARDNAMEA._fields_ = [
        ('dwStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hSCardContext', UIntPtr),
        ('lpstrGroupNames', win32more.Foundation.PSTR),
        ('nMaxGroupNames', UInt32),
        ('lpstrCardNames', win32more.Foundation.PSTR),
        ('nMaxCardNames', UInt32),
        ('rgguidInterfaces', POINTER(Guid)),
        ('cguidInterfaces', UInt32),
        ('lpstrRdr', win32more.Foundation.PSTR),
        ('nMaxRdr', UInt32),
        ('lpstrCard', win32more.Foundation.PSTR),
        ('nMaxCard', UInt32),
        ('lpstrTitle', win32more.Foundation.PSTR),
        ('dwFlags', UInt32),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
        ('dwActiveProtocol', UInt32),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCA),
        ('lpfnCheck', win32more.Security.Credentials.LPOCNCHKPROC),
        ('lpfnDisconnect', win32more.Security.Credentials.LPOCNDSCPROC),
        ('hCardHandle', UIntPtr),
    ]
    return OPENCARDNAMEA
def _define_OPENCARDNAMEW_head():
    class OPENCARDNAMEW(Structure):
        pass
    return OPENCARDNAMEW
def _define_OPENCARDNAMEW():
    OPENCARDNAMEW = win32more.Security.Credentials.OPENCARDNAMEW_head
    OPENCARDNAMEW._fields_ = [
        ('dwStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hSCardContext', UIntPtr),
        ('lpstrGroupNames', win32more.Foundation.PWSTR),
        ('nMaxGroupNames', UInt32),
        ('lpstrCardNames', win32more.Foundation.PWSTR),
        ('nMaxCardNames', UInt32),
        ('rgguidInterfaces', POINTER(Guid)),
        ('cguidInterfaces', UInt32),
        ('lpstrRdr', win32more.Foundation.PWSTR),
        ('nMaxRdr', UInt32),
        ('lpstrCard', win32more.Foundation.PWSTR),
        ('nMaxCard', UInt32),
        ('lpstrTitle', win32more.Foundation.PWSTR),
        ('dwFlags', UInt32),
        ('pvUserData', c_void_p),
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
        ('dwActiveProtocol', UInt32),
        ('lpfnConnect', win32more.Security.Credentials.LPOCNCONNPROCW),
        ('lpfnCheck', win32more.Security.Credentials.LPOCNCHKPROC),
        ('lpfnDisconnect', win32more.Security.Credentials.LPOCNDSCPROC),
        ('hCardHandle', UIntPtr),
    ]
    return OPENCARDNAMEW
def _define_READER_SEL_REQUEST_head():
    class READER_SEL_REQUEST(Structure):
        pass
    return READER_SEL_REQUEST
def _define_READER_SEL_REQUEST():
    READER_SEL_REQUEST = win32more.Security.Credentials.READER_SEL_REQUEST_head
    class READER_SEL_REQUEST__Anonymous_e__Union(Union):
        pass
    class READER_SEL_REQUEST__Anonymous_e__Union__ReaderAndContainerParameter_e__Struct(Structure):
        pass
    READER_SEL_REQUEST__Anonymous_e__Union__ReaderAndContainerParameter_e__Struct._fields_ = [
        ('cbReaderNameOffset', UInt32),
        ('cchReaderNameLength', UInt32),
        ('cbContainerNameOffset', UInt32),
        ('cchContainerNameLength', UInt32),
        ('dwDesiredCardModuleVersion', UInt32),
        ('dwCspFlags', UInt32),
    ]
    class READER_SEL_REQUEST__Anonymous_e__Union__SerialNumberParameter_e__Struct(Structure):
        pass
    READER_SEL_REQUEST__Anonymous_e__Union__SerialNumberParameter_e__Struct._fields_ = [
        ('cbSerialNumberOffset', UInt32),
        ('cbSerialNumberLength', UInt32),
        ('dwDesiredCardModuleVersion', UInt32),
    ]
    READER_SEL_REQUEST__Anonymous_e__Union._fields_ = [
        ('ReaderAndContainerParameter', READER_SEL_REQUEST__Anonymous_e__Union__ReaderAndContainerParameter_e__Struct),
        ('SerialNumberParameter', READER_SEL_REQUEST__Anonymous_e__Union__SerialNumberParameter_e__Struct),
    ]
    READER_SEL_REQUEST._anonymous_ = [
        'Anonymous',
    ]
    READER_SEL_REQUEST._fields_ = [
        ('dwShareMode', UInt32),
        ('dwPreferredProtocols', UInt32),
        ('MatchType', win32more.Security.Credentials.READER_SEL_REQUEST_MATCH_TYPE),
        ('Anonymous', READER_SEL_REQUEST__Anonymous_e__Union),
    ]
    return READER_SEL_REQUEST
READER_SEL_REQUEST_MATCH_TYPE = Int32
RSR_MATCH_TYPE_READER_AND_CONTAINER = 1
RSR_MATCH_TYPE_SERIAL_NUMBER = 2
RSR_MATCH_TYPE_ALL_CARDS = 3
def _define_READER_SEL_RESPONSE_head():
    class READER_SEL_RESPONSE(Structure):
        pass
    return READER_SEL_RESPONSE
def _define_READER_SEL_RESPONSE():
    READER_SEL_RESPONSE = win32more.Security.Credentials.READER_SEL_RESPONSE_head
    READER_SEL_RESPONSE._fields_ = [
        ('cbReaderNameOffset', UInt32),
        ('cchReaderNameLength', UInt32),
        ('cbCardNameOffset', UInt32),
        ('cchCardNameLength', UInt32),
    ]
    return READER_SEL_RESPONSE
def _define_SCARD_ATRMASK_head():
    class SCARD_ATRMASK(Structure):
        pass
    return SCARD_ATRMASK
def _define_SCARD_ATRMASK():
    SCARD_ATRMASK = win32more.Security.Credentials.SCARD_ATRMASK_head
    SCARD_ATRMASK._fields_ = [
        ('cbAtr', UInt32),
        ('rgbAtr', Byte * 36),
        ('rgbMask', Byte * 36),
    ]
    return SCARD_ATRMASK
def _define_SCARD_IO_REQUEST_head():
    class SCARD_IO_REQUEST(Structure):
        pass
    return SCARD_IO_REQUEST
def _define_SCARD_IO_REQUEST():
    SCARD_IO_REQUEST = win32more.Security.Credentials.SCARD_IO_REQUEST_head
    SCARD_IO_REQUEST._fields_ = [
        ('dwProtocol', UInt32),
        ('cbPciLength', UInt32),
    ]
    return SCARD_IO_REQUEST
def _define_SCARD_READERSTATEA_head():
    class SCARD_READERSTATEA(Structure):
        pass
    return SCARD_READERSTATEA
def _define_SCARD_READERSTATEA():
    SCARD_READERSTATEA = win32more.Security.Credentials.SCARD_READERSTATEA_head
    SCARD_READERSTATEA._fields_ = [
        ('szReader', win32more.Foundation.PSTR),
        ('pvUserData', c_void_p),
        ('dwCurrentState', win32more.Security.Credentials.SCARD_STATE),
        ('dwEventState', win32more.Security.Credentials.SCARD_STATE),
        ('cbAtr', UInt32),
        ('rgbAtr', Byte * 36),
    ]
    return SCARD_READERSTATEA
def _define_SCARD_READERSTATEW_head():
    class SCARD_READERSTATEW(Structure):
        pass
    return SCARD_READERSTATEW
def _define_SCARD_READERSTATEW():
    SCARD_READERSTATEW = win32more.Security.Credentials.SCARD_READERSTATEW_head
    SCARD_READERSTATEW._fields_ = [
        ('szReader', win32more.Foundation.PWSTR),
        ('pvUserData', c_void_p),
        ('dwCurrentState', win32more.Security.Credentials.SCARD_STATE),
        ('dwEventState', win32more.Security.Credentials.SCARD_STATE),
        ('cbAtr', UInt32),
        ('rgbAtr', Byte * 36),
    ]
    return SCARD_READERSTATEW
SCARD_SCOPE = UInt32
SCARD_SCOPE_USER = 0
SCARD_SCOPE_SYSTEM = 2
SCARD_STATE = UInt32
SCARD_STATE_UNAWARE = 0
SCARD_STATE_IGNORE = 1
SCARD_STATE_UNAVAILABLE = 8
SCARD_STATE_EMPTY = 16
SCARD_STATE_PRESENT = 32
SCARD_STATE_ATRMATCH = 64
SCARD_STATE_EXCLUSIVE = 128
SCARD_STATE_INUSE = 256
SCARD_STATE_MUTE = 512
SCARD_STATE_CHANGED = 2
SCARD_STATE_UNKNOWN = 4
def _define_SCARD_T0_COMMAND_head():
    class SCARD_T0_COMMAND(Structure):
        pass
    return SCARD_T0_COMMAND
def _define_SCARD_T0_COMMAND():
    SCARD_T0_COMMAND = win32more.Security.Credentials.SCARD_T0_COMMAND_head
    SCARD_T0_COMMAND._fields_ = [
        ('bCla', Byte),
        ('bIns', Byte),
        ('bP1', Byte),
        ('bP2', Byte),
        ('bP3', Byte),
    ]
    return SCARD_T0_COMMAND
def _define_SCARD_T0_REQUEST_head():
    class SCARD_T0_REQUEST(Structure):
        pass
    return SCARD_T0_REQUEST
def _define_SCARD_T0_REQUEST():
    SCARD_T0_REQUEST = win32more.Security.Credentials.SCARD_T0_REQUEST_head
    class SCARD_T0_REQUEST__Anonymous_e__Union(Union):
        pass
    SCARD_T0_REQUEST__Anonymous_e__Union._fields_ = [
        ('CmdBytes', win32more.Security.Credentials.SCARD_T0_COMMAND),
        ('rgbHeader', Byte * 5),
    ]
    SCARD_T0_REQUEST._anonymous_ = [
        'Anonymous',
    ]
    SCARD_T0_REQUEST._fields_ = [
        ('ioRequest', win32more.Security.Credentials.SCARD_IO_REQUEST),
        ('bSw1', Byte),
        ('bSw2', Byte),
        ('Anonymous', SCARD_T0_REQUEST__Anonymous_e__Union),
    ]
    return SCARD_T0_REQUEST
def _define_SCARD_T1_REQUEST_head():
    class SCARD_T1_REQUEST(Structure):
        pass
    return SCARD_T1_REQUEST
def _define_SCARD_T1_REQUEST():
    SCARD_T1_REQUEST = win32more.Security.Credentials.SCARD_T1_REQUEST_head
    SCARD_T1_REQUEST._fields_ = [
        ('ioRequest', win32more.Security.Credentials.SCARD_IO_REQUEST),
    ]
    return SCARD_T1_REQUEST
def _define_SecHandle_head():
    class SecHandle(Structure):
        pass
    return SecHandle
def _define_SecHandle():
    SecHandle = win32more.Security.Credentials.SecHandle_head
    SecHandle._fields_ = [
        ('dwLower', UIntPtr),
        ('dwUpper', UIntPtr),
    ]
    return SecHandle
def _define_SecPkgContext_ClientCreds_head():
    class SecPkgContext_ClientCreds(Structure):
        pass
    return SecPkgContext_ClientCreds
def _define_SecPkgContext_ClientCreds():
    SecPkgContext_ClientCreds = win32more.Security.Credentials.SecPkgContext_ClientCreds_head
    SecPkgContext_ClientCreds._fields_ = [
        ('AuthBufferLen', UInt32),
        ('AuthBuffer', c_char_p_no),
    ]
    return SecPkgContext_ClientCreds
def _define_USERNAME_TARGET_CREDENTIAL_INFO_head():
    class USERNAME_TARGET_CREDENTIAL_INFO(Structure):
        pass
    return USERNAME_TARGET_CREDENTIAL_INFO
def _define_USERNAME_TARGET_CREDENTIAL_INFO():
    USERNAME_TARGET_CREDENTIAL_INFO = win32more.Security.Credentials.USERNAME_TARGET_CREDENTIAL_INFO_head
    USERNAME_TARGET_CREDENTIAL_INFO._fields_ = [
        ('UserName', win32more.Foundation.PWSTR),
    ]
    return USERNAME_TARGET_CREDENTIAL_INFO
__all__ = [
    "BINARY_BLOB_CREDENTIAL_INFO",
    "CERT_CREDENTIAL_INFO",
    "CERT_HASH_LENGTH",
    "CREDENTIALA",
    "CREDENTIALW",
    "CREDENTIAL_ATTRIBUTEA",
    "CREDENTIAL_ATTRIBUTEW",
    "CREDENTIAL_TARGET_INFORMATIONA",
    "CREDENTIAL_TARGET_INFORMATIONW",
    "CREDSPP_SUBMIT_TYPE",
    "CREDSPP_SUBMIT_TYPE_CredsspCertificateCreds",
    "CREDSPP_SUBMIT_TYPE_CredsspCredEx",
    "CREDSPP_SUBMIT_TYPE_CredsspPasswordCreds",
    "CREDSPP_SUBMIT_TYPE_CredsspSchannelCreds",
    "CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBoth",
    "CREDSPP_SUBMIT_TYPE_CredsspSubmitBufferBothOld",
    "CREDSSP_CRED",
    "CREDSSP_CRED_EX",
    "CREDSSP_CRED_EX_VERSION",
    "CREDSSP_FLAG_REDIRECT",
    "CREDSSP_NAME",
    "CREDSSP_SERVER_AUTH_CERTIFICATE",
    "CREDSSP_SERVER_AUTH_LOOPBACK",
    "CREDSSP_SERVER_AUTH_NEGOTIATE",
    "CREDUIWIN_AUTHPACKAGE_ONLY",
    "CREDUIWIN_CHECKBOX",
    "CREDUIWIN_DOWNLEVEL_HELLO_AS_SMART_CARD",
    "CREDUIWIN_ENUMERATE_ADMINS",
    "CREDUIWIN_ENUMERATE_CURRENT_USER",
    "CREDUIWIN_FLAGS",
    "CREDUIWIN_GENERIC",
    "CREDUIWIN_IGNORE_CLOUDAUTHORITY_NAME",
    "CREDUIWIN_IN_CRED_ONLY",
    "CREDUIWIN_PACK_32_WOW",
    "CREDUIWIN_PREPROMPTING",
    "CREDUIWIN_SECURE_PROMPT",
    "CREDUI_FLAGS",
    "CREDUI_FLAGS_ALWAYS_SHOW_UI",
    "CREDUI_FLAGS_COMPLETE_USERNAME",
    "CREDUI_FLAGS_DO_NOT_PERSIST",
    "CREDUI_FLAGS_EXCLUDE_CERTIFICATES",
    "CREDUI_FLAGS_EXPECT_CONFIRMATION",
    "CREDUI_FLAGS_GENERIC_CREDENTIALS",
    "CREDUI_FLAGS_INCORRECT_PASSWORD",
    "CREDUI_FLAGS_KEEP_USERNAME",
    "CREDUI_FLAGS_PASSWORD_ONLY_OK",
    "CREDUI_FLAGS_PERSIST",
    "CREDUI_FLAGS_REQUEST_ADMINISTRATOR",
    "CREDUI_FLAGS_REQUIRE_CERTIFICATE",
    "CREDUI_FLAGS_REQUIRE_SMARTCARD",
    "CREDUI_FLAGS_SERVER_CREDENTIAL",
    "CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX",
    "CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS",
    "CREDUI_FLAGS_VALIDATE_USERNAME",
    "CREDUI_INFOA",
    "CREDUI_INFOW",
    "CREDUI_MAX_CAPTION_LENGTH",
    "CREDUI_MAX_DOMAIN_TARGET_LENGTH",
    "CREDUI_MAX_GENERIC_TARGET_LENGTH",
    "CREDUI_MAX_MESSAGE_LENGTH",
    "CREDUI_MAX_USERNAME_LENGTH",
    "CRED_ALLOW_NAME_RESOLUTION",
    "CRED_CACHE_TARGET_INFORMATION",
    "CRED_ENUMERATE_ALL_CREDENTIALS",
    "CRED_ENUMERATE_FLAGS",
    "CRED_FLAGS",
    "CRED_FLAGS_NGC_CERT",
    "CRED_FLAGS_OWF_CRED_BLOB",
    "CRED_FLAGS_PASSWORD_FOR_CERT",
    "CRED_FLAGS_PROMPT_NOW",
    "CRED_FLAGS_REQUIRE_CONFIRMATION",
    "CRED_FLAGS_USERNAME_TARGET",
    "CRED_FLAGS_VALID_FLAGS",
    "CRED_FLAGS_VALID_INPUT_FLAGS",
    "CRED_FLAGS_VSM_PROTECTED",
    "CRED_FLAGS_WILDCARD_MATCH",
    "CRED_LOGON_TYPES_MASK",
    "CRED_MARSHAL_TYPE",
    "CRED_MARSHAL_TYPE_BinaryBlobCredential",
    "CRED_MARSHAL_TYPE_BinaryBlobForSystem",
    "CRED_MARSHAL_TYPE_CertCredential",
    "CRED_MARSHAL_TYPE_UsernameForPackedCredentials",
    "CRED_MARSHAL_TYPE_UsernameTargetCredential",
    "CRED_MAX_ATTRIBUTES",
    "CRED_MAX_CREDENTIAL_BLOB_SIZE",
    "CRED_MAX_DOMAIN_TARGET_NAME_LENGTH",
    "CRED_MAX_GENERIC_TARGET_NAME_LENGTH",
    "CRED_MAX_STRING_LENGTH",
    "CRED_MAX_TARGETNAME_ATTRIBUTE_LENGTH",
    "CRED_MAX_TARGETNAME_NAMESPACE_LENGTH",
    "CRED_MAX_USERNAME_LENGTH",
    "CRED_MAX_VALUE_SIZE",
    "CRED_PACK_FLAGS",
    "CRED_PACK_GENERIC_CREDENTIALS",
    "CRED_PACK_ID_PROVIDER_CREDENTIALS",
    "CRED_PACK_PROTECTED_CREDENTIALS",
    "CRED_PACK_WOW_BUFFER",
    "CRED_PERSIST",
    "CRED_PERSIST_ENTERPRISE",
    "CRED_PERSIST_LOCAL_MACHINE",
    "CRED_PERSIST_NONE",
    "CRED_PERSIST_SESSION",
    "CRED_PRESERVE_CREDENTIAL_BLOB",
    "CRED_PROTECTION_TYPE",
    "CRED_PROTECTION_TYPE_CredForSystemProtection",
    "CRED_PROTECTION_TYPE_CredTrustedProtection",
    "CRED_PROTECTION_TYPE_CredUnprotected",
    "CRED_PROTECTION_TYPE_CredUserProtection",
    "CRED_PROTECT_AS_SELF",
    "CRED_PROTECT_TO_SYSTEM",
    "CRED_SESSION_WILDCARD_NAME",
    "CRED_SESSION_WILDCARD_NAME_A",
    "CRED_SESSION_WILDCARD_NAME_W",
    "CRED_TARGETNAME_ATTRIBUTE_BATCH",
    "CRED_TARGETNAME_ATTRIBUTE_BATCH_A",
    "CRED_TARGETNAME_ATTRIBUTE_BATCH_W",
    "CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE",
    "CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_A",
    "CRED_TARGETNAME_ATTRIBUTE_CACHEDINTERACTIVE_W",
    "CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE",
    "CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_A",
    "CRED_TARGETNAME_ATTRIBUTE_INTERACTIVE_W",
    "CRED_TARGETNAME_ATTRIBUTE_NAME",
    "CRED_TARGETNAME_ATTRIBUTE_NAME_A",
    "CRED_TARGETNAME_ATTRIBUTE_NAME_W",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORK",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_A",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORKCLEARTEXT_W",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORK_A",
    "CRED_TARGETNAME_ATTRIBUTE_NETWORK_W",
    "CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE",
    "CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_A",
    "CRED_TARGETNAME_ATTRIBUTE_REMOTEINTERACTIVE_W",
    "CRED_TARGETNAME_ATTRIBUTE_SERVICE",
    "CRED_TARGETNAME_ATTRIBUTE_SERVICE_A",
    "CRED_TARGETNAME_ATTRIBUTE_SERVICE_W",
    "CRED_TARGETNAME_ATTRIBUTE_TARGET",
    "CRED_TARGETNAME_ATTRIBUTE_TARGET_A",
    "CRED_TARGETNAME_ATTRIBUTE_TARGET_W",
    "CRED_TARGETNAME_DOMAIN_NAMESPACE",
    "CRED_TARGETNAME_DOMAIN_NAMESPACE_A",
    "CRED_TARGETNAME_DOMAIN_NAMESPACE_W",
    "CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_A",
    "CRED_TARGETNAME_LEGACYGENERIC_NAMESPACE_W",
    "CRED_TI_CREATE_EXPLICIT_CRED",
    "CRED_TI_DNSTREE_IS_DFS_SERVER",
    "CRED_TI_DOMAIN_FORMAT_UNKNOWN",
    "CRED_TI_ONLY_PASSWORD_REQUIRED",
    "CRED_TI_SERVER_FORMAT_UNKNOWN",
    "CRED_TI_USERNAME_TARGET",
    "CRED_TI_VALID_FLAGS",
    "CRED_TI_WORKGROUP_MEMBER",
    "CRED_TYPE",
    "CRED_TYPE_DOMAIN_CERTIFICATE",
    "CRED_TYPE_DOMAIN_EXTENDED",
    "CRED_TYPE_DOMAIN_PASSWORD",
    "CRED_TYPE_DOMAIN_VISIBLE_PASSWORD",
    "CRED_TYPE_GENERIC",
    "CRED_TYPE_GENERIC_CERTIFICATE",
    "CRED_TYPE_MAXIMUM",
    "CRED_TYPE_MAXIMUM_EX",
    "CRED_UNPROTECT_ALLOW_TO_SYSTEM",
    "CRED_UNPROTECT_AS_SELF",
    "CredDeleteA",
    "CredDeleteW",
    "CredEnumerateA",
    "CredEnumerateW",
    "CredFindBestCredentialA",
    "CredFindBestCredentialW",
    "CredFree",
    "CredGetSessionTypes",
    "CredGetTargetInfoA",
    "CredGetTargetInfoW",
    "CredIsMarshaledCredentialA",
    "CredIsMarshaledCredentialW",
    "CredIsProtectedA",
    "CredIsProtectedW",
    "CredMarshalCredentialA",
    "CredMarshalCredentialW",
    "CredPackAuthenticationBufferA",
    "CredPackAuthenticationBufferW",
    "CredProtectA",
    "CredProtectW",
    "CredReadA",
    "CredReadDomainCredentialsA",
    "CredReadDomainCredentialsW",
    "CredReadW",
    "CredRenameA",
    "CredRenameW",
    "CredUICmdLinePromptForCredentialsA",
    "CredUICmdLinePromptForCredentialsW",
    "CredUIConfirmCredentialsA",
    "CredUIConfirmCredentialsW",
    "CredUIParseUserNameA",
    "CredUIParseUserNameW",
    "CredUIPromptForCredentialsA",
    "CredUIPromptForCredentialsW",
    "CredUIPromptForWindowsCredentialsA",
    "CredUIPromptForWindowsCredentialsW",
    "CredUIReadSSOCredW",
    "CredUIStoreSSOCredW",
    "CredUnPackAuthenticationBufferA",
    "CredUnPackAuthenticationBufferW",
    "CredUnmarshalCredentialA",
    "CredUnmarshalCredentialW",
    "CredUnprotectA",
    "CredUnprotectW",
    "CredWriteA",
    "CredWriteDomainCredentialsA",
    "CredWriteDomainCredentialsW",
    "CredWriteW",
    "FILE_DEVICE_SMARTCARD",
    "GUID_DEVINTERFACE_SMARTCARD_READER",
    "GetOpenCardNameA",
    "GetOpenCardNameW",
    "KeyCredentialManagerFreeInformation",
    "KeyCredentialManagerGetInformation",
    "KeyCredentialManagerGetOperationErrorStates",
    "KeyCredentialManagerInfo",
    "KeyCredentialManagerOperationErrorStates",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateCertificateFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateDeviceJoinFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateHardwareFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateNone",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePinExistsFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStatePolicyFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateRemoteSessionFailure",
    "KeyCredentialManagerOperationErrorStates_KeyCredentialManagerOperationErrorStateTokenFailure",
    "KeyCredentialManagerOperationType",
    "KeyCredentialManagerOperationType_KeyCredentialManagerPinChange",
    "KeyCredentialManagerOperationType_KeyCredentialManagerPinReset",
    "KeyCredentialManagerOperationType_KeyCredentialManagerProvisioning",
    "KeyCredentialManagerShowUIOperation",
    "LPOCNCHKPROC",
    "LPOCNCONNPROCA",
    "LPOCNCONNPROCW",
    "LPOCNDSCPROC",
    "MAXIMUM_ATTR_STRING_LENGTH",
    "MAXIMUM_SMARTCARD_READERS",
    "OPENCARDNAMEA",
    "OPENCARDNAMEW",
    "OPENCARDNAME_EXA",
    "OPENCARDNAME_EXW",
    "OPENCARD_SEARCH_CRITERIAA",
    "OPENCARD_SEARCH_CRITERIAW",
    "READER_SEL_REQUEST",
    "READER_SEL_REQUEST_MATCH_TYPE",
    "READER_SEL_RESPONSE",
    "RSR_MATCH_TYPE_ALL_CARDS",
    "RSR_MATCH_TYPE_READER_AND_CONTAINER",
    "RSR_MATCH_TYPE_SERIAL_NUMBER",
    "SCARD_ABSENT",
    "SCARD_ALL_READERS",
    "SCARD_ATRMASK",
    "SCARD_ATR_LENGTH",
    "SCARD_AUDIT_CHV_FAILURE",
    "SCARD_AUDIT_CHV_SUCCESS",
    "SCARD_CLASS_COMMUNICATIONS",
    "SCARD_CLASS_ICC_STATE",
    "SCARD_CLASS_IFD_PROTOCOL",
    "SCARD_CLASS_MECHANICAL",
    "SCARD_CLASS_PERF",
    "SCARD_CLASS_POWER_MGMT",
    "SCARD_CLASS_PROTOCOL",
    "SCARD_CLASS_SECURITY",
    "SCARD_CLASS_SYSTEM",
    "SCARD_CLASS_VENDOR_DEFINED",
    "SCARD_CLASS_VENDOR_INFO",
    "SCARD_COLD_RESET",
    "SCARD_DEFAULT_READERS",
    "SCARD_EJECT_CARD",
    "SCARD_IO_REQUEST",
    "SCARD_LEAVE_CARD",
    "SCARD_LOCAL_READERS",
    "SCARD_NEGOTIABLE",
    "SCARD_POWERED",
    "SCARD_POWER_DOWN",
    "SCARD_PRESENT",
    "SCARD_PROTOCOL_DEFAULT",
    "SCARD_PROTOCOL_OPTIMAL",
    "SCARD_PROTOCOL_RAW",
    "SCARD_PROTOCOL_T0",
    "SCARD_PROTOCOL_T1",
    "SCARD_PROTOCOL_UNDEFINED",
    "SCARD_PROVIDER_CSP",
    "SCARD_PROVIDER_KSP",
    "SCARD_PROVIDER_PRIMARY",
    "SCARD_READERSTATEA",
    "SCARD_READERSTATEW",
    "SCARD_READER_CONFISCATES",
    "SCARD_READER_CONTACTLESS",
    "SCARD_READER_EJECTS",
    "SCARD_READER_SWALLOWS",
    "SCARD_READER_TYPE_EMBEDDEDSE",
    "SCARD_READER_TYPE_IDE",
    "SCARD_READER_TYPE_KEYBOARD",
    "SCARD_READER_TYPE_NFC",
    "SCARD_READER_TYPE_NGC",
    "SCARD_READER_TYPE_PARALELL",
    "SCARD_READER_TYPE_PCMCIA",
    "SCARD_READER_TYPE_SCSI",
    "SCARD_READER_TYPE_SERIAL",
    "SCARD_READER_TYPE_TPM",
    "SCARD_READER_TYPE_UICC",
    "SCARD_READER_TYPE_USB",
    "SCARD_READER_TYPE_VENDOR",
    "SCARD_RESET_CARD",
    "SCARD_SCOPE",
    "SCARD_SCOPE_SYSTEM",
    "SCARD_SCOPE_TERMINAL",
    "SCARD_SCOPE_USER",
    "SCARD_SHARE_DIRECT",
    "SCARD_SHARE_EXCLUSIVE",
    "SCARD_SHARE_SHARED",
    "SCARD_SPECIFIC",
    "SCARD_STATE",
    "SCARD_STATE_ATRMATCH",
    "SCARD_STATE_CHANGED",
    "SCARD_STATE_EMPTY",
    "SCARD_STATE_EXCLUSIVE",
    "SCARD_STATE_IGNORE",
    "SCARD_STATE_INUSE",
    "SCARD_STATE_MUTE",
    "SCARD_STATE_PRESENT",
    "SCARD_STATE_UNAVAILABLE",
    "SCARD_STATE_UNAWARE",
    "SCARD_STATE_UNKNOWN",
    "SCARD_STATE_UNPOWERED",
    "SCARD_SWALLOWED",
    "SCARD_SYSTEM_READERS",
    "SCARD_T0_CMD_LENGTH",
    "SCARD_T0_COMMAND",
    "SCARD_T0_HEADER_LENGTH",
    "SCARD_T0_REQUEST",
    "SCARD_T1_EPILOGUE_LENGTH",
    "SCARD_T1_EPILOGUE_LENGTH_LRC",
    "SCARD_T1_MAX_IFS",
    "SCARD_T1_PROLOGUE_LENGTH",
    "SCARD_T1_REQUEST",
    "SCARD_UNKNOWN",
    "SCARD_UNPOWER_CARD",
    "SCARD_WARM_RESET",
    "SCERR_NOCARDNAME",
    "SCERR_NOGUIDS",
    "SC_DLG_FORCE_UI",
    "SC_DLG_MINIMAL_UI",
    "SC_DLG_NO_UI",
    "SCardAccessStartedEvent",
    "SCardAddReaderToGroupA",
    "SCardAddReaderToGroupW",
    "SCardAudit",
    "SCardBeginTransaction",
    "SCardCancel",
    "SCardConnectA",
    "SCardConnectW",
    "SCardControl",
    "SCardDisconnect",
    "SCardDlgExtendedError",
    "SCardEndTransaction",
    "SCardEstablishContext",
    "SCardForgetCardTypeA",
    "SCardForgetCardTypeW",
    "SCardForgetReaderA",
    "SCardForgetReaderGroupA",
    "SCardForgetReaderGroupW",
    "SCardForgetReaderW",
    "SCardFreeMemory",
    "SCardGetAttrib",
    "SCardGetCardTypeProviderNameA",
    "SCardGetCardTypeProviderNameW",
    "SCardGetDeviceTypeIdA",
    "SCardGetDeviceTypeIdW",
    "SCardGetProviderIdA",
    "SCardGetProviderIdW",
    "SCardGetReaderDeviceInstanceIdA",
    "SCardGetReaderDeviceInstanceIdW",
    "SCardGetReaderIconA",
    "SCardGetReaderIconW",
    "SCardGetStatusChangeA",
    "SCardGetStatusChangeW",
    "SCardGetTransmitCount",
    "SCardIntroduceCardTypeA",
    "SCardIntroduceCardTypeW",
    "SCardIntroduceReaderA",
    "SCardIntroduceReaderGroupA",
    "SCardIntroduceReaderGroupW",
    "SCardIntroduceReaderW",
    "SCardIsValidContext",
    "SCardListCardsA",
    "SCardListCardsW",
    "SCardListInterfacesA",
    "SCardListInterfacesW",
    "SCardListReaderGroupsA",
    "SCardListReaderGroupsW",
    "SCardListReadersA",
    "SCardListReadersW",
    "SCardListReadersWithDeviceInstanceIdA",
    "SCardListReadersWithDeviceInstanceIdW",
    "SCardLocateCardsA",
    "SCardLocateCardsByATRA",
    "SCardLocateCardsByATRW",
    "SCardLocateCardsW",
    "SCardReadCacheA",
    "SCardReadCacheW",
    "SCardReconnect",
    "SCardReleaseContext",
    "SCardReleaseStartedEvent",
    "SCardRemoveReaderFromGroupA",
    "SCardRemoveReaderFromGroupW",
    "SCardSetAttrib",
    "SCardSetCardTypeProviderNameA",
    "SCardSetCardTypeProviderNameW",
    "SCardState",
    "SCardStatusA",
    "SCardStatusW",
    "SCardTransmit",
    "SCardUIDlgSelectCardA",
    "SCardUIDlgSelectCardW",
    "SCardWriteCacheA",
    "SCardWriteCacheW",
    "SECPKG_ALT_ATTR",
    "SECPKG_ATTR_C_FULL_IDENT_TOKEN",
    "STATUS_ACCOUNT_DISABLED",
    "STATUS_ACCOUNT_EXPIRED",
    "STATUS_ACCOUNT_LOCKED_OUT",
    "STATUS_ACCOUNT_RESTRICTION",
    "STATUS_AUTHENTICATION_FIREWALL_FAILED",
    "STATUS_DOWNGRADE_DETECTED",
    "STATUS_LOGON_FAILURE",
    "STATUS_LOGON_TYPE_NOT_GRANTED",
    "STATUS_NO_SUCH_LOGON_SESSION",
    "STATUS_NO_SUCH_USER",
    "STATUS_PASSWORD_EXPIRED",
    "STATUS_PASSWORD_MUST_CHANGE",
    "STATUS_WRONG_PASSWORD",
    "SecHandle",
    "SecPkgContext_ClientCreds",
    "TS_SSP_NAME",
    "TS_SSP_NAME_A",
    "USERNAME_TARGET_CREDENTIAL_INFO",
    "szOID_TS_KP_TS_SERVER_AUTH",
]
