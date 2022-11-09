from win32more.base import *
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.DataExchange

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
WM_DDE_FIRST = 992
WM_DDE_INITIATE = 992
WM_DDE_TERMINATE = 993
WM_DDE_ADVISE = 994
WM_DDE_UNADVISE = 995
WM_DDE_ACK = 996
WM_DDE_DATA = 997
WM_DDE_REQUEST = 998
WM_DDE_POKE = 999
WM_DDE_EXECUTE = 1000
WM_DDE_LAST = 1000
CADV_LATEACK = 65535
DDE_FACK = 32768
DDE_FBUSY = 16384
DDE_FDEFERUPD = 16384
DDE_FACKREQ = 32768
DDE_FRELEASE = 8192
DDE_FREQUESTED = 4096
DDE_FAPPSTATUS = 255
DDE_FNOTPROCESSED = 0
MSGF_DDEMGR = 32769
CP_WINANSI = 1004
CP_WINUNICODE = 1200
CP_WINNEUTRAL = 1200
XTYPF_NOBLOCK = 2
XTYPF_NODATA = 4
XTYPF_ACKREQ = 8
XCLASS_MASK = 64512
XCLASS_BOOL = 4096
XCLASS_DATA = 8192
XCLASS_FLAGS = 16384
XCLASS_NOTIFICATION = 32768
XTYP_MASK = 240
XTYP_SHIFT = 4
TIMEOUT_ASYNC = 4294967295
QID_SYNC = 4294967295
APPCMD_MASK = 4080
APPCLASS_MASK = 15
HDATA_APPOWNED = 1
DMLERR_NO_ERROR = 0
DMLERR_FIRST = 16384
DMLERR_ADVACKTIMEOUT = 16384
DMLERR_BUSY = 16385
DMLERR_DATAACKTIMEOUT = 16386
DMLERR_DLL_NOT_INITIALIZED = 16387
DMLERR_DLL_USAGE = 16388
DMLERR_EXECACKTIMEOUT = 16389
DMLERR_INVALIDPARAMETER = 16390
DMLERR_LOW_MEMORY = 16391
DMLERR_MEMORY_ERROR = 16392
DMLERR_NOTPROCESSED = 16393
DMLERR_NO_CONV_ESTABLISHED = 16394
DMLERR_POKEACKTIMEOUT = 16395
DMLERR_POSTMSG_FAILED = 16396
DMLERR_REENTRANCY = 16397
DMLERR_SERVER_DIED = 16398
DMLERR_SYS_ERROR = 16399
DMLERR_UNADVACKTIMEOUT = 16400
DMLERR_UNFOUND_QUEUE_ID = 16401
DMLERR_LAST = 16401
MH_CREATE = 1
MH_KEEP = 2
MH_DELETE = 3
MH_CLEANUP = 4
MAX_MONITORS = 4
MF_MASK = 4278190080
DDE_ENABLE_CALLBACK_CMD = UInt32
EC_ENABLEALL = 0
EC_ENABLEONE = 128
EC_DISABLE = 8
EC_QUERYWAITING = 2
DDE_INITIALIZE_COMMAND = UInt32
APPCLASS_MONITOR = 1
APPCLASS_STANDARD = 0
APPCMD_CLIENTONLY = 16
APPCMD_FILTERINITS = 32
CBF_FAIL_ALLSVRXACTIONS = 258048
CBF_FAIL_ADVISES = 16384
CBF_FAIL_CONNECTIONS = 8192
CBF_FAIL_EXECUTES = 32768
CBF_FAIL_POKES = 65536
CBF_FAIL_REQUESTS = 131072
CBF_FAIL_SELFCONNECTIONS = 4096
CBF_SKIP_ALLNOTIFICATIONS = 3932160
CBF_SKIP_CONNECT_CONFIRMS = 262144
CBF_SKIP_DISCONNECTS = 2097152
CBF_SKIP_REGISTRATIONS = 524288
CBF_SKIP_UNREGISTRATIONS = 1048576
MF_CALLBACKS = 134217728
MF_CONV = 1073741824
MF_ERRORS = 268435456
MF_HSZ_INFO = 16777216
MF_LINKS = 536870912
MF_POSTMSGS = 67108864
MF_SENDMSGS = 33554432
DDE_NAME_SERVICE_CMD = UInt32
DNS_REGISTER = 1
DNS_UNREGISTER = 2
DNS_FILTERON = 4
DNS_FILTEROFF = 8
DDE_CLIENT_TRANSACTION_TYPE = UInt32
XTYP_ADVSTART = 4144
XTYP_ADVSTOP = 32832
XTYP_EXECUTE = 16464
XTYP_POKE = 16528
XTYP_REQUEST = 8368
XTYP_ADVDATA = 16400
XTYP_ADVREQ = 8226
XTYP_CONNECT = 4194
XTYP_CONNECT_CONFIRM = 32882
XTYP_DISCONNECT = 32962
XTYP_MONITOR = 33010
XTYP_REGISTER = 32930
XTYP_UNREGISTER = 32978
XTYP_WILDCONNECT = 8418
XTYP_XACT_COMPLETE = 32896
CONVINFO_CONVERSATION_STATE = UInt32
XST_ADVACKRCVD = 13
XST_ADVDATAACKRCVD = 16
XST_ADVDATASENT = 15
XST_ADVSENT = 11
XST_CONNECTED = 2
XST_DATARCVD = 6
XST_EXECACKRCVD = 10
XST_EXECSENT = 9
XST_INCOMPLETE = 1
XST_INIT1 = 3
XST_INIT2 = 4
XST_NULL = 0
XST_POKEACKRCVD = 8
XST_POKESENT = 7
XST_REQSENT = 5
XST_UNADVACKRCVD = 14
XST_UNADVSENT = 12
CONVINFO_STATUS = UInt32
ST_ADVISE = 2
ST_BLOCKED = 8
ST_BLOCKNEXT = 128
ST_CLIENT = 16
ST_CONNECTED = 1
ST_INLIST = 64
ST_ISLOCAL = 4
ST_ISSELF = 256
ST_TERMINATED = 32
HSZ = IntPtr
HCONV = IntPtr
HCONVLIST = IntPtr
HDDEDATA = IntPtr
def _define_DDEACK_head():
    class DDEACK(Structure):
        pass
    return DDEACK
def _define_DDEACK():
    DDEACK = win32more.System.DataExchange.DDEACK_head
    DDEACK._fields_ = [
        ("_bitfield", UInt16),
    ]
    return DDEACK
def _define_DDEADVISE_head():
    class DDEADVISE(Structure):
        pass
    return DDEADVISE
def _define_DDEADVISE():
    DDEADVISE = win32more.System.DataExchange.DDEADVISE_head
    DDEADVISE._fields_ = [
        ("_bitfield", UInt16),
        ("cfFormat", Int16),
    ]
    return DDEADVISE
def _define_DDEDATA_head():
    class DDEDATA(Structure):
        pass
    return DDEDATA
def _define_DDEDATA():
    DDEDATA = win32more.System.DataExchange.DDEDATA_head
    DDEDATA._fields_ = [
        ("_bitfield", UInt16),
        ("cfFormat", Int16),
        ("Value", Byte * 0),
    ]
    return DDEDATA
def _define_DDEPOKE_head():
    class DDEPOKE(Structure):
        pass
    return DDEPOKE
def _define_DDEPOKE():
    DDEPOKE = win32more.System.DataExchange.DDEPOKE_head
    DDEPOKE._fields_ = [
        ("_bitfield", UInt16),
        ("cfFormat", Int16),
        ("Value", Byte * 0),
    ]
    return DDEPOKE
def _define_DDELN_head():
    class DDELN(Structure):
        pass
    return DDELN
def _define_DDELN():
    DDELN = win32more.System.DataExchange.DDELN_head
    DDELN._fields_ = [
        ("_bitfield", UInt16),
        ("cfFormat", Int16),
    ]
    return DDELN
def _define_DDEUP_head():
    class DDEUP(Structure):
        pass
    return DDEUP
def _define_DDEUP():
    DDEUP = win32more.System.DataExchange.DDEUP_head
    DDEUP._fields_ = [
        ("_bitfield", UInt16),
        ("cfFormat", Int16),
        ("rgb", Byte * 0),
    ]
    return DDEUP
def _define_HSZPAIR_head():
    class HSZPAIR(Structure):
        pass
    return HSZPAIR
def _define_HSZPAIR():
    HSZPAIR = win32more.System.DataExchange.HSZPAIR_head
    HSZPAIR._fields_ = [
        ("hszSvc", win32more.System.DataExchange.HSZ),
        ("hszTopic", win32more.System.DataExchange.HSZ),
    ]
    return HSZPAIR
def _define_CONVCONTEXT_head():
    class CONVCONTEXT(Structure):
        pass
    return CONVCONTEXT
def _define_CONVCONTEXT():
    CONVCONTEXT = win32more.System.DataExchange.CONVCONTEXT_head
    CONVCONTEXT._fields_ = [
        ("cb", UInt32),
        ("wFlags", UInt32),
        ("wCountryID", UInt32),
        ("iCodePage", Int32),
        ("dwLangID", UInt32),
        ("dwSecurity", UInt32),
        ("qos", win32more.Security.SECURITY_QUALITY_OF_SERVICE),
    ]
    return CONVCONTEXT
def _define_CONVINFO_head():
    class CONVINFO(Structure):
        pass
    return CONVINFO
def _define_CONVINFO():
    CONVINFO = win32more.System.DataExchange.CONVINFO_head
    CONVINFO._fields_ = [
        ("cb", UInt32),
        ("hUser", UIntPtr),
        ("hConvPartner", win32more.System.DataExchange.HCONV),
        ("hszSvcPartner", win32more.System.DataExchange.HSZ),
        ("hszServiceReq", win32more.System.DataExchange.HSZ),
        ("hszTopic", win32more.System.DataExchange.HSZ),
        ("hszItem", win32more.System.DataExchange.HSZ),
        ("wFmt", UInt32),
        ("wType", win32more.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE),
        ("wStatus", win32more.System.DataExchange.CONVINFO_STATUS),
        ("wConvst", win32more.System.DataExchange.CONVINFO_CONVERSATION_STATE),
        ("wLastError", UInt32),
        ("hConvList", win32more.System.DataExchange.HCONVLIST),
        ("ConvCtxt", win32more.System.DataExchange.CONVCONTEXT),
        ("hwnd", win32more.Foundation.HWND),
        ("hwndPartner", win32more.Foundation.HWND),
    ]
    return CONVINFO
def _define_PFNCALLBACK():
    return CFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HDDEDATA,UIntPtr,UIntPtr, use_last_error=False)
def _define_DDEML_MSG_HOOK_DATA_head():
    class DDEML_MSG_HOOK_DATA(Structure):
        pass
    return DDEML_MSG_HOOK_DATA
def _define_DDEML_MSG_HOOK_DATA():
    DDEML_MSG_HOOK_DATA = win32more.System.DataExchange.DDEML_MSG_HOOK_DATA_head
    DDEML_MSG_HOOK_DATA._fields_ = [
        ("uiLo", UIntPtr),
        ("uiHi", UIntPtr),
        ("cbData", UInt32),
        ("Data", UInt32 * 8),
    ]
    return DDEML_MSG_HOOK_DATA
def _define_MONMSGSTRUCT_head():
    class MONMSGSTRUCT(Structure):
        pass
    return MONMSGSTRUCT
def _define_MONMSGSTRUCT():
    MONMSGSTRUCT = win32more.System.DataExchange.MONMSGSTRUCT_head
    MONMSGSTRUCT._fields_ = [
        ("cb", UInt32),
        ("hwndTo", win32more.Foundation.HWND),
        ("dwTime", UInt32),
        ("hTask", win32more.Foundation.HANDLE),
        ("wMsg", UInt32),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
        ("dmhd", win32more.System.DataExchange.DDEML_MSG_HOOK_DATA),
    ]
    return MONMSGSTRUCT
def _define_MONCBSTRUCT_head():
    class MONCBSTRUCT(Structure):
        pass
    return MONCBSTRUCT
def _define_MONCBSTRUCT():
    MONCBSTRUCT = win32more.System.DataExchange.MONCBSTRUCT_head
    MONCBSTRUCT._fields_ = [
        ("cb", UInt32),
        ("dwTime", UInt32),
        ("hTask", win32more.Foundation.HANDLE),
        ("dwRet", UInt32),
        ("wType", UInt32),
        ("wFmt", UInt32),
        ("hConv", win32more.System.DataExchange.HCONV),
        ("hsz1", win32more.System.DataExchange.HSZ),
        ("hsz2", win32more.System.DataExchange.HSZ),
        ("hData", win32more.System.DataExchange.HDDEDATA),
        ("dwData1", UIntPtr),
        ("dwData2", UIntPtr),
        ("cc", win32more.System.DataExchange.CONVCONTEXT),
        ("cbData", UInt32),
        ("Data", UInt32 * 8),
    ]
    return MONCBSTRUCT
def _define_MONHSZSTRUCTA_head():
    class MONHSZSTRUCTA(Structure):
        pass
    return MONHSZSTRUCTA
def _define_MONHSZSTRUCTA():
    MONHSZSTRUCTA = win32more.System.DataExchange.MONHSZSTRUCTA_head
    MONHSZSTRUCTA._fields_ = [
        ("cb", UInt32),
        ("fsAction", win32more.Foundation.BOOL),
        ("dwTime", UInt32),
        ("hsz", win32more.System.DataExchange.HSZ),
        ("hTask", win32more.Foundation.HANDLE),
        ("str", win32more.Foundation.CHAR * 0),
    ]
    return MONHSZSTRUCTA
def _define_MONHSZSTRUCTW_head():
    class MONHSZSTRUCTW(Structure):
        pass
    return MONHSZSTRUCTW
def _define_MONHSZSTRUCTW():
    MONHSZSTRUCTW = win32more.System.DataExchange.MONHSZSTRUCTW_head
    MONHSZSTRUCTW._fields_ = [
        ("cb", UInt32),
        ("fsAction", win32more.Foundation.BOOL),
        ("dwTime", UInt32),
        ("hsz", win32more.System.DataExchange.HSZ),
        ("hTask", win32more.Foundation.HANDLE),
        ("str", Char * 0),
    ]
    return MONHSZSTRUCTW
def _define_MONERRSTRUCT_head():
    class MONERRSTRUCT(Structure):
        pass
    return MONERRSTRUCT
def _define_MONERRSTRUCT():
    MONERRSTRUCT = win32more.System.DataExchange.MONERRSTRUCT_head
    MONERRSTRUCT._fields_ = [
        ("cb", UInt32),
        ("wLastError", UInt32),
        ("dwTime", UInt32),
        ("hTask", win32more.Foundation.HANDLE),
    ]
    return MONERRSTRUCT
def _define_MONLINKSTRUCT_head():
    class MONLINKSTRUCT(Structure):
        pass
    return MONLINKSTRUCT
def _define_MONLINKSTRUCT():
    MONLINKSTRUCT = win32more.System.DataExchange.MONLINKSTRUCT_head
    MONLINKSTRUCT._fields_ = [
        ("cb", UInt32),
        ("dwTime", UInt32),
        ("hTask", win32more.Foundation.HANDLE),
        ("fEstablished", win32more.Foundation.BOOL),
        ("fNoData", win32more.Foundation.BOOL),
        ("hszSvc", win32more.System.DataExchange.HSZ),
        ("hszTopic", win32more.System.DataExchange.HSZ),
        ("hszItem", win32more.System.DataExchange.HSZ),
        ("wFmt", UInt32),
        ("fServer", win32more.Foundation.BOOL),
        ("hConvServer", win32more.System.DataExchange.HCONV),
        ("hConvClient", win32more.System.DataExchange.HCONV),
    ]
    return MONLINKSTRUCT
def _define_MONCONVSTRUCT_head():
    class MONCONVSTRUCT(Structure):
        pass
    return MONCONVSTRUCT
def _define_MONCONVSTRUCT():
    MONCONVSTRUCT = win32more.System.DataExchange.MONCONVSTRUCT_head
    MONCONVSTRUCT._fields_ = [
        ("cb", UInt32),
        ("fConnect", win32more.Foundation.BOOL),
        ("dwTime", UInt32),
        ("hTask", win32more.Foundation.HANDLE),
        ("hszSvc", win32more.System.DataExchange.HSZ),
        ("hszTopic", win32more.System.DataExchange.HSZ),
        ("hConvClient", win32more.System.DataExchange.HCONV),
        ("hConvServer", win32more.System.DataExchange.HCONV),
    ]
    return MONCONVSTRUCT
def _define_METAFILEPICT_head():
    class METAFILEPICT(Structure):
        pass
    return METAFILEPICT
def _define_METAFILEPICT():
    METAFILEPICT = win32more.System.DataExchange.METAFILEPICT_head
    METAFILEPICT._fields_ = [
        ("mm", Int32),
        ("xExt", Int32),
        ("yExt", Int32),
        ("hMF", win32more.Graphics.Gdi.HMETAFILE),
    ]
    return METAFILEPICT
def _define_COPYDATASTRUCT_head():
    class COPYDATASTRUCT(Structure):
        pass
    return COPYDATASTRUCT
def _define_COPYDATASTRUCT():
    COPYDATASTRUCT = win32more.System.DataExchange.COPYDATASTRUCT_head
    COPYDATASTRUCT._fields_ = [
        ("dwData", UIntPtr),
        ("cbData", UInt32),
        ("lpData", c_void_p),
    ]
    return COPYDATASTRUCT
def _define_DdeSetQualityOfService():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Security.SECURITY_QUALITY_OF_SERVICE_head),POINTER(win32more.Security.SECURITY_QUALITY_OF_SERVICE_head), use_last_error=True)(("DdeSetQualityOfService", windll["USER32"]), ((1, 'hwndClient'),(1, 'pqosNew'),(1, 'pqosPrev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImpersonateDdeClientWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=True)(("ImpersonateDdeClientWindow", windll["USER32"]), ((1, 'hWndClient'),(1, 'hWndServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.LPARAM,UInt32,UIntPtr,UIntPtr, use_last_error=False)(("PackDDElParam", windll["USER32"]), ((1, 'msg'),(1, 'uiLo'),(1, 'uiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnpackDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.LPARAM,POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=False)(("UnpackDDElParam", windll["USER32"]), ((1, 'msg'),(1, 'lParam'),(1, 'puiLo'),(1, 'puiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.LPARAM, use_last_error=False)(("FreeDDElParam", windll["USER32"]), ((1, 'msg'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReuseDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.LPARAM,win32more.Foundation.LPARAM,UInt32,UInt32,UIntPtr,UIntPtr, use_last_error=False)(("ReuseDDElParam", windll["USER32"]), ((1, 'lParam'),(1, 'msgIn'),(1, 'msgOut'),(1, 'uiLo'),(1, 'uiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeInitializeA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.System.DataExchange.PFNCALLBACK,win32more.System.DataExchange.DDE_INITIALIZE_COMMAND,UInt32, use_last_error=False)(("DdeInitializeA", windll["USER32"]), ((1, 'pidInst'),(1, 'pfnCallback'),(1, 'afCmd'),(1, 'ulRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeInitializeW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.System.DataExchange.PFNCALLBACK,win32more.System.DataExchange.DDE_INITIALIZE_COMMAND,UInt32, use_last_error=False)(("DdeInitializeW", windll["USER32"]), ((1, 'pidInst'),(1, 'pfnCallback'),(1, 'afCmd'),(1, 'ulRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeInitialize():
    return win32more.System.DataExchange.DdeInitializeW
def _define_DdeUninitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("DdeUninitialize", windll["USER32"]), ((1, 'idInst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeConnectList():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONVLIST,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HCONVLIST,POINTER(win32more.System.DataExchange.CONVCONTEXT_head), use_last_error=False)(("DdeConnectList", windll["USER32"]), ((1, 'idInst'),(1, 'hszService'),(1, 'hszTopic'),(1, 'hConvList'),(1, 'pCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryNextServer():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HCONVLIST,win32more.System.DataExchange.HCONV, use_last_error=False)(("DdeQueryNextServer", windll["USER32"]), ((1, 'hConvList'),(1, 'hConvPrev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeDisconnectList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONVLIST, use_last_error=False)(("DdeDisconnectList", windll["USER32"]), ((1, 'hConvList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeConnect():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,POINTER(win32more.System.DataExchange.CONVCONTEXT_head), use_last_error=False)(("DdeConnect", windll["USER32"]), ((1, 'idInst'),(1, 'hszService'),(1, 'hszTopic'),(1, 'pCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeDisconnect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV, use_last_error=False)(("DdeDisconnect", windll["USER32"]), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeReconnect():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HCONV, use_last_error=False)(("DdeReconnect", windll["USER32"]), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryConvInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.DataExchange.HCONV,UInt32,POINTER(win32more.System.DataExchange.CONVINFO_head), use_last_error=False)(("DdeQueryConvInfo", windll["USER32"]), ((1, 'hConv'),(1, 'idTransaction'),(1, 'pConvInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeSetUserHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV,UInt32,UIntPtr, use_last_error=False)(("DdeSetUserHandle", windll["USER32"]), ((1, 'hConv'),(1, 'id'),(1, 'hUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAbandonTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HCONV,UInt32, use_last_error=False)(("DdeAbandonTransaction", windll["USER32"]), ((1, 'idInst'),(1, 'hConv'),(1, 'idTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdePostAdvise():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ, use_last_error=False)(("DdePostAdvise", windll["USER32"]), ((1, 'idInst'),(1, 'hszTopic'),(1, 'hszItem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeEnableCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.DDE_ENABLE_CALLBACK_CMD, use_last_error=False)(("DdeEnableCallback", windll["USER32"]), ((1, 'idInst'),(1, 'hConv'),(1, 'wCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeImpersonateClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV, use_last_error=True)(("DdeImpersonateClient", windll["USER32"]), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeNameService():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.DDE_NAME_SERVICE_CMD, use_last_error=False)(("DdeNameService", windll["USER32"]), ((1, 'idInst'),(1, 'hsz1'),(1, 'hsz2'),(1, 'afCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeClientTransaction():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HSZ,UInt32,win32more.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE,UInt32,POINTER(UInt32), use_last_error=False)(("DdeClientTransaction", windll["USER32"]), ((1, 'pData'),(1, 'cbData'),(1, 'hConv'),(1, 'hszItem'),(1, 'wFmt'),(1, 'wType'),(1, 'dwTimeout'),(1, 'pdwResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateDataHandle():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,c_char_p_no,UInt32,UInt32,win32more.System.DataExchange.HSZ,UInt32,UInt32, use_last_error=False)(("DdeCreateDataHandle", windll["USER32"]), ((1, 'idInst'),(1, 'pSrc'),(1, 'cb'),(1, 'cbOff'),(1, 'hszItem'),(1, 'wFmt'),(1, 'afCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAddData():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,UInt32, use_last_error=False)(("DdeAddData", windll["USER32"]), ((1, 'hData'),(1, 'pSrc'),(1, 'cb'),(1, 'cbOff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeGetData():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,UInt32, use_last_error=False)(("DdeGetData", windll["USER32"]), ((1, 'hData'),(1, 'pDst'),(1, 'cbMax'),(1, 'cbOff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAccessData():
    try:
        return WINFUNCTYPE(c_char_p_no,win32more.System.DataExchange.HDDEDATA,POINTER(UInt32), use_last_error=False)(("DdeAccessData", windll["USER32"]), ((1, 'hData'),(1, 'pcbDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeUnaccessData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HDDEDATA, use_last_error=False)(("DdeUnaccessData", windll["USER32"]), ((1, 'hData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeFreeDataHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HDDEDATA, use_last_error=False)(("DdeFreeDataHandle", windll["USER32"]), ((1, 'hData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeGetLastError():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("DdeGetLastError", windll["USER32"]), ((1, 'idInst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateStringHandleA():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HSZ,UInt32,win32more.Foundation.PSTR,Int32, use_last_error=False)(("DdeCreateStringHandleA", windll["USER32"]), ((1, 'idInst'),(1, 'psz'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateStringHandleW():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HSZ,UInt32,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("DdeCreateStringHandleW", windll["USER32"]), ((1, 'idInst'),(1, 'psz'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateStringHandle():
    return win32more.System.DataExchange.DdeCreateStringHandleW
def _define_DdeQueryStringA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.System.DataExchange.HSZ,POINTER(Byte),UInt32,Int32, use_last_error=False)(("DdeQueryStringA", windll["USER32"]), ((1, 'idInst'),(1, 'hsz'),(1, 'psz'),(1, 'cchMax'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryStringW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.System.DataExchange.HSZ,POINTER(Char),UInt32,Int32, use_last_error=False)(("DdeQueryStringW", windll["USER32"]), ((1, 'idInst'),(1, 'hsz'),(1, 'psz'),(1, 'cchMax'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryString():
    return win32more.System.DataExchange.DdeQueryStringW
def _define_DdeFreeStringHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ, use_last_error=False)(("DdeFreeStringHandle", windll["USER32"]), ((1, 'idInst'),(1, 'hsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeKeepStringHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ, use_last_error=False)(("DdeKeepStringHandle", windll["USER32"]), ((1, 'idInst'),(1, 'hsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCmpStringHandles():
    try:
        return WINFUNCTYPE(Int32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ, use_last_error=False)(("DdeCmpStringHandles", windll["USER32"]), ((1, 'hsz1'),(1, 'hsz2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWinMetaFileBits():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,UInt32,c_char_p_no,win32more.Graphics.Gdi.HDC,POINTER(win32more.System.DataExchange.METAFILEPICT_head), use_last_error=False)(("SetWinMetaFileBits", windll["GDI32"]), ((1, 'nSize'),(1, 'lpMeta16Data'),(1, 'hdcRef'),(1, 'lpMFP'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("OpenClipboard", windll["USER32"]), ((1, 'hWndNewOwner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=True)(("CloseClipboard", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardSequenceNumber():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetClipboardSequenceNumber", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardOwner():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=True)(("GetClipboardOwner", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetClipboardViewer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=True)(("SetClipboardViewer", windll["USER32"]), ((1, 'hWndNewViewer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardViewer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=True)(("GetClipboardViewer", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeClipboardChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=False)(("ChangeClipboardChain", windll["USER32"]), ((1, 'hWndRemove'),(1, 'hWndNewNext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetClipboardData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE, use_last_error=True)(("SetClipboardData", windll["USER32"]), ((1, 'uFormat'),(1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("GetClipboardData", windll["USER32"]), ((1, 'uFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterClipboardFormatA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=True)(("RegisterClipboardFormatA", windll["USER32"]), ((1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterClipboardFormatW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=True)(("RegisterClipboardFormatW", windll["USER32"]), ((1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterClipboardFormat():
    return win32more.System.DataExchange.RegisterClipboardFormatW
def _define_CountClipboardFormats():
    try:
        return WINFUNCTYPE(Int32, use_last_error=True)(("CountClipboardFormats", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumClipboardFormats():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=True)(("EnumClipboardFormats", windll["USER32"]), ((1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardFormatNameA():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(Byte),Int32, use_last_error=True)(("GetClipboardFormatNameA", windll["USER32"]), ((1, 'format'),(1, 'lpszFormatName'),(1, 'cchMaxCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardFormatNameW():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(Char),Int32, use_last_error=True)(("GetClipboardFormatNameW", windll["USER32"]), ((1, 'format'),(1, 'lpszFormatName'),(1, 'cchMaxCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardFormatName():
    return win32more.System.DataExchange.GetClipboardFormatNameW
def _define_EmptyClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=True)(("EmptyClipboard", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsClipboardFormatAvailable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=True)(("IsClipboardFormatAvailable", windll["USER32"]), ((1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPriorityClipboardFormat():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),Int32, use_last_error=True)(("GetPriorityClipboardFormat", windll["USER32"]), ((1, 'paFormatPriorityList'),(1, 'cFormats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOpenClipboardWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=True)(("GetOpenClipboardWindow", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddClipboardFormatListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("AddClipboardFormatListener", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveClipboardFormatListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("RemoveClipboardFormatListener", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUpdatedClipboardFormats():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=True)(("GetUpdatedClipboardFormats", windll["USER32"]), ((1, 'lpuiFormats'),(1, 'cFormats'),(1, 'pcFormatsOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalDeleteAtom():
    try:
        return WINFUNCTYPE(UInt16,UInt16, use_last_error=True)(("GlobalDeleteAtom", windll["KERNEL32"]), ((1, 'nAtom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitAtomTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("InitAtomTable", windll["KERNEL32"]), ((1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAtom():
    try:
        return WINFUNCTYPE(UInt16,UInt16, use_last_error=True)(("DeleteAtom", windll["KERNEL32"]), ((1, 'nAtom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR, use_last_error=True)(("GlobalAddAtomA", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR, use_last_error=True)(("GlobalAddAtomW", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtom():
    return win32more.System.DataExchange.GlobalAddAtomW
def _define_GlobalAddAtomExA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("GlobalAddAtomExA", windll["KERNEL32"]), ((1, 'lpString'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomExW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("GlobalAddAtomExW", windll["KERNEL32"]), ((1, 'lpString'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomEx():
    return win32more.System.DataExchange.GlobalAddAtomExW
def _define_GlobalFindAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR, use_last_error=True)(("GlobalFindAtomA", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFindAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR, use_last_error=True)(("GlobalFindAtomW", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFindAtom():
    return win32more.System.DataExchange.GlobalFindAtomW
def _define_GlobalGetAtomNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(Byte),Int32, use_last_error=True)(("GlobalGetAtomNameA", windll["KERNEL32"]), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalGetAtomNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(Char),Int32, use_last_error=True)(("GlobalGetAtomNameW", windll["KERNEL32"]), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalGetAtomName():
    return win32more.System.DataExchange.GlobalGetAtomNameW
def _define_AddAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR, use_last_error=True)(("AddAtomA", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR, use_last_error=True)(("AddAtomW", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAtom():
    return win32more.System.DataExchange.AddAtomW
def _define_FindAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR, use_last_error=True)(("FindAtomA", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR, use_last_error=True)(("FindAtomW", windll["KERNEL32"]), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindAtom():
    return win32more.System.DataExchange.FindAtomW
def _define_GetAtomNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(Byte),Int32, use_last_error=True)(("GetAtomNameA", windll["KERNEL32"]), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAtomNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt16,POINTER(Char),Int32, use_last_error=True)(("GetAtomNameW", windll["KERNEL32"]), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAtomName():
    return win32more.System.DataExchange.GetAtomNameW
__all__ = [
    "WM_DDE_FIRST",
    "WM_DDE_INITIATE",
    "WM_DDE_TERMINATE",
    "WM_DDE_ADVISE",
    "WM_DDE_UNADVISE",
    "WM_DDE_ACK",
    "WM_DDE_DATA",
    "WM_DDE_REQUEST",
    "WM_DDE_POKE",
    "WM_DDE_EXECUTE",
    "WM_DDE_LAST",
    "CADV_LATEACK",
    "DDE_FACK",
    "DDE_FBUSY",
    "DDE_FDEFERUPD",
    "DDE_FACKREQ",
    "DDE_FRELEASE",
    "DDE_FREQUESTED",
    "DDE_FAPPSTATUS",
    "DDE_FNOTPROCESSED",
    "MSGF_DDEMGR",
    "CP_WINANSI",
    "CP_WINUNICODE",
    "CP_WINNEUTRAL",
    "XTYPF_NOBLOCK",
    "XTYPF_NODATA",
    "XTYPF_ACKREQ",
    "XCLASS_MASK",
    "XCLASS_BOOL",
    "XCLASS_DATA",
    "XCLASS_FLAGS",
    "XCLASS_NOTIFICATION",
    "XTYP_MASK",
    "XTYP_SHIFT",
    "TIMEOUT_ASYNC",
    "QID_SYNC",
    "APPCMD_MASK",
    "APPCLASS_MASK",
    "HDATA_APPOWNED",
    "DMLERR_NO_ERROR",
    "DMLERR_FIRST",
    "DMLERR_ADVACKTIMEOUT",
    "DMLERR_BUSY",
    "DMLERR_DATAACKTIMEOUT",
    "DMLERR_DLL_NOT_INITIALIZED",
    "DMLERR_DLL_USAGE",
    "DMLERR_EXECACKTIMEOUT",
    "DMLERR_INVALIDPARAMETER",
    "DMLERR_LOW_MEMORY",
    "DMLERR_MEMORY_ERROR",
    "DMLERR_NOTPROCESSED",
    "DMLERR_NO_CONV_ESTABLISHED",
    "DMLERR_POKEACKTIMEOUT",
    "DMLERR_POSTMSG_FAILED",
    "DMLERR_REENTRANCY",
    "DMLERR_SERVER_DIED",
    "DMLERR_SYS_ERROR",
    "DMLERR_UNADVACKTIMEOUT",
    "DMLERR_UNFOUND_QUEUE_ID",
    "DMLERR_LAST",
    "MH_CREATE",
    "MH_KEEP",
    "MH_DELETE",
    "MH_CLEANUP",
    "MAX_MONITORS",
    "MF_MASK",
    "DDE_ENABLE_CALLBACK_CMD",
    "EC_ENABLEALL",
    "EC_ENABLEONE",
    "EC_DISABLE",
    "EC_QUERYWAITING",
    "DDE_INITIALIZE_COMMAND",
    "APPCLASS_MONITOR",
    "APPCLASS_STANDARD",
    "APPCMD_CLIENTONLY",
    "APPCMD_FILTERINITS",
    "CBF_FAIL_ALLSVRXACTIONS",
    "CBF_FAIL_ADVISES",
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
    "MF_CALLBACKS",
    "MF_CONV",
    "MF_ERRORS",
    "MF_HSZ_INFO",
    "MF_LINKS",
    "MF_POSTMSGS",
    "MF_SENDMSGS",
    "DDE_NAME_SERVICE_CMD",
    "DNS_REGISTER",
    "DNS_UNREGISTER",
    "DNS_FILTERON",
    "DNS_FILTEROFF",
    "DDE_CLIENT_TRANSACTION_TYPE",
    "XTYP_ADVSTART",
    "XTYP_ADVSTOP",
    "XTYP_EXECUTE",
    "XTYP_POKE",
    "XTYP_REQUEST",
    "XTYP_ADVDATA",
    "XTYP_ADVREQ",
    "XTYP_CONNECT",
    "XTYP_CONNECT_CONFIRM",
    "XTYP_DISCONNECT",
    "XTYP_MONITOR",
    "XTYP_REGISTER",
    "XTYP_UNREGISTER",
    "XTYP_WILDCONNECT",
    "XTYP_XACT_COMPLETE",
    "CONVINFO_CONVERSATION_STATE",
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
    "CONVINFO_STATUS",
    "ST_ADVISE",
    "ST_BLOCKED",
    "ST_BLOCKNEXT",
    "ST_CLIENT",
    "ST_CONNECTED",
    "ST_INLIST",
    "ST_ISLOCAL",
    "ST_ISSELF",
    "ST_TERMINATED",
    "HSZ",
    "HCONV",
    "HCONVLIST",
    "HDDEDATA",
    "DDEACK",
    "DDEADVISE",
    "DDEDATA",
    "DDEPOKE",
    "DDELN",
    "DDEUP",
    "HSZPAIR",
    "CONVCONTEXT",
    "CONVINFO",
    "PFNCALLBACK",
    "DDEML_MSG_HOOK_DATA",
    "MONMSGSTRUCT",
    "MONCBSTRUCT",
    "MONHSZSTRUCTA",
    "MONHSZSTRUCTW",
    "MONERRSTRUCT",
    "MONLINKSTRUCT",
    "MONCONVSTRUCT",
    "METAFILEPICT",
    "COPYDATASTRUCT",
    "DdeSetQualityOfService",
    "ImpersonateDdeClientWindow",
    "PackDDElParam",
    "UnpackDDElParam",
    "FreeDDElParam",
    "ReuseDDElParam",
    "DdeInitializeA",
    "DdeInitializeW",
    "DdeInitialize",
    "DdeUninitialize",
    "DdeConnectList",
    "DdeQueryNextServer",
    "DdeDisconnectList",
    "DdeConnect",
    "DdeDisconnect",
    "DdeReconnect",
    "DdeQueryConvInfo",
    "DdeSetUserHandle",
    "DdeAbandonTransaction",
    "DdePostAdvise",
    "DdeEnableCallback",
    "DdeImpersonateClient",
    "DdeNameService",
    "DdeClientTransaction",
    "DdeCreateDataHandle",
    "DdeAddData",
    "DdeGetData",
    "DdeAccessData",
    "DdeUnaccessData",
    "DdeFreeDataHandle",
    "DdeGetLastError",
    "DdeCreateStringHandleA",
    "DdeCreateStringHandleW",
    "DdeCreateStringHandle",
    "DdeQueryStringA",
    "DdeQueryStringW",
    "DdeQueryString",
    "DdeFreeStringHandle",
    "DdeKeepStringHandle",
    "DdeCmpStringHandles",
    "SetWinMetaFileBits",
    "OpenClipboard",
    "CloseClipboard",
    "GetClipboardSequenceNumber",
    "GetClipboardOwner",
    "SetClipboardViewer",
    "GetClipboardViewer",
    "ChangeClipboardChain",
    "SetClipboardData",
    "GetClipboardData",
    "RegisterClipboardFormatA",
    "RegisterClipboardFormatW",
    "RegisterClipboardFormat",
    "CountClipboardFormats",
    "EnumClipboardFormats",
    "GetClipboardFormatNameA",
    "GetClipboardFormatNameW",
    "GetClipboardFormatName",
    "EmptyClipboard",
    "IsClipboardFormatAvailable",
    "GetPriorityClipboardFormat",
    "GetOpenClipboardWindow",
    "AddClipboardFormatListener",
    "RemoveClipboardFormatListener",
    "GetUpdatedClipboardFormats",
    "GlobalDeleteAtom",
    "InitAtomTable",
    "DeleteAtom",
    "GlobalAddAtomA",
    "GlobalAddAtomW",
    "GlobalAddAtom",
    "GlobalAddAtomExA",
    "GlobalAddAtomExW",
    "GlobalAddAtomEx",
    "GlobalFindAtomA",
    "GlobalFindAtomW",
    "GlobalFindAtom",
    "GlobalGetAtomNameA",
    "GlobalGetAtomNameW",
    "GlobalGetAtomName",
    "AddAtomA",
    "AddAtomW",
    "AddAtom",
    "FindAtomA",
    "FindAtomW",
    "FindAtom",
    "GetAtomNameA",
    "GetAtomNameW",
    "GetAtomName",
]
