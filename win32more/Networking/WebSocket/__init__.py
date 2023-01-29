from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.WebSocket
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
WEB_SOCKET_MAX_CLOSE_REASON_LENGTH: UInt32 = 123
@winfunctype('websocket.dll')
def WebSocketCreateClientHandle(pProperties: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_head), ulPropertyCount: UInt32, phWebSocket: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketBeginClientHandshake(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, pszSubprotocols: POINTER(win32more.Foundation.PSTR), ulSubprotocolCount: UInt32, pszExtensions: POINTER(win32more.Foundation.PSTR), ulExtensionCount: UInt32, pInitialHeaders: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head), ulInitialHeaderCount: UInt32, pAdditionalHeaders: POINTER(POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head)), pulAdditionalHeaderCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketEndClientHandshake(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, pResponseHeaders: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head), ulReponseHeaderCount: UInt32, pulSelectedExtensions: POINTER(UInt32), pulSelectedExtensionCount: POINTER(UInt32), pulSelectedSubprotocol: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketCreateServerHandle(pProperties: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_head), ulPropertyCount: UInt32, phWebSocket: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketBeginServerHandshake(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, pszSubprotocolSelected: win32more.Foundation.PSTR, pszExtensionSelected: POINTER(win32more.Foundation.PSTR), ulExtensionSelectedCount: UInt32, pRequestHeaders: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head), ulRequestHeaderCount: UInt32, pResponseHeaders: POINTER(POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head)), pulResponseHeaderCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketEndServerHandshake(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketSend(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, BufferType: win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE, pBuffer: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head), Context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketReceive(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, pBuffer: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head), pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketGetAction(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, eActionQueue: win32more.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE, pDataBuffers: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head), pulDataBufferCount: POINTER(UInt32), pAction: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_ACTION), pBufferType: POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE), pvApplicationContext: POINTER(c_void_p), pvActionContext: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketCompleteAction(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, pvActionContext: c_void_p, ulBytesTransferred: UInt32) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketAbortHandle(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketDeleteHandle(hWebSocket: win32more.Networking.WebSocket.WEB_SOCKET_HANDLE) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketGetGlobalProperty(eType: win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE, pvValue: c_void_p, ulSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
WEB_SOCKET_ACTION = Int32
WEB_SOCKET_NO_ACTION: WEB_SOCKET_ACTION = 0
WEB_SOCKET_SEND_TO_NETWORK_ACTION: WEB_SOCKET_ACTION = 1
WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION: WEB_SOCKET_ACTION = 2
WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION: WEB_SOCKET_ACTION = 3
WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION: WEB_SOCKET_ACTION = 4
WEB_SOCKET_ACTION_QUEUE = Int32
WEB_SOCKET_SEND_ACTION_QUEUE: WEB_SOCKET_ACTION_QUEUE = 1
WEB_SOCKET_RECEIVE_ACTION_QUEUE: WEB_SOCKET_ACTION_QUEUE = 2
WEB_SOCKET_ALL_ACTION_QUEUE: WEB_SOCKET_ACTION_QUEUE = 3
class WEB_SOCKET_BUFFER(Union):
    Data: _Data_e__Struct
    CloseStatus: _CloseStatus_e__Struct
    class _Data_e__Struct(Structure):
        pbBuffer: c_char_p_no
        ulBufferLength: UInt32
    class _CloseStatus_e__Struct(Structure):
        pbReason: c_char_p_no
        ulReasonLength: UInt32
        usStatus: UInt16
WEB_SOCKET_BUFFER_TYPE = Int32
WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483648
WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483647
WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483646
WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483645
WEB_SOCKET_CLOSE_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483644
WEB_SOCKET_PING_PONG_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483643
WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE: WEB_SOCKET_BUFFER_TYPE = -2147483642
WEB_SOCKET_CLOSE_STATUS = Int32
WEB_SOCKET_SUCCESS_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1000
WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1001
WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1002
WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1003
WEB_SOCKET_EMPTY_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1005
WEB_SOCKET_ABORTED_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1006
WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1007
WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1008
WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1009
WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1010
WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1011
WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS: WEB_SOCKET_CLOSE_STATUS = 1015
WEB_SOCKET_HANDLE = IntPtr
class WEB_SOCKET_HTTP_HEADER(Structure):
    pcName: win32more.Foundation.PSTR
    ulNameLength: UInt32
    pcValue: win32more.Foundation.PSTR
    ulValueLength: UInt32
class WEB_SOCKET_PROPERTY(Structure):
    Type: win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE
    pvValue: c_void_p
    ulValueSize: UInt32
WEB_SOCKET_PROPERTY_TYPE = Int32
WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 0
WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 1
WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 2
WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 3
WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 4
WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 5
WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE: WEB_SOCKET_PROPERTY_TYPE = 6
make_head(_module, 'WEB_SOCKET_BUFFER')
make_head(_module, 'WEB_SOCKET_HTTP_HEADER')
make_head(_module, 'WEB_SOCKET_PROPERTY')
__all__ = [
    "WEB_SOCKET_ABORTED_CLOSE_STATUS",
    "WEB_SOCKET_ACTION",
    "WEB_SOCKET_ACTION_QUEUE",
    "WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE",
    "WEB_SOCKET_ALL_ACTION_QUEUE",
    "WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE",
    "WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE",
    "WEB_SOCKET_BUFFER",
    "WEB_SOCKET_BUFFER_TYPE",
    "WEB_SOCKET_CLOSE_BUFFER_TYPE",
    "WEB_SOCKET_CLOSE_STATUS",
    "WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE",
    "WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE",
    "WEB_SOCKET_EMPTY_CLOSE_STATUS",
    "WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS",
    "WEB_SOCKET_HANDLE",
    "WEB_SOCKET_HTTP_HEADER",
    "WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION",
    "WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION",
    "WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    "WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    "WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE",
    "WEB_SOCKET_MAX_CLOSE_REASON_LENGTH",
    "WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    "WEB_SOCKET_NO_ACTION",
    "WEB_SOCKET_PING_PONG_BUFFER_TYPE",
    "WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    "WEB_SOCKET_PROPERTY",
    "WEB_SOCKET_PROPERTY_TYPE",
    "WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_RECEIVE_ACTION_QUEUE",
    "WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE",
    "WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION",
    "WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_SEND_ACTION_QUEUE",
    "WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE",
    "WEB_SOCKET_SEND_TO_NETWORK_ACTION",
    "WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    "WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE",
    "WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE",
    "WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    "WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE",
    "WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE",
    "WebSocketAbortHandle",
    "WebSocketBeginClientHandshake",
    "WebSocketBeginServerHandshake",
    "WebSocketCompleteAction",
    "WebSocketCreateClientHandle",
    "WebSocketCreateServerHandle",
    "WebSocketDeleteHandle",
    "WebSocketEndClientHandshake",
    "WebSocketEndServerHandshake",
    "WebSocketGetAction",
    "WebSocketGetGlobalProperty",
    "WebSocketReceive",
    "WebSocketSend",
]
_arch_optional = [
]
