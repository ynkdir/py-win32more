from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.Authentication.Identity.Provider
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ACCOUNT_STATE = Int32
NOT_CONNECTED: ACCOUNT_STATE = 0
CONNECTING: ACCOUNT_STATE = 1
CONNECT_COMPLETED: ACCOUNT_STATE = 2
IDENTITY_KEYWORD_ASSOCIATED: String = 'associated'
IDENTITY_KEYWORD_LOCAL: String = 'local'
IDENTITY_KEYWORD_HOMEGROUP: String = 'homegroup'
IDENTITY_KEYWORD_CONNECTED: String = 'connected'
OID_OAssociatedIdentityProviderObject: Guid = Guid('98c5a3dd-db68-4f1a-8d-2b-90-79-cd-fe-af-61')
STR_OUT_OF_BOX_EXPERIENCE: String = 'OutOfBoxExperience'
STR_MODERN_SETTINGS_ADD_USER: String = 'ModernSettingsAddUser'
STR_OUT_OF_BOX_UPGRADE_EXPERIENCE: String = 'OutOfBoxUpgradeExperience'
STR_COMPLETE_ACCOUNT: String = 'CompleteAccount'
STR_NTH_USER_FIRST_AUTH: String = 'NthUserFirstAuth'
STR_USER_NAME: String = 'Username'
STR_PROPERTY_STORE: String = 'PropertyStore'
class AsyncIAssociatedIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2834d6ed-297e-4e72-8a-51-96-1e-86-f0-51-52')
    @commethod(3)
    def Begin_AssociateIdentity(hwndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_AssociateIdentity(ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisassociateIdentity(hwndParent: win32more.Foundation.HWND, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisassociateIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_ChangeCredential(hwndParent: win32more.Foundation.HWND, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_ChangeCredential() -> win32more.Foundation.HRESULT: ...
class AsyncIConnectedIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9ce55141-bce9-4e15-82-4d-43-d7-9f-51-2f-93')
    @commethod(3)
    def Begin_ConnectIdentity(AuthBuffer: c_char_p_no, AuthBufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_ConnectIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisconnectIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisconnectIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_IsConnected() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_IsConnected(Connected: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_GetUrl(Identifier: win32more.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: win32more.System.Com.IBindCtx_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_GetUrl(PostData: POINTER(win32more.System.Com.VARIANT_head), Url: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_GetAccountState() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_GetAccountState(pState: POINTER(win32more.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> win32more.Foundation.HRESULT: ...
class AsyncIIdentityAdvise(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3ab4c8da-d038-4830-8d-d9-32-53-c5-5a-12-7f')
    @commethod(3)
    def Begin_IdentityUpdated(dwIdentityUpdateEvents: UInt32, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_IdentityUpdated() -> win32more.Foundation.HRESULT: ...
class AsyncIIdentityAuthentication(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9a2f918-feca-4e9c-96-33-61-cb-f1-3e-d3-4d')
    @commethod(3)
    def Begin_SetIdentityCredential(CredBuffer: c_char_p_no, CredBufferLength: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_SetIdentityCredential() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_ValidateIdentityCredential(CredBuffer: c_char_p_no, CredBufferLength: UInt32, ppIdentityProperties: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_ValidateIdentityCredential(ppIdentityProperties: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
class AsyncIIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c6fc9901-c433-4646-8f-48-4e-46-87-aa-e2-a0')
    @commethod(3)
    def Begin_GetIdentityEnum(eIdentityType: win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetIdentityEnum(ppIdentityEnum: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Create(lpszUserName: win32more.Foundation.PWSTR, pKeywordsToAdd: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Create(ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_Import(pPropertyStore: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_Import() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_Delete(lpszUniqueID: win32more.Foundation.PWSTR, pKeywordsToDelete: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_FindByUniqueID(lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_FindByUniqueID(ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_GetProviderPropertyStore() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_GetProviderPropertyStore(ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Begin_Advise(pIdentityAdvise: win32more.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Finish_Advise(pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Begin_UnAdvise(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Finish_UnAdvise() -> win32more.Foundation.HRESULT: ...
class AsyncIIdentityStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eefa1616-48de-4872-aa-64-6e-62-06-53-5a-51')
    @commethod(3)
    def Begin_GetCount() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetCount(pdwProviders: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_GetAt(dwProvider: UInt32, pProvGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_GetAt(pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_AddToCache(lpszUniqueID: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_AddToCache() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_ConvertToSid(lpszUniqueID: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_ConvertToSid(pSid: c_char_p_no, pcbRequiredSid: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_EnumerateIdentities(eIdentityType: win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_EnumerateIdentities(ppIdentityEnum: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_Reset() -> win32more.Foundation.HRESULT: ...
class AsyncIIdentityStoreEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fca3af9a-8a07-4eae-86-32-ec-3d-e6-58-a3-6a')
    @commethod(3)
    def Begin_CreateConnectedIdentity(LocalName: win32more.Foundation.PWSTR, ConnectedName: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_CreateConnectedIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DeleteConnectedIdentity(ConnectedName: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DeleteConnectedIdentity() -> win32more.Foundation.HRESULT: ...
CIdentityProfileHandler = Guid('ecf5bf46-e3b6-449a-b5-6b-43-f5-8f-86-78-14')
CoClassIdentityStore = Guid('30d49246-d217-465f-b0-0b-ac-9d-dd-65-2e-b7')
class IAssociatedIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2af066b3-4cbb-4cba-a7-98-20-4b-6a-f6-8c-c0')
    @commethod(3)
    def AssociateIdentity(hwndParent: win32more.Foundation.HWND, ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DisassociateIdentity(hwndParent: win32more.Foundation.HWND, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeCredential(hwndParent: win32more.Foundation.HWND, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IConnectedIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b7417b54-e08c-429b-96-c8-67-8d-13-69-ec-b1')
    @commethod(3)
    def ConnectIdentity(AuthBuffer: c_char_p_no, AuthBufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectIdentity() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsConnected(Connected: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetUrl(Identifier: win32more.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: win32more.System.Com.IBindCtx_head, PostData: POINTER(win32more.System.Com.VARIANT_head), Url: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAccountState(pState: POINTER(win32more.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> win32more.Foundation.HRESULT: ...
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
class IIdentityAdvise(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4e982fed-d14b-440c-b8-d6-bb-38-64-53-d3-86')
    @commethod(3)
    def IdentityUpdated(dwIdentityUpdateEvents: win32more.Security.Authentication.Identity.Provider.IdentityUpdateEvent, lpszUniqueID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IIdentityAuthentication(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5e7ef254-979f-43b5-b7-4e-06-e4-eb-7d-f0-f9')
    @commethod(3)
    def SetIdentityCredential(CredBuffer: c_char_p_no, CredBufferLength: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ValidateIdentityCredential(CredBuffer: c_char_p_no, CredBufferLength: UInt32, ppIdentityProperties: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
class IIdentityProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0d1b9e0c-e8ba-4f55-a8-1b-bc-e9-34-b9-48-f5')
    @commethod(3)
    def GetIdentityEnum(eIdentityType: win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Create(lpszUserName: win32more.Foundation.PWSTR, ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), pKeywordsToAdd: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Import(pPropertyStore: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(lpszUniqueID: win32more.Foundation.PWSTR, pKeywordsToDelete: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindByUniqueID(lpszUniqueID: win32more.Foundation.PWSTR, ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetProviderPropertyStore(ppPropertyStore: POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(pIdentityAdvise: win32more.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: win32more.Security.Authentication.Identity.Provider.IdentityUpdateEvent, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def UnAdvise(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class IIdentityStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('df586fa5-6f35-44f1-b2-09-b3-8e-16-97-72-eb')
    @commethod(3)
    def GetCount(pdwProviders: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(dwProvider: UInt32, pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddToCache(lpszUniqueID: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertToSid(lpszUniqueID: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: c_char_p_no, pcbRequiredSid: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateIdentities(eIdentityType: win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Reset() -> win32more.Foundation.HRESULT: ...
class IIdentityStoreEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9f9eb98-8f7f-4e38-95-77-69-80-11-4c-e3-2b')
    @commethod(3)
    def CreateConnectedIdentity(LocalName: win32more.Foundation.PWSTR, ConnectedName: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteConnectedIdentity(ConnectedName: win32more.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
IdentityUpdateEvent = UInt32
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
__all__ = [
    "ACCOUNT_STATE",
    "AsyncIAssociatedIdentityProvider",
    "AsyncIConnectedIdentityProvider",
    "AsyncIIdentityAdvise",
    "AsyncIIdentityAuthentication",
    "AsyncIIdentityProvider",
    "AsyncIIdentityStore",
    "AsyncIIdentityStoreEx",
    "CIdentityProfileHandler",
    "CONNECTING",
    "CONNECT_COMPLETED",
    "CoClassIdentityStore",
    "IAssociatedIdentityProvider",
    "IConnectedIdentityProvider",
    "IDENTITIES_ALL",
    "IDENTITIES_ME_ONLY",
    "IDENTITY_ASSOCIATED",
    "IDENTITY_CONNECTED",
    "IDENTITY_CREATED",
    "IDENTITY_DELETED",
    "IDENTITY_DISASSOCIATED",
    "IDENTITY_DISCONNECTED",
    "IDENTITY_IMPORTED",
    "IDENTITY_KEYWORD_ASSOCIATED",
    "IDENTITY_KEYWORD_CONNECTED",
    "IDENTITY_KEYWORD_HOMEGROUP",
    "IDENTITY_KEYWORD_LOCAL",
    "IDENTITY_PROPCHANGED",
    "IDENTITY_TYPE",
    "IDENTITY_URL",
    "IDENTITY_URL_ACCOUNT_SETTINGS",
    "IDENTITY_URL_CHANGE_PASSWORD_WIZARD",
    "IDENTITY_URL_CONNECT_WIZARD",
    "IDENTITY_URL_CREATE_ACCOUNT_WIZARD",
    "IDENTITY_URL_IFEXISTS_WIZARD",
    "IDENTITY_URL_RESTORE_WIZARD",
    "IDENTITY_URL_SIGN_IN_WIZARD",
    "IIdentityAdvise",
    "IIdentityAuthentication",
    "IIdentityProvider",
    "IIdentityStore",
    "IIdentityStoreEx",
    "IdentityUpdateEvent",
    "NOT_CONNECTED",
    "OID_OAssociatedIdentityProviderObject",
    "STR_COMPLETE_ACCOUNT",
    "STR_MODERN_SETTINGS_ADD_USER",
    "STR_NTH_USER_FIRST_AUTH",
    "STR_OUT_OF_BOX_EXPERIENCE",
    "STR_OUT_OF_BOX_UPGRADE_EXPERIENCE",
    "STR_PROPERTY_STORE",
    "STR_USER_NAME",
]
_arch_optional = [
]
