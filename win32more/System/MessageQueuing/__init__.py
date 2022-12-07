from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.MessageQueuing
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class _DMSMQEventEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e078-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
PRLT: UInt32 = 0
PRLE: UInt32 = 1
PRGT: UInt32 = 2
PRGE: UInt32 = 3
PREQ: UInt32 = 4
PRNE: UInt32 = 5
QUERY_SORTASCEND: UInt32 = 0
QUERY_SORTDESCEND: UInt32 = 1
MQ_MOVE_ACCESS: UInt32 = 4
MQ_ACTION_RECEIVE: UInt32 = 0
MQ_ACTION_PEEK_CURRENT: UInt32 = 2147483648
MQ_ACTION_PEEK_NEXT: UInt32 = 2147483649
MQ_LOOKUP_PEEK_CURRENT: UInt32 = 1073741840
MQ_LOOKUP_PEEK_NEXT: UInt32 = 1073741841
MQ_LOOKUP_PEEK_PREV: UInt32 = 1073741842
MQ_LOOKUP_PEEK_FIRST: UInt32 = 1073741844
MQ_LOOKUP_PEEK_LAST: UInt32 = 1073741848
MQ_LOOKUP_RECEIVE_CURRENT: UInt32 = 1073741856
MQ_LOOKUP_RECEIVE_NEXT: UInt32 = 1073741857
MQ_LOOKUP_RECEIVE_PREV: UInt32 = 1073741858
MQ_LOOKUP_RECEIVE_FIRST: UInt32 = 1073741860
MQ_LOOKUP_RECEIVE_LAST: UInt32 = 1073741864
MQ_LOOKUP_RECEIVE_ALLOW_PEEK: UInt32 = 1073742112
PROPID_M_BASE: UInt32 = 0
PROPID_M_CLASS: UInt32 = 1
PROPID_M_MSGID: UInt32 = 2
PROPID_M_CORRELATIONID: UInt32 = 3
PROPID_M_PRIORITY: UInt32 = 4
PROPID_M_DELIVERY: UInt32 = 5
PROPID_M_ACKNOWLEDGE: UInt32 = 6
PROPID_M_JOURNAL: UInt32 = 7
PROPID_M_APPSPECIFIC: UInt32 = 8
PROPID_M_BODY: UInt32 = 9
PROPID_M_BODY_SIZE: UInt32 = 10
PROPID_M_LABEL: UInt32 = 11
PROPID_M_LABEL_LEN: UInt32 = 12
PROPID_M_TIME_TO_REACH_QUEUE: UInt32 = 13
PROPID_M_TIME_TO_BE_RECEIVED: UInt32 = 14
PROPID_M_RESP_QUEUE: UInt32 = 15
PROPID_M_RESP_QUEUE_LEN: UInt32 = 16
PROPID_M_ADMIN_QUEUE: UInt32 = 17
PROPID_M_ADMIN_QUEUE_LEN: UInt32 = 18
PROPID_M_VERSION: UInt32 = 19
PROPID_M_SENDERID: UInt32 = 20
PROPID_M_SENDERID_LEN: UInt32 = 21
PROPID_M_SENDERID_TYPE: UInt32 = 22
PROPID_M_PRIV_LEVEL: UInt32 = 23
PROPID_M_AUTH_LEVEL: UInt32 = 24
PROPID_M_AUTHENTICATED: UInt32 = 25
PROPID_M_HASH_ALG: UInt32 = 26
PROPID_M_ENCRYPTION_ALG: UInt32 = 27
PROPID_M_SENDER_CERT: UInt32 = 28
PROPID_M_SENDER_CERT_LEN: UInt32 = 29
PROPID_M_SRC_MACHINE_ID: UInt32 = 30
PROPID_M_SENTTIME: UInt32 = 31
PROPID_M_ARRIVEDTIME: UInt32 = 32
PROPID_M_DEST_QUEUE: UInt32 = 33
PROPID_M_DEST_QUEUE_LEN: UInt32 = 34
PROPID_M_EXTENSION: UInt32 = 35
PROPID_M_EXTENSION_LEN: UInt32 = 36
PROPID_M_SECURITY_CONTEXT: UInt32 = 37
PROPID_M_CONNECTOR_TYPE: UInt32 = 38
PROPID_M_XACT_STATUS_QUEUE: UInt32 = 39
PROPID_M_XACT_STATUS_QUEUE_LEN: UInt32 = 40
PROPID_M_TRACE: UInt32 = 41
PROPID_M_BODY_TYPE: UInt32 = 42
PROPID_M_DEST_SYMM_KEY: UInt32 = 43
PROPID_M_DEST_SYMM_KEY_LEN: UInt32 = 44
PROPID_M_SIGNATURE: UInt32 = 45
PROPID_M_SIGNATURE_LEN: UInt32 = 46
PROPID_M_PROV_TYPE: UInt32 = 47
PROPID_M_PROV_NAME: UInt32 = 48
PROPID_M_PROV_NAME_LEN: UInt32 = 49
PROPID_M_FIRST_IN_XACT: UInt32 = 50
PROPID_M_LAST_IN_XACT: UInt32 = 51
PROPID_M_XACTID: UInt32 = 52
PROPID_M_AUTHENTICATED_EX: UInt32 = 53
PROPID_M_RESP_FORMAT_NAME: UInt32 = 54
PROPID_M_RESP_FORMAT_NAME_LEN: UInt32 = 55
PROPID_M_DEST_FORMAT_NAME: UInt32 = 58
PROPID_M_DEST_FORMAT_NAME_LEN: UInt32 = 59
PROPID_M_LOOKUPID: UInt32 = 60
PROPID_M_SOAP_ENVELOPE: UInt32 = 61
PROPID_M_SOAP_ENVELOPE_LEN: UInt32 = 62
PROPID_M_COMPOUND_MESSAGE: UInt32 = 63
PROPID_M_COMPOUND_MESSAGE_SIZE: UInt32 = 64
PROPID_M_SOAP_HEADER: UInt32 = 65
PROPID_M_SOAP_BODY: UInt32 = 66
PROPID_M_DEADLETTER_QUEUE: UInt32 = 67
PROPID_M_DEADLETTER_QUEUE_LEN: UInt32 = 68
PROPID_M_ABORT_COUNT: UInt32 = 69
PROPID_M_MOVE_COUNT: UInt32 = 70
PROPID_M_LAST_MOVE_TIME: UInt32 = 75
PROPID_M_MSGID_SIZE: UInt32 = 20
PROPID_M_CORRELATIONID_SIZE: UInt32 = 20
PROPID_M_XACTID_SIZE: UInt32 = 20
MQMSG_PRIV_LEVEL_BODY_AES: UInt32 = 5
MQMSG_AUTHENTICATED_QM_MESSAGE: UInt32 = 11
MQMSG_NOT_FIRST_IN_XACT: UInt32 = 0
MQMSG_FIRST_IN_XACT: UInt32 = 1
MQMSG_NOT_LAST_IN_XACT: UInt32 = 0
MQMSG_LAST_IN_XACT: UInt32 = 1
PROPID_Q_BASE: UInt32 = 100
PROPID_Q_INSTANCE: UInt32 = 101
PROPID_Q_TYPE: UInt32 = 102
PROPID_Q_PATHNAME: UInt32 = 103
PROPID_Q_JOURNAL: UInt32 = 104
PROPID_Q_QUOTA: UInt32 = 105
PROPID_Q_BASEPRIORITY: UInt32 = 106
PROPID_Q_JOURNAL_QUOTA: UInt32 = 107
PROPID_Q_LABEL: UInt32 = 108
PROPID_Q_CREATE_TIME: UInt32 = 109
PROPID_Q_MODIFY_TIME: UInt32 = 110
PROPID_Q_AUTHENTICATE: UInt32 = 111
PROPID_Q_PRIV_LEVEL: UInt32 = 112
PROPID_Q_TRANSACTION: UInt32 = 113
PROPID_Q_PATHNAME_DNS: UInt32 = 124
PROPID_Q_MULTICAST_ADDRESS: UInt32 = 125
PROPID_Q_ADS_PATH: UInt32 = 126
PROPID_QM_BASE: UInt32 = 200
PROPID_QM_SITE_ID: UInt32 = 201
PROPID_QM_MACHINE_ID: UInt32 = 202
PROPID_QM_PATHNAME: UInt32 = 203
PROPID_QM_CONNECTION: UInt32 = 204
PROPID_QM_ENCRYPTION_PK: UInt32 = 205
PROPID_QM_ENCRYPTION_PK_BASE: UInt32 = 231
PROPID_QM_ENCRYPTION_PK_ENHANCED: UInt32 = 232
PROPID_QM_PATHNAME_DNS: UInt32 = 233
PROPID_QM_ENCRYPTION_PK_AES: UInt32 = 244
PROPID_PC_BASE: UInt32 = 5800
PROPID_PC_VERSION: UInt32 = 5801
PROPID_PC_DS_ENABLED: UInt32 = 5802
PROPID_MGMT_MSMQ_BASE: UInt32 = 0
PROPID_MGMT_MSMQ_ACTIVEQUEUES: UInt32 = 1
PROPID_MGMT_MSMQ_PRIVATEQ: UInt32 = 2
PROPID_MGMT_MSMQ_DSSERVER: UInt32 = 3
PROPID_MGMT_MSMQ_CONNECTED: UInt32 = 4
PROPID_MGMT_MSMQ_TYPE: UInt32 = 5
PROPID_MGMT_MSMQ_BYTES_IN_ALL_QUEUES: UInt32 = 6
MSMQ_CONNECTED: String = 'CONNECTED'
MSMQ_DISCONNECTED: String = 'DISCONNECTED'
PROPID_MGMT_QUEUE_BASE: UInt32 = 0
PROPID_MGMT_QUEUE_PATHNAME: UInt32 = 1
PROPID_MGMT_QUEUE_FORMATNAME: UInt32 = 2
PROPID_MGMT_QUEUE_TYPE: UInt32 = 3
PROPID_MGMT_QUEUE_LOCATION: UInt32 = 4
PROPID_MGMT_QUEUE_XACT: UInt32 = 5
PROPID_MGMT_QUEUE_FOREIGN: UInt32 = 6
PROPID_MGMT_QUEUE_MESSAGE_COUNT: UInt32 = 7
PROPID_MGMT_QUEUE_BYTES_IN_QUEUE: UInt32 = 8
PROPID_MGMT_QUEUE_JOURNAL_MESSAGE_COUNT: UInt32 = 9
PROPID_MGMT_QUEUE_BYTES_IN_JOURNAL: UInt32 = 10
PROPID_MGMT_QUEUE_STATE: UInt32 = 11
PROPID_MGMT_QUEUE_NEXTHOPS: UInt32 = 12
PROPID_MGMT_QUEUE_EOD_LAST_ACK: UInt32 = 13
PROPID_MGMT_QUEUE_EOD_LAST_ACK_TIME: UInt32 = 14
PROPID_MGMT_QUEUE_EOD_LAST_ACK_COUNT: UInt32 = 15
PROPID_MGMT_QUEUE_EOD_FIRST_NON_ACK: UInt32 = 16
PROPID_MGMT_QUEUE_EOD_LAST_NON_ACK: UInt32 = 17
PROPID_MGMT_QUEUE_EOD_NEXT_SEQ: UInt32 = 18
PROPID_MGMT_QUEUE_EOD_NO_READ_COUNT: UInt32 = 19
PROPID_MGMT_QUEUE_EOD_NO_ACK_COUNT: UInt32 = 20
PROPID_MGMT_QUEUE_EOD_RESEND_TIME: UInt32 = 21
PROPID_MGMT_QUEUE_EOD_RESEND_INTERVAL: UInt32 = 22
PROPID_MGMT_QUEUE_EOD_RESEND_COUNT: UInt32 = 23
PROPID_MGMT_QUEUE_EOD_SOURCE_INFO: UInt32 = 24
PROPID_MGMT_QUEUE_CONNECTION_HISTORY: UInt32 = 25
PROPID_MGMT_QUEUE_SUBQUEUE_COUNT: UInt32 = 26
PROPID_MGMT_QUEUE_SUBQUEUE_NAMES: UInt32 = 27
PROPID_MGMT_QUEUE_USED_QUOTA: UInt32 = 8
PROPID_MGMT_QUEUE_JOURNAL_USED_QUOTA: UInt32 = 10
MGMT_QUEUE_TYPE_PUBLIC: String = 'PUBLIC'
MGMT_QUEUE_TYPE_PRIVATE: String = 'PRIVATE'
MGMT_QUEUE_TYPE_MACHINE: String = 'MACHINE'
MGMT_QUEUE_TYPE_CONNECTOR: String = 'CONNECTOR'
MGMT_QUEUE_TYPE_MULTICAST: String = 'MULTICAST'
MGMT_QUEUE_STATE_LOCAL: String = 'LOCAL CONNECTION'
MGMT_QUEUE_STATE_NONACTIVE: String = 'INACTIVE'
MGMT_QUEUE_STATE_WAITING: String = 'WAITING'
MGMT_QUEUE_STATE_NEED_VALIDATE: String = 'NEED VALIDATION'
MGMT_QUEUE_STATE_ONHOLD: String = 'ONHOLD'
MGMT_QUEUE_STATE_CONNECTED: String = 'CONNECTED'
MGMT_QUEUE_STATE_DISCONNECTING: String = 'DISCONNECTING'
MGMT_QUEUE_STATE_DISCONNECTED: String = 'DISCONNECTED'
MGMT_QUEUE_STATE_LOCKED: String = 'LOCKED'
MGMT_QUEUE_LOCAL_LOCATION: String = 'LOCAL'
MGMT_QUEUE_REMOTE_LOCATION: String = 'REMOTE'
MGMT_QUEUE_UNKNOWN_TYPE: String = 'UNKNOWN'
MGMT_QUEUE_CORRECT_TYPE: String = 'YES'
MGMT_QUEUE_INCORRECT_TYPE: String = 'NO'
MGMT_QUEUE_TRANSACTIONAL_TYPE: String = 'YES'
MGMT_QUEUE_NOT_TRANSACTIONAL_TYPE: String = 'NO'
MGMT_QUEUE_FOREIGN_TYPE: String = 'YES'
MGMT_QUEUE_NOT_FOREIGN_TYPE: String = 'NO'
MO_MACHINE_TOKEN: String = 'MACHINE'
MO_QUEUE_TOKEN: String = 'QUEUE'
MACHINE_ACTION_CONNECT: String = 'CONNECT'
MACHINE_ACTION_DISCONNECT: String = 'DISCONNECT'
MACHINE_ACTION_TIDY: String = 'TIDY'
QUEUE_ACTION_PAUSE: String = 'PAUSE'
QUEUE_ACTION_RESUME: String = 'RESUME'
QUEUE_ACTION_EOD_RESEND: String = 'EOD_RESEND'
LONG_LIVED: UInt32 = 4294967294
MQSEC_DELETE_MESSAGE: UInt32 = 1
MQSEC_PEEK_MESSAGE: UInt32 = 2
MQSEC_WRITE_MESSAGE: UInt32 = 4
MQSEC_DELETE_JOURNAL_MESSAGE: UInt32 = 8
MQSEC_SET_QUEUE_PROPERTIES: UInt32 = 16
MQSEC_GET_QUEUE_PROPERTIES: UInt32 = 32
MQSEC_QUEUE_GENERIC_EXECUTE: UInt32 = 0
MQ_OK: win32more.Foundation.HRESULT = 0
MQ_ERROR_RESOLVE_ADDRESS: win32more.Foundation.HRESULT = -1072824167
MQ_ERROR_TOO_MANY_PROPERTIES: win32more.Foundation.HRESULT = -1072824166
MQ_ERROR_MESSAGE_NOT_AUTHENTICATED: win32more.Foundation.HRESULT = -1072824165
MQ_ERROR_MESSAGE_LOCKED_UNDER_TRANSACTION: win32more.Foundation.HRESULT = -1072824164
FOREIGN_STATUS = Int32
MQ_STATUS_FOREIGN: FOREIGN_STATUS = 0
MQ_STATUS_NOT_FOREIGN: FOREIGN_STATUS = 1
MQ_STATUS_UNKNOWN: FOREIGN_STATUS = 2
class IMSMQApplication(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e085-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def MachineIdOfMachineName(MachineName: win32more.Foundation.BSTR, pbstrGuid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IMSMQApplication2(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQApplication
    Guid = Guid('12a30900-7300-11d2-b0-e6-00-e0-2c-07-4f-6b')
    @commethod(8)
    def RegisterCertificate(Flags: POINTER(win32more.System.Com.VARIANT_head), ExternalCertificate: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def MachineNameOfMachineId(bstrGuid: win32more.Foundation.BSTR, pbstrMachineName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MSMQVersionMajor(psMSMQVersionMajor: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_MSMQVersionMinor(psMSMQVersionMinor: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_MSMQVersionBuild(psMSMQVersionBuild: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsDsEnabled(pfIsDsEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQApplication3(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQApplication2
    Guid = Guid('eba96b1f-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(15)
    def get_ActiveQueues(pvActiveQueues: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_PrivateQueues(pvPrivateQueues: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_DirectoryServiceServer(pbstrDirectoryServiceServer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_IsConnected(pfIsConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_BytesInAllQueues(pvBytesInAllQueues: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Machine(bstrMachine: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Machine(pbstrMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Connect() -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Disconnect() -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Tidy() -> win32more.Foundation.HRESULT: ...
class IMSMQCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0188ac2f-ecb3-4173-97-79-63-5c-a2-03-9c-72')
    @commethod(7)
    def Item(Index: POINTER(win32more.System.Com.VARIANT_head), pvarRet: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def _NewEnum(ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQCoordinatedTransactionDispenser(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e081-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQCoordinatedTransactionDispenser2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b10-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQCoordinatedTransactionDispenser3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b14-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQDestination(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b16-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def Open() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsOpen(pfIsOpen: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_IADs(ppIADs: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def putref_IADs(pIADs: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ADsPath(pbstrADsPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ADsPath(bstrADsPath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_PathName(pbstrPathName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_PathName(bstrPathName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_FormatName(bstrFormatName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Destinations(ppDestinations: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def putref_Destinations(pDestinations: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e077-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
class IMSMQEvent2(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQEvent
    Guid = Guid('eba96b12-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQEvent3(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQEvent2
    Guid = Guid('eba96b1c-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
class IMSMQManagement(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('be5f0241-e489-4957-8c-c4-a4-52-fc-f3-e2-3e')
    @commethod(7)
    def Init(Machine: POINTER(win32more.System.Com.VARIANT_head), Pathname: POINTER(win32more.System.Com.VARIANT_head), FormatName: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Machine(pbstrMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MessageCount(plMessageCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ForeignStatus(plForeignStatus: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_QueueType(plQueueType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsLocal(pfIsLocal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_TransactionalStatus(plTransactionalStatus: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_BytesInQueue(pvBytesInQueue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQMessage(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e074-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def get_Class(plClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_AuthLevel(plAuthLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_AuthLevel(lAuthLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsAuthenticated(pisAuthenticated: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Delivery(plDelivery: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Delivery(lDelivery: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Trace(plTrace: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Trace(lTrace: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Priority(plPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Priority(lPriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ResponseQueueInfo(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def putref_ResponseQueueInfo(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AppSpecific(plAppSpecific: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AppSpecific(lAppSpecific: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceMachineGuid(pbstrGuidSrcMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_BodyLength(pcbBody: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Body(pvarBody: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Body(varBody: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_AdminQueueInfo(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def putref_AdminQueueInfo(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Id(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CorrelationId(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CorrelationId(varMsgId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_Ack(plAck: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_Ack(lAck: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_MaxTimeToReachQueue(plMaxTimeToReachQueue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_MaxTimeToReachQueue(lMaxTimeToReachQueue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxTimeToReceive(plMaxTimeToReceive: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxTimeToReceive(lMaxTimeToReceive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_HashAlgorithm(plHashAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_HashAlgorithm(lHashAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_EncryptAlgorithm(plEncryptAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_EncryptAlgorithm(lEncryptAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_SentTime(pvarSentTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_ArrivedTime(plArrivedTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_DestinationQueueInfo(ppqinfoDest: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SenderCertificate(pvarSenderCert: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_SenderCertificate(varSenderCert: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_SenderId(pvarSenderId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_SenderIdType(plSenderIdType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def put_SenderIdType(lSenderIdType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def Send(DestinationQueue: win32more.System.MessageQueuing.IMSMQQueue_head, Transaction: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def AttachCurrentSecurityContext() -> win32more.Foundation.HRESULT: ...
class IMSMQMessage2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d9933be0-a567-11d2-b0-f3-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Class(plClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_AuthLevel(plAuthLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_AuthLevel(lAuthLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsAuthenticated(pisAuthenticated: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Delivery(plDelivery: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Delivery(lDelivery: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Trace(plTrace: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Trace(lTrace: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Priority(plPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Priority(lPriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ResponseQueueInfo_v1(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def putref_ResponseQueueInfo_v1(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AppSpecific(plAppSpecific: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AppSpecific(lAppSpecific: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceMachineGuid(pbstrGuidSrcMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_BodyLength(pcbBody: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Body(pvarBody: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Body(varBody: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_AdminQueueInfo_v1(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def putref_AdminQueueInfo_v1(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Id(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CorrelationId(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CorrelationId(varMsgId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_Ack(plAck: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_Ack(lAck: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_MaxTimeToReachQueue(plMaxTimeToReachQueue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_MaxTimeToReachQueue(lMaxTimeToReachQueue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxTimeToReceive(plMaxTimeToReceive: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxTimeToReceive(lMaxTimeToReceive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_HashAlgorithm(plHashAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_HashAlgorithm(lHashAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_EncryptAlgorithm(plEncryptAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_EncryptAlgorithm(lEncryptAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_SentTime(pvarSentTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_ArrivedTime(plArrivedTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_DestinationQueueInfo(ppqinfoDest: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SenderCertificate(pvarSenderCert: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_SenderCertificate(varSenderCert: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_SenderId(pvarSenderId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_SenderIdType(plSenderIdType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def put_SenderIdType(lSenderIdType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def Send(DestinationQueue: win32more.System.MessageQueuing.IMSMQQueue2_head, Transaction: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def AttachCurrentSecurityContext() -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def get_SenderVersion(plSenderVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_Extension(pvarExtension: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_Extension(varExtension: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ConnectorTypeGuid(pbstrGuidConnectorType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ConnectorTypeGuid(bstrGuidConnectorType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def get_TransactionStatusQueueInfo(ppqinfoXactStatus: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def get_DestinationSymmetricKey(pvarDestSymmKey: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def put_DestinationSymmetricKey(varDestSymmKey: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def get_Signature(pvarSignature: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def put_Signature(varSignature: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def get_AuthenticationProviderType(plAuthProvType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def put_AuthenticationProviderType(lAuthProvType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def get_AuthenticationProviderName(pbstrAuthProvName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def put_AuthenticationProviderName(bstrAuthProvName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_SenderId(varSenderId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_MsgClass(plMsgClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def put_MsgClass(lMsgClass: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_TransactionId(pvarXactId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def get_IsFirstInTransaction(pisFirstInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_IsLastInTransaction(pisLastInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def get_ResponseQueueInfo(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def putref_ResponseQueueInfo(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def get_AdminQueueInfo(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def putref_AdminQueueInfo(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def get_ReceivedAuthenticationLevel(psReceivedAuthenticationLevel: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
class IMSMQMessage3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b1a-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Class(plClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_AuthLevel(plAuthLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_AuthLevel(lAuthLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsAuthenticated(pisAuthenticated: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Delivery(plDelivery: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Delivery(lDelivery: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Trace(plTrace: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Trace(lTrace: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Priority(plPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Priority(lPriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ResponseQueueInfo_v1(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def putref_ResponseQueueInfo_v1(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AppSpecific(plAppSpecific: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AppSpecific(lAppSpecific: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceMachineGuid(pbstrGuidSrcMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_BodyLength(pcbBody: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Body(pvarBody: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Body(varBody: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_AdminQueueInfo_v1(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def putref_AdminQueueInfo_v1(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Id(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CorrelationId(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CorrelationId(varMsgId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_Ack(plAck: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_Ack(lAck: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_MaxTimeToReachQueue(plMaxTimeToReachQueue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_MaxTimeToReachQueue(lMaxTimeToReachQueue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxTimeToReceive(plMaxTimeToReceive: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxTimeToReceive(lMaxTimeToReceive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_HashAlgorithm(plHashAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_HashAlgorithm(lHashAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_EncryptAlgorithm(plEncryptAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_EncryptAlgorithm(lEncryptAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_SentTime(pvarSentTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_ArrivedTime(plArrivedTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_DestinationQueueInfo(ppqinfoDest: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SenderCertificate(pvarSenderCert: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_SenderCertificate(varSenderCert: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_SenderId(pvarSenderId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_SenderIdType(plSenderIdType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def put_SenderIdType(lSenderIdType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def Send(DestinationQueue: win32more.System.Com.IDispatch_head, Transaction: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def AttachCurrentSecurityContext() -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def get_SenderVersion(plSenderVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_Extension(pvarExtension: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_Extension(varExtension: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ConnectorTypeGuid(pbstrGuidConnectorType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ConnectorTypeGuid(bstrGuidConnectorType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def get_TransactionStatusQueueInfo(ppqinfoXactStatus: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def get_DestinationSymmetricKey(pvarDestSymmKey: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def put_DestinationSymmetricKey(varDestSymmKey: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def get_Signature(pvarSignature: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def put_Signature(varSignature: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def get_AuthenticationProviderType(plAuthProvType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def put_AuthenticationProviderType(lAuthProvType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def get_AuthenticationProviderName(pbstrAuthProvName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def put_AuthenticationProviderName(bstrAuthProvName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_SenderId(varSenderId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_MsgClass(plMsgClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def put_MsgClass(lMsgClass: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_TransactionId(pvarXactId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def get_IsFirstInTransaction(pisFirstInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_IsLastInTransaction(pisLastInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def get_ResponseQueueInfo_v2(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def putref_ResponseQueueInfo_v2(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def get_AdminQueueInfo_v2(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def putref_AdminQueueInfo_v2(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def get_ReceivedAuthenticationLevel(psReceivedAuthenticationLevel: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def get_ResponseQueueInfo(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def putref_ResponseQueueInfo(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo3_head) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def get_AdminQueueInfo(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def putref_AdminQueueInfo(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo3_head) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def get_ResponseDestination(ppdestResponse: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def putref_ResponseDestination(pdestResponse: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def get_Destination(ppdestDestination: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def get_LookupId(pvarLookupId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def get_IsAuthenticated2(pisAuthenticated: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def get_IsFirstInTransaction2(pisFirstInXact: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def get_IsLastInTransaction2(pisLastInXact: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def AttachCurrentSecurityContext2() -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def get_SoapEnvelope(pbstrSoapEnvelope: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def get_CompoundMessage(pvarCompoundMessage: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def put_SoapHeader(bstrSoapHeader: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def put_SoapBody(bstrSoapBody: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IMSMQMessage4(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b23-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Class(plClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_AuthLevel(plAuthLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_AuthLevel(lAuthLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsAuthenticated(pisAuthenticated: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Delivery(plDelivery: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Delivery(lDelivery: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Trace(plTrace: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Trace(lTrace: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Priority(plPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Priority(lPriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_ResponseQueueInfo_v1(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def putref_ResponseQueueInfo_v1(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AppSpecific(plAppSpecific: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AppSpecific(lAppSpecific: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SourceMachineGuid(pbstrGuidSrcMachine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_BodyLength(pcbBody: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Body(pvarBody: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Body(varBody: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_AdminQueueInfo_v1(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def putref_AdminQueueInfo_v1(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Id(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CorrelationId(pvarMsgId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def put_CorrelationId(varMsgId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_Ack(plAck: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def put_Ack(lAck: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_MaxTimeToReachQueue(plMaxTimeToReachQueue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def put_MaxTimeToReachQueue(lMaxTimeToReachQueue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MaxTimeToReceive(plMaxTimeToReceive: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def put_MaxTimeToReceive(lMaxTimeToReceive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_HashAlgorithm(plHashAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def put_HashAlgorithm(lHashAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_EncryptAlgorithm(plEncryptAlg: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def put_EncryptAlgorithm(lEncryptAlg: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_SentTime(pvarSentTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_ArrivedTime(plArrivedTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_DestinationQueueInfo(ppqinfoDest: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_SenderCertificate(pvarSenderCert: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_SenderCertificate(varSenderCert: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_SenderId(pvarSenderId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_SenderIdType(plSenderIdType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def put_SenderIdType(lSenderIdType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def Send(DestinationQueue: win32more.System.Com.IDispatch_head, Transaction: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def AttachCurrentSecurityContext() -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def get_SenderVersion(plSenderVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_Extension(pvarExtension: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_Extension(varExtension: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_ConnectorTypeGuid(pbstrGuidConnectorType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_ConnectorTypeGuid(bstrGuidConnectorType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def get_TransactionStatusQueueInfo(ppqinfoXactStatus: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def get_DestinationSymmetricKey(pvarDestSymmKey: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def put_DestinationSymmetricKey(varDestSymmKey: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def get_Signature(pvarSignature: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def put_Signature(varSignature: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def get_AuthenticationProviderType(plAuthProvType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def put_AuthenticationProviderType(lAuthProvType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def get_AuthenticationProviderName(pbstrAuthProvName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def put_AuthenticationProviderName(bstrAuthProvName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def put_SenderId(varSenderId: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def get_MsgClass(plMsgClass: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def put_MsgClass(lMsgClass: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def get_TransactionId(pvarXactId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def get_IsFirstInTransaction(pisFirstInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def get_IsLastInTransaction(pisLastInXact: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def get_ResponseQueueInfo_v2(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def putref_ResponseQueueInfo_v2(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def get_AdminQueueInfo_v2(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def putref_AdminQueueInfo_v2(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def get_ReceivedAuthenticationLevel(psReceivedAuthenticationLevel: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def get_ResponseQueueInfo(ppqinfoResponse: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def putref_ResponseQueueInfo(pqinfoResponse: win32more.System.MessageQueuing.IMSMQQueueInfo4_head) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def get_AdminQueueInfo(ppqinfoAdmin: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def putref_AdminQueueInfo(pqinfoAdmin: win32more.System.MessageQueuing.IMSMQQueueInfo4_head) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def get_ResponseDestination(ppdestResponse: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def putref_ResponseDestination(pdestResponse: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def get_Destination(ppdestDestination: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def get_LookupId(pvarLookupId: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def get_IsAuthenticated2(pisAuthenticated: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def get_IsFirstInTransaction2(pisFirstInXact: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def get_IsLastInTransaction2(pisLastInXact: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def AttachCurrentSecurityContext2() -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def get_SoapEnvelope(pbstrSoapEnvelope: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def get_CompoundMessage(pvarCompoundMessage: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def put_SoapHeader(bstrSoapHeader: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def put_SoapBody(bstrSoapBody: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IMSMQOutgoingQueueManagement(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQManagement
    Guid = Guid('64c478fb-f9b0-4695-8a-7f-43-9a-c9-43-26-d3')
    @commethod(16)
    def get_State(plState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_NextHops(pvNextHops: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EodGetSendInfo(ppCollection: POINTER(win32more.System.MessageQueuing.IMSMQCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def EodResend() -> win32more.Foundation.HRESULT: ...
class IMSMQPrivateDestination(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b17-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Handle(pvarHandle: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Handle(varHandle: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSMQPrivateEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7ab3341-c9d3-11d1-bb-47-00-80-c7-c5-a2-c0')
    @commethod(7)
    def get_Hwnd(phwnd: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def FireArrivedEvent(pq: win32more.System.MessageQueuing.IMSMQQueue_head, msgcursor: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def FireArrivedErrorEvent(pq: win32more.System.MessageQueuing.IMSMQQueue_head, hrStatus: win32more.Foundation.HRESULT, msgcursor: Int32) -> win32more.Foundation.HRESULT: ...
class IMSMQQuery(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e072-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def LookupQueue(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQuery2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b0e-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def LookupQueue(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQuery3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b19-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def LookupQueue_v2(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def LookupQueue(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), MulticastAddress: POINTER(win32more.System.Com.VARIANT_head), RelMulticastAddress: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos3_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQuery4(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b24-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def LookupQueue_v2(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def LookupQueue(QueueGuid: POINTER(win32more.System.Com.VARIANT_head), ServiceTypeGuid: POINTER(win32more.System.Com.VARIANT_head), Label: POINTER(win32more.System.Com.VARIANT_head), CreateTime: POINTER(win32more.System.Com.VARIANT_head), ModifyTime: POINTER(win32more.System.Com.VARIANT_head), RelServiceType: POINTER(win32more.System.Com.VARIANT_head), RelLabel: POINTER(win32more.System.Com.VARIANT_head), RelCreateTime: POINTER(win32more.System.Com.VARIANT_head), RelModifyTime: POINTER(win32more.System.Com.VARIANT_head), MulticastAddress: POINTER(win32more.System.Com.VARIANT_head), RelMulticastAddress: POINTER(win32more.System.Com.VARIANT_head), ppqinfos: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos4_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueue(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e076-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def get_Access(plAccess: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ShareMode(plShareMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_QueueInfo(ppqinfo: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Handle(plHandle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsOpen(pisOpen: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Receive(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Peek(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnableNotification(Event: win32more.System.MessageQueuing.IMSMQEvent_head, Cursor: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ReceiveCurrent(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def PeekNext(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PeekCurrent(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueue2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ef0574e0-06d8-11d3-b1-00-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Access(plAccess: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ShareMode(plShareMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_QueueInfo(ppqinfo: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Handle(plHandle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsOpen(pisOpen: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Receive_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Peek_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnableNotification(Event: win32more.System.MessageQueuing.IMSMQEvent2_head, Cursor: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ReceiveCurrent_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def PeekNext_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PeekCurrent_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Receive(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Peek(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ReceiveCurrent(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def PeekNext(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def PeekCurrent(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueue3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b1b-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Access(plAccess: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ShareMode(plShareMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_QueueInfo(ppqinfo: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Handle(plHandle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsOpen(pisOpen: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Receive_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Peek_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnableNotification(Event: win32more.System.MessageQueuing.IMSMQEvent3_head, Cursor: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ReceiveCurrent_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def PeekNext_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PeekCurrent_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Receive(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Peek(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ReceiveCurrent(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def PeekNext(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def PeekCurrent(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Handle2(pvarHandle: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def ReceiveByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def ReceiveNextByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def ReceivePreviousByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ReceiveFirstByLookupId(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def ReceiveLastByLookupId(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def PeekByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def PeekNextByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def PeekPreviousByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def PeekFirstByLookupId(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def PeekLastByLookupId(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def Purge() -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_IsOpen2(pisOpen: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueue4(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b20-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_Access(plAccess: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ShareMode(plShareMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_QueueInfo(ppqinfo: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Handle(plHandle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsOpen(pisOpen: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Receive_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Peek_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnableNotification(Event: win32more.System.MessageQueuing.IMSMQEvent3_head, Cursor: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ReceiveCurrent_v1(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def PeekNext_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def PeekCurrent_v1(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Receive(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Peek(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ReceiveCurrent(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def PeekNext(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def PeekCurrent(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), ReceiveTimeout: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Handle2(pvarHandle: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def ReceiveByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def ReceiveNextByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def ReceivePreviousByLookupId(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ReceiveFirstByLookupId(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def ReceiveLastByLookupId(Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def PeekByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def PeekNextByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def PeekPreviousByLookupId(LookupId: win32more.System.Com.VARIANT, WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def PeekFirstByLookupId(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def PeekLastByLookupId(WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def Purge() -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_IsOpen2(pisOpen: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def ReceiveByLookupIdAllowPeek(LookupId: win32more.System.Com.VARIANT, Transaction: POINTER(win32more.System.Com.VARIANT_head), WantDestinationQueue: POINTER(win32more.System.Com.VARIANT_head), WantBody: POINTER(win32more.System.Com.VARIANT_head), WantConnectorType: POINTER(win32more.System.Com.VARIANT_head), ppmsg: POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e07b-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def get_QueueGuid(pbstrGuidQueue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServiceTypeGuid(pbstrGuidServiceType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_ServiceTypeGuid(bstrGuidServiceType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PathName(pbstrPathName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_PathName(bstrPathName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FormatName(bstrFormatName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsTransactional(pisTransactional: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Quota(plQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Quota(lQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_BasePriority(plBasePriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_BasePriority(lBasePriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_CreateTime(pvarCreateTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ModifyTime(pvarModifyTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Authenticate(plAuthenticate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Authenticate(lAuthenticate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_JournalQuota(plJournalQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_JournalQuota(lJournalQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_IsWorldReadable(pisWorldReadable: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def Create(IsTransactional: POINTER(win32more.System.Com.VARIANT_head), IsWorldReadable: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def Open(Access: Int32, ShareMode: Int32, ppq: POINTER(win32more.System.MessageQueuing.IMSMQQueue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def Update() -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfo2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fd174a80-89cf-11d2-b0-f2-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_QueueGuid(pbstrGuidQueue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServiceTypeGuid(pbstrGuidServiceType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_ServiceTypeGuid(bstrGuidServiceType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PathName(pbstrPathName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_PathName(bstrPathName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FormatName(bstrFormatName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsTransactional(pisTransactional: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Quota(plQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Quota(lQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_BasePriority(plBasePriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_BasePriority(lBasePriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_CreateTime(pvarCreateTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ModifyTime(pvarModifyTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Authenticate(plAuthenticate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Authenticate(lAuthenticate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_JournalQuota(plJournalQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_JournalQuota(lJournalQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_IsWorldReadable(pisWorldReadable: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def Create(IsTransactional: POINTER(win32more.System.Com.VARIANT_head), IsWorldReadable: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def Open(Access: Int32, ShareMode: Int32, ppq: POINTER(win32more.System.MessageQueuing.IMSMQQueue2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def Update() -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_PathNameDNS(pbstrPathNameDNS: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_Security(pvarSecurity: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_Security(varSecurity: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfo3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b1d-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_QueueGuid(pbstrGuidQueue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServiceTypeGuid(pbstrGuidServiceType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_ServiceTypeGuid(bstrGuidServiceType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PathName(pbstrPathName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_PathName(bstrPathName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FormatName(bstrFormatName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsTransactional(pisTransactional: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Quota(plQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Quota(lQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_BasePriority(plBasePriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_BasePriority(lBasePriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_CreateTime(pvarCreateTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ModifyTime(pvarModifyTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Authenticate(plAuthenticate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Authenticate(lAuthenticate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_JournalQuota(plJournalQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_JournalQuota(lJournalQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_IsWorldReadable(pisWorldReadable: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def Create(IsTransactional: POINTER(win32more.System.Com.VARIANT_head), IsWorldReadable: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def Open(Access: Int32, ShareMode: Int32, ppq: POINTER(win32more.System.MessageQueuing.IMSMQQueue3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def Update() -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_PathNameDNS(pbstrPathNameDNS: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_Security(pvarSecurity: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_Security(varSecurity: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsTransactional2(pisTransactional: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_IsWorldReadable2(pisWorldReadable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_MulticastAddress(pbstrMulticastAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def put_MulticastAddress(bstrMulticastAddress: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_ADsPath(pbstrADsPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfo4(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b21-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def get_QueueGuid(pbstrGuidQueue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ServiceTypeGuid(pbstrGuidServiceType: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_ServiceTypeGuid(bstrGuidServiceType: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Label(pbstrLabel: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Label(bstrLabel: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PathName(pbstrPathName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_PathName(bstrPathName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_FormatName(pbstrFormatName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_FormatName(bstrFormatName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsTransactional(pisTransactional: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PrivLevel(plPrivLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_PrivLevel(lPrivLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Journal(plJournal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_Journal(lJournal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Quota(plQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Quota(lQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_BasePriority(plBasePriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_BasePriority(lBasePriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_CreateTime(pvarCreateTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ModifyTime(pvarModifyTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Authenticate(plAuthenticate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_Authenticate(lAuthenticate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_JournalQuota(plJournalQuota: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_JournalQuota(lJournalQuota: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_IsWorldReadable(pisWorldReadable: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def Create(IsTransactional: POINTER(win32more.System.Com.VARIANT_head), IsWorldReadable: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def Open(Access: Int32, ShareMode: Int32, ppq: POINTER(win32more.System.MessageQueuing.IMSMQQueue4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def Update() -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_PathNameDNS(pbstrPathNameDNS: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_Security(pvarSecurity: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_Security(varSecurity: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsTransactional2(pisTransactional: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def get_IsWorldReadable2(pisWorldReadable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_MulticastAddress(pbstrMulticastAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def put_MulticastAddress(bstrMulticastAddress: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_ADsPath(pbstrADsPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfos(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e07d-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(ppqinfoNext: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfos2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b0f-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(ppqinfoNext: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfos3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b1e-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(ppqinfoNext: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueInfos4(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b22-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(ppqinfoNext: POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQQueueManagement(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQManagement
    Guid = Guid('7fbe7759-5760-444d-b8-a5-5e-7a-b9-a8-4c-ce')
    @commethod(16)
    def get_JournalMessageCount(plJournalMessageCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_BytesInJournal(pvBytesInJournal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EodGetReceiveInfo(pvCollection: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransaction(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e07f-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def get_Transaction(plTransaction: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(fRetaining: POINTER(win32more.System.Com.VARIANT_head), grfTC: POINTER(win32more.System.Com.VARIANT_head), grfRM: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Abort(fRetaining: POINTER(win32more.System.Com.VARIANT_head), fAsync: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransaction2(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQTransaction
    Guid = Guid('2ce0c5b0-6e67-11d2-b0-e6-00-e0-2c-07-4f-6b')
    @commethod(10)
    def InitNew(varTransaction: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransaction3(c_void_p):
    extends: win32more.System.MessageQueuing.IMSMQTransaction2
    Guid = Guid('eba96b13-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(12)
    def get_ITransaction(pvarITransaction: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransactionDispenser(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d7d6e083-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransactionDispenser2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b11-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
class IMSMQTransactionDispenser3(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('eba96b15-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
    @commethod(7)
    def BeginTransaction(ptransaction: POINTER(win32more.System.MessageQueuing.IMSMQTransaction3_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Properties(ppcolProperties: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
MQACCESS = Int32
MQ_RECEIVE_ACCESS: MQACCESS = 1
MQ_SEND_ACCESS: MQACCESS = 2
MQ_PEEK_ACCESS: MQACCESS = 32
MQ_ADMIN_ACCESS: MQACCESS = 128
MQAUTHENTICATE = Int32
MQ_AUTHENTICATE_NONE: MQAUTHENTICATE = 0
MQ_AUTHENTICATE: MQAUTHENTICATE = 1
MQCALG = Int32
MQMSG_CALG_MD2: MQCALG = 32769
MQMSG_CALG_MD4: MQCALG = 32770
MQMSG_CALG_MD5: MQCALG = 32771
MQMSG_CALG_SHA: MQCALG = 32772
MQMSG_CALG_SHA1: MQCALG = 32772
MQMSG_CALG_MAC: MQCALG = 32773
MQMSG_CALG_RSA_SIGN: MQCALG = 9216
MQMSG_CALG_DSS_SIGN: MQCALG = 8704
MQMSG_CALG_RSA_KEYX: MQCALG = 41984
MQMSG_CALG_DES: MQCALG = 26113
MQMSG_CALG_RC2: MQCALG = 26114
MQMSG_CALG_RC4: MQCALG = 26625
MQMSG_CALG_SEAL: MQCALG = 26626
MQCERT_REGISTER = Int32
MQCERT_REGISTER_ALWAYS: MQCERT_REGISTER = 1
MQCERT_REGISTER_IF_NOT_EXIST: MQCERT_REGISTER = 2
MQDEFAULT = Int32
DEFAULT_M_PRIORITY: MQDEFAULT = 3
DEFAULT_M_DELIVERY: MQDEFAULT = 0
DEFAULT_M_ACKNOWLEDGE: MQDEFAULT = 0
DEFAULT_M_JOURNAL: MQDEFAULT = 0
DEFAULT_M_APPSPECIFIC: MQDEFAULT = 0
DEFAULT_M_PRIV_LEVEL: MQDEFAULT = 0
DEFAULT_M_AUTH_LEVEL: MQDEFAULT = 0
DEFAULT_M_SENDERID_TYPE: MQDEFAULT = 1
DEFAULT_Q_JOURNAL: MQDEFAULT = 0
DEFAULT_Q_BASEPRIORITY: MQDEFAULT = 0
DEFAULT_Q_QUOTA: MQDEFAULT = -1
DEFAULT_Q_JOURNAL_QUOTA: MQDEFAULT = -1
DEFAULT_Q_TRANSACTION: MQDEFAULT = 0
DEFAULT_Q_AUTHENTICATE: MQDEFAULT = 0
DEFAULT_Q_PRIV_LEVEL: MQDEFAULT = 1
DEFAULT_M_LOOKUPID: MQDEFAULT = 0
MQERROR = Int32
MQ_ERROR: MQERROR = -1072824319
MQ_ERROR_PROPERTY: MQERROR = -1072824318
MQ_ERROR_QUEUE_NOT_FOUND: MQERROR = -1072824317
MQ_ERROR_QUEUE_NOT_ACTIVE: MQERROR = -1072824316
MQ_ERROR_QUEUE_EXISTS: MQERROR = -1072824315
MQ_ERROR_INVALID_PARAMETER: MQERROR = -1072824314
MQ_ERROR_INVALID_HANDLE: MQERROR = -1072824313
MQ_ERROR_OPERATION_CANCELLED: MQERROR = -1072824312
MQ_ERROR_SHARING_VIOLATION: MQERROR = -1072824311
MQ_ERROR_SERVICE_NOT_AVAILABLE: MQERROR = -1072824309
MQ_ERROR_MACHINE_NOT_FOUND: MQERROR = -1072824307
MQ_ERROR_ILLEGAL_SORT: MQERROR = -1072824304
MQ_ERROR_ILLEGAL_USER: MQERROR = -1072824303
MQ_ERROR_NO_DS: MQERROR = -1072824301
MQ_ERROR_ILLEGAL_QUEUE_PATHNAME: MQERROR = -1072824300
MQ_ERROR_ILLEGAL_PROPERTY_VALUE: MQERROR = -1072824296
MQ_ERROR_ILLEGAL_PROPERTY_VT: MQERROR = -1072824295
MQ_ERROR_BUFFER_OVERFLOW: MQERROR = -1072824294
MQ_ERROR_IO_TIMEOUT: MQERROR = -1072824293
MQ_ERROR_ILLEGAL_CURSOR_ACTION: MQERROR = -1072824292
MQ_ERROR_MESSAGE_ALREADY_RECEIVED: MQERROR = -1072824291
MQ_ERROR_ILLEGAL_FORMATNAME: MQERROR = -1072824290
MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL: MQERROR = -1072824289
MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION: MQERROR = -1072824288
MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR: MQERROR = -1072824287
MQ_ERROR_SENDERID_BUFFER_TOO_SMALL: MQERROR = -1072824286
MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL: MQERROR = -1072824285
MQ_ERROR_CANNOT_IMPERSONATE_CLIENT: MQERROR = -1072824284
MQ_ERROR_ACCESS_DENIED: MQERROR = -1072824283
MQ_ERROR_PRIVILEGE_NOT_HELD: MQERROR = -1072824282
MQ_ERROR_INSUFFICIENT_RESOURCES: MQERROR = -1072824281
MQ_ERROR_USER_BUFFER_TOO_SMALL: MQERROR = -1072824280
MQ_ERROR_MESSAGE_STORAGE_FAILED: MQERROR = -1072824278
MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL: MQERROR = -1072824277
MQ_ERROR_INVALID_CERTIFICATE: MQERROR = -1072824276
MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE: MQERROR = -1072824275
MQ_ERROR_INTERNAL_USER_CERT_EXIST: MQERROR = -1072824274
MQ_ERROR_NO_INTERNAL_USER_CERT: MQERROR = -1072824273
MQ_ERROR_CORRUPTED_SECURITY_DATA: MQERROR = -1072824272
MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE: MQERROR = -1072824271
MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION: MQERROR = -1072824269
MQ_ERROR_BAD_SECURITY_CONTEXT: MQERROR = -1072824267
MQ_ERROR_COULD_NOT_GET_USER_SID: MQERROR = -1072824266
MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO: MQERROR = -1072824265
MQ_ERROR_ILLEGAL_MQCOLUMNS: MQERROR = -1072824264
MQ_ERROR_ILLEGAL_PROPID: MQERROR = -1072824263
MQ_ERROR_ILLEGAL_RELATION: MQERROR = -1072824262
MQ_ERROR_ILLEGAL_PROPERTY_SIZE: MQERROR = -1072824261
MQ_ERROR_ILLEGAL_RESTRICTION_PROPID: MQERROR = -1072824260
MQ_ERROR_ILLEGAL_MQQUEUEPROPS: MQERROR = -1072824259
MQ_ERROR_PROPERTY_NOTALLOWED: MQERROR = -1072824258
MQ_ERROR_INSUFFICIENT_PROPERTIES: MQERROR = -1072824257
MQ_ERROR_MACHINE_EXISTS: MQERROR = -1072824256
MQ_ERROR_ILLEGAL_MQQMPROPS: MQERROR = -1072824255
MQ_ERROR_DS_IS_FULL: MQERROR = -1072824254
MQ_ERROR_DS_ERROR: MQERROR = -1072824253
MQ_ERROR_INVALID_OWNER: MQERROR = -1072824252
MQ_ERROR_UNSUPPORTED_ACCESS_MODE: MQERROR = -1072824251
MQ_ERROR_RESULT_BUFFER_TOO_SMALL: MQERROR = -1072824250
MQ_ERROR_DELETE_CN_IN_USE: MQERROR = -1072824248
MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER: MQERROR = -1072824247
MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE: MQERROR = -1072824246
MQ_ERROR_QUEUE_NOT_AVAILABLE: MQERROR = -1072824245
MQ_ERROR_DTC_CONNECT: MQERROR = -1072824244
MQ_ERROR_TRANSACTION_IMPORT: MQERROR = -1072824242
MQ_ERROR_TRANSACTION_USAGE: MQERROR = -1072824240
MQ_ERROR_TRANSACTION_SEQUENCE: MQERROR = -1072824239
MQ_ERROR_MISSING_CONNECTOR_TYPE: MQERROR = -1072824235
MQ_ERROR_STALE_HANDLE: MQERROR = -1072824234
MQ_ERROR_TRANSACTION_ENLIST: MQERROR = -1072824232
MQ_ERROR_QUEUE_DELETED: MQERROR = -1072824230
MQ_ERROR_ILLEGAL_CONTEXT: MQERROR = -1072824229
MQ_ERROR_ILLEGAL_SORT_PROPID: MQERROR = -1072824228
MQ_ERROR_LABEL_TOO_LONG: MQERROR = -1072824227
MQ_ERROR_LABEL_BUFFER_TOO_SMALL: MQERROR = -1072824226
MQ_ERROR_MQIS_SERVER_EMPTY: MQERROR = -1072824225
MQ_ERROR_MQIS_READONLY_MODE: MQERROR = -1072824224
MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL: MQERROR = -1072824223
MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL: MQERROR = -1072824222
MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL: MQERROR = -1072824221
MQ_ERROR_ILLEGAL_OPERATION: MQERROR = -1072824220
MQ_ERROR_WRITE_NOT_ALLOWED: MQERROR = -1072824219
MQ_ERROR_WKS_CANT_SERVE_CLIENT: MQERROR = -1072824218
MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW: MQERROR = -1072824217
MQ_CORRUPTED_QUEUE_WAS_DELETED: MQERROR = -1072824216
MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE: MQERROR = -1072824215
MQ_ERROR_UNSUPPORTED_OPERATION: MQERROR = -1072824214
MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED: MQERROR = -1072824213
MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR: MQERROR = -1072824212
MQ_ERROR_CERTIFICATE_NOT_PROVIDED: MQERROR = -1072824211
MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED: MQERROR = -1072824210
MQ_ERROR_CANT_CREATE_CERT_STORE: MQERROR = -1072824209
MQ_ERROR_CANNOT_CREATE_CERT_STORE: MQERROR = -1072824209
MQ_ERROR_CANT_OPEN_CERT_STORE: MQERROR = -1072824208
MQ_ERROR_CANNOT_OPEN_CERT_STORE: MQERROR = -1072824208
MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION: MQERROR = -1072824207
MQ_ERROR_CANNOT_GRANT_ADD_GUID: MQERROR = -1072824206
MQ_ERROR_CANNOT_LOAD_MSMQOCM: MQERROR = -1072824205
MQ_ERROR_NO_ENTRY_POINT_MSMQOCM: MQERROR = -1072824204
MQ_ERROR_NO_MSMQ_SERVERS_ON_DC: MQERROR = -1072824203
MQ_ERROR_CANNOT_JOIN_DOMAIN: MQERROR = -1072824202
MQ_ERROR_CANNOT_CREATE_ON_GC: MQERROR = -1072824201
MQ_ERROR_GUID_NOT_MATCHING: MQERROR = -1072824200
MQ_ERROR_PUBLIC_KEY_NOT_FOUND: MQERROR = -1072824199
MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST: MQERROR = -1072824198
MQ_ERROR_ILLEGAL_MQPRIVATEPROPS: MQERROR = -1072824197
MQ_ERROR_NO_GC_IN_DOMAIN: MQERROR = -1072824196
MQ_ERROR_NO_MSMQ_SERVERS_ON_GC: MQERROR = -1072824195
MQ_ERROR_CANNOT_GET_DN: MQERROR = -1072824194
MQ_ERROR_CANNOT_HASH_DATA_EX: MQERROR = -1072824193
MQ_ERROR_CANNOT_SIGN_DATA_EX: MQERROR = -1072824192
MQ_ERROR_CANNOT_CREATE_HASH_EX: MQERROR = -1072824191
MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX: MQERROR = -1072824190
MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS: MQERROR = -1072824189
MQ_ERROR_NO_MQUSER_OU: MQERROR = -1072824188
MQ_ERROR_CANNOT_LOAD_MQAD: MQERROR = -1072824187
MQ_ERROR_CANNOT_LOAD_MQDSSRV: MQERROR = -1072824186
MQ_ERROR_PROPERTIES_CONFLICT: MQERROR = -1072824185
MQ_ERROR_MESSAGE_NOT_FOUND: MQERROR = -1072824184
MQ_ERROR_CANT_RESOLVE_SITES: MQERROR = -1072824183
MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS: MQERROR = -1072824182
MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER: MQERROR = -1072824181
MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS: MQERROR = -1072824180
MQ_ERROR_MULTI_SORT_KEYS: MQERROR = -1072824179
MQ_ERROR_GC_NEEDED: MQERROR = -1072824178
MQ_ERROR_DS_BIND_ROOT_FOREST: MQERROR = -1072824177
MQ_ERROR_DS_LOCAL_USER: MQERROR = -1072824176
MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED: MQERROR = -1072824175
MQ_ERROR_BAD_XML_FORMAT: MQERROR = -1072824174
MQ_ERROR_UNSUPPORTED_CLASS: MQERROR = -1072824173
MQ_ERROR_UNINITIALIZED_OBJECT: MQERROR = -1072824172
MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS: MQERROR = -1072824171
MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS: MQERROR = -1072824170
MQJOURNAL = Int32
MQ_JOURNAL_NONE: MQJOURNAL = 0
MQ_JOURNAL: MQJOURNAL = 1
MQMAX = Int32
MQ_MAX_Q_NAME_LEN: MQMAX = 124
MQ_MAX_Q_LABEL_LEN: MQMAX = 124
MQMSGACKNOWLEDGEMENT = Int32
MQMSG_ACKNOWLEDGMENT_NONE: MQMSGACKNOWLEDGEMENT = 0
MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL: MQMSGACKNOWLEDGEMENT = 1
MQMSG_ACKNOWLEDGMENT_POS_RECEIVE: MQMSGACKNOWLEDGEMENT = 2
MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL: MQMSGACKNOWLEDGEMENT = 4
MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE: MQMSGACKNOWLEDGEMENT = 8
MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE: MQMSGACKNOWLEDGEMENT = 4
MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE: MQMSGACKNOWLEDGEMENT = 5
MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE: MQMSGACKNOWLEDGEMENT = 12
MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE: MQMSGACKNOWLEDGEMENT = 14
MQMSGAUTHENTICATION = Int32
MQMSG_AUTHENTICATION_NOT_REQUESTED: MQMSGAUTHENTICATION = 0
MQMSG_AUTHENTICATION_REQUESTED: MQMSGAUTHENTICATION = 1
MQMSG_AUTHENTICATED_SIG10: MQMSGAUTHENTICATION = 1
MQMSG_AUTHENTICATION_REQUESTED_EX: MQMSGAUTHENTICATION = 3
MQMSG_AUTHENTICATED_SIG20: MQMSGAUTHENTICATION = 3
MQMSG_AUTHENTICATED_SIG30: MQMSGAUTHENTICATION = 5
MQMSG_AUTHENTICATED_SIGXML: MQMSGAUTHENTICATION = 9
MQMSGAUTHLEVEL = Int32
MQMSG_AUTH_LEVEL_NONE: MQMSGAUTHLEVEL = 0
MQMSG_AUTH_LEVEL_ALWAYS: MQMSGAUTHLEVEL = 1
MQMSG_AUTH_LEVEL_MSMQ10: MQMSGAUTHLEVEL = 2
MQMSG_AUTH_LEVEL_SIG10: MQMSGAUTHLEVEL = 2
MQMSG_AUTH_LEVEL_MSMQ20: MQMSGAUTHLEVEL = 4
MQMSG_AUTH_LEVEL_SIG20: MQMSGAUTHLEVEL = 4
MQMSG_AUTH_LEVEL_SIG30: MQMSGAUTHLEVEL = 8
MQMSGCLASS = Int32
MQMSG_CLASS_NORMAL: MQMSGCLASS = 0
MQMSG_CLASS_REPORT: MQMSGCLASS = 1
MQMSG_CLASS_ACK_REACH_QUEUE: MQMSGCLASS = 2
MQMSG_CLASS_ACK_RECEIVE: MQMSGCLASS = 16384
MQMSG_CLASS_NACK_BAD_DST_Q: MQMSGCLASS = 32768
MQMSG_CLASS_NACK_PURGED: MQMSGCLASS = 32769
MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT: MQMSGCLASS = 32770
MQMSG_CLASS_NACK_Q_EXCEED_QUOTA: MQMSGCLASS = 32771
MQMSG_CLASS_NACK_ACCESS_DENIED: MQMSGCLASS = 32772
MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED: MQMSGCLASS = 32773
MQMSG_CLASS_NACK_BAD_SIGNATURE: MQMSGCLASS = 32774
MQMSG_CLASS_NACK_BAD_ENCRYPTION: MQMSGCLASS = 32775
MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT: MQMSGCLASS = 32776
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q: MQMSGCLASS = 32777
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG: MQMSGCLASS = 32778
MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER: MQMSGCLASS = 32779
MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED: MQMSGCLASS = 32780
MQMSG_CLASS_NACK_Q_DELETED: MQMSGCLASS = 49152
MQMSG_CLASS_NACK_Q_PURGED: MQMSGCLASS = 49153
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT: MQMSGCLASS = 49154
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER: MQMSGCLASS = 49155
MQMSGCURSOR = Int32
MQMSG_FIRST: MQMSGCURSOR = 0
MQMSG_CURRENT: MQMSGCURSOR = 1
MQMSG_NEXT: MQMSGCURSOR = 2
MQMSGDELIVERY = Int32
MQMSG_DELIVERY_EXPRESS: MQMSGDELIVERY = 0
MQMSG_DELIVERY_RECOVERABLE: MQMSGDELIVERY = 1
MQMSGIDSIZE = Int32
MQMSG_MSGID_SIZE: MQMSGIDSIZE = 20
MQMSG_CORRELATIONID_SIZE: MQMSGIDSIZE = 20
MQMSG_XACTID_SIZE: MQMSGIDSIZE = 20
MQMSGJOURNAL = Int32
MQMSG_JOURNAL_NONE: MQMSGJOURNAL = 0
MQMSG_DEADLETTER: MQMSGJOURNAL = 1
MQMSG_JOURNAL: MQMSGJOURNAL = 2
MQMSGMAX = Int32
MQ_MAX_MSG_LABEL_LEN: MQMSGMAX = 249
MQMSGPRIVLEVEL = Int32
MQMSG_PRIV_LEVEL_NONE: MQMSGPRIVLEVEL = 0
MQMSG_PRIV_LEVEL_BODY_BASE: MQMSGPRIVLEVEL = 1
MQMSG_PRIV_LEVEL_BODY_ENHANCED: MQMSGPRIVLEVEL = 3
MQMSGSENDERIDTYPE = Int32
MQMSG_SENDERID_TYPE_NONE: MQMSGSENDERIDTYPE = 0
MQMSG_SENDERID_TYPE_SID: MQMSGSENDERIDTYPE = 1
MQMSGTRACE = Int32
MQMSG_TRACE_NONE: MQMSGTRACE = 0
MQMSG_SEND_ROUTE_TO_REPORT_QUEUE: MQMSGTRACE = 1
MQPRIORITY = Int32
MQ_MIN_PRIORITY: MQPRIORITY = 0
MQ_MAX_PRIORITY: MQPRIORITY = 7
MQPRIVLEVEL = Int32
MQ_PRIV_LEVEL_NONE: MQPRIVLEVEL = 0
MQ_PRIV_LEVEL_OPTIONAL: MQPRIVLEVEL = 1
MQ_PRIV_LEVEL_BODY: MQPRIVLEVEL = 2
MQSHARE = Int32
MQ_DENY_NONE: MQSHARE = 0
MQ_DENY_RECEIVE_SHARE: MQSHARE = 1
MQTRANSACTION = Int32
MQ_NO_TRANSACTION: MQTRANSACTION = 0
MQ_MTS_TRANSACTION: MQTRANSACTION = 1
MQ_XA_TRANSACTION: MQTRANSACTION = 2
MQ_SINGLE_MESSAGE: MQTRANSACTION = 3
MQTRANSACTIONAL = Int32
MQ_TRANSACTIONAL_NONE: MQTRANSACTIONAL = 0
MQ_TRANSACTIONAL: MQTRANSACTIONAL = 1
MQWARNING = Int32
MQ_INFORMATION_PROPERTY: MQWARNING = 1074659329
MQ_INFORMATION_ILLEGAL_PROPERTY: MQWARNING = 1074659330
MQ_INFORMATION_PROPERTY_IGNORED: MQWARNING = 1074659331
MQ_INFORMATION_UNSUPPORTED_PROPERTY: MQWARNING = 1074659332
MQ_INFORMATION_DUPLICATE_PROPERTY: MQWARNING = 1074659333
MQ_INFORMATION_OPERATION_PENDING: MQWARNING = 1074659334
MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL: MQWARNING = 1074659337
MQ_INFORMATION_INTERNAL_USER_CERT_EXIST: MQWARNING = 1074659338
MQ_INFORMATION_OWNER_IGNORED: MQWARNING = 1074659339
MSMQApplication = Guid('d7d6e086-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQCollection = Guid('f72b9031-2f0c-43e8-92-4e-e6-05-2c-dc-49-3f')
MSMQCoordinatedTransactionDispenser = Guid('d7d6e082-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQDestination = Guid('eba96b18-2168-11d3-89-8c-00-e0-2c-07-4f-6b')
MSMQEvent = Guid('d7d6e07a-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQManagement = Guid('39ce96fe-f4c5-4484-a1-43-4c-2d-5d-32-42-29')
MSMQMessage = Guid('d7d6e075-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQOutgoingQueueManagement = Guid('0188401c-247a-4fed-99-c6-bf-14-11-9d-70-55')
MSMQQuery = Guid('d7d6e073-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQQueue = Guid('d7d6e079-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQQueueInfo = Guid('d7d6e07c-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQQueueInfos = Guid('d7d6e07e-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQQueueManagement = Guid('33b6d07e-f27d-42fa-b2-d7-bf-82-e1-1e-93-74')
MSMQTransaction = Guid('d7d6e080-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
MSMQTransactionDispenser = Guid('d7d6e084-dccd-11d0-aa-4b-00-60-97-0d-eb-ae')
QUEUE_STATE = Int32
MQ_QUEUE_STATE_LOCAL_CONNECTION: QUEUE_STATE = 0
MQ_QUEUE_STATE_DISCONNECTED: QUEUE_STATE = 1
MQ_QUEUE_STATE_WAITING: QUEUE_STATE = 2
MQ_QUEUE_STATE_NEEDVALIDATE: QUEUE_STATE = 3
MQ_QUEUE_STATE_ONHOLD: QUEUE_STATE = 4
MQ_QUEUE_STATE_NONACTIVE: QUEUE_STATE = 5
MQ_QUEUE_STATE_CONNECTED: QUEUE_STATE = 6
MQ_QUEUE_STATE_DISCONNECTING: QUEUE_STATE = 7
MQ_QUEUE_STATE_LOCKED: QUEUE_STATE = 8
QUEUE_TYPE = Int32
MQ_TYPE_PUBLIC: QUEUE_TYPE = 0
MQ_TYPE_PRIVATE: QUEUE_TYPE = 1
MQ_TYPE_MACHINE: QUEUE_TYPE = 2
MQ_TYPE_CONNECTOR: QUEUE_TYPE = 3
MQ_TYPE_MULTICAST: QUEUE_TYPE = 4
RELOPS = Int32
REL_NOP: RELOPS = 0
REL_EQ: RELOPS = 1
REL_NEQ: RELOPS = 2
REL_LT: RELOPS = 3
REL_GT: RELOPS = 4
REL_LE: RELOPS = 5
REL_GE: RELOPS = 6
XACT_STATUS = Int32
MQ_XACT_STATUS_XACT: XACT_STATUS = 0
MQ_XACT_STATUS_NOT_XACT: XACT_STATUS = 1
MQ_XACT_STATUS_UNKNOWN: XACT_STATUS = 2
make_head(_module, '_DMSMQEventEvents')
make_head(_module, 'IMSMQApplication')
make_head(_module, 'IMSMQApplication2')
make_head(_module, 'IMSMQApplication3')
make_head(_module, 'IMSMQCollection')
make_head(_module, 'IMSMQCoordinatedTransactionDispenser')
make_head(_module, 'IMSMQCoordinatedTransactionDispenser2')
make_head(_module, 'IMSMQCoordinatedTransactionDispenser3')
make_head(_module, 'IMSMQDestination')
make_head(_module, 'IMSMQEvent')
make_head(_module, 'IMSMQEvent2')
make_head(_module, 'IMSMQEvent3')
make_head(_module, 'IMSMQManagement')
make_head(_module, 'IMSMQMessage')
make_head(_module, 'IMSMQMessage2')
make_head(_module, 'IMSMQMessage3')
make_head(_module, 'IMSMQMessage4')
make_head(_module, 'IMSMQOutgoingQueueManagement')
make_head(_module, 'IMSMQPrivateDestination')
make_head(_module, 'IMSMQPrivateEvent')
make_head(_module, 'IMSMQQuery')
make_head(_module, 'IMSMQQuery2')
make_head(_module, 'IMSMQQuery3')
make_head(_module, 'IMSMQQuery4')
make_head(_module, 'IMSMQQueue')
make_head(_module, 'IMSMQQueue2')
make_head(_module, 'IMSMQQueue3')
make_head(_module, 'IMSMQQueue4')
make_head(_module, 'IMSMQQueueInfo')
make_head(_module, 'IMSMQQueueInfo2')
make_head(_module, 'IMSMQQueueInfo3')
make_head(_module, 'IMSMQQueueInfo4')
make_head(_module, 'IMSMQQueueInfos')
make_head(_module, 'IMSMQQueueInfos2')
make_head(_module, 'IMSMQQueueInfos3')
make_head(_module, 'IMSMQQueueInfos4')
make_head(_module, 'IMSMQQueueManagement')
make_head(_module, 'IMSMQTransaction')
make_head(_module, 'IMSMQTransaction2')
make_head(_module, 'IMSMQTransaction3')
make_head(_module, 'IMSMQTransactionDispenser')
make_head(_module, 'IMSMQTransactionDispenser2')
make_head(_module, 'IMSMQTransactionDispenser3')
__all__ = [
    "DEFAULT_M_ACKNOWLEDGE",
    "DEFAULT_M_APPSPECIFIC",
    "DEFAULT_M_AUTH_LEVEL",
    "DEFAULT_M_DELIVERY",
    "DEFAULT_M_JOURNAL",
    "DEFAULT_M_LOOKUPID",
    "DEFAULT_M_PRIORITY",
    "DEFAULT_M_PRIV_LEVEL",
    "DEFAULT_M_SENDERID_TYPE",
    "DEFAULT_Q_AUTHENTICATE",
    "DEFAULT_Q_BASEPRIORITY",
    "DEFAULT_Q_JOURNAL",
    "DEFAULT_Q_JOURNAL_QUOTA",
    "DEFAULT_Q_PRIV_LEVEL",
    "DEFAULT_Q_QUOTA",
    "DEFAULT_Q_TRANSACTION",
    "FOREIGN_STATUS",
    "IMSMQApplication",
    "IMSMQApplication2",
    "IMSMQApplication3",
    "IMSMQCollection",
    "IMSMQCoordinatedTransactionDispenser",
    "IMSMQCoordinatedTransactionDispenser2",
    "IMSMQCoordinatedTransactionDispenser3",
    "IMSMQDestination",
    "IMSMQEvent",
    "IMSMQEvent2",
    "IMSMQEvent3",
    "IMSMQManagement",
    "IMSMQMessage",
    "IMSMQMessage2",
    "IMSMQMessage3",
    "IMSMQMessage4",
    "IMSMQOutgoingQueueManagement",
    "IMSMQPrivateDestination",
    "IMSMQPrivateEvent",
    "IMSMQQuery",
    "IMSMQQuery2",
    "IMSMQQuery3",
    "IMSMQQuery4",
    "IMSMQQueue",
    "IMSMQQueue2",
    "IMSMQQueue3",
    "IMSMQQueue4",
    "IMSMQQueueInfo",
    "IMSMQQueueInfo2",
    "IMSMQQueueInfo3",
    "IMSMQQueueInfo4",
    "IMSMQQueueInfos",
    "IMSMQQueueInfos2",
    "IMSMQQueueInfos3",
    "IMSMQQueueInfos4",
    "IMSMQQueueManagement",
    "IMSMQTransaction",
    "IMSMQTransaction2",
    "IMSMQTransaction3",
    "IMSMQTransactionDispenser",
    "IMSMQTransactionDispenser2",
    "IMSMQTransactionDispenser3",
    "LONG_LIVED",
    "MACHINE_ACTION_CONNECT",
    "MACHINE_ACTION_DISCONNECT",
    "MACHINE_ACTION_TIDY",
    "MGMT_QUEUE_CORRECT_TYPE",
    "MGMT_QUEUE_FOREIGN_TYPE",
    "MGMT_QUEUE_INCORRECT_TYPE",
    "MGMT_QUEUE_LOCAL_LOCATION",
    "MGMT_QUEUE_NOT_FOREIGN_TYPE",
    "MGMT_QUEUE_NOT_TRANSACTIONAL_TYPE",
    "MGMT_QUEUE_REMOTE_LOCATION",
    "MGMT_QUEUE_STATE_CONNECTED",
    "MGMT_QUEUE_STATE_DISCONNECTED",
    "MGMT_QUEUE_STATE_DISCONNECTING",
    "MGMT_QUEUE_STATE_LOCAL",
    "MGMT_QUEUE_STATE_LOCKED",
    "MGMT_QUEUE_STATE_NEED_VALIDATE",
    "MGMT_QUEUE_STATE_NONACTIVE",
    "MGMT_QUEUE_STATE_ONHOLD",
    "MGMT_QUEUE_STATE_WAITING",
    "MGMT_QUEUE_TRANSACTIONAL_TYPE",
    "MGMT_QUEUE_TYPE_CONNECTOR",
    "MGMT_QUEUE_TYPE_MACHINE",
    "MGMT_QUEUE_TYPE_MULTICAST",
    "MGMT_QUEUE_TYPE_PRIVATE",
    "MGMT_QUEUE_TYPE_PUBLIC",
    "MGMT_QUEUE_UNKNOWN_TYPE",
    "MO_MACHINE_TOKEN",
    "MO_QUEUE_TOKEN",
    "MQACCESS",
    "MQAUTHENTICATE",
    "MQCALG",
    "MQCERT_REGISTER",
    "MQCERT_REGISTER_ALWAYS",
    "MQCERT_REGISTER_IF_NOT_EXIST",
    "MQDEFAULT",
    "MQERROR",
    "MQJOURNAL",
    "MQMAX",
    "MQMSGACKNOWLEDGEMENT",
    "MQMSGAUTHENTICATION",
    "MQMSGAUTHLEVEL",
    "MQMSGCLASS",
    "MQMSGCURSOR",
    "MQMSGDELIVERY",
    "MQMSGIDSIZE",
    "MQMSGJOURNAL",
    "MQMSGMAX",
    "MQMSGPRIVLEVEL",
    "MQMSGSENDERIDTYPE",
    "MQMSGTRACE",
    "MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE",
    "MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE",
    "MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL",
    "MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_NONE",
    "MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL",
    "MQMSG_ACKNOWLEDGMENT_POS_RECEIVE",
    "MQMSG_AUTHENTICATED_QM_MESSAGE",
    "MQMSG_AUTHENTICATED_SIG10",
    "MQMSG_AUTHENTICATED_SIG20",
    "MQMSG_AUTHENTICATED_SIG30",
    "MQMSG_AUTHENTICATED_SIGXML",
    "MQMSG_AUTHENTICATION_NOT_REQUESTED",
    "MQMSG_AUTHENTICATION_REQUESTED",
    "MQMSG_AUTHENTICATION_REQUESTED_EX",
    "MQMSG_AUTH_LEVEL_ALWAYS",
    "MQMSG_AUTH_LEVEL_MSMQ10",
    "MQMSG_AUTH_LEVEL_MSMQ20",
    "MQMSG_AUTH_LEVEL_NONE",
    "MQMSG_AUTH_LEVEL_SIG10",
    "MQMSG_AUTH_LEVEL_SIG20",
    "MQMSG_AUTH_LEVEL_SIG30",
    "MQMSG_CALG_DES",
    "MQMSG_CALG_DSS_SIGN",
    "MQMSG_CALG_MAC",
    "MQMSG_CALG_MD2",
    "MQMSG_CALG_MD4",
    "MQMSG_CALG_MD5",
    "MQMSG_CALG_RC2",
    "MQMSG_CALG_RC4",
    "MQMSG_CALG_RSA_KEYX",
    "MQMSG_CALG_RSA_SIGN",
    "MQMSG_CALG_SEAL",
    "MQMSG_CALG_SHA",
    "MQMSG_CALG_SHA1",
    "MQMSG_CLASS_ACK_REACH_QUEUE",
    "MQMSG_CLASS_ACK_RECEIVE",
    "MQMSG_CLASS_NACK_ACCESS_DENIED",
    "MQMSG_CLASS_NACK_BAD_DST_Q",
    "MQMSG_CLASS_NACK_BAD_ENCRYPTION",
    "MQMSG_CLASS_NACK_BAD_SIGNATURE",
    "MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT",
    "MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED",
    "MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG",
    "MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q",
    "MQMSG_CLASS_NACK_PURGED",
    "MQMSG_CLASS_NACK_Q_DELETED",
    "MQMSG_CLASS_NACK_Q_EXCEED_QUOTA",
    "MQMSG_CLASS_NACK_Q_PURGED",
    "MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT",
    "MQMSG_CLASS_NACK_RECEIVE_TIMEOUT",
    "MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER",
    "MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED",
    "MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER",
    "MQMSG_CLASS_NORMAL",
    "MQMSG_CLASS_REPORT",
    "MQMSG_CORRELATIONID_SIZE",
    "MQMSG_CURRENT",
    "MQMSG_DEADLETTER",
    "MQMSG_DELIVERY_EXPRESS",
    "MQMSG_DELIVERY_RECOVERABLE",
    "MQMSG_FIRST",
    "MQMSG_FIRST_IN_XACT",
    "MQMSG_JOURNAL",
    "MQMSG_JOURNAL_NONE",
    "MQMSG_LAST_IN_XACT",
    "MQMSG_MSGID_SIZE",
    "MQMSG_NEXT",
    "MQMSG_NOT_FIRST_IN_XACT",
    "MQMSG_NOT_LAST_IN_XACT",
    "MQMSG_PRIV_LEVEL_BODY_AES",
    "MQMSG_PRIV_LEVEL_BODY_BASE",
    "MQMSG_PRIV_LEVEL_BODY_ENHANCED",
    "MQMSG_PRIV_LEVEL_NONE",
    "MQMSG_SENDERID_TYPE_NONE",
    "MQMSG_SENDERID_TYPE_SID",
    "MQMSG_SEND_ROUTE_TO_REPORT_QUEUE",
    "MQMSG_TRACE_NONE",
    "MQMSG_XACTID_SIZE",
    "MQPRIORITY",
    "MQPRIVLEVEL",
    "MQSEC_DELETE_JOURNAL_MESSAGE",
    "MQSEC_DELETE_MESSAGE",
    "MQSEC_GET_QUEUE_PROPERTIES",
    "MQSEC_PEEK_MESSAGE",
    "MQSEC_QUEUE_GENERIC_EXECUTE",
    "MQSEC_SET_QUEUE_PROPERTIES",
    "MQSEC_WRITE_MESSAGE",
    "MQSHARE",
    "MQTRANSACTION",
    "MQTRANSACTIONAL",
    "MQWARNING",
    "MQ_ACTION_PEEK_CURRENT",
    "MQ_ACTION_PEEK_NEXT",
    "MQ_ACTION_RECEIVE",
    "MQ_ADMIN_ACCESS",
    "MQ_AUTHENTICATE",
    "MQ_AUTHENTICATE_NONE",
    "MQ_CORRUPTED_QUEUE_WAS_DELETED",
    "MQ_DENY_NONE",
    "MQ_DENY_RECEIVE_SHARE",
    "MQ_ERROR",
    "MQ_ERROR_ACCESS_DENIED",
    "MQ_ERROR_BAD_SECURITY_CONTEXT",
    "MQ_ERROR_BAD_XML_FORMAT",
    "MQ_ERROR_BUFFER_OVERFLOW",
    "MQ_ERROR_CANNOT_CREATE_CERT_STORE",
    "MQ_ERROR_CANNOT_CREATE_HASH_EX",
    "MQ_ERROR_CANNOT_CREATE_ON_GC",
    "MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS",
    "MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS",
    "MQ_ERROR_CANNOT_GET_DN",
    "MQ_ERROR_CANNOT_GRANT_ADD_GUID",
    "MQ_ERROR_CANNOT_HASH_DATA_EX",
    "MQ_ERROR_CANNOT_IMPERSONATE_CLIENT",
    "MQ_ERROR_CANNOT_JOIN_DOMAIN",
    "MQ_ERROR_CANNOT_LOAD_MQAD",
    "MQ_ERROR_CANNOT_LOAD_MQDSSRV",
    "MQ_ERROR_CANNOT_LOAD_MSMQOCM",
    "MQ_ERROR_CANNOT_OPEN_CERT_STORE",
    "MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR",
    "MQ_ERROR_CANNOT_SIGN_DATA_EX",
    "MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS",
    "MQ_ERROR_CANT_CREATE_CERT_STORE",
    "MQ_ERROR_CANT_OPEN_CERT_STORE",
    "MQ_ERROR_CANT_RESOLVE_SITES",
    "MQ_ERROR_CERTIFICATE_NOT_PROVIDED",
    "MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION",
    "MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE",
    "MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE",
    "MQ_ERROR_CORRUPTED_SECURITY_DATA",
    "MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO",
    "MQ_ERROR_COULD_NOT_GET_USER_SID",
    "MQ_ERROR_DELETE_CN_IN_USE",
    "MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW",
    "MQ_ERROR_DS_BIND_ROOT_FOREST",
    "MQ_ERROR_DS_ERROR",
    "MQ_ERROR_DS_IS_FULL",
    "MQ_ERROR_DS_LOCAL_USER",
    "MQ_ERROR_DTC_CONNECT",
    "MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED",
    "MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX",
    "MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL",
    "MQ_ERROR_GC_NEEDED",
    "MQ_ERROR_GUID_NOT_MATCHING",
    "MQ_ERROR_ILLEGAL_CONTEXT",
    "MQ_ERROR_ILLEGAL_CURSOR_ACTION",
    "MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION",
    "MQ_ERROR_ILLEGAL_FORMATNAME",
    "MQ_ERROR_ILLEGAL_MQCOLUMNS",
    "MQ_ERROR_ILLEGAL_MQPRIVATEPROPS",
    "MQ_ERROR_ILLEGAL_MQQMPROPS",
    "MQ_ERROR_ILLEGAL_MQQUEUEPROPS",
    "MQ_ERROR_ILLEGAL_OPERATION",
    "MQ_ERROR_ILLEGAL_PROPERTY_SIZE",
    "MQ_ERROR_ILLEGAL_PROPERTY_VALUE",
    "MQ_ERROR_ILLEGAL_PROPERTY_VT",
    "MQ_ERROR_ILLEGAL_PROPID",
    "MQ_ERROR_ILLEGAL_QUEUE_PATHNAME",
    "MQ_ERROR_ILLEGAL_RELATION",
    "MQ_ERROR_ILLEGAL_RESTRICTION_PROPID",
    "MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR",
    "MQ_ERROR_ILLEGAL_SORT",
    "MQ_ERROR_ILLEGAL_SORT_PROPID",
    "MQ_ERROR_ILLEGAL_USER",
    "MQ_ERROR_INSUFFICIENT_PROPERTIES",
    "MQ_ERROR_INSUFFICIENT_RESOURCES",
    "MQ_ERROR_INTERNAL_USER_CERT_EXIST",
    "MQ_ERROR_INVALID_CERTIFICATE",
    "MQ_ERROR_INVALID_HANDLE",
    "MQ_ERROR_INVALID_OWNER",
    "MQ_ERROR_INVALID_PARAMETER",
    "MQ_ERROR_IO_TIMEOUT",
    "MQ_ERROR_LABEL_BUFFER_TOO_SMALL",
    "MQ_ERROR_LABEL_TOO_LONG",
    "MQ_ERROR_MACHINE_EXISTS",
    "MQ_ERROR_MACHINE_NOT_FOUND",
    "MQ_ERROR_MESSAGE_ALREADY_RECEIVED",
    "MQ_ERROR_MESSAGE_LOCKED_UNDER_TRANSACTION",
    "MQ_ERROR_MESSAGE_NOT_AUTHENTICATED",
    "MQ_ERROR_MESSAGE_NOT_FOUND",
    "MQ_ERROR_MESSAGE_STORAGE_FAILED",
    "MQ_ERROR_MISSING_CONNECTOR_TYPE",
    "MQ_ERROR_MQIS_READONLY_MODE",
    "MQ_ERROR_MQIS_SERVER_EMPTY",
    "MQ_ERROR_MULTI_SORT_KEYS",
    "MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS",
    "MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS",
    "MQ_ERROR_NO_DS",
    "MQ_ERROR_NO_ENTRY_POINT_MSMQOCM",
    "MQ_ERROR_NO_GC_IN_DOMAIN",
    "MQ_ERROR_NO_INTERNAL_USER_CERT",
    "MQ_ERROR_NO_MQUSER_OU",
    "MQ_ERROR_NO_MSMQ_SERVERS_ON_DC",
    "MQ_ERROR_NO_MSMQ_SERVERS_ON_GC",
    "MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER",
    "MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE",
    "MQ_ERROR_OPERATION_CANCELLED",
    "MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER",
    "MQ_ERROR_PRIVILEGE_NOT_HELD",
    "MQ_ERROR_PROPERTIES_CONFLICT",
    "MQ_ERROR_PROPERTY",
    "MQ_ERROR_PROPERTY_NOTALLOWED",
    "MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL",
    "MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST",
    "MQ_ERROR_PUBLIC_KEY_NOT_FOUND",
    "MQ_ERROR_QUEUE_DELETED",
    "MQ_ERROR_QUEUE_EXISTS",
    "MQ_ERROR_QUEUE_NOT_ACTIVE",
    "MQ_ERROR_QUEUE_NOT_AVAILABLE",
    "MQ_ERROR_QUEUE_NOT_FOUND",
    "MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED",
    "MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED",
    "MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE",
    "MQ_ERROR_RESOLVE_ADDRESS",
    "MQ_ERROR_RESULT_BUFFER_TOO_SMALL",
    "MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL",
    "MQ_ERROR_SENDERID_BUFFER_TOO_SMALL",
    "MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL",
    "MQ_ERROR_SERVICE_NOT_AVAILABLE",
    "MQ_ERROR_SHARING_VIOLATION",
    "MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL",
    "MQ_ERROR_STALE_HANDLE",
    "MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL",
    "MQ_ERROR_TOO_MANY_PROPERTIES",
    "MQ_ERROR_TRANSACTION_ENLIST",
    "MQ_ERROR_TRANSACTION_IMPORT",
    "MQ_ERROR_TRANSACTION_SEQUENCE",
    "MQ_ERROR_TRANSACTION_USAGE",
    "MQ_ERROR_UNINITIALIZED_OBJECT",
    "MQ_ERROR_UNSUPPORTED_ACCESS_MODE",
    "MQ_ERROR_UNSUPPORTED_CLASS",
    "MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION",
    "MQ_ERROR_UNSUPPORTED_OPERATION",
    "MQ_ERROR_USER_BUFFER_TOO_SMALL",
    "MQ_ERROR_WKS_CANT_SERVE_CLIENT",
    "MQ_ERROR_WRITE_NOT_ALLOWED",
    "MQ_INFORMATION_DUPLICATE_PROPERTY",
    "MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL",
    "MQ_INFORMATION_ILLEGAL_PROPERTY",
    "MQ_INFORMATION_INTERNAL_USER_CERT_EXIST",
    "MQ_INFORMATION_OPERATION_PENDING",
    "MQ_INFORMATION_OWNER_IGNORED",
    "MQ_INFORMATION_PROPERTY",
    "MQ_INFORMATION_PROPERTY_IGNORED",
    "MQ_INFORMATION_UNSUPPORTED_PROPERTY",
    "MQ_JOURNAL",
    "MQ_JOURNAL_NONE",
    "MQ_LOOKUP_PEEK_CURRENT",
    "MQ_LOOKUP_PEEK_FIRST",
    "MQ_LOOKUP_PEEK_LAST",
    "MQ_LOOKUP_PEEK_NEXT",
    "MQ_LOOKUP_PEEK_PREV",
    "MQ_LOOKUP_RECEIVE_ALLOW_PEEK",
    "MQ_LOOKUP_RECEIVE_CURRENT",
    "MQ_LOOKUP_RECEIVE_FIRST",
    "MQ_LOOKUP_RECEIVE_LAST",
    "MQ_LOOKUP_RECEIVE_NEXT",
    "MQ_LOOKUP_RECEIVE_PREV",
    "MQ_MAX_MSG_LABEL_LEN",
    "MQ_MAX_PRIORITY",
    "MQ_MAX_Q_LABEL_LEN",
    "MQ_MAX_Q_NAME_LEN",
    "MQ_MIN_PRIORITY",
    "MQ_MOVE_ACCESS",
    "MQ_MTS_TRANSACTION",
    "MQ_NO_TRANSACTION",
    "MQ_OK",
    "MQ_PEEK_ACCESS",
    "MQ_PRIV_LEVEL_BODY",
    "MQ_PRIV_LEVEL_NONE",
    "MQ_PRIV_LEVEL_OPTIONAL",
    "MQ_QUEUE_STATE_CONNECTED",
    "MQ_QUEUE_STATE_DISCONNECTED",
    "MQ_QUEUE_STATE_DISCONNECTING",
    "MQ_QUEUE_STATE_LOCAL_CONNECTION",
    "MQ_QUEUE_STATE_LOCKED",
    "MQ_QUEUE_STATE_NEEDVALIDATE",
    "MQ_QUEUE_STATE_NONACTIVE",
    "MQ_QUEUE_STATE_ONHOLD",
    "MQ_QUEUE_STATE_WAITING",
    "MQ_RECEIVE_ACCESS",
    "MQ_SEND_ACCESS",
    "MQ_SINGLE_MESSAGE",
    "MQ_STATUS_FOREIGN",
    "MQ_STATUS_NOT_FOREIGN",
    "MQ_STATUS_UNKNOWN",
    "MQ_TRANSACTIONAL",
    "MQ_TRANSACTIONAL_NONE",
    "MQ_TYPE_CONNECTOR",
    "MQ_TYPE_MACHINE",
    "MQ_TYPE_MULTICAST",
    "MQ_TYPE_PRIVATE",
    "MQ_TYPE_PUBLIC",
    "MQ_XACT_STATUS_NOT_XACT",
    "MQ_XACT_STATUS_UNKNOWN",
    "MQ_XACT_STATUS_XACT",
    "MQ_XA_TRANSACTION",
    "MSMQApplication",
    "MSMQCollection",
    "MSMQCoordinatedTransactionDispenser",
    "MSMQDestination",
    "MSMQEvent",
    "MSMQManagement",
    "MSMQMessage",
    "MSMQOutgoingQueueManagement",
    "MSMQQuery",
    "MSMQQueue",
    "MSMQQueueInfo",
    "MSMQQueueInfos",
    "MSMQQueueManagement",
    "MSMQTransaction",
    "MSMQTransactionDispenser",
    "MSMQ_CONNECTED",
    "MSMQ_DISCONNECTED",
    "PREQ",
    "PRGE",
    "PRGT",
    "PRLE",
    "PRLT",
    "PRNE",
    "PROPID_MGMT_MSMQ_ACTIVEQUEUES",
    "PROPID_MGMT_MSMQ_BASE",
    "PROPID_MGMT_MSMQ_BYTES_IN_ALL_QUEUES",
    "PROPID_MGMT_MSMQ_CONNECTED",
    "PROPID_MGMT_MSMQ_DSSERVER",
    "PROPID_MGMT_MSMQ_PRIVATEQ",
    "PROPID_MGMT_MSMQ_TYPE",
    "PROPID_MGMT_QUEUE_BASE",
    "PROPID_MGMT_QUEUE_BYTES_IN_JOURNAL",
    "PROPID_MGMT_QUEUE_BYTES_IN_QUEUE",
    "PROPID_MGMT_QUEUE_CONNECTION_HISTORY",
    "PROPID_MGMT_QUEUE_EOD_FIRST_NON_ACK",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK_COUNT",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK_TIME",
    "PROPID_MGMT_QUEUE_EOD_LAST_NON_ACK",
    "PROPID_MGMT_QUEUE_EOD_NEXT_SEQ",
    "PROPID_MGMT_QUEUE_EOD_NO_ACK_COUNT",
    "PROPID_MGMT_QUEUE_EOD_NO_READ_COUNT",
    "PROPID_MGMT_QUEUE_EOD_RESEND_COUNT",
    "PROPID_MGMT_QUEUE_EOD_RESEND_INTERVAL",
    "PROPID_MGMT_QUEUE_EOD_RESEND_TIME",
    "PROPID_MGMT_QUEUE_EOD_SOURCE_INFO",
    "PROPID_MGMT_QUEUE_FOREIGN",
    "PROPID_MGMT_QUEUE_FORMATNAME",
    "PROPID_MGMT_QUEUE_JOURNAL_MESSAGE_COUNT",
    "PROPID_MGMT_QUEUE_JOURNAL_USED_QUOTA",
    "PROPID_MGMT_QUEUE_LOCATION",
    "PROPID_MGMT_QUEUE_MESSAGE_COUNT",
    "PROPID_MGMT_QUEUE_NEXTHOPS",
    "PROPID_MGMT_QUEUE_PATHNAME",
    "PROPID_MGMT_QUEUE_STATE",
    "PROPID_MGMT_QUEUE_SUBQUEUE_COUNT",
    "PROPID_MGMT_QUEUE_SUBQUEUE_NAMES",
    "PROPID_MGMT_QUEUE_TYPE",
    "PROPID_MGMT_QUEUE_USED_QUOTA",
    "PROPID_MGMT_QUEUE_XACT",
    "PROPID_M_ABORT_COUNT",
    "PROPID_M_ACKNOWLEDGE",
    "PROPID_M_ADMIN_QUEUE",
    "PROPID_M_ADMIN_QUEUE_LEN",
    "PROPID_M_APPSPECIFIC",
    "PROPID_M_ARRIVEDTIME",
    "PROPID_M_AUTHENTICATED",
    "PROPID_M_AUTHENTICATED_EX",
    "PROPID_M_AUTH_LEVEL",
    "PROPID_M_BASE",
    "PROPID_M_BODY",
    "PROPID_M_BODY_SIZE",
    "PROPID_M_BODY_TYPE",
    "PROPID_M_CLASS",
    "PROPID_M_COMPOUND_MESSAGE",
    "PROPID_M_COMPOUND_MESSAGE_SIZE",
    "PROPID_M_CONNECTOR_TYPE",
    "PROPID_M_CORRELATIONID",
    "PROPID_M_CORRELATIONID_SIZE",
    "PROPID_M_DEADLETTER_QUEUE",
    "PROPID_M_DEADLETTER_QUEUE_LEN",
    "PROPID_M_DELIVERY",
    "PROPID_M_DEST_FORMAT_NAME",
    "PROPID_M_DEST_FORMAT_NAME_LEN",
    "PROPID_M_DEST_QUEUE",
    "PROPID_M_DEST_QUEUE_LEN",
    "PROPID_M_DEST_SYMM_KEY",
    "PROPID_M_DEST_SYMM_KEY_LEN",
    "PROPID_M_ENCRYPTION_ALG",
    "PROPID_M_EXTENSION",
    "PROPID_M_EXTENSION_LEN",
    "PROPID_M_FIRST_IN_XACT",
    "PROPID_M_HASH_ALG",
    "PROPID_M_JOURNAL",
    "PROPID_M_LABEL",
    "PROPID_M_LABEL_LEN",
    "PROPID_M_LAST_IN_XACT",
    "PROPID_M_LAST_MOVE_TIME",
    "PROPID_M_LOOKUPID",
    "PROPID_M_MOVE_COUNT",
    "PROPID_M_MSGID",
    "PROPID_M_MSGID_SIZE",
    "PROPID_M_PRIORITY",
    "PROPID_M_PRIV_LEVEL",
    "PROPID_M_PROV_NAME",
    "PROPID_M_PROV_NAME_LEN",
    "PROPID_M_PROV_TYPE",
    "PROPID_M_RESP_FORMAT_NAME",
    "PROPID_M_RESP_FORMAT_NAME_LEN",
    "PROPID_M_RESP_QUEUE",
    "PROPID_M_RESP_QUEUE_LEN",
    "PROPID_M_SECURITY_CONTEXT",
    "PROPID_M_SENDERID",
    "PROPID_M_SENDERID_LEN",
    "PROPID_M_SENDERID_TYPE",
    "PROPID_M_SENDER_CERT",
    "PROPID_M_SENDER_CERT_LEN",
    "PROPID_M_SENTTIME",
    "PROPID_M_SIGNATURE",
    "PROPID_M_SIGNATURE_LEN",
    "PROPID_M_SOAP_BODY",
    "PROPID_M_SOAP_ENVELOPE",
    "PROPID_M_SOAP_ENVELOPE_LEN",
    "PROPID_M_SOAP_HEADER",
    "PROPID_M_SRC_MACHINE_ID",
    "PROPID_M_TIME_TO_BE_RECEIVED",
    "PROPID_M_TIME_TO_REACH_QUEUE",
    "PROPID_M_TRACE",
    "PROPID_M_VERSION",
    "PROPID_M_XACTID",
    "PROPID_M_XACTID_SIZE",
    "PROPID_M_XACT_STATUS_QUEUE",
    "PROPID_M_XACT_STATUS_QUEUE_LEN",
    "PROPID_PC_BASE",
    "PROPID_PC_DS_ENABLED",
    "PROPID_PC_VERSION",
    "PROPID_QM_BASE",
    "PROPID_QM_CONNECTION",
    "PROPID_QM_ENCRYPTION_PK",
    "PROPID_QM_ENCRYPTION_PK_AES",
    "PROPID_QM_ENCRYPTION_PK_BASE",
    "PROPID_QM_ENCRYPTION_PK_ENHANCED",
    "PROPID_QM_MACHINE_ID",
    "PROPID_QM_PATHNAME",
    "PROPID_QM_PATHNAME_DNS",
    "PROPID_QM_SITE_ID",
    "PROPID_Q_ADS_PATH",
    "PROPID_Q_AUTHENTICATE",
    "PROPID_Q_BASE",
    "PROPID_Q_BASEPRIORITY",
    "PROPID_Q_CREATE_TIME",
    "PROPID_Q_INSTANCE",
    "PROPID_Q_JOURNAL",
    "PROPID_Q_JOURNAL_QUOTA",
    "PROPID_Q_LABEL",
    "PROPID_Q_MODIFY_TIME",
    "PROPID_Q_MULTICAST_ADDRESS",
    "PROPID_Q_PATHNAME",
    "PROPID_Q_PATHNAME_DNS",
    "PROPID_Q_PRIV_LEVEL",
    "PROPID_Q_QUOTA",
    "PROPID_Q_TRANSACTION",
    "PROPID_Q_TYPE",
    "QUERY_SORTASCEND",
    "QUERY_SORTDESCEND",
    "QUEUE_ACTION_EOD_RESEND",
    "QUEUE_ACTION_PAUSE",
    "QUEUE_ACTION_RESUME",
    "QUEUE_STATE",
    "QUEUE_TYPE",
    "RELOPS",
    "REL_EQ",
    "REL_GE",
    "REL_GT",
    "REL_LE",
    "REL_LT",
    "REL_NEQ",
    "REL_NOP",
    "XACT_STATUS",
    "_DMSMQEventEvents",
]
