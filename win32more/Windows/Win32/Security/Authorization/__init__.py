from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Authorization
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Threading
import win32more.Windows.Win32.System.Variant
ACCESS_MODE = Int32
NOT_USED_ACCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 0
GRANT_ACCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 1
SET_ACCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 2
DENY_ACCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 3
REVOKE_ACCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 4
SET_AUDIT_SUCCESS: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 5
SET_AUDIT_FAILURE: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE = 6
class ACTRL_ACCESSA(Structure):
    cEntries: UInt32
    pPropertyAccessList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_PROPERTY_ENTRYA)
class ACTRL_ACCESSW(Structure):
    cEntries: UInt32
    pPropertyAccessList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_PROPERTY_ENTRYW)
ACTRL_ACCESS = UnicodeAlias('ACTRL_ACCESSW')
class ACTRL_ACCESS_ENTRYA(Structure):
    Trustee: win32more.Windows.Win32.Security.Authorization.TRUSTEE_A
    fAccessFlags: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS
    Access: UInt32
    ProvSpecificAccess: UInt32
    Inheritance: win32more.Windows.Win32.Security.ACE_FLAGS
    lpInheritProperty: win32more.Windows.Win32.Foundation.PSTR
class ACTRL_ACCESS_ENTRYW(Structure):
    Trustee: win32more.Windows.Win32.Security.Authorization.TRUSTEE_W
    fAccessFlags: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS
    Access: UInt32
    ProvSpecificAccess: UInt32
    Inheritance: win32more.Windows.Win32.Security.ACE_FLAGS
    lpInheritProperty: win32more.Windows.Win32.Foundation.PWSTR
ACTRL_ACCESS_ENTRY = UnicodeAlias('ACTRL_ACCESS_ENTRYW')
ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = UInt32
ACTRL_ACCESS_ALLOWED: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 1
ACTRL_ACCESS_DENIED: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 2
ACTRL_AUDIT_SUCCESS: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 4
ACTRL_AUDIT_FAILURE: win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = 8
class ACTRL_ACCESS_ENTRY_LISTA(Structure):
    cEntries: UInt32
    pAccessList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRYA)
class ACTRL_ACCESS_ENTRY_LISTW(Structure):
    cEntries: UInt32
    pAccessList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRYW)
ACTRL_ACCESS_ENTRY_LIST = UnicodeAlias('ACTRL_ACCESS_ENTRY_LISTW')
class ACTRL_ACCESS_INFOA(Structure):
    fAccessPermission: UInt32
    lpAccessPermissionName: win32more.Windows.Win32.Foundation.PSTR
class ACTRL_ACCESS_INFOW(Structure):
    fAccessPermission: UInt32
    lpAccessPermissionName: win32more.Windows.Win32.Foundation.PWSTR
ACTRL_ACCESS_INFO = UnicodeAlias('ACTRL_ACCESS_INFOW')
class ACTRL_CONTROL_INFOA(Structure):
    lpControlId: win32more.Windows.Win32.Foundation.PSTR
    lpControlName: win32more.Windows.Win32.Foundation.PSTR
class ACTRL_CONTROL_INFOW(Structure):
    lpControlId: win32more.Windows.Win32.Foundation.PWSTR
    lpControlName: win32more.Windows.Win32.Foundation.PWSTR
ACTRL_CONTROL_INFO = UnicodeAlias('ACTRL_CONTROL_INFOW')
class ACTRL_OVERLAPPED(Structure):
    Anonymous: _Anonymous_e__Union
    Reserved2: UInt32
    hEvent: win32more.Windows.Win32.Foundation.HANDLE
    class _Anonymous_e__Union(Union):
        Provider: VoidPtr
        Reserved1: UInt32
class ACTRL_PROPERTY_ENTRYA(Structure):
    lpProperty: win32more.Windows.Win32.Foundation.PSTR
    pAccessEntryList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTA)
    fListFlags: UInt32
class ACTRL_PROPERTY_ENTRYW(Structure):
    lpProperty: win32more.Windows.Win32.Foundation.PWSTR
    pAccessEntryList: POINTER(win32more.Windows.Win32.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTW)
    fListFlags: UInt32
ACTRL_PROPERTY_ENTRY = UnicodeAlias('ACTRL_PROPERTY_ENTRYW')
class AUDIT_IP_ADDRESS(Structure):
    pIpAddress: Byte * 128
class AUDIT_OBJECT_TYPE(Structure):
    ObjectType: Guid
    Flags: UInt16
    Level: UInt16
    AccessMask: UInt32
class AUDIT_OBJECT_TYPES(Structure):
    Count: UInt16
    Flags: UInt16
    pObjectTypes: POINTER(win32more.Windows.Win32.Security.Authorization.AUDIT_OBJECT_TYPE)
class AUDIT_PARAM(Structure):
    Type: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE
    Length: UInt32
    Flags: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        Data0: UIntPtr
        String: win32more.Windows.Win32.Foundation.PWSTR
        u: UIntPtr
        psid: POINTER(win32more.Windows.Win32.Security.SID)
        pguid: POINTER(Guid)
        LogonId_LowPart: UInt32
        pObjectTypes: POINTER(win32more.Windows.Win32.Security.Authorization.AUDIT_OBJECT_TYPES)
        pIpAddress: POINTER(win32more.Windows.Win32.Security.Authorization.AUDIT_IP_ADDRESS)
    class _Anonymous2_e__Union(Union):
        Data1: UIntPtr
        LogonId_HighPart: Int32
class AUDIT_PARAMS(Structure):
    Length: UInt32
    Flags: UInt32
    Count: UInt16
    Parameters: POINTER(win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM)
AUDIT_PARAM_TYPE = Int32
APT_None: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 1
APT_String: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 2
APT_Ulong: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 3
APT_Pointer: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 4
APT_Sid: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 5
APT_LogonId: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 6
APT_ObjectTypeList: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 7
APT_Luid: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 8
APT_Guid: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 9
APT_Time: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 10
APT_Int64: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 11
APT_IpAddress: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 12
APT_LogonIdWithSid: win32more.Windows.Win32.Security.Authorization.AUDIT_PARAM_TYPE = 13
AUTHZ_ACCESS_CHECK_FLAGS = UInt32
AUTHZ_ACCESS_CHECK_NO_DEEP_COPY_SD: win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_FLAGS = 1
AUTHZ_ACCESS_CHECK_RESULTS_HANDLE = VoidPtr
class AUTHZ_ACCESS_REPLY(Structure):
    ResultListLength: UInt32
    GrantedAccessMask: POINTER(UInt32)
    SaclEvaluationResults: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_GENERATE_RESULTS)
    Error: POINTER(UInt32)
class AUTHZ_ACCESS_REQUEST(Structure):
    DesiredAccess: UInt32
    PrincipalSelfSid: win32more.Windows.Win32.Security.PSID
    ObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST)
    ObjectTypeListLength: UInt32
    OptionalArguments: VoidPtr
AUTHZ_AUDIT_EVENT_HANDLE = VoidPtr
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = Int32
AuthzAuditEventInfoFlags: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 1
AuthzAuditEventInfoOperationType: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 2
AuthzAuditEventInfoObjectType: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 3
AuthzAuditEventInfoObjectName: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 4
AuthzAuditEventInfoAdditionalInfo: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = 5
AUTHZ_AUDIT_EVENT_TYPE_HANDLE = VoidPtr
class AUTHZ_AUDIT_EVENT_TYPE_LEGACY(Structure):
    CategoryId: UInt16
    AuditId: UInt16
    ParameterCount: UInt16
class AUTHZ_AUDIT_EVENT_TYPE_OLD(Structure):
    Version: UInt32
    dwFlags: UInt32
    RefCount: Int32
    hAudit: UIntPtr
    LinkId: win32more.Windows.Win32.Foundation.LUID
    u: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_UNION
class AUTHZ_AUDIT_EVENT_TYPE_UNION(Union):
    Legacy: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_LEGACY
AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE = VoidPtr
AUTHZ_CLIENT_CONTEXT_HANDLE = VoidPtr
AUTHZ_CONTEXT_INFORMATION_CLASS = Int32
AuthzContextInfoUserSid: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 1
AuthzContextInfoGroupsSids: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 2
AuthzContextInfoRestrictedSids: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 3
AuthzContextInfoPrivileges: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 4
AuthzContextInfoExpirationTime: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 5
AuthzContextInfoServerContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 6
AuthzContextInfoIdentifier: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 7
AuthzContextInfoSource: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 8
AuthzContextInfoAll: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 9
AuthzContextInfoAuthenticationId: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 10
AuthzContextInfoSecurityAttributes: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 11
AuthzContextInfoDeviceSids: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 12
AuthzContextInfoUserClaims: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 13
AuthzContextInfoDeviceClaims: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 14
AuthzContextInfoAppContainerSid: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 15
AuthzContextInfoCapabilitySids: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS = 16
AUTHZ_GENERATE_RESULTS = UInt32
AUTHZ_GENERATE_SUCCESS_AUDIT: win32more.Windows.Win32.Security.Authorization.AUTHZ_GENERATE_RESULTS = 1
AUTHZ_GENERATE_FAILURE_AUDIT: win32more.Windows.Win32.Security.Authorization.AUTHZ_GENERATE_RESULTS = 2
AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = UInt32
AUTHZ_NO_SUCCESS_AUDIT: win32more.Windows.Win32.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 1
AUTHZ_NO_FAILURE_AUDIT: win32more.Windows.Win32.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 2
AUTHZ_NO_ALLOC_STRINGS: win32more.Windows.Win32.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = 4
class AUTHZ_INIT_INFO(Structure):
    version: UInt16
    szResourceManagerName: win32more.Windows.Win32.Foundation.PWSTR
    pfnDynamicAccessCheck: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK
    pfnComputeDynamicGroups: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS
    pfnFreeDynamicGroups: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS
    pfnGetCentralAccessPolicy: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY
    pfnFreeCentralAccessPolicy: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY
class AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET(Structure):
    szObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR
    dwOffset: UInt32
AUTHZ_RESOURCE_MANAGER_FLAGS = UInt32
AUTHZ_RM_FLAG_NO_AUDIT: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS = 1
AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS = 2
AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS = 4
AUTHZ_RESOURCE_MANAGER_HANDLE = VoidPtr
class AUTHZ_RPC_INIT_INFO_CLIENT(Structure):
    version: UInt16
    ObjectUuid: win32more.Windows.Win32.Foundation.PWSTR
    ProtSeq: win32more.Windows.Win32.Foundation.PWSTR
    NetworkAddr: win32more.Windows.Win32.Foundation.PWSTR
    Endpoint: win32more.Windows.Win32.Foundation.PWSTR
    Options: win32more.Windows.Win32.Foundation.PWSTR
    ServerSpn: win32more.Windows.Win32.Foundation.PWSTR
class AUTHZ_SECURITY_ATTRIBUTES_INFORMATION(Structure):
    Version: UInt16
    Reserved: UInt16
    AttributeCount: UInt32
    Attribute: _Attribute_e__Union
    class _Attribute_e__Union(Union):
        pAttributeV1: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_V1)
AUTHZ_SECURITY_ATTRIBUTE_FLAGS = UInt32
AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FLAGS = 1
AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FLAGS = 2
class AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE(Structure):
    Version: UInt64
    pName: win32more.Windows.Win32.Foundation.PWSTR
class AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(Structure):
    pValue: VoidPtr
    ValueLength: UInt32
AUTHZ_SECURITY_ATTRIBUTE_OPERATION = Int32
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 0
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 1
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 2
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 3
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION = 4
class AUTHZ_SECURITY_ATTRIBUTE_V1(Structure):
    pName: win32more.Windows.Win32.Foundation.PWSTR
    ValueType: UInt16
    Reserved: UInt16
    Flags: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FLAGS
    ValueCount: UInt32
    Values: _Values_e__Union
    class _Values_e__Union(Union):
        pInt64: POINTER(Int64)
        pUint64: POINTER(UInt64)
        ppString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        pFqbn: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE)
        pOctetString: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE)
AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE = VoidPtr
AUTHZ_SID_OPERATION = Int32
AUTHZ_SID_OPERATION_NONE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION = 0
AUTHZ_SID_OPERATION_REPLACE_ALL: win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION = 1
AUTHZ_SID_OPERATION_ADD: win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION = 2
AUTHZ_SID_OPERATION_DELETE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION = 3
AUTHZ_SID_OPERATION_REPLACE: win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION = 4
class AUTHZ_SOURCE_SCHEMA_REGISTRATION(Structure):
    dwFlags: UInt32
    szEventSourceName: win32more.Windows.Win32.Foundation.PWSTR
    szEventMessageFile: win32more.Windows.Win32.Foundation.PWSTR
    szEventSourceXmlSchemaFile: win32more.Windows.Win32.Foundation.PWSTR
    szEventAccessStringsFile: win32more.Windows.Win32.Foundation.PWSTR
    szExecutableImagePath: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    dwObjectTypeNameCount: UInt32
    ObjectTypeNames: win32more.Windows.Win32.Security.Authorization.AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET * 1
    class _Anonymous_e__Union(Union):
        pReserved: VoidPtr
        pProviderGuid: POINTER(Guid)
AZ_PROP_CONSTANTS = Int32
AZ_PROP_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_PROP_DESCRIPTION: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
AZ_PROP_WRITABLE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 3
AZ_PROP_APPLICATION_DATA: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 4
AZ_PROP_CHILD_CREATE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 5
AZ_MAX_APPLICATION_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 512
AZ_MAX_OPERATION_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_TASK_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_SCOPE_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_MAX_GROUP_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_ROLE_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_NAME_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_MAX_DESCRIPTION_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1024
AZ_MAX_APPLICATION_DATA_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 4096
AZ_SUBMIT_FLAG_ABORT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_SUBMIT_FLAG_FLUSH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
AZ_MAX_POLICY_URL_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_AZSTORE_FLAG_CREATE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
AZ_AZSTORE_FLAG_BATCH_UPDATE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 4
AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 8
AZ_AZSTORE_FORCE_APPLICATION_CLOSE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 16
AZ_AZSTORE_NT6_FUNCTION_LEVEL: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 32
AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 32768
AZ_PROP_AZSTORE_DOMAIN_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 100
AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 15000
AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 101
AZ_AZSTORE_MIN_DOMAIN_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 500
AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 5000
AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 45000
AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 102
AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 120
AZ_PROP_AZSTORE_MAJOR_VERSION: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 103
AZ_PROP_AZSTORE_MINOR_VERSION: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 104
AZ_PROP_AZSTORE_TARGET_MACHINE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 105
AZ_PROP_AZTORE_IS_ADAM_INSTANCE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 106
AZ_PROP_OPERATION_ID: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 200
AZ_PROP_TASK_OPERATIONS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 300
AZ_PROP_TASK_BIZRULE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 301
AZ_PROP_TASK_BIZRULE_LANGUAGE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 302
AZ_PROP_TASK_TASKS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 303
AZ_PROP_TASK_BIZRULE_IMPORTED_PATH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 304
AZ_PROP_TASK_IS_ROLE_DEFINITION: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 305
AZ_MAX_TASK_BIZRULE_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 512
AZ_MAX_BIZRULE_STRING: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_PROP_GROUP_TYPE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 400
AZ_GROUPTYPE_LDAP_QUERY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_GROUPTYPE_BASIC: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
AZ_GROUPTYPE_BIZRULE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 3
AZ_PROP_GROUP_APP_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 401
AZ_PROP_GROUP_APP_NON_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 402
AZ_PROP_GROUP_LDAP_QUERY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 403
AZ_MAX_GROUP_LDAP_QUERY_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 4096
AZ_PROP_GROUP_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 404
AZ_PROP_GROUP_NON_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 405
AZ_PROP_GROUP_MEMBERS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 406
AZ_PROP_GROUP_NON_MEMBERS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 407
AZ_PROP_GROUP_BIZRULE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 408
AZ_PROP_GROUP_BIZRULE_LANGUAGE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 409
AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 410
AZ_MAX_GROUP_BIZRULE_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 65536
AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 64
AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 512
AZ_PROP_ROLE_APP_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 500
AZ_PROP_ROLE_MEMBERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 501
AZ_PROP_ROLE_OPERATIONS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 502
AZ_PROP_ROLE_TASKS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 504
AZ_PROP_ROLE_MEMBERS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 505
AZ_PROP_SCOPE_BIZRULES_WRITABLE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 600
AZ_PROP_SCOPE_CAN_BE_DELEGATED: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 601
AZ_PROP_CLIENT_CONTEXT_USER_DN: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 700
AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 701
AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 702
AZ_PROP_CLIENT_CONTEXT_USER_GUID: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 703
AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 704
AZ_PROP_CLIENT_CONTEXT_USER_UPN: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 705
AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 707
AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 708
AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 709
AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 800
AZ_PROP_APPLICATION_VERSION: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 801
AZ_MAX_APPLICATION_VERSION_LENGTH: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 512
AZ_PROP_APPLICATION_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 802
AZ_PROP_APPLICATION_BIZRULE_ENABLED: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 803
AZ_PROP_APPLY_STORE_SACL: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 900
AZ_PROP_GENERATE_AUDITS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 901
AZ_PROP_POLICY_ADMINS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 902
AZ_PROP_POLICY_READERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 903
AZ_PROP_DELEGATED_POLICY_USERS: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 904
AZ_PROP_POLICY_ADMINS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 905
AZ_PROP_POLICY_READERS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 906
AZ_PROP_DELEGATED_POLICY_USERS_NAME: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 907
AZ_CLIENT_CONTEXT_SKIP_GROUP: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 1
AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS = 2
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
OLESCRIPT_E_SYNTAX: win32more.Windows.Win32.Foundation.HRESULT = -2147352319
@winfunctype('AUTHZ.dll')
def AuthzAccessCheck(Flags: win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_FLAGS, hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST), hAuditEvent: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, OptionalSecurityDescriptorArray: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), OptionalSecurityDescriptorCount: UInt32, pReply: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY), phAccessCheckResults: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzCachedAccessCheck(Flags: UInt32, hAccessCheckResults: win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE, pRequest: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST), hAuditEvent: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pReply: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzOpenObjectAudit(Flags: UInt32, hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST), hAuditEvent: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, OptionalSecurityDescriptorArray: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), OptionalSecurityDescriptorCount: UInt32, pReply: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REPLY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeHandle(hAccessCheckResults: win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeResourceManager(Flags: UInt32, pfnDynamicAccessCheck: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK, pfnComputeDynamicGroups: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS, pfnFreeDynamicGroups: win32more.Windows.Win32.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS, szResourceManagerName: win32more.Windows.Win32.Foundation.PWSTR, phAuthzResourceManager: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeResourceManagerEx(Flags: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS, pAuthzInitInfo: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_INIT_INFO), phAuthzResourceManager: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeRemoteResourceManager(pRpcInitInfo: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_RPC_INIT_INFO_CLIENT), phAuthzResourceManager: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeResourceManager(hAuthzResourceManager: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromToken(Flags: UInt32, TokenHandle: win32more.Windows.Win32.Foundation.HANDLE, hAuthzResourceManager: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE, pExpirationTime: POINTER(Int64), Identifier: win32more.Windows.Win32.Foundation.LUID, DynamicGroupArgs: VoidPtr, phAuthzClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromSid(Flags: UInt32, UserSid: win32more.Windows.Win32.Security.PSID, hAuthzResourceManager: win32more.Windows.Win32.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE, pExpirationTime: POINTER(Int64), Identifier: win32more.Windows.Win32.Foundation.LUID, DynamicGroupArgs: VoidPtr, phAuthzClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeContextFromAuthzContext(Flags: UInt32, hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pExpirationTime: POINTER(Int64), Identifier: win32more.Windows.Win32.Foundation.LUID, DynamicGroupArgs: VoidPtr, phNewAuthzClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInitializeCompoundContext(UserContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, DeviceContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, phCompoundContext: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzAddSidsToContext(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, Sids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES), SidCount: UInt32, RestrictedSids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES), RestrictedSidCount: UInt32, phNewAuthzClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifySecurityAttributes(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pAttributes: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifyClaims(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, ClaimClass: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, pClaimOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pClaims: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzModifySids(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, SidClass: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, pSidOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pSids: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzSetAppContainerInformation(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pAppContainerSid: win32more.Windows.Win32.Security.PSID, CapabilityCount: UInt32, pCapabilitySids: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzGetInformationFromContext(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, InfoClass: win32more.Windows.Win32.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS, BufferSize: UInt32, pSizeRequired: POINTER(UInt32), Buffer: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeContext(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzInitializeObjectAccessAuditEvent(Flags: win32more.Windows.Win32.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS, hAuditEventType: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE, szOperationType: win32more.Windows.Win32.Foundation.PWSTR, szObjectType: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, szAdditionalInfo: win32more.Windows.Win32.Foundation.PWSTR, phAuditEvent: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE), dwAdditionalParameterCount: UInt32, *__arglist) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzInitializeObjectAccessAuditEvent2(Flags: UInt32, hAuditEventType: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE, szOperationType: win32more.Windows.Win32.Foundation.PWSTR, szObjectType: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, szAdditionalInfo: win32more.Windows.Win32.Foundation.PWSTR, szAdditionalInfo2: win32more.Windows.Win32.Foundation.PWSTR, phAuditEvent: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE), dwAdditionalParameterCount: UInt32, *__arglist) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeAuditEvent(hAuditEvent: win32more.Windows.Win32.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzEvaluateSacl(AuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pRequest: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_ACCESS_REQUEST), Sacl: POINTER(win32more.Windows.Win32.Security.ACL), GrantedAccess: UInt32, AccessGranted: win32more.Windows.Win32.Foundation.BOOL, pbGenerateAudit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzInstallSecurityEventSource(dwFlags: UInt32, pRegistration: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUninstallSecurityEventSource(dwFlags: UInt32, szEventSourceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzEnumerateSecurityEventSources(dwFlags: UInt32, Buffer: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION), pdwCount: POINTER(UInt32), pdwLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzRegisterSecurityEventSource(dwFlags: UInt32, szEventSourceName: win32more.Windows.Win32.Foundation.PWSTR, phEventProvider: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUnregisterSecurityEventSource(dwFlags: UInt32, phEventProvider: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('AUTHZ.dll', variadic=True)
def AuthzReportSecurityEvent(dwFlags: UInt32, hEventProvider: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE, dwAuditId: UInt32, pUserSid: win32more.Windows.Win32.Security.PSID, dwCount: UInt32, *__arglist) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzReportSecurityEventFromParams(dwFlags: UInt32, hEventProvider: win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE, dwAuditId: UInt32, pUserSid: win32more.Windows.Win32.Security.PSID, pParams: POINTER(win32more.Windows.Win32.Security.Authorization.AUDIT_PARAMS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzRegisterCapChangeNotification(phCapChangeSubscription: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE), pfnCapChangeCallback: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pCallbackContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzUnregisterCapChangeNotification(hCapChangeSubscription: win32more.Windows.Win32.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('AUTHZ.dll')
def AuthzFreeCentralAccessPolicyCache() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def SetEntriesInAclA(cCountOfExplicitEntries: UInt32, pListOfExplicitEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A), OldAcl: POINTER(win32more.Windows.Win32.Security.ACL), NewAcl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetEntriesInAclW(cCountOfExplicitEntries: UInt32, pListOfExplicitEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W), OldAcl: POINTER(win32more.Windows.Win32.Security.ACL), NewAcl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SetEntriesInAcl = UnicodeAlias('SetEntriesInAclW')
@winfunctype('ADVAPI32.dll')
def GetExplicitEntriesFromAclA(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pcCountOfExplicitEntries: POINTER(UInt32), pListOfExplicitEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetExplicitEntriesFromAclW(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pcCountOfExplicitEntries: POINTER(UInt32), pListOfExplicitEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W))) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
GetExplicitEntriesFromAcl = UnicodeAlias('GetExplicitEntriesFromAclW')
@winfunctype('ADVAPI32.dll')
def GetEffectiveRightsFromAclA(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pAccessRights: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetEffectiveRightsFromAclW(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pAccessRights: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
GetEffectiveRightsFromAcl = UnicodeAlias('GetEffectiveRightsFromAclW')
@winfunctype('ADVAPI32.dll')
def GetAuditedPermissionsFromAclA(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pSuccessfulAuditedRights: POINTER(UInt32), pFailedAuditRights: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetAuditedPermissionsFromAclW(pacl: POINTER(win32more.Windows.Win32.Security.ACL), pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pSuccessfulAuditedRights: POINTER(UInt32), pFailedAuditRights: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
GetAuditedPermissionsFromAcl = UnicodeAlias('GetAuditedPermissionsFromAclW')
@winfunctype('ADVAPI32.dll')
def GetNamedSecurityInfoA(pObjectName: win32more.Windows.Win32.Foundation.PSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppsidOwner: POINTER(win32more.Windows.Win32.Security.PSID), ppsidGroup: POINTER(win32more.Windows.Win32.Security.PSID), ppDacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetNamedSecurityInfoW(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppsidOwner: POINTER(win32more.Windows.Win32.Security.PSID), ppsidGroup: POINTER(win32more.Windows.Win32.Security.PSID), ppDacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
GetNamedSecurityInfo = UnicodeAlias('GetNamedSecurityInfoW')
@winfunctype('ADVAPI32.dll')
def GetSecurityInfo(handle: win32more.Windows.Win32.Foundation.HANDLE, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppsidOwner: POINTER(win32more.Windows.Win32.Security.PSID), ppsidGroup: POINTER(win32more.Windows.Win32.Security.PSID), ppDacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSacl: POINTER(POINTER(win32more.Windows.Win32.Security.ACL)), ppSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetNamedSecurityInfoA(pObjectName: win32more.Windows.Win32.Foundation.PSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, psidOwner: win32more.Windows.Win32.Security.PSID, psidGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def SetNamedSecurityInfoW(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, psidOwner: win32more.Windows.Win32.Security.PSID, psidGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SetNamedSecurityInfo = UnicodeAlias('SetNamedSecurityInfoW')
@winfunctype('ADVAPI32.dll')
def SetSecurityInfo(handle: win32more.Windows.Win32.Foundation.HANDLE, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, psidOwner: win32more.Windows.Win32.Security.PSID, psidGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetInheritanceSourceA(pObjectName: win32more.Windows.Win32.Foundation.PSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, Container: win32more.Windows.Win32.Foundation.BOOL, pObjectClassGuids: POINTER(POINTER(Guid)), GuidCount: UInt32, pAcl: POINTER(win32more.Windows.Win32.Security.ACL), pfnArray: POINTER(win32more.Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS), pGenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), pInheritArray: POINTER(win32more.Windows.Win32.Security.Authorization.INHERITED_FROMA)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def GetInheritanceSourceW(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, Container: win32more.Windows.Win32.Foundation.BOOL, pObjectClassGuids: POINTER(POINTER(Guid)), GuidCount: UInt32, pAcl: POINTER(win32more.Windows.Win32.Security.ACL), pfnArray: POINTER(win32more.Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS), pGenericMapping: POINTER(win32more.Windows.Win32.Security.GENERIC_MAPPING), pInheritArray: POINTER(win32more.Windows.Win32.Security.Authorization.INHERITED_FROMW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
GetInheritanceSource = UnicodeAlias('GetInheritanceSourceW')
@winfunctype('ADVAPI32.dll')
def FreeInheritedFromArray(pInheritArray: POINTER(win32more.Windows.Win32.Security.Authorization.INHERITED_FROMW), AceCnt: UInt16, pfnArray: POINTER(win32more.Windows.Win32.Security.Authorization.FN_OBJECT_MGR_FUNCTS)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeResetNamedSecurityInfoA(pObjectName: win32more.Windows.Win32.Foundation.PSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pOwner: win32more.Windows.Win32.Security.PSID, pGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL), KeepExplicit: win32more.Windows.Win32.Foundation.BOOL, fnProgress: win32more.Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeResetNamedSecurityInfoW(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pOwner: win32more.Windows.Win32.Security.PSID, pGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL), KeepExplicit: win32more.Windows.Win32.Foundation.BOOL, fnProgress: win32more.Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
TreeResetNamedSecurityInfo = UnicodeAlias('TreeResetNamedSecurityInfoW')
@winfunctype('ADVAPI32.dll')
def TreeSetNamedSecurityInfoA(pObjectName: win32more.Windows.Win32.Foundation.PSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pOwner: win32more.Windows.Win32.Security.PSID, pGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL), dwAction: win32more.Windows.Win32.Security.Authorization.TREE_SEC_INFO, fnProgress: win32more.Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def TreeSetNamedSecurityInfoW(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, SecurityInfo: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pOwner: win32more.Windows.Win32.Security.PSID, pGroup: win32more.Windows.Win32.Security.PSID, pDacl: POINTER(win32more.Windows.Win32.Security.ACL), pSacl: POINTER(win32more.Windows.Win32.Security.ACL), dwAction: win32more.Windows.Win32.Security.Authorization.TREE_SEC_INFO, fnProgress: win32more.Windows.Win32.Security.Authorization.FN_PROGRESS, ProgressInvokeSetting: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING, Args: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
TreeSetNamedSecurityInfo = UnicodeAlias('TreeSetNamedSecurityInfoW')
@winfunctype('ADVAPI32.dll')
def BuildSecurityDescriptorA(pOwner: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pGroup: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), cCountOfAccessEntries: UInt32, pListOfAccessEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A), cCountOfAuditEntries: UInt32, pListOfAuditEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A), pOldSD: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pSizeNewSD: POINTER(UInt32), pNewSD: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def BuildSecurityDescriptorW(pOwner: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pGroup: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), cCountOfAccessEntries: UInt32, pListOfAccessEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W), cCountOfAuditEntries: UInt32, pListOfAuditEntries: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W), pOldSD: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, pSizeNewSD: POINTER(UInt32), pNewSD: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
BuildSecurityDescriptor = UnicodeAlias('BuildSecurityDescriptorW')
@winfunctype('ADVAPI32.dll')
def LookupSecurityDescriptorPartsA(ppOwner: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)), ppGroup: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)), pcCountOfAccessEntries: POINTER(UInt32), ppListOfAccessEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A)), pcCountOfAuditEntries: POINTER(UInt32), ppListOfAuditEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A)), pSD: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def LookupSecurityDescriptorPartsW(ppOwner: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)), ppGroup: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)), pcCountOfAccessEntries: POINTER(UInt32), ppListOfAccessEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W)), pcCountOfAuditEntries: POINTER(UInt32), ppListOfAuditEntries: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W)), pSD: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
LookupSecurityDescriptorParts = UnicodeAlias('LookupSecurityDescriptorPartsW')
@winfunctype('ADVAPI32.dll')
def BuildExplicitAccessWithNameA(pExplicitAccess: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A), pTrusteeName: win32more.Windows.Win32.Foundation.PSTR, AccessPermissions: UInt32, AccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: win32more.Windows.Win32.Security.ACE_FLAGS) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildExplicitAccessWithNameW(pExplicitAccess: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W), pTrusteeName: win32more.Windows.Win32.Foundation.PWSTR, AccessPermissions: UInt32, AccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: win32more.Windows.Win32.Security.ACE_FLAGS) -> Void: ...
BuildExplicitAccessWithName = UnicodeAlias('BuildExplicitAccessWithNameW')
@winfunctype('ADVAPI32.dll')
def BuildImpersonateExplicitAccessWithNameA(pExplicitAccess: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_A), pTrusteeName: win32more.Windows.Win32.Foundation.PSTR, pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), AccessPermissions: UInt32, AccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: UInt32) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateExplicitAccessWithNameW(pExplicitAccess: POINTER(win32more.Windows.Win32.Security.Authorization.EXPLICIT_ACCESS_W), pTrusteeName: win32more.Windows.Win32.Foundation.PWSTR, pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), AccessPermissions: UInt32, AccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE, Inheritance: UInt32) -> Void: ...
BuildImpersonateExplicitAccessWithName = UnicodeAlias('BuildImpersonateExplicitAccessWithNameW')
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithNameA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pName: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithNameW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pName: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
BuildTrusteeWithName = UnicodeAlias('BuildTrusteeWithNameW')
@winfunctype('ADVAPI32.dll')
def BuildImpersonateTrusteeA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pImpersonateTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildImpersonateTrusteeW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pImpersonateTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> Void: ...
BuildImpersonateTrustee = UnicodeAlias('BuildImpersonateTrusteeW')
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithSidA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pSid: win32more.Windows.Win32.Security.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithSidW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pSid: win32more.Windows.Win32.Security.PSID) -> Void: ...
BuildTrusteeWithSid = UnicodeAlias('BuildTrusteeWithSidW')
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndSidA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pObjSid: POINTER(win32more.Windows.Win32.Security.Authorization.OBJECTS_AND_SID), pObjectGuid: POINTER(Guid), pInheritedObjectGuid: POINTER(Guid), pSid: win32more.Windows.Win32.Security.PSID) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndSidW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pObjSid: POINTER(win32more.Windows.Win32.Security.Authorization.OBJECTS_AND_SID), pObjectGuid: POINTER(Guid), pInheritedObjectGuid: POINTER(Guid), pSid: win32more.Windows.Win32.Security.PSID) -> Void: ...
BuildTrusteeWithObjectsAndSid = UnicodeAlias('BuildTrusteeWithObjectsAndSidW')
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndNameA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A), pObjName: POINTER(win32more.Windows.Win32.Security.Authorization.OBJECTS_AND_NAME_A), ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, InheritedObjectTypeName: win32more.Windows.Win32.Foundation.PSTR, Name: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('ADVAPI32.dll')
def BuildTrusteeWithObjectsAndNameW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W), pObjName: POINTER(win32more.Windows.Win32.Security.Authorization.OBJECTS_AND_NAME_W), ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE, ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, InheritedObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR, Name: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
BuildTrusteeWithObjectsAndName = UnicodeAlias('BuildTrusteeWithObjectsAndNameW')
@winfunctype('ADVAPI32.dll')
def GetTrusteeNameA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeNameW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> win32more.Windows.Win32.Foundation.PWSTR: ...
GetTrusteeName = UnicodeAlias('GetTrusteeNameW')
@winfunctype('ADVAPI32.dll')
def GetTrusteeTypeA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeTypeW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE: ...
GetTrusteeType = UnicodeAlias('GetTrusteeTypeW')
@winfunctype('ADVAPI32.dll')
def GetTrusteeFormA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM: ...
@winfunctype('ADVAPI32.dll')
def GetTrusteeFormW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM: ...
GetTrusteeForm = UnicodeAlias('GetTrusteeFormW')
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeOperationA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION: ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeOperationW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION: ...
GetMultipleTrusteeOperation = UnicodeAlias('GetMultipleTrusteeOperationW')
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeA(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)) -> POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A): ...
@winfunctype('ADVAPI32.dll')
def GetMultipleTrusteeW(pTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)) -> POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W): ...
GetMultipleTrustee = UnicodeAlias('GetMultipleTrusteeW')
@winfunctype('ADVAPI32.dll')
def ConvertSidToStringSidA(Sid: win32more.Windows.Win32.Security.PSID, StringSid: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertSidToStringSidW(Sid: win32more.Windows.Win32.Security.PSID, StringSid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ConvertSidToStringSid = UnicodeAlias('ConvertSidToStringSidW')
@winfunctype('ADVAPI32.dll')
def ConvertStringSidToSidA(StringSid: win32more.Windows.Win32.Foundation.PSTR, Sid: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSidToSidW(StringSid: win32more.Windows.Win32.Foundation.PWSTR, Sid: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ConvertStringSidToSid = UnicodeAlias('ConvertStringSidToSidW')
@winfunctype('ADVAPI32.dll')
def ConvertStringSecurityDescriptorToSecurityDescriptorA(StringSecurityDescriptor: win32more.Windows.Win32.Foundation.PSTR, StringSDRevision: UInt32, SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertStringSecurityDescriptorToSecurityDescriptorW(StringSecurityDescriptor: win32more.Windows.Win32.Foundation.PWSTR, StringSDRevision: UInt32, SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), SecurityDescriptorSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ConvertStringSecurityDescriptorToSecurityDescriptor = UnicodeAlias('ConvertStringSecurityDescriptorToSecurityDescriptorW')
@winfunctype('ADVAPI32.dll')
def ConvertSecurityDescriptorToStringSecurityDescriptorA(SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, RequestedStringSDRevision: UInt32, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, StringSecurityDescriptor: POINTER(win32more.Windows.Win32.Foundation.PSTR), StringSecurityDescriptorLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def ConvertSecurityDescriptorToStringSecurityDescriptorW(SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, RequestedStringSDRevision: UInt32, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, StringSecurityDescriptor: POINTER(win32more.Windows.Win32.Foundation.PWSTR), StringSecurityDescriptorLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ConvertSecurityDescriptorToStringSecurityDescriptor = UnicodeAlias('ConvertSecurityDescriptorToStringSecurityDescriptorW')
AzAuthorizationStore = Guid('{b2bcff59-a757-4b0b-a1bc-ea69981da69e}')
AzBizRuleContext = Guid('{5c2dc96f-8d51-434b-b33c-379bccae77c3}')
AzPrincipalLocator = Guid('{483afb5d-70df-4e16-abdc-a1de4d015a3e}')
class EXPLICIT_ACCESS_A(Structure):
    grfAccessPermissions: UInt32
    grfAccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE
    grfInheritance: win32more.Windows.Win32.Security.ACE_FLAGS
    Trustee: win32more.Windows.Win32.Security.Authorization.TRUSTEE_A
class EXPLICIT_ACCESS_W(Structure):
    grfAccessPermissions: UInt32
    grfAccessMode: win32more.Windows.Win32.Security.Authorization.ACCESS_MODE
    grfInheritance: win32more.Windows.Win32.Security.ACE_FLAGS
    Trustee: win32more.Windows.Win32.Security.Authorization.TRUSTEE_W
EXPLICIT_ACCESS = UnicodeAlias('EXPLICIT_ACCESS_W')
class FN_OBJECT_MGR_FUNCTS(Structure):
    Placeholder: UInt32
@winfunctype_pointer
def FN_PROGRESS(pObjectName: win32more.Windows.Win32.Foundation.PWSTR, Status: UInt32, pInvokeSetting: POINTER(win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING), Args: VoidPtr, SecuritySet: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class IAzApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{987bc7c7-b813-4d27-bede-6ba5ae867e95}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AuthzInterfaceClsid(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AuthzInterfaceClsid(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Version(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Version(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GenerateAudits(self, pbProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GenerateAudits(self, bProp: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ApplyStoreSacl(self, pbProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ApplyStoreSacl(self, bProp: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PolicyReaders(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddPolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeletePolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Scopes(self, ppScopeCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScopes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def OpenScope(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppScope: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScope)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateScope(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppScope: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScope)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def DeleteScope(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Operations(self, ppOperationCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzOperations)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def OpenOperation(self, bstrOperationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppOperation: POINTER(win32more.Windows.Win32.Security.Authorization.IAzOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def CreateOperation(self, bstrOperationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppOperation: POINTER(win32more.Windows.Win32.Security.Authorization.IAzOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def DeleteOperation(self, bstrOperationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Tasks(self, ppTaskCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTasks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def OpenTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTask)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CreateTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTask)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DeleteTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def OpenApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def CreateApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def DeleteApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_Roles(self, ppRoleCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def OpenRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRole)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def CreateRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRole)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def DeleteRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def InitializeClientContextFromToken(self, ullTokenHandle: UInt64, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.IAzClientContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def AddPropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def InitializeClientContextFromName(self, ClientName: win32more.Windows.Win32.Foundation.BSTR, DomainName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.IAzClientContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_DelegatedPolicyUsers(self, pvarDelegatedPolicyUsers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def InitializeClientContextFromStringSid(self, SidString: win32more.Windows.Win32.Foundation.BSTR, lOptions: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.IAzClientContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_PolicyReadersName(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def AddPolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def DeletePolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def AddPolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def DeletePolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_DelegatedPolicyUsersName(self, pvarDelegatedPolicyUsers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplication2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzApplication
    _iid_ = Guid('{086a68af-a249-437c-b18d-d4d86d6a9660}')
    @commethod(68)
    def InitializeClientContextFromToken2(self, ulTokenHandleLowPart: UInt32, ulTokenHandleHighPart: UInt32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.IAzClientContext2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def InitializeClientContext2(self, IdentifyingString: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppClientContext: POINTER(win32more.Windows.Win32.Security.Authorization.IAzClientContext2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplication3(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzApplication2
    _iid_ = Guid('{181c845e-7196-4a7d-ac2e-020c0bb7a303}')
    @commethod(70)
    def ScopeExists(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, pbExist: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def OpenScope2(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, ppScope2: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScope2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def CreateScope2(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, ppScope2: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScope2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def DeleteScope2(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinitions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def CreateRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def OpenRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def DeleteRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_RoleAssignments(self, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def CreateRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def OpenRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def DeleteRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_BizRulesEnabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_BizRulesEnabled(self, bEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f1b744cd-58a6-4e06-9fbf-36f6d779e21e}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(self, plProp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Type(self, lProp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_LdapQuery(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_LdapQuery(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AppMembers(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AppNonMembers(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Members(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_NonMembers(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddAppMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteAppMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddAppNonMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteAppNonMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddNonMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DeleteNonMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def AddPropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def AddMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def DeleteMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddNonMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeleteNonMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_MembersName(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_NonMembersName(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroup2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup
    _iid_ = Guid('{3f0613fc-b71a-464e-a11d-5b881a56cefa}')
    @commethod(39)
    def get_BizRule(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_BizRule(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_BizRuleLanguage(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_BizRuleLanguage(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_BizRuleImportedPath(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_BizRuleImportedPath(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RoleAssignments(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, bRecursive: win32more.Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplicationGroups(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4ce66ad5-9f3c-469d-a911-b99887a7e685}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzApplications(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{929b11a9-95c5-4a84-a29a-20ad42c2f16c}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{edbd9ca9-9b82-4f6a-9e8b-98301e450f14}')
    @commethod(7)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DomainTimeout(self, plProp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_DomainTimeout(self, lProp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ScriptEngineTimeout(self, plProp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ScriptEngineTimeout(self, lProp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MaxScriptEngines(self, plProp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MaxScriptEngines(self, lProp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GenerateAudits(self, pbProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GenerateAudits(self, bProp: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddPropertyItem(self, lPropId: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PolicyReaders(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddPolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeletePolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Initialize(self, lFlags: win32more.Windows.Win32.Security.Authorization.AZ_PROP_CONSTANTS, bstrPolicyURL: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def UpdateCache(self, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Delete(self, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Applications(self, ppAppCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplications)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def OpenApplication(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CreateApplication(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeleteApplication(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CreateApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def OpenApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DeleteApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_DelegatedPolicyUsers(self, pvarDelegatedPolicyUsers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_TargetMachine(self, pbstrTargetMachine: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ApplyStoreSacl(self, pbApplyStoreSacl: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ApplyStoreSacl(self, bApplyStoreSacl: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_PolicyReadersName(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def AddPolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def DeletePolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def AddPolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def DeletePolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_DelegatedPolicyUsersName(self, pvarDelegatedPolicyUsers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def CloseApplication(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, lFlag: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzAuthorizationStore
    _iid_ = Guid('{b11e5584-d577-4273-b6c5-0973e0f8e80d}')
    @commethod(58)
    def OpenApplication2(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplication2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def CreateApplication2(self, bstrApplicationName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppApplication: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplication2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzAuthorizationStore3(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzAuthorizationStore2
    _iid_ = Guid('{abc08425-0c86-4fa0-9be3-7189956c926e}')
    @commethod(60)
    def IsUpdateNeeded(self, pbIsUpdateNeeded: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def BizruleGroupSupported(self, pbSupported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def UpgradeStoresFunctionalLevel(self, lFunctionalLevel: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def IsFunctionalLevelUpgradeSupported(self, lFunctionalLevel: Int32, pbSupported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetSchemaVersion(self, plMajorVersion: POINTER(Int32), plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e192f17d-d59f-455e-a152-940316cd77b2}')
    @commethod(7)
    def put_BusinessRuleResult(self, bResult: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BusinessRuleString(self, bstrBusinessRuleString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_BusinessRuleString(self, pbstrBusinessRuleString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetParameter(self, bstrParameterName: win32more.Windows.Win32.Foundation.BSTR, pvarParameterValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleInterfaces(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e94128c7-e9da-44cc-b0bd-53036f3aab3d}')
    @commethod(7)
    def AddInterface(self, bstrInterfaceName: win32more.Windows.Win32.Foundation.BSTR, lInterfaceFlag: Int32, varInterface: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddInterfaces(self, varInterfaceNames: win32more.Windows.Win32.System.Variant.VARIANT, varInterfaceFlags: win32more.Windows.Win32.System.Variant.VARIANT, varInterfaces: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInterfaceValue(self, bstrInterfaceName: win32more.Windows.Win32.Foundation.BSTR, lInterfaceFlag: POINTER(Int32), varInterface: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, bstrInterfaceName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Count(self, plCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzBizRuleParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fc17685f-e25d-4dcd-bae1-276ec9533cb5}')
    @commethod(7)
    def AddParameter(self, bstrParameterName: win32more.Windows.Win32.Foundation.BSTR, varParameterValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddParameters(self, varParameterNames: win32more.Windows.Win32.System.Variant.VARIANT, varParameterValues: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParameterValue(self, bstrParameterName: win32more.Windows.Win32.Foundation.BSTR, pvarParameterValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, varParameterName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Count(self, plCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eff1f00b-488a-466d-afd9-a401c5f9eef5}')
    @commethod(7)
    def AccessCheck(self, bstrObjectName: win32more.Windows.Win32.Foundation.BSTR, varScopeNames: win32more.Windows.Win32.System.Variant.VARIANT, varOperations: win32more.Windows.Win32.System.Variant.VARIANT, varParameterNames: win32more.Windows.Win32.System.Variant.VARIANT, varParameterValues: win32more.Windows.Win32.System.Variant.VARIANT, varInterfaceNames: win32more.Windows.Win32.System.Variant.VARIANT, varInterfaceFlags: win32more.Windows.Win32.System.Variant.VARIANT, varInterfaces: win32more.Windows.Win32.System.Variant.VARIANT, pvarResults: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBusinessRuleString(self, pbstrBusinessRuleString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_UserDn(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_UserSamCompat(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_UserDisplay(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UserGuid(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UserCanonical(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_UserUpn(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserDnsSamCompat(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRoles(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, pvarRoleNames: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_RoleForAccessCheck(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_RoleForAccessCheck(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzClientContext
    _iid_ = Guid('{2b0c92b8-208a-488a-8f81-e4edb22111cd}')
    @commethod(20)
    def GetAssignedScopesPage(self, lOptions: Int32, PageSize: Int32, pvarCursor: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarScopeNames: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddRoles(self, varRoles: win32more.Windows.Win32.System.Variant.VARIANT, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddApplicationGroups(self, varApplicationGroups: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddStringSids(self, varStringSids: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_LDAPQueryDN(self, bstrLDAPQueryDN: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_LDAPQueryDN(self, pbstrLDAPQueryDN: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzClientContext3(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzClientContext2
    _iid_ = Guid('{11894fde-1deb-4b4b-8907-6d1cda1f5d4f}')
    @commethod(26)
    def AccessCheck2(self, bstrObjectName: win32more.Windows.Win32.Foundation.BSTR, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, lOperation: Int32, plResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def IsInRoleAssignment(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, pbIsInRole: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetOperations(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, ppOperationCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzOperations)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetTasks(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, ppTaskCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTasks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_BizRuleParameters(self, ppBizRuleParam: POINTER(win32more.Windows.Win32.Security.Authorization.IAzBizRuleParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_BizRuleInterfaces(self, ppBizRuleInterfaces: POINTER(win32more.Windows.Win32.Security.Authorization.IAzBizRuleInterfaces)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetGroups(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, ulOptions: UInt32, pGroupArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Sids(self, pStringSidArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzNameResolver(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{504d0f15-73e2-43df-a870-a64f40714f53}')
    @commethod(7)
    def NameFromSid(self, bstrSid: win32more.Windows.Win32.Foundation.BSTR, pSidType: POINTER(Int32), pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NamesFromSids(self, vSids: win32more.Windows.Win32.System.Variant.VARIANT, pvSidTypes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvNames: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzObjectPicker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{63130a48-699a-42d8-bf01-c62ac3fb79f9}')
    @commethod(7)
    def GetPrincipals(self, hParentWnd: win32more.Windows.Win32.Foundation.HWND, bstrTitle: win32more.Windows.Win32.Foundation.BSTR, pvSidTypes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvNames: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvSids: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5e56b24f-ea01-4d61-be44-c49b5e4eaf74}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OperationID(self, plProp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OperationID(self, lProp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzOperation2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzOperation
    _iid_ = Guid('{1f5ea01f-44a2-4184-9c48-a75b4dcc8ccc}')
    @commethod(19)
    def RoleAssignments(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, bRecursive: win32more.Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzOperations(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{90ef9c07-9706-49d9-af80-0438a5f3ec35}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzPrincipalLocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e5c3507d-ad6a-4992-9c7f-74ab480b44cc}')
    @commethod(7)
    def get_NameResolver(self, ppNameResolver: POINTER(win32more.Windows.Win32.Security.Authorization.IAzNameResolver)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ObjectPicker(self, ppObjectPicker: POINTER(win32more.Windows.Win32.Security.Authorization.IAzObjectPicker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRole(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{859e0d8d-62d7-41d8-a034-c0cd5d43fdfa}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddAppMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteAppMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddTask(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteTask(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddOperation(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteOperation(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteMember(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_AppMembers(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Members(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Operations(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Tasks(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddPropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def AddMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def DeleteMemberName(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_MembersName(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRoleAssignment(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzRole
    _iid_ = Guid('{55647d31-0d5a-4fa3-b4ac-2b5f9ad5ab76}')
    @commethod(34)
    def AddRoleDefinition(self, bstrRoleDefinition: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteRoleDefinition(self, bstrRoleDefinition: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinitions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_Scope(self, ppScope: POINTER(win32more.Windows.Win32.Security.Authorization.IAzScope)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRoleAssignments(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9c80b900-fceb-4d73-a0f4-c83b0bbf2481}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRoleDefinition(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzTask
    _iid_ = Guid('{d97fcea1-2599-44f1-9fc3-58e9fbe09466}')
    @commethod(33)
    def RoleAssignments(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, bRecursive: win32more.Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddRoleDefinition(self, bstrRoleDefinition: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteRoleDefinition(self, bstrRoleDefinition: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinitions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRoleDefinitions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{881f25a5-d755-4550-957a-d503a3b34001}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzRoles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{95e0f119-13b4-4dae-b65f-2f7d60d822e4}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzScope(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{00e52487-e08d-4514-b62e-877d5645f5ab}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AddPropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PolicyAdministrators(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_PolicyReaders(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AddPolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeletePolicyAdministrator(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AddPolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeletePolicyReader(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_ApplicationGroups(self, ppGroupCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroups)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OpenApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppGroup: POINTER(win32more.Windows.Win32.Security.Authorization.IAzApplicationGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeleteApplicationGroup(self, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Roles(self, ppRoleCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OpenRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRole)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppRole: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRole)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeleteRole(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Tasks(self, ppTaskCollection: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTasks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def OpenTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTask)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, ppTask: POINTER(win32more.Windows.Win32.Security.Authorization.IAzTask)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DeleteTask(self, bstrTaskName: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_CanBeDelegated(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_BizrulesWritable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_PolicyAdministratorsName(self, pvarAdmins: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_PolicyReadersName(self, pvarReaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def AddPolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def DeletePolicyAdministratorName(self, bstrAdmin: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddPolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeletePolicyReaderName(self, bstrReader: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzScope2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzScope
    _iid_ = Guid('{ee9fe8c9-c9f3-40e2-aa12-d1d8599727fd}')
    @commethod(45)
    def get_RoleDefinitions(self, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinitions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CreateRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def OpenRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR, ppRoleDefinitions: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleDefinition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def DeleteRoleDefinition(self, bstrRoleDefinitionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_RoleAssignments(self, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def CreateRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def OpenRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR, ppRoleAssignment: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def DeleteRoleAssignment(self, bstrRoleAssignmentName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzScopes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{78e14853-9f5e-406d-9b91-6bdba6973510}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzTask(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cb94e592-2e0e-4a6c-a336-b89a6dc1e388}')
    @commethod(7)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, bstrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationData(self, pbstrApplicationData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationData(self, bstrApplicationData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_BizRule(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_BizRule(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BizRuleLanguage(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_BizRuleLanguage(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BizRuleImportedPath(self, pbstrProp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BizRuleImportedPath(self, bstrProp: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_IsRoleDefinition(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_IsRoleDefinition(self, fProp: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Operations(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Tasks(self, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddOperation(self, bstrOp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteOperation(self, bstrOp: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddTask(self, bstrTask: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DeleteTask(self, bstrTask: win32more.Windows.Win32.Foundation.BSTR, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Writable(self, pfProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetProperty(self, lPropId: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT, pvarProp: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetProperty(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def AddPropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def DeletePropertyItem(self, lPropId: Int32, varProp: win32more.Windows.Win32.System.Variant.VARIANT, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Submit(self, lFlags: Int32, varReserved: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzTask2(ComPtr):
    extends: win32more.Windows.Win32.Security.Authorization.IAzTask
    _iid_ = Guid('{03a9a5ee-48c8-4832-9025-aad503c46526}')
    @commethod(33)
    def RoleAssignments(self, bstrScopeName: win32more.Windows.Win32.Foundation.BSTR, bRecursive: win32more.Windows.Win32.Foundation.VARIANT_BOOL, ppRoleAssignments: POINTER(win32more.Windows.Win32.Security.Authorization.IAzRoleAssignments)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAzTasks(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b338ccab-4c85-4388-8c0a-c58592bad398}')
    @commethod(7)
    def get_Item(self, Index: Int32, pvarObtPtr: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnumPtr: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INHERITED_FROMA(Structure):
    GenerationGap: Int32
    AncestorName: win32more.Windows.Win32.Foundation.PSTR
class INHERITED_FROMW(Structure):
    GenerationGap: Int32
    AncestorName: win32more.Windows.Win32.Foundation.PWSTR
INHERITED_FROM = UnicodeAlias('INHERITED_FROMW')
MULTIPLE_TRUSTEE_OPERATION = Int32
NO_MULTIPLE_TRUSTEE: win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION = 0
TRUSTEE_IS_IMPERSONATE: win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION = 1
class OBJECTS_AND_NAME_A(Structure):
    ObjectsPresent: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE
    ObjectTypeName: win32more.Windows.Win32.Foundation.PSTR
    InheritedObjectTypeName: win32more.Windows.Win32.Foundation.PSTR
    ptstrName: win32more.Windows.Win32.Foundation.PSTR
class OBJECTS_AND_NAME_W(Structure):
    ObjectsPresent: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectType: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE
    ObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR
    InheritedObjectTypeName: win32more.Windows.Win32.Foundation.PWSTR
    ptstrName: win32more.Windows.Win32.Foundation.PWSTR
OBJECTS_AND_NAME = UnicodeAlias('OBJECTS_AND_NAME_W')
class OBJECTS_AND_SID(Structure):
    ObjectsPresent: win32more.Windows.Win32.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS
    ObjectTypeGuid: Guid
    InheritedObjectTypeGuid: Guid
    pSid: POINTER(win32more.Windows.Win32.Security.SID)
@winfunctype_pointer
def PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, Args: VoidPtr, pSidAttrArray: POINTER(POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)), pSidCount: POINTER(UInt32), pRestrictedSidAttrArray: POINTER(POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)), pRestrictedSidCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_AUTHZ_DYNAMIC_ACCESS_CHECK(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, pAce: POINTER(win32more.Windows.Win32.Security.ACE_HEADER), pArgs: VoidPtr, pbAceApplicable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY(pCentralAccessPolicy: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFN_AUTHZ_FREE_DYNAMIC_GROUPS(pSidAttrArray: POINTER(win32more.Windows.Win32.Security.SID_AND_ATTRIBUTES)) -> Void: ...
@winfunctype_pointer
def PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY(hAuthzClientContext: win32more.Windows.Win32.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, capid: win32more.Windows.Win32.Security.PSID, pArgs: VoidPtr, pCentralAccessPolicyApplicable: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppCentralAccessPolicy: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PROG_INVOKE_SETTING = Int32
ProgressInvokeNever: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 1
ProgressInvokeEveryObject: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 2
ProgressInvokeOnError: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 3
ProgressCancelOperation: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 4
ProgressRetryOperation: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 5
ProgressInvokePrePostError: win32more.Windows.Win32.Security.Authorization.PROG_INVOKE_SETTING = 6
SE_OBJECT_TYPE = Int32
SE_UNKNOWN_OBJECT_TYPE: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 0
SE_FILE_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 1
SE_SERVICE: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 2
SE_PRINTER: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 3
SE_REGISTRY_KEY: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 4
SE_LMSHARE: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 5
SE_KERNEL_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 6
SE_WINDOW_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 7
SE_DS_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 8
SE_DS_OBJECT_ALL: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 9
SE_PROVIDER_DEFINED_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 10
SE_WMIGUID_OBJECT: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 11
SE_REGISTRY_WOW64_32KEY: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 12
SE_REGISTRY_WOW64_64KEY: win32more.Windows.Win32.Security.Authorization.SE_OBJECT_TYPE = 13
TREE_SEC_INFO = UInt32
TREE_SEC_INFO_SET: win32more.Windows.Win32.Security.Authorization.TREE_SEC_INFO = 1
TREE_SEC_INFO_RESET: win32more.Windows.Win32.Security.Authorization.TREE_SEC_INFO = 2
TREE_SEC_INFO_RESET_KEEP_EXPLICIT: win32more.Windows.Win32.Security.Authorization.TREE_SEC_INFO = 3
class TRUSTEE_A(Structure):
    pMultipleTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_A)
    MultipleTrusteeOperation: win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION
    TrusteeForm: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM
    TrusteeType: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE
    ptstrName: win32more.Windows.Win32.Foundation.PSTR
class TRUSTEE_ACCESSA(Structure):
    lpProperty: win32more.Windows.Win32.Foundation.PSTR
    Access: UInt32
    fAccessFlags: UInt32
    fReturnedAccess: UInt32
class TRUSTEE_ACCESSW(Structure):
    lpProperty: win32more.Windows.Win32.Foundation.PWSTR
    Access: UInt32
    fAccessFlags: UInt32
    fReturnedAccess: UInt32
TRUSTEE_ACCESS = UnicodeAlias('TRUSTEE_ACCESSW')
TRUSTEE_FORM = Int32
TRUSTEE_IS_SID: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM = 0
TRUSTEE_IS_NAME: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM = 1
TRUSTEE_BAD_FORM: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM = 2
TRUSTEE_IS_OBJECTS_AND_SID: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM = 3
TRUSTEE_IS_OBJECTS_AND_NAME: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM = 4
TRUSTEE_TYPE = Int32
TRUSTEE_IS_UNKNOWN: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 0
TRUSTEE_IS_USER: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 1
TRUSTEE_IS_GROUP: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 2
TRUSTEE_IS_DOMAIN: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 3
TRUSTEE_IS_ALIAS: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 4
TRUSTEE_IS_WELL_KNOWN_GROUP: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 5
TRUSTEE_IS_DELETED: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 6
TRUSTEE_IS_INVALID: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 7
TRUSTEE_IS_COMPUTER: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE = 8
class TRUSTEE_W(Structure):
    pMultipleTrustee: POINTER(win32more.Windows.Win32.Security.Authorization.TRUSTEE_W)
    MultipleTrusteeOperation: win32more.Windows.Win32.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION
    TrusteeForm: win32more.Windows.Win32.Security.Authorization.TRUSTEE_FORM
    TrusteeType: win32more.Windows.Win32.Security.Authorization.TRUSTEE_TYPE
    ptstrName: win32more.Windows.Win32.Foundation.PWSTR
TRUSTEE = UnicodeAlias('TRUSTEE_W')


make_ready(__name__)
