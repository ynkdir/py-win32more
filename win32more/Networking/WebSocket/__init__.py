from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.WebSocket

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WEB_SOCKET_MAX_CLOSE_REASON_LENGTH = 123
WEB_SOCKET_HANDLE = IntPtr
WEB_SOCKET_CLOSE_STATUS = Int32
WEB_SOCKET_SUCCESS_CLOSE_STATUS = 1000
WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS = 1001
WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS = 1002
WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS = 1003
WEB_SOCKET_EMPTY_CLOSE_STATUS = 1005
WEB_SOCKET_ABORTED_CLOSE_STATUS = 1006
WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS = 1007
WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS = 1008
WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS = 1009
WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS = 1010
WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS = 1011
WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS = 1015
WEB_SOCKET_PROPERTY_TYPE = Int32
WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE = 0
WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE = 1
WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE = 2
WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE = 3
WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE = 4
WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE = 5
WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE = 6
WEB_SOCKET_ACTION_QUEUE = Int32
WEB_SOCKET_SEND_ACTION_QUEUE = 1
WEB_SOCKET_RECEIVE_ACTION_QUEUE = 2
WEB_SOCKET_ALL_ACTION_QUEUE = 3
WEB_SOCKET_BUFFER_TYPE = Int32
WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE = -2147483648
WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE = -2147483647
WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE = -2147483646
WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE = -2147483645
WEB_SOCKET_CLOSE_BUFFER_TYPE = -2147483644
WEB_SOCKET_PING_PONG_BUFFER_TYPE = -2147483643
WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE = -2147483642
WEB_SOCKET_ACTION = Int32
WEB_SOCKET_NO_ACTION = 0
WEB_SOCKET_SEND_TO_NETWORK_ACTION = 1
WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION = 2
WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION = 3
WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION = 4
def _define_WEB_SOCKET_PROPERTY_head():
    class WEB_SOCKET_PROPERTY(Structure):
        pass
    return WEB_SOCKET_PROPERTY
def _define_WEB_SOCKET_PROPERTY():
    WEB_SOCKET_PROPERTY = win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_head
    WEB_SOCKET_PROPERTY._fields_ = [
        ("Type", win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE),
        ("pvValue", c_void_p),
        ("ulValueSize", UInt32),
    ]
    return WEB_SOCKET_PROPERTY
def _define_WEB_SOCKET_HTTP_HEADER_head():
    class WEB_SOCKET_HTTP_HEADER(Structure):
        pass
    return WEB_SOCKET_HTTP_HEADER
def _define_WEB_SOCKET_HTTP_HEADER():
    WEB_SOCKET_HTTP_HEADER = win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head
    WEB_SOCKET_HTTP_HEADER._fields_ = [
        ("pcName", win32more.Foundation.PSTR),
        ("ulNameLength", UInt32),
        ("pcValue", win32more.Foundation.PSTR),
        ("ulValueLength", UInt32),
    ]
    return WEB_SOCKET_HTTP_HEADER
def _define_WEB_SOCKET_BUFFER_head():
    class WEB_SOCKET_BUFFER(Union):
        pass
    return WEB_SOCKET_BUFFER
def _define_WEB_SOCKET_BUFFER():
    WEB_SOCKET_BUFFER = win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head
    class WEB_SOCKET_BUFFER__Data_e__Struct(Structure):
        pass
    WEB_SOCKET_BUFFER__Data_e__Struct._fields_ = [
        ("pbBuffer", c_char_p_no),
        ("ulBufferLength", UInt32),
    ]
    class WEB_SOCKET_BUFFER__CloseStatus_e__Struct(Structure):
        pass
    WEB_SOCKET_BUFFER__CloseStatus_e__Struct._fields_ = [
        ("pbReason", c_char_p_no),
        ("ulReasonLength", UInt32),
        ("usStatus", UInt16),
    ]
    WEB_SOCKET_BUFFER._fields_ = [
        ("Data", WEB_SOCKET_BUFFER__Data_e__Struct),
        ("CloseStatus", WEB_SOCKET_BUFFER__CloseStatus_e__Struct),
    ]
    return WEB_SOCKET_BUFFER
def _define_WebSocketCreateClientHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY),UInt32,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HANDLE), use_last_error=False)(("WebSocketCreateClientHandle", windll["websocket"]), ((1, 'pProperties'),(1, 'ulPropertyCount'),(1, 'phWebSocket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketBeginClientHandshake():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,POINTER(win32more.Foundation.PSTR),UInt32,POINTER(win32more.Foundation.PSTR),UInt32,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER),UInt32,POINTER(POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head)),POINTER(UInt32), use_last_error=False)(("WebSocketBeginClientHandshake", windll["websocket"]), ((1, 'hWebSocket'),(1, 'pszSubprotocols'),(1, 'ulSubprotocolCount'),(1, 'pszExtensions'),(1, 'ulExtensionCount'),(1, 'pInitialHeaders'),(1, 'ulInitialHeaderCount'),(1, 'pAdditionalHeaders'),(1, 'pulAdditionalHeaderCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketEndClientHandshake():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("WebSocketEndClientHandshake", windll["websocket"]), ((1, 'hWebSocket'),(1, 'pResponseHeaders'),(1, 'ulReponseHeaderCount'),(1, 'pulSelectedExtensions'),(1, 'pulSelectedExtensionCount'),(1, 'pulSelectedSubprotocol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketCreateServerHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY),UInt32,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HANDLE), use_last_error=False)(("WebSocketCreateServerHandle", windll["websocket"]), ((1, 'pProperties'),(1, 'ulPropertyCount'),(1, 'phWebSocket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketBeginServerHandshake():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR),UInt32,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER),UInt32,POINTER(POINTER(win32more.Networking.WebSocket.WEB_SOCKET_HTTP_HEADER_head)),POINTER(UInt32), use_last_error=False)(("WebSocketBeginServerHandshake", windll["websocket"]), ((1, 'hWebSocket'),(1, 'pszSubprotocolSelected'),(1, 'pszExtensionSelected'),(1, 'ulExtensionSelectedCount'),(1, 'pRequestHeaders'),(1, 'ulRequestHeaderCount'),(1, 'pResponseHeaders'),(1, 'pulResponseHeaderCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketEndServerHandshake():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, use_last_error=False)(("WebSocketEndServerHandshake", windll["websocket"]), ((1, 'hWebSocket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketSend():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head),c_void_p, use_last_error=False)(("WebSocketSend", windll["websocket"]), ((1, 'hWebSocket'),(1, 'BufferType'),(1, 'pBuffer'),(1, 'Context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketReceive():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_head),c_void_p, use_last_error=False)(("WebSocketReceive", windll["websocket"]), ((1, 'hWebSocket'),(1, 'pBuffer'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketGetAction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,win32more.Networking.WebSocket.WEB_SOCKET_ACTION_QUEUE,POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER),POINTER(UInt32),POINTER(win32more.Networking.WebSocket.WEB_SOCKET_ACTION),POINTER(win32more.Networking.WebSocket.WEB_SOCKET_BUFFER_TYPE),POINTER(c_void_p),POINTER(c_void_p), use_last_error=False)(("WebSocketGetAction", windll["websocket"]), ((1, 'hWebSocket'),(1, 'eActionQueue'),(1, 'pDataBuffers'),(1, 'pulDataBufferCount'),(1, 'pAction'),(1, 'pBufferType'),(1, 'pvApplicationContext'),(1, 'pvActionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketCompleteAction():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE,c_void_p,UInt32, use_last_error=False)(("WebSocketCompleteAction", windll["websocket"]), ((1, 'hWebSocket'),(1, 'pvActionContext'),(1, 'ulBytesTransferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketAbortHandle():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, use_last_error=False)(("WebSocketAbortHandle", windll["websocket"]), ((1, 'hWebSocket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketDeleteHandle():
    try:
        return WINFUNCTYPE(Void,win32more.Networking.WebSocket.WEB_SOCKET_HANDLE, use_last_error=False)(("WebSocketDeleteHandle", windll["websocket"]), ((1, 'hWebSocket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebSocketGetGlobalProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WebSocket.WEB_SOCKET_PROPERTY_TYPE,POINTER(Void),POINTER(UInt32), use_last_error=False)(("WebSocketGetGlobalProperty", windll["websocket"]), ((1, 'eType'),(1, 'pvValue'),(1, 'ulSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WEB_SOCKET_MAX_CLOSE_REASON_LENGTH",
    "WEB_SOCKET_HANDLE",
    "WEB_SOCKET_CLOSE_STATUS",
    "WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    "WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS",
    "WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    "WEB_SOCKET_EMPTY_CLOSE_STATUS",
    "WEB_SOCKET_ABORTED_CLOSE_STATUS",
    "WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    "WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    "WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    "WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    "WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
    "WEB_SOCKET_PROPERTY_TYPE",
    "WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE",
    "WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE",
    "WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE",
    "WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE",
    "WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE",
    "WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE",
    "WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE",
    "WEB_SOCKET_ACTION_QUEUE",
    "WEB_SOCKET_SEND_ACTION_QUEUE",
    "WEB_SOCKET_RECEIVE_ACTION_QUEUE",
    "WEB_SOCKET_ALL_ACTION_QUEUE",
    "WEB_SOCKET_BUFFER_TYPE",
    "WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE",
    "WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE",
    "WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE",
    "WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE",
    "WEB_SOCKET_CLOSE_BUFFER_TYPE",
    "WEB_SOCKET_PING_PONG_BUFFER_TYPE",
    "WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE",
    "WEB_SOCKET_ACTION",
    "WEB_SOCKET_NO_ACTION",
    "WEB_SOCKET_SEND_TO_NETWORK_ACTION",
    "WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION",
    "WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION",
    "WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION",
    "WEB_SOCKET_PROPERTY",
    "WEB_SOCKET_HTTP_HEADER",
    "WEB_SOCKET_BUFFER",
    "WebSocketCreateClientHandle",
    "WebSocketBeginClientHandshake",
    "WebSocketEndClientHandshake",
    "WebSocketCreateServerHandle",
    "WebSocketBeginServerHandshake",
    "WebSocketEndServerHandshake",
    "WebSocketSend",
    "WebSocketReceive",
    "WebSocketGetAction",
    "WebSocketCompleteAction",
    "WebSocketAbortHandle",
    "WebSocketDeleteHandle",
    "WebSocketGetGlobalProperty",
]
