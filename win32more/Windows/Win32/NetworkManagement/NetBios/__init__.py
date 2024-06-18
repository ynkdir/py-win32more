from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.NetBios
class ACTION_HEADER(Structure):
    transport_id: UInt32
    action_code: UInt16
    reserved: UInt16
class ADAPTER_STATUS(Structure):
    adapter_address: Byte * 6
    rev_major: Byte
    reserved0: Byte
    adapter_type: Byte
    rev_minor: Byte
    duration: UInt16
    frmr_recv: UInt16
    frmr_xmit: UInt16
    iframe_recv_err: UInt16
    xmit_aborts: UInt16
    xmit_success: UInt32
    recv_success: UInt32
    iframe_xmit_err: UInt16
    recv_buff_unavail: UInt16
    t1_timeouts: UInt16
    ti_timeouts: UInt16
    reserved1: UInt32
    free_ncbs: UInt16
    max_cfg_ncbs: UInt16
    max_ncbs: UInt16
    xmit_buf_unavail: UInt16
    max_dgram_size: UInt16
    pending_sess: UInt16
    max_cfg_sess: UInt16
    max_sess: UInt16
    max_sess_pkt_size: UInt16
    name_count: UInt16
NCBNAMSZ: UInt32 = 16
MAX_LANA: UInt32 = 254
NAME_FLAGS_MASK: UInt32 = 135
GROUP_NAME: UInt32 = 128
UNIQUE_NAME: UInt32 = 0
REGISTERING: UInt32 = 0
REGISTERED: UInt32 = 4
DEREGISTERED: UInt32 = 5
DUPLICATE: UInt32 = 6
DUPLICATE_DEREG: UInt32 = 7
LISTEN_OUTSTANDING: UInt32 = 1
CALL_PENDING: UInt32 = 2
SESSION_ESTABLISHED: UInt32 = 3
HANGUP_PENDING: UInt32 = 4
HANGUP_COMPLETE: UInt32 = 5
SESSION_ABORTED: UInt32 = 6
ALL_TRANSPORTS: String = 'M\x00\x00\x00'
MS_NBF: String = 'MNBF'
NCBCALL: UInt32 = 16
NCBLISTEN: UInt32 = 17
NCBHANGUP: UInt32 = 18
NCBSEND: UInt32 = 20
NCBRECV: UInt32 = 21
NCBRECVANY: UInt32 = 22
NCBCHAINSEND: UInt32 = 23
NCBDGSEND: UInt32 = 32
NCBDGRECV: UInt32 = 33
NCBDGSENDBC: UInt32 = 34
NCBDGRECVBC: UInt32 = 35
NCBADDNAME: UInt32 = 48
NCBDELNAME: UInt32 = 49
NCBRESET: UInt32 = 50
NCBASTAT: UInt32 = 51
NCBSSTAT: UInt32 = 52
NCBCANCEL: UInt32 = 53
NCBADDGRNAME: UInt32 = 54
NCBENUM: UInt32 = 55
NCBUNLINK: UInt32 = 112
NCBSENDNA: UInt32 = 113
NCBCHAINSENDNA: UInt32 = 114
NCBLANSTALERT: UInt32 = 115
NCBACTION: UInt32 = 119
NCBFINDNAME: UInt32 = 120
NCBTRACE: UInt32 = 121
ASYNCH: UInt32 = 128
NRC_GOODRET: UInt32 = 0
NRC_BUFLEN: UInt32 = 1
NRC_ILLCMD: UInt32 = 3
NRC_CMDTMO: UInt32 = 5
NRC_INCOMP: UInt32 = 6
NRC_BADDR: UInt32 = 7
NRC_SNUMOUT: UInt32 = 8
NRC_NORES: UInt32 = 9
NRC_SCLOSED: UInt32 = 10
NRC_CMDCAN: UInt32 = 11
NRC_DUPNAME: UInt32 = 13
NRC_NAMTFUL: UInt32 = 14
NRC_ACTSES: UInt32 = 15
NRC_LOCTFUL: UInt32 = 17
NRC_REMTFUL: UInt32 = 18
NRC_ILLNN: UInt32 = 19
NRC_NOCALL: UInt32 = 20
NRC_NOWILD: UInt32 = 21
NRC_INUSE: UInt32 = 22
NRC_NAMERR: UInt32 = 23
NRC_SABORT: UInt32 = 24
NRC_NAMCONF: UInt32 = 25
NRC_IFBUSY: UInt32 = 33
NRC_TOOMANY: UInt32 = 34
NRC_BRIDGE: UInt32 = 35
NRC_CANOCCR: UInt32 = 36
NRC_CANCEL: UInt32 = 38
NRC_DUPENV: UInt32 = 48
NRC_ENVNOTDEF: UInt32 = 52
NRC_OSRESNOTAV: UInt32 = 53
NRC_MAXAPPS: UInt32 = 54
NRC_NOSAPS: UInt32 = 55
NRC_NORESOURCES: UInt32 = 56
NRC_INVADDRESS: UInt32 = 57
NRC_INVDDID: UInt32 = 59
NRC_LOCKFAIL: UInt32 = 60
NRC_OPENERR: UInt32 = 63
NRC_SYSTEM: UInt32 = 64
NRC_PENDING: UInt32 = 255
@winfunctype('NETAPI32.dll')
def Netbios(pncb: POINTER(win32more.Windows.Win32.NetworkManagement.NetBios.NCB)) -> Byte: ...
class FIND_NAME_BUFFER(Structure):
    length: Byte
    access_control: Byte
    frame_control: Byte
    destination_addr: Byte * 6
    source_addr: Byte * 6
    routing_info: Byte * 18
class FIND_NAME_HEADER(Structure):
    node_count: UInt16
    reserved: Byte
    unique_group: Byte
class LANA_ENUM(Structure):
    length: Byte
    lana: Byte * 255
class NAME_BUFFER(Structure):
    name: Byte * 16
    name_num: Byte
    name_flags: Byte
if ARCH in 'X64,ARM64':
    class NCB(Structure):
        ncb_command: Byte
        ncb_retcode: Byte
        ncb_lsn: Byte
        ncb_num: Byte
        ncb_buffer: POINTER(Byte)
        ncb_length: UInt16
        ncb_callname: Byte * 16
        ncb_name: Byte * 16
        ncb_rto: Byte
        ncb_sto: Byte
        ncb_post: IntPtr
        ncb_lana_num: Byte
        ncb_cmd_cplt: Byte
        ncb_reserve: Byte * 18
        ncb_event: win32more.Windows.Win32.Foundation.HANDLE
elif ARCH in 'X86':
    class NCB(Structure):
        ncb_command: Byte
        ncb_retcode: Byte
        ncb_lsn: Byte
        ncb_num: Byte
        ncb_buffer: POINTER(Byte)
        ncb_length: UInt16
        ncb_callname: Byte * 16
        ncb_name: Byte * 16
        ncb_rto: Byte
        ncb_sto: Byte
        ncb_post: IntPtr
        ncb_lana_num: Byte
        ncb_cmd_cplt: Byte
        ncb_reserve: Byte * 10
        ncb_event: win32more.Windows.Win32.Foundation.HANDLE
class SESSION_BUFFER(Structure):
    lsn: Byte
    state: Byte
    local_name: Byte * 16
    remote_name: Byte * 16
    rcvs_outstanding: Byte
    sends_outstanding: Byte
class SESSION_HEADER(Structure):
    sess_name: Byte
    num_sess: Byte
    rcv_dg_outstanding: Byte
    rcv_any_outstanding: Byte


make_ready(__name__)
