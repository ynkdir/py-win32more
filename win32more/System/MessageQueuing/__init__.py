from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.MessageQueuing

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
PRLT = 0
PRLE = 1
PRGT = 2
PRGE = 3
PREQ = 4
PRNE = 5
QUERY_SORTASCEND = 0
QUERY_SORTDESCEND = 1
MQ_MOVE_ACCESS = 4
MQ_ACTION_RECEIVE = 0
MQ_ACTION_PEEK_CURRENT = 2147483648
MQ_ACTION_PEEK_NEXT = 2147483649
MQ_LOOKUP_PEEK_CURRENT = 1073741840
MQ_LOOKUP_PEEK_NEXT = 1073741841
MQ_LOOKUP_PEEK_PREV = 1073741842
MQ_LOOKUP_PEEK_FIRST = 1073741844
MQ_LOOKUP_PEEK_LAST = 1073741848
MQ_LOOKUP_RECEIVE_CURRENT = 1073741856
MQ_LOOKUP_RECEIVE_NEXT = 1073741857
MQ_LOOKUP_RECEIVE_PREV = 1073741858
MQ_LOOKUP_RECEIVE_FIRST = 1073741860
MQ_LOOKUP_RECEIVE_LAST = 1073741864
MQ_LOOKUP_RECEIVE_ALLOW_PEEK = 1073742112
PROPID_M_BASE = 0
PROPID_M_CLASS = 1
PROPID_M_MSGID = 2
PROPID_M_CORRELATIONID = 3
PROPID_M_PRIORITY = 4
PROPID_M_DELIVERY = 5
PROPID_M_ACKNOWLEDGE = 6
PROPID_M_JOURNAL = 7
PROPID_M_APPSPECIFIC = 8
PROPID_M_BODY = 9
PROPID_M_BODY_SIZE = 10
PROPID_M_LABEL = 11
PROPID_M_LABEL_LEN = 12
PROPID_M_TIME_TO_REACH_QUEUE = 13
PROPID_M_TIME_TO_BE_RECEIVED = 14
PROPID_M_RESP_QUEUE = 15
PROPID_M_RESP_QUEUE_LEN = 16
PROPID_M_ADMIN_QUEUE = 17
PROPID_M_ADMIN_QUEUE_LEN = 18
PROPID_M_VERSION = 19
PROPID_M_SENDERID = 20
PROPID_M_SENDERID_LEN = 21
PROPID_M_SENDERID_TYPE = 22
PROPID_M_PRIV_LEVEL = 23
PROPID_M_AUTH_LEVEL = 24
PROPID_M_AUTHENTICATED = 25
PROPID_M_HASH_ALG = 26
PROPID_M_ENCRYPTION_ALG = 27
PROPID_M_SENDER_CERT = 28
PROPID_M_SENDER_CERT_LEN = 29
PROPID_M_SRC_MACHINE_ID = 30
PROPID_M_SENTTIME = 31
PROPID_M_ARRIVEDTIME = 32
PROPID_M_DEST_QUEUE = 33
PROPID_M_DEST_QUEUE_LEN = 34
PROPID_M_EXTENSION = 35
PROPID_M_EXTENSION_LEN = 36
PROPID_M_SECURITY_CONTEXT = 37
PROPID_M_CONNECTOR_TYPE = 38
PROPID_M_XACT_STATUS_QUEUE = 39
PROPID_M_XACT_STATUS_QUEUE_LEN = 40
PROPID_M_TRACE = 41
PROPID_M_BODY_TYPE = 42
PROPID_M_DEST_SYMM_KEY = 43
PROPID_M_DEST_SYMM_KEY_LEN = 44
PROPID_M_SIGNATURE = 45
PROPID_M_SIGNATURE_LEN = 46
PROPID_M_PROV_TYPE = 47
PROPID_M_PROV_NAME = 48
PROPID_M_PROV_NAME_LEN = 49
PROPID_M_FIRST_IN_XACT = 50
PROPID_M_LAST_IN_XACT = 51
PROPID_M_XACTID = 52
PROPID_M_AUTHENTICATED_EX = 53
PROPID_M_RESP_FORMAT_NAME = 54
PROPID_M_RESP_FORMAT_NAME_LEN = 55
PROPID_M_DEST_FORMAT_NAME = 58
PROPID_M_DEST_FORMAT_NAME_LEN = 59
PROPID_M_LOOKUPID = 60
PROPID_M_SOAP_ENVELOPE = 61
PROPID_M_SOAP_ENVELOPE_LEN = 62
PROPID_M_COMPOUND_MESSAGE = 63
PROPID_M_COMPOUND_MESSAGE_SIZE = 64
PROPID_M_SOAP_HEADER = 65
PROPID_M_SOAP_BODY = 66
PROPID_M_DEADLETTER_QUEUE = 67
PROPID_M_DEADLETTER_QUEUE_LEN = 68
PROPID_M_ABORT_COUNT = 69
PROPID_M_MOVE_COUNT = 70
PROPID_M_LAST_MOVE_TIME = 75
PROPID_M_MSGID_SIZE = 20
PROPID_M_CORRELATIONID_SIZE = 20
PROPID_M_XACTID_SIZE = 20
MQMSG_PRIV_LEVEL_BODY_AES = 5
MQMSG_AUTHENTICATED_QM_MESSAGE = 11
MQMSG_NOT_FIRST_IN_XACT = 0
MQMSG_FIRST_IN_XACT = 1
MQMSG_NOT_LAST_IN_XACT = 0
MQMSG_LAST_IN_XACT = 1
PROPID_Q_BASE = 100
PROPID_Q_INSTANCE = 101
PROPID_Q_TYPE = 102
PROPID_Q_PATHNAME = 103
PROPID_Q_JOURNAL = 104
PROPID_Q_QUOTA = 105
PROPID_Q_BASEPRIORITY = 106
PROPID_Q_JOURNAL_QUOTA = 107
PROPID_Q_LABEL = 108
PROPID_Q_CREATE_TIME = 109
PROPID_Q_MODIFY_TIME = 110
PROPID_Q_AUTHENTICATE = 111
PROPID_Q_PRIV_LEVEL = 112
PROPID_Q_TRANSACTION = 113
PROPID_Q_PATHNAME_DNS = 124
PROPID_Q_MULTICAST_ADDRESS = 125
PROPID_Q_ADS_PATH = 126
PROPID_QM_BASE = 200
PROPID_QM_SITE_ID = 201
PROPID_QM_MACHINE_ID = 202
PROPID_QM_PATHNAME = 203
PROPID_QM_CONNECTION = 204
PROPID_QM_ENCRYPTION_PK = 205
PROPID_QM_ENCRYPTION_PK_BASE = 231
PROPID_QM_ENCRYPTION_PK_ENHANCED = 232
PROPID_QM_PATHNAME_DNS = 233
PROPID_QM_ENCRYPTION_PK_AES = 244
PROPID_PC_BASE = 5800
PROPID_PC_VERSION = 5801
PROPID_PC_DS_ENABLED = 5802
PROPID_MGMT_MSMQ_BASE = 0
PROPID_MGMT_MSMQ_ACTIVEQUEUES = 1
PROPID_MGMT_MSMQ_PRIVATEQ = 2
PROPID_MGMT_MSMQ_DSSERVER = 3
PROPID_MGMT_MSMQ_CONNECTED = 4
PROPID_MGMT_MSMQ_TYPE = 5
PROPID_MGMT_MSMQ_BYTES_IN_ALL_QUEUES = 6
PROPID_MGMT_QUEUE_BASE = 0
PROPID_MGMT_QUEUE_PATHNAME = 1
PROPID_MGMT_QUEUE_FORMATNAME = 2
PROPID_MGMT_QUEUE_TYPE = 3
PROPID_MGMT_QUEUE_LOCATION = 4
PROPID_MGMT_QUEUE_XACT = 5
PROPID_MGMT_QUEUE_FOREIGN = 6
PROPID_MGMT_QUEUE_MESSAGE_COUNT = 7
PROPID_MGMT_QUEUE_BYTES_IN_QUEUE = 8
PROPID_MGMT_QUEUE_JOURNAL_MESSAGE_COUNT = 9
PROPID_MGMT_QUEUE_BYTES_IN_JOURNAL = 10
PROPID_MGMT_QUEUE_STATE = 11
PROPID_MGMT_QUEUE_NEXTHOPS = 12
PROPID_MGMT_QUEUE_EOD_LAST_ACK = 13
PROPID_MGMT_QUEUE_EOD_LAST_ACK_TIME = 14
PROPID_MGMT_QUEUE_EOD_LAST_ACK_COUNT = 15
PROPID_MGMT_QUEUE_EOD_FIRST_NON_ACK = 16
PROPID_MGMT_QUEUE_EOD_LAST_NON_ACK = 17
PROPID_MGMT_QUEUE_EOD_NEXT_SEQ = 18
PROPID_MGMT_QUEUE_EOD_NO_READ_COUNT = 19
PROPID_MGMT_QUEUE_EOD_NO_ACK_COUNT = 20
PROPID_MGMT_QUEUE_EOD_RESEND_TIME = 21
PROPID_MGMT_QUEUE_EOD_RESEND_INTERVAL = 22
PROPID_MGMT_QUEUE_EOD_RESEND_COUNT = 23
PROPID_MGMT_QUEUE_EOD_SOURCE_INFO = 24
PROPID_MGMT_QUEUE_CONNECTION_HISTORY = 25
PROPID_MGMT_QUEUE_SUBQUEUE_COUNT = 26
PROPID_MGMT_QUEUE_SUBQUEUE_NAMES = 27
PROPID_MGMT_QUEUE_USED_QUOTA = 8
PROPID_MGMT_QUEUE_JOURNAL_USED_QUOTA = 10
LONG_LIVED = 4294967294
MQSEC_DELETE_MESSAGE = 1
MQSEC_PEEK_MESSAGE = 2
MQSEC_WRITE_MESSAGE = 4
MQSEC_DELETE_JOURNAL_MESSAGE = 8
MQSEC_SET_QUEUE_PROPERTIES = 16
MQSEC_GET_QUEUE_PROPERTIES = 32
MQSEC_DELETE_QUEUE = 65536
MQSEC_CHANGE_QUEUE_PERMISSIONS = 262144
MQSEC_TAKE_QUEUE_OWNERSHIP = 524288
MQSEC_QUEUE_GENERIC_EXECUTE = 0
MQ_OK = 0
MQ_ERROR_RESOLVE_ADDRESS = -1072824167
MQ_ERROR_TOO_MANY_PROPERTIES = -1072824166
MQ_ERROR_MESSAGE_NOT_AUTHENTICATED = -1072824165
MQ_ERROR_MESSAGE_LOCKED_UNDER_TRANSACTION = -1072824164
MSMQQuery = Guid('d7d6e073-dccd-11d0-aa4b-0060970debae')
MSMQMessage = Guid('d7d6e075-dccd-11d0-aa4b-0060970debae')
MSMQQueue = Guid('d7d6e079-dccd-11d0-aa4b-0060970debae')
MSMQEvent = Guid('d7d6e07a-dccd-11d0-aa4b-0060970debae')
MSMQQueueInfo = Guid('d7d6e07c-dccd-11d0-aa4b-0060970debae')
MSMQQueueInfos = Guid('d7d6e07e-dccd-11d0-aa4b-0060970debae')
MSMQTransaction = Guid('d7d6e080-dccd-11d0-aa4b-0060970debae')
MSMQCoordinatedTransactionDispenser = Guid('d7d6e082-dccd-11d0-aa4b-0060970debae')
MSMQTransactionDispenser = Guid('d7d6e084-dccd-11d0-aa4b-0060970debae')
MSMQApplication = Guid('d7d6e086-dccd-11d0-aa4b-0060970debae')
MSMQDestination = Guid('eba96b18-2168-11d3-898c-00e02c074f6b')
MSMQCollection = Guid('f72b9031-2f0c-43e8-924e-e6052cdc493f')
MSMQManagement = Guid('39ce96fe-f4c5-4484-a143-4c2d5d324229')
MSMQOutgoingQueueManagement = Guid('0188401c-247a-4fed-99c6-bf14119d7055')
MSMQQueueManagement = Guid('33b6d07e-f27d-42fa-b2d7-bf82e11e9374')
MQCALG = Int32
MQMSG_CALG_MD2 = 32769
MQMSG_CALG_MD4 = 32770
MQMSG_CALG_MD5 = 32771
MQMSG_CALG_SHA = 32772
MQMSG_CALG_SHA1 = 32772
MQMSG_CALG_MAC = 32773
MQMSG_CALG_RSA_SIGN = 9216
MQMSG_CALG_DSS_SIGN = 8704
MQMSG_CALG_RSA_KEYX = 41984
MQMSG_CALG_DES = 26113
MQMSG_CALG_RC2 = 26114
MQMSG_CALG_RC4 = 26625
MQMSG_CALG_SEAL = 26626
MQTRANSACTION = Int32
MQ_NO_TRANSACTION = 0
MQ_MTS_TRANSACTION = 1
MQ_XA_TRANSACTION = 2
MQ_SINGLE_MESSAGE = 3
RELOPS = Int32
REL_NOP = 0
REL_EQ = 1
REL_NEQ = 2
REL_LT = 3
REL_GT = 4
REL_LE = 5
REL_GE = 6
MQCERT_REGISTER = Int32
MQCERT_REGISTER_ALWAYS = 1
MQCERT_REGISTER_IF_NOT_EXIST = 2
MQMSGCURSOR = Int32
MQMSG_FIRST = 0
MQMSG_CURRENT = 1
MQMSG_NEXT = 2
MQMSGCLASS = Int32
MQMSG_CLASS_NORMAL = 0
MQMSG_CLASS_REPORT = 1
MQMSG_CLASS_ACK_REACH_QUEUE = 2
MQMSG_CLASS_ACK_RECEIVE = 16384
MQMSG_CLASS_NACK_BAD_DST_Q = 32768
MQMSG_CLASS_NACK_PURGED = 32769
MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT = 32770
MQMSG_CLASS_NACK_Q_EXCEED_QUOTA = 32771
MQMSG_CLASS_NACK_ACCESS_DENIED = 32772
MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED = 32773
MQMSG_CLASS_NACK_BAD_SIGNATURE = 32774
MQMSG_CLASS_NACK_BAD_ENCRYPTION = 32775
MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT = 32776
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q = 32777
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG = 32778
MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER = 32779
MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED = 32780
MQMSG_CLASS_NACK_Q_DELETED = 49152
MQMSG_CLASS_NACK_Q_PURGED = 49153
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT = 49154
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER = 49155
MQMSGDELIVERY = Int32
MQMSG_DELIVERY_EXPRESS = 0
MQMSG_DELIVERY_RECOVERABLE = 1
MQMSGACKNOWLEDGEMENT = Int32
MQMSG_ACKNOWLEDGMENT_NONE = 0
MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL = 1
MQMSG_ACKNOWLEDGMENT_POS_RECEIVE = 2
MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL = 4
MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE = 8
MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE = 4
MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE = 5
MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE = 12
MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE = 14
MQMSGJOURNAL = Int32
MQMSG_JOURNAL_NONE = 0
MQMSG_DEADLETTER = 1
MQMSG_JOURNAL = 2
MQMSGTRACE = Int32
MQMSG_TRACE_NONE = 0
MQMSG_SEND_ROUTE_TO_REPORT_QUEUE = 1
MQMSGSENDERIDTYPE = Int32
MQMSG_SENDERID_TYPE_NONE = 0
MQMSG_SENDERID_TYPE_SID = 1
MQMSGPRIVLEVEL = Int32
MQMSG_PRIV_LEVEL_NONE = 0
MQMSG_PRIV_LEVEL_BODY_BASE = 1
MQMSG_PRIV_LEVEL_BODY_ENHANCED = 3
MQMSGAUTHLEVEL = Int32
MQMSG_AUTH_LEVEL_NONE = 0
MQMSG_AUTH_LEVEL_ALWAYS = 1
MQMSG_AUTH_LEVEL_MSMQ10 = 2
MQMSG_AUTH_LEVEL_SIG10 = 2
MQMSG_AUTH_LEVEL_MSMQ20 = 4
MQMSG_AUTH_LEVEL_SIG20 = 4
MQMSG_AUTH_LEVEL_SIG30 = 8
MQMSGIDSIZE = Int32
MQMSG_MSGID_SIZE = 20
MQMSG_CORRELATIONID_SIZE = 20
MQMSG_XACTID_SIZE = 20
MQMSGMAX = Int32
MQ_MAX_MSG_LABEL_LEN = 249
MQMSGAUTHENTICATION = Int32
MQMSG_AUTHENTICATION_NOT_REQUESTED = 0
MQMSG_AUTHENTICATION_REQUESTED = 1
MQMSG_AUTHENTICATED_SIG10 = 1
MQMSG_AUTHENTICATION_REQUESTED_EX = 3
MQMSG_AUTHENTICATED_SIG20 = 3
MQMSG_AUTHENTICATED_SIG30 = 5
MQMSG_AUTHENTICATED_SIGXML = 9
MQSHARE = Int32
MQ_DENY_NONE = 0
MQ_DENY_RECEIVE_SHARE = 1
MQACCESS = Int32
MQ_RECEIVE_ACCESS = 1
MQ_SEND_ACCESS = 2
MQ_PEEK_ACCESS = 32
MQ_ADMIN_ACCESS = 128
MQJOURNAL = Int32
MQ_JOURNAL_NONE = 0
MQ_JOURNAL = 1
MQTRANSACTIONAL = Int32
MQ_TRANSACTIONAL_NONE = 0
MQ_TRANSACTIONAL = 1
MQAUTHENTICATE = Int32
MQ_AUTHENTICATE_NONE = 0
MQ_AUTHENTICATE = 1
MQPRIVLEVEL = Int32
MQ_PRIV_LEVEL_NONE = 0
MQ_PRIV_LEVEL_OPTIONAL = 1
MQ_PRIV_LEVEL_BODY = 2
MQPRIORITY = Int32
MQ_MIN_PRIORITY = 0
MQ_MAX_PRIORITY = 7
MQMAX = Int32
MQ_MAX_Q_NAME_LEN = 124
MQ_MAX_Q_LABEL_LEN = 124
QUEUE_TYPE = Int32
MQ_TYPE_PUBLIC = 0
MQ_TYPE_PRIVATE = 1
MQ_TYPE_MACHINE = 2
MQ_TYPE_CONNECTOR = 3
MQ_TYPE_MULTICAST = 4
FOREIGN_STATUS = Int32
MQ_STATUS_FOREIGN = 0
MQ_STATUS_NOT_FOREIGN = 1
MQ_STATUS_UNKNOWN = 2
XACT_STATUS = Int32
MQ_XACT_STATUS_XACT = 0
MQ_XACT_STATUS_NOT_XACT = 1
MQ_XACT_STATUS_UNKNOWN = 2
QUEUE_STATE = Int32
MQ_QUEUE_STATE_LOCAL_CONNECTION = 0
MQ_QUEUE_STATE_DISCONNECTED = 1
MQ_QUEUE_STATE_WAITING = 2
MQ_QUEUE_STATE_NEEDVALIDATE = 3
MQ_QUEUE_STATE_ONHOLD = 4
MQ_QUEUE_STATE_NONACTIVE = 5
MQ_QUEUE_STATE_CONNECTED = 6
MQ_QUEUE_STATE_DISCONNECTING = 7
MQ_QUEUE_STATE_LOCKED = 8
MQDEFAULT = Int32
DEFAULT_M_PRIORITY = 3
DEFAULT_M_DELIVERY = 0
DEFAULT_M_ACKNOWLEDGE = 0
DEFAULT_M_JOURNAL = 0
DEFAULT_M_APPSPECIFIC = 0
DEFAULT_M_PRIV_LEVEL = 0
DEFAULT_M_AUTH_LEVEL = 0
DEFAULT_M_SENDERID_TYPE = 1
DEFAULT_Q_JOURNAL = 0
DEFAULT_Q_BASEPRIORITY = 0
DEFAULT_Q_QUOTA = -1
DEFAULT_Q_JOURNAL_QUOTA = -1
DEFAULT_Q_TRANSACTION = 0
DEFAULT_Q_AUTHENTICATE = 0
DEFAULT_Q_PRIV_LEVEL = 1
DEFAULT_M_LOOKUPID = 0
MQERROR = Int32
MQ_ERROR = -1072824319
MQ_ERROR_PROPERTY = -1072824318
MQ_ERROR_QUEUE_NOT_FOUND = -1072824317
MQ_ERROR_QUEUE_NOT_ACTIVE = -1072824316
MQ_ERROR_QUEUE_EXISTS = -1072824315
MQ_ERROR_INVALID_PARAMETER = -1072824314
MQ_ERROR_INVALID_HANDLE = -1072824313
MQ_ERROR_OPERATION_CANCELLED = -1072824312
MQ_ERROR_SHARING_VIOLATION = -1072824311
MQ_ERROR_SERVICE_NOT_AVAILABLE = -1072824309
MQ_ERROR_MACHINE_NOT_FOUND = -1072824307
MQ_ERROR_ILLEGAL_SORT = -1072824304
MQ_ERROR_ILLEGAL_USER = -1072824303
MQ_ERROR_NO_DS = -1072824301
MQ_ERROR_ILLEGAL_QUEUE_PATHNAME = -1072824300
MQ_ERROR_ILLEGAL_PROPERTY_VALUE = -1072824296
MQ_ERROR_ILLEGAL_PROPERTY_VT = -1072824295
MQ_ERROR_BUFFER_OVERFLOW = -1072824294
MQ_ERROR_IO_TIMEOUT = -1072824293
MQ_ERROR_ILLEGAL_CURSOR_ACTION = -1072824292
MQ_ERROR_MESSAGE_ALREADY_RECEIVED = -1072824291
MQ_ERROR_ILLEGAL_FORMATNAME = -1072824290
MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL = -1072824289
MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION = -1072824288
MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR = -1072824287
MQ_ERROR_SENDERID_BUFFER_TOO_SMALL = -1072824286
MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL = -1072824285
MQ_ERROR_CANNOT_IMPERSONATE_CLIENT = -1072824284
MQ_ERROR_ACCESS_DENIED = -1072824283
MQ_ERROR_PRIVILEGE_NOT_HELD = -1072824282
MQ_ERROR_INSUFFICIENT_RESOURCES = -1072824281
MQ_ERROR_USER_BUFFER_TOO_SMALL = -1072824280
MQ_ERROR_MESSAGE_STORAGE_FAILED = -1072824278
MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL = -1072824277
MQ_ERROR_INVALID_CERTIFICATE = -1072824276
MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE = -1072824275
MQ_ERROR_INTERNAL_USER_CERT_EXIST = -1072824274
MQ_ERROR_NO_INTERNAL_USER_CERT = -1072824273
MQ_ERROR_CORRUPTED_SECURITY_DATA = -1072824272
MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE = -1072824271
MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION = -1072824269
MQ_ERROR_BAD_SECURITY_CONTEXT = -1072824267
MQ_ERROR_COULD_NOT_GET_USER_SID = -1072824266
MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO = -1072824265
MQ_ERROR_ILLEGAL_MQCOLUMNS = -1072824264
MQ_ERROR_ILLEGAL_PROPID = -1072824263
MQ_ERROR_ILLEGAL_RELATION = -1072824262
MQ_ERROR_ILLEGAL_PROPERTY_SIZE = -1072824261
MQ_ERROR_ILLEGAL_RESTRICTION_PROPID = -1072824260
MQ_ERROR_ILLEGAL_MQQUEUEPROPS = -1072824259
MQ_ERROR_PROPERTY_NOTALLOWED = -1072824258
MQ_ERROR_INSUFFICIENT_PROPERTIES = -1072824257
MQ_ERROR_MACHINE_EXISTS = -1072824256
MQ_ERROR_ILLEGAL_MQQMPROPS = -1072824255
MQ_ERROR_DS_IS_FULL = -1072824254
MQ_ERROR_DS_ERROR = -1072824253
MQ_ERROR_INVALID_OWNER = -1072824252
MQ_ERROR_UNSUPPORTED_ACCESS_MODE = -1072824251
MQ_ERROR_RESULT_BUFFER_TOO_SMALL = -1072824250
MQ_ERROR_DELETE_CN_IN_USE = -1072824248
MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER = -1072824247
MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE = -1072824246
MQ_ERROR_QUEUE_NOT_AVAILABLE = -1072824245
MQ_ERROR_DTC_CONNECT = -1072824244
MQ_ERROR_TRANSACTION_IMPORT = -1072824242
MQ_ERROR_TRANSACTION_USAGE = -1072824240
MQ_ERROR_TRANSACTION_SEQUENCE = -1072824239
MQ_ERROR_MISSING_CONNECTOR_TYPE = -1072824235
MQ_ERROR_STALE_HANDLE = -1072824234
MQ_ERROR_TRANSACTION_ENLIST = -1072824232
MQ_ERROR_QUEUE_DELETED = -1072824230
MQ_ERROR_ILLEGAL_CONTEXT = -1072824229
MQ_ERROR_ILLEGAL_SORT_PROPID = -1072824228
MQ_ERROR_LABEL_TOO_LONG = -1072824227
MQ_ERROR_LABEL_BUFFER_TOO_SMALL = -1072824226
MQ_ERROR_MQIS_SERVER_EMPTY = -1072824225
MQ_ERROR_MQIS_READONLY_MODE = -1072824224
MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL = -1072824223
MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL = -1072824222
MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL = -1072824221
MQ_ERROR_ILLEGAL_OPERATION = -1072824220
MQ_ERROR_WRITE_NOT_ALLOWED = -1072824219
MQ_ERROR_WKS_CANT_SERVE_CLIENT = -1072824218
MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW = -1072824217
MQ_CORRUPTED_QUEUE_WAS_DELETED = -1072824216
MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE = -1072824215
MQ_ERROR_UNSUPPORTED_OPERATION = -1072824214
MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED = -1072824213
MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR = -1072824212
MQ_ERROR_CERTIFICATE_NOT_PROVIDED = -1072824211
MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED = -1072824210
MQ_ERROR_CANT_CREATE_CERT_STORE = -1072824209
MQ_ERROR_CANNOT_CREATE_CERT_STORE = -1072824209
MQ_ERROR_CANT_OPEN_CERT_STORE = -1072824208
MQ_ERROR_CANNOT_OPEN_CERT_STORE = -1072824208
MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION = -1072824207
MQ_ERROR_CANNOT_GRANT_ADD_GUID = -1072824206
MQ_ERROR_CANNOT_LOAD_MSMQOCM = -1072824205
MQ_ERROR_NO_ENTRY_POINT_MSMQOCM = -1072824204
MQ_ERROR_NO_MSMQ_SERVERS_ON_DC = -1072824203
MQ_ERROR_CANNOT_JOIN_DOMAIN = -1072824202
MQ_ERROR_CANNOT_CREATE_ON_GC = -1072824201
MQ_ERROR_GUID_NOT_MATCHING = -1072824200
MQ_ERROR_PUBLIC_KEY_NOT_FOUND = -1072824199
MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST = -1072824198
MQ_ERROR_ILLEGAL_MQPRIVATEPROPS = -1072824197
MQ_ERROR_NO_GC_IN_DOMAIN = -1072824196
MQ_ERROR_NO_MSMQ_SERVERS_ON_GC = -1072824195
MQ_ERROR_CANNOT_GET_DN = -1072824194
MQ_ERROR_CANNOT_HASH_DATA_EX = -1072824193
MQ_ERROR_CANNOT_SIGN_DATA_EX = -1072824192
MQ_ERROR_CANNOT_CREATE_HASH_EX = -1072824191
MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX = -1072824190
MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS = -1072824189
MQ_ERROR_NO_MQUSER_OU = -1072824188
MQ_ERROR_CANNOT_LOAD_MQAD = -1072824187
MQ_ERROR_CANNOT_LOAD_MQDSSRV = -1072824186
MQ_ERROR_PROPERTIES_CONFLICT = -1072824185
MQ_ERROR_MESSAGE_NOT_FOUND = -1072824184
MQ_ERROR_CANT_RESOLVE_SITES = -1072824183
MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS = -1072824182
MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER = -1072824181
MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS = -1072824180
MQ_ERROR_MULTI_SORT_KEYS = -1072824179
MQ_ERROR_GC_NEEDED = -1072824178
MQ_ERROR_DS_BIND_ROOT_FOREST = -1072824177
MQ_ERROR_DS_LOCAL_USER = -1072824176
MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED = -1072824175
MQ_ERROR_BAD_XML_FORMAT = -1072824174
MQ_ERROR_UNSUPPORTED_CLASS = -1072824173
MQ_ERROR_UNINITIALIZED_OBJECT = -1072824172
MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS = -1072824171
MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS = -1072824170
MQWARNING = Int32
MQ_INFORMATION_PROPERTY = 1074659329
MQ_INFORMATION_ILLEGAL_PROPERTY = 1074659330
MQ_INFORMATION_PROPERTY_IGNORED = 1074659331
MQ_INFORMATION_UNSUPPORTED_PROPERTY = 1074659332
MQ_INFORMATION_DUPLICATE_PROPERTY = 1074659333
MQ_INFORMATION_OPERATION_PENDING = 1074659334
MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL = 1074659337
MQ_INFORMATION_INTERNAL_USER_CERT_EXIST = 1074659338
MQ_INFORMATION_OWNER_IGNORED = 1074659339
def _define_IMSMQQuery_head():
    class IMSMQQuery(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e072-dccd-11d0-aa4b-0060970debae')
    return IMSMQQuery
def _define_IMSMQQuery():
    IMSMQQuery = win32more.System.MessageQueuing.IMSMQQuery_head
    IMSMQQuery.LookupQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos_head), use_last_error=False)(7, 'LookupQueue', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'ppqinfos'),)))
    win32more.System.Com.IDispatch
    return IMSMQQuery
def _define_IMSMQQueueInfo_head():
    class IMSMQQueueInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e07b-dccd-11d0-aa4b-0060970debae')
    return IMSMQQueueInfo
def _define_IMSMQQueueInfo():
    IMSMQQueueInfo = win32more.System.MessageQueuing.IMSMQQueueInfo_head
    IMSMQQueueInfo.get_QueueGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_QueueGuid', ((1, 'pbstrGuidQueue'),)))
    IMSMQQueueInfo.get_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServiceTypeGuid', ((1, 'pbstrGuidServiceType'),)))
    IMSMQQueueInfo.put_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_ServiceTypeGuid', ((1, 'bstrGuidServiceType'),)))
    IMSMQQueueInfo.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQQueueInfo.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQQueueInfo.get_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_PathName', ((1, 'pbstrPathName'),)))
    IMSMQQueueInfo.put_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_PathName', ((1, 'bstrPathName'),)))
    IMSMQQueueInfo.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQQueueInfo.put_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_FormatName', ((1, 'bstrFormatName'),)))
    IMSMQQueueInfo.get_IsTransactional = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsTransactional', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQQueueInfo.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQQueueInfo.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQQueueInfo.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQQueueInfo.get_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_Quota', ((1, 'plQuota'),)))
    IMSMQQueueInfo.put_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_Quota', ((1, 'lQuota'),)))
    IMSMQQueueInfo.get_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_BasePriority', ((1, 'plBasePriority'),)))
    IMSMQQueueInfo.put_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_BasePriority', ((1, 'lBasePriority'),)))
    IMSMQQueueInfo.get_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_CreateTime', ((1, 'pvarCreateTime'),)))
    IMSMQQueueInfo.get_ModifyTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_ModifyTime', ((1, 'pvarModifyTime'),)))
    IMSMQQueueInfo.get_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_Authenticate', ((1, 'plAuthenticate'),)))
    IMSMQQueueInfo.put_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_Authenticate', ((1, 'lAuthenticate'),)))
    IMSMQQueueInfo.get_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_JournalQuota', ((1, 'plJournalQuota'),)))
    IMSMQQueueInfo.put_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_JournalQuota', ((1, 'lJournalQuota'),)))
    IMSMQQueueInfo.get_IsWorldReadable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_IsWorldReadable', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'Create', ((1, 'IsTransactional'),(1, 'IsWorldReadable'),)))
    IMSMQQueueInfo.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'Delete', ()))
    IMSMQQueueInfo.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.MessageQueuing.IMSMQQueue_head), use_last_error=False)(34, 'Open', ((1, 'Access'),(1, 'ShareMode'),(1, 'ppq'),)))
    IMSMQQueueInfo.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Refresh', ()))
    IMSMQQueueInfo.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'Update', ()))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfo
def _define_IMSMQQueueInfo2_head():
    class IMSMQQueueInfo2(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd174a80-89cf-11d2-b0f2-00e02c074f6b')
    return IMSMQQueueInfo2
def _define_IMSMQQueueInfo2():
    IMSMQQueueInfo2 = win32more.System.MessageQueuing.IMSMQQueueInfo2_head
    IMSMQQueueInfo2.get_QueueGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_QueueGuid', ((1, 'pbstrGuidQueue'),)))
    IMSMQQueueInfo2.get_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServiceTypeGuid', ((1, 'pbstrGuidServiceType'),)))
    IMSMQQueueInfo2.put_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_ServiceTypeGuid', ((1, 'bstrGuidServiceType'),)))
    IMSMQQueueInfo2.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQQueueInfo2.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQQueueInfo2.get_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_PathName', ((1, 'pbstrPathName'),)))
    IMSMQQueueInfo2.put_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_PathName', ((1, 'bstrPathName'),)))
    IMSMQQueueInfo2.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQQueueInfo2.put_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_FormatName', ((1, 'bstrFormatName'),)))
    IMSMQQueueInfo2.get_IsTransactional = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsTransactional', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo2.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQQueueInfo2.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQQueueInfo2.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQQueueInfo2.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQQueueInfo2.get_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_Quota', ((1, 'plQuota'),)))
    IMSMQQueueInfo2.put_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_Quota', ((1, 'lQuota'),)))
    IMSMQQueueInfo2.get_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_BasePriority', ((1, 'plBasePriority'),)))
    IMSMQQueueInfo2.put_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_BasePriority', ((1, 'lBasePriority'),)))
    IMSMQQueueInfo2.get_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_CreateTime', ((1, 'pvarCreateTime'),)))
    IMSMQQueueInfo2.get_ModifyTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_ModifyTime', ((1, 'pvarModifyTime'),)))
    IMSMQQueueInfo2.get_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_Authenticate', ((1, 'plAuthenticate'),)))
    IMSMQQueueInfo2.put_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_Authenticate', ((1, 'lAuthenticate'),)))
    IMSMQQueueInfo2.get_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_JournalQuota', ((1, 'plJournalQuota'),)))
    IMSMQQueueInfo2.put_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_JournalQuota', ((1, 'lJournalQuota'),)))
    IMSMQQueueInfo2.get_IsWorldReadable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_IsWorldReadable', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo2.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'Create', ((1, 'IsTransactional'),(1, 'IsWorldReadable'),)))
    IMSMQQueueInfo2.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'Delete', ()))
    IMSMQQueueInfo2.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.MessageQueuing.IMSMQQueue2_head), use_last_error=False)(34, 'Open', ((1, 'Access'),(1, 'ShareMode'),(1, 'ppq'),)))
    IMSMQQueueInfo2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Refresh', ()))
    IMSMQQueueInfo2.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'Update', ()))
    IMSMQQueueInfo2.get_PathNameDNS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_PathNameDNS', ((1, 'pbstrPathNameDNS'),)))
    IMSMQQueueInfo2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(38, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQueueInfo2.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(39, 'get_Security', ((1, 'pvarSecurity'),)))
    IMSMQQueueInfo2.put_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(40, 'put_Security', ((1, 'varSecurity'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfo2
def _define_IMSMQQueueInfo3_head():
    class IMSMQQueueInfo3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b1d-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueueInfo3
def _define_IMSMQQueueInfo3():
    IMSMQQueueInfo3 = win32more.System.MessageQueuing.IMSMQQueueInfo3_head
    IMSMQQueueInfo3.get_QueueGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_QueueGuid', ((1, 'pbstrGuidQueue'),)))
    IMSMQQueueInfo3.get_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServiceTypeGuid', ((1, 'pbstrGuidServiceType'),)))
    IMSMQQueueInfo3.put_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_ServiceTypeGuid', ((1, 'bstrGuidServiceType'),)))
    IMSMQQueueInfo3.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQQueueInfo3.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQQueueInfo3.get_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_PathName', ((1, 'pbstrPathName'),)))
    IMSMQQueueInfo3.put_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_PathName', ((1, 'bstrPathName'),)))
    IMSMQQueueInfo3.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQQueueInfo3.put_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_FormatName', ((1, 'bstrFormatName'),)))
    IMSMQQueueInfo3.get_IsTransactional = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsTransactional', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo3.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQQueueInfo3.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQQueueInfo3.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQQueueInfo3.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQQueueInfo3.get_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_Quota', ((1, 'plQuota'),)))
    IMSMQQueueInfo3.put_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_Quota', ((1, 'lQuota'),)))
    IMSMQQueueInfo3.get_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_BasePriority', ((1, 'plBasePriority'),)))
    IMSMQQueueInfo3.put_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_BasePriority', ((1, 'lBasePriority'),)))
    IMSMQQueueInfo3.get_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_CreateTime', ((1, 'pvarCreateTime'),)))
    IMSMQQueueInfo3.get_ModifyTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_ModifyTime', ((1, 'pvarModifyTime'),)))
    IMSMQQueueInfo3.get_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_Authenticate', ((1, 'plAuthenticate'),)))
    IMSMQQueueInfo3.put_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_Authenticate', ((1, 'lAuthenticate'),)))
    IMSMQQueueInfo3.get_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_JournalQuota', ((1, 'plJournalQuota'),)))
    IMSMQQueueInfo3.put_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_JournalQuota', ((1, 'lJournalQuota'),)))
    IMSMQQueueInfo3.get_IsWorldReadable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_IsWorldReadable', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo3.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'Create', ((1, 'IsTransactional'),(1, 'IsWorldReadable'),)))
    IMSMQQueueInfo3.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'Delete', ()))
    IMSMQQueueInfo3.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.MessageQueuing.IMSMQQueue3_head), use_last_error=False)(34, 'Open', ((1, 'Access'),(1, 'ShareMode'),(1, 'ppq'),)))
    IMSMQQueueInfo3.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Refresh', ()))
    IMSMQQueueInfo3.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'Update', ()))
    IMSMQQueueInfo3.get_PathNameDNS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_PathNameDNS', ((1, 'pbstrPathNameDNS'),)))
    IMSMQQueueInfo3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(38, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQueueInfo3.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(39, 'get_Security', ((1, 'pvarSecurity'),)))
    IMSMQQueueInfo3.put_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(40, 'put_Security', ((1, 'varSecurity'),)))
    IMSMQQueueInfo3.get_IsTransactional2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(41, 'get_IsTransactional2', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo3.get_IsWorldReadable2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_IsWorldReadable2', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo3.get_MulticastAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(43, 'get_MulticastAddress', ((1, 'pbstrMulticastAddress'),)))
    IMSMQQueueInfo3.put_MulticastAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(44, 'put_MulticastAddress', ((1, 'bstrMulticastAddress'),)))
    IMSMQQueueInfo3.get_ADsPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_ADsPath', ((1, 'pbstrADsPath'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfo3
def _define_IMSMQQueueInfo4_head():
    class IMSMQQueueInfo4(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b21-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueueInfo4
def _define_IMSMQQueueInfo4():
    IMSMQQueueInfo4 = win32more.System.MessageQueuing.IMSMQQueueInfo4_head
    IMSMQQueueInfo4.get_QueueGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_QueueGuid', ((1, 'pbstrGuidQueue'),)))
    IMSMQQueueInfo4.get_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ServiceTypeGuid', ((1, 'pbstrGuidServiceType'),)))
    IMSMQQueueInfo4.put_ServiceTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_ServiceTypeGuid', ((1, 'bstrGuidServiceType'),)))
    IMSMQQueueInfo4.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQQueueInfo4.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQQueueInfo4.get_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_PathName', ((1, 'pbstrPathName'),)))
    IMSMQQueueInfo4.put_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_PathName', ((1, 'bstrPathName'),)))
    IMSMQQueueInfo4.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQQueueInfo4.put_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_FormatName', ((1, 'bstrFormatName'),)))
    IMSMQQueueInfo4.get_IsTransactional = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_IsTransactional', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo4.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQQueueInfo4.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQQueueInfo4.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQQueueInfo4.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQQueueInfo4.get_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_Quota', ((1, 'plQuota'),)))
    IMSMQQueueInfo4.put_Quota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_Quota', ((1, 'lQuota'),)))
    IMSMQQueueInfo4.get_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_BasePriority', ((1, 'plBasePriority'),)))
    IMSMQQueueInfo4.put_BasePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_BasePriority', ((1, 'lBasePriority'),)))
    IMSMQQueueInfo4.get_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(25, 'get_CreateTime', ((1, 'pvarCreateTime'),)))
    IMSMQQueueInfo4.get_ModifyTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_ModifyTime', ((1, 'pvarModifyTime'),)))
    IMSMQQueueInfo4.get_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_Authenticate', ((1, 'plAuthenticate'),)))
    IMSMQQueueInfo4.put_Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_Authenticate', ((1, 'lAuthenticate'),)))
    IMSMQQueueInfo4.get_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_JournalQuota', ((1, 'plJournalQuota'),)))
    IMSMQQueueInfo4.put_JournalQuota = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_JournalQuota', ((1, 'lJournalQuota'),)))
    IMSMQQueueInfo4.get_IsWorldReadable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_IsWorldReadable', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo4.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'Create', ((1, 'IsTransactional'),(1, 'IsWorldReadable'),)))
    IMSMQQueueInfo4.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'Delete', ()))
    IMSMQQueueInfo4.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.MessageQueuing.IMSMQQueue4_head), use_last_error=False)(34, 'Open', ((1, 'Access'),(1, 'ShareMode'),(1, 'ppq'),)))
    IMSMQQueueInfo4.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Refresh', ()))
    IMSMQQueueInfo4.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(36, 'Update', ()))
    IMSMQQueueInfo4.get_PathNameDNS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_PathNameDNS', ((1, 'pbstrPathNameDNS'),)))
    IMSMQQueueInfo4.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(38, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQueueInfo4.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(39, 'get_Security', ((1, 'pvarSecurity'),)))
    IMSMQQueueInfo4.put_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(40, 'put_Security', ((1, 'varSecurity'),)))
    IMSMQQueueInfo4.get_IsTransactional2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(41, 'get_IsTransactional2', ((1, 'pisTransactional'),)))
    IMSMQQueueInfo4.get_IsWorldReadable2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_IsWorldReadable2', ((1, 'pisWorldReadable'),)))
    IMSMQQueueInfo4.get_MulticastAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(43, 'get_MulticastAddress', ((1, 'pbstrMulticastAddress'),)))
    IMSMQQueueInfo4.put_MulticastAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(44, 'put_MulticastAddress', ((1, 'bstrMulticastAddress'),)))
    IMSMQQueueInfo4.get_ADsPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_ADsPath', ((1, 'pbstrADsPath'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfo4
def _define_IMSMQQueue_head():
    class IMSMQQueue(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e076-dccd-11d0-aa4b-0060970debae')
    return IMSMQQueue
def _define_IMSMQQueue():
    IMSMQQueue = win32more.System.MessageQueuing.IMSMQQueue_head
    IMSMQQueue.get_Access = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Access', ((1, 'plAccess'),)))
    IMSMQQueue.get_ShareMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ShareMode', ((1, 'plShareMode'),)))
    IMSMQQueue.get_QueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(9, 'get_QueueInfo', ((1, 'ppqinfo'),)))
    IMSMQQueue.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Handle', ((1, 'plHandle'),)))
    IMSMQQueue.get_IsOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsOpen', ((1, 'pisOpen'),)))
    IMSMQQueue.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Close', ()))
    IMSMQQueue.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(13, 'Receive', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue.Peek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(14, 'Peek', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue.EnableNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQEvent_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'EnableNotification', ((1, 'Event'),(1, 'Cursor'),(1, 'ReceiveTimeout'),)))
    IMSMQQueue.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Reset', ()))
    IMSMQQueue.ReceiveCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(17, 'ReceiveCurrent', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue.PeekNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(18, 'PeekNext', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue.PeekCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(19, 'PeekCurrent', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueue
def _define_IMSMQQueue2_head():
    class IMSMQQueue2(win32more.System.Com.IDispatch_head):
        Guid = Guid('ef0574e0-06d8-11d3-b100-00e02c074f6b')
    return IMSMQQueue2
def _define_IMSMQQueue2():
    IMSMQQueue2 = win32more.System.MessageQueuing.IMSMQQueue2_head
    IMSMQQueue2.get_Access = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Access', ((1, 'plAccess'),)))
    IMSMQQueue2.get_ShareMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ShareMode', ((1, 'plShareMode'),)))
    IMSMQQueue2.get_QueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(9, 'get_QueueInfo', ((1, 'ppqinfo'),)))
    IMSMQQueue2.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Handle', ((1, 'plHandle'),)))
    IMSMQQueue2.get_IsOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsOpen', ((1, 'pisOpen'),)))
    IMSMQQueue2.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Close', ()))
    IMSMQQueue2.Receive_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(13, 'Receive_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue2.Peek_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(14, 'Peek_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue2.EnableNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQEvent2_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'EnableNotification', ((1, 'Event'),(1, 'Cursor'),(1, 'ReceiveTimeout'),)))
    IMSMQQueue2.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Reset', ()))
    IMSMQQueue2.ReceiveCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(17, 'ReceiveCurrent_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue2.PeekNext_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(18, 'PeekNext_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue2.PeekCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(19, 'PeekCurrent_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue2.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head), use_last_error=False)(20, 'Receive', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue2.Peek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head), use_last_error=False)(21, 'Peek', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue2.ReceiveCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head), use_last_error=False)(22, 'ReceiveCurrent', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue2.PeekNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head), use_last_error=False)(23, 'PeekNext', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue2.PeekCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage2_head), use_last_error=False)(24, 'PeekCurrent', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(25, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueue2
def _define_IMSMQQueue3_head():
    class IMSMQQueue3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b1b-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueue3
def _define_IMSMQQueue3():
    IMSMQQueue3 = win32more.System.MessageQueuing.IMSMQQueue3_head
    IMSMQQueue3.get_Access = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Access', ((1, 'plAccess'),)))
    IMSMQQueue3.get_ShareMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ShareMode', ((1, 'plShareMode'),)))
    IMSMQQueue3.get_QueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(9, 'get_QueueInfo', ((1, 'ppqinfo'),)))
    IMSMQQueue3.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Handle', ((1, 'plHandle'),)))
    IMSMQQueue3.get_IsOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsOpen', ((1, 'pisOpen'),)))
    IMSMQQueue3.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Close', ()))
    IMSMQQueue3.Receive_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(13, 'Receive_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue3.Peek_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(14, 'Peek_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue3.EnableNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQEvent3_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'EnableNotification', ((1, 'Event'),(1, 'Cursor'),(1, 'ReceiveTimeout'),)))
    IMSMQQueue3.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Reset', ()))
    IMSMQQueue3.ReceiveCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(17, 'ReceiveCurrent_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekNext_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(18, 'PeekNext_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(19, 'PeekCurrent_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue3.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(20, 'Receive', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.Peek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(21, 'Peek', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.ReceiveCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(22, 'ReceiveCurrent', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(23, 'PeekNext', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(24, 'PeekCurrent', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(25, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQueue3.get_Handle2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_Handle2', ((1, 'pvarHandle'),)))
    IMSMQQueue3.ReceiveByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(27, 'ReceiveByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.ReceiveNextByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(28, 'ReceiveNextByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.ReceivePreviousByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(29, 'ReceivePreviousByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.ReceiveFirstByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(30, 'ReceiveFirstByLookupId', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.ReceiveLastByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(31, 'ReceiveLastByLookupId', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(32, 'PeekByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekNextByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(33, 'PeekNextByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekPreviousByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(34, 'PeekPreviousByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekFirstByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(35, 'PeekFirstByLookupId', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.PeekLastByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage3_head), use_last_error=False)(36, 'PeekLastByLookupId', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue3.Purge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(37, 'Purge', ()))
    IMSMQQueue3.get_IsOpen2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(38, 'get_IsOpen2', ((1, 'pisOpen'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueue3
def _define_IMSMQQueue4_head():
    class IMSMQQueue4(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b20-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueue4
def _define_IMSMQQueue4():
    IMSMQQueue4 = win32more.System.MessageQueuing.IMSMQQueue4_head
    IMSMQQueue4.get_Access = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Access', ((1, 'plAccess'),)))
    IMSMQQueue4.get_ShareMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ShareMode', ((1, 'plShareMode'),)))
    IMSMQQueue4.get_QueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(9, 'get_QueueInfo', ((1, 'ppqinfo'),)))
    IMSMQQueue4.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Handle', ((1, 'plHandle'),)))
    IMSMQQueue4.get_IsOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsOpen', ((1, 'pisOpen'),)))
    IMSMQQueue4.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Close', ()))
    IMSMQQueue4.Receive_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(13, 'Receive_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue4.Peek_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(14, 'Peek_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue4.EnableNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQEvent3_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'EnableNotification', ((1, 'Event'),(1, 'Cursor'),(1, 'ReceiveTimeout'),)))
    IMSMQQueue4.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Reset', ()))
    IMSMQQueue4.ReceiveCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(17, 'ReceiveCurrent_v1', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekNext_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(18, 'PeekNext_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekCurrent_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage_head), use_last_error=False)(19, 'PeekCurrent_v1', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'ppmsg'),)))
    IMSMQQueue4.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(20, 'Receive', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.Peek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(21, 'Peek', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.ReceiveCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(22, 'ReceiveCurrent', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(23, 'PeekNext', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(24, 'PeekCurrent', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'ReceiveTimeout'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(25, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQueue4.get_Handle2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(26, 'get_Handle2', ((1, 'pvarHandle'),)))
    IMSMQQueue4.ReceiveByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(27, 'ReceiveByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.ReceiveNextByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(28, 'ReceiveNextByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.ReceivePreviousByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(29, 'ReceivePreviousByLookupId', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.ReceiveFirstByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(30, 'ReceiveFirstByLookupId', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.ReceiveLastByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(31, 'ReceiveLastByLookupId', ((1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(32, 'PeekByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekNextByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(33, 'PeekNextByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekPreviousByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(34, 'PeekPreviousByLookupId', ((1, 'LookupId'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekFirstByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(35, 'PeekFirstByLookupId', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.PeekLastByLookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(36, 'PeekLastByLookupId', ((1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    IMSMQQueue4.Purge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(37, 'Purge', ()))
    IMSMQQueue4.get_IsOpen2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(38, 'get_IsOpen2', ((1, 'pisOpen'),)))
    IMSMQQueue4.ReceiveByLookupIdAllowPeek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQMessage4_head), use_last_error=False)(39, 'ReceiveByLookupIdAllowPeek', ((1, 'LookupId'),(1, 'Transaction'),(1, 'WantDestinationQueue'),(1, 'WantBody'),(1, 'WantConnectorType'),(1, 'ppmsg'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueue4
def _define_IMSMQMessage_head():
    class IMSMQMessage(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e074-dccd-11d0-aa4b-0060970debae')
    return IMSMQMessage
def _define_IMSMQMessage():
    IMSMQMessage = win32more.System.MessageQueuing.IMSMQMessage_head
    IMSMQMessage.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Class', ((1, 'plClass'),)))
    IMSMQMessage.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQMessage.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQMessage.get_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_AuthLevel', ((1, 'plAuthLevel'),)))
    IMSMQMessage.put_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_AuthLevel', ((1, 'lAuthLevel'),)))
    IMSMQMessage.get_IsAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsAuthenticated', ((1, 'pisAuthenticated'),)))
    IMSMQMessage.get_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Delivery', ((1, 'plDelivery'),)))
    IMSMQMessage.put_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Delivery', ((1, 'lDelivery'),)))
    IMSMQMessage.get_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Trace', ((1, 'plTrace'),)))
    IMSMQMessage.put_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Trace', ((1, 'lTrace'),)))
    IMSMQMessage.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Priority', ((1, 'plPriority'),)))
    IMSMQMessage.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_Priority', ((1, 'lPriority'),)))
    IMSMQMessage.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQMessage.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQMessage.get_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(21, 'get_ResponseQueueInfo', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage.putref_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(22, 'putref_ResponseQueueInfo', ((1, 'pqinfoResponse'),)))
    IMSMQMessage.get_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AppSpecific', ((1, 'plAppSpecific'),)))
    IMSMQMessage.put_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AppSpecific', ((1, 'lAppSpecific'),)))
    IMSMQMessage.get_SourceMachineGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_SourceMachineGuid', ((1, 'pbstrGuidSrcMachine'),)))
    IMSMQMessage.get_BodyLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_BodyLength', ((1, 'pcbBody'),)))
    IMSMQMessage.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(27, 'get_Body', ((1, 'pvarBody'),)))
    IMSMQMessage.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(28, 'put_Body', ((1, 'varBody'),)))
    IMSMQMessage.get_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(29, 'get_AdminQueueInfo', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage.putref_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(30, 'putref_AdminQueueInfo', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'get_Id', ((1, 'pvarMsgId'),)))
    IMSMQMessage.get_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'get_CorrelationId', ((1, 'pvarMsgId'),)))
    IMSMQMessage.put_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(33, 'put_CorrelationId', ((1, 'varMsgId'),)))
    IMSMQMessage.get_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'get_Ack', ((1, 'plAck'),)))
    IMSMQMessage.put_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'put_Ack', ((1, 'lAck'),)))
    IMSMQMessage.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQMessage.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQMessage.get_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'get_MaxTimeToReachQueue', ((1, 'plMaxTimeToReachQueue'),)))
    IMSMQMessage.put_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'put_MaxTimeToReachQueue', ((1, 'lMaxTimeToReachQueue'),)))
    IMSMQMessage.get_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'get_MaxTimeToReceive', ((1, 'plMaxTimeToReceive'),)))
    IMSMQMessage.put_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(41, 'put_MaxTimeToReceive', ((1, 'lMaxTimeToReceive'),)))
    IMSMQMessage.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'get_HashAlgorithm', ((1, 'plHashAlg'),)))
    IMSMQMessage.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'put_HashAlgorithm', ((1, 'lHashAlg'),)))
    IMSMQMessage.get_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'get_EncryptAlgorithm', ((1, 'plEncryptAlg'),)))
    IMSMQMessage.put_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'put_EncryptAlgorithm', ((1, 'lEncryptAlg'),)))
    IMSMQMessage.get_SentTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(46, 'get_SentTime', ((1, 'pvarSentTime'),)))
    IMSMQMessage.get_ArrivedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(47, 'get_ArrivedTime', ((1, 'plArrivedTime'),)))
    IMSMQMessage.get_DestinationQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(48, 'get_DestinationQueueInfo', ((1, 'ppqinfoDest'),)))
    IMSMQMessage.get_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'get_SenderCertificate', ((1, 'pvarSenderCert'),)))
    IMSMQMessage.put_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(50, 'put_SenderCertificate', ((1, 'varSenderCert'),)))
    IMSMQMessage.get_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(51, 'get_SenderId', ((1, 'pvarSenderId'),)))
    IMSMQMessage.get_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'get_SenderIdType', ((1, 'plSenderIdType'),)))
    IMSMQMessage.put_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'put_SenderIdType', ((1, 'lSenderIdType'),)))
    IMSMQMessage.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueue_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'Send', ((1, 'DestinationQueue'),(1, 'Transaction'),)))
    IMSMQMessage.AttachCurrentSecurityContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(55, 'AttachCurrentSecurityContext', ()))
    win32more.System.Com.IDispatch
    return IMSMQMessage
def _define_IMSMQQueueInfos_head():
    class IMSMQQueueInfos(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e07d-dccd-11d0-aa4b-0060970debae')
    return IMSMQQueueInfos
def _define_IMSMQQueueInfos():
    IMSMQQueueInfos = win32more.System.MessageQueuing.IMSMQQueueInfos_head
    IMSMQQueueInfos.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    IMSMQQueueInfos.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(8, 'Next', ((1, 'ppqinfoNext'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfos
def _define_IMSMQQueueInfos2_head():
    class IMSMQQueueInfos2(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b0f-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueueInfos2
def _define_IMSMQQueueInfos2():
    IMSMQQueueInfos2 = win32more.System.MessageQueuing.IMSMQQueueInfos2_head
    IMSMQQueueInfos2.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    IMSMQQueueInfos2.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(8, 'Next', ((1, 'ppqinfoNext'),)))
    IMSMQQueueInfos2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(9, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfos2
def _define_IMSMQQueueInfos3_head():
    class IMSMQQueueInfos3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b1e-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueueInfos3
def _define_IMSMQQueueInfos3():
    IMSMQQueueInfos3 = win32more.System.MessageQueuing.IMSMQQueueInfos3_head
    IMSMQQueueInfos3.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    IMSMQQueueInfos3.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(8, 'Next', ((1, 'ppqinfoNext'),)))
    IMSMQQueueInfos3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(9, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfos3
def _define_IMSMQQueueInfos4_head():
    class IMSMQQueueInfos4(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b22-2168-11d3-898c-00e02c074f6b')
    return IMSMQQueueInfos4
def _define_IMSMQQueueInfos4():
    IMSMQQueueInfos4 = win32more.System.MessageQueuing.IMSMQQueueInfos4_head
    IMSMQQueueInfos4.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    IMSMQQueueInfos4.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(8, 'Next', ((1, 'ppqinfoNext'),)))
    IMSMQQueueInfos4.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(9, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQQueueInfos4
def _define_IMSMQEvent_head():
    class IMSMQEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e077-dccd-11d0-aa4b-0060970debae')
    return IMSMQEvent
def _define_IMSMQEvent():
    IMSMQEvent = win32more.System.MessageQueuing.IMSMQEvent_head
    win32more.System.Com.IDispatch
    return IMSMQEvent
def _define_IMSMQEvent2_head():
    class IMSMQEvent2(win32more.System.MessageQueuing.IMSMQEvent_head):
        Guid = Guid('eba96b12-2168-11d3-898c-00e02c074f6b')
    return IMSMQEvent2
def _define_IMSMQEvent2():
    IMSMQEvent2 = win32more.System.MessageQueuing.IMSMQEvent2_head
    IMSMQEvent2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.MessageQueuing.IMSMQEvent
    return IMSMQEvent2
def _define_IMSMQEvent3_head():
    class IMSMQEvent3(win32more.System.MessageQueuing.IMSMQEvent2_head):
        Guid = Guid('eba96b1c-2168-11d3-898c-00e02c074f6b')
    return IMSMQEvent3
def _define_IMSMQEvent3():
    IMSMQEvent3 = win32more.System.MessageQueuing.IMSMQEvent3_head
    win32more.System.MessageQueuing.IMSMQEvent2
    return IMSMQEvent3
def _define_IMSMQTransaction_head():
    class IMSMQTransaction(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e07f-dccd-11d0-aa4b-0060970debae')
    return IMSMQTransaction
def _define_IMSMQTransaction():
    IMSMQTransaction = win32more.System.MessageQueuing.IMSMQTransaction_head
    IMSMQTransaction.get_Transaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Transaction', ((1, 'plTransaction'),)))
    IMSMQTransaction.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'Commit', ((1, 'fRetaining'),(1, 'grfTC'),(1, 'grfRM'),)))
    IMSMQTransaction.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'Abort', ((1, 'fRetaining'),(1, 'fAsync'),)))
    win32more.System.Com.IDispatch
    return IMSMQTransaction
def _define_IMSMQCoordinatedTransactionDispenser_head():
    class IMSMQCoordinatedTransactionDispenser(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e081-dccd-11d0-aa4b-0060970debae')
    return IMSMQCoordinatedTransactionDispenser
def _define_IMSMQCoordinatedTransactionDispenser():
    IMSMQCoordinatedTransactionDispenser = win32more.System.MessageQueuing.IMSMQCoordinatedTransactionDispenser_head
    IMSMQCoordinatedTransactionDispenser.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    win32more.System.Com.IDispatch
    return IMSMQCoordinatedTransactionDispenser
def _define_IMSMQTransactionDispenser_head():
    class IMSMQTransactionDispenser(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e083-dccd-11d0-aa4b-0060970debae')
    return IMSMQTransactionDispenser
def _define_IMSMQTransactionDispenser():
    IMSMQTransactionDispenser = win32more.System.MessageQueuing.IMSMQTransactionDispenser_head
    IMSMQTransactionDispenser.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    win32more.System.Com.IDispatch
    return IMSMQTransactionDispenser
def _define_IMSMQQuery2_head():
    class IMSMQQuery2(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b0e-2168-11d3-898c-00e02c074f6b')
    return IMSMQQuery2
def _define_IMSMQQuery2():
    IMSMQQuery2 = win32more.System.MessageQueuing.IMSMQQuery2_head
    IMSMQQuery2.LookupQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos2_head), use_last_error=False)(7, 'LookupQueue', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'ppqinfos'),)))
    IMSMQQuery2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQQuery2
def _define_IMSMQQuery3_head():
    class IMSMQQuery3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b19-2168-11d3-898c-00e02c074f6b')
    return IMSMQQuery3
def _define_IMSMQQuery3():
    IMSMQQuery3 = win32more.System.MessageQueuing.IMSMQQuery3_head
    IMSMQQuery3.LookupQueue_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos3_head), use_last_error=False)(7, 'LookupQueue_v2', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'ppqinfos'),)))
    IMSMQQuery3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQuery3.LookupQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos3_head), use_last_error=False)(9, 'LookupQueue', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'MulticastAddress'),(1, 'RelMulticastAddress'),(1, 'ppqinfos'),)))
    win32more.System.Com.IDispatch
    return IMSMQQuery3
def _define_IMSMQQuery4_head():
    class IMSMQQuery4(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b24-2168-11d3-898c-00e02c074f6b')
    return IMSMQQuery4
def _define_IMSMQQuery4():
    IMSMQQuery4 = win32more.System.MessageQueuing.IMSMQQuery4_head
    IMSMQQuery4.LookupQueue_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos4_head), use_last_error=False)(7, 'LookupQueue_v2', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'ppqinfos'),)))
    IMSMQQuery4.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQQuery4.LookupQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.MessageQueuing.IMSMQQueueInfos4_head), use_last_error=False)(9, 'LookupQueue', ((1, 'QueueGuid'),(1, 'ServiceTypeGuid'),(1, 'Label'),(1, 'CreateTime'),(1, 'ModifyTime'),(1, 'RelServiceType'),(1, 'RelLabel'),(1, 'RelCreateTime'),(1, 'RelModifyTime'),(1, 'MulticastAddress'),(1, 'RelMulticastAddress'),(1, 'ppqinfos'),)))
    win32more.System.Com.IDispatch
    return IMSMQQuery4
def _define_IMSMQMessage2_head():
    class IMSMQMessage2(win32more.System.Com.IDispatch_head):
        Guid = Guid('d9933be0-a567-11d2-b0f3-00e02c074f6b')
    return IMSMQMessage2
def _define_IMSMQMessage2():
    IMSMQMessage2 = win32more.System.MessageQueuing.IMSMQMessage2_head
    IMSMQMessage2.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Class', ((1, 'plClass'),)))
    IMSMQMessage2.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQMessage2.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQMessage2.get_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_AuthLevel', ((1, 'plAuthLevel'),)))
    IMSMQMessage2.put_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_AuthLevel', ((1, 'lAuthLevel'),)))
    IMSMQMessage2.get_IsAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsAuthenticated', ((1, 'pisAuthenticated'),)))
    IMSMQMessage2.get_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Delivery', ((1, 'plDelivery'),)))
    IMSMQMessage2.put_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Delivery', ((1, 'lDelivery'),)))
    IMSMQMessage2.get_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Trace', ((1, 'plTrace'),)))
    IMSMQMessage2.put_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Trace', ((1, 'lTrace'),)))
    IMSMQMessage2.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Priority', ((1, 'plPriority'),)))
    IMSMQMessage2.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_Priority', ((1, 'lPriority'),)))
    IMSMQMessage2.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQMessage2.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQMessage2.get_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(21, 'get_ResponseQueueInfo_v1', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage2.putref_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(22, 'putref_ResponseQueueInfo_v1', ((1, 'pqinfoResponse'),)))
    IMSMQMessage2.get_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AppSpecific', ((1, 'plAppSpecific'),)))
    IMSMQMessage2.put_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AppSpecific', ((1, 'lAppSpecific'),)))
    IMSMQMessage2.get_SourceMachineGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_SourceMachineGuid', ((1, 'pbstrGuidSrcMachine'),)))
    IMSMQMessage2.get_BodyLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_BodyLength', ((1, 'pcbBody'),)))
    IMSMQMessage2.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(27, 'get_Body', ((1, 'pvarBody'),)))
    IMSMQMessage2.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(28, 'put_Body', ((1, 'varBody'),)))
    IMSMQMessage2.get_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(29, 'get_AdminQueueInfo_v1', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage2.putref_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(30, 'putref_AdminQueueInfo_v1', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage2.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'get_Id', ((1, 'pvarMsgId'),)))
    IMSMQMessage2.get_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'get_CorrelationId', ((1, 'pvarMsgId'),)))
    IMSMQMessage2.put_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(33, 'put_CorrelationId', ((1, 'varMsgId'),)))
    IMSMQMessage2.get_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'get_Ack', ((1, 'plAck'),)))
    IMSMQMessage2.put_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'put_Ack', ((1, 'lAck'),)))
    IMSMQMessage2.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQMessage2.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQMessage2.get_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'get_MaxTimeToReachQueue', ((1, 'plMaxTimeToReachQueue'),)))
    IMSMQMessage2.put_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'put_MaxTimeToReachQueue', ((1, 'lMaxTimeToReachQueue'),)))
    IMSMQMessage2.get_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'get_MaxTimeToReceive', ((1, 'plMaxTimeToReceive'),)))
    IMSMQMessage2.put_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(41, 'put_MaxTimeToReceive', ((1, 'lMaxTimeToReceive'),)))
    IMSMQMessage2.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'get_HashAlgorithm', ((1, 'plHashAlg'),)))
    IMSMQMessage2.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'put_HashAlgorithm', ((1, 'lHashAlg'),)))
    IMSMQMessage2.get_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'get_EncryptAlgorithm', ((1, 'plEncryptAlg'),)))
    IMSMQMessage2.put_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'put_EncryptAlgorithm', ((1, 'lEncryptAlg'),)))
    IMSMQMessage2.get_SentTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(46, 'get_SentTime', ((1, 'pvarSentTime'),)))
    IMSMQMessage2.get_ArrivedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(47, 'get_ArrivedTime', ((1, 'plArrivedTime'),)))
    IMSMQMessage2.get_DestinationQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(48, 'get_DestinationQueueInfo', ((1, 'ppqinfoDest'),)))
    IMSMQMessage2.get_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'get_SenderCertificate', ((1, 'pvarSenderCert'),)))
    IMSMQMessage2.put_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(50, 'put_SenderCertificate', ((1, 'varSenderCert'),)))
    IMSMQMessage2.get_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(51, 'get_SenderId', ((1, 'pvarSenderId'),)))
    IMSMQMessage2.get_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'get_SenderIdType', ((1, 'plSenderIdType'),)))
    IMSMQMessage2.put_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'put_SenderIdType', ((1, 'lSenderIdType'),)))
    IMSMQMessage2.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueue2_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'Send', ((1, 'DestinationQueue'),(1, 'Transaction'),)))
    IMSMQMessage2.AttachCurrentSecurityContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(55, 'AttachCurrentSecurityContext', ()))
    IMSMQMessage2.get_SenderVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(56, 'get_SenderVersion', ((1, 'plSenderVersion'),)))
    IMSMQMessage2.get_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(57, 'get_Extension', ((1, 'pvarExtension'),)))
    IMSMQMessage2.put_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(58, 'put_Extension', ((1, 'varExtension'),)))
    IMSMQMessage2.get_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(59, 'get_ConnectorTypeGuid', ((1, 'pbstrGuidConnectorType'),)))
    IMSMQMessage2.put_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(60, 'put_ConnectorTypeGuid', ((1, 'bstrGuidConnectorType'),)))
    IMSMQMessage2.get_TransactionStatusQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(61, 'get_TransactionStatusQueueInfo', ((1, 'ppqinfoXactStatus'),)))
    IMSMQMessage2.get_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(62, 'get_DestinationSymmetricKey', ((1, 'pvarDestSymmKey'),)))
    IMSMQMessage2.put_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(63, 'put_DestinationSymmetricKey', ((1, 'varDestSymmKey'),)))
    IMSMQMessage2.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(64, 'get_Signature', ((1, 'pvarSignature'),)))
    IMSMQMessage2.put_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(65, 'put_Signature', ((1, 'varSignature'),)))
    IMSMQMessage2.get_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(66, 'get_AuthenticationProviderType', ((1, 'plAuthProvType'),)))
    IMSMQMessage2.put_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(67, 'put_AuthenticationProviderType', ((1, 'lAuthProvType'),)))
    IMSMQMessage2.get_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(68, 'get_AuthenticationProviderName', ((1, 'pbstrAuthProvName'),)))
    IMSMQMessage2.put_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(69, 'put_AuthenticationProviderName', ((1, 'bstrAuthProvName'),)))
    IMSMQMessage2.put_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(70, 'put_SenderId', ((1, 'varSenderId'),)))
    IMSMQMessage2.get_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_MsgClass', ((1, 'plMsgClass'),)))
    IMSMQMessage2.put_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(72, 'put_MsgClass', ((1, 'lMsgClass'),)))
    IMSMQMessage2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(73, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQMessage2.get_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(74, 'get_TransactionId', ((1, 'pvarXactId'),)))
    IMSMQMessage2.get_IsFirstInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(75, 'get_IsFirstInTransaction', ((1, 'pisFirstInXact'),)))
    IMSMQMessage2.get_IsLastInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(76, 'get_IsLastInTransaction', ((1, 'pisLastInXact'),)))
    IMSMQMessage2.get_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(77, 'get_ResponseQueueInfo', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage2.putref_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(78, 'putref_ResponseQueueInfo', ((1, 'pqinfoResponse'),)))
    IMSMQMessage2.get_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(79, 'get_AdminQueueInfo', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage2.putref_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(80, 'putref_AdminQueueInfo', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage2.get_ReceivedAuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(81, 'get_ReceivedAuthenticationLevel', ((1, 'psReceivedAuthenticationLevel'),)))
    win32more.System.Com.IDispatch
    return IMSMQMessage2
def _define_IMSMQMessage3_head():
    class IMSMQMessage3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b1a-2168-11d3-898c-00e02c074f6b')
    return IMSMQMessage3
def _define_IMSMQMessage3():
    IMSMQMessage3 = win32more.System.MessageQueuing.IMSMQMessage3_head
    IMSMQMessage3.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Class', ((1, 'plClass'),)))
    IMSMQMessage3.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQMessage3.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQMessage3.get_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_AuthLevel', ((1, 'plAuthLevel'),)))
    IMSMQMessage3.put_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_AuthLevel', ((1, 'lAuthLevel'),)))
    IMSMQMessage3.get_IsAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsAuthenticated', ((1, 'pisAuthenticated'),)))
    IMSMQMessage3.get_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Delivery', ((1, 'plDelivery'),)))
    IMSMQMessage3.put_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Delivery', ((1, 'lDelivery'),)))
    IMSMQMessage3.get_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Trace', ((1, 'plTrace'),)))
    IMSMQMessage3.put_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Trace', ((1, 'lTrace'),)))
    IMSMQMessage3.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Priority', ((1, 'plPriority'),)))
    IMSMQMessage3.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_Priority', ((1, 'lPriority'),)))
    IMSMQMessage3.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQMessage3.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQMessage3.get_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(21, 'get_ResponseQueueInfo_v1', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage3.putref_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(22, 'putref_ResponseQueueInfo_v1', ((1, 'pqinfoResponse'),)))
    IMSMQMessage3.get_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AppSpecific', ((1, 'plAppSpecific'),)))
    IMSMQMessage3.put_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AppSpecific', ((1, 'lAppSpecific'),)))
    IMSMQMessage3.get_SourceMachineGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_SourceMachineGuid', ((1, 'pbstrGuidSrcMachine'),)))
    IMSMQMessage3.get_BodyLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_BodyLength', ((1, 'pcbBody'),)))
    IMSMQMessage3.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(27, 'get_Body', ((1, 'pvarBody'),)))
    IMSMQMessage3.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(28, 'put_Body', ((1, 'varBody'),)))
    IMSMQMessage3.get_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(29, 'get_AdminQueueInfo_v1', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage3.putref_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(30, 'putref_AdminQueueInfo_v1', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage3.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'get_Id', ((1, 'pvarMsgId'),)))
    IMSMQMessage3.get_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'get_CorrelationId', ((1, 'pvarMsgId'),)))
    IMSMQMessage3.put_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(33, 'put_CorrelationId', ((1, 'varMsgId'),)))
    IMSMQMessage3.get_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'get_Ack', ((1, 'plAck'),)))
    IMSMQMessage3.put_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'put_Ack', ((1, 'lAck'),)))
    IMSMQMessage3.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQMessage3.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQMessage3.get_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'get_MaxTimeToReachQueue', ((1, 'plMaxTimeToReachQueue'),)))
    IMSMQMessage3.put_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'put_MaxTimeToReachQueue', ((1, 'lMaxTimeToReachQueue'),)))
    IMSMQMessage3.get_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'get_MaxTimeToReceive', ((1, 'plMaxTimeToReceive'),)))
    IMSMQMessage3.put_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(41, 'put_MaxTimeToReceive', ((1, 'lMaxTimeToReceive'),)))
    IMSMQMessage3.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'get_HashAlgorithm', ((1, 'plHashAlg'),)))
    IMSMQMessage3.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'put_HashAlgorithm', ((1, 'lHashAlg'),)))
    IMSMQMessage3.get_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'get_EncryptAlgorithm', ((1, 'plEncryptAlg'),)))
    IMSMQMessage3.put_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'put_EncryptAlgorithm', ((1, 'lEncryptAlg'),)))
    IMSMQMessage3.get_SentTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(46, 'get_SentTime', ((1, 'pvarSentTime'),)))
    IMSMQMessage3.get_ArrivedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(47, 'get_ArrivedTime', ((1, 'plArrivedTime'),)))
    IMSMQMessage3.get_DestinationQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(48, 'get_DestinationQueueInfo', ((1, 'ppqinfoDest'),)))
    IMSMQMessage3.get_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'get_SenderCertificate', ((1, 'pvarSenderCert'),)))
    IMSMQMessage3.put_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(50, 'put_SenderCertificate', ((1, 'varSenderCert'),)))
    IMSMQMessage3.get_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(51, 'get_SenderId', ((1, 'pvarSenderId'),)))
    IMSMQMessage3.get_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'get_SenderIdType', ((1, 'plSenderIdType'),)))
    IMSMQMessage3.put_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'put_SenderIdType', ((1, 'lSenderIdType'),)))
    IMSMQMessage3.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'Send', ((1, 'DestinationQueue'),(1, 'Transaction'),)))
    IMSMQMessage3.AttachCurrentSecurityContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(55, 'AttachCurrentSecurityContext', ()))
    IMSMQMessage3.get_SenderVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(56, 'get_SenderVersion', ((1, 'plSenderVersion'),)))
    IMSMQMessage3.get_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(57, 'get_Extension', ((1, 'pvarExtension'),)))
    IMSMQMessage3.put_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(58, 'put_Extension', ((1, 'varExtension'),)))
    IMSMQMessage3.get_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(59, 'get_ConnectorTypeGuid', ((1, 'pbstrGuidConnectorType'),)))
    IMSMQMessage3.put_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(60, 'put_ConnectorTypeGuid', ((1, 'bstrGuidConnectorType'),)))
    IMSMQMessage3.get_TransactionStatusQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(61, 'get_TransactionStatusQueueInfo', ((1, 'ppqinfoXactStatus'),)))
    IMSMQMessage3.get_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(62, 'get_DestinationSymmetricKey', ((1, 'pvarDestSymmKey'),)))
    IMSMQMessage3.put_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(63, 'put_DestinationSymmetricKey', ((1, 'varDestSymmKey'),)))
    IMSMQMessage3.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(64, 'get_Signature', ((1, 'pvarSignature'),)))
    IMSMQMessage3.put_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(65, 'put_Signature', ((1, 'varSignature'),)))
    IMSMQMessage3.get_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(66, 'get_AuthenticationProviderType', ((1, 'plAuthProvType'),)))
    IMSMQMessage3.put_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(67, 'put_AuthenticationProviderType', ((1, 'lAuthProvType'),)))
    IMSMQMessage3.get_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(68, 'get_AuthenticationProviderName', ((1, 'pbstrAuthProvName'),)))
    IMSMQMessage3.put_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(69, 'put_AuthenticationProviderName', ((1, 'bstrAuthProvName'),)))
    IMSMQMessage3.put_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(70, 'put_SenderId', ((1, 'varSenderId'),)))
    IMSMQMessage3.get_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_MsgClass', ((1, 'plMsgClass'),)))
    IMSMQMessage3.put_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(72, 'put_MsgClass', ((1, 'lMsgClass'),)))
    IMSMQMessage3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(73, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQMessage3.get_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(74, 'get_TransactionId', ((1, 'pvarXactId'),)))
    IMSMQMessage3.get_IsFirstInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(75, 'get_IsFirstInTransaction', ((1, 'pisFirstInXact'),)))
    IMSMQMessage3.get_IsLastInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(76, 'get_IsLastInTransaction', ((1, 'pisLastInXact'),)))
    IMSMQMessage3.get_ResponseQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(77, 'get_ResponseQueueInfo_v2', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage3.putref_ResponseQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(78, 'putref_ResponseQueueInfo_v2', ((1, 'pqinfoResponse'),)))
    IMSMQMessage3.get_AdminQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(79, 'get_AdminQueueInfo_v2', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage3.putref_AdminQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(80, 'putref_AdminQueueInfo_v2', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage3.get_ReceivedAuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(81, 'get_ReceivedAuthenticationLevel', ((1, 'psReceivedAuthenticationLevel'),)))
    IMSMQMessage3.get_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(82, 'get_ResponseQueueInfo', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage3.putref_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo3_head, use_last_error=False)(83, 'putref_ResponseQueueInfo', ((1, 'pqinfoResponse'),)))
    IMSMQMessage3.get_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo3_head), use_last_error=False)(84, 'get_AdminQueueInfo', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage3.putref_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo3_head, use_last_error=False)(85, 'putref_AdminQueueInfo', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage3.get_ResponseDestination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(86, 'get_ResponseDestination', ((1, 'ppdestResponse'),)))
    IMSMQMessage3.putref_ResponseDestination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(87, 'putref_ResponseDestination', ((1, 'pdestResponse'),)))
    IMSMQMessage3.get_Destination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(88, 'get_Destination', ((1, 'ppdestDestination'),)))
    IMSMQMessage3.get_LookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(89, 'get_LookupId', ((1, 'pvarLookupId'),)))
    IMSMQMessage3.get_IsAuthenticated2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(90, 'get_IsAuthenticated2', ((1, 'pisAuthenticated'),)))
    IMSMQMessage3.get_IsFirstInTransaction2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(91, 'get_IsFirstInTransaction2', ((1, 'pisFirstInXact'),)))
    IMSMQMessage3.get_IsLastInTransaction2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(92, 'get_IsLastInTransaction2', ((1, 'pisLastInXact'),)))
    IMSMQMessage3.AttachCurrentSecurityContext2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(93, 'AttachCurrentSecurityContext2', ()))
    IMSMQMessage3.get_SoapEnvelope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(94, 'get_SoapEnvelope', ((1, 'pbstrSoapEnvelope'),)))
    IMSMQMessage3.get_CompoundMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(95, 'get_CompoundMessage', ((1, 'pvarCompoundMessage'),)))
    IMSMQMessage3.put_SoapHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(96, 'put_SoapHeader', ((1, 'bstrSoapHeader'),)))
    IMSMQMessage3.put_SoapBody = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(97, 'put_SoapBody', ((1, 'bstrSoapBody'),)))
    win32more.System.Com.IDispatch
    return IMSMQMessage3
def _define_IMSMQMessage4_head():
    class IMSMQMessage4(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b23-2168-11d3-898c-00e02c074f6b')
    return IMSMQMessage4
def _define_IMSMQMessage4():
    IMSMQMessage4 = win32more.System.MessageQueuing.IMSMQMessage4_head
    IMSMQMessage4.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Class', ((1, 'plClass'),)))
    IMSMQMessage4.get_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_PrivLevel', ((1, 'plPrivLevel'),)))
    IMSMQMessage4.put_PrivLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_PrivLevel', ((1, 'lPrivLevel'),)))
    IMSMQMessage4.get_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_AuthLevel', ((1, 'plAuthLevel'),)))
    IMSMQMessage4.put_AuthLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_AuthLevel', ((1, 'lAuthLevel'),)))
    IMSMQMessage4.get_IsAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_IsAuthenticated', ((1, 'pisAuthenticated'),)))
    IMSMQMessage4.get_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Delivery', ((1, 'plDelivery'),)))
    IMSMQMessage4.put_Delivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Delivery', ((1, 'lDelivery'),)))
    IMSMQMessage4.get_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Trace', ((1, 'plTrace'),)))
    IMSMQMessage4.put_Trace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Trace', ((1, 'lTrace'),)))
    IMSMQMessage4.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Priority', ((1, 'plPriority'),)))
    IMSMQMessage4.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_Priority', ((1, 'lPriority'),)))
    IMSMQMessage4.get_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_Journal', ((1, 'plJournal'),)))
    IMSMQMessage4.put_Journal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_Journal', ((1, 'lJournal'),)))
    IMSMQMessage4.get_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(21, 'get_ResponseQueueInfo_v1', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage4.putref_ResponseQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(22, 'putref_ResponseQueueInfo_v1', ((1, 'pqinfoResponse'),)))
    IMSMQMessage4.get_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AppSpecific', ((1, 'plAppSpecific'),)))
    IMSMQMessage4.put_AppSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AppSpecific', ((1, 'lAppSpecific'),)))
    IMSMQMessage4.get_SourceMachineGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_SourceMachineGuid', ((1, 'pbstrGuidSrcMachine'),)))
    IMSMQMessage4.get_BodyLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'get_BodyLength', ((1, 'pcbBody'),)))
    IMSMQMessage4.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(27, 'get_Body', ((1, 'pvarBody'),)))
    IMSMQMessage4.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(28, 'put_Body', ((1, 'varBody'),)))
    IMSMQMessage4.get_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo_head), use_last_error=False)(29, 'get_AdminQueueInfo_v1', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage4.putref_AdminQueueInfo_v1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo_head, use_last_error=False)(30, 'putref_AdminQueueInfo_v1', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage4.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'get_Id', ((1, 'pvarMsgId'),)))
    IMSMQMessage4.get_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'get_CorrelationId', ((1, 'pvarMsgId'),)))
    IMSMQMessage4.put_CorrelationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(33, 'put_CorrelationId', ((1, 'varMsgId'),)))
    IMSMQMessage4.get_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'get_Ack', ((1, 'plAck'),)))
    IMSMQMessage4.put_Ack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'put_Ack', ((1, 'lAck'),)))
    IMSMQMessage4.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_Label', ((1, 'pbstrLabel'),)))
    IMSMQMessage4.put_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_Label', ((1, 'bstrLabel'),)))
    IMSMQMessage4.get_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'get_MaxTimeToReachQueue', ((1, 'plMaxTimeToReachQueue'),)))
    IMSMQMessage4.put_MaxTimeToReachQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'put_MaxTimeToReachQueue', ((1, 'lMaxTimeToReachQueue'),)))
    IMSMQMessage4.get_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'get_MaxTimeToReceive', ((1, 'plMaxTimeToReceive'),)))
    IMSMQMessage4.put_MaxTimeToReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(41, 'put_MaxTimeToReceive', ((1, 'lMaxTimeToReceive'),)))
    IMSMQMessage4.get_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'get_HashAlgorithm', ((1, 'plHashAlg'),)))
    IMSMQMessage4.put_HashAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'put_HashAlgorithm', ((1, 'lHashAlg'),)))
    IMSMQMessage4.get_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'get_EncryptAlgorithm', ((1, 'plEncryptAlg'),)))
    IMSMQMessage4.put_EncryptAlgorithm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'put_EncryptAlgorithm', ((1, 'lEncryptAlg'),)))
    IMSMQMessage4.get_SentTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(46, 'get_SentTime', ((1, 'pvarSentTime'),)))
    IMSMQMessage4.get_ArrivedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(47, 'get_ArrivedTime', ((1, 'plArrivedTime'),)))
    IMSMQMessage4.get_DestinationQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(48, 'get_DestinationQueueInfo', ((1, 'ppqinfoDest'),)))
    IMSMQMessage4.get_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'get_SenderCertificate', ((1, 'pvarSenderCert'),)))
    IMSMQMessage4.put_SenderCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(50, 'put_SenderCertificate', ((1, 'varSenderCert'),)))
    IMSMQMessage4.get_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(51, 'get_SenderId', ((1, 'pvarSenderId'),)))
    IMSMQMessage4.get_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'get_SenderIdType', ((1, 'plSenderIdType'),)))
    IMSMQMessage4.put_SenderIdType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'put_SenderIdType', ((1, 'lSenderIdType'),)))
    IMSMQMessage4.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(54, 'Send', ((1, 'DestinationQueue'),(1, 'Transaction'),)))
    IMSMQMessage4.AttachCurrentSecurityContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(55, 'AttachCurrentSecurityContext', ()))
    IMSMQMessage4.get_SenderVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(56, 'get_SenderVersion', ((1, 'plSenderVersion'),)))
    IMSMQMessage4.get_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(57, 'get_Extension', ((1, 'pvarExtension'),)))
    IMSMQMessage4.put_Extension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(58, 'put_Extension', ((1, 'varExtension'),)))
    IMSMQMessage4.get_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(59, 'get_ConnectorTypeGuid', ((1, 'pbstrGuidConnectorType'),)))
    IMSMQMessage4.put_ConnectorTypeGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(60, 'put_ConnectorTypeGuid', ((1, 'bstrGuidConnectorType'),)))
    IMSMQMessage4.get_TransactionStatusQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(61, 'get_TransactionStatusQueueInfo', ((1, 'ppqinfoXactStatus'),)))
    IMSMQMessage4.get_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(62, 'get_DestinationSymmetricKey', ((1, 'pvarDestSymmKey'),)))
    IMSMQMessage4.put_DestinationSymmetricKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(63, 'put_DestinationSymmetricKey', ((1, 'varDestSymmKey'),)))
    IMSMQMessage4.get_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(64, 'get_Signature', ((1, 'pvarSignature'),)))
    IMSMQMessage4.put_Signature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(65, 'put_Signature', ((1, 'varSignature'),)))
    IMSMQMessage4.get_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(66, 'get_AuthenticationProviderType', ((1, 'plAuthProvType'),)))
    IMSMQMessage4.put_AuthenticationProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(67, 'put_AuthenticationProviderType', ((1, 'lAuthProvType'),)))
    IMSMQMessage4.get_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(68, 'get_AuthenticationProviderName', ((1, 'pbstrAuthProvName'),)))
    IMSMQMessage4.put_AuthenticationProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(69, 'put_AuthenticationProviderName', ((1, 'bstrAuthProvName'),)))
    IMSMQMessage4.put_SenderId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(70, 'put_SenderId', ((1, 'varSenderId'),)))
    IMSMQMessage4.get_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_MsgClass', ((1, 'plMsgClass'),)))
    IMSMQMessage4.put_MsgClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(72, 'put_MsgClass', ((1, 'lMsgClass'),)))
    IMSMQMessage4.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(73, 'get_Properties', ((1, 'ppcolProperties'),)))
    IMSMQMessage4.get_TransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(74, 'get_TransactionId', ((1, 'pvarXactId'),)))
    IMSMQMessage4.get_IsFirstInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(75, 'get_IsFirstInTransaction', ((1, 'pisFirstInXact'),)))
    IMSMQMessage4.get_IsLastInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(76, 'get_IsLastInTransaction', ((1, 'pisLastInXact'),)))
    IMSMQMessage4.get_ResponseQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(77, 'get_ResponseQueueInfo_v2', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage4.putref_ResponseQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(78, 'putref_ResponseQueueInfo_v2', ((1, 'pqinfoResponse'),)))
    IMSMQMessage4.get_AdminQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo2_head), use_last_error=False)(79, 'get_AdminQueueInfo_v2', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage4.putref_AdminQueueInfo_v2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo2_head, use_last_error=False)(80, 'putref_AdminQueueInfo_v2', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage4.get_ReceivedAuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(81, 'get_ReceivedAuthenticationLevel', ((1, 'psReceivedAuthenticationLevel'),)))
    IMSMQMessage4.get_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(82, 'get_ResponseQueueInfo', ((1, 'ppqinfoResponse'),)))
    IMSMQMessage4.putref_ResponseQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo4_head, use_last_error=False)(83, 'putref_ResponseQueueInfo', ((1, 'pqinfoResponse'),)))
    IMSMQMessage4.get_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQQueueInfo4_head), use_last_error=False)(84, 'get_AdminQueueInfo', ((1, 'ppqinfoAdmin'),)))
    IMSMQMessage4.putref_AdminQueueInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueueInfo4_head, use_last_error=False)(85, 'putref_AdminQueueInfo', ((1, 'pqinfoAdmin'),)))
    IMSMQMessage4.get_ResponseDestination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(86, 'get_ResponseDestination', ((1, 'ppdestResponse'),)))
    IMSMQMessage4.putref_ResponseDestination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(87, 'putref_ResponseDestination', ((1, 'pdestResponse'),)))
    IMSMQMessage4.get_Destination = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(88, 'get_Destination', ((1, 'ppdestDestination'),)))
    IMSMQMessage4.get_LookupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(89, 'get_LookupId', ((1, 'pvarLookupId'),)))
    IMSMQMessage4.get_IsAuthenticated2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(90, 'get_IsAuthenticated2', ((1, 'pisAuthenticated'),)))
    IMSMQMessage4.get_IsFirstInTransaction2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(91, 'get_IsFirstInTransaction2', ((1, 'pisFirstInXact'),)))
    IMSMQMessage4.get_IsLastInTransaction2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(92, 'get_IsLastInTransaction2', ((1, 'pisLastInXact'),)))
    IMSMQMessage4.AttachCurrentSecurityContext2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(93, 'AttachCurrentSecurityContext2', ()))
    IMSMQMessage4.get_SoapEnvelope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(94, 'get_SoapEnvelope', ((1, 'pbstrSoapEnvelope'),)))
    IMSMQMessage4.get_CompoundMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(95, 'get_CompoundMessage', ((1, 'pvarCompoundMessage'),)))
    IMSMQMessage4.put_SoapHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(96, 'put_SoapHeader', ((1, 'bstrSoapHeader'),)))
    IMSMQMessage4.put_SoapBody = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(97, 'put_SoapBody', ((1, 'bstrSoapBody'),)))
    win32more.System.Com.IDispatch
    return IMSMQMessage4
def _define_IMSMQPrivateEvent_head():
    class IMSMQPrivateEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7ab3341-c9d3-11d1-bb47-0080c7c5a2c0')
    return IMSMQPrivateEvent
def _define_IMSMQPrivateEvent():
    IMSMQPrivateEvent = win32more.System.MessageQueuing.IMSMQPrivateEvent_head
    IMSMQPrivateEvent.get_Hwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Hwnd', ((1, 'phwnd'),)))
    IMSMQPrivateEvent.FireArrivedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueue_head,Int32, use_last_error=False)(8, 'FireArrivedEvent', ((1, 'pq'),(1, 'msgcursor'),)))
    IMSMQPrivateEvent.FireArrivedErrorEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.MessageQueuing.IMSMQQueue_head,win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'FireArrivedErrorEvent', ((1, 'pq'),(1, 'hrStatus'),(1, 'msgcursor'),)))
    win32more.System.Com.IDispatch
    return IMSMQPrivateEvent
def _define__DMSMQEventEvents_head():
    class _DMSMQEventEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e078-dccd-11d0-aa4b-0060970debae')
    return _DMSMQEventEvents
def _define__DMSMQEventEvents():
    _DMSMQEventEvents = win32more.System.MessageQueuing._DMSMQEventEvents_head
    win32more.System.Com.IDispatch
    return _DMSMQEventEvents
def _define_IMSMQTransaction2_head():
    class IMSMQTransaction2(win32more.System.MessageQueuing.IMSMQTransaction_head):
        Guid = Guid('2ce0c5b0-6e67-11d2-b0e6-00e02c074f6b')
    return IMSMQTransaction2
def _define_IMSMQTransaction2():
    IMSMQTransaction2 = win32more.System.MessageQueuing.IMSMQTransaction2_head
    IMSMQTransaction2.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'InitNew', ((1, 'varTransaction'),)))
    IMSMQTransaction2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(11, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.MessageQueuing.IMSMQTransaction
    return IMSMQTransaction2
def _define_IMSMQTransaction3_head():
    class IMSMQTransaction3(win32more.System.MessageQueuing.IMSMQTransaction2_head):
        Guid = Guid('eba96b13-2168-11d3-898c-00e02c074f6b')
    return IMSMQTransaction3
def _define_IMSMQTransaction3():
    IMSMQTransaction3 = win32more.System.MessageQueuing.IMSMQTransaction3_head
    IMSMQTransaction3.get_ITransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'get_ITransaction', ((1, 'pvarITransaction'),)))
    win32more.System.MessageQueuing.IMSMQTransaction2
    return IMSMQTransaction3
def _define_IMSMQCoordinatedTransactionDispenser2_head():
    class IMSMQCoordinatedTransactionDispenser2(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b10-2168-11d3-898c-00e02c074f6b')
    return IMSMQCoordinatedTransactionDispenser2
def _define_IMSMQCoordinatedTransactionDispenser2():
    IMSMQCoordinatedTransactionDispenser2 = win32more.System.MessageQueuing.IMSMQCoordinatedTransactionDispenser2_head
    IMSMQCoordinatedTransactionDispenser2.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction2_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    IMSMQCoordinatedTransactionDispenser2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQCoordinatedTransactionDispenser2
def _define_IMSMQCoordinatedTransactionDispenser3_head():
    class IMSMQCoordinatedTransactionDispenser3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b14-2168-11d3-898c-00e02c074f6b')
    return IMSMQCoordinatedTransactionDispenser3
def _define_IMSMQCoordinatedTransactionDispenser3():
    IMSMQCoordinatedTransactionDispenser3 = win32more.System.MessageQueuing.IMSMQCoordinatedTransactionDispenser3_head
    IMSMQCoordinatedTransactionDispenser3.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction3_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    IMSMQCoordinatedTransactionDispenser3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQCoordinatedTransactionDispenser3
def _define_IMSMQTransactionDispenser2_head():
    class IMSMQTransactionDispenser2(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b11-2168-11d3-898c-00e02c074f6b')
    return IMSMQTransactionDispenser2
def _define_IMSMQTransactionDispenser2():
    IMSMQTransactionDispenser2 = win32more.System.MessageQueuing.IMSMQTransactionDispenser2_head
    IMSMQTransactionDispenser2.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction2_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    IMSMQTransactionDispenser2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQTransactionDispenser2
def _define_IMSMQTransactionDispenser3_head():
    class IMSMQTransactionDispenser3(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b15-2168-11d3-898c-00e02c074f6b')
    return IMSMQTransactionDispenser3
def _define_IMSMQTransactionDispenser3():
    IMSMQTransactionDispenser3 = win32more.System.MessageQueuing.IMSMQTransactionDispenser3_head
    IMSMQTransactionDispenser3.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQTransaction3_head), use_last_error=False)(7, 'BeginTransaction', ((1, 'ptransaction'),)))
    IMSMQTransactionDispenser3.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQTransactionDispenser3
def _define_IMSMQApplication_head():
    class IMSMQApplication(win32more.System.Com.IDispatch_head):
        Guid = Guid('d7d6e085-dccd-11d0-aa4b-0060970debae')
    return IMSMQApplication
def _define_IMSMQApplication():
    IMSMQApplication = win32more.System.MessageQueuing.IMSMQApplication_head
    IMSMQApplication.MachineIdOfMachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'MachineIdOfMachineName', ((1, 'MachineName'),(1, 'pbstrGuid'),)))
    win32more.System.Com.IDispatch
    return IMSMQApplication
def _define_IMSMQApplication2_head():
    class IMSMQApplication2(win32more.System.MessageQueuing.IMSMQApplication_head):
        Guid = Guid('12a30900-7300-11d2-b0e6-00e02c074f6b')
    return IMSMQApplication2
def _define_IMSMQApplication2():
    IMSMQApplication2 = win32more.System.MessageQueuing.IMSMQApplication2_head
    IMSMQApplication2.RegisterCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'RegisterCertificate', ((1, 'Flags'),(1, 'ExternalCertificate'),)))
    IMSMQApplication2.MachineNameOfMachineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'MachineNameOfMachineId', ((1, 'bstrGuid'),(1, 'pbstrMachineName'),)))
    IMSMQApplication2.get_MSMQVersionMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_MSMQVersionMajor', ((1, 'psMSMQVersionMajor'),)))
    IMSMQApplication2.get_MSMQVersionMinor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_MSMQVersionMinor', ((1, 'psMSMQVersionMinor'),)))
    IMSMQApplication2.get_MSMQVersionBuild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_MSMQVersionBuild', ((1, 'psMSMQVersionBuild'),)))
    IMSMQApplication2.get_IsDsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_IsDsEnabled', ((1, 'pfIsDsEnabled'),)))
    IMSMQApplication2.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(14, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.MessageQueuing.IMSMQApplication
    return IMSMQApplication2
def _define_IMSMQApplication3_head():
    class IMSMQApplication3(win32more.System.MessageQueuing.IMSMQApplication2_head):
        Guid = Guid('eba96b1f-2168-11d3-898c-00e02c074f6b')
    return IMSMQApplication3
def _define_IMSMQApplication3():
    IMSMQApplication3 = win32more.System.MessageQueuing.IMSMQApplication3_head
    IMSMQApplication3.get_ActiveQueues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_ActiveQueues', ((1, 'pvActiveQueues'),)))
    IMSMQApplication3.get_PrivateQueues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'get_PrivateQueues', ((1, 'pvPrivateQueues'),)))
    IMSMQApplication3.get_DirectoryServiceServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_DirectoryServiceServer', ((1, 'pbstrDirectoryServiceServer'),)))
    IMSMQApplication3.get_IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_IsConnected', ((1, 'pfIsConnected'),)))
    IMSMQApplication3.get_BytesInAllQueues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'get_BytesInAllQueues', ((1, 'pvBytesInAllQueues'),)))
    IMSMQApplication3.put_Machine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_Machine', ((1, 'bstrMachine'),)))
    IMSMQApplication3.get_Machine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_Machine', ((1, 'pbstrMachine'),)))
    IMSMQApplication3.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'Connect', ()))
    IMSMQApplication3.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Disconnect', ()))
    IMSMQApplication3.Tidy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'Tidy', ()))
    win32more.System.MessageQueuing.IMSMQApplication2
    return IMSMQApplication3
def _define_IMSMQDestination_head():
    class IMSMQDestination(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b16-2168-11d3-898c-00e02c074f6b')
    return IMSMQDestination
def _define_IMSMQDestination():
    IMSMQDestination = win32more.System.MessageQueuing.IMSMQDestination_head
    IMSMQDestination.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Open', ()))
    IMSMQDestination.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Close', ()))
    IMSMQDestination.get_IsOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsOpen', ((1, 'pfIsOpen'),)))
    IMSMQDestination.get_IADs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(10, 'get_IADs', ((1, 'ppIADs'),)))
    IMSMQDestination.putref_IADs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(11, 'putref_IADs', ((1, 'pIADs'),)))
    IMSMQDestination.get_ADsPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_ADsPath', ((1, 'pbstrADsPath'),)))
    IMSMQDestination.put_ADsPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'put_ADsPath', ((1, 'bstrADsPath'),)))
    IMSMQDestination.get_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_PathName', ((1, 'pbstrPathName'),)))
    IMSMQDestination.put_PathName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_PathName', ((1, 'bstrPathName'),)))
    IMSMQDestination.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQDestination.put_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(17, 'put_FormatName', ((1, 'bstrFormatName'),)))
    IMSMQDestination.get_Destinations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(18, 'get_Destinations', ((1, 'ppDestinations'),)))
    IMSMQDestination.putref_Destinations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(19, 'putref_Destinations', ((1, 'pDestinations'),)))
    IMSMQDestination.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(20, 'get_Properties', ((1, 'ppcolProperties'),)))
    win32more.System.Com.IDispatch
    return IMSMQDestination
def _define_IMSMQPrivateDestination_head():
    class IMSMQPrivateDestination(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba96b17-2168-11d3-898c-00e02c074f6b')
    return IMSMQPrivateDestination
def _define_IMSMQPrivateDestination():
    IMSMQPrivateDestination = win32more.System.MessageQueuing.IMSMQPrivateDestination_head
    IMSMQPrivateDestination.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Handle', ((1, 'pvarHandle'),)))
    IMSMQPrivateDestination.put_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Handle', ((1, 'varHandle'),)))
    win32more.System.Com.IDispatch
    return IMSMQPrivateDestination
def _define_IMSMQCollection_head():
    class IMSMQCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('0188ac2f-ecb3-4173-9779-635ca2039c72')
    return IMSMQCollection
def _define_IMSMQCollection():
    IMSMQCollection = win32more.System.MessageQueuing.IMSMQCollection_head
    IMSMQCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'pvarRet'),)))
    IMSMQCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pCount'),)))
    IMSMQCollection._NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, '_NewEnum', ((1, 'ppunk'),)))
    win32more.System.Com.IDispatch
    return IMSMQCollection
def _define_IMSMQManagement_head():
    class IMSMQManagement(win32more.System.Com.IDispatch_head):
        Guid = Guid('be5f0241-e489-4957-8cc4-a452fcf3e23e')
    return IMSMQManagement
def _define_IMSMQManagement():
    IMSMQManagement = win32more.System.MessageQueuing.IMSMQManagement_head
    IMSMQManagement.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'Init', ((1, 'Machine'),(1, 'Pathname'),(1, 'FormatName'),)))
    IMSMQManagement.get_FormatName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_FormatName', ((1, 'pbstrFormatName'),)))
    IMSMQManagement.get_Machine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Machine', ((1, 'pbstrMachine'),)))
    IMSMQManagement.get_MessageCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_MessageCount', ((1, 'plMessageCount'),)))
    IMSMQManagement.get_ForeignStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_ForeignStatus', ((1, 'plForeignStatus'),)))
    IMSMQManagement.get_QueueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_QueueType', ((1, 'plQueueType'),)))
    IMSMQManagement.get_IsLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_IsLocal', ((1, 'pfIsLocal'),)))
    IMSMQManagement.get_TransactionalStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_TransactionalStatus', ((1, 'plTransactionalStatus'),)))
    IMSMQManagement.get_BytesInQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_BytesInQueue', ((1, 'pvBytesInQueue'),)))
    win32more.System.Com.IDispatch
    return IMSMQManagement
def _define_IMSMQOutgoingQueueManagement_head():
    class IMSMQOutgoingQueueManagement(win32more.System.MessageQueuing.IMSMQManagement_head):
        Guid = Guid('64c478fb-f9b0-4695-8a7f-439ac94326d3')
    return IMSMQOutgoingQueueManagement
def _define_IMSMQOutgoingQueueManagement():
    IMSMQOutgoingQueueManagement = win32more.System.MessageQueuing.IMSMQOutgoingQueueManagement_head
    IMSMQOutgoingQueueManagement.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_State', ((1, 'plState'),)))
    IMSMQOutgoingQueueManagement.get_NextHops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'get_NextHops', ((1, 'pvNextHops'),)))
    IMSMQOutgoingQueueManagement.EodGetSendInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.MessageQueuing.IMSMQCollection_head), use_last_error=False)(18, 'EodGetSendInfo', ((1, 'ppCollection'),)))
    IMSMQOutgoingQueueManagement.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'Resume', ()))
    IMSMQOutgoingQueueManagement.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Pause', ()))
    IMSMQOutgoingQueueManagement.EodResend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'EodResend', ()))
    win32more.System.MessageQueuing.IMSMQManagement
    return IMSMQOutgoingQueueManagement
def _define_IMSMQQueueManagement_head():
    class IMSMQQueueManagement(win32more.System.MessageQueuing.IMSMQManagement_head):
        Guid = Guid('7fbe7759-5760-444d-b8a5-5e7ab9a84cce')
    return IMSMQQueueManagement
def _define_IMSMQQueueManagement():
    IMSMQQueueManagement = win32more.System.MessageQueuing.IMSMQQueueManagement_head
    IMSMQQueueManagement.get_JournalMessageCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_JournalMessageCount', ((1, 'plJournalMessageCount'),)))
    IMSMQQueueManagement.get_BytesInJournal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'get_BytesInJournal', ((1, 'pvBytesInJournal'),)))
    IMSMQQueueManagement.EodGetReceiveInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'EodGetReceiveInfo', ((1, 'pvCollection'),)))
    win32more.System.MessageQueuing.IMSMQManagement
    return IMSMQQueueManagement
__all__ = [
    "PRLT",
    "PRLE",
    "PRGT",
    "PRGE",
    "PREQ",
    "PRNE",
    "QUERY_SORTASCEND",
    "QUERY_SORTDESCEND",
    "MQ_MOVE_ACCESS",
    "MQ_ACTION_RECEIVE",
    "MQ_ACTION_PEEK_CURRENT",
    "MQ_ACTION_PEEK_NEXT",
    "MQ_LOOKUP_PEEK_CURRENT",
    "MQ_LOOKUP_PEEK_NEXT",
    "MQ_LOOKUP_PEEK_PREV",
    "MQ_LOOKUP_PEEK_FIRST",
    "MQ_LOOKUP_PEEK_LAST",
    "MQ_LOOKUP_RECEIVE_CURRENT",
    "MQ_LOOKUP_RECEIVE_NEXT",
    "MQ_LOOKUP_RECEIVE_PREV",
    "MQ_LOOKUP_RECEIVE_FIRST",
    "MQ_LOOKUP_RECEIVE_LAST",
    "MQ_LOOKUP_RECEIVE_ALLOW_PEEK",
    "PROPID_M_BASE",
    "PROPID_M_CLASS",
    "PROPID_M_MSGID",
    "PROPID_M_CORRELATIONID",
    "PROPID_M_PRIORITY",
    "PROPID_M_DELIVERY",
    "PROPID_M_ACKNOWLEDGE",
    "PROPID_M_JOURNAL",
    "PROPID_M_APPSPECIFIC",
    "PROPID_M_BODY",
    "PROPID_M_BODY_SIZE",
    "PROPID_M_LABEL",
    "PROPID_M_LABEL_LEN",
    "PROPID_M_TIME_TO_REACH_QUEUE",
    "PROPID_M_TIME_TO_BE_RECEIVED",
    "PROPID_M_RESP_QUEUE",
    "PROPID_M_RESP_QUEUE_LEN",
    "PROPID_M_ADMIN_QUEUE",
    "PROPID_M_ADMIN_QUEUE_LEN",
    "PROPID_M_VERSION",
    "PROPID_M_SENDERID",
    "PROPID_M_SENDERID_LEN",
    "PROPID_M_SENDERID_TYPE",
    "PROPID_M_PRIV_LEVEL",
    "PROPID_M_AUTH_LEVEL",
    "PROPID_M_AUTHENTICATED",
    "PROPID_M_HASH_ALG",
    "PROPID_M_ENCRYPTION_ALG",
    "PROPID_M_SENDER_CERT",
    "PROPID_M_SENDER_CERT_LEN",
    "PROPID_M_SRC_MACHINE_ID",
    "PROPID_M_SENTTIME",
    "PROPID_M_ARRIVEDTIME",
    "PROPID_M_DEST_QUEUE",
    "PROPID_M_DEST_QUEUE_LEN",
    "PROPID_M_EXTENSION",
    "PROPID_M_EXTENSION_LEN",
    "PROPID_M_SECURITY_CONTEXT",
    "PROPID_M_CONNECTOR_TYPE",
    "PROPID_M_XACT_STATUS_QUEUE",
    "PROPID_M_XACT_STATUS_QUEUE_LEN",
    "PROPID_M_TRACE",
    "PROPID_M_BODY_TYPE",
    "PROPID_M_DEST_SYMM_KEY",
    "PROPID_M_DEST_SYMM_KEY_LEN",
    "PROPID_M_SIGNATURE",
    "PROPID_M_SIGNATURE_LEN",
    "PROPID_M_PROV_TYPE",
    "PROPID_M_PROV_NAME",
    "PROPID_M_PROV_NAME_LEN",
    "PROPID_M_FIRST_IN_XACT",
    "PROPID_M_LAST_IN_XACT",
    "PROPID_M_XACTID",
    "PROPID_M_AUTHENTICATED_EX",
    "PROPID_M_RESP_FORMAT_NAME",
    "PROPID_M_RESP_FORMAT_NAME_LEN",
    "PROPID_M_DEST_FORMAT_NAME",
    "PROPID_M_DEST_FORMAT_NAME_LEN",
    "PROPID_M_LOOKUPID",
    "PROPID_M_SOAP_ENVELOPE",
    "PROPID_M_SOAP_ENVELOPE_LEN",
    "PROPID_M_COMPOUND_MESSAGE",
    "PROPID_M_COMPOUND_MESSAGE_SIZE",
    "PROPID_M_SOAP_HEADER",
    "PROPID_M_SOAP_BODY",
    "PROPID_M_DEADLETTER_QUEUE",
    "PROPID_M_DEADLETTER_QUEUE_LEN",
    "PROPID_M_ABORT_COUNT",
    "PROPID_M_MOVE_COUNT",
    "PROPID_M_LAST_MOVE_TIME",
    "PROPID_M_MSGID_SIZE",
    "PROPID_M_CORRELATIONID_SIZE",
    "PROPID_M_XACTID_SIZE",
    "MQMSG_PRIV_LEVEL_BODY_AES",
    "MQMSG_AUTHENTICATED_QM_MESSAGE",
    "MQMSG_NOT_FIRST_IN_XACT",
    "MQMSG_FIRST_IN_XACT",
    "MQMSG_NOT_LAST_IN_XACT",
    "MQMSG_LAST_IN_XACT",
    "PROPID_Q_BASE",
    "PROPID_Q_INSTANCE",
    "PROPID_Q_TYPE",
    "PROPID_Q_PATHNAME",
    "PROPID_Q_JOURNAL",
    "PROPID_Q_QUOTA",
    "PROPID_Q_BASEPRIORITY",
    "PROPID_Q_JOURNAL_QUOTA",
    "PROPID_Q_LABEL",
    "PROPID_Q_CREATE_TIME",
    "PROPID_Q_MODIFY_TIME",
    "PROPID_Q_AUTHENTICATE",
    "PROPID_Q_PRIV_LEVEL",
    "PROPID_Q_TRANSACTION",
    "PROPID_Q_PATHNAME_DNS",
    "PROPID_Q_MULTICAST_ADDRESS",
    "PROPID_Q_ADS_PATH",
    "PROPID_QM_BASE",
    "PROPID_QM_SITE_ID",
    "PROPID_QM_MACHINE_ID",
    "PROPID_QM_PATHNAME",
    "PROPID_QM_CONNECTION",
    "PROPID_QM_ENCRYPTION_PK",
    "PROPID_QM_ENCRYPTION_PK_BASE",
    "PROPID_QM_ENCRYPTION_PK_ENHANCED",
    "PROPID_QM_PATHNAME_DNS",
    "PROPID_QM_ENCRYPTION_PK_AES",
    "PROPID_PC_BASE",
    "PROPID_PC_VERSION",
    "PROPID_PC_DS_ENABLED",
    "PROPID_MGMT_MSMQ_BASE",
    "PROPID_MGMT_MSMQ_ACTIVEQUEUES",
    "PROPID_MGMT_MSMQ_PRIVATEQ",
    "PROPID_MGMT_MSMQ_DSSERVER",
    "PROPID_MGMT_MSMQ_CONNECTED",
    "PROPID_MGMT_MSMQ_TYPE",
    "PROPID_MGMT_MSMQ_BYTES_IN_ALL_QUEUES",
    "PROPID_MGMT_QUEUE_BASE",
    "PROPID_MGMT_QUEUE_PATHNAME",
    "PROPID_MGMT_QUEUE_FORMATNAME",
    "PROPID_MGMT_QUEUE_TYPE",
    "PROPID_MGMT_QUEUE_LOCATION",
    "PROPID_MGMT_QUEUE_XACT",
    "PROPID_MGMT_QUEUE_FOREIGN",
    "PROPID_MGMT_QUEUE_MESSAGE_COUNT",
    "PROPID_MGMT_QUEUE_BYTES_IN_QUEUE",
    "PROPID_MGMT_QUEUE_JOURNAL_MESSAGE_COUNT",
    "PROPID_MGMT_QUEUE_BYTES_IN_JOURNAL",
    "PROPID_MGMT_QUEUE_STATE",
    "PROPID_MGMT_QUEUE_NEXTHOPS",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK_TIME",
    "PROPID_MGMT_QUEUE_EOD_LAST_ACK_COUNT",
    "PROPID_MGMT_QUEUE_EOD_FIRST_NON_ACK",
    "PROPID_MGMT_QUEUE_EOD_LAST_NON_ACK",
    "PROPID_MGMT_QUEUE_EOD_NEXT_SEQ",
    "PROPID_MGMT_QUEUE_EOD_NO_READ_COUNT",
    "PROPID_MGMT_QUEUE_EOD_NO_ACK_COUNT",
    "PROPID_MGMT_QUEUE_EOD_RESEND_TIME",
    "PROPID_MGMT_QUEUE_EOD_RESEND_INTERVAL",
    "PROPID_MGMT_QUEUE_EOD_RESEND_COUNT",
    "PROPID_MGMT_QUEUE_EOD_SOURCE_INFO",
    "PROPID_MGMT_QUEUE_CONNECTION_HISTORY",
    "PROPID_MGMT_QUEUE_SUBQUEUE_COUNT",
    "PROPID_MGMT_QUEUE_SUBQUEUE_NAMES",
    "PROPID_MGMT_QUEUE_USED_QUOTA",
    "PROPID_MGMT_QUEUE_JOURNAL_USED_QUOTA",
    "LONG_LIVED",
    "MQSEC_DELETE_MESSAGE",
    "MQSEC_PEEK_MESSAGE",
    "MQSEC_WRITE_MESSAGE",
    "MQSEC_DELETE_JOURNAL_MESSAGE",
    "MQSEC_SET_QUEUE_PROPERTIES",
    "MQSEC_GET_QUEUE_PROPERTIES",
    "MQSEC_DELETE_QUEUE",
    "MQSEC_CHANGE_QUEUE_PERMISSIONS",
    "MQSEC_TAKE_QUEUE_OWNERSHIP",
    "MQSEC_QUEUE_GENERIC_EXECUTE",
    "MQ_OK",
    "MQ_ERROR_RESOLVE_ADDRESS",
    "MQ_ERROR_TOO_MANY_PROPERTIES",
    "MQ_ERROR_MESSAGE_NOT_AUTHENTICATED",
    "MQ_ERROR_MESSAGE_LOCKED_UNDER_TRANSACTION",
    "MSMQQuery",
    "MSMQMessage",
    "MSMQQueue",
    "MSMQEvent",
    "MSMQQueueInfo",
    "MSMQQueueInfos",
    "MSMQTransaction",
    "MSMQCoordinatedTransactionDispenser",
    "MSMQTransactionDispenser",
    "MSMQApplication",
    "MSMQDestination",
    "MSMQCollection",
    "MSMQManagement",
    "MSMQOutgoingQueueManagement",
    "MSMQQueueManagement",
    "MQCALG",
    "MQMSG_CALG_MD2",
    "MQMSG_CALG_MD4",
    "MQMSG_CALG_MD5",
    "MQMSG_CALG_SHA",
    "MQMSG_CALG_SHA1",
    "MQMSG_CALG_MAC",
    "MQMSG_CALG_RSA_SIGN",
    "MQMSG_CALG_DSS_SIGN",
    "MQMSG_CALG_RSA_KEYX",
    "MQMSG_CALG_DES",
    "MQMSG_CALG_RC2",
    "MQMSG_CALG_RC4",
    "MQMSG_CALG_SEAL",
    "MQTRANSACTION",
    "MQ_NO_TRANSACTION",
    "MQ_MTS_TRANSACTION",
    "MQ_XA_TRANSACTION",
    "MQ_SINGLE_MESSAGE",
    "RELOPS",
    "REL_NOP",
    "REL_EQ",
    "REL_NEQ",
    "REL_LT",
    "REL_GT",
    "REL_LE",
    "REL_GE",
    "MQCERT_REGISTER",
    "MQCERT_REGISTER_ALWAYS",
    "MQCERT_REGISTER_IF_NOT_EXIST",
    "MQMSGCURSOR",
    "MQMSG_FIRST",
    "MQMSG_CURRENT",
    "MQMSG_NEXT",
    "MQMSGCLASS",
    "MQMSG_CLASS_NORMAL",
    "MQMSG_CLASS_REPORT",
    "MQMSG_CLASS_ACK_REACH_QUEUE",
    "MQMSG_CLASS_ACK_RECEIVE",
    "MQMSG_CLASS_NACK_BAD_DST_Q",
    "MQMSG_CLASS_NACK_PURGED",
    "MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT",
    "MQMSG_CLASS_NACK_Q_EXCEED_QUOTA",
    "MQMSG_CLASS_NACK_ACCESS_DENIED",
    "MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED",
    "MQMSG_CLASS_NACK_BAD_SIGNATURE",
    "MQMSG_CLASS_NACK_BAD_ENCRYPTION",
    "MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT",
    "MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q",
    "MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG",
    "MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER",
    "MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED",
    "MQMSG_CLASS_NACK_Q_DELETED",
    "MQMSG_CLASS_NACK_Q_PURGED",
    "MQMSG_CLASS_NACK_RECEIVE_TIMEOUT",
    "MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER",
    "MQMSGDELIVERY",
    "MQMSG_DELIVERY_EXPRESS",
    "MQMSG_DELIVERY_RECOVERABLE",
    "MQMSGACKNOWLEDGEMENT",
    "MQMSG_ACKNOWLEDGMENT_NONE",
    "MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL",
    "MQMSG_ACKNOWLEDGMENT_POS_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL",
    "MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE",
    "MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE",
    "MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE",
    "MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE",
    "MQMSGJOURNAL",
    "MQMSG_JOURNAL_NONE",
    "MQMSG_DEADLETTER",
    "MQMSG_JOURNAL",
    "MQMSGTRACE",
    "MQMSG_TRACE_NONE",
    "MQMSG_SEND_ROUTE_TO_REPORT_QUEUE",
    "MQMSGSENDERIDTYPE",
    "MQMSG_SENDERID_TYPE_NONE",
    "MQMSG_SENDERID_TYPE_SID",
    "MQMSGPRIVLEVEL",
    "MQMSG_PRIV_LEVEL_NONE",
    "MQMSG_PRIV_LEVEL_BODY_BASE",
    "MQMSG_PRIV_LEVEL_BODY_ENHANCED",
    "MQMSGAUTHLEVEL",
    "MQMSG_AUTH_LEVEL_NONE",
    "MQMSG_AUTH_LEVEL_ALWAYS",
    "MQMSG_AUTH_LEVEL_MSMQ10",
    "MQMSG_AUTH_LEVEL_SIG10",
    "MQMSG_AUTH_LEVEL_MSMQ20",
    "MQMSG_AUTH_LEVEL_SIG20",
    "MQMSG_AUTH_LEVEL_SIG30",
    "MQMSGIDSIZE",
    "MQMSG_MSGID_SIZE",
    "MQMSG_CORRELATIONID_SIZE",
    "MQMSG_XACTID_SIZE",
    "MQMSGMAX",
    "MQ_MAX_MSG_LABEL_LEN",
    "MQMSGAUTHENTICATION",
    "MQMSG_AUTHENTICATION_NOT_REQUESTED",
    "MQMSG_AUTHENTICATION_REQUESTED",
    "MQMSG_AUTHENTICATED_SIG10",
    "MQMSG_AUTHENTICATION_REQUESTED_EX",
    "MQMSG_AUTHENTICATED_SIG20",
    "MQMSG_AUTHENTICATED_SIG30",
    "MQMSG_AUTHENTICATED_SIGXML",
    "MQSHARE",
    "MQ_DENY_NONE",
    "MQ_DENY_RECEIVE_SHARE",
    "MQACCESS",
    "MQ_RECEIVE_ACCESS",
    "MQ_SEND_ACCESS",
    "MQ_PEEK_ACCESS",
    "MQ_ADMIN_ACCESS",
    "MQJOURNAL",
    "MQ_JOURNAL_NONE",
    "MQ_JOURNAL",
    "MQTRANSACTIONAL",
    "MQ_TRANSACTIONAL_NONE",
    "MQ_TRANSACTIONAL",
    "MQAUTHENTICATE",
    "MQ_AUTHENTICATE_NONE",
    "MQ_AUTHENTICATE",
    "MQPRIVLEVEL",
    "MQ_PRIV_LEVEL_NONE",
    "MQ_PRIV_LEVEL_OPTIONAL",
    "MQ_PRIV_LEVEL_BODY",
    "MQPRIORITY",
    "MQ_MIN_PRIORITY",
    "MQ_MAX_PRIORITY",
    "MQMAX",
    "MQ_MAX_Q_NAME_LEN",
    "MQ_MAX_Q_LABEL_LEN",
    "QUEUE_TYPE",
    "MQ_TYPE_PUBLIC",
    "MQ_TYPE_PRIVATE",
    "MQ_TYPE_MACHINE",
    "MQ_TYPE_CONNECTOR",
    "MQ_TYPE_MULTICAST",
    "FOREIGN_STATUS",
    "MQ_STATUS_FOREIGN",
    "MQ_STATUS_NOT_FOREIGN",
    "MQ_STATUS_UNKNOWN",
    "XACT_STATUS",
    "MQ_XACT_STATUS_XACT",
    "MQ_XACT_STATUS_NOT_XACT",
    "MQ_XACT_STATUS_UNKNOWN",
    "QUEUE_STATE",
    "MQ_QUEUE_STATE_LOCAL_CONNECTION",
    "MQ_QUEUE_STATE_DISCONNECTED",
    "MQ_QUEUE_STATE_WAITING",
    "MQ_QUEUE_STATE_NEEDVALIDATE",
    "MQ_QUEUE_STATE_ONHOLD",
    "MQ_QUEUE_STATE_NONACTIVE",
    "MQ_QUEUE_STATE_CONNECTED",
    "MQ_QUEUE_STATE_DISCONNECTING",
    "MQ_QUEUE_STATE_LOCKED",
    "MQDEFAULT",
    "DEFAULT_M_PRIORITY",
    "DEFAULT_M_DELIVERY",
    "DEFAULT_M_ACKNOWLEDGE",
    "DEFAULT_M_JOURNAL",
    "DEFAULT_M_APPSPECIFIC",
    "DEFAULT_M_PRIV_LEVEL",
    "DEFAULT_M_AUTH_LEVEL",
    "DEFAULT_M_SENDERID_TYPE",
    "DEFAULT_Q_JOURNAL",
    "DEFAULT_Q_BASEPRIORITY",
    "DEFAULT_Q_QUOTA",
    "DEFAULT_Q_JOURNAL_QUOTA",
    "DEFAULT_Q_TRANSACTION",
    "DEFAULT_Q_AUTHENTICATE",
    "DEFAULT_Q_PRIV_LEVEL",
    "DEFAULT_M_LOOKUPID",
    "MQERROR",
    "MQ_ERROR",
    "MQ_ERROR_PROPERTY",
    "MQ_ERROR_QUEUE_NOT_FOUND",
    "MQ_ERROR_QUEUE_NOT_ACTIVE",
    "MQ_ERROR_QUEUE_EXISTS",
    "MQ_ERROR_INVALID_PARAMETER",
    "MQ_ERROR_INVALID_HANDLE",
    "MQ_ERROR_OPERATION_CANCELLED",
    "MQ_ERROR_SHARING_VIOLATION",
    "MQ_ERROR_SERVICE_NOT_AVAILABLE",
    "MQ_ERROR_MACHINE_NOT_FOUND",
    "MQ_ERROR_ILLEGAL_SORT",
    "MQ_ERROR_ILLEGAL_USER",
    "MQ_ERROR_NO_DS",
    "MQ_ERROR_ILLEGAL_QUEUE_PATHNAME",
    "MQ_ERROR_ILLEGAL_PROPERTY_VALUE",
    "MQ_ERROR_ILLEGAL_PROPERTY_VT",
    "MQ_ERROR_BUFFER_OVERFLOW",
    "MQ_ERROR_IO_TIMEOUT",
    "MQ_ERROR_ILLEGAL_CURSOR_ACTION",
    "MQ_ERROR_MESSAGE_ALREADY_RECEIVED",
    "MQ_ERROR_ILLEGAL_FORMATNAME",
    "MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL",
    "MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION",
    "MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR",
    "MQ_ERROR_SENDERID_BUFFER_TOO_SMALL",
    "MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL",
    "MQ_ERROR_CANNOT_IMPERSONATE_CLIENT",
    "MQ_ERROR_ACCESS_DENIED",
    "MQ_ERROR_PRIVILEGE_NOT_HELD",
    "MQ_ERROR_INSUFFICIENT_RESOURCES",
    "MQ_ERROR_USER_BUFFER_TOO_SMALL",
    "MQ_ERROR_MESSAGE_STORAGE_FAILED",
    "MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL",
    "MQ_ERROR_INVALID_CERTIFICATE",
    "MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE",
    "MQ_ERROR_INTERNAL_USER_CERT_EXIST",
    "MQ_ERROR_NO_INTERNAL_USER_CERT",
    "MQ_ERROR_CORRUPTED_SECURITY_DATA",
    "MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE",
    "MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION",
    "MQ_ERROR_BAD_SECURITY_CONTEXT",
    "MQ_ERROR_COULD_NOT_GET_USER_SID",
    "MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO",
    "MQ_ERROR_ILLEGAL_MQCOLUMNS",
    "MQ_ERROR_ILLEGAL_PROPID",
    "MQ_ERROR_ILLEGAL_RELATION",
    "MQ_ERROR_ILLEGAL_PROPERTY_SIZE",
    "MQ_ERROR_ILLEGAL_RESTRICTION_PROPID",
    "MQ_ERROR_ILLEGAL_MQQUEUEPROPS",
    "MQ_ERROR_PROPERTY_NOTALLOWED",
    "MQ_ERROR_INSUFFICIENT_PROPERTIES",
    "MQ_ERROR_MACHINE_EXISTS",
    "MQ_ERROR_ILLEGAL_MQQMPROPS",
    "MQ_ERROR_DS_IS_FULL",
    "MQ_ERROR_DS_ERROR",
    "MQ_ERROR_INVALID_OWNER",
    "MQ_ERROR_UNSUPPORTED_ACCESS_MODE",
    "MQ_ERROR_RESULT_BUFFER_TOO_SMALL",
    "MQ_ERROR_DELETE_CN_IN_USE",
    "MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER",
    "MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE",
    "MQ_ERROR_QUEUE_NOT_AVAILABLE",
    "MQ_ERROR_DTC_CONNECT",
    "MQ_ERROR_TRANSACTION_IMPORT",
    "MQ_ERROR_TRANSACTION_USAGE",
    "MQ_ERROR_TRANSACTION_SEQUENCE",
    "MQ_ERROR_MISSING_CONNECTOR_TYPE",
    "MQ_ERROR_STALE_HANDLE",
    "MQ_ERROR_TRANSACTION_ENLIST",
    "MQ_ERROR_QUEUE_DELETED",
    "MQ_ERROR_ILLEGAL_CONTEXT",
    "MQ_ERROR_ILLEGAL_SORT_PROPID",
    "MQ_ERROR_LABEL_TOO_LONG",
    "MQ_ERROR_LABEL_BUFFER_TOO_SMALL",
    "MQ_ERROR_MQIS_SERVER_EMPTY",
    "MQ_ERROR_MQIS_READONLY_MODE",
    "MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL",
    "MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL",
    "MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL",
    "MQ_ERROR_ILLEGAL_OPERATION",
    "MQ_ERROR_WRITE_NOT_ALLOWED",
    "MQ_ERROR_WKS_CANT_SERVE_CLIENT",
    "MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW",
    "MQ_CORRUPTED_QUEUE_WAS_DELETED",
    "MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE",
    "MQ_ERROR_UNSUPPORTED_OPERATION",
    "MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED",
    "MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR",
    "MQ_ERROR_CERTIFICATE_NOT_PROVIDED",
    "MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED",
    "MQ_ERROR_CANT_CREATE_CERT_STORE",
    "MQ_ERROR_CANNOT_CREATE_CERT_STORE",
    "MQ_ERROR_CANT_OPEN_CERT_STORE",
    "MQ_ERROR_CANNOT_OPEN_CERT_STORE",
    "MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION",
    "MQ_ERROR_CANNOT_GRANT_ADD_GUID",
    "MQ_ERROR_CANNOT_LOAD_MSMQOCM",
    "MQ_ERROR_NO_ENTRY_POINT_MSMQOCM",
    "MQ_ERROR_NO_MSMQ_SERVERS_ON_DC",
    "MQ_ERROR_CANNOT_JOIN_DOMAIN",
    "MQ_ERROR_CANNOT_CREATE_ON_GC",
    "MQ_ERROR_GUID_NOT_MATCHING",
    "MQ_ERROR_PUBLIC_KEY_NOT_FOUND",
    "MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST",
    "MQ_ERROR_ILLEGAL_MQPRIVATEPROPS",
    "MQ_ERROR_NO_GC_IN_DOMAIN",
    "MQ_ERROR_NO_MSMQ_SERVERS_ON_GC",
    "MQ_ERROR_CANNOT_GET_DN",
    "MQ_ERROR_CANNOT_HASH_DATA_EX",
    "MQ_ERROR_CANNOT_SIGN_DATA_EX",
    "MQ_ERROR_CANNOT_CREATE_HASH_EX",
    "MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX",
    "MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS",
    "MQ_ERROR_NO_MQUSER_OU",
    "MQ_ERROR_CANNOT_LOAD_MQAD",
    "MQ_ERROR_CANNOT_LOAD_MQDSSRV",
    "MQ_ERROR_PROPERTIES_CONFLICT",
    "MQ_ERROR_MESSAGE_NOT_FOUND",
    "MQ_ERROR_CANT_RESOLVE_SITES",
    "MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS",
    "MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER",
    "MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS",
    "MQ_ERROR_MULTI_SORT_KEYS",
    "MQ_ERROR_GC_NEEDED",
    "MQ_ERROR_DS_BIND_ROOT_FOREST",
    "MQ_ERROR_DS_LOCAL_USER",
    "MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED",
    "MQ_ERROR_BAD_XML_FORMAT",
    "MQ_ERROR_UNSUPPORTED_CLASS",
    "MQ_ERROR_UNINITIALIZED_OBJECT",
    "MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS",
    "MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS",
    "MQWARNING",
    "MQ_INFORMATION_PROPERTY",
    "MQ_INFORMATION_ILLEGAL_PROPERTY",
    "MQ_INFORMATION_PROPERTY_IGNORED",
    "MQ_INFORMATION_UNSUPPORTED_PROPERTY",
    "MQ_INFORMATION_DUPLICATE_PROPERTY",
    "MQ_INFORMATION_OPERATION_PENDING",
    "MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL",
    "MQ_INFORMATION_INTERNAL_USER_CERT_EXIST",
    "MQ_INFORMATION_OWNER_IGNORED",
    "IMSMQQuery",
    "IMSMQQueueInfo",
    "IMSMQQueueInfo2",
    "IMSMQQueueInfo3",
    "IMSMQQueueInfo4",
    "IMSMQQueue",
    "IMSMQQueue2",
    "IMSMQQueue3",
    "IMSMQQueue4",
    "IMSMQMessage",
    "IMSMQQueueInfos",
    "IMSMQQueueInfos2",
    "IMSMQQueueInfos3",
    "IMSMQQueueInfos4",
    "IMSMQEvent",
    "IMSMQEvent2",
    "IMSMQEvent3",
    "IMSMQTransaction",
    "IMSMQCoordinatedTransactionDispenser",
    "IMSMQTransactionDispenser",
    "IMSMQQuery2",
    "IMSMQQuery3",
    "IMSMQQuery4",
    "IMSMQMessage2",
    "IMSMQMessage3",
    "IMSMQMessage4",
    "IMSMQPrivateEvent",
    "_DMSMQEventEvents",
    "IMSMQTransaction2",
    "IMSMQTransaction3",
    "IMSMQCoordinatedTransactionDispenser2",
    "IMSMQCoordinatedTransactionDispenser3",
    "IMSMQTransactionDispenser2",
    "IMSMQTransactionDispenser3",
    "IMSMQApplication",
    "IMSMQApplication2",
    "IMSMQApplication3",
    "IMSMQDestination",
    "IMSMQPrivateDestination",
    "IMSMQCollection",
    "IMSMQManagement",
    "IMSMQOutgoingQueueManagement",
    "IMSMQQueueManagement",
]
