from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.Authorization
import Windows.Win32.System.Com
import Windows.Win32.System.Threading
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACCESS_MODE = Int32
NOT_USED_ACCESS: ACCESS_MODE = 0
GRANT_ACCESS: ACCESS_MODE = 1
SET_ACCESS: ACCESS_MODE = 2
DENY_ACCESS: ACCESS_MODE = 3
REVOKE_ACCESS: ACCESS_MODE = 4
SET_AUDIT_SUCCESS: ACCESS_MODE = 5
SET_AUDIT_FAILURE: ACCESS_MODE = 6
class ACTRL_ACCESSA(EasyCastStructure):
    cEntries: UInt32
    pPropertyAccessList: POINTER(Windows.Win32.Security.Authorization.ACTRL_PROPERTY_ENTRYA_head)
class ACTRL_ACCESSW(EasyCastStructure):
    cEntries: UInt32
    pPropertyAccessList: POINTER(Windows.Win32.Security.Authorization.ACTRL_PROPERTY_ENTRYW_head)
class ACTRL_ACCESS_ENTRYA(EasyCastStructure):
    Trustee: Windows.Win32.Security.Authorization.TRUSTEE_A
    fAccessFlags: Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS
    Access: UInt32
    ProvSpecificAccess: UInt32
    Inheritance: Windows.Win32.Security.ACE_FLAGS
    lpInheritProperty: Windows.Win32.Foundation.PSTR
class ACTRL_ACCESS_ENTRYW(EasyCastStructure):
    Trustee: Windows.Win32.Security.Authorization.TRUSTEE_W
    fAccessFlags: Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS
    Access: UInt32
    ProvSpecificAccess: UInt32
    Inheritance: Windows.Win32.Security.ACE_FLAGS
    lpInheritProperty: Windows.Win32.Foundation.PWSTR
ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = UInt32
ACTRL_ACCESS_ALLOWED: ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 1
ACTRL_ACCESS_DENIED: ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 2
ACTRL_AUDIT_SUCCESS: ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 4
ACTRL_AUDIT_FAILURE: ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 8
class ACTRL_ACCESS_ENTRY_LISTA(EasyCastStructure):
    cEntries: UInt32
    pAccessList: POINTER(Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRYA_head)
class ACTRL_ACCESS_ENTRY_LISTW(EasyCastStructure):
    cEntries: UInt32
    pAccessList: POINTER(Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRYW_head)
class ACTRL_ACCESS_INFOA(EasyCastStructure):
    fAccessPermission: UInt32
    lpAccessPermissionName: Windows.Win32.Foundation.PSTR
class ACTRL_ACCESS_INFOW(EasyCastStructure):
    fAccessPermission: UInt32
    lpAccessPermissionName: Windows.Win32.Foundation.PWSTR
class ACTRL_CONTROL_INFOA(EasyCastStructure):
    lpControlId: Windows.Win32.Foundation.PSTR
    lpControlName: Windows.Win32.Foundation.PSTR
class ACTRL_CONTROL_INFOW(EasyCastStructure):
    lpControlId: Windows.Win32.Foundation.PWSTR
    lpControlName: Windows.Win32.Foundation.PWSTR
class ACTRL_OVERLAPPED(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    Reserved2: UInt32
    hEvent: Windows.Win32.Foundation.HANDLE
    class _Anonymous_e__Union(EasyCastUnion):
        Provider: c_void_p
        Reserved1: UInt32
class ACTRL_PROPERTY_ENTRYA(EasyCastStructure):
    lpProperty: Windows.Win32.Foundation.PSTR
    pAccessEntryList: POINTER(Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTA_head)
    fListFlags: UInt32
class ACTRL_PROPERTY_ENTRYW(EasyCastStructure):
    lpProperty: Windows.Win32.Foundation.PWSTR
    pAccessEntryList: POINTER(Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTW_head)
    fListFlags: UInt32
class AUDIT_IP_ADDRESS(EasyCastStructure):
    pIpAddress: Byte * 128
class AUDIT_OBJECT_TYPE(EasyCastStructure):
    ObjectType: Guid
    Flags: UInt16
    Level: UInt16
    AccessMask: UInt32
class AUDIT_OBJECT_TYPES(EasyCastStructure):
    Count: UInt16
    Flags: UInt16
    pObjectTypes: POINTER(Windows.Win32.Security.Authorization.AUDIT_OBJECT_TYPE_head)
class AUDIT_PARAM(EasyCastStructure):
    Type: Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE
    Length: UInt32
    Flags: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        Data0: UIntPtr
        String: Windows.Win32.Foundation.PWSTR
        u: UIntPtr
        psid: POINTER(Windows.Win32.Security.SID_head)
        pguid: POINTER(Guid)
        LogonId_LowPart: UInt32
        pObjectTypes: POINTER(Windows.Win32.Security.Authorization.AUDIT_OBJECT_TYPES_head)
        pIpAddress: POINTER(Windows.Win32.Security.Authorization.AUDIT_IP_ADDRESS_head)
    class _Anonymous2_e__Union(EasyCastUnion):
        Data1: UIntPtr
        LogonId_HighPart: Int32
class AUDIT_PARAMS(EasyCastStructure):
    Length: UInt32
    Flags: UInt32
    Count: UInt16
    Parameters: POINTER(Windows.Win32.Security.Authorization.AUDIT_PARAM_head)
AUDIT_PARAM_TYPE = Int32
APT_None: AUDIT_PARAM_TYPE = 1
APT_String: AUDIT_PARAM_TYPE = 2
APT_Ulong: AUDIT_PARAM_TYPE = 3
APT_Pointer: AUDIT_PARAM_TYPE = 4
APT_Sid: AUDIT_PARAM_TYPE = 5
APT_LogonId: AUDIT_PARAM_TYPE = 6
APT_ObjectTypeList: AUDIT_PARAM_TYPE = 7
APT_Luid: AUDIT_PARAM_TYPE = 8
APT_Guid: AUDIT_PARAM_TYPE = 9
APT_Time: AUDIT_PARAM_TYPE = 10
APT_Int64: AUDIT_PARAM_TYPE = 11
APT_IpAddress: AUDIT_PARAM_TYPE = 12
APT_LogonIdWithSid: AUDIT_PARAM_TYPE = 13
AUTHZ_ACCESS_CHECK_FLAGS = UInt32
AUTHZ_ACCESS_CHECK_NO_DEEP_COPY_SD: AUTHZ_ACCESS_CHECK_FLAGS = 1
AUTHZ_ACCESS_CHECK_RESULTS_HANDLE = IntPtr
class AUTHZ_ACCESS_REPLY(EasyCastStructure):
    ResultListLength: UInt32
    GrantedAccessMask: POINTER(UInt32)
    SaclEvaluationResults: POINTER(Windows.Win32.Security.Authorization.AUTHZ_GENERATE_RESULTS)
    Error: POINTER(UInt32)
class AUTHZ_ACCESS_REQUEST(EasyCastStructure):
    DesiredAccess: UInt32
    PrincipalSelfSid: Windows.Win32.Foundation.PSID
    ObjectTypeList: POINTER(Windows.Win32.Security.OBJECT_TYPE_LIST_head)
    ObjectTypeListLength: UInt32
    OptionalArguments: c_void_p
AUTHZ_AUDIT_EVENT_HANDLE = IntPtr
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = Int32
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoFlags: AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 1
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoOperationType: AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 2
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectType: AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 3
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectName: AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 4
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoAdditionalInfo: AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 5
AUTHZ_AUDIT_EVENT_TYPE_HANDLE = IntPtr
class AUTHZ_AUDIT_EVENT_TYPE_LEGACY(EasyCastStructure):
    CategoryId: UInt16
    AuditId: UInt16
    ParameterCount: UInt16
class AUTHZ_AUDIT_EVENT_TYPE_OLD(EasyCastStructure):
    Version: UInt32
    dwFlags: UInt32
    RefCount: Int32
    hAudit: UIntPtr
    LinkId: Windows.Win32.Foundation.LUID
    u: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_UNION
class AUTHZ_AUDIT_EVENT_TYPE_UNION(EasyCastUnion):
    Legacy: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_LEGACY
AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE = IntPtr
AUTHZ_CLIENT_CONTEXT_HANDLE = IntPtr
AUTHZ_CONTEXT_INFORMATION_CLASS = Int32
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserSid: AUTHZ_CONTEXT_INFORMATION_CLASS = 1
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoGroupsSids: AUTHZ_CONTEXT_INFORMATION_CLASS = 2
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoRestrictedSids: AUTHZ_CONTEXT_INFORMATION_CLASS = 3
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoPrivileges: AUTHZ_CONTEXT_INFORMATION_CLASS = 4
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoExpirationTime: AUTHZ_CONTEXT_INFORMATION_CLASS = 5
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoServerContext: AUTHZ_CONTEXT_INFORMATION_CLASS = 6
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoIdentifier: AUTHZ_CONTEXT_INFORMATION_CLASS = 7
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSource: AUTHZ_CONTEXT_INFORMATION_CLASS = 8
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAll: AUTHZ_CONTEXT_INFORMATION_CLASS = 9
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAuthenticationId: AUTHZ_CONTEXT_INFORMATION_CLASS = 10
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSecurityAttributes: AUTHZ_CONTEXT_INFORMATION_CLASS = 11
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceSids: AUTHZ_CONTEXT_INFORMATION_CLASS = 12
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserClaims: AUTHZ_CONTEXT_INFORMATION_CLASS = 13
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceClaims: AUTHZ_CONTEXT_INFORMATION_CLASS = 14
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAppContainerSid: AUTHZ_CONTEXT_INFORMATION_CLASS = 15
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoCapabilitySids: AUTHZ_CONTEXT_INFORMATION_CLASS = 16
AUTHZ_GENERATE_RESULTS = UInt32
AUTHZ_GENERATE_SUCCESS_AUDIT: AUTHZ_GENERATE_RESULTS = 1
AUTHZ_GENERATE_FAILURE_AUDIT: AUTHZ_GENERATE_RESULTS = 2
AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = UInt32
AUTHZ_NO_SUCCESS_AUDIT: AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 1
AUTHZ_NO_FAILURE_AUDIT: AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 2
AUTHZ_NO_ALLOC_STRINGS: AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 4
class AUTHZ_INIT_INFO(EasyCastStructure):
    version: UInt16
    szResourceManagerName: Windows.Win32.Foundation.PWSTR
    pfnDynamicAccessCheck: Windows.Win32.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK
    pfnComputeDynamicGroups: Windows.Win32.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS
    pfnFreeDynamicGroups: Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS
    pfnGetCentralAccessPolicy: Windows.Win32.Security.Authorization.PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY
    pfnFreeCentralAccessPolicy: Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY
class AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET(EasyCastStructure):
    szObjectTypeName: Windows.Win32.Foundation.PWSTR
    dwOffset: UInt32
AUTHZ_RESOURCE_MANAGER_FLAGS = UInt32
AUTHZ_RM_FLAG_NO_AUDIT: AUTHZ_RESOURCE_MANAGER_FLAGS = 1
AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION: AUTHZ_RESOURCE_MANAGER_FLAGS = 2
AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES: AUTHZ_RESOURCE_MANAGER_FLAGS = 4
AUTHZ_RESOURCE_MANAGER_HANDLE = IntPtr
class AUTHZ_RPC_INIT_INFO_CLIENT(EasyCastStructure):
    version: UInt16
    ObjectUuid: Windows.Win32.Foundation.PWSTR
    ProtSeq: Windows.Win32.Foundation.PWSTR
    NetworkAddr: Windows.Win32.Foundation.PWSTR
    Endpoint: Windows.Win32.Foundation.PWSTR
    Options: Windows.Win32.Foundation.PWSTR
    ServerSpn: Windows.Win32.Foundation.PWSTR
class AUTHZ_SECURITY_ATTRIBUTES_INFORMATION(EasyCastStructure):
    Version: UInt16
    Reserved: UInt16
    AttributeCount: UInt32
    Attribute: _Attribute_e__Union
    class _Attribute_e__Union(EasyCastUnion):
        pAttributeV1: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_V1_head)
AUTHZ_SECURITY_ATTRIBUTE_FLAGS = UInt32
AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE: AUTHZ_SECURITY_ATTRIBUTE_FLAGS = 1
AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE: AUTHZ_SECURITY_ATTRIBUTE_FLAGS = 2
class AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE(EasyCastStructure):
    Version: UInt64
    pName: Windows.Win32.Foundation.PWSTR
class AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(EasyCastStructure):
    pValue: c_void_p
    ValueLength: UInt32
AUTHZ_SECURITY_ATTRIBUTE_OPERATION = Int32
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE: AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 0
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL: AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 1
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD: AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 2
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE: AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 3
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE: AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 4
class AUTHZ_SECURITY_ATTRIBUTE_V1(EasyCastStructure):
    pName: Windows.Win32.Foundation.PWSTR
    ValueType: UInt16
    Reserved: UInt16
    Flags: Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FLAGS
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(EasyCastUnion):
        pInt64: POINTER(Int64)
        pUint64: POINTER(UInt64)
        ppString: POINTER(Windows.Win32.Foundation.PWSTR)
        pFqbn: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE_head)
        pOctetString: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head)
AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE = IntPtr
AUTHZ_SID_OPERATION = Int32
AUTHZ_SID_OPERATION_NONE: AUTHZ_SID_OPERATION = 0
AUTHZ_SID_OPERATION_REPLACE_ALL: AUTHZ_SID_OPERATION = 1
AUTHZ_SID_OPERATION_ADD: AUTHZ_SID_OPERATION = 2
AUTHZ_SID_OPERATION_DELETE: AUTHZ_SID_OPERATION = 3
AUTHZ_SID_OPERATION_REPLACE: AUTHZ_SID_OPERATION = 4
class AUTHZ_SOURCE_SCHEMA_REGISTRATION(EasyCastStructure):
    dwFlags: UInt32
    szEventSourceName: Windows.Win32.Foundation.PWSTR
    szEventMessageFile: Windows.Win32.Foundation.PWSTR
    szEventSourceXmlSchemaFile: Windows.Win32.Foundation.PWSTR
    szEventAccessStringsFile: Windows.Win32.Foundation.PWSTR
    szExecutableImagePath: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    dwObjectTypeNameCount: UInt32
    ObjectTypeNames: Windows.Win32.Security.Authorization.AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET * 1
    class _Anonymous_e__Union(EasyCastUnion):
        pReserved: c_void_p
        pProviderGuid: POINTER(Guid)
AZ_PROP_CONSTANTS = Int32
AZ_PROP_NAME: AZ_PROP_CONSTANTS = 1
AZ_PROP_DESCRIPTION: AZ_PROP_CONSTANTS = 2
AZ_PROP_WRITABLE: AZ_PROP_CONSTANTS = 3
AZ_PROP_APPLICATION_DATA: AZ_PROP_CONSTANTS = 4
AZ_PROP_CHILD_CREATE: AZ_PROP_CONSTANTS = 5
AZ_MAX_APPLICATION_NAME_LENGTH: AZ_PROP_CONSTANTS = 512
AZ_MAX_OPERATION_NAME_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_TASK_NAME_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_SCOPE_NAME_LENGTH: AZ_PROP_CONSTANTS = 65536
AZ_MAX_GROUP_NAME_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_ROLE_NAME_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_NAME_LENGTH: AZ_PROP_CONSTANTS = 65536
AZ_MAX_DESCRIPTION_LENGTH: AZ_PROP_CONSTANTS = 1024
AZ_MAX_APPLICATION_DATA_LENGTH: AZ_PROP_CONSTANTS = 4096
AZ_SUBMIT_FLAG_ABORT: AZ_PROP_CONSTANTS = 1
AZ_SUBMIT_FLAG_FLUSH: AZ_PROP_CONSTANTS = 2
AZ_MAX_POLICY_URL_LENGTH: AZ_PROP_CONSTANTS = 65536
AZ_AZSTORE_FLAG_CREATE: AZ_PROP_CONSTANTS = 1
AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY: AZ_PROP_CONSTANTS = 2
AZ_AZSTORE_FLAG_BATCH_UPDATE: AZ_PROP_CONSTANTS = 4
AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL: AZ_PROP_CONSTANTS = 8
AZ_AZSTORE_FORCE_APPLICATION_CLOSE: AZ_PROP_CONSTANTS = 16
AZ_AZSTORE_NT6_FUNCTION_LEVEL: AZ_PROP_CONSTANTS = 32
AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT: AZ_PROP_CONSTANTS = 32768
AZ_PROP_AZSTORE_DOMAIN_TIMEOUT: AZ_PROP_CONSTANTS = 100
AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT: AZ_PROP_CONSTANTS = 15000
AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT: AZ_PROP_CONSTANTS = 101
AZ_AZSTORE_MIN_DOMAIN_TIMEOUT: AZ_PROP_CONSTANTS = 500
AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT: AZ_PROP_CONSTANTS = 5000
AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT: AZ_PROP_CONSTANTS = 45000
AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES: AZ_PROP_CONSTANTS = 102
AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES: AZ_PROP_CONSTANTS = 120
AZ_PROP_AZSTORE_MAJOR_VERSION: AZ_PROP_CONSTANTS = 103
AZ_PROP_AZSTORE_MINOR_VERSION: AZ_PROP_CONSTANTS = 104
AZ_PROP_AZSTORE_TARGET_MACHINE: AZ_PROP_CONSTANTS = 105
AZ_PROP_AZTORE_IS_ADAM_INSTANCE: AZ_PROP_CONSTANTS = 106
AZ_PROP_OPERATION_ID: AZ_PROP_CONSTANTS = 200
AZ_PROP_TASK_OPERATIONS: AZ_PROP_CONSTANTS = 300
AZ_PROP_TASK_BIZRULE: AZ_PROP_CONSTANTS = 301
AZ_PROP_TASK_BIZRULE_LANGUAGE: AZ_PROP_CONSTANTS = 302
AZ_PROP_TASK_TASKS: AZ_PROP_CONSTANTS = 303
AZ_PROP_TASK_BIZRULE_IMPORTED_PATH: AZ_PROP_CONSTANTS = 304
AZ_PROP_TASK_IS_ROLE_DEFINITION: AZ_PROP_CONSTANTS = 305
AZ_MAX_TASK_BIZRULE_LENGTH: AZ_PROP_CONSTANTS = 65536
AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH: AZ_PROP_CONSTANTS = 512
AZ_MAX_BIZRULE_STRING: AZ_PROP_CONSTANTS = 65536
AZ_PROP_GROUP_TYPE: AZ_PROP_CONSTANTS = 400
AZ_GROUPTYPE_LDAP_QUERY: AZ_PROP_CONSTANTS = 1
AZ_GROUPTYPE_BASIC: AZ_PROP_CONSTANTS = 2
AZ_GROUPTYPE_BIZRULE: AZ_PROP_CONSTANTS = 3
AZ_PROP_GROUP_APP_MEMBERS: AZ_PROP_CONSTANTS = 401
AZ_PROP_GROUP_APP_NON_MEMBERS: AZ_PROP_CONSTANTS = 402
AZ_PROP_GROUP_LDAP_QUERY: AZ_PROP_CONSTANTS = 403
AZ_MAX_GROUP_LDAP_QUERY_LENGTH: AZ_PROP_CONSTANTS = 4096
AZ_PROP_GROUP_MEMBERS: AZ_PROP_CONSTANTS = 404
AZ_PROP_GROUP_NON_MEMBERS: AZ_PROP_CONSTANTS = 405
AZ_PROP_GROUP_MEMBERS_NAME: AZ_PROP_CONSTANTS = 406
AZ_PROP_GROUP_NON_MEMBERS_NAME: AZ_PROP_CONSTANTS = 407
AZ_PROP_GROUP_BIZRULE: AZ_PROP_CONSTANTS = 408
AZ_PROP_GROUP_BIZRULE_LANGUAGE: AZ_PROP_CONSTANTS = 409
AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH: AZ_PROP_CONSTANTS = 410
AZ_MAX_GROUP_BIZRULE_LENGTH: AZ_PROP_CONSTANTS = 65536
AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH: AZ_PROP_CONSTANTS = 64
AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH: AZ_PROP_CONSTANTS = 512
AZ_PROP_ROLE_APP_MEMBERS: AZ_PROP_CONSTANTS = 500
AZ_PROP_ROLE_MEMBERS: AZ_PROP_CONSTANTS = 501
AZ_PROP_ROLE_OPERATIONS: AZ_PROP_CONSTANTS = 502
AZ_PROP_ROLE_TASKS: AZ_PROP_CONSTANTS = 504
AZ_PROP_ROLE_MEMBERS_NAME: AZ_PROP_CONSTANTS = 505
AZ_PROP_SCOPE_BIZRULES_WRITABLE: AZ_PROP_CONSTANTS = 600
AZ_PROP_SCOPE_CAN_BE_DELEGATED: AZ_PROP_CONSTANTS = 601
AZ_PROP_CLIENT_CONTEXT_USER_DN: AZ_PROP_CONSTANTS = 700
AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT: AZ_PROP_CONSTANTS = 701
AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY: AZ_PROP_CONSTANTS = 702
AZ_PROP_CLIENT_CONTEXT_USER_GUID: AZ_PROP_CONSTANTS = 703
AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL: AZ_PROP_CONSTANTS = 704
AZ_PROP_CLIENT_CONTEXT_USER_UPN: AZ_PROP_CONSTANTS = 705
AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT: AZ_PROP_CONSTANTS = 707
AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK: AZ_PROP_CONSTANTS = 708
AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN: AZ_PROP_CONSTANTS = 709
AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID: AZ_PROP_CONSTANTS = 800
AZ_PROP_APPLICATION_VERSION: AZ_PROP_CONSTANTS = 801
AZ_MAX_APPLICATION_VERSION_LENGTH: AZ_PROP_CONSTANTS = 512
AZ_PROP_APPLICATION_NAME: AZ_PROP_CONSTANTS = 802
AZ_PROP_APPLICATION_BIZRULE_ENABLED: AZ_PROP_CONSTANTS = 803
AZ_PROP_APPLY_STORE_SACL: AZ_PROP_CONSTANTS = 900
AZ_PROP_GENERATE_AUDITS: AZ_PROP_CONSTANTS = 901
AZ_PROP_POLICY_ADMINS: AZ_PROP_CONSTANTS = 902
AZ_PROP_POLICY_READERS: AZ_PROP_CONSTANTS = 903
AZ_PROP_DELEGATED_POLICY_USERS: AZ_PROP_CONSTANTS = 904
AZ_PROP_POLICY_ADMINS_NAME: AZ_PROP_CONSTANTS = 905
AZ_PROP_POLICY_READERS_NAME: AZ_PROP_CONSTANTS = 906
AZ_PROP_DELEGATED_POLICY_USERS_NAME: AZ_PROP_CONSTANTS = 907
AZ_CLIENT_CONTEXT_SKIP_GROUP: AZ_PROP_CONSTANTS = 1
AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY: AZ_PROP_CONSTANTS = 1
AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE: AZ_PROP_CONSTANTS = 2
AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY: AZ_PROP_CONSTANTS = 2
SDDL_REVISION_1: UInt32 = 1
SDDL_REVISION: UInt32 = 1
SDDL_OWNER: String = 'O'
SDDL_GROUP: String = 'G'
SDDL_DACL: String = 'D'
SDDL_SACL: String = 'S'
SDDL_PROTECTED: String = 'P'
SDDL_AUTO_INHERIT_REQ: String = 'AR'
SDDL_AUTO_INHERITED: String = 'AI'
SDDL_NULL_ACL: String = 'NO_ACCESS_CONTROL'
SDDL_ACCESS_ALLOWED: String = 'A'
SDDL_ACCESS_DENIED: String = 'D'
SDDL_OBJECT_ACCESS_ALLOWED: String = 'OA'
SDDL_OBJECT_ACCESS_DENIED: String = 'OD'
SDDL_AUDIT: String = 'AU'
SDDL_ALARM: String = 'AL'
SDDL_OBJECT_AUDIT: String = 'OU'
SDDL_OBJECT_ALARM: String = 'OL'
SDDL_MANDATORY_LABEL: String = 'ML'
SDDL_PROCESS_TRUST_LABEL: String = 'TL'
SDDL_CALLBACK_ACCESS_ALLOWED: String = 'XA'
SDDL_CALLBACK_ACCESS_DENIED: String = 'XD'
SDDL_RESOURCE_ATTRIBUTE: String = 'RA'
SDDL_SCOPED_POLICY_ID: String = 'SP'
SDDL_CALLBACK_AUDIT: String = 'XU'
SDDL_CALLBACK_OBJECT_ACCESS_ALLOWED: String = 'ZA'
SDDL_ACCESS_FILTER: String = 'FL'
SDDL_INT: String = 'TI'
SDDL_UINT: String = 'TU'
SDDL_WSTRING: String = 'TS'
SDDL_SID: String = 'TD'
SDDL_BLOB: String = 'TX'
SDDL_BOOLEAN: String = 'TB'
SDDL_CONTAINER_INHERIT: String = 'CI'
SDDL_OBJECT_INHERIT: String = 'OI'
SDDL_NO_PROPAGATE: String = 'NP'
SDDL_INHERIT_ONLY: String = 'IO'
SDDL_INHERITED: String = 'ID'
SDDL_CRITICAL: String = 'CR'
SDDL_TRUST_PROTECTED_FILTER: String = 'TP'
SDDL_AUDIT_SUCCESS: String = 'SA'
SDDL_AUDIT_FAILURE: String = 'FA'
SDDL_READ_PROPERTY: String = 'RP'
SDDL_WRITE_PROPERTY: String = 'WP'
SDDL_CREATE_CHILD: String = 'CC'
SDDL_DELETE_CHILD: String = 'DC'
SDDL_LIST_CHILDREN: String = 'LC'
SDDL_SELF_WRITE: String = 'SW'
SDDL_LIST_OBJECT: String = 'LO'
SDDL_DELETE_TREE: String = 'DT'
SDDL_CONTROL_ACCESS: String = 'CR'
SDDL_READ_CONTROL: String = 'RC'
SDDL_WRITE_DAC: String = 'WD'
SDDL_WRITE_OWNER: String = 'WO'
SDDL_STANDARD_DELETE: String = 'SD'
SDDL_GENERIC_ALL: String = 'GA'
SDDL_GENERIC_READ: String = 'GR'
SDDL_GENERIC_WRITE: String = 'GW'
SDDL_GENERIC_EXECUTE: String = 'GX'
SDDL_FILE_ALL: String = 'FA'
SDDL_FILE_READ: String = 'FR'
SDDL_FILE_WRITE: String = 'FW'
SDDL_FILE_EXECUTE: String = 'FX'
SDDL_KEY_ALL: String = 'KA'
SDDL_KEY_READ: String = 'KR'
SDDL_KEY_WRITE: String = 'KW'
SDDL_KEY_EXECUTE: String = 'KX'
SDDL_NO_WRITE_UP: String = 'NW'
SDDL_NO_READ_UP: String = 'NR'
SDDL_NO_EXECUTE_UP: String = 'NX'
SDDL_ALIAS_SIZE: UInt32 = 2
SDDL_DOMAIN_ADMINISTRATORS: String = 'DA'
SDDL_DOMAIN_GUESTS: String = 'DG'
SDDL_DOMAIN_USERS: String = 'DU'
SDDL_ENTERPRISE_DOMAIN_CONTROLLERS: String = 'ED'
SDDL_DOMAIN_DOMAIN_CONTROLLERS: String = 'DD'
SDDL_DOMAIN_COMPUTERS: String = 'DC'
SDDL_BUILTIN_ADMINISTRATORS: String = 'BA'
SDDL_BUILTIN_GUESTS: String = 'BG'
SDDL_BUILTIN_USERS: String = 'BU'
SDDL_LOCAL_ADMIN: String = 'LA'
SDDL_LOCAL_GUEST: String = 'LG'
SDDL_ACCOUNT_OPERATORS: String = 'AO'
SDDL_BACKUP_OPERATORS: String = 'BO'
SDDL_PRINTER_OPERATORS: String = 'PO'
SDDL_SERVER_OPERATORS: String = 'SO'
SDDL_AUTHENTICATED_USERS: String = 'AU'
SDDL_PERSONAL_SELF: String = 'PS'
SDDL_CREATOR_OWNER: String = 'CO'
SDDL_CREATOR_GROUP: String = 'CG'
SDDL_LOCAL_SYSTEM: String = 'SY'
SDDL_POWER_USERS: String = 'PU'
SDDL_EVERYONE: String = 'WD'
SDDL_REPLICATOR: String = 'RE'
SDDL_INTERACTIVE: String = 'IU'
SDDL_NETWORK: String = 'NU'
SDDL_SERVICE: String = 'SU'
SDDL_RESTRICTED_CODE: String = 'RC'
SDDL_WRITE_RESTRICTED_CODE: String = 'WR'
SDDL_ANONYMOUS: String = 'AN'
SDDL_SCHEMA_ADMINISTRATORS: String = 'SA'
SDDL_CERT_SERV_ADMINISTRATORS: String = 'CA'
SDDL_RAS_SERVERS: String = 'RS'
SDDL_ENTERPRISE_ADMINS: String = 'EA'
SDDL_GROUP_POLICY_ADMINS: String = 'PA'
SDDL_ALIAS_PREW2KCOMPACC: String = 'RU'
SDDL_LOCAL_SERVICE: String = 'LS'
SDDL_NETWORK_SERVICE: String = 'NS'
SDDL_REMOTE_DESKTOP: String = 'RD'
SDDL_NETWORK_CONFIGURATION_OPS: String = 'NO'
SDDL_PERFMON_USERS: String = 'MU'
SDDL_PERFLOG_USERS: String = 'LU'
SDDL_IIS_USERS: String = 'IS'
SDDL_CRYPTO_OPERATORS: String = 'CY'
SDDL_OWNER_RIGHTS: String = 'OW'
SDDL_EVENT_LOG_READERS: String = 'ER'
SDDL_ENTERPRISE_RO_DCs: String = 'RO'
SDDL_CERTSVC_DCOM_ACCESS: String = 'CD'
SDDL_ALL_APP_PACKAGES: String = 'AC'
SDDL_RDS_REMOTE_ACCESS_SERVERS: String = 'RA'
SDDL_RDS_ENDPOINT_SERVERS: String = 'ES'
SDDL_RDS_MANAGEMENT_SERVERS: String = 'MS'
SDDL_USER_MODE_DRIVERS: String = 'UD'
SDDL_HYPER_V_ADMINS: String = 'HA'
SDDL_CLONEABLE_CONTROLLERS: String = 'CN'
SDDL_ACCESS_CONTROL_ASSISTANCE_OPS: String = 'AA'
SDDL_REMOTE_MANAGEMENT_USERS: String = 'RM'
SDDL_AUTHORITY_ASSERTED: String = 'AS'
SDDL_SERVICE_ASSERTED: String = 'SS'
SDDL_PROTECTED_USERS: String = 'AP'
SDDL_KEY_ADMINS: String = 'KA'
SDDL_ENTERPRISE_KEY_ADMINS: String = 'EK'
SDDL_ML_LOW: String = 'LW'
SDDL_ML_MEDIUM: String = 'ME'
SDDL_ML_MEDIUM_PLUS: String = 'MP'
SDDL_ML_HIGH: String = 'HI'
SDDL_ML_SYSTEM: String = 'SI'
SDDL_SEPERATOR: String = ';'
SDDL_DELIMINATOR: String = ':'
SDDL_ACE_BEGIN: String = '('
SDDL_ACE_END: String = ')'
SDDL_ACE_COND_BEGIN: String = '('
SDDL_ACE_COND_END: String = ')'
SDDL_SPACE: String = ' '
SDDL_ACE_COND_BLOB_PREFIX: String = '#'
SDDL_ACE_COND_SID_PREFIX: String = 'SID'
SDDL_ACE_COND_ATTRIBUTE_PREFIX: String = '@'
SDDL_ACE_COND_USER_ATTRIBUTE_PREFIX: String = '@USER.'
SDDL_ACE_COND_RESOURCE_ATTRIBUTE_PREFIX: String = '@RESOURCE.'
SDDL_ACE_COND_DEVICE_ATTRIBUTE_PREFIX: String = '@DEVICE.'
SDDL_ACE_COND_TOKEN_ATTRIBUTE_PREFIX: String = '@TOKEN.'
INHERITED_ACCESS_ENTRY: UInt32 = 16
INHERITED_PARENT: UInt32 = 268435456
INHERITED_GRANDPARENT: UInt32 = 536870912
ACCCTRL_DEFAULT_PROVIDERA: String = 'Windows NT Access Provider'
ACCCTRL_DEFAULT_PROVIDERW: String = 'Windows NT Access Provider'
ACCCTRL_DEFAULT_PROVIDER: String = 'Windows NT Access Provider'
TRUSTEE_ACCESS_ALLOWED: Int32 = 1
TRUSTEE_ACCESS_READ: Int32 = 2
TRUSTEE_ACCESS_WRITE: Int32 = 4
TRUSTEE_ACCESS_EXPLICIT: Int32 = 1
TRUSTEE_ACCESS_ALL: Int32 = -1
ACTRL_RESERVED: UInt32 = 0
ACTRL_PERM_1: UInt32 = 1
ACTRL_PERM_2: UInt32 = 2
ACTRL_PERM_3: UInt32 = 4
ACTRL_PERM_4: UInt32 = 8
ACTRL_PERM_5: UInt32 = 16
ACTRL_PERM_6: UInt32 = 32
ACTRL_PERM_7: UInt32 = 64
ACTRL_PERM_8: UInt32 = 128
ACTRL_PERM_9: UInt32 = 256
ACTRL_PERM_10: UInt32 = 512
ACTRL_PERM_11: UInt32 = 1024
ACTRL_PERM_12: UInt32 = 2048
ACTRL_PERM_13: UInt32 = 4096
ACTRL_PERM_14: UInt32 = 8192
ACTRL_PERM_15: UInt32 = 16384
ACTRL_PERM_16: UInt32 = 32768
ACTRL_PERM_17: UInt32 = 65536
ACTRL_PERM_18: UInt32 = 131072
ACTRL_PERM_19: UInt32 = 262144
ACTRL_PERM_20: UInt32 = 524288
ACTRL_ACCESS_PROTECTED: UInt32 = 1
ACTRL_SYSTEM_ACCESS: UInt32 = 67108864
ACTRL_DELETE: UInt32 = 134217728
ACTRL_READ_CONTROL: UInt32 = 268435456
ACTRL_CHANGE_ACCESS: UInt32 = 536870912
ACTRL_CHANGE_OWNER: UInt32 = 1073741824
ACTRL_SYNCHRONIZE: UInt32 = 2147483648
ACTRL_STD_RIGHTS_ALL: UInt32 = 4160749568
ACTRL_FILE_READ: UInt32 = 1
ACTRL_FILE_WRITE: UInt32 = 2
ACTRL_FILE_APPEND: UInt32 = 4
ACTRL_FILE_READ_PROP: UInt32 = 8
ACTRL_FILE_WRITE_PROP: UInt32 = 16
ACTRL_FILE_EXECUTE: UInt32 = 32
ACTRL_FILE_READ_ATTRIB: UInt32 = 128
ACTRL_FILE_WRITE_ATTRIB: UInt32 = 256
ACTRL_FILE_CREATE_PIPE: UInt32 = 512
ACTRL_DIR_LIST: UInt32 = 1
ACTRL_DIR_CREATE_OBJECT: UInt32 = 2
ACTRL_DIR_CREATE_CHILD: UInt32 = 4
ACTRL_DIR_DELETE_CHILD: UInt32 = 64
ACTRL_DIR_TRAVERSE: UInt32 = 32
ACTRL_KERNEL_TERMINATE: UInt32 = 1
ACTRL_KERNEL_THREAD: UInt32 = 2
ACTRL_KERNEL_VM: UInt32 = 4
ACTRL_KERNEL_VM_READ: UInt32 = 8
ACTRL_KERNEL_VM_WRITE: UInt32 = 16
ACTRL_KERNEL_DUP_HANDLE: UInt32 = 32
ACTRL_KERNEL_PROCESS: UInt32 = 64
ACTRL_KERNEL_SET_INFO: UInt32 = 128
ACTRL_KERNEL_GET_INFO: UInt32 = 256
ACTRL_KERNEL_CONTROL: UInt32 = 512
ACTRL_KERNEL_ALERT: UInt32 = 1024
ACTRL_KERNEL_GET_CONTEXT: UInt32 = 2048
ACTRL_KERNEL_SET_CONTEXT: UInt32 = 4096
ACTRL_KERNEL_TOKEN: UInt32 = 8192
ACTRL_KERNEL_IMPERSONATE: UInt32 = 16384
ACTRL_KERNEL_DIMPERSONATE: UInt32 = 32768
ACTRL_PRINT_SADMIN: UInt32 = 1
ACTRL_PRINT_SLIST: UInt32 = 2
ACTRL_PRINT_PADMIN: UInt32 = 4
ACTRL_PRINT_PUSE: UInt32 = 8
ACTRL_PRINT_JADMIN: UInt32 = 16
ACTRL_SVC_GET_INFO: UInt32 = 1
ACTRL_SVC_SET_INFO: UInt32 = 2
ACTRL_SVC_STATUS: UInt32 = 4
ACTRL_SVC_LIST: UInt32 = 8
ACTRL_SVC_START: UInt32 = 16
ACTRL_SVC_STOP: UInt32 = 32
ACTRL_SVC_PAUSE: UInt32 = 64
ACTRL_SVC_INTERROGATE: UInt32 = 128
ACTRL_SVC_UCONTROL: UInt32 = 256
ACTRL_REG_QUERY: UInt32 = 1
ACTRL_REG_SET: UInt32 = 2
ACTRL_REG_CREATE_CHILD: UInt32 = 4
ACTRL_REG_LIST: UInt32 = 8
ACTRL_REG_NOTIFY: UInt32 = 16
ACTRL_REG_LINK: UInt32 = 32
ACTRL_WIN_CLIPBRD: UInt32 = 1
ACTRL_WIN_GLOBAL_ATOMS: UInt32 = 2
ACTRL_WIN_CREATE: UInt32 = 4
ACTRL_WIN_LIST_DESK: UInt32 = 8
ACTRL_WIN_LIST: UInt32 = 16
ACTRL_WIN_READ_ATTRIBS: UInt32 = 32
ACTRL_WIN_WRITE_ATTRIBS: UInt32 = 64
ACTRL_WIN_SCREEN: UInt32 = 128
ACTRL_WIN_EXIT: UInt32 = 256
ACTRL_ACCESS_NO_OPTIONS: UInt32 = 0
ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES: UInt32 = 1
AUDIT_TYPE_LEGACY: UInt32 = 1
AUDIT_TYPE_WMI: UInt32 = 2
AP_ParamTypeBits: UInt32 = 8
AP_ParamTypeMask: Int32 = 255
_AUTHZ_SS_MAXSIZE: UInt32 = 128
APF_AuditFailure: UInt32 = 0
APF_AuditSuccess: UInt32 = 1
APF_ValidFlags: UInt32 = 1
AUTHZP_WPD_EVENT: UInt32 = 16
AUTHZ_ALLOW_MULTIPLE_SOURCE_INSTANCES: UInt32 = 1
AUTHZ_MIGRATED_LEGACY_PUBLISHER: UInt32 = 2
AUTHZ_AUDIT_INSTANCE_INFORMATION: UInt32 = 2
AUTHZ_SKIP_TOKEN_GROUPS: UInt32 = 2
AUTHZ_REQUIRE_S4U_LOGON: UInt32 = 4
AUTHZ_COMPUTE_PRIVILEGES: UInt32 = 8
AUTHZ_SECURITY_ATTRIBUTE_TYPE_INVALID: UInt32 = 0
AUTHZ_SECURITY_ATTRIBUTE_TYPE_INT64: UInt32 = 1
AUTHZ_SECURITY_ATTRIBUTE_TYPE_UINT64: UInt32 = 2
AUTHZ_SECURITY_ATTRIBUTE_TYPE_STRING: UInt32 = 3
AUTHZ_SECURITY_ATTRIBUTE_TYPE_FQBN: UInt32 = 4
AUTHZ_SECURITY_ATTRIBUTE_TYPE_SID: UInt32 = 5
AUTHZ_SECURITY_ATTRIBUTE_TYPE_BOOLEAN: UInt32 = 6
AUTHZ_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING: UInt32 = 16
AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION_V1: UInt32 = 1
AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION: UInt32 = 1
AUTHZ_RPC_INIT_INFO_CLIENT_VERSION_V1: UInt32 = 1
AUTHZ_INIT_INFO_VERSION_V1: UInt32 = 1
AUTHZ_WPD_CATEGORY_FLAG: UInt32 = 16
AUTHZ_FLAG_ALLOW_MULTIPLE_SOURCE_INSTANCES: UInt32 = 1
OLESCRIPT_E_SYNTAX: Windows.Win32.Foundation.HRESULT = -2147352319
@winfunctype('AUTHZ.dll')
def AuthzAccessCheck(Flags: Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_FLAGS, hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST_head), hAuditEvent: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, OptionalSecurityDescriptorArray: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), OptionalSecurityDescriptorCount: UInt32, pReply: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY_head), phAccessCheckResults: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzCachedAccessCheck(Flags: UInt32, hAccessCheckResults: Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE, pRequest: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST_head), hAuditEvent: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pReply: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzOpenObjectAudit(Flags: UInt32, hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST_head), hAuditEvent: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, OptionalSecurityDescriptorArray: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), OptionalSecurityDescriptorCount: UInt32, pReply: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeHandle(hAccessCheckResults: Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeResourceManager(Flags: UInt32, pfnDynamicAccessCheck: Windows.Win32.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK, pfnComputeDynamicGroups: Windows.Win32.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS, pfnFreeDynamicGroups: Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS, szResourceManagerName: Windows.Win32.Foundation.PWSTR, phAuthzResourceManager: POINTER(Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeResourceManagerEx(Flags: Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS, pAuthzInitInfo: POINTER(Windows.Win32.Security.Authorization.AUTHZ_INIT_INFO_head), phAuthzResourceManager: POINTER(Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeRemoteResourceManager(pRpcInitInfo: POINTER(Windows.Win32.Security.Authorization.AUTHZ_RPC_INIT_INFO_CLIENT_head), phAuthzResourceManager: POINTER(Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeResourceManager(hAuthzResourceManager: Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromToken(Flags: UInt32, TokenHandle: Windows.Win32.Foundation.HANDLE, hAuthzResourceManager: Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE, pExpirationTime: POINTER(Int64), Identifier: Windows.Win32.Foundation.LUID, DynamicGroupArgs: c_void_p, phAuthzClientContext: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromSid(Flags: UInt32, UserSid: Windows.Win32.Foundation.PSID, hAuthzResourceManager: Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE, pExpirationTime: POINTER(Int64), Identifier: Windows.Win32.Foundation.LUID, DynamicGroupArgs: c_void_p, phAuthzClientContext: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromAuthzContext(Flags: UInt32, hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pExpirationTime: POINTER(Int64), Identifier: Windows.Win32.Foundation.LUID, DynamicGroupArgs: c_void_p, phNewAuthzClientContext: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeCompoundContext(UserContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, DeviceContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, phCompoundContext: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzAddSidsToContext(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, Sids: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head), SidCount: UInt32, RestrictedSids: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head), RestrictedSidCount: UInt32, phNewAuthzClientContext: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifySecurityAttributes(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pAttributes: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifyClaims(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, ClaimClass: Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, pClaimOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pClaims: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifySids(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, SidClass: Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, pSidOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pSids: POINTER(Windows.Win32.Security.TOKEN_GROUPS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzSetAppContainerInformation(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pAppContainerSid: Windows.Win32.Foundation.PSID, CapabilityCount: UInt32, pCapabilitySids: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzGetInformationFromContext(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, InfoClass: Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, BufferSize: UInt32, pSizeRequired: POINTER(UInt32), Buffer: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeContext(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzInitializeObjectAccessAuditEvent(Flags: Windows.Win32.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS, hAuditEventType: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE, szOperationType: Windows.Win32.Foundation.PWSTR, szObjectType: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, szAdditionalInfo: Windows.Win32.Foundation.PWSTR, phAuditEvent: POINTER(Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE), dwAdditionalParameterCount: UInt32, *__arglist) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzInitializeObjectAccessAuditEvent2(Flags: UInt32, hAuditEventType: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE, szOperationType: Windows.Win32.Foundation.PWSTR, szObjectType: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, szAdditionalInfo: Windows.Win32.Foundation.PWSTR, szAdditionalInfo2: Windows.Win32.Foundation.PWSTR, phAuditEvent: POINTER(Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE), dwAdditionalParameterCount: UInt32, *__arglist) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeAuditEvent(hAuditEvent: Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzEvaluateSacl(AuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST_head), Sacl: POINTER(Windows.Win32.Security.ACL_head), GrantedAccess: UInt32, AccessGranted: Windows.Win32.Foundation.BOOL, pbGenerateAudit: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInstallSecurityEventSource(dwFlags: UInt32, pRegistration: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUninstallSecurityEventSource(dwFlags: UInt32, szEventSourceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzEnumerateSecurityEventSources(dwFlags: UInt32, Buffer: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION_head), pdwCount: POINTER(UInt32), pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzRegisterSecurityEventSource(dwFlags: UInt32, szEventSourceName: Windows.Win32.Foundation.PWSTR, phEventProvider: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUnregisterSecurityEventSource(dwFlags: UInt32, phEventProvider: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzReportSecurityEvent(dwFlags: UInt32, hEventProvider: Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE, dwAuditId: UInt32, pUserSid: Windows.Win32.Foundation.PSID, dwCount: UInt32, *__arglist) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzReportSecurityEventFromParams(dwFlags: UInt32, hEventProvider: Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE, dwAuditId: UInt32, pUserSid: Windows.Win32.Foundation.PSID, pParams: POINTER(Windows.Win32.Security.Authorization.AUDIT_PARAMS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzRegisterCapChangeNotification(phCapChangeSubscription: POINTER(Windows.Win32.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE), pfnCapChangeCallback: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pCallbackContext: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUnregisterCapChangeNotification(hCapChangeSubscription: Windows.Win32.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeCentralAccessPolicyCache() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetEntriesInAclA(cCountOfExplicitEntries: UInt32, pListOfExplicitEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head), OldAcl: POINTER(Windows.Win32.Security.ACL_head), NewAcl: POINTER(POINTER(Windows.Win32.Security.ACL_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetEntriesInAclW(cCountOfExplicitEntries: UInt32, pListOfExplicitEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head), OldAcl: POINTER(Windows.Win32.Security.ACL_head), NewAcl: POINTER(POINTER(Windows.Win32.Security.ACL_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetExplicitEntriesFromAclA(pacl: POINTER(Windows.Win32.Security.ACL_head), pcCountOfExplicitEntries: POINTER(UInt32), pListOfExplicitEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetExplicitEntriesFromAclW(pacl: POINTER(Windows.Win32.Security.ACL_head), pcCountOfExplicitEntries: POINTER(UInt32), pListOfExplicitEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head))) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetEffectiveRightsFromAclA(pacl: POINTER(Windows.Win32.Security.ACL_head), pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pAccessRights: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetEffectiveRightsFromAclW(pacl: POINTER(Windows.Win32.Security.ACL_head), pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pAccessRights: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetAuditedPermissionsFromAclA(pacl: POINTER(Windows.Win32.Security.ACL_head), pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pSuccessfulAuditedRights: POINTER(UInt32), pFailedAuditRights: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetAuditedPermissionsFromAclW(pacl: POINTER(Windows.Win32.Security.ACL_head), pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pSuccessfulAuditedRights: POINTER(UInt32), pFailedAuditRights: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetNamedSecurityInfoA(pObjectName: Windows.Win32.Foundation.PSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppsidOwner: POINTER(Windows.Win32.Foundation.PSID), ppsidGroup: POINTER(Windows.Win32.Foundation.PSID), ppDacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetNamedSecurityInfoW(pObjectName: Windows.Win32.Foundation.PWSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppsidOwner: POINTER(Windows.Win32.Foundation.PSID), ppsidGroup: POINTER(Windows.Win32.Foundation.PSID), ppDacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetSecurityInfo(handle: Windows.Win32.Foundation.HANDLE, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, ppsidOwner: POINTER(Windows.Win32.Foundation.PSID), ppsidGroup: POINTER(Windows.Win32.Foundation.PSID), ppDacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSacl: POINTER(POINTER(Windows.Win32.Security.ACL_head)), ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetNamedSecurityInfoA(pObjectName: Windows.Win32.Foundation.PSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, psidOwner: Windows.Win32.Foundation.PSID, psidGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetNamedSecurityInfoW(pObjectName: Windows.Win32.Foundation.PWSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, psidOwner: Windows.Win32.Foundation.PSID, psidGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetSecurityInfo(handle: Windows.Win32.Foundation.HANDLE, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, psidOwner: Windows.Win32.Foundation.PSID, psidGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetInheritanceSourceA(pObjectName: Windows.Win32.Foundation.PSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, Container: Windows.Win32.Foundation.BOOL, pObjectClassGuids: POINTER(POINTER(Guid)), GuidCount: UInt32, pAcl: POINTER(Windows.Win32.Security.ACL_head), pfnArray: POINTER(Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS_head), pGenericMapping: POINTER(Windows.Win32.Security.GENERIC_MAPPING_head), pInheritArray: POINTER(Windows.Win32.Security.Authorization.INHERITED_FROMA_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetInheritanceSourceW(pObjectName: Windows.Win32.Foundation.PWSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, Container: Windows.Win32.Foundation.BOOL, pObjectClassGuids: POINTER(POINTER(Guid)), GuidCount: UInt32, pAcl: POINTER(Windows.Win32.Security.ACL_head), pfnArray: POINTER(Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS_head), pGenericMapping: POINTER(Windows.Win32.Security.GENERIC_MAPPING_head), pInheritArray: POINTER(Windows.Win32.Security.Authorization.INHERITED_FROMW_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def FreeInheritedFromArray(pInheritArray: POINTER(Windows.Win32.Security.Authorization.INHERITED_FROMW_head), AceCnt: UInt16, pfnArray: POINTER(Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS_head)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeResetNamedSecurityInfoA(pObjectName: Windows.Win32.Foundation.PSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, pOwner: Windows.Win32.Foundation.PSID, pGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head), KeepExplicit: Windows.Win32.Foundation.BOOL, fnProgress: Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeResetNamedSecurityInfoW(pObjectName: Windows.Win32.Foundation.PWSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, pOwner: Windows.Win32.Foundation.PSID, pGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head), KeepExplicit: Windows.Win32.Foundation.BOOL, fnProgress: Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeSetNamedSecurityInfoA(pObjectName: Windows.Win32.Foundation.PSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, pOwner: Windows.Win32.Foundation.PSID, pGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head), dwAction: Windows.Win32.Security.Authorization.TREE_SEC_INFO, fnProgress: Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeSetNamedSecurityInfoW(pObjectName: Windows.Win32.Foundation.PWSTR, ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: UInt32, pOwner: Windows.Win32.Foundation.PSID, pGroup: Windows.Win32.Foundation.PSID, pDacl: POINTER(Windows.Win32.Security.ACL_head), pSacl: POINTER(Windows.Win32.Security.ACL_head), dwAction: Windows.Win32.Security.Authorization.TREE_SEC_INFO, fnProgress: Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: c_void_p) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def BuildSecurityDescriptorA(pOwner: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pGroup: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), cCountOfAccessEntries: UInt32, pListOfAccessEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head), cCountOfAuditEntries: UInt32, pListOfAuditEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head), pOldSD: Windows.Win32.Security.PSECURITY_DESCRIPTOR, pSizeNewSD: POINTER(UInt32), pNewSD: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def BuildSecurityDescriptorW(pOwner: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pGroup: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), cCountOfAccessEntries: UInt32, pListOfAccessEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head), cCountOfAuditEntries: UInt32, pListOfAuditEntries: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head), pOldSD: Windows.Win32.Security.PSECURITY_DESCRIPTOR, pSizeNewSD: POINTER(UInt32), pNewSD: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def LookupSecurityDescriptorPartsA(ppOwner: POINTER(POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)), ppGroup: POINTER(POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)), pcCountOfAccessEntries: POINTER(UInt32), ppListOfAccessEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head)), pcCountOfAuditEntries: POINTER(UInt32), ppListOfAuditEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head)), pSD: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def LookupSecurityDescriptorPartsW(ppOwner: POINTER(POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)), ppGroup: POINTER(POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)), pcCountOfAccessEntries: POINTER(UInt32), ppListOfAccessEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head)), pcCountOfAuditEntries: POINTER(UInt32), ppListOfAuditEntries: POINTER(POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head)), pSD: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def BuildExplicitAccessWithNameA(pExplicitAccess: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head), pTrusteeName: Windows.Win32.Foundation.PSTR, AccessPermissions: UInt32, AccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: Windows.Win32.Security.ACE_FLAGS) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildExplicitAccessWithNameW(pExplicitAccess: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head), pTrusteeName: Windows.Win32.Foundation.PWSTR, AccessPermissions: UInt32, AccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: Windows.Win32.Security.ACE_FLAGS) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateExplicitAccessWithNameA(pExplicitAccess: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A_head), pTrusteeName: Windows.Win32.Foundation.PSTR, pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), AccessPermissions: UInt32, AccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: UInt32) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateExplicitAccessWithNameW(pExplicitAccess: POINTER(Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W_head), pTrusteeName: Windows.Win32.Foundation.PWSTR, pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), AccessPermissions: UInt32, AccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: UInt32) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithNameA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pName: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithNameW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pName: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateTrusteeA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pImpersonateTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateTrusteeW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pImpersonateTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithSidA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pSid: Windows.Win32.Foundation.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithSidW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pSid: Windows.Win32.Foundation.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndSidA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pObjSid: POINTER(Windows.Win32.Security.Authorization.OBJECTS_AND_SID_head), pObjectGuid: POINTER(Guid), pInheritedObjectGuid: POINTER(Guid), pSid: Windows.Win32.Foundation.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndSidW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pObjSid: POINTER(Windows.Win32.Security.Authorization.OBJECTS_AND_SID_head), pObjectGuid: POINTER(Guid), pInheritedObjectGuid: POINTER(Guid), pSid: Windows.Win32.Foundation.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndNameA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head), pObjName: POINTER(Windows.Win32.Security.Authorization.OBJECTS_AND_NAME_A_head), ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, ObjectTypeName: Windows.Win32.Foundation.PSTR, InheritedObjectTypeName: Windows.Win32.Foundation.PSTR, Name: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndNameW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head), pObjName: POINTER(Windows.Win32.Security.Authorization.OBJECTS_AND_NAME_W_head), ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, ObjectTypeName: Windows.Win32.Foundation.PWSTR, InheritedObjectTypeName: Windows.Win32.Foundation.PWSTR, Name: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeNameA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeNameW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeTypeA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> Windows.Win32.Security.Authorization.TRUSTEE_TYPE: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeTypeW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> Windows.Win32.Security.Authorization.TRUSTEE_TYPE: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeFormA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> Windows.Win32.Security.Authorization.TRUSTEE_FORM: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeFormW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> Windows.Win32.Security.Authorization.TRUSTEE_FORM: ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeOperationA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION: ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeOperationW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION: ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeA(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)) -> POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head): ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeW(pTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)) -> POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head): ...
@winfunctype('ADVAPI32.dll')
def ConvertSidToStringSidA(Sid: Windows.Win32.Foundation.PSID, StringSid: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertSidToStringSidW(Sid: Windows.Win32.Foundation.PSID, StringSid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSidToSidA(StringSid: Windows.Win32.Foundation.PSTR, Sid: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSidToSidW(StringSid: Windows.Win32.Foundation.PWSTR, Sid: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSecurityDescriptorToSecurityDescriptorA(StringSecurityDescriptor: Windows.Win32.Foundation.PSTR, StringSDRevision: UInt32, SecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSecurityDescriptorToSecurityDescriptorW(StringSecurityDescriptor: Windows.Win32.Foundation.PWSTR, StringSDRevision: UInt32, SecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertSecurityDescriptorToStringSecurityDescriptorA(SecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, RequestedStringSDRevision: UInt32, SecurityInformation: UInt32, StringSecurityDescriptor: POINTER(Windows.Win32.Foundation.PSTR), StringSecurityDescriptorLen: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertSecurityDescriptorToStringSecurityDescriptorW(SecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, RequestedStringSDRevision: UInt32, SecurityInformation: UInt32, StringSecurityDescriptor: POINTER(Windows.Win32.Foundation.PWSTR), StringSecurityDescriptorLen: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
AzAuthorizationStore = Guid('b2bcff59-a757-4b0b-a1-bc-ea-69-98-1d-a6-9e')
AzBizRuleContext = Guid('5c2dc96f-8d51-434b-b3-3c-37-9b-cc-ae-77-c3')
AzPrincipalLocator = Guid('483afb5d-70df-4e16-ab-dc-a1-de-4d-01-5a-3e')
class EXPLICIT_ACCESS_A(EasyCastStructure):
    grfAccessPermissions: UInt32
    grfAccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE
    grfInheritance: Windows.Win32.Security.ACE_FLAGS
    Trustee: Windows.Win32.Security.Authorization.TRUSTEE_A
class EXPLICIT_ACCESS_W(EasyCastStructure):
    grfAccessPermissions: UInt32
    grfAccessMode: Windows.Win32.Security.Authorization.ACCESS_MODE
    grfInheritance: Windows.Win32.Security.ACE_FLAGS
    Trustee: Windows.Win32.Security.Authorization.TRUSTEE_W
class FN_OBJECT_MGR_FUNCTS(EasyCastStructure):
    Placeholder: UInt32
@winfunctype_pointer
def FN_PROGRESS(pObjectName: Windows.Win32.Foundation.PWSTR, Status: UInt32, pInvokeSetting: POINTER(Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING), Args: c_void_p, SecuritySet: Windows.Win32.Foundation.BOOL) -> Void: ...
class IAzApplication(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('987bc7c7-b813-4d27-be-de-6b-a5-ae-86-7e-95')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AuthzInterfaceClsid(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AuthzInterfaceClsid(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Version(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Version(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GenerateAudits(self, pbProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GenerateAudits(self, bProp: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ApplyStoreSacl(self, pbProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ApplyStoreSacl(self, bProp: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PolicyReaders(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddPolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeletePolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Scopes(self, ppScopeCollection: POINTER(Windows.Win32.Security.Authorization.IAzScopes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def OpenScope(self, bstrScopeName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppScope: POINTER(Windows.Win32.Security.Authorization.IAzScope_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateScope(self, bstrScopeName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppScope: POINTER(Windows.Win32.Security.Authorization.IAzScope_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def DeleteScope(self, bstrScopeName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Operations(self, ppOperationCollection: POINTER(Windows.Win32.Security.Authorization.IAzOperations_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def OpenOperation(self, bstrOperationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppOperation: POINTER(Windows.Win32.Security.Authorization.IAzOperation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def CreateOperation(self, bstrOperationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppOperation: POINTER(Windows.Win32.Security.Authorization.IAzOperation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DeleteOperation(self, bstrOperationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Tasks(self, ppTaskCollection: POINTER(Windows.Win32.Security.Authorization.IAzTasks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def OpenTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(Windows.Win32.Security.Authorization.IAzTask_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CreateTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(Windows.Win32.Security.Authorization.IAzTask_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DeleteTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def OpenApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def CreateApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def DeleteApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_Roles(self, ppRoleCollection: POINTER(Windows.Win32.Security.Authorization.IAzRoles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def OpenRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(Windows.Win32.Security.Authorization.IAzRole_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def CreateRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(Windows.Win32.Security.Authorization.IAzRole_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def DeleteRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def InitializeClientContextFromToken(self, ullTokenHandle: UInt64, varReserved: Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(Windows.Win32.Security.Authorization.IAzClientContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def AddPropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def InitializeClientContextFromName(self, ClientName: Windows.Win32.Foundation.BSTR, DomainName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(Windows.Win32.Security.Authorization.IAzClientContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_DelegatedPolicyUsers(self, pvarDelegatedPolicyUsers: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def InitializeClientContextFromStringSid(self, SidString: Windows.Win32.Foundation.BSTR, lOptions: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(Windows.Win32.Security.Authorization.IAzClientContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_PolicyReadersName(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def AddPolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def DeletePolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def AddPolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def DeletePolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_DelegatedPolicyUsersName(self, pvarDelegatedPolicyUsers: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplication2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzApplication
    _iid_ = Guid('086a68af-a249-437c-b1-8d-d4-d8-6d-6a-96-60')
    @commethod(68)
    def InitializeClientContextFromToken2(self, ulTokenHandleLowPart: UInt32, ulTokenHandleHighPart: UInt32, varReserved: Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(Windows.Win32.Security.Authorization.IAzClientContext2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def InitializeClientContext2(self, IdentifyingString: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(Windows.Win32.Security.Authorization.IAzClientContext2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplication3(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzApplication2
    _iid_ = Guid('181c845e-7196-4a7d-ac-2e-02-0c-0b-b7-a3-03')
    @commethod(70)
    def ScopeExists(self, bstrScopeName: Windows.Win32.Foundation.BSTR, pbExist: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def OpenScope2(self, bstrScopeName: Windows.Win32.Foundation.BSTR, ppScope2: POINTER(Windows.Win32.Security.Authorization.IAzScope2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def CreateScope2(self, bstrScopeName: Windows.Win32.Foundation.BSTR, ppScope2: POINTER(Windows.Win32.Security.Authorization.IAzScope2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def DeleteScope2(self, bstrScopeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def CreateRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def OpenRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def DeleteRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_RoleAssignments(self, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def CreateRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def OpenRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def DeleteRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_BizRulesEnabled(self, pbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_BizRulesEnabled(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroup(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('f1b744cd-58a6-4e06-9f-bf-36-f6-d7-79-e2-1e')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(self, plProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Type(self, lProp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_LdapQuery(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_LdapQuery(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AppMembers(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AppNonMembers(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Members(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_NonMembers(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddAppMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteAppMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddAppNonMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteAppNonMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddNonMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DeleteNonMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def AddPropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def AddMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def DeleteMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddNonMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeleteNonMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_MembersName(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_NonMembersName(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroup2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzApplicationGroup
    _iid_ = Guid('3f0613fc-b71a-464e-a1-1d-5b-88-1a-56-ce-fa')
    @commethod(39)
    def get_BizRule(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_BizRule(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_BizRuleLanguage(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_BizRuleLanguage(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_BizRuleImportedPath(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_BizRuleImportedPath(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RoleAssignments(self, bstrScopeName: Windows.Win32.Foundation.BSTR, bRecursive: Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroups(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('4ce66ad5-9f3c-469d-a9-11-b9-98-87-a7-e6-85')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzApplications(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('929b11a9-95c5-4a84-a2-9a-20-ad-42-c2-f1-6c')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('edbd9ca9-9b82-4f6a-9e-8b-98-30-1e-45-0f-14')
    @commethod(7)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DomainTimeout(self, plProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_DomainTimeout(self, lProp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ScriptEngineTimeout(self, plProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ScriptEngineTimeout(self, lProp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MaxScriptEngines(self, plProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MaxScriptEngines(self, lProp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GenerateAudits(self, pbProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GenerateAudits(self, bProp: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddPropertyItem(self, lPropId: Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PolicyReaders(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddPolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeletePolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Initialize(self, lFlags: Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS, bstrPolicyURL: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def UpdateCache(self, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Delete(self, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Applications(self, ppAppCollection: POINTER(Windows.Win32.Security.Authorization.IAzApplications_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def OpenApplication(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(Windows.Win32.Security.Authorization.IAzApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CreateApplication(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(Windows.Win32.Security.Authorization.IAzApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeleteApplication(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CreateApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def OpenApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DeleteApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_DelegatedPolicyUsers(self, pvarDelegatedPolicyUsers: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_TargetMachine(self, pbstrTargetMachine: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ApplyStoreSacl(self, pbApplyStoreSacl: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ApplyStoreSacl(self, bApplyStoreSacl: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_PolicyReadersName(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def AddPolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def DeletePolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def AddPolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def DeletePolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_DelegatedPolicyUsersName(self, pvarDelegatedPolicyUsers: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def CloseApplication(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, lFlag: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzAuthorizationStore
    _iid_ = Guid('b11e5584-d577-4273-b6-c5-09-73-e0-f8-e8-0d')
    @commethod(58)
    def OpenApplication2(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(Windows.Win32.Security.Authorization.IAzApplication2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def CreateApplication2(self, bstrApplicationName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(Windows.Win32.Security.Authorization.IAzApplication2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore3(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzAuthorizationStore2
    _iid_ = Guid('abc08425-0c86-4fa0-9b-e3-71-89-95-6c-92-6e')
    @commethod(60)
    def IsUpdateNeeded(self, pbIsUpdateNeeded: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def BizruleGroupSupported(self, pbSupported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def UpgradeStoresFunctionalLevel(self, lFunctionalLevel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def IsFunctionalLevelUpgradeSupported(self, lFunctionalLevel: Int32, pbSupported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetSchemaVersion(self, plMajorVersion: POINTER(Int32), plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('e192f17d-d59f-455e-a1-52-94-03-16-cd-77-b2')
    @commethod(7)
    def put_BusinessRuleResult(self, bResult: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BusinessRuleString(self, bstrBusinessRuleString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BusinessRuleString(self, pbstrBusinessRuleString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetParameter(self, bstrParameterName: Windows.Win32.Foundation.BSTR, pvarParameterValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleInterfaces(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('e94128c7-e9da-44cc-b0-bd-53-03-6f-3a-ab-3d')
    @commethod(7)
    def AddInterface(self, bstrInterfaceName: Windows.Win32.Foundation.BSTR, lInterfaceFlag: Int32, varInterface: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddInterfaces(self, varInterfaceNames: Windows.Win32.System.Variant.VARIANT, varInterfaceFlags: Windows.Win32.System.Variant.VARIANT, varInterfaces: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInterfaceValue(self, bstrInterfaceName: Windows.Win32.Foundation.BSTR, lInterfaceFlag: POINTER(Int32), varInterface: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, bstrInterfaceName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAll(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Count(self, plCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleParameters(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('fc17685f-e25d-4dcd-ba-e1-27-6e-c9-53-3c-b5')
    @commethod(7)
    def AddParameter(self, bstrParameterName: Windows.Win32.Foundation.BSTR, varParameterValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddParameters(self, varParameterNames: Windows.Win32.System.Variant.VARIANT, varParameterValues: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParameterValue(self, bstrParameterName: Windows.Win32.Foundation.BSTR, pvarParameterValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, varParameterName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAll(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Count(self, plCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('eff1f00b-488a-466d-af-d9-a4-01-c5-f9-ee-f5')
    @commethod(7)
    def AccessCheck(self, bstrObjectName: Windows.Win32.Foundation.BSTR, varScopeNames: Windows.Win32.System.Variant.VARIANT, varOperations: Windows.Win32.System.Variant.VARIANT, varParameterNames: Windows.Win32.System.Variant.VARIANT, varParameterValues: Windows.Win32.System.Variant.VARIANT, varInterfaceNames: Windows.Win32.System.Variant.VARIANT, varInterfaceFlags: Windows.Win32.System.Variant.VARIANT, varInterfaces: Windows.Win32.System.Variant.VARIANT, pvarResults: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBusinessRuleString(self, pbstrBusinessRuleString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UserDn(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UserSamCompat(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_UserDisplay(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UserGuid(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UserCanonical(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_UserUpn(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserDnsSamCompat(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRoles(self, bstrScopeName: Windows.Win32.Foundation.BSTR, pvarRoleNames: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_RoleForAccessCheck(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_RoleForAccessCheck(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzClientContext
    _iid_ = Guid('2b0c92b8-208a-488a-8f-81-e4-ed-b2-21-11-cd')
    @commethod(20)
    def GetAssignedScopesPage(self, lOptions: Int32, PageSize: Int32, pvarCursor: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarScopeNames: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddRoles(self, varRoles: Windows.Win32.System.Variant.VARIANT, bstrScopeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddApplicationGroups(self, varApplicationGroups: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddStringSids(self, varStringSids: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_LDAPQueryDN(self, bstrLDAPQueryDN: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_LDAPQueryDN(self, pbstrLDAPQueryDN: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext3(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzClientContext2
    _iid_ = Guid('11894fde-1deb-4b4b-89-07-6d-1c-da-1f-5d-4f')
    @commethod(26)
    def AccessCheck2(self, bstrObjectName: Windows.Win32.Foundation.BSTR, bstrScopeName: Windows.Win32.Foundation.BSTR, lOperation: Int32, plResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def IsInRoleAssignment(self, bstrScopeName: Windows.Win32.Foundation.BSTR, bstrRoleName: Windows.Win32.Foundation.BSTR, pbIsInRole: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetOperations(self, bstrScopeName: Windows.Win32.Foundation.BSTR, ppOperationCollection: POINTER(Windows.Win32.Security.Authorization.IAzOperations_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetTasks(self, bstrScopeName: Windows.Win32.Foundation.BSTR, ppTaskCollection: POINTER(Windows.Win32.Security.Authorization.IAzTasks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_BizRuleParameters(self, ppBizRuleParam: POINTER(Windows.Win32.Security.Authorization.IAzBizRuleParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_BizRuleInterfaces(self, ppBizRuleInterfaces: POINTER(Windows.Win32.Security.Authorization.IAzBizRuleInterfaces_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetGroups(self, bstrScopeName: Windows.Win32.Foundation.BSTR, ulOptions: Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS, pGroupArray: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Sids(self, pStringSidArray: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzNameResolver(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('504d0f15-73e2-43df-a8-70-a6-4f-40-71-4f-53')
    @commethod(7)
    def NameFromSid(self, bstrSid: Windows.Win32.Foundation.BSTR, pSidType: POINTER(Int32), pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NamesFromSids(self, vSids: Windows.Win32.System.Variant.VARIANT, pvSidTypes: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvNames: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzObjectPicker(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('63130a48-699a-42d8-bf-01-c6-2a-c3-fb-79-f9')
    @commethod(7)
    def GetPrincipals(self, hParentWnd: Windows.Win32.Foundation.HWND, bstrTitle: Windows.Win32.Foundation.BSTR, pvSidTypes: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvNames: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvSids: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzOperation(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('5e56b24f-ea01-4d61-be-44-c4-9b-5e-4e-af-74')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OperationID(self, plProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OperationID(self, lProp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IAzOperation2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzOperation
    _iid_ = Guid('1f5ea01f-44a2-4184-9c-48-a7-5b-4d-cc-8c-cc')
    @commethod(19)
    def RoleAssignments(self, bstrScopeName: Windows.Win32.Foundation.BSTR, bRecursive: Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzOperations(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('90ef9c07-9706-49d9-af-80-04-38-a5-f3-ec-35')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzPrincipalLocator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('e5c3507d-ad6a-4992-9c-7f-74-ab-48-0b-44-cc')
    @commethod(7)
    def get_NameResolver(self, ppNameResolver: POINTER(Windows.Win32.Security.Authorization.IAzNameResolver_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ObjectPicker(self, ppObjectPicker: POINTER(Windows.Win32.Security.Authorization.IAzObjectPicker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRole(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('859e0d8d-62d7-41d8-a0-34-c0-cd-5d-43-fd-fa')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddAppMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteAppMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddTask(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteTask(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddOperation(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteOperation(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteMember(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AppMembers(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Members(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Operations(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Tasks(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def AddMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def DeleteMemberName(self, bstrProp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_MembersName(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRoleAssignment(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzRole
    _iid_ = Guid('55647d31-0d5a-4fa3-b4-ac-2b-5f-9a-d5-ab-76')
    @commethod(34)
    def AddRoleDefinition(self, bstrRoleDefinition: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteRoleDefinition(self, bstrRoleDefinition: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_Scope(self, ppScope: POINTER(Windows.Win32.Security.Authorization.IAzScope_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRoleAssignments(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('9c80b900-fceb-4d73-a0-f4-c8-3b-0b-bf-24-81')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRoleDefinition(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzTask
    _iid_ = Guid('d97fcea1-2599-44f1-9f-c3-58-e9-fb-e0-94-66')
    @commethod(33)
    def RoleAssignments(self, bstrScopeName: Windows.Win32.Foundation.BSTR, bRecursive: Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddRoleDefinition(self, bstrRoleDefinition: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteRoleDefinition(self, bstrRoleDefinition: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRoleDefinitions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('881f25a5-d755-4550-95-7a-d5-03-a3-b3-40-01')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzRoles(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('95e0f119-13b4-4dae-b6-5f-2f-7d-60-d8-22-e4')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzScope(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('00e52487-e08d-4514-b6-2e-87-7d-56-45-f5-ab')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddPropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_PolicyReaders(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AddPolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeletePolicyAdministrator(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddPolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeletePolicyReader(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OpenApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(Windows.Win32.Security.Authorization.IAzApplicationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeleteApplicationGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Roles(self, ppRoleCollection: POINTER(Windows.Win32.Security.Authorization.IAzRoles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OpenRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(Windows.Win32.Security.Authorization.IAzRole_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(Windows.Win32.Security.Authorization.IAzRole_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeleteRole(self, bstrRoleName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Tasks(self, ppTaskCollection: POINTER(Windows.Win32.Security.Authorization.IAzTasks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def OpenTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(Windows.Win32.Security.Authorization.IAzTask_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(Windows.Win32.Security.Authorization.IAzTask_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteTask(self, bstrTaskName: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_CanBeDelegated(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_BizrulesWritable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_PolicyReadersName(self, pvarReaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def AddPolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def DeletePolicyAdministratorName(self, bstrAdmin: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddPolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeletePolicyReaderName(self, bstrReader: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IAzScope2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzScope
    _iid_ = Guid('ee9fe8c9-c9f3-40e2-aa-12-d1-d8-59-97-27-fd')
    @commethod(45)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinitions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CreateRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def OpenRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(Windows.Win32.Security.Authorization.IAzRoleDefinition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def DeleteRoleDefinition(self, bstrRoleDefinitionName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_RoleAssignments(self, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def CreateRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def OpenRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def DeleteRoleAssignment(self, bstrRoleAssignmentName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAzScopes(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('78e14853-9f5e-406d-9b-91-6b-db-a6-97-35-10')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzTask(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('cb94e592-2e0e-4a6c-a3-36-b8-9a-6d-c1-e3-88')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BizRule(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_BizRule(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BizRuleLanguage(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_BizRuleLanguage(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BizRuleImportedPath(self, pbstrProp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BizRuleImportedPath(self, bstrProp: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_IsRoleDefinition(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_IsRoleDefinition(self, fProp: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Operations(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Tasks(self, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddOperation(self, bstrOp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteOperation(self, bstrOp: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddTask(self, bstrTask: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DeleteTask(self, bstrTask: Windows.Win32.Foundation.BSTR, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Writable(self, pfProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetProperty(self, lPropId: Int32, varReserved: Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetProperty(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def AddPropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeletePropertyItem(self, lPropId: Int32, varProp: Windows.Win32.System.Variant.VARIANT, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Submit(self, lFlags: Int32, varReserved: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IAzTask2(ComPtr):
    extends: Windows.Win32.Security.Authorization.IAzTask
    _iid_ = Guid('03a9a5ee-48c8-4832-90-25-aa-d5-03-c4-65-26')
    @commethod(33)
    def RoleAssignments(self, bstrScopeName: Windows.Win32.Foundation.BSTR, bRecursive: Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(Windows.Win32.Security.Authorization.IAzRoleAssignments_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAzTasks(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('b338ccab-4c85-4388-8c-0a-c5-85-92-ba-d3-98')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INHERITED_FROMA(EasyCastStructure):
    GenerationGap: Int32
    AncestorName: Windows.Win32.Foundation.PSTR
class INHERITED_FROMW(EasyCastStructure):
    GenerationGap: Int32
    AncestorName: Windows.Win32.Foundation.PWSTR
MULTIPLE_TRUSTEE_OPERATION = Int32
NO_MULTIPLE_TRUSTEE: MULTIPLE_TRUSTEE_OPERATION = 0
TRUSTEE_IS_IMPERSONATE: MULTIPLE_TRUSTEE_OPERATION = 1
class OBJECTS_AND_NAME_A(EasyCastStructure):
    ObjectsPresent: Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE
    ObjectTypeName: Windows.Win32.Foundation.PSTR
    InheritedObjectTypeName: Windows.Win32.Foundation.PSTR
    ptstrName: Windows.Win32.Foundation.PSTR
class OBJECTS_AND_NAME_W(EasyCastStructure):
    ObjectsPresent: Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: Windows.Win32.Security.Authorization.SE_OBJECT_TYPE
    ObjectTypeName: Windows.Win32.Foundation.PWSTR
    InheritedObjectTypeName: Windows.Win32.Foundation.PWSTR
    ptstrName: Windows.Win32.Foundation.PWSTR
class OBJECTS_AND_SID(EasyCastStructure):
    ObjectsPresent: Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectTypeGuid: Guid
    InheritedObjectTypeGuid: Guid
    pSid: POINTER(Windows.Win32.Security.SID_head)
@winfunctype_pointer
def PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, Args: c_void_p, pSidAttrArray: POINTER(POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)), pSidCount: POINTER(UInt32), pRestrictedSidAttrArray: POINTER(POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)), pRestrictedSidCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_AUTHZ_DYNAMIC_ACCESS_CHECK(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pAce: POINTER(Windows.Win32.Security.ACE_HEADER_head), pArgs: c_void_p, pbAceApplicable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY(pCentralAccessPolicy: c_void_p) -> Void: ...
@winfunctype_pointer
def PFN_AUTHZ_FREE_DYNAMIC_GROUPS(pSidAttrArray: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)) -> Void: ...
@winfunctype_pointer
def PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY(hAuthzClientContext: Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, capid: Windows.Win32.Foundation.PSID, pArgs: c_void_p, pCentralAccessPolicyApplicable: POINTER(Windows.Win32.Foundation.BOOL), ppCentralAccessPolicy: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
PROG_INVOKE_SETTING = Int32
PROG_INVOKE_SETTING_ProgressInvokeNever: PROG_INVOKE_SETTING = 1
PROG_INVOKE_SETTING_ProgressInvokeEveryObject: PROG_INVOKE_SETTING = 2
PROG_INVOKE_SETTING_ProgressInvokeOnError: PROG_INVOKE_SETTING = 3
PROG_INVOKE_SETTING_ProgressCancelOperation: PROG_INVOKE_SETTING = 4
PROG_INVOKE_SETTING_ProgressRetryOperation: PROG_INVOKE_SETTING = 5
PROG_INVOKE_SETTING_ProgressInvokePrePostError: PROG_INVOKE_SETTING = 6
SE_OBJECT_TYPE = Int32
SE_UNKNOWN_OBJECT_TYPE: SE_OBJECT_TYPE = 0
SE_FILE_OBJECT: SE_OBJECT_TYPE = 1
SE_SERVICE: SE_OBJECT_TYPE = 2
SE_PRINTER: SE_OBJECT_TYPE = 3
SE_REGISTRY_KEY: SE_OBJECT_TYPE = 4
SE_LMSHARE: SE_OBJECT_TYPE = 5
SE_KERNEL_OBJECT: SE_OBJECT_TYPE = 6
SE_WINDOW_OBJECT: SE_OBJECT_TYPE = 7
SE_DS_OBJECT: SE_OBJECT_TYPE = 8
SE_DS_OBJECT_ALL: SE_OBJECT_TYPE = 9
SE_PROVIDER_DEFINED_OBJECT: SE_OBJECT_TYPE = 10
SE_WMIGUID_OBJECT: SE_OBJECT_TYPE = 11
SE_REGISTRY_WOW64_32KEY: SE_OBJECT_TYPE = 12
SE_REGISTRY_WOW64_64KEY: SE_OBJECT_TYPE = 13
TREE_SEC_INFO = UInt32
TREE_SEC_INFO_SET: TREE_SEC_INFO = 1
TREE_SEC_INFO_RESET: TREE_SEC_INFO = 2
TREE_SEC_INFO_RESET_KEEP_EXPLICIT: TREE_SEC_INFO = 3
class TRUSTEE_A(EasyCastStructure):
    pMultipleTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_A_head)
    MultipleTrusteeOperation: Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION
    TrusteeForm: Windows.Win32.Security.Authorization.TRUSTEE_FORM
    TrusteeType: Windows.Win32.Security.Authorization.TRUSTEE_TYPE
    ptstrName: Windows.Win32.Foundation.PSTR
class TRUSTEE_ACCESSA(EasyCastStructure):
    lpProperty: Windows.Win32.Foundation.PSTR
    Access: UInt32
    fAccessFlags: UInt32
    fReturnedAccess: UInt32
class TRUSTEE_ACCESSW(EasyCastStructure):
    lpProperty: Windows.Win32.Foundation.PWSTR
    Access: UInt32
    fAccessFlags: UInt32
    fReturnedAccess: UInt32
TRUSTEE_FORM = Int32
TRUSTEE_IS_SID: TRUSTEE_FORM = 0
TRUSTEE_IS_NAME: TRUSTEE_FORM = 1
TRUSTEE_BAD_FORM: TRUSTEE_FORM = 2
TRUSTEE_IS_OBJECTS_AND_SID: TRUSTEE_FORM = 3
TRUSTEE_IS_OBJECTS_AND_NAME: TRUSTEE_FORM = 4
TRUSTEE_TYPE = Int32
TRUSTEE_IS_UNKNOWN: TRUSTEE_TYPE = 0
TRUSTEE_IS_USER: TRUSTEE_TYPE = 1
TRUSTEE_IS_GROUP: TRUSTEE_TYPE = 2
TRUSTEE_IS_DOMAIN: TRUSTEE_TYPE = 3
TRUSTEE_IS_ALIAS: TRUSTEE_TYPE = 4
TRUSTEE_IS_WELL_KNOWN_GROUP: TRUSTEE_TYPE = 5
TRUSTEE_IS_DELETED: TRUSTEE_TYPE = 6
TRUSTEE_IS_INVALID: TRUSTEE_TYPE = 7
TRUSTEE_IS_COMPUTER: TRUSTEE_TYPE = 8
class TRUSTEE_W(EasyCastStructure):
    pMultipleTrustee: POINTER(Windows.Win32.Security.Authorization.TRUSTEE_W_head)
    MultipleTrusteeOperation: Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION
    TrusteeForm: Windows.Win32.Security.Authorization.TRUSTEE_FORM
    TrusteeType: Windows.Win32.Security.Authorization.TRUSTEE_TYPE
    ptstrName: Windows.Win32.Foundation.PWSTR
make_head(_module, 'ACTRL_ACCESSA')
make_head(_module, 'ACTRL_ACCESSW')
make_head(_module, 'ACTRL_ACCESS_ENTRYA')
make_head(_module, 'ACTRL_ACCESS_ENTRYW')
make_head(_module, 'ACTRL_ACCESS_ENTRY_LISTA')
make_head(_module, 'ACTRL_ACCESS_ENTRY_LISTW')
make_head(_module, 'ACTRL_ACCESS_INFOA')
make_head(_module, 'ACTRL_ACCESS_INFOW')
make_head(_module, 'ACTRL_CONTROL_INFOA')
make_head(_module, 'ACTRL_CONTROL_INFOW')
make_head(_module, 'ACTRL_OVERLAPPED')
make_head(_module, 'ACTRL_PROPERTY_ENTRYA')
make_head(_module, 'ACTRL_PROPERTY_ENTRYW')
make_head(_module, 'AUDIT_IP_ADDRESS')
make_head(_module, 'AUDIT_OBJECT_TYPE')
make_head(_module, 'AUDIT_OBJECT_TYPES')
make_head(_module, 'AUDIT_PARAM')
make_head(_module, 'AUDIT_PARAMS')
make_head(_module, 'AUTHZ_ACCESS_REPLY')
make_head(_module, 'AUTHZ_ACCESS_REQUEST')
make_head(_module, 'AUTHZ_AUDIT_EVENT_TYPE_LEGACY')
make_head(_module, 'AUTHZ_AUDIT_EVENT_TYPE_OLD')
make_head(_module, 'AUTHZ_AUDIT_EVENT_TYPE_UNION')
make_head(_module, 'AUTHZ_INIT_INFO')
make_head(_module, 'AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET')
make_head(_module, 'AUTHZ_RPC_INIT_INFO_CLIENT')
make_head(_module, 'AUTHZ_SECURITY_ATTRIBUTES_INFORMATION')
make_head(_module, 'AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE')
make_head(_module, 'AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE')
make_head(_module, 'AUTHZ_SECURITY_ATTRIBUTE_V1')
make_head(_module, 'AUTHZ_SOURCE_SCHEMA_REGISTRATION')
make_head(_module, 'EXPLICIT_ACCESS_A')
make_head(_module, 'EXPLICIT_ACCESS_W')
make_head(_module, 'FN_OBJECT_MGR_FUNCTS')
make_head(_module, 'FN_PROGRESS')
make_head(_module, 'IAzApplication')
make_head(_module, 'IAzApplication2')
make_head(_module, 'IAzApplication3')
make_head(_module, 'IAzApplicationGroup')
make_head(_module, 'IAzApplicationGroup2')
make_head(_module, 'IAzApplicationGroups')
make_head(_module, 'IAzApplications')
make_head(_module, 'IAzAuthorizationStore')
make_head(_module, 'IAzAuthorizationStore2')
make_head(_module, 'IAzAuthorizationStore3')
make_head(_module, 'IAzBizRuleContext')
make_head(_module, 'IAzBizRuleInterfaces')
make_head(_module, 'IAzBizRuleParameters')
make_head(_module, 'IAzClientContext')
make_head(_module, 'IAzClientContext2')
make_head(_module, 'IAzClientContext3')
make_head(_module, 'IAzNameResolver')
make_head(_module, 'IAzObjectPicker')
make_head(_module, 'IAzOperation')
make_head(_module, 'IAzOperation2')
make_head(_module, 'IAzOperations')
make_head(_module, 'IAzPrincipalLocator')
make_head(_module, 'IAzRole')
make_head(_module, 'IAzRoleAssignment')
make_head(_module, 'IAzRoleAssignments')
make_head(_module, 'IAzRoleDefinition')
make_head(_module, 'IAzRoleDefinitions')
make_head(_module, 'IAzRoles')
make_head(_module, 'IAzScope')
make_head(_module, 'IAzScope2')
make_head(_module, 'IAzScopes')
make_head(_module, 'IAzTask')
make_head(_module, 'IAzTask2')
make_head(_module, 'IAzTasks')
make_head(_module, 'INHERITED_FROMA')
make_head(_module, 'INHERITED_FROMW')
make_head(_module, 'OBJECTS_AND_NAME_A')
make_head(_module, 'OBJECTS_AND_NAME_W')
make_head(_module, 'OBJECTS_AND_SID')
make_head(_module, 'PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS')
make_head(_module, 'PFN_AUTHZ_DYNAMIC_ACCESS_CHECK')
make_head(_module, 'PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY')
make_head(_module, 'PFN_AUTHZ_FREE_DYNAMIC_GROUPS')
make_head(_module, 'PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY')
make_head(_module, 'TRUSTEE_A')
make_head(_module, 'TRUSTEE_ACCESSA')
make_head(_module, 'TRUSTEE_ACCESSW')
make_head(_module, 'TRUSTEE_W')
