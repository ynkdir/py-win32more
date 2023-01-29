from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Mapi
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
MAPI_OLE: UInt32 = 1
MAPI_OLE_STATIC: UInt32 = 2
MAPI_ORIG: UInt32 = 0
MAPI_TO: UInt32 = 1
MAPI_CC: UInt32 = 2
MAPI_BCC: UInt32 = 3
MAPI_UNREAD: UInt32 = 1
MAPI_RECEIPT_REQUESTED: UInt32 = 2
MAPI_SENT: UInt32 = 4
MAPI_LOGON_UI: UInt32 = 1
MAPI_PASSWORD_UI: UInt32 = 131072
MAPI_NEW_SESSION: UInt32 = 2
MAPI_FORCE_DOWNLOAD: UInt32 = 4096
MAPI_EXTENDED: UInt32 = 32
MAPI_DIALOG: UInt32 = 8
MAPI_FORCE_UNICODE: UInt32 = 262144
MAPI_UNREAD_ONLY: UInt32 = 32
MAPI_GUARANTEE_FIFO: UInt32 = 256
MAPI_LONG_MSGID: UInt32 = 16384
MAPI_PEEK: UInt32 = 128
MAPI_SUPPRESS_ATTACH: UInt32 = 2048
MAPI_ENVELOPE_ONLY: UInt32 = 64
MAPI_BODY_AS_FILE: UInt32 = 512
MAPI_AB_NOMODIFY: UInt32 = 1024
SUCCESS_SUCCESS: UInt32 = 0
MAPI_USER_ABORT: UInt32 = 1
MAPI_E_USER_ABORT: UInt32 = 1
MAPI_E_FAILURE: UInt32 = 2
MAPI_E_LOGON_FAILURE: UInt32 = 3
MAPI_E_LOGIN_FAILURE: UInt32 = 3
MAPI_E_DISK_FULL: UInt32 = 4
MAPI_E_INSUFFICIENT_MEMORY: UInt32 = 5
MAPI_E_ACCESS_DENIED: UInt32 = 6
MAPI_E_TOO_MANY_SESSIONS: UInt32 = 8
MAPI_E_TOO_MANY_FILES: UInt32 = 9
MAPI_E_TOO_MANY_RECIPIENTS: UInt32 = 10
MAPI_E_ATTACHMENT_NOT_FOUND: UInt32 = 11
MAPI_E_ATTACHMENT_OPEN_FAILURE: UInt32 = 12
MAPI_E_ATTACHMENT_WRITE_FAILURE: UInt32 = 13
MAPI_E_UNKNOWN_RECIPIENT: UInt32 = 14
MAPI_E_BAD_RECIPTYPE: UInt32 = 15
MAPI_E_NO_MESSAGES: UInt32 = 16
MAPI_E_INVALID_MESSAGE: UInt32 = 17
MAPI_E_TEXT_TOO_LARGE: UInt32 = 18
MAPI_E_INVALID_SESSION: UInt32 = 19
MAPI_E_TYPE_NOT_SUPPORTED: UInt32 = 20
MAPI_E_AMBIGUOUS_RECIPIENT: UInt32 = 21
MAPI_E_AMBIG_RECIP: UInt32 = 21
MAPI_E_MESSAGE_IN_USE: UInt32 = 22
MAPI_E_NETWORK_FAILURE: UInt32 = 23
MAPI_E_INVALID_EDITFIELDS: UInt32 = 24
MAPI_E_INVALID_RECIPS: UInt32 = 25
MAPI_E_NOT_SUPPORTED: UInt32 = 26
MAPI_E_UNICODE_NOT_SUPPORTED: UInt32 = 27
MAPI_E_ATTACHMENT_TOO_LARGE: UInt32 = 28
@winfunctype('MAPI32.dll')
def MAPIFreeBuffer(pv: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPMAPIADDRESS(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszCaption: win32more.Foundation.PSTR, nEditFields: UInt32, lpszLabels: win32more.Foundation.PSTR, nRecips: UInt32, lpRecips: POINTER(win32more.System.Mapi.MapiRecipDesc_head), flFlags: UInt32, ulReserved: UInt32, lpnNewRecips: POINTER(UInt32), lppNewRecips: POINTER(POINTER(win32more.System.Mapi.MapiRecipDesc_head))) -> UInt32: ...
@winfunctype_pointer
def LPMAPIDELETEMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageID: win32more.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPIDETAILS(lhSession: UIntPtr, ulUIParam: UIntPtr, lpRecip: POINTER(win32more.System.Mapi.MapiRecipDesc_head), flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPIFINDNEXT(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageType: win32more.Foundation.PSTR, lpszSeedMessageID: win32more.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lpszMessageID: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype_pointer
def LPMAPIFREEBUFFER(pv: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPMAPILOGOFF(lhSession: UIntPtr, ulUIParam: UIntPtr, flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPILOGON(ulUIParam: UIntPtr, lpszProfileName: win32more.Foundation.PSTR, lpszPassword: win32more.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lplhSession: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype_pointer
def LPMAPIREADMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageID: win32more.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lppMessage: POINTER(POINTER(win32more.System.Mapi.MapiMessage_head))) -> UInt32: ...
@winfunctype_pointer
def LPMAPIRESOLVENAME(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszName: win32more.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lppRecip: POINTER(POINTER(win32more.System.Mapi.MapiRecipDesc_head))) -> UInt32: ...
@winfunctype_pointer
def LPMAPISAVEMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpMessage: POINTER(win32more.System.Mapi.MapiMessage_head), flFlags: UInt32, ulReserved: UInt32, lpszMessageID: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype_pointer
def LPMAPISENDDOCUMENTS(ulUIParam: UIntPtr, lpszDelimChar: win32more.Foundation.PSTR, lpszFilePaths: win32more.Foundation.PSTR, lpszFileNames: win32more.Foundation.PSTR, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPISENDMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpMessage: POINTER(win32more.System.Mapi.MapiMessage_head), flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPISENDMAILW(lhSession: UIntPtr, ulUIParam: UIntPtr, lpMessage: POINTER(win32more.System.Mapi.MapiMessageW_head), flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
class MapiFileDesc(Structure):
    ulReserved: UInt32
    flFlags: UInt32
    nPosition: UInt32
    lpszPathName: win32more.Foundation.PSTR
    lpszFileName: win32more.Foundation.PSTR
    lpFileType: c_void_p
class MapiFileDescW(Structure):
    ulReserved: UInt32
    flFlags: UInt32
    nPosition: UInt32
    lpszPathName: win32more.Foundation.PWSTR
    lpszFileName: win32more.Foundation.PWSTR
    lpFileType: c_void_p
class MapiFileTagExt(Structure):
    ulReserved: UInt32
    cbTag: UInt32
    lpTag: c_char_p_no
    cbEncoding: UInt32
    lpEncoding: c_char_p_no
class MapiMessage(Structure):
    ulReserved: UInt32
    lpszSubject: win32more.Foundation.PSTR
    lpszNoteText: win32more.Foundation.PSTR
    lpszMessageType: win32more.Foundation.PSTR
    lpszDateReceived: win32more.Foundation.PSTR
    lpszConversationID: win32more.Foundation.PSTR
    flFlags: UInt32
    lpOriginator: POINTER(win32more.System.Mapi.MapiRecipDesc_head)
    nRecipCount: UInt32
    lpRecips: POINTER(win32more.System.Mapi.MapiRecipDesc_head)
    nFileCount: UInt32
    lpFiles: POINTER(win32more.System.Mapi.MapiFileDesc_head)
class MapiMessageW(Structure):
    ulReserved: UInt32
    lpszSubject: win32more.Foundation.PWSTR
    lpszNoteText: win32more.Foundation.PWSTR
    lpszMessageType: win32more.Foundation.PWSTR
    lpszDateReceived: win32more.Foundation.PWSTR
    lpszConversationID: win32more.Foundation.PWSTR
    flFlags: UInt32
    lpOriginator: POINTER(win32more.System.Mapi.MapiRecipDescW_head)
    nRecipCount: UInt32
    lpRecips: POINTER(win32more.System.Mapi.MapiRecipDescW_head)
    nFileCount: UInt32
    lpFiles: POINTER(win32more.System.Mapi.MapiFileDescW_head)
class MapiRecipDesc(Structure):
    ulReserved: UInt32
    ulRecipClass: UInt32
    lpszName: win32more.Foundation.PSTR
    lpszAddress: win32more.Foundation.PSTR
    ulEIDSize: UInt32
    lpEntryID: c_void_p
class MapiRecipDescW(Structure):
    ulReserved: UInt32
    ulRecipClass: UInt32
    lpszName: win32more.Foundation.PWSTR
    lpszAddress: win32more.Foundation.PWSTR
    ulEIDSize: UInt32
    lpEntryID: c_void_p
make_head(_module, 'LPMAPIADDRESS')
make_head(_module, 'LPMAPIDELETEMAIL')
make_head(_module, 'LPMAPIDETAILS')
make_head(_module, 'LPMAPIFINDNEXT')
make_head(_module, 'LPMAPIFREEBUFFER')
make_head(_module, 'LPMAPILOGOFF')
make_head(_module, 'LPMAPILOGON')
make_head(_module, 'LPMAPIREADMAIL')
make_head(_module, 'LPMAPIRESOLVENAME')
make_head(_module, 'LPMAPISAVEMAIL')
make_head(_module, 'LPMAPISENDDOCUMENTS')
make_head(_module, 'LPMAPISENDMAIL')
make_head(_module, 'LPMAPISENDMAILW')
make_head(_module, 'MapiFileDesc')
make_head(_module, 'MapiFileDescW')
make_head(_module, 'MapiFileTagExt')
make_head(_module, 'MapiMessage')
make_head(_module, 'MapiMessageW')
make_head(_module, 'MapiRecipDesc')
make_head(_module, 'MapiRecipDescW')
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
_arch_optional = [
]
