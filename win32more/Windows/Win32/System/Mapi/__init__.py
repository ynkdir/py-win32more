from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Mapi
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
def MAPIFreeBuffer(pv: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPMAPIADDRESS(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszCaption: win32more.Windows.Win32.Foundation.PSTR, nEditFields: UInt32, lpszLabels: win32more.Windows.Win32.Foundation.PSTR, nRecips: UInt32, lpRecips: POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDesc), flFlags: UInt32, ulReserved: UInt32, lpnNewRecips: POINTER(UInt32), lppNewRecips: POINTER(POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDesc))) -> UInt32: ...
@winfunctype_pointer
def LPMAPIDELETEMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageID: win32more.Windows.Win32.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPIDETAILS(lhSession: UIntPtr, ulUIParam: UIntPtr, lpRecip: POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDesc), flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPIFINDNEXT(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageType: win32more.Windows.Win32.Foundation.PSTR, lpszSeedMessageID: win32more.Windows.Win32.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lpszMessageID: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype_pointer
def LPMAPIFREEBUFFER(pv: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPMAPILOGOFF(lhSession: UIntPtr, ulUIParam: UIntPtr, flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPILOGON(ulUIParam: UIntPtr, lpszProfileName: win32more.Windows.Win32.Foundation.PSTR, lpszPassword: win32more.Windows.Win32.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lplhSession: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype_pointer
def LPMAPIREADMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszMessageID: win32more.Windows.Win32.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lppMessage: POINTER(POINTER(win32more.Windows.Win32.System.Mapi.MapiMessage))) -> UInt32: ...
@winfunctype_pointer
def LPMAPIRESOLVENAME(lhSession: UIntPtr, ulUIParam: UIntPtr, lpszName: win32more.Windows.Win32.Foundation.PSTR, flFlags: UInt32, ulReserved: UInt32, lppRecip: POINTER(POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDesc))) -> UInt32: ...
@winfunctype_pointer
def LPMAPISAVEMAIL(lhSession: UIntPtr, ulUIParam: UIntPtr, lpMessage: POINTER(win32more.Windows.Win32.System.Mapi.MapiMessage), flFlags: UInt32, ulReserved: UInt32, lpszMessageID: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype_pointer
def LPMAPISENDDOCUMENTS(ulUIParam: UIntPtr, lpszDelimChar: win32more.Windows.Win32.Foundation.PSTR, lpszFilePaths: win32more.Windows.Win32.Foundation.PSTR, lpszFileNames: win32more.Windows.Win32.Foundation.PSTR, ulReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def LPMAPISENDMAILW(lhSession: UIntPtr, ulUIParam: UIntPtr, lpMessage: POINTER(win32more.Windows.Win32.System.Mapi.MapiMessageW), flFlags: UInt32, ulReserved: UInt32) -> UInt32: ...
LPMAPISENDMAIL = UnicodeAlias('LPMAPISENDMAILW')
class MapiFileDescW(Structure):
    ulReserved: UInt32
    flFlags: UInt32
    nPosition: UInt32
    lpszPathName: win32more.Windows.Win32.Foundation.PWSTR
    lpszFileName: win32more.Windows.Win32.Foundation.PWSTR
    lpFileType: VoidPtr
MapiFileDesc = UnicodeAlias('MapiFileDescW')
class MapiFileTagExt(Structure):
    ulReserved: UInt32
    cbTag: UInt32
    lpTag: POINTER(Byte)
    cbEncoding: UInt32
    lpEncoding: POINTER(Byte)
class MapiMessageW(Structure):
    ulReserved: UInt32
    lpszSubject: win32more.Windows.Win32.Foundation.PWSTR
    lpszNoteText: win32more.Windows.Win32.Foundation.PWSTR
    lpszMessageType: win32more.Windows.Win32.Foundation.PWSTR
    lpszDateReceived: win32more.Windows.Win32.Foundation.PWSTR
    lpszConversationID: win32more.Windows.Win32.Foundation.PWSTR
    flFlags: UInt32
    lpOriginator: POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDescW)
    nRecipCount: UInt32
    lpRecips: POINTER(win32more.Windows.Win32.System.Mapi.MapiRecipDescW)
    nFileCount: UInt32
    lpFiles: POINTER(win32more.Windows.Win32.System.Mapi.MapiFileDescW)
MapiMessage = UnicodeAlias('MapiMessageW')
class MapiRecipDescW(Structure):
    ulReserved: UInt32
    ulRecipClass: UInt32
    lpszName: win32more.Windows.Win32.Foundation.PWSTR
    lpszAddress: win32more.Windows.Win32.Foundation.PWSTR
    ulEIDSize: UInt32
    lpEntryID: VoidPtr
MapiRecipDesc = UnicodeAlias('MapiRecipDescW')


make_ready(__name__)
