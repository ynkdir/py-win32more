from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.System
import win32more.Windows.Web.Http
import win32more.Windows.Web.Http.Filters
import win32more.Windows.Win32.System.WinRT
class HttpBaseProtocolFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter
    _classid_ = 'Windows.Web.Http.Filters.HttpBaseProtocolFilter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
    @winrt_mixinmethod
    def get_AllowAutoRedirect(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowAutoRedirect(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowUI(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowUI(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AutomaticDecompression(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutomaticDecompression(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CacheControl(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Web.Http.Filters.HttpCacheControl: ...
    @winrt_mixinmethod
    def get_CookieManager(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Web.Http.HttpCookieManager: ...
    @winrt_mixinmethod
    def get_ClientCertificate(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def put_ClientCertificate(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorableServerCertificateErrors(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_MaxConnectionsPerServer(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxConnectionsPerServer(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_UseProxy(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseProxy(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVersion(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter2) -> win32more.Windows.Web.Http.HttpVersion: ...
    @winrt_mixinmethod
    def put_MaxVersion(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter2, value: win32more.Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_mixinmethod
    def get_CookieUsageBehavior(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter3) -> win32more.Windows.Web.Http.Filters.HttpCookieUsageBehavior: ...
    @winrt_mixinmethod
    def put_CookieUsageBehavior(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter3, value: win32more.Windows.Web.Http.Filters.HttpCookieUsageBehavior) -> Void: ...
    @winrt_mixinmethod
    def add_ServerCustomValidationRequested(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter, win32more.Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCustomValidationRequested(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ClearAuthenticationCache(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter4) -> Void: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilter5) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def SendRequestAsync(self: win32more.Windows.Web.Http.Filters.IHttpFilter, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForUser(cls: win32more.Windows.Web.Http.Filters.IHttpBaseProtocolFilterStatics, user: win32more.Windows.System.User) -> win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
    AllowAutoRedirect = property(get_AllowAutoRedirect, put_AllowAutoRedirect)
    AllowUI = property(get_AllowUI, put_AllowUI)
    AutomaticDecompression = property(get_AutomaticDecompression, put_AutomaticDecompression)
    CacheControl = property(get_CacheControl, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    CookieManager = property(get_CookieManager, None)
    CookieUsageBehavior = property(get_CookieUsageBehavior, put_CookieUsageBehavior)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    MaxConnectionsPerServer = property(get_MaxConnectionsPerServer, put_MaxConnectionsPerServer)
    MaxVersion = property(get_MaxVersion, put_MaxVersion)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    UseProxy = property(get_UseProxy, put_UseProxy)
    User = property(get_User, None)
    ServerCustomValidationRequested = event()
class HttpCacheControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Filters.IHttpCacheControl
    _classid_ = 'Windows.Web.Http.Filters.HttpCacheControl'
    @winrt_mixinmethod
    def get_ReadBehavior(self: win32more.Windows.Web.Http.Filters.IHttpCacheControl) -> win32more.Windows.Web.Http.Filters.HttpCacheReadBehavior: ...
    @winrt_mixinmethod
    def put_ReadBehavior(self: win32more.Windows.Web.Http.Filters.IHttpCacheControl, value: win32more.Windows.Web.Http.Filters.HttpCacheReadBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_WriteBehavior(self: win32more.Windows.Web.Http.Filters.IHttpCacheControl) -> win32more.Windows.Web.Http.Filters.HttpCacheWriteBehavior: ...
    @winrt_mixinmethod
    def put_WriteBehavior(self: win32more.Windows.Web.Http.Filters.IHttpCacheControl, value: win32more.Windows.Web.Http.Filters.HttpCacheWriteBehavior) -> Void: ...
    ReadBehavior = property(get_ReadBehavior, put_ReadBehavior)
    WriteBehavior = property(get_WriteBehavior, put_WriteBehavior)
class HttpCacheReadBehavior(Enum, Int32):
    Default = 0
    MostRecent = 1
    OnlyFromCache = 2
    NoCache = 3
class HttpCacheWriteBehavior(Enum, Int32):
    Default = 0
    NoCache = 1
class HttpCookieUsageBehavior(Enum, Int32):
    Default = 0
    NoCookies = 1
class HttpServerCustomValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs
    _classid_ = 'Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def Reject(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    RequestMessage = property(get_RequestMessage, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class IHttpBaseProtocolFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilter'
    _iid_ = Guid('{71c89b09-e131-4b54-a53c-eb43ff37e9bb}')
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
    def get_CacheControl(self) -> win32more.Windows.Web.Http.Filters.HttpCacheControl: ...
    @winrt_commethod(13)
    def get_CookieManager(self) -> win32more.Windows.Web.Http.HttpCookieManager: ...
    @winrt_commethod(14)
    def get_ClientCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(15)
    def put_ClientCertificate(self, value: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> Void: ...
    @winrt_commethod(16)
    def get_IgnorableServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(17)
    def get_MaxConnectionsPerServer(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_MaxConnectionsPerServer(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_ProxyCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(20)
    def put_ProxyCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(21)
    def get_ServerCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(22)
    def put_ServerCredential(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(23)
    def get_UseProxy(self) -> Boolean: ...
    @winrt_commethod(24)
    def put_UseProxy(self, value: Boolean) -> Void: ...
    AllowAutoRedirect = property(get_AllowAutoRedirect, put_AllowAutoRedirect)
    AllowUI = property(get_AllowUI, put_AllowUI)
    AutomaticDecompression = property(get_AutomaticDecompression, put_AutomaticDecompression)
    CacheControl = property(get_CacheControl, None)
    ClientCertificate = property(get_ClientCertificate, put_ClientCertificate)
    CookieManager = property(get_CookieManager, None)
    IgnorableServerCertificateErrors = property(get_IgnorableServerCertificateErrors, None)
    MaxConnectionsPerServer = property(get_MaxConnectionsPerServer, put_MaxConnectionsPerServer)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    UseProxy = property(get_UseProxy, put_UseProxy)
class IHttpBaseProtocolFilter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilter2'
    _iid_ = Guid('{2ec30013-9427-4900-a017-fa7da3b5c9ae}')
    @winrt_commethod(6)
    def get_MaxVersion(self) -> win32more.Windows.Web.Http.HttpVersion: ...
    @winrt_commethod(7)
    def put_MaxVersion(self, value: win32more.Windows.Web.Http.HttpVersion) -> Void: ...
    MaxVersion = property(get_MaxVersion, put_MaxVersion)
class IHttpBaseProtocolFilter3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilter3'
    _iid_ = Guid('{d43f4d4c-bd42-43ae-8717-ad2c8f4b2937}')
    @winrt_commethod(6)
    def get_CookieUsageBehavior(self) -> win32more.Windows.Web.Http.Filters.HttpCookieUsageBehavior: ...
    @winrt_commethod(7)
    def put_CookieUsageBehavior(self, value: win32more.Windows.Web.Http.Filters.HttpCookieUsageBehavior) -> Void: ...
    CookieUsageBehavior = property(get_CookieUsageBehavior, put_CookieUsageBehavior)
class IHttpBaseProtocolFilter4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilter4'
    _iid_ = Guid('{9fe36ccf-2983-4893-941f-eb518ca8cef9}')
    @winrt_commethod(6)
    def add_ServerCustomValidationRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter, win32more.Windows.Web.Http.Filters.HttpServerCustomValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCustomValidationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def ClearAuthenticationCache(self) -> Void: ...
    ServerCustomValidationRequested = event()
class IHttpBaseProtocolFilter5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilter5'
    _iid_ = Guid('{416e4993-31e3-4816-bf09-e018ee8dc1f5}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IHttpBaseProtocolFilterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpBaseProtocolFilterStatics'
    _iid_ = Guid('{6d4dee0c-e908-494e-b5a3-1263c9b8242a}')
    @winrt_commethod(6)
    def CreateForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Web.Http.Filters.HttpBaseProtocolFilter: ...
class IHttpCacheControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpCacheControl'
    _iid_ = Guid('{c77e1cb4-3cea-4eb5-ac85-04e186e63ab7}')
    @winrt_commethod(6)
    def get_ReadBehavior(self) -> win32more.Windows.Web.Http.Filters.HttpCacheReadBehavior: ...
    @winrt_commethod(7)
    def put_ReadBehavior(self, value: win32more.Windows.Web.Http.Filters.HttpCacheReadBehavior) -> Void: ...
    @winrt_commethod(8)
    def get_WriteBehavior(self) -> win32more.Windows.Web.Http.Filters.HttpCacheWriteBehavior: ...
    @winrt_commethod(9)
    def put_WriteBehavior(self, value: win32more.Windows.Web.Http.Filters.HttpCacheWriteBehavior) -> Void: ...
    ReadBehavior = property(get_ReadBehavior, put_ReadBehavior)
    WriteBehavior = property(get_WriteBehavior, put_WriteBehavior)
class IHttpFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Web.Http.Filters.IHttpFilter'
    _iid_ = Guid('{a4cb6dd5-0902-439e-bfd7-e12552b165ce}')
    @winrt_commethod(6)
    def SendRequestAsync(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
class IHttpServerCustomValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Filters.IHttpServerCustomValidationRequestedEventArgs'
    _iid_ = Guid('{3165fe32-e7dd-48b7-a361-939c750e63cc}')
    @winrt_commethod(6)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(7)
    def get_ServerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(9)
    def get_ServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(10)
    def get_ServerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_commethod(11)
    def Reject(self) -> Void: ...
    @winrt_commethod(12)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    RequestMessage = property(get_RequestMessage, None)
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)


make_ready(__name__)
