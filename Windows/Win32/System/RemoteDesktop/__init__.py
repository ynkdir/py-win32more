from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Audio.Apo
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.RemoteDesktop
import Windows.Win32.System.WinRT
import Windows.Win32.UI.WindowsAndMessaging
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
class AAAccountingData(Structure):
    userName: Windows.Win32.Foundation.BSTR
    clientName: Windows.Win32.Foundation.BSTR
    authType: Windows.Win32.System.RemoteDesktop.AAAuthSchemes
    resourceName: Windows.Win32.Foundation.BSTR
    portNumber: Int32
    protocolName: Windows.Win32.Foundation.BSTR
    numberOfBytesReceived: Int32
    numberOfBytesTransfered: Int32
    reasonForDisconnect: Windows.Win32.Foundation.BSTR
    mainSessionId: Guid
    subSessionId: Int32
AAAccountingDataType = Int32
AA_MAIN_SESSION_CREATION: AAAccountingDataType = 0
AA_SUB_SESSION_CREATION: AAAccountingDataType = 1
AA_SUB_SESSION_CLOSED: AAAccountingDataType = 2
AA_MAIN_SESSION_CLOSED: AAAccountingDataType = 3
AAAuthSchemes = Int32
AA_AUTH_MIN: AAAuthSchemes = 0
AA_AUTH_BASIC: AAAuthSchemes = 1
AA_AUTH_NTLM: AAAuthSchemes = 2
AA_AUTH_SC: AAAuthSchemes = 3
AA_AUTH_LOGGEDONCREDENTIALS: AAAuthSchemes = 4
AA_AUTH_NEGOTIATE: AAAuthSchemes = 5
AA_AUTH_ANY: AAAuthSchemes = 6
AA_AUTH_COOKIE: AAAuthSchemes = 7
AA_AUTH_DIGEST: AAAuthSchemes = 8
AA_AUTH_ORGID: AAAuthSchemes = 9
AA_AUTH_CONID: AAAuthSchemes = 10
AA_AUTH_SSPI_NTLM: AAAuthSchemes = 11
AA_AUTH_MAX: AAAuthSchemes = 12
AATrustClassID = Int32
AA_UNTRUSTED: AATrustClassID = 0
AA_TRUSTEDUSER_UNTRUSTEDCLIENT: AATrustClassID = 1
AA_TRUSTEDUSER_TRUSTEDCLIENT: AATrustClassID = 2
ADsTSUserEx = Guid('e2e9cae6-1e7b-4b8e-ba-bd-e9-bf-62-92-ac-29')
class AE_CURRENT_POSITION(Structure):
    u64DevicePosition: UInt64
    u64StreamPosition: UInt64
    u64PaddingFrames: UInt64
    hnsQPCPosition: Int64
    f32FramesPerSecond: Single
    Flag: Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS
AE_POSITION_FLAGS = Int32
POSITION_INVALID: AE_POSITION_FLAGS = 0
POSITION_DISCONTINUOUS: AE_POSITION_FLAGS = 1
POSITION_CONTINUOUS: AE_POSITION_FLAGS = 2
POSITION_QPC_ERROR: AE_POSITION_FLAGS = 4
WTS_CURRENT_SERVER: Windows.Win32.Foundation.HANDLE = 0
WTS_CURRENT_SERVER_HANDLE: Windows.Win32.Foundation.HANDLE = 0
WTS_CURRENT_SERVER_NAME: String = ''
WTS_DOMAIN_LENGTH: UInt32 = 255
WTS_USERNAME_LENGTH: UInt32 = 255
WTS_PASSWORD_LENGTH: UInt32 = 255
WTS_DIRECTORY_LENGTH: UInt32 = 256
WTS_INITIALPROGRAM_LENGTH: UInt32 = 256
WTS_PROTOCOL_NAME_LENGTH: UInt32 = 8
WTS_DRIVER_NAME_LENGTH: UInt32 = 8
WTS_DEVICE_NAME_LENGTH: UInt32 = 19
WTS_IMEFILENAME_LENGTH: UInt32 = 32
WTS_CLIENTNAME_LENGTH: UInt32 = 20
WTS_CLIENTADDRESS_LENGTH: UInt32 = 30
WTS_CLIENT_PRODUCT_ID_LENGTH: UInt32 = 32
WTS_MAX_PROTOCOL_CACHE: UInt32 = 4
WTS_MAX_CACHE_RESERVED: UInt32 = 20
WTS_MAX_RESERVED: UInt32 = 100
WTS_MAX_COUNTERS: UInt32 = 100
WTS_MAX_DISPLAY_IOCTL_DATA: UInt32 = 256
WTS_PERF_DISABLE_NOTHING: UInt32 = 0
WTS_PERF_DISABLE_WALLPAPER: UInt32 = 1
WTS_PERF_DISABLE_FULLWINDOWDRAG: UInt32 = 2
WTS_PERF_DISABLE_MENUANIMATIONS: UInt32 = 4
WTS_PERF_DISABLE_THEMING: UInt32 = 8
WTS_PERF_ENABLE_ENHANCED_GRAPHICS: UInt32 = 16
WTS_PERF_DISABLE_CURSOR_SHADOW: UInt32 = 32
WTS_PERF_DISABLE_CURSORSETTINGS: UInt32 = 64
WTS_PERF_ENABLE_FONT_SMOOTHING: UInt32 = 128
WTS_PERF_ENABLE_DESKTOP_COMPOSITION: UInt32 = 256
WTS_VALUE_TYPE_ULONG: UInt32 = 1
WTS_VALUE_TYPE_STRING: UInt32 = 2
WTS_VALUE_TYPE_BINARY: UInt32 = 3
WTS_VALUE_TYPE_GUID: UInt32 = 4
WTS_KEY_EXCHANGE_ALG_RSA: UInt32 = 1
WTS_KEY_EXCHANGE_ALG_DH: UInt32 = 2
WTS_LICENSE_PROTOCOL_VERSION: UInt32 = 65536
WTS_LICENSE_PREAMBLE_VERSION: UInt32 = 3
WRDS_DOMAIN_LENGTH: UInt32 = 255
WRDS_USERNAME_LENGTH: UInt32 = 255
WRDS_PASSWORD_LENGTH: UInt32 = 255
WRDS_DIRECTORY_LENGTH: UInt32 = 256
WRDS_INITIALPROGRAM_LENGTH: UInt32 = 256
WRDS_PROTOCOL_NAME_LENGTH: UInt32 = 8
WRDS_DRIVER_NAME_LENGTH: UInt32 = 8
WRDS_DEVICE_NAME_LENGTH: UInt32 = 19
WRDS_IMEFILENAME_LENGTH: UInt32 = 32
WRDS_CLIENTNAME_LENGTH: UInt32 = 20
WRDS_CLIENTADDRESS_LENGTH: UInt32 = 30
WRDS_CLIENT_PRODUCT_ID_LENGTH: UInt32 = 32
WRDS_MAX_PROTOCOL_CACHE: UInt32 = 4
WRDS_MAX_CACHE_RESERVED: UInt32 = 20
WRDS_MAX_RESERVED: UInt32 = 100
WRDS_MAX_COUNTERS: UInt32 = 100
WRDS_MAX_DISPLAY_IOCTL_DATA: UInt32 = 256
WRDS_PERF_DISABLE_NOTHING: UInt32 = 0
WRDS_PERF_DISABLE_WALLPAPER: UInt32 = 1
WRDS_PERF_DISABLE_FULLWINDOWDRAG: UInt32 = 2
WRDS_PERF_DISABLE_MENUANIMATIONS: UInt32 = 4
WRDS_PERF_DISABLE_THEMING: UInt32 = 8
WRDS_PERF_ENABLE_ENHANCED_GRAPHICS: UInt32 = 16
WRDS_PERF_DISABLE_CURSOR_SHADOW: UInt32 = 32
WRDS_PERF_DISABLE_CURSORSETTINGS: UInt32 = 64
WRDS_PERF_ENABLE_FONT_SMOOTHING: UInt32 = 128
WRDS_PERF_ENABLE_DESKTOP_COMPOSITION: UInt32 = 256
WRDS_VALUE_TYPE_ULONG: UInt32 = 1
WRDS_VALUE_TYPE_STRING: UInt32 = 2
WRDS_VALUE_TYPE_BINARY: UInt32 = 3
WRDS_VALUE_TYPE_GUID: UInt32 = 4
WRDS_KEY_EXCHANGE_ALG_RSA: UInt32 = 1
WRDS_KEY_EXCHANGE_ALG_DH: UInt32 = 2
WRDS_LICENSE_PROTOCOL_VERSION: UInt32 = 65536
WRDS_LICENSE_PREAMBLE_VERSION: UInt32 = 3
SINGLE_SESSION: UInt32 = 1
FORCE_REJOIN: UInt32 = 2
FORCE_REJOIN_IN_CLUSTERMODE: UInt32 = 3
RESERVED_FOR_LEGACY: UInt32 = 4
KEEP_EXISTING_SESSIONS: UInt32 = 8
CHANNEL_EVENT_INITIALIZED: UInt32 = 0
CHANNEL_EVENT_CONNECTED: UInt32 = 1
CHANNEL_EVENT_V1_CONNECTED: UInt32 = 2
CHANNEL_EVENT_DISCONNECTED: UInt32 = 3
CHANNEL_EVENT_TERMINATED: UInt32 = 4
CHANNEL_EVENT_DATA_RECEIVED: UInt32 = 10
CHANNEL_EVENT_WRITE_COMPLETE: UInt32 = 11
CHANNEL_EVENT_WRITE_CANCELLED: UInt32 = 12
CHANNEL_RC_OK: UInt32 = 0
CHANNEL_RC_ALREADY_INITIALIZED: UInt32 = 1
CHANNEL_RC_NOT_INITIALIZED: UInt32 = 2
CHANNEL_RC_ALREADY_CONNECTED: UInt32 = 3
CHANNEL_RC_NOT_CONNECTED: UInt32 = 4
CHANNEL_RC_TOO_MANY_CHANNELS: UInt32 = 5
CHANNEL_RC_BAD_CHANNEL: UInt32 = 6
CHANNEL_RC_BAD_CHANNEL_HANDLE: UInt32 = 7
CHANNEL_RC_NO_BUFFER: UInt32 = 8
CHANNEL_RC_BAD_INIT_HANDLE: UInt32 = 9
CHANNEL_RC_NOT_OPEN: UInt32 = 10
CHANNEL_RC_BAD_PROC: UInt32 = 11
CHANNEL_RC_NO_MEMORY: UInt32 = 12
CHANNEL_RC_UNKNOWN_CHANNEL_NAME: UInt32 = 13
CHANNEL_RC_ALREADY_OPEN: UInt32 = 14
CHANNEL_RC_NOT_IN_VIRTUALCHANNELENTRY: UInt32 = 15
CHANNEL_RC_NULL_DATA: UInt32 = 16
CHANNEL_RC_ZERO_LENGTH: UInt32 = 17
CHANNEL_RC_INVALID_INSTANCE: UInt32 = 18
CHANNEL_RC_UNSUPPORTED_VERSION: UInt32 = 19
CHANNEL_RC_INITIALIZATION_ERROR: UInt32 = 20
VIRTUAL_CHANNEL_VERSION_WIN2000: UInt32 = 1
CHANNEL_CHUNK_LENGTH: UInt32 = 1600
CHANNEL_BUFFER_SIZE: UInt32 = 65535
CHANNEL_FLAG_FIRST: UInt32 = 1
CHANNEL_FLAG_LAST: UInt32 = 2
CHANNEL_FLAG_MIDDLE: UInt32 = 0
CHANNEL_FLAG_FAIL: UInt32 = 256
CHANNEL_OPTION_INITIALIZED: UInt32 = 2147483648
CHANNEL_OPTION_ENCRYPT_RDP: UInt32 = 1073741824
CHANNEL_OPTION_ENCRYPT_SC: UInt32 = 536870912
CHANNEL_OPTION_ENCRYPT_CS: UInt32 = 268435456
CHANNEL_OPTION_PRI_HIGH: UInt32 = 134217728
CHANNEL_OPTION_PRI_MED: UInt32 = 67108864
CHANNEL_OPTION_PRI_LOW: UInt32 = 33554432
CHANNEL_OPTION_COMPRESS_RDP: UInt32 = 8388608
CHANNEL_OPTION_COMPRESS: UInt32 = 4194304
CHANNEL_OPTION_SHOW_PROTOCOL: UInt32 = 2097152
CHANNEL_OPTION_REMOTE_CONTROL_PERSISTENT: UInt32 = 1048576
CHANNEL_MAX_COUNT: UInt32 = 30
CHANNEL_NAME_LEN: UInt32 = 7
MAX_POLICY_ATTRIBUTES: UInt32 = 20
WTS_CURRENT_SESSION: UInt32 = 4294967295
USERNAME_LENGTH: UInt32 = 20
CLIENTNAME_LENGTH: UInt32 = 20
CLIENTADDRESS_LENGTH: UInt32 = 30
WTS_WSD_LOGOFF: UInt32 = 1
WTS_WSD_SHUTDOWN: UInt32 = 2
WTS_WSD_REBOOT: UInt32 = 4
WTS_WSD_POWEROFF: UInt32 = 8
WTS_WSD_FASTREBOOT: UInt32 = 16
MAX_ELAPSED_TIME_LENGTH: UInt32 = 15
MAX_DATE_TIME_LENGTH: UInt32 = 56
WINSTATIONNAME_LENGTH: UInt32 = 32
DOMAIN_LENGTH: UInt32 = 17
WTS_DRIVE_LENGTH: UInt32 = 3
WTS_LISTENER_NAME_LENGTH: UInt32 = 32
WTS_COMMENT_LENGTH: UInt32 = 60
WTS_LISTENER_CREATE: UInt32 = 1
WTS_LISTENER_UPDATE: UInt32 = 16
WTS_PROTOCOL_TYPE_CONSOLE: UInt32 = 0
WTS_PROTOCOL_TYPE_ICA: UInt32 = 1
WTS_PROTOCOL_TYPE_RDP: UInt32 = 2
WTS_SESSIONSTATE_UNKNOWN: UInt32 = 4294967295
WTS_SESSIONSTATE_LOCK: UInt32 = 0
WTS_SESSIONSTATE_UNLOCK: UInt32 = 1
PRODUCTINFO_COMPANYNAME_LENGTH: UInt32 = 256
PRODUCTINFO_PRODUCTID_LENGTH: UInt32 = 4
VALIDATIONINFORMATION_LICENSE_LENGTH: UInt32 = 16384
VALIDATIONINFORMATION_HARDWAREID_LENGTH: UInt32 = 20
WTS_EVENT_NONE: UInt32 = 0
WTS_EVENT_CREATE: UInt32 = 1
WTS_EVENT_DELETE: UInt32 = 2
WTS_EVENT_RENAME: UInt32 = 4
WTS_EVENT_CONNECT: UInt32 = 8
WTS_EVENT_DISCONNECT: UInt32 = 16
WTS_EVENT_LOGON: UInt32 = 32
WTS_EVENT_LOGOFF: UInt32 = 64
WTS_EVENT_STATECHANGE: UInt32 = 128
WTS_EVENT_LICENSE: UInt32 = 256
WTS_EVENT_ALL: UInt32 = 2147483647
WTS_EVENT_FLUSH: UInt32 = 2147483648
REMOTECONTROL_KBDSHIFT_HOTKEY: UInt32 = 1
REMOTECONTROL_KBDCTRL_HOTKEY: UInt32 = 2
REMOTECONTROL_KBDALT_HOTKEY: UInt32 = 4
WTS_CHANNEL_OPTION_DYNAMIC: UInt32 = 1
WTS_CHANNEL_OPTION_DYNAMIC_PRI_LOW: UInt32 = 0
WTS_CHANNEL_OPTION_DYNAMIC_PRI_MED: UInt32 = 2
WTS_CHANNEL_OPTION_DYNAMIC_PRI_HIGH: UInt32 = 4
WTS_CHANNEL_OPTION_DYNAMIC_PRI_REAL: UInt32 = 6
WTS_CHANNEL_OPTION_DYNAMIC_NO_COMPRESS: UInt32 = 8
NOTIFY_FOR_ALL_SESSIONS: UInt32 = 1
NOTIFY_FOR_THIS_SESSION: UInt32 = 0
WTS_PROCESS_INFO_LEVEL_0: UInt32 = 0
WTS_PROCESS_INFO_LEVEL_1: UInt32 = 1
PLUGIN_CAPABILITY_EXTERNAL_REDIRECTION: UInt32 = 1
MaxFQDN_Len: UInt32 = 256
MaxNetBiosName_Len: UInt32 = 16
MaxNumOfExposed_IPs: UInt32 = 12
MaxUserName_Len: UInt32 = 104
MaxDomainName_Len: UInt32 = 256
MaxFarm_Len: UInt32 = 256
MaxAppName_Len: UInt32 = 256
WKS_FLAG_CLEAR_CREDS_ON_LAST_RESOURCE: UInt32 = 1
WKS_FLAG_PASSWORD_ENCRYPTED: UInt32 = 2
WKS_FLAG_CREDS_AUTHENTICATED: UInt32 = 4
SB_SYNCH_CONFLICT_MAX_WRITE_ATTEMPTS: UInt32 = 100
ACQUIRE_TARGET_LOCK_TIMEOUT: UInt32 = 300000
RENDER_HINT_CLEAR: UInt32 = 0
RENDER_HINT_VIDEO: UInt32 = 1
RENDER_HINT_MAPPEDWINDOW: UInt32 = 2
WTS_PROPERTY_DEFAULT_CONFIG: String = 'DefaultConfig'
TS_VC_LISTENER_STATIC_CHANNEL: UInt32 = 1
WRdsGraphicsChannels_LossyChannelMaxMessageSize: UInt32 = 988
RFX_RDP_MSG_PREFIX: UInt32 = 0
RFX_GFX_MSG_PREFIX: UInt32 = 48
RFX_GFX_MSG_PREFIX_MASK: UInt32 = 48
RFX_GFX_MAX_SUPPORTED_MONITORS: UInt32 = 16
RFX_CLIENT_ID_LENGTH: UInt32 = 32
DISPID_METHOD_REMOTEDESKTOPCLIENT_CONNECT: UInt32 = 701
DISPID_METHOD_REMOTEDESKTOPCLIENT_DISCONNECT: UInt32 = 702
DISPID_METHOD_REMOTEDESKTOPCLIENT_RECONNECT: UInt32 = 703
DISPID_METHOD_REMOTEDESKTOPCLIENT_DELETE_SAVED_CREDENTIALS: UInt32 = 704
DISPID_METHOD_REMOTEDESKTOPCLIENT_UPDATE_SESSION_DISPLAYSETTINGS: UInt32 = 705
DISPID_METHOD_REMOTEDESKTOPCLIENT_ATTACH_EVENT: UInt32 = 706
DISPID_METHOD_REMOTEDESKTOPCLIENT_DETACH_EVENT: UInt32 = 707
DISPID_PROP_REMOTEDESKTOPCLIENT_SETTINGS: UInt32 = 710
DISPID_PROP_REMOTEDESKTOPCLIENT_ACTIONS: UInt32 = 711
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCH_POINTER: UInt32 = 712
DISPID_METHOD_REMOTEDESKTOPCLIENT_SET_RDPPROPERTY: UInt32 = 720
DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_RDPPROPERTY: UInt32 = 721
DISPID_METHOD_REMOTEDESKTOPCLIENT_APPLY_SETTINGS: UInt32 = 722
DISPID_METHOD_REMOTEDESKTOPCLIENT_RETRIEVE_SETTINGS: UInt32 = 723
DISPID_METHOD_REMOTEDESKTOPCLIENT_SUSPEND_SCREEN_UPDATES: UInt32 = 730
DISPID_METHOD_REMOTEDESKTOPCLIENT_RESUME_SCREEN_UPDATES: UInt32 = 731
DISPID_METHOD_REMOTEDESKTOPCLIENT_EXECUTE_REMOTE_ACTION: UInt32 = 732
DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_SNAPSHOT: UInt32 = 733
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_ENABLED: UInt32 = 740
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_EVENTSENABLED: UInt32 = 741
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_POINTERSPEED: UInt32 = 742
DISPID_AX_CONNECTING: UInt32 = 750
DISPID_AX_CONNECTED: UInt32 = 751
DISPID_AX_LOGINCOMPLETED: UInt32 = 752
DISPID_AX_DISCONNECTED: UInt32 = 753
DISPID_AX_STATUSCHANGED: UInt32 = 754
DISPID_AX_AUTORECONNECTING: UInt32 = 755
DISPID_AX_AUTORECONNECTED: UInt32 = 756
DISPID_AX_DIALOGDISPLAYING: UInt32 = 757
DISPID_AX_DIALOGDISMISSED: UInt32 = 758
DISPID_AX_NETWORKSTATUSCHANGED: UInt32 = 759
DISPID_AX_ADMINMESSAGERECEIVED: UInt32 = 760
DISPID_AX_KEYCOMBINATIONPRESSED: UInt32 = 761
DISPID_AX_REMOTEDESKTOPSIZECHANGED: UInt32 = 762
DISPID_AX_TOUCHPOINTERCURSORMOVED: UInt32 = 800
RDCLIENT_BITMAP_RENDER_SERVICE: Guid = Guid('e4cc08cb-942e-4b19-85-04-bd-5a-89-a7-47-f5')
WTS_QUERY_ALLOWED_INITIAL_APP: Guid = Guid('c77d1b30-5be1-4c6b-a0-e1-bd-6d-2e-5c-9f-cc')
WTS_QUERY_LOGON_SCREEN_SIZE: Guid = Guid('8b8e0fe7-0804-4a0e-b2-79-86-60-b1-df-00-49')
WTS_QUERY_AUDIOENUM_DLL: Guid = Guid('9bf4fa97-c883-4c2a-80-ab-5a-39-c9-af-00-db')
WTS_QUERY_MF_FORMAT_SUPPORT: Guid = Guid('41869ad0-6332-4dc8-95-d5-db-74-9e-2f-1d-94')
WRDS_SERVICE_ID_GRAPHICS_GUID: Guid = Guid('d2993f4d-02cf-4280-8c-48-16-24-b4-4f-87-06')
PROPERTY_DYNAMIC_TIME_ZONE_INFORMATION: Guid = Guid('0cdfd28e-d0b9-4c1f-a5-eb-6d-1f-6c-65-35-b9')
PROPERTY_TYPE_GET_FAST_RECONNECT: Guid = Guid('6212d757-0043-4862-99-c3-9f-30-59-ac-2a-3b')
PROPERTY_TYPE_GET_FAST_RECONNECT_USER_SID: Guid = Guid('197c427a-0135-4b6d-9c-5e-e6-57-9a-0a-b6-25')
PROPERTY_TYPE_ENABLE_UNIVERSAL_APPS_FOR_CUSTOM_SHELL: Guid = Guid('ed2c3fda-338d-4d3f-81-a3-e7-67-31-0d-90-8e')
CONNECTION_PROPERTY_IDLE_TIME_WARNING: Guid = Guid('693f7ff5-0c4e-4d17-b8-e0-1f-70-32-5e-5d-58')
CONNECTION_PROPERTY_CURSOR_BLINK_DISABLED: Guid = Guid('4b150580-fea4-4d3c-9d-e4-74-33-a6-66-18-f7')
@winfunctype('WTSAPI32.dll')
def WTSStopRemoteControlSession(LogonId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSStartRemoteControlSessionW(pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetLogonId: UInt32, HotkeyVk: Byte, HotkeyModifiers: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSStartRemoteControlSessionA(pTargetServerName: Windows.Win32.Foundation.PSTR, TargetLogonId: UInt32, HotkeyVk: Byte, HotkeyModifiers: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSConnectSessionA(LogonId: UInt32, TargetLogonId: UInt32, pPassword: Windows.Win32.Foundation.PSTR, bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSConnectSessionW(LogonId: UInt32, TargetLogonId: UInt32, pPassword: Windows.Win32.Foundation.PWSTR, bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateServersW(pDomainName: Windows.Win32.Foundation.PWSTR, Reserved: UInt32, Version: UInt32, ppServerInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVER_INFOW_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateServersA(pDomainName: Windows.Win32.Foundation.PSTR, Reserved: UInt32, Version: UInt32, ppServerInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVER_INFOA_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerW(pServerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerA(pServerName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerExW(pServerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerExA(pServerName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSCloseServer(hServer: Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsW(hServer: Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppSessionInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFOW_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsA(hServer: Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppSessionInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFOA_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsExW(hServer: Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), Filter: UInt32, ppSessionInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFO_1W_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsExA(hServer: Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), Filter: UInt32, ppSessionInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFO_1A_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesW(hServer: Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppProcessInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROCESS_INFOW_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesA(hServer: Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppProcessInfo: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROCESS_INFOA_head)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSTerminateProcess(hServer: Windows.Win32.Foundation.HANDLE, ProcessId: UInt32, ExitCode: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQuerySessionInformationW(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, WTSInfoClass: Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS, ppBuffer: POINTER(Windows.Win32.Foundation.PWSTR), pBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQuerySessionInformationA(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, WTSInfoClass: Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS, ppBuffer: POINTER(Windows.Win32.Foundation.PSTR), pBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryUserConfigW(pServerName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR, WTSConfigClass: Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, ppBuffer: POINTER(Windows.Win32.Foundation.PWSTR), pBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryUserConfigA(pServerName: Windows.Win32.Foundation.PSTR, pUserName: Windows.Win32.Foundation.PSTR, WTSConfigClass: Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, ppBuffer: POINTER(Windows.Win32.Foundation.PSTR), pBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetUserConfigW(pServerName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR, WTSConfigClass: Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, pBuffer: Windows.Win32.Foundation.PWSTR, DataLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetUserConfigA(pServerName: Windows.Win32.Foundation.PSTR, pUserName: Windows.Win32.Foundation.PSTR, WTSConfigClass: Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, pBuffer: Windows.Win32.Foundation.PSTR, DataLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSendMessageW(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pTitle: Windows.Win32.Foundation.PWSTR, TitleLength: UInt32, pMessage: Windows.Win32.Foundation.PWSTR, MessageLength: UInt32, Style: Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, Timeout: UInt32, pResponse: POINTER(Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_RESULT), bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSendMessageA(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pTitle: Windows.Win32.Foundation.PSTR, TitleLength: UInt32, pMessage: Windows.Win32.Foundation.PSTR, MessageLength: UInt32, Style: Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, Timeout: UInt32, pResponse: POINTER(Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_RESULT), bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSDisconnectSession(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSLogoffSession(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSShutdownSystem(hServer: Windows.Win32.Foundation.HANDLE, ShutdownFlag: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSWaitSystemEvent(hServer: Windows.Win32.Foundation.HANDLE, EventMask: UInt32, pEventFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelOpen(hServer: Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pVirtualName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.System.RemoteDesktop.HwtsVirtualChannelHandle: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelOpenEx(SessionId: UInt32, pVirtualName: Windows.Win32.Foundation.PSTR, flags: UInt32) -> Windows.Win32.System.RemoteDesktop.HwtsVirtualChannelHandle: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelClose(hChannelHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelRead(hChannelHandle: Windows.Win32.Foundation.HANDLE, TimeOut: UInt32, Buffer: Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelWrite(hChannelHandle: Windows.Win32.Foundation.HANDLE, Buffer: Windows.Win32.Foundation.PSTR, Length: UInt32, pBytesWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelPurgeInput(hChannelHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelPurgeOutput(hChannelHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelQuery(hChannelHandle: Windows.Win32.Foundation.HANDLE, param1: Windows.Win32.System.RemoteDesktop.WTS_VIRTUAL_CLASS, ppBuffer: POINTER(c_void_p), pBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSFreeMemory(pMemory: c_void_p) -> Void: ...
@winfunctype('WTSAPI32.dll')
def WTSRegisterSessionNotification(hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSUnRegisterSessionNotification(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSRegisterSessionNotificationEx(hServer: Windows.Win32.Foundation.HANDLE, hWnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSUnRegisterSessionNotificationEx(hServer: Windows.Win32.Foundation.HANDLE, hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryUserToken(SessionId: UInt32, phToken: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSFreeMemoryExW(WTSTypeClass: Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS, pMemory: c_void_p, NumberOfEntries: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSFreeMemoryExA(WTSTypeClass: Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS, pMemory: c_void_p, NumberOfEntries: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesExW(hServer: Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), SessionId: UInt32, ppProcessInfo: POINTER(Windows.Win32.Foundation.PWSTR), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesExA(hServer: Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), SessionId: UInt32, ppProcessInfo: POINTER(Windows.Win32.Foundation.PSTR), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateListenersW(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListeners: POINTER(POINTER(UInt16)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateListenersA(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListeners: POINTER(POINTER(SByte)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryListenerConfigW(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryListenerConfigA(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PSTR, pBuffer: POINTER(Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSCreateListenerW(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGW_head), flag: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSCreateListenerA(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PSTR, pBuffer: POINTER(Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGA_head), flag: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetListenerSecurityW(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetListenerSecurityA(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSGetListenerSecurityW(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PWSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSGetListenerSecurityA(hServer: Windows.Win32.Foundation.HANDLE, pReserved: c_void_p, Reserved: UInt32, pListenerName: Windows.Win32.Foundation.PSTR, SecurityInformation: UInt32, pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnableChildSessions(bEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSIsChildSessionsEnabled(pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSGetChildSessionId(pSessionId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetRenderHint(pRenderHintID: POINTER(UInt64), hwndOwner: Windows.Win32.Foundation.HWND, renderHintType: UInt32, cbHintDataLength: UInt32, pHintData: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ProcessIdToSessionId(dwProcessId: UInt32, pSessionId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WTSGetActiveConsoleSessionId() -> UInt32: ...
class BITMAP_RENDERER_STATISTICS(Structure):
    dwFramesDelivered: UInt32
    dwFramesDropped: UInt32
class CHANNEL_DEF(Structure):
    name: Windows.Win32.Foundation.CHAR * 8
    options: UInt32
    _pack_ = 1
class CHANNEL_ENTRY_POINTS(Structure):
    cbSize: UInt32
    protocolVersion: UInt32
    pVirtualChannelInit: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELINIT
    pVirtualChannelOpen: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELOPEN
    pVirtualChannelClose: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELCLOSE
    pVirtualChannelWrite: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELWRITE
class CHANNEL_PDU_HEADER(Structure):
    length: UInt32
    flags: UInt32
class CLIENT_DISPLAY(Structure):
    HorizontalResolution: UInt32
    VerticalResolution: UInt32
    ColorDepth: UInt32
CLIENT_MESSAGE_TYPE = Int32
CLIENT_MESSAGE_CONNECTION_INVALID: CLIENT_MESSAGE_TYPE = 0
CLIENT_MESSAGE_CONNECTION_STATUS: CLIENT_MESSAGE_TYPE = 1
CLIENT_MESSAGE_CONNECTION_ERROR: CLIENT_MESSAGE_TYPE = 2
CONNECTION_CHANGE_NOTIFICATION = Int32
CONNECTION_REQUEST_INVALID: CONNECTION_CHANGE_NOTIFICATION = 0
CONNECTION_REQUEST_PENDING: CONNECTION_CHANGE_NOTIFICATION = 1
CONNECTION_REQUEST_FAILED: CONNECTION_CHANGE_NOTIFICATION = 2
CONNECTION_REQUEST_TIMEDOUT: CONNECTION_CHANGE_NOTIFICATION = 3
CONNECTION_REQUEST_SUCCEEDED: CONNECTION_CHANGE_NOTIFICATION = 4
CONNECTION_REQUEST_CANCELLED: CONNECTION_CHANGE_NOTIFICATION = 5
CONNECTION_REQUEST_LB_COMPLETED: CONNECTION_CHANGE_NOTIFICATION = 6
CONNECTION_REQUEST_QUERY_PL_COMPLETED: CONNECTION_CHANGE_NOTIFICATION = 7
CONNECTION_REQUEST_ORCH_COMPLETED: CONNECTION_CHANGE_NOTIFICATION = 8
HwtsVirtualChannelHandle = IntPtr
class IADsTSUserEx(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c4930e79-2989-4462-8a-60-2f-cf-2f-29-55-ef')
    @commethod(7)
    def get_TerminalServicesProfilePath(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TerminalServicesProfilePath(pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TerminalServicesHomeDirectory(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TerminalServicesHomeDirectory(pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TerminalServicesHomeDrive(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_TerminalServicesHomeDrive(pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowLogon(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowLogon(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableRemoteControl(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableRemoteControl(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MaxDisconnectionTime(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_MaxDisconnectionTime(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MaxConnectionTime(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_MaxConnectionTime(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_MaxIdleTime(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_MaxIdleTime(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ReconnectionAction(pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_ReconnectionAction(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_BrokenConnectionAction(pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_BrokenConnectionAction(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ConnectClientDrivesAtLogon(pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ConnectClientDrivesAtLogon(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ConnectClientPrintersAtLogon(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ConnectClientPrintersAtLogon(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DefaultToMainPrinter(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_DefaultToMainPrinter(NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_TerminalServicesWorkDirectory(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_TerminalServicesWorkDirectory(pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TerminalServicesInitialProgram(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_TerminalServicesInitialProgram(pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioDeviceEndpoint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d4952f5a-a0b2-4cc4-8b-82-93-58-48-8d-d8-ac')
    @commethod(3)
    def SetBuffer(MaxPeriod: Int64, u32LatencyCoefficient: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRTCaps(pbIsRTCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventDrivenCapable(pbisEventCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteExclusiveModeParametersToSharedMemory(hTargetProcess: UIntPtr, hnsPeriod: Int64, hnsBufferDuration: Int64, u32LatencyCoefficient: UInt32, pu32SharedMemorySize: POINTER(UInt32), phSharedMemory: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpoint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30a99515-1527-4451-af-9f-00-c5-f0-23-4d-af')
    @commethod(3)
    def GetFrameFormat(ppFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesPerPacket(pFramesPerPacket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatency(pLatency: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStreamFlags(streamFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEventHandle(eventHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c684b72a-6df4-4774-bd-f9-76-b7-75-09-b6-53')
    @commethod(3)
    def Start() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfd2005f-a6e5-4d39-a2-65-93-9a-da-9f-bb-4d')
    @commethod(3)
    def GetCurrentPadding(pPadding: POINTER(Int64), pAeCurrentPosition: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> Void: ...
    @commethod(4)
    def ProcessingComplete() -> Void: ...
    @commethod(5)
    def SetPinInactive() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPinActive() -> Windows.Win32.Foundation.HRESULT: ...
class IAudioInputEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8026ab61-92b2-43c1-a1-df-5c-37-eb-d0-8d-82')
    @commethod(3)
    def GetInputDataPointer(pConnectionProperty: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head), pAeTimeStamp: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> Void: ...
    @commethod(4)
    def ReleaseInputDataPointer(u32FrameCount: UInt32, pDataPointer: UIntPtr) -> Void: ...
    @commethod(5)
    def PulseEndpoint() -> Void: ...
class IAudioOutputEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fa906e4-c31c-4e31-93-2e-19-a6-63-85-e9-aa')
    @commethod(3)
    def GetOutputDataPointer(u32FrameCount: UInt32, pAeTimeStamp: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> UIntPtr: ...
    @commethod(4)
    def ReleaseOutputDataPointer(pConnectionProperty: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)) -> Void: ...
    @commethod(5)
    def PulseEndpoint() -> Void: ...
class IRemoteDesktopClient(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('57d25668-625a-4905-be-4e-30-4c-aa-13-f8-9c')
    @commethod(7)
    def Connect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reconnect(width: UInt32, height: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Settings(settings: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(actions: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientActions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TouchPointer(touchPointer: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientTouchPointer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteSavedCredentials(serverName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateSessionDisplaySettings(width: UInt32, height: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def attachEvent(eventName: Windows.Win32.Foundation.BSTR, callback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def detachEvent(eventName: Windows.Win32.Foundation.BSTR, callback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientActions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7d54bc4e-1028-45d4-8b-0a-b9-b6-bf-fb-a1-76')
    @commethod(7)
    def SuspendScreenUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResumeScreenUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ExecuteRemoteAction(remoteAction: Windows.Win32.System.RemoteDesktop.RemoteActionType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSnapshot(snapshotEncoding: Windows.Win32.System.RemoteDesktop.SnapshotEncodingType, snapshotFormat: Windows.Win32.System.RemoteDesktop.SnapshotFormatType, snapshotWidth: UInt32, snapshotHeight: UInt32, snapshotData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientSettings(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('48a0f2a7-2713-431f-bb-ac-6f-45-58-e7-d6-4d')
    @commethod(7)
    def ApplySettings(rdpFileContents: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveSettings(rdpFileContents: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRdpProperty(propertyName: Windows.Win32.Foundation.BSTR, value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRdpProperty(propertyName: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientTouchPointer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('260ec22d-8cbc-44b5-9e-88-2a-37-f6-c9-3a-e9')
    @commethod(7)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_EventsEnabled(eventsEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventsEnabled(eventsEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_PointerSpeed(pointerSpeed: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PointerSpeed(pointerSpeed: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteSystemAdditionalInfoProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eeaa3d5f-ec63-4d27-af-38-e8-6b-1d-72-92-cb')
    @commethod(3)
    def GetAdditionalInfo(deduplicationId: POINTER(Windows.Win32.System.WinRT.HSTRING), riid: POINTER(Guid), mapView: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAccountingEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ce2a0c9-e874-4f1a-86-f4-06-bb-b9-11-53-38')
    @commethod(3)
    def DoAccounting(accountingDataType: Windows.Win32.System.RemoteDesktop.AAAccountingDataType, accountingData: Windows.Win32.System.RemoteDesktop.AAAccountingData) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticateUserSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2c3e2e73-a782-47f9-8d-fb-77-ee-1e-d2-7a-03')
    @commethod(3)
    def OnUserAuthenticated(userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, context: UIntPtr, userToken: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUserAuthenticationFailed(context: UIntPtr, genericErrorCode: Windows.Win32.Foundation.HRESULT, specificErrorCode: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReauthenticateUser(context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisconnectUser(context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticationEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ee3e5bf-04ab-4691-99-8c-d7-f6-22-32-1a-56')
    @commethod(3)
    def AuthenticateUser(mainSessionId: Guid, cookieData: c_char_p_no, numCookieBytes: UInt32, context: UIntPtr, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthenticateUserSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelAuthentication(mainSessionId: Guid, context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeConnectionSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c27ece33-7781-4318-98-ef-1c-f2-da-7b-70-05')
    @commethod(3)
    def OnConnectionAuthorized(hrIn: Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, cbSoHResponse: UInt32, pbSoHResponse: c_char_p_no, idleTimeout: UInt32, sessionTimeout: UInt32, sessionTimeoutAction: Windows.Win32.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE, trustClass: Windows.Win32.System.RemoteDesktop.AATrustClassID, policyAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeResourceSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('feddfcd4-fa12-4435-ae-55-7a-d1-a9-77-9a-f7')
    @commethod(3)
    def OnChannelAuthorized(hrIn: Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, subSessionId: Int32, allowedResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numAllowedResourceNames: UInt32, failedResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numFailedResourceNames: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGPolicyEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8bc24f08-6223-42f4-a5-b4-8e-37-cd-13-5b-bd')
    @commethod(3)
    def AuthorizeConnection(mainSessionId: Guid, username: Windows.Win32.Foundation.BSTR, authType: Windows.Win32.System.RemoteDesktop.AAAuthSchemes, clientMachineIP: Windows.Win32.Foundation.BSTR, clientMachineName: Windows.Win32.Foundation.BSTR, sohData: c_char_p_no, numSOHBytes: UInt32, cookieData: c_char_p_no, numCookieBytes: UInt32, userToken: Windows.Win32.Foundation.HANDLE_PTR, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthorizeConnectionSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AuthorizeResource(mainSessionId: Guid, subSessionId: Int32, username: Windows.Win32.Foundation.BSTR, resourceNames: POINTER(Windows.Win32.Foundation.BSTR), numResources: UInt32, alternateResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numAlternateResourceName: UInt32, portNumber: UInt32, operation: Windows.Win32.Foundation.BSTR, cookie: c_char_p_no, numBytesInCookie: UInt32, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthorizeResourceSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsQuarantineEnabled(quarantineEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbBaseNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('808a6537-1282-4989-9e-09-f4-39-38-b7-17-22')
    @commethod(3)
    def OnError(hrError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReportStatus(messageType: Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE, messageID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('18857499-ad61-4b1b-b7-df-cb-cd-41-fb-83-38')
    @commethod(3)
    def get_UserName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Domain(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_InitialProgram(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_LoadBalanceResult(ppVal: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_FarmName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutContext(contextId: Windows.Win32.Foundation.BSTR, context: Windows.Win32.System.Com.VARIANT, existingContext: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContext(contextId: Windows.Win32.Foundation.BSTR, context: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Environment(ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ConnectionError() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SamUserAccount(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClientConnectionPropertySet(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbClientConnectionPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsFirstAssignment(ppVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RdFarmType(pRdFarmType: POINTER(Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserSidString(pszUserSidString: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDisconnectedSession(ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnectionPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('e51995b0-46d6-11dd-aa-21-ce-dc-55-d8-95-93')
class ITsSbEnvironment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8c87f7f7-bf51-4a5c-87-bf-8e-94-fb-6e-22-56')
    @commethod(3)
    def get_Name(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ServerWeight(pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EnvironmentPropertySet(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_EnvironmentPropertySet(pVal: Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbEnvironmentPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('d0d1bf7e-7acf-11dd-a2-43-e5-11-56-d8-95-93')
class ITsSbFilterPluginStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85b44b0f-ed78-413f-97-02-fa-6d-3b-5e-e7-55')
    @commethod(3)
    def SaveProperties(pPropertySet: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateProperties(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteProperties(propertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbGenericNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4c4c8c4f-300b-46ad-91-64-84-68-a7-e7-56-8c')
    @commethod(3)
    def OnCompleted(Status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWaitTimeout(pftTimeout: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbGlobalStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ab60f7b-bd72-4d9f-8a-3a-a0-ea-55-74-e6-35')
    @commethod(3)
    def QueryTarget(ProviderName: Windows.Win32.Foundation.BSTR, TargetName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(ProviderName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32, TargetName: Windows.Win32.Foundation.BSTR, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateFarms(ProviderName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateTargets(ProviderName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, EnvName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateEnvironmentsByProvider(ProviderName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumerateSessions(ProviderName: Windows.Win32.Foundation.BSTR, targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, pSessionState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFarmProperty(farmName: Windows.Win32.Foundation.BSTR, propertyName: Windows.Win32.Foundation.BSTR, pVarValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalanceResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('24fdb7ac-fea6-11dc-96-72-9a-89-56-d8-95-93')
    @commethod(3)
    def get_TargetName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancing(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('24329274-9eb7-11dc-ae-98-f2-b4-56-d8-95-93')
    @commethod(5)
    def GetMostSuitableTarget(pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pLBSink: Windows.Win32.System.RemoteDesktop.ITsSbLoadBalancingNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancingNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('5f8a8297-3244-4e6a-95-8a-27-c8-22-c1-e1-41')
    @commethod(5)
    def OnGetMostSuitableTarget(pLBResult: Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head, fIsNewConnection: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestration(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('64fc1172-9eb7-11dc-8b-00-3a-ba-56-d8-95-93')
    @commethod(5)
    def PrepareTargetForConnect(pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pOrchestrationNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbOrchestrationNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestrationNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('36c37d61-926b-442f-bc-a5-11-8c-6d-50-dc-f2')
    @commethod(5)
    def OnReadyToConnect(pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacement(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('daadee5f-6d32-480e-9e-36-dd-ab-23-29-f0-6d')
    @commethod(5)
    def QueryEnvironmentForTarget(pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pPlacementSink: Windows.Win32.System.RemoteDesktop.ITsSbPlacementNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacementNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('68a0c487-2b4f-46c2-94-a1-6c-e6-85-18-36-34')
    @commethod(5)
    def OnQueryEnvironmentCompleted(pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('48cd7406-caab-465f-a5-d6-ba-a8-63-b9-ea-4f')
    @commethod(3)
    def Initialize(pProvider: Windows.Win32.System.RemoteDesktop.ITsSbProvider_head, pNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbPluginNotifySink_head, pPropertySet: Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('44dfe30b-c3be-40f5-bf-82-7a-95-bb-79-5a-df')
    @commethod(5)
    def OnInitialized(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTerminated() -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPluginPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('95006e34-7eff-4b6c-bb-40-49-a4-fd-a7-ce-a6')
class ITsSbPropertySet(c_void_p):
    extends: Windows.Win32.System.Com.StructuredStorage.IPropertyBag
    Guid = Guid('5c025171-bb1e-4baf-a2-12-6d-5e-97-74-b3-3b')
class ITsSbProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('87a4098f-6d7b-44dd-bc-17-8c-e4-4e-37-0d-52')
    @commethod(3)
    def CreateTargetObject(TargetName: Windows.Win32.Foundation.BSTR, EnvironmentName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateLoadBalanceResultObject(TargetName: Windows.Win32.Foundation.BSTR, ppLBResult: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateSessionObject(TargetName: Windows.Win32.Foundation.BSTR, UserName: Windows.Win32.Foundation.BSTR, Domain: Windows.Win32.Foundation.BSTR, SessionId: UInt32, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreatePluginPropertySet(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateTargetPropertySetObject(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEnvironmentObject(Name: Windows.Win32.Foundation.BSTR, ServerWeight: UInt32, ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetResourcePluginStore(ppStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbResourcePluginStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilterPluginStore(ppStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbFilterPluginStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterForNotification(notificationType: UInt32, ResourceToMonitor: Windows.Win32.Foundation.BSTR, pPluginNotification: Windows.Win32.System.RemoteDesktop.ITsSbResourceNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnRegisterForNotification(notificationType: UInt32, ResourceToMonitor: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceOfGlobalStore(ppGlobalStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbGlobalStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateEnvironmentPropertySetObject(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioning(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('2f6f0dbb-9e4f-462b-9c-3f-fc-cc-3d-cb-62-32')
    @commethod(5)
    def CreateVirtualMachines(JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PatchVirtualMachines(JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head, pVMPatchInfo: POINTER(Windows.Win32.System.RemoteDesktop.VM_PATCH_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteVirtualMachines(JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelJob(JobGuid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioningPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('aca87a8e-818b-4581-a0-32-49-c3-df-b9-c7-01')
    @commethod(3)
    def OnJobCreated(pVmNotifyInfo: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnVirtualMachineStatusChanged(pVmNotifyEntry: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head), VmNotifyStatus: Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS, ErrorCode: Windows.Win32.Foundation.HRESULT, ErrorDescr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnJobCompleted(ResultCode: Windows.Win32.Foundation.HRESULT, ResultDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnJobCancelled() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockVirtualMachine(pVmNotifyEntry: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnVirtualMachineHostStatusChanged(VmHost: Windows.Win32.Foundation.BSTR, VmHostNotifyStatus: Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS, ErrorCode: Windows.Win32.Foundation.HRESULT, ErrorDescr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('65d3e85a-c39b-11dc-b9-2d-3c-d2-55-d8-95-93')
    @commethod(3)
    def NotifySessionChange(changeType: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE, pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChange(TargetChangeType: UInt32, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChange(ChangeType: Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION, pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotificationEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8a47fde-ca91-44d2-b8-97-3a-a2-8a-43-b2-b7')
    @commethod(3)
    def NotifySessionChangeEx(targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, domain: Windows.Win32.Foundation.BSTR, sessionId: UInt32, sessionState: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChangeEx(targetName: Windows.Win32.Foundation.BSTR, targetChangeType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChangeEx(userName: Windows.Win32.Foundation.BSTR, domain: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, targetName: Windows.Win32.Foundation.BSTR, connectionChangeType: Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourcePlugin(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('ea8db42c-98ed-4535-a8-8b-2a-16-4f-35-49-0f')
class ITsSbResourcePluginStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5c38f65f-bcf1-4036-a6-bf-9e-3c-cc-ae-0b-63')
    @commethod(3)
    def QueryTarget(TargetName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(dwSessionId: UInt32, TargetName: Windows.Win32.Foundation.BSTR, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddTargetToStore(pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddSessionToStore(pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddEnvironmentToStore(pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveEnvironmentFromStore(EnvironmentName: Windows.Win32.Foundation.BSTR, bIgnoreOwner: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateFarms(pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryEnvironment(EnvironmentName: Windows.Win32.Foundation.BSTR, ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumerateEnvironments(pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveTarget(pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head, bForceWrite: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveEnvironment(pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head, bForceWrite: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SaveSession(pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetTargetProperty(TargetName: Windows.Win32.Foundation.BSTR, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEnvironmentProperty(EnvironmentName: Windows.Win32.Foundation.BSTR, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTargetState(targetName: Windows.Win32.Foundation.BSTR, newState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, pOldState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetSessionState(sbSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnumerateTargets(FarmName: Windows.Win32.Foundation.BSTR, EnvName: Windows.Win32.Foundation.BSTR, sortByFieldId: Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY, sortyByPropName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnumerateSessions(targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, pSessionState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFarmProperty(farmName: Windows.Win32.Foundation.BSTR, propertyName: Windows.Win32.Foundation.BSTR, pVarValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteTarget(targetName: Windows.Win32.Foundation.BSTR, hostName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetTargetPropertyWithVersionCheck(pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetEnvironmentPropertyWithVersionCheck(pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AcquireTargetLock(targetName: Windows.Win32.Foundation.BSTR, dwTimeout: UInt32, ppContext: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ReleaseTargetLock(pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def TestAndSetServerState(PoolName: Windows.Win32.Foundation.BSTR, ServerFQDN: Windows.Win32.Foundation.BSTR, NewState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, TestState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, pInitState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetServerWaitingToStart(PoolName: Windows.Win32.Foundation.BSTR, serverName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetServerState(PoolName: Windows.Win32.Foundation.BSTR, ServerFQDN: Windows.Win32.Foundation.BSTR, pState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetServerDrainMode(ServerFQDN: Windows.Win32.Foundation.BSTR, DrainMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbServiceNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('86cb68ae-86e0-4f57-8a-64-bb-74-06-bc-55-50')
    @commethod(3)
    def NotifyServiceFailure() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceSuccess() -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbSession(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d453aac7-b1d8-4c5e-ba-34-9a-fb-4c-8c-55-10')
    @commethod(3)
    def get_SessionId(pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TargetName(targetName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_TargetName(targetName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Username(userName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Domain(domain: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(pState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(State: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CreateTime(pTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_CreateTime(Time: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DisconnectTime(pTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DisconnectTime(Time: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InitialProgram(app: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_InitialProgram(Application: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ClientDisplay(pClientDisplay: POINTER(Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ClientDisplay(pClientDisplay: Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ProtocolType(pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ProtocolType(Val: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('16616ecc-272d-411d-b3-24-12-68-93-03-38-56')
    @commethod(3)
    def get_TargetName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TargetName(Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_FarmName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_FarmName(Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_TargetFQDN(TargetFqdnName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TargetFQDN(Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TargetNetbios(TargetNetbiosName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TargetNetbios(Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddresses(SOCKADDR: POINTER(Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint_head), numAddresses: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddresses(SOCKADDR: POINTER(Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint_head), numAddresses: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TargetState(pState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_TargetState(State: Windows.Win32.System.RemoteDesktop.TARGET_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TargetPropertySet(ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_TargetPropertySet(pVal: Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EnvironmentName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_EnvironmentName(Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_NumSessions(pNumSessions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_NumPendingConnections(pNumPendingConnections: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TargetLoad(pTargetLoad: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTargetPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('f7bda5d6-994c-4e11-a0-79-27-63-b6-18-30-ac')
class ITsSbTaskInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('523d1083-89be-48dd-99-ea-04-e8-2f-fa-72-65')
    @commethod(3)
    def get_TargetId(pName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StartTime(pStartTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EndTime(pEndTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Deadline(pDeadline: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Identifier(pIdentifier: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Label(pLabel: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Context(pContext: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Plugin(pPlugin: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(pStatus: POINTER(Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPlugin(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('fa22ef0f-8705-41be-93-bc-44-bd-bc-f1-c9-c4')
    @commethod(5)
    def InitializeTaskPlugin(pITsSbTaskPluginNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbTaskPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTaskQueue(pszHostName: Windows.Win32.Foundation.BSTR, SbTaskInfoSize: UInt32, pITsSbTaskInfo: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTaskInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('6aaf899e-c2ec-45ee-aa-37-45-e6-08-95-26-1a')
    @commethod(5)
    def OnSetTaskTime(szTargetName: Windows.Win32.Foundation.BSTR, TaskStartTime: Windows.Win32.Foundation.FILETIME, TaskEndTime: Windows.Win32.Foundation.FILETIME, TaskDeadline: Windows.Win32.Foundation.FILETIME, szTaskLabel: Windows.Win32.Foundation.BSTR, szTaskIdentifier: Windows.Win32.Foundation.BSTR, szTaskPlugin: Windows.Win32.Foundation.BSTR, dwTaskStatus: UInt32, saContext: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDeleteTaskTime(szTargetName: Windows.Win32.Foundation.BSTR, szTaskIdentifier: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUpdateTaskStatus(szTargetName: Windows.Win32.Foundation.BSTR, TaskIdentifier: Windows.Win32.Foundation.BSTR, TaskStatus: Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnReportTasks(szHostName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsEnhancedFastReconnectArbitrator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5718ae9b-47f2-499f-b6-34-d8-17-5b-d5-11-31')
    @commethod(3)
    def GetSessionForEnhancedFastReconnect(pSessionIdArray: POINTER(Int32), dwSessionCount: UInt32, pResultSessionId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('684b7a0b-edff-43ad-d5-a2-4a-8d-53-88-f4-01')
    @commethod(3)
    def Write(cbSize: UInt32, pBuffer: c_char_p_no, pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Open(pChannelEvents: Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannelEvents_head, pOpenContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('67f2368c-d674-4fae-66-a5-d2-06-28-a6-40-d2')
    @commethod(3)
    def OnDataReceived(cbSize: UInt32, pBuffer: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChannelOpened(OpenResult: Windows.Win32.Foundation.HRESULT, pOpenContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDataSent(pWriteContext: Windows.Win32.System.Com.IUnknown_head, bCancelled: Windows.Win32.Foundation.BOOL, pBuffer: c_char_p_no, cbBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnMetricsUpdate(bandwidth: UInt32, RTT: UInt32, lastSentByteIndex: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0fd57159-e83e-476a-a8-b9-4a-79-76-e7-1e-18')
    @commethod(3)
    def CreateChannel(pszChannelName: c_char_p_no, channelType: Windows.Win32.System.RemoteDesktop.WRdsGraphicsChannelType, ppVirtualChannel: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('324ed94f-fdaf-4ff6-81-a8-42-ab-e7-55-83-0b')
    @commethod(3)
    def GetLogonErrorRedirector(ppLogonErrorRedir: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolLogonErrorRedirector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AcceptConnection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClientData(pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientMonitorData(pNumMonitors: POINTER(UInt32), pPrimaryMonitor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(pUserCreds: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(ppLicenseConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolLicenseConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), SessionHandle: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputHandles(pKeyboardHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetVideoHandle(pVideoHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConnectNotify(SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUserAllowedToLogon(SessionId: UInt32, UserToken: Windows.Win32.Foundation.HANDLE_PTR, pDomainName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SessionArbitrationEnumeration(hUserToken: Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LogonNotify(hClientToken: Windows.Win32.Foundation.HANDLE_PTR, wszUserName: Windows.Win32.Foundation.PWSTR, wszDomainName: Windows.Win32.Foundation.PWSTR, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PreDisconnect(DisconnectReason: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisconnectNotify() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetProtocolStatus(pProtocolStatus: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetLastInputTime(pLastInputTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetErrorInfo(ulError: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(szEndpointName: Windows.Win32.Foundation.PSTR, bStatic: Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(ppShadowConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyCommandProcessCreated(SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1d70332-d070-4ef1-a0-88-78-31-35-36-c2-d6')
    @commethod(3)
    def OnReady() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(Reason: UInt32, Source: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(rect: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionId(pConnectionId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('83fcf5d3-f6f4-ea94-9c-d2-32-f2-80-e1-e5-10')
    @commethod(3)
    def SetConnectionSetting(PropertyID: Guid, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionSetting(PropertyID: Guid, pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLicenseConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1d6a145f-d095-4424-95-7a-40-7f-ae-82-2d-84')
    @commethod(3)
    def RequestLicensingCapabilities(ppLicenseCapabilities: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head), pcbLicenseCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(pClientLicense: c_char_p_no, cbClientLicense: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(Reserve1: c_char_p_no, Reserve2: UInt32, ppClientLicense: c_char_p_no, pcbClientLicense: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(ulComplete: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fcbc131b-c686-451d-a7-73-e2-79-e2-30-f5-40')
    @commethod(3)
    def GetSettings(WRdsListenerSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL, pWRdsListenerSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartListen(pCallback: Windows.Win32.System.RemoteDesktop.IWRdsProtocolListenerCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopListen() -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3ab27e5b-4449-4dc1-b7-4a-91-62-1d-4f-e9-84')
    @commethod(3)
    def OnConnected(pConnection: Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnection_head, pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head), pCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnectionCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLogonErrorRedirector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('519fe83b-142a-4120-a3-d5-a4-05-d3-15-28-1a')
    @commethod(3)
    def OnBeginPainting() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(pszMessage: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dc796967-3abb-40cd-a4-46-10-52-76-b5-89-50')
    @commethod(3)
    def Initialize(pIWRdsSettings: Windows.Win32.System.RemoteDesktop.IWRdsProtocolSettings_head, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateListener(wszListenerName: Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyServiceStateChange(pTSServiceStateChange: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStart(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionOfServiceStop(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifySessionStateChange(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), EventId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NotifySettingsChange(pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Uninitialize() -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('654a5a6a-2550-47eb-b6-f7-eb-d6-37-47-52-65')
    @commethod(3)
    def GetSettings(WRdsSettingType: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE, WRdsSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MergeSettings(pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head), WRdsConnectionSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL, pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e0667ce0-0372-40d6-ad-b2-a0-f3-32-26-74-d6')
    @commethod(3)
    def StopShadow() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: c_char_p_no, Param1Size: UInt32, pParam2: c_char_p_no, Param2Size: UInt32, pParam3: c_char_p_no, Param3Size: UInt32, pParam4: c_char_p_no, Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ae85ce6-cade-4548-8f-eb-99-01-65-97-f6-0a')
    @commethod(3)
    def Start(pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(pParam1: c_char_p_no, Param1Size: UInt32, pParam2: c_char_p_no, Param2Size: UInt32, pParam3: c_char_p_no, Param3Size: UInt32, pParam4: c_char_p_no, Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsWddmIddProps(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1382df4d-a289-43d1-a1-84-14-47-26-f9-af-90')
    @commethod(3)
    def GetHardwareId(pDisplayDriverHardwareId: Windows.Win32.Foundation.PWSTR, Count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDriverLoad(SessionId: UInt32, DriverHandle: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDriverUnload(SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableWddmIdd(Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ea326091-05fe-40c1-b4-9c-3d-2e-f4-62-6a-0e')
    @commethod(3)
    def GetMappedRenderer(mappingId: UInt64, pMappedRendererCallback: Windows.Win32.System.RemoteDesktop.IWTSBitmapRendererCallback_head, ppMappedRenderer: POINTER(Windows.Win32.System.RemoteDesktop.IWTSBitmapRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b7acc97-f3c9-46f7-8c-5b-fa-68-5d-34-41-b1')
    @commethod(3)
    def Render(imageFormat: Guid, dwWidth: UInt32, dwHeight: UInt32, cbStride: Int32, cbImageBuffer: UInt32, pImageBuffer: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRendererStatistics(pStatistics: POINTER(Windows.Win32.System.RemoteDesktop.BITMAP_RENDERER_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveMapping() -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRendererCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d782928e-fe4e-4e77-ae-90-9c-d0-b3-e3-b3-53')
    @commethod(3)
    def OnTargetSizeChanged(rcNewSize: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230206-9a39-4d58-86-74-cd-b4-df-f4-e7-3b')
    @commethod(3)
    def GetConfiguration(ppPropertyBag: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230203-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def OnNewChannelConnection(pChannel: Windows.Win32.System.RemoteDesktop.IWTSVirtualChannel_head, data: Windows.Win32.Foundation.BSTR, pbAccept: POINTER(Windows.Win32.Foundation.BOOL), ppCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230201-1439-4e62-a4-14-19-0d-0a-c3-d4-0e')
    @commethod(3)
    def Initialize(pChannelMgr: Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connected() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnected(dwDisconnectCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminated() -> Windows.Win32.Foundation.HRESULT: ...
class IWTSPluginServiceProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d3e07363-087c-476c-86-a7-db-b1-5f-46-dd-b4')
    @commethod(3)
    def GetService(ServiceId: Guid, ppunkObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-9095-4648-98-bf-ef-81-c9-14-03-2d')
    @commethod(3)
    def GetLogonErrorRedirector(ppLogonErrorRedir: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolLogonErrorRedirector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendPolicyData(pPolicyData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AcceptConnection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientData(pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(pUserCreds: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(ppLicenseConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolLicenseConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProtocolHandles(pKeyboardHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pVideoHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ConnectNotify(SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsUserAllowedToLogon(SessionId: UInt32, UserToken: Windows.Win32.Foundation.HANDLE_PTR, pDomainName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SessionArbitrationEnumeration(hUserToken: Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LogonNotify(hClientToken: Windows.Win32.Foundation.HANDLE_PTR, wszUserName: Windows.Win32.Foundation.PWSTR, wszDomainName: Windows.Win32.Foundation.PWSTR, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserData(pPolicyData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA_head), pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DisconnectNotify() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetProtocolStatus(pProtocolStatus: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetLastInputTime(pLastInputTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetErrorInfo(ulError: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SendBeep(Frequency: UInt32, Duration: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(szEndpointName: Windows.Win32.Foundation.PSTR, bStatic: Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(ppShadowConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnectionCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-75eb-41fe-b4-fb-e0-86-24-2a-fa-0f')
    @commethod(3)
    def OnReady() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(Reason: UInt32, Source: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(rect: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DisplayIOCtl(DisplayIOCtl: POINTER(Windows.Win32.System.RemoteDesktop.WTS_DISPLAY_IOCTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLicenseConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-178c-4079-8e-4a-fe-a6-49-6a-4d-70')
    @commethod(3)
    def RequestLicensingCapabilities(ppLicenseCapabilities: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head), pcbLicenseCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(pClientLicense: c_char_p_no, cbClientLicense: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(Reserve1: c_char_p_no, Reserve2: UInt32, ppClientLicense: c_char_p_no, pcbClientLicense: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(ulComplete: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-45f0-4394-8f-69-32-b2-bc-0e-f4-ca')
    @commethod(3)
    def StartListen(pCallback: Windows.Win32.System.RemoteDesktop.IWTSProtocolListenerCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopListen() -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-1a2d-4de2-97-de-4a-35-f2-60-f0-b3')
    @commethod(3)
    def OnConnected(pConnection: Windows.Win32.System.RemoteDesktop.IWTSProtocolConnection_head, pCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolConnectionCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLogonErrorRedirector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd9b61a7-2916-4627-8d-ee-43-28-71-1a-d6-cb')
    @commethod(3)
    def OnBeginPainting() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(pszMessage: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9eaf6cc-ed79-4f01-82-1d-1f-88-1b-9f-66-cc')
    @commethod(3)
    def CreateListener(wszListenerName: Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceStateChange(pTSServiceStateChange: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifySessionOfServiceStart(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStop(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionStateChange(SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), EventId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('503a2504-aae5-4ab1-93-e0-6d-1c-4b-c6-f7-1a')
    @commethod(3)
    def StopShadow() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: c_char_p_no, Param1Size: UInt32, pParam2: c_char_p_no, Param2Size: UInt32, pParam3: c_char_p_no, Param3Size: UInt32, pParam4: c_char_p_no, Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ee3b0c14-37fb-456b-ba-b3-6d-6c-d5-1e-13-bf')
    @commethod(3)
    def Start(pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(pParam1: c_char_p_no, Param1Size: UInt32, pParam2: c_char_p_no, Param2Size: UInt32, pParam3: c_char_p_no, Param3Size: UInt32, pParam4: c_char_p_no, Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSSBPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dc44be78-b18d-4399-b2-10-64-1b-f6-7a-00-2c')
    @commethod(3)
    def Initialize(PluginCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WTSSBX_MachineChangeNotification(NotificationType: Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, pMachineInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WTSSBX_SessionChangeNotification(NotificationType: Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, NumOfSessions: UInt32, SessionInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WTSSBX_GetMostSuitableServer(UserName: Windows.Win32.Foundation.PWSTR, DomainName: Windows.Win32.Foundation.PWSTR, ApplicationType: Windows.Win32.Foundation.PWSTR, FarmName: Windows.Win32.Foundation.PWSTR, pMachineId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Terminated() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WTSSBX_GetUserExternalSession(UserName: Windows.Win32.Foundation.PWSTR, DomainName: Windows.Win32.Foundation.PWSTR, ApplicationType: Windows.Win32.Foundation.PWSTR, RedirectorInternalIP: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS_head), pSessionId: POINTER(UInt32), pMachineConnectInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230207-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def Write(cbSize: UInt32, pBuffer: c_char_p_no, pReserved: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230204-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def OnDataReceived(cbSize: UInt32, pBuffer: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose() -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230205-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def CreateListener(pszChannelName: Windows.Win32.Foundation.PSTR, uFlags: UInt32, pListenerCallback: Windows.Win32.System.RemoteDesktop.IWTSListenerCallback_head, ppListener: POINTER(Windows.Win32.System.RemoteDesktop.IWTSListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b922bbb8-4c55-4fea-84-96-be-b0-b4-42-85-e5')
    @commethod(3)
    def GetWorkspaceNames(psaWkspNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartRemoteApplication(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, psaParams: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProcessId(pulProcessId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspace
    Guid = Guid('96d8d7cf-783e-4286-83-4c-eb-c0-e9-5f-78-3c')
    @commethod(6)
    def StartRemoteApplicationEx(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrRequestingAppId: Windows.Win32.Foundation.BSTR, bstrRequestingAppFamilyName: Windows.Win32.Foundation.BSTR, bLaunchIntoImmersiveClient: Windows.Win32.Foundation.VARIANT_BOOL, bstrImmersiveClientActivationContext: Windows.Win32.Foundation.BSTR, psaParams: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace3(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspace2
    Guid = Guid('1becbe4a-d654-423b-af-eb-be-8d-53-2c-13-c6')
    @commethod(7)
    def GetClaimsToken2(bstrClaimsHint: Windows.Win32.Foundation.BSTR, bstrUserHint: Windows.Win32.Foundation.BSTR, claimCookie: UInt32, hwndCredUiParent: UInt32, rectCredUiParent: Windows.Win32.Foundation.RECT, pbstrAccessToken: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetClaimsToken(bstrAccessToken: Windows.Win32.Foundation.BSTR, ullAccessTokenExpiration: UInt64, bstrRefreshToken: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceClientExt(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12b952f4-41ca-4f21-a8-29-a6-d0-7d-9a-16-e5')
    @commethod(3)
    def GetResourceId(bstrWorkspaceId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResourceDisplayName(bstrWorkspaceDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IssueDisconnect() -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b922bbb8-4c55-4fea-84-96-be-b0-b4-42-85-e6')
    @commethod(3)
    def AddResource(pUnk: Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveResource(dwCookieConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceRegistration
    Guid = Guid('cf59f654-39bb-44d8-94-d0-46-35-72-89-57-e9')
    @commethod(5)
    def AddResourceEx(pUnk: Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt_head, bstrEventLogUploadAddress: Windows.Win32.Foundation.BSTR, pdwCookie: POINTER(UInt32), correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveResourceEx(dwCookieConnection: UInt32, correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceReportMessage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a7c06739-500f-4e8c-99-a8-2b-d6-95-58-99-eb')
    @commethod(3)
    def RegisterErrorLogMessage(bstrMessage: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsErrorMessageRegistered(bstrWkspId: Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32, pfErrorExist: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterErrorEvent(bstrWkspId: Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceResTypeRegistry(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('1d428c79-6e2e-4351-a3-61-c0-40-1a-03-a0-ba')
    @commethod(7)
    def AddResourceType(fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, bstrLauncher: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteResourceType(fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRegisteredFileExtensions(fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, psaFileExtensions: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResourceTypeInfo(fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, pbstrLauncher: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ModifyResourceType(fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, bstrLauncher: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('efea49a2-dda5-429d-8f-42-b2-3b-92-c4-c3-47')
    @commethod(7)
    def DisconnectWorkspace(bstrWorkspaceId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartWorkspace(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsWorkspaceCredentialSpecified(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bCountUnauthenticatedCredentials: Windows.Win32.Foundation.VARIANT_BOOL, pbCredExist: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsWorkspaceSSOEnabled(pbSSOEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearWorkspaceCredential(bstrWorkspaceId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnAuthenticated(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DisconnectWorkspaceByFriendlyName(bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable
    Guid = Guid('efea49a2-dda5-429d-8f-42-b3-3b-a2-c4-c3-48')
    @commethod(14)
    def StartWorkspaceEx(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR, bstrRedirectorName: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrAppContainer: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ResourceDismissed(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable3(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable2
    Guid = Guid('531e6512-2cbf-4bd2-80-a5-d9-0a-71-63-6a-9a')
    @commethod(16)
    def StartWorkspaceEx2(bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR, bstrRedirectorName: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrAppContainer: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32, bstrEventLogUploadAddress: Windows.Win32.Foundation.BSTR, correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70c04b05-f347-412b-82-2f-36-c9-9c-54-ca-45')
    @commethod(3)
    def GetResourceList(userID: Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.pluginResource_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(alias: Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCacheLastUpdateTime(lastUpdateTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_pluginName(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_pluginVersion(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResolveResource(resourceType: POINTER(UInt32), resourceLocation: Windows.Win32.Foundation.PWSTR, endPointName: Windows.Win32.Foundation.PWSTR, userID: Windows.Win32.Foundation.PWSTR, alias: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ItsPubPlugin
    Guid = Guid('fa4ce418-aad7-4ec6-ba-d1-0a-32-1b-a4-65-d5')
    @commethod(9)
    def GetResource2List(userID: Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResource2(alias: Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResolvePersonalDesktop(userId: Windows.Win32.Foundation.PWSTR, poolId: Windows.Win32.Foundation.PWSTR, ePdResolutionType: Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE, pPdAssignmentType: POINTER(Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE), endPointName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeletePersonalDesktopAssignment(userId: Windows.Win32.Foundation.PWSTR, poolId: Windows.Win32.Foundation.PWSTR, endpointName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
KeyCombinationType = Int32
KeyCombinationType_KeyCombinationHome: KeyCombinationType = 0
KeyCombinationType_KeyCombinationLeft: KeyCombinationType = 1
KeyCombinationType_KeyCombinationUp: KeyCombinationType = 2
KeyCombinationType_KeyCombinationRight: KeyCombinationType = 3
KeyCombinationType_KeyCombinationDown: KeyCombinationType = 4
KeyCombinationType_KeyCombinationScroll: KeyCombinationType = 5
@winfunctype_pointer
def PCHANNEL_INIT_EVENT_FN(pInitHandle: c_void_p, event: UInt32, pData: c_void_p, dataLength: UInt32) -> Void: ...
@winfunctype_pointer
def PCHANNEL_OPEN_EVENT_FN(openHandle: UInt32, event: UInt32, pData: c_void_p, dataLength: UInt32, totalLength: UInt32, dataFlags: UInt32) -> Void: ...
PLUGIN_TYPE = Int32
UNKNOWN_PLUGIN: PLUGIN_TYPE = 0
POLICY_PLUGIN: PLUGIN_TYPE = 1
RESOURCE_PLUGIN: PLUGIN_TYPE = 2
LOAD_BALANCING_PLUGIN: PLUGIN_TYPE = 4
PLACEMENT_PLUGIN: PLUGIN_TYPE = 8
ORCHESTRATION_PLUGIN: PLUGIN_TYPE = 16
PROVISIONING_PLUGIN: PLUGIN_TYPE = 32
TASK_PLUGIN: PLUGIN_TYPE = 64
class PRODUCT_INFOA(Structure):
    CompanyName: Windows.Win32.Foundation.CHAR * 256
    ProductID: Windows.Win32.Foundation.CHAR * 4
class PRODUCT_INFOW(Structure):
    CompanyName: Char * 256
    ProductID: Char * 4
@winfunctype_pointer
def PVIRTUALCHANNELCLOSE(openHandle: UInt32) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELENTRY(pEntryPoints: POINTER(Windows.Win32.System.RemoteDesktop.CHANNEL_ENTRY_POINTS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PVIRTUALCHANNELINIT(ppInitHandle: POINTER(c_void_p), pChannel: POINTER(Windows.Win32.System.RemoteDesktop.CHANNEL_DEF_head), channelCount: Int32, versionRequested: UInt32, pChannelInitEventProc: Windows.Win32.System.RemoteDesktop.PCHANNEL_INIT_EVENT_FN) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELOPEN(pInitHandle: c_void_p, pOpenHandle: POINTER(UInt32), pChannelName: Windows.Win32.Foundation.PSTR, pChannelOpenEventProc: Windows.Win32.System.RemoteDesktop.PCHANNEL_OPEN_EVENT_FN) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELWRITE(openHandle: UInt32, pData: c_void_p, dataLength: UInt32, pUserData: c_void_p) -> UInt32: ...
PasswordEncodingType = Int32
PasswordEncodingType_PasswordEncodingUTF8: PasswordEncodingType = 0
PasswordEncodingType_PasswordEncodingUTF16LE: PasswordEncodingType = 1
PasswordEncodingType_PasswordEncodingUTF16BE: PasswordEncodingType = 2
PolicyAttributeType = Int32
PolicyAttributeType_EnableAllRedirections: PolicyAttributeType = 0
PolicyAttributeType_DisableAllRedirections: PolicyAttributeType = 1
PolicyAttributeType_DriveRedirectionDisabled: PolicyAttributeType = 2
PolicyAttributeType_PrinterRedirectionDisabled: PolicyAttributeType = 3
PolicyAttributeType_PortRedirectionDisabled: PolicyAttributeType = 4
PolicyAttributeType_ClipboardRedirectionDisabled: PolicyAttributeType = 5
PolicyAttributeType_PnpRedirectionDisabled: PolicyAttributeType = 6
PolicyAttributeType_AllowOnlySDRServers: PolicyAttributeType = 7
RDV_TASK_STATUS = Int32
RDV_TASK_STATUS_UNKNOWN: RDV_TASK_STATUS = 0
RDV_TASK_STATUS_SEARCHING: RDV_TASK_STATUS = 1
RDV_TASK_STATUS_DOWNLOADING: RDV_TASK_STATUS = 2
RDV_TASK_STATUS_APPLYING: RDV_TASK_STATUS = 3
RDV_TASK_STATUS_REBOOTING: RDV_TASK_STATUS = 4
RDV_TASK_STATUS_REBOOTED: RDV_TASK_STATUS = 5
RDV_TASK_STATUS_SUCCESS: RDV_TASK_STATUS = 6
RDV_TASK_STATUS_FAILED: RDV_TASK_STATUS = 7
RDV_TASK_STATUS_TIMEOUT: RDV_TASK_STATUS = 8
RD_FARM_TYPE = Int32
RD_FARM_RDSH: RD_FARM_TYPE = 0
RD_FARM_TEMP_VM: RD_FARM_TYPE = 1
RD_FARM_MANUAL_PERSONAL_VM: RD_FARM_TYPE = 2
RD_FARM_AUTO_PERSONAL_VM: RD_FARM_TYPE = 3
RD_FARM_MANUAL_PERSONAL_RDSH: RD_FARM_TYPE = 4
RD_FARM_AUTO_PERSONAL_RDSH: RD_FARM_TYPE = 5
RD_FARM_TYPE_UNKNOWN: RD_FARM_TYPE = -1
class RFX_GFX_MONITOR_INFO(Structure):
    left: Int32
    top: Int32
    right: Int32
    bottom: Int32
    physicalWidth: UInt32
    physicalHeight: UInt32
    orientation: UInt32
    primary: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    reserved: UInt32
    monitorCount: UInt32
    MonitorData: Windows.Win32.System.RemoteDesktop.RFX_GFX_MONITOR_INFO * 16
    clientUniqueId: Char * 32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    ulBpp: UInt32
    Reserved: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_INPUT_RESET(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_RESEND_REQUEST(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    RedrawRect: Windows.Win32.System.RemoteDesktop.RFX_GFX_RECT
class RFX_GFX_MSG_DISCONNECT_NOTIFY(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    DisconnectReason: UInt32
    _pack_ = 1
class RFX_GFX_MSG_HEADER(Structure):
    uMSGType: UInt16
    cbSize: UInt16
    _pack_ = 1
class RFX_GFX_MSG_RDP_DATA(Structure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    rdpData: Byte * 1
class RFX_GFX_RECT(Structure):
    left: Int32
    top: Int32
    right: Int32
    bottom: Int32
    _pack_ = 1
RemoteActionType = Int32
RemoteActionType_RemoteActionCharms: RemoteActionType = 0
RemoteActionType_RemoteActionAppbar: RemoteActionType = 1
RemoteActionType_RemoteActionSnap: RemoteActionType = 2
RemoteActionType_RemoteActionStartScreen: RemoteActionType = 3
RemoteActionType_RemoteActionAppSwitch: RemoteActionType = 4
SESSION_TIMEOUT_ACTION_TYPE = Int32
SESSION_TIMEOUT_ACTION_DISCONNECT: SESSION_TIMEOUT_ACTION_TYPE = 0
SESSION_TIMEOUT_ACTION_SILENT_REAUTH: SESSION_TIMEOUT_ACTION_TYPE = 1
SnapshotEncodingType = Int32
SnapshotEncodingType_SnapshotEncodingDataUri: SnapshotEncodingType = 0
SnapshotFormatType = Int32
SnapshotFormatType_SnapshotFormatPng: SnapshotFormatType = 0
SnapshotFormatType_SnapshotFormatJpeg: SnapshotFormatType = 1
SnapshotFormatType_SnapshotFormatBmp: SnapshotFormatType = 2
TARGET_CHANGE_TYPE = Int32
TARGET_CHANGE_UNSPEC: TARGET_CHANGE_TYPE = 1
TARGET_EXTERNALIP_CHANGED: TARGET_CHANGE_TYPE = 2
TARGET_INTERNALIP_CHANGED: TARGET_CHANGE_TYPE = 4
TARGET_JOINED: TARGET_CHANGE_TYPE = 8
TARGET_REMOVED: TARGET_CHANGE_TYPE = 16
TARGET_STATE_CHANGED: TARGET_CHANGE_TYPE = 32
TARGET_IDLE: TARGET_CHANGE_TYPE = 64
TARGET_PENDING: TARGET_CHANGE_TYPE = 128
TARGET_INUSE: TARGET_CHANGE_TYPE = 256
TARGET_PATCH_STATE_CHANGED: TARGET_CHANGE_TYPE = 512
TARGET_FARM_MEMBERSHIP_CHANGED: TARGET_CHANGE_TYPE = 1024
TARGET_OWNER = Int32
OWNER_UNKNOWN: TARGET_OWNER = 0
OWNER_MS_TS_PLUGIN: TARGET_OWNER = 1
OWNER_MS_VM_PLUGIN: TARGET_OWNER = 2
TARGET_PATCH_STATE = Int32
TARGET_PATCH_UNKNOWN: TARGET_PATCH_STATE = 0
TARGET_PATCH_NOT_STARTED: TARGET_PATCH_STATE = 1
TARGET_PATCH_IN_PROGRESS: TARGET_PATCH_STATE = 2
TARGET_PATCH_COMPLETED: TARGET_PATCH_STATE = 3
TARGET_PATCH_FAILED: TARGET_PATCH_STATE = 4
TARGET_STATE = Int32
TARGET_UNKNOWN: TARGET_STATE = 1
TARGET_INITIALIZING: TARGET_STATE = 2
TARGET_RUNNING: TARGET_STATE = 3
TARGET_DOWN: TARGET_STATE = 4
TARGET_HIBERNATED: TARGET_STATE = 5
TARGET_CHECKED_OUT: TARGET_STATE = 6
TARGET_STOPPED: TARGET_STATE = 7
TARGET_INVALID: TARGET_STATE = 8
TARGET_STARTING: TARGET_STATE = 9
TARGET_STOPPING: TARGET_STATE = 10
TARGET_MAXSTATE: TARGET_STATE = 11
TARGET_TYPE = Int32
UNKNOWN: TARGET_TYPE = 0
FARM: TARGET_TYPE = 1
NONFARM: TARGET_TYPE = 2
TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = Int32
TSPUB_PLUGIN_PD_ASSIGNMENT_NEW: TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = 0
TSPUB_PLUGIN_PD_ASSIGNMENT_EXISTING: TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = 1
TSPUB_PLUGIN_PD_RESOLUTION_TYPE = Int32
TSPUB_PLUGIN_PD_QUERY_OR_CREATE: TSPUB_PLUGIN_PD_RESOLUTION_TYPE = 0
TSPUB_PLUGIN_PD_QUERY_EXISTING: TSPUB_PLUGIN_PD_RESOLUTION_TYPE = 1
TSSB_NOTIFICATION_TYPE = Int32
TSSB_NOTIFY_INVALID: TSSB_NOTIFICATION_TYPE = 0
TSSB_NOTIFY_TARGET_CHANGE: TSSB_NOTIFICATION_TYPE = 1
TSSB_NOTIFY_SESSION_CHANGE: TSSB_NOTIFICATION_TYPE = 2
TSSB_NOTIFY_CONNECTION_REQUEST_CHANGE: TSSB_NOTIFICATION_TYPE = 4
TSSD_AddrV46Type = Int32
TSSD_ADDR_UNDEFINED: TSSD_AddrV46Type = 0
TSSD_ADDR_IPv4: TSSD_AddrV46Type = 4
TSSD_ADDR_IPv6: TSSD_AddrV46Type = 6
class TSSD_ConnectionPoint(Structure):
    ServerAddressB: Byte * 16
    AddressType: Windows.Win32.System.RemoteDesktop.TSSD_AddrV46Type
    PortNumber: UInt16
    AddressScope: UInt32
TSSESSION_STATE = Int32
STATE_INVALID: TSSESSION_STATE = -1
STATE_ACTIVE: TSSESSION_STATE = 0
STATE_CONNECTED: TSSESSION_STATE = 1
STATE_CONNECTQUERY: TSSESSION_STATE = 2
STATE_SHADOW: TSSESSION_STATE = 3
STATE_DISCONNECTED: TSSESSION_STATE = 4
STATE_IDLE: TSSESSION_STATE = 5
STATE_LISTEN: TSSESSION_STATE = 6
STATE_RESET: TSSESSION_STATE = 7
STATE_DOWN: TSSESSION_STATE = 8
STATE_INIT: TSSESSION_STATE = 9
STATE_MAX: TSSESSION_STATE = 10
TSUserExInterfaces = Guid('0910dd01-df8c-11d1-ae-27-00-c0-4f-a3-58-13')
TS_SB_SORT_BY = Int32
TS_SB_SORT_BY_NONE: TS_SB_SORT_BY = 0
TS_SB_SORT_BY_NAME: TS_SB_SORT_BY = 1
TS_SB_SORT_BY_PROP: TS_SB_SORT_BY = 2
VM_HOST_NOTIFY_STATUS = Int32
VM_HOST_STATUS_INIT_PENDING: VM_HOST_NOTIFY_STATUS = 0
VM_HOST_STATUS_INIT_IN_PROGRESS: VM_HOST_NOTIFY_STATUS = 1
VM_HOST_STATUS_INIT_COMPLETE: VM_HOST_NOTIFY_STATUS = 2
VM_HOST_STATUS_INIT_FAILED: VM_HOST_NOTIFY_STATUS = 3
class VM_NOTIFY_ENTRY(Structure):
    VmName: Char * 128
    VmHost: Char * 128
class VM_NOTIFY_INFO(Structure):
    dwNumEntries: UInt32
    ppVmEntries: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head))
VM_NOTIFY_STATUS = Int32
VM_NOTIFY_STATUS_PENDING: VM_NOTIFY_STATUS = 0
VM_NOTIFY_STATUS_IN_PROGRESS: VM_NOTIFY_STATUS = 1
VM_NOTIFY_STATUS_COMPLETE: VM_NOTIFY_STATUS = 2
VM_NOTIFY_STATUS_FAILED: VM_NOTIFY_STATUS = 3
VM_NOTIFY_STATUS_CANCELED: VM_NOTIFY_STATUS = 4
class VM_PATCH_INFO(Structure):
    dwNumEntries: UInt32
    pVmNames: POINTER(Windows.Win32.Foundation.PWSTR)
class WRDS_CONNECTION_SETTING(Union):
    WRdsConnectionSettings1: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_1
class WRDS_CONNECTION_SETTINGS(Structure):
    WRdsConnectionSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL
    WRdsConnectionSetting: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING
class WRDS_CONNECTION_SETTINGS_1(Structure):
    fInheritInitialProgram: Windows.Win32.Foundation.BOOLEAN
    fInheritColorDepth: Windows.Win32.Foundation.BOOLEAN
    fHideTitleBar: Windows.Win32.Foundation.BOOLEAN
    fInheritAutoLogon: Windows.Win32.Foundation.BOOLEAN
    fMaximizeShell: Windows.Win32.Foundation.BOOLEAN
    fDisablePNP: Windows.Win32.Foundation.BOOLEAN
    fPasswordIsScPin: Windows.Win32.Foundation.BOOLEAN
    fPromptForPassword: Windows.Win32.Foundation.BOOLEAN
    fDisableCpm: Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: Windows.Win32.Foundation.BOOLEAN
    fDisableClip: Windows.Win32.Foundation.BOOLEAN
    fResetBroken: Windows.Win32.Foundation.BOOLEAN
    fDisableEncryption: Windows.Win32.Foundation.BOOLEAN
    fDisableAutoReconnect: Windows.Win32.Foundation.BOOLEAN
    fDisableCtrlAltDel: Windows.Win32.Foundation.BOOLEAN
    fDoubleClickDetect: Windows.Win32.Foundation.BOOLEAN
    fEnableWindowsKey: Windows.Win32.Foundation.BOOLEAN
    fUsingSavedCreds: Windows.Win32.Foundation.BOOLEAN
    fMouse: Windows.Win32.Foundation.BOOLEAN
    fNoAudioPlayback: Windows.Win32.Foundation.BOOLEAN
    fRemoteConsoleAudio: Windows.Win32.Foundation.BOOLEAN
    EncryptionLevel: Byte
    ColorDepth: UInt16
    ProtocolType: UInt16
    HRes: UInt16
    VRes: UInt16
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    KeyboardLayout: UInt32
    MaxConnectionTime: UInt32
    MaxDisconnectionTime: UInt32
    MaxIdleTime: UInt32
    PerformanceFlags: UInt32
    KeyboardType: UInt32
    KeyboardSubType: UInt32
    KeyboardFunctionKey: UInt32
    ActiveInputLocale: UInt32
    SerialNumber: UInt32
    ClientAddressFamily: UInt32
    ClientBuildNumber: UInt32
    ClientSessionId: UInt32
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    UserName: Char * 256
    Domain: Char * 256
    Password: Char * 256
    ProtocolName: Char * 9
    DisplayDriverName: Char * 9
    DisplayDeviceName: Char * 20
    imeFileName: Char * 33
    AudioDriverName: Char * 9
    ClientName: Char * 21
    ClientAddress: Char * 31
    ClientDirectory: Char * 257
    ClientDigProductId: Char * 33
    ClientSockAddress: Windows.Win32.System.RemoteDesktop.WTS_SOCKADDR
    ClientTimeZone: Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
    WRdsListenerSettings: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS
    EventLogActivityId: Guid
    ContextSize: UInt32
    ContextData: c_char_p_no
WRDS_CONNECTION_SETTING_LEVEL = Int32
WRDS_CONNECTION_SETTING_LEVEL_INVALID: WRDS_CONNECTION_SETTING_LEVEL = 0
WRDS_CONNECTION_SETTING_LEVEL_1: WRDS_CONNECTION_SETTING_LEVEL = 1
class WRDS_DYNAMIC_TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    DaylightBias: Int32
    TimeZoneKeyName: Char * 128
    DynamicDaylightTimeDisabled: UInt16
class WRDS_LISTENER_SETTING(Union):
    WRdsListenerSettings1: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_1
class WRDS_LISTENER_SETTINGS(Structure):
    WRdsListenerSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL
    WRdsListenerSetting: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING
class WRDS_LISTENER_SETTINGS_1(Structure):
    MaxProtocolListenerConnectionCount: UInt32
    SecurityDescriptorSize: UInt32
    pSecurityDescriptor: c_char_p_no
WRDS_LISTENER_SETTING_LEVEL = Int32
WRDS_LISTENER_SETTING_LEVEL_INVALID: WRDS_LISTENER_SETTING_LEVEL = 0
WRDS_LISTENER_SETTING_LEVEL_1: WRDS_LISTENER_SETTING_LEVEL = 1
class WRDS_SETTING(Union):
    WRdsSettings1: Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_1
class WRDS_SETTINGS(Structure):
    WRdsSettingType: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE
    WRdsSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL
    WRdsSetting: Windows.Win32.System.RemoteDesktop.WRDS_SETTING
class WRDS_SETTINGS_1(Structure):
    WRdsDisableClipStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableClipValue: UInt32
    WRdsDisableLPTStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableLPTValue: UInt32
    WRdsDisableCcmStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCcmValue: UInt32
    WRdsDisableCdmStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCdmValue: UInt32
    WRdsDisableCpmStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCpmValue: UInt32
    WRdsDisablePnpStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisablePnpValue: UInt32
    WRdsEncryptionLevelStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsEncryptionValue: UInt32
    WRdsColorDepthStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsColorDepthValue: UInt32
    WRdsDisableAutoReconnecetStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableAutoReconnecetValue: UInt32
    WRdsDisableEncryptionStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableEncryptionValue: UInt32
    WRdsResetBrokenStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsResetBrokenValue: UInt32
    WRdsMaxIdleTimeStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxIdleTimeValue: UInt32
    WRdsMaxDisconnectTimeStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxDisconnectTimeValue: UInt32
    WRdsMaxConnectTimeStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxConnectTimeValue: UInt32
    WRdsKeepAliveStatus: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsKeepAliveStartValue: Windows.Win32.Foundation.BOOLEAN
    WRdsKeepAliveIntervalValue: UInt32
WRDS_SETTING_LEVEL = Int32
WRDS_SETTING_LEVEL_INVALID: WRDS_SETTING_LEVEL = 0
WRDS_SETTING_LEVEL_1: WRDS_SETTING_LEVEL = 1
WRDS_SETTING_STATUS = Int32
WRDS_SETTING_STATUS_NOTAPPLICABLE: WRDS_SETTING_STATUS = -1
WRDS_SETTING_STATUS_DISABLED: WRDS_SETTING_STATUS = 0
WRDS_SETTING_STATUS_ENABLED: WRDS_SETTING_STATUS = 1
WRDS_SETTING_STATUS_NOTCONFIGURED: WRDS_SETTING_STATUS = 2
WRDS_SETTING_TYPE = Int32
WRDS_SETTING_TYPE_INVALID: WRDS_SETTING_TYPE = 0
WRDS_SETTING_TYPE_MACHINE: WRDS_SETTING_TYPE = 1
WRDS_SETTING_TYPE_USER: WRDS_SETTING_TYPE = 2
WRDS_SETTING_TYPE_SAM: WRDS_SETTING_TYPE = 3
WRdsGraphicsChannelType = Int32
WRdsGraphicsChannelType_GuaranteedDelivery: WRdsGraphicsChannelType = 0
WRdsGraphicsChannelType_BestEffortDelivery: WRdsGraphicsChannelType = 1
class WTSCLIENTA(Structure):
    ClientName: Windows.Win32.Foundation.CHAR * 21
    Domain: Windows.Win32.Foundation.CHAR * 18
    UserName: Windows.Win32.Foundation.CHAR * 21
    WorkDirectory: Windows.Win32.Foundation.CHAR * 261
    InitialProgram: Windows.Win32.Foundation.CHAR * 261
    EncryptionLevel: Byte
    ClientAddressFamily: UInt32
    ClientAddress: UInt16 * 31
    HRes: UInt16
    VRes: UInt16
    ColorDepth: UInt16
    ClientDirectory: Windows.Win32.Foundation.CHAR * 261
    ClientBuildNumber: UInt32
    ClientHardwareId: UInt32
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    DeviceId: Windows.Win32.Foundation.CHAR * 261
class WTSCLIENTW(Structure):
    ClientName: Char * 21
    Domain: Char * 18
    UserName: Char * 21
    WorkDirectory: Char * 261
    InitialProgram: Char * 261
    EncryptionLevel: Byte
    ClientAddressFamily: UInt32
    ClientAddress: UInt16 * 31
    HRes: UInt16
    VRes: UInt16
    ColorDepth: UInt16
    ClientDirectory: Char * 261
    ClientBuildNumber: UInt32
    ClientHardwareId: UInt32
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    DeviceId: Char * 261
class WTSCONFIGINFOA(Structure):
    version: UInt32
    fConnectClientDrivesAtLogon: UInt32
    fConnectPrinterAtLogon: UInt32
    fDisablePrinterRedirection: UInt32
    fDisableDefaultMainClientPrinter: UInt32
    ShadowSettings: UInt32
    LogonUserName: Windows.Win32.Foundation.CHAR * 21
    LogonDomain: Windows.Win32.Foundation.CHAR * 18
    WorkDirectory: Windows.Win32.Foundation.CHAR * 261
    InitialProgram: Windows.Win32.Foundation.CHAR * 261
    ApplicationName: Windows.Win32.Foundation.CHAR * 261
class WTSCONFIGINFOW(Structure):
    version: UInt32
    fConnectClientDrivesAtLogon: UInt32
    fConnectPrinterAtLogon: UInt32
    fDisablePrinterRedirection: UInt32
    fDisableDefaultMainClientPrinter: UInt32
    ShadowSettings: UInt32
    LogonUserName: Char * 21
    LogonDomain: Char * 18
    WorkDirectory: Char * 261
    InitialProgram: Char * 261
    ApplicationName: Char * 261
class WTSINFOA(Structure):
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBy: UInt32
    WinStationName: Windows.Win32.Foundation.CHAR * 32
    Domain: Windows.Win32.Foundation.CHAR * 17
    UserName: Windows.Win32.Foundation.CHAR * 21
    ConnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    DisconnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastInputTime: Windows.Win32.Foundation.LARGE_INTEGER
    LogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    CurrentTime: Windows.Win32.Foundation.LARGE_INTEGER
class WTSINFOEXA(Structure):
    Level: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_A
class WTSINFOEXW(Structure):
    Level: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_W
class WTSINFOEX_LEVEL1_A(Structure):
    SessionId: UInt32
    SessionState: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionFlags: Int32
    WinStationName: Windows.Win32.Foundation.CHAR * 33
    UserName: Windows.Win32.Foundation.CHAR * 21
    DomainName: Windows.Win32.Foundation.CHAR * 18
    LogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    ConnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    DisconnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastInputTime: Windows.Win32.Foundation.LARGE_INTEGER
    CurrentTime: Windows.Win32.Foundation.LARGE_INTEGER
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBytes: UInt32
class WTSINFOEX_LEVEL1_W(Structure):
    SessionId: UInt32
    SessionState: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionFlags: Int32
    WinStationName: Char * 33
    UserName: Char * 21
    DomainName: Char * 18
    LogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    ConnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    DisconnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastInputTime: Windows.Win32.Foundation.LARGE_INTEGER
    CurrentTime: Windows.Win32.Foundation.LARGE_INTEGER
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBytes: UInt32
class WTSINFOEX_LEVEL_A(Union):
    WTSInfoExLevel1: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_A
class WTSINFOEX_LEVEL_W(Union):
    WTSInfoExLevel1: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_W
class WTSINFOW(Structure):
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBytes: UInt32
    WinStationName: Char * 32
    Domain: Char * 17
    UserName: Char * 21
    ConnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    DisconnectTime: Windows.Win32.Foundation.LARGE_INTEGER
    LastInputTime: Windows.Win32.Foundation.LARGE_INTEGER
    LogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    CurrentTime: Windows.Win32.Foundation.LARGE_INTEGER
class WTSLISTENERCONFIGA(Structure):
    version: UInt32
    fEnableListener: UInt32
    MaxConnectionCount: UInt32
    fPromptForPassword: UInt32
    fInheritColorDepth: UInt32
    ColorDepth: UInt32
    fInheritBrokenTimeoutSettings: UInt32
    BrokenTimeoutSettings: UInt32
    fDisablePrinterRedirection: UInt32
    fDisableDriveRedirection: UInt32
    fDisableComPortRedirection: UInt32
    fDisableLPTPortRedirection: UInt32
    fDisableClipboardRedirection: UInt32
    fDisableAudioRedirection: UInt32
    fDisablePNPRedirection: UInt32
    fDisableDefaultMainClientPrinter: UInt32
    LanAdapter: UInt32
    PortNumber: UInt32
    fInheritShadowSettings: UInt32
    ShadowSettings: UInt32
    TimeoutSettingsConnection: UInt32
    TimeoutSettingsDisconnection: UInt32
    TimeoutSettingsIdle: UInt32
    SecurityLayer: UInt32
    MinEncryptionLevel: UInt32
    UserAuthentication: UInt32
    Comment: Windows.Win32.Foundation.CHAR * 61
    LogonUserName: Windows.Win32.Foundation.CHAR * 21
    LogonDomain: Windows.Win32.Foundation.CHAR * 18
    WorkDirectory: Windows.Win32.Foundation.CHAR * 261
    InitialProgram: Windows.Win32.Foundation.CHAR * 261
class WTSLISTENERCONFIGW(Structure):
    version: UInt32
    fEnableListener: UInt32
    MaxConnectionCount: UInt32
    fPromptForPassword: UInt32
    fInheritColorDepth: UInt32
    ColorDepth: UInt32
    fInheritBrokenTimeoutSettings: UInt32
    BrokenTimeoutSettings: UInt32
    fDisablePrinterRedirection: UInt32
    fDisableDriveRedirection: UInt32
    fDisableComPortRedirection: UInt32
    fDisableLPTPortRedirection: UInt32
    fDisableClipboardRedirection: UInt32
    fDisableAudioRedirection: UInt32
    fDisablePNPRedirection: UInt32
    fDisableDefaultMainClientPrinter: UInt32
    LanAdapter: UInt32
    PortNumber: UInt32
    fInheritShadowSettings: UInt32
    ShadowSettings: UInt32
    TimeoutSettingsConnection: UInt32
    TimeoutSettingsDisconnection: UInt32
    TimeoutSettingsIdle: UInt32
    SecurityLayer: UInt32
    MinEncryptionLevel: UInt32
    UserAuthentication: UInt32
    Comment: Char * 61
    LogonUserName: Char * 21
    LogonDomain: Char * 18
    WorkDirectory: Char * 261
    InitialProgram: Char * 261
WTSSBX_ADDRESS_FAMILY = Int32
WTSSBX_ADDRESS_FAMILY_AF_UNSPEC: WTSSBX_ADDRESS_FAMILY = 0
WTSSBX_ADDRESS_FAMILY_AF_INET: WTSSBX_ADDRESS_FAMILY = 1
WTSSBX_ADDRESS_FAMILY_AF_INET6: WTSSBX_ADDRESS_FAMILY = 2
WTSSBX_ADDRESS_FAMILY_AF_IPX: WTSSBX_ADDRESS_FAMILY = 3
WTSSBX_ADDRESS_FAMILY_AF_NETBIOS: WTSSBX_ADDRESS_FAMILY = 4
class WTSSBX_IP_ADDRESS(Structure):
    AddressFamily: Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY
    Address: Byte * 16
    PortNumber: UInt16
    dwScope: UInt32
class WTSSBX_MACHINE_CONNECT_INFO(Structure):
    wczMachineFQDN: Char * 257
    wczMachineNetBiosName: Char * 17
    dwNumOfIPAddr: UInt32
    IPaddr: Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS * 12
WTSSBX_MACHINE_DRAIN = Int32
WTSSBX_MACHINE_DRAIN_UNSPEC: WTSSBX_MACHINE_DRAIN = 0
WTSSBX_MACHINE_DRAIN_OFF: WTSSBX_MACHINE_DRAIN = 1
WTSSBX_MACHINE_DRAIN_ON: WTSSBX_MACHINE_DRAIN = 2
class WTSSBX_MACHINE_INFO(Structure):
    ClientConnectInfo: Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO
    wczFarmName: Char * 257
    InternalIPAddress: Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS
    dwMaxSessionsLimit: UInt32
    ServerWeight: UInt32
    SingleSessionMode: Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE
    InDrain: Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN
    MachineState: Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_STATE
WTSSBX_MACHINE_SESSION_MODE = Int32
WTSSBX_MACHINE_SESSION_MODE_UNSPEC: WTSSBX_MACHINE_SESSION_MODE = 0
WTSSBX_MACHINE_SESSION_MODE_SINGLE: WTSSBX_MACHINE_SESSION_MODE = 1
WTSSBX_MACHINE_SESSION_MODE_MULTIPLE: WTSSBX_MACHINE_SESSION_MODE = 2
WTSSBX_MACHINE_STATE = Int32
WTSSBX_MACHINE_STATE_UNSPEC: WTSSBX_MACHINE_STATE = 0
WTSSBX_MACHINE_STATE_READY: WTSSBX_MACHINE_STATE = 1
WTSSBX_MACHINE_STATE_SYNCHRONIZING: WTSSBX_MACHINE_STATE = 2
WTSSBX_NOTIFICATION_TYPE = Int32
WTSSBX_NOTIFICATION_REMOVED: WTSSBX_NOTIFICATION_TYPE = 1
WTSSBX_NOTIFICATION_CHANGED: WTSSBX_NOTIFICATION_TYPE = 2
WTSSBX_NOTIFICATION_ADDED: WTSSBX_NOTIFICATION_TYPE = 4
WTSSBX_NOTIFICATION_RESYNC: WTSSBX_NOTIFICATION_TYPE = 8
class WTSSBX_SESSION_INFO(Structure):
    wszUserName: Char * 105
    wszDomainName: Char * 257
    ApplicationType: Char * 257
    dwSessionId: UInt32
    CreateTime: Windows.Win32.Foundation.FILETIME
    DisconnectTime: Windows.Win32.Foundation.FILETIME
    SessionState: Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_STATE
WTSSBX_SESSION_STATE = Int32
WTSSBX_SESSION_STATE_UNSPEC: WTSSBX_SESSION_STATE = 0
WTSSBX_SESSION_STATE_ACTIVE: WTSSBX_SESSION_STATE = 1
WTSSBX_SESSION_STATE_DISCONNECTED: WTSSBX_SESSION_STATE = 2
class WTSSESSION_NOTIFICATION(Structure):
    cbSize: UInt32
    dwSessionId: UInt32
class WTSUSERCONFIGA(Structure):
    Source: UInt32
    InheritInitialProgram: UInt32
    AllowLogonTerminalServer: UInt32
    TimeoutSettingsConnections: UInt32
    TimeoutSettingsDisconnections: UInt32
    TimeoutSettingsIdle: UInt32
    DeviceClientDrives: UInt32
    DeviceClientPrinters: UInt32
    ClientDefaultPrinter: UInt32
    BrokenTimeoutSettings: UInt32
    ReconnectSettings: UInt32
    ShadowingSettings: UInt32
    TerminalServerRemoteHomeDir: UInt32
    InitialProgram: Windows.Win32.Foundation.CHAR * 261
    WorkDirectory: Windows.Win32.Foundation.CHAR * 261
    TerminalServerProfilePath: Windows.Win32.Foundation.CHAR * 261
    TerminalServerHomeDir: Windows.Win32.Foundation.CHAR * 261
    TerminalServerHomeDirDrive: Windows.Win32.Foundation.CHAR * 4
class WTSUSERCONFIGW(Structure):
    Source: UInt32
    InheritInitialProgram: UInt32
    AllowLogonTerminalServer: UInt32
    TimeoutSettingsConnections: UInt32
    TimeoutSettingsDisconnections: UInt32
    TimeoutSettingsIdle: UInt32
    DeviceClientDrives: UInt32
    DeviceClientPrinters: UInt32
    ClientDefaultPrinter: UInt32
    BrokenTimeoutSettings: UInt32
    ReconnectSettings: UInt32
    ShadowingSettings: UInt32
    TerminalServerRemoteHomeDir: UInt32
    InitialProgram: Char * 261
    WorkDirectory: Char * 261
    TerminalServerProfilePath: Char * 261
    TerminalServerHomeDir: Char * 261
    TerminalServerHomeDirDrive: Char * 4
class WTS_CACHE_STATS(Structure):
    Specific: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS_UN
    ProtocolType: UInt16
    Length: UInt16
class WTS_CACHE_STATS_UN(Union):
    ProtocolCache: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_CACHE * 4
    TShareCacheStats: UInt32
    Reserved: UInt32 * 20
WTS_CERT_TYPE = Int32
WTS_CERT_TYPE_INVALID: WTS_CERT_TYPE = 0
WTS_CERT_TYPE_PROPRIETORY: WTS_CERT_TYPE = 1
WTS_CERT_TYPE_X509: WTS_CERT_TYPE = 2
class WTS_CLIENT_ADDRESS(Structure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_CLIENT_DATA(Structure):
    fDisableCtrlAltDel: Windows.Win32.Foundation.BOOLEAN
    fDoubleClickDetect: Windows.Win32.Foundation.BOOLEAN
    fEnableWindowsKey: Windows.Win32.Foundation.BOOLEAN
    fHideTitleBar: Windows.Win32.Foundation.BOOLEAN
    fInheritAutoLogon: Windows.Win32.Foundation.BOOL
    fPromptForPassword: Windows.Win32.Foundation.BOOLEAN
    fUsingSavedCreds: Windows.Win32.Foundation.BOOLEAN
    Domain: Char * 256
    UserName: Char * 256
    Password: Char * 256
    fPasswordIsScPin: Windows.Win32.Foundation.BOOLEAN
    fInheritInitialProgram: Windows.Win32.Foundation.BOOL
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    fMaximizeShell: Windows.Win32.Foundation.BOOLEAN
    EncryptionLevel: Byte
    PerformanceFlags: UInt32
    ProtocolName: Char * 9
    ProtocolType: UInt16
    fInheritColorDepth: Windows.Win32.Foundation.BOOL
    HRes: UInt16
    VRes: UInt16
    ColorDepth: UInt16
    DisplayDriverName: Char * 9
    DisplayDeviceName: Char * 20
    fMouse: Windows.Win32.Foundation.BOOLEAN
    KeyboardLayout: UInt32
    KeyboardType: UInt32
    KeyboardSubType: UInt32
    KeyboardFunctionKey: UInt32
    imeFileName: Char * 33
    ActiveInputLocale: UInt32
    fNoAudioPlayback: Windows.Win32.Foundation.BOOLEAN
    fRemoteConsoleAudio: Windows.Win32.Foundation.BOOLEAN
    AudioDriverName: Char * 9
    ClientTimeZone: Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
    ClientName: Char * 21
    SerialNumber: UInt32
    ClientAddressFamily: UInt32
    ClientAddress: Char * 31
    ClientSockAddress: Windows.Win32.System.RemoteDesktop.WTS_SOCKADDR
    ClientDirectory: Char * 257
    ClientBuildNumber: UInt32
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    ClientSessionId: UInt32
    ClientDigProductId: Char * 33
    fDisableCpm: Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: Windows.Win32.Foundation.BOOLEAN
    fDisableClip: Windows.Win32.Foundation.BOOLEAN
    fDisablePNP: Windows.Win32.Foundation.BOOLEAN
class WTS_CLIENT_DISPLAY(Structure):
    HorizontalResolution: UInt32
    VerticalResolution: UInt32
    ColorDepth: UInt32
WTS_CONFIG_CLASS = Int32
WTS_CONFIG_CLASS_WTSUserConfigInitialProgram: WTS_CONFIG_CLASS = 0
WTS_CONFIG_CLASS_WTSUserConfigWorkingDirectory: WTS_CONFIG_CLASS = 1
WTS_CONFIG_CLASS_WTSUserConfigfInheritInitialProgram: WTS_CONFIG_CLASS = 2
WTS_CONFIG_CLASS_WTSUserConfigfAllowLogonTerminalServer: WTS_CONFIG_CLASS = 3
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsConnections: WTS_CONFIG_CLASS = 4
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsDisconnections: WTS_CONFIG_CLASS = 5
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsIdle: WTS_CONFIG_CLASS = 6
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDrives: WTS_CONFIG_CLASS = 7
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientPrinters: WTS_CONFIG_CLASS = 8
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDefaultPrinter: WTS_CONFIG_CLASS = 9
WTS_CONFIG_CLASS_WTSUserConfigBrokenTimeoutSettings: WTS_CONFIG_CLASS = 10
WTS_CONFIG_CLASS_WTSUserConfigReconnectSettings: WTS_CONFIG_CLASS = 11
WTS_CONFIG_CLASS_WTSUserConfigModemCallbackSettings: WTS_CONFIG_CLASS = 12
WTS_CONFIG_CLASS_WTSUserConfigModemCallbackPhoneNumber: WTS_CONFIG_CLASS = 13
WTS_CONFIG_CLASS_WTSUserConfigShadowingSettings: WTS_CONFIG_CLASS = 14
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerProfilePath: WTS_CONFIG_CLASS = 15
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDir: WTS_CONFIG_CLASS = 16
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDirDrive: WTS_CONFIG_CLASS = 17
WTS_CONFIG_CLASS_WTSUserConfigfTerminalServerRemoteHomeDir: WTS_CONFIG_CLASS = 18
WTS_CONFIG_CLASS_WTSUserConfigUser: WTS_CONFIG_CLASS = 19
WTS_CONFIG_SOURCE = Int32
WTS_CONFIG_SOURCE_WTSUserConfigSourceSAM: WTS_CONFIG_SOURCE = 0
WTS_CONNECTSTATE_CLASS = Int32
WTS_CONNECTSTATE_CLASS_WTSActive: WTS_CONNECTSTATE_CLASS = 0
WTS_CONNECTSTATE_CLASS_WTSConnected: WTS_CONNECTSTATE_CLASS = 1
WTS_CONNECTSTATE_CLASS_WTSConnectQuery: WTS_CONNECTSTATE_CLASS = 2
WTS_CONNECTSTATE_CLASS_WTSShadow: WTS_CONNECTSTATE_CLASS = 3
WTS_CONNECTSTATE_CLASS_WTSDisconnected: WTS_CONNECTSTATE_CLASS = 4
WTS_CONNECTSTATE_CLASS_WTSIdle: WTS_CONNECTSTATE_CLASS = 5
WTS_CONNECTSTATE_CLASS_WTSListen: WTS_CONNECTSTATE_CLASS = 6
WTS_CONNECTSTATE_CLASS_WTSReset: WTS_CONNECTSTATE_CLASS = 7
WTS_CONNECTSTATE_CLASS_WTSDown: WTS_CONNECTSTATE_CLASS = 8
WTS_CONNECTSTATE_CLASS_WTSInit: WTS_CONNECTSTATE_CLASS = 9
class WTS_DISPLAY_IOCTL(Structure):
    pDisplayIOCtlData: Byte * 256
    cbDisplayIOCtlData: UInt32
WTS_INFO_CLASS = Int32
WTS_INFO_CLASS_WTSInitialProgram: WTS_INFO_CLASS = 0
WTS_INFO_CLASS_WTSApplicationName: WTS_INFO_CLASS = 1
WTS_INFO_CLASS_WTSWorkingDirectory: WTS_INFO_CLASS = 2
WTS_INFO_CLASS_WTSOEMId: WTS_INFO_CLASS = 3
WTS_INFO_CLASS_WTSSessionId: WTS_INFO_CLASS = 4
WTS_INFO_CLASS_WTSUserName: WTS_INFO_CLASS = 5
WTS_INFO_CLASS_WTSWinStationName: WTS_INFO_CLASS = 6
WTS_INFO_CLASS_WTSDomainName: WTS_INFO_CLASS = 7
WTS_INFO_CLASS_WTSConnectState: WTS_INFO_CLASS = 8
WTS_INFO_CLASS_WTSClientBuildNumber: WTS_INFO_CLASS = 9
WTS_INFO_CLASS_WTSClientName: WTS_INFO_CLASS = 10
WTS_INFO_CLASS_WTSClientDirectory: WTS_INFO_CLASS = 11
WTS_INFO_CLASS_WTSClientProductId: WTS_INFO_CLASS = 12
WTS_INFO_CLASS_WTSClientHardwareId: WTS_INFO_CLASS = 13
WTS_INFO_CLASS_WTSClientAddress: WTS_INFO_CLASS = 14
WTS_INFO_CLASS_WTSClientDisplay: WTS_INFO_CLASS = 15
WTS_INFO_CLASS_WTSClientProtocolType: WTS_INFO_CLASS = 16
WTS_INFO_CLASS_WTSIdleTime: WTS_INFO_CLASS = 17
WTS_INFO_CLASS_WTSLogonTime: WTS_INFO_CLASS = 18
WTS_INFO_CLASS_WTSIncomingBytes: WTS_INFO_CLASS = 19
WTS_INFO_CLASS_WTSOutgoingBytes: WTS_INFO_CLASS = 20
WTS_INFO_CLASS_WTSIncomingFrames: WTS_INFO_CLASS = 21
WTS_INFO_CLASS_WTSOutgoingFrames: WTS_INFO_CLASS = 22
WTS_INFO_CLASS_WTSClientInfo: WTS_INFO_CLASS = 23
WTS_INFO_CLASS_WTSSessionInfo: WTS_INFO_CLASS = 24
WTS_INFO_CLASS_WTSSessionInfoEx: WTS_INFO_CLASS = 25
WTS_INFO_CLASS_WTSConfigInfo: WTS_INFO_CLASS = 26
WTS_INFO_CLASS_WTSValidationInfo: WTS_INFO_CLASS = 27
WTS_INFO_CLASS_WTSSessionAddressV4: WTS_INFO_CLASS = 28
WTS_INFO_CLASS_WTSIsRemoteSession: WTS_INFO_CLASS = 29
class WTS_LICENSE_CAPABILITIES(Structure):
    KeyExchangeAlg: UInt32
    ProtocolVer: UInt32
    fAuthenticateServer: Windows.Win32.Foundation.BOOL
    CertType: Windows.Win32.System.RemoteDesktop.WTS_CERT_TYPE
    cbClientName: UInt32
    rgbClientName: Byte * 42
WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = Int32
WTS_LOGON_ERR_INVALID: WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 0
WTS_LOGON_ERR_NOT_HANDLED: WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 1
WTS_LOGON_ERR_HANDLED_SHOW: WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 2
WTS_LOGON_ERR_HANDLED_DONT_SHOW: WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 3
WTS_LOGON_ERR_HANDLED_DONT_SHOW_START_OVER: WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 4
class WTS_POLICY_DATA(Structure):
    fDisableEncryption: Windows.Win32.Foundation.BOOLEAN
    fDisableAutoReconnect: Windows.Win32.Foundation.BOOLEAN
    ColorDepth: UInt32
    MinEncryptionLevel: Byte
    fDisableCpm: Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: Windows.Win32.Foundation.BOOLEAN
    fDisableClip: Windows.Win32.Foundation.BOOLEAN
    fDisablePNPRedir: Windows.Win32.Foundation.BOOLEAN
class WTS_PROCESS_INFOA(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PSTR
    pUserSid: Windows.Win32.Foundation.PSID
class WTS_PROCESS_INFOW(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PWSTR
    pUserSid: Windows.Win32.Foundation.PSID
class WTS_PROCESS_INFO_EXA(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PSTR
    pUserSid: Windows.Win32.Foundation.PSID
    NumberOfThreads: UInt32
    HandleCount: UInt32
    PagefileUsage: UInt32
    PeakPagefileUsage: UInt32
    WorkingSetSize: UInt32
    PeakWorkingSetSize: UInt32
    UserTime: Windows.Win32.Foundation.LARGE_INTEGER
    KernelTime: Windows.Win32.Foundation.LARGE_INTEGER
class WTS_PROCESS_INFO_EXW(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PWSTR
    pUserSid: Windows.Win32.Foundation.PSID
    NumberOfThreads: UInt32
    HandleCount: UInt32
    PagefileUsage: UInt32
    PeakPagefileUsage: UInt32
    WorkingSetSize: UInt32
    PeakWorkingSetSize: UInt32
    UserTime: Windows.Win32.Foundation.LARGE_INTEGER
    KernelTime: Windows.Win32.Foundation.LARGE_INTEGER
class WTS_PROPERTY_VALUE(Structure):
    Type: UInt16
    u: _u_e__Union
    class _u_e__Union(Union):
        ulVal: UInt32
        strVal: _strVal_e__Struct
        bVal: _bVal_e__Struct
        guidVal: Guid
        class _strVal_e__Struct(Structure):
            size: UInt32
            pstrVal: Windows.Win32.Foundation.PWSTR
        class _bVal_e__Struct(Structure):
            size: UInt32
            pbVal: Windows.Win32.Foundation.PSTR
class WTS_PROTOCOL_CACHE(Structure):
    CacheReads: UInt32
    CacheHits: UInt32
class WTS_PROTOCOL_COUNTERS(Structure):
    WdBytes: UInt32
    WdFrames: UInt32
    WaitForOutBuf: UInt32
    Frames: UInt32
    Bytes: UInt32
    CompressedBytes: UInt32
    CompressFlushes: UInt32
    Errors: UInt32
    Timeouts: UInt32
    AsyncFramingError: UInt32
    AsyncOverrunError: UInt32
    AsyncOverflowError: UInt32
    AsyncParityError: UInt32
    TdErrors: UInt32
    ProtocolType: UInt16
    Length: UInt16
    Specific: UInt16
    Reserved: UInt32 * 100
class WTS_PROTOCOL_STATUS(Structure):
    Output: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Input: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Cache: Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS
    AsyncSignal: UInt32
    AsyncSignalMask: UInt32
    Counters: Windows.Win32.Foundation.LARGE_INTEGER * 100
WTS_RCM_DRAIN_STATE = Int32
WTS_DRAIN_STATE_NONE: WTS_RCM_DRAIN_STATE = 0
WTS_DRAIN_IN_DRAIN: WTS_RCM_DRAIN_STATE = 1
WTS_DRAIN_NOT_IN_DRAIN: WTS_RCM_DRAIN_STATE = 2
WTS_RCM_SERVICE_STATE = Int32
WTS_SERVICE_NONE: WTS_RCM_SERVICE_STATE = 0
WTS_SERVICE_START: WTS_RCM_SERVICE_STATE = 1
WTS_SERVICE_STOP: WTS_RCM_SERVICE_STATE = 2
WTS_SECURITY_FLAGS = UInt32
WTS_SECURITY_CURRENT_GUEST_ACCESS: WTS_SECURITY_FLAGS = 72
WTS_SECURITY_USER_ACCESS: WTS_SECURITY_FLAGS = 329
WTS_SECURITY_CURRENT_USER_ACCESS: WTS_SECURITY_FLAGS = 590
WTS_SECURITY_ALL_ACCESS: WTS_SECURITY_FLAGS = 983999
WTS_SECURITY_QUERY_INFORMATION: WTS_SECURITY_FLAGS = 1
WTS_SECURITY_SET_INFORMATION: WTS_SECURITY_FLAGS = 2
WTS_SECURITY_RESET: WTS_SECURITY_FLAGS = 4
WTS_SECURITY_VIRTUAL_CHANNELS: WTS_SECURITY_FLAGS = 8
WTS_SECURITY_REMOTE_CONTROL: WTS_SECURITY_FLAGS = 16
WTS_SECURITY_LOGON: WTS_SECURITY_FLAGS = 32
WTS_SECURITY_LOGOFF: WTS_SECURITY_FLAGS = 64
WTS_SECURITY_MESSAGE: WTS_SECURITY_FLAGS = 128
WTS_SECURITY_CONNECT: WTS_SECURITY_FLAGS = 256
WTS_SECURITY_DISCONNECT: WTS_SECURITY_FLAGS = 512
WTS_SECURITY_GUEST_ACCESS: WTS_SECURITY_FLAGS = 32
class WTS_SERVER_INFOA(Structure):
    pServerName: Windows.Win32.Foundation.PSTR
class WTS_SERVER_INFOW(Structure):
    pServerName: Windows.Win32.Foundation.PWSTR
class WTS_SERVICE_STATE(Structure):
    RcmServiceState: Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE
    RcmDrainState: Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE
class WTS_SESSION_ADDRESS(Structure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_SESSION_ID(Structure):
    SessionUniqueGuid: Guid
    SessionId: UInt32
class WTS_SESSION_INFOA(Structure):
    SessionId: UInt32
    pWinStationName: Windows.Win32.Foundation.PSTR
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
class WTS_SESSION_INFOW(Structure):
    SessionId: UInt32
    pWinStationName: Windows.Win32.Foundation.PWSTR
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
class WTS_SESSION_INFO_1A(Structure):
    ExecEnvId: UInt32
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: Windows.Win32.Foundation.PSTR
    pHostName: Windows.Win32.Foundation.PSTR
    pUserName: Windows.Win32.Foundation.PSTR
    pDomainName: Windows.Win32.Foundation.PSTR
    pFarmName: Windows.Win32.Foundation.PSTR
class WTS_SESSION_INFO_1W(Structure):
    ExecEnvId: UInt32
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: Windows.Win32.Foundation.PWSTR
    pHostName: Windows.Win32.Foundation.PWSTR
    pUserName: Windows.Win32.Foundation.PWSTR
    pDomainName: Windows.Win32.Foundation.PWSTR
    pFarmName: Windows.Win32.Foundation.PWSTR
class WTS_SMALL_RECT(Structure):
    Left: Int16
    Top: Int16
    Right: Int16
    Bottom: Int16
class WTS_SOCKADDR(Structure):
    sin_family: UInt16
    u: _u_e__Union
    class _u_e__Union(Union):
        ipv4: _ipv4_e__Struct
        ipv6: _ipv6_e__Struct
        class _ipv4_e__Struct(Structure):
            sin_port: UInt16
            IN_ADDR: UInt32
            sin_zero: Byte * 8
        class _ipv6_e__Struct(Structure):
            sin6_port: UInt16
            sin6_flowinfo: UInt32
            sin6_addr: UInt16 * 8
            sin6_scope_id: UInt32
class WTS_SYSTEMTIME(Structure):
    wYear: UInt16
    wMonth: UInt16
    wDayOfWeek: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
    wMilliseconds: UInt16
class WTS_TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    DaylightBias: Int32
WTS_TYPE_CLASS = Int32
WTS_TYPE_CLASS_WTSTypeProcessInfoLevel0: WTS_TYPE_CLASS = 0
WTS_TYPE_CLASS_WTSTypeProcessInfoLevel1: WTS_TYPE_CLASS = 1
WTS_TYPE_CLASS_WTSTypeSessionInfoLevel1: WTS_TYPE_CLASS = 2
class WTS_USER_CREDENTIAL(Structure):
    UserName: Char * 256
    Password: Char * 256
    Domain: Char * 256
class WTS_USER_DATA(Structure):
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    UserTimeZone: Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
class WTS_VALIDATION_INFORMATIONA(Structure):
    ProductInfo: Windows.Win32.System.RemoteDesktop.PRODUCT_INFOA
    License: Byte * 16384
    LicenseLength: UInt32
    HardwareID: Byte * 20
    HardwareIDLength: UInt32
class WTS_VALIDATION_INFORMATIONW(Structure):
    ProductInfo: Windows.Win32.System.RemoteDesktop.PRODUCT_INFOW
    License: Byte * 16384
    LicenseLength: UInt32
    HardwareID: Byte * 20
    HardwareIDLength: UInt32
WTS_VIRTUAL_CLASS = Int32
WTS_VIRTUAL_CLASS_WTSVirtualClientData: WTS_VIRTUAL_CLASS = 0
WTS_VIRTUAL_CLASS_WTSVirtualFileHandle: WTS_VIRTUAL_CLASS = 1
Workspace = Guid('4f1dfca6-3aad-48e1-84-06-4b-c2-1a-50-1d-7c')
class _ITSWkspEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b922bbb8-4c55-4fea-84-96-be-b0-b4-42-85-e9')
class pluginResource(Structure):
    alias: Char * 256
    name: Char * 256
    resourceFileContents: Windows.Win32.Foundation.PWSTR
    fileExtension: Char * 256
    resourcePluginType: Char * 256
    isDiscoverable: Byte
    resourceType: Int32
    pceIconSize: UInt32
    iconContents: c_char_p_no
    pcePluginBlobSize: UInt32
    blobContents: c_char_p_no
class pluginResource2(Structure):
    resourceV1: Windows.Win32.System.RemoteDesktop.pluginResource
    pceFileAssocListSize: UInt32
    fileAssocList: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2FileAssociation_head)
    securityDescriptor: Windows.Win32.Foundation.PWSTR
    pceFolderListSize: UInt32
    folderList: POINTER(POINTER(UInt16))
class pluginResource2FileAssociation(Structure):
    extName: Char * 256
    primaryHandler: Byte
    pceIconSize: UInt32
    iconContents: c_char_p_no
make_head(_module, 'AAAccountingData')
make_head(_module, 'AE_CURRENT_POSITION')
make_head(_module, 'BITMAP_RENDERER_STATISTICS')
make_head(_module, 'CHANNEL_DEF')
make_head(_module, 'CHANNEL_ENTRY_POINTS')
make_head(_module, 'CHANNEL_PDU_HEADER')
make_head(_module, 'CLIENT_DISPLAY')
make_head(_module, 'IADsTSUserEx')
make_head(_module, 'IAudioDeviceEndpoint')
make_head(_module, 'IAudioEndpoint')
make_head(_module, 'IAudioEndpointControl')
make_head(_module, 'IAudioEndpointRT')
make_head(_module, 'IAudioInputEndpointRT')
make_head(_module, 'IAudioOutputEndpointRT')
make_head(_module, 'IRemoteDesktopClient')
make_head(_module, 'IRemoteDesktopClientActions')
make_head(_module, 'IRemoteDesktopClientSettings')
make_head(_module, 'IRemoteDesktopClientTouchPointer')
make_head(_module, 'IRemoteSystemAdditionalInfoProvider')
make_head(_module, 'ITSGAccountingEngine')
make_head(_module, 'ITSGAuthenticateUserSink')
make_head(_module, 'ITSGAuthenticationEngine')
make_head(_module, 'ITSGAuthorizeConnectionSink')
make_head(_module, 'ITSGAuthorizeResourceSink')
make_head(_module, 'ITSGPolicyEngine')
make_head(_module, 'ITsSbBaseNotifySink')
make_head(_module, 'ITsSbClientConnection')
make_head(_module, 'ITsSbClientConnectionPropertySet')
make_head(_module, 'ITsSbEnvironment')
make_head(_module, 'ITsSbEnvironmentPropertySet')
make_head(_module, 'ITsSbFilterPluginStore')
make_head(_module, 'ITsSbGenericNotifySink')
make_head(_module, 'ITsSbGlobalStore')
make_head(_module, 'ITsSbLoadBalanceResult')
make_head(_module, 'ITsSbLoadBalancing')
make_head(_module, 'ITsSbLoadBalancingNotifySink')
make_head(_module, 'ITsSbOrchestration')
make_head(_module, 'ITsSbOrchestrationNotifySink')
make_head(_module, 'ITsSbPlacement')
make_head(_module, 'ITsSbPlacementNotifySink')
make_head(_module, 'ITsSbPlugin')
make_head(_module, 'ITsSbPluginNotifySink')
make_head(_module, 'ITsSbPluginPropertySet')
make_head(_module, 'ITsSbPropertySet')
make_head(_module, 'ITsSbProvider')
make_head(_module, 'ITsSbProvisioning')
make_head(_module, 'ITsSbProvisioningPluginNotifySink')
make_head(_module, 'ITsSbResourceNotification')
make_head(_module, 'ITsSbResourceNotificationEx')
make_head(_module, 'ITsSbResourcePlugin')
make_head(_module, 'ITsSbResourcePluginStore')
make_head(_module, 'ITsSbServiceNotification')
make_head(_module, 'ITsSbSession')
make_head(_module, 'ITsSbTarget')
make_head(_module, 'ITsSbTargetPropertySet')
make_head(_module, 'ITsSbTaskInfo')
make_head(_module, 'ITsSbTaskPlugin')
make_head(_module, 'ITsSbTaskPluginNotifySink')
make_head(_module, 'IWRdsEnhancedFastReconnectArbitrator')
make_head(_module, 'IWRdsGraphicsChannel')
make_head(_module, 'IWRdsGraphicsChannelEvents')
make_head(_module, 'IWRdsGraphicsChannelManager')
make_head(_module, 'IWRdsProtocolConnection')
make_head(_module, 'IWRdsProtocolConnectionCallback')
make_head(_module, 'IWRdsProtocolConnectionSettings')
make_head(_module, 'IWRdsProtocolLicenseConnection')
make_head(_module, 'IWRdsProtocolListener')
make_head(_module, 'IWRdsProtocolListenerCallback')
make_head(_module, 'IWRdsProtocolLogonErrorRedirector')
make_head(_module, 'IWRdsProtocolManager')
make_head(_module, 'IWRdsProtocolSettings')
make_head(_module, 'IWRdsProtocolShadowCallback')
make_head(_module, 'IWRdsProtocolShadowConnection')
make_head(_module, 'IWRdsWddmIddProps')
make_head(_module, 'IWTSBitmapRenderService')
make_head(_module, 'IWTSBitmapRenderer')
make_head(_module, 'IWTSBitmapRendererCallback')
make_head(_module, 'IWTSListener')
make_head(_module, 'IWTSListenerCallback')
make_head(_module, 'IWTSPlugin')
make_head(_module, 'IWTSPluginServiceProvider')
make_head(_module, 'IWTSProtocolConnection')
make_head(_module, 'IWTSProtocolConnectionCallback')
make_head(_module, 'IWTSProtocolLicenseConnection')
make_head(_module, 'IWTSProtocolListener')
make_head(_module, 'IWTSProtocolListenerCallback')
make_head(_module, 'IWTSProtocolLogonErrorRedirector')
make_head(_module, 'IWTSProtocolManager')
make_head(_module, 'IWTSProtocolShadowCallback')
make_head(_module, 'IWTSProtocolShadowConnection')
make_head(_module, 'IWTSSBPlugin')
make_head(_module, 'IWTSVirtualChannel')
make_head(_module, 'IWTSVirtualChannelCallback')
make_head(_module, 'IWTSVirtualChannelManager')
make_head(_module, 'IWorkspace')
make_head(_module, 'IWorkspace2')
make_head(_module, 'IWorkspace3')
make_head(_module, 'IWorkspaceClientExt')
make_head(_module, 'IWorkspaceRegistration')
make_head(_module, 'IWorkspaceRegistration2')
make_head(_module, 'IWorkspaceReportMessage')
make_head(_module, 'IWorkspaceResTypeRegistry')
make_head(_module, 'IWorkspaceScriptable')
make_head(_module, 'IWorkspaceScriptable2')
make_head(_module, 'IWorkspaceScriptable3')
make_head(_module, 'ItsPubPlugin')
make_head(_module, 'ItsPubPlugin2')
make_head(_module, 'PCHANNEL_INIT_EVENT_FN')
make_head(_module, 'PCHANNEL_OPEN_EVENT_FN')
make_head(_module, 'PRODUCT_INFOA')
make_head(_module, 'PRODUCT_INFOW')
make_head(_module, 'PVIRTUALCHANNELCLOSE')
make_head(_module, 'PVIRTUALCHANNELENTRY')
make_head(_module, 'PVIRTUALCHANNELINIT')
make_head(_module, 'PVIRTUALCHANNELOPEN')
make_head(_module, 'PVIRTUALCHANNELWRITE')
make_head(_module, 'RFX_GFX_MONITOR_INFO')
make_head(_module, 'RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST')
make_head(_module, 'RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE')
make_head(_module, 'RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM')
make_head(_module, 'RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY')
make_head(_module, 'RFX_GFX_MSG_DESKTOP_INPUT_RESET')
make_head(_module, 'RFX_GFX_MSG_DESKTOP_RESEND_REQUEST')
make_head(_module, 'RFX_GFX_MSG_DISCONNECT_NOTIFY')
make_head(_module, 'RFX_GFX_MSG_HEADER')
make_head(_module, 'RFX_GFX_MSG_RDP_DATA')
make_head(_module, 'RFX_GFX_RECT')
make_head(_module, 'TSSD_ConnectionPoint')
make_head(_module, 'VM_NOTIFY_ENTRY')
make_head(_module, 'VM_NOTIFY_INFO')
make_head(_module, 'VM_PATCH_INFO')
make_head(_module, 'WRDS_CONNECTION_SETTING')
make_head(_module, 'WRDS_CONNECTION_SETTINGS')
make_head(_module, 'WRDS_CONNECTION_SETTINGS_1')
make_head(_module, 'WRDS_DYNAMIC_TIME_ZONE_INFORMATION')
make_head(_module, 'WRDS_LISTENER_SETTING')
make_head(_module, 'WRDS_LISTENER_SETTINGS')
make_head(_module, 'WRDS_LISTENER_SETTINGS_1')
make_head(_module, 'WRDS_SETTING')
make_head(_module, 'WRDS_SETTINGS')
make_head(_module, 'WRDS_SETTINGS_1')
make_head(_module, 'WTSCLIENTA')
make_head(_module, 'WTSCLIENTW')
make_head(_module, 'WTSCONFIGINFOA')
make_head(_module, 'WTSCONFIGINFOW')
make_head(_module, 'WTSINFOA')
make_head(_module, 'WTSINFOEXA')
make_head(_module, 'WTSINFOEXW')
make_head(_module, 'WTSINFOEX_LEVEL1_A')
make_head(_module, 'WTSINFOEX_LEVEL1_W')
make_head(_module, 'WTSINFOEX_LEVEL_A')
make_head(_module, 'WTSINFOEX_LEVEL_W')
make_head(_module, 'WTSINFOW')
make_head(_module, 'WTSLISTENERCONFIGA')
make_head(_module, 'WTSLISTENERCONFIGW')
make_head(_module, 'WTSSBX_IP_ADDRESS')
make_head(_module, 'WTSSBX_MACHINE_CONNECT_INFO')
make_head(_module, 'WTSSBX_MACHINE_INFO')
make_head(_module, 'WTSSBX_SESSION_INFO')
make_head(_module, 'WTSSESSION_NOTIFICATION')
make_head(_module, 'WTSUSERCONFIGA')
make_head(_module, 'WTSUSERCONFIGW')
make_head(_module, 'WTS_CACHE_STATS')
make_head(_module, 'WTS_CACHE_STATS_UN')
make_head(_module, 'WTS_CLIENT_ADDRESS')
make_head(_module, 'WTS_CLIENT_DATA')
make_head(_module, 'WTS_CLIENT_DISPLAY')
make_head(_module, 'WTS_DISPLAY_IOCTL')
make_head(_module, 'WTS_LICENSE_CAPABILITIES')
make_head(_module, 'WTS_POLICY_DATA')
make_head(_module, 'WTS_PROCESS_INFOA')
make_head(_module, 'WTS_PROCESS_INFOW')
make_head(_module, 'WTS_PROCESS_INFO_EXA')
make_head(_module, 'WTS_PROCESS_INFO_EXW')
make_head(_module, 'WTS_PROPERTY_VALUE')
make_head(_module, 'WTS_PROTOCOL_CACHE')
make_head(_module, 'WTS_PROTOCOL_COUNTERS')
make_head(_module, 'WTS_PROTOCOL_STATUS')
make_head(_module, 'WTS_SERVER_INFOA')
make_head(_module, 'WTS_SERVER_INFOW')
make_head(_module, 'WTS_SERVICE_STATE')
make_head(_module, 'WTS_SESSION_ADDRESS')
make_head(_module, 'WTS_SESSION_ID')
make_head(_module, 'WTS_SESSION_INFOA')
make_head(_module, 'WTS_SESSION_INFOW')
make_head(_module, 'WTS_SESSION_INFO_1A')
make_head(_module, 'WTS_SESSION_INFO_1W')
make_head(_module, 'WTS_SMALL_RECT')
make_head(_module, 'WTS_SOCKADDR')
make_head(_module, 'WTS_SYSTEMTIME')
make_head(_module, 'WTS_TIME_ZONE_INFORMATION')
make_head(_module, 'WTS_USER_CREDENTIAL')
make_head(_module, 'WTS_USER_DATA')
make_head(_module, 'WTS_VALIDATION_INFORMATIONA')
make_head(_module, 'WTS_VALIDATION_INFORMATIONW')
make_head(_module, '_ITSWkspEvents')
make_head(_module, 'pluginResource')
make_head(_module, 'pluginResource2')
make_head(_module, 'pluginResource2FileAssociation')
__all__ = [
    "AAAccountingData",
    "AAAccountingDataType",
    "AAAuthSchemes",
    "AATrustClassID",
    "AA_AUTH_ANY",
    "AA_AUTH_BASIC",
    "AA_AUTH_CONID",
    "AA_AUTH_COOKIE",
    "AA_AUTH_DIGEST",
    "AA_AUTH_LOGGEDONCREDENTIALS",
    "AA_AUTH_MAX",
    "AA_AUTH_MIN",
    "AA_AUTH_NEGOTIATE",
    "AA_AUTH_NTLM",
    "AA_AUTH_ORGID",
    "AA_AUTH_SC",
    "AA_AUTH_SSPI_NTLM",
    "AA_MAIN_SESSION_CLOSED",
    "AA_MAIN_SESSION_CREATION",
    "AA_SUB_SESSION_CLOSED",
    "AA_SUB_SESSION_CREATION",
    "AA_TRUSTEDUSER_TRUSTEDCLIENT",
    "AA_TRUSTEDUSER_UNTRUSTEDCLIENT",
    "AA_UNTRUSTED",
    "ACQUIRE_TARGET_LOCK_TIMEOUT",
    "ADsTSUserEx",
    "AE_CURRENT_POSITION",
    "AE_POSITION_FLAGS",
    "BITMAP_RENDERER_STATISTICS",
    "CHANNEL_BUFFER_SIZE",
    "CHANNEL_CHUNK_LENGTH",
    "CHANNEL_DEF",
    "CHANNEL_ENTRY_POINTS",
    "CHANNEL_EVENT_CONNECTED",
    "CHANNEL_EVENT_DATA_RECEIVED",
    "CHANNEL_EVENT_DISCONNECTED",
    "CHANNEL_EVENT_INITIALIZED",
    "CHANNEL_EVENT_TERMINATED",
    "CHANNEL_EVENT_V1_CONNECTED",
    "CHANNEL_EVENT_WRITE_CANCELLED",
    "CHANNEL_EVENT_WRITE_COMPLETE",
    "CHANNEL_FLAG_FAIL",
    "CHANNEL_FLAG_FIRST",
    "CHANNEL_FLAG_LAST",
    "CHANNEL_FLAG_MIDDLE",
    "CHANNEL_MAX_COUNT",
    "CHANNEL_NAME_LEN",
    "CHANNEL_OPTION_COMPRESS",
    "CHANNEL_OPTION_COMPRESS_RDP",
    "CHANNEL_OPTION_ENCRYPT_CS",
    "CHANNEL_OPTION_ENCRYPT_RDP",
    "CHANNEL_OPTION_ENCRYPT_SC",
    "CHANNEL_OPTION_INITIALIZED",
    "CHANNEL_OPTION_PRI_HIGH",
    "CHANNEL_OPTION_PRI_LOW",
    "CHANNEL_OPTION_PRI_MED",
    "CHANNEL_OPTION_REMOTE_CONTROL_PERSISTENT",
    "CHANNEL_OPTION_SHOW_PROTOCOL",
    "CHANNEL_PDU_HEADER",
    "CHANNEL_RC_ALREADY_CONNECTED",
    "CHANNEL_RC_ALREADY_INITIALIZED",
    "CHANNEL_RC_ALREADY_OPEN",
    "CHANNEL_RC_BAD_CHANNEL",
    "CHANNEL_RC_BAD_CHANNEL_HANDLE",
    "CHANNEL_RC_BAD_INIT_HANDLE",
    "CHANNEL_RC_BAD_PROC",
    "CHANNEL_RC_INITIALIZATION_ERROR",
    "CHANNEL_RC_INVALID_INSTANCE",
    "CHANNEL_RC_NOT_CONNECTED",
    "CHANNEL_RC_NOT_INITIALIZED",
    "CHANNEL_RC_NOT_IN_VIRTUALCHANNELENTRY",
    "CHANNEL_RC_NOT_OPEN",
    "CHANNEL_RC_NO_BUFFER",
    "CHANNEL_RC_NO_MEMORY",
    "CHANNEL_RC_NULL_DATA",
    "CHANNEL_RC_OK",
    "CHANNEL_RC_TOO_MANY_CHANNELS",
    "CHANNEL_RC_UNKNOWN_CHANNEL_NAME",
    "CHANNEL_RC_UNSUPPORTED_VERSION",
    "CHANNEL_RC_ZERO_LENGTH",
    "CLIENTADDRESS_LENGTH",
    "CLIENTNAME_LENGTH",
    "CLIENT_DISPLAY",
    "CLIENT_MESSAGE_CONNECTION_ERROR",
    "CLIENT_MESSAGE_CONNECTION_INVALID",
    "CLIENT_MESSAGE_CONNECTION_STATUS",
    "CLIENT_MESSAGE_TYPE",
    "CONNECTION_CHANGE_NOTIFICATION",
    "CONNECTION_PROPERTY_CURSOR_BLINK_DISABLED",
    "CONNECTION_PROPERTY_IDLE_TIME_WARNING",
    "CONNECTION_REQUEST_CANCELLED",
    "CONNECTION_REQUEST_FAILED",
    "CONNECTION_REQUEST_INVALID",
    "CONNECTION_REQUEST_LB_COMPLETED",
    "CONNECTION_REQUEST_ORCH_COMPLETED",
    "CONNECTION_REQUEST_PENDING",
    "CONNECTION_REQUEST_QUERY_PL_COMPLETED",
    "CONNECTION_REQUEST_SUCCEEDED",
    "CONNECTION_REQUEST_TIMEDOUT",
    "DISPID_AX_ADMINMESSAGERECEIVED",
    "DISPID_AX_AUTORECONNECTED",
    "DISPID_AX_AUTORECONNECTING",
    "DISPID_AX_CONNECTED",
    "DISPID_AX_CONNECTING",
    "DISPID_AX_DIALOGDISMISSED",
    "DISPID_AX_DIALOGDISPLAYING",
    "DISPID_AX_DISCONNECTED",
    "DISPID_AX_KEYCOMBINATIONPRESSED",
    "DISPID_AX_LOGINCOMPLETED",
    "DISPID_AX_NETWORKSTATUSCHANGED",
    "DISPID_AX_REMOTEDESKTOPSIZECHANGED",
    "DISPID_AX_STATUSCHANGED",
    "DISPID_AX_TOUCHPOINTERCURSORMOVED",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_APPLY_SETTINGS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_ATTACH_EVENT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_CONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DELETE_SAVED_CREDENTIALS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DETACH_EVENT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DISCONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_EXECUTE_REMOTE_ACTION",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_RDPPROPERTY",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_SNAPSHOT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RECONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RESUME_SCREEN_UPDATES",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RETRIEVE_SETTINGS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_SET_RDPPROPERTY",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_SUSPEND_SCREEN_UPDATES",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_UPDATE_SESSION_DISPLAYSETTINGS",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_ACTIONS",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_SETTINGS",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_ENABLED",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_EVENTSENABLED",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_POINTERSPEED",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCH_POINTER",
    "DOMAIN_LENGTH",
    "FARM",
    "FORCE_REJOIN",
    "FORCE_REJOIN_IN_CLUSTERMODE",
    "HwtsVirtualChannelHandle",
    "IADsTSUserEx",
    "IAudioDeviceEndpoint",
    "IAudioEndpoint",
    "IAudioEndpointControl",
    "IAudioEndpointRT",
    "IAudioInputEndpointRT",
    "IAudioOutputEndpointRT",
    "IRemoteDesktopClient",
    "IRemoteDesktopClientActions",
    "IRemoteDesktopClientSettings",
    "IRemoteDesktopClientTouchPointer",
    "IRemoteSystemAdditionalInfoProvider",
    "ITSGAccountingEngine",
    "ITSGAuthenticateUserSink",
    "ITSGAuthenticationEngine",
    "ITSGAuthorizeConnectionSink",
    "ITSGAuthorizeResourceSink",
    "ITSGPolicyEngine",
    "ITsSbBaseNotifySink",
    "ITsSbClientConnection",
    "ITsSbClientConnectionPropertySet",
    "ITsSbEnvironment",
    "ITsSbEnvironmentPropertySet",
    "ITsSbFilterPluginStore",
    "ITsSbGenericNotifySink",
    "ITsSbGlobalStore",
    "ITsSbLoadBalanceResult",
    "ITsSbLoadBalancing",
    "ITsSbLoadBalancingNotifySink",
    "ITsSbOrchestration",
    "ITsSbOrchestrationNotifySink",
    "ITsSbPlacement",
    "ITsSbPlacementNotifySink",
    "ITsSbPlugin",
    "ITsSbPluginNotifySink",
    "ITsSbPluginPropertySet",
    "ITsSbPropertySet",
    "ITsSbProvider",
    "ITsSbProvisioning",
    "ITsSbProvisioningPluginNotifySink",
    "ITsSbResourceNotification",
    "ITsSbResourceNotificationEx",
    "ITsSbResourcePlugin",
    "ITsSbResourcePluginStore",
    "ITsSbServiceNotification",
    "ITsSbSession",
    "ITsSbTarget",
    "ITsSbTargetPropertySet",
    "ITsSbTaskInfo",
    "ITsSbTaskPlugin",
    "ITsSbTaskPluginNotifySink",
    "IWRdsEnhancedFastReconnectArbitrator",
    "IWRdsGraphicsChannel",
    "IWRdsGraphicsChannelEvents",
    "IWRdsGraphicsChannelManager",
    "IWRdsProtocolConnection",
    "IWRdsProtocolConnectionCallback",
    "IWRdsProtocolConnectionSettings",
    "IWRdsProtocolLicenseConnection",
    "IWRdsProtocolListener",
    "IWRdsProtocolListenerCallback",
    "IWRdsProtocolLogonErrorRedirector",
    "IWRdsProtocolManager",
    "IWRdsProtocolSettings",
    "IWRdsProtocolShadowCallback",
    "IWRdsProtocolShadowConnection",
    "IWRdsWddmIddProps",
    "IWTSBitmapRenderService",
    "IWTSBitmapRenderer",
    "IWTSBitmapRendererCallback",
    "IWTSListener",
    "IWTSListenerCallback",
    "IWTSPlugin",
    "IWTSPluginServiceProvider",
    "IWTSProtocolConnection",
    "IWTSProtocolConnectionCallback",
    "IWTSProtocolLicenseConnection",
    "IWTSProtocolListener",
    "IWTSProtocolListenerCallback",
    "IWTSProtocolLogonErrorRedirector",
    "IWTSProtocolManager",
    "IWTSProtocolShadowCallback",
    "IWTSProtocolShadowConnection",
    "IWTSSBPlugin",
    "IWTSVirtualChannel",
    "IWTSVirtualChannelCallback",
    "IWTSVirtualChannelManager",
    "IWorkspace",
    "IWorkspace2",
    "IWorkspace3",
    "IWorkspaceClientExt",
    "IWorkspaceRegistration",
    "IWorkspaceRegistration2",
    "IWorkspaceReportMessage",
    "IWorkspaceResTypeRegistry",
    "IWorkspaceScriptable",
    "IWorkspaceScriptable2",
    "IWorkspaceScriptable3",
    "ItsPubPlugin",
    "ItsPubPlugin2",
    "KEEP_EXISTING_SESSIONS",
    "KeyCombinationType",
    "KeyCombinationType_KeyCombinationDown",
    "KeyCombinationType_KeyCombinationHome",
    "KeyCombinationType_KeyCombinationLeft",
    "KeyCombinationType_KeyCombinationRight",
    "KeyCombinationType_KeyCombinationScroll",
    "KeyCombinationType_KeyCombinationUp",
    "LOAD_BALANCING_PLUGIN",
    "MAX_DATE_TIME_LENGTH",
    "MAX_ELAPSED_TIME_LENGTH",
    "MAX_POLICY_ATTRIBUTES",
    "MaxAppName_Len",
    "MaxDomainName_Len",
    "MaxFQDN_Len",
    "MaxFarm_Len",
    "MaxNetBiosName_Len",
    "MaxNumOfExposed_IPs",
    "MaxUserName_Len",
    "NONFARM",
    "NOTIFY_FOR_ALL_SESSIONS",
    "NOTIFY_FOR_THIS_SESSION",
    "ORCHESTRATION_PLUGIN",
    "OWNER_MS_TS_PLUGIN",
    "OWNER_MS_VM_PLUGIN",
    "OWNER_UNKNOWN",
    "PCHANNEL_INIT_EVENT_FN",
    "PCHANNEL_OPEN_EVENT_FN",
    "PLACEMENT_PLUGIN",
    "PLUGIN_CAPABILITY_EXTERNAL_REDIRECTION",
    "PLUGIN_TYPE",
    "POLICY_PLUGIN",
    "POSITION_CONTINUOUS",
    "POSITION_DISCONTINUOUS",
    "POSITION_INVALID",
    "POSITION_QPC_ERROR",
    "PRODUCTINFO_COMPANYNAME_LENGTH",
    "PRODUCTINFO_PRODUCTID_LENGTH",
    "PRODUCT_INFOA",
    "PRODUCT_INFOW",
    "PROPERTY_DYNAMIC_TIME_ZONE_INFORMATION",
    "PROPERTY_TYPE_ENABLE_UNIVERSAL_APPS_FOR_CUSTOM_SHELL",
    "PROPERTY_TYPE_GET_FAST_RECONNECT",
    "PROPERTY_TYPE_GET_FAST_RECONNECT_USER_SID",
    "PROVISIONING_PLUGIN",
    "PVIRTUALCHANNELCLOSE",
    "PVIRTUALCHANNELENTRY",
    "PVIRTUALCHANNELINIT",
    "PVIRTUALCHANNELOPEN",
    "PVIRTUALCHANNELWRITE",
    "PasswordEncodingType",
    "PasswordEncodingType_PasswordEncodingUTF16BE",
    "PasswordEncodingType_PasswordEncodingUTF16LE",
    "PasswordEncodingType_PasswordEncodingUTF8",
    "PolicyAttributeType",
    "PolicyAttributeType_AllowOnlySDRServers",
    "PolicyAttributeType_ClipboardRedirectionDisabled",
    "PolicyAttributeType_DisableAllRedirections",
    "PolicyAttributeType_DriveRedirectionDisabled",
    "PolicyAttributeType_EnableAllRedirections",
    "PolicyAttributeType_PnpRedirectionDisabled",
    "PolicyAttributeType_PortRedirectionDisabled",
    "PolicyAttributeType_PrinterRedirectionDisabled",
    "ProcessIdToSessionId",
    "RDCLIENT_BITMAP_RENDER_SERVICE",
    "RDV_TASK_STATUS",
    "RDV_TASK_STATUS_APPLYING",
    "RDV_TASK_STATUS_DOWNLOADING",
    "RDV_TASK_STATUS_FAILED",
    "RDV_TASK_STATUS_REBOOTED",
    "RDV_TASK_STATUS_REBOOTING",
    "RDV_TASK_STATUS_SEARCHING",
    "RDV_TASK_STATUS_SUCCESS",
    "RDV_TASK_STATUS_TIMEOUT",
    "RDV_TASK_STATUS_UNKNOWN",
    "RD_FARM_AUTO_PERSONAL_RDSH",
    "RD_FARM_AUTO_PERSONAL_VM",
    "RD_FARM_MANUAL_PERSONAL_RDSH",
    "RD_FARM_MANUAL_PERSONAL_VM",
    "RD_FARM_RDSH",
    "RD_FARM_TEMP_VM",
    "RD_FARM_TYPE",
    "RD_FARM_TYPE_UNKNOWN",
    "REMOTECONTROL_KBDALT_HOTKEY",
    "REMOTECONTROL_KBDCTRL_HOTKEY",
    "REMOTECONTROL_KBDSHIFT_HOTKEY",
    "RENDER_HINT_CLEAR",
    "RENDER_HINT_MAPPEDWINDOW",
    "RENDER_HINT_VIDEO",
    "RESERVED_FOR_LEGACY",
    "RESOURCE_PLUGIN",
    "RFX_CLIENT_ID_LENGTH",
    "RFX_GFX_MAX_SUPPORTED_MONITORS",
    "RFX_GFX_MONITOR_INFO",
    "RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST",
    "RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE",
    "RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM",
    "RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY",
    "RFX_GFX_MSG_DESKTOP_INPUT_RESET",
    "RFX_GFX_MSG_DESKTOP_RESEND_REQUEST",
    "RFX_GFX_MSG_DISCONNECT_NOTIFY",
    "RFX_GFX_MSG_HEADER",
    "RFX_GFX_MSG_PREFIX",
    "RFX_GFX_MSG_PREFIX_MASK",
    "RFX_GFX_MSG_RDP_DATA",
    "RFX_GFX_RECT",
    "RFX_RDP_MSG_PREFIX",
    "RemoteActionType",
    "RemoteActionType_RemoteActionAppSwitch",
    "RemoteActionType_RemoteActionAppbar",
    "RemoteActionType_RemoteActionCharms",
    "RemoteActionType_RemoteActionSnap",
    "RemoteActionType_RemoteActionStartScreen",
    "SB_SYNCH_CONFLICT_MAX_WRITE_ATTEMPTS",
    "SESSION_TIMEOUT_ACTION_DISCONNECT",
    "SESSION_TIMEOUT_ACTION_SILENT_REAUTH",
    "SESSION_TIMEOUT_ACTION_TYPE",
    "SINGLE_SESSION",
    "STATE_ACTIVE",
    "STATE_CONNECTED",
    "STATE_CONNECTQUERY",
    "STATE_DISCONNECTED",
    "STATE_DOWN",
    "STATE_IDLE",
    "STATE_INIT",
    "STATE_INVALID",
    "STATE_LISTEN",
    "STATE_MAX",
    "STATE_RESET",
    "STATE_SHADOW",
    "SnapshotEncodingType",
    "SnapshotEncodingType_SnapshotEncodingDataUri",
    "SnapshotFormatType",
    "SnapshotFormatType_SnapshotFormatBmp",
    "SnapshotFormatType_SnapshotFormatJpeg",
    "SnapshotFormatType_SnapshotFormatPng",
    "TARGET_CHANGE_TYPE",
    "TARGET_CHANGE_UNSPEC",
    "TARGET_CHECKED_OUT",
    "TARGET_DOWN",
    "TARGET_EXTERNALIP_CHANGED",
    "TARGET_FARM_MEMBERSHIP_CHANGED",
    "TARGET_HIBERNATED",
    "TARGET_IDLE",
    "TARGET_INITIALIZING",
    "TARGET_INTERNALIP_CHANGED",
    "TARGET_INUSE",
    "TARGET_INVALID",
    "TARGET_JOINED",
    "TARGET_MAXSTATE",
    "TARGET_OWNER",
    "TARGET_PATCH_COMPLETED",
    "TARGET_PATCH_FAILED",
    "TARGET_PATCH_IN_PROGRESS",
    "TARGET_PATCH_NOT_STARTED",
    "TARGET_PATCH_STATE",
    "TARGET_PATCH_STATE_CHANGED",
    "TARGET_PATCH_UNKNOWN",
    "TARGET_PENDING",
    "TARGET_REMOVED",
    "TARGET_RUNNING",
    "TARGET_STARTING",
    "TARGET_STATE",
    "TARGET_STATE_CHANGED",
    "TARGET_STOPPED",
    "TARGET_STOPPING",
    "TARGET_TYPE",
    "TARGET_UNKNOWN",
    "TASK_PLUGIN",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_EXISTING",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_NEW",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE",
    "TSPUB_PLUGIN_PD_QUERY_EXISTING",
    "TSPUB_PLUGIN_PD_QUERY_OR_CREATE",
    "TSPUB_PLUGIN_PD_RESOLUTION_TYPE",
    "TSSB_NOTIFICATION_TYPE",
    "TSSB_NOTIFY_CONNECTION_REQUEST_CHANGE",
    "TSSB_NOTIFY_INVALID",
    "TSSB_NOTIFY_SESSION_CHANGE",
    "TSSB_NOTIFY_TARGET_CHANGE",
    "TSSD_ADDR_IPv4",
    "TSSD_ADDR_IPv6",
    "TSSD_ADDR_UNDEFINED",
    "TSSD_AddrV46Type",
    "TSSD_ConnectionPoint",
    "TSSESSION_STATE",
    "TSUserExInterfaces",
    "TS_SB_SORT_BY",
    "TS_SB_SORT_BY_NAME",
    "TS_SB_SORT_BY_NONE",
    "TS_SB_SORT_BY_PROP",
    "TS_VC_LISTENER_STATIC_CHANNEL",
    "UNKNOWN",
    "UNKNOWN_PLUGIN",
    "USERNAME_LENGTH",
    "VALIDATIONINFORMATION_HARDWAREID_LENGTH",
    "VALIDATIONINFORMATION_LICENSE_LENGTH",
    "VIRTUAL_CHANNEL_VERSION_WIN2000",
    "VM_HOST_NOTIFY_STATUS",
    "VM_HOST_STATUS_INIT_COMPLETE",
    "VM_HOST_STATUS_INIT_FAILED",
    "VM_HOST_STATUS_INIT_IN_PROGRESS",
    "VM_HOST_STATUS_INIT_PENDING",
    "VM_NOTIFY_ENTRY",
    "VM_NOTIFY_INFO",
    "VM_NOTIFY_STATUS",
    "VM_NOTIFY_STATUS_CANCELED",
    "VM_NOTIFY_STATUS_COMPLETE",
    "VM_NOTIFY_STATUS_FAILED",
    "VM_NOTIFY_STATUS_IN_PROGRESS",
    "VM_NOTIFY_STATUS_PENDING",
    "VM_PATCH_INFO",
    "WINSTATIONNAME_LENGTH",
    "WKS_FLAG_CLEAR_CREDS_ON_LAST_RESOURCE",
    "WKS_FLAG_CREDS_AUTHENTICATED",
    "WKS_FLAG_PASSWORD_ENCRYPTED",
    "WRDS_CLIENTADDRESS_LENGTH",
    "WRDS_CLIENTNAME_LENGTH",
    "WRDS_CLIENT_PRODUCT_ID_LENGTH",
    "WRDS_CONNECTION_SETTING",
    "WRDS_CONNECTION_SETTINGS",
    "WRDS_CONNECTION_SETTINGS_1",
    "WRDS_CONNECTION_SETTING_LEVEL",
    "WRDS_CONNECTION_SETTING_LEVEL_1",
    "WRDS_CONNECTION_SETTING_LEVEL_INVALID",
    "WRDS_DEVICE_NAME_LENGTH",
    "WRDS_DIRECTORY_LENGTH",
    "WRDS_DOMAIN_LENGTH",
    "WRDS_DRIVER_NAME_LENGTH",
    "WRDS_DYNAMIC_TIME_ZONE_INFORMATION",
    "WRDS_IMEFILENAME_LENGTH",
    "WRDS_INITIALPROGRAM_LENGTH",
    "WRDS_KEY_EXCHANGE_ALG_DH",
    "WRDS_KEY_EXCHANGE_ALG_RSA",
    "WRDS_LICENSE_PREAMBLE_VERSION",
    "WRDS_LICENSE_PROTOCOL_VERSION",
    "WRDS_LISTENER_SETTING",
    "WRDS_LISTENER_SETTINGS",
    "WRDS_LISTENER_SETTINGS_1",
    "WRDS_LISTENER_SETTING_LEVEL",
    "WRDS_LISTENER_SETTING_LEVEL_1",
    "WRDS_LISTENER_SETTING_LEVEL_INVALID",
    "WRDS_MAX_CACHE_RESERVED",
    "WRDS_MAX_COUNTERS",
    "WRDS_MAX_DISPLAY_IOCTL_DATA",
    "WRDS_MAX_PROTOCOL_CACHE",
    "WRDS_MAX_RESERVED",
    "WRDS_PASSWORD_LENGTH",
    "WRDS_PERF_DISABLE_CURSORSETTINGS",
    "WRDS_PERF_DISABLE_CURSOR_SHADOW",
    "WRDS_PERF_DISABLE_FULLWINDOWDRAG",
    "WRDS_PERF_DISABLE_MENUANIMATIONS",
    "WRDS_PERF_DISABLE_NOTHING",
    "WRDS_PERF_DISABLE_THEMING",
    "WRDS_PERF_DISABLE_WALLPAPER",
    "WRDS_PERF_ENABLE_DESKTOP_COMPOSITION",
    "WRDS_PERF_ENABLE_ENHANCED_GRAPHICS",
    "WRDS_PERF_ENABLE_FONT_SMOOTHING",
    "WRDS_PROTOCOL_NAME_LENGTH",
    "WRDS_SERVICE_ID_GRAPHICS_GUID",
    "WRDS_SETTING",
    "WRDS_SETTINGS",
    "WRDS_SETTINGS_1",
    "WRDS_SETTING_LEVEL",
    "WRDS_SETTING_LEVEL_1",
    "WRDS_SETTING_LEVEL_INVALID",
    "WRDS_SETTING_STATUS",
    "WRDS_SETTING_STATUS_DISABLED",
    "WRDS_SETTING_STATUS_ENABLED",
    "WRDS_SETTING_STATUS_NOTAPPLICABLE",
    "WRDS_SETTING_STATUS_NOTCONFIGURED",
    "WRDS_SETTING_TYPE",
    "WRDS_SETTING_TYPE_INVALID",
    "WRDS_SETTING_TYPE_MACHINE",
    "WRDS_SETTING_TYPE_SAM",
    "WRDS_SETTING_TYPE_USER",
    "WRDS_USERNAME_LENGTH",
    "WRDS_VALUE_TYPE_BINARY",
    "WRDS_VALUE_TYPE_GUID",
    "WRDS_VALUE_TYPE_STRING",
    "WRDS_VALUE_TYPE_ULONG",
    "WRdsGraphicsChannelType",
    "WRdsGraphicsChannelType_BestEffortDelivery",
    "WRdsGraphicsChannelType_GuaranteedDelivery",
    "WRdsGraphicsChannels_LossyChannelMaxMessageSize",
    "WTSCLIENTA",
    "WTSCLIENTW",
    "WTSCONFIGINFOA",
    "WTSCONFIGINFOW",
    "WTSCloseServer",
    "WTSConnectSessionA",
    "WTSConnectSessionW",
    "WTSCreateListenerA",
    "WTSCreateListenerW",
    "WTSDisconnectSession",
    "WTSEnableChildSessions",
    "WTSEnumerateListenersA",
    "WTSEnumerateListenersW",
    "WTSEnumerateProcessesA",
    "WTSEnumerateProcessesExA",
    "WTSEnumerateProcessesExW",
    "WTSEnumerateProcessesW",
    "WTSEnumerateServersA",
    "WTSEnumerateServersW",
    "WTSEnumerateSessionsA",
    "WTSEnumerateSessionsExA",
    "WTSEnumerateSessionsExW",
    "WTSEnumerateSessionsW",
    "WTSFreeMemory",
    "WTSFreeMemoryExA",
    "WTSFreeMemoryExW",
    "WTSGetActiveConsoleSessionId",
    "WTSGetChildSessionId",
    "WTSGetListenerSecurityA",
    "WTSGetListenerSecurityW",
    "WTSINFOA",
    "WTSINFOEXA",
    "WTSINFOEXW",
    "WTSINFOEX_LEVEL1_A",
    "WTSINFOEX_LEVEL1_W",
    "WTSINFOEX_LEVEL_A",
    "WTSINFOEX_LEVEL_W",
    "WTSINFOW",
    "WTSIsChildSessionsEnabled",
    "WTSLISTENERCONFIGA",
    "WTSLISTENERCONFIGW",
    "WTSLogoffSession",
    "WTSOpenServerA",
    "WTSOpenServerExA",
    "WTSOpenServerExW",
    "WTSOpenServerW",
    "WTSQueryListenerConfigA",
    "WTSQueryListenerConfigW",
    "WTSQuerySessionInformationA",
    "WTSQuerySessionInformationW",
    "WTSQueryUserConfigA",
    "WTSQueryUserConfigW",
    "WTSQueryUserToken",
    "WTSRegisterSessionNotification",
    "WTSRegisterSessionNotificationEx",
    "WTSSBX_ADDRESS_FAMILY",
    "WTSSBX_ADDRESS_FAMILY_AF_INET",
    "WTSSBX_ADDRESS_FAMILY_AF_INET6",
    "WTSSBX_ADDRESS_FAMILY_AF_IPX",
    "WTSSBX_ADDRESS_FAMILY_AF_NETBIOS",
    "WTSSBX_ADDRESS_FAMILY_AF_UNSPEC",
    "WTSSBX_IP_ADDRESS",
    "WTSSBX_MACHINE_CONNECT_INFO",
    "WTSSBX_MACHINE_DRAIN",
    "WTSSBX_MACHINE_DRAIN_OFF",
    "WTSSBX_MACHINE_DRAIN_ON",
    "WTSSBX_MACHINE_DRAIN_UNSPEC",
    "WTSSBX_MACHINE_INFO",
    "WTSSBX_MACHINE_SESSION_MODE",
    "WTSSBX_MACHINE_SESSION_MODE_MULTIPLE",
    "WTSSBX_MACHINE_SESSION_MODE_SINGLE",
    "WTSSBX_MACHINE_SESSION_MODE_UNSPEC",
    "WTSSBX_MACHINE_STATE",
    "WTSSBX_MACHINE_STATE_READY",
    "WTSSBX_MACHINE_STATE_SYNCHRONIZING",
    "WTSSBX_MACHINE_STATE_UNSPEC",
    "WTSSBX_NOTIFICATION_ADDED",
    "WTSSBX_NOTIFICATION_CHANGED",
    "WTSSBX_NOTIFICATION_REMOVED",
    "WTSSBX_NOTIFICATION_RESYNC",
    "WTSSBX_NOTIFICATION_TYPE",
    "WTSSBX_SESSION_INFO",
    "WTSSBX_SESSION_STATE",
    "WTSSBX_SESSION_STATE_ACTIVE",
    "WTSSBX_SESSION_STATE_DISCONNECTED",
    "WTSSBX_SESSION_STATE_UNSPEC",
    "WTSSESSION_NOTIFICATION",
    "WTSSendMessageA",
    "WTSSendMessageW",
    "WTSSetListenerSecurityA",
    "WTSSetListenerSecurityW",
    "WTSSetRenderHint",
    "WTSSetUserConfigA",
    "WTSSetUserConfigW",
    "WTSShutdownSystem",
    "WTSStartRemoteControlSessionA",
    "WTSStartRemoteControlSessionW",
    "WTSStopRemoteControlSession",
    "WTSTerminateProcess",
    "WTSUSERCONFIGA",
    "WTSUSERCONFIGW",
    "WTSUnRegisterSessionNotification",
    "WTSUnRegisterSessionNotificationEx",
    "WTSVirtualChannelClose",
    "WTSVirtualChannelOpen",
    "WTSVirtualChannelOpenEx",
    "WTSVirtualChannelPurgeInput",
    "WTSVirtualChannelPurgeOutput",
    "WTSVirtualChannelQuery",
    "WTSVirtualChannelRead",
    "WTSVirtualChannelWrite",
    "WTSWaitSystemEvent",
    "WTS_CACHE_STATS",
    "WTS_CACHE_STATS_UN",
    "WTS_CERT_TYPE",
    "WTS_CERT_TYPE_INVALID",
    "WTS_CERT_TYPE_PROPRIETORY",
    "WTS_CERT_TYPE_X509",
    "WTS_CHANNEL_OPTION_DYNAMIC",
    "WTS_CHANNEL_OPTION_DYNAMIC_NO_COMPRESS",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_HIGH",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_LOW",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_MED",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_REAL",
    "WTS_CLIENTADDRESS_LENGTH",
    "WTS_CLIENTNAME_LENGTH",
    "WTS_CLIENT_ADDRESS",
    "WTS_CLIENT_DATA",
    "WTS_CLIENT_DISPLAY",
    "WTS_CLIENT_PRODUCT_ID_LENGTH",
    "WTS_COMMENT_LENGTH",
    "WTS_CONFIG_CLASS",
    "WTS_CONFIG_CLASS_WTSUserConfigBrokenTimeoutSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigInitialProgram",
    "WTS_CONFIG_CLASS_WTSUserConfigModemCallbackPhoneNumber",
    "WTS_CONFIG_CLASS_WTSUserConfigModemCallbackSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigReconnectSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigShadowingSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDir",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDirDrive",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerProfilePath",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsConnections",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsDisconnections",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsIdle",
    "WTS_CONFIG_CLASS_WTSUserConfigUser",
    "WTS_CONFIG_CLASS_WTSUserConfigWorkingDirectory",
    "WTS_CONFIG_CLASS_WTSUserConfigfAllowLogonTerminalServer",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDefaultPrinter",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDrives",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientPrinters",
    "WTS_CONFIG_CLASS_WTSUserConfigfInheritInitialProgram",
    "WTS_CONFIG_CLASS_WTSUserConfigfTerminalServerRemoteHomeDir",
    "WTS_CONFIG_SOURCE",
    "WTS_CONFIG_SOURCE_WTSUserConfigSourceSAM",
    "WTS_CONNECTSTATE_CLASS",
    "WTS_CONNECTSTATE_CLASS_WTSActive",
    "WTS_CONNECTSTATE_CLASS_WTSConnectQuery",
    "WTS_CONNECTSTATE_CLASS_WTSConnected",
    "WTS_CONNECTSTATE_CLASS_WTSDisconnected",
    "WTS_CONNECTSTATE_CLASS_WTSDown",
    "WTS_CONNECTSTATE_CLASS_WTSIdle",
    "WTS_CONNECTSTATE_CLASS_WTSInit",
    "WTS_CONNECTSTATE_CLASS_WTSListen",
    "WTS_CONNECTSTATE_CLASS_WTSReset",
    "WTS_CONNECTSTATE_CLASS_WTSShadow",
    "WTS_CURRENT_SERVER",
    "WTS_CURRENT_SERVER_HANDLE",
    "WTS_CURRENT_SERVER_NAME",
    "WTS_CURRENT_SESSION",
    "WTS_DEVICE_NAME_LENGTH",
    "WTS_DIRECTORY_LENGTH",
    "WTS_DISPLAY_IOCTL",
    "WTS_DOMAIN_LENGTH",
    "WTS_DRAIN_IN_DRAIN",
    "WTS_DRAIN_NOT_IN_DRAIN",
    "WTS_DRAIN_STATE_NONE",
    "WTS_DRIVER_NAME_LENGTH",
    "WTS_DRIVE_LENGTH",
    "WTS_EVENT_ALL",
    "WTS_EVENT_CONNECT",
    "WTS_EVENT_CREATE",
    "WTS_EVENT_DELETE",
    "WTS_EVENT_DISCONNECT",
    "WTS_EVENT_FLUSH",
    "WTS_EVENT_LICENSE",
    "WTS_EVENT_LOGOFF",
    "WTS_EVENT_LOGON",
    "WTS_EVENT_NONE",
    "WTS_EVENT_RENAME",
    "WTS_EVENT_STATECHANGE",
    "WTS_IMEFILENAME_LENGTH",
    "WTS_INFO_CLASS",
    "WTS_INFO_CLASS_WTSApplicationName",
    "WTS_INFO_CLASS_WTSClientAddress",
    "WTS_INFO_CLASS_WTSClientBuildNumber",
    "WTS_INFO_CLASS_WTSClientDirectory",
    "WTS_INFO_CLASS_WTSClientDisplay",
    "WTS_INFO_CLASS_WTSClientHardwareId",
    "WTS_INFO_CLASS_WTSClientInfo",
    "WTS_INFO_CLASS_WTSClientName",
    "WTS_INFO_CLASS_WTSClientProductId",
    "WTS_INFO_CLASS_WTSClientProtocolType",
    "WTS_INFO_CLASS_WTSConfigInfo",
    "WTS_INFO_CLASS_WTSConnectState",
    "WTS_INFO_CLASS_WTSDomainName",
    "WTS_INFO_CLASS_WTSIdleTime",
    "WTS_INFO_CLASS_WTSIncomingBytes",
    "WTS_INFO_CLASS_WTSIncomingFrames",
    "WTS_INFO_CLASS_WTSInitialProgram",
    "WTS_INFO_CLASS_WTSIsRemoteSession",
    "WTS_INFO_CLASS_WTSLogonTime",
    "WTS_INFO_CLASS_WTSOEMId",
    "WTS_INFO_CLASS_WTSOutgoingBytes",
    "WTS_INFO_CLASS_WTSOutgoingFrames",
    "WTS_INFO_CLASS_WTSSessionAddressV4",
    "WTS_INFO_CLASS_WTSSessionId",
    "WTS_INFO_CLASS_WTSSessionInfo",
    "WTS_INFO_CLASS_WTSSessionInfoEx",
    "WTS_INFO_CLASS_WTSUserName",
    "WTS_INFO_CLASS_WTSValidationInfo",
    "WTS_INFO_CLASS_WTSWinStationName",
    "WTS_INFO_CLASS_WTSWorkingDirectory",
    "WTS_INITIALPROGRAM_LENGTH",
    "WTS_KEY_EXCHANGE_ALG_DH",
    "WTS_KEY_EXCHANGE_ALG_RSA",
    "WTS_LICENSE_CAPABILITIES",
    "WTS_LICENSE_PREAMBLE_VERSION",
    "WTS_LICENSE_PROTOCOL_VERSION",
    "WTS_LISTENER_CREATE",
    "WTS_LISTENER_NAME_LENGTH",
    "WTS_LISTENER_UPDATE",
    "WTS_LOGON_ERROR_REDIRECTOR_RESPONSE",
    "WTS_LOGON_ERR_HANDLED_DONT_SHOW",
    "WTS_LOGON_ERR_HANDLED_DONT_SHOW_START_OVER",
    "WTS_LOGON_ERR_HANDLED_SHOW",
    "WTS_LOGON_ERR_INVALID",
    "WTS_LOGON_ERR_NOT_HANDLED",
    "WTS_MAX_CACHE_RESERVED",
    "WTS_MAX_COUNTERS",
    "WTS_MAX_DISPLAY_IOCTL_DATA",
    "WTS_MAX_PROTOCOL_CACHE",
    "WTS_MAX_RESERVED",
    "WTS_PASSWORD_LENGTH",
    "WTS_PERF_DISABLE_CURSORSETTINGS",
    "WTS_PERF_DISABLE_CURSOR_SHADOW",
    "WTS_PERF_DISABLE_FULLWINDOWDRAG",
    "WTS_PERF_DISABLE_MENUANIMATIONS",
    "WTS_PERF_DISABLE_NOTHING",
    "WTS_PERF_DISABLE_THEMING",
    "WTS_PERF_DISABLE_WALLPAPER",
    "WTS_PERF_ENABLE_DESKTOP_COMPOSITION",
    "WTS_PERF_ENABLE_ENHANCED_GRAPHICS",
    "WTS_PERF_ENABLE_FONT_SMOOTHING",
    "WTS_POLICY_DATA",
    "WTS_PROCESS_INFOA",
    "WTS_PROCESS_INFOW",
    "WTS_PROCESS_INFO_EXA",
    "WTS_PROCESS_INFO_EXW",
    "WTS_PROCESS_INFO_LEVEL_0",
    "WTS_PROCESS_INFO_LEVEL_1",
    "WTS_PROPERTY_DEFAULT_CONFIG",
    "WTS_PROPERTY_VALUE",
    "WTS_PROTOCOL_CACHE",
    "WTS_PROTOCOL_COUNTERS",
    "WTS_PROTOCOL_NAME_LENGTH",
    "WTS_PROTOCOL_STATUS",
    "WTS_PROTOCOL_TYPE_CONSOLE",
    "WTS_PROTOCOL_TYPE_ICA",
    "WTS_PROTOCOL_TYPE_RDP",
    "WTS_QUERY_ALLOWED_INITIAL_APP",
    "WTS_QUERY_AUDIOENUM_DLL",
    "WTS_QUERY_LOGON_SCREEN_SIZE",
    "WTS_QUERY_MF_FORMAT_SUPPORT",
    "WTS_RCM_DRAIN_STATE",
    "WTS_RCM_SERVICE_STATE",
    "WTS_SECURITY_ALL_ACCESS",
    "WTS_SECURITY_CONNECT",
    "WTS_SECURITY_CURRENT_GUEST_ACCESS",
    "WTS_SECURITY_CURRENT_USER_ACCESS",
    "WTS_SECURITY_DISCONNECT",
    "WTS_SECURITY_FLAGS",
    "WTS_SECURITY_GUEST_ACCESS",
    "WTS_SECURITY_LOGOFF",
    "WTS_SECURITY_LOGON",
    "WTS_SECURITY_MESSAGE",
    "WTS_SECURITY_QUERY_INFORMATION",
    "WTS_SECURITY_REMOTE_CONTROL",
    "WTS_SECURITY_RESET",
    "WTS_SECURITY_SET_INFORMATION",
    "WTS_SECURITY_USER_ACCESS",
    "WTS_SECURITY_VIRTUAL_CHANNELS",
    "WTS_SERVER_INFOA",
    "WTS_SERVER_INFOW",
    "WTS_SERVICE_NONE",
    "WTS_SERVICE_START",
    "WTS_SERVICE_STATE",
    "WTS_SERVICE_STOP",
    "WTS_SESSIONSTATE_LOCK",
    "WTS_SESSIONSTATE_UNKNOWN",
    "WTS_SESSIONSTATE_UNLOCK",
    "WTS_SESSION_ADDRESS",
    "WTS_SESSION_ID",
    "WTS_SESSION_INFOA",
    "WTS_SESSION_INFOW",
    "WTS_SESSION_INFO_1A",
    "WTS_SESSION_INFO_1W",
    "WTS_SMALL_RECT",
    "WTS_SOCKADDR",
    "WTS_SYSTEMTIME",
    "WTS_TIME_ZONE_INFORMATION",
    "WTS_TYPE_CLASS",
    "WTS_TYPE_CLASS_WTSTypeProcessInfoLevel0",
    "WTS_TYPE_CLASS_WTSTypeProcessInfoLevel1",
    "WTS_TYPE_CLASS_WTSTypeSessionInfoLevel1",
    "WTS_USERNAME_LENGTH",
    "WTS_USER_CREDENTIAL",
    "WTS_USER_DATA",
    "WTS_VALIDATION_INFORMATIONA",
    "WTS_VALIDATION_INFORMATIONW",
    "WTS_VALUE_TYPE_BINARY",
    "WTS_VALUE_TYPE_GUID",
    "WTS_VALUE_TYPE_STRING",
    "WTS_VALUE_TYPE_ULONG",
    "WTS_VIRTUAL_CLASS",
    "WTS_VIRTUAL_CLASS_WTSVirtualClientData",
    "WTS_VIRTUAL_CLASS_WTSVirtualFileHandle",
    "WTS_WSD_FASTREBOOT",
    "WTS_WSD_LOGOFF",
    "WTS_WSD_POWEROFF",
    "WTS_WSD_REBOOT",
    "WTS_WSD_SHUTDOWN",
    "Workspace",
    "_ITSWkspEvents",
    "pluginResource",
    "pluginResource2",
    "pluginResource2FileAssociation",
]
_arch_optional = [
]
