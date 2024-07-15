from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.Web.Http
import win32more.Windows.Web.Http.Filters
import win32more.Windows.Web.Http.Headers
import win32more.Windows.Win32.System.WinRT
class HttpBufferContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpBufferContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpBufferContent.CreateFromBuffer(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Web.Http.HttpBufferContent.CreateFromBufferWithOffset(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromBuffer(cls: win32more.Windows.Web.Http.IHttpBufferContentFactory, content: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Web.Http.HttpBufferContent: ...
    @winrt_factorymethod
    def CreateFromBufferWithOffset(cls: win32more.Windows.Web.Http.IHttpBufferContentFactory, content: win32more.Windows.Storage.Streams.IBuffer, offset: UInt32, count: UInt32) -> win32more.Windows.Web.Http.HttpBufferContent: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpClient
    _classid_ = 'Windows.Web.Http.HttpClient'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.HttpClient.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpClient.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.HttpClient: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpClientFactory, filter: win32more.Windows.Web.Http.Filters.IHttpFilter) -> win32more.Windows.Web.Http.HttpClient: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetWithOptionAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetBufferAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetInputStreamAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetStringAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def PostAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def PutAsync(self: win32more.Windows.Web.Http.IHttpClient, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def SendRequestAsync(self: win32more.Windows.Web.Http.IHttpClient, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def SendRequestWithOptionAsync(self: win32more.Windows.Web.Http.IHttpClient, request: win32more.Windows.Web.Http.HttpRequestMessage, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def get_DefaultRequestHeaders(self: win32more.Windows.Web.Http.IHttpClient) -> win32more.Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_mixinmethod
    def TryDeleteAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetAsync2(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetBufferAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetBufferResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetInputStreamAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetInputStreamResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetStringAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetStringResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryPostAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryPutAsync(self: win32more.Windows.Web.Http.IHttpClient2, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TrySendRequestAsync(self: win32more.Windows.Web.Http.IHttpClient2, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TrySendRequestAsync2(self: win32more.Windows.Web.Http.IHttpClient2, request: win32more.Windows.Web.Http.HttpRequestMessage, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def get_DefaultPrivacyAnnotation(self: win32more.Windows.Web.Http.IHttpClient3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultPrivacyAnnotation(self: win32more.Windows.Web.Http.IHttpClient3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    DefaultPrivacyAnnotation = property(get_DefaultPrivacyAnnotation, put_DefaultPrivacyAnnotation)
    DefaultRequestHeaders = property(get_DefaultRequestHeaders, None)
class HttpCompletionOption(Enum, Int32):
    ResponseContentRead = 0
    ResponseHeadersRead = 1
class HttpCookie(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.IHttpCookie
    _classid_ = 'Windows.Web.Http.HttpCookie'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Web.Http.HttpCookie.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpCookieFactory, name: WinRT_String, domain: WinRT_String, path: WinRT_String) -> win32more.Windows.Web.Http.HttpCookie: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: win32more.Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Expires(self: win32more.Windows.Web.Http.IHttpCookie) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Expires(self: win32more.Windows.Web.Http.IHttpCookie, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_HttpOnly(self: win32more.Windows.Web.Http.IHttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_HttpOnly(self: win32more.Windows.Web.Http.IHttpCookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Secure(self: win32more.Windows.Web.Http.IHttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_Secure(self: win32more.Windows.Web.Http.IHttpCookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Web.Http.IHttpCookie, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Domain = property(get_Domain, None)
    Expires = property(get_Expires, put_Expires)
    HttpOnly = property(get_HttpOnly, put_HttpOnly)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Secure = property(get_Secure, put_Secure)
    Value = property(get_Value, put_Value)
class HttpCookieCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Web.Http.HttpCookie]]
    default_interface: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie]
    _classid_ = 'Windows.Web.Http.HttpCookieCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie], index: UInt32) -> win32more.Windows.Web.Http.HttpCookie: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie], value: win32more.Windows.Web.Http.HttpCookie, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.HttpCookie], startIndex: UInt32, items: FillArray[win32more.Windows.Web.Http.HttpCookie]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Web.Http.HttpCookie]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Web.Http.HttpCookie]: ...
    Size = property(get_Size, None)
class HttpCookieManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.IHttpCookieManager
    _classid_ = 'Windows.Web.Http.HttpCookieManager'
    @winrt_mixinmethod
    def SetCookie(self: win32more.Windows.Web.Http.IHttpCookieManager, cookie: win32more.Windows.Web.Http.HttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def SetCookieWithThirdParty(self: win32more.Windows.Web.Http.IHttpCookieManager, cookie: win32more.Windows.Web.Http.HttpCookie, thirdParty: Boolean) -> Boolean: ...
    @winrt_mixinmethod
    def DeleteCookie(self: win32more.Windows.Web.Http.IHttpCookieManager, cookie: win32more.Windows.Web.Http.HttpCookie) -> Void: ...
    @winrt_mixinmethod
    def GetCookies(self: win32more.Windows.Web.Http.IHttpCookieManager, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Web.Http.HttpCookieCollection: ...
class HttpFormUrlEncodedContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpFormUrlEncodedContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpFormUrlEncodedContent.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpFormUrlEncodedContentFactory, content: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Web.Http.HttpFormUrlEncodedContent: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpGetBufferResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpGetBufferResult
    _classid_ = 'Windows.Web.Http.HttpGetBufferResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Web.Http.IHttpGetBufferResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.IHttpGetBufferResult) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Windows.Web.Http.IHttpGetBufferResult) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Web.Http.IHttpGetBufferResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Web.Http.IHttpGetBufferResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class HttpGetInputStreamResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpGetInputStreamResult
    _classid_ = 'Windows.Web.Http.HttpGetInputStreamResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Web.Http.IHttpGetInputStreamResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.IHttpGetInputStreamResult) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Windows.Web.Http.IHttpGetInputStreamResult) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Web.Http.IHttpGetInputStreamResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Web.Http.IHttpGetInputStreamResult) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class HttpGetStringResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpGetStringResult
    _classid_ = 'Windows.Web.Http.HttpGetStringResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Web.Http.IHttpGetStringResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.IHttpGetStringResult) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Windows.Web.Http.IHttpGetStringResult) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Web.Http.IHttpGetStringResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Web.Http.IHttpGetStringResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class _HttpMethod_Meta_(ComPtr.__class__):
    pass
class HttpMethod(ComPtr, metaclass=_HttpMethod_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.IHttpMethod
    _classid_ = 'Windows.Web.Http.HttpMethod'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpMethod.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpMethodFactory, method: WinRT_String) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Web.Http.IHttpMethod) -> WinRT_String: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def get_Delete(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Get(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Head(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Options(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Patch(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Post(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Put(cls: win32more.Windows.Web.Http.IHttpMethodStatics) -> win32more.Windows.Web.Http.HttpMethod: ...
    Method = property(get_Method, None)
    _HttpMethod_Meta_.Delete = property(get_Delete, None)
    _HttpMethod_Meta_.Get = property(get_Get, None)
    _HttpMethod_Meta_.Head = property(get_Head, None)
    _HttpMethod_Meta_.Options = property(get_Options, None)
    _HttpMethod_Meta_.Patch = property(get_Patch, None)
    _HttpMethod_Meta_.Post = property(get_Post, None)
    _HttpMethod_Meta_.Put = property(get_Put, None)
class HttpMultipartContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Web.Http.IHttpContent], ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpMultipartContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.HttpMultipartContent.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpMultipartContent.CreateWithSubtype(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Web.Http.HttpMultipartContent.CreateWithSubtypeAndBoundary(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.HttpMultipartContent: ...
    @winrt_factorymethod
    def CreateWithSubtype(cls: win32more.Windows.Web.Http.IHttpMultipartContentFactory, subtype: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartContent: ...
    @winrt_factorymethod
    def CreateWithSubtypeAndBoundary(cls: win32more.Windows.Web.Http.IHttpMultipartContentFactory, subtype: WinRT_String, boundary: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartContent: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Web.Http.IHttpMultipartContent, content: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Web.Http.IHttpContent]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Web.Http.IHttpContent]: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpMultipartFormDataContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Web.Http.IHttpContent], ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpMultipartFormDataContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.HttpMultipartFormDataContent.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpMultipartFormDataContent.CreateWithBoundary(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.HttpMultipartFormDataContent: ...
    @winrt_factorymethod
    def CreateWithBoundary(cls: win32more.Windows.Web.Http.IHttpMultipartFormDataContentFactory, boundary: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartFormDataContent: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.Web.Http.IHttpMultipartFormDataContent, content: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def AddWithName(self: win32more.Windows.Web.Http.IHttpMultipartFormDataContent, content: win32more.Windows.Web.Http.IHttpContent, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddWithNameAndFileName(self: win32more.Windows.Web.Http.IHttpMultipartFormDataContent, content: win32more.Windows.Web.Http.IHttpContent, name: WinRT_String, fileName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Web.Http.IHttpContent]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Web.Http.IHttpContent]: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpProgress(Structure):
    Stage: win32more.Windows.Web.Http.HttpProgressStage
    BytesSent: UInt64
    TotalBytesToSend: win32more.Windows.Foundation.IReference[UInt64]
    BytesReceived: UInt64
    TotalBytesToReceive: win32more.Windows.Foundation.IReference[UInt64]
    Retries: UInt32
class HttpProgressStage(Enum, Int32):
    None_ = 0
    DetectingProxy = 10
    ResolvingName = 20
    ConnectingToServer = 30
    NegotiatingSsl = 40
    SendingHeaders = 50
    SendingContent = 60
    WaitingForResponse = 70
    ReceivingHeaders = 80
    ReceivingContent = 90
class HttpRequestMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpRequestMessage
    _classid_ = 'Windows.Web.Http.HttpRequestMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.HttpRequestMessage.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Web.Http.HttpRequestMessage.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpRequestMessageFactory, method: win32more.Windows.Web.Http.HttpMethod, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Web.Http.IHttpContent: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.Web.Http.IHttpRequestMessage, value: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_mixinmethod
    def put_Method(self: win32more.Windows.Web.Http.IHttpRequestMessage, value: win32more.Windows.Web.Http.HttpMethod) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_RequestUri(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RequestUri(self: win32more.Windows.Web.Http.IHttpRequestMessage, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_TransportInformation(self: win32more.Windows.Web.Http.IHttpRequestMessage) -> win32more.Windows.Web.Http.HttpTransportInformation: ...
    @winrt_mixinmethod
    def get_PrivacyAnnotation(self: win32more.Windows.Web.Http.IHttpRequestMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrivacyAnnotation(self: win32more.Windows.Web.Http.IHttpRequestMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    PrivacyAnnotation = property(get_PrivacyAnnotation, put_PrivacyAnnotation)
    Properties = property(get_Properties, None)
    RequestUri = property(get_RequestUri, put_RequestUri)
    TransportInformation = property(get_TransportInformation, None)
class HttpRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpRequestResult
    _classid_ = 'Windows.Web.Http.HttpRequestResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Web.Http.IHttpRequestResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.IHttpRequestResult) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Windows.Web.Http.IHttpRequestResult) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Web.Http.IHttpRequestResult) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
class HttpResponseMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpResponseMessage
    _classid_ = 'Windows.Web.Http.HttpResponseMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.Http.HttpResponseMessage.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpResponseMessage.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Web.Http.IHttpResponseMessageFactory, statusCode: win32more.Windows.Web.Http.HttpStatusCode) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.IHttpContent: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.Headers.HttpResponseHeaderCollection: ...
    @winrt_mixinmethod
    def get_IsSuccessStatusCode(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_ReasonPhrase(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReasonPhrase(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def put_RequestMessage(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: win32more.Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.HttpResponseMessageSource: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: win32more.Windows.Web.Http.HttpResponseMessageSource) -> Void: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.HttpStatusCode: ...
    @winrt_mixinmethod
    def put_StatusCode(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: win32more.Windows.Web.Http.HttpStatusCode) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.HttpVersion: ...
    @winrt_mixinmethod
    def put_Version(self: win32more.Windows.Web.Http.IHttpResponseMessage, value: win32more.Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_mixinmethod
    def EnsureSuccessStatusCode(self: win32more.Windows.Web.Http.IHttpResponseMessage) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    IsSuccessStatusCode = property(get_IsSuccessStatusCode, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    RequestMessage = property(get_RequestMessage, put_RequestMessage)
    Source = property(get_Source, put_Source)
    StatusCode = property(get_StatusCode, put_StatusCode)
    Version = property(get_Version, put_Version)
class HttpResponseMessageSource(Enum, Int32):
    None_ = 0
    Cache = 1
    Network = 2
class HttpStatusCode(Enum, Int32):
    None_ = 0
    Continue = 100
    SwitchingProtocols = 101
    Processing = 102
    Ok = 200
    Created = 201
    Accepted = 202
    NonAuthoritativeInformation = 203
    NoContent = 204
    ResetContent = 205
    PartialContent = 206
    MultiStatus = 207
    AlreadyReported = 208
    IMUsed = 226
    MultipleChoices = 300
    MovedPermanently = 301
    Found = 302
    SeeOther = 303
    NotModified = 304
    UseProxy = 305
    TemporaryRedirect = 307
    PermanentRedirect = 308
    BadRequest = 400
    Unauthorized = 401
    PaymentRequired = 402
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    ProxyAuthenticationRequired = 407
    RequestTimeout = 408
    Conflict = 409
    Gone = 410
    LengthRequired = 411
    PreconditionFailed = 412
    RequestEntityTooLarge = 413
    RequestUriTooLong = 414
    UnsupportedMediaType = 415
    RequestedRangeNotSatisfiable = 416
    ExpectationFailed = 417
    UnprocessableEntity = 422
    Locked = 423
    FailedDependency = 424
    UpgradeRequired = 426
    PreconditionRequired = 428
    TooManyRequests = 429
    RequestHeaderFieldsTooLarge = 431
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HttpVersionNotSupported = 505
    VariantAlsoNegotiates = 506
    InsufficientStorage = 507
    LoopDetected = 508
    NotExtended = 510
    NetworkAuthenticationRequired = 511
class HttpStreamContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpStreamContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpStreamContent.CreateFromInputStream(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromInputStream(cls: win32more.Windows.Web.Http.IHttpStreamContentFactory, content: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Web.Http.HttpStreamContent: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpStringContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Web.Http.IHttpContent
    _classid_ = 'Windows.Web.Http.HttpStringContent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.Http.HttpStringContent.CreateFromString(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Web.Http.HttpStringContent.CreateFromStringWithEncoding(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Web.Http.HttpStringContent.CreateFromStringWithEncodingAndMediaType(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromString(cls: win32more.Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String) -> win32more.Windows.Web.Http.HttpStringContent: ...
    @winrt_factorymethod
    def CreateFromStringWithEncoding(cls: win32more.Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Web.Http.HttpStringContent: ...
    @winrt_factorymethod
    def CreateFromStringWithEncodingAndMediaType(cls: win32more.Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding, mediaType: WinRT_String) -> win32more.Windows.Web.Http.HttpStringContent: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: win32more.Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: win32more.Windows.Web.Http.IHttpContent, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpTransportInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.IHttpTransportInformation
    _classid_ = 'Windows.Web.Http.HttpTransportInformation'
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Windows.Web.Http.IHttpTransportInformation) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: win32more.Windows.Web.Http.IHttpTransportInformation) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: win32more.Windows.Web.Http.IHttpTransportInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: win32more.Windows.Web.Http.IHttpTransportInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
class HttpVersion(Enum, Int32):
    None_ = 0
    Http10 = 1
    Http11 = 2
    Http20 = 3
class IHttpBufferContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpBufferContentFactory'
    _iid_ = Guid('{bc20c193-c41f-4ff7-9123-6435736eadc2}')
    @winrt_commethod(6)
    def CreateFromBuffer(self, content: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Web.Http.HttpBufferContent: ...
    @winrt_commethod(7)
    def CreateFromBufferWithOffset(self, content: win32more.Windows.Storage.Streams.IBuffer, offset: UInt32, count: UInt32) -> win32more.Windows.Web.Http.HttpBufferContent: ...
class IHttpClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpClient'
    _iid_ = Guid('{7fda1151-3574-4880-a8ba-e6b1e0061f3d}')
    @winrt_commethod(6)
    def DeleteAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(7)
    def GetAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(8)
    def GetWithOptionAsync(self, uri: win32more.Windows.Foundation.Uri, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(9)
    def GetBufferAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(10)
    def GetInputStreamAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(11)
    def GetStringAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(12)
    def PostAsync(self, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(13)
    def PutAsync(self, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(14)
    def SendRequestAsync(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(15)
    def SendRequestWithOptionAsync(self, request: win32more.Windows.Web.Http.HttpRequestMessage, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpResponseMessage, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(16)
    def get_DefaultRequestHeaders(self) -> win32more.Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    DefaultRequestHeaders = property(get_DefaultRequestHeaders, None)
class IHttpClient2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpClient2'
    _iid_ = Guid('{cdd83348-e8b7-4cec-b1b0-dc455fe72c92}')
    @winrt_commethod(6)
    def TryDeleteAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(7)
    def TryGetAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(8)
    def TryGetAsync2(self, uri: win32more.Windows.Foundation.Uri, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(9)
    def TryGetBufferAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetBufferResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(10)
    def TryGetInputStreamAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetInputStreamResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(11)
    def TryGetStringAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpGetStringResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(12)
    def TryPostAsync(self, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(13)
    def TryPutAsync(self, uri: win32more.Windows.Foundation.Uri, content: win32more.Windows.Web.Http.IHttpContent) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(14)
    def TrySendRequestAsync(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(15)
    def TrySendRequestAsync2(self, request: win32more.Windows.Web.Http.HttpRequestMessage, completionOption: win32more.Windows.Web.Http.HttpCompletionOption) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Http.HttpRequestResult, win32more.Windows.Web.Http.HttpProgress]: ...
class IHttpClient3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpClient3'
    _iid_ = Guid('{1172fd01-9899-4194-963f-8f9d72a7ec15}')
    @winrt_commethod(6)
    def get_DefaultPrivacyAnnotation(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DefaultPrivacyAnnotation(self, value: WinRT_String) -> Void: ...
    DefaultPrivacyAnnotation = property(get_DefaultPrivacyAnnotation, put_DefaultPrivacyAnnotation)
class IHttpClientFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpClientFactory'
    _iid_ = Guid('{c30c4eca-e3fa-4f99-afb4-63cc65009462}')
    @winrt_commethod(6)
    def Create(self, filter: win32more.Windows.Web.Http.Filters.IHttpFilter) -> win32more.Windows.Web.Http.HttpClient: ...
class IHttpContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Web.Http.IHttpContent'
    _iid_ = Guid('{6b14a441-fba7-4bd2-af0a-839de7c295da}')
    @winrt_commethod(6)
    def get_Headers(self) -> win32more.Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_commethod(7)
    def BufferAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_commethod(8)
    def ReadAsBufferAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_commethod(9)
    def ReadAsInputStreamAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_commethod(10)
    def ReadAsStringAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_commethod(11)
    def TryComputeLength(self, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_commethod(12)
    def WriteToStreamAsync(self, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    Headers = property(get_Headers, None)
class IHttpCookie(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpCookie'
    _iid_ = Guid('{1f5488e2-cc2d-4779-86a7-88f10687d249}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Domain(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Expires(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(10)
    def put_Expires(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(11)
    def get_HttpOnly(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_HttpOnly(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_Secure(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Secure(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_Value(self, value: WinRT_String) -> Void: ...
    Domain = property(get_Domain, None)
    Expires = property(get_Expires, put_Expires)
    HttpOnly = property(get_HttpOnly, put_HttpOnly)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Secure = property(get_Secure, put_Secure)
    Value = property(get_Value, put_Value)
class IHttpCookieFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpCookieFactory'
    _iid_ = Guid('{6a0585a9-931c-4cd1-a96d-c21701785c5f}')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String, domain: WinRT_String, path: WinRT_String) -> win32more.Windows.Web.Http.HttpCookie: ...
class IHttpCookieManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpCookieManager'
    _iid_ = Guid('{7a431780-cd4f-4e57-a84a-5b0a53d6bb96}')
    @winrt_commethod(6)
    def SetCookie(self, cookie: win32more.Windows.Web.Http.HttpCookie) -> Boolean: ...
    @winrt_commethod(7)
    def SetCookieWithThirdParty(self, cookie: win32more.Windows.Web.Http.HttpCookie, thirdParty: Boolean) -> Boolean: ...
    @winrt_commethod(8)
    def DeleteCookie(self, cookie: win32more.Windows.Web.Http.HttpCookie) -> Void: ...
    @winrt_commethod(9)
    def GetCookies(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Web.Http.HttpCookieCollection: ...
class IHttpFormUrlEncodedContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpFormUrlEncodedContentFactory'
    _iid_ = Guid('{43f0138c-2f73-4302-b5f3-eae9238a5e01}')
    @winrt_commethod(6)
    def Create(self, content: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Web.Http.HttpFormUrlEncodedContent: ...
class IHttpGetBufferResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpGetBufferResult'
    _iid_ = Guid('{53d08e7c-e209-404e-9a49-742d8236fd3a}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class IHttpGetInputStreamResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpGetInputStreamResult'
    _iid_ = Guid('{d5d63463-13aa-4ee0-be95-a0c39fe91203}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class IHttpGetStringResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpGetStringResult'
    _iid_ = Guid('{9bac466d-8509-4775-b16d-8953f47a7f5f}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Value(self) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class IHttpMethod(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMethod'
    _iid_ = Guid('{728d4022-700d-4fe0-afa5-40299c58dbfd}')
    @winrt_commethod(6)
    def get_Method(self) -> WinRT_String: ...
    Method = property(get_Method, None)
class IHttpMethodFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMethodFactory'
    _iid_ = Guid('{3c51d10d-36d7-40f8-a86d-e759caf2f83f}')
    @winrt_commethod(6)
    def Create(self, method: WinRT_String) -> win32more.Windows.Web.Http.HttpMethod: ...
class IHttpMethodStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMethodStatics'
    _iid_ = Guid('{64d171f0-d99a-4153-8dc6-d68cc4cce317}')
    @winrt_commethod(6)
    def get_Delete(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(7)
    def get_Get(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(8)
    def get_Head(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(9)
    def get_Options(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(10)
    def get_Patch(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(11)
    def get_Post(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(12)
    def get_Put(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    Delete = property(get_Delete, None)
    Get = property(get_Get, None)
    Head = property(get_Head, None)
    Options = property(get_Options, None)
    Patch = property(get_Patch, None)
    Post = property(get_Post, None)
    Put = property(get_Put, None)
class IHttpMultipartContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMultipartContent'
    _iid_ = Guid('{df916aff-9926-4ac9-aaf1-e0d04ef09bb9}')
    @winrt_commethod(6)
    def Add(self, content: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
class IHttpMultipartContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMultipartContentFactory'
    _iid_ = Guid('{7eb42e62-0222-4f20-b372-47d5db5d33b4}')
    @winrt_commethod(6)
    def CreateWithSubtype(self, subtype: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartContent: ...
    @winrt_commethod(7)
    def CreateWithSubtypeAndBoundary(self, subtype: WinRT_String, boundary: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartContent: ...
class IHttpMultipartFormDataContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMultipartFormDataContent'
    _iid_ = Guid('{64d337e2-e967-4624-b6d1-cf74604a4a42}')
    @winrt_commethod(6)
    def Add(self, content: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(7)
    def AddWithName(self, content: win32more.Windows.Web.Http.IHttpContent, name: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def AddWithNameAndFileName(self, content: win32more.Windows.Web.Http.IHttpContent, name: WinRT_String, fileName: WinRT_String) -> Void: ...
class IHttpMultipartFormDataContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpMultipartFormDataContentFactory'
    _iid_ = Guid('{a04d7311-5017-4622-93a8-49b24a4fcbfc}')
    @winrt_commethod(6)
    def CreateWithBoundary(self, boundary: WinRT_String) -> win32more.Windows.Web.Http.HttpMultipartFormDataContent: ...
class IHttpRequestMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpRequestMessage'
    _iid_ = Guid('{f5762b3c-74d4-4811-b5dc-9f8b4e2f9abf}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Web.Http.IHttpContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> win32more.Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_commethod(9)
    def get_Method(self) -> win32more.Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(10)
    def put_Method(self, value: win32more.Windows.Web.Http.HttpMethod) -> Void: ...
    @winrt_commethod(11)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(12)
    def get_RequestUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_RequestUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(14)
    def get_TransportInformation(self) -> win32more.Windows.Web.Http.HttpTransportInformation: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    Properties = property(get_Properties, None)
    RequestUri = property(get_RequestUri, put_RequestUri)
    TransportInformation = property(get_TransportInformation, None)
class IHttpRequestMessage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpRequestMessage2'
    _iid_ = Guid('{c3c60489-62c2-4a3f-9554-226e7c60bd96}')
    @winrt_commethod(6)
    def get_PrivacyAnnotation(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PrivacyAnnotation(self, value: WinRT_String) -> Void: ...
    PrivacyAnnotation = property(get_PrivacyAnnotation, put_PrivacyAnnotation)
class IHttpRequestMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpRequestMessageFactory'
    _iid_ = Guid('{5bac994e-3886-412e-aec3-52ec7f25616f}')
    @winrt_commethod(6)
    def Create(self, method: win32more.Windows.Web.Http.HttpMethod, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
class IHttpRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpRequestResult'
    _iid_ = Guid('{6acf4da8-b5eb-4a35-a902-4217fbe820c5}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
class IHttpResponseMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpResponseMessage'
    _iid_ = Guid('{fee200fb-8664-44e0-95d9-42696199bffc}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Web.Http.IHttpContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> win32more.Windows.Web.Http.Headers.HttpResponseHeaderCollection: ...
    @winrt_commethod(9)
    def get_IsSuccessStatusCode(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ReasonPhrase(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ReasonPhrase(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(13)
    def put_RequestMessage(self, value: win32more.Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_commethod(14)
    def get_Source(self) -> win32more.Windows.Web.Http.HttpResponseMessageSource: ...
    @winrt_commethod(15)
    def put_Source(self, value: win32more.Windows.Web.Http.HttpResponseMessageSource) -> Void: ...
    @winrt_commethod(16)
    def get_StatusCode(self) -> win32more.Windows.Web.Http.HttpStatusCode: ...
    @winrt_commethod(17)
    def put_StatusCode(self, value: win32more.Windows.Web.Http.HttpStatusCode) -> Void: ...
    @winrt_commethod(18)
    def get_Version(self) -> win32more.Windows.Web.Http.HttpVersion: ...
    @winrt_commethod(19)
    def put_Version(self, value: win32more.Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_commethod(20)
    def EnsureSuccessStatusCode(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    IsSuccessStatusCode = property(get_IsSuccessStatusCode, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    RequestMessage = property(get_RequestMessage, put_RequestMessage)
    Source = property(get_Source, put_Source)
    StatusCode = property(get_StatusCode, put_StatusCode)
    Version = property(get_Version, put_Version)
class IHttpResponseMessageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpResponseMessageFactory'
    _iid_ = Guid('{52a8af99-f095-43da-b60f-7cfc2bc7ea2f}')
    @winrt_commethod(6)
    def Create(self, statusCode: win32more.Windows.Web.Http.HttpStatusCode) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
class IHttpStreamContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpStreamContentFactory'
    _iid_ = Guid('{f3e64d9d-f725-407e-942f-0eda189809f4}')
    @winrt_commethod(6)
    def CreateFromInputStream(self, content: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Web.Http.HttpStreamContent: ...
class IHttpStringContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpStringContentFactory'
    _iid_ = Guid('{46649d5b-2e93-48eb-8e61-19677878e57f}')
    @winrt_commethod(6)
    def CreateFromString(self, content: WinRT_String) -> win32more.Windows.Web.Http.HttpStringContent: ...
    @winrt_commethod(7)
    def CreateFromStringWithEncoding(self, content: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Web.Http.HttpStringContent: ...
    @winrt_commethod(8)
    def CreateFromStringWithEncodingAndMediaType(self, content: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding, mediaType: WinRT_String) -> win32more.Windows.Web.Http.HttpStringContent: ...
class IHttpTransportInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.IHttpTransportInformation'
    _iid_ = Guid('{70127198-c6a7-4ed0-833a-83fd8b8f178d}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> win32more.Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)


make_ready(__name__)
