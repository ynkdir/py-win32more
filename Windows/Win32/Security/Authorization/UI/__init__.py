from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.Authorization
import Windows.Win32.Security.Authorization.UI
import Windows.Win32.System.Com
import Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def CreateSecurityPage(psi: Windows.Win32.Security.Authorization.UI.ISecurityInformation_head) -> Windows.Win32.UI.Controls.HPROPSHEETPAGE: ...
@winfunctype('ACLUI.dll')
def EditSecurity(hwndOwner: Windows.Win32.Foundation.HWND, psi: Windows.Win32.Security.Authorization.UI.ISecurityInformation_head) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ACLUI.dll')
def EditSecurityAdvanced(hwndOwner: Windows.Win32.Foundation.HWND, psi: Windows.Win32.Security.Authorization.UI.ISecurityInformation_head, uSIPage: Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class EFFPERM_RESULT_LIST(EasyCastStructure):
    fEvaluated: Windows.Win32.Foundation.BOOLEAN
    cObjectTypeListLength: UInt32
    pObjectTypeList: POINTER(Windows.Win32.Security.OBJECT_TYPE_LIST_head)
    pGrantedAccessList: POINTER(UInt32)
class IEffectivePermission(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3853dc76-9f35-407c-88a1-d19344365fbc}')
    @commethod(3)
    def GetEffectivePermission(self, pguidObjectType: POINTER(Guid), pUserSid: Windows.Win32.Foundation.PSID, pszServerName: Windows.Win32.Foundation.PWSTR, pSD: Windows.Win32.Security.PSECURITY_DESCRIPTOR, ppObjectTypeList: POINTER(POINTER(Windows.Win32.Security.OBJECT_TYPE_LIST_head)), pcObjectTypeListLength: POINTER(UInt32), ppGrantedAccessList: POINTER(POINTER(UInt32)), pcGrantedAccessListLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEffectivePermission2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{941fabca-dd47-4fca-90bb-b0e10255f20d}')
    @commethod(3)
    def ComputeEffectivePermissionWithSecondarySecurity(self, pSid: Windows.Win32.Foundation.PSID, pDeviceSid: Windows.Win32.Foundation.PSID, pszServerName: Windows.Win32.Foundation.PWSTR, pSecurityObjects: POINTER(Windows.Win32.Security.Authorization.UI.SECURITY_OBJECT_head), dwSecurityObjectCount: UInt32, pUserGroups: POINTER(Windows.Win32.Security.TOKEN_GROUPS_head), pAuthzUserGroupsOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pDeviceGroups: POINTER(Windows.Win32.Security.TOKEN_GROUPS_head), pAuthzDeviceGroupsOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SID_OPERATION), pAuthzUserClaims: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), pAuthzUserClaimsOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pAuthzDeviceClaims: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), pAuthzDeviceClaimsOperations: POINTER(Windows.Win32.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pEffpermResultLists: POINTER(Windows.Win32.Security.Authorization.UI.EFFPERM_RESULT_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{965fc360-16ff-11d0-91cb-00aa00bbb723}')
    @commethod(3)
    def GetObjectInformation(self, pObjectInfo: POINTER(Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecurity(self, RequestedInformation: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, ppSecurityDescriptor: POINTER(Windows.Win32.Security.PSECURITY_DESCRIPTOR), fDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSecurity(self, SecurityInformation: Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAccessRights(self, pguidObjectType: POINTER(Guid), dwFlags: Windows.Win32.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS, ppAccess: POINTER(POINTER(Windows.Win32.Security.Authorization.UI.SI_ACCESS_head)), pcAccesses: POINTER(UInt32), piDefaultAccess: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MapGeneric(self, pguidObjectType: POINTER(Guid), pAceFlags: POINTER(Byte), pMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetInheritTypes(self, ppInheritTypes: POINTER(POINTER(Windows.Win32.Security.Authorization.UI.SI_INHERIT_TYPE_head)), pcInheritTypes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PropertySheetPageCallback(self, hwnd: Windows.Win32.Foundation.HWND, uMsg: Windows.Win32.UI.Controls.PSPCB_MESSAGE, uPage: Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a}')
    @commethod(3)
    def IsDaclCanonical(self, pDacl: POINTER(Windows.Win32.Security.ACL_head)) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def LookupSids(self, cSids: UInt32, rgpSids: POINTER(Windows.Win32.Foundation.PSID), ppdo: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation3(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2cdc9cc-31bd-4f8f-8c8b-b641af516a1a}')
    @commethod(3)
    def GetFullResourceName(self, ppszResourceName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenElevatedEditor(self, hWnd: Windows.Win32.Foundation.HWND, uPage: Windows.Win32.Security.Authorization.UI.SI_PAGE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityInformation4(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea961070-cd14-4621-ace4-f63c03e583e4}')
    @commethod(3)
    def GetSecondarySecurity(self, pSecurityObjects: POINTER(POINTER(Windows.Win32.Security.Authorization.UI.SECURITY_OBJECT_head)), pSecurityObjectCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityObjectTypeInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc3066eb-79ef-444b-9111-d18a75ebf2fa}')
    @commethod(3)
    def GetInheritSource(self, si: UInt32, pACL: POINTER(Windows.Win32.Security.ACL_head), ppInheritArray: POINTER(POINTER(Windows.Win32.Security.Authorization.INHERITED_FROMA_head))) -> Windows.Win32.Foundation.HRESULT: ...
SECURITY_INFO_PAGE_FLAGS = UInt32
SI_ADVANCED: SECURITY_INFO_PAGE_FLAGS = 16
SI_EDIT_AUDITS: SECURITY_INFO_PAGE_FLAGS = 2
SI_EDIT_PROPERTIES: SECURITY_INFO_PAGE_FLAGS = 128
class SECURITY_OBJECT(EasyCastStructure):
    pwszName: Windows.Win32.Foundation.PWSTR
    pData: VoidPtr
    cbData: UInt32
    pData2: VoidPtr
    cbData2: UInt32
    Id: UInt32
    fWellKnown: Windows.Win32.Foundation.BOOLEAN
class SID_INFO(EasyCastStructure):
    pSid: Windows.Win32.Foundation.PSID
    pwzCommonName: Windows.Win32.Foundation.PWSTR
    pwzClass: Windows.Win32.Foundation.PWSTR
    pwzUPN: Windows.Win32.Foundation.PWSTR
class SID_INFO_LIST(EasyCastStructure):
    cItems: UInt32
    aSidInfo: Windows.Win32.Security.Authorization.UI.SID_INFO * 1
class SI_ACCESS(EasyCastStructure):
    pguid: POINTER(Guid)
    mask: UInt32
    pszName: Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
class SI_INHERIT_TYPE(EasyCastStructure):
    pguid: POINTER(Guid)
    dwFlags: Windows.Win32.Security.ACE_FLAGS
    pszName: Windows.Win32.Foundation.PWSTR
class SI_OBJECT_INFO(EasyCastStructure):
    dwFlags: Windows.Win32.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS
    hInstance: Windows.Win32.Foundation.HINSTANCE
    pszServerName: Windows.Win32.Foundation.PWSTR
    pszObjectName: Windows.Win32.Foundation.PWSTR
    pszPageTitle: Windows.Win32.Foundation.PWSTR
    guidObjectType: Guid
SI_OBJECT_INFO_FLAGS = UInt32
SI_AUDITS_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 33554432
SI_DISABLE_DENY_ACE: SI_OBJECT_INFO_FLAGS = 2147483648
SI_EDIT_EFFECTIVE: SI_OBJECT_INFO_FLAGS = 131072
SI_ENABLE_CENTRAL_POLICY: SI_OBJECT_INFO_FLAGS = 1073741824
SI_ENABLE_EDIT_ATTRIBUTE_CONDITION: SI_OBJECT_INFO_FLAGS = 536870912
SI_MAY_WRITE: SI_OBJECT_INFO_FLAGS = 268435456
SI_NO_ADDITIONAL_PERMISSION: SI_OBJECT_INFO_FLAGS = 2097152
SI_OWNER_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 67108864
SI_PERMS_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 16777216
SI_RESET_DACL: SI_OBJECT_INFO_FLAGS = 262144
SI_RESET_OWNER: SI_OBJECT_INFO_FLAGS = 1048576
SI_RESET_SACL: SI_OBJECT_INFO_FLAGS = 524288
SI_SCOPE_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 134217728
SI_VIEW_ONLY: SI_OBJECT_INFO_FLAGS = 4194304
SI_PAGE_ACTIVATED = Int32
SI_SHOW_DEFAULT: SI_PAGE_ACTIVATED = 0
SI_SHOW_PERM_ACTIVATED: SI_PAGE_ACTIVATED = 1
SI_SHOW_AUDIT_ACTIVATED: SI_PAGE_ACTIVATED = 2
SI_SHOW_OWNER_ACTIVATED: SI_PAGE_ACTIVATED = 3
SI_SHOW_EFFECTIVE_ACTIVATED: SI_PAGE_ACTIVATED = 4
SI_SHOW_SHARE_ACTIVATED: SI_PAGE_ACTIVATED = 5
SI_SHOW_CENTRAL_POLICY_ACTIVATED: SI_PAGE_ACTIVATED = 6
SI_PAGE_TYPE = Int32
SI_PAGE_PERM: SI_PAGE_TYPE = 0
SI_PAGE_ADVPERM: SI_PAGE_TYPE = 1
SI_PAGE_AUDIT: SI_PAGE_TYPE = 2
SI_PAGE_OWNER: SI_PAGE_TYPE = 3
SI_PAGE_EFFECTIVE: SI_PAGE_TYPE = 4
SI_PAGE_TAKEOWNERSHIP: SI_PAGE_TYPE = 5
SI_PAGE_SHARE: SI_PAGE_TYPE = 6
make_head(_module, 'EFFPERM_RESULT_LIST')
make_head(_module, 'IEffectivePermission')
make_head(_module, 'IEffectivePermission2')
make_head(_module, 'ISecurityInformation')
make_head(_module, 'ISecurityInformation2')
make_head(_module, 'ISecurityInformation3')
make_head(_module, 'ISecurityInformation4')
make_head(_module, 'ISecurityObjectTypeInfo')
make_head(_module, 'SECURITY_OBJECT')
make_head(_module, 'SID_INFO')
make_head(_module, 'SID_INFO_LIST')
make_head(_module, 'SI_ACCESS')
make_head(_module, 'SI_INHERIT_TYPE')
make_head(_module, 'SI_OBJECT_INFO')
