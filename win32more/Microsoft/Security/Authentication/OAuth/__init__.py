from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Security.Authentication.OAuth
import win32more.Microsoft.UI
import win32more.Windows.Data.Json
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Web.Http
import win32more.Windows.Web.Http.Headers
import win32more.Windows.Win32.System.WinRT
class AuthFailure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure
    _classid_ = 'Microsoft.Security.Authentication.OAuth.AuthFailure'
    @winrt_mixinmethod
    def get_Error(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorDescription(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorUri(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthFailure) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    Error = property(get_Error, None)
    ErrorDescription = property(get_ErrorDescription, None)
    ErrorUri = property(get_ErrorUri, None)
    State = property(get_State, None)
class AuthRequestParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams
    _classid_ = 'Microsoft.Security.Authentication.OAuth.AuthRequestParams'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParamsFactory, responseType: WinRT_String, clientId: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParamsFactory, responseType: WinRT_String, clientId: WinRT_String, redirectUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    @winrt_mixinmethod
    def get_ResponseType(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ResponseType(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClientId(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClientId(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RedirectUri(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RedirectUri(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CodeChallenge(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CodeChallenge(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CodeChallengeMethod(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> win32more.Microsoft.Security.Authentication.OAuth.CodeChallengeMethodKind: ...
    @winrt_mixinmethod
    def put_CodeChallengeMethod(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams, value: win32more.Microsoft.Security.Authentication.OAuth.CodeChallengeMethodKind) -> Void: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParams) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_classmethod
    def CreateForAuthorizationCodeRequest(cls: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParamsStatics, clientId: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    @winrt_classmethod
    def CreateForAuthorizationCodeRequest2(cls: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestParamsStatics, clientId: WinRT_String, redirectUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    AdditionalParams = property(get_AdditionalParams, None)
    ClientId = property(get_ClientId, put_ClientId)
    CodeChallenge = property(get_CodeChallenge, put_CodeChallenge)
    CodeChallengeMethod = property(get_CodeChallengeMethod, put_CodeChallengeMethod)
    RedirectUri = property(get_RedirectUri, put_RedirectUri)
    ResponseType = property(get_ResponseType, put_ResponseType)
    Scope = property(get_Scope, put_Scope)
    State = property(get_State, put_State)
class AuthRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestResult
    _classid_ = 'Microsoft.Security.Authentication.OAuth.AuthRequestResult'
    @winrt_mixinmethod
    def get_ResponseUri(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestResult) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestResult) -> win32more.Microsoft.Security.Authentication.OAuth.AuthResponse: ...
    @winrt_mixinmethod
    def get_Failure(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthRequestResult) -> win32more.Microsoft.Security.Authentication.OAuth.AuthFailure: ...
    Failure = property(get_Failure, None)
    Response = property(get_Response, None)
    ResponseUri = property(get_ResponseUri, None)
class AuthResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse
    _classid_ = 'Microsoft.Security.Authentication.OAuth.AuthResponse'
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Code(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessToken(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TokenType(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpiresIn(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.IAuthResponse) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    AccessToken = property(get_AccessToken, None)
    AdditionalParams = property(get_AdditionalParams, None)
    Code = property(get_Code, None)
    ExpiresIn = property(get_ExpiresIn, None)
    Scope = property(get_Scope, None)
    State = property(get_State, None)
    TokenType = property(get_TokenType, None)
class ClientAuthentication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ClientAuthentication'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthenticationFactory, authorization: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication: ...
    @winrt_mixinmethod
    def get_Authorization(self: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication) -> win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue: ...
    @winrt_mixinmethod
    def put_Authorization(self: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication, value: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyAuthorization(self: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication) -> win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue: ...
    @winrt_mixinmethod
    def put_ProxyAuthorization(self: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication, value: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> Void: ...
    @winrt_mixinmethod
    def get_AdditionalHeaders(self: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthentication) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_classmethod
    def CreateForBasicAuthorization(cls: win32more.Microsoft.Security.Authentication.OAuth.IClientAuthenticationStatics, clientId: WinRT_String, clientSecret: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication: ...
    AdditionalHeaders = property(get_AdditionalHeaders, None)
    Authorization = property(get_Authorization, put_Authorization)
    ProxyAuthorization = property(get_ProxyAuthorization, put_ProxyAuthorization)
class CodeChallengeMethodKind(Enum, Int32):
    None_ = 0
    S256 = 1
    Plain = 2
class IAuthFailure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthFailure'
    _iid_ = Guid('{ec55ed5f-0497-53cb-976b-abd146350175}')
    @winrt_commethod(6)
    def get_Error(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ErrorDescription(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ErrorUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_State(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    Error = property(get_Error, None)
    ErrorDescription = property(get_ErrorDescription, None)
    ErrorUri = property(get_ErrorUri, None)
    State = property(get_State, None)
class IAuthRequestParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthRequestParams'
    _iid_ = Guid('{aac61e23-9155-551a-ac37-cdb2995f88d2}')
    @winrt_commethod(6)
    def get_ResponseType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ResponseType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ClientId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ClientId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RedirectUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_RedirectUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(12)
    def get_State(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_State(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Scope(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_CodeChallenge(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_CodeChallenge(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_CodeChallengeMethod(self) -> win32more.Microsoft.Security.Authentication.OAuth.CodeChallengeMethodKind: ...
    @winrt_commethod(19)
    def put_CodeChallengeMethod(self, value: win32more.Microsoft.Security.Authentication.OAuth.CodeChallengeMethodKind) -> Void: ...
    @winrt_commethod(20)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    ClientId = property(get_ClientId, put_ClientId)
    CodeChallenge = property(get_CodeChallenge, put_CodeChallenge)
    CodeChallengeMethod = property(get_CodeChallengeMethod, put_CodeChallengeMethod)
    RedirectUri = property(get_RedirectUri, put_RedirectUri)
    ResponseType = property(get_ResponseType, put_ResponseType)
    Scope = property(get_Scope, put_Scope)
    State = property(get_State, put_State)
class IAuthRequestParamsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthRequestParamsFactory'
    _iid_ = Guid('{539bdca7-bde4-5a63-85d1-33403f6e3452}')
    @winrt_commethod(6)
    def CreateInstance(self, responseType: WinRT_String, clientId: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    @winrt_commethod(7)
    def CreateInstance2(self, responseType: WinRT_String, clientId: WinRT_String, redirectUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
class IAuthRequestParamsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthRequestParamsStatics'
    _iid_ = Guid('{0befd4f0-6864-5bf4-bd8e-2f3bf98906b5}')
    @winrt_commethod(6)
    def CreateForAuthorizationCodeRequest(self, clientId: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
    @winrt_commethod(7)
    def CreateForAuthorizationCodeRequest2(self, clientId: WinRT_String, redirectUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams: ...
class IAuthRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthRequestResult'
    _iid_ = Guid('{10f8b804-04cf-5651-bd52-7da9346debc1}')
    @winrt_commethod(6)
    def get_ResponseUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Response(self) -> win32more.Microsoft.Security.Authentication.OAuth.AuthResponse: ...
    @winrt_commethod(8)
    def get_Failure(self) -> win32more.Microsoft.Security.Authentication.OAuth.AuthFailure: ...
    Failure = property(get_Failure, None)
    Response = property(get_Response, None)
    ResponseUri = property(get_ResponseUri, None)
class IAuthResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IAuthResponse'
    _iid_ = Guid('{5bc1fa62-fded-5769-9d40-ded1eea90d72}')
    @winrt_commethod(6)
    def get_State(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Code(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AccessToken(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TokenType(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ExpiresIn(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    AccessToken = property(get_AccessToken, None)
    AdditionalParams = property(get_AdditionalParams, None)
    Code = property(get_Code, None)
    ExpiresIn = property(get_ExpiresIn, None)
    Scope = property(get_Scope, None)
    State = property(get_State, None)
    TokenType = property(get_TokenType, None)
class IClientAuthentication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IClientAuthentication'
    _iid_ = Guid('{ef99342d-d597-5eff-878a-8de0cb597172}')
    @winrt_commethod(6)
    def get_Authorization(self) -> win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue: ...
    @winrt_commethod(7)
    def put_Authorization(self, value: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> Void: ...
    @winrt_commethod(8)
    def get_ProxyAuthorization(self) -> win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue: ...
    @winrt_commethod(9)
    def put_ProxyAuthorization(self, value: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> Void: ...
    @winrt_commethod(10)
    def get_AdditionalHeaders(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    AdditionalHeaders = property(get_AdditionalHeaders, None)
    Authorization = property(get_Authorization, put_Authorization)
    ProxyAuthorization = property(get_ProxyAuthorization, put_ProxyAuthorization)
class IClientAuthenticationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IClientAuthenticationFactory'
    _iid_ = Guid('{0d50e9f5-c37f-57cc-b9ec-2b193b0f9cec}')
    @winrt_commethod(6)
    def CreateInstance(self, authorization: win32more.Windows.Web.Http.Headers.HttpCredentialsHeaderValue) -> win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication: ...
class IClientAuthenticationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IClientAuthenticationStatics'
    _iid_ = Guid('{65613560-2b6f-52fd-a479-3a96624682ae}')
    @winrt_commethod(6)
    def CreateForBasicAuthorization(self, clientId: WinRT_String, clientSecret: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication: ...
class IOAuth2ManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.IOAuth2ManagerStatics'
    _iid_ = Guid('{ac9d0dd1-c07e-5302-8150-199c7d343f57}')
    @winrt_commethod(6)
    def RequestAuthWithParamsAsync(self, parentWindowId: win32more.Microsoft.UI.WindowId, authEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.AuthRequestResult]: ...
    @winrt_commethod(7)
    def CompleteAuthRequest(self, responseUri: win32more.Windows.Foundation.Uri) -> Boolean: ...
    @winrt_commethod(8)
    def RequestTokenAsync(self, tokenEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.TokenRequestResult]: ...
    @winrt_commethod(9)
    def RequestTokenAsync2(self, tokenEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams, clientAuth: win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.TokenRequestResult]: ...
class ITokenFailure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenFailure'
    _iid_ = Guid('{60f8d417-ea6a-51d2-8ad7-f0e5177aef0a}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.Security.Authentication.OAuth.TokenFailureKind: ...
    @winrt_commethod(7)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Error(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ErrorDescription(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ErrorUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Data.Json.IJsonValue]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    Error = property(get_Error, None)
    ErrorCode = property(get_ErrorCode, None)
    ErrorDescription = property(get_ErrorDescription, None)
    ErrorUri = property(get_ErrorUri, None)
    Kind = property(get_Kind, None)
class ITokenRequestParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenRequestParams'
    _iid_ = Guid('{49134dbc-aab5-5ba4-bcdf-950214d81182}')
    @winrt_commethod(6)
    def get_GrantType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_GrantType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Code(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Code(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RedirectUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_RedirectUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(12)
    def get_CodeVerifier(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CodeVerifier(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_ClientId(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_ClientId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Username(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_Username(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Password(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_Password(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_Scope(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_RefreshToken(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def put_RefreshToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(24)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    ClientId = property(get_ClientId, put_ClientId)
    Code = property(get_Code, put_Code)
    CodeVerifier = property(get_CodeVerifier, put_CodeVerifier)
    GrantType = property(get_GrantType, put_GrantType)
    Password = property(get_Password, put_Password)
    RedirectUri = property(get_RedirectUri, put_RedirectUri)
    RefreshToken = property(get_RefreshToken, put_RefreshToken)
    Scope = property(get_Scope, put_Scope)
    Username = property(get_Username, put_Username)
class ITokenRequestParamsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenRequestParamsFactory'
    _iid_ = Guid('{2bf39c30-2f30-5788-98d2-a8ba622be809}')
    @winrt_commethod(6)
    def CreateInstance(self, grantType: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
class ITokenRequestParamsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenRequestParamsStatics'
    _iid_ = Guid('{68b7af65-4381-5593-8820-f74a605b9f3b}')
    @winrt_commethod(6)
    def CreateForAuthorizationCodeRequest(self, authResponse: win32more.Microsoft.Security.Authentication.OAuth.AuthResponse) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_commethod(7)
    def CreateForClientCredentials(self) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_commethod(8)
    def CreateForExtension(self, extensionUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_commethod(9)
    def CreateForRefreshToken(self, refreshToken: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
class ITokenRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenRequestResult'
    _iid_ = Guid('{35b31f77-f166-50df-a837-ec0460215166}')
    @winrt_commethod(6)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(7)
    def get_Response(self) -> win32more.Microsoft.Security.Authentication.OAuth.TokenResponse: ...
    @winrt_commethod(8)
    def get_Failure(self) -> win32more.Microsoft.Security.Authentication.OAuth.TokenFailure: ...
    Failure = property(get_Failure, None)
    Response = property(get_Response, None)
    ResponseMessage = property(get_ResponseMessage, None)
class ITokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.ITokenResponse'
    _iid_ = Guid('{9d9d8cd3-04b2-5df6-bfd2-e8a6859745da}')
    @winrt_commethod(6)
    def get_AccessToken(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TokenType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpiresIn(self) -> Double: ...
    @winrt_commethod(9)
    def get_RefreshToken(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Scope(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AdditionalParams(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Data.Json.IJsonValue]: ...
    AccessToken = property(get_AccessToken, None)
    AdditionalParams = property(get_AdditionalParams, None)
    ExpiresIn = property(get_ExpiresIn, None)
    RefreshToken = property(get_RefreshToken, None)
    Scope = property(get_Scope, None)
    TokenType = property(get_TokenType, None)
class OAuth2Manager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Security.Authentication.OAuth.OAuth2Manager'
    @winrt_classmethod
    def RequestAuthWithParamsAsync(cls: win32more.Microsoft.Security.Authentication.OAuth.IOAuth2ManagerStatics, parentWindowId: win32more.Microsoft.UI.WindowId, authEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.AuthRequestParams) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.AuthRequestResult]: ...
    @winrt_classmethod
    def CompleteAuthRequest(cls: win32more.Microsoft.Security.Authentication.OAuth.IOAuth2ManagerStatics, responseUri: win32more.Windows.Foundation.Uri) -> Boolean: ...
    @winrt_classmethod
    def RequestTokenAsync(cls: win32more.Microsoft.Security.Authentication.OAuth.IOAuth2ManagerStatics, tokenEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.TokenRequestResult]: ...
    @winrt_classmethod
    def RequestTokenAsync2(cls: win32more.Microsoft.Security.Authentication.OAuth.IOAuth2ManagerStatics, tokenEndpoint: win32more.Windows.Foundation.Uri, params: win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams, clientAuth: win32more.Microsoft.Security.Authentication.OAuth.ClientAuthentication) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Security.Authentication.OAuth.TokenRequestResult]: ...
OAuthContract: UInt32 = 65536
class TokenFailure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure
    _classid_ = 'Microsoft.Security.Authentication.OAuth.TokenFailure'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> win32more.Microsoft.Security.Authentication.OAuth.TokenFailureKind: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorDescription(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorUri(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenFailure) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Data.Json.IJsonValue]: ...
    AdditionalParams = property(get_AdditionalParams, None)
    Error = property(get_Error, None)
    ErrorCode = property(get_ErrorCode, None)
    ErrorDescription = property(get_ErrorDescription, None)
    ErrorUri = property(get_ErrorUri, None)
    Kind = property(get_Kind, None)
class TokenFailureKind(Enum, Int32):
    ErrorResponse = 0
    HttpFailure = 1
    InvalidResponse = 2
class TokenRequestParams(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams
    _classid_ = 'Microsoft.Security.Authentication.OAuth.TokenRequestParams'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParamsFactory, grantType: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_mixinmethod
    def get_GrantType(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_GrantType(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Code(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Code(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RedirectUri(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RedirectUri(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_CodeVerifier(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CodeVerifier(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ClientId(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ClientId(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Username(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Username(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Password(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RefreshToken(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RefreshToken(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParams) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_classmethod
    def CreateForAuthorizationCodeRequest(cls: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParamsStatics, authResponse: win32more.Microsoft.Security.Authentication.OAuth.AuthResponse) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_classmethod
    def CreateForClientCredentials(cls: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParamsStatics) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_classmethod
    def CreateForExtension(cls: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParamsStatics, extensionUri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    @winrt_classmethod
    def CreateForRefreshToken(cls: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestParamsStatics, refreshToken: WinRT_String) -> win32more.Microsoft.Security.Authentication.OAuth.TokenRequestParams: ...
    AdditionalParams = property(get_AdditionalParams, None)
    ClientId = property(get_ClientId, put_ClientId)
    Code = property(get_Code, put_Code)
    CodeVerifier = property(get_CodeVerifier, put_CodeVerifier)
    GrantType = property(get_GrantType, put_GrantType)
    Password = property(get_Password, put_Password)
    RedirectUri = property(get_RedirectUri, put_RedirectUri)
    RefreshToken = property(get_RefreshToken, put_RefreshToken)
    Scope = property(get_Scope, put_Scope)
    Username = property(get_Username, put_Username)
class TokenRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestResult
    _classid_ = 'Microsoft.Security.Authentication.OAuth.TokenRequestResult'
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestResult) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestResult) -> win32more.Microsoft.Security.Authentication.OAuth.TokenResponse: ...
    @winrt_mixinmethod
    def get_Failure(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenRequestResult) -> win32more.Microsoft.Security.Authentication.OAuth.TokenFailure: ...
    Failure = property(get_Failure, None)
    Response = property(get_Response, None)
    ResponseMessage = property(get_ResponseMessage, None)
class TokenResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse
    _classid_ = 'Microsoft.Security.Authentication.OAuth.TokenResponse'
    @winrt_mixinmethod
    def get_AccessToken(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TokenType(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpiresIn(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> Double: ...
    @winrt_mixinmethod
    def get_RefreshToken(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Scope(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AdditionalParams(self: win32more.Microsoft.Security.Authentication.OAuth.ITokenResponse) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Data.Json.IJsonValue]: ...
    AccessToken = property(get_AccessToken, None)
    AdditionalParams = property(get_AdditionalParams, None)
    ExpiresIn = property(get_ExpiresIn, None)
    RefreshToken = property(get_RefreshToken, None)
    Scope = property(get_Scope, None)
    TokenType = property(get_TokenType, None)


make_ready(__name__)
