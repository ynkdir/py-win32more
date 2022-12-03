from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.NetworkManagement.NetBios
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
def _define_ACTION_HEADER_head():
    class ACTION_HEADER(Structure):
        pass
    return ACTION_HEADER
def _define_ACTION_HEADER():
    ACTION_HEADER = win32more.NetworkManagement.NetBios.ACTION_HEADER_head
    ACTION_HEADER._fields_ = [
        ('transport_id', UInt32),
        ('action_code', UInt16),
        ('reserved', UInt16),
    ]
    return ACTION_HEADER
def _define_ADAPTER_STATUS_head():
    class ADAPTER_STATUS(Structure):
        pass
    return ADAPTER_STATUS
def _define_ADAPTER_STATUS():
    ADAPTER_STATUS = win32more.NetworkManagement.NetBios.ADAPTER_STATUS_head
    ADAPTER_STATUS._fields_ = [
        ('adapter_address', Byte * 6),
        ('rev_major', Byte),
        ('reserved0', Byte),
        ('adapter_type', Byte),
        ('rev_minor', Byte),
        ('duration', UInt16),
        ('frmr_recv', UInt16),
        ('frmr_xmit', UInt16),
        ('iframe_recv_err', UInt16),
        ('xmit_aborts', UInt16),
        ('xmit_success', UInt32),
        ('recv_success', UInt32),
        ('iframe_xmit_err', UInt16),
        ('recv_buff_unavail', UInt16),
        ('t1_timeouts', UInt16),
        ('ti_timeouts', UInt16),
        ('reserved1', UInt32),
        ('free_ncbs', UInt16),
        ('max_cfg_ncbs', UInt16),
        ('max_ncbs', UInt16),
        ('xmit_buf_unavail', UInt16),
        ('max_dgram_size', UInt16),
        ('pending_sess', UInt16),
        ('max_cfg_sess', UInt16),
        ('max_sess', UInt16),
        ('max_sess_pkt_size', UInt16),
        ('name_count', UInt16),
    ]
    return ADAPTER_STATUS
NCBNAMSZ = 16
MAX_LANA = 254
NAME_FLAGS_MASK = 135
GROUP_NAME = 128
UNIQUE_NAME = 0
REGISTERING = 0
REGISTERED = 4
DEREGISTERED = 5
DUPLICATE = 6
DUPLICATE_DEREG = 7
LISTEN_OUTSTANDING = 1
CALL_PENDING = 2
SESSION_ESTABLISHED = 3
HANGUP_PENDING = 4
HANGUP_COMPLETE = 5
SESSION_ABORTED = 6
ALL_TRANSPORTS = 'M\x00\x00\x00'
MS_NBF = 'MNBF'
NCBCALL = 16
NCBLISTEN = 17
NCBHANGUP = 18
NCBSEND = 20
NCBRECV = 21
NCBRECVANY = 22
NCBCHAINSEND = 23
NCBDGSEND = 32
NCBDGRECV = 33
NCBDGSENDBC = 34
NCBDGRECVBC = 35
NCBADDNAME = 48
NCBDELNAME = 49
NCBRESET = 50
NCBASTAT = 51
NCBSSTAT = 52
NCBCANCEL = 53
NCBADDGRNAME = 54
NCBENUM = 55
NCBUNLINK = 112
NCBSENDNA = 113
NCBCHAINSENDNA = 114
NCBLANSTALERT = 115
NCBACTION = 119
NCBFINDNAME = 120
NCBTRACE = 121
ASYNCH = 128
NRC_GOODRET = 0
NRC_BUFLEN = 1
NRC_ILLCMD = 3
NRC_CMDTMO = 5
NRC_INCOMP = 6
NRC_BADDR = 7
NRC_SNUMOUT = 8
NRC_NORES = 9
NRC_SCLOSED = 10
NRC_CMDCAN = 11
NRC_DUPNAME = 13
NRC_NAMTFUL = 14
NRC_ACTSES = 15
NRC_LOCTFUL = 17
NRC_REMTFUL = 18
NRC_ILLNN = 19
NRC_NOCALL = 20
NRC_NOWILD = 21
NRC_INUSE = 22
NRC_NAMERR = 23
NRC_SABORT = 24
NRC_NAMCONF = 25
NRC_IFBUSY = 33
NRC_TOOMANY = 34
NRC_BRIDGE = 35
NRC_CANOCCR = 36
NRC_CANCEL = 38
NRC_DUPENV = 48
NRC_ENVNOTDEF = 52
NRC_OSRESNOTAV = 53
NRC_MAXAPPS = 54
NRC_NOSAPS = 55
NRC_NORESOURCES = 56
NRC_INVADDRESS = 57
NRC_INVDDID = 59
NRC_LOCKFAIL = 60
NRC_OPENERR = 63
NRC_SYSTEM = 64
NRC_PENDING = 255
def _define_Netbios():
    try:
        return WINFUNCTYPE(Byte,POINTER(win32more.NetworkManagement.NetBios.NCB_head))(('Netbios', windll['NETAPI32.dll']), ((1, 'pncb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FIND_NAME_BUFFER_head():
    class FIND_NAME_BUFFER(Structure):
        pass
    return FIND_NAME_BUFFER
def _define_FIND_NAME_BUFFER():
    FIND_NAME_BUFFER = win32more.NetworkManagement.NetBios.FIND_NAME_BUFFER_head
    FIND_NAME_BUFFER._fields_ = [
        ('length', Byte),
        ('access_control', Byte),
        ('frame_control', Byte),
        ('destination_addr', Byte * 6),
        ('source_addr', Byte * 6),
        ('routing_info', Byte * 18),
    ]
    return FIND_NAME_BUFFER
def _define_FIND_NAME_HEADER_head():
    class FIND_NAME_HEADER(Structure):
        pass
    return FIND_NAME_HEADER
def _define_FIND_NAME_HEADER():
    FIND_NAME_HEADER = win32more.NetworkManagement.NetBios.FIND_NAME_HEADER_head
    FIND_NAME_HEADER._fields_ = [
        ('node_count', UInt16),
        ('reserved', Byte),
        ('unique_group', Byte),
    ]
    return FIND_NAME_HEADER
def _define_LANA_ENUM_head():
    class LANA_ENUM(Structure):
        pass
    return LANA_ENUM
def _define_LANA_ENUM():
    LANA_ENUM = win32more.NetworkManagement.NetBios.LANA_ENUM_head
    LANA_ENUM._fields_ = [
        ('length', Byte),
        ('lana', Byte * 255),
    ]
    return LANA_ENUM
def _define_NAME_BUFFER_head():
    class NAME_BUFFER(Structure):
        pass
    return NAME_BUFFER
def _define_NAME_BUFFER():
    NAME_BUFFER = win32more.NetworkManagement.NetBios.NAME_BUFFER_head
    NAME_BUFFER._fields_ = [
        ('name', Byte * 16),
        ('name_num', Byte),
        ('name_flags', Byte),
    ]
    return NAME_BUFFER
def _define_NCB_head():
    class NCB(Structure):
        pass
    return NCB
def _define_NCB():
    NCB = win32more.NetworkManagement.NetBios.NCB_head
    NCB._fields_ = [
        ('ncb_command', Byte),
        ('ncb_retcode', Byte),
        ('ncb_lsn', Byte),
        ('ncb_num', Byte),
        ('ncb_buffer', c_char_p_no),
        ('ncb_length', UInt16),
        ('ncb_callname', Byte * 16),
        ('ncb_name', Byte * 16),
        ('ncb_rto', Byte),
        ('ncb_sto', Byte),
        ('ncb_post', IntPtr),
        ('ncb_lana_num', Byte),
        ('ncb_cmd_cplt', Byte),
        ('ncb_reserve', Byte * 18),
        ('ncb_event', win32more.Foundation.HANDLE),
    ]
    return NCB
def _define_SESSION_BUFFER_head():
    class SESSION_BUFFER(Structure):
        pass
    return SESSION_BUFFER
def _define_SESSION_BUFFER():
    SESSION_BUFFER = win32more.NetworkManagement.NetBios.SESSION_BUFFER_head
    SESSION_BUFFER._fields_ = [
        ('lsn', Byte),
        ('state', Byte),
        ('local_name', Byte * 16),
        ('remote_name', Byte * 16),
        ('rcvs_outstanding', Byte),
        ('sends_outstanding', Byte),
    ]
    return SESSION_BUFFER
def _define_SESSION_HEADER_head():
    class SESSION_HEADER(Structure):
        pass
    return SESSION_HEADER
def _define_SESSION_HEADER():
    SESSION_HEADER = win32more.NetworkManagement.NetBios.SESSION_HEADER_head
    SESSION_HEADER._fields_ = [
        ('sess_name', Byte),
        ('num_sess', Byte),
        ('rcv_dg_outstanding', Byte),
        ('rcv_any_outstanding', Byte),
    ]
    return SESSION_HEADER
__all__ = [
    "ACTION_HEADER",
    "ADAPTER_STATUS",
    "ALL_TRANSPORTS",
    "ASYNCH",
    "CALL_PENDING",
    "DEREGISTERED",
    "DUPLICATE",
    "DUPLICATE_DEREG",
    "FIND_NAME_BUFFER",
    "FIND_NAME_HEADER",
    "GROUP_NAME",
    "HANGUP_COMPLETE",
    "HANGUP_PENDING",
    "LANA_ENUM",
    "LISTEN_OUTSTANDING",
    "MAX_LANA",
    "MS_NBF",
    "NAME_BUFFER",
    "NAME_FLAGS_MASK",
    "NCB",
    "NCBACTION",
    "NCBADDGRNAME",
    "NCBADDNAME",
    "NCBASTAT",
    "NCBCALL",
    "NCBCANCEL",
    "NCBCHAINSEND",
    "NCBCHAINSENDNA",
    "NCBDELNAME",
    "NCBDGRECV",
    "NCBDGRECVBC",
    "NCBDGSEND",
    "NCBDGSENDBC",
    "NCBENUM",
    "NCBFINDNAME",
    "NCBHANGUP",
    "NCBLANSTALERT",
    "NCBLISTEN",
    "NCBNAMSZ",
    "NCBRECV",
    "NCBRECVANY",
    "NCBRESET",
    "NCBSEND",
    "NCBSENDNA",
    "NCBSSTAT",
    "NCBTRACE",
    "NCBUNLINK",
    "NRC_ACTSES",
    "NRC_BADDR",
    "NRC_BRIDGE",
    "NRC_BUFLEN",
    "NRC_CANCEL",
    "NRC_CANOCCR",
    "NRC_CMDCAN",
    "NRC_CMDTMO",
    "NRC_DUPENV",
    "NRC_DUPNAME",
    "NRC_ENVNOTDEF",
    "NRC_GOODRET",
    "NRC_IFBUSY",
    "NRC_ILLCMD",
    "NRC_ILLNN",
    "NRC_INCOMP",
    "NRC_INUSE",
    "NRC_INVADDRESS",
    "NRC_INVDDID",
    "NRC_LOCKFAIL",
    "NRC_LOCTFUL",
    "NRC_MAXAPPS",
    "NRC_NAMCONF",
    "NRC_NAMERR",
    "NRC_NAMTFUL",
    "NRC_NOCALL",
    "NRC_NORES",
    "NRC_NORESOURCES",
    "NRC_NOSAPS",
    "NRC_NOWILD",
    "NRC_OPENERR",
    "NRC_OSRESNOTAV",
    "NRC_PENDING",
    "NRC_REMTFUL",
    "NRC_SABORT",
    "NRC_SCLOSED",
    "NRC_SNUMOUT",
    "NRC_SYSTEM",
    "NRC_TOOMANY",
    "Netbios",
    "REGISTERED",
    "REGISTERING",
    "SESSION_ABORTED",
    "SESSION_BUFFER",
    "SESSION_ESTABLISHED",
    "SESSION_HEADER",
    "UNIQUE_NAME",
]
