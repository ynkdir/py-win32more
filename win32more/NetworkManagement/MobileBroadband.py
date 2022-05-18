from win32more import *
import win32more.Foundation
import win32more.NetworkManagement.MobileBroadband
import win32more.System.Com

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
MbnConnectionProfileManager = Guid('bdfee05a-4418-11dd-90ed-001c257ccff1')
MbnInterfaceManager = Guid('bdfee05b-4418-11dd-90ed-001c257ccff1')
MbnConnectionManager = Guid('bdfee05c-4418-11dd-90ed-001c257ccff1')
MbnDeviceServicesManager = Guid('2269daa3-2a9f-4165-a501-ce00a6f7a75b')
def _define_IDummyMBNUCMExt_head():
    class IDummyMBNUCMExt(win32more.System.Com.IDispatch_head):
        Guid = Guid('dcbbbab6-ffff-4bbb-aaee-338e368af6fa')
    return IDummyMBNUCMExt
def _define_IDummyMBNUCMExt():
    IDummyMBNUCMExt = win32more.NetworkManagement.MobileBroadband.IDummyMBNUCMExt_head
    return IDummyMBNUCMExt
MBN_SIGNAL_CONSTANTS = Int32
MBN_RSSI_DEFAULT = -1
MBN_RSSI_DISABLE = 0
MBN_RSSI_UNKNOWN = 99
MBN_ERROR_RATE_UNKNOWN = 99
MBN_CELLULAR_CLASS = Int32
MBN_CELLULAR_CLASS_NONE = 0
MBN_CELLULAR_CLASS_GSM = 1
MBN_CELLULAR_CLASS_CDMA = 2
MBN_VOICE_CLASS = Int32
MBN_VOICE_CLASS_NONE = 0
MBN_VOICE_CLASS_NO_VOICE = 1
MBN_VOICE_CLASS_SEPARATE_VOICE_DATA = 2
MBN_VOICE_CLASS_SIMULTANEOUS_VOICE_DATA = 3
MBN_PROVIDER_STATE = Int32
MBN_PROVIDER_STATE_NONE = 0
MBN_PROVIDER_STATE_HOME = 1
MBN_PROVIDER_STATE_FORBIDDEN = 2
MBN_PROVIDER_STATE_PREFERRED = 4
MBN_PROVIDER_STATE_VISIBLE = 8
MBN_PROVIDER_STATE_REGISTERED = 16
MBN_PROVIDER_STATE_PREFERRED_MULTICARRIER = 32
MBN_PROVIDER_CONSTANTS = Int32
MBN_PROVIDERNAME_LEN = 20
MBN_PROVIDERID_LEN = 6
MBN_INTERFACE_CAPS_CONSTANTS = Int32
MBN_DEVICEID_LEN = 18
MBN_MANUFACTURER_LEN = 32
MBN_MODEL_LEN = 32
MBN_FIRMWARE_LEN = 32
MBN_DATA_CLASS = Int32
MBN_DATA_CLASS_NONE = 0
MBN_DATA_CLASS_GPRS = 1
MBN_DATA_CLASS_EDGE = 2
MBN_DATA_CLASS_UMTS = 4
MBN_DATA_CLASS_HSDPA = 8
MBN_DATA_CLASS_HSUPA = 16
MBN_DATA_CLASS_LTE = 32
MBN_DATA_CLASS_5G_NSA = 64
MBN_DATA_CLASS_5G_SA = 128
MBN_DATA_CLASS_1XRTT = 65536
MBN_DATA_CLASS_1XEVDO = 131072
MBN_DATA_CLASS_1XEVDO_REVA = 262144
MBN_DATA_CLASS_1XEVDV = 524288
MBN_DATA_CLASS_3XRTT = 1048576
MBN_DATA_CLASS_1XEVDO_REVB = 2097152
MBN_DATA_CLASS_UMB = 4194304
MBN_DATA_CLASS_CUSTOM = -2147483648
MBN_CTRL_CAPS = Int32
MBN_CTRL_CAPS_NONE = 0
MBN_CTRL_CAPS_REG_MANUAL = 1
MBN_CTRL_CAPS_HW_RADIO_SWITCH = 2
MBN_CTRL_CAPS_CDMA_MOBILE_IP = 4
MBN_CTRL_CAPS_CDMA_SIMPLE_IP = 8
MBN_CTRL_CAPS_PROTECT_UNIQUEID = 16
MBN_CTRL_CAPS_MODEL_MULTI_CARRIER = 32
MBN_CTRL_CAPS_USSD = 64
MBN_CTRL_CAPS_MULTI_MODE = 128
MBN_SMS_CAPS = Int32
MBN_SMS_CAPS_NONE = 0
MBN_SMS_CAPS_PDU_RECEIVE = 1
MBN_SMS_CAPS_PDU_SEND = 2
MBN_SMS_CAPS_TEXT_RECEIVE = 4
MBN_SMS_CAPS_TEXT_SEND = 8
MBN_BAND_CLASS = Int32
MBN_BAND_CLASS_NONE = 0
MBN_BAND_CLASS_0 = 1
MBN_BAND_CLASS_I = 2
MBN_BAND_CLASS_II = 4
MBN_BAND_CLASS_III = 8
MBN_BAND_CLASS_IV = 16
MBN_BAND_CLASS_V = 32
MBN_BAND_CLASS_VI = 64
MBN_BAND_CLASS_VII = 128
MBN_BAND_CLASS_VIII = 256
MBN_BAND_CLASS_IX = 512
MBN_BAND_CLASS_X = 1024
MBN_BAND_CLASS_XI = 2048
MBN_BAND_CLASS_XII = 4096
MBN_BAND_CLASS_XIII = 8192
MBN_BAND_CLASS_XIV = 16384
MBN_BAND_CLASS_XV = 32768
MBN_BAND_CLASS_XVI = 65536
MBN_BAND_CLASS_XVII = 131072
MBN_BAND_CLASS_CUSTOM = -2147483648
def _define_MBN_INTERFACE_CAPS_head():
    class MBN_INTERFACE_CAPS(Structure):
        pass
    return MBN_INTERFACE_CAPS
def _define_MBN_INTERFACE_CAPS():
    MBN_INTERFACE_CAPS = win32more.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_head
    MBN_INTERFACE_CAPS._fields_ = [
        ("cellularClass", win32more.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS),
        ("voiceClass", win32more.NetworkManagement.MobileBroadband.MBN_VOICE_CLASS),
        ("dataClass", UInt32),
        ("customDataClass", win32more.Foundation.BSTR),
        ("gsmBandClass", UInt32),
        ("cdmaBandClass", UInt32),
        ("customBandClass", win32more.Foundation.BSTR),
        ("smsCaps", UInt32),
        ("controlCaps", UInt32),
        ("deviceID", win32more.Foundation.BSTR),
        ("manufacturer", win32more.Foundation.BSTR),
        ("model", win32more.Foundation.BSTR),
        ("firmwareInfo", win32more.Foundation.BSTR),
    ]
    return MBN_INTERFACE_CAPS
def _define_MBN_PROVIDER_head():
    class MBN_PROVIDER(Structure):
        pass
    return MBN_PROVIDER
def _define_MBN_PROVIDER():
    MBN_PROVIDER = win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER_head
    MBN_PROVIDER._fields_ = [
        ("providerID", win32more.Foundation.BSTR),
        ("providerState", UInt32),
        ("providerName", win32more.Foundation.BSTR),
        ("dataClass", UInt32),
    ]
    return MBN_PROVIDER
def _define_MBN_PROVIDER2_head():
    class MBN_PROVIDER2(Structure):
        pass
    return MBN_PROVIDER2
def _define_MBN_PROVIDER2():
    MBN_PROVIDER2 = win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER2_head
    MBN_PROVIDER2._fields_ = [
        ("provider", win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER),
        ("cellularClass", win32more.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS),
        ("signalStrength", UInt32),
        ("signalError", UInt32),
    ]
    return MBN_PROVIDER2
MBN_READY_STATE = Int32
MBN_READY_STATE_OFF = 0
MBN_READY_STATE_INITIALIZED = 1
MBN_READY_STATE_SIM_NOT_INSERTED = 2
MBN_READY_STATE_BAD_SIM = 3
MBN_READY_STATE_FAILURE = 4
MBN_READY_STATE_NOT_ACTIVATED = 5
MBN_READY_STATE_DEVICE_LOCKED = 6
MBN_READY_STATE_DEVICE_BLOCKED = 7
MBN_READY_STATE_NO_ESIM_PROFILE = 8
MBN_ACTIVATION_STATE = Int32
MBN_ACTIVATION_STATE_NONE = 0
MBN_ACTIVATION_STATE_ACTIVATED = 1
MBN_ACTIVATION_STATE_ACTIVATING = 2
MBN_ACTIVATION_STATE_DEACTIVATED = 3
MBN_ACTIVATION_STATE_DEACTIVATING = 4
MBN_CONNECTION_MODE = Int32
MBN_CONNECTION_MODE_PROFILE = 0
MBN_CONNECTION_MODE_TMP_PROFILE = 1
MBN_VOICE_CALL_STATE = Int32
MBN_VOICE_CALL_STATE_NONE = 0
MBN_VOICE_CALL_STATE_IN_PROGRESS = 1
MBN_VOICE_CALL_STATE_HANGUP = 2
MBN_REGISTRATION_CONSTANTS = Int32
MBN_ROAMTEXT_LEN = 64
MBN_CDMA_DEFAULT_PROVIDER_ID = 0
MBN_REGISTER_STATE = Int32
MBN_REGISTER_STATE_NONE = 0
MBN_REGISTER_STATE_DEREGISTERED = 1
MBN_REGISTER_STATE_SEARCHING = 2
MBN_REGISTER_STATE_HOME = 3
MBN_REGISTER_STATE_ROAMING = 4
MBN_REGISTER_STATE_PARTNER = 5
MBN_REGISTER_STATE_DENIED = 6
MBN_REGISTER_MODE = Int32
MBN_REGISTER_MODE_NONE = 0
MBN_REGISTER_MODE_AUTOMATIC = 1
MBN_REGISTER_MODE_MANUAL = 2
MBN_PIN_CONSTANTS = Int32
MBN_ATTEMPTS_REMAINING_UNKNOWN = -1
MBN_PIN_LENGTH_UNKNOWN = -1
MBN_PIN_STATE = Int32
MBN_PIN_STATE_NONE = 0
MBN_PIN_STATE_ENTER = 1
MBN_PIN_STATE_UNBLOCK = 2
MBN_PIN_TYPE = Int32
MBN_PIN_TYPE_NONE = 0
MBN_PIN_TYPE_CUSTOM = 1
MBN_PIN_TYPE_PIN1 = 2
MBN_PIN_TYPE_PIN2 = 3
MBN_PIN_TYPE_DEVICE_SIM_PIN = 4
MBN_PIN_TYPE_DEVICE_FIRST_SIM_PIN = 5
MBN_PIN_TYPE_NETWORK_PIN = 6
MBN_PIN_TYPE_NETWORK_SUBSET_PIN = 7
MBN_PIN_TYPE_SVC_PROVIDER_PIN = 8
MBN_PIN_TYPE_CORPORATE_PIN = 9
MBN_PIN_TYPE_SUBSIDY_LOCK = 10
def _define_MBN_PIN_INFO_head():
    class MBN_PIN_INFO(Structure):
        pass
    return MBN_PIN_INFO
def _define_MBN_PIN_INFO():
    MBN_PIN_INFO = win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head
    MBN_PIN_INFO._fields_ = [
        ("pinState", win32more.NetworkManagement.MobileBroadband.MBN_PIN_STATE),
        ("pinType", win32more.NetworkManagement.MobileBroadband.MBN_PIN_TYPE),
        ("attemptsRemaining", UInt32),
    ]
    return MBN_PIN_INFO
MBN_PIN_MODE = Int32
MBN_PIN_MODE_ENABLED = 1
MBN_PIN_MODE_DISABLED = 2
MBN_PIN_FORMAT = Int32
MBN_PIN_FORMAT_NONE = 0
MBN_PIN_FORMAT_NUMERIC = 1
MBN_PIN_FORMAT_ALPHANUMERIC = 2
MBN_CONTEXT_CONSTANTS = Int32
MBN_ACCESSSTRING_LEN = 100
MBN_USERNAME_LEN = 255
MBN_PASSWORD_LEN = 255
MBN_CONTEXT_ID_APPEND = -1
MBN_AUTH_PROTOCOL = Int32
MBN_AUTH_PROTOCOL_NONE = 0
MBN_AUTH_PROTOCOL_PAP = 1
MBN_AUTH_PROTOCOL_CHAP = 2
MBN_AUTH_PROTOCOL_MSCHAPV2 = 3
MBN_COMPRESSION = Int32
MBN_COMPRESSION_NONE = 0
MBN_COMPRESSION_ENABLE = 1
MBN_CONTEXT_TYPE = Int32
MBN_CONTEXT_TYPE_NONE = 0
MBN_CONTEXT_TYPE_INTERNET = 1
MBN_CONTEXT_TYPE_VPN = 2
MBN_CONTEXT_TYPE_VOICE = 3
MBN_CONTEXT_TYPE_VIDEO_SHARE = 4
MBN_CONTEXT_TYPE_CUSTOM = 5
MBN_CONTEXT_TYPE_PURCHASE = 6
def _define_MBN_CONTEXT_head():
    class MBN_CONTEXT(Structure):
        pass
    return MBN_CONTEXT
def _define_MBN_CONTEXT():
    MBN_CONTEXT = win32more.NetworkManagement.MobileBroadband.MBN_CONTEXT_head
    MBN_CONTEXT._fields_ = [
        ("contextID", UInt32),
        ("contextType", win32more.NetworkManagement.MobileBroadband.MBN_CONTEXT_TYPE),
        ("accessString", win32more.Foundation.BSTR),
        ("userName", win32more.Foundation.BSTR),
        ("password", win32more.Foundation.BSTR),
        ("compression", win32more.NetworkManagement.MobileBroadband.MBN_COMPRESSION),
        ("authType", win32more.NetworkManagement.MobileBroadband.MBN_AUTH_PROTOCOL),
    ]
    return MBN_CONTEXT
WWAEXT_SMS_CONSTANTS = Int32
MBN_MESSAGE_INDEX_NONE = 0
MBN_CDMA_SHORT_MSG_SIZE_UNKNOWN = 0
MBN_CDMA_SHORT_MSG_SIZE_MAX = 160
MBN_MSG_STATUS = Int32
MBN_MSG_STATUS_NEW = 0
MBN_MSG_STATUS_OLD = 1
MBN_MSG_STATUS_DRAFT = 2
MBN_MSG_STATUS_SENT = 3
MBN_SMS_CDMA_LANG = Int32
MBN_SMS_CDMA_LANG_NONE = 0
MBN_SMS_CDMA_LANG_ENGLISH = 1
MBN_SMS_CDMA_LANG_FRENCH = 2
MBN_SMS_CDMA_LANG_SPANISH = 3
MBN_SMS_CDMA_LANG_JAPANESE = 4
MBN_SMS_CDMA_LANG_KOREAN = 5
MBN_SMS_CDMA_LANG_CHINESE = 6
MBN_SMS_CDMA_LANG_HEBREW = 7
MBN_SMS_CDMA_ENCODING = Int32
MBN_SMS_CDMA_ENCODING_OCTET = 0
MBN_SMS_CDMA_ENCODING_EPM = 1
MBN_SMS_CDMA_ENCODING_7BIT_ASCII = 2
MBN_SMS_CDMA_ENCODING_IA5 = 3
MBN_SMS_CDMA_ENCODING_UNICODE = 4
MBN_SMS_CDMA_ENCODING_SHIFT_JIS = 5
MBN_SMS_CDMA_ENCODING_KOREAN = 6
MBN_SMS_CDMA_ENCODING_LATIN_HEBREW = 7
MBN_SMS_CDMA_ENCODING_LATIN = 8
MBN_SMS_CDMA_ENCODING_GSM_7BIT = 9
MBN_SMS_FLAG = Int32
MBN_SMS_FLAG_ALL = 0
MBN_SMS_FLAG_INDEX = 1
MBN_SMS_FLAG_NEW = 2
MBN_SMS_FLAG_OLD = 3
MBN_SMS_FLAG_SENT = 4
MBN_SMS_FLAG_DRAFT = 5
def _define_MBN_SMS_FILTER_head():
    class MBN_SMS_FILTER(Structure):
        pass
    return MBN_SMS_FILTER
def _define_MBN_SMS_FILTER():
    MBN_SMS_FILTER = win32more.NetworkManagement.MobileBroadband.MBN_SMS_FILTER_head
    MBN_SMS_FILTER._fields_ = [
        ("flag", win32more.NetworkManagement.MobileBroadband.MBN_SMS_FLAG),
        ("messageIndex", UInt32),
    ]
    return MBN_SMS_FILTER
MBN_SMS_STATUS_FLAG = Int32
MBN_SMS_FLAG_NONE = 0
MBN_SMS_FLAG_MESSAGE_STORE_FULL = 1
MBN_SMS_FLAG_NEW_MESSAGE = 2
def _define_MBN_SMS_STATUS_INFO_head():
    class MBN_SMS_STATUS_INFO(Structure):
        pass
    return MBN_SMS_STATUS_INFO
def _define_MBN_SMS_STATUS_INFO():
    MBN_SMS_STATUS_INFO = win32more.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_INFO_head
    MBN_SMS_STATUS_INFO._fields_ = [
        ("flag", UInt32),
        ("messageIndex", UInt32),
    ]
    return MBN_SMS_STATUS_INFO
MBN_SMS_FORMAT = Int32
MBN_SMS_FORMAT_NONE = 0
MBN_SMS_FORMAT_PDU = 1
MBN_SMS_FORMAT_TEXT = 2
MBN_RADIO = Int32
MBN_RADIO_OFF = 0
MBN_RADIO_ON = 1
MBN_DEVICE_SERVICE_SESSIONS_STATE = Int32
MBN_DEVICE_SERVICE_SESSIONS_RESTORED = 0
def _define_MBN_DEVICE_SERVICE_head():
    class MBN_DEVICE_SERVICE(Structure):
        pass
    return MBN_DEVICE_SERVICE
def _define_MBN_DEVICE_SERVICE():
    MBN_DEVICE_SERVICE = win32more.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICE_head
    MBN_DEVICE_SERVICE._fields_ = [
        ("deviceServiceID", win32more.Foundation.BSTR),
        ("dataWriteSupported", Int16),
        ("dataReadSupported", Int16),
    ]
    return MBN_DEVICE_SERVICE
MBN_DEVICE_SERVICES_INTERFACE_STATE = Int32
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_ARRIVAL = 0
MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_REMOVAL = 1
def _define_IMbnConnection_head():
    class IMbnConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200d-4bbb-aaee-338e368af6fa')
    return IMbnConnection
def _define_IMbnConnection():
    IMbnConnection = win32more.NetworkManagement.MobileBroadband.IMbnConnection_head
    IMbnConnection.get_ConnectionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_ConnectionID', ((1, 'ConnectionID'),)))
    IMbnConnection.get_InterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_InterfaceID', ((1, 'InterfaceID'),)))
    IMbnConnection.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_CONNECTION_MODE,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(5, 'Connect', ((1, 'connectionMode'),(1, 'strProfile'),(1, 'requestID'),)))
    IMbnConnection.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'Disconnect', ((1, 'requestID'),)))
    IMbnConnection.GetConnectionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_ACTIVATION_STATE),POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetConnectionState', ((1, 'ConnectionState'),(1, 'ProfileName'),)))
    IMbnConnection.GetVoiceCallState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_VOICE_CALL_STATE), use_last_error=False)(8, 'GetVoiceCallState', ((1, 'voiceCallState'),)))
    IMbnConnection.GetActivationNetworkError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetActivationNetworkError', ((1, 'networkError'),)))
    return IMbnConnection
def _define_IMbnConnectionEvents_head():
    class IMbnConnectionEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200e-4bbb-aaee-338e368af6fa')
    return IMbnConnectionEvents
def _define_IMbnConnectionEvents():
    IMbnConnectionEvents = win32more.NetworkManagement.MobileBroadband.IMbnConnectionEvents_head
    IMbnConnectionEvents.OnConnectComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnConnectComplete', ((1, 'newConnection'),(1, 'requestID'),(1, 'status'),)))
    IMbnConnectionEvents.OnDisconnectComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnDisconnectComplete', ((1, 'newConnection'),(1, 'requestID'),(1, 'status'),)))
    IMbnConnectionEvents.OnConnectStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head, use_last_error=False)(5, 'OnConnectStateChange', ((1, 'newConnection'),)))
    IMbnConnectionEvents.OnVoiceCallStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head, use_last_error=False)(6, 'OnVoiceCallStateChange', ((1, 'newConnection'),)))
    return IMbnConnectionEvents
def _define_IMbnInterface_head():
    class IMbnInterface(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2001-4bbb-aaee-338e368af6fa')
    return IMbnInterface
def _define_IMbnInterface():
    IMbnInterface = win32more.NetworkManagement.MobileBroadband.IMbnInterface_head
    IMbnInterface.get_InterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_InterfaceID', ((1, 'InterfaceID'),)))
    IMbnInterface.GetInterfaceCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_head), use_last_error=False)(4, 'GetInterfaceCapability', ((1, 'interfaceCaps'),)))
    IMbnInterface.GetSubscriberInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnSubscriberInformation_head), use_last_error=False)(5, 'GetSubscriberInformation', ((1, 'subscriberInformation'),)))
    IMbnInterface.GetReadyState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_READY_STATE), use_last_error=False)(6, 'GetReadyState', ((1, 'readyState'),)))
    IMbnInterface.InEmergencyMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'InEmergencyMode', ((1, 'emergencyMode'),)))
    IMbnInterface.GetHomeProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER_head), use_last_error=False)(8, 'GetHomeProvider', ((1, 'homeProvider'),)))
    IMbnInterface.GetPreferredProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(9, 'GetPreferredProviders', ((1, 'preferredProviders'),)))
    IMbnInterface.SetPreferredProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(10, 'SetPreferredProviders', ((1, 'preferredProviders'),(1, 'requestID'),)))
    IMbnInterface.GetVisibleProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(11, 'GetVisibleProviders', ((1, 'age'),(1, 'visibleProviders'),)))
    IMbnInterface.ScanNetwork = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'ScanNetwork', ((1, 'requestID'),)))
    IMbnInterface.GetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnConnection_head), use_last_error=False)(13, 'GetConnection', ((1, 'mbnConnection'),)))
    return IMbnInterface
def _define_IMbnInterfaceEvents_head():
    class IMbnInterfaceEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2002-4bbb-aaee-338e368af6fa')
    return IMbnInterfaceEvents
def _define_IMbnInterfaceEvents():
    IMbnInterfaceEvents = win32more.NetworkManagement.MobileBroadband.IMbnInterfaceEvents_head
    IMbnInterfaceEvents.OnInterfaceCapabilityAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(3, 'OnInterfaceCapabilityAvailable', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnSubscriberInformationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(4, 'OnSubscriberInformationChange', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnReadyStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(5, 'OnReadyStateChange', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnEmergencyModeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(6, 'OnEmergencyModeChange', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnHomeProviderAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(7, 'OnHomeProviderAvailable', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnPreferredProvidersChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(8, 'OnPreferredProvidersChange', ((1, 'newInterface'),)))
    IMbnInterfaceEvents.OnSetPreferredProvidersComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(9, 'OnSetPreferredProvidersComplete', ((1, 'newInterface'),(1, 'requestID'),(1, 'status'),)))
    IMbnInterfaceEvents.OnScanNetworkComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(10, 'OnScanNetworkComplete', ((1, 'newInterface'),(1, 'requestID'),(1, 'status'),)))
    return IMbnInterfaceEvents
def _define_IMbnInterfaceManager_head():
    class IMbnInterfaceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201b-4bbb-aaee-338e368af6fa')
    return IMbnInterfaceManager
def _define_IMbnInterfaceManager():
    IMbnInterfaceManager = win32more.NetworkManagement.MobileBroadband.IMbnInterfaceManager_head
    IMbnInterfaceManager.GetInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnInterface_head), use_last_error=False)(3, 'GetInterface', ((1, 'interfaceID'),(1, 'mbnInterface'),)))
    IMbnInterfaceManager.GetInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetInterfaces', ((1, 'mbnInterfaces'),)))
    return IMbnInterfaceManager
def _define_IMbnInterfaceManagerEvents_head():
    class IMbnInterfaceManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201c-4bbb-aaee-338e368af6fa')
    return IMbnInterfaceManagerEvents
def _define_IMbnInterfaceManagerEvents():
    IMbnInterfaceManagerEvents = win32more.NetworkManagement.MobileBroadband.IMbnInterfaceManagerEvents_head
    IMbnInterfaceManagerEvents.OnInterfaceArrival = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(3, 'OnInterfaceArrival', ((1, 'newInterface'),)))
    IMbnInterfaceManagerEvents.OnInterfaceRemoval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head, use_last_error=False)(4, 'OnInterfaceRemoval', ((1, 'oldInterface'),)))
    return IMbnInterfaceManagerEvents
def _define_IMbnRegistration_head():
    class IMbnRegistration(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2009-4bbb-aaee-338e368af6fa')
    return IMbnRegistration
def _define_IMbnRegistration():
    IMbnRegistration = win32more.NetworkManagement.MobileBroadband.IMbnRegistration_head
    IMbnRegistration.GetRegisterState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_REGISTER_STATE), use_last_error=False)(3, 'GetRegisterState', ((1, 'registerState'),)))
    IMbnRegistration.GetRegisterMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE), use_last_error=False)(4, 'GetRegisterMode', ((1, 'registerMode'),)))
    IMbnRegistration.GetProviderID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetProviderID', ((1, 'providerID'),)))
    IMbnRegistration.GetProviderName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetProviderName', ((1, 'providerName'),)))
    IMbnRegistration.GetRoamingText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetRoamingText', ((1, 'roamingText'),)))
    IMbnRegistration.GetAvailableDataClasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetAvailableDataClasses', ((1, 'availableDataClasses'),)))
    IMbnRegistration.GetCurrentDataClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetCurrentDataClass', ((1, 'currentDataClass'),)))
    IMbnRegistration.GetRegistrationNetworkError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetRegistrationNetworkError', ((1, 'registrationNetworkError'),)))
    IMbnRegistration.GetPacketAttachNetworkError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetPacketAttachNetworkError', ((1, 'packetAttachNetworkError'),)))
    IMbnRegistration.SetRegisterMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_REGISTER_MODE,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(12, 'SetRegisterMode', ((1, 'registerMode'),(1, 'providerID'),(1, 'dataClass'),(1, 'requestID'),)))
    return IMbnRegistration
def _define_IMbnRegistrationEvents_head():
    class IMbnRegistrationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200a-4bbb-aaee-338e368af6fa')
    return IMbnRegistrationEvents
def _define_IMbnRegistrationEvents():
    IMbnRegistrationEvents = win32more.NetworkManagement.MobileBroadband.IMbnRegistrationEvents_head
    IMbnRegistrationEvents.OnRegisterModeAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRegistration_head, use_last_error=False)(3, 'OnRegisterModeAvailable', ((1, 'newInterface'),)))
    IMbnRegistrationEvents.OnRegisterStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRegistration_head, use_last_error=False)(4, 'OnRegisterStateChange', ((1, 'newInterface'),)))
    IMbnRegistrationEvents.OnPacketServiceStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRegistration_head, use_last_error=False)(5, 'OnPacketServiceStateChange', ((1, 'newInterface'),)))
    IMbnRegistrationEvents.OnSetRegisterModeComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRegistration_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnSetRegisterModeComplete', ((1, 'newInterface'),(1, 'requestID'),(1, 'status'),)))
    return IMbnRegistrationEvents
def _define_IMbnConnectionManager_head():
    class IMbnConnectionManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201d-4bbb-aaee-338e368af6fa')
    return IMbnConnectionManager
def _define_IMbnConnectionManager():
    IMbnConnectionManager = win32more.NetworkManagement.MobileBroadband.IMbnConnectionManager_head
    IMbnConnectionManager.GetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnConnection_head), use_last_error=False)(3, 'GetConnection', ((1, 'connectionID'),(1, 'mbnConnection'),)))
    IMbnConnectionManager.GetConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetConnections', ((1, 'mbnConnections'),)))
    return IMbnConnectionManager
def _define_IMbnConnectionManagerEvents_head():
    class IMbnConnectionManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201e-4bbb-aaee-338e368af6fa')
    return IMbnConnectionManagerEvents
def _define_IMbnConnectionManagerEvents():
    IMbnConnectionManagerEvents = win32more.NetworkManagement.MobileBroadband.IMbnConnectionManagerEvents_head
    IMbnConnectionManagerEvents.OnConnectionArrival = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head, use_last_error=False)(3, 'OnConnectionArrival', ((1, 'newConnection'),)))
    IMbnConnectionManagerEvents.OnConnectionRemoval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnection_head, use_last_error=False)(4, 'OnConnectionRemoval', ((1, 'oldConnection'),)))
    return IMbnConnectionManagerEvents
def _define_IMbnPinManager_head():
    class IMbnPinManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2005-4bbb-aaee-338e368af6fa')
    return IMbnPinManager
def _define_IMbnPinManager():
    IMbnPinManager = win32more.NetworkManagement.MobileBroadband.IMbnPinManager_head
    IMbnPinManager.GetPinList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetPinList', ((1, 'pinList'),)))
    IMbnPinManager.GetPin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_PIN_TYPE,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnPin_head), use_last_error=False)(4, 'GetPin', ((1, 'pinType'),(1, 'pin'),)))
    IMbnPinManager.GetPinState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetPinState', ((1, 'requestID'),)))
    return IMbnPinManager
def _define_IMbnPinManagerEvents_head():
    class IMbnPinManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2006-4bbb-aaee-338e368af6fa')
    return IMbnPinManagerEvents
def _define_IMbnPinManagerEvents():
    IMbnPinManagerEvents = win32more.NetworkManagement.MobileBroadband.IMbnPinManagerEvents_head
    IMbnPinManagerEvents.OnPinListAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPinManager_head, use_last_error=False)(3, 'OnPinListAvailable', ((1, 'pinManager'),)))
    IMbnPinManagerEvents.OnGetPinStateComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPinManager_head,win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnGetPinStateComplete', ((1, 'pinManager'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    return IMbnPinManagerEvents
def _define_IMbnPinEvents_head():
    class IMbnPinEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2008-4bbb-aaee-338e368af6fa')
    return IMbnPinEvents
def _define_IMbnPinEvents():
    IMbnPinEvents = win32more.NetworkManagement.MobileBroadband.IMbnPinEvents_head
    IMbnPinEvents.OnEnableComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPin_head,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnEnableComplete', ((1, 'pin'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    IMbnPinEvents.OnDisableComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPin_head,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnDisableComplete', ((1, 'pin'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    IMbnPinEvents.OnEnterComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPin_head,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(5, 'OnEnterComplete', ((1, 'Pin'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    IMbnPinEvents.OnChangeComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPin_head,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnChangeComplete', ((1, 'Pin'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    IMbnPinEvents.OnUnblockComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnPin_head,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_INFO_head),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(7, 'OnUnblockComplete', ((1, 'Pin'),(1, 'pinInfo'),(1, 'requestID'),(1, 'status'),)))
    return IMbnPinEvents
def _define_IMbnSubscriberInformation_head():
    class IMbnSubscriberInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('459ecc43-bcf5-11dc-a8a8-001321f1405f')
    return IMbnSubscriberInformation
def _define_IMbnSubscriberInformation():
    IMbnSubscriberInformation = win32more.NetworkManagement.MobileBroadband.IMbnSubscriberInformation_head
    IMbnSubscriberInformation.get_SubscriberID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_SubscriberID', ((1, 'SubscriberID'),)))
    IMbnSubscriberInformation.get_SimIccID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_SimIccID', ((1, 'SimIccID'),)))
    IMbnSubscriberInformation.get_TelephoneNumbers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'get_TelephoneNumbers', ((1, 'TelephoneNumbers'),)))
    return IMbnSubscriberInformation
def _define_IMbnSignal_head():
    class IMbnSignal(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2003-4bbb-aaee-338e368af6fa')
    return IMbnSignal
def _define_IMbnSignal():
    IMbnSignal = win32more.NetworkManagement.MobileBroadband.IMbnSignal_head
    IMbnSignal.GetSignalStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetSignalStrength', ((1, 'signalStrength'),)))
    IMbnSignal.GetSignalError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetSignalError', ((1, 'signalError'),)))
    return IMbnSignal
def _define_IMbnSignalEvents_head():
    class IMbnSignalEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2004-4bbb-aaee-338e368af6fa')
    return IMbnSignalEvents
def _define_IMbnSignalEvents():
    IMbnSignalEvents = win32more.NetworkManagement.MobileBroadband.IMbnSignalEvents_head
    IMbnSignalEvents.OnSignalStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSignal_head, use_last_error=False)(3, 'OnSignalStateChange', ((1, 'newInterface'),)))
    return IMbnSignalEvents
def _define_IMbnConnectionContext_head():
    class IMbnConnectionContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200b-4bbb-aaee-338e368af6fa')
    return IMbnConnectionContext
def _define_IMbnConnectionContext():
    IMbnConnectionContext = win32more.NetworkManagement.MobileBroadband.IMbnConnectionContext_head
    IMbnConnectionContext.GetProvisionedContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetProvisionedContexts', ((1, 'provisionedContexts'),)))
    IMbnConnectionContext.SetProvisionedContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_CONTEXT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(4, 'SetProvisionedContext', ((1, 'provisionedContexts'),(1, 'providerID'),(1, 'requestID'),)))
    return IMbnConnectionContext
def _define_IMbnConnectionContextEvents_head():
    class IMbnConnectionContextEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200c-4bbb-aaee-338e368af6fa')
    return IMbnConnectionContextEvents
def _define_IMbnConnectionContextEvents():
    IMbnConnectionContextEvents = win32more.NetworkManagement.MobileBroadband.IMbnConnectionContextEvents_head
    IMbnConnectionContextEvents.OnProvisionedContextListChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnectionContext_head, use_last_error=False)(3, 'OnProvisionedContextListChange', ((1, 'newInterface'),)))
    IMbnConnectionContextEvents.OnSetProvisionedContextComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnectionContext_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnSetProvisionedContextComplete', ((1, 'newInterface'),(1, 'requestID'),(1, 'status'),)))
    return IMbnConnectionContextEvents
def _define_IMbnConnectionProfileManager_head():
    class IMbnConnectionProfileManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-200f-4bbb-aaee-338e368af6fa')
    return IMbnConnectionProfileManager
def _define_IMbnConnectionProfileManager():
    IMbnConnectionProfileManager = win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfileManager_head
    IMbnConnectionProfileManager.GetConnectionProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetConnectionProfiles', ((1, 'mbnInterface'),(1, 'connectionProfiles'),)))
    IMbnConnectionProfileManager.GetConnectionProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnInterface_head,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head), use_last_error=False)(4, 'GetConnectionProfile', ((1, 'mbnInterface'),(1, 'profileName'),(1, 'connectionProfile'),)))
    IMbnConnectionProfileManager.CreateConnectionProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'CreateConnectionProfile', ((1, 'xmlProfile'),)))
    return IMbnConnectionProfileManager
def _define_IMbnConnectionProfile_head():
    class IMbnConnectionProfile(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2010-4bbb-aaee-338e368af6fa')
    return IMbnConnectionProfile
def _define_IMbnConnectionProfile():
    IMbnConnectionProfile = win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head
    IMbnConnectionProfile.GetProfileXmlData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetProfileXmlData', ((1, 'profileData'),)))
    IMbnConnectionProfile.UpdateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'UpdateProfile', ((1, 'strProfile'),)))
    IMbnConnectionProfile.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Delete', ()))
    return IMbnConnectionProfile
def _define_IMbnConnectionProfileEvents_head():
    class IMbnConnectionProfileEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2011-4bbb-aaee-338e368af6fa')
    return IMbnConnectionProfileEvents
def _define_IMbnConnectionProfileEvents():
    IMbnConnectionProfileEvents = win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfileEvents_head
    IMbnConnectionProfileEvents.OnProfileUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head, use_last_error=False)(3, 'OnProfileUpdate', ((1, 'newProfile'),)))
    return IMbnConnectionProfileEvents
def _define_IMbnSmsConfiguration_head():
    class IMbnSmsConfiguration(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2012-4bbb-aaee-338e368af6fa')
    return IMbnSmsConfiguration
def _define_IMbnSmsConfiguration():
    IMbnSmsConfiguration = win32more.NetworkManagement.MobileBroadband.IMbnSmsConfiguration_head
    IMbnSmsConfiguration.get_ServiceCenterAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_ServiceCenterAddress', ((1, 'scAddress'),)))
    IMbnSmsConfiguration.put_ServiceCenterAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'put_ServiceCenterAddress', ((1, 'scAddress'),)))
    IMbnSmsConfiguration.get_MaxMessageIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_MaxMessageIndex', ((1, 'index'),)))
    IMbnSmsConfiguration.get_CdmaShortMsgSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_CdmaShortMsgSize', ((1, 'shortMsgSize'),)))
    IMbnSmsConfiguration.get_SmsFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT), use_last_error=False)(7, 'get_SmsFormat', ((1, 'smsFormat'),)))
    IMbnSmsConfiguration.put_SmsFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT, use_last_error=False)(8, 'put_SmsFormat', ((1, 'smsFormat'),)))
    return IMbnSmsConfiguration
def _define_IMbnSmsReadMsgPdu_head():
    class IMbnSmsReadMsgPdu(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2013-4bbb-aaee-338e368af6fa')
    return IMbnSmsReadMsgPdu
def _define_IMbnSmsReadMsgPdu():
    IMbnSmsReadMsgPdu = win32more.NetworkManagement.MobileBroadband.IMbnSmsReadMsgPdu_head
    IMbnSmsReadMsgPdu.get_Index = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'get_Index', ((1, 'Index'),)))
    IMbnSmsReadMsgPdu.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_MSG_STATUS), use_last_error=False)(4, 'get_Status', ((1, 'Status'),)))
    IMbnSmsReadMsgPdu.get_PduData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_PduData', ((1, 'PduData'),)))
    IMbnSmsReadMsgPdu.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'get_Message', ((1, 'Message'),)))
    return IMbnSmsReadMsgPdu
def _define_IMbnSmsReadMsgTextCdma_head():
    class IMbnSmsReadMsgTextCdma(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2014-4bbb-aaee-338e368af6fa')
    return IMbnSmsReadMsgTextCdma
def _define_IMbnSmsReadMsgTextCdma():
    IMbnSmsReadMsgTextCdma = win32more.NetworkManagement.MobileBroadband.IMbnSmsReadMsgTextCdma_head
    IMbnSmsReadMsgTextCdma.get_Index = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'get_Index', ((1, 'Index'),)))
    IMbnSmsReadMsgTextCdma.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_MSG_STATUS), use_last_error=False)(4, 'get_Status', ((1, 'Status'),)))
    IMbnSmsReadMsgTextCdma.get_Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_Address', ((1, 'Address'),)))
    IMbnSmsReadMsgTextCdma.get_Timestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_Timestamp', ((1, 'Timestamp'),)))
    IMbnSmsReadMsgTextCdma.get_EncodingID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING), use_last_error=False)(7, 'get_EncodingID', ((1, 'EncodingID'),)))
    IMbnSmsReadMsgTextCdma.get_LanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG), use_last_error=False)(8, 'get_LanguageID', ((1, 'LanguageID'),)))
    IMbnSmsReadMsgTextCdma.get_SizeInCharacters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_SizeInCharacters', ((1, 'SizeInCharacters'),)))
    IMbnSmsReadMsgTextCdma.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(10, 'get_Message', ((1, 'Message'),)))
    return IMbnSmsReadMsgTextCdma
def _define_IMbnSms_head():
    class IMbnSms(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2015-4bbb-aaee-338e368af6fa')
    return IMbnSms
def _define_IMbnSms():
    IMbnSms = win32more.NetworkManagement.MobileBroadband.IMbnSms_head
    IMbnSms.GetSmsConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnSmsConfiguration_head), use_last_error=False)(3, 'GetSmsConfiguration', ((1, 'smsConfiguration'),)))
    IMbnSms.SetSmsConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSmsConfiguration_head,POINTER(UInt32), use_last_error=False)(4, 'SetSmsConfiguration', ((1, 'smsConfiguration'),(1, 'requestID'),)))
    IMbnSms.SmsSendPdu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,POINTER(UInt32), use_last_error=False)(5, 'SmsSendPdu', ((1, 'pduData'),(1, 'size'),(1, 'requestID'),)))
    IMbnSms.SmsSendCdma = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_ENCODING,win32more.NetworkManagement.MobileBroadband.MBN_SMS_CDMA_LANG,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(6, 'SmsSendCdma', ((1, 'address'),(1, 'encoding'),(1, 'language'),(1, 'sizeInCharacters'),(1, 'message'),(1, 'requestID'),)))
    IMbnSms.SmsSendCdmaPdu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(7, 'SmsSendCdmaPdu', ((1, 'message'),(1, 'requestID'),)))
    IMbnSms.SmsRead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_FILTER_head),win32more.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT,POINTER(UInt32), use_last_error=False)(8, 'SmsRead', ((1, 'smsFilter'),(1, 'smsFormat'),(1, 'requestID'),)))
    IMbnSms.SmsDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_FILTER_head),POINTER(UInt32), use_last_error=False)(9, 'SmsDelete', ((1, 'smsFilter'),(1, 'requestID'),)))
    IMbnSms.GetSmsStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_INFO_head), use_last_error=False)(10, 'GetSmsStatus', ((1, 'smsStatusInfo'),)))
    return IMbnSms
def _define_IMbnSmsEvents_head():
    class IMbnSmsEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2016-4bbb-aaee-338e368af6fa')
    return IMbnSmsEvents
def _define_IMbnSmsEvents():
    IMbnSmsEvents = win32more.NetworkManagement.MobileBroadband.IMbnSmsEvents_head
    IMbnSmsEvents.OnSmsConfigurationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head, use_last_error=False)(3, 'OnSmsConfigurationChange', ((1, 'sms'),)))
    IMbnSmsEvents.OnSetSmsConfigurationComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnSetSmsConfigurationComplete', ((1, 'sms'),(1, 'requestID'),(1, 'status'),)))
    IMbnSmsEvents.OnSmsSendComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(5, 'OnSmsSendComplete', ((1, 'sms'),(1, 'requestID'),(1, 'status'),)))
    IMbnSmsEvents.OnSmsReadComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head,win32more.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT,POINTER(win32more.System.Com.SAFEARRAY_head),Int16,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnSmsReadComplete', ((1, 'sms'),(1, 'smsFormat'),(1, 'readMsgs'),(1, 'moreMsgs'),(1, 'requestID'),(1, 'status'),)))
    IMbnSmsEvents.OnSmsNewClass0Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head,win32more.NetworkManagement.MobileBroadband.MBN_SMS_FORMAT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(7, 'OnSmsNewClass0Message', ((1, 'sms'),(1, 'smsFormat'),(1, 'readMsgs'),)))
    IMbnSmsEvents.OnSmsDeleteComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(8, 'OnSmsDeleteComplete', ((1, 'sms'),(1, 'requestID'),(1, 'status'),)))
    IMbnSmsEvents.OnSmsStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnSms_head, use_last_error=False)(9, 'OnSmsStatusChange', ((1, 'sms'),)))
    return IMbnSmsEvents
def _define_IMbnServiceActivation_head():
    class IMbnServiceActivation(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2017-4bbb-aaee-338e368af6fa')
    return IMbnServiceActivation
def _define_IMbnServiceActivation():
    IMbnServiceActivation = win32more.NetworkManagement.MobileBroadband.IMbnServiceActivation_head
    IMbnServiceActivation.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(3, 'Activate', ((1, 'vendorSpecificData'),(1, 'requestID'),)))
    return IMbnServiceActivation
def _define_IMbnServiceActivationEvents_head():
    class IMbnServiceActivationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2018-4bbb-aaee-338e368af6fa')
    return IMbnServiceActivationEvents
def _define_IMbnServiceActivationEvents():
    IMbnServiceActivationEvents = win32more.NetworkManagement.MobileBroadband.IMbnServiceActivationEvents_head
    IMbnServiceActivationEvents.OnActivationComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnServiceActivation_head,POINTER(win32more.System.Com.SAFEARRAY_head),UInt32,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'OnActivationComplete', ((1, 'serviceActivation'),(1, 'vendorSpecificData'),(1, 'requestID'),(1, 'status'),(1, 'networkError'),)))
    return IMbnServiceActivationEvents
def _define_IMbnVendorSpecificOperation_head():
    class IMbnVendorSpecificOperation(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2019-4bbb-aaee-338e368af6fa')
    return IMbnVendorSpecificOperation
def _define_IMbnVendorSpecificOperation():
    IMbnVendorSpecificOperation = win32more.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation_head
    IMbnVendorSpecificOperation.SetVendorSpecific = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(3, 'SetVendorSpecific', ((1, 'vendorSpecificData'),(1, 'requestID'),)))
    return IMbnVendorSpecificOperation
def _define_IMbnVendorSpecificEvents_head():
    class IMbnVendorSpecificEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201a-4bbb-aaee-338e368af6fa')
    return IMbnVendorSpecificEvents
def _define_IMbnVendorSpecificEvents():
    IMbnVendorSpecificEvents = win32more.NetworkManagement.MobileBroadband.IMbnVendorSpecificEvents_head
    IMbnVendorSpecificEvents.OnEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation_head,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(3, 'OnEventNotification', ((1, 'vendorOperation'),(1, 'vendorSpecificData'),)))
    IMbnVendorSpecificEvents.OnSetVendorSpecificComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnVendorSpecificOperation_head,POINTER(win32more.System.Com.SAFEARRAY_head),UInt32, use_last_error=False)(4, 'OnSetVendorSpecificComplete', ((1, 'vendorOperation'),(1, 'vendorSpecificData'),(1, 'requestID'),)))
    return IMbnVendorSpecificEvents
def _define_IMbnConnectionProfileManagerEvents_head():
    class IMbnConnectionProfileManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-201f-4bbb-aaee-338e368af6fa')
    return IMbnConnectionProfileManagerEvents
def _define_IMbnConnectionProfileManagerEvents():
    IMbnConnectionProfileManagerEvents = win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfileManagerEvents_head
    IMbnConnectionProfileManagerEvents.OnConnectionProfileArrival = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head, use_last_error=False)(3, 'OnConnectionProfileArrival', ((1, 'newConnectionProfile'),)))
    IMbnConnectionProfileManagerEvents.OnConnectionProfileRemoval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnConnectionProfile_head, use_last_error=False)(4, 'OnConnectionProfileRemoval', ((1, 'oldConnectionProfile'),)))
    return IMbnConnectionProfileManagerEvents
def _define_IMbnRadio_head():
    class IMbnRadio(win32more.System.Com.IUnknown_head):
        Guid = Guid('dccccab6-201f-4bbb-aaee-338e368af6fa')
    return IMbnRadio
def _define_IMbnRadio():
    IMbnRadio = win32more.NetworkManagement.MobileBroadband.IMbnRadio_head
    IMbnRadio.get_SoftwareRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_RADIO), use_last_error=False)(3, 'get_SoftwareRadioState', ((1, 'SoftwareRadioState'),)))
    IMbnRadio.get_HardwareRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_RADIO), use_last_error=False)(4, 'get_HardwareRadioState', ((1, 'HardwareRadioState'),)))
    IMbnRadio.SetSoftwareRadioState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.MBN_RADIO,POINTER(UInt32), use_last_error=False)(5, 'SetSoftwareRadioState', ((1, 'radioState'),(1, 'requestID'),)))
    return IMbnRadio
def _define_IMbnRadioEvents_head():
    class IMbnRadioEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcdddab6-201f-4bbb-aaee-338e368af6fa')
    return IMbnRadioEvents
def _define_IMbnRadioEvents():
    IMbnRadioEvents = win32more.NetworkManagement.MobileBroadband.IMbnRadioEvents_head
    IMbnRadioEvents.OnRadioStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRadio_head, use_last_error=False)(3, 'OnRadioStateChange', ((1, 'newInterface'),)))
    IMbnRadioEvents.OnSetSoftwareRadioStateComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnRadio_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnSetSoftwareRadioStateComplete', ((1, 'newInterface'),(1, 'requestID'),(1, 'status'),)))
    return IMbnRadioEvents
def _define_IMbnMultiCarrier_head():
    class IMbnMultiCarrier(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2020-4bbb-aaee-338e368af6fa')
    return IMbnMultiCarrier
def _define_IMbnMultiCarrier():
    IMbnMultiCarrier = win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head
    IMbnMultiCarrier.SetHomeProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER2_head),POINTER(UInt32), use_last_error=False)(3, 'SetHomeProvider', ((1, 'homeProvider'),(1, 'requestID'),)))
    IMbnMultiCarrier.GetPreferredProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetPreferredProviders', ((1, 'preferredMulticarrierProviders'),)))
    IMbnMultiCarrier.GetVisibleProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetVisibleProviders', ((1, 'age'),(1, 'visibleProviders'),)))
    IMbnMultiCarrier.GetSupportedCellularClasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetSupportedCellularClasses', ((1, 'cellularClasses'),)))
    IMbnMultiCarrier.GetCurrentCellularClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_CELLULAR_CLASS), use_last_error=False)(7, 'GetCurrentCellularClass', ((1, 'currentCellularClass'),)))
    IMbnMultiCarrier.ScanNetwork = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'ScanNetwork', ((1, 'requestID'),)))
    return IMbnMultiCarrier
def _define_IMbnMultiCarrierEvents_head():
    class IMbnMultiCarrierEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcdddab6-2021-4bbb-aaee-338e368af6fa')
    return IMbnMultiCarrierEvents
def _define_IMbnMultiCarrierEvents():
    IMbnMultiCarrierEvents = win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrierEvents_head
    IMbnMultiCarrierEvents.OnSetHomeProviderComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnSetHomeProviderComplete', ((1, 'mbnInterface'),(1, 'requestID'),(1, 'status'),)))
    IMbnMultiCarrierEvents.OnCurrentCellularClassChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head, use_last_error=False)(4, 'OnCurrentCellularClassChange', ((1, 'mbnInterface'),)))
    IMbnMultiCarrierEvents.OnPreferredProvidersChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head, use_last_error=False)(5, 'OnPreferredProvidersChange', ((1, 'mbnInterface'),)))
    IMbnMultiCarrierEvents.OnScanNetworkComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnScanNetworkComplete', ((1, 'mbnInterface'),(1, 'requestID'),(1, 'status'),)))
    IMbnMultiCarrierEvents.OnInterfaceCapabilityChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnMultiCarrier_head, use_last_error=False)(7, 'OnInterfaceCapabilityChange', ((1, 'mbnInterface'),)))
    return IMbnMultiCarrierEvents
def _define_IMbnDeviceServiceStateEvents_head():
    class IMbnDeviceServiceStateEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d3ff196-89ee-49d8-8b60-33ffddffc58d')
    return IMbnDeviceServiceStateEvents
def _define_IMbnDeviceServiceStateEvents():
    IMbnDeviceServiceStateEvents = win32more.NetworkManagement.MobileBroadband.IMbnDeviceServiceStateEvents_head
    IMbnDeviceServiceStateEvents.OnSessionsStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICE_SESSIONS_STATE, use_last_error=False)(3, 'OnSessionsStateChange', ((1, 'interfaceID'),(1, 'stateChange'),)))
    return IMbnDeviceServiceStateEvents
def _define_IMbnDeviceServicesManager_head():
    class IMbnDeviceServicesManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('20a26258-6811-4478-ac1d-13324e45e41c')
    return IMbnDeviceServicesManager
def _define_IMbnDeviceServicesManager():
    IMbnDeviceServicesManager = win32more.NetworkManagement.MobileBroadband.IMbnDeviceServicesManager_head
    IMbnDeviceServicesManager.GetDeviceServicesContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnDeviceServicesContext_head), use_last_error=False)(3, 'GetDeviceServicesContext', ((1, 'networkInterfaceID'),(1, 'mbnDevicesContext'),)))
    return IMbnDeviceServicesManager
def _define_IMbnDeviceServicesContext_head():
    class IMbnDeviceServicesContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc5ac347-1592-4068-80bb-6a57580150d8')
    return IMbnDeviceServicesContext
def _define_IMbnDeviceServicesContext():
    IMbnDeviceServicesContext = win32more.NetworkManagement.MobileBroadband.IMbnDeviceServicesContext_head
    IMbnDeviceServicesContext.EnumerateDeviceServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'EnumerateDeviceServices', ((1, 'deviceServices'),)))
    IMbnDeviceServicesContext.GetDeviceService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head), use_last_error=False)(4, 'GetDeviceService', ((1, 'deviceServiceID'),(1, 'mbnDeviceService'),)))
    IMbnDeviceServicesContext.get_MaxCommandSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_MaxCommandSize', ((1, 'maxCommandSize'),)))
    IMbnDeviceServicesContext.get_MaxDataSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_MaxDataSize', ((1, 'maxDataSize'),)))
    return IMbnDeviceServicesContext
def _define_IMbnDeviceServicesEvents_head():
    class IMbnDeviceServicesEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a900c19-6824-4e97-b76e-cf239d0ca642')
    return IMbnDeviceServicesEvents
def _define_IMbnDeviceServicesEvents():
    IMbnDeviceServicesEvents = win32more.NetworkManagement.MobileBroadband.IMbnDeviceServicesEvents_head
    IMbnDeviceServicesEvents.OnQuerySupportedCommandsComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'OnQuerySupportedCommandsComplete', ((1, 'deviceService'),(1, 'commandIDList'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnOpenCommandSessionComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'OnOpenCommandSessionComplete', ((1, 'deviceService'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnCloseCommandSessionComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'OnCloseCommandSessionComplete', ((1, 'deviceService'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnSetCommandComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'OnSetCommandComplete', ((1, 'deviceService'),(1, 'responseID'),(1, 'deviceServiceData'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnQueryCommandComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'OnQueryCommandComplete', ((1, 'deviceService'),(1, 'responseID'),(1, 'deviceServiceData'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(8, 'OnEventNotification', ((1, 'deviceService'),(1, 'eventID'),(1, 'deviceServiceData'),)))
    IMbnDeviceServicesEvents.OnOpenDataSessionComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'OnOpenDataSessionComplete', ((1, 'deviceService'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnCloseDataSessionComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'OnCloseDataSessionComplete', ((1, 'deviceService'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnWriteDataComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'OnWriteDataComplete', ((1, 'deviceService'),(1, 'status'),(1, 'requestID'),)))
    IMbnDeviceServicesEvents.OnReadData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(12, 'OnReadData', ((1, 'deviceService'),(1, 'deviceServiceData'),)))
    IMbnDeviceServicesEvents.OnInterfaceStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.NetworkManagement.MobileBroadband.MBN_DEVICE_SERVICES_INTERFACE_STATE, use_last_error=False)(13, 'OnInterfaceStateChange', ((1, 'interfaceID'),(1, 'stateChange'),)))
    return IMbnDeviceServicesEvents
def _define_IMbnDeviceService_head():
    class IMbnDeviceService(win32more.System.Com.IUnknown_head):
        Guid = Guid('b3bb9a71-dc70-4be9-a4da-7886ae8b191b')
    return IMbnDeviceService
def _define_IMbnDeviceService():
    IMbnDeviceService = win32more.NetworkManagement.MobileBroadband.IMbnDeviceService_head
    IMbnDeviceService.QuerySupportedCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'QuerySupportedCommands', ((1, 'requestID'),)))
    IMbnDeviceService.OpenCommandSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'OpenCommandSession', ((1, 'requestID'),)))
    IMbnDeviceService.CloseCommandSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'CloseCommandSession', ((1, 'requestID'),)))
    IMbnDeviceService.SetCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(6, 'SetCommand', ((1, 'commandID'),(1, 'deviceServiceData'),(1, 'requestID'),)))
    IMbnDeviceService.QueryCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(7, 'QueryCommand', ((1, 'commandID'),(1, 'deviceServiceData'),(1, 'requestID'),)))
    IMbnDeviceService.OpenDataSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'OpenDataSession', ((1, 'requestID'),)))
    IMbnDeviceService.CloseDataSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'CloseDataSession', ((1, 'requestID'),)))
    IMbnDeviceService.WriteData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt32), use_last_error=False)(10, 'WriteData', ((1, 'deviceServiceData'),(1, 'requestID'),)))
    IMbnDeviceService.get_InterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_InterfaceID', ((1, 'InterfaceID'),)))
    IMbnDeviceService.get_DeviceServiceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_DeviceServiceID', ((1, 'DeviceServiceID'),)))
    IMbnDeviceService.get_IsCommandSessionOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'get_IsCommandSessionOpen', ((1, 'value'),)))
    IMbnDeviceService.get_IsDataSessionOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'get_IsDataSessionOpen', ((1, 'value'),)))
    return IMbnDeviceService
def _define___mbnapi_ReferenceRemainingTypes___head():
    class __mbnapi_ReferenceRemainingTypes__(Structure):
        pass
    return __mbnapi_ReferenceRemainingTypes__
def _define___mbnapi_ReferenceRemainingTypes__():
    __mbnapi_ReferenceRemainingTypes__ = win32more.NetworkManagement.MobileBroadband.__mbnapi_ReferenceRemainingTypes___head
    __mbnapi_ReferenceRemainingTypes__._fields_ = [
        ("bandClass", win32more.NetworkManagement.MobileBroadband.MBN_BAND_CLASS),
        ("contextConstants", win32more.NetworkManagement.MobileBroadband.MBN_CONTEXT_CONSTANTS),
        ("ctrlCaps", win32more.NetworkManagement.MobileBroadband.MBN_CTRL_CAPS),
        ("dataClass", win32more.NetworkManagement.MobileBroadband.MBN_DATA_CLASS),
        ("interfaceCapsConstants", win32more.NetworkManagement.MobileBroadband.MBN_INTERFACE_CAPS_CONSTANTS),
        ("pinConstants", win32more.NetworkManagement.MobileBroadband.MBN_PIN_CONSTANTS),
        ("providerConstants", win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER_CONSTANTS),
        ("providerState", win32more.NetworkManagement.MobileBroadband.MBN_PROVIDER_STATE),
        ("registrationConstants", win32more.NetworkManagement.MobileBroadband.MBN_REGISTRATION_CONSTANTS),
        ("signalConstants", win32more.NetworkManagement.MobileBroadband.MBN_SIGNAL_CONSTANTS),
        ("smsCaps", win32more.NetworkManagement.MobileBroadband.MBN_SMS_CAPS),
        ("smsConstants", win32more.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS),
        ("wwaextSmsConstants", win32more.NetworkManagement.MobileBroadband.WWAEXT_SMS_CONSTANTS),
        ("smsStatusFlag", win32more.NetworkManagement.MobileBroadband.MBN_SMS_STATUS_FLAG),
    ]
    return __mbnapi_ReferenceRemainingTypes__
def _define___DummyPinType___head():
    class __DummyPinType__(Structure):
        pass
    return __DummyPinType__
def _define___DummyPinType__():
    __DummyPinType__ = win32more.NetworkManagement.MobileBroadband.__DummyPinType___head
    __DummyPinType__._fields_ = [
        ("pinType", UInt32),
    ]
    return __DummyPinType__
def _define_IMbnPin_head():
    class IMbnPin(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcbbbab6-2007-4bbb-aaee-338e368af6fa')
    return IMbnPin
def _define_IMbnPin():
    IMbnPin = win32more.NetworkManagement.MobileBroadband.IMbnPin_head
    IMbnPin.get_PinType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_TYPE), use_last_error=False)(3, 'get_PinType', ((1, 'PinType'),)))
    IMbnPin.get_PinFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_FORMAT), use_last_error=False)(4, 'get_PinFormat', ((1, 'PinFormat'),)))
    IMbnPin.get_PinLengthMin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_PinLengthMin', ((1, 'PinLengthMin'),)))
    IMbnPin.get_PinLengthMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_PinLengthMax', ((1, 'PinLengthMax'),)))
    IMbnPin.get_PinMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.MBN_PIN_MODE), use_last_error=False)(7, 'get_PinMode', ((1, 'PinMode'),)))
    IMbnPin.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(8, 'Enable', ((1, 'pin'),(1, 'requestID'),)))
    IMbnPin.Disable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(9, 'Disable', ((1, 'pin'),(1, 'requestID'),)))
    IMbnPin.Enter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(10, 'Enter', ((1, 'pin'),(1, 'requestID'),)))
    IMbnPin.Change = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(11, 'Change', ((1, 'pin'),(1, 'newPin'),(1, 'requestID'),)))
    IMbnPin.Unblock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(12, 'Unblock', ((1, 'puk'),(1, 'newPin'),(1, 'requestID'),)))
    IMbnPin.GetPinManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.MobileBroadband.IMbnPinManager_head), use_last_error=False)(13, 'GetPinManager', ((1, 'pinManager'),)))
    return IMbnPin
__all__ = [
    "MbnConnectionProfileManager",
    "MbnInterfaceManager",
    "MbnConnectionManager",
    "MbnDeviceServicesManager",
    "IDummyMBNUCMExt",
    "MBN_SIGNAL_CONSTANTS",
    "MBN_RSSI_DEFAULT",
    "MBN_RSSI_DISABLE",
    "MBN_RSSI_UNKNOWN",
    "MBN_ERROR_RATE_UNKNOWN",
    "MBN_CELLULAR_CLASS",
    "MBN_CELLULAR_CLASS_NONE",
    "MBN_CELLULAR_CLASS_GSM",
    "MBN_CELLULAR_CLASS_CDMA",
    "MBN_VOICE_CLASS",
    "MBN_VOICE_CLASS_NONE",
    "MBN_VOICE_CLASS_NO_VOICE",
    "MBN_VOICE_CLASS_SEPARATE_VOICE_DATA",
    "MBN_VOICE_CLASS_SIMULTANEOUS_VOICE_DATA",
    "MBN_PROVIDER_STATE",
    "MBN_PROVIDER_STATE_NONE",
    "MBN_PROVIDER_STATE_HOME",
    "MBN_PROVIDER_STATE_FORBIDDEN",
    "MBN_PROVIDER_STATE_PREFERRED",
    "MBN_PROVIDER_STATE_VISIBLE",
    "MBN_PROVIDER_STATE_REGISTERED",
    "MBN_PROVIDER_STATE_PREFERRED_MULTICARRIER",
    "MBN_PROVIDER_CONSTANTS",
    "MBN_PROVIDERNAME_LEN",
    "MBN_PROVIDERID_LEN",
    "MBN_INTERFACE_CAPS_CONSTANTS",
    "MBN_DEVICEID_LEN",
    "MBN_MANUFACTURER_LEN",
    "MBN_MODEL_LEN",
    "MBN_FIRMWARE_LEN",
    "MBN_DATA_CLASS",
    "MBN_DATA_CLASS_NONE",
    "MBN_DATA_CLASS_GPRS",
    "MBN_DATA_CLASS_EDGE",
    "MBN_DATA_CLASS_UMTS",
    "MBN_DATA_CLASS_HSDPA",
    "MBN_DATA_CLASS_HSUPA",
    "MBN_DATA_CLASS_LTE",
    "MBN_DATA_CLASS_5G_NSA",
    "MBN_DATA_CLASS_5G_SA",
    "MBN_DATA_CLASS_1XRTT",
    "MBN_DATA_CLASS_1XEVDO",
    "MBN_DATA_CLASS_1XEVDO_REVA",
    "MBN_DATA_CLASS_1XEVDV",
    "MBN_DATA_CLASS_3XRTT",
    "MBN_DATA_CLASS_1XEVDO_REVB",
    "MBN_DATA_CLASS_UMB",
    "MBN_DATA_CLASS_CUSTOM",
    "MBN_CTRL_CAPS",
    "MBN_CTRL_CAPS_NONE",
    "MBN_CTRL_CAPS_REG_MANUAL",
    "MBN_CTRL_CAPS_HW_RADIO_SWITCH",
    "MBN_CTRL_CAPS_CDMA_MOBILE_IP",
    "MBN_CTRL_CAPS_CDMA_SIMPLE_IP",
    "MBN_CTRL_CAPS_PROTECT_UNIQUEID",
    "MBN_CTRL_CAPS_MODEL_MULTI_CARRIER",
    "MBN_CTRL_CAPS_USSD",
    "MBN_CTRL_CAPS_MULTI_MODE",
    "MBN_SMS_CAPS",
    "MBN_SMS_CAPS_NONE",
    "MBN_SMS_CAPS_PDU_RECEIVE",
    "MBN_SMS_CAPS_PDU_SEND",
    "MBN_SMS_CAPS_TEXT_RECEIVE",
    "MBN_SMS_CAPS_TEXT_SEND",
    "MBN_BAND_CLASS",
    "MBN_BAND_CLASS_NONE",
    "MBN_BAND_CLASS_0",
    "MBN_BAND_CLASS_I",
    "MBN_BAND_CLASS_II",
    "MBN_BAND_CLASS_III",
    "MBN_BAND_CLASS_IV",
    "MBN_BAND_CLASS_V",
    "MBN_BAND_CLASS_VI",
    "MBN_BAND_CLASS_VII",
    "MBN_BAND_CLASS_VIII",
    "MBN_BAND_CLASS_IX",
    "MBN_BAND_CLASS_X",
    "MBN_BAND_CLASS_XI",
    "MBN_BAND_CLASS_XII",
    "MBN_BAND_CLASS_XIII",
    "MBN_BAND_CLASS_XIV",
    "MBN_BAND_CLASS_XV",
    "MBN_BAND_CLASS_XVI",
    "MBN_BAND_CLASS_XVII",
    "MBN_BAND_CLASS_CUSTOM",
    "MBN_INTERFACE_CAPS",
    "MBN_PROVIDER",
    "MBN_PROVIDER2",
    "MBN_READY_STATE",
    "MBN_READY_STATE_OFF",
    "MBN_READY_STATE_INITIALIZED",
    "MBN_READY_STATE_SIM_NOT_INSERTED",
    "MBN_READY_STATE_BAD_SIM",
    "MBN_READY_STATE_FAILURE",
    "MBN_READY_STATE_NOT_ACTIVATED",
    "MBN_READY_STATE_DEVICE_LOCKED",
    "MBN_READY_STATE_DEVICE_BLOCKED",
    "MBN_READY_STATE_NO_ESIM_PROFILE",
    "MBN_ACTIVATION_STATE",
    "MBN_ACTIVATION_STATE_NONE",
    "MBN_ACTIVATION_STATE_ACTIVATED",
    "MBN_ACTIVATION_STATE_ACTIVATING",
    "MBN_ACTIVATION_STATE_DEACTIVATED",
    "MBN_ACTIVATION_STATE_DEACTIVATING",
    "MBN_CONNECTION_MODE",
    "MBN_CONNECTION_MODE_PROFILE",
    "MBN_CONNECTION_MODE_TMP_PROFILE",
    "MBN_VOICE_CALL_STATE",
    "MBN_VOICE_CALL_STATE_NONE",
    "MBN_VOICE_CALL_STATE_IN_PROGRESS",
    "MBN_VOICE_CALL_STATE_HANGUP",
    "MBN_REGISTRATION_CONSTANTS",
    "MBN_ROAMTEXT_LEN",
    "MBN_CDMA_DEFAULT_PROVIDER_ID",
    "MBN_REGISTER_STATE",
    "MBN_REGISTER_STATE_NONE",
    "MBN_REGISTER_STATE_DEREGISTERED",
    "MBN_REGISTER_STATE_SEARCHING",
    "MBN_REGISTER_STATE_HOME",
    "MBN_REGISTER_STATE_ROAMING",
    "MBN_REGISTER_STATE_PARTNER",
    "MBN_REGISTER_STATE_DENIED",
    "MBN_REGISTER_MODE",
    "MBN_REGISTER_MODE_NONE",
    "MBN_REGISTER_MODE_AUTOMATIC",
    "MBN_REGISTER_MODE_MANUAL",
    "MBN_PIN_CONSTANTS",
    "MBN_ATTEMPTS_REMAINING_UNKNOWN",
    "MBN_PIN_LENGTH_UNKNOWN",
    "MBN_PIN_STATE",
    "MBN_PIN_STATE_NONE",
    "MBN_PIN_STATE_ENTER",
    "MBN_PIN_STATE_UNBLOCK",
    "MBN_PIN_TYPE",
    "MBN_PIN_TYPE_NONE",
    "MBN_PIN_TYPE_CUSTOM",
    "MBN_PIN_TYPE_PIN1",
    "MBN_PIN_TYPE_PIN2",
    "MBN_PIN_TYPE_DEVICE_SIM_PIN",
    "MBN_PIN_TYPE_DEVICE_FIRST_SIM_PIN",
    "MBN_PIN_TYPE_NETWORK_PIN",
    "MBN_PIN_TYPE_NETWORK_SUBSET_PIN",
    "MBN_PIN_TYPE_SVC_PROVIDER_PIN",
    "MBN_PIN_TYPE_CORPORATE_PIN",
    "MBN_PIN_TYPE_SUBSIDY_LOCK",
    "MBN_PIN_INFO",
    "MBN_PIN_MODE",
    "MBN_PIN_MODE_ENABLED",
    "MBN_PIN_MODE_DISABLED",
    "MBN_PIN_FORMAT",
    "MBN_PIN_FORMAT_NONE",
    "MBN_PIN_FORMAT_NUMERIC",
    "MBN_PIN_FORMAT_ALPHANUMERIC",
    "MBN_CONTEXT_CONSTANTS",
    "MBN_ACCESSSTRING_LEN",
    "MBN_USERNAME_LEN",
    "MBN_PASSWORD_LEN",
    "MBN_CONTEXT_ID_APPEND",
    "MBN_AUTH_PROTOCOL",
    "MBN_AUTH_PROTOCOL_NONE",
    "MBN_AUTH_PROTOCOL_PAP",
    "MBN_AUTH_PROTOCOL_CHAP",
    "MBN_AUTH_PROTOCOL_MSCHAPV2",
    "MBN_COMPRESSION",
    "MBN_COMPRESSION_NONE",
    "MBN_COMPRESSION_ENABLE",
    "MBN_CONTEXT_TYPE",
    "MBN_CONTEXT_TYPE_NONE",
    "MBN_CONTEXT_TYPE_INTERNET",
    "MBN_CONTEXT_TYPE_VPN",
    "MBN_CONTEXT_TYPE_VOICE",
    "MBN_CONTEXT_TYPE_VIDEO_SHARE",
    "MBN_CONTEXT_TYPE_CUSTOM",
    "MBN_CONTEXT_TYPE_PURCHASE",
    "MBN_CONTEXT",
    "WWAEXT_SMS_CONSTANTS",
    "MBN_MESSAGE_INDEX_NONE",
    "MBN_CDMA_SHORT_MSG_SIZE_UNKNOWN",
    "MBN_CDMA_SHORT_MSG_SIZE_MAX",
    "MBN_MSG_STATUS",
    "MBN_MSG_STATUS_NEW",
    "MBN_MSG_STATUS_OLD",
    "MBN_MSG_STATUS_DRAFT",
    "MBN_MSG_STATUS_SENT",
    "MBN_SMS_CDMA_LANG",
    "MBN_SMS_CDMA_LANG_NONE",
    "MBN_SMS_CDMA_LANG_ENGLISH",
    "MBN_SMS_CDMA_LANG_FRENCH",
    "MBN_SMS_CDMA_LANG_SPANISH",
    "MBN_SMS_CDMA_LANG_JAPANESE",
    "MBN_SMS_CDMA_LANG_KOREAN",
    "MBN_SMS_CDMA_LANG_CHINESE",
    "MBN_SMS_CDMA_LANG_HEBREW",
    "MBN_SMS_CDMA_ENCODING",
    "MBN_SMS_CDMA_ENCODING_OCTET",
    "MBN_SMS_CDMA_ENCODING_EPM",
    "MBN_SMS_CDMA_ENCODING_7BIT_ASCII",
    "MBN_SMS_CDMA_ENCODING_IA5",
    "MBN_SMS_CDMA_ENCODING_UNICODE",
    "MBN_SMS_CDMA_ENCODING_SHIFT_JIS",
    "MBN_SMS_CDMA_ENCODING_KOREAN",
    "MBN_SMS_CDMA_ENCODING_LATIN_HEBREW",
    "MBN_SMS_CDMA_ENCODING_LATIN",
    "MBN_SMS_CDMA_ENCODING_GSM_7BIT",
    "MBN_SMS_FLAG",
    "MBN_SMS_FLAG_ALL",
    "MBN_SMS_FLAG_INDEX",
    "MBN_SMS_FLAG_NEW",
    "MBN_SMS_FLAG_OLD",
    "MBN_SMS_FLAG_SENT",
    "MBN_SMS_FLAG_DRAFT",
    "MBN_SMS_FILTER",
    "MBN_SMS_STATUS_FLAG",
    "MBN_SMS_FLAG_NONE",
    "MBN_SMS_FLAG_MESSAGE_STORE_FULL",
    "MBN_SMS_FLAG_NEW_MESSAGE",
    "MBN_SMS_STATUS_INFO",
    "MBN_SMS_FORMAT",
    "MBN_SMS_FORMAT_NONE",
    "MBN_SMS_FORMAT_PDU",
    "MBN_SMS_FORMAT_TEXT",
    "MBN_RADIO",
    "MBN_RADIO_OFF",
    "MBN_RADIO_ON",
    "MBN_DEVICE_SERVICE_SESSIONS_STATE",
    "MBN_DEVICE_SERVICE_SESSIONS_RESTORED",
    "MBN_DEVICE_SERVICE",
    "MBN_DEVICE_SERVICES_INTERFACE_STATE",
    "MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_ARRIVAL",
    "MBN_DEVICE_SERVICES_CAPABLE_INTERFACE_REMOVAL",
    "IMbnConnection",
    "IMbnConnectionEvents",
    "IMbnInterface",
    "IMbnInterfaceEvents",
    "IMbnInterfaceManager",
    "IMbnInterfaceManagerEvents",
    "IMbnRegistration",
    "IMbnRegistrationEvents",
    "IMbnConnectionManager",
    "IMbnConnectionManagerEvents",
    "IMbnPinManager",
    "IMbnPinManagerEvents",
    "IMbnPinEvents",
    "IMbnSubscriberInformation",
    "IMbnSignal",
    "IMbnSignalEvents",
    "IMbnConnectionContext",
    "IMbnConnectionContextEvents",
    "IMbnConnectionProfileManager",
    "IMbnConnectionProfile",
    "IMbnConnectionProfileEvents",
    "IMbnSmsConfiguration",
    "IMbnSmsReadMsgPdu",
    "IMbnSmsReadMsgTextCdma",
    "IMbnSms",
    "IMbnSmsEvents",
    "IMbnServiceActivation",
    "IMbnServiceActivationEvents",
    "IMbnVendorSpecificOperation",
    "IMbnVendorSpecificEvents",
    "IMbnConnectionProfileManagerEvents",
    "IMbnRadio",
    "IMbnRadioEvents",
    "IMbnMultiCarrier",
    "IMbnMultiCarrierEvents",
    "IMbnDeviceServiceStateEvents",
    "IMbnDeviceServicesManager",
    "IMbnDeviceServicesContext",
    "IMbnDeviceServicesEvents",
    "IMbnDeviceService",
    "__mbnapi_ReferenceRemainingTypes__",
    "__DummyPinType__",
    "IMbnPin",
]
