from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security
import Windows.Win32.System.DataExchange
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
WM_DDE_FIRST: UInt32 = 992
WM_DDE_INITIATE: UInt32 = 992
WM_DDE_TERMINATE: UInt32 = 993
WM_DDE_ADVISE: UInt32 = 994
WM_DDE_UNADVISE: UInt32 = 995
WM_DDE_ACK: UInt32 = 996
WM_DDE_DATA: UInt32 = 997
WM_DDE_REQUEST: UInt32 = 998
WM_DDE_POKE: UInt32 = 999
WM_DDE_EXECUTE: UInt32 = 1000
WM_DDE_LAST: UInt32 = 1000
CADV_LATEACK: UInt32 = 65535
DDE_FACK: UInt32 = 32768
DDE_FBUSY: UInt32 = 16384
DDE_FDEFERUPD: UInt32 = 16384
DDE_FACKREQ: UInt32 = 32768
DDE_FRELEASE: UInt32 = 8192
DDE_FREQUESTED: UInt32 = 4096
DDE_FAPPSTATUS: UInt32 = 255
DDE_FNOTPROCESSED: UInt32 = 0
MSGF_DDEMGR: UInt32 = 32769
CP_WINANSI: Int32 = 1004
CP_WINUNICODE: Int32 = 1200
CP_WINNEUTRAL: Int32 = 1200
XTYPF_NOBLOCK: UInt32 = 2
XTYPF_NODATA: UInt32 = 4
XTYPF_ACKREQ: UInt32 = 8
XCLASS_MASK: UInt32 = 64512
XCLASS_BOOL: UInt32 = 4096
XCLASS_DATA: UInt32 = 8192
XCLASS_FLAGS: UInt32 = 16384
XCLASS_NOTIFICATION: UInt32 = 32768
XTYP_MASK: UInt32 = 240
XTYP_SHIFT: UInt32 = 4
TIMEOUT_ASYNC: UInt32 = 4294967295
QID_SYNC: UInt32 = 4294967295
SZDDESYS_TOPIC: String = 'System'
SZDDESYS_ITEM_TOPICS: String = 'Topics'
SZDDESYS_ITEM_SYSITEMS: String = 'SysItems'
SZDDESYS_ITEM_RTNMSG: String = 'ReturnMessage'
SZDDESYS_ITEM_STATUS: String = 'Status'
SZDDESYS_ITEM_FORMATS: String = 'Formats'
SZDDESYS_ITEM_HELP: String = 'Help'
SZDDE_ITEM_ITEMLIST: String = 'TopicItemList'
APPCMD_MASK: Int32 = 4080
APPCLASS_MASK: Int32 = 15
HDATA_APPOWNED: UInt32 = 1
DMLERR_NO_ERROR: UInt32 = 0
DMLERR_FIRST: UInt32 = 16384
DMLERR_ADVACKTIMEOUT: UInt32 = 16384
DMLERR_BUSY: UInt32 = 16385
DMLERR_DATAACKTIMEOUT: UInt32 = 16386
DMLERR_DLL_NOT_INITIALIZED: UInt32 = 16387
DMLERR_DLL_USAGE: UInt32 = 16388
DMLERR_EXECACKTIMEOUT: UInt32 = 16389
DMLERR_INVALIDPARAMETER: UInt32 = 16390
DMLERR_LOW_MEMORY: UInt32 = 16391
DMLERR_MEMORY_ERROR: UInt32 = 16392
DMLERR_NOTPROCESSED: UInt32 = 16393
DMLERR_NO_CONV_ESTABLISHED: UInt32 = 16394
DMLERR_POKEACKTIMEOUT: UInt32 = 16395
DMLERR_POSTMSG_FAILED: UInt32 = 16396
DMLERR_REENTRANCY: UInt32 = 16397
DMLERR_SERVER_DIED: UInt32 = 16398
DMLERR_SYS_ERROR: UInt32 = 16399
DMLERR_UNADVACKTIMEOUT: UInt32 = 16400
DMLERR_UNFOUND_QUEUE_ID: UInt32 = 16401
DMLERR_LAST: UInt32 = 16401
MH_CREATE: UInt32 = 1
MH_KEEP: UInt32 = 2
MH_DELETE: UInt32 = 3
MH_CLEANUP: UInt32 = 4
MAX_MONITORS: UInt32 = 4
MF_MASK: UInt32 = 4278190080
@winfunctype('USER32.dll')
def DdeSetQualityOfService(hwndClient: Windows.Win32.Foundation.HWND, pqosNew: POINTER(Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE_head), pqosPrev: POINTER(Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ImpersonateDdeClientWindow(hWndClient: Windows.Win32.Foundation.HWND, hWndServer: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def PackDDElParam(msg: UInt32, uiLo: UIntPtr, uiHi: UIntPtr) -> Windows.Win32.Foundation.LPARAM: ...
@winfunctype('USER32.dll')
def UnpackDDElParam(msg: UInt32, lParam: Windows.Win32.Foundation.LPARAM, puiLo: POINTER(UIntPtr), puiHi: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def FreeDDElParam(msg: UInt32, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ReuseDDElParam(lParam: Windows.Win32.Foundation.LPARAM, msgIn: UInt32, msgOut: UInt32, uiLo: UIntPtr, uiHi: UIntPtr) -> Windows.Win32.Foundation.LPARAM: ...
@winfunctype('USER32.dll')
def DdeInitializeA(pidInst: POINTER(UInt32), pfnCallback: Windows.Win32.System.DataExchange.PFNCALLBACK, afCmd: Windows.Win32.System.DataExchange.DDE_INITIALIZE_COMMAND, ulRes: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeInitializeW(pidInst: POINTER(UInt32), pfnCallback: Windows.Win32.System.DataExchange.PFNCALLBACK, afCmd: Windows.Win32.System.DataExchange.DDE_INITIALIZE_COMMAND, ulRes: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeUninitialize(idInst: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeConnectList(idInst: UInt32, hszService: Windows.Win32.System.DataExchange.HSZ, hszTopic: Windows.Win32.System.DataExchange.HSZ, hConvList: Windows.Win32.System.DataExchange.HCONVLIST, pCC: POINTER(Windows.Win32.System.DataExchange.CONVCONTEXT_head)) -> Windows.Win32.System.DataExchange.HCONVLIST: ...
@winfunctype('USER32.dll')
def DdeQueryNextServer(hConvList: Windows.Win32.System.DataExchange.HCONVLIST, hConvPrev: Windows.Win32.System.DataExchange.HCONV) -> Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeDisconnectList(hConvList: Windows.Win32.System.DataExchange.HCONVLIST) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeConnect(idInst: UInt32, hszService: Windows.Win32.System.DataExchange.HSZ, hszTopic: Windows.Win32.System.DataExchange.HSZ, pCC: POINTER(Windows.Win32.System.DataExchange.CONVCONTEXT_head)) -> Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeDisconnect(hConv: Windows.Win32.System.DataExchange.HCONV) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeReconnect(hConv: Windows.Win32.System.DataExchange.HCONV) -> Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeQueryConvInfo(hConv: Windows.Win32.System.DataExchange.HCONV, idTransaction: UInt32, pConvInfo: POINTER(Windows.Win32.System.DataExchange.CONVINFO_head)) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeSetUserHandle(hConv: Windows.Win32.System.DataExchange.HCONV, id: UInt32, hUser: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeAbandonTransaction(idInst: UInt32, hConv: Windows.Win32.System.DataExchange.HCONV, idTransaction: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdePostAdvise(idInst: UInt32, hszTopic: Windows.Win32.System.DataExchange.HSZ, hszItem: Windows.Win32.System.DataExchange.HSZ) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeEnableCallback(idInst: UInt32, hConv: Windows.Win32.System.DataExchange.HCONV, wCmd: Windows.Win32.System.DataExchange.DDE_ENABLE_CALLBACK_CMD) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeImpersonateClient(hConv: Windows.Win32.System.DataExchange.HCONV) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeNameService(idInst: UInt32, hsz1: Windows.Win32.System.DataExchange.HSZ, hsz2: Windows.Win32.System.DataExchange.HSZ, afCmd: Windows.Win32.System.DataExchange.DDE_NAME_SERVICE_CMD) -> Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeClientTransaction(pData: c_char_p_no, cbData: UInt32, hConv: Windows.Win32.System.DataExchange.HCONV, hszItem: Windows.Win32.System.DataExchange.HSZ, wFmt: UInt32, wType: Windows.Win32.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE, dwTimeout: UInt32, pdwResult: POINTER(UInt32)) -> Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeCreateDataHandle(idInst: UInt32, pSrc: c_char_p_no, cb: UInt32, cbOff: UInt32, hszItem: Windows.Win32.System.DataExchange.HSZ, wFmt: UInt32, afCmd: UInt32) -> Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeAddData(hData: Windows.Win32.System.DataExchange.HDDEDATA, pSrc: c_char_p_no, cb: UInt32, cbOff: UInt32) -> Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeGetData(hData: Windows.Win32.System.DataExchange.HDDEDATA, pDst: c_char_p_no, cbMax: UInt32, cbOff: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeAccessData(hData: Windows.Win32.System.DataExchange.HDDEDATA, pcbDataSize: POINTER(UInt32)) -> c_char_p_no: ...
@winfunctype('USER32.dll')
def DdeUnaccessData(hData: Windows.Win32.System.DataExchange.HDDEDATA) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeFreeDataHandle(hData: Windows.Win32.System.DataExchange.HDDEDATA) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeGetLastError(idInst: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeCreateStringHandleA(idInst: UInt32, psz: Windows.Win32.Foundation.PSTR, iCodePage: Int32) -> Windows.Win32.System.DataExchange.HSZ: ...
@winfunctype('USER32.dll')
def DdeCreateStringHandleW(idInst: UInt32, psz: Windows.Win32.Foundation.PWSTR, iCodePage: Int32) -> Windows.Win32.System.DataExchange.HSZ: ...
@winfunctype('USER32.dll')
def DdeQueryStringA(idInst: UInt32, hsz: Windows.Win32.System.DataExchange.HSZ, psz: Windows.Win32.Foundation.PSTR, cchMax: UInt32, iCodePage: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeQueryStringW(idInst: UInt32, hsz: Windows.Win32.System.DataExchange.HSZ, psz: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, iCodePage: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeFreeStringHandle(idInst: UInt32, hsz: Windows.Win32.System.DataExchange.HSZ) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeKeepStringHandle(idInst: UInt32, hsz: Windows.Win32.System.DataExchange.HSZ) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeCmpStringHandles(hsz1: Windows.Win32.System.DataExchange.HSZ, hsz2: Windows.Win32.System.DataExchange.HSZ) -> Int32: ...
@winfunctype('GDI32.dll')
def SetWinMetaFileBits(nSize: UInt32, lpMeta16Data: c_char_p_no, hdcRef: Windows.Win32.Graphics.Gdi.HDC, lpMFP: POINTER(Windows.Win32.System.DataExchange.METAFILEPICT_head)) -> Windows.Win32.Graphics.Gdi.HENHMETAFILE: ...
@winfunctype('USER32.dll')
def OpenClipboard(hWndNewOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseClipboard() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetClipboardSequenceNumber() -> UInt32: ...
@winfunctype('USER32.dll')
def GetClipboardOwner() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def SetClipboardViewer(hWndNewViewer: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetClipboardViewer() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def ChangeClipboardChain(hWndRemove: Windows.Win32.Foundation.HWND, hWndNewNext: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetClipboardData(uFormat: UInt32, hMem: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USER32.dll')
def GetClipboardData(uFormat: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USER32.dll')
def RegisterClipboardFormatA(lpszFormat: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('USER32.dll')
def RegisterClipboardFormatW(lpszFormat: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('USER32.dll')
def CountClipboardFormats() -> Int32: ...
@winfunctype('USER32.dll')
def EnumClipboardFormats(format: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetClipboardFormatNameA(format: UInt32, lpszFormatName: Windows.Win32.Foundation.PSTR, cchMaxCount: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetClipboardFormatNameW(format: UInt32, lpszFormatName: Windows.Win32.Foundation.PWSTR, cchMaxCount: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def EmptyClipboard() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsClipboardFormatAvailable(format: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPriorityClipboardFormat(paFormatPriorityList: POINTER(UInt32), cFormats: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetOpenClipboardWindow() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def AddClipboardFormatListener(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RemoveClipboardFormatListener(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUpdatedClipboardFormats(lpuiFormats: POINTER(UInt32), cFormats: UInt32, pcFormatsOut: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GlobalDeleteAtom(nAtom: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def InitAtomTable(nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteAtom(nAtom: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomA(lpString: Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomW(lpString: Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomExA(lpString: Windows.Win32.Foundation.PSTR, Flags: UInt32) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomExW(lpString: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalFindAtomA(lpString: Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalFindAtomW(lpString: Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalGetAtomNameA(nAtom: UInt16, lpBuffer: Windows.Win32.Foundation.PSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalGetAtomNameW(nAtom: UInt16, lpBuffer: Windows.Win32.Foundation.PWSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddAtomA(lpString: Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def AddAtomW(lpString: Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def FindAtomA(lpString: Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def FindAtomW(lpString: Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetAtomNameA(nAtom: UInt16, lpBuffer: Windows.Win32.Foundation.PSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetAtomNameW(nAtom: UInt16, lpBuffer: Windows.Win32.Foundation.PWSTR, nSize: Int32) -> UInt32: ...
class CONVCONTEXT(Structure):
    cb: UInt32
    wFlags: UInt32
    wCountryID: UInt32
    iCodePage: Int32
    dwLangID: UInt32
    dwSecurity: UInt32
    qos: Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE
class CONVINFO(Structure):
    cb: UInt32
    hUser: UIntPtr
    hConvPartner: Windows.Win32.System.DataExchange.HCONV
    hszSvcPartner: Windows.Win32.System.DataExchange.HSZ
    hszServiceReq: Windows.Win32.System.DataExchange.HSZ
    hszTopic: Windows.Win32.System.DataExchange.HSZ
    hszItem: Windows.Win32.System.DataExchange.HSZ
    wFmt: UInt32
    wType: Windows.Win32.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE
    wStatus: Windows.Win32.System.DataExchange.CONVINFO_STATUS
    wConvst: Windows.Win32.System.DataExchange.CONVINFO_CONVERSATION_STATE
    wLastError: UInt32
    hConvList: Windows.Win32.System.DataExchange.HCONVLIST
    ConvCtxt: Windows.Win32.System.DataExchange.CONVCONTEXT
    hwnd: Windows.Win32.Foundation.HWND
    hwndPartner: Windows.Win32.Foundation.HWND
CONVINFO_CONVERSATION_STATE = UInt32
XST_ADVACKRCVD: CONVINFO_CONVERSATION_STATE = 13
XST_ADVDATAACKRCVD: CONVINFO_CONVERSATION_STATE = 16
XST_ADVDATASENT: CONVINFO_CONVERSATION_STATE = 15
XST_ADVSENT: CONVINFO_CONVERSATION_STATE = 11
XST_CONNECTED: CONVINFO_CONVERSATION_STATE = 2
XST_DATARCVD: CONVINFO_CONVERSATION_STATE = 6
XST_EXECACKRCVD: CONVINFO_CONVERSATION_STATE = 10
XST_EXECSENT: CONVINFO_CONVERSATION_STATE = 9
XST_INCOMPLETE: CONVINFO_CONVERSATION_STATE = 1
XST_INIT1: CONVINFO_CONVERSATION_STATE = 3
XST_INIT2: CONVINFO_CONVERSATION_STATE = 4
XST_NULL: CONVINFO_CONVERSATION_STATE = 0
XST_POKEACKRCVD: CONVINFO_CONVERSATION_STATE = 8
XST_POKESENT: CONVINFO_CONVERSATION_STATE = 7
XST_REQSENT: CONVINFO_CONVERSATION_STATE = 5
XST_UNADVACKRCVD: CONVINFO_CONVERSATION_STATE = 14
XST_UNADVSENT: CONVINFO_CONVERSATION_STATE = 12
CONVINFO_STATUS = UInt32
ST_ADVISE: CONVINFO_STATUS = 2
ST_BLOCKED: CONVINFO_STATUS = 8
ST_BLOCKNEXT: CONVINFO_STATUS = 128
ST_CLIENT: CONVINFO_STATUS = 16
ST_CONNECTED: CONVINFO_STATUS = 1
ST_INLIST: CONVINFO_STATUS = 64
ST_ISLOCAL: CONVINFO_STATUS = 4
ST_ISSELF: CONVINFO_STATUS = 256
ST_TERMINATED: CONVINFO_STATUS = 32
class COPYDATASTRUCT(Structure):
    dwData: UIntPtr
    cbData: UInt32
    lpData: c_void_p
class DDEACK(Structure):
    _bitfield: UInt16
class DDEADVISE(Structure):
    _bitfield: UInt16
    cfFormat: Int16
class DDEDATA(Structure):
    _bitfield: UInt16
    cfFormat: Int16
    Value: Byte * 1
class DDELN(Structure):
    _bitfield: UInt16
    cfFormat: Int16
class DDEML_MSG_HOOK_DATA(Structure):
    uiLo: UIntPtr
    uiHi: UIntPtr
    cbData: UInt32
    Data: UInt32 * 8
class DDEPOKE(Structure):
    _bitfield: UInt16
    cfFormat: Int16
    Value: Byte * 1
class DDEUP(Structure):
    _bitfield: UInt16
    cfFormat: Int16
    rgb: Byte * 1
DDE_CLIENT_TRANSACTION_TYPE = UInt32
XTYP_ADVSTART: DDE_CLIENT_TRANSACTION_TYPE = 4144
XTYP_ADVSTOP: DDE_CLIENT_TRANSACTION_TYPE = 32832
XTYP_EXECUTE: DDE_CLIENT_TRANSACTION_TYPE = 16464
XTYP_POKE: DDE_CLIENT_TRANSACTION_TYPE = 16528
XTYP_REQUEST: DDE_CLIENT_TRANSACTION_TYPE = 8368
XTYP_ADVDATA: DDE_CLIENT_TRANSACTION_TYPE = 16400
XTYP_ADVREQ: DDE_CLIENT_TRANSACTION_TYPE = 8226
XTYP_CONNECT: DDE_CLIENT_TRANSACTION_TYPE = 4194
XTYP_CONNECT_CONFIRM: DDE_CLIENT_TRANSACTION_TYPE = 32882
XTYP_DISCONNECT: DDE_CLIENT_TRANSACTION_TYPE = 32962
XTYP_MONITOR: DDE_CLIENT_TRANSACTION_TYPE = 33010
XTYP_REGISTER: DDE_CLIENT_TRANSACTION_TYPE = 32930
XTYP_UNREGISTER: DDE_CLIENT_TRANSACTION_TYPE = 32978
XTYP_WILDCONNECT: DDE_CLIENT_TRANSACTION_TYPE = 8418
XTYP_XACT_COMPLETE: DDE_CLIENT_TRANSACTION_TYPE = 32896
DDE_ENABLE_CALLBACK_CMD = UInt32
EC_ENABLEALL: DDE_ENABLE_CALLBACK_CMD = 0
EC_ENABLEONE: DDE_ENABLE_CALLBACK_CMD = 128
EC_DISABLE: DDE_ENABLE_CALLBACK_CMD = 8
EC_QUERYWAITING: DDE_ENABLE_CALLBACK_CMD = 2
DDE_INITIALIZE_COMMAND = UInt32
APPCLASS_MONITOR: DDE_INITIALIZE_COMMAND = 1
APPCLASS_STANDARD: DDE_INITIALIZE_COMMAND = 0
APPCMD_CLIENTONLY: DDE_INITIALIZE_COMMAND = 16
APPCMD_FILTERINITS: DDE_INITIALIZE_COMMAND = 32
CBF_FAIL_ALLSVRXACTIONS: DDE_INITIALIZE_COMMAND = 258048
CBF_FAIL_ADVISES: DDE_INITIALIZE_COMMAND = 16384
CBF_FAIL_CONNECTIONS: DDE_INITIALIZE_COMMAND = 8192
CBF_FAIL_EXECUTES: DDE_INITIALIZE_COMMAND = 32768
CBF_FAIL_POKES: DDE_INITIALIZE_COMMAND = 65536
CBF_FAIL_REQUESTS: DDE_INITIALIZE_COMMAND = 131072
CBF_FAIL_SELFCONNECTIONS: DDE_INITIALIZE_COMMAND = 4096
CBF_SKIP_ALLNOTIFICATIONS: DDE_INITIALIZE_COMMAND = 3932160
CBF_SKIP_CONNECT_CONFIRMS: DDE_INITIALIZE_COMMAND = 262144
CBF_SKIP_DISCONNECTS: DDE_INITIALIZE_COMMAND = 2097152
CBF_SKIP_REGISTRATIONS: DDE_INITIALIZE_COMMAND = 524288
CBF_SKIP_UNREGISTRATIONS: DDE_INITIALIZE_COMMAND = 1048576
MF_CALLBACKS: DDE_INITIALIZE_COMMAND = 134217728
MF_CONV: DDE_INITIALIZE_COMMAND = 1073741824
MF_ERRORS: DDE_INITIALIZE_COMMAND = 268435456
MF_HSZ_INFO: DDE_INITIALIZE_COMMAND = 16777216
MF_LINKS: DDE_INITIALIZE_COMMAND = 536870912
MF_POSTMSGS: DDE_INITIALIZE_COMMAND = 67108864
MF_SENDMSGS: DDE_INITIALIZE_COMMAND = 33554432
DDE_NAME_SERVICE_CMD = UInt32
DNS_REGISTER: DDE_NAME_SERVICE_CMD = 1
DNS_UNREGISTER: DDE_NAME_SERVICE_CMD = 2
DNS_FILTERON: DDE_NAME_SERVICE_CMD = 4
DNS_FILTEROFF: DDE_NAME_SERVICE_CMD = 8
HCONV = IntPtr
HCONVLIST = IntPtr
HDDEDATA = IntPtr
HSZ = IntPtr
class HSZPAIR(Structure):
    hszSvc: Windows.Win32.System.DataExchange.HSZ
    hszTopic: Windows.Win32.System.DataExchange.HSZ
class METAFILEPICT(Structure):
    mm: Int32
    xExt: Int32
    yExt: Int32
    hMF: Windows.Win32.Graphics.Gdi.HMETAFILE
class MONCBSTRUCT(Structure):
    cb: UInt32
    dwTime: UInt32
    hTask: Windows.Win32.Foundation.HANDLE
    dwRet: UInt32
    wType: UInt32
    wFmt: UInt32
    hConv: Windows.Win32.System.DataExchange.HCONV
    hsz1: Windows.Win32.System.DataExchange.HSZ
    hsz2: Windows.Win32.System.DataExchange.HSZ
    hData: Windows.Win32.System.DataExchange.HDDEDATA
    dwData1: UIntPtr
    dwData2: UIntPtr
    cc: Windows.Win32.System.DataExchange.CONVCONTEXT
    cbData: UInt32
    Data: UInt32 * 8
class MONCONVSTRUCT(Structure):
    cb: UInt32
    fConnect: Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hTask: Windows.Win32.Foundation.HANDLE
    hszSvc: Windows.Win32.System.DataExchange.HSZ
    hszTopic: Windows.Win32.System.DataExchange.HSZ
    hConvClient: Windows.Win32.System.DataExchange.HCONV
    hConvServer: Windows.Win32.System.DataExchange.HCONV
class MONERRSTRUCT(Structure):
    cb: UInt32
    wLastError: UInt32
    dwTime: UInt32
    hTask: Windows.Win32.Foundation.HANDLE
class MONHSZSTRUCTA(Structure):
    cb: UInt32
    fsAction: Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hsz: Windows.Win32.System.DataExchange.HSZ
    hTask: Windows.Win32.Foundation.HANDLE
    str: Windows.Win32.Foundation.CHAR * 1
class MONHSZSTRUCTW(Structure):
    cb: UInt32
    fsAction: Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hsz: Windows.Win32.System.DataExchange.HSZ
    hTask: Windows.Win32.Foundation.HANDLE
    str: Char * 1
class MONLINKSTRUCT(Structure):
    cb: UInt32
    dwTime: UInt32
    hTask: Windows.Win32.Foundation.HANDLE
    fEstablished: Windows.Win32.Foundation.BOOL
    fNoData: Windows.Win32.Foundation.BOOL
    hszSvc: Windows.Win32.System.DataExchange.HSZ
    hszTopic: Windows.Win32.System.DataExchange.HSZ
    hszItem: Windows.Win32.System.DataExchange.HSZ
    wFmt: UInt32
    fServer: Windows.Win32.Foundation.BOOL
    hConvServer: Windows.Win32.System.DataExchange.HCONV
    hConvClient: Windows.Win32.System.DataExchange.HCONV
class MONMSGSTRUCT(Structure):
    cb: UInt32
    hwndTo: Windows.Win32.Foundation.HWND
    dwTime: UInt32
    hTask: Windows.Win32.Foundation.HANDLE
    wMsg: UInt32
    wParam: Windows.Win32.Foundation.WPARAM
    lParam: Windows.Win32.Foundation.LPARAM
    dmhd: Windows.Win32.System.DataExchange.DDEML_MSG_HOOK_DATA
@winfunctype_pointer
def PFNCALLBACK(wType: UInt32, wFmt: UInt32, hConv: Windows.Win32.System.DataExchange.HCONV, hsz1: Windows.Win32.System.DataExchange.HSZ, hsz2: Windows.Win32.System.DataExchange.HSZ, hData: Windows.Win32.System.DataExchange.HDDEDATA, dwData1: UIntPtr, dwData2: UIntPtr) -> Windows.Win32.System.DataExchange.HDDEDATA: ...
make_head(_module, 'CONVCONTEXT')
make_head(_module, 'CONVINFO')
make_head(_module, 'COPYDATASTRUCT')
make_head(_module, 'DDEACK')
make_head(_module, 'DDEADVISE')
make_head(_module, 'DDEDATA')
make_head(_module, 'DDELN')
make_head(_module, 'DDEML_MSG_HOOK_DATA')
make_head(_module, 'DDEPOKE')
make_head(_module, 'DDEUP')
make_head(_module, 'HSZPAIR')
make_head(_module, 'METAFILEPICT')
make_head(_module, 'MONCBSTRUCT')
make_head(_module, 'MONCONVSTRUCT')
make_head(_module, 'MONERRSTRUCT')
make_head(_module, 'MONHSZSTRUCTA')
make_head(_module, 'MONHSZSTRUCTW')
make_head(_module, 'MONLINKSTRUCT')
make_head(_module, 'MONMSGSTRUCT')
make_head(_module, 'PFNCALLBACK')
__all__ = [
    "APPCLASS_MASK",
    "APPCLASS_MONITOR",
    "APPCLASS_STANDARD",
    "APPCMD_CLIENTONLY",
    "APPCMD_FILTERINITS",
    "APPCMD_MASK",
    "AddAtomA",
    "AddAtomW",
    "AddClipboardFormatListener",
    "CADV_LATEACK",
    "CBF_FAIL_ADVISES",
    "CBF_FAIL_ALLSVRXACTIONS",
    "CBF_FAIL_CONNECTIONS",
    "CBF_FAIL_EXECUTES",
    "CBF_FAIL_POKES",
    "CBF_FAIL_REQUESTS",
    "CBF_FAIL_SELFCONNECTIONS",
    "CBF_SKIP_ALLNOTIFICATIONS",
    "CBF_SKIP_CONNECT_CONFIRMS",
    "CBF_SKIP_DISCONNECTS",
    "CBF_SKIP_REGISTRATIONS",
    "CBF_SKIP_UNREGISTRATIONS",
    "CONVCONTEXT",
    "CONVINFO",
    "CONVINFO_CONVERSATION_STATE",
    "CONVINFO_STATUS",
    "COPYDATASTRUCT",
    "CP_WINANSI",
    "CP_WINNEUTRAL",
    "CP_WINUNICODE",
    "ChangeClipboardChain",
    "CloseClipboard",
    "CountClipboardFormats",
    "DDEACK",
    "DDEADVISE",
    "DDEDATA",
    "DDELN",
    "DDEML_MSG_HOOK_DATA",
    "DDEPOKE",
    "DDEUP",
    "DDE_CLIENT_TRANSACTION_TYPE",
    "DDE_ENABLE_CALLBACK_CMD",
    "DDE_FACK",
    "DDE_FACKREQ",
    "DDE_FAPPSTATUS",
    "DDE_FBUSY",
    "DDE_FDEFERUPD",
    "DDE_FNOTPROCESSED",
    "DDE_FRELEASE",
    "DDE_FREQUESTED",
    "DDE_INITIALIZE_COMMAND",
    "DDE_NAME_SERVICE_CMD",
    "DMLERR_ADVACKTIMEOUT",
    "DMLERR_BUSY",
    "DMLERR_DATAACKTIMEOUT",
    "DMLERR_DLL_NOT_INITIALIZED",
    "DMLERR_DLL_USAGE",
    "DMLERR_EXECACKTIMEOUT",
    "DMLERR_FIRST",
    "DMLERR_INVALIDPARAMETER",
    "DMLERR_LAST",
    "DMLERR_LOW_MEMORY",
    "DMLERR_MEMORY_ERROR",
    "DMLERR_NOTPROCESSED",
    "DMLERR_NO_CONV_ESTABLISHED",
    "DMLERR_NO_ERROR",
    "DMLERR_POKEACKTIMEOUT",
    "DMLERR_POSTMSG_FAILED",
    "DMLERR_REENTRANCY",
    "DMLERR_SERVER_DIED",
    "DMLERR_SYS_ERROR",
    "DMLERR_UNADVACKTIMEOUT",
    "DMLERR_UNFOUND_QUEUE_ID",
    "DNS_FILTEROFF",
    "DNS_FILTERON",
    "DNS_REGISTER",
    "DNS_UNREGISTER",
    "DdeAbandonTransaction",
    "DdeAccessData",
    "DdeAddData",
    "DdeClientTransaction",
    "DdeCmpStringHandles",
    "DdeConnect",
    "DdeConnectList",
    "DdeCreateDataHandle",
    "DdeCreateStringHandleA",
    "DdeCreateStringHandleW",
    "DdeDisconnect",
    "DdeDisconnectList",
    "DdeEnableCallback",
    "DdeFreeDataHandle",
    "DdeFreeStringHandle",
    "DdeGetData",
    "DdeGetLastError",
    "DdeImpersonateClient",
    "DdeInitializeA",
    "DdeInitializeW",
    "DdeKeepStringHandle",
    "DdeNameService",
    "DdePostAdvise",
    "DdeQueryConvInfo",
    "DdeQueryNextServer",
    "DdeQueryStringA",
    "DdeQueryStringW",
    "DdeReconnect",
    "DdeSetQualityOfService",
    "DdeSetUserHandle",
    "DdeUnaccessData",
    "DdeUninitialize",
    "DeleteAtom",
    "EC_DISABLE",
    "EC_ENABLEALL",
    "EC_ENABLEONE",
    "EC_QUERYWAITING",
    "EmptyClipboard",
    "EnumClipboardFormats",
    "FindAtomA",
    "FindAtomW",
    "FreeDDElParam",
    "GetAtomNameA",
    "GetAtomNameW",
    "GetClipboardData",
    "GetClipboardFormatNameA",
    "GetClipboardFormatNameW",
    "GetClipboardOwner",
    "GetClipboardSequenceNumber",
    "GetClipboardViewer",
    "GetOpenClipboardWindow",
    "GetPriorityClipboardFormat",
    "GetUpdatedClipboardFormats",
    "GlobalAddAtomA",
    "GlobalAddAtomExA",
    "GlobalAddAtomExW",
    "GlobalAddAtomW",
    "GlobalDeleteAtom",
    "GlobalFindAtomA",
    "GlobalFindAtomW",
    "GlobalGetAtomNameA",
    "GlobalGetAtomNameW",
    "HCONV",
    "HCONVLIST",
    "HDATA_APPOWNED",
    "HDDEDATA",
    "HSZ",
    "HSZPAIR",
    "ImpersonateDdeClientWindow",
    "InitAtomTable",
    "IsClipboardFormatAvailable",
    "MAX_MONITORS",
    "METAFILEPICT",
    "MF_CALLBACKS",
    "MF_CONV",
    "MF_ERRORS",
    "MF_HSZ_INFO",
    "MF_LINKS",
    "MF_MASK",
    "MF_POSTMSGS",
    "MF_SENDMSGS",
    "MH_CLEANUP",
    "MH_CREATE",
    "MH_DELETE",
    "MH_KEEP",
    "MONCBSTRUCT",
    "MONCONVSTRUCT",
    "MONERRSTRUCT",
    "MONHSZSTRUCTA",
    "MONHSZSTRUCTW",
    "MONLINKSTRUCT",
    "MONMSGSTRUCT",
    "MSGF_DDEMGR",
    "OpenClipboard",
    "PFNCALLBACK",
    "PackDDElParam",
    "QID_SYNC",
    "RegisterClipboardFormatA",
    "RegisterClipboardFormatW",
    "RemoveClipboardFormatListener",
    "ReuseDDElParam",
    "ST_ADVISE",
    "ST_BLOCKED",
    "ST_BLOCKNEXT",
    "ST_CLIENT",
    "ST_CONNECTED",
    "ST_INLIST",
    "ST_ISLOCAL",
    "ST_ISSELF",
    "ST_TERMINATED",
    "SZDDESYS_ITEM_FORMATS",
    "SZDDESYS_ITEM_HELP",
    "SZDDESYS_ITEM_RTNMSG",
    "SZDDESYS_ITEM_STATUS",
    "SZDDESYS_ITEM_SYSITEMS",
    "SZDDESYS_ITEM_TOPICS",
    "SZDDESYS_TOPIC",
    "SZDDE_ITEM_ITEMLIST",
    "SetClipboardData",
    "SetClipboardViewer",
    "SetWinMetaFileBits",
    "TIMEOUT_ASYNC",
    "UnpackDDElParam",
    "WM_DDE_ACK",
    "WM_DDE_ADVISE",
    "WM_DDE_DATA",
    "WM_DDE_EXECUTE",
    "WM_DDE_FIRST",
    "WM_DDE_INITIATE",
    "WM_DDE_LAST",
    "WM_DDE_POKE",
    "WM_DDE_REQUEST",
    "WM_DDE_TERMINATE",
    "WM_DDE_UNADVISE",
    "XCLASS_BOOL",
    "XCLASS_DATA",
    "XCLASS_FLAGS",
    "XCLASS_MASK",
    "XCLASS_NOTIFICATION",
    "XST_ADVACKRCVD",
    "XST_ADVDATAACKRCVD",
    "XST_ADVDATASENT",
    "XST_ADVSENT",
    "XST_CONNECTED",
    "XST_DATARCVD",
    "XST_EXECACKRCVD",
    "XST_EXECSENT",
    "XST_INCOMPLETE",
    "XST_INIT1",
    "XST_INIT2",
    "XST_NULL",
    "XST_POKEACKRCVD",
    "XST_POKESENT",
    "XST_REQSENT",
    "XST_UNADVACKRCVD",
    "XST_UNADVSENT",
    "XTYPF_ACKREQ",
    "XTYPF_NOBLOCK",
    "XTYPF_NODATA",
    "XTYP_ADVDATA",
    "XTYP_ADVREQ",
    "XTYP_ADVSTART",
    "XTYP_ADVSTOP",
    "XTYP_CONNECT",
    "XTYP_CONNECT_CONFIRM",
    "XTYP_DISCONNECT",
    "XTYP_EXECUTE",
    "XTYP_MASK",
    "XTYP_MONITOR",
    "XTYP_POKE",
    "XTYP_REGISTER",
    "XTYP_REQUEST",
    "XTYP_SHIFT",
    "XTYP_UNREGISTER",
    "XTYP_WILDCONNECT",
    "XTYP_XACT_COMPLETE",
]
_arch_optional = [
]
