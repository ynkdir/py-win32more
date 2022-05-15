from win32more import *
import win32more.Devices.AllJoyn
import win32more.Foundation
import win32more.Security

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Devices.AllJoyn, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Devices.AllJoyn, name)
def __dir__():
    return __all__
QCC_TRUE = 1
QCC_FALSE = 0
ALLJOYN_MESSAGE_FLAG_NO_REPLY_EXPECTED = 1
ALLJOYN_MESSAGE_FLAG_AUTO_START = 2
ALLJOYN_MESSAGE_FLAG_ALLOW_REMOTE_MSG = 4
ALLJOYN_MESSAGE_FLAG_SESSIONLESS = 16
ALLJOYN_MESSAGE_FLAG_GLOBAL_BROADCAST = 32
ALLJOYN_MESSAGE_FLAG_ENCRYPTED = 128
ALLJOYN_TRAFFIC_TYPE_MESSAGES = 1
ALLJOYN_TRAFFIC_TYPE_RAW_UNRELIABLE = 2
ALLJOYN_TRAFFIC_TYPE_RAW_RELIABLE = 4
ALLJOYN_PROXIMITY_ANY = 255
ALLJOYN_PROXIMITY_PHYSICAL = 1
ALLJOYN_PROXIMITY_NETWORK = 2
ALLJOYN_READ_READY = 1
ALLJOYN_WRITE_READY = 2
ALLJOYN_DISCONNECTED = 4
ALLJOYN_LITTLE_ENDIAN = 108
ALLJOYN_BIG_ENDIAN = 66
ALLJOYN_MESSAGE_DEFAULT_TIMEOUT = 25000
ALLJOYN_CRED_PASSWORD = 1
ALLJOYN_CRED_USER_NAME = 2
ALLJOYN_CRED_CERT_CHAIN = 4
ALLJOYN_CRED_PRIVATE_KEY = 8
ALLJOYN_CRED_LOGON_ENTRY = 16
ALLJOYN_CRED_EXPIRATION = 32
ALLJOYN_CRED_NEW_PASSWORD = 4097
ALLJOYN_CRED_ONE_TIME_PWD = 8193
ALLJOYN_PROP_ACCESS_READ = 1
ALLJOYN_PROP_ACCESS_WRITE = 2
ALLJOYN_PROP_ACCESS_RW = 3
ALLJOYN_MEMBER_ANNOTATE_NO_REPLY = 1
ALLJOYN_MEMBER_ANNOTATE_DEPRECATED = 2
ALLJOYN_MEMBER_ANNOTATE_SESSIONCAST = 4
ALLJOYN_MEMBER_ANNOTATE_SESSIONLESS = 8
ALLJOYN_MEMBER_ANNOTATE_UNICAST = 16
ALLJOYN_MEMBER_ANNOTATE_GLOBAL_BROADCAST = 32
alljoyn_about_announceflag = Int32
UNANNOUNCED = 0
ANNOUNCED = 1
QStatus = Int32
ER_OK = 0
ER_FAIL = 1
ER_UTF_CONVERSION_FAILED = 2
ER_BUFFER_TOO_SMALL = 3
ER_OS_ERROR = 4
ER_OUT_OF_MEMORY = 5
ER_SOCKET_BIND_ERROR = 6
ER_INIT_FAILED = 7
ER_WOULDBLOCK = 8
ER_NOT_IMPLEMENTED = 9
ER_TIMEOUT = 10
ER_SOCK_OTHER_END_CLOSED = 11
ER_BAD_ARG_1 = 12
ER_BAD_ARG_2 = 13
ER_BAD_ARG_3 = 14
ER_BAD_ARG_4 = 15
ER_BAD_ARG_5 = 16
ER_BAD_ARG_6 = 17
ER_BAD_ARG_7 = 18
ER_BAD_ARG_8 = 19
ER_INVALID_ADDRESS = 20
ER_INVALID_DATA = 21
ER_READ_ERROR = 22
ER_WRITE_ERROR = 23
ER_OPEN_FAILED = 24
ER_PARSE_ERROR = 25
ER_END_OF_DATA = 26
ER_CONN_REFUSED = 27
ER_BAD_ARG_COUNT = 28
ER_WARNING = 29
ER_EOF = 30
ER_DEADLOCK = 31
ER_COMMON_ERRORS = 4096
ER_STOPPING_THREAD = 4097
ER_ALERTED_THREAD = 4098
ER_XML_MALFORMED = 4099
ER_AUTH_FAIL = 4100
ER_AUTH_USER_REJECT = 4101
ER_NO_SUCH_ALARM = 4102
ER_TIMER_FALLBEHIND = 4103
ER_SSL_ERRORS = 4104
ER_SSL_INIT = 4105
ER_SSL_CONNECT = 4106
ER_SSL_VERIFY = 4107
ER_EXTERNAL_THREAD = 4108
ER_CRYPTO_ERROR = 4109
ER_CRYPTO_TRUNCATED = 4110
ER_CRYPTO_KEY_UNAVAILABLE = 4111
ER_BAD_HOSTNAME = 4112
ER_CRYPTO_KEY_UNUSABLE = 4113
ER_EMPTY_KEY_BLOB = 4114
ER_CORRUPT_KEYBLOB = 4115
ER_INVALID_KEY_ENCODING = 4116
ER_DEAD_THREAD = 4117
ER_THREAD_RUNNING = 4118
ER_THREAD_STOPPING = 4119
ER_BAD_STRING_ENCODING = 4120
ER_CRYPTO_INSUFFICIENT_SECURITY = 4121
ER_CRYPTO_ILLEGAL_PARAMETERS = 4122
ER_CRYPTO_HASH_UNINITIALIZED = 4123
ER_THREAD_NO_WAIT = 4124
ER_TIMER_EXITING = 4125
ER_INVALID_GUID = 4126
ER_THREADPOOL_EXHAUSTED = 4127
ER_THREADPOOL_STOPPING = 4128
ER_INVALID_STREAM = 4129
ER_TIMER_FULL = 4130
ER_IODISPATCH_STOPPING = 4131
ER_SLAP_INVALID_PACKET_LEN = 4132
ER_SLAP_HDR_CHECKSUM_ERROR = 4133
ER_SLAP_INVALID_PACKET_TYPE = 4134
ER_SLAP_LEN_MISMATCH = 4135
ER_SLAP_PACKET_TYPE_MISMATCH = 4136
ER_SLAP_CRC_ERROR = 4137
ER_SLAP_ERROR = 4138
ER_SLAP_OTHER_END_CLOSED = 4139
ER_TIMER_NOT_ALLOWED = 4140
ER_NOT_CONN = 4141
ER_XML_CONVERTER_ERROR = 8192
ER_XML_INVALID_RULES_COUNT = 8193
ER_XML_INTERFACE_MEMBERS_MISSING = 8194
ER_XML_INVALID_MEMBER_TYPE = 8195
ER_XML_INVALID_MEMBER_ACTION = 8196
ER_XML_MEMBER_DENY_ACTION_WITH_OTHER = 8197
ER_XML_INVALID_ANNOTATIONS_COUNT = 8198
ER_XML_INVALID_ELEMENT_NAME = 8199
ER_XML_INVALID_ATTRIBUTE_VALUE = 8200
ER_XML_INVALID_SECURITY_LEVEL_ANNOTATION_VALUE = 8201
ER_XML_INVALID_ELEMENT_CHILDREN_COUNT = 8202
ER_XML_INVALID_POLICY_VERSION = 8203
ER_XML_INVALID_POLICY_SERIAL_NUMBER = 8204
ER_XML_INVALID_ACL_PEER_TYPE = 8205
ER_XML_INVALID_ACL_PEER_CHILDREN_COUNT = 8206
ER_XML_ACL_ALL_TYPE_PEER_WITH_OTHERS = 8207
ER_XML_INVALID_ACL_PEER_PUBLIC_KEY = 8208
ER_XML_ACL_PEER_NOT_UNIQUE = 8209
ER_XML_ACL_PEER_PUBLIC_KEY_SET = 8210
ER_XML_ACLS_MISSING = 8211
ER_XML_ACL_PEERS_MISSING = 8212
ER_XML_INVALID_OBJECT_PATH = 8213
ER_XML_INVALID_INTERFACE_NAME = 8214
ER_XML_INVALID_MEMBER_NAME = 8215
ER_XML_INVALID_MANIFEST_VERSION = 8216
ER_XML_INVALID_OID = 8217
ER_XML_INVALID_BASE64 = 8218
ER_XML_INTERFACE_NAME_NOT_UNIQUE = 8219
ER_XML_MEMBER_NAME_NOT_UNIQUE = 8220
ER_XML_OBJECT_PATH_NOT_UNIQUE = 8221
ER_XML_ANNOTATION_NOT_UNIQUE = 8222
ER_NONE = 65535
ER_BUS_ERRORS = 36864
ER_BUS_READ_ERROR = 36865
ER_BUS_WRITE_ERROR = 36866
ER_BUS_BAD_VALUE_TYPE = 36867
ER_BUS_BAD_HEADER_FIELD = 36868
ER_BUS_BAD_SIGNATURE = 36869
ER_BUS_BAD_OBJ_PATH = 36870
ER_BUS_BAD_MEMBER_NAME = 36871
ER_BUS_BAD_INTERFACE_NAME = 36872
ER_BUS_BAD_ERROR_NAME = 36873
ER_BUS_BAD_BUS_NAME = 36874
ER_BUS_NAME_TOO_LONG = 36875
ER_BUS_BAD_LENGTH = 36876
ER_BUS_BAD_VALUE = 36877
ER_BUS_BAD_HDR_FLAGS = 36878
ER_BUS_BAD_BODY_LEN = 36879
ER_BUS_BAD_HEADER_LEN = 36880
ER_BUS_UNKNOWN_SERIAL = 36881
ER_BUS_UNKNOWN_PATH = 36882
ER_BUS_UNKNOWN_INTERFACE = 36883
ER_BUS_ESTABLISH_FAILED = 36884
ER_BUS_UNEXPECTED_SIGNATURE = 36885
ER_BUS_INTERFACE_MISSING = 36886
ER_BUS_PATH_MISSING = 36887
ER_BUS_MEMBER_MISSING = 36888
ER_BUS_REPLY_SERIAL_MISSING = 36889
ER_BUS_ERROR_NAME_MISSING = 36890
ER_BUS_INTERFACE_NO_SUCH_MEMBER = 36891
ER_BUS_NO_SUCH_OBJECT = 36892
ER_BUS_OBJECT_NO_SUCH_MEMBER = 36893
ER_BUS_OBJECT_NO_SUCH_INTERFACE = 36894
ER_BUS_NO_SUCH_INTERFACE = 36895
ER_BUS_MEMBER_NO_SUCH_SIGNATURE = 36896
ER_BUS_NOT_NUL_TERMINATED = 36897
ER_BUS_NO_SUCH_PROPERTY = 36898
ER_BUS_SET_WRONG_SIGNATURE = 36899
ER_BUS_PROPERTY_VALUE_NOT_SET = 36900
ER_BUS_PROPERTY_ACCESS_DENIED = 36901
ER_BUS_NO_TRANSPORTS = 36902
ER_BUS_BAD_TRANSPORT_ARGS = 36903
ER_BUS_NO_ROUTE = 36904
ER_BUS_NO_ENDPOINT = 36905
ER_BUS_BAD_SEND_PARAMETER = 36906
ER_BUS_UNMATCHED_REPLY_SERIAL = 36907
ER_BUS_BAD_SENDER_ID = 36908
ER_BUS_TRANSPORT_NOT_STARTED = 36909
ER_BUS_EMPTY_MESSAGE = 36910
ER_BUS_NOT_OWNER = 36911
ER_BUS_SET_PROPERTY_REJECTED = 36912
ER_BUS_CONNECT_FAILED = 36913
ER_BUS_REPLY_IS_ERROR_MESSAGE = 36914
ER_BUS_NOT_AUTHENTICATING = 36915
ER_BUS_NO_LISTENER = 36916
ER_BUS_NOT_ALLOWED = 36918
ER_BUS_WRITE_QUEUE_FULL = 36919
ER_BUS_ENDPOINT_CLOSING = 36920
ER_BUS_INTERFACE_MISMATCH = 36921
ER_BUS_MEMBER_ALREADY_EXISTS = 36922
ER_BUS_PROPERTY_ALREADY_EXISTS = 36923
ER_BUS_IFACE_ALREADY_EXISTS = 36924
ER_BUS_ERROR_RESPONSE = 36925
ER_BUS_BAD_XML = 36926
ER_BUS_BAD_CHILD_PATH = 36927
ER_BUS_OBJ_ALREADY_EXISTS = 36928
ER_BUS_OBJ_NOT_FOUND = 36929
ER_BUS_CANNOT_EXPAND_MESSAGE = 36930
ER_BUS_NOT_COMPRESSED = 36931
ER_BUS_ALREADY_CONNECTED = 36932
ER_BUS_NOT_CONNECTED = 36933
ER_BUS_ALREADY_LISTENING = 36934
ER_BUS_KEY_UNAVAILABLE = 36935
ER_BUS_TRUNCATED = 36936
ER_BUS_KEY_STORE_NOT_LOADED = 36937
ER_BUS_NO_AUTHENTICATION_MECHANISM = 36938
ER_BUS_BUS_ALREADY_STARTED = 36939
ER_BUS_BUS_NOT_STARTED = 36940
ER_BUS_KEYBLOB_OP_INVALID = 36941
ER_BUS_INVALID_HEADER_CHECKSUM = 36942
ER_BUS_MESSAGE_NOT_ENCRYPTED = 36943
ER_BUS_INVALID_HEADER_SERIAL = 36944
ER_BUS_TIME_TO_LIVE_EXPIRED = 36945
ER_BUS_HDR_EXPANSION_INVALID = 36946
ER_BUS_MISSING_COMPRESSION_TOKEN = 36947
ER_BUS_NO_PEER_GUID = 36948
ER_BUS_MESSAGE_DECRYPTION_FAILED = 36949
ER_BUS_SECURITY_FATAL = 36950
ER_BUS_KEY_EXPIRED = 36951
ER_BUS_CORRUPT_KEYSTORE = 36952
ER_BUS_NO_CALL_FOR_REPLY = 36953
ER_BUS_NOT_A_COMPLETE_TYPE = 36954
ER_BUS_POLICY_VIOLATION = 36955
ER_BUS_NO_SUCH_SERVICE = 36956
ER_BUS_TRANSPORT_NOT_AVAILABLE = 36957
ER_BUS_INVALID_AUTH_MECHANISM = 36958
ER_BUS_KEYSTORE_VERSION_MISMATCH = 36959
ER_BUS_BLOCKING_CALL_NOT_ALLOWED = 36960
ER_BUS_SIGNATURE_MISMATCH = 36961
ER_BUS_STOPPING = 36962
ER_BUS_METHOD_CALL_ABORTED = 36963
ER_BUS_CANNOT_ADD_INTERFACE = 36964
ER_BUS_CANNOT_ADD_HANDLER = 36965
ER_BUS_KEYSTORE_NOT_LOADED = 36966
ER_BUS_NO_SUCH_HANDLE = 36971
ER_BUS_HANDLES_NOT_ENABLED = 36972
ER_BUS_HANDLES_MISMATCH = 36973
ER_BUS_NO_SESSION = 36975
ER_BUS_ELEMENT_NOT_FOUND = 36976
ER_BUS_NOT_A_DICTIONARY = 36977
ER_BUS_WAIT_FAILED = 36978
ER_BUS_BAD_SESSION_OPTS = 36980
ER_BUS_CONNECTION_REJECTED = 36981
ER_DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER = 36982
ER_DBUS_REQUEST_NAME_REPLY_IN_QUEUE = 36983
ER_DBUS_REQUEST_NAME_REPLY_EXISTS = 36984
ER_DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER = 36985
ER_DBUS_RELEASE_NAME_REPLY_RELEASED = 36986
ER_DBUS_RELEASE_NAME_REPLY_NON_EXISTENT = 36987
ER_DBUS_RELEASE_NAME_REPLY_NOT_OWNER = 36988
ER_DBUS_START_REPLY_ALREADY_RUNNING = 36990
ER_ALLJOYN_BINDSESSIONPORT_REPLY_ALREADY_EXISTS = 36992
ER_ALLJOYN_BINDSESSIONPORT_REPLY_FAILED = 36993
ER_ALLJOYN_JOINSESSION_REPLY_NO_SESSION = 36995
ER_ALLJOYN_JOINSESSION_REPLY_UNREACHABLE = 36996
ER_ALLJOYN_JOINSESSION_REPLY_CONNECT_FAILED = 36997
ER_ALLJOYN_JOINSESSION_REPLY_REJECTED = 36998
ER_ALLJOYN_JOINSESSION_REPLY_BAD_SESSION_OPTS = 36999
ER_ALLJOYN_JOINSESSION_REPLY_FAILED = 37000
ER_ALLJOYN_LEAVESESSION_REPLY_NO_SESSION = 37002
ER_ALLJOYN_LEAVESESSION_REPLY_FAILED = 37003
ER_ALLJOYN_ADVERTISENAME_REPLY_TRANSPORT_NOT_AVAILABLE = 37004
ER_ALLJOYN_ADVERTISENAME_REPLY_ALREADY_ADVERTISING = 37005
ER_ALLJOYN_ADVERTISENAME_REPLY_FAILED = 37006
ER_ALLJOYN_CANCELADVERTISENAME_REPLY_FAILED = 37008
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_TRANSPORT_NOT_AVAILABLE = 37009
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_ALREADY_DISCOVERING = 37010
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_FAILED = 37011
ER_ALLJOYN_CANCELFINDADVERTISEDNAME_REPLY_FAILED = 37013
ER_BUS_UNEXPECTED_DISPOSITION = 37014
ER_BUS_INTERFACE_ACTIVATED = 37015
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_BAD_PORT = 37016
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_FAILED = 37017
ER_ALLJOYN_BINDSESSIONPORT_REPLY_INVALID_OPTS = 37018
ER_ALLJOYN_JOINSESSION_REPLY_ALREADY_JOINED = 37019
ER_BUS_SELF_CONNECT = 37020
ER_BUS_SECURITY_NOT_ENABLED = 37021
ER_BUS_LISTENER_ALREADY_SET = 37022
ER_BUS_PEER_AUTH_VERSION_MISMATCH = 37023
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NOT_SUPPORTED = 37024
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NO_DEST_SUPPORT = 37025
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_FAILED = 37026
ER_ALLJOYN_ACCESS_PERMISSION_WARNING = 37027
ER_ALLJOYN_ACCESS_PERMISSION_ERROR = 37028
ER_BUS_DESTINATION_NOT_AUTHENTICATED = 37029
ER_BUS_ENDPOINT_REDIRECTED = 37030
ER_BUS_AUTHENTICATION_PENDING = 37031
ER_BUS_NOT_AUTHORIZED = 37032
ER_PACKET_BUS_NO_SUCH_CHANNEL = 37033
ER_PACKET_BAD_FORMAT = 37034
ER_PACKET_CONNECT_TIMEOUT = 37035
ER_PACKET_CHANNEL_FAIL = 37036
ER_PACKET_TOO_LARGE = 37037
ER_PACKET_BAD_PARAMETER = 37038
ER_PACKET_BAD_CRC = 37039
ER_RENDEZVOUS_SERVER_DEACTIVATED_USER = 37067
ER_RENDEZVOUS_SERVER_UNKNOWN_USER = 37068
ER_UNABLE_TO_CONNECT_TO_RENDEZVOUS_SERVER = 37069
ER_NOT_CONNECTED_TO_RENDEZVOUS_SERVER = 37070
ER_UNABLE_TO_SEND_MESSAGE_TO_RENDEZVOUS_SERVER = 37071
ER_INVALID_RENDEZVOUS_SERVER_INTERFACE_MESSAGE = 37072
ER_INVALID_PERSISTENT_CONNECTION_MESSAGE_RESPONSE = 37073
ER_INVALID_ON_DEMAND_CONNECTION_MESSAGE_RESPONSE = 37074
ER_INVALID_HTTP_METHOD_USED_FOR_RENDEZVOUS_SERVER_INTERFACE_MESSAGE = 37075
ER_RENDEZVOUS_SERVER_ERR500_INTERNAL_ERROR = 37076
ER_RENDEZVOUS_SERVER_ERR503_STATUS_UNAVAILABLE = 37077
ER_RENDEZVOUS_SERVER_ERR401_UNAUTHORIZED_REQUEST = 37078
ER_RENDEZVOUS_SERVER_UNRECOVERABLE_ERROR = 37079
ER_RENDEZVOUS_SERVER_ROOT_CERTIFICATE_UNINITIALIZED = 37080
ER_BUS_NO_SUCH_ANNOTATION = 37081
ER_BUS_ANNOTATION_ALREADY_EXISTS = 37082
ER_SOCK_CLOSING = 37083
ER_NO_SUCH_DEVICE = 37084
ER_P2P = 37085
ER_P2P_TIMEOUT = 37086
ER_P2P_NOT_CONNECTED = 37087
ER_BAD_TRANSPORT_MASK = 37088
ER_PROXIMITY_CONNECTION_ESTABLISH_FAIL = 37089
ER_PROXIMITY_NO_PEERS_FOUND = 37090
ER_BUS_OBJECT_NOT_REGISTERED = 37091
ER_P2P_DISABLED = 37092
ER_P2P_BUSY = 37093
ER_BUS_INCOMPATIBLE_DAEMON = 37094
ER_P2P_NO_GO = 37095
ER_P2P_NO_STA = 37096
ER_P2P_FORBIDDEN = 37097
ER_ALLJOYN_ONAPPSUSPEND_REPLY_FAILED = 37098
ER_ALLJOYN_ONAPPSUSPEND_REPLY_UNSUPPORTED = 37099
ER_ALLJOYN_ONAPPRESUME_REPLY_FAILED = 37100
ER_ALLJOYN_ONAPPRESUME_REPLY_UNSUPPORTED = 37101
ER_BUS_NO_SUCH_MESSAGE = 37102
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_NO_SESSION = 37103
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_BINDER = 37104
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_MULTIPOINT = 37105
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_FOUND = 37106
ER_ALLJOYN_REMOVESESSIONMEMBER_INCOMPATIBLE_REMOTE_DAEMON = 37107
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_FAILED = 37108
ER_BUS_REMOVED_BY_BINDER = 37109
ER_BUS_MATCH_RULE_NOT_FOUND = 37110
ER_ALLJOYN_PING_FAILED = 37111
ER_ALLJOYN_PING_REPLY_UNREACHABLE = 37112
ER_UDP_MSG_TOO_LONG = 37113
ER_UDP_DEMUX_NO_ENDPOINT = 37114
ER_UDP_NO_NETWORK = 37115
ER_UDP_UNEXPECTED_LENGTH = 37116
ER_UDP_UNEXPECTED_FLOW = 37117
ER_UDP_DISCONNECT = 37118
ER_UDP_NOT_IMPLEMENTED = 37119
ER_UDP_NO_LISTENER = 37120
ER_UDP_STOPPING = 37121
ER_ARDP_BACKPRESSURE = 37122
ER_UDP_BACKPRESSURE = 37123
ER_ARDP_INVALID_STATE = 37124
ER_ARDP_TTL_EXPIRED = 37125
ER_ARDP_PERSIST_TIMEOUT = 37126
ER_ARDP_PROBE_TIMEOUT = 37127
ER_ARDP_REMOTE_CONNECTION_RESET = 37128
ER_UDP_BUSHELLO = 37129
ER_UDP_MESSAGE = 37130
ER_UDP_INVALID = 37131
ER_UDP_UNSUPPORTED = 37132
ER_UDP_ENDPOINT_STALLED = 37133
ER_ARDP_INVALID_RESPONSE = 37134
ER_ARDP_INVALID_CONNECTION = 37135
ER_UDP_LOCAL_DISCONNECT = 37136
ER_UDP_EARLY_EXIT = 37137
ER_UDP_LOCAL_DISCONNECT_FAIL = 37138
ER_ARDP_DISCONNECTING = 37139
ER_ALLJOYN_PING_REPLY_INCOMPATIBLE_REMOTE_ROUTING_NODE = 37140
ER_ALLJOYN_PING_REPLY_TIMEOUT = 37141
ER_ALLJOYN_PING_REPLY_UNKNOWN_NAME = 37142
ER_ALLJOYN_PING_REPLY_FAILED = 37143
ER_TCP_MAX_UNTRUSTED = 37144
ER_ALLJOYN_PING_REPLY_IN_PROGRESS = 37145
ER_LANGUAGE_NOT_SUPPORTED = 37146
ER_ABOUT_FIELD_ALREADY_SPECIFIED = 37147
ER_UDP_NOT_DISCONNECTED = 37148
ER_UDP_ENDPOINT_NOT_STARTED = 37149
ER_UDP_ENDPOINT_REMOVED = 37150
ER_ARDP_VERSION_NOT_SUPPORTED = 37151
ER_CONNECTION_LIMIT_EXCEEDED = 37152
ER_ARDP_WRITE_BLOCKED = 37153
ER_PERMISSION_DENIED = 37154
ER_ABOUT_DEFAULT_LANGUAGE_NOT_SPECIFIED = 37155
ER_ABOUT_SESSIONPORT_NOT_BOUND = 37156
ER_ABOUT_ABOUTDATA_MISSING_REQUIRED_FIELD = 37157
ER_ABOUT_INVALID_ABOUTDATA_LISTENER = 37158
ER_BUS_PING_GROUP_NOT_FOUND = 37159
ER_BUS_REMOVED_BY_BINDER_SELF = 37160
ER_INVALID_CONFIG = 37161
ER_ABOUT_INVALID_ABOUTDATA_FIELD_VALUE = 37162
ER_ABOUT_INVALID_ABOUTDATA_FIELD_APPID_SIZE = 37163
ER_BUS_TRANSPORT_ACCESS_DENIED = 37164
ER_INVALID_CERTIFICATE = 37165
ER_CERTIFICATE_NOT_FOUND = 37166
ER_DUPLICATE_CERTIFICATE = 37167
ER_UNKNOWN_CERTIFICATE = 37168
ER_MISSING_DIGEST_IN_CERTIFICATE = 37169
ER_DIGEST_MISMATCH = 37170
ER_DUPLICATE_KEY = 37171
ER_NO_COMMON_TRUST = 37172
ER_MANIFEST_NOT_FOUND = 37173
ER_INVALID_CERT_CHAIN = 37174
ER_NO_TRUST_ANCHOR = 37175
ER_INVALID_APPLICATION_STATE = 37176
ER_FEATURE_NOT_AVAILABLE = 37177
ER_KEY_STORE_ALREADY_INITIALIZED = 37178
ER_KEY_STORE_ID_NOT_YET_SET = 37179
ER_POLICY_NOT_NEWER = 37180
ER_MANIFEST_REJECTED = 37181
ER_INVALID_CERTIFICATE_USAGE = 37182
ER_INVALID_SIGNAL_EMISSION_TYPE = 37183
ER_APPLICATION_STATE_LISTENER_ALREADY_EXISTS = 37184
ER_APPLICATION_STATE_LISTENER_NO_SUCH_LISTENER = 37185
ER_MANAGEMENT_ALREADY_STARTED = 37186
ER_MANAGEMENT_NOT_STARTED = 37187
ER_BUS_DESCRIPTION_ALREADY_EXISTS = 37188
alljoyn_typeid = Int32
ALLJOYN_INVALID = 0
ALLJOYN_ARRAY = 97
ALLJOYN_BOOLEAN = 98
ALLJOYN_DOUBLE = 100
ALLJOYN_DICT_ENTRY = 101
ALLJOYN_SIGNATURE = 103
ALLJOYN_HANDLE = 104
ALLJOYN_INT32 = 105
ALLJOYN_INT16 = 110
ALLJOYN_OBJECT_PATH = 111
ALLJOYN_UINT16 = 113
ALLJOYN_STRUCT = 114
ALLJOYN_STRING = 115
ALLJOYN_UINT64 = 116
ALLJOYN_UINT32 = 117
ALLJOYN_VARIANT = 118
ALLJOYN_INT64 = 120
ALLJOYN_BYTE = 121
ALLJOYN_STRUCT_OPEN = 40
ALLJOYN_STRUCT_CLOSE = 41
ALLJOYN_DICT_ENTRY_OPEN = 123
ALLJOYN_DICT_ENTRY_CLOSE = 125
ALLJOYN_BOOLEAN_ARRAY = 25185
ALLJOYN_DOUBLE_ARRAY = 25697
ALLJOYN_INT32_ARRAY = 26977
ALLJOYN_INT16_ARRAY = 28257
ALLJOYN_UINT16_ARRAY = 29025
ALLJOYN_UINT64_ARRAY = 29793
ALLJOYN_UINT32_ARRAY = 30049
ALLJOYN_INT64_ARRAY = 30817
ALLJOYN_BYTE_ARRAY = 31073
ALLJOYN_WILDCARD = 42
def _define__alljoyn_abouticon_handle_head():
    class _alljoyn_abouticon_handle(Structure):
        pass
    return _alljoyn_abouticon_handle
def _define__alljoyn_abouticon_handle():
    _alljoyn_abouticon_handle = win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head
    return _alljoyn_abouticon_handle
alljoyn_applicationstate = Int32
NOT_CLAIMABLE = 0
CLAIMABLE = 1
CLAIMED = 2
NEED_UPDATE = 3
alljoyn_claimcapability_masks = Int32
CAPABLE_ECDHE_NULL = 1
CAPABLE_ECDHE_ECDSA = 4
CAPABLE_ECDHE_SPEKE = 8
alljoyn_claimcapabilityadditionalinfo_masks = Int32
PASSWORD_GENERATED_BY_SECURITY_MANAGER = 1
PASSWORD_GENERATED_BY_APPLICATION = 2
def _define_alljoyn_certificateid_head():
    class alljoyn_certificateid(Structure):
        pass
    return alljoyn_certificateid
def _define_alljoyn_certificateid():
    alljoyn_certificateid = win32more.Devices.AllJoyn.alljoyn_certificateid_head
    alljoyn_certificateid._fields_ = [
        ("serial", c_char_p_no),
        ("serialLen", UIntPtr),
        ("issuerPublicKey", POINTER(SByte)),
        ("issuerAki", c_char_p_no),
        ("issuerAkiLen", UIntPtr),
    ]
    return alljoyn_certificateid
def _define_alljoyn_certificateidarray_head():
    class alljoyn_certificateidarray(Structure):
        pass
    return alljoyn_certificateidarray
def _define_alljoyn_certificateidarray():
    alljoyn_certificateidarray = win32more.Devices.AllJoyn.alljoyn_certificateidarray_head
    alljoyn_certificateidarray._fields_ = [
        ("count", UIntPtr),
        ("ids", POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head)),
    ]
    return alljoyn_certificateidarray
def _define_alljoyn_manifestarray_head():
    class alljoyn_manifestarray(Structure):
        pass
    return alljoyn_manifestarray
def _define_alljoyn_manifestarray():
    alljoyn_manifestarray = win32more.Devices.AllJoyn.alljoyn_manifestarray_head
    alljoyn_manifestarray._fields_ = [
        ("count", UIntPtr),
        ("xmls", POINTER(POINTER(SByte))),
    ]
    return alljoyn_manifestarray
def _define_alljoyn_applicationstatelistener_state_ptr():
    return CFUNCTYPE(Void,POINTER(SByte),POINTER(SByte),win32more.Devices.AllJoyn.alljoyn_applicationstate,c_void_p, use_last_error=False)
def _define_alljoyn_applicationstatelistener_callbacks_head():
    class alljoyn_applicationstatelistener_callbacks(Structure):
        pass
    return alljoyn_applicationstatelistener_callbacks
def _define_alljoyn_applicationstatelistener_callbacks():
    alljoyn_applicationstatelistener_callbacks = win32more.Devices.AllJoyn.alljoyn_applicationstatelistener_callbacks_head
    alljoyn_applicationstatelistener_callbacks._fields_ = [
        ("state", win32more.Devices.AllJoyn.alljoyn_applicationstatelistener_state_ptr),
    ]
    return alljoyn_applicationstatelistener_callbacks
def _define_alljoyn_keystorelistener_loadrequest_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_keystorelistener,win32more.Devices.AllJoyn.alljoyn_keystore, use_last_error=False)
def _define_alljoyn_keystorelistener_storerequest_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_keystorelistener,win32more.Devices.AllJoyn.alljoyn_keystore, use_last_error=False)
def _define_alljoyn_keystorelistener_acquireexclusivelock_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_keystorelistener, use_last_error=False)
def _define_alljoyn_keystorelistener_releaseexclusivelock_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Devices.AllJoyn.alljoyn_keystorelistener, use_last_error=False)
def _define_alljoyn_keystorelistener_callbacks_head():
    class alljoyn_keystorelistener_callbacks(Structure):
        pass
    return alljoyn_keystorelistener_callbacks
def _define_alljoyn_keystorelistener_callbacks():
    alljoyn_keystorelistener_callbacks = win32more.Devices.AllJoyn.alljoyn_keystorelistener_callbacks_head
    alljoyn_keystorelistener_callbacks._fields_ = [
        ("load_request", win32more.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr),
        ("store_request", win32more.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr),
    ]
    return alljoyn_keystorelistener_callbacks
def _define_alljoyn_keystorelistener_with_synchronization_callbacks_head():
    class alljoyn_keystorelistener_with_synchronization_callbacks(Structure):
        pass
    return alljoyn_keystorelistener_with_synchronization_callbacks
def _define_alljoyn_keystorelistener_with_synchronization_callbacks():
    alljoyn_keystorelistener_with_synchronization_callbacks = win32more.Devices.AllJoyn.alljoyn_keystorelistener_with_synchronization_callbacks_head
    alljoyn_keystorelistener_with_synchronization_callbacks._fields_ = [
        ("load_request", win32more.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr),
        ("store_request", win32more.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr),
        ("acquire_exclusive_lock", win32more.Devices.AllJoyn.alljoyn_keystorelistener_acquireexclusivelock_ptr),
        ("release_exclusive_lock", win32more.Devices.AllJoyn.alljoyn_keystorelistener_releaseexclusivelock_ptr),
    ]
    return alljoyn_keystorelistener_with_synchronization_callbacks
alljoyn_messagetype = Int32
ALLJOYN_MESSAGE_INVALID = 0
ALLJOYN_MESSAGE_METHOD_CALL = 1
ALLJOYN_MESSAGE_METHOD_RET = 2
ALLJOYN_MESSAGE_ERROR = 3
ALLJOYN_MESSAGE_SIGNAL = 4
def _define_alljoyn_authlistener_requestcredentials_ptr():
    return CFUNCTYPE(Int32,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,win32more.Foundation.PSTR,UInt16,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)
def _define_alljoyn_authlistener_requestcredentialsasync_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_authlistener,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,win32more.Foundation.PSTR,UInt16,c_void_p, use_last_error=False)
def _define_alljoyn_authlistener_verifycredentials_ptr():
    return CFUNCTYPE(Int32,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)
def _define_alljoyn_authlistener_verifycredentialsasync_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_authlistener,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials,c_void_p, use_last_error=False)
def _define_alljoyn_authlistener_securityviolation_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)
def _define_alljoyn_authlistener_authenticationcomplete_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)
def _define_alljoyn_authlistener_callbacks_head():
    class alljoyn_authlistener_callbacks(Structure):
        pass
    return alljoyn_authlistener_callbacks
def _define_alljoyn_authlistener_callbacks():
    alljoyn_authlistener_callbacks = win32more.Devices.AllJoyn.alljoyn_authlistener_callbacks_head
    alljoyn_authlistener_callbacks._fields_ = [
        ("request_credentials", win32more.Devices.AllJoyn.alljoyn_authlistener_requestcredentials_ptr),
        ("verify_credentials", win32more.Devices.AllJoyn.alljoyn_authlistener_verifycredentials_ptr),
        ("security_violation", win32more.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr),
        ("authentication_complete", win32more.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr),
    ]
    return alljoyn_authlistener_callbacks
def _define_alljoyn_authlistenerasync_callbacks_head():
    class alljoyn_authlistenerasync_callbacks(Structure):
        pass
    return alljoyn_authlistenerasync_callbacks
def _define_alljoyn_authlistenerasync_callbacks():
    alljoyn_authlistenerasync_callbacks = win32more.Devices.AllJoyn.alljoyn_authlistenerasync_callbacks_head
    alljoyn_authlistenerasync_callbacks._fields_ = [
        ("request_credentials", win32more.Devices.AllJoyn.alljoyn_authlistener_requestcredentialsasync_ptr),
        ("verify_credentials", win32more.Devices.AllJoyn.alljoyn_authlistener_verifycredentialsasync_ptr),
        ("security_violation", win32more.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr),
        ("authentication_complete", win32more.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr),
    ]
    return alljoyn_authlistenerasync_callbacks
def _define_alljoyn_buslistener_listener_registered_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)
def _define_alljoyn_buslistener_listener_unregistered_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_buslistener_found_advertised_name_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,UInt16,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_buslistener_lost_advertised_name_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,UInt16,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_buslistener_name_owner_changed_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_buslistener_bus_stopping_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_buslistener_bus_disconnected_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_buslistener_bus_prop_changed_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)
def _define_alljoyn_buslistener_callbacks_head():
    class alljoyn_buslistener_callbacks(Structure):
        pass
    return alljoyn_buslistener_callbacks
def _define_alljoyn_buslistener_callbacks():
    alljoyn_buslistener_callbacks = win32more.Devices.AllJoyn.alljoyn_buslistener_callbacks_head
    alljoyn_buslistener_callbacks._fields_ = [
        ("listener_registered", win32more.Devices.AllJoyn.alljoyn_buslistener_listener_registered_ptr),
        ("listener_unregistered", win32more.Devices.AllJoyn.alljoyn_buslistener_listener_unregistered_ptr),
        ("found_advertised_name", win32more.Devices.AllJoyn.alljoyn_buslistener_found_advertised_name_ptr),
        ("lost_advertised_name", win32more.Devices.AllJoyn.alljoyn_buslistener_lost_advertised_name_ptr),
        ("name_owner_changed", win32more.Devices.AllJoyn.alljoyn_buslistener_name_owner_changed_ptr),
        ("bus_stopping", win32more.Devices.AllJoyn.alljoyn_buslistener_bus_stopping_ptr),
        ("bus_disconnected", win32more.Devices.AllJoyn.alljoyn_buslistener_bus_disconnected_ptr),
        ("property_changed", win32more.Devices.AllJoyn.alljoyn_buslistener_bus_prop_changed_ptr),
    ]
    return alljoyn_buslistener_callbacks
alljoyn_interfacedescription_securitypolicy = Int32
AJ_IFC_SECURITY_INHERIT = 0
AJ_IFC_SECURITY_REQUIRED = 1
AJ_IFC_SECURITY_OFF = 2
def _define_alljoyn_interfacedescription_member_head():
    class alljoyn_interfacedescription_member(Structure):
        pass
    return alljoyn_interfacedescription_member
def _define_alljoyn_interfacedescription_member():
    alljoyn_interfacedescription_member = win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head
    alljoyn_interfacedescription_member._fields_ = [
        ("iface", win32more.Devices.AllJoyn.alljoyn_interfacedescription),
        ("memberType", win32more.Devices.AllJoyn.alljoyn_messagetype),
        ("name", win32more.Foundation.PSTR),
        ("signature", win32more.Foundation.PSTR),
        ("returnSignature", win32more.Foundation.PSTR),
        ("argNames", win32more.Foundation.PSTR),
        ("internal_member", c_void_p),
    ]
    return alljoyn_interfacedescription_member
def _define_alljoyn_interfacedescription_translation_callback_ptr():
    return CFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_interfacedescription_property_head():
    class alljoyn_interfacedescription_property(Structure):
        pass
    return alljoyn_interfacedescription_property
def _define_alljoyn_interfacedescription_property():
    alljoyn_interfacedescription_property = win32more.Devices.AllJoyn.alljoyn_interfacedescription_property_head
    alljoyn_interfacedescription_property._fields_ = [
        ("name", win32more.Foundation.PSTR),
        ("signature", win32more.Foundation.PSTR),
        ("access", Byte),
        ("internal_property", c_void_p),
    ]
    return alljoyn_interfacedescription_property
def _define_alljoyn_messagereceiver_methodhandler_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busobject,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head),win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)
def _define_alljoyn_messagereceiver_replyhandler_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_message,c_void_p, use_last_error=False)
def _define_alljoyn_messagereceiver_signalhandler_ptr():
    return CFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head),win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)
def _define_alljoyn_busobject_prop_get_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)
def _define_alljoyn_busobject_prop_set_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)
def _define_alljoyn_busobject_object_registration_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_busobject_callbacks_head():
    class alljoyn_busobject_callbacks(Structure):
        pass
    return alljoyn_busobject_callbacks
def _define_alljoyn_busobject_callbacks():
    alljoyn_busobject_callbacks = win32more.Devices.AllJoyn.alljoyn_busobject_callbacks_head
    alljoyn_busobject_callbacks._fields_ = [
        ("property_get", win32more.Devices.AllJoyn.alljoyn_busobject_prop_get_ptr),
        ("property_set", win32more.Devices.AllJoyn.alljoyn_busobject_prop_set_ptr),
        ("object_registered", win32more.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr),
        ("object_unregistered", win32more.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr),
    ]
    return alljoyn_busobject_callbacks
def _define_alljoyn_busobject_methodentry_head():
    class alljoyn_busobject_methodentry(Structure):
        pass
    return alljoyn_busobject_methodentry
def _define_alljoyn_busobject_methodentry():
    alljoyn_busobject_methodentry = win32more.Devices.AllJoyn.alljoyn_busobject_methodentry_head
    alljoyn_busobject_methodentry._fields_ = [
        ("member", POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head)),
        ("method_handler", win32more.Devices.AllJoyn.alljoyn_messagereceiver_methodhandler_ptr),
    ]
    return alljoyn_busobject_methodentry
def _define_alljoyn_proxybusobject_listener_introspectcb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,c_void_p, use_last_error=False)
def _define_alljoyn_proxybusobject_listener_getpropertycb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_msgarg,c_void_p, use_last_error=False)
def _define_alljoyn_proxybusobject_listener_getallpropertiescb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_msgarg,c_void_p, use_last_error=False)
def _define_alljoyn_proxybusobject_listener_setpropertycb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,c_void_p, use_last_error=False)
def _define_alljoyn_proxybusobject_listener_propertieschanged_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg,c_void_p, use_last_error=False)
def _define_alljoyn_permissionconfigurationlistener_factoryreset_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p, use_last_error=False)
def _define_alljoyn_permissionconfigurationlistener_policychanged_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_permissionconfigurationlistener_startmanagement_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_permissionconfigurationlistener_endmanagement_ptr():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_alljoyn_permissionconfigurationlistener_callbacks_head():
    class alljoyn_permissionconfigurationlistener_callbacks(Structure):
        pass
    return alljoyn_permissionconfigurationlistener_callbacks
def _define_alljoyn_permissionconfigurationlistener_callbacks():
    alljoyn_permissionconfigurationlistener_callbacks = win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_callbacks_head
    alljoyn_permissionconfigurationlistener_callbacks._fields_ = [
        ("factory_reset", win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_factoryreset_ptr),
        ("policy_changed", win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_policychanged_ptr),
        ("start_management", win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_startmanagement_ptr),
        ("end_management", win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_endmanagement_ptr),
    ]
    return alljoyn_permissionconfigurationlistener_callbacks
alljoyn_sessionlostreason = Int32
ALLJOYN_SESSIONLOST_INVALID = 0
ALLJOYN_SESSIONLOST_REMOTE_END_LEFT_SESSION = 1
ALLJOYN_SESSIONLOST_REMOTE_END_CLOSED_ABRUPTLY = 2
ALLJOYN_SESSIONLOST_REMOVED_BY_BINDER = 3
ALLJOYN_SESSIONLOST_LINK_TIMEOUT = 4
ALLJOYN_SESSIONLOST_REASON_OTHER = 5
def _define_alljoyn_sessionlistener_sessionlost_ptr():
    return CFUNCTYPE(Void,c_void_p,UInt32,win32more.Devices.AllJoyn.alljoyn_sessionlostreason, use_last_error=False)
def _define_alljoyn_sessionlistener_sessionmemberadded_ptr():
    return CFUNCTYPE(Void,c_void_p,UInt32,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_sessionlistener_sessionmemberremoved_ptr():
    return CFUNCTYPE(Void,c_void_p,UInt32,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_sessionlistener_callbacks_head():
    class alljoyn_sessionlistener_callbacks(Structure):
        pass
    return alljoyn_sessionlistener_callbacks
def _define_alljoyn_sessionlistener_callbacks():
    alljoyn_sessionlistener_callbacks = win32more.Devices.AllJoyn.alljoyn_sessionlistener_callbacks_head
    alljoyn_sessionlistener_callbacks._fields_ = [
        ("session_lost", win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionlost_ptr),
        ("session_member_added", win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberadded_ptr),
        ("session_member_removed", win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberremoved_ptr),
    ]
    return alljoyn_sessionlistener_callbacks
def _define_alljoyn_sessionportlistener_acceptsessionjoiner_ptr():
    return CFUNCTYPE(Int32,c_void_p,UInt16,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)
def _define_alljoyn_sessionportlistener_sessionjoined_ptr():
    return CFUNCTYPE(Void,c_void_p,UInt16,UInt32,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_sessionportlistener_callbacks_head():
    class alljoyn_sessionportlistener_callbacks(Structure):
        pass
    return alljoyn_sessionportlistener_callbacks
def _define_alljoyn_sessionportlistener_callbacks():
    alljoyn_sessionportlistener_callbacks = win32more.Devices.AllJoyn.alljoyn_sessionportlistener_callbacks_head
    alljoyn_sessionportlistener_callbacks._fields_ = [
        ("accept_session_joiner", win32more.Devices.AllJoyn.alljoyn_sessionportlistener_acceptsessionjoiner_ptr),
        ("session_joined", win32more.Devices.AllJoyn.alljoyn_sessionportlistener_sessionjoined_ptr),
    ]
    return alljoyn_sessionportlistener_callbacks
def _define_alljoyn_about_announced_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,UInt16,UInt16,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)
def _define_alljoyn_aboutlistener_callback_head():
    class alljoyn_aboutlistener_callback(Structure):
        pass
    return alljoyn_aboutlistener_callback
def _define_alljoyn_aboutlistener_callback():
    alljoyn_aboutlistener_callback = win32more.Devices.AllJoyn.alljoyn_aboutlistener_callback_head
    alljoyn_aboutlistener_callback._fields_ = [
        ("about_listener_announced", win32more.Devices.AllJoyn.alljoyn_about_announced_ptr),
    ]
    return alljoyn_aboutlistener_callback
def _define_alljoyn_busattachment_joinsessioncb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,UInt32,win32more.Devices.AllJoyn.alljoyn_sessionopts,c_void_p, use_last_error=False)
def _define_alljoyn_busattachment_setlinktimeoutcb_ptr():
    return CFUNCTYPE(Void,win32more.Devices.AllJoyn.QStatus,UInt32,c_void_p, use_last_error=False)
def _define__alljoyn_abouticonobj_handle_head():
    class _alljoyn_abouticonobj_handle(Structure):
        pass
    return _alljoyn_abouticonobj_handle
def _define__alljoyn_abouticonobj_handle():
    _alljoyn_abouticonobj_handle = win32more.Devices.AllJoyn._alljoyn_abouticonobj_handle_head
    return _alljoyn_abouticonobj_handle
def _define__alljoyn_abouticonproxy_handle_head():
    class _alljoyn_abouticonproxy_handle(Structure):
        pass
    return _alljoyn_abouticonproxy_handle
def _define__alljoyn_abouticonproxy_handle():
    _alljoyn_abouticonproxy_handle = win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head
    return _alljoyn_abouticonproxy_handle
def _define_alljoyn_aboutdatalistener_getaboutdata_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_aboutdatalistener_getannouncedaboutdata_ptr():
    return CFUNCTYPE(win32more.Devices.AllJoyn.QStatus,c_void_p,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)
def _define_alljoyn_aboutdatalistener_callbacks_head():
    class alljoyn_aboutdatalistener_callbacks(Structure):
        pass
    return alljoyn_aboutdatalistener_callbacks
def _define_alljoyn_aboutdatalistener_callbacks():
    alljoyn_aboutdatalistener_callbacks = win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_callbacks_head
    alljoyn_aboutdatalistener_callbacks._fields_ = [
        ("about_datalistener_getaboutdata", win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_getaboutdata_ptr),
        ("about_datalistener_getannouncedaboutdata", win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_getannouncedaboutdata_ptr),
    ]
    return alljoyn_aboutdatalistener_callbacks
def _define_alljoyn_autopinger_destination_lost_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_autopinger_destination_found_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)
def _define_alljoyn_pinglistener_callback_head():
    class alljoyn_pinglistener_callback(Structure):
        pass
    return alljoyn_pinglistener_callback
def _define_alljoyn_pinglistener_callback():
    alljoyn_pinglistener_callback = win32more.Devices.AllJoyn.alljoyn_pinglistener_callback_head
    alljoyn_pinglistener_callback._fields_ = [
        ("destination_found", win32more.Devices.AllJoyn.alljoyn_autopinger_destination_found_ptr),
        ("destination_lost", win32more.Devices.AllJoyn.alljoyn_autopinger_destination_lost_ptr),
    ]
    return alljoyn_pinglistener_callback
def _define_alljoyn_observer_object_discovered_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)
def _define_alljoyn_observer_object_lost_ptr():
    return CFUNCTYPE(Void,c_void_p,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)
def _define_alljoyn_observerlistener_callback_head():
    class alljoyn_observerlistener_callback(Structure):
        pass
    return alljoyn_observerlistener_callback
def _define_alljoyn_observerlistener_callback():
    alljoyn_observerlistener_callback = win32more.Devices.AllJoyn.alljoyn_observerlistener_callback_head
    alljoyn_observerlistener_callback._fields_ = [
        ("object_discovered", win32more.Devices.AllJoyn.alljoyn_observer_object_discovered_ptr),
        ("object_lost", win32more.Devices.AllJoyn.alljoyn_observer_object_lost_ptr),
    ]
    return alljoyn_observerlistener_callback
alljoyn_aboutdata = IntPtr
alljoyn_aboutdatalistener = IntPtr
alljoyn_aboutlistener = IntPtr
alljoyn_aboutobj = IntPtr
alljoyn_aboutobjectdescription = IntPtr
alljoyn_aboutproxy = IntPtr
alljoyn_applicationstatelistener = IntPtr
alljoyn_authlistener = IntPtr
alljoyn_autopinger = IntPtr
alljoyn_busattachment = IntPtr
alljoyn_buslistener = IntPtr
alljoyn_busobject = IntPtr
alljoyn_credentials = IntPtr
alljoyn_interfacedescription = IntPtr
alljoyn_keystore = IntPtr
alljoyn_keystorelistener = IntPtr
alljoyn_message = IntPtr
alljoyn_msgarg = IntPtr
alljoyn_observer = IntPtr
alljoyn_observerlistener = IntPtr
alljoyn_permissionconfigurationlistener = IntPtr
alljoyn_permissionconfigurator = IntPtr
alljoyn_pinglistener = IntPtr
alljoyn_proxybusobject = IntPtr
alljoyn_proxybusobject_ref = IntPtr
alljoyn_securityapplicationproxy = IntPtr
alljoyn_sessionlistener = IntPtr
alljoyn_sessionopts = IntPtr
alljoyn_sessionportlistener = IntPtr
def _define_AllJoynConnectToBus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=True)(("AllJoynConnectToBus", windll["MSAJApi"]), ((1, 'connectionSpec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynCloseBusHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("AllJoynCloseBusHandle", windll["MSAJApi"]), ((1, 'busHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynSendToBus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),c_void_p, use_last_error=True)(("AllJoynSendToBus", windll["MSAJApi"]), ((1, 'connectedBusHandle'),(1, 'buffer'),(1, 'bytesToWrite'),(1, 'bytesTransferred'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynReceiveFromBus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),c_void_p, use_last_error=True)(("AllJoynReceiveFromBus", windll["MSAJApi"]), ((1, 'connectedBusHandle'),(1, 'buffer'),(1, 'bytesToRead'),(1, 'bytesTransferred'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynEventSelect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("AllJoynEventSelect", windll["MSAJApi"]), ((1, 'connectedBusHandle'),(1, 'eventHandle'),(1, 'eventTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynEnumEvents():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=True)(("AllJoynEnumEvents", windll["MSAJApi"]), ((1, 'connectedBusHandle'),(1, 'eventToReset'),(1, 'eventTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynCreateBus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), use_last_error=False)(("AllJoynCreateBus", windll["MSAJApi"]), ((1, 'outBufferSize'),(1, 'inBufferSize'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllJoynAcceptBusConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("AllJoynAcceptBusConnection", windll["MSAJApi"]), ((1, 'serverBusHandle'),(1, 'abortEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_unity_deferred_callbacks_process():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("alljoyn_unity_deferred_callbacks_process", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_unity_set_deferred_callback_mainthread_only():
    try:
        return WINFUNCTYPE(Void,Int32, use_last_error=False)(("alljoyn_unity_set_deferred_callback_mainthread_only", windll["MSAJApi"]), ((1, 'mainthread_only'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QCC_StatusText():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("QCC_StatusText", windll["MSAJApi"]), ((1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_create", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_create_and_set():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_create_and_set", windll["MSAJApi"]), ((1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_destroy", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_msgarg_array_create", windll["MSAJApi"]), ((1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_element():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_msgarg_array_element", windll["MSAJApi"]), ((1, 'arg'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_set", windll["MSAJApi"]), ((1, 'arg'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_get", windll["MSAJApi"]), ((1, 'arg'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_copy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_copy", windll["MSAJApi"]), ((1, 'source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_clone():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_clone", windll["MSAJApi"]), ((1, 'destination'),(1, 'source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_equal():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_equal", windll["MSAJApi"]), ((1, 'lhv'),(1, 'rhv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_set():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_array_set", windll["MSAJApi"]), ((1, 'args'),(1, 'numArgs'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_get():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_array_get", windll["MSAJApi"]), ((1, 'args'),(1, 'numArgs'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_tostring():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR,UIntPtr,UIntPtr, use_last_error=False)(("alljoyn_msgarg_tostring", windll["MSAJApi"]), ((1, 'arg'),(1, 'str'),(1, 'buf'),(1, 'indent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_tostring():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,win32more.Foundation.PSTR,UIntPtr,UIntPtr, use_last_error=False)(("alljoyn_msgarg_array_tostring", windll["MSAJApi"]), ((1, 'args'),(1, 'numArgs'),(1, 'str'),(1, 'buf'),(1, 'indent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_signature():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_msgarg_signature", windll["MSAJApi"]), ((1, 'arg'),(1, 'str'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_signature():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_msgarg_array_signature", windll["MSAJApi"]), ((1, 'values'),(1, 'numValues'),(1, 'str'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_hassignature():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_hassignature", windll["MSAJApi"]), ((1, 'arg'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_getdictelement():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_getdictelement", windll["MSAJApi"]), ((1, 'arg'),(1, 'elemSig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_gettype():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_typeid,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_gettype", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_clear():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_clear", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_stabilize():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_stabilize", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_array_set_offset():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(UIntPtr),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_array_set_offset", windll["MSAJApi"]), ((1, 'args'),(1, 'argOffset'),(1, 'numArgs'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_and_stabilize():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_set_and_stabilize", windll["MSAJApi"]), ((1, 'arg'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint8():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Byte, use_last_error=False)(("alljoyn_msgarg_set_uint8", windll["MSAJApi"]), ((1, 'arg'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_bool():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Int32, use_last_error=False)(("alljoyn_msgarg_set_bool", windll["MSAJApi"]), ((1, 'arg'),(1, 'b'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int16():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Int16, use_last_error=False)(("alljoyn_msgarg_set_int16", windll["MSAJApi"]), ((1, 'arg'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint16():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UInt16, use_last_error=False)(("alljoyn_msgarg_set_uint16", windll["MSAJApi"]), ((1, 'arg'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int32():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Int32, use_last_error=False)(("alljoyn_msgarg_set_int32", windll["MSAJApi"]), ((1, 'arg'),(1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint32():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UInt32, use_last_error=False)(("alljoyn_msgarg_set_uint32", windll["MSAJApi"]), ((1, 'arg'),(1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int64():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Int64, use_last_error=False)(("alljoyn_msgarg_set_int64", windll["MSAJApi"]), ((1, 'arg'),(1, 'x'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint64():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UInt64, use_last_error=False)(("alljoyn_msgarg_set_uint64", windll["MSAJApi"]), ((1, 'arg'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_double():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,Double, use_last_error=False)(("alljoyn_msgarg_set_double", windll["MSAJApi"]), ((1, 'arg'),(1, 'd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_string():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_set_string", windll["MSAJApi"]), ((1, 'arg'),(1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_objectpath():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_set_objectpath", windll["MSAJApi"]), ((1, 'arg'),(1, 'o'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_signature():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_msgarg_set_signature", windll["MSAJApi"]), ((1, 'arg'),(1, 'g'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint8():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,c_char_p_no, use_last_error=False)(("alljoyn_msgarg_get_uint8", windll["MSAJApi"]), ((1, 'arg'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_bool():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_get_bool", windll["MSAJApi"]), ((1, 'arg'),(1, 'b'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int16():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(Int16), use_last_error=False)(("alljoyn_msgarg_get_int16", windll["MSAJApi"]), ((1, 'arg'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint16():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UInt16), use_last_error=False)(("alljoyn_msgarg_get_uint16", windll["MSAJApi"]), ((1, 'arg'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int32():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_get_int32", windll["MSAJApi"]), ((1, 'arg'),(1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint32():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UInt32), use_last_error=False)(("alljoyn_msgarg_get_uint32", windll["MSAJApi"]), ((1, 'arg'),(1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int64():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(Int64), use_last_error=False)(("alljoyn_msgarg_get_int64", windll["MSAJApi"]), ((1, 'arg'),(1, 'x'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint64():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UInt64), use_last_error=False)(("alljoyn_msgarg_get_uint64", windll["MSAJApi"]), ((1, 'arg'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_double():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(Double), use_last_error=False)(("alljoyn_msgarg_get_double", windll["MSAJApi"]), ((1, 'arg'),(1, 'd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_string():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_get_string", windll["MSAJApi"]), ((1, 'arg'),(1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_objectpath():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_get_objectpath", windll["MSAJApi"]), ((1, 'arg'),(1, 'o'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_signature():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_get_signature", windll["MSAJApi"]), ((1, 'arg'),(1, 'g'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_variant():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_get_variant", windll["MSAJApi"]), ((1, 'arg'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint8_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,c_char_p_no, use_last_error=False)(("alljoyn_msgarg_set_uint8_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_bool_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_set_bool_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ab'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int16_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(Int16), use_last_error=False)(("alljoyn_msgarg_set_int16_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'an'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint16_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(UInt16), use_last_error=False)(("alljoyn_msgarg_set_uint16_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'aq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int32_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_set_int32_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ai'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint32_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(UInt32), use_last_error=False)(("alljoyn_msgarg_set_uint32_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'au'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_int64_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(Int64), use_last_error=False)(("alljoyn_msgarg_set_int64_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_uint64_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(UInt64), use_last_error=False)(("alljoyn_msgarg_set_uint64_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'at'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_double_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(Double), use_last_error=False)(("alljoyn_msgarg_set_double_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ad'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_string_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_set_string_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'as'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_objectpath_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_set_objectpath_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ao'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_set_signature_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_msgarg_set_signature_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint8_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),c_char_p_no, use_last_error=False)(("alljoyn_msgarg_get_uint8_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ay'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_bool_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_get_bool_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ab'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int16_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(Int16), use_last_error=False)(("alljoyn_msgarg_get_int16_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'an'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint16_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(UInt16), use_last_error=False)(("alljoyn_msgarg_get_uint16_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'aq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int32_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(Int32), use_last_error=False)(("alljoyn_msgarg_get_int32_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ai'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint32_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("alljoyn_msgarg_get_uint32_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'au'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_int64_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(Int64), use_last_error=False)(("alljoyn_msgarg_get_int64_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_uint64_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(UInt64), use_last_error=False)(("alljoyn_msgarg_get_uint64_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'at'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_double_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,POINTER(UIntPtr),POINTER(Double), use_last_error=False)(("alljoyn_msgarg_get_double_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'length'),(1, 'ad'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_variant_array():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR,POINTER(UIntPtr),POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg), use_last_error=False)(("alljoyn_msgarg_get_variant_array", windll["MSAJApi"]), ((1, 'arg'),(1, 'signature'),(1, 'length'),(1, 'av'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_array_numberofelements():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_get_array_numberofelements", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_array_element():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg), use_last_error=False)(("alljoyn_msgarg_get_array_element", windll["MSAJApi"]), ((1, 'arg'),(1, 'index'),(1, 'element'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_get_array_elementsignature():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_msgarg_get_array_elementsignature", windll["MSAJApi"]), ((1, 'arg'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_getkey():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_getkey", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_getvalue():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_getvalue", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_setdictentry():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_setdictentry", windll["MSAJApi"]), ((1, 'arg'),(1, 'key'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_setstruct():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_msgarg_setstruct", windll["MSAJApi"]), ((1, 'arg'),(1, 'struct_members'),(1, 'num_members'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_getnummembers():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_msgarg_getnummembers", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_msgarg_getmember():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_msgarg_getmember", windll["MSAJApi"]), ((1, 'arg'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_create_empty():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutdata, use_last_error=False)(("alljoyn_aboutdata_create_empty", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_create", windll["MSAJApi"]), ((1, 'defaultLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_create_full():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_create_full", windll["MSAJApi"]), ((1, 'arg'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutdata, use_last_error=False)(("alljoyn_aboutdata_destroy", windll["MSAJApi"]), ((1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_createfromxml():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_createfromxml", windll["MSAJApi"]), ((1, 'data'),(1, 'aboutDataXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_isvalid():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_isvalid", windll["MSAJApi"]), ((1, 'data'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_createfrommsgarg():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_createfrommsgarg", windll["MSAJApi"]), ((1, 'data'),(1, 'arg'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setappid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,c_char_p_no,UIntPtr, use_last_error=False)(("alljoyn_aboutdata_setappid", windll["MSAJApi"]), ((1, 'data'),(1, 'appId'),(1, 'num'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setappid_fromstring():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setappid_fromstring", windll["MSAJApi"]), ((1, 'data'),(1, 'appId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getappid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)(("alljoyn_aboutdata_getappid", windll["MSAJApi"]), ((1, 'data'),(1, 'appId'),(1, 'num'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setdefaultlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setdefaultlanguage", windll["MSAJApi"]), ((1, 'data'),(1, 'defaultLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getdefaultlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getdefaultlanguage", windll["MSAJApi"]), ((1, 'data'),(1, 'defaultLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setdevicename():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setdevicename", windll["MSAJApi"]), ((1, 'data'),(1, 'deviceName'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getdevicename():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getdevicename", windll["MSAJApi"]), ((1, 'data'),(1, 'deviceName'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setdeviceid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setdeviceid", windll["MSAJApi"]), ((1, 'data'),(1, 'deviceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getdeviceid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getdeviceid", windll["MSAJApi"]), ((1, 'data'),(1, 'deviceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setappname():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setappname", windll["MSAJApi"]), ((1, 'data'),(1, 'appName'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getappname():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getappname", windll["MSAJApi"]), ((1, 'data'),(1, 'appName'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setmanufacturer():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setmanufacturer", windll["MSAJApi"]), ((1, 'data'),(1, 'manufacturer'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getmanufacturer():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getmanufacturer", windll["MSAJApi"]), ((1, 'data'),(1, 'manufacturer'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setmodelnumber():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setmodelnumber", windll["MSAJApi"]), ((1, 'data'),(1, 'modelNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getmodelnumber():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getmodelnumber", windll["MSAJApi"]), ((1, 'data'),(1, 'modelNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setsupportedlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setsupportedlanguage", windll["MSAJApi"]), ((1, 'data'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getsupportedlanguages():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_aboutdata_getsupportedlanguages", windll["MSAJApi"]), ((1, 'data'),(1, 'languageTags'),(1, 'num'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setdescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setdescription", windll["MSAJApi"]), ((1, 'data'),(1, 'description'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getdescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getdescription", windll["MSAJApi"]), ((1, 'data'),(1, 'description'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setdateofmanufacture():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setdateofmanufacture", windll["MSAJApi"]), ((1, 'data'),(1, 'dateOfManufacture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getdateofmanufacture():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getdateofmanufacture", windll["MSAJApi"]), ((1, 'data'),(1, 'dateOfManufacture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setsoftwareversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setsoftwareversion", windll["MSAJApi"]), ((1, 'data'),(1, 'softwareVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getsoftwareversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getsoftwareversion", windll["MSAJApi"]), ((1, 'data'),(1, 'softwareVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getajsoftwareversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getajsoftwareversion", windll["MSAJApi"]), ((1, 'data'),(1, 'ajSoftwareVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_sethardwareversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_sethardwareversion", windll["MSAJApi"]), ((1, 'data'),(1, 'hardwareVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_gethardwareversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_gethardwareversion", windll["MSAJApi"]), ((1, 'data'),(1, 'hardwareVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setsupporturl():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setsupporturl", windll["MSAJApi"]), ((1, 'data'),(1, 'supportUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getsupporturl():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_aboutdata_getsupporturl", windll["MSAJApi"]), ((1, 'data'),(1, 'supportUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_setfield():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_setfield", windll["MSAJApi"]), ((1, 'data'),(1, 'name'),(1, 'value'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getfield():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg),win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getfield", windll["MSAJApi"]), ((1, 'data'),(1, 'name'),(1, 'value'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getfields():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_aboutdata,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_aboutdata_getfields", windll["MSAJApi"]), ((1, 'data'),(1, 'fields'),(1, 'num_fields'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getaboutdata():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getaboutdata", windll["MSAJApi"]), ((1, 'data'),(1, 'msgArg'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getannouncedaboutdata():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutdata_getannouncedaboutdata", windll["MSAJApi"]), ((1, 'data'),(1, 'msgArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_isfieldrequired():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_isfieldrequired", windll["MSAJApi"]), ((1, 'data'),(1, 'fieldName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_isfieldannounced():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_isfieldannounced", windll["MSAJApi"]), ((1, 'data'),(1, 'fieldName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_isfieldlocalized():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_isfieldlocalized", windll["MSAJApi"]), ((1, 'data'),(1, 'fieldName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdata_getfieldsignature():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_aboutdata,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutdata_getfieldsignature", windll["MSAJApi"]), ((1, 'data'),(1, 'fieldName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_create():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), use_last_error=False)(("alljoyn_abouticon_create", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), use_last_error=False)(("alljoyn_abouticon_destroy", windll["MSAJApi"]), ((1, 'icon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_getcontent():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)(("alljoyn_abouticon_getcontent", windll["MSAJApi"]), ((1, 'icon'),(1, 'data'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_setcontent():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head),win32more.Foundation.PSTR,c_char_p_no,UIntPtr,Byte, use_last_error=False)(("alljoyn_abouticon_setcontent", windll["MSAJApi"]), ((1, 'icon'),(1, 'type'),(1, 'data'),(1, 'csize'),(1, 'ownsData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_geturl():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head),POINTER(POINTER(SByte)),POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_abouticon_geturl", windll["MSAJApi"]), ((1, 'icon'),(1, 'type'),(1, 'url'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_seturl():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_abouticon_seturl", windll["MSAJApi"]), ((1, 'icon'),(1, 'type'),(1, 'url'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_clear():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), use_last_error=False)(("alljoyn_abouticon_clear", windll["MSAJApi"]), ((1, 'icon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticon_setcontent_frommsgarg():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head),win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_abouticon_setcontent_frommsgarg", windll["MSAJApi"]), ((1, 'icon'),(1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getdefaultclaimcapabilities():
    try:
        return WINFUNCTYPE(UInt16, use_last_error=False)(("alljoyn_permissionconfigurator_getdefaultclaimcapabilities", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getapplicationstate():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstate), use_last_error=False)(("alljoyn_permissionconfigurator_getapplicationstate", windll["MSAJApi"]), ((1, 'configurator'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_setapplicationstate():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,win32more.Devices.AllJoyn.alljoyn_applicationstate, use_last_error=False)(("alljoyn_permissionconfigurator_setapplicationstate", windll["MSAJApi"]), ((1, 'configurator'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getpublickey():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_permissionconfigurator_getpublickey", windll["MSAJApi"]), ((1, 'configurator'),(1, 'publicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_publickey_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_publickey_destroy", windll["MSAJApi"]), ((1, 'publicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getmanifesttemplate():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_permissionconfigurator_getmanifesttemplate", windll["MSAJApi"]), ((1, 'configurator'),(1, 'manifestTemplateXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_manifesttemplate_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_manifesttemplate_destroy", windll["MSAJApi"]), ((1, 'manifestTemplateXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_setmanifesttemplatefromxml():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_setmanifesttemplatefromxml", windll["MSAJApi"]), ((1, 'configurator'),(1, 'manifestTemplateXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getclaimcapabilities():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(UInt16), use_last_error=False)(("alljoyn_permissionconfigurator_getclaimcapabilities", windll["MSAJApi"]), ((1, 'configurator'),(1, 'claimCapabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_setclaimcapabilities():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,UInt16, use_last_error=False)(("alljoyn_permissionconfigurator_setclaimcapabilities", windll["MSAJApi"]), ((1, 'configurator'),(1, 'claimCapabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(UInt16), use_last_error=False)(("alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo", windll["MSAJApi"]), ((1, 'configurator'),(1, 'additionalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,UInt16, use_last_error=False)(("alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo", windll["MSAJApi"]), ((1, 'configurator'),(1, 'additionalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_reset():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, use_last_error=False)(("alljoyn_permissionconfigurator_reset", windll["MSAJApi"]), ((1, 'configurator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_claim():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(SByte),POINTER(SByte),c_char_p_no,UIntPtr,POINTER(SByte),POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_permissionconfigurator_claim", windll["MSAJApi"]), ((1, 'configurator'),(1, 'caKey'),(1, 'identityCertificateChain'),(1, 'groupId'),(1, 'groupSize'),(1, 'groupAuthority'),(1, 'manifestsXmls'),(1, 'manifestsCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_updateidentity():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(SByte),POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_permissionconfigurator_updateidentity", windll["MSAJApi"]), ((1, 'configurator'),(1, 'identityCertificateChain'),(1, 'manifestsXmls'),(1, 'manifestsCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getidentity():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_permissionconfigurator_getidentity", windll["MSAJApi"]), ((1, 'configurator'),(1, 'identityCertificateChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_certificatechain_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_certificatechain_destroy", windll["MSAJApi"]), ((1, 'certificateChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getmanifests():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(win32more.Devices.AllJoyn.alljoyn_manifestarray_head), use_last_error=False)(("alljoyn_permissionconfigurator_getmanifests", windll["MSAJApi"]), ((1, 'configurator'),(1, 'manifestArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_manifestarray_cleanup():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn.alljoyn_manifestarray_head), use_last_error=False)(("alljoyn_permissionconfigurator_manifestarray_cleanup", windll["MSAJApi"]), ((1, 'manifestArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_installmanifests():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)),UIntPtr,Int32, use_last_error=False)(("alljoyn_permissionconfigurator_installmanifests", windll["MSAJApi"]), ((1, 'configurator'),(1, 'manifestsXmls'),(1, 'manifestsCount'),(1, 'append'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getidentitycertificateid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head), use_last_error=False)(("alljoyn_permissionconfigurator_getidentitycertificateid", windll["MSAJApi"]), ((1, 'configurator'),(1, 'certificateId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_certificateid_cleanup():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head), use_last_error=False)(("alljoyn_permissionconfigurator_certificateid_cleanup", windll["MSAJApi"]), ((1, 'certificateId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_updatepolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_updatepolicy", windll["MSAJApi"]), ((1, 'configurator'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_permissionconfigurator_getpolicy", windll["MSAJApi"]), ((1, 'configurator'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getdefaultpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_permissionconfigurator_getdefaultpolicy", windll["MSAJApi"]), ((1, 'configurator'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_policy_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_policy_destroy", windll["MSAJApi"]), ((1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_resetpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, use_last_error=False)(("alljoyn_permissionconfigurator_resetpolicy", windll["MSAJApi"]), ((1, 'configurator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_getmembershipsummaries():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(win32more.Devices.AllJoyn.alljoyn_certificateidarray_head), use_last_error=False)(("alljoyn_permissionconfigurator_getmembershipsummaries", windll["MSAJApi"]), ((1, 'configurator'),(1, 'certificateIds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_certificateidarray_cleanup():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn.alljoyn_certificateidarray_head), use_last_error=False)(("alljoyn_permissionconfigurator_certificateidarray_cleanup", windll["MSAJApi"]), ((1, 'certificateIdArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_installmembership():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,POINTER(SByte), use_last_error=False)(("alljoyn_permissionconfigurator_installmembership", windll["MSAJApi"]), ((1, 'configurator'),(1, 'membershipCertificateChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_removemembership():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,c_char_p_no,UIntPtr,POINTER(SByte),c_char_p_no,UIntPtr, use_last_error=False)(("alljoyn_permissionconfigurator_removemembership", windll["MSAJApi"]), ((1, 'configurator'),(1, 'serial'),(1, 'serialLen'),(1, 'issuerPublicKey'),(1, 'issuerAki'),(1, 'issuerAkiLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_startmanagement():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, use_last_error=False)(("alljoyn_permissionconfigurator_startmanagement", windll["MSAJApi"]), ((1, 'configurator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurator_endmanagement():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, use_last_error=False)(("alljoyn_permissionconfigurator_endmanagement", windll["MSAJApi"]), ((1, 'configurator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_applicationstatelistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_applicationstatelistener,POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstatelistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_applicationstatelistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_applicationstatelistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_applicationstatelistener, use_last_error=False)(("alljoyn_applicationstatelistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_keystorelistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_keystorelistener,POINTER(win32more.Devices.AllJoyn.alljoyn_keystorelistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_keystorelistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_keystorelistener_with_synchronization_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_keystorelistener,POINTER(win32more.Devices.AllJoyn.alljoyn_keystorelistener_with_synchronization_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_keystorelistener_with_synchronization_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_keystorelistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_keystorelistener, use_last_error=False)(("alljoyn_keystorelistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_keystorelistener_putkeys():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_keystorelistener,win32more.Devices.AllJoyn.alljoyn_keystore,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_keystorelistener_putkeys", windll["MSAJApi"]), ((1, 'listener'),(1, 'keyStore'),(1, 'source'),(1, 'password'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_keystorelistener_getkeys():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_keystorelistener,win32more.Devices.AllJoyn.alljoyn_keystore,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_keystorelistener_getkeys", windll["MSAJApi"]), ((1, 'listener'),(1, 'keyStore'),(1, 'sink'),(1, 'sink_sz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_sessionopts,Byte,Int32,Byte,UInt16, use_last_error=False)(("alljoyn_sessionopts_create", windll["MSAJApi"]), ((1, 'traffic'),(1, 'isMultipoint'),(1, 'proximity'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_destroy", windll["MSAJApi"]), ((1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_get_traffic():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_get_traffic", windll["MSAJApi"]), ((1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_set_traffic():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionopts,Byte, use_last_error=False)(("alljoyn_sessionopts_set_traffic", windll["MSAJApi"]), ((1, 'opts'),(1, 'traffic'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_get_multipoint():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_get_multipoint", windll["MSAJApi"]), ((1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_set_multipoint():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionopts,Int32, use_last_error=False)(("alljoyn_sessionopts_set_multipoint", windll["MSAJApi"]), ((1, 'opts'),(1, 'isMultipoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_get_proximity():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_get_proximity", windll["MSAJApi"]), ((1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_set_proximity():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionopts,Byte, use_last_error=False)(("alljoyn_sessionopts_set_proximity", windll["MSAJApi"]), ((1, 'opts'),(1, 'proximity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_get_transports():
    try:
        return WINFUNCTYPE(UInt16,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_get_transports", windll["MSAJApi"]), ((1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_set_transports():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionopts,UInt16, use_last_error=False)(("alljoyn_sessionopts_set_transports", windll["MSAJApi"]), ((1, 'opts'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_iscompatible():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_sessionopts,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_iscompatible", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionopts_cmp():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_sessionopts,win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_sessionopts_cmp", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_message,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_message_create", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_destroy", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_isbroadcastsignal():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_isbroadcastsignal", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_isglobalbroadcast():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_isglobalbroadcast", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_issessionless():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_issessionless", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getflags():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getflags", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_isexpired():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message,POINTER(UInt32), use_last_error=False)(("alljoyn_message_isexpired", windll["MSAJApi"]), ((1, 'msg'),(1, 'tillExpireMS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_isunreliable():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_isunreliable", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_isencrypted():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_isencrypted", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getauthmechanism():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getauthmechanism", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_gettype():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_messagetype,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_gettype", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getargs():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_message,POINTER(UIntPtr),POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg), use_last_error=False)(("alljoyn_message_getargs", windll["MSAJApi"]), ((1, 'msg'),(1, 'numArgs'),(1, 'args'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getarg():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_message,UIntPtr, use_last_error=False)(("alljoyn_message_getarg", windll["MSAJApi"]), ((1, 'msg'),(1, 'argN'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_parseargs():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_message,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_message_parseargs", windll["MSAJApi"]), ((1, 'msg'),(1, 'signature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getcallserial():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getcallserial", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getsignature():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getsignature", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getobjectpath():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getobjectpath", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getinterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getinterface", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getmembername():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getmembername", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getreplyserial():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getreplyserial", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getsender():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getsender", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getreceiveendpointname():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getreceiveendpointname", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getdestination():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getdestination", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getcompressiontoken():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getcompressiontoken", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_getsessionid():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_getsessionid", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_geterrorname():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_message,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_message_geterrorname", windll["MSAJApi"]), ((1, 'msg'),(1, 'errorMessage'),(1, 'errorMessage_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_tostring():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_message,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_message_tostring", windll["MSAJApi"]), ((1, 'msg'),(1, 'str'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_description():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_message,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_message_description", windll["MSAJApi"]), ((1, 'msg'),(1, 'str'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_gettimestamp():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_gettimestamp", windll["MSAJApi"]), ((1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_eql():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_message,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_message_eql", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_message_setendianess():
    try:
        return WINFUNCTYPE(Void,SByte, use_last_error=False)(("alljoyn_message_setendianess", windll["MSAJApi"]), ((1, 'endian'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistener_requestcredentialsresponse():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_authlistener,c_void_p,Int32,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_authlistener_requestcredentialsresponse", windll["MSAJApi"]), ((1, 'listener'),(1, 'authContext'),(1, 'accept'),(1, 'credentials'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistener_verifycredentialsresponse():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_authlistener,c_void_p,Int32, use_last_error=False)(("alljoyn_authlistener_verifycredentialsresponse", windll["MSAJApi"]), ((1, 'listener'),(1, 'authContext'),(1, 'accept'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_authlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_authlistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_authlistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistenerasync_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_authlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_authlistenerasync_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_authlistenerasync_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_authlistener, use_last_error=False)(("alljoyn_authlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistenerasync_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_authlistener, use_last_error=False)(("alljoyn_authlistenerasync_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_authlistener_setsharedsecret():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_authlistener,c_char_p_no,UIntPtr, use_last_error=False)(("alljoyn_authlistener_setsharedsecret", windll["MSAJApi"]), ((1, 'listener'),(1, 'sharedSecret'),(1, 'sharedSecretSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_create", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_destroy", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_isset():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_credentials,UInt16, use_last_error=False)(("alljoyn_credentials_isset", windll["MSAJApi"]), ((1, 'cred'),(1, 'creds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setpassword():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_credentials_setpassword", windll["MSAJApi"]), ((1, 'cred'),(1, 'pwd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setusername():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_credentials_setusername", windll["MSAJApi"]), ((1, 'cred'),(1, 'userName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setcertchain():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_credentials_setcertchain", windll["MSAJApi"]), ((1, 'cred'),(1, 'certChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setprivatekey():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_credentials_setprivatekey", windll["MSAJApi"]), ((1, 'cred'),(1, 'pk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setlogonentry():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_credentials_setlogonentry", windll["MSAJApi"]), ((1, 'cred'),(1, 'logonEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_setexpiration():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials,UInt32, use_last_error=False)(("alljoyn_credentials_setexpiration", windll["MSAJApi"]), ((1, 'cred'),(1, 'expiration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getpassword():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getpassword", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getusername():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getusername", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getcertchain():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getcertchain", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getprivateKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getprivateKey", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getlogonentry():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getlogonentry", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_getexpiration():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_getexpiration", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_credentials_clear():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_credentials, use_last_error=False)(("alljoyn_credentials_clear", windll["MSAJApi"]), ((1, 'cred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_buslistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_buslistener,POINTER(win32more.Devices.AllJoyn.alljoyn_buslistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_buslistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_buslistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_buslistener, use_last_error=False)(("alljoyn_buslistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getannotationscount():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, use_last_error=False)(("alljoyn_interfacedescription_member_getannotationscount", windll["MSAJApi"]), ((1, 'member'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getannotationatindex():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,UIntPtr,win32more.Foundation.PSTR,POINTER(UIntPtr),win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_member_getannotationatindex", windll["MSAJApi"]), ((1, 'member'),(1, 'index'),(1, 'name'),(1, 'name_size'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_member_getannotation", windll["MSAJApi"]), ((1, 'member'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getargannotationscount():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_member_getargannotationscount", windll["MSAJApi"]), ((1, 'member'),(1, 'argName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getargannotationatindex():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR,POINTER(UIntPtr),win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_member_getargannotationatindex", windll["MSAJApi"]), ((1, 'member'),(1, 'argName'),(1, 'index'),(1, 'name'),(1, 'name_size'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_getargannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_member_getargannotation", windll["MSAJApi"]), ((1, 'member'),(1, 'argName'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_property_getannotationscount():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_property, use_last_error=False)(("alljoyn_interfacedescription_property_getannotationscount", windll["MSAJApi"]), ((1, 'property'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_property_getannotationatindex():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription_property,UIntPtr,win32more.Foundation.PSTR,POINTER(UIntPtr),win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_property_getannotationatindex", windll["MSAJApi"]), ((1, 'property'),(1, 'index'),(1, 'name'),(1, 'name_size'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_property_getannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_property,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_property_getannotation", windll["MSAJApi"]), ((1, 'property'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_activate():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_activate", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addannotation():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_getannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getannotationscount():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_getannotationscount", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getannotationatindex():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription,UIntPtr,win32more.Foundation.PSTR,POINTER(UIntPtr),win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_getannotationatindex", windll["MSAJApi"]), ((1, 'iface'),(1, 'index'),(1, 'name'),(1, 'name_size'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmember():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), use_last_error=False)(("alljoyn_interfacedescription_getmember", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'member'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addmember():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_messagetype,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Byte, use_last_error=False)(("alljoyn_interfacedescription_addmember", windll["MSAJApi"]), ((1, 'iface'),(1, 'type'),(1, 'name'),(1, 'inputSig'),(1, 'outSig'),(1, 'argNames'),(1, 'annotation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addmemberannotation():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addmemberannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmemberannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_getmemberannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmembers():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head),UIntPtr, use_last_error=False)(("alljoyn_interfacedescription_getmembers", windll["MSAJApi"]), ((1, 'iface'),(1, 'members'),(1, 'numMembers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_hasmember():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_hasmember", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'inSig'),(1, 'outSig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addmethod():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Byte,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addmethod", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'inputSig'),(1, 'outSig'),(1, 'argNames'),(1, 'annotation'),(1, 'accessPerms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmethod():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), use_last_error=False)(("alljoyn_interfacedescription_getmethod", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'member'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addsignal():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Byte,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addsignal", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'sig'),(1, 'argNames'),(1, 'annotation'),(1, 'accessPerms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getsignal():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), use_last_error=False)(("alljoyn_interfacedescription_getsignal", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'member'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getproperty():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_property_head), use_last_error=False)(("alljoyn_interfacedescription_getproperty", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'property'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getproperties():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_property_head),UIntPtr, use_last_error=False)(("alljoyn_interfacedescription_getproperties", windll["MSAJApi"]), ((1, 'iface'),(1, 'props'),(1, 'numProps'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addproperty():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Byte, use_last_error=False)(("alljoyn_interfacedescription_addproperty", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'signature'),(1, 'access'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addpropertyannotation():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addpropertyannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'property'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getpropertyannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_getpropertyannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'property'),(1, 'name'),(1, 'value'),(1, 'str_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_hasproperty():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_hasproperty", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_hasproperties():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_hasproperties", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getname():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_getname", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_introspect():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,UIntPtr,UIntPtr, use_last_error=False)(("alljoyn_interfacedescription_introspect", windll["MSAJApi"]), ((1, 'iface'),(1, 'str'),(1, 'buf'),(1, 'indent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_issecure():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_issecure", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getsecuritypolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_getsecuritypolicy", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setdescriptionlanguage():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setdescriptionlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'language'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getdescriptionlanguages():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_interfacedescription_getdescriptionlanguages", windll["MSAJApi"]), ((1, 'iface'),(1, 'languages'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getdescriptionlanguages2():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_interfacedescription_getdescriptionlanguages2", windll["MSAJApi"]), ((1, 'iface'),(1, 'languages'),(1, 'languagesSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setdescription():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setdescription", windll["MSAJApi"]), ((1, 'iface'),(1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setdescriptionforlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'description'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getdescriptionforlanguage():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_getdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'description'),(1, 'maxLanguageLength'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setmemberdescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setmemberdescription", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setmemberdescriptionforlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setmemberdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'description'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmemberdescriptionforlanguage():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_getmemberdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'description'),(1, 'maxLanguageLength'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setargdescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setargdescription", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'argName'),(1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setargdescriptionforlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setargdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'arg'),(1, 'description'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getargdescriptionforlanguage():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_getargdescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'arg'),(1, 'description'),(1, 'maxLanguageLength'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setpropertydescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setpropertydescription", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setpropertydescriptionforlanguage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_setpropertydescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'name'),(1, 'description'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getpropertydescriptionforlanguage():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_getpropertydescriptionforlanguage", windll["MSAJApi"]), ((1, 'iface'),(1, 'property'),(1, 'description'),(1, 'maxLanguageLength'),(1, 'languageTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_setdescriptiontranslationcallback():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_interfacedescription_translation_callback_ptr, use_last_error=False)(("alljoyn_interfacedescription_setdescriptiontranslationcallback", windll["MSAJApi"]), ((1, 'iface'),(1, 'translationCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getdescriptiontranslationcallback():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_interfacedescription_translation_callback_ptr,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_getdescriptiontranslationcallback", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_hasdescription():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_hasdescription", windll["MSAJApi"]), ((1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_addargannotation():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_interfacedescription_addargannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'argName'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_getmemberargannotation():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_interfacedescription_getmemberargannotation", windll["MSAJApi"]), ((1, 'iface'),(1, 'member'),(1, 'argName'),(1, 'name'),(1, 'value'),(1, 'value_size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_eql():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_interfacedescription_eql", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_member_eql():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, use_last_error=False)(("alljoyn_interfacedescription_member_eql", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_interfacedescription_property_eql():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_property,win32more.Devices.AllJoyn.alljoyn_interfacedescription_property, use_last_error=False)(("alljoyn_interfacedescription_property_eql", windll["MSAJApi"]), ((1, 'one'),(1, 'other'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Foundation.PSTR,Int32,POINTER(win32more.Devices.AllJoyn.alljoyn_busobject_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_busobject_create", windll["MSAJApi"]), ((1, 'path'),(1, 'isPlaceholder'),(1, 'callbacks_in'),(1, 'context_in'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busobject_destroy", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_getpath():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busobject_getpath", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_emitpropertychanged():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,UInt32, use_last_error=False)(("alljoyn_busobject_emitpropertychanged", windll["MSAJApi"]), ((1, 'bus'),(1, 'ifcName'),(1, 'propName'),(1, 'val'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_emitpropertieschanged():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UIntPtr,UInt32, use_last_error=False)(("alljoyn_busobject_emitpropertieschanged", windll["MSAJApi"]), ((1, 'bus'),(1, 'ifcName'),(1, 'propNames'),(1, 'numProps'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_getname():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("alljoyn_busobject_getname", windll["MSAJApi"]), ((1, 'bus'),(1, 'buffer'),(1, 'bufferSz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_addinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_busobject_addinterface", windll["MSAJApi"]), ((1, 'bus'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_addmethodhandler():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_messagereceiver_methodhandler_ptr,c_void_p, use_last_error=False)(("alljoyn_busobject_addmethodhandler", windll["MSAJApi"]), ((1, 'bus'),(1, 'member'),(1, 'handler'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_addmethodhandlers():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,POINTER(win32more.Devices.AllJoyn.alljoyn_busobject_methodentry_head),UIntPtr, use_last_error=False)(("alljoyn_busobject_addmethodhandlers", windll["MSAJApi"]), ((1, 'bus'),(1, 'entries'),(1, 'numEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_methodreply_args():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_message,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr, use_last_error=False)(("alljoyn_busobject_methodreply_args", windll["MSAJApi"]), ((1, 'bus'),(1, 'msg'),(1, 'args'),(1, 'numArgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_methodreply_err():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_message,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busobject_methodreply_err", windll["MSAJApi"]), ((1, 'bus'),(1, 'msg'),(1, 'error'),(1, 'errorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_methodreply_status():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_message,win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("alljoyn_busobject_methodreply_status", windll["MSAJApi"]), ((1, 'bus'),(1, 'msg'),(1, 'status'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_getbusattachment():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busobject_getbusattachment", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_signal():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Foundation.PSTR,UInt32,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,UInt16,Byte,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_busobject_signal", windll["MSAJApi"]), ((1, 'bus'),(1, 'destination'),(1, 'sessionId'),(1, 'signal'),(1, 'args'),(1, 'numArgs'),(1, 'timeToLive'),(1, 'flags'),(1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_cancelsessionlessmessage_serial():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,UInt32, use_last_error=False)(("alljoyn_busobject_cancelsessionlessmessage_serial", windll["MSAJApi"]), ((1, 'bus'),(1, 'serialNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_cancelsessionlessmessage():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_message, use_last_error=False)(("alljoyn_busobject_cancelsessionlessmessage", windll["MSAJApi"]), ((1, 'bus'),(1, 'msg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_issecure():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busobject_issecure", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_getannouncedinterfacenames():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_busobject,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_busobject_getannouncedinterfacenames", windll["MSAJApi"]), ((1, 'bus'),(1, 'interfaces'),(1, 'numInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_setannounceflag():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_about_announceflag, use_last_error=False)(("alljoyn_busobject_setannounceflag", windll["MSAJApi"]), ((1, 'bus'),(1, 'iface'),(1, 'isAnnounced'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busobject_addinterface_announced():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_busobject_addinterface_announced", windll["MSAJApi"]), ((1, 'bus'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_proxybusobject_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'service'),(1, 'path'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_create_secure():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_proxybusobject_create_secure", windll["MSAJApi"]), ((1, 'bus'),(1, 'service'),(1, 'path'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_destroy", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_addinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_proxybusobject_addinterface", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_addinterface_by_name():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_addinterface_by_name", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getchildren():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_proxybusobject,POINTER(win32more.Devices.AllJoyn.alljoyn_proxybusobject),UIntPtr, use_last_error=False)(("alljoyn_proxybusobject_getchildren", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'children'),(1, 'numChildren'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getchild():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_getchild", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_addchild():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_addchild", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'child'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_removechild():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_removechild", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_introspectremoteobject():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_introspectremoteobject", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_introspectremoteobjectasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_introspectcb_ptr,c_void_p, use_last_error=False)(("alljoyn_proxybusobject_introspectremoteobjectasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getproperty():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_proxybusobject_getproperty", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'property'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getpropertyasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_getpropertycb_ptr,UInt32,c_void_p, use_last_error=False)(("alljoyn_proxybusobject_getpropertyasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'property'),(1, 'callback'),(1, 'timeout'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getallproperties():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_proxybusobject_getallproperties", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getallpropertiesasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_getallpropertiescb_ptr,UInt32,c_void_p, use_last_error=False)(("alljoyn_proxybusobject_getallpropertiesasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'callback'),(1, 'timeout'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_setproperty():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_proxybusobject_setproperty", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'property'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_registerpropertieschangedlistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UIntPtr,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_propertieschanged_ptr,c_void_p, use_last_error=False)(("alljoyn_proxybusobject_registerpropertieschangedlistener", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'properties'),(1, 'numProperties'),(1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_unregisterpropertieschangedlistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_propertieschanged_ptr, use_last_error=False)(("alljoyn_proxybusobject_unregisterpropertieschangedlistener", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_setpropertyasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_setpropertycb_ptr,UInt32,c_void_p, use_last_error=False)(("alljoyn_proxybusobject_setpropertyasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),(1, 'property'),(1, 'value'),(1, 'callback'),(1, 'timeout'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcall():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,win32more.Devices.AllJoyn.alljoyn_message,UInt32,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcall", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'ifaceName'),(1, 'methodName'),(1, 'args'),(1, 'numArgs'),(1, 'replyMsg'),(1, 'timeout'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcall_member():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,win32more.Devices.AllJoyn.alljoyn_message,UInt32,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcall_member", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'method'),(1, 'args'),(1, 'numArgs'),(1, 'replyMsg'),(1, 'timeout'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcall_noreply():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcall_noreply", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'ifaceName'),(1, 'methodName'),(1, 'args'),(1, 'numArgs'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcall_member_noreply():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcall_member_noreply", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'method'),(1, 'args'),(1, 'numArgs'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcallasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_messagereceiver_replyhandler_ptr,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,c_void_p,UInt32,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcallasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'ifaceName'),(1, 'methodName'),(1, 'replyFunc'),(1, 'args'),(1, 'numArgs'),(1, 'context'),(1, 'timeout'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_methodcallasync_member():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Devices.AllJoyn.alljoyn_messagereceiver_replyhandler_ptr,win32more.Devices.AllJoyn.alljoyn_msgarg,UIntPtr,c_void_p,UInt32,Byte, use_last_error=False)(("alljoyn_proxybusobject_methodcallasync_member", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'method'),(1, 'replyFunc'),(1, 'args'),(1, 'numArgs'),(1, 'context'),(1, 'timeout'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_parsexml():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_parsexml", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'xml'),(1, 'identifier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_secureconnection():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,Int32, use_last_error=False)(("alljoyn_proxybusobject_secureconnection", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'forceAuth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_secureconnectionasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_proxybusobject,Int32, use_last_error=False)(("alljoyn_proxybusobject_secureconnectionasync", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'forceAuth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_getinterface", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getinterfaces():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_proxybusobject,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription),UIntPtr, use_last_error=False)(("alljoyn_proxybusobject_getinterfaces", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'ifaces'),(1, 'numIfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getpath():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_getpath", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getservicename():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_getservicename", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getuniquename():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_getuniquename", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_getsessionid():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_getsessionid", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_implementsinterface():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_proxybusobject_implementsinterface", windll["MSAJApi"]), ((1, 'proxyObj'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_copy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_copy", windll["MSAJApi"]), ((1, 'source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_isvalid():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_isvalid", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_issecure():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_issecure", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_enablepropertycaching():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_enablepropertycaching", windll["MSAJApi"]), ((1, 'proxyObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurationlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_permissionconfigurationlistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_permissionconfigurationlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener, use_last_error=False)(("alljoyn_permissionconfigurationlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_sessionlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_sessionlistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_sessionlistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionlistener, use_last_error=False)(("alljoyn_sessionlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionportlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_sessionportlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_sessionportlistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_sessionportlistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_sessionportlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_sessionportlistener, use_last_error=False)(("alljoyn_sessionportlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_aboutlistener_callback_head),c_void_p, use_last_error=False)(("alljoyn_aboutlistener_create", windll["MSAJApi"]), ((1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutlistener, use_last_error=False)(("alljoyn_aboutlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,Int32, use_last_error=False)(("alljoyn_busattachment_create", windll["MSAJApi"]), ((1, 'applicationName'),(1, 'allowRemoteMessages'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_create_concurrency():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,Int32,UInt32, use_last_error=False)(("alljoyn_busattachment_create_concurrency", windll["MSAJApi"]), ((1, 'applicationName'),(1, 'allowRemoteMessages'),(1, 'concurrency'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_destroy", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_start():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_start", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_stop():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_stop", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_join():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_join", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getconcurrency():
    try:
        return WINFUNCTYPE(UInt32,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getconcurrency", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getconnectspec():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getconnectspec", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_enableconcurrentcallbacks():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_enableconcurrentcallbacks", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_createinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription), use_last_error=False)(("alljoyn_busattachment_createinterface", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_createinterface_secure():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription),win32more.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy, use_last_error=False)(("alljoyn_busattachment_createinterface_secure", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'iface'),(1, 'secPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_connect():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_connect", windll["MSAJApi"]), ((1, 'bus'),(1, 'connectSpec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registerbuslistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_buslistener, use_last_error=False)(("alljoyn_busattachment_registerbuslistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisterbuslistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_buslistener, use_last_error=False)(("alljoyn_busattachment_unregisterbuslistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_findadvertisedname():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_findadvertisedname", windll["MSAJApi"]), ((1, 'bus'),(1, 'namePrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_findadvertisednamebytransport():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16, use_last_error=False)(("alljoyn_busattachment_findadvertisednamebytransport", windll["MSAJApi"]), ((1, 'bus'),(1, 'namePrefix'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_cancelfindadvertisedname():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_cancelfindadvertisedname", windll["MSAJApi"]), ((1, 'bus'),(1, 'namePrefix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_cancelfindadvertisednamebytransport():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16, use_last_error=False)(("alljoyn_busattachment_cancelfindadvertisednamebytransport", windll["MSAJApi"]), ((1, 'bus'),(1, 'namePrefix'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_advertisename():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16, use_last_error=False)(("alljoyn_busattachment_advertisename", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_canceladvertisename():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16, use_last_error=False)(("alljoyn_busattachment_canceladvertisename", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'transports'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_interfacedescription,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_getinterface", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_joinsession():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16,win32more.Devices.AllJoyn.alljoyn_sessionlistener,POINTER(UInt32),win32more.Devices.AllJoyn.alljoyn_sessionopts, use_last_error=False)(("alljoyn_busattachment_joinsession", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionHost'),(1, 'sessionPort'),(1, 'listener'),(1, 'sessionId'),(1, 'opts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_joinsessionasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt16,win32more.Devices.AllJoyn.alljoyn_sessionlistener,win32more.Devices.AllJoyn.alljoyn_sessionopts,win32more.Devices.AllJoyn.alljoyn_busattachment_joinsessioncb_ptr,c_void_p, use_last_error=False)(("alljoyn_busattachment_joinsessionasync", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionHost'),(1, 'sessionPort'),(1, 'listener'),(1, 'opts'),(1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registerbusobject():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busattachment_registerbusobject", windll["MSAJApi"]), ((1, 'bus'),(1, 'obj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registerbusobject_secure():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busattachment_registerbusobject_secure", windll["MSAJApi"]), ((1, 'bus'),(1, 'obj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisterbusobject():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_busobject, use_last_error=False)(("alljoyn_busattachment_unregisterbusobject", windll["MSAJApi"]), ((1, 'bus'),(1, 'object'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_requestname():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_busattachment_requestname", windll["MSAJApi"]), ((1, 'bus'),(1, 'requestedName'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_releasename():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_releasename", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_bindsessionport():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(UInt16),win32more.Devices.AllJoyn.alljoyn_sessionopts,win32more.Devices.AllJoyn.alljoyn_sessionportlistener, use_last_error=False)(("alljoyn_busattachment_bindsessionport", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionPort'),(1, 'opts'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unbindsessionport():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt16, use_last_error=False)(("alljoyn_busattachment_unbindsessionport", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_enablepeersecurity():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_authlistener,win32more.Foundation.PSTR,Int32, use_last_error=False)(("alljoyn_busattachment_enablepeersecurity", windll["MSAJApi"]), ((1, 'bus'),(1, 'authMechanisms'),(1, 'listener'),(1, 'keyStoreFileName'),(1, 'isShared'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_authlistener,win32more.Foundation.PSTR,Int32,win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener, use_last_error=False)(("alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'authMechanisms'),(1, 'authListener'),(1, 'keyStoreFileName'),(1, 'isShared'),(1, 'permissionConfigurationListener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_ispeersecurityenabled():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_ispeersecurityenabled", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_createinterfacesfromxml():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_createinterfacesfromxml", windll["MSAJApi"]), ((1, 'bus'),(1, 'xml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getinterfaces():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription),UIntPtr, use_last_error=False)(("alljoyn_busattachment_getinterfaces", windll["MSAJApi"]), ((1, 'bus'),(1, 'ifaces'),(1, 'numIfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_deleteinterface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_interfacedescription, use_last_error=False)(("alljoyn_busattachment_deleteinterface", windll["MSAJApi"]), ((1, 'bus'),(1, 'iface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_isstarted():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_isstarted", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_isstopping():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_isstopping", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_isconnected():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_isconnected", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_disconnect():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_disconnect", windll["MSAJApi"]), ((1, 'bus'),(1, 'unused'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getdbusproxyobj():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getdbusproxyobj", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getalljoynproxyobj():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getalljoynproxyobj", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getalljoyndebugobj():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getalljoyndebugobj", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getuniquename():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getuniquename", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getglobalguidstring():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getglobalguidstring", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registersignalhandler():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_registersignalhandler", windll["MSAJApi"]), ((1, 'bus'),(1, 'signal_handler'),(1, 'member'),(1, 'srcPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registersignalhandlerwithrule():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_registersignalhandlerwithrule", windll["MSAJApi"]), ((1, 'bus'),(1, 'signal_handler'),(1, 'member'),(1, 'matchRule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregistersignalhandler():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_unregistersignalhandler", windll["MSAJApi"]), ((1, 'bus'),(1, 'signal_handler'),(1, 'member'),(1, 'srcPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregistersignalhandlerwithrule():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr,win32more.Devices.AllJoyn.alljoyn_interfacedescription_member,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_unregistersignalhandlerwithrule", windll["MSAJApi"]), ((1, 'bus'),(1, 'signal_handler'),(1, 'member'),(1, 'matchRule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisterallhandlers():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_unregisterallhandlers", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registerkeystorelistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_keystorelistener, use_last_error=False)(("alljoyn_busattachment_registerkeystorelistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_reloadkeystore():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_reloadkeystore", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_clearkeystore():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_clearkeystore", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_clearkeys():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_clearkeys", windll["MSAJApi"]), ((1, 'bus'),(1, 'guid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_setkeyexpiration():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_busattachment_setkeyexpiration", windll["MSAJApi"]), ((1, 'bus'),(1, 'guid'),(1, 'timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getkeyexpiration():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("alljoyn_busattachment_getkeyexpiration", windll["MSAJApi"]), ((1, 'bus'),(1, 'guid'),(1, 'timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_addlogonentry():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_addlogonentry", windll["MSAJApi"]), ((1, 'bus'),(1, 'authMechanism'),(1, 'userName'),(1, 'password'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_addmatch():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_addmatch", windll["MSAJApi"]), ((1, 'bus'),(1, 'rule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_removematch():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_removematch", windll["MSAJApi"]), ((1, 'bus'),(1, 'rule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_setsessionlistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt32,win32more.Devices.AllJoyn.alljoyn_sessionlistener, use_last_error=False)(("alljoyn_busattachment_setsessionlistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionId'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_leavesession():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt32, use_last_error=False)(("alljoyn_busattachment_leavesession", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_secureconnection():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,Int32, use_last_error=False)(("alljoyn_busattachment_secureconnection", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'forceAuth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_secureconnectionasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,Int32, use_last_error=False)(("alljoyn_busattachment_secureconnectionasync", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'forceAuth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_removesessionmember():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_removesessionmember", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionId'),(1, 'memberName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_setlinktimeout():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt32,POINTER(UInt32), use_last_error=False)(("alljoyn_busattachment_setlinktimeout", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionid'),(1, 'linkTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_setlinktimeoutasync():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,UInt32,UInt32,win32more.Devices.AllJoyn.alljoyn_busattachment_setlinktimeoutcb_ptr,c_void_p, use_last_error=False)(("alljoyn_busattachment_setlinktimeoutasync", windll["MSAJApi"]), ((1, 'bus'),(1, 'sessionid'),(1, 'linkTimeout'),(1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_namehasowner():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,POINTER(Int32), use_last_error=False)(("alljoyn_busattachment_namehasowner", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'hasOwner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getpeerguid():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UIntPtr), use_last_error=False)(("alljoyn_busattachment_getpeerguid", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'guid'),(1, 'guidSz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_setdaemondebug():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_busattachment_setdaemondebug", windll["MSAJApi"]), ((1, 'bus'),(1, 'module'),(1, 'level'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_gettimestamp():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("alljoyn_busattachment_gettimestamp", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_ping():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_busattachment_ping", windll["MSAJApi"]), ((1, 'bus'),(1, 'name'),(1, 'timeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registeraboutlistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_aboutlistener, use_last_error=False)(("alljoyn_busattachment_registeraboutlistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'aboutListener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisteraboutlistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_aboutlistener, use_last_error=False)(("alljoyn_busattachment_unregisteraboutlistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'aboutListener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisterallaboutlisteners():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_unregisterallaboutlisteners", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_whoimplements_interfaces():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_busattachment_whoimplements_interfaces", windll["MSAJApi"]), ((1, 'bus'),(1, 'implementsInterfaces'),(1, 'numberInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_whoimplements_interface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_whoimplements_interface", windll["MSAJApi"]), ((1, 'bus'),(1, 'implementsInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_cancelwhoimplements_interfaces():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_busattachment_cancelwhoimplements_interfaces", windll["MSAJApi"]), ((1, 'bus'),(1, 'implementsInterfaces'),(1, 'numberInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_cancelwhoimplements_interface():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_cancelwhoimplements_interface", windll["MSAJApi"]), ((1, 'bus'),(1, 'implementsInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_getpermissionconfigurator():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_permissionconfigurator,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_busattachment_getpermissionconfigurator", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_registerapplicationstatelistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_applicationstatelistener, use_last_error=False)(("alljoyn_busattachment_registerapplicationstatelistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_unregisterapplicationstatelistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_applicationstatelistener, use_last_error=False)(("alljoyn_busattachment_unregisterapplicationstatelistener", windll["MSAJApi"]), ((1, 'bus'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_busattachment_deletedefaultkeystore():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_busattachment_deletedefaultkeystore", windll["MSAJApi"]), ((1, 'applicationName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonobj_create():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonobj_handle_head),win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), use_last_error=False)(("alljoyn_abouticonobj_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'icon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonobj_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonobj_handle_head), use_last_error=False)(("alljoyn_abouticonobj_destroy", windll["MSAJApi"]), ((1, 'icon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonproxy_create():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head),win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_abouticonproxy_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'busName'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonproxy_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head), use_last_error=False)(("alljoyn_abouticonproxy_destroy", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonproxy_geticon():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head),POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), use_last_error=False)(("alljoyn_abouticonproxy_geticon", windll["MSAJApi"]), ((1, 'proxy'),(1, 'icon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_abouticonproxy_getversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head),POINTER(UInt16), use_last_error=False)(("alljoyn_abouticonproxy_getversion", windll["MSAJApi"]), ((1, 'proxy'),(1, 'version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdatalistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutdatalistener,POINTER(win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_callbacks_head),c_void_p, use_last_error=False)(("alljoyn_aboutdatalistener_create", windll["MSAJApi"]), ((1, 'callbacks'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutdatalistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutdatalistener, use_last_error=False)(("alljoyn_aboutdatalistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobj_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutobj,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Devices.AllJoyn.alljoyn_about_announceflag, use_last_error=False)(("alljoyn_aboutobj_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'isAnnounced'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobj_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutobj, use_last_error=False)(("alljoyn_aboutobj_destroy", windll["MSAJApi"]), ((1, 'obj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobj_announce():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutobj,UInt16,win32more.Devices.AllJoyn.alljoyn_aboutdata, use_last_error=False)(("alljoyn_aboutobj_announce", windll["MSAJApi"]), ((1, 'obj'),(1, 'sessionPort'),(1, 'aboutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobj_announce_using_datalistener():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutobj,UInt16,win32more.Devices.AllJoyn.alljoyn_aboutdatalistener, use_last_error=False)(("alljoyn_aboutobj_announce_using_datalistener", windll["MSAJApi"]), ((1, 'obj'),(1, 'sessionPort'),(1, 'aboutListener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobj_unannounce():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutobj, use_last_error=False)(("alljoyn_aboutobj_unannounce", windll["MSAJApi"]), ((1, 'obj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, use_last_error=False)(("alljoyn_aboutobjectdescription_create", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_create_full():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutobjectdescription_create_full", windll["MSAJApi"]), ((1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_createfrommsgarg():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutobjectdescription_createfrommsgarg", windll["MSAJApi"]), ((1, 'description'),(1, 'arg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, use_last_error=False)(("alljoyn_aboutobjectdescription_destroy", windll["MSAJApi"]), ((1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_getpaths():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_aboutobjectdescription_getpaths", windll["MSAJApi"]), ((1, 'description'),(1, 'paths'),(1, 'numPaths'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_getinterfaces():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_aboutobjectdescription_getinterfaces", windll["MSAJApi"]), ((1, 'description'),(1, 'path'),(1, 'interfaces'),(1, 'numInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_getinterfacepaths():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_aboutobjectdescription_getinterfacepaths", windll["MSAJApi"]), ((1, 'description'),(1, 'interfaceName'),(1, 'paths'),(1, 'numPaths'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_clear():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, use_last_error=False)(("alljoyn_aboutobjectdescription_clear", windll["MSAJApi"]), ((1, 'description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_haspath():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutobjectdescription_haspath", windll["MSAJApi"]), ((1, 'description'),(1, 'path'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_hasinterface():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutobjectdescription_hasinterface", windll["MSAJApi"]), ((1, 'description'),(1, 'interfaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_hasinterfaceatpath():
    try:
        return WINFUNCTYPE(Byte,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_aboutobjectdescription_hasinterfaceatpath", windll["MSAJApi"]), ((1, 'description'),(1, 'path'),(1, 'interfaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutobjectdescription_getmsgarg():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutobjectdescription_getmsgarg", windll["MSAJApi"]), ((1, 'description'),(1, 'msgArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutproxy_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_aboutproxy,win32more.Devices.AllJoyn.alljoyn_busattachment,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_aboutproxy_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'busName'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutproxy_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_aboutproxy, use_last_error=False)(("alljoyn_aboutproxy_destroy", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutproxy_getobjectdescription():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutproxy,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutproxy_getobjectdescription", windll["MSAJApi"]), ((1, 'proxy'),(1, 'objectDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutproxy_getaboutdata():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutproxy,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_msgarg, use_last_error=False)(("alljoyn_aboutproxy_getaboutdata", windll["MSAJApi"]), ((1, 'proxy'),(1, 'language'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_aboutproxy_getversion():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_aboutproxy,POINTER(UInt16), use_last_error=False)(("alljoyn_aboutproxy_getversion", windll["MSAJApi"]), ((1, 'proxy'),(1, 'version'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_pinglistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_pinglistener,POINTER(win32more.Devices.AllJoyn.alljoyn_pinglistener_callback_head),c_void_p, use_last_error=False)(("alljoyn_pinglistener_create", windll["MSAJApi"]), ((1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_pinglistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_pinglistener, use_last_error=False)(("alljoyn_pinglistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Devices.AllJoyn.alljoyn_busattachment, use_last_error=False)(("alljoyn_autopinger_create", windll["MSAJApi"]), ((1, 'bus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_autopinger, use_last_error=False)(("alljoyn_autopinger_destroy", windll["MSAJApi"]), ((1, 'autopinger'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_pause():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_autopinger, use_last_error=False)(("alljoyn_autopinger_pause", windll["MSAJApi"]), ((1, 'autopinger'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_resume():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_autopinger, use_last_error=False)(("alljoyn_autopinger_resume", windll["MSAJApi"]), ((1, 'autopinger'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_addpinggroup():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Foundation.PSTR,win32more.Devices.AllJoyn.alljoyn_pinglistener,UInt32, use_last_error=False)(("alljoyn_autopinger_addpinggroup", windll["MSAJApi"]), ((1, 'autopinger'),(1, 'group'),(1, 'listener'),(1, 'pinginterval'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_removepinggroup():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_autopinger_removepinggroup", windll["MSAJApi"]), ((1, 'autopinger'),(1, 'group'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_setpinginterval():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("alljoyn_autopinger_setpinginterval", windll["MSAJApi"]), ((1, 'autopinger'),(1, 'group'),(1, 'pinginterval'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_adddestination():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_autopinger_adddestination", windll["MSAJApi"]), ((1, 'autopinger'),(1, 'group'),(1, 'destination'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_autopinger_removedestination():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_autopinger,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("alljoyn_autopinger_removedestination", windll["MSAJApi"]), ((1, 'autopinger'),(1, 'group'),(1, 'destination'),(1, 'removeall'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_getversion():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_getversion", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_getbuildinfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_getbuildinfo", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_getnumericversion():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("alljoyn_getnumericversion", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_init():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("alljoyn_init", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_shutdown():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("alljoyn_shutdown", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_routerinit():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("alljoyn_routerinit", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_routerinitwithconfig():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(SByte), use_last_error=False)(("alljoyn_routerinitwithconfig", windll["MSAJApi"]), ((1, 'configXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_routershutdown():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus, use_last_error=False)(("alljoyn_routershutdown", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_ref_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref,win32more.Devices.AllJoyn.alljoyn_proxybusobject, use_last_error=False)(("alljoyn_proxybusobject_ref_create", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_ref_get():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)(("alljoyn_proxybusobject_ref_get", windll["MSAJApi"]), ((1, 'ref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_ref_incref():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)(("alljoyn_proxybusobject_ref_incref", windll["MSAJApi"]), ((1, 'ref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_proxybusobject_ref_decref():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)(("alljoyn_proxybusobject_ref_decref", windll["MSAJApi"]), ((1, 'ref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observerlistener_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_observerlistener,POINTER(win32more.Devices.AllJoyn.alljoyn_observerlistener_callback_head),c_void_p, use_last_error=False)(("alljoyn_observerlistener_create", windll["MSAJApi"]), ((1, 'callback'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observerlistener_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_observerlistener, use_last_error=False)(("alljoyn_observerlistener_destroy", windll["MSAJApi"]), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_observer,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_observer_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'mandatoryInterfaces'),(1, 'numMandatoryInterfaces'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_observer, use_last_error=False)(("alljoyn_observer_destroy", windll["MSAJApi"]), ((1, 'observer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_registerlistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_observer,win32more.Devices.AllJoyn.alljoyn_observerlistener,Int32, use_last_error=False)(("alljoyn_observer_registerlistener", windll["MSAJApi"]), ((1, 'observer'),(1, 'listener'),(1, 'triggerOnExisting'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_unregisterlistener():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_observer,win32more.Devices.AllJoyn.alljoyn_observerlistener, use_last_error=False)(("alljoyn_observer_unregisterlistener", windll["MSAJApi"]), ((1, 'observer'),(1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_unregisteralllisteners():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_observer, use_last_error=False)(("alljoyn_observer_unregisteralllisteners", windll["MSAJApi"]), ((1, 'observer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_get():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref,win32more.Devices.AllJoyn.alljoyn_observer,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_observer_get", windll["MSAJApi"]), ((1, 'observer'),(1, 'uniqueBusName'),(1, 'objectPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_getfirst():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref,win32more.Devices.AllJoyn.alljoyn_observer, use_last_error=False)(("alljoyn_observer_getfirst", windll["MSAJApi"]), ((1, 'observer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_observer_getnext():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref,win32more.Devices.AllJoyn.alljoyn_observer,win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref, use_last_error=False)(("alljoyn_observer_getnext", windll["MSAJApi"]), ((1, 'observer'),(1, 'proxyref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_passwordmanager_setcredentials():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("alljoyn_passwordmanager_setcredentials", windll["MSAJApi"]), ((1, 'authMechanism'),(1, 'password'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getpermissionmanagementsessionport():
    try:
        return WINFUNCTYPE(UInt16, use_last_error=False)(("alljoyn_securityapplicationproxy_getpermissionmanagementsessionport", windll["MSAJApi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_create():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,win32more.Devices.AllJoyn.alljoyn_busattachment,POINTER(SByte),UInt32, use_last_error=False)(("alljoyn_securityapplicationproxy_create", windll["MSAJApi"]), ((1, 'bus'),(1, 'appBusName'),(1, 'sessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_destroy():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, use_last_error=False)(("alljoyn_securityapplicationproxy_destroy", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_claim():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(SByte),POINTER(SByte),c_char_p_no,UIntPtr,POINTER(SByte),POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_securityapplicationproxy_claim", windll["MSAJApi"]), ((1, 'proxy'),(1, 'caKey'),(1, 'identityCertificateChain'),(1, 'groupId'),(1, 'groupSize'),(1, 'groupAuthority'),(1, 'manifestsXmls'),(1, 'manifestsCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getmanifesttemplate():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_getmanifesttemplate", windll["MSAJApi"]), ((1, 'proxy'),(1, 'manifestTemplateXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_manifesttemplate_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_manifesttemplate_destroy", windll["MSAJApi"]), ((1, 'manifestTemplateXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getapplicationstate():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstate), use_last_error=False)(("alljoyn_securityapplicationproxy_getapplicationstate", windll["MSAJApi"]), ((1, 'proxy'),(1, 'applicationState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getclaimcapabilities():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(UInt16), use_last_error=False)(("alljoyn_securityapplicationproxy_getclaimcapabilities", windll["MSAJApi"]), ((1, 'proxy'),(1, 'capabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(UInt16), use_last_error=False)(("alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo", windll["MSAJApi"]), ((1, 'proxy'),(1, 'additionalInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_getpolicy", windll["MSAJApi"]), ((1, 'proxy'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_getdefaultpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_getdefaultpolicy", windll["MSAJApi"]), ((1, 'proxy'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_policy_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_policy_destroy", windll["MSAJApi"]), ((1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_updatepolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_updatepolicy", windll["MSAJApi"]), ((1, 'proxy'),(1, 'policyXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_updateidentity():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(SByte),POINTER(POINTER(SByte)),UIntPtr, use_last_error=False)(("alljoyn_securityapplicationproxy_updateidentity", windll["MSAJApi"]), ((1, 'proxy'),(1, 'identityCertificateChain'),(1, 'manifestsXmls'),(1, 'manifestsCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_installmembership():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_installmembership", windll["MSAJApi"]), ((1, 'proxy'),(1, 'membershipCertificateChain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_reset():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, use_last_error=False)(("alljoyn_securityapplicationproxy_reset", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_resetpolicy():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, use_last_error=False)(("alljoyn_securityapplicationproxy_resetpolicy", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_startmanagement():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, use_last_error=False)(("alljoyn_securityapplicationproxy_startmanagement", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_endmanagement():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, use_last_error=False)(("alljoyn_securityapplicationproxy_endmanagement", windll["MSAJApi"]), ((1, 'proxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_geteccpublickey():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_geteccpublickey", windll["MSAJApi"]), ((1, 'proxy'),(1, 'eccPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_eccpublickey_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_eccpublickey_destroy", windll["MSAJApi"]), ((1, 'eccPublicKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_signmanifest():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(SByte),POINTER(SByte),POINTER(SByte),POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_signmanifest", windll["MSAJApi"]), ((1, 'unsignedManifestXml'),(1, 'identityCertificatePem'),(1, 'signingPrivateKeyPem'),(1, 'signedManifestXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_manifest_destroy():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte), use_last_error=False)(("alljoyn_securityapplicationproxy_manifest_destroy", windll["MSAJApi"]), ((1, 'signedManifestXml'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_computemanifestdigest():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(SByte),POINTER(SByte),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)(("alljoyn_securityapplicationproxy_computemanifestdigest", windll["MSAJApi"]), ((1, 'unsignedManifestXml'),(1, 'identityCertificatePem'),(1, 'digest'),(1, 'digestSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_digest_destroy():
    try:
        return WINFUNCTYPE(Void,c_char_p_no, use_last_error=False)(("alljoyn_securityapplicationproxy_digest_destroy", windll["MSAJApi"]), ((1, 'digest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_alljoyn_securityapplicationproxy_setmanifestsignature():
    try:
        return WINFUNCTYPE(win32more.Devices.AllJoyn.QStatus,POINTER(SByte),POINTER(SByte),c_char_p_no,UIntPtr,POINTER(POINTER(SByte)), use_last_error=False)(("alljoyn_securityapplicationproxy_setmanifestsignature", windll["MSAJApi"]), ((1, 'unsignedManifestXml'),(1, 'identityCertificatePem'),(1, 'signature'),(1, 'signatureSize'),(1, 'signedManifestXml'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "QCC_TRUE",
    "QCC_FALSE",
    "ALLJOYN_MESSAGE_FLAG_NO_REPLY_EXPECTED",
    "ALLJOYN_MESSAGE_FLAG_AUTO_START",
    "ALLJOYN_MESSAGE_FLAG_ALLOW_REMOTE_MSG",
    "ALLJOYN_MESSAGE_FLAG_SESSIONLESS",
    "ALLJOYN_MESSAGE_FLAG_GLOBAL_BROADCAST",
    "ALLJOYN_MESSAGE_FLAG_ENCRYPTED",
    "ALLJOYN_TRAFFIC_TYPE_MESSAGES",
    "ALLJOYN_TRAFFIC_TYPE_RAW_UNRELIABLE",
    "ALLJOYN_TRAFFIC_TYPE_RAW_RELIABLE",
    "ALLJOYN_PROXIMITY_ANY",
    "ALLJOYN_PROXIMITY_PHYSICAL",
    "ALLJOYN_PROXIMITY_NETWORK",
    "ALLJOYN_READ_READY",
    "ALLJOYN_WRITE_READY",
    "ALLJOYN_DISCONNECTED",
    "ALLJOYN_LITTLE_ENDIAN",
    "ALLJOYN_BIG_ENDIAN",
    "ALLJOYN_MESSAGE_DEFAULT_TIMEOUT",
    "ALLJOYN_CRED_PASSWORD",
    "ALLJOYN_CRED_USER_NAME",
    "ALLJOYN_CRED_CERT_CHAIN",
    "ALLJOYN_CRED_PRIVATE_KEY",
    "ALLJOYN_CRED_LOGON_ENTRY",
    "ALLJOYN_CRED_EXPIRATION",
    "ALLJOYN_CRED_NEW_PASSWORD",
    "ALLJOYN_CRED_ONE_TIME_PWD",
    "ALLJOYN_PROP_ACCESS_READ",
    "ALLJOYN_PROP_ACCESS_WRITE",
    "ALLJOYN_PROP_ACCESS_RW",
    "ALLJOYN_MEMBER_ANNOTATE_NO_REPLY",
    "ALLJOYN_MEMBER_ANNOTATE_DEPRECATED",
    "ALLJOYN_MEMBER_ANNOTATE_SESSIONCAST",
    "ALLJOYN_MEMBER_ANNOTATE_SESSIONLESS",
    "ALLJOYN_MEMBER_ANNOTATE_UNICAST",
    "ALLJOYN_MEMBER_ANNOTATE_GLOBAL_BROADCAST",
    "alljoyn_about_announceflag",
    "UNANNOUNCED",
    "ANNOUNCED",
    "QStatus",
    "ER_OK",
    "ER_FAIL",
    "ER_UTF_CONVERSION_FAILED",
    "ER_BUFFER_TOO_SMALL",
    "ER_OS_ERROR",
    "ER_OUT_OF_MEMORY",
    "ER_SOCKET_BIND_ERROR",
    "ER_INIT_FAILED",
    "ER_WOULDBLOCK",
    "ER_NOT_IMPLEMENTED",
    "ER_TIMEOUT",
    "ER_SOCK_OTHER_END_CLOSED",
    "ER_BAD_ARG_1",
    "ER_BAD_ARG_2",
    "ER_BAD_ARG_3",
    "ER_BAD_ARG_4",
    "ER_BAD_ARG_5",
    "ER_BAD_ARG_6",
    "ER_BAD_ARG_7",
    "ER_BAD_ARG_8",
    "ER_INVALID_ADDRESS",
    "ER_INVALID_DATA",
    "ER_READ_ERROR",
    "ER_WRITE_ERROR",
    "ER_OPEN_FAILED",
    "ER_PARSE_ERROR",
    "ER_END_OF_DATA",
    "ER_CONN_REFUSED",
    "ER_BAD_ARG_COUNT",
    "ER_WARNING",
    "ER_EOF",
    "ER_DEADLOCK",
    "ER_COMMON_ERRORS",
    "ER_STOPPING_THREAD",
    "ER_ALERTED_THREAD",
    "ER_XML_MALFORMED",
    "ER_AUTH_FAIL",
    "ER_AUTH_USER_REJECT",
    "ER_NO_SUCH_ALARM",
    "ER_TIMER_FALLBEHIND",
    "ER_SSL_ERRORS",
    "ER_SSL_INIT",
    "ER_SSL_CONNECT",
    "ER_SSL_VERIFY",
    "ER_EXTERNAL_THREAD",
    "ER_CRYPTO_ERROR",
    "ER_CRYPTO_TRUNCATED",
    "ER_CRYPTO_KEY_UNAVAILABLE",
    "ER_BAD_HOSTNAME",
    "ER_CRYPTO_KEY_UNUSABLE",
    "ER_EMPTY_KEY_BLOB",
    "ER_CORRUPT_KEYBLOB",
    "ER_INVALID_KEY_ENCODING",
    "ER_DEAD_THREAD",
    "ER_THREAD_RUNNING",
    "ER_THREAD_STOPPING",
    "ER_BAD_STRING_ENCODING",
    "ER_CRYPTO_INSUFFICIENT_SECURITY",
    "ER_CRYPTO_ILLEGAL_PARAMETERS",
    "ER_CRYPTO_HASH_UNINITIALIZED",
    "ER_THREAD_NO_WAIT",
    "ER_TIMER_EXITING",
    "ER_INVALID_GUID",
    "ER_THREADPOOL_EXHAUSTED",
    "ER_THREADPOOL_STOPPING",
    "ER_INVALID_STREAM",
    "ER_TIMER_FULL",
    "ER_IODISPATCH_STOPPING",
    "ER_SLAP_INVALID_PACKET_LEN",
    "ER_SLAP_HDR_CHECKSUM_ERROR",
    "ER_SLAP_INVALID_PACKET_TYPE",
    "ER_SLAP_LEN_MISMATCH",
    "ER_SLAP_PACKET_TYPE_MISMATCH",
    "ER_SLAP_CRC_ERROR",
    "ER_SLAP_ERROR",
    "ER_SLAP_OTHER_END_CLOSED",
    "ER_TIMER_NOT_ALLOWED",
    "ER_NOT_CONN",
    "ER_XML_CONVERTER_ERROR",
    "ER_XML_INVALID_RULES_COUNT",
    "ER_XML_INTERFACE_MEMBERS_MISSING",
    "ER_XML_INVALID_MEMBER_TYPE",
    "ER_XML_INVALID_MEMBER_ACTION",
    "ER_XML_MEMBER_DENY_ACTION_WITH_OTHER",
    "ER_XML_INVALID_ANNOTATIONS_COUNT",
    "ER_XML_INVALID_ELEMENT_NAME",
    "ER_XML_INVALID_ATTRIBUTE_VALUE",
    "ER_XML_INVALID_SECURITY_LEVEL_ANNOTATION_VALUE",
    "ER_XML_INVALID_ELEMENT_CHILDREN_COUNT",
    "ER_XML_INVALID_POLICY_VERSION",
    "ER_XML_INVALID_POLICY_SERIAL_NUMBER",
    "ER_XML_INVALID_ACL_PEER_TYPE",
    "ER_XML_INVALID_ACL_PEER_CHILDREN_COUNT",
    "ER_XML_ACL_ALL_TYPE_PEER_WITH_OTHERS",
    "ER_XML_INVALID_ACL_PEER_PUBLIC_KEY",
    "ER_XML_ACL_PEER_NOT_UNIQUE",
    "ER_XML_ACL_PEER_PUBLIC_KEY_SET",
    "ER_XML_ACLS_MISSING",
    "ER_XML_ACL_PEERS_MISSING",
    "ER_XML_INVALID_OBJECT_PATH",
    "ER_XML_INVALID_INTERFACE_NAME",
    "ER_XML_INVALID_MEMBER_NAME",
    "ER_XML_INVALID_MANIFEST_VERSION",
    "ER_XML_INVALID_OID",
    "ER_XML_INVALID_BASE64",
    "ER_XML_INTERFACE_NAME_NOT_UNIQUE",
    "ER_XML_MEMBER_NAME_NOT_UNIQUE",
    "ER_XML_OBJECT_PATH_NOT_UNIQUE",
    "ER_XML_ANNOTATION_NOT_UNIQUE",
    "ER_NONE",
    "ER_BUS_ERRORS",
    "ER_BUS_READ_ERROR",
    "ER_BUS_WRITE_ERROR",
    "ER_BUS_BAD_VALUE_TYPE",
    "ER_BUS_BAD_HEADER_FIELD",
    "ER_BUS_BAD_SIGNATURE",
    "ER_BUS_BAD_OBJ_PATH",
    "ER_BUS_BAD_MEMBER_NAME",
    "ER_BUS_BAD_INTERFACE_NAME",
    "ER_BUS_BAD_ERROR_NAME",
    "ER_BUS_BAD_BUS_NAME",
    "ER_BUS_NAME_TOO_LONG",
    "ER_BUS_BAD_LENGTH",
    "ER_BUS_BAD_VALUE",
    "ER_BUS_BAD_HDR_FLAGS",
    "ER_BUS_BAD_BODY_LEN",
    "ER_BUS_BAD_HEADER_LEN",
    "ER_BUS_UNKNOWN_SERIAL",
    "ER_BUS_UNKNOWN_PATH",
    "ER_BUS_UNKNOWN_INTERFACE",
    "ER_BUS_ESTABLISH_FAILED",
    "ER_BUS_UNEXPECTED_SIGNATURE",
    "ER_BUS_INTERFACE_MISSING",
    "ER_BUS_PATH_MISSING",
    "ER_BUS_MEMBER_MISSING",
    "ER_BUS_REPLY_SERIAL_MISSING",
    "ER_BUS_ERROR_NAME_MISSING",
    "ER_BUS_INTERFACE_NO_SUCH_MEMBER",
    "ER_BUS_NO_SUCH_OBJECT",
    "ER_BUS_OBJECT_NO_SUCH_MEMBER",
    "ER_BUS_OBJECT_NO_SUCH_INTERFACE",
    "ER_BUS_NO_SUCH_INTERFACE",
    "ER_BUS_MEMBER_NO_SUCH_SIGNATURE",
    "ER_BUS_NOT_NUL_TERMINATED",
    "ER_BUS_NO_SUCH_PROPERTY",
    "ER_BUS_SET_WRONG_SIGNATURE",
    "ER_BUS_PROPERTY_VALUE_NOT_SET",
    "ER_BUS_PROPERTY_ACCESS_DENIED",
    "ER_BUS_NO_TRANSPORTS",
    "ER_BUS_BAD_TRANSPORT_ARGS",
    "ER_BUS_NO_ROUTE",
    "ER_BUS_NO_ENDPOINT",
    "ER_BUS_BAD_SEND_PARAMETER",
    "ER_BUS_UNMATCHED_REPLY_SERIAL",
    "ER_BUS_BAD_SENDER_ID",
    "ER_BUS_TRANSPORT_NOT_STARTED",
    "ER_BUS_EMPTY_MESSAGE",
    "ER_BUS_NOT_OWNER",
    "ER_BUS_SET_PROPERTY_REJECTED",
    "ER_BUS_CONNECT_FAILED",
    "ER_BUS_REPLY_IS_ERROR_MESSAGE",
    "ER_BUS_NOT_AUTHENTICATING",
    "ER_BUS_NO_LISTENER",
    "ER_BUS_NOT_ALLOWED",
    "ER_BUS_WRITE_QUEUE_FULL",
    "ER_BUS_ENDPOINT_CLOSING",
    "ER_BUS_INTERFACE_MISMATCH",
    "ER_BUS_MEMBER_ALREADY_EXISTS",
    "ER_BUS_PROPERTY_ALREADY_EXISTS",
    "ER_BUS_IFACE_ALREADY_EXISTS",
    "ER_BUS_ERROR_RESPONSE",
    "ER_BUS_BAD_XML",
    "ER_BUS_BAD_CHILD_PATH",
    "ER_BUS_OBJ_ALREADY_EXISTS",
    "ER_BUS_OBJ_NOT_FOUND",
    "ER_BUS_CANNOT_EXPAND_MESSAGE",
    "ER_BUS_NOT_COMPRESSED",
    "ER_BUS_ALREADY_CONNECTED",
    "ER_BUS_NOT_CONNECTED",
    "ER_BUS_ALREADY_LISTENING",
    "ER_BUS_KEY_UNAVAILABLE",
    "ER_BUS_TRUNCATED",
    "ER_BUS_KEY_STORE_NOT_LOADED",
    "ER_BUS_NO_AUTHENTICATION_MECHANISM",
    "ER_BUS_BUS_ALREADY_STARTED",
    "ER_BUS_BUS_NOT_STARTED",
    "ER_BUS_KEYBLOB_OP_INVALID",
    "ER_BUS_INVALID_HEADER_CHECKSUM",
    "ER_BUS_MESSAGE_NOT_ENCRYPTED",
    "ER_BUS_INVALID_HEADER_SERIAL",
    "ER_BUS_TIME_TO_LIVE_EXPIRED",
    "ER_BUS_HDR_EXPANSION_INVALID",
    "ER_BUS_MISSING_COMPRESSION_TOKEN",
    "ER_BUS_NO_PEER_GUID",
    "ER_BUS_MESSAGE_DECRYPTION_FAILED",
    "ER_BUS_SECURITY_FATAL",
    "ER_BUS_KEY_EXPIRED",
    "ER_BUS_CORRUPT_KEYSTORE",
    "ER_BUS_NO_CALL_FOR_REPLY",
    "ER_BUS_NOT_A_COMPLETE_TYPE",
    "ER_BUS_POLICY_VIOLATION",
    "ER_BUS_NO_SUCH_SERVICE",
    "ER_BUS_TRANSPORT_NOT_AVAILABLE",
    "ER_BUS_INVALID_AUTH_MECHANISM",
    "ER_BUS_KEYSTORE_VERSION_MISMATCH",
    "ER_BUS_BLOCKING_CALL_NOT_ALLOWED",
    "ER_BUS_SIGNATURE_MISMATCH",
    "ER_BUS_STOPPING",
    "ER_BUS_METHOD_CALL_ABORTED",
    "ER_BUS_CANNOT_ADD_INTERFACE",
    "ER_BUS_CANNOT_ADD_HANDLER",
    "ER_BUS_KEYSTORE_NOT_LOADED",
    "ER_BUS_NO_SUCH_HANDLE",
    "ER_BUS_HANDLES_NOT_ENABLED",
    "ER_BUS_HANDLES_MISMATCH",
    "ER_BUS_NO_SESSION",
    "ER_BUS_ELEMENT_NOT_FOUND",
    "ER_BUS_NOT_A_DICTIONARY",
    "ER_BUS_WAIT_FAILED",
    "ER_BUS_BAD_SESSION_OPTS",
    "ER_BUS_CONNECTION_REJECTED",
    "ER_DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER",
    "ER_DBUS_REQUEST_NAME_REPLY_IN_QUEUE",
    "ER_DBUS_REQUEST_NAME_REPLY_EXISTS",
    "ER_DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER",
    "ER_DBUS_RELEASE_NAME_REPLY_RELEASED",
    "ER_DBUS_RELEASE_NAME_REPLY_NON_EXISTENT",
    "ER_DBUS_RELEASE_NAME_REPLY_NOT_OWNER",
    "ER_DBUS_START_REPLY_ALREADY_RUNNING",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_ALREADY_EXISTS",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_FAILED",
    "ER_ALLJOYN_JOINSESSION_REPLY_NO_SESSION",
    "ER_ALLJOYN_JOINSESSION_REPLY_UNREACHABLE",
    "ER_ALLJOYN_JOINSESSION_REPLY_CONNECT_FAILED",
    "ER_ALLJOYN_JOINSESSION_REPLY_REJECTED",
    "ER_ALLJOYN_JOINSESSION_REPLY_BAD_SESSION_OPTS",
    "ER_ALLJOYN_JOINSESSION_REPLY_FAILED",
    "ER_ALLJOYN_LEAVESESSION_REPLY_NO_SESSION",
    "ER_ALLJOYN_LEAVESESSION_REPLY_FAILED",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_TRANSPORT_NOT_AVAILABLE",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_ALREADY_ADVERTISING",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_FAILED",
    "ER_ALLJOYN_CANCELADVERTISENAME_REPLY_FAILED",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_TRANSPORT_NOT_AVAILABLE",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_ALREADY_DISCOVERING",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_FAILED",
    "ER_ALLJOYN_CANCELFINDADVERTISEDNAME_REPLY_FAILED",
    "ER_BUS_UNEXPECTED_DISPOSITION",
    "ER_BUS_INTERFACE_ACTIVATED",
    "ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_BAD_PORT",
    "ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_FAILED",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_INVALID_OPTS",
    "ER_ALLJOYN_JOINSESSION_REPLY_ALREADY_JOINED",
    "ER_BUS_SELF_CONNECT",
    "ER_BUS_SECURITY_NOT_ENABLED",
    "ER_BUS_LISTENER_ALREADY_SET",
    "ER_BUS_PEER_AUTH_VERSION_MISMATCH",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NOT_SUPPORTED",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NO_DEST_SUPPORT",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_FAILED",
    "ER_ALLJOYN_ACCESS_PERMISSION_WARNING",
    "ER_ALLJOYN_ACCESS_PERMISSION_ERROR",
    "ER_BUS_DESTINATION_NOT_AUTHENTICATED",
    "ER_BUS_ENDPOINT_REDIRECTED",
    "ER_BUS_AUTHENTICATION_PENDING",
    "ER_BUS_NOT_AUTHORIZED",
    "ER_PACKET_BUS_NO_SUCH_CHANNEL",
    "ER_PACKET_BAD_FORMAT",
    "ER_PACKET_CONNECT_TIMEOUT",
    "ER_PACKET_CHANNEL_FAIL",
    "ER_PACKET_TOO_LARGE",
    "ER_PACKET_BAD_PARAMETER",
    "ER_PACKET_BAD_CRC",
    "ER_RENDEZVOUS_SERVER_DEACTIVATED_USER",
    "ER_RENDEZVOUS_SERVER_UNKNOWN_USER",
    "ER_UNABLE_TO_CONNECT_TO_RENDEZVOUS_SERVER",
    "ER_NOT_CONNECTED_TO_RENDEZVOUS_SERVER",
    "ER_UNABLE_TO_SEND_MESSAGE_TO_RENDEZVOUS_SERVER",
    "ER_INVALID_RENDEZVOUS_SERVER_INTERFACE_MESSAGE",
    "ER_INVALID_PERSISTENT_CONNECTION_MESSAGE_RESPONSE",
    "ER_INVALID_ON_DEMAND_CONNECTION_MESSAGE_RESPONSE",
    "ER_INVALID_HTTP_METHOD_USED_FOR_RENDEZVOUS_SERVER_INTERFACE_MESSAGE",
    "ER_RENDEZVOUS_SERVER_ERR500_INTERNAL_ERROR",
    "ER_RENDEZVOUS_SERVER_ERR503_STATUS_UNAVAILABLE",
    "ER_RENDEZVOUS_SERVER_ERR401_UNAUTHORIZED_REQUEST",
    "ER_RENDEZVOUS_SERVER_UNRECOVERABLE_ERROR",
    "ER_RENDEZVOUS_SERVER_ROOT_CERTIFICATE_UNINITIALIZED",
    "ER_BUS_NO_SUCH_ANNOTATION",
    "ER_BUS_ANNOTATION_ALREADY_EXISTS",
    "ER_SOCK_CLOSING",
    "ER_NO_SUCH_DEVICE",
    "ER_P2P",
    "ER_P2P_TIMEOUT",
    "ER_P2P_NOT_CONNECTED",
    "ER_BAD_TRANSPORT_MASK",
    "ER_PROXIMITY_CONNECTION_ESTABLISH_FAIL",
    "ER_PROXIMITY_NO_PEERS_FOUND",
    "ER_BUS_OBJECT_NOT_REGISTERED",
    "ER_P2P_DISABLED",
    "ER_P2P_BUSY",
    "ER_BUS_INCOMPATIBLE_DAEMON",
    "ER_P2P_NO_GO",
    "ER_P2P_NO_STA",
    "ER_P2P_FORBIDDEN",
    "ER_ALLJOYN_ONAPPSUSPEND_REPLY_FAILED",
    "ER_ALLJOYN_ONAPPSUSPEND_REPLY_UNSUPPORTED",
    "ER_ALLJOYN_ONAPPRESUME_REPLY_FAILED",
    "ER_ALLJOYN_ONAPPRESUME_REPLY_UNSUPPORTED",
    "ER_BUS_NO_SUCH_MESSAGE",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_NO_SESSION",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_BINDER",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_MULTIPOINT",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_FOUND",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_INCOMPATIBLE_REMOTE_DAEMON",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_FAILED",
    "ER_BUS_REMOVED_BY_BINDER",
    "ER_BUS_MATCH_RULE_NOT_FOUND",
    "ER_ALLJOYN_PING_FAILED",
    "ER_ALLJOYN_PING_REPLY_UNREACHABLE",
    "ER_UDP_MSG_TOO_LONG",
    "ER_UDP_DEMUX_NO_ENDPOINT",
    "ER_UDP_NO_NETWORK",
    "ER_UDP_UNEXPECTED_LENGTH",
    "ER_UDP_UNEXPECTED_FLOW",
    "ER_UDP_DISCONNECT",
    "ER_UDP_NOT_IMPLEMENTED",
    "ER_UDP_NO_LISTENER",
    "ER_UDP_STOPPING",
    "ER_ARDP_BACKPRESSURE",
    "ER_UDP_BACKPRESSURE",
    "ER_ARDP_INVALID_STATE",
    "ER_ARDP_TTL_EXPIRED",
    "ER_ARDP_PERSIST_TIMEOUT",
    "ER_ARDP_PROBE_TIMEOUT",
    "ER_ARDP_REMOTE_CONNECTION_RESET",
    "ER_UDP_BUSHELLO",
    "ER_UDP_MESSAGE",
    "ER_UDP_INVALID",
    "ER_UDP_UNSUPPORTED",
    "ER_UDP_ENDPOINT_STALLED",
    "ER_ARDP_INVALID_RESPONSE",
    "ER_ARDP_INVALID_CONNECTION",
    "ER_UDP_LOCAL_DISCONNECT",
    "ER_UDP_EARLY_EXIT",
    "ER_UDP_LOCAL_DISCONNECT_FAIL",
    "ER_ARDP_DISCONNECTING",
    "ER_ALLJOYN_PING_REPLY_INCOMPATIBLE_REMOTE_ROUTING_NODE",
    "ER_ALLJOYN_PING_REPLY_TIMEOUT",
    "ER_ALLJOYN_PING_REPLY_UNKNOWN_NAME",
    "ER_ALLJOYN_PING_REPLY_FAILED",
    "ER_TCP_MAX_UNTRUSTED",
    "ER_ALLJOYN_PING_REPLY_IN_PROGRESS",
    "ER_LANGUAGE_NOT_SUPPORTED",
    "ER_ABOUT_FIELD_ALREADY_SPECIFIED",
    "ER_UDP_NOT_DISCONNECTED",
    "ER_UDP_ENDPOINT_NOT_STARTED",
    "ER_UDP_ENDPOINT_REMOVED",
    "ER_ARDP_VERSION_NOT_SUPPORTED",
    "ER_CONNECTION_LIMIT_EXCEEDED",
    "ER_ARDP_WRITE_BLOCKED",
    "ER_PERMISSION_DENIED",
    "ER_ABOUT_DEFAULT_LANGUAGE_NOT_SPECIFIED",
    "ER_ABOUT_SESSIONPORT_NOT_BOUND",
    "ER_ABOUT_ABOUTDATA_MISSING_REQUIRED_FIELD",
    "ER_ABOUT_INVALID_ABOUTDATA_LISTENER",
    "ER_BUS_PING_GROUP_NOT_FOUND",
    "ER_BUS_REMOVED_BY_BINDER_SELF",
    "ER_INVALID_CONFIG",
    "ER_ABOUT_INVALID_ABOUTDATA_FIELD_VALUE",
    "ER_ABOUT_INVALID_ABOUTDATA_FIELD_APPID_SIZE",
    "ER_BUS_TRANSPORT_ACCESS_DENIED",
    "ER_INVALID_CERTIFICATE",
    "ER_CERTIFICATE_NOT_FOUND",
    "ER_DUPLICATE_CERTIFICATE",
    "ER_UNKNOWN_CERTIFICATE",
    "ER_MISSING_DIGEST_IN_CERTIFICATE",
    "ER_DIGEST_MISMATCH",
    "ER_DUPLICATE_KEY",
    "ER_NO_COMMON_TRUST",
    "ER_MANIFEST_NOT_FOUND",
    "ER_INVALID_CERT_CHAIN",
    "ER_NO_TRUST_ANCHOR",
    "ER_INVALID_APPLICATION_STATE",
    "ER_FEATURE_NOT_AVAILABLE",
    "ER_KEY_STORE_ALREADY_INITIALIZED",
    "ER_KEY_STORE_ID_NOT_YET_SET",
    "ER_POLICY_NOT_NEWER",
    "ER_MANIFEST_REJECTED",
    "ER_INVALID_CERTIFICATE_USAGE",
    "ER_INVALID_SIGNAL_EMISSION_TYPE",
    "ER_APPLICATION_STATE_LISTENER_ALREADY_EXISTS",
    "ER_APPLICATION_STATE_LISTENER_NO_SUCH_LISTENER",
    "ER_MANAGEMENT_ALREADY_STARTED",
    "ER_MANAGEMENT_NOT_STARTED",
    "ER_BUS_DESCRIPTION_ALREADY_EXISTS",
    "alljoyn_typeid",
    "ALLJOYN_INVALID",
    "ALLJOYN_ARRAY",
    "ALLJOYN_BOOLEAN",
    "ALLJOYN_DOUBLE",
    "ALLJOYN_DICT_ENTRY",
    "ALLJOYN_SIGNATURE",
    "ALLJOYN_HANDLE",
    "ALLJOYN_INT32",
    "ALLJOYN_INT16",
    "ALLJOYN_OBJECT_PATH",
    "ALLJOYN_UINT16",
    "ALLJOYN_STRUCT",
    "ALLJOYN_STRING",
    "ALLJOYN_UINT64",
    "ALLJOYN_UINT32",
    "ALLJOYN_VARIANT",
    "ALLJOYN_INT64",
    "ALLJOYN_BYTE",
    "ALLJOYN_STRUCT_OPEN",
    "ALLJOYN_STRUCT_CLOSE",
    "ALLJOYN_DICT_ENTRY_OPEN",
    "ALLJOYN_DICT_ENTRY_CLOSE",
    "ALLJOYN_BOOLEAN_ARRAY",
    "ALLJOYN_DOUBLE_ARRAY",
    "ALLJOYN_INT32_ARRAY",
    "ALLJOYN_INT16_ARRAY",
    "ALLJOYN_UINT16_ARRAY",
    "ALLJOYN_UINT64_ARRAY",
    "ALLJOYN_UINT32_ARRAY",
    "ALLJOYN_INT64_ARRAY",
    "ALLJOYN_BYTE_ARRAY",
    "ALLJOYN_WILDCARD",
    "_alljoyn_abouticon_handle",
    "alljoyn_applicationstate",
    "NOT_CLAIMABLE",
    "CLAIMABLE",
    "CLAIMED",
    "NEED_UPDATE",
    "alljoyn_claimcapability_masks",
    "CAPABLE_ECDHE_NULL",
    "CAPABLE_ECDHE_ECDSA",
    "CAPABLE_ECDHE_SPEKE",
    "alljoyn_claimcapabilityadditionalinfo_masks",
    "PASSWORD_GENERATED_BY_SECURITY_MANAGER",
    "PASSWORD_GENERATED_BY_APPLICATION",
    "alljoyn_certificateid",
    "alljoyn_certificateidarray",
    "alljoyn_manifestarray",
    "alljoyn_applicationstatelistener_state_ptr",
    "alljoyn_applicationstatelistener_callbacks",
    "alljoyn_keystorelistener_loadrequest_ptr",
    "alljoyn_keystorelistener_storerequest_ptr",
    "alljoyn_keystorelistener_acquireexclusivelock_ptr",
    "alljoyn_keystorelistener_releaseexclusivelock_ptr",
    "alljoyn_keystorelistener_callbacks",
    "alljoyn_keystorelistener_with_synchronization_callbacks",
    "alljoyn_messagetype",
    "ALLJOYN_MESSAGE_INVALID",
    "ALLJOYN_MESSAGE_METHOD_CALL",
    "ALLJOYN_MESSAGE_METHOD_RET",
    "ALLJOYN_MESSAGE_ERROR",
    "ALLJOYN_MESSAGE_SIGNAL",
    "alljoyn_authlistener_requestcredentials_ptr",
    "alljoyn_authlistener_requestcredentialsasync_ptr",
    "alljoyn_authlistener_verifycredentials_ptr",
    "alljoyn_authlistener_verifycredentialsasync_ptr",
    "alljoyn_authlistener_securityviolation_ptr",
    "alljoyn_authlistener_authenticationcomplete_ptr",
    "alljoyn_authlistener_callbacks",
    "alljoyn_authlistenerasync_callbacks",
    "alljoyn_buslistener_listener_registered_ptr",
    "alljoyn_buslistener_listener_unregistered_ptr",
    "alljoyn_buslistener_found_advertised_name_ptr",
    "alljoyn_buslistener_lost_advertised_name_ptr",
    "alljoyn_buslistener_name_owner_changed_ptr",
    "alljoyn_buslistener_bus_stopping_ptr",
    "alljoyn_buslistener_bus_disconnected_ptr",
    "alljoyn_buslistener_bus_prop_changed_ptr",
    "alljoyn_buslistener_callbacks",
    "alljoyn_interfacedescription_securitypolicy",
    "AJ_IFC_SECURITY_INHERIT",
    "AJ_IFC_SECURITY_REQUIRED",
    "AJ_IFC_SECURITY_OFF",
    "alljoyn_interfacedescription_member",
    "alljoyn_interfacedescription_translation_callback_ptr",
    "alljoyn_interfacedescription_property",
    "alljoyn_messagereceiver_methodhandler_ptr",
    "alljoyn_messagereceiver_replyhandler_ptr",
    "alljoyn_messagereceiver_signalhandler_ptr",
    "alljoyn_busobject_prop_get_ptr",
    "alljoyn_busobject_prop_set_ptr",
    "alljoyn_busobject_object_registration_ptr",
    "alljoyn_busobject_callbacks",
    "alljoyn_busobject_methodentry",
    "alljoyn_proxybusobject_listener_introspectcb_ptr",
    "alljoyn_proxybusobject_listener_getpropertycb_ptr",
    "alljoyn_proxybusobject_listener_getallpropertiescb_ptr",
    "alljoyn_proxybusobject_listener_setpropertycb_ptr",
    "alljoyn_proxybusobject_listener_propertieschanged_ptr",
    "alljoyn_permissionconfigurationlistener_factoryreset_ptr",
    "alljoyn_permissionconfigurationlistener_policychanged_ptr",
    "alljoyn_permissionconfigurationlistener_startmanagement_ptr",
    "alljoyn_permissionconfigurationlistener_endmanagement_ptr",
    "alljoyn_permissionconfigurationlistener_callbacks",
    "alljoyn_sessionlostreason",
    "ALLJOYN_SESSIONLOST_INVALID",
    "ALLJOYN_SESSIONLOST_REMOTE_END_LEFT_SESSION",
    "ALLJOYN_SESSIONLOST_REMOTE_END_CLOSED_ABRUPTLY",
    "ALLJOYN_SESSIONLOST_REMOVED_BY_BINDER",
    "ALLJOYN_SESSIONLOST_LINK_TIMEOUT",
    "ALLJOYN_SESSIONLOST_REASON_OTHER",
    "alljoyn_sessionlistener_sessionlost_ptr",
    "alljoyn_sessionlistener_sessionmemberadded_ptr",
    "alljoyn_sessionlistener_sessionmemberremoved_ptr",
    "alljoyn_sessionlistener_callbacks",
    "alljoyn_sessionportlistener_acceptsessionjoiner_ptr",
    "alljoyn_sessionportlistener_sessionjoined_ptr",
    "alljoyn_sessionportlistener_callbacks",
    "alljoyn_about_announced_ptr",
    "alljoyn_aboutlistener_callback",
    "alljoyn_busattachment_joinsessioncb_ptr",
    "alljoyn_busattachment_setlinktimeoutcb_ptr",
    "_alljoyn_abouticonobj_handle",
    "_alljoyn_abouticonproxy_handle",
    "alljoyn_aboutdatalistener_getaboutdata_ptr",
    "alljoyn_aboutdatalistener_getannouncedaboutdata_ptr",
    "alljoyn_aboutdatalistener_callbacks",
    "alljoyn_autopinger_destination_lost_ptr",
    "alljoyn_autopinger_destination_found_ptr",
    "alljoyn_pinglistener_callback",
    "alljoyn_observer_object_discovered_ptr",
    "alljoyn_observer_object_lost_ptr",
    "alljoyn_observerlistener_callback",
    "alljoyn_aboutdata",
    "alljoyn_aboutdatalistener",
    "alljoyn_aboutlistener",
    "alljoyn_aboutobj",
    "alljoyn_aboutobjectdescription",
    "alljoyn_aboutproxy",
    "alljoyn_applicationstatelistener",
    "alljoyn_authlistener",
    "alljoyn_autopinger",
    "alljoyn_busattachment",
    "alljoyn_buslistener",
    "alljoyn_busobject",
    "alljoyn_credentials",
    "alljoyn_interfacedescription",
    "alljoyn_keystore",
    "alljoyn_keystorelistener",
    "alljoyn_message",
    "alljoyn_msgarg",
    "alljoyn_observer",
    "alljoyn_observerlistener",
    "alljoyn_permissionconfigurationlistener",
    "alljoyn_permissionconfigurator",
    "alljoyn_pinglistener",
    "alljoyn_proxybusobject",
    "alljoyn_proxybusobject_ref",
    "alljoyn_securityapplicationproxy",
    "alljoyn_sessionlistener",
    "alljoyn_sessionopts",
    "alljoyn_sessionportlistener",
    "AllJoynConnectToBus",
    "AllJoynCloseBusHandle",
    "AllJoynSendToBus",
    "AllJoynReceiveFromBus",
    "AllJoynEventSelect",
    "AllJoynEnumEvents",
    "AllJoynCreateBus",
    "AllJoynAcceptBusConnection",
    "alljoyn_unity_deferred_callbacks_process",
    "alljoyn_unity_set_deferred_callback_mainthread_only",
    "QCC_StatusText",
    "alljoyn_msgarg_create",
    "alljoyn_msgarg_create_and_set",
    "alljoyn_msgarg_destroy",
    "alljoyn_msgarg_array_create",
    "alljoyn_msgarg_array_element",
    "alljoyn_msgarg_set",
    "alljoyn_msgarg_get",
    "alljoyn_msgarg_copy",
    "alljoyn_msgarg_clone",
    "alljoyn_msgarg_equal",
    "alljoyn_msgarg_array_set",
    "alljoyn_msgarg_array_get",
    "alljoyn_msgarg_tostring",
    "alljoyn_msgarg_array_tostring",
    "alljoyn_msgarg_signature",
    "alljoyn_msgarg_array_signature",
    "alljoyn_msgarg_hassignature",
    "alljoyn_msgarg_getdictelement",
    "alljoyn_msgarg_gettype",
    "alljoyn_msgarg_clear",
    "alljoyn_msgarg_stabilize",
    "alljoyn_msgarg_array_set_offset",
    "alljoyn_msgarg_set_and_stabilize",
    "alljoyn_msgarg_set_uint8",
    "alljoyn_msgarg_set_bool",
    "alljoyn_msgarg_set_int16",
    "alljoyn_msgarg_set_uint16",
    "alljoyn_msgarg_set_int32",
    "alljoyn_msgarg_set_uint32",
    "alljoyn_msgarg_set_int64",
    "alljoyn_msgarg_set_uint64",
    "alljoyn_msgarg_set_double",
    "alljoyn_msgarg_set_string",
    "alljoyn_msgarg_set_objectpath",
    "alljoyn_msgarg_set_signature",
    "alljoyn_msgarg_get_uint8",
    "alljoyn_msgarg_get_bool",
    "alljoyn_msgarg_get_int16",
    "alljoyn_msgarg_get_uint16",
    "alljoyn_msgarg_get_int32",
    "alljoyn_msgarg_get_uint32",
    "alljoyn_msgarg_get_int64",
    "alljoyn_msgarg_get_uint64",
    "alljoyn_msgarg_get_double",
    "alljoyn_msgarg_get_string",
    "alljoyn_msgarg_get_objectpath",
    "alljoyn_msgarg_get_signature",
    "alljoyn_msgarg_get_variant",
    "alljoyn_msgarg_set_uint8_array",
    "alljoyn_msgarg_set_bool_array",
    "alljoyn_msgarg_set_int16_array",
    "alljoyn_msgarg_set_uint16_array",
    "alljoyn_msgarg_set_int32_array",
    "alljoyn_msgarg_set_uint32_array",
    "alljoyn_msgarg_set_int64_array",
    "alljoyn_msgarg_set_uint64_array",
    "alljoyn_msgarg_set_double_array",
    "alljoyn_msgarg_set_string_array",
    "alljoyn_msgarg_set_objectpath_array",
    "alljoyn_msgarg_set_signature_array",
    "alljoyn_msgarg_get_uint8_array",
    "alljoyn_msgarg_get_bool_array",
    "alljoyn_msgarg_get_int16_array",
    "alljoyn_msgarg_get_uint16_array",
    "alljoyn_msgarg_get_int32_array",
    "alljoyn_msgarg_get_uint32_array",
    "alljoyn_msgarg_get_int64_array",
    "alljoyn_msgarg_get_uint64_array",
    "alljoyn_msgarg_get_double_array",
    "alljoyn_msgarg_get_variant_array",
    "alljoyn_msgarg_get_array_numberofelements",
    "alljoyn_msgarg_get_array_element",
    "alljoyn_msgarg_get_array_elementsignature",
    "alljoyn_msgarg_getkey",
    "alljoyn_msgarg_getvalue",
    "alljoyn_msgarg_setdictentry",
    "alljoyn_msgarg_setstruct",
    "alljoyn_msgarg_getnummembers",
    "alljoyn_msgarg_getmember",
    "alljoyn_aboutdata_create_empty",
    "alljoyn_aboutdata_create",
    "alljoyn_aboutdata_create_full",
    "alljoyn_aboutdata_destroy",
    "alljoyn_aboutdata_createfromxml",
    "alljoyn_aboutdata_isvalid",
    "alljoyn_aboutdata_createfrommsgarg",
    "alljoyn_aboutdata_setappid",
    "alljoyn_aboutdata_setappid_fromstring",
    "alljoyn_aboutdata_getappid",
    "alljoyn_aboutdata_setdefaultlanguage",
    "alljoyn_aboutdata_getdefaultlanguage",
    "alljoyn_aboutdata_setdevicename",
    "alljoyn_aboutdata_getdevicename",
    "alljoyn_aboutdata_setdeviceid",
    "alljoyn_aboutdata_getdeviceid",
    "alljoyn_aboutdata_setappname",
    "alljoyn_aboutdata_getappname",
    "alljoyn_aboutdata_setmanufacturer",
    "alljoyn_aboutdata_getmanufacturer",
    "alljoyn_aboutdata_setmodelnumber",
    "alljoyn_aboutdata_getmodelnumber",
    "alljoyn_aboutdata_setsupportedlanguage",
    "alljoyn_aboutdata_getsupportedlanguages",
    "alljoyn_aboutdata_setdescription",
    "alljoyn_aboutdata_getdescription",
    "alljoyn_aboutdata_setdateofmanufacture",
    "alljoyn_aboutdata_getdateofmanufacture",
    "alljoyn_aboutdata_setsoftwareversion",
    "alljoyn_aboutdata_getsoftwareversion",
    "alljoyn_aboutdata_getajsoftwareversion",
    "alljoyn_aboutdata_sethardwareversion",
    "alljoyn_aboutdata_gethardwareversion",
    "alljoyn_aboutdata_setsupporturl",
    "alljoyn_aboutdata_getsupporturl",
    "alljoyn_aboutdata_setfield",
    "alljoyn_aboutdata_getfield",
    "alljoyn_aboutdata_getfields",
    "alljoyn_aboutdata_getaboutdata",
    "alljoyn_aboutdata_getannouncedaboutdata",
    "alljoyn_aboutdata_isfieldrequired",
    "alljoyn_aboutdata_isfieldannounced",
    "alljoyn_aboutdata_isfieldlocalized",
    "alljoyn_aboutdata_getfieldsignature",
    "alljoyn_abouticon_create",
    "alljoyn_abouticon_destroy",
    "alljoyn_abouticon_getcontent",
    "alljoyn_abouticon_setcontent",
    "alljoyn_abouticon_geturl",
    "alljoyn_abouticon_seturl",
    "alljoyn_abouticon_clear",
    "alljoyn_abouticon_setcontent_frommsgarg",
    "alljoyn_permissionconfigurator_getdefaultclaimcapabilities",
    "alljoyn_permissionconfigurator_getapplicationstate",
    "alljoyn_permissionconfigurator_setapplicationstate",
    "alljoyn_permissionconfigurator_getpublickey",
    "alljoyn_permissionconfigurator_publickey_destroy",
    "alljoyn_permissionconfigurator_getmanifesttemplate",
    "alljoyn_permissionconfigurator_manifesttemplate_destroy",
    "alljoyn_permissionconfigurator_setmanifesttemplatefromxml",
    "alljoyn_permissionconfigurator_getclaimcapabilities",
    "alljoyn_permissionconfigurator_setclaimcapabilities",
    "alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo",
    "alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo",
    "alljoyn_permissionconfigurator_reset",
    "alljoyn_permissionconfigurator_claim",
    "alljoyn_permissionconfigurator_updateidentity",
    "alljoyn_permissionconfigurator_getidentity",
    "alljoyn_permissionconfigurator_certificatechain_destroy",
    "alljoyn_permissionconfigurator_getmanifests",
    "alljoyn_permissionconfigurator_manifestarray_cleanup",
    "alljoyn_permissionconfigurator_installmanifests",
    "alljoyn_permissionconfigurator_getidentitycertificateid",
    "alljoyn_permissionconfigurator_certificateid_cleanup",
    "alljoyn_permissionconfigurator_updatepolicy",
    "alljoyn_permissionconfigurator_getpolicy",
    "alljoyn_permissionconfigurator_getdefaultpolicy",
    "alljoyn_permissionconfigurator_policy_destroy",
    "alljoyn_permissionconfigurator_resetpolicy",
    "alljoyn_permissionconfigurator_getmembershipsummaries",
    "alljoyn_permissionconfigurator_certificateidarray_cleanup",
    "alljoyn_permissionconfigurator_installmembership",
    "alljoyn_permissionconfigurator_removemembership",
    "alljoyn_permissionconfigurator_startmanagement",
    "alljoyn_permissionconfigurator_endmanagement",
    "alljoyn_applicationstatelistener_create",
    "alljoyn_applicationstatelistener_destroy",
    "alljoyn_keystorelistener_create",
    "alljoyn_keystorelistener_with_synchronization_create",
    "alljoyn_keystorelistener_destroy",
    "alljoyn_keystorelistener_putkeys",
    "alljoyn_keystorelistener_getkeys",
    "alljoyn_sessionopts_create",
    "alljoyn_sessionopts_destroy",
    "alljoyn_sessionopts_get_traffic",
    "alljoyn_sessionopts_set_traffic",
    "alljoyn_sessionopts_get_multipoint",
    "alljoyn_sessionopts_set_multipoint",
    "alljoyn_sessionopts_get_proximity",
    "alljoyn_sessionopts_set_proximity",
    "alljoyn_sessionopts_get_transports",
    "alljoyn_sessionopts_set_transports",
    "alljoyn_sessionopts_iscompatible",
    "alljoyn_sessionopts_cmp",
    "alljoyn_message_create",
    "alljoyn_message_destroy",
    "alljoyn_message_isbroadcastsignal",
    "alljoyn_message_isglobalbroadcast",
    "alljoyn_message_issessionless",
    "alljoyn_message_getflags",
    "alljoyn_message_isexpired",
    "alljoyn_message_isunreliable",
    "alljoyn_message_isencrypted",
    "alljoyn_message_getauthmechanism",
    "alljoyn_message_gettype",
    "alljoyn_message_getargs",
    "alljoyn_message_getarg",
    "alljoyn_message_parseargs",
    "alljoyn_message_getcallserial",
    "alljoyn_message_getsignature",
    "alljoyn_message_getobjectpath",
    "alljoyn_message_getinterface",
    "alljoyn_message_getmembername",
    "alljoyn_message_getreplyserial",
    "alljoyn_message_getsender",
    "alljoyn_message_getreceiveendpointname",
    "alljoyn_message_getdestination",
    "alljoyn_message_getcompressiontoken",
    "alljoyn_message_getsessionid",
    "alljoyn_message_geterrorname",
    "alljoyn_message_tostring",
    "alljoyn_message_description",
    "alljoyn_message_gettimestamp",
    "alljoyn_message_eql",
    "alljoyn_message_setendianess",
    "alljoyn_authlistener_requestcredentialsresponse",
    "alljoyn_authlistener_verifycredentialsresponse",
    "alljoyn_authlistener_create",
    "alljoyn_authlistenerasync_create",
    "alljoyn_authlistener_destroy",
    "alljoyn_authlistenerasync_destroy",
    "alljoyn_authlistener_setsharedsecret",
    "alljoyn_credentials_create",
    "alljoyn_credentials_destroy",
    "alljoyn_credentials_isset",
    "alljoyn_credentials_setpassword",
    "alljoyn_credentials_setusername",
    "alljoyn_credentials_setcertchain",
    "alljoyn_credentials_setprivatekey",
    "alljoyn_credentials_setlogonentry",
    "alljoyn_credentials_setexpiration",
    "alljoyn_credentials_getpassword",
    "alljoyn_credentials_getusername",
    "alljoyn_credentials_getcertchain",
    "alljoyn_credentials_getprivateKey",
    "alljoyn_credentials_getlogonentry",
    "alljoyn_credentials_getexpiration",
    "alljoyn_credentials_clear",
    "alljoyn_buslistener_create",
    "alljoyn_buslistener_destroy",
    "alljoyn_interfacedescription_member_getannotationscount",
    "alljoyn_interfacedescription_member_getannotationatindex",
    "alljoyn_interfacedescription_member_getannotation",
    "alljoyn_interfacedescription_member_getargannotationscount",
    "alljoyn_interfacedescription_member_getargannotationatindex",
    "alljoyn_interfacedescription_member_getargannotation",
    "alljoyn_interfacedescription_property_getannotationscount",
    "alljoyn_interfacedescription_property_getannotationatindex",
    "alljoyn_interfacedescription_property_getannotation",
    "alljoyn_interfacedescription_activate",
    "alljoyn_interfacedescription_addannotation",
    "alljoyn_interfacedescription_getannotation",
    "alljoyn_interfacedescription_getannotationscount",
    "alljoyn_interfacedescription_getannotationatindex",
    "alljoyn_interfacedescription_getmember",
    "alljoyn_interfacedescription_addmember",
    "alljoyn_interfacedescription_addmemberannotation",
    "alljoyn_interfacedescription_getmemberannotation",
    "alljoyn_interfacedescription_getmembers",
    "alljoyn_interfacedescription_hasmember",
    "alljoyn_interfacedescription_addmethod",
    "alljoyn_interfacedescription_getmethod",
    "alljoyn_interfacedescription_addsignal",
    "alljoyn_interfacedescription_getsignal",
    "alljoyn_interfacedescription_getproperty",
    "alljoyn_interfacedescription_getproperties",
    "alljoyn_interfacedescription_addproperty",
    "alljoyn_interfacedescription_addpropertyannotation",
    "alljoyn_interfacedescription_getpropertyannotation",
    "alljoyn_interfacedescription_hasproperty",
    "alljoyn_interfacedescription_hasproperties",
    "alljoyn_interfacedescription_getname",
    "alljoyn_interfacedescription_introspect",
    "alljoyn_interfacedescription_issecure",
    "alljoyn_interfacedescription_getsecuritypolicy",
    "alljoyn_interfacedescription_setdescriptionlanguage",
    "alljoyn_interfacedescription_getdescriptionlanguages",
    "alljoyn_interfacedescription_getdescriptionlanguages2",
    "alljoyn_interfacedescription_setdescription",
    "alljoyn_interfacedescription_setdescriptionforlanguage",
    "alljoyn_interfacedescription_getdescriptionforlanguage",
    "alljoyn_interfacedescription_setmemberdescription",
    "alljoyn_interfacedescription_setmemberdescriptionforlanguage",
    "alljoyn_interfacedescription_getmemberdescriptionforlanguage",
    "alljoyn_interfacedescription_setargdescription",
    "alljoyn_interfacedescription_setargdescriptionforlanguage",
    "alljoyn_interfacedescription_getargdescriptionforlanguage",
    "alljoyn_interfacedescription_setpropertydescription",
    "alljoyn_interfacedescription_setpropertydescriptionforlanguage",
    "alljoyn_interfacedescription_getpropertydescriptionforlanguage",
    "alljoyn_interfacedescription_setdescriptiontranslationcallback",
    "alljoyn_interfacedescription_getdescriptiontranslationcallback",
    "alljoyn_interfacedescription_hasdescription",
    "alljoyn_interfacedescription_addargannotation",
    "alljoyn_interfacedescription_getmemberargannotation",
    "alljoyn_interfacedescription_eql",
    "alljoyn_interfacedescription_member_eql",
    "alljoyn_interfacedescription_property_eql",
    "alljoyn_busobject_create",
    "alljoyn_busobject_destroy",
    "alljoyn_busobject_getpath",
    "alljoyn_busobject_emitpropertychanged",
    "alljoyn_busobject_emitpropertieschanged",
    "alljoyn_busobject_getname",
    "alljoyn_busobject_addinterface",
    "alljoyn_busobject_addmethodhandler",
    "alljoyn_busobject_addmethodhandlers",
    "alljoyn_busobject_methodreply_args",
    "alljoyn_busobject_methodreply_err",
    "alljoyn_busobject_methodreply_status",
    "alljoyn_busobject_getbusattachment",
    "alljoyn_busobject_signal",
    "alljoyn_busobject_cancelsessionlessmessage_serial",
    "alljoyn_busobject_cancelsessionlessmessage",
    "alljoyn_busobject_issecure",
    "alljoyn_busobject_getannouncedinterfacenames",
    "alljoyn_busobject_setannounceflag",
    "alljoyn_busobject_addinterface_announced",
    "alljoyn_proxybusobject_create",
    "alljoyn_proxybusobject_create_secure",
    "alljoyn_proxybusobject_destroy",
    "alljoyn_proxybusobject_addinterface",
    "alljoyn_proxybusobject_addinterface_by_name",
    "alljoyn_proxybusobject_getchildren",
    "alljoyn_proxybusobject_getchild",
    "alljoyn_proxybusobject_addchild",
    "alljoyn_proxybusobject_removechild",
    "alljoyn_proxybusobject_introspectremoteobject",
    "alljoyn_proxybusobject_introspectremoteobjectasync",
    "alljoyn_proxybusobject_getproperty",
    "alljoyn_proxybusobject_getpropertyasync",
    "alljoyn_proxybusobject_getallproperties",
    "alljoyn_proxybusobject_getallpropertiesasync",
    "alljoyn_proxybusobject_setproperty",
    "alljoyn_proxybusobject_registerpropertieschangedlistener",
    "alljoyn_proxybusobject_unregisterpropertieschangedlistener",
    "alljoyn_proxybusobject_setpropertyasync",
    "alljoyn_proxybusobject_methodcall",
    "alljoyn_proxybusobject_methodcall_member",
    "alljoyn_proxybusobject_methodcall_noreply",
    "alljoyn_proxybusobject_methodcall_member_noreply",
    "alljoyn_proxybusobject_methodcallasync",
    "alljoyn_proxybusobject_methodcallasync_member",
    "alljoyn_proxybusobject_parsexml",
    "alljoyn_proxybusobject_secureconnection",
    "alljoyn_proxybusobject_secureconnectionasync",
    "alljoyn_proxybusobject_getinterface",
    "alljoyn_proxybusobject_getinterfaces",
    "alljoyn_proxybusobject_getpath",
    "alljoyn_proxybusobject_getservicename",
    "alljoyn_proxybusobject_getuniquename",
    "alljoyn_proxybusobject_getsessionid",
    "alljoyn_proxybusobject_implementsinterface",
    "alljoyn_proxybusobject_copy",
    "alljoyn_proxybusobject_isvalid",
    "alljoyn_proxybusobject_issecure",
    "alljoyn_proxybusobject_enablepropertycaching",
    "alljoyn_permissionconfigurationlistener_create",
    "alljoyn_permissionconfigurationlistener_destroy",
    "alljoyn_sessionlistener_create",
    "alljoyn_sessionlistener_destroy",
    "alljoyn_sessionportlistener_create",
    "alljoyn_sessionportlistener_destroy",
    "alljoyn_aboutlistener_create",
    "alljoyn_aboutlistener_destroy",
    "alljoyn_busattachment_create",
    "alljoyn_busattachment_create_concurrency",
    "alljoyn_busattachment_destroy",
    "alljoyn_busattachment_start",
    "alljoyn_busattachment_stop",
    "alljoyn_busattachment_join",
    "alljoyn_busattachment_getconcurrency",
    "alljoyn_busattachment_getconnectspec",
    "alljoyn_busattachment_enableconcurrentcallbacks",
    "alljoyn_busattachment_createinterface",
    "alljoyn_busattachment_createinterface_secure",
    "alljoyn_busattachment_connect",
    "alljoyn_busattachment_registerbuslistener",
    "alljoyn_busattachment_unregisterbuslistener",
    "alljoyn_busattachment_findadvertisedname",
    "alljoyn_busattachment_findadvertisednamebytransport",
    "alljoyn_busattachment_cancelfindadvertisedname",
    "alljoyn_busattachment_cancelfindadvertisednamebytransport",
    "alljoyn_busattachment_advertisename",
    "alljoyn_busattachment_canceladvertisename",
    "alljoyn_busattachment_getinterface",
    "alljoyn_busattachment_joinsession",
    "alljoyn_busattachment_joinsessionasync",
    "alljoyn_busattachment_registerbusobject",
    "alljoyn_busattachment_registerbusobject_secure",
    "alljoyn_busattachment_unregisterbusobject",
    "alljoyn_busattachment_requestname",
    "alljoyn_busattachment_releasename",
    "alljoyn_busattachment_bindsessionport",
    "alljoyn_busattachment_unbindsessionport",
    "alljoyn_busattachment_enablepeersecurity",
    "alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener",
    "alljoyn_busattachment_ispeersecurityenabled",
    "alljoyn_busattachment_createinterfacesfromxml",
    "alljoyn_busattachment_getinterfaces",
    "alljoyn_busattachment_deleteinterface",
    "alljoyn_busattachment_isstarted",
    "alljoyn_busattachment_isstopping",
    "alljoyn_busattachment_isconnected",
    "alljoyn_busattachment_disconnect",
    "alljoyn_busattachment_getdbusproxyobj",
    "alljoyn_busattachment_getalljoynproxyobj",
    "alljoyn_busattachment_getalljoyndebugobj",
    "alljoyn_busattachment_getuniquename",
    "alljoyn_busattachment_getglobalguidstring",
    "alljoyn_busattachment_registersignalhandler",
    "alljoyn_busattachment_registersignalhandlerwithrule",
    "alljoyn_busattachment_unregistersignalhandler",
    "alljoyn_busattachment_unregistersignalhandlerwithrule",
    "alljoyn_busattachment_unregisterallhandlers",
    "alljoyn_busattachment_registerkeystorelistener",
    "alljoyn_busattachment_reloadkeystore",
    "alljoyn_busattachment_clearkeystore",
    "alljoyn_busattachment_clearkeys",
    "alljoyn_busattachment_setkeyexpiration",
    "alljoyn_busattachment_getkeyexpiration",
    "alljoyn_busattachment_addlogonentry",
    "alljoyn_busattachment_addmatch",
    "alljoyn_busattachment_removematch",
    "alljoyn_busattachment_setsessionlistener",
    "alljoyn_busattachment_leavesession",
    "alljoyn_busattachment_secureconnection",
    "alljoyn_busattachment_secureconnectionasync",
    "alljoyn_busattachment_removesessionmember",
    "alljoyn_busattachment_setlinktimeout",
    "alljoyn_busattachment_setlinktimeoutasync",
    "alljoyn_busattachment_namehasowner",
    "alljoyn_busattachment_getpeerguid",
    "alljoyn_busattachment_setdaemondebug",
    "alljoyn_busattachment_gettimestamp",
    "alljoyn_busattachment_ping",
    "alljoyn_busattachment_registeraboutlistener",
    "alljoyn_busattachment_unregisteraboutlistener",
    "alljoyn_busattachment_unregisterallaboutlisteners",
    "alljoyn_busattachment_whoimplements_interfaces",
    "alljoyn_busattachment_whoimplements_interface",
    "alljoyn_busattachment_cancelwhoimplements_interfaces",
    "alljoyn_busattachment_cancelwhoimplements_interface",
    "alljoyn_busattachment_getpermissionconfigurator",
    "alljoyn_busattachment_registerapplicationstatelistener",
    "alljoyn_busattachment_unregisterapplicationstatelistener",
    "alljoyn_busattachment_deletedefaultkeystore",
    "alljoyn_abouticonobj_create",
    "alljoyn_abouticonobj_destroy",
    "alljoyn_abouticonproxy_create",
    "alljoyn_abouticonproxy_destroy",
    "alljoyn_abouticonproxy_geticon",
    "alljoyn_abouticonproxy_getversion",
    "alljoyn_aboutdatalistener_create",
    "alljoyn_aboutdatalistener_destroy",
    "alljoyn_aboutobj_create",
    "alljoyn_aboutobj_destroy",
    "alljoyn_aboutobj_announce",
    "alljoyn_aboutobj_announce_using_datalistener",
    "alljoyn_aboutobj_unannounce",
    "alljoyn_aboutobjectdescription_create",
    "alljoyn_aboutobjectdescription_create_full",
    "alljoyn_aboutobjectdescription_createfrommsgarg",
    "alljoyn_aboutobjectdescription_destroy",
    "alljoyn_aboutobjectdescription_getpaths",
    "alljoyn_aboutobjectdescription_getinterfaces",
    "alljoyn_aboutobjectdescription_getinterfacepaths",
    "alljoyn_aboutobjectdescription_clear",
    "alljoyn_aboutobjectdescription_haspath",
    "alljoyn_aboutobjectdescription_hasinterface",
    "alljoyn_aboutobjectdescription_hasinterfaceatpath",
    "alljoyn_aboutobjectdescription_getmsgarg",
    "alljoyn_aboutproxy_create",
    "alljoyn_aboutproxy_destroy",
    "alljoyn_aboutproxy_getobjectdescription",
    "alljoyn_aboutproxy_getaboutdata",
    "alljoyn_aboutproxy_getversion",
    "alljoyn_pinglistener_create",
    "alljoyn_pinglistener_destroy",
    "alljoyn_autopinger_create",
    "alljoyn_autopinger_destroy",
    "alljoyn_autopinger_pause",
    "alljoyn_autopinger_resume",
    "alljoyn_autopinger_addpinggroup",
    "alljoyn_autopinger_removepinggroup",
    "alljoyn_autopinger_setpinginterval",
    "alljoyn_autopinger_adddestination",
    "alljoyn_autopinger_removedestination",
    "alljoyn_getversion",
    "alljoyn_getbuildinfo",
    "alljoyn_getnumericversion",
    "alljoyn_init",
    "alljoyn_shutdown",
    "alljoyn_routerinit",
    "alljoyn_routerinitwithconfig",
    "alljoyn_routershutdown",
    "alljoyn_proxybusobject_ref_create",
    "alljoyn_proxybusobject_ref_get",
    "alljoyn_proxybusobject_ref_incref",
    "alljoyn_proxybusobject_ref_decref",
    "alljoyn_observerlistener_create",
    "alljoyn_observerlistener_destroy",
    "alljoyn_observer_create",
    "alljoyn_observer_destroy",
    "alljoyn_observer_registerlistener",
    "alljoyn_observer_unregisterlistener",
    "alljoyn_observer_unregisteralllisteners",
    "alljoyn_observer_get",
    "alljoyn_observer_getfirst",
    "alljoyn_observer_getnext",
    "alljoyn_passwordmanager_setcredentials",
    "alljoyn_securityapplicationproxy_getpermissionmanagementsessionport",
    "alljoyn_securityapplicationproxy_create",
    "alljoyn_securityapplicationproxy_destroy",
    "alljoyn_securityapplicationproxy_claim",
    "alljoyn_securityapplicationproxy_getmanifesttemplate",
    "alljoyn_securityapplicationproxy_manifesttemplate_destroy",
    "alljoyn_securityapplicationproxy_getapplicationstate",
    "alljoyn_securityapplicationproxy_getclaimcapabilities",
    "alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo",
    "alljoyn_securityapplicationproxy_getpolicy",
    "alljoyn_securityapplicationproxy_getdefaultpolicy",
    "alljoyn_securityapplicationproxy_policy_destroy",
    "alljoyn_securityapplicationproxy_updatepolicy",
    "alljoyn_securityapplicationproxy_updateidentity",
    "alljoyn_securityapplicationproxy_installmembership",
    "alljoyn_securityapplicationproxy_reset",
    "alljoyn_securityapplicationproxy_resetpolicy",
    "alljoyn_securityapplicationproxy_startmanagement",
    "alljoyn_securityapplicationproxy_endmanagement",
    "alljoyn_securityapplicationproxy_geteccpublickey",
    "alljoyn_securityapplicationproxy_eccpublickey_destroy",
    "alljoyn_securityapplicationproxy_signmanifest",
    "alljoyn_securityapplicationproxy_manifest_destroy",
    "alljoyn_securityapplicationproxy_computemanifestdigest",
    "alljoyn_securityapplicationproxy_digest_destroy",
    "alljoyn_securityapplicationproxy_setmanifestsignature",
]
