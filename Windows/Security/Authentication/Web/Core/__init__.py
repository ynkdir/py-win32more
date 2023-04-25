from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authentication.Web.Core
import Windows.Security.Credentials
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class FindAllAccountsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.FindAllAccountsResult'
    @winrt_mixinmethod
    def get_Accounts(self: Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.WebAccount]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> Windows.Security.Authentication.Web.Core.FindAllWebAccountsStatus: ...
    @winrt_mixinmethod
    def get_ProviderError(self: Windows.Security.Authentication.Web.Core.IFindAllAccountsResult) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    Accounts = property(get_Accounts, None)
    Status = property(get_Status, None)
    ProviderError = property(get_ProviderError, None)
FindAllWebAccountsStatus = Int32
FindAllWebAccountsStatus_Success: FindAllWebAccountsStatus = 0
FindAllWebAccountsStatus_NotAllowedByProvider: FindAllWebAccountsStatus = 1
FindAllWebAccountsStatus_NotSupportedByProvider: FindAllWebAccountsStatus = 2
FindAllWebAccountsStatus_ProviderError: FindAllWebAccountsStatus = 3
class IFindAllAccountsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a5812b5d-b72e-420c-86-ab-aa-c0-d7-b7-26-1f')
    @winrt_commethod(6)
    def get_Accounts(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Security.Authentication.Web.Core.FindAllWebAccountsStatus: ...
    @winrt_commethod(8)
    def get_ProviderError(self) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    Accounts = property(get_Accounts, None)
    Status = property(get_Status, None)
    ProviderError = property(get_ProviderError, None)
class IWebAccountEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6fb7037d-424e-44ec-97-7c-ef-24-15-46-2a-5a')
    @winrt_commethod(6)
    def get_Account(self) -> Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class IWebAccountMonitor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7445f5fd-aa9d-4619-8d-5d-c1-38-a4-ed-e3-e5')
    @winrt_commethod(6)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DefaultSignInAccountChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DefaultSignInAccountChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebAccountMonitor2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a7adc1f8-24b8-4f01-9a-e5-24-54-5e-71-23-3a')
    @winrt_commethod(6)
    def add_AccountPictureUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountPictureUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebAuthenticationCoreManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6aca7c92-a581-4479-9c-10-75-2e-ff-44-fd-34')
    @winrt_commethod(6)
    def GetTokenSilentlyAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(7)
    def GetTokenSilentlyWithWebAccountAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(8)
    def RequestTokenAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(9)
    def RequestTokenWithWebAccountAsync(self, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_commethod(10)
    def FindAccountAsync(self, provider: Windows.Security.Credentials.WebAccountProvider, webAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccount]: ...
    @winrt_commethod(11)
    def FindAccountProviderAsync(self, webAccountProviderId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(12)
    def FindAccountProviderWithAuthorityAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
class IWebAuthenticationCoreManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f584184a-8b57-4820-b6-a4-70-a5-b6-fc-f4-4a')
    @winrt_commethod(6)
    def FindAccountProviderWithAuthorityForUserAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
class IWebAuthenticationCoreManagerStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2404eeb2-8924-4d93-ab-3a-99-68-8b-41-9d-56')
    @winrt_commethod(6)
    def CreateWebAccountMonitor(self, webAccounts: Windows.Foundation.Collections.IIterable[Windows.Security.Credentials.WebAccount]) -> Windows.Security.Authentication.Web.Core.WebAccountMonitor: ...
class IWebAuthenticationCoreManagerStatics4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('54e633fe-96e0-41e8-98-32-12-98-89-7c-2a-af')
    @winrt_commethod(6)
    def FindAllAccountsAsync(self, provider: Windows.Security.Credentials.WebAccountProvider) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_commethod(7)
    def FindAllAccountsWithClientIdAsync(self, provider: Windows.Security.Credentials.WebAccountProvider, clientId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_commethod(8)
    def FindSystemAccountProviderAsync(self, webAccountProviderId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(9)
    def FindSystemAccountProviderWithAuthorityAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_commethod(10)
    def FindSystemAccountProviderWithAuthorityForUserAsync(self, webAccountProviderId: WinRT_String, authority: WinRT_String, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
class IWebProviderError(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db191bb1-50c5-4809-8d-ca-09-c9-94-10-24-5c')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ErrorMessage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ErrorCode = property(get_ErrorCode, None)
    ErrorMessage = property(get_ErrorMessage, None)
    Properties = property(get_Properties, None)
class IWebProviderErrorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3c40a2d-89ef-4e37-84-7f-a8-b9-d5-a3-29-10')
    @winrt_commethod(6)
    def Create(self, errorCode: UInt32, errorMessage: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
class IWebTokenRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b77b4d68-adcb-4673-b3-64-0c-f7-b3-5c-af-97')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ClientId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PromptType(self) -> Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    Scope = property(get_Scope, None)
    ClientId = property(get_ClientId, None)
    PromptType = property(get_PromptType, None)
    Properties = property(get_Properties, None)
class IWebTokenRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d700c079-30c8-4397-96-54-96-1c-3b-e8-b8-55')
    @winrt_commethod(6)
    def get_AppProperties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    AppProperties = property(get_AppProperties, None)
class IWebTokenRequest3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5a755b51-3bb1-41a5-a6-3d-90-bc-32-c7-db-9a')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_CorrelationId(self, value: WinRT_String) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
class IWebTokenRequestFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6cf2141c-0ff0-4c67-b8-4f-99-dd-be-4a-72-c9')
    @winrt_commethod(6)
    def Create(self, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(7)
    def CreateWithPromptType(self, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String, promptType: Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(8)
    def CreateWithProvider(self, provider: Windows.Security.Credentials.WebAccountProvider) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_commethod(9)
    def CreateWithScope(self, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
class IWebTokenRequestResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c12a8305-d1f8-4483-8d-54-38-fe-29-27-84-ff')
    @winrt_commethod(6)
    def get_ResponseData(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Web.Core.WebTokenResponse]: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> Windows.Security.Authentication.Web.Core.WebTokenRequestStatus: ...
    @winrt_commethod(8)
    def get_ResponseError(self) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_commethod(9)
    def InvalidateCacheAsync(self) -> Windows.Foundation.IAsyncAction: ...
    ResponseData = property(get_ResponseData, None)
    ResponseStatus = property(get_ResponseStatus, None)
    ResponseError = property(get_ResponseError, None)
class IWebTokenResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('67a7c5ca-83f6-44c6-a3-b1-0e-b6-9e-41-fa-8a')
    @winrt_commethod(6)
    def get_Token(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProviderError(self) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_commethod(8)
    def get_WebAccount(self) -> Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(9)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Token = property(get_Token, None)
    ProviderError = property(get_ProviderError, None)
    WebAccount = property(get_WebAccount, None)
    Properties = property(get_Properties, None)
class IWebTokenResponseFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab6bf7f8-5450-4ef6-97-f7-05-2b-04-31-c0-f0')
    @winrt_commethod(6)
    def CreateWithToken(self, token: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_commethod(7)
    def CreateWithTokenAndAccount(self, token: WinRT_String, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_commethod(8)
    def CreateWithTokenAccountAndError(self, token: WinRT_String, webAccount: Windows.Security.Credentials.WebAccount, error: Windows.Security.Authentication.Web.Core.WebProviderError) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
class WebAccountEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebAccountEventArgs'
    @winrt_mixinmethod
    def get_Account(self: Windows.Security.Authentication.Web.Core.IWebAccountEventArgs) -> Windows.Security.Credentials.WebAccount: ...
    Account = property(get_Account, None)
class WebAccountMonitor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebAccountMonitor'
    @winrt_mixinmethod
    def add_Updated(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DefaultSignInAccountChanged(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DefaultSignInAccountChanged(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AccountPictureUpdated(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor2, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authentication.Web.Core.WebAccountMonitor, Windows.Security.Authentication.Web.Core.WebAccountEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountPictureUpdated(self: Windows.Security.Authentication.Web.Core.IWebAccountMonitor2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class WebAuthenticationCoreManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebAuthenticationCoreManager'
    @winrt_classmethod
    def FindAllAccountsAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, provider: Windows.Security.Credentials.WebAccountProvider) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_classmethod
    def FindAllAccountsWithClientIdAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, provider: Windows.Security.Credentials.WebAccountProvider, clientId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.FindAllAccountsResult]: ...
    @winrt_classmethod
    def FindSystemAccountProviderAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindSystemAccountProviderWithAuthorityAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String, authority: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindSystemAccountProviderWithAuthorityForUserAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics4, webAccountProviderId: WinRT_String, authority: WinRT_String, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def CreateWebAccountMonitor(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics3, webAccounts: Windows.Foundation.Collections.IIterable[Windows.Security.Credentials.WebAccount]) -> Windows.Security.Authentication.Web.Core.WebAccountMonitor: ...
    @winrt_classmethod
    def FindAccountProviderWithAuthorityForUserAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics2, webAccountProviderId: WinRT_String, authority: WinRT_String, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def GetTokenSilentlyAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: Windows.Security.Authentication.Web.Core.WebTokenRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def GetTokenSilentlyWithWebAccountAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: Windows.Security.Authentication.Web.Core.WebTokenRequest) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenWithWebAccountAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, request: Windows.Security.Authentication.Web.Core.WebTokenRequest, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.Core.WebTokenRequestResult]: ...
    @winrt_classmethod
    def FindAccountAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, provider: Windows.Security.Credentials.WebAccountProvider, webAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccount]: ...
    @winrt_classmethod
    def FindAccountProviderAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, webAccountProviderId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
    @winrt_classmethod
    def FindAccountProviderWithAuthorityAsync(cls: Windows.Security.Authentication.Web.Core.IWebAuthenticationCoreManagerStatics, webAccountProviderId: WinRT_String, authority: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Credentials.WebAccountProvider]: ...
class WebProviderError(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebProviderError'
    @winrt_factorymethod
    def Create(cls: Windows.Security.Authentication.Web.Core.IWebProviderErrorFactory, errorCode: UInt32, errorMessage: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Security.Authentication.Web.Core.IWebProviderError) -> UInt32: ...
    @winrt_mixinmethod
    def get_ErrorMessage(self: Windows.Security.Authentication.Web.Core.IWebProviderError) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Security.Authentication.Web.Core.IWebProviderError) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    ErrorCode = property(get_ErrorCode, None)
    ErrorMessage = property(get_ErrorMessage, None)
    Properties = property(get_Properties, None)
class WebTokenRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebTokenRequest'
    @winrt_factorymethod
    def Create(cls: Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def CreateWithPromptType(cls: Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String, clientId: WinRT_String, promptType: Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def CreateWithProvider(cls: Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: Windows.Security.Credentials.WebAccountProvider) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_factorymethod
    def CreateWithScope(cls: Windows.Security.Authentication.Web.Core.IWebTokenRequestFactory, provider: Windows.Security.Credentials.WebAccountProvider, scope: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenRequest: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Scope(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ClientId(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PromptType(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_AppProperties(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest2) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: Windows.Security.Authentication.Web.Core.IWebTokenRequest3, value: WinRT_String) -> Void: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    Scope = property(get_Scope, None)
    ClientId = property(get_ClientId, None)
    PromptType = property(get_PromptType, None)
    Properties = property(get_Properties, None)
    AppProperties = property(get_AppProperties, None)
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
WebTokenRequestPromptType = Int32
WebTokenRequestPromptType_Default: WebTokenRequestPromptType = 0
WebTokenRequestPromptType_ForceAuthentication: WebTokenRequestPromptType = 1
class WebTokenRequestResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebTokenRequestResult'
    @winrt_mixinmethod
    def get_ResponseData(self: Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Web.Core.WebTokenResponse]: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> Windows.Security.Authentication.Web.Core.WebTokenRequestStatus: ...
    @winrt_mixinmethod
    def get_ResponseError(self: Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def InvalidateCacheAsync(self: Windows.Security.Authentication.Web.Core.IWebTokenRequestResult) -> Windows.Foundation.IAsyncAction: ...
    ResponseData = property(get_ResponseData, None)
    ResponseStatus = property(get_ResponseStatus, None)
    ResponseError = property(get_ResponseError, None)
WebTokenRequestStatus = Int32
WebTokenRequestStatus_Success: WebTokenRequestStatus = 0
WebTokenRequestStatus_UserCancel: WebTokenRequestStatus = 1
WebTokenRequestStatus_AccountSwitch: WebTokenRequestStatus = 2
WebTokenRequestStatus_UserInteractionRequired: WebTokenRequestStatus = 3
WebTokenRequestStatus_AccountProviderNotAvailable: WebTokenRequestStatus = 4
WebTokenRequestStatus_ProviderError: WebTokenRequestStatus = 5
class WebTokenResponse(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.Core.WebTokenResponse'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithToken(cls: Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithTokenAndAccount(cls: Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String, webAccount: Windows.Security.Credentials.WebAccount) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_factorymethod
    def CreateWithTokenAccountAndError(cls: Windows.Security.Authentication.Web.Core.IWebTokenResponseFactory, token: WinRT_String, webAccount: Windows.Security.Credentials.WebAccount, error: Windows.Security.Authentication.Web.Core.WebProviderError) -> Windows.Security.Authentication.Web.Core.WebTokenResponse: ...
    @winrt_mixinmethod
    def get_Token(self: Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProviderError(self: Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> Windows.Security.Authentication.Web.Core.WebProviderError: ...
    @winrt_mixinmethod
    def get_WebAccount(self: Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Security.Authentication.Web.Core.IWebTokenResponse) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Token = property(get_Token, None)
    ProviderError = property(get_ProviderError, None)
    WebAccount = property(get_WebAccount, None)
    Properties = property(get_Properties, None)
make_head(_module, 'FindAllAccountsResult')
make_head(_module, 'IFindAllAccountsResult')
make_head(_module, 'IWebAccountEventArgs')
make_head(_module, 'IWebAccountMonitor')
make_head(_module, 'IWebAccountMonitor2')
make_head(_module, 'IWebAuthenticationCoreManagerStatics')
make_head(_module, 'IWebAuthenticationCoreManagerStatics2')
make_head(_module, 'IWebAuthenticationCoreManagerStatics3')
make_head(_module, 'IWebAuthenticationCoreManagerStatics4')
make_head(_module, 'IWebProviderError')
make_head(_module, 'IWebProviderErrorFactory')
make_head(_module, 'IWebTokenRequest')
make_head(_module, 'IWebTokenRequest2')
make_head(_module, 'IWebTokenRequest3')
make_head(_module, 'IWebTokenRequestFactory')
make_head(_module, 'IWebTokenRequestResult')
make_head(_module, 'IWebTokenResponse')
make_head(_module, 'IWebTokenResponseFactory')
make_head(_module, 'WebAccountEventArgs')
make_head(_module, 'WebAccountMonitor')
make_head(_module, 'WebAuthenticationCoreManager')
make_head(_module, 'WebProviderError')
make_head(_module, 'WebTokenRequest')
make_head(_module, 'WebTokenRequestResult')
make_head(_module, 'WebTokenResponse')
