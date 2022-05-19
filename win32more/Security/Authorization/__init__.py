from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization
import win32more.System.Com
import win32more.System.Threading

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
SDDL_REVISION_1 = 1
SDDL_REVISION = 1
SDDL_ALIAS_SIZE = 2
INHERITED_ACCESS_ENTRY = 16
INHERITED_PARENT = 268435456
INHERITED_GRANDPARENT = 536870912
TRUSTEE_ACCESS_ALLOWED = 1
TRUSTEE_ACCESS_READ = 2
TRUSTEE_ACCESS_WRITE = 4
TRUSTEE_ACCESS_EXPLICIT = 1
TRUSTEE_ACCESS_ALL = -1
ACTRL_RESERVED = 0
ACTRL_PERM_1 = 1
ACTRL_PERM_2 = 2
ACTRL_PERM_3 = 4
ACTRL_PERM_4 = 8
ACTRL_PERM_5 = 16
ACTRL_PERM_6 = 32
ACTRL_PERM_7 = 64
ACTRL_PERM_8 = 128
ACTRL_PERM_9 = 256
ACTRL_PERM_10 = 512
ACTRL_PERM_11 = 1024
ACTRL_PERM_12 = 2048
ACTRL_PERM_13 = 4096
ACTRL_PERM_14 = 8192
ACTRL_PERM_15 = 16384
ACTRL_PERM_16 = 32768
ACTRL_PERM_17 = 65536
ACTRL_PERM_18 = 131072
ACTRL_PERM_19 = 262144
ACTRL_PERM_20 = 524288
ACTRL_ACCESS_PROTECTED = 1
ACTRL_SYSTEM_ACCESS = 67108864
ACTRL_DELETE = 134217728
ACTRL_READ_CONTROL = 268435456
ACTRL_CHANGE_ACCESS = 536870912
ACTRL_CHANGE_OWNER = 1073741824
ACTRL_SYNCHRONIZE = 2147483648
ACTRL_STD_RIGHTS_ALL = 4160749568
ACTRL_FILE_READ = 1
ACTRL_FILE_WRITE = 2
ACTRL_FILE_APPEND = 4
ACTRL_FILE_READ_PROP = 8
ACTRL_FILE_WRITE_PROP = 16
ACTRL_FILE_EXECUTE = 32
ACTRL_FILE_READ_ATTRIB = 128
ACTRL_FILE_WRITE_ATTRIB = 256
ACTRL_FILE_CREATE_PIPE = 512
ACTRL_DIR_LIST = 1
ACTRL_DIR_CREATE_OBJECT = 2
ACTRL_DIR_CREATE_CHILD = 4
ACTRL_DIR_DELETE_CHILD = 64
ACTRL_DIR_TRAVERSE = 32
ACTRL_KERNEL_TERMINATE = 1
ACTRL_KERNEL_THREAD = 2
ACTRL_KERNEL_VM = 4
ACTRL_KERNEL_VM_READ = 8
ACTRL_KERNEL_VM_WRITE = 16
ACTRL_KERNEL_DUP_HANDLE = 32
ACTRL_KERNEL_PROCESS = 64
ACTRL_KERNEL_SET_INFO = 128
ACTRL_KERNEL_GET_INFO = 256
ACTRL_KERNEL_CONTROL = 512
ACTRL_KERNEL_ALERT = 1024
ACTRL_KERNEL_GET_CONTEXT = 2048
ACTRL_KERNEL_SET_CONTEXT = 4096
ACTRL_KERNEL_TOKEN = 8192
ACTRL_KERNEL_IMPERSONATE = 16384
ACTRL_KERNEL_DIMPERSONATE = 32768
ACTRL_PRINT_SADMIN = 1
ACTRL_PRINT_SLIST = 2
ACTRL_PRINT_PADMIN = 4
ACTRL_PRINT_PUSE = 8
ACTRL_PRINT_JADMIN = 16
ACTRL_SVC_GET_INFO = 1
ACTRL_SVC_SET_INFO = 2
ACTRL_SVC_STATUS = 4
ACTRL_SVC_LIST = 8
ACTRL_SVC_START = 16
ACTRL_SVC_STOP = 32
ACTRL_SVC_PAUSE = 64
ACTRL_SVC_INTERROGATE = 128
ACTRL_SVC_UCONTROL = 256
ACTRL_REG_QUERY = 1
ACTRL_REG_SET = 2
ACTRL_REG_CREATE_CHILD = 4
ACTRL_REG_LIST = 8
ACTRL_REG_NOTIFY = 16
ACTRL_REG_LINK = 32
ACTRL_WIN_CLIPBRD = 1
ACTRL_WIN_GLOBAL_ATOMS = 2
ACTRL_WIN_CREATE = 4
ACTRL_WIN_LIST_DESK = 8
ACTRL_WIN_LIST = 16
ACTRL_WIN_READ_ATTRIBS = 32
ACTRL_WIN_WRITE_ATTRIBS = 64
ACTRL_WIN_SCREEN = 128
ACTRL_WIN_EXIT = 256
ACTRL_ACCESS_NO_OPTIONS = 0
ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES = 1
AUDIT_TYPE_LEGACY = 1
AUDIT_TYPE_WMI = 2
AP_ParamTypeBits = 8
AP_ParamTypeMask = 255
_AUTHZ_SS_MAXSIZE = 128
APF_AuditFailure = 0
APF_AuditSuccess = 1
APF_ValidFlags = 1
AUTHZP_WPD_EVENT = 16
AUTHZ_ALLOW_MULTIPLE_SOURCE_INSTANCES = 1
AUTHZ_MIGRATED_LEGACY_PUBLISHER = 2
AUTHZ_AUDIT_INSTANCE_INFORMATION = 2
AUTHZ_SKIP_TOKEN_GROUPS = 2
AUTHZ_REQUIRE_S4U_LOGON = 4
AUTHZ_COMPUTE_PRIVILEGES = 8
AUTHZ_SECURITY_ATTRIBUTE_TYPE_INVALID = 0
AUTHZ_SECURITY_ATTRIBUTE_TYPE_INT64 = 1
AUTHZ_SECURITY_ATTRIBUTE_TYPE_UINT64 = 2
AUTHZ_SECURITY_ATTRIBUTE_TYPE_STRING = 3
AUTHZ_SECURITY_ATTRIBUTE_TYPE_FQBN = 4
AUTHZ_SECURITY_ATTRIBUTE_TYPE_SID = 5
AUTHZ_SECURITY_ATTRIBUTE_TYPE_BOOLEAN = 6
AUTHZ_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING = 16
AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION_V1 = 1
AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION = 1
AUTHZ_RPC_INIT_INFO_CLIENT_VERSION_V1 = 1
AUTHZ_INIT_INFO_VERSION_V1 = 1
AUTHZ_WPD_CATEGORY_FLAG = 16
AUTHZ_FLAG_ALLOW_MULTIPLE_SOURCE_INSTANCES = 1
OLESCRIPT_E_SYNTAX = -2147352319
AUTHZ_RESOURCE_MANAGER_FLAGS = UInt32
AUTHZ_RM_FLAG_NO_AUDIT = 1
AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION = 2
AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES = 4
AUTHZ_ACCESS_CHECK_FLAGS = UInt32
AUTHZ_ACCESS_CHECK_NO_DEEP_COPY_SD = 1
AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS = UInt32
AUTHZ_NO_SUCCESS_AUDIT = 1
AUTHZ_NO_FAILURE_AUDIT = 2
AUTHZ_NO_ALLOC_STRINGS = 4
TREE_SEC_INFO = UInt32
TREE_SEC_INFO_SET = 1
TREE_SEC_INFO_RESET = 2
TREE_SEC_INFO_RESET_KEEP_EXPLICIT = 3
AUTHZ_GENERATE_RESULTS = UInt32
AUTHZ_GENERATE_SUCCESS_AUDIT = 1
AUTHZ_GENERATE_FAILURE_AUDIT = 2
ACTRL_ACCESS_ENTRY_ACCESS_FLAGS = UInt32
ACTRL_ACCESS_ALLOWED = 1
ACTRL_ACCESS_DENIED = 2
ACTRL_AUDIT_SUCCESS = 4
ACTRL_AUDIT_FAILURE = 8
AUTHZ_SECURITY_ATTRIBUTE_FLAGS = UInt32
AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE = 1
AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE = 2
SE_OBJECT_TYPE = Int32
SE_UNKNOWN_OBJECT_TYPE = 0
SE_FILE_OBJECT = 1
SE_SERVICE = 2
SE_PRINTER = 3
SE_REGISTRY_KEY = 4
SE_LMSHARE = 5
SE_KERNEL_OBJECT = 6
SE_WINDOW_OBJECT = 7
SE_DS_OBJECT = 8
SE_DS_OBJECT_ALL = 9
SE_PROVIDER_DEFINED_OBJECT = 10
SE_WMIGUID_OBJECT = 11
SE_REGISTRY_WOW64_32KEY = 12
SE_REGISTRY_WOW64_64KEY = 13
TRUSTEE_TYPE = Int32
TRUSTEE_IS_UNKNOWN = 0
TRUSTEE_IS_USER = 1
TRUSTEE_IS_GROUP = 2
TRUSTEE_IS_DOMAIN = 3
TRUSTEE_IS_ALIAS = 4
TRUSTEE_IS_WELL_KNOWN_GROUP = 5
TRUSTEE_IS_DELETED = 6
TRUSTEE_IS_INVALID = 7
TRUSTEE_IS_COMPUTER = 8
TRUSTEE_FORM = Int32
TRUSTEE_IS_SID = 0
TRUSTEE_IS_NAME = 1
TRUSTEE_BAD_FORM = 2
TRUSTEE_IS_OBJECTS_AND_SID = 3
TRUSTEE_IS_OBJECTS_AND_NAME = 4
MULTIPLE_TRUSTEE_OPERATION = Int32
NO_MULTIPLE_TRUSTEE = 0
TRUSTEE_IS_IMPERSONATE = 1
def _define_OBJECTS_AND_SID_head():
    class OBJECTS_AND_SID(Structure):
        pass
    return OBJECTS_AND_SID
def _define_OBJECTS_AND_SID():
    OBJECTS_AND_SID = win32more.Security.Authorization.OBJECTS_AND_SID_head
    OBJECTS_AND_SID._fields_ = [
        ("ObjectsPresent", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectTypeGuid", Guid),
        ("InheritedObjectTypeGuid", Guid),
        ("pSid", POINTER(win32more.Security.SID_head)),
    ]
    return OBJECTS_AND_SID
def _define_OBJECTS_AND_NAME_A_head():
    class OBJECTS_AND_NAME_A(Structure):
        pass
    return OBJECTS_AND_NAME_A
def _define_OBJECTS_AND_NAME_A():
    OBJECTS_AND_NAME_A = win32more.Security.Authorization.OBJECTS_AND_NAME_A_head
    OBJECTS_AND_NAME_A._fields_ = [
        ("ObjectsPresent", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", win32more.Security.Authorization.SE_OBJECT_TYPE),
        ("ObjectTypeName", win32more.Foundation.PSTR),
        ("InheritedObjectTypeName", win32more.Foundation.PSTR),
        ("ptstrName", win32more.Foundation.PSTR),
    ]
    return OBJECTS_AND_NAME_A
def _define_OBJECTS_AND_NAME_W_head():
    class OBJECTS_AND_NAME_W(Structure):
        pass
    return OBJECTS_AND_NAME_W
def _define_OBJECTS_AND_NAME_W():
    OBJECTS_AND_NAME_W = win32more.Security.Authorization.OBJECTS_AND_NAME_W_head
    OBJECTS_AND_NAME_W._fields_ = [
        ("ObjectsPresent", win32more.Security.SYSTEM_AUDIT_OBJECT_ACE_FLAGS),
        ("ObjectType", win32more.Security.Authorization.SE_OBJECT_TYPE),
        ("ObjectTypeName", win32more.Foundation.PWSTR),
        ("InheritedObjectTypeName", win32more.Foundation.PWSTR),
        ("ptstrName", win32more.Foundation.PWSTR),
    ]
    return OBJECTS_AND_NAME_W
def _define_TRUSTEE_A_head():
    class TRUSTEE_A(Structure):
        pass
    return TRUSTEE_A
def _define_TRUSTEE_A():
    TRUSTEE_A = win32more.Security.Authorization.TRUSTEE_A_head
    TRUSTEE_A._fields_ = [
        ("pMultipleTrustee", POINTER(win32more.Security.Authorization.TRUSTEE_A_head)),
        ("MultipleTrusteeOperation", win32more.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION),
        ("TrusteeForm", win32more.Security.Authorization.TRUSTEE_FORM),
        ("TrusteeType", win32more.Security.Authorization.TRUSTEE_TYPE),
        ("ptstrName", win32more.Foundation.PSTR),
    ]
    return TRUSTEE_A
def _define_TRUSTEE_W_head():
    class TRUSTEE_W(Structure):
        pass
    return TRUSTEE_W
def _define_TRUSTEE_W():
    TRUSTEE_W = win32more.Security.Authorization.TRUSTEE_W_head
    TRUSTEE_W._fields_ = [
        ("pMultipleTrustee", POINTER(win32more.Security.Authorization.TRUSTEE_W_head)),
        ("MultipleTrusteeOperation", win32more.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION),
        ("TrusteeForm", win32more.Security.Authorization.TRUSTEE_FORM),
        ("TrusteeType", win32more.Security.Authorization.TRUSTEE_TYPE),
        ("ptstrName", win32more.Foundation.PWSTR),
    ]
    return TRUSTEE_W
ACCESS_MODE = Int32
NOT_USED_ACCESS = 0
GRANT_ACCESS = 1
SET_ACCESS = 2
DENY_ACCESS = 3
REVOKE_ACCESS = 4
SET_AUDIT_SUCCESS = 5
SET_AUDIT_FAILURE = 6
def _define_EXPLICIT_ACCESS_A_head():
    class EXPLICIT_ACCESS_A(Structure):
        pass
    return EXPLICIT_ACCESS_A
def _define_EXPLICIT_ACCESS_A():
    EXPLICIT_ACCESS_A = win32more.Security.Authorization.EXPLICIT_ACCESS_A_head
    EXPLICIT_ACCESS_A._fields_ = [
        ("grfAccessPermissions", UInt32),
        ("grfAccessMode", win32more.Security.Authorization.ACCESS_MODE),
        ("grfInheritance", win32more.Security.ACE_FLAGS),
        ("Trustee", win32more.Security.Authorization.TRUSTEE_A),
    ]
    return EXPLICIT_ACCESS_A
def _define_EXPLICIT_ACCESS_W_head():
    class EXPLICIT_ACCESS_W(Structure):
        pass
    return EXPLICIT_ACCESS_W
def _define_EXPLICIT_ACCESS_W():
    EXPLICIT_ACCESS_W = win32more.Security.Authorization.EXPLICIT_ACCESS_W_head
    EXPLICIT_ACCESS_W._fields_ = [
        ("grfAccessPermissions", UInt32),
        ("grfAccessMode", win32more.Security.Authorization.ACCESS_MODE),
        ("grfInheritance", win32more.Security.ACE_FLAGS),
        ("Trustee", win32more.Security.Authorization.TRUSTEE_W),
    ]
    return EXPLICIT_ACCESS_W
def _define_ACTRL_ACCESS_ENTRYA_head():
    class ACTRL_ACCESS_ENTRYA(Structure):
        pass
    return ACTRL_ACCESS_ENTRYA
def _define_ACTRL_ACCESS_ENTRYA():
    ACTRL_ACCESS_ENTRYA = win32more.Security.Authorization.ACTRL_ACCESS_ENTRYA_head
    ACTRL_ACCESS_ENTRYA._fields_ = [
        ("Trustee", win32more.Security.Authorization.TRUSTEE_A),
        ("fAccessFlags", win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS),
        ("Access", UInt32),
        ("ProvSpecificAccess", UInt32),
        ("Inheritance", win32more.Security.ACE_FLAGS),
        ("lpInheritProperty", win32more.Foundation.PSTR),
    ]
    return ACTRL_ACCESS_ENTRYA
def _define_ACTRL_ACCESS_ENTRYW_head():
    class ACTRL_ACCESS_ENTRYW(Structure):
        pass
    return ACTRL_ACCESS_ENTRYW
def _define_ACTRL_ACCESS_ENTRYW():
    ACTRL_ACCESS_ENTRYW = win32more.Security.Authorization.ACTRL_ACCESS_ENTRYW_head
    ACTRL_ACCESS_ENTRYW._fields_ = [
        ("Trustee", win32more.Security.Authorization.TRUSTEE_W),
        ("fAccessFlags", win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_ACCESS_FLAGS),
        ("Access", UInt32),
        ("ProvSpecificAccess", UInt32),
        ("Inheritance", win32more.Security.ACE_FLAGS),
        ("lpInheritProperty", win32more.Foundation.PWSTR),
    ]
    return ACTRL_ACCESS_ENTRYW
def _define_ACTRL_ACCESS_ENTRY_LISTA_head():
    class ACTRL_ACCESS_ENTRY_LISTA(Structure):
        pass
    return ACTRL_ACCESS_ENTRY_LISTA
def _define_ACTRL_ACCESS_ENTRY_LISTA():
    ACTRL_ACCESS_ENTRY_LISTA = win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTA_head
    ACTRL_ACCESS_ENTRY_LISTA._fields_ = [
        ("cEntries", UInt32),
        ("pAccessList", POINTER(win32more.Security.Authorization.ACTRL_ACCESS_ENTRYA_head)),
    ]
    return ACTRL_ACCESS_ENTRY_LISTA
def _define_ACTRL_ACCESS_ENTRY_LISTW_head():
    class ACTRL_ACCESS_ENTRY_LISTW(Structure):
        pass
    return ACTRL_ACCESS_ENTRY_LISTW
def _define_ACTRL_ACCESS_ENTRY_LISTW():
    ACTRL_ACCESS_ENTRY_LISTW = win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTW_head
    ACTRL_ACCESS_ENTRY_LISTW._fields_ = [
        ("cEntries", UInt32),
        ("pAccessList", POINTER(win32more.Security.Authorization.ACTRL_ACCESS_ENTRYW_head)),
    ]
    return ACTRL_ACCESS_ENTRY_LISTW
def _define_ACTRL_PROPERTY_ENTRYA_head():
    class ACTRL_PROPERTY_ENTRYA(Structure):
        pass
    return ACTRL_PROPERTY_ENTRYA
def _define_ACTRL_PROPERTY_ENTRYA():
    ACTRL_PROPERTY_ENTRYA = win32more.Security.Authorization.ACTRL_PROPERTY_ENTRYA_head
    ACTRL_PROPERTY_ENTRYA._fields_ = [
        ("lpProperty", win32more.Foundation.PSTR),
        ("pAccessEntryList", POINTER(win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTA_head)),
        ("fListFlags", UInt32),
    ]
    return ACTRL_PROPERTY_ENTRYA
def _define_ACTRL_PROPERTY_ENTRYW_head():
    class ACTRL_PROPERTY_ENTRYW(Structure):
        pass
    return ACTRL_PROPERTY_ENTRYW
def _define_ACTRL_PROPERTY_ENTRYW():
    ACTRL_PROPERTY_ENTRYW = win32more.Security.Authorization.ACTRL_PROPERTY_ENTRYW_head
    ACTRL_PROPERTY_ENTRYW._fields_ = [
        ("lpProperty", win32more.Foundation.PWSTR),
        ("pAccessEntryList", POINTER(win32more.Security.Authorization.ACTRL_ACCESS_ENTRY_LISTW_head)),
        ("fListFlags", UInt32),
    ]
    return ACTRL_PROPERTY_ENTRYW
def _define_ACTRL_ACCESSA_head():
    class ACTRL_ACCESSA(Structure):
        pass
    return ACTRL_ACCESSA
def _define_ACTRL_ACCESSA():
    ACTRL_ACCESSA = win32more.Security.Authorization.ACTRL_ACCESSA_head
    ACTRL_ACCESSA._fields_ = [
        ("cEntries", UInt32),
        ("pPropertyAccessList", POINTER(win32more.Security.Authorization.ACTRL_PROPERTY_ENTRYA_head)),
    ]
    return ACTRL_ACCESSA
def _define_ACTRL_ACCESSW_head():
    class ACTRL_ACCESSW(Structure):
        pass
    return ACTRL_ACCESSW
def _define_ACTRL_ACCESSW():
    ACTRL_ACCESSW = win32more.Security.Authorization.ACTRL_ACCESSW_head
    ACTRL_ACCESSW._fields_ = [
        ("cEntries", UInt32),
        ("pPropertyAccessList", POINTER(win32more.Security.Authorization.ACTRL_PROPERTY_ENTRYW_head)),
    ]
    return ACTRL_ACCESSW
def _define_TRUSTEE_ACCESSA_head():
    class TRUSTEE_ACCESSA(Structure):
        pass
    return TRUSTEE_ACCESSA
def _define_TRUSTEE_ACCESSA():
    TRUSTEE_ACCESSA = win32more.Security.Authorization.TRUSTEE_ACCESSA_head
    TRUSTEE_ACCESSA._fields_ = [
        ("lpProperty", win32more.Foundation.PSTR),
        ("Access", UInt32),
        ("fAccessFlags", UInt32),
        ("fReturnedAccess", UInt32),
    ]
    return TRUSTEE_ACCESSA
def _define_TRUSTEE_ACCESSW_head():
    class TRUSTEE_ACCESSW(Structure):
        pass
    return TRUSTEE_ACCESSW
def _define_TRUSTEE_ACCESSW():
    TRUSTEE_ACCESSW = win32more.Security.Authorization.TRUSTEE_ACCESSW_head
    TRUSTEE_ACCESSW._fields_ = [
        ("lpProperty", win32more.Foundation.PWSTR),
        ("Access", UInt32),
        ("fAccessFlags", UInt32),
        ("fReturnedAccess", UInt32),
    ]
    return TRUSTEE_ACCESSW
def _define_ACTRL_OVERLAPPED_head():
    class ACTRL_OVERLAPPED(Structure):
        pass
    return ACTRL_OVERLAPPED
def _define_ACTRL_OVERLAPPED():
    ACTRL_OVERLAPPED = win32more.Security.Authorization.ACTRL_OVERLAPPED_head
    class ACTRL_OVERLAPPED__Anonymous_e__Union(Union):
        pass
    ACTRL_OVERLAPPED__Anonymous_e__Union._fields_ = [
        ("Provider", c_void_p),
        ("Reserved1", UInt32),
    ]
    ACTRL_OVERLAPPED._anonymous_ = [
        'Anonymous',
    ]
    ACTRL_OVERLAPPED._fields_ = [
        ("Anonymous", ACTRL_OVERLAPPED__Anonymous_e__Union),
        ("Reserved2", UInt32),
        ("hEvent", win32more.Foundation.HANDLE),
    ]
    return ACTRL_OVERLAPPED
def _define_ACTRL_ACCESS_INFOA_head():
    class ACTRL_ACCESS_INFOA(Structure):
        pass
    return ACTRL_ACCESS_INFOA
def _define_ACTRL_ACCESS_INFOA():
    ACTRL_ACCESS_INFOA = win32more.Security.Authorization.ACTRL_ACCESS_INFOA_head
    ACTRL_ACCESS_INFOA._fields_ = [
        ("fAccessPermission", UInt32),
        ("lpAccessPermissionName", win32more.Foundation.PSTR),
    ]
    return ACTRL_ACCESS_INFOA
def _define_ACTRL_ACCESS_INFOW_head():
    class ACTRL_ACCESS_INFOW(Structure):
        pass
    return ACTRL_ACCESS_INFOW
def _define_ACTRL_ACCESS_INFOW():
    ACTRL_ACCESS_INFOW = win32more.Security.Authorization.ACTRL_ACCESS_INFOW_head
    ACTRL_ACCESS_INFOW._fields_ = [
        ("fAccessPermission", UInt32),
        ("lpAccessPermissionName", win32more.Foundation.PWSTR),
    ]
    return ACTRL_ACCESS_INFOW
def _define_ACTRL_CONTROL_INFOA_head():
    class ACTRL_CONTROL_INFOA(Structure):
        pass
    return ACTRL_CONTROL_INFOA
def _define_ACTRL_CONTROL_INFOA():
    ACTRL_CONTROL_INFOA = win32more.Security.Authorization.ACTRL_CONTROL_INFOA_head
    ACTRL_CONTROL_INFOA._fields_ = [
        ("lpControlId", win32more.Foundation.PSTR),
        ("lpControlName", win32more.Foundation.PSTR),
    ]
    return ACTRL_CONTROL_INFOA
def _define_ACTRL_CONTROL_INFOW_head():
    class ACTRL_CONTROL_INFOW(Structure):
        pass
    return ACTRL_CONTROL_INFOW
def _define_ACTRL_CONTROL_INFOW():
    ACTRL_CONTROL_INFOW = win32more.Security.Authorization.ACTRL_CONTROL_INFOW_head
    ACTRL_CONTROL_INFOW._fields_ = [
        ("lpControlId", win32more.Foundation.PWSTR),
        ("lpControlName", win32more.Foundation.PWSTR),
    ]
    return ACTRL_CONTROL_INFOW
PROG_INVOKE_SETTING = Int32
PROG_INVOKE_SETTING_ProgressInvokeNever = 1
PROG_INVOKE_SETTING_ProgressInvokeEveryObject = 2
PROG_INVOKE_SETTING_ProgressInvokeOnError = 3
PROG_INVOKE_SETTING_ProgressCancelOperation = 4
PROG_INVOKE_SETTING_ProgressRetryOperation = 5
PROG_INVOKE_SETTING_ProgressInvokePrePostError = 6
def _define_FN_OBJECT_MGR_FUNCTIONS_head():
    class FN_OBJECT_MGR_FUNCTIONS(Structure):
        pass
    return FN_OBJECT_MGR_FUNCTIONS
def _define_FN_OBJECT_MGR_FUNCTIONS():
    FN_OBJECT_MGR_FUNCTIONS = win32more.Security.Authorization.FN_OBJECT_MGR_FUNCTIONS_head
    FN_OBJECT_MGR_FUNCTIONS._fields_ = [
        ("Placeholder", UInt32),
    ]
    return FN_OBJECT_MGR_FUNCTIONS
def _define_INHERITED_FROMA_head():
    class INHERITED_FROMA(Structure):
        pass
    return INHERITED_FROMA
def _define_INHERITED_FROMA():
    INHERITED_FROMA = win32more.Security.Authorization.INHERITED_FROMA_head
    INHERITED_FROMA._fields_ = [
        ("GenerationGap", Int32),
        ("AncestorName", win32more.Foundation.PSTR),
    ]
    return INHERITED_FROMA
def _define_INHERITED_FROMW_head():
    class INHERITED_FROMW(Structure):
        pass
    return INHERITED_FROMW
def _define_INHERITED_FROMW():
    INHERITED_FROMW = win32more.Security.Authorization.INHERITED_FROMW_head
    INHERITED_FROMW._fields_ = [
        ("GenerationGap", Int32),
        ("AncestorName", win32more.Foundation.PWSTR),
    ]
    return INHERITED_FROMW
AUDIT_PARAM_TYPE = Int32
APT_None = 1
APT_String = 2
APT_Ulong = 3
APT_Pointer = 4
APT_Sid = 5
APT_LogonId = 6
APT_ObjectTypeList = 7
APT_Luid = 8
APT_Guid = 9
APT_Time = 10
APT_Int64 = 11
APT_IpAddress = 12
APT_LogonIdWithSid = 13
def _define_AUDIT_OBJECT_TYPE_head():
    class AUDIT_OBJECT_TYPE(Structure):
        pass
    return AUDIT_OBJECT_TYPE
def _define_AUDIT_OBJECT_TYPE():
    AUDIT_OBJECT_TYPE = win32more.Security.Authorization.AUDIT_OBJECT_TYPE_head
    AUDIT_OBJECT_TYPE._fields_ = [
        ("ObjectType", Guid),
        ("Flags", UInt16),
        ("Level", UInt16),
        ("AccessMask", UInt32),
    ]
    return AUDIT_OBJECT_TYPE
def _define_AUDIT_OBJECT_TYPES_head():
    class AUDIT_OBJECT_TYPES(Structure):
        pass
    return AUDIT_OBJECT_TYPES
def _define_AUDIT_OBJECT_TYPES():
    AUDIT_OBJECT_TYPES = win32more.Security.Authorization.AUDIT_OBJECT_TYPES_head
    AUDIT_OBJECT_TYPES._fields_ = [
        ("Count", UInt16),
        ("Flags", UInt16),
        ("pObjectTypes", POINTER(win32more.Security.Authorization.AUDIT_OBJECT_TYPE_head)),
    ]
    return AUDIT_OBJECT_TYPES
def _define_AUDIT_IP_ADDRESS_head():
    class AUDIT_IP_ADDRESS(Structure):
        pass
    return AUDIT_IP_ADDRESS
def _define_AUDIT_IP_ADDRESS():
    AUDIT_IP_ADDRESS = win32more.Security.Authorization.AUDIT_IP_ADDRESS_head
    AUDIT_IP_ADDRESS._fields_ = [
        ("pIpAddress", Byte * 128),
    ]
    return AUDIT_IP_ADDRESS
def _define_AUDIT_PARAM_head():
    class AUDIT_PARAM(Structure):
        pass
    return AUDIT_PARAM
def _define_AUDIT_PARAM():
    AUDIT_PARAM = win32more.Security.Authorization.AUDIT_PARAM_head
    class AUDIT_PARAM__Anonymous1_e__Union(Union):
        pass
    AUDIT_PARAM__Anonymous1_e__Union._fields_ = [
        ("Data0", UIntPtr),
        ("String", win32more.Foundation.PWSTR),
        ("u", UIntPtr),
        ("psid", POINTER(win32more.Security.SID_head)),
        ("pguid", POINTER(Guid)),
        ("LogonId_LowPart", UInt32),
        ("pObjectTypes", POINTER(win32more.Security.Authorization.AUDIT_OBJECT_TYPES_head)),
        ("pIpAddress", POINTER(win32more.Security.Authorization.AUDIT_IP_ADDRESS_head)),
    ]
    class AUDIT_PARAM__Anonymous2_e__Union(Union):
        pass
    AUDIT_PARAM__Anonymous2_e__Union._fields_ = [
        ("Data1", UIntPtr),
        ("LogonId_HighPart", Int32),
    ]
    AUDIT_PARAM._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    AUDIT_PARAM._fields_ = [
        ("Type", win32more.Security.Authorization.AUDIT_PARAM_TYPE),
        ("Length", UInt32),
        ("Flags", UInt32),
        ("Anonymous1", AUDIT_PARAM__Anonymous1_e__Union),
        ("Anonymous2", AUDIT_PARAM__Anonymous2_e__Union),
    ]
    return AUDIT_PARAM
def _define_AUDIT_PARAMS_head():
    class AUDIT_PARAMS(Structure):
        pass
    return AUDIT_PARAMS
def _define_AUDIT_PARAMS():
    AUDIT_PARAMS = win32more.Security.Authorization.AUDIT_PARAMS_head
    AUDIT_PARAMS._fields_ = [
        ("Length", UInt32),
        ("Flags", UInt32),
        ("Count", UInt16),
        ("Parameters", POINTER(win32more.Security.Authorization.AUDIT_PARAM_head)),
    ]
    return AUDIT_PARAMS
def _define_AUTHZ_AUDIT_EVENT_TYPE_LEGACY_head():
    class AUTHZ_AUDIT_EVENT_TYPE_LEGACY(Structure):
        pass
    return AUTHZ_AUDIT_EVENT_TYPE_LEGACY
def _define_AUTHZ_AUDIT_EVENT_TYPE_LEGACY():
    AUTHZ_AUDIT_EVENT_TYPE_LEGACY = win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_LEGACY_head
    AUTHZ_AUDIT_EVENT_TYPE_LEGACY._fields_ = [
        ("CategoryId", UInt16),
        ("AuditId", UInt16),
        ("ParameterCount", UInt16),
    ]
    return AUTHZ_AUDIT_EVENT_TYPE_LEGACY
def _define_AUTHZ_AUDIT_EVENT_TYPE_UNION_head():
    class AUTHZ_AUDIT_EVENT_TYPE_UNION(Union):
        pass
    return AUTHZ_AUDIT_EVENT_TYPE_UNION
def _define_AUTHZ_AUDIT_EVENT_TYPE_UNION():
    AUTHZ_AUDIT_EVENT_TYPE_UNION = win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_UNION_head
    AUTHZ_AUDIT_EVENT_TYPE_UNION._fields_ = [
        ("Legacy", win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_LEGACY),
    ]
    return AUTHZ_AUDIT_EVENT_TYPE_UNION
def _define_AUTHZ_AUDIT_EVENT_TYPE_OLD_head():
    class AUTHZ_AUDIT_EVENT_TYPE_OLD(Structure):
        pass
    return AUTHZ_AUDIT_EVENT_TYPE_OLD
def _define_AUTHZ_AUDIT_EVENT_TYPE_OLD():
    AUTHZ_AUDIT_EVENT_TYPE_OLD = win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_OLD_head
    AUTHZ_AUDIT_EVENT_TYPE_OLD._fields_ = [
        ("Version", UInt32),
        ("dwFlags", UInt32),
        ("RefCount", Int32),
        ("hAudit", UIntPtr),
        ("LinkId", win32more.Foundation.LUID),
        ("u", win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_UNION),
    ]
    return AUTHZ_AUDIT_EVENT_TYPE_OLD
def _define_AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE___head():
    class AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__(Structure):
        pass
    return AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__
def _define_AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__():
    AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__ = win32more.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE___head
    AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__._fields_ = [
        ("unused", Int32),
    ]
    return AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__
def _define_AUTHZ_ACCESS_REQUEST_head():
    class AUTHZ_ACCESS_REQUEST(Structure):
        pass
    return AUTHZ_ACCESS_REQUEST
def _define_AUTHZ_ACCESS_REQUEST():
    AUTHZ_ACCESS_REQUEST = win32more.Security.Authorization.AUTHZ_ACCESS_REQUEST_head
    AUTHZ_ACCESS_REQUEST._fields_ = [
        ("DesiredAccess", UInt32),
        ("PrincipalSelfSid", win32more.Foundation.PSID),
        ("ObjectTypeList", POINTER(win32more.Security.OBJECT_TYPE_LIST_head)),
        ("ObjectTypeListLength", UInt32),
        ("OptionalArguments", c_void_p),
    ]
    return AUTHZ_ACCESS_REQUEST
def _define_AUTHZ_ACCESS_REPLY_head():
    class AUTHZ_ACCESS_REPLY(Structure):
        pass
    return AUTHZ_ACCESS_REPLY
def _define_AUTHZ_ACCESS_REPLY():
    AUTHZ_ACCESS_REPLY = win32more.Security.Authorization.AUTHZ_ACCESS_REPLY_head
    AUTHZ_ACCESS_REPLY._fields_ = [
        ("ResultListLength", UInt32),
        ("GrantedAccessMask", POINTER(UInt32)),
        ("SaclEvaluationResults", POINTER(win32more.Security.Authorization.AUTHZ_GENERATE_RESULTS)),
        ("Error", POINTER(UInt32)),
    ]
    return AUTHZ_ACCESS_REPLY
def _define_PFN_AUTHZ_DYNAMIC_ACCESS_CHECK():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.ACE_HEADER_head),c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)
def _define_PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,c_void_p,POINTER(POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),POINTER(UInt32),POINTER(POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),POINTER(UInt32), use_last_error=False)
def _define_PFN_AUTHZ_FREE_DYNAMIC_GROUPS():
    return CFUNCTYPE(Void,POINTER(win32more.Security.SID_AND_ATTRIBUTES_head), use_last_error=False)
def _define_PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Foundation.PSID,c_void_p,POINTER(win32more.Foundation.BOOL),POINTER(c_void_p), use_last_error=False)
def _define_PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE_head():
    class AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE(Structure):
        pass
    return AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE
def _define_AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE():
    AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE = win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE_head
    AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE._fields_ = [
        ("Version", UInt64),
        ("pName", win32more.Foundation.PWSTR),
    ]
    return AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE
def _define_AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head():
    class AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE(Structure):
        pass
    return AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE
def _define_AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE():
    AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE = win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head
    AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE._fields_ = [
        ("pValue", c_void_p),
        ("ValueLength", UInt32),
    ]
    return AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE
AUTHZ_SECURITY_ATTRIBUTE_OPERATION = Int32
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE = 0
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL = 1
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD = 2
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE = 3
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE = 4
AUTHZ_SID_OPERATION = Int32
AUTHZ_SID_OPERATION_NONE = 0
AUTHZ_SID_OPERATION_REPLACE_ALL = 1
AUTHZ_SID_OPERATION_ADD = 2
AUTHZ_SID_OPERATION_DELETE = 3
AUTHZ_SID_OPERATION_REPLACE = 4
def _define_AUTHZ_SECURITY_ATTRIBUTE_V1_head():
    class AUTHZ_SECURITY_ATTRIBUTE_V1(Structure):
        pass
    return AUTHZ_SECURITY_ATTRIBUTE_V1
def _define_AUTHZ_SECURITY_ATTRIBUTE_V1():
    AUTHZ_SECURITY_ATTRIBUTE_V1 = win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_V1_head
    class AUTHZ_SECURITY_ATTRIBUTE_V1__Values_e__Union(Union):
        pass
    AUTHZ_SECURITY_ATTRIBUTE_V1__Values_e__Union._fields_ = [
        ("pInt64", POINTER(Int64)),
        ("pUint64", POINTER(UInt64)),
        ("ppString", POINTER(win32more.Foundation.PWSTR)),
        ("pFqbn", POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE_head)),
        ("pOctetString", POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE_head)),
    ]
    AUTHZ_SECURITY_ATTRIBUTE_V1._fields_ = [
        ("pName", win32more.Foundation.PWSTR),
        ("ValueType", UInt16),
        ("Reserved", UInt16),
        ("Flags", win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_FLAGS),
        ("ValueCount", UInt32),
        ("Values", AUTHZ_SECURITY_ATTRIBUTE_V1__Values_e__Union),
    ]
    return AUTHZ_SECURITY_ATTRIBUTE_V1
def _define_AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head():
    class AUTHZ_SECURITY_ATTRIBUTES_INFORMATION(Structure):
        pass
    return AUTHZ_SECURITY_ATTRIBUTES_INFORMATION
def _define_AUTHZ_SECURITY_ATTRIBUTES_INFORMATION():
    AUTHZ_SECURITY_ATTRIBUTES_INFORMATION = win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head
    class AUTHZ_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union(Union):
        pass
    AUTHZ_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union._fields_ = [
        ("pAttributeV1", POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_V1_head)),
    ]
    AUTHZ_SECURITY_ATTRIBUTES_INFORMATION._fields_ = [
        ("Version", UInt16),
        ("Reserved", UInt16),
        ("AttributeCount", UInt32),
        ("Attribute", AUTHZ_SECURITY_ATTRIBUTES_INFORMATION__Attribute_e__Union),
    ]
    return AUTHZ_SECURITY_ATTRIBUTES_INFORMATION
def _define_AUTHZ_RPC_INIT_INFO_CLIENT_head():
    class AUTHZ_RPC_INIT_INFO_CLIENT(Structure):
        pass
    return AUTHZ_RPC_INIT_INFO_CLIENT
def _define_AUTHZ_RPC_INIT_INFO_CLIENT():
    AUTHZ_RPC_INIT_INFO_CLIENT = win32more.Security.Authorization.AUTHZ_RPC_INIT_INFO_CLIENT_head
    AUTHZ_RPC_INIT_INFO_CLIENT._fields_ = [
        ("version", UInt16),
        ("ObjectUuid", win32more.Foundation.PWSTR),
        ("ProtSeq", win32more.Foundation.PWSTR),
        ("NetworkAddr", win32more.Foundation.PWSTR),
        ("Endpoint", win32more.Foundation.PWSTR),
        ("Options", win32more.Foundation.PWSTR),
        ("ServerSpn", win32more.Foundation.PWSTR),
    ]
    return AUTHZ_RPC_INIT_INFO_CLIENT
def _define_AUTHZ_INIT_INFO_head():
    class AUTHZ_INIT_INFO(Structure):
        pass
    return AUTHZ_INIT_INFO
def _define_AUTHZ_INIT_INFO():
    AUTHZ_INIT_INFO = win32more.Security.Authorization.AUTHZ_INIT_INFO_head
    AUTHZ_INIT_INFO._fields_ = [
        ("version", UInt16),
        ("szResourceManagerName", win32more.Foundation.PWSTR),
        ("pfnDynamicAccessCheck", win32more.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK),
        ("pfnComputeDynamicGroups", win32more.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS),
        ("pfnFreeDynamicGroups", win32more.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS),
        ("pfnGetCentralAccessPolicy", win32more.Security.Authorization.PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY),
        ("pfnFreeCentralAccessPolicy", win32more.Security.Authorization.PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY),
    ]
    return AUTHZ_INIT_INFO
AUTHZ_CONTEXT_INFORMATION_CLASS = Int32
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserSid = 1
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoGroupsSids = 2
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoRestrictedSids = 3
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoPrivileges = 4
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoExpirationTime = 5
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoServerContext = 6
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoIdentifier = 7
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSource = 8
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAll = 9
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAuthenticationId = 10
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSecurityAttributes = 11
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceSids = 12
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserClaims = 13
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceClaims = 14
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAppContainerSid = 15
AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoCapabilitySids = 16
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS = Int32
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoFlags = 1
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoOperationType = 2
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectType = 3
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectName = 4
AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoAdditionalInfo = 5
def _define_AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET_head():
    class AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET(Structure):
        pass
    return AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET
def _define_AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET():
    AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET = win32more.Security.Authorization.AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET_head
    AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET._fields_ = [
        ("szObjectTypeName", win32more.Foundation.PWSTR),
        ("dwOffset", UInt32),
    ]
    return AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET
def _define_AUTHZ_SOURCE_SCHEMA_REGISTRATION_head():
    class AUTHZ_SOURCE_SCHEMA_REGISTRATION(Structure):
        pass
    return AUTHZ_SOURCE_SCHEMA_REGISTRATION
def _define_AUTHZ_SOURCE_SCHEMA_REGISTRATION():
    AUTHZ_SOURCE_SCHEMA_REGISTRATION = win32more.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION_head
    class AUTHZ_SOURCE_SCHEMA_REGISTRATION__Anonymous_e__Union(Union):
        pass
    AUTHZ_SOURCE_SCHEMA_REGISTRATION__Anonymous_e__Union._fields_ = [
        ("pReserved", c_void_p),
        ("pProviderGuid", POINTER(Guid)),
    ]
    AUTHZ_SOURCE_SCHEMA_REGISTRATION._anonymous_ = [
        'Anonymous',
    ]
    AUTHZ_SOURCE_SCHEMA_REGISTRATION._fields_ = [
        ("dwFlags", UInt32),
        ("szEventSourceName", win32more.Foundation.PWSTR),
        ("szEventMessageFile", win32more.Foundation.PWSTR),
        ("szEventSourceXmlSchemaFile", win32more.Foundation.PWSTR),
        ("szEventAccessStringsFile", win32more.Foundation.PWSTR),
        ("szExecutableImagePath", win32more.Foundation.PWSTR),
        ("Anonymous", AUTHZ_SOURCE_SCHEMA_REGISTRATION__Anonymous_e__Union),
        ("dwObjectTypeNameCount", UInt32),
        ("ObjectTypeNames", win32more.Security.Authorization.AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET * 0),
    ]
    return AUTHZ_SOURCE_SCHEMA_REGISTRATION
AzAuthorizationStore = Guid('b2bcff59-a757-4b0b-a1bc-ea69981da69e')
AzBizRuleContext = Guid('5c2dc96f-8d51-434b-b33c-379bccae77c3')
AzPrincipalLocator = Guid('483afb5d-70df-4e16-abdc-a1de4d015a3e')
def _define_IAzAuthorizationStore_head():
    class IAzAuthorizationStore(win32more.System.Com.IDispatch_head):
        Guid = Guid('edbd9ca9-9b82-4f6a-9e8b-98301e450f14')
    return IAzAuthorizationStore
def _define_IAzAuthorizationStore():
    IAzAuthorizationStore = win32more.Security.Authorization.IAzAuthorizationStore_head
    IAzAuthorizationStore.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzAuthorizationStore.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Description', ((1, 'bstrDescription'),)))
    IAzAuthorizationStore.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzAuthorizationStore.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzAuthorizationStore.get_DomainTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_DomainTimeout', ((1, 'plProp'),)))
    IAzAuthorizationStore.put_DomainTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_DomainTimeout', ((1, 'lProp'),)))
    IAzAuthorizationStore.get_ScriptEngineTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_ScriptEngineTimeout', ((1, 'plProp'),)))
    IAzAuthorizationStore.put_ScriptEngineTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_ScriptEngineTimeout', ((1, 'lProp'),)))
    IAzAuthorizationStore.get_MaxScriptEngines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_MaxScriptEngines', ((1, 'plProp'),)))
    IAzAuthorizationStore.put_MaxScriptEngines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_MaxScriptEngines', ((1, 'lProp'),)))
    IAzAuthorizationStore.get_GenerateAudits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'get_GenerateAudits', ((1, 'pbProp'),)))
    IAzAuthorizationStore.put_GenerateAudits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(18, 'put_GenerateAudits', ((1, 'bProp'),)))
    IAzAuthorizationStore.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'get_Writable', ((1, 'pfProp'),)))
    IAzAuthorizationStore.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(20, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzAuthorizationStore.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(21, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzAuthorizationStore.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authorization.AZ_PROP_CONSTANTS,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(22, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzAuthorizationStore.get_PolicyAdministrators = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'get_PolicyAdministrators', ((1, 'pvarAdmins'),)))
    IAzAuthorizationStore.get_PolicyReaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_PolicyReaders', ((1, 'pvarReaders'),)))
    IAzAuthorizationStore.AddPolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(26, 'AddPolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeletePolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(27, 'DeletePolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzAuthorizationStore.AddPolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(28, 'AddPolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeletePolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(29, 'DeletePolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzAuthorizationStore.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authorization.AZ_PROP_CONSTANTS,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(30, 'Initialize', ((1, 'lFlags'),(1, 'bstrPolicyURL'),(1, 'varReserved'),)))
    IAzAuthorizationStore.UpdateCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(31, 'UpdateCache', ((1, 'varReserved'),)))
    IAzAuthorizationStore.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(32, 'Delete', ((1, 'varReserved'),)))
    IAzAuthorizationStore.get_Applications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzApplications_head), use_last_error=False)(33, 'get_Applications', ((1, 'ppAppCollection'),)))
    IAzAuthorizationStore.OpenApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplication_head), use_last_error=False)(34, 'OpenApplication', ((1, 'bstrApplicationName'),(1, 'varReserved'),(1, 'ppApplication'),)))
    IAzAuthorizationStore.CreateApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplication_head), use_last_error=False)(35, 'CreateApplication', ((1, 'bstrApplicationName'),(1, 'varReserved'),(1, 'ppApplication'),)))
    IAzAuthorizationStore.DeleteApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(36, 'DeleteApplication', ((1, 'bstrApplicationName'),(1, 'varReserved'),)))
    IAzAuthorizationStore.get_ApplicationGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzApplicationGroups_head), use_last_error=False)(37, 'get_ApplicationGroups', ((1, 'ppGroupCollection'),)))
    IAzAuthorizationStore.CreateApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(38, 'CreateApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzAuthorizationStore.OpenApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(39, 'OpenApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzAuthorizationStore.DeleteApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(40, 'DeleteApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),)))
    IAzAuthorizationStore.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(41, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    IAzAuthorizationStore.get_DelegatedPolicyUsers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(42, 'get_DelegatedPolicyUsers', ((1, 'pvarDelegatedPolicyUsers'),)))
    IAzAuthorizationStore.AddDelegatedPolicyUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(43, 'AddDelegatedPolicyUser', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeleteDelegatedPolicyUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(44, 'DeleteDelegatedPolicyUser', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzAuthorizationStore.get_TargetMachine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_TargetMachine', ((1, 'pbstrTargetMachine'),)))
    IAzAuthorizationStore.get_ApplyStoreSacl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(46, 'get_ApplyStoreSacl', ((1, 'pbApplyStoreSacl'),)))
    IAzAuthorizationStore.put_ApplyStoreSacl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(47, 'put_ApplyStoreSacl', ((1, 'bApplyStoreSacl'),)))
    IAzAuthorizationStore.get_PolicyAdministratorsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(48, 'get_PolicyAdministratorsName', ((1, 'pvarAdmins'),)))
    IAzAuthorizationStore.get_PolicyReadersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'get_PolicyReadersName', ((1, 'pvarReaders'),)))
    IAzAuthorizationStore.AddPolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(50, 'AddPolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeletePolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(51, 'DeletePolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzAuthorizationStore.AddPolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(52, 'AddPolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeletePolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(53, 'DeletePolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzAuthorizationStore.get_DelegatedPolicyUsersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'get_DelegatedPolicyUsersName', ((1, 'pvarDelegatedPolicyUsers'),)))
    IAzAuthorizationStore.AddDelegatedPolicyUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(55, 'AddDelegatedPolicyUserName', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzAuthorizationStore.DeleteDelegatedPolicyUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(56, 'DeleteDelegatedPolicyUserName', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzAuthorizationStore.CloseApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(57, 'CloseApplication', ((1, 'bstrApplicationName'),(1, 'lFlag'),)))
    return IAzAuthorizationStore
def _define_IAzAuthorizationStore2_head():
    class IAzAuthorizationStore2(win32more.Security.Authorization.IAzAuthorizationStore_head):
        Guid = Guid('b11e5584-d577-4273-b6c5-0973e0f8e80d')
    return IAzAuthorizationStore2
def _define_IAzAuthorizationStore2():
    IAzAuthorizationStore2 = win32more.Security.Authorization.IAzAuthorizationStore2_head
    IAzAuthorizationStore2.OpenApplication2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplication2_head), use_last_error=False)(58, 'OpenApplication2', ((1, 'bstrApplicationName'),(1, 'varReserved'),(1, 'ppApplication'),)))
    IAzAuthorizationStore2.CreateApplication2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplication2_head), use_last_error=False)(59, 'CreateApplication2', ((1, 'bstrApplicationName'),(1, 'varReserved'),(1, 'ppApplication'),)))
    return IAzAuthorizationStore2
def _define_IAzAuthorizationStore3_head():
    class IAzAuthorizationStore3(win32more.Security.Authorization.IAzAuthorizationStore2_head):
        Guid = Guid('abc08425-0c86-4fa0-9be3-7189956c926e')
    return IAzAuthorizationStore3
def _define_IAzAuthorizationStore3():
    IAzAuthorizationStore3 = win32more.Security.Authorization.IAzAuthorizationStore3_head
    IAzAuthorizationStore3.IsUpdateNeeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(60, 'IsUpdateNeeded', ((1, 'pbIsUpdateNeeded'),)))
    IAzAuthorizationStore3.BizruleGroupSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(61, 'BizruleGroupSupported', ((1, 'pbSupported'),)))
    IAzAuthorizationStore3.UpgradeStoresFunctionalLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(62, 'UpgradeStoresFunctionalLevel', ((1, 'lFunctionalLevel'),)))
    IAzAuthorizationStore3.IsFunctionalLevelUpgradeSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int16), use_last_error=False)(63, 'IsFunctionalLevelUpgradeSupported', ((1, 'lFunctionalLevel'),(1, 'pbSupported'),)))
    IAzAuthorizationStore3.GetSchemaVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(64, 'GetSchemaVersion', ((1, 'plMajorVersion'),(1, 'plMinorVersion'),)))
    return IAzAuthorizationStore3
def _define_IAzApplication_head():
    class IAzApplication(win32more.System.Com.IDispatch_head):
        Guid = Guid('987bc7c7-b813-4d27-bede-6ba5ae867e95')
    return IAzApplication
def _define_IAzApplication():
    IAzApplication = win32more.Security.Authorization.IAzApplication_head
    IAzApplication.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzApplication.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzApplication.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzApplication.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'bstrDescription'),)))
    IAzApplication.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzApplication.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzApplication.get_AuthzInterfaceClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_AuthzInterfaceClsid', ((1, 'pbstrProp'),)))
    IAzApplication.put_AuthzInterfaceClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_AuthzInterfaceClsid', ((1, 'bstrProp'),)))
    IAzApplication.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Version', ((1, 'pbstrProp'),)))
    IAzApplication.put_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Version', ((1, 'bstrProp'),)))
    IAzApplication.get_GenerateAudits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'get_GenerateAudits', ((1, 'pbProp'),)))
    IAzApplication.put_GenerateAudits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(18, 'put_GenerateAudits', ((1, 'bProp'),)))
    IAzApplication.get_ApplyStoreSacl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'get_ApplyStoreSacl', ((1, 'pbProp'),)))
    IAzApplication.put_ApplyStoreSacl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(20, 'put_ApplyStoreSacl', ((1, 'bProp'),)))
    IAzApplication.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'get_Writable', ((1, 'pfProp'),)))
    IAzApplication.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(22, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzApplication.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplication.get_PolicyAdministrators = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'get_PolicyAdministrators', ((1, 'pvarAdmins'),)))
    IAzApplication.get_PolicyReaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_PolicyReaders', ((1, 'pvarReaders'),)))
    IAzApplication.AddPolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(26, 'AddPolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzApplication.DeletePolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(27, 'DeletePolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzApplication.AddPolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(28, 'AddPolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzApplication.DeletePolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(29, 'DeletePolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzApplication.get_Scopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzScopes_head), use_last_error=False)(30, 'get_Scopes', ((1, 'ppScopeCollection'),)))
    IAzApplication.OpenScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzScope_head), use_last_error=False)(31, 'OpenScope', ((1, 'bstrScopeName'),(1, 'varReserved'),(1, 'ppScope'),)))
    IAzApplication.CreateScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzScope_head), use_last_error=False)(32, 'CreateScope', ((1, 'bstrScopeName'),(1, 'varReserved'),(1, 'ppScope'),)))
    IAzApplication.DeleteScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(33, 'DeleteScope', ((1, 'bstrScopeName'),(1, 'varReserved'),)))
    IAzApplication.get_Operations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzOperations_head), use_last_error=False)(34, 'get_Operations', ((1, 'ppOperationCollection'),)))
    IAzApplication.OpenOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzOperation_head), use_last_error=False)(35, 'OpenOperation', ((1, 'bstrOperationName'),(1, 'varReserved'),(1, 'ppOperation'),)))
    IAzApplication.CreateOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzOperation_head), use_last_error=False)(36, 'CreateOperation', ((1, 'bstrOperationName'),(1, 'varReserved'),(1, 'ppOperation'),)))
    IAzApplication.DeleteOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(37, 'DeleteOperation', ((1, 'bstrOperationName'),(1, 'varReserved'),)))
    IAzApplication.get_Tasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzTasks_head), use_last_error=False)(38, 'get_Tasks', ((1, 'ppTaskCollection'),)))
    IAzApplication.OpenTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzTask_head), use_last_error=False)(39, 'OpenTask', ((1, 'bstrTaskName'),(1, 'varReserved'),(1, 'ppTask'),)))
    IAzApplication.CreateTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzTask_head), use_last_error=False)(40, 'CreateTask', ((1, 'bstrTaskName'),(1, 'varReserved'),(1, 'ppTask'),)))
    IAzApplication.DeleteTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(41, 'DeleteTask', ((1, 'bstrTaskName'),(1, 'varReserved'),)))
    IAzApplication.get_ApplicationGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzApplicationGroups_head), use_last_error=False)(42, 'get_ApplicationGroups', ((1, 'ppGroupCollection'),)))
    IAzApplication.OpenApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(43, 'OpenApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzApplication.CreateApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(44, 'CreateApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzApplication.DeleteApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(45, 'DeleteApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),)))
    IAzApplication.get_Roles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoles_head), use_last_error=False)(46, 'get_Roles', ((1, 'ppRoleCollection'),)))
    IAzApplication.OpenRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzRole_head), use_last_error=False)(47, 'OpenRole', ((1, 'bstrRoleName'),(1, 'varReserved'),(1, 'ppRole'),)))
    IAzApplication.CreateRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzRole_head), use_last_error=False)(48, 'CreateRole', ((1, 'bstrRoleName'),(1, 'varReserved'),(1, 'ppRole'),)))
    IAzApplication.DeleteRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(49, 'DeleteRole', ((1, 'bstrRoleName'),(1, 'varReserved'),)))
    IAzApplication.InitializeClientContextFromToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzClientContext_head), use_last_error=False)(50, 'InitializeClientContextFromToken', ((1, 'ullTokenHandle'),(1, 'varReserved'),(1, 'ppClientContext'),)))
    IAzApplication.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(51, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplication.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(52, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplication.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(53, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    IAzApplication.InitializeClientContextFromName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzClientContext_head), use_last_error=False)(54, 'InitializeClientContextFromName', ((1, 'ClientName'),(1, 'DomainName'),(1, 'varReserved'),(1, 'ppClientContext'),)))
    IAzApplication.get_DelegatedPolicyUsers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(55, 'get_DelegatedPolicyUsers', ((1, 'pvarDelegatedPolicyUsers'),)))
    IAzApplication.AddDelegatedPolicyUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(56, 'AddDelegatedPolicyUser', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzApplication.DeleteDelegatedPolicyUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(57, 'DeleteDelegatedPolicyUser', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzApplication.InitializeClientContextFromStringSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzClientContext_head), use_last_error=False)(58, 'InitializeClientContextFromStringSid', ((1, 'SidString'),(1, 'lOptions'),(1, 'varReserved'),(1, 'ppClientContext'),)))
    IAzApplication.get_PolicyAdministratorsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(59, 'get_PolicyAdministratorsName', ((1, 'pvarAdmins'),)))
    IAzApplication.get_PolicyReadersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(60, 'get_PolicyReadersName', ((1, 'pvarReaders'),)))
    IAzApplication.AddPolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(61, 'AddPolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzApplication.DeletePolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(62, 'DeletePolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzApplication.AddPolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(63, 'AddPolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzApplication.DeletePolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(64, 'DeletePolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzApplication.get_DelegatedPolicyUsersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(65, 'get_DelegatedPolicyUsersName', ((1, 'pvarDelegatedPolicyUsers'),)))
    IAzApplication.AddDelegatedPolicyUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(66, 'AddDelegatedPolicyUserName', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    IAzApplication.DeleteDelegatedPolicyUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(67, 'DeleteDelegatedPolicyUserName', ((1, 'bstrDelegatedPolicyUser'),(1, 'varReserved'),)))
    return IAzApplication
def _define_IAzApplication2_head():
    class IAzApplication2(win32more.Security.Authorization.IAzApplication_head):
        Guid = Guid('086a68af-a249-437c-b18d-d4d86d6a9660')
    return IAzApplication2
def _define_IAzApplication2():
    IAzApplication2 = win32more.Security.Authorization.IAzApplication2_head
    IAzApplication2.InitializeClientContextFromToken2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzClientContext2_head), use_last_error=False)(68, 'InitializeClientContextFromToken2', ((1, 'ulTokenHandleLowPart'),(1, 'ulTokenHandleHighPart'),(1, 'varReserved'),(1, 'ppClientContext'),)))
    IAzApplication2.InitializeClientContext2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzClientContext2_head), use_last_error=False)(69, 'InitializeClientContext2', ((1, 'IdentifyingString'),(1, 'varReserved'),(1, 'ppClientContext'),)))
    return IAzApplication2
def _define_IAzApplications_head():
    class IAzApplications(win32more.System.Com.IDispatch_head):
        Guid = Guid('929b11a9-95c5-4a84-a29a-20ad42c2f16c')
    return IAzApplications
def _define_IAzApplications():
    IAzApplications = win32more.Security.Authorization.IAzApplications_head
    IAzApplications.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzApplications.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzApplications.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzApplications
def _define_IAzOperation_head():
    class IAzOperation(win32more.System.Com.IDispatch_head):
        Guid = Guid('5e56b24f-ea01-4d61-be44-c49b5e4eaf74')
    return IAzOperation
def _define_IAzOperation():
    IAzOperation = win32more.Security.Authorization.IAzOperation_head
    IAzOperation.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzOperation.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzOperation.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzOperation.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'bstrDescription'),)))
    IAzOperation.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzOperation.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzOperation.get_OperationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_OperationID', ((1, 'plProp'),)))
    IAzOperation.put_OperationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_OperationID', ((1, 'lProp'),)))
    IAzOperation.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'get_Writable', ((1, 'pfProp'),)))
    IAzOperation.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzOperation.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(17, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzOperation.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(18, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    return IAzOperation
def _define_IAzOperations_head():
    class IAzOperations(win32more.System.Com.IDispatch_head):
        Guid = Guid('90ef9c07-9706-49d9-af80-0438a5f3ec35')
    return IAzOperations
def _define_IAzOperations():
    IAzOperations = win32more.Security.Authorization.IAzOperations_head
    IAzOperations.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzOperations.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzOperations.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzOperations
def _define_IAzTask_head():
    class IAzTask(win32more.System.Com.IDispatch_head):
        Guid = Guid('cb94e592-2e0e-4a6c-a336-b89a6dc1e388')
    return IAzTask
def _define_IAzTask():
    IAzTask = win32more.Security.Authorization.IAzTask_head
    IAzTask.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzTask.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzTask.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzTask.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'bstrDescription'),)))
    IAzTask.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzTask.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzTask.get_BizRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_BizRule', ((1, 'pbstrProp'),)))
    IAzTask.put_BizRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_BizRule', ((1, 'bstrProp'),)))
    IAzTask.get_BizRuleLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_BizRuleLanguage', ((1, 'pbstrProp'),)))
    IAzTask.put_BizRuleLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_BizRuleLanguage', ((1, 'bstrProp'),)))
    IAzTask.get_BizRuleImportedPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_BizRuleImportedPath', ((1, 'pbstrProp'),)))
    IAzTask.put_BizRuleImportedPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_BizRuleImportedPath', ((1, 'bstrProp'),)))
    IAzTask.get_IsRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'get_IsRoleDefinition', ((1, 'pfProp'),)))
    IAzTask.put_IsRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(20, 'put_IsRoleDefinition', ((1, 'fProp'),)))
    IAzTask.get_Operations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(21, 'get_Operations', ((1, 'pvarProp'),)))
    IAzTask.get_Tasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(22, 'get_Tasks', ((1, 'pvarProp'),)))
    IAzTask.AddOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(23, 'AddOperation', ((1, 'bstrOp'),(1, 'varReserved'),)))
    IAzTask.DeleteOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(24, 'DeleteOperation', ((1, 'bstrOp'),(1, 'varReserved'),)))
    IAzTask.AddTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(25, 'AddTask', ((1, 'bstrTask'),(1, 'varReserved'),)))
    IAzTask.DeleteTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(26, 'DeleteTask', ((1, 'bstrTask'),(1, 'varReserved'),)))
    IAzTask.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(27, 'get_Writable', ((1, 'pfProp'),)))
    IAzTask.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(28, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzTask.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(29, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzTask.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(30, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzTask.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(31, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzTask.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(32, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    return IAzTask
def _define_IAzTasks_head():
    class IAzTasks(win32more.System.Com.IDispatch_head):
        Guid = Guid('b338ccab-4c85-4388-8c0a-c58592bad398')
    return IAzTasks
def _define_IAzTasks():
    IAzTasks = win32more.Security.Authorization.IAzTasks_head
    IAzTasks.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzTasks.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzTasks.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzTasks
def _define_IAzScope_head():
    class IAzScope(win32more.System.Com.IDispatch_head):
        Guid = Guid('00e52487-e08d-4514-b62e-877d5645f5ab')
    return IAzScope
def _define_IAzScope():
    IAzScope = win32more.Security.Authorization.IAzScope_head
    IAzScope.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzScope.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzScope.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzScope.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'bstrDescription'),)))
    IAzScope.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzScope.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzScope.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'get_Writable', ((1, 'pfProp'),)))
    IAzScope.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzScope.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(15, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzScope.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(16, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzScope.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(17, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzScope.get_PolicyAdministrators = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'get_PolicyAdministrators', ((1, 'pvarAdmins'),)))
    IAzScope.get_PolicyReaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'get_PolicyReaders', ((1, 'pvarReaders'),)))
    IAzScope.AddPolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(20, 'AddPolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzScope.DeletePolicyAdministrator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(21, 'DeletePolicyAdministrator', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzScope.AddPolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(22, 'AddPolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzScope.DeletePolicyReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(23, 'DeletePolicyReader', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzScope.get_ApplicationGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzApplicationGroups_head), use_last_error=False)(24, 'get_ApplicationGroups', ((1, 'ppGroupCollection'),)))
    IAzScope.OpenApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(25, 'OpenApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzScope.CreateApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzApplicationGroup_head), use_last_error=False)(26, 'CreateApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),(1, 'ppGroup'),)))
    IAzScope.DeleteApplicationGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(27, 'DeleteApplicationGroup', ((1, 'bstrGroupName'),(1, 'varReserved'),)))
    IAzScope.get_Roles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoles_head), use_last_error=False)(28, 'get_Roles', ((1, 'ppRoleCollection'),)))
    IAzScope.OpenRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzRole_head), use_last_error=False)(29, 'OpenRole', ((1, 'bstrRoleName'),(1, 'varReserved'),(1, 'ppRole'),)))
    IAzScope.CreateRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzRole_head), use_last_error=False)(30, 'CreateRole', ((1, 'bstrRoleName'),(1, 'varReserved'),(1, 'ppRole'),)))
    IAzScope.DeleteRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(31, 'DeleteRole', ((1, 'bstrRoleName'),(1, 'varReserved'),)))
    IAzScope.get_Tasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzTasks_head), use_last_error=False)(32, 'get_Tasks', ((1, 'ppTaskCollection'),)))
    IAzScope.OpenTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzTask_head), use_last_error=False)(33, 'OpenTask', ((1, 'bstrTaskName'),(1, 'varReserved'),(1, 'ppTask'),)))
    IAzScope.CreateTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.Security.Authorization.IAzTask_head), use_last_error=False)(34, 'CreateTask', ((1, 'bstrTaskName'),(1, 'varReserved'),(1, 'ppTask'),)))
    IAzScope.DeleteTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(35, 'DeleteTask', ((1, 'bstrTaskName'),(1, 'varReserved'),)))
    IAzScope.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(36, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    IAzScope.get_CanBeDelegated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(37, 'get_CanBeDelegated', ((1, 'pfProp'),)))
    IAzScope.get_BizrulesWritable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(38, 'get_BizrulesWritable', ((1, 'pfProp'),)))
    IAzScope.get_PolicyAdministratorsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(39, 'get_PolicyAdministratorsName', ((1, 'pvarAdmins'),)))
    IAzScope.get_PolicyReadersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(40, 'get_PolicyReadersName', ((1, 'pvarReaders'),)))
    IAzScope.AddPolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(41, 'AddPolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzScope.DeletePolicyAdministratorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(42, 'DeletePolicyAdministratorName', ((1, 'bstrAdmin'),(1, 'varReserved'),)))
    IAzScope.AddPolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(43, 'AddPolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    IAzScope.DeletePolicyReaderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(44, 'DeletePolicyReaderName', ((1, 'bstrReader'),(1, 'varReserved'),)))
    return IAzScope
def _define_IAzScopes_head():
    class IAzScopes(win32more.System.Com.IDispatch_head):
        Guid = Guid('78e14853-9f5e-406d-9b91-6bdba6973510')
    return IAzScopes
def _define_IAzScopes():
    IAzScopes = win32more.Security.Authorization.IAzScopes_head
    IAzScopes.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzScopes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzScopes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzScopes
def _define_IAzApplicationGroup_head():
    class IAzApplicationGroup(win32more.System.Com.IDispatch_head):
        Guid = Guid('f1b744cd-58a6-4e06-9fbf-36f6d779e21e')
    return IAzApplicationGroup
def _define_IAzApplicationGroup():
    IAzApplicationGroup = win32more.Security.Authorization.IAzApplicationGroup_head
    IAzApplicationGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzApplicationGroup.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzApplicationGroup.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Type', ((1, 'plProp'),)))
    IAzApplicationGroup.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_Type', ((1, 'lProp'),)))
    IAzApplicationGroup.get_LdapQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_LdapQuery', ((1, 'pbstrProp'),)))
    IAzApplicationGroup.put_LdapQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_LdapQuery', ((1, 'bstrProp'),)))
    IAzApplicationGroup.get_AppMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_AppMembers', ((1, 'pvarProp'),)))
    IAzApplicationGroup.get_AppNonMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'get_AppNonMembers', ((1, 'pvarProp'),)))
    IAzApplicationGroup.get_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_Members', ((1, 'pvarProp'),)))
    IAzApplicationGroup.get_NonMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'get_NonMembers', ((1, 'pvarProp'),)))
    IAzApplicationGroup.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzApplicationGroup.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_Description', ((1, 'bstrDescription'),)))
    IAzApplicationGroup.AddAppMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(19, 'AddAppMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteAppMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(20, 'DeleteAppMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddAppNonMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(21, 'AddAppNonMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteAppNonMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(22, 'DeleteAppNonMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(23, 'AddMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(24, 'DeleteMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddNonMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(25, 'AddNonMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteNonMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(26, 'DeleteNonMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(27, 'get_Writable', ((1, 'pfProp'),)))
    IAzApplicationGroup.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(28, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzApplicationGroup.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(29, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(30, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(31, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(32, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(33, 'AddMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(34, 'DeleteMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.AddNonMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(35, 'AddNonMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.DeleteNonMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(36, 'DeleteNonMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzApplicationGroup.get_MembersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(37, 'get_MembersName', ((1, 'pvarProp'),)))
    IAzApplicationGroup.get_NonMembersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(38, 'get_NonMembersName', ((1, 'pvarProp'),)))
    return IAzApplicationGroup
def _define_IAzApplicationGroups_head():
    class IAzApplicationGroups(win32more.System.Com.IDispatch_head):
        Guid = Guid('4ce66ad5-9f3c-469d-a911-b99887a7e685')
    return IAzApplicationGroups
def _define_IAzApplicationGroups():
    IAzApplicationGroups = win32more.Security.Authorization.IAzApplicationGroups_head
    IAzApplicationGroups.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzApplicationGroups.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzApplicationGroups.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzApplicationGroups
def _define_IAzRole_head():
    class IAzRole(win32more.System.Com.IDispatch_head):
        Guid = Guid('859e0d8d-62d7-41d8-a034-c0cd5d43fdfa')
    return IAzRole
def _define_IAzRole():
    IAzRole = win32more.Security.Authorization.IAzRole_head
    IAzRole.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    IAzRole.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'bstrName'),)))
    IAzRole.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'pbstrDescription'),)))
    IAzRole.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'bstrDescription'),)))
    IAzRole.get_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationData', ((1, 'pbstrApplicationData'),)))
    IAzRole.put_ApplicationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationData', ((1, 'bstrApplicationData'),)))
    IAzRole.AddAppMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(13, 'AddAppMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.DeleteAppMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(14, 'DeleteAppMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.AddTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(15, 'AddTask', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.DeleteTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(16, 'DeleteTask', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.AddOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(17, 'AddOperation', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.DeleteOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(18, 'DeleteOperation', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.AddMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(19, 'AddMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.DeleteMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(20, 'DeleteMember', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.get_Writable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'get_Writable', ((1, 'pfProp'),)))
    IAzRole.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(22, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzRole.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'SetProperty', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzRole.get_AppMembers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'get_AppMembers', ((1, 'pvarProp'),)))
    IAzRole.get_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_Members', ((1, 'pvarProp'),)))
    IAzRole.get_Operations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_Operations', ((1, 'pvarProp'),)))
    IAzRole.get_Tasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(27, 'get_Tasks', ((1, 'pvarProp'),)))
    IAzRole.AddPropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(28, 'AddPropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzRole.DeletePropertyItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(29, 'DeletePropertyItem', ((1, 'lPropId'),(1, 'varProp'),(1, 'varReserved'),)))
    IAzRole.Submit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(30, 'Submit', ((1, 'lFlags'),(1, 'varReserved'),)))
    IAzRole.AddMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(31, 'AddMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.DeleteMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(32, 'DeleteMemberName', ((1, 'bstrProp'),(1, 'varReserved'),)))
    IAzRole.get_MembersName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(33, 'get_MembersName', ((1, 'pvarProp'),)))
    return IAzRole
def _define_IAzRoles_head():
    class IAzRoles(win32more.System.Com.IDispatch_head):
        Guid = Guid('95e0f119-13b4-4dae-b65f-2f7d60d822e4')
    return IAzRoles
def _define_IAzRoles():
    IAzRoles = win32more.Security.Authorization.IAzRoles_head
    IAzRoles.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzRoles.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzRoles.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzRoles
def _define_IAzClientContext_head():
    class IAzClientContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('eff1f00b-488a-466d-afd9-a401c5f9eef5')
    return IAzClientContext
def _define_IAzClientContext():
    IAzClientContext = win32more.Security.Authorization.IAzClientContext_head
    IAzClientContext.AccessCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'AccessCheck', ((1, 'bstrObjectName'),(1, 'varScopeNames'),(1, 'varOperations'),(1, 'varParameterNames'),(1, 'varParameterValues'),(1, 'varInterfaceNames'),(1, 'varInterfaceFlags'),(1, 'varInterfaces'),(1, 'pvarResults'),)))
    IAzClientContext.GetBusinessRuleString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetBusinessRuleString', ((1, 'pbstrBusinessRuleString'),)))
    IAzClientContext.get_UserDn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_UserDn', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserSamCompat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_UserSamCompat', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_UserDisplay', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_UserGuid', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserCanonical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_UserCanonical', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserUpn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_UserUpn', ((1, 'pbstrProp'),)))
    IAzClientContext.get_UserDnsSamCompat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_UserDnsSamCompat', ((1, 'pbstrProp'),)))
    IAzClientContext.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'GetProperty', ((1, 'lPropId'),(1, 'varReserved'),(1, 'pvarProp'),)))
    IAzClientContext.GetRoles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'GetRoles', ((1, 'bstrScopeName'),(1, 'pvarRoleNames'),)))
    IAzClientContext.get_RoleForAccessCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_RoleForAccessCheck', ((1, 'pbstrProp'),)))
    IAzClientContext.put_RoleForAccessCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'put_RoleForAccessCheck', ((1, 'bstrProp'),)))
    return IAzClientContext
def _define_IAzClientContext2_head():
    class IAzClientContext2(win32more.Security.Authorization.IAzClientContext_head):
        Guid = Guid('2b0c92b8-208a-488a-8f81-e4edb22111cd')
    return IAzClientContext2
def _define_IAzClientContext2():
    IAzClientContext2 = win32more.Security.Authorization.IAzClientContext2_head
    IAzClientContext2.GetAssignedScopesPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(20, 'GetAssignedScopesPage', ((1, 'lOptions'),(1, 'PageSize'),(1, 'pvarCursor'),(1, 'pvarScopeNames'),)))
    IAzClientContext2.AddRoles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Foundation.BSTR, use_last_error=False)(21, 'AddRoles', ((1, 'varRoles'),(1, 'bstrScopeName'),)))
    IAzClientContext2.AddApplicationGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(22, 'AddApplicationGroups', ((1, 'varApplicationGroups'),)))
    IAzClientContext2.AddStringSids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'AddStringSids', ((1, 'varStringSids'),)))
    IAzClientContext2.put_LDAPQueryDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_LDAPQueryDN', ((1, 'bstrLDAPQueryDN'),)))
    IAzClientContext2.get_LDAPQueryDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_LDAPQueryDN', ((1, 'pbstrLDAPQueryDN'),)))
    return IAzClientContext2
def _define_IAzBizRuleContext_head():
    class IAzBizRuleContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('e192f17d-d59f-455e-a152-940316cd77b2')
    return IAzBizRuleContext
def _define_IAzBizRuleContext():
    IAzBizRuleContext = win32more.Security.Authorization.IAzBizRuleContext_head
    IAzBizRuleContext.put_BusinessRuleResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'put_BusinessRuleResult', ((1, 'bResult'),)))
    IAzBizRuleContext.put_BusinessRuleString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_BusinessRuleString', ((1, 'bstrBusinessRuleString'),)))
    IAzBizRuleContext.get_BusinessRuleString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_BusinessRuleString', ((1, 'pbstrBusinessRuleString'),)))
    IAzBizRuleContext.GetParameter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetParameter', ((1, 'bstrParameterName'),(1, 'pvarParameterValue'),)))
    return IAzBizRuleContext
def _define_IAzBizRuleParameters_head():
    class IAzBizRuleParameters(win32more.System.Com.IDispatch_head):
        Guid = Guid('fc17685f-e25d-4dcd-bae1-276ec9533cb5')
    return IAzBizRuleParameters
def _define_IAzBizRuleParameters():
    IAzBizRuleParameters = win32more.Security.Authorization.IAzBizRuleParameters_head
    IAzBizRuleParameters.AddParameter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(7, 'AddParameter', ((1, 'bstrParameterName'),(1, 'varParameterValue'),)))
    IAzBizRuleParameters.AddParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'AddParameters', ((1, 'varParameterNames'),(1, 'varParameterValues'),)))
    IAzBizRuleParameters.GetParameterValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetParameterValue', ((1, 'bstrParameterName'),(1, 'pvarParameterValue'),)))
    IAzBizRuleParameters.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'Remove', ((1, 'varParameterName'),)))
    IAzBizRuleParameters.RemoveAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RemoveAll', ()))
    IAzBizRuleParameters.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_Count', ((1, 'plCount'),)))
    return IAzBizRuleParameters
def _define_IAzBizRuleInterfaces_head():
    class IAzBizRuleInterfaces(win32more.System.Com.IDispatch_head):
        Guid = Guid('e94128c7-e9da-44cc-b0bd-53036f3aab3d')
    return IAzBizRuleInterfaces
def _define_IAzBizRuleInterfaces():
    IAzBizRuleInterfaces = win32more.Security.Authorization.IAzBizRuleInterfaces_head
    IAzBizRuleInterfaces.AddInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.VARIANT, use_last_error=False)(7, 'AddInterface', ((1, 'bstrInterfaceName'),(1, 'lInterfaceFlag'),(1, 'varInterface'),)))
    IAzBizRuleInterfaces.AddInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'AddInterfaces', ((1, 'varInterfaceNames'),(1, 'varInterfaceFlags'),(1, 'varInterfaces'),)))
    IAzBizRuleInterfaces.GetInterfaceValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetInterfaceValue', ((1, 'bstrInterfaceName'),(1, 'lInterfaceFlag'),(1, 'varInterface'),)))
    IAzBizRuleInterfaces.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'Remove', ((1, 'bstrInterfaceName'),)))
    IAzBizRuleInterfaces.RemoveAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RemoveAll', ()))
    IAzBizRuleInterfaces.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_Count', ((1, 'plCount'),)))
    return IAzBizRuleInterfaces
def _define_IAzClientContext3_head():
    class IAzClientContext3(win32more.Security.Authorization.IAzClientContext2_head):
        Guid = Guid('11894fde-1deb-4b4b-8907-6d1cda1f5d4f')
    return IAzClientContext3
def _define_IAzClientContext3():
    IAzClientContext3 = win32more.Security.Authorization.IAzClientContext3_head
    IAzClientContext3.AccessCheck2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(UInt32), use_last_error=False)(26, 'AccessCheck2', ((1, 'bstrObjectName'),(1, 'bstrScopeName'),(1, 'lOperation'),(1, 'plResult'),)))
    IAzClientContext3.IsInRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(27, 'IsInRoleAssignment', ((1, 'bstrScopeName'),(1, 'bstrRoleName'),(1, 'pbIsInRole'),)))
    IAzClientContext3.GetOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzOperations_head), use_last_error=False)(28, 'GetOperations', ((1, 'bstrScopeName'),(1, 'ppOperationCollection'),)))
    IAzClientContext3.GetTasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzTasks_head), use_last_error=False)(29, 'GetTasks', ((1, 'bstrScopeName'),(1, 'ppTaskCollection'),)))
    IAzClientContext3.get_BizRuleParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzBizRuleParameters_head), use_last_error=False)(30, 'get_BizRuleParameters', ((1, 'ppBizRuleParam'),)))
    IAzClientContext3.get_BizRuleInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzBizRuleInterfaces_head), use_last_error=False)(31, 'get_BizRuleInterfaces', ((1, 'ppBizRuleInterfaces'),)))
    IAzClientContext3.GetGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Security.Authorization.AZ_PROP_CONSTANTS,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'GetGroups', ((1, 'bstrScopeName'),(1, 'ulOptions'),(1, 'pGroupArray'),)))
    IAzClientContext3.get_Sids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(33, 'get_Sids', ((1, 'pStringSidArray'),)))
    return IAzClientContext3
def _define_IAzScope2_head():
    class IAzScope2(win32more.Security.Authorization.IAzScope_head):
        Guid = Guid('ee9fe8c9-c9f3-40e2-aa12-d1d8599727fd')
    return IAzScope2
def _define_IAzScope2():
    IAzScope2 = win32more.Security.Authorization.IAzScope2_head
    IAzScope2.get_RoleDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleDefinitions_head), use_last_error=False)(45, 'get_RoleDefinitions', ((1, 'ppRoleDefinitions'),)))
    IAzScope2.CreateRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleDefinition_head), use_last_error=False)(46, 'CreateRoleDefinition', ((1, 'bstrRoleDefinitionName'),(1, 'ppRoleDefinitions'),)))
    IAzScope2.OpenRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleDefinition_head), use_last_error=False)(47, 'OpenRoleDefinition', ((1, 'bstrRoleDefinitionName'),(1, 'ppRoleDefinitions'),)))
    IAzScope2.DeleteRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(48, 'DeleteRoleDefinition', ((1, 'bstrRoleDefinitionName'),)))
    IAzScope2.get_RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(49, 'get_RoleAssignments', ((1, 'ppRoleAssignments'),)))
    IAzScope2.CreateRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleAssignment_head), use_last_error=False)(50, 'CreateRoleAssignment', ((1, 'bstrRoleAssignmentName'),(1, 'ppRoleAssignment'),)))
    IAzScope2.OpenRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleAssignment_head), use_last_error=False)(51, 'OpenRoleAssignment', ((1, 'bstrRoleAssignmentName'),(1, 'ppRoleAssignment'),)))
    IAzScope2.DeleteRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(52, 'DeleteRoleAssignment', ((1, 'bstrRoleAssignmentName'),)))
    return IAzScope2
def _define_IAzApplication3_head():
    class IAzApplication3(win32more.Security.Authorization.IAzApplication2_head):
        Guid = Guid('181c845e-7196-4a7d-ac2e-020c0bb7a303')
    return IAzApplication3
def _define_IAzApplication3():
    IAzApplication3 = win32more.Security.Authorization.IAzApplication3_head
    IAzApplication3.ScopeExists = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(70, 'ScopeExists', ((1, 'bstrScopeName'),(1, 'pbExist'),)))
    IAzApplication3.OpenScope2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzScope2_head), use_last_error=False)(71, 'OpenScope2', ((1, 'bstrScopeName'),(1, 'ppScope2'),)))
    IAzApplication3.CreateScope2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzScope2_head), use_last_error=False)(72, 'CreateScope2', ((1, 'bstrScopeName'),(1, 'ppScope2'),)))
    IAzApplication3.DeleteScope2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(73, 'DeleteScope2', ((1, 'bstrScopeName'),)))
    IAzApplication3.get_RoleDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleDefinitions_head), use_last_error=False)(74, 'get_RoleDefinitions', ((1, 'ppRoleDefinitions'),)))
    IAzApplication3.CreateRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleDefinition_head), use_last_error=False)(75, 'CreateRoleDefinition', ((1, 'bstrRoleDefinitionName'),(1, 'ppRoleDefinitions'),)))
    IAzApplication3.OpenRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleDefinition_head), use_last_error=False)(76, 'OpenRoleDefinition', ((1, 'bstrRoleDefinitionName'),(1, 'ppRoleDefinitions'),)))
    IAzApplication3.DeleteRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(77, 'DeleteRoleDefinition', ((1, 'bstrRoleDefinitionName'),)))
    IAzApplication3.get_RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(78, 'get_RoleAssignments', ((1, 'ppRoleAssignments'),)))
    IAzApplication3.CreateRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleAssignment_head), use_last_error=False)(79, 'CreateRoleAssignment', ((1, 'bstrRoleAssignmentName'),(1, 'ppRoleAssignment'),)))
    IAzApplication3.OpenRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Security.Authorization.IAzRoleAssignment_head), use_last_error=False)(80, 'OpenRoleAssignment', ((1, 'bstrRoleAssignmentName'),(1, 'ppRoleAssignment'),)))
    IAzApplication3.DeleteRoleAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(81, 'DeleteRoleAssignment', ((1, 'bstrRoleAssignmentName'),)))
    IAzApplication3.get_BizRulesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(82, 'get_BizRulesEnabled', ((1, 'pbEnabled'),)))
    IAzApplication3.put_BizRulesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(83, 'put_BizRulesEnabled', ((1, 'bEnabled'),)))
    return IAzApplication3
def _define_IAzOperation2_head():
    class IAzOperation2(win32more.Security.Authorization.IAzOperation_head):
        Guid = Guid('1f5ea01f-44a2-4184-9c48-a75b4dcc8ccc')
    return IAzOperation2
def _define_IAzOperation2():
    IAzOperation2 = win32more.Security.Authorization.IAzOperation2_head
    IAzOperation2.RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(19, 'RoleAssignments', ((1, 'bstrScopeName'),(1, 'bRecursive'),(1, 'ppRoleAssignments'),)))
    return IAzOperation2
def _define_IAzRoleDefinitions_head():
    class IAzRoleDefinitions(win32more.System.Com.IDispatch_head):
        Guid = Guid('881f25a5-d755-4550-957a-d503a3b34001')
    return IAzRoleDefinitions
def _define_IAzRoleDefinitions():
    IAzRoleDefinitions = win32more.Security.Authorization.IAzRoleDefinitions_head
    IAzRoleDefinitions.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzRoleDefinitions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzRoleDefinitions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzRoleDefinitions
def _define_IAzRoleDefinition_head():
    class IAzRoleDefinition(win32more.Security.Authorization.IAzTask_head):
        Guid = Guid('d97fcea1-2599-44f1-9fc3-58e9fbe09466')
    return IAzRoleDefinition
def _define_IAzRoleDefinition():
    IAzRoleDefinition = win32more.Security.Authorization.IAzRoleDefinition_head
    IAzRoleDefinition.RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(33, 'RoleAssignments', ((1, 'bstrScopeName'),(1, 'bRecursive'),(1, 'ppRoleAssignments'),)))
    IAzRoleDefinition.AddRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'AddRoleDefinition', ((1, 'bstrRoleDefinition'),)))
    IAzRoleDefinition.DeleteRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'DeleteRoleDefinition', ((1, 'bstrRoleDefinition'),)))
    IAzRoleDefinition.get_RoleDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleDefinitions_head), use_last_error=False)(36, 'get_RoleDefinitions', ((1, 'ppRoleDefinitions'),)))
    return IAzRoleDefinition
def _define_IAzRoleAssignment_head():
    class IAzRoleAssignment(win32more.Security.Authorization.IAzRole_head):
        Guid = Guid('55647d31-0d5a-4fa3-b4ac-2b5f9ad5ab76')
    return IAzRoleAssignment
def _define_IAzRoleAssignment():
    IAzRoleAssignment = win32more.Security.Authorization.IAzRoleAssignment_head
    IAzRoleAssignment.AddRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'AddRoleDefinition', ((1, 'bstrRoleDefinition'),)))
    IAzRoleAssignment.DeleteRoleDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'DeleteRoleDefinition', ((1, 'bstrRoleDefinition'),)))
    IAzRoleAssignment.get_RoleDefinitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzRoleDefinitions_head), use_last_error=False)(36, 'get_RoleDefinitions', ((1, 'ppRoleDefinitions'),)))
    IAzRoleAssignment.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzScope_head), use_last_error=False)(37, 'get_Scope', ((1, 'ppScope'),)))
    return IAzRoleAssignment
def _define_IAzRoleAssignments_head():
    class IAzRoleAssignments(win32more.System.Com.IDispatch_head):
        Guid = Guid('9c80b900-fceb-4d73-a0f4-c83b0bbf2481')
    return IAzRoleAssignments
def _define_IAzRoleAssignments():
    IAzRoleAssignments = win32more.Security.Authorization.IAzRoleAssignments_head
    IAzRoleAssignments.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Item', ((1, 'Index'),(1, 'pvarObtPtr'),)))
    IAzRoleAssignments.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'plCount'),)))
    IAzRoleAssignments.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumPtr'),)))
    return IAzRoleAssignments
def _define_IAzPrincipalLocator_head():
    class IAzPrincipalLocator(win32more.System.Com.IDispatch_head):
        Guid = Guid('e5c3507d-ad6a-4992-9c7f-74ab480b44cc')
    return IAzPrincipalLocator
def _define_IAzPrincipalLocator():
    IAzPrincipalLocator = win32more.Security.Authorization.IAzPrincipalLocator_head
    IAzPrincipalLocator.get_NameResolver = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzNameResolver_head), use_last_error=False)(7, 'get_NameResolver', ((1, 'ppNameResolver'),)))
    IAzPrincipalLocator.get_ObjectPicker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.IAzObjectPicker_head), use_last_error=False)(8, 'get_ObjectPicker', ((1, 'ppObjectPicker'),)))
    return IAzPrincipalLocator
def _define_IAzNameResolver_head():
    class IAzNameResolver(win32more.System.Com.IDispatch_head):
        Guid = Guid('504d0f15-73e2-43df-a870-a64f40714f53')
    return IAzNameResolver
def _define_IAzNameResolver():
    IAzNameResolver = win32more.Security.Authorization.IAzNameResolver_head
    IAzNameResolver.NameFromSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'NameFromSid', ((1, 'bstrSid'),(1, 'pSidType'),(1, 'pbstrName'),)))
    IAzNameResolver.NamesFromSids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'NamesFromSids', ((1, 'vSids'),(1, 'pvSidTypes'),(1, 'pvNames'),)))
    return IAzNameResolver
def _define_IAzObjectPicker_head():
    class IAzObjectPicker(win32more.System.Com.IDispatch_head):
        Guid = Guid('63130a48-699a-42d8-bf01-c62ac3fb79f9')
    return IAzObjectPicker
def _define_IAzObjectPicker():
    IAzObjectPicker = win32more.Security.Authorization.IAzObjectPicker_head
    IAzObjectPicker.GetPrincipals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetPrincipals', ((1, 'hParentWnd'),(1, 'bstrTitle'),(1, 'pvSidTypes'),(1, 'pvNames'),(1, 'pvSids'),)))
    IAzObjectPicker.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Name', ((1, 'pbstrName'),)))
    return IAzObjectPicker
def _define_IAzApplicationGroup2_head():
    class IAzApplicationGroup2(win32more.Security.Authorization.IAzApplicationGroup_head):
        Guid = Guid('3f0613fc-b71a-464e-a11d-5b881a56cefa')
    return IAzApplicationGroup2
def _define_IAzApplicationGroup2():
    IAzApplicationGroup2 = win32more.Security.Authorization.IAzApplicationGroup2_head
    IAzApplicationGroup2.get_BizRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(39, 'get_BizRule', ((1, 'pbstrProp'),)))
    IAzApplicationGroup2.put_BizRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(40, 'put_BizRule', ((1, 'bstrProp'),)))
    IAzApplicationGroup2.get_BizRuleLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(41, 'get_BizRuleLanguage', ((1, 'pbstrProp'),)))
    IAzApplicationGroup2.put_BizRuleLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(42, 'put_BizRuleLanguage', ((1, 'bstrProp'),)))
    IAzApplicationGroup2.get_BizRuleImportedPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(43, 'get_BizRuleImportedPath', ((1, 'pbstrProp'),)))
    IAzApplicationGroup2.put_BizRuleImportedPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(44, 'put_BizRuleImportedPath', ((1, 'bstrProp'),)))
    IAzApplicationGroup2.RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(45, 'RoleAssignments', ((1, 'bstrScopeName'),(1, 'bRecursive'),(1, 'ppRoleAssignments'),)))
    return IAzApplicationGroup2
def _define_IAzTask2_head():
    class IAzTask2(win32more.Security.Authorization.IAzTask_head):
        Guid = Guid('03a9a5ee-48c8-4832-9025-aad503c46526')
    return IAzTask2
def _define_IAzTask2():
    IAzTask2 = win32more.Security.Authorization.IAzTask2_head
    IAzTask2.RoleAssignments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.Security.Authorization.IAzRoleAssignments_head), use_last_error=False)(33, 'RoleAssignments', ((1, 'bstrScopeName'),(1, 'bRecursive'),(1, 'ppRoleAssignments'),)))
    return IAzTask2
AZ_PROP_CONSTANTS = Int32
AZ_PROP_NAME = 1
AZ_PROP_DESCRIPTION = 2
AZ_PROP_WRITABLE = 3
AZ_PROP_APPLICATION_DATA = 4
AZ_PROP_CHILD_CREATE = 5
AZ_MAX_APPLICATION_NAME_LENGTH = 512
AZ_MAX_OPERATION_NAME_LENGTH = 64
AZ_MAX_TASK_NAME_LENGTH = 64
AZ_MAX_SCOPE_NAME_LENGTH = 65536
AZ_MAX_GROUP_NAME_LENGTH = 64
AZ_MAX_ROLE_NAME_LENGTH = 64
AZ_MAX_NAME_LENGTH = 65536
AZ_MAX_DESCRIPTION_LENGTH = 1024
AZ_MAX_APPLICATION_DATA_LENGTH = 4096
AZ_SUBMIT_FLAG_ABORT = 1
AZ_SUBMIT_FLAG_FLUSH = 2
AZ_MAX_POLICY_URL_LENGTH = 65536
AZ_AZSTORE_FLAG_CREATE = 1
AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY = 2
AZ_AZSTORE_FLAG_BATCH_UPDATE = 4
AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL = 8
AZ_AZSTORE_FORCE_APPLICATION_CLOSE = 16
AZ_AZSTORE_NT6_FUNCTION_LEVEL = 32
AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT = 32768
AZ_PROP_AZSTORE_DOMAIN_TIMEOUT = 100
AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT = 15000
AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT = 101
AZ_AZSTORE_MIN_DOMAIN_TIMEOUT = 500
AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT = 5000
AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT = 45000
AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES = 102
AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES = 120
AZ_PROP_AZSTORE_MAJOR_VERSION = 103
AZ_PROP_AZSTORE_MINOR_VERSION = 104
AZ_PROP_AZSTORE_TARGET_MACHINE = 105
AZ_PROP_AZTORE_IS_ADAM_INSTANCE = 106
AZ_PROP_OPERATION_ID = 200
AZ_PROP_TASK_OPERATIONS = 300
AZ_PROP_TASK_BIZRULE = 301
AZ_PROP_TASK_BIZRULE_LANGUAGE = 302
AZ_PROP_TASK_TASKS = 303
AZ_PROP_TASK_BIZRULE_IMPORTED_PATH = 304
AZ_PROP_TASK_IS_ROLE_DEFINITION = 305
AZ_MAX_TASK_BIZRULE_LENGTH = 65536
AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH = 64
AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH = 512
AZ_MAX_BIZRULE_STRING = 65536
AZ_PROP_GROUP_TYPE = 400
AZ_GROUPTYPE_LDAP_QUERY = 1
AZ_GROUPTYPE_BASIC = 2
AZ_GROUPTYPE_BIZRULE = 3
AZ_PROP_GROUP_APP_MEMBERS = 401
AZ_PROP_GROUP_APP_NON_MEMBERS = 402
AZ_PROP_GROUP_LDAP_QUERY = 403
AZ_MAX_GROUP_LDAP_QUERY_LENGTH = 4096
AZ_PROP_GROUP_MEMBERS = 404
AZ_PROP_GROUP_NON_MEMBERS = 405
AZ_PROP_GROUP_MEMBERS_NAME = 406
AZ_PROP_GROUP_NON_MEMBERS_NAME = 407
AZ_PROP_GROUP_BIZRULE = 408
AZ_PROP_GROUP_BIZRULE_LANGUAGE = 409
AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH = 410
AZ_MAX_GROUP_BIZRULE_LENGTH = 65536
AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH = 64
AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH = 512
AZ_PROP_ROLE_APP_MEMBERS = 500
AZ_PROP_ROLE_MEMBERS = 501
AZ_PROP_ROLE_OPERATIONS = 502
AZ_PROP_ROLE_TASKS = 504
AZ_PROP_ROLE_MEMBERS_NAME = 505
AZ_PROP_SCOPE_BIZRULES_WRITABLE = 600
AZ_PROP_SCOPE_CAN_BE_DELEGATED = 601
AZ_PROP_CLIENT_CONTEXT_USER_DN = 700
AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT = 701
AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY = 702
AZ_PROP_CLIENT_CONTEXT_USER_GUID = 703
AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL = 704
AZ_PROP_CLIENT_CONTEXT_USER_UPN = 705
AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT = 707
AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK = 708
AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN = 709
AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID = 800
AZ_PROP_APPLICATION_VERSION = 801
AZ_MAX_APPLICATION_VERSION_LENGTH = 512
AZ_PROP_APPLICATION_NAME = 802
AZ_PROP_APPLICATION_BIZRULE_ENABLED = 803
AZ_PROP_APPLY_STORE_SACL = 900
AZ_PROP_GENERATE_AUDITS = 901
AZ_PROP_POLICY_ADMINS = 902
AZ_PROP_POLICY_READERS = 903
AZ_PROP_DELEGATED_POLICY_USERS = 904
AZ_PROP_POLICY_ADMINS_NAME = 905
AZ_PROP_POLICY_READERS_NAME = 906
AZ_PROP_DELEGATED_POLICY_USERS_NAME = 907
AZ_CLIENT_CONTEXT_SKIP_GROUP = 1
AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY = 1
AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE = 2
AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY = 2
def _define_FN_PROGRESS():
    return CFUNCTYPE(Void,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.PROG_INVOKE_SETTING),c_void_p,win32more.Foundation.BOOL, use_last_error=False)
AUTHZ_ACCESS_CHECK_RESULTS_HANDLE = IntPtr
AUTHZ_CLIENT_CONTEXT_HANDLE = IntPtr
AUTHZ_RESOURCE_MANAGER_HANDLE = IntPtr
AUTHZ_AUDIT_EVENT_HANDLE = IntPtr
AUTHZ_AUDIT_EVENT_TYPE_HANDLE = IntPtr
AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE = IntPtr
def _define_AuthzAccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_ACCESS_CHECK_FLAGS,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REQUEST_head),win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),UInt32,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REPLY_head),POINTER(IntPtr), use_last_error=True)(("AuthzAccessCheck", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAuthzClientContext'),(1, 'pRequest'),(1, 'hAuditEvent'),(1, 'pSecurityDescriptor'),(1, 'OptionalSecurityDescriptorArray'),(1, 'OptionalSecurityDescriptorCount'),(1, 'pReply'),(1, 'phAccessCheckResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzCachedAccessCheck():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REQUEST_head),win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REPLY_head), use_last_error=True)(("AuthzCachedAccessCheck", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAccessCheckResults'),(1, 'pRequest'),(1, 'hAuditEvent'),(1, 'pReply'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzOpenObjectAudit():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REQUEST_head),win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),UInt32,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REPLY_head), use_last_error=True)(("AuthzOpenObjectAudit", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAuthzClientContext'),(1, 'pRequest'),(1, 'hAuditEvent'),(1, 'pSecurityDescriptor'),(1, 'OptionalSecurityDescriptorArray'),(1, 'OptionalSecurityDescriptorCount'),(1, 'pReply'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzFreeHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_ACCESS_CHECK_RESULTS_HANDLE, use_last_error=True)(("AuthzFreeHandle", windll["AUTHZ"]), ((1, 'hAccessCheckResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.PFN_AUTHZ_DYNAMIC_ACCESS_CHECK,win32more.Security.Authorization.PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS,win32more.Security.Authorization.PFN_AUTHZ_FREE_DYNAMIC_GROUPS,win32more.Foundation.PWSTR,POINTER(win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE), use_last_error=True)(("AuthzInitializeResourceManager", windll["AUTHZ"]), ((1, 'Flags'),(1, 'pfnDynamicAccessCheck'),(1, 'pfnComputeDynamicGroups'),(1, 'pfnFreeDynamicGroups'),(1, 'szResourceManagerName'),(1, 'phAuthzResourceManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeResourceManagerEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_FLAGS,POINTER(win32more.Security.Authorization.AUTHZ_INIT_INFO_head),POINTER(win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE), use_last_error=True)(("AuthzInitializeResourceManagerEx", windll["AUTHZ"]), ((1, 'Flags'),(1, 'pAuthzInitInfo'),(1, 'phAuthzResourceManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeRemoteResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Authorization.AUTHZ_RPC_INIT_INFO_CLIENT_head),POINTER(win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE), use_last_error=True)(("AuthzInitializeRemoteResourceManager", windll["AUTHZ"]), ((1, 'pRpcInitInfo'),(1, 'phAuthzResourceManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzFreeResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE, use_last_error=True)(("AuthzFreeResourceManager", windll["AUTHZ"]), ((1, 'hAuthzResourceManager'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeContextFromToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE,win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.LUID,c_void_p,POINTER(IntPtr), use_last_error=True)(("AuthzInitializeContextFromToken", windll["AUTHZ"]), ((1, 'Flags'),(1, 'TokenHandle'),(1, 'hAuthzResourceManager'),(1, 'pExpirationTime'),(1, 'Identifier'),(1, 'DynamicGroupArgs'),(1, 'phAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeContextFromSid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSID,win32more.Security.Authorization.AUTHZ_RESOURCE_MANAGER_HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.LUID,c_void_p,POINTER(IntPtr), use_last_error=True)(("AuthzInitializeContextFromSid", windll["AUTHZ"]), ((1, 'Flags'),(1, 'UserSid'),(1, 'hAuthzResourceManager'),(1, 'pExpirationTime'),(1, 'Identifier'),(1, 'DynamicGroupArgs'),(1, 'phAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeContextFromAuthzContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Foundation.LUID,c_void_p,POINTER(IntPtr), use_last_error=True)(("AuthzInitializeContextFromAuthzContext", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAuthzClientContext'),(1, 'pExpirationTime'),(1, 'Identifier'),(1, 'DynamicGroupArgs'),(1, 'phNewAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeCompoundContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(IntPtr), use_last_error=True)(("AuthzInitializeCompoundContext", windll["AUTHZ"]), ((1, 'UserContext'),(1, 'DeviceContext'),(1, 'phCompoundContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzAddSidsToContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.SID_AND_ATTRIBUTES_head),UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES_head),UInt32,POINTER(IntPtr), use_last_error=True)(("AuthzAddSidsToContext", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'Sids'),(1, 'SidCount'),(1, 'RestrictedSids'),(1, 'RestrictedSidCount'),(1, 'phNewAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzModifySecurityAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), use_last_error=True)(("AuthzModifySecurityAttributes", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'pOperations'),(1, 'pAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzModifyClaims():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS,POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), use_last_error=True)(("AuthzModifyClaims", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'ClaimClass'),(1, 'pClaimOperations'),(1, 'pClaims'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzModifySids():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS,POINTER(win32more.Security.Authorization.AUTHZ_SID_OPERATION),POINTER(win32more.Security.TOKEN_GROUPS_head), use_last_error=True)(("AuthzModifySids", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'SidClass'),(1, 'pSidOperations'),(1, 'pSids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzSetAppContainerInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Foundation.PSID,UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES), use_last_error=True)(("AuthzSetAppContainerInformation", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'pAppContainerSid'),(1, 'CapabilityCount'),(1, 'pCapabilitySids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzGetInformationFromContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,win32more.Security.Authorization.AUTHZ_CONTEXT_INFORMATION_CLASS,UInt32,POINTER(UInt32),c_void_p, use_last_error=True)(("AuthzGetInformationFromContext", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),(1, 'InfoClass'),(1, 'BufferSize'),(1, 'pSizeRequired'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzFreeContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE, use_last_error=True)(("AuthzFreeContext", windll["AUTHZ"]), ((1, 'hAuthzClientContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeObjectAccessAuditEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS,win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(IntPtr),UInt32, use_last_error=True)(("AuthzInitializeObjectAccessAuditEvent", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAuditEventType'),(1, 'szOperationType'),(1, 'szObjectType'),(1, 'szObjectName'),(1, 'szAdditionalInfo'),(1, 'phAuditEvent'),(1, 'dwAdditionalParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInitializeObjectAccessAuditEvent2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_TYPE_HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(IntPtr),UInt32, use_last_error=True)(("AuthzInitializeObjectAccessAuditEvent2", windll["AUTHZ"]), ((1, 'Flags'),(1, 'hAuditEventType'),(1, 'szOperationType'),(1, 'szObjectType'),(1, 'szObjectName'),(1, 'szAdditionalInfo'),(1, 'szAdditionalInfo2'),(1, 'phAuditEvent'),(1, 'dwAdditionalParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzFreeAuditEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_AUDIT_EVENT_HANDLE, use_last_error=True)(("AuthzFreeAuditEvent", windll["AUTHZ"]), ((1, 'hAuditEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzEvaluateSacl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.Authorization.AUTHZ_CLIENT_CONTEXT_HANDLE,POINTER(win32more.Security.Authorization.AUTHZ_ACCESS_REQUEST_head),POINTER(win32more.Security.ACL_head),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("AuthzEvaluateSacl", windll["AUTHZ"]), ((1, 'AuthzClientContext'),(1, 'pRequest'),(1, 'Sacl'),(1, 'GrantedAccess'),(1, 'AccessGranted'),(1, 'pbGenerateAudit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzInstallSecurityEventSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION_head), use_last_error=True)(("AuthzInstallSecurityEventSource", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'pRegistration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzUninstallSecurityEventSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR, use_last_error=True)(("AuthzUninstallSecurityEventSource", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'szEventSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzEnumerateSecurityEventSources():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Security.Authorization.AUTHZ_SOURCE_SCHEMA_REGISTRATION_head),POINTER(UInt32),POINTER(UInt32), use_last_error=True)(("AuthzEnumerateSecurityEventSources", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'Buffer'),(1, 'pdwCount'),(1, 'pdwLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzRegisterSecurityEventSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(IntPtr), use_last_error=True)(("AuthzRegisterSecurityEventSource", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'szEventSourceName'),(1, 'phEventProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzUnregisterSecurityEventSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(IntPtr), use_last_error=True)(("AuthzUnregisterSecurityEventSource", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'phEventProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzReportSecurityEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE,UInt32,win32more.Foundation.PSID,UInt32, use_last_error=True)(("AuthzReportSecurityEvent", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'hEventProvider'),(1, 'dwAuditId'),(1, 'pUserSid'),(1, 'dwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzReportSecurityEventFromParams():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Security.Authorization.AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE,UInt32,win32more.Foundation.PSID,POINTER(win32more.Security.Authorization.AUDIT_PARAMS_head), use_last_error=True)(("AuthzReportSecurityEventFromParams", windll["AUTHZ"]), ((1, 'dwFlags'),(1, 'hEventProvider'),(1, 'dwAuditId'),(1, 'pUserSid'),(1, 'pParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzRegisterCapChangeNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(POINTER(win32more.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE___head)),win32more.System.Threading.LPTHREAD_START_ROUTINE,c_void_p, use_last_error=True)(("AuthzRegisterCapChangeNotification", windll["AUTHZ"]), ((1, 'phCapChangeSubscription'),(1, 'pfnCapChangeCallback'),(1, 'pCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzUnregisterCapChangeNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.Authorization.AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE___head), use_last_error=True)(("AuthzUnregisterCapChangeNotification", windll["AUTHZ"]), ((1, 'hCapChangeSubscription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AuthzFreeCentralAccessPolicyCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=True)(("AuthzFreeCentralAccessPolicyCache", windll["AUTHZ"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEntriesInAclA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A),POINTER(win32more.Security.ACL_head),POINTER(POINTER(win32more.Security.ACL_head)), use_last_error=False)(("SetEntriesInAclA", windll["ADVAPI32"]), ((1, 'cCountOfExplicitEntries'),(1, 'pListOfExplicitEntries'),(1, 'OldAcl'),(1, 'NewAcl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEntriesInAclW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W),POINTER(win32more.Security.ACL_head),POINTER(POINTER(win32more.Security.ACL_head)), use_last_error=False)(("SetEntriesInAclW", windll["ADVAPI32"]), ((1, 'cCountOfExplicitEntries'),(1, 'pListOfExplicitEntries'),(1, 'OldAcl'),(1, 'NewAcl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEntriesInAcl():
    return win32more.Security.Authorization.SetEntriesInAclW
def _define_GetExplicitEntriesFromAclA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A_head)), use_last_error=False)(("GetExplicitEntriesFromAclA", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pcCountOfExplicitEntries'),(1, 'pListOfExplicitEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExplicitEntriesFromAclW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W_head)), use_last_error=False)(("GetExplicitEntriesFromAclW", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pcCountOfExplicitEntries'),(1, 'pListOfExplicitEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExplicitEntriesFromAcl():
    return win32more.Security.Authorization.GetExplicitEntriesFromAclW
def _define_GetEffectiveRightsFromAclA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(UInt32), use_last_error=False)(("GetEffectiveRightsFromAclA", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pTrustee'),(1, 'pAccessRights'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEffectiveRightsFromAclW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(UInt32), use_last_error=False)(("GetEffectiveRightsFromAclW", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pTrustee'),(1, 'pAccessRights'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEffectiveRightsFromAcl():
    return win32more.Security.Authorization.GetEffectiveRightsFromAclW
def _define_GetAuditedPermissionsFromAclA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetAuditedPermissionsFromAclA", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pTrustee'),(1, 'pSuccessfulAuditedRights'),(1, 'pFailedAuditRights'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAuditedPermissionsFromAclW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetAuditedPermissionsFromAclW", windll["ADVAPI32"]), ((1, 'pacl'),(1, 'pTrustee'),(1, 'pSuccessfulAuditedRights'),(1, 'pFailedAuditRights'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAuditedPermissionsFromAcl():
    return win32more.Security.Authorization.GetAuditedPermissionsFromAclW
def _define_GetNamedSecurityInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Security.OBJECT_SECURITY_INFORMATION,POINTER(win32more.Foundation.PSID),POINTER(win32more.Foundation.PSID),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=False)(("GetNamedSecurityInfoA", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'ppsidOwner'),(1, 'ppsidGroup'),(1, 'ppDacl'),(1, 'ppSacl'),(1, 'ppSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedSecurityInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Security.OBJECT_SECURITY_INFORMATION,POINTER(win32more.Foundation.PSID),POINTER(win32more.Foundation.PSID),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=False)(("GetNamedSecurityInfoW", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'ppsidOwner'),(1, 'ppsidGroup'),(1, 'ppDacl'),(1, 'ppSacl'),(1, 'ppSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedSecurityInfo():
    return win32more.Security.Authorization.GetNamedSecurityInfoW
def _define_GetSecurityInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,POINTER(win32more.Foundation.PSID),POINTER(win32more.Foundation.PSID),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.ACL_head)),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=False)(("GetSecurityInfo", windll["ADVAPI32"]), ((1, 'handle'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'ppsidOwner'),(1, 'ppsidGroup'),(1, 'ppDacl'),(1, 'ppSacl'),(1, 'ppSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNamedSecurityInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Security.OBJECT_SECURITY_INFORMATION,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head), use_last_error=False)(("SetNamedSecurityInfoA", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'psidOwner'),(1, 'psidGroup'),(1, 'pDacl'),(1, 'pSacl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNamedSecurityInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Security.OBJECT_SECURITY_INFORMATION,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head), use_last_error=False)(("SetNamedSecurityInfoW", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'psidOwner'),(1, 'psidGroup'),(1, 'pDacl'),(1, 'pSacl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetNamedSecurityInfo():
    return win32more.Security.Authorization.SetNamedSecurityInfoW
def _define_SetSecurityInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head), use_last_error=False)(("SetSecurityInfo", windll["ADVAPI32"]), ((1, 'handle'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'psidOwner'),(1, 'psidGroup'),(1, 'pDacl'),(1, 'pSacl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInheritanceSourceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.BOOL,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.FN_OBJECT_MGR_FUNCTIONS_head),POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.Authorization.INHERITED_FROMA_head), use_last_error=False)(("GetInheritanceSourceA", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'Container'),(1, 'pObjectClassGuids'),(1, 'GuidCount'),(1, 'pAcl'),(1, 'pfnArray'),(1, 'pGenericMapping'),(1, 'pInheritArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInheritanceSourceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.BOOL,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.Authorization.FN_OBJECT_MGR_FUNCTIONS_head),POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.Authorization.INHERITED_FROMW_head), use_last_error=False)(("GetInheritanceSourceW", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'Container'),(1, 'pObjectClassGuids'),(1, 'GuidCount'),(1, 'pAcl'),(1, 'pfnArray'),(1, 'pGenericMapping'),(1, 'pInheritArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInheritanceSource():
    return win32more.Security.Authorization.GetInheritanceSourceW
def _define_FreeInheritedFromArray():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Authorization.INHERITED_FROMW),UInt16,POINTER(win32more.Security.Authorization.FN_OBJECT_MGR_FUNCTIONS_head), use_last_error=False)(("FreeInheritedFromArray", windll["ADVAPI32"]), ((1, 'pInheritArray'),(1, 'AceCnt'),(1, 'pfnArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TreeResetNamedSecurityInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head),win32more.Foundation.BOOL,win32more.Security.Authorization.FN_PROGRESS,win32more.Security.Authorization.PROG_INVOKE_SETTING,c_void_p, use_last_error=False)(("TreeResetNamedSecurityInfoA", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'pOwner'),(1, 'pGroup'),(1, 'pDacl'),(1, 'pSacl'),(1, 'KeepExplicit'),(1, 'fnProgress'),(1, 'ProgressInvokeSetting'),(1, 'Args'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TreeResetNamedSecurityInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head),win32more.Foundation.BOOL,win32more.Security.Authorization.FN_PROGRESS,win32more.Security.Authorization.PROG_INVOKE_SETTING,c_void_p, use_last_error=False)(("TreeResetNamedSecurityInfoW", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'pOwner'),(1, 'pGroup'),(1, 'pDacl'),(1, 'pSacl'),(1, 'KeepExplicit'),(1, 'fnProgress'),(1, 'ProgressInvokeSetting'),(1, 'Args'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TreeResetNamedSecurityInfo():
    return win32more.Security.Authorization.TreeResetNamedSecurityInfoW
def _define_TreeSetNamedSecurityInfoA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head),win32more.Security.Authorization.TREE_SEC_INFO,win32more.Security.Authorization.FN_PROGRESS,win32more.Security.Authorization.PROG_INVOKE_SETTING,c_void_p, use_last_error=False)(("TreeSetNamedSecurityInfoA", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'pOwner'),(1, 'pGroup'),(1, 'pDacl'),(1, 'pSacl'),(1, 'dwAction'),(1, 'fnProgress'),(1, 'ProgressInvokeSetting'),(1, 'Args'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TreeSetNamedSecurityInfoW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Security.Authorization.SE_OBJECT_TYPE,UInt32,win32more.Foundation.PSID,win32more.Foundation.PSID,POINTER(win32more.Security.ACL_head),POINTER(win32more.Security.ACL_head),win32more.Security.Authorization.TREE_SEC_INFO,win32more.Security.Authorization.FN_PROGRESS,win32more.Security.Authorization.PROG_INVOKE_SETTING,c_void_p, use_last_error=False)(("TreeSetNamedSecurityInfoW", windll["ADVAPI32"]), ((1, 'pObjectName'),(1, 'ObjectType'),(1, 'SecurityInfo'),(1, 'pOwner'),(1, 'pGroup'),(1, 'pDacl'),(1, 'pSacl'),(1, 'dwAction'),(1, 'fnProgress'),(1, 'ProgressInvokeSetting'),(1, 'Args'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TreeSetNamedSecurityInfo():
    return win32more.Security.Authorization.TreeSetNamedSecurityInfoW
def _define_BuildSecurityDescriptorA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(win32more.Security.Authorization.TRUSTEE_A_head),UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A),UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=False)(("BuildSecurityDescriptorA", windll["ADVAPI32"]), ((1, 'pOwner'),(1, 'pGroup'),(1, 'cCountOfAccessEntries'),(1, 'pListOfAccessEntries'),(1, 'cCountOfAuditEntries'),(1, 'pListOfAuditEntries'),(1, 'pOldSD'),(1, 'pSizeNewSD'),(1, 'pNewSD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildSecurityDescriptorW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(win32more.Security.Authorization.TRUSTEE_W_head),UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W),UInt32,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(UInt32),POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)), use_last_error=False)(("BuildSecurityDescriptorW", windll["ADVAPI32"]), ((1, 'pOwner'),(1, 'pGroup'),(1, 'cCountOfAccessEntries'),(1, 'pListOfAccessEntries'),(1, 'cCountOfAuditEntries'),(1, 'pListOfAuditEntries'),(1, 'pOldSD'),(1, 'pSizeNewSD'),(1, 'pNewSD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildSecurityDescriptor():
    return win32more.Security.Authorization.BuildSecurityDescriptorW
def _define_LookupSecurityDescriptorPartsA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Security.Authorization.TRUSTEE_A_head)),POINTER(POINTER(win32more.Security.Authorization.TRUSTEE_A_head)),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A_head)),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A_head)),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("LookupSecurityDescriptorPartsA", windll["ADVAPI32"]), ((1, 'ppOwner'),(1, 'ppGroup'),(1, 'pcCountOfAccessEntries'),(1, 'ppListOfAccessEntries'),(1, 'pcCountOfAuditEntries'),(1, 'ppListOfAuditEntries'),(1, 'pSD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupSecurityDescriptorPartsW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(POINTER(win32more.Security.Authorization.TRUSTEE_W_head)),POINTER(POINTER(win32more.Security.Authorization.TRUSTEE_W_head)),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W_head)),POINTER(UInt32),POINTER(POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W_head)),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(("LookupSecurityDescriptorPartsW", windll["ADVAPI32"]), ((1, 'ppOwner'),(1, 'ppGroup'),(1, 'pcCountOfAccessEntries'),(1, 'ppListOfAccessEntries'),(1, 'pcCountOfAuditEntries'),(1, 'ppListOfAuditEntries'),(1, 'pSD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LookupSecurityDescriptorParts():
    return win32more.Security.Authorization.LookupSecurityDescriptorPartsW
def _define_BuildExplicitAccessWithNameA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A_head),win32more.Foundation.PSTR,UInt32,win32more.Security.Authorization.ACCESS_MODE,win32more.Security.ACE_FLAGS, use_last_error=False)(("BuildExplicitAccessWithNameA", windll["ADVAPI32"]), ((1, 'pExplicitAccess'),(1, 'pTrusteeName'),(1, 'AccessPermissions'),(1, 'AccessMode'),(1, 'Inheritance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildExplicitAccessWithNameW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W_head),win32more.Foundation.PWSTR,UInt32,win32more.Security.Authorization.ACCESS_MODE,win32more.Security.ACE_FLAGS, use_last_error=False)(("BuildExplicitAccessWithNameW", windll["ADVAPI32"]), ((1, 'pExplicitAccess'),(1, 'pTrusteeName'),(1, 'AccessPermissions'),(1, 'AccessMode'),(1, 'Inheritance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildExplicitAccessWithName():
    return win32more.Security.Authorization.BuildExplicitAccessWithNameW
def _define_BuildImpersonateExplicitAccessWithNameA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_A_head),win32more.Foundation.PSTR,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),UInt32,win32more.Security.Authorization.ACCESS_MODE,UInt32, use_last_error=False)(("BuildImpersonateExplicitAccessWithNameA", windll["ADVAPI32"]), ((1, 'pExplicitAccess'),(1, 'pTrusteeName'),(1, 'pTrustee'),(1, 'AccessPermissions'),(1, 'AccessMode'),(1, 'Inheritance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildImpersonateExplicitAccessWithNameW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.EXPLICIT_ACCESS_W_head),win32more.Foundation.PWSTR,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),UInt32,win32more.Security.Authorization.ACCESS_MODE,UInt32, use_last_error=False)(("BuildImpersonateExplicitAccessWithNameW", windll["ADVAPI32"]), ((1, 'pExplicitAccess'),(1, 'pTrusteeName'),(1, 'pTrustee'),(1, 'AccessPermissions'),(1, 'AccessMode'),(1, 'Inheritance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildImpersonateExplicitAccessWithName():
    return win32more.Security.Authorization.BuildImpersonateExplicitAccessWithNameW
def _define_BuildTrusteeWithNameA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),win32more.Foundation.PSTR, use_last_error=False)(("BuildTrusteeWithNameA", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithNameW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),win32more.Foundation.PWSTR, use_last_error=False)(("BuildTrusteeWithNameW", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithName():
    return win32more.Security.Authorization.BuildTrusteeWithNameW
def _define_BuildImpersonateTrusteeA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("BuildImpersonateTrusteeA", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pImpersonateTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildImpersonateTrusteeW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("BuildImpersonateTrusteeW", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pImpersonateTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildImpersonateTrustee():
    return win32more.Security.Authorization.BuildImpersonateTrusteeW
def _define_BuildTrusteeWithSidA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),win32more.Foundation.PSID, use_last_error=False)(("BuildTrusteeWithSidA", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithSidW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),win32more.Foundation.PSID, use_last_error=False)(("BuildTrusteeWithSidW", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithSid():
    return win32more.Security.Authorization.BuildTrusteeWithSidW
def _define_BuildTrusteeWithObjectsAndSidA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(win32more.Security.Authorization.OBJECTS_AND_SID_head),POINTER(Guid),POINTER(Guid),win32more.Foundation.PSID, use_last_error=False)(("BuildTrusteeWithObjectsAndSidA", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pObjSid'),(1, 'pObjectGuid'),(1, 'pInheritedObjectGuid'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithObjectsAndSidW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(win32more.Security.Authorization.OBJECTS_AND_SID_head),POINTER(Guid),POINTER(Guid),win32more.Foundation.PSID, use_last_error=False)(("BuildTrusteeWithObjectsAndSidW", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pObjSid'),(1, 'pObjectGuid'),(1, 'pInheritedObjectGuid'),(1, 'pSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithObjectsAndSid():
    return win32more.Security.Authorization.BuildTrusteeWithObjectsAndSidW
def _define_BuildTrusteeWithObjectsAndNameA():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(win32more.Security.Authorization.OBJECTS_AND_NAME_A_head),win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("BuildTrusteeWithObjectsAndNameA", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pObjName'),(1, 'ObjectType'),(1, 'ObjectTypeName'),(1, 'InheritedObjectTypeName'),(1, 'Name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithObjectsAndNameW():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(win32more.Security.Authorization.OBJECTS_AND_NAME_W_head),win32more.Security.Authorization.SE_OBJECT_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("BuildTrusteeWithObjectsAndNameW", windll["ADVAPI32"]), ((1, 'pTrustee'),(1, 'pObjName'),(1, 'ObjectType'),(1, 'ObjectTypeName'),(1, 'InheritedObjectTypeName'),(1, 'Name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildTrusteeWithObjectsAndName():
    return win32more.Security.Authorization.BuildTrusteeWithObjectsAndNameW
def _define_GetTrusteeNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("GetTrusteeNameA", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("GetTrusteeNameW", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeName():
    return win32more.Security.Authorization.GetTrusteeNameW
def _define_GetTrusteeTypeA():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.TRUSTEE_TYPE,POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("GetTrusteeTypeA", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeTypeW():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.TRUSTEE_TYPE,POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("GetTrusteeTypeW", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeType():
    return win32more.Security.Authorization.GetTrusteeTypeW
def _define_GetTrusteeFormA():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.TRUSTEE_FORM,POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("GetTrusteeFormA", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeFormW():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.TRUSTEE_FORM,POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("GetTrusteeFormW", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTrusteeForm():
    return win32more.Security.Authorization.GetTrusteeFormW
def _define_GetMultipleTrusteeOperationA():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION,POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("GetMultipleTrusteeOperationA", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMultipleTrusteeOperationW():
    try:
        return WINFUNCTYPE(win32more.Security.Authorization.MULTIPLE_TRUSTEE_OPERATION,POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("GetMultipleTrusteeOperationW", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMultipleTrusteeOperation():
    return win32more.Security.Authorization.GetMultipleTrusteeOperationW
def _define_GetMultipleTrusteeA():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Authorization.TRUSTEE_A_head),POINTER(win32more.Security.Authorization.TRUSTEE_A_head), use_last_error=False)(("GetMultipleTrusteeA", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMultipleTrusteeW():
    try:
        return WINFUNCTYPE(POINTER(win32more.Security.Authorization.TRUSTEE_W_head),POINTER(win32more.Security.Authorization.TRUSTEE_W_head), use_last_error=False)(("GetMultipleTrusteeW", windll["ADVAPI32"]), ((1, 'pTrustee'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMultipleTrustee():
    return win32more.Security.Authorization.GetMultipleTrusteeW
def _define_ConvertSidToStringSidA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,POINTER(win32more.Foundation.PSTR), use_last_error=True)(("ConvertSidToStringSidA", windll["ADVAPI32"]), ((1, 'Sid'),(1, 'StringSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertSidToStringSidW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSID,POINTER(win32more.Foundation.PWSTR), use_last_error=True)(("ConvertSidToStringSidW", windll["ADVAPI32"]), ((1, 'Sid'),(1, 'StringSid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertSidToStringSid():
    return win32more.Security.Authorization.ConvertSidToStringSidW
def _define_ConvertStringSidToSidA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSID), use_last_error=True)(("ConvertStringSidToSidA", windll["ADVAPI32"]), ((1, 'StringSid'),(1, 'Sid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertStringSidToSidW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PSID), use_last_error=True)(("ConvertStringSidToSidW", windll["ADVAPI32"]), ((1, 'StringSid'),(1, 'Sid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertStringSidToSid():
    return win32more.Security.Authorization.ConvertStringSidToSidW
def _define_ConvertStringSecurityDescriptorToSecurityDescriptorA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=True)(("ConvertStringSecurityDescriptorToSecurityDescriptorA", windll["ADVAPI32"]), ((1, 'StringSecurityDescriptor'),(1, 'StringSDRevision'),(1, 'SecurityDescriptor'),(1, 'SecurityDescriptorSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertStringSecurityDescriptorToSecurityDescriptorW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),POINTER(UInt32), use_last_error=True)(("ConvertStringSecurityDescriptorToSecurityDescriptorW", windll["ADVAPI32"]), ((1, 'StringSecurityDescriptor'),(1, 'StringSDRevision'),(1, 'SecurityDescriptor'),(1, 'SecurityDescriptorSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertStringSecurityDescriptorToSecurityDescriptor():
    return win32more.Security.Authorization.ConvertStringSecurityDescriptorToSecurityDescriptorW
def _define_ConvertSecurityDescriptorToStringSecurityDescriptorA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,UInt32,POINTER(win32more.Foundation.PSTR),POINTER(UInt32), use_last_error=True)(("ConvertSecurityDescriptorToStringSecurityDescriptorA", windll["ADVAPI32"]), ((1, 'SecurityDescriptor'),(1, 'RequestedStringSDRevision'),(1, 'SecurityInformation'),(1, 'StringSecurityDescriptor'),(1, 'StringSecurityDescriptorLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertSecurityDescriptorToStringSecurityDescriptorW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=True)(("ConvertSecurityDescriptorToStringSecurityDescriptorW", windll["ADVAPI32"]), ((1, 'SecurityDescriptor'),(1, 'RequestedStringSDRevision'),(1, 'SecurityInformation'),(1, 'StringSecurityDescriptor'),(1, 'StringSecurityDescriptorLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertSecurityDescriptorToStringSecurityDescriptor():
    return win32more.Security.Authorization.ConvertSecurityDescriptorToStringSecurityDescriptorW
__all__ = [
    "SDDL_REVISION_1",
    "SDDL_REVISION",
    "SDDL_ALIAS_SIZE",
    "INHERITED_ACCESS_ENTRY",
    "INHERITED_PARENT",
    "INHERITED_GRANDPARENT",
    "TRUSTEE_ACCESS_ALLOWED",
    "TRUSTEE_ACCESS_READ",
    "TRUSTEE_ACCESS_WRITE",
    "TRUSTEE_ACCESS_EXPLICIT",
    "TRUSTEE_ACCESS_ALL",
    "ACTRL_RESERVED",
    "ACTRL_PERM_1",
    "ACTRL_PERM_2",
    "ACTRL_PERM_3",
    "ACTRL_PERM_4",
    "ACTRL_PERM_5",
    "ACTRL_PERM_6",
    "ACTRL_PERM_7",
    "ACTRL_PERM_8",
    "ACTRL_PERM_9",
    "ACTRL_PERM_10",
    "ACTRL_PERM_11",
    "ACTRL_PERM_12",
    "ACTRL_PERM_13",
    "ACTRL_PERM_14",
    "ACTRL_PERM_15",
    "ACTRL_PERM_16",
    "ACTRL_PERM_17",
    "ACTRL_PERM_18",
    "ACTRL_PERM_19",
    "ACTRL_PERM_20",
    "ACTRL_ACCESS_PROTECTED",
    "ACTRL_SYSTEM_ACCESS",
    "ACTRL_DELETE",
    "ACTRL_READ_CONTROL",
    "ACTRL_CHANGE_ACCESS",
    "ACTRL_CHANGE_OWNER",
    "ACTRL_SYNCHRONIZE",
    "ACTRL_STD_RIGHTS_ALL",
    "ACTRL_FILE_READ",
    "ACTRL_FILE_WRITE",
    "ACTRL_FILE_APPEND",
    "ACTRL_FILE_READ_PROP",
    "ACTRL_FILE_WRITE_PROP",
    "ACTRL_FILE_EXECUTE",
    "ACTRL_FILE_READ_ATTRIB",
    "ACTRL_FILE_WRITE_ATTRIB",
    "ACTRL_FILE_CREATE_PIPE",
    "ACTRL_DIR_LIST",
    "ACTRL_DIR_CREATE_OBJECT",
    "ACTRL_DIR_CREATE_CHILD",
    "ACTRL_DIR_DELETE_CHILD",
    "ACTRL_DIR_TRAVERSE",
    "ACTRL_KERNEL_TERMINATE",
    "ACTRL_KERNEL_THREAD",
    "ACTRL_KERNEL_VM",
    "ACTRL_KERNEL_VM_READ",
    "ACTRL_KERNEL_VM_WRITE",
    "ACTRL_KERNEL_DUP_HANDLE",
    "ACTRL_KERNEL_PROCESS",
    "ACTRL_KERNEL_SET_INFO",
    "ACTRL_KERNEL_GET_INFO",
    "ACTRL_KERNEL_CONTROL",
    "ACTRL_KERNEL_ALERT",
    "ACTRL_KERNEL_GET_CONTEXT",
    "ACTRL_KERNEL_SET_CONTEXT",
    "ACTRL_KERNEL_TOKEN",
    "ACTRL_KERNEL_IMPERSONATE",
    "ACTRL_KERNEL_DIMPERSONATE",
    "ACTRL_PRINT_SADMIN",
    "ACTRL_PRINT_SLIST",
    "ACTRL_PRINT_PADMIN",
    "ACTRL_PRINT_PUSE",
    "ACTRL_PRINT_JADMIN",
    "ACTRL_SVC_GET_INFO",
    "ACTRL_SVC_SET_INFO",
    "ACTRL_SVC_STATUS",
    "ACTRL_SVC_LIST",
    "ACTRL_SVC_START",
    "ACTRL_SVC_STOP",
    "ACTRL_SVC_PAUSE",
    "ACTRL_SVC_INTERROGATE",
    "ACTRL_SVC_UCONTROL",
    "ACTRL_REG_QUERY",
    "ACTRL_REG_SET",
    "ACTRL_REG_CREATE_CHILD",
    "ACTRL_REG_LIST",
    "ACTRL_REG_NOTIFY",
    "ACTRL_REG_LINK",
    "ACTRL_WIN_CLIPBRD",
    "ACTRL_WIN_GLOBAL_ATOMS",
    "ACTRL_WIN_CREATE",
    "ACTRL_WIN_LIST_DESK",
    "ACTRL_WIN_LIST",
    "ACTRL_WIN_READ_ATTRIBS",
    "ACTRL_WIN_WRITE_ATTRIBS",
    "ACTRL_WIN_SCREEN",
    "ACTRL_WIN_EXIT",
    "ACTRL_ACCESS_NO_OPTIONS",
    "ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES",
    "AUDIT_TYPE_LEGACY",
    "AUDIT_TYPE_WMI",
    "AP_ParamTypeBits",
    "AP_ParamTypeMask",
    "_AUTHZ_SS_MAXSIZE",
    "APF_AuditFailure",
    "APF_AuditSuccess",
    "APF_ValidFlags",
    "AUTHZP_WPD_EVENT",
    "AUTHZ_ALLOW_MULTIPLE_SOURCE_INSTANCES",
    "AUTHZ_MIGRATED_LEGACY_PUBLISHER",
    "AUTHZ_AUDIT_INSTANCE_INFORMATION",
    "AUTHZ_SKIP_TOKEN_GROUPS",
    "AUTHZ_REQUIRE_S4U_LOGON",
    "AUTHZ_COMPUTE_PRIVILEGES",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_INVALID",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_INT64",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_UINT64",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_STRING",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_FQBN",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_SID",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_BOOLEAN",
    "AUTHZ_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING",
    "AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION_V1",
    "AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_VERSION",
    "AUTHZ_RPC_INIT_INFO_CLIENT_VERSION_V1",
    "AUTHZ_INIT_INFO_VERSION_V1",
    "AUTHZ_WPD_CATEGORY_FLAG",
    "AUTHZ_FLAG_ALLOW_MULTIPLE_SOURCE_INSTANCES",
    "OLESCRIPT_E_SYNTAX",
    "AUTHZ_RESOURCE_MANAGER_FLAGS",
    "AUTHZ_RM_FLAG_NO_AUDIT",
    "AUTHZ_RM_FLAG_INITIALIZE_UNDER_IMPERSONATION",
    "AUTHZ_RM_FLAG_NO_CENTRAL_ACCESS_POLICIES",
    "AUTHZ_ACCESS_CHECK_FLAGS",
    "AUTHZ_ACCESS_CHECK_NO_DEEP_COPY_SD",
    "AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS",
    "AUTHZ_NO_SUCCESS_AUDIT",
    "AUTHZ_NO_FAILURE_AUDIT",
    "AUTHZ_NO_ALLOC_STRINGS",
    "TREE_SEC_INFO",
    "TREE_SEC_INFO_SET",
    "TREE_SEC_INFO_RESET",
    "TREE_SEC_INFO_RESET_KEEP_EXPLICIT",
    "AUTHZ_GENERATE_RESULTS",
    "AUTHZ_GENERATE_SUCCESS_AUDIT",
    "AUTHZ_GENERATE_FAILURE_AUDIT",
    "ACTRL_ACCESS_ENTRY_ACCESS_FLAGS",
    "ACTRL_ACCESS_ALLOWED",
    "ACTRL_ACCESS_DENIED",
    "ACTRL_AUDIT_SUCCESS",
    "ACTRL_AUDIT_FAILURE",
    "AUTHZ_SECURITY_ATTRIBUTE_FLAGS",
    "AUTHZ_SECURITY_ATTRIBUTE_NON_INHERITABLE",
    "AUTHZ_SECURITY_ATTRIBUTE_VALUE_CASE_SENSITIVE",
    "SE_OBJECT_TYPE",
    "SE_UNKNOWN_OBJECT_TYPE",
    "SE_FILE_OBJECT",
    "SE_SERVICE",
    "SE_PRINTER",
    "SE_REGISTRY_KEY",
    "SE_LMSHARE",
    "SE_KERNEL_OBJECT",
    "SE_WINDOW_OBJECT",
    "SE_DS_OBJECT",
    "SE_DS_OBJECT_ALL",
    "SE_PROVIDER_DEFINED_OBJECT",
    "SE_WMIGUID_OBJECT",
    "SE_REGISTRY_WOW64_32KEY",
    "SE_REGISTRY_WOW64_64KEY",
    "TRUSTEE_TYPE",
    "TRUSTEE_IS_UNKNOWN",
    "TRUSTEE_IS_USER",
    "TRUSTEE_IS_GROUP",
    "TRUSTEE_IS_DOMAIN",
    "TRUSTEE_IS_ALIAS",
    "TRUSTEE_IS_WELL_KNOWN_GROUP",
    "TRUSTEE_IS_DELETED",
    "TRUSTEE_IS_INVALID",
    "TRUSTEE_IS_COMPUTER",
    "TRUSTEE_FORM",
    "TRUSTEE_IS_SID",
    "TRUSTEE_IS_NAME",
    "TRUSTEE_BAD_FORM",
    "TRUSTEE_IS_OBJECTS_AND_SID",
    "TRUSTEE_IS_OBJECTS_AND_NAME",
    "MULTIPLE_TRUSTEE_OPERATION",
    "NO_MULTIPLE_TRUSTEE",
    "TRUSTEE_IS_IMPERSONATE",
    "OBJECTS_AND_SID",
    "OBJECTS_AND_NAME_A",
    "OBJECTS_AND_NAME_W",
    "TRUSTEE_A",
    "TRUSTEE_W",
    "ACCESS_MODE",
    "NOT_USED_ACCESS",
    "GRANT_ACCESS",
    "SET_ACCESS",
    "DENY_ACCESS",
    "REVOKE_ACCESS",
    "SET_AUDIT_SUCCESS",
    "SET_AUDIT_FAILURE",
    "EXPLICIT_ACCESS_A",
    "EXPLICIT_ACCESS_W",
    "ACTRL_ACCESS_ENTRYA",
    "ACTRL_ACCESS_ENTRYW",
    "ACTRL_ACCESS_ENTRY_LISTA",
    "ACTRL_ACCESS_ENTRY_LISTW",
    "ACTRL_PROPERTY_ENTRYA",
    "ACTRL_PROPERTY_ENTRYW",
    "ACTRL_ACCESSA",
    "ACTRL_ACCESSW",
    "TRUSTEE_ACCESSA",
    "TRUSTEE_ACCESSW",
    "ACTRL_OVERLAPPED",
    "ACTRL_ACCESS_INFOA",
    "ACTRL_ACCESS_INFOW",
    "ACTRL_CONTROL_INFOA",
    "ACTRL_CONTROL_INFOW",
    "PROG_INVOKE_SETTING",
    "PROG_INVOKE_SETTING_ProgressInvokeNever",
    "PROG_INVOKE_SETTING_ProgressInvokeEveryObject",
    "PROG_INVOKE_SETTING_ProgressInvokeOnError",
    "PROG_INVOKE_SETTING_ProgressCancelOperation",
    "PROG_INVOKE_SETTING_ProgressRetryOperation",
    "PROG_INVOKE_SETTING_ProgressInvokePrePostError",
    "FN_OBJECT_MGR_FUNCTIONS",
    "INHERITED_FROMA",
    "INHERITED_FROMW",
    "AUDIT_PARAM_TYPE",
    "APT_None",
    "APT_String",
    "APT_Ulong",
    "APT_Pointer",
    "APT_Sid",
    "APT_LogonId",
    "APT_ObjectTypeList",
    "APT_Luid",
    "APT_Guid",
    "APT_Time",
    "APT_Int64",
    "APT_IpAddress",
    "APT_LogonIdWithSid",
    "AUDIT_OBJECT_TYPE",
    "AUDIT_OBJECT_TYPES",
    "AUDIT_IP_ADDRESS",
    "AUDIT_PARAM",
    "AUDIT_PARAMS",
    "AUTHZ_AUDIT_EVENT_TYPE_LEGACY",
    "AUTHZ_AUDIT_EVENT_TYPE_UNION",
    "AUTHZ_AUDIT_EVENT_TYPE_OLD",
    "AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__",
    "AUTHZ_ACCESS_REQUEST",
    "AUTHZ_ACCESS_REPLY",
    "PFN_AUTHZ_DYNAMIC_ACCESS_CHECK",
    "PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS",
    "PFN_AUTHZ_FREE_DYNAMIC_GROUPS",
    "PFN_AUTHZ_GET_CENTRAL_ACCESS_POLICY",
    "PFN_AUTHZ_FREE_CENTRAL_ACCESS_POLICY",
    "AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE",
    "AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE",
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE",
    "AUTHZ_SID_OPERATION",
    "AUTHZ_SID_OPERATION_NONE",
    "AUTHZ_SID_OPERATION_REPLACE_ALL",
    "AUTHZ_SID_OPERATION_ADD",
    "AUTHZ_SID_OPERATION_DELETE",
    "AUTHZ_SID_OPERATION_REPLACE",
    "AUTHZ_SECURITY_ATTRIBUTE_V1",
    "AUTHZ_SECURITY_ATTRIBUTES_INFORMATION",
    "AUTHZ_RPC_INIT_INFO_CLIENT",
    "AUTHZ_INIT_INFO",
    "AUTHZ_CONTEXT_INFORMATION_CLASS",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserSid",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoGroupsSids",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoRestrictedSids",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoPrivileges",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoExpirationTime",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoServerContext",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoIdentifier",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSource",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAll",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAuthenticationId",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoSecurityAttributes",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceSids",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoUserClaims",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoDeviceClaims",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoAppContainerSid",
    "AUTHZ_CONTEXT_INFORMATION_CLASS_AuthzContextInfoCapabilitySids",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoFlags",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoOperationType",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectType",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoObjectName",
    "AUTHZ_AUDIT_EVENT_INFORMATION_CLASS_AuthzAuditEventInfoAdditionalInfo",
    "AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET",
    "AUTHZ_SOURCE_SCHEMA_REGISTRATION",
    "AzAuthorizationStore",
    "AzBizRuleContext",
    "AzPrincipalLocator",
    "IAzAuthorizationStore",
    "IAzAuthorizationStore2",
    "IAzAuthorizationStore3",
    "IAzApplication",
    "IAzApplication2",
    "IAzApplications",
    "IAzOperation",
    "IAzOperations",
    "IAzTask",
    "IAzTasks",
    "IAzScope",
    "IAzScopes",
    "IAzApplicationGroup",
    "IAzApplicationGroups",
    "IAzRole",
    "IAzRoles",
    "IAzClientContext",
    "IAzClientContext2",
    "IAzBizRuleContext",
    "IAzBizRuleParameters",
    "IAzBizRuleInterfaces",
    "IAzClientContext3",
    "IAzScope2",
    "IAzApplication3",
    "IAzOperation2",
    "IAzRoleDefinitions",
    "IAzRoleDefinition",
    "IAzRoleAssignment",
    "IAzRoleAssignments",
    "IAzPrincipalLocator",
    "IAzNameResolver",
    "IAzObjectPicker",
    "IAzApplicationGroup2",
    "IAzTask2",
    "AZ_PROP_CONSTANTS",
    "AZ_PROP_NAME",
    "AZ_PROP_DESCRIPTION",
    "AZ_PROP_WRITABLE",
    "AZ_PROP_APPLICATION_DATA",
    "AZ_PROP_CHILD_CREATE",
    "AZ_MAX_APPLICATION_NAME_LENGTH",
    "AZ_MAX_OPERATION_NAME_LENGTH",
    "AZ_MAX_TASK_NAME_LENGTH",
    "AZ_MAX_SCOPE_NAME_LENGTH",
    "AZ_MAX_GROUP_NAME_LENGTH",
    "AZ_MAX_ROLE_NAME_LENGTH",
    "AZ_MAX_NAME_LENGTH",
    "AZ_MAX_DESCRIPTION_LENGTH",
    "AZ_MAX_APPLICATION_DATA_LENGTH",
    "AZ_SUBMIT_FLAG_ABORT",
    "AZ_SUBMIT_FLAG_FLUSH",
    "AZ_MAX_POLICY_URL_LENGTH",
    "AZ_AZSTORE_FLAG_CREATE",
    "AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY",
    "AZ_AZSTORE_FLAG_BATCH_UPDATE",
    "AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL",
    "AZ_AZSTORE_FORCE_APPLICATION_CLOSE",
    "AZ_AZSTORE_NT6_FUNCTION_LEVEL",
    "AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT",
    "AZ_PROP_AZSTORE_DOMAIN_TIMEOUT",
    "AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT",
    "AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT",
    "AZ_AZSTORE_MIN_DOMAIN_TIMEOUT",
    "AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT",
    "AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT",
    "AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES",
    "AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES",
    "AZ_PROP_AZSTORE_MAJOR_VERSION",
    "AZ_PROP_AZSTORE_MINOR_VERSION",
    "AZ_PROP_AZSTORE_TARGET_MACHINE",
    "AZ_PROP_AZTORE_IS_ADAM_INSTANCE",
    "AZ_PROP_OPERATION_ID",
    "AZ_PROP_TASK_OPERATIONS",
    "AZ_PROP_TASK_BIZRULE",
    "AZ_PROP_TASK_BIZRULE_LANGUAGE",
    "AZ_PROP_TASK_TASKS",
    "AZ_PROP_TASK_BIZRULE_IMPORTED_PATH",
    "AZ_PROP_TASK_IS_ROLE_DEFINITION",
    "AZ_MAX_TASK_BIZRULE_LENGTH",
    "AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH",
    "AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH",
    "AZ_MAX_BIZRULE_STRING",
    "AZ_PROP_GROUP_TYPE",
    "AZ_GROUPTYPE_LDAP_QUERY",
    "AZ_GROUPTYPE_BASIC",
    "AZ_GROUPTYPE_BIZRULE",
    "AZ_PROP_GROUP_APP_MEMBERS",
    "AZ_PROP_GROUP_APP_NON_MEMBERS",
    "AZ_PROP_GROUP_LDAP_QUERY",
    "AZ_MAX_GROUP_LDAP_QUERY_LENGTH",
    "AZ_PROP_GROUP_MEMBERS",
    "AZ_PROP_GROUP_NON_MEMBERS",
    "AZ_PROP_GROUP_MEMBERS_NAME",
    "AZ_PROP_GROUP_NON_MEMBERS_NAME",
    "AZ_PROP_GROUP_BIZRULE",
    "AZ_PROP_GROUP_BIZRULE_LANGUAGE",
    "AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH",
    "AZ_MAX_GROUP_BIZRULE_LENGTH",
    "AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH",
    "AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH",
    "AZ_PROP_ROLE_APP_MEMBERS",
    "AZ_PROP_ROLE_MEMBERS",
    "AZ_PROP_ROLE_OPERATIONS",
    "AZ_PROP_ROLE_TASKS",
    "AZ_PROP_ROLE_MEMBERS_NAME",
    "AZ_PROP_SCOPE_BIZRULES_WRITABLE",
    "AZ_PROP_SCOPE_CAN_BE_DELEGATED",
    "AZ_PROP_CLIENT_CONTEXT_USER_DN",
    "AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT",
    "AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY",
    "AZ_PROP_CLIENT_CONTEXT_USER_GUID",
    "AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL",
    "AZ_PROP_CLIENT_CONTEXT_USER_UPN",
    "AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT",
    "AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK",
    "AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN",
    "AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID",
    "AZ_PROP_APPLICATION_VERSION",
    "AZ_MAX_APPLICATION_VERSION_LENGTH",
    "AZ_PROP_APPLICATION_NAME",
    "AZ_PROP_APPLICATION_BIZRULE_ENABLED",
    "AZ_PROP_APPLY_STORE_SACL",
    "AZ_PROP_GENERATE_AUDITS",
    "AZ_PROP_POLICY_ADMINS",
    "AZ_PROP_POLICY_READERS",
    "AZ_PROP_DELEGATED_POLICY_USERS",
    "AZ_PROP_POLICY_ADMINS_NAME",
    "AZ_PROP_POLICY_READERS_NAME",
    "AZ_PROP_DELEGATED_POLICY_USERS_NAME",
    "AZ_CLIENT_CONTEXT_SKIP_GROUP",
    "AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY",
    "AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE",
    "AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY",
    "FN_PROGRESS",
    "AUTHZ_ACCESS_CHECK_RESULTS_HANDLE",
    "AUTHZ_CLIENT_CONTEXT_HANDLE",
    "AUTHZ_RESOURCE_MANAGER_HANDLE",
    "AUTHZ_AUDIT_EVENT_HANDLE",
    "AUTHZ_AUDIT_EVENT_TYPE_HANDLE",
    "AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE",
    "AuthzAccessCheck",
    "AuthzCachedAccessCheck",
    "AuthzOpenObjectAudit",
    "AuthzFreeHandle",
    "AuthzInitializeResourceManager",
    "AuthzInitializeResourceManagerEx",
    "AuthzInitializeRemoteResourceManager",
    "AuthzFreeResourceManager",
    "AuthzInitializeContextFromToken",
    "AuthzInitializeContextFromSid",
    "AuthzInitializeContextFromAuthzContext",
    "AuthzInitializeCompoundContext",
    "AuthzAddSidsToContext",
    "AuthzModifySecurityAttributes",
    "AuthzModifyClaims",
    "AuthzModifySids",
    "AuthzSetAppContainerInformation",
    "AuthzGetInformationFromContext",
    "AuthzFreeContext",
    "AuthzInitializeObjectAccessAuditEvent",
    "AuthzInitializeObjectAccessAuditEvent2",
    "AuthzFreeAuditEvent",
    "AuthzEvaluateSacl",
    "AuthzInstallSecurityEventSource",
    "AuthzUninstallSecurityEventSource",
    "AuthzEnumerateSecurityEventSources",
    "AuthzRegisterSecurityEventSource",
    "AuthzUnregisterSecurityEventSource",
    "AuthzReportSecurityEvent",
    "AuthzReportSecurityEventFromParams",
    "AuthzRegisterCapChangeNotification",
    "AuthzUnregisterCapChangeNotification",
    "AuthzFreeCentralAccessPolicyCache",
    "SetEntriesInAclA",
    "SetEntriesInAclW",
    "SetEntriesInAcl",
    "GetExplicitEntriesFromAclA",
    "GetExplicitEntriesFromAclW",
    "GetExplicitEntriesFromAcl",
    "GetEffectiveRightsFromAclA",
    "GetEffectiveRightsFromAclW",
    "GetEffectiveRightsFromAcl",
    "GetAuditedPermissionsFromAclA",
    "GetAuditedPermissionsFromAclW",
    "GetAuditedPermissionsFromAcl",
    "GetNamedSecurityInfoA",
    "GetNamedSecurityInfoW",
    "GetNamedSecurityInfo",
    "GetSecurityInfo",
    "SetNamedSecurityInfoA",
    "SetNamedSecurityInfoW",
    "SetNamedSecurityInfo",
    "SetSecurityInfo",
    "GetInheritanceSourceA",
    "GetInheritanceSourceW",
    "GetInheritanceSource",
    "FreeInheritedFromArray",
    "TreeResetNamedSecurityInfoA",
    "TreeResetNamedSecurityInfoW",
    "TreeResetNamedSecurityInfo",
    "TreeSetNamedSecurityInfoA",
    "TreeSetNamedSecurityInfoW",
    "TreeSetNamedSecurityInfo",
    "BuildSecurityDescriptorA",
    "BuildSecurityDescriptorW",
    "BuildSecurityDescriptor",
    "LookupSecurityDescriptorPartsA",
    "LookupSecurityDescriptorPartsW",
    "LookupSecurityDescriptorParts",
    "BuildExplicitAccessWithNameA",
    "BuildExplicitAccessWithNameW",
    "BuildExplicitAccessWithName",
    "BuildImpersonateExplicitAccessWithNameA",
    "BuildImpersonateExplicitAccessWithNameW",
    "BuildImpersonateExplicitAccessWithName",
    "BuildTrusteeWithNameA",
    "BuildTrusteeWithNameW",
    "BuildTrusteeWithName",
    "BuildImpersonateTrusteeA",
    "BuildImpersonateTrusteeW",
    "BuildImpersonateTrustee",
    "BuildTrusteeWithSidA",
    "BuildTrusteeWithSidW",
    "BuildTrusteeWithSid",
    "BuildTrusteeWithObjectsAndSidA",
    "BuildTrusteeWithObjectsAndSidW",
    "BuildTrusteeWithObjectsAndSid",
    "BuildTrusteeWithObjectsAndNameA",
    "BuildTrusteeWithObjectsAndNameW",
    "BuildTrusteeWithObjectsAndName",
    "GetTrusteeNameA",
    "GetTrusteeNameW",
    "GetTrusteeName",
    "GetTrusteeTypeA",
    "GetTrusteeTypeW",
    "GetTrusteeType",
    "GetTrusteeFormA",
    "GetTrusteeFormW",
    "GetTrusteeForm",
    "GetMultipleTrusteeOperationA",
    "GetMultipleTrusteeOperationW",
    "GetMultipleTrusteeOperation",
    "GetMultipleTrusteeA",
    "GetMultipleTrusteeW",
    "GetMultipleTrustee",
    "ConvertSidToStringSidA",
    "ConvertSidToStringSidW",
    "ConvertSidToStringSid",
    "ConvertStringSidToSidA",
    "ConvertStringSidToSidW",
    "ConvertStringSidToSid",
    "ConvertStringSecurityDescriptorToSecurityDescriptorA",
    "ConvertStringSecurityDescriptorToSecurityDescriptorW",
    "ConvertStringSecurityDescriptorToSecurityDescriptor",
    "ConvertSecurityDescriptorToStringSecurityDescriptorA",
    "ConvertSecurityDescriptorToStringSecurityDescriptorW",
    "ConvertSecurityDescriptorToStringSecurityDescriptor",
]
