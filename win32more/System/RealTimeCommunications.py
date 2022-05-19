from win32more import *
import win32more.Foundation
import win32more.Media.DirectShow
import win32more.Networking.WinSock
import win32more.System.Com
import win32more.System.RealTimeCommunications

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
RTCCS_FORCE_PROFILE = 1
RTCCS_FAIL_ON_REDIRECT = 2
RTCMT_AUDIO_SEND = 1
RTCMT_AUDIO_RECEIVE = 2
RTCMT_VIDEO_SEND = 4
RTCMT_VIDEO_RECEIVE = 8
RTCMT_T120_SENDRECV = 16
RTCSI_PC_TO_PC = 1
RTCSI_PC_TO_PHONE = 2
RTCSI_PHONE_TO_PHONE = 4
RTCSI_IM = 8
RTCSI_MULTIPARTY_IM = 16
RTCSI_APPLICATION = 32
RTCTR_UDP = 1
RTCTR_TCP = 2
RTCTR_TLS = 4
RTCAU_BASIC = 1
RTCAU_DIGEST = 2
RTCAU_NTLM = 4
RTCAU_KERBEROS = 8
RTCAU_USE_LOGON_CRED = 65536
RTCRF_REGISTER_INVITE_SESSIONS = 1
RTCRF_REGISTER_MESSAGE_SESSIONS = 2
RTCRF_REGISTER_PRESENCE = 4
RTCRF_REGISTER_NOTIFY = 8
RTCRF_REGISTER_ALL = 15
RTCRMF_BUDDY_ROAMING = 1
RTCRMF_WATCHER_ROAMING = 2
RTCRMF_PRESENCE_ROAMING = 4
RTCRMF_PROFILE_ROAMING = 8
RTCRMF_ALL_ROAMING = 15
RTCEF_CLIENT = 1
RTCEF_REGISTRATION_STATE_CHANGE = 2
RTCEF_SESSION_STATE_CHANGE = 4
RTCEF_SESSION_OPERATION_COMPLETE = 8
RTCEF_PARTICIPANT_STATE_CHANGE = 16
RTCEF_MEDIA = 32
RTCEF_INTENSITY = 64
RTCEF_MESSAGING = 128
RTCEF_BUDDY = 256
RTCEF_WATCHER = 512
RTCEF_PROFILE = 1024
RTCEF_USERSEARCH = 2048
RTCEF_INFO = 4096
RTCEF_GROUP = 8192
RTCEF_MEDIA_REQUEST = 16384
RTCEF_ROAMING = 65536
RTCEF_PRESENCE_PROPERTY = 131072
RTCEF_BUDDY2 = 262144
RTCEF_WATCHER2 = 524288
RTCEF_SESSION_REFER_STATUS = 1048576
RTCEF_SESSION_REFERRED = 2097152
RTCEF_REINVITE = 4194304
RTCEF_PRESENCE_DATA = 8388608
RTCEF_PRESENCE_STATUS = 16777216
RTCEF_ALL = 33554431
RTCIF_DISABLE_MEDIA = 1
RTCIF_DISABLE_UPNP = 2
RTCIF_ENABLE_SERVER_CLASS = 4
RTCIF_DISABLE_STRICT_DNS = 8
FACILITY_RTC_INTERFACE = 238
FACILITY_SIP_STATUS_CODE = 239
FACILITY_PINT_STATUS_CODE = 240
STATUS_SEVERITY_RTC_ERROR = 2
RTC_E_SIP_CODECS_DO_NOT_MATCH = -2131886080
RTC_E_SIP_STREAM_PRESENT = -2131886079
RTC_E_SIP_STREAM_NOT_PRESENT = -2131886078
RTC_E_SIP_NO_STREAM = -2131886077
RTC_E_SIP_PARSE_FAILED = -2131886076
RTC_E_SIP_HEADER_NOT_PRESENT = -2131886075
RTC_E_SDP_NOT_PRESENT = -2131886074
RTC_E_SDP_PARSE_FAILED = -2131886073
RTC_E_SDP_UPDATE_FAILED = -2131886072
RTC_E_SDP_MULTICAST = -2131886071
RTC_E_SDP_CONNECTION_ADDR = -2131886070
RTC_E_SDP_NO_MEDIA = -2131886069
RTC_E_SIP_TIMEOUT = -2131886068
RTC_E_SDP_FAILED_TO_BUILD = -2131886067
RTC_E_SIP_INVITE_TRANSACTION_PENDING = -2131886066
RTC_E_SIP_AUTH_HEADER_SENT = -2131886065
RTC_E_SIP_AUTH_TYPE_NOT_SUPPORTED = -2131886064
RTC_E_SIP_AUTH_FAILED = -2131886063
RTC_E_INVALID_SIP_URL = -2131886062
RTC_E_DESTINATION_ADDRESS_LOCAL = -2131886061
RTC_E_INVALID_ADDRESS_LOCAL = -2131886060
RTC_E_DESTINATION_ADDRESS_MULTICAST = -2131886059
RTC_E_INVALID_PROXY_ADDRESS = -2131886058
RTC_E_SIP_TRANSPORT_NOT_SUPPORTED = -2131886057
RTC_E_SIP_NEED_MORE_DATA = -2131886056
RTC_E_SIP_CALL_DISCONNECTED = -2131886055
RTC_E_SIP_REQUEST_DESTINATION_ADDR_NOT_PRESENT = -2131886054
RTC_E_SIP_UDP_SIZE_EXCEEDED = -2131886053
RTC_E_SIP_SSL_TUNNEL_FAILED = -2131886052
RTC_E_SIP_SSL_NEGOTIATION_TIMEOUT = -2131886051
RTC_E_SIP_STACK_SHUTDOWN = -2131886050
RTC_E_MEDIA_CONTROLLER_STATE = -2131886049
RTC_E_MEDIA_NEED_TERMINAL = -2131886048
RTC_E_MEDIA_AUDIO_DEVICE_NOT_AVAILABLE = -2131886047
RTC_E_MEDIA_VIDEO_DEVICE_NOT_AVAILABLE = -2131886046
RTC_E_START_STREAM = -2131886045
RTC_E_MEDIA_AEC = -2131886044
RTC_E_CLIENT_NOT_INITIALIZED = -2131886043
RTC_E_CLIENT_ALREADY_INITIALIZED = -2131886042
RTC_E_CLIENT_ALREADY_SHUT_DOWN = -2131886041
RTC_E_PRESENCE_NOT_ENABLED = -2131886040
RTC_E_INVALID_SESSION_TYPE = -2131886039
RTC_E_INVALID_SESSION_STATE = -2131886038
RTC_E_NO_PROFILE = -2131886037
RTC_E_LOCAL_PHONE_NEEDED = -2131886036
RTC_E_NO_DEVICE = -2131886035
RTC_E_INVALID_PROFILE = -2131886034
RTC_E_PROFILE_NO_PROVISION = -2131886033
RTC_E_PROFILE_NO_KEY = -2131886032
RTC_E_PROFILE_NO_NAME = -2131886031
RTC_E_PROFILE_NO_USER = -2131886030
RTC_E_PROFILE_NO_USER_URI = -2131886029
RTC_E_PROFILE_NO_SERVER = -2131886028
RTC_E_PROFILE_NO_SERVER_ADDRESS = -2131886027
RTC_E_PROFILE_NO_SERVER_PROTOCOL = -2131886026
RTC_E_PROFILE_INVALID_SERVER_PROTOCOL = -2131886025
RTC_E_PROFILE_INVALID_SERVER_AUTHMETHOD = -2131886024
RTC_E_PROFILE_INVALID_SERVER_ROLE = -2131886023
RTC_E_PROFILE_MULTIPLE_REGISTRARS = -2131886022
RTC_E_PROFILE_INVALID_SESSION = -2131886021
RTC_E_PROFILE_INVALID_SESSION_PARTY = -2131886020
RTC_E_PROFILE_INVALID_SESSION_TYPE = -2131886019
RTC_E_OPERATION_WITH_TOO_MANY_PARTICIPANTS = -2131886018
RTC_E_BASIC_AUTH_SET_TLS = -2131886017
RTC_E_SIP_HIGH_SECURITY_SET_TLS = -2131886016
RTC_S_ROAMING_NOT_SUPPORTED = 15597633
RTC_E_PROFILE_SERVER_UNAUTHORIZED = -2131886014
RTC_E_DUPLICATE_REALM = -2131886013
RTC_E_POLICY_NOT_ALLOW = -2131886012
RTC_E_PORT_MAPPING_UNAVAILABLE = -2131886011
RTC_E_PORT_MAPPING_FAILED = -2131886010
RTC_E_SECURITY_LEVEL_NOT_COMPATIBLE = -2131886009
RTC_E_SECURITY_LEVEL_NOT_DEFINED = -2131886008
RTC_E_SECURITY_LEVEL_NOT_SUPPORTED_BY_PARTICIPANT = -2131886007
RTC_E_DUPLICATE_BUDDY = -2131886006
RTC_E_DUPLICATE_WATCHER = -2131886005
RTC_E_MALFORMED_XML = -2131886004
RTC_E_ROAMING_OPERATION_INTERRUPTED = -2131886003
RTC_E_ROAMING_FAILED = -2131886002
RTC_E_INVALID_BUDDY_LIST = -2131886001
RTC_E_INVALID_ACL_LIST = -2131886000
RTC_E_NO_GROUP = -2131885999
RTC_E_DUPLICATE_GROUP = -2131885998
RTC_E_TOO_MANY_GROUPS = -2131885997
RTC_E_NO_BUDDY = -2131885996
RTC_E_NO_WATCHER = -2131885995
RTC_E_NO_REALM = -2131885994
RTC_E_NO_TRANSPORT = -2131885993
RTC_E_NOT_EXIST = -2131885992
RTC_E_INVALID_PREFERENCE_LIST = -2131885991
RTC_E_MAX_PENDING_OPERATIONS = -2131885990
RTC_E_TOO_MANY_RETRIES = -2131885989
RTC_E_INVALID_PORTRANGE = -2131885988
RTC_E_SIP_CALL_CONNECTION_NOT_ESTABLISHED = -2131885987
RTC_E_SIP_ADDITIONAL_PARTY_IN_TWO_PARTY_SESSION = -2131885986
RTC_E_SIP_PARTY_ALREADY_IN_SESSION = -2131885985
RTC_E_SIP_OTHER_PARTY_JOIN_IN_PROGRESS = -2131885984
RTC_E_INVALID_OBJECT_STATE = -2131885983
RTC_E_PRESENCE_ENABLED = -2131885982
RTC_E_ROAMING_ENABLED = -2131885981
RTC_E_SIP_TLS_INCOMPATIBLE_ENCRYPTION = -2131885980
RTC_E_SIP_INVALID_CERTIFICATE = -2131885979
RTC_E_SIP_DNS_FAIL = -2131885978
RTC_E_SIP_TCP_FAIL = -2131885977
RTC_E_TOO_SMALL_EXPIRES_VALUE = -2131885976
RTC_E_SIP_TLS_FAIL = -2131885975
RTC_E_NOT_PRESENCE_PROFILE = -2131885974
RTC_E_SIP_INVITEE_PARTY_TIMEOUT = -2131885973
RTC_E_SIP_AUTH_TIME_SKEW = -2131885972
RTC_E_INVALID_REGISTRATION_STATE = -2131885971
RTC_E_MEDIA_DISABLED = -2131885970
RTC_E_MEDIA_ENABLED = -2131885969
RTC_E_REFER_NOT_ACCEPTED = -2131885968
RTC_E_REFER_NOT_ALLOWED = -2131885967
RTC_E_REFER_NOT_EXIST = -2131885966
RTC_E_SIP_HOLD_OPERATION_PENDING = -2131885965
RTC_E_SIP_UNHOLD_OPERATION_PENDING = -2131885964
RTC_E_MEDIA_SESSION_NOT_EXIST = -2131885963
RTC_E_MEDIA_SESSION_IN_HOLD = -2131885962
RTC_E_ANOTHER_MEDIA_SESSION_ACTIVE = -2131885961
RTC_E_MAX_REDIRECTS = -2131885960
RTC_E_REDIRECT_PROCESSING_FAILED = -2131885959
RTC_E_LISTENING_SOCKET_NOT_EXIST = -2131885958
RTC_E_INVALID_LISTEN_SOCKET = -2131885957
RTC_E_PORT_MANAGER_ALREADY_SET = -2131885956
RTC_E_SECURITY_LEVEL_ALREADY_SET = -2131885955
RTC_E_UDP_NOT_SUPPORTED = -2131885954
RTC_E_SIP_REFER_OPERATION_PENDING = -2131885953
RTC_E_PLATFORM_NOT_SUPPORTED = -2131885952
RTC_E_SIP_PEER_PARTICIPANT_IN_MULTIPARTY_SESSION = -2131885951
RTC_E_NOT_ALLOWED = -2131885950
RTC_E_REGISTRATION_DEACTIVATED = -2131885949
RTC_E_REGISTRATION_REJECTED = -2131885948
RTC_E_REGISTRATION_UNREGISTERED = -2131885947
RTC_E_STATUS_INFO_TRYING = 15663204
RTC_E_STATUS_INFO_RINGING = 15663284
RTC_E_STATUS_INFO_CALL_FORWARDING = 15663285
RTC_E_STATUS_INFO_QUEUED = 15663286
RTC_E_STATUS_SESSION_PROGRESS = 15663287
RTC_E_STATUS_SUCCESS = 15663304
RTC_E_STATUS_REDIRECT_MULTIPLE_CHOICES = -2131820244
RTC_E_STATUS_REDIRECT_MOVED_PERMANENTLY = -2131820243
RTC_E_STATUS_REDIRECT_MOVED_TEMPORARILY = -2131820242
RTC_E_STATUS_REDIRECT_SEE_OTHER = -2131820241
RTC_E_STATUS_REDIRECT_USE_PROXY = -2131820239
RTC_E_STATUS_REDIRECT_ALTERNATIVE_SERVICE = -2131820164
RTC_E_STATUS_CLIENT_BAD_REQUEST = -2131820144
RTC_E_STATUS_CLIENT_UNAUTHORIZED = -2131820143
RTC_E_STATUS_CLIENT_PAYMENT_REQUIRED = -2131820142
RTC_E_STATUS_CLIENT_FORBIDDEN = -2131820141
RTC_E_STATUS_CLIENT_NOT_FOUND = -2131820140
RTC_E_STATUS_CLIENT_METHOD_NOT_ALLOWED = -2131820139
RTC_E_STATUS_CLIENT_NOT_ACCEPTABLE = -2131820138
RTC_E_STATUS_CLIENT_PROXY_AUTHENTICATION_REQUIRED = -2131820137
RTC_E_STATUS_CLIENT_REQUEST_TIMEOUT = -2131820136
RTC_E_STATUS_CLIENT_CONFLICT = -2131820135
RTC_E_STATUS_CLIENT_GONE = -2131820134
RTC_E_STATUS_CLIENT_LENGTH_REQUIRED = -2131820133
RTC_E_STATUS_CLIENT_REQUEST_ENTITY_TOO_LARGE = -2131820131
RTC_E_STATUS_CLIENT_REQUEST_URI_TOO_LARGE = -2131820130
RTC_E_STATUS_CLIENT_UNSUPPORTED_MEDIA_TYPE = -2131820129
RTC_E_STATUS_CLIENT_BAD_EXTENSION = -2131820124
RTC_E_STATUS_CLIENT_TEMPORARILY_NOT_AVAILABLE = -2131820064
RTC_E_STATUS_CLIENT_TRANSACTION_DOES_NOT_EXIST = -2131820063
RTC_E_STATUS_CLIENT_LOOP_DETECTED = -2131820062
RTC_E_STATUS_CLIENT_TOO_MANY_HOPS = -2131820061
RTC_E_STATUS_CLIENT_ADDRESS_INCOMPLETE = -2131820060
RTC_E_STATUS_CLIENT_AMBIGUOUS = -2131820059
RTC_E_STATUS_CLIENT_BUSY_HERE = -2131820058
RTC_E_STATUS_REQUEST_TERMINATED = -2131820057
RTC_E_STATUS_NOT_ACCEPTABLE_HERE = -2131820056
RTC_E_STATUS_SERVER_INTERNAL_ERROR = -2131820044
RTC_E_STATUS_SERVER_NOT_IMPLEMENTED = -2131820043
RTC_E_STATUS_SERVER_BAD_GATEWAY = -2131820042
RTC_E_STATUS_SERVER_SERVICE_UNAVAILABLE = -2131820041
RTC_E_STATUS_SERVER_SERVER_TIMEOUT = -2131820040
RTC_E_STATUS_SERVER_VERSION_NOT_SUPPORTED = -2131820039
RTC_E_STATUS_GLOBAL_BUSY_EVERYWHERE = -2131819944
RTC_E_STATUS_GLOBAL_DECLINE = -2131819941
RTC_E_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE = -2131819940
RTC_E_STATUS_GLOBAL_NOT_ACCEPTABLE = -2131819938
RTC_E_PINT_STATUS_REJECTED_BUSY = -2131755003
RTC_E_PINT_STATUS_REJECTED_NO_ANSWER = -2131755002
RTC_E_PINT_STATUS_REJECTED_ALL_BUSY = -2131755001
RTC_E_PINT_STATUS_REJECTED_PL_FAILED = -2131755000
RTC_E_PINT_STATUS_REJECTED_SW_FAILED = -2131754999
RTC_E_PINT_STATUS_REJECTED_CANCELLED = -2131754998
RTC_E_PINT_STATUS_REJECTED_BADNUMBER = -2131754997
RTCClient = Guid('7a42ea29-a2b7-40c4-b091-f6f024aa89be')
RTC_AUDIO_DEVICE = Int32
RTCAD_SPEAKER = 0
RTCAD_MICROPHONE = 1
RTC_VIDEO_DEVICE = Int32
RTCVD_RECEIVE = 0
RTCVD_PREVIEW = 1
RTC_EVENT = Int32
RTCE_CLIENT = 0
RTCE_REGISTRATION_STATE_CHANGE = 1
RTCE_SESSION_STATE_CHANGE = 2
RTCE_SESSION_OPERATION_COMPLETE = 3
RTCE_PARTICIPANT_STATE_CHANGE = 4
RTCE_MEDIA = 5
RTCE_INTENSITY = 6
RTCE_MESSAGING = 7
RTCE_BUDDY = 8
RTCE_WATCHER = 9
RTCE_PROFILE = 10
RTCE_USERSEARCH = 11
RTCE_INFO = 12
RTCE_GROUP = 13
RTCE_MEDIA_REQUEST = 14
RTCE_ROAMING = 15
RTCE_PRESENCE_PROPERTY = 16
RTCE_PRESENCE_DATA = 17
RTCE_PRESENCE_STATUS = 18
RTCE_SESSION_REFER_STATUS = 19
RTCE_SESSION_REFERRED = 20
RTCE_REINVITE = 21
RTC_LISTEN_MODE = Int32
RTCLM_NONE = 0
RTCLM_DYNAMIC = 1
RTCLM_BOTH = 2
RTC_CLIENT_EVENT_TYPE = Int32
RTCCET_VOLUME_CHANGE = 0
RTCCET_DEVICE_CHANGE = 1
RTCCET_NETWORK_QUALITY_CHANGE = 2
RTCCET_ASYNC_CLEANUP_DONE = 3
RTC_BUDDY_EVENT_TYPE = Int32
RTCBET_BUDDY_ADD = 0
RTCBET_BUDDY_REMOVE = 1
RTCBET_BUDDY_UPDATE = 2
RTCBET_BUDDY_STATE_CHANGE = 3
RTCBET_BUDDY_ROAMED = 4
RTCBET_BUDDY_SUBSCRIBED = 5
RTC_WATCHER_EVENT_TYPE = Int32
RTCWET_WATCHER_ADD = 0
RTCWET_WATCHER_REMOVE = 1
RTCWET_WATCHER_UPDATE = 2
RTCWET_WATCHER_OFFERING = 3
RTCWET_WATCHER_ROAMED = 4
RTC_GROUP_EVENT_TYPE = Int32
RTCGET_GROUP_ADD = 0
RTCGET_GROUP_REMOVE = 1
RTCGET_GROUP_UPDATE = 2
RTCGET_GROUP_BUDDY_ADD = 3
RTCGET_GROUP_BUDDY_REMOVE = 4
RTCGET_GROUP_ROAMED = 5
RTC_TERMINATE_REASON = Int32
RTCTR_NORMAL = 0
RTCTR_DND = 1
RTCTR_BUSY = 2
RTCTR_REJECT = 3
RTCTR_TIMEOUT = 4
RTCTR_SHUTDOWN = 5
RTCTR_INSUFFICIENT_SECURITY_LEVEL = 6
RTCTR_NOT_SUPPORTED = 7
RTC_REGISTRATION_STATE = Int32
RTCRS_NOT_REGISTERED = 0
RTCRS_REGISTERING = 1
RTCRS_REGISTERED = 2
RTCRS_REJECTED = 3
RTCRS_UNREGISTERING = 4
RTCRS_ERROR = 5
RTCRS_LOGGED_OFF = 6
RTCRS_LOCAL_PA_LOGGED_OFF = 7
RTCRS_REMOTE_PA_LOGGED_OFF = 8
RTC_SESSION_STATE = Int32
RTCSS_IDLE = 0
RTCSS_INCOMING = 1
RTCSS_ANSWERING = 2
RTCSS_INPROGRESS = 3
RTCSS_CONNECTED = 4
RTCSS_DISCONNECTED = 5
RTCSS_HOLD = 6
RTCSS_REFER = 7
RTC_PARTICIPANT_STATE = Int32
RTCPS_IDLE = 0
RTCPS_PENDING = 1
RTCPS_INCOMING = 2
RTCPS_ANSWERING = 3
RTCPS_INPROGRESS = 4
RTCPS_ALERTING = 5
RTCPS_CONNECTED = 6
RTCPS_DISCONNECTING = 7
RTCPS_DISCONNECTED = 8
RTC_WATCHER_STATE = Int32
RTCWS_UNKNOWN = 0
RTCWS_OFFERING = 1
RTCWS_ALLOWED = 2
RTCWS_BLOCKED = 3
RTCWS_DENIED = 4
RTCWS_PROMPT = 5
RTC_ACE_SCOPE = Int32
RTCAS_SCOPE_USER = 0
RTCAS_SCOPE_DOMAIN = 1
RTCAS_SCOPE_ALL = 2
RTC_OFFER_WATCHER_MODE = Int32
RTCOWM_OFFER_WATCHER_EVENT = 0
RTCOWM_AUTOMATICALLY_ADD_WATCHER = 1
RTC_WATCHER_MATCH_MODE = Int32
RTCWMM_EXACT_MATCH = 0
RTCWMM_BEST_ACE_MATCH = 1
RTC_PRIVACY_MODE = Int32
RTCPM_BLOCK_LIST_EXCLUDED = 0
RTCPM_ALLOW_LIST_ONLY = 1
RTC_SESSION_TYPE = Int32
RTCST_PC_TO_PC = 0
RTCST_PC_TO_PHONE = 1
RTCST_PHONE_TO_PHONE = 2
RTCST_IM = 3
RTCST_MULTIPARTY_IM = 4
RTCST_APPLICATION = 5
RTC_PRESENCE_STATUS = Int32
RTCXS_PRESENCE_OFFLINE = 0
RTCXS_PRESENCE_ONLINE = 1
RTCXS_PRESENCE_AWAY = 2
RTCXS_PRESENCE_IDLE = 3
RTCXS_PRESENCE_BUSY = 4
RTCXS_PRESENCE_BE_RIGHT_BACK = 5
RTCXS_PRESENCE_ON_THE_PHONE = 6
RTCXS_PRESENCE_OUT_TO_LUNCH = 7
RTC_BUDDY_SUBSCRIPTION_TYPE = Int32
RTCBT_SUBSCRIBED = 0
RTCBT_ALWAYS_OFFLINE = 1
RTCBT_ALWAYS_ONLINE = 2
RTCBT_POLL = 3
RTC_MEDIA_EVENT_TYPE = Int32
RTCMET_STOPPED = 0
RTCMET_STARTED = 1
RTCMET_FAILED = 2
RTC_MEDIA_EVENT_REASON = Int32
RTCMER_NORMAL = 0
RTCMER_HOLD = 1
RTCMER_TIMEOUT = 2
RTCMER_BAD_DEVICE = 3
RTCMER_NO_PORT = 4
RTCMER_PORT_MAPPING_FAILED = 5
RTCMER_REMOTE_REQUEST = 6
RTC_MESSAGING_EVENT_TYPE = Int32
RTCMSET_MESSAGE = 0
RTCMSET_STATUS = 1
RTC_MESSAGING_USER_STATUS = Int32
RTCMUS_IDLE = 0
RTCMUS_TYPING = 1
RTC_DTMF = Int32
RTC_DTMF_0 = 0
RTC_DTMF_1 = 1
RTC_DTMF_2 = 2
RTC_DTMF_3 = 3
RTC_DTMF_4 = 4
RTC_DTMF_5 = 5
RTC_DTMF_6 = 6
RTC_DTMF_7 = 7
RTC_DTMF_8 = 8
RTC_DTMF_9 = 9
RTC_DTMF_STAR = 10
RTC_DTMF_POUND = 11
RTC_DTMF_A = 12
RTC_DTMF_B = 13
RTC_DTMF_C = 14
RTC_DTMF_D = 15
RTC_DTMF_FLASH = 16
RTC_PROVIDER_URI = Int32
RTCPU_URIHOMEPAGE = 0
RTCPU_URIHELPDESK = 1
RTCPU_URIPERSONALACCOUNT = 2
RTCPU_URIDISPLAYDURINGCALL = 3
RTCPU_URIDISPLAYDURINGIDLE = 4
RTC_RING_TYPE = Int32
RTCRT_PHONE = 0
RTCRT_MESSAGE = 1
RTCRT_RINGBACK = 2
RTC_T120_APPLET = Int32
RTCTA_WHITEBOARD = 0
RTCTA_APPSHARING = 1
RTC_PORT_TYPE = Int32
RTCPT_AUDIO_RTP = 0
RTCPT_AUDIO_RTCP = 1
RTCPT_VIDEO_RTP = 2
RTCPT_VIDEO_RTCP = 3
RTCPT_SIP = 4
RTC_USER_SEARCH_COLUMN = Int32
RTCUSC_URI = 0
RTCUSC_DISPLAYNAME = 1
RTCUSC_TITLE = 2
RTCUSC_OFFICE = 3
RTCUSC_PHONE = 4
RTCUSC_COMPANY = 5
RTCUSC_CITY = 6
RTCUSC_STATE = 7
RTCUSC_COUNTRY = 8
RTCUSC_EMAIL = 9
RTC_USER_SEARCH_PREFERENCE = Int32
RTCUSP_MAX_MATCHES = 0
RTCUSP_TIME_LIMIT = 1
RTC_ROAMING_EVENT_TYPE = Int32
RTCRET_BUDDY_ROAMING = 0
RTCRET_WATCHER_ROAMING = 1
RTCRET_PRESENCE_ROAMING = 2
RTCRET_PROFILE_ROAMING = 3
RTCRET_WPENDING_ROAMING = 4
RTC_PROFILE_EVENT_TYPE = Int32
RTCPFET_PROFILE_GET = 0
RTCPFET_PROFILE_UPDATE = 1
RTC_ANSWER_MODE = Int32
RTCAM_OFFER_SESSION_EVENT = 0
RTCAM_AUTOMATICALLY_ACCEPT = 1
RTCAM_AUTOMATICALLY_REJECT = 2
RTCAM_NOT_SUPPORTED = 3
RTC_SESSION_REFER_STATUS = Int32
RTCSRS_REFERRING = 0
RTCSRS_ACCEPTED = 1
RTCSRS_ERROR = 2
RTCSRS_REJECTED = 3
RTCSRS_DROPPED = 4
RTCSRS_DONE = 5
RTC_PRESENCE_PROPERTY = Int32
RTCPP_PHONENUMBER = 0
RTCPP_DISPLAYNAME = 1
RTCPP_EMAIL = 2
RTCPP_DEVICE_NAME = 3
RTCPP_MULTIPLE = 4
RTC_SECURITY_TYPE = Int32
RTCSECT_AUDIO_VIDEO_MEDIA_ENCRYPTION = 0
RTCSECT_T120_MEDIA_ENCRYPTION = 1
RTC_SECURITY_LEVEL = Int32
RTCSECL_UNSUPPORTED = 1
RTCSECL_SUPPORTED = 2
RTCSECL_REQUIRED = 3
RTC_REINVITE_STATE = Int32
RTCRIN_INCOMING = 0
RTCRIN_SUCCEEDED = 1
RTCRIN_FAIL = 2
def _define_IRTCClient_head():
    class IRTCClient(win32more.System.Com.IUnknown_head):
        Guid = Guid('07829e45-9a34-408e-a011-bddf13487cd1')
    return IRTCClient
def _define_IRTCClient():
    IRTCClient = win32more.System.RealTimeCommunications.IRTCClient_head
    IRTCClient.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Initialize', ()))
    IRTCClient.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Shutdown', ()))
    IRTCClient.PrepareForShutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'PrepareForShutdown', ()))
    IRTCClient.put_EventFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(6, 'put_EventFilter', ((1, 'lFilter'),)))
    IRTCClient.get_EventFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_EventFilter', ((1, 'plFilter'),)))
    IRTCClient.SetPreferredMediaTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int16, use_last_error=False)(8, 'SetPreferredMediaTypes', ((1, 'lMediaTypes'),(1, 'fPersistent'),)))
    IRTCClient.get_PreferredMediaTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_PreferredMediaTypes', ((1, 'plMediaTypes'),)))
    IRTCClient.get_MediaCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_MediaCapabilities', ((1, 'plMediaTypes'),)))
    IRTCClient.CreateSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SESSION_TYPE,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCSession_head), use_last_error=False)(11, 'CreateSession', ((1, 'enType'),(1, 'bstrLocalPhoneURI'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppSession'),)))
    IRTCClient.put_ListenForIncomingSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_LISTEN_MODE, use_last_error=False)(12, 'put_ListenForIncomingSessions', ((1, 'enListen'),)))
    IRTCClient.get_ListenForIncomingSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_LISTEN_MODE), use_last_error=False)(13, 'get_ListenForIncomingSessions', ((1, 'penListen'),)))
    IRTCClient.get_NetworkAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int16,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'get_NetworkAddresses', ((1, 'fTCP'),(1, 'fExternal'),(1, 'pvAddresses'),)))
    IRTCClient.put_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,Int32, use_last_error=False)(15, 'put_Volume', ((1, 'enDevice'),(1, 'lVolume'),)))
    IRTCClient.get_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,POINTER(Int32), use_last_error=False)(16, 'get_Volume', ((1, 'enDevice'),(1, 'plVolume'),)))
    IRTCClient.put_AudioMuted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,Int16, use_last_error=False)(17, 'put_AudioMuted', ((1, 'enDevice'),(1, 'fMuted'),)))
    IRTCClient.get_AudioMuted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,POINTER(Int16), use_last_error=False)(18, 'get_AudioMuted', ((1, 'enDevice'),(1, 'pfMuted'),)))
    IRTCClient.get_IVideoWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_VIDEO_DEVICE,POINTER(win32more.Media.DirectShow.IVideoWindow_head), use_last_error=False)(19, 'get_IVideoWindow', ((1, 'enDevice'),(1, 'ppIVideoWindow'),)))
    IRTCClient.put_PreferredAudioDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_PreferredAudioDevice', ((1, 'enDevice'),(1, 'bstrDeviceName'),)))
    IRTCClient.get_PreferredAudioDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_PreferredAudioDevice', ((1, 'enDevice'),(1, 'pbstrDeviceName'),)))
    IRTCClient.put_PreferredVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,Int32, use_last_error=False)(22, 'put_PreferredVolume', ((1, 'enDevice'),(1, 'lVolume'),)))
    IRTCClient.get_PreferredVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE,POINTER(Int32), use_last_error=False)(23, 'get_PreferredVolume', ((1, 'enDevice'),(1, 'plVolume'),)))
    IRTCClient.put_PreferredAEC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(24, 'put_PreferredAEC', ((1, 'bEnable'),)))
    IRTCClient.get_PreferredAEC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_PreferredAEC', ((1, 'pbEnabled'),)))
    IRTCClient.put_PreferredVideoDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_PreferredVideoDevice', ((1, 'bstrDeviceName'),)))
    IRTCClient.get_PreferredVideoDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(27, 'get_PreferredVideoDevice', ((1, 'pbstrDeviceName'),)))
    IRTCClient.get_ActiveMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'get_ActiveMedia', ((1, 'plMediaType'),)))
    IRTCClient.put_MaxBitrate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'put_MaxBitrate', ((1, 'lMaxBitrate'),)))
    IRTCClient.get_MaxBitrate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(30, 'get_MaxBitrate', ((1, 'plMaxBitrate'),)))
    IRTCClient.put_TemporalSpatialTradeOff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(31, 'put_TemporalSpatialTradeOff', ((1, 'lValue'),)))
    IRTCClient.get_TemporalSpatialTradeOff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(32, 'get_TemporalSpatialTradeOff', ((1, 'plValue'),)))
    IRTCClient.get_NetworkQuality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(33, 'get_NetworkQuality', ((1, 'plNetworkQuality'),)))
    IRTCClient.StartT120Applet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_T120_APPLET, use_last_error=False)(34, 'StartT120Applet', ((1, 'enApplet'),)))
    IRTCClient.StopT120Applets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'StopT120Applets', ()))
    IRTCClient.get_IsT120AppletRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_T120_APPLET,POINTER(Int16), use_last_error=False)(36, 'get_IsT120AppletRunning', ((1, 'enApplet'),(1, 'pfRunning'),)))
    IRTCClient.get_LocalUserURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_LocalUserURI', ((1, 'pbstrUserURI'),)))
    IRTCClient.put_LocalUserURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(38, 'put_LocalUserURI', ((1, 'bstrUserURI'),)))
    IRTCClient.get_LocalUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(39, 'get_LocalUserName', ((1, 'pbstrUserName'),)))
    IRTCClient.put_LocalUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(40, 'put_LocalUserName', ((1, 'bstrUserName'),)))
    IRTCClient.PlayRing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_RING_TYPE,Int16, use_last_error=False)(41, 'PlayRing', ((1, 'enType'),(1, 'bPlay'),)))
    IRTCClient.SendDTMF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_DTMF, use_last_error=False)(42, 'SendDTMF', ((1, 'enDTMF'),)))
    IRTCClient.InvokeTuningWizard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(43, 'InvokeTuningWizard', ((1, 'hwndParent'),)))
    IRTCClient.get_IsTuned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(44, 'get_IsTuned', ((1, 'pfTuned'),)))
    return IRTCClient
def _define_IRTCClient2_head():
    class IRTCClient2(win32more.System.RealTimeCommunications.IRTCClient_head):
        Guid = Guid('0c91d71d-1064-42da-bfa5-572beb8eea84')
    return IRTCClient2
def _define_IRTCClient2():
    IRTCClient2 = win32more.System.RealTimeCommunications.IRTCClient2_head
    IRTCClient2.put_AnswerMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SESSION_TYPE,win32more.System.RealTimeCommunications.RTC_ANSWER_MODE, use_last_error=False)(45, 'put_AnswerMode', ((1, 'enType'),(1, 'enMode'),)))
    IRTCClient2.get_AnswerMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SESSION_TYPE,POINTER(win32more.System.RealTimeCommunications.RTC_ANSWER_MODE), use_last_error=False)(46, 'get_AnswerMode', ((1, 'enType'),(1, 'penMode'),)))
    IRTCClient2.InvokeTuningWizardEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,Int16,Int16, use_last_error=False)(47, 'InvokeTuningWizardEx', ((1, 'hwndParent'),(1, 'fAllowAudio'),(1, 'fAllowVideo'),)))
    IRTCClient2.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(48, 'get_Version', ((1, 'plVersion'),)))
    IRTCClient2.put_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(49, 'put_ClientName', ((1, 'bstrClientName'),)))
    IRTCClient2.put_ClientCurVer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(50, 'put_ClientCurVer', ((1, 'bstrClientCurVer'),)))
    IRTCClient2.InitializeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(51, 'InitializeEx', ((1, 'lFlags'),)))
    IRTCClient2.CreateSessionWithDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(52, 'CreateSessionWithDescription', ((1, 'bstrContentType'),(1, 'bstrSessionDescription'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppSession2'),)))
    IRTCClient2.SetSessionDescriptionManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCSessionDescriptionManager_head, use_last_error=False)(53, 'SetSessionDescriptionManager', ((1, 'pSessionDescriptionManager'),)))
    IRTCClient2.put_PreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL, use_last_error=False)(54, 'put_PreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'enSecurityLevel'),)))
    IRTCClient2.get_PreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL), use_last_error=False)(55, 'get_PreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'penSecurityLevel'),)))
    IRTCClient2.put_AllowedPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.RealTimeCommunications.RTC_LISTEN_MODE, use_last_error=False)(56, 'put_AllowedPorts', ((1, 'lTransport'),(1, 'enListenMode'),)))
    IRTCClient2.get_AllowedPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.RealTimeCommunications.RTC_LISTEN_MODE), use_last_error=False)(57, 'get_AllowedPorts', ((1, 'lTransport'),(1, 'penListenMode'),)))
    return IRTCClient2
def _define_IRTCClientPresence_head():
    class IRTCClientPresence(win32more.System.Com.IUnknown_head):
        Guid = Guid('11c3cbcc-0744-42d1-968a-51aa1bb274c6')
    return IRTCClientPresence
def _define_IRTCClientPresence():
    IRTCClientPresence = win32more.System.RealTimeCommunications.IRTCClientPresence_head
    IRTCClientPresence.EnablePresence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.System.Com.VARIANT, use_last_error=False)(3, 'EnablePresence', ((1, 'fUseStorage'),(1, 'varStorage'),)))
    IRTCClientPresence.Export = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(4, 'Export', ((1, 'varStorage'),)))
    IRTCClientPresence.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int16, use_last_error=False)(5, 'Import', ((1, 'varStorage'),(1, 'fReplaceAll'),)))
    IRTCClientPresence.EnumerateBuddies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head), use_last_error=False)(6, 'EnumerateBuddies', ((1, 'ppEnum'),)))
    IRTCClientPresence.get_Buddies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(7, 'get_Buddies', ((1, 'ppCollection'),)))
    IRTCClientPresence.get_Buddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head), use_last_error=False)(8, 'get_Buddy', ((1, 'bstrPresentityURI'),(1, 'ppBuddy'),)))
    IRTCClientPresence.AddBuddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head), use_last_error=False)(9, 'AddBuddy', ((1, 'bstrPresentityURI'),(1, 'bstrUserName'),(1, 'bstrData'),(1, 'fPersistent'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppBuddy'),)))
    IRTCClientPresence.RemoveBuddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCBuddy_head, use_last_error=False)(10, 'RemoveBuddy', ((1, 'pBuddy'),)))
    IRTCClientPresence.EnumerateWatchers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumWatchers_head), use_last_error=False)(11, 'EnumerateWatchers', ((1, 'ppEnum'),)))
    IRTCClientPresence.get_Watchers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(12, 'get_Watchers', ((1, 'ppCollection'),)))
    IRTCClientPresence.get_Watcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head), use_last_error=False)(13, 'get_Watcher', ((1, 'bstrPresentityURI'),(1, 'ppWatcher'),)))
    IRTCClientPresence.AddWatcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head), use_last_error=False)(14, 'AddWatcher', ((1, 'bstrPresentityURI'),(1, 'bstrUserName'),(1, 'bstrData'),(1, 'fBlocked'),(1, 'fPersistent'),(1, 'ppWatcher'),)))
    IRTCClientPresence.RemoveWatcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCWatcher_head, use_last_error=False)(15, 'RemoveWatcher', ((1, 'pWatcher'),)))
    IRTCClientPresence.SetLocalPresenceInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS,win32more.Foundation.BSTR, use_last_error=False)(16, 'SetLocalPresenceInfo', ((1, 'enStatus'),(1, 'bstrNotes'),)))
    IRTCClientPresence.get_OfferWatcherMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE), use_last_error=False)(17, 'get_OfferWatcherMode', ((1, 'penMode'),)))
    IRTCClientPresence.put_OfferWatcherMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE, use_last_error=False)(18, 'put_OfferWatcherMode', ((1, 'enMode'),)))
    IRTCClientPresence.get_PrivacyMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRIVACY_MODE), use_last_error=False)(19, 'get_PrivacyMode', ((1, 'penMode'),)))
    IRTCClientPresence.put_PrivacyMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRIVACY_MODE, use_last_error=False)(20, 'put_PrivacyMode', ((1, 'enMode'),)))
    return IRTCClientPresence
def _define_IRTCClientPresence2_head():
    class IRTCClientPresence2(win32more.System.RealTimeCommunications.IRTCClientPresence_head):
        Guid = Guid('ad1809e8-62f7-4783-909a-29c9d2cb1d34')
    return IRTCClientPresence2
def _define_IRTCClientPresence2():
    IRTCClientPresence2 = win32more.System.RealTimeCommunications.IRTCClientPresence2_head
    IRTCClientPresence2.EnablePresenceEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCProfile_head,win32more.System.Com.VARIANT,Int32, use_last_error=False)(21, 'EnablePresenceEx', ((1, 'pProfile'),(1, 'varStorage'),(1, 'lFlags'),)))
    IRTCClientPresence2.DisablePresence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'DisablePresence', ()))
    IRTCClientPresence2.AddGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head), use_last_error=False)(23, 'AddGroup', ((1, 'bstrGroupName'),(1, 'bstrData'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppGroup'),)))
    IRTCClientPresence2.RemoveGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCBuddyGroup_head, use_last_error=False)(24, 'RemoveGroup', ((1, 'pGroup'),)))
    IRTCClientPresence2.EnumerateGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head), use_last_error=False)(25, 'EnumerateGroups', ((1, 'ppEnum'),)))
    IRTCClientPresence2.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(26, 'get_Groups', ((1, 'ppCollection'),)))
    IRTCClientPresence2.get_Group = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head), use_last_error=False)(27, 'get_Group', ((1, 'bstrGroupName'),(1, 'ppGroup'),)))
    IRTCClientPresence2.AddWatcherEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.RTC_WATCHER_STATE,Int16,win32more.System.RealTimeCommunications.RTC_ACE_SCOPE,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher2_head), use_last_error=False)(28, 'AddWatcherEx', ((1, 'bstrPresentityURI'),(1, 'bstrUserName'),(1, 'bstrData'),(1, 'enState'),(1, 'fPersistent'),(1, 'enScope'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppWatcher'),)))
    IRTCClientPresence2.get_WatcherEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_WATCHER_MATCH_MODE,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher2_head), use_last_error=False)(29, 'get_WatcherEx', ((1, 'enMode'),(1, 'bstrPresentityURI'),(1, 'ppWatcher'),)))
    IRTCClientPresence2.put_PresenceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY,win32more.Foundation.BSTR, use_last_error=False)(30, 'put_PresenceProperty', ((1, 'enProperty'),(1, 'bstrProperty'),)))
    IRTCClientPresence2.get_PresenceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_PresenceProperty', ((1, 'enProperty'),(1, 'pbstrProperty'),)))
    IRTCClientPresence2.SetPresenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(32, 'SetPresenceData', ((1, 'bstrNamespace'),(1, 'bstrData'),)))
    IRTCClientPresence2.GetPresenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'GetPresenceData', ((1, 'pbstrNamespace'),(1, 'pbstrData'),)))
    IRTCClientPresence2.GetLocalPresenceInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS),POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'GetLocalPresenceInfo', ((1, 'penStatus'),(1, 'pbstrNotes'),)))
    IRTCClientPresence2.AddBuddyEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,win32more.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy2_head), use_last_error=False)(35, 'AddBuddyEx', ((1, 'bstrPresentityURI'),(1, 'bstrUserName'),(1, 'bstrData'),(1, 'fPersistent'),(1, 'enSubscriptionType'),(1, 'pProfile'),(1, 'lFlags'),(1, 'ppBuddy'),)))
    return IRTCClientPresence2
def _define_IRTCClientProvisioning_head():
    class IRTCClientProvisioning(win32more.System.Com.IUnknown_head):
        Guid = Guid('b9f5cf06-65b9-4a80-a0e6-73cae3ef3822')
    return IRTCClientProvisioning
def _define_IRTCClientProvisioning():
    IRTCClientProvisioning = win32more.System.RealTimeCommunications.IRTCClientProvisioning_head
    IRTCClientProvisioning.CreateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head), use_last_error=False)(3, 'CreateProfile', ((1, 'bstrProfileXML'),(1, 'ppProfile'),)))
    IRTCClientProvisioning.EnableProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32, use_last_error=False)(4, 'EnableProfile', ((1, 'pProfile'),(1, 'lRegisterFlags'),)))
    IRTCClientProvisioning.DisableProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCProfile_head, use_last_error=False)(5, 'DisableProfile', ((1, 'pProfile'),)))
    IRTCClientProvisioning.EnumerateProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumProfiles_head), use_last_error=False)(6, 'EnumerateProfiles', ((1, 'ppEnum'),)))
    IRTCClientProvisioning.get_Profiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(7, 'get_Profiles', ((1, 'ppCollection'),)))
    IRTCClientProvisioning.GetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,IntPtr, use_last_error=False)(8, 'GetProfile', ((1, 'bstrUserAccount'),(1, 'bstrUserPassword'),(1, 'bstrUserURI'),(1, 'bstrServer'),(1, 'lTransport'),(1, 'lCookie'),)))
    IRTCClientProvisioning.get_SessionCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_SessionCapabilities', ((1, 'plSupportedSessions'),)))
    return IRTCClientProvisioning
def _define_IRTCClientProvisioning2_head():
    class IRTCClientProvisioning2(win32more.System.RealTimeCommunications.IRTCClientProvisioning_head):
        Guid = Guid('a70909b5-f40e-4587-bb75-e6bc0845023e')
    return IRTCClientProvisioning2
def _define_IRTCClientProvisioning2():
    IRTCClientProvisioning2 = win32more.System.RealTimeCommunications.IRTCClientProvisioning2_head
    IRTCClientProvisioning2.EnableProfileEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32,Int32, use_last_error=False)(10, 'EnableProfileEx', ((1, 'pProfile'),(1, 'lRegisterFlags'),(1, 'lRoamingFlags'),)))
    return IRTCClientProvisioning2
def _define_IRTCProfile_head():
    class IRTCProfile(win32more.System.Com.IUnknown_head):
        Guid = Guid('d07eca9e-4062-4dd4-9e7d-722a49ba7303')
    return IRTCProfile
def _define_IRTCProfile():
    IRTCProfile = win32more.System.RealTimeCommunications.IRTCProfile_head
    IRTCProfile.get_Key = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Key', ((1, 'pbstrKey'),)))
    IRTCProfile.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_Name', ((1, 'pbstrName'),)))
    IRTCProfile.get_XML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_XML', ((1, 'pbstrXML'),)))
    IRTCProfile.get_ProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_ProviderName', ((1, 'pbstrName'),)))
    IRTCProfile.get_ProviderURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PROVIDER_URI,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ProviderURI', ((1, 'enURI'),(1, 'pbstrURI'),)))
    IRTCProfile.get_ProviderData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ProviderData', ((1, 'pbstrData'),)))
    IRTCProfile.get_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ClientName', ((1, 'pbstrName'),)))
    IRTCProfile.get_ClientBanner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_ClientBanner', ((1, 'pfBanner'),)))
    IRTCProfile.get_ClientMinVer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ClientMinVer', ((1, 'pbstrMinVer'),)))
    IRTCProfile.get_ClientCurVer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_ClientCurVer', ((1, 'pbstrCurVer'),)))
    IRTCProfile.get_ClientUpdateURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_ClientUpdateURI', ((1, 'pbstrUpdateURI'),)))
    IRTCProfile.get_ClientData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_ClientData', ((1, 'pbstrData'),)))
    IRTCProfile.get_UserURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_UserURI', ((1, 'pbstrUserURI'),)))
    IRTCProfile.get_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_UserName', ((1, 'pbstrUserName'),)))
    IRTCProfile.get_UserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_UserAccount', ((1, 'pbstrUserAccount'),)))
    IRTCProfile.SetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(18, 'SetCredentials', ((1, 'bstrUserURI'),(1, 'bstrUserAccount'),(1, 'bstrPassword'),)))
    IRTCProfile.get_SessionCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_SessionCapabilities', ((1, 'plSupportedSessions'),)))
    IRTCProfile.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_REGISTRATION_STATE), use_last_error=False)(20, 'get_State', ((1, 'penState'),)))
    return IRTCProfile
def _define_IRTCProfile2_head():
    class IRTCProfile2(win32more.System.RealTimeCommunications.IRTCProfile_head):
        Guid = Guid('4b81f84e-bdc7-4184-9154-3cb2dd7917fb')
    return IRTCProfile2
def _define_IRTCProfile2():
    IRTCProfile2 = win32more.System.RealTimeCommunications.IRTCProfile2_head
    IRTCProfile2.get_Realm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_Realm', ((1, 'pbstrRealm'),)))
    IRTCProfile2.put_Realm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_Realm', ((1, 'bstrRealm'),)))
    IRTCProfile2.get_AllowedAuth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_AllowedAuth', ((1, 'plAllowedAuth'),)))
    IRTCProfile2.put_AllowedAuth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_AllowedAuth', ((1, 'lAllowedAuth'),)))
    return IRTCProfile2
def _define_IRTCSession_head():
    class IRTCSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('387c8086-99be-42fb-9973-7c0fc0ca9fa8')
    return IRTCSession
def _define_IRTCSession():
    IRTCSession = win32more.System.RealTimeCommunications.IRTCSession_head
    IRTCSession.get_Client = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCClient_head), use_last_error=False)(3, 'get_Client', ((1, 'ppClient'),)))
    IRTCSession.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_STATE), use_last_error=False)(4, 'get_State', ((1, 'penState'),)))
    IRTCSession.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_TYPE), use_last_error=False)(5, 'get_Type', ((1, 'penType'),)))
    IRTCSession.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head), use_last_error=False)(6, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCSession.get_Participants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(7, 'get_Participants', ((1, 'ppCollection'),)))
    IRTCSession.Answer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Answer', ()))
    IRTCSession.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_TERMINATE_REASON, use_last_error=False)(9, 'Terminate', ((1, 'enReason'),)))
    IRTCSession.Redirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SESSION_TYPE,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.IRTCProfile_head,Int32, use_last_error=False)(10, 'Redirect', ((1, 'enType'),(1, 'bstrLocalPhoneURI'),(1, 'pProfile'),(1, 'lFlags'),)))
    IRTCSession.AddParticipant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), use_last_error=False)(11, 'AddParticipant', ((1, 'bstrAddress'),(1, 'bstrName'),(1, 'ppParticipant'),)))
    IRTCSession.RemoveParticipant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCParticipant_head, use_last_error=False)(12, 'RemoveParticipant', ((1, 'pParticipant'),)))
    IRTCSession.EnumerateParticipants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumParticipants_head), use_last_error=False)(13, 'EnumerateParticipants', ((1, 'ppEnum'),)))
    IRTCSession.get_CanAddParticipants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_CanAddParticipants', ((1, 'pfCanAdd'),)))
    IRTCSession.get_RedirectedUserURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_RedirectedUserURI', ((1, 'pbstrUserURI'),)))
    IRTCSession.get_RedirectedUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_RedirectedUserName', ((1, 'pbstrUserName'),)))
    IRTCSession.NextRedirectedUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'NextRedirectedUser', ()))
    IRTCSession.SendMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,IntPtr, use_last_error=False)(18, 'SendMessage', ((1, 'bstrMessageHeader'),(1, 'bstrMessage'),(1, 'lCookie'),)))
    IRTCSession.SendMessageStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS,IntPtr, use_last_error=False)(19, 'SendMessageStatus', ((1, 'enUserStatus'),(1, 'lCookie'),)))
    IRTCSession.AddStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,IntPtr, use_last_error=False)(20, 'AddStream', ((1, 'lMediaType'),(1, 'lCookie'),)))
    IRTCSession.RemoveStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,IntPtr, use_last_error=False)(21, 'RemoveStream', ((1, 'lMediaType'),(1, 'lCookie'),)))
    IRTCSession.put_EncryptionKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_EncryptionKey', ((1, 'lMediaType'),(1, 'EncryptionKey'),)))
    return IRTCSession
def _define_IRTCSession2_head():
    class IRTCSession2(win32more.System.RealTimeCommunications.IRTCSession_head):
        Guid = Guid('17d7cdfc-b007-484c-99d2-86a8a820991d')
    return IRTCSession2
def _define_IRTCSession2():
    IRTCSession2 = win32more.System.RealTimeCommunications.IRTCSession2_head
    IRTCSession2.SendInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,IntPtr, use_last_error=False)(23, 'SendInfo', ((1, 'bstrInfoHeader'),(1, 'bstrInfo'),(1, 'lCookie'),)))
    IRTCSession2.put_PreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL, use_last_error=False)(24, 'put_PreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'enSecurityLevel'),)))
    IRTCSession2.get_PreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL), use_last_error=False)(25, 'get_PreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'penSecurityLevel'),)))
    IRTCSession2.IsSecurityEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,POINTER(Int16), use_last_error=False)(26, 'IsSecurityEnabled', ((1, 'enSecurityType'),(1, 'pfSecurityEnabled'),)))
    IRTCSession2.AnswerWithSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(27, 'AnswerWithSessionDescription', ((1, 'bstrContentType'),(1, 'bstrSessionDescription'),)))
    IRTCSession2.ReInviteWithSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,IntPtr, use_last_error=False)(28, 'ReInviteWithSessionDescription', ((1, 'bstrContentType'),(1, 'bstrSessionDescription'),(1, 'lCookie'),)))
    return IRTCSession2
def _define_IRTCSessionCallControl_head():
    class IRTCSessionCallControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('e9a50d94-190b-4f82-9530-3b8ebf60758a')
    return IRTCSessionCallControl
def _define_IRTCSessionCallControl():
    IRTCSessionCallControl = win32more.System.RealTimeCommunications.IRTCSessionCallControl_head
    IRTCSessionCallControl.Hold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(3, 'Hold', ((1, 'lCookie'),)))
    IRTCSessionCallControl.UnHold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(4, 'UnHold', ((1, 'lCookie'),)))
    IRTCSessionCallControl.Forward = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(5, 'Forward', ((1, 'bstrForwardToURI'),)))
    IRTCSessionCallControl.Refer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(6, 'Refer', ((1, 'bstrReferToURI'),(1, 'bstrReferCookie'),)))
    IRTCSessionCallControl.put_ReferredByURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'put_ReferredByURI', ((1, 'bstrReferredByURI'),)))
    IRTCSessionCallControl.get_ReferredByURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ReferredByURI', ((1, 'pbstrReferredByURI'),)))
    IRTCSessionCallControl.put_ReferCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'put_ReferCookie', ((1, 'bstrReferCookie'),)))
    IRTCSessionCallControl.get_ReferCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_ReferCookie', ((1, 'pbstrReferCookie'),)))
    IRTCSessionCallControl.get_IsReferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_IsReferred', ((1, 'pfIsReferred'),)))
    return IRTCSessionCallControl
def _define_IRTCParticipant_head():
    class IRTCParticipant(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae86add5-26b1-4414-af1d-b94cd938d739')
    return IRTCParticipant
def _define_IRTCParticipant():
    IRTCParticipant = win32more.System.RealTimeCommunications.IRTCParticipant_head
    IRTCParticipant.get_UserURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_UserURI', ((1, 'pbstrUserURI'),)))
    IRTCParticipant.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_Name', ((1, 'pbstrName'),)))
    IRTCParticipant.get_Removable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(5, 'get_Removable', ((1, 'pfRemovable'),)))
    IRTCParticipant.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PARTICIPANT_STATE), use_last_error=False)(6, 'get_State', ((1, 'penState'),)))
    IRTCParticipant.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    return IRTCParticipant
def _define_IRTCRoamingEvent_head():
    class IRTCRoamingEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('79960a6b-0cb1-4dc8-a805-7318e99902e8')
    return IRTCRoamingEvent
def _define_IRTCRoamingEvent():
    IRTCRoamingEvent = win32more.System.RealTimeCommunications.IRTCRoamingEvent_head
    IRTCRoamingEvent.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_ROAMING_EVENT_TYPE), use_last_error=False)(7, 'get_EventType', ((1, 'pEventType'),)))
    IRTCRoamingEvent.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head), use_last_error=False)(8, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCRoamingEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCRoamingEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCRoamingEvent
def _define_IRTCProfileEvent_head():
    class IRTCProfileEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d6d5ab3b-770e-43e8-800a-79b062395fca')
    return IRTCProfileEvent
def _define_IRTCProfileEvent():
    IRTCProfileEvent = win32more.System.RealTimeCommunications.IRTCProfileEvent_head
    IRTCProfileEvent.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head), use_last_error=False)(7, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCProfileEvent.get_Cookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr), use_last_error=False)(8, 'get_Cookie', ((1, 'plCookie'),)))
    IRTCProfileEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    return IRTCProfileEvent
def _define_IRTCProfileEvent2_head():
    class IRTCProfileEvent2(win32more.System.RealTimeCommunications.IRTCProfileEvent_head):
        Guid = Guid('62e56edc-03fa-4121-94fb-23493fd0ae64')
    return IRTCProfileEvent2
def _define_IRTCProfileEvent2():
    IRTCProfileEvent2 = win32more.System.RealTimeCommunications.IRTCProfileEvent2_head
    IRTCProfileEvent2.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PROFILE_EVENT_TYPE), use_last_error=False)(10, 'get_EventType', ((1, 'pEventType'),)))
    return IRTCProfileEvent2
def _define_IRTCClientEvent_head():
    class IRTCClientEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('2b493b7a-3cba-4170-9c8b-76a9dacdd644')
    return IRTCClientEvent
def _define_IRTCClientEvent():
    IRTCClientEvent = win32more.System.RealTimeCommunications.IRTCClientEvent_head
    IRTCClientEvent.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_CLIENT_EVENT_TYPE), use_last_error=False)(7, 'get_EventType', ((1, 'penEventType'),)))
    IRTCClientEvent.get_Client = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCClient_head), use_last_error=False)(8, 'get_Client', ((1, 'ppClient'),)))
    return IRTCClientEvent
def _define_IRTCRegistrationStateChangeEvent_head():
    class IRTCRegistrationStateChangeEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('62d0991b-50ab-4f02-b948-ca94f26f8f95')
    return IRTCRegistrationStateChangeEvent
def _define_IRTCRegistrationStateChangeEvent():
    IRTCRegistrationStateChangeEvent = win32more.System.RealTimeCommunications.IRTCRegistrationStateChangeEvent_head
    IRTCRegistrationStateChangeEvent.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head), use_last_error=False)(7, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCRegistrationStateChangeEvent.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_REGISTRATION_STATE), use_last_error=False)(8, 'get_State', ((1, 'penState'),)))
    IRTCRegistrationStateChangeEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCRegistrationStateChangeEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCRegistrationStateChangeEvent
def _define_IRTCSessionStateChangeEvent_head():
    class IRTCSessionStateChangeEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('b5bad703-5952-48b3-9321-7f4500521506')
    return IRTCSessionStateChangeEvent
def _define_IRTCSessionStateChangeEvent():
    IRTCSessionStateChangeEvent = win32more.System.RealTimeCommunications.IRTCSessionStateChangeEvent_head
    IRTCSessionStateChangeEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCSessionStateChangeEvent.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_STATE), use_last_error=False)(8, 'get_State', ((1, 'penState'),)))
    IRTCSessionStateChangeEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCSessionStateChangeEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCSessionStateChangeEvent
def _define_IRTCSessionStateChangeEvent2_head():
    class IRTCSessionStateChangeEvent2(win32more.System.RealTimeCommunications.IRTCSessionStateChangeEvent_head):
        Guid = Guid('4f933171-6f95-4880-80d9-2ec8d495d261')
    return IRTCSessionStateChangeEvent2
def _define_IRTCSessionStateChangeEvent2():
    IRTCSessionStateChangeEvent2 = win32more.System.RealTimeCommunications.IRTCSessionStateChangeEvent2_head
    IRTCSessionStateChangeEvent2.get_MediaTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_MediaTypes', ((1, 'pMediaTypes'),)))
    IRTCSessionStateChangeEvent2.get_RemotePreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL), use_last_error=False)(12, 'get_RemotePreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'penSecurityLevel'),)))
    IRTCSessionStateChangeEvent2.get_IsForked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_IsForked', ((1, 'pfIsForked'),)))
    IRTCSessionStateChangeEvent2.GetRemoteSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetRemoteSessionDescription', ((1, 'pbstrContentType'),(1, 'pbstrSessionDescription'),)))
    return IRTCSessionStateChangeEvent2
def _define_IRTCSessionOperationCompleteEvent_head():
    class IRTCSessionOperationCompleteEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('a6bff4c0-f7c8-4d3c-9a41-3550f78a95b0')
    return IRTCSessionOperationCompleteEvent
def _define_IRTCSessionOperationCompleteEvent():
    IRTCSessionOperationCompleteEvent = win32more.System.RealTimeCommunications.IRTCSessionOperationCompleteEvent_head
    IRTCSessionOperationCompleteEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCSessionOperationCompleteEvent.get_Cookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr), use_last_error=False)(8, 'get_Cookie', ((1, 'plCookie'),)))
    IRTCSessionOperationCompleteEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCSessionOperationCompleteEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCSessionOperationCompleteEvent
def _define_IRTCSessionOperationCompleteEvent2_head():
    class IRTCSessionOperationCompleteEvent2(win32more.System.RealTimeCommunications.IRTCSessionOperationCompleteEvent_head):
        Guid = Guid('f6fc2a9b-d5bc-4241-b436-1b8460c13832')
    return IRTCSessionOperationCompleteEvent2
def _define_IRTCSessionOperationCompleteEvent2():
    IRTCSessionOperationCompleteEvent2 = win32more.System.RealTimeCommunications.IRTCSessionOperationCompleteEvent2_head
    IRTCSessionOperationCompleteEvent2.get_Participant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), use_last_error=False)(11, 'get_Participant', ((1, 'ppParticipant'),)))
    IRTCSessionOperationCompleteEvent2.GetRemoteSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetRemoteSessionDescription', ((1, 'pbstrContentType'),(1, 'pbstrSessionDescription'),)))
    return IRTCSessionOperationCompleteEvent2
def _define_IRTCParticipantStateChangeEvent_head():
    class IRTCParticipantStateChangeEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('09bcb597-f0fa-48f9-b420-468cea7fde04')
    return IRTCParticipantStateChangeEvent
def _define_IRTCParticipantStateChangeEvent():
    IRTCParticipantStateChangeEvent = win32more.System.RealTimeCommunications.IRTCParticipantStateChangeEvent_head
    IRTCParticipantStateChangeEvent.get_Participant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), use_last_error=False)(7, 'get_Participant', ((1, 'ppParticipant'),)))
    IRTCParticipantStateChangeEvent.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PARTICIPANT_STATE), use_last_error=False)(8, 'get_State', ((1, 'penState'),)))
    IRTCParticipantStateChangeEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    return IRTCParticipantStateChangeEvent
def _define_IRTCMediaEvent_head():
    class IRTCMediaEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('099944fb-bcda-453e-8c41-e13da2adf7f3')
    return IRTCMediaEvent
def _define_IRTCMediaEvent():
    IRTCMediaEvent = win32more.System.RealTimeCommunications.IRTCMediaEvent_head
    IRTCMediaEvent.get_MediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_MediaType', ((1, 'pMediaType'),)))
    IRTCMediaEvent.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_MEDIA_EVENT_TYPE), use_last_error=False)(8, 'get_EventType', ((1, 'penEventType'),)))
    IRTCMediaEvent.get_EventReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_MEDIA_EVENT_REASON), use_last_error=False)(9, 'get_EventReason', ((1, 'penEventReason'),)))
    return IRTCMediaEvent
def _define_IRTCIntensityEvent_head():
    class IRTCIntensityEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('4c23bf51-390c-4992-a41d-41eec05b2a4b')
    return IRTCIntensityEvent
def _define_IRTCIntensityEvent():
    IRTCIntensityEvent = win32more.System.RealTimeCommunications.IRTCIntensityEvent_head
    IRTCIntensityEvent.get_Level = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Level', ((1, 'plLevel'),)))
    IRTCIntensityEvent.get_Min = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Min', ((1, 'plMin'),)))
    IRTCIntensityEvent.get_Max = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Max', ((1, 'plMax'),)))
    IRTCIntensityEvent.get_Direction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE), use_last_error=False)(10, 'get_Direction', ((1, 'penDirection'),)))
    return IRTCIntensityEvent
def _define_IRTCMessagingEvent_head():
    class IRTCMessagingEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d3609541-1b29-4de5-a4ad-5aebaf319512')
    return IRTCMessagingEvent
def _define_IRTCMessagingEvent():
    IRTCMessagingEvent = win32more.System.RealTimeCommunications.IRTCMessagingEvent_head
    IRTCMessagingEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCMessagingEvent.get_Participant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), use_last_error=False)(8, 'get_Participant', ((1, 'ppParticipant'),)))
    IRTCMessagingEvent.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_MESSAGING_EVENT_TYPE), use_last_error=False)(9, 'get_EventType', ((1, 'penEventType'),)))
    IRTCMessagingEvent.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Message', ((1, 'pbstrMessage'),)))
    IRTCMessagingEvent.get_MessageHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_MessageHeader', ((1, 'pbstrMessageHeader'),)))
    IRTCMessagingEvent.get_UserStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS), use_last_error=False)(12, 'get_UserStatus', ((1, 'penUserStatus'),)))
    return IRTCMessagingEvent
def _define_IRTCBuddyEvent_head():
    class IRTCBuddyEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('f36d755d-17e6-404e-954f-0fc07574c78d')
    return IRTCBuddyEvent
def _define_IRTCBuddyEvent():
    IRTCBuddyEvent = win32more.System.RealTimeCommunications.IRTCBuddyEvent_head
    IRTCBuddyEvent.get_Buddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head), use_last_error=False)(7, 'get_Buddy', ((1, 'ppBuddy'),)))
    return IRTCBuddyEvent
def _define_IRTCBuddyEvent2_head():
    class IRTCBuddyEvent2(win32more.System.RealTimeCommunications.IRTCBuddyEvent_head):
        Guid = Guid('484a7f1e-73f0-4990-bfc2-60bc3978a720')
    return IRTCBuddyEvent2
def _define_IRTCBuddyEvent2():
    IRTCBuddyEvent2 = win32more.System.RealTimeCommunications.IRTCBuddyEvent2_head
    IRTCBuddyEvent2.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_BUDDY_EVENT_TYPE), use_last_error=False)(8, 'get_EventType', ((1, 'pEventType'),)))
    IRTCBuddyEvent2.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCBuddyEvent2.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCBuddyEvent2
def _define_IRTCWatcherEvent_head():
    class IRTCWatcherEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('f30d7261-587a-424f-822c-312788f43548')
    return IRTCWatcherEvent
def _define_IRTCWatcherEvent():
    IRTCWatcherEvent = win32more.System.RealTimeCommunications.IRTCWatcherEvent_head
    IRTCWatcherEvent.get_Watcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head), use_last_error=False)(7, 'get_Watcher', ((1, 'ppWatcher'),)))
    return IRTCWatcherEvent
def _define_IRTCWatcherEvent2_head():
    class IRTCWatcherEvent2(win32more.System.RealTimeCommunications.IRTCWatcherEvent_head):
        Guid = Guid('e52891e8-188c-49af-b005-98ed13f83f9c')
    return IRTCWatcherEvent2
def _define_IRTCWatcherEvent2():
    IRTCWatcherEvent2 = win32more.System.RealTimeCommunications.IRTCWatcherEvent2_head
    IRTCWatcherEvent2.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_WATCHER_EVENT_TYPE), use_last_error=False)(8, 'get_EventType', ((1, 'pEventType'),)))
    IRTCWatcherEvent2.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    return IRTCWatcherEvent2
def _define_IRTCBuddyGroupEvent_head():
    class IRTCBuddyGroupEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('3a79e1d1-b736-4414-96f8-bbc7f08863e4')
    return IRTCBuddyGroupEvent
def _define_IRTCBuddyGroupEvent():
    IRTCBuddyGroupEvent = win32more.System.RealTimeCommunications.IRTCBuddyGroupEvent_head
    IRTCBuddyGroupEvent.get_EventType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_GROUP_EVENT_TYPE), use_last_error=False)(7, 'get_EventType', ((1, 'pEventType'),)))
    IRTCBuddyGroupEvent.get_Group = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head), use_last_error=False)(8, 'get_Group', ((1, 'ppGroup'),)))
    IRTCBuddyGroupEvent.get_Buddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy2_head), use_last_error=False)(9, 'get_Buddy', ((1, 'ppBuddy'),)))
    IRTCBuddyGroupEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_StatusCode', ((1, 'plStatusCode'),)))
    return IRTCBuddyGroupEvent
def _define_IRTCInfoEvent_head():
    class IRTCInfoEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('4e1d68ae-1912-4f49-b2c3-594fadfd425f')
    return IRTCInfoEvent
def _define_IRTCInfoEvent():
    IRTCInfoEvent = win32more.System.RealTimeCommunications.IRTCInfoEvent_head
    IRTCInfoEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCInfoEvent.get_Participant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), use_last_error=False)(8, 'get_Participant', ((1, 'ppParticipant'),)))
    IRTCInfoEvent.get_Info = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Info', ((1, 'pbstrInfo'),)))
    IRTCInfoEvent.get_InfoHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_InfoHeader', ((1, 'pbstrInfoHeader'),)))
    return IRTCInfoEvent
def _define_IRTCMediaRequestEvent_head():
    class IRTCMediaRequestEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('52572d15-148c-4d97-a36c-2da55c289d63')
    return IRTCMediaRequestEvent
def _define_IRTCMediaRequestEvent():
    IRTCMediaRequestEvent = win32more.System.RealTimeCommunications.IRTCMediaRequestEvent_head
    IRTCMediaRequestEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCMediaRequestEvent.get_ProposedMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ProposedMedia', ((1, 'plMediaTypes'),)))
    IRTCMediaRequestEvent.get_CurrentMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_CurrentMedia', ((1, 'plMediaTypes'),)))
    IRTCMediaRequestEvent.Accept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Accept', ((1, 'lMediaTypes'),)))
    IRTCMediaRequestEvent.get_RemotePreferredSecurityLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE,POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL), use_last_error=False)(11, 'get_RemotePreferredSecurityLevel', ((1, 'enSecurityType'),(1, 'penSecurityLevel'),)))
    IRTCMediaRequestEvent.Reject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Reject', ()))
    IRTCMediaRequestEvent.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_REINVITE_STATE), use_last_error=False)(13, 'get_State', ((1, 'pState'),)))
    return IRTCMediaRequestEvent
def _define_IRTCReInviteEvent_head():
    class IRTCReInviteEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('11558d84-204c-43e7-99b0-2034e9417f7d')
    return IRTCReInviteEvent
def _define_IRTCReInviteEvent():
    IRTCReInviteEvent = win32more.System.RealTimeCommunications.IRTCReInviteEvent_head
    IRTCReInviteEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession2'),)))
    IRTCReInviteEvent.Accept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(8, 'Accept', ((1, 'bstrContentType'),(1, 'bstrSessionDescription'),)))
    IRTCReInviteEvent.Reject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Reject', ()))
    IRTCReInviteEvent.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_REINVITE_STATE), use_last_error=False)(10, 'get_State', ((1, 'pState'),)))
    IRTCReInviteEvent.GetRemoteSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetRemoteSessionDescription', ((1, 'pbstrContentType'),(1, 'pbstrSessionDescription'),)))
    return IRTCReInviteEvent
def _define_IRTCPresencePropertyEvent_head():
    class IRTCPresencePropertyEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('f777f570-a820-49d5-86bd-e099493f1518')
    return IRTCPresencePropertyEvent
def _define_IRTCPresencePropertyEvent():
    IRTCPresencePropertyEvent = win32more.System.RealTimeCommunications.IRTCPresencePropertyEvent_head
    IRTCPresencePropertyEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCPresencePropertyEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    IRTCPresencePropertyEvent.get_PresenceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY), use_last_error=False)(9, 'get_PresenceProperty', ((1, 'penPresProp'),)))
    IRTCPresencePropertyEvent.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Value', ((1, 'pbstrValue'),)))
    return IRTCPresencePropertyEvent
def _define_IRTCPresenceDataEvent_head():
    class IRTCPresenceDataEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('38f0e78c-8b87-4c04-a82d-aedd83c909bb')
    return IRTCPresenceDataEvent
def _define_IRTCPresenceDataEvent():
    IRTCPresenceDataEvent = win32more.System.RealTimeCommunications.IRTCPresenceDataEvent_head
    IRTCPresenceDataEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCPresenceDataEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    IRTCPresenceDataEvent.GetPresenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetPresenceData', ((1, 'pbstrNamespace'),(1, 'pbstrData'),)))
    return IRTCPresenceDataEvent
def _define_IRTCPresenceStatusEvent_head():
    class IRTCPresenceStatusEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('78673f32-4a0f-462c-89aa-ee7706707678')
    return IRTCPresenceStatusEvent
def _define_IRTCPresenceStatusEvent():
    IRTCPresenceStatusEvent = win32more.System.RealTimeCommunications.IRTCPresenceStatusEvent_head
    IRTCPresenceStatusEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCPresenceStatusEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    IRTCPresenceStatusEvent.GetLocalPresenceInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS),POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetLocalPresenceInfo', ((1, 'penStatus'),(1, 'pbstrNotes'),)))
    return IRTCPresenceStatusEvent
def _define_IRTCCollection_head():
    class IRTCCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('ec7c8096-b918-4044-94f1-e4fba0361d5c')
    return IRTCCollection
def _define_IRTCCollection():
    IRTCCollection = win32more.System.RealTimeCommunications.IRTCCollection_head
    IRTCCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'lCount'),)))
    IRTCCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'Index'),(1, 'pVariant'),)))
    IRTCCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppNewEnum'),)))
    return IRTCCollection
def _define_IRTCEnumParticipants_head():
    class IRTCEnumParticipants(win32more.System.Com.IUnknown_head):
        Guid = Guid('fcd56f29-4a4f-41b2-ba5c-f5bccc060bf6')
    return IRTCEnumParticipants
def _define_IRTCEnumParticipants():
    IRTCEnumParticipants = win32more.System.RealTimeCommunications.IRTCEnumParticipants_head
    IRTCEnumParticipants.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumParticipants.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumParticipants.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumParticipants.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumParticipants_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumParticipants
def _define_IRTCEnumProfiles_head():
    class IRTCEnumProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('29b7c41c-ed82-4bca-84ad-39d5101b58e3')
    return IRTCEnumProfiles
def _define_IRTCEnumProfiles():
    IRTCEnumProfiles = win32more.System.RealTimeCommunications.IRTCEnumProfiles_head
    IRTCEnumProfiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumProfiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumProfiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumProfiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumProfiles_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumProfiles
def _define_IRTCEnumBuddies_head():
    class IRTCEnumBuddies(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7296917-5569-4b3b-b3af-98d1144b2b87')
    return IRTCEnumBuddies
def _define_IRTCEnumBuddies():
    IRTCEnumBuddies = win32more.System.RealTimeCommunications.IRTCEnumBuddies_head
    IRTCEnumBuddies.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumBuddies.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumBuddies.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumBuddies.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumBuddies
def _define_IRTCEnumWatchers_head():
    class IRTCEnumWatchers(win32more.System.Com.IUnknown_head):
        Guid = Guid('a87d55d7-db74-4ed1-9ca4-77a0e41b413e')
    return IRTCEnumWatchers
def _define_IRTCEnumWatchers():
    IRTCEnumWatchers = win32more.System.RealTimeCommunications.IRTCEnumWatchers_head
    IRTCEnumWatchers.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumWatchers.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumWatchers.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumWatchers.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumWatchers_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumWatchers
def _define_IRTCEnumGroups_head():
    class IRTCEnumGroups(win32more.System.Com.IUnknown_head):
        Guid = Guid('742378d6-a141-4415-8f27-35d99076cf5d')
    return IRTCEnumGroups
def _define_IRTCEnumGroups():
    IRTCEnumGroups = win32more.System.RealTimeCommunications.IRTCEnumGroups_head
    IRTCEnumGroups.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumGroups.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumGroups.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumGroups.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumGroups
def _define_IRTCPresenceContact_head():
    class IRTCPresenceContact(win32more.System.Com.IUnknown_head):
        Guid = Guid('8b22f92c-cd90-42db-a733-212205c3e3df')
    return IRTCPresenceContact
def _define_IRTCPresenceContact():
    IRTCPresenceContact = win32more.System.RealTimeCommunications.IRTCPresenceContact_head
    IRTCPresenceContact.get_PresentityURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_PresentityURI', ((1, 'pbstrPresentityURI'),)))
    IRTCPresenceContact.put_PresentityURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'put_PresentityURI', ((1, 'bstrPresentityURI'),)))
    IRTCPresenceContact.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_Name', ((1, 'pbstrName'),)))
    IRTCPresenceContact.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(6, 'put_Name', ((1, 'bstrName'),)))
    IRTCPresenceContact.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Data', ((1, 'pbstrData'),)))
    IRTCPresenceContact.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Data', ((1, 'bstrData'),)))
    IRTCPresenceContact.get_Persistent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_Persistent', ((1, 'pfPersistent'),)))
    IRTCPresenceContact.put_Persistent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_Persistent', ((1, 'fPersistent'),)))
    return IRTCPresenceContact
def _define_IRTCBuddy_head():
    class IRTCBuddy(win32more.System.RealTimeCommunications.IRTCPresenceContact_head):
        Guid = Guid('fcb136c8-7b90-4e0c-befe-56edf0ba6f1c')
    return IRTCBuddy
def _define_IRTCBuddy():
    IRTCBuddy = win32more.System.RealTimeCommunications.IRTCBuddy_head
    IRTCBuddy.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS), use_last_error=False)(11, 'get_Status', ((1, 'penStatus'),)))
    IRTCBuddy.get_Notes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Notes', ((1, 'pbstrNotes'),)))
    return IRTCBuddy
def _define_IRTCBuddy2_head():
    class IRTCBuddy2(win32more.System.RealTimeCommunications.IRTCBuddy_head):
        Guid = Guid('102f9588-23e7-40e3-954d-cd7a1d5c0361')
    return IRTCBuddy2
def _define_IRTCBuddy2():
    IRTCBuddy2 = win32more.System.RealTimeCommunications.IRTCBuddy2_head
    IRTCBuddy2.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head), use_last_error=False)(13, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCBuddy2.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Refresh', ()))
    IRTCBuddy2.EnumerateGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head), use_last_error=False)(15, 'EnumerateGroups', ((1, 'ppEnum'),)))
    IRTCBuddy2.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(16, 'get_Groups', ((1, 'ppCollection'),)))
    IRTCBuddy2.get_PresenceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_PresenceProperty', ((1, 'enProperty'),(1, 'pbstrProperty'),)))
    IRTCBuddy2.EnumeratePresenceDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumPresenceDevices_head), use_last_error=False)(18, 'EnumeratePresenceDevices', ((1, 'ppEnumDevices'),)))
    IRTCBuddy2.get_PresenceDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(19, 'get_PresenceDevices', ((1, 'ppDevicesCollection'),)))
    IRTCBuddy2.get_SubscriptionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE), use_last_error=False)(20, 'get_SubscriptionType', ((1, 'penSubscriptionType'),)))
    return IRTCBuddy2
def _define_IRTCWatcher_head():
    class IRTCWatcher(win32more.System.RealTimeCommunications.IRTCPresenceContact_head):
        Guid = Guid('c7cedad8-346b-4d1b-ac02-a2088df9be4f')
    return IRTCWatcher
def _define_IRTCWatcher():
    IRTCWatcher = win32more.System.RealTimeCommunications.IRTCWatcher_head
    IRTCWatcher.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_WATCHER_STATE), use_last_error=False)(11, 'get_State', ((1, 'penState'),)))
    IRTCWatcher.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_WATCHER_STATE, use_last_error=False)(12, 'put_State', ((1, 'enState'),)))
    return IRTCWatcher
def _define_IRTCWatcher2_head():
    class IRTCWatcher2(win32more.System.RealTimeCommunications.IRTCWatcher_head):
        Guid = Guid('d4d9967f-d011-4b1d-91e3-aba78f96393d')
    return IRTCWatcher2
def _define_IRTCWatcher2():
    IRTCWatcher2 = win32more.System.RealTimeCommunications.IRTCWatcher2_head
    IRTCWatcher2.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head), use_last_error=False)(13, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCWatcher2.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_ACE_SCOPE), use_last_error=False)(14, 'get_Scope', ((1, 'penScope'),)))
    return IRTCWatcher2
def _define_IRTCBuddyGroup_head():
    class IRTCBuddyGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('60361e68-9164-4389-a4c6-d0b3925bda5e')
    return IRTCBuddyGroup
def _define_IRTCBuddyGroup():
    IRTCBuddyGroup = win32more.System.RealTimeCommunications.IRTCBuddyGroup_head
    IRTCBuddyGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Name', ((1, 'pbstrGroupName'),)))
    IRTCBuddyGroup.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'put_Name', ((1, 'bstrGroupName'),)))
    IRTCBuddyGroup.AddBuddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCBuddy_head, use_last_error=False)(5, 'AddBuddy', ((1, 'pBuddy'),)))
    IRTCBuddyGroup.RemoveBuddy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCBuddy_head, use_last_error=False)(6, 'RemoveBuddy', ((1, 'pBuddy'),)))
    IRTCBuddyGroup.EnumerateBuddies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head), use_last_error=False)(7, 'EnumerateBuddies', ((1, 'ppEnum'),)))
    IRTCBuddyGroup.get_Buddies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(8, 'get_Buddies', ((1, 'ppCollection'),)))
    IRTCBuddyGroup.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Data', ((1, 'pbstrData'),)))
    IRTCBuddyGroup.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Data', ((1, 'bstrData'),)))
    IRTCBuddyGroup.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head), use_last_error=False)(11, 'get_Profile', ((1, 'ppProfile'),)))
    return IRTCBuddyGroup
def _define_IRTCEventNotification_head():
    class IRTCEventNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('13fa24c7-5748-4b21-91f5-7397609ce747')
    return IRTCEventNotification
def _define_IRTCEventNotification():
    IRTCEventNotification = win32more.System.RealTimeCommunications.IRTCEventNotification_head
    IRTCEventNotification.Event = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_EVENT,win32more.System.Com.IDispatch_head, use_last_error=False)(3, 'Event', ((1, 'RTCEvent'),(1, 'pEvent'),)))
    return IRTCEventNotification
def _define_IRTCPortManager_head():
    class IRTCPortManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('da77c14b-6208-43ca-8ddf-5b60a0a69fac')
    return IRTCPortManager
def _define_IRTCPortManager():
    IRTCPortManager = win32more.System.RealTimeCommunications.IRTCPortManager_head
    IRTCPortManager.GetMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.RealTimeCommunications.RTC_PORT_TYPE,POINTER(win32more.Foundation.BSTR),POINTER(Int32),POINTER(win32more.Foundation.BSTR),POINTER(Int32), use_last_error=False)(3, 'GetMapping', ((1, 'bstrRemoteAddress'),(1, 'enPortType'),(1, 'pbstrInternalLocalAddress'),(1, 'plInternalLocalPort'),(1, 'pbstrExternalLocalAddress'),(1, 'plExternalLocalPort'),)))
    IRTCPortManager.UpdateRemoteAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int32, use_last_error=False)(4, 'UpdateRemoteAddress', ((1, 'bstrRemoteAddress'),(1, 'bstrInternalLocalAddress'),(1, 'lInternalLocalPort'),(1, 'bstrExternalLocalAddress'),(1, 'lExternalLocalPort'),)))
    IRTCPortManager.ReleaseMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int32, use_last_error=False)(5, 'ReleaseMapping', ((1, 'bstrInternalLocalAddress'),(1, 'lInternalLocalPort'),(1, 'bstrExternalLocalAddress'),(1, 'lExternalLocalAddress'),)))
    return IRTCPortManager
def _define_IRTCSessionPortManagement_head():
    class IRTCSessionPortManagement(win32more.System.Com.IUnknown_head):
        Guid = Guid('a072f1d6-0286-4e1f-85f2-17a2948456ec')
    return IRTCSessionPortManagement
def _define_IRTCSessionPortManagement():
    IRTCSessionPortManagement = win32more.System.RealTimeCommunications.IRTCSessionPortManagement_head
    IRTCSessionPortManagement.SetPortManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCPortManager_head, use_last_error=False)(3, 'SetPortManager', ((1, 'pPortManager'),)))
    return IRTCSessionPortManagement
def _define_IRTCClientPortManagement_head():
    class IRTCClientPortManagement(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5df3f03-4bde-4417-aefe-71177bdaea66')
    return IRTCClientPortManagement
def _define_IRTCClientPortManagement():
    IRTCClientPortManagement = win32more.System.RealTimeCommunications.IRTCClientPortManagement_head
    IRTCClientPortManagement.StartListenAddressAndPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(3, 'StartListenAddressAndPort', ((1, 'bstrInternalLocalAddress'),(1, 'lInternalLocalPort'),)))
    IRTCClientPortManagement.StopListenAddressAndPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(4, 'StopListenAddressAndPort', ((1, 'bstrInternalLocalAddress'),(1, 'lInternalLocalPort'),)))
    IRTCClientPortManagement.GetPortRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PORT_TYPE,POINTER(Int32),POINTER(Int32), use_last_error=False)(5, 'GetPortRange', ((1, 'enPortType'),(1, 'plMinValue'),(1, 'plMaxValue'),)))
    return IRTCClientPortManagement
def _define_IRTCUserSearch_head():
    class IRTCUserSearch(win32more.System.Com.IUnknown_head):
        Guid = Guid('b619882b-860c-4db4-be1b-693b6505bbe5')
    return IRTCUserSearch
def _define_IRTCUserSearch():
    IRTCUserSearch = win32more.System.RealTimeCommunications.IRTCUserSearch_head
    IRTCUserSearch.CreateQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head), use_last_error=False)(3, 'CreateQuery', ((1, 'ppQuery'),)))
    IRTCUserSearch.ExecuteSearch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head,win32more.System.RealTimeCommunications.IRTCProfile_head,IntPtr, use_last_error=False)(4, 'ExecuteSearch', ((1, 'pQuery'),(1, 'pProfile'),(1, 'lCookie'),)))
    return IRTCUserSearch
def _define_IRTCUserSearchQuery_head():
    class IRTCUserSearchQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('288300f5-d23a-4365-9a73-9985c98c2881')
    return IRTCUserSearchQuery
def _define_IRTCUserSearchQuery():
    IRTCUserSearchQuery = win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head
    IRTCUserSearchQuery.put_SearchTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(3, 'put_SearchTerm', ((1, 'bstrName'),(1, 'bstrValue'),)))
    IRTCUserSearchQuery.get_SearchTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_SearchTerm', ((1, 'bstrName'),(1, 'pbstrValue'),)))
    IRTCUserSearchQuery.get_SearchTerms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_SearchTerms', ((1, 'pbstrNames'),)))
    IRTCUserSearchQuery.put_SearchPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE,Int32, use_last_error=False)(6, 'put_SearchPreference', ((1, 'enPreference'),(1, 'lValue'),)))
    IRTCUserSearchQuery.get_SearchPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE,POINTER(Int32), use_last_error=False)(7, 'get_SearchPreference', ((1, 'enPreference'),(1, 'plValue'),)))
    IRTCUserSearchQuery.put_SearchDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_SearchDomain', ((1, 'bstrDomain'),)))
    IRTCUserSearchQuery.get_SearchDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_SearchDomain', ((1, 'pbstrDomain'),)))
    return IRTCUserSearchQuery
def _define_IRTCUserSearchResult_head():
    class IRTCUserSearchResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('851278b2-9592-480f-8db5-2de86b26b54d')
    return IRTCUserSearchResult
def _define_IRTCUserSearchResult():
    IRTCUserSearchResult = win32more.System.RealTimeCommunications.IRTCUserSearchResult_head
    IRTCUserSearchResult.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_USER_SEARCH_COLUMN,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Value', ((1, 'enColumn'),(1, 'pbstrValue'),)))
    return IRTCUserSearchResult
def _define_IRTCEnumUserSearchResults_head():
    class IRTCEnumUserSearchResults(win32more.System.Com.IUnknown_head):
        Guid = Guid('83d4d877-aa5d-4a5b-8d0e-002a8067e0e8')
    return IRTCEnumUserSearchResults
def _define_IRTCEnumUserSearchResults():
    IRTCEnumUserSearchResults = win32more.System.RealTimeCommunications.IRTCEnumUserSearchResults_head
    IRTCEnumUserSearchResults.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchResult_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumUserSearchResults.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumUserSearchResults.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumUserSearchResults.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumUserSearchResults_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumUserSearchResults
def _define_IRTCUserSearchResultsEvent_head():
    class IRTCUserSearchResultsEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d8c8c3cd-7fac-4088-81c5-c24cbc0938e3')
    return IRTCUserSearchResultsEvent
def _define_IRTCUserSearchResultsEvent():
    IRTCUserSearchResultsEvent = win32more.System.RealTimeCommunications.IRTCUserSearchResultsEvent_head
    IRTCUserSearchResultsEvent.EnumerateResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumUserSearchResults_head), use_last_error=False)(7, 'EnumerateResults', ((1, 'ppEnum'),)))
    IRTCUserSearchResultsEvent.get_Results = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head), use_last_error=False)(8, 'get_Results', ((1, 'ppCollection'),)))
    IRTCUserSearchResultsEvent.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head), use_last_error=False)(9, 'get_Profile', ((1, 'ppProfile'),)))
    IRTCUserSearchResultsEvent.get_Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head), use_last_error=False)(10, 'get_Query', ((1, 'ppQuery'),)))
    IRTCUserSearchResultsEvent.get_Cookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr), use_last_error=False)(11, 'get_Cookie', ((1, 'plCookie'),)))
    IRTCUserSearchResultsEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCUserSearchResultsEvent.get_MoreAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_MoreAvailable', ((1, 'pfMoreAvailable'),)))
    return IRTCUserSearchResultsEvent
def _define_IRTCSessionReferStatusEvent_head():
    class IRTCSessionReferStatusEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('3d8fc2cd-5d76-44ab-bb68-2a80353b34a2')
    return IRTCSessionReferStatusEvent
def _define_IRTCSessionReferStatusEvent():
    IRTCSessionReferStatusEvent = win32more.System.RealTimeCommunications.IRTCSessionReferStatusEvent_head
    IRTCSessionReferStatusEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCSessionReferStatusEvent.get_ReferStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_REFER_STATUS), use_last_error=False)(8, 'get_ReferStatus', ((1, 'penReferStatus'),)))
    IRTCSessionReferStatusEvent.get_StatusCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_StatusCode', ((1, 'plStatusCode'),)))
    IRTCSessionReferStatusEvent.get_StatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StatusText', ((1, 'pbstrStatusText'),)))
    return IRTCSessionReferStatusEvent
def _define_IRTCSessionReferredEvent_head():
    class IRTCSessionReferredEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('176a6828-4fcc-4f28-a862-04597a6cf1c4')
    return IRTCSessionReferredEvent
def _define_IRTCSessionReferredEvent():
    IRTCSessionReferredEvent = win32more.System.RealTimeCommunications.IRTCSessionReferredEvent_head
    IRTCSessionReferredEvent.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head), use_last_error=False)(7, 'get_Session', ((1, 'ppSession'),)))
    IRTCSessionReferredEvent.get_ReferredByURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_ReferredByURI', ((1, 'pbstrReferredByURI'),)))
    IRTCSessionReferredEvent.get_ReferToURI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ReferToURI', ((1, 'pbstrReferoURI'),)))
    IRTCSessionReferredEvent.get_ReferCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_ReferCookie', ((1, 'pbstrReferCookie'),)))
    IRTCSessionReferredEvent.Accept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Accept', ()))
    IRTCSessionReferredEvent.Reject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Reject', ()))
    IRTCSessionReferredEvent.SetReferredSessionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_SESSION_STATE, use_last_error=False)(13, 'SetReferredSessionState', ((1, 'enState'),)))
    return IRTCSessionReferredEvent
def _define_IRTCSessionDescriptionManager_head():
    class IRTCSessionDescriptionManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('ba7f518e-d336-4070-93a6-865395c843f9')
    return IRTCSessionDescriptionManager
def _define_IRTCSessionDescriptionManager():
    IRTCSessionDescriptionManager = win32more.System.RealTimeCommunications.IRTCSessionDescriptionManager_head
    IRTCSessionDescriptionManager.EvaluateSessionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(3, 'EvaluateSessionDescription', ((1, 'bstrContentType'),(1, 'bstrSessionDescription'),(1, 'pfApplicationSession'),)))
    return IRTCSessionDescriptionManager
def _define_IRTCEnumPresenceDevices_head():
    class IRTCEnumPresenceDevices(win32more.System.Com.IUnknown_head):
        Guid = Guid('708c2ab7-8bf8-42f8-8c7d-635197ad5539')
    return IRTCEnumPresenceDevices
def _define_IRTCEnumPresenceDevices():
    IRTCEnumPresenceDevices = win32more.System.RealTimeCommunications.IRTCEnumPresenceDevices_head
    IRTCEnumPresenceDevices.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.RealTimeCommunications.IRTCPresenceDevice_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'ppElements'),(1, 'pceltFetched'),)))
    IRTCEnumPresenceDevices.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IRTCEnumPresenceDevices.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Skip', ((1, 'celt'),)))
    IRTCEnumPresenceDevices.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.IRTCEnumPresenceDevices_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IRTCEnumPresenceDevices
def _define_IRTCPresenceDevice_head():
    class IRTCPresenceDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc6a90dd-ad9a-48da-9b0c-2515e38521ad')
    return IRTCPresenceDevice
def _define_IRTCPresenceDevice():
    IRTCPresenceDevice = win32more.System.RealTimeCommunications.IRTCPresenceDevice_head
    IRTCPresenceDevice.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS), use_last_error=False)(3, 'get_Status', ((1, 'penStatus'),)))
    IRTCPresenceDevice.get_Notes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_Notes', ((1, 'pbstrNotes'),)))
    IRTCPresenceDevice.get_PresenceProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_PresenceProperty', ((1, 'enProperty'),(1, 'pbstrProperty'),)))
    IRTCPresenceDevice.GetPresenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetPresenceData', ((1, 'pbstrNamespace'),(1, 'pbstrData'),)))
    return IRTCPresenceDevice
def _define_IRTCDispatchEventNotification_head():
    class IRTCDispatchEventNotification(win32more.System.Com.IDispatch_head):
        Guid = Guid('176ddfbe-fec0-4d55-bc87-84cff1ef7f91')
    return IRTCDispatchEventNotification
def _define_IRTCDispatchEventNotification():
    IRTCDispatchEventNotification = win32more.System.RealTimeCommunications.IRTCDispatchEventNotification_head
    return IRTCDispatchEventNotification
def _define_TRANSPORT_SETTING_head():
    class TRANSPORT_SETTING(Structure):
        pass
    return TRANSPORT_SETTING
def _define_TRANSPORT_SETTING():
    TRANSPORT_SETTING = win32more.System.RealTimeCommunications.TRANSPORT_SETTING_head
    TRANSPORT_SETTING._fields_ = [
        ("SettingId", win32more.Networking.WinSock.TRANSPORT_SETTING_ID),
        ("Length", POINTER(UInt32)),
        ("Value", c_char_p_no),
    ]
    return TRANSPORT_SETTING
def _define_ITransportSettingsInternal_head():
    class ITransportSettingsInternal(win32more.System.Com.IUnknown_head):
        Guid = Guid('5123e076-29e3-4bfd-84fe-0192d411e3e8')
    return ITransportSettingsInternal
def _define_ITransportSettingsInternal():
    ITransportSettingsInternal = win32more.System.RealTimeCommunications.ITransportSettingsInternal_head
    ITransportSettingsInternal.ApplySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.TRANSPORT_SETTING_head), use_last_error=False)(3, 'ApplySetting', ((1, 'Setting'),)))
    ITransportSettingsInternal.QuerySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RealTimeCommunications.TRANSPORT_SETTING_head), use_last_error=False)(4, 'QuerySetting', ((1, 'Setting'),)))
    return ITransportSettingsInternal
def _define_INetworkTransportSettings_head():
    class INetworkTransportSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e7abb2c-f2c1-4a61-bd35-deb7a08ab0f1')
    return INetworkTransportSettings
def _define_INetworkTransportSettings():
    INetworkTransportSettings = win32more.System.RealTimeCommunications.INetworkTransportSettings_head
    INetworkTransportSettings.ApplySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WinSock.TRANSPORT_SETTING_ID_head),UInt32,POINTER(Byte),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(3, 'ApplySetting', ((1, 'SettingId'),(1, 'LengthIn'),(1, 'ValueIn'),(1, 'LengthOut'),(1, 'ValueOut'),)))
    INetworkTransportSettings.QuerySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WinSock.TRANSPORT_SETTING_ID_head),UInt32,POINTER(Byte),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(4, 'QuerySetting', ((1, 'SettingId'),(1, 'LengthIn'),(1, 'ValueIn'),(1, 'LengthOut'),(1, 'ValueOut'),)))
    return INetworkTransportSettings
def _define_INotificationTransportSync_head():
    class INotificationTransportSync(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eb1402-0ab8-49c0-9e14-a1ae4ba93058')
    return INotificationTransportSync
def _define_INotificationTransportSync():
    INotificationTransportSync = win32more.System.RealTimeCommunications.INotificationTransportSync_head
    INotificationTransportSync.CompleteDelivery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'CompleteDelivery', ()))
    INotificationTransportSync.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Flush', ()))
    return INotificationTransportSync
__all__ = [
    "RTCCS_FORCE_PROFILE",
    "RTCCS_FAIL_ON_REDIRECT",
    "RTCMT_AUDIO_SEND",
    "RTCMT_AUDIO_RECEIVE",
    "RTCMT_VIDEO_SEND",
    "RTCMT_VIDEO_RECEIVE",
    "RTCMT_T120_SENDRECV",
    "RTCSI_PC_TO_PC",
    "RTCSI_PC_TO_PHONE",
    "RTCSI_PHONE_TO_PHONE",
    "RTCSI_IM",
    "RTCSI_MULTIPARTY_IM",
    "RTCSI_APPLICATION",
    "RTCTR_UDP",
    "RTCTR_TCP",
    "RTCTR_TLS",
    "RTCAU_BASIC",
    "RTCAU_DIGEST",
    "RTCAU_NTLM",
    "RTCAU_KERBEROS",
    "RTCAU_USE_LOGON_CRED",
    "RTCRF_REGISTER_INVITE_SESSIONS",
    "RTCRF_REGISTER_MESSAGE_SESSIONS",
    "RTCRF_REGISTER_PRESENCE",
    "RTCRF_REGISTER_NOTIFY",
    "RTCRF_REGISTER_ALL",
    "RTCRMF_BUDDY_ROAMING",
    "RTCRMF_WATCHER_ROAMING",
    "RTCRMF_PRESENCE_ROAMING",
    "RTCRMF_PROFILE_ROAMING",
    "RTCRMF_ALL_ROAMING",
    "RTCEF_CLIENT",
    "RTCEF_REGISTRATION_STATE_CHANGE",
    "RTCEF_SESSION_STATE_CHANGE",
    "RTCEF_SESSION_OPERATION_COMPLETE",
    "RTCEF_PARTICIPANT_STATE_CHANGE",
    "RTCEF_MEDIA",
    "RTCEF_INTENSITY",
    "RTCEF_MESSAGING",
    "RTCEF_BUDDY",
    "RTCEF_WATCHER",
    "RTCEF_PROFILE",
    "RTCEF_USERSEARCH",
    "RTCEF_INFO",
    "RTCEF_GROUP",
    "RTCEF_MEDIA_REQUEST",
    "RTCEF_ROAMING",
    "RTCEF_PRESENCE_PROPERTY",
    "RTCEF_BUDDY2",
    "RTCEF_WATCHER2",
    "RTCEF_SESSION_REFER_STATUS",
    "RTCEF_SESSION_REFERRED",
    "RTCEF_REINVITE",
    "RTCEF_PRESENCE_DATA",
    "RTCEF_PRESENCE_STATUS",
    "RTCEF_ALL",
    "RTCIF_DISABLE_MEDIA",
    "RTCIF_DISABLE_UPNP",
    "RTCIF_ENABLE_SERVER_CLASS",
    "RTCIF_DISABLE_STRICT_DNS",
    "FACILITY_RTC_INTERFACE",
    "FACILITY_SIP_STATUS_CODE",
    "FACILITY_PINT_STATUS_CODE",
    "STATUS_SEVERITY_RTC_ERROR",
    "RTC_E_SIP_CODECS_DO_NOT_MATCH",
    "RTC_E_SIP_STREAM_PRESENT",
    "RTC_E_SIP_STREAM_NOT_PRESENT",
    "RTC_E_SIP_NO_STREAM",
    "RTC_E_SIP_PARSE_FAILED",
    "RTC_E_SIP_HEADER_NOT_PRESENT",
    "RTC_E_SDP_NOT_PRESENT",
    "RTC_E_SDP_PARSE_FAILED",
    "RTC_E_SDP_UPDATE_FAILED",
    "RTC_E_SDP_MULTICAST",
    "RTC_E_SDP_CONNECTION_ADDR",
    "RTC_E_SDP_NO_MEDIA",
    "RTC_E_SIP_TIMEOUT",
    "RTC_E_SDP_FAILED_TO_BUILD",
    "RTC_E_SIP_INVITE_TRANSACTION_PENDING",
    "RTC_E_SIP_AUTH_HEADER_SENT",
    "RTC_E_SIP_AUTH_TYPE_NOT_SUPPORTED",
    "RTC_E_SIP_AUTH_FAILED",
    "RTC_E_INVALID_SIP_URL",
    "RTC_E_DESTINATION_ADDRESS_LOCAL",
    "RTC_E_INVALID_ADDRESS_LOCAL",
    "RTC_E_DESTINATION_ADDRESS_MULTICAST",
    "RTC_E_INVALID_PROXY_ADDRESS",
    "RTC_E_SIP_TRANSPORT_NOT_SUPPORTED",
    "RTC_E_SIP_NEED_MORE_DATA",
    "RTC_E_SIP_CALL_DISCONNECTED",
    "RTC_E_SIP_REQUEST_DESTINATION_ADDR_NOT_PRESENT",
    "RTC_E_SIP_UDP_SIZE_EXCEEDED",
    "RTC_E_SIP_SSL_TUNNEL_FAILED",
    "RTC_E_SIP_SSL_NEGOTIATION_TIMEOUT",
    "RTC_E_SIP_STACK_SHUTDOWN",
    "RTC_E_MEDIA_CONTROLLER_STATE",
    "RTC_E_MEDIA_NEED_TERMINAL",
    "RTC_E_MEDIA_AUDIO_DEVICE_NOT_AVAILABLE",
    "RTC_E_MEDIA_VIDEO_DEVICE_NOT_AVAILABLE",
    "RTC_E_START_STREAM",
    "RTC_E_MEDIA_AEC",
    "RTC_E_CLIENT_NOT_INITIALIZED",
    "RTC_E_CLIENT_ALREADY_INITIALIZED",
    "RTC_E_CLIENT_ALREADY_SHUT_DOWN",
    "RTC_E_PRESENCE_NOT_ENABLED",
    "RTC_E_INVALID_SESSION_TYPE",
    "RTC_E_INVALID_SESSION_STATE",
    "RTC_E_NO_PROFILE",
    "RTC_E_LOCAL_PHONE_NEEDED",
    "RTC_E_NO_DEVICE",
    "RTC_E_INVALID_PROFILE",
    "RTC_E_PROFILE_NO_PROVISION",
    "RTC_E_PROFILE_NO_KEY",
    "RTC_E_PROFILE_NO_NAME",
    "RTC_E_PROFILE_NO_USER",
    "RTC_E_PROFILE_NO_USER_URI",
    "RTC_E_PROFILE_NO_SERVER",
    "RTC_E_PROFILE_NO_SERVER_ADDRESS",
    "RTC_E_PROFILE_NO_SERVER_PROTOCOL",
    "RTC_E_PROFILE_INVALID_SERVER_PROTOCOL",
    "RTC_E_PROFILE_INVALID_SERVER_AUTHMETHOD",
    "RTC_E_PROFILE_INVALID_SERVER_ROLE",
    "RTC_E_PROFILE_MULTIPLE_REGISTRARS",
    "RTC_E_PROFILE_INVALID_SESSION",
    "RTC_E_PROFILE_INVALID_SESSION_PARTY",
    "RTC_E_PROFILE_INVALID_SESSION_TYPE",
    "RTC_E_OPERATION_WITH_TOO_MANY_PARTICIPANTS",
    "RTC_E_BASIC_AUTH_SET_TLS",
    "RTC_E_SIP_HIGH_SECURITY_SET_TLS",
    "RTC_S_ROAMING_NOT_SUPPORTED",
    "RTC_E_PROFILE_SERVER_UNAUTHORIZED",
    "RTC_E_DUPLICATE_REALM",
    "RTC_E_POLICY_NOT_ALLOW",
    "RTC_E_PORT_MAPPING_UNAVAILABLE",
    "RTC_E_PORT_MAPPING_FAILED",
    "RTC_E_SECURITY_LEVEL_NOT_COMPATIBLE",
    "RTC_E_SECURITY_LEVEL_NOT_DEFINED",
    "RTC_E_SECURITY_LEVEL_NOT_SUPPORTED_BY_PARTICIPANT",
    "RTC_E_DUPLICATE_BUDDY",
    "RTC_E_DUPLICATE_WATCHER",
    "RTC_E_MALFORMED_XML",
    "RTC_E_ROAMING_OPERATION_INTERRUPTED",
    "RTC_E_ROAMING_FAILED",
    "RTC_E_INVALID_BUDDY_LIST",
    "RTC_E_INVALID_ACL_LIST",
    "RTC_E_NO_GROUP",
    "RTC_E_DUPLICATE_GROUP",
    "RTC_E_TOO_MANY_GROUPS",
    "RTC_E_NO_BUDDY",
    "RTC_E_NO_WATCHER",
    "RTC_E_NO_REALM",
    "RTC_E_NO_TRANSPORT",
    "RTC_E_NOT_EXIST",
    "RTC_E_INVALID_PREFERENCE_LIST",
    "RTC_E_MAX_PENDING_OPERATIONS",
    "RTC_E_TOO_MANY_RETRIES",
    "RTC_E_INVALID_PORTRANGE",
    "RTC_E_SIP_CALL_CONNECTION_NOT_ESTABLISHED",
    "RTC_E_SIP_ADDITIONAL_PARTY_IN_TWO_PARTY_SESSION",
    "RTC_E_SIP_PARTY_ALREADY_IN_SESSION",
    "RTC_E_SIP_OTHER_PARTY_JOIN_IN_PROGRESS",
    "RTC_E_INVALID_OBJECT_STATE",
    "RTC_E_PRESENCE_ENABLED",
    "RTC_E_ROAMING_ENABLED",
    "RTC_E_SIP_TLS_INCOMPATIBLE_ENCRYPTION",
    "RTC_E_SIP_INVALID_CERTIFICATE",
    "RTC_E_SIP_DNS_FAIL",
    "RTC_E_SIP_TCP_FAIL",
    "RTC_E_TOO_SMALL_EXPIRES_VALUE",
    "RTC_E_SIP_TLS_FAIL",
    "RTC_E_NOT_PRESENCE_PROFILE",
    "RTC_E_SIP_INVITEE_PARTY_TIMEOUT",
    "RTC_E_SIP_AUTH_TIME_SKEW",
    "RTC_E_INVALID_REGISTRATION_STATE",
    "RTC_E_MEDIA_DISABLED",
    "RTC_E_MEDIA_ENABLED",
    "RTC_E_REFER_NOT_ACCEPTED",
    "RTC_E_REFER_NOT_ALLOWED",
    "RTC_E_REFER_NOT_EXIST",
    "RTC_E_SIP_HOLD_OPERATION_PENDING",
    "RTC_E_SIP_UNHOLD_OPERATION_PENDING",
    "RTC_E_MEDIA_SESSION_NOT_EXIST",
    "RTC_E_MEDIA_SESSION_IN_HOLD",
    "RTC_E_ANOTHER_MEDIA_SESSION_ACTIVE",
    "RTC_E_MAX_REDIRECTS",
    "RTC_E_REDIRECT_PROCESSING_FAILED",
    "RTC_E_LISTENING_SOCKET_NOT_EXIST",
    "RTC_E_INVALID_LISTEN_SOCKET",
    "RTC_E_PORT_MANAGER_ALREADY_SET",
    "RTC_E_SECURITY_LEVEL_ALREADY_SET",
    "RTC_E_UDP_NOT_SUPPORTED",
    "RTC_E_SIP_REFER_OPERATION_PENDING",
    "RTC_E_PLATFORM_NOT_SUPPORTED",
    "RTC_E_SIP_PEER_PARTICIPANT_IN_MULTIPARTY_SESSION",
    "RTC_E_NOT_ALLOWED",
    "RTC_E_REGISTRATION_DEACTIVATED",
    "RTC_E_REGISTRATION_REJECTED",
    "RTC_E_REGISTRATION_UNREGISTERED",
    "RTC_E_STATUS_INFO_TRYING",
    "RTC_E_STATUS_INFO_RINGING",
    "RTC_E_STATUS_INFO_CALL_FORWARDING",
    "RTC_E_STATUS_INFO_QUEUED",
    "RTC_E_STATUS_SESSION_PROGRESS",
    "RTC_E_STATUS_SUCCESS",
    "RTC_E_STATUS_REDIRECT_MULTIPLE_CHOICES",
    "RTC_E_STATUS_REDIRECT_MOVED_PERMANENTLY",
    "RTC_E_STATUS_REDIRECT_MOVED_TEMPORARILY",
    "RTC_E_STATUS_REDIRECT_SEE_OTHER",
    "RTC_E_STATUS_REDIRECT_USE_PROXY",
    "RTC_E_STATUS_REDIRECT_ALTERNATIVE_SERVICE",
    "RTC_E_STATUS_CLIENT_BAD_REQUEST",
    "RTC_E_STATUS_CLIENT_UNAUTHORIZED",
    "RTC_E_STATUS_CLIENT_PAYMENT_REQUIRED",
    "RTC_E_STATUS_CLIENT_FORBIDDEN",
    "RTC_E_STATUS_CLIENT_NOT_FOUND",
    "RTC_E_STATUS_CLIENT_METHOD_NOT_ALLOWED",
    "RTC_E_STATUS_CLIENT_NOT_ACCEPTABLE",
    "RTC_E_STATUS_CLIENT_PROXY_AUTHENTICATION_REQUIRED",
    "RTC_E_STATUS_CLIENT_REQUEST_TIMEOUT",
    "RTC_E_STATUS_CLIENT_CONFLICT",
    "RTC_E_STATUS_CLIENT_GONE",
    "RTC_E_STATUS_CLIENT_LENGTH_REQUIRED",
    "RTC_E_STATUS_CLIENT_REQUEST_ENTITY_TOO_LARGE",
    "RTC_E_STATUS_CLIENT_REQUEST_URI_TOO_LARGE",
    "RTC_E_STATUS_CLIENT_UNSUPPORTED_MEDIA_TYPE",
    "RTC_E_STATUS_CLIENT_BAD_EXTENSION",
    "RTC_E_STATUS_CLIENT_TEMPORARILY_NOT_AVAILABLE",
    "RTC_E_STATUS_CLIENT_TRANSACTION_DOES_NOT_EXIST",
    "RTC_E_STATUS_CLIENT_LOOP_DETECTED",
    "RTC_E_STATUS_CLIENT_TOO_MANY_HOPS",
    "RTC_E_STATUS_CLIENT_ADDRESS_INCOMPLETE",
    "RTC_E_STATUS_CLIENT_AMBIGUOUS",
    "RTC_E_STATUS_CLIENT_BUSY_HERE",
    "RTC_E_STATUS_REQUEST_TERMINATED",
    "RTC_E_STATUS_NOT_ACCEPTABLE_HERE",
    "RTC_E_STATUS_SERVER_INTERNAL_ERROR",
    "RTC_E_STATUS_SERVER_NOT_IMPLEMENTED",
    "RTC_E_STATUS_SERVER_BAD_GATEWAY",
    "RTC_E_STATUS_SERVER_SERVICE_UNAVAILABLE",
    "RTC_E_STATUS_SERVER_SERVER_TIMEOUT",
    "RTC_E_STATUS_SERVER_VERSION_NOT_SUPPORTED",
    "RTC_E_STATUS_GLOBAL_BUSY_EVERYWHERE",
    "RTC_E_STATUS_GLOBAL_DECLINE",
    "RTC_E_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE",
    "RTC_E_STATUS_GLOBAL_NOT_ACCEPTABLE",
    "RTC_E_PINT_STATUS_REJECTED_BUSY",
    "RTC_E_PINT_STATUS_REJECTED_NO_ANSWER",
    "RTC_E_PINT_STATUS_REJECTED_ALL_BUSY",
    "RTC_E_PINT_STATUS_REJECTED_PL_FAILED",
    "RTC_E_PINT_STATUS_REJECTED_SW_FAILED",
    "RTC_E_PINT_STATUS_REJECTED_CANCELLED",
    "RTC_E_PINT_STATUS_REJECTED_BADNUMBER",
    "RTCClient",
    "RTC_AUDIO_DEVICE",
    "RTCAD_SPEAKER",
    "RTCAD_MICROPHONE",
    "RTC_VIDEO_DEVICE",
    "RTCVD_RECEIVE",
    "RTCVD_PREVIEW",
    "RTC_EVENT",
    "RTCE_CLIENT",
    "RTCE_REGISTRATION_STATE_CHANGE",
    "RTCE_SESSION_STATE_CHANGE",
    "RTCE_SESSION_OPERATION_COMPLETE",
    "RTCE_PARTICIPANT_STATE_CHANGE",
    "RTCE_MEDIA",
    "RTCE_INTENSITY",
    "RTCE_MESSAGING",
    "RTCE_BUDDY",
    "RTCE_WATCHER",
    "RTCE_PROFILE",
    "RTCE_USERSEARCH",
    "RTCE_INFO",
    "RTCE_GROUP",
    "RTCE_MEDIA_REQUEST",
    "RTCE_ROAMING",
    "RTCE_PRESENCE_PROPERTY",
    "RTCE_PRESENCE_DATA",
    "RTCE_PRESENCE_STATUS",
    "RTCE_SESSION_REFER_STATUS",
    "RTCE_SESSION_REFERRED",
    "RTCE_REINVITE",
    "RTC_LISTEN_MODE",
    "RTCLM_NONE",
    "RTCLM_DYNAMIC",
    "RTCLM_BOTH",
    "RTC_CLIENT_EVENT_TYPE",
    "RTCCET_VOLUME_CHANGE",
    "RTCCET_DEVICE_CHANGE",
    "RTCCET_NETWORK_QUALITY_CHANGE",
    "RTCCET_ASYNC_CLEANUP_DONE",
    "RTC_BUDDY_EVENT_TYPE",
    "RTCBET_BUDDY_ADD",
    "RTCBET_BUDDY_REMOVE",
    "RTCBET_BUDDY_UPDATE",
    "RTCBET_BUDDY_STATE_CHANGE",
    "RTCBET_BUDDY_ROAMED",
    "RTCBET_BUDDY_SUBSCRIBED",
    "RTC_WATCHER_EVENT_TYPE",
    "RTCWET_WATCHER_ADD",
    "RTCWET_WATCHER_REMOVE",
    "RTCWET_WATCHER_UPDATE",
    "RTCWET_WATCHER_OFFERING",
    "RTCWET_WATCHER_ROAMED",
    "RTC_GROUP_EVENT_TYPE",
    "RTCGET_GROUP_ADD",
    "RTCGET_GROUP_REMOVE",
    "RTCGET_GROUP_UPDATE",
    "RTCGET_GROUP_BUDDY_ADD",
    "RTCGET_GROUP_BUDDY_REMOVE",
    "RTCGET_GROUP_ROAMED",
    "RTC_TERMINATE_REASON",
    "RTCTR_NORMAL",
    "RTCTR_DND",
    "RTCTR_BUSY",
    "RTCTR_REJECT",
    "RTCTR_TIMEOUT",
    "RTCTR_SHUTDOWN",
    "RTCTR_INSUFFICIENT_SECURITY_LEVEL",
    "RTCTR_NOT_SUPPORTED",
    "RTC_REGISTRATION_STATE",
    "RTCRS_NOT_REGISTERED",
    "RTCRS_REGISTERING",
    "RTCRS_REGISTERED",
    "RTCRS_REJECTED",
    "RTCRS_UNREGISTERING",
    "RTCRS_ERROR",
    "RTCRS_LOGGED_OFF",
    "RTCRS_LOCAL_PA_LOGGED_OFF",
    "RTCRS_REMOTE_PA_LOGGED_OFF",
    "RTC_SESSION_STATE",
    "RTCSS_IDLE",
    "RTCSS_INCOMING",
    "RTCSS_ANSWERING",
    "RTCSS_INPROGRESS",
    "RTCSS_CONNECTED",
    "RTCSS_DISCONNECTED",
    "RTCSS_HOLD",
    "RTCSS_REFER",
    "RTC_PARTICIPANT_STATE",
    "RTCPS_IDLE",
    "RTCPS_PENDING",
    "RTCPS_INCOMING",
    "RTCPS_ANSWERING",
    "RTCPS_INPROGRESS",
    "RTCPS_ALERTING",
    "RTCPS_CONNECTED",
    "RTCPS_DISCONNECTING",
    "RTCPS_DISCONNECTED",
    "RTC_WATCHER_STATE",
    "RTCWS_UNKNOWN",
    "RTCWS_OFFERING",
    "RTCWS_ALLOWED",
    "RTCWS_BLOCKED",
    "RTCWS_DENIED",
    "RTCWS_PROMPT",
    "RTC_ACE_SCOPE",
    "RTCAS_SCOPE_USER",
    "RTCAS_SCOPE_DOMAIN",
    "RTCAS_SCOPE_ALL",
    "RTC_OFFER_WATCHER_MODE",
    "RTCOWM_OFFER_WATCHER_EVENT",
    "RTCOWM_AUTOMATICALLY_ADD_WATCHER",
    "RTC_WATCHER_MATCH_MODE",
    "RTCWMM_EXACT_MATCH",
    "RTCWMM_BEST_ACE_MATCH",
    "RTC_PRIVACY_MODE",
    "RTCPM_BLOCK_LIST_EXCLUDED",
    "RTCPM_ALLOW_LIST_ONLY",
    "RTC_SESSION_TYPE",
    "RTCST_PC_TO_PC",
    "RTCST_PC_TO_PHONE",
    "RTCST_PHONE_TO_PHONE",
    "RTCST_IM",
    "RTCST_MULTIPARTY_IM",
    "RTCST_APPLICATION",
    "RTC_PRESENCE_STATUS",
    "RTCXS_PRESENCE_OFFLINE",
    "RTCXS_PRESENCE_ONLINE",
    "RTCXS_PRESENCE_AWAY",
    "RTCXS_PRESENCE_IDLE",
    "RTCXS_PRESENCE_BUSY",
    "RTCXS_PRESENCE_BE_RIGHT_BACK",
    "RTCXS_PRESENCE_ON_THE_PHONE",
    "RTCXS_PRESENCE_OUT_TO_LUNCH",
    "RTC_BUDDY_SUBSCRIPTION_TYPE",
    "RTCBT_SUBSCRIBED",
    "RTCBT_ALWAYS_OFFLINE",
    "RTCBT_ALWAYS_ONLINE",
    "RTCBT_POLL",
    "RTC_MEDIA_EVENT_TYPE",
    "RTCMET_STOPPED",
    "RTCMET_STARTED",
    "RTCMET_FAILED",
    "RTC_MEDIA_EVENT_REASON",
    "RTCMER_NORMAL",
    "RTCMER_HOLD",
    "RTCMER_TIMEOUT",
    "RTCMER_BAD_DEVICE",
    "RTCMER_NO_PORT",
    "RTCMER_PORT_MAPPING_FAILED",
    "RTCMER_REMOTE_REQUEST",
    "RTC_MESSAGING_EVENT_TYPE",
    "RTCMSET_MESSAGE",
    "RTCMSET_STATUS",
    "RTC_MESSAGING_USER_STATUS",
    "RTCMUS_IDLE",
    "RTCMUS_TYPING",
    "RTC_DTMF",
    "RTC_DTMF_0",
    "RTC_DTMF_1",
    "RTC_DTMF_2",
    "RTC_DTMF_3",
    "RTC_DTMF_4",
    "RTC_DTMF_5",
    "RTC_DTMF_6",
    "RTC_DTMF_7",
    "RTC_DTMF_8",
    "RTC_DTMF_9",
    "RTC_DTMF_STAR",
    "RTC_DTMF_POUND",
    "RTC_DTMF_A",
    "RTC_DTMF_B",
    "RTC_DTMF_C",
    "RTC_DTMF_D",
    "RTC_DTMF_FLASH",
    "RTC_PROVIDER_URI",
    "RTCPU_URIHOMEPAGE",
    "RTCPU_URIHELPDESK",
    "RTCPU_URIPERSONALACCOUNT",
    "RTCPU_URIDISPLAYDURINGCALL",
    "RTCPU_URIDISPLAYDURINGIDLE",
    "RTC_RING_TYPE",
    "RTCRT_PHONE",
    "RTCRT_MESSAGE",
    "RTCRT_RINGBACK",
    "RTC_T120_APPLET",
    "RTCTA_WHITEBOARD",
    "RTCTA_APPSHARING",
    "RTC_PORT_TYPE",
    "RTCPT_AUDIO_RTP",
    "RTCPT_AUDIO_RTCP",
    "RTCPT_VIDEO_RTP",
    "RTCPT_VIDEO_RTCP",
    "RTCPT_SIP",
    "RTC_USER_SEARCH_COLUMN",
    "RTCUSC_URI",
    "RTCUSC_DISPLAYNAME",
    "RTCUSC_TITLE",
    "RTCUSC_OFFICE",
    "RTCUSC_PHONE",
    "RTCUSC_COMPANY",
    "RTCUSC_CITY",
    "RTCUSC_STATE",
    "RTCUSC_COUNTRY",
    "RTCUSC_EMAIL",
    "RTC_USER_SEARCH_PREFERENCE",
    "RTCUSP_MAX_MATCHES",
    "RTCUSP_TIME_LIMIT",
    "RTC_ROAMING_EVENT_TYPE",
    "RTCRET_BUDDY_ROAMING",
    "RTCRET_WATCHER_ROAMING",
    "RTCRET_PRESENCE_ROAMING",
    "RTCRET_PROFILE_ROAMING",
    "RTCRET_WPENDING_ROAMING",
    "RTC_PROFILE_EVENT_TYPE",
    "RTCPFET_PROFILE_GET",
    "RTCPFET_PROFILE_UPDATE",
    "RTC_ANSWER_MODE",
    "RTCAM_OFFER_SESSION_EVENT",
    "RTCAM_AUTOMATICALLY_ACCEPT",
    "RTCAM_AUTOMATICALLY_REJECT",
    "RTCAM_NOT_SUPPORTED",
    "RTC_SESSION_REFER_STATUS",
    "RTCSRS_REFERRING",
    "RTCSRS_ACCEPTED",
    "RTCSRS_ERROR",
    "RTCSRS_REJECTED",
    "RTCSRS_DROPPED",
    "RTCSRS_DONE",
    "RTC_PRESENCE_PROPERTY",
    "RTCPP_PHONENUMBER",
    "RTCPP_DISPLAYNAME",
    "RTCPP_EMAIL",
    "RTCPP_DEVICE_NAME",
    "RTCPP_MULTIPLE",
    "RTC_SECURITY_TYPE",
    "RTCSECT_AUDIO_VIDEO_MEDIA_ENCRYPTION",
    "RTCSECT_T120_MEDIA_ENCRYPTION",
    "RTC_SECURITY_LEVEL",
    "RTCSECL_UNSUPPORTED",
    "RTCSECL_SUPPORTED",
    "RTCSECL_REQUIRED",
    "RTC_REINVITE_STATE",
    "RTCRIN_INCOMING",
    "RTCRIN_SUCCEEDED",
    "RTCRIN_FAIL",
    "IRTCClient",
    "IRTCClient2",
    "IRTCClientPresence",
    "IRTCClientPresence2",
    "IRTCClientProvisioning",
    "IRTCClientProvisioning2",
    "IRTCProfile",
    "IRTCProfile2",
    "IRTCSession",
    "IRTCSession2",
    "IRTCSessionCallControl",
    "IRTCParticipant",
    "IRTCRoamingEvent",
    "IRTCProfileEvent",
    "IRTCProfileEvent2",
    "IRTCClientEvent",
    "IRTCRegistrationStateChangeEvent",
    "IRTCSessionStateChangeEvent",
    "IRTCSessionStateChangeEvent2",
    "IRTCSessionOperationCompleteEvent",
    "IRTCSessionOperationCompleteEvent2",
    "IRTCParticipantStateChangeEvent",
    "IRTCMediaEvent",
    "IRTCIntensityEvent",
    "IRTCMessagingEvent",
    "IRTCBuddyEvent",
    "IRTCBuddyEvent2",
    "IRTCWatcherEvent",
    "IRTCWatcherEvent2",
    "IRTCBuddyGroupEvent",
    "IRTCInfoEvent",
    "IRTCMediaRequestEvent",
    "IRTCReInviteEvent",
    "IRTCPresencePropertyEvent",
    "IRTCPresenceDataEvent",
    "IRTCPresenceStatusEvent",
    "IRTCCollection",
    "IRTCEnumParticipants",
    "IRTCEnumProfiles",
    "IRTCEnumBuddies",
    "IRTCEnumWatchers",
    "IRTCEnumGroups",
    "IRTCPresenceContact",
    "IRTCBuddy",
    "IRTCBuddy2",
    "IRTCWatcher",
    "IRTCWatcher2",
    "IRTCBuddyGroup",
    "IRTCEventNotification",
    "IRTCPortManager",
    "IRTCSessionPortManagement",
    "IRTCClientPortManagement",
    "IRTCUserSearch",
    "IRTCUserSearchQuery",
    "IRTCUserSearchResult",
    "IRTCEnumUserSearchResults",
    "IRTCUserSearchResultsEvent",
    "IRTCSessionReferStatusEvent",
    "IRTCSessionReferredEvent",
    "IRTCSessionDescriptionManager",
    "IRTCEnumPresenceDevices",
    "IRTCPresenceDevice",
    "IRTCDispatchEventNotification",
    "TRANSPORT_SETTING",
    "ITransportSettingsInternal",
    "INetworkTransportSettings",
    "INotificationTransportSync",
]
