from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Mapi
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
MAPI_OLE = 1
MAPI_OLE_STATIC = 2
MAPI_ORIG = 0
MAPI_TO = 1
MAPI_CC = 2
MAPI_BCC = 3
MAPI_UNREAD = 1
MAPI_RECEIPT_REQUESTED = 2
MAPI_SENT = 4
MAPI_LOGON_UI = 1
MAPI_PASSWORD_UI = 131072
MAPI_NEW_SESSION = 2
MAPI_FORCE_DOWNLOAD = 4096
MAPI_EXTENDED = 32
MAPI_DIALOG = 8
MAPI_FORCE_UNICODE = 262144
MAPI_UNREAD_ONLY = 32
MAPI_GUARANTEE_FIFO = 256
MAPI_LONG_MSGID = 16384
MAPI_PEEK = 128
MAPI_SUPPRESS_ATTACH = 2048
MAPI_ENVELOPE_ONLY = 64
MAPI_BODY_AS_FILE = 512
MAPI_AB_NOMODIFY = 1024
SUCCESS_SUCCESS = 0
MAPI_USER_ABORT = 1
MAPI_E_USER_ABORT = 1
MAPI_E_FAILURE = 2
MAPI_E_LOGON_FAILURE = 3
MAPI_E_LOGIN_FAILURE = 3
MAPI_E_DISK_FULL = 4
MAPI_E_INSUFFICIENT_MEMORY = 5
MAPI_E_ACCESS_DENIED = 6
MAPI_E_TOO_MANY_SESSIONS = 8
MAPI_E_TOO_MANY_FILES = 9
MAPI_E_TOO_MANY_RECIPIENTS = 10
MAPI_E_ATTACHMENT_NOT_FOUND = 11
MAPI_E_ATTACHMENT_OPEN_FAILURE = 12
MAPI_E_ATTACHMENT_WRITE_FAILURE = 13
MAPI_E_UNKNOWN_RECIPIENT = 14
MAPI_E_BAD_RECIPTYPE = 15
MAPI_E_NO_MESSAGES = 16
MAPI_E_INVALID_MESSAGE = 17
MAPI_E_TEXT_TOO_LARGE = 18
MAPI_E_INVALID_SESSION = 19
MAPI_E_TYPE_NOT_SUPPORTED = 20
MAPI_E_AMBIGUOUS_RECIPIENT = 21
MAPI_E_AMBIG_RECIP = 21
MAPI_E_MESSAGE_IN_USE = 22
MAPI_E_NETWORK_FAILURE = 23
MAPI_E_INVALID_EDITFIELDS = 24
MAPI_E_INVALID_RECIPS = 25
MAPI_E_NOT_SUPPORTED = 26
MAPI_E_UNICODE_NOT_SUPPORTED = 27
MAPI_E_ATTACHMENT_TOO_LARGE = 28
def _define_MAPIFreeBuffer():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('MAPIFreeBuffer', windll['MAPI32.dll']), ((1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPMAPIADDRESS():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.System.Mapi.MapiRecipDesc_head),UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.Mapi.MapiRecipDesc_head)))
def _define_LPMAPIDELETEMAIL():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,win32more.Foundation.PSTR,UInt32,UInt32)
def _define_LPMAPIDETAILS():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,POINTER(win32more.System.Mapi.MapiRecipDesc_head),UInt32,UInt32)
def _define_LPMAPIFINDNEXT():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,win32more.Foundation.PSTR)
def _define_LPMAPIFREEBUFFER():
    return WINFUNCTYPE(UInt32,c_void_p)
def _define_LPMAPILOGOFF():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,UInt32,UInt32)
def _define_LPMAPILOGON():
    return WINFUNCTYPE(UInt32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(UIntPtr))
def _define_LPMAPIREADMAIL():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(POINTER(win32more.System.Mapi.MapiMessage_head)))
def _define_LPMAPIRESOLVENAME():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(POINTER(win32more.System.Mapi.MapiRecipDesc_head)))
def _define_LPMAPISAVEMAIL():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,POINTER(win32more.System.Mapi.MapiMessage_head),UInt32,UInt32,win32more.Foundation.PSTR)
def _define_LPMAPISENDDOCUMENTS():
    return WINFUNCTYPE(UInt32,UIntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)
def _define_LPMAPISENDMAIL():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,POINTER(win32more.System.Mapi.MapiMessage_head),UInt32,UInt32)
def _define_LPMAPISENDMAILW():
    return WINFUNCTYPE(UInt32,UIntPtr,UIntPtr,POINTER(win32more.System.Mapi.MapiMessageW_head),UInt32,UInt32)
def _define_MapiFileDesc_head():
    class MapiFileDesc(Structure):
        pass
    return MapiFileDesc
def _define_MapiFileDesc():
    MapiFileDesc = win32more.System.Mapi.MapiFileDesc_head
    MapiFileDesc._fields_ = [
        ('ulReserved', UInt32),
        ('flFlags', UInt32),
        ('nPosition', UInt32),
        ('lpszPathName', win32more.Foundation.PSTR),
        ('lpszFileName', win32more.Foundation.PSTR),
        ('lpFileType', c_void_p),
    ]
    return MapiFileDesc
def _define_MapiFileDescW_head():
    class MapiFileDescW(Structure):
        pass
    return MapiFileDescW
def _define_MapiFileDescW():
    MapiFileDescW = win32more.System.Mapi.MapiFileDescW_head
    MapiFileDescW._fields_ = [
        ('ulReserved', UInt32),
        ('flFlags', UInt32),
        ('nPosition', UInt32),
        ('lpszPathName', win32more.Foundation.PWSTR),
        ('lpszFileName', win32more.Foundation.PWSTR),
        ('lpFileType', c_void_p),
    ]
    return MapiFileDescW
def _define_MapiFileTagExt_head():
    class MapiFileTagExt(Structure):
        pass
    return MapiFileTagExt
def _define_MapiFileTagExt():
    MapiFileTagExt = win32more.System.Mapi.MapiFileTagExt_head
    MapiFileTagExt._fields_ = [
        ('ulReserved', UInt32),
        ('cbTag', UInt32),
        ('lpTag', c_char_p_no),
        ('cbEncoding', UInt32),
        ('lpEncoding', c_char_p_no),
    ]
    return MapiFileTagExt
def _define_MapiMessage_head():
    class MapiMessage(Structure):
        pass
    return MapiMessage
def _define_MapiMessage():
    MapiMessage = win32more.System.Mapi.MapiMessage_head
    MapiMessage._fields_ = [
        ('ulReserved', UInt32),
        ('lpszSubject', win32more.Foundation.PSTR),
        ('lpszNoteText', win32more.Foundation.PSTR),
        ('lpszMessageType', win32more.Foundation.PSTR),
        ('lpszDateReceived', win32more.Foundation.PSTR),
        ('lpszConversationID', win32more.Foundation.PSTR),
        ('flFlags', UInt32),
        ('lpOriginator', POINTER(win32more.System.Mapi.MapiRecipDesc_head)),
        ('nRecipCount', UInt32),
        ('lpRecips', POINTER(win32more.System.Mapi.MapiRecipDesc_head)),
        ('nFileCount', UInt32),
        ('lpFiles', POINTER(win32more.System.Mapi.MapiFileDesc_head)),
    ]
    return MapiMessage
def _define_MapiMessageW_head():
    class MapiMessageW(Structure):
        pass
    return MapiMessageW
def _define_MapiMessageW():
    MapiMessageW = win32more.System.Mapi.MapiMessageW_head
    MapiMessageW._fields_ = [
        ('ulReserved', UInt32),
        ('lpszSubject', win32more.Foundation.PWSTR),
        ('lpszNoteText', win32more.Foundation.PWSTR),
        ('lpszMessageType', win32more.Foundation.PWSTR),
        ('lpszDateReceived', win32more.Foundation.PWSTR),
        ('lpszConversationID', win32more.Foundation.PWSTR),
        ('flFlags', UInt32),
        ('lpOriginator', POINTER(win32more.System.Mapi.MapiRecipDescW_head)),
        ('nRecipCount', UInt32),
        ('lpRecips', POINTER(win32more.System.Mapi.MapiRecipDescW_head)),
        ('nFileCount', UInt32),
        ('lpFiles', POINTER(win32more.System.Mapi.MapiFileDescW_head)),
    ]
    return MapiMessageW
def _define_MapiRecipDesc_head():
    class MapiRecipDesc(Structure):
        pass
    return MapiRecipDesc
def _define_MapiRecipDesc():
    MapiRecipDesc = win32more.System.Mapi.MapiRecipDesc_head
    MapiRecipDesc._fields_ = [
        ('ulReserved', UInt32),
        ('ulRecipClass', UInt32),
        ('lpszName', win32more.Foundation.PSTR),
        ('lpszAddress', win32more.Foundation.PSTR),
        ('ulEIDSize', UInt32),
        ('lpEntryID', c_void_p),
    ]
    return MapiRecipDesc
def _define_MapiRecipDescW_head():
    class MapiRecipDescW(Structure):
        pass
    return MapiRecipDescW
def _define_MapiRecipDescW():
    MapiRecipDescW = win32more.System.Mapi.MapiRecipDescW_head
    MapiRecipDescW._fields_ = [
        ('ulReserved', UInt32),
        ('ulRecipClass', UInt32),
        ('lpszName', win32more.Foundation.PWSTR),
        ('lpszAddress', win32more.Foundation.PWSTR),
        ('ulEIDSize', UInt32),
        ('lpEntryID', c_void_p),
    ]
    return MapiRecipDescW
__all__ = [
    "LPMAPIADDRESS",
    "LPMAPIDELETEMAIL",
    "LPMAPIDETAILS",
    "LPMAPIFINDNEXT",
    "LPMAPIFREEBUFFER",
    "LPMAPILOGOFF",
    "LPMAPILOGON",
    "LPMAPIREADMAIL",
    "LPMAPIRESOLVENAME",
    "LPMAPISAVEMAIL",
    "LPMAPISENDDOCUMENTS",
    "LPMAPISENDMAIL",
    "LPMAPISENDMAILW",
    "MAPIFreeBuffer",
    "MAPI_AB_NOMODIFY",
    "MAPI_BCC",
    "MAPI_BODY_AS_FILE",
    "MAPI_CC",
    "MAPI_DIALOG",
    "MAPI_ENVELOPE_ONLY",
    "MAPI_EXTENDED",
    "MAPI_E_ACCESS_DENIED",
    "MAPI_E_AMBIGUOUS_RECIPIENT",
    "MAPI_E_AMBIG_RECIP",
    "MAPI_E_ATTACHMENT_NOT_FOUND",
    "MAPI_E_ATTACHMENT_OPEN_FAILURE",
    "MAPI_E_ATTACHMENT_TOO_LARGE",
    "MAPI_E_ATTACHMENT_WRITE_FAILURE",
    "MAPI_E_BAD_RECIPTYPE",
    "MAPI_E_DISK_FULL",
    "MAPI_E_FAILURE",
    "MAPI_E_INSUFFICIENT_MEMORY",
    "MAPI_E_INVALID_EDITFIELDS",
    "MAPI_E_INVALID_MESSAGE",
    "MAPI_E_INVALID_RECIPS",
    "MAPI_E_INVALID_SESSION",
    "MAPI_E_LOGIN_FAILURE",
    "MAPI_E_LOGON_FAILURE",
    "MAPI_E_MESSAGE_IN_USE",
    "MAPI_E_NETWORK_FAILURE",
    "MAPI_E_NOT_SUPPORTED",
    "MAPI_E_NO_MESSAGES",
    "MAPI_E_TEXT_TOO_LARGE",
    "MAPI_E_TOO_MANY_FILES",
    "MAPI_E_TOO_MANY_RECIPIENTS",
    "MAPI_E_TOO_MANY_SESSIONS",
    "MAPI_E_TYPE_NOT_SUPPORTED",
    "MAPI_E_UNICODE_NOT_SUPPORTED",
    "MAPI_E_UNKNOWN_RECIPIENT",
    "MAPI_E_USER_ABORT",
    "MAPI_FORCE_DOWNLOAD",
    "MAPI_FORCE_UNICODE",
    "MAPI_GUARANTEE_FIFO",
    "MAPI_LOGON_UI",
    "MAPI_LONG_MSGID",
    "MAPI_NEW_SESSION",
    "MAPI_OLE",
    "MAPI_OLE_STATIC",
    "MAPI_ORIG",
    "MAPI_PASSWORD_UI",
    "MAPI_PEEK",
    "MAPI_RECEIPT_REQUESTED",
    "MAPI_SENT",
    "MAPI_SUPPRESS_ATTACH",
    "MAPI_TO",
    "MAPI_UNREAD",
    "MAPI_UNREAD_ONLY",
    "MAPI_USER_ABORT",
    "MapiFileDesc",
    "MapiFileDescW",
    "MapiFileTagExt",
    "MapiMessage",
    "MapiMessageW",
    "MapiRecipDesc",
    "MapiRecipDescW",
    "SUCCESS_SUCCESS",
]
