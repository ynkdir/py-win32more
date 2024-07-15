from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Web
import win32more.Windows.Security.Authentication.Web.Core
import win32more.Windows.Security.Authentication.Web.Provider
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Core
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Web.Http
import win32more.Windows.Win32.System.WinRT
class IWebAccountClientView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountClientView'
    _iid_ = Guid('{e7bd66ba-0bc7-4c66-bfd4-65d3082cbca8}')
    @winrt_commethod(6)
    def get_ApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Type(self) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType: ...
    @winrt_commethod(8)
    def get_AccountPairwiseId(self) -> WinRT_String: ...
    AccountPairwiseId = property(get_AccountPairwiseId, None)
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    Type = property(get_Type, None)
class IWebAccountClientViewFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountClientViewFactory'
    _iid_ = Guid('{616d16a4-de22-4855-a326-06cebf2a3f23}')
    @winrt_commethod(6)
    def Create(self, viewType: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType, applicationCallbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView: ...
    @winrt_commethod(7)
    def CreateWithPairwiseId(self, viewType: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType, applicationCallbackUri: win32more.Windows.Foundation.Uri, accountPairwiseId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView: ...
class IWebAccountManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics'
    _iid_ = Guid('{b2e8e1a6-d49a-4032-84bf-1a2847747bf1}')
    @winrt_commethod(6)
    def UpdateWebAccountPropertiesAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, webAccountUserName: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def AddWebAccountAsync(self, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(8)
    def DeleteWebAccountAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def FindAllProviderWebAccountsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]]: ...
    @winrt_commethod(10)
    def PushCookiesAsync(self, uri: win32more.Windows.Foundation.Uri, cookies: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def SetViewAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, view: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ClearViewAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, applicationCallbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def GetViewsAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView]]: ...
    @winrt_commethod(14)
    def SetWebAccountPictureAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, webAccountPicture: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def ClearWebAccountPictureAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
class IWebAccountManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics2'
    _iid_ = Guid('{68a7a829-2d5f-4653-8bb0-bd2fa6bd2d87}')
    @winrt_commethod(6)
    def PullCookiesAsync(self, uriString: WinRT_String, callerPFN: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IWebAccountManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics3'
    _iid_ = Guid('{dd4523a6-8a4f-4aa2-b15e-03f550af1359}')
    @winrt_commethod(6)
    def FindAllProviderWebAccountsForUserAsync(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]]: ...
    @winrt_commethod(7)
    def AddWebAccountForUserAsync(self, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(8)
    def AddWebAccountWithScopeForUserAsync(self, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(9)
    def AddWebAccountWithScopeAndMapForUserAsync(self, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
class IWebAccountManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics4'
    _iid_ = Guid('{59ebc2d2-f7db-412f-bc3f-f2fea04430b4}')
    @winrt_commethod(6)
    def InvalidateAppCacheForAllAccountsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def InvalidateAppCacheForAccountAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
class IWebAccountMapManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountMapManagerStatics'
    _iid_ = Guid('{e8fa446f-3a1b-48a4-8e90-1e59ca6f54db}')
    @winrt_commethod(6)
    def AddWebAccountWithScopeAndMapAsync(self, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(7)
    def SetPerAppToPerUserAccountAsync(self, perAppAccount: win32more.Windows.Security.Credentials.WebAccount, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetPerUserFromPerAppAccountAsync(self, perAppAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(9)
    def ClearPerUserFromPerAppAccountAsync(self, perAppAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
class IWebAccountProviderAddAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderAddAccountOperation'
    _iid_ = Guid('{73ebdccf-4378-4c79-9335-a5d7ab81594e}')
    @winrt_commethod(6)
    def ReportCompleted(self) -> Void: ...
class IWebAccountProviderBaseReportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation'
    _iid_ = Guid('{bba4acbb-993b-4d57-bbe4-1421e3668b4c}')
    @winrt_commethod(6)
    def ReportCompleted(self) -> Void: ...
    @winrt_commethod(7)
    def ReportError(self, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
class IWebAccountProviderDeleteAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderDeleteAccountOperation'
    _iid_ = Guid('{0abb48b8-9e01-49c9-a355-7d48caf7d6ca}')
    @winrt_commethod(6)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    WebAccount = property(get_WebAccount, None)
class IWebAccountProviderManageAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderManageAccountOperation'
    _iid_ = Guid('{ed20dc5c-d21b-463e-a9b7-c1fd0edae978}')
    @winrt_commethod(6)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(7)
    def ReportCompleted(self) -> Void: ...
    WebAccount = property(get_WebAccount, None)
class IWebAccountProviderOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation'
    _iid_ = Guid('{6d5d2426-10b1-419a-a44e-f9c5161574e6}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
class IWebAccountProviderRetrieveCookiesOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation'
    _iid_ = Guid('{5a040441-0fa3-4ab1-a01c-20b110358594}')
    @winrt_commethod(6)
    def get_Context(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Cookies(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Http.HttpCookie]: ...
    @winrt_commethod(8)
    def put_Uri(self, uri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_ApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    Context = property(get_Context, None)
    Cookies = property(get_Cookies, None)
    Uri = property(get_Uri, put_Uri)
class IWebAccountProviderSignOutAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderSignOutAccountOperation'
    _iid_ = Guid('{b890e21d-0c55-47bc-8c72-04a6fc7cac07}')
    @winrt_commethod(6)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(7)
    def get_ApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ClientId(self) -> WinRT_String: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    ClientId = property(get_ClientId, None)
    WebAccount = property(get_WebAccount, None)
class IWebAccountProviderSilentReportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderSilentReportOperation'
    _iid_ = Guid('{e0b545f8-3b0f-44da-924c-7b18baaa62a9}')
    @winrt_commethod(6)
    def ReportUserInteractionRequired(self) -> Void: ...
    @winrt_commethod(7)
    def ReportUserInteractionRequiredWithError(self, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
class IWebAccountProviderTokenObjects(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenObjects'
    _iid_ = Guid('{408f284b-1328-42db-89a4-0bce7a717d8e}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IWebAccountProviderTokenObjects2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenObjects2'
    _iid_ = Guid('{1020b893-5ca5-4fff-95fb-b820273fc395}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IWebAccountProviderTokenOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation'
    _iid_ = Guid('{95c613be-2034-4c38-9434-d26c14b2b4b2}')
    @winrt_commethod(6)
    def get_ProviderRequest(self) -> win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenRequest: ...
    @winrt_commethod(7)
    def get_ProviderResponses(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse]: ...
    @winrt_commethod(8)
    def put_CacheExpirationTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(9)
    def get_CacheExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    CacheExpirationTime = property(get_CacheExpirationTime, put_CacheExpirationTime)
    ProviderRequest = property(get_ProviderRequest, None)
    ProviderResponses = property(get_ProviderResponses, None)
class IWebAccountProviderUIReportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountProviderUIReportOperation'
    _iid_ = Guid('{28ff92d3-8f80-42fb-944f-b2107bbd42e6}')
    @winrt_commethod(6)
    def ReportUserCanceled(self) -> Void: ...
class IWebAccountScopeManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebAccountScopeManagerStatics'
    _iid_ = Guid('{5c6ce37c-12b2-423a-bf3d-85b8d7e53656}')
    @winrt_commethod(6)
    def AddWebAccountWithScopeAsync(self, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(7)
    def SetScopeAsync(self, webAccount: win32more.Windows.Security.Credentials.WebAccount, scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetScope(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope: ...
class IWebProviderTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest'
    _iid_ = Guid('{1e18778b-8805-454b-9f11-468d2af1095a}')
    @winrt_commethod(6)
    def get_ClientRequest(self) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(7)
    def get_WebAccounts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(8)
    def get_WebAccountSelectionOptions(self) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountSelectionOptions: ...
    @winrt_commethod(9)
    def get_ApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def GetApplicationTokenBindingKeyAsync(self, keyType: win32more.Windows.Security.Authentication.Web.TokenBindingKeyType, target: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Core.CryptographicKey]: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    ClientRequest = property(get_ClientRequest, None)
    WebAccountSelectionOptions = property(get_WebAccountSelectionOptions, None)
    WebAccounts = property(get_WebAccounts, None)
class IWebProviderTokenRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest2'
    _iid_ = Guid('{b5d72e4c-10b1-4aa6-88b1-0b6c9e0c1e46}')
    @winrt_commethod(6)
    def GetApplicationTokenBindingKeyIdAsync(self, keyType: win32more.Windows.Security.Authentication.Web.TokenBindingKeyType, target: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
class IWebProviderTokenRequest3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest3'
    _iid_ = Guid('{1b2716aa-4289-446e-9256-dafb6f66a51e}')
    @winrt_commethod(6)
    def get_ApplicationPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ApplicationProcessName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def CheckApplicationForCapabilityAsync(self, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    ApplicationPackageFamilyName = property(get_ApplicationPackageFamilyName, None)
    ApplicationProcessName = property(get_ApplicationProcessName, None)
class IWebProviderTokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebProviderTokenResponse'
    _iid_ = Guid('{ef213793-ef55-4186-b7ce-8cb2e7f9849e}')
    @winrt_commethod(6)
    def get_ClientResponse(self) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    ClientResponse = property(get_ClientResponse, None)
class IWebProviderTokenResponseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.IWebProviderTokenResponseFactory'
    _iid_ = Guid('{fa49d99a-25ba-4077-9cfa-9db4dea7b71a}')
    @winrt_commethod(6)
    def Create(self, webTokenResponse: win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse) -> win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse: ...
class WebAccountClientView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientView
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountClientView'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView.CreateWithPairwiseId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientViewFactory, viewType: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType, applicationCallbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView: ...
    @winrt_factorymethod
    def CreateWithPairwiseId(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientViewFactory, viewType: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType, applicationCallbackUri: win32more.Windows.Foundation.Uri, accountPairwiseId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView: ...
    @winrt_mixinmethod
    def get_ApplicationCallbackUri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientView) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientView) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType: ...
    @winrt_mixinmethod
    def get_AccountPairwiseId(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountClientView) -> WinRT_String: ...
    AccountPairwiseId = property(get_AccountPairwiseId, None)
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    Type = property(get_Type, None)
class WebAccountClientViewType(Enum, Int32):
    IdOnly = 0
    IdAndProperties = 1
class WebAccountManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountManager'
    @winrt_classmethod
    def InvalidateAppCacheForAllAccountsAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics4) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def InvalidateAppCacheForAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics4, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def FindAllProviderWebAccountsForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics3, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]]: ...
    @winrt_classmethod
    def AddWebAccountForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics3, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def AddWebAccountWithScopeForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics3, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def AddWebAccountWithScopeAndMapForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics3, user: win32more.Windows.System.User, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def AddWebAccountWithScopeAndMapAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountMapManagerStatics, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def SetPerAppToPerUserAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountMapManagerStatics, perAppAccount: win32more.Windows.Security.Credentials.WebAccount, perUserWebAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetPerUserFromPerAppAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountMapManagerStatics, perAppAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def ClearPerUserFromPerAppAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountMapManagerStatics, perAppAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AddWebAccountWithScopeAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountScopeManagerStatics, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String], scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def SetScopeAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountScopeManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount, scope: win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetScope(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountScopeManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountScope: ...
    @winrt_classmethod
    def PullCookiesAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics2, uriString: WinRT_String, callerPFN: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def UpdateWebAccountPropertiesAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount, webAccountUserName: WinRT_String, additionalProperties: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AddWebAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccountId: WinRT_String, webAccountUserName: WinRT_String, props: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def DeleteWebAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def FindAllProviderWebAccountsAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]]: ...
    @winrt_classmethod
    def PushCookiesAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, uri: win32more.Windows.Foundation.Uri, cookies: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SetViewAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount, view: win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ClearViewAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount, applicationCallbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetViewsAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Web.Provider.WebAccountClientView]]: ...
    @winrt_classmethod
    def SetWebAccountPictureAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount, webAccountPicture: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ClearWebAccountPictureAsync(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountManagerStatics, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncAction: ...
class WebAccountProviderAddAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderAddAccountOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderAddAccountOperation'
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderAddAccountOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
class WebAccountProviderDeleteAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderDeleteAccountOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderDeleteAccountOperation'
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderDeleteAccountOperation) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    Kind = property(get_Kind, None)
    WebAccount = property(get_WebAccount, None)
class WebAccountProviderGetTokenSilentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderGetTokenSilentOperation'
    @winrt_mixinmethod
    def get_ProviderRequest(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenRequest: ...
    @winrt_mixinmethod
    def get_ProviderResponses(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse]: ...
    @winrt_mixinmethod
    def put_CacheExpirationTime(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_CacheExpirationTime(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    @winrt_mixinmethod
    def ReportUserInteractionRequired(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSilentReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportUserInteractionRequiredWithError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSilentReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    CacheExpirationTime = property(get_CacheExpirationTime, put_CacheExpirationTime)
    Kind = property(get_Kind, None)
    ProviderRequest = property(get_ProviderRequest, None)
    ProviderResponses = property(get_ProviderResponses, None)
class WebAccountProviderManageAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderManageAccountOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderManageAccountOperation'
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderManageAccountOperation) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderManageAccountOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    Kind = property(get_Kind, None)
    WebAccount = property(get_WebAccount, None)
class WebAccountProviderOperationKind(Enum, Int32):
    RequestToken = 0
    GetTokenSilently = 1
    AddAccount = 2
    ManageAccount = 3
    DeleteAccount = 4
    RetrieveCookies = 5
    SignOutAccount = 6
class WebAccountProviderRequestTokenOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderRequestTokenOperation'
    @winrt_mixinmethod
    def get_ProviderRequest(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenRequest: ...
    @winrt_mixinmethod
    def get_ProviderResponses(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse]: ...
    @winrt_mixinmethod
    def put_CacheExpirationTime(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_CacheExpirationTime(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenOperation) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    @winrt_mixinmethod
    def ReportUserCanceled(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderUIReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    CacheExpirationTime = property(get_CacheExpirationTime, put_CacheExpirationTime)
    Kind = property(get_Kind, None)
    ProviderRequest = property(get_ProviderRequest, None)
    ProviderResponses = property(get_ProviderResponses, None)
class WebAccountProviderRetrieveCookiesOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderRetrieveCookiesOperation'
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Cookies(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Http.HttpCookie]: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation, uri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ApplicationCallbackUri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderRetrieveCookiesOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    Context = property(get_Context, None)
    Cookies = property(get_Cookies, None)
    Kind = property(get_Kind, None)
    Uri = property(get_Uri, put_Uri)
class WebAccountProviderSignOutAccountOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSignOutAccountOperation
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderSignOutAccountOperation'
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSignOutAccountOperation) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_ApplicationCallbackUri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSignOutAccountOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ClientId(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderSignOutAccountOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderBaseReportOperation, value: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> Void: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    ClientId = property(get_ClientId, None)
    Kind = property(get_Kind, None)
    WebAccount = property(get_WebAccount, None)
class WebAccountProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenObjects
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebAccountProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenObjects) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderTokenObjects2) -> win32more.Windows.System.User: ...
    Operation = property(get_Operation, None)
    User = property(get_User, None)
class WebAccountScope(Enum, Int32):
    PerUser = 0
    PerApplication = 1
class WebAccountSelectionOptions(Enum, UInt32):
    Default = 0
    New = 1
class WebProviderTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebProviderTokenRequest'
    @winrt_mixinmethod
    def get_ClientRequest(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_mixinmethod
    def get_WebAccounts(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_mixinmethod
    def get_WebAccountSelectionOptions(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest) -> win32more.Windows.Security.Authentication.Web.Provider.WebAccountSelectionOptions: ...
    @winrt_mixinmethod
    def get_ApplicationCallbackUri(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetApplicationTokenBindingKeyAsync(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest, keyType: win32more.Windows.Security.Authentication.Web.TokenBindingKeyType, target: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Cryptography.Core.CryptographicKey]: ...
    @winrt_mixinmethod
    def GetApplicationTokenBindingKeyIdAsync(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest2, keyType: win32more.Windows.Security.Authentication.Web.TokenBindingKeyType, target: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_ApplicationPackageFamilyName(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationProcessName(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest3) -> WinRT_String: ...
    @winrt_mixinmethod
    def CheckApplicationForCapabilityAsync(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenRequest3, capabilityName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    ApplicationCallbackUri = property(get_ApplicationCallbackUri, None)
    ApplicationPackageFamilyName = property(get_ApplicationPackageFamilyName, None)
    ApplicationProcessName = property(get_ApplicationProcessName, None)
    ClientRequest = property(get_ClientRequest, None)
    WebAccountSelectionOptions = property(get_WebAccountSelectionOptions, None)
    WebAccounts = property(get_WebAccounts, None)
class WebProviderTokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenResponse
    _classid_ = 'Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenResponseFactory, webTokenResponse: win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse) -> win32more.Windows.Security.Authentication.Web.Provider.WebProviderTokenResponse: ...
    @winrt_mixinmethod
    def get_ClientResponse(self: win32more.Windows.Security.Authentication.Web.Provider.IWebProviderTokenResponse) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    ClientResponse = property(get_ClientResponse, None)


make_ready(__name__)
