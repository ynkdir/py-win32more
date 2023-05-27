from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.Web
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    def GetStatus(cls: Windows.Web.IWebErrorStatics, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
WebErrorStatus = Int32
WebErrorStatus_Unknown: WebErrorStatus = 0
WebErrorStatus_CertificateCommonNameIsIncorrect: WebErrorStatus = 1
WebErrorStatus_CertificateExpired: WebErrorStatus = 2
WebErrorStatus_CertificateContainsErrors: WebErrorStatus = 3
WebErrorStatus_CertificateRevoked: WebErrorStatus = 4
WebErrorStatus_CertificateIsInvalid: WebErrorStatus = 5
WebErrorStatus_ServerUnreachable: WebErrorStatus = 6
WebErrorStatus_Timeout: WebErrorStatus = 7
WebErrorStatus_ErrorHttpInvalidServerResponse: WebErrorStatus = 8
WebErrorStatus_ConnectionAborted: WebErrorStatus = 9
WebErrorStatus_ConnectionReset: WebErrorStatus = 10
WebErrorStatus_Disconnected: WebErrorStatus = 11
WebErrorStatus_HttpToHttpsOnRedirection: WebErrorStatus = 12
WebErrorStatus_HttpsToHttpOnRedirection: WebErrorStatus = 13
WebErrorStatus_CannotConnect: WebErrorStatus = 14
WebErrorStatus_HostNameNotResolved: WebErrorStatus = 15
WebErrorStatus_OperationCanceled: WebErrorStatus = 16
WebErrorStatus_RedirectFailed: WebErrorStatus = 17
WebErrorStatus_UnexpectedStatusCode: WebErrorStatus = 18
WebErrorStatus_UnexpectedRedirection: WebErrorStatus = 19
WebErrorStatus_UnexpectedClientError: WebErrorStatus = 20
WebErrorStatus_UnexpectedServerError: WebErrorStatus = 21
WebErrorStatus_InsufficientRangeSupport: WebErrorStatus = 22
WebErrorStatus_MissingContentLengthSupport: WebErrorStatus = 23
WebErrorStatus_MultipleChoices: WebErrorStatus = 300
WebErrorStatus_MovedPermanently: WebErrorStatus = 301
WebErrorStatus_Found: WebErrorStatus = 302
WebErrorStatus_SeeOther: WebErrorStatus = 303
WebErrorStatus_NotModified: WebErrorStatus = 304
WebErrorStatus_UseProxy: WebErrorStatus = 305
WebErrorStatus_TemporaryRedirect: WebErrorStatus = 307
WebErrorStatus_BadRequest: WebErrorStatus = 400
WebErrorStatus_Unauthorized: WebErrorStatus = 401
WebErrorStatus_PaymentRequired: WebErrorStatus = 402
WebErrorStatus_Forbidden: WebErrorStatus = 403
WebErrorStatus_NotFound: WebErrorStatus = 404
WebErrorStatus_MethodNotAllowed: WebErrorStatus = 405
WebErrorStatus_NotAcceptable: WebErrorStatus = 406
WebErrorStatus_ProxyAuthenticationRequired: WebErrorStatus = 407
WebErrorStatus_RequestTimeout: WebErrorStatus = 408
WebErrorStatus_Conflict: WebErrorStatus = 409
WebErrorStatus_Gone: WebErrorStatus = 410
WebErrorStatus_LengthRequired: WebErrorStatus = 411
WebErrorStatus_PreconditionFailed: WebErrorStatus = 412
WebErrorStatus_RequestEntityTooLarge: WebErrorStatus = 413
WebErrorStatus_RequestUriTooLong: WebErrorStatus = 414
WebErrorStatus_UnsupportedMediaType: WebErrorStatus = 415
WebErrorStatus_RequestedRangeNotSatisfiable: WebErrorStatus = 416
WebErrorStatus_ExpectationFailed: WebErrorStatus = 417
WebErrorStatus_InternalServerError: WebErrorStatus = 500
WebErrorStatus_NotImplemented: WebErrorStatus = 501
WebErrorStatus_BadGateway: WebErrorStatus = 502
WebErrorStatus_ServiceUnavailable: WebErrorStatus = 503
WebErrorStatus_GatewayTimeout: WebErrorStatus = 504
WebErrorStatus_HttpVersionNotSupported: WebErrorStatus = 505
make_head(_module, 'IUriToStreamResolver')
make_head(_module, 'IWebErrorStatics')
make_head(_module, 'WebError')
