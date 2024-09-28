from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Web.Core
import win32more.Windows.Security.Credentials
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class FindAllAccountsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IFindAllAccountsResult
    _classid_ = 'Windows.Security.Authentication.Web.Core.FindAllAccountsResult'
    @winrt_mixinmethod
    def get_Accounts(self: win32more.Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> win32more.Windows.Security.Authentication.Web.Core.FindAllWebAccountsStatus: ...
    @winrt_mixinmethod
    def get_ProviderError(self: win32more.Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    Accounts = property(get_Accounts, None)
    ProviderError = property(get_ProviderError, None)
    Status = property(get_Status, None)
class FindAllWebAccountsStatus(Enum, Int32):
    Success = 0
    NotAllowedByProvider = 1
    NotSupportedByProvider = 2
    ProviderError = 3
class IFindAllAccountsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IFindAllAccountsResult'
    _iid_ = Guid('{a5812b5d-b72e-420c-86ab-aac0d7b7261f}')
    @winrt_commethod(6)
    def get_Accounts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Security.Authentication.Web.Core.FindAllWebAccountsStatus: ...
    @winrt_commethod(8)
    def get_ProviderError(self) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    Accounts = property(get_Accounts, None)
    ProviderError = property(get_ProviderError, None)
    Status = property(get_Status, None)
class IWebAccountEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAccountEventArgs'
    _iid_ = Guid('{6fb7037d-424e-44ec-977c-ef2415462a5a}')
    @winrt_commethod(6)
    def get_Account(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class IWebAccountMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAccountMonitor'
    _iid_ = Guid('{7445f5fd-aa9d-4619-8d5d-c138a4ede3e5}')
    @winrt_commethod(6)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DefaultSignInAccountChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DefaultSignInAccountChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Updated = event()
    Removed = event()
    DefaultSignInAccountChanged = event()
class IWebAccountMonitor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAccountMonitor2'
    _iid_ = Guid('{a7adc1f8-24b8-4f01-9ae5-24545e71233a}')
    @winrt_commethod(6)
    def add_AccountPictureUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountPictureUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AccountPictureUpdated = event()
class IWebAuthenticationAddAccountResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponse'
    _iid_ = Guid('{7fb013e8-0bd8-542b-b486-8323163a4b85}')
    @winrt_commethod(6)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Properties = property(get_Properties, None)
    WebAccount = property(get_WebAccount, None)
class IWebAuthenticationAddAccountResponseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponseFactory'
    _iid_ = Guid('{325f903e-77be-5365-81d9-0321cdd82195}')
    @winrt_commethod(6)
    def CreateWithAccount(self, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse: ...
class IWebAuthenticationAddAccountResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResult'
    _iid_ = Guid('{88fad03c-901d-5ffa-9259-701d3ca08ef2}')
    @winrt_commethod(6)
    def get_ResponseData(self) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountStatus: ...
    @winrt_commethod(8)
    def get_ResponseError(self) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    ResponseData = property(get_ResponseData, None)
    ResponseError = property(get_ResponseError, None)
    ResponseStatus = property(get_ResponseStatus, None)
class IWebAuthenticationCoreManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics'
    _iid_ = Guid('{6aca7c92-a581-4479-9c10-752eff44fd34}')
    @winrt_commethod(6)
    def GetTokenSilentlyAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(7)
    def GetTokenSilentlyWithWebAccountAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(8)
    def RequestTokenAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(9)
    def RequestTokenWithWebAccountAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(10)
    def FindAccountAsync(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, webAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(11)
    def FindAccountProviderAsync(self, webAccountProviderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(12)
    def FindAccountProviderWithAuthorityAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
class IWebAuthenticationCoreManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics2'
    _iid_ = Guid('{f584184a-8b57-4820-b6a4-70a5b6fcf44a}')
    @winrt_commethod(6)
    def FindAccountProviderWithAuthorityForUserAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
class IWebAuthenticationCoreManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics3'
    _iid_ = Guid('{2404eeb2-8924-4d93-ab3a-99688b419d56}')
    @winrt_commethod(6)
    def CreateWebAccountMonitor(self, webAccounts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Credentials.WebAccount]) -> win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor: ...
class IWebAuthenticationCoreManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4'
    _iid_ = Guid('{54e633fe-96e0-41e8-9832-1298897c2aaf}')
    @winrt_commethod(6)
    def FindAllAccountsAsync(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_commethod(7)
    def FindAllAccountsWithClientIdAsync(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, clientId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_commethod(8)
    def FindSystemAccountProviderAsync(self, webAccountProviderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(9)
    def FindSystemAccountProviderWithAuthorityAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(10)
    def FindSystemAccountProviderWithAuthorityForUserAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
class IWebAuthenticationCoreManagerStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics5'
    _iid_ = Guid('{d07c1ded-270f-4554-9966-27b7df05b965}')
    @winrt_commethod(6)
    def AddAccountWithTransferTokenAsync(self, request: win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResult]: ...
class IWebAuthenticationTransferTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest'
    _iid_ = Guid('{7acfa5b6-529d-5e76-9846-f3fd999304d0}')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_TransferToken(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_TransferToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(10)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CorrelationId(self, value: WinRT_String) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    Properties = property(get_Properties, None)
    TransferToken = property(get_TransferToken, put_TransferToken)
    WebAccountProvider = property(get_WebAccountProvider, None)
class IWebAuthenticationTransferTokenRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequestFactory'
    _iid_ = Guid('{5f16b627-04c4-5f0b-8683-8bab58965656}')
    @winrt_commethod(6)
    def Create(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, transferToken: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest: ...
    @winrt_commethod(7)
    def CreateWithCorrelationId(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, transferToken: WinRT_String, correlationId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest: ...
class IWebProviderError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebProviderError'
    _iid_ = Guid('{db191bb1-50c5-4809-8dca-09c99410245c}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ErrorMessage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ErrorCode = property(get_ErrorCode, None)
    ErrorMessage = property(get_ErrorMessage, None)
    Properties = property(get_Properties, None)
class IWebProviderErrorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebProviderErrorFactory'
    _iid_ = Guid('{e3c40a2d-89ef-4e37-847f-a8b9d5a32910}')
    @winrt_commethod(6)
    def Create(self, errorCode: UInt32, errorMessage: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
class IWebTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenRequest'
    _iid_ = Guid('{b77b4d68-adcb-4673-b364-0cf7b35caf97}')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ClientId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PromptType(self) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType: ...
    @winrt_commethod(10)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ClientId = property(get_ClientId, None)
    PromptType = property(get_PromptType, None)
    Properties = property(get_Properties, None)
    Scope = property(get_Scope, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class IWebTokenRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenRequest2'
    _iid_ = Guid('{d700c079-30c8-4397-9654-961c3be8b855}')
    @winrt_commethod(6)
    def get_AppProperties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    AppProperties = property(get_AppProperties, None)
class IWebTokenRequest3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenRequest3'
    _iid_ = Guid('{5a755b51-3bb1-41a5-a63d-90bc32c7db9a}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CorrelationId(self, value: WinRT_String) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
class IWebTokenRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory'
    _iid_ = Guid('{6cf2141c-0ff0-4c67-b84f-99ddbe4a72c9}')
    @winrt_commethod(6)
    def Create(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(7)
    def CreateWithPromptType(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String, promptType: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(8)
    def CreateWithProvider(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(9)
    def CreateWithScope(self, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
class IWebTokenRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenRequestResult'
    _iid_ = Guid('{c12a8305-d1f8-4483-8d54-38fe292784ff}')
    @winrt_commethod(6)
    def get_ResponseData(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse]: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestStatus: ...
    @winrt_commethod(8)
    def get_ResponseError(self) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_commethod(9)
    def InvalidateCacheAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    ResponseData = property(get_ResponseData, None)
    ResponseError = property(get_ResponseError, None)
    ResponseStatus = property(get_ResponseStatus, None)
class IWebTokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenResponse'
    _iid_ = Guid('{67a7c5ca-83f6-44c6-a3b1-0eb69e41fa8a}')
    @winrt_commethod(6)
    def get_Token(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProviderError(self) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_commethod(8)
    def get_WebAccount(self) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(9)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Properties = property(get_Properties, None)
    ProviderError = property(get_ProviderError, None)
    Token = property(get_Token, None)
    WebAccount = property(get_WebAccount, None)
class IWebTokenResponseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory'
    _iid_ = Guid('{ab6bf7f8-5450-4ef6-97f7-052b0431c0f0}')
    @winrt_commethod(6)
    def CreateWithToken(self, token: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_commethod(7)
    def CreateWithTokenAndAccount(self, token: WinRT_String, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_commethod(8)
    def CreateWithTokenAccountAndError(self, token: WinRT_String, webAccount: win32more.Windows.Security.Credentials.WebAccount, error: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
class WebAccountEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebAccountEventArgs
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAccountEventArgs'
    @winrt_mixinmethod
    def get_Account(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountEventArgs) -> win32more.Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class WebAccountMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAccountMonitor'
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DefaultSignInAccountChanged(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DefaultSignInAccountChanged(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountPictureUpdated(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor, win32more.Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountPictureUpdated(self: win32more.Windows.Security.Authentication.Web.Core.IWebAccountMonitor2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Updated = event()
    Removed = event()
    DefaultSignInAccountChanged = event()
    AccountPictureUpdated = event()
class WebAuthenticationAddAccountResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponse
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse.CreateWithAccount(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithAccount(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponseFactory, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse: ...
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponse) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResponse) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Properties = property(get_Properties, None)
    WebAccount = property(get_WebAccount, None)
class WebAuthenticationAddAccountResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResult
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResult'
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResult) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResponse: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResult) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountStatus: ...
    @winrt_mixinmethod
    def get_ResponseError(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationAddAccountResult) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    ResponseData = property(get_ResponseData, None)
    ResponseError = property(get_ResponseError, None)
    ResponseStatus = property(get_ResponseStatus, None)
class WebAuthenticationAddAccountStatus(Enum, Int32):
    Success = 0
    Error = 1
    NotSupportedByProvider = 2
    ServiceConnectionError = 3
    ProviderError = 4
class WebAuthenticationCoreManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAuthenticationCoreManager'
    @winrt_classmethod
    def AddAccountWithTransferTokenAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics5, request: win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationAddAccountResult]: ...
    @winrt_classmethod
    def FindAllAccountsAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, provider: win32more.Windows.Security.Credentials.WebAccountProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_classmethod
    def FindAllAccountsWithClientIdAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, provider: win32more.Windows.Security.Credentials.WebAccountProvider, clientId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_classmethod
    def FindSystemAccountProviderAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindSystemAccountProviderWithAuthorityAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String, authority: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindSystemAccountProviderWithAuthorityForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String, authority: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def CreateWebAccountMonitor(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics3, webAccounts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Security.Credentials.WebAccount]) -> win32more.Windows.Security.Authentication.Web.Core.WebAccountMonitor: ...
    @winrt_classmethod
    def FindAccountProviderWithAuthorityForUserAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics2, webAccountProviderId: WinRT_String, authority: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def GetTokenSilentlyAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def GetTokenSilentlyWithWebAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenWithWebAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def FindAccountAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, provider: win32more.Windows.Security.Credentials.WebAccountProvider, webAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def FindAccountProviderAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, webAccountProviderId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindAccountProviderWithAuthorityAsync(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, webAccountProviderId: WinRT_String, authority: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Credentials.WebAccountProvider]: ...
class WebAuthenticationTransferTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest.CreateWithCorrelationId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider, transferToken: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest: ...
    @winrt_factorymethod
    def CreateWithCorrelationId(cls: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider, transferToken: WinRT_String, correlationId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebAuthenticationTransferTokenRequest: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_TransferToken(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TransferToken(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: win32more.Windows.Security.Authentication.Web.Core.IWebAuthenticationTransferTokenRequest, value: WinRT_String) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    Properties = property(get_Properties, None)
    TransferToken = property(get_TransferToken, put_TransferToken)
    WebAccountProvider = property(get_WebAccountProvider, None)
class WebProviderError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebProviderError
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebProviderError'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebProviderError.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.Authentication.Web.Core.IWebProviderErrorFactory, errorCode: UInt32, errorMessage: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Security.Authentication.Web.Core.IWebProviderError) -> UInt32: ...
    @winrt_mixinmethod
    def get_ErrorMessage(self: win32more.Windows.Security.Authentication.Web.Core.IWebProviderError) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Authentication.Web.Core.IWebProviderError) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ErrorCode = property(get_ErrorCode, None)
    ErrorMessage = property(get_ErrorMessage, None)
    Properties = property(get_Properties, None)
class WebTokenRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebTokenRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest.CreateWithProvider(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest.CreateWithScope(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest.Create(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest.CreateWithPromptType(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithProvider(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def CreateWithScope(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def CreateWithPromptType(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: win32more.Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String, promptType: win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> win32more.Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Scope(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ClientId(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PromptType(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_AppProperties(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest2) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequest3, value: WinRT_String) -> Void: ...
    AppProperties = property(get_AppProperties, None)
    ClientId = property(get_ClientId, None)
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
    PromptType = property(get_PromptType, None)
    Properties = property(get_Properties, None)
    Scope = property(get_Scope, None)
    WebAccountProvider = property(get_WebAccountProvider, None)
class WebTokenRequestPromptType(Enum, Int32):
    Default = 0
    ForceAuthentication = 1
class WebTokenRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestResult
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebTokenRequestResult'
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse]: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenRequestStatus: ...
    @winrt_mixinmethod
    def get_ResponseError(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def InvalidateCacheAsync(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> win32more.Windows.Foundation.IAsyncAction: ...
    ResponseData = property(get_ResponseData, None)
    ResponseError = property(get_ResponseError, None)
    ResponseStatus = property(get_ResponseStatus, None)
class WebTokenRequestStatus(Enum, Int32):
    Success = 0
    UserCancel = 1
    AccountSwitch = 2
    UserInteractionRequired = 3
    AccountProviderNotAvailable = 4
    ProviderError = 5
class WebTokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponse
    _classid_ = 'Windows.Security.Authentication.Web.Core.WebTokenResponse'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse.CreateWithToken(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse.CreateWithTokenAndAccount(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse.CreateWithTokenAccountAndError(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithToken(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithTokenAndAccount(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String, webAccount: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithTokenAccountAndError(cls: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String, webAccount: win32more.Windows.Security.Credentials.WebAccount, error: win32more.Windows.Security.Authentication.Web.Core.WebProviderError) -> win32more.Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_mixinmethod
    def get_Token(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderError(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> win32more.Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def get_WebAccount(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> win32more.Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Properties = property(get_Properties, None)
    ProviderError = property(get_ProviderError, None)
    Token = property(get_Token, None)
    WebAccount = property(get_WebAccount, None)


make_ready(__name__)
