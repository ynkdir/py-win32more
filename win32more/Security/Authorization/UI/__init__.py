from win32more.base import *
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization
import win32more.Security.Authorization.UI
import win32more.System.Com
import win32more.UI.Controls

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
SI_EDIT_PERMS = 0
SI_EDIT_OWNER = 1
SI_CONTAINER = 4
SI_READONLY = 8
SI_RESET = 32
SI_OWNER_READONLY = 64
SI_OWNER_RECURSE = 256
SI_NO_ACL_PROTECT = 512
SI_NO_TREE_APPLY = 1024
SI_PAGE_TITLE = 2048
SI_SERVER_IS_DC = 4096
SI_RESET_DACL_TREE = 16384
SI_RESET_SACL_TREE = 32768
SI_OBJECT_GUID = 65536
SI_ACCESS_SPECIFIC = 65536
SI_ACCESS_GENERAL = 131072
SI_ACCESS_CONTAINER = 262144
SI_ACCESS_PROPERTY = 524288
DOBJ_RES_CONT = 1
DOBJ_RES_ROOT = 2
DOBJ_VOL_NTACLS = 4
DOBJ_COND_NTACLS = 8
DOBJ_RIBBON_LAUNCH = 16
SECURITY_OBJECT_ID_OBJECT_SD = 1
SECURITY_OBJECT_ID_SHARE = 2
SECURITY_OBJECT_ID_CENTRAL_POLICY = 3
SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE = 4
SECURITY_INFO_PAGE_FLAGS = UInt32
SI_ADVANCED = 16
SI_EDIT_AUDITS = 2
SI_EDIT_PROPERTIES = 128
SI_OBJECT_INFO_FLAGS = UInt32
SI_AUDITS_ELEVATION_REQUIRED = 33554432
SI_DISABLE_DENY_ACE = 2147483648
SI_EDIT_EFFECTIVE = 131072
SI_ENABLE_CENTRAL_POLICY = 1073741824
SI_ENABLE_EDIT_ATTRIBUTE_CONDITION = 536870912
SI_MAY_WRITE = 268435456
SI_NO_ADDITIONAL_PERMISSION = 2097152
SI_OWNER_ELEVATION_REQUIRED = 67108864
SI_PERMS_ELEVATION_REQUIRED = 16777216
SI_RESET_DACL = 262144
SI_RESET_OWNER = 1048576
SI_RESET_SACL = 524288
SI_SCOPE_ELEVATION_REQUIRED = 134217728
SI_VIEW_ONLY = 4194304
def _define_SI_OBJECT_INFO_head():
    class SI_OBJECT_INFO(Structure):
        pass
    return SI_OBJECT_INFO
def _define_SI_OBJECT_INFO():
    SI_OBJECT_INFO = win32more.Security.Authorization.UI.SI_OBJECT_INFO_head
    SI_OBJECT_INFO._fields_ = [
        ("dwFlags", win32more.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("pszServerName", win32more.Foundation.PWSTR),
        ("pszObjectName", win32more.Foundation.PWSTR),
        ("pszPageTitle", win32more.Foundation.PWSTR),
        ("guidObjectType", Guid),
    ]
    return SI_OBJECT_INFO
def _define_SI_ACCESS_head():
    class SI_ACCESS(Structure):
        pass
    return SI_ACCESS
def _define_SI_ACCESS():
    SI_ACCESS = win32more.Security.Authorization.UI.SI_ACCESS_head
    SI_ACCESS._fields_ = [
        ("pguid", POINTER(Guid)),
        ("mask", UInt32),
        ("pszName", win32more.Foundation.PWSTR),
        ("dwFlags", UInt32),
    ]
    return SI_ACCESS
def _define_SI_INHERIT_TYPE_head():
    class SI_INHERIT_TYPE(Structure):
        pass
    return SI_INHERIT_TYPE
def _define_SI_INHERIT_TYPE():
    SI_INHERIT_TYPE = win32more.Security.Authorization.UI.SI_INHERIT_TYPE_head
    SI_INHERIT_TYPE._fields_ = [
        ("pguid", POINTER(Guid)),
        ("dwFlags", win32more.Security.ACE_FLAGS),
        ("pszName", win32more.Foundation.PWSTR),
    ]
    return SI_INHERIT_TYPE
SI_PAGE_TYPE = Int32
SI_PAGE_PERM = 0
SI_PAGE_ADVPERM = 1
SI_PAGE_AUDIT = 2
SI_PAGE_OWNER = 3
SI_PAGE_EFFECTIVE = 4
SI_PAGE_TAKEOWNERSHIP = 5
SI_PAGE_SHARE = 6
SI_PAGE_ACTIVATED = Int32
SI_SHOW_DEFAULT = 0
SI_SHOW_PERM_ACTIVATED = 1
SI_SHOW_AUDIT_ACTIVATED = 2
SI_SHOW_OWNER_ACTIVATED = 3
SI_SHOW_EFFECTIVE_ACTIVATED = 4
SI_SHOW_SHARE_ACTIVATED = 5
SI_SHOW_CENTRAL_POLICY_ACTIVATED = 6
def _define_ISecurityInformation_head():
    class ISecurityInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('965fc360-16ff-11d0-91cb-00aa00bbb723')
    return ISecurityInformation
def _define_ISecurityInformation():
    ISecurityInformation = win32more.Security.Authorization.UI.ISecurityInformation_head
    ISecurityInformation.GetObjectInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authorization.UI.SI_OBJECT_INFO_head), use_last_error=False)(3, 'GetObjectInformation', ((1, 'pObjectInfo'),)))
    ISecurityInformation.GetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.OBJECT_SECURITY_INFORMATION,POINTER(POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),win32more.Foundation.BOOL, use_last_error=False)(4, 'GetSecurity', ((1, 'RequestedInformation'),(1, 'ppSecurityDescriptor'),(1, 'fDefault'),)))
    ISecurityInformation.SetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.OBJECT_SECURITY_INFORMATION,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=False)(5, 'SetSecurity', ((1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),)))
    ISecurityInformation.GetAccessRights = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS,POINTER(POINTER(win32more.Security.Authorization.UI.SI_ACCESS_head)),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetAccessRights', ((1, 'pguidObjectType'),(1, 'dwFlags'),(1, 'ppAccess'),(1, 'pcAccesses'),(1, 'piDefaultAccess'),)))
    ISecurityInformation.MapGeneric = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_char_p_no,POINTER(UInt32), use_last_error=False)(7, 'MapGeneric', ((1, 'pguidObjectType'),(1, 'pAceFlags'),(1, 'pMask'),)))
    ISecurityInformation.GetInheritTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Authorization.UI.SI_INHERIT_TYPE_head)),POINTER(UInt32), use_last_error=False)(8, 'GetInheritTypes', ((1, 'ppInheritTypes'),(1, 'pcInheritTypes'),)))
    ISecurityInformation.PropertySheetPageCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.Controls.PSPCB_MESSAGE,win32more.Security.Authorization.UI.SI_PAGE_TYPE, use_last_error=False)(9, 'PropertySheetPageCallback', ((1, 'hwnd'),(1, 'uMsg'),(1, 'uPage'),)))
    win32more.System.Com.IUnknown
    return ISecurityInformation
def _define_ISecurityInformation2_head():
    class ISecurityInformation2(win32more.System.Com.IUnknown_head):
        Guid = Guid('c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a')
    return ISecurityInformation2
def _define_ISecurityInformation2():
    ISecurityInformation2 = win32more.Security.Authorization.UI.ISecurityInformation2_head
    ISecurityInformation2.IsDaclCanonical = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.ACL_head), use_last_error=False)(3, 'IsDaclCanonical', ((1, 'pDacl'),)))
    ISecurityInformation2.LookupSids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PSID),POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(4, 'LookupSids', ((1, 'cSids'),(1, 'rgpSids'),(1, 'ppdo'),)))
    win32more.System.Com.IUnknown
    return ISecurityInformation2
def _define_SID_INFO_head():
    class SID_INFO(Structure):
        pass
    return SID_INFO
def _define_SID_INFO():
    SID_INFO = win32more.Security.Authorization.UI.SID_INFO_head
    SID_INFO._fields_ = [
        ("pSid", win32more.Foundation.PSID),
        ("pwzCommonName", win32more.Foundation.PWSTR),
        ("pwzClass", win32more.Foundation.PWSTR),
        ("pwzUPN", win32more.Foundation.PWSTR),
    ]
    return SID_INFO
def _define_SID_INFO_LIST_head():
    class SID_INFO_LIST(Structure):
        pass
    return SID_INFO_LIST
def _define_SID_INFO_LIST():
    SID_INFO_LIST = win32more.Security.Authorization.UI.SID_INFO_LIST_head
    SID_INFO_LIST._fields_ = [
        ("cItems", UInt32),
        ("aSidInfo", win32more.Security.Authorization.UI.SID_INFO * 0),
    ]
    return SID_INFO_LIST
def _define_IEffectivePermission_head():
    class IEffectivePermission(win32more.System.Com.IUnknown_head):
        Guid = Guid('3853dc76-9f35-407c-88a1-d19344365fbc')
    return IEffectivePermission
def _define_IEffectivePermission():
    IEffectivePermission = win32more.Security.Authorization.UI.IEffectivePermission_head
    IEffectivePermission.GetEffectivePermission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PSID,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(POINTER(win32more.Security.OBJECT_TYPE_LIST_head)),POINTER(UInt32),POINTER(POINTER(UInt32)),POINTER(UInt32), use_last_error=False)(3, 'GetEffectivePermission', ((1, 'pguidObjectType'),(1, 'pUserSid'),(1, 'pszServerName'),(1, 'pSD'),(1, 'ppObjectTypeList'),(1, 'pcObjectTypeListLength'),(1, 'ppGrantedAccessList'),(1, 'pcGrantedAccessListLength'),)))
    win32more.System.Com.IUnknown
    return IEffectivePermission
def _define_ISecurityObjectTypeInfo_head():
    class ISecurityObjectTypeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc3066eb-79ef-444b-9111-d18a75ebf2fa')
    return ISecurityObjectTypeInfo
def _define_ISecurityObjectTypeInfo():
    ISecurityObjectTypeInfo = win32more.Security.Authorization.UI.ISecurityObjectTypeInfo_head
    ISecurityObjectTypeInfo.GetInheritSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Security.ACL_head),POINTER(POINTER(win32more.Security.Authorization.INHERITED_FROMA_head)), use_last_error=False)(3, 'GetInheritSource', ((1, 'si'),(1, 'pACL'),(1, 'ppInheritArray'),)))
    win32more.System.Com.IUnknown
    return ISecurityObjectTypeInfo
def _define_ISecurityInformation3_head():
    class ISecurityInformation3(win32more.System.Com.IUnknown_head):
        Guid = Guid('e2cdc9cc-31bd-4f8f-8c8b-b641af516a1a')
    return ISecurityInformation3
def _define_ISecurityInformation3():
    ISecurityInformation3 = win32more.Security.Authorization.UI.ISecurityInformation3_head
    ISecurityInformation3.GetFullResourceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetFullResourceName', ((1, 'ppszResourceName'),)))
    ISecurityInformation3.OpenElevatedEditor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Security.Authorization.UI.SI_PAGE_TYPE, use_last_error=False)(4, 'OpenElevatedEditor', ((1, 'hWnd'),(1, 'uPage'),)))
    win32more.System.Com.IUnknown
    return ISecurityInformation3
def _define_SECURITY_OBJECT_head():
    class SECURITY_OBJECT(Structure):
        pass
    return SECURITY_OBJECT
def _define_SECURITY_OBJECT():
    SECURITY_OBJECT = win32more.Security.Authorization.UI.SECURITY_OBJECT_head
    SECURITY_OBJECT._fields_ = [
        ("pwszName", win32more.Foundation.PWSTR),
        ("pData", c_void_p),
        ("cbData", UInt32),
        ("pData2", c_void_p),
        ("cbData2", UInt32),
        ("Id", UInt32),
        ("fWellKnown", win32more.Foundation.BOOLEAN),
    ]
    return SECURITY_OBJECT
def _define_EFFPERM_RESULT_LIST_head():
    class EFFPERM_RESULT_LIST(Structure):
        pass
    return EFFPERM_RESULT_LIST
def _define_EFFPERM_RESULT_LIST():
    EFFPERM_RESULT_LIST = win32more.Security.Authorization.UI.EFFPERM_RESULT_LIST_head
    EFFPERM_RESULT_LIST._fields_ = [
        ("fEvaluated", win32more.Foundation.BOOLEAN),
        ("cObjectTypeListLength", UInt32),
        ("pObjectTypeList", POINTER(win32more.Security.OBJECT_TYPE_LIST_head)),
        ("pGrantedAccessList", POINTER(UInt32)),
    ]
    return EFFPERM_RESULT_LIST
def _define_ISecurityInformation4_head():
    class ISecurityInformation4(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea961070-cd14-4621-ace4-f63c03e583e4')
    return ISecurityInformation4
def _define_ISecurityInformation4():
    ISecurityInformation4 = win32more.Security.Authorization.UI.ISecurityInformation4_head
    ISecurityInformation4.GetSecondarySecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Authorization.UI.SECURITY_OBJECT_head)),POINTER(UInt32), use_last_error=False)(3, 'GetSecondarySecurity', ((1, 'pSecurityObjects'),(1, 'pSecurityObjectCount'),)))
    win32more.System.Com.IUnknown
    return ISecurityInformation4
def _define_IEffectivePermission2_head():
    class IEffectivePermission2(win32more.System.Com.IUnknown_head):
        Guid = Guid('941fabca-dd47-4fca-90bb-b0e10255f20d')
    return IEffectivePermission2
def _define_IEffectivePermission2():
    IEffectivePermission2 = win32more.Security.Authorization.UI.IEffectivePermission2_head
    IEffectivePermission2.ComputeEffectivePermissionWithSecondarySecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PSID,win32more.Foundation.PWSTR,POINTER(win32more.Security.Authorization.UI.SECURITY_OBJECT),UInt32,POINTER(win32more.Security.TOKEN_GROUPS_head),POINTER(win32more.Security.Authorization.AUTHZ_SID_OPERATION),POINTER(win32more.Security.TOKEN_GROUPS_head),POINTER(win32more.Security.Authorization.AUTHZ_SID_OPERATION),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head),POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION),POINTER(win32more.Security.Authorization.UI.EFFPERM_RESULT_LIST), use_last_error=False)(3, 'ComputeEffectivePermissionWithSecondarySecurity', ((1, 'pSid'),(1, 'pDeviceSid'),(1, 'pszServerName'),(1, 'pSecurityObjects'),(1, 'dwSecurityObjectCount'),(1, 'pUserGroups'),(1, 'pAuthzUserGroupsOperations'),(1, 'pDeviceGroups'),(1, 'pAuthzDeviceGroupsOperations'),(1, 'pAuthzUserClaims'),(1, 'pAuthzUserClaimsOperations'),(1, 'pAuthzDeviceClaims'),(1, 'pAuthzDeviceClaimsOperations'),(1, 'pEffpermResultLists'),)))
    win32more.System.Com.IUnknown
    return IEffectivePermission2
def _define_CreateSecurityPage():
    try:
        return WINFUNCTYPE(win32more.UI.Controls.HPROPSHEETPAGE,win32more.Security.Authorization.UI.ISecurityInformation_head, use_last_error=True)(("CreateSecurityPage", windll["ACLUI"]), ((1, 'psi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EditSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Security.Authorization.UI.ISecurityInformation_head, use_last_error=True)(("EditSecurity", windll["ACLUI"]), ((1, 'hwndOwner'),(1, 'psi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EditSecurityAdvanced():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Security.Authorization.UI.ISecurityInformation_head,win32more.Security.Authorization.UI.SI_PAGE_TYPE, use_last_error=False)(("EditSecurityAdvanced", windll["ACLUI"]), ((1, 'hwndOwner'),(1, 'psi'),(1, 'uSIPage'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "SI_EDIT_PERMS",
    "SI_EDIT_OWNER",
    "SI_CONTAINER",
    "SI_READONLY",
    "SI_RESET",
    "SI_OWNER_READONLY",
    "SI_OWNER_RECURSE",
    "SI_NO_ACL_PROTECT",
    "SI_NO_TREE_APPLY",
    "SI_PAGE_TITLE",
    "SI_SERVER_IS_DC",
    "SI_RESET_DACL_TREE",
    "SI_RESET_SACL_TREE",
    "SI_OBJECT_GUID",
    "SI_ACCESS_SPECIFIC",
    "SI_ACCESS_GENERAL",
    "SI_ACCESS_CONTAINER",
    "SI_ACCESS_PROPERTY",
    "DOBJ_RES_CONT",
    "DOBJ_RES_ROOT",
    "DOBJ_VOL_NTACLS",
    "DOBJ_COND_NTACLS",
    "DOBJ_RIBBON_LAUNCH",
    "SECURITY_OBJECT_ID_OBJECT_SD",
    "SECURITY_OBJECT_ID_SHARE",
    "SECURITY_OBJECT_ID_CENTRAL_POLICY",
    "SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE",
    "SECURITY_INFO_PAGE_FLAGS",
    "SI_ADVANCED",
    "SI_EDIT_AUDITS",
    "SI_EDIT_PROPERTIES",
    "SI_OBJECT_INFO_FLAGS",
    "SI_AUDITS_ELEVATION_REQUIRED",
    "SI_DISABLE_DENY_ACE",
    "SI_EDIT_EFFECTIVE",
    "SI_ENABLE_CENTRAL_POLICY",
    "SI_ENABLE_EDIT_ATTRIBUTE_CONDITION",
    "SI_MAY_WRITE",
    "SI_NO_ADDITIONAL_PERMISSION",
    "SI_OWNER_ELEVATION_REQUIRED",
    "SI_PERMS_ELEVATION_REQUIRED",
    "SI_RESET_DACL",
    "SI_RESET_OWNER",
    "SI_RESET_SACL",
    "SI_SCOPE_ELEVATION_REQUIRED",
    "SI_VIEW_ONLY",
    "SI_OBJECT_INFO",
    "SI_ACCESS",
    "SI_INHERIT_TYPE",
    "SI_PAGE_TYPE",
    "SI_PAGE_PERM",
    "SI_PAGE_ADVPERM",
    "SI_PAGE_AUDIT",
    "SI_PAGE_OWNER",
    "SI_PAGE_EFFECTIVE",
    "SI_PAGE_TAKEOWNERSHIP",
    "SI_PAGE_SHARE",
    "SI_PAGE_ACTIVATED",
    "SI_SHOW_DEFAULT",
    "SI_SHOW_PERM_ACTIVATED",
    "SI_SHOW_AUDIT_ACTIVATED",
    "SI_SHOW_OWNER_ACTIVATED",
    "SI_SHOW_EFFECTIVE_ACTIVATED",
    "SI_SHOW_SHARE_ACTIVATED",
    "SI_SHOW_CENTRAL_POLICY_ACTIVATED",
    "ISecurityInformation",
    "ISecurityInformation2",
    "SID_INFO",
    "SID_INFO_LIST",
    "IEffectivePermission",
    "ISecurityObjectTypeInfo",
    "ISecurityInformation3",
    "SECURITY_OBJECT",
    "EFFPERM_RESULT_LIST",
    "ISecurityInformation4",
    "IEffectivePermission2",
    "CreateSecurityPage",
    "EditSecurity",
    "EditSecurityAdvanced",
]
