from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Security.Authentication.Identity.Provider
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Variant
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACCOUNT_STATE = Int32
NOT_CONNECTED: ACCOUNT_STATE = 0
CONNECTING: ACCOUNT_STATE = 1
CONNECT_COMPLETED: ACCOUNT_STATE = 2
IDENTITY_KEYWORD_ASSOCIATED: String = 'associated'
IDENTITY_KEYWORD_LOCAL: String = 'local'
IDENTITY_KEYWORD_HOMEGROUP: String = 'homegroup'
IDENTITY_KEYWORD_CONNECTED: String = 'connected'
OID_OAssociatedIdentityProviderObject: Guid = Guid('{98c5a3dd-db68-4f1a-8d2b-9079cdfeaf61}')
STR_OUT_OF_BOX_EXPERIENCE: String = 'OutOfBoxExperience'
STR_MODERN_SETTINGS_ADD_USER: String = 'ModernSettingsAddUser'
STR_OUT_OF_BOX_UPGRADE_EXPERIENCE: String = 'OutOfBoxUpgradeExperience'
STR_COMPLETE_ACCOUNT: String = 'CompleteAccount'
STR_NTH_USER_FIRST_AUTH: String = 'NthUserFirstAuth'
STR_USER_NAME: String = 'Username'
STR_PROPERTY_STORE: String = 'PropertyStore'
class AsyncIAssociatedIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2834d6ed-297e-4e72-8a51-961e86f05152}')
    @commethod(3)
    def Begin_AssociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_AssociateIdentity(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisassociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisassociateIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_ChangeCredential(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_ChangeCredential(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIConnectedIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ce55141-bce9-4e15-824d-43d79f512f93}')
    @commethod(3)
    def Begin_ConnectIdentity(self, AuthBuffer: POINTER(Byte), AuthBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_ConnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_IsConnected(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_IsConnected(self, Connected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_GetUrl(self, Identifier: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_GetUrl(self, PostData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Url: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_GetAccountState(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_GetAccountState(self, pState: POINTER(Windows.Win32.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityAdvise(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3ab4c8da-d038-4830-8dd9-3253c55a127f}')
    @commethod(3)
    def Begin_IdentityUpdated(self, dwIdentityUpdateEvents: UInt32, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_IdentityUpdated(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityAuthentication(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9a2f918-feca-4e9c-9633-61cbf13ed34d}')
    @commethod(3)
    def Begin_SetIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_SetIdentityCredential(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_ValidateIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_ValidateIdentityCredential(self, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c6fc9901-c433-4646-8f48-4e4687aae2a0}')
    @commethod(3)
    def Begin_GetIdentityEnum(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetIdentityEnum(self, ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Create(self, lpszUserName: Windows.Win32.Foundation.PWSTR, pKeywordsToAdd: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Create(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_Import(self, pPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_Import(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_Delete(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, pKeywordsToDelete: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_FindByUniqueID(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_FindByUniqueID(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_GetProviderPropertyStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_GetProviderPropertyStore(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Begin_Advise(self, pIdentityAdvise: Windows.Win32.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Finish_Advise(self, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Begin_UnAdvise(self, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Finish_UnAdvise(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityStore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eefa1616-48de-4872-aa64-6e6206535a51}')
    @commethod(3)
    def Begin_GetCount(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetCount(self, pdwProviders: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_GetAt(self, dwProvider: UInt32, pProvGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_GetAt(self, pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_AddToCache(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_AddToCache(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_ConvertToSid(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_ConvertToSid(self, pSid: POINTER(Byte), pcbRequiredSid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_EnumerateIdentities(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_EnumerateIdentities(self, ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityStoreEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fca3af9a-8a07-4eae-8632-ec3de658a36a}')
    @commethod(3)
    def Begin_CreateConnectedIdentity(self, LocalName: Windows.Win32.Foundation.PWSTR, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_CreateConnectedIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DeleteConnectedIdentity(self, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DeleteConnectedIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
CIdentityProfileHandler = Guid('{ecf5bf46-e3b6-449a-b56b-43f58f867814}')
CoClassIdentityStore = Guid('{30d49246-d217-465f-b00b-ac9ddd652eb7}')
class IAssociatedIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2af066b3-4cbb-4cba-a798-204b6af68cc0}')
    @commethod(3)
    def AssociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisassociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeCredential(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IConnectedIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7417b54-e08c-429b-96c8-678d1369ecb1}')
    @commethod(3)
    def ConnectIdentity(self, AuthBuffer: POINTER(Byte), AuthBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsConnected(self, Connected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUrl(self, Identifier: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: Windows.Win32.System.Com.IBindCtx_head, PostData: POINTER(Windows.Win32.System.Variant.VARIANT_head), Url: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAccountState(self, pState: POINTER(Windows.Win32.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
IDENTITY_TYPE = Int32
IDENTITIES_ALL: IDENTITY_TYPE = 0
IDENTITIES_ME_ONLY: IDENTITY_TYPE = 1
IDENTITY_URL = Int32
IDENTITY_URL_CREATE_ACCOUNT_WIZARD: IDENTITY_URL = 0
IDENTITY_URL_SIGN_IN_WIZARD: IDENTITY_URL = 1
IDENTITY_URL_CHANGE_PASSWORD_WIZARD: IDENTITY_URL = 2
IDENTITY_URL_IFEXISTS_WIZARD: IDENTITY_URL = 3
IDENTITY_URL_ACCOUNT_SETTINGS: IDENTITY_URL = 4
IDENTITY_URL_RESTORE_WIZARD: IDENTITY_URL = 5
IDENTITY_URL_CONNECT_WIZARD: IDENTITY_URL = 6
class IIdentityAdvise(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e982fed-d14b-440c-b8d6-bb386453d386}')
    @commethod(3)
    def IdentityUpdated(self, dwIdentityUpdateEvents: UInt32, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityAuthentication(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e7ef254-979f-43b5-b74e-06e4eb7df0f9}')
    @commethod(3)
    def SetIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ValidateIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d1b9e0c-e8ba-4f55-a81b-bce934b948f5}')
    @commethod(3)
    def GetIdentityEnum(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Create(self, lpszUserName: Windows.Win32.Foundation.PWSTR, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head), pKeywordsToAdd: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Import(self, pPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, pKeywordsToDelete: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindByUniqueID(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProviderPropertyStore(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, pIdentityAdvise: Windows.Win32.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: UInt32, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnAdvise(self, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityStore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df586fa5-6f35-44f1-b209-b38e169772eb}')
    @commethod(3)
    def GetCount(self, pdwProviders: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwProvider: UInt32, pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddToCache(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertToSid(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: POINTER(Byte), pcbRequiredSid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateIdentities(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityStoreEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9f9eb98-8f7f-4e38-9577-6980114ce32b}')
    @commethod(3)
    def CreateConnectedIdentity(self, LocalName: Windows.Win32.Foundation.PWSTR, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteConnectedIdentity(self, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
IdentityUpdateEvent = Int32
IDENTITY_ASSOCIATED: IdentityUpdateEvent = 1
IDENTITY_DISASSOCIATED: IdentityUpdateEvent = 2
IDENTITY_CREATED: IdentityUpdateEvent = 4
IDENTITY_IMPORTED: IdentityUpdateEvent = 8
IDENTITY_DELETED: IdentityUpdateEvent = 16
IDENTITY_PROPCHANGED: IdentityUpdateEvent = 32
IDENTITY_CONNECTED: IdentityUpdateEvent = 64
IDENTITY_DISCONNECTED: IdentityUpdateEvent = 128
make_head(_module, 'AsyncIAssociatedIdentityProvider')
make_head(_module, 'AsyncIConnectedIdentityProvider')
make_head(_module, 'AsyncIIdentityAdvise')
make_head(_module, 'AsyncIIdentityAuthentication')
make_head(_module, 'AsyncIIdentityProvider')
make_head(_module, 'AsyncIIdentityStore')
make_head(_module, 'AsyncIIdentityStoreEx')
make_head(_module, 'IAssociatedIdentityProvider')
make_head(_module, 'IConnectedIdentityProvider')
make_head(_module, 'IIdentityAdvise')
make_head(_module, 'IIdentityAuthentication')
make_head(_module, 'IIdentityProvider')
make_head(_module, 'IIdentityStore')
make_head(_module, 'IIdentityStoreEx')
