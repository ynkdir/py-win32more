from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WebSocket
WEB_SOCKET_MAX_CLOSE_REASON_LENGTH: UInt32 = 123
@winfunctype('websocket.dll')
def WebSocketCreateClientHandle(pProperties: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY), ulPropertyCount: UInt32, phWebSocket: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketBeginClientHandshake(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, pszSubprotocols: POINTER(win32more.Windows.Win32.Foundation.PSTR), ulSubprotocolCount: UInt32, pszExtensions: POINTER(win32more.Windows.Win32.Foundation.PSTR), ulExtensionCount: UInt32, pInitialHeaders: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER), ulInitialHeaderCount: UInt32, pAdditionalHeaders: POINTER(POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER)), pulAdditionalHeaderCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketEndClientHandshake(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, pResponseHeaders: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER), ulReponseHeaderCount: UInt32, pulSelectedExtensions: POINTER(UInt32), pulSelectedExtensionCount: POINTER(UInt32), pulSelectedSubprotocol: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketCreateServerHandle(pProperties: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY), ulPropertyCount: UInt32, phWebSocket: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketBeginServerHandshake(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, pszSubprotocolSelected: win32more.Windows.Win32.Foundation.PSTR, pszExtensionSelected: POINTER(win32more.Windows.Win32.Foundation.PSTR), ulExtensionSelectedCount: UInt32, pRequestHeaders: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER), ulRequestHeaderCount: UInt32, pResponseHeaders: POINTER(POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER)), pulResponseHeaderCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketEndServerHandshake(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketSend(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, BufferType: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE, pBuffer: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER), Context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketReceive(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, pBuffer: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER), pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketGetAction(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, eActionQueue: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE, pDataBuffers: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER), pulDataBufferCount: POINTER(UInt32), pAction: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION), pBufferType: POINTER(win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE), pvApplicationContext: POINTER(VoidPtr), pvActionContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('websocket.dll')
def WebSocketCompleteAction(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE, pvActionContext: VoidPtr, ulBytesTransferred: UInt32) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketAbortHandle(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketDeleteHandle(hWebSocket: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_HANDLE) -> Void: ...
@winfunctype('websocket.dll')
def WebSocketGetGlobalProperty(eType: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE, pvValue: VoidPtr, ulSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WEB_SOCKET_ACTION = Int32
WEB_SOCKET_NO_ACTION: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION = 0
WEB_SOCKET_SEND_TO_NETWORK_ACTION: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION = 1
WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION = 2
WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION = 3
WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION = 4
WEB_SOCKET_ACTION_QUEUE = Int32
WEB_SOCKET_SEND_ACTION_QUEUE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE = 1
WEB_SOCKET_RECEIVE_ACTION_QUEUE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE = 2
WEB_SOCKET_ALL_ACTION_QUEUE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE = 3
class WEB_SOCKET_BUFFER(Union):
    Data: _Data_e__Struct
    CloseStatus: _CloseStatus_e__Struct
    class _Data_e__Struct(Structure):
        pbBuffer: POINTER(Byte)
        ulBufferLength: UInt32
    class _CloseStatus_e__Struct(Structure):
        pbReason: POINTER(Byte)
        ulReasonLength: UInt32
        usStatus: UInt16
WEB_SOCKET_BUFFER_TYPE = Int32
WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483648
WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483647
WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483646
WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483645
WEB_SOCKET_CLOSE_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483644
WEB_SOCKET_PING_PONG_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483643
WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE = -2147483642
WEB_SOCKET_CLOSE_STATUS = Int32
WEB_SOCKET_SUCCESS_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1000
WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1001
WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1002
WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1003
WEB_SOCKET_EMPTY_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1005
WEB_SOCKET_ABORTED_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1006
WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1007
WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1008
WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1009
WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1010
WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1011
WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_CLOSE_STATUS = 1015
WEB_SOCKET_HANDLE = VoidPtr
class WEB_SOCKET_HTTP_HEADER(Structure):
    pcName: win32more.Windows.Win32.Foundation.PSTR
    ulNameLength: UInt32
    pcValue: win32more.Windows.Win32.Foundation.PSTR
    ulValueLength: UInt32
class WEB_SOCKET_PROPERTY(Structure):
    Type: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE
    pvValue: VoidPtr
    ulValueSize: UInt32
WEB_SOCKET_PROPERTY_TYPE = Int32
WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 0
WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 1
WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 2
WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 3
WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 4
WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 5
WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE: win32more.Windows.Win32.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE = 6


make_ready(__name__)
