from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
CVT_SECONDS = 1
TOKEN_PRIVILEGES_ATTRIBUTES = UInt32
SE_PRIVILEGE_ENABLED = 2
SE_PRIVILEGE_ENABLED_BY_DEFAULT = 1
SE_PRIVILEGE_REMOVED = 4
SE_PRIVILEGE_USED_FOR_ACCESS = 2147483648
LOGON32_PROVIDER = UInt32
LOGON32_PROVIDER_DEFAULT = 0
LOGON32_PROVIDER_WINNT50 = 3
LOGON32_PROVIDER_WINNT40 = 2
CREATE_RESTRICTED_TOKEN_FLAGS = UInt32
DISABLE_MAX_PRIVILEGE = 1
SANDBOX_INERT = 2
LUA_TOKEN = 4
WRITE_RESTRICTED = 8
LOGON32_LOGON = UInt32
LOGON32_LOGON_BATCH = 4
LOGON32_LOGON_INTERACTIVE = 2
LOGON32_LOGON_NETWORK = 3
LOGON32_LOGON_NETWORK_CLEARTEXT = 8
LOGON32_LOGON_NEW_CREDENTIALS = 9
LOGON32_LOGON_SERVICE = 5
LOGON32_LOGON_UNLOCK = 7
ACE_FLAGS = UInt32
CONTAINER_INHERIT_ACE = 2
FAILED_ACCESS_ACE_FLAG = 128
INHERIT_ONLY_ACE = 8
INHERITED_ACE = 16
NO_PROPAGATE_INHERIT_ACE = 4
OBJECT_INHERIT_ACE = 1
SUCCESSFUL_ACCESS_ACE_FLAG = 64
SUB_CONTAINERS_AND_OBJECTS_INHERIT = 3
SUB_CONTAINERS_ONLY_INHERIT = 2
SUB_OBJECTS_ONLY_INHERIT = 1
INHERIT_NO_PROPAGATE = 4
INHERIT_ONLY = 8
NO_INHERITANCE = 0
INHERIT_ONLY_ACE_ = 8
OBJECT_SECURITY_INFORMATION = UInt32
ATTRIBUTE_SECURITY_INFORMATION = 32
BACKUP_SECURITY_INFORMATION = 65536
DACL_SECURITY_INFORMATION = 4
GROUP_SECURITY_INFORMATION = 2
LABEL_SECURITY_INFORMATION = 16
OWNER_SECURITY_INFORMATION = 1
PROTECTED_DACL_SECURITY_INFORMATION = 2147483648
PROTECTED_SACL_SECURITY_INFORMATION = 1073741824
SACL_SECURITY_INFORMATION = 8
SCOPE_SECURITY_INFORMATION = 64
UNPROTECTED_DACL_SECURITY_INFORMATION = 536870912
UNPROTECTED_SACL_SECURITY_INFORMATION = 268435456
SECURITY_AUTO_INHERIT_FLAGS = UInt32
SEF_AVOID_OWNER_CHECK = 16
SEF_AVOID_OWNER_RESTRICTION = 4096
SEF_AVOID_PRIVILEGE_CHECK = 8
SEF_DACL_AUTO_INHERIT = 1
SEF_DEFAULT_DESCRIPTOR_FOR_OBJECT = 4
SEF_DEFAULT_GROUP_FROM_PARENT = 64
SEF_DEFAULT_OWNER_FROM_PARENT = 32
SEF_MACL_NO_EXECUTE_UP = 1024
SEF_MACL_NO_READ_UP = 512
SEF_MACL_NO_WRITE_UP = 256
SEF_SACL_AUTO_INHERIT = 2
ACE_REVISION = UInt32
ACL_REVISION = 2
ACL_REVISION_DS = 4
TOKEN_MANDATORY_POLICY_ID = UInt32
TOKEN_MANDATORY_POLICY_OFF = 0
TOKEN_MANDATORY_POLICY_NO_WRITE_UP = 1
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN = 2
TOKEN_MANDATORY_POLICY_VALID_MASK = 3
SYSTEM_AUDIT_OBJECT_ACE_FLAGS = UInt32
ACE_OBJECT_TYPE_PRESENT = 1
ACE_INHERITED_OBJECT_TYPE_PRESENT = 2
CLAIM_SECURITY_ATTRIBUTE_FLAGS = UInt32
CLAIM_SECURITY_ATTRIBUTE_NON_INHERITABLE = 1
CLAIM_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE = 2
CLAIM_SECURITY_ATTRIBUTE_USE_FOR_DENY_ONLY = 4
CLAIM_SECURITY_ATTRIBUTE_DISABLED_BY_DEFAULT = 8
CLAIM_SECURITY_ATTRIBUTE_DISABLED = 16
CLAIM_SECURITY_ATTRIBUTE_MANDATORY = 32
CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = UInt16
CLAIM_SECURITY_ATTRIBUTE_TYPE_INT64 = 1
CLAIM_SECURITY_ATTRIBUTE_TYPE_UINT64 = 2
CLAIM_SECURITY_ATTRIBUTE_TYPE_STRING = 3
CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING = 16
CLAIM_SECURITY_ATTRIBUTE_TYPE_FQBN = 4
CLAIM_SECURITY_ATTRIBUTE_TYPE_SID = 5
CLAIM_SECURITY_ATTRIBUTE_TYPE_BOOLEAN = 6
def _define_PLSA_AP_CALL_PACKAGE_UNTRUSTED():
    return CFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(c_void_p),c_void_p,c_void_p,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(Int32), use_last_error=False)
def _define_SEC_THREAD_START():
    return CFUNCTYPE(UInt32,c_void_p, use_last_error=False)
TOKEN_ACCESS_MASK = UInt32
TOKEN_DELETE = 65536
TOKEN_READ_CONTROL = 131072
TOKEN_WRITE_DAC = 262144
TOKEN_WRITE_OWNER = 524288
TOKEN_ACCESS_SYSTEM_SECURITY = 16777216
TOKEN_ASSIGN_PRIMARY = 1
TOKEN_DUPLICATE = 2
TOKEN_IMPERSONATE = 4
TOKEN_QUERY = 8
TOKEN_QUERY_SOURCE = 16
TOKEN_ADJUST_PRIVILEGES = 32
TOKEN_ADJUST_GROUPS = 64
TOKEN_ADJUST_DEFAULT = 128
TOKEN_ADJUST_SESSIONID = 256
TOKEN_ALL_ACCESS = 983295
HDIAGNOSTIC_DATA_QUERY_SESSION = IntPtr
HDIAGNOSTIC_REPORT = IntPtr
HDIAGNOSTIC_EVENT_TAG_DESCRIPTION = IntPtr
HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION = IntPtr
HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION = IntPtr
HDIAGNOSTIC_RECORD = IntPtr
NCRYPT_DESCRIPTOR_HANDLE = IntPtr
NCRYPT_STREAM_HANDLE = IntPtr
SAFER_LEVEL_HANDLE = IntPtr
SC_HANDLE = IntPtr
def _define_SECURITY_ATTRIBUTES_head():
    class SECURITY_ATTRIBUTES(Structure):
        pass
    return SECURITY_ATTRIBUTES
def _define_SECURITY_ATTRIBUTES():
    SECURITY_ATTRIBUTES = win32more.Security.SECURITY_ATTRIBUTES_head
    SECURITY_ATTRIBUTES._fields_ = [
        ("nLength", UInt32),
        ("lpSecurityDescriptor", c_void_p),
        ("bInheritHandle", win32more.Foundation.BOOL),
    ]
    return SECURITY_ATTRIBUTES
ENUM_PERIOD = Int32
ENUM_PERIOD_INVALID = -1
ENUM_PERIOD_SECONDS = 0
ENUM_PERIOD_MINUTES = 1
ENUM_PERIOD_HOURS = 2
ENUM_PERIOD_DAYS = 3
ENUM_PERIOD_WEEKS = 4
ENUM_PERIOD_MONTHS = 5
ENUM_PERIOD_YEARS = 6
def _define_LLFILETIME_head():
    class LLFILETIME(Structure):
        pass
    return LLFILETIME
def _define_LLFILETIME():
    LLFILETIME = win32more.Security.LLFILETIME_head
    class LLFILETIME__Anonymous_e__Union(Union):
        pass
    LLFILETIME__Anonymous_e__Union._fields_ = [
        ("ll", Int64),
        ("ft", win32more.Foundation.FILETIME),
    ]
    LLFILETIME._anonymous_ = [
        'Anonymous',
    ]
    LLFILETIME._fields_ = [
        ("Anonymous", LLFILETIME__Anonymous_e__Union),
    ]
    return LLFILETIME
def _define_GENERIC_MAPPING_head():
    class GENERIC_MAPPING(Structure):
        pass
    return GENERIC_MAPPING
def _define_GENERIC_MAPPING():
    GENERIC_MAPPING = win32more.Security.GENERIC_MAPPING_head
    GENERIC_MAPPING._fields_ = [
        ("GenericRead", UInt32),
        ("GenericWrite", UInt32),
        ("GenericExecute", UInt32),
        ("GenericAll", UInt32),
    ]
    return GENERIC_MAPPING
def _define_LUID_AND_ATTRIBUTES_head():
    class LUID_AND_ATTRIBUTES(Structure):
        pass
    return LUID_AND_ATTRIBUTES
def _define_LUID_AND_ATTRIBUTES():
    LUID_AND_ATTRIBUTES = win32more.Security.LUID_AND_ATTRIBUTES_head
    LUID_AND_ATTRIBUTES._fields_ = [
        ("Luid", win32more.Foundation.LUID),
        ("Attributes", win32more.Security.TOKEN_PRIVILEGES_ATTRIBUTES),
    ]
    return LUID_AND_ATTRIBUTES
def _define_SID_IDENTIFIER_AUTHORITY_head():
    class SID_IDENTIFIER_AUTHORITY(Structure):
        pass
    return SID_IDENTIFIER_AUTHORITY
def _define_SID_IDENTIFIER_AUTHORITY():
    SID_IDENTIFIER_AUTHORITY = win32more.Security.SID_IDENTIFIER_AUTHORITY_head
    SID_IDENTIFIER_AUTHORITY._fields_ = [
        ("Value", Byte * 6),
    ]
    return SID_IDENTIFIER_AUTHORITY
def _define_SID_head():
    class SID(Structure):
        pass
    return SID
def _define_SID():
    SID = win32more.Security.SID_head
    SID._fields_ = [
        ("Revision", Byte),
        ("SubAuthorityCount", Byte),
        ("IdentifierAuthority", win32more.Security.SID_IDENTIFIER_AUTHORITY),
        ("SubAuthority", UInt32 * 0),
    ]
    return SID
def _define_SE_SID_head():
    class SE_SID(Union):
        pass
    return SE_SID
def _define_SE_SID():
    SE_SID = win32more.Security.SE_SID_head
    SE_SID._fields_ = [
        ("Sid", win32more.Security.SID),
        ("Buffer", Byte * 68),
    ]
    return SE_SID
SID_NAME_USE = Int32
SID_NAME_USE_SidTypeUser = 1
SID_NAME_USE_SidTypeGroup = 2
SID_NAME_USE_SidTypeDomain = 3
SID_NAME_USE_SidTypeAlias = 4
SID_NAME_USE_SidTypeWellKnownGroup = 5
SID_NAME_USE_SidTypeDeletedAccount = 6
SID_NAME_USE_SidTypeInvalid = 7
SID_NAME_USE_SidTypeUnknown = 8
SID_NAME_USE_SidTypeComputer = 9
SID_NAME_USE_SidTypeLabel = 10
SID_NAME_USE_SidTypeLogonSession = 11
def _define_SID_AND_ATTRIBUTES_head():
    class SID_AND_ATTRIBUTES(Structure):
        pass
    return SID_AND_ATTRIBUTES
def _define_SID_AND_ATTRIBUTES():
    SID_AND_ATTRIBUTES = win32more.Security.SID_AND_ATTRIBUTES_head
    SID_AND_ATTRIBUTES._fields_ = [
        ("Sid", win32more.Foundation.PSID),
        ("Attributes", UInt32),
    ]
    return SID_AND_ATTRIBUTES
def _define_SID_AND_ATTRIBUTES_HASH_head():
    class SID_AND_ATTRIBUTES_HASH(Structure):
        pass
    return SID_AND_ATTRIBUTES_HASH
def _define_SID_AND_ATTRIBUTES_HASH():
    SID_AND_ATTRIBUTES_HASH = win32more.Security.SID_AND_ATTRIBUTES_HASH_head
    SID_AND_ATTRIBUTES_HASH._fields_ = [
        ("SidCount", UInt32),
        ("SidAttr", POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
        ("Hash", UIntPtr * 32),
    ]
    return SID_AND_ATTRIBUTES_HASH
WELL_KNOWN_SID_TYPE = Int32
WELL_KNOWN_SID_TYPE_WinNullSid = 0
WELL_KNOWN_SID_TYPE_WinWorldSid = 1
WELL_KNOWN_SID_TYPE_WinLocalSid = 2
WELL_KNOWN_SID_TYPE_WinCreatorOwnerSid = 3
WELL_KNOWN_SID_TYPE_WinCreatorGroupSid = 4
WELL_KNOWN_SID_TYPE_WinCreatorOwnerServerSid = 5
WELL_KNOWN_SID_TYPE_WinCreatorGroupServerSid = 6
WELL_KNOWN_SID_TYPE_WinNtAuthoritySid = 7
WELL_KNOWN_SID_TYPE_WinDialupSid = 8
WELL_KNOWN_SID_TYPE_WinNetworkSid = 9
WELL_KNOWN_SID_TYPE_WinBatchSid = 10
WELL_KNOWN_SID_TYPE_WinInteractiveSid = 11
WELL_KNOWN_SID_TYPE_WinServiceSid = 12
WELL_KNOWN_SID_TYPE_WinAnonymousSid = 13
WELL_KNOWN_SID_TYPE_WinProxySid = 14
WELL_KNOWN_SID_TYPE_WinEnterpriseControllersSid = 15
WELL_KNOWN_SID_TYPE_WinSelfSid = 16
WELL_KNOWN_SID_TYPE_WinAuthenticatedUserSid = 17
WELL_KNOWN_SID_TYPE_WinRestrictedCodeSid = 18
WELL_KNOWN_SID_TYPE_WinTerminalServerSid = 19
WELL_KNOWN_SID_TYPE_WinRemoteLogonIdSid = 20
WELL_KNOWN_SID_TYPE_WinLogonIdsSid = 21
WELL_KNOWN_SID_TYPE_WinLocalSystemSid = 22
WELL_KNOWN_SID_TYPE_WinLocalServiceSid = 23
WELL_KNOWN_SID_TYPE_WinNetworkServiceSid = 24
WELL_KNOWN_SID_TYPE_WinBuiltinDomainSid = 25
WELL_KNOWN_SID_TYPE_WinBuiltinAdministratorsSid = 26
WELL_KNOWN_SID_TYPE_WinBuiltinUsersSid = 27
WELL_KNOWN_SID_TYPE_WinBuiltinGuestsSid = 28
WELL_KNOWN_SID_TYPE_WinBuiltinPowerUsersSid = 29
WELL_KNOWN_SID_TYPE_WinBuiltinAccountOperatorsSid = 30
WELL_KNOWN_SID_TYPE_WinBuiltinSystemOperatorsSid = 31
WELL_KNOWN_SID_TYPE_WinBuiltinPrintOperatorsSid = 32
WELL_KNOWN_SID_TYPE_WinBuiltinBackupOperatorsSid = 33
WELL_KNOWN_SID_TYPE_WinBuiltinReplicatorSid = 34
WELL_KNOWN_SID_TYPE_WinBuiltinPreWindows2000CompatibleAccessSid = 35
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteDesktopUsersSid = 36
WELL_KNOWN_SID_TYPE_WinBuiltinNetworkConfigurationOperatorsSid = 37
WELL_KNOWN_SID_TYPE_WinAccountAdministratorSid = 38
WELL_KNOWN_SID_TYPE_WinAccountGuestSid = 39
WELL_KNOWN_SID_TYPE_WinAccountKrbtgtSid = 40
WELL_KNOWN_SID_TYPE_WinAccountDomainAdminsSid = 41
WELL_KNOWN_SID_TYPE_WinAccountDomainUsersSid = 42
WELL_KNOWN_SID_TYPE_WinAccountDomainGuestsSid = 43
WELL_KNOWN_SID_TYPE_WinAccountComputersSid = 44
WELL_KNOWN_SID_TYPE_WinAccountControllersSid = 45
WELL_KNOWN_SID_TYPE_WinAccountCertAdminsSid = 46
WELL_KNOWN_SID_TYPE_WinAccountSchemaAdminsSid = 47
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseAdminsSid = 48
WELL_KNOWN_SID_TYPE_WinAccountPolicyAdminsSid = 49
WELL_KNOWN_SID_TYPE_WinAccountRasAndIasServersSid = 50
WELL_KNOWN_SID_TYPE_WinNTLMAuthenticationSid = 51
WELL_KNOWN_SID_TYPE_WinDigestAuthenticationSid = 52
WELL_KNOWN_SID_TYPE_WinSChannelAuthenticationSid = 53
WELL_KNOWN_SID_TYPE_WinThisOrganizationSid = 54
WELL_KNOWN_SID_TYPE_WinOtherOrganizationSid = 55
WELL_KNOWN_SID_TYPE_WinBuiltinIncomingForestTrustBuildersSid = 56
WELL_KNOWN_SID_TYPE_WinBuiltinPerfMonitoringUsersSid = 57
WELL_KNOWN_SID_TYPE_WinBuiltinPerfLoggingUsersSid = 58
WELL_KNOWN_SID_TYPE_WinBuiltinAuthorizationAccessSid = 59
WELL_KNOWN_SID_TYPE_WinBuiltinTerminalServerLicenseServersSid = 60
WELL_KNOWN_SID_TYPE_WinBuiltinDCOMUsersSid = 61
WELL_KNOWN_SID_TYPE_WinBuiltinIUsersSid = 62
WELL_KNOWN_SID_TYPE_WinIUserSid = 63
WELL_KNOWN_SID_TYPE_WinBuiltinCryptoOperatorsSid = 64
WELL_KNOWN_SID_TYPE_WinUntrustedLabelSid = 65
WELL_KNOWN_SID_TYPE_WinLowLabelSid = 66
WELL_KNOWN_SID_TYPE_WinMediumLabelSid = 67
WELL_KNOWN_SID_TYPE_WinHighLabelSid = 68
WELL_KNOWN_SID_TYPE_WinSystemLabelSid = 69
WELL_KNOWN_SID_TYPE_WinWriteRestrictedCodeSid = 70
WELL_KNOWN_SID_TYPE_WinCreatorOwnerRightsSid = 71
WELL_KNOWN_SID_TYPE_WinCacheablePrincipalsGroupSid = 72
WELL_KNOWN_SID_TYPE_WinNonCacheablePrincipalsGroupSid = 73
WELL_KNOWN_SID_TYPE_WinEnterpriseReadonlyControllersSid = 74
WELL_KNOWN_SID_TYPE_WinAccountReadonlyControllersSid = 75
WELL_KNOWN_SID_TYPE_WinBuiltinEventLogReadersGroup = 76
WELL_KNOWN_SID_TYPE_WinNewEnterpriseReadonlyControllersSid = 77
WELL_KNOWN_SID_TYPE_WinBuiltinCertSvcDComAccessGroup = 78
WELL_KNOWN_SID_TYPE_WinMediumPlusLabelSid = 79
WELL_KNOWN_SID_TYPE_WinLocalLogonSid = 80
WELL_KNOWN_SID_TYPE_WinConsoleLogonSid = 81
WELL_KNOWN_SID_TYPE_WinThisOrganizationCertificateSid = 82
WELL_KNOWN_SID_TYPE_WinApplicationPackageAuthoritySid = 83
WELL_KNOWN_SID_TYPE_WinBuiltinAnyPackageSid = 84
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientSid = 85
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientServerSid = 86
WELL_KNOWN_SID_TYPE_WinCapabilityPrivateNetworkClientServerSid = 87
WELL_KNOWN_SID_TYPE_WinCapabilityPicturesLibrarySid = 88
WELL_KNOWN_SID_TYPE_WinCapabilityVideosLibrarySid = 89
WELL_KNOWN_SID_TYPE_WinCapabilityMusicLibrarySid = 90
WELL_KNOWN_SID_TYPE_WinCapabilityDocumentsLibrarySid = 91
WELL_KNOWN_SID_TYPE_WinCapabilitySharedUserCertificatesSid = 92
WELL_KNOWN_SID_TYPE_WinCapabilityEnterpriseAuthenticationSid = 93
WELL_KNOWN_SID_TYPE_WinCapabilityRemovableStorageSid = 94
WELL_KNOWN_SID_TYPE_WinBuiltinRDSRemoteAccessServersSid = 95
WELL_KNOWN_SID_TYPE_WinBuiltinRDSEndpointServersSid = 96
WELL_KNOWN_SID_TYPE_WinBuiltinRDSManagementServersSid = 97
WELL_KNOWN_SID_TYPE_WinUserModeDriversSid = 98
WELL_KNOWN_SID_TYPE_WinBuiltinHyperVAdminsSid = 99
WELL_KNOWN_SID_TYPE_WinAccountCloneableControllersSid = 100
WELL_KNOWN_SID_TYPE_WinBuiltinAccessControlAssistanceOperatorsSid = 101
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteManagementUsersSid = 102
WELL_KNOWN_SID_TYPE_WinAuthenticationAuthorityAssertedSid = 103
WELL_KNOWN_SID_TYPE_WinAuthenticationServiceAssertedSid = 104
WELL_KNOWN_SID_TYPE_WinLocalAccountSid = 105
WELL_KNOWN_SID_TYPE_WinLocalAccountAndAdministratorSid = 106
WELL_KNOWN_SID_TYPE_WinAccountProtectedUsersSid = 107
WELL_KNOWN_SID_TYPE_WinCapabilityAppointmentsSid = 108
WELL_KNOWN_SID_TYPE_WinCapabilityContactsSid = 109
WELL_KNOWN_SID_TYPE_WinAccountDefaultSystemManagedSid = 110
WELL_KNOWN_SID_TYPE_WinBuiltinDefaultSystemManagedGroupSid = 111
WELL_KNOWN_SID_TYPE_WinBuiltinStorageReplicaAdminsSid = 112
WELL_KNOWN_SID_TYPE_WinAccountKeyAdminsSid = 113
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseKeyAdminsSid = 114
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyTrustSid = 115
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyMFASid = 116
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyAttestationSid = 117
WELL_KNOWN_SID_TYPE_WinAuthenticationFreshKeyAuthSid = 118
WELL_KNOWN_SID_TYPE_WinBuiltinDeviceOwnersSid = 119
def _define_ACL_head():
    class ACL(Structure):
        pass
    return ACL
def _define_ACL():
    ACL = win32more.Security.ACL_head
    ACL._fields_ = [
        ("AclRevision", Byte),
        ("Sbz1", Byte),
        ("AclSize", UInt16),
        ("AceCount", UInt16),
        ("Sbz2", UInt16),
    ]
    return ACL
def _define_ACE_HEADER_head():
    class ACE_HEADER(Structure):
        pass
    return ACE_HEADER
def _define_ACE_HEADER():
    ACE_HEADER = win32more.Security.ACE_HEADER_head
    ACE_HEADER._fields_ = [
        ("AceType", Byte),
        ("AceFlags", Byte),
        ("AceSize", UInt16),
    ]
    return ACE_HEADER
def _define_ACCESS_ALLOWED_ACE_head():
    class ACCESS_ALLOWED_ACE(Structure):
        pass
    return ACCESS_ALLOWED_ACE
def _define_ACCESS_ALLOWED_ACE():
    ACCESS_ALLOWED_ACE = win32more.Security.ACCESS_ALLOWED_ACE_head
    ACCESS_ALLOWED_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return ACCESS_ALLOWED_ACE
def _define_ACCESS_DENIED_ACE_head():
    class ACCESS_DENIED_ACE(Structure):
        pass
    return ACCESS_DENIED_ACE
def _define_ACCESS_DENIED_ACE():
    ACCESS_DENIED_ACE = win32more.Security.ACCESS_DENIED_ACE_head
    ACCESS_DENIED_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return ACCESS_DENIED_ACE
def _define_SYSTEM_AUDIT_ACE_head():
    class SYSTEM_AUDIT_ACE(Structure):
        pass
    return SYSTEM_AUDIT_ACE
def _define_SYSTEM_AUDIT_ACE():
    SYSTEM_AUDIT_ACE = win32more.Security.SYSTEM_AUDIT_ACE_head
    SYSTEM_AUDIT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_AUDIT_ACE
def _define_SYSTEM_ALARM_ACE_head():
    class SYSTEM_ALARM_ACE(Structure):
        pass
    return SYSTEM_ALARM_ACE
def _define_SYSTEM_ALARM_ACE():
    SYSTEM_ALARM_ACE = win32more.Security.SYSTEM_ALARM_ACE_head
    SYSTEM_ALARM_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_ALARM_ACE
def _define_SYSTEM_RESOURCE_ATTRIBUTE_ACE_head():
    class SYSTEM_RESOURCE_ATTRIBUTE_ACE(Structure):
        pass
    return SYSTEM_RESOURCE_ATTRIBUTE_ACE
def _define_SYSTEM_RESOURCE_ATTRIBUTE_ACE():
    SYSTEM_RESOURCE_ATTRIBUTE_ACE = win32more.Security.SYSTEM_RESOURCE_ATTRIBUTE_ACE_head
    SYSTEM_RESOURCE_ATTRIBUTE_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_RESOURCE_ATTRIBUTE_ACE
def _define_SYSTEM_SCOPED_POLICY_ID_ACE_head():
    class SYSTEM_SCOPED_POLICY_ID_ACE(Structure):
        pass
    return SYSTEM_SCOPED_POLICY_ID_ACE
def _define_SYSTEM_SCOPED_POLICY_ID_ACE():
    SYSTEM_SCOPED_POLICY_ID_ACE = win32more.Security.SYSTEM_SCOPED_POLICY_ID_ACE_head
    SYSTEM_SCOPED_POLICY_ID_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_SCOPED_POLICY_ID_ACE
def _define_SYSTEM_MANDATORY_LABEL_ACE_head():
    class SYSTEM_MANDATORY_LABEL_ACE(Structure):
        pass
    return SYSTEM_MANDATORY_LABEL_ACE
def _define_SYSTEM_MANDATORY_LABEL_ACE():
    SYSTEM_MANDATORY_LABEL_ACE = win32more.Security.SYSTEM_MANDATORY_LABEL_ACE_head
    SYSTEM_MANDATORY_LABEL_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_MANDATORY_LABEL_ACE
def _define_SYSTEM_PROCESS_TRUST_LABEL_ACE_head():
    class SYSTEM_PROCESS_TRUST_LABEL_ACE(Structure):
        pass
    return SYSTEM_PROCESS_TRUST_LABEL_ACE
def _define_SYSTEM_PROCESS_TRUST_LABEL_ACE():
    SYSTEM_PROCESS_TRUST_LABEL_ACE = win32more.Security.SYSTEM_PROCESS_TRUST_LABEL_ACE_head
    SYSTEM_PROCESS_TRUST_LABEL_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_PROCESS_TRUST_LABEL_ACE
def _define_SYSTEM_ACCESS_FILTER_ACE_head():
    class SYSTEM_ACCESS_FILTER_ACE(Structure):
        pass
    return SYSTEM_ACCESS_FILTER_ACE
def _define_SYSTEM_ACCESS_FILTER_ACE():
    SYSTEM_ACCESS_FILTER_ACE = win32more.Security.SYSTEM_ACCESS_FILTER_ACE_head
    SYSTEM_ACCESS_FILTER_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_ACCESS_FILTER_ACE
def _define_ACCESS_ALLOWED_OBJECT_ACE_head():
    class ACCESS_ALLOWED_OBJECT_ACE(Structure):
        pass
    return ACCESS_ALLOWED_OBJECT_ACE
def _define_ACCESS_ALLOWED_OBJECT_ACE():
    ACCESS_ALLOWED_OBJECT_ACE = win32more.Security.ACCESS_ALLOWED_OBJECT_ACE_head
    ACCESS_ALLOWED_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return ACCESS_ALLOWED_OBJECT_ACE
def _define_ACCESS_DENIED_OBJECT_ACE_head():
    class ACCESS_DENIED_OBJECT_ACE(Structure):
        pass
    return ACCESS_DENIED_OBJECT_ACE
def _define_ACCESS_DENIED_OBJECT_ACE():
    ACCESS_DENIED_OBJECT_ACE = win32more.Security.ACCESS_DENIED_OBJECT_ACE_head
    ACCESS_DENIED_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return ACCESS_DENIED_OBJECT_ACE
def _define_SYSTEM_AUDIT_OBJECT_ACE_head():
    class SYSTEM_AUDIT_OBJECT_ACE(Structure):
        pass
    return SYSTEM_AUDIT_OBJECT_ACE
def _define_SYSTEM_AUDIT_OBJECT_ACE():
    SYSTEM_AUDIT_OBJECT_ACE = win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_head
    SYSTEM_AUDIT_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return SYSTEM_AUDIT_OBJECT_ACE
def _define_SYSTEM_ALARM_OBJECT_ACE_head():
    class SYSTEM_ALARM_OBJECT_ACE(Structure):
        pass
    return SYSTEM_ALARM_OBJECT_ACE
def _define_SYSTEM_ALARM_OBJECT_ACE():
    SYSTEM_ALARM_OBJECT_ACE = win32more.Security.SYSTEM_ALARM_OBJECT_ACE_head
    SYSTEM_ALARM_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", UInt32),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return SYSTEM_ALARM_OBJECT_ACE
def _define_ACCESS_ALLOWED_CALLBACK_ACE_head():
    class ACCESS_ALLOWED_CALLBACK_ACE(Structure):
        pass
    return ACCESS_ALLOWED_CALLBACK_ACE
def _define_ACCESS_ALLOWED_CALLBACK_ACE():
    ACCESS_ALLOWED_CALLBACK_ACE = win32more.Security.ACCESS_ALLOWED_CALLBACK_ACE_head
    ACCESS_ALLOWED_CALLBACK_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return ACCESS_ALLOWED_CALLBACK_ACE
def _define_ACCESS_DENIED_CALLBACK_ACE_head():
    class ACCESS_DENIED_CALLBACK_ACE(Structure):
        pass
    return ACCESS_DENIED_CALLBACK_ACE
def _define_ACCESS_DENIED_CALLBACK_ACE():
    ACCESS_DENIED_CALLBACK_ACE = win32more.Security.ACCESS_DENIED_CALLBACK_ACE_head
    ACCESS_DENIED_CALLBACK_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return ACCESS_DENIED_CALLBACK_ACE
def _define_SYSTEM_AUDIT_CALLBACK_ACE_head():
    class SYSTEM_AUDIT_CALLBACK_ACE(Structure):
        pass
    return SYSTEM_AUDIT_CALLBACK_ACE
def _define_SYSTEM_AUDIT_CALLBACK_ACE():
    SYSTEM_AUDIT_CALLBACK_ACE = win32more.Security.SYSTEM_AUDIT_CALLBACK_ACE_head
    SYSTEM_AUDIT_CALLBACK_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_AUDIT_CALLBACK_ACE
def _define_SYSTEM_ALARM_CALLBACK_ACE_head():
    class SYSTEM_ALARM_CALLBACK_ACE(Structure):
        pass
    return SYSTEM_ALARM_CALLBACK_ACE
def _define_SYSTEM_ALARM_CALLBACK_ACE():
    SYSTEM_ALARM_CALLBACK_ACE = win32more.Security.SYSTEM_ALARM_CALLBACK_ACE_head
    SYSTEM_ALARM_CALLBACK_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("SidStart", UInt32),
    ]
    return SYSTEM_ALARM_CALLBACK_ACE
def _define_ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_head():
    class ACCESS_ALLOWED_CALLBACK_OBJECT_ACE(Structure):
        pass
    return ACCESS_ALLOWED_CALLBACK_OBJECT_ACE
def _define_ACCESS_ALLOWED_CALLBACK_OBJECT_ACE():
    ACCESS_ALLOWED_CALLBACK_OBJECT_ACE = win32more.Security.ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_head
    ACCESS_ALLOWED_CALLBACK_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return ACCESS_ALLOWED_CALLBACK_OBJECT_ACE
def _define_ACCESS_DENIED_CALLBACK_OBJECT_ACE_head():
    class ACCESS_DENIED_CALLBACK_OBJECT_ACE(Structure):
        pass
    return ACCESS_DENIED_CALLBACK_OBJECT_ACE
def _define_ACCESS_DENIED_CALLBACK_OBJECT_ACE():
    ACCESS_DENIED_CALLBACK_OBJECT_ACE = win32more.Security.ACCESS_DENIED_CALLBACK_OBJECT_ACE_head
    ACCESS_DENIED_CALLBACK_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return ACCESS_DENIED_CALLBACK_OBJECT_ACE
def _define_SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_head():
    class SYSTEM_AUDIT_CALLBACK_OBJECT_ACE(Structure):
        pass
    return SYSTEM_AUDIT_CALLBACK_OBJECT_ACE
def _define_SYSTEM_AUDIT_CALLBACK_OBJECT_ACE():
    SYSTEM_AUDIT_CALLBACK_OBJECT_ACE = win32more.Security.SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_head
    SYSTEM_AUDIT_CALLBACK_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return SYSTEM_AUDIT_CALLBACK_OBJECT_ACE
def _define_SYSTEM_ALARM_CALLBACK_OBJECT_ACE_head():
    class SYSTEM_ALARM_CALLBACK_OBJECT_ACE(Structure):
        pass
    return SYSTEM_ALARM_CALLBACK_OBJECT_ACE
def _define_SYSTEM_ALARM_CALLBACK_OBJECT_ACE():
    SYSTEM_ALARM_CALLBACK_OBJECT_ACE = win32more.Security.SYSTEM_ALARM_CALLBACK_OBJECT_ACE_head
    SYSTEM_ALARM_CALLBACK_OBJECT_ACE._fields_ = [
        ("Header", win32more.Security.ACE_HEADER),
        ("Mask", UInt32),
        ("Flags", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", Guid),
        ("InheritedObjectType", Guid),
        ("SidStart", UInt32),
    ]
    return SYSTEM_ALARM_CALLBACK_OBJECT_ACE
ACL_INFORMATION_CLASS = Int32
ACL_INFORMATION_CLASS_AclRevisionInformation = 1
ACL_INFORMATION_CLASS_AclSizeInformation = 2
def _define_ACL_REVISION_INFORMATION_head():
    class ACL_REVISION_INFORMATION(Structure):
        pass
    return ACL_REVISION_INFORMATION
def _define_ACL_REVISION_INFORMATION():
    ACL_REVISION_INFORMATION = win32more.Security.ACL_REVISION_INFORMATION_head
    ACL_REVISION_INFORMATION._fields_ = [
        ("AclRevision", UInt32),
    ]
    return ACL_REVISION_INFORMATION
def _define_ACL_SIZE_INFORMATION_head():
    class ACL_SIZE_INFORMATION(Structure):
        pass
    return ACL_SIZE_INFORMATION
def _define_ACL_SIZE_INFORMATION():
    ACL_SIZE_INFORMATION = win32more.Security.ACL_SIZE_INFORMATION_head
    ACL_SIZE_INFORMATION._fields_ = [
        ("AceCount", UInt32),
        ("AclBytesInUse", UInt32),
        ("AclBytesFree", UInt32),
    ]
    return ACL_SIZE_INFORMATION
def _define_SECURITY_DESCRIPTOR_head():
    class SECURITY_DESCRIPTOR(Structure):
        pass
    return SECURITY_DESCRIPTOR
def _define_SECURITY_DESCRIPTOR():
    SECURITY_DESCRIPTOR = win32more.Security.SECURITY_DESCRIPTOR_head
    SECURITY_DESCRIPTOR._fields_ = [
        ("Revision", Byte),
        ("Sbz1", Byte),
        ("Control", UInt16),
        ("Owner", win32more.Foundation.PSID),
        ("Group", win32more.Foundation.PSID),
        ("Sacl", POINTER(win32more.Security.ACL_head)),
        ("Dacl", POINTER(win32more.Security.ACL_head)),
    ]
    return SECURITY_DESCRIPTOR
def _define_OBJECT_TYPE_LIST_head():
    class OBJECT_TYPE_LIST(Structure):
        pass
    return OBJECT_TYPE_LIST
def _define_OBJECT_TYPE_LIST():
    OBJECT_TYPE_LIST = win32more.Security.OBJECT_TYPE_LIST_head
    OBJECT_TYPE_LIST._fields_ = [
        ("Level", UInt16),
        ("Sbz", UInt16),
        ("ObjectType", POINTER(Guid)),
    ]
    return OBJECT_TYPE_LIST
AUDIT_EVENT_TYPE = Int32
AUDIT_EVENT_TYPE_AuditEventObjectAccess = 0
AUDIT_EVENT_TYPE_AuditEventDirectoryServiceAccess = 1
def _define_PRIVILEGE_SET_head():
    class PRIVILEGE_SET(Structure):
        pass
    return PRIVILEGE_SET
def _define_PRIVILEGE_SET():
    PRIVILEGE_SET = win32more.Security.PRIVILEGE_SET_head
    PRIVILEGE_SET._fields_ = [
        ("PrivilegeCount", UInt32),
        ("Control", UInt32),
        ("Privilege", win32more.Security.LUID_AND_ATTRIBUTES * 0),
    ]
    return PRIVILEGE_SET
def _define_ACCESS_REASONS_head():
    class ACCESS_REASONS(Structure):
        pass
    return ACCESS_REASONS
def _define_ACCESS_REASONS():
    ACCESS_REASONS = win32more.Security.ACCESS_REASONS_head
    ACCESS_REASONS._fields_ = [
        ("Data", UInt32 * 32),
    ]
    return ACCESS_REASONS
def _define_SE_SECURITY_DESCRIPTOR_head():
    class SE_SECURITY_DESCRIPTOR(Structure):
        pass
    return SE_SECURITY_DESCRIPTOR
def _define_SE_SECURITY_DESCRIPTOR():
    SE_SECURITY_DESCRIPTOR = win32more.Security.SE_SECURITY_DESCRIPTOR_head
    SE_SECURITY_DESCRIPTOR._fields_ = [
        ("Size", UInt32),
        ("Flags", UInt32),
        ("SecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
    ]
    return SE_SECURITY_DESCRIPTOR
def _define_SE_ACCESS_REQUEST_head():
    class SE_ACCESS_REQUEST(Structure):
        pass
    return SE_ACCESS_REQUEST
def _define_SE_ACCESS_REQUEST():
    SE_ACCESS_REQUEST = win32more.Security.SE_ACCESS_REQUEST_head
    SE_ACCESS_REQUEST._fields_ = [
        ("Size", UInt32),
        ("SeSecurityDescriptor", POINTER(win32more.Security.SE_SECURITY_DESCRIPTOR_head)),
        ("DesiredAccess", UInt32),
        ("PreviouslyGrantedAccess", UInt32),
        ("PrincipalSelfSid", win32more.Foundation.PSID),
        ("GenericMapping", POINTER(win32more.Security.GENERIC_MAPPING_head)),
        ("ObjectTypeListCount", UInt32),
        ("ObjectTypeList", POINTER(win32more.Security.OBJECT_TYPE_LIST_head)),
    ]
    return SE_ACCESS_REQUEST
def _define_SE_ACCESS_REPLY_head():
    class SE_ACCESS_REPLY(Structure):
        pass
    return SE_ACCESS_REPLY
def _define_SE_ACCESS_REPLY():
    SE_ACCESS_REPLY = win32more.Security.SE_ACCESS_REPLY_head
    SE_ACCESS_REPLY._fields_ = [
        ("Size", UInt32),
        ("ResultListCount", UInt32),
        ("GrantedAccess", POINTER(UInt32)),
        ("AccessStatus", POINTER(UInt32)),
        ("AccessReason", POINTER(win32more.Security.ACCESS_REASONS_head)),
        ("Privileges", POINTER(POINTER(win32more.Security.PRIVILEGE_SET_head))),
    ]
    return SE_ACCESS_REPLY
SECURITY_IMPERSONATION_LEVEL = Int32
SECURITY_IMPERSONATION_LEVEL_SecurityAnonymous = 0
SECURITY_IMPERSONATION_LEVEL_SecurityIdentification = 1
SECURITY_IMPERSONATION_LEVEL_SecurityImpersonation = 2
SECURITY_IMPERSONATION_LEVEL_SecurityDelegation = 3
TOKEN_TYPE = Int32
TOKEN_TYPE_TokenPrimary = 1
TOKEN_TYPE_TokenImpersonation = 2
TOKEN_ELEVATION_TYPE = Int32
TOKEN_ELEVATION_TYPE_TokenElevationTypeDefault = 1
TOKEN_ELEVATION_TYPE_TokenElevationTypeFull = 2
TOKEN_ELEVATION_TYPE_TokenElevationTypeLimited = 3
TOKEN_INFORMATION_CLASS = Int32
TOKEN_INFORMATION_CLASS_TokenUser = 1
TOKEN_INFORMATION_CLASS_TokenGroups = 2
TOKEN_INFORMATION_CLASS_TokenPrivileges = 3
TOKEN_INFORMATION_CLASS_TokenOwner = 4
TOKEN_INFORMATION_CLASS_TokenPrimaryGroup = 5
TOKEN_INFORMATION_CLASS_TokenDefaultDacl = 6
TOKEN_INFORMATION_CLASS_TokenSource = 7
TOKEN_INFORMATION_CLASS_TokenType = 8
TOKEN_INFORMATION_CLASS_TokenImpersonationLevel = 9
TOKEN_INFORMATION_CLASS_TokenStatistics = 10
TOKEN_INFORMATION_CLASS_TokenRestrictedSids = 11
TOKEN_INFORMATION_CLASS_TokenSessionId = 12
TOKEN_INFORMATION_CLASS_TokenGroupsAndPrivileges = 13
TOKEN_INFORMATION_CLASS_TokenSessionReference = 14
TOKEN_INFORMATION_CLASS_TokenSandBoxInert = 15
TOKEN_INFORMATION_CLASS_TokenAuditPolicy = 16
TOKEN_INFORMATION_CLASS_TokenOrigin = 17
TOKEN_INFORMATION_CLASS_TokenElevationType = 18
TOKEN_INFORMATION_CLASS_TokenLinkedToken = 19
TOKEN_INFORMATION_CLASS_TokenElevation = 20
TOKEN_INFORMATION_CLASS_TokenHasRestrictions = 21
TOKEN_INFORMATION_CLASS_TokenAccessInformation = 22
TOKEN_INFORMATION_CLASS_TokenVirtualizationAllowed = 23
TOKEN_INFORMATION_CLASS_TokenVirtualizationEnabled = 24
TOKEN_INFORMATION_CLASS_TokenIntegrityLevel = 25
TOKEN_INFORMATION_CLASS_TokenUIAccess = 26
TOKEN_INFORMATION_CLASS_TokenMandatoryPolicy = 27
TOKEN_INFORMATION_CLASS_TokenLogonSid = 28
TOKEN_INFORMATION_CLASS_TokenIsAppContainer = 29
TOKEN_INFORMATION_CLASS_TokenCapabilities = 30
TOKEN_INFORMATION_CLASS_TokenAppContainerSid = 31
TOKEN_INFORMATION_CLASS_TokenAppContainerNumber = 32
TOKEN_INFORMATION_CLASS_TokenUserClaimAttributes = 33
TOKEN_INFORMATION_CLASS_TokenDeviceClaimAttributes = 34
TOKEN_INFORMATION_CLASS_TokenRestrictedUserClaimAttributes = 35
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceClaimAttributes = 36
TOKEN_INFORMATION_CLASS_TokenDeviceGroups = 37
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceGroups = 38
TOKEN_INFORMATION_CLASS_TokenSecurityAttributes = 39
TOKEN_INFORMATION_CLASS_TokenIsRestricted = 40
TOKEN_INFORMATION_CLASS_TokenProcessTrustLevel = 41
TOKEN_INFORMATION_CLASS_TokenPrivateNameSpace = 42
TOKEN_INFORMATION_CLASS_TokenSingletonAttributes = 43
TOKEN_INFORMATION_CLASS_TokenBnoIsolation = 44
TOKEN_INFORMATION_CLASS_TokenChildProcessFlags = 45
TOKEN_INFORMATION_CLASS_TokenIsLessPrivilegedAppContainer = 46
TOKEN_INFORMATION_CLASS_TokenIsSandboxed = 47
TOKEN_INFORMATION_CLASS_MaxTokenInfoClass = 48
def _define_TOKEN_USER_head():
    class TOKEN_USER(Structure):
        pass
    return TOKEN_USER
def _define_TOKEN_USER():
    TOKEN_USER = win32more.Security.TOKEN_USER_head
    TOKEN_USER._fields_ = [
        ("User", win32more.Security.SID_AND_ATTRIBUTES),
    ]
    return TOKEN_USER
def _define_TOKEN_GROUPS_head():
    class TOKEN_GROUPS(Structure):
        pass
    return TOKEN_GROUPS
def _define_TOKEN_GROUPS():
    TOKEN_GROUPS = win32more.Security.TOKEN_GROUPS_head
    TOKEN_GROUPS._fields_ = [
        ("GroupCount", UInt32),
        ("Groups", win32more.Security.SID_AND_ATTRIBUTES * 0),
    ]
    return TOKEN_GROUPS
def _define_TOKEN_PRIVILEGES_head():
    class TOKEN_PRIVILEGES(Structure):
        pass
    return TOKEN_PRIVILEGES
def _define_TOKEN_PRIVILEGES():
    TOKEN_PRIVILEGES = win32more.Security.TOKEN_PRIVILEGES_head
    TOKEN_PRIVILEGES._fields_ = [
        ("PrivilegeCount", UInt32),
        ("Privileges", win32more.Security.LUID_AND_ATTRIBUTES * 0),
    ]
    return TOKEN_PRIVILEGES
def _define_TOKEN_OWNER_head():
    class TOKEN_OWNER(Structure):
        pass
    return TOKEN_OWNER
def _define_TOKEN_OWNER():
    TOKEN_OWNER = win32more.Security.TOKEN_OWNER_head
    TOKEN_OWNER._fields_ = [
        ("Owner", win32more.Foundation.PSID),
    ]
    return TOKEN_OWNER
def _define_TOKEN_PRIMARY_GROUP_head():
    class TOKEN_PRIMARY_GROUP(Structure):
        pass
    return TOKEN_PRIMARY_GROUP
def _define_TOKEN_PRIMARY_GROUP():
    TOKEN_PRIMARY_GROUP = win32more.Security.TOKEN_PRIMARY_GROUP_head
    TOKEN_PRIMARY_GROUP._fields_ = [
        ("PrimaryGroup", win32more.Foundation.PSID),
    ]
    return TOKEN_PRIMARY_GROUP
def _define_TOKEN_DEFAULT_DACL_head():
    class TOKEN_DEFAULT_DACL(Structure):
        pass
    return TOKEN_DEFAULT_DACL
def _define_TOKEN_DEFAULT_DACL():
    TOKEN_DEFAULT_DACL = win32more.Security.TOKEN_DEFAULT_DACL_head
    TOKEN_DEFAULT_DACL._fields_ = [
        ("DefaultDacl", POINTER(win32more.Security.ACL_head)),
    ]
    return TOKEN_DEFAULT_DACL
def _define_TOKEN_USER_CLAIMS_head():
    class TOKEN_USER_CLAIMS(Structure):
        pass
    return TOKEN_USER_CLAIMS
def _define_TOKEN_USER_CLAIMS():
    TOKEN_USER_CLAIMS = win32more.Security.TOKEN_USER_CLAIMS_head
    TOKEN_USER_CLAIMS._fields_ = [
        ("UserClaims", c_void_p),
    ]
    return TOKEN_USER_CLAIMS
def _define_TOKEN_DEVICE_CLAIMS_head():
    class TOKEN_DEVICE_CLAIMS(Structure):
        pass
    return TOKEN_DEVICE_CLAIMS
def _define_TOKEN_DEVICE_CLAIMS():
    TOKEN_DEVICE_CLAIMS = win32more.Security.TOKEN_DEVICE_CLAIMS_head
    TOKEN_DEVICE_CLAIMS._fields_ = [
        ("DeviceClaims", c_void_p),
    ]
    return TOKEN_DEVICE_CLAIMS
def _define_TOKEN_GROUPS_AND_PRIVILEGES_head():
    class TOKEN_GROUPS_AND_PRIVILEGES(Structure):
        pass
    return TOKEN_GROUPS_AND_PRIVILEGES
def _define_TOKEN_GROUPS_AND_PRIVILEGES():
    TOKEN_GROUPS_AND_PRIVILEGES = win32more.Security.TOKEN_GROUPS_AND_PRIVILEGES_head
    TOKEN_GROUPS_AND_PRIVILEGES._fields_ = [
        ("SidCount", UInt32),
        ("SidLength", UInt32),
        ("Sids", POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
        ("RestrictedSidCount", UInt32),
        ("RestrictedSidLength", UInt32),
        ("RestrictedSids", POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
        ("PrivilegeCount", UInt32),
        ("PrivilegeLength", UInt32),
        ("Privileges", POINTER(win32more.Security.LUID_AND_ATTRIBUTES_head)),
        ("AuthenticationId", win32more.Foundation.LUID),
    ]
    return TOKEN_GROUPS_AND_PRIVILEGES
def _define_TOKEN_LINKED_TOKEN_head():
    class TOKEN_LINKED_TOKEN(Structure):
        pass
    return TOKEN_LINKED_TOKEN
def _define_TOKEN_LINKED_TOKEN():
    TOKEN_LINKED_TOKEN = win32more.Security.TOKEN_LINKED_TOKEN_head
    TOKEN_LINKED_TOKEN._fields_ = [
        ("LinkedToken", win32more.Foundation.HANDLE),
    ]
    return TOKEN_LINKED_TOKEN
def _define_TOKEN_ELEVATION_head():
    class TOKEN_ELEVATION(Structure):
        pass
    return TOKEN_ELEVATION
def _define_TOKEN_ELEVATION():
    TOKEN_ELEVATION = win32more.Security.TOKEN_ELEVATION_head
    TOKEN_ELEVATION._fields_ = [
        ("TokenIsElevated", UInt32),
    ]
    return TOKEN_ELEVATION
def _define_TOKEN_MANDATORY_LABEL_head():
    class TOKEN_MANDATORY_LABEL(Structure):
        pass
    return TOKEN_MANDATORY_LABEL
def _define_TOKEN_MANDATORY_LABEL():
    TOKEN_MANDATORY_LABEL = win32more.Security.TOKEN_MANDATORY_LABEL_head
    TOKEN_MANDATORY_LABEL._fields_ = [
        ("Label", win32more.Security.SID_AND_ATTRIBUTES),
    ]
    return TOKEN_MANDATORY_LABEL
def _define_TOKEN_MANDATORY_POLICY_head():
    class TOKEN_MANDATORY_POLICY(Structure):
        pass
    return TOKEN_MANDATORY_POLICY
def _define_TOKEN_MANDATORY_POLICY():
    TOKEN_MANDATORY_POLICY = win32more.Security.TOKEN_MANDATORY_POLICY_head
    TOKEN_MANDATORY_POLICY._fields_ = [
        ("Policy", win32more.Security.TOKEN_MANDATORY_POLICY_ID),
    ]
    return TOKEN_MANDATORY_POLICY
def _define_TOKEN_ACCESS_INFORMATION_head():
    class TOKEN_ACCESS_INFORMATION(Structure):
        pass
    return TOKEN_ACCESS_INFORMATION
def _define_TOKEN_ACCESS_INFORMATION():
    TOKEN_ACCESS_INFORMATION = win32more.Security.TOKEN_ACCESS_INFORMATION_head
    TOKEN_ACCESS_INFORMATION._fields_ = [
        ("SidHash", POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)),
        ("RestrictedSidHash", POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)),
        ("Privileges", POINTER(win32more.Security.TOKEN_PRIVILEGES_head)),
        ("AuthenticationId", win32more.Foundation.LUID),
        ("TokenType", win32more.Security.TOKEN_TYPE),
        ("ImpersonationLevel", win32more.Security.SECURITY_IMPERSONATION_LEVEL),
        ("MandatoryPolicy", win32more.Security.TOKEN_MANDATORY_POLICY),
        ("Flags", UInt32),
        ("AppContainerNumber", UInt32),
        ("PackageSid", win32more.Foundation.PSID),
        ("CapabilitiesHash", POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)),
        ("TrustLevelSid", win32more.Foundation.PSID),
        ("SecurityAttributes", c_void_p),
    ]
    return TOKEN_ACCESS_INFORMATION
def _define_TOKEN_AUDIT_POLICY_head():
    class TOKEN_AUDIT_POLICY(Structure):
        pass
    return TOKEN_AUDIT_POLICY
def _define_TOKEN_AUDIT_POLICY():
    TOKEN_AUDIT_POLICY = win32more.Security.TOKEN_AUDIT_POLICY_head
    TOKEN_AUDIT_POLICY._fields_ = [
        ("PerUserPolicy", Byte * 30),
    ]
    return TOKEN_AUDIT_POLICY
def _define_TOKEN_SOURCE_head():
    class TOKEN_SOURCE(Structure):
        pass
    return TOKEN_SOURCE
def _define_TOKEN_SOURCE():
    TOKEN_SOURCE = win32more.Security.TOKEN_SOURCE_head
    TOKEN_SOURCE._fields_ = [
        ("SourceName", win32more.Foundation.CHAR * 8),
        ("SourceIdentifier", win32more.Foundation.LUID),
    ]
    return TOKEN_SOURCE
def _define_TOKEN_STATISTICS_head():
    class TOKEN_STATISTICS(Structure):
        pass
    return TOKEN_STATISTICS
def _define_TOKEN_STATISTICS():
    TOKEN_STATISTICS = win32more.Security.TOKEN_STATISTICS_head
    TOKEN_STATISTICS._fields_ = [
        ("TokenId", win32more.Foundation.LUID),
        ("AuthenticationId", win32more.Foundation.LUID),
        ("ExpirationTime", win32more.Foundation.LARGE_INTEGER),
        ("TokenType", win32more.Security.TOKEN_TYPE),
        ("ImpersonationLevel", win32more.Security.SECURITY_IMPERSONATION_LEVEL),
        ("DynamicCharged", UInt32),
        ("DynamicAvailable", UInt32),
        ("GroupCount", UInt32),
        ("PrivilegeCount", UInt32),
        ("ModifiedId", win32more.Foundation.LUID),
    ]
    return TOKEN_STATISTICS
def _define_TOKEN_CONTROL_head():
    class TOKEN_CONTROL(Structure):
        pass
    return TOKEN_CONTROL
def _define_TOKEN_CONTROL():
    TOKEN_CONTROL = win32more.Security.TOKEN_CONTROL_head
    TOKEN_CONTROL._fields_ = [
        ("TokenId", win32more.Foundation.LUID),
        ("AuthenticationId", win32more.Foundation.LUID),
        ("ModifiedId", win32more.Foundation.LUID),
        ("TokenSource", win32more.Security.TOKEN_SOURCE),
    ]
    return TOKEN_CONTROL
def _define_TOKEN_ORIGIN_head():
    class TOKEN_ORIGIN(Structure):
        pass
    return TOKEN_ORIGIN
def _define_TOKEN_ORIGIN():
    TOKEN_ORIGIN = win32more.Security.TOKEN_ORIGIN_head
    TOKEN_ORIGIN._fields_ = [
        ("OriginatingLogonSession", win32more.Foundation.LUID),
    ]
    return TOKEN_ORIGIN
MANDATORY_LEVEL = Int32
MANDATORY_LEVEL_MandatoryLevelUntrusted = 0
MANDATORY_LEVEL_MandatoryLevelLow = 1
MANDATORY_LEVEL_MandatoryLevelMedium = 2
MANDATORY_LEVEL_MandatoryLevelHigh = 3
MANDATORY_LEVEL_MandatoryLevelSystem = 4
MANDATORY_LEVEL_MandatoryLevelSecureProcess = 5
MANDATORY_LEVEL_MandatoryLevelCount = 6
def _define_TOKEN_APPCONTAINER_INFORMATION_head():
    class TOKEN_APPCONTAINER_INFORMATION(Structure):
        pass
    return TOKEN_APPCONTAINER_INFORMATION
def _define_TOKEN_APPCONTAINER_INFORMATION():
    TOKEN_APPCONTAINER_INFORMATION = win32more.Security.TOKEN_APPCONTAINER_INFORMATION_head
    TOKEN_APPCONTAINER_INFORMATION._fields_ = [
        ("TokenAppContainer", win32more.Foundation.PSID),
    ]
    return TOKEN_APPCONTAINER_INFORMATION
def _define_CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE_head():
    class CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE(Structure):
        pass
    return CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE
def _define_CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE():
    CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE = win32more.Security.CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE_head
    CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE._fields_ = [
        ("Version", UInt64),
        ("Name", win32more.Foundation.PWSTR),
    ]
    return CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE
def _define_CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head():
    class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(Structure):
        pass
    return CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE
def _define_CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE():
    CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE = win32more.Security.CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head
    CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE._fields_ = [
        ("pValue", c_void_p),
        ("ValueLength", UInt32),
    ]
    return CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE
def _define_CLAIM_SECURITY_ATTRIBUTE_V1_head():
    class CLAIM_SECURITY_ATTRIBUTE_V1(Structure):
        pass
    return CLAIM_SECURITY_ATTRIBUTE_V1
def _define_CLAIM_SECURITY_ATTRIBUTE_V1():
    CLAIM_SECURITY_ATTRIBUTE_V1 = win32more.Security.CLAIM_SECURITY_ATTRIBUTE_V1_head
    class CLAIM_SECURITY_ATTRIBUTE_V1__Values_e__Union(Union):
        pass
    CLAIM_SECURITY_ATTRIBUTE_V1__Values_e__Union._fields_ = [
        ("pInt64", POINTER(Int64)),
        ("pUint64", POINTER(UInt64)),
        ("ppString", POINTER(win32more.Foundation.PWSTR)),
        ("pFqbn", POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE_head)),
        ("pOctetString", POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head)),
    ]
    CLAIM_SECURITY_ATTRIBUTE_V1._fields_ = [
        ("Name", win32more.Foundation.PWSTR),
        ("ValueType", win32more.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE),
        ("Reserved", UInt16),
        ("Flags", UInt32),
        ("ValueCount", UInt32),
        ("Values", CLAIM_SECURITY_ATTRIBUTE_V1__Values_e__Union),
    ]
    return CLAIM_SECURITY_ATTRIBUTE_V1
def _define_CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1_head():
    class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(Structure):
        pass
    return CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
def _define_CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1():
    CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 = win32more.Security.CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1_head
    class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1__Values_e__Union(Union):
        pass
    CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1__Values_e__Union._fields_ = [
        ("pInt64", UInt32 * 0),
        ("pUint64", UInt32 * 0),
        ("ppString", UInt32 * 0),
        ("pFqbn", UInt32 * 0),
        ("pOctetString", UInt32 * 0),
    ]
    CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1._fields_ = [
        ("Name", UInt32),
        ("ValueType", win32more.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE),
        ("Reserved", UInt16),
        ("Flags", win32more.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS),
        ("ValueCount", UInt32),
        ("Values", CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1__Values_e__Union),
    ]
    return CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
def _define_CLAIM_SECURITY_ATTRIBUTES_INFORMATION_head():
    class CLAIM_SECURITY_ATTRIBUTES_INFORMATION(Structure):
        pass
    return CLAIM_SECURITY_ATTRIBUTES_INFORMATION
def _define_CLAIM_SECURITY_ATTRIBUTES_INFORMATION():
    CLAIM_SECURITY_ATTRIBUTES_INFORMATION = win32more.Security.CLAIM_SECURITY_ATTRIBUTES_INFORMATION_head
    class CLAIM_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union(Union):
        pass
    CLAIM_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union._fields_ = [
        ("pAttributeV1", POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_V1_head)),
    ]
    CLAIM_SECURITY_ATTRIBUTES_INFORMATION._fields_ = [
        ("Version", UInt16),
        ("Reserved", UInt16),
        ("AttributeCount", UInt32),
        ("Attribute", CLAIM_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union),
    ]
    return CLAIM_SECURITY_ATTRIBUTES_INFORMATION
def _define_SECURITY_QUALITY_OF_SERVICE_head():
    class SECURITY_QUALITY_OF_SERVICE(Structure):
        pass
    return SECURITY_QUALITY_OF_SERVICE
def _define_SECURITY_QUALITY_OF_SERVICE():
    SECURITY_QUALITY_OF_SERVICE = win32more.Security.SECURITY_QUALITY_OF_SERVICE_head
    SECURITY_QUALITY_OF_SERVICE._fields_ = [
        ("Length", UInt32),
        ("ImpersonationLevel", win32more.Security.SECURITY_IMPERSONATION_LEVEL),
        ("ContextTrackingMode", Byte),
        ("EffectiveOnly", win32more.Foundation.BOOLEAN),
    ]
    return SECURITY_QUALITY_OF_SERVICE
def _define_SE_IMPERSONATION_STATE_head():
    class SE_IMPERSONATION_STATE(Structure):
        pass
    return SE_IMPERSONATION_STATE
def _define_SE_IMPERSONATION_STATE():
    SE_IMPERSONATION_STATE = win32more.Security.SE_IMPERSONATION_STATE_head
    SE_IMPERSONATION_STATE._fields_ = [
        ("Token", c_void_p),
        ("CopyOnOpen", win32more.Foundation.BOOLEAN),
        ("EffectiveOnly", win32more.Foundation.BOOLEAN),
        ("Level", win32more.Security.SECURITY_IMPERSONATION_LEVEL),
    ]
    return SE_IMPERSONATION_STATE
def _define_SECURITY_CAPABILITIES_head():
    class SECURITY_CAPABILITIES(Structure):
        pass
    return SECURITY_CAPABILITIES
def _define_SECURITY_CAPABILITIES():
    SECURITY_CAPABILITIES = win32more.Security.SECURITY_CAPABILITIES_head
    SECURITY_CAPABILITIES._fields_ = [
        ("AppContainerSid", win32more.Foundation.PSID),
        ("Capabilities", POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
        ("CapabilityCount", UInt32),
        ("Reserved", UInt32),
    ]
    return SECURITY_CAPABILITIES
def _define_QUOTA_LIMITS_head():
    class QUOTA_LIMITS(Structure):
        pass
    return QUOTA_LIMITS
def _define_QUOTA_LIMITS():
    QUOTA_LIMITS = win32more.Security.QUOTA_LIMITS_head
    QUOTA_LIMITS._fields_ = [
        ("PagedPoolLimit", UIntPtr),
        ("NonPagedPoolLimit", UIntPtr),
        ("MinimumWorkingSetSize", UIntPtr),
        ("MaximumWorkingSetSize", UIntPtr),
        ("PagefileLimit", UIntPtr),
        ("TimeLimit", win32more.Foundation.LARGE_INTEGER),
    ]
    return QUOTA_LIMITS
def _define_AccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=True)(("AccessCheck", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'GenericMapping'),(1, 'PrivilegeSet'),(1, 'PrivilegeSetLength'),(1, 'GrantedAccess'),(1, 'AccessStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckAndAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(Int32),POINTER(Int32), use_last_error=False)(("AccessCheckAndAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'DesiredAccess'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatus'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckAndAuditAlarm():
    return win32more.Security.AccessCheckAndAuditAlarmW
def _define_AccessCheckByType():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=True)(("AccessCheckByType", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'PrivilegeSet'),(1, 'PrivilegeSetLength'),(1, 'GrantedAccess'),(1, 'AccessStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeResultList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("AccessCheckByTypeResultList", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'PrivilegeSet'),(1, 'PrivilegeSetLength'),(1, 'GrantedAccessList'),(1, 'AccessStatusList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeAndAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(Int32),POINTER(Int32), use_last_error=False)(("AccessCheckByTypeAndAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatus'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeAndAuditAlarm():
    return win32more.Security.AccessCheckByTypeAndAuditAlarmW
def _define_AccessCheckByTypeResultListAndAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=False)(("AccessCheckByTypeResultListAndAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccessList'),(1, 'AccessStatusList'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeResultListAndAuditAlarm():
    return win32more.Security.AccessCheckByTypeResultListAndAuditAlarmW
def _define_AccessCheckByTypeResultListAndAuditAlarmByHandleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=False)(("AccessCheckByTypeResultListAndAuditAlarmByHandleW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ClientToken'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccessList'),(1, 'AccessStatusList'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeResultListAndAuditAlarmByHandle():
    return win32more.Security.AccessCheckByTypeResultListAndAuditAlarmByHandleW
def _define_AddAccessAllowedAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddAccessAllowedAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AccessMask'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAccessAllowedAceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddAccessAllowedAceEx", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAccessAllowedObjectAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,POINTER(Guid),POINTER(Guid),win32more.Foundation.PSID, use_last_error=True)(("AddAccessAllowedObjectAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'ObjectTypeGuid'),(1, 'InheritedObjectTypeGuid'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAccessDeniedAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddAccessDeniedAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AccessMask'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAccessDeniedAceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddAccessDeniedAceEx", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAccessDeniedObjectAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,POINTER(Guid),POINTER(Guid),win32more.Foundation.PSID, use_last_error=True)(("AddAccessDeniedObjectAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'ObjectTypeGuid'),(1, 'InheritedObjectTypeGuid'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,UInt32,c_void_p,UInt32, use_last_error=True)(("AddAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'dwStartingAceIndex'),(1, 'pAceList'),(1, 'nAceListLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAuditAccessAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,UInt32,win32more.Foundation.PSID,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("AddAuditAccessAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'dwAccessMask'),(1, 'pSid'),(1, 'bAuditSuccess'),(1, 'bAuditFailure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAuditAccessAceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("AddAuditAccessAceEx", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'dwAccessMask'),(1, 'pSid'),(1, 'bAuditSuccess'),(1, 'bAuditFailure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAuditAccessObjectAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,POINTER(Guid),POINTER(Guid),win32more.Foundation.PSID,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("AddAuditAccessObjectAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'ObjectTypeGuid'),(1, 'InheritedObjectTypeGuid'),(1, 'pSid'),(1, 'bAuditSuccess'),(1, 'bAuditFailure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddMandatoryAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),win32more.Security.ACE_REVISION,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddMandatoryAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'MandatoryPolicy'),(1, 'pLabelSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddResourceAttributeAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID,POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTES_INFORMATION_head),POINTER(UInt32), use_last_error=True)(("AddResourceAttributeAce", windll["KERNEL32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'pSid'),(1, 'pAttributeInfo'),(1, 'pReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddScopedPolicyIDAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,UInt32,win32more.Foundation.PSID, use_last_error=True)(("AddScopedPolicyIDAce", windll["KERNEL32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AccessMask'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdjustTokenGroups():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.Security.TOKEN_GROUPS_head),UInt32,POINTER(win32more.Security.TOKEN_GROUPS_head),POINTER(UInt32), use_last_error=True)(("AdjustTokenGroups", windll["ADVAPI32"]), ((1, 'TokenHandle'),(1, 'ResetToDefault'),(1, 'NewState'),(1, 'BufferLength'),(1, 'PreviousState'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdjustTokenPrivileges():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.Security.TOKEN_PRIVILEGES_head),UInt32,POINTER(win32more.Security.TOKEN_PRIVILEGES_head),POINTER(UInt32), use_last_error=True)(("AdjustTokenPrivileges", windll["ADVAPI32"]), ((1, 'TokenHandle'),(1, 'DisableAllPrivileges'),(1, 'NewState'),(1, 'BufferLength'),(1, 'PreviousState'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocateAndInitializeSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head),Byte,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.PSID), use_last_error=True)(("AllocateAndInitializeSid", windll["ADVAPI32"]), ((1, 'pIdentifierAuthority'),(1, 'nSubAuthorityCount'),(1, 'nSubAuthority0'),(1, 'nSubAuthority1'),(1, 'nSubAuthority2'),(1, 'nSubAuthority3'),(1, 'nSubAuthority4'),(1, 'nSubAuthority5'),(1, 'nSubAuthority6'),(1, 'nSubAuthority7'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocateLocallyUniqueId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.LUID_head), use_last_error=True)(("AllocateLocallyUniqueId", windll["ADVAPI32"]), ((1, 'Luid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreAllAccessesGranted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(("AreAllAccessesGranted", windll["ADVAPI32"]), ((1, 'GrantedAccess'),(1, 'DesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreAnyAccessesGranted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(("AreAnyAccessesGranted", windll["ADVAPI32"]), ((1, 'GrantedAccess'),(1, 'DesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckTokenMembership():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSID,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("CheckTokenMembership", windll["ADVAPI32"]), ((1, 'TokenHandle'),(1, 'SidToCheck'),(1, 'IsMember'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckTokenCapability():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSID,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("CheckTokenCapability", windll["KERNEL32"]), ((1, 'TokenHandle'),(1, 'CapabilitySidToCheck'),(1, 'HasCapability'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAppContainerAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("GetAppContainerAce", windll["KERNEL32"]), ((1, 'Acl'),(1, 'StartingAceIndex'),(1, 'AppContainerAce'),(1, 'AppContainerAceIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckTokenMembershipEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSID,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("CheckTokenMembershipEx", windll["KERNEL32"]), ((1, 'TokenHandle'),(1, 'SidToCheck'),(1, 'Flags'),(1, 'IsMember'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertToAutoInheritPrivateObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(Guid),win32more.Foundation.BOOLEAN,POINTER(win32more.Security.GENERIC_MAPPING_head), use_last_error=True)(("ConvertToAutoInheritPrivateObjectSecurity", windll["ADVAPI32"]), ((1, 'ParentDescriptor'),(1, 'CurrentSecurityDescriptor'),(1, 'NewSecurityDescriptor'),(1, 'ObjectType'),(1, 'IsDirectoryObject'),(1, 'GenericMapping'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopySid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID, use_last_error=True)(("CopySid", windll["ADVAPI32"]), ((1, 'nDestinationSidLength'),(1, 'pDestinationSid'),(1, 'pSourceSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePrivateObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Security.GENERIC_MAPPING_head), use_last_error=True)(("CreatePrivateObjectSecurity", windll["ADVAPI32"]), ((1, 'ParentDescriptor'),(1, 'CreatorDescriptor'),(1, 'NewDescriptor'),(1, 'IsDirectoryObject'),(1, 'Token'),(1, 'GenericMapping'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePrivateObjectSecurityEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(Guid),win32more.Foundation.BOOL,win32more.Security.SECURITY_AUTO_INHERIT_FLAGS,win32more.Foundation.HANDLE,POINTER(win32more.Security.GENERIC_MAPPING_head), use_last_error=True)(("CreatePrivateObjectSecurityEx", windll["ADVAPI32"]), ((1, 'ParentDescriptor'),(1, 'CreatorDescriptor'),(1, 'NewDescriptor'),(1, 'ObjectType'),(1, 'IsContainerObject'),(1, 'AutoInheritFlags'),(1, 'Token'),(1, 'GenericMapping'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePrivateObjectSecurityWithMultipleInheritance():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(POINTER(Guid)),UInt32,win32more.Foundation.BOOL,win32more.Security.SECURITY_AUTO_INHERIT_FLAGS,win32more.Foundation.HANDLE,POINTER(win32more.Security.GENERIC_MAPPING_head), use_last_error=True)(("CreatePrivateObjectSecurityWithMultipleInheritance", windll["ADVAPI32"]), ((1, 'ParentDescriptor'),(1, 'CreatorDescriptor'),(1, 'NewDescriptor'),(1, 'ObjectTypes'),(1, 'GuidCount'),(1, 'IsContainerObject'),(1, 'AutoInheritFlags'),(1, 'Token'),(1, 'GenericMapping'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRestrictedToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.CREATE_RESTRICTED_TOKEN_FLAGS,UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES),UInt32,POINTER(win32more.Security.LUID_AND_ATTRIBUTES),UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES),POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("CreateRestrictedToken", windll["ADVAPI32"]), ((1, 'ExistingTokenHandle'),(1, 'Flags'),(1, 'DisableSidCount'),(1, 'SidsToDisable'),(1, 'DeletePrivilegeCount'),(1, 'PrivilegesToDelete'),(1, 'RestrictedSidCount'),(1, 'SidsToRestrict'),(1, 'NewTokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateWellKnownSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.WELL_KNOWN_SID_TYPE,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(UInt32), use_last_error=True)(("CreateWellKnownSid", windll["ADVAPI32"]), ((1, 'WellKnownSidType'),(1, 'DomainSid'),(1, 'pSid'),(1, 'cbSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EqualDomainSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("EqualDomainSid", windll["ADVAPI32"]), ((1, 'pSid1'),(1, 'pSid2'),(1, 'pfEqual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32, use_last_error=True)(("DeleteAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyPrivateObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=True)(("DestroyPrivateObjectSecurity", windll["ADVAPI32"]), ((1, 'ObjectDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DuplicateToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.SECURITY_IMPERSONATION_LEVEL,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("DuplicateToken", windll["ADVAPI32"]), ((1, 'ExistingTokenHandle'),(1, 'ImpersonationLevel'),(1, 'DuplicateTokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DuplicateTokenEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.TOKEN_ACCESS_MASK,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Security.SECURITY_IMPERSONATION_LEVEL,win32more.Security.TOKEN_TYPE,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("DuplicateTokenEx", windll["ADVAPI32"]), ((1, 'hExistingToken'),(1, 'dwDesiredAccess'),(1, 'lpTokenAttributes'),(1, 'ImpersonationLevel'),(1, 'TokenType'),(1, 'phNewToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EqualPrefixSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,win32more.Foundation.PSID, use_last_error=True)(("EqualPrefixSid", windll["ADVAPI32"]), ((1, 'pSid1'),(1, 'pSid2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EqualSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,win32more.Foundation.PSID, use_last_error=True)(("EqualSid", windll["ADVAPI32"]), ((1, 'pSid1'),(1, 'pSid2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFreeAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),POINTER(c_void_p), use_last_error=True)(("FindFirstFreeAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'pAce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeSid():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.PSID, use_last_error=False)(("FreeSid", windll["ADVAPI32"]), ((1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,POINTER(c_void_p), use_last_error=True)(("GetAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceIndex'),(1, 'pAce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAclInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),c_void_p,UInt32,win32more.Security.ACL_INFORMATION_CLASS, use_last_error=True)(("GetAclInformation", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'pAclInformation'),(1, 'nAclInformationLength'),(1, 'dwAclInformationClass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileSecurityW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=False)(("GetFileSecurityW", windll["ADVAPI32"]), ((1, 'lpFileName'),(1, 'RequestedInformation'),(1, 'pSecurityDescriptor'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileSecurity():
    return win32more.Security.GetFileSecurityW
def _define_GetKernelObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("GetKernelObjectSecurity", windll["ADVAPI32"]), ((1, 'Handle'),(1, 'RequestedInformation'),(1, 'pSecurityDescriptor'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLengthSid():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSID, use_last_error=False)(("GetLengthSid", windll["ADVAPI32"]), ((1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPrivateObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("GetPrivateObjectSecurity", windll["ADVAPI32"]), ((1, 'ObjectDescriptor'),(1, 'SecurityInformation'),(1, 'ResultantDescriptor'),(1, 'DescriptorLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorControl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt16),POINTER(UInt32), use_last_error=True)(("GetSecurityDescriptorControl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'pControl'),(1, 'lpdwRevision'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorDacl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(Int32),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(Int32), use_last_error=True)(("GetSecurityDescriptorDacl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'lpbDaclPresent'),(1, 'pDacl'),(1, 'lpbDaclDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Foundation.PSID),POINTER(Int32), use_last_error=True)(("GetSecurityDescriptorGroup", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'pGroup'),(1, 'lpbGroupDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorLength():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("GetSecurityDescriptorLength", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorOwner():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Foundation.PSID),POINTER(Int32), use_last_error=True)(("GetSecurityDescriptorOwner", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'pOwner'),(1, 'lpbOwnerDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorRMControl():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),c_char_p_no, use_last_error=False)(("GetSecurityDescriptorRMControl", windll["ADVAPI32"]), ((1, 'SecurityDescriptor'),(1, 'RMControl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSecurityDescriptorSacl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(Int32),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(Int32), use_last_error=True)(("GetSecurityDescriptorSacl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'lpbSaclPresent'),(1, 'pSacl'),(1, 'lpbSaclDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSidIdentifierAuthority():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head),win32more.Foundation.PSID, use_last_error=True)(("GetSidIdentifierAuthority", windll["ADVAPI32"]), ((1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSidLengthRequired():
    try:
        return WINFUNCTYPE(UInt32,Byte, use_last_error=False)(("GetSidLengthRequired", windll["ADVAPI32"]), ((1, 'nSubAuthorityCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSidSubAuthority():
    try:
        return WINFUNCTYPE(POINTER(UInt32),win32more.Foundation.PSID,UInt32, use_last_error=True)(("GetSidSubAuthority", windll["ADVAPI32"]), ((1, 'pSid'),(1, 'nSubAuthority'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSidSubAuthorityCount():
    try:
        return WINFUNCTYPE(c_char_p_no,win32more.Foundation.PSID, use_last_error=True)(("GetSidSubAuthorityCount", windll["ADVAPI32"]), ((1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTokenInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.TOKEN_INFORMATION_CLASS,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("GetTokenInformation", windll["ADVAPI32"]), ((1, 'TokenHandle'),(1, 'TokenInformationClass'),(1, 'TokenInformation'),(1, 'TokenInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowsAccountDomainSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(UInt32), use_last_error=True)(("GetWindowsAccountDomainSid", windll["ADVAPI32"]), ((1, 'pSid'),(1, 'pDomainSid'),(1, 'cbDomainSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImpersonateAnonymousToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("ImpersonateAnonymousToken", windll["ADVAPI32"]), ((1, 'ThreadHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImpersonateLoggedOnUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("ImpersonateLoggedOnUser", windll["ADVAPI32"]), ((1, 'hToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImpersonateSelf():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.SECURITY_IMPERSONATION_LEVEL, use_last_error=True)(("ImpersonateSelf", windll["ADVAPI32"]), ((1, 'ImpersonationLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeAcl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,UInt32, use_last_error=True)(("InitializeAcl", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'nAclLength'),(1, 'dwAclRevision'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeSecurityDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32, use_last_error=True)(("InitializeSecurityDescriptor", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'dwRevision'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head),Byte, use_last_error=True)(("InitializeSid", windll["ADVAPI32"]), ((1, 'Sid'),(1, 'pIdentifierAuthority'),(1, 'nSubAuthorityCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsTokenRestricted():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("IsTokenRestricted", windll["ADVAPI32"]), ((1, 'TokenHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidAcl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head), use_last_error=False)(("IsValidAcl", windll["ADVAPI32"]), ((1, 'pAcl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidSecurityDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("IsValidSecurityDescriptor", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID, use_last_error=False)(("IsValidSid", windll["ADVAPI32"]), ((1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWellKnownSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,win32more.Security.WELL_KNOWN_SID_TYPE, use_last_error=False)(("IsWellKnownSid", windll["ADVAPI32"]), ((1, 'pSid'),(1, 'WellKnownSidType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MakeAbsoluteSD():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32),POINTER(win32more.Security.ACL_head),POINTER(UInt32),POINTER(win32more.Security.ACL_head),POINTER(UInt32),win32more.Foundation.PSID,POINTER(UInt32),win32more.Foundation.PSID,POINTER(UInt32), use_last_error=True)(("MakeAbsoluteSD", windll["ADVAPI32"]), ((1, 'pSelfRelativeSecurityDescriptor'),(1, 'pAbsoluteSecurityDescriptor'),(1, 'lpdwAbsoluteSecurityDescriptorSize'),(1, 'pDacl'),(1, 'lpdwDaclSize'),(1, 'pSacl'),(1, 'lpdwSaclSize'),(1, 'pOwner'),(1, 'lpdwOwnerSize'),(1, 'pPrimaryGroup'),(1, 'lpdwPrimaryGroupSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MakeSelfRelativeSD():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32), use_last_error=True)(("MakeSelfRelativeSD", windll["ADVAPI32"]), ((1, 'pAbsoluteSecurityDescriptor'),(1, 'pSelfRelativeSecurityDescriptor'),(1, 'lpdwBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapGenericMask():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Security.GENERIC_MAPPING_head), use_last_error=False)(("MapGenericMask", windll["ADVAPI32"]), ((1, 'AccessMask'),(1, 'GenericMapping'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectCloseAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.BOOL, use_last_error=False)(("ObjectCloseAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectCloseAuditAlarm():
    return win32more.Security.ObjectCloseAuditAlarmW
def _define_ObjectDeleteAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.BOOL, use_last_error=False)(("ObjectDeleteAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectDeleteAuditAlarm():
    return win32more.Security.ObjectDeleteAuditAlarmW
def _define_ObjectOpenAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(("ObjectOpenAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'pSecurityDescriptor'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'GrantedAccess'),(1, 'Privileges'),(1, 'ObjectCreation'),(1, 'AccessGranted'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectOpenAuditAlarm():
    return win32more.Security.ObjectOpenAuditAlarmW
def _define_ObjectPrivilegeAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL, use_last_error=False)(("ObjectPrivilegeAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'Privileges'),(1, 'AccessGranted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectPrivilegeAuditAlarm():
    return win32more.Security.ObjectPrivilegeAuditAlarmW
def _define_PrivilegeCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(Int32), use_last_error=True)(("PrivilegeCheck", windll["ADVAPI32"]), ((1, 'ClientToken'),(1, 'RequiredPrivileges'),(1, 'pfResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrivilegedServiceAuditAlarmW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL, use_last_error=False)(("PrivilegedServiceAuditAlarmW", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'ServiceName'),(1, 'ClientToken'),(1, 'Privileges'),(1, 'AccessGranted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrivilegedServiceAuditAlarm():
    return win32more.Security.PrivilegedServiceAuditAlarmW
def _define_QuerySecurityAccessMask():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(UInt32), use_last_error=False)(("QuerySecurityAccessMask", windll["ADVAPI32"]), ((1, 'SecurityInformation'),(1, 'DesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RevertToSelf():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=True)(("RevertToSelf", windll["ADVAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetAclInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),c_void_p,UInt32,win32more.Security.ACL_INFORMATION_CLASS, use_last_error=True)(("SetAclInformation", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'pAclInformation'),(1, 'nAclInformationLength'),(1, 'dwAclInformationClass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileSecurityW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("SetFileSecurityW", windll["ADVAPI32"]), ((1, 'lpFileName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileSecurity():
    return win32more.Security.SetFileSecurityW
def _define_SetKernelObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=True)(("SetKernelObjectSecurity", windll["ADVAPI32"]), ((1, 'Handle'),(1, 'SecurityInformation'),(1, 'SecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPrivateObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.HANDLE, use_last_error=True)(("SetPrivateObjectSecurity", windll["ADVAPI32"]), ((1, 'SecurityInformation'),(1, 'ModificationDescriptor'),(1, 'ObjectsSecurityDescriptor'),(1, 'GenericMapping'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPrivateObjectSecurityEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),win32more.Security.SECURITY_AUTO_INHERIT_FLAGS,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.HANDLE, use_last_error=True)(("SetPrivateObjectSecurityEx", windll["ADVAPI32"]), ((1, 'SecurityInformation'),(1, 'ModificationDescriptor'),(1, 'ObjectsSecurityDescriptor'),(1, 'AutoInheritFlags'),(1, 'GenericMapping'),(1, 'Token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityAccessMask():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(UInt32), use_last_error=False)(("SetSecurityAccessMask", windll["ADVAPI32"]), ((1, 'SecurityInformation'),(1, 'DesiredAccess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorControl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt16,UInt16, use_last_error=True)(("SetSecurityDescriptorControl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'ControlBitsOfInterest'),(1, 'ControlBitsToSet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorDacl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),win32more.Foundation.BOOL, use_last_error=True)(("SetSecurityDescriptorDacl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'bDaclPresent'),(1, 'pDacl'),(1, 'bDaclDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,win32more.Foundation.BOOL, use_last_error=True)(("SetSecurityDescriptorGroup", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'pGroup'),(1, 'bGroupDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorOwner():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,win32more.Foundation.BOOL, use_last_error=True)(("SetSecurityDescriptorOwner", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'pOwner'),(1, 'bOwnerDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorRMControl():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),c_char_p_no, use_last_error=False)(("SetSecurityDescriptorRMControl", windll["ADVAPI32"]), ((1, 'SecurityDescriptor'),(1, 'RMControl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSecurityDescriptorSacl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),win32more.Foundation.BOOL, use_last_error=True)(("SetSecurityDescriptorSacl", windll["ADVAPI32"]), ((1, 'pSecurityDescriptor'),(1, 'bSaclPresent'),(1, 'pSacl'),(1, 'bSaclDefaulted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTokenInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Security.TOKEN_INFORMATION_CLASS,c_void_p,UInt32, use_last_error=True)(("SetTokenInformation", windll["ADVAPI32"]), ((1, 'TokenHandle'),(1, 'TokenInformationClass'),(1, 'TokenInformation'),(1, 'TokenInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCachedSigningLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE),UInt32,UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("SetCachedSigningLevel", windll["KERNEL32"]), ((1, 'SourceFiles'),(1, 'SourceFileCount'),(1, 'Flags'),(1, 'TargetFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCachedSigningLevel():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),c_char_p_no,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetCachedSigningLevel", windll["KERNEL32"]), ((1, 'File'),(1, 'Flags'),(1, 'SigningLevel'),(1, 'Thumbprint'),(1, 'ThumbprintSize'),(1, 'ThumbprintAlgorithm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeriveCapabilitySidsFromName():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Foundation.PSID)),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.PSID)),POINTER(UInt32), use_last_error=True)(("DeriveCapabilitySidsFromName", windll["api-ms-win-security-base-l1-2-2"]), ((1, 'CapName'),(1, 'CapabilityGroupSids'),(1, 'CapabilityGroupSidCount'),(1, 'CapabilitySids'),(1, 'CapabilitySidCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlNormalizeSecurityDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32),win32more.Foundation.BOOLEAN, use_last_error=False)(("RtlNormalizeSecurityDescriptor", windll["ntdll"]), ((1, 'SecurityDescriptor'),(1, 'SecurityDescriptorLength'),(1, 'NewSecurityDescriptor'),(1, 'NewSecurityDescriptorLength'),(1, 'CheckOnly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Security.OBJECT_SECURITY_INFORMATION),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=True)(("SetUserObjectSecurity", windll["USER32"]), ((1, 'hObj'),(1, 'pSIRequested'),(1, 'pSID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUserObjectSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("GetUserObjectSecurity", windll["USER32"]), ((1, 'hObj'),(1, 'pSIRequested'),(1, 'pSID'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckAndAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(Int32),POINTER(Int32), use_last_error=True)(("AccessCheckAndAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'DesiredAccess'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatus'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeAndAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(Int32),POINTER(Int32), use_last_error=True)(("AccessCheckByTypeAndAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatus'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeResultListAndAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=True)(("AccessCheckByTypeResultListAndAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatusList'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessCheckByTypeResultListAndAuditAlarmByHandleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.PSID,UInt32,win32more.Security.AUDIT_EVENT_TYPE,UInt32,POINTER(win32more.Security.OBJECT_TYPE_LIST),UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32),POINTER(Int32), use_last_error=True)(("AccessCheckByTypeResultListAndAuditAlarmByHandleA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ClientToken'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'SecurityDescriptor'),(1, 'PrincipalSelfSid'),(1, 'DesiredAccess'),(1, 'AuditType'),(1, 'Flags'),(1, 'ObjectTypeList'),(1, 'ObjectTypeListLength'),(1, 'GenericMapping'),(1, 'ObjectCreation'),(1, 'GrantedAccess'),(1, 'AccessStatusList'),(1, 'pfGenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectOpenAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=True)(("ObjectOpenAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ObjectTypeName'),(1, 'ObjectName'),(1, 'pSecurityDescriptor'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'GrantedAccess'),(1, 'Privileges'),(1, 'ObjectCreation'),(1, 'AccessGranted'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectPrivilegeAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL, use_last_error=True)(("ObjectPrivilegeAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'ClientToken'),(1, 'DesiredAccess'),(1, 'Privileges'),(1, 'AccessGranted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectCloseAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.BOOL, use_last_error=True)(("ObjectCloseAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectDeleteAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,c_void_p,win32more.Foundation.BOOL, use_last_error=True)(("ObjectDeleteAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'HandleId'),(1, 'GenerateOnClose'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrivilegedServiceAuditAlarmA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.HANDLE,POINTER(win32more.Security.PRIVILEGE_SET_head),win32more.Foundation.BOOL, use_last_error=True)(("PrivilegedServiceAuditAlarmA", windll["ADVAPI32"]), ((1, 'SubsystemName'),(1, 'ServiceName'),(1, 'ClientToken'),(1, 'Privileges'),(1, 'AccessGranted'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddConditionalAce():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head),UInt32,win32more.Security.ACE_FLAGS,Byte,UInt32,win32more.Foundation.PSID,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=True)(("AddConditionalAce", windll["ADVAPI32"]), ((1, 'pAcl'),(1, 'dwAceRevision'),(1, 'AceFlags'),(1, 'AceType'),(1, 'AccessMask'),(1, 'pSid'),(1, 'ConditionStr'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileSecurityA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=True)(("SetFileSecurityA", windll["ADVAPI32"]), ((1, 'lpFileName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileSecurityA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("GetFileSecurityA", windll["ADVAPI32"]), ((1, 'lpFileName'),(1, 'RequestedInformation'),(1, 'pSecurityDescriptor'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupAccountSidA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSID,POINTER(Byte),POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(win32more.Security.SID_NAME_USE), use_last_error=True)(("LookupAccountSidA", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'Sid'),(1, 'Name'),(1, 'cchName'),(1, 'ReferencedDomainName'),(1, 'cchReferencedDomainName'),(1, 'peUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupAccountSidW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PSID,POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(win32more.Security.SID_NAME_USE), use_last_error=True)(("LookupAccountSidW", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'Sid'),(1, 'Name'),(1, 'cchName'),(1, 'ReferencedDomainName'),(1, 'cchReferencedDomainName'),(1, 'peUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupAccountSid():
    return win32more.Security.LookupAccountSidW
def _define_LookupAccountNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSID,POINTER(UInt32),POINTER(Byte),POINTER(UInt32),POINTER(win32more.Security.SID_NAME_USE), use_last_error=True)(("LookupAccountNameA", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpAccountName'),(1, 'Sid'),(1, 'cbSid'),(1, 'ReferencedDomainName'),(1, 'cchReferencedDomainName'),(1, 'peUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupAccountNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PSID,POINTER(UInt32),POINTER(Char),POINTER(UInt32),POINTER(win32more.Security.SID_NAME_USE), use_last_error=True)(("LookupAccountNameW", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpAccountName'),(1, 'Sid'),(1, 'cbSid'),(1, 'ReferencedDomainName'),(1, 'cchReferencedDomainName'),(1, 'peUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupAccountName():
    return win32more.Security.LookupAccountNameW
def _define_LookupPrivilegeValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Foundation.LUID_head), use_last_error=True)(("LookupPrivilegeValueA", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpName'),(1, 'lpLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.LUID_head), use_last_error=True)(("LookupPrivilegeValueW", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpName'),(1, 'lpLuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeValue():
    return win32more.Security.LookupPrivilegeValueW
def _define_LookupPrivilegeNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.LUID_head),POINTER(Byte),POINTER(UInt32), use_last_error=True)(("LookupPrivilegeNameA", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpLuid'),(1, 'lpName'),(1, 'cchName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.LUID_head),POINTER(Char),POINTER(UInt32), use_last_error=True)(("LookupPrivilegeNameW", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpLuid'),(1, 'lpName'),(1, 'cchName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeName():
    return win32more.Security.LookupPrivilegeNameW
def _define_LookupPrivilegeDisplayNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Byte),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("LookupPrivilegeDisplayNameA", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpName'),(1, 'lpDisplayName'),(1, 'cchDisplayName'),(1, 'lpLanguageId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeDisplayNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("LookupPrivilegeDisplayNameW", windll["ADVAPI32"]), ((1, 'lpSystemName'),(1, 'lpName'),(1, 'lpDisplayName'),(1, 'cchDisplayName'),(1, 'lpLanguageId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupPrivilegeDisplayName():
    return win32more.Security.LookupPrivilegeDisplayNameW
def _define_LogonUserA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Security.LOGON32_LOGON,win32more.Security.LOGON32_PROVIDER,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("LogonUserA", windll["ADVAPI32"]), ((1, 'lpszUsername'),(1, 'lpszDomain'),(1, 'lpszPassword'),(1, 'dwLogonType'),(1, 'dwLogonProvider'),(1, 'phToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogonUserW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Security.LOGON32_LOGON,win32more.Security.LOGON32_PROVIDER,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("LogonUserW", windll["ADVAPI32"]), ((1, 'lpszUsername'),(1, 'lpszDomain'),(1, 'lpszPassword'),(1, 'dwLogonType'),(1, 'dwLogonProvider'),(1, 'phToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogonUser():
    return win32more.Security.LogonUserW
def _define_LogonUserExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Security.LOGON32_LOGON,win32more.Security.LOGON32_PROVIDER,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.PSID),POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Security.QUOTA_LIMITS_head), use_last_error=True)(("LogonUserExA", windll["ADVAPI32"]), ((1, 'lpszUsername'),(1, 'lpszDomain'),(1, 'lpszPassword'),(1, 'dwLogonType'),(1, 'dwLogonProvider'),(1, 'phToken'),(1, 'ppLogonSid'),(1, 'ppProfileBuffer'),(1, 'pdwProfileLength'),(1, 'pQuotaLimits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogonUserExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Security.LOGON32_LOGON,win32more.Security.LOGON32_PROVIDER,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.Foundation.PSID),POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Security.QUOTA_LIMITS_head), use_last_error=True)(("LogonUserExW", windll["ADVAPI32"]), ((1, 'lpszUsername'),(1, 'lpszDomain'),(1, 'lpszPassword'),(1, 'dwLogonType'),(1, 'dwLogonProvider'),(1, 'phToken'),(1, 'ppLogonSid'),(1, 'ppProfileBuffer'),(1, 'pdwProfileLength'),(1, 'pQuotaLimits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogonUserEx():
    return win32more.Security.LogonUserExW
def _define_RtlConvertSidToUnicodeString():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.UNICODE_STRING_head),win32more.Foundation.PSID,win32more.Foundation.BOOLEAN, use_last_error=False)(("RtlConvertSidToUnicodeString", windll["ntdll"]), ((1, 'UnicodeString'),(1, 'Sid'),(1, 'AllocateDestinationString'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CVT_SECONDS",
    "TOKEN_PRIVILEGES_ATTRIBUTES",
    "SE_PRIVILEGE_ENABLED",
    "SE_PRIVILEGE_ENABLED_BY_DEFAULT",
    "SE_PRIVILEGE_REMOVED",
    "SE_PRIVILEGE_USED_FOR_ACCESS",
    "LOGON32_PROVIDER",
    "LOGON32_PROVIDER_DEFAULT",
    "LOGON32_PROVIDER_WINNT50",
    "LOGON32_PROVIDER_WINNT40",
    "CREATE_RESTRICTED_TOKEN_FLAGS",
    "DISABLE_MAX_PRIVILEGE",
    "SANDBOX_INERT",
    "LUA_TOKEN",
    "WRITE_RESTRICTED",
    "LOGON32_LOGON",
    "LOGON32_LOGON_BATCH",
    "LOGON32_LOGON_INTERACTIVE",
    "LOGON32_LOGON_NETWORK",
    "LOGON32_LOGON_NETWORK_CLEARTEXT",
    "LOGON32_LOGON_NEW_CREDENTIALS",
    "LOGON32_LOGON_SERVICE",
    "LOGON32_LOGON_UNLOCK",
    "ACE_FLAGS",
    "CONTAINER_INHERIT_ACE",
    "FAILED_ACCESS_ACE_FLAG",
    "INHERIT_ONLY_ACE",
    "INHERITED_ACE",
    "NO_PROPAGATE_INHERIT_ACE",
    "OBJECT_INHERIT_ACE",
    "SUCCESSFUL_ACCESS_ACE_FLAG",
    "SUB_CONTAINERS_AND_OBJECTS_INHERIT",
    "SUB_CONTAINERS_ONLY_INHERIT",
    "SUB_OBJECTS_ONLY_INHERIT",
    "INHERIT_NO_PROPAGATE",
    "INHERIT_ONLY",
    "NO_INHERITANCE",
    "INHERIT_ONLY_ACE_",
    "OBJECT_SECURITY_INFORMATION",
    "ATTRIBUTE_SECURITY_INFORMATION",
    "BACKUP_SECURITY_INFORMATION",
    "DACL_SECURITY_INFORMATION",
    "GROUP_SECURITY_INFORMATION",
    "LABEL_SECURITY_INFORMATION",
    "OWNER_SECURITY_INFORMATION",
    "PROTECTED_DACL_SECURITY_INFORMATION",
    "PROTECTED_SACL_SECURITY_INFORMATION",
    "SACL_SECURITY_INFORMATION",
    "SCOPE_SECURITY_INFORMATION",
    "UNPROTECTED_DACL_SECURITY_INFORMATION",
    "UNPROTECTED_SACL_SECURITY_INFORMATION",
    "SECURITY_AUTO_INHERIT_FLAGS",
    "SEF_AVOID_OWNER_CHECK",
    "SEF_AVOID_OWNER_RESTRICTION",
    "SEF_AVOID_PRIVILEGE_CHECK",
    "SEF_DACL_AUTO_INHERIT",
    "SEF_DEFAULT_DESCRIPTOR_FOR_OBJECT",
    "SEF_DEFAULT_GROUP_FROM_PARENT",
    "SEF_DEFAULT_OWNER_FROM_PARENT",
    "SEF_MACL_NO_EXECUTE_UP",
    "SEF_MACL_NO_READ_UP",
    "SEF_MACL_NO_WRITE_UP",
    "SEF_SACL_AUTO_INHERIT",
    "ACE_REVISION",
    "ACL_REVISION",
    "ACL_REVISION_DS",
    "TOKEN_MANDATORY_POLICY_ID",
    "TOKEN_MANDATORY_POLICY_OFF",
    "TOKEN_MANDATORY_POLICY_NO_WRITE_UP",
    "TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN",
    "TOKEN_MANDATORY_POLICY_VALID_MASK",
    "SYSTEM_AUDIT_OBJECT_ACE_FLAGS",
    "ACE_OBJECT_TYPE_PRESENT",
    "ACE_INHERITED_OBJECT_TYPE_PRESENT",
    "CLAIM_SECURITY_ATTRIBUTE_FLAGS",
    "CLAIM_SECURITY_ATTRIBUTE_NON_INHERITABLE",
    "CLAIM_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE",
    "CLAIM_SECURITY_ATTRIBUTE_USE_FOR_DENY_ONLY",
    "CLAIM_SECURITY_ATTRIBUTE_DISABLED_BY_DEFAULT",
    "CLAIM_SECURITY_ATTRIBUTE_DISABLED",
    "CLAIM_SECURITY_ATTRIBUTE_MANDATORY",
    "CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_INT64",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_UINT64",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_STRING",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_FQBN",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_SID",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_BOOLEAN",
    "PLSA_AP_CALL_PACKAGE_UNTRUSTED",
    "SEC_THREAD_START",
    "TOKEN_ACCESS_MASK",
    "TOKEN_DELETE",
    "TOKEN_READ_CONTROL",
    "TOKEN_WRITE_DAC",
    "TOKEN_WRITE_OWNER",
    "TOKEN_ACCESS_SYSTEM_SECURITY",
    "TOKEN_ASSIGN_PRIMARY",
    "TOKEN_DUPLICATE",
    "TOKEN_IMPERSONATE",
    "TOKEN_QUERY",
    "TOKEN_QUERY_SOURCE",
    "TOKEN_ADJUST_PRIVILEGES",
    "TOKEN_ADJUST_GROUPS",
    "TOKEN_ADJUST_DEFAULT",
    "TOKEN_ADJUST_SESSIONID",
    "TOKEN_ALL_ACCESS",
    "HDIAGNOSTIC_DATA_QUERY_SESSION",
    "HDIAGNOSTIC_REPORT",
    "HDIAGNOSTIC_EVENT_TAG_DESCRIPTION",
    "HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION",
    "HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION",
    "HDIAGNOSTIC_RECORD",
    "NCRYPT_DESCRIPTOR_HANDLE",
    "NCRYPT_STREAM_HANDLE",
    "SAFER_LEVEL_HANDLE",
    "SC_HANDLE",
    "SECURITY_ATTRIBUTES",
    "ENUM_PERIOD",
    "ENUM_PERIOD_INVALID",
    "ENUM_PERIOD_SECONDS",
    "ENUM_PERIOD_MINUTES",
    "ENUM_PERIOD_HOURS",
    "ENUM_PERIOD_DAYS",
    "ENUM_PERIOD_WEEKS",
    "ENUM_PERIOD_MONTHS",
    "ENUM_PERIOD_YEARS",
    "LLFILETIME",
    "GENERIC_MAPPING",
    "LUID_AND_ATTRIBUTES",
    "SID_IDENTIFIER_AUTHORITY",
    "SID",
    "SE_SID",
    "SID_NAME_USE",
    "SID_NAME_USE_SidTypeUser",
    "SID_NAME_USE_SidTypeGroup",
    "SID_NAME_USE_SidTypeDomain",
    "SID_NAME_USE_SidTypeAlias",
    "SID_NAME_USE_SidTypeWellKnownGroup",
    "SID_NAME_USE_SidTypeDeletedAccount",
    "SID_NAME_USE_SidTypeInvalid",
    "SID_NAME_USE_SidTypeUnknown",
    "SID_NAME_USE_SidTypeComputer",
    "SID_NAME_USE_SidTypeLabel",
    "SID_NAME_USE_SidTypeLogonSession",
    "SID_AND_ATTRIBUTES",
    "SID_AND_ATTRIBUTES_HASH",
    "WELL_KNOWN_SID_TYPE",
    "WELL_KNOWN_SID_TYPE_WinNullSid",
    "WELL_KNOWN_SID_TYPE_WinWorldSid",
    "WELL_KNOWN_SID_TYPE_WinLocalSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorGroupSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerServerSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorGroupServerSid",
    "WELL_KNOWN_SID_TYPE_WinNtAuthoritySid",
    "WELL_KNOWN_SID_TYPE_WinDialupSid",
    "WELL_KNOWN_SID_TYPE_WinNetworkSid",
    "WELL_KNOWN_SID_TYPE_WinBatchSid",
    "WELL_KNOWN_SID_TYPE_WinInteractiveSid",
    "WELL_KNOWN_SID_TYPE_WinServiceSid",
    "WELL_KNOWN_SID_TYPE_WinAnonymousSid",
    "WELL_KNOWN_SID_TYPE_WinProxySid",
    "WELL_KNOWN_SID_TYPE_WinEnterpriseControllersSid",
    "WELL_KNOWN_SID_TYPE_WinSelfSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticatedUserSid",
    "WELL_KNOWN_SID_TYPE_WinRestrictedCodeSid",
    "WELL_KNOWN_SID_TYPE_WinTerminalServerSid",
    "WELL_KNOWN_SID_TYPE_WinRemoteLogonIdSid",
    "WELL_KNOWN_SID_TYPE_WinLogonIdsSid",
    "WELL_KNOWN_SID_TYPE_WinLocalSystemSid",
    "WELL_KNOWN_SID_TYPE_WinLocalServiceSid",
    "WELL_KNOWN_SID_TYPE_WinNetworkServiceSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDomainSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAdministratorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinGuestsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPowerUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAccountOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinSystemOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPrintOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinBackupOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinReplicatorSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPreWindows2000CompatibleAccessSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRemoteDesktopUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinNetworkConfigurationOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountAdministratorSid",
    "WELL_KNOWN_SID_TYPE_WinAccountGuestSid",
    "WELL_KNOWN_SID_TYPE_WinAccountKrbtgtSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainUsersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainGuestsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountComputersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountControllersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountCertAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountSchemaAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountEnterpriseAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountPolicyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountRasAndIasServersSid",
    "WELL_KNOWN_SID_TYPE_WinNTLMAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinDigestAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinSChannelAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinThisOrganizationSid",
    "WELL_KNOWN_SID_TYPE_WinOtherOrganizationSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinIncomingForestTrustBuildersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPerfMonitoringUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPerfLoggingUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAuthorizationAccessSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinTerminalServerLicenseServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDCOMUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinIUsersSid",
    "WELL_KNOWN_SID_TYPE_WinIUserSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinCryptoOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinUntrustedLabelSid",
    "WELL_KNOWN_SID_TYPE_WinLowLabelSid",
    "WELL_KNOWN_SID_TYPE_WinMediumLabelSid",
    "WELL_KNOWN_SID_TYPE_WinHighLabelSid",
    "WELL_KNOWN_SID_TYPE_WinSystemLabelSid",
    "WELL_KNOWN_SID_TYPE_WinWriteRestrictedCodeSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerRightsSid",
    "WELL_KNOWN_SID_TYPE_WinCacheablePrincipalsGroupSid",
    "WELL_KNOWN_SID_TYPE_WinNonCacheablePrincipalsGroupSid",
    "WELL_KNOWN_SID_TYPE_WinEnterpriseReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinEventLogReadersGroup",
    "WELL_KNOWN_SID_TYPE_WinNewEnterpriseReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinCertSvcDComAccessGroup",
    "WELL_KNOWN_SID_TYPE_WinMediumPlusLabelSid",
    "WELL_KNOWN_SID_TYPE_WinLocalLogonSid",
    "WELL_KNOWN_SID_TYPE_WinConsoleLogonSid",
    "WELL_KNOWN_SID_TYPE_WinThisOrganizationCertificateSid",
    "WELL_KNOWN_SID_TYPE_WinApplicationPackageAuthoritySid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAnyPackageSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientServerSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityPrivateNetworkClientServerSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityPicturesLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityVideosLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityMusicLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityDocumentsLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilitySharedUserCertificatesSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityEnterpriseAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityRemovableStorageSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSRemoteAccessServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSEndpointServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSManagementServersSid",
    "WELL_KNOWN_SID_TYPE_WinUserModeDriversSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinHyperVAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountCloneableControllersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAccessControlAssistanceOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRemoteManagementUsersSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationAuthorityAssertedSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationServiceAssertedSid",
    "WELL_KNOWN_SID_TYPE_WinLocalAccountSid",
    "WELL_KNOWN_SID_TYPE_WinLocalAccountAndAdministratorSid",
    "WELL_KNOWN_SID_TYPE_WinAccountProtectedUsersSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityAppointmentsSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityContactsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDefaultSystemManagedSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDefaultSystemManagedGroupSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinStorageReplicaAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountKeyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountEnterpriseKeyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyTrustSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyMFASid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyAttestationSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationFreshKeyAuthSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDeviceOwnersSid",
    "ACL",
    "ACE_HEADER",
    "ACCESS_ALLOWED_ACE",
    "ACCESS_DENIED_ACE",
    "SYSTEM_AUDIT_ACE",
    "SYSTEM_ALARM_ACE",
    "SYSTEM_RESOURCE_ATTRIBUTE_ACE",
    "SYSTEM_SCOPED_POLICY_ID_ACE",
    "SYSTEM_MANDATORY_LABEL_ACE",
    "SYSTEM_PROCESS_TRUST_LABEL_ACE",
    "SYSTEM_ACCESS_FILTER_ACE",
    "ACCESS_ALLOWED_OBJECT_ACE",
    "ACCESS_DENIED_OBJECT_ACE",
    "SYSTEM_AUDIT_OBJECT_ACE",
    "SYSTEM_ALARM_OBJECT_ACE",
    "ACCESS_ALLOWED_CALLBACK_ACE",
    "ACCESS_DENIED_CALLBACK_ACE",
    "SYSTEM_AUDIT_CALLBACK_ACE",
    "SYSTEM_ALARM_CALLBACK_ACE",
    "ACCESS_ALLOWED_CALLBACK_OBJECT_ACE",
    "ACCESS_DENIED_CALLBACK_OBJECT_ACE",
    "SYSTEM_AUDIT_CALLBACK_OBJECT_ACE",
    "SYSTEM_ALARM_CALLBACK_OBJECT_ACE",
    "ACL_INFORMATION_CLASS",
    "ACL_INFORMATION_CLASS_AclRevisionInformation",
    "ACL_INFORMATION_CLASS_AclSizeInformation",
    "ACL_REVISION_INFORMATION",
    "ACL_SIZE_INFORMATION",
    "SECURITY_DESCRIPTOR",
    "OBJECT_TYPE_LIST",
    "AUDIT_EVENT_TYPE",
    "AUDIT_EVENT_TYPE_AuditEventObjectAccess",
    "AUDIT_EVENT_TYPE_AuditEventDirectoryServiceAccess",
    "PRIVILEGE_SET",
    "ACCESS_REASONS",
    "SE_SECURITY_DESCRIPTOR",
    "SE_ACCESS_REQUEST",
    "SE_ACCESS_REPLY",
    "SECURITY_IMPERSONATION_LEVEL",
    "SECURITY_IMPERSONATION_LEVEL_SecurityAnonymous",
    "SECURITY_IMPERSONATION_LEVEL_SecurityIdentification",
    "SECURITY_IMPERSONATION_LEVEL_SecurityImpersonation",
    "SECURITY_IMPERSONATION_LEVEL_SecurityDelegation",
    "TOKEN_TYPE",
    "TOKEN_TYPE_TokenPrimary",
    "TOKEN_TYPE_TokenImpersonation",
    "TOKEN_ELEVATION_TYPE",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeDefault",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeFull",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeLimited",
    "TOKEN_INFORMATION_CLASS",
    "TOKEN_INFORMATION_CLASS_TokenUser",
    "TOKEN_INFORMATION_CLASS_TokenGroups",
    "TOKEN_INFORMATION_CLASS_TokenPrivileges",
    "TOKEN_INFORMATION_CLASS_TokenOwner",
    "TOKEN_INFORMATION_CLASS_TokenPrimaryGroup",
    "TOKEN_INFORMATION_CLASS_TokenDefaultDacl",
    "TOKEN_INFORMATION_CLASS_TokenSource",
    "TOKEN_INFORMATION_CLASS_TokenType",
    "TOKEN_INFORMATION_CLASS_TokenImpersonationLevel",
    "TOKEN_INFORMATION_CLASS_TokenStatistics",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedSids",
    "TOKEN_INFORMATION_CLASS_TokenSessionId",
    "TOKEN_INFORMATION_CLASS_TokenGroupsAndPrivileges",
    "TOKEN_INFORMATION_CLASS_TokenSessionReference",
    "TOKEN_INFORMATION_CLASS_TokenSandBoxInert",
    "TOKEN_INFORMATION_CLASS_TokenAuditPolicy",
    "TOKEN_INFORMATION_CLASS_TokenOrigin",
    "TOKEN_INFORMATION_CLASS_TokenElevationType",
    "TOKEN_INFORMATION_CLASS_TokenLinkedToken",
    "TOKEN_INFORMATION_CLASS_TokenElevation",
    "TOKEN_INFORMATION_CLASS_TokenHasRestrictions",
    "TOKEN_INFORMATION_CLASS_TokenAccessInformation",
    "TOKEN_INFORMATION_CLASS_TokenVirtualizationAllowed",
    "TOKEN_INFORMATION_CLASS_TokenVirtualizationEnabled",
    "TOKEN_INFORMATION_CLASS_TokenIntegrityLevel",
    "TOKEN_INFORMATION_CLASS_TokenUIAccess",
    "TOKEN_INFORMATION_CLASS_TokenMandatoryPolicy",
    "TOKEN_INFORMATION_CLASS_TokenLogonSid",
    "TOKEN_INFORMATION_CLASS_TokenIsAppContainer",
    "TOKEN_INFORMATION_CLASS_TokenCapabilities",
    "TOKEN_INFORMATION_CLASS_TokenAppContainerSid",
    "TOKEN_INFORMATION_CLASS_TokenAppContainerNumber",
    "TOKEN_INFORMATION_CLASS_TokenUserClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenDeviceClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedUserClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenDeviceGroups",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceGroups",
    "TOKEN_INFORMATION_CLASS_TokenSecurityAttributes",
    "TOKEN_INFORMATION_CLASS_TokenIsRestricted",
    "TOKEN_INFORMATION_CLASS_TokenProcessTrustLevel",
    "TOKEN_INFORMATION_CLASS_TokenPrivateNameSpace",
    "TOKEN_INFORMATION_CLASS_TokenSingletonAttributes",
    "TOKEN_INFORMATION_CLASS_TokenBnoIsolation",
    "TOKEN_INFORMATION_CLASS_TokenChildProcessFlags",
    "TOKEN_INFORMATION_CLASS_TokenIsLessPrivilegedAppContainer",
    "TOKEN_INFORMATION_CLASS_TokenIsSandboxed",
    "TOKEN_INFORMATION_CLASS_MaxTokenInfoClass",
    "TOKEN_USER",
    "TOKEN_GROUPS",
    "TOKEN_PRIVILEGES",
    "TOKEN_OWNER",
    "TOKEN_PRIMARY_GROUP",
    "TOKEN_DEFAULT_DACL",
    "TOKEN_USER_CLAIMS",
    "TOKEN_DEVICE_CLAIMS",
    "TOKEN_GROUPS_AND_PRIVILEGES",
    "TOKEN_LINKED_TOKEN",
    "TOKEN_ELEVATION",
    "TOKEN_MANDATORY_LABEL",
    "TOKEN_MANDATORY_POLICY",
    "TOKEN_ACCESS_INFORMATION",
    "TOKEN_AUDIT_POLICY",
    "TOKEN_SOURCE",
    "TOKEN_STATISTICS",
    "TOKEN_CONTROL",
    "TOKEN_ORIGIN",
    "MANDATORY_LEVEL",
    "MANDATORY_LEVEL_MandatoryLevelUntrusted",
    "MANDATORY_LEVEL_MandatoryLevelLow",
    "MANDATORY_LEVEL_MandatoryLevelMedium",
    "MANDATORY_LEVEL_MandatoryLevelHigh",
    "MANDATORY_LEVEL_MandatoryLevelSystem",
    "MANDATORY_LEVEL_MandatoryLevelSecureProcess",
    "MANDATORY_LEVEL_MandatoryLevelCount",
    "TOKEN_APPCONTAINER_INFORMATION",
    "CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE",
    "CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE",
    "CLAIM_SECURITY_ATTRIBUTE_V1",
    "CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1",
    "CLAIM_SECURITY_ATTRIBUTES_INFORMATION",
    "SECURITY_QUALITY_OF_SERVICE",
    "SE_IMPERSONATION_STATE",
    "SECURITY_CAPABILITIES",
    "QUOTA_LIMITS",
    "AccessCheck",
    "AccessCheckAndAuditAlarmW",
    "AccessCheckAndAuditAlarm",
    "AccessCheckByType",
    "AccessCheckByTypeResultList",
    "AccessCheckByTypeAndAuditAlarmW",
    "AccessCheckByTypeAndAuditAlarm",
    "AccessCheckByTypeResultListAndAuditAlarmW",
    "AccessCheckByTypeResultListAndAuditAlarm",
    "AccessCheckByTypeResultListAndAuditAlarmByHandleW",
    "AccessCheckByTypeResultListAndAuditAlarmByHandle",
    "AddAccessAllowedAce",
    "AddAccessAllowedAceEx",
    "AddAccessAllowedObjectAce",
    "AddAccessDeniedAce",
    "AddAccessDeniedAceEx",
    "AddAccessDeniedObjectAce",
    "AddAce",
    "AddAuditAccessAce",
    "AddAuditAccessAceEx",
    "AddAuditAccessObjectAce",
    "AddMandatoryAce",
    "AddResourceAttributeAce",
    "AddScopedPolicyIDAce",
    "AdjustTokenGroups",
    "AdjustTokenPrivileges",
    "AllocateAndInitializeSid",
    "AllocateLocallyUniqueId",
    "AreAllAccessesGranted",
    "AreAnyAccessesGranted",
    "CheckTokenMembership",
    "CheckTokenCapability",
    "GetAppContainerAce",
    "CheckTokenMembershipEx",
    "ConvertToAutoInheritPrivateObjectSecurity",
    "CopySid",
    "CreatePrivateObjectSecurity",
    "CreatePrivateObjectSecurityEx",
    "CreatePrivateObjectSecurityWithMultipleInheritance",
    "CreateRestrictedToken",
    "CreateWellKnownSid",
    "EqualDomainSid",
    "DeleteAce",
    "DestroyPrivateObjectSecurity",
    "DuplicateToken",
    "DuplicateTokenEx",
    "EqualPrefixSid",
    "EqualSid",
    "FindFirstFreeAce",
    "FreeSid",
    "GetAce",
    "GetAclInformation",
    "GetFileSecurityW",
    "GetFileSecurity",
    "GetKernelObjectSecurity",
    "GetLengthSid",
    "GetPrivateObjectSecurity",
    "GetSecurityDescriptorControl",
    "GetSecurityDescriptorDacl",
    "GetSecurityDescriptorGroup",
    "GetSecurityDescriptorLength",
    "GetSecurityDescriptorOwner",
    "GetSecurityDescriptorRMControl",
    "GetSecurityDescriptorSacl",
    "GetSidIdentifierAuthority",
    "GetSidLengthRequired",
    "GetSidSubAuthority",
    "GetSidSubAuthorityCount",
    "GetTokenInformation",
    "GetWindowsAccountDomainSid",
    "ImpersonateAnonymousToken",
    "ImpersonateLoggedOnUser",
    "ImpersonateSelf",
    "InitializeAcl",
    "InitializeSecurityDescriptor",
    "InitializeSid",
    "IsTokenRestricted",
    "IsValidAcl",
    "IsValidSecurityDescriptor",
    "IsValidSid",
    "IsWellKnownSid",
    "MakeAbsoluteSD",
    "MakeSelfRelativeSD",
    "MapGenericMask",
    "ObjectCloseAuditAlarmW",
    "ObjectCloseAuditAlarm",
    "ObjectDeleteAuditAlarmW",
    "ObjectDeleteAuditAlarm",
    "ObjectOpenAuditAlarmW",
    "ObjectOpenAuditAlarm",
    "ObjectPrivilegeAuditAlarmW",
    "ObjectPrivilegeAuditAlarm",
    "PrivilegeCheck",
    "PrivilegedServiceAuditAlarmW",
    "PrivilegedServiceAuditAlarm",
    "QuerySecurityAccessMask",
    "RevertToSelf",
    "SetAclInformation",
    "SetFileSecurityW",
    "SetFileSecurity",
    "SetKernelObjectSecurity",
    "SetPrivateObjectSecurity",
    "SetPrivateObjectSecurityEx",
    "SetSecurityAccessMask",
    "SetSecurityDescriptorControl",
    "SetSecurityDescriptorDacl",
    "SetSecurityDescriptorGroup",
    "SetSecurityDescriptorOwner",
    "SetSecurityDescriptorRMControl",
    "SetSecurityDescriptorSacl",
    "SetTokenInformation",
    "SetCachedSigningLevel",
    "GetCachedSigningLevel",
    "DeriveCapabilitySidsFromName",
    "RtlNormalizeSecurityDescriptor",
    "SetUserObjectSecurity",
    "GetUserObjectSecurity",
    "AccessCheckAndAuditAlarmA",
    "AccessCheckByTypeAndAuditAlarmA",
    "AccessCheckByTypeResultListAndAuditAlarmA",
    "AccessCheckByTypeResultListAndAuditAlarmByHandleA",
    "ObjectOpenAuditAlarmA",
    "ObjectPrivilegeAuditAlarmA",
    "ObjectCloseAuditAlarmA",
    "ObjectDeleteAuditAlarmA",
    "PrivilegedServiceAuditAlarmA",
    "AddConditionalAce",
    "SetFileSecurityA",
    "GetFileSecurityA",
    "LookupAccountSidA",
    "LookupAccountSidW",
    "LookupAccountSid",
    "LookupAccountNameA",
    "LookupAccountNameW",
    "LookupAccountName",
    "LookupPrivilegeValueA",
    "LookupPrivilegeValueW",
    "LookupPrivilegeValue",
    "LookupPrivilegeNameA",
    "LookupPrivilegeNameW",
    "LookupPrivilegeName",
    "LookupPrivilegeDisplayNameA",
    "LookupPrivilegeDisplayNameW",
    "LookupPrivilegeDisplayName",
    "LogonUserA",
    "LogonUserW",
    "LogonUser",
    "LogonUserExA",
    "LogonUserExW",
    "LogonUserEx",
    "RtlConvertSidToUnicodeString",
]
