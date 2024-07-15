from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.System.Diagnostics.DevicePortal
import win32more.Windows.Web.Http
import win32more.Windows.Win32.System.WinRT
class DevicePortalConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.DevicePortalConnection'
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection, win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RequestReceived(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection, win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionRequestReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RequestReceived(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetServerMessageWebSocketForRequest(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_mixinmethod
    def GetServerMessageWebSocketForRequest2(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection, request: win32more.Windows.Web.Http.HttpRequestMessage, messageType: win32more.Windows.Networking.Sockets.SocketMessageType, protocol: WinRT_String) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_mixinmethod
    def GetServerMessageWebSocketForRequest3(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection, request: win32more.Windows.Web.Http.HttpRequestMessage, messageType: win32more.Windows.Networking.Sockets.SocketMessageType, protocol: WinRT_String, outboundBufferSizeInBytes: UInt32, maxMessageSize: UInt32, receiveMode: win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_mixinmethod
    def GetServerStreamWebSocketForRequest(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocket: ...
    @winrt_mixinmethod
    def GetServerStreamWebSocketForRequest2(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection, request: win32more.Windows.Web.Http.HttpRequestMessage, protocol: WinRT_String, outboundBufferSizeInBytes: UInt32, noDelay: Boolean) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocket: ...
    @winrt_classmethod
    def GetForAppServiceConnection(cls: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionStatics, appServiceConnection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection: ...
    Closed = event()
    RequestReceived = event()
class DevicePortalConnectionClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionClosedEventArgs
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionClosedEventArgs) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedReason: ...
    Reason = property(get_Reason, None)
class DevicePortalConnectionClosedReason(Enum, Int32):
    Unknown = 0
    ResourceLimitsExceeded = 1
    ProtocolError = 2
    NotAuthorized = 3
    UserNotPresent = 4
    ServiceTerminated = 5
class DevicePortalConnectionRequestReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionRequestReceivedEventArgs
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionRequestReceivedEventArgs'
    @winrt_mixinmethod
    def get_RequestMessage(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionRequestReceivedEventArgs) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def get_ResponseMessage(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionRequestReceivedEventArgs) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    @winrt_mixinmethod
    def get_IsWebSocketUpgradeRequest(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnectionRequestReceivedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_WebSocketProtocolsRequested(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnectionRequestReceivedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnectionRequestReceivedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    IsWebSocketUpgradeRequest = property(get_IsWebSocketUpgradeRequest, None)
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    WebSocketProtocolsRequested = property(get_WebSocketProtocolsRequested, None)
class IDevicePortalConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalConnection'
    _iid_ = Guid('{0f447f51-1198-4da1-8d54-bdef393e09b6}')
    @winrt_commethod(6)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection, win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RequestReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection, win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionRequestReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RequestReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Closed = event()
    RequestReceived = event()
class IDevicePortalConnectionClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionClosedEventArgs'
    _iid_ = Guid('{fcf70e38-7032-428c-9f50-945c15a9f0cb}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedReason: ...
    Reason = property(get_Reason, None)
class IDevicePortalConnectionRequestReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionRequestReceivedEventArgs'
    _iid_ = Guid('{64dae045-6fda-4459-9ebd-ecce22e38559}')
    @winrt_commethod(6)
    def get_RequestMessage(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(7)
    def get_ResponseMessage(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
class IDevicePortalConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionStatics'
    _iid_ = Guid('{4bbe31e7-e9b9-4645-8fed-a53eea0edbd6}')
    @winrt_commethod(6)
    def GetForAppServiceConnection(self, appServiceConnection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection: ...
class IDevicePortalWebSocketConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnection'
    _iid_ = Guid('{67657920-d65a-42f0-aef4-787808098b7b}')
    @winrt_commethod(6)
    def GetServerMessageWebSocketForRequest(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_commethod(7)
    def GetServerMessageWebSocketForRequest2(self, request: win32more.Windows.Web.Http.HttpRequestMessage, messageType: win32more.Windows.Networking.Sockets.SocketMessageType, protocol: WinRT_String) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_commethod(8)
    def GetServerMessageWebSocketForRequest3(self, request: win32more.Windows.Web.Http.HttpRequestMessage, messageType: win32more.Windows.Networking.Sockets.SocketMessageType, protocol: WinRT_String, outboundBufferSizeInBytes: UInt32, maxMessageSize: UInt32, receiveMode: win32more.Windows.Networking.Sockets.MessageWebSocketReceiveMode) -> win32more.Windows.Networking.Sockets.ServerMessageWebSocket: ...
    @winrt_commethod(9)
    def GetServerStreamWebSocketForRequest(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocket: ...
    @winrt_commethod(10)
    def GetServerStreamWebSocketForRequest2(self, request: win32more.Windows.Web.Http.HttpRequestMessage, protocol: WinRT_String, outboundBufferSizeInBytes: UInt32, noDelay: Boolean) -> win32more.Windows.Networking.Sockets.ServerStreamWebSocket: ...
class IDevicePortalWebSocketConnectionRequestReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.IDevicePortalWebSocketConnectionRequestReceivedEventArgs'
    _iid_ = Guid('{79fdcaba-175c-4739-9f74-dda797c35b3f}')
    @winrt_commethod(6)
    def get_IsWebSocketUpgradeRequest(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_WebSocketProtocolsRequested(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsWebSocketUpgradeRequest = property(get_IsWebSocketUpgradeRequest, None)
    WebSocketProtocolsRequested = property(get_WebSocketProtocolsRequested, None)


make_ready(__name__)
