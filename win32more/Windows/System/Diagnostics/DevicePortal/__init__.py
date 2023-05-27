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
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.Sockets
import win32more.Windows.System.Diagnostics.DevicePortal
import win32more.Windows.Web.Http
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    def GetForAppServiceConnection(cls: Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionStatics, appServiceConnection: win32more.Windows.ApplicationModel.AppService.AppServiceConnection) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnection: ...
class DevicePortalConnectionClosedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionClosedEventArgs
    _classid_ = 'Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.System.Diagnostics.DevicePortal.IDevicePortalConnectionClosedEventArgs) -> win32more.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedReason: ...
    Reason = property(get_Reason, None)
DevicePortalConnectionClosedReason = Int32
DevicePortalConnectionClosedReason_Unknown: DevicePortalConnectionClosedReason = 0
DevicePortalConnectionClosedReason_ResourceLimitsExceeded: DevicePortalConnectionClosedReason = 1
DevicePortalConnectionClosedReason_ProtocolError: DevicePortalConnectionClosedReason = 2
DevicePortalConnectionClosedReason_NotAuthorized: DevicePortalConnectionClosedReason = 3
DevicePortalConnectionClosedReason_UserNotPresent: DevicePortalConnectionClosedReason = 4
DevicePortalConnectionClosedReason_ServiceTerminated: DevicePortalConnectionClosedReason = 5
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
    RequestMessage = property(get_RequestMessage, None)
    ResponseMessage = property(get_ResponseMessage, None)
    IsWebSocketUpgradeRequest = property(get_IsWebSocketUpgradeRequest, None)
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
make_head(_module, 'DevicePortalConnection')
make_head(_module, 'DevicePortalConnectionClosedEventArgs')
make_head(_module, 'DevicePortalConnectionRequestReceivedEventArgs')
make_head(_module, 'IDevicePortalConnection')
make_head(_module, 'IDevicePortalConnectionClosedEventArgs')
make_head(_module, 'IDevicePortalConnectionRequestReceivedEventArgs')
make_head(_module, 'IDevicePortalConnectionStatics')
make_head(_module, 'IDevicePortalWebSocketConnection')
make_head(_module, 'IDevicePortalWebSocketConnectionRequestReceivedEventArgs')
