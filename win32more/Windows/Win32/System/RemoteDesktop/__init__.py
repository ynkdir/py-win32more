from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Audio.Apo
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.RemoteDesktop
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.UI.WindowsAndMessaging
class AAAccountingData(Structure):
    userName: win32more.Windows.Win32.Foundation.BSTR
    clientName: win32more.Windows.Win32.Foundation.BSTR
    authType: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes
    resourceName: win32more.Windows.Win32.Foundation.BSTR
    portNumber: Int32
    protocolName: win32more.Windows.Win32.Foundation.BSTR
    numberOfBytesReceived: Int32
    numberOfBytesTransfered: Int32
    reasonForDisconnect: win32more.Windows.Win32.Foundation.BSTR
    mainSessionId: Guid
    subSessionId: Int32
AAAccountingDataType = Int32
AA_MAIN_SESSION_CREATION: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingDataType = 0
AA_SUB_SESSION_CREATION: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingDataType = 1
AA_SUB_SESSION_CLOSED: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingDataType = 2
AA_MAIN_SESSION_CLOSED: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingDataType = 3
AAAuthSchemes = Int32
AA_AUTH_MIN: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 0
AA_AUTH_BASIC: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 1
AA_AUTH_NTLM: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 2
AA_AUTH_SC: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 3
AA_AUTH_LOGGEDONCREDENTIALS: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 4
AA_AUTH_NEGOTIATE: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 5
AA_AUTH_ANY: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 6
AA_AUTH_COOKIE: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 7
AA_AUTH_DIGEST: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 8
AA_AUTH_ORGID: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 9
AA_AUTH_CONID: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 10
AA_AUTH_SSPI_NTLM: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 11
AA_AUTH_MAX: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes = 12
AATrustClassID = Int32
AA_UNTRUSTED: win32more.Windows.Win32.System.RemoteDesktop.AATrustClassID = 0
AA_TRUSTEDUSER_UNTRUSTEDCLIENT: win32more.Windows.Win32.System.RemoteDesktop.AATrustClassID = 1
AA_TRUSTEDUSER_TRUSTEDCLIENT: win32more.Windows.Win32.System.RemoteDesktop.AATrustClassID = 2
ADsTSUserEx = Guid('{e2e9cae6-1e7b-4b8e-babd-e9bf6292ac29}')
class AE_CURRENT_POSITION(Structure):
    u64DevicePosition: UInt64
    u64StreamPosition: UInt64
    u64PaddingFrames: UInt64
    hnsQPCPosition: Int64
    f32FramesPerSecond: Single
    Flag: win32more.Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS
AE_POSITION_FLAGS = Int32
POSITION_INVALID: win32more.Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS = 0
POSITION_DISCONTINUOUS: win32more.Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS = 1
POSITION_CONTINUOUS: win32more.Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS = 2
POSITION_QPC_ERROR: win32more.Windows.Win32.System.RemoteDesktop.AE_POSITION_FLAGS = 4
WTS_CURRENT_SERVER: win32more.Windows.Win32.Foundation.HANDLE = 0
WTS_CURRENT_SERVER_HANDLE: win32more.Windows.Win32.Foundation.HANDLE = 0
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
RDCLIENT_BITMAP_RENDER_SERVICE: Guid = Guid('{e4cc08cb-942e-4b19-8504-bd5a89a747f5}')
WTS_QUERY_ALLOWED_INITIAL_APP: Guid = Guid('{c77d1b30-5be1-4c6b-a0e1-bd6d2e5c9fcc}')
WTS_QUERY_LOGON_SCREEN_SIZE: Guid = Guid('{8b8e0fe7-0804-4a0e-b279-8660b1df0049}')
WTS_QUERY_AUDIOENUM_DLL: Guid = Guid('{9bf4fa97-c883-4c2a-80ab-5a39c9af00db}')
WTS_QUERY_MF_FORMAT_SUPPORT: Guid = Guid('{41869ad0-6332-4dc8-95d5-db749e2f1d94}')
WRDS_SERVICE_ID_GRAPHICS_GUID: Guid = Guid('{d2993f4d-02cf-4280-8c48-1624b44f8706}')
PROPERTY_DYNAMIC_TIME_ZONE_INFORMATION: Guid = Guid('{0cdfd28e-d0b9-4c1f-a5eb-6d1f6c6535b9}')
PROPERTY_TYPE_GET_FAST_RECONNECT: Guid = Guid('{6212d757-0043-4862-99c3-9f3059ac2a3b}')
PROPERTY_TYPE_GET_FAST_RECONNECT_USER_SID: Guid = Guid('{197c427a-0135-4b6d-9c5e-e6579a0ab625}')
PROPERTY_TYPE_ENABLE_UNIVERSAL_APPS_FOR_CUSTOM_SHELL: Guid = Guid('{ed2c3fda-338d-4d3f-81a3-e767310d908e}')
CONNECTION_PROPERTY_IDLE_TIME_WARNING: Guid = Guid('{693f7ff5-0c4e-4d17-b8e0-1f70325e5d58}')
CONNECTION_PROPERTY_CURSOR_BLINK_DISABLED: Guid = Guid('{4b150580-fea4-4d3c-9de4-7433a66618f7}')
@winfunctype('WTSAPI32.dll')
def WTSStopRemoteControlSession(LogonId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSStartRemoteControlSessionW(pTargetServerName: win32more.Windows.Win32.Foundation.PWSTR, TargetLogonId: UInt32, HotkeyVk: Byte, HotkeyModifiers: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSStartRemoteControlSession = UnicodeAlias('WTSStartRemoteControlSessionW')
@winfunctype('WTSAPI32.dll')
def WTSStartRemoteControlSessionA(pTargetServerName: win32more.Windows.Win32.Foundation.PSTR, TargetLogonId: UInt32, HotkeyVk: Byte, HotkeyModifiers: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSConnectSessionA(LogonId: UInt32, TargetLogonId: UInt32, pPassword: win32more.Windows.Win32.Foundation.PSTR, bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSConnectSessionW(LogonId: UInt32, TargetLogonId: UInt32, pPassword: win32more.Windows.Win32.Foundation.PWSTR, bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSConnectSession = UnicodeAlias('WTSConnectSessionW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateServersW(pDomainName: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, Version: UInt32, ppServerInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SERVER_INFOW)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateServers = UnicodeAlias('WTSEnumerateServersW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateServersA(pDomainName: win32more.Windows.Win32.Foundation.PSTR, Reserved: UInt32, Version: UInt32, ppServerInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SERVER_INFOA)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerW(pServerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
WTSOpenServer = UnicodeAlias('WTSOpenServerW')
@winfunctype('WTSAPI32.dll')
def WTSOpenServerA(pServerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSOpenServerExW(pServerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
WTSOpenServerEx = UnicodeAlias('WTSOpenServerExW')
@winfunctype('WTSAPI32.dll')
def WTSOpenServerExA(pServerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSCloseServer(hServer: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsW(hServer: win32more.Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppSessionInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFOW)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateSessions = UnicodeAlias('WTSEnumerateSessionsW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsA(hServer: win32more.Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppSessionInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFOA)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsExW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), Filter: UInt32, ppSessionInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFO_1W)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateSessionsEx = UnicodeAlias('WTSEnumerateSessionsExW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateSessionsExA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), Filter: UInt32, ppSessionInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_INFO_1A)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesW(hServer: win32more.Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppProcessInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROCESS_INFOW)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateProcesses = UnicodeAlias('WTSEnumerateProcessesW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesA(hServer: win32more.Windows.Win32.Foundation.HANDLE, Reserved: UInt32, Version: UInt32, ppProcessInfo: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROCESS_INFOA)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSTerminateProcess(hServer: win32more.Windows.Win32.Foundation.HANDLE, ProcessId: UInt32, ExitCode: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQuerySessionInformationW(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, WTSInfoClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS, ppBuffer: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSQuerySessionInformation = UnicodeAlias('WTSQuerySessionInformationW')
@winfunctype('WTSAPI32.dll')
def WTSQuerySessionInformationA(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, WTSInfoClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS, ppBuffer: POINTER(win32more.Windows.Win32.Foundation.PSTR), pBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryUserConfigW(pServerName: win32more.Windows.Win32.Foundation.PWSTR, pUserName: win32more.Windows.Win32.Foundation.PWSTR, WTSConfigClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, ppBuffer: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSQueryUserConfig = UnicodeAlias('WTSQueryUserConfigW')
@winfunctype('WTSAPI32.dll')
def WTSQueryUserConfigA(pServerName: win32more.Windows.Win32.Foundation.PSTR, pUserName: win32more.Windows.Win32.Foundation.PSTR, WTSConfigClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, ppBuffer: POINTER(win32more.Windows.Win32.Foundation.PSTR), pBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetUserConfigW(pServerName: win32more.Windows.Win32.Foundation.PWSTR, pUserName: win32more.Windows.Win32.Foundation.PWSTR, WTSConfigClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, pBuffer: win32more.Windows.Win32.Foundation.PWSTR, DataLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSSetUserConfig = UnicodeAlias('WTSSetUserConfigW')
@winfunctype('WTSAPI32.dll')
def WTSSetUserConfigA(pServerName: win32more.Windows.Win32.Foundation.PSTR, pUserName: win32more.Windows.Win32.Foundation.PSTR, WTSConfigClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS, pBuffer: win32more.Windows.Win32.Foundation.PSTR, DataLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSendMessageW(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pTitle: win32more.Windows.Win32.Foundation.PWSTR, TitleLength: UInt32, pMessage: win32more.Windows.Win32.Foundation.PWSTR, MessageLength: UInt32, Style: win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, Timeout: UInt32, pResponse: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_RESULT), bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSSendMessage = UnicodeAlias('WTSSendMessageW')
@winfunctype('WTSAPI32.dll')
def WTSSendMessageA(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pTitle: win32more.Windows.Win32.Foundation.PSTR, TitleLength: UInt32, pMessage: win32more.Windows.Win32.Foundation.PSTR, MessageLength: UInt32, Style: win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, Timeout: UInt32, pResponse: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_RESULT), bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSDisconnectSession(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSLogoffSession(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSShutdownSystem(hServer: win32more.Windows.Win32.Foundation.HANDLE, ShutdownFlag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSWaitSystemEvent(hServer: win32more.Windows.Win32.Foundation.HANDLE, EventMask: UInt32, pEventFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelOpen(hServer: win32more.Windows.Win32.Foundation.HANDLE, SessionId: UInt32, pVirtualName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelOpenEx(SessionId: UInt32, pVirtualName: win32more.Windows.Win32.Foundation.PSTR, flags: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelClose(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelRead(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE, TimeOut: UInt32, Buffer: win32more.Windows.Win32.Foundation.PSTR, BufferSize: UInt32, pBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelWrite(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE, Buffer: win32more.Windows.Win32.Foundation.PSTR, Length: UInt32, pBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelPurgeInput(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelPurgeOutput(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSVirtualChannelQuery(hChannelHandle: win32more.Windows.Win32.Foundation.HANDLE, param1: win32more.Windows.Win32.System.RemoteDesktop.WTS_VIRTUAL_CLASS, ppBuffer: POINTER(VoidPtr), pBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSFreeMemory(pMemory: VoidPtr) -> Void: ...
@winfunctype('WTSAPI32.dll')
def WTSRegisterSessionNotification(hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSUnRegisterSessionNotification(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSRegisterSessionNotificationEx(hServer: win32more.Windows.Win32.Foundation.HANDLE, hWnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSUnRegisterSessionNotificationEx(hServer: win32more.Windows.Win32.Foundation.HANDLE, hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryUserToken(SessionId: UInt32, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSFreeMemoryExW(WTSTypeClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS, pMemory: VoidPtr, NumberOfEntries: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSFreeMemoryEx = UnicodeAlias('WTSFreeMemoryExW')
@winfunctype('WTSAPI32.dll')
def WTSFreeMemoryExA(WTSTypeClass: win32more.Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS, pMemory: VoidPtr, NumberOfEntries: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesExW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), SessionId: UInt32, ppProcessInfo: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateProcessesEx = UnicodeAlias('WTSEnumerateProcessesExW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateProcessesExA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pLevel: POINTER(UInt32), SessionId: UInt32, ppProcessInfo: POINTER(win32more.Windows.Win32.Foundation.PSTR), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnumerateListenersW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListeners: POINTER(POINTER(UInt16)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSEnumerateListeners = UnicodeAlias('WTSEnumerateListenersW')
@winfunctype('WTSAPI32.dll')
def WTSEnumerateListenersA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListeners: POINTER(POINTER(SByte)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSQueryListenerConfigW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSQueryListenerConfig = UnicodeAlias('WTSQueryListenerConfigW')
@winfunctype('WTSAPI32.dll')
def WTSQueryListenerConfigA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PSTR, pBuffer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSCreateListenerW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGW), flag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSCreateListener = UnicodeAlias('WTSCreateListenerW')
@winfunctype('WTSAPI32.dll')
def WTSCreateListenerA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PSTR, pBuffer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSLISTENERCONFIGA), flag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetListenerSecurityW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PWSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSSetListenerSecurity = UnicodeAlias('WTSSetListenerSecurityW')
@winfunctype('WTSAPI32.dll')
def WTSSetListenerSecurityA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSGetListenerSecurityW(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PWSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WTSGetListenerSecurity = UnicodeAlias('WTSGetListenerSecurityW')
@winfunctype('WTSAPI32.dll')
def WTSGetListenerSecurityA(hServer: win32more.Windows.Win32.Foundation.HANDLE, pReserved: VoidPtr, Reserved: UInt32, pListenerName: win32more.Windows.Win32.Foundation.PSTR, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, nLength: UInt32, lpnLengthNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSEnableChildSessions(bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSIsChildSessionsEnabled(pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSGetChildSessionId(pSessionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WTSAPI32.dll')
def WTSSetRenderHint(pRenderHintID: POINTER(UInt64), hwndOwner: win32more.Windows.Win32.Foundation.HWND, renderHintType: UInt32, cbHintDataLength: UInt32, pHintData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ProcessIdToSessionId(dwProcessId: UInt32, pSessionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WTSGetActiveConsoleSessionId() -> UInt32: ...
class BITMAP_RENDERER_STATISTICS(Structure):
    dwFramesDelivered: UInt32
    dwFramesDropped: UInt32
class CHANNEL_DEF(Structure):
    name: win32more.Windows.Win32.Foundation.CHAR * 8
    options: UInt32
    _pack_ = 1
class CHANNEL_ENTRY_POINTS(Structure):
    cbSize: UInt32
    protocolVersion: UInt32
    pVirtualChannelInit: win32more.Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELINIT
    pVirtualChannelOpen: win32more.Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELOPEN
    pVirtualChannelClose: win32more.Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELCLOSE
    pVirtualChannelWrite: win32more.Windows.Win32.System.RemoteDesktop.PVIRTUALCHANNELWRITE
class CHANNEL_PDU_HEADER(Structure):
    length: UInt32
    flags: UInt32
class CLIENT_DISPLAY(Structure):
    HorizontalResolution: UInt32
    VerticalResolution: UInt32
    ColorDepth: UInt32
CLIENT_MESSAGE_TYPE = Int32
CLIENT_MESSAGE_CONNECTION_INVALID: win32more.Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE = 0
CLIENT_MESSAGE_CONNECTION_STATUS: win32more.Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE = 1
CLIENT_MESSAGE_CONNECTION_ERROR: win32more.Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE = 2
CONNECTION_CHANGE_NOTIFICATION = Int32
CONNECTION_REQUEST_INVALID: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 0
CONNECTION_REQUEST_PENDING: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 1
CONNECTION_REQUEST_FAILED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 2
CONNECTION_REQUEST_TIMEDOUT: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 3
CONNECTION_REQUEST_SUCCEEDED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 4
CONNECTION_REQUEST_CANCELLED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 5
CONNECTION_REQUEST_LB_COMPLETED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 6
CONNECTION_REQUEST_QUERY_PL_COMPLETED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 7
CONNECTION_REQUEST_ORCH_COMPLETED: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION = 8
class IADsTSUserEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c4930e79-2989-4462-8a60-2fcf2f2955ef}')
    @commethod(7)
    def get_TerminalServicesProfilePath(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TerminalServicesProfilePath(self, pNewVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TerminalServicesHomeDirectory(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TerminalServicesHomeDirectory(self, pNewVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TerminalServicesHomeDrive(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_TerminalServicesHomeDrive(self, pNewVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowLogon(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowLogon(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EnableRemoteControl(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EnableRemoteControl(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_MaxDisconnectionTime(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_MaxDisconnectionTime(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MaxConnectionTime(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_MaxConnectionTime(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_MaxIdleTime(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_MaxIdleTime(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ReconnectionAction(self, pNewVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_ReconnectionAction(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_BrokenConnectionAction(self, pNewVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_BrokenConnectionAction(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ConnectClientDrivesAtLogon(self, pNewVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ConnectClientDrivesAtLogon(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ConnectClientPrintersAtLogon(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ConnectClientPrintersAtLogon(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DefaultToMainPrinter(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_DefaultToMainPrinter(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_TerminalServicesWorkDirectory(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_TerminalServicesWorkDirectory(self, pNewVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_TerminalServicesInitialProgram(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_TerminalServicesInitialProgram(self, pNewVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioDeviceEndpoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d4952f5a-a0b2-4cc4-8b82-9358488dd8ac}')
    @commethod(3)
    def SetBuffer(self, MaxPeriod: Int64, u32LatencyCoefficient: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRTCaps(self, pbIsRTCapable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEventDrivenCapable(self, pbisEventCapable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteExclusiveModeParametersToSharedMemory(self, hTargetProcess: UIntPtr, hnsPeriod: Int64, hnsBufferDuration: Int64, u32LatencyCoefficient: UInt32, pu32SharedMemorySize: POINTER(UInt32), phSharedMemory: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30a99515-1527-4451-af9f-00c5f0234daf}')
    @commethod(3)
    def GetFrameFormat(self, ppFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesPerPacket(self, pFramesPerPacket: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatency(self, pLatency: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetStreamFlags(self, streamFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEventHandle(self, eventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c684b72a-6df4-4774-bdf9-76b77509b653}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEndpointRT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfd2005f-a6e5-4d39-a265-939ada9fbb4d}')
    @commethod(3)
    def GetCurrentPadding(self, pPadding: POINTER(Int64), pAeCurrentPosition: POINTER(win32more.Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION)) -> Void: ...
    @commethod(4)
    def ProcessingComplete(self) -> Void: ...
    @commethod(5)
    def SetPinInactive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPinActive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioInputEndpointRT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8026ab61-92b2-43c1-a1df-5c37ebd08d82}')
    @commethod(3)
    def GetInputDataPointer(self, pConnectionProperty: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY), pAeTimeStamp: POINTER(win32more.Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION)) -> Void: ...
    @commethod(4)
    def ReleaseInputDataPointer(self, u32FrameCount: UInt32, pDataPointer: UIntPtr) -> Void: ...
    @commethod(5)
    def PulseEndpoint(self) -> Void: ...
class IAudioOutputEndpointRT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fa906e4-c31c-4e31-932e-19a66385e9aa}')
    @commethod(3)
    def GetOutputDataPointer(self, u32FrameCount: UInt32, pAeTimeStamp: POINTER(win32more.Windows.Win32.System.RemoteDesktop.AE_CURRENT_POSITION)) -> UIntPtr: ...
    @commethod(4)
    def ReleaseOutputDataPointer(self, pConnectionProperty: POINTER(win32more.Windows.Win32.Media.Audio.Apo.APO_CONNECTION_PROPERTY)) -> Void: ...
    @commethod(5)
    def PulseEndpoint(self) -> Void: ...
class IRemoteDesktopClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{57d25668-625a-4905-be4e-304caa13f89c}')
    @commethod(7)
    def Connect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reconnect(self, width: UInt32, height: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Settings(self, settings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientSettings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(self, actions: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientActions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TouchPointer(self, touchPointer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IRemoteDesktopClientTouchPointer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteSavedCredentials(self, serverName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateSessionDisplaySettings(self, width: UInt32, height: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def attachEvent(self, eventName: win32more.Windows.Win32.Foundation.BSTR, callback: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def detachEvent(self, eventName: win32more.Windows.Win32.Foundation.BSTR, callback: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientActions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7d54bc4e-1028-45d4-8b0a-b9b6bffba176}')
    @commethod(7)
    def SuspendScreenUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResumeScreenUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ExecuteRemoteAction(self, remoteAction: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSnapshot(self, snapshotEncoding: win32more.Windows.Win32.System.RemoteDesktop.SnapshotEncodingType, snapshotFormat: win32more.Windows.Win32.System.RemoteDesktop.SnapshotFormatType, snapshotWidth: UInt32, snapshotHeight: UInt32, snapshotData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{48a0f2a7-2713-431f-bbac-6f4558e7d64d}')
    @commethod(7)
    def ApplySettings(self, rdpFileContents: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveSettings(self, rdpFileContents: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRdpProperty(self, propertyName: win32more.Windows.Win32.Foundation.BSTR, value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRdpProperty(self, propertyName: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDesktopClientTouchPointer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{260ec22d-8cbc-44b5-9e88-2a37f6c93ae9}')
    @commethod(7)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_EventsEnabled(self, eventsEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventsEnabled(self, eventsEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_PointerSpeed(self, pointerSpeed: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PointerSpeed(self, pointerSpeed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteSystemAdditionalInfoProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eeaa3d5f-ec63-4d27-af38-e86b1d7292cb}')
    @commethod(3)
    def GetAdditionalInfo(self, deduplicationId: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), riid: POINTER(Guid), mapView: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGAccountingEngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ce2a0c9-e874-4f1a-86f4-06bbb9115338}')
    @commethod(3)
    def DoAccounting(self, accountingDataType: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingDataType, accountingData: win32more.Windows.Win32.System.RemoteDesktop.AAAccountingData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticateUserSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c3e2e73-a782-47f9-8dfb-77ee1ed27a03}')
    @commethod(3)
    def OnUserAuthenticated(self, userName: win32more.Windows.Win32.Foundation.BSTR, userDomain: win32more.Windows.Win32.Foundation.BSTR, context: UIntPtr, userToken: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUserAuthenticationFailed(self, context: UIntPtr, genericErrorCode: win32more.Windows.Win32.Foundation.HRESULT, specificErrorCode: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReauthenticateUser(self, context: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisconnectUser(self, context: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthenticationEngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ee3e5bf-04ab-4691-998c-d7f622321a56}')
    @commethod(3)
    def AuthenticateUser(self, mainSessionId: Guid, cookieData: POINTER(Byte), numCookieBytes: UInt32, context: UIntPtr, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITSGAuthenticateUserSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelAuthentication(self, mainSessionId: Guid, context: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeConnectionSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c27ece33-7781-4318-98ef-1cf2da7b7005}')
    @commethod(3)
    def OnConnectionAuthorized(self, hrIn: win32more.Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, cbSoHResponse: UInt32, pbSoHResponse: POINTER(Byte), idleTimeout: UInt32, sessionTimeout: UInt32, sessionTimeoutAction: win32more.Windows.Win32.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE, trustClass: win32more.Windows.Win32.System.RemoteDesktop.AATrustClassID, policyAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGAuthorizeResourceSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feddfcd4-fa12-4435-ae55-7ad1a9779af7}')
    @commethod(3)
    def OnChannelAuthorized(self, hrIn: win32more.Windows.Win32.Foundation.HRESULT, mainSessionId: Guid, subSessionId: Int32, allowedResourceNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), numAllowedResourceNames: UInt32, failedResourceNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), numFailedResourceNames: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITSGPolicyEngine(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8bc24f08-6223-42f4-a5b4-8e37cd135bbd}')
    @commethod(3)
    def AuthorizeConnection(self, mainSessionId: Guid, username: win32more.Windows.Win32.Foundation.BSTR, authType: win32more.Windows.Win32.System.RemoteDesktop.AAAuthSchemes, clientMachineIP: win32more.Windows.Win32.Foundation.BSTR, clientMachineName: win32more.Windows.Win32.Foundation.BSTR, sohData: POINTER(Byte), numSOHBytes: UInt32, cookieData: POINTER(Byte), numCookieBytes: UInt32, userToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITSGAuthorizeConnectionSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AuthorizeResource(self, mainSessionId: Guid, subSessionId: Int32, username: win32more.Windows.Win32.Foundation.BSTR, resourceNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), numResources: UInt32, alternateResourceNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), numAlternateResourceName: UInt32, portNumber: UInt32, operation: win32more.Windows.Win32.Foundation.BSTR, cookie: POINTER(Byte), numBytesInCookie: UInt32, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITSGAuthorizeResourceSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsQuarantineEnabled(self, quarantineEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbBaseNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{808a6537-1282-4989-9e09-f43938b71722}')
    @commethod(3)
    def OnError(self, hrError: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReportStatus(self, messageType: win32more.Windows.Win32.System.RemoteDesktop.CLIENT_MESSAGE_TYPE, messageID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18857499-ad61-4b1b-b7df-cbcd41fb8338}')
    @commethod(3)
    def get_UserName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Domain(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_InitialProgram(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_LoadBalanceResult(self, ppVal: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_FarmName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutContext(self, contextId: win32more.Windows.Win32.Foundation.BSTR, context: win32more.Windows.Win32.System.Variant.VARIANT, existingContext: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContext(self, contextId: win32more.Windows.Win32.Foundation.BSTR, context: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Environment(self, ppEnvironment: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ConnectionError(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_SamUserAccount(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ClientConnectionPropertySet(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbClientConnectionPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsFirstAssignment(self, ppVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RdFarmType(self, pRdFarmType: POINTER(win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UserSidString(self, pszUserSidString: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDisconnectedSession(self, ppSession: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbClientConnectionPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    _iid_ = Guid('{e51995b0-46d6-11dd-aa21-cedc55d89593}')
class ITsSbEnvironment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c87f7f7-bf51-4a5c-87bf-8e94fb6e2256}')
    @commethod(3)
    def get_Name(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ServerWeight(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EnvironmentPropertySet(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_EnvironmentPropertySet(self, pVal: win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbEnvironmentPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    _iid_ = Guid('{d0d1bf7e-7acf-11dd-a243-e51156d89593}')
class ITsSbFilterPluginStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85b44b0f-ed78-413f-9702-fa6d3b5ee755}')
    @commethod(3)
    def SaveProperties(self, pPropertySet: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateProperties(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteProperties(self, propertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbGenericNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c4c8c4f-300b-46ad-9164-8468a7e7568c}')
    @commethod(3)
    def OnCompleted(self, Status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWaitTimeout(self, pftTimeout: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbGlobalStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ab60f7b-bd72-4d9f-8a3a-a0ea5574e635}')
    @commethod(3)
    def QueryTarget(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, TargetName: win32more.Windows.Win32.Foundation.BSTR, FarmName: win32more.Windows.Win32.Foundation.BSTR, ppTarget: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32, TargetName: win32more.Windows.Win32.Foundation.BSTR, ppSession: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateFarms(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateTargets(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, FarmName: win32more.Windows.Win32.Foundation.BSTR, EnvName: win32more.Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateEnvironmentsByProvider(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumerateSessions(self, ProviderName: win32more.Windows.Win32.Foundation.BSTR, targetName: win32more.Windows.Win32.Foundation.BSTR, userName: win32more.Windows.Win32.Foundation.BSTR, userDomain: win32more.Windows.Win32.Foundation.BSTR, poolName: win32more.Windows.Win32.Foundation.BSTR, initialProgram: win32more.Windows.Win32.Foundation.BSTR, pSessionState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFarmProperty(self, farmName: win32more.Windows.Win32.Foundation.BSTR, propertyName: win32more.Windows.Win32.Foundation.BSTR, pVarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalanceResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24fdb7ac-fea6-11dc-9672-9a8956d89593}')
    @commethod(3)
    def get_TargetName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancing(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{24329274-9eb7-11dc-ae98-f2b456d89593}')
    @commethod(5)
    def GetMostSuitableTarget(self, pConnection: win32more.Windows.Win32.System.RemoteDesktop.ITsSbClientConnection, pLBSink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbLoadBalancingNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbLoadBalancingNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    _iid_ = Guid('{5f8a8297-3244-4e6a-958a-27c822c1e141}')
    @commethod(5)
    def OnGetMostSuitableTarget(self, pLBResult: win32more.Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult, fIsNewConnection: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestration(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{64fc1172-9eb7-11dc-8b00-3aba56d89593}')
    @commethod(5)
    def PrepareTargetForConnect(self, pConnection: win32more.Windows.Win32.System.RemoteDesktop.ITsSbClientConnection, pOrchestrationNotifySink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbOrchestrationNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbOrchestrationNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    _iid_ = Guid('{36c37d61-926b-442f-bca5-118c6d50dcf2}')
    @commethod(5)
    def OnReadyToConnect(self, pTarget: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacement(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{daadee5f-6d32-480e-9e36-ddab2329f06d}')
    @commethod(5)
    def QueryEnvironmentForTarget(self, pConnection: win32more.Windows.Win32.System.RemoteDesktop.ITsSbClientConnection, pPlacementSink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlacementNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlacementNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    _iid_ = Guid('{68a0c487-2b4f-46c2-94a1-6ce685183634}')
    @commethod(5)
    def OnQueryEnvironmentCompleted(self, pEnvironment: win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{48cd7406-caab-465f-a5d6-baa863b9ea4f}')
    @commethod(3)
    def Initialize(self, pProvider: win32more.Windows.Win32.System.RemoteDesktop.ITsSbProvider, pNotifySink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPluginNotifySink, pPropertySet: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbPluginNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    _iid_ = Guid('{44dfe30b-c3be-40f5-bf82-7a95bb795adf}')
    @commethod(5)
    def OnInitialized(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTerminated(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbPluginPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    _iid_ = Guid('{95006e34-7eff-4b6c-bb40-49a4fda7cea6}')
class ITsSbPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag
    _iid_ = Guid('{5c025171-bb1e-4baf-a212-6d5e9774b33b}')
class ITsSbProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87a4098f-6d7b-44dd-bc17-8ce44e370d52}')
    @commethod(3)
    def CreateTargetObject(self, TargetName: win32more.Windows.Win32.Foundation.BSTR, EnvironmentName: win32more.Windows.Win32.Foundation.BSTR, ppTarget: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateLoadBalanceResultObject(self, TargetName: win32more.Windows.Win32.Foundation.BSTR, ppLBResult: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbLoadBalanceResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateSessionObject(self, TargetName: win32more.Windows.Win32.Foundation.BSTR, UserName: win32more.Windows.Win32.Foundation.BSTR, Domain: win32more.Windows.Win32.Foundation.BSTR, SessionId: UInt32, ppSession: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreatePluginPropertySet(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbPluginPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateTargetPropertySetObject(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEnvironmentObject(self, Name: win32more.Windows.Win32.Foundation.BSTR, ServerWeight: UInt32, ppEnvironment: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetResourcePluginStore(self, ppStore: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbResourcePluginStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilterPluginStore(self, ppStore: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbFilterPluginStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterForNotification(self, notificationType: UInt32, ResourceToMonitor: win32more.Windows.Win32.Foundation.BSTR, pPluginNotification: win32more.Windows.Win32.System.RemoteDesktop.ITsSbResourceNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnRegisterForNotification(self, notificationType: UInt32, ResourceToMonitor: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceOfGlobalStore(self, ppGlobalStore: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbGlobalStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateEnvironmentPropertySetObject(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironmentPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioning(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{2f6f0dbb-9e4f-462b-9c3f-fccc3dcb6232}')
    @commethod(5)
    def CreateVirtualMachines(self, JobXmlString: win32more.Windows.Win32.Foundation.BSTR, JobGuid: win32more.Windows.Win32.Foundation.BSTR, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PatchVirtualMachines(self, JobXmlString: win32more.Windows.Win32.Foundation.BSTR, JobGuid: win32more.Windows.Win32.Foundation.BSTR, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink, pVMPatchInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.VM_PATCH_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteVirtualMachines(self, JobXmlString: win32more.Windows.Win32.Foundation.BSTR, JobGuid: win32more.Windows.Win32.Foundation.BSTR, pSink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelJob(self, JobGuid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbProvisioningPluginNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aca87a8e-818b-4581-a032-49c3dfb9c701}')
    @commethod(3)
    def OnJobCreated(self, pVmNotifyInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnVirtualMachineStatusChanged(self, pVmNotifyEntry: POINTER(win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY), VmNotifyStatus: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS, ErrorCode: win32more.Windows.Win32.Foundation.HRESULT, ErrorDescr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnJobCompleted(self, ResultCode: win32more.Windows.Win32.Foundation.HRESULT, ResultDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnJobCancelled(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockVirtualMachine(self, pVmNotifyEntry: POINTER(win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnVirtualMachineHostStatusChanged(self, VmHost: win32more.Windows.Win32.Foundation.BSTR, VmHostNotifyStatus: win32more.Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS, ErrorCode: win32more.Windows.Win32.Foundation.HRESULT, ErrorDescr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65d3e85a-c39b-11dc-b92d-3cd255d89593}')
    @commethod(3)
    def NotifySessionChange(self, changeType: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE, pSession: win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChange(self, TargetChangeType: UInt32, pTarget: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChange(self, ChangeType: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION, pConnection: win32more.Windows.Win32.System.RemoteDesktop.ITsSbClientConnection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourceNotificationEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8a47fde-ca91-44d2-b897-3aa28a43b2b7}')
    @commethod(3)
    def NotifySessionChangeEx(self, targetName: win32more.Windows.Win32.Foundation.BSTR, userName: win32more.Windows.Win32.Foundation.BSTR, domain: win32more.Windows.Win32.Foundation.BSTR, sessionId: UInt32, sessionState: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyTargetChangeEx(self, targetName: win32more.Windows.Win32.Foundation.BSTR, targetChangeType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyClientConnectionStateChangeEx(self, userName: win32more.Windows.Win32.Foundation.BSTR, domain: win32more.Windows.Win32.Foundation.BSTR, initialProgram: win32more.Windows.Win32.Foundation.BSTR, poolName: win32more.Windows.Win32.Foundation.BSTR, targetName: win32more.Windows.Win32.Foundation.BSTR, connectionChangeType: win32more.Windows.Win32.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbResourcePlugin(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{ea8db42c-98ed-4535-a88b-2a164f35490f}')
class ITsSbResourcePluginStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c38f65f-bcf1-4036-a6bf-9e3cccae0b63}')
    @commethod(3)
    def QueryTarget(self, TargetName: win32more.Windows.Win32.Foundation.BSTR, FarmName: win32more.Windows.Win32.Foundation.BSTR, ppTarget: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QuerySessionBySessionId(self, dwSessionId: UInt32, TargetName: win32more.Windows.Win32.Foundation.BSTR, ppSession: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddTargetToStore(self, pTarget: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddSessionToStore(self, pSession: win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddEnvironmentToStore(self, pEnvironment: win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveEnvironmentFromStore(self, EnvironmentName: win32more.Windows.Win32.Foundation.BSTR, bIgnoreOwner: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateFarms(self, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryEnvironment(self, EnvironmentName: win32more.Windows.Win32.Foundation.BSTR, ppEnvironment: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumerateEnvironments(self, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveTarget(self, pTarget: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget, bForceWrite: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveEnvironment(self, pEnvironment: win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment, bForceWrite: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SaveSession(self, pSession: win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetTargetProperty(self, TargetName: win32more.Windows.Win32.Foundation.BSTR, PropertyName: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEnvironmentProperty(self, EnvironmentName: win32more.Windows.Win32.Foundation.BSTR, PropertyName: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTargetState(self, targetName: win32more.Windows.Win32.Foundation.BSTR, newState: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE, pOldState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetSessionState(self, sbSession: win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnumerateTargets(self, FarmName: win32more.Windows.Win32.Foundation.BSTR, EnvName: win32more.Windows.Win32.Foundation.BSTR, sortByFieldId: win32more.Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY, sortyByPropName: win32more.Windows.Win32.Foundation.BSTR, pdwCount: POINTER(UInt32), pVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnumerateSessions(self, targetName: win32more.Windows.Win32.Foundation.BSTR, userName: win32more.Windows.Win32.Foundation.BSTR, userDomain: win32more.Windows.Win32.Foundation.BSTR, poolName: win32more.Windows.Win32.Foundation.BSTR, initialProgram: win32more.Windows.Win32.Foundation.BSTR, pSessionState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE), pdwCount: POINTER(UInt32), ppVal: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbSession))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFarmProperty(self, farmName: win32more.Windows.Win32.Foundation.BSTR, propertyName: win32more.Windows.Win32.Foundation.BSTR, pVarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DeleteTarget(self, targetName: win32more.Windows.Win32.Foundation.BSTR, hostName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetTargetPropertyWithVersionCheck(self, pTarget: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTarget, PropertyName: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetEnvironmentPropertyWithVersionCheck(self, pEnvironment: win32more.Windows.Win32.System.RemoteDesktop.ITsSbEnvironment, PropertyName: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AcquireTargetLock(self, targetName: win32more.Windows.Win32.Foundation.BSTR, dwTimeout: UInt32, ppContext: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ReleaseTargetLock(self, pContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def TestAndSetServerState(self, PoolName: win32more.Windows.Win32.Foundation.BSTR, ServerFQDN: win32more.Windows.Win32.Foundation.BSTR, NewState: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE, TestState: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE, pInitState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetServerWaitingToStart(self, PoolName: win32more.Windows.Win32.Foundation.BSTR, serverName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetServerState(self, PoolName: win32more.Windows.Win32.Foundation.BSTR, ServerFQDN: win32more.Windows.Win32.Foundation.BSTR, pState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetServerDrainMode(self, ServerFQDN: win32more.Windows.Win32.Foundation.BSTR, DrainMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbServiceNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86cb68ae-86e0-4f57-8a64-bb7406bc5550}')
    @commethod(3)
    def NotifyServiceFailure(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceSuccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d453aac7-b1d8-4c5e-ba34-9afb4c8c5510}')
    @commethod(3)
    def get_SessionId(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TargetName(self, targetName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_TargetName(self, targetName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Username(self, userName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Domain(self, domain: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_State(self, pState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_State(self, State: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CreateTime(self, pTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_CreateTime(self, Time: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DisconnectTime(self, pTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DisconnectTime(self, Time: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_InitialProgram(self, app: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_InitialProgram(self, Application: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ClientDisplay(self, pClientDisplay: POINTER(win32more.Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ClientDisplay(self, pClientDisplay: win32more.Windows.Win32.System.RemoteDesktop.CLIENT_DISPLAY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ProtocolType(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ProtocolType(self, Val: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{16616ecc-272d-411d-b324-126893033856}')
    @commethod(3)
    def get_TargetName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_TargetName(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_FarmName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_FarmName(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_TargetFQDN(self, TargetFqdnName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_TargetFQDN(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TargetNetbios(self, TargetNetbiosName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_TargetNetbios(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddresses(self, SOCKADDR: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint), numAddresses: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddresses(self, SOCKADDR: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSSD_ConnectionPoint), numAddresses: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TargetState(self, pState: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_TargetState(self, State: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_TargetPropertySet(self, ppPropertySet: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_TargetPropertySet(self, pVal: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTargetPropertySet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_EnvironmentName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_EnvironmentName(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_NumSessions(self, pNumSessions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_NumPendingConnections(self, pNumPendingConnections: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TargetLoad(self, pTargetLoad: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbTargetPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPropertySet
    _iid_ = Guid('{f7bda5d6-994c-4e11-a079-2763b61830ac}')
class ITsSbTaskInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{523d1083-89be-48dd-99ea-04e82ffa7265}')
    @commethod(3)
    def get_TargetId(self, pName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StartTime(self, pStartTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_EndTime(self, pEndTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Deadline(self, pDeadline: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Identifier(self, pIdentifier: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Label(self, pLabel: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Context(self, pContext: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Plugin(self, pPlugin: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbPlugin
    _iid_ = Guid('{fa22ef0f-8705-41be-93bc-44bdbcf1c9c4}')
    @commethod(5)
    def InitializeTaskPlugin(self, pITsSbTaskPluginNotifySink: win32more.Windows.Win32.System.RemoteDesktop.ITsSbTaskPluginNotifySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTaskQueue(self, pszHostName: win32more.Windows.Win32.Foundation.BSTR, SbTaskInfoSize: UInt32, pITsSbTaskInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.ITsSbTaskInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITsSbTaskPluginNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ITsSbBaseNotifySink
    _iid_ = Guid('{6aaf899e-c2ec-45ee-aa37-45e60895261a}')
    @commethod(5)
    def OnSetTaskTime(self, szTargetName: win32more.Windows.Win32.Foundation.BSTR, TaskStartTime: win32more.Windows.Win32.Foundation.FILETIME, TaskEndTime: win32more.Windows.Win32.Foundation.FILETIME, TaskDeadline: win32more.Windows.Win32.Foundation.FILETIME, szTaskLabel: win32more.Windows.Win32.Foundation.BSTR, szTaskIdentifier: win32more.Windows.Win32.Foundation.BSTR, szTaskPlugin: win32more.Windows.Win32.Foundation.BSTR, dwTaskStatus: UInt32, saContext: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDeleteTaskTime(self, szTargetName: win32more.Windows.Win32.Foundation.BSTR, szTaskIdentifier: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUpdateTaskStatus(self, szTargetName: win32more.Windows.Win32.Foundation.BSTR, TaskIdentifier: win32more.Windows.Win32.Foundation.BSTR, TaskStatus: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnReportTasks(self, szHostName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsEnhancedFastReconnectArbitrator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5718ae9b-47f2-499f-b634-d8175bd51131}')
    @commethod(3)
    def GetSessionForEnhancedFastReconnect(self, pSessionIdArray: POINTER(Int32), dwSessionCount: UInt32, pResultSessionId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{684b7a0b-edff-43ad-d5a2-4a8d5388f401}')
    @commethod(3)
    def Write(self, cbSize: UInt32, pBuffer: POINTER(Byte), pContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Open(self, pChannelEvents: win32more.Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannelEvents, pOpenContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{67f2368c-d674-4fae-66a5-d20628a640d2}')
    @commethod(3)
    def OnDataReceived(self, cbSize: UInt32, pBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChannelOpened(self, OpenResult: win32more.Windows.Win32.Foundation.HRESULT, pOpenContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDataSent(self, pWriteContext: win32more.Windows.Win32.System.Com.IUnknown, bCancelled: win32more.Windows.Win32.Foundation.BOOL, pBuffer: POINTER(Byte), cbBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnMetricsUpdate(self, bandwidth: UInt32, RTT: UInt32, lastSentByteIndex: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsGraphicsChannelManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0fd57159-e83e-476a-a8b9-4a7976e71e18}')
    @commethod(3)
    def CreateChannel(self, pszChannelName: POINTER(Byte), channelType: win32more.Windows.Win32.System.RemoteDesktop.WRdsGraphicsChannelType, ppVirtualChannel: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsGraphicsChannel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{324ed94f-fdaf-4ff6-81a8-42abe755830b}')
    @commethod(3)
    def GetLogonErrorRedirector(self, ppLogonErrorRedir: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolLogonErrorRedirector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AcceptConnection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClientData(self, pClientData: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientMonitorData(self, pNumMonitors: POINTER(UInt32), pPrimaryMonitor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(self, pUserCreds: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(self, ppLicenseConnection: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolLicenseConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID), SessionHandle: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInputHandles(self, pKeyboardHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetVideoHandle(self, pVideoHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConnectNotify(self, SessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUserAllowedToLogon(self, SessionId: UInt32, UserToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, pDomainName: win32more.Windows.Win32.Foundation.PWSTR, pUserName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SessionArbitrationEnumeration(self, hUserToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: win32more.Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def LogonNotify(self, hClientToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, wszUserName: win32more.Windows.Win32.Foundation.PWSTR, wszDomainName: win32more.Windows.Win32.Foundation.PWSTR, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID), pWRdsConnectionSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PreDisconnect(self, DisconnectReason: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DisconnectNotify(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetProtocolStatus(self, pProtocolStatus: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetLastInputTime(self, pLastInputTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetErrorInfo(self, ulError: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(self, szEndpointName: win32more.Windows.Win32.Foundation.PSTR, bStatic: win32more.Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(self, QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE), pPropertyEntriesOut: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(self, ppShadowConnection: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyCommandProcessCreated(self, SessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f1d70332-d070-4ef1-a088-78313536c2d6}')
    @commethod(3)
    def OnReady(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(self, Reason: UInt32, Source: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(self, rect: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetConnectionId(self, pConnectionId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolConnectionSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83fcf5d3-f6f4-ea94-9cd2-32f280e1e510}')
    @commethod(3)
    def SetConnectionSetting(self, PropertyID: Guid, pPropertyEntriesIn: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionSetting(self, PropertyID: Guid, pPropertyEntriesOut: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLicenseConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d6a145f-d095-4424-957a-407fae822d84}')
    @commethod(3)
    def RequestLicensingCapabilities(self, ppLicenseCapabilities: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES), pcbLicenseCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(self, pClientLicense: POINTER(Byte), cbClientLicense: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(self, Reserve1: POINTER(Byte), Reserve2: UInt32, ppClientLicense: POINTER(Byte), pcbClientLicense: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(self, ulComplete: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListener(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcbc131b-c686-451d-a773-e279e230f540}')
    @commethod(3)
    def GetSettings(self, WRdsListenerSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL, pWRdsListenerSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartListen(self, pCallback: win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolListenerCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopListen(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolListenerCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3ab27e5b-4449-4dc1-b74a-91621d4fe984}')
    @commethod(3)
    def OnConnected(self, pConnection: win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnection, pWRdsConnectionSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS), pCallback: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolConnectionCallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolLogonErrorRedirector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{519fe83b-142a-4120-a3d5-a405d315281a}')
    @commethod(3)
    def OnBeginPainting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(self, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(self, pszCaption: win32more.Windows.Win32.Foundation.PWSTR, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(self, ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: win32more.Windows.Win32.Foundation.PWSTR, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc796967-3abb-40cd-a446-105276b58950}')
    @commethod(3)
    def Initialize(self, pIWRdsSettings: win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolSettings, pWRdsSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateListener(self, wszListenerName: win32more.Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolListener)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyServiceStateChange(self, pTSServiceStateChange: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStart(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionOfServiceStop(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifySessionStateChange(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID), EventId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NotifySettingsChange(self, pWRdsSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Uninitialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{654a5a6a-2550-47eb-b6f7-ebd637475265}')
    @commethod(3)
    def GetSettings(self, WRdsSettingType: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE, WRdsSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL, pWRdsSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MergeSettings(self, pWRdsSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS), WRdsConnectionSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL, pWRdsConnectionSettings: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e0667ce0-0372-40d6-adb2-a0f3322674d6}')
    @commethod(3)
    def StopShadow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(self, pTargetServerName: win32more.Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsProtocolShadowConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ae85ce6-cade-4548-8feb-99016597f60a}')
    @commethod(3)
    def Start(self, pTargetServerName: win32more.Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: win32more.Windows.Win32.System.RemoteDesktop.IWRdsProtocolShadowCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(self, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsWddmIddProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1382df4d-a289-43d1-a184-144726f9af90}')
    @commethod(3)
    def GetHardwareId(self, pDisplayDriverHardwareId: win32more.Windows.Win32.Foundation.PWSTR, Count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDriverLoad(self, SessionId: UInt32, DriverHandle: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDriverUnload(self, SessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableWddmIdd(self, Enabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWRdsWddmIddProps1(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{60f71b1a-3682-4bc7-997e-4e4f02a08148}')
    @commethod(3)
    def GetHardwareId(self, pDisplayDriverHardwareId: win32more.Windows.Win32.Foundation.PWSTR, Count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDriverLoad(self, SessionId: UInt32, DeviceInstance: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDriverUnload(self, SessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea326091-05fe-40c1-b49c-3d2ef4626a0e}')
    @commethod(3)
    def GetMappedRenderer(self, mappingId: UInt64, pMappedRendererCallback: win32more.Windows.Win32.System.RemoteDesktop.IWTSBitmapRendererCallback, ppMappedRenderer: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSBitmapRenderer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRenderer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b7acc97-f3c9-46f7-8c5b-fa685d3441b1}')
    @commethod(3)
    def Render(self, imageFormat: Guid, dwWidth: UInt32, dwHeight: UInt32, cbStride: Int32, cbImageBuffer: UInt32, pImageBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRendererStatistics(self, pStatistics: POINTER(win32more.Windows.Win32.System.RemoteDesktop.BITMAP_RENDERER_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveMapping(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSBitmapRendererCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d782928e-fe4e-4e77-ae90-9cd0b3e3b353}')
    @commethod(3)
    def OnTargetSizeChanged(self, rcNewSize: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSListener(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230206-9a39-4d58-8674-cdb4dff4e73b}')
    @commethod(3)
    def GetConfiguration(self, ppPropertyBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSListenerCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230203-d6a7-11d8-b9fd-000bdbd1f198}')
    @commethod(3)
    def OnNewChannelConnection(self, pChannel: win32more.Windows.Win32.System.RemoteDesktop.IWTSVirtualChannel, data: win32more.Windows.Win32.Foundation.BSTR, pbAccept: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppCallback: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelCallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230201-1439-4e62-a414-190d0ac3d40e}')
    @commethod(3)
    def Initialize(self, pChannelMgr: win32more.Windows.Win32.System.RemoteDesktop.IWTSVirtualChannelManager) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnected(self, dwDisconnectCode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminated(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSPluginServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d3e07363-087c-476c-86a7-dbb15f46ddb4}')
    @commethod(3)
    def GetService(self, ServiceId: Guid, ppunkObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23083765-9095-4648-98bf-ef81c914032d}')
    @commethod(3)
    def GetLogonErrorRedirector(self, ppLogonErrorRedir: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolLogonErrorRedirector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendPolicyData(self, pPolicyData: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AcceptConnection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClientData(self, pClientData: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_CLIENT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUserCredentials(self, pUserCreds: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_USER_CREDENTIAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLicenseConnection(self, ppLicenseConnection: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolLicenseConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AuthenticateClientToSession(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifySessionId(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProtocolHandles(self, pKeyboardHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR), pMouseHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR), pBeepHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR), pVideoHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ConnectNotify(self, SessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsUserAllowedToLogon(self, SessionId: UInt32, UserToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, pDomainName: win32more.Windows.Win32.Foundation.PWSTR, pUserName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SessionArbitrationEnumeration(self, hUserToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, bSingleSessionPerUserEnabled: win32more.Windows.Win32.Foundation.BOOL, pSessionIdArray: POINTER(UInt32), pdwSessionIdentifierCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LogonNotify(self, hClientToken: win32more.Windows.Win32.Foundation.HANDLE_PTR, wszUserName: win32more.Windows.Win32.Foundation.PWSTR, wszDomainName: win32more.Windows.Win32.Foundation.PWSTR, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserData(self, pPolicyData: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_POLICY_DATA), pClientData: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_USER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DisconnectNotify(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetProtocolStatus(self, pProtocolStatus: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetLastInputTime(self, pLastInputTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetErrorInfo(self, ulError: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SendBeep(self, Frequency: UInt32, Duration: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateVirtualChannel(self, szEndpointName: win32more.Windows.Win32.Foundation.PSTR, bStatic: win32more.Windows.Win32.Foundation.BOOL, RequestedPriority: UInt32, phChannel: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryProperty(self, QueryType: Guid, ulNumEntriesIn: UInt32, ulNumEntriesOut: UInt32, pPropertyEntriesIn: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE), pPropertyEntriesOut: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_PROPERTY_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetShadowConnection(self, ppShadowConnection: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowConnection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolConnectionCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23083765-75eb-41fe-b4fb-e086242afa0f}')
    @commethod(3)
    def OnReady(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BrokenConnection(self, Reason: UInt32, Source: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopScreenUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedrawWindow(self, rect: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SMALL_RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DisplayIOCtl(self, DisplayIOCtl: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_DISPLAY_IOCTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLicenseConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23083765-178c-4079-8e4a-fea6496a4d70}')
    @commethod(3)
    def RequestLicensingCapabilities(self, ppLicenseCapabilities: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES), pcbLicenseCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendClientLicense(self, pClientLicense: POINTER(Byte), cbClientLicense: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestClientLicense(self, Reserve1: POINTER(Byte), Reserve2: UInt32, ppClientLicense: POINTER(Byte), pcbClientLicense: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProtocolComplete(self, ulComplete: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListener(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23083765-45f0-4394-8f69-32b2bc0ef4ca}')
    @commethod(3)
    def StartListen(self, pCallback: win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolListenerCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopListen(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolListenerCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23083765-1a2d-4de2-97de-4a35f260f0b3}')
    @commethod(3)
    def OnConnected(self, pConnection: win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolConnection, pCallback: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolConnectionCallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolLogonErrorRedirector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd9b61a7-2916-4627-8dee-4328711ad6cb}')
    @commethod(3)
    def OnBeginPainting(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RedirectStatus(self, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RedirectMessage(self, pszCaption: win32more.Windows.Win32.Foundation.PWSTR, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RedirectLogonError(self, ntsStatus: Int32, ntsSubstatus: Int32, pszCaption: win32more.Windows.Win32.Foundation.PWSTR, pszMessage: win32more.Windows.Win32.Foundation.PWSTR, uType: UInt32, pResponse: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9eaf6cc-ed79-4f01-821d-1f881b9f66cc}')
    @commethod(3)
    def CreateListener(self, wszListenerName: win32more.Windows.Win32.Foundation.PWSTR, pProtocolListener: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolListener)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyServiceStateChange(self, pTSServiceStateChange: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SERVICE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifySessionOfServiceStart(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifySessionOfServiceStop(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifySessionStateChange(self, SessionId: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTS_SESSION_ID), EventId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{503a2504-aae5-4ab1-93e0-6d1c4bc6f71a}')
    @commethod(3)
    def StopShadow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeTargetShadow(self, pTargetServerName: win32more.Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSProtocolShadowConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee3b0c14-37fb-456b-bab3-6d6cd51e13bf}')
    @commethod(3)
    def Start(self, pTargetServerName: win32more.Windows.Win32.Foundation.PWSTR, TargetSessionId: UInt32, HotKeyVk: Byte, HotkeyModifiers: UInt16, pShadowCallback: win32more.Windows.Win32.System.RemoteDesktop.IWTSProtocolShadowCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoTarget(self, pParam1: POINTER(Byte), Param1Size: UInt32, pParam2: POINTER(Byte), Param2Size: UInt32, pParam3: POINTER(Byte), Param3Size: UInt32, pParam4: POINTER(Byte), Param4Size: UInt32, pClientName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSSBPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc44be78-b18d-4399-b210-641bf67a002c}')
    @commethod(3)
    def Initialize(self, PluginCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WTSSBX_MachineChangeNotification(self, NotificationType: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, pMachineInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WTSSBX_SessionChangeNotification(self, NotificationType: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE, MachineId: Int32, NumOfSessions: UInt32, SessionInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WTSSBX_GetMostSuitableServer(self, UserName: win32more.Windows.Win32.Foundation.PWSTR, DomainName: win32more.Windows.Win32.Foundation.PWSTR, ApplicationType: win32more.Windows.Win32.Foundation.PWSTR, FarmName: win32more.Windows.Win32.Foundation.PWSTR, pMachineId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Terminated(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WTSSBX_GetUserExternalSession(self, UserName: win32more.Windows.Win32.Foundation.PWSTR, DomainName: win32more.Windows.Win32.Foundation.PWSTR, ApplicationType: win32more.Windows.Win32.Foundation.PWSTR, RedirectorInternalIP: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS), pSessionId: POINTER(UInt32), pMachineConnectInfo: POINTER(win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230207-d6a7-11d8-b9fd-000bdbd1f198}')
    @commethod(3)
    def Write(self, cbSize: UInt32, pBuffer: POINTER(Byte), pReserved: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230204-d6a7-11d8-b9fd-000bdbd1f198}')
    @commethod(3)
    def OnDataReceived(self, cbSize: UInt32, pBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWTSVirtualChannelManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1230205-d6a7-11d8-b9fd-000bdbd1f198}')
    @commethod(3)
    def CreateListener(self, pszChannelName: win32more.Windows.Win32.Foundation.PSTR, uFlags: UInt32, pListenerCallback: win32more.Windows.Win32.System.RemoteDesktop.IWTSListenerCallback, ppListener: POINTER(win32more.Windows.Win32.System.RemoteDesktop.IWTSListener)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b922bbb8-4c55-4fea-8496-beb0b44285e5}')
    @commethod(3)
    def GetWorkspaceNames(self, psaWkspNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartRemoteApplication(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, psaParams: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProcessId(self, pulProcessId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspace2(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.IWorkspace
    _iid_ = Guid('{96d8d7cf-783e-4286-834c-ebc0e95f783c}')
    @commethod(6)
    def StartRemoteApplicationEx(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrRequestingAppId: win32more.Windows.Win32.Foundation.BSTR, bstrRequestingAppFamilyName: win32more.Windows.Win32.Foundation.BSTR, bLaunchIntoImmersiveClient: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrImmersiveClientActivationContext: win32more.Windows.Win32.Foundation.BSTR, psaParams: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspace3(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.IWorkspace2
    _iid_ = Guid('{1becbe4a-d654-423b-afeb-be8d532c13c6}')
    @commethod(7)
    def GetClaimsToken2(self, bstrClaimsHint: win32more.Windows.Win32.Foundation.BSTR, bstrUserHint: win32more.Windows.Win32.Foundation.BSTR, claimCookie: UInt32, hwndCredUiParent: UInt32, rectCredUiParent: win32more.Windows.Win32.Foundation.RECT, pbstrAccessToken: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetClaimsToken(self, bstrAccessToken: win32more.Windows.Win32.Foundation.BSTR, ullAccessTokenExpiration: UInt64, bstrRefreshToken: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceClientExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12b952f4-41ca-4f21-a829-a6d07d9a16e5}')
    @commethod(3)
    def GetResourceId(self, bstrWorkspaceId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResourceDisplayName(self, bstrWorkspaceDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IssueDisconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b922bbb8-4c55-4fea-8496-beb0b44285e6}')
    @commethod(3)
    def AddResource(self, pUnk: win32more.Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveResource(self, dwCookieConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceRegistration2(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.IWorkspaceRegistration
    _iid_ = Guid('{cf59f654-39bb-44d8-94d0-4635728957e9}')
    @commethod(5)
    def AddResourceEx(self, pUnk: win32more.Windows.Win32.System.RemoteDesktop.IWorkspaceClientExt, bstrEventLogUploadAddress: win32more.Windows.Win32.Foundation.BSTR, pdwCookie: POINTER(UInt32), correlationId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveResourceEx(self, dwCookieConnection: UInt32, correlationId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceReportMessage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7c06739-500f-4e8c-99a8-2bd6955899eb}')
    @commethod(3)
    def RegisterErrorLogMessage(self, bstrMessage: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsErrorMessageRegistered(self, bstrWkspId: win32more.Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: win32more.Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32, pfErrorExist: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterErrorEvent(self, bstrWkspId: win32more.Windows.Win32.Foundation.BSTR, dwErrorType: UInt32, bstrErrorMessageType: win32more.Windows.Win32.Foundation.BSTR, dwErrorCode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceResTypeRegistry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1d428c79-6e2e-4351-a361-c0401a03a0ba}')
    @commethod(7)
    def AddResourceType(self, fMachineWide: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: win32more.Windows.Win32.Foundation.BSTR, bstrLauncher: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteResourceType(self, fMachineWide: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRegisteredFileExtensions(self, fMachineWide: win32more.Windows.Win32.Foundation.VARIANT_BOOL, psaFileExtensions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResourceTypeInfo(self, fMachineWide: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: win32more.Windows.Win32.Foundation.BSTR, pbstrLauncher: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ModifyResourceType(self, fMachineWide: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrFileExtension: win32more.Windows.Win32.Foundation.BSTR, bstrLauncher: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{efea49a2-dda5-429d-8f42-b23b92c4c347}')
    @commethod(7)
    def DisconnectWorkspace(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartWorkspace(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: win32more.Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsWorkspaceCredentialSpecified(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bCountUnauthenticatedCredentials: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pbCredExist: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsWorkspaceSSOEnabled(self, pbSSOEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearWorkspaceCredential(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnAuthenticated(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DisconnectWorkspaceByFriendlyName(self, bstrWorkspaceFriendlyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable2(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable
    _iid_ = Guid('{efea49a2-dda5-429d-8f42-b33ba2c4c348}')
    @commethod(14)
    def StartWorkspaceEx(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: win32more.Windows.Win32.Foundation.BSTR, bstrRedirectorName: win32more.Windows.Win32.Foundation.BSTR, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bstrAppContainer: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: win32more.Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ResourceDismissed(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWorkspaceScriptable3(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.IWorkspaceScriptable2
    _iid_ = Guid('{531e6512-2cbf-4bd2-80a5-d90a71636a9a}')
    @commethod(16)
    def StartWorkspaceEx2(self, bstrWorkspaceId: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceFriendlyName: win32more.Windows.Win32.Foundation.BSTR, bstrRedirectorName: win32more.Windows.Win32.Foundation.BSTR, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bstrAppContainer: win32more.Windows.Win32.Foundation.BSTR, bstrWorkspaceParams: win32more.Windows.Win32.Foundation.BSTR, lTimeout: Int32, lFlags: Int32, bstrEventLogUploadAddress: win32more.Windows.Win32.Foundation.BSTR, correlationId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70c04b05-f347-412b-822f-36c99c54ca45}')
    @commethod(3)
    def GetResourceList(self, userID: win32more.Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.pluginResource))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(self, alias: win32more.Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(win32more.Windows.Win32.System.RemoteDesktop.pluginResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCacheLastUpdateTime(self, lastUpdateTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_pluginName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_pluginVersion(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResolveResource(self, resourceType: POINTER(UInt32), resourceLocation: win32more.Windows.Win32.Foundation.PWSTR, endPointName: win32more.Windows.Win32.Foundation.PWSTR, userID: win32more.Windows.Win32.Foundation.PWSTR, alias: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ItsPubPlugin2(ComPtr):
    extends: win32more.Windows.Win32.System.RemoteDesktop.ItsPubPlugin
    _iid_ = Guid('{fa4ce418-aad7-4ec6-bad1-0a321ba465d5}')
    @commethod(9)
    def GetResource2List(self, userID: win32more.Windows.Win32.Foundation.PWSTR, pceAppListSize: POINTER(Int32), resourceList: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.pluginResource2))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetResource2(self, alias: win32more.Windows.Win32.Foundation.PWSTR, flags: Int32, resource: POINTER(win32more.Windows.Win32.System.RemoteDesktop.pluginResource2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResolvePersonalDesktop(self, userId: win32more.Windows.Win32.Foundation.PWSTR, poolId: win32more.Windows.Win32.Foundation.PWSTR, ePdResolutionType: win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE, pPdAssignmentType: POINTER(win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE), endPointName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeletePersonalDesktopAssignment(self, userId: win32more.Windows.Win32.Foundation.PWSTR, poolId: win32more.Windows.Win32.Foundation.PWSTR, endpointName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
KeyCombinationType = Int32
KeyCombinationHome: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 0
KeyCombinationLeft: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 1
KeyCombinationUp: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 2
KeyCombinationRight: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 3
KeyCombinationDown: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 4
KeyCombinationScroll: win32more.Windows.Win32.System.RemoteDesktop.KeyCombinationType = 5
@winfunctype_pointer
def PCHANNEL_INIT_EVENT_FN(pInitHandle: VoidPtr, event: UInt32, pData: VoidPtr, dataLength: UInt32) -> Void: ...
@winfunctype_pointer
def PCHANNEL_OPEN_EVENT_FN(openHandle: UInt32, event: UInt32, pData: VoidPtr, dataLength: UInt32, totalLength: UInt32, dataFlags: UInt32) -> Void: ...
PLUGIN_TYPE = Int32
UNKNOWN_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 0
POLICY_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 1
RESOURCE_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 2
LOAD_BALANCING_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 4
PLACEMENT_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 8
ORCHESTRATION_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 16
PROVISIONING_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 32
TASK_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.PLUGIN_TYPE = 64
class PRODUCT_INFOA(Structure):
    CompanyName: win32more.Windows.Win32.Foundation.CHAR * 256
    ProductID: win32more.Windows.Win32.Foundation.CHAR * 4
class PRODUCT_INFOW(Structure):
    CompanyName: Char * 256
    ProductID: Char * 4
PRODUCT_INFO = UnicodeAlias('PRODUCT_INFOW')
@winfunctype_pointer
def PVIRTUALCHANNELCLOSE(openHandle: UInt32) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELENTRY(pEntryPoints: POINTER(win32more.Windows.Win32.System.RemoteDesktop.CHANNEL_ENTRY_POINTS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PVIRTUALCHANNELINIT(ppInitHandle: POINTER(VoidPtr), pChannel: POINTER(win32more.Windows.Win32.System.RemoteDesktop.CHANNEL_DEF), channelCount: Int32, versionRequested: UInt32, pChannelInitEventProc: win32more.Windows.Win32.System.RemoteDesktop.PCHANNEL_INIT_EVENT_FN) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELOPEN(pInitHandle: VoidPtr, pOpenHandle: POINTER(UInt32), pChannelName: win32more.Windows.Win32.Foundation.PSTR, pChannelOpenEventProc: win32more.Windows.Win32.System.RemoteDesktop.PCHANNEL_OPEN_EVENT_FN) -> UInt32: ...
@winfunctype_pointer
def PVIRTUALCHANNELWRITE(openHandle: UInt32, pData: VoidPtr, dataLength: UInt32, pUserData: VoidPtr) -> UInt32: ...
PasswordEncodingType = Int32
PasswordEncodingUTF8: win32more.Windows.Win32.System.RemoteDesktop.PasswordEncodingType = 0
PasswordEncodingUTF16LE: win32more.Windows.Win32.System.RemoteDesktop.PasswordEncodingType = 1
PasswordEncodingUTF16BE: win32more.Windows.Win32.System.RemoteDesktop.PasswordEncodingType = 2
PolicyAttributeType = Int32
EnableAllRedirections: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 0
DisableAllRedirections: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 1
DriveRedirectionDisabled: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 2
PrinterRedirectionDisabled: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 3
PortRedirectionDisabled: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 4
ClipboardRedirectionDisabled: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 5
PnpRedirectionDisabled: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 6
AllowOnlySDRServers: win32more.Windows.Win32.System.RemoteDesktop.PolicyAttributeType = 7
RDV_TASK_STATUS = Int32
RDV_TASK_STATUS_UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 0
RDV_TASK_STATUS_SEARCHING: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 1
RDV_TASK_STATUS_DOWNLOADING: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 2
RDV_TASK_STATUS_APPLYING: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 3
RDV_TASK_STATUS_REBOOTING: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 4
RDV_TASK_STATUS_REBOOTED: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 5
RDV_TASK_STATUS_SUCCESS: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 6
RDV_TASK_STATUS_FAILED: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 7
RDV_TASK_STATUS_TIMEOUT: win32more.Windows.Win32.System.RemoteDesktop.RDV_TASK_STATUS = 8
RD_FARM_TYPE = Int32
RD_FARM_RDSH: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 0
RD_FARM_TEMP_VM: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 1
RD_FARM_MANUAL_PERSONAL_VM: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 2
RD_FARM_AUTO_PERSONAL_VM: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 3
RD_FARM_MANUAL_PERSONAL_RDSH: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 4
RD_FARM_AUTO_PERSONAL_RDSH: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = 5
RD_FARM_TYPE_UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.RD_FARM_TYPE = -1
class RFX_GFX_MONITOR_INFO(Structure):
    left: Int32
    top: Int32
    right: Int32
    bottom: Int32
    physicalWidth: UInt32
    physicalHeight: UInt32
    orientation: UInt32
    primary: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    reserved: UInt32
    monitorCount: UInt32
    MonitorData: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MONITOR_INFO * 16
    clientUniqueId: Char * 32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    ulBpp: UInt32
    Reserved: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_INPUT_RESET(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    ulWidth: UInt32
    ulHeight: UInt32
    _pack_ = 1
class RFX_GFX_MSG_DESKTOP_RESEND_REQUEST(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    RedrawRect: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_RECT
class RFX_GFX_MSG_DISCONNECT_NOTIFY(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    DisconnectReason: UInt32
    _pack_ = 1
class RFX_GFX_MSG_HEADER(Structure):
    uMSGType: UInt16
    cbSize: UInt16
    _pack_ = 1
class RFX_GFX_MSG_RDP_DATA(Structure):
    channelHdr: win32more.Windows.Win32.System.RemoteDesktop.RFX_GFX_MSG_HEADER
    rdpData: Byte * 1
class RFX_GFX_RECT(Structure):
    left: Int32
    top: Int32
    right: Int32
    bottom: Int32
    _pack_ = 1
RemoteActionType = Int32
RemoteActionCharms: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType = 0
RemoteActionAppbar: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType = 1
RemoteActionSnap: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType = 2
RemoteActionStartScreen: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType = 3
RemoteActionAppSwitch: win32more.Windows.Win32.System.RemoteDesktop.RemoteActionType = 4
SESSION_TIMEOUT_ACTION_TYPE = Int32
SESSION_TIMEOUT_ACTION_DISCONNECT: win32more.Windows.Win32.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE = 0
SESSION_TIMEOUT_ACTION_SILENT_REAUTH: win32more.Windows.Win32.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE = 1
SnapshotEncodingType = Int32
SnapshotEncodingDataUri: win32more.Windows.Win32.System.RemoteDesktop.SnapshotEncodingType = 0
SnapshotFormatType = Int32
SnapshotFormatPng: win32more.Windows.Win32.System.RemoteDesktop.SnapshotFormatType = 0
SnapshotFormatJpeg: win32more.Windows.Win32.System.RemoteDesktop.SnapshotFormatType = 1
SnapshotFormatBmp: win32more.Windows.Win32.System.RemoteDesktop.SnapshotFormatType = 2
TARGET_CHANGE_TYPE = Int32
TARGET_CHANGE_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 1
TARGET_EXTERNALIP_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 2
TARGET_INTERNALIP_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 4
TARGET_JOINED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 8
TARGET_REMOVED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 16
TARGET_STATE_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 32
TARGET_IDLE: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 64
TARGET_PENDING: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 128
TARGET_INUSE: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 256
TARGET_PATCH_STATE_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 512
TARGET_FARM_MEMBERSHIP_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_CHANGE_TYPE = 1024
TARGET_OWNER = Int32
OWNER_UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_OWNER = 0
OWNER_MS_TS_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_OWNER = 1
OWNER_MS_VM_PLUGIN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_OWNER = 2
TARGET_PATCH_STATE = Int32
TARGET_PATCH_UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_PATCH_STATE = 0
TARGET_PATCH_NOT_STARTED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_PATCH_STATE = 1
TARGET_PATCH_IN_PROGRESS: win32more.Windows.Win32.System.RemoteDesktop.TARGET_PATCH_STATE = 2
TARGET_PATCH_COMPLETED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_PATCH_STATE = 3
TARGET_PATCH_FAILED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_PATCH_STATE = 4
TARGET_STATE = Int32
TARGET_UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 1
TARGET_INITIALIZING: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 2
TARGET_RUNNING: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 3
TARGET_DOWN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 4
TARGET_HIBERNATED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 5
TARGET_CHECKED_OUT: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 6
TARGET_STOPPED: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 7
TARGET_INVALID: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 8
TARGET_STARTING: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 9
TARGET_STOPPING: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 10
TARGET_MAXSTATE: win32more.Windows.Win32.System.RemoteDesktop.TARGET_STATE = 11
TARGET_TYPE = Int32
UNKNOWN: win32more.Windows.Win32.System.RemoteDesktop.TARGET_TYPE = 0
FARM: win32more.Windows.Win32.System.RemoteDesktop.TARGET_TYPE = 1
NONFARM: win32more.Windows.Win32.System.RemoteDesktop.TARGET_TYPE = 2
TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = Int32
TSPUB_PLUGIN_PD_ASSIGNMENT_NEW: win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = 0
TSPUB_PLUGIN_PD_ASSIGNMENT_EXISTING: win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = 1
TSPUB_PLUGIN_PD_RESOLUTION_TYPE = Int32
TSPUB_PLUGIN_PD_QUERY_OR_CREATE: win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE = 0
TSPUB_PLUGIN_PD_QUERY_EXISTING: win32more.Windows.Win32.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE = 1
TSSB_NOTIFICATION_TYPE = Int32
TSSB_NOTIFY_INVALID: win32more.Windows.Win32.System.RemoteDesktop.TSSB_NOTIFICATION_TYPE = 0
TSSB_NOTIFY_TARGET_CHANGE: win32more.Windows.Win32.System.RemoteDesktop.TSSB_NOTIFICATION_TYPE = 1
TSSB_NOTIFY_SESSION_CHANGE: win32more.Windows.Win32.System.RemoteDesktop.TSSB_NOTIFICATION_TYPE = 2
TSSB_NOTIFY_CONNECTION_REQUEST_CHANGE: win32more.Windows.Win32.System.RemoteDesktop.TSSB_NOTIFICATION_TYPE = 4
TSSD_AddrV46Type = Int32
TSSD_ADDR_UNDEFINED: win32more.Windows.Win32.System.RemoteDesktop.TSSD_AddrV46Type = 0
TSSD_ADDR_IPv4: win32more.Windows.Win32.System.RemoteDesktop.TSSD_AddrV46Type = 4
TSSD_ADDR_IPv6: win32more.Windows.Win32.System.RemoteDesktop.TSSD_AddrV46Type = 6
class TSSD_ConnectionPoint(Structure):
    ServerAddressB: Byte * 16
    AddressType: win32more.Windows.Win32.System.RemoteDesktop.TSSD_AddrV46Type
    PortNumber: UInt16
    AddressScope: UInt32
TSSESSION_STATE = Int32
STATE_INVALID: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = -1
STATE_ACTIVE: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 0
STATE_CONNECTED: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 1
STATE_CONNECTQUERY: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 2
STATE_SHADOW: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 3
STATE_DISCONNECTED: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 4
STATE_IDLE: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 5
STATE_LISTEN: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 6
STATE_RESET: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 7
STATE_DOWN: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 8
STATE_INIT: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 9
STATE_MAX: win32more.Windows.Win32.System.RemoteDesktop.TSSESSION_STATE = 10
TSUserExInterfaces = Guid('{0910dd01-df8c-11d1-ae27-00c04fa35813}')
TS_SB_SORT_BY = Int32
TS_SB_SORT_BY_NONE: win32more.Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY = 0
TS_SB_SORT_BY_NAME: win32more.Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY = 1
TS_SB_SORT_BY_PROP: win32more.Windows.Win32.System.RemoteDesktop.TS_SB_SORT_BY = 2
VM_HOST_NOTIFY_STATUS = Int32
VM_HOST_STATUS_INIT_PENDING: win32more.Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS = 0
VM_HOST_STATUS_INIT_IN_PROGRESS: win32more.Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS = 1
VM_HOST_STATUS_INIT_COMPLETE: win32more.Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS = 2
VM_HOST_STATUS_INIT_FAILED: win32more.Windows.Win32.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS = 3
class VM_NOTIFY_ENTRY(Structure):
    VmName: Char * 128
    VmHost: Char * 128
class VM_NOTIFY_INFO(Structure):
    dwNumEntries: UInt32
    ppVmEntries: POINTER(POINTER(win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_ENTRY))
VM_NOTIFY_STATUS = Int32
VM_NOTIFY_STATUS_PENDING: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS = 0
VM_NOTIFY_STATUS_IN_PROGRESS: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS = 1
VM_NOTIFY_STATUS_COMPLETE: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS = 2
VM_NOTIFY_STATUS_FAILED: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS = 3
VM_NOTIFY_STATUS_CANCELED: win32more.Windows.Win32.System.RemoteDesktop.VM_NOTIFY_STATUS = 4
class VM_PATCH_INFO(Structure):
    dwNumEntries: UInt32
    pVmNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class WRDS_CONNECTION_SETTING(Union):
    WRdsConnectionSettings1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_1
class WRDS_CONNECTION_SETTINGS(Structure):
    WRdsConnectionSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL
    WRdsConnectionSetting: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING
class WRDS_CONNECTION_SETTINGS_1(Structure):
    fInheritInitialProgram: win32more.Windows.Win32.Foundation.BOOLEAN
    fInheritColorDepth: win32more.Windows.Win32.Foundation.BOOLEAN
    fHideTitleBar: win32more.Windows.Win32.Foundation.BOOLEAN
    fInheritAutoLogon: win32more.Windows.Win32.Foundation.BOOLEAN
    fMaximizeShell: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisablePNP: win32more.Windows.Win32.Foundation.BOOLEAN
    fPasswordIsScPin: win32more.Windows.Win32.Foundation.BOOLEAN
    fPromptForPassword: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCpm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableClip: win32more.Windows.Win32.Foundation.BOOLEAN
    fResetBroken: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableEncryption: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableAutoReconnect: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCtrlAltDel: win32more.Windows.Win32.Foundation.BOOLEAN
    fDoubleClickDetect: win32more.Windows.Win32.Foundation.BOOLEAN
    fEnableWindowsKey: win32more.Windows.Win32.Foundation.BOOLEAN
    fUsingSavedCreds: win32more.Windows.Win32.Foundation.BOOLEAN
    fMouse: win32more.Windows.Win32.Foundation.BOOLEAN
    fNoAudioPlayback: win32more.Windows.Win32.Foundation.BOOLEAN
    fRemoteConsoleAudio: win32more.Windows.Win32.Foundation.BOOLEAN
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
    ClientSockAddress: win32more.Windows.Win32.System.RemoteDesktop.WTS_SOCKADDR
    ClientTimeZone: win32more.Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
    WRdsListenerSettings: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS
    EventLogActivityId: Guid
    ContextSize: UInt32
    ContextData: POINTER(Byte)
WRDS_CONNECTION_SETTING_LEVEL = Int32
WRDS_CONNECTION_SETTING_LEVEL_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL = 0
WRDS_CONNECTION_SETTING_LEVEL_1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL = 1
class WRDS_DYNAMIC_TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: win32more.Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: win32more.Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    DaylightBias: Int32
    TimeZoneKeyName: Char * 128
    DynamicDaylightTimeDisabled: UInt16
class WRDS_LISTENER_SETTING(Union):
    WRdsListenerSettings1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_1
class WRDS_LISTENER_SETTINGS(Structure):
    WRdsListenerSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL
    WRdsListenerSetting: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING
class WRDS_LISTENER_SETTINGS_1(Structure):
    MaxProtocolListenerConnectionCount: UInt32
    SecurityDescriptorSize: UInt32
    pSecurityDescriptor: POINTER(Byte)
WRDS_LISTENER_SETTING_LEVEL = Int32
WRDS_LISTENER_SETTING_LEVEL_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL = 0
WRDS_LISTENER_SETTING_LEVEL_1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL = 1
class WRDS_SETTING(Union):
    WRdsSettings1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTINGS_1
class WRDS_SETTINGS(Structure):
    WRdsSettingType: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE
    WRdsSettingLevel: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL
    WRdsSetting: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING
class WRDS_SETTINGS_1(Structure):
    WRdsDisableClipStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableClipValue: UInt32
    WRdsDisableLPTStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableLPTValue: UInt32
    WRdsDisableCcmStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCcmValue: UInt32
    WRdsDisableCdmStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCdmValue: UInt32
    WRdsDisableCpmStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableCpmValue: UInt32
    WRdsDisablePnpStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisablePnpValue: UInt32
    WRdsEncryptionLevelStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsEncryptionValue: UInt32
    WRdsColorDepthStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsColorDepthValue: UInt32
    WRdsDisableAutoReconnecetStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableAutoReconnecetValue: UInt32
    WRdsDisableEncryptionStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsDisableEncryptionValue: UInt32
    WRdsResetBrokenStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsResetBrokenValue: UInt32
    WRdsMaxIdleTimeStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxIdleTimeValue: UInt32
    WRdsMaxDisconnectTimeStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxDisconnectTimeValue: UInt32
    WRdsMaxConnectTimeStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsMaxConnectTimeValue: UInt32
    WRdsKeepAliveStatus: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS
    WRdsKeepAliveStartValue: win32more.Windows.Win32.Foundation.BOOLEAN
    WRdsKeepAliveIntervalValue: UInt32
WRDS_SETTING_LEVEL = Int32
WRDS_SETTING_LEVEL_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL = 0
WRDS_SETTING_LEVEL_1: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_LEVEL = 1
WRDS_SETTING_STATUS = Int32
WRDS_SETTING_STATUS_NOTAPPLICABLE: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS = -1
WRDS_SETTING_STATUS_DISABLED: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS = 0
WRDS_SETTING_STATUS_ENABLED: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS = 1
WRDS_SETTING_STATUS_NOTCONFIGURED: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_STATUS = 2
WRDS_SETTING_TYPE = Int32
WRDS_SETTING_TYPE_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE = 0
WRDS_SETTING_TYPE_MACHINE: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE = 1
WRDS_SETTING_TYPE_USER: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE = 2
WRDS_SETTING_TYPE_SAM: win32more.Windows.Win32.System.RemoteDesktop.WRDS_SETTING_TYPE = 3
WRdsGraphicsChannelType = Int32
WRdsGraphicsChannelType_GuaranteedDelivery: win32more.Windows.Win32.System.RemoteDesktop.WRdsGraphicsChannelType = 0
WRdsGraphicsChannelType_BestEffortDelivery: win32more.Windows.Win32.System.RemoteDesktop.WRdsGraphicsChannelType = 1
class WTSCLIENTA(Structure):
    ClientName: win32more.Windows.Win32.Foundation.CHAR * 21
    Domain: win32more.Windows.Win32.Foundation.CHAR * 18
    UserName: win32more.Windows.Win32.Foundation.CHAR * 21
    WorkDirectory: win32more.Windows.Win32.Foundation.CHAR * 261
    InitialProgram: win32more.Windows.Win32.Foundation.CHAR * 261
    EncryptionLevel: Byte
    ClientAddressFamily: UInt32
    ClientAddress: UInt16 * 31
    HRes: UInt16
    VRes: UInt16
    ColorDepth: UInt16
    ClientDirectory: win32more.Windows.Win32.Foundation.CHAR * 261
    ClientBuildNumber: UInt32
    ClientHardwareId: UInt32
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    DeviceId: win32more.Windows.Win32.Foundation.CHAR * 261
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
WTSCLIENT = UnicodeAlias('WTSCLIENTW')
class WTSCONFIGINFOA(Structure):
    version: UInt32
    fConnectClientDrivesAtLogon: UInt32
    fConnectPrinterAtLogon: UInt32
    fDisablePrinterRedirection: UInt32
    fDisableDefaultMainClientPrinter: UInt32
    ShadowSettings: UInt32
    LogonUserName: win32more.Windows.Win32.Foundation.CHAR * 21
    LogonDomain: win32more.Windows.Win32.Foundation.CHAR * 18
    WorkDirectory: win32more.Windows.Win32.Foundation.CHAR * 261
    InitialProgram: win32more.Windows.Win32.Foundation.CHAR * 261
    ApplicationName: win32more.Windows.Win32.Foundation.CHAR * 261
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
WTSCONFIGINFO = UnicodeAlias('WTSCONFIGINFOW')
class WTSINFOA(Structure):
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    IncomingBytes: UInt32
    OutgoingBytes: UInt32
    IncomingFrames: UInt32
    OutgoingFrames: UInt32
    IncomingCompressedBytes: UInt32
    OutgoingCompressedBy: UInt32
    WinStationName: win32more.Windows.Win32.Foundation.CHAR * 32
    Domain: win32more.Windows.Win32.Foundation.CHAR * 17
    UserName: win32more.Windows.Win32.Foundation.CHAR * 21
    ConnectTime: Int64
    DisconnectTime: Int64
    LastInputTime: Int64
    LogonTime: Int64
    CurrentTime: Int64
class WTSINFOEXA(Structure):
    Level: UInt32
    Data: win32more.Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_A
class WTSINFOEXW(Structure):
    Level: UInt32
    Data: win32more.Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL_W
WTSINFOEX = UnicodeAlias('WTSINFOEXW')
class WTSINFOEX_LEVEL1_A(Structure):
    SessionId: UInt32
    SessionState: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionFlags: Int32
    WinStationName: win32more.Windows.Win32.Foundation.CHAR * 33
    UserName: win32more.Windows.Win32.Foundation.CHAR * 21
    DomainName: win32more.Windows.Win32.Foundation.CHAR * 18
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
class WTSINFOEX_LEVEL1_W(Structure):
    SessionId: UInt32
    SessionState: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
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
WTSINFOEX_LEVEL1 = UnicodeAlias('WTSINFOEX_LEVEL1_W')
class WTSINFOEX_LEVEL_A(Union):
    WTSInfoExLevel1: win32more.Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_A
class WTSINFOEX_LEVEL_W(Union):
    WTSInfoExLevel1: win32more.Windows.Win32.System.RemoteDesktop.WTSINFOEX_LEVEL1_W
WTSINFOEX_LEVEL = UnicodeAlias('WTSINFOEX_LEVEL_W')
class WTSINFOW(Structure):
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
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
WTSINFO = UnicodeAlias('WTSINFOW')
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
    Comment: win32more.Windows.Win32.Foundation.CHAR * 61
    LogonUserName: win32more.Windows.Win32.Foundation.CHAR * 21
    LogonDomain: win32more.Windows.Win32.Foundation.CHAR * 18
    WorkDirectory: win32more.Windows.Win32.Foundation.CHAR * 261
    InitialProgram: win32more.Windows.Win32.Foundation.CHAR * 261
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
WTSLISTENERCONFIG = UnicodeAlias('WTSLISTENERCONFIGW')
WTSSBX_ADDRESS_FAMILY = Int32
WTSSBX_ADDRESS_FAMILY_AF_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY = 0
WTSSBX_ADDRESS_FAMILY_AF_INET: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY = 1
WTSSBX_ADDRESS_FAMILY_AF_INET6: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY = 2
WTSSBX_ADDRESS_FAMILY_AF_IPX: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY = 3
WTSSBX_ADDRESS_FAMILY_AF_NETBIOS: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY = 4
class WTSSBX_IP_ADDRESS(Structure):
    AddressFamily: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY
    Address: Byte * 16
    PortNumber: UInt16
    dwScope: UInt32
class WTSSBX_MACHINE_CONNECT_INFO(Structure):
    wczMachineFQDN: Char * 257
    wczMachineNetBiosName: Char * 17
    dwNumOfIPAddr: UInt32
    IPaddr: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS * 12
WTSSBX_MACHINE_DRAIN = Int32
WTSSBX_MACHINE_DRAIN_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN = 0
WTSSBX_MACHINE_DRAIN_OFF: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN = 1
WTSSBX_MACHINE_DRAIN_ON: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN = 2
class WTSSBX_MACHINE_INFO(Structure):
    ClientConnectInfo: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO
    wczFarmName: Char * 257
    InternalIPAddress: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_IP_ADDRESS
    dwMaxSessionsLimit: UInt32
    ServerWeight: UInt32
    SingleSessionMode: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE
    InDrain: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN
    MachineState: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_STATE
WTSSBX_MACHINE_SESSION_MODE = Int32
WTSSBX_MACHINE_SESSION_MODE_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE = 0
WTSSBX_MACHINE_SESSION_MODE_SINGLE: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE = 1
WTSSBX_MACHINE_SESSION_MODE_MULTIPLE: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE = 2
WTSSBX_MACHINE_STATE = Int32
WTSSBX_MACHINE_STATE_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_STATE = 0
WTSSBX_MACHINE_STATE_READY: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_STATE = 1
WTSSBX_MACHINE_STATE_SYNCHRONIZING: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_MACHINE_STATE = 2
WTSSBX_NOTIFICATION_TYPE = Int32
WTSSBX_NOTIFICATION_REMOVED: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE = 1
WTSSBX_NOTIFICATION_CHANGED: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE = 2
WTSSBX_NOTIFICATION_ADDED: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE = 4
WTSSBX_NOTIFICATION_RESYNC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE = 8
class WTSSBX_SESSION_INFO(Structure):
    wszUserName: Char * 105
    wszDomainName: Char * 257
    ApplicationType: Char * 257
    dwSessionId: UInt32
    CreateTime: win32more.Windows.Win32.Foundation.FILETIME
    DisconnectTime: win32more.Windows.Win32.Foundation.FILETIME
    SessionState: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_STATE
WTSSBX_SESSION_STATE = Int32
WTSSBX_SESSION_STATE_UNSPEC: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_STATE = 0
WTSSBX_SESSION_STATE_ACTIVE: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_STATE = 1
WTSSBX_SESSION_STATE_DISCONNECTED: win32more.Windows.Win32.System.RemoteDesktop.WTSSBX_SESSION_STATE = 2
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
    InitialProgram: win32more.Windows.Win32.Foundation.CHAR * 261
    WorkDirectory: win32more.Windows.Win32.Foundation.CHAR * 261
    TerminalServerProfilePath: win32more.Windows.Win32.Foundation.CHAR * 261
    TerminalServerHomeDir: win32more.Windows.Win32.Foundation.CHAR * 261
    TerminalServerHomeDirDrive: win32more.Windows.Win32.Foundation.CHAR * 4
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
WTSUSERCONFIG = UnicodeAlias('WTSUSERCONFIGW')
class WTS_CACHE_STATS(Structure):
    Specific: UInt32
    Data: win32more.Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS_UN
    ProtocolType: UInt16
    Length: UInt16
class WTS_CACHE_STATS_UN(Union):
    ProtocolCache: win32more.Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_CACHE * 4
    TShareCacheStats: UInt32
    Reserved: UInt32 * 20
WTS_CERT_TYPE = Int32
WTS_CERT_TYPE_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WTS_CERT_TYPE = 0
WTS_CERT_TYPE_PROPRIETORY: win32more.Windows.Win32.System.RemoteDesktop.WTS_CERT_TYPE = 1
WTS_CERT_TYPE_X509: win32more.Windows.Win32.System.RemoteDesktop.WTS_CERT_TYPE = 2
class WTS_CLIENT_ADDRESS(Structure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_CLIENT_DATA(Structure):
    fDisableCtrlAltDel: win32more.Windows.Win32.Foundation.BOOLEAN
    fDoubleClickDetect: win32more.Windows.Win32.Foundation.BOOLEAN
    fEnableWindowsKey: win32more.Windows.Win32.Foundation.BOOLEAN
    fHideTitleBar: win32more.Windows.Win32.Foundation.BOOLEAN
    fInheritAutoLogon: win32more.Windows.Win32.Foundation.BOOL
    fPromptForPassword: win32more.Windows.Win32.Foundation.BOOLEAN
    fUsingSavedCreds: win32more.Windows.Win32.Foundation.BOOLEAN
    Domain: Char * 256
    UserName: Char * 256
    Password: Char * 256
    fPasswordIsScPin: win32more.Windows.Win32.Foundation.BOOLEAN
    fInheritInitialProgram: win32more.Windows.Win32.Foundation.BOOL
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    fMaximizeShell: win32more.Windows.Win32.Foundation.BOOLEAN
    EncryptionLevel: Byte
    PerformanceFlags: UInt32
    ProtocolName: Char * 9
    ProtocolType: UInt16
    fInheritColorDepth: win32more.Windows.Win32.Foundation.BOOL
    HRes: UInt16
    VRes: UInt16
    ColorDepth: UInt16
    DisplayDriverName: Char * 9
    DisplayDeviceName: Char * 20
    fMouse: win32more.Windows.Win32.Foundation.BOOLEAN
    KeyboardLayout: UInt32
    KeyboardType: UInt32
    KeyboardSubType: UInt32
    KeyboardFunctionKey: UInt32
    imeFileName: Char * 33
    ActiveInputLocale: UInt32
    fNoAudioPlayback: win32more.Windows.Win32.Foundation.BOOLEAN
    fRemoteConsoleAudio: win32more.Windows.Win32.Foundation.BOOLEAN
    AudioDriverName: Char * 9
    ClientTimeZone: win32more.Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
    ClientName: Char * 21
    SerialNumber: UInt32
    ClientAddressFamily: UInt32
    ClientAddress: Char * 31
    ClientSockAddress: win32more.Windows.Win32.System.RemoteDesktop.WTS_SOCKADDR
    ClientDirectory: Char * 257
    ClientBuildNumber: UInt32
    ClientProductId: UInt16
    OutBufCountHost: UInt16
    OutBufCountClient: UInt16
    OutBufLength: UInt16
    ClientSessionId: UInt32
    ClientDigProductId: Char * 33
    fDisableCpm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableClip: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisablePNP: win32more.Windows.Win32.Foundation.BOOLEAN
class WTS_CLIENT_DISPLAY(Structure):
    HorizontalResolution: UInt32
    VerticalResolution: UInt32
    ColorDepth: UInt32
WTS_CONFIG_CLASS = Int32
WTSUserConfigInitialProgram: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 0
WTSUserConfigWorkingDirectory: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 1
WTSUserConfigfInheritInitialProgram: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 2
WTSUserConfigfAllowLogonTerminalServer: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 3
WTSUserConfigTimeoutSettingsConnections: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 4
WTSUserConfigTimeoutSettingsDisconnections: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 5
WTSUserConfigTimeoutSettingsIdle: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 6
WTSUserConfigfDeviceClientDrives: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 7
WTSUserConfigfDeviceClientPrinters: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 8
WTSUserConfigfDeviceClientDefaultPrinter: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 9
WTSUserConfigBrokenTimeoutSettings: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 10
WTSUserConfigReconnectSettings: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 11
WTSUserConfigModemCallbackSettings: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 12
WTSUserConfigModemCallbackPhoneNumber: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 13
WTSUserConfigShadowingSettings: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 14
WTSUserConfigTerminalServerProfilePath: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 15
WTSUserConfigTerminalServerHomeDir: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 16
WTSUserConfigTerminalServerHomeDirDrive: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 17
WTSUserConfigfTerminalServerRemoteHomeDir: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 18
WTSUserConfigUser: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_CLASS = 19
WTS_CONFIG_SOURCE = Int32
WTSUserConfigSourceSAM: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONFIG_SOURCE = 0
WTS_CONNECTSTATE_CLASS = Int32
WTSActive: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 0
WTSConnected: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 1
WTSConnectQuery: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 2
WTSShadow: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 3
WTSDisconnected: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 4
WTSIdle: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 5
WTSListen: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 6
WTSReset: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 7
WTSDown: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 8
WTSInit: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS = 9
class WTS_DISPLAY_IOCTL(Structure):
    pDisplayIOCtlData: Byte * 256
    cbDisplayIOCtlData: UInt32
WTS_INFO_CLASS = Int32
WTSInitialProgram: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 0
WTSApplicationName: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 1
WTSWorkingDirectory: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 2
WTSOEMId: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 3
WTSSessionId: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 4
WTSUserName: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 5
WTSWinStationName: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 6
WTSDomainName: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 7
WTSConnectState: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 8
WTSClientBuildNumber: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 9
WTSClientName: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 10
WTSClientDirectory: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 11
WTSClientProductId: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 12
WTSClientHardwareId: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 13
WTSClientAddress: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 14
WTSClientDisplay: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 15
WTSClientProtocolType: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 16
WTSIdleTime: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 17
WTSLogonTime: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 18
WTSIncomingBytes: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 19
WTSOutgoingBytes: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 20
WTSIncomingFrames: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 21
WTSOutgoingFrames: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 22
WTSClientInfo: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 23
WTSSessionInfo: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 24
WTSSessionInfoEx: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 25
WTSConfigInfo: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 26
WTSValidationInfo: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 27
WTSSessionAddressV4: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 28
WTSIsRemoteSession: win32more.Windows.Win32.System.RemoteDesktop.WTS_INFO_CLASS = 29
class WTS_LICENSE_CAPABILITIES(Structure):
    KeyExchangeAlg: UInt32
    ProtocolVer: UInt32
    fAuthenticateServer: win32more.Windows.Win32.Foundation.BOOL
    CertType: win32more.Windows.Win32.System.RemoteDesktop.WTS_CERT_TYPE
    cbClientName: UInt32
    rgbClientName: Byte * 42
WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = Int32
WTS_LOGON_ERR_INVALID: win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 0
WTS_LOGON_ERR_NOT_HANDLED: win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 1
WTS_LOGON_ERR_HANDLED_SHOW: win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 2
WTS_LOGON_ERR_HANDLED_DONT_SHOW: win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 3
WTS_LOGON_ERR_HANDLED_DONT_SHOW_START_OVER: win32more.Windows.Win32.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = 4
class WTS_POLICY_DATA(Structure):
    fDisableEncryption: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableAutoReconnect: win32more.Windows.Win32.Foundation.BOOLEAN
    ColorDepth: UInt32
    MinEncryptionLevel: Byte
    fDisableCpm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCdm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableCcm: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableLPT: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisableClip: win32more.Windows.Win32.Foundation.BOOLEAN
    fDisablePNPRedir: win32more.Windows.Win32.Foundation.BOOLEAN
class WTS_PROCESS_INFOA(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: win32more.Windows.Win32.Foundation.PSTR
    pUserSid: win32more.Windows.Win32.Security.PSID
class WTS_PROCESS_INFOW(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: win32more.Windows.Win32.Foundation.PWSTR
    pUserSid: win32more.Windows.Win32.Security.PSID
WTS_PROCESS_INFO = UnicodeAlias('WTS_PROCESS_INFOW')
class WTS_PROCESS_INFO_EXA(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: win32more.Windows.Win32.Foundation.PSTR
    pUserSid: win32more.Windows.Win32.Security.PSID
    NumberOfThreads: UInt32
    HandleCount: UInt32
    PagefileUsage: UInt32
    PeakPagefileUsage: UInt32
    WorkingSetSize: UInt32
    PeakWorkingSetSize: UInt32
    UserTime: Int64
    KernelTime: Int64
class WTS_PROCESS_INFO_EXW(Structure):
    SessionId: UInt32
    ProcessId: UInt32
    pProcessName: win32more.Windows.Win32.Foundation.PWSTR
    pUserSid: win32more.Windows.Win32.Security.PSID
    NumberOfThreads: UInt32
    HandleCount: UInt32
    PagefileUsage: UInt32
    PeakPagefileUsage: UInt32
    WorkingSetSize: UInt32
    PeakWorkingSetSize: UInt32
    UserTime: Int64
    KernelTime: Int64
WTS_PROCESS_INFO_EX = UnicodeAlias('WTS_PROCESS_INFO_EXW')
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
            pstrVal: win32more.Windows.Win32.Foundation.PWSTR
        class _bVal_e__Struct(Structure):
            size: UInt32
            pbVal: win32more.Windows.Win32.Foundation.PSTR
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
    Output: win32more.Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Input: win32more.Windows.Win32.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS
    Cache: win32more.Windows.Win32.System.RemoteDesktop.WTS_CACHE_STATS
    AsyncSignal: UInt32
    AsyncSignalMask: UInt32
    Counters: Int64 * 100
WTS_RCM_DRAIN_STATE = Int32
WTS_DRAIN_STATE_NONE: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE = 0
WTS_DRAIN_IN_DRAIN: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE = 1
WTS_DRAIN_NOT_IN_DRAIN: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE = 2
WTS_RCM_SERVICE_STATE = Int32
WTS_SERVICE_NONE: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE = 0
WTS_SERVICE_START: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE = 1
WTS_SERVICE_STOP: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE = 2
WTS_SECURITY_FLAGS = UInt32
WTS_SECURITY_CURRENT_GUEST_ACCESS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 72
WTS_SECURITY_USER_ACCESS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 329
WTS_SECURITY_CURRENT_USER_ACCESS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 590
WTS_SECURITY_ALL_ACCESS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 983999
WTS_SECURITY_QUERY_INFORMATION: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 1
WTS_SECURITY_SET_INFORMATION: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 2
WTS_SECURITY_RESET: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 4
WTS_SECURITY_VIRTUAL_CHANNELS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 8
WTS_SECURITY_REMOTE_CONTROL: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 16
WTS_SECURITY_LOGON: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 32
WTS_SECURITY_LOGOFF: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 64
WTS_SECURITY_MESSAGE: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 128
WTS_SECURITY_CONNECT: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 256
WTS_SECURITY_DISCONNECT: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 512
WTS_SECURITY_GUEST_ACCESS: win32more.Windows.Win32.System.RemoteDesktop.WTS_SECURITY_FLAGS = 32
class WTS_SERVER_INFOA(Structure):
    pServerName: win32more.Windows.Win32.Foundation.PSTR
class WTS_SERVER_INFOW(Structure):
    pServerName: win32more.Windows.Win32.Foundation.PWSTR
WTS_SERVER_INFO = UnicodeAlias('WTS_SERVER_INFOW')
class WTS_SERVICE_STATE(Structure):
    RcmServiceState: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_SERVICE_STATE
    RcmDrainState: win32more.Windows.Win32.System.RemoteDesktop.WTS_RCM_DRAIN_STATE
class WTS_SESSION_ADDRESS(Structure):
    AddressFamily: UInt32
    Address: Byte * 20
class WTS_SESSION_ID(Structure):
    SessionUniqueGuid: Guid
    SessionId: UInt32
class WTS_SESSION_INFOA(Structure):
    SessionId: UInt32
    pWinStationName: win32more.Windows.Win32.Foundation.PSTR
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
class WTS_SESSION_INFOW(Structure):
    SessionId: UInt32
    pWinStationName: win32more.Windows.Win32.Foundation.PWSTR
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
WTS_SESSION_INFO = UnicodeAlias('WTS_SESSION_INFOW')
class WTS_SESSION_INFO_1A(Structure):
    ExecEnvId: UInt32
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: win32more.Windows.Win32.Foundation.PSTR
    pHostName: win32more.Windows.Win32.Foundation.PSTR
    pUserName: win32more.Windows.Win32.Foundation.PSTR
    pDomainName: win32more.Windows.Win32.Foundation.PSTR
    pFarmName: win32more.Windows.Win32.Foundation.PSTR
class WTS_SESSION_INFO_1W(Structure):
    ExecEnvId: UInt32
    State: win32more.Windows.Win32.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS
    SessionId: UInt32
    pSessionName: win32more.Windows.Win32.Foundation.PWSTR
    pHostName: win32more.Windows.Win32.Foundation.PWSTR
    pUserName: win32more.Windows.Win32.Foundation.PWSTR
    pDomainName: win32more.Windows.Win32.Foundation.PWSTR
    pFarmName: win32more.Windows.Win32.Foundation.PWSTR
WTS_SESSION_INFO_1 = UnicodeAlias('WTS_SESSION_INFO_1W')
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
    StandardDate: win32more.Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: win32more.Windows.Win32.System.RemoteDesktop.WTS_SYSTEMTIME
    DaylightBias: Int32
WTS_TYPE_CLASS = Int32
WTSTypeProcessInfoLevel0: win32more.Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS = 0
WTSTypeProcessInfoLevel1: win32more.Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS = 1
WTSTypeSessionInfoLevel1: win32more.Windows.Win32.System.RemoteDesktop.WTS_TYPE_CLASS = 2
class WTS_USER_CREDENTIAL(Structure):
    UserName: Char * 256
    Password: Char * 256
    Domain: Char * 256
class WTS_USER_DATA(Structure):
    WorkDirectory: Char * 257
    InitialProgram: Char * 257
    UserTimeZone: win32more.Windows.Win32.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION
class WTS_VALIDATION_INFORMATIONA(Structure):
    ProductInfo: win32more.Windows.Win32.System.RemoteDesktop.PRODUCT_INFOA
    License: Byte * 16384
    LicenseLength: UInt32
    HardwareID: Byte * 20
    HardwareIDLength: UInt32
class WTS_VALIDATION_INFORMATIONW(Structure):
    ProductInfo: win32more.Windows.Win32.System.RemoteDesktop.PRODUCT_INFOW
    License: Byte * 16384
    LicenseLength: UInt32
    HardwareID: Byte * 20
    HardwareIDLength: UInt32
WTS_VALIDATION_INFORMATION = UnicodeAlias('WTS_VALIDATION_INFORMATIONW')
WTS_VIRTUAL_CLASS = Int32
WTSVirtualClientData: win32more.Windows.Win32.System.RemoteDesktop.WTS_VIRTUAL_CLASS = 0
WTSVirtualFileHandle: win32more.Windows.Win32.System.RemoteDesktop.WTS_VIRTUAL_CLASS = 1
Workspace = Guid('{4f1dfca6-3aad-48e1-8406-4bc21a501d7c}')
class _ITSWkspEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b922bbb8-4c55-4fea-8496-beb0b44285e9}')
class pluginResource(Structure):
    alias: Char * 256
    name: Char * 256
    resourceFileContents: win32more.Windows.Win32.Foundation.PWSTR
    fileExtension: Char * 256
    resourcePluginType: Char * 256
    isDiscoverable: Byte
    resourceType: Int32
    pceIconSize: UInt32
    iconContents: POINTER(Byte)
    pcePluginBlobSize: UInt32
    blobContents: POINTER(Byte)
class pluginResource2(Structure):
    resourceV1: win32more.Windows.Win32.System.RemoteDesktop.pluginResource
    pceFileAssocListSize: UInt32
    fileAssocList: POINTER(win32more.Windows.Win32.System.RemoteDesktop.pluginResource2FileAssociation)
    securityDescriptor: win32more.Windows.Win32.Foundation.PWSTR
    pceFolderListSize: UInt32
    folderList: POINTER(POINTER(UInt16))
class pluginResource2FileAssociation(Structure):
    extName: Char * 256
    primaryHandler: Byte
    pceIconSize: UInt32
    iconContents: POINTER(Byte)


make_ready(__name__)
