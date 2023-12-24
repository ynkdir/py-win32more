from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
class ACCESS_ALLOWED_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_ALLOWED_CALLBACK_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_ALLOWED_CALLBACK_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_ALLOWED_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_DENIED_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_DENIED_CALLBACK_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_DENIED_CALLBACK_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_DENIED_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_REASONS(EasyCastStructure):
    Data: UInt32 * 32
ACE_FLAGS = UInt32
CONTAINER_INHERIT_ACE: win32more.Windows.Win32.Security.ACE_FLAGS = 2
FAILED_ACCESS_ACE_FLAG: win32more.Windows.Win32.Security.ACE_FLAGS = 128
INHERIT_ONLY_ACE: win32more.Windows.Win32.Security.ACE_FLAGS = 8
INHERITED_ACE: win32more.Windows.Win32.Security.ACE_FLAGS = 16
NO_PROPAGATE_INHERIT_ACE: win32more.Windows.Win32.Security.ACE_FLAGS = 4
OBJECT_INHERIT_ACE: win32more.Windows.Win32.Security.ACE_FLAGS = 1
SUCCESSFUL_ACCESS_ACE_FLAG: win32more.Windows.Win32.Security.ACE_FLAGS = 64
SUB_CONTAINERS_AND_OBJECTS_INHERIT: win32more.Windows.Win32.Security.ACE_FLAGS = 3
SUB_CONTAINERS_ONLY_INHERIT: win32more.Windows.Win32.Security.ACE_FLAGS = 2
SUB_OBJECTS_ONLY_INHERIT: win32more.Windows.Win32.Security.ACE_FLAGS = 1
INHERIT_NO_PROPAGATE: win32more.Windows.Win32.Security.ACE_FLAGS = 4
INHERIT_ONLY: win32more.Windows.Win32.Security.ACE_FLAGS = 8
NO_INHERITANCE: win32more.Windows.Win32.Security.ACE_FLAGS = 0
class ACE_HEADER(EasyCastStructure):
    AceType: Byte
    AceFlags: Byte
    AceSize: UInt16
ACE_REVISION = UInt32
ACL_REVISION: win32more.Windows.Win32.Security.ACE_REVISION = 2
ACL_REVISION_DS: win32more.Windows.Win32.Security.ACE_REVISION = 4
class ACL(EasyCastStructure):
    AclRevision: Byte
    Sbz1: Byte
    AclSize: UInt16
    AceCount: UInt16
    Sbz2: UInt16
ACL_INFORMATION_CLASS = Int32
ACL_INFORMATION_CLASS_AclRevisionInformation: win32more.Windows.Win32.Security.ACL_INFORMATION_CLASS = 1
ACL_INFORMATION_CLASS_AclSizeInformation: win32more.Windows.Win32.Security.ACL_INFORMATION_CLASS = 2
class ACL_REVISION_INFORMATION(EasyCastStructure):
    AclRevision: UInt32
class ACL_SIZE_INFORMATION(EasyCastStructure):
    AceCount: UInt32
    AclBytesInUse: UInt32
    AclBytesFree: UInt32
AUDIT_EVENT_TYPE = Int32
AUDIT_EVENT_TYPE_AuditEventObjectAccess: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE = 0
AUDIT_EVENT_TYPE_AuditEventDirectoryServiceAccess: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE = 1
SECURITY_DYNAMIC_TRACKING: win32more.Windows.Win32.Foundation.BOOLEAN = 1
SECURITY_STATIC_TRACKING: win32more.Windows.Win32.Foundation.BOOLEAN = 0
SECURITY_NULL_SID_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 0))
SECURITY_WORLD_SID_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 1))
SECURITY_LOCAL_SID_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 2))
SECURITY_CREATOR_SID_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 3))
SECURITY_NON_UNIQUE_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 4))
SECURITY_NT_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 5))
SECURITY_RESOURCE_MANAGER_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 9))
SECURITY_APP_PACKAGE_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 15))
SECURITY_MANDATORY_LABEL_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 16))
SECURITY_SCOPED_POLICY_ID_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 17))
SECURITY_AUTHENTICATION_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 18))
SECURITY_PROCESS_TRUST_AUTHORITY: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY = ConstantLazyLoader((0, 0, 0, 0, 0, 19))
SE_CREATE_TOKEN_NAME: String = 'SeCreateTokenPrivilege'
SE_ASSIGNPRIMARYTOKEN_NAME: String = 'SeAssignPrimaryTokenPrivilege'
SE_LOCK_MEMORY_NAME: String = 'SeLockMemoryPrivilege'
SE_INCREASE_QUOTA_NAME: String = 'SeIncreaseQuotaPrivilege'
SE_UNSOLICITED_INPUT_NAME: String = 'SeUnsolicitedInputPrivilege'
SE_MACHINE_ACCOUNT_NAME: String = 'SeMachineAccountPrivilege'
SE_TCB_NAME: String = 'SeTcbPrivilege'
SE_SECURITY_NAME: String = 'SeSecurityPrivilege'
SE_TAKE_OWNERSHIP_NAME: String = 'SeTakeOwnershipPrivilege'
SE_LOAD_DRIVER_NAME: String = 'SeLoadDriverPrivilege'
SE_SYSTEM_PROFILE_NAME: String = 'SeSystemProfilePrivilege'
SE_SYSTEMTIME_NAME: String = 'SeSystemtimePrivilege'
SE_PROF_SINGLE_PROCESS_NAME: String = 'SeProfileSingleProcessPrivilege'
SE_INC_BASE_PRIORITY_NAME: String = 'SeIncreaseBasePriorityPrivilege'
SE_CREATE_PAGEFILE_NAME: String = 'SeCreatePagefilePrivilege'
SE_CREATE_PERMANENT_NAME: String = 'SeCreatePermanentPrivilege'
SE_BACKUP_NAME: String = 'SeBackupPrivilege'
SE_RESTORE_NAME: String = 'SeRestorePrivilege'
SE_SHUTDOWN_NAME: String = 'SeShutdownPrivilege'
SE_DEBUG_NAME: String = 'SeDebugPrivilege'
SE_AUDIT_NAME: String = 'SeAuditPrivilege'
SE_SYSTEM_ENVIRONMENT_NAME: String = 'SeSystemEnvironmentPrivilege'
SE_CHANGE_NOTIFY_NAME: String = 'SeChangeNotifyPrivilege'
SE_REMOTE_SHUTDOWN_NAME: String = 'SeRemoteShutdownPrivilege'
SE_UNDOCK_NAME: String = 'SeUndockPrivilege'
SE_SYNC_AGENT_NAME: String = 'SeSyncAgentPrivilege'
SE_ENABLE_DELEGATION_NAME: String = 'SeEnableDelegationPrivilege'
SE_MANAGE_VOLUME_NAME: String = 'SeManageVolumePrivilege'
SE_IMPERSONATE_NAME: String = 'SeImpersonatePrivilege'
SE_CREATE_GLOBAL_NAME: String = 'SeCreateGlobalPrivilege'
SE_TRUSTED_CREDMAN_ACCESS_NAME: String = 'SeTrustedCredManAccessPrivilege'
SE_RELABEL_NAME: String = 'SeRelabelPrivilege'
SE_INC_WORKING_SET_NAME: String = 'SeIncreaseWorkingSetPrivilege'
SE_TIME_ZONE_NAME: String = 'SeTimeZonePrivilege'
SE_CREATE_SYMBOLIC_LINK_NAME: String = 'SeCreateSymbolicLinkPrivilege'
SE_DELEGATE_SESSION_USER_IMPERSONATE_NAME: String = 'SeDelegateSessionUserImpersonatePrivilege'
wszCERTENROLLSHAREPATH: String = 'CertSrv\\CertEnroll'
cwcHRESULTSTRING: UInt32 = 40
szLBRACE: String = '{'
szRBRACE: String = '}'
wszLBRACE: String = '{'
wszRBRACE: String = '}'
szLPAREN: String = '('
szRPAREN: String = ')'
wszLPAREN: String = '('
wszRPAREN: String = ')'
CVT_SECONDS: UInt32 = 1
cwcFILENAMESUFFIXMAX: UInt32 = 20
wszFCSAPARM_SERVERDNSNAME: String = '%1'
wszFCSAPARM_SERVERSHORTNAME: String = '%2'
wszFCSAPARM_SANITIZEDCANAME: String = '%3'
wszFCSAPARM_CERTFILENAMESUFFIX: String = '%4'
wszFCSAPARM_DOMAINDN: String = '%5'
wszFCSAPARM_CONFIGDN: String = '%6'
wszFCSAPARM_SANITIZEDCANAMEHASH: String = '%7'
wszFCSAPARM_CRLFILENAMESUFFIX: String = '%8'
wszFCSAPARM_CRLDELTAFILENAMESUFFIX: String = '%9'
wszFCSAPARM_DSCRLATTRIBUTE: String = '%10'
wszFCSAPARM_DSCACERTATTRIBUTE: String = '%11'
wszFCSAPARM_DSUSERCERTATTRIBUTE: String = '%12'
wszFCSAPARM_DSKRACERTATTRIBUTE: String = '%13'
wszFCSAPARM_DSCROSSCERTPAIRATTRIBUTE: String = '%14'
@winfunctype('ADVAPI32.dll')
def AccessCheck(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), PrivilegeSet: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckAndAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, ObjectName: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByType(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), PrivilegeSet: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultList(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), PrivilegeSet: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), PrivilegeSetLength: POINTER(UInt32), GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeAndAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, ObjectName: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, ObjectName: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmByHandleW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, ObjectName: win32more.Windows.Win32.Foundation.PWSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedAceEx(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedObjectAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedAceEx(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedObjectAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, dwStartingAceIndex: UInt32, pAceList: VoidPtr, nAceListLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, dwAccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID, bAuditSuccess: win32more.Windows.Win32.Foundation.BOOL, bAuditFailure: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessAceEx(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, dwAccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID, bAuditSuccess: win32more.Windows.Win32.Foundation.BOOL, bAuditFailure: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessObjectAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Windows.Win32.Foundation.PSID, bAuditSuccess: win32more.Windows.Win32.Foundation.BOOL, bAuditFailure: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddMandatoryAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, MandatoryPolicy: UInt32, pLabelSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddResourceAttributeAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID, pAttributeInfo: POINTER(win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTES_INFORMATION), pReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddScopedPolicyIDAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AdjustTokenGroups(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, ResetToDefault: win32more.Windows.Win32.Foundation.BOOL, NewState: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS), BufferLength: UInt32, PreviousState: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS), ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AdjustTokenPrivileges(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, DisableAllPrivileges: win32more.Windows.Win32.Foundation.BOOL, NewState: POINTER(win32more.Windows.Win32.Security.TOKEN_PRIVILEGES), BufferLength: UInt32, PreviousState: POINTER(win32more.Windows.Win32.Security.TOKEN_PRIVILEGES), ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AllocateAndInitializeSid(pIdentifierAuthority: POINTER(win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY), nSubAuthorityCount: Byte, nSubAuthority0: UInt32, nSubAuthority1: UInt32, nSubAuthority2: UInt32, nSubAuthority3: UInt32, nSubAuthority4: UInt32, nSubAuthority5: UInt32, nSubAuthority6: UInt32, nSubAuthority7: UInt32, pSid: POINTER(win32more.Windows.Win32.Foundation.PSID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AllocateLocallyUniqueId(Luid: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AreAllAccessesGranted(GrantedAccess: UInt32, DesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AreAnyAccessesGranted(GrantedAccess: UInt32, DesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CheckTokenMembership(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, SidToCheck: win32more.Windows.Win32.Foundation.PSID, IsMember: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckTokenCapability(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, CapabilitySidToCheck: win32more.Windows.Win32.Foundation.PSID, HasCapability: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetAppContainerAce(Acl: POINTER(win32more.Windows.Win32.Security.ACL), StartingAceIndex: UInt32, AppContainerAce: POINTER(VoidPtr), AppContainerAceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckTokenMembershipEx(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, SidToCheck: win32more.Windows.Win32.Foundation.PSID, Flags: UInt32, IsMember: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertToAutoInheritPrivateObjectSecurity(ParentDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, CurrentSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, NewSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), ObjectType: POINTER(Guid), IsDirectoryObject: win32more.Windows.Win32.Foundation.BOOLEAN, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CopySid(nDestinationSidLength: UInt32, pDestinationSid: win32more.Windows.Win32.Foundation.PSID, pSourceSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurity(ParentDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), IsDirectoryObject: win32more.Windows.Win32.Foundation.BOOL, Token: win32more.Windows.Win32.Foundation.HANDLE, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurityEx(ParentDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), ObjectType: POINTER(Guid), IsContainerObject: win32more.Windows.Win32.Foundation.BOOL, AutoInheritFlags: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS, Token: win32more.Windows.Win32.Foundation.HANDLE, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurityWithMultipleInheritance(ParentDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), ObjectTypes: POINTER(POINTER(Guid)), GuidCount: UInt32, IsContainerObject: win32more.Windows.Win32.Foundation.BOOL, AutoInheritFlags: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS, Token: win32more.Windows.Win32.Foundation.HANDLE, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateRestrictedToken(ExistingTokenHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.Security.CREATE_RESTRICTED_TOKEN_FLAGS, DisableSidCount: UInt32, SidsToDisable: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES), DeletePrivilegeCount: UInt32, PrivilegesToDelete: POINTER(win32more.Windows.Win32.Security.LUID_AND_ATTRIBUTES), RestrictedSidCount: UInt32, SidsToRestrict: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES), NewTokenHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateWellKnownSid(WellKnownSidType: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE, DomainSid: win32more.Windows.Win32.Foundation.PSID, pSid: win32more.Windows.Win32.Foundation.PSID, cbSid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualDomainSid(pSid1: win32more.Windows.Win32.Foundation.PSID, pSid2: win32more.Windows.Win32.Foundation.PSID, pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DeleteAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceIndex: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DestroyPrivateObjectSecurity(ObjectDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateToken(ExistingTokenHandle: win32more.Windows.Win32.Foundation.HANDLE, ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL, DuplicateTokenHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateTokenEx(hExistingToken: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK, lpTokenAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL, TokenType: win32more.Windows.Win32.Security.TOKEN_TYPE, phNewToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualPrefixSid(pSid1: win32more.Windows.Win32.Foundation.PSID, pSid2: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualSid(pSid1: win32more.Windows.Win32.Foundation.PSID, pSid2: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FindFirstFreeAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), pAce: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FreeSid(pSid: win32more.Windows.Win32.Foundation.PSID) -> VoidPtr: ...
@winfunctype('ADVAPI32.dll')
def GetAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceIndex: UInt32, pAce: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetAclInformation(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), pAclInformation: VoidPtr, nAclInformationLength: UInt32, dwAclInformationClass: win32more.Windows.Win32.Security.ACL_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetFileSecurityW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetKernelObjectSecurity(Handle: win32more.Windows.Win32.Foundation.HANDLE, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetLengthSid(pSid: win32more.Windows.Win32.Foundation.PSID) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetPrivateObjectSecurity(ObjectDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ResultantDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, DescriptorLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorControl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pControl: POINTER(UInt16), lpdwRevision: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorDacl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, lpbDaclPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL), pDacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), lpbDaclDefaulted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorGroup(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pGroup: POINTER(win32more.Windows.Win32.Foundation.PSID), lpbGroupDefaulted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorLength(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorOwner(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pOwner: POINTER(win32more.Windows.Win32.Foundation.PSID), lpbOwnerDefaulted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorRMControl(SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, RMControl: POINTER(Byte)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorSacl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, lpbSaclPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL), pSacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), lpbSaclDefaulted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSidIdentifierAuthority(pSid: win32more.Windows.Win32.Foundation.PSID) -> POINTER(win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY): ...
@winfunctype('ADVAPI32.dll')
def GetSidLengthRequired(nSubAuthorityCount: Byte) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSidSubAuthority(pSid: win32more.Windows.Win32.Foundation.PSID, nSubAuthority: UInt32) -> POINTER(UInt32): ...
@winfunctype('ADVAPI32.dll')
def GetSidSubAuthorityCount(pSid: win32more.Windows.Win32.Foundation.PSID) -> POINTER(Byte): ...
@winfunctype('ADVAPI32.dll')
def GetTokenInformation(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, TokenInformationClass: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS, TokenInformation: VoidPtr, TokenInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetWindowsAccountDomainSid(pSid: win32more.Windows.Win32.Foundation.PSID, pDomainSid: win32more.Windows.Win32.Foundation.PSID, cbDomainSid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateAnonymousToken(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateLoggedOnUser(hToken: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateSelf(ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeAcl(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), nAclLength: UInt32, dwAclRevision: win32more.Windows.Win32.Security.ACE_REVISION) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeSecurityDescriptor(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, dwRevision: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeSid(Sid: win32more.Windows.Win32.Foundation.PSID, pIdentifierAuthority: POINTER(win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY), nSubAuthorityCount: Byte) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsTokenRestricted(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidAcl(pAcl: POINTER(win32more.Windows.Win32.Security.ACL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidSecurityDescriptor(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidSid(pSid: win32more.Windows.Win32.Foundation.PSID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsWellKnownSid(pSid: win32more.Windows.Win32.Foundation.PSID, WellKnownSidType: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MakeAbsoluteSD(pSelfRelativeSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pAbsoluteSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, lpdwAbsoluteSecurityDescriptorSize: POINTER(UInt32), pDacl: POINTER(win32more.Windows.Win32.Security.ACL), lpdwDaclSize: POINTER(UInt32), pSacl: POINTER(win32more.Windows.Win32.Security.ACL), lpdwSaclSize: POINTER(UInt32), pOwner: win32more.Windows.Win32.Foundation.PSID, lpdwOwnerSize: POINTER(UInt32), pPrimaryGroup: win32more.Windows.Win32.Foundation.PSID, lpdwPrimaryGroupSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MakeSelfRelativeSD(pAbsoluteSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pSelfRelativeSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, lpdwBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MapGenericMask(AccessMask: POINTER(UInt32), GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def ObjectCloseAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, GenerateOnClose: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectDeleteAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, GenerateOnClose: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectOpenAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, ObjectName: win32more.Windows.Win32.Foundation.PWSTR, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, GrantedAccess: UInt32, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, AccessGranted: win32more.Windows.Win32.Foundation.BOOL, GenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectPrivilegeAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, HandleId: VoidPtr, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), AccessGranted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegeCheck(ClientToken: win32more.Windows.Win32.Foundation.HANDLE, RequiredPrivileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), pfResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegedServiceAuditAlarmW(SubsystemName: win32more.Windows.Win32.Foundation.PWSTR, ServiceName: win32more.Windows.Win32.Foundation.PWSTR, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), AccessGranted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QuerySecurityAccessMask(SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, DesiredAccess: POINTER(UInt32)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def RevertToSelf() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetAclInformation(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), pAclInformation: VoidPtr, nAclInformationLength: UInt32, dwAclInformationClass: win32more.Windows.Win32.Security.ACL_INFORMATION_CLASS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetFileSecurityW(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetKernelObjectSecurity(Handle: win32more.Windows.Win32.Foundation.HANDLE, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetPrivateObjectSecurity(SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ModificationDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ObjectsSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), Token: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetPrivateObjectSecurityEx(SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ModificationDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ObjectsSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), AutoInheritFlags: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), Token: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityAccessMask(SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, DesiredAccess: POINTER(UInt32)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorControl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ControlBitsOfInterest: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL, ControlBitsToSet: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorDacl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, bDaclPresent: win32more.Windows.Win32.Foundation.BOOL, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), bDaclDefaulted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorGroup(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pGroup: win32more.Windows.Win32.Foundation.PSID, bGroupDefaulted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorOwner(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pOwner: win32more.Windows.Win32.Foundation.PSID, bOwnerDefaulted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorRMControl(SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, RMControl: POINTER(Byte)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorSacl(pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, bSaclPresent: win32more.Windows.Win32.Foundation.BOOL, pSacl: POINTER(win32more.Windows.Win32.Security.ACL), bSaclDefaulted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetTokenInformation(TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, TokenInformationClass: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS, TokenInformation: VoidPtr, TokenInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCachedSigningLevel(SourceFiles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), SourceFileCount: UInt32, Flags: UInt32, TargetFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCachedSigningLevel(File: win32more.Windows.Win32.Foundation.HANDLE, Flags: POINTER(UInt32), SigningLevel: POINTER(UInt32), Thumbprint: POINTER(Byte), ThumbprintSize: POINTER(UInt32), ThumbprintAlgorithm: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-security-base-l1-2-2.dll')
def DeriveCapabilitySidsFromName(CapName: win32more.Windows.Win32.Foundation.PWSTR, CapabilityGroupSids: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSID)), CapabilityGroupSidCount: POINTER(UInt32), CapabilitySids: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSID)), CapabilitySidCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ntdll.dll')
def RtlNormalizeSecurityDescriptor(SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorLength: UInt32, NewSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), NewSecurityDescriptorLength: POINTER(UInt32), CheckOnly: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('USER32.dll')
def SetUserObjectSecurity(hObj: win32more.Windows.Win32.Foundation.HANDLE, pSIRequested: POINTER(win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION), pSID: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUserObjectSecurity(hObj: win32more.Windows.Win32.Foundation.HANDLE, pSIRequested: POINTER(UInt32), pSID: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckAndAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, ObjectName: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeAndAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, ObjectName: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, ObjectName: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmByHandleA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, ObjectName: win32more.Windows.Win32.Foundation.PSTR, SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Windows.Win32.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectOpenAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, ObjectName: win32more.Windows.Win32.Foundation.PSTR, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, GrantedAccess: UInt32, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), ObjectCreation: win32more.Windows.Win32.Foundation.BOOL, AccessGranted: win32more.Windows.Win32.Foundation.BOOL, GenerateOnClose: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectPrivilegeAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: UInt32, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), AccessGranted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectCloseAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, GenerateOnClose: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectDeleteAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, HandleId: VoidPtr, GenerateOnClose: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegedServiceAuditAlarmA(SubsystemName: win32more.Windows.Win32.Foundation.PSTR, ServiceName: win32more.Windows.Win32.Foundation.PSTR, ClientToken: win32more.Windows.Win32.Foundation.HANDLE, Privileges: POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET), AccessGranted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddConditionalAce(pAcl: POINTER(win32more.Windows.Win32.Security.ACL), dwAceRevision: win32more.Windows.Win32.Security.ACE_REVISION, AceFlags: win32more.Windows.Win32.Security.ACE_FLAGS, AceType: Byte, AccessMask: UInt32, pSid: win32more.Windows.Win32.Foundation.PSID, ConditionStr: win32more.Windows.Win32.Foundation.PWSTR, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetFileSecurityA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetFileSecurityA(lpFileName: win32more.Windows.Win32.Foundation.PSTR, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountSidA(lpSystemName: win32more.Windows.Win32.Foundation.PSTR, Sid: win32more.Windows.Win32.Foundation.PSID, Name: win32more.Windows.Win32.Foundation.PSTR, cchName: POINTER(UInt32), ReferencedDomainName: win32more.Windows.Win32.Foundation.PSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Windows.Win32.Security.SID_NAME_USE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountSidW(lpSystemName: win32more.Windows.Win32.Foundation.PWSTR, Sid: win32more.Windows.Win32.Foundation.PSID, Name: win32more.Windows.Win32.Foundation.PWSTR, cchName: POINTER(UInt32), ReferencedDomainName: win32more.Windows.Win32.Foundation.PWSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Windows.Win32.Security.SID_NAME_USE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountNameA(lpSystemName: win32more.Windows.Win32.Foundation.PSTR, lpAccountName: win32more.Windows.Win32.Foundation.PSTR, Sid: win32more.Windows.Win32.Foundation.PSID, cbSid: POINTER(UInt32), ReferencedDomainName: win32more.Windows.Win32.Foundation.PSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Windows.Win32.Security.SID_NAME_USE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountNameW(lpSystemName: win32more.Windows.Win32.Foundation.PWSTR, lpAccountName: win32more.Windows.Win32.Foundation.PWSTR, Sid: win32more.Windows.Win32.Foundation.PSID, cbSid: POINTER(UInt32), ReferencedDomainName: win32more.Windows.Win32.Foundation.PWSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Windows.Win32.Security.SID_NAME_USE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeValueA(lpSystemName: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, lpLuid: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeValueW(lpSystemName: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpLuid: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeNameA(lpSystemName: win32more.Windows.Win32.Foundation.PSTR, lpLuid: POINTER(win32more.Windows.Win32.Foundation.LUID), lpName: win32more.Windows.Win32.Foundation.PSTR, cchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeNameW(lpSystemName: win32more.Windows.Win32.Foundation.PWSTR, lpLuid: POINTER(win32more.Windows.Win32.Foundation.LUID), lpName: win32more.Windows.Win32.Foundation.PWSTR, cchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeDisplayNameA(lpSystemName: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PSTR, cchDisplayName: POINTER(UInt32), lpLanguageId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeDisplayNameW(lpSystemName: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpDisplayName: win32more.Windows.Win32.Foundation.PWSTR, cchDisplayName: POINTER(UInt32), lpLanguageId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserA(lpszUsername: win32more.Windows.Win32.Foundation.PSTR, lpszDomain: win32more.Windows.Win32.Foundation.PSTR, lpszPassword: win32more.Windows.Win32.Foundation.PSTR, dwLogonType: win32more.Windows.Win32.Security.LOGON32_LOGON, dwLogonProvider: win32more.Windows.Win32.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserW(lpszUsername: win32more.Windows.Win32.Foundation.PWSTR, lpszDomain: win32more.Windows.Win32.Foundation.PWSTR, lpszPassword: win32more.Windows.Win32.Foundation.PWSTR, dwLogonType: win32more.Windows.Win32.Security.LOGON32_LOGON, dwLogonProvider: win32more.Windows.Win32.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserExA(lpszUsername: win32more.Windows.Win32.Foundation.PSTR, lpszDomain: win32more.Windows.Win32.Foundation.PSTR, lpszPassword: win32more.Windows.Win32.Foundation.PSTR, dwLogonType: win32more.Windows.Win32.Security.LOGON32_LOGON, dwLogonProvider: win32more.Windows.Win32.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE), ppLogonSid: POINTER(win32more.Windows.Win32.Foundation.PSID), ppProfileBuffer: POINTER(VoidPtr), pdwProfileLength: POINTER(UInt32), pQuotaLimits: POINTER(win32more.Windows.Win32.Security.QUOTA_LIMITS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserExW(lpszUsername: win32more.Windows.Win32.Foundation.PWSTR, lpszDomain: win32more.Windows.Win32.Foundation.PWSTR, lpszPassword: win32more.Windows.Win32.Foundation.PWSTR, dwLogonType: win32more.Windows.Win32.Security.LOGON32_LOGON, dwLogonProvider: win32more.Windows.Win32.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE), ppLogonSid: POINTER(win32more.Windows.Win32.Foundation.PSID), ppProfileBuffer: POINTER(VoidPtr), pdwProfileLength: POINTER(UInt32), pQuotaLimits: POINTER(win32more.Windows.Win32.Security.QUOTA_LIMITS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ntdll.dll')
def RtlConvertSidToUnicodeString(UnicodeString: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), Sid: win32more.Windows.Win32.Foundation.PSID, AllocateDestinationString: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class CLAIM_SECURITY_ATTRIBUTES_INFORMATION(EasyCastStructure):
    Version: UInt16
    Reserved: UInt16
    AttributeCount: UInt32
    Attribute: _Attribute_e__Union
    class _Attribute_e__Union(EasyCastUnion):
        pAttributeV1: POINTER(win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_V1)
CLAIM_SECURITY_ATTRIBUTE_FLAGS = UInt32
CLAIM_SECURITY_ATTRIBUTE_NON_INHERITABLE: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 1
CLAIM_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 2
CLAIM_SECURITY_ATTRIBUTE_USE_FOR_DENY_ONLY: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 4
CLAIM_SECURITY_ATTRIBUTE_DISABLED_BY_DEFAULT: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 8
CLAIM_SECURITY_ATTRIBUTE_DISABLED: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 16
CLAIM_SECURITY_ATTRIBUTE_MANDATORY: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS = 32
class CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE(EasyCastStructure):
    Version: UInt64
    Name: win32more.Windows.Win32.Foundation.PWSTR
class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(EasyCastStructure):
    pValue: VoidPtr
    ValueLength: UInt32
class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(EasyCastStructure):
    Name: UInt32
    ValueType: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE
    Reserved: UInt16
    Flags: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(EasyCastUnion):
        pInt64: UInt32 * 1
        pUint64: UInt32 * 1
        ppString: UInt32 * 1
        pFqbn: UInt32 * 1
        pOctetString: UInt32 * 1
class CLAIM_SECURITY_ATTRIBUTE_V1(EasyCastStructure):
    Name: win32more.Windows.Win32.Foundation.PWSTR
    ValueType: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE
    Reserved: UInt16
    Flags: UInt32
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(EasyCastUnion):
        pInt64: POINTER(Int64)
        pUint64: POINTER(UInt64)
        ppString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        pFqbn: POINTER(win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE)
        pOctetString: POINTER(win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE)
CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = UInt16
CLAIM_SECURITY_ATTRIBUTE_TYPE_INT64: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 1
CLAIM_SECURITY_ATTRIBUTE_TYPE_UINT64: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 2
CLAIM_SECURITY_ATTRIBUTE_TYPE_STRING: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 3
CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 16
CLAIM_SECURITY_ATTRIBUTE_TYPE_FQBN: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 4
CLAIM_SECURITY_ATTRIBUTE_TYPE_SID: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 5
CLAIM_SECURITY_ATTRIBUTE_TYPE_BOOLEAN: win32more.Windows.Win32.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 6
CREATE_RESTRICTED_TOKEN_FLAGS = UInt32
DISABLE_MAX_PRIVILEGE: win32more.Windows.Win32.Security.CREATE_RESTRICTED_TOKEN_FLAGS = 1
SANDBOX_INERT: win32more.Windows.Win32.Security.CREATE_RESTRICTED_TOKEN_FLAGS = 2
LUA_TOKEN: win32more.Windows.Win32.Security.CREATE_RESTRICTED_TOKEN_FLAGS = 4
WRITE_RESTRICTED: win32more.Windows.Win32.Security.CREATE_RESTRICTED_TOKEN_FLAGS = 8
ENUM_PERIOD = Int32
ENUM_PERIOD_INVALID: win32more.Windows.Win32.Security.ENUM_PERIOD = -1
ENUM_PERIOD_SECONDS: win32more.Windows.Win32.Security.ENUM_PERIOD = 0
ENUM_PERIOD_MINUTES: win32more.Windows.Win32.Security.ENUM_PERIOD = 1
ENUM_PERIOD_HOURS: win32more.Windows.Win32.Security.ENUM_PERIOD = 2
ENUM_PERIOD_DAYS: win32more.Windows.Win32.Security.ENUM_PERIOD = 3
ENUM_PERIOD_WEEKS: win32more.Windows.Win32.Security.ENUM_PERIOD = 4
ENUM_PERIOD_MONTHS: win32more.Windows.Win32.Security.ENUM_PERIOD = 5
ENUM_PERIOD_YEARS: win32more.Windows.Win32.Security.ENUM_PERIOD = 6
class GENERIC_MAPPING(EasyCastStructure):
    GenericRead: UInt32
    GenericWrite: UInt32
    GenericExecute: UInt32
    GenericAll: UInt32
HDIAGNOSTIC_DATA_QUERY_SESSION = IntPtr
HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION = IntPtr
HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION = IntPtr
HDIAGNOSTIC_EVENT_TAG_DESCRIPTION = IntPtr
HDIAGNOSTIC_RECORD = IntPtr
HDIAGNOSTIC_REPORT = IntPtr
class LLFILETIME(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        ll: Int64
        ft: win32more.Windows.Win32.Foundation.FILETIME
LOGON32_LOGON = UInt32
LOGON32_LOGON_BATCH: win32more.Windows.Win32.Security.LOGON32_LOGON = 4
LOGON32_LOGON_INTERACTIVE: win32more.Windows.Win32.Security.LOGON32_LOGON = 2
LOGON32_LOGON_NETWORK: win32more.Windows.Win32.Security.LOGON32_LOGON = 3
LOGON32_LOGON_NETWORK_CLEARTEXT: win32more.Windows.Win32.Security.LOGON32_LOGON = 8
LOGON32_LOGON_NEW_CREDENTIALS: win32more.Windows.Win32.Security.LOGON32_LOGON = 9
LOGON32_LOGON_SERVICE: win32more.Windows.Win32.Security.LOGON32_LOGON = 5
LOGON32_LOGON_UNLOCK: win32more.Windows.Win32.Security.LOGON32_LOGON = 7
LOGON32_PROVIDER = UInt32
LOGON32_PROVIDER_DEFAULT: win32more.Windows.Win32.Security.LOGON32_PROVIDER = 0
LOGON32_PROVIDER_WINNT50: win32more.Windows.Win32.Security.LOGON32_PROVIDER = 3
LOGON32_PROVIDER_WINNT40: win32more.Windows.Win32.Security.LOGON32_PROVIDER = 2
class LUID_AND_ATTRIBUTES(EasyCastStructure):
    Luid: win32more.Windows.Win32.Foundation.LUID
    Attributes: win32more.Windows.Win32.Security.TOKEN_PRIVILEGES_ATTRIBUTES
MANDATORY_LEVEL = Int32
MANDATORY_LEVEL_MandatoryLevelUntrusted: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 0
MANDATORY_LEVEL_MandatoryLevelLow: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 1
MANDATORY_LEVEL_MandatoryLevelMedium: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 2
MANDATORY_LEVEL_MandatoryLevelHigh: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 3
MANDATORY_LEVEL_MandatoryLevelSystem: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 4
MANDATORY_LEVEL_MandatoryLevelSecureProcess: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 5
MANDATORY_LEVEL_MandatoryLevelCount: win32more.Windows.Win32.Security.MANDATORY_LEVEL = 6
NCRYPT_DESCRIPTOR_HANDLE = IntPtr
NCRYPT_STREAM_HANDLE = IntPtr
OBJECT_SECURITY_INFORMATION = UInt32
ATTRIBUTE_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 32
BACKUP_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 65536
DACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 4
GROUP_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 2
LABEL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 16
OWNER_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 1
PROTECTED_DACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 2147483648
PROTECTED_SACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 1073741824
SACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 8
SCOPE_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 64
UNPROTECTED_DACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 536870912
UNPROTECTED_SACL_SECURITY_INFORMATION: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION = 268435456
class OBJECT_TYPE_LIST(EasyCastStructure):
    Level: UInt16
    Sbz: UInt16
    ObjectType: POINTER(Guid)
@winfunctype_pointer
def PLSA_AP_CALL_PACKAGE_UNTRUSTED(ClientRequest: POINTER(VoidPtr), ProtocolSubmitBuffer: VoidPtr, ClientBufferBase: VoidPtr, SubmitBufferLength: UInt32, ProtocolReturnBuffer: POINTER(VoidPtr), ReturnBufferLength: POINTER(UInt32), ProtocolStatus: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class PRIVILEGE_SET(EasyCastStructure):
    PrivilegeCount: UInt32
    Control: UInt32
    Privilege: win32more.Windows.Win32.Security.LUID_AND_ATTRIBUTES * 1
PSECURITY_DESCRIPTOR = VoidPtr
class QUOTA_LIMITS(EasyCastStructure):
    PagedPoolLimit: UIntPtr
    NonPagedPoolLimit: UIntPtr
    MinimumWorkingSetSize: UIntPtr
    MaximumWorkingSetSize: UIntPtr
    PagefileLimit: UIntPtr
    TimeLimit: Int64
SAFER_LEVEL_HANDLE = IntPtr
SC_HANDLE = IntPtr
class SECURITY_ATTRIBUTES(EasyCastStructure):
    nLength: UInt32
    lpSecurityDescriptor: VoidPtr
    bInheritHandle: win32more.Windows.Win32.Foundation.BOOL
SECURITY_AUTO_INHERIT_FLAGS = UInt32
SEF_AVOID_OWNER_CHECK: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 16
SEF_AVOID_OWNER_RESTRICTION: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 4096
SEF_AVOID_PRIVILEGE_CHECK: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 8
SEF_DACL_AUTO_INHERIT: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 1
SEF_DEFAULT_DESCRIPTOR_FOR_OBJECT: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 4
SEF_DEFAULT_GROUP_FROM_PARENT: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 64
SEF_DEFAULT_OWNER_FROM_PARENT: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 32
SEF_MACL_NO_EXECUTE_UP: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 1024
SEF_MACL_NO_READ_UP: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 512
SEF_MACL_NO_WRITE_UP: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 256
SEF_SACL_AUTO_INHERIT: win32more.Windows.Win32.Security.SECURITY_AUTO_INHERIT_FLAGS = 2
class SECURITY_CAPABILITIES(EasyCastStructure):
    AppContainerSid: win32more.Windows.Win32.Foundation.PSID
    Capabilities: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)
    CapabilityCount: UInt32
    Reserved: UInt32
class SECURITY_DESCRIPTOR(EasyCastStructure):
    Revision: Byte
    Sbz1: Byte
    Control: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL
    Owner: win32more.Windows.Win32.Foundation.PSID
    Group: win32more.Windows.Win32.Foundation.PSID
    Sacl: POINTER(win32more.Windows.Win32.Security.ACL)
    Dacl: POINTER(win32more.Windows.Win32.Security.ACL)
SECURITY_DESCRIPTOR_CONTROL = UInt16
SE_OWNER_DEFAULTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 1
SE_GROUP_DEFAULTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 2
SE_DACL_PRESENT: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 4
SE_DACL_DEFAULTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 8
SE_SACL_PRESENT: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 16
SE_SACL_DEFAULTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 32
SE_DACL_AUTO_INHERIT_REQ: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 256
SE_SACL_AUTO_INHERIT_REQ: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 512
SE_DACL_AUTO_INHERITED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 1024
SE_SACL_AUTO_INHERITED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 2048
SE_DACL_PROTECTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 4096
SE_SACL_PROTECTED: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 8192
SE_RM_CONTROL_VALID: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 16384
SE_SELF_RELATIVE: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL = 32768
class SECURITY_DESCRIPTOR_RELATIVE(EasyCastStructure):
    Revision: Byte
    Sbz1: Byte
    Control: win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR_CONTROL
    Owner: UInt32
    Group: UInt32
    Sacl: UInt32
    Dacl: UInt32
SECURITY_IMPERSONATION_LEVEL = Int32
SECURITY_IMPERSONATION_LEVEL_SecurityAnonymous: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL = 0
SECURITY_IMPERSONATION_LEVEL_SecurityIdentification: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL = 1
SECURITY_IMPERSONATION_LEVEL_SecurityImpersonation: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL = 2
SECURITY_IMPERSONATION_LEVEL_SecurityDelegation: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL = 3
class SECURITY_QUALITY_OF_SERVICE(EasyCastStructure):
    Length: UInt32
    ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL
    ContextTrackingMode: Byte
    EffectiveOnly: win32more.Windows.Win32.Foundation.BOOLEAN
@winfunctype_pointer
def SEC_THREAD_START(lpThreadParameter: VoidPtr) -> UInt32: ...
class SE_ACCESS_REPLY(EasyCastStructure):
    Size: UInt32
    ResultListCount: UInt32
    GrantedAccess: POINTER(UInt32)
    AccessStatus: POINTER(UInt32)
    AccessReason: POINTER(win32more.Windows.Win32.Security.ACCESS_REASONS)
    Privileges: POINTER(POINTER(win32more.Windows.Win32.Security.PRIVILEGE_SET))
class SE_ACCESS_REQUEST(EasyCastStructure):
    Size: UInt32
    SeSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SE_SECURITY_DESCRIPTOR)
    DesiredAccess: UInt32
    PreviouslyGrantedAccess: UInt32
    PrincipalSelfSid: win32more.Windows.Win32.Foundation.PSID
    GenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING)
    ObjectTypeListCount: UInt32
    ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST)
class SE_IMPERSONATION_STATE(EasyCastStructure):
    Token: VoidPtr
    CopyOnOpen: win32more.Windows.Win32.Foundation.BOOLEAN
    EffectiveOnly: win32more.Windows.Win32.Foundation.BOOLEAN
    Level: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL
class SE_SECURITY_DESCRIPTOR(EasyCastStructure):
    Size: UInt32
    Flags: UInt32
    SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
class SE_SID(EasyCastUnion):
    Sid: win32more.Windows.Win32.Security.SID
    Buffer: Byte * 68
class SID(EasyCastStructure):
    Revision: Byte
    SubAuthorityCount: Byte
    IdentifierAuthority: win32more.Windows.Win32.Security.SID_IDENTIFIER_AUTHORITY
    SubAuthority: UInt32 * 1
class SID_AND_ATTRIBUTES(EasyCastStructure):
    Sid: win32more.Windows.Win32.Foundation.PSID
    Attributes: UInt32
class SID_AND_ATTRIBUTES_HASH(EasyCastStructure):
    SidCount: UInt32
    SidAttr: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)
    Hash: UIntPtr * 32
class SID_IDENTIFIER_AUTHORITY(EasyCastStructure):
    Value: Byte * 6
SID_NAME_USE = Int32
SID_NAME_USE_SidTypeUser: win32more.Windows.Win32.Security.SID_NAME_USE = 1
SID_NAME_USE_SidTypeGroup: win32more.Windows.Win32.Security.SID_NAME_USE = 2
SID_NAME_USE_SidTypeDomain: win32more.Windows.Win32.Security.SID_NAME_USE = 3
SID_NAME_USE_SidTypeAlias: win32more.Windows.Win32.Security.SID_NAME_USE = 4
SID_NAME_USE_SidTypeWellKnownGroup: win32more.Windows.Win32.Security.SID_NAME_USE = 5
SID_NAME_USE_SidTypeDeletedAccount: win32more.Windows.Win32.Security.SID_NAME_USE = 6
SID_NAME_USE_SidTypeInvalid: win32more.Windows.Win32.Security.SID_NAME_USE = 7
SID_NAME_USE_SidTypeUnknown: win32more.Windows.Win32.Security.SID_NAME_USE = 8
SID_NAME_USE_SidTypeComputer: win32more.Windows.Win32.Security.SID_NAME_USE = 9
SID_NAME_USE_SidTypeLabel: win32more.Windows.Win32.Security.SID_NAME_USE = 10
SID_NAME_USE_SidTypeLogonSession: win32more.Windows.Win32.Security.SID_NAME_USE = 11
class SYSTEM_ACCESS_FILTER_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_CALLBACK_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_CALLBACK_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_ALARM_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: UInt32
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_AUDIT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_AUDIT_CALLBACK_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_AUDIT_CALLBACK_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_AUDIT_OBJECT_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
SYSTEM_AUDIT_OBJECT_ACE_FLAGS = UInt32
ACE_OBJECT_TYPE_PRESENT: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS = 1
ACE_INHERITED_OBJECT_TYPE_PRESENT: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS = 2
class SYSTEM_MANDATORY_LABEL_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_PROCESS_TRUST_LABEL_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_RESOURCE_ATTRIBUTE_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_SCOPED_POLICY_ID_ACE(EasyCastStructure):
    Header: win32more.Windows.Win32.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class TOKEN_ACCESS_INFORMATION(EasyCastStructure):
    SidHash: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_HASH)
    RestrictedSidHash: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_HASH)
    Privileges: POINTER(win32more.Windows.Win32.Security.TOKEN_PRIVILEGES)
    AuthenticationId: win32more.Windows.Win32.Foundation.LUID
    TokenType: win32more.Windows.Win32.Security.TOKEN_TYPE
    ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL
    MandatoryPolicy: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY
    Flags: UInt32
    AppContainerNumber: UInt32
    PackageSid: win32more.Windows.Win32.Foundation.PSID
    CapabilitiesHash: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES_HASH)
    TrustLevelSid: win32more.Windows.Win32.Foundation.PSID
    SecurityAttributes: VoidPtr
TOKEN_ACCESS_MASK = UInt32
TOKEN_DELETE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 65536
TOKEN_READ_CONTROL: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 131072
TOKEN_WRITE_DAC: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 262144
TOKEN_WRITE_OWNER: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 524288
TOKEN_ACCESS_SYSTEM_SECURITY: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 16777216
TOKEN_ASSIGN_PRIMARY: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 1
TOKEN_DUPLICATE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 2
TOKEN_IMPERSONATE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 4
TOKEN_QUERY: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 8
TOKEN_QUERY_SOURCE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 16
TOKEN_ADJUST_PRIVILEGES: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 32
TOKEN_ADJUST_GROUPS: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 64
TOKEN_ADJUST_DEFAULT: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 128
TOKEN_ADJUST_SESSIONID: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 256
TOKEN_READ: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 131080
TOKEN_WRITE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 131296
TOKEN_EXECUTE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 131072
TOKEN_TRUST_CONSTRAINT_MASK: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 131096
TOKEN_ACCESS_PSEUDO_HANDLE_WIN8: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 24
TOKEN_ACCESS_PSEUDO_HANDLE: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 24
TOKEN_ALL_ACCESS: win32more.Windows.Win32.Security.TOKEN_ACCESS_MASK = 983551
class TOKEN_APPCONTAINER_INFORMATION(EasyCastStructure):
    TokenAppContainer: win32more.Windows.Win32.Foundation.PSID
class TOKEN_AUDIT_POLICY(EasyCastStructure):
    PerUserPolicy: Byte * 30
class TOKEN_CONTROL(EasyCastStructure):
    TokenId: win32more.Windows.Win32.Foundation.LUID
    AuthenticationId: win32more.Windows.Win32.Foundation.LUID
    ModifiedId: win32more.Windows.Win32.Foundation.LUID
    TokenSource: win32more.Windows.Win32.Security.TOKEN_SOURCE
class TOKEN_DEFAULT_DACL(EasyCastStructure):
    DefaultDacl: POINTER(win32more.Windows.Win32.Security.ACL)
class TOKEN_DEVICE_CLAIMS(EasyCastStructure):
    DeviceClaims: VoidPtr
class TOKEN_ELEVATION(EasyCastStructure):
    TokenIsElevated: UInt32
TOKEN_ELEVATION_TYPE = Int32
TOKEN_ELEVATION_TYPE_TokenElevationTypeDefault: win32more.Windows.Win32.Security.TOKEN_ELEVATION_TYPE = 1
TOKEN_ELEVATION_TYPE_TokenElevationTypeFull: win32more.Windows.Win32.Security.TOKEN_ELEVATION_TYPE = 2
TOKEN_ELEVATION_TYPE_TokenElevationTypeLimited: win32more.Windows.Win32.Security.TOKEN_ELEVATION_TYPE = 3
class TOKEN_GROUPS(EasyCastStructure):
    GroupCount: UInt32
    Groups: win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES * 1
class TOKEN_GROUPS_AND_PRIVILEGES(EasyCastStructure):
    SidCount: UInt32
    SidLength: UInt32
    Sids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)
    RestrictedSidCount: UInt32
    RestrictedSidLength: UInt32
    RestrictedSids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)
    PrivilegeCount: UInt32
    PrivilegeLength: UInt32
    Privileges: POINTER(win32more.Windows.Win32.Security.LUID_AND_ATTRIBUTES)
    AuthenticationId: win32more.Windows.Win32.Foundation.LUID
TOKEN_INFORMATION_CLASS = Int32
TOKEN_INFORMATION_CLASS_TokenUser: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 1
TOKEN_INFORMATION_CLASS_TokenGroups: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 2
TOKEN_INFORMATION_CLASS_TokenPrivileges: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 3
TOKEN_INFORMATION_CLASS_TokenOwner: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 4
TOKEN_INFORMATION_CLASS_TokenPrimaryGroup: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 5
TOKEN_INFORMATION_CLASS_TokenDefaultDacl: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 6
TOKEN_INFORMATION_CLASS_TokenSource: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 7
TOKEN_INFORMATION_CLASS_TokenType: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 8
TOKEN_INFORMATION_CLASS_TokenImpersonationLevel: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 9
TOKEN_INFORMATION_CLASS_TokenStatistics: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 10
TOKEN_INFORMATION_CLASS_TokenRestrictedSids: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 11
TOKEN_INFORMATION_CLASS_TokenSessionId: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 12
TOKEN_INFORMATION_CLASS_TokenGroupsAndPrivileges: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 13
TOKEN_INFORMATION_CLASS_TokenSessionReference: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 14
TOKEN_INFORMATION_CLASS_TokenSandBoxInert: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 15
TOKEN_INFORMATION_CLASS_TokenAuditPolicy: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 16
TOKEN_INFORMATION_CLASS_TokenOrigin: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 17
TOKEN_INFORMATION_CLASS_TokenElevationType: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 18
TOKEN_INFORMATION_CLASS_TokenLinkedToken: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 19
TOKEN_INFORMATION_CLASS_TokenElevation: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 20
TOKEN_INFORMATION_CLASS_TokenHasRestrictions: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 21
TOKEN_INFORMATION_CLASS_TokenAccessInformation: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 22
TOKEN_INFORMATION_CLASS_TokenVirtualizationAllowed: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 23
TOKEN_INFORMATION_CLASS_TokenVirtualizationEnabled: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 24
TOKEN_INFORMATION_CLASS_TokenIntegrityLevel: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 25
TOKEN_INFORMATION_CLASS_TokenUIAccess: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 26
TOKEN_INFORMATION_CLASS_TokenMandatoryPolicy: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 27
TOKEN_INFORMATION_CLASS_TokenLogonSid: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 28
TOKEN_INFORMATION_CLASS_TokenIsAppContainer: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 29
TOKEN_INFORMATION_CLASS_TokenCapabilities: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 30
TOKEN_INFORMATION_CLASS_TokenAppContainerSid: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 31
TOKEN_INFORMATION_CLASS_TokenAppContainerNumber: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 32
TOKEN_INFORMATION_CLASS_TokenUserClaimAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 33
TOKEN_INFORMATION_CLASS_TokenDeviceClaimAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 34
TOKEN_INFORMATION_CLASS_TokenRestrictedUserClaimAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 35
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceClaimAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 36
TOKEN_INFORMATION_CLASS_TokenDeviceGroups: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 37
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceGroups: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 38
TOKEN_INFORMATION_CLASS_TokenSecurityAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 39
TOKEN_INFORMATION_CLASS_TokenIsRestricted: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 40
TOKEN_INFORMATION_CLASS_TokenProcessTrustLevel: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 41
TOKEN_INFORMATION_CLASS_TokenPrivateNameSpace: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 42
TOKEN_INFORMATION_CLASS_TokenSingletonAttributes: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 43
TOKEN_INFORMATION_CLASS_TokenBnoIsolation: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 44
TOKEN_INFORMATION_CLASS_TokenChildProcessFlags: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 45
TOKEN_INFORMATION_CLASS_TokenIsLessPrivilegedAppContainer: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 46
TOKEN_INFORMATION_CLASS_TokenIsSandboxed: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 47
TOKEN_INFORMATION_CLASS_TokenIsAppSilo: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 48
TOKEN_INFORMATION_CLASS_MaxTokenInfoClass: win32more.Windows.Win32.Security.TOKEN_INFORMATION_CLASS = 49
class TOKEN_LINKED_TOKEN(EasyCastStructure):
    LinkedToken: win32more.Windows.Win32.Foundation.HANDLE
class TOKEN_MANDATORY_LABEL(EasyCastStructure):
    Label: win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES
class TOKEN_MANDATORY_POLICY(EasyCastStructure):
    Policy: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY_ID
TOKEN_MANDATORY_POLICY_ID = UInt32
TOKEN_MANDATORY_POLICY_OFF: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY_ID = 0
TOKEN_MANDATORY_POLICY_NO_WRITE_UP: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY_ID = 1
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY_ID = 2
TOKEN_MANDATORY_POLICY_VALID_MASK: win32more.Windows.Win32.Security.TOKEN_MANDATORY_POLICY_ID = 3
class TOKEN_ORIGIN(EasyCastStructure):
    OriginatingLogonSession: win32more.Windows.Win32.Foundation.LUID
class TOKEN_OWNER(EasyCastStructure):
    Owner: win32more.Windows.Win32.Foundation.PSID
class TOKEN_PRIMARY_GROUP(EasyCastStructure):
    PrimaryGroup: win32more.Windows.Win32.Foundation.PSID
class TOKEN_PRIVILEGES(EasyCastStructure):
    PrivilegeCount: UInt32
    Privileges: win32more.Windows.Win32.Security.LUID_AND_ATTRIBUTES * 1
TOKEN_PRIVILEGES_ATTRIBUTES = UInt32
SE_PRIVILEGE_ENABLED: win32more.Windows.Win32.Security.TOKEN_PRIVILEGES_ATTRIBUTES = 2
SE_PRIVILEGE_ENABLED_BY_DEFAULT: win32more.Windows.Win32.Security.TOKEN_PRIVILEGES_ATTRIBUTES = 1
SE_PRIVILEGE_REMOVED: win32more.Windows.Win32.Security.TOKEN_PRIVILEGES_ATTRIBUTES = 4
SE_PRIVILEGE_USED_FOR_ACCESS: win32more.Windows.Win32.Security.TOKEN_PRIVILEGES_ATTRIBUTES = 2147483648
class TOKEN_SOURCE(EasyCastStructure):
    SourceName: win32more.Windows.Win32.Foundation.CHAR * 8
    SourceIdentifier: win32more.Windows.Win32.Foundation.LUID
class TOKEN_STATISTICS(EasyCastStructure):
    TokenId: win32more.Windows.Win32.Foundation.LUID
    AuthenticationId: win32more.Windows.Win32.Foundation.LUID
    ExpirationTime: Int64
    TokenType: win32more.Windows.Win32.Security.TOKEN_TYPE
    ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL
    DynamicCharged: UInt32
    DynamicAvailable: UInt32
    GroupCount: UInt32
    PrivilegeCount: UInt32
    ModifiedId: win32more.Windows.Win32.Foundation.LUID
TOKEN_TYPE = Int32
TOKEN_TYPE_TokenPrimary: win32more.Windows.Win32.Security.TOKEN_TYPE = 1
TOKEN_TYPE_TokenImpersonation: win32more.Windows.Win32.Security.TOKEN_TYPE = 2
class TOKEN_USER(EasyCastStructure):
    User: win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES
class TOKEN_USER_CLAIMS(EasyCastStructure):
    UserClaims: VoidPtr
WELL_KNOWN_SID_TYPE = Int32
WELL_KNOWN_SID_TYPE_WinNullSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 0
WELL_KNOWN_SID_TYPE_WinWorldSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 1
WELL_KNOWN_SID_TYPE_WinLocalSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 2
WELL_KNOWN_SID_TYPE_WinCreatorOwnerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 3
WELL_KNOWN_SID_TYPE_WinCreatorGroupSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 4
WELL_KNOWN_SID_TYPE_WinCreatorOwnerServerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 5
WELL_KNOWN_SID_TYPE_WinCreatorGroupServerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 6
WELL_KNOWN_SID_TYPE_WinNtAuthoritySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 7
WELL_KNOWN_SID_TYPE_WinDialupSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 8
WELL_KNOWN_SID_TYPE_WinNetworkSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 9
WELL_KNOWN_SID_TYPE_WinBatchSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 10
WELL_KNOWN_SID_TYPE_WinInteractiveSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 11
WELL_KNOWN_SID_TYPE_WinServiceSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 12
WELL_KNOWN_SID_TYPE_WinAnonymousSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 13
WELL_KNOWN_SID_TYPE_WinProxySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 14
WELL_KNOWN_SID_TYPE_WinEnterpriseControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 15
WELL_KNOWN_SID_TYPE_WinSelfSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 16
WELL_KNOWN_SID_TYPE_WinAuthenticatedUserSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 17
WELL_KNOWN_SID_TYPE_WinRestrictedCodeSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 18
WELL_KNOWN_SID_TYPE_WinTerminalServerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 19
WELL_KNOWN_SID_TYPE_WinRemoteLogonIdSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 20
WELL_KNOWN_SID_TYPE_WinLogonIdsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 21
WELL_KNOWN_SID_TYPE_WinLocalSystemSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 22
WELL_KNOWN_SID_TYPE_WinLocalServiceSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 23
WELL_KNOWN_SID_TYPE_WinNetworkServiceSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 24
WELL_KNOWN_SID_TYPE_WinBuiltinDomainSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 25
WELL_KNOWN_SID_TYPE_WinBuiltinAdministratorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 26
WELL_KNOWN_SID_TYPE_WinBuiltinUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 27
WELL_KNOWN_SID_TYPE_WinBuiltinGuestsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 28
WELL_KNOWN_SID_TYPE_WinBuiltinPowerUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 29
WELL_KNOWN_SID_TYPE_WinBuiltinAccountOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 30
WELL_KNOWN_SID_TYPE_WinBuiltinSystemOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 31
WELL_KNOWN_SID_TYPE_WinBuiltinPrintOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 32
WELL_KNOWN_SID_TYPE_WinBuiltinBackupOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 33
WELL_KNOWN_SID_TYPE_WinBuiltinReplicatorSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 34
WELL_KNOWN_SID_TYPE_WinBuiltinPreWindows2000CompatibleAccessSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 35
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteDesktopUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 36
WELL_KNOWN_SID_TYPE_WinBuiltinNetworkConfigurationOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 37
WELL_KNOWN_SID_TYPE_WinAccountAdministratorSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 38
WELL_KNOWN_SID_TYPE_WinAccountGuestSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 39
WELL_KNOWN_SID_TYPE_WinAccountKrbtgtSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 40
WELL_KNOWN_SID_TYPE_WinAccountDomainAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 41
WELL_KNOWN_SID_TYPE_WinAccountDomainUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 42
WELL_KNOWN_SID_TYPE_WinAccountDomainGuestsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 43
WELL_KNOWN_SID_TYPE_WinAccountComputersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 44
WELL_KNOWN_SID_TYPE_WinAccountControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 45
WELL_KNOWN_SID_TYPE_WinAccountCertAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 46
WELL_KNOWN_SID_TYPE_WinAccountSchemaAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 47
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 48
WELL_KNOWN_SID_TYPE_WinAccountPolicyAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 49
WELL_KNOWN_SID_TYPE_WinAccountRasAndIasServersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 50
WELL_KNOWN_SID_TYPE_WinNTLMAuthenticationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 51
WELL_KNOWN_SID_TYPE_WinDigestAuthenticationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 52
WELL_KNOWN_SID_TYPE_WinSChannelAuthenticationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 53
WELL_KNOWN_SID_TYPE_WinThisOrganizationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 54
WELL_KNOWN_SID_TYPE_WinOtherOrganizationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 55
WELL_KNOWN_SID_TYPE_WinBuiltinIncomingForestTrustBuildersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 56
WELL_KNOWN_SID_TYPE_WinBuiltinPerfMonitoringUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 57
WELL_KNOWN_SID_TYPE_WinBuiltinPerfLoggingUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 58
WELL_KNOWN_SID_TYPE_WinBuiltinAuthorizationAccessSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 59
WELL_KNOWN_SID_TYPE_WinBuiltinTerminalServerLicenseServersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 60
WELL_KNOWN_SID_TYPE_WinBuiltinDCOMUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 61
WELL_KNOWN_SID_TYPE_WinBuiltinIUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 62
WELL_KNOWN_SID_TYPE_WinIUserSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 63
WELL_KNOWN_SID_TYPE_WinBuiltinCryptoOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 64
WELL_KNOWN_SID_TYPE_WinUntrustedLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 65
WELL_KNOWN_SID_TYPE_WinLowLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 66
WELL_KNOWN_SID_TYPE_WinMediumLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 67
WELL_KNOWN_SID_TYPE_WinHighLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 68
WELL_KNOWN_SID_TYPE_WinSystemLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 69
WELL_KNOWN_SID_TYPE_WinWriteRestrictedCodeSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 70
WELL_KNOWN_SID_TYPE_WinCreatorOwnerRightsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 71
WELL_KNOWN_SID_TYPE_WinCacheablePrincipalsGroupSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 72
WELL_KNOWN_SID_TYPE_WinNonCacheablePrincipalsGroupSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 73
WELL_KNOWN_SID_TYPE_WinEnterpriseReadonlyControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 74
WELL_KNOWN_SID_TYPE_WinAccountReadonlyControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 75
WELL_KNOWN_SID_TYPE_WinBuiltinEventLogReadersGroup: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 76
WELL_KNOWN_SID_TYPE_WinNewEnterpriseReadonlyControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 77
WELL_KNOWN_SID_TYPE_WinBuiltinCertSvcDComAccessGroup: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 78
WELL_KNOWN_SID_TYPE_WinMediumPlusLabelSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 79
WELL_KNOWN_SID_TYPE_WinLocalLogonSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 80
WELL_KNOWN_SID_TYPE_WinConsoleLogonSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 81
WELL_KNOWN_SID_TYPE_WinThisOrganizationCertificateSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 82
WELL_KNOWN_SID_TYPE_WinApplicationPackageAuthoritySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 83
WELL_KNOWN_SID_TYPE_WinBuiltinAnyPackageSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 84
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 85
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientServerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 86
WELL_KNOWN_SID_TYPE_WinCapabilityPrivateNetworkClientServerSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 87
WELL_KNOWN_SID_TYPE_WinCapabilityPicturesLibrarySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 88
WELL_KNOWN_SID_TYPE_WinCapabilityVideosLibrarySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 89
WELL_KNOWN_SID_TYPE_WinCapabilityMusicLibrarySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 90
WELL_KNOWN_SID_TYPE_WinCapabilityDocumentsLibrarySid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 91
WELL_KNOWN_SID_TYPE_WinCapabilitySharedUserCertificatesSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 92
WELL_KNOWN_SID_TYPE_WinCapabilityEnterpriseAuthenticationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 93
WELL_KNOWN_SID_TYPE_WinCapabilityRemovableStorageSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 94
WELL_KNOWN_SID_TYPE_WinBuiltinRDSRemoteAccessServersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 95
WELL_KNOWN_SID_TYPE_WinBuiltinRDSEndpointServersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 96
WELL_KNOWN_SID_TYPE_WinBuiltinRDSManagementServersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 97
WELL_KNOWN_SID_TYPE_WinUserModeDriversSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 98
WELL_KNOWN_SID_TYPE_WinBuiltinHyperVAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 99
WELL_KNOWN_SID_TYPE_WinAccountCloneableControllersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 100
WELL_KNOWN_SID_TYPE_WinBuiltinAccessControlAssistanceOperatorsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 101
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteManagementUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 102
WELL_KNOWN_SID_TYPE_WinAuthenticationAuthorityAssertedSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 103
WELL_KNOWN_SID_TYPE_WinAuthenticationServiceAssertedSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 104
WELL_KNOWN_SID_TYPE_WinLocalAccountSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 105
WELL_KNOWN_SID_TYPE_WinLocalAccountAndAdministratorSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 106
WELL_KNOWN_SID_TYPE_WinAccountProtectedUsersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 107
WELL_KNOWN_SID_TYPE_WinCapabilityAppointmentsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 108
WELL_KNOWN_SID_TYPE_WinCapabilityContactsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 109
WELL_KNOWN_SID_TYPE_WinAccountDefaultSystemManagedSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 110
WELL_KNOWN_SID_TYPE_WinBuiltinDefaultSystemManagedGroupSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 111
WELL_KNOWN_SID_TYPE_WinBuiltinStorageReplicaAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 112
WELL_KNOWN_SID_TYPE_WinAccountKeyAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 113
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseKeyAdminsSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 114
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyTrustSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 115
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyMFASid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 116
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyAttestationSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 117
WELL_KNOWN_SID_TYPE_WinAuthenticationFreshKeyAuthSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 118
WELL_KNOWN_SID_TYPE_WinBuiltinDeviceOwnersSid: win32more.Windows.Win32.Security.WELL_KNOWN_SID_TYPE = 119


make_ready(__name__)
