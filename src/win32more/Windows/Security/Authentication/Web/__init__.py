from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Web
class IWebAuthenticationBrokerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics'
    _iid_ = Guid('{2f149f1a-e673-40b5-bc22-201a6864a37b}')
    @winrt_commethod(6)
    def AuthenticateWithCallbackUriAsync(self, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(7)
    def AuthenticateWithoutCallbackUriAsync(self, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(8)
    def GetCurrentApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
class IWebAuthenticationBrokerStatics2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2'
    _iid_ = Guid('{73cdfb9e-14e7-41da-a971-aaf4410b621e}')
    @winrt_commethod(6)
    def AuthenticateAndContinue(self, requestUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def AuthenticateWithCallbackUriAndContinue(self, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def AuthenticateWithCallbackUriContinuationDataAndOptionsAndContinue(self, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri, continuationData: win32more.Windows.Foundation.Collections.ValueSet, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Void: ...
    @winrt_commethod(9)
    def AuthenticateSilentlyAsync(self, requestUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(10)
    def AuthenticateSilentlyWithOptionsAsync(self, requestUri: win32more.Windows.Foundation.Uri, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
class IWebAuthenticationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.IWebAuthenticationResult'
    _iid_ = Guid('{64002b4b-ede9-470a-a5cd-0323faf6e262}')
    @winrt_commethod(6)
    def get_ResponseData(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
    @winrt_commethod(8)
    def get_ResponseErrorDetail(self) -> UInt32: ...
    ResponseData = property(get_ResponseData, None)
    ResponseErrorDetail = property(get_ResponseErrorDetail, None)
    ResponseStatus = property(get_ResponseStatus, None)
class TokenBindingKeyType(Enum, Int32):
    Rsa2048 = 0
    EcdsaP256 = 1
    AnyExisting = 2
class WebAuthenticationBroker(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.WebAuthenticationBroker'
    @winrt_classmethod
    def AuthenticateAndContinue(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriAndContinue(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriContinuationDataAndOptionsAndContinue(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri, continuationData: win32more.Windows.Foundation.Collections.ValueSet, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Void: ...
    @winrt_classmethod
    def AuthenticateSilentlyAsync(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateSilentlyWithOptionsAsync(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: win32more.Windows.Foundation.Uri, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriAsync(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateWithoutCallbackUriAsync(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def GetCurrentApplicationCallbackUri(cls: win32more.Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics) -> win32more.Windows.Foundation.Uri: ...
class WebAuthenticationOptions(Enum, UInt32):
    None_ = 0
    SilentMode = 1
    UseTitle = 2
    UseHttpPost = 4
    UseCorporateNetwork = 8
class WebAuthenticationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult
    _classid_ = 'Windows.Security.Authentication.Web.WebAuthenticationResult'
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_ResponseErrorDetail(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> UInt32: ...
    ResponseData = property(get_ResponseData, None)
    ResponseErrorDetail = property(get_ResponseErrorDetail, None)
    ResponseStatus = property(get_ResponseStatus, None)
class WebAuthenticationStatus(Enum, Int32):
    Success = 0
    UserCancel = 1
    ErrorHttp = 2


make_ready(__name__)
