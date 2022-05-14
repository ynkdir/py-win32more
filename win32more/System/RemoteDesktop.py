from win32more import *
import win32more.System.RemoteDesktop
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Audio.Apo
import win32more.Security
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.WinRT
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.RemoteDesktop, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.RemoteDesktop, name)
WTS_DOMAIN_LENGTH = 255
WTS_USERNAME_LENGTH = 255
WTS_PASSWORD_LENGTH = 255
WTS_DIRECTORY_LENGTH = 256
WTS_INITIALPROGRAM_LENGTH = 256
WTS_PROTOCOL_NAME_LENGTH = 8
WTS_DRIVER_NAME_LENGTH = 8
WTS_DEVICE_NAME_LENGTH = 19
WTS_IMEFILENAME_LENGTH = 32
WTS_CLIENTNAME_LENGTH = 20
WTS_CLIENTADDRESS_LENGTH = 30
WTS_CLIENT_PRODUCT_ID_LENGTH = 32
WTS_MAX_PROTOCOL_CACHE = 4
WTS_MAX_CACHE_RESERVED = 20
WTS_MAX_RESERVED = 100
WTS_MAX_COUNTERS = 100
WTS_MAX_DISPLAY_IOCTL_DATA = 256
WTS_PERF_DISABLE_NOTHING = 0
WTS_PERF_DISABLE_WALLPAPER = 1
WTS_PERF_DISABLE_FULLWINDOWDRAG = 2
WTS_PERF_DISABLE_MENUANIMATIONS = 4
WTS_PERF_DISABLE_THEMING = 8
WTS_PERF_ENABLE_ENHANCED_GRAPHICS = 16
WTS_PERF_DISABLE_CURSOR_SHADOW = 32
WTS_PERF_DISABLE_CURSORSETTINGS = 64
WTS_PERF_ENABLE_FONT_SMOOTHING = 128
WTS_PERF_ENABLE_DESKTOP_COMPOSITION = 256
WTS_VALUE_TYPE_ULONG = 1
WTS_VALUE_TYPE_STRING = 2
WTS_VALUE_TYPE_BINARY = 3
WTS_VALUE_TYPE_GUID = 4
WTS_KEY_EXCHANGE_ALG_RSA = 1
WTS_KEY_EXCHANGE_ALG_DH = 2
WTS_LICENSE_PROTOCOL_VERSION = 65536
WTS_LICENSE_PREAMBLE_VERSION = 3
WRDS_DOMAIN_LENGTH = 255
WRDS_USERNAME_LENGTH = 255
WRDS_PASSWORD_LENGTH = 255
WRDS_DIRECTORY_LENGTH = 256
WRDS_INITIALPROGRAM_LENGTH = 256
WRDS_PROTOCOL_NAME_LENGTH = 8
WRDS_DRIVER_NAME_LENGTH = 8
WRDS_DEVICE_NAME_LENGTH = 19
WRDS_IMEFILENAME_LENGTH = 32
WRDS_CLIENTNAME_LENGTH = 20
WRDS_CLIENTADDRESS_LENGTH = 30
WRDS_CLIENT_PRODUCT_ID_LENGTH = 32
WRDS_MAX_PROTOCOL_CACHE = 4
WRDS_MAX_CACHE_RESERVED = 20
WRDS_MAX_RESERVED = 100
WRDS_MAX_COUNTERS = 100
WRDS_MAX_DISPLAY_IOCTL_DATA = 256
WRDS_PERF_DISABLE_NOTHING = 0
WRDS_PERF_DISABLE_WALLPAPER = 1
WRDS_PERF_DISABLE_FULLWINDOWDRAG = 2
WRDS_PERF_DISABLE_MENUANIMATIONS = 4
WRDS_PERF_DISABLE_THEMING = 8
WRDS_PERF_ENABLE_ENHANCED_GRAPHICS = 16
WRDS_PERF_DISABLE_CURSOR_SHADOW = 32
WRDS_PERF_DISABLE_CURSORSETTINGS = 64
WRDS_PERF_ENABLE_FONT_SMOOTHING = 128
WRDS_PERF_ENABLE_DESKTOP_COMPOSITION = 256
WRDS_VALUE_TYPE_ULONG = 1
WRDS_VALUE_TYPE_STRING = 2
WRDS_VALUE_TYPE_BINARY = 3
WRDS_VALUE_TYPE_GUID = 4
WRDS_KEY_EXCHANGE_ALG_RSA = 1
WRDS_KEY_EXCHANGE_ALG_DH = 2
WRDS_LICENSE_PROTOCOL_VERSION = 65536
WRDS_LICENSE_PREAMBLE_VERSION = 3
SINGLE_SESSION = 1
FORCE_REJOIN = 2
FORCE_REJOIN_IN_CLUSTERMODE = 3
RESERVED_FOR_LEGACY = 4
KEEP_EXISTING_SESSIONS = 8
CHANNEL_EVENT_INITIALIZED = 0
CHANNEL_EVENT_CONNECTED = 1
CHANNEL_EVENT_V1_CONNECTED = 2
CHANNEL_EVENT_DISCONNECTED = 3
CHANNEL_EVENT_TERMINATED = 4
CHANNEL_EVENT_DATA_RECEIVED = 10
CHANNEL_EVENT_WRITE_COMPLETE = 11
CHANNEL_EVENT_WRITE_CANCELLED = 12
CHANNEL_RC_OK = 0
CHANNEL_RC_ALREADY_INITIALIZED = 1
CHANNEL_RC_NOT_INITIALIZED = 2
CHANNEL_RC_ALREADY_CONNECTED = 3
CHANNEL_RC_NOT_CONNECTED = 4
CHANNEL_RC_TOO_MANY_CHANNELS = 5
CHANNEL_RC_BAD_CHANNEL = 6
CHANNEL_RC_BAD_CHANNEL_HANDLE = 7
CHANNEL_RC_NO_BUFFER = 8
CHANNEL_RC_BAD_INIT_HANDLE = 9
CHANNEL_RC_NOT_OPEN = 10
CHANNEL_RC_BAD_PROC = 11
CHANNEL_RC_NO_MEMORY = 12
CHANNEL_RC_UNKNOWN_CHANNEL_NAME = 13
CHANNEL_RC_ALREADY_OPEN = 14
CHANNEL_RC_NOT_IN_VIRTUALCHANNELENTRY = 15
CHANNEL_RC_NULL_DATA = 16
CHANNEL_RC_ZERO_LENGTH = 17
CHANNEL_RC_INVALID_INSTANCE = 18
CHANNEL_RC_UNSUPPORTED_VERSION = 19
CHANNEL_RC_INITIALIZATION_ERROR = 20
VIRTUAL_CHANNEL_VERSION_WIN2000 = 1
CHANNEL_CHUNK_LENGTH = 1600
CHANNEL_BUFFER_SIZE = 65535
CHANNEL_FLAG_FIRST = 1
CHANNEL_FLAG_LAST = 2
CHANNEL_FLAG_MIDDLE = 0
CHANNEL_FLAG_FAIL = 256
CHANNEL_OPTION_INITIALIZED = 2147483648
CHANNEL_OPTION_ENCRYPT_RDP = 1073741824
CHANNEL_OPTION_ENCRYPT_SC = 536870912
CHANNEL_OPTION_ENCRYPT_CS = 268435456
CHANNEL_OPTION_PRI_HIGH = 134217728
CHANNEL_OPTION_PRI_MED = 67108864
CHANNEL_OPTION_PRI_LOW = 33554432
CHANNEL_OPTION_COMPRESS_RDP = 8388608
CHANNEL_OPTION_COMPRESS = 4194304
CHANNEL_OPTION_SHOW_PROTOCOL = 2097152
CHANNEL_OPTION_REMOTE_CONTROL_PERSISTENT = 1048576
CHANNEL_MAX_COUNT = 30
CHANNEL_NAME_LEN = 7
MAX_POLICY_ATTRIBUTES = 20
WTS_CURRENT_SESSION = 4294967295
USERNAME_LENGTH = 20
CLIENTNAME_LENGTH = 20
CLIENTADDRESS_LENGTH = 30
WTS_WSD_LOGOFF = 1
WTS_WSD_SHUTDOWN = 2
WTS_WSD_REBOOT = 4
WTS_WSD_POWEROFF = 8
WTS_WSD_FASTREBOOT = 16
MAX_ELAPSED_TIME_LENGTH = 15
MAX_DATE_TIME_LENGTH = 56
WINSTATIONNAME_LENGTH = 32
DOMAIN_LENGTH = 17
WTS_DRIVE_LENGTH = 3
WTS_LISTENER_NAME_LENGTH = 32
WTS_COMMENT_LENGTH = 60
WTS_LISTENER_CREATE = 1
WTS_LISTENER_UPDATE = 16
WTS_SECURITY_QUERY_INFORMATION = 1
WTS_SECURITY_SET_INFORMATION = 2
WTS_SECURITY_RESET = 4
WTS_SECURITY_VIRTUAL_CHANNELS = 8
WTS_SECURITY_REMOTE_CONTROL = 16
WTS_SECURITY_LOGON = 32
WTS_SECURITY_LOGOFF = 64
WTS_SECURITY_MESSAGE = 128
WTS_SECURITY_CONNECT = 256
WTS_SECURITY_DISCONNECT = 512
WTS_SECURITY_GUEST_ACCESS = 32
WTS_PROTOCOL_TYPE_CONSOLE = 0
WTS_PROTOCOL_TYPE_ICA = 1
WTS_PROTOCOL_TYPE_RDP = 2
WTS_SESSIONSTATE_UNKNOWN = 4294967295
WTS_SESSIONSTATE_LOCK = 0
WTS_SESSIONSTATE_UNLOCK = 1
PRODUCTINFO_COMPANYNAME_LENGTH = 256
PRODUCTINFO_PRODUCTID_LENGTH = 4
VALIDATIONINFORMATION_LICENSE_LENGTH = 16384
VALIDATIONINFORMATION_HARDWAREID_LENGTH = 20
WTS_EVENT_NONE = 0
WTS_EVENT_CREATE = 1
WTS_EVENT_DELETE = 2
WTS_EVENT_RENAME = 4
WTS_EVENT_CONNECT = 8
WTS_EVENT_DISCONNECT = 16
WTS_EVENT_LOGON = 32
WTS_EVENT_LOGOFF = 64
WTS_EVENT_STATECHANGE = 128
WTS_EVENT_LICENSE = 256
WTS_EVENT_ALL = 2147483647
WTS_EVENT_FLUSH = 2147483648
REMOTECONTROL_KBDSHIFT_HOTKEY = 1
REMOTECONTROL_KBDCTRL_HOTKEY = 2
REMOTECONTROL_KBDALT_HOTKEY = 4
WTS_CHANNEL_OPTION_DYNAMIC = 1
WTS_CHANNEL_OPTION_DYNAMIC_PRI_LOW = 0
WTS_CHANNEL_OPTION_DYNAMIC_PRI_MED = 2
WTS_CHANNEL_OPTION_DYNAMIC_PRI_HIGH = 4
WTS_CHANNEL_OPTION_DYNAMIC_PRI_REAL = 6
WTS_CHANNEL_OPTION_DYNAMIC_NO_COMPRESS = 8
NOTIFY_FOR_ALL_SESSIONS = 1
NOTIFY_FOR_THIS_SESSION = 0
WTS_PROCESS_INFO_LEVEL_0 = 0
WTS_PROCESS_INFO_LEVEL_1 = 1
PLUGIN_CAPABILITY_EXTERNAL_REDIRECTION = 1
MaxFQDN_Len = 256
MaxNetBiosName_Len = 16
MaxNumOfExposed_IPs = 12
MaxUserName_Len = 104
MaxDomainName_Len = 256
MaxFarm_Len = 256
MaxAppName_Len = 256
WKS_FLAG_CLEAR_CREDS_ON_LAST_RESOURCE = 1
WKS_FLAG_PASSWORD_ENCRYPTED = 2
WKS_FLAG_CREDS_AUTHENTICATED = 4
SB_SYNCH_CONFLICT_MAX_WRITE_ATTEMPTS = 100
ACQUIRE_TARGET_LOCK_TIMEOUT = 300000
RENDER_HINT_CLEAR = 0
RENDER_HINT_VIDEO = 1
RENDER_HINT_MAPPEDWINDOW = 2
TS_VC_LISTENER_STATIC_CHANNEL = 1
WRdsGraphicsChannels_LossyChannelMaxMessageSize = 988
RFX_RDP_MSG_PREFIX = 0
RFX_GFX_MSG_PREFIX = 48
RFX_GFX_MSG_PREFIX_MASK = 48
RFX_GFX_MAX_SUPPORTED_MONITORS = 16
RFX_CLIENT_ID_LENGTH = 32
DISPID_METHOD_REMOTEDESKTOPCLIENT_CONNECT = 701
DISPID_METHOD_REMOTEDESKTOPCLIENT_DISCONNECT = 702
DISPID_METHOD_REMOTEDESKTOPCLIENT_RECONNECT = 703
DISPID_METHOD_REMOTEDESKTOPCLIENT_DELETE_SAVED_CREDENTIALS = 704
DISPID_METHOD_REMOTEDESKTOPCLIENT_UPDATE_SESSION_DISPLAYSETTINGS = 705
DISPID_METHOD_REMOTEDESKTOPCLIENT_ATTACH_EVENT = 706
DISPID_METHOD_REMOTEDESKTOPCLIENT_DETACH_EVENT = 707
DISPID_PROP_REMOTEDESKTOPCLIENT_SETTINGS = 710
DISPID_PROP_REMOTEDESKTOPCLIENT_ACTIONS = 711
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCH_POINTER = 712
DISPID_METHOD_REMOTEDESKTOPCLIENT_SET_RDPPROPERTY = 720
DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_RDPPROPERTY = 721
DISPID_METHOD_REMOTEDESKTOPCLIENT_APPLY_SETTINGS = 722
DISPID_METHOD_REMOTEDESKTOPCLIENT_RETRIEVE_SETTINGS = 723
DISPID_METHOD_REMOTEDESKTOPCLIENT_SUSPEND_SCREEN_UPDATES = 730
DISPID_METHOD_REMOTEDESKTOPCLIENT_RESUME_SCREEN_UPDATES = 731
DISPID_METHOD_REMOTEDESKTOPCLIENT_EXECUTE_REMOTE_ACTION = 732
DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_SNAPSHOT = 733
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_ENABLED = 740
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_EVENTSENABLED = 741
DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_POINTERSPEED = 742
DISPID_AX_CONNECTING = 750
DISPID_AX_CONNECTED = 751
DISPID_AX_LOGINCOMPLETED = 752
DISPID_AX_DISCONNECTED = 753
DISPID_AX_STATUSCHANGED = 754
DISPID_AX_AUTORECONNECTING = 755
DISPID_AX_AUTORECONNECTED = 756
DISPID_AX_DIALOGDISPLAYING = 757
DISPID_AX_DIALOGDISMISSED = 758
DISPID_AX_NETWORKSTATUSCHANGED = 759
DISPID_AX_ADMINMESSAGERECEIVED = 760
DISPID_AX_KEYCOMBINATIONPRESSED = 761
DISPID_AX_REMOTEDESKTOPSIZECHANGED = 762
DISPID_AX_TOUCHPOINTERCURSORMOVED = 800
RDCLIENT_BITMAP_RENDER_SERVICE = 'e4cc08cb-942e-4b19-8504-bd5a89a747f5'
WTS_QUERY_ALLOWED_INITIAL_APP = 'c77d1b30-5be1-4c6b-a0e1-bd6d2e5c9fcc'
WTS_QUERY_LOGON_SCREEN_SIZE = '8b8e0fe7-0804-4a0e-b279-8660b1df0049'
WTS_QUERY_AUDIOENUM_DLL = '9bf4fa97-c883-4c2a-80ab-5a39c9af00db'
WTS_QUERY_MF_FORMAT_SUPPORT = '41869ad0-6332-4dc8-95d5-db749e2f1d94'
WRDS_SERVICE_ID_GRAPHICS_GUID = 'd2993f4d-02cf-4280-8c48-1624b44f8706'
PROPERTY_DYNAMIC_TIME_ZONE_INFORMATION = '0cdfd28e-d0b9-4c1f-a5eb-6d1f6c6535b9'
PROPERTY_TYPE_GET_FAST_RECONNECT = '6212d757-0043-4862-99c3-9f3059ac2a3b'
PROPERTY_TYPE_GET_FAST_RECONNECT_USER_SID = '197c427a-0135-4b6d-9c5e-e6579a0ab625'
PROPERTY_TYPE_ENABLE_UNIVERSAL_APPS_FOR_CUSTOM_SHELL = 'ed2c3fda-338d-4d3f-81a3-e767310d908e'
CONNECTION_PROPERTY_IDLE_TIME_WARNING = '693f7ff5-0c4e-4d17-b8e0-1f70325e5d58'
CONNECTION_PROPERTY_CURSOR_BLINK_DISABLED = '4b150580-fea4-4d3c-9de4-7433a66618f7'
AE_POSITION_FLAGS = Int32
POSITION_INVALID = 0
POSITION_DISCONTINUOUS = 1
POSITION_CONTINUOUS = 2
POSITION_QPC_ERROR = 4
def _define_AE_CURRENT_POSITION_head():
    class AE_CURRENT_POSITION(Structure):
        pass
    return AE_CURRENT_POSITION
def _define_AE_CURRENT_POSITION():
    AE_CURRENT_POSITION = win32more.System.RemoteDesktop.AE_CURRENT_POSITION_head
    AE_CURRENT_POSITION._fields_ = [
        ("u64DevicePosition", UInt64),
        ("u64StreamPosition", UInt64),
        ("u64PaddingFrames", UInt64),
        ("hnsQPCPosition", Int64),
        ("f32FramesPerSecond", Single),
        ("Flag", win32more.System.RemoteDesktop.AE_POSITION_FLAGS),
    ]
    return AE_CURRENT_POSITION
def _define_IAudioEndpoint_head():
    class IAudioEndpoint(win32more.System.Com.IUnknown_head):
        Guid = Guid('30a99515-1527-4451-af9f-00c5f0234daf')
    return IAudioEndpoint
def _define_IAudioEndpoint():
    IAudioEndpoint = win32more.System.RemoteDesktop.IAudioEndpoint_head
    IAudioEndpoint.GetFrameFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(3, 'GetFrameFormat', ((1, 'ppFormat'),)))
    IAudioEndpoint.GetFramesPerPacket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetFramesPerPacket', ((1, 'pFramesPerPacket'),)))
    IAudioEndpoint.GetLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(5, 'GetLatency', ((1, 'pLatency'),)))
    IAudioEndpoint.SetStreamFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetStreamFlags', ((1, 'streamFlags'),)))
    IAudioEndpoint.SetEventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(7, 'SetEventHandle', ((1, 'eventHandle'),)))
    return IAudioEndpoint
def _define_IAudioEndpointRT_head():
    class IAudioEndpointRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('dfd2005f-a6e5-4d39-a265-939ada9fbb4d')
    return IAudioEndpointRT
def _define_IAudioEndpointRT():
    IAudioEndpointRT = win32more.System.RemoteDesktop.IAudioEndpointRT_head
    IAudioEndpointRT.GetCurrentPadding = COMMETHOD(WINFUNCTYPE(Void,POINTER(Int64),POINTER(win32more.System.RemoteDesktop.AE_CURRENT_POSITION_head), use_last_error=False)(3, 'GetCurrentPadding', ((1, 'pPadding'),(1, 'pAeCurrentPosition'),)))
    IAudioEndpointRT.ProcessingComplete = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'ProcessingComplete', ()))
    IAudioEndpointRT.SetPinInactive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SetPinInactive', ()))
    IAudioEndpointRT.SetPinActive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'SetPinActive', ()))
    return IAudioEndpointRT
def _define_IAudioInputEndpointRT_head():
    class IAudioInputEndpointRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('8026ab61-92b2-43c1-a1df-5c37ebd08d82')
    return IAudioInputEndpointRT
def _define_IAudioInputEndpointRT():
    IAudioInputEndpointRT = win32more.System.RemoteDesktop.IAudioInputEndpointRT_head
    IAudioInputEndpointRT.GetInputDataPointer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head),POINTER(win32more.System.RemoteDesktop.AE_CURRENT_POSITION_head), use_last_error=False)(3, 'GetInputDataPointer', ((1, 'pConnectionProperty'),(1, 'pAeTimeStamp'),)))
    IAudioInputEndpointRT.ReleaseInputDataPointer = COMMETHOD(WINFUNCTYPE(Void,UInt32,UIntPtr, use_last_error=False)(4, 'ReleaseInputDataPointer', ((1, 'u32FrameCount'),(1, 'pDataPointer'),)))
    IAudioInputEndpointRT.PulseEndpoint = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'PulseEndpoint', ()))
    return IAudioInputEndpointRT
def _define_IAudioOutputEndpointRT_head():
    class IAudioOutputEndpointRT(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fa906e4-c31c-4e31-932e-19a66385e9aa')
    return IAudioOutputEndpointRT
def _define_IAudioOutputEndpointRT():
    IAudioOutputEndpointRT = win32more.System.RemoteDesktop.IAudioOutputEndpointRT_head
    IAudioOutputEndpointRT.GetOutputDataPointer = COMMETHOD(WINFUNCTYPE(UIntPtr,UInt32,POINTER(win32more.System.RemoteDesktop.AE_CURRENT_POSITION_head), use_last_error=False)(3, 'GetOutputDataPointer', ((1, 'u32FrameCount'),(1, 'pAeTimeStamp'),)))
    IAudioOutputEndpointRT.ReleaseOutputDataPointer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Media.Audio.Apo.APO_CONNECTION_PROPERTY_head), use_last_error=False)(4, 'ReleaseOutputDataPointer', ((1, 'pConnectionProperty'),)))
    IAudioOutputEndpointRT.PulseEndpoint = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'PulseEndpoint', ()))
    return IAudioOutputEndpointRT
def _define_IAudioDeviceEndpoint_head():
    class IAudioDeviceEndpoint(win32more.System.Com.IUnknown_head):
        Guid = Guid('d4952f5a-a0b2-4cc4-8b82-9358488dd8ac')
    return IAudioDeviceEndpoint
def _define_IAudioDeviceEndpoint():
    IAudioDeviceEndpoint = win32more.System.RemoteDesktop.IAudioDeviceEndpoint_head
    IAudioDeviceEndpoint.SetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32, use_last_error=False)(3, 'SetBuffer', ((1, 'MaxPeriod'),(1, 'u32LatencyCoefficient'),)))
    IAudioDeviceEndpoint.GetRTCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetRTCaps', ((1, 'pbIsRTCapable'),)))
    IAudioDeviceEndpoint.GetEventDrivenCapable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetEventDrivenCapable', ((1, 'pbisEventCapable'),)))
    IAudioDeviceEndpoint.WriteExclusiveModeParametersToSharedMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,Int64,Int64,UInt32,POINTER(UInt32),POINTER(UIntPtr), use_last_error=False)(6, 'WriteExclusiveModeParametersToSharedMemory', ((1, 'hTargetProcess'),(1, 'hnsPeriod'),(1, 'hnsBufferDuration'),(1, 'u32LatencyCoefficient'),(1, 'pu32SharedMemorySize'),(1, 'phSharedMemory'),)))
    return IAudioDeviceEndpoint
def _define_IAudioEndpointControl_head():
    class IAudioEndpointControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('c684b72a-6df4-4774-bdf9-76b77509b653')
    return IAudioEndpointControl
def _define_IAudioEndpointControl():
    IAudioEndpointControl = win32more.System.RemoteDesktop.IAudioEndpointControl_head
    IAudioEndpointControl.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Start', ()))
    IAudioEndpointControl.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Reset', ()))
    IAudioEndpointControl.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Stop', ()))
    return IAudioEndpointControl
HwtsVirtualChannelHandle = IntPtr
TSUserExInterfaces = Guid('0910dd01-df8c-11d1-ae27-00c04fa35813')
ADsTSUserEx = Guid('e2e9cae6-1e7b-4b8e-babd-e9bf6292ac29')
def _define_IADsTSUserEx_head():
    class IADsTSUserEx(win32more.System.Com.IDispatch_head):
        Guid = Guid('c4930e79-2989-4462-8a60-2fcf2f2955ef')
    return IADsTSUserEx
def _define_IADsTSUserEx():
    IADsTSUserEx = win32more.System.RemoteDesktop.IADsTSUserEx_head
    IADsTSUserEx.get_TerminalServicesProfilePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_TerminalServicesProfilePath', ((1, 'pVal'),)))
    IADsTSUserEx.put_TerminalServicesProfilePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_TerminalServicesProfilePath', ((1, 'pNewVal'),)))
    IADsTSUserEx.get_TerminalServicesHomeDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_TerminalServicesHomeDirectory', ((1, 'pVal'),)))
    IADsTSUserEx.put_TerminalServicesHomeDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_TerminalServicesHomeDirectory', ((1, 'pNewVal'),)))
    IADsTSUserEx.get_TerminalServicesHomeDrive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_TerminalServicesHomeDrive', ((1, 'pVal'),)))
    IADsTSUserEx.put_TerminalServicesHomeDrive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_TerminalServicesHomeDrive', ((1, 'pNewVal'),)))
    IADsTSUserEx.get_AllowLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_AllowLogon', ((1, 'pVal'),)))
    IADsTSUserEx.put_AllowLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_AllowLogon', ((1, 'NewVal'),)))
    IADsTSUserEx.get_EnableRemoteControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_EnableRemoteControl', ((1, 'pVal'),)))
    IADsTSUserEx.put_EnableRemoteControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_EnableRemoteControl', ((1, 'NewVal'),)))
    IADsTSUserEx.get_MaxDisconnectionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_MaxDisconnectionTime', ((1, 'pVal'),)))
    IADsTSUserEx.put_MaxDisconnectionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_MaxDisconnectionTime', ((1, 'NewVal'),)))
    IADsTSUserEx.get_MaxConnectionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_MaxConnectionTime', ((1, 'pVal'),)))
    IADsTSUserEx.put_MaxConnectionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'put_MaxConnectionTime', ((1, 'NewVal'),)))
    IADsTSUserEx.get_MaxIdleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_MaxIdleTime', ((1, 'pVal'),)))
    IADsTSUserEx.put_MaxIdleTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_MaxIdleTime', ((1, 'NewVal'),)))
    IADsTSUserEx.get_ReconnectionAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_ReconnectionAction', ((1, 'pNewVal'),)))
    IADsTSUserEx.put_ReconnectionAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_ReconnectionAction', ((1, 'NewVal'),)))
    IADsTSUserEx.get_BrokenConnectionAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_BrokenConnectionAction', ((1, 'pNewVal'),)))
    IADsTSUserEx.put_BrokenConnectionAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_BrokenConnectionAction', ((1, 'NewVal'),)))
    IADsTSUserEx.get_ConnectClientDrivesAtLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_ConnectClientDrivesAtLogon', ((1, 'pNewVal'),)))
    IADsTSUserEx.put_ConnectClientDrivesAtLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_ConnectClientDrivesAtLogon', ((1, 'NewVal'),)))
    IADsTSUserEx.get_ConnectClientPrintersAtLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_ConnectClientPrintersAtLogon', ((1, 'pVal'),)))
    IADsTSUserEx.put_ConnectClientPrintersAtLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_ConnectClientPrintersAtLogon', ((1, 'NewVal'),)))
    IADsTSUserEx.get_DefaultToMainPrinter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(31, 'get_DefaultToMainPrinter', ((1, 'pVal'),)))
    IADsTSUserEx.put_DefaultToMainPrinter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(32, 'put_DefaultToMainPrinter', ((1, 'NewVal'),)))
    IADsTSUserEx.get_TerminalServicesWorkDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'get_TerminalServicesWorkDirectory', ((1, 'pVal'),)))
    IADsTSUserEx.put_TerminalServicesWorkDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_TerminalServicesWorkDirectory', ((1, 'pNewVal'),)))
    IADsTSUserEx.get_TerminalServicesInitialProgram = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_TerminalServicesInitialProgram', ((1, 'pVal'),)))
    IADsTSUserEx.put_TerminalServicesInitialProgram = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_TerminalServicesInitialProgram', ((1, 'pNewVal'),)))
    return IADsTSUserEx
AAAuthSchemes = Int32
AA_AUTH_MIN = 0
AA_AUTH_BASIC = 1
AA_AUTH_NTLM = 2
AA_AUTH_SC = 3
AA_AUTH_LOGGEDONCREDENTIALS = 4
AA_AUTH_NEGOTIATE = 5
AA_AUTH_ANY = 6
AA_AUTH_COOKIE = 7
AA_AUTH_DIGEST = 8
AA_AUTH_ORGID = 9
AA_AUTH_CONID = 10
AA_AUTH_SSPI_NTLM = 11
AA_AUTH_MAX = 12
AAAccountingDataType = Int32
AA_MAIN_SESSION_CREATION = 0
AA_SUB_SESSION_CREATION = 1
AA_SUB_SESSION_CLOSED = 2
AA_MAIN_SESSION_CLOSED = 3
def _define_AAAccountingData_head():
    class AAAccountingData(Structure):
        pass
    return AAAccountingData
def _define_AAAccountingData():
    AAAccountingData = win32more.System.RemoteDesktop.AAAccountingData_head
    AAAccountingData._fields_ = [
        ("userName", win32more.Foundation.BSTR),
        ("clientName", win32more.Foundation.BSTR),
        ("authType", win32more.System.RemoteDesktop.AAAuthSchemes),
        ("resourceName", win32more.Foundation.BSTR),
        ("portNumber", Int32),
        ("protocolName", win32more.Foundation.BSTR),
        ("numberOfBytesReceived", Int32),
        ("numberOfBytesTransfered", Int32),
        ("reasonForDisconnect", win32more.Foundation.BSTR),
        ("mainSessionId", Guid),
        ("subSessionId", Int32),
    ]
    return AAAccountingData
SESSION_TIMEOUT_ACTION_TYPE = Int32
SESSION_TIMEOUT_ACTION_DISCONNECT = 0
SESSION_TIMEOUT_ACTION_SILENT_REAUTH = 1
PolicyAttributeType = Int32
PolicyAttributeType_EnableAllRedirections = 0
PolicyAttributeType_DisableAllRedirections = 1
PolicyAttributeType_DriveRedirectionDisabled = 2
PolicyAttributeType_PrinterRedirectionDisabled = 3
PolicyAttributeType_PortRedirectionDisabled = 4
PolicyAttributeType_ClipboardRedirectionDisabled = 5
PolicyAttributeType_PnpRedirectionDisabled = 6
PolicyAttributeType_AllowOnlySDRServers = 7
AATrustClassID = Int32
AA_UNTRUSTED = 0
AA_TRUSTEDUSER_UNTRUSTEDCLIENT = 1
AA_TRUSTEDUSER_TRUSTEDCLIENT = 2
def _define_ITSGAuthorizeConnectionSink_head():
    class ITSGAuthorizeConnectionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('c27ece33-7781-4318-98ef-1cf2da7b7005')
    return ITSGAuthorizeConnectionSink
def _define_ITSGAuthorizeConnectionSink():
    ITSGAuthorizeConnectionSink = win32more.System.RemoteDesktop.ITSGAuthorizeConnectionSink_head
    ITSGAuthorizeConnectionSink.OnConnectionAuthorized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,Guid,UInt32,POINTER(Byte),UInt32,UInt32,win32more.System.RemoteDesktop.SESSION_TIMEOUT_ACTION_TYPE,win32more.System.RemoteDesktop.AATrustClassID,POINTER(UInt32), use_last_error=False)(3, 'OnConnectionAuthorized', ((1, 'hrIn'),(1, 'mainSessionId'),(1, 'cbSoHResponse'),(1, 'pbSoHResponse'),(1, 'idleTimeout'),(1, 'sessionTimeout'),(1, 'sessionTimeoutAction'),(1, 'trustClass'),(1, 'policyAttributes'),)))
    return ITSGAuthorizeConnectionSink
def _define_ITSGAuthorizeResourceSink_head():
    class ITSGAuthorizeResourceSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('feddfcd4-fa12-4435-ae55-7ad1a9779af7')
    return ITSGAuthorizeResourceSink
def _define_ITSGAuthorizeResourceSink():
    ITSGAuthorizeResourceSink = win32more.System.RemoteDesktop.ITSGAuthorizeResourceSink_head
    ITSGAuthorizeResourceSink.OnChannelAuthorized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,Guid,Int32,POINTER(win32more.Foundation.BSTR),UInt32,POINTER(win32more.Foundation.BSTR),UInt32, use_last_error=False)(3, 'OnChannelAuthorized', ((1, 'hrIn'),(1, 'mainSessionId'),(1, 'subSessionId'),(1, 'allowedResourceNames'),(1, 'numAllowedResourceNames'),(1, 'failedResourceNames'),(1, 'numFailedResourceNames'),)))
    return ITSGAuthorizeResourceSink
def _define_ITSGPolicyEngine_head():
    class ITSGPolicyEngine(win32more.System.Com.IUnknown_head):
        Guid = Guid('8bc24f08-6223-42f4-a5b4-8e37cd135bbd')
    return ITSGPolicyEngine
def _define_ITSGPolicyEngine():
    ITSGPolicyEngine = win32more.System.RemoteDesktop.ITSGPolicyEngine_head
    ITSGPolicyEngine.AuthorizeConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.AAAuthSchemes,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.HANDLE_PTR,win32more.System.RemoteDesktop.ITSGAuthorizeConnectionSink_head, use_last_error=False)(3, 'AuthorizeConnection', ((1, 'mainSessionId'),(1, 'username'),(1, 'authType'),(1, 'clientMachineIP'),(1, 'clientMachineName'),(1, 'sohData'),(1, 'numSOHBytes'),(1, 'cookieData'),(1, 'numCookieBytes'),(1, 'userToken'),(1, 'pSink'),)))
    ITSGPolicyEngine.AuthorizeResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),UInt32,POINTER(win32more.Foundation.BSTR),UInt32,UInt32,win32more.Foundation.BSTR,POINTER(Byte),UInt32,win32more.System.RemoteDesktop.ITSGAuthorizeResourceSink_head, use_last_error=False)(4, 'AuthorizeResource', ((1, 'mainSessionId'),(1, 'subSessionId'),(1, 'username'),(1, 'resourceNames'),(1, 'numResources'),(1, 'alternateResourceNames'),(1, 'numAlternateResourceName'),(1, 'portNumber'),(1, 'operation'),(1, 'cookie'),(1, 'numBytesInCookie'),(1, 'pSink'),)))
    ITSGPolicyEngine.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Refresh', ()))
    ITSGPolicyEngine.IsQuarantineEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'IsQuarantineEnabled', ((1, 'quarantineEnabled'),)))
    return ITSGPolicyEngine
def _define_ITSGAccountingEngine_head():
    class ITSGAccountingEngine(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ce2a0c9-e874-4f1a-86f4-06bbb9115338')
    return ITSGAccountingEngine
def _define_ITSGAccountingEngine():
    ITSGAccountingEngine = win32more.System.RemoteDesktop.ITSGAccountingEngine_head
    ITSGAccountingEngine.DoAccounting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.AAAccountingDataType,win32more.System.RemoteDesktop.AAAccountingData, use_last_error=False)(3, 'DoAccounting', ((1, 'accountingDataType'),(1, 'accountingData'),)))
    return ITSGAccountingEngine
def _define_ITSGAuthenticateUserSink_head():
    class ITSGAuthenticateUserSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c3e2e73-a782-47f9-8dfb-77ee1ed27a03')
    return ITSGAuthenticateUserSink
def _define_ITSGAuthenticateUserSink():
    ITSGAuthenticateUserSink = win32more.System.RemoteDesktop.ITSGAuthenticateUserSink_head
    ITSGAuthenticateUserSink.OnUserAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UIntPtr,win32more.Foundation.HANDLE_PTR, use_last_error=False)(3, 'OnUserAuthenticated', ((1, 'userName'),(1, 'userDomain'),(1, 'context'),(1, 'userToken'),)))
    ITSGAuthenticateUserSink.OnUserAuthenticationFailed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnUserAuthenticationFailed', ((1, 'context'),(1, 'genericErrorCode'),(1, 'specificErrorCode'),)))
    ITSGAuthenticateUserSink.ReauthenticateUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(5, 'ReauthenticateUser', ((1, 'context'),)))
    ITSGAuthenticateUserSink.DisconnectUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(6, 'DisconnectUser', ((1, 'context'),)))
    return ITSGAuthenticateUserSink
def _define_ITSGAuthenticationEngine_head():
    class ITSGAuthenticationEngine(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ee3e5bf-04ab-4691-998c-d7f622321a56')
    return ITSGAuthenticationEngine
def _define_ITSGAuthenticationEngine():
    ITSGAuthenticationEngine = win32more.System.RemoteDesktop.ITSGAuthenticationEngine_head
    ITSGAuthenticationEngine.AuthenticateUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,c_char_p_no,UInt32,UIntPtr,win32more.System.RemoteDesktop.ITSGAuthenticateUserSink_head, use_last_error=False)(3, 'AuthenticateUser', ((1, 'mainSessionId'),(1, 'cookieData'),(1, 'numCookieBytes'),(1, 'context'),(1, 'pSink'),)))
    ITSGAuthenticationEngine.CancelAuthentication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UIntPtr, use_last_error=False)(4, 'CancelAuthentication', ((1, 'mainSessionId'),(1, 'context'),)))
    return ITSGAuthenticationEngine
WTS_CONNECTSTATE_CLASS = Int32
WTS_CONNECTSTATE_CLASS_WTSActive = 0
WTS_CONNECTSTATE_CLASS_WTSConnected = 1
WTS_CONNECTSTATE_CLASS_WTSConnectQuery = 2
WTS_CONNECTSTATE_CLASS_WTSShadow = 3
WTS_CONNECTSTATE_CLASS_WTSDisconnected = 4
WTS_CONNECTSTATE_CLASS_WTSIdle = 5
WTS_CONNECTSTATE_CLASS_WTSListen = 6
WTS_CONNECTSTATE_CLASS_WTSReset = 7
WTS_CONNECTSTATE_CLASS_WTSDown = 8
WTS_CONNECTSTATE_CLASS_WTSInit = 9
def _define_WTS_SERVER_INFOW_head():
    class WTS_SERVER_INFOW(Structure):
        pass
    return WTS_SERVER_INFOW
def _define_WTS_SERVER_INFOW():
    WTS_SERVER_INFOW = win32more.System.RemoteDesktop.WTS_SERVER_INFOW_head
    WTS_SERVER_INFOW._fields_ = [
        ("pServerName", win32more.Foundation.PWSTR),
    ]
    return WTS_SERVER_INFOW
def _define_WTS_SERVER_INFOA_head():
    class WTS_SERVER_INFOA(Structure):
        pass
    return WTS_SERVER_INFOA
def _define_WTS_SERVER_INFOA():
    WTS_SERVER_INFOA = win32more.System.RemoteDesktop.WTS_SERVER_INFOA_head
    WTS_SERVER_INFOA._fields_ = [
        ("pServerName", win32more.Foundation.PSTR),
    ]
    return WTS_SERVER_INFOA
def _define_WTS_SESSION_INFOW_head():
    class WTS_SESSION_INFOW(Structure):
        pass
    return WTS_SESSION_INFOW
def _define_WTS_SESSION_INFOW():
    WTS_SESSION_INFOW = win32more.System.RemoteDesktop.WTS_SESSION_INFOW_head
    WTS_SESSION_INFOW._fields_ = [
        ("SessionId", UInt32),
        ("pWinStationName", win32more.Foundation.PWSTR),
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
    ]
    return WTS_SESSION_INFOW
def _define_WTS_SESSION_INFOA_head():
    class WTS_SESSION_INFOA(Structure):
        pass
    return WTS_SESSION_INFOA
def _define_WTS_SESSION_INFOA():
    WTS_SESSION_INFOA = win32more.System.RemoteDesktop.WTS_SESSION_INFOA_head
    WTS_SESSION_INFOA._fields_ = [
        ("SessionId", UInt32),
        ("pWinStationName", win32more.Foundation.PSTR),
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
    ]
    return WTS_SESSION_INFOA
def _define_WTS_SESSION_INFO_1W_head():
    class WTS_SESSION_INFO_1W(Structure):
        pass
    return WTS_SESSION_INFO_1W
def _define_WTS_SESSION_INFO_1W():
    WTS_SESSION_INFO_1W = win32more.System.RemoteDesktop.WTS_SESSION_INFO_1W_head
    WTS_SESSION_INFO_1W._fields_ = [
        ("ExecEnvId", UInt32),
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionId", UInt32),
        ("pSessionName", win32more.Foundation.PWSTR),
        ("pHostName", win32more.Foundation.PWSTR),
        ("pUserName", win32more.Foundation.PWSTR),
        ("pDomainName", win32more.Foundation.PWSTR),
        ("pFarmName", win32more.Foundation.PWSTR),
    ]
    return WTS_SESSION_INFO_1W
def _define_WTS_SESSION_INFO_1A_head():
    class WTS_SESSION_INFO_1A(Structure):
        pass
    return WTS_SESSION_INFO_1A
def _define_WTS_SESSION_INFO_1A():
    WTS_SESSION_INFO_1A = win32more.System.RemoteDesktop.WTS_SESSION_INFO_1A_head
    WTS_SESSION_INFO_1A._fields_ = [
        ("ExecEnvId", UInt32),
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionId", UInt32),
        ("pSessionName", win32more.Foundation.PSTR),
        ("pHostName", win32more.Foundation.PSTR),
        ("pUserName", win32more.Foundation.PSTR),
        ("pDomainName", win32more.Foundation.PSTR),
        ("pFarmName", win32more.Foundation.PSTR),
    ]
    return WTS_SESSION_INFO_1A
def _define_WTS_PROCESS_INFOW_head():
    class WTS_PROCESS_INFOW(Structure):
        pass
    return WTS_PROCESS_INFOW
def _define_WTS_PROCESS_INFOW():
    WTS_PROCESS_INFOW = win32more.System.RemoteDesktop.WTS_PROCESS_INFOW_head
    WTS_PROCESS_INFOW._fields_ = [
        ("SessionId", UInt32),
        ("ProcessId", UInt32),
        ("pProcessName", win32more.Foundation.PWSTR),
        ("pUserSid", win32more.Foundation.PSID),
    ]
    return WTS_PROCESS_INFOW
def _define_WTS_PROCESS_INFOA_head():
    class WTS_PROCESS_INFOA(Structure):
        pass
    return WTS_PROCESS_INFOA
def _define_WTS_PROCESS_INFOA():
    WTS_PROCESS_INFOA = win32more.System.RemoteDesktop.WTS_PROCESS_INFOA_head
    WTS_PROCESS_INFOA._fields_ = [
        ("SessionId", UInt32),
        ("ProcessId", UInt32),
        ("pProcessName", win32more.Foundation.PSTR),
        ("pUserSid", win32more.Foundation.PSID),
    ]
    return WTS_PROCESS_INFOA
WTS_INFO_CLASS = Int32
WTS_INFO_CLASS_WTSInitialProgram = 0
WTS_INFO_CLASS_WTSApplicationName = 1
WTS_INFO_CLASS_WTSWorkingDirectory = 2
WTS_INFO_CLASS_WTSOEMId = 3
WTS_INFO_CLASS_WTSSessionId = 4
WTS_INFO_CLASS_WTSUserName = 5
WTS_INFO_CLASS_WTSWinStationName = 6
WTS_INFO_CLASS_WTSDomainName = 7
WTS_INFO_CLASS_WTSConnectState = 8
WTS_INFO_CLASS_WTSClientBuildNumber = 9
WTS_INFO_CLASS_WTSClientName = 10
WTS_INFO_CLASS_WTSClientDirectory = 11
WTS_INFO_CLASS_WTSClientProductId = 12
WTS_INFO_CLASS_WTSClientHardwareId = 13
WTS_INFO_CLASS_WTSClientAddress = 14
WTS_INFO_CLASS_WTSClientDisplay = 15
WTS_INFO_CLASS_WTSClientProtocolType = 16
WTS_INFO_CLASS_WTSIdleTime = 17
WTS_INFO_CLASS_WTSLogonTime = 18
WTS_INFO_CLASS_WTSIncomingBytes = 19
WTS_INFO_CLASS_WTSOutgoingBytes = 20
WTS_INFO_CLASS_WTSIncomingFrames = 21
WTS_INFO_CLASS_WTSOutgoingFrames = 22
WTS_INFO_CLASS_WTSClientInfo = 23
WTS_INFO_CLASS_WTSSessionInfo = 24
WTS_INFO_CLASS_WTSSessionInfoEx = 25
WTS_INFO_CLASS_WTSConfigInfo = 26
WTS_INFO_CLASS_WTSValidationInfo = 27
WTS_INFO_CLASS_WTSSessionAddressV4 = 28
WTS_INFO_CLASS_WTSIsRemoteSession = 29
def _define_WTSCONFIGINFOW_head():
    class WTSCONFIGINFOW(Structure):
        pass
    return WTSCONFIGINFOW
def _define_WTSCONFIGINFOW():
    WTSCONFIGINFOW = win32more.System.RemoteDesktop.WTSCONFIGINFOW_head
    WTSCONFIGINFOW._fields_ = [
        ("version", UInt32),
        ("fConnectClientDrivesAtLogon", UInt32),
        ("fConnectPrinterAtLogon", UInt32),
        ("fDisablePrinterRedirection", UInt32),
        ("fDisableDefaultMainClientPrinter", UInt32),
        ("ShadowSettings", UInt32),
        ("LogonUserName", Char * 21),
        ("LogonDomain", Char * 18),
        ("WorkDirectory", Char * 261),
        ("InitialProgram", Char * 261),
        ("ApplicationName", Char * 261),
    ]
    return WTSCONFIGINFOW
def _define_WTSCONFIGINFOA_head():
    class WTSCONFIGINFOA(Structure):
        pass
    return WTSCONFIGINFOA
def _define_WTSCONFIGINFOA():
    WTSCONFIGINFOA = win32more.System.RemoteDesktop.WTSCONFIGINFOA_head
    WTSCONFIGINFOA._fields_ = [
        ("version", UInt32),
        ("fConnectClientDrivesAtLogon", UInt32),
        ("fConnectPrinterAtLogon", UInt32),
        ("fDisablePrinterRedirection", UInt32),
        ("fDisableDefaultMainClientPrinter", UInt32),
        ("ShadowSettings", UInt32),
        ("LogonUserName", win32more.Foundation.CHAR * 21),
        ("LogonDomain", win32more.Foundation.CHAR * 18),
        ("WorkDirectory", win32more.Foundation.CHAR * 261),
        ("InitialProgram", win32more.Foundation.CHAR * 261),
        ("ApplicationName", win32more.Foundation.CHAR * 261),
    ]
    return WTSCONFIGINFOA
def _define_WTSINFOW_head():
    class WTSINFOW(Structure):
        pass
    return WTSINFOW
def _define_WTSINFOW():
    WTSINFOW = win32more.System.RemoteDesktop.WTSINFOW_head
    WTSINFOW._fields_ = [
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionId", UInt32),
        ("IncomingBytes", UInt32),
        ("OutgoingBytes", UInt32),
        ("IncomingFrames", UInt32),
        ("OutgoingFrames", UInt32),
        ("IncomingCompressedBytes", UInt32),
        ("OutgoingCompressedBytes", UInt32),
        ("WinStationName", Char * 32),
        ("Domain", Char * 17),
        ("UserName", Char * 21),
        ("ConnectTime", win32more.Foundation.LARGE_INTEGER),
        ("DisconnectTime", win32more.Foundation.LARGE_INTEGER),
        ("LastInputTime", win32more.Foundation.LARGE_INTEGER),
        ("LogonTime", win32more.Foundation.LARGE_INTEGER),
        ("CurrentTime", win32more.Foundation.LARGE_INTEGER),
    ]
    return WTSINFOW
def _define_WTSINFOA_head():
    class WTSINFOA(Structure):
        pass
    return WTSINFOA
def _define_WTSINFOA():
    WTSINFOA = win32more.System.RemoteDesktop.WTSINFOA_head
    WTSINFOA._fields_ = [
        ("State", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionId", UInt32),
        ("IncomingBytes", UInt32),
        ("OutgoingBytes", UInt32),
        ("IncomingFrames", UInt32),
        ("OutgoingFrames", UInt32),
        ("IncomingCompressedBytes", UInt32),
        ("OutgoingCompressedBy", UInt32),
        ("WinStationName", win32more.Foundation.CHAR * 32),
        ("Domain", win32more.Foundation.CHAR * 17),
        ("UserName", win32more.Foundation.CHAR * 21),
        ("ConnectTime", win32more.Foundation.LARGE_INTEGER),
        ("DisconnectTime", win32more.Foundation.LARGE_INTEGER),
        ("LastInputTime", win32more.Foundation.LARGE_INTEGER),
        ("LogonTime", win32more.Foundation.LARGE_INTEGER),
        ("CurrentTime", win32more.Foundation.LARGE_INTEGER),
    ]
    return WTSINFOA
def _define_WTSINFOEX_LEVEL1_W_head():
    class WTSINFOEX_LEVEL1_W(Structure):
        pass
    return WTSINFOEX_LEVEL1_W
def _define_WTSINFOEX_LEVEL1_W():
    WTSINFOEX_LEVEL1_W = win32more.System.RemoteDesktop.WTSINFOEX_LEVEL1_W_head
    WTSINFOEX_LEVEL1_W._fields_ = [
        ("SessionId", UInt32),
        ("SessionState", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionFlags", Int32),
        ("WinStationName", Char * 33),
        ("UserName", Char * 21),
        ("DomainName", Char * 18),
        ("LogonTime", win32more.Foundation.LARGE_INTEGER),
        ("ConnectTime", win32more.Foundation.LARGE_INTEGER),
        ("DisconnectTime", win32more.Foundation.LARGE_INTEGER),
        ("LastInputTime", win32more.Foundation.LARGE_INTEGER),
        ("CurrentTime", win32more.Foundation.LARGE_INTEGER),
        ("IncomingBytes", UInt32),
        ("OutgoingBytes", UInt32),
        ("IncomingFrames", UInt32),
        ("OutgoingFrames", UInt32),
        ("IncomingCompressedBytes", UInt32),
        ("OutgoingCompressedBytes", UInt32),
    ]
    return WTSINFOEX_LEVEL1_W
def _define_WTSINFOEX_LEVEL1_A_head():
    class WTSINFOEX_LEVEL1_A(Structure):
        pass
    return WTSINFOEX_LEVEL1_A
def _define_WTSINFOEX_LEVEL1_A():
    WTSINFOEX_LEVEL1_A = win32more.System.RemoteDesktop.WTSINFOEX_LEVEL1_A_head
    WTSINFOEX_LEVEL1_A._fields_ = [
        ("SessionId", UInt32),
        ("SessionState", win32more.System.RemoteDesktop.WTS_CONNECTSTATE_CLASS),
        ("SessionFlags", Int32),
        ("WinStationName", win32more.Foundation.CHAR * 33),
        ("UserName", win32more.Foundation.CHAR * 21),
        ("DomainName", win32more.Foundation.CHAR * 18),
        ("LogonTime", win32more.Foundation.LARGE_INTEGER),
        ("ConnectTime", win32more.Foundation.LARGE_INTEGER),
        ("DisconnectTime", win32more.Foundation.LARGE_INTEGER),
        ("LastInputTime", win32more.Foundation.LARGE_INTEGER),
        ("CurrentTime", win32more.Foundation.LARGE_INTEGER),
        ("IncomingBytes", UInt32),
        ("OutgoingBytes", UInt32),
        ("IncomingFrames", UInt32),
        ("OutgoingFrames", UInt32),
        ("IncomingCompressedBytes", UInt32),
        ("OutgoingCompressedBytes", UInt32),
    ]
    return WTSINFOEX_LEVEL1_A
def _define_WTSINFOEX_LEVEL_W_head():
    class WTSINFOEX_LEVEL_W(Union):
        pass
    return WTSINFOEX_LEVEL_W
def _define_WTSINFOEX_LEVEL_W():
    WTSINFOEX_LEVEL_W = win32more.System.RemoteDesktop.WTSINFOEX_LEVEL_W_head
    WTSINFOEX_LEVEL_W._fields_ = [
        ("WTSInfoExLevel1", win32more.System.RemoteDesktop.WTSINFOEX_LEVEL1_W),
    ]
    return WTSINFOEX_LEVEL_W
def _define_WTSINFOEX_LEVEL_A_head():
    class WTSINFOEX_LEVEL_A(Union):
        pass
    return WTSINFOEX_LEVEL_A
def _define_WTSINFOEX_LEVEL_A():
    WTSINFOEX_LEVEL_A = win32more.System.RemoteDesktop.WTSINFOEX_LEVEL_A_head
    WTSINFOEX_LEVEL_A._fields_ = [
        ("WTSInfoExLevel1", win32more.System.RemoteDesktop.WTSINFOEX_LEVEL1_A),
    ]
    return WTSINFOEX_LEVEL_A
def _define_WTSINFOEXW_head():
    class WTSINFOEXW(Structure):
        pass
    return WTSINFOEXW
def _define_WTSINFOEXW():
    WTSINFOEXW = win32more.System.RemoteDesktop.WTSINFOEXW_head
    WTSINFOEXW._fields_ = [
        ("Level", UInt32),
        ("Data", win32more.System.RemoteDesktop.WTSINFOEX_LEVEL_W),
    ]
    return WTSINFOEXW
def _define_WTSINFOEXA_head():
    class WTSINFOEXA(Structure):
        pass
    return WTSINFOEXA
def _define_WTSINFOEXA():
    WTSINFOEXA = win32more.System.RemoteDesktop.WTSINFOEXA_head
    WTSINFOEXA._fields_ = [
        ("Level", UInt32),
        ("Data", win32more.System.RemoteDesktop.WTSINFOEX_LEVEL_A),
    ]
    return WTSINFOEXA
def _define_WTSCLIENTW_head():
    class WTSCLIENTW(Structure):
        pass
    return WTSCLIENTW
def _define_WTSCLIENTW():
    WTSCLIENTW = win32more.System.RemoteDesktop.WTSCLIENTW_head
    WTSCLIENTW._fields_ = [
        ("ClientName", Char * 21),
        ("Domain", Char * 18),
        ("UserName", Char * 21),
        ("WorkDirectory", Char * 261),
        ("InitialProgram", Char * 261),
        ("EncryptionLevel", Byte),
        ("ClientAddressFamily", UInt32),
        ("ClientAddress", UInt16 * 31),
        ("HRes", UInt16),
        ("VRes", UInt16),
        ("ColorDepth", UInt16),
        ("ClientDirectory", Char * 261),
        ("ClientBuildNumber", UInt32),
        ("ClientHardwareId", UInt32),
        ("ClientProductId", UInt16),
        ("OutBufCountHost", UInt16),
        ("OutBufCountClient", UInt16),
        ("OutBufLength", UInt16),
        ("DeviceId", Char * 261),
    ]
    return WTSCLIENTW
def _define_WTSCLIENTA_head():
    class WTSCLIENTA(Structure):
        pass
    return WTSCLIENTA
def _define_WTSCLIENTA():
    WTSCLIENTA = win32more.System.RemoteDesktop.WTSCLIENTA_head
    WTSCLIENTA._fields_ = [
        ("ClientName", win32more.Foundation.CHAR * 21),
        ("Domain", win32more.Foundation.CHAR * 18),
        ("UserName", win32more.Foundation.CHAR * 21),
        ("WorkDirectory", win32more.Foundation.CHAR * 261),
        ("InitialProgram", win32more.Foundation.CHAR * 261),
        ("EncryptionLevel", Byte),
        ("ClientAddressFamily", UInt32),
        ("ClientAddress", UInt16 * 31),
        ("HRes", UInt16),
        ("VRes", UInt16),
        ("ColorDepth", UInt16),
        ("ClientDirectory", win32more.Foundation.CHAR * 261),
        ("ClientBuildNumber", UInt32),
        ("ClientHardwareId", UInt32),
        ("ClientProductId", UInt16),
        ("OutBufCountHost", UInt16),
        ("OutBufCountClient", UInt16),
        ("OutBufLength", UInt16),
        ("DeviceId", win32more.Foundation.CHAR * 261),
    ]
    return WTSCLIENTA
def _define__WTS_PRODUCT_INFOA_head():
    class _WTS_PRODUCT_INFOA(Structure):
        pass
    return _WTS_PRODUCT_INFOA
def _define__WTS_PRODUCT_INFOA():
    _WTS_PRODUCT_INFOA = win32more.System.RemoteDesktop._WTS_PRODUCT_INFOA_head
    _WTS_PRODUCT_INFOA._fields_ = [
        ("CompanyName", win32more.Foundation.CHAR * 256),
        ("ProductID", win32more.Foundation.CHAR * 4),
    ]
    return _WTS_PRODUCT_INFOA
def _define__WTS_PRODUCT_INFOW_head():
    class _WTS_PRODUCT_INFOW(Structure):
        pass
    return _WTS_PRODUCT_INFOW
def _define__WTS_PRODUCT_INFOW():
    _WTS_PRODUCT_INFOW = win32more.System.RemoteDesktop._WTS_PRODUCT_INFOW_head
    _WTS_PRODUCT_INFOW._fields_ = [
        ("CompanyName", Char * 256),
        ("ProductID", Char * 4),
    ]
    return _WTS_PRODUCT_INFOW
def _define_WTS_VALIDATION_INFORMATIONA_head():
    class WTS_VALIDATION_INFORMATIONA(Structure):
        pass
    return WTS_VALIDATION_INFORMATIONA
def _define_WTS_VALIDATION_INFORMATIONA():
    WTS_VALIDATION_INFORMATIONA = win32more.System.RemoteDesktop.WTS_VALIDATION_INFORMATIONA_head
    WTS_VALIDATION_INFORMATIONA._fields_ = [
        ("ProductInfo", win32more.System.RemoteDesktop._WTS_PRODUCT_INFOA),
        ("License", Byte * 16384),
        ("LicenseLength", UInt32),
        ("HardwareID", Byte * 20),
        ("HardwareIDLength", UInt32),
    ]
    return WTS_VALIDATION_INFORMATIONA
def _define_WTS_VALIDATION_INFORMATIONW_head():
    class WTS_VALIDATION_INFORMATIONW(Structure):
        pass
    return WTS_VALIDATION_INFORMATIONW
def _define_WTS_VALIDATION_INFORMATIONW():
    WTS_VALIDATION_INFORMATIONW = win32more.System.RemoteDesktop.WTS_VALIDATION_INFORMATIONW_head
    WTS_VALIDATION_INFORMATIONW._fields_ = [
        ("ProductInfo", win32more.System.RemoteDesktop._WTS_PRODUCT_INFOW),
        ("License", Byte * 16384),
        ("LicenseLength", UInt32),
        ("HardwareID", Byte * 20),
        ("HardwareIDLength", UInt32),
    ]
    return WTS_VALIDATION_INFORMATIONW
def _define_WTS_CLIENT_ADDRESS_head():
    class WTS_CLIENT_ADDRESS(Structure):
        pass
    return WTS_CLIENT_ADDRESS
def _define_WTS_CLIENT_ADDRESS():
    WTS_CLIENT_ADDRESS = win32more.System.RemoteDesktop.WTS_CLIENT_ADDRESS_head
    WTS_CLIENT_ADDRESS._fields_ = [
        ("AddressFamily", UInt32),
        ("Address", Byte * 20),
    ]
    return WTS_CLIENT_ADDRESS
def _define_WTS_CLIENT_DISPLAY_head():
    class WTS_CLIENT_DISPLAY(Structure):
        pass
    return WTS_CLIENT_DISPLAY
def _define_WTS_CLIENT_DISPLAY():
    WTS_CLIENT_DISPLAY = win32more.System.RemoteDesktop.WTS_CLIENT_DISPLAY_head
    WTS_CLIENT_DISPLAY._fields_ = [
        ("HorizontalResolution", UInt32),
        ("VerticalResolution", UInt32),
        ("ColorDepth", UInt32),
    ]
    return WTS_CLIENT_DISPLAY
WTS_CONFIG_CLASS = Int32
WTS_CONFIG_CLASS_WTSUserConfigInitialProgram = 0
WTS_CONFIG_CLASS_WTSUserConfigWorkingDirectory = 1
WTS_CONFIG_CLASS_WTSUserConfigfInheritInitialProgram = 2
WTS_CONFIG_CLASS_WTSUserConfigfAllowLogonTerminalServer = 3
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsConnections = 4
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsDisconnections = 5
WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsIdle = 6
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDrives = 7
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientPrinters = 8
WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDefaultPrinter = 9
WTS_CONFIG_CLASS_WTSUserConfigBrokenTimeoutSettings = 10
WTS_CONFIG_CLASS_WTSUserConfigReconnectSettings = 11
WTS_CONFIG_CLASS_WTSUserConfigModemCallbackSettings = 12
WTS_CONFIG_CLASS_WTSUserConfigModemCallbackPhoneNumber = 13
WTS_CONFIG_CLASS_WTSUserConfigShadowingSettings = 14
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerProfilePath = 15
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDir = 16
WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDirDrive = 17
WTS_CONFIG_CLASS_WTSUserConfigfTerminalServerRemoteHomeDir = 18
WTS_CONFIG_CLASS_WTSUserConfigUser = 19
WTS_CONFIG_SOURCE = Int32
WTS_CONFIG_SOURCE_WTSUserConfigSourceSAM = 0
def _define_WTSUSERCONFIGA_head():
    class WTSUSERCONFIGA(Structure):
        pass
    return WTSUSERCONFIGA
def _define_WTSUSERCONFIGA():
    WTSUSERCONFIGA = win32more.System.RemoteDesktop.WTSUSERCONFIGA_head
    WTSUSERCONFIGA._fields_ = [
        ("Source", UInt32),
        ("InheritInitialProgram", UInt32),
        ("AllowLogonTerminalServer", UInt32),
        ("TimeoutSettingsConnections", UInt32),
        ("TimeoutSettingsDisconnections", UInt32),
        ("TimeoutSettingsIdle", UInt32),
        ("DeviceClientDrives", UInt32),
        ("DeviceClientPrinters", UInt32),
        ("ClientDefaultPrinter", UInt32),
        ("BrokenTimeoutSettings", UInt32),
        ("ReconnectSettings", UInt32),
        ("ShadowingSettings", UInt32),
        ("TerminalServerRemoteHomeDir", UInt32),
        ("InitialProgram", win32more.Foundation.CHAR * 261),
        ("WorkDirectory", win32more.Foundation.CHAR * 261),
        ("TerminalServerProfilePath", win32more.Foundation.CHAR * 261),
        ("TerminalServerHomeDir", win32more.Foundation.CHAR * 261),
        ("TerminalServerHomeDirDrive", win32more.Foundation.CHAR * 4),
    ]
    return WTSUSERCONFIGA
def _define_WTSUSERCONFIGW_head():
    class WTSUSERCONFIGW(Structure):
        pass
    return WTSUSERCONFIGW
def _define_WTSUSERCONFIGW():
    WTSUSERCONFIGW = win32more.System.RemoteDesktop.WTSUSERCONFIGW_head
    WTSUSERCONFIGW._fields_ = [
        ("Source", UInt32),
        ("InheritInitialProgram", UInt32),
        ("AllowLogonTerminalServer", UInt32),
        ("TimeoutSettingsConnections", UInt32),
        ("TimeoutSettingsDisconnections", UInt32),
        ("TimeoutSettingsIdle", UInt32),
        ("DeviceClientDrives", UInt32),
        ("DeviceClientPrinters", UInt32),
        ("ClientDefaultPrinter", UInt32),
        ("BrokenTimeoutSettings", UInt32),
        ("ReconnectSettings", UInt32),
        ("ShadowingSettings", UInt32),
        ("TerminalServerRemoteHomeDir", UInt32),
        ("InitialProgram", Char * 261),
        ("WorkDirectory", Char * 261),
        ("TerminalServerProfilePath", Char * 261),
        ("TerminalServerHomeDir", Char * 261),
        ("TerminalServerHomeDirDrive", Char * 4),
    ]
    return WTSUSERCONFIGW
WTS_VIRTUAL_CLASS = Int32
WTS_VIRTUAL_CLASS_WTSVirtualClientData = 0
WTS_VIRTUAL_CLASS_WTSVirtualFileHandle = 1
def _define_WTS_SESSION_ADDRESS_head():
    class WTS_SESSION_ADDRESS(Structure):
        pass
    return WTS_SESSION_ADDRESS
def _define_WTS_SESSION_ADDRESS():
    WTS_SESSION_ADDRESS = win32more.System.RemoteDesktop.WTS_SESSION_ADDRESS_head
    WTS_SESSION_ADDRESS._fields_ = [
        ("AddressFamily", UInt32),
        ("Address", Byte * 20),
    ]
    return WTS_SESSION_ADDRESS
def _define_WTS_PROCESS_INFO_EXW_head():
    class WTS_PROCESS_INFO_EXW(Structure):
        pass
    return WTS_PROCESS_INFO_EXW
def _define_WTS_PROCESS_INFO_EXW():
    WTS_PROCESS_INFO_EXW = win32more.System.RemoteDesktop.WTS_PROCESS_INFO_EXW_head
    WTS_PROCESS_INFO_EXW._fields_ = [
        ("SessionId", UInt32),
        ("ProcessId", UInt32),
        ("pProcessName", win32more.Foundation.PWSTR),
        ("pUserSid", win32more.Foundation.PSID),
        ("NumberOfThreads", UInt32),
        ("HandleCount", UInt32),
        ("PagefileUsage", UInt32),
        ("PeakPagefileUsage", UInt32),
        ("WorkingSetSize", UInt32),
        ("PeakWorkingSetSize", UInt32),
        ("UserTime", win32more.Foundation.LARGE_INTEGER),
        ("KernelTime", win32more.Foundation.LARGE_INTEGER),
    ]
    return WTS_PROCESS_INFO_EXW
def _define_WTS_PROCESS_INFO_EXA_head():
    class WTS_PROCESS_INFO_EXA(Structure):
        pass
    return WTS_PROCESS_INFO_EXA
def _define_WTS_PROCESS_INFO_EXA():
    WTS_PROCESS_INFO_EXA = win32more.System.RemoteDesktop.WTS_PROCESS_INFO_EXA_head
    WTS_PROCESS_INFO_EXA._fields_ = [
        ("SessionId", UInt32),
        ("ProcessId", UInt32),
        ("pProcessName", win32more.Foundation.PSTR),
        ("pUserSid", win32more.Foundation.PSID),
        ("NumberOfThreads", UInt32),
        ("HandleCount", UInt32),
        ("PagefileUsage", UInt32),
        ("PeakPagefileUsage", UInt32),
        ("WorkingSetSize", UInt32),
        ("PeakWorkingSetSize", UInt32),
        ("UserTime", win32more.Foundation.LARGE_INTEGER),
        ("KernelTime", win32more.Foundation.LARGE_INTEGER),
    ]
    return WTS_PROCESS_INFO_EXA
WTS_TYPE_CLASS = Int32
WTS_TYPE_CLASS_WTSTypeProcessInfoLevel0 = 0
WTS_TYPE_CLASS_WTSTypeProcessInfoLevel1 = 1
WTS_TYPE_CLASS_WTSTypeSessionInfoLevel1 = 2
def _define_WTSLISTENERCONFIGW_head():
    class WTSLISTENERCONFIGW(Structure):
        pass
    return WTSLISTENERCONFIGW
def _define_WTSLISTENERCONFIGW():
    WTSLISTENERCONFIGW = win32more.System.RemoteDesktop.WTSLISTENERCONFIGW_head
    WTSLISTENERCONFIGW._fields_ = [
        ("version", UInt32),
        ("fEnableListener", UInt32),
        ("MaxConnectionCount", UInt32),
        ("fPromptForPassword", UInt32),
        ("fInheritColorDepth", UInt32),
        ("ColorDepth", UInt32),
        ("fInheritBrokenTimeoutSettings", UInt32),
        ("BrokenTimeoutSettings", UInt32),
        ("fDisablePrinterRedirection", UInt32),
        ("fDisableDriveRedirection", UInt32),
        ("fDisableComPortRedirection", UInt32),
        ("fDisableLPTPortRedirection", UInt32),
        ("fDisableClipboardRedirection", UInt32),
        ("fDisableAudioRedirection", UInt32),
        ("fDisablePNPRedirection", UInt32),
        ("fDisableDefaultMainClientPrinter", UInt32),
        ("LanAdapter", UInt32),
        ("PortNumber", UInt32),
        ("fInheritShadowSettings", UInt32),
        ("ShadowSettings", UInt32),
        ("TimeoutSettingsConnection", UInt32),
        ("TimeoutSettingsDisconnection", UInt32),
        ("TimeoutSettingsIdle", UInt32),
        ("SecurityLayer", UInt32),
        ("MinEncryptionLevel", UInt32),
        ("UserAuthentication", UInt32),
        ("Comment", Char * 61),
        ("LogonUserName", Char * 21),
        ("LogonDomain", Char * 18),
        ("WorkDirectory", Char * 261),
        ("InitialProgram", Char * 261),
    ]
    return WTSLISTENERCONFIGW
def _define_WTSLISTENERCONFIGA_head():
    class WTSLISTENERCONFIGA(Structure):
        pass
    return WTSLISTENERCONFIGA
def _define_WTSLISTENERCONFIGA():
    WTSLISTENERCONFIGA = win32more.System.RemoteDesktop.WTSLISTENERCONFIGA_head
    WTSLISTENERCONFIGA._fields_ = [
        ("version", UInt32),
        ("fEnableListener", UInt32),
        ("MaxConnectionCount", UInt32),
        ("fPromptForPassword", UInt32),
        ("fInheritColorDepth", UInt32),
        ("ColorDepth", UInt32),
        ("fInheritBrokenTimeoutSettings", UInt32),
        ("BrokenTimeoutSettings", UInt32),
        ("fDisablePrinterRedirection", UInt32),
        ("fDisableDriveRedirection", UInt32),
        ("fDisableComPortRedirection", UInt32),
        ("fDisableLPTPortRedirection", UInt32),
        ("fDisableClipboardRedirection", UInt32),
        ("fDisableAudioRedirection", UInt32),
        ("fDisablePNPRedirection", UInt32),
        ("fDisableDefaultMainClientPrinter", UInt32),
        ("LanAdapter", UInt32),
        ("PortNumber", UInt32),
        ("fInheritShadowSettings", UInt32),
        ("ShadowSettings", UInt32),
        ("TimeoutSettingsConnection", UInt32),
        ("TimeoutSettingsDisconnection", UInt32),
        ("TimeoutSettingsIdle", UInt32),
        ("SecurityLayer", UInt32),
        ("MinEncryptionLevel", UInt32),
        ("UserAuthentication", UInt32),
        ("Comment", win32more.Foundation.CHAR * 61),
        ("LogonUserName", win32more.Foundation.CHAR * 21),
        ("LogonDomain", win32more.Foundation.CHAR * 18),
        ("WorkDirectory", win32more.Foundation.CHAR * 261),
        ("InitialProgram", win32more.Foundation.CHAR * 261),
    ]
    return WTSLISTENERCONFIGA
WTSSBX_MACHINE_DRAIN = Int32
WTSSBX_MACHINE_DRAIN_UNSPEC = 0
WTSSBX_MACHINE_DRAIN_OFF = 1
WTSSBX_MACHINE_DRAIN_ON = 2
WTSSBX_MACHINE_SESSION_MODE = Int32
WTSSBX_MACHINE_SESSION_MODE_UNSPEC = 0
WTSSBX_MACHINE_SESSION_MODE_SINGLE = 1
WTSSBX_MACHINE_SESSION_MODE_MULTIPLE = 2
WTSSBX_ADDRESS_FAMILY = Int32
WTSSBX_ADDRESS_FAMILY_AF_UNSPEC = 0
WTSSBX_ADDRESS_FAMILY_AF_INET = 1
WTSSBX_ADDRESS_FAMILY_AF_INET6 = 2
WTSSBX_ADDRESS_FAMILY_AF_IPX = 3
WTSSBX_ADDRESS_FAMILY_AF_NETBIOS = 4
def _define_WTSSBX_IP_ADDRESS_head():
    class WTSSBX_IP_ADDRESS(Structure):
        pass
    return WTSSBX_IP_ADDRESS
def _define_WTSSBX_IP_ADDRESS():
    WTSSBX_IP_ADDRESS = win32more.System.RemoteDesktop.WTSSBX_IP_ADDRESS_head
    WTSSBX_IP_ADDRESS._fields_ = [
        ("AddressFamily", win32more.System.RemoteDesktop.WTSSBX_ADDRESS_FAMILY),
        ("Address", Byte * 16),
        ("PortNumber", UInt16),
        ("dwScope", UInt32),
    ]
    return WTSSBX_IP_ADDRESS
WTSSBX_MACHINE_STATE = Int32
WTSSBX_MACHINE_STATE_UNSPEC = 0
WTSSBX_MACHINE_STATE_READY = 1
WTSSBX_MACHINE_STATE_SYNCHRONIZING = 2
def _define_WTSSBX_MACHINE_CONNECT_INFO_head():
    class WTSSBX_MACHINE_CONNECT_INFO(Structure):
        pass
    return WTSSBX_MACHINE_CONNECT_INFO
def _define_WTSSBX_MACHINE_CONNECT_INFO():
    WTSSBX_MACHINE_CONNECT_INFO = win32more.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO_head
    WTSSBX_MACHINE_CONNECT_INFO._fields_ = [
        ("wczMachineFQDN", Char * 257),
        ("wczMachineNetBiosName", Char * 17),
        ("dwNumOfIPAddr", UInt32),
        ("IPaddr", win32more.System.RemoteDesktop.WTSSBX_IP_ADDRESS * 12),
    ]
    return WTSSBX_MACHINE_CONNECT_INFO
def _define_WTSSBX_MACHINE_INFO_head():
    class WTSSBX_MACHINE_INFO(Structure):
        pass
    return WTSSBX_MACHINE_INFO
def _define_WTSSBX_MACHINE_INFO():
    WTSSBX_MACHINE_INFO = win32more.System.RemoteDesktop.WTSSBX_MACHINE_INFO_head
    WTSSBX_MACHINE_INFO._fields_ = [
        ("ClientConnectInfo", win32more.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO),
        ("wczFarmName", Char * 257),
        ("InternalIPAddress", win32more.System.RemoteDesktop.WTSSBX_IP_ADDRESS),
        ("dwMaxSessionsLimit", UInt32),
        ("ServerWeight", UInt32),
        ("SingleSessionMode", win32more.System.RemoteDesktop.WTSSBX_MACHINE_SESSION_MODE),
        ("InDrain", win32more.System.RemoteDesktop.WTSSBX_MACHINE_DRAIN),
        ("MachineState", win32more.System.RemoteDesktop.WTSSBX_MACHINE_STATE),
    ]
    return WTSSBX_MACHINE_INFO
WTSSBX_SESSION_STATE = Int32
WTSSBX_SESSION_STATE_UNSPEC = 0
WTSSBX_SESSION_STATE_ACTIVE = 1
WTSSBX_SESSION_STATE_DISCONNECTED = 2
def _define_WTSSBX_SESSION_INFO_head():
    class WTSSBX_SESSION_INFO(Structure):
        pass
    return WTSSBX_SESSION_INFO
def _define_WTSSBX_SESSION_INFO():
    WTSSBX_SESSION_INFO = win32more.System.RemoteDesktop.WTSSBX_SESSION_INFO_head
    WTSSBX_SESSION_INFO._fields_ = [
        ("wszUserName", Char * 105),
        ("wszDomainName", Char * 257),
        ("ApplicationType", Char * 257),
        ("dwSessionId", UInt32),
        ("CreateTime", win32more.Foundation.FILETIME),
        ("DisconnectTime", win32more.Foundation.FILETIME),
        ("SessionState", win32more.System.RemoteDesktop.WTSSBX_SESSION_STATE),
    ]
    return WTSSBX_SESSION_INFO
WTSSBX_NOTIFICATION_TYPE = Int32
WTSSBX_NOTIFICATION_REMOVED = 1
WTSSBX_NOTIFICATION_CHANGED = 2
WTSSBX_NOTIFICATION_ADDED = 4
WTSSBX_NOTIFICATION_RESYNC = 8
def _define_IWTSSBPlugin_head():
    class IWTSSBPlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc44be78-b18d-4399-b210-641bf67a002c')
    return IWTSSBPlugin
def _define_IWTSSBPlugin():
    IWTSSBPlugin = win32more.System.RemoteDesktop.IWTSSBPlugin_head
    IWTSSBPlugin.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'Initialize', ((1, 'PluginCapabilities'),)))
    IWTSSBPlugin.WTSSBX_MachineChangeNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE,Int32,POINTER(win32more.System.RemoteDesktop.WTSSBX_MACHINE_INFO_head), use_last_error=False)(4, 'WTSSBX_MachineChangeNotification', ((1, 'NotificationType'),(1, 'MachineId'),(1, 'pMachineInfo'),)))
    IWTSSBPlugin.WTSSBX_SessionChangeNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.WTSSBX_NOTIFICATION_TYPE,Int32,UInt32,POINTER(win32more.System.RemoteDesktop.WTSSBX_SESSION_INFO), use_last_error=False)(5, 'WTSSBX_SessionChangeNotification', ((1, 'NotificationType'),(1, 'MachineId'),(1, 'NumOfSessions'),(1, 'SessionInfo'),)))
    IWTSSBPlugin.WTSSBX_GetMostSuitableServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(6, 'WTSSBX_GetMostSuitableServer', ((1, 'UserName'),(1, 'DomainName'),(1, 'ApplicationType'),(1, 'FarmName'),(1, 'pMachineId'),)))
    IWTSSBPlugin.Terminated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Terminated', ()))
    IWTSSBPlugin.WTSSBX_GetUserExternalSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTSSBX_IP_ADDRESS_head),POINTER(UInt32),POINTER(win32more.System.RemoteDesktop.WTSSBX_MACHINE_CONNECT_INFO_head), use_last_error=False)(8, 'WTSSBX_GetUserExternalSession', ((1, 'UserName'),(1, 'DomainName'),(1, 'ApplicationType'),(1, 'RedirectorInternalIP'),(1, 'pSessionId'),(1, 'pMachineConnectInfo'),)))
    return IWTSSBPlugin
def _define_CHANNEL_DEF_head():
    class CHANNEL_DEF(Structure):
        pass
    return CHANNEL_DEF
def _define_CHANNEL_DEF():
    CHANNEL_DEF = win32more.System.RemoteDesktop.CHANNEL_DEF_head
    CHANNEL_DEF._pack_ = 1
    CHANNEL_DEF._fields_ = [
        ("name", win32more.Foundation.CHAR * 8),
        ("options", UInt32),
    ]
    return CHANNEL_DEF
def _define_CHANNEL_PDU_HEADER_head():
    class CHANNEL_PDU_HEADER(Structure):
        pass
    return CHANNEL_PDU_HEADER
def _define_CHANNEL_PDU_HEADER():
    CHANNEL_PDU_HEADER = win32more.System.RemoteDesktop.CHANNEL_PDU_HEADER_head
    CHANNEL_PDU_HEADER._fields_ = [
        ("length", UInt32),
        ("flags", UInt32),
    ]
    return CHANNEL_PDU_HEADER
def _define_PCHANNEL_INIT_EVENT_FN():
    return CFUNCTYPE(Void,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)
def _define_PCHANNEL_OPEN_EVENT_FN():
    return CFUNCTYPE(Void,UInt32,UInt32,c_void_p,UInt32,UInt32,UInt32, use_last_error=False)
def _define_PVIRTUALCHANNELINIT():
    return CFUNCTYPE(UInt32,POINTER(c_void_p),POINTER(win32more.System.RemoteDesktop.CHANNEL_DEF_head),Int32,UInt32,win32more.System.RemoteDesktop.PCHANNEL_INIT_EVENT_FN, use_last_error=False)
def _define_PVIRTUALCHANNELOPEN():
    return CFUNCTYPE(UInt32,c_void_p,POINTER(UInt32),win32more.Foundation.PSTR,win32more.System.RemoteDesktop.PCHANNEL_OPEN_EVENT_FN, use_last_error=False)
def _define_PVIRTUALCHANNELCLOSE():
    return CFUNCTYPE(UInt32,UInt32, use_last_error=False)
def _define_PVIRTUALCHANNELWRITE():
    return CFUNCTYPE(UInt32,UInt32,c_void_p,UInt32,c_void_p, use_last_error=False)
def _define_CHANNEL_ENTRY_POINTS_head():
    class CHANNEL_ENTRY_POINTS(Structure):
        pass
    return CHANNEL_ENTRY_POINTS
def _define_CHANNEL_ENTRY_POINTS():
    CHANNEL_ENTRY_POINTS = win32more.System.RemoteDesktop.CHANNEL_ENTRY_POINTS_head
    CHANNEL_ENTRY_POINTS._fields_ = [
        ("cbSize", UInt32),
        ("protocolVersion", UInt32),
        ("pVirtualChannelInit", win32more.System.RemoteDesktop.PVIRTUALCHANNELINIT),
        ("pVirtualChannelOpen", win32more.System.RemoteDesktop.PVIRTUALCHANNELOPEN),
        ("pVirtualChannelClose", win32more.System.RemoteDesktop.PVIRTUALCHANNELCLOSE),
        ("pVirtualChannelWrite", win32more.System.RemoteDesktop.PVIRTUALCHANNELWRITE),
    ]
    return CHANNEL_ENTRY_POINTS
def _define_PVIRTUALCHANNELENTRY():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.RemoteDesktop.CHANNEL_ENTRY_POINTS_head), use_last_error=False)
Workspace = Guid('4f1dfca6-3aad-48e1-8406-4bc21a501d7c')
def _define_IWorkspaceClientExt_head():
    class IWorkspaceClientExt(win32more.System.Com.IUnknown_head):
        Guid = Guid('12b952f4-41ca-4f21-a829-a6d07d9a16e5')
    return IWorkspaceClientExt
def _define_IWorkspaceClientExt():
    IWorkspaceClientExt = win32more.System.RemoteDesktop.IWorkspaceClientExt_head
    IWorkspaceClientExt.GetResourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetResourceId', ((1, 'bstrWorkspaceId'),)))
    IWorkspaceClientExt.GetResourceDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetResourceDisplayName', ((1, 'bstrWorkspaceDisplayName'),)))
    IWorkspaceClientExt.IssueDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'IssueDisconnect', ()))
    return IWorkspaceClientExt
def _define_IWorkspace_head():
    class IWorkspace(win32more.System.Com.IUnknown_head):
        Guid = Guid('b922bbb8-4c55-4fea-8496-beb0b44285e5')
    return IWorkspace
def _define_IWorkspace():
    IWorkspace = win32more.System.RemoteDesktop.IWorkspace_head
    IWorkspace.GetWorkspaceNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetWorkspaceNames', ((1, 'psaWkspNames'),)))
    IWorkspace.StartRemoteApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(4, 'StartRemoteApplication', ((1, 'bstrWorkspaceId'),(1, 'psaParams'),)))
    IWorkspace.GetProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetProcessId', ((1, 'pulProcessId'),)))
    return IWorkspace
def _define_IWorkspace2_head():
    class IWorkspace2(win32more.System.RemoteDesktop.IWorkspace_head):
        Guid = Guid('96d8d7cf-783e-4286-834c-ebc0e95f783c')
    return IWorkspace2
def _define_IWorkspace2():
    IWorkspace2 = win32more.System.RemoteDesktop.IWorkspace2_head
    IWorkspace2.StartRemoteApplicationEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,win32more.Foundation.BSTR,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(6, 'StartRemoteApplicationEx', ((1, 'bstrWorkspaceId'),(1, 'bstrRequestingAppId'),(1, 'bstrRequestingAppFamilyName'),(1, 'bLaunchIntoImmersiveClient'),(1, 'bstrImmersiveClientActivationContext'),(1, 'psaParams'),)))
    return IWorkspace2
def _define_IWorkspace3_head():
    class IWorkspace3(win32more.System.RemoteDesktop.IWorkspace2_head):
        Guid = Guid('1becbe4a-d654-423b-afeb-be8d532c13c6')
    return IWorkspace3
def _define_IWorkspace3():
    IWorkspace3 = win32more.System.RemoteDesktop.IWorkspace3_head
    IWorkspace3.GetClaimsToken2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,UInt32,win32more.Foundation.RECT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetClaimsToken2', ((1, 'bstrClaimsHint'),(1, 'bstrUserHint'),(1, 'claimCookie'),(1, 'hwndCredUiParent'),(1, 'rectCredUiParent'),(1, 'pbstrAccessToken'),)))
    IWorkspace3.SetClaimsToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt64,win32more.Foundation.BSTR, use_last_error=False)(8, 'SetClaimsToken', ((1, 'bstrAccessToken'),(1, 'ullAccessTokenExpiration'),(1, 'bstrRefreshToken'),)))
    return IWorkspace3
def _define_IWorkspaceRegistration_head():
    class IWorkspaceRegistration(win32more.System.Com.IUnknown_head):
        Guid = Guid('b922bbb8-4c55-4fea-8496-beb0b44285e6')
    return IWorkspaceRegistration
def _define_IWorkspaceRegistration():
    IWorkspaceRegistration = win32more.System.RemoteDesktop.IWorkspaceRegistration_head
    IWorkspaceRegistration.AddResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWorkspaceClientExt_head,POINTER(UInt32), use_last_error=False)(3, 'AddResource', ((1, 'pUnk'),(1, 'pdwCookie'),)))
    IWorkspaceRegistration.RemoveResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'RemoveResource', ((1, 'dwCookieConnection'),)))
    return IWorkspaceRegistration
def _define_IWorkspaceRegistration2_head():
    class IWorkspaceRegistration2(win32more.System.RemoteDesktop.IWorkspaceRegistration_head):
        Guid = Guid('cf59f654-39bb-44d8-94d0-4635728957e9')
    return IWorkspaceRegistration2
def _define_IWorkspaceRegistration2():
    IWorkspaceRegistration2 = win32more.System.RemoteDesktop.IWorkspaceRegistration2_head
    IWorkspaceRegistration2.AddResourceEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWorkspaceClientExt_head,win32more.Foundation.BSTR,POINTER(UInt32),Guid, use_last_error=False)(5, 'AddResourceEx', ((1, 'pUnk'),(1, 'bstrEventLogUploadAddress'),(1, 'pdwCookie'),(1, 'correlationId'),)))
    IWorkspaceRegistration2.RemoveResourceEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Guid, use_last_error=False)(6, 'RemoveResourceEx', ((1, 'dwCookieConnection'),(1, 'correlationId'),)))
    return IWorkspaceRegistration2
def _define_IWorkspaceScriptable_head():
    class IWorkspaceScriptable(win32more.System.Com.IDispatch_head):
        Guid = Guid('efea49a2-dda5-429d-8f42-b23b92c4c347')
    return IWorkspaceScriptable
def _define_IWorkspaceScriptable():
    IWorkspaceScriptable = win32more.System.RemoteDesktop.IWorkspaceScriptable_head
    IWorkspaceScriptable.DisconnectWorkspace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'DisconnectWorkspace', ((1, 'bstrWorkspaceId'),)))
    IWorkspaceScriptable.StartWorkspace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,Int32, use_last_error=False)(8, 'StartWorkspace', ((1, 'bstrWorkspaceId'),(1, 'bstrUserName'),(1, 'bstrPassword'),(1, 'bstrWorkspaceParams'),(1, 'lTimeout'),(1, 'lFlags'),)))
    IWorkspaceScriptable.IsWorkspaceCredentialSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(Int16), use_last_error=False)(9, 'IsWorkspaceCredentialSpecified', ((1, 'bstrWorkspaceId'),(1, 'bCountUnauthenticatedCredentials'),(1, 'pbCredExist'),)))
    IWorkspaceScriptable.IsWorkspaceSSOEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'IsWorkspaceSSOEnabled', ((1, 'pbSSOEnabled'),)))
    IWorkspaceScriptable.ClearWorkspaceCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'ClearWorkspaceCredential', ((1, 'bstrWorkspaceId'),)))
    IWorkspaceScriptable.OnAuthenticated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(12, 'OnAuthenticated', ((1, 'bstrWorkspaceId'),(1, 'bstrUserName'),)))
    IWorkspaceScriptable.DisconnectWorkspaceByFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'DisconnectWorkspaceByFriendlyName', ((1, 'bstrWorkspaceFriendlyName'),)))
    return IWorkspaceScriptable
def _define_IWorkspaceScriptable2_head():
    class IWorkspaceScriptable2(win32more.System.RemoteDesktop.IWorkspaceScriptable_head):
        Guid = Guid('efea49a2-dda5-429d-8f42-b33ba2c4c348')
    return IWorkspaceScriptable2
def _define_IWorkspaceScriptable2():
    IWorkspaceScriptable2 = win32more.System.RemoteDesktop.IWorkspaceScriptable2_head
    IWorkspaceScriptable2.StartWorkspaceEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,Int32, use_last_error=False)(14, 'StartWorkspaceEx', ((1, 'bstrWorkspaceId'),(1, 'bstrWorkspaceFriendlyName'),(1, 'bstrRedirectorName'),(1, 'bstrUserName'),(1, 'bstrPassword'),(1, 'bstrAppContainer'),(1, 'bstrWorkspaceParams'),(1, 'lTimeout'),(1, 'lFlags'),)))
    IWorkspaceScriptable2.ResourceDismissed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(15, 'ResourceDismissed', ((1, 'bstrWorkspaceId'),(1, 'bstrWorkspaceFriendlyName'),)))
    return IWorkspaceScriptable2
def _define_IWorkspaceScriptable3_head():
    class IWorkspaceScriptable3(win32more.System.RemoteDesktop.IWorkspaceScriptable2_head):
        Guid = Guid('531e6512-2cbf-4bd2-80a5-d90a71636a9a')
    return IWorkspaceScriptable3
def _define_IWorkspaceScriptable3():
    IWorkspaceScriptable3 = win32more.System.RemoteDesktop.IWorkspaceScriptable3_head
    IWorkspaceScriptable3.StartWorkspaceEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,Int32,win32more.Foundation.BSTR,Guid, use_last_error=False)(16, 'StartWorkspaceEx2', ((1, 'bstrWorkspaceId'),(1, 'bstrWorkspaceFriendlyName'),(1, 'bstrRedirectorName'),(1, 'bstrUserName'),(1, 'bstrPassword'),(1, 'bstrAppContainer'),(1, 'bstrWorkspaceParams'),(1, 'lTimeout'),(1, 'lFlags'),(1, 'bstrEventLogUploadAddress'),(1, 'correlationId'),)))
    return IWorkspaceScriptable3
def _define_IWorkspaceReportMessage_head():
    class IWorkspaceReportMessage(win32more.System.Com.IUnknown_head):
        Guid = Guid('a7c06739-500f-4e8c-99a8-2bd6955899eb')
    return IWorkspaceReportMessage
def _define_IWorkspaceReportMessage():
    IWorkspaceReportMessage = win32more.System.RemoteDesktop.IWorkspaceReportMessage_head
    IWorkspaceReportMessage.RegisterErrorLogMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(3, 'RegisterErrorLogMessage', ((1, 'bstrMessage'),)))
    IWorkspaceReportMessage.IsErrorMessageRegistered = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,win32more.Foundation.BSTR,UInt32,POINTER(Int16), use_last_error=False)(4, 'IsErrorMessageRegistered', ((1, 'bstrWkspId'),(1, 'dwErrorType'),(1, 'bstrErrorMessageType'),(1, 'dwErrorCode'),(1, 'pfErrorExist'),)))
    IWorkspaceReportMessage.RegisterErrorEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,win32more.Foundation.BSTR,UInt32, use_last_error=False)(5, 'RegisterErrorEvent', ((1, 'bstrWkspId'),(1, 'dwErrorType'),(1, 'bstrErrorMessageType'),(1, 'dwErrorCode'),)))
    return IWorkspaceReportMessage
def _define__ITSWkspEvents_head():
    class _ITSWkspEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('b922bbb8-4c55-4fea-8496-beb0b44285e9')
    return _ITSWkspEvents
def _define__ITSWkspEvents():
    _ITSWkspEvents = win32more.System.RemoteDesktop._ITSWkspEvents_head
    return _ITSWkspEvents
TSSD_AddrV46Type = Int32
TSSD_ADDR_UNDEFINED = 0
TSSD_ADDR_IPv4 = 4
TSSD_ADDR_IPv6 = 6
TSSB_NOTIFICATION_TYPE = Int32
TSSB_NOTIFY_INVALID = 0
TSSB_NOTIFY_TARGET_CHANGE = 1
TSSB_NOTIFY_SESSION_CHANGE = 2
TSSB_NOTIFY_CONNECTION_REQUEST_CHANGE = 4
TARGET_STATE = Int32
TARGET_UNKNOWN = 1
TARGET_INITIALIZING = 2
TARGET_RUNNING = 3
TARGET_DOWN = 4
TARGET_HIBERNATED = 5
TARGET_CHECKED_OUT = 6
TARGET_STOPPED = 7
TARGET_INVALID = 8
TARGET_STARTING = 9
TARGET_STOPPING = 10
TARGET_MAXSTATE = 11
TARGET_CHANGE_TYPE = Int32
TARGET_CHANGE_UNSPEC = 1
TARGET_EXTERNALIP_CHANGED = 2
TARGET_INTERNALIP_CHANGED = 4
TARGET_JOINED = 8
TARGET_REMOVED = 16
TARGET_STATE_CHANGED = 32
TARGET_IDLE = 64
TARGET_PENDING = 128
TARGET_INUSE = 256
TARGET_PATCH_STATE_CHANGED = 512
TARGET_FARM_MEMBERSHIP_CHANGED = 1024
TARGET_TYPE = Int32
UNKNOWN = 0
FARM = 1
NONFARM = 2
TARGET_PATCH_STATE = Int32
TARGET_PATCH_UNKNOWN = 0
TARGET_PATCH_NOT_STARTED = 1
TARGET_PATCH_IN_PROGRESS = 2
TARGET_PATCH_COMPLETED = 3
TARGET_PATCH_FAILED = 4
CLIENT_MESSAGE_TYPE = Int32
CLIENT_MESSAGE_CONNECTION_INVALID = 0
CLIENT_MESSAGE_CONNECTION_STATUS = 1
CLIENT_MESSAGE_CONNECTION_ERROR = 2
CONNECTION_CHANGE_NOTIFICATION = Int32
CONNECTION_REQUEST_INVALID = 0
CONNECTION_REQUEST_PENDING = 1
CONNECTION_REQUEST_FAILED = 2
CONNECTION_REQUEST_TIMEDOUT = 3
CONNECTION_REQUEST_SUCCEEDED = 4
CONNECTION_REQUEST_CANCELLED = 5
CONNECTION_REQUEST_LB_COMPLETED = 6
CONNECTION_REQUEST_QUERY_PL_COMPLETED = 7
CONNECTION_REQUEST_ORCH_COMPLETED = 8
RD_FARM_TYPE = Int32
RD_FARM_RDSH = 0
RD_FARM_TEMP_VM = 1
RD_FARM_MANUAL_PERSONAL_VM = 2
RD_FARM_AUTO_PERSONAL_VM = 3
RD_FARM_MANUAL_PERSONAL_RDSH = 4
RD_FARM_AUTO_PERSONAL_RDSH = 5
RD_FARM_TYPE_UNKNOWN = -1
PLUGIN_TYPE = Int32
UNKNOWN_PLUGIN = 0
POLICY_PLUGIN = 1
RESOURCE_PLUGIN = 2
LOAD_BALANCING_PLUGIN = 4
PLACEMENT_PLUGIN = 8
ORCHESTRATION_PLUGIN = 16
PROVISIONING_PLUGIN = 32
TASK_PLUGIN = 64
TSSESSION_STATE = Int32
STATE_INVALID = -1
STATE_ACTIVE = 0
STATE_CONNECTED = 1
STATE_CONNECTQUERY = 2
STATE_SHADOW = 3
STATE_DISCONNECTED = 4
STATE_IDLE = 5
STATE_LISTEN = 6
STATE_RESET = 7
STATE_DOWN = 8
STATE_INIT = 9
STATE_MAX = 10
TARGET_OWNER = Int32
OWNER_UNKNOWN = 0
OWNER_MS_TS_PLUGIN = 1
OWNER_MS_VM_PLUGIN = 2
def _define_CLIENT_DISPLAY_head():
    class CLIENT_DISPLAY(Structure):
        pass
    return CLIENT_DISPLAY
def _define_CLIENT_DISPLAY():
    CLIENT_DISPLAY = win32more.System.RemoteDesktop.CLIENT_DISPLAY_head
    CLIENT_DISPLAY._fields_ = [
        ("HorizontalResolution", UInt32),
        ("VerticalResolution", UInt32),
        ("ColorDepth", UInt32),
    ]
    return CLIENT_DISPLAY
def _define_TSSD_ConnectionPoint_head():
    class TSSD_ConnectionPoint(Structure):
        pass
    return TSSD_ConnectionPoint
def _define_TSSD_ConnectionPoint():
    TSSD_ConnectionPoint = win32more.System.RemoteDesktop.TSSD_ConnectionPoint_head
    TSSD_ConnectionPoint._fields_ = [
        ("ServerAddressB", Byte * 16),
        ("AddressType", win32more.System.RemoteDesktop.TSSD_AddrV46Type),
        ("PortNumber", UInt16),
        ("AddressScope", UInt32),
    ]
    return TSSD_ConnectionPoint
VM_NOTIFY_STATUS = Int32
VM_NOTIFY_STATUS_PENDING = 0
VM_NOTIFY_STATUS_IN_PROGRESS = 1
VM_NOTIFY_STATUS_COMPLETE = 2
VM_NOTIFY_STATUS_FAILED = 3
VM_NOTIFY_STATUS_CANCELED = 4
def _define_VM_NOTIFY_ENTRY_head():
    class VM_NOTIFY_ENTRY(Structure):
        pass
    return VM_NOTIFY_ENTRY
def _define_VM_NOTIFY_ENTRY():
    VM_NOTIFY_ENTRY = win32more.System.RemoteDesktop.VM_NOTIFY_ENTRY_head
    VM_NOTIFY_ENTRY._fields_ = [
        ("VmName", Char * 128),
        ("VmHost", Char * 128),
    ]
    return VM_NOTIFY_ENTRY
def _define_VM_PATCH_INFO_head():
    class VM_PATCH_INFO(Structure):
        pass
    return VM_PATCH_INFO
def _define_VM_PATCH_INFO():
    VM_PATCH_INFO = win32more.System.RemoteDesktop.VM_PATCH_INFO_head
    VM_PATCH_INFO._fields_ = [
        ("dwNumEntries", UInt32),
        ("pVmNames", POINTER(win32more.Foundation.PWSTR)),
    ]
    return VM_PATCH_INFO
def _define_VM_NOTIFY_INFO_head():
    class VM_NOTIFY_INFO(Structure):
        pass
    return VM_NOTIFY_INFO
def _define_VM_NOTIFY_INFO():
    VM_NOTIFY_INFO = win32more.System.RemoteDesktop.VM_NOTIFY_INFO_head
    VM_NOTIFY_INFO._fields_ = [
        ("dwNumEntries", UInt32),
        ("ppVmEntries", POINTER(POINTER(win32more.System.RemoteDesktop.VM_NOTIFY_ENTRY_head))),
    ]
    return VM_NOTIFY_INFO
VM_HOST_NOTIFY_STATUS = Int32
VM_HOST_STATUS_INIT_PENDING = 0
VM_HOST_STATUS_INIT_IN_PROGRESS = 1
VM_HOST_STATUS_INIT_COMPLETE = 2
VM_HOST_STATUS_INIT_FAILED = 3
RDV_TASK_STATUS = Int32
RDV_TASK_STATUS_UNKNOWN = 0
RDV_TASK_STATUS_SEARCHING = 1
RDV_TASK_STATUS_DOWNLOADING = 2
RDV_TASK_STATUS_APPLYING = 3
RDV_TASK_STATUS_REBOOTING = 4
RDV_TASK_STATUS_REBOOTED = 5
RDV_TASK_STATUS_SUCCESS = 6
RDV_TASK_STATUS_FAILED = 7
RDV_TASK_STATUS_TIMEOUT = 8
TS_SB_SORT_BY = Int32
TS_SB_SORT_BY_NONE = 0
TS_SB_SORT_BY_NAME = 1
TS_SB_SORT_BY_PROP = 2
def _define_ITsSbPlugin_head():
    class ITsSbPlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('48cd7406-caab-465f-a5d6-baa863b9ea4f')
    return ITsSbPlugin
def _define_ITsSbPlugin():
    ITsSbPlugin = win32more.System.RemoteDesktop.ITsSbPlugin_head
    ITsSbPlugin.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbProvider_head,win32more.System.RemoteDesktop.ITsSbPluginNotifySink_head,win32more.System.RemoteDesktop.ITsSbPluginPropertySet_head, use_last_error=False)(3, 'Initialize', ((1, 'pProvider'),(1, 'pNotifySink'),(1, 'pPropertySet'),)))
    ITsSbPlugin.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'Terminate', ((1, 'hr'),)))
    return ITsSbPlugin
def _define_ITsSbResourcePlugin_head():
    class ITsSbResourcePlugin(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('ea8db42c-98ed-4535-a88b-2a164f35490f')
    return ITsSbResourcePlugin
def _define_ITsSbResourcePlugin():
    ITsSbResourcePlugin = win32more.System.RemoteDesktop.ITsSbResourcePlugin_head
    return ITsSbResourcePlugin
def _define_ITsSbServiceNotification_head():
    class ITsSbServiceNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('86cb68ae-86e0-4f57-8a64-bb7406bc5550')
    return ITsSbServiceNotification
def _define_ITsSbServiceNotification():
    ITsSbServiceNotification = win32more.System.RemoteDesktop.ITsSbServiceNotification_head
    ITsSbServiceNotification.NotifyServiceFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'NotifyServiceFailure', ()))
    ITsSbServiceNotification.NotifyServiceSuccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'NotifyServiceSuccess', ()))
    return ITsSbServiceNotification
def _define_ITsSbLoadBalancing_head():
    class ITsSbLoadBalancing(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('24329274-9eb7-11dc-ae98-f2b456d89593')
    return ITsSbLoadBalancing
def _define_ITsSbLoadBalancing():
    ITsSbLoadBalancing = win32more.System.RemoteDesktop.ITsSbLoadBalancing_head
    ITsSbLoadBalancing.GetMostSuitableTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbClientConnection_head,win32more.System.RemoteDesktop.ITsSbLoadBalancingNotifySink_head, use_last_error=False)(5, 'GetMostSuitableTarget', ((1, 'pConnection'),(1, 'pLBSink'),)))
    return ITsSbLoadBalancing
def _define_ITsSbPlacement_head():
    class ITsSbPlacement(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('daadee5f-6d32-480e-9e36-ddab2329f06d')
    return ITsSbPlacement
def _define_ITsSbPlacement():
    ITsSbPlacement = win32more.System.RemoteDesktop.ITsSbPlacement_head
    ITsSbPlacement.QueryEnvironmentForTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbClientConnection_head,win32more.System.RemoteDesktop.ITsSbPlacementNotifySink_head, use_last_error=False)(5, 'QueryEnvironmentForTarget', ((1, 'pConnection'),(1, 'pPlacementSink'),)))
    return ITsSbPlacement
def _define_ITsSbOrchestration_head():
    class ITsSbOrchestration(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('64fc1172-9eb7-11dc-8b00-3aba56d89593')
    return ITsSbOrchestration
def _define_ITsSbOrchestration():
    ITsSbOrchestration = win32more.System.RemoteDesktop.ITsSbOrchestration_head
    ITsSbOrchestration.PrepareTargetForConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbClientConnection_head,win32more.System.RemoteDesktop.ITsSbOrchestrationNotifySink_head, use_last_error=False)(5, 'PrepareTargetForConnect', ((1, 'pConnection'),(1, 'pOrchestrationNotifySink'),)))
    return ITsSbOrchestration
def _define_ITsSbEnvironment_head():
    class ITsSbEnvironment(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c87f7f7-bf51-4a5c-87bf-8e94fb6e2256')
    return ITsSbEnvironment
def _define_ITsSbEnvironment():
    ITsSbEnvironment = win32more.System.RemoteDesktop.ITsSbEnvironment_head
    ITsSbEnvironment.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Name', ((1, 'pVal'),)))
    ITsSbEnvironment.get_ServerWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'get_ServerWeight', ((1, 'pVal'),)))
    ITsSbEnvironment.get_EnvironmentPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head), use_last_error=False)(5, 'get_EnvironmentPropertySet', ((1, 'ppPropertySet'),)))
    ITsSbEnvironment.put_EnvironmentPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head, use_last_error=False)(6, 'put_EnvironmentPropertySet', ((1, 'pVal'),)))
    return ITsSbEnvironment
def _define_ITsSbLoadBalanceResult_head():
    class ITsSbLoadBalanceResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('24fdb7ac-fea6-11dc-9672-9a8956d89593')
    return ITsSbLoadBalanceResult
def _define_ITsSbLoadBalanceResult():
    ITsSbLoadBalanceResult = win32more.System.RemoteDesktop.ITsSbLoadBalanceResult_head
    ITsSbLoadBalanceResult.get_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_TargetName', ((1, 'pVal'),)))
    return ITsSbLoadBalanceResult
def _define_ITsSbTarget_head():
    class ITsSbTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('16616ecc-272d-411d-b324-126893033856')
    return ITsSbTarget
def _define_ITsSbTarget():
    ITsSbTarget = win32more.System.RemoteDesktop.ITsSbTarget_head
    ITsSbTarget.get_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_TargetName', ((1, 'pVal'),)))
    ITsSbTarget.put_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'put_TargetName', ((1, 'Val'),)))
    ITsSbTarget.get_FarmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_FarmName', ((1, 'pVal'),)))
    ITsSbTarget.put_FarmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(6, 'put_FarmName', ((1, 'Val'),)))
    ITsSbTarget.get_TargetFQDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_TargetFQDN', ((1, 'TargetFqdnName'),)))
    ITsSbTarget.put_TargetFQDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_TargetFQDN', ((1, 'Val'),)))
    ITsSbTarget.get_TargetNetbios = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_TargetNetbios', ((1, 'TargetNetbiosName'),)))
    ITsSbTarget.put_TargetNetbios = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_TargetNetbios', ((1, 'Val'),)))
    ITsSbTarget.get_IpAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.TSSD_ConnectionPoint),POINTER(UInt32), use_last_error=False)(11, 'get_IpAddresses', ((1, 'SOCKADDR'),(1, 'numAddresses'),)))
    ITsSbTarget.put_IpAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.TSSD_ConnectionPoint),UInt32, use_last_error=False)(12, 'put_IpAddresses', ((1, 'SOCKADDR'),(1, 'numAddresses'),)))
    ITsSbTarget.get_TargetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.TARGET_STATE), use_last_error=False)(13, 'get_TargetState', ((1, 'pState'),)))
    ITsSbTarget.put_TargetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.TARGET_STATE, use_last_error=False)(14, 'put_TargetState', ((1, 'State'),)))
    ITsSbTarget.get_TargetPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbTargetPropertySet_head), use_last_error=False)(15, 'get_TargetPropertySet', ((1, 'ppPropertySet'),)))
    ITsSbTarget.put_TargetPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTargetPropertySet_head, use_last_error=False)(16, 'put_TargetPropertySet', ((1, 'pVal'),)))
    ITsSbTarget.get_EnvironmentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_EnvironmentName', ((1, 'pVal'),)))
    ITsSbTarget.put_EnvironmentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_EnvironmentName', ((1, 'Val'),)))
    ITsSbTarget.get_NumSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'get_NumSessions', ((1, 'pNumSessions'),)))
    ITsSbTarget.get_NumPendingConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(20, 'get_NumPendingConnections', ((1, 'pNumPendingConnections'),)))
    ITsSbTarget.get_TargetLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(21, 'get_TargetLoad', ((1, 'pTargetLoad'),)))
    return ITsSbTarget
def _define_ITsSbSession_head():
    class ITsSbSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('d453aac7-b1d8-4c5e-ba34-9afb4c8c5510')
    return ITsSbSession
def _define_ITsSbSession():
    ITsSbSession = win32more.System.RemoteDesktop.ITsSbSession_head
    ITsSbSession.get_SessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'get_SessionId', ((1, 'pVal'),)))
    ITsSbSession.get_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_TargetName', ((1, 'targetName'),)))
    ITsSbSession.put_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(5, 'put_TargetName', ((1, 'targetName'),)))
    ITsSbSession.get_Username = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_Username', ((1, 'userName'),)))
    ITsSbSession.get_Domain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Domain', ((1, 'domain'),)))
    ITsSbSession.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.TSSESSION_STATE), use_last_error=False)(8, 'get_State', ((1, 'pState'),)))
    ITsSbSession.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.TSSESSION_STATE, use_last_error=False)(9, 'put_State', ((1, 'State'),)))
    ITsSbSession.get_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(10, 'get_CreateTime', ((1, 'pTime'),)))
    ITsSbSession.put_CreateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.FILETIME, use_last_error=False)(11, 'put_CreateTime', ((1, 'Time'),)))
    ITsSbSession.get_DisconnectTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(12, 'get_DisconnectTime', ((1, 'pTime'),)))
    ITsSbSession.put_DisconnectTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.FILETIME, use_last_error=False)(13, 'put_DisconnectTime', ((1, 'Time'),)))
    ITsSbSession.get_InitialProgram = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_InitialProgram', ((1, 'app'),)))
    ITsSbSession.put_InitialProgram = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_InitialProgram', ((1, 'Application'),)))
    ITsSbSession.get_ClientDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.CLIENT_DISPLAY_head), use_last_error=False)(16, 'get_ClientDisplay', ((1, 'pClientDisplay'),)))
    ITsSbSession.put_ClientDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.CLIENT_DISPLAY, use_last_error=False)(17, 'put_ClientDisplay', ((1, 'pClientDisplay'),)))
    ITsSbSession.get_ProtocolType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(18, 'get_ProtocolType', ((1, 'pVal'),)))
    ITsSbSession.put_ProtocolType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(19, 'put_ProtocolType', ((1, 'Val'),)))
    return ITsSbSession
def _define_ITsSbResourceNotification_head():
    class ITsSbResourceNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('65d3e85a-c39b-11dc-b92d-3cd255d89593')
    return ITsSbResourceNotification
def _define_ITsSbResourceNotification():
    ITsSbResourceNotification = win32more.System.RemoteDesktop.ITsSbResourceNotification_head
    ITsSbResourceNotification.NotifySessionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.TSSESSION_STATE,win32more.System.RemoteDesktop.ITsSbSession_head, use_last_error=False)(3, 'NotifySessionChange', ((1, 'changeType'),(1, 'pSession'),)))
    ITsSbResourceNotification.NotifyTargetChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.RemoteDesktop.ITsSbTarget_head, use_last_error=False)(4, 'NotifyTargetChange', ((1, 'TargetChangeType'),(1, 'pTarget'),)))
    ITsSbResourceNotification.NotifyClientConnectionStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION,win32more.System.RemoteDesktop.ITsSbClientConnection_head, use_last_error=False)(5, 'NotifyClientConnectionStateChange', ((1, 'ChangeType'),(1, 'pConnection'),)))
    return ITsSbResourceNotification
def _define_ITsSbResourceNotificationEx_head():
    class ITsSbResourceNotificationEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8a47fde-ca91-44d2-b897-3aa28a43b2b7')
    return ITsSbResourceNotificationEx
def _define_ITsSbResourceNotificationEx():
    ITsSbResourceNotificationEx = win32more.System.RemoteDesktop.ITsSbResourceNotificationEx_head
    ITsSbResourceNotificationEx.NotifySessionChangeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,win32more.System.RemoteDesktop.TSSESSION_STATE, use_last_error=False)(3, 'NotifySessionChangeEx', ((1, 'targetName'),(1, 'userName'),(1, 'domain'),(1, 'sessionId'),(1, 'sessionState'),)))
    ITsSbResourceNotificationEx.NotifyTargetChangeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32, use_last_error=False)(4, 'NotifyTargetChangeEx', ((1, 'targetName'),(1, 'targetChangeType'),)))
    ITsSbResourceNotificationEx.NotifyClientConnectionStateChangeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.CONNECTION_CHANGE_NOTIFICATION, use_last_error=False)(5, 'NotifyClientConnectionStateChangeEx', ((1, 'userName'),(1, 'domain'),(1, 'initialProgram'),(1, 'poolName'),(1, 'targetName'),(1, 'connectionChangeType'),)))
    return ITsSbResourceNotificationEx
def _define_ITsSbTaskInfo_head():
    class ITsSbTaskInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('523d1083-89be-48dd-99ea-04e82ffa7265')
    return ITsSbTaskInfo
def _define_ITsSbTaskInfo():
    ITsSbTaskInfo = win32more.System.RemoteDesktop.ITsSbTaskInfo_head
    ITsSbTaskInfo.get_TargetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_TargetId', ((1, 'pName'),)))
    ITsSbTaskInfo.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(4, 'get_StartTime', ((1, 'pStartTime'),)))
    ITsSbTaskInfo.get_EndTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(5, 'get_EndTime', ((1, 'pEndTime'),)))
    ITsSbTaskInfo.get_Deadline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(6, 'get_Deadline', ((1, 'pDeadline'),)))
    ITsSbTaskInfo.get_Identifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Identifier', ((1, 'pIdentifier'),)))
    ITsSbTaskInfo.get_Label = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Label', ((1, 'pLabel'),)))
    ITsSbTaskInfo.get_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(9, 'get_Context', ((1, 'pContext'),)))
    ITsSbTaskInfo.get_Plugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Plugin', ((1, 'pPlugin'),)))
    ITsSbTaskInfo.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.RDV_TASK_STATUS), use_last_error=False)(11, 'get_Status', ((1, 'pStatus'),)))
    return ITsSbTaskInfo
def _define_ITsSbTaskPlugin_head():
    class ITsSbTaskPlugin(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('fa22ef0f-8705-41be-93bc-44bdbcf1c9c4')
    return ITsSbTaskPlugin
def _define_ITsSbTaskPlugin():
    ITsSbTaskPlugin = win32more.System.RemoteDesktop.ITsSbTaskPlugin_head
    ITsSbTaskPlugin.InitializeTaskPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTaskPluginNotifySink_head, use_last_error=False)(5, 'InitializeTaskPlugin', ((1, 'pITsSbTaskPluginNotifySink'),)))
    ITsSbTaskPlugin.SetTaskQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.RemoteDesktop.ITsSbTaskInfo_head), use_last_error=False)(6, 'SetTaskQueue', ((1, 'pszHostName'),(1, 'SbTaskInfoSize'),(1, 'pITsSbTaskInfo'),)))
    return ITsSbTaskPlugin
def _define_ITsSbPropertySet_head():
    class ITsSbPropertySet(win32more.System.Com.StructuredStorage.IPropertyBag_head):
        Guid = Guid('5c025171-bb1e-4baf-a212-6d5e9774b33b')
    return ITsSbPropertySet
def _define_ITsSbPropertySet():
    ITsSbPropertySet = win32more.System.RemoteDesktop.ITsSbPropertySet_head
    return ITsSbPropertySet
def _define_ITsSbPluginPropertySet_head():
    class ITsSbPluginPropertySet(win32more.System.RemoteDesktop.ITsSbPropertySet_head):
        Guid = Guid('95006e34-7eff-4b6c-bb40-49a4fda7cea6')
    return ITsSbPluginPropertySet
def _define_ITsSbPluginPropertySet():
    ITsSbPluginPropertySet = win32more.System.RemoteDesktop.ITsSbPluginPropertySet_head
    return ITsSbPluginPropertySet
def _define_ITsSbClientConnectionPropertySet_head():
    class ITsSbClientConnectionPropertySet(win32more.System.RemoteDesktop.ITsSbPropertySet_head):
        Guid = Guid('e51995b0-46d6-11dd-aa21-cedc55d89593')
    return ITsSbClientConnectionPropertySet
def _define_ITsSbClientConnectionPropertySet():
    ITsSbClientConnectionPropertySet = win32more.System.RemoteDesktop.ITsSbClientConnectionPropertySet_head
    return ITsSbClientConnectionPropertySet
def _define_ITsSbTargetPropertySet_head():
    class ITsSbTargetPropertySet(win32more.System.RemoteDesktop.ITsSbPropertySet_head):
        Guid = Guid('f7bda5d6-994c-4e11-a079-2763b61830ac')
    return ITsSbTargetPropertySet
def _define_ITsSbTargetPropertySet():
    ITsSbTargetPropertySet = win32more.System.RemoteDesktop.ITsSbTargetPropertySet_head
    return ITsSbTargetPropertySet
def _define_ITsSbEnvironmentPropertySet_head():
    class ITsSbEnvironmentPropertySet(win32more.System.RemoteDesktop.ITsSbPropertySet_head):
        Guid = Guid('d0d1bf7e-7acf-11dd-a243-e51156d89593')
    return ITsSbEnvironmentPropertySet
def _define_ITsSbEnvironmentPropertySet():
    ITsSbEnvironmentPropertySet = win32more.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head
    return ITsSbEnvironmentPropertySet
def _define_ITsSbBaseNotifySink_head():
    class ITsSbBaseNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('808a6537-1282-4989-9e09-f43938b71722')
    return ITsSbBaseNotifySink
def _define_ITsSbBaseNotifySink():
    ITsSbBaseNotifySink = win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head
    ITsSbBaseNotifySink.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnError', ((1, 'hrError'),)))
    ITsSbBaseNotifySink.OnReportStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.CLIENT_MESSAGE_TYPE,UInt32, use_last_error=False)(4, 'OnReportStatus', ((1, 'messageType'),(1, 'messageID'),)))
    return ITsSbBaseNotifySink
def _define_ITsSbPluginNotifySink_head():
    class ITsSbPluginNotifySink(win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head):
        Guid = Guid('44dfe30b-c3be-40f5-bf82-7a95bb795adf')
    return ITsSbPluginNotifySink
def _define_ITsSbPluginNotifySink():
    ITsSbPluginNotifySink = win32more.System.RemoteDesktop.ITsSbPluginNotifySink_head
    ITsSbPluginNotifySink.OnInitialized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(5, 'OnInitialized', ((1, 'hr'),)))
    ITsSbPluginNotifySink.OnTerminated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnTerminated', ()))
    return ITsSbPluginNotifySink
def _define_ITsSbLoadBalancingNotifySink_head():
    class ITsSbLoadBalancingNotifySink(win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head):
        Guid = Guid('5f8a8297-3244-4e6a-958a-27c822c1e141')
    return ITsSbLoadBalancingNotifySink
def _define_ITsSbLoadBalancingNotifySink():
    ITsSbLoadBalancingNotifySink = win32more.System.RemoteDesktop.ITsSbLoadBalancingNotifySink_head
    ITsSbLoadBalancingNotifySink.OnGetMostSuitableTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbLoadBalanceResult_head,win32more.Foundation.BOOL, use_last_error=False)(5, 'OnGetMostSuitableTarget', ((1, 'pLBResult'),(1, 'fIsNewConnection'),)))
    return ITsSbLoadBalancingNotifySink
def _define_ITsSbPlacementNotifySink_head():
    class ITsSbPlacementNotifySink(win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head):
        Guid = Guid('68a0c487-2b4f-46c2-94a1-6ce685183634')
    return ITsSbPlacementNotifySink
def _define_ITsSbPlacementNotifySink():
    ITsSbPlacementNotifySink = win32more.System.RemoteDesktop.ITsSbPlacementNotifySink_head
    ITsSbPlacementNotifySink.OnQueryEnvironmentCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbEnvironment_head, use_last_error=False)(5, 'OnQueryEnvironmentCompleted', ((1, 'pEnvironment'),)))
    return ITsSbPlacementNotifySink
def _define_ITsSbOrchestrationNotifySink_head():
    class ITsSbOrchestrationNotifySink(win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head):
        Guid = Guid('36c37d61-926b-442f-bca5-118c6d50dcf2')
    return ITsSbOrchestrationNotifySink
def _define_ITsSbOrchestrationNotifySink():
    ITsSbOrchestrationNotifySink = win32more.System.RemoteDesktop.ITsSbOrchestrationNotifySink_head
    ITsSbOrchestrationNotifySink.OnReadyToConnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTarget_head, use_last_error=False)(5, 'OnReadyToConnect', ((1, 'pTarget'),)))
    return ITsSbOrchestrationNotifySink
def _define_ITsSbTaskPluginNotifySink_head():
    class ITsSbTaskPluginNotifySink(win32more.System.RemoteDesktop.ITsSbBaseNotifySink_head):
        Guid = Guid('6aaf899e-c2ec-45ee-aa37-45e60895261a')
    return ITsSbTaskPluginNotifySink
def _define_ITsSbTaskPluginNotifySink():
    ITsSbTaskPluginNotifySink = win32more.System.RemoteDesktop.ITsSbTaskPluginNotifySink_head
    ITsSbTaskPluginNotifySink.OnSetTaskTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.FILETIME,win32more.Foundation.FILETIME,win32more.Foundation.FILETIME,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(5, 'OnSetTaskTime', ((1, 'szTargetName'),(1, 'TaskStartTime'),(1, 'TaskEndTime'),(1, 'TaskDeadline'),(1, 'szTaskLabel'),(1, 'szTaskIdentifier'),(1, 'szTaskPlugin'),(1, 'dwTaskStatus'),(1, 'saContext'),)))
    ITsSbTaskPluginNotifySink.OnDeleteTaskTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(6, 'OnDeleteTaskTime', ((1, 'szTargetName'),(1, 'szTaskIdentifier'),)))
    ITsSbTaskPluginNotifySink.OnUpdateTaskStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.RDV_TASK_STATUS, use_last_error=False)(7, 'OnUpdateTaskStatus', ((1, 'szTargetName'),(1, 'TaskIdentifier'),(1, 'TaskStatus'),)))
    ITsSbTaskPluginNotifySink.OnReportTasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'OnReportTasks', ((1, 'szHostName'),)))
    return ITsSbTaskPluginNotifySink
def _define_ITsSbClientConnection_head():
    class ITsSbClientConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('18857499-ad61-4b1b-b7df-cbcd41fb8338')
    return ITsSbClientConnection
def _define_ITsSbClientConnection():
    ITsSbClientConnection = win32more.System.RemoteDesktop.ITsSbClientConnection_head
    ITsSbClientConnection.get_UserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_UserName', ((1, 'pVal'),)))
    ITsSbClientConnection.get_Domain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_Domain', ((1, 'pVal'),)))
    ITsSbClientConnection.get_InitialProgram = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_InitialProgram', ((1, 'pVal'),)))
    ITsSbClientConnection.get_LoadBalanceResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbLoadBalanceResult_head), use_last_error=False)(6, 'get_LoadBalanceResult', ((1, 'ppVal'),)))
    ITsSbClientConnection.get_FarmName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_FarmName', ((1, 'pVal'),)))
    ITsSbClientConnection.PutContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'PutContext', ((1, 'contextId'),(1, 'context'),(1, 'existingContext'),)))
    ITsSbClientConnection.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetContext', ((1, 'contextId'),(1, 'context'),)))
    ITsSbClientConnection.get_Environment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbEnvironment_head), use_last_error=False)(10, 'get_Environment', ((1, 'ppEnvironment'),)))
    ITsSbClientConnection.get_ConnectionError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'get_ConnectionError', ()))
    ITsSbClientConnection.get_SamUserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_SamUserAccount', ((1, 'pVal'),)))
    ITsSbClientConnection.get_ClientConnectionPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbClientConnectionPropertySet_head), use_last_error=False)(13, 'get_ClientConnectionPropertySet', ((1, 'ppPropertySet'),)))
    ITsSbClientConnection.get_IsFirstAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'get_IsFirstAssignment', ((1, 'ppVal'),)))
    ITsSbClientConnection.get_RdFarmType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.RD_FARM_TYPE), use_last_error=False)(15, 'get_RdFarmType', ((1, 'pRdFarmType'),)))
    ITsSbClientConnection.get_UserSidString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(SByte)), use_last_error=False)(16, 'get_UserSidString', ((1, 'pszUserSidString'),)))
    ITsSbClientConnection.GetDisconnectedSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbSession_head), use_last_error=False)(17, 'GetDisconnectedSession', ((1, 'ppSession'),)))
    return ITsSbClientConnection
def _define_ITsSbProvider_head():
    class ITsSbProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('87a4098f-6d7b-44dd-bc17-8ce44e370d52')
    return ITsSbProvider
def _define_ITsSbProvider():
    ITsSbProvider = win32more.System.RemoteDesktop.ITsSbProvider_head
    ITsSbProvider.CreateTargetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbTarget_head), use_last_error=False)(3, 'CreateTargetObject', ((1, 'TargetName'),(1, 'EnvironmentName'),(1, 'ppTarget'),)))
    ITsSbProvider.CreateLoadBalanceResultObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbLoadBalanceResult_head), use_last_error=False)(4, 'CreateLoadBalanceResultObject', ((1, 'TargetName'),(1, 'ppLBResult'),)))
    ITsSbProvider.CreateSessionObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.RemoteDesktop.ITsSbSession_head), use_last_error=False)(5, 'CreateSessionObject', ((1, 'TargetName'),(1, 'UserName'),(1, 'Domain'),(1, 'SessionId'),(1, 'ppSession'),)))
    ITsSbProvider.CreatePluginPropertySet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbPluginPropertySet_head), use_last_error=False)(6, 'CreatePluginPropertySet', ((1, 'ppPropertySet'),)))
    ITsSbProvider.CreateTargetPropertySetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbTargetPropertySet_head), use_last_error=False)(7, 'CreateTargetPropertySetObject', ((1, 'ppPropertySet'),)))
    ITsSbProvider.CreateEnvironmentObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.RemoteDesktop.ITsSbEnvironment_head), use_last_error=False)(8, 'CreateEnvironmentObject', ((1, 'Name'),(1, 'ServerWeight'),(1, 'ppEnvironment'),)))
    ITsSbProvider.GetResourcePluginStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbResourcePluginStore_head), use_last_error=False)(9, 'GetResourcePluginStore', ((1, 'ppStore'),)))
    ITsSbProvider.GetFilterPluginStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbFilterPluginStore_head), use_last_error=False)(10, 'GetFilterPluginStore', ((1, 'ppStore'),)))
    ITsSbProvider.RegisterForNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.ITsSbResourceNotification_head, use_last_error=False)(11, 'RegisterForNotification', ((1, 'notificationType'),(1, 'ResourceToMonitor'),(1, 'pPluginNotification'),)))
    ITsSbProvider.UnRegisterForNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR, use_last_error=False)(12, 'UnRegisterForNotification', ((1, 'notificationType'),(1, 'ResourceToMonitor'),)))
    ITsSbProvider.GetInstanceOfGlobalStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbGlobalStore_head), use_last_error=False)(13, 'GetInstanceOfGlobalStore', ((1, 'ppGlobalStore'),)))
    ITsSbProvider.CreateEnvironmentPropertySetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbEnvironmentPropertySet_head), use_last_error=False)(14, 'CreateEnvironmentPropertySetObject', ((1, 'ppPropertySet'),)))
    return ITsSbProvider
def _define_ITsSbResourcePluginStore_head():
    class ITsSbResourcePluginStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('5c38f65f-bcf1-4036-a6bf-9e3cccae0b63')
    return ITsSbResourcePluginStore
def _define_ITsSbResourcePluginStore():
    ITsSbResourcePluginStore = win32more.System.RemoteDesktop.ITsSbResourcePluginStore_head
    ITsSbResourcePluginStore.QueryTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbTarget_head), use_last_error=False)(3, 'QueryTarget', ((1, 'TargetName'),(1, 'FarmName'),(1, 'ppTarget'),)))
    ITsSbResourcePluginStore.QuerySessionBySessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbSession_head), use_last_error=False)(4, 'QuerySessionBySessionId', ((1, 'dwSessionId'),(1, 'TargetName'),(1, 'ppSession'),)))
    ITsSbResourcePluginStore.AddTargetToStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTarget_head, use_last_error=False)(5, 'AddTargetToStore', ((1, 'pTarget'),)))
    ITsSbResourcePluginStore.AddSessionToStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbSession_head, use_last_error=False)(6, 'AddSessionToStore', ((1, 'pSession'),)))
    ITsSbResourcePluginStore.AddEnvironmentToStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbEnvironment_head, use_last_error=False)(7, 'AddEnvironmentToStore', ((1, 'pEnvironment'),)))
    ITsSbResourcePluginStore.RemoveEnvironmentFromStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL, use_last_error=False)(8, 'RemoveEnvironmentFromStore', ((1, 'EnvironmentName'),(1, 'bIgnoreOwner'),)))
    ITsSbResourcePluginStore.EnumerateFarms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(9, 'EnumerateFarms', ((1, 'pdwCount'),(1, 'pVal'),)))
    ITsSbResourcePluginStore.QueryEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbEnvironment_head), use_last_error=False)(10, 'QueryEnvironment', ((1, 'EnvironmentName'),(1, 'ppEnvironment'),)))
    ITsSbResourcePluginStore.EnumerateEnvironments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbEnvironment_head)), use_last_error=False)(11, 'EnumerateEnvironments', ((1, 'pdwCount'),(1, 'pVal'),)))
    ITsSbResourcePluginStore.SaveTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTarget_head,win32more.Foundation.BOOL, use_last_error=False)(12, 'SaveTarget', ((1, 'pTarget'),(1, 'bForceWrite'),)))
    ITsSbResourcePluginStore.SaveEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbEnvironment_head,win32more.Foundation.BOOL, use_last_error=False)(13, 'SaveEnvironment', ((1, 'pEnvironment'),(1, 'bForceWrite'),)))
    ITsSbResourcePluginStore.SaveSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbSession_head, use_last_error=False)(14, 'SaveSession', ((1, 'pSession'),)))
    ITsSbResourcePluginStore.SetTargetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'SetTargetProperty', ((1, 'TargetName'),(1, 'PropertyName'),(1, 'pProperty'),)))
    ITsSbResourcePluginStore.SetEnvironmentProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'SetEnvironmentProperty', ((1, 'EnvironmentName'),(1, 'PropertyName'),(1, 'pProperty'),)))
    ITsSbResourcePluginStore.SetTargetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.TARGET_STATE,POINTER(win32more.System.RemoteDesktop.TARGET_STATE), use_last_error=False)(17, 'SetTargetState', ((1, 'targetName'),(1, 'newState'),(1, 'pOldState'),)))
    ITsSbResourcePluginStore.SetSessionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbSession_head, use_last_error=False)(18, 'SetSessionState', ((1, 'sbSession'),)))
    ITsSbResourcePluginStore.EnumerateTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.TS_SB_SORT_BY,win32more.Foundation.BSTR,POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbTarget_head)), use_last_error=False)(19, 'EnumerateTargets', ((1, 'FarmName'),(1, 'EnvName'),(1, 'sortByFieldId'),(1, 'sortyByPropName'),(1, 'pdwCount'),(1, 'pVal'),)))
    ITsSbResourcePluginStore.EnumerateSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.TSSESSION_STATE),POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbSession_head)), use_last_error=False)(20, 'EnumerateSessions', ((1, 'targetName'),(1, 'userName'),(1, 'userDomain'),(1, 'poolName'),(1, 'initialProgram'),(1, 'pSessionState'),(1, 'pdwCount'),(1, 'ppVal'),)))
    ITsSbResourcePluginStore.GetFarmProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(21, 'GetFarmProperty', ((1, 'farmName'),(1, 'propertyName'),(1, 'pVarValue'),)))
    ITsSbResourcePluginStore.DeleteTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(22, 'DeleteTarget', ((1, 'targetName'),(1, 'hostName'),)))
    ITsSbResourcePluginStore.SetTargetPropertyWithVersionCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbTarget_head,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(23, 'SetTargetPropertyWithVersionCheck', ((1, 'pTarget'),(1, 'PropertyName'),(1, 'pProperty'),)))
    ITsSbResourcePluginStore.SetEnvironmentPropertyWithVersionCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbEnvironment_head,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'SetEnvironmentPropertyWithVersionCheck', ((1, 'pEnvironment'),(1, 'PropertyName'),(1, 'pProperty'),)))
    ITsSbResourcePluginStore.AcquireTargetLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(25, 'AcquireTargetLock', ((1, 'targetName'),(1, 'dwTimeout'),(1, 'ppContext'),)))
    ITsSbResourcePluginStore.ReleaseTargetLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(26, 'ReleaseTargetLock', ((1, 'pContext'),)))
    ITsSbResourcePluginStore.TestAndSetServerState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.TARGET_STATE,win32more.System.RemoteDesktop.TARGET_STATE,POINTER(win32more.System.RemoteDesktop.TARGET_STATE), use_last_error=False)(27, 'TestAndSetServerState', ((1, 'PoolName'),(1, 'ServerFQDN'),(1, 'NewState'),(1, 'TestState'),(1, 'pInitState'),)))
    ITsSbResourcePluginStore.SetServerWaitingToStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(28, 'SetServerWaitingToStart', ((1, 'PoolName'),(1, 'serverName'),)))
    ITsSbResourcePluginStore.GetServerState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.TARGET_STATE), use_last_error=False)(29, 'GetServerState', ((1, 'PoolName'),(1, 'ServerFQDN'),(1, 'pState'),)))
    ITsSbResourcePluginStore.SetServerDrainMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32, use_last_error=False)(30, 'SetServerDrainMode', ((1, 'ServerFQDN'),(1, 'DrainMode'),)))
    return ITsSbResourcePluginStore
def _define_ITsSbFilterPluginStore_head():
    class ITsSbFilterPluginStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('85b44b0f-ed78-413f-9702-fa6d3b5ee755')
    return ITsSbFilterPluginStore
def _define_ITsSbFilterPluginStore():
    ITsSbFilterPluginStore = win32more.System.RemoteDesktop.ITsSbFilterPluginStore_head
    ITsSbFilterPluginStore.SaveProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.ITsSbPropertySet_head, use_last_error=False)(3, 'SaveProperties', ((1, 'pPropertySet'),)))
    ITsSbFilterPluginStore.EnumerateProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.ITsSbPropertySet_head), use_last_error=False)(4, 'EnumerateProperties', ((1, 'ppPropertySet'),)))
    ITsSbFilterPluginStore.DeleteProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(5, 'DeleteProperties', ((1, 'propertyName'),)))
    return ITsSbFilterPluginStore
def _define_ITsSbGlobalStore_head():
    class ITsSbGlobalStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ab60f7b-bd72-4d9f-8a3a-a0ea5574e635')
    return ITsSbGlobalStore
def _define_ITsSbGlobalStore():
    ITsSbGlobalStore = win32more.System.RemoteDesktop.ITsSbGlobalStore_head
    ITsSbGlobalStore.QueryTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbTarget_head), use_last_error=False)(3, 'QueryTarget', ((1, 'ProviderName'),(1, 'TargetName'),(1, 'FarmName'),(1, 'ppTarget'),)))
    ITsSbGlobalStore.QuerySessionBySessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.ITsSbSession_head), use_last_error=False)(4, 'QuerySessionBySessionId', ((1, 'ProviderName'),(1, 'dwSessionId'),(1, 'TargetName'),(1, 'ppSession'),)))
    ITsSbGlobalStore.EnumerateFarms = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'EnumerateFarms', ((1, 'ProviderName'),(1, 'pdwCount'),(1, 'pVal'),)))
    ITsSbGlobalStore.EnumerateTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbTarget_head)), use_last_error=False)(6, 'EnumerateTargets', ((1, 'ProviderName'),(1, 'FarmName'),(1, 'EnvName'),(1, 'pdwCount'),(1, 'pVal'),)))
    ITsSbGlobalStore.EnumerateEnvironmentsByProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbEnvironment_head)), use_last_error=False)(7, 'EnumerateEnvironmentsByProvider', ((1, 'ProviderName'),(1, 'pdwCount'),(1, 'ppVal'),)))
    ITsSbGlobalStore.EnumerateSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.RemoteDesktop.TSSESSION_STATE),POINTER(UInt32),POINTER(POINTER(win32more.System.RemoteDesktop.ITsSbSession_head)), use_last_error=False)(8, 'EnumerateSessions', ((1, 'ProviderName'),(1, 'targetName'),(1, 'userName'),(1, 'userDomain'),(1, 'poolName'),(1, 'initialProgram'),(1, 'pSessionState'),(1, 'pdwCount'),(1, 'ppVal'),)))
    ITsSbGlobalStore.GetFarmProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetFarmProperty', ((1, 'farmName'),(1, 'propertyName'),(1, 'pVarValue'),)))
    return ITsSbGlobalStore
def _define_ITsSbProvisioningPluginNotifySink_head():
    class ITsSbProvisioningPluginNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aca87a8e-818b-4581-a032-49c3dfb9c701')
    return ITsSbProvisioningPluginNotifySink
def _define_ITsSbProvisioningPluginNotifySink():
    ITsSbProvisioningPluginNotifySink = win32more.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head
    ITsSbProvisioningPluginNotifySink.OnJobCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.VM_NOTIFY_INFO_head), use_last_error=False)(3, 'OnJobCreated', ((1, 'pVmNotifyInfo'),)))
    ITsSbProvisioningPluginNotifySink.OnVirtualMachineStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.VM_NOTIFY_ENTRY_head),win32more.System.RemoteDesktop.VM_NOTIFY_STATUS,win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'OnVirtualMachineStatusChanged', ((1, 'pVmNotifyEntry'),(1, 'VmNotifyStatus'),(1, 'ErrorCode'),(1, 'ErrorDescr'),)))
    ITsSbProvisioningPluginNotifySink.OnJobCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(5, 'OnJobCompleted', ((1, 'ResultCode'),(1, 'ResultDescription'),)))
    ITsSbProvisioningPluginNotifySink.OnJobCancelled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnJobCancelled', ()))
    ITsSbProvisioningPluginNotifySink.LockVirtualMachine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.VM_NOTIFY_ENTRY_head), use_last_error=False)(7, 'LockVirtualMachine', ((1, 'pVmNotifyEntry'),)))
    ITsSbProvisioningPluginNotifySink.OnVirtualMachineHostStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.VM_HOST_NOTIFY_STATUS,win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'OnVirtualMachineHostStatusChanged', ((1, 'VmHost'),(1, 'VmHostNotifyStatus'),(1, 'ErrorCode'),(1, 'ErrorDescr'),)))
    return ITsSbProvisioningPluginNotifySink
def _define_ITsSbProvisioning_head():
    class ITsSbProvisioning(win32more.System.RemoteDesktop.ITsSbPlugin_head):
        Guid = Guid('2f6f0dbb-9e4f-462b-9c3f-fccc3dcb6232')
    return ITsSbProvisioning
def _define_ITsSbProvisioning():
    ITsSbProvisioning = win32more.System.RemoteDesktop.ITsSbProvisioning_head
    ITsSbProvisioning.CreateVirtualMachines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head, use_last_error=False)(5, 'CreateVirtualMachines', ((1, 'JobXmlString'),(1, 'JobGuid'),(1, 'pSink'),)))
    ITsSbProvisioning.PatchVirtualMachines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head,POINTER(win32more.System.RemoteDesktop.VM_PATCH_INFO_head), use_last_error=False)(6, 'PatchVirtualMachines', ((1, 'JobXmlString'),(1, 'JobGuid'),(1, 'pSink'),(1, 'pVMPatchInfo'),)))
    ITsSbProvisioning.DeleteVirtualMachines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.RemoteDesktop.ITsSbProvisioningPluginNotifySink_head, use_last_error=False)(7, 'DeleteVirtualMachines', ((1, 'JobXmlString'),(1, 'JobGuid'),(1, 'pSink'),)))
    ITsSbProvisioning.CancelJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'CancelJob', ((1, 'JobGuid'),)))
    return ITsSbProvisioning
def _define_ITsSbGenericNotifySink_head():
    class ITsSbGenericNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c4c8c4f-300b-46ad-9164-8468a7e7568c')
    return ITsSbGenericNotifySink
def _define_ITsSbGenericNotifySink():
    ITsSbGenericNotifySink = win32more.System.RemoteDesktop.ITsSbGenericNotifySink_head
    ITsSbGenericNotifySink.OnCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnCompleted', ((1, 'Status'),)))
    ITsSbGenericNotifySink.GetWaitTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(4, 'GetWaitTimeout', ((1, 'pftTimeout'),)))
    return ITsSbGenericNotifySink
def _define_pluginResource_head():
    class pluginResource(Structure):
        pass
    return pluginResource
def _define_pluginResource():
    pluginResource = win32more.System.RemoteDesktop.pluginResource_head
    pluginResource._fields_ = [
        ("alias", Char * 256),
        ("name", Char * 256),
        ("resourceFileContents", win32more.Foundation.PWSTR),
        ("fileExtension", Char * 256),
        ("resourcePluginType", Char * 256),
        ("isDiscoverable", Byte),
        ("resourceType", Int32),
        ("pceIconSize", UInt32),
        ("iconContents", c_char_p_no),
        ("pcePluginBlobSize", UInt32),
        ("blobContents", c_char_p_no),
    ]
    return pluginResource
def _define_ItsPubPlugin_head():
    class ItsPubPlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('70c04b05-f347-412b-822f-36c99c54ca45')
    return ItsPubPlugin
def _define_ItsPubPlugin():
    ItsPubPlugin = win32more.System.RemoteDesktop.ItsPubPlugin_head
    ItsPubPlugin.GetResourceList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32),POINTER(POINTER(win32more.System.RemoteDesktop.pluginResource_head)), use_last_error=False)(3, 'GetResourceList', ((1, 'userID'),(1, 'pceAppListSize'),(1, 'resourceList'),)))
    ItsPubPlugin.GetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.RemoteDesktop.pluginResource_head), use_last_error=False)(4, 'GetResource', ((1, 'alias'),(1, 'flags'),(1, 'resource'),)))
    ItsPubPlugin.GetCacheLastUpdateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetCacheLastUpdateTime', ((1, 'lastUpdateTime'),)))
    ItsPubPlugin.get_pluginName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_pluginName', ((1, 'pVal'),)))
    ItsPubPlugin.get_pluginVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_pluginVersion', ((1, 'pVal'),)))
    ItsPubPlugin.ResolveResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(8, 'ResolveResource', ((1, 'resourceType'),(1, 'resourceLocation'),(1, 'endPointName'),(1, 'userID'),(1, 'alias'),)))
    return ItsPubPlugin
def _define_pluginResource2FileAssociation_head():
    class pluginResource2FileAssociation(Structure):
        pass
    return pluginResource2FileAssociation
def _define_pluginResource2FileAssociation():
    pluginResource2FileAssociation = win32more.System.RemoteDesktop.pluginResource2FileAssociation_head
    pluginResource2FileAssociation._fields_ = [
        ("extName", Char * 256),
        ("primaryHandler", Byte),
        ("pceIconSize", UInt32),
        ("iconContents", c_char_p_no),
    ]
    return pluginResource2FileAssociation
def _define_pluginResource2_head():
    class pluginResource2(Structure):
        pass
    return pluginResource2
def _define_pluginResource2():
    pluginResource2 = win32more.System.RemoteDesktop.pluginResource2_head
    pluginResource2._fields_ = [
        ("resourceV1", win32more.System.RemoteDesktop.pluginResource),
        ("pceFileAssocListSize", UInt32),
        ("fileAssocList", POINTER(win32more.System.RemoteDesktop.pluginResource2FileAssociation_head)),
        ("securityDescriptor", win32more.Foundation.PWSTR),
        ("pceFolderListSize", UInt32),
        ("folderList", POINTER(POINTER(UInt16))),
    ]
    return pluginResource2
TSPUB_PLUGIN_PD_RESOLUTION_TYPE = Int32
TSPUB_PLUGIN_PD_QUERY_OR_CREATE = 0
TSPUB_PLUGIN_PD_QUERY_EXISTING = 1
TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE = Int32
TSPUB_PLUGIN_PD_ASSIGNMENT_NEW = 0
TSPUB_PLUGIN_PD_ASSIGNMENT_EXISTING = 1
def _define_ItsPubPlugin2_head():
    class ItsPubPlugin2(win32more.System.RemoteDesktop.ItsPubPlugin_head):
        Guid = Guid('fa4ce418-aad7-4ec6-bad1-0a321ba465d5')
    return ItsPubPlugin2
def _define_ItsPubPlugin2():
    ItsPubPlugin2 = win32more.System.RemoteDesktop.ItsPubPlugin2_head
    ItsPubPlugin2.GetResource2List = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32),POINTER(POINTER(win32more.System.RemoteDesktop.pluginResource2_head)), use_last_error=False)(9, 'GetResource2List', ((1, 'userID'),(1, 'pceAppListSize'),(1, 'resourceList'),)))
    ItsPubPlugin2.GetResource2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.RemoteDesktop.pluginResource2_head), use_last_error=False)(10, 'GetResource2', ((1, 'alias'),(1, 'flags'),(1, 'resource'),)))
    ItsPubPlugin2.ResolvePersonalDesktop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.RemoteDesktop.TSPUB_PLUGIN_PD_RESOLUTION_TYPE,POINTER(win32more.System.RemoteDesktop.TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE),win32more.Foundation.PWSTR, use_last_error=False)(11, 'ResolvePersonalDesktop', ((1, 'userId'),(1, 'poolId'),(1, 'ePdResolutionType'),(1, 'pPdAssignmentType'),(1, 'endPointName'),)))
    ItsPubPlugin2.DeletePersonalDesktopAssignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(12, 'DeletePersonalDesktopAssignment', ((1, 'userId'),(1, 'poolId'),(1, 'endpointName'),)))
    return ItsPubPlugin2
def _define_IWorkspaceResTypeRegistry_head():
    class IWorkspaceResTypeRegistry(win32more.System.Com.IDispatch_head):
        Guid = Guid('1d428c79-6e2e-4351-a361-c0401a03a0ba')
    return IWorkspaceResTypeRegistry
def _define_IWorkspaceResTypeRegistry():
    IWorkspaceResTypeRegistry = win32more.System.RemoteDesktop.IWorkspaceResTypeRegistry_head
    IWorkspaceResTypeRegistry.AddResourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'AddResourceType', ((1, 'fMachineWide'),(1, 'bstrFileExtension'),(1, 'bstrLauncher'),)))
    IWorkspaceResTypeRegistry.DeleteResourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.BSTR, use_last_error=False)(8, 'DeleteResourceType', ((1, 'fMachineWide'),(1, 'bstrFileExtension'),)))
    IWorkspaceResTypeRegistry.GetRegisteredFileExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(9, 'GetRegisteredFileExtensions', ((1, 'fMachineWide'),(1, 'psaFileExtensions'),)))
    IWorkspaceResTypeRegistry.GetResourceTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetResourceTypeInfo', ((1, 'fMachineWide'),(1, 'bstrFileExtension'),(1, 'pbstrLauncher'),)))
    IWorkspaceResTypeRegistry.ModifyResourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(11, 'ModifyResourceType', ((1, 'fMachineWide'),(1, 'bstrFileExtension'),(1, 'bstrLauncher'),)))
    return IWorkspaceResTypeRegistry
def _define_IWTSPlugin_head():
    class IWTSPlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230201-1439-4e62-a414-190d0ac3d40e')
    return IWTSPlugin
def _define_IWTSPlugin():
    IWTSPlugin = win32more.System.RemoteDesktop.IWTSPlugin_head
    IWTSPlugin.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWTSVirtualChannelManager_head, use_last_error=False)(3, 'Initialize', ((1, 'pChannelMgr'),)))
    IWTSPlugin.Connected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Connected', ()))
    IWTSPlugin.Disconnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Disconnected', ((1, 'dwDisconnectCode'),)))
    IWTSPlugin.Terminated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Terminated', ()))
    return IWTSPlugin
def _define_IWTSListener_head():
    class IWTSListener(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230206-9a39-4d58-8674-cdb4dff4e73b')
    return IWTSListener
def _define_IWTSListener():
    IWTSListener = win32more.System.RemoteDesktop.IWTSListener_head
    IWTSListener.GetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IPropertyBag_head), use_last_error=False)(3, 'GetConfiguration', ((1, 'ppPropertyBag'),)))
    return IWTSListener
def _define_IWTSListenerCallback_head():
    class IWTSListenerCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230203-d6a7-11d8-b9fd-000bdbd1f198')
    return IWTSListenerCallback
def _define_IWTSListenerCallback():
    IWTSListenerCallback = win32more.System.RemoteDesktop.IWTSListenerCallback_head
    IWTSListenerCallback.OnNewChannelConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWTSVirtualChannel_head,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL),POINTER(win32more.System.RemoteDesktop.IWTSVirtualChannelCallback_head), use_last_error=False)(3, 'OnNewChannelConnection', ((1, 'pChannel'),(1, 'data'),(1, 'pbAccept'),(1, 'ppCallback'),)))
    return IWTSListenerCallback
def _define_IWTSVirtualChannelCallback_head():
    class IWTSVirtualChannelCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230204-d6a7-11d8-b9fd-000bdbd1f198')
    return IWTSVirtualChannelCallback
def _define_IWTSVirtualChannelCallback():
    IWTSVirtualChannelCallback = win32more.System.RemoteDesktop.IWTSVirtualChannelCallback_head
    IWTSVirtualChannelCallback.OnDataReceived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte), use_last_error=False)(3, 'OnDataReceived', ((1, 'cbSize'),(1, 'pBuffer'),)))
    IWTSVirtualChannelCallback.OnClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnClose', ()))
    return IWTSVirtualChannelCallback
def _define_IWTSVirtualChannelManager_head():
    class IWTSVirtualChannelManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230205-d6a7-11d8-b9fd-000bdbd1f198')
    return IWTSVirtualChannelManager
def _define_IWTSVirtualChannelManager():
    IWTSVirtualChannelManager = win32more.System.RemoteDesktop.IWTSVirtualChannelManager_head
    IWTSVirtualChannelManager.CreateListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,win32more.System.RemoteDesktop.IWTSListenerCallback_head,POINTER(win32more.System.RemoteDesktop.IWTSListener_head), use_last_error=False)(3, 'CreateListener', ((1, 'pszChannelName'),(1, 'uFlags'),(1, 'pListenerCallback'),(1, 'ppListener'),)))
    return IWTSVirtualChannelManager
def _define_IWTSVirtualChannel_head():
    class IWTSVirtualChannel(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1230207-d6a7-11d8-b9fd-000bdbd1f198')
    return IWTSVirtualChannel
def _define_IWTSVirtualChannel():
    IWTSVirtualChannel = win32more.System.RemoteDesktop.IWTSVirtualChannel_head
    IWTSVirtualChannel.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Write', ((1, 'cbSize'),(1, 'pBuffer'),(1, 'pReserved'),)))
    IWTSVirtualChannel.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return IWTSVirtualChannel
def _define_IWTSPluginServiceProvider_head():
    class IWTSPluginServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3e07363-087c-476c-86a7-dbb15f46ddb4')
    return IWTSPluginServiceProvider
def _define_IWTSPluginServiceProvider():
    IWTSPluginServiceProvider = win32more.System.RemoteDesktop.IWTSPluginServiceProvider_head
    IWTSPluginServiceProvider.GetService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetService', ((1, 'ServiceId'),(1, 'ppunkObject'),)))
    return IWTSPluginServiceProvider
def _define_BITMAP_RENDERER_STATISTICS_head():
    class BITMAP_RENDERER_STATISTICS(Structure):
        pass
    return BITMAP_RENDERER_STATISTICS
def _define_BITMAP_RENDERER_STATISTICS():
    BITMAP_RENDERER_STATISTICS = win32more.System.RemoteDesktop.BITMAP_RENDERER_STATISTICS_head
    BITMAP_RENDERER_STATISTICS._fields_ = [
        ("dwFramesDelivered", UInt32),
        ("dwFramesDropped", UInt32),
    ]
    return BITMAP_RENDERER_STATISTICS
def _define_IWTSBitmapRenderer_head():
    class IWTSBitmapRenderer(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b7acc97-f3c9-46f7-8c5b-fa685d3441b1')
    return IWTSBitmapRenderer
def _define_IWTSBitmapRenderer():
    IWTSBitmapRenderer = win32more.System.RemoteDesktop.IWTSBitmapRenderer_head
    IWTSBitmapRenderer.Render = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,UInt32,Int32,UInt32,POINTER(Byte), use_last_error=False)(3, 'Render', ((1, 'imageFormat'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'cbStride'),(1, 'cbImageBuffer'),(1, 'pImageBuffer'),)))
    IWTSBitmapRenderer.GetRendererStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.BITMAP_RENDERER_STATISTICS_head), use_last_error=False)(4, 'GetRendererStatistics', ((1, 'pStatistics'),)))
    IWTSBitmapRenderer.RemoveMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'RemoveMapping', ()))
    return IWTSBitmapRenderer
def _define_IWTSBitmapRendererCallback_head():
    class IWTSBitmapRendererCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('d782928e-fe4e-4e77-ae90-9cd0b3e3b353')
    return IWTSBitmapRendererCallback
def _define_IWTSBitmapRendererCallback():
    IWTSBitmapRendererCallback = win32more.System.RemoteDesktop.IWTSBitmapRendererCallback_head
    IWTSBitmapRendererCallback.OnTargetSizeChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT, use_last_error=False)(3, 'OnTargetSizeChanged', ((1, 'rcNewSize'),)))
    return IWTSBitmapRendererCallback
def _define_IWTSBitmapRenderService_head():
    class IWTSBitmapRenderService(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea326091-05fe-40c1-b49c-3d2ef4626a0e')
    return IWTSBitmapRenderService
def _define_IWTSBitmapRenderService():
    IWTSBitmapRenderService = win32more.System.RemoteDesktop.IWTSBitmapRenderService_head
    IWTSBitmapRenderService.GetMappedRenderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.System.RemoteDesktop.IWTSBitmapRendererCallback_head,POINTER(win32more.System.RemoteDesktop.IWTSBitmapRenderer_head), use_last_error=False)(3, 'GetMappedRenderer', ((1, 'mappingId'),(1, 'pMappedRendererCallback'),(1, 'ppMappedRenderer'),)))
    return IWTSBitmapRenderService
def _define_IWRdsGraphicsChannelEvents_head():
    class IWRdsGraphicsChannelEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('67f2368c-d674-4fae-66a5-d20628a640d2')
    return IWRdsGraphicsChannelEvents
def _define_IWRdsGraphicsChannelEvents():
    IWRdsGraphicsChannelEvents = win32more.System.RemoteDesktop.IWRdsGraphicsChannelEvents_head
    IWRdsGraphicsChannelEvents.OnDataReceived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no, use_last_error=False)(3, 'OnDataReceived', ((1, 'cbSize'),(1, 'pBuffer'),)))
    IWRdsGraphicsChannelEvents.OnClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnClose', ()))
    IWRdsGraphicsChannelEvents.OnChannelOpened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'OnChannelOpened', ((1, 'OpenResult'),(1, 'pOpenContext'),)))
    IWRdsGraphicsChannelEvents.OnDataSent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,c_char_p_no,UInt32, use_last_error=False)(6, 'OnDataSent', ((1, 'pWriteContext'),(1, 'bCancelled'),(1, 'pBuffer'),(1, 'cbBuffer'),)))
    IWRdsGraphicsChannelEvents.OnMetricsUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt64, use_last_error=False)(7, 'OnMetricsUpdate', ((1, 'bandwidth'),(1, 'RTT'),(1, 'lastSentByteIndex'),)))
    return IWRdsGraphicsChannelEvents
def _define_IWRdsGraphicsChannel_head():
    class IWRdsGraphicsChannel(win32more.System.Com.IUnknown_head):
        Guid = Guid('684b7a0b-edff-43ad-d5a2-4a8d5388f401')
    return IWRdsGraphicsChannel
def _define_IWRdsGraphicsChannel():
    IWRdsGraphicsChannel = win32more.System.RemoteDesktop.IWRdsGraphicsChannel_head
    IWRdsGraphicsChannel.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Write', ((1, 'cbSize'),(1, 'pBuffer'),(1, 'pContext'),)))
    IWRdsGraphicsChannel.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IWRdsGraphicsChannel.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWRdsGraphicsChannelEvents_head,win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'Open', ((1, 'pChannelEvents'),(1, 'pOpenContext'),)))
    return IWRdsGraphicsChannel
WRdsGraphicsChannelType = Int32
WRdsGraphicsChannelType_GuaranteedDelivery = 0
WRdsGraphicsChannelType_BestEffortDelivery = 1
def _define_IWRdsGraphicsChannelManager_head():
    class IWRdsGraphicsChannelManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('0fd57159-e83e-476a-a8b9-4a7976e71e18')
    return IWRdsGraphicsChannelManager
def _define_IWRdsGraphicsChannelManager():
    IWRdsGraphicsChannelManager = win32more.System.RemoteDesktop.IWRdsGraphicsChannelManager_head
    IWRdsGraphicsChannelManager.CreateChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,win32more.System.RemoteDesktop.WRdsGraphicsChannelType,POINTER(win32more.System.RemoteDesktop.IWRdsGraphicsChannel_head), use_last_error=False)(3, 'CreateChannel', ((1, 'pszChannelName'),(1, 'channelType'),(1, 'ppVirtualChannel'),)))
    return IWRdsGraphicsChannelManager
def _define_RFX_GFX_RECT_head():
    class RFX_GFX_RECT(Structure):
        pass
    return RFX_GFX_RECT
def _define_RFX_GFX_RECT():
    RFX_GFX_RECT = win32more.System.RemoteDesktop.RFX_GFX_RECT_head
    RFX_GFX_RECT._pack_ = 1
    RFX_GFX_RECT._fields_ = [
        ("left", Int32),
        ("top", Int32),
        ("right", Int32),
        ("bottom", Int32),
    ]
    return RFX_GFX_RECT
def _define_RFX_GFX_MSG_HEADER_head():
    class RFX_GFX_MSG_HEADER(Structure):
        pass
    return RFX_GFX_MSG_HEADER
def _define_RFX_GFX_MSG_HEADER():
    RFX_GFX_MSG_HEADER = win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER_head
    RFX_GFX_MSG_HEADER._pack_ = 1
    RFX_GFX_MSG_HEADER._fields_ = [
        ("uMSGType", UInt16),
        ("cbSize", UInt16),
    ]
    return RFX_GFX_MSG_HEADER
def _define_RFX_GFX_MONITOR_INFO_head():
    class RFX_GFX_MONITOR_INFO(Structure):
        pass
    return RFX_GFX_MONITOR_INFO
def _define_RFX_GFX_MONITOR_INFO():
    RFX_GFX_MONITOR_INFO = win32more.System.RemoteDesktop.RFX_GFX_MONITOR_INFO_head
    RFX_GFX_MONITOR_INFO._pack_ = 1
    RFX_GFX_MONITOR_INFO._fields_ = [
        ("left", Int32),
        ("top", Int32),
        ("right", Int32),
        ("bottom", Int32),
        ("physicalWidth", UInt32),
        ("physicalHeight", UInt32),
        ("orientation", UInt32),
        ("primary", win32more.Foundation.BOOL),
    ]
    return RFX_GFX_MONITOR_INFO
def _define_RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST_head():
    class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST(Structure):
        pass
    return RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST
def _define_RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST():
    RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST = win32more.System.RemoteDesktop.RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST_head
    RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
    ]
    return RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST
def _define_RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE_head():
    class RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE(Structure):
        pass
    return RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE
def _define_RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE():
    RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE = win32more.System.RemoteDesktop.RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE_head
    RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE._pack_ = 1
    RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("reserved", UInt32),
        ("monitorCount", UInt32),
        ("MonitorData", win32more.System.RemoteDesktop.RFX_GFX_MONITOR_INFO * 16),
        ("clientUniqueId", Char * 32),
    ]
    return RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE
def _define_RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY_head():
    class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY(Structure):
        pass
    return RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY
def _define_RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY():
    RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY = win32more.System.RemoteDesktop.RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY_head
    RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY._pack_ = 1
    RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("ulWidth", UInt32),
        ("ulHeight", UInt32),
        ("ulBpp", UInt32),
        ("Reserved", UInt32),
    ]
    return RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY
def _define_RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM_head():
    class RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM(Structure):
        pass
    return RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM
def _define_RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM():
    RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM = win32more.System.RemoteDesktop.RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM_head
    RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
    ]
    return RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM
def _define_RFX_GFX_MSG_DESKTOP_INPUT_RESET_head():
    class RFX_GFX_MSG_DESKTOP_INPUT_RESET(Structure):
        pass
    return RFX_GFX_MSG_DESKTOP_INPUT_RESET
def _define_RFX_GFX_MSG_DESKTOP_INPUT_RESET():
    RFX_GFX_MSG_DESKTOP_INPUT_RESET = win32more.System.RemoteDesktop.RFX_GFX_MSG_DESKTOP_INPUT_RESET_head
    RFX_GFX_MSG_DESKTOP_INPUT_RESET._pack_ = 1
    RFX_GFX_MSG_DESKTOP_INPUT_RESET._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("ulWidth", UInt32),
        ("ulHeight", UInt32),
    ]
    return RFX_GFX_MSG_DESKTOP_INPUT_RESET
def _define_RFX_GFX_MSG_DISCONNECT_NOTIFY_head():
    class RFX_GFX_MSG_DISCONNECT_NOTIFY(Structure):
        pass
    return RFX_GFX_MSG_DISCONNECT_NOTIFY
def _define_RFX_GFX_MSG_DISCONNECT_NOTIFY():
    RFX_GFX_MSG_DISCONNECT_NOTIFY = win32more.System.RemoteDesktop.RFX_GFX_MSG_DISCONNECT_NOTIFY_head
    RFX_GFX_MSG_DISCONNECT_NOTIFY._pack_ = 1
    RFX_GFX_MSG_DISCONNECT_NOTIFY._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("DisconnectReason", UInt32),
    ]
    return RFX_GFX_MSG_DISCONNECT_NOTIFY
def _define_RFX_GFX_MSG_DESKTOP_RESEND_REQUEST_head():
    class RFX_GFX_MSG_DESKTOP_RESEND_REQUEST(Structure):
        pass
    return RFX_GFX_MSG_DESKTOP_RESEND_REQUEST
def _define_RFX_GFX_MSG_DESKTOP_RESEND_REQUEST():
    RFX_GFX_MSG_DESKTOP_RESEND_REQUEST = win32more.System.RemoteDesktop.RFX_GFX_MSG_DESKTOP_RESEND_REQUEST_head
    RFX_GFX_MSG_DESKTOP_RESEND_REQUEST._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("RedrawRect", win32more.System.RemoteDesktop.RFX_GFX_RECT),
    ]
    return RFX_GFX_MSG_DESKTOP_RESEND_REQUEST
def _define_RFX_GFX_MSG_RDP_DATA_head():
    class RFX_GFX_MSG_RDP_DATA(Structure):
        pass
    return RFX_GFX_MSG_RDP_DATA
def _define_RFX_GFX_MSG_RDP_DATA():
    RFX_GFX_MSG_RDP_DATA = win32more.System.RemoteDesktop.RFX_GFX_MSG_RDP_DATA_head
    RFX_GFX_MSG_RDP_DATA._fields_ = [
        ("channelHdr", win32more.System.RemoteDesktop.RFX_GFX_MSG_HEADER),
        ("rdpData", Byte * 0),
    ]
    return RFX_GFX_MSG_RDP_DATA
def _define_WTS_SOCKADDR_head():
    class WTS_SOCKADDR(Structure):
        pass
    return WTS_SOCKADDR
def _define_WTS_SOCKADDR():
    WTS_SOCKADDR = win32more.System.RemoteDesktop.WTS_SOCKADDR_head
    class WTS_SOCKADDR__u_e__Union(Union):
        pass
    class WTS_SOCKADDR__u_e__Union__ipv6_e__Struct(Structure):
        pass
    WTS_SOCKADDR__u_e__Union__ipv6_e__Struct._fields_ = [
        ("sin6_port", UInt16),
        ("sin6_flowinfo", UInt32),
        ("sin6_addr", UInt16 * 8),
        ("sin6_scope_id", UInt32),
    ]
    class WTS_SOCKADDR__u_e__Union__ipv4_e__Struct(Structure):
        pass
    WTS_SOCKADDR__u_e__Union__ipv4_e__Struct._fields_ = [
        ("sin_port", UInt16),
        ("IN_ADDR", UInt32),
        ("sin_zero", Byte * 8),
    ]
    WTS_SOCKADDR__u_e__Union._fields_ = [
        ("ipv4", WTS_SOCKADDR__u_e__Union__ipv4_e__Struct),
        ("ipv6", WTS_SOCKADDR__u_e__Union__ipv6_e__Struct),
    ]
    WTS_SOCKADDR._fields_ = [
        ("sin_family", UInt16),
        ("u", WTS_SOCKADDR__u_e__Union),
    ]
    return WTS_SOCKADDR
def _define_WTS_SMALL_RECT_head():
    class WTS_SMALL_RECT(Structure):
        pass
    return WTS_SMALL_RECT
def _define_WTS_SMALL_RECT():
    WTS_SMALL_RECT = win32more.System.RemoteDesktop.WTS_SMALL_RECT_head
    WTS_SMALL_RECT._fields_ = [
        ("Left", Int16),
        ("Top", Int16),
        ("Right", Int16),
        ("Bottom", Int16),
    ]
    return WTS_SMALL_RECT
WTS_RCM_SERVICE_STATE = Int32
WTS_SERVICE_NONE = 0
WTS_SERVICE_START = 1
WTS_SERVICE_STOP = 2
WTS_RCM_DRAIN_STATE = Int32
WTS_DRAIN_STATE_NONE = 0
WTS_DRAIN_IN_DRAIN = 1
WTS_DRAIN_NOT_IN_DRAIN = 2
def _define_WTS_SERVICE_STATE_head():
    class WTS_SERVICE_STATE(Structure):
        pass
    return WTS_SERVICE_STATE
def _define_WTS_SERVICE_STATE():
    WTS_SERVICE_STATE = win32more.System.RemoteDesktop.WTS_SERVICE_STATE_head
    WTS_SERVICE_STATE._fields_ = [
        ("RcmServiceState", win32more.System.RemoteDesktop.WTS_RCM_SERVICE_STATE),
        ("RcmDrainState", win32more.System.RemoteDesktop.WTS_RCM_DRAIN_STATE),
    ]
    return WTS_SERVICE_STATE
def _define_WTS_SESSION_ID_head():
    class WTS_SESSION_ID(Structure):
        pass
    return WTS_SESSION_ID
def _define_WTS_SESSION_ID():
    WTS_SESSION_ID = win32more.System.RemoteDesktop.WTS_SESSION_ID_head
    WTS_SESSION_ID._fields_ = [
        ("SessionUniqueGuid", Guid),
        ("SessionId", UInt32),
    ]
    return WTS_SESSION_ID
def _define_WTS_USER_CREDENTIAL_head():
    class WTS_USER_CREDENTIAL(Structure):
        pass
    return WTS_USER_CREDENTIAL
def _define_WTS_USER_CREDENTIAL():
    WTS_USER_CREDENTIAL = win32more.System.RemoteDesktop.WTS_USER_CREDENTIAL_head
    WTS_USER_CREDENTIAL._fields_ = [
        ("UserName", Char * 256),
        ("Password", Char * 256),
        ("Domain", Char * 256),
    ]
    return WTS_USER_CREDENTIAL
def _define_WTS_SYSTEMTIME_head():
    class WTS_SYSTEMTIME(Structure):
        pass
    return WTS_SYSTEMTIME
def _define_WTS_SYSTEMTIME():
    WTS_SYSTEMTIME = win32more.System.RemoteDesktop.WTS_SYSTEMTIME_head
    WTS_SYSTEMTIME._fields_ = [
        ("wYear", UInt16),
        ("wMonth", UInt16),
        ("wDayOfWeek", UInt16),
        ("wDay", UInt16),
        ("wHour", UInt16),
        ("wMinute", UInt16),
        ("wSecond", UInt16),
        ("wMilliseconds", UInt16),
    ]
    return WTS_SYSTEMTIME
def _define_WTS_TIME_ZONE_INFORMATION_head():
    class WTS_TIME_ZONE_INFORMATION(Structure):
        pass
    return WTS_TIME_ZONE_INFORMATION
def _define_WTS_TIME_ZONE_INFORMATION():
    WTS_TIME_ZONE_INFORMATION = win32more.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION_head
    WTS_TIME_ZONE_INFORMATION._fields_ = [
        ("Bias", Int32),
        ("StandardName", Char * 32),
        ("StandardDate", win32more.System.RemoteDesktop.WTS_SYSTEMTIME),
        ("StandardBias", Int32),
        ("DaylightName", Char * 32),
        ("DaylightDate", win32more.System.RemoteDesktop.WTS_SYSTEMTIME),
        ("DaylightBias", Int32),
    ]
    return WTS_TIME_ZONE_INFORMATION
def _define_WRDS_DYNAMIC_TIME_ZONE_INFORMATION_head():
    class WRDS_DYNAMIC_TIME_ZONE_INFORMATION(Structure):
        pass
    return WRDS_DYNAMIC_TIME_ZONE_INFORMATION
def _define_WRDS_DYNAMIC_TIME_ZONE_INFORMATION():
    WRDS_DYNAMIC_TIME_ZONE_INFORMATION = win32more.System.RemoteDesktop.WRDS_DYNAMIC_TIME_ZONE_INFORMATION_head
    WRDS_DYNAMIC_TIME_ZONE_INFORMATION._fields_ = [
        ("Bias", Int32),
        ("StandardName", Char * 32),
        ("StandardDate", win32more.System.RemoteDesktop.WTS_SYSTEMTIME),
        ("StandardBias", Int32),
        ("DaylightName", Char * 32),
        ("DaylightDate", win32more.System.RemoteDesktop.WTS_SYSTEMTIME),
        ("DaylightBias", Int32),
        ("TimeZoneKeyName", Char * 128),
        ("DynamicDaylightTimeDisabled", UInt16),
    ]
    return WRDS_DYNAMIC_TIME_ZONE_INFORMATION
def _define_WTS_CLIENT_DATA_head():
    class WTS_CLIENT_DATA(Structure):
        pass
    return WTS_CLIENT_DATA
def _define_WTS_CLIENT_DATA():
    WTS_CLIENT_DATA = win32more.System.RemoteDesktop.WTS_CLIENT_DATA_head
    WTS_CLIENT_DATA._fields_ = [
        ("fDisableCtrlAltDel", win32more.Foundation.BOOLEAN),
        ("fDoubleClickDetect", win32more.Foundation.BOOLEAN),
        ("fEnableWindowsKey", win32more.Foundation.BOOLEAN),
        ("fHideTitleBar", win32more.Foundation.BOOLEAN),
        ("fInheritAutoLogon", win32more.Foundation.BOOL),
        ("fPromptForPassword", win32more.Foundation.BOOLEAN),
        ("fUsingSavedCreds", win32more.Foundation.BOOLEAN),
        ("Domain", Char * 256),
        ("UserName", Char * 256),
        ("Password", Char * 256),
        ("fPasswordIsScPin", win32more.Foundation.BOOLEAN),
        ("fInheritInitialProgram", win32more.Foundation.BOOL),
        ("WorkDirectory", Char * 257),
        ("InitialProgram", Char * 257),
        ("fMaximizeShell", win32more.Foundation.BOOLEAN),
        ("EncryptionLevel", Byte),
        ("PerformanceFlags", UInt32),
        ("ProtocolName", Char * 9),
        ("ProtocolType", UInt16),
        ("fInheritColorDepth", win32more.Foundation.BOOL),
        ("HRes", UInt16),
        ("VRes", UInt16),
        ("ColorDepth", UInt16),
        ("DisplayDriverName", Char * 9),
        ("DisplayDeviceName", Char * 20),
        ("fMouse", win32more.Foundation.BOOLEAN),
        ("KeyboardLayout", UInt32),
        ("KeyboardType", UInt32),
        ("KeyboardSubType", UInt32),
        ("KeyboardFunctionKey", UInt32),
        ("imeFileName", Char * 33),
        ("ActiveInputLocale", UInt32),
        ("fNoAudioPlayback", win32more.Foundation.BOOLEAN),
        ("fRemoteConsoleAudio", win32more.Foundation.BOOLEAN),
        ("AudioDriverName", Char * 9),
        ("ClientTimeZone", win32more.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION),
        ("ClientName", Char * 21),
        ("SerialNumber", UInt32),
        ("ClientAddressFamily", UInt32),
        ("ClientAddress", Char * 31),
        ("ClientSockAddress", win32more.System.RemoteDesktop.WTS_SOCKADDR),
        ("ClientDirectory", Char * 257),
        ("ClientBuildNumber", UInt32),
        ("ClientProductId", UInt16),
        ("OutBufCountHost", UInt16),
        ("OutBufCountClient", UInt16),
        ("OutBufLength", UInt16),
        ("ClientSessionId", UInt32),
        ("ClientDigProductId", Char * 33),
        ("fDisableCpm", win32more.Foundation.BOOLEAN),
        ("fDisableCdm", win32more.Foundation.BOOLEAN),
        ("fDisableCcm", win32more.Foundation.BOOLEAN),
        ("fDisableLPT", win32more.Foundation.BOOLEAN),
        ("fDisableClip", win32more.Foundation.BOOLEAN),
        ("fDisablePNP", win32more.Foundation.BOOLEAN),
    ]
    return WTS_CLIENT_DATA
def _define_WTS_USER_DATA_head():
    class WTS_USER_DATA(Structure):
        pass
    return WTS_USER_DATA
def _define_WTS_USER_DATA():
    WTS_USER_DATA = win32more.System.RemoteDesktop.WTS_USER_DATA_head
    WTS_USER_DATA._fields_ = [
        ("WorkDirectory", Char * 257),
        ("InitialProgram", Char * 257),
        ("UserTimeZone", win32more.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION),
    ]
    return WTS_USER_DATA
def _define_WTS_POLICY_DATA_head():
    class WTS_POLICY_DATA(Structure):
        pass
    return WTS_POLICY_DATA
def _define_WTS_POLICY_DATA():
    WTS_POLICY_DATA = win32more.System.RemoteDesktop.WTS_POLICY_DATA_head
    WTS_POLICY_DATA._fields_ = [
        ("fDisableEncryption", win32more.Foundation.BOOLEAN),
        ("fDisableAutoReconnect", win32more.Foundation.BOOLEAN),
        ("ColorDepth", UInt32),
        ("MinEncryptionLevel", Byte),
        ("fDisableCpm", win32more.Foundation.BOOLEAN),
        ("fDisableCdm", win32more.Foundation.BOOLEAN),
        ("fDisableCcm", win32more.Foundation.BOOLEAN),
        ("fDisableLPT", win32more.Foundation.BOOLEAN),
        ("fDisableClip", win32more.Foundation.BOOLEAN),
        ("fDisablePNPRedir", win32more.Foundation.BOOLEAN),
    ]
    return WTS_POLICY_DATA
def _define_WTS_PROTOCOL_CACHE_head():
    class WTS_PROTOCOL_CACHE(Structure):
        pass
    return WTS_PROTOCOL_CACHE
def _define_WTS_PROTOCOL_CACHE():
    WTS_PROTOCOL_CACHE = win32more.System.RemoteDesktop.WTS_PROTOCOL_CACHE_head
    WTS_PROTOCOL_CACHE._fields_ = [
        ("CacheReads", UInt32),
        ("CacheHits", UInt32),
    ]
    return WTS_PROTOCOL_CACHE
def _define_WTS_CACHE_STATS_UN_head():
    class WTS_CACHE_STATS_UN(Union):
        pass
    return WTS_CACHE_STATS_UN
def _define_WTS_CACHE_STATS_UN():
    WTS_CACHE_STATS_UN = win32more.System.RemoteDesktop.WTS_CACHE_STATS_UN_head
    WTS_CACHE_STATS_UN._fields_ = [
        ("ProtocolCache", win32more.System.RemoteDesktop.WTS_PROTOCOL_CACHE * 4),
        ("TShareCacheStats", UInt32),
        ("Reserved", UInt32 * 20),
    ]
    return WTS_CACHE_STATS_UN
def _define_WTS_CACHE_STATS_head():
    class WTS_CACHE_STATS(Structure):
        pass
    return WTS_CACHE_STATS
def _define_WTS_CACHE_STATS():
    WTS_CACHE_STATS = win32more.System.RemoteDesktop.WTS_CACHE_STATS_head
    WTS_CACHE_STATS._fields_ = [
        ("Specific", UInt32),
        ("Data", win32more.System.RemoteDesktop.WTS_CACHE_STATS_UN),
        ("ProtocolType", UInt16),
        ("Length", UInt16),
    ]
    return WTS_CACHE_STATS
def _define_WTS_PROTOCOL_COUNTERS_head():
    class WTS_PROTOCOL_COUNTERS(Structure):
        pass
    return WTS_PROTOCOL_COUNTERS
def _define_WTS_PROTOCOL_COUNTERS():
    WTS_PROTOCOL_COUNTERS = win32more.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS_head
    WTS_PROTOCOL_COUNTERS._fields_ = [
        ("WdBytes", UInt32),
        ("WdFrames", UInt32),
        ("WaitForOutBuf", UInt32),
        ("Frames", UInt32),
        ("Bytes", UInt32),
        ("CompressedBytes", UInt32),
        ("CompressFlushes", UInt32),
        ("Errors", UInt32),
        ("Timeouts", UInt32),
        ("AsyncFramingError", UInt32),
        ("AsyncOverrunError", UInt32),
        ("AsyncOverflowError", UInt32),
        ("AsyncParityError", UInt32),
        ("TdErrors", UInt32),
        ("ProtocolType", UInt16),
        ("Length", UInt16),
        ("Specific", UInt16),
        ("Reserved", UInt32 * 100),
    ]
    return WTS_PROTOCOL_COUNTERS
def _define_WTS_PROTOCOL_STATUS_head():
    class WTS_PROTOCOL_STATUS(Structure):
        pass
    return WTS_PROTOCOL_STATUS
def _define_WTS_PROTOCOL_STATUS():
    WTS_PROTOCOL_STATUS = win32more.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head
    WTS_PROTOCOL_STATUS._fields_ = [
        ("Output", win32more.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS),
        ("Input", win32more.System.RemoteDesktop.WTS_PROTOCOL_COUNTERS),
        ("Cache", win32more.System.RemoteDesktop.WTS_CACHE_STATS),
        ("AsyncSignal", UInt32),
        ("AsyncSignalMask", UInt32),
        ("Counters", win32more.Foundation.LARGE_INTEGER * 100),
    ]
    return WTS_PROTOCOL_STATUS
def _define_WTS_DISPLAY_IOCTL_head():
    class WTS_DISPLAY_IOCTL(Structure):
        pass
    return WTS_DISPLAY_IOCTL
def _define_WTS_DISPLAY_IOCTL():
    WTS_DISPLAY_IOCTL = win32more.System.RemoteDesktop.WTS_DISPLAY_IOCTL_head
    WTS_DISPLAY_IOCTL._fields_ = [
        ("pDisplayIOCtlData", Byte * 256),
        ("cbDisplayIOCtlData", UInt32),
    ]
    return WTS_DISPLAY_IOCTL
WTS_LOGON_ERROR_REDIRECTOR_RESPONSE = Int32
WTS_LOGON_ERR_INVALID = 0
WTS_LOGON_ERR_NOT_HANDLED = 1
WTS_LOGON_ERR_HANDLED_SHOW = 2
WTS_LOGON_ERR_HANDLED_DONT_SHOW = 3
WTS_LOGON_ERR_HANDLED_DONT_SHOW_START_OVER = 4
def _define_WTS_PROPERTY_VALUE_head():
    class WTS_PROPERTY_VALUE(Structure):
        pass
    return WTS_PROPERTY_VALUE
def _define_WTS_PROPERTY_VALUE():
    WTS_PROPERTY_VALUE = win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE_head
    class WTS_PROPERTY_VALUE__u_e__Union(Union):
        pass
    class WTS_PROPERTY_VALUE__u_e__Union__bVal_e__Struct(Structure):
        pass
    WTS_PROPERTY_VALUE__u_e__Union__bVal_e__Struct._fields_ = [
        ("size", UInt32),
        ("pbVal", win32more.Foundation.PSTR),
    ]
    class WTS_PROPERTY_VALUE__u_e__Union__strVal_e__Struct(Structure):
        pass
    WTS_PROPERTY_VALUE__u_e__Union__strVal_e__Struct._fields_ = [
        ("size", UInt32),
        ("pstrVal", win32more.Foundation.PWSTR),
    ]
    WTS_PROPERTY_VALUE__u_e__Union._fields_ = [
        ("ulVal", UInt32),
        ("strVal", WTS_PROPERTY_VALUE__u_e__Union__strVal_e__Struct),
        ("bVal", WTS_PROPERTY_VALUE__u_e__Union__bVal_e__Struct),
        ("guidVal", Guid),
    ]
    WTS_PROPERTY_VALUE._fields_ = [
        ("Type", UInt16),
        ("u", WTS_PROPERTY_VALUE__u_e__Union),
    ]
    return WTS_PROPERTY_VALUE
WTS_CERT_TYPE = Int32
WTS_CERT_TYPE_INVALID = 0
WTS_CERT_TYPE_PROPRIETORY = 1
WTS_CERT_TYPE_X509 = 2
def _define_WTS_LICENSE_CAPABILITIES_head():
    class WTS_LICENSE_CAPABILITIES(Structure):
        pass
    return WTS_LICENSE_CAPABILITIES
def _define_WTS_LICENSE_CAPABILITIES():
    WTS_LICENSE_CAPABILITIES = win32more.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head
    WTS_LICENSE_CAPABILITIES._fields_ = [
        ("KeyExchangeAlg", UInt32),
        ("ProtocolVer", UInt32),
        ("fAuthenticateServer", win32more.Foundation.BOOL),
        ("CertType", win32more.System.RemoteDesktop.WTS_CERT_TYPE),
        ("cbClientName", UInt32),
        ("rgbClientName", Byte * 42),
    ]
    return WTS_LICENSE_CAPABILITIES
WRDS_CONNECTION_SETTING_LEVEL = Int32
WRDS_CONNECTION_SETTING_LEVEL_INVALID = 0
WRDS_CONNECTION_SETTING_LEVEL_1 = 1
WRDS_LISTENER_SETTING_LEVEL = Int32
WRDS_LISTENER_SETTING_LEVEL_INVALID = 0
WRDS_LISTENER_SETTING_LEVEL_1 = 1
WRDS_SETTING_TYPE = Int32
WRDS_SETTING_TYPE_INVALID = 0
WRDS_SETTING_TYPE_MACHINE = 1
WRDS_SETTING_TYPE_USER = 2
WRDS_SETTING_TYPE_SAM = 3
WRDS_SETTING_STATUS = Int32
WRDS_SETTING_STATUS_NOTAPPLICABLE = -1
WRDS_SETTING_STATUS_DISABLED = 0
WRDS_SETTING_STATUS_ENABLED = 1
WRDS_SETTING_STATUS_NOTCONFIGURED = 2
WRDS_SETTING_LEVEL = Int32
WRDS_SETTING_LEVEL_INVALID = 0
WRDS_SETTING_LEVEL_1 = 1
def _define_WRDS_LISTENER_SETTINGS_1_head():
    class WRDS_LISTENER_SETTINGS_1(Structure):
        pass
    return WRDS_LISTENER_SETTINGS_1
def _define_WRDS_LISTENER_SETTINGS_1():
    WRDS_LISTENER_SETTINGS_1 = win32more.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_1_head
    WRDS_LISTENER_SETTINGS_1._fields_ = [
        ("MaxProtocolListenerConnectionCount", UInt32),
        ("SecurityDescriptorSize", UInt32),
        ("pSecurityDescriptor", c_char_p_no),
    ]
    return WRDS_LISTENER_SETTINGS_1
def _define_WRDS_LISTENER_SETTING_head():
    class WRDS_LISTENER_SETTING(Union):
        pass
    return WRDS_LISTENER_SETTING
def _define_WRDS_LISTENER_SETTING():
    WRDS_LISTENER_SETTING = win32more.System.RemoteDesktop.WRDS_LISTENER_SETTING_head
    WRDS_LISTENER_SETTING._fields_ = [
        ("WRdsListenerSettings1", win32more.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_1),
    ]
    return WRDS_LISTENER_SETTING
def _define_WRDS_LISTENER_SETTINGS_head():
    class WRDS_LISTENER_SETTINGS(Structure):
        pass
    return WRDS_LISTENER_SETTINGS
def _define_WRDS_LISTENER_SETTINGS():
    WRDS_LISTENER_SETTINGS = win32more.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_head
    WRDS_LISTENER_SETTINGS._fields_ = [
        ("WRdsListenerSettingLevel", win32more.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL),
        ("WRdsListenerSetting", win32more.System.RemoteDesktop.WRDS_LISTENER_SETTING),
    ]
    return WRDS_LISTENER_SETTINGS
def _define_WRDS_CONNECTION_SETTINGS_1_head():
    class WRDS_CONNECTION_SETTINGS_1(Structure):
        pass
    return WRDS_CONNECTION_SETTINGS_1
def _define_WRDS_CONNECTION_SETTINGS_1():
    WRDS_CONNECTION_SETTINGS_1 = win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_1_head
    WRDS_CONNECTION_SETTINGS_1._fields_ = [
        ("fInheritInitialProgram", win32more.Foundation.BOOLEAN),
        ("fInheritColorDepth", win32more.Foundation.BOOLEAN),
        ("fHideTitleBar", win32more.Foundation.BOOLEAN),
        ("fInheritAutoLogon", win32more.Foundation.BOOLEAN),
        ("fMaximizeShell", win32more.Foundation.BOOLEAN),
        ("fDisablePNP", win32more.Foundation.BOOLEAN),
        ("fPasswordIsScPin", win32more.Foundation.BOOLEAN),
        ("fPromptForPassword", win32more.Foundation.BOOLEAN),
        ("fDisableCpm", win32more.Foundation.BOOLEAN),
        ("fDisableCdm", win32more.Foundation.BOOLEAN),
        ("fDisableCcm", win32more.Foundation.BOOLEAN),
        ("fDisableLPT", win32more.Foundation.BOOLEAN),
        ("fDisableClip", win32more.Foundation.BOOLEAN),
        ("fResetBroken", win32more.Foundation.BOOLEAN),
        ("fDisableEncryption", win32more.Foundation.BOOLEAN),
        ("fDisableAutoReconnect", win32more.Foundation.BOOLEAN),
        ("fDisableCtrlAltDel", win32more.Foundation.BOOLEAN),
        ("fDoubleClickDetect", win32more.Foundation.BOOLEAN),
        ("fEnableWindowsKey", win32more.Foundation.BOOLEAN),
        ("fUsingSavedCreds", win32more.Foundation.BOOLEAN),
        ("fMouse", win32more.Foundation.BOOLEAN),
        ("fNoAudioPlayback", win32more.Foundation.BOOLEAN),
        ("fRemoteConsoleAudio", win32more.Foundation.BOOLEAN),
        ("EncryptionLevel", Byte),
        ("ColorDepth", UInt16),
        ("ProtocolType", UInt16),
        ("HRes", UInt16),
        ("VRes", UInt16),
        ("ClientProductId", UInt16),
        ("OutBufCountHost", UInt16),
        ("OutBufCountClient", UInt16),
        ("OutBufLength", UInt16),
        ("KeyboardLayout", UInt32),
        ("MaxConnectionTime", UInt32),
        ("MaxDisconnectionTime", UInt32),
        ("MaxIdleTime", UInt32),
        ("PerformanceFlags", UInt32),
        ("KeyboardType", UInt32),
        ("KeyboardSubType", UInt32),
        ("KeyboardFunctionKey", UInt32),
        ("ActiveInputLocale", UInt32),
        ("SerialNumber", UInt32),
        ("ClientAddressFamily", UInt32),
        ("ClientBuildNumber", UInt32),
        ("ClientSessionId", UInt32),
        ("WorkDirectory", Char * 257),
        ("InitialProgram", Char * 257),
        ("UserName", Char * 256),
        ("Domain", Char * 256),
        ("Password", Char * 256),
        ("ProtocolName", Char * 9),
        ("DisplayDriverName", Char * 9),
        ("DisplayDeviceName", Char * 20),
        ("imeFileName", Char * 33),
        ("AudioDriverName", Char * 9),
        ("ClientName", Char * 21),
        ("ClientAddress", Char * 31),
        ("ClientDirectory", Char * 257),
        ("ClientDigProductId", Char * 33),
        ("ClientSockAddress", win32more.System.RemoteDesktop.WTS_SOCKADDR),
        ("ClientTimeZone", win32more.System.RemoteDesktop.WTS_TIME_ZONE_INFORMATION),
        ("WRdsListenerSettings", win32more.System.RemoteDesktop.WRDS_LISTENER_SETTINGS),
        ("EventLogActivityId", Guid),
        ("ContextSize", UInt32),
        ("ContextData", c_char_p_no),
    ]
    return WRDS_CONNECTION_SETTINGS_1
def _define_WRDS_SETTINGS_1_head():
    class WRDS_SETTINGS_1(Structure):
        pass
    return WRDS_SETTINGS_1
def _define_WRDS_SETTINGS_1():
    WRDS_SETTINGS_1 = win32more.System.RemoteDesktop.WRDS_SETTINGS_1_head
    WRDS_SETTINGS_1._fields_ = [
        ("WRdsDisableClipStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableClipValue", UInt32),
        ("WRdsDisableLPTStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableLPTValue", UInt32),
        ("WRdsDisableCcmStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableCcmValue", UInt32),
        ("WRdsDisableCdmStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableCdmValue", UInt32),
        ("WRdsDisableCpmStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableCpmValue", UInt32),
        ("WRdsDisablePnpStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisablePnpValue", UInt32),
        ("WRdsEncryptionLevelStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsEncryptionValue", UInt32),
        ("WRdsColorDepthStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsColorDepthValue", UInt32),
        ("WRdsDisableAutoReconnecetStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableAutoReconnecetValue", UInt32),
        ("WRdsDisableEncryptionStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsDisableEncryptionValue", UInt32),
        ("WRdsResetBrokenStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsResetBrokenValue", UInt32),
        ("WRdsMaxIdleTimeStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsMaxIdleTimeValue", UInt32),
        ("WRdsMaxDisconnectTimeStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsMaxDisconnectTimeValue", UInt32),
        ("WRdsMaxConnectTimeStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsMaxConnectTimeValue", UInt32),
        ("WRdsKeepAliveStatus", win32more.System.RemoteDesktop.WRDS_SETTING_STATUS),
        ("WRdsKeepAliveStartValue", win32more.Foundation.BOOLEAN),
        ("WRdsKeepAliveIntervalValue", UInt32),
    ]
    return WRDS_SETTINGS_1
def _define_WRDS_CONNECTION_SETTING_head():
    class WRDS_CONNECTION_SETTING(Union):
        pass
    return WRDS_CONNECTION_SETTING
def _define_WRDS_CONNECTION_SETTING():
    WRDS_CONNECTION_SETTING = win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTING_head
    WRDS_CONNECTION_SETTING._fields_ = [
        ("WRdsConnectionSettings1", win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_1),
    ]
    return WRDS_CONNECTION_SETTING
def _define_WRDS_CONNECTION_SETTINGS_head():
    class WRDS_CONNECTION_SETTINGS(Structure):
        pass
    return WRDS_CONNECTION_SETTINGS
def _define_WRDS_CONNECTION_SETTINGS():
    WRDS_CONNECTION_SETTINGS = win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head
    WRDS_CONNECTION_SETTINGS._fields_ = [
        ("WRdsConnectionSettingLevel", win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL),
        ("WRdsConnectionSetting", win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTING),
    ]
    return WRDS_CONNECTION_SETTINGS
def _define_WRDS_SETTING_head():
    class WRDS_SETTING(Union):
        pass
    return WRDS_SETTING
def _define_WRDS_SETTING():
    WRDS_SETTING = win32more.System.RemoteDesktop.WRDS_SETTING_head
    WRDS_SETTING._fields_ = [
        ("WRdsSettings1", win32more.System.RemoteDesktop.WRDS_SETTINGS_1),
    ]
    return WRDS_SETTING
def _define_WRDS_SETTINGS_head():
    class WRDS_SETTINGS(Structure):
        pass
    return WRDS_SETTINGS
def _define_WRDS_SETTINGS():
    WRDS_SETTINGS = win32more.System.RemoteDesktop.WRDS_SETTINGS_head
    WRDS_SETTINGS._fields_ = [
        ("WRdsSettingType", win32more.System.RemoteDesktop.WRDS_SETTING_TYPE),
        ("WRdsSettingLevel", win32more.System.RemoteDesktop.WRDS_SETTING_LEVEL),
        ("WRdsSetting", win32more.System.RemoteDesktop.WRDS_SETTING),
    ]
    return WRDS_SETTINGS
def _define_IWTSProtocolManager_head():
    class IWTSProtocolManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9eaf6cc-ed79-4f01-821d-1f881b9f66cc')
    return IWTSProtocolManager
def _define_IWTSProtocolManager():
    IWTSProtocolManager = win32more.System.RemoteDesktop.IWTSProtocolManager_head
    IWTSProtocolManager.CreateListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.IWTSProtocolListener_head), use_last_error=False)(3, 'CreateListener', ((1, 'wszListenerName'),(1, 'pProtocolListener'),)))
    IWTSProtocolManager.NotifyServiceStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SERVICE_STATE_head), use_last_error=False)(4, 'NotifyServiceStateChange', ((1, 'pTSServiceStateChange'),)))
    IWTSProtocolManager.NotifySessionOfServiceStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(5, 'NotifySessionOfServiceStart', ((1, 'SessionId'),)))
    IWTSProtocolManager.NotifySessionOfServiceStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(6, 'NotifySessionOfServiceStop', ((1, 'SessionId'),)))
    IWTSProtocolManager.NotifySessionStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head),UInt32, use_last_error=False)(7, 'NotifySessionStateChange', ((1, 'SessionId'),(1, 'EventId'),)))
    return IWTSProtocolManager
def _define_IWTSProtocolListener_head():
    class IWTSProtocolListener(win32more.System.Com.IUnknown_head):
        Guid = Guid('23083765-45f0-4394-8f69-32b2bc0ef4ca')
    return IWTSProtocolListener
def _define_IWTSProtocolListener():
    IWTSProtocolListener = win32more.System.RemoteDesktop.IWTSProtocolListener_head
    IWTSProtocolListener.StartListen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWTSProtocolListenerCallback_head, use_last_error=False)(3, 'StartListen', ((1, 'pCallback'),)))
    IWTSProtocolListener.StopListen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'StopListen', ()))
    return IWTSProtocolListener
def _define_IWTSProtocolListenerCallback_head():
    class IWTSProtocolListenerCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('23083765-1a2d-4de2-97de-4a35f260f0b3')
    return IWTSProtocolListenerCallback
def _define_IWTSProtocolListenerCallback():
    IWTSProtocolListenerCallback = win32more.System.RemoteDesktop.IWTSProtocolListenerCallback_head
    IWTSProtocolListenerCallback.OnConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWTSProtocolConnection_head,POINTER(win32more.System.RemoteDesktop.IWTSProtocolConnectionCallback_head), use_last_error=False)(3, 'OnConnected', ((1, 'pConnection'),(1, 'pCallback'),)))
    return IWTSProtocolListenerCallback
def _define_IWTSProtocolConnection_head():
    class IWTSProtocolConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('23083765-9095-4648-98bf-ef81c914032d')
    return IWTSProtocolConnection
def _define_IWTSProtocolConnection():
    IWTSProtocolConnection = win32more.System.RemoteDesktop.IWTSProtocolConnection_head
    IWTSProtocolConnection.GetLogonErrorRedirector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWTSProtocolLogonErrorRedirector_head), use_last_error=False)(3, 'GetLogonErrorRedirector', ((1, 'ppLogonErrorRedir'),)))
    IWTSProtocolConnection.SendPolicyData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_POLICY_DATA_head), use_last_error=False)(4, 'SendPolicyData', ((1, 'pPolicyData'),)))
    IWTSProtocolConnection.AcceptConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'AcceptConnection', ()))
    IWTSProtocolConnection.GetClientData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_CLIENT_DATA_head), use_last_error=False)(6, 'GetClientData', ((1, 'pClientData'),)))
    IWTSProtocolConnection.GetUserCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_USER_CREDENTIAL_head), use_last_error=False)(7, 'GetUserCredentials', ((1, 'pUserCreds'),)))
    IWTSProtocolConnection.GetLicenseConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWTSProtocolLicenseConnection_head), use_last_error=False)(8, 'GetLicenseConnection', ((1, 'ppLicenseConnection'),)))
    IWTSProtocolConnection.AuthenticateClientToSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(9, 'AuthenticateClientToSession', ((1, 'SessionId'),)))
    IWTSProtocolConnection.NotifySessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(10, 'NotifySessionId', ((1, 'SessionId'),)))
    IWTSProtocolConnection.GetProtocolHandles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR),POINTER(win32more.Foundation.HANDLE_PTR),POINTER(win32more.Foundation.HANDLE_PTR),POINTER(win32more.Foundation.HANDLE_PTR), use_last_error=False)(11, 'GetProtocolHandles', ((1, 'pKeyboardHandle'),(1, 'pMouseHandle'),(1, 'pBeepHandle'),(1, 'pVideoHandle'),)))
    IWTSProtocolConnection.ConnectNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'ConnectNotify', ((1, 'SessionId'),)))
    IWTSProtocolConnection.IsUserAllowedToLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HANDLE_PTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(13, 'IsUserAllowedToLogon', ((1, 'SessionId'),(1, 'UserToken'),(1, 'pDomainName'),(1, 'pUserName'),)))
    IWTSProtocolConnection.SessionArbitrationEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(14, 'SessionArbitrationEnumeration', ((1, 'hUserToken'),(1, 'bSingleSessionPerUserEnabled'),(1, 'pSessionIdArray'),(1, 'pdwSessionIdentifierCount'),)))
    IWTSProtocolConnection.LogonNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(15, 'LogonNotify', ((1, 'hClientToken'),(1, 'wszUserName'),(1, 'wszDomainName'),(1, 'SessionId'),)))
    IWTSProtocolConnection.GetUserData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_POLICY_DATA_head),POINTER(win32more.System.RemoteDesktop.WTS_USER_DATA_head), use_last_error=False)(16, 'GetUserData', ((1, 'pPolicyData'),(1, 'pClientData'),)))
    IWTSProtocolConnection.DisconnectNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'DisconnectNotify', ()))
    IWTSProtocolConnection.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Close', ()))
    IWTSProtocolConnection.GetProtocolStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head), use_last_error=False)(19, 'GetProtocolStatus', ((1, 'pProtocolStatus'),)))
    IWTSProtocolConnection.GetLastInputTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(20, 'GetLastInputTime', ((1, 'pLastInputTime'),)))
    IWTSProtocolConnection.SetErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(21, 'SetErrorInfo', ((1, 'ulError'),)))
    IWTSProtocolConnection.SendBeep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(22, 'SendBeep', ((1, 'Frequency'),(1, 'Duration'),)))
    IWTSProtocolConnection.CreateVirtualChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.BOOL,UInt32,POINTER(UIntPtr), use_last_error=False)(23, 'CreateVirtualChannel', ((1, 'szEndpointName'),(1, 'bStatic'),(1, 'RequestedPriority'),(1, 'phChannel'),)))
    IWTSProtocolConnection.QueryProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE),POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE), use_last_error=False)(24, 'QueryProperty', ((1, 'QueryType'),(1, 'ulNumEntriesIn'),(1, 'ulNumEntriesOut'),(1, 'pPropertyEntriesIn'),(1, 'pPropertyEntriesOut'),)))
    IWTSProtocolConnection.GetShadowConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWTSProtocolShadowConnection_head), use_last_error=False)(25, 'GetShadowConnection', ((1, 'ppShadowConnection'),)))
    return IWTSProtocolConnection
def _define_IWTSProtocolConnectionCallback_head():
    class IWTSProtocolConnectionCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('23083765-75eb-41fe-b4fb-e086242afa0f')
    return IWTSProtocolConnectionCallback
def _define_IWTSProtocolConnectionCallback():
    IWTSProtocolConnectionCallback = win32more.System.RemoteDesktop.IWTSProtocolConnectionCallback_head
    IWTSProtocolConnectionCallback.OnReady = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnReady', ()))
    IWTSProtocolConnectionCallback.BrokenConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'BrokenConnection', ((1, 'Reason'),(1, 'Source'),)))
    IWTSProtocolConnectionCallback.StopScreenUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'StopScreenUpdates', ()))
    IWTSProtocolConnectionCallback.RedrawWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SMALL_RECT_head), use_last_error=False)(6, 'RedrawWindow', ((1, 'rect'),)))
    IWTSProtocolConnectionCallback.DisplayIOCtl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_DISPLAY_IOCTL_head), use_last_error=False)(7, 'DisplayIOCtl', ((1, 'DisplayIOCtl'),)))
    return IWTSProtocolConnectionCallback
def _define_IWTSProtocolShadowConnection_head():
    class IWTSProtocolShadowConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('ee3b0c14-37fb-456b-bab3-6d6cd51e13bf')
    return IWTSProtocolShadowConnection
def _define_IWTSProtocolShadowConnection():
    IWTSProtocolShadowConnection = win32more.System.RemoteDesktop.IWTSProtocolShadowConnection_head
    IWTSProtocolShadowConnection.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,Byte,UInt16,win32more.System.RemoteDesktop.IWTSProtocolShadowCallback_head, use_last_error=False)(3, 'Start', ((1, 'pTargetServerName'),(1, 'TargetSessionId'),(1, 'HotKeyVk'),(1, 'HotkeyModifiers'),(1, 'pShadowCallback'),)))
    IWTSProtocolShadowConnection.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Stop', ()))
    IWTSProtocolShadowConnection.DoTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(5, 'DoTarget', ((1, 'pParam1'),(1, 'Param1Size'),(1, 'pParam2'),(1, 'Param2Size'),(1, 'pParam3'),(1, 'Param3Size'),(1, 'pParam4'),(1, 'Param4Size'),(1, 'pClientName'),)))
    return IWTSProtocolShadowConnection
def _define_IWTSProtocolShadowCallback_head():
    class IWTSProtocolShadowCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('503a2504-aae5-4ab1-93e0-6d1c4bc6f71a')
    return IWTSProtocolShadowCallback
def _define_IWTSProtocolShadowCallback():
    IWTSProtocolShadowCallback = win32more.System.RemoteDesktop.IWTSProtocolShadowCallback_head
    IWTSProtocolShadowCallback.StopShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'StopShadow', ()))
    IWTSProtocolShadowCallback.InvokeTargetShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'InvokeTargetShadow', ((1, 'pTargetServerName'),(1, 'TargetSessionId'),(1, 'pParam1'),(1, 'Param1Size'),(1, 'pParam2'),(1, 'Param2Size'),(1, 'pParam3'),(1, 'Param3Size'),(1, 'pParam4'),(1, 'Param4Size'),(1, 'pClientName'),)))
    return IWTSProtocolShadowCallback
def _define_IWTSProtocolLicenseConnection_head():
    class IWTSProtocolLicenseConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('23083765-178c-4079-8e4a-fea6496a4d70')
    return IWTSProtocolLicenseConnection
def _define_IWTSProtocolLicenseConnection():
    IWTSProtocolLicenseConnection = win32more.System.RemoteDesktop.IWTSProtocolLicenseConnection_head
    IWTSProtocolLicenseConnection.RequestLicensingCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head),POINTER(UInt32), use_last_error=False)(3, 'RequestLicensingCapabilities', ((1, 'ppLicenseCapabilities'),(1, 'pcbLicenseCapabilities'),)))
    IWTSProtocolLicenseConnection.SendClientLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(4, 'SendClientLicense', ((1, 'pClientLicense'),(1, 'cbClientLicense'),)))
    IWTSProtocolLicenseConnection.RequestClientLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'RequestClientLicense', ((1, 'Reserve1'),(1, 'Reserve2'),(1, 'ppClientLicense'),(1, 'pcbClientLicense'),)))
    IWTSProtocolLicenseConnection.ProtocolComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'ProtocolComplete', ((1, 'ulComplete'),)))
    return IWTSProtocolLicenseConnection
def _define_IWTSProtocolLogonErrorRedirector_head():
    class IWTSProtocolLogonErrorRedirector(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd9b61a7-2916-4627-8dee-4328711ad6cb')
    return IWTSProtocolLogonErrorRedirector
def _define_IWTSProtocolLogonErrorRedirector():
    IWTSProtocolLogonErrorRedirector = win32more.System.RemoteDesktop.IWTSProtocolLogonErrorRedirector_head
    IWTSProtocolLogonErrorRedirector.OnBeginPainting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnBeginPainting', ()))
    IWTSProtocolLogonErrorRedirector.RedirectStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(4, 'RedirectStatus', ((1, 'pszMessage'),(1, 'pResponse'),)))
    IWTSProtocolLogonErrorRedirector.RedirectMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(5, 'RedirectMessage', ((1, 'pszCaption'),(1, 'pszMessage'),(1, 'uType'),(1, 'pResponse'),)))
    IWTSProtocolLogonErrorRedirector.RedirectLogonError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(6, 'RedirectLogonError', ((1, 'ntsStatus'),(1, 'ntsSubstatus'),(1, 'pszCaption'),(1, 'pszMessage'),(1, 'uType'),(1, 'pResponse'),)))
    return IWTSProtocolLogonErrorRedirector
def _define_IWRdsProtocolSettings_head():
    class IWRdsProtocolSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('654a5a6a-2550-47eb-b6f7-ebd637475265')
    return IWRdsProtocolSettings
def _define_IWRdsProtocolSettings():
    IWRdsProtocolSettings = win32more.System.RemoteDesktop.IWRdsProtocolSettings_head
    IWRdsProtocolSettings.GetSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.WRDS_SETTING_TYPE,win32more.System.RemoteDesktop.WRDS_SETTING_LEVEL,POINTER(win32more.System.RemoteDesktop.WRDS_SETTINGS_head), use_last_error=False)(3, 'GetSettings', ((1, 'WRdsSettingType'),(1, 'WRdsSettingLevel'),(1, 'pWRdsSettings'),)))
    IWRdsProtocolSettings.MergeSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WRDS_SETTINGS_head),win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTING_LEVEL,POINTER(win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head), use_last_error=False)(4, 'MergeSettings', ((1, 'pWRdsSettings'),(1, 'WRdsConnectionSettingLevel'),(1, 'pWRdsConnectionSettings'),)))
    return IWRdsProtocolSettings
def _define_IWRdsProtocolManager_head():
    class IWRdsProtocolManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc796967-3abb-40cd-a446-105276b58950')
    return IWRdsProtocolManager
def _define_IWRdsProtocolManager():
    IWRdsProtocolManager = win32more.System.RemoteDesktop.IWRdsProtocolManager_head
    IWRdsProtocolManager.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWRdsProtocolSettings_head,POINTER(win32more.System.RemoteDesktop.WRDS_SETTINGS_head), use_last_error=False)(3, 'Initialize', ((1, 'pIWRdsSettings'),(1, 'pWRdsSettings'),)))
    IWRdsProtocolManager.CreateListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.IWRdsProtocolListener_head), use_last_error=False)(4, 'CreateListener', ((1, 'wszListenerName'),(1, 'pProtocolListener'),)))
    IWRdsProtocolManager.NotifyServiceStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SERVICE_STATE_head), use_last_error=False)(5, 'NotifyServiceStateChange', ((1, 'pTSServiceStateChange'),)))
    IWRdsProtocolManager.NotifySessionOfServiceStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(6, 'NotifySessionOfServiceStart', ((1, 'SessionId'),)))
    IWRdsProtocolManager.NotifySessionOfServiceStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(7, 'NotifySessionOfServiceStop', ((1, 'SessionId'),)))
    IWRdsProtocolManager.NotifySessionStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head),UInt32, use_last_error=False)(8, 'NotifySessionStateChange', ((1, 'SessionId'),(1, 'EventId'),)))
    IWRdsProtocolManager.NotifySettingsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WRDS_SETTINGS_head), use_last_error=False)(9, 'NotifySettingsChange', ((1, 'pWRdsSettings'),)))
    IWRdsProtocolManager.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Uninitialize', ()))
    return IWRdsProtocolManager
def _define_IWRdsProtocolListener_head():
    class IWRdsProtocolListener(win32more.System.Com.IUnknown_head):
        Guid = Guid('fcbc131b-c686-451d-a773-e279e230f540')
    return IWRdsProtocolListener
def _define_IWRdsProtocolListener():
    IWRdsProtocolListener = win32more.System.RemoteDesktop.IWRdsProtocolListener_head
    IWRdsProtocolListener.GetSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.WRDS_LISTENER_SETTING_LEVEL,POINTER(win32more.System.RemoteDesktop.WRDS_LISTENER_SETTINGS_head), use_last_error=False)(3, 'GetSettings', ((1, 'WRdsListenerSettingLevel'),(1, 'pWRdsListenerSettings'),)))
    IWRdsProtocolListener.StartListen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWRdsProtocolListenerCallback_head, use_last_error=False)(4, 'StartListen', ((1, 'pCallback'),)))
    IWRdsProtocolListener.StopListen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'StopListen', ()))
    return IWRdsProtocolListener
def _define_IWRdsProtocolListenerCallback_head():
    class IWRdsProtocolListenerCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('3ab27e5b-4449-4dc1-b74a-91621d4fe984')
    return IWRdsProtocolListenerCallback
def _define_IWRdsProtocolListenerCallback():
    IWRdsProtocolListenerCallback = win32more.System.RemoteDesktop.IWRdsProtocolListenerCallback_head
    IWRdsProtocolListenerCallback.OnConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.IWRdsProtocolConnection_head,POINTER(win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head),POINTER(win32more.System.RemoteDesktop.IWRdsProtocolConnectionCallback_head), use_last_error=False)(3, 'OnConnected', ((1, 'pConnection'),(1, 'pWRdsConnectionSettings'),(1, 'pCallback'),)))
    return IWRdsProtocolListenerCallback
def _define_IWRdsProtocolConnection_head():
    class IWRdsProtocolConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('324ed94f-fdaf-4ff6-81a8-42abe755830b')
    return IWRdsProtocolConnection
def _define_IWRdsProtocolConnection():
    IWRdsProtocolConnection = win32more.System.RemoteDesktop.IWRdsProtocolConnection_head
    IWRdsProtocolConnection.GetLogonErrorRedirector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWRdsProtocolLogonErrorRedirector_head), use_last_error=False)(3, 'GetLogonErrorRedirector', ((1, 'ppLogonErrorRedir'),)))
    IWRdsProtocolConnection.AcceptConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'AcceptConnection', ()))
    IWRdsProtocolConnection.GetClientData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_CLIENT_DATA_head), use_last_error=False)(5, 'GetClientData', ((1, 'pClientData'),)))
    IWRdsProtocolConnection.GetClientMonitorData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetClientMonitorData', ((1, 'pNumMonitors'),(1, 'pPrimaryMonitor'),)))
    IWRdsProtocolConnection.GetUserCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_USER_CREDENTIAL_head), use_last_error=False)(7, 'GetUserCredentials', ((1, 'pUserCreds'),)))
    IWRdsProtocolConnection.GetLicenseConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWRdsProtocolLicenseConnection_head), use_last_error=False)(8, 'GetLicenseConnection', ((1, 'ppLicenseConnection'),)))
    IWRdsProtocolConnection.AuthenticateClientToSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head), use_last_error=False)(9, 'AuthenticateClientToSession', ((1, 'SessionId'),)))
    IWRdsProtocolConnection.NotifySessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head),win32more.Foundation.HANDLE_PTR, use_last_error=False)(10, 'NotifySessionId', ((1, 'SessionId'),(1, 'SessionHandle'),)))
    IWRdsProtocolConnection.GetInputHandles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR),POINTER(win32more.Foundation.HANDLE_PTR),POINTER(win32more.Foundation.HANDLE_PTR), use_last_error=False)(11, 'GetInputHandles', ((1, 'pKeyboardHandle'),(1, 'pMouseHandle'),(1, 'pBeepHandle'),)))
    IWRdsProtocolConnection.GetVideoHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR), use_last_error=False)(12, 'GetVideoHandle', ((1, 'pVideoHandle'),)))
    IWRdsProtocolConnection.ConnectNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'ConnectNotify', ((1, 'SessionId'),)))
    IWRdsProtocolConnection.IsUserAllowedToLogon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HANDLE_PTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(14, 'IsUserAllowedToLogon', ((1, 'SessionId'),(1, 'UserToken'),(1, 'pDomainName'),(1, 'pUserName'),)))
    IWRdsProtocolConnection.SessionArbitrationEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(15, 'SessionArbitrationEnumeration', ((1, 'hUserToken'),(1, 'bSingleSessionPerUserEnabled'),(1, 'pSessionIdArray'),(1, 'pdwSessionIdentifierCount'),)))
    IWRdsProtocolConnection.LogonNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTS_SESSION_ID_head),POINTER(win32more.System.RemoteDesktop.WRDS_CONNECTION_SETTINGS_head), use_last_error=False)(16, 'LogonNotify', ((1, 'hClientToken'),(1, 'wszUserName'),(1, 'wszDomainName'),(1, 'SessionId'),(1, 'pWRdsConnectionSettings'),)))
    IWRdsProtocolConnection.PreDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'PreDisconnect', ((1, 'DisconnectReason'),)))
    IWRdsProtocolConnection.DisconnectNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'DisconnectNotify', ()))
    IWRdsProtocolConnection.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'Close', ()))
    IWRdsProtocolConnection.GetProtocolStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_PROTOCOL_STATUS_head), use_last_error=False)(20, 'GetProtocolStatus', ((1, 'pProtocolStatus'),)))
    IWRdsProtocolConnection.GetLastInputTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(21, 'GetLastInputTime', ((1, 'pLastInputTime'),)))
    IWRdsProtocolConnection.SetErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(22, 'SetErrorInfo', ((1, 'ulError'),)))
    IWRdsProtocolConnection.CreateVirtualChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.BOOL,UInt32,POINTER(UIntPtr), use_last_error=False)(23, 'CreateVirtualChannel', ((1, 'szEndpointName'),(1, 'bStatic'),(1, 'RequestedPriority'),(1, 'phChannel'),)))
    IWRdsProtocolConnection.QueryProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE),POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE), use_last_error=False)(24, 'QueryProperty', ((1, 'QueryType'),(1, 'ulNumEntriesIn'),(1, 'ulNumEntriesOut'),(1, 'pPropertyEntriesIn'),(1, 'pPropertyEntriesOut'),)))
    IWRdsProtocolConnection.GetShadowConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IWRdsProtocolShadowConnection_head), use_last_error=False)(25, 'GetShadowConnection', ((1, 'ppShadowConnection'),)))
    IWRdsProtocolConnection.NotifyCommandProcessCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(26, 'NotifyCommandProcessCreated', ((1, 'SessionId'),)))
    return IWRdsProtocolConnection
def _define_IWRdsProtocolConnectionCallback_head():
    class IWRdsProtocolConnectionCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('f1d70332-d070-4ef1-a088-78313536c2d6')
    return IWRdsProtocolConnectionCallback
def _define_IWRdsProtocolConnectionCallback():
    IWRdsProtocolConnectionCallback = win32more.System.RemoteDesktop.IWRdsProtocolConnectionCallback_head
    IWRdsProtocolConnectionCallback.OnReady = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnReady', ()))
    IWRdsProtocolConnectionCallback.BrokenConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'BrokenConnection', ((1, 'Reason'),(1, 'Source'),)))
    IWRdsProtocolConnectionCallback.StopScreenUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'StopScreenUpdates', ()))
    IWRdsProtocolConnectionCallback.RedrawWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_SMALL_RECT_head), use_last_error=False)(6, 'RedrawWindow', ((1, 'rect'),)))
    IWRdsProtocolConnectionCallback.GetConnectionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetConnectionId', ((1, 'pConnectionId'),)))
    return IWRdsProtocolConnectionCallback
def _define_IWRdsProtocolShadowConnection_head():
    class IWRdsProtocolShadowConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ae85ce6-cade-4548-8feb-99016597f60a')
    return IWRdsProtocolShadowConnection
def _define_IWRdsProtocolShadowConnection():
    IWRdsProtocolShadowConnection = win32more.System.RemoteDesktop.IWRdsProtocolShadowConnection_head
    IWRdsProtocolShadowConnection.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,Byte,UInt16,win32more.System.RemoteDesktop.IWRdsProtocolShadowCallback_head, use_last_error=False)(3, 'Start', ((1, 'pTargetServerName'),(1, 'TargetSessionId'),(1, 'HotKeyVk'),(1, 'HotkeyModifiers'),(1, 'pShadowCallback'),)))
    IWRdsProtocolShadowConnection.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Stop', ()))
    IWRdsProtocolShadowConnection.DoTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(5, 'DoTarget', ((1, 'pParam1'),(1, 'Param1Size'),(1, 'pParam2'),(1, 'Param2Size'),(1, 'pParam3'),(1, 'Param3Size'),(1, 'pParam4'),(1, 'Param4Size'),(1, 'pClientName'),)))
    return IWRdsProtocolShadowConnection
def _define_IWRdsProtocolShadowCallback_head():
    class IWRdsProtocolShadowCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('e0667ce0-0372-40d6-adb2-a0f3322674d6')
    return IWRdsProtocolShadowCallback
def _define_IWRdsProtocolShadowCallback():
    IWRdsProtocolShadowCallback = win32more.System.RemoteDesktop.IWRdsProtocolShadowCallback_head
    IWRdsProtocolShadowCallback.StopShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'StopShadow', ()))
    IWRdsProtocolShadowCallback.InvokeTargetShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'InvokeTargetShadow', ((1, 'pTargetServerName'),(1, 'TargetSessionId'),(1, 'pParam1'),(1, 'Param1Size'),(1, 'pParam2'),(1, 'Param2Size'),(1, 'pParam3'),(1, 'Param3Size'),(1, 'pParam4'),(1, 'Param4Size'),(1, 'pClientName'),)))
    return IWRdsProtocolShadowCallback
def _define_IWRdsProtocolLicenseConnection_head():
    class IWRdsProtocolLicenseConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('1d6a145f-d095-4424-957a-407fae822d84')
    return IWRdsProtocolLicenseConnection
def _define_IWRdsProtocolLicenseConnection():
    IWRdsProtocolLicenseConnection = win32more.System.RemoteDesktop.IWRdsProtocolLicenseConnection_head
    IWRdsProtocolLicenseConnection.RequestLicensingCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.WTS_LICENSE_CAPABILITIES_head),POINTER(UInt32), use_last_error=False)(3, 'RequestLicensingCapabilities', ((1, 'ppLicenseCapabilities'),(1, 'pcbLicenseCapabilities'),)))
    IWRdsProtocolLicenseConnection.SendClientLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(4, 'SendClientLicense', ((1, 'pClientLicense'),(1, 'cbClientLicense'),)))
    IWRdsProtocolLicenseConnection.RequestClientLicense = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'RequestClientLicense', ((1, 'Reserve1'),(1, 'Reserve2'),(1, 'ppClientLicense'),(1, 'pcbClientLicense'),)))
    IWRdsProtocolLicenseConnection.ProtocolComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'ProtocolComplete', ((1, 'ulComplete'),)))
    return IWRdsProtocolLicenseConnection
def _define_IWRdsProtocolLogonErrorRedirector_head():
    class IWRdsProtocolLogonErrorRedirector(win32more.System.Com.IUnknown_head):
        Guid = Guid('519fe83b-142a-4120-a3d5-a405d315281a')
    return IWRdsProtocolLogonErrorRedirector
def _define_IWRdsProtocolLogonErrorRedirector():
    IWRdsProtocolLogonErrorRedirector = win32more.System.RemoteDesktop.IWRdsProtocolLogonErrorRedirector_head
    IWRdsProtocolLogonErrorRedirector.OnBeginPainting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnBeginPainting', ()))
    IWRdsProtocolLogonErrorRedirector.RedirectStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(4, 'RedirectStatus', ((1, 'pszMessage'),(1, 'pResponse'),)))
    IWRdsProtocolLogonErrorRedirector.RedirectMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(5, 'RedirectMessage', ((1, 'pszCaption'),(1, 'pszMessage'),(1, 'uType'),(1, 'pResponse'),)))
    IWRdsProtocolLogonErrorRedirector.RedirectLogonError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.RemoteDesktop.WTS_LOGON_ERROR_REDIRECTOR_RESPONSE), use_last_error=False)(6, 'RedirectLogonError', ((1, 'ntsStatus'),(1, 'ntsSubstatus'),(1, 'pszCaption'),(1, 'pszMessage'),(1, 'uType'),(1, 'pResponse'),)))
    return IWRdsProtocolLogonErrorRedirector
def _define_IWRdsWddmIddProps_head():
    class IWRdsWddmIddProps(win32more.System.Com.IUnknown_head):
        Guid = Guid('1382df4d-a289-43d1-a184-144726f9af90')
    return IWRdsWddmIddProps
def _define_IWRdsWddmIddProps():
    IWRdsWddmIddProps = win32more.System.RemoteDesktop.IWRdsWddmIddProps_head
    IWRdsWddmIddProps.GetHardwareId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(3, 'GetHardwareId', ((1, 'pDisplayDriverHardwareId'),(1, 'Count'),)))
    IWRdsWddmIddProps.OnDriverLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HANDLE_PTR, use_last_error=False)(4, 'OnDriverLoad', ((1, 'SessionId'),(1, 'DriverHandle'),)))
    IWRdsWddmIddProps.OnDriverUnload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'OnDriverUnload', ((1, 'SessionId'),)))
    IWRdsWddmIddProps.EnableWddmIdd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'EnableWddmIdd', ((1, 'Enabled'),)))
    return IWRdsWddmIddProps
def _define_IWRdsProtocolConnectionSettings_head():
    class IWRdsProtocolConnectionSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('83fcf5d3-f6f4-ea94-9cd2-32f280e1e510')
    return IWRdsProtocolConnectionSettings
def _define_IWRdsProtocolConnectionSettings():
    IWRdsProtocolConnectionSettings = win32more.System.RemoteDesktop.IWRdsProtocolConnectionSettings_head
    IWRdsProtocolConnectionSettings.SetConnectionSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), use_last_error=False)(3, 'SetConnectionSetting', ((1, 'PropertyID'),(1, 'pPropertyEntriesIn'),)))
    IWRdsProtocolConnectionSettings.GetConnectionSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.RemoteDesktop.WTS_PROPERTY_VALUE_head), use_last_error=False)(4, 'GetConnectionSetting', ((1, 'PropertyID'),(1, 'pPropertyEntriesOut'),)))
    return IWRdsProtocolConnectionSettings
def _define_IWRdsEnhancedFastReconnectArbitrator_head():
    class IWRdsEnhancedFastReconnectArbitrator(win32more.System.Com.IUnknown_head):
        Guid = Guid('5718ae9b-47f2-499f-b634-d8175bd51131')
    return IWRdsEnhancedFastReconnectArbitrator
def _define_IWRdsEnhancedFastReconnectArbitrator():
    IWRdsEnhancedFastReconnectArbitrator = win32more.System.RemoteDesktop.IWRdsEnhancedFastReconnectArbitrator_head
    IWRdsEnhancedFastReconnectArbitrator.GetSessionForEnhancedFastReconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(Int32), use_last_error=False)(3, 'GetSessionForEnhancedFastReconnect', ((1, 'pSessionIdArray'),(1, 'dwSessionCount'),(1, 'pResultSessionId'),)))
    return IWRdsEnhancedFastReconnectArbitrator
PasswordEncodingType = Int32
PasswordEncodingType_PasswordEncodingUTF8 = 0
PasswordEncodingType_PasswordEncodingUTF16LE = 1
PasswordEncodingType_PasswordEncodingUTF16BE = 2
def _define_IRemoteDesktopClientSettings_head():
    class IRemoteDesktopClientSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('48a0f2a7-2713-431f-bbac-6f4558e7d64d')
    return IRemoteDesktopClientSettings
def _define_IRemoteDesktopClientSettings():
    IRemoteDesktopClientSettings = win32more.System.RemoteDesktop.IRemoteDesktopClientSettings_head
    IRemoteDesktopClientSettings.ApplySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'ApplySettings', ((1, 'rdpFileContents'),)))
    IRemoteDesktopClientSettings.RetrieveSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'RetrieveSettings', ((1, 'rdpFileContents'),)))
    IRemoteDesktopClientSettings.GetRdpProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetRdpProperty', ((1, 'propertyName'),(1, 'value'),)))
    IRemoteDesktopClientSettings.SetRdpProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(10, 'SetRdpProperty', ((1, 'propertyName'),(1, 'value'),)))
    return IRemoteDesktopClientSettings
RemoteActionType = Int32
RemoteActionType_RemoteActionCharms = 0
RemoteActionType_RemoteActionAppbar = 1
RemoteActionType_RemoteActionSnap = 2
RemoteActionType_RemoteActionStartScreen = 3
RemoteActionType_RemoteActionAppSwitch = 4
SnapshotEncodingType = Int32
SnapshotEncodingType_SnapshotEncodingDataUri = 0
SnapshotFormatType = Int32
SnapshotFormatType_SnapshotFormatPng = 0
SnapshotFormatType_SnapshotFormatJpeg = 1
SnapshotFormatType_SnapshotFormatBmp = 2
def _define_IRemoteDesktopClientActions_head():
    class IRemoteDesktopClientActions(win32more.System.Com.IDispatch_head):
        Guid = Guid('7d54bc4e-1028-45d4-8b0a-b9b6bffba176')
    return IRemoteDesktopClientActions
def _define_IRemoteDesktopClientActions():
    IRemoteDesktopClientActions = win32more.System.RemoteDesktop.IRemoteDesktopClientActions_head
    IRemoteDesktopClientActions.SuspendScreenUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'SuspendScreenUpdates', ()))
    IRemoteDesktopClientActions.ResumeScreenUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'ResumeScreenUpdates', ()))
    IRemoteDesktopClientActions.ExecuteRemoteAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.RemoteActionType, use_last_error=False)(9, 'ExecuteRemoteAction', ((1, 'remoteAction'),)))
    IRemoteDesktopClientActions.GetSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.RemoteDesktop.SnapshotEncodingType,win32more.System.RemoteDesktop.SnapshotFormatType,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetSnapshot', ((1, 'snapshotEncoding'),(1, 'snapshotFormat'),(1, 'snapshotWidth'),(1, 'snapshotHeight'),(1, 'snapshotData'),)))
    return IRemoteDesktopClientActions
def _define_IRemoteDesktopClientTouchPointer_head():
    class IRemoteDesktopClientTouchPointer(win32more.System.Com.IDispatch_head):
        Guid = Guid('260ec22d-8cbc-44b5-9e88-2a37f6c93ae9')
    return IRemoteDesktopClientTouchPointer
def _define_IRemoteDesktopClientTouchPointer():
    IRemoteDesktopClientTouchPointer = win32more.System.RemoteDesktop.IRemoteDesktopClientTouchPointer_head
    IRemoteDesktopClientTouchPointer.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(7, 'put_Enabled', ((1, 'enabled'),)))
    IRemoteDesktopClientTouchPointer.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_Enabled', ((1, 'enabled'),)))
    IRemoteDesktopClientTouchPointer.put_EventsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(9, 'put_EventsEnabled', ((1, 'eventsEnabled'),)))
    IRemoteDesktopClientTouchPointer.get_EventsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_EventsEnabled', ((1, 'eventsEnabled'),)))
    IRemoteDesktopClientTouchPointer.put_PointerSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'put_PointerSpeed', ((1, 'pointerSpeed'),)))
    IRemoteDesktopClientTouchPointer.get_PointerSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_PointerSpeed', ((1, 'pointerSpeed'),)))
    return IRemoteDesktopClientTouchPointer
KeyCombinationType = Int32
KeyCombinationType_KeyCombinationHome = 0
KeyCombinationType_KeyCombinationLeft = 1
KeyCombinationType_KeyCombinationUp = 2
KeyCombinationType_KeyCombinationRight = 3
KeyCombinationType_KeyCombinationDown = 4
KeyCombinationType_KeyCombinationScroll = 5
def _define_IRemoteDesktopClient_head():
    class IRemoteDesktopClient(win32more.System.Com.IDispatch_head):
        Guid = Guid('57d25668-625a-4905-be4e-304caa13f89c')
    return IRemoteDesktopClient
def _define_IRemoteDesktopClient():
    IRemoteDesktopClient = win32more.System.RemoteDesktop.IRemoteDesktopClient_head
    IRemoteDesktopClient.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Connect', ()))
    IRemoteDesktopClient.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Disconnect', ()))
    IRemoteDesktopClient.Reconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(9, 'Reconnect', ((1, 'width'),(1, 'height'),)))
    IRemoteDesktopClient.get_Settings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IRemoteDesktopClientSettings_head), use_last_error=False)(10, 'get_Settings', ((1, 'settings'),)))
    IRemoteDesktopClient.get_Actions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IRemoteDesktopClientActions_head), use_last_error=False)(11, 'get_Actions', ((1, 'actions'),)))
    IRemoteDesktopClient.get_TouchPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteDesktop.IRemoteDesktopClientTouchPointer_head), use_last_error=False)(12, 'get_TouchPointer', ((1, 'touchPointer'),)))
    IRemoteDesktopClient.DeleteSavedCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(13, 'DeleteSavedCredentials', ((1, 'serverName'),)))
    IRemoteDesktopClient.UpdateSessionDisplaySettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(14, 'UpdateSessionDisplaySettings', ((1, 'width'),(1, 'height'),)))
    IRemoteDesktopClient.attachEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head, use_last_error=False)(15, 'attachEvent', ((1, 'eventName'),(1, 'callback'),)))
    IRemoteDesktopClient.detachEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head, use_last_error=False)(16, 'detachEvent', ((1, 'eventName'),(1, 'callback'),)))
    return IRemoteDesktopClient
def _define_IRemoteSystemAdditionalInfoProvider_head():
    class IRemoteSystemAdditionalInfoProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('eeaa3d5f-ec63-4d27-af38-e86b1d7292cb')
    return IRemoteSystemAdditionalInfoProvider
def _define_IRemoteSystemAdditionalInfoProvider():
    IRemoteSystemAdditionalInfoProvider = win32more.System.RemoteDesktop.IRemoteSystemAdditionalInfoProvider_head
    IRemoteSystemAdditionalInfoProvider.GetAdditionalInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetAdditionalInfo', ((1, 'deduplicationId'),(1, 'riid'),(1, 'mapView'),)))
    return IRemoteSystemAdditionalInfoProvider
def _define_WTSSESSION_NOTIFICATION_head():
    class WTSSESSION_NOTIFICATION(Structure):
        pass
    return WTSSESSION_NOTIFICATION
def _define_WTSSESSION_NOTIFICATION():
    WTSSESSION_NOTIFICATION = win32more.System.RemoteDesktop.WTSSESSION_NOTIFICATION_head
    WTSSESSION_NOTIFICATION._fields_ = [
        ("cbSize", UInt32),
        ("dwSessionId", UInt32),
    ]
    return WTSSESSION_NOTIFICATION
def _define_WTSStopRemoteControlSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=True)(("WTSStopRemoteControlSession", windll["WTSAPI32"]), ((1, 'LogonId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSStartRemoteControlSessionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,Byte,UInt16, use_last_error=True)(("WTSStartRemoteControlSessionW", windll["WTSAPI32"]), ((1, 'pTargetServerName'),(1, 'TargetLogonId'),(1, 'HotkeyVk'),(1, 'HotkeyModifiers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSStartRemoteControlSession():
    return win32more.System.RemoteDesktop.WTSStartRemoteControlSessionW
def _define_WTSStartRemoteControlSessionA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,Byte,UInt16, use_last_error=True)(("WTSStartRemoteControlSessionA", windll["WTSAPI32"]), ((1, 'pTargetServerName'),(1, 'TargetLogonId'),(1, 'HotkeyVk'),(1, 'HotkeyModifiers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSConnectSessionA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=True)(("WTSConnectSessionA", windll["WTSAPI32"]), ((1, 'LogonId'),(1, 'TargetLogonId'),(1, 'pPassword'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSConnectSessionW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=True)(("WTSConnectSessionW", windll["WTSAPI32"]), ((1, 'LogonId'),(1, 'TargetLogonId'),(1, 'pPassword'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSConnectSession():
    return win32more.System.RemoteDesktop.WTSConnectSessionW
def _define_WTSEnumerateServersW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SERVER_INFOW_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateServersW", windll["WTSAPI32"]), ((1, 'pDomainName'),(1, 'Reserved'),(1, 'Version'),(1, 'ppServerInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateServers():
    return win32more.System.RemoteDesktop.WTSEnumerateServersW
def _define_WTSEnumerateServersA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SERVER_INFOA_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateServersA", windll["WTSAPI32"]), ((1, 'pDomainName'),(1, 'Reserved'),(1, 'Version'),(1, 'ppServerInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSOpenServerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("WTSOpenServerW", windll["WTSAPI32"]), ((1, 'pServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSOpenServer():
    return win32more.System.RemoteDesktop.WTSOpenServerW
def _define_WTSOpenServerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR, use_last_error=False)(("WTSOpenServerA", windll["WTSAPI32"]), ((1, 'pServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSOpenServerExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("WTSOpenServerExW", windll["WTSAPI32"]), ((1, 'pServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSOpenServerEx():
    return win32more.System.RemoteDesktop.WTSOpenServerExW
def _define_WTSOpenServerExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR, use_last_error=False)(("WTSOpenServerExA", windll["WTSAPI32"]), ((1, 'pServerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSCloseServer():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)(("WTSCloseServer", windll["WTSAPI32"]), ((1, 'hServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateSessionsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SESSION_INFOW_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateSessionsW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'Reserved'),(1, 'Version'),(1, 'ppSessionInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateSessions():
    return win32more.System.RemoteDesktop.WTSEnumerateSessionsW
def _define_WTSEnumerateSessionsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SESSION_INFOA_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateSessionsA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'Reserved'),(1, 'Version'),(1, 'ppSessionInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateSessionsExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SESSION_INFO_1W_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateSessionsExW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pLevel'),(1, 'Filter'),(1, 'ppSessionInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateSessionsEx():
    return win32more.System.RemoteDesktop.WTSEnumerateSessionsExW
def _define_WTSEnumerateSessionsExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_SESSION_INFO_1A_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateSessionsExA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pLevel'),(1, 'Filter'),(1, 'ppSessionInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateProcessesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_PROCESS_INFOW_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateProcessesW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'Reserved'),(1, 'Version'),(1, 'ppProcessInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateProcesses():
    return win32more.System.RemoteDesktop.WTSEnumerateProcessesW
def _define_WTSEnumerateProcessesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(POINTER(win32more.System.RemoteDesktop.WTS_PROCESS_INFOA_head)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateProcessesA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'Reserved'),(1, 'Version'),(1, 'ppProcessInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSTerminateProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32, use_last_error=True)(("WTSTerminateProcess", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'ProcessId'),(1, 'ExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQuerySessionInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.System.RemoteDesktop.WTS_INFO_CLASS,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=True)(("WTSQuerySessionInformationW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'WTSInfoClass'),(1, 'ppBuffer'),(1, 'pBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQuerySessionInformation():
    return win32more.System.RemoteDesktop.WTSQuerySessionInformationW
def _define_WTSQuerySessionInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.System.RemoteDesktop.WTS_INFO_CLASS,POINTER(win32more.Foundation.PSTR),POINTER(UInt32), use_last_error=True)(("WTSQuerySessionInformationA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'WTSInfoClass'),(1, 'ppBuffer'),(1, 'pBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQueryUserConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.RemoteDesktop.WTS_CONFIG_CLASS,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=True)(("WTSQueryUserConfigW", windll["WTSAPI32"]), ((1, 'pServerName'),(1, 'pUserName'),(1, 'WTSConfigClass'),(1, 'ppBuffer'),(1, 'pBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQueryUserConfig():
    return win32more.System.RemoteDesktop.WTSQueryUserConfigW
def _define_WTSQueryUserConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.RemoteDesktop.WTS_CONFIG_CLASS,POINTER(win32more.Foundation.PSTR),POINTER(UInt32), use_last_error=True)(("WTSQueryUserConfigA", windll["WTSAPI32"]), ((1, 'pServerName'),(1, 'pUserName'),(1, 'WTSConfigClass'),(1, 'ppBuffer'),(1, 'pBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSetUserConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.RemoteDesktop.WTS_CONFIG_CLASS,win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("WTSSetUserConfigW", windll["WTSAPI32"]), ((1, 'pServerName'),(1, 'pUserName'),(1, 'WTSConfigClass'),(1, 'pBuffer'),(1, 'DataLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSetUserConfig():
    return win32more.System.RemoteDesktop.WTSSetUserConfigW
def _define_WTSSetUserConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.RemoteDesktop.WTS_CONFIG_CLASS,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("WTSSetUserConfigA", windll["WTSAPI32"]), ((1, 'pServerName'),(1, 'pUserName'),(1, 'WTSConfigClass'),(1, 'pBuffer'),(1, 'DataLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSendMessageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.UI.WindowsAndMessaging.MESSAGEBOX_STYLE,UInt32,POINTER(win32more.UI.WindowsAndMessaging.MESSAGEBOX_RESULT),win32more.Foundation.BOOL, use_last_error=True)(("WTSSendMessageW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'pTitle'),(1, 'TitleLength'),(1, 'pMessage'),(1, 'MessageLength'),(1, 'Style'),(1, 'Timeout'),(1, 'pResponse'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSendMessage():
    return win32more.System.RemoteDesktop.WTSSendMessageW
def _define_WTSSendMessageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,UInt32,win32more.UI.WindowsAndMessaging.MESSAGEBOX_STYLE,UInt32,POINTER(win32more.UI.WindowsAndMessaging.MESSAGEBOX_RESULT),win32more.Foundation.BOOL, use_last_error=True)(("WTSSendMessageA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'pTitle'),(1, 'TitleLength'),(1, 'pMessage'),(1, 'MessageLength'),(1, 'Style'),(1, 'Timeout'),(1, 'pResponse'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSDisconnectSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL, use_last_error=True)(("WTSDisconnectSession", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSLogoffSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL, use_last_error=True)(("WTSLogoffSession", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'bWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSShutdownSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=True)(("WTSShutdownSystem", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'ShutdownFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSWaitSystemEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(UInt32), use_last_error=True)(("WTSWaitSystemEvent", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'EventMask'),(1, 'pEventFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelOpen():
    try:
        return WINFUNCTYPE(win32more.System.RemoteDesktop.HwtsVirtualChannelHandle,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR, use_last_error=True)(("WTSVirtualChannelOpen", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'SessionId'),(1, 'pVirtualName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelOpenEx():
    try:
        return WINFUNCTYPE(win32more.System.RemoteDesktop.HwtsVirtualChannelHandle,UInt32,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("WTSVirtualChannelOpenEx", windll["WTSAPI32"]), ((1, 'SessionId'),(1, 'pVirtualName'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("WTSVirtualChannelClose", windll["WTSAPI32"]), ((1, 'hChannelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelRead():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(UInt32), use_last_error=True)(("WTSVirtualChannelRead", windll["WTSAPI32"]), ((1, 'hChannelHandle'),(1, 'TimeOut'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'pBytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelWrite():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,POINTER(UInt32), use_last_error=True)(("WTSVirtualChannelWrite", windll["WTSAPI32"]), ((1, 'hChannelHandle'),(1, 'Buffer'),(1, 'Length'),(1, 'pBytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelPurgeInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("WTSVirtualChannelPurgeInput", windll["WTSAPI32"]), ((1, 'hChannelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelPurgeOutput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("WTSVirtualChannelPurgeOutput", windll["WTSAPI32"]), ((1, 'hChannelHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSVirtualChannelQuery():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.RemoteDesktop.WTS_VIRTUAL_CLASS,POINTER(c_void_p),POINTER(UInt32), use_last_error=True)(("WTSVirtualChannelQuery", windll["WTSAPI32"]), ((1, 'hChannelHandle'),(1, 'param1'),(1, 'ppBuffer'),(1, 'pBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSFreeMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("WTSFreeMemory", windll["WTSAPI32"]), ((1, 'pMemory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSRegisterSessionNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32, use_last_error=True)(("WTSRegisterSessionNotification", windll["WTSAPI32"]), ((1, 'hWnd'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSUnRegisterSessionNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("WTSUnRegisterSessionNotification", windll["WTSAPI32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSRegisterSessionNotificationEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HWND,UInt32, use_last_error=True)(("WTSRegisterSessionNotificationEx", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'hWnd'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSUnRegisterSessionNotificationEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HWND, use_last_error=True)(("WTSUnRegisterSessionNotificationEx", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQueryUserToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("WTSQueryUserToken", windll["WTSAPI32"]), ((1, 'SessionId'),(1, 'phToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSFreeMemoryExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.RemoteDesktop.WTS_TYPE_CLASS,c_void_p,UInt32, use_last_error=True)(("WTSFreeMemoryExW", windll["WTSAPI32"]), ((1, 'WTSTypeClass'),(1, 'pMemory'),(1, 'NumberOfEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSFreeMemoryEx():
    return win32more.System.RemoteDesktop.WTSFreeMemoryExW
def _define_WTSFreeMemoryExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.RemoteDesktop.WTS_TYPE_CLASS,c_void_p,UInt32, use_last_error=True)(("WTSFreeMemoryExA", windll["WTSAPI32"]), ((1, 'WTSTypeClass'),(1, 'pMemory'),(1, 'NumberOfEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateProcessesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=True)(("WTSEnumerateProcessesExW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pLevel'),(1, 'SessionId'),(1, 'ppProcessInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateProcessesEx():
    return win32more.System.RemoteDesktop.WTSEnumerateProcessesExW
def _define_WTSEnumerateProcessesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.PSTR),POINTER(UInt32), use_last_error=True)(("WTSEnumerateProcessesExA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pLevel'),(1, 'SessionId'),(1, 'ppProcessInfo'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateListenersW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateListenersW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListeners'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnumerateListeners():
    return win32more.System.RemoteDesktop.WTSEnumerateListenersW
def _define_WTSEnumerateListenersA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(POINTER(SByte)),POINTER(UInt32), use_last_error=True)(("WTSEnumerateListenersA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListeners'),(1, 'pCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQueryListenerConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTSLISTENERCONFIGW_head), use_last_error=True)(("WTSQueryListenerConfigW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSQueryListenerConfig():
    return win32more.System.RemoteDesktop.WTSQueryListenerConfigW
def _define_WTSQueryListenerConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.RemoteDesktop.WTSLISTENERCONFIGA_head), use_last_error=True)(("WTSQueryListenerConfigA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSCreateListenerW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.RemoteDesktop.WTSLISTENERCONFIGW_head),UInt32, use_last_error=True)(("WTSCreateListenerW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'pBuffer'),(1, 'flag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSCreateListener():
    return win32more.System.RemoteDesktop.WTSCreateListenerW
def _define_WTSCreateListenerA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.RemoteDesktop.WTSLISTENERCONFIGA_head),UInt32, use_last_error=True)(("WTSCreateListenerA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'pBuffer'),(1, 'flag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSetListenerSecurityW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=True)(("WTSSetListenerSecurityW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSetListenerSecurity():
    return win32more.System.RemoteDesktop.WTSSetListenerSecurityW
def _define_WTSSetListenerSecurityA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), use_last_error=True)(("WTSSetListenerSecurityA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSGetListenerSecurityW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("WTSGetListenerSecurityW", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSGetListenerSecurity():
    return win32more.System.RemoteDesktop.WTSGetListenerSecurityW
def _define_WTSGetListenerSecurityA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),UInt32,POINTER(UInt32), use_last_error=True)(("WTSGetListenerSecurityA", windll["WTSAPI32"]), ((1, 'hServer'),(1, 'pReserved'),(1, 'Reserved'),(1, 'pListenerName'),(1, 'SecurityInformation'),(1, 'pSecurityDescriptor'),(1, 'nLength'),(1, 'lpnLengthNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSEnableChildSessions():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("WTSEnableChildSessions", windll["WTSAPI32"]), ((1, 'bEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSIsChildSessionsEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WTSIsChildSessionsEnabled", windll["WTSAPI32"]), ((1, 'pbEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSGetChildSessionId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("WTSGetChildSessionId", windll["WTSAPI32"]), ((1, 'pSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSSetRenderHint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),win32more.Foundation.HWND,UInt32,UInt32,c_char_p_no, use_last_error=False)(("WTSSetRenderHint", windll["WTSAPI32"]), ((1, 'pRenderHintID'),(1, 'hwndOwner'),(1, 'renderHintType'),(1, 'cbHintDataLength'),(1, 'pHintData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessIdToSessionId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32), use_last_error=True)(("ProcessIdToSessionId", windll["KERNEL32"]), ((1, 'dwProcessId'),(1, 'pSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WTSGetActiveConsoleSessionId():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("WTSGetActiveConsoleSessionId", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WTS_DOMAIN_LENGTH",
    "WTS_USERNAME_LENGTH",
    "WTS_PASSWORD_LENGTH",
    "WTS_DIRECTORY_LENGTH",
    "WTS_INITIALPROGRAM_LENGTH",
    "WTS_PROTOCOL_NAME_LENGTH",
    "WTS_DRIVER_NAME_LENGTH",
    "WTS_DEVICE_NAME_LENGTH",
    "WTS_IMEFILENAME_LENGTH",
    "WTS_CLIENTNAME_LENGTH",
    "WTS_CLIENTADDRESS_LENGTH",
    "WTS_CLIENT_PRODUCT_ID_LENGTH",
    "WTS_MAX_PROTOCOL_CACHE",
    "WTS_MAX_CACHE_RESERVED",
    "WTS_MAX_RESERVED",
    "WTS_MAX_COUNTERS",
    "WTS_MAX_DISPLAY_IOCTL_DATA",
    "WTS_PERF_DISABLE_NOTHING",
    "WTS_PERF_DISABLE_WALLPAPER",
    "WTS_PERF_DISABLE_FULLWINDOWDRAG",
    "WTS_PERF_DISABLE_MENUANIMATIONS",
    "WTS_PERF_DISABLE_THEMING",
    "WTS_PERF_ENABLE_ENHANCED_GRAPHICS",
    "WTS_PERF_DISABLE_CURSOR_SHADOW",
    "WTS_PERF_DISABLE_CURSORSETTINGS",
    "WTS_PERF_ENABLE_FONT_SMOOTHING",
    "WTS_PERF_ENABLE_DESKTOP_COMPOSITION",
    "WTS_VALUE_TYPE_ULONG",
    "WTS_VALUE_TYPE_STRING",
    "WTS_VALUE_TYPE_BINARY",
    "WTS_VALUE_TYPE_GUID",
    "WTS_KEY_EXCHANGE_ALG_RSA",
    "WTS_KEY_EXCHANGE_ALG_DH",
    "WTS_LICENSE_PROTOCOL_VERSION",
    "WTS_LICENSE_PREAMBLE_VERSION",
    "WRDS_DOMAIN_LENGTH",
    "WRDS_USERNAME_LENGTH",
    "WRDS_PASSWORD_LENGTH",
    "WRDS_DIRECTORY_LENGTH",
    "WRDS_INITIALPROGRAM_LENGTH",
    "WRDS_PROTOCOL_NAME_LENGTH",
    "WRDS_DRIVER_NAME_LENGTH",
    "WRDS_DEVICE_NAME_LENGTH",
    "WRDS_IMEFILENAME_LENGTH",
    "WRDS_CLIENTNAME_LENGTH",
    "WRDS_CLIENTADDRESS_LENGTH",
    "WRDS_CLIENT_PRODUCT_ID_LENGTH",
    "WRDS_MAX_PROTOCOL_CACHE",
    "WRDS_MAX_CACHE_RESERVED",
    "WRDS_MAX_RESERVED",
    "WRDS_MAX_COUNTERS",
    "WRDS_MAX_DISPLAY_IOCTL_DATA",
    "WRDS_PERF_DISABLE_NOTHING",
    "WRDS_PERF_DISABLE_WALLPAPER",
    "WRDS_PERF_DISABLE_FULLWINDOWDRAG",
    "WRDS_PERF_DISABLE_MENUANIMATIONS",
    "WRDS_PERF_DISABLE_THEMING",
    "WRDS_PERF_ENABLE_ENHANCED_GRAPHICS",
    "WRDS_PERF_DISABLE_CURSOR_SHADOW",
    "WRDS_PERF_DISABLE_CURSORSETTINGS",
    "WRDS_PERF_ENABLE_FONT_SMOOTHING",
    "WRDS_PERF_ENABLE_DESKTOP_COMPOSITION",
    "WRDS_VALUE_TYPE_ULONG",
    "WRDS_VALUE_TYPE_STRING",
    "WRDS_VALUE_TYPE_BINARY",
    "WRDS_VALUE_TYPE_GUID",
    "WRDS_KEY_EXCHANGE_ALG_RSA",
    "WRDS_KEY_EXCHANGE_ALG_DH",
    "WRDS_LICENSE_PROTOCOL_VERSION",
    "WRDS_LICENSE_PREAMBLE_VERSION",
    "SINGLE_SESSION",
    "FORCE_REJOIN",
    "FORCE_REJOIN_IN_CLUSTERMODE",
    "RESERVED_FOR_LEGACY",
    "KEEP_EXISTING_SESSIONS",
    "CHANNEL_EVENT_INITIALIZED",
    "CHANNEL_EVENT_CONNECTED",
    "CHANNEL_EVENT_V1_CONNECTED",
    "CHANNEL_EVENT_DISCONNECTED",
    "CHANNEL_EVENT_TERMINATED",
    "CHANNEL_EVENT_DATA_RECEIVED",
    "CHANNEL_EVENT_WRITE_COMPLETE",
    "CHANNEL_EVENT_WRITE_CANCELLED",
    "CHANNEL_RC_OK",
    "CHANNEL_RC_ALREADY_INITIALIZED",
    "CHANNEL_RC_NOT_INITIALIZED",
    "CHANNEL_RC_ALREADY_CONNECTED",
    "CHANNEL_RC_NOT_CONNECTED",
    "CHANNEL_RC_TOO_MANY_CHANNELS",
    "CHANNEL_RC_BAD_CHANNEL",
    "CHANNEL_RC_BAD_CHANNEL_HANDLE",
    "CHANNEL_RC_NO_BUFFER",
    "CHANNEL_RC_BAD_INIT_HANDLE",
    "CHANNEL_RC_NOT_OPEN",
    "CHANNEL_RC_BAD_PROC",
    "CHANNEL_RC_NO_MEMORY",
    "CHANNEL_RC_UNKNOWN_CHANNEL_NAME",
    "CHANNEL_RC_ALREADY_OPEN",
    "CHANNEL_RC_NOT_IN_VIRTUALCHANNELENTRY",
    "CHANNEL_RC_NULL_DATA",
    "CHANNEL_RC_ZERO_LENGTH",
    "CHANNEL_RC_INVALID_INSTANCE",
    "CHANNEL_RC_UNSUPPORTED_VERSION",
    "CHANNEL_RC_INITIALIZATION_ERROR",
    "VIRTUAL_CHANNEL_VERSION_WIN2000",
    "CHANNEL_CHUNK_LENGTH",
    "CHANNEL_BUFFER_SIZE",
    "CHANNEL_FLAG_FIRST",
    "CHANNEL_FLAG_LAST",
    "CHANNEL_FLAG_MIDDLE",
    "CHANNEL_FLAG_FAIL",
    "CHANNEL_OPTION_INITIALIZED",
    "CHANNEL_OPTION_ENCRYPT_RDP",
    "CHANNEL_OPTION_ENCRYPT_SC",
    "CHANNEL_OPTION_ENCRYPT_CS",
    "CHANNEL_OPTION_PRI_HIGH",
    "CHANNEL_OPTION_PRI_MED",
    "CHANNEL_OPTION_PRI_LOW",
    "CHANNEL_OPTION_COMPRESS_RDP",
    "CHANNEL_OPTION_COMPRESS",
    "CHANNEL_OPTION_SHOW_PROTOCOL",
    "CHANNEL_OPTION_REMOTE_CONTROL_PERSISTENT",
    "CHANNEL_MAX_COUNT",
    "CHANNEL_NAME_LEN",
    "MAX_POLICY_ATTRIBUTES",
    "WTS_CURRENT_SESSION",
    "USERNAME_LENGTH",
    "CLIENTNAME_LENGTH",
    "CLIENTADDRESS_LENGTH",
    "WTS_WSD_LOGOFF",
    "WTS_WSD_SHUTDOWN",
    "WTS_WSD_REBOOT",
    "WTS_WSD_POWEROFF",
    "WTS_WSD_FASTREBOOT",
    "MAX_ELAPSED_TIME_LENGTH",
    "MAX_DATE_TIME_LENGTH",
    "WINSTATIONNAME_LENGTH",
    "DOMAIN_LENGTH",
    "WTS_DRIVE_LENGTH",
    "WTS_LISTENER_NAME_LENGTH",
    "WTS_COMMENT_LENGTH",
    "WTS_LISTENER_CREATE",
    "WTS_LISTENER_UPDATE",
    "WTS_SECURITY_QUERY_INFORMATION",
    "WTS_SECURITY_SET_INFORMATION",
    "WTS_SECURITY_RESET",
    "WTS_SECURITY_VIRTUAL_CHANNELS",
    "WTS_SECURITY_REMOTE_CONTROL",
    "WTS_SECURITY_LOGON",
    "WTS_SECURITY_LOGOFF",
    "WTS_SECURITY_MESSAGE",
    "WTS_SECURITY_CONNECT",
    "WTS_SECURITY_DISCONNECT",
    "WTS_SECURITY_GUEST_ACCESS",
    "WTS_PROTOCOL_TYPE_CONSOLE",
    "WTS_PROTOCOL_TYPE_ICA",
    "WTS_PROTOCOL_TYPE_RDP",
    "WTS_SESSIONSTATE_UNKNOWN",
    "WTS_SESSIONSTATE_LOCK",
    "WTS_SESSIONSTATE_UNLOCK",
    "PRODUCTINFO_COMPANYNAME_LENGTH",
    "PRODUCTINFO_PRODUCTID_LENGTH",
    "VALIDATIONINFORMATION_LICENSE_LENGTH",
    "VALIDATIONINFORMATION_HARDWAREID_LENGTH",
    "WTS_EVENT_NONE",
    "WTS_EVENT_CREATE",
    "WTS_EVENT_DELETE",
    "WTS_EVENT_RENAME",
    "WTS_EVENT_CONNECT",
    "WTS_EVENT_DISCONNECT",
    "WTS_EVENT_LOGON",
    "WTS_EVENT_LOGOFF",
    "WTS_EVENT_STATECHANGE",
    "WTS_EVENT_LICENSE",
    "WTS_EVENT_ALL",
    "WTS_EVENT_FLUSH",
    "REMOTECONTROL_KBDSHIFT_HOTKEY",
    "REMOTECONTROL_KBDCTRL_HOTKEY",
    "REMOTECONTROL_KBDALT_HOTKEY",
    "WTS_CHANNEL_OPTION_DYNAMIC",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_LOW",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_MED",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_HIGH",
    "WTS_CHANNEL_OPTION_DYNAMIC_PRI_REAL",
    "WTS_CHANNEL_OPTION_DYNAMIC_NO_COMPRESS",
    "NOTIFY_FOR_ALL_SESSIONS",
    "NOTIFY_FOR_THIS_SESSION",
    "WTS_PROCESS_INFO_LEVEL_0",
    "WTS_PROCESS_INFO_LEVEL_1",
    "PLUGIN_CAPABILITY_EXTERNAL_REDIRECTION",
    "MaxFQDN_Len",
    "MaxNetBiosName_Len",
    "MaxNumOfExposed_IPs",
    "MaxUserName_Len",
    "MaxDomainName_Len",
    "MaxFarm_Len",
    "MaxAppName_Len",
    "WKS_FLAG_CLEAR_CREDS_ON_LAST_RESOURCE",
    "WKS_FLAG_PASSWORD_ENCRYPTED",
    "WKS_FLAG_CREDS_AUTHENTICATED",
    "SB_SYNCH_CONFLICT_MAX_WRITE_ATTEMPTS",
    "ACQUIRE_TARGET_LOCK_TIMEOUT",
    "RENDER_HINT_CLEAR",
    "RENDER_HINT_VIDEO",
    "RENDER_HINT_MAPPEDWINDOW",
    "TS_VC_LISTENER_STATIC_CHANNEL",
    "WRdsGraphicsChannels_LossyChannelMaxMessageSize",
    "RFX_RDP_MSG_PREFIX",
    "RFX_GFX_MSG_PREFIX",
    "RFX_GFX_MSG_PREFIX_MASK",
    "RFX_GFX_MAX_SUPPORTED_MONITORS",
    "RFX_CLIENT_ID_LENGTH",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_CONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DISCONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RECONNECT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DELETE_SAVED_CREDENTIALS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_UPDATE_SESSION_DISPLAYSETTINGS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_ATTACH_EVENT",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_DETACH_EVENT",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_SETTINGS",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_ACTIONS",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCH_POINTER",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_SET_RDPPROPERTY",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_RDPPROPERTY",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_APPLY_SETTINGS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RETRIEVE_SETTINGS",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_SUSPEND_SCREEN_UPDATES",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_RESUME_SCREEN_UPDATES",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_EXECUTE_REMOTE_ACTION",
    "DISPID_METHOD_REMOTEDESKTOPCLIENT_GET_SNAPSHOT",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_ENABLED",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_EVENTSENABLED",
    "DISPID_PROP_REMOTEDESKTOPCLIENT_TOUCHPOINTER_POINTERSPEED",
    "DISPID_AX_CONNECTING",
    "DISPID_AX_CONNECTED",
    "DISPID_AX_LOGINCOMPLETED",
    "DISPID_AX_DISCONNECTED",
    "DISPID_AX_STATUSCHANGED",
    "DISPID_AX_AUTORECONNECTING",
    "DISPID_AX_AUTORECONNECTED",
    "DISPID_AX_DIALOGDISPLAYING",
    "DISPID_AX_DIALOGDISMISSED",
    "DISPID_AX_NETWORKSTATUSCHANGED",
    "DISPID_AX_ADMINMESSAGERECEIVED",
    "DISPID_AX_KEYCOMBINATIONPRESSED",
    "DISPID_AX_REMOTEDESKTOPSIZECHANGED",
    "DISPID_AX_TOUCHPOINTERCURSORMOVED",
    "RDCLIENT_BITMAP_RENDER_SERVICE",
    "WTS_QUERY_ALLOWED_INITIAL_APP",
    "WTS_QUERY_LOGON_SCREEN_SIZE",
    "WTS_QUERY_AUDIOENUM_DLL",
    "WTS_QUERY_MF_FORMAT_SUPPORT",
    "WRDS_SERVICE_ID_GRAPHICS_GUID",
    "PROPERTY_DYNAMIC_TIME_ZONE_INFORMATION",
    "PROPERTY_TYPE_GET_FAST_RECONNECT",
    "PROPERTY_TYPE_GET_FAST_RECONNECT_USER_SID",
    "PROPERTY_TYPE_ENABLE_UNIVERSAL_APPS_FOR_CUSTOM_SHELL",
    "CONNECTION_PROPERTY_IDLE_TIME_WARNING",
    "CONNECTION_PROPERTY_CURSOR_BLINK_DISABLED",
    "AE_POSITION_FLAGS",
    "POSITION_INVALID",
    "POSITION_DISCONTINUOUS",
    "POSITION_CONTINUOUS",
    "POSITION_QPC_ERROR",
    "AE_CURRENT_POSITION",
    "IAudioEndpoint",
    "IAudioEndpointRT",
    "IAudioInputEndpointRT",
    "IAudioOutputEndpointRT",
    "IAudioDeviceEndpoint",
    "IAudioEndpointControl",
    "HwtsVirtualChannelHandle",
    "TSUserExInterfaces",
    "ADsTSUserEx",
    "IADsTSUserEx",
    "AAAuthSchemes",
    "AA_AUTH_MIN",
    "AA_AUTH_BASIC",
    "AA_AUTH_NTLM",
    "AA_AUTH_SC",
    "AA_AUTH_LOGGEDONCREDENTIALS",
    "AA_AUTH_NEGOTIATE",
    "AA_AUTH_ANY",
    "AA_AUTH_COOKIE",
    "AA_AUTH_DIGEST",
    "AA_AUTH_ORGID",
    "AA_AUTH_CONID",
    "AA_AUTH_SSPI_NTLM",
    "AA_AUTH_MAX",
    "AAAccountingDataType",
    "AA_MAIN_SESSION_CREATION",
    "AA_SUB_SESSION_CREATION",
    "AA_SUB_SESSION_CLOSED",
    "AA_MAIN_SESSION_CLOSED",
    "AAAccountingData",
    "SESSION_TIMEOUT_ACTION_TYPE",
    "SESSION_TIMEOUT_ACTION_DISCONNECT",
    "SESSION_TIMEOUT_ACTION_SILENT_REAUTH",
    "PolicyAttributeType",
    "PolicyAttributeType_EnableAllRedirections",
    "PolicyAttributeType_DisableAllRedirections",
    "PolicyAttributeType_DriveRedirectionDisabled",
    "PolicyAttributeType_PrinterRedirectionDisabled",
    "PolicyAttributeType_PortRedirectionDisabled",
    "PolicyAttributeType_ClipboardRedirectionDisabled",
    "PolicyAttributeType_PnpRedirectionDisabled",
    "PolicyAttributeType_AllowOnlySDRServers",
    "AATrustClassID",
    "AA_UNTRUSTED",
    "AA_TRUSTEDUSER_UNTRUSTEDCLIENT",
    "AA_TRUSTEDUSER_TRUSTEDCLIENT",
    "ITSGAuthorizeConnectionSink",
    "ITSGAuthorizeResourceSink",
    "ITSGPolicyEngine",
    "ITSGAccountingEngine",
    "ITSGAuthenticateUserSink",
    "ITSGAuthenticationEngine",
    "WTS_CONNECTSTATE_CLASS",
    "WTS_CONNECTSTATE_CLASS_WTSActive",
    "WTS_CONNECTSTATE_CLASS_WTSConnected",
    "WTS_CONNECTSTATE_CLASS_WTSConnectQuery",
    "WTS_CONNECTSTATE_CLASS_WTSShadow",
    "WTS_CONNECTSTATE_CLASS_WTSDisconnected",
    "WTS_CONNECTSTATE_CLASS_WTSIdle",
    "WTS_CONNECTSTATE_CLASS_WTSListen",
    "WTS_CONNECTSTATE_CLASS_WTSReset",
    "WTS_CONNECTSTATE_CLASS_WTSDown",
    "WTS_CONNECTSTATE_CLASS_WTSInit",
    "WTS_SERVER_INFOW",
    "WTS_SERVER_INFOA",
    "WTS_SESSION_INFOW",
    "WTS_SESSION_INFOA",
    "WTS_SESSION_INFO_1W",
    "WTS_SESSION_INFO_1A",
    "WTS_PROCESS_INFOW",
    "WTS_PROCESS_INFOA",
    "WTS_INFO_CLASS",
    "WTS_INFO_CLASS_WTSInitialProgram",
    "WTS_INFO_CLASS_WTSApplicationName",
    "WTS_INFO_CLASS_WTSWorkingDirectory",
    "WTS_INFO_CLASS_WTSOEMId",
    "WTS_INFO_CLASS_WTSSessionId",
    "WTS_INFO_CLASS_WTSUserName",
    "WTS_INFO_CLASS_WTSWinStationName",
    "WTS_INFO_CLASS_WTSDomainName",
    "WTS_INFO_CLASS_WTSConnectState",
    "WTS_INFO_CLASS_WTSClientBuildNumber",
    "WTS_INFO_CLASS_WTSClientName",
    "WTS_INFO_CLASS_WTSClientDirectory",
    "WTS_INFO_CLASS_WTSClientProductId",
    "WTS_INFO_CLASS_WTSClientHardwareId",
    "WTS_INFO_CLASS_WTSClientAddress",
    "WTS_INFO_CLASS_WTSClientDisplay",
    "WTS_INFO_CLASS_WTSClientProtocolType",
    "WTS_INFO_CLASS_WTSIdleTime",
    "WTS_INFO_CLASS_WTSLogonTime",
    "WTS_INFO_CLASS_WTSIncomingBytes",
    "WTS_INFO_CLASS_WTSOutgoingBytes",
    "WTS_INFO_CLASS_WTSIncomingFrames",
    "WTS_INFO_CLASS_WTSOutgoingFrames",
    "WTS_INFO_CLASS_WTSClientInfo",
    "WTS_INFO_CLASS_WTSSessionInfo",
    "WTS_INFO_CLASS_WTSSessionInfoEx",
    "WTS_INFO_CLASS_WTSConfigInfo",
    "WTS_INFO_CLASS_WTSValidationInfo",
    "WTS_INFO_CLASS_WTSSessionAddressV4",
    "WTS_INFO_CLASS_WTSIsRemoteSession",
    "WTSCONFIGINFOW",
    "WTSCONFIGINFOA",
    "WTSINFOW",
    "WTSINFOA",
    "WTSINFOEX_LEVEL1_W",
    "WTSINFOEX_LEVEL1_A",
    "WTSINFOEX_LEVEL_W",
    "WTSINFOEX_LEVEL_A",
    "WTSINFOEXW",
    "WTSINFOEXA",
    "WTSCLIENTW",
    "WTSCLIENTA",
    "_WTS_PRODUCT_INFOA",
    "_WTS_PRODUCT_INFOW",
    "WTS_VALIDATION_INFORMATIONA",
    "WTS_VALIDATION_INFORMATIONW",
    "WTS_CLIENT_ADDRESS",
    "WTS_CLIENT_DISPLAY",
    "WTS_CONFIG_CLASS",
    "WTS_CONFIG_CLASS_WTSUserConfigInitialProgram",
    "WTS_CONFIG_CLASS_WTSUserConfigWorkingDirectory",
    "WTS_CONFIG_CLASS_WTSUserConfigfInheritInitialProgram",
    "WTS_CONFIG_CLASS_WTSUserConfigfAllowLogonTerminalServer",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsConnections",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsDisconnections",
    "WTS_CONFIG_CLASS_WTSUserConfigTimeoutSettingsIdle",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDrives",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientPrinters",
    "WTS_CONFIG_CLASS_WTSUserConfigfDeviceClientDefaultPrinter",
    "WTS_CONFIG_CLASS_WTSUserConfigBrokenTimeoutSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigReconnectSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigModemCallbackSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigModemCallbackPhoneNumber",
    "WTS_CONFIG_CLASS_WTSUserConfigShadowingSettings",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerProfilePath",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDir",
    "WTS_CONFIG_CLASS_WTSUserConfigTerminalServerHomeDirDrive",
    "WTS_CONFIG_CLASS_WTSUserConfigfTerminalServerRemoteHomeDir",
    "WTS_CONFIG_CLASS_WTSUserConfigUser",
    "WTS_CONFIG_SOURCE",
    "WTS_CONFIG_SOURCE_WTSUserConfigSourceSAM",
    "WTSUSERCONFIGA",
    "WTSUSERCONFIGW",
    "WTS_VIRTUAL_CLASS",
    "WTS_VIRTUAL_CLASS_WTSVirtualClientData",
    "WTS_VIRTUAL_CLASS_WTSVirtualFileHandle",
    "WTS_SESSION_ADDRESS",
    "WTS_PROCESS_INFO_EXW",
    "WTS_PROCESS_INFO_EXA",
    "WTS_TYPE_CLASS",
    "WTS_TYPE_CLASS_WTSTypeProcessInfoLevel0",
    "WTS_TYPE_CLASS_WTSTypeProcessInfoLevel1",
    "WTS_TYPE_CLASS_WTSTypeSessionInfoLevel1",
    "WTSLISTENERCONFIGW",
    "WTSLISTENERCONFIGA",
    "WTSSBX_MACHINE_DRAIN",
    "WTSSBX_MACHINE_DRAIN_UNSPEC",
    "WTSSBX_MACHINE_DRAIN_OFF",
    "WTSSBX_MACHINE_DRAIN_ON",
    "WTSSBX_MACHINE_SESSION_MODE",
    "WTSSBX_MACHINE_SESSION_MODE_UNSPEC",
    "WTSSBX_MACHINE_SESSION_MODE_SINGLE",
    "WTSSBX_MACHINE_SESSION_MODE_MULTIPLE",
    "WTSSBX_ADDRESS_FAMILY",
    "WTSSBX_ADDRESS_FAMILY_AF_UNSPEC",
    "WTSSBX_ADDRESS_FAMILY_AF_INET",
    "WTSSBX_ADDRESS_FAMILY_AF_INET6",
    "WTSSBX_ADDRESS_FAMILY_AF_IPX",
    "WTSSBX_ADDRESS_FAMILY_AF_NETBIOS",
    "WTSSBX_IP_ADDRESS",
    "WTSSBX_MACHINE_STATE",
    "WTSSBX_MACHINE_STATE_UNSPEC",
    "WTSSBX_MACHINE_STATE_READY",
    "WTSSBX_MACHINE_STATE_SYNCHRONIZING",
    "WTSSBX_MACHINE_CONNECT_INFO",
    "WTSSBX_MACHINE_INFO",
    "WTSSBX_SESSION_STATE",
    "WTSSBX_SESSION_STATE_UNSPEC",
    "WTSSBX_SESSION_STATE_ACTIVE",
    "WTSSBX_SESSION_STATE_DISCONNECTED",
    "WTSSBX_SESSION_INFO",
    "WTSSBX_NOTIFICATION_TYPE",
    "WTSSBX_NOTIFICATION_REMOVED",
    "WTSSBX_NOTIFICATION_CHANGED",
    "WTSSBX_NOTIFICATION_ADDED",
    "WTSSBX_NOTIFICATION_RESYNC",
    "IWTSSBPlugin",
    "CHANNEL_DEF",
    "CHANNEL_PDU_HEADER",
    "PCHANNEL_INIT_EVENT_FN",
    "PCHANNEL_OPEN_EVENT_FN",
    "PVIRTUALCHANNELINIT",
    "PVIRTUALCHANNELOPEN",
    "PVIRTUALCHANNELCLOSE",
    "PVIRTUALCHANNELWRITE",
    "CHANNEL_ENTRY_POINTS",
    "PVIRTUALCHANNELENTRY",
    "Workspace",
    "IWorkspaceClientExt",
    "IWorkspace",
    "IWorkspace2",
    "IWorkspace3",
    "IWorkspaceRegistration",
    "IWorkspaceRegistration2",
    "IWorkspaceScriptable",
    "IWorkspaceScriptable2",
    "IWorkspaceScriptable3",
    "IWorkspaceReportMessage",
    "_ITSWkspEvents",
    "TSSD_AddrV46Type",
    "TSSD_ADDR_UNDEFINED",
    "TSSD_ADDR_IPv4",
    "TSSD_ADDR_IPv6",
    "TSSB_NOTIFICATION_TYPE",
    "TSSB_NOTIFY_INVALID",
    "TSSB_NOTIFY_TARGET_CHANGE",
    "TSSB_NOTIFY_SESSION_CHANGE",
    "TSSB_NOTIFY_CONNECTION_REQUEST_CHANGE",
    "TARGET_STATE",
    "TARGET_UNKNOWN",
    "TARGET_INITIALIZING",
    "TARGET_RUNNING",
    "TARGET_DOWN",
    "TARGET_HIBERNATED",
    "TARGET_CHECKED_OUT",
    "TARGET_STOPPED",
    "TARGET_INVALID",
    "TARGET_STARTING",
    "TARGET_STOPPING",
    "TARGET_MAXSTATE",
    "TARGET_CHANGE_TYPE",
    "TARGET_CHANGE_UNSPEC",
    "TARGET_EXTERNALIP_CHANGED",
    "TARGET_INTERNALIP_CHANGED",
    "TARGET_JOINED",
    "TARGET_REMOVED",
    "TARGET_STATE_CHANGED",
    "TARGET_IDLE",
    "TARGET_PENDING",
    "TARGET_INUSE",
    "TARGET_PATCH_STATE_CHANGED",
    "TARGET_FARM_MEMBERSHIP_CHANGED",
    "TARGET_TYPE",
    "UNKNOWN",
    "FARM",
    "NONFARM",
    "TARGET_PATCH_STATE",
    "TARGET_PATCH_UNKNOWN",
    "TARGET_PATCH_NOT_STARTED",
    "TARGET_PATCH_IN_PROGRESS",
    "TARGET_PATCH_COMPLETED",
    "TARGET_PATCH_FAILED",
    "CLIENT_MESSAGE_TYPE",
    "CLIENT_MESSAGE_CONNECTION_INVALID",
    "CLIENT_MESSAGE_CONNECTION_STATUS",
    "CLIENT_MESSAGE_CONNECTION_ERROR",
    "CONNECTION_CHANGE_NOTIFICATION",
    "CONNECTION_REQUEST_INVALID",
    "CONNECTION_REQUEST_PENDING",
    "CONNECTION_REQUEST_FAILED",
    "CONNECTION_REQUEST_TIMEDOUT",
    "CONNECTION_REQUEST_SUCCEEDED",
    "CONNECTION_REQUEST_CANCELLED",
    "CONNECTION_REQUEST_LB_COMPLETED",
    "CONNECTION_REQUEST_QUERY_PL_COMPLETED",
    "CONNECTION_REQUEST_ORCH_COMPLETED",
    "RD_FARM_TYPE",
    "RD_FARM_RDSH",
    "RD_FARM_TEMP_VM",
    "RD_FARM_MANUAL_PERSONAL_VM",
    "RD_FARM_AUTO_PERSONAL_VM",
    "RD_FARM_MANUAL_PERSONAL_RDSH",
    "RD_FARM_AUTO_PERSONAL_RDSH",
    "RD_FARM_TYPE_UNKNOWN",
    "PLUGIN_TYPE",
    "UNKNOWN_PLUGIN",
    "POLICY_PLUGIN",
    "RESOURCE_PLUGIN",
    "LOAD_BALANCING_PLUGIN",
    "PLACEMENT_PLUGIN",
    "ORCHESTRATION_PLUGIN",
    "PROVISIONING_PLUGIN",
    "TASK_PLUGIN",
    "TSSESSION_STATE",
    "STATE_INVALID",
    "STATE_ACTIVE",
    "STATE_CONNECTED",
    "STATE_CONNECTQUERY",
    "STATE_SHADOW",
    "STATE_DISCONNECTED",
    "STATE_IDLE",
    "STATE_LISTEN",
    "STATE_RESET",
    "STATE_DOWN",
    "STATE_INIT",
    "STATE_MAX",
    "TARGET_OWNER",
    "OWNER_UNKNOWN",
    "OWNER_MS_TS_PLUGIN",
    "OWNER_MS_VM_PLUGIN",
    "CLIENT_DISPLAY",
    "TSSD_ConnectionPoint",
    "VM_NOTIFY_STATUS",
    "VM_NOTIFY_STATUS_PENDING",
    "VM_NOTIFY_STATUS_IN_PROGRESS",
    "VM_NOTIFY_STATUS_COMPLETE",
    "VM_NOTIFY_STATUS_FAILED",
    "VM_NOTIFY_STATUS_CANCELED",
    "VM_NOTIFY_ENTRY",
    "VM_PATCH_INFO",
    "VM_NOTIFY_INFO",
    "VM_HOST_NOTIFY_STATUS",
    "VM_HOST_STATUS_INIT_PENDING",
    "VM_HOST_STATUS_INIT_IN_PROGRESS",
    "VM_HOST_STATUS_INIT_COMPLETE",
    "VM_HOST_STATUS_INIT_FAILED",
    "RDV_TASK_STATUS",
    "RDV_TASK_STATUS_UNKNOWN",
    "RDV_TASK_STATUS_SEARCHING",
    "RDV_TASK_STATUS_DOWNLOADING",
    "RDV_TASK_STATUS_APPLYING",
    "RDV_TASK_STATUS_REBOOTING",
    "RDV_TASK_STATUS_REBOOTED",
    "RDV_TASK_STATUS_SUCCESS",
    "RDV_TASK_STATUS_FAILED",
    "RDV_TASK_STATUS_TIMEOUT",
    "TS_SB_SORT_BY",
    "TS_SB_SORT_BY_NONE",
    "TS_SB_SORT_BY_NAME",
    "TS_SB_SORT_BY_PROP",
    "ITsSbPlugin",
    "ITsSbResourcePlugin",
    "ITsSbServiceNotification",
    "ITsSbLoadBalancing",
    "ITsSbPlacement",
    "ITsSbOrchestration",
    "ITsSbEnvironment",
    "ITsSbLoadBalanceResult",
    "ITsSbTarget",
    "ITsSbSession",
    "ITsSbResourceNotification",
    "ITsSbResourceNotificationEx",
    "ITsSbTaskInfo",
    "ITsSbTaskPlugin",
    "ITsSbPropertySet",
    "ITsSbPluginPropertySet",
    "ITsSbClientConnectionPropertySet",
    "ITsSbTargetPropertySet",
    "ITsSbEnvironmentPropertySet",
    "ITsSbBaseNotifySink",
    "ITsSbPluginNotifySink",
    "ITsSbLoadBalancingNotifySink",
    "ITsSbPlacementNotifySink",
    "ITsSbOrchestrationNotifySink",
    "ITsSbTaskPluginNotifySink",
    "ITsSbClientConnection",
    "ITsSbProvider",
    "ITsSbResourcePluginStore",
    "ITsSbFilterPluginStore",
    "ITsSbGlobalStore",
    "ITsSbProvisioningPluginNotifySink",
    "ITsSbProvisioning",
    "ITsSbGenericNotifySink",
    "pluginResource",
    "ItsPubPlugin",
    "pluginResource2FileAssociation",
    "pluginResource2",
    "TSPUB_PLUGIN_PD_RESOLUTION_TYPE",
    "TSPUB_PLUGIN_PD_QUERY_OR_CREATE",
    "TSPUB_PLUGIN_PD_QUERY_EXISTING",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_TYPE",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_NEW",
    "TSPUB_PLUGIN_PD_ASSIGNMENT_EXISTING",
    "ItsPubPlugin2",
    "IWorkspaceResTypeRegistry",
    "IWTSPlugin",
    "IWTSListener",
    "IWTSListenerCallback",
    "IWTSVirtualChannelCallback",
    "IWTSVirtualChannelManager",
    "IWTSVirtualChannel",
    "IWTSPluginServiceProvider",
    "BITMAP_RENDERER_STATISTICS",
    "IWTSBitmapRenderer",
    "IWTSBitmapRendererCallback",
    "IWTSBitmapRenderService",
    "IWRdsGraphicsChannelEvents",
    "IWRdsGraphicsChannel",
    "WRdsGraphicsChannelType",
    "WRdsGraphicsChannelType_GuaranteedDelivery",
    "WRdsGraphicsChannelType_BestEffortDelivery",
    "IWRdsGraphicsChannelManager",
    "RFX_GFX_RECT",
    "RFX_GFX_MSG_HEADER",
    "RFX_GFX_MONITOR_INFO",
    "RFX_GFX_MSG_CLIENT_DESKTOP_INFO_REQUEST",
    "RFX_GFX_MSG_CLIENT_DESKTOP_INFO_RESPONSE",
    "RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_NOTIFY",
    "RFX_GFX_MSG_DESKTOP_CONFIG_CHANGE_CONFIRM",
    "RFX_GFX_MSG_DESKTOP_INPUT_RESET",
    "RFX_GFX_MSG_DISCONNECT_NOTIFY",
    "RFX_GFX_MSG_DESKTOP_RESEND_REQUEST",
    "RFX_GFX_MSG_RDP_DATA",
    "WTS_SOCKADDR",
    "WTS_SMALL_RECT",
    "WTS_RCM_SERVICE_STATE",
    "WTS_SERVICE_NONE",
    "WTS_SERVICE_START",
    "WTS_SERVICE_STOP",
    "WTS_RCM_DRAIN_STATE",
    "WTS_DRAIN_STATE_NONE",
    "WTS_DRAIN_IN_DRAIN",
    "WTS_DRAIN_NOT_IN_DRAIN",
    "WTS_SERVICE_STATE",
    "WTS_SESSION_ID",
    "WTS_USER_CREDENTIAL",
    "WTS_SYSTEMTIME",
    "WTS_TIME_ZONE_INFORMATION",
    "WRDS_DYNAMIC_TIME_ZONE_INFORMATION",
    "WTS_CLIENT_DATA",
    "WTS_USER_DATA",
    "WTS_POLICY_DATA",
    "WTS_PROTOCOL_CACHE",
    "WTS_CACHE_STATS_UN",
    "WTS_CACHE_STATS",
    "WTS_PROTOCOL_COUNTERS",
    "WTS_PROTOCOL_STATUS",
    "WTS_DISPLAY_IOCTL",
    "WTS_LOGON_ERROR_REDIRECTOR_RESPONSE",
    "WTS_LOGON_ERR_INVALID",
    "WTS_LOGON_ERR_NOT_HANDLED",
    "WTS_LOGON_ERR_HANDLED_SHOW",
    "WTS_LOGON_ERR_HANDLED_DONT_SHOW",
    "WTS_LOGON_ERR_HANDLED_DONT_SHOW_START_OVER",
    "WTS_PROPERTY_VALUE",
    "WTS_CERT_TYPE",
    "WTS_CERT_TYPE_INVALID",
    "WTS_CERT_TYPE_PROPRIETORY",
    "WTS_CERT_TYPE_X509",
    "WTS_LICENSE_CAPABILITIES",
    "WRDS_CONNECTION_SETTING_LEVEL",
    "WRDS_CONNECTION_SETTING_LEVEL_INVALID",
    "WRDS_CONNECTION_SETTING_LEVEL_1",
    "WRDS_LISTENER_SETTING_LEVEL",
    "WRDS_LISTENER_SETTING_LEVEL_INVALID",
    "WRDS_LISTENER_SETTING_LEVEL_1",
    "WRDS_SETTING_TYPE",
    "WRDS_SETTING_TYPE_INVALID",
    "WRDS_SETTING_TYPE_MACHINE",
    "WRDS_SETTING_TYPE_USER",
    "WRDS_SETTING_TYPE_SAM",
    "WRDS_SETTING_STATUS",
    "WRDS_SETTING_STATUS_NOTAPPLICABLE",
    "WRDS_SETTING_STATUS_DISABLED",
    "WRDS_SETTING_STATUS_ENABLED",
    "WRDS_SETTING_STATUS_NOTCONFIGURED",
    "WRDS_SETTING_LEVEL",
    "WRDS_SETTING_LEVEL_INVALID",
    "WRDS_SETTING_LEVEL_1",
    "WRDS_LISTENER_SETTINGS_1",
    "WRDS_LISTENER_SETTING",
    "WRDS_LISTENER_SETTINGS",
    "WRDS_CONNECTION_SETTINGS_1",
    "WRDS_SETTINGS_1",
    "WRDS_CONNECTION_SETTING",
    "WRDS_CONNECTION_SETTINGS",
    "WRDS_SETTING",
    "WRDS_SETTINGS",
    "IWTSProtocolManager",
    "IWTSProtocolListener",
    "IWTSProtocolListenerCallback",
    "IWTSProtocolConnection",
    "IWTSProtocolConnectionCallback",
    "IWTSProtocolShadowConnection",
    "IWTSProtocolShadowCallback",
    "IWTSProtocolLicenseConnection",
    "IWTSProtocolLogonErrorRedirector",
    "IWRdsProtocolSettings",
    "IWRdsProtocolManager",
    "IWRdsProtocolListener",
    "IWRdsProtocolListenerCallback",
    "IWRdsProtocolConnection",
    "IWRdsProtocolConnectionCallback",
    "IWRdsProtocolShadowConnection",
    "IWRdsProtocolShadowCallback",
    "IWRdsProtocolLicenseConnection",
    "IWRdsProtocolLogonErrorRedirector",
    "IWRdsWddmIddProps",
    "IWRdsProtocolConnectionSettings",
    "IWRdsEnhancedFastReconnectArbitrator",
    "PasswordEncodingType",
    "PasswordEncodingType_PasswordEncodingUTF8",
    "PasswordEncodingType_PasswordEncodingUTF16LE",
    "PasswordEncodingType_PasswordEncodingUTF16BE",
    "IRemoteDesktopClientSettings",
    "RemoteActionType",
    "RemoteActionType_RemoteActionCharms",
    "RemoteActionType_RemoteActionAppbar",
    "RemoteActionType_RemoteActionSnap",
    "RemoteActionType_RemoteActionStartScreen",
    "RemoteActionType_RemoteActionAppSwitch",
    "SnapshotEncodingType",
    "SnapshotEncodingType_SnapshotEncodingDataUri",
    "SnapshotFormatType",
    "SnapshotFormatType_SnapshotFormatPng",
    "SnapshotFormatType_SnapshotFormatJpeg",
    "SnapshotFormatType_SnapshotFormatBmp",
    "IRemoteDesktopClientActions",
    "IRemoteDesktopClientTouchPointer",
    "KeyCombinationType",
    "KeyCombinationType_KeyCombinationHome",
    "KeyCombinationType_KeyCombinationLeft",
    "KeyCombinationType_KeyCombinationUp",
    "KeyCombinationType_KeyCombinationRight",
    "KeyCombinationType_KeyCombinationDown",
    "KeyCombinationType_KeyCombinationScroll",
    "IRemoteDesktopClient",
    "IRemoteSystemAdditionalInfoProvider",
    "WTSSESSION_NOTIFICATION",
    "WTSStopRemoteControlSession",
    "WTSStartRemoteControlSessionW",
    "WTSStartRemoteControlSession",
    "WTSStartRemoteControlSessionA",
    "WTSConnectSessionA",
    "WTSConnectSessionW",
    "WTSConnectSession",
    "WTSEnumerateServersW",
    "WTSEnumerateServers",
    "WTSEnumerateServersA",
    "WTSOpenServerW",
    "WTSOpenServer",
    "WTSOpenServerA",
    "WTSOpenServerExW",
    "WTSOpenServerEx",
    "WTSOpenServerExA",
    "WTSCloseServer",
    "WTSEnumerateSessionsW",
    "WTSEnumerateSessions",
    "WTSEnumerateSessionsA",
    "WTSEnumerateSessionsExW",
    "WTSEnumerateSessionsEx",
    "WTSEnumerateSessionsExA",
    "WTSEnumerateProcessesW",
    "WTSEnumerateProcesses",
    "WTSEnumerateProcessesA",
    "WTSTerminateProcess",
    "WTSQuerySessionInformationW",
    "WTSQuerySessionInformation",
    "WTSQuerySessionInformationA",
    "WTSQueryUserConfigW",
    "WTSQueryUserConfig",
    "WTSQueryUserConfigA",
    "WTSSetUserConfigW",
    "WTSSetUserConfig",
    "WTSSetUserConfigA",
    "WTSSendMessageW",
    "WTSSendMessage",
    "WTSSendMessageA",
    "WTSDisconnectSession",
    "WTSLogoffSession",
    "WTSShutdownSystem",
    "WTSWaitSystemEvent",
    "WTSVirtualChannelOpen",
    "WTSVirtualChannelOpenEx",
    "WTSVirtualChannelClose",
    "WTSVirtualChannelRead",
    "WTSVirtualChannelWrite",
    "WTSVirtualChannelPurgeInput",
    "WTSVirtualChannelPurgeOutput",
    "WTSVirtualChannelQuery",
    "WTSFreeMemory",
    "WTSRegisterSessionNotification",
    "WTSUnRegisterSessionNotification",
    "WTSRegisterSessionNotificationEx",
    "WTSUnRegisterSessionNotificationEx",
    "WTSQueryUserToken",
    "WTSFreeMemoryExW",
    "WTSFreeMemoryEx",
    "WTSFreeMemoryExA",
    "WTSEnumerateProcessesExW",
    "WTSEnumerateProcessesEx",
    "WTSEnumerateProcessesExA",
    "WTSEnumerateListenersW",
    "WTSEnumerateListeners",
    "WTSEnumerateListenersA",
    "WTSQueryListenerConfigW",
    "WTSQueryListenerConfig",
    "WTSQueryListenerConfigA",
    "WTSCreateListenerW",
    "WTSCreateListener",
    "WTSCreateListenerA",
    "WTSSetListenerSecurityW",
    "WTSSetListenerSecurity",
    "WTSSetListenerSecurityA",
    "WTSGetListenerSecurityW",
    "WTSGetListenerSecurity",
    "WTSGetListenerSecurityA",
    "WTSEnableChildSessions",
    "WTSIsChildSessionsEnabled",
    "WTSGetChildSessionId",
    "WTSSetRenderHint",
    "ProcessIdToSessionId",
    "WTSGetActiveConsoleSessionId",
]
