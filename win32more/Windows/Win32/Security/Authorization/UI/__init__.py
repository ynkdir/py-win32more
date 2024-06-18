from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.Authorization
import win32more.Windows.Win32.Security.Authorization.UI
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Controls
SI_EDIT_PERMS: Int32 = 0
SI_EDIT_OWNER: Int32 = 1
SI_CONTAINER: Int32 = 4
SI_READONLY: Int32 = 8
SI_RESET: Int32 = 32
SI_OWNER_READONLY: Int32 = 64
SI_OWNER_RECURSE: Int32 = 256
SI_NO_ACL_PROTECT: Int32 = 512
SI_NO_TREE_APPLY: Int32 = 1024
SI_PAGE_TITLE: Int32 = 2048
SI_SERVER_IS_DC: Int32 = 4096
SI_RESET_DACL_TREE: Int32 = 16384
SI_RESET_SACL_TREE: Int32 = 32768
SI_OBJECT_GUID: Int32 = 65536
SI_ACCESS_SPECIFIC: Int32 = 65536
SI_ACCESS_GENERAL: Int32 = 131072
SI_ACCESS_CONTAINER: Int32 = 262144
SI_ACCESS_PROPERTY: Int32 = 524288
DOBJ_RES_CONT: Int32 = 1
DOBJ_RES_ROOT: Int32 = 2
DOBJ_VOL_NTACLS: Int32 = 4
DOBJ_COND_NTACLS: Int32 = 8
DOBJ_RIBBON_LAUNCH: Int32 = 16
CFSTR_ACLUI_SID_INFO_LIST: String = 'CFSTR_ACLUI_SID_INFO_LIST'
SECURITY_OBJECT_ID_OBJECT_SD: UInt32 = 1
SECURITY_OBJECT_ID_SHARE: UInt32 = 2
SECURITY_OBJECT_ID_CENTRAL_POLICY: UInt32 = 3
SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE: UInt32 = 4
@winfunctype('ACLUI.dll')
def CreateSecurityPage(psi: win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation) -> win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE: ...
@winfunctype('ACLUI.dll')
def EditSecurity(hwndOwner: win32more.Windows.Win32.Foundation.HWND, psi: win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ACLUI.dll')
def EditSecurityAdvanced(hwndOwner: win32more.Windows.Win32.Foundation.HWND, psi: win32more.Windows.Win32.Security.Authorization.UI.ISecurityInformation, uSIPage: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class EFFPERM_RESULT_LIST(Structure):
    fEvaluated: win32more.Windows.Win32.Foundation.BOOLEAN
    cObjectTypeListLength: UInt32
    pObjectTypeList: POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST)
    pGrantedAccessList: POINTER(UInt32)
class IEffectivePermission(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3853dc76-9f35-407c-88a1-d19344365fbc}')
    @commethod(3)
    def GetEffectivePermission(self, pguidObjectType: POINTER(Guid), pUserSid: win32more.Windows.Win32.Security.PSID, pszServerName: win32more.Windows.Win32.Foundation.PWSTR, pSD: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, ppObjectTypeList: POINTER(POINTER(win32more.Windows.Win32.Security.OBJECT_TYPE_LIST)), pcObjectTypeListLength: POINTER(UInt32), ppGrantedAccessList: POINTER(POINTER(UInt32)), pcGrantedAccessListLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEffectivePermission2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{941fabca-dd47-4fca-90bb-b0e10255f20d}')
    @commethod(3)
    def ComputeEffectivePermissionWithSecondarySecurity(self, pSid: win32more.Windows.Win32.Security.PSID, pDeviceSid: win32more.Windows.Win32.Security.PSID, pszServerName: win32more.Windows.Win32.Foundation.PWSTR, pSecurityObjects: POINTER(win32more.Windows.Win32.Security.Authorization.UI.SECURITY_OBJECT), dwSecurityObjectCount: UInt32, pUserGroups: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS), pAuthzUserGroupsOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pDeviceGroups: POINTER(win32more.Windows.Win32.Security.TOKEN_GROUPS), pAuthzDeviceGroupsOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pAuthzUserClaims: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION), pAuthzUserClaimsOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pAuthzDeviceClaims: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION), pAuthzDeviceClaimsOperations: POINTER(win32more.Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pEffpermResultLists: POINTER(win32more.Windows.Win32.Security.Authorization.UI.EFFPERM_RESULT_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{965fc360-16ff-11d0-91cb-00aa00bbb723}')
    @commethod(3)
    def GetObjectInformation(self, pObjectInfo: POINTER(win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecurity(self, RequestedInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR), fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSecurity(self, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAccessRights(self, pguidObjectType: POINTER(Guid), dwFlags: win32more.Windows.Win32.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS, ppAccess: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.UI.SI_ACCESS)), pcAccesses: POINTER(UInt32), piDefaultAccess: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MapGeneric(self, pguidObjectType: POINTER(Guid), pAceFlags: POINTER(Byte), pMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetInheritTypes(self, ppInheritTypes: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.UI.SI_INHERIT_TYPE)), pcInheritTypes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PropertySheetPageCallback(self, hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: win32more.Windows.Win32.UI.Controls.PSPCB_MESSAGE, uPage: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a}')
    @commethod(3)
    def IsDaclCanonical(self, pDacl: POINTER(win32more.Windows.Win32.Security.ACL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def LookupSids(self, cSids: UInt32, rgpSids: POINTER(win32more.Windows.Win32.Security.PSID), ppdo: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2cdc9cc-31bd-4f8f-8c8b-b641af516a1a}')
    @commethod(3)
    def GetFullResourceName(self, ppszResourceName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenElevatedEditor(self, hWnd: win32more.Windows.Win32.Foundation.HWND, uPage: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation4(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea961070-cd14-4621-ace4-f63c03e583e4}')
    @commethod(3)
    def GetSecondarySecurity(self, pSecurityObjects: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.UI.SECURITY_OBJECT)), pSecurityObjectCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityObjectTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc3066eb-79ef-444b-9111-d18a75ebf2fa}')
    @commethod(3)
    def GetInheritSource(self, si: UInt32, pACL: POINTER(win32more.Windows.Win32.Security.ACL), ppInheritArray: POINTER(POINTER(win32more.Windows.Win32.Security.Authorization.INHERITED_FROMA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SECURITY_INFO_PAGE_FLAGS = UInt32
SI_ADVANCED: win32more.Windows.Win32.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS = 16
SI_EDIT_AUDITS: win32more.Windows.Win32.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS = 2
SI_EDIT_PROPERTIES: win32more.Windows.Win32.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS = 128
class SECURITY_OBJECT(Structure):
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    pData: VoidPtr
    cbData: UInt32
    pData2: VoidPtr
    cbData2: UInt32
    Id: UInt32
    fWellKnown: win32more.Windows.Win32.Foundation.BOOLEAN
class SID_INFO(Structure):
    pSid: win32more.Windows.Win32.Security.PSID
    pwzCommonName: win32more.Windows.Win32.Foundation.PWSTR
    pwzClass: win32more.Windows.Win32.Foundation.PWSTR
    pwzUPN: win32more.Windows.Win32.Foundation.PWSTR
class SID_INFO_LIST(Structure):
    cItems: UInt32
    aSidInfo: win32more.Windows.Win32.Security.Authorization.UI.SID_INFO * 1
class SI_ACCESS(Structure):
    pguid: POINTER(Guid)
    mask: UInt32
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
class SI_INHERIT_TYPE(Structure):
    pguid: POINTER(Guid)
    dwFlags: win32more.Windows.Win32.Security.ACE_FLAGS
    pszName: win32more.Windows.Win32.Foundation.PWSTR
class SI_OBJECT_INFO(Structure):
    dwFlags: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pszServerName: win32more.Windows.Win32.Foundation.PWSTR
    pszObjectName: win32more.Windows.Win32.Foundation.PWSTR
    pszPageTitle: win32more.Windows.Win32.Foundation.PWSTR
    guidObjectType: Guid
SI_OBJECT_INFO_FLAGS = UInt32
SI_AUDITS_ELEVATION_REQUIRED: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 33554432
SI_DISABLE_DENY_ACE: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 2147483648
SI_EDIT_EFFECTIVE: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 131072
SI_ENABLE_CENTRAL_POLICY: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 1073741824
SI_ENABLE_EDIT_ATTRIBUTE_CONDITION: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 536870912
SI_MAY_WRITE: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 268435456
SI_NO_ADDITIONAL_PERMISSION: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 2097152
SI_OWNER_ELEVATION_REQUIRED: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 67108864
SI_PERMS_ELEVATION_REQUIRED: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 16777216
SI_RESET_DACL: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 262144
SI_RESET_OWNER: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 1048576
SI_RESET_SACL: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 524288
SI_SCOPE_ELEVATION_REQUIRED: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 134217728
SI_VIEW_ONLY: win32more.Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS = 4194304
SI_PAGE_ACTIVATED = Int32
SI_SHOW_DEFAULT: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 0
SI_SHOW_PERM_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 1
SI_SHOW_AUDIT_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 2
SI_SHOW_OWNER_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 3
SI_SHOW_EFFECTIVE_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 4
SI_SHOW_SHARE_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 5
SI_SHOW_CENTRAL_POLICY_ACTIVATED: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_ACTIVATED = 6
SI_PAGE_TYPE = Int32
SI_PAGE_PERM: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 0
SI_PAGE_ADVPERM: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 1
SI_PAGE_AUDIT: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 2
SI_PAGE_OWNER: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 3
SI_PAGE_EFFECTIVE: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 4
SI_PAGE_TAKEOWNERSHIP: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 5
SI_PAGE_SHARE: win32more.Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE = 6


make_ready(__name__)
