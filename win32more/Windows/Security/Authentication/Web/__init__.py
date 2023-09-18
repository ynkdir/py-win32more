from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Web
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWebAuthenticationBrokerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics'
    _iid_ = Guid('{2f149f1a-e673-40b5-bc22-201a6864a37b}')
    @winrt_commethod(6)
    def AuthenticateWithCallbackUriAsync(self, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri, callbackUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(7)
    def AuthenticateWithoutCallbackUriAsync(self, options: win32more.Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(8)
    def GetCurrentApplicationCallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
class IWebAuthenticationBrokerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Web.IWebAuthenticationResult'
    _iid_ = Guid('{64002b4b-ede9-470a-a5cd-0323faf6e262}')
    @winrt_commethod(6)
    def get_ResponseData(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
    @winrt_commethod(8)
    def get_ResponseErrorDetail(self) -> UInt32: ...
    ResponseData = property(get_ResponseData, None)
    ResponseStatus = property(get_ResponseStatus, None)
    ResponseErrorDetail = property(get_ResponseErrorDetail, None)
TokenBindingKeyType = Int32
TokenBindingKeyType_Rsa2048: TokenBindingKeyType = 0
TokenBindingKeyType_EcdsaP256: TokenBindingKeyType = 1
TokenBindingKeyType_AnyExisting: TokenBindingKeyType = 2
class WebAuthenticationBroker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
WebAuthenticationOptions = UInt32
WebAuthenticationOptions_None: WebAuthenticationOptions = 0
WebAuthenticationOptions_SilentMode: WebAuthenticationOptions = 1
WebAuthenticationOptions_UseTitle: WebAuthenticationOptions = 2
WebAuthenticationOptions_UseHttpPost: WebAuthenticationOptions = 4
WebAuthenticationOptions_UseCorporateNetwork: WebAuthenticationOptions = 8
class WebAuthenticationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult
    _classid_ = 'Windows.Security.Authentication.Web.WebAuthenticationResult'
    @winrt_mixinmethod
    def get_ResponseData(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_ResponseErrorDetail(self: win32more.Windows.Security.Authentication.Web.IWebAuthenticationResult) -> UInt32: ...
    ResponseData = property(get_ResponseData, None)
    ResponseStatus = property(get_ResponseStatus, None)
    ResponseErrorDetail = property(get_ResponseErrorDetail, None)
WebAuthenticationStatus = Int32
WebAuthenticationStatus_Success: WebAuthenticationStatus = 0
WebAuthenticationStatus_UserCancel: WebAuthenticationStatus = 1
WebAuthenticationStatus_ErrorHttp: WebAuthenticationStatus = 2
make_head(_module, 'IWebAuthenticationBrokerStatics')
make_head(_module, 'IWebAuthenticationBrokerStatics2')
make_head(_module, 'IWebAuthenticationResult')
make_head(_module, 'WebAuthenticationBroker')
make_head(_module, 'WebAuthenticationResult')
