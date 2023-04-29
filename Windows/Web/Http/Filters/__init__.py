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
import Windows.Networking.Sockets
import Windows.Security.Credentials
import Windows.Security.Cryptography.Certificates
import Windows.System
import Windows.Web.Http
import Windows.Web.Http.Filters
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HttpBaseProtocolFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.Http.Filters.HttpBaseProtocolFilter'
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
    @winrt_mixinmethod
    def get_AllowAutoRedirect(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowAutoRedirect(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowUI(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowUI(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutomaticDecompression(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutomaticDecompression(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CacheControl(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Web.Http.Filters.HttpCacheControl: ...
    @winrt_mixinmethod
    def get_CookieManager(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Web.Http.HttpCookieManager: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_MaxConnectionsPerServer(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxConnectionsPerServer(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_UseProxy(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseProxy(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVersion(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter2) -> Windows.Web.Http.HttpVersion: ...
    @winrt_mixinmethod
    def put_MaxVersion(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter2, value: Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_mixinmethod
    def get_CookieUsageBehavior(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter3) -> Windows.Web.Http.Filters.HttpCookieUsageBehavior: ...
    @winrt_mixinmethod
    def put_CookieUsageBehavior(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter3, value: Windows.Web.Http.Filters.HttpCookieUsageBehavior) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter4, handler: Windows.Foundation.TypedEventHandler[Windows.Web.Http.Filters.HttpBaseProtocolFilter, Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ClearAuthenticationCache(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter4) -> Void: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Web.Http.Filters.IHttpBaseProtocolFilter5) -> Windows.System.User: ...
    @winrt_mixinmethod
    def SendRequestAsync(self: Windows.Web.Http.Filters.IHttpFilter, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForUser(cls: Windows.Web.Http.Filters.IHttpBaseProtocolFilterStatics, user: Windows.System.User) -> Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
    AllowAutoRedirect = property(get_AllowAutoRedirect, put_AllowAutoRedirect)
    AllowUI = property(get_AllowUI, put_AllowUI)
    AutomaticDecompression = property(get_AutomaticDecompression, put_AutomaticDecompression)
    CacheControl = property(get_CacheControl, None)
    CookieManager = property(get_CookieManager, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    MaxConnectionsPerServer = property(get_MaxConnectionsPerServer, put_MaxConnectionsPerServer)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    UseProxy = property(get_UseProxy, put_UseProxy)
    MaxVersion = property(get_MaxVersion, put_MaxVersion)
    CookieUsageBehavior = property(get_CookieUsageBehavior, put_CookieUsageBehavior)
    User = property(get_User, None)
class HttpCacheControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.Http.Filters.HttpCacheControl'
    @winrt_mixinmethod
    def get_ReadBehavior(self: Windows.Web.Http.Filters.IHttpCacheControl) -> Windows.Web.Http.Filters.HttpCacheReadBehavior: ...
    @winrt_mixinmethod
    def put_ReadBehavior(self: Windows.Web.Http.Filters.IHttpCacheControl, value: Windows.Web.Http.Filters.HttpCacheReadBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_WriteBehavior(self: Windows.Web.Http.Filters.IHttpCacheControl) -> Windows.Web.Http.Filters.HttpCacheWriteBehavior: ...
    @winrt_mixinmethod
    def put_WriteBehavior(self: Windows.Web.Http.Filters.IHttpCacheControl, value: Windows.Web.Http.Filters.HttpCacheWriteBehavior) -> Void: ...
    ReadBehavior = property(get_ReadBehavior, put_ReadBehavior)
    WriteBehavior = property(get_WriteBehavior, put_WriteBehavior)
HttpCacheReadBehavior = Int32
HttpCacheReadBehavior_Default: HttpCacheReadBehavior = 0
HttpCacheReadBehavior_MostRecent: HttpCacheReadBehavior = 1
HttpCacheReadBehavior_OnlyFromCache: HttpCacheReadBehavior = 2
HttpCacheReadBehavior_NoCache: HttpCacheReadBehavior = 3
HttpCacheWriteBehavior = Int32
HttpCacheWriteBehavior_Default: HttpCacheWriteBehavior = 0
HttpCacheWriteBehavior_NoCache: HttpCacheWriteBehavior = 1
HttpCookieUsageBehavior = Int32
HttpCookieUsageBehavior_Default: HttpCookieUsageBehavior = 0
HttpCookieUsageBehavior_NoCookies: HttpCookieUsageBehavior = 1
class HttpServerCustomValidationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Reject(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    RequestMessage = property(get_RequestMessage, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IHttpBaseProtocolFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71c89b09-e131-4b54-a5-3c-eb-43-ff-37-e9-bb')
    @winrt_commethod(6)
    def get_AllowAutoRedirect(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowAutoRedirect(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AllowUI(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AllowUI(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_AutomaticDecompression(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AutomaticDecompression(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_CacheControl(self) -> Windows.Web.Http.Filters.HttpCacheControl: ...
    @winrt_commethod(13)
    def get_CookieManager(self) -> Windows.Web.Http.HttpCookieManager: ...
    @winrt_commethod(14)
    def get_ClientCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(15)
    def put_ClientCertificate(self, value: Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(16)
    def get_IgnorableServerCertificateErrors(self) -> Windows.Foundation.Collections.IVector[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(17)
    def get_MaxConnectionsPerServer(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_MaxConnectionsPerServer(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_ProxyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(20)
    def put_ProxyCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(21)
    def get_ServerCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(22)
    def put_ServerCredential(self, value: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(23)
    def get_UseProxy(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_UseProxy(self, value: Boolean) -> Void: ...
    AllowAutoRedirect = property(get_AllowAutoRedirect, put_AllowAutoRedirect)
    AllowUI = property(get_AllowUI, put_AllowUI)
    AutomaticDecompression = property(get_AutomaticDecompression, put_AutomaticDecompression)
    CacheControl = property(get_CacheControl, None)
    CookieManager = property(get_CookieManager, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    MaxConnectionsPerServer = property(get_MaxConnectionsPerServer, put_MaxConnectionsPerServer)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    UseProxy = property(get_UseProxy, put_UseProxy)
class IHttpBaseProtocolFilter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2ec30013-9427-4900-a0-17-fa-7d-a3-b5-c9-ae')
    @winrt_commethod(6)
    def get_MaxVersion(self) -> Windows.Web.Http.HttpVersion: ...
    @winrt_commethod(7)
    def put_MaxVersion(self, value: Windows.Web.Http.HttpVersion) -> Void: ...
    MaxVersion = property(get_MaxVersion, put_MaxVersion)
class IHttpBaseProtocolFilter3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d43f4d4c-bd42-43ae-87-17-ad-2c-8f-4b-29-37')
    @winrt_commethod(6)
    def get_CookieUsageBehavior(self) -> Windows.Web.Http.Filters.HttpCookieUsageBehavior: ...
    @winrt_commethod(7)
    def put_CookieUsageBehavior(self, value: Windows.Web.Http.Filters.HttpCookieUsageBehavior) -> Void: ...
    CookieUsageBehavior = property(get_CookieUsageBehavior, put_CookieUsageBehavior)
class IHttpBaseProtocolFilter4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9fe36ccf-2983-4893-94-1f-eb-51-8c-a8-ce-f9')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.Http.Filters.HttpBaseProtocolFilter, Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def ClearAuthenticationCache(self) -> Void: ...
class IHttpBaseProtocolFilter5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('416e4993-31e3-4816-bf-09-e0-18-ee-8d-c1-f5')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IHttpBaseProtocolFilterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6d4dee0c-e908-494e-b5-a3-12-63-c9-b8-24-2a')
    @winrt_commethod(6)
    def CreateForUser(self, user: Windows.System.User) -> Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
class IHttpCacheControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c77e1cb4-3cea-4eb5-ac-85-04-e1-86-e6-3a-b7')
    @winrt_commethod(6)
    def get_ReadBehavior(self) -> Windows.Web.Http.Filters.HttpCacheReadBehavior: ...
    @winrt_commethod(7)
    def put_ReadBehavior(self, value: Windows.Web.Http.Filters.HttpCacheReadBehavior) -> Void: ...
    @winrt_commethod(8)
    def get_WriteBehavior(self) -> Windows.Web.Http.Filters.HttpCacheWriteBehavior: ...
    @winrt_commethod(9)
    def put_WriteBehavior(self, value: Windows.Web.Http.Filters.HttpCacheWriteBehavior) -> Void: ...
    ReadBehavior = property(get_ReadBehavior, put_ReadBehavior)
    WriteBehavior = property(get_WriteBehavior, put_WriteBehavior)
class IHttpFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4cb6dd5-0902-439e-bf-d7-e1-25-52-b1-65-ce')
    @winrt_commethod(6)
    def SendRequestAsync(self, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
class IHttpServerCustomValidationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3165fe32-e7dd-48b7-a3-61-93-9c-75-0e-63-cc')
    @winrt_commethod(6)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(7)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(9)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(10)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(11)
    def Reject(self) -> Void: ...
    @winrt_commethod(12)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    RequestMessage = property(get_RequestMessage, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
make_head(_module, 'HttpBaseProtocolFilter')
make_head(_module, 'HttpCacheControl')
make_head(_module, 'HttpServerCustomValidationRequestedEventArgs')
make_head(_module, 'IHttpBaseProtocolFilter')
make_head(_module, 'IHttpBaseProtocolFilter2')
make_head(_module, 'IHttpBaseProtocolFilter3')
make_head(_module, 'IHttpBaseProtocolFilter4')
make_head(_module, 'IHttpBaseProtocolFilter5')
make_head(_module, 'IHttpBaseProtocolFilterStatics')
make_head(_module, 'IHttpCacheControl')
make_head(_module, 'IHttpFilter')
make_head(_module, 'IHttpServerCustomValidationRequestedEventArgs')
