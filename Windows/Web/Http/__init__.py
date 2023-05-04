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
import Windows.Security.Cryptography.Certificates
import Windows.Storage.Streams
import Windows.Web.Http
import Windows.Web.Http.Filters
import Windows.Web.Http.Headers
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HttpBufferContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpBufferContent'
    @winrt_factorymethod
    def CreateFromBuffer(cls: Windows.Web.Http.IHttpBufferContentFactory, content: Windows.Storage.Streams.IBuffer) -> Windows.Web.Http.HttpBufferContent: ...
    @winrt_factorymethod
    def CreateFromBufferWithOffset(cls: Windows.Web.Http.IHttpBufferContentFactory, content: Windows.Storage.Streams.IBuffer, offset: UInt32, count: UInt32) -> Windows.Web.Http.HttpBufferContent: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpClient'
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.HttpClient: ...
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpClientFactory, filter: Windows.Web.Http.Filters.IHttpFilter) -> Windows.Web.Http.HttpClient: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetWithOptionAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetBufferAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetInputStreamAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def GetStringAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def PostAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def PutAsync(self: Windows.Web.Http.IHttpClient, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def SendRequestAsync(self: Windows.Web.Http.IHttpClient, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def SendRequestWithOptionAsync(self: Windows.Web.Http.IHttpClient, request: Windows.Web.Http.HttpRequestMessage, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def get_DefaultRequestHeaders(self: Windows.Web.Http.IHttpClient) -> Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_mixinmethod
    def TryDeleteAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetAsync2(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetBufferAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetBufferResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetInputStreamAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetInputStreamResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryGetStringAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetStringResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryPostAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TryPutAsync(self: Windows.Web.Http.IHttpClient2, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TrySendRequestAsync(self: Windows.Web.Http.IHttpClient2, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def TrySendRequestAsync2(self: Windows.Web.Http.IHttpClient2, request: Windows.Web.Http.HttpRequestMessage, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_mixinmethod
    def get_DefaultPrivacyAnnotation(self: Windows.Web.Http.IHttpClient3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultPrivacyAnnotation(self: Windows.Web.Http.IHttpClient3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    DefaultRequestHeaders = property(get_DefaultRequestHeaders, None)
    DefaultPrivacyAnnotation = property(get_DefaultPrivacyAnnotation, put_DefaultPrivacyAnnotation)
HttpCompletionOption = Int32
HttpCompletionOption_ResponseContentRead: HttpCompletionOption = 0
HttpCompletionOption_ResponseHeadersRead: HttpCompletionOption = 1
class HttpCookie(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpCookie'
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpCookieFactory, name: WinRT_String, domain: WinRT_String, path: WinRT_String) -> Windows.Web.Http.HttpCookie: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Expires(self: Windows.Web.Http.IHttpCookie) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Expires(self: Windows.Web.Http.IHttpCookie, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_HttpOnly(self: Windows.Web.Http.IHttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_HttpOnly(self: Windows.Web.Http.IHttpCookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Secure(self: Windows.Web.Http.IHttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_Secure(self: Windows.Web.Http.IHttpCookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Web.Http.IHttpCookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Web.Http.IHttpCookie, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Path = property(get_Path, None)
    Expires = property(get_Expires, put_Expires)
    HttpOnly = property(get_HttpOnly, put_HttpOnly)
    Secure = property(get_Secure, put_Secure)
    Value = property(get_Value, put_Value)
class HttpCookieCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpCookieCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Web.Http.HttpCookie], index: UInt32) -> Windows.Web.Http.HttpCookie: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Web.Http.HttpCookie]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Web.Http.HttpCookie], value: Windows.Web.Http.HttpCookie, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Web.Http.HttpCookie], startIndex: UInt32, items: POINTER(Windows.Web.Http.HttpCookie)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Web.Http.HttpCookie]) -> Windows.Foundation.Collections.IIterator[Windows.Web.Http.HttpCookie]: ...
    Size = property(get_Size, None)
class HttpCookieManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpCookieManager'
    @winrt_mixinmethod
    def SetCookie(self: Windows.Web.Http.IHttpCookieManager, cookie: Windows.Web.Http.HttpCookie) -> Boolean: ...
    @winrt_mixinmethod
    def SetCookieWithThirdParty(self: Windows.Web.Http.IHttpCookieManager, cookie: Windows.Web.Http.HttpCookie, thirdParty: Boolean) -> Boolean: ...
    @winrt_mixinmethod
    def DeleteCookie(self: Windows.Web.Http.IHttpCookieManager, cookie: Windows.Web.Http.HttpCookie) -> Void: ...
    @winrt_mixinmethod
    def GetCookies(self: Windows.Web.Http.IHttpCookieManager, uri: Windows.Foundation.Uri) -> Windows.Web.Http.HttpCookieCollection: ...
class HttpFormUrlEncodedContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpFormUrlEncodedContent'
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpFormUrlEncodedContentFactory, content: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Web.Http.HttpFormUrlEncodedContent: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpGetBufferResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpGetBufferResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Web.Http.IHttpGetBufferResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.IHttpGetBufferResult) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: Windows.Web.Http.IHttpGetBufferResult) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Web.Http.IHttpGetBufferResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Web.Http.IHttpGetBufferResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class HttpGetInputStreamResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpGetInputStreamResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Web.Http.IHttpGetInputStreamResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.IHttpGetInputStreamResult) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: Windows.Web.Http.IHttpGetInputStreamResult) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Web.Http.IHttpGetInputStreamResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Web.Http.IHttpGetInputStreamResult) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class HttpGetStringResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpGetStringResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Web.Http.IHttpGetStringResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.IHttpGetStringResult) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: Windows.Web.Http.IHttpGetStringResult) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Web.Http.IHttpGetStringResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Web.Http.IHttpGetStringResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class HttpMethod(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpMethod'
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpMethodFactory, method: WinRT_String) -> Windows.Web.Http.HttpMethod: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Web.Http.IHttpMethod) -> WinRT_String: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def get_Delete(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Get(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Head(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Options(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Patch(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Post(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    @winrt_classmethod
    def get_Put(cls: Windows.Web.Http.IHttpMethodStatics) -> Windows.Web.Http.HttpMethod: ...
    Method = property(get_Method, None)
    Delete = property(get_Delete, None)
    Get = property(get_Get, None)
    Head = property(get_Head, None)
    Options = property(get_Options, None)
    Patch = property(get_Patch, None)
    Post = property(get_Post, None)
    Put = property(get_Put, None)
class HttpMultipartContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpMultipartContent'
    @winrt_factorymethod
    def CreateWithSubtype(cls: Windows.Web.Http.IHttpMultipartContentFactory, subtype: WinRT_String) -> Windows.Web.Http.HttpMultipartContent: ...
    @winrt_factorymethod
    def CreateWithSubtypeAndBoundary(cls: Windows.Web.Http.IHttpMultipartContentFactory, subtype: WinRT_String, boundary: WinRT_String) -> Windows.Web.Http.HttpMultipartContent: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.HttpMultipartContent: ...
    @winrt_mixinmethod
    def Add(self: Windows.Web.Http.IHttpMultipartContent, content: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Web.Http.IHttpContent]) -> Windows.Foundation.Collections.IIterator[Windows.Web.Http.IHttpContent]: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpMultipartFormDataContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpMultipartFormDataContent'
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.HttpMultipartFormDataContent: ...
    @winrt_factorymethod
    def CreateWithBoundary(cls: Windows.Web.Http.IHttpMultipartFormDataContentFactory, boundary: WinRT_String) -> Windows.Web.Http.HttpMultipartFormDataContent: ...
    @winrt_mixinmethod
    def Add(self: Windows.Web.Http.IHttpMultipartFormDataContent, content: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def AddWithName(self: Windows.Web.Http.IHttpMultipartFormDataContent, content: Windows.Web.Http.IHttpContent, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddWithNameAndFileName(self: Windows.Web.Http.IHttpMultipartFormDataContent, content: Windows.Web.Http.IHttpContent, name: WinRT_String, fileName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Web.Http.IHttpContent]) -> Windows.Foundation.Collections.IIterator[Windows.Web.Http.IHttpContent]: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpProgress(EasyCastStructure):
    Stage: Windows.Web.Http.HttpProgressStage
    BytesSent: UInt64
    TotalBytesToSend: Windows.Foundation.IReference[UInt64]
    BytesReceived: UInt64
    TotalBytesToReceive: Windows.Foundation.IReference[UInt64]
    Retries: UInt32
HttpProgressStage = Int32
HttpProgressStage_None: HttpProgressStage = 0
HttpProgressStage_DetectingProxy: HttpProgressStage = 10
HttpProgressStage_ResolvingName: HttpProgressStage = 20
HttpProgressStage_ConnectingToServer: HttpProgressStage = 30
HttpProgressStage_NegotiatingSsl: HttpProgressStage = 40
HttpProgressStage_SendingHeaders: HttpProgressStage = 50
HttpProgressStage_SendingContent: HttpProgressStage = 60
HttpProgressStage_WaitingForResponse: HttpProgressStage = 70
HttpProgressStage_ReceivingHeaders: HttpProgressStage = 80
HttpProgressStage_ReceivingContent: HttpProgressStage = 90
class HttpRequestMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpRequestMessage'
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpRequestMessageFactory, method: Windows.Web.Http.HttpMethod, uri: Windows.Foundation.Uri) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Web.Http.IHttpContent: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.Web.Http.IHttpRequestMessage, value: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Web.Http.HttpMethod: ...
    @winrt_mixinmethod
    def put_Method(self: Windows.Web.Http.IHttpRequestMessage, value: Windows.Web.Http.HttpMethod) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_RequestUri(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RequestUri(self: Windows.Web.Http.IHttpRequestMessage, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_TransportInformation(self: Windows.Web.Http.IHttpRequestMessage) -> Windows.Web.Http.HttpTransportInformation: ...
    @winrt_mixinmethod
    def get_PrivacyAnnotation(self: Windows.Web.Http.IHttpRequestMessage2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrivacyAnnotation(self: Windows.Web.Http.IHttpRequestMessage2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    Properties = property(get_Properties, None)
    RequestUri = property(get_RequestUri, put_RequestUri)
    TransportInformation = property(get_TransportInformation, None)
    PrivacyAnnotation = property(get_PrivacyAnnotation, put_PrivacyAnnotation)
class HttpRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpRequestResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Web.Http.IHttpRequestResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.IHttpRequestResult) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: Windows.Web.Http.IHttpRequestResult) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Web.Http.IHttpRequestResult) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
class HttpResponseMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpResponseMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_factorymethod
    def Create(cls: Windows.Web.Http.IHttpResponseMessageFactory, statusCode: Windows.Web.Http.HttpStatusCode) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.IHttpContent: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.Web.Http.IHttpResponseMessage, value: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.Headers.HttpResponseHeaderCollection: ...
    @winrt_mixinmethod
    def get_IsSuccessStatusCode(self: Windows.Web.Http.IHttpResponseMessage) -> Boolean: ...
    @winrt_mixinmethod
    def get_ReasonPhrase(self: Windows.Web.Http.IHttpResponseMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReasonPhrase(self: Windows.Web.Http.IHttpResponseMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RequestMessage(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def put_RequestMessage(self: Windows.Web.Http.IHttpResponseMessage, value: Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.HttpResponseMessageSource: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.Web.Http.IHttpResponseMessage, value: Windows.Web.Http.HttpResponseMessageSource) -> Void: ...
    @winrt_mixinmethod
    def get_StatusCode(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.HttpStatusCode: ...
    @winrt_mixinmethod
    def put_StatusCode(self: Windows.Web.Http.IHttpResponseMessage, value: Windows.Web.Http.HttpStatusCode) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.HttpVersion: ...
    @winrt_mixinmethod
    def put_Version(self: Windows.Web.Http.IHttpResponseMessage, value: Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_mixinmethod
    def EnsureSuccessStatusCode(self: Windows.Web.Http.IHttpResponseMessage) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    IsSuccessStatusCode = property(get_IsSuccessStatusCode, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    RequestMessage = property(get_RequestMessage, put_RequestMessage)
    Source = property(get_Source, put_Source)
    StatusCode = property(get_StatusCode, put_StatusCode)
    Version = property(get_Version, put_Version)
HttpResponseMessageSource = Int32
HttpResponseMessageSource_None: HttpResponseMessageSource = 0
HttpResponseMessageSource_Cache: HttpResponseMessageSource = 1
HttpResponseMessageSource_Network: HttpResponseMessageSource = 2
HttpStatusCode = Int32
HttpStatusCode_None: HttpStatusCode = 0
HttpStatusCode_Continue: HttpStatusCode = 100
HttpStatusCode_SwitchingProtocols: HttpStatusCode = 101
HttpStatusCode_Processing: HttpStatusCode = 102
HttpStatusCode_Ok: HttpStatusCode = 200
HttpStatusCode_Created: HttpStatusCode = 201
HttpStatusCode_Accepted: HttpStatusCode = 202
HttpStatusCode_NonAuthoritativeInformation: HttpStatusCode = 203
HttpStatusCode_NoContent: HttpStatusCode = 204
HttpStatusCode_ResetContent: HttpStatusCode = 205
HttpStatusCode_PartialContent: HttpStatusCode = 206
HttpStatusCode_MultiStatus: HttpStatusCode = 207
HttpStatusCode_AlreadyReported: HttpStatusCode = 208
HttpStatusCode_IMUsed: HttpStatusCode = 226
HttpStatusCode_MultipleChoices: HttpStatusCode = 300
HttpStatusCode_MovedPermanently: HttpStatusCode = 301
HttpStatusCode_Found: HttpStatusCode = 302
HttpStatusCode_SeeOther: HttpStatusCode = 303
HttpStatusCode_NotModified: HttpStatusCode = 304
HttpStatusCode_UseProxy: HttpStatusCode = 305
HttpStatusCode_TemporaryRedirect: HttpStatusCode = 307
HttpStatusCode_PermanentRedirect: HttpStatusCode = 308
HttpStatusCode_BadRequest: HttpStatusCode = 400
HttpStatusCode_Unauthorized: HttpStatusCode = 401
HttpStatusCode_PaymentRequired: HttpStatusCode = 402
HttpStatusCode_Forbidden: HttpStatusCode = 403
HttpStatusCode_NotFound: HttpStatusCode = 404
HttpStatusCode_MethodNotAllowed: HttpStatusCode = 405
HttpStatusCode_NotAcceptable: HttpStatusCode = 406
HttpStatusCode_ProxyAuthenticationRequired: HttpStatusCode = 407
HttpStatusCode_RequestTimeout: HttpStatusCode = 408
HttpStatusCode_Conflict: HttpStatusCode = 409
HttpStatusCode_Gone: HttpStatusCode = 410
HttpStatusCode_LengthRequired: HttpStatusCode = 411
HttpStatusCode_PreconditionFailed: HttpStatusCode = 412
HttpStatusCode_RequestEntityTooLarge: HttpStatusCode = 413
HttpStatusCode_RequestUriTooLong: HttpStatusCode = 414
HttpStatusCode_UnsupportedMediaType: HttpStatusCode = 415
HttpStatusCode_RequestedRangeNotSatisfiable: HttpStatusCode = 416
HttpStatusCode_ExpectationFailed: HttpStatusCode = 417
HttpStatusCode_UnprocessableEntity: HttpStatusCode = 422
HttpStatusCode_Locked: HttpStatusCode = 423
HttpStatusCode_FailedDependency: HttpStatusCode = 424
HttpStatusCode_UpgradeRequired: HttpStatusCode = 426
HttpStatusCode_PreconditionRequired: HttpStatusCode = 428
HttpStatusCode_TooManyRequests: HttpStatusCode = 429
HttpStatusCode_RequestHeaderFieldsTooLarge: HttpStatusCode = 431
HttpStatusCode_InternalServerError: HttpStatusCode = 500
HttpStatusCode_NotImplemented: HttpStatusCode = 501
HttpStatusCode_BadGateway: HttpStatusCode = 502
HttpStatusCode_ServiceUnavailable: HttpStatusCode = 503
HttpStatusCode_GatewayTimeout: HttpStatusCode = 504
HttpStatusCode_HttpVersionNotSupported: HttpStatusCode = 505
HttpStatusCode_VariantAlsoNegotiates: HttpStatusCode = 506
HttpStatusCode_InsufficientStorage: HttpStatusCode = 507
HttpStatusCode_LoopDetected: HttpStatusCode = 508
HttpStatusCode_NotExtended: HttpStatusCode = 510
HttpStatusCode_NetworkAuthenticationRequired: HttpStatusCode = 511
class HttpStreamContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpStreamContent'
    @winrt_factorymethod
    def CreateFromInputStream(cls: Windows.Web.Http.IHttpStreamContentFactory, content: Windows.Storage.Streams.IInputStream) -> Windows.Web.Http.HttpStreamContent: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpStringContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpStringContent'
    @winrt_factorymethod
    def CreateFromString(cls: Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String) -> Windows.Web.Http.HttpStringContent: ...
    @winrt_factorymethod
    def CreateFromStringWithEncoding(cls: Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Web.Http.HttpStringContent: ...
    @winrt_factorymethod
    def CreateFromStringWithEncodingAndMediaType(cls: Windows.Web.Http.IHttpStringContentFactory, content: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding, mediaType: WinRT_String) -> Windows.Web.Http.HttpStringContent: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Web.Http.IHttpContent) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_mixinmethod
    def BufferAllAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsBufferAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsInputStreamAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_mixinmethod
    def ReadAsStringAsync(self: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_mixinmethod
    def TryComputeLength(self: Windows.Web.Http.IHttpContent, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_mixinmethod
    def WriteToStreamAsync(self: Windows.Web.Http.IHttpContent, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    Headers = property(get_Headers, None)
class HttpTransportInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.HttpTransportInformation'
    @winrt_mixinmethod
    def get_ServerCertificate(self: Windows.Web.Http.IHttpTransportInformation) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrorSeverity(self: Windows.Web.Http.IHttpTransportInformation) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_mixinmethod
    def get_ServerCertificateErrors(self: Windows.Web.Http.IHttpTransportInformation) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_mixinmethod
    def get_ServerIntermediateCertificates(self: Windows.Web.Http.IHttpTransportInformation) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
HttpVersion = Int32
HttpVersion_None: HttpVersion = 0
HttpVersion_Http10: HttpVersion = 1
HttpVersion_Http11: HttpVersion = 2
HttpVersion_Http20: HttpVersion = 3
class IHttpBufferContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bc20c193-c41f-4ff7-9123-6435736eadc2}')
    @winrt_commethod(6)
    def CreateFromBuffer(self, content: Windows.Storage.Streams.IBuffer) -> Windows.Web.Http.HttpBufferContent: ...
    @winrt_commethod(7)
    def CreateFromBufferWithOffset(self, content: Windows.Storage.Streams.IBuffer, offset: UInt32, count: UInt32) -> Windows.Web.Http.HttpBufferContent: ...
class IHttpClient(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7fda1151-3574-4880-a8ba-e6b1e0061f3d}')
    @winrt_commethod(6)
    def DeleteAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(7)
    def GetAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(8)
    def GetWithOptionAsync(self, uri: Windows.Foundation.Uri, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(9)
    def GetBufferAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(10)
    def GetInputStreamAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(11)
    def GetStringAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(12)
    def PostAsync(self, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(13)
    def PutAsync(self, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(14)
    def SendRequestAsync(self, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(15)
    def SendRequestWithOptionAsync(self, request: Windows.Web.Http.HttpRequestMessage, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpResponseMessage, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(16)
    def get_DefaultRequestHeaders(self) -> Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    DefaultRequestHeaders = property(get_DefaultRequestHeaders, None)
class IHttpClient2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cdd83348-e8b7-4cec-b1b0-dc455fe72c92}')
    @winrt_commethod(6)
    def TryDeleteAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(7)
    def TryGetAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(8)
    def TryGetAsync2(self, uri: Windows.Foundation.Uri, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(9)
    def TryGetBufferAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetBufferResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(10)
    def TryGetInputStreamAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetInputStreamResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(11)
    def TryGetStringAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpGetStringResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(12)
    def TryPostAsync(self, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(13)
    def TryPutAsync(self, uri: Windows.Foundation.Uri, content: Windows.Web.Http.IHttpContent) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(14)
    def TrySendRequestAsync(self, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
    @winrt_commethod(15)
    def TrySendRequestAsync2(self, request: Windows.Web.Http.HttpRequestMessage, completionOption: Windows.Web.Http.HttpCompletionOption) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Web.Http.HttpRequestResult, Windows.Web.Http.HttpProgress]: ...
class IHttpClient3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1172fd01-9899-4194-963f-8f9d72a7ec15}')
    @winrt_commethod(6)
    def get_DefaultPrivacyAnnotation(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DefaultPrivacyAnnotation(self, value: WinRT_String) -> Void: ...
    DefaultPrivacyAnnotation = property(get_DefaultPrivacyAnnotation, put_DefaultPrivacyAnnotation)
class IHttpClientFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c30c4eca-e3fa-4f99-afb4-63cc65009462}')
    @winrt_commethod(6)
    def Create(self, filter: Windows.Web.Http.Filters.IHttpFilter) -> Windows.Web.Http.HttpClient: ...
class IHttpContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6b14a441-fba7-4bd2-af0a-839de7c295da}')
    @winrt_commethod(6)
    def get_Headers(self) -> Windows.Web.Http.Headers.HttpContentHeaderCollection: ...
    @winrt_commethod(7)
    def BufferAllAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    @winrt_commethod(8)
    def ReadAsBufferAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, UInt64]: ...
    @winrt_commethod(9)
    def ReadAsInputStreamAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IInputStream, UInt64]: ...
    @winrt_commethod(10)
    def ReadAsStringAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[WinRT_String, UInt64]: ...
    @winrt_commethod(11)
    def TryComputeLength(self, length: POINTER(UInt64)) -> Boolean: ...
    @winrt_commethod(12)
    def WriteToStreamAsync(self, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt64, UInt64]: ...
    Headers = property(get_Headers, None)
class IHttpCookie(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1f5488e2-cc2d-4779-86a7-88f10687d249}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Domain(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Expires(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(10)
    def put_Expires(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
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
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Path = property(get_Path, None)
    Expires = property(get_Expires, put_Expires)
    HttpOnly = property(get_HttpOnly, put_HttpOnly)
    Secure = property(get_Secure, put_Secure)
    Value = property(get_Value, put_Value)
class IHttpCookieFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6a0585a9-931c-4cd1-a96d-c21701785c5f}')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String, domain: WinRT_String, path: WinRT_String) -> Windows.Web.Http.HttpCookie: ...
class IHttpCookieManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7a431780-cd4f-4e57-a84a-5b0a53d6bb96}')
    @winrt_commethod(6)
    def SetCookie(self, cookie: Windows.Web.Http.HttpCookie) -> Boolean: ...
    @winrt_commethod(7)
    def SetCookieWithThirdParty(self, cookie: Windows.Web.Http.HttpCookie, thirdParty: Boolean) -> Boolean: ...
    @winrt_commethod(8)
    def DeleteCookie(self, cookie: Windows.Web.Http.HttpCookie) -> Void: ...
    @winrt_commethod(9)
    def GetCookies(self, uri: Windows.Foundation.Uri) -> Windows.Web.Http.HttpCookieCollection: ...
class IHttpFormUrlEncodedContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{43f0138c-2f73-4302-b5f3-eae9238a5e01}')
    @winrt_commethod(6)
    def Create(self, content: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Web.Http.HttpFormUrlEncodedContent: ...
class IHttpGetBufferResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{53d08e7c-e209-404e-9a49-742d8236fd3a}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Value(self) -> Windows.Storage.Streams.IBuffer: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class IHttpGetInputStreamResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d5d63463-13aa-4ee0-be95-a0c39fe91203}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Value(self) -> Windows.Storage.Streams.IInputStream: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
    Value = property(get_Value, None)
class IHttpGetStringResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9bac466d-8509-4775-b16d-8953f47a7f5f}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{728d4022-700d-4fe0-afa5-40299c58dbfd}')
    @winrt_commethod(6)
    def get_Method(self) -> WinRT_String: ...
    Method = property(get_Method, None)
class IHttpMethodFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3c51d10d-36d7-40f8-a86d-e759caf2f83f}')
    @winrt_commethod(6)
    def Create(self, method: WinRT_String) -> Windows.Web.Http.HttpMethod: ...
class IHttpMethodStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{64d171f0-d99a-4153-8dc6-d68cc4cce317}')
    @winrt_commethod(6)
    def get_Delete(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(7)
    def get_Get(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(8)
    def get_Head(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(9)
    def get_Options(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(10)
    def get_Patch(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(11)
    def get_Post(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(12)
    def get_Put(self) -> Windows.Web.Http.HttpMethod: ...
    Delete = property(get_Delete, None)
    Get = property(get_Get, None)
    Head = property(get_Head, None)
    Options = property(get_Options, None)
    Patch = property(get_Patch, None)
    Post = property(get_Post, None)
    Put = property(get_Put, None)
class IHttpMultipartContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{df916aff-9926-4ac9-aaf1-e0d04ef09bb9}')
    @winrt_commethod(6)
    def Add(self, content: Windows.Web.Http.IHttpContent) -> Void: ...
class IHttpMultipartContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7eb42e62-0222-4f20-b372-47d5db5d33b4}')
    @winrt_commethod(6)
    def CreateWithSubtype(self, subtype: WinRT_String) -> Windows.Web.Http.HttpMultipartContent: ...
    @winrt_commethod(7)
    def CreateWithSubtypeAndBoundary(self, subtype: WinRT_String, boundary: WinRT_String) -> Windows.Web.Http.HttpMultipartContent: ...
class IHttpMultipartFormDataContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{64d337e2-e967-4624-b6d1-cf74604a4a42}')
    @winrt_commethod(6)
    def Add(self, content: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(7)
    def AddWithName(self, content: Windows.Web.Http.IHttpContent, name: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def AddWithNameAndFileName(self, content: Windows.Web.Http.IHttpContent, name: WinRT_String, fileName: WinRT_String) -> Void: ...
class IHttpMultipartFormDataContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a04d7311-5017-4622-93a8-49b24a4fcbfc}')
    @winrt_commethod(6)
    def CreateWithBoundary(self, boundary: WinRT_String) -> Windows.Web.Http.HttpMultipartFormDataContent: ...
class IHttpRequestMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f5762b3c-74d4-4811-b5dc-9f8b4e2f9abf}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Web.Http.IHttpContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> Windows.Web.Http.Headers.HttpRequestHeaderCollection: ...
    @winrt_commethod(9)
    def get_Method(self) -> Windows.Web.Http.HttpMethod: ...
    @winrt_commethod(10)
    def put_Method(self, value: Windows.Web.Http.HttpMethod) -> Void: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def get_RequestUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_RequestUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(14)
    def get_TransportInformation(self) -> Windows.Web.Http.HttpTransportInformation: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    Properties = property(get_Properties, None)
    RequestUri = property(get_RequestUri, put_RequestUri)
    TransportInformation = property(get_TransportInformation, None)
class IHttpRequestMessage2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c3c60489-62c2-4a3f-9554-226e7c60bd96}')
    @winrt_commethod(6)
    def get_PrivacyAnnotation(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PrivacyAnnotation(self, value: WinRT_String) -> Void: ...
    PrivacyAnnotation = property(get_PrivacyAnnotation, put_PrivacyAnnotation)
class IHttpRequestMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5bac994e-3886-412e-aec3-52ec7f25616f}')
    @winrt_commethod(6)
    def Create(self, method: Windows.Web.Http.HttpMethod, uri: Windows.Foundation.Uri) -> Windows.Web.Http.HttpRequestMessage: ...
class IHttpRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6acf4da8-b5eb-4a35-a902-4217fbe820c5}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def get_ResponseMessage(self) -> Windows.Web.Http.HttpResponseMessage: ...
    @winrt_commethod(9)
    def get_Succeeded(self) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    Succeeded = property(get_Succeeded, None)
class IHttpResponseMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fee200fb-8664-44e0-95d9-42696199bffc}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Web.Http.IHttpContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: Windows.Web.Http.IHttpContent) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> Windows.Web.Http.Headers.HttpResponseHeaderCollection: ...
    @winrt_commethod(9)
    def get_IsSuccessStatusCode(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_ReasonPhrase(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ReasonPhrase(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_RequestMessage(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(13)
    def put_RequestMessage(self, value: Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_commethod(14)
    def get_Source(self) -> Windows.Web.Http.HttpResponseMessageSource: ...
    @winrt_commethod(15)
    def put_Source(self, value: Windows.Web.Http.HttpResponseMessageSource) -> Void: ...
    @winrt_commethod(16)
    def get_StatusCode(self) -> Windows.Web.Http.HttpStatusCode: ...
    @winrt_commethod(17)
    def put_StatusCode(self, value: Windows.Web.Http.HttpStatusCode) -> Void: ...
    @winrt_commethod(18)
    def get_Version(self) -> Windows.Web.Http.HttpVersion: ...
    @winrt_commethod(19)
    def put_Version(self, value: Windows.Web.Http.HttpVersion) -> Void: ...
    @winrt_commethod(20)
    def EnsureSuccessStatusCode(self) -> Windows.Web.Http.HttpResponseMessage: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    IsSuccessStatusCode = property(get_IsSuccessStatusCode, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    RequestMessage = property(get_RequestMessage, put_RequestMessage)
    Source = property(get_Source, put_Source)
    StatusCode = property(get_StatusCode, put_StatusCode)
    Version = property(get_Version, put_Version)
class IHttpResponseMessageFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{52a8af99-f095-43da-b60f-7cfc2bc7ea2f}')
    @winrt_commethod(6)
    def Create(self, statusCode: Windows.Web.Http.HttpStatusCode) -> Windows.Web.Http.HttpResponseMessage: ...
class IHttpStreamContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f3e64d9d-f725-407e-942f-0eda189809f4}')
    @winrt_commethod(6)
    def CreateFromInputStream(self, content: Windows.Storage.Streams.IInputStream) -> Windows.Web.Http.HttpStreamContent: ...
class IHttpStringContentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{46649d5b-2e93-48eb-8e61-19677878e57f}')
    @winrt_commethod(6)
    def CreateFromString(self, content: WinRT_String) -> Windows.Web.Http.HttpStringContent: ...
    @winrt_commethod(7)
    def CreateFromStringWithEncoding(self, content: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Web.Http.HttpStringContent: ...
    @winrt_commethod(8)
    def CreateFromStringWithEncodingAndMediaType(self, content: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding, mediaType: WinRT_String) -> Windows.Web.Http.HttpStringContent: ...
class IHttpTransportInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{70127198-c6a7-4ed0-833a-83fd8b8f178d}')
    @winrt_commethod(6)
    def get_ServerCertificate(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(7)
    def get_ServerCertificateErrorSeverity(self) -> Windows.Networking.Sockets.SocketSslErrorSeverity: ...
    @winrt_commethod(8)
    def get_ServerCertificateErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.ChainValidationResult]: ...
    @winrt_commethod(9)
    def get_ServerIntermediateCertificates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Cryptography.Certificates.Certificate]: ...
    ServerCertificate = property(get_ServerCertificate, None)
    ServerCertificateErrorSeverity = property(get_ServerCertificateErrorSeverity, None)
    ServerCertificateErrors = property(get_ServerCertificateErrors, None)
    ServerIntermediateCertificates = property(get_ServerIntermediateCertificates, None)
make_head(_module, 'HttpBufferContent')
make_head(_module, 'HttpClient')
make_head(_module, 'HttpCookie')
make_head(_module, 'HttpCookieCollection')
make_head(_module, 'HttpCookieManager')
make_head(_module, 'HttpFormUrlEncodedContent')
make_head(_module, 'HttpGetBufferResult')
make_head(_module, 'HttpGetInputStreamResult')
make_head(_module, 'HttpGetStringResult')
make_head(_module, 'HttpMethod')
make_head(_module, 'HttpMultipartContent')
make_head(_module, 'HttpMultipartFormDataContent')
make_head(_module, 'HttpProgress')
make_head(_module, 'HttpRequestMessage')
make_head(_module, 'HttpRequestResult')
make_head(_module, 'HttpResponseMessage')
make_head(_module, 'HttpStreamContent')
make_head(_module, 'HttpStringContent')
make_head(_module, 'HttpTransportInformation')
make_head(_module, 'IHttpBufferContentFactory')
make_head(_module, 'IHttpClient')
make_head(_module, 'IHttpClient2')
make_head(_module, 'IHttpClient3')
make_head(_module, 'IHttpClientFactory')
make_head(_module, 'IHttpContent')
make_head(_module, 'IHttpCookie')
make_head(_module, 'IHttpCookieFactory')
make_head(_module, 'IHttpCookieManager')
make_head(_module, 'IHttpFormUrlEncodedContentFactory')
make_head(_module, 'IHttpGetBufferResult')
make_head(_module, 'IHttpGetInputStreamResult')
make_head(_module, 'IHttpGetStringResult')
make_head(_module, 'IHttpMethod')
make_head(_module, 'IHttpMethodFactory')
make_head(_module, 'IHttpMethodStatics')
make_head(_module, 'IHttpMultipartContent')
make_head(_module, 'IHttpMultipartContentFactory')
make_head(_module, 'IHttpMultipartFormDataContent')
make_head(_module, 'IHttpMultipartFormDataContentFactory')
make_head(_module, 'IHttpRequestMessage')
make_head(_module, 'IHttpRequestMessage2')
make_head(_module, 'IHttpRequestMessageFactory')
make_head(_module, 'IHttpRequestResult')
make_head(_module, 'IHttpResponseMessage')
make_head(_module, 'IHttpResponseMessageFactory')
make_head(_module, 'IHttpStreamContentFactory')
make_head(_module, 'IHttpStringContentFactory')
make_head(_module, 'IHttpTransportInformation')
