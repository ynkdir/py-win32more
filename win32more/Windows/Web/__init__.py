from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.Web
import win32more.Windows.Win32.System.WinRT
class IUriToStreamResolver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.IUriToStreamResolver'
    _iid_ = Guid('{b0aba86a-9aeb-4d3a-9590-003e3ca7e290}')
    @winrt_commethod(6)
    def UriToStreamAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IInputStream]: ...
class IWebErrorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.IWebErrorStatics'
    _iid_ = Guid('{fe616766-bf27-4064-87b7-6563bb11ce2e}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class WebError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.WebError'
    @winrt_classmethod
    def GetStatus(cls: win32more.Windows.Web.IWebErrorStatics, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class WebErrorStatus(Enum, Int32):
    Unknown = 0
    CertificateCommonNameIsIncorrect = 1
    CertificateExpired = 2
    CertificateContainsErrors = 3
    CertificateRevoked = 4
    CertificateIsInvalid = 5
    ServerUnreachable = 6
    Timeout = 7
    ErrorHttpInvalidServerResponse = 8
    ConnectionAborted = 9
    ConnectionReset = 10
    Disconnected = 11
    HttpToHttpsOnRedirection = 12
    HttpsToHttpOnRedirection = 13
    CannotConnect = 14
    HostNameNotResolved = 15
    OperationCanceled = 16
    RedirectFailed = 17
    UnexpectedStatusCode = 18
    UnexpectedRedirection = 19
    UnexpectedClientError = 20
    UnexpectedServerError = 21
    InsufficientRangeSupport = 22
    MissingContentLengthSupport = 23
    MultipleChoices = 300
    MovedPermanently = 301
    Found = 302
    SeeOther = 303
    NotModified = 304
    UseProxy = 305
    TemporaryRedirect = 307
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
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HttpVersionNotSupported = 505


make_ready(__name__)
