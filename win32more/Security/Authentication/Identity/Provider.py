from win32more import *
import win32more.Foundation
import win32more.Security.Authentication.Identity.Provider
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
OID_OAssociatedIdentityProviderObject = '98c5a3dd-db68-4f1a-8d2b-9079cdfeaf61'
IDENTITY_TYPE = Int32
IDENTITIES_ALL = 0
IDENTITIES_ME_ONLY = 1
IdentityUpdateEvent = UInt32
IDENTITY_ASSOCIATED = 1
IDENTITY_DISASSOCIATED = 2
IDENTITY_CREATED = 4
IDENTITY_IMPORTED = 8
IDENTITY_DELETED = 16
IDENTITY_PROPCHANGED = 32
IDENTITY_CONNECTED = 64
IDENTITY_DISCONNECTED = 128
def _define_IIdentityAdvise_head():
    class IIdentityAdvise(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e982fed-d14b-440c-b8d6-bb386453d386')
    return IIdentityAdvise
def _define_IIdentityAdvise():
    IIdentityAdvise = win32more.Security.Authentication.Identity.Provider.IIdentityAdvise_head
    IIdentityAdvise.IdentityUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IdentityUpdateEvent,win32more.Foundation.PWSTR, use_last_error=False)(3, 'IdentityUpdated', ((1, 'dwIdentityUpdateEvents'),(1, 'lpszUniqueID'),)))
    return IIdentityAdvise
def _define_AsyncIIdentityAdvise_head():
    class AsyncIIdentityAdvise(win32more.System.Com.IUnknown_head):
        Guid = Guid('3ab4c8da-d038-4830-8dd9-3253c55a127f')
    return AsyncIIdentityAdvise
def _define_AsyncIIdentityAdvise():
    AsyncIIdentityAdvise = win32more.Security.Authentication.Identity.Provider.AsyncIIdentityAdvise_head
    AsyncIIdentityAdvise.Begin_IdentityUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Begin_IdentityUpdated', ((1, 'dwIdentityUpdateEvents'),(1, 'lpszUniqueID'),)))
    AsyncIIdentityAdvise.Finish_IdentityUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Finish_IdentityUpdated', ()))
    return AsyncIIdentityAdvise
def _define_IIdentityProvider_head():
    class IIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d1b9e0c-e8ba-4f55-a81b-bce934b948f5')
    return IIdentityProvider
def _define_IIdentityProvider():
    IIdentityProvider = win32more.Security.Authentication.Identity.Provider.IIdentityProvider_head
    IIdentityProvider.GetIdentityEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(3, 'GetIdentityEnum', ((1, 'eIdentityType'),(1, 'pFilterkey'),(1, 'pFilterPropVarValue'),(1, 'ppIdentityEnum'),)))
    IIdentityProvider.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'Create', ((1, 'lpszUserName'),(1, 'ppPropertyStore'),(1, 'pKeywordsToAdd'),)))
    IIdentityProvider.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(5, 'Import', ((1, 'pPropertyStore'),)))
    IIdentityProvider.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'Delete', ((1, 'lpszUniqueID'),(1, 'pKeywordsToDelete'),)))
    IIdentityProvider.FindByUniqueID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(7, 'FindByUniqueID', ((1, 'lpszUniqueID'),(1, 'ppPropertyStore'),)))
    IIdentityProvider.GetProviderPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(8, 'GetProviderPropertyStore', ((1, 'ppPropertyStore'),)))
    IIdentityProvider.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IIdentityAdvise_head,win32more.Security.Authentication.Identity.Provider.IdentityUpdateEvent,POINTER(UInt32), use_last_error=False)(9, 'Advise', ((1, 'pIdentityAdvise'),(1, 'dwIdentityUpdateEvents'),(1, 'pdwCookie'),)))
    IIdentityProvider.UnAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'UnAdvise', ((1, 'dwCookie'),)))
    return IIdentityProvider
def _define_AsyncIIdentityProvider_head():
    class AsyncIIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('c6fc9901-c433-4646-8f48-4e4687aae2a0')
    return AsyncIIdentityProvider
def _define_AsyncIIdentityProvider():
    AsyncIIdentityProvider = win32more.Security.Authentication.Identity.Provider.AsyncIIdentityProvider_head
    AsyncIIdentityProvider.Begin_GetIdentityEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(3, 'Begin_GetIdentityEnum', ((1, 'eIdentityType'),(1, 'pFilterkey'),(1, 'pFilterPropVarValue'),)))
    AsyncIIdentityProvider.Finish_GetIdentityEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(4, 'Finish_GetIdentityEnum', ((1, 'ppIdentityEnum'),)))
    AsyncIIdentityProvider.Begin_Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'Begin_Create', ((1, 'lpszUserName'),(1, 'pKeywordsToAdd'),)))
    AsyncIIdentityProvider.Finish_Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(6, 'Finish_Create', ((1, 'ppPropertyStore'),)))
    AsyncIIdentityProvider.Begin_Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(7, 'Begin_Import', ((1, 'pPropertyStore'),)))
    AsyncIIdentityProvider.Finish_Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Finish_Import', ()))
    AsyncIIdentityProvider.Begin_Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(9, 'Begin_Delete', ((1, 'lpszUniqueID'),(1, 'pKeywordsToDelete'),)))
    AsyncIIdentityProvider.Finish_Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Finish_Delete', ()))
    AsyncIIdentityProvider.Begin_FindByUniqueID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(11, 'Begin_FindByUniqueID', ((1, 'lpszUniqueID'),)))
    AsyncIIdentityProvider.Finish_FindByUniqueID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(12, 'Finish_FindByUniqueID', ((1, 'ppPropertyStore'),)))
    AsyncIIdentityProvider.Begin_GetProviderPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Begin_GetProviderPropertyStore', ()))
    AsyncIIdentityProvider.Finish_GetProviderPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(14, 'Finish_GetProviderPropertyStore', ((1, 'ppPropertyStore'),)))
    AsyncIIdentityProvider.Begin_Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IIdentityAdvise_head,UInt32, use_last_error=False)(15, 'Begin_Advise', ((1, 'pIdentityAdvise'),(1, 'dwIdentityUpdateEvents'),)))
    AsyncIIdentityProvider.Finish_Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'Finish_Advise', ((1, 'pdwCookie'),)))
    AsyncIIdentityProvider.Begin_UnAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'Begin_UnAdvise', ((1, 'dwCookie'),)))
    AsyncIIdentityProvider.Finish_UnAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Finish_UnAdvise', ()))
    return AsyncIIdentityProvider
def _define_IAssociatedIdentityProvider_head():
    class IAssociatedIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2af066b3-4cbb-4cba-a798-204b6af68cc0')
    return IAssociatedIdentityProvider
def _define_IAssociatedIdentityProvider():
    IAssociatedIdentityProvider = win32more.Security.Authentication.Identity.Provider.IAssociatedIdentityProvider_head
    IAssociatedIdentityProvider.AssociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(3, 'AssociateIdentity', ((1, 'hwndParent'),(1, 'ppPropertyStore'),)))
    IAssociatedIdentityProvider.DisassociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(4, 'DisassociateIdentity', ((1, 'hwndParent'),(1, 'lpszUniqueID'),)))
    IAssociatedIdentityProvider.ChangeCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(5, 'ChangeCredential', ((1, 'hwndParent'),(1, 'lpszUniqueID'),)))
    return IAssociatedIdentityProvider
def _define_AsyncIAssociatedIdentityProvider_head():
    class AsyncIAssociatedIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2834d6ed-297e-4e72-8a51-961e86f05152')
    return AsyncIAssociatedIdentityProvider
def _define_AsyncIAssociatedIdentityProvider():
    AsyncIAssociatedIdentityProvider = win32more.Security.Authentication.Identity.Provider.AsyncIAssociatedIdentityProvider_head
    AsyncIAssociatedIdentityProvider.Begin_AssociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'Begin_AssociateIdentity', ((1, 'hwndParent'),)))
    AsyncIAssociatedIdentityProvider.Finish_AssociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(4, 'Finish_AssociateIdentity', ((1, 'ppPropertyStore'),)))
    AsyncIAssociatedIdentityProvider.Begin_DisassociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Begin_DisassociateIdentity', ((1, 'hwndParent'),(1, 'lpszUniqueID'),)))
    AsyncIAssociatedIdentityProvider.Finish_DisassociateIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Finish_DisassociateIdentity', ()))
    AsyncIAssociatedIdentityProvider.Begin_ChangeCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(7, 'Begin_ChangeCredential', ((1, 'hwndParent'),(1, 'lpszUniqueID'),)))
    AsyncIAssociatedIdentityProvider.Finish_ChangeCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Finish_ChangeCredential', ()))
    return AsyncIAssociatedIdentityProvider
IDENTITY_URL = Int32
IDENTITY_URL_CREATE_ACCOUNT_WIZARD = 0
IDENTITY_URL_SIGN_IN_WIZARD = 1
IDENTITY_URL_CHANGE_PASSWORD_WIZARD = 2
IDENTITY_URL_IFEXISTS_WIZARD = 3
IDENTITY_URL_ACCOUNT_SETTINGS = 4
IDENTITY_URL_RESTORE_WIZARD = 5
IDENTITY_URL_CONNECT_WIZARD = 6
ACCOUNT_STATE = Int32
NOT_CONNECTED = 0
CONNECTING = 1
CONNECT_COMPLETED = 2
def _define_IConnectedIdentityProvider_head():
    class IConnectedIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b7417b54-e08c-429b-96c8-678d1369ecb1')
    return IConnectedIdentityProvider
def _define_IConnectedIdentityProvider():
    IConnectedIdentityProvider = win32more.Security.Authentication.Identity.Provider.IConnectedIdentityProvider_head
    IConnectedIdentityProvider.ConnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'ConnectIdentity', ((1, 'AuthBuffer'),(1, 'AuthBufferSize'),)))
    IConnectedIdentityProvider.DisconnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DisconnectIdentity', ()))
    IConnectedIdentityProvider.IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'IsConnected', ((1, 'Connected'),)))
    IConnectedIdentityProvider.GetUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_URL,win32more.System.Com.IBindCtx_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetUrl', ((1, 'Identifier'),(1, 'Context'),(1, 'PostData'),(1, 'Url'),)))
    IConnectedIdentityProvider.GetAccountState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authentication.Identity.Provider.ACCOUNT_STATE), use_last_error=False)(7, 'GetAccountState', ((1, 'pState'),)))
    return IConnectedIdentityProvider
def _define_AsyncIConnectedIdentityProvider_head():
    class AsyncIConnectedIdentityProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ce55141-bce9-4e15-824d-43d79f512f93')
    return AsyncIConnectedIdentityProvider
def _define_AsyncIConnectedIdentityProvider():
    AsyncIConnectedIdentityProvider = win32more.Security.Authentication.Identity.Provider.AsyncIConnectedIdentityProvider_head
    AsyncIConnectedIdentityProvider.Begin_ConnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'Begin_ConnectIdentity', ((1, 'AuthBuffer'),(1, 'AuthBufferSize'),)))
    AsyncIConnectedIdentityProvider.Finish_ConnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Finish_ConnectIdentity', ()))
    AsyncIConnectedIdentityProvider.Begin_DisconnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Begin_DisconnectIdentity', ()))
    AsyncIConnectedIdentityProvider.Finish_DisconnectIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Finish_DisconnectIdentity', ()))
    AsyncIConnectedIdentityProvider.Begin_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Begin_IsConnected', ()))
    AsyncIConnectedIdentityProvider.Finish_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'Finish_IsConnected', ((1, 'Connected'),)))
    AsyncIConnectedIdentityProvider.Begin_GetUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_URL,win32more.System.Com.IBindCtx_head, use_last_error=False)(9, 'Begin_GetUrl', ((1, 'Identifier'),(1, 'Context'),)))
    AsyncIConnectedIdentityProvider.Finish_GetUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'Finish_GetUrl', ((1, 'PostData'),(1, 'Url'),)))
    AsyncIConnectedIdentityProvider.Begin_GetAccountState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Begin_GetAccountState', ()))
    AsyncIConnectedIdentityProvider.Finish_GetAccountState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Authentication.Identity.Provider.ACCOUNT_STATE), use_last_error=False)(12, 'Finish_GetAccountState', ((1, 'pState'),)))
    return AsyncIConnectedIdentityProvider
def _define_IIdentityAuthentication_head():
    class IIdentityAuthentication(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e7ef254-979f-43b5-b74e-06e4eb7df0f9')
    return IIdentityAuthentication
def _define_IIdentityAuthentication():
    IIdentityAuthentication = win32more.Security.Authentication.Identity.Provider.IIdentityAuthentication_head
    IIdentityAuthentication.SetIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'SetIdentityCredential', ((1, 'CredBuffer'),(1, 'CredBufferLength'),)))
    IIdentityAuthentication.ValidateIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(4, 'ValidateIdentityCredential', ((1, 'CredBuffer'),(1, 'CredBufferLength'),(1, 'ppIdentityProperties'),)))
    return IIdentityAuthentication
def _define_AsyncIIdentityAuthentication_head():
    class AsyncIIdentityAuthentication(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9a2f918-feca-4e9c-9633-61cbf13ed34d')
    return AsyncIIdentityAuthentication
def _define_AsyncIIdentityAuthentication():
    AsyncIIdentityAuthentication = win32more.Security.Authentication.Identity.Provider.AsyncIIdentityAuthentication_head
    AsyncIIdentityAuthentication.Begin_SetIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'Begin_SetIdentityCredential', ((1, 'CredBuffer'),(1, 'CredBufferLength'),)))
    AsyncIIdentityAuthentication.Finish_SetIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Finish_SetIdentityCredential', ()))
    AsyncIIdentityAuthentication.Begin_ValidateIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(5, 'Begin_ValidateIdentityCredential', ((1, 'CredBuffer'),(1, 'CredBufferLength'),(1, 'ppIdentityProperties'),)))
    AsyncIIdentityAuthentication.Finish_ValidateIdentityCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(6, 'Finish_ValidateIdentityCredential', ((1, 'ppIdentityProperties'),)))
    return AsyncIIdentityAuthentication
CoClassIdentityStore = Guid('30d49246-d217-465f-b00b-ac9ddd652eb7')
CIdentityProfileHandler = Guid('ecf5bf46-e3b6-449a-b56b-43f58f867814')
def _define_IIdentityStore_head():
    class IIdentityStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('df586fa5-6f35-44f1-b209-b38e169772eb')
    return IIdentityStore
def _define_IIdentityStore():
    IIdentityStore = win32more.Security.Authentication.Identity.Provider.IIdentityStore_head
    IIdentityStore.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwProviders'),)))
    IIdentityStore.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'GetAt', ((1, 'dwProvider'),(1, 'pProvGuid'),(1, 'ppIdentityProvider'),)))
    IIdentityStore.AddToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(5, 'AddToCache', ((1, 'lpszUniqueID'),(1, 'ProviderGUID'),)))
    IIdentityStore.ConvertToSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt16,POINTER(Byte),POINTER(UInt16), use_last_error=False)(6, 'ConvertToSid', ((1, 'lpszUniqueID'),(1, 'ProviderGUID'),(1, 'cbSid'),(1, 'pSid'),(1, 'pcbRequiredSid'),)))
    IIdentityStore.EnumerateIdentities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(7, 'EnumerateIdentities', ((1, 'eIdentityType'),(1, 'pFilterkey'),(1, 'pFilterPropVarValue'),(1, 'ppIdentityEnum'),)))
    IIdentityStore.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reset', ()))
    return IIdentityStore
def _define_AsyncIIdentityStore_head():
    class AsyncIIdentityStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('eefa1616-48de-4872-aa64-6e6206535a51')
    return AsyncIIdentityStore
def _define_AsyncIIdentityStore():
    AsyncIIdentityStore = win32more.Security.Authentication.Identity.Provider.AsyncIIdentityStore_head
    AsyncIIdentityStore.Begin_GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Begin_GetCount', ()))
    AsyncIIdentityStore.Finish_GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'Finish_GetCount', ((1, 'pdwProviders'),)))
    AsyncIIdentityStore.Begin_GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(5, 'Begin_GetAt', ((1, 'dwProvider'),(1, 'pProvGuid'),)))
    AsyncIIdentityStore.Finish_GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'Finish_GetAt', ((1, 'pProvGuid'),(1, 'ppIdentityProvider'),)))
    AsyncIIdentityStore.Begin_AddToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(7, 'Begin_AddToCache', ((1, 'lpszUniqueID'),(1, 'ProviderGUID'),)))
    AsyncIIdentityStore.Finish_AddToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Finish_AddToCache', ()))
    AsyncIIdentityStore.Begin_ConvertToSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt16,c_char_p_no, use_last_error=False)(9, 'Begin_ConvertToSid', ((1, 'lpszUniqueID'),(1, 'ProviderGUID'),(1, 'cbSid'),(1, 'pSid'),)))
    AsyncIIdentityStore.Finish_ConvertToSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt16), use_last_error=False)(10, 'Finish_ConvertToSid', ((1, 'pSid'),(1, 'pcbRequiredSid'),)))
    AsyncIIdentityStore.Begin_EnumerateIdentities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Authentication.Identity.Provider.IDENTITY_TYPE,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(11, 'Begin_EnumerateIdentities', ((1, 'eIdentityType'),(1, 'pFilterkey'),(1, 'pFilterPropVarValue'),)))
    AsyncIIdentityStore.Finish_EnumerateIdentities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(12, 'Finish_EnumerateIdentities', ((1, 'ppIdentityEnum'),)))
    AsyncIIdentityStore.Begin_Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Begin_Reset', ()))
    AsyncIIdentityStore.Finish_Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Finish_Reset', ()))
    return AsyncIIdentityStore
def _define_IIdentityStoreEx_head():
    class IIdentityStoreEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9f9eb98-8f7f-4e38-9577-6980114ce32b')
    return IIdentityStoreEx
def _define_IIdentityStoreEx():
    IIdentityStoreEx = win32more.Security.Authentication.Identity.Provider.IIdentityStoreEx_head
    IIdentityStoreEx.CreateConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(3, 'CreateConnectedIdentity', ((1, 'LocalName'),(1, 'ConnectedName'),(1, 'ProviderGUID'),)))
    IIdentityStoreEx.DeleteConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(4, 'DeleteConnectedIdentity', ((1, 'ConnectedName'),(1, 'ProviderGUID'),)))
    return IIdentityStoreEx
def _define_AsyncIIdentityStoreEx_head():
    class AsyncIIdentityStoreEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('fca3af9a-8a07-4eae-8632-ec3de658a36a')
    return AsyncIIdentityStoreEx
def _define_AsyncIIdentityStoreEx():
    AsyncIIdentityStoreEx = win32more.Security.Authentication.Identity.Provider.AsyncIIdentityStoreEx_head
    AsyncIIdentityStoreEx.Begin_CreateConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(3, 'Begin_CreateConnectedIdentity', ((1, 'LocalName'),(1, 'ConnectedName'),(1, 'ProviderGUID'),)))
    AsyncIIdentityStoreEx.Finish_CreateConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Finish_CreateConnectedIdentity', ()))
    AsyncIIdentityStoreEx.Begin_DeleteConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(5, 'Begin_DeleteConnectedIdentity', ((1, 'ConnectedName'),(1, 'ProviderGUID'),)))
    AsyncIIdentityStoreEx.Finish_DeleteConnectedIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Finish_DeleteConnectedIdentity', ()))
    return AsyncIIdentityStoreEx
__all__ = [
    "OID_OAssociatedIdentityProviderObject",
    "IDENTITY_TYPE",
    "IDENTITIES_ALL",
    "IDENTITIES_ME_ONLY",
    "IdentityUpdateEvent",
    "IDENTITY_ASSOCIATED",
    "IDENTITY_DISASSOCIATED",
    "IDENTITY_CREATED",
    "IDENTITY_IMPORTED",
    "IDENTITY_DELETED",
    "IDENTITY_PROPCHANGED",
    "IDENTITY_CONNECTED",
    "IDENTITY_DISCONNECTED",
    "IIdentityAdvise",
    "AsyncIIdentityAdvise",
    "IIdentityProvider",
    "AsyncIIdentityProvider",
    "IAssociatedIdentityProvider",
    "AsyncIAssociatedIdentityProvider",
    "IDENTITY_URL",
    "IDENTITY_URL_CREATE_ACCOUNT_WIZARD",
    "IDENTITY_URL_SIGN_IN_WIZARD",
    "IDENTITY_URL_CHANGE_PASSWORD_WIZARD",
    "IDENTITY_URL_IFEXISTS_WIZARD",
    "IDENTITY_URL_ACCOUNT_SETTINGS",
    "IDENTITY_URL_RESTORE_WIZARD",
    "IDENTITY_URL_CONNECT_WIZARD",
    "ACCOUNT_STATE",
    "NOT_CONNECTED",
    "CONNECTING",
    "CONNECT_COMPLETED",
    "IConnectedIdentityProvider",
    "AsyncIConnectedIdentityProvider",
    "IIdentityAuthentication",
    "AsyncIIdentityAuthentication",
    "CoClassIdentityStore",
    "CIdentityProfileHandler",
    "IIdentityStore",
    "AsyncIIdentityStore",
    "IIdentityStoreEx",
    "AsyncIIdentityStoreEx",
]
