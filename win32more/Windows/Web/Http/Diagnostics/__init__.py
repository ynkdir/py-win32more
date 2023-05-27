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
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Diagnostics
import win32more.Windows.Web.Http
import win32more.Windows.Web.Http.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HttpDiagnosticProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticProvider'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider) -> Void: ...
    @winrt_mixinmethod
    def add_RequestSent(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestSentEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestSent(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ResponseReceived(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderResponseReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResponseReceived(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RequestResponseCompleted(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestResponseCompleted(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromProcessDiagnosticInfo(cls: Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderStatics, processDiagnosticInfo: win32more.Windows.System.Diagnostics.ProcessDiagnosticInfo) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider: ...
class HttpDiagnosticProviderRequestResponseCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseCompletedEventArgs'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Timestamps(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseTimestamps: ...
    @winrt_mixinmethod
    def get_RequestedUri(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ProcessId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_ThreadId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Initiator(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator: ...
    @winrt_mixinmethod
    def get_SourceLocations(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticSourceLocation]: ...
    ActivityId = property(get_ActivityId, None)
    Timestamps = property(get_Timestamps, None)
    RequestedUri = property(get_RequestedUri, None)
    ProcessId = property(get_ProcessId, None)
    ThreadId = property(get_ThreadId, None)
    Initiator = property(get_Initiator, None)
    SourceLocations = property(get_SourceLocations, None)
class HttpDiagnosticProviderRequestResponseTimestamps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseTimestamps'
    @winrt_mixinmethod
    def get_CacheCheckedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ConnectionInitiatedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_NameResolvedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_SslNegotiatedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ConnectionCompletedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_RequestSentTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_RequestCompletedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ResponseReceivedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_ResponseCompletedTimestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    CacheCheckedTimestamp = property(get_CacheCheckedTimestamp, None)
    ConnectionInitiatedTimestamp = property(get_ConnectionInitiatedTimestamp, None)
    NameResolvedTimestamp = property(get_NameResolvedTimestamp, None)
    SslNegotiatedTimestamp = property(get_SslNegotiatedTimestamp, None)
    ConnectionCompletedTimestamp = property(get_ConnectionCompletedTimestamp, None)
    RequestSentTimestamp = property(get_RequestSentTimestamp, None)
    RequestCompletedTimestamp = property(get_RequestCompletedTimestamp, None)
    ResponseReceivedTimestamp = property(get_ResponseReceivedTimestamp, None)
    ResponseCompletedTimestamp = property(get_ResponseCompletedTimestamp, None)
class HttpDiagnosticProviderRequestSentEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestSentEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ProcessId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_ThreadId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Initiator(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator: ...
    @winrt_mixinmethod
    def get_SourceLocations(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticSourceLocation]: ...
    Timestamp = property(get_Timestamp, None)
    ActivityId = property(get_ActivityId, None)
    Message = property(get_Message, None)
    ProcessId = property(get_ProcessId, None)
    ThreadId = property(get_ThreadId, None)
    Initiator = property(get_Initiator, None)
    SourceLocations = property(get_SourceLocations, None)
class HttpDiagnosticProviderResponseReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderResponseReceivedEventArgs
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticProviderResponseReceivedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderResponseReceivedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderResponseReceivedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderResponseReceivedEventArgs) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    Timestamp = property(get_Timestamp, None)
    ActivityId = property(get_ActivityId, None)
    Message = property(get_Message, None)
HttpDiagnosticRequestInitiator = Int32
HttpDiagnosticRequestInitiator_ParsedElement: HttpDiagnosticRequestInitiator = 0
HttpDiagnosticRequestInitiator_Script: HttpDiagnosticRequestInitiator = 1
HttpDiagnosticRequestInitiator_Image: HttpDiagnosticRequestInitiator = 2
HttpDiagnosticRequestInitiator_Link: HttpDiagnosticRequestInitiator = 3
HttpDiagnosticRequestInitiator_Style: HttpDiagnosticRequestInitiator = 4
HttpDiagnosticRequestInitiator_XmlHttpRequest: HttpDiagnosticRequestInitiator = 5
HttpDiagnosticRequestInitiator_Media: HttpDiagnosticRequestInitiator = 6
HttpDiagnosticRequestInitiator_HtmlDownload: HttpDiagnosticRequestInitiator = 7
HttpDiagnosticRequestInitiator_Prefetch: HttpDiagnosticRequestInitiator = 8
HttpDiagnosticRequestInitiator_Other: HttpDiagnosticRequestInitiator = 9
HttpDiagnosticRequestInitiator_CrossOriginPreFlight: HttpDiagnosticRequestInitiator = 10
HttpDiagnosticRequestInitiator_Fetch: HttpDiagnosticRequestInitiator = 11
HttpDiagnosticRequestInitiator_Beacon: HttpDiagnosticRequestInitiator = 12
class HttpDiagnosticSourceLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticSourceLocation
    _classid_ = 'Windows.Web.Http.Diagnostics.HttpDiagnosticSourceLocation'
    @winrt_mixinmethod
    def get_SourceUri(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticSourceLocation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_LineNumber(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticSourceLocation) -> UInt64: ...
    @winrt_mixinmethod
    def get_ColumnNumber(self: win32more.Windows.Web.Http.Diagnostics.IHttpDiagnosticSourceLocation) -> UInt64: ...
    SourceUri = property(get_SourceUri, None)
    LineNumber = property(get_LineNumber, None)
    ColumnNumber = property(get_ColumnNumber, None)
HttpDiagnosticsContract: UInt32 = 131072
class IHttpDiagnosticProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProvider'
    _iid_ = Guid('{bd811501-a056-4d39-b174-833b7b03b02c}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def add_RequestSent(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestSentEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RequestSent(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ResponseReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderResponseReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ResponseReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_RequestResponseCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider, win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RequestResponseCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IHttpDiagnosticProviderRequestResponseCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseCompletedEventArgs'
    _iid_ = Guid('{735f98ee-94f6-4532-b26e-61e1b1e4efd4}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Timestamps(self) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProviderRequestResponseTimestamps: ...
    @winrt_commethod(8)
    def get_RequestedUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_ProcessId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ThreadId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Initiator(self) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator: ...
    @winrt_commethod(12)
    def get_SourceLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticSourceLocation]: ...
    ActivityId = property(get_ActivityId, None)
    Timestamps = property(get_Timestamps, None)
    RequestedUri = property(get_RequestedUri, None)
    ProcessId = property(get_ProcessId, None)
    ThreadId = property(get_ThreadId, None)
    Initiator = property(get_Initiator, None)
    SourceLocations = property(get_SourceLocations, None)
class IHttpDiagnosticProviderRequestResponseTimestamps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestResponseTimestamps'
    _iid_ = Guid('{e0afde10-55cf-4c01-91d4-a20557d849f0}')
    @winrt_commethod(6)
    def get_CacheCheckedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_ConnectionInitiatedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def get_NameResolvedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_SslNegotiatedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(10)
    def get_ConnectionCompletedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def get_RequestSentTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(12)
    def get_RequestCompletedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(13)
    def get_ResponseReceivedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(14)
    def get_ResponseCompletedTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    CacheCheckedTimestamp = property(get_CacheCheckedTimestamp, None)
    ConnectionInitiatedTimestamp = property(get_ConnectionInitiatedTimestamp, None)
    NameResolvedTimestamp = property(get_NameResolvedTimestamp, None)
    SslNegotiatedTimestamp = property(get_SslNegotiatedTimestamp, None)
    ConnectionCompletedTimestamp = property(get_ConnectionCompletedTimestamp, None)
    RequestSentTimestamp = property(get_RequestSentTimestamp, None)
    RequestCompletedTimestamp = property(get_RequestCompletedTimestamp, None)
    ResponseReceivedTimestamp = property(get_ResponseReceivedTimestamp, None)
    ResponseCompletedTimestamp = property(get_ResponseCompletedTimestamp, None)
class IHttpDiagnosticProviderRequestSentEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderRequestSentEventArgs'
    _iid_ = Guid('{3f5196d0-4c1f-4ebe-a57a-06930771c50d}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_Message(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(9)
    def get_ProcessId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ThreadId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Initiator(self) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator: ...
    @winrt_commethod(12)
    def get_SourceLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticSourceLocation]: ...
    Timestamp = property(get_Timestamp, None)
    ActivityId = property(get_ActivityId, None)
    Message = property(get_Message, None)
    ProcessId = property(get_ProcessId, None)
    ThreadId = property(get_ThreadId, None)
    Initiator = property(get_Initiator, None)
    SourceLocations = property(get_SourceLocations, None)
class IHttpDiagnosticProviderResponseReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderResponseReceivedEventArgs'
    _iid_ = Guid('{a0a2566c-ab5f-4d66-bb2d-084cf41635d0}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_ActivityId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_Message(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    Timestamp = property(get_Timestamp, None)
    ActivityId = property(get_ActivityId, None)
    Message = property(get_Message, None)
class IHttpDiagnosticProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticProviderStatics'
    _iid_ = Guid('{5b824ec1-6a6c-47cc-afec-1e86bc26053b}')
    @winrt_commethod(6)
    def CreateFromProcessDiagnosticInfo(self, processDiagnosticInfo: win32more.Windows.System.Diagnostics.ProcessDiagnosticInfo) -> win32more.Windows.Web.Http.Diagnostics.HttpDiagnosticProvider: ...
class IHttpDiagnosticSourceLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.Http.Diagnostics.IHttpDiagnosticSourceLocation'
    _iid_ = Guid('{54a9d260-8860-423f-b6fa-d77716f647a7}')
    @winrt_commethod(6)
    def get_SourceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_LineNumber(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ColumnNumber(self) -> UInt64: ...
    SourceUri = property(get_SourceUri, None)
    LineNumber = property(get_LineNumber, None)
    ColumnNumber = property(get_ColumnNumber, None)
make_head(_module, 'HttpDiagnosticProvider')
make_head(_module, 'HttpDiagnosticProviderRequestResponseCompletedEventArgs')
make_head(_module, 'HttpDiagnosticProviderRequestResponseTimestamps')
make_head(_module, 'HttpDiagnosticProviderRequestSentEventArgs')
make_head(_module, 'HttpDiagnosticProviderResponseReceivedEventArgs')
make_head(_module, 'HttpDiagnosticSourceLocation')
make_head(_module, 'IHttpDiagnosticProvider')
make_head(_module, 'IHttpDiagnosticProviderRequestResponseCompletedEventArgs')
make_head(_module, 'IHttpDiagnosticProviderRequestResponseTimestamps')
make_head(_module, 'IHttpDiagnosticProviderRequestSentEventArgs')
make_head(_module, 'IHttpDiagnosticProviderResponseReceivedEventArgs')
make_head(_module, 'IHttpDiagnosticProviderStatics')
make_head(_module, 'IHttpDiagnosticSourceLocation')
