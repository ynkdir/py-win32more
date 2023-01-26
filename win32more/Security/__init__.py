from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class ACCESS_ALLOWED_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_ALLOWED_CALLBACK_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_ALLOWED_CALLBACK_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_ALLOWED_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_DENIED_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_DENIED_CALLBACK_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class ACCESS_DENIED_CALLBACK_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_DENIED_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class ACCESS_REASONS(Structure):
    Data: UInt32 * 32
ACE_FLAGS = UInt32
CONTAINER_INHERIT_ACE: ACE_FLAGS = 2
FAILED_ACCESS_ACE_FLAG: ACE_FLAGS = 128
INHERIT_ONLY_ACE: ACE_FLAGS = 8
INHERITED_ACE: ACE_FLAGS = 16
NO_PROPAGATE_INHERIT_ACE: ACE_FLAGS = 4
OBJECT_INHERIT_ACE: ACE_FLAGS = 1
SUCCESSFUL_ACCESS_ACE_FLAG: ACE_FLAGS = 64
SUB_CONTAINERS_AND_OBJECTS_INHERIT: ACE_FLAGS = 3
SUB_CONTAINERS_ONLY_INHERIT: ACE_FLAGS = 2
SUB_OBJECTS_ONLY_INHERIT: ACE_FLAGS = 1
INHERIT_NO_PROPAGATE: ACE_FLAGS = 4
INHERIT_ONLY: ACE_FLAGS = 8
NO_INHERITANCE: ACE_FLAGS = 0
class ACE_HEADER(Structure):
    AceType: Byte
    AceFlags: Byte
    AceSize: UInt16
ACE_REVISION = UInt32
ACL_REVISION: ACE_REVISION = 2
ACL_REVISION_DS: ACE_REVISION = 4
class ACL(Structure):
    AclRevision: Byte
    Sbz1: Byte
    AclSize: UInt16
    AceCount: UInt16
    Sbz2: UInt16
ACL_INFORMATION_CLASS = Int32
ACL_INFORMATION_CLASS_AclRevisionInformation: ACL_INFORMATION_CLASS = 1
ACL_INFORMATION_CLASS_AclSizeInformation: ACL_INFORMATION_CLASS = 2
class ACL_REVISION_INFORMATION(Structure):
    AclRevision: UInt32
class ACL_SIZE_INFORMATION(Structure):
    AceCount: UInt32
    AclBytesInUse: UInt32
    AclBytesFree: UInt32
SECURITY_DYNAMIC_TRACKING: win32more.Foundation.BOOLEAN = 1
SECURITY_STATIC_TRACKING: win32more.Foundation.BOOLEAN = 0
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
def AccessCheck(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), PrivilegeSet: POINTER(win32more.Security.PRIVILEGE_SET_head), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckAndAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PWSTR, ObjectName: win32more.Foundation.PWSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByType(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), PrivilegeSet: POINTER(win32more.Security.PRIVILEGE_SET_head), PrivilegeSetLength: POINTER(UInt32), GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultList(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), PrivilegeSet: POINTER(win32more.Security.PRIVILEGE_SET_head), PrivilegeSetLength: POINTER(UInt32), GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeAndAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PWSTR, ObjectName: win32more.Foundation.PWSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PWSTR, ObjectName: win32more.Foundation.PWSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmByHandleW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ClientToken: win32more.Foundation.HANDLE, ObjectTypeName: win32more.Foundation.PWSTR, ObjectName: win32more.Foundation.PWSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccessList: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AccessMask: UInt32, pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedAceEx(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessAllowedObjectAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AccessMask: UInt32, pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedAceEx(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAccessDeniedObjectAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, dwStartingAceIndex: UInt32, pAceList: c_void_p, nAceListLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, dwAccessMask: UInt32, pSid: win32more.Foundation.PSID, bAuditSuccess: win32more.Foundation.BOOL, bAuditFailure: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessAceEx(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, dwAccessMask: UInt32, pSid: win32more.Foundation.PSID, bAuditSuccess: win32more.Foundation.BOOL, bAuditFailure: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddAuditAccessObjectAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, ObjectTypeGuid: POINTER(Guid), InheritedObjectTypeGuid: POINTER(Guid), pSid: win32more.Foundation.PSID, bAuditSuccess: win32more.Foundation.BOOL, bAuditFailure: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddMandatoryAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, MandatoryPolicy: UInt32, pLabelSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddResourceAttributeAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Foundation.PSID, pAttributeInfo: POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTES_INFORMATION_head), pReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddScopedPolicyIDAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AccessMask: UInt32, pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AdjustTokenGroups(TokenHandle: win32more.Foundation.HANDLE, ResetToDefault: win32more.Foundation.BOOL, NewState: POINTER(win32more.Security.TOKEN_GROUPS_head), BufferLength: UInt32, PreviousState: POINTER(win32more.Security.TOKEN_GROUPS_head), ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AdjustTokenPrivileges(TokenHandle: win32more.Foundation.HANDLE, DisableAllPrivileges: win32more.Foundation.BOOL, NewState: POINTER(win32more.Security.TOKEN_PRIVILEGES_head), BufferLength: UInt32, PreviousState: POINTER(win32more.Security.TOKEN_PRIVILEGES_head), ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AllocateAndInitializeSid(pIdentifierAuthority: POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head), nSubAuthorityCount: Byte, nSubAuthority0: UInt32, nSubAuthority1: UInt32, nSubAuthority2: UInt32, nSubAuthority3: UInt32, nSubAuthority4: UInt32, nSubAuthority5: UInt32, nSubAuthority6: UInt32, nSubAuthority7: UInt32, pSid: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AllocateLocallyUniqueId(Luid: POINTER(win32more.Foundation.LUID_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AreAllAccessesGranted(GrantedAccess: UInt32, DesiredAccess: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AreAnyAccessesGranted(GrantedAccess: UInt32, DesiredAccess: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CheckTokenMembership(TokenHandle: win32more.Foundation.HANDLE, SidToCheck: win32more.Foundation.PSID, IsMember: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckTokenCapability(TokenHandle: win32more.Foundation.HANDLE, CapabilitySidToCheck: win32more.Foundation.PSID, HasCapability: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetAppContainerAce(Acl: POINTER(win32more.Security.ACL_head), StartingAceIndex: UInt32, AppContainerAce: POINTER(c_void_p), AppContainerAceIndex: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CheckTokenMembershipEx(TokenHandle: win32more.Foundation.HANDLE, SidToCheck: win32more.Foundation.PSID, Flags: UInt32, IsMember: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertToAutoInheritPrivateObjectSecurity(ParentDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, CurrentSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, NewSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), ObjectType: POINTER(Guid), IsDirectoryObject: win32more.Foundation.BOOLEAN, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CopySid(nDestinationSidLength: UInt32, pDestinationSid: win32more.Foundation.PSID, pSourceSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurity(ParentDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), IsDirectoryObject: win32more.Foundation.BOOL, Token: win32more.Foundation.HANDLE, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurityEx(ParentDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), ObjectType: POINTER(Guid), IsContainerObject: win32more.Foundation.BOOL, AutoInheritFlags: win32more.Security.SECURITY_AUTO_INHERIT_FLAGS, Token: win32more.Foundation.HANDLE, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreatePrivateObjectSecurityWithMultipleInheritance(ParentDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, CreatorDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, NewDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), ObjectTypes: POINTER(POINTER(Guid)), GuidCount: UInt32, IsContainerObject: win32more.Foundation.BOOL, AutoInheritFlags: win32more.Security.SECURITY_AUTO_INHERIT_FLAGS, Token: win32more.Foundation.HANDLE, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateRestrictedToken(ExistingTokenHandle: win32more.Foundation.HANDLE, Flags: win32more.Security.CREATE_RESTRICTED_TOKEN_FLAGS, DisableSidCount: UInt32, SidsToDisable: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head), DeletePrivilegeCount: UInt32, PrivilegesToDelete: POINTER(win32more.Security.LUID_AND_ATTRIBUTES_head), RestrictedSidCount: UInt32, SidsToRestrict: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head), NewTokenHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def CreateWellKnownSid(WellKnownSidType: win32more.Security.WELL_KNOWN_SID_TYPE, DomainSid: win32more.Foundation.PSID, pSid: win32more.Foundation.PSID, cbSid: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualDomainSid(pSid1: win32more.Foundation.PSID, pSid2: win32more.Foundation.PSID, pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DeleteAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceIndex: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DestroyPrivateObjectSecurity(ObjectDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateToken(ExistingTokenHandle: win32more.Foundation.HANDLE, ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL, DuplicateTokenHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def DuplicateTokenEx(hExistingToken: win32more.Foundation.HANDLE, dwDesiredAccess: win32more.Security.TOKEN_ACCESS_MASK, lpTokenAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL, TokenType: win32more.Security.TOKEN_TYPE, phNewToken: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualPrefixSid(pSid1: win32more.Foundation.PSID, pSid2: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EqualSid(pSid1: win32more.Foundation.PSID, pSid2: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FindFirstFreeAce(pAcl: POINTER(win32more.Security.ACL_head), pAce: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def FreeSid(pSid: win32more.Foundation.PSID) -> c_void_p: ...
@winfunctype('ADVAPI32.dll')
def GetAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceIndex: UInt32, pAce: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetAclInformation(pAcl: POINTER(win32more.Security.ACL_head), pAclInformation: c_void_p, nAclInformationLength: UInt32, dwAclInformationClass: win32more.Security.ACL_INFORMATION_CLASS) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetFileSecurityW(lpFileName: win32more.Foundation.PWSTR, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetKernelObjectSecurity(Handle: win32more.Foundation.HANDLE, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetLengthSid(pSid: win32more.Foundation.PSID) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetPrivateObjectSecurity(ObjectDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, SecurityInformation: UInt32, ResultantDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, DescriptorLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorControl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pControl: POINTER(UInt16), lpdwRevision: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorDacl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, lpbDaclPresent: POINTER(Int32), pDacl: POINTER(POINTER(win32more.Security.ACL_head)), lpbDaclDefaulted: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorGroup(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pGroup: POINTER(win32more.Foundation.PSID), lpbGroupDefaulted: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorLength(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorOwner(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pOwner: POINTER(win32more.Foundation.PSID), lpbOwnerDefaulted: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorRMControl(SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, RMControl: c_char_p_no) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityDescriptorSacl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, lpbSaclPresent: POINTER(Int32), pSacl: POINTER(POINTER(win32more.Security.ACL_head)), lpbSaclDefaulted: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetSidIdentifierAuthority(pSid: win32more.Foundation.PSID) -> POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head): ...
@winfunctype('ADVAPI32.dll')
def GetSidLengthRequired(nSubAuthorityCount: Byte) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetSidSubAuthority(pSid: win32more.Foundation.PSID, nSubAuthority: UInt32) -> POINTER(UInt32): ...
@winfunctype('ADVAPI32.dll')
def GetSidSubAuthorityCount(pSid: win32more.Foundation.PSID) -> c_char_p_no: ...
@winfunctype('ADVAPI32.dll')
def GetTokenInformation(TokenHandle: win32more.Foundation.HANDLE, TokenInformationClass: win32more.Security.TOKEN_INFORMATION_CLASS, TokenInformation: c_void_p, TokenInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetWindowsAccountDomainSid(pSid: win32more.Foundation.PSID, pDomainSid: win32more.Foundation.PSID, cbDomainSid: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateAnonymousToken(ThreadHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateLoggedOnUser(hToken: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ImpersonateSelf(ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeAcl(pAcl: POINTER(win32more.Security.ACL_head), nAclLength: UInt32, dwAclRevision: win32more.Security.ACE_REVISION) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeSecurityDescriptor(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, dwRevision: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitializeSid(Sid: win32more.Foundation.PSID, pIdentifierAuthority: POINTER(win32more.Security.SID_IDENTIFIER_AUTHORITY_head), nSubAuthorityCount: Byte) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsTokenRestricted(TokenHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidAcl(pAcl: POINTER(win32more.Security.ACL_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidSecurityDescriptor(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsValidSid(pSid: win32more.Foundation.PSID) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def IsWellKnownSid(pSid: win32more.Foundation.PSID, WellKnownSidType: win32more.Security.WELL_KNOWN_SID_TYPE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MakeAbsoluteSD(pSelfRelativeSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pAbsoluteSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, lpdwAbsoluteSecurityDescriptorSize: POINTER(UInt32), pDacl: POINTER(win32more.Security.ACL_head), lpdwDaclSize: POINTER(UInt32), pSacl: POINTER(win32more.Security.ACL_head), lpdwSaclSize: POINTER(UInt32), pOwner: win32more.Foundation.PSID, lpdwOwnerSize: POINTER(UInt32), pPrimaryGroup: win32more.Foundation.PSID, lpdwPrimaryGroupSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MakeSelfRelativeSD(pAbsoluteSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pSelfRelativeSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, lpdwBufferLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def MapGenericMask(AccessMask: POINTER(UInt32), GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def ObjectCloseAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, GenerateOnClose: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectDeleteAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, GenerateOnClose: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectOpenAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PWSTR, ObjectName: win32more.Foundation.PWSTR, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, GrantedAccess: UInt32, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), ObjectCreation: win32more.Foundation.BOOL, AccessGranted: win32more.Foundation.BOOL, GenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectPrivilegeAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, HandleId: c_void_p, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), AccessGranted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegeCheck(ClientToken: win32more.Foundation.HANDLE, RequiredPrivileges: POINTER(win32more.Security.PRIVILEGE_SET_head), pfResult: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegedServiceAuditAlarmW(SubsystemName: win32more.Foundation.PWSTR, ServiceName: win32more.Foundation.PWSTR, ClientToken: win32more.Foundation.HANDLE, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), AccessGranted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def QuerySecurityAccessMask(SecurityInformation: UInt32, DesiredAccess: POINTER(UInt32)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def RevertToSelf() -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetAclInformation(pAcl: POINTER(win32more.Security.ACL_head), pAclInformation: c_void_p, nAclInformationLength: UInt32, dwAclInformationClass: win32more.Security.ACL_INFORMATION_CLASS) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetFileSecurityW(lpFileName: win32more.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetKernelObjectSecurity(Handle: win32more.Foundation.HANDLE, SecurityInformation: UInt32, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetPrivateObjectSecurity(SecurityInformation: UInt32, ModificationDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ObjectsSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), Token: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetPrivateObjectSecurityEx(SecurityInformation: UInt32, ModificationDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ObjectsSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), AutoInheritFlags: win32more.Security.SECURITY_AUTO_INHERIT_FLAGS, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), Token: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityAccessMask(SecurityInformation: UInt32, DesiredAccess: POINTER(UInt32)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorControl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ControlBitsOfInterest: win32more.Security.SECURITY_DESCRIPTOR_CONTROL, ControlBitsToSet: win32more.Security.SECURITY_DESCRIPTOR_CONTROL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorDacl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, bDaclPresent: win32more.Foundation.BOOL, pDacl: POINTER(win32more.Security.ACL_head), bDaclDefaulted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorGroup(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pGroup: win32more.Foundation.PSID, bGroupDefaulted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorOwner(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, pOwner: win32more.Foundation.PSID, bOwnerDefaulted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorRMControl(SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, RMControl: c_char_p_no) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityDescriptorSacl(pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, bSaclPresent: win32more.Foundation.BOOL, pSacl: POINTER(win32more.Security.ACL_head), bSaclDefaulted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetTokenInformation(TokenHandle: win32more.Foundation.HANDLE, TokenInformationClass: win32more.Security.TOKEN_INFORMATION_CLASS, TokenInformation: c_void_p, TokenInformationLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCachedSigningLevel(SourceFiles: POINTER(win32more.Foundation.HANDLE), SourceFileCount: UInt32, Flags: UInt32, TargetFile: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCachedSigningLevel(File: win32more.Foundation.HANDLE, Flags: POINTER(UInt32), SigningLevel: POINTER(UInt32), Thumbprint: c_char_p_no, ThumbprintSize: POINTER(UInt32), ThumbprintAlgorithm: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-security-base-l1-2-2.dll')
def DeriveCapabilitySidsFromName(CapName: win32more.Foundation.PWSTR, CapabilityGroupSids: POINTER(POINTER(win32more.Foundation.PSID)), CapabilityGroupSidCount: POINTER(UInt32), CapabilitySids: POINTER(POINTER(win32more.Foundation.PSID)), CapabilitySidCount: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ntdll.dll')
def RtlNormalizeSecurityDescriptor(SecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorLength: UInt32, NewSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), NewSecurityDescriptorLength: POINTER(UInt32), CheckOnly: win32more.Foundation.BOOLEAN) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('USER32.dll')
def SetUserObjectSecurity(hObj: win32more.Foundation.HANDLE, pSIRequested: POINTER(win32more.Security.OBJECT_SECURITY_INFORMATION), pSID: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUserObjectSecurity(hObj: win32more.Foundation.HANDLE, pSIRequested: POINTER(UInt32), pSID: win32more.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckAndAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PSTR, ObjectName: win32more.Foundation.PSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, DesiredAccess: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeAndAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PSTR, ObjectName: win32more.Foundation.PSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatus: POINTER(Int32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PSTR, ObjectName: win32more.Foundation.PSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AccessCheckByTypeResultListAndAuditAlarmByHandleA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ClientToken: win32more.Foundation.HANDLE, ObjectTypeName: win32more.Foundation.PSTR, ObjectName: win32more.Foundation.PSTR, SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, PrincipalSelfSid: win32more.Foundation.PSID, DesiredAccess: UInt32, AuditType: win32more.Security.AUDIT_EVENT_TYPE, Flags: UInt32, ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head), ObjectTypeListLength: UInt32, GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head), ObjectCreation: win32more.Foundation.BOOL, GrantedAccess: POINTER(UInt32), AccessStatusList: POINTER(UInt32), pfGenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectOpenAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ObjectTypeName: win32more.Foundation.PSTR, ObjectName: win32more.Foundation.PSTR, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, GrantedAccess: UInt32, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), ObjectCreation: win32more.Foundation.BOOL, AccessGranted: win32more.Foundation.BOOL, GenerateOnClose: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectPrivilegeAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, ClientToken: win32more.Foundation.HANDLE, DesiredAccess: UInt32, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), AccessGranted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectCloseAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, GenerateOnClose: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ObjectDeleteAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, HandleId: c_void_p, GenerateOnClose: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def PrivilegedServiceAuditAlarmA(SubsystemName: win32more.Foundation.PSTR, ServiceName: win32more.Foundation.PSTR, ClientToken: win32more.Foundation.HANDLE, Privileges: POINTER(win32more.Security.PRIVILEGE_SET_head), AccessGranted: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AddConditionalAce(pAcl: POINTER(win32more.Security.ACL_head), dwAceRevision: win32more.Security.ACE_REVISION, AceFlags: win32more.Security.ACE_FLAGS, AceType: Byte, AccessMask: UInt32, pSid: win32more.Foundation.PSID, ConditionStr: win32more.Foundation.PWSTR, ReturnLength: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetFileSecurityA(lpFileName: win32more.Foundation.PSTR, SecurityInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def GetFileSecurityA(lpFileName: win32more.Foundation.PSTR, RequestedInformation: UInt32, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountSidA(lpSystemName: win32more.Foundation.PSTR, Sid: win32more.Foundation.PSID, Name: win32more.Foundation.PSTR, cchName: POINTER(UInt32), ReferencedDomainName: win32more.Foundation.PSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Security.SID_NAME_USE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountSidW(lpSystemName: win32more.Foundation.PWSTR, Sid: win32more.Foundation.PSID, Name: win32more.Foundation.PWSTR, cchName: POINTER(UInt32), ReferencedDomainName: win32more.Foundation.PWSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Security.SID_NAME_USE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountNameA(lpSystemName: win32more.Foundation.PSTR, lpAccountName: win32more.Foundation.PSTR, Sid: win32more.Foundation.PSID, cbSid: POINTER(UInt32), ReferencedDomainName: win32more.Foundation.PSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Security.SID_NAME_USE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupAccountNameW(lpSystemName: win32more.Foundation.PWSTR, lpAccountName: win32more.Foundation.PWSTR, Sid: win32more.Foundation.PSID, cbSid: POINTER(UInt32), ReferencedDomainName: win32more.Foundation.PWSTR, cchReferencedDomainName: POINTER(UInt32), peUse: POINTER(win32more.Security.SID_NAME_USE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeValueA(lpSystemName: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, lpLuid: POINTER(win32more.Foundation.LUID_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeValueW(lpSystemName: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lpLuid: POINTER(win32more.Foundation.LUID_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeNameA(lpSystemName: win32more.Foundation.PSTR, lpLuid: POINTER(win32more.Foundation.LUID_head), lpName: win32more.Foundation.PSTR, cchName: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeNameW(lpSystemName: win32more.Foundation.PWSTR, lpLuid: POINTER(win32more.Foundation.LUID_head), lpName: win32more.Foundation.PWSTR, cchName: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeDisplayNameA(lpSystemName: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, lpDisplayName: win32more.Foundation.PSTR, cchDisplayName: POINTER(UInt32), lpLanguageId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LookupPrivilegeDisplayNameW(lpSystemName: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lpDisplayName: win32more.Foundation.PWSTR, cchDisplayName: POINTER(UInt32), lpLanguageId: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserA(lpszUsername: win32more.Foundation.PSTR, lpszDomain: win32more.Foundation.PSTR, lpszPassword: win32more.Foundation.PSTR, dwLogonType: win32more.Security.LOGON32_LOGON, dwLogonProvider: win32more.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserW(lpszUsername: win32more.Foundation.PWSTR, lpszDomain: win32more.Foundation.PWSTR, lpszPassword: win32more.Foundation.PWSTR, dwLogonType: win32more.Security.LOGON32_LOGON, dwLogonProvider: win32more.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserExA(lpszUsername: win32more.Foundation.PSTR, lpszDomain: win32more.Foundation.PSTR, lpszPassword: win32more.Foundation.PSTR, dwLogonType: win32more.Security.LOGON32_LOGON, dwLogonProvider: win32more.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Foundation.HANDLE), ppLogonSid: POINTER(win32more.Foundation.PSID), ppProfileBuffer: POINTER(c_void_p), pdwProfileLength: POINTER(UInt32), pQuotaLimits: POINTER(win32more.Security.QUOTA_LIMITS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def LogonUserExW(lpszUsername: win32more.Foundation.PWSTR, lpszDomain: win32more.Foundation.PWSTR, lpszPassword: win32more.Foundation.PWSTR, dwLogonType: win32more.Security.LOGON32_LOGON, dwLogonProvider: win32more.Security.LOGON32_PROVIDER, phToken: POINTER(win32more.Foundation.HANDLE), ppLogonSid: POINTER(win32more.Foundation.PSID), ppProfileBuffer: POINTER(c_void_p), pdwProfileLength: POINTER(UInt32), pQuotaLimits: POINTER(win32more.Security.QUOTA_LIMITS_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ntdll.dll')
def RtlConvertSidToUnicodeString(UnicodeString: POINTER(win32more.Foundation.UNICODE_STRING_head), Sid: win32more.Foundation.PSID, AllocateDestinationString: win32more.Foundation.BOOLEAN) -> win32more.Foundation.NTSTATUS: ...
AUDIT_EVENT_TYPE = Int32
AUDIT_EVENT_TYPE_AuditEventObjectAccess: AUDIT_EVENT_TYPE = 0
AUDIT_EVENT_TYPE_AuditEventDirectoryServiceAccess: AUDIT_EVENT_TYPE = 1
CLAIM_SECURITY_ATTRIBUTE_FLAGS = UInt32
CLAIM_SECURITY_ATTRIBUTE_NON_INHERITABLE: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 1
CLAIM_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 2
CLAIM_SECURITY_ATTRIBUTE_USE_FOR_DENY_ONLY: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 4
CLAIM_SECURITY_ATTRIBUTE_DISABLED_BY_DEFAULT: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 8
CLAIM_SECURITY_ATTRIBUTE_DISABLED: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 16
CLAIM_SECURITY_ATTRIBUTE_MANDATORY: CLAIM_SECURITY_ATTRIBUTE_FLAGS = 32
class CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE(Structure):
    Version: UInt64
    Name: win32more.Foundation.PWSTR
class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(Structure):
    pValue: c_void_p
    ValueLength: UInt32
class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(Structure):
    Name: UInt32
    ValueType: win32more.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE
    Reserved: UInt16
    Flags: win32more.Security.CLAIM_SECURITY_ATTRIBUTE_FLAGS
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(Union):
        pInt64: UInt32 * 1
        pUint64: UInt32 * 1
        ppString: UInt32 * 1
        pFqbn: UInt32 * 1
        pOctetString: UInt32 * 1
class CLAIM_SECURITY_ATTRIBUTE_V1(Structure):
    Name: win32more.Foundation.PWSTR
    ValueType: win32more.Security.CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE
    Reserved: UInt16
    Flags: UInt32
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(Union):
        pInt64: POINTER(Int64)
        pUint64: POINTER(UInt64)
        ppString: POINTER(win32more.Foundation.PWSTR)
        pFqbn: POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE_head)
        pOctetString: POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head)
CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = UInt16
CLAIM_SECURITY_ATTRIBUTE_TYPE_INT64: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 1
CLAIM_SECURITY_ATTRIBUTE_TYPE_UINT64: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 2
CLAIM_SECURITY_ATTRIBUTE_TYPE_STRING: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 3
CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 16
CLAIM_SECURITY_ATTRIBUTE_TYPE_FQBN: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 4
CLAIM_SECURITY_ATTRIBUTE_TYPE_SID: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 5
CLAIM_SECURITY_ATTRIBUTE_TYPE_BOOLEAN: CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE = 6
class CLAIM_SECURITY_ATTRIBUTES_INFORMATION(Structure):
    Version: UInt16
    Reserved: UInt16
    AttributeCount: UInt32
    Attribute: _Attribute_e__Union
    class _Attribute_e__Union(Union):
        pAttributeV1: POINTER(win32more.Security.CLAIM_SECURITY_ATTRIBUTE_V1_head)
CREATE_RESTRICTED_TOKEN_FLAGS = UInt32
DISABLE_MAX_PRIVILEGE: CREATE_RESTRICTED_TOKEN_FLAGS = 1
SANDBOX_INERT: CREATE_RESTRICTED_TOKEN_FLAGS = 2
LUA_TOKEN: CREATE_RESTRICTED_TOKEN_FLAGS = 4
WRITE_RESTRICTED: CREATE_RESTRICTED_TOKEN_FLAGS = 8
ENUM_PERIOD = Int32
ENUM_PERIOD_INVALID: ENUM_PERIOD = -1
ENUM_PERIOD_SECONDS: ENUM_PERIOD = 0
ENUM_PERIOD_MINUTES: ENUM_PERIOD = 1
ENUM_PERIOD_HOURS: ENUM_PERIOD = 2
ENUM_PERIOD_DAYS: ENUM_PERIOD = 3
ENUM_PERIOD_WEEKS: ENUM_PERIOD = 4
ENUM_PERIOD_MONTHS: ENUM_PERIOD = 5
ENUM_PERIOD_YEARS: ENUM_PERIOD = 6
class GENERIC_MAPPING(Structure):
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
class LLFILETIME(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ll: Int64
        ft: win32more.Foundation.FILETIME
LOGON32_LOGON = UInt32
LOGON32_LOGON_BATCH: LOGON32_LOGON = 4
LOGON32_LOGON_INTERACTIVE: LOGON32_LOGON = 2
LOGON32_LOGON_NETWORK: LOGON32_LOGON = 3
LOGON32_LOGON_NETWORK_CLEARTEXT: LOGON32_LOGON = 8
LOGON32_LOGON_NEW_CREDENTIALS: LOGON32_LOGON = 9
LOGON32_LOGON_SERVICE: LOGON32_LOGON = 5
LOGON32_LOGON_UNLOCK: LOGON32_LOGON = 7
LOGON32_PROVIDER = UInt32
LOGON32_PROVIDER_DEFAULT: LOGON32_PROVIDER = 0
LOGON32_PROVIDER_WINNT50: LOGON32_PROVIDER = 3
LOGON32_PROVIDER_WINNT40: LOGON32_PROVIDER = 2
class LUID_AND_ATTRIBUTES(Structure):
    Luid: win32more.Foundation.LUID
    Attributes: win32more.Security.TOKEN_PRIVILEGES_ATTRIBUTES
MANDATORY_LEVEL = Int32
MANDATORY_LEVEL_MandatoryLevelUntrusted: MANDATORY_LEVEL = 0
MANDATORY_LEVEL_MandatoryLevelLow: MANDATORY_LEVEL = 1
MANDATORY_LEVEL_MandatoryLevelMedium: MANDATORY_LEVEL = 2
MANDATORY_LEVEL_MandatoryLevelHigh: MANDATORY_LEVEL = 3
MANDATORY_LEVEL_MandatoryLevelSystem: MANDATORY_LEVEL = 4
MANDATORY_LEVEL_MandatoryLevelSecureProcess: MANDATORY_LEVEL = 5
MANDATORY_LEVEL_MandatoryLevelCount: MANDATORY_LEVEL = 6
NCRYPT_DESCRIPTOR_HANDLE = IntPtr
NCRYPT_STREAM_HANDLE = IntPtr
OBJECT_SECURITY_INFORMATION = UInt32
ATTRIBUTE_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 32
BACKUP_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 65536
DACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 4
GROUP_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 2
LABEL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 16
OWNER_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 1
PROTECTED_DACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 2147483648
PROTECTED_SACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 1073741824
SACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 8
SCOPE_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 64
UNPROTECTED_DACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 536870912
UNPROTECTED_SACL_SECURITY_INFORMATION: OBJECT_SECURITY_INFORMATION = 268435456
class OBJECT_TYPE_LIST(Structure):
    Level: UInt16
    Sbz: UInt16
    ObjectType: POINTER(Guid)
@winfunctype_pointer
def PLSA_AP_CALL_PACKAGE_UNTRUSTED(ClientRequest: POINTER(c_void_p), ProtocolSubmitBuffer: c_void_p, ClientBufferBase: c_void_p, SubmitBufferLength: UInt32, ProtocolReturnBuffer: POINTER(c_void_p), ReturnBufferLength: POINTER(UInt32), ProtocolStatus: POINTER(Int32)) -> win32more.Foundation.NTSTATUS: ...
class PRIVILEGE_SET(Structure):
    PrivilegeCount: UInt32
    Control: UInt32
    Privilege: win32more.Security.LUID_AND_ATTRIBUTES * 1
PSECURITY_DESCRIPTOR = c_void_p
class QUOTA_LIMITS(Structure):
    PagedPoolLimit: UIntPtr
    NonPagedPoolLimit: UIntPtr
    MinimumWorkingSetSize: UIntPtr
    MaximumWorkingSetSize: UIntPtr
    PagefileLimit: UIntPtr
    TimeLimit: win32more.Foundation.LARGE_INTEGER
SAFER_LEVEL_HANDLE = IntPtr
SC_HANDLE = IntPtr
class SE_ACCESS_REPLY(Structure):
    Size: UInt32
    ResultListCount: UInt32
    GrantedAccess: POINTER(UInt32)
    AccessStatus: POINTER(UInt32)
    AccessReason: POINTER(win32more.Security.ACCESS_REASONS_head)
    Privileges: POINTER(POINTER(win32more.Security.PRIVILEGE_SET_head))
class SE_ACCESS_REQUEST(Structure):
    Size: UInt32
    SeSecurityDescriptor: POINTER(win32more.Security.SE_SECURITY_DESCRIPTOR_head)
    DesiredAccess: UInt32
    PreviouslyGrantedAccess: UInt32
    PrincipalSelfSid: win32more.Foundation.PSID
    GenericMapping: POINTER(win32more.Security.GENERIC_MAPPING_head)
    ObjectTypeListCount: UInt32
    ObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head)
class SE_IMPERSONATION_STATE(Structure):
    Token: c_void_p
    CopyOnOpen: win32more.Foundation.BOOLEAN
    EffectiveOnly: win32more.Foundation.BOOLEAN
    Level: win32more.Security.SECURITY_IMPERSONATION_LEVEL
class SE_SECURITY_DESCRIPTOR(Structure):
    Size: UInt32
    Flags: UInt32
    SecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR
class SE_SID(Union):
    Sid: win32more.Security.SID
    Buffer: Byte * 68
@winfunctype_pointer
def SEC_THREAD_START(lpThreadParameter: c_void_p) -> UInt32: ...
class SECURITY_ATTRIBUTES(Structure):
    nLength: UInt32
    lpSecurityDescriptor: c_void_p
    bInheritHandle: win32more.Foundation.BOOL
SECURITY_AUTO_INHERIT_FLAGS = UInt32
SEF_AVOID_OWNER_CHECK: SECURITY_AUTO_INHERIT_FLAGS = 16
SEF_AVOID_OWNER_RESTRICTION: SECURITY_AUTO_INHERIT_FLAGS = 4096
SEF_AVOID_PRIVILEGE_CHECK: SECURITY_AUTO_INHERIT_FLAGS = 8
SEF_DACL_AUTO_INHERIT: SECURITY_AUTO_INHERIT_FLAGS = 1
SEF_DEFAULT_DESCRIPTOR_FOR_OBJECT: SECURITY_AUTO_INHERIT_FLAGS = 4
SEF_DEFAULT_GROUP_FROM_PARENT: SECURITY_AUTO_INHERIT_FLAGS = 64
SEF_DEFAULT_OWNER_FROM_PARENT: SECURITY_AUTO_INHERIT_FLAGS = 32
SEF_MACL_NO_EXECUTE_UP: SECURITY_AUTO_INHERIT_FLAGS = 1024
SEF_MACL_NO_READ_UP: SECURITY_AUTO_INHERIT_FLAGS = 512
SEF_MACL_NO_WRITE_UP: SECURITY_AUTO_INHERIT_FLAGS = 256
SEF_SACL_AUTO_INHERIT: SECURITY_AUTO_INHERIT_FLAGS = 2
class SECURITY_CAPABILITIES(Structure):
    AppContainerSid: win32more.Foundation.PSID
    Capabilities: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)
    CapabilityCount: UInt32
    Reserved: UInt32
class SECURITY_DESCRIPTOR(Structure):
    Revision: Byte
    Sbz1: Byte
    Control: win32more.Security.SECURITY_DESCRIPTOR_CONTROL
    Owner: win32more.Foundation.PSID
    Group: win32more.Foundation.PSID
    Sacl: POINTER(win32more.Security.ACL_head)
    Dacl: POINTER(win32more.Security.ACL_head)
SECURITY_DESCRIPTOR_CONTROL = UInt16
SE_OWNER_DEFAULTED: SECURITY_DESCRIPTOR_CONTROL = 1
SE_GROUP_DEFAULTED: SECURITY_DESCRIPTOR_CONTROL = 2
SE_DACL_PRESENT: SECURITY_DESCRIPTOR_CONTROL = 4
SE_DACL_DEFAULTED: SECURITY_DESCRIPTOR_CONTROL = 8
SE_SACL_PRESENT: SECURITY_DESCRIPTOR_CONTROL = 16
SE_SACL_DEFAULTED: SECURITY_DESCRIPTOR_CONTROL = 32
SE_DACL_AUTO_INHERIT_REQ: SECURITY_DESCRIPTOR_CONTROL = 256
SE_SACL_AUTO_INHERIT_REQ: SECURITY_DESCRIPTOR_CONTROL = 512
SE_DACL_AUTO_INHERITED: SECURITY_DESCRIPTOR_CONTROL = 1024
SE_SACL_AUTO_INHERITED: SECURITY_DESCRIPTOR_CONTROL = 2048
SE_DACL_PROTECTED: SECURITY_DESCRIPTOR_CONTROL = 4096
SE_SACL_PROTECTED: SECURITY_DESCRIPTOR_CONTROL = 8192
SE_RM_CONTROL_VALID: SECURITY_DESCRIPTOR_CONTROL = 16384
SE_SELF_RELATIVE: SECURITY_DESCRIPTOR_CONTROL = 32768
class SECURITY_DESCRIPTOR_RELATIVE(Structure):
    Revision: Byte
    Sbz1: Byte
    Control: win32more.Security.SECURITY_DESCRIPTOR_CONTROL
    Owner: UInt32
    Group: UInt32
    Sacl: UInt32
    Dacl: UInt32
SECURITY_IMPERSONATION_LEVEL = Int32
SECURITY_IMPERSONATION_LEVEL_SecurityAnonymous: SECURITY_IMPERSONATION_LEVEL = 0
SECURITY_IMPERSONATION_LEVEL_SecurityIdentification: SECURITY_IMPERSONATION_LEVEL = 1
SECURITY_IMPERSONATION_LEVEL_SecurityImpersonation: SECURITY_IMPERSONATION_LEVEL = 2
SECURITY_IMPERSONATION_LEVEL_SecurityDelegation: SECURITY_IMPERSONATION_LEVEL = 3
class SECURITY_QUALITY_OF_SERVICE(Structure):
    Length: UInt32
    ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL
    ContextTrackingMode: Byte
    EffectiveOnly: win32more.Foundation.BOOLEAN
class SID(Structure):
    Revision: Byte
    SubAuthorityCount: Byte
    IdentifierAuthority: win32more.Security.SID_IDENTIFIER_AUTHORITY
    SubAuthority: UInt32 * 1
class SID_AND_ATTRIBUTES(Structure):
    Sid: win32more.Foundation.PSID
    Attributes: UInt32
class SID_AND_ATTRIBUTES_HASH(Structure):
    SidCount: UInt32
    SidAttr: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)
    Hash: UIntPtr * 32
class SID_IDENTIFIER_AUTHORITY(Structure):
    Value: Byte * 6
SID_NAME_USE = Int32
SID_NAME_USE_SidTypeUser: SID_NAME_USE = 1
SID_NAME_USE_SidTypeGroup: SID_NAME_USE = 2
SID_NAME_USE_SidTypeDomain: SID_NAME_USE = 3
SID_NAME_USE_SidTypeAlias: SID_NAME_USE = 4
SID_NAME_USE_SidTypeWellKnownGroup: SID_NAME_USE = 5
SID_NAME_USE_SidTypeDeletedAccount: SID_NAME_USE = 6
SID_NAME_USE_SidTypeInvalid: SID_NAME_USE = 7
SID_NAME_USE_SidTypeUnknown: SID_NAME_USE = 8
SID_NAME_USE_SidTypeComputer: SID_NAME_USE = 9
SID_NAME_USE_SidTypeLabel: SID_NAME_USE = 10
SID_NAME_USE_SidTypeLogonSession: SID_NAME_USE = 11
class SYSTEM_ACCESS_FILTER_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_CALLBACK_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_ALARM_CALLBACK_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_ALARM_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: UInt32
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_AUDIT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_AUDIT_CALLBACK_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_AUDIT_CALLBACK_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
class SYSTEM_AUDIT_OBJECT_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    Flags: win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Guid
    InheritedObjectType: Guid
    SidStart: UInt32
SYSTEM_AUDIT_OBJECT_ACE_FLAGS = UInt32
ACE_OBJECT_TYPE_PRESENT: SYSTEM_AUDIT_OBJECT_ACE_FLAGS = 1
ACE_INHERITED_OBJECT_TYPE_PRESENT: SYSTEM_AUDIT_OBJECT_ACE_FLAGS = 2
class SYSTEM_MANDATORY_LABEL_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_PROCESS_TRUST_LABEL_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_RESOURCE_ATTRIBUTE_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class SYSTEM_SCOPED_POLICY_ID_ACE(Structure):
    Header: win32more.Security.ACE_HEADER
    Mask: UInt32
    SidStart: UInt32
class TOKEN_ACCESS_INFORMATION(Structure):
    SidHash: POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)
    RestrictedSidHash: POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)
    Privileges: POINTER(win32more.Security.TOKEN_PRIVILEGES_head)
    AuthenticationId: win32more.Foundation.LUID
    TokenType: win32more.Security.TOKEN_TYPE
    ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL
    MandatoryPolicy: win32more.Security.TOKEN_MANDATORY_POLICY
    Flags: UInt32
    AppContainerNumber: UInt32
    PackageSid: win32more.Foundation.PSID
    CapabilitiesHash: POINTER(win32more.Security.SID_AND_ATTRIBUTES_HASH_head)
    TrustLevelSid: win32more.Foundation.PSID
    SecurityAttributes: c_void_p
TOKEN_ACCESS_MASK = UInt32
TOKEN_DELETE: TOKEN_ACCESS_MASK = 65536
TOKEN_READ_CONTROL: TOKEN_ACCESS_MASK = 131072
TOKEN_WRITE_DAC: TOKEN_ACCESS_MASK = 262144
TOKEN_WRITE_OWNER: TOKEN_ACCESS_MASK = 524288
TOKEN_ACCESS_SYSTEM_SECURITY: TOKEN_ACCESS_MASK = 16777216
TOKEN_ASSIGN_PRIMARY: TOKEN_ACCESS_MASK = 1
TOKEN_DUPLICATE: TOKEN_ACCESS_MASK = 2
TOKEN_IMPERSONATE: TOKEN_ACCESS_MASK = 4
TOKEN_QUERY: TOKEN_ACCESS_MASK = 8
TOKEN_QUERY_SOURCE: TOKEN_ACCESS_MASK = 16
TOKEN_ADJUST_PRIVILEGES: TOKEN_ACCESS_MASK = 32
TOKEN_ADJUST_GROUPS: TOKEN_ACCESS_MASK = 64
TOKEN_ADJUST_DEFAULT: TOKEN_ACCESS_MASK = 128
TOKEN_ADJUST_SESSIONID: TOKEN_ACCESS_MASK = 256
TOKEN_READ: TOKEN_ACCESS_MASK = 131080
TOKEN_WRITE: TOKEN_ACCESS_MASK = 131296
TOKEN_EXECUTE: TOKEN_ACCESS_MASK = 131072
TOKEN_TRUST_CONSTRAINT_MASK: TOKEN_ACCESS_MASK = 131096
TOKEN_ACCESS_PSEUDO_HANDLE_WIN8: TOKEN_ACCESS_MASK = 24
TOKEN_ACCESS_PSEUDO_HANDLE: TOKEN_ACCESS_MASK = 24
TOKEN_ALL_ACCESS: TOKEN_ACCESS_MASK = 983551
class TOKEN_APPCONTAINER_INFORMATION(Structure):
    TokenAppContainer: win32more.Foundation.PSID
class TOKEN_AUDIT_POLICY(Structure):
    PerUserPolicy: Byte * 30
class TOKEN_CONTROL(Structure):
    TokenId: win32more.Foundation.LUID
    AuthenticationId: win32more.Foundation.LUID
    ModifiedId: win32more.Foundation.LUID
    TokenSource: win32more.Security.TOKEN_SOURCE
class TOKEN_DEFAULT_DACL(Structure):
    DefaultDacl: POINTER(win32more.Security.ACL_head)
class TOKEN_DEVICE_CLAIMS(Structure):
    DeviceClaims: c_void_p
class TOKEN_ELEVATION(Structure):
    TokenIsElevated: UInt32
TOKEN_ELEVATION_TYPE = Int32
TOKEN_ELEVATION_TYPE_TokenElevationTypeDefault: TOKEN_ELEVATION_TYPE = 1
TOKEN_ELEVATION_TYPE_TokenElevationTypeFull: TOKEN_ELEVATION_TYPE = 2
TOKEN_ELEVATION_TYPE_TokenElevationTypeLimited: TOKEN_ELEVATION_TYPE = 3
class TOKEN_GROUPS(Structure):
    GroupCount: UInt32
    Groups: win32more.Security.SID_AND_ATTRIBUTES * 1
class TOKEN_GROUPS_AND_PRIVILEGES(Structure):
    SidCount: UInt32
    SidLength: UInt32
    Sids: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)
    RestrictedSidCount: UInt32
    RestrictedSidLength: UInt32
    RestrictedSids: POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)
    PrivilegeCount: UInt32
    PrivilegeLength: UInt32
    Privileges: POINTER(win32more.Security.LUID_AND_ATTRIBUTES_head)
    AuthenticationId: win32more.Foundation.LUID
TOKEN_INFORMATION_CLASS = Int32
TOKEN_INFORMATION_CLASS_TokenUser: TOKEN_INFORMATION_CLASS = 1
TOKEN_INFORMATION_CLASS_TokenGroups: TOKEN_INFORMATION_CLASS = 2
TOKEN_INFORMATION_CLASS_TokenPrivileges: TOKEN_INFORMATION_CLASS = 3
TOKEN_INFORMATION_CLASS_TokenOwner: TOKEN_INFORMATION_CLASS = 4
TOKEN_INFORMATION_CLASS_TokenPrimaryGroup: TOKEN_INFORMATION_CLASS = 5
TOKEN_INFORMATION_CLASS_TokenDefaultDacl: TOKEN_INFORMATION_CLASS = 6
TOKEN_INFORMATION_CLASS_TokenSource: TOKEN_INFORMATION_CLASS = 7
TOKEN_INFORMATION_CLASS_TokenType: TOKEN_INFORMATION_CLASS = 8
TOKEN_INFORMATION_CLASS_TokenImpersonationLevel: TOKEN_INFORMATION_CLASS = 9
TOKEN_INFORMATION_CLASS_TokenStatistics: TOKEN_INFORMATION_CLASS = 10
TOKEN_INFORMATION_CLASS_TokenRestrictedSids: TOKEN_INFORMATION_CLASS = 11
TOKEN_INFORMATION_CLASS_TokenSessionId: TOKEN_INFORMATION_CLASS = 12
TOKEN_INFORMATION_CLASS_TokenGroupsAndPrivileges: TOKEN_INFORMATION_CLASS = 13
TOKEN_INFORMATION_CLASS_TokenSessionReference: TOKEN_INFORMATION_CLASS = 14
TOKEN_INFORMATION_CLASS_TokenSandBoxInert: TOKEN_INFORMATION_CLASS = 15
TOKEN_INFORMATION_CLASS_TokenAuditPolicy: TOKEN_INFORMATION_CLASS = 16
TOKEN_INFORMATION_CLASS_TokenOrigin: TOKEN_INFORMATION_CLASS = 17
TOKEN_INFORMATION_CLASS_TokenElevationType: TOKEN_INFORMATION_CLASS = 18
TOKEN_INFORMATION_CLASS_TokenLinkedToken: TOKEN_INFORMATION_CLASS = 19
TOKEN_INFORMATION_CLASS_TokenElevation: TOKEN_INFORMATION_CLASS = 20
TOKEN_INFORMATION_CLASS_TokenHasRestrictions: TOKEN_INFORMATION_CLASS = 21
TOKEN_INFORMATION_CLASS_TokenAccessInformation: TOKEN_INFORMATION_CLASS = 22
TOKEN_INFORMATION_CLASS_TokenVirtualizationAllowed: TOKEN_INFORMATION_CLASS = 23
TOKEN_INFORMATION_CLASS_TokenVirtualizationEnabled: TOKEN_INFORMATION_CLASS = 24
TOKEN_INFORMATION_CLASS_TokenIntegrityLevel: TOKEN_INFORMATION_CLASS = 25
TOKEN_INFORMATION_CLASS_TokenUIAccess: TOKEN_INFORMATION_CLASS = 26
TOKEN_INFORMATION_CLASS_TokenMandatoryPolicy: TOKEN_INFORMATION_CLASS = 27
TOKEN_INFORMATION_CLASS_TokenLogonSid: TOKEN_INFORMATION_CLASS = 28
TOKEN_INFORMATION_CLASS_TokenIsAppContainer: TOKEN_INFORMATION_CLASS = 29
TOKEN_INFORMATION_CLASS_TokenCapabilities: TOKEN_INFORMATION_CLASS = 30
TOKEN_INFORMATION_CLASS_TokenAppContainerSid: TOKEN_INFORMATION_CLASS = 31
TOKEN_INFORMATION_CLASS_TokenAppContainerNumber: TOKEN_INFORMATION_CLASS = 32
TOKEN_INFORMATION_CLASS_TokenUserClaimAttributes: TOKEN_INFORMATION_CLASS = 33
TOKEN_INFORMATION_CLASS_TokenDeviceClaimAttributes: TOKEN_INFORMATION_CLASS = 34
TOKEN_INFORMATION_CLASS_TokenRestrictedUserClaimAttributes: TOKEN_INFORMATION_CLASS = 35
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceClaimAttributes: TOKEN_INFORMATION_CLASS = 36
TOKEN_INFORMATION_CLASS_TokenDeviceGroups: TOKEN_INFORMATION_CLASS = 37
TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceGroups: TOKEN_INFORMATION_CLASS = 38
TOKEN_INFORMATION_CLASS_TokenSecurityAttributes: TOKEN_INFORMATION_CLASS = 39
TOKEN_INFORMATION_CLASS_TokenIsRestricted: TOKEN_INFORMATION_CLASS = 40
TOKEN_INFORMATION_CLASS_TokenProcessTrustLevel: TOKEN_INFORMATION_CLASS = 41
TOKEN_INFORMATION_CLASS_TokenPrivateNameSpace: TOKEN_INFORMATION_CLASS = 42
TOKEN_INFORMATION_CLASS_TokenSingletonAttributes: TOKEN_INFORMATION_CLASS = 43
TOKEN_INFORMATION_CLASS_TokenBnoIsolation: TOKEN_INFORMATION_CLASS = 44
TOKEN_INFORMATION_CLASS_TokenChildProcessFlags: TOKEN_INFORMATION_CLASS = 45
TOKEN_INFORMATION_CLASS_TokenIsLessPrivilegedAppContainer: TOKEN_INFORMATION_CLASS = 46
TOKEN_INFORMATION_CLASS_TokenIsSandboxed: TOKEN_INFORMATION_CLASS = 47
TOKEN_INFORMATION_CLASS_MaxTokenInfoClass: TOKEN_INFORMATION_CLASS = 48
class TOKEN_LINKED_TOKEN(Structure):
    LinkedToken: win32more.Foundation.HANDLE
class TOKEN_MANDATORY_LABEL(Structure):
    Label: win32more.Security.SID_AND_ATTRIBUTES
class TOKEN_MANDATORY_POLICY(Structure):
    Policy: win32more.Security.TOKEN_MANDATORY_POLICY_ID
TOKEN_MANDATORY_POLICY_ID = UInt32
TOKEN_MANDATORY_POLICY_OFF: TOKEN_MANDATORY_POLICY_ID = 0
TOKEN_MANDATORY_POLICY_NO_WRITE_UP: TOKEN_MANDATORY_POLICY_ID = 1
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN: TOKEN_MANDATORY_POLICY_ID = 2
TOKEN_MANDATORY_POLICY_VALID_MASK: TOKEN_MANDATORY_POLICY_ID = 3
class TOKEN_ORIGIN(Structure):
    OriginatingLogonSession: win32more.Foundation.LUID
class TOKEN_OWNER(Structure):
    Owner: win32more.Foundation.PSID
class TOKEN_PRIMARY_GROUP(Structure):
    PrimaryGroup: win32more.Foundation.PSID
class TOKEN_PRIVILEGES(Structure):
    PrivilegeCount: UInt32
    Privileges: win32more.Security.LUID_AND_ATTRIBUTES * 1
TOKEN_PRIVILEGES_ATTRIBUTES = UInt32
SE_PRIVILEGE_ENABLED: TOKEN_PRIVILEGES_ATTRIBUTES = 2
SE_PRIVILEGE_ENABLED_BY_DEFAULT: TOKEN_PRIVILEGES_ATTRIBUTES = 1
SE_PRIVILEGE_REMOVED: TOKEN_PRIVILEGES_ATTRIBUTES = 4
SE_PRIVILEGE_USED_FOR_ACCESS: TOKEN_PRIVILEGES_ATTRIBUTES = 2147483648
class TOKEN_SOURCE(Structure):
    SourceName: win32more.Foundation.CHAR * 8
    SourceIdentifier: win32more.Foundation.LUID
class TOKEN_STATISTICS(Structure):
    TokenId: win32more.Foundation.LUID
    AuthenticationId: win32more.Foundation.LUID
    ExpirationTime: win32more.Foundation.LARGE_INTEGER
    TokenType: win32more.Security.TOKEN_TYPE
    ImpersonationLevel: win32more.Security.SECURITY_IMPERSONATION_LEVEL
    DynamicCharged: UInt32
    DynamicAvailable: UInt32
    GroupCount: UInt32
    PrivilegeCount: UInt32
    ModifiedId: win32more.Foundation.LUID
TOKEN_TYPE = Int32
TOKEN_TYPE_TokenPrimary: TOKEN_TYPE = 1
TOKEN_TYPE_TokenImpersonation: TOKEN_TYPE = 2
class TOKEN_USER(Structure):
    User: win32more.Security.SID_AND_ATTRIBUTES
class TOKEN_USER_CLAIMS(Structure):
    UserClaims: c_void_p
WELL_KNOWN_SID_TYPE = Int32
WELL_KNOWN_SID_TYPE_WinNullSid: WELL_KNOWN_SID_TYPE = 0
WELL_KNOWN_SID_TYPE_WinWorldSid: WELL_KNOWN_SID_TYPE = 1
WELL_KNOWN_SID_TYPE_WinLocalSid: WELL_KNOWN_SID_TYPE = 2
WELL_KNOWN_SID_TYPE_WinCreatorOwnerSid: WELL_KNOWN_SID_TYPE = 3
WELL_KNOWN_SID_TYPE_WinCreatorGroupSid: WELL_KNOWN_SID_TYPE = 4
WELL_KNOWN_SID_TYPE_WinCreatorOwnerServerSid: WELL_KNOWN_SID_TYPE = 5
WELL_KNOWN_SID_TYPE_WinCreatorGroupServerSid: WELL_KNOWN_SID_TYPE = 6
WELL_KNOWN_SID_TYPE_WinNtAuthoritySid: WELL_KNOWN_SID_TYPE = 7
WELL_KNOWN_SID_TYPE_WinDialupSid: WELL_KNOWN_SID_TYPE = 8
WELL_KNOWN_SID_TYPE_WinNetworkSid: WELL_KNOWN_SID_TYPE = 9
WELL_KNOWN_SID_TYPE_WinBatchSid: WELL_KNOWN_SID_TYPE = 10
WELL_KNOWN_SID_TYPE_WinInteractiveSid: WELL_KNOWN_SID_TYPE = 11
WELL_KNOWN_SID_TYPE_WinServiceSid: WELL_KNOWN_SID_TYPE = 12
WELL_KNOWN_SID_TYPE_WinAnonymousSid: WELL_KNOWN_SID_TYPE = 13
WELL_KNOWN_SID_TYPE_WinProxySid: WELL_KNOWN_SID_TYPE = 14
WELL_KNOWN_SID_TYPE_WinEnterpriseControllersSid: WELL_KNOWN_SID_TYPE = 15
WELL_KNOWN_SID_TYPE_WinSelfSid: WELL_KNOWN_SID_TYPE = 16
WELL_KNOWN_SID_TYPE_WinAuthenticatedUserSid: WELL_KNOWN_SID_TYPE = 17
WELL_KNOWN_SID_TYPE_WinRestrictedCodeSid: WELL_KNOWN_SID_TYPE = 18
WELL_KNOWN_SID_TYPE_WinTerminalServerSid: WELL_KNOWN_SID_TYPE = 19
WELL_KNOWN_SID_TYPE_WinRemoteLogonIdSid: WELL_KNOWN_SID_TYPE = 20
WELL_KNOWN_SID_TYPE_WinLogonIdsSid: WELL_KNOWN_SID_TYPE = 21
WELL_KNOWN_SID_TYPE_WinLocalSystemSid: WELL_KNOWN_SID_TYPE = 22
WELL_KNOWN_SID_TYPE_WinLocalServiceSid: WELL_KNOWN_SID_TYPE = 23
WELL_KNOWN_SID_TYPE_WinNetworkServiceSid: WELL_KNOWN_SID_TYPE = 24
WELL_KNOWN_SID_TYPE_WinBuiltinDomainSid: WELL_KNOWN_SID_TYPE = 25
WELL_KNOWN_SID_TYPE_WinBuiltinAdministratorsSid: WELL_KNOWN_SID_TYPE = 26
WELL_KNOWN_SID_TYPE_WinBuiltinUsersSid: WELL_KNOWN_SID_TYPE = 27
WELL_KNOWN_SID_TYPE_WinBuiltinGuestsSid: WELL_KNOWN_SID_TYPE = 28
WELL_KNOWN_SID_TYPE_WinBuiltinPowerUsersSid: WELL_KNOWN_SID_TYPE = 29
WELL_KNOWN_SID_TYPE_WinBuiltinAccountOperatorsSid: WELL_KNOWN_SID_TYPE = 30
WELL_KNOWN_SID_TYPE_WinBuiltinSystemOperatorsSid: WELL_KNOWN_SID_TYPE = 31
WELL_KNOWN_SID_TYPE_WinBuiltinPrintOperatorsSid: WELL_KNOWN_SID_TYPE = 32
WELL_KNOWN_SID_TYPE_WinBuiltinBackupOperatorsSid: WELL_KNOWN_SID_TYPE = 33
WELL_KNOWN_SID_TYPE_WinBuiltinReplicatorSid: WELL_KNOWN_SID_TYPE = 34
WELL_KNOWN_SID_TYPE_WinBuiltinPreWindows2000CompatibleAccessSid: WELL_KNOWN_SID_TYPE = 35
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteDesktopUsersSid: WELL_KNOWN_SID_TYPE = 36
WELL_KNOWN_SID_TYPE_WinBuiltinNetworkConfigurationOperatorsSid: WELL_KNOWN_SID_TYPE = 37
WELL_KNOWN_SID_TYPE_WinAccountAdministratorSid: WELL_KNOWN_SID_TYPE = 38
WELL_KNOWN_SID_TYPE_WinAccountGuestSid: WELL_KNOWN_SID_TYPE = 39
WELL_KNOWN_SID_TYPE_WinAccountKrbtgtSid: WELL_KNOWN_SID_TYPE = 40
WELL_KNOWN_SID_TYPE_WinAccountDomainAdminsSid: WELL_KNOWN_SID_TYPE = 41
WELL_KNOWN_SID_TYPE_WinAccountDomainUsersSid: WELL_KNOWN_SID_TYPE = 42
WELL_KNOWN_SID_TYPE_WinAccountDomainGuestsSid: WELL_KNOWN_SID_TYPE = 43
WELL_KNOWN_SID_TYPE_WinAccountComputersSid: WELL_KNOWN_SID_TYPE = 44
WELL_KNOWN_SID_TYPE_WinAccountControllersSid: WELL_KNOWN_SID_TYPE = 45
WELL_KNOWN_SID_TYPE_WinAccountCertAdminsSid: WELL_KNOWN_SID_TYPE = 46
WELL_KNOWN_SID_TYPE_WinAccountSchemaAdminsSid: WELL_KNOWN_SID_TYPE = 47
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseAdminsSid: WELL_KNOWN_SID_TYPE = 48
WELL_KNOWN_SID_TYPE_WinAccountPolicyAdminsSid: WELL_KNOWN_SID_TYPE = 49
WELL_KNOWN_SID_TYPE_WinAccountRasAndIasServersSid: WELL_KNOWN_SID_TYPE = 50
WELL_KNOWN_SID_TYPE_WinNTLMAuthenticationSid: WELL_KNOWN_SID_TYPE = 51
WELL_KNOWN_SID_TYPE_WinDigestAuthenticationSid: WELL_KNOWN_SID_TYPE = 52
WELL_KNOWN_SID_TYPE_WinSChannelAuthenticationSid: WELL_KNOWN_SID_TYPE = 53
WELL_KNOWN_SID_TYPE_WinThisOrganizationSid: WELL_KNOWN_SID_TYPE = 54
WELL_KNOWN_SID_TYPE_WinOtherOrganizationSid: WELL_KNOWN_SID_TYPE = 55
WELL_KNOWN_SID_TYPE_WinBuiltinIncomingForestTrustBuildersSid: WELL_KNOWN_SID_TYPE = 56
WELL_KNOWN_SID_TYPE_WinBuiltinPerfMonitoringUsersSid: WELL_KNOWN_SID_TYPE = 57
WELL_KNOWN_SID_TYPE_WinBuiltinPerfLoggingUsersSid: WELL_KNOWN_SID_TYPE = 58
WELL_KNOWN_SID_TYPE_WinBuiltinAuthorizationAccessSid: WELL_KNOWN_SID_TYPE = 59
WELL_KNOWN_SID_TYPE_WinBuiltinTerminalServerLicenseServersSid: WELL_KNOWN_SID_TYPE = 60
WELL_KNOWN_SID_TYPE_WinBuiltinDCOMUsersSid: WELL_KNOWN_SID_TYPE = 61
WELL_KNOWN_SID_TYPE_WinBuiltinIUsersSid: WELL_KNOWN_SID_TYPE = 62
WELL_KNOWN_SID_TYPE_WinIUserSid: WELL_KNOWN_SID_TYPE = 63
WELL_KNOWN_SID_TYPE_WinBuiltinCryptoOperatorsSid: WELL_KNOWN_SID_TYPE = 64
WELL_KNOWN_SID_TYPE_WinUntrustedLabelSid: WELL_KNOWN_SID_TYPE = 65
WELL_KNOWN_SID_TYPE_WinLowLabelSid: WELL_KNOWN_SID_TYPE = 66
WELL_KNOWN_SID_TYPE_WinMediumLabelSid: WELL_KNOWN_SID_TYPE = 67
WELL_KNOWN_SID_TYPE_WinHighLabelSid: WELL_KNOWN_SID_TYPE = 68
WELL_KNOWN_SID_TYPE_WinSystemLabelSid: WELL_KNOWN_SID_TYPE = 69
WELL_KNOWN_SID_TYPE_WinWriteRestrictedCodeSid: WELL_KNOWN_SID_TYPE = 70
WELL_KNOWN_SID_TYPE_WinCreatorOwnerRightsSid: WELL_KNOWN_SID_TYPE = 71
WELL_KNOWN_SID_TYPE_WinCacheablePrincipalsGroupSid: WELL_KNOWN_SID_TYPE = 72
WELL_KNOWN_SID_TYPE_WinNonCacheablePrincipalsGroupSid: WELL_KNOWN_SID_TYPE = 73
WELL_KNOWN_SID_TYPE_WinEnterpriseReadonlyControllersSid: WELL_KNOWN_SID_TYPE = 74
WELL_KNOWN_SID_TYPE_WinAccountReadonlyControllersSid: WELL_KNOWN_SID_TYPE = 75
WELL_KNOWN_SID_TYPE_WinBuiltinEventLogReadersGroup: WELL_KNOWN_SID_TYPE = 76
WELL_KNOWN_SID_TYPE_WinNewEnterpriseReadonlyControllersSid: WELL_KNOWN_SID_TYPE = 77
WELL_KNOWN_SID_TYPE_WinBuiltinCertSvcDComAccessGroup: WELL_KNOWN_SID_TYPE = 78
WELL_KNOWN_SID_TYPE_WinMediumPlusLabelSid: WELL_KNOWN_SID_TYPE = 79
WELL_KNOWN_SID_TYPE_WinLocalLogonSid: WELL_KNOWN_SID_TYPE = 80
WELL_KNOWN_SID_TYPE_WinConsoleLogonSid: WELL_KNOWN_SID_TYPE = 81
WELL_KNOWN_SID_TYPE_WinThisOrganizationCertificateSid: WELL_KNOWN_SID_TYPE = 82
WELL_KNOWN_SID_TYPE_WinApplicationPackageAuthoritySid: WELL_KNOWN_SID_TYPE = 83
WELL_KNOWN_SID_TYPE_WinBuiltinAnyPackageSid: WELL_KNOWN_SID_TYPE = 84
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientSid: WELL_KNOWN_SID_TYPE = 85
WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientServerSid: WELL_KNOWN_SID_TYPE = 86
WELL_KNOWN_SID_TYPE_WinCapabilityPrivateNetworkClientServerSid: WELL_KNOWN_SID_TYPE = 87
WELL_KNOWN_SID_TYPE_WinCapabilityPicturesLibrarySid: WELL_KNOWN_SID_TYPE = 88
WELL_KNOWN_SID_TYPE_WinCapabilityVideosLibrarySid: WELL_KNOWN_SID_TYPE = 89
WELL_KNOWN_SID_TYPE_WinCapabilityMusicLibrarySid: WELL_KNOWN_SID_TYPE = 90
WELL_KNOWN_SID_TYPE_WinCapabilityDocumentsLibrarySid: WELL_KNOWN_SID_TYPE = 91
WELL_KNOWN_SID_TYPE_WinCapabilitySharedUserCertificatesSid: WELL_KNOWN_SID_TYPE = 92
WELL_KNOWN_SID_TYPE_WinCapabilityEnterpriseAuthenticationSid: WELL_KNOWN_SID_TYPE = 93
WELL_KNOWN_SID_TYPE_WinCapabilityRemovableStorageSid: WELL_KNOWN_SID_TYPE = 94
WELL_KNOWN_SID_TYPE_WinBuiltinRDSRemoteAccessServersSid: WELL_KNOWN_SID_TYPE = 95
WELL_KNOWN_SID_TYPE_WinBuiltinRDSEndpointServersSid: WELL_KNOWN_SID_TYPE = 96
WELL_KNOWN_SID_TYPE_WinBuiltinRDSManagementServersSid: WELL_KNOWN_SID_TYPE = 97
WELL_KNOWN_SID_TYPE_WinUserModeDriversSid: WELL_KNOWN_SID_TYPE = 98
WELL_KNOWN_SID_TYPE_WinBuiltinHyperVAdminsSid: WELL_KNOWN_SID_TYPE = 99
WELL_KNOWN_SID_TYPE_WinAccountCloneableControllersSid: WELL_KNOWN_SID_TYPE = 100
WELL_KNOWN_SID_TYPE_WinBuiltinAccessControlAssistanceOperatorsSid: WELL_KNOWN_SID_TYPE = 101
WELL_KNOWN_SID_TYPE_WinBuiltinRemoteManagementUsersSid: WELL_KNOWN_SID_TYPE = 102
WELL_KNOWN_SID_TYPE_WinAuthenticationAuthorityAssertedSid: WELL_KNOWN_SID_TYPE = 103
WELL_KNOWN_SID_TYPE_WinAuthenticationServiceAssertedSid: WELL_KNOWN_SID_TYPE = 104
WELL_KNOWN_SID_TYPE_WinLocalAccountSid: WELL_KNOWN_SID_TYPE = 105
WELL_KNOWN_SID_TYPE_WinLocalAccountAndAdministratorSid: WELL_KNOWN_SID_TYPE = 106
WELL_KNOWN_SID_TYPE_WinAccountProtectedUsersSid: WELL_KNOWN_SID_TYPE = 107
WELL_KNOWN_SID_TYPE_WinCapabilityAppointmentsSid: WELL_KNOWN_SID_TYPE = 108
WELL_KNOWN_SID_TYPE_WinCapabilityContactsSid: WELL_KNOWN_SID_TYPE = 109
WELL_KNOWN_SID_TYPE_WinAccountDefaultSystemManagedSid: WELL_KNOWN_SID_TYPE = 110
WELL_KNOWN_SID_TYPE_WinBuiltinDefaultSystemManagedGroupSid: WELL_KNOWN_SID_TYPE = 111
WELL_KNOWN_SID_TYPE_WinBuiltinStorageReplicaAdminsSid: WELL_KNOWN_SID_TYPE = 112
WELL_KNOWN_SID_TYPE_WinAccountKeyAdminsSid: WELL_KNOWN_SID_TYPE = 113
WELL_KNOWN_SID_TYPE_WinAccountEnterpriseKeyAdminsSid: WELL_KNOWN_SID_TYPE = 114
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyTrustSid: WELL_KNOWN_SID_TYPE = 115
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyMFASid: WELL_KNOWN_SID_TYPE = 116
WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyAttestationSid: WELL_KNOWN_SID_TYPE = 117
WELL_KNOWN_SID_TYPE_WinAuthenticationFreshKeyAuthSid: WELL_KNOWN_SID_TYPE = 118
WELL_KNOWN_SID_TYPE_WinBuiltinDeviceOwnersSid: WELL_KNOWN_SID_TYPE = 119
make_head(_module, 'ACCESS_ALLOWED_ACE')
make_head(_module, 'ACCESS_ALLOWED_CALLBACK_ACE')
make_head(_module, 'ACCESS_ALLOWED_CALLBACK_OBJECT_ACE')
make_head(_module, 'ACCESS_ALLOWED_OBJECT_ACE')
make_head(_module, 'ACCESS_DENIED_ACE')
make_head(_module, 'ACCESS_DENIED_CALLBACK_ACE')
make_head(_module, 'ACCESS_DENIED_CALLBACK_OBJECT_ACE')
make_head(_module, 'ACCESS_DENIED_OBJECT_ACE')
make_head(_module, 'ACCESS_REASONS')
make_head(_module, 'ACE_HEADER')
make_head(_module, 'ACL')
make_head(_module, 'ACL_REVISION_INFORMATION')
make_head(_module, 'ACL_SIZE_INFORMATION')
make_head(_module, 'CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE')
make_head(_module, 'CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE')
make_head(_module, 'CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1')
make_head(_module, 'CLAIM_SECURITY_ATTRIBUTE_V1')
make_head(_module, 'CLAIM_SECURITY_ATTRIBUTES_INFORMATION')
make_head(_module, 'GENERIC_MAPPING')
make_head(_module, 'LLFILETIME')
make_head(_module, 'LUID_AND_ATTRIBUTES')
make_head(_module, 'OBJECT_TYPE_LIST')
make_head(_module, 'PLSA_AP_CALL_PACKAGE_UNTRUSTED')
make_head(_module, 'PRIVILEGE_SET')
make_head(_module, 'QUOTA_LIMITS')
make_head(_module, 'SE_ACCESS_REPLY')
make_head(_module, 'SE_ACCESS_REQUEST')
make_head(_module, 'SE_IMPERSONATION_STATE')
make_head(_module, 'SE_SECURITY_DESCRIPTOR')
make_head(_module, 'SE_SID')
make_head(_module, 'SEC_THREAD_START')
make_head(_module, 'SECURITY_ATTRIBUTES')
make_head(_module, 'SECURITY_CAPABILITIES')
make_head(_module, 'SECURITY_DESCRIPTOR')
make_head(_module, 'SECURITY_DESCRIPTOR_RELATIVE')
make_head(_module, 'SECURITY_QUALITY_OF_SERVICE')
make_head(_module, 'SID')
make_head(_module, 'SID_AND_ATTRIBUTES')
make_head(_module, 'SID_AND_ATTRIBUTES_HASH')
make_head(_module, 'SID_IDENTIFIER_AUTHORITY')
make_head(_module, 'SYSTEM_ACCESS_FILTER_ACE')
make_head(_module, 'SYSTEM_ALARM_ACE')
make_head(_module, 'SYSTEM_ALARM_CALLBACK_ACE')
make_head(_module, 'SYSTEM_ALARM_CALLBACK_OBJECT_ACE')
make_head(_module, 'SYSTEM_ALARM_OBJECT_ACE')
make_head(_module, 'SYSTEM_AUDIT_ACE')
make_head(_module, 'SYSTEM_AUDIT_CALLBACK_ACE')
make_head(_module, 'SYSTEM_AUDIT_CALLBACK_OBJECT_ACE')
make_head(_module, 'SYSTEM_AUDIT_OBJECT_ACE')
make_head(_module, 'SYSTEM_MANDATORY_LABEL_ACE')
make_head(_module, 'SYSTEM_PROCESS_TRUST_LABEL_ACE')
make_head(_module, 'SYSTEM_RESOURCE_ATTRIBUTE_ACE')
make_head(_module, 'SYSTEM_SCOPED_POLICY_ID_ACE')
make_head(_module, 'TOKEN_ACCESS_INFORMATION')
make_head(_module, 'TOKEN_APPCONTAINER_INFORMATION')
make_head(_module, 'TOKEN_AUDIT_POLICY')
make_head(_module, 'TOKEN_CONTROL')
make_head(_module, 'TOKEN_DEFAULT_DACL')
make_head(_module, 'TOKEN_DEVICE_CLAIMS')
make_head(_module, 'TOKEN_ELEVATION')
make_head(_module, 'TOKEN_GROUPS')
make_head(_module, 'TOKEN_GROUPS_AND_PRIVILEGES')
make_head(_module, 'TOKEN_LINKED_TOKEN')
make_head(_module, 'TOKEN_MANDATORY_LABEL')
make_head(_module, 'TOKEN_MANDATORY_POLICY')
make_head(_module, 'TOKEN_ORIGIN')
make_head(_module, 'TOKEN_OWNER')
make_head(_module, 'TOKEN_PRIMARY_GROUP')
make_head(_module, 'TOKEN_PRIVILEGES')
make_head(_module, 'TOKEN_SOURCE')
make_head(_module, 'TOKEN_STATISTICS')
make_head(_module, 'TOKEN_USER')
make_head(_module, 'TOKEN_USER_CLAIMS')
__all__ = [
    "ACCESS_ALLOWED_ACE",
    "ACCESS_ALLOWED_CALLBACK_ACE",
    "ACCESS_ALLOWED_CALLBACK_OBJECT_ACE",
    "ACCESS_ALLOWED_OBJECT_ACE",
    "ACCESS_DENIED_ACE",
    "ACCESS_DENIED_CALLBACK_ACE",
    "ACCESS_DENIED_CALLBACK_OBJECT_ACE",
    "ACCESS_DENIED_OBJECT_ACE",
    "ACCESS_REASONS",
    "ACE_FLAGS",
    "ACE_HEADER",
    "ACE_INHERITED_OBJECT_TYPE_PRESENT",
    "ACE_OBJECT_TYPE_PRESENT",
    "ACE_REVISION",
    "ACL",
    "ACL_INFORMATION_CLASS",
    "ACL_INFORMATION_CLASS_AclRevisionInformation",
    "ACL_INFORMATION_CLASS_AclSizeInformation",
    "ACL_REVISION",
    "ACL_REVISION_DS",
    "ACL_REVISION_INFORMATION",
    "ACL_SIZE_INFORMATION",
    "ATTRIBUTE_SECURITY_INFORMATION",
    "AUDIT_EVENT_TYPE",
    "AUDIT_EVENT_TYPE_AuditEventDirectoryServiceAccess",
    "AUDIT_EVENT_TYPE_AuditEventObjectAccess",
    "AccessCheck",
    "AccessCheckAndAuditAlarmA",
    "AccessCheckAndAuditAlarmW",
    "AccessCheckByType",
    "AccessCheckByTypeAndAuditAlarmA",
    "AccessCheckByTypeAndAuditAlarmW",
    "AccessCheckByTypeResultList",
    "AccessCheckByTypeResultListAndAuditAlarmA",
    "AccessCheckByTypeResultListAndAuditAlarmByHandleA",
    "AccessCheckByTypeResultListAndAuditAlarmByHandleW",
    "AccessCheckByTypeResultListAndAuditAlarmW",
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
    "AddConditionalAce",
    "AddMandatoryAce",
    "AddResourceAttributeAce",
    "AddScopedPolicyIDAce",
    "AdjustTokenGroups",
    "AdjustTokenPrivileges",
    "AllocateAndInitializeSid",
    "AllocateLocallyUniqueId",
    "AreAllAccessesGranted",
    "AreAnyAccessesGranted",
    "BACKUP_SECURITY_INFORMATION",
    "CLAIM_SECURITY_ATTRIBUTES_INFORMATION",
    "CLAIM_SECURITY_ATTRIBUTE_DISABLED",
    "CLAIM_SECURITY_ATTRIBUTE_DISABLED_BY_DEFAULT",
    "CLAIM_SECURITY_ATTRIBUTE_FLAGS",
    "CLAIM_SECURITY_ATTRIBUTE_FQBN_VALUE",
    "CLAIM_SECURITY_ATTRIBUTE_MANDATORY",
    "CLAIM_SECURITY_ATTRIBUTE_NON_INHERITABLE",
    "CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE",
    "CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_BOOLEAN",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_FQBN",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_INT64",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_SID",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_STRING",
    "CLAIM_SECURITY_ATTRIBUTE_TYPE_UINT64",
    "CLAIM_SECURITY_ATTRIBUTE_USE_FOR_DENY_ONLY",
    "CLAIM_SECURITY_ATTRIBUTE_V1",
    "CLAIM_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE",
    "CLAIM_SECURITY_ATTRIBUTE_VALUE_TYPE",
    "CONTAINER_INHERIT_ACE",
    "CREATE_RESTRICTED_TOKEN_FLAGS",
    "CVT_SECONDS",
    "CheckTokenCapability",
    "CheckTokenMembership",
    "CheckTokenMembershipEx",
    "ConvertToAutoInheritPrivateObjectSecurity",
    "CopySid",
    "CreatePrivateObjectSecurity",
    "CreatePrivateObjectSecurityEx",
    "CreatePrivateObjectSecurityWithMultipleInheritance",
    "CreateRestrictedToken",
    "CreateWellKnownSid",
    "DACL_SECURITY_INFORMATION",
    "DISABLE_MAX_PRIVILEGE",
    "DeleteAce",
    "DeriveCapabilitySidsFromName",
    "DestroyPrivateObjectSecurity",
    "DuplicateToken",
    "DuplicateTokenEx",
    "ENUM_PERIOD",
    "ENUM_PERIOD_DAYS",
    "ENUM_PERIOD_HOURS",
    "ENUM_PERIOD_INVALID",
    "ENUM_PERIOD_MINUTES",
    "ENUM_PERIOD_MONTHS",
    "ENUM_PERIOD_SECONDS",
    "ENUM_PERIOD_WEEKS",
    "ENUM_PERIOD_YEARS",
    "EqualDomainSid",
    "EqualPrefixSid",
    "EqualSid",
    "FAILED_ACCESS_ACE_FLAG",
    "FindFirstFreeAce",
    "FreeSid",
    "GENERIC_MAPPING",
    "GROUP_SECURITY_INFORMATION",
    "GetAce",
    "GetAclInformation",
    "GetAppContainerAce",
    "GetCachedSigningLevel",
    "GetFileSecurityA",
    "GetFileSecurityW",
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
    "GetUserObjectSecurity",
    "GetWindowsAccountDomainSid",
    "HDIAGNOSTIC_DATA_QUERY_SESSION",
    "HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION",
    "HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION",
    "HDIAGNOSTIC_EVENT_TAG_DESCRIPTION",
    "HDIAGNOSTIC_RECORD",
    "HDIAGNOSTIC_REPORT",
    "INHERITED_ACE",
    "INHERIT_NO_PROPAGATE",
    "INHERIT_ONLY",
    "INHERIT_ONLY_ACE",
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
    "LABEL_SECURITY_INFORMATION",
    "LLFILETIME",
    "LOGON32_LOGON",
    "LOGON32_LOGON_BATCH",
    "LOGON32_LOGON_INTERACTIVE",
    "LOGON32_LOGON_NETWORK",
    "LOGON32_LOGON_NETWORK_CLEARTEXT",
    "LOGON32_LOGON_NEW_CREDENTIALS",
    "LOGON32_LOGON_SERVICE",
    "LOGON32_LOGON_UNLOCK",
    "LOGON32_PROVIDER",
    "LOGON32_PROVIDER_DEFAULT",
    "LOGON32_PROVIDER_WINNT40",
    "LOGON32_PROVIDER_WINNT50",
    "LUA_TOKEN",
    "LUID_AND_ATTRIBUTES",
    "LogonUserA",
    "LogonUserExA",
    "LogonUserExW",
    "LogonUserW",
    "LookupAccountNameA",
    "LookupAccountNameW",
    "LookupAccountSidA",
    "LookupAccountSidW",
    "LookupPrivilegeDisplayNameA",
    "LookupPrivilegeDisplayNameW",
    "LookupPrivilegeNameA",
    "LookupPrivilegeNameW",
    "LookupPrivilegeValueA",
    "LookupPrivilegeValueW",
    "MANDATORY_LEVEL",
    "MANDATORY_LEVEL_MandatoryLevelCount",
    "MANDATORY_LEVEL_MandatoryLevelHigh",
    "MANDATORY_LEVEL_MandatoryLevelLow",
    "MANDATORY_LEVEL_MandatoryLevelMedium",
    "MANDATORY_LEVEL_MandatoryLevelSecureProcess",
    "MANDATORY_LEVEL_MandatoryLevelSystem",
    "MANDATORY_LEVEL_MandatoryLevelUntrusted",
    "MakeAbsoluteSD",
    "MakeSelfRelativeSD",
    "MapGenericMask",
    "NCRYPT_DESCRIPTOR_HANDLE",
    "NCRYPT_STREAM_HANDLE",
    "NO_INHERITANCE",
    "NO_PROPAGATE_INHERIT_ACE",
    "OBJECT_INHERIT_ACE",
    "OBJECT_SECURITY_INFORMATION",
    "OBJECT_TYPE_LIST",
    "OWNER_SECURITY_INFORMATION",
    "ObjectCloseAuditAlarmA",
    "ObjectCloseAuditAlarmW",
    "ObjectDeleteAuditAlarmA",
    "ObjectDeleteAuditAlarmW",
    "ObjectOpenAuditAlarmA",
    "ObjectOpenAuditAlarmW",
    "ObjectPrivilegeAuditAlarmA",
    "ObjectPrivilegeAuditAlarmW",
    "PLSA_AP_CALL_PACKAGE_UNTRUSTED",
    "PRIVILEGE_SET",
    "PROTECTED_DACL_SECURITY_INFORMATION",
    "PROTECTED_SACL_SECURITY_INFORMATION",
    "PSECURITY_DESCRIPTOR",
    "PrivilegeCheck",
    "PrivilegedServiceAuditAlarmA",
    "PrivilegedServiceAuditAlarmW",
    "QUOTA_LIMITS",
    "QuerySecurityAccessMask",
    "RevertToSelf",
    "RtlConvertSidToUnicodeString",
    "RtlNormalizeSecurityDescriptor",
    "SACL_SECURITY_INFORMATION",
    "SAFER_LEVEL_HANDLE",
    "SANDBOX_INERT",
    "SCOPE_SECURITY_INFORMATION",
    "SC_HANDLE",
    "SECURITY_ATTRIBUTES",
    "SECURITY_AUTO_INHERIT_FLAGS",
    "SECURITY_CAPABILITIES",
    "SECURITY_DESCRIPTOR",
    "SECURITY_DESCRIPTOR_CONTROL",
    "SECURITY_DESCRIPTOR_RELATIVE",
    "SECURITY_DYNAMIC_TRACKING",
    "SECURITY_IMPERSONATION_LEVEL",
    "SECURITY_IMPERSONATION_LEVEL_SecurityAnonymous",
    "SECURITY_IMPERSONATION_LEVEL_SecurityDelegation",
    "SECURITY_IMPERSONATION_LEVEL_SecurityIdentification",
    "SECURITY_IMPERSONATION_LEVEL_SecurityImpersonation",
    "SECURITY_QUALITY_OF_SERVICE",
    "SECURITY_STATIC_TRACKING",
    "SEC_THREAD_START",
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
    "SE_ACCESS_REPLY",
    "SE_ACCESS_REQUEST",
    "SE_ASSIGNPRIMARYTOKEN_NAME",
    "SE_AUDIT_NAME",
    "SE_BACKUP_NAME",
    "SE_CHANGE_NOTIFY_NAME",
    "SE_CREATE_GLOBAL_NAME",
    "SE_CREATE_PAGEFILE_NAME",
    "SE_CREATE_PERMANENT_NAME",
    "SE_CREATE_SYMBOLIC_LINK_NAME",
    "SE_CREATE_TOKEN_NAME",
    "SE_DACL_AUTO_INHERITED",
    "SE_DACL_AUTO_INHERIT_REQ",
    "SE_DACL_DEFAULTED",
    "SE_DACL_PRESENT",
    "SE_DACL_PROTECTED",
    "SE_DEBUG_NAME",
    "SE_DELEGATE_SESSION_USER_IMPERSONATE_NAME",
    "SE_ENABLE_DELEGATION_NAME",
    "SE_GROUP_DEFAULTED",
    "SE_IMPERSONATE_NAME",
    "SE_IMPERSONATION_STATE",
    "SE_INCREASE_QUOTA_NAME",
    "SE_INC_BASE_PRIORITY_NAME",
    "SE_INC_WORKING_SET_NAME",
    "SE_LOAD_DRIVER_NAME",
    "SE_LOCK_MEMORY_NAME",
    "SE_MACHINE_ACCOUNT_NAME",
    "SE_MANAGE_VOLUME_NAME",
    "SE_OWNER_DEFAULTED",
    "SE_PRIVILEGE_ENABLED",
    "SE_PRIVILEGE_ENABLED_BY_DEFAULT",
    "SE_PRIVILEGE_REMOVED",
    "SE_PRIVILEGE_USED_FOR_ACCESS",
    "SE_PROF_SINGLE_PROCESS_NAME",
    "SE_RELABEL_NAME",
    "SE_REMOTE_SHUTDOWN_NAME",
    "SE_RESTORE_NAME",
    "SE_RM_CONTROL_VALID",
    "SE_SACL_AUTO_INHERITED",
    "SE_SACL_AUTO_INHERIT_REQ",
    "SE_SACL_DEFAULTED",
    "SE_SACL_PRESENT",
    "SE_SACL_PROTECTED",
    "SE_SECURITY_DESCRIPTOR",
    "SE_SECURITY_NAME",
    "SE_SELF_RELATIVE",
    "SE_SHUTDOWN_NAME",
    "SE_SID",
    "SE_SYNC_AGENT_NAME",
    "SE_SYSTEMTIME_NAME",
    "SE_SYSTEM_ENVIRONMENT_NAME",
    "SE_SYSTEM_PROFILE_NAME",
    "SE_TAKE_OWNERSHIP_NAME",
    "SE_TCB_NAME",
    "SE_TIME_ZONE_NAME",
    "SE_TRUSTED_CREDMAN_ACCESS_NAME",
    "SE_UNDOCK_NAME",
    "SE_UNSOLICITED_INPUT_NAME",
    "SID",
    "SID_AND_ATTRIBUTES",
    "SID_AND_ATTRIBUTES_HASH",
    "SID_IDENTIFIER_AUTHORITY",
    "SID_NAME_USE",
    "SID_NAME_USE_SidTypeAlias",
    "SID_NAME_USE_SidTypeComputer",
    "SID_NAME_USE_SidTypeDeletedAccount",
    "SID_NAME_USE_SidTypeDomain",
    "SID_NAME_USE_SidTypeGroup",
    "SID_NAME_USE_SidTypeInvalid",
    "SID_NAME_USE_SidTypeLabel",
    "SID_NAME_USE_SidTypeLogonSession",
    "SID_NAME_USE_SidTypeUnknown",
    "SID_NAME_USE_SidTypeUser",
    "SID_NAME_USE_SidTypeWellKnownGroup",
    "SUB_CONTAINERS_AND_OBJECTS_INHERIT",
    "SUB_CONTAINERS_ONLY_INHERIT",
    "SUB_OBJECTS_ONLY_INHERIT",
    "SUCCESSFUL_ACCESS_ACE_FLAG",
    "SYSTEM_ACCESS_FILTER_ACE",
    "SYSTEM_ALARM_ACE",
    "SYSTEM_ALARM_CALLBACK_ACE",
    "SYSTEM_ALARM_CALLBACK_OBJECT_ACE",
    "SYSTEM_ALARM_OBJECT_ACE",
    "SYSTEM_AUDIT_ACE",
    "SYSTEM_AUDIT_CALLBACK_ACE",
    "SYSTEM_AUDIT_CALLBACK_OBJECT_ACE",
    "SYSTEM_AUDIT_OBJECT_ACE",
    "SYSTEM_AUDIT_OBJECT_ACE_FLAGS",
    "SYSTEM_MANDATORY_LABEL_ACE",
    "SYSTEM_PROCESS_TRUST_LABEL_ACE",
    "SYSTEM_RESOURCE_ATTRIBUTE_ACE",
    "SYSTEM_SCOPED_POLICY_ID_ACE",
    "SetAclInformation",
    "SetCachedSigningLevel",
    "SetFileSecurityA",
    "SetFileSecurityW",
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
    "SetUserObjectSecurity",
    "TOKEN_ACCESS_INFORMATION",
    "TOKEN_ACCESS_MASK",
    "TOKEN_ACCESS_PSEUDO_HANDLE",
    "TOKEN_ACCESS_PSEUDO_HANDLE_WIN8",
    "TOKEN_ACCESS_SYSTEM_SECURITY",
    "TOKEN_ADJUST_DEFAULT",
    "TOKEN_ADJUST_GROUPS",
    "TOKEN_ADJUST_PRIVILEGES",
    "TOKEN_ADJUST_SESSIONID",
    "TOKEN_ALL_ACCESS",
    "TOKEN_APPCONTAINER_INFORMATION",
    "TOKEN_ASSIGN_PRIMARY",
    "TOKEN_AUDIT_POLICY",
    "TOKEN_CONTROL",
    "TOKEN_DEFAULT_DACL",
    "TOKEN_DELETE",
    "TOKEN_DEVICE_CLAIMS",
    "TOKEN_DUPLICATE",
    "TOKEN_ELEVATION",
    "TOKEN_ELEVATION_TYPE",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeDefault",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeFull",
    "TOKEN_ELEVATION_TYPE_TokenElevationTypeLimited",
    "TOKEN_EXECUTE",
    "TOKEN_GROUPS",
    "TOKEN_GROUPS_AND_PRIVILEGES",
    "TOKEN_IMPERSONATE",
    "TOKEN_INFORMATION_CLASS",
    "TOKEN_INFORMATION_CLASS_MaxTokenInfoClass",
    "TOKEN_INFORMATION_CLASS_TokenAccessInformation",
    "TOKEN_INFORMATION_CLASS_TokenAppContainerNumber",
    "TOKEN_INFORMATION_CLASS_TokenAppContainerSid",
    "TOKEN_INFORMATION_CLASS_TokenAuditPolicy",
    "TOKEN_INFORMATION_CLASS_TokenBnoIsolation",
    "TOKEN_INFORMATION_CLASS_TokenCapabilities",
    "TOKEN_INFORMATION_CLASS_TokenChildProcessFlags",
    "TOKEN_INFORMATION_CLASS_TokenDefaultDacl",
    "TOKEN_INFORMATION_CLASS_TokenDeviceClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenDeviceGroups",
    "TOKEN_INFORMATION_CLASS_TokenElevation",
    "TOKEN_INFORMATION_CLASS_TokenElevationType",
    "TOKEN_INFORMATION_CLASS_TokenGroups",
    "TOKEN_INFORMATION_CLASS_TokenGroupsAndPrivileges",
    "TOKEN_INFORMATION_CLASS_TokenHasRestrictions",
    "TOKEN_INFORMATION_CLASS_TokenImpersonationLevel",
    "TOKEN_INFORMATION_CLASS_TokenIntegrityLevel",
    "TOKEN_INFORMATION_CLASS_TokenIsAppContainer",
    "TOKEN_INFORMATION_CLASS_TokenIsLessPrivilegedAppContainer",
    "TOKEN_INFORMATION_CLASS_TokenIsRestricted",
    "TOKEN_INFORMATION_CLASS_TokenIsSandboxed",
    "TOKEN_INFORMATION_CLASS_TokenLinkedToken",
    "TOKEN_INFORMATION_CLASS_TokenLogonSid",
    "TOKEN_INFORMATION_CLASS_TokenMandatoryPolicy",
    "TOKEN_INFORMATION_CLASS_TokenOrigin",
    "TOKEN_INFORMATION_CLASS_TokenOwner",
    "TOKEN_INFORMATION_CLASS_TokenPrimaryGroup",
    "TOKEN_INFORMATION_CLASS_TokenPrivateNameSpace",
    "TOKEN_INFORMATION_CLASS_TokenPrivileges",
    "TOKEN_INFORMATION_CLASS_TokenProcessTrustLevel",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedDeviceGroups",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedSids",
    "TOKEN_INFORMATION_CLASS_TokenRestrictedUserClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenSandBoxInert",
    "TOKEN_INFORMATION_CLASS_TokenSecurityAttributes",
    "TOKEN_INFORMATION_CLASS_TokenSessionId",
    "TOKEN_INFORMATION_CLASS_TokenSessionReference",
    "TOKEN_INFORMATION_CLASS_TokenSingletonAttributes",
    "TOKEN_INFORMATION_CLASS_TokenSource",
    "TOKEN_INFORMATION_CLASS_TokenStatistics",
    "TOKEN_INFORMATION_CLASS_TokenType",
    "TOKEN_INFORMATION_CLASS_TokenUIAccess",
    "TOKEN_INFORMATION_CLASS_TokenUser",
    "TOKEN_INFORMATION_CLASS_TokenUserClaimAttributes",
    "TOKEN_INFORMATION_CLASS_TokenVirtualizationAllowed",
    "TOKEN_INFORMATION_CLASS_TokenVirtualizationEnabled",
    "TOKEN_LINKED_TOKEN",
    "TOKEN_MANDATORY_LABEL",
    "TOKEN_MANDATORY_POLICY",
    "TOKEN_MANDATORY_POLICY_ID",
    "TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN",
    "TOKEN_MANDATORY_POLICY_NO_WRITE_UP",
    "TOKEN_MANDATORY_POLICY_OFF",
    "TOKEN_MANDATORY_POLICY_VALID_MASK",
    "TOKEN_ORIGIN",
    "TOKEN_OWNER",
    "TOKEN_PRIMARY_GROUP",
    "TOKEN_PRIVILEGES",
    "TOKEN_PRIVILEGES_ATTRIBUTES",
    "TOKEN_QUERY",
    "TOKEN_QUERY_SOURCE",
    "TOKEN_READ",
    "TOKEN_READ_CONTROL",
    "TOKEN_SOURCE",
    "TOKEN_STATISTICS",
    "TOKEN_TRUST_CONSTRAINT_MASK",
    "TOKEN_TYPE",
    "TOKEN_TYPE_TokenImpersonation",
    "TOKEN_TYPE_TokenPrimary",
    "TOKEN_USER",
    "TOKEN_USER_CLAIMS",
    "TOKEN_WRITE",
    "TOKEN_WRITE_DAC",
    "TOKEN_WRITE_OWNER",
    "UNPROTECTED_DACL_SECURITY_INFORMATION",
    "UNPROTECTED_SACL_SECURITY_INFORMATION",
    "WELL_KNOWN_SID_TYPE",
    "WELL_KNOWN_SID_TYPE_WinAccountAdministratorSid",
    "WELL_KNOWN_SID_TYPE_WinAccountCertAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountCloneableControllersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountComputersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountControllersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDefaultSystemManagedSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainGuestsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountDomainUsersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountEnterpriseAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountEnterpriseKeyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountGuestSid",
    "WELL_KNOWN_SID_TYPE_WinAccountKeyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountKrbtgtSid",
    "WELL_KNOWN_SID_TYPE_WinAccountPolicyAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAccountProtectedUsersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountRasAndIasServersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinAccountSchemaAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinAnonymousSid",
    "WELL_KNOWN_SID_TYPE_WinApplicationPackageAuthoritySid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticatedUserSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationAuthorityAssertedSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationFreshKeyAuthSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyAttestationSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyPropertyMFASid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationKeyTrustSid",
    "WELL_KNOWN_SID_TYPE_WinAuthenticationServiceAssertedSid",
    "WELL_KNOWN_SID_TYPE_WinBatchSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAccessControlAssistanceOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAccountOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAdministratorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAnyPackageSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinAuthorizationAccessSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinBackupOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinCertSvcDComAccessGroup",
    "WELL_KNOWN_SID_TYPE_WinBuiltinCryptoOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDCOMUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDefaultSystemManagedGroupSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDeviceOwnersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinDomainSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinEventLogReadersGroup",
    "WELL_KNOWN_SID_TYPE_WinBuiltinGuestsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinHyperVAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinIUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinIncomingForestTrustBuildersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinNetworkConfigurationOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPerfLoggingUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPerfMonitoringUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPowerUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPreWindows2000CompatibleAccessSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinPrintOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSEndpointServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSManagementServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRDSRemoteAccessServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRemoteDesktopUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinRemoteManagementUsersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinReplicatorSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinStorageReplicaAdminsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinSystemOperatorsSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinTerminalServerLicenseServersSid",
    "WELL_KNOWN_SID_TYPE_WinBuiltinUsersSid",
    "WELL_KNOWN_SID_TYPE_WinCacheablePrincipalsGroupSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityAppointmentsSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityContactsSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityDocumentsLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityEnterpriseAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientServerSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityInternetClientSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityMusicLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityPicturesLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityPrivateNetworkClientServerSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityRemovableStorageSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilitySharedUserCertificatesSid",
    "WELL_KNOWN_SID_TYPE_WinCapabilityVideosLibrarySid",
    "WELL_KNOWN_SID_TYPE_WinConsoleLogonSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorGroupServerSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorGroupSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerRightsSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerServerSid",
    "WELL_KNOWN_SID_TYPE_WinCreatorOwnerSid",
    "WELL_KNOWN_SID_TYPE_WinDialupSid",
    "WELL_KNOWN_SID_TYPE_WinDigestAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinEnterpriseControllersSid",
    "WELL_KNOWN_SID_TYPE_WinEnterpriseReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinHighLabelSid",
    "WELL_KNOWN_SID_TYPE_WinIUserSid",
    "WELL_KNOWN_SID_TYPE_WinInteractiveSid",
    "WELL_KNOWN_SID_TYPE_WinLocalAccountAndAdministratorSid",
    "WELL_KNOWN_SID_TYPE_WinLocalAccountSid",
    "WELL_KNOWN_SID_TYPE_WinLocalLogonSid",
    "WELL_KNOWN_SID_TYPE_WinLocalServiceSid",
    "WELL_KNOWN_SID_TYPE_WinLocalSid",
    "WELL_KNOWN_SID_TYPE_WinLocalSystemSid",
    "WELL_KNOWN_SID_TYPE_WinLogonIdsSid",
    "WELL_KNOWN_SID_TYPE_WinLowLabelSid",
    "WELL_KNOWN_SID_TYPE_WinMediumLabelSid",
    "WELL_KNOWN_SID_TYPE_WinMediumPlusLabelSid",
    "WELL_KNOWN_SID_TYPE_WinNTLMAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinNetworkServiceSid",
    "WELL_KNOWN_SID_TYPE_WinNetworkSid",
    "WELL_KNOWN_SID_TYPE_WinNewEnterpriseReadonlyControllersSid",
    "WELL_KNOWN_SID_TYPE_WinNonCacheablePrincipalsGroupSid",
    "WELL_KNOWN_SID_TYPE_WinNtAuthoritySid",
    "WELL_KNOWN_SID_TYPE_WinNullSid",
    "WELL_KNOWN_SID_TYPE_WinOtherOrganizationSid",
    "WELL_KNOWN_SID_TYPE_WinProxySid",
    "WELL_KNOWN_SID_TYPE_WinRemoteLogonIdSid",
    "WELL_KNOWN_SID_TYPE_WinRestrictedCodeSid",
    "WELL_KNOWN_SID_TYPE_WinSChannelAuthenticationSid",
    "WELL_KNOWN_SID_TYPE_WinSelfSid",
    "WELL_KNOWN_SID_TYPE_WinServiceSid",
    "WELL_KNOWN_SID_TYPE_WinSystemLabelSid",
    "WELL_KNOWN_SID_TYPE_WinTerminalServerSid",
    "WELL_KNOWN_SID_TYPE_WinThisOrganizationCertificateSid",
    "WELL_KNOWN_SID_TYPE_WinThisOrganizationSid",
    "WELL_KNOWN_SID_TYPE_WinUntrustedLabelSid",
    "WELL_KNOWN_SID_TYPE_WinUserModeDriversSid",
    "WELL_KNOWN_SID_TYPE_WinWorldSid",
    "WELL_KNOWN_SID_TYPE_WinWriteRestrictedCodeSid",
    "WRITE_RESTRICTED",
    "cwcFILENAMESUFFIXMAX",
    "cwcHRESULTSTRING",
    "szLBRACE",
    "szLPAREN",
    "szRBRACE",
    "szRPAREN",
    "wszCERTENROLLSHAREPATH",
    "wszFCSAPARM_CERTFILENAMESUFFIX",
    "wszFCSAPARM_CONFIGDN",
    "wszFCSAPARM_CRLDELTAFILENAMESUFFIX",
    "wszFCSAPARM_CRLFILENAMESUFFIX",
    "wszFCSAPARM_DOMAINDN",
    "wszFCSAPARM_DSCACERTATTRIBUTE",
    "wszFCSAPARM_DSCRLATTRIBUTE",
    "wszFCSAPARM_DSCROSSCERTPAIRATTRIBUTE",
    "wszFCSAPARM_DSKRACERTATTRIBUTE",
    "wszFCSAPARM_DSUSERCERTATTRIBUTE",
    "wszFCSAPARM_SANITIZEDCANAME",
    "wszFCSAPARM_SANITIZEDCANAMEHASH",
    "wszFCSAPARM_SERVERDNSNAME",
    "wszFCSAPARM_SERVERSHORTNAME",
    "wszLBRACE",
    "wszLPAREN",
    "wszRBRACE",
    "wszRPAREN",
]
