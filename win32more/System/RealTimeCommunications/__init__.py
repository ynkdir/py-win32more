from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Media.DirectShow
import win32more.Networking.WinSock
import win32more.System.Com
import win32more.System.RealTimeCommunications
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
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
RTC_E_SIP_CODECS_DO_NOT_MATCH: win32more.Foundation.HRESULT = -2131886080
RTC_E_SIP_STREAM_PRESENT: win32more.Foundation.HRESULT = -2131886079
RTC_E_SIP_STREAM_NOT_PRESENT: win32more.Foundation.HRESULT = -2131886078
RTC_E_SIP_NO_STREAM: win32more.Foundation.HRESULT = -2131886077
RTC_E_SIP_PARSE_FAILED: win32more.Foundation.HRESULT = -2131886076
RTC_E_SIP_HEADER_NOT_PRESENT: win32more.Foundation.HRESULT = -2131886075
RTC_E_SDP_NOT_PRESENT: win32more.Foundation.HRESULT = -2131886074
RTC_E_SDP_PARSE_FAILED: win32more.Foundation.HRESULT = -2131886073
RTC_E_SDP_UPDATE_FAILED: win32more.Foundation.HRESULT = -2131886072
RTC_E_SDP_MULTICAST: win32more.Foundation.HRESULT = -2131886071
RTC_E_SDP_CONNECTION_ADDR: win32more.Foundation.HRESULT = -2131886070
RTC_E_SDP_NO_MEDIA: win32more.Foundation.HRESULT = -2131886069
RTC_E_SIP_TIMEOUT: win32more.Foundation.HRESULT = -2131886068
RTC_E_SDP_FAILED_TO_BUILD: win32more.Foundation.HRESULT = -2131886067
RTC_E_SIP_INVITE_TRANSACTION_PENDING: win32more.Foundation.HRESULT = -2131886066
RTC_E_SIP_AUTH_HEADER_SENT: win32more.Foundation.HRESULT = -2131886065
RTC_E_SIP_AUTH_TYPE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2131886064
RTC_E_SIP_AUTH_FAILED: win32more.Foundation.HRESULT = -2131886063
RTC_E_INVALID_SIP_URL: win32more.Foundation.HRESULT = -2131886062
RTC_E_DESTINATION_ADDRESS_LOCAL: win32more.Foundation.HRESULT = -2131886061
RTC_E_INVALID_ADDRESS_LOCAL: win32more.Foundation.HRESULT = -2131886060
RTC_E_DESTINATION_ADDRESS_MULTICAST: win32more.Foundation.HRESULT = -2131886059
RTC_E_INVALID_PROXY_ADDRESS: win32more.Foundation.HRESULT = -2131886058
RTC_E_SIP_TRANSPORT_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2131886057
RTC_E_SIP_NEED_MORE_DATA: win32more.Foundation.HRESULT = -2131886056
RTC_E_SIP_CALL_DISCONNECTED: win32more.Foundation.HRESULT = -2131886055
RTC_E_SIP_REQUEST_DESTINATION_ADDR_NOT_PRESENT: win32more.Foundation.HRESULT = -2131886054
RTC_E_SIP_UDP_SIZE_EXCEEDED: win32more.Foundation.HRESULT = -2131886053
RTC_E_SIP_SSL_TUNNEL_FAILED: win32more.Foundation.HRESULT = -2131886052
RTC_E_SIP_SSL_NEGOTIATION_TIMEOUT: win32more.Foundation.HRESULT = -2131886051
RTC_E_SIP_STACK_SHUTDOWN: win32more.Foundation.HRESULT = -2131886050
RTC_E_MEDIA_CONTROLLER_STATE: win32more.Foundation.HRESULT = -2131886049
RTC_E_MEDIA_NEED_TERMINAL: win32more.Foundation.HRESULT = -2131886048
RTC_E_MEDIA_AUDIO_DEVICE_NOT_AVAILABLE: win32more.Foundation.HRESULT = -2131886047
RTC_E_MEDIA_VIDEO_DEVICE_NOT_AVAILABLE: win32more.Foundation.HRESULT = -2131886046
RTC_E_START_STREAM: win32more.Foundation.HRESULT = -2131886045
RTC_E_MEDIA_AEC: win32more.Foundation.HRESULT = -2131886044
RTC_E_CLIENT_NOT_INITIALIZED: win32more.Foundation.HRESULT = -2131886043
RTC_E_CLIENT_ALREADY_INITIALIZED: win32more.Foundation.HRESULT = -2131886042
RTC_E_CLIENT_ALREADY_SHUT_DOWN: win32more.Foundation.HRESULT = -2131886041
RTC_E_PRESENCE_NOT_ENABLED: win32more.Foundation.HRESULT = -2131886040
RTC_E_INVALID_SESSION_TYPE: win32more.Foundation.HRESULT = -2131886039
RTC_E_INVALID_SESSION_STATE: win32more.Foundation.HRESULT = -2131886038
RTC_E_NO_PROFILE: win32more.Foundation.HRESULT = -2131886037
RTC_E_LOCAL_PHONE_NEEDED: win32more.Foundation.HRESULT = -2131886036
RTC_E_NO_DEVICE: win32more.Foundation.HRESULT = -2131886035
RTC_E_INVALID_PROFILE: win32more.Foundation.HRESULT = -2131886034
RTC_E_PROFILE_NO_PROVISION: win32more.Foundation.HRESULT = -2131886033
RTC_E_PROFILE_NO_KEY: win32more.Foundation.HRESULT = -2131886032
RTC_E_PROFILE_NO_NAME: win32more.Foundation.HRESULT = -2131886031
RTC_E_PROFILE_NO_USER: win32more.Foundation.HRESULT = -2131886030
RTC_E_PROFILE_NO_USER_URI: win32more.Foundation.HRESULT = -2131886029
RTC_E_PROFILE_NO_SERVER: win32more.Foundation.HRESULT = -2131886028
RTC_E_PROFILE_NO_SERVER_ADDRESS: win32more.Foundation.HRESULT = -2131886027
RTC_E_PROFILE_NO_SERVER_PROTOCOL: win32more.Foundation.HRESULT = -2131886026
RTC_E_PROFILE_INVALID_SERVER_PROTOCOL: win32more.Foundation.HRESULT = -2131886025
RTC_E_PROFILE_INVALID_SERVER_AUTHMETHOD: win32more.Foundation.HRESULT = -2131886024
RTC_E_PROFILE_INVALID_SERVER_ROLE: win32more.Foundation.HRESULT = -2131886023
RTC_E_PROFILE_MULTIPLE_REGISTRARS: win32more.Foundation.HRESULT = -2131886022
RTC_E_PROFILE_INVALID_SESSION: win32more.Foundation.HRESULT = -2131886021
RTC_E_PROFILE_INVALID_SESSION_PARTY: win32more.Foundation.HRESULT = -2131886020
RTC_E_PROFILE_INVALID_SESSION_TYPE: win32more.Foundation.HRESULT = -2131886019
RTC_E_OPERATION_WITH_TOO_MANY_PARTICIPANTS: win32more.Foundation.HRESULT = -2131886018
RTC_E_BASIC_AUTH_SET_TLS: win32more.Foundation.HRESULT = -2131886017
RTC_E_SIP_HIGH_SECURITY_SET_TLS: win32more.Foundation.HRESULT = -2131886016
RTC_S_ROAMING_NOT_SUPPORTED: win32more.Foundation.HRESULT = 15597633
RTC_E_PROFILE_SERVER_UNAUTHORIZED: win32more.Foundation.HRESULT = -2131886014
RTC_E_DUPLICATE_REALM: win32more.Foundation.HRESULT = -2131886013
RTC_E_POLICY_NOT_ALLOW: win32more.Foundation.HRESULT = -2131886012
RTC_E_PORT_MAPPING_UNAVAILABLE: win32more.Foundation.HRESULT = -2131886011
RTC_E_PORT_MAPPING_FAILED: win32more.Foundation.HRESULT = -2131886010
RTC_E_SECURITY_LEVEL_NOT_COMPATIBLE: win32more.Foundation.HRESULT = -2131886009
RTC_E_SECURITY_LEVEL_NOT_DEFINED: win32more.Foundation.HRESULT = -2131886008
RTC_E_SECURITY_LEVEL_NOT_SUPPORTED_BY_PARTICIPANT: win32more.Foundation.HRESULT = -2131886007
RTC_E_DUPLICATE_BUDDY: win32more.Foundation.HRESULT = -2131886006
RTC_E_DUPLICATE_WATCHER: win32more.Foundation.HRESULT = -2131886005
RTC_E_MALFORMED_XML: win32more.Foundation.HRESULT = -2131886004
RTC_E_ROAMING_OPERATION_INTERRUPTED: win32more.Foundation.HRESULT = -2131886003
RTC_E_ROAMING_FAILED: win32more.Foundation.HRESULT = -2131886002
RTC_E_INVALID_BUDDY_LIST: win32more.Foundation.HRESULT = -2131886001
RTC_E_INVALID_ACL_LIST: win32more.Foundation.HRESULT = -2131886000
RTC_E_NO_GROUP: win32more.Foundation.HRESULT = -2131885999
RTC_E_DUPLICATE_GROUP: win32more.Foundation.HRESULT = -2131885998
RTC_E_TOO_MANY_GROUPS: win32more.Foundation.HRESULT = -2131885997
RTC_E_NO_BUDDY: win32more.Foundation.HRESULT = -2131885996
RTC_E_NO_WATCHER: win32more.Foundation.HRESULT = -2131885995
RTC_E_NO_REALM: win32more.Foundation.HRESULT = -2131885994
RTC_E_NO_TRANSPORT: win32more.Foundation.HRESULT = -2131885993
RTC_E_NOT_EXIST: win32more.Foundation.HRESULT = -2131885992
RTC_E_INVALID_PREFERENCE_LIST: win32more.Foundation.HRESULT = -2131885991
RTC_E_MAX_PENDING_OPERATIONS: win32more.Foundation.HRESULT = -2131885990
RTC_E_TOO_MANY_RETRIES: win32more.Foundation.HRESULT = -2131885989
RTC_E_INVALID_PORTRANGE: win32more.Foundation.HRESULT = -2131885988
RTC_E_SIP_CALL_CONNECTION_NOT_ESTABLISHED: win32more.Foundation.HRESULT = -2131885987
RTC_E_SIP_ADDITIONAL_PARTY_IN_TWO_PARTY_SESSION: win32more.Foundation.HRESULT = -2131885986
RTC_E_SIP_PARTY_ALREADY_IN_SESSION: win32more.Foundation.HRESULT = -2131885985
RTC_E_SIP_OTHER_PARTY_JOIN_IN_PROGRESS: win32more.Foundation.HRESULT = -2131885984
RTC_E_INVALID_OBJECT_STATE: win32more.Foundation.HRESULT = -2131885983
RTC_E_PRESENCE_ENABLED: win32more.Foundation.HRESULT = -2131885982
RTC_E_ROAMING_ENABLED: win32more.Foundation.HRESULT = -2131885981
RTC_E_SIP_TLS_INCOMPATIBLE_ENCRYPTION: win32more.Foundation.HRESULT = -2131885980
RTC_E_SIP_INVALID_CERTIFICATE: win32more.Foundation.HRESULT = -2131885979
RTC_E_SIP_DNS_FAIL: win32more.Foundation.HRESULT = -2131885978
RTC_E_SIP_TCP_FAIL: win32more.Foundation.HRESULT = -2131885977
RTC_E_TOO_SMALL_EXPIRES_VALUE: win32more.Foundation.HRESULT = -2131885976
RTC_E_SIP_TLS_FAIL: win32more.Foundation.HRESULT = -2131885975
RTC_E_NOT_PRESENCE_PROFILE: win32more.Foundation.HRESULT = -2131885974
RTC_E_SIP_INVITEE_PARTY_TIMEOUT: win32more.Foundation.HRESULT = -2131885973
RTC_E_SIP_AUTH_TIME_SKEW: win32more.Foundation.HRESULT = -2131885972
RTC_E_INVALID_REGISTRATION_STATE: win32more.Foundation.HRESULT = -2131885971
RTC_E_MEDIA_DISABLED: win32more.Foundation.HRESULT = -2131885970
RTC_E_MEDIA_ENABLED: win32more.Foundation.HRESULT = -2131885969
RTC_E_REFER_NOT_ACCEPTED: win32more.Foundation.HRESULT = -2131885968
RTC_E_REFER_NOT_ALLOWED: win32more.Foundation.HRESULT = -2131885967
RTC_E_REFER_NOT_EXIST: win32more.Foundation.HRESULT = -2131885966
RTC_E_SIP_HOLD_OPERATION_PENDING: win32more.Foundation.HRESULT = -2131885965
RTC_E_SIP_UNHOLD_OPERATION_PENDING: win32more.Foundation.HRESULT = -2131885964
RTC_E_MEDIA_SESSION_NOT_EXIST: win32more.Foundation.HRESULT = -2131885963
RTC_E_MEDIA_SESSION_IN_HOLD: win32more.Foundation.HRESULT = -2131885962
RTC_E_ANOTHER_MEDIA_SESSION_ACTIVE: win32more.Foundation.HRESULT = -2131885961
RTC_E_MAX_REDIRECTS: win32more.Foundation.HRESULT = -2131885960
RTC_E_REDIRECT_PROCESSING_FAILED: win32more.Foundation.HRESULT = -2131885959
RTC_E_LISTENING_SOCKET_NOT_EXIST: win32more.Foundation.HRESULT = -2131885958
RTC_E_INVALID_LISTEN_SOCKET: win32more.Foundation.HRESULT = -2131885957
RTC_E_PORT_MANAGER_ALREADY_SET: win32more.Foundation.HRESULT = -2131885956
RTC_E_SECURITY_LEVEL_ALREADY_SET: win32more.Foundation.HRESULT = -2131885955
RTC_E_UDP_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2131885954
RTC_E_SIP_REFER_OPERATION_PENDING: win32more.Foundation.HRESULT = -2131885953
RTC_E_PLATFORM_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2131885952
RTC_E_SIP_PEER_PARTICIPANT_IN_MULTIPARTY_SESSION: win32more.Foundation.HRESULT = -2131885951
RTC_E_NOT_ALLOWED: win32more.Foundation.HRESULT = -2131885950
RTC_E_REGISTRATION_DEACTIVATED: win32more.Foundation.HRESULT = -2131885949
RTC_E_REGISTRATION_REJECTED: win32more.Foundation.HRESULT = -2131885948
RTC_E_REGISTRATION_UNREGISTERED: win32more.Foundation.HRESULT = -2131885947
RTC_E_STATUS_INFO_TRYING: win32more.Foundation.HRESULT = 15663204
RTC_E_STATUS_INFO_RINGING: win32more.Foundation.HRESULT = 15663284
RTC_E_STATUS_INFO_CALL_FORWARDING: win32more.Foundation.HRESULT = 15663285
RTC_E_STATUS_INFO_QUEUED: win32more.Foundation.HRESULT = 15663286
RTC_E_STATUS_SESSION_PROGRESS: win32more.Foundation.HRESULT = 15663287
RTC_E_STATUS_SUCCESS: win32more.Foundation.HRESULT = 15663304
RTC_E_STATUS_REDIRECT_MULTIPLE_CHOICES: win32more.Foundation.HRESULT = -2131820244
RTC_E_STATUS_REDIRECT_MOVED_PERMANENTLY: win32more.Foundation.HRESULT = -2131820243
RTC_E_STATUS_REDIRECT_MOVED_TEMPORARILY: win32more.Foundation.HRESULT = -2131820242
RTC_E_STATUS_REDIRECT_SEE_OTHER: win32more.Foundation.HRESULT = -2131820241
RTC_E_STATUS_REDIRECT_USE_PROXY: win32more.Foundation.HRESULT = -2131820239
RTC_E_STATUS_REDIRECT_ALTERNATIVE_SERVICE: win32more.Foundation.HRESULT = -2131820164
RTC_E_STATUS_CLIENT_BAD_REQUEST: win32more.Foundation.HRESULT = -2131820144
RTC_E_STATUS_CLIENT_UNAUTHORIZED: win32more.Foundation.HRESULT = -2131820143
RTC_E_STATUS_CLIENT_PAYMENT_REQUIRED: win32more.Foundation.HRESULT = -2131820142
RTC_E_STATUS_CLIENT_FORBIDDEN: win32more.Foundation.HRESULT = -2131820141
RTC_E_STATUS_CLIENT_NOT_FOUND: win32more.Foundation.HRESULT = -2131820140
RTC_E_STATUS_CLIENT_METHOD_NOT_ALLOWED: win32more.Foundation.HRESULT = -2131820139
RTC_E_STATUS_CLIENT_NOT_ACCEPTABLE: win32more.Foundation.HRESULT = -2131820138
RTC_E_STATUS_CLIENT_PROXY_AUTHENTICATION_REQUIRED: win32more.Foundation.HRESULT = -2131820137
RTC_E_STATUS_CLIENT_REQUEST_TIMEOUT: win32more.Foundation.HRESULT = -2131820136
RTC_E_STATUS_CLIENT_CONFLICT: win32more.Foundation.HRESULT = -2131820135
RTC_E_STATUS_CLIENT_GONE: win32more.Foundation.HRESULT = -2131820134
RTC_E_STATUS_CLIENT_LENGTH_REQUIRED: win32more.Foundation.HRESULT = -2131820133
RTC_E_STATUS_CLIENT_REQUEST_ENTITY_TOO_LARGE: win32more.Foundation.HRESULT = -2131820131
RTC_E_STATUS_CLIENT_REQUEST_URI_TOO_LARGE: win32more.Foundation.HRESULT = -2131820130
RTC_E_STATUS_CLIENT_UNSUPPORTED_MEDIA_TYPE: win32more.Foundation.HRESULT = -2131820129
RTC_E_STATUS_CLIENT_BAD_EXTENSION: win32more.Foundation.HRESULT = -2131820124
RTC_E_STATUS_CLIENT_TEMPORARILY_NOT_AVAILABLE: win32more.Foundation.HRESULT = -2131820064
RTC_E_STATUS_CLIENT_TRANSACTION_DOES_NOT_EXIST: win32more.Foundation.HRESULT = -2131820063
RTC_E_STATUS_CLIENT_LOOP_DETECTED: win32more.Foundation.HRESULT = -2131820062
RTC_E_STATUS_CLIENT_TOO_MANY_HOPS: win32more.Foundation.HRESULT = -2131820061
RTC_E_STATUS_CLIENT_ADDRESS_INCOMPLETE: win32more.Foundation.HRESULT = -2131820060
RTC_E_STATUS_CLIENT_AMBIGUOUS: win32more.Foundation.HRESULT = -2131820059
RTC_E_STATUS_CLIENT_BUSY_HERE: win32more.Foundation.HRESULT = -2131820058
RTC_E_STATUS_REQUEST_TERMINATED: win32more.Foundation.HRESULT = -2131820057
RTC_E_STATUS_NOT_ACCEPTABLE_HERE: win32more.Foundation.HRESULT = -2131820056
RTC_E_STATUS_SERVER_INTERNAL_ERROR: win32more.Foundation.HRESULT = -2131820044
RTC_E_STATUS_SERVER_NOT_IMPLEMENTED: win32more.Foundation.HRESULT = -2131820043
RTC_E_STATUS_SERVER_BAD_GATEWAY: win32more.Foundation.HRESULT = -2131820042
RTC_E_STATUS_SERVER_SERVICE_UNAVAILABLE: win32more.Foundation.HRESULT = -2131820041
RTC_E_STATUS_SERVER_SERVER_TIMEOUT: win32more.Foundation.HRESULT = -2131820040
RTC_E_STATUS_SERVER_VERSION_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2131820039
RTC_E_STATUS_GLOBAL_BUSY_EVERYWHERE: win32more.Foundation.HRESULT = -2131819944
RTC_E_STATUS_GLOBAL_DECLINE: win32more.Foundation.HRESULT = -2131819941
RTC_E_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE: win32more.Foundation.HRESULT = -2131819940
RTC_E_STATUS_GLOBAL_NOT_ACCEPTABLE: win32more.Foundation.HRESULT = -2131819938
RTC_E_PINT_STATUS_REJECTED_BUSY: win32more.Foundation.HRESULT = -2131755003
RTC_E_PINT_STATUS_REJECTED_NO_ANSWER: win32more.Foundation.HRESULT = -2131755002
RTC_E_PINT_STATUS_REJECTED_ALL_BUSY: win32more.Foundation.HRESULT = -2131755001
RTC_E_PINT_STATUS_REJECTED_PL_FAILED: win32more.Foundation.HRESULT = -2131755000
RTC_E_PINT_STATUS_REJECTED_SW_FAILED: win32more.Foundation.HRESULT = -2131754999
RTC_E_PINT_STATUS_REJECTED_CANCELLED: win32more.Foundation.HRESULT = -2131754998
RTC_E_PINT_STATUS_REJECTED_BADNUMBER: win32more.Foundation.HRESULT = -2131754997
class INetworkTransportSettings(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5e7abb2c-f2c1-4a61-bd-35-de-b7-a0-8a-b0-f1')
    @commethod(3)
    def ApplySetting(SettingId: POINTER(win32more.Networking.WinSock.TRANSPORT_SETTING_ID_head), LengthIn: UInt32, ValueIn: c_char_p_no, LengthOut: POINTER(UInt32), ValueOut: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySetting(SettingId: POINTER(win32more.Networking.WinSock.TRANSPORT_SETTING_ID_head), LengthIn: UInt32, ValueIn: c_char_p_no, LengthOut: POINTER(UInt32), ValueOut: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class INotificationTransportSync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79eb1402-0ab8-49c0-9e-14-a1-ae-4b-a9-30-58')
    @commethod(3)
    def CompleteDelivery() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Flush() -> win32more.Foundation.HRESULT: ...
class IRTCBuddy(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCPresenceContact
    Guid = Guid('fcb136c8-7b90-4e0c-be-fe-56-ed-f0-ba-6f-1c')
    @commethod(11)
    def get_Status(penStatus: POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Notes(pbstrNotes: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCBuddy2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCBuddy
    Guid = Guid('102f9588-23e7-40e3-95-4d-cd-7a-1d-5c-03-61')
    @commethod(13)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnumerateGroups(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Groups(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PresenceProperty(enProperty: win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EnumeratePresenceDevices(ppEnumDevices: POINTER(win32more.System.RealTimeCommunications.IRTCEnumPresenceDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_PresenceDevices(ppDevicesCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_SubscriptionType(penSubscriptionType: POINTER(win32more.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE)) -> win32more.Foundation.HRESULT: ...
class IRTCBuddyEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f36d755d-17e6-404e-95-4f-0f-c0-75-74-c7-8d')
    @commethod(7)
    def get_Buddy(ppBuddy: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head)) -> win32more.Foundation.HRESULT: ...
class IRTCBuddyEvent2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCBuddyEvent
    Guid = Guid('484a7f1e-73f0-4990-bf-c2-60-bc-39-78-a7-20')
    @commethod(8)
    def get_EventType(pEventType: POINTER(win32more.System.RealTimeCommunications.RTC_BUDDY_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCBuddyGroup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('60361e68-9164-4389-a4-c6-d0-b3-92-5b-da-5e')
    @commethod(3)
    def get_Name(pbstrGroupName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_Name(bstrGroupName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddBuddy(pBuddy: win32more.System.RealTimeCommunications.IRTCBuddy_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveBuddy(pBuddy: win32more.System.RealTimeCommunications.IRTCBuddy_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateBuddies(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Buddies(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Data(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Data(bstrData: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head)) -> win32more.Foundation.HRESULT: ...
class IRTCBuddyGroupEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('3a79e1d1-b736-4414-96-f8-bb-c7-f0-88-63-e4')
    @commethod(7)
    def get_EventType(pEventType: POINTER(win32more.System.RealTimeCommunications.RTC_GROUP_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Group(ppGroup: POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Buddy(ppBuddy: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IRTCClient(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('07829e45-9a34-408e-a0-11-bd-df-13-48-7c-d1')
    @commethod(3)
    def Initialize() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareForShutdown() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_EventFilter(lFilter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_EventFilter(plFilter: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetPreferredMediaTypes(lMediaTypes: Int32, fPersistent: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_PreferredMediaTypes(plMediaTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MediaCapabilities(plMediaTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSession(enType: win32more.System.RealTimeCommunications.RTC_SESSION_TYPE, bstrLocalPhoneURI: win32more.Foundation.BSTR, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_ListenForIncomingSessions(enListen: win32more.System.RealTimeCommunications.RTC_LISTEN_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ListenForIncomingSessions(penListen: POINTER(win32more.System.RealTimeCommunications.RTC_LISTEN_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_NetworkAddresses(fTCP: win32more.Foundation.VARIANT_BOOL, fExternal: win32more.Foundation.VARIANT_BOOL, pvAddresses: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_Volume(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, lVolume: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Volume(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, plVolume: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_AudioMuted(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, fMuted: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_AudioMuted(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, pfMuted: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_IVideoWindow(enDevice: win32more.System.RealTimeCommunications.RTC_VIDEO_DEVICE, ppIVideoWindow: POINTER(win32more.Media.DirectShow.IVideoWindow_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_PreferredAudioDevice(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, bstrDeviceName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_PreferredAudioDevice(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, pbstrDeviceName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_PreferredVolume(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, lVolume: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_PreferredVolume(enDevice: win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE, plVolume: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_PreferredAEC(bEnable: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_PreferredAEC(pbEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_PreferredVideoDevice(bstrDeviceName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_PreferredVideoDevice(pbstrDeviceName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_ActiveMedia(plMediaType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_MaxBitrate(lMaxBitrate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_MaxBitrate(plMaxBitrate: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_TemporalSpatialTradeOff(lValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_TemporalSpatialTradeOff(plValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_NetworkQuality(plNetworkQuality: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def StartT120Applet(enApplet: win32more.System.RealTimeCommunications.RTC_T120_APPLET) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def StopT120Applets() -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_IsT120AppletRunning(enApplet: win32more.System.RealTimeCommunications.RTC_T120_APPLET, pfRunning: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_LocalUserURI(pbstrUserURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_LocalUserURI(bstrUserURI: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_LocalUserName(pbstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_LocalUserName(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def PlayRing(enType: win32more.System.RealTimeCommunications.RTC_RING_TYPE, bPlay: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SendDTMF(enDTMF: win32more.System.RealTimeCommunications.RTC_DTMF) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def InvokeTuningWizard(hwndParent: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def get_IsTuned(pfTuned: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IRTCClient2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCClient
    Guid = Guid('0c91d71d-1064-42da-bf-a5-57-2b-eb-8e-ea-84')
    @commethod(45)
    def put_AnswerMode(enType: win32more.System.RealTimeCommunications.RTC_SESSION_TYPE, enMode: win32more.System.RealTimeCommunications.RTC_ANSWER_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def get_AnswerMode(enType: win32more.System.RealTimeCommunications.RTC_SESSION_TYPE, penMode: POINTER(win32more.System.RealTimeCommunications.RTC_ANSWER_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def InvokeTuningWizardEx(hwndParent: IntPtr, fAllowAudio: win32more.Foundation.VARIANT_BOOL, fAllowVideo: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_Version(plVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def put_ClientName(bstrClientName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_ClientCurVer(bstrClientCurVer: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def InitializeEx(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def CreateSessionWithDescription(bstrContentType: win32more.Foundation.BSTR, bstrSessionDescription: win32more.Foundation.BSTR, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppSession2: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def SetSessionDescriptionManager(pSessionDescriptionManager: win32more.System.RealTimeCommunications.IRTCSessionDescriptionManager_head) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_PreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, enSecurityLevel: win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_PreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_AllowedPorts(lTransport: Int32, enListenMode: win32more.System.RealTimeCommunications.RTC_LISTEN_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def get_AllowedPorts(lTransport: Int32, penListenMode: POINTER(win32more.System.RealTimeCommunications.RTC_LISTEN_MODE)) -> win32more.Foundation.HRESULT: ...
class IRTCClientEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2b493b7a-3cba-4170-9c-8b-76-a9-da-cd-d6-44')
    @commethod(7)
    def get_EventType(penEventType: POINTER(win32more.System.RealTimeCommunications.RTC_CLIENT_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Client(ppClient: POINTER(win32more.System.RealTimeCommunications.IRTCClient_head)) -> win32more.Foundation.HRESULT: ...
class IRTCClientPortManagement(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5df3f03-4bde-4417-ae-fe-71-17-7b-da-ea-66')
    @commethod(3)
    def StartListenAddressAndPort(bstrInternalLocalAddress: win32more.Foundation.BSTR, lInternalLocalPort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StopListenAddressAndPort(bstrInternalLocalAddress: win32more.Foundation.BSTR, lInternalLocalPort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPortRange(enPortType: win32more.System.RealTimeCommunications.RTC_PORT_TYPE, plMinValue: POINTER(Int32), plMaxValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IRTCClientPresence(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('11c3cbcc-0744-42d1-96-8a-51-aa-1b-b2-74-c6')
    @commethod(3)
    def EnablePresence(fUseStorage: win32more.Foundation.VARIANT_BOOL, varStorage: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Export(varStorage: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Import(varStorage: win32more.System.Com.VARIANT, fReplaceAll: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateBuddies(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Buddies(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Buddy(bstrPresentityURI: win32more.Foundation.BSTR, ppBuddy: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddBuddy(bstrPresentityURI: win32more.Foundation.BSTR, bstrUserName: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR, fPersistent: win32more.Foundation.VARIANT_BOOL, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppBuddy: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveBuddy(pBuddy: win32more.System.RealTimeCommunications.IRTCBuddy_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumerateWatchers(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumWatchers_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Watchers(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Watcher(bstrPresentityURI: win32more.Foundation.BSTR, ppWatcher: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def AddWatcher(bstrPresentityURI: win32more.Foundation.BSTR, bstrUserName: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR, fBlocked: win32more.Foundation.VARIANT_BOOL, fPersistent: win32more.Foundation.VARIANT_BOOL, ppWatcher: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveWatcher(pWatcher: win32more.System.RealTimeCommunications.IRTCWatcher_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetLocalPresenceInfo(enStatus: win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS, bstrNotes: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_OfferWatcherMode(penMode: POINTER(win32more.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_OfferWatcherMode(enMode: win32more.System.RealTimeCommunications.RTC_OFFER_WATCHER_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_PrivacyMode(penMode: POINTER(win32more.System.RealTimeCommunications.RTC_PRIVACY_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_PrivacyMode(enMode: win32more.System.RealTimeCommunications.RTC_PRIVACY_MODE) -> win32more.Foundation.HRESULT: ...
class IRTCClientPresence2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCClientPresence
    Guid = Guid('ad1809e8-62f7-4783-90-9a-29-c9-d2-cb-1d-34')
    @commethod(21)
    def EnablePresenceEx(pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, varStorage: win32more.System.Com.VARIANT, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def DisablePresence() -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def AddGroup(bstrGroupName: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppGroup: POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveGroup(pGroup: win32more.System.RealTimeCommunications.IRTCBuddyGroup_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def EnumerateGroups(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Groups(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Group(bstrGroupName: win32more.Foundation.BSTR, ppGroup: POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def AddWatcherEx(bstrPresentityURI: win32more.Foundation.BSTR, bstrUserName: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR, enState: win32more.System.RealTimeCommunications.RTC_WATCHER_STATE, fPersistent: win32more.Foundation.VARIANT_BOOL, enScope: win32more.System.RealTimeCommunications.RTC_ACE_SCOPE, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppWatcher: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_WatcherEx(enMode: win32more.System.RealTimeCommunications.RTC_WATCHER_MATCH_MODE, bstrPresentityURI: win32more.Foundation.BSTR, ppWatcher: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_PresenceProperty(enProperty: win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, bstrProperty: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_PresenceProperty(enProperty: win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetPresenceData(bstrNamespace: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetPresenceData(pbstrNamespace: POINTER(win32more.Foundation.BSTR), pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetLocalPresenceInfo(penStatus: POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS), pbstrNotes: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def AddBuddyEx(bstrPresentityURI: win32more.Foundation.BSTR, bstrUserName: win32more.Foundation.BSTR, bstrData: win32more.Foundation.BSTR, fPersistent: win32more.Foundation.VARIANT_BOOL, enSubscriptionType: win32more.System.RealTimeCommunications.RTC_BUDDY_SUBSCRIPTION_TYPE, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32, ppBuddy: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy2_head)) -> win32more.Foundation.HRESULT: ...
class IRTCClientProvisioning(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b9f5cf06-65b9-4a80-a0-e6-73-ca-e3-ef-38-22')
    @commethod(3)
    def CreateProfile(bstrProfileXML: win32more.Foundation.BSTR, ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnableProfile(pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lRegisterFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DisableProfile(pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateProfiles(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumProfiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Profiles(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetProfile(bstrUserAccount: win32more.Foundation.BSTR, bstrUserPassword: win32more.Foundation.BSTR, bstrUserURI: win32more.Foundation.BSTR, bstrServer: win32more.Foundation.BSTR, lTransport: Int32, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_SessionCapabilities(plSupportedSessions: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IRTCClientProvisioning2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCClientProvisioning
    Guid = Guid('a70909b5-f40e-4587-bb-75-e6-bc-08-45-02-3e')
    @commethod(10)
    def EnableProfileEx(pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lRegisterFlags: Int32, lRoamingFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IRTCCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ec7c8096-b918-4044-94-f1-e4-fb-a0-36-1d-5c')
    @commethod(7)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(Index: Int32, pVariant: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppNewEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IRTCDispatchEventNotification(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('176ddfbe-fec0-4d55-bc-87-84-cf-f1-ef-7f-91')
class IRTCEnumBuddies(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f7296917-5569-4b3b-b3-af-98-d1-14-4b-2b-87')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCBuddy_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumBuddies_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumGroups(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('742378d6-a141-4415-8f-27-35-d9-90-76-cf-5d')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCBuddyGroup_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumGroups_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumParticipants(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fcd56f29-4a4f-41b2-ba-5c-f5-bc-cc-06-0b-f6')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumParticipants_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumPresenceDevices(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('708c2ab7-8bf8-42f8-8c-7d-63-51-97-ad-55-39')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCPresenceDevice_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumPresenceDevices_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumProfiles(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('29b7c41c-ed82-4bca-84-ad-39-d5-10-1b-58-e3')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumProfiles_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumUserSearchResults(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('83d4d877-aa5d-4a5b-8d-0e-00-2a-80-67-e0-e8')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchResult_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumUserSearchResults_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEnumWatchers(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a87d55d7-db74-4ed1-9c-a4-77-a0-e4-1b-41-3e')
    @commethod(3)
    def Next(celt: UInt32, ppElements: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumWatchers_head)) -> win32more.Foundation.HRESULT: ...
class IRTCEventNotification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('13fa24c7-5748-4b21-91-f5-73-97-60-9c-e7-47')
    @commethod(3)
    def Event(RTCEvent: win32more.System.RealTimeCommunications.RTC_EVENT, pEvent: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class IRTCInfoEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('4e1d68ae-1912-4f49-b2-c3-59-4f-ad-fd-42-5f')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Participant(ppParticipant: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Info(pbstrInfo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_InfoHeader(pbstrInfoHeader: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCIntensityEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('4c23bf51-390c-4992-a4-1d-41-ee-c0-5b-2a-4b')
    @commethod(7)
    def get_Level(plLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Min(plMin: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Max(plMax: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Direction(penDirection: POINTER(win32more.System.RealTimeCommunications.RTC_AUDIO_DEVICE)) -> win32more.Foundation.HRESULT: ...
class IRTCMediaEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('099944fb-bcda-453e-8c-41-e1-3d-a2-ad-f7-f3')
    @commethod(7)
    def get_MediaType(pMediaType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_EventType(penEventType: POINTER(win32more.System.RealTimeCommunications.RTC_MEDIA_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventReason(penEventReason: POINTER(win32more.System.RealTimeCommunications.RTC_MEDIA_EVENT_REASON)) -> win32more.Foundation.HRESULT: ...
class IRTCMediaRequestEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('52572d15-148c-4d97-a3-6c-2d-a5-5c-28-9d-63')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProposedMedia(plMediaTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentMedia(plMediaTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Accept(lMediaTypes: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_RemotePreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Reject() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_State(pState: POINTER(win32more.System.RealTimeCommunications.RTC_REINVITE_STATE)) -> win32more.Foundation.HRESULT: ...
class IRTCMessagingEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d3609541-1b29-4de5-a4-ad-5a-eb-af-31-95-12')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Participant(ppParticipant: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventType(penEventType: POINTER(win32more.System.RealTimeCommunications.RTC_MESSAGING_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Message(pbstrMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_MessageHeader(pbstrMessageHeader: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_UserStatus(penUserStatus: POINTER(win32more.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS)) -> win32more.Foundation.HRESULT: ...
class IRTCParticipant(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ae86add5-26b1-4414-af-1d-b9-4c-d9-38-d7-39')
    @commethod(3)
    def get_UserURI(pbstrUserURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Name(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Removable(pfRemovable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_PARTICIPANT_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession_head)) -> win32more.Foundation.HRESULT: ...
class IRTCParticipantStateChangeEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('09bcb597-f0fa-48f9-b4-20-46-8c-ea-7f-de-04')
    @commethod(7)
    def get_Participant(ppParticipant: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_PARTICIPANT_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IRTCPortManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('da77c14b-6208-43ca-8d-df-5b-60-a0-a6-9f-ac')
    @commethod(3)
    def GetMapping(bstrRemoteAddress: win32more.Foundation.BSTR, enPortType: win32more.System.RealTimeCommunications.RTC_PORT_TYPE, pbstrInternalLocalAddress: POINTER(win32more.Foundation.BSTR), plInternalLocalPort: POINTER(Int32), pbstrExternalLocalAddress: POINTER(win32more.Foundation.BSTR), plExternalLocalPort: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateRemoteAddress(bstrRemoteAddress: win32more.Foundation.BSTR, bstrInternalLocalAddress: win32more.Foundation.BSTR, lInternalLocalPort: Int32, bstrExternalLocalAddress: win32more.Foundation.BSTR, lExternalLocalPort: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReleaseMapping(bstrInternalLocalAddress: win32more.Foundation.BSTR, lInternalLocalPort: Int32, bstrExternalLocalAddress: win32more.Foundation.BSTR, lExternalLocalAddress: Int32) -> win32more.Foundation.HRESULT: ...
class IRTCPresenceContact(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8b22f92c-cd90-42db-a7-33-21-22-05-c3-e3-df')
    @commethod(3)
    def get_PresentityURI(pbstrPresentityURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_PresentityURI(bstrPresentityURI: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Name(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_Name(bstrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Data(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Data(bstrData: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Persistent(pfPersistent: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Persistent(fPersistent: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IRTCPresenceDataEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('38f0e78c-8b87-4c04-a8-2d-ae-dd-83-c9-09-bb')
    @commethod(7)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPresenceData(pbstrNamespace: POINTER(win32more.Foundation.BSTR), pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCPresenceDevice(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bc6a90dd-ad9a-48da-9b-0c-25-15-e3-85-21-ad')
    @commethod(3)
    def get_Status(penStatus: POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Notes(pbstrNotes: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_PresenceProperty(enProperty: win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY, pbstrProperty: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPresenceData(pbstrNamespace: POINTER(win32more.Foundation.BSTR), pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCPresencePropertyEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f777f570-a820-49d5-86-bd-e0-99-49-3f-15-18')
    @commethod(7)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_PresenceProperty(penPresProp: POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_PROPERTY)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Value(pbstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCPresenceStatusEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('78673f32-4a0f-462c-89-aa-ee-77-06-70-76-78')
    @commethod(7)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocalPresenceInfo(penStatus: POINTER(win32more.System.RealTimeCommunications.RTC_PRESENCE_STATUS), pbstrNotes: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCProfile(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d07eca9e-4062-4dd4-9e-7d-72-2a-49-ba-73-03')
    @commethod(3)
    def get_Key(pbstrKey: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Name(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_XML(pbstrXML: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_ProviderName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_ProviderURI(enURI: win32more.System.RealTimeCommunications.RTC_PROVIDER_URI, pbstrURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProviderData(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ClientName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ClientBanner(pfBanner: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ClientMinVer(pbstrMinVer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClientCurVer(pbstrCurVer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClientUpdateURI(pbstrUpdateURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ClientData(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserURI(pbstrUserURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserName(pbstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_UserAccount(pbstrUserAccount: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetCredentials(bstrUserURI: win32more.Foundation.BSTR, bstrUserAccount: win32more.Foundation.BSTR, bstrPassword: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_SessionCapabilities(plSupportedSessions: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_REGISTRATION_STATE)) -> win32more.Foundation.HRESULT: ...
class IRTCProfile2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCProfile
    Guid = Guid('4b81f84e-bdc7-4184-91-54-3c-b2-dd-79-17-fb')
    @commethod(21)
    def get_Realm(pbstrRealm: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Realm(bstrRealm: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_AllowedAuth(plAllowedAuth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_AllowedAuth(lAllowedAuth: Int32) -> win32more.Foundation.HRESULT: ...
class IRTCProfileEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d6d5ab3b-770e-43e8-80-0a-79-b0-62-39-5f-ca')
    @commethod(7)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Cookie(plCookie: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IRTCProfileEvent2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCProfileEvent
    Guid = Guid('62e56edc-03fa-4121-94-fb-23-49-3f-d0-ae-64')
    @commethod(10)
    def get_EventType(pEventType: POINTER(win32more.System.RealTimeCommunications.RTC_PROFILE_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
class IRTCReInviteEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('11558d84-204c-43e7-99-b0-20-34-e9-41-7f-7d')
    @commethod(7)
    def get_Session(ppSession2: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Accept(bstrContentType: win32more.Foundation.BSTR, bstrSessionDescription: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Reject() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(pState: POINTER(win32more.System.RealTimeCommunications.RTC_REINVITE_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRemoteSessionDescription(pbstrContentType: POINTER(win32more.Foundation.BSTR), pbstrSessionDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCRegistrationStateChangeEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('62d0991b-50ab-4f02-b9-48-ca-94-f2-6f-8f-95')
    @commethod(7)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_REGISTRATION_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCRoamingEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('79960a6b-0cb1-4dc8-a8-05-73-18-e9-99-02-e8')
    @commethod(7)
    def get_EventType(pEventType: POINTER(win32more.System.RealTimeCommunications.RTC_ROAMING_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('387c8086-99be-42fb-99-73-7c-0f-c0-ca-9f-a8')
    @commethod(3)
    def get_Client(ppClient: POINTER(win32more.System.RealTimeCommunications.IRTCClient_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(penType: POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Participants(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Answer() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Terminate(enReason: win32more.System.RealTimeCommunications.RTC_TERMINATE_REASON) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Redirect(enType: win32more.System.RealTimeCommunications.RTC_SESSION_TYPE, bstrLocalPhoneURI: win32more.Foundation.BSTR, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AddParticipant(bstrAddress: win32more.Foundation.BSTR, bstrName: win32more.Foundation.BSTR, ppParticipant: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveParticipant(pParticipant: win32more.System.RealTimeCommunications.IRTCParticipant_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def EnumerateParticipants(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumParticipants_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_CanAddParticipants(pfCanAdd: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_RedirectedUserURI(pbstrUserURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_RedirectedUserName(pbstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def NextRedirectedUser() -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SendMessage(bstrMessageHeader: win32more.Foundation.BSTR, bstrMessage: win32more.Foundation.BSTR, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SendMessageStatus(enUserStatus: win32more.System.RealTimeCommunications.RTC_MESSAGING_USER_STATUS, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def AddStream(lMediaType: Int32, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def RemoveStream(lMediaType: Int32, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_EncryptionKey(lMediaType: Int32, EncryptionKey: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IRTCSession2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCSession
    Guid = Guid('17d7cdfc-b007-484c-99-d2-86-a8-a8-20-99-1d')
    @commethod(23)
    def SendInfo(bstrInfoHeader: win32more.Foundation.BSTR, bstrInfo: win32more.Foundation.BSTR, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_PreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, enSecurityLevel: win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_PreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def IsSecurityEnabled(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, pfSecurityEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def AnswerWithSessionDescription(bstrContentType: win32more.Foundation.BSTR, bstrSessionDescription: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def ReInviteWithSessionDescription(bstrContentType: win32more.Foundation.BSTR, bstrSessionDescription: win32more.Foundation.BSTR, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
class IRTCSessionCallControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e9a50d94-190b-4f82-95-30-3b-8e-bf-60-75-8a')
    @commethod(3)
    def Hold(lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnHold(lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Forward(bstrForwardToURI: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Refer(bstrReferToURI: win32more.Foundation.BSTR, bstrReferCookie: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_ReferredByURI(bstrReferredByURI: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferredByURI(pbstrReferredByURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_ReferCookie(bstrReferCookie: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReferCookie(pbstrReferCookie: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsReferred(pfIsReferred: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionDescriptionManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ba7f518e-d336-4070-93-a6-86-53-95-c8-43-f9')
    @commethod(3)
    def EvaluateSessionDescription(bstrContentType: win32more.Foundation.BSTR, bstrSessionDescription: win32more.Foundation.BSTR, pfApplicationSession: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionOperationCompleteEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('a6bff4c0-f7c8-4d3c-9a-41-35-50-f7-8a-95-b0')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Cookie(plCookie: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionOperationCompleteEvent2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCSessionOperationCompleteEvent
    Guid = Guid('f6fc2a9b-d5bc-4241-b4-36-1b-84-60-c1-38-32')
    @commethod(11)
    def get_Participant(ppParticipant: POINTER(win32more.System.RealTimeCommunications.IRTCParticipant_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetRemoteSessionDescription(pbstrContentType: POINTER(win32more.Foundation.BSTR), pbstrSessionDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionPortManagement(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a072f1d6-0286-4e1f-85-f2-17-a2-94-84-56-ec')
    @commethod(3)
    def SetPortManager(pPortManager: win32more.System.RealTimeCommunications.IRTCPortManager_head) -> win32more.Foundation.HRESULT: ...
class IRTCSessionReferStatusEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('3d8fc2cd-5d76-44ab-bb-68-2a-80-35-3b-34-a2')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferStatus(penReferStatus: POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_REFER_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionReferredEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('176a6828-4fcc-4f28-a8-62-04-59-7a-6c-f1-c4')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ReferredByURI(pbstrReferredByURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ReferToURI(pbstrReferoURI: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReferCookie(pbstrReferCookie: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Accept() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Reject() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetReferredSessionState(enState: win32more.System.RealTimeCommunications.RTC_SESSION_STATE) -> win32more.Foundation.HRESULT: ...
class IRTCSessionStateChangeEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b5bad703-5952-48b3-93-21-7f-45-00-52-15-06')
    @commethod(7)
    def get_Session(ppSession: POINTER(win32more.System.RealTimeCommunications.IRTCSession_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_SESSION_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_StatusText(pbstrStatusText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCSessionStateChangeEvent2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCSessionStateChangeEvent
    Guid = Guid('4f933171-6f95-4880-80-d9-2e-c8-d4-95-d2-61')
    @commethod(11)
    def get_MediaTypes(pMediaTypes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_RemotePreferredSecurityLevel(enSecurityType: win32more.System.RealTimeCommunications.RTC_SECURITY_TYPE, penSecurityLevel: POINTER(win32more.System.RealTimeCommunications.RTC_SECURITY_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_IsForked(pfIsForked: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRemoteSessionDescription(pbstrContentType: POINTER(win32more.Foundation.BSTR), pbstrSessionDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCUserSearch(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b619882b-860c-4db4-be-1b-69-3b-65-05-bb-e5')
    @commethod(3)
    def CreateQuery(ppQuery: POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ExecuteSearch(pQuery: win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head, pProfile: win32more.System.RealTimeCommunications.IRTCProfile_head, lCookie: IntPtr) -> win32more.Foundation.HRESULT: ...
class IRTCUserSearchQuery(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('288300f5-d23a-4365-9a-73-99-85-c9-8c-28-81')
    @commethod(3)
    def put_SearchTerm(bstrName: win32more.Foundation.BSTR, bstrValue: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_SearchTerm(bstrName: win32more.Foundation.BSTR, pbstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_SearchTerms(pbstrNames: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_SearchPreference(enPreference: win32more.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE, lValue: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_SearchPreference(enPreference: win32more.System.RealTimeCommunications.RTC_USER_SEARCH_PREFERENCE, plValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_SearchDomain(bstrDomain: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_SearchDomain(pbstrDomain: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCUserSearchResult(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('851278b2-9592-480f-8d-b5-2d-e8-6b-26-b5-4d')
    @commethod(3)
    def get_Value(enColumn: win32more.System.RealTimeCommunications.RTC_USER_SEARCH_COLUMN, pbstrValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRTCUserSearchResultsEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d8c8c3cd-7fac-4088-81-c5-c2-4c-bc-09-38-e3')
    @commethod(7)
    def EnumerateResults(ppEnum: POINTER(win32more.System.RealTimeCommunications.IRTCEnumUserSearchResults_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Results(ppCollection: POINTER(win32more.System.RealTimeCommunications.IRTCCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Query(ppQuery: POINTER(win32more.System.RealTimeCommunications.IRTCUserSearchQuery_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Cookie(plCookie: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_MoreAvailable(pfMoreAvailable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IRTCWatcher(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCPresenceContact
    Guid = Guid('c7cedad8-346b-4d1b-ac-02-a2-08-8d-f9-be-4f')
    @commethod(11)
    def get_State(penState: POINTER(win32more.System.RealTimeCommunications.RTC_WATCHER_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_State(enState: win32more.System.RealTimeCommunications.RTC_WATCHER_STATE) -> win32more.Foundation.HRESULT: ...
class IRTCWatcher2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCWatcher
    Guid = Guid('d4d9967f-d011-4b1d-91-e3-ab-a7-8f-96-39-3d')
    @commethod(13)
    def get_Profile(ppProfile: POINTER(win32more.System.RealTimeCommunications.IRTCProfile2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_Scope(penScope: POINTER(win32more.System.RealTimeCommunications.RTC_ACE_SCOPE)) -> win32more.Foundation.HRESULT: ...
class IRTCWatcherEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f30d7261-587a-424f-82-2c-31-27-88-f4-35-48')
    @commethod(7)
    def get_Watcher(ppWatcher: POINTER(win32more.System.RealTimeCommunications.IRTCWatcher_head)) -> win32more.Foundation.HRESULT: ...
class IRTCWatcherEvent2(c_void_p):
    extends: win32more.System.RealTimeCommunications.IRTCWatcherEvent
    Guid = Guid('e52891e8-188c-49af-b0-05-98-ed-13-f8-3f-9c')
    @commethod(8)
    def get_EventType(pEventType: POINTER(win32more.System.RealTimeCommunications.RTC_WATCHER_EVENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_StatusCode(plStatusCode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ITransportSettingsInternal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5123e076-29e3-4bfd-84-fe-01-92-d4-11-e3-e8')
    @commethod(3)
    def ApplySetting(Setting: POINTER(win32more.System.RealTimeCommunications.TRANSPORT_SETTING_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySetting(Setting: POINTER(win32more.System.RealTimeCommunications.TRANSPORT_SETTING_head)) -> win32more.Foundation.HRESULT: ...
RTCClient = Guid('7a42ea29-a2b7-40c4-b0-91-f6-f0-24-aa-89-be')
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
class TRANSPORT_SETTING(Structure):
    SettingId: win32more.Networking.WinSock.TRANSPORT_SETTING_ID
    Length: POINTER(UInt32)
    Value: c_char_p_no
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
__all__ = [
    "FACILITY_PINT_STATUS_CODE",
    "FACILITY_RTC_INTERFACE",
    "FACILITY_SIP_STATUS_CODE",
    "INetworkTransportSettings",
    "INotificationTransportSync",
    "IRTCBuddy",
    "IRTCBuddy2",
    "IRTCBuddyEvent",
    "IRTCBuddyEvent2",
    "IRTCBuddyGroup",
    "IRTCBuddyGroupEvent",
    "IRTCClient",
    "IRTCClient2",
    "IRTCClientEvent",
    "IRTCClientPortManagement",
    "IRTCClientPresence",
    "IRTCClientPresence2",
    "IRTCClientProvisioning",
    "IRTCClientProvisioning2",
    "IRTCCollection",
    "IRTCDispatchEventNotification",
    "IRTCEnumBuddies",
    "IRTCEnumGroups",
    "IRTCEnumParticipants",
    "IRTCEnumPresenceDevices",
    "IRTCEnumProfiles",
    "IRTCEnumUserSearchResults",
    "IRTCEnumWatchers",
    "IRTCEventNotification",
    "IRTCInfoEvent",
    "IRTCIntensityEvent",
    "IRTCMediaEvent",
    "IRTCMediaRequestEvent",
    "IRTCMessagingEvent",
    "IRTCParticipant",
    "IRTCParticipantStateChangeEvent",
    "IRTCPortManager",
    "IRTCPresenceContact",
    "IRTCPresenceDataEvent",
    "IRTCPresenceDevice",
    "IRTCPresencePropertyEvent",
    "IRTCPresenceStatusEvent",
    "IRTCProfile",
    "IRTCProfile2",
    "IRTCProfileEvent",
    "IRTCProfileEvent2",
    "IRTCReInviteEvent",
    "IRTCRegistrationStateChangeEvent",
    "IRTCRoamingEvent",
    "IRTCSession",
    "IRTCSession2",
    "IRTCSessionCallControl",
    "IRTCSessionDescriptionManager",
    "IRTCSessionOperationCompleteEvent",
    "IRTCSessionOperationCompleteEvent2",
    "IRTCSessionPortManagement",
    "IRTCSessionReferStatusEvent",
    "IRTCSessionReferredEvent",
    "IRTCSessionStateChangeEvent",
    "IRTCSessionStateChangeEvent2",
    "IRTCUserSearch",
    "IRTCUserSearchQuery",
    "IRTCUserSearchResult",
    "IRTCUserSearchResultsEvent",
    "IRTCWatcher",
    "IRTCWatcher2",
    "IRTCWatcherEvent",
    "IRTCWatcherEvent2",
    "ITransportSettingsInternal",
    "RTCAD_MICROPHONE",
    "RTCAD_SPEAKER",
    "RTCAM_AUTOMATICALLY_ACCEPT",
    "RTCAM_AUTOMATICALLY_REJECT",
    "RTCAM_NOT_SUPPORTED",
    "RTCAM_OFFER_SESSION_EVENT",
    "RTCAS_SCOPE_ALL",
    "RTCAS_SCOPE_DOMAIN",
    "RTCAS_SCOPE_USER",
    "RTCAU_BASIC",
    "RTCAU_DIGEST",
    "RTCAU_KERBEROS",
    "RTCAU_NTLM",
    "RTCAU_USE_LOGON_CRED",
    "RTCBET_BUDDY_ADD",
    "RTCBET_BUDDY_REMOVE",
    "RTCBET_BUDDY_ROAMED",
    "RTCBET_BUDDY_STATE_CHANGE",
    "RTCBET_BUDDY_SUBSCRIBED",
    "RTCBET_BUDDY_UPDATE",
    "RTCBT_ALWAYS_OFFLINE",
    "RTCBT_ALWAYS_ONLINE",
    "RTCBT_POLL",
    "RTCBT_SUBSCRIBED",
    "RTCCET_ASYNC_CLEANUP_DONE",
    "RTCCET_DEVICE_CHANGE",
    "RTCCET_NETWORK_QUALITY_CHANGE",
    "RTCCET_VOLUME_CHANGE",
    "RTCCS_FAIL_ON_REDIRECT",
    "RTCCS_FORCE_PROFILE",
    "RTCClient",
    "RTCEF_ALL",
    "RTCEF_BUDDY",
    "RTCEF_BUDDY2",
    "RTCEF_CLIENT",
    "RTCEF_GROUP",
    "RTCEF_INFO",
    "RTCEF_INTENSITY",
    "RTCEF_MEDIA",
    "RTCEF_MEDIA_REQUEST",
    "RTCEF_MESSAGING",
    "RTCEF_PARTICIPANT_STATE_CHANGE",
    "RTCEF_PRESENCE_DATA",
    "RTCEF_PRESENCE_PROPERTY",
    "RTCEF_PRESENCE_STATUS",
    "RTCEF_PROFILE",
    "RTCEF_REGISTRATION_STATE_CHANGE",
    "RTCEF_REINVITE",
    "RTCEF_ROAMING",
    "RTCEF_SESSION_OPERATION_COMPLETE",
    "RTCEF_SESSION_REFERRED",
    "RTCEF_SESSION_REFER_STATUS",
    "RTCEF_SESSION_STATE_CHANGE",
    "RTCEF_USERSEARCH",
    "RTCEF_WATCHER",
    "RTCEF_WATCHER2",
    "RTCE_BUDDY",
    "RTCE_CLIENT",
    "RTCE_GROUP",
    "RTCE_INFO",
    "RTCE_INTENSITY",
    "RTCE_MEDIA",
    "RTCE_MEDIA_REQUEST",
    "RTCE_MESSAGING",
    "RTCE_PARTICIPANT_STATE_CHANGE",
    "RTCE_PRESENCE_DATA",
    "RTCE_PRESENCE_PROPERTY",
    "RTCE_PRESENCE_STATUS",
    "RTCE_PROFILE",
    "RTCE_REGISTRATION_STATE_CHANGE",
    "RTCE_REINVITE",
    "RTCE_ROAMING",
    "RTCE_SESSION_OPERATION_COMPLETE",
    "RTCE_SESSION_REFERRED",
    "RTCE_SESSION_REFER_STATUS",
    "RTCE_SESSION_STATE_CHANGE",
    "RTCE_USERSEARCH",
    "RTCE_WATCHER",
    "RTCGET_GROUP_ADD",
    "RTCGET_GROUP_BUDDY_ADD",
    "RTCGET_GROUP_BUDDY_REMOVE",
    "RTCGET_GROUP_REMOVE",
    "RTCGET_GROUP_ROAMED",
    "RTCGET_GROUP_UPDATE",
    "RTCIF_DISABLE_MEDIA",
    "RTCIF_DISABLE_STRICT_DNS",
    "RTCIF_DISABLE_UPNP",
    "RTCIF_ENABLE_SERVER_CLASS",
    "RTCLM_BOTH",
    "RTCLM_DYNAMIC",
    "RTCLM_NONE",
    "RTCMER_BAD_DEVICE",
    "RTCMER_HOLD",
    "RTCMER_NORMAL",
    "RTCMER_NO_PORT",
    "RTCMER_PORT_MAPPING_FAILED",
    "RTCMER_REMOTE_REQUEST",
    "RTCMER_TIMEOUT",
    "RTCMET_FAILED",
    "RTCMET_STARTED",
    "RTCMET_STOPPED",
    "RTCMSET_MESSAGE",
    "RTCMSET_STATUS",
    "RTCMT_AUDIO_RECEIVE",
    "RTCMT_AUDIO_SEND",
    "RTCMT_T120_SENDRECV",
    "RTCMT_VIDEO_RECEIVE",
    "RTCMT_VIDEO_SEND",
    "RTCMUS_IDLE",
    "RTCMUS_TYPING",
    "RTCOWM_AUTOMATICALLY_ADD_WATCHER",
    "RTCOWM_OFFER_WATCHER_EVENT",
    "RTCPFET_PROFILE_GET",
    "RTCPFET_PROFILE_UPDATE",
    "RTCPM_ALLOW_LIST_ONLY",
    "RTCPM_BLOCK_LIST_EXCLUDED",
    "RTCPP_DEVICE_NAME",
    "RTCPP_DISPLAYNAME",
    "RTCPP_EMAIL",
    "RTCPP_MULTIPLE",
    "RTCPP_PHONENUMBER",
    "RTCPS_ALERTING",
    "RTCPS_ANSWERING",
    "RTCPS_CONNECTED",
    "RTCPS_DISCONNECTED",
    "RTCPS_DISCONNECTING",
    "RTCPS_IDLE",
    "RTCPS_INCOMING",
    "RTCPS_INPROGRESS",
    "RTCPS_PENDING",
    "RTCPT_AUDIO_RTCP",
    "RTCPT_AUDIO_RTP",
    "RTCPT_SIP",
    "RTCPT_VIDEO_RTCP",
    "RTCPT_VIDEO_RTP",
    "RTCPU_URIDISPLAYDURINGCALL",
    "RTCPU_URIDISPLAYDURINGIDLE",
    "RTCPU_URIHELPDESK",
    "RTCPU_URIHOMEPAGE",
    "RTCPU_URIPERSONALACCOUNT",
    "RTCRET_BUDDY_ROAMING",
    "RTCRET_PRESENCE_ROAMING",
    "RTCRET_PROFILE_ROAMING",
    "RTCRET_WATCHER_ROAMING",
    "RTCRET_WPENDING_ROAMING",
    "RTCRF_REGISTER_ALL",
    "RTCRF_REGISTER_INVITE_SESSIONS",
    "RTCRF_REGISTER_MESSAGE_SESSIONS",
    "RTCRF_REGISTER_NOTIFY",
    "RTCRF_REGISTER_PRESENCE",
    "RTCRIN_FAIL",
    "RTCRIN_INCOMING",
    "RTCRIN_SUCCEEDED",
    "RTCRMF_ALL_ROAMING",
    "RTCRMF_BUDDY_ROAMING",
    "RTCRMF_PRESENCE_ROAMING",
    "RTCRMF_PROFILE_ROAMING",
    "RTCRMF_WATCHER_ROAMING",
    "RTCRS_ERROR",
    "RTCRS_LOCAL_PA_LOGGED_OFF",
    "RTCRS_LOGGED_OFF",
    "RTCRS_NOT_REGISTERED",
    "RTCRS_REGISTERED",
    "RTCRS_REGISTERING",
    "RTCRS_REJECTED",
    "RTCRS_REMOTE_PA_LOGGED_OFF",
    "RTCRS_UNREGISTERING",
    "RTCRT_MESSAGE",
    "RTCRT_PHONE",
    "RTCRT_RINGBACK",
    "RTCSECL_REQUIRED",
    "RTCSECL_SUPPORTED",
    "RTCSECL_UNSUPPORTED",
    "RTCSECT_AUDIO_VIDEO_MEDIA_ENCRYPTION",
    "RTCSECT_T120_MEDIA_ENCRYPTION",
    "RTCSI_APPLICATION",
    "RTCSI_IM",
    "RTCSI_MULTIPARTY_IM",
    "RTCSI_PC_TO_PC",
    "RTCSI_PC_TO_PHONE",
    "RTCSI_PHONE_TO_PHONE",
    "RTCSRS_ACCEPTED",
    "RTCSRS_DONE",
    "RTCSRS_DROPPED",
    "RTCSRS_ERROR",
    "RTCSRS_REFERRING",
    "RTCSRS_REJECTED",
    "RTCSS_ANSWERING",
    "RTCSS_CONNECTED",
    "RTCSS_DISCONNECTED",
    "RTCSS_HOLD",
    "RTCSS_IDLE",
    "RTCSS_INCOMING",
    "RTCSS_INPROGRESS",
    "RTCSS_REFER",
    "RTCST_APPLICATION",
    "RTCST_IM",
    "RTCST_MULTIPARTY_IM",
    "RTCST_PC_TO_PC",
    "RTCST_PC_TO_PHONE",
    "RTCST_PHONE_TO_PHONE",
    "RTCTA_APPSHARING",
    "RTCTA_WHITEBOARD",
    "RTCTR_BUSY",
    "RTCTR_DND",
    "RTCTR_INSUFFICIENT_SECURITY_LEVEL",
    "RTCTR_NORMAL",
    "RTCTR_NOT_SUPPORTED",
    "RTCTR_REJECT",
    "RTCTR_SHUTDOWN",
    "RTCTR_TCP",
    "RTCTR_TIMEOUT",
    "RTCTR_TLS",
    "RTCTR_UDP",
    "RTCUSC_CITY",
    "RTCUSC_COMPANY",
    "RTCUSC_COUNTRY",
    "RTCUSC_DISPLAYNAME",
    "RTCUSC_EMAIL",
    "RTCUSC_OFFICE",
    "RTCUSC_PHONE",
    "RTCUSC_STATE",
    "RTCUSC_TITLE",
    "RTCUSC_URI",
    "RTCUSP_MAX_MATCHES",
    "RTCUSP_TIME_LIMIT",
    "RTCVD_PREVIEW",
    "RTCVD_RECEIVE",
    "RTCWET_WATCHER_ADD",
    "RTCWET_WATCHER_OFFERING",
    "RTCWET_WATCHER_REMOVE",
    "RTCWET_WATCHER_ROAMED",
    "RTCWET_WATCHER_UPDATE",
    "RTCWMM_BEST_ACE_MATCH",
    "RTCWMM_EXACT_MATCH",
    "RTCWS_ALLOWED",
    "RTCWS_BLOCKED",
    "RTCWS_DENIED",
    "RTCWS_OFFERING",
    "RTCWS_PROMPT",
    "RTCWS_UNKNOWN",
    "RTCXS_PRESENCE_AWAY",
    "RTCXS_PRESENCE_BE_RIGHT_BACK",
    "RTCXS_PRESENCE_BUSY",
    "RTCXS_PRESENCE_IDLE",
    "RTCXS_PRESENCE_OFFLINE",
    "RTCXS_PRESENCE_ONLINE",
    "RTCXS_PRESENCE_ON_THE_PHONE",
    "RTCXS_PRESENCE_OUT_TO_LUNCH",
    "RTC_ACE_SCOPE",
    "RTC_ANSWER_MODE",
    "RTC_AUDIO_DEVICE",
    "RTC_BUDDY_EVENT_TYPE",
    "RTC_BUDDY_SUBSCRIPTION_TYPE",
    "RTC_CLIENT_EVENT_TYPE",
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
    "RTC_DTMF_A",
    "RTC_DTMF_B",
    "RTC_DTMF_C",
    "RTC_DTMF_D",
    "RTC_DTMF_FLASH",
    "RTC_DTMF_POUND",
    "RTC_DTMF_STAR",
    "RTC_EVENT",
    "RTC_E_ANOTHER_MEDIA_SESSION_ACTIVE",
    "RTC_E_BASIC_AUTH_SET_TLS",
    "RTC_E_CLIENT_ALREADY_INITIALIZED",
    "RTC_E_CLIENT_ALREADY_SHUT_DOWN",
    "RTC_E_CLIENT_NOT_INITIALIZED",
    "RTC_E_DESTINATION_ADDRESS_LOCAL",
    "RTC_E_DESTINATION_ADDRESS_MULTICAST",
    "RTC_E_DUPLICATE_BUDDY",
    "RTC_E_DUPLICATE_GROUP",
    "RTC_E_DUPLICATE_REALM",
    "RTC_E_DUPLICATE_WATCHER",
    "RTC_E_INVALID_ACL_LIST",
    "RTC_E_INVALID_ADDRESS_LOCAL",
    "RTC_E_INVALID_BUDDY_LIST",
    "RTC_E_INVALID_LISTEN_SOCKET",
    "RTC_E_INVALID_OBJECT_STATE",
    "RTC_E_INVALID_PORTRANGE",
    "RTC_E_INVALID_PREFERENCE_LIST",
    "RTC_E_INVALID_PROFILE",
    "RTC_E_INVALID_PROXY_ADDRESS",
    "RTC_E_INVALID_REGISTRATION_STATE",
    "RTC_E_INVALID_SESSION_STATE",
    "RTC_E_INVALID_SESSION_TYPE",
    "RTC_E_INVALID_SIP_URL",
    "RTC_E_LISTENING_SOCKET_NOT_EXIST",
    "RTC_E_LOCAL_PHONE_NEEDED",
    "RTC_E_MALFORMED_XML",
    "RTC_E_MAX_PENDING_OPERATIONS",
    "RTC_E_MAX_REDIRECTS",
    "RTC_E_MEDIA_AEC",
    "RTC_E_MEDIA_AUDIO_DEVICE_NOT_AVAILABLE",
    "RTC_E_MEDIA_CONTROLLER_STATE",
    "RTC_E_MEDIA_DISABLED",
    "RTC_E_MEDIA_ENABLED",
    "RTC_E_MEDIA_NEED_TERMINAL",
    "RTC_E_MEDIA_SESSION_IN_HOLD",
    "RTC_E_MEDIA_SESSION_NOT_EXIST",
    "RTC_E_MEDIA_VIDEO_DEVICE_NOT_AVAILABLE",
    "RTC_E_NOT_ALLOWED",
    "RTC_E_NOT_EXIST",
    "RTC_E_NOT_PRESENCE_PROFILE",
    "RTC_E_NO_BUDDY",
    "RTC_E_NO_DEVICE",
    "RTC_E_NO_GROUP",
    "RTC_E_NO_PROFILE",
    "RTC_E_NO_REALM",
    "RTC_E_NO_TRANSPORT",
    "RTC_E_NO_WATCHER",
    "RTC_E_OPERATION_WITH_TOO_MANY_PARTICIPANTS",
    "RTC_E_PINT_STATUS_REJECTED_ALL_BUSY",
    "RTC_E_PINT_STATUS_REJECTED_BADNUMBER",
    "RTC_E_PINT_STATUS_REJECTED_BUSY",
    "RTC_E_PINT_STATUS_REJECTED_CANCELLED",
    "RTC_E_PINT_STATUS_REJECTED_NO_ANSWER",
    "RTC_E_PINT_STATUS_REJECTED_PL_FAILED",
    "RTC_E_PINT_STATUS_REJECTED_SW_FAILED",
    "RTC_E_PLATFORM_NOT_SUPPORTED",
    "RTC_E_POLICY_NOT_ALLOW",
    "RTC_E_PORT_MANAGER_ALREADY_SET",
    "RTC_E_PORT_MAPPING_FAILED",
    "RTC_E_PORT_MAPPING_UNAVAILABLE",
    "RTC_E_PRESENCE_ENABLED",
    "RTC_E_PRESENCE_NOT_ENABLED",
    "RTC_E_PROFILE_INVALID_SERVER_AUTHMETHOD",
    "RTC_E_PROFILE_INVALID_SERVER_PROTOCOL",
    "RTC_E_PROFILE_INVALID_SERVER_ROLE",
    "RTC_E_PROFILE_INVALID_SESSION",
    "RTC_E_PROFILE_INVALID_SESSION_PARTY",
    "RTC_E_PROFILE_INVALID_SESSION_TYPE",
    "RTC_E_PROFILE_MULTIPLE_REGISTRARS",
    "RTC_E_PROFILE_NO_KEY",
    "RTC_E_PROFILE_NO_NAME",
    "RTC_E_PROFILE_NO_PROVISION",
    "RTC_E_PROFILE_NO_SERVER",
    "RTC_E_PROFILE_NO_SERVER_ADDRESS",
    "RTC_E_PROFILE_NO_SERVER_PROTOCOL",
    "RTC_E_PROFILE_NO_USER",
    "RTC_E_PROFILE_NO_USER_URI",
    "RTC_E_PROFILE_SERVER_UNAUTHORIZED",
    "RTC_E_REDIRECT_PROCESSING_FAILED",
    "RTC_E_REFER_NOT_ACCEPTED",
    "RTC_E_REFER_NOT_ALLOWED",
    "RTC_E_REFER_NOT_EXIST",
    "RTC_E_REGISTRATION_DEACTIVATED",
    "RTC_E_REGISTRATION_REJECTED",
    "RTC_E_REGISTRATION_UNREGISTERED",
    "RTC_E_ROAMING_ENABLED",
    "RTC_E_ROAMING_FAILED",
    "RTC_E_ROAMING_OPERATION_INTERRUPTED",
    "RTC_E_SDP_CONNECTION_ADDR",
    "RTC_E_SDP_FAILED_TO_BUILD",
    "RTC_E_SDP_MULTICAST",
    "RTC_E_SDP_NOT_PRESENT",
    "RTC_E_SDP_NO_MEDIA",
    "RTC_E_SDP_PARSE_FAILED",
    "RTC_E_SDP_UPDATE_FAILED",
    "RTC_E_SECURITY_LEVEL_ALREADY_SET",
    "RTC_E_SECURITY_LEVEL_NOT_COMPATIBLE",
    "RTC_E_SECURITY_LEVEL_NOT_DEFINED",
    "RTC_E_SECURITY_LEVEL_NOT_SUPPORTED_BY_PARTICIPANT",
    "RTC_E_SIP_ADDITIONAL_PARTY_IN_TWO_PARTY_SESSION",
    "RTC_E_SIP_AUTH_FAILED",
    "RTC_E_SIP_AUTH_HEADER_SENT",
    "RTC_E_SIP_AUTH_TIME_SKEW",
    "RTC_E_SIP_AUTH_TYPE_NOT_SUPPORTED",
    "RTC_E_SIP_CALL_CONNECTION_NOT_ESTABLISHED",
    "RTC_E_SIP_CALL_DISCONNECTED",
    "RTC_E_SIP_CODECS_DO_NOT_MATCH",
    "RTC_E_SIP_DNS_FAIL",
    "RTC_E_SIP_HEADER_NOT_PRESENT",
    "RTC_E_SIP_HIGH_SECURITY_SET_TLS",
    "RTC_E_SIP_HOLD_OPERATION_PENDING",
    "RTC_E_SIP_INVALID_CERTIFICATE",
    "RTC_E_SIP_INVITEE_PARTY_TIMEOUT",
    "RTC_E_SIP_INVITE_TRANSACTION_PENDING",
    "RTC_E_SIP_NEED_MORE_DATA",
    "RTC_E_SIP_NO_STREAM",
    "RTC_E_SIP_OTHER_PARTY_JOIN_IN_PROGRESS",
    "RTC_E_SIP_PARSE_FAILED",
    "RTC_E_SIP_PARTY_ALREADY_IN_SESSION",
    "RTC_E_SIP_PEER_PARTICIPANT_IN_MULTIPARTY_SESSION",
    "RTC_E_SIP_REFER_OPERATION_PENDING",
    "RTC_E_SIP_REQUEST_DESTINATION_ADDR_NOT_PRESENT",
    "RTC_E_SIP_SSL_NEGOTIATION_TIMEOUT",
    "RTC_E_SIP_SSL_TUNNEL_FAILED",
    "RTC_E_SIP_STACK_SHUTDOWN",
    "RTC_E_SIP_STREAM_NOT_PRESENT",
    "RTC_E_SIP_STREAM_PRESENT",
    "RTC_E_SIP_TCP_FAIL",
    "RTC_E_SIP_TIMEOUT",
    "RTC_E_SIP_TLS_FAIL",
    "RTC_E_SIP_TLS_INCOMPATIBLE_ENCRYPTION",
    "RTC_E_SIP_TRANSPORT_NOT_SUPPORTED",
    "RTC_E_SIP_UDP_SIZE_EXCEEDED",
    "RTC_E_SIP_UNHOLD_OPERATION_PENDING",
    "RTC_E_START_STREAM",
    "RTC_E_STATUS_CLIENT_ADDRESS_INCOMPLETE",
    "RTC_E_STATUS_CLIENT_AMBIGUOUS",
    "RTC_E_STATUS_CLIENT_BAD_EXTENSION",
    "RTC_E_STATUS_CLIENT_BAD_REQUEST",
    "RTC_E_STATUS_CLIENT_BUSY_HERE",
    "RTC_E_STATUS_CLIENT_CONFLICT",
    "RTC_E_STATUS_CLIENT_FORBIDDEN",
    "RTC_E_STATUS_CLIENT_GONE",
    "RTC_E_STATUS_CLIENT_LENGTH_REQUIRED",
    "RTC_E_STATUS_CLIENT_LOOP_DETECTED",
    "RTC_E_STATUS_CLIENT_METHOD_NOT_ALLOWED",
    "RTC_E_STATUS_CLIENT_NOT_ACCEPTABLE",
    "RTC_E_STATUS_CLIENT_NOT_FOUND",
    "RTC_E_STATUS_CLIENT_PAYMENT_REQUIRED",
    "RTC_E_STATUS_CLIENT_PROXY_AUTHENTICATION_REQUIRED",
    "RTC_E_STATUS_CLIENT_REQUEST_ENTITY_TOO_LARGE",
    "RTC_E_STATUS_CLIENT_REQUEST_TIMEOUT",
    "RTC_E_STATUS_CLIENT_REQUEST_URI_TOO_LARGE",
    "RTC_E_STATUS_CLIENT_TEMPORARILY_NOT_AVAILABLE",
    "RTC_E_STATUS_CLIENT_TOO_MANY_HOPS",
    "RTC_E_STATUS_CLIENT_TRANSACTION_DOES_NOT_EXIST",
    "RTC_E_STATUS_CLIENT_UNAUTHORIZED",
    "RTC_E_STATUS_CLIENT_UNSUPPORTED_MEDIA_TYPE",
    "RTC_E_STATUS_GLOBAL_BUSY_EVERYWHERE",
    "RTC_E_STATUS_GLOBAL_DECLINE",
    "RTC_E_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE",
    "RTC_E_STATUS_GLOBAL_NOT_ACCEPTABLE",
    "RTC_E_STATUS_INFO_CALL_FORWARDING",
    "RTC_E_STATUS_INFO_QUEUED",
    "RTC_E_STATUS_INFO_RINGING",
    "RTC_E_STATUS_INFO_TRYING",
    "RTC_E_STATUS_NOT_ACCEPTABLE_HERE",
    "RTC_E_STATUS_REDIRECT_ALTERNATIVE_SERVICE",
    "RTC_E_STATUS_REDIRECT_MOVED_PERMANENTLY",
    "RTC_E_STATUS_REDIRECT_MOVED_TEMPORARILY",
    "RTC_E_STATUS_REDIRECT_MULTIPLE_CHOICES",
    "RTC_E_STATUS_REDIRECT_SEE_OTHER",
    "RTC_E_STATUS_REDIRECT_USE_PROXY",
    "RTC_E_STATUS_REQUEST_TERMINATED",
    "RTC_E_STATUS_SERVER_BAD_GATEWAY",
    "RTC_E_STATUS_SERVER_INTERNAL_ERROR",
    "RTC_E_STATUS_SERVER_NOT_IMPLEMENTED",
    "RTC_E_STATUS_SERVER_SERVER_TIMEOUT",
    "RTC_E_STATUS_SERVER_SERVICE_UNAVAILABLE",
    "RTC_E_STATUS_SERVER_VERSION_NOT_SUPPORTED",
    "RTC_E_STATUS_SESSION_PROGRESS",
    "RTC_E_STATUS_SUCCESS",
    "RTC_E_TOO_MANY_GROUPS",
    "RTC_E_TOO_MANY_RETRIES",
    "RTC_E_TOO_SMALL_EXPIRES_VALUE",
    "RTC_E_UDP_NOT_SUPPORTED",
    "RTC_GROUP_EVENT_TYPE",
    "RTC_LISTEN_MODE",
    "RTC_MEDIA_EVENT_REASON",
    "RTC_MEDIA_EVENT_TYPE",
    "RTC_MESSAGING_EVENT_TYPE",
    "RTC_MESSAGING_USER_STATUS",
    "RTC_OFFER_WATCHER_MODE",
    "RTC_PARTICIPANT_STATE",
    "RTC_PORT_TYPE",
    "RTC_PRESENCE_PROPERTY",
    "RTC_PRESENCE_STATUS",
    "RTC_PRIVACY_MODE",
    "RTC_PROFILE_EVENT_TYPE",
    "RTC_PROVIDER_URI",
    "RTC_REGISTRATION_STATE",
    "RTC_REINVITE_STATE",
    "RTC_RING_TYPE",
    "RTC_ROAMING_EVENT_TYPE",
    "RTC_SECURITY_LEVEL",
    "RTC_SECURITY_TYPE",
    "RTC_SESSION_REFER_STATUS",
    "RTC_SESSION_STATE",
    "RTC_SESSION_TYPE",
    "RTC_S_ROAMING_NOT_SUPPORTED",
    "RTC_T120_APPLET",
    "RTC_TERMINATE_REASON",
    "RTC_USER_SEARCH_COLUMN",
    "RTC_USER_SEARCH_PREFERENCE",
    "RTC_VIDEO_DEVICE",
    "RTC_WATCHER_EVENT_TYPE",
    "RTC_WATCHER_MATCH_MODE",
    "RTC_WATCHER_STATE",
    "STATUS_SEVERITY_RTC_ERROR",
    "TRANSPORT_SETTING",
]
_arch_optional = [
]
