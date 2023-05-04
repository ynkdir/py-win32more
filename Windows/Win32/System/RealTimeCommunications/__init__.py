from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Media.DirectShow
import Windows.Win32.Networking.WinSock
import Windows.Win32.System.Com
import Windows.Win32.System.RealTimeCommunications
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
RTCCS_FORCE_PROFILE: UInt32 = 1
RTCCS_FAIL_ON_REDIRECT: UInt32 = 2
RTCMT_AUDIO_SEND: UInt32 = 1
RTCMT_AUDIO_RECEIVE: UInt32 = 2
RTCMT_VIDEO_SEND: UInt32 = 4
RTCMT_VIDEO_RECEIVE: UInt32 = 8
RTCMT_T120_SENDRECV: UInt32 = 16
RTCSI_PC_TO_PC: UInt32 = 1
RTCSI_PC_TO_PHONE: UInt32 = 2
RTCSI_PHONE_TO_PHONE: UInt32 = 4
RTCSI_IM: UInt32 = 8
RTCSI_MULTIPARTY_IM: UInt32 = 16
RTCSI_APPLICATION: UInt32 = 32
RTCTR_UDP: UInt32 = 1
RTCTR_TCP: UInt32 = 2
RTCTR_TLS: UInt32 = 4
RTCAU_BASIC: UInt32 = 1
RTCAU_DIGEST: UInt32 = 2
RTCAU_NTLM: UInt32 = 4
RTCAU_KERBEROS: UInt32 = 8
RTCAU_USE_LOGON_CRED: UInt32 = 65536
RTCRF_REGISTER_INVITE_SESSIONS: UInt32 = 1
RTCRF_REGISTER_MESSAGE_SESSIONS: UInt32 = 2
RTCRF_REGISTER_PRESENCE: UInt32 = 4
RTCRF_REGISTER_NOTIFY: UInt32 = 8
RTCRF_REGISTER_ALL: UInt32 = 15
RTCRMF_BUDDY_ROAMING: UInt32 = 1
RTCRMF_WATCHER_ROAMING: UInt32 = 2
RTCRMF_PRESENCE_ROAMING: UInt32 = 4
RTCRMF_PROFILE_ROAMING: UInt32 = 8
RTCRMF_ALL_ROAMING: UInt32 = 15
RTCEF_CLIENT: UInt32 = 1
RTCEF_REGISTRATION_STATE_CHANGE: UInt32 = 2
RTCEF_SESSION_STATE_CHANGE: UInt32 = 4
RTCEF_SESSION_OPERATION_COMPLETE: UInt32 = 8
RTCEF_PARTICIPANT_STATE_CHANGE: UInt32 = 16
RTCEF_MEDIA: UInt32 = 32
RTCEF_INTENSITY: UInt32 = 64
RTCEF_MESSAGING: UInt32 = 128
RTCEF_BUDDY: UInt32 = 256
RTCEF_WATCHER: UInt32 = 512
RTCEF_PROFILE: UInt32 = 1024
RTCEF_USERSEARCH: UInt32 = 2048
RTCEF_INFO: UInt32 = 4096
RTCEF_GROUP: UInt32 = 8192
RTCEF_MEDIA_REQUEST: UInt32 = 16384
RTCEF_ROAMING: UInt32 = 65536
RTCEF_PRESENCE_PROPERTY: UInt32 = 131072
RTCEF_BUDDY2: UInt32 = 262144
RTCEF_WATCHER2: UInt32 = 524288
RTCEF_SESSION_REFER_STATUS: UInt32 = 1048576
RTCEF_SESSION_REFERRED: UInt32 = 2097152
RTCEF_REINVITE: UInt32 = 4194304
RTCEF_PRESENCE_DATA: UInt32 = 8388608
RTCEF_PRESENCE_STATUS: UInt32 = 16777216
RTCEF_ALL: UInt32 = 33554431
RTCIF_DISABLE_MEDIA: UInt32 = 1
RTCIF_DISABLE_UPNP: UInt32 = 2
RTCIF_ENABLE_SERVER_CLASS: UInt32 = 4
RTCIF_DISABLE_STRICT_DNS: UInt32 = 8
FACILITY_RTC_INTERFACE: UInt32 = 238
FACILITY_SIP_STATUS_CODE: UInt32 = 239
FACILITY_PINT_STATUS_CODE: UInt32 = 240
STATUS_SEVERITY_RTC_ERROR: UInt32 = 2
RTC_E_SIP_CODECS_DO_NOT_MATCH: Windows.Win32.Foundation.HRESULT = -2131886080
RTC_E_SIP_STREAM_PRESENT: Windows.Win32.Foundation.HRESULT = -2131886079
RTC_E_SIP_STREAM_NOT_PRESENT: Windows.Win32.Foundation.HRESULT = -2131886078
RTC_E_SIP_NO_STREAM: Windows.Win32.Foundation.HRESULT = -2131886077
RTC_E_SIP_PARSE_FAILED: Windows.Win32.Foundation.HRESULT = -2131886076
RTC_E_SIP_HEADER_NOT_PRESENT: Windows.Win32.Foundation.HRESULT = -2131886075
RTC_E_SDP_NOT_PRESENT: Windows.Win32.Foundation.HRESULT = -2131886074
RTC_E_SDP_PARSE_FAILED: Windows.Win32.Foundation.HRESULT = -2131886073
RTC_E_SDP_UPDATE_FAILED: Windows.Win32.Foundation.HRESULT = -2131886072
RTC_E_SDP_MULTICAST: Windows.Win32.Foundation.HRESULT = -2131886071
RTC_E_SDP_CONNECTION_ADDR: Windows.Win32.Foundation.HRESULT = -2131886070
RTC_E_SDP_NO_MEDIA: Windows.Win32.Foundation.HRESULT = -2131886069
RTC_E_SIP_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2131886068
RTC_E_SDP_FAILED_TO_BUILD: Windows.Win32.Foundation.HRESULT = -2131886067
RTC_E_SIP_INVITE_TRANSACTION_PENDING: Windows.Win32.Foundation.HRESULT = -2131886066
RTC_E_SIP_AUTH_HEADER_SENT: Windows.Win32.Foundation.HRESULT = -2131886065
RTC_E_SIP_AUTH_TYPE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2131886064
RTC_E_SIP_AUTH_FAILED: Windows.Win32.Foundation.HRESULT = -2131886063
RTC_E_INVALID_SIP_URL: Windows.Win32.Foundation.HRESULT = -2131886062
RTC_E_DESTINATION_ADDRESS_LOCAL: Windows.Win32.Foundation.HRESULT = -2131886061
RTC_E_INVALID_ADDRESS_LOCAL: Windows.Win32.Foundation.HRESULT = -2131886060
RTC_E_DESTINATION_ADDRESS_MULTICAST: Windows.Win32.Foundation.HRESULT = -2131886059
RTC_E_INVALID_PROXY_ADDRESS: Windows.Win32.Foundation.HRESULT = -2131886058
RTC_E_SIP_TRANSPORT_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2131886057
RTC_E_SIP_NEED_MORE_DATA: Windows.Win32.Foundation.HRESULT = -2131886056
RTC_E_SIP_CALL_DISCONNECTED: Windows.Win32.Foundation.HRESULT = -2131886055
RTC_E_SIP_REQUEST_DESTINATION_ADDR_NOT_PRESENT: Windows.Win32.Foundation.HRESULT = -2131886054
RTC_E_SIP_UDP_SIZE_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2131886053
RTC_E_SIP_SSL_TUNNEL_FAILED: Windows.Win32.Foundation.HRESULT = -2131886052
RTC_E_SIP_SSL_NEGOTIATION_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2131886051
RTC_E_SIP_STACK_SHUTDOWN: Windows.Win32.Foundation.HRESULT = -2131886050
RTC_E_MEDIA_CONTROLLER_STATE: Windows.Win32.Foundation.HRESULT = -2131886049
RTC_E_MEDIA_NEED_TERMINAL: Windows.Win32.Foundation.HRESULT = -2131886048
RTC_E_MEDIA_AUDIO_DEVICE_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2131886047
RTC_E_MEDIA_VIDEO_DEVICE_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2131886046
RTC_E_START_STREAM: Windows.Win32.Foundation.HRESULT = -2131886045
RTC_E_MEDIA_AEC: Windows.Win32.Foundation.HRESULT = -2131886044
RTC_E_CLIENT_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2131886043
RTC_E_CLIENT_ALREADY_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2131886042
RTC_E_CLIENT_ALREADY_SHUT_DOWN: Windows.Win32.Foundation.HRESULT = -2131886041
RTC_E_PRESENCE_NOT_ENABLED: Windows.Win32.Foundation.HRESULT = -2131886040
RTC_E_INVALID_SESSION_TYPE: Windows.Win32.Foundation.HRESULT = -2131886039
RTC_E_INVALID_SESSION_STATE: Windows.Win32.Foundation.HRESULT = -2131886038
RTC_E_NO_PROFILE: Windows.Win32.Foundation.HRESULT = -2131886037
RTC_E_LOCAL_PHONE_NEEDED: Windows.Win32.Foundation.HRESULT = -2131886036
RTC_E_NO_DEVICE: Windows.Win32.Foundation.HRESULT = -2131886035
RTC_E_INVALID_PROFILE: Windows.Win32.Foundation.HRESULT = -2131886034
RTC_E_PROFILE_NO_PROVISION: Windows.Win32.Foundation.HRESULT = -2131886033
RTC_E_PROFILE_NO_KEY: Windows.Win32.Foundation.HRESULT = -2131886032
RTC_E_PROFILE_NO_NAME: Windows.Win32.Foundation.HRESULT = -2131886031
RTC_E_PROFILE_NO_USER: Windows.Win32.Foundation.HRESULT = -2131886030
RTC_E_PROFILE_NO_USER_URI: Windows.Win32.Foundation.HRESULT = -2131886029
RTC_E_PROFILE_NO_SERVER: Windows.Win32.Foundation.HRESULT = -2131886028
RTC_E_PROFILE_NO_SERVER_ADDRESS: Windows.Win32.Foundation.HRESULT = -2131886027
RTC_E_PROFILE_NO_SERVER_PROTOCOL: Windows.Win32.Foundation.HRESULT = -2131886026
RTC_E_PROFILE_INVALID_SERVER_PROTOCOL: Windows.Win32.Foundation.HRESULT = -2131886025
RTC_E_PROFILE_INVALID_SERVER_AUTHMETHOD: Windows.Win32.Foundation.HRESULT = -2131886024
RTC_E_PROFILE_INVALID_SERVER_ROLE: Windows.Win32.Foundation.HRESULT = -2131886023
RTC_E_PROFILE_MULTIPLE_REGISTRARS: Windows.Win32.Foundation.HRESULT = -2131886022
RTC_E_PROFILE_INVALID_SESSION: Windows.Win32.Foundation.HRESULT = -2131886021
RTC_E_PROFILE_INVALID_SESSION_PARTY: Windows.Win32.Foundation.HRESULT = -2131886020
RTC_E_PROFILE_INVALID_SESSION_TYPE: Windows.Win32.Foundation.HRESULT = -2131886019
RTC_E_OPERATION_WITH_TOO_MANY_PARTICIPANTS: Windows.Win32.Foundation.HRESULT = -2131886018
RTC_E_BASIC_AUTH_SET_TLS: Windows.Win32.Foundation.HRESULT = -2131886017
RTC_E_SIP_HIGH_SECURITY_SET_TLS: Windows.Win32.Foundation.HRESULT = -2131886016
RTC_S_ROAMING_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = 15597633
RTC_E_PROFILE_SERVER_UNAUTHORIZED: Windows.Win32.Foundation.HRESULT = -2131886014
RTC_E_DUPLICATE_REALM: Windows.Win32.Foundation.HRESULT = -2131886013
RTC_E_POLICY_NOT_ALLOW: Windows.Win32.Foundation.HRESULT = -2131886012
RTC_E_PORT_MAPPING_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2131886011
RTC_E_PORT_MAPPING_FAILED: Windows.Win32.Foundation.HRESULT = -2131886010
RTC_E_SECURITY_LEVEL_NOT_COMPATIBLE: Windows.Win32.Foundation.HRESULT = -2131886009
RTC_E_SECURITY_LEVEL_NOT_DEFINED: Windows.Win32.Foundation.HRESULT = -2131886008
RTC_E_SECURITY_LEVEL_NOT_SUPPORTED_BY_PARTICIPANT: Windows.Win32.Foundation.HRESULT = -2131886007
RTC_E_DUPLICATE_BUDDY: Windows.Win32.Foundation.HRESULT = -2131886006
RTC_E_DUPLICATE_WATCHER: Windows.Win32.Foundation.HRESULT = -2131886005
RTC_E_MALFORMED_XML: Windows.Win32.Foundation.HRESULT = -2131886004
RTC_E_ROAMING_OPERATION_INTERRUPTED: Windows.Win32.Foundation.HRESULT = -2131886003
RTC_E_ROAMING_FAILED: Windows.Win32.Foundation.HRESULT = -2131886002
RTC_E_INVALID_BUDDY_LIST: Windows.Win32.Foundation.HRESULT = -2131886001
RTC_E_INVALID_ACL_LIST: Windows.Win32.Foundation.HRESULT = -2131886000
RTC_E_NO_GROUP: Windows.Win32.Foundation.HRESULT = -2131885999
RTC_E_DUPLICATE_GROUP: Windows.Win32.Foundation.HRESULT = -2131885998
RTC_E_TOO_MANY_GROUPS: Windows.Win32.Foundation.HRESULT = -2131885997
RTC_E_NO_BUDDY: Windows.Win32.Foundation.HRESULT = -2131885996
RTC_E_NO_WATCHER: Windows.Win32.Foundation.HRESULT = -2131885995
RTC_E_NO_REALM: Windows.Win32.Foundation.HRESULT = -2131885994
RTC_E_NO_TRANSPORT: Windows.Win32.Foundation.HRESULT = -2131885993
RTC_E_NOT_EXIST: Windows.Win32.Foundation.HRESULT = -2131885992
RTC_E_INVALID_PREFERENCE_LIST: Windows.Win32.Foundation.HRESULT = -2131885991
RTC_E_MAX_PENDING_OPERATIONS: Windows.Win32.Foundation.HRESULT = -2131885990
RTC_E_TOO_MANY_RETRIES: Windows.Win32.Foundation.HRESULT = -2131885989
RTC_E_INVALID_PORTRANGE: Windows.Win32.Foundation.HRESULT = -2131885988
RTC_E_SIP_CALL_CONNECTION_NOT_ESTABLISHED: Windows.Win32.Foundation.HRESULT = -2131885987
RTC_E_SIP_ADDITIONAL_PARTY_IN_TWO_PARTY_SESSION: Windows.Win32.Foundation.HRESULT = -2131885986
RTC_E_SIP_PARTY_ALREADY_IN_SESSION: Windows.Win32.Foundation.HRESULT = -2131885985
RTC_E_SIP_OTHER_PARTY_JOIN_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2131885984
RTC_E_INVALID_OBJECT_STATE: Windows.Win32.Foundation.HRESULT = -2131885983
RTC_E_PRESENCE_ENABLED: Windows.Win32.Foundation.HRESULT = -2131885982
RTC_E_ROAMING_ENABLED: Windows.Win32.Foundation.HRESULT = -2131885981
RTC_E_SIP_TLS_INCOMPATIBLE_ENCRYPTION: Windows.Win32.Foundation.HRESULT = -2131885980
RTC_E_SIP_INVALID_CERTIFICATE: Windows.Win32.Foundation.HRESULT = -2131885979
RTC_E_SIP_DNS_FAIL: Windows.Win32.Foundation.HRESULT = -2131885978
RTC_E_SIP_TCP_FAIL: Windows.Win32.Foundation.HRESULT = -2131885977
RTC_E_TOO_SMALL_EXPIRES_VALUE: Windows.Win32.Foundation.HRESULT = -2131885976
RTC_E_SIP_TLS_FAIL: Windows.Win32.Foundation.HRESULT = -2131885975
RTC_E_NOT_PRESENCE_PROFILE: Windows.Win32.Foundation.HRESULT = -2131885974
RTC_E_SIP_INVITEE_PARTY_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2131885973
RTC_E_SIP_AUTH_TIME_SKEW: Windows.Win32.Foundation.HRESULT = -2131885972
RTC_E_INVALID_REGISTRATION_STATE: Windows.Win32.Foundation.HRESULT = -2131885971
RTC_E_MEDIA_DISABLED: Windows.Win32.Foundation.HRESULT = -2131885970
RTC_E_MEDIA_ENABLED: Windows.Win32.Foundation.HRESULT = -2131885969
RTC_E_REFER_NOT_ACCEPTED: Windows.Win32.Foundation.HRESULT = -2131885968
RTC_E_REFER_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2131885967
RTC_E_REFER_NOT_EXIST: Windows.Win32.Foundation.HRESULT = -2131885966
RTC_E_SIP_HOLD_OPERATION_PENDING: Windows.Win32.Foundation.HRESULT = -2131885965
RTC_E_SIP_UNHOLD_OPERATION_PENDING: Windows.Win32.Foundation.HRESULT = -2131885964
RTC_E_MEDIA_SESSION_NOT_EXIST: Windows.Win32.Foundation.HRESULT = -2131885963
RTC_E_MEDIA_SESSION_IN_HOLD: Windows.Win32.Foundation.HRESULT = -2131885962
RTC_E_ANOTHER_MEDIA_SESSION_ACTIVE: Windows.Win32.Foundation.HRESULT = -2131885961
RTC_E_MAX_REDIRECTS: Windows.Win32.Foundation.HRESULT = -2131885960
RTC_E_REDIRECT_PROCESSING_FAILED: Windows.Win32.Foundation.HRESULT = -2131885959
RTC_E_LISTENING_SOCKET_NOT_EXIST: Windows.Win32.Foundation.HRESULT = -2131885958
RTC_E_INVALID_LISTEN_SOCKET: Windows.Win32.Foundation.HRESULT = -2131885957
RTC_E_PORT_MANAGER_ALREADY_SET: Windows.Win32.Foundation.HRESULT = -2131885956
RTC_E_SECURITY_LEVEL_ALREADY_SET: Windows.Win32.Foundation.HRESULT = -2131885955
RTC_E_UDP_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2131885954
RTC_E_SIP_REFER_OPERATION_PENDING: Windows.Win32.Foundation.HRESULT = -2131885953
RTC_E_PLATFORM_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2131885952
RTC_E_SIP_PEER_PARTICIPANT_IN_MULTIPARTY_SESSION: Windows.Win32.Foundation.HRESULT = -2131885951
RTC_E_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2131885950
RTC_E_REGISTRATION_DEACTIVATED: Windows.Win32.Foundation.HRESULT = -2131885949
RTC_E_REGISTRATION_REJECTED: Windows.Win32.Foundation.HRESULT = -2131885948
RTC_E_REGISTRATION_UNREGISTERED: Windows.Win32.Foundation.HRESULT = -2131885947
RTC_E_STATUS_INFO_TRYING: Windows.Win32.Foundation.HRESULT = 15663204
RTC_E_STATUS_INFO_RINGING: Windows.Win32.Foundation.HRESULT = 15663284
RTC_E_STATUS_INFO_CALL_FORWARDING: Windows.Win32.Foundation.HRESULT = 15663285
RTC_E_STATUS_INFO_QUEUED: Windows.Win32.Foundation.HRESULT = 15663286
RTC_E_STATUS_SESSION_PROGRESS: Windows.Win32.Foundation.HRESULT = 15663287
RTC_E_STATUS_SUCCESS: Windows.Win32.Foundation.HRESULT = 15663304
RTC_E_STATUS_REDIRECT_MULTIPLE_CHOICES: Windows.Win32.Foundation.HRESULT = -2131820244
RTC_E_STATUS_REDIRECT_MOVED_PERMANENTLY: Windows.Win32.Foundation.HRESULT = -2131820243
RTC_E_STATUS_REDIRECT_MOVED_TEMPORARILY: Windows.Win32.Foundation.HRESULT = -2131820242
RTC_E_STATUS_REDIRECT_SEE_OTHER: Windows.Win32.Foundation.HRESULT = -2131820241
RTC_E_STATUS_REDIRECT_USE_PROXY: Windows.Win32.Foundation.HRESULT = -2131820239
RTC_E_STATUS_REDIRECT_ALTERNATIVE_SERVICE: Windows.Win32.Foundation.HRESULT = -2131820164
RTC_E_STATUS_CLIENT_BAD_REQUEST: Windows.Win32.Foundation.HRESULT = -2131820144
RTC_E_STATUS_CLIENT_UNAUTHORIZED: Windows.Win32.Foundation.HRESULT = -2131820143
RTC_E_STATUS_CLIENT_PAYMENT_REQUIRED: Windows.Win32.Foundation.HRESULT = -2131820142
RTC_E_STATUS_CLIENT_FORBIDDEN: Windows.Win32.Foundation.HRESULT = -2131820141
RTC_E_STATUS_CLIENT_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2131820140
RTC_E_STATUS_CLIENT_METHOD_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2131820139
RTC_E_STATUS_CLIENT_NOT_ACCEPTABLE: Windows.Win32.Foundation.HRESULT = -2131820138
RTC_E_STATUS_CLIENT_PROXY_AUTHENTICATION_REQUIRED: Windows.Win32.Foundation.HRESULT = -2131820137
RTC_E_STATUS_CLIENT_REQUEST_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2131820136
RTC_E_STATUS_CLIENT_CONFLICT: Windows.Win32.Foundation.HRESULT = -2131820135
RTC_E_STATUS_CLIENT_GONE: Windows.Win32.Foundation.HRESULT = -2131820134
RTC_E_STATUS_CLIENT_LENGTH_REQUIRED: Windows.Win32.Foundation.HRESULT = -2131820133
RTC_E_STATUS_CLIENT_REQUEST_ENTITY_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2131820131
RTC_E_STATUS_CLIENT_REQUEST_URI_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2131820130
RTC_E_STATUS_CLIENT_UNSUPPORTED_MEDIA_TYPE: Windows.Win32.Foundation.HRESULT = -2131820129
RTC_E_STATUS_CLIENT_BAD_EXTENSION: Windows.Win32.Foundation.HRESULT = -2131820124
RTC_E_STATUS_CLIENT_TEMPORARILY_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2131820064
RTC_E_STATUS_CLIENT_TRANSACTION_DOES_NOT_EXIST: Windows.Win32.Foundation.HRESULT = -2131820063
RTC_E_STATUS_CLIENT_LOOP_DETECTED: Windows.Win32.Foundation.HRESULT = -2131820062
RTC_E_STATUS_CLIENT_TOO_MANY_HOPS: Windows.Win32.Foundation.HRESULT = -2131820061
RTC_E_STATUS_CLIENT_ADDRESS_INCOMPLETE: Windows.Win32.Foundation.HRESULT = -2131820060
RTC_E_STATUS_CLIENT_AMBIGUOUS: Windows.Win32.Foundation.HRESULT = -2131820059
RTC_E_STATUS_CLIENT_BUSY_HERE: Windows.Win32.Foundation.HRESULT = -2131820058
RTC_E_STATUS_REQUEST_TERMINATED: Windows.Win32.Foundation.HRESULT = -2131820057
RTC_E_STATUS_NOT_ACCEPTABLE_HERE: Windows.Win32.Foundation.HRESULT = -2131820056
RTC_E_STATUS_SERVER_INTERNAL_ERROR: Windows.Win32.Foundation.HRESULT = -2131820044
RTC_E_STATUS_SERVER_NOT_IMPLEMENTED: Windows.Win32.Foundation.HRESULT = -2131820043
RTC_E_STATUS_SERVER_BAD_GATEWAY: Windows.Win32.Foundation.HRESULT = -2131820042
RTC_E_STATUS_SERVER_SERVICE_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2131820041
RTC_E_STATUS_SERVER_SERVER_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2131820040
RTC_E_STATUS_SERVER_VERSION_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2131820039
RTC_E_STATUS_GLOBAL_BUSY_EVERYWHERE: Windows.Win32.Foundation.HRESULT = -2131819944
RTC_E_STATUS_GLOBAL_DECLINE: Windows.Win32.Foundation.HRESULT = -2131819941
RTC_E_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE: Windows.Win32.Foundation.HRESULT = -2131819940
RTC_E_STATUS_GLOBAL_NOT_ACCEPTABLE: Windows.Win32.Foundation.HRESULT = -2131819938
RTC_E_PINT_STATUS_REJECTED_BUSY: Windows.Win32.Foundation.HRESULT = -2131755003
RTC_E_PINT_STATUS_REJECTED_NO_ANSWER: Windows.Win32.Foundation.HRESULT = -2131755002
RTC_E_PINT_STATUS_REJECTED_ALL_BUSY: Windows.Win32.Foundation.HRESULT = -2131755001
RTC_E_PINT_STATUS_REJECTED_PL_FAILED: Windows.Win32.Foundation.HRESULT = -2131755000
RTC_E_PINT_STATUS_REJECTED_SW_FAILED: Windows.Win32.Foundation.HRESULT = -2131754999
RTC_E_PINT_STATUS_REJECTED_CANCELLED: Windows.Win32.Foundation.HRESULT = -2131754998
RTC_E_PINT_STATUS_REJECTED_BADNUMBER: Windows.Win32.Foundation.HRESULT = -2131754997
class INetworkTransportSettings(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e7abb2c-f2c1-4a61-bd35-deb7a08ab0f1}')
    @commethod(3)
    def ApplySetting(self, SettingId: POINTER(Windows.Win32.Networking.WinSock.TRANSPORT_SETTING_ID_head), LengthIn: UInt32, ValueIn: POINTER(Byte), LengthOut: POINTER(UInt32), ValueOut: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySetting(self, SettingId: POINTER(Windows.Win32.Networking.WinSock.TRANSPORT_SETTING_ID_head), LengthIn: UInt32, ValueIn: POINTER(Byte), LengthOut: POINTER(UInt32), ValueOut: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class INotificationTransportSync(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eb1402-0ab8-49c0-9e14-a1ae4ba93058}')
    @commethod(3)
    def CompleteDelivery(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddy(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCPresenceContact
    _iid_ = Guid('{fcb136c8-7b90-4e0c-befe-56edf0ba6f1c}')
    @commethod(11)
    def get_Status(self, penStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Notes(self, pbstrNotes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddy2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCBuddy
    _iid_ = Guid('{102f9588-23e7-40e3-954d-cd7a1d5c0361}')
    @commethod(13)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EnumerateGroups(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Groups(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PresenceProperty(self, enProperty: Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumeratePresenceDevices(self, ppEnumDevices: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumPresenceDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_PresenceDevices(self, ppDevicesCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_SubscriptionType(self, penSubscriptionType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddyEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f36d755d-17e6-404e-954f-0fc07574c78d}')
    @commethod(7)
    def get_Buddy(self, ppBuddy: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddyEvent2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCBuddyEvent
    _iid_ = Guid('{484a7f1e-73f0-4990-bfc2-60bc3978a720}')
    @commethod(8)
    def get_EventType(self, pEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_BUDDY_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddyGroup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{60361e68-9164-4389-a4c6-d0b3925bda5e}')
    @commethod(3)
    def get_Name(self, pbstrGroupName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Name(self, bstrGroupName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddBuddy(self, pBuddy: Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveBuddy(self, pBuddy: Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateBuddies(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Buddies(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Data(self, pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Data(self, bstrData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCBuddyGroupEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3a79e1d1-b736-4414-96f8-bbc7f08863e4}')
    @commethod(7)
    def get_EventType(self, pEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_GROUP_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Group(self, ppGroup: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Buddy(self, ppBuddy: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{07829e45-9a34-408e-a011-bddf13487cd1}')
    @commethod(3)
    def Initialize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareForShutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_EventFilter(self, lFilter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_EventFilter(self, plFilter: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPreferredMediaTypes(self, lMediaTypes: Int32, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PreferredMediaTypes(self, plMediaTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MediaCapabilities(self, plMediaTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSession(self, enType: Windows.Win32.System.RealTimeCommunications.RTC_SESSION_TYPE, bstrLocalPhoneURI: Windows.Win32.Foundation.BSTR, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ListenForIncomingSessions(self, enListen: Windows.Win32.System.RealTimeCommunications.RTC_LISTEN_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ListenForIncomingSessions(self, penListen: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_LISTEN_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NetworkAddresses(self, fTCP: Windows.Win32.Foundation.VARIANT_BOOL, fExternal: Windows.Win32.Foundation.VARIANT_BOOL, pvAddresses: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Volume(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, lVolume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Volume(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, plVolume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_AudioMuted(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, fMuted: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_AudioMuted(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, pfMuted: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_IVideoWindow(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_VIDEO_DEVICE, ppIVideoWindow: POINTER(Windows.Win32.Media.DirectShow.IVideoWindow_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_PreferredAudioDevice(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, bstrDeviceName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_PreferredAudioDevice(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PreferredVolume(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, lVolume: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_PreferredVolume(self, enDevice: Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE, plVolume: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_PreferredAEC(self, bEnable: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PreferredAEC(self, pbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_PreferredVideoDevice(self, bstrDeviceName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_PreferredVideoDevice(self, pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_ActiveMedia(self, plMediaType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxBitrate(self, lMaxBitrate: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_MaxBitrate(self, plMaxBitrate: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_TemporalSpatialTradeOff(self, lValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_TemporalSpatialTradeOff(self, plValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_NetworkQuality(self, plNetworkQuality: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def StartT120Applet(self, enApplet: Windows.Win32.System.RealTimeCommunications.RTC_T120_APPLET) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def StopT120Applets(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_IsT120AppletRunning(self, enApplet: Windows.Win32.System.RealTimeCommunications.RTC_T120_APPLET, pfRunning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_LocalUserURI(self, pbstrUserURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_LocalUserURI(self, bstrUserURI: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_LocalUserName(self, pbstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_LocalUserName(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def PlayRing(self, enType: Windows.Win32.System.RealTimeCommunications.RTC_RING_TYPE, bPlay: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SendDTMF(self, enDTMF: Windows.Win32.System.RealTimeCommunications.RTC_DTMF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def InvokeTuningWizard(self, hwndParent: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_IsTuned(self, pfTuned: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClient2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCClient
    _iid_ = Guid('{0c91d71d-1064-42da-bfa5-572beb8eea84}')
    @commethod(45)
    def put_AnswerMode(self, enType: Windows.Win32.System.RealTimeCommunications.RTC_SESSION_TYPE, enMode: Windows.Win32.System.RealTimeCommunications.RTC_ANSWER_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_AnswerMode(self, enType: Windows.Win32.System.RealTimeCommunications.RTC_SESSION_TYPE, penMode: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_ANSWER_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def InvokeTuningWizardEx(self, hwndParent: IntPtr, fAllowAudio: Windows.Win32.Foundation.VARIANT_BOOL, fAllowVideo: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Version(self, plVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_ClientName(self, bstrClientName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_ClientCurVer(self, bstrClientCurVer: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def InitializeEx(self, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def CreateSessionWithDescription(self, bstrContentType: Windows.Win32.Foundation.BSTR, bstrSessionDescription: Windows.Win32.Foundation.BSTR, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppSession2: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetSessionDescriptionManager(self, pSessionDescriptionManager: Windows.Win32.System.RealTimeCommunications.IRTCSessionDescriptionManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_PreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, enSecurityLevel: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_PreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_AllowedPorts(self, lTransport: Int32, enListenMode: Windows.Win32.System.RealTimeCommunications.RTC_LISTEN_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_AllowedPorts(self, lTransport: Int32, penListenMode: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_LISTEN_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2b493b7a-3cba-4170-9c8b-76a9dacdd644}')
    @commethod(7)
    def get_EventType(self, penEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_CLIENT_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Client(self, ppClient: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCClient_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientPortManagement(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5df3f03-4bde-4417-aefe-71177bdaea66}')
    @commethod(3)
    def StartListenAddressAndPort(self, bstrInternalLocalAddress: Windows.Win32.Foundation.BSTR, lInternalLocalPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopListenAddressAndPort(self, bstrInternalLocalAddress: Windows.Win32.Foundation.BSTR, lInternalLocalPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPortRange(self, enPortType: Windows.Win32.System.RealTimeCommunications.RTC_PORT_TYPE, plMinValue: POINTER(Int32), plMaxValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientPresence(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11c3cbcc-0744-42d1-968a-51aa1bb274c6}')
    @commethod(3)
    def EnablePresence(self, fUseStorage: Windows.Win32.Foundation.VARIANT_BOOL, varStorage: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Export(self, varStorage: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Import(self, varStorage: Windows.Win32.System.Variant.VARIANT, fReplaceAll: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateBuddies(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Buddies(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Buddy(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, ppBuddy: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddBuddy(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppBuddy: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveBuddy(self, pBuddy: Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumerateWatchers(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumWatchers_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Watchers(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Watcher(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, ppWatcher: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddWatcher(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR, fBlocked: Windows.Win32.Foundation.VARIANT_BOOL, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL, ppWatcher: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveWatcher(self, pWatcher: Windows.Win32.System.RealTimeCommunications.IRTCWatcher_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetLocalPresenceInfo(self, enStatus: Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_STATUS, bstrNotes: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_OfferWatcherMode(self, penMode: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_OfferWatcherMode(self, enMode: Windows.Win32.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_PrivacyMode(self, penMode: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRIVACY_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_PrivacyMode(self, enMode: Windows.Win32.System.RealTimeCommunications.RTC_PRIVACY_MODE) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientPresence2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCClientPresence
    _iid_ = Guid('{ad1809e8-62f7-4783-909a-29c9d2cb1d34}')
    @commethod(21)
    def EnablePresenceEx(self, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, varStorage: Windows.Win32.System.Variant.VARIANT, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DisablePresence(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddGroup(self, bstrGroupName: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppGroup: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveGroup(self, pGroup: Windows.Win32.System.RealTimeCommunications.IRTCBuddyGroup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def EnumerateGroups(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Groups(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Group(self, bstrGroupName: Windows.Win32.Foundation.BSTR, ppGroup: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AddWatcherEx(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR, enState: Windows.Win32.System.RealTimeCommunications.RTC_WATCHER_STATE, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL, enScope: Windows.Win32.System.RealTimeCommunications.RTC_ACE_SCOPE, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppWatcher: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_WatcherEx(self, enMode: Windows.Win32.System.RealTimeCommunications.RTC_WATCHER_MATCH_MODE, bstrPresentityURI: Windows.Win32.Foundation.BSTR, ppWatcher: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_PresenceProperty(self, enProperty: Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, bstrProperty: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_PresenceProperty(self, enProperty: Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetPresenceData(self, bstrNamespace: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetPresenceData(self, pbstrNamespace: POINTER(Windows.Win32.Foundation.BSTR), pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetLocalPresenceInfo(self, penStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_STATUS), pbstrNotes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddBuddyEx(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrData: Windows.Win32.Foundation.BSTR, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL, enSubscriptionType: Windows.Win32.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppBuddy: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientProvisioning(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b9f5cf06-65b9-4a80-a0e6-73cae3ef3822}')
    @commethod(3)
    def CreateProfile(self, bstrProfileXML: Windows.Win32.Foundation.BSTR, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableProfile(self, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lRegisterFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DisableProfile(self, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateProfiles(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumProfiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Profiles(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProfile(self, bstrUserAccount: Windows.Win32.Foundation.BSTR, bstrUserPassword: Windows.Win32.Foundation.BSTR, bstrUserURI: Windows.Win32.Foundation.BSTR, bstrServer: Windows.Win32.Foundation.BSTR, lTransport: Int32, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SessionCapabilities(self, plSupportedSessions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCClientProvisioning2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCClientProvisioning
    _iid_ = Guid('{a70909b5-f40e-4587-bb75-e6bc0845023e}')
    @commethod(10)
    def EnableProfileEx(self, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lRegisterFlags: Int32, lRoamingFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ec7c8096-b918-4044-94f1-e4fba0361d5c}')
    @commethod(7)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, Index: Int32, pVariant: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppNewEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCDispatchEventNotification(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{176ddfbe-fec0-4d55-bc87-84cff1ef7f91}')
class IRTCEnumBuddies(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7296917-5569-4b3b-b3af-98d1144b2b87}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddy_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumGroups(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{742378d6-a141-4415-8f27-35d99076cf5d}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCBuddyGroup_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumGroups_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumParticipants(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcd56f29-4a4f-41b2-ba5c-f5bccc060bf6}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumParticipants_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumPresenceDevices(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{708c2ab7-8bf8-42f8-8c7d-635197ad5539}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCPresenceDevice_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumPresenceDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumProfiles(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{29b7c41c-ed82-4bca-84ad-39d5101b58e3}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumProfiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumUserSearchResults(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83d4d877-aa5d-4a5b-8d0e-002a8067e0e8}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCUserSearchResult_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumUserSearchResults_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEnumWatchers(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a87d55d7-db74-4ed1-9ca4-77a0e41b413e}')
    @commethod(3)
    def Next(self, celt: UInt32, ppElements: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumWatchers_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCEventNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13fa24c7-5748-4b21-91f5-7397609ce747}')
    @commethod(3)
    def Event(self, RTCEvent: Windows.Win32.System.RealTimeCommunications.RTC_EVENT, pEvent: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCInfoEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4e1d68ae-1912-4f49-b2c3-594fadfd425f}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Participant(self, ppParticipant: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Info(self, pbstrInfo: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InfoHeader(self, pbstrInfoHeader: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCIntensityEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4c23bf51-390c-4992-a41d-41eec05b2a4b}')
    @commethod(7)
    def get_Level(self, plLevel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Min(self, plMin: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Max(self, plMax: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Direction(self, penDirection: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_AUDIO_DEVICE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCMediaEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{099944fb-bcda-453e-8c41-e13da2adf7f3}')
    @commethod(7)
    def get_MediaType(self, pMediaType: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_EventType(self, penEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_MEDIA_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventReason(self, penEventReason: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_MEDIA_EVENT_REASON)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCMediaRequestEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{52572d15-148c-4d97-a36c-2da55c289d63}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProposedMedia(self, plMediaTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentMedia(self, plMediaTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Accept(self, lMediaTypes: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RemotePreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_State(self, pState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_REINVITE_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCMessagingEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d3609541-1b29-4de5-a4ad-5aebaf319512}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Participant(self, ppParticipant: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventType(self, penEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_MESSAGING_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Message(self, pbstrMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MessageHeader(self, pbstrMessageHeader: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UserStatus(self, penUserStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCParticipant(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae86add5-26b1-4414-af1d-b94cd938d739}')
    @commethod(3)
    def get_UserURI(self, pbstrUserURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Removable(self, pfRemovable: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PARTICIPANT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCParticipantStateChangeEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{09bcb597-f0fa-48f9-b420-468cea7fde04}')
    @commethod(7)
    def get_Participant(self, ppParticipant: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PARTICIPANT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPortManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da77c14b-6208-43ca-8ddf-5b60a0a69fac}')
    @commethod(3)
    def GetMapping(self, bstrRemoteAddress: Windows.Win32.Foundation.BSTR, enPortType: Windows.Win32.System.RealTimeCommunications.RTC_PORT_TYPE, pbstrInternalLocalAddress: POINTER(Windows.Win32.Foundation.BSTR), plInternalLocalPort: POINTER(Int32), pbstrExternalLocalAddress: POINTER(Windows.Win32.Foundation.BSTR), plExternalLocalPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateRemoteAddress(self, bstrRemoteAddress: Windows.Win32.Foundation.BSTR, bstrInternalLocalAddress: Windows.Win32.Foundation.BSTR, lInternalLocalPort: Int32, bstrExternalLocalAddress: Windows.Win32.Foundation.BSTR, lExternalLocalPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReleaseMapping(self, bstrInternalLocalAddress: Windows.Win32.Foundation.BSTR, lInternalLocalPort: Int32, bstrExternalLocalAddress: Windows.Win32.Foundation.BSTR, lExternalLocalAddress: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPresenceContact(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8b22f92c-cd90-42db-a733-212205c3e3df}')
    @commethod(3)
    def get_PresentityURI(self, pbstrPresentityURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_PresentityURI(self, bstrPresentityURI: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Name(self, bstrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Data(self, pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Data(self, bstrData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Persistent(self, pfPersistent: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Persistent(self, fPersistent: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPresenceDataEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{38f0e78c-8b87-4c04-a82d-aedd83c909bb}')
    @commethod(7)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPresenceData(self, pbstrNamespace: POINTER(Windows.Win32.Foundation.BSTR), pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPresenceDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc6a90dd-ad9a-48da-9b0c-2515e38521ad}')
    @commethod(3)
    def get_Status(self, penStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Notes(self, pbstrNotes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PresenceProperty(self, enProperty: Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPresenceData(self, pbstrNamespace: POINTER(Windows.Win32.Foundation.BSTR), pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPresencePropertyEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f777f570-a820-49d5-86bd-e099493f1518}')
    @commethod(7)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PresenceProperty(self, penPresProp: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Value(self, pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCPresenceStatusEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{78673f32-4a0f-462c-89aa-ee7706707678}')
    @commethod(7)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocalPresenceInfo(self, penStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PRESENCE_STATUS), pbstrNotes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCProfile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d07eca9e-4062-4dd4-9e7d-722a49ba7303}')
    @commethod(3)
    def get_Key(self, pbstrKey: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_XML(self, pbstrXML: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_ProviderName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ProviderURI(self, enURI: Windows.Win32.System.RealTimeCommunications.RTC_PROVIDER_URI, pbstrURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProviderData(self, pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ClientName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ClientBanner(self, pfBanner: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClientMinVer(self, pbstrMinVer: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClientCurVer(self, pbstrCurVer: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClientUpdateURI(self, pbstrUpdateURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ClientData(self, pbstrData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserURI(self, pbstrUserURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserName(self, pbstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_UserAccount(self, pbstrUserAccount: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetCredentials(self, bstrUserURI: Windows.Win32.Foundation.BSTR, bstrUserAccount: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SessionCapabilities(self, plSupportedSessions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_REGISTRATION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCProfile2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCProfile
    _iid_ = Guid('{4b81f84e-bdc7-4184-9154-3cb2dd7917fb}')
    @commethod(21)
    def get_Realm(self, pbstrRealm: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Realm(self, bstrRealm: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AllowedAuth(self, plAllowedAuth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AllowedAuth(self, lAllowedAuth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCProfileEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d6d5ab3b-770e-43e8-800a-79b062395fca}')
    @commethod(7)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Cookie(self, plCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCProfileEvent2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCProfileEvent
    _iid_ = Guid('{62e56edc-03fa-4121-94fb-23493fd0ae64}')
    @commethod(10)
    def get_EventType(self, pEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_PROFILE_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCReInviteEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{11558d84-204c-43e7-99b0-2034e9417f7d}')
    @commethod(7)
    def get_Session(self, ppSession2: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Accept(self, bstrContentType: Windows.Win32.Foundation.BSTR, bstrSessionDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(self, pState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_REINVITE_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRemoteSessionDescription(self, pbstrContentType: POINTER(Windows.Win32.Foundation.BSTR), pbstrSessionDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCRegistrationStateChangeEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{62d0991b-50ab-4f02-b948-ca94f26f8f95}')
    @commethod(7)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_REGISTRATION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCRoamingEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79960a6b-0cb1-4dc8-a805-7318e99902e8}')
    @commethod(7)
    def get_EventType(self, pEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_ROAMING_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{387c8086-99be-42fb-9973-7c0fc0ca9fa8}')
    @commethod(3)
    def get_Client(self, ppClient: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCClient_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SESSION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(self, penType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SESSION_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Participants(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Answer(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Terminate(self, enReason: Windows.Win32.System.RealTimeCommunications.RTC_TERMINATE_REASON) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Redirect(self, enType: Windows.Win32.System.RealTimeCommunications.RTC_SESSION_TYPE, bstrLocalPhoneURI: Windows.Win32.Foundation.BSTR, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddParticipant(self, bstrAddress: Windows.Win32.Foundation.BSTR, bstrName: Windows.Win32.Foundation.BSTR, ppParticipant: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveParticipant(self, pParticipant: Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnumerateParticipants(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumParticipants_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CanAddParticipants(self, pfCanAdd: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RedirectedUserURI(self, pbstrUserURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RedirectedUserName(self, pbstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def NextRedirectedUser(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SendMessage(self, bstrMessageHeader: Windows.Win32.Foundation.BSTR, bstrMessage: Windows.Win32.Foundation.BSTR, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SendMessageStatus(self, enUserStatus: Windows.Win32.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AddStream(self, lMediaType: Int32, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RemoveStream(self, lMediaType: Int32, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_EncryptionKey(self, lMediaType: Int32, EncryptionKey: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSession2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCSession
    _iid_ = Guid('{17d7cdfc-b007-484c-99d2-86a8a820991d}')
    @commethod(23)
    def SendInfo(self, bstrInfoHeader: Windows.Win32.Foundation.BSTR, bstrInfo: Windows.Win32.Foundation.BSTR, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_PreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, enSecurityLevel: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_PreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def IsSecurityEnabled(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, pfSecurityEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def AnswerWithSessionDescription(self, bstrContentType: Windows.Win32.Foundation.BSTR, bstrSessionDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def ReInviteWithSessionDescription(self, bstrContentType: Windows.Win32.Foundation.BSTR, bstrSessionDescription: Windows.Win32.Foundation.BSTR, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionCallControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9a50d94-190b-4f82-9530-3b8ebf60758a}')
    @commethod(3)
    def Hold(self, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnHold(self, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Forward(self, bstrForwardToURI: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Refer(self, bstrReferToURI: Windows.Win32.Foundation.BSTR, bstrReferCookie: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_ReferredByURI(self, bstrReferredByURI: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferredByURI(self, pbstrReferredByURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ReferCookie(self, bstrReferCookie: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReferCookie(self, pbstrReferCookie: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsReferred(self, pfIsReferred: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionDescriptionManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba7f518e-d336-4070-93a6-865395c843f9}')
    @commethod(3)
    def EvaluateSessionDescription(self, bstrContentType: Windows.Win32.Foundation.BSTR, bstrSessionDescription: Windows.Win32.Foundation.BSTR, pfApplicationSession: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionOperationCompleteEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a6bff4c0-f7c8-4d3c-9a41-3550f78a95b0}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Cookie(self, plCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionOperationCompleteEvent2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCSessionOperationCompleteEvent
    _iid_ = Guid('{f6fc2a9b-d5bc-4241-b436-1b8460c13832}')
    @commethod(11)
    def get_Participant(self, ppParticipant: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCParticipant_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRemoteSessionDescription(self, pbstrContentType: POINTER(Windows.Win32.Foundation.BSTR), pbstrSessionDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionPortManagement(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a072f1d6-0286-4e1f-85f2-17a2948456ec}')
    @commethod(3)
    def SetPortManager(self, pPortManager: Windows.Win32.System.RealTimeCommunications.IRTCPortManager_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionReferStatusEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3d8fc2cd-5d76-44ab-bb68-2a80353b34a2}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferStatus(self, penReferStatus: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SESSION_REFER_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionReferredEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{176a6828-4fcc-4f28-a862-04597a6cf1c4}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferredByURI(self, pbstrReferredByURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ReferToURI(self, pbstrReferoURI: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReferCookie(self, pbstrReferCookie: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Accept(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetReferredSessionState(self, enState: Windows.Win32.System.RealTimeCommunications.RTC_SESSION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionStateChangeEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b5bad703-5952-48b3-9321-7f4500521506}')
    @commethod(7)
    def get_Session(self, ppSession: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SESSION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(self, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCSessionStateChangeEvent2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCSessionStateChangeEvent
    _iid_ = Guid('{4f933171-6f95-4880-80d9-2ec8d495d261}')
    @commethod(11)
    def get_MediaTypes(self, pMediaTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RemotePreferredSecurityLevel(self, enSecurityType: Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsForked(self, pfIsForked: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRemoteSessionDescription(self, pbstrContentType: POINTER(Windows.Win32.Foundation.BSTR), pbstrSessionDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCUserSearch(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b619882b-860c-4db4-be1b-693b6505bbe5}')
    @commethod(3)
    def CreateQuery(self, ppQuery: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCUserSearchQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ExecuteSearch(self, pQuery: Windows.Win32.System.RealTimeCommunications.IRTCUserSearchQuery_head, pProfile: Windows.Win32.System.RealTimeCommunications.IRTCProfile_head, lCookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCUserSearchQuery(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{288300f5-d23a-4365-9a73-9985c98c2881}')
    @commethod(3)
    def put_SearchTerm(self, bstrName: Windows.Win32.Foundation.BSTR, bstrValue: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SearchTerm(self, bstrName: Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_SearchTerms(self, pbstrNames: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_SearchPreference(self, enPreference: Windows.Win32.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE, lValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_SearchPreference(self, enPreference: Windows.Win32.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE, plValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SearchDomain(self, bstrDomain: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SearchDomain(self, pbstrDomain: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCUserSearchResult(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{851278b2-9592-480f-8db5-2de86b26b54d}')
    @commethod(3)
    def get_Value(self, enColumn: Windows.Win32.System.RealTimeCommunications.RTC_USER_SEARCH_COLUMN, pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCUserSearchResultsEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d8c8c3cd-7fac-4088-81c5-c24cbc0938e3}')
    @commethod(7)
    def EnumerateResults(self, ppEnum: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCEnumUserSearchResults_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Results(self, ppCollection: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Query(self, ppQuery: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCUserSearchQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Cookie(self, plCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MoreAvailable(self, pfMoreAvailable: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCWatcher(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCPresenceContact
    _iid_ = Guid('{c7cedad8-346b-4d1b-ac02-a2088df9be4f}')
    @commethod(11)
    def get_State(self, penState: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_WATCHER_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_State(self, enState: Windows.Win32.System.RealTimeCommunications.RTC_WATCHER_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCWatcher2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCWatcher
    _iid_ = Guid('{d4d9967f-d011-4b1d-91e3-aba78f96393d}')
    @commethod(13)
    def get_Profile(self, ppProfile: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCProfile2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Scope(self, penScope: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_ACE_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCWatcherEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f30d7261-587a-424f-822c-312788f43548}')
    @commethod(7)
    def get_Watcher(self, ppWatcher: POINTER(Windows.Win32.System.RealTimeCommunications.IRTCWatcher_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRTCWatcherEvent2(ComPtr):
    extends: Windows.Win32.System.RealTimeCommunications.IRTCWatcherEvent
    _iid_ = Guid('{e52891e8-188c-49af-b005-98ed13f83f9c}')
    @commethod(8)
    def get_EventType(self, pEventType: POINTER(Windows.Win32.System.RealTimeCommunications.RTC_WATCHER_EVENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(self, plStatusCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransportSettingsInternal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5123e076-29e3-4bfd-84fe-0192d411e3e8}')
    @commethod(3)
    def ApplySetting(self, Setting: POINTER(Windows.Win32.System.RealTimeCommunications.TRANSPORT_SETTING_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySetting(self, Setting: POINTER(Windows.Win32.System.RealTimeCommunications.TRANSPORT_SETTING_head)) -> Windows.Win32.Foundation.HRESULT: ...
RTCClient = Guid('{7a42ea29-a2b7-40c4-b091-f6f024aa89be}')
RTC_ACE_SCOPE = Int32
RTCAS_SCOPE_USER: RTC_ACE_SCOPE = 0
RTCAS_SCOPE_DOMAIN: RTC_ACE_SCOPE = 1
RTCAS_SCOPE_ALL: RTC_ACE_SCOPE = 2
RTC_ANSWER_MODE = Int32
RTCAM_OFFER_SESSION_EVENT: RTC_ANSWER_MODE = 0
RTCAM_AUTOMATICALLY_ACCEPT: RTC_ANSWER_MODE = 1
RTCAM_AUTOMATICALLY_REJECT: RTC_ANSWER_MODE = 2
RTCAM_NOT_SUPPORTED: RTC_ANSWER_MODE = 3
RTC_AUDIO_DEVICE = Int32
RTCAD_SPEAKER: RTC_AUDIO_DEVICE = 0
RTCAD_MICROPHONE: RTC_AUDIO_DEVICE = 1
RTC_BUDDY_EVENT_TYPE = Int32
RTCBET_BUDDY_ADD: RTC_BUDDY_EVENT_TYPE = 0
RTCBET_BUDDY_REMOVE: RTC_BUDDY_EVENT_TYPE = 1
RTCBET_BUDDY_UPDATE: RTC_BUDDY_EVENT_TYPE = 2
RTCBET_BUDDY_STATE_CHANGE: RTC_BUDDY_EVENT_TYPE = 3
RTCBET_BUDDY_ROAMED: RTC_BUDDY_EVENT_TYPE = 4
RTCBET_BUDDY_SUBSCRIBED: RTC_BUDDY_EVENT_TYPE = 5
RTC_BUDDY_SUBSCRIPTION_TYPE = Int32
RTCBT_SUBSCRIBED: RTC_BUDDY_SUBSCRIPTION_TYPE = 0
RTCBT_ALWAYS_OFFLINE: RTC_BUDDY_SUBSCRIPTION_TYPE = 1
RTCBT_ALWAYS_ONLINE: RTC_BUDDY_SUBSCRIPTION_TYPE = 2
RTCBT_POLL: RTC_BUDDY_SUBSCRIPTION_TYPE = 3
RTC_CLIENT_EVENT_TYPE = Int32
RTCCET_VOLUME_CHANGE: RTC_CLIENT_EVENT_TYPE = 0
RTCCET_DEVICE_CHANGE: RTC_CLIENT_EVENT_TYPE = 1
RTCCET_NETWORK_QUALITY_CHANGE: RTC_CLIENT_EVENT_TYPE = 2
RTCCET_ASYNC_CLEANUP_DONE: RTC_CLIENT_EVENT_TYPE = 3
RTC_DTMF = Int32
RTC_DTMF_0: RTC_DTMF = 0
RTC_DTMF_1: RTC_DTMF = 1
RTC_DTMF_2: RTC_DTMF = 2
RTC_DTMF_3: RTC_DTMF = 3
RTC_DTMF_4: RTC_DTMF = 4
RTC_DTMF_5: RTC_DTMF = 5
RTC_DTMF_6: RTC_DTMF = 6
RTC_DTMF_7: RTC_DTMF = 7
RTC_DTMF_8: RTC_DTMF = 8
RTC_DTMF_9: RTC_DTMF = 9
RTC_DTMF_STAR: RTC_DTMF = 10
RTC_DTMF_POUND: RTC_DTMF = 11
RTC_DTMF_A: RTC_DTMF = 12
RTC_DTMF_B: RTC_DTMF = 13
RTC_DTMF_C: RTC_DTMF = 14
RTC_DTMF_D: RTC_DTMF = 15
RTC_DTMF_FLASH: RTC_DTMF = 16
RTC_EVENT = Int32
RTCE_CLIENT: RTC_EVENT = 0
RTCE_REGISTRATION_STATE_CHANGE: RTC_EVENT = 1
RTCE_SESSION_STATE_CHANGE: RTC_EVENT = 2
RTCE_SESSION_OPERATION_COMPLETE: RTC_EVENT = 3
RTCE_PARTICIPANT_STATE_CHANGE: RTC_EVENT = 4
RTCE_MEDIA: RTC_EVENT = 5
RTCE_INTENSITY: RTC_EVENT = 6
RTCE_MESSAGING: RTC_EVENT = 7
RTCE_BUDDY: RTC_EVENT = 8
RTCE_WATCHER: RTC_EVENT = 9
RTCE_PROFILE: RTC_EVENT = 10
RTCE_USERSEARCH: RTC_EVENT = 11
RTCE_INFO: RTC_EVENT = 12
RTCE_GROUP: RTC_EVENT = 13
RTCE_MEDIA_REQUEST: RTC_EVENT = 14
RTCE_ROAMING: RTC_EVENT = 15
RTCE_PRESENCE_PROPERTY: RTC_EVENT = 16
RTCE_PRESENCE_DATA: RTC_EVENT = 17
RTCE_PRESENCE_STATUS: RTC_EVENT = 18
RTCE_SESSION_REFER_STATUS: RTC_EVENT = 19
RTCE_SESSION_REFERRED: RTC_EVENT = 20
RTCE_REINVITE: RTC_EVENT = 21
RTC_GROUP_EVENT_TYPE = Int32
RTCGET_GROUP_ADD: RTC_GROUP_EVENT_TYPE = 0
RTCGET_GROUP_REMOVE: RTC_GROUP_EVENT_TYPE = 1
RTCGET_GROUP_UPDATE: RTC_GROUP_EVENT_TYPE = 2
RTCGET_GROUP_BUDDY_ADD: RTC_GROUP_EVENT_TYPE = 3
RTCGET_GROUP_BUDDY_REMOVE: RTC_GROUP_EVENT_TYPE = 4
RTCGET_GROUP_ROAMED: RTC_GROUP_EVENT_TYPE = 5
RTC_LISTEN_MODE = Int32
RTCLM_NONE: RTC_LISTEN_MODE = 0
RTCLM_DYNAMIC: RTC_LISTEN_MODE = 1
RTCLM_BOTH: RTC_LISTEN_MODE = 2
RTC_MEDIA_EVENT_REASON = Int32
RTCMER_NORMAL: RTC_MEDIA_EVENT_REASON = 0
RTCMER_HOLD: RTC_MEDIA_EVENT_REASON = 1
RTCMER_TIMEOUT: RTC_MEDIA_EVENT_REASON = 2
RTCMER_BAD_DEVICE: RTC_MEDIA_EVENT_REASON = 3
RTCMER_NO_PORT: RTC_MEDIA_EVENT_REASON = 4
RTCMER_PORT_MAPPING_FAILED: RTC_MEDIA_EVENT_REASON = 5
RTCMER_REMOTE_REQUEST: RTC_MEDIA_EVENT_REASON = 6
RTC_MEDIA_EVENT_TYPE = Int32
RTCMET_STOPPED: RTC_MEDIA_EVENT_TYPE = 0
RTCMET_STARTED: RTC_MEDIA_EVENT_TYPE = 1
RTCMET_FAILED: RTC_MEDIA_EVENT_TYPE = 2
RTC_MESSAGING_EVENT_TYPE = Int32
RTCMSET_MESSAGE: RTC_MESSAGING_EVENT_TYPE = 0
RTCMSET_STATUS: RTC_MESSAGING_EVENT_TYPE = 1
RTC_MESSAGING_USER_STATUS = Int32
RTCMUS_IDLE: RTC_MESSAGING_USER_STATUS = 0
RTCMUS_TYPING: RTC_MESSAGING_USER_STATUS = 1
RTC_OFFER_WATCHER_MODE = Int32
RTCOWM_OFFER_WATCHER_EVENT: RTC_OFFER_WATCHER_MODE = 0
RTCOWM_AUTOMATICALLY_ADD_WATCHER: RTC_OFFER_WATCHER_MODE = 1
RTC_PARTICIPANT_STATE = Int32
RTCPS_IDLE: RTC_PARTICIPANT_STATE = 0
RTCPS_PENDING: RTC_PARTICIPANT_STATE = 1
RTCPS_INCOMING: RTC_PARTICIPANT_STATE = 2
RTCPS_ANSWERING: RTC_PARTICIPANT_STATE = 3
RTCPS_INPROGRESS: RTC_PARTICIPANT_STATE = 4
RTCPS_ALERTING: RTC_PARTICIPANT_STATE = 5
RTCPS_CONNECTED: RTC_PARTICIPANT_STATE = 6
RTCPS_DISCONNECTING: RTC_PARTICIPANT_STATE = 7
RTCPS_DISCONNECTED: RTC_PARTICIPANT_STATE = 8
RTC_PORT_TYPE = Int32
RTCPT_AUDIO_RTP: RTC_PORT_TYPE = 0
RTCPT_AUDIO_RTCP: RTC_PORT_TYPE = 1
RTCPT_VIDEO_RTP: RTC_PORT_TYPE = 2
RTCPT_VIDEO_RTCP: RTC_PORT_TYPE = 3
RTCPT_SIP: RTC_PORT_TYPE = 4
RTC_PRESENCE_PROPERTY = Int32
RTCPP_PHONENUMBER: RTC_PRESENCE_PROPERTY = 0
RTCPP_DISPLAYNAME: RTC_PRESENCE_PROPERTY = 1
RTCPP_EMAIL: RTC_PRESENCE_PROPERTY = 2
RTCPP_DEVICE_NAME: RTC_PRESENCE_PROPERTY = 3
RTCPP_MULTIPLE: RTC_PRESENCE_PROPERTY = 4
RTC_PRESENCE_STATUS = Int32
RTCXS_PRESENCE_OFFLINE: RTC_PRESENCE_STATUS = 0
RTCXS_PRESENCE_ONLINE: RTC_PRESENCE_STATUS = 1
RTCXS_PRESENCE_AWAY: RTC_PRESENCE_STATUS = 2
RTCXS_PRESENCE_IDLE: RTC_PRESENCE_STATUS = 3
RTCXS_PRESENCE_BUSY: RTC_PRESENCE_STATUS = 4
RTCXS_PRESENCE_BE_RIGHT_BACK: RTC_PRESENCE_STATUS = 5
RTCXS_PRESENCE_ON_THE_PHONE: RTC_PRESENCE_STATUS = 6
RTCXS_PRESENCE_OUT_TO_LUNCH: RTC_PRESENCE_STATUS = 7
RTC_PRIVACY_MODE = Int32
RTCPM_BLOCK_LIST_EXCLUDED: RTC_PRIVACY_MODE = 0
RTCPM_ALLOW_LIST_ONLY: RTC_PRIVACY_MODE = 1
RTC_PROFILE_EVENT_TYPE = Int32
RTCPFET_PROFILE_GET: RTC_PROFILE_EVENT_TYPE = 0
RTCPFET_PROFILE_UPDATE: RTC_PROFILE_EVENT_TYPE = 1
RTC_PROVIDER_URI = Int32
RTCPU_URIHOMEPAGE: RTC_PROVIDER_URI = 0
RTCPU_URIHELPDESK: RTC_PROVIDER_URI = 1
RTCPU_URIPERSONALACCOUNT: RTC_PROVIDER_URI = 2
RTCPU_URIDISPLAYDURINGCALL: RTC_PROVIDER_URI = 3
RTCPU_URIDISPLAYDURINGIDLE: RTC_PROVIDER_URI = 4
RTC_REGISTRATION_STATE = Int32
RTCRS_NOT_REGISTERED: RTC_REGISTRATION_STATE = 0
RTCRS_REGISTERING: RTC_REGISTRATION_STATE = 1
RTCRS_REGISTERED: RTC_REGISTRATION_STATE = 2
RTCRS_REJECTED: RTC_REGISTRATION_STATE = 3
RTCRS_UNREGISTERING: RTC_REGISTRATION_STATE = 4
RTCRS_ERROR: RTC_REGISTRATION_STATE = 5
RTCRS_LOGGED_OFF: RTC_REGISTRATION_STATE = 6
RTCRS_LOCAL_PA_LOGGED_OFF: RTC_REGISTRATION_STATE = 7
RTCRS_REMOTE_PA_LOGGED_OFF: RTC_REGISTRATION_STATE = 8
RTC_REINVITE_STATE = Int32
RTCRIN_INCOMING: RTC_REINVITE_STATE = 0
RTCRIN_SUCCEEDED: RTC_REINVITE_STATE = 1
RTCRIN_FAIL: RTC_REINVITE_STATE = 2
RTC_RING_TYPE = Int32
RTCRT_PHONE: RTC_RING_TYPE = 0
RTCRT_MESSAGE: RTC_RING_TYPE = 1
RTCRT_RINGBACK: RTC_RING_TYPE = 2
RTC_ROAMING_EVENT_TYPE = Int32
RTCRET_BUDDY_ROAMING: RTC_ROAMING_EVENT_TYPE = 0
RTCRET_WATCHER_ROAMING: RTC_ROAMING_EVENT_TYPE = 1
RTCRET_PRESENCE_ROAMING: RTC_ROAMING_EVENT_TYPE = 2
RTCRET_PROFILE_ROAMING: RTC_ROAMING_EVENT_TYPE = 3
RTCRET_WPENDING_ROAMING: RTC_ROAMING_EVENT_TYPE = 4
RTC_SECURITY_LEVEL = Int32
RTCSECL_UNSUPPORTED: RTC_SECURITY_LEVEL = 1
RTCSECL_SUPPORTED: RTC_SECURITY_LEVEL = 2
RTCSECL_REQUIRED: RTC_SECURITY_LEVEL = 3
RTC_SECURITY_TYPE = Int32
RTCSECT_AUDIO_VIDEO_MEDIA_ENCRYPTION: RTC_SECURITY_TYPE = 0
RTCSECT_T120_MEDIA_ENCRYPTION: RTC_SECURITY_TYPE = 1
RTC_SESSION_REFER_STATUS = Int32
RTCSRS_REFERRING: RTC_SESSION_REFER_STATUS = 0
RTCSRS_ACCEPTED: RTC_SESSION_REFER_STATUS = 1
RTCSRS_ERROR: RTC_SESSION_REFER_STATUS = 2
RTCSRS_REJECTED: RTC_SESSION_REFER_STATUS = 3
RTCSRS_DROPPED: RTC_SESSION_REFER_STATUS = 4
RTCSRS_DONE: RTC_SESSION_REFER_STATUS = 5
RTC_SESSION_STATE = Int32
RTCSS_IDLE: RTC_SESSION_STATE = 0
RTCSS_INCOMING: RTC_SESSION_STATE = 1
RTCSS_ANSWERING: RTC_SESSION_STATE = 2
RTCSS_INPROGRESS: RTC_SESSION_STATE = 3
RTCSS_CONNECTED: RTC_SESSION_STATE = 4
RTCSS_DISCONNECTED: RTC_SESSION_STATE = 5
RTCSS_HOLD: RTC_SESSION_STATE = 6
RTCSS_REFER: RTC_SESSION_STATE = 7
RTC_SESSION_TYPE = Int32
RTCST_PC_TO_PC: RTC_SESSION_TYPE = 0
RTCST_PC_TO_PHONE: RTC_SESSION_TYPE = 1
RTCST_PHONE_TO_PHONE: RTC_SESSION_TYPE = 2
RTCST_IM: RTC_SESSION_TYPE = 3
RTCST_MULTIPARTY_IM: RTC_SESSION_TYPE = 4
RTCST_APPLICATION: RTC_SESSION_TYPE = 5
RTC_T120_APPLET = Int32
RTCTA_WHITEBOARD: RTC_T120_APPLET = 0
RTCTA_APPSHARING: RTC_T120_APPLET = 1
RTC_TERMINATE_REASON = Int32
RTCTR_NORMAL: RTC_TERMINATE_REASON = 0
RTCTR_DND: RTC_TERMINATE_REASON = 1
RTCTR_BUSY: RTC_TERMINATE_REASON = 2
RTCTR_REJECT: RTC_TERMINATE_REASON = 3
RTCTR_TIMEOUT: RTC_TERMINATE_REASON = 4
RTCTR_SHUTDOWN: RTC_TERMINATE_REASON = 5
RTCTR_INSUFFICIENT_SECURITY_LEVEL: RTC_TERMINATE_REASON = 6
RTCTR_NOT_SUPPORTED: RTC_TERMINATE_REASON = 7
RTC_USER_SEARCH_COLUMN = Int32
RTCUSC_URI: RTC_USER_SEARCH_COLUMN = 0
RTCUSC_DISPLAYNAME: RTC_USER_SEARCH_COLUMN = 1
RTCUSC_TITLE: RTC_USER_SEARCH_COLUMN = 2
RTCUSC_OFFICE: RTC_USER_SEARCH_COLUMN = 3
RTCUSC_PHONE: RTC_USER_SEARCH_COLUMN = 4
RTCUSC_COMPANY: RTC_USER_SEARCH_COLUMN = 5
RTCUSC_CITY: RTC_USER_SEARCH_COLUMN = 6
RTCUSC_STATE: RTC_USER_SEARCH_COLUMN = 7
RTCUSC_COUNTRY: RTC_USER_SEARCH_COLUMN = 8
RTCUSC_EMAIL: RTC_USER_SEARCH_COLUMN = 9
RTC_USER_SEARCH_PREFERENCE = Int32
RTCUSP_MAX_MATCHES: RTC_USER_SEARCH_PREFERENCE = 0
RTCUSP_TIME_LIMIT: RTC_USER_SEARCH_PREFERENCE = 1
RTC_VIDEO_DEVICE = Int32
RTCVD_RECEIVE: RTC_VIDEO_DEVICE = 0
RTCVD_PREVIEW: RTC_VIDEO_DEVICE = 1
RTC_WATCHER_EVENT_TYPE = Int32
RTCWET_WATCHER_ADD: RTC_WATCHER_EVENT_TYPE = 0
RTCWET_WATCHER_REMOVE: RTC_WATCHER_EVENT_TYPE = 1
RTCWET_WATCHER_UPDATE: RTC_WATCHER_EVENT_TYPE = 2
RTCWET_WATCHER_OFFERING: RTC_WATCHER_EVENT_TYPE = 3
RTCWET_WATCHER_ROAMED: RTC_WATCHER_EVENT_TYPE = 4
RTC_WATCHER_MATCH_MODE = Int32
RTCWMM_EXACT_MATCH: RTC_WATCHER_MATCH_MODE = 0
RTCWMM_BEST_ACE_MATCH: RTC_WATCHER_MATCH_MODE = 1
RTC_WATCHER_STATE = Int32
RTCWS_UNKNOWN: RTC_WATCHER_STATE = 0
RTCWS_OFFERING: RTC_WATCHER_STATE = 1
RTCWS_ALLOWED: RTC_WATCHER_STATE = 2
RTCWS_BLOCKED: RTC_WATCHER_STATE = 3
RTCWS_DENIED: RTC_WATCHER_STATE = 4
RTCWS_PROMPT: RTC_WATCHER_STATE = 5
class TRANSPORT_SETTING(EasyCastStructure):
    SettingId: Windows.Win32.Networking.WinSock.TRANSPORT_SETTING_ID
    Length: POINTER(UInt32)
    Value: POINTER(Byte)
make_head(_module, 'INetworkTransportSettings')
make_head(_module, 'INotificationTransportSync')
make_head(_module, 'IRTCBuddy')
make_head(_module, 'IRTCBuddy2')
make_head(_module, 'IRTCBuddyEvent')
make_head(_module, 'IRTCBuddyEvent2')
make_head(_module, 'IRTCBuddyGroup')
make_head(_module, 'IRTCBuddyGroupEvent')
make_head(_module, 'IRTCClient')
make_head(_module, 'IRTCClient2')
make_head(_module, 'IRTCClientEvent')
make_head(_module, 'IRTCClientPortManagement')
make_head(_module, 'IRTCClientPresence')
make_head(_module, 'IRTCClientPresence2')
make_head(_module, 'IRTCClientProvisioning')
make_head(_module, 'IRTCClientProvisioning2')
make_head(_module, 'IRTCCollection')
make_head(_module, 'IRTCDispatchEventNotification')
make_head(_module, 'IRTCEnumBuddies')
make_head(_module, 'IRTCEnumGroups')
make_head(_module, 'IRTCEnumParticipants')
make_head(_module, 'IRTCEnumPresenceDevices')
make_head(_module, 'IRTCEnumProfiles')
make_head(_module, 'IRTCEnumUserSearchResults')
make_head(_module, 'IRTCEnumWatchers')
make_head(_module, 'IRTCEventNotification')
make_head(_module, 'IRTCInfoEvent')
make_head(_module, 'IRTCIntensityEvent')
make_head(_module, 'IRTCMediaEvent')
make_head(_module, 'IRTCMediaRequestEvent')
make_head(_module, 'IRTCMessagingEvent')
make_head(_module, 'IRTCParticipant')
make_head(_module, 'IRTCParticipantStateChangeEvent')
make_head(_module, 'IRTCPortManager')
make_head(_module, 'IRTCPresenceContact')
make_head(_module, 'IRTCPresenceDataEvent')
make_head(_module, 'IRTCPresenceDevice')
make_head(_module, 'IRTCPresencePropertyEvent')
make_head(_module, 'IRTCPresenceStatusEvent')
make_head(_module, 'IRTCProfile')
make_head(_module, 'IRTCProfile2')
make_head(_module, 'IRTCProfileEvent')
make_head(_module, 'IRTCProfileEvent2')
make_head(_module, 'IRTCReInviteEvent')
make_head(_module, 'IRTCRegistrationStateChangeEvent')
make_head(_module, 'IRTCRoamingEvent')
make_head(_module, 'IRTCSession')
make_head(_module, 'IRTCSession2')
make_head(_module, 'IRTCSessionCallControl')
make_head(_module, 'IRTCSessionDescriptionManager')
make_head(_module, 'IRTCSessionOperationCompleteEvent')
make_head(_module, 'IRTCSessionOperationCompleteEvent2')
make_head(_module, 'IRTCSessionPortManagement')
make_head(_module, 'IRTCSessionReferStatusEvent')
make_head(_module, 'IRTCSessionReferredEvent')
make_head(_module, 'IRTCSessionStateChangeEvent')
make_head(_module, 'IRTCSessionStateChangeEvent2')
make_head(_module, 'IRTCUserSearch')
make_head(_module, 'IRTCUserSearchQuery')
make_head(_module, 'IRTCUserSearchResult')
make_head(_module, 'IRTCUserSearchResultsEvent')
make_head(_module, 'IRTCWatcher')
make_head(_module, 'IRTCWatcher2')
make_head(_module, 'IRTCWatcherEvent')
make_head(_module, 'IRTCWatcherEvent2')
make_head(_module, 'ITransportSettingsInternal')
make_head(_module, 'TRANSPORT_SETTING')
