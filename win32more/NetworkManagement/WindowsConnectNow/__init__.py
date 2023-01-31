from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.WindowsConnectNow
import win32more.System.Com
import win32more.UI.Shell.PropertiesSystem
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
WCN_E_PEER_NOT_FOUND: win32more.Foundation.HRESULT = -2147206143
WCN_E_AUTHENTICATION_FAILED: win32more.Foundation.HRESULT = -2147206142
WCN_E_CONNECTION_REJECTED: win32more.Foundation.HRESULT = -2147206141
WCN_E_SESSION_TIMEDOUT: win32more.Foundation.HRESULT = -2147206140
WCN_E_PROTOCOL_ERROR: win32more.Foundation.HRESULT = -2147206139
WCN_QUERY_CONSTRAINT_USE_SOFTAP: String = 'WCN.Discovery.SoftAP'
WCN_VALUE_DT_CATEGORY_COMPUTER: UInt32 = 1
WCN_VALUE_DT_CATEGORY_INPUT_DEVICE: UInt32 = 2
WCN_VALUE_DT_CATEGORY_PRINTER: UInt32 = 3
WCN_VALUE_DT_CATEGORY_CAMERA: UInt32 = 4
WCN_VALUE_DT_CATEGORY_STORAGE: UInt32 = 5
WCN_VALUE_DT_CATEGORY_NETWORK_INFRASTRUCTURE: UInt32 = 6
WCN_VALUE_DT_CATEGORY_DISPLAY: UInt32 = 7
WCN_VALUE_DT_CATEGORY_MULTIMEDIA_DEVICE: UInt32 = 8
WCN_VALUE_DT_CATEGORY_GAMING_DEVICE: UInt32 = 9
WCN_VALUE_DT_CATEGORY_TELEPHONE: UInt32 = 10
WCN_VALUE_DT_CATEGORY_AUDIO_DEVICE: UInt32 = 11
WCN_VALUE_DT_CATEGORY_OTHER: UInt32 = 255
WCN_VALUE_DT_SUBTYPE_WIFI_OUI: UInt32 = 5304836
WCN_VALUE_DT_SUBTYPE_COMPUTER__PC: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_COMPUTER__SERVER: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_COMPUTER__MEDIACENTER: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_COMPUTER__ULTRAMOBILEPC: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_COMPUTER__NOTEBOOK: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_COMPUTER__DESKTOP: UInt32 = 6
WCN_VALUE_DT_SUBTYPE_COMPUTER__MID: UInt32 = 7
WCN_VALUE_DT_SUBTYPE_COMPUTER__NETBOOK: UInt32 = 8
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__KEYBOARD: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__MOUSE: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__JOYSTICK: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__TRACKBALL: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__GAMECONTROLLER: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__REMOTE: UInt32 = 6
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__TOUCHSCREEN: UInt32 = 7
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__BIOMETRICREADER: UInt32 = 8
WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__BARCODEREADER: UInt32 = 9
WCN_VALUE_DT_SUBTYPE_PRINTER__PRINTER: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_PRINTER__SCANNER: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_PRINTER__FAX: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_PRINTER__COPIER: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_PRINTER__ALLINONE: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_CAMERA__STILL_CAMERA: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_CAMERA__VIDEO_CAMERA: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_CAMERA__WEB_CAMERA: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_CAMERA__SECURITY_CAMERA: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_STORAGE__NAS: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__AP: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__ROUTER: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__SWITCH: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__GATEWAY: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__BRIDGE: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_DISPLAY__TELEVISION: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_DISPLAY__PICTURE_FRAME: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_DISPLAY__PROJECTOR: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_DISPLAY__MONITOR: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__DAR: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__PVR: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__MCX: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__SETTOPBOX: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__MEDIA_SERVER_ADAPT_EXT: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__PVP: UInt32 = 6
WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__XBOX: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__XBOX360: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__PLAYSTATION: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__CONSOLE_ADAPT: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__PORTABLE: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_TELEPHONE__WINDOWS_MOBILE: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_TELEPHONE__PHONE_SINGLEMODE: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_TELEPHONE__PHONE_DUALMODE: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_TELEPHONE__SMARTPHONE_SINGLEMODE: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_TELEPHONE__SMARTPHONE_DUALMODE: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__TUNER_RECEIVER: UInt32 = 1
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__SPEAKERS: UInt32 = 2
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__PMP: UInt32 = 3
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HEADSET: UInt32 = 4
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HEADPHONES: UInt32 = 5
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__MICROPHONE: UInt32 = 6
WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HOMETHEATER: UInt32 = 7
WCN_API_MAX_BUFFER_SIZE: UInt32 = 2096
WCN_MICROSOFT_VENDOR_ID: UInt32 = 311
WCN_NO_SUBTYPE: UInt32 = 4294967294
WCN_FLAG_DISCOVERY_VE: UInt32 = 1
WCN_FLAG_AUTHENTICATED_VE: UInt32 = 2
WCN_FLAG_ENCRYPTED_VE: UInt32 = 4
SID_WcnProvider: Guid = Guid('c100beca-d33a-4a4b-bf-23-bb-ef-46-63-d0-17')
def PKEY_WCN_DeviceType_Category():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=16)
def PKEY_WCN_DeviceType_SubCategoryOUI():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=17)
def PKEY_WCN_DeviceType_SubCategory():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=18)
def PKEY_WCN_SSID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('88190b8b-4684-11da-a2-6a-00-02-b3-98-8e-81'), pid=32)
class IWCNConnectNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c100be9f-d33a-4a4b-bf-23-bb-ef-46-63-d0-17')
    @commethod(3)
    def ConnectSucceeded() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectFailed(hrFailure: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IWCNDevice(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c100be9c-d33a-4a4b-bf-23-bb-ef-46-63-d0-17')
    @commethod(3)
    def SetPassword(Type: win32more.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE, dwPasswordLength: UInt32, pbPassword: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(pNotify: win32more.NetworkManagement.WindowsConnectNow.IWCNConnectNotify_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttribute(AttributeType: win32more.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, dwMaxBufferSize: UInt32, pbBuffer: c_char_p_no, pdwBufferUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIntegerAttribute(AttributeType: win32more.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, puInteger: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStringAttribute(AttributeType: win32more.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, cchMaxString: UInt32, wszString: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetworkProfile(cchMaxStringLength: UInt32, wszProfile: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetNetworkProfile(pszProfileXml: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetVendorExtension(pVendorExtSpec: POINTER(win32more.NetworkManagement.WindowsConnectNow.WCN_VENDOR_EXTENSION_SPEC_head), dwMaxBufferSize: UInt32, pbBuffer: c_char_p_no, pdwBufferUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetVendorExtension(pVendorExtSpec: POINTER(win32more.NetworkManagement.WindowsConnectNow.WCN_VENDOR_EXTENSION_SPEC_head), cbBuffer: UInt32, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetNFCPasswordParams(Type: win32more.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE, dwOOBPasswordID: UInt32, dwPasswordLength: UInt32, pbPassword: c_char_p_no, dwRemotePublicKeyHashLength: UInt32, pbRemotePublicKeyHash: c_char_p_no, dwDHKeyBlobLength: UInt32, pbDHKeyBlob: c_char_p_no) -> win32more.Foundation.HRESULT: ...
WCNDeviceObject = Guid('c100bea7-d33a-4a4b-bf-23-bb-ef-46-63-d0-17')
WCN_ATTRIBUTE_TYPE = Int32
WCN_TYPE_AP_CHANNEL: WCN_ATTRIBUTE_TYPE = 0
WCN_TYPE_ASSOCIATION_STATE: WCN_ATTRIBUTE_TYPE = 1
WCN_TYPE_AUTHENTICATION_TYPE: WCN_ATTRIBUTE_TYPE = 2
WCN_TYPE_AUTHENTICATION_TYPE_FLAGS: WCN_ATTRIBUTE_TYPE = 3
WCN_TYPE_AUTHENTICATOR: WCN_ATTRIBUTE_TYPE = 4
WCN_TYPE_CONFIG_METHODS: WCN_ATTRIBUTE_TYPE = 5
WCN_TYPE_CONFIGURATION_ERROR: WCN_ATTRIBUTE_TYPE = 6
WCN_TYPE_CONFIRMATION_URL4: WCN_ATTRIBUTE_TYPE = 7
WCN_TYPE_CONFIRMATION_URL6: WCN_ATTRIBUTE_TYPE = 8
WCN_TYPE_CONNECTION_TYPE: WCN_ATTRIBUTE_TYPE = 9
WCN_TYPE_CONNECTION_TYPE_FLAGS: WCN_ATTRIBUTE_TYPE = 10
WCN_TYPE_CREDENTIAL: WCN_ATTRIBUTE_TYPE = 11
WCN_TYPE_DEVICE_NAME: WCN_ATTRIBUTE_TYPE = 12
WCN_TYPE_DEVICE_PASSWORD_ID: WCN_ATTRIBUTE_TYPE = 13
WCN_TYPE_E_HASH1: WCN_ATTRIBUTE_TYPE = 14
WCN_TYPE_E_HASH2: WCN_ATTRIBUTE_TYPE = 15
WCN_TYPE_E_SNONCE1: WCN_ATTRIBUTE_TYPE = 16
WCN_TYPE_E_SNONCE2: WCN_ATTRIBUTE_TYPE = 17
WCN_TYPE_ENCRYPTED_SETTINGS: WCN_ATTRIBUTE_TYPE = 18
WCN_TYPE_ENCRYPTION_TYPE: WCN_ATTRIBUTE_TYPE = 19
WCN_TYPE_ENCRYPTION_TYPE_FLAGS: WCN_ATTRIBUTE_TYPE = 20
WCN_TYPE_ENROLLEE_NONCE: WCN_ATTRIBUTE_TYPE = 21
WCN_TYPE_FEATURE_ID: WCN_ATTRIBUTE_TYPE = 22
WCN_TYPE_IDENTITY: WCN_ATTRIBUTE_TYPE = 23
WCN_TYPE_IDENTITY_PROOF: WCN_ATTRIBUTE_TYPE = 24
WCN_TYPE_KEY_WRAP_AUTHENTICATOR: WCN_ATTRIBUTE_TYPE = 25
WCN_TYPE_KEY_IDENTIFIER: WCN_ATTRIBUTE_TYPE = 26
WCN_TYPE_MAC_ADDRESS: WCN_ATTRIBUTE_TYPE = 27
WCN_TYPE_MANUFACTURER: WCN_ATTRIBUTE_TYPE = 28
WCN_TYPE_MESSAGE_TYPE: WCN_ATTRIBUTE_TYPE = 29
WCN_TYPE_MODEL_NAME: WCN_ATTRIBUTE_TYPE = 30
WCN_TYPE_MODEL_NUMBER: WCN_ATTRIBUTE_TYPE = 31
WCN_TYPE_NETWORK_INDEX: WCN_ATTRIBUTE_TYPE = 32
WCN_TYPE_NETWORK_KEY: WCN_ATTRIBUTE_TYPE = 33
WCN_TYPE_NETWORK_KEY_INDEX: WCN_ATTRIBUTE_TYPE = 34
WCN_TYPE_NEW_DEVICE_NAME: WCN_ATTRIBUTE_TYPE = 35
WCN_TYPE_NEW_PASSWORD: WCN_ATTRIBUTE_TYPE = 36
WCN_TYPE_OOB_DEVICE_PASSWORD: WCN_ATTRIBUTE_TYPE = 37
WCN_TYPE_OS_VERSION: WCN_ATTRIBUTE_TYPE = 38
WCN_TYPE_POWER_LEVEL: WCN_ATTRIBUTE_TYPE = 39
WCN_TYPE_PSK_CURRENT: WCN_ATTRIBUTE_TYPE = 40
WCN_TYPE_PSK_MAX: WCN_ATTRIBUTE_TYPE = 41
WCN_TYPE_PUBLIC_KEY: WCN_ATTRIBUTE_TYPE = 42
WCN_TYPE_RADIO_ENABLED: WCN_ATTRIBUTE_TYPE = 43
WCN_TYPE_REBOOT: WCN_ATTRIBUTE_TYPE = 44
WCN_TYPE_REGISTRAR_CURRENT: WCN_ATTRIBUTE_TYPE = 45
WCN_TYPE_REGISTRAR_ESTABLISHED: WCN_ATTRIBUTE_TYPE = 46
WCN_TYPE_REGISTRAR_LIST: WCN_ATTRIBUTE_TYPE = 47
WCN_TYPE_REGISTRAR_MAX: WCN_ATTRIBUTE_TYPE = 48
WCN_TYPE_REGISTRAR_NONCE: WCN_ATTRIBUTE_TYPE = 49
WCN_TYPE_REQUEST_TYPE: WCN_ATTRIBUTE_TYPE = 50
WCN_TYPE_RESPONSE_TYPE: WCN_ATTRIBUTE_TYPE = 51
WCN_TYPE_RF_BANDS: WCN_ATTRIBUTE_TYPE = 52
WCN_TYPE_R_HASH1: WCN_ATTRIBUTE_TYPE = 53
WCN_TYPE_R_HASH2: WCN_ATTRIBUTE_TYPE = 54
WCN_TYPE_R_SNONCE1: WCN_ATTRIBUTE_TYPE = 55
WCN_TYPE_R_SNONCE2: WCN_ATTRIBUTE_TYPE = 56
WCN_TYPE_SELECTED_REGISTRAR: WCN_ATTRIBUTE_TYPE = 57
WCN_TYPE_SERIAL_NUMBER: WCN_ATTRIBUTE_TYPE = 58
WCN_TYPE_WI_FI_PROTECTED_SETUP_STATE: WCN_ATTRIBUTE_TYPE = 59
WCN_TYPE_SSID: WCN_ATTRIBUTE_TYPE = 60
WCN_TYPE_TOTAL_NETWORKS: WCN_ATTRIBUTE_TYPE = 61
WCN_TYPE_UUID_E: WCN_ATTRIBUTE_TYPE = 62
WCN_TYPE_UUID_R: WCN_ATTRIBUTE_TYPE = 63
WCN_TYPE_VENDOR_EXTENSION: WCN_ATTRIBUTE_TYPE = 64
WCN_TYPE_VERSION: WCN_ATTRIBUTE_TYPE = 65
WCN_TYPE_X_509_CERTIFICATE_REQUEST: WCN_ATTRIBUTE_TYPE = 66
WCN_TYPE_X_509_CERTIFICATE: WCN_ATTRIBUTE_TYPE = 67
WCN_TYPE_EAP_IDENTITY: WCN_ATTRIBUTE_TYPE = 68
WCN_TYPE_MESSAGE_COUNTER: WCN_ATTRIBUTE_TYPE = 69
WCN_TYPE_PUBLIC_KEY_HASH: WCN_ATTRIBUTE_TYPE = 70
WCN_TYPE_REKEY_KEY: WCN_ATTRIBUTE_TYPE = 71
WCN_TYPE_KEY_LIFETIME: WCN_ATTRIBUTE_TYPE = 72
WCN_TYPE_PERMITTED_CONFIG_METHODS: WCN_ATTRIBUTE_TYPE = 73
WCN_TYPE_SELECTED_REGISTRAR_CONFIG_METHODS: WCN_ATTRIBUTE_TYPE = 74
WCN_TYPE_PRIMARY_DEVICE_TYPE: WCN_ATTRIBUTE_TYPE = 75
WCN_TYPE_SECONDARY_DEVICE_TYPE_LIST: WCN_ATTRIBUTE_TYPE = 76
WCN_TYPE_PORTABLE_DEVICE: WCN_ATTRIBUTE_TYPE = 77
WCN_TYPE_AP_SETUP_LOCKED: WCN_ATTRIBUTE_TYPE = 78
WCN_TYPE_APPLICATION_EXTENSION: WCN_ATTRIBUTE_TYPE = 79
WCN_TYPE_EAP_TYPE: WCN_ATTRIBUTE_TYPE = 80
WCN_TYPE_INITIALIZATION_VECTOR: WCN_ATTRIBUTE_TYPE = 81
WCN_TYPE_KEY_PROVIDED_AUTOMATICALLY: WCN_ATTRIBUTE_TYPE = 82
WCN_TYPE_802_1X_ENABLED: WCN_ATTRIBUTE_TYPE = 83
WCN_TYPE_APPSESSIONKEY: WCN_ATTRIBUTE_TYPE = 84
WCN_TYPE_WEPTRANSMITKEY: WCN_ATTRIBUTE_TYPE = 85
WCN_TYPE_UUID: WCN_ATTRIBUTE_TYPE = 86
WCN_TYPE_PRIMARY_DEVICE_TYPE_CATEGORY: WCN_ATTRIBUTE_TYPE = 87
WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY_OUI: WCN_ATTRIBUTE_TYPE = 88
WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY: WCN_ATTRIBUTE_TYPE = 89
WCN_TYPE_CURRENT_SSID: WCN_ATTRIBUTE_TYPE = 90
WCN_TYPE_BSSID: WCN_ATTRIBUTE_TYPE = 91
WCN_TYPE_DOT11_MAC_ADDRESS: WCN_ATTRIBUTE_TYPE = 92
WCN_TYPE_AUTHORIZED_MACS: WCN_ATTRIBUTE_TYPE = 93
WCN_TYPE_NETWORK_KEY_SHAREABLE: WCN_ATTRIBUTE_TYPE = 94
WCN_TYPE_REQUEST_TO_ENROLL: WCN_ATTRIBUTE_TYPE = 95
WCN_TYPE_REQUESTED_DEVICE_TYPE: WCN_ATTRIBUTE_TYPE = 96
WCN_TYPE_SETTINGS_DELAY_TIME: WCN_ATTRIBUTE_TYPE = 97
WCN_TYPE_VERSION2: WCN_ATTRIBUTE_TYPE = 98
WCN_TYPE_VENDOR_EXTENSION_WFA: WCN_ATTRIBUTE_TYPE = 99
WCN_NUM_ATTRIBUTE_TYPES: WCN_ATTRIBUTE_TYPE = 100
WCN_PASSWORD_TYPE = Int32
WCN_PASSWORD_TYPE_PUSH_BUTTON: WCN_PASSWORD_TYPE = 0
WCN_PASSWORD_TYPE_PIN: WCN_PASSWORD_TYPE = 1
WCN_PASSWORD_TYPE_PIN_REGISTRAR_SPECIFIED: WCN_PASSWORD_TYPE = 2
WCN_PASSWORD_TYPE_OOB_SPECIFIED: WCN_PASSWORD_TYPE = 3
WCN_PASSWORD_TYPE_WFDS: WCN_PASSWORD_TYPE = 4
WCN_SESSION_STATUS = Int32
WCN_SESSION_STATUS_SUCCESS: WCN_SESSION_STATUS = 0
WCN_SESSION_STATUS_FAILURE_GENERIC: WCN_SESSION_STATUS = 1
WCN_SESSION_STATUS_FAILURE_TIMEOUT: WCN_SESSION_STATUS = 2
WCN_VALUE_TYPE_ASSOCIATION_STATE = Int32
WCN_VALUE_AS_NOT_ASSOCIATED: WCN_VALUE_TYPE_ASSOCIATION_STATE = 0
WCN_VALUE_AS_CONNECTION_SUCCESS: WCN_VALUE_TYPE_ASSOCIATION_STATE = 1
WCN_VALUE_AS_CONFIGURATION_FAILURE: WCN_VALUE_TYPE_ASSOCIATION_STATE = 2
WCN_VALUE_AS_ASSOCIATION_FAILURE: WCN_VALUE_TYPE_ASSOCIATION_STATE = 3
WCN_VALUE_AS_IP_FAILURE: WCN_VALUE_TYPE_ASSOCIATION_STATE = 4
WCN_VALUE_TYPE_AUTHENTICATION_TYPE = Int32
WCN_VALUE_AT_OPEN: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 1
WCN_VALUE_AT_WPAPSK: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 2
WCN_VALUE_AT_SHARED: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 4
WCN_VALUE_AT_WPA: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 8
WCN_VALUE_AT_WPA2: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 16
WCN_VALUE_AT_WPA2PSK: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 32
WCN_VALUE_AT_WPAWPA2PSK_MIXED: WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 34
WCN_VALUE_TYPE_BOOLEAN = Int32
WCN_VALUE_FALSE: WCN_VALUE_TYPE_BOOLEAN = 0
WCN_VALUE_TRUE: WCN_VALUE_TYPE_BOOLEAN = 1
WCN_VALUE_TYPE_CONFIGURATION_ERROR = Int32
WCN_VALUE_CE_NO_ERROR: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 0
WCN_VALUE_CE_OOB_INTERFACE_READ_ERROR: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 1
WCN_VALUE_CE_DECRYPTION_CRC_FAILURE: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 2
WCN_VALUE_CE_2_4_CHANNEL_NOT_SUPPORTED: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 3
WCN_VALUE_CE_5_0_CHANNEL_NOT_SUPPORTED: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 4
WCN_VALUE_CE_SIGNAL_TOO_WEAK: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 5
WCN_VALUE_CE_NETWORK_AUTHENTICATION_FAILURE: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 6
WCN_VALUE_CE_NETWORK_ASSOCIATION_FAILURE: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 7
WCN_VALUE_CE_NO_DHCP_RESPONSE: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 8
WCN_VALUE_CE_FAILED_DHCP_CONFIG: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 9
WCN_VALUE_CE_IP_ADDRESS_CONFLICT: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 10
WCN_VALUE_CE_COULD_NOT_CONNECT_TO_REGISTRAR: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 11
WCN_VALUE_CE_MULTIPLE_PBC_SESSIONS_DETECTED: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 12
WCN_VALUE_CE_ROGUE_ACTIVITY_SUSPECTED: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 13
WCN_VALUE_CE_DEVICE_BUSY: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 14
WCN_VALUE_CE_SETUP_LOCKED: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 15
WCN_VALUE_CE_MESSAGE_TIMEOUT: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 16
WCN_VALUE_CE_REGISTRATION_SESSION_TIMEOUT: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 17
WCN_VALUE_CE_DEVICE_PASSWORD_AUTH_FAILURE: WCN_VALUE_TYPE_CONFIGURATION_ERROR = 18
WCN_VALUE_TYPE_CONFIG_METHODS = Int32
WCN_VALUE_CM_USBA: WCN_VALUE_TYPE_CONFIG_METHODS = 1
WCN_VALUE_CM_ETHERNET: WCN_VALUE_TYPE_CONFIG_METHODS = 2
WCN_VALUE_CM_LABEL: WCN_VALUE_TYPE_CONFIG_METHODS = 4
WCN_VALUE_CM_DISPLAY: WCN_VALUE_TYPE_CONFIG_METHODS = 8
WCN_VALUE_CM_EXTERNAL_NFC: WCN_VALUE_TYPE_CONFIG_METHODS = 16
WCN_VALUE_CM_INTEGRATED_NFC: WCN_VALUE_TYPE_CONFIG_METHODS = 32
WCN_VALUE_CM_NFC_INTERFACE: WCN_VALUE_TYPE_CONFIG_METHODS = 64
WCN_VALUE_CM_PUSHBUTTON: WCN_VALUE_TYPE_CONFIG_METHODS = 128
WCN_VALUE_CM_KEYPAD: WCN_VALUE_TYPE_CONFIG_METHODS = 256
WCN_VALUE_CM_VIRT_PUSHBUTTON: WCN_VALUE_TYPE_CONFIG_METHODS = 640
WCN_VALUE_CM_PHYS_PUSHBUTTON: WCN_VALUE_TYPE_CONFIG_METHODS = 1152
WCN_VALUE_CM_VIRT_DISPLAY: WCN_VALUE_TYPE_CONFIG_METHODS = 8200
WCN_VALUE_CM_PHYS_DISPLAY: WCN_VALUE_TYPE_CONFIG_METHODS = 16392
WCN_VALUE_TYPE_CONNECTION_TYPE = Int32
WCN_VALUE_CT_ESS: WCN_VALUE_TYPE_CONNECTION_TYPE = 1
WCN_VALUE_CT_IBSS: WCN_VALUE_TYPE_CONNECTION_TYPE = 2
WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = Int32
WCN_VALUE_DP_DEFAULT: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 0
WCN_VALUE_DP_USER_SPECIFIED: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 1
WCN_VALUE_DP_MACHINE_SPECIFIED: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 2
WCN_VALUE_DP_REKEY: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 3
WCN_VALUE_DP_PUSHBUTTON: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 4
WCN_VALUE_DP_REGISTRAR_SPECIFIED: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 5
WCN_VALUE_DP_NFC_CONNECTION_HANDOVER: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 7
WCN_VALUE_DP_WFD_SERVICES: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 8
WCN_VALUE_DP_OUTOFBAND_MIN: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 16
WCN_VALUE_DP_OUTOFBAND_MAX: WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 65535
WCN_VALUE_TYPE_ENCRYPTION_TYPE = Int32
WCN_VALUE_ET_NONE: WCN_VALUE_TYPE_ENCRYPTION_TYPE = 1
WCN_VALUE_ET_WEP: WCN_VALUE_TYPE_ENCRYPTION_TYPE = 2
WCN_VALUE_ET_TKIP: WCN_VALUE_TYPE_ENCRYPTION_TYPE = 4
WCN_VALUE_ET_AES: WCN_VALUE_TYPE_ENCRYPTION_TYPE = 8
WCN_VALUE_ET_TKIP_AES_MIXED: WCN_VALUE_TYPE_ENCRYPTION_TYPE = 12
WCN_VALUE_TYPE_MESSAGE_TYPE = Int32
WCN_VALUE_MT_BEACON: WCN_VALUE_TYPE_MESSAGE_TYPE = 1
WCN_VALUE_MT_PROBE_REQUEST: WCN_VALUE_TYPE_MESSAGE_TYPE = 2
WCN_VALUE_MT_PROBE_RESPONSE: WCN_VALUE_TYPE_MESSAGE_TYPE = 3
WCN_VALUE_MT_M1: WCN_VALUE_TYPE_MESSAGE_TYPE = 4
WCN_VALUE_MT_M2: WCN_VALUE_TYPE_MESSAGE_TYPE = 5
WCN_VALUE_MT_M2D: WCN_VALUE_TYPE_MESSAGE_TYPE = 6
WCN_VALUE_MT_M3: WCN_VALUE_TYPE_MESSAGE_TYPE = 7
WCN_VALUE_MT_M4: WCN_VALUE_TYPE_MESSAGE_TYPE = 8
WCN_VALUE_MT_M5: WCN_VALUE_TYPE_MESSAGE_TYPE = 9
WCN_VALUE_MT_M6: WCN_VALUE_TYPE_MESSAGE_TYPE = 10
WCN_VALUE_MT_M7: WCN_VALUE_TYPE_MESSAGE_TYPE = 11
WCN_VALUE_MT_M8: WCN_VALUE_TYPE_MESSAGE_TYPE = 12
WCN_VALUE_MT_ACK: WCN_VALUE_TYPE_MESSAGE_TYPE = 13
WCN_VALUE_MT_NACK: WCN_VALUE_TYPE_MESSAGE_TYPE = 14
WCN_VALUE_MT_DONE: WCN_VALUE_TYPE_MESSAGE_TYPE = 15
class WCN_VALUE_TYPE_PRIMARY_DEVICE_TYPE(Structure):
    Category: UInt16
    SubCategoryOUI: UInt32
    SubCategory: UInt16
    _pack_ = 1
WCN_VALUE_TYPE_REQUEST_TYPE = Int32
WCN_VALUE_ReqT_ENROLLEE_INFO: WCN_VALUE_TYPE_REQUEST_TYPE = 0
WCN_VALUE_ReqT_ENROLLEE_OPEN_1X: WCN_VALUE_TYPE_REQUEST_TYPE = 1
WCN_VALUE_ReqT_REGISTRAR: WCN_VALUE_TYPE_REQUEST_TYPE = 2
WCN_VALUE_ReqT_MANAGER_REGISTRAR: WCN_VALUE_TYPE_REQUEST_TYPE = 3
WCN_VALUE_TYPE_RESPONSE_TYPE = Int32
WCN_VALUE_RspT_ENROLLEE_INFO: WCN_VALUE_TYPE_RESPONSE_TYPE = 0
WCN_VALUE_RspT_ENROLLEE_OPEN_1X: WCN_VALUE_TYPE_RESPONSE_TYPE = 1
WCN_VALUE_RspT_REGISTRAR: WCN_VALUE_TYPE_RESPONSE_TYPE = 2
WCN_VALUE_RspT_AP: WCN_VALUE_TYPE_RESPONSE_TYPE = 3
WCN_VALUE_TYPE_RF_BANDS = Int32
WCN_VALUE_RB_24GHZ: WCN_VALUE_TYPE_RF_BANDS = 1
WCN_VALUE_RB_50GHZ: WCN_VALUE_TYPE_RF_BANDS = 2
WCN_VALUE_TYPE_VERSION = Int32
WCN_VALUE_VERSION_1_0: WCN_VALUE_TYPE_VERSION = 16
WCN_VALUE_VERSION_2_0: WCN_VALUE_TYPE_VERSION = 32
WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = Int32
WCN_VALUE_SS_RESERVED00: WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 0
WCN_VALUE_SS_NOT_CONFIGURED: WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 1
WCN_VALUE_SS_CONFIGURED: WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 2
class WCN_VENDOR_EXTENSION_SPEC(Structure):
    VendorId: UInt32
    SubType: UInt32
    Index: UInt32
    Flags: UInt32
make_head(_module, 'PKEY_WCN_DeviceType_Category')
make_head(_module, 'PKEY_WCN_DeviceType_SubCategoryOUI')
make_head(_module, 'PKEY_WCN_DeviceType_SubCategory')
make_head(_module, 'PKEY_WCN_SSID')
make_head(_module, 'IWCNConnectNotify')
make_head(_module, 'IWCNDevice')
make_head(_module, 'WCN_VALUE_TYPE_PRIMARY_DEVICE_TYPE')
make_head(_module, 'WCN_VENDOR_EXTENSION_SPEC')
__all__ = [
    "IWCNConnectNotify",
    "IWCNDevice",
    "PKEY_WCN_DeviceType_Category",
    "PKEY_WCN_DeviceType_SubCategory",
    "PKEY_WCN_DeviceType_SubCategoryOUI",
    "PKEY_WCN_SSID",
    "SID_WcnProvider",
    "WCNDeviceObject",
    "WCN_API_MAX_BUFFER_SIZE",
    "WCN_ATTRIBUTE_TYPE",
    "WCN_E_AUTHENTICATION_FAILED",
    "WCN_E_CONNECTION_REJECTED",
    "WCN_E_PEER_NOT_FOUND",
    "WCN_E_PROTOCOL_ERROR",
    "WCN_E_SESSION_TIMEDOUT",
    "WCN_FLAG_AUTHENTICATED_VE",
    "WCN_FLAG_DISCOVERY_VE",
    "WCN_FLAG_ENCRYPTED_VE",
    "WCN_MICROSOFT_VENDOR_ID",
    "WCN_NO_SUBTYPE",
    "WCN_NUM_ATTRIBUTE_TYPES",
    "WCN_PASSWORD_TYPE",
    "WCN_PASSWORD_TYPE_OOB_SPECIFIED",
    "WCN_PASSWORD_TYPE_PIN",
    "WCN_PASSWORD_TYPE_PIN_REGISTRAR_SPECIFIED",
    "WCN_PASSWORD_TYPE_PUSH_BUTTON",
    "WCN_PASSWORD_TYPE_WFDS",
    "WCN_QUERY_CONSTRAINT_USE_SOFTAP",
    "WCN_SESSION_STATUS",
    "WCN_SESSION_STATUS_FAILURE_GENERIC",
    "WCN_SESSION_STATUS_FAILURE_TIMEOUT",
    "WCN_SESSION_STATUS_SUCCESS",
    "WCN_TYPE_802_1X_ENABLED",
    "WCN_TYPE_APPLICATION_EXTENSION",
    "WCN_TYPE_APPSESSIONKEY",
    "WCN_TYPE_AP_CHANNEL",
    "WCN_TYPE_AP_SETUP_LOCKED",
    "WCN_TYPE_ASSOCIATION_STATE",
    "WCN_TYPE_AUTHENTICATION_TYPE",
    "WCN_TYPE_AUTHENTICATION_TYPE_FLAGS",
    "WCN_TYPE_AUTHENTICATOR",
    "WCN_TYPE_AUTHORIZED_MACS",
    "WCN_TYPE_BSSID",
    "WCN_TYPE_CONFIGURATION_ERROR",
    "WCN_TYPE_CONFIG_METHODS",
    "WCN_TYPE_CONFIRMATION_URL4",
    "WCN_TYPE_CONFIRMATION_URL6",
    "WCN_TYPE_CONNECTION_TYPE",
    "WCN_TYPE_CONNECTION_TYPE_FLAGS",
    "WCN_TYPE_CREDENTIAL",
    "WCN_TYPE_CURRENT_SSID",
    "WCN_TYPE_DEVICE_NAME",
    "WCN_TYPE_DEVICE_PASSWORD_ID",
    "WCN_TYPE_DOT11_MAC_ADDRESS",
    "WCN_TYPE_EAP_IDENTITY",
    "WCN_TYPE_EAP_TYPE",
    "WCN_TYPE_ENCRYPTED_SETTINGS",
    "WCN_TYPE_ENCRYPTION_TYPE",
    "WCN_TYPE_ENCRYPTION_TYPE_FLAGS",
    "WCN_TYPE_ENROLLEE_NONCE",
    "WCN_TYPE_E_HASH1",
    "WCN_TYPE_E_HASH2",
    "WCN_TYPE_E_SNONCE1",
    "WCN_TYPE_E_SNONCE2",
    "WCN_TYPE_FEATURE_ID",
    "WCN_TYPE_IDENTITY",
    "WCN_TYPE_IDENTITY_PROOF",
    "WCN_TYPE_INITIALIZATION_VECTOR",
    "WCN_TYPE_KEY_IDENTIFIER",
    "WCN_TYPE_KEY_LIFETIME",
    "WCN_TYPE_KEY_PROVIDED_AUTOMATICALLY",
    "WCN_TYPE_KEY_WRAP_AUTHENTICATOR",
    "WCN_TYPE_MAC_ADDRESS",
    "WCN_TYPE_MANUFACTURER",
    "WCN_TYPE_MESSAGE_COUNTER",
    "WCN_TYPE_MESSAGE_TYPE",
    "WCN_TYPE_MODEL_NAME",
    "WCN_TYPE_MODEL_NUMBER",
    "WCN_TYPE_NETWORK_INDEX",
    "WCN_TYPE_NETWORK_KEY",
    "WCN_TYPE_NETWORK_KEY_INDEX",
    "WCN_TYPE_NETWORK_KEY_SHAREABLE",
    "WCN_TYPE_NEW_DEVICE_NAME",
    "WCN_TYPE_NEW_PASSWORD",
    "WCN_TYPE_OOB_DEVICE_PASSWORD",
    "WCN_TYPE_OS_VERSION",
    "WCN_TYPE_PERMITTED_CONFIG_METHODS",
    "WCN_TYPE_PORTABLE_DEVICE",
    "WCN_TYPE_POWER_LEVEL",
    "WCN_TYPE_PRIMARY_DEVICE_TYPE",
    "WCN_TYPE_PRIMARY_DEVICE_TYPE_CATEGORY",
    "WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY",
    "WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY_OUI",
    "WCN_TYPE_PSK_CURRENT",
    "WCN_TYPE_PSK_MAX",
    "WCN_TYPE_PUBLIC_KEY",
    "WCN_TYPE_PUBLIC_KEY_HASH",
    "WCN_TYPE_RADIO_ENABLED",
    "WCN_TYPE_REBOOT",
    "WCN_TYPE_REGISTRAR_CURRENT",
    "WCN_TYPE_REGISTRAR_ESTABLISHED",
    "WCN_TYPE_REGISTRAR_LIST",
    "WCN_TYPE_REGISTRAR_MAX",
    "WCN_TYPE_REGISTRAR_NONCE",
    "WCN_TYPE_REKEY_KEY",
    "WCN_TYPE_REQUESTED_DEVICE_TYPE",
    "WCN_TYPE_REQUEST_TO_ENROLL",
    "WCN_TYPE_REQUEST_TYPE",
    "WCN_TYPE_RESPONSE_TYPE",
    "WCN_TYPE_RF_BANDS",
    "WCN_TYPE_R_HASH1",
    "WCN_TYPE_R_HASH2",
    "WCN_TYPE_R_SNONCE1",
    "WCN_TYPE_R_SNONCE2",
    "WCN_TYPE_SECONDARY_DEVICE_TYPE_LIST",
    "WCN_TYPE_SELECTED_REGISTRAR",
    "WCN_TYPE_SELECTED_REGISTRAR_CONFIG_METHODS",
    "WCN_TYPE_SERIAL_NUMBER",
    "WCN_TYPE_SETTINGS_DELAY_TIME",
    "WCN_TYPE_SSID",
    "WCN_TYPE_TOTAL_NETWORKS",
    "WCN_TYPE_UUID",
    "WCN_TYPE_UUID_E",
    "WCN_TYPE_UUID_R",
    "WCN_TYPE_VENDOR_EXTENSION",
    "WCN_TYPE_VENDOR_EXTENSION_WFA",
    "WCN_TYPE_VERSION",
    "WCN_TYPE_VERSION2",
    "WCN_TYPE_WEPTRANSMITKEY",
    "WCN_TYPE_WI_FI_PROTECTED_SETUP_STATE",
    "WCN_TYPE_X_509_CERTIFICATE",
    "WCN_TYPE_X_509_CERTIFICATE_REQUEST",
    "WCN_VALUE_AS_ASSOCIATION_FAILURE",
    "WCN_VALUE_AS_CONFIGURATION_FAILURE",
    "WCN_VALUE_AS_CONNECTION_SUCCESS",
    "WCN_VALUE_AS_IP_FAILURE",
    "WCN_VALUE_AS_NOT_ASSOCIATED",
    "WCN_VALUE_AT_OPEN",
    "WCN_VALUE_AT_SHARED",
    "WCN_VALUE_AT_WPA",
    "WCN_VALUE_AT_WPA2",
    "WCN_VALUE_AT_WPA2PSK",
    "WCN_VALUE_AT_WPAPSK",
    "WCN_VALUE_AT_WPAWPA2PSK_MIXED",
    "WCN_VALUE_CE_2_4_CHANNEL_NOT_SUPPORTED",
    "WCN_VALUE_CE_5_0_CHANNEL_NOT_SUPPORTED",
    "WCN_VALUE_CE_COULD_NOT_CONNECT_TO_REGISTRAR",
    "WCN_VALUE_CE_DECRYPTION_CRC_FAILURE",
    "WCN_VALUE_CE_DEVICE_BUSY",
    "WCN_VALUE_CE_DEVICE_PASSWORD_AUTH_FAILURE",
    "WCN_VALUE_CE_FAILED_DHCP_CONFIG",
    "WCN_VALUE_CE_IP_ADDRESS_CONFLICT",
    "WCN_VALUE_CE_MESSAGE_TIMEOUT",
    "WCN_VALUE_CE_MULTIPLE_PBC_SESSIONS_DETECTED",
    "WCN_VALUE_CE_NETWORK_ASSOCIATION_FAILURE",
    "WCN_VALUE_CE_NETWORK_AUTHENTICATION_FAILURE",
    "WCN_VALUE_CE_NO_DHCP_RESPONSE",
    "WCN_VALUE_CE_NO_ERROR",
    "WCN_VALUE_CE_OOB_INTERFACE_READ_ERROR",
    "WCN_VALUE_CE_REGISTRATION_SESSION_TIMEOUT",
    "WCN_VALUE_CE_ROGUE_ACTIVITY_SUSPECTED",
    "WCN_VALUE_CE_SETUP_LOCKED",
    "WCN_VALUE_CE_SIGNAL_TOO_WEAK",
    "WCN_VALUE_CM_DISPLAY",
    "WCN_VALUE_CM_ETHERNET",
    "WCN_VALUE_CM_EXTERNAL_NFC",
    "WCN_VALUE_CM_INTEGRATED_NFC",
    "WCN_VALUE_CM_KEYPAD",
    "WCN_VALUE_CM_LABEL",
    "WCN_VALUE_CM_NFC_INTERFACE",
    "WCN_VALUE_CM_PHYS_DISPLAY",
    "WCN_VALUE_CM_PHYS_PUSHBUTTON",
    "WCN_VALUE_CM_PUSHBUTTON",
    "WCN_VALUE_CM_USBA",
    "WCN_VALUE_CM_VIRT_DISPLAY",
    "WCN_VALUE_CM_VIRT_PUSHBUTTON",
    "WCN_VALUE_CT_ESS",
    "WCN_VALUE_CT_IBSS",
    "WCN_VALUE_DP_DEFAULT",
    "WCN_VALUE_DP_MACHINE_SPECIFIED",
    "WCN_VALUE_DP_NFC_CONNECTION_HANDOVER",
    "WCN_VALUE_DP_OUTOFBAND_MAX",
    "WCN_VALUE_DP_OUTOFBAND_MIN",
    "WCN_VALUE_DP_PUSHBUTTON",
    "WCN_VALUE_DP_REGISTRAR_SPECIFIED",
    "WCN_VALUE_DP_REKEY",
    "WCN_VALUE_DP_USER_SPECIFIED",
    "WCN_VALUE_DP_WFD_SERVICES",
    "WCN_VALUE_DT_CATEGORY_AUDIO_DEVICE",
    "WCN_VALUE_DT_CATEGORY_CAMERA",
    "WCN_VALUE_DT_CATEGORY_COMPUTER",
    "WCN_VALUE_DT_CATEGORY_DISPLAY",
    "WCN_VALUE_DT_CATEGORY_GAMING_DEVICE",
    "WCN_VALUE_DT_CATEGORY_INPUT_DEVICE",
    "WCN_VALUE_DT_CATEGORY_MULTIMEDIA_DEVICE",
    "WCN_VALUE_DT_CATEGORY_NETWORK_INFRASTRUCTURE",
    "WCN_VALUE_DT_CATEGORY_OTHER",
    "WCN_VALUE_DT_CATEGORY_PRINTER",
    "WCN_VALUE_DT_CATEGORY_STORAGE",
    "WCN_VALUE_DT_CATEGORY_TELEPHONE",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HEADPHONES",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HEADSET",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__HOMETHEATER",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__MICROPHONE",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__PMP",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__SPEAKERS",
    "WCN_VALUE_DT_SUBTYPE_AUDIO_DEVICE__TUNER_RECEIVER",
    "WCN_VALUE_DT_SUBTYPE_CAMERA__SECURITY_CAMERA",
    "WCN_VALUE_DT_SUBTYPE_CAMERA__STILL_CAMERA",
    "WCN_VALUE_DT_SUBTYPE_CAMERA__VIDEO_CAMERA",
    "WCN_VALUE_DT_SUBTYPE_CAMERA__WEB_CAMERA",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__DESKTOP",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__MEDIACENTER",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__MID",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__NETBOOK",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__NOTEBOOK",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__PC",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__SERVER",
    "WCN_VALUE_DT_SUBTYPE_COMPUTER__ULTRAMOBILEPC",
    "WCN_VALUE_DT_SUBTYPE_DISPLAY__MONITOR",
    "WCN_VALUE_DT_SUBTYPE_DISPLAY__PICTURE_FRAME",
    "WCN_VALUE_DT_SUBTYPE_DISPLAY__PROJECTOR",
    "WCN_VALUE_DT_SUBTYPE_DISPLAY__TELEVISION",
    "WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__CONSOLE_ADAPT",
    "WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__PLAYSTATION",
    "WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__PORTABLE",
    "WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__XBOX",
    "WCN_VALUE_DT_SUBTYPE_GAMING_DEVICE__XBOX360",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__BARCODEREADER",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__BIOMETRICREADER",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__GAMECONTROLLER",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__JOYSTICK",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__KEYBOARD",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__MOUSE",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__REMOTE",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__TOUCHSCREEN",
    "WCN_VALUE_DT_SUBTYPE_INPUT_DEVICE__TRACKBALL",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__DAR",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__MCX",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__MEDIA_SERVER_ADAPT_EXT",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__PVP",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__PVR",
    "WCN_VALUE_DT_SUBTYPE_MULTIMEDIA_DEVICE__SETTOPBOX",
    "WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__AP",
    "WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__BRIDGE",
    "WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__GATEWAY",
    "WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__ROUTER",
    "WCN_VALUE_DT_SUBTYPE_NETWORK_INFRASTRUCUTURE__SWITCH",
    "WCN_VALUE_DT_SUBTYPE_PRINTER__ALLINONE",
    "WCN_VALUE_DT_SUBTYPE_PRINTER__COPIER",
    "WCN_VALUE_DT_SUBTYPE_PRINTER__FAX",
    "WCN_VALUE_DT_SUBTYPE_PRINTER__PRINTER",
    "WCN_VALUE_DT_SUBTYPE_PRINTER__SCANNER",
    "WCN_VALUE_DT_SUBTYPE_STORAGE__NAS",
    "WCN_VALUE_DT_SUBTYPE_TELEPHONE__PHONE_DUALMODE",
    "WCN_VALUE_DT_SUBTYPE_TELEPHONE__PHONE_SINGLEMODE",
    "WCN_VALUE_DT_SUBTYPE_TELEPHONE__SMARTPHONE_DUALMODE",
    "WCN_VALUE_DT_SUBTYPE_TELEPHONE__SMARTPHONE_SINGLEMODE",
    "WCN_VALUE_DT_SUBTYPE_TELEPHONE__WINDOWS_MOBILE",
    "WCN_VALUE_DT_SUBTYPE_WIFI_OUI",
    "WCN_VALUE_ET_AES",
    "WCN_VALUE_ET_NONE",
    "WCN_VALUE_ET_TKIP",
    "WCN_VALUE_ET_TKIP_AES_MIXED",
    "WCN_VALUE_ET_WEP",
    "WCN_VALUE_FALSE",
    "WCN_VALUE_MT_ACK",
    "WCN_VALUE_MT_BEACON",
    "WCN_VALUE_MT_DONE",
    "WCN_VALUE_MT_M1",
    "WCN_VALUE_MT_M2",
    "WCN_VALUE_MT_M2D",
    "WCN_VALUE_MT_M3",
    "WCN_VALUE_MT_M4",
    "WCN_VALUE_MT_M5",
    "WCN_VALUE_MT_M6",
    "WCN_VALUE_MT_M7",
    "WCN_VALUE_MT_M8",
    "WCN_VALUE_MT_NACK",
    "WCN_VALUE_MT_PROBE_REQUEST",
    "WCN_VALUE_MT_PROBE_RESPONSE",
    "WCN_VALUE_RB_24GHZ",
    "WCN_VALUE_RB_50GHZ",
    "WCN_VALUE_ReqT_ENROLLEE_INFO",
    "WCN_VALUE_ReqT_ENROLLEE_OPEN_1X",
    "WCN_VALUE_ReqT_MANAGER_REGISTRAR",
    "WCN_VALUE_ReqT_REGISTRAR",
    "WCN_VALUE_RspT_AP",
    "WCN_VALUE_RspT_ENROLLEE_INFO",
    "WCN_VALUE_RspT_ENROLLEE_OPEN_1X",
    "WCN_VALUE_RspT_REGISTRAR",
    "WCN_VALUE_SS_CONFIGURED",
    "WCN_VALUE_SS_NOT_CONFIGURED",
    "WCN_VALUE_SS_RESERVED00",
    "WCN_VALUE_TRUE",
    "WCN_VALUE_TYPE_ASSOCIATION_STATE",
    "WCN_VALUE_TYPE_AUTHENTICATION_TYPE",
    "WCN_VALUE_TYPE_BOOLEAN",
    "WCN_VALUE_TYPE_CONFIGURATION_ERROR",
    "WCN_VALUE_TYPE_CONFIG_METHODS",
    "WCN_VALUE_TYPE_CONNECTION_TYPE",
    "WCN_VALUE_TYPE_DEVICE_PASSWORD_ID",
    "WCN_VALUE_TYPE_ENCRYPTION_TYPE",
    "WCN_VALUE_TYPE_MESSAGE_TYPE",
    "WCN_VALUE_TYPE_PRIMARY_DEVICE_TYPE",
    "WCN_VALUE_TYPE_REQUEST_TYPE",
    "WCN_VALUE_TYPE_RESPONSE_TYPE",
    "WCN_VALUE_TYPE_RF_BANDS",
    "WCN_VALUE_TYPE_VERSION",
    "WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE",
    "WCN_VALUE_VERSION_1_0",
    "WCN_VALUE_VERSION_2_0",
    "WCN_VENDOR_EXTENSION_SPEC",
]
_arch_optional = [
]
