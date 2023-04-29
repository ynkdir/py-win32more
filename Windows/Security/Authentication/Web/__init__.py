from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authentication.Web
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
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f149f1a-e673-40b5-bc-22-20-1a-68-64-a3-7b')
    @winrt_commethod(6)
    def AuthenticateWithCallbackUriAsync(self, options: Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(7)
    def AuthenticateWithoutCallbackUriAsync(self, options: Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(8)
    def GetCurrentApplicationCallbackUri(self) -> Windows.Foundation.Uri: ...
class IWebAuthenticationBrokerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('73cdfb9e-14e7-41da-a9-71-aa-f4-41-0b-62-1e')
    @winrt_commethod(6)
    def AuthenticateAndContinue(self, requestUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def AuthenticateWithCallbackUriAndContinue(self, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def AuthenticateWithCallbackUriContinuationDataAndOptionsAndContinue(self, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri, continuationData: Windows.Foundation.Collections.ValueSet, options: Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Void: ...
    @winrt_commethod(9)
    def AuthenticateSilentlyAsync(self, requestUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_commethod(10)
    def AuthenticateSilentlyWithOptionsAsync(self, requestUri: Windows.Foundation.Uri, options: Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
class IWebAuthenticationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64002b4b-ede9-470a-a5-cd-03-23-fa-f6-e2-62')
    @winrt_commethod(6)
    def get_ResponseData(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ResponseStatus(self) -> Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.WebAuthenticationBroker'
    @winrt_classmethod
    def AuthenticateAndContinue(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriAndContinue(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriContinuationDataAndOptionsAndContinue(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri, continuationData: Windows.Foundation.Collections.ValueSet, options: Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Void: ...
    @winrt_classmethod
    def AuthenticateSilentlyAsync(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateSilentlyWithOptionsAsync(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics2, requestUri: Windows.Foundation.Uri, options: Windows.Security.Authentication.Web.WebAuthenticationOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateWithCallbackUriAsync(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics, options: Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: Windows.Foundation.Uri, callbackUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def AuthenticateWithoutCallbackUriAsync(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics, options: Windows.Security.Authentication.Web.WebAuthenticationOptions, requestUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authentication.Web.WebAuthenticationResult]: ...
    @winrt_classmethod
    def GetCurrentApplicationCallbackUri(cls: Windows.Security.Authentication.Web.IWebAuthenticationBrokerStatics) -> Windows.Foundation.Uri: ...
WebAuthenticationOptions = UInt32
WebAuthenticationOptions_None: WebAuthenticationOptions = 0
WebAuthenticationOptions_SilentMode: WebAuthenticationOptions = 1
WebAuthenticationOptions_UseTitle: WebAuthenticationOptions = 2
WebAuthenticationOptions_UseHttpPost: WebAuthenticationOptions = 4
WebAuthenticationOptions_UseCorporateNetwork: WebAuthenticationOptions = 8
class WebAuthenticationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Authentication.Web.WebAuthenticationResult'
    @winrt_mixinmethod
    def get_ResponseData(self: Windows.Security.Authentication.Web.IWebAuthenticationResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResponseStatus(self: Windows.Security.Authentication.Web.IWebAuthenticationResult) -> Windows.Security.Authentication.Web.WebAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_ResponseErrorDetail(self: Windows.Security.Authentication.Web.IWebAuthenticationResult) -> UInt32: ...
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
