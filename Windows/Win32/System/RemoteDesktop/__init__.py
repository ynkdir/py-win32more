from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AAAccountingData(EasyCastStructure):
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
class AE_CURRENT_POSITION(EasyCastStructure):
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
def WTSSetRenderHint(pRenderHintID: POINTER(UInt64), hwndOwner: Windows.Win32.Foundation.HWND, renderHintType: UInt32, cbHintDataLength: UInt32, pHintData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ProcessIdToSessionId(dwProcessId: UInt32, pSessionId: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WTSGetActiveConsoleSessionId() -> UInt32: ...
class BITMAP_RENDERER_STATISTICS(EasyCastStructure):
    dwFramesDelivered: UInt32
    dwFramesDropped: UInt32
class CHANNEL_DEF(EasyCastStructure):
    name: Windows.Win32.Foundation.CHAR * 8
    options: UInt32
    _pack_ = 1
class CHANNEL_ENTRY_POINTS(EasyCastStructure):
    cbSize: UInt32
    protocolVersion: UInt32
    pVirtualChannelInit: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELINIT
    pVirtualChannelOpen: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELOPEN
    pVirtualChannelClose: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELCLOSE
    pVirtualChannelWrite: Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELWRITE
class CHANNEL_PDU_HEADER(EasyCastStructure):
    length: UInt32
    flags: UInt32
class CLIENT_DISPLAY(EasyCastStructure):
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
    def get_TerminalServicesProfilePath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TerminalServicesProfilePath(self, pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TerminalServicesHomeDirectory(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TerminalServicesHomeDirectory(self, pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TerminalServicesHomeDrive(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_TerminalServicesHomeDrive(self, pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowLogon(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowLogon(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableRemoteControl(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableRemoteControl(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MaxDisconnectionTime(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_MaxDisconnectionTime(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MaxConnectionTime(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_MaxConnectionTime(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_MaxIdleTime(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_MaxIdleTime(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ReconnectionAction(self, pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_ReconnectionAction(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_BrokenConnectionAction(self, pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_BrokenConnectionAction(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ConnectClientDrivesAtLogon(self, pNewVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ConnectClientDrivesAtLogon(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ConnectClientPrintersAtLogon(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ConnectClientPrintersAtLogon(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DefaultToMainPrinter(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_DefaultToMainPrinter(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_TerminalServicesWorkDirectory(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_TerminalServicesWorkDirectory(self, pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TerminalServicesInitialProgram(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_TerminalServicesInitialProgram(self, pNewVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioDeviceEndpoint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d4952f5a-a0b2-4cc4-8b-82-93-58-48-8d-d8-ac')
    @commethod(3)
    def SetBuffer(self, MaxPeriod: Int64, u32LatencyCoefficient: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRTCaps(self, pbIsRTCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventDrivenCapable(self, pbisEventCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteExclusiveModeParametersToSharedMemory(self, hTargetProcess: UIntPtr, hnsPeriod: Int64, hnsBufferDuration: Int64, u32LatencyCoefficient: UInt32, pu32SharedMemorySize: POINTER(UInt32), phSharedMemory: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpoint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30a99515-1527-4451-af-9f-00-c5-f0-23-4d-af')
    @commethod(3)
    def GetFrameFormat(self, ppFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesPerPacket(self, pFramesPerPacket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatency(self, pLatency: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStreamFlags(self, streamFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEventHandle(self, eventHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c684b72a-6df4-4774-bd-f9-76-b7-75-09-b6-53')
    @commethod(3)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfd2005f-a6e5-4d39-a2-65-93-9a-da-9f-bb-4d')
    @commethod(3)
    def GetCurrentPadding(self, pPadding: POINTER(Int64), pAeCurrentPosition: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> Void: ...
    @commethod(4)
    def ProcessingComplete(self) -> Void: ...
    @commethod(5)
    def SetPinInactive(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPinActive(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioInputEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8026ab61-92b2-43c1-a1-df-5c-37-eb-d0-8d-82')
    @commethod(3)
    def GetInputDataPointer(self, pConnectionProperty: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head), pAeTimeStamp: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> Void: ...
    @commethod(4)
    def ReleaseInputDataPointer(self, u32FrameCount: UInt32, pDataPointer: UIntPtr) -> Void: ...
    @commethod(5)
    def PulseEndpoint(self) -> Void: ...
class IAudioOutputEndpointRT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fa906e4-c31c-4e31-93-2e-19-a6-63-85-e9-aa')
    @commethod(3)
    def GetOutputDataPointer(self, u32FrameCount: UInt32, pAeTimeStamp: POINTER(Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION_head)) -> UIntPtr: ...
    @commethod(4)
    def ReleaseOutputDataPointer(self, pConnectionProperty: POINTER(Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head)) -> Void: ...
    @commethod(5)
    def PulseEndpoint(self) -> Void: ...
class IRemoteDesktopClient(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('57d25668-625a-4905-be-4e-30-4c-aa-13-f8-9c')
    @commethod(7)
    def Connect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reconnect(self, width: UInt32, height: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Settings(self, settings: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(self, actions: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientActions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TouchPointer(self, touchPointer: POINTER(Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientTouchPointer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteSavedCredentials(self, serverName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateSessionDisplaySettings(self, width: UInt32, height: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def attachEvent(self, eventName: Windows.Win32.Foundation.BSTR, callback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def detachEvent(self, eventName: Windows.Win32.Foundation.BSTR, callback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientActions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7d54bc4e-1028-45d4-8b-0a-b9-b6-bf-fb-a1-76')
    @commethod(7)
    def SuspendScreenUpdates(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResumeScreenUpdates(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ExecuteRemoteAction(self, remoteAction: Windows.Win32.System.RemoteDesktop.RemoteActionType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSnapshot(self, snapshotEncoding: Windows.Win32.System.RemoteDesktop.SnapshotEncodingType, snapshotFormat: Windows.Win32.System.RemoteDesktop.SnapshotFormatType, snapshotWidth: UInt32, snapshotHeight: UInt32, snapshotData: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientSettings(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('48a0f2a7-2713-431f-bb-ac-6f-45-58-e7-d6-4d')
    @commethod(7)
    def ApplySettings(self, rdpFileContents: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveSettings(self, rdpFileContents: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRdpProperty(self, propertyName: Windows.Win32.Foundation.BSTR, value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRdpProperty(self, propertyName: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientTouchPointer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('260ec22d-8cbc-44b5-9e-88-2a-37-f6-c9-3a-e9')
    @commethod(7)
    def put_Enabled(self, enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Enabled(self, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_EventsEnabled(self, eventsEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventsEnabled(self, eventsEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_PointerSpeed(self, pointerSpeed: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PointerSpeed(self, pointerSpeed: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteSystemAdditionalInfoProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eeaa3d5f-ec63-4d27-af-38-e8-6b-1d-72-92-cb')
    @commethod(3)
    def GetAdditionalInfo(self, deduplicationId: POINTER(Windows.Win32.System.WinRT.HSTRING), riid: POINTER(Guid), mapView: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAccountingEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ce2a0c9-e874-4f1a-86-f4-06-bb-b9-11-53-38')
    @commethod(3)
    def DoAccounting(self, accountingDataType: Windows.Win32.System.RemoteDesktop.AAAccountingDataType, accountingData: Windows.Win32.System.RemoteDesktop.AAAccountingData) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticateUserSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2c3e2e73-a782-47f9-8d-fb-77-ee-1e-d2-7a-03')
    @commethod(3)
    def OnUserAuthenticated(self, userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, context: UIntPtr, userToken: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUserAuthenticationFailed(self, context: UIntPtr, genericErrorCode: Windows.Win32.Foundation.HRESULT, specificErrorCode: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReauthenticateUser(self, context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisconnectUser(self, context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticationEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ee3e5bf-04ab-4691-99-8c-d7-f6-22-32-1a-56')
    @commethod(3)
    def AuthenticateUser(self, mainSessionId: Guid, cookieData: POINTER(Byte), numCookieBytes: UInt32, context: UIntPtr, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthenticateUserSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelAuthentication(self, mainSessionId: Guid, context: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeConnectionSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c27ece33-7781-4318-98-ef-1c-f2-da-7b-70-05')
    @commethod(3)
    def OnConnectionAuthorized(self, hrIn: Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, cbSoHResponse: UInt32, pbSoHResponse: POINTER(Byte), idleTimeout: UInt32, sessionTimeout: UInt32, sessionTimeoutAction: Windows.Win32.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE, trustClass: Windows.Win32.System.RemoteDesktop.AATrustClassID, policyAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeResourceSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('feddfcd4-fa12-4435-ae-55-7a-d1-a9-77-9a-f7')
    @commethod(3)
    def OnChannelAuthorized(self, hrIn: Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, subSessionId: Int32, allowedResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numAllowedResourceNames: UInt32, failedResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numFailedResourceNames: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITSGPolicyEngine(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8bc24f08-6223-42f4-a5-b4-8e-37-cd-13-5b-bd')
    @commethod(3)
    def AuthorizeConnection(self, mainSessionId: Guid, username: Windows.Win32.Foundation.BSTR, authType: Windows.Win32.System.RemoteDesktop.AAAuthSchemes, clientMachineIP: Windows.Win32.Foundation.BSTR, clientMachineName: Windows.Win32.Foundation.BSTR, sohData: POINTER(Byte), numSOHBytes: UInt32, cookieData: POINTER(Byte), numCookieBytes: UInt32, userToken: Windows.Win32.Foundation.HANDLE_PTR, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthorizeConnectionSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AuthorizeResource(self, mainSessionId: Guid, subSessionId: Int32, username: Windows.Win32.Foundation.BSTR, resourceNames: POINTER(Windows.Win32.Foundation.BSTR), numResources: UInt32, alternateResourceNames: POINTER(Windows.Win32.Foundation.BSTR), numAlternateResourceName: UInt32, portNumber: UInt32, operation: Windows.Win32.Foundation.BSTR, cookie: POINTER(Byte), numBytesInCookie: UInt32, pSink: Windows.Win32.System.RemoteDesktop.ITSGAuthorizeResourceSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsQuarantineEnabled(self, quarantineEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbBaseNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('808a6537-1282-4989-9e-09-f4-39-38-b7-17-22')
    @commethod(3)
    def OnError(self, hrError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReportStatus(self, messageType: Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE, messageID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('18857499-ad61-4b1b-b7-df-cb-cd-41-fb-83-38')
    @commethod(3)
    def get_UserName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Domain(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_InitialProgram(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_LoadBalanceResult(self, ppVal: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_FarmName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutContext(self, contextId: Windows.Win32.Foundation.BSTR, context: Windows.Win32.System.Com.VARIANT, existingContext: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContext(self, contextId: Windows.Win32.Foundation.BSTR, context: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Environment(self, ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ConnectionError(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SamUserAccount(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClientConnectionPropertySet(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbClientConnectionPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsFirstAssignment(self, ppVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RdFarmType(self, pRdFarmType: POINTER(Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserSidString(self, pszUserSidString: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDisconnectedSession(self, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnectionPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('e51995b0-46d6-11dd-aa-21-ce-dc-55-d8-95-93')
class ITsSbEnvironment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8c87f7f7-bf51-4a5c-87-bf-8e-94-fb-6e-22-56')
    @commethod(3)
    def get_Name(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ServerWeight(self, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EnvironmentPropertySet(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_EnvironmentPropertySet(self, pVal: Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbEnvironmentPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('d0d1bf7e-7acf-11dd-a2-43-e5-11-56-d8-95-93')
class ITsSbFilterPluginStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85b44b0f-ed78-413f-97-02-fa-6d-3b-5e-e7-55')
    @commethod(3)
    def SaveProperties(self, pPropertySet: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateProperties(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteProperties(self, propertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbGenericNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4c4c8c4f-300b-46ad-91-64-84-68-a7-e7-56-8c')
    @commethod(3)
    def OnCompleted(self, Status: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWaitTimeout(self, pftTimeout: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbGlobalStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ab60f7b-bd72-4d9f-8a-3a-a0-ea-55-74-e6-35')
    @commethod(3)
    def QueryTarget(self, ProviderName: Windows.Win32.Foundation.BSTR, TargetName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(self, ProviderName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32, TargetName: Windows.Win32.Foundation.BSTR, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateFarms(self, ProviderName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateTargets(self, ProviderName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, EnvName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateEnvironmentsByProvider(self, ProviderName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumerateSessions(self, ProviderName: Windows.Win32.Foundation.BSTR, targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, pSessionState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFarmProperty(self, farmName: Windows.Win32.Foundation.BSTR, propertyName: Windows.Win32.Foundation.BSTR, pVarValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalanceResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('24fdb7ac-fea6-11dc-96-72-9a-89-56-d8-95-93')
    @commethod(3)
    def get_TargetName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancing(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('24329274-9eb7-11dc-ae-98-f2-b4-56-d8-95-93')
    @commethod(5)
    def GetMostSuitableTarget(self, pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pLBSink: Windows.Win32.System.RemoteDesktop.ITsSbLoadBalancingNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancingNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('5f8a8297-3244-4e6a-95-8a-27-c8-22-c1-e1-41')
    @commethod(5)
    def OnGetMostSuitableTarget(self, pLBResult: Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head, fIsNewConnection: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestration(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('64fc1172-9eb7-11dc-8b-00-3a-ba-56-d8-95-93')
    @commethod(5)
    def PrepareTargetForConnect(self, pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pOrchestrationNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbOrchestrationNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestrationNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('36c37d61-926b-442f-bc-a5-11-8c-6d-50-dc-f2')
    @commethod(5)
    def OnReadyToConnect(self, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacement(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('daadee5f-6d32-480e-9e-36-dd-ab-23-29-f0-6d')
    @commethod(5)
    def QueryEnvironmentForTarget(self, pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head, pPlacementSink: Windows.Win32.System.RemoteDesktop.ITsSbPlacementNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacementNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('68a0c487-2b4f-46c2-94-a1-6c-e6-85-18-36-34')
    @commethod(5)
    def OnQueryEnvironmentCompleted(self, pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('48cd7406-caab-465f-a5-d6-ba-a8-63-b9-ea-4f')
    @commethod(3)
    def Initialize(self, pProvider: Windows.Win32.System.RemoteDesktop.ITsSbProvider_head, pNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbPluginNotifySink_head, pPropertySet: Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(self, hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('44dfe30b-c3be-40f5-bf-82-7a-95-bb-79-5a-df')
    @commethod(5)
    def OnInitialized(self, hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTerminated(self) -> Windows.Win32.Foundation.HRESULT: ...
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
    def CreateTargetObject(self, TargetName: Windows.Win32.Foundation.BSTR, EnvironmentName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateLoadBalanceResultObject(self, TargetName: Windows.Win32.Foundation.BSTR, ppLBResult: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateSessionObject(self, TargetName: Windows.Win32.Foundation.BSTR, UserName: Windows.Win32.Foundation.BSTR, Domain: Windows.Win32.Foundation.BSTR, SessionId: UInt32, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreatePluginPropertySet(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateTargetPropertySetObject(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEnvironmentObject(self, Name: Windows.Win32.Foundation.BSTR, ServerWeight: UInt32, ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetResourcePluginStore(self, ppStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbResourcePluginStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilterPluginStore(self, ppStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbFilterPluginStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterForNotification(self, notificationType: UInt32, ResourceToMonitor: Windows.Win32.Foundation.BSTR, pPluginNotification: Windows.Win32.System.RemoteDesktop.ITsSbResourceNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnRegisterForNotification(self, notificationType: UInt32, ResourceToMonitor: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceOfGlobalStore(self, ppGlobalStore: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbGlobalStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateEnvironmentPropertySetObject(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioning(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('2f6f0dbb-9e4f-462b-9c-3f-fc-cc-3d-cb-62-32')
    @commethod(5)
    def CreateVirtualMachines(self, JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PatchVirtualMachines(self, JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head, pVMPatchInfo: POINTER(Windows.Win32.System.RemoteDesktop.VM_PATCH_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteVirtualMachines(self, JobXmlString: Windows.Win32.Foundation.BSTR, JobGuid: Windows.Win32.Foundation.BSTR, pSink: Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelJob(self, JobGuid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioningPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('aca87a8e-818b-4581-a0-32-49-c3-df-b9-c7-01')
    @commethod(3)
    def OnJobCreated(self, pVmNotifyInfo: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnVirtualMachineStatusChanged(self, pVmNotifyEntry: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head), VmNotifyStatus: Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS, ErrorCode: Windows.Win32.Foundation.HRESULT, ErrorDescr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnJobCompleted(self, ResultCode: Windows.Win32.Foundation.HRESULT, ResultDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnJobCancelled(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockVirtualMachine(self, pVmNotifyEntry: POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnVirtualMachineHostStatusChanged(self, VmHost: Windows.Win32.Foundation.BSTR, VmHostNotifyStatus: Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS, ErrorCode: Windows.Win32.Foundation.HRESULT, ErrorDescr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('65d3e85a-c39b-11dc-b9-2d-3c-d2-55-d8-95-93')
    @commethod(3)
    def NotifySessionChange(self, changeType: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE, pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChange(self, TargetChangeType: UInt32, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChange(self, ChangeType: Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION, pConnection: Windows.Win32.System.RemoteDesktop.ITsSbClientConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotificationEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8a47fde-ca91-44d2-b8-97-3a-a2-8a-43-b2-b7')
    @commethod(3)
    def NotifySessionChangeEx(self, targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, domain: Windows.Win32.Foundation.BSTR, sessionId: UInt32, sessionState: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChangeEx(self, targetName: Windows.Win32.Foundation.BSTR, targetChangeType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChangeEx(self, userName: Windows.Win32.Foundation.BSTR, domain: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, targetName: Windows.Win32.Foundation.BSTR, connectionChangeType: Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourcePlugin(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('ea8db42c-98ed-4535-a8-8b-2a-16-4f-35-49-0f')
class ITsSbResourcePluginStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5c38f65f-bcf1-4036-a6-bf-9e-3c-cc-ae-0b-63')
    @commethod(3)
    def QueryTarget(self, TargetName: Windows.Win32.Foundation.BSTR, FarmName: Windows.Win32.Foundation.BSTR, ppTarget: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(self, dwSessionId: UInt32, TargetName: Windows.Win32.Foundation.BSTR, ppSession: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddTargetToStore(self, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddSessionToStore(self, pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddEnvironmentToStore(self, pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveEnvironmentFromStore(self, EnvironmentName: Windows.Win32.Foundation.BSTR, bIgnoreOwner: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateFarms(self, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryEnvironment(self, EnvironmentName: Windows.Win32.Foundation.BSTR, ppEnvironment: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumerateEnvironments(self, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveTarget(self, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head, bForceWrite: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveEnvironment(self, pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head, bForceWrite: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SaveSession(self, pSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetTargetProperty(self, TargetName: Windows.Win32.Foundation.BSTR, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEnvironmentProperty(self, EnvironmentName: Windows.Win32.Foundation.BSTR, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTargetState(self, targetName: Windows.Win32.Foundation.BSTR, newState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, pOldState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetSessionState(self, sbSession: Windows.Win32.System.RemoteDesktop.ITsSbSession_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnumerateTargets(self, FarmName: Windows.Win32.Foundation.BSTR, EnvName: Windows.Win32.Foundation.BSTR, sortByFieldId: Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY, sortyByPropName: Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTarget_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnumerateSessions(self, targetName: Windows.Win32.Foundation.BSTR, userName: Windows.Win32.Foundation.BSTR, userDomain: Windows.Win32.Foundation.BSTR, poolName: Windows.Win32.Foundation.BSTR, initialProgram: Windows.Win32.Foundation.BSTR, pSessionState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.ITsSbSession_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFarmProperty(self, farmName: Windows.Win32.Foundation.BSTR, propertyName: Windows.Win32.Foundation.BSTR, pVarValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteTarget(self, targetName: Windows.Win32.Foundation.BSTR, hostName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetTargetPropertyWithVersionCheck(self, pTarget: Windows.Win32.System.RemoteDesktop.ITsSbTarget_head, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetEnvironmentPropertyWithVersionCheck(self, pEnvironment: Windows.Win32.System.RemoteDesktop.ITsSbEnvironment_head, PropertyName: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AcquireTargetLock(self, targetName: Windows.Win32.Foundation.BSTR, dwTimeout: UInt32, ppContext: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ReleaseTargetLock(self, pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def TestAndSetServerState(self, PoolName: Windows.Win32.Foundation.BSTR, ServerFQDN: Windows.Win32.Foundation.BSTR, NewState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, TestState: Windows.Win32.System.RemoteDesktop.TARGET_STATE, pInitState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetServerWaitingToStart(self, PoolName: Windows.Win32.Foundation.BSTR, serverName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetServerState(self, PoolName: Windows.Win32.Foundation.BSTR, ServerFQDN: Windows.Win32.Foundation.BSTR, pState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetServerDrainMode(self, ServerFQDN: Windows.Win32.Foundation.BSTR, DrainMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbServiceNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('86cb68ae-86e0-4f57-8a-64-bb-74-06-bc-55-50')
    @commethod(3)
    def NotifyServiceFailure(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceSuccess(self) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbSession(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d453aac7-b1d8-4c5e-ba-34-9a-fb-4c-8c-55-10')
    @commethod(3)
    def get_SessionId(self, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TargetName(self, targetName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_TargetName(self, targetName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Username(self, userName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Domain(self, domain: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(self, pState: POINTER(Windows.Win32.System.RemoteDesktop.TSSESSION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(self, State: Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CreateTime(self, pTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_CreateTime(self, Time: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DisconnectTime(self, pTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DisconnectTime(self, Time: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InitialProgram(self, app: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_InitialProgram(self, Application: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ClientDisplay(self, pClientDisplay: POINTER(Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ClientDisplay(self, pClientDisplay: Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ProtocolType(self, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ProtocolType(self, Val: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('16616ecc-272d-411d-b3-24-12-68-93-03-38-56')
    @commethod(3)
    def get_TargetName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TargetName(self, Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_FarmName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_FarmName(self, Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_TargetFQDN(self, TargetFqdnName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TargetFQDN(self, Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TargetNetbios(self, TargetNetbiosName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TargetNetbios(self, Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddresses(self, SOCKADDR: POINTER(Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint_head), numAddresses: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddresses(self, SOCKADDR: POINTER(Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint_head), numAddresses: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TargetState(self, pState: POINTER(Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_TargetState(self, State: Windows.Win32.System.RemoteDesktop.TARGET_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TargetPropertySet(self, ppPropertySet: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_TargetPropertySet(self, pVal: Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EnvironmentName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_EnvironmentName(self, Val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_NumSessions(self, pNumSessions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_NumPendingConnections(self, pNumPendingConnections: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TargetLoad(self, pTargetLoad: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTargetPropertySet(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    Guid = Guid('f7bda5d6-994c-4e11-a0-79-27-63-b6-18-30-ac')
class ITsSbTaskInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('523d1083-89be-48dd-99-ea-04-e8-2f-fa-72-65')
    @commethod(3)
    def get_TargetId(self, pName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StartTime(self, pStartTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EndTime(self, pEndTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Deadline(self, pDeadline: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Identifier(self, pIdentifier: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Label(self, pLabel: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Context(self, pContext: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Plugin(self, pPlugin: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(self, pStatus: POINTER(Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPlugin(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    Guid = Guid('fa22ef0f-8705-41be-93-bc-44-bd-bc-f1-c9-c4')
    @commethod(5)
    def InitializeTaskPlugin(self, pITsSbTaskPluginNotifySink: Windows.Win32.System.RemoteDesktop.ITsSbTaskPluginNotifySink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTaskQueue(self, pszHostName: Windows.Win32.Foundation.BSTR, SbTaskInfoSize: UInt32, pITsSbTaskInfo: POINTER(Windows.Win32.System.RemoteDesktop.ITsSbTaskInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPluginNotifySink(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    Guid = Guid('6aaf899e-c2ec-45ee-aa-37-45-e6-08-95-26-1a')
    @commethod(5)
    def OnSetTaskTime(self, szTargetName: Windows.Win32.Foundation.BSTR, TaskStartTime: Windows.Win32.Foundation.FILETIME, TaskEndTime: Windows.Win32.Foundation.FILETIME, TaskDeadline: Windows.Win32.Foundation.FILETIME, szTaskLabel: Windows.Win32.Foundation.BSTR, szTaskIdentifier: Windows.Win32.Foundation.BSTR, szTaskPlugin: Windows.Win32.Foundation.BSTR, dwTaskStatus: UInt32, saContext: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDeleteTaskTime(self, szTargetName: Windows.Win32.Foundation.BSTR, szTaskIdentifier: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUpdateTaskStatus(self, szTargetName: Windows.Win32.Foundation.BSTR, TaskIdentifier: Windows.Win32.Foundation.BSTR, TaskStatus: Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnReportTasks(self, szHostName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsEnhancedFastReconnectArbitrator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5718ae9b-47f2-499f-b6-34-d8-17-5b-d5-11-31')
    @commethod(3)
    def GetSessionForEnhancedFastReconnect(self, pSessionIdArray: POINTER(Int32), dwSessionCount: UInt32, pResultSessionId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('684b7a0b-edff-43ad-d5-a2-4a-8d-53-88-f4-01')
    @commethod(3)
    def Write(self, cbSize: UInt32, pBuffer: POINTER(Byte), pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Open(self, pChannelEvents: Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannelEvents_head, pOpenContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('67f2368c-d674-4fae-66-a5-d2-06-28-a6-40-d2')
    @commethod(3)
    def OnDataReceived(self, cbSize: UInt32, pBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChannelOpened(self, OpenResult: Windows.Win32.Foundation.HRESULT, pOpenContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDataSent(self, pWriteContext: Windows.Win32.System.Com.IUnknown_head, bCancelled: Windows.Win32.Foundation.BOOL, pBuffer: POINTER(Byte), cbBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnMetricsUpdate(self, bandwidth: UInt32, RTT: UInt32, lastSentByteIndex: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0fd57159-e83e-476a-a8-b9-4a-79-76-e7-1e-18')
    @commethod(3)
    def CreateChannel(self, pszChannelName: POINTER(Byte), channelType: Windows.Win32.System.RemoteDesktop.WRdsGraphicsChannelType, ppVirtualChannel: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('324ed94f-fdaf-4ff6-81-a8-42-ab-e7-55-83-0b')
    @commethod(3)
    def GetLogonErrorRedirector(self, ppLogonErrorRedir: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolLogonErrorRedirector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AcceptConnection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClientData(self, pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientMonitorData(self, pNumMonitors: POINTER(UInt32), pPrimaryMonitor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(self, pUserCreds: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(self, ppLicenseConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolLicenseConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), SessionHandle: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputHandles(self, pKeyboardHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetVideoHandle(self, pVideoHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConnectNotify(self, SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUserAllowedToLogon(self, SessionId: UInt32, UserToken: Windows.Win32.Foundation.HANDLE_PTR, pDomainName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SessionArbitrationEnumeration(self, hUserToken: Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LogonNotify(self, hClientToken: Windows.Win32.Foundation.HANDLE_PTR, wszUserName: Windows.Win32.Foundation.PWSTR, wszDomainName: Windows.Win32.Foundation.PWSTR, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PreDisconnect(self, DisconnectReason: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisconnectNotify(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetProtocolStatus(self, pProtocolStatus: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetLastInputTime(self, pLastInputTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetErrorInfo(self, ulError: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(self, szEndpointName: Windows.Win32.Foundation.PSTR, bStatic: Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(self, QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(self, ppShadowConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyCommandProcessCreated(self, SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1d70332-d070-4ef1-a0-88-78-31-35-36-c2-d6')
    @commethod(3)
    def OnReady(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(self, Reason: UInt32, Source: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(self, rect: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionId(self, pConnectionId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('83fcf5d3-f6f4-ea94-9c-d2-32-f2-80-e1-e5-10')
    @commethod(3)
    def SetConnectionSetting(self, PropertyID: Guid, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionSetting(self, PropertyID: Guid, pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLicenseConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1d6a145f-d095-4424-95-7a-40-7f-ae-82-2d-84')
    @commethod(3)
    def RequestLicensingCapabilities(self, ppLicenseCapabilities: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head), pcbLicenseCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(self, pClientLicense: POINTER(Byte), cbClientLicense: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(self, Reserve1: POINTER(Byte), Reserve2: UInt32, ppClientLicense: POINTER(Byte), pcbClientLicense: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(self, ulComplete: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fcbc131b-c686-451d-a7-73-e2-79-e2-30-f5-40')
    @commethod(3)
    def GetSettings(self, WRdsListenerSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL, pWRdsListenerSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartListen(self, pCallback: Windows.Win32.System.RemoteDesktop.IWRdsProtocolListenerCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopListen(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3ab27e5b-4449-4dc1-b7-4a-91-62-1d-4f-e9-84')
    @commethod(3)
    def OnConnected(self, pConnection: Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnection_head, pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head), pCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnectionCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLogonErrorRedirector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('519fe83b-142a-4120-a3-d5-a4-05-d3-15-28-1a')
    @commethod(3)
    def OnBeginPainting(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(self, pszMessage: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(self, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(self, ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dc796967-3abb-40cd-a4-46-10-52-76-b5-89-50')
    @commethod(3)
    def Initialize(self, pIWRdsSettings: Windows.Win32.System.RemoteDesktop.IWRdsProtocolSettings_head, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateListener(self, wszListenerName: Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(Windows.Win32.System.RemoteDesktop.IWRdsProtocolListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyServiceStateChange(self, pTSServiceStateChange: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStart(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionOfServiceStop(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifySessionStateChange(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), EventId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NotifySettingsChange(self, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Uninitialize(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('654a5a6a-2550-47eb-b6-f7-eb-d6-37-47-52-65')
    @commethod(3)
    def GetSettings(self, WRdsSettingType: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE, WRdsSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MergeSettings(self, pWRdsSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_head), WRdsConnectionSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL, pWRdsConnectionSettings: POINTER(Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e0667ce0-0372-40d6-ad-b2-a0-f3-32-26-74-d6')
    @commethod(3)
    def StopShadow(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(self, pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ae85ce6-cade-4548-8f-eb-99-01-65-97-f6-0a')
    @commethod(3)
    def Start(self, pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(self, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWRdsWddmIddProps(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1382df4d-a289-43d1-a1-84-14-47-26-f9-af-90')
    @commethod(3)
    def GetHardwareId(self, pDisplayDriverHardwareId: Windows.Win32.Foundation.PWSTR, Count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDriverLoad(self, SessionId: UInt32, DriverHandle: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDriverUnload(self, SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableWddmIdd(self, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ea326091-05fe-40c1-b4-9c-3d-2e-f4-62-6a-0e')
    @commethod(3)
    def GetMappedRenderer(self, mappingId: UInt64, pMappedRendererCallback: Windows.Win32.System.RemoteDesktop.IWTSBitmapRendererCallback_head, ppMappedRenderer: POINTER(Windows.Win32.System.RemoteDesktop.IWTSBitmapRenderer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b7acc97-f3c9-46f7-8c-5b-fa-68-5d-34-41-b1')
    @commethod(3)
    def Render(self, imageFormat: Guid, dwWidth: UInt32, dwHeight: UInt32, cbStride: Int32, cbImageBuffer: UInt32, pImageBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRendererStatistics(self, pStatistics: POINTER(Windows.Win32.System.RemoteDesktop.BITMAP_RENDERER_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveMapping(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRendererCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d782928e-fe4e-4e77-ae-90-9c-d0-b3-e3-b3-53')
    @commethod(3)
    def OnTargetSizeChanged(self, rcNewSize: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230206-9a39-4d58-86-74-cd-b4-df-f4-e7-3b')
    @commethod(3)
    def GetConfiguration(self, ppPropertyBag: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230203-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def OnNewChannelConnection(self, pChannel: Windows.Win32.System.RemoteDesktop.IWTSVirtualChannel_head, data: Windows.Win32.Foundation.BSTR, pbAccept: POINTER(Windows.Win32.Foundation.BOOL), ppCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230201-1439-4e62-a4-14-19-0d-0a-c3-d4-0e')
    @commethod(3)
    def Initialize(self, pChannelMgr: Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connected(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnected(self, dwDisconnectCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminated(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSPluginServiceProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d3e07363-087c-476c-86-a7-db-b1-5f-46-dd-b4')
    @commethod(3)
    def GetService(self, ServiceId: Guid, ppunkObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-9095-4648-98-bf-ef-81-c9-14-03-2d')
    @commethod(3)
    def GetLogonErrorRedirector(self, ppLogonErrorRedir: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolLogonErrorRedirector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendPolicyData(self, pPolicyData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AcceptConnection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientData(self, pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(self, pUserCreds: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(self, ppLicenseConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolLicenseConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProtocolHandles(self, pKeyboardHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR), pVideoHandle: POINTER(Windows.Win32.Foundation.HANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ConnectNotify(self, SessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsUserAllowedToLogon(self, SessionId: UInt32, UserToken: Windows.Win32.Foundation.HANDLE_PTR, pDomainName: Windows.Win32.Foundation.PWSTR, pUserName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SessionArbitrationEnumeration(self, hUserToken: Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LogonNotify(self, hClientToken: Windows.Win32.Foundation.HANDLE_PTR, wszUserName: Windows.Win32.Foundation.PWSTR, wszDomainName: Windows.Win32.Foundation.PWSTR, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserData(self, pPolicyData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA_head), pClientData: POINTER(Windows.Win32.System.RemoteDesktop.WTS_USER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DisconnectNotify(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetProtocolStatus(self, pProtocolStatus: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetLastInputTime(self, pLastInputTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetErrorInfo(self, ulError: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SendBeep(self, Frequency: UInt32, Duration: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(self, szEndpointName: Windows.Win32.Foundation.PSTR, bStatic: Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(self, QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), pPropertyEntriesOut: POINTER(Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(self, ppShadowConnection: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnectionCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-75eb-41fe-b4-fb-e0-86-24-2a-fa-0f')
    @commethod(3)
    def OnReady(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(self, Reason: UInt32, Source: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(self, rect: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DisplayIOCtl(self, DisplayIOCtl: POINTER(Windows.Win32.System.RemoteDesktop.WTS_DISPLAY_IOCTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLicenseConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-178c-4079-8e-4a-fe-a6-49-6a-4d-70')
    @commethod(3)
    def RequestLicensingCapabilities(self, ppLicenseCapabilities: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head), pcbLicenseCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(self, pClientLicense: POINTER(Byte), cbClientLicense: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(self, Reserve1: POINTER(Byte), Reserve2: UInt32, ppClientLicense: POINTER(Byte), pcbClientLicense: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(self, ulComplete: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListener(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-45f0-4394-8f-69-32-b2-bc-0e-f4-ca')
    @commethod(3)
    def StartListen(self, pCallback: Windows.Win32.System.RemoteDesktop.IWTSProtocolListenerCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopListen(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListenerCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23083765-1a2d-4de2-97-de-4a-35-f2-60-f0-b3')
    @commethod(3)
    def OnConnected(self, pConnection: Windows.Win32.System.RemoteDesktop.IWTSProtocolConnection_head, pCallback: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolConnectionCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLogonErrorRedirector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd9b61a7-2916-4627-8d-ee-43-28-71-1a-d6-cb')
    @commethod(3)
    def OnBeginPainting(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(self, pszMessage: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(self, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(self, ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: Windows.Win32.Foundation.PWSTR, pszMessage: Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9eaf6cc-ed79-4f01-82-1d-1f-88-1b-9f-66-cc')
    @commethod(3)
    def CreateListener(self, wszListenerName: Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(Windows.Win32.System.RemoteDesktop.IWTSProtocolListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceStateChange(self, pTSServiceStateChange: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifySessionOfServiceStart(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStop(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionStateChange(self, SessionId: POINTER(Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID_head), EventId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('503a2504-aae5-4ab1-93-e0-6d-1c-4b-c6-f7-1a')
    @commethod(3)
    def StopShadow(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(self, pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ee3b0c14-37fb-456b-ba-b3-6d-6c-d5-1e-13-bf')
    @commethod(3)
    def Start(self, pTargetServerName: Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(self, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSSBPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dc44be78-b18d-4399-b2-10-64-1b-f6-7a-00-2c')
    @commethod(3)
    def Initialize(self, PluginCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WTSSBX_MachineChangeNotification(self, NotificationType: Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, pMachineInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WTSSBX_SessionChangeNotification(self, NotificationType: Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, NumOfSessions: UInt32, SessionInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WTSSBX_GetMostSuitableServer(self, UserName: Windows.Win32.Foundation.PWSTR, DomainName: Windows.Win32.Foundation.PWSTR, ApplicationType: Windows.Win32.Foundation.PWSTR, FarmName: Windows.Win32.Foundation.PWSTR, pMachineId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Terminated(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WTSSBX_GetUserExternalSession(self, UserName: Windows.Win32.Foundation.PWSTR, DomainName: Windows.Win32.Foundation.PWSTR, ApplicationType: Windows.Win32.Foundation.PWSTR, RedirectorInternalIP: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS_head), pSessionId: POINTER(UInt32), pMachineConnectInfo: POINTER(Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230207-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def Write(self, cbSize: UInt32, pBuffer: POINTER(Byte), pReserved: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230204-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def OnDataReceived(self, cbSize: UInt32, pBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a1230205-d6a7-11d8-b9-fd-00-0b-db-d1-f1-98')
    @commethod(3)
    def CreateListener(self, pszChannelName: Windows.Win32.Foundation.PSTR, uFlags: UInt32, pListenerCallback: Windows.Win32.System.RemoteDesktop.IWTSListenerCallback_head, ppListener: POINTER(Windows.Win32.System.RemoteDesktop.IWTSListener_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b922bbb8-4c55-4fea-84-96-be-b0-b4-42-85-e5')
    @commethod(3)
    def GetWorkspaceNames(self, psaWkspNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartRemoteApplication(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, psaParams: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProcessId(self, pulProcessId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspace
    Guid = Guid('96d8d7cf-783e-4286-83-4c-eb-c0-e9-5f-78-3c')
    @commethod(6)
    def StartRemoteApplicationEx(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrRequestingAppId: Windows.Win32.Foundation.BSTR, bstrRequestingAppFamilyName: Windows.Win32.Foundation.BSTR, bLaunchIntoImmersiveClient: Windows.Win32.Foundation.VARIANT_BOOL, bstrImmersiveClientActivationContext: Windows.Win32.Foundation.BSTR, psaParams: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspace3(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspace2
    Guid = Guid('1becbe4a-d654-423b-af-eb-be-8d-53-2c-13-c6')
    @commethod(7)
    def GetClaimsToken2(self, bstrClaimsHint: Windows.Win32.Foundation.BSTR, bstrUserHint: Windows.Win32.Foundation.BSTR, claimCookie: UInt32, hwndCredUiParent: UInt32, rectCredUiParent: Windows.Win32.Foundation.RECT, pbstrAccessToken: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetClaimsToken(self, bstrAccessToken: Windows.Win32.Foundation.BSTR, ullAccessTokenExpiration: UInt64, bstrRefreshToken: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceClientExt(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12b952f4-41ca-4f21-a8-29-a6-d0-7d-9a-16-e5')
    @commethod(3)
    def GetResourceId(self, bstrWorkspaceId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResourceDisplayName(self, bstrWorkspaceDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IssueDisconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b922bbb8-4c55-4fea-84-96-be-b0-b4-42-85-e6')
    @commethod(3)
    def AddResource(self, pUnk: Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveResource(self, dwCookieConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceRegistration
    Guid = Guid('cf59f654-39bb-44d8-94-d0-46-35-72-89-57-e9')
    @commethod(5)
    def AddResourceEx(self, pUnk: Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt_head, bstrEventLogUploadAddress: Windows.Win32.Foundation.BSTR, pdwCookie: POINTER(UInt32), correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveResourceEx(self, dwCookieConnection: UInt32, correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceReportMessage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a7c06739-500f-4e8c-99-a8-2b-d6-95-58-99-eb')
    @commethod(3)
    def RegisterErrorLogMessage(self, bstrMessage: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsErrorMessageRegistered(self, bstrWkspId: Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32, pfErrorExist: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterErrorEvent(self, bstrWkspId: Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceResTypeRegistry(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('1d428c79-6e2e-4351-a3-61-c0-40-1a-03-a0-ba')
    @commethod(7)
    def AddResourceType(self, fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, bstrLauncher: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteResourceType(self, fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRegisteredFileExtensions(self, fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, psaFileExtensions: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResourceTypeInfo(self, fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, pbstrLauncher: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ModifyResourceType(self, fMachineWide: Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: Windows.Win32.Foundation.BSTR, bstrLauncher: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('efea49a2-dda5-429d-8f-42-b2-3b-92-c4-c3-47')
    @commethod(7)
    def DisconnectWorkspace(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartWorkspace(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsWorkspaceCredentialSpecified(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bCountUnauthenticatedCredentials: Windows.Win32.Foundation.VARIANT_BOOL, pbCredExist: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsWorkspaceSSOEnabled(self, pbSSOEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearWorkspaceCredential(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnAuthenticated(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DisconnectWorkspaceByFriendlyName(self, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable
    Guid = Guid('efea49a2-dda5-429d-8f-42-b3-3b-a2-c4-c3-48')
    @commethod(14)
    def StartWorkspaceEx(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR, bstrRedirectorName: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrAppContainer: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ResourceDismissed(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable3(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable2
    Guid = Guid('531e6512-2cbf-4bd2-80-a5-d9-0a-71-63-6a-9a')
    @commethod(16)
    def StartWorkspaceEx2(self, bstrWorkspaceId: Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: Windows.Win32.Foundation.BSTR, bstrRedirectorName: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrAppContainer: Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32, bstrEventLogUploadAddress: Windows.Win32.Foundation.BSTR, correlationId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70c04b05-f347-412b-82-2f-36-c9-9c-54-ca-45')
    @commethod(3)
    def GetResourceList(self, userID: Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.pluginResource_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(self, alias: Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCacheLastUpdateTime(self, lastUpdateTime: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_pluginName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_pluginVersion(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResolveResource(self, resourceType: POINTER(UInt32), resourceLocation: Windows.Win32.Foundation.PWSTR, endPointName: Windows.Win32.Foundation.PWSTR, userID: Windows.Win32.Foundation.PWSTR, alias: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin2(c_void_p):
    extends: Windows.Win32.System.RemoteDesktop.ItsPubPlugin
    Guid = Guid('fa4ce418-aad7-4ec6-ba-d1-0a-32-1b-a4-65-d5')
    @commethod(9)
    def GetResource2List(self, userID: Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResource2(self, alias: Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResolvePersonalDesktop(self, userId: Windows.Win32.Foundation.PWSTR, poolId: Windows.Win32.Foundation.PWSTR, ePdResolutionType: Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE, pPdAssignmentType: POINTER(Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE), endPointName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeletePersonalDesktopAssignment(self, userId: Windows.Win32.Foundation.PWSTR, poolId: Windows.Win32.Foundation.PWSTR, endpointName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
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
class PRODUCT_INFOA(EasyCastStructure):
    CompanyName: Windows.Win32.Foundation.CHAR * 256
    ProductID: Windows.Win32.Foundation.CHAR * 4
class PRODUCT_INFOW(EasyCastStructure):
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
class RFX_GFX_MONITOR_INFO(EasyCastStructure):
    left: Int32
    top: Int32
    right: Int32
    bottom: Int32
    physicalWidth: UInt32
    physicalHeight: UInt32
    orientation: UInt32
    primary: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    reserved: UInt32
    monitorCount: UInt32
    MonitorData: Windows.Win32.System.RemoteDesktop.RFX_GFX_MONITOR_INFO * 16
    clientUniqueId: Char * 32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    ulBpp: UInt32
    Reserved: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_INPUT_RESET(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_RESEND_REQUEST(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    RedrawRect: Windows.Win32.System.RemoteDesktop.RFX_GFX_RECT
class RFX_GFX_MSG_DISCONNECT_NOTIFY(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    DisconnectReason: UInt32
    _pack_ = 1
class RFX_GFX_MSG_HEADER(EasyCastStructure):
    uMSGType: UInt16
    cbSize: UInt16
    _pack_ = 1
class RFX_GFX_MSG_RDP_DATA(EasyCastStructure):
    channelHdr: Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    rdpData: Byte * 1
class RFX_GFX_RECT(EasyCastStructure):
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
class TSSD_ConnectionPoint(EasyCastStructure):
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
class VM_NOTIFY_ENTRY(EasyCastStructure):
    VmName: Char * 128
    VmHost: Char * 128
class VM_NOTIFY_INFO(EasyCastStructure):
    dwNumEntries: UInt32
    ppVmEntries: POINTER(POINTER(Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY_head))
VM_NOTIFY_STATUS = Int32
VM_NOTIFY_STATUS_PENDING: VM_NOTIFY_STATUS = 0
VM_NOTIFY_STATUS_IN_PROGRESS: VM_NOTIFY_STATUS = 1
VM_NOTIFY_STATUS_COMPLETE: VM_NOTIFY_STATUS = 2
VM_NOTIFY_STATUS_FAILED: VM_NOTIFY_STATUS = 3
VM_NOTIFY_STATUS_CANCELED: VM_NOTIFY_STATUS = 4
class VM_PATCH_INFO(EasyCastStructure):
    dwNumEntries: UInt32
    pVmNames: POINTER(Windows.Win32.Foundation.PWSTR)
class WRDS_CONNECTION_SETTING(EasyCastUnion):
    WRdsConnectionSettings1: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_1
class WRDS_CONNECTION_SETTINGS(EasyCastStructure):
    WRdsConnectionSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL
    WRdsConnectionSetting: Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING
class WRDS_CONNECTION_SETTINGS_1(EasyCastStructure):
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
    ContextData: POINTER(Byte)
WRDS_CONNECTION_SETTING_LEVEL = Int32
WRDS_CONNECTION_SETTING_LEVEL_INVALID: WRDS_CONNECTION_SETTING_LEVEL = 0
WRDS_CONNECTION_SETTING_LEVEL_1: WRDS_CONNECTION_SETTING_LEVEL = 1
class WRDS_DYNAMIC_TIME_ZONE_INFORMATION(EasyCastStructure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    DaylightBias: Int32
    TimeZoneKeyName: Char * 128
    DynamicDaylightTimeDisabled: UInt16
class WRDS_LISTENER_SETTING(EasyCastUnion):
    WRdsListenerSettings1: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_1
class WRDS_LISTENER_SETTINGS(EasyCastStructure):
    WRdsListenerSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL
    WRdsListenerSetting: Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING
class WRDS_LISTENER_SETTINGS_1(EasyCastStructure):
    MaxProtocolListenerConnectionCount: UInt32
    SecurityDescriptorSize: UInt32
    pSecurityDescriptor: POINTER(Byte)
WRDS_LISTENER_SETTING_LEVEL = Int32
WRDS_LISTENER_SETTING_LEVEL_INVALID: WRDS_LISTENER_SETTING_LEVEL = 0
WRDS_LISTENER_SETTING_LEVEL_1: WRDS_LISTENER_SETTING_LEVEL = 1
class WRDS_SETTING(EasyCastUnion):
    WRdsSettings1: Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_1
class WRDS_SETTINGS(EasyCastStructure):
    WRdsSettingType: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE
    WRdsSettingLevel: Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL
    WRdsSetting: Windows.Win32.System.RemoteDesktop.WRDS_SETTING
class WRDS_SETTINGS_1(EasyCastStructure):
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
class WTSCLIENTA(EasyCastStructure):
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
class WTSCLIENTW(EasyCastStructure):
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
class WTSCONFIGINFOA(EasyCastStructure):
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
class WTSCONFIGINFOW(EasyCastStructure):
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
class WTSINFOA(EasyCastStructure):
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
    ConnectTime: Int64
    DisconnectTime: Int64
    LastInputTime: Int64
    LogonTime: Int64
    CurrentTime: Int64
class WTSINFOEXA(EasyCastStructure):
    Level: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_A
class WTSINFOEXW(EasyCastStructure):
    Level: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_W
class WTSINFOEX_LEVEL1_A(EasyCastStructure):
    SessionId: UInt32
    SessionState: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionFlags: Int32
    WinStationName: Windows.Win32.Foundation.CHAR * 33
    UserName: Windows.Win32.Foundation.CHAR * 21
    DomainName: Windows.Win32.Foundation.CHAR * 18
    LogonTime: Int64
    ConnectTime: Int64
    DisconnectTime: Int64
    LastInputTime: Int64
    CurrentTime: Int64
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBytes: UInt32
class WTSINFOEX_LEVEL1_W(EasyCastStructure):
    SessionId: UInt32
    SessionState: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionFlags: Int32
    WinStationName: Char * 33
    UserName: Char * 21
    DomainName: Char * 18
    LogonTime: Int64
    ConnectTime: Int64
    DisconnectTime: Int64
    LastInputTime: Int64
    CurrentTime: Int64
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBytes: UInt32
class WTSINFOEX_LEVEL_A(EasyCastUnion):
    WTSInfoExLevel1: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_A
class WTSINFOEX_LEVEL_W(EasyCastUnion):
    WTSInfoExLevel1: Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_W
class WTSINFOW(EasyCastStructure):
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
    ConnectTime: Int64
    DisconnectTime: Int64
    LastInputTime: Int64
    LogonTime: Int64
    CurrentTime: Int64
class WTSLISTENERCONFIGA(EasyCastStructure):
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
class WTSLISTENERCONFIGW(EasyCastStructure):
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
class WTSSBX_IP_ADDRESS(EasyCastStructure):
    AddressFamily: Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY
    Address: Byte * 16
    PortNumber: UInt16
    dwScope: UInt32
class WTSSBX_MACHINE_CONNECT_INFO(EasyCastStructure):
    wczMachineFQDN: Char * 257
    wczMachineNetBiosName: Char * 17
    dwNumOfIPAddr: UInt32
    IPaddr: Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS * 12
WTSSBX_MACHINE_DRAIN = Int32
WTSSBX_MACHINE_DRAIN_UNSPEC: WTSSBX_MACHINE_DRAIN = 0
WTSSBX_MACHINE_DRAIN_OFF: WTSSBX_MACHINE_DRAIN = 1
WTSSBX_MACHINE_DRAIN_ON: WTSSBX_MACHINE_DRAIN = 2
class WTSSBX_MACHINE_INFO(EasyCastStructure):
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
class WTSSBX_SESSION_INFO(EasyCastStructure):
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
class WTSSESSION_NOTIFICATION(EasyCastStructure):
    cbSize: UInt32
    dwSessionId: UInt32
class WTSUSERCONFIGA(EasyCastStructure):
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
class WTSUSERCONFIGW(EasyCastStructure):
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
class WTS_CACHE_STATS(EasyCastStructure):
    Specific: UInt32
    Data: Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS_UN
    ProtocolType: UInt16
    Length: UInt16
class WTS_CACHE_STATS_UN(EasyCastUnion):
    ProtocolCache: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_CACHE * 4
    TShareCacheStats: UInt32
    Reserved: UInt32 * 20
WTS_CERT_TYPE = Int32
WTS_CERT_TYPE_INVALID: WTS_CERT_TYPE = 0
WTS_CERT_TYPE_PROPRIETORY: WTS_CERT_TYPE = 1
WTS_CERT_TYPE_X509: WTS_CERT_TYPE = 2
class WTS_CLIENT_ADDRESS(EasyCastStructure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_CLIENT_DATA(EasyCastStructure):
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
class WTS_CLIENT_DISPLAY(EasyCastStructure):
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
class WTS_DISPLAY_IOCTL(EasyCastStructure):
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
class WTS_LICENSE_CAPABILITIES(EasyCastStructure):
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
class WTS_POLICY_DATA(EasyCastStructure):
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
class WTS_PROCESS_INFOA(EasyCastStructure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PSTR
    pUserSid: Windows.Win32.Foundation.PSID
class WTS_PROCESS_INFOW(EasyCastStructure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: Windows.Win32.Foundation.PWSTR
    pUserSid: Windows.Win32.Foundation.PSID
class WTS_PROCESS_INFO_EXA(EasyCastStructure):
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
    UserTime: Int64
    KernelTime: Int64
class WTS_PROCESS_INFO_EXW(EasyCastStructure):
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
    UserTime: Int64
    KernelTime: Int64
class WTS_PROPERTY_VALUE(EasyCastStructure):
    Type: UInt16
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        ulVal: UInt32
        strVal: _strVal_e__Struct
        bVal: _bVal_e__Struct
        guidVal: Guid
        class _strVal_e__Struct(EasyCastStructure):
            size: UInt32
            pstrVal: Windows.Win32.Foundation.PWSTR
        class _bVal_e__Struct(EasyCastStructure):
            size: UInt32
            pbVal: Windows.Win32.Foundation.PSTR
class WTS_PROTOCOL_CACHE(EasyCastStructure):
    CacheReads: UInt32
    CacheHits: UInt32
class WTS_PROTOCOL_COUNTERS(EasyCastStructure):
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
class WTS_PROTOCOL_STATUS(EasyCastStructure):
    Output: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Input: Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Cache: Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS
    AsyncSignal: UInt32
    AsyncSignalMask: UInt32
    Counters: Int64 * 100
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
class WTS_SERVER_INFOA(EasyCastStructure):
    pServerName: Windows.Win32.Foundation.PSTR
class WTS_SERVER_INFOW(EasyCastStructure):
    pServerName: Windows.Win32.Foundation.PWSTR
class WTS_SERVICE_STATE(EasyCastStructure):
    RcmServiceState: Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE
    RcmDrainState: Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE
class WTS_SESSION_ADDRESS(EasyCastStructure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_SESSION_ID(EasyCastStructure):
    SessionUniqueGuid: Guid
    SessionId: UInt32
class WTS_SESSION_INFOA(EasyCastStructure):
    SessionId: UInt32
    pWinStationName: Windows.Win32.Foundation.PSTR
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
class WTS_SESSION_INFOW(EasyCastStructure):
    SessionId: UInt32
    pWinStationName: Windows.Win32.Foundation.PWSTR
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
class WTS_SESSION_INFO_1A(EasyCastStructure):
    ExecEnvId: UInt32
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: Windows.Win32.Foundation.PSTR
    pHostName: Windows.Win32.Foundation.PSTR
    pUserName: Windows.Win32.Foundation.PSTR
    pDomainName: Windows.Win32.Foundation.PSTR
    pFarmName: Windows.Win32.Foundation.PSTR
class WTS_SESSION_INFO_1W(EasyCastStructure):
    ExecEnvId: UInt32
    State: Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: Windows.Win32.Foundation.PWSTR
    pHostName: Windows.Win32.Foundation.PWSTR
    pUserName: Windows.Win32.Foundation.PWSTR
    pDomainName: Windows.Win32.Foundation.PWSTR
    pFarmName: Windows.Win32.Foundation.PWSTR
class WTS_SMALL_RECT(EasyCastStructure):
    Left: Int16
    Top: Int16
    Right: Int16
    Bottom: Int16
class WTS_SOCKADDR(EasyCastStructure):
    sin_family: UInt16
    u: _u_e__Union
    class _u_e__Union(EasyCastUnion):
        ipv4: _ipv4_e__Struct
        ipv6: _ipv6_e__Struct
        class _ipv4_e__Struct(EasyCastStructure):
            sin_port: UInt16
            IN_ADDR: UInt32
            sin_zero: Byte * 8
        class _ipv6_e__Struct(EasyCastStructure):
            sin6_port: UInt16
            sin6_flowinfo: UInt32
            sin6_addr: UInt16 * 8
            sin6_scope_id: UInt32
class WTS_SYSTEMTIME(EasyCastStructure):
    wYear: UInt16
    wMonth: UInt16
    wDayOfWeek: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
    wMilliseconds: UInt16
class WTS_TIME_ZONE_INFORMATION(EasyCastStructure):
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
class WTS_USER_CREDENTIAL(EasyCastStructure):
    UserName: Char * 256
    Password: Char * 256
    Domain: Char * 256
class WTS_USER_DATA(EasyCastStructure):
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    UserTimeZone: Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
class WTS_VALIDATION_INFORMATIONA(EasyCastStructure):
    ProductInfo: Windows.Win32.System.RemoteDesktop.PRODUCT_INFOA
    License: Byte * 16384
    LicenseLength: UInt32
    HardwareID: Byte * 20
    HardwareIDLength: UInt32
class WTS_VALIDATION_INFORMATIONW(EasyCastStructure):
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
class pluginResource(EasyCastStructure):
    alias: Char * 256
    name: Char * 256
    resourceFileContents: Windows.Win32.Foundation.PWSTR
    fileExtension: Char * 256
    resourcePluginType: Char * 256
    isDiscoverable: Byte
    resourceType: Int32
    pceIconSize: UInt32
    iconContents: POINTER(Byte)
    pcePluginBlobSize: UInt32
    blobContents: POINTER(Byte)
class pluginResource2(EasyCastStructure):
    resourceV1: Windows.Win32.System.RemoteDesktop.pluginResource
    pceFileAssocListSize: UInt32
    fileAssocList: POINTER(Windows.Win32.System.RemoteDesktop.pluginResource2FileAssociation_head)
    securityDescriptor: Windows.Win32.Foundation.PWSTR
    pceFolderListSize: UInt32
    folderList: POINTER(POINTER(UInt16))
class pluginResource2FileAssociation(EasyCastStructure):
    extName: Char * 256
    primaryHandler: Byte
    pceIconSize: UInt32
    iconContents: POINTER(Byte)
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
