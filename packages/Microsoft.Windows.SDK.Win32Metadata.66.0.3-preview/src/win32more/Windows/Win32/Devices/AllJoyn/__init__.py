from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Devices.AllJoyn
import win32more.Windows.Win32.Foundation
QCC_TRUE: UInt32 = 1
QCC_FALSE: UInt32 = 0
ALLJOYN_MESSAGE_FLAG_NO_REPLY_EXPECTED: UInt32 = 1
ALLJOYN_MESSAGE_FLAG_AUTO_START: UInt32 = 2
ALLJOYN_MESSAGE_FLAG_ALLOW_REMOTE_MSG: UInt32 = 4
ALLJOYN_MESSAGE_FLAG_SESSIONLESS: UInt32 = 16
ALLJOYN_MESSAGE_FLAG_GLOBAL_BROADCAST: UInt32 = 32
ALLJOYN_MESSAGE_FLAG_ENCRYPTED: UInt32 = 128
ALLJOYN_TRAFFIC_TYPE_MESSAGES: UInt32 = 1
ALLJOYN_TRAFFIC_TYPE_RAW_UNRELIABLE: UInt32 = 2
ALLJOYN_TRAFFIC_TYPE_RAW_RELIABLE: UInt32 = 4
ALLJOYN_PROXIMITY_ANY: UInt32 = 255
ALLJOYN_PROXIMITY_PHYSICAL: UInt32 = 1
ALLJOYN_PROXIMITY_NETWORK: UInt32 = 2
ALLJOYN_NAMED_PIPE_CONNECT_SPEC: String = 'npipe:'
ALLJOYN_READ_READY: UInt32 = 1
ALLJOYN_WRITE_READY: UInt32 = 2
ALLJOYN_DISCONNECTED: UInt32 = 4
ALLJOYN_LITTLE_ENDIAN: Byte = 108
ALLJOYN_BIG_ENDIAN: Byte = 66
ALLJOYN_MESSAGE_DEFAULT_TIMEOUT: UInt32 = 25000
ALLJOYN_CRED_PASSWORD: UInt16 = 1
ALLJOYN_CRED_USER_NAME: UInt16 = 2
ALLJOYN_CRED_CERT_CHAIN: UInt16 = 4
ALLJOYN_CRED_PRIVATE_KEY: UInt16 = 8
ALLJOYN_CRED_LOGON_ENTRY: UInt16 = 16
ALLJOYN_CRED_EXPIRATION: UInt16 = 32
ALLJOYN_CRED_NEW_PASSWORD: UInt16 = 4097
ALLJOYN_CRED_ONE_TIME_PWD: UInt16 = 8193
ALLJOYN_PROP_ACCESS_READ: Byte = 1
ALLJOYN_PROP_ACCESS_WRITE: Byte = 2
ALLJOYN_PROP_ACCESS_RW: Byte = 3
ALLJOYN_MEMBER_ANNOTATE_NO_REPLY: Byte = 1
ALLJOYN_MEMBER_ANNOTATE_DEPRECATED: Byte = 2
ALLJOYN_MEMBER_ANNOTATE_SESSIONCAST: Byte = 4
ALLJOYN_MEMBER_ANNOTATE_SESSIONLESS: Byte = 8
ALLJOYN_MEMBER_ANNOTATE_UNICAST: Byte = 16
ALLJOYN_MEMBER_ANNOTATE_GLOBAL_BROADCAST: Byte = 32
QStatus = Int32
ER_OK: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 0
ER_FAIL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 1
ER_UTF_CONVERSION_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 2
ER_BUFFER_TOO_SMALL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 3
ER_OS_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4
ER_OUT_OF_MEMORY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 5
ER_SOCKET_BIND_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 6
ER_INIT_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 7
ER_WOULDBLOCK: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8
ER_NOT_IMPLEMENTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 9
ER_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 10
ER_SOCK_OTHER_END_CLOSED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 11
ER_BAD_ARG_1: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 12
ER_BAD_ARG_2: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 13
ER_BAD_ARG_3: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 14
ER_BAD_ARG_4: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 15
ER_BAD_ARG_5: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 16
ER_BAD_ARG_6: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 17
ER_BAD_ARG_7: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 18
ER_BAD_ARG_8: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 19
ER_INVALID_ADDRESS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 20
ER_INVALID_DATA: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 21
ER_READ_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 22
ER_WRITE_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 23
ER_OPEN_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 24
ER_PARSE_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 25
ER_END_OF_DATA: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 26
ER_CONN_REFUSED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 27
ER_BAD_ARG_COUNT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 28
ER_WARNING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 29
ER_EOF: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 30
ER_DEADLOCK: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 31
ER_COMMON_ERRORS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4096
ER_STOPPING_THREAD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4097
ER_ALERTED_THREAD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4098
ER_XML_MALFORMED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4099
ER_AUTH_FAIL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4100
ER_AUTH_USER_REJECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4101
ER_NO_SUCH_ALARM: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4102
ER_TIMER_FALLBEHIND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4103
ER_SSL_ERRORS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4104
ER_SSL_INIT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4105
ER_SSL_CONNECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4106
ER_SSL_VERIFY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4107
ER_EXTERNAL_THREAD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4108
ER_CRYPTO_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4109
ER_CRYPTO_TRUNCATED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4110
ER_CRYPTO_KEY_UNAVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4111
ER_BAD_HOSTNAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4112
ER_CRYPTO_KEY_UNUSABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4113
ER_EMPTY_KEY_BLOB: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4114
ER_CORRUPT_KEYBLOB: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4115
ER_INVALID_KEY_ENCODING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4116
ER_DEAD_THREAD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4117
ER_THREAD_RUNNING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4118
ER_THREAD_STOPPING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4119
ER_BAD_STRING_ENCODING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4120
ER_CRYPTO_INSUFFICIENT_SECURITY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4121
ER_CRYPTO_ILLEGAL_PARAMETERS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4122
ER_CRYPTO_HASH_UNINITIALIZED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4123
ER_THREAD_NO_WAIT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4124
ER_TIMER_EXITING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4125
ER_INVALID_GUID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4126
ER_THREADPOOL_EXHAUSTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4127
ER_THREADPOOL_STOPPING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4128
ER_INVALID_STREAM: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4129
ER_TIMER_FULL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4130
ER_IODISPATCH_STOPPING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4131
ER_SLAP_INVALID_PACKET_LEN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4132
ER_SLAP_HDR_CHECKSUM_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4133
ER_SLAP_INVALID_PACKET_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4134
ER_SLAP_LEN_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4135
ER_SLAP_PACKET_TYPE_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4136
ER_SLAP_CRC_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4137
ER_SLAP_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4138
ER_SLAP_OTHER_END_CLOSED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4139
ER_TIMER_NOT_ALLOWED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4140
ER_NOT_CONN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 4141
ER_XML_CONVERTER_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8192
ER_XML_INVALID_RULES_COUNT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8193
ER_XML_INTERFACE_MEMBERS_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8194
ER_XML_INVALID_MEMBER_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8195
ER_XML_INVALID_MEMBER_ACTION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8196
ER_XML_MEMBER_DENY_ACTION_WITH_OTHER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8197
ER_XML_INVALID_ANNOTATIONS_COUNT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8198
ER_XML_INVALID_ELEMENT_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8199
ER_XML_INVALID_ATTRIBUTE_VALUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8200
ER_XML_INVALID_SECURITY_LEVEL_ANNOTATION_VALUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8201
ER_XML_INVALID_ELEMENT_CHILDREN_COUNT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8202
ER_XML_INVALID_POLICY_VERSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8203
ER_XML_INVALID_POLICY_SERIAL_NUMBER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8204
ER_XML_INVALID_ACL_PEER_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8205
ER_XML_INVALID_ACL_PEER_CHILDREN_COUNT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8206
ER_XML_ACL_ALL_TYPE_PEER_WITH_OTHERS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8207
ER_XML_INVALID_ACL_PEER_PUBLIC_KEY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8208
ER_XML_ACL_PEER_NOT_UNIQUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8209
ER_XML_ACL_PEER_PUBLIC_KEY_SET: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8210
ER_XML_ACLS_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8211
ER_XML_ACL_PEERS_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8212
ER_XML_INVALID_OBJECT_PATH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8213
ER_XML_INVALID_INTERFACE_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8214
ER_XML_INVALID_MEMBER_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8215
ER_XML_INVALID_MANIFEST_VERSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8216
ER_XML_INVALID_OID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8217
ER_XML_INVALID_BASE64: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8218
ER_XML_INTERFACE_NAME_NOT_UNIQUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8219
ER_XML_MEMBER_NAME_NOT_UNIQUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8220
ER_XML_OBJECT_PATH_NOT_UNIQUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8221
ER_XML_ANNOTATION_NOT_UNIQUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 8222
ER_NONE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 65535
ER_BUS_ERRORS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36864
ER_BUS_READ_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36865
ER_BUS_WRITE_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36866
ER_BUS_BAD_VALUE_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36867
ER_BUS_BAD_HEADER_FIELD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36868
ER_BUS_BAD_SIGNATURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36869
ER_BUS_BAD_OBJ_PATH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36870
ER_BUS_BAD_MEMBER_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36871
ER_BUS_BAD_INTERFACE_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36872
ER_BUS_BAD_ERROR_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36873
ER_BUS_BAD_BUS_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36874
ER_BUS_NAME_TOO_LONG: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36875
ER_BUS_BAD_LENGTH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36876
ER_BUS_BAD_VALUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36877
ER_BUS_BAD_HDR_FLAGS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36878
ER_BUS_BAD_BODY_LEN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36879
ER_BUS_BAD_HEADER_LEN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36880
ER_BUS_UNKNOWN_SERIAL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36881
ER_BUS_UNKNOWN_PATH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36882
ER_BUS_UNKNOWN_INTERFACE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36883
ER_BUS_ESTABLISH_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36884
ER_BUS_UNEXPECTED_SIGNATURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36885
ER_BUS_INTERFACE_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36886
ER_BUS_PATH_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36887
ER_BUS_MEMBER_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36888
ER_BUS_REPLY_SERIAL_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36889
ER_BUS_ERROR_NAME_MISSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36890
ER_BUS_INTERFACE_NO_SUCH_MEMBER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36891
ER_BUS_NO_SUCH_OBJECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36892
ER_BUS_OBJECT_NO_SUCH_MEMBER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36893
ER_BUS_OBJECT_NO_SUCH_INTERFACE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36894
ER_BUS_NO_SUCH_INTERFACE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36895
ER_BUS_MEMBER_NO_SUCH_SIGNATURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36896
ER_BUS_NOT_NUL_TERMINATED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36897
ER_BUS_NO_SUCH_PROPERTY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36898
ER_BUS_SET_WRONG_SIGNATURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36899
ER_BUS_PROPERTY_VALUE_NOT_SET: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36900
ER_BUS_PROPERTY_ACCESS_DENIED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36901
ER_BUS_NO_TRANSPORTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36902
ER_BUS_BAD_TRANSPORT_ARGS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36903
ER_BUS_NO_ROUTE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36904
ER_BUS_NO_ENDPOINT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36905
ER_BUS_BAD_SEND_PARAMETER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36906
ER_BUS_UNMATCHED_REPLY_SERIAL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36907
ER_BUS_BAD_SENDER_ID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36908
ER_BUS_TRANSPORT_NOT_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36909
ER_BUS_EMPTY_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36910
ER_BUS_NOT_OWNER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36911
ER_BUS_SET_PROPERTY_REJECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36912
ER_BUS_CONNECT_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36913
ER_BUS_REPLY_IS_ERROR_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36914
ER_BUS_NOT_AUTHENTICATING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36915
ER_BUS_NO_LISTENER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36916
ER_BUS_NOT_ALLOWED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36918
ER_BUS_WRITE_QUEUE_FULL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36919
ER_BUS_ENDPOINT_CLOSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36920
ER_BUS_INTERFACE_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36921
ER_BUS_MEMBER_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36922
ER_BUS_PROPERTY_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36923
ER_BUS_IFACE_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36924
ER_BUS_ERROR_RESPONSE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36925
ER_BUS_BAD_XML: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36926
ER_BUS_BAD_CHILD_PATH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36927
ER_BUS_OBJ_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36928
ER_BUS_OBJ_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36929
ER_BUS_CANNOT_EXPAND_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36930
ER_BUS_NOT_COMPRESSED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36931
ER_BUS_ALREADY_CONNECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36932
ER_BUS_NOT_CONNECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36933
ER_BUS_ALREADY_LISTENING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36934
ER_BUS_KEY_UNAVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36935
ER_BUS_TRUNCATED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36936
ER_BUS_KEY_STORE_NOT_LOADED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36937
ER_BUS_NO_AUTHENTICATION_MECHANISM: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36938
ER_BUS_BUS_ALREADY_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36939
ER_BUS_BUS_NOT_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36940
ER_BUS_KEYBLOB_OP_INVALID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36941
ER_BUS_INVALID_HEADER_CHECKSUM: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36942
ER_BUS_MESSAGE_NOT_ENCRYPTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36943
ER_BUS_INVALID_HEADER_SERIAL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36944
ER_BUS_TIME_TO_LIVE_EXPIRED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36945
ER_BUS_HDR_EXPANSION_INVALID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36946
ER_BUS_MISSING_COMPRESSION_TOKEN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36947
ER_BUS_NO_PEER_GUID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36948
ER_BUS_MESSAGE_DECRYPTION_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36949
ER_BUS_SECURITY_FATAL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36950
ER_BUS_KEY_EXPIRED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36951
ER_BUS_CORRUPT_KEYSTORE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36952
ER_BUS_NO_CALL_FOR_REPLY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36953
ER_BUS_NOT_A_COMPLETE_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36954
ER_BUS_POLICY_VIOLATION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36955
ER_BUS_NO_SUCH_SERVICE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36956
ER_BUS_TRANSPORT_NOT_AVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36957
ER_BUS_INVALID_AUTH_MECHANISM: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36958
ER_BUS_KEYSTORE_VERSION_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36959
ER_BUS_BLOCKING_CALL_NOT_ALLOWED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36960
ER_BUS_SIGNATURE_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36961
ER_BUS_STOPPING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36962
ER_BUS_METHOD_CALL_ABORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36963
ER_BUS_CANNOT_ADD_INTERFACE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36964
ER_BUS_CANNOT_ADD_HANDLER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36965
ER_BUS_KEYSTORE_NOT_LOADED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36966
ER_BUS_NO_SUCH_HANDLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36971
ER_BUS_HANDLES_NOT_ENABLED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36972
ER_BUS_HANDLES_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36973
ER_BUS_NO_SESSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36975
ER_BUS_ELEMENT_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36976
ER_BUS_NOT_A_DICTIONARY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36977
ER_BUS_WAIT_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36978
ER_BUS_BAD_SESSION_OPTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36980
ER_BUS_CONNECTION_REJECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36981
ER_DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36982
ER_DBUS_REQUEST_NAME_REPLY_IN_QUEUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36983
ER_DBUS_REQUEST_NAME_REPLY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36984
ER_DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36985
ER_DBUS_RELEASE_NAME_REPLY_RELEASED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36986
ER_DBUS_RELEASE_NAME_REPLY_NON_EXISTENT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36987
ER_DBUS_RELEASE_NAME_REPLY_NOT_OWNER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36988
ER_DBUS_START_REPLY_ALREADY_RUNNING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36990
ER_ALLJOYN_BINDSESSIONPORT_REPLY_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36992
ER_ALLJOYN_BINDSESSIONPORT_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36993
ER_ALLJOYN_JOINSESSION_REPLY_NO_SESSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36995
ER_ALLJOYN_JOINSESSION_REPLY_UNREACHABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36996
ER_ALLJOYN_JOINSESSION_REPLY_CONNECT_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36997
ER_ALLJOYN_JOINSESSION_REPLY_REJECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36998
ER_ALLJOYN_JOINSESSION_REPLY_BAD_SESSION_OPTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 36999
ER_ALLJOYN_JOINSESSION_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37000
ER_ALLJOYN_LEAVESESSION_REPLY_NO_SESSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37002
ER_ALLJOYN_LEAVESESSION_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37003
ER_ALLJOYN_ADVERTISENAME_REPLY_TRANSPORT_NOT_AVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37004
ER_ALLJOYN_ADVERTISENAME_REPLY_ALREADY_ADVERTISING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37005
ER_ALLJOYN_ADVERTISENAME_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37006
ER_ALLJOYN_CANCELADVERTISENAME_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37008
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_TRANSPORT_NOT_AVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37009
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_ALREADY_DISCOVERING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37010
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37011
ER_ALLJOYN_CANCELFINDADVERTISEDNAME_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37013
ER_BUS_UNEXPECTED_DISPOSITION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37014
ER_BUS_INTERFACE_ACTIVATED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37015
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_BAD_PORT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37016
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37017
ER_ALLJOYN_BINDSESSIONPORT_REPLY_INVALID_OPTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37018
ER_ALLJOYN_JOINSESSION_REPLY_ALREADY_JOINED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37019
ER_BUS_SELF_CONNECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37020
ER_BUS_SECURITY_NOT_ENABLED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37021
ER_BUS_LISTENER_ALREADY_SET: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37022
ER_BUS_PEER_AUTH_VERSION_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37023
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NOT_SUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37024
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NO_DEST_SUPPORT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37025
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37026
ER_ALLJOYN_ACCESS_PERMISSION_WARNING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37027
ER_ALLJOYN_ACCESS_PERMISSION_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37028
ER_BUS_DESTINATION_NOT_AUTHENTICATED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37029
ER_BUS_ENDPOINT_REDIRECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37030
ER_BUS_AUTHENTICATION_PENDING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37031
ER_BUS_NOT_AUTHORIZED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37032
ER_PACKET_BUS_NO_SUCH_CHANNEL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37033
ER_PACKET_BAD_FORMAT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37034
ER_PACKET_CONNECT_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37035
ER_PACKET_CHANNEL_FAIL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37036
ER_PACKET_TOO_LARGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37037
ER_PACKET_BAD_PARAMETER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37038
ER_PACKET_BAD_CRC: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37039
ER_RENDEZVOUS_SERVER_DEACTIVATED_USER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37067
ER_RENDEZVOUS_SERVER_UNKNOWN_USER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37068
ER_UNABLE_TO_CONNECT_TO_RENDEZVOUS_SERVER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37069
ER_NOT_CONNECTED_TO_RENDEZVOUS_SERVER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37070
ER_UNABLE_TO_SEND_MESSAGE_TO_RENDEZVOUS_SERVER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37071
ER_INVALID_RENDEZVOUS_SERVER_INTERFACE_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37072
ER_INVALID_PERSISTENT_CONNECTION_MESSAGE_RESPONSE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37073
ER_INVALID_ON_DEMAND_CONNECTION_MESSAGE_RESPONSE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37074
ER_INVALID_HTTP_METHOD_USED_FOR_RENDEZVOUS_SERVER_INTERFACE_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37075
ER_RENDEZVOUS_SERVER_ERR500_INTERNAL_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37076
ER_RENDEZVOUS_SERVER_ERR503_STATUS_UNAVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37077
ER_RENDEZVOUS_SERVER_ERR401_UNAUTHORIZED_REQUEST: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37078
ER_RENDEZVOUS_SERVER_UNRECOVERABLE_ERROR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37079
ER_RENDEZVOUS_SERVER_ROOT_CERTIFICATE_UNINITIALIZED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37080
ER_BUS_NO_SUCH_ANNOTATION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37081
ER_BUS_ANNOTATION_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37082
ER_SOCK_CLOSING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37083
ER_NO_SUCH_DEVICE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37084
ER_P2P: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37085
ER_P2P_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37086
ER_P2P_NOT_CONNECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37087
ER_BAD_TRANSPORT_MASK: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37088
ER_PROXIMITY_CONNECTION_ESTABLISH_FAIL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37089
ER_PROXIMITY_NO_PEERS_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37090
ER_BUS_OBJECT_NOT_REGISTERED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37091
ER_P2P_DISABLED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37092
ER_P2P_BUSY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37093
ER_BUS_INCOMPATIBLE_DAEMON: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37094
ER_P2P_NO_GO: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37095
ER_P2P_NO_STA: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37096
ER_P2P_FORBIDDEN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37097
ER_ALLJOYN_ONAPPSUSPEND_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37098
ER_ALLJOYN_ONAPPSUSPEND_REPLY_UNSUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37099
ER_ALLJOYN_ONAPPRESUME_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37100
ER_ALLJOYN_ONAPPRESUME_REPLY_UNSUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37101
ER_BUS_NO_SUCH_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37102
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_NO_SESSION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37103
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_BINDER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37104
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_MULTIPOINT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37105
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37106
ER_ALLJOYN_REMOVESESSIONMEMBER_INCOMPATIBLE_REMOTE_DAEMON: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37107
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37108
ER_BUS_REMOVED_BY_BINDER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37109
ER_BUS_MATCH_RULE_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37110
ER_ALLJOYN_PING_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37111
ER_ALLJOYN_PING_REPLY_UNREACHABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37112
ER_UDP_MSG_TOO_LONG: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37113
ER_UDP_DEMUX_NO_ENDPOINT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37114
ER_UDP_NO_NETWORK: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37115
ER_UDP_UNEXPECTED_LENGTH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37116
ER_UDP_UNEXPECTED_FLOW: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37117
ER_UDP_DISCONNECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37118
ER_UDP_NOT_IMPLEMENTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37119
ER_UDP_NO_LISTENER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37120
ER_UDP_STOPPING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37121
ER_ARDP_BACKPRESSURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37122
ER_UDP_BACKPRESSURE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37123
ER_ARDP_INVALID_STATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37124
ER_ARDP_TTL_EXPIRED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37125
ER_ARDP_PERSIST_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37126
ER_ARDP_PROBE_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37127
ER_ARDP_REMOTE_CONNECTION_RESET: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37128
ER_UDP_BUSHELLO: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37129
ER_UDP_MESSAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37130
ER_UDP_INVALID: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37131
ER_UDP_UNSUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37132
ER_UDP_ENDPOINT_STALLED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37133
ER_ARDP_INVALID_RESPONSE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37134
ER_ARDP_INVALID_CONNECTION: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37135
ER_UDP_LOCAL_DISCONNECT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37136
ER_UDP_EARLY_EXIT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37137
ER_UDP_LOCAL_DISCONNECT_FAIL: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37138
ER_ARDP_DISCONNECTING: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37139
ER_ALLJOYN_PING_REPLY_INCOMPATIBLE_REMOTE_ROUTING_NODE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37140
ER_ALLJOYN_PING_REPLY_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37141
ER_ALLJOYN_PING_REPLY_UNKNOWN_NAME: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37142
ER_ALLJOYN_PING_REPLY_FAILED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37143
ER_TCP_MAX_UNTRUSTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37144
ER_ALLJOYN_PING_REPLY_IN_PROGRESS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37145
ER_LANGUAGE_NOT_SUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37146
ER_ABOUT_FIELD_ALREADY_SPECIFIED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37147
ER_UDP_NOT_DISCONNECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37148
ER_UDP_ENDPOINT_NOT_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37149
ER_UDP_ENDPOINT_REMOVED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37150
ER_ARDP_VERSION_NOT_SUPPORTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37151
ER_CONNECTION_LIMIT_EXCEEDED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37152
ER_ARDP_WRITE_BLOCKED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37153
ER_PERMISSION_DENIED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37154
ER_ABOUT_DEFAULT_LANGUAGE_NOT_SPECIFIED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37155
ER_ABOUT_SESSIONPORT_NOT_BOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37156
ER_ABOUT_ABOUTDATA_MISSING_REQUIRED_FIELD: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37157
ER_ABOUT_INVALID_ABOUTDATA_LISTENER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37158
ER_BUS_PING_GROUP_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37159
ER_BUS_REMOVED_BY_BINDER_SELF: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37160
ER_INVALID_CONFIG: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37161
ER_ABOUT_INVALID_ABOUTDATA_FIELD_VALUE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37162
ER_ABOUT_INVALID_ABOUTDATA_FIELD_APPID_SIZE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37163
ER_BUS_TRANSPORT_ACCESS_DENIED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37164
ER_INVALID_CERTIFICATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37165
ER_CERTIFICATE_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37166
ER_DUPLICATE_CERTIFICATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37167
ER_UNKNOWN_CERTIFICATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37168
ER_MISSING_DIGEST_IN_CERTIFICATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37169
ER_DIGEST_MISMATCH: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37170
ER_DUPLICATE_KEY: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37171
ER_NO_COMMON_TRUST: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37172
ER_MANIFEST_NOT_FOUND: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37173
ER_INVALID_CERT_CHAIN: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37174
ER_NO_TRUST_ANCHOR: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37175
ER_INVALID_APPLICATION_STATE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37176
ER_FEATURE_NOT_AVAILABLE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37177
ER_KEY_STORE_ALREADY_INITIALIZED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37178
ER_KEY_STORE_ID_NOT_YET_SET: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37179
ER_POLICY_NOT_NEWER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37180
ER_MANIFEST_REJECTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37181
ER_INVALID_CERTIFICATE_USAGE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37182
ER_INVALID_SIGNAL_EMISSION_TYPE: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37183
ER_APPLICATION_STATE_LISTENER_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37184
ER_APPLICATION_STATE_LISTENER_NO_SUCH_LISTENER: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37185
ER_MANAGEMENT_ALREADY_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37186
ER_MANAGEMENT_NOT_STARTED: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37187
ER_BUS_DESCRIPTION_ALREADY_EXISTS: win32more.Windows.Win32.Devices.AllJoyn.QStatus = 37188
@winfunctype_pointer
def alljoyn_about_announced_ptr(context: VoidPtr, busName: win32more.Windows.Win32.Foundation.PSTR, version: UInt16, port: UInt16, objectDescriptionArg: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, aboutDataArg: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
alljoyn_about_announceflag = Int32
UNANNOUNCED: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_about_announceflag = 0
ANNOUNCED: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_about_announceflag = 1
alljoyn_aboutdata = IntPtr
alljoyn_aboutdatalistener = IntPtr
class alljoyn_aboutdatalistener_callbacks(Structure):
    about_datalistener_getaboutdata: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_aboutdatalistener_getaboutdata_ptr
    about_datalistener_getannouncedaboutdata: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_aboutdatalistener_getannouncedaboutdata_ptr
@winfunctype_pointer
def alljoyn_aboutdatalistener_getaboutdata_ptr(context: VoidPtr, msgArg: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_aboutdatalistener_getannouncedaboutdata_ptr(context: VoidPtr, msgArg: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
alljoyn_abouticon = IntPtr
alljoyn_abouticonobj = IntPtr
alljoyn_abouticonproxy = IntPtr
alljoyn_aboutlistener = IntPtr
class alljoyn_aboutlistener_callback(Structure):
    about_listener_announced: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_about_announced_ptr
alljoyn_aboutobj = IntPtr
alljoyn_aboutobjectdescription = IntPtr
alljoyn_aboutproxy = IntPtr
alljoyn_applicationstate = Int32
NOT_CLAIMABLE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstate = 0
CLAIMABLE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstate = 1
CLAIMED: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstate = 2
NEED_UPDATE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstate = 3
alljoyn_applicationstatelistener = IntPtr
class alljoyn_applicationstatelistener_callbacks(Structure):
    state: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstatelistener_state_ptr
@winfunctype_pointer
def alljoyn_applicationstatelistener_state_ptr(busName: POINTER(SByte), publicKey: POINTER(SByte), applicationState: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_applicationstate, context: VoidPtr) -> Void: ...
alljoyn_authlistener = IntPtr
@winfunctype_pointer
def alljoyn_authlistener_authenticationcomplete_ptr(context: VoidPtr, authMechanism: win32more.Windows.Win32.Foundation.PSTR, peerName: win32more.Windows.Win32.Foundation.PSTR, success: Int32) -> Void: ...
class alljoyn_authlistener_callbacks(Structure):
    request_credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_requestcredentials_ptr
    verify_credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_verifycredentials_ptr
    security_violation: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr
    authentication_complete: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr
@winfunctype_pointer
def alljoyn_authlistener_requestcredentials_ptr(context: VoidPtr, authMechanism: win32more.Windows.Win32.Foundation.PSTR, peerName: win32more.Windows.Win32.Foundation.PSTR, authCount: UInt16, userName: win32more.Windows.Win32.Foundation.PSTR, credMask: UInt16, credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_credentials) -> Int32: ...
@winfunctype_pointer
def alljoyn_authlistener_requestcredentialsasync_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener, authMechanism: win32more.Windows.Win32.Foundation.PSTR, peerName: win32more.Windows.Win32.Foundation.PSTR, authCount: UInt16, userName: win32more.Windows.Win32.Foundation.PSTR, credMask: UInt16, authContext: VoidPtr) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_authlistener_securityviolation_ptr(context: VoidPtr, status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, msg: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_message) -> Void: ...
@winfunctype_pointer
def alljoyn_authlistener_verifycredentials_ptr(context: VoidPtr, authMechanism: win32more.Windows.Win32.Foundation.PSTR, peerName: win32more.Windows.Win32.Foundation.PSTR, credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_credentials) -> Int32: ...
@winfunctype_pointer
def alljoyn_authlistener_verifycredentialsasync_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener, authMechanism: win32more.Windows.Win32.Foundation.PSTR, peerName: win32more.Windows.Win32.Foundation.PSTR, credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_credentials, authContext: VoidPtr) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
class alljoyn_authlistenerasync_callbacks(Structure):
    request_credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_requestcredentialsasync_ptr
    verify_credentials: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_verifycredentialsasync_ptr
    security_violation: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr
    authentication_complete: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr
alljoyn_autopinger = IntPtr
@winfunctype_pointer
def alljoyn_autopinger_destination_found_ptr(context: VoidPtr, group: win32more.Windows.Win32.Foundation.PSTR, destination: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_autopinger_destination_lost_ptr(context: VoidPtr, group: win32more.Windows.Win32.Foundation.PSTR, destination: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
alljoyn_busattachment = IntPtr
@winfunctype_pointer
def alljoyn_busattachment_joinsessioncb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, sessionId: UInt32, opts: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionopts, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_busattachment_setlinktimeoutcb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, timeout: UInt32, context: VoidPtr) -> Void: ...
alljoyn_buslistener = IntPtr
@winfunctype_pointer
def alljoyn_buslistener_bus_disconnected_ptr(context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_bus_prop_changed_ptr(context: VoidPtr, prop_name: win32more.Windows.Win32.Foundation.PSTR, prop_value: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_bus_stopping_ptr(context: VoidPtr) -> Void: ...
class alljoyn_buslistener_callbacks(Structure):
    listener_registered: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_listener_registered_ptr
    listener_unregistered: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_listener_unregistered_ptr
    found_advertised_name: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_found_advertised_name_ptr
    lost_advertised_name: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_lost_advertised_name_ptr
    name_owner_changed: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_name_owner_changed_ptr
    bus_stopping: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_bus_stopping_ptr
    bus_disconnected: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_bus_disconnected_ptr
    property_changed: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_buslistener_bus_prop_changed_ptr
@winfunctype_pointer
def alljoyn_buslistener_found_advertised_name_ptr(context: VoidPtr, name: win32more.Windows.Win32.Foundation.PSTR, transport: UInt16, namePrefix: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_listener_registered_ptr(context: VoidPtr, bus: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_listener_unregistered_ptr(context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_lost_advertised_name_ptr(context: VoidPtr, name: win32more.Windows.Win32.Foundation.PSTR, transport: UInt16, namePrefix: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_name_owner_changed_ptr(context: VoidPtr, busName: win32more.Windows.Win32.Foundation.PSTR, previousOwner: win32more.Windows.Win32.Foundation.PSTR, newOwner: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
alljoyn_busobject = IntPtr
class alljoyn_busobject_callbacks(Structure):
    property_get: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busobject_prop_get_ptr
    property_set: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busobject_prop_set_ptr
    object_registered: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr
    object_unregistered: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr
class alljoyn_busobject_methodentry(Structure):
    member: POINTER(win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_member)
    method_handler: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagereceiver_methodhandler_ptr
@winfunctype_pointer
def alljoyn_busobject_object_registration_ptr(context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_busobject_prop_get_ptr(context: VoidPtr, ifcName: win32more.Windows.Win32.Foundation.PSTR, propName: win32more.Windows.Win32.Foundation.PSTR, val: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_busobject_prop_set_ptr(context: VoidPtr, ifcName: win32more.Windows.Win32.Foundation.PSTR, propName: win32more.Windows.Win32.Foundation.PSTR, val: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
class alljoyn_certificateid(Structure):
    serial: POINTER(Byte)
    serialLen: UIntPtr
    issuerPublicKey: POINTER(SByte)
    issuerAki: POINTER(Byte)
    issuerAkiLen: UIntPtr
class alljoyn_certificateidarray(Structure):
    count: UIntPtr
    ids: POINTER(win32more.Windows.Win32.Devices.AllJoyn.alljoyn_certificateid)
alljoyn_claimcapability_masks = Int32
CAPABLE_ECDHE_NULL: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_claimcapability_masks = 1
CAPABLE_ECDHE_ECDSA: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_claimcapability_masks = 4
CAPABLE_ECDHE_SPEKE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_claimcapability_masks = 8
alljoyn_claimcapabilityadditionalinfo_masks = Int32
PASSWORD_GENERATED_BY_SECURITY_MANAGER: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_claimcapabilityadditionalinfo_masks = 1
PASSWORD_GENERATED_BY_APPLICATION: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_claimcapabilityadditionalinfo_masks = 2
alljoyn_credentials = IntPtr
alljoyn_interfacedescription = IntPtr
class alljoyn_interfacedescription_member(Structure):
    iface: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription
    memberType: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype
    name: win32more.Windows.Win32.Foundation.PSTR
    signature: win32more.Windows.Win32.Foundation.PSTR
    returnSignature: win32more.Windows.Win32.Foundation.PSTR
    argNames: win32more.Windows.Win32.Foundation.PSTR
    internal_member: VoidPtr
class alljoyn_interfacedescription_property(Structure):
    name: win32more.Windows.Win32.Foundation.PSTR
    signature: win32more.Windows.Win32.Foundation.PSTR
    access: Byte
    internal_property: VoidPtr
alljoyn_interfacedescription_securitypolicy = Int32
AJ_IFC_SECURITY_INHERIT: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy = 0
AJ_IFC_SECURITY_REQUIRED: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy = 1
AJ_IFC_SECURITY_OFF: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy = 2
@winfunctype_pointer
def alljoyn_interfacedescription_translation_callback_ptr(sourceLanguage: win32more.Windows.Win32.Foundation.PSTR, targetLanguage: win32more.Windows.Win32.Foundation.PSTR, sourceText: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
alljoyn_keystore = IntPtr
alljoyn_keystorelistener = IntPtr
@winfunctype_pointer
def alljoyn_keystorelistener_acquireexclusivelock_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
class alljoyn_keystorelistener_callbacks(Structure):
    load_request: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr
    store_request: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr
@winfunctype_pointer
def alljoyn_keystorelistener_loadrequest_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystore) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_keystorelistener_releaseexclusivelock_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener) -> Void: ...
@winfunctype_pointer
def alljoyn_keystorelistener_storerequest_ptr(context: VoidPtr, listener: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystore) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
class alljoyn_keystorelistener_with_synchronization_callbacks(Structure):
    load_request: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr
    store_request: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr
    acquire_exclusive_lock: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_acquireexclusivelock_ptr
    release_exclusive_lock: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_keystorelistener_releaseexclusivelock_ptr
class alljoyn_manifestarray(Structure):
    count: UIntPtr
    xmls: POINTER(POINTER(SByte))
alljoyn_message = IntPtr
@winfunctype_pointer
def alljoyn_messagereceiver_methodhandler_ptr(bus: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_busobject, member: POINTER(win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_member), message: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_message) -> Void: ...
@winfunctype_pointer
def alljoyn_messagereceiver_replyhandler_ptr(message: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_message, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_messagereceiver_signalhandler_ptr(member: POINTER(win32more.Windows.Win32.Devices.AllJoyn.alljoyn_interfacedescription_member), srcPath: win32more.Windows.Win32.Foundation.PSTR, message: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_message) -> Void: ...
alljoyn_messagetype = Int32
ALLJOYN_MESSAGE_INVALID: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype = 0
ALLJOYN_MESSAGE_METHOD_CALL: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype = 1
ALLJOYN_MESSAGE_METHOD_RET: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype = 2
ALLJOYN_MESSAGE_ERROR: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype = 3
ALLJOYN_MESSAGE_SIGNAL: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_messagetype = 4
alljoyn_msgarg = IntPtr
alljoyn_observer = IntPtr
@winfunctype_pointer
def alljoyn_observer_object_discovered_ptr(context: VoidPtr, proxyref: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
@winfunctype_pointer
def alljoyn_observer_object_lost_ptr(context: VoidPtr, proxyref: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
alljoyn_observerlistener = IntPtr
class alljoyn_observerlistener_callback(Structure):
    object_discovered: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_observer_object_discovered_ptr
    object_lost: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_observer_object_lost_ptr
alljoyn_permissionconfigurationlistener = IntPtr
class alljoyn_permissionconfigurationlistener_callbacks(Structure):
    factory_reset: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_factoryreset_ptr
    policy_changed: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_policychanged_ptr
    start_management: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_startmanagement_ptr
    end_management: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_endmanagement_ptr
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_endmanagement_ptr(context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_factoryreset_ptr(context: VoidPtr) -> win32more.Windows.Win32.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_policychanged_ptr(context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_startmanagement_ptr(context: VoidPtr) -> Void: ...
alljoyn_permissionconfigurator = IntPtr
alljoyn_pinglistener = IntPtr
class alljoyn_pinglistener_callback(Structure):
    destination_found: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_autopinger_destination_found_ptr
    destination_lost: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_autopinger_destination_lost_ptr
alljoyn_proxybusobject = IntPtr
@winfunctype_pointer
def alljoyn_proxybusobject_listener_getallpropertiescb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, obj: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject, values: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_getpropertycb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, obj: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject, value: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_introspectcb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, obj: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_propertieschanged_ptr(obj: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject, ifaceName: win32more.Windows.Win32.Foundation.PSTR, changed: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, invalidated: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_msgarg, context: VoidPtr) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_setpropertycb_ptr(status: win32more.Windows.Win32.Devices.AllJoyn.QStatus, obj: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_proxybusobject, context: VoidPtr) -> Void: ...
alljoyn_proxybusobject_ref = IntPtr
alljoyn_securityapplicationproxy = IntPtr
alljoyn_sessionlistener = IntPtr
class alljoyn_sessionlistener_callbacks(Structure):
    session_lost: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlistener_sessionlost_ptr
    session_member_added: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberadded_ptr
    session_member_removed: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberremoved_ptr
@winfunctype_pointer
def alljoyn_sessionlistener_sessionlost_ptr(context: VoidPtr, sessionId: UInt32, reason: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason) -> Void: ...
@winfunctype_pointer
def alljoyn_sessionlistener_sessionmemberadded_ptr(context: VoidPtr, sessionId: UInt32, uniqueName: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_sessionlistener_sessionmemberremoved_ptr(context: VoidPtr, sessionId: UInt32, uniqueName: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
alljoyn_sessionlostreason = Int32
ALLJOYN_SESSIONLOST_INVALID: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 0
ALLJOYN_SESSIONLOST_REMOTE_END_LEFT_SESSION: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 1
ALLJOYN_SESSIONLOST_REMOTE_END_CLOSED_ABRUPTLY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 2
ALLJOYN_SESSIONLOST_REMOVED_BY_BINDER: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 3
ALLJOYN_SESSIONLOST_LINK_TIMEOUT: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 4
ALLJOYN_SESSIONLOST_REASON_OTHER: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionlostreason = 5
alljoyn_sessionopts = IntPtr
alljoyn_sessionportlistener = IntPtr
@winfunctype_pointer
def alljoyn_sessionportlistener_acceptsessionjoiner_ptr(context: VoidPtr, sessionPort: UInt16, joiner: win32more.Windows.Win32.Foundation.PSTR, opts: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionopts) -> Int32: ...
class alljoyn_sessionportlistener_callbacks(Structure):
    accept_session_joiner: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionportlistener_acceptsessionjoiner_ptr
    session_joined: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_sessionportlistener_sessionjoined_ptr
@winfunctype_pointer
def alljoyn_sessionportlistener_sessionjoined_ptr(context: VoidPtr, sessionPort: UInt16, id: UInt32, joiner: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
alljoyn_typeid = Int32
ALLJOYN_INVALID: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 0
ALLJOYN_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 97
ALLJOYN_BOOLEAN: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 98
ALLJOYN_DOUBLE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 100
ALLJOYN_DICT_ENTRY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 101
ALLJOYN_SIGNATURE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 103
ALLJOYN_HANDLE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 104
ALLJOYN_INT32: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 105
ALLJOYN_INT16: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 110
ALLJOYN_OBJECT_PATH: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 111
ALLJOYN_UINT16: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 113
ALLJOYN_STRUCT: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 114
ALLJOYN_STRING: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 115
ALLJOYN_UINT64: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 116
ALLJOYN_UINT32: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 117
ALLJOYN_VARIANT: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 118
ALLJOYN_INT64: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 120
ALLJOYN_BYTE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 121
ALLJOYN_STRUCT_OPEN: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 40
ALLJOYN_STRUCT_CLOSE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 41
ALLJOYN_DICT_ENTRY_OPEN: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 123
ALLJOYN_DICT_ENTRY_CLOSE: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 125
ALLJOYN_BOOLEAN_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 25185
ALLJOYN_DOUBLE_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 25697
ALLJOYN_INT32_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 26977
ALLJOYN_INT16_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 28257
ALLJOYN_UINT16_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 29025
ALLJOYN_UINT64_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 29793
ALLJOYN_UINT32_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 30049
ALLJOYN_INT64_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 30817
ALLJOYN_BYTE_ARRAY: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 31073
ALLJOYN_WILDCARD: win32more.Windows.Win32.Devices.AllJoyn.alljoyn_typeid = 42


make_ready(__name__)
