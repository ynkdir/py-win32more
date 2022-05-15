from win32more import *
import win32more.NetworkManagement.NetBios
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.NetworkManagement.NetBios, name, globals()[f"_define_{name}"]())
    return getattr(win32more.NetworkManagement.NetBios, name)
def __dir__():
    return __all__
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
def _define_NCB_head():
    class NCB(Structure):
        pass
    return NCB
def _define_NCB():
    NCB = win32more.NetworkManagement.NetBios.NCB_head
    NCB._fields_ = [
        ("ncb_command", Byte),
        ("ncb_retcode", Byte),
        ("ncb_lsn", Byte),
        ("ncb_num", Byte),
        ("ncb_buffer", c_char_p_no),
        ("ncb_length", UInt16),
        ("ncb_callname", Byte * 16),
        ("ncb_name", Byte * 16),
        ("ncb_rto", Byte),
        ("ncb_sto", Byte),
        ("ncb_post", IntPtr),
        ("ncb_lana_num", Byte),
        ("ncb_cmd_cplt", Byte),
        ("ncb_reserve", Byte * 18),
        ("ncb_event", win32more.Foundation.HANDLE),
    ]
    return NCB
def _define_ADAPTER_STATUS_head():
    class ADAPTER_STATUS(Structure):
        pass
    return ADAPTER_STATUS
def _define_ADAPTER_STATUS():
    ADAPTER_STATUS = win32more.NetworkManagement.NetBios.ADAPTER_STATUS_head
    ADAPTER_STATUS._fields_ = [
        ("adapter_address", Byte * 6),
        ("rev_major", Byte),
        ("reserved0", Byte),
        ("adapter_type", Byte),
        ("rev_minor", Byte),
        ("duration", UInt16),
        ("frmr_recv", UInt16),
        ("frmr_xmit", UInt16),
        ("iframe_recv_err", UInt16),
        ("xmit_aborts", UInt16),
        ("xmit_success", UInt32),
        ("recv_success", UInt32),
        ("iframe_xmit_err", UInt16),
        ("recv_buff_unavail", UInt16),
        ("t1_timeouts", UInt16),
        ("ti_timeouts", UInt16),
        ("reserved1", UInt32),
        ("free_ncbs", UInt16),
        ("max_cfg_ncbs", UInt16),
        ("max_ncbs", UInt16),
        ("xmit_buf_unavail", UInt16),
        ("max_dgram_size", UInt16),
        ("pending_sess", UInt16),
        ("max_cfg_sess", UInt16),
        ("max_sess", UInt16),
        ("max_sess_pkt_size", UInt16),
        ("name_count", UInt16),
    ]
    return ADAPTER_STATUS
def _define_NAME_BUFFER_head():
    class NAME_BUFFER(Structure):
        pass
    return NAME_BUFFER
def _define_NAME_BUFFER():
    NAME_BUFFER = win32more.NetworkManagement.NetBios.NAME_BUFFER_head
    NAME_BUFFER._fields_ = [
        ("name", Byte * 16),
        ("name_num", Byte),
        ("name_flags", Byte),
    ]
    return NAME_BUFFER
def _define_SESSION_HEADER_head():
    class SESSION_HEADER(Structure):
        pass
    return SESSION_HEADER
def _define_SESSION_HEADER():
    SESSION_HEADER = win32more.NetworkManagement.NetBios.SESSION_HEADER_head
    SESSION_HEADER._fields_ = [
        ("sess_name", Byte),
        ("num_sess", Byte),
        ("rcv_dg_outstanding", Byte),
        ("rcv_any_outstanding", Byte),
    ]
    return SESSION_HEADER
def _define_SESSION_BUFFER_head():
    class SESSION_BUFFER(Structure):
        pass
    return SESSION_BUFFER
def _define_SESSION_BUFFER():
    SESSION_BUFFER = win32more.NetworkManagement.NetBios.SESSION_BUFFER_head
    SESSION_BUFFER._fields_ = [
        ("lsn", Byte),
        ("state", Byte),
        ("local_name", Byte * 16),
        ("remote_name", Byte * 16),
        ("rcvs_outstanding", Byte),
        ("sends_outstanding", Byte),
    ]
    return SESSION_BUFFER
def _define_LANA_ENUM_head():
    class LANA_ENUM(Structure):
        pass
    return LANA_ENUM
def _define_LANA_ENUM():
    LANA_ENUM = win32more.NetworkManagement.NetBios.LANA_ENUM_head
    LANA_ENUM._fields_ = [
        ("length", Byte),
        ("lana", Byte * 255),
    ]
    return LANA_ENUM
def _define_FIND_NAME_HEADER_head():
    class FIND_NAME_HEADER(Structure):
        pass
    return FIND_NAME_HEADER
def _define_FIND_NAME_HEADER():
    FIND_NAME_HEADER = win32more.NetworkManagement.NetBios.FIND_NAME_HEADER_head
    FIND_NAME_HEADER._fields_ = [
        ("node_count", UInt16),
        ("reserved", Byte),
        ("unique_group", Byte),
    ]
    return FIND_NAME_HEADER
def _define_FIND_NAME_BUFFER_head():
    class FIND_NAME_BUFFER(Structure):
        pass
    return FIND_NAME_BUFFER
def _define_FIND_NAME_BUFFER():
    FIND_NAME_BUFFER = win32more.NetworkManagement.NetBios.FIND_NAME_BUFFER_head
    FIND_NAME_BUFFER._fields_ = [
        ("length", Byte),
        ("access_control", Byte),
        ("frame_control", Byte),
        ("destination_addr", Byte * 6),
        ("source_addr", Byte * 6),
        ("routing_info", Byte * 18),
    ]
    return FIND_NAME_BUFFER
def _define_ACTION_HEADER_head():
    class ACTION_HEADER(Structure):
        pass
    return ACTION_HEADER
def _define_ACTION_HEADER():
    ACTION_HEADER = win32more.NetworkManagement.NetBios.ACTION_HEADER_head
    ACTION_HEADER._fields_ = [
        ("transport_id", UInt32),
        ("action_code", UInt16),
        ("reserved", UInt16),
    ]
    return ACTION_HEADER
def _define_Netbios():
    try:
        return WINFUNCTYPE(Byte,POINTER(win32more.NetworkManagement.NetBios.NCB_head), use_last_error=False)(("Netbios", windll["NETAPI32"]), ((1, 'pncb'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NCBNAMSZ",
    "MAX_LANA",
    "NAME_FLAGS_MASK",
    "GROUP_NAME",
    "UNIQUE_NAME",
    "REGISTERING",
    "REGISTERED",
    "DEREGISTERED",
    "DUPLICATE",
    "DUPLICATE_DEREG",
    "LISTEN_OUTSTANDING",
    "CALL_PENDING",
    "SESSION_ESTABLISHED",
    "HANGUP_PENDING",
    "HANGUP_COMPLETE",
    "SESSION_ABORTED",
    "NCBCALL",
    "NCBLISTEN",
    "NCBHANGUP",
    "NCBSEND",
    "NCBRECV",
    "NCBRECVANY",
    "NCBCHAINSEND",
    "NCBDGSEND",
    "NCBDGRECV",
    "NCBDGSENDBC",
    "NCBDGRECVBC",
    "NCBADDNAME",
    "NCBDELNAME",
    "NCBRESET",
    "NCBASTAT",
    "NCBSSTAT",
    "NCBCANCEL",
    "NCBADDGRNAME",
    "NCBENUM",
    "NCBUNLINK",
    "NCBSENDNA",
    "NCBCHAINSENDNA",
    "NCBLANSTALERT",
    "NCBACTION",
    "NCBFINDNAME",
    "NCBTRACE",
    "ASYNCH",
    "NRC_GOODRET",
    "NRC_BUFLEN",
    "NRC_ILLCMD",
    "NRC_CMDTMO",
    "NRC_INCOMP",
    "NRC_BADDR",
    "NRC_SNUMOUT",
    "NRC_NORES",
    "NRC_SCLOSED",
    "NRC_CMDCAN",
    "NRC_DUPNAME",
    "NRC_NAMTFUL",
    "NRC_ACTSES",
    "NRC_LOCTFUL",
    "NRC_REMTFUL",
    "NRC_ILLNN",
    "NRC_NOCALL",
    "NRC_NOWILD",
    "NRC_INUSE",
    "NRC_NAMERR",
    "NRC_SABORT",
    "NRC_NAMCONF",
    "NRC_IFBUSY",
    "NRC_TOOMANY",
    "NRC_BRIDGE",
    "NRC_CANOCCR",
    "NRC_CANCEL",
    "NRC_DUPENV",
    "NRC_ENVNOTDEF",
    "NRC_OSRESNOTAV",
    "NRC_MAXAPPS",
    "NRC_NOSAPS",
    "NRC_NORESOURCES",
    "NRC_INVADDRESS",
    "NRC_INVDDID",
    "NRC_LOCKFAIL",
    "NRC_OPENERR",
    "NRC_SYSTEM",
    "NRC_PENDING",
    "NCB",
    "ADAPTER_STATUS",
    "NAME_BUFFER",
    "SESSION_HEADER",
    "SESSION_BUFFER",
    "LANA_ENUM",
    "FIND_NAME_HEADER",
    "FIND_NAME_BUFFER",
    "ACTION_HEADER",
    "Netbios",
]
