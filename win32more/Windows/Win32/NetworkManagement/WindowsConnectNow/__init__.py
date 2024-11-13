from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WindowsConnectNow
import win32more.Windows.Win32.System.Com
WCN_E_PEER_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147206143
WCN_E_AUTHENTICATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147206142
WCN_E_CONNECTION_REJECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147206141
WCN_E_SESSION_TIMEDOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147206140
WCN_E_PROTOCOL_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147206139
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
SID_WcnProvider: Guid = Guid('{c100beca-d33a-4a4b-bf23-bbef4663d017}')
PKEY_WCN_DeviceType_Category: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{88190b8b-4684-11da-a26a-0002b3988e81}'), pid=16)
PKEY_WCN_DeviceType_SubCategoryOUI: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{88190b8b-4684-11da-a26a-0002b3988e81}'), pid=17)
PKEY_WCN_DeviceType_SubCategory: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{88190b8b-4684-11da-a26a-0002b3988e81}'), pid=18)
PKEY_WCN_SSID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{88190b8b-4684-11da-a26a-0002b3988e81}'), pid=32)
class IWCNConnectNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c100be9f-d33a-4a4b-bf23-bbef4663d017}')
    @commethod(3)
    def ConnectSucceeded(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConnectFailed(self, hrFailure: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWCNDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c100be9c-d33a-4a4b-bf23-bbef4663d017}')
    @commethod(3)
    def SetPassword(self, Type: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE, dwPasswordLength: UInt32, pbPassword: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(self, pNotify: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.IWCNConnectNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttribute(self, AttributeType: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, dwMaxBufferSize: UInt32, pbBuffer: POINTER(Byte), pdwBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIntegerAttribute(self, AttributeType: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, puInteger: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStringAttribute(self, AttributeType: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE, cchMaxString: UInt32, wszString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetworkProfile(self, cchMaxStringLength: UInt32, wszProfile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetNetworkProfile(self, pszProfileXml: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetVendorExtension(self, pVendorExtSpec: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VENDOR_EXTENSION_SPEC), dwMaxBufferSize: UInt32, pbBuffer: POINTER(Byte), pdwBufferUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetVendorExtension(self, pVendorExtSpec: POINTER(win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VENDOR_EXTENSION_SPEC), cbBuffer: UInt32, pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Unadvise(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetNFCPasswordParams(self, Type: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE, dwOOBPasswordID: UInt32, dwPasswordLength: UInt32, pbPassword: POINTER(Byte), dwRemotePublicKeyHashLength: UInt32, pbRemotePublicKeyHash: POINTER(Byte), dwDHKeyBlobLength: UInt32, pbDHKeyBlob: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WCNDeviceObject = Guid('{c100bea7-d33a-4a4b-bf23-bbef4663d017}')
WCN_ATTRIBUTE_TYPE = Int32
WCN_TYPE_AP_CHANNEL: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 0
WCN_TYPE_ASSOCIATION_STATE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 1
WCN_TYPE_AUTHENTICATION_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 2
WCN_TYPE_AUTHENTICATION_TYPE_FLAGS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 3
WCN_TYPE_AUTHENTICATOR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 4
WCN_TYPE_CONFIG_METHODS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 5
WCN_TYPE_CONFIGURATION_ERROR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 6
WCN_TYPE_CONFIRMATION_URL4: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 7
WCN_TYPE_CONFIRMATION_URL6: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 8
WCN_TYPE_CONNECTION_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 9
WCN_TYPE_CONNECTION_TYPE_FLAGS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 10
WCN_TYPE_CREDENTIAL: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 11
WCN_TYPE_DEVICE_NAME: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 12
WCN_TYPE_DEVICE_PASSWORD_ID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 13
WCN_TYPE_E_HASH1: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 14
WCN_TYPE_E_HASH2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 15
WCN_TYPE_E_SNONCE1: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 16
WCN_TYPE_E_SNONCE2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 17
WCN_TYPE_ENCRYPTED_SETTINGS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 18
WCN_TYPE_ENCRYPTION_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 19
WCN_TYPE_ENCRYPTION_TYPE_FLAGS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 20
WCN_TYPE_ENROLLEE_NONCE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 21
WCN_TYPE_FEATURE_ID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 22
WCN_TYPE_IDENTITY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 23
WCN_TYPE_IDENTITY_PROOF: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 24
WCN_TYPE_KEY_WRAP_AUTHENTICATOR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 25
WCN_TYPE_KEY_IDENTIFIER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 26
WCN_TYPE_MAC_ADDRESS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 27
WCN_TYPE_MANUFACTURER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 28
WCN_TYPE_MESSAGE_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 29
WCN_TYPE_MODEL_NAME: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 30
WCN_TYPE_MODEL_NUMBER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 31
WCN_TYPE_NETWORK_INDEX: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 32
WCN_TYPE_NETWORK_KEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 33
WCN_TYPE_NETWORK_KEY_INDEX: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 34
WCN_TYPE_NEW_DEVICE_NAME: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 35
WCN_TYPE_NEW_PASSWORD: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 36
WCN_TYPE_OOB_DEVICE_PASSWORD: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 37
WCN_TYPE_OS_VERSION: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 38
WCN_TYPE_POWER_LEVEL: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 39
WCN_TYPE_PSK_CURRENT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 40
WCN_TYPE_PSK_MAX: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 41
WCN_TYPE_PUBLIC_KEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 42
WCN_TYPE_RADIO_ENABLED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 43
WCN_TYPE_REBOOT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 44
WCN_TYPE_REGISTRAR_CURRENT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 45
WCN_TYPE_REGISTRAR_ESTABLISHED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 46
WCN_TYPE_REGISTRAR_LIST: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 47
WCN_TYPE_REGISTRAR_MAX: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 48
WCN_TYPE_REGISTRAR_NONCE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 49
WCN_TYPE_REQUEST_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 50
WCN_TYPE_RESPONSE_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 51
WCN_TYPE_RF_BANDS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 52
WCN_TYPE_R_HASH1: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 53
WCN_TYPE_R_HASH2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 54
WCN_TYPE_R_SNONCE1: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 55
WCN_TYPE_R_SNONCE2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 56
WCN_TYPE_SELECTED_REGISTRAR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 57
WCN_TYPE_SERIAL_NUMBER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 58
WCN_TYPE_WI_FI_PROTECTED_SETUP_STATE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 59
WCN_TYPE_SSID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 60
WCN_TYPE_TOTAL_NETWORKS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 61
WCN_TYPE_UUID_E: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 62
WCN_TYPE_UUID_R: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 63
WCN_TYPE_VENDOR_EXTENSION: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 64
WCN_TYPE_VERSION: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 65
WCN_TYPE_X_509_CERTIFICATE_REQUEST: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 66
WCN_TYPE_X_509_CERTIFICATE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 67
WCN_TYPE_EAP_IDENTITY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 68
WCN_TYPE_MESSAGE_COUNTER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 69
WCN_TYPE_PUBLIC_KEY_HASH: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 70
WCN_TYPE_REKEY_KEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 71
WCN_TYPE_KEY_LIFETIME: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 72
WCN_TYPE_PERMITTED_CONFIG_METHODS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 73
WCN_TYPE_SELECTED_REGISTRAR_CONFIG_METHODS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 74
WCN_TYPE_PRIMARY_DEVICE_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 75
WCN_TYPE_SECONDARY_DEVICE_TYPE_LIST: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 76
WCN_TYPE_PORTABLE_DEVICE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 77
WCN_TYPE_AP_SETUP_LOCKED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 78
WCN_TYPE_APPLICATION_EXTENSION: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 79
WCN_TYPE_EAP_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 80
WCN_TYPE_INITIALIZATION_VECTOR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 81
WCN_TYPE_KEY_PROVIDED_AUTOMATICALLY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 82
WCN_TYPE_802_1X_ENABLED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 83
WCN_TYPE_APPSESSIONKEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 84
WCN_TYPE_WEPTRANSMITKEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 85
WCN_TYPE_UUID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 86
WCN_TYPE_PRIMARY_DEVICE_TYPE_CATEGORY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 87
WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY_OUI: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 88
WCN_TYPE_PRIMARY_DEVICE_TYPE_SUBCATEGORY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 89
WCN_TYPE_CURRENT_SSID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 90
WCN_TYPE_BSSID: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 91
WCN_TYPE_DOT11_MAC_ADDRESS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 92
WCN_TYPE_AUTHORIZED_MACS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 93
WCN_TYPE_NETWORK_KEY_SHAREABLE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 94
WCN_TYPE_REQUEST_TO_ENROLL: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 95
WCN_TYPE_REQUESTED_DEVICE_TYPE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 96
WCN_TYPE_SETTINGS_DELAY_TIME: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 97
WCN_TYPE_VERSION2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 98
WCN_TYPE_VENDOR_EXTENSION_WFA: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 99
WCN_NUM_ATTRIBUTE_TYPES: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_ATTRIBUTE_TYPE = 100
WCN_PASSWORD_TYPE = Int32
WCN_PASSWORD_TYPE_PUSH_BUTTON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE = 0
WCN_PASSWORD_TYPE_PIN: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE = 1
WCN_PASSWORD_TYPE_PIN_REGISTRAR_SPECIFIED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE = 2
WCN_PASSWORD_TYPE_OOB_SPECIFIED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE = 3
WCN_PASSWORD_TYPE_WFDS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_PASSWORD_TYPE = 4
WCN_SESSION_STATUS = Int32
WCN_SESSION_STATUS_SUCCESS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_SESSION_STATUS = 0
WCN_SESSION_STATUS_FAILURE_GENERIC: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_SESSION_STATUS = 1
WCN_SESSION_STATUS_FAILURE_TIMEOUT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_SESSION_STATUS = 2
WCN_VALUE_TYPE_ASSOCIATION_STATE = Int32
WCN_VALUE_AS_NOT_ASSOCIATED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ASSOCIATION_STATE = 0
WCN_VALUE_AS_CONNECTION_SUCCESS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ASSOCIATION_STATE = 1
WCN_VALUE_AS_CONFIGURATION_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ASSOCIATION_STATE = 2
WCN_VALUE_AS_ASSOCIATION_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ASSOCIATION_STATE = 3
WCN_VALUE_AS_IP_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ASSOCIATION_STATE = 4
WCN_VALUE_TYPE_AUTHENTICATION_TYPE = Int32
WCN_VALUE_AT_OPEN: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 1
WCN_VALUE_AT_WPAPSK: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 2
WCN_VALUE_AT_SHARED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 4
WCN_VALUE_AT_WPA: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 8
WCN_VALUE_AT_WPA2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 16
WCN_VALUE_AT_WPA2PSK: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 32
WCN_VALUE_AT_WPAWPA2PSK_MIXED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_AUTHENTICATION_TYPE = 34
WCN_VALUE_TYPE_BOOLEAN = Int32
WCN_VALUE_FALSE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_BOOLEAN = 0
WCN_VALUE_TRUE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_BOOLEAN = 1
WCN_VALUE_TYPE_CONFIGURATION_ERROR = Int32
WCN_VALUE_CE_NO_ERROR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 0
WCN_VALUE_CE_OOB_INTERFACE_READ_ERROR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 1
WCN_VALUE_CE_DECRYPTION_CRC_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 2
WCN_VALUE_CE_2_4_CHANNEL_NOT_SUPPORTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 3
WCN_VALUE_CE_5_0_CHANNEL_NOT_SUPPORTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 4
WCN_VALUE_CE_SIGNAL_TOO_WEAK: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 5
WCN_VALUE_CE_NETWORK_AUTHENTICATION_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 6
WCN_VALUE_CE_NETWORK_ASSOCIATION_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 7
WCN_VALUE_CE_NO_DHCP_RESPONSE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 8
WCN_VALUE_CE_FAILED_DHCP_CONFIG: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 9
WCN_VALUE_CE_IP_ADDRESS_CONFLICT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 10
WCN_VALUE_CE_COULD_NOT_CONNECT_TO_REGISTRAR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 11
WCN_VALUE_CE_MULTIPLE_PBC_SESSIONS_DETECTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 12
WCN_VALUE_CE_ROGUE_ACTIVITY_SUSPECTED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 13
WCN_VALUE_CE_DEVICE_BUSY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 14
WCN_VALUE_CE_SETUP_LOCKED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 15
WCN_VALUE_CE_MESSAGE_TIMEOUT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 16
WCN_VALUE_CE_REGISTRATION_SESSION_TIMEOUT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 17
WCN_VALUE_CE_DEVICE_PASSWORD_AUTH_FAILURE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIGURATION_ERROR = 18
WCN_VALUE_TYPE_CONFIG_METHODS = Int32
WCN_VALUE_CM_USBA: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 1
WCN_VALUE_CM_ETHERNET: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 2
WCN_VALUE_CM_LABEL: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 4
WCN_VALUE_CM_DISPLAY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 8
WCN_VALUE_CM_EXTERNAL_NFC: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 16
WCN_VALUE_CM_INTEGRATED_NFC: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 32
WCN_VALUE_CM_NFC_INTERFACE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 64
WCN_VALUE_CM_PUSHBUTTON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 128
WCN_VALUE_CM_KEYPAD: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 256
WCN_VALUE_CM_VIRT_PUSHBUTTON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 640
WCN_VALUE_CM_PHYS_PUSHBUTTON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 1152
WCN_VALUE_CM_VIRT_DISPLAY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 8200
WCN_VALUE_CM_PHYS_DISPLAY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONFIG_METHODS = 16392
WCN_VALUE_TYPE_CONNECTION_TYPE = Int32
WCN_VALUE_CT_ESS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONNECTION_TYPE = 1
WCN_VALUE_CT_IBSS: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_CONNECTION_TYPE = 2
WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = Int32
WCN_VALUE_DP_DEFAULT: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 0
WCN_VALUE_DP_USER_SPECIFIED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 1
WCN_VALUE_DP_MACHINE_SPECIFIED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 2
WCN_VALUE_DP_REKEY: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 3
WCN_VALUE_DP_PUSHBUTTON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 4
WCN_VALUE_DP_REGISTRAR_SPECIFIED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 5
WCN_VALUE_DP_NFC_CONNECTION_HANDOVER: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 7
WCN_VALUE_DP_WFD_SERVICES: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 8
WCN_VALUE_DP_OUTOFBAND_MIN: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 16
WCN_VALUE_DP_OUTOFBAND_MAX: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_DEVICE_PASSWORD_ID = 65535
WCN_VALUE_TYPE_ENCRYPTION_TYPE = Int32
WCN_VALUE_ET_NONE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ENCRYPTION_TYPE = 1
WCN_VALUE_ET_WEP: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ENCRYPTION_TYPE = 2
WCN_VALUE_ET_TKIP: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ENCRYPTION_TYPE = 4
WCN_VALUE_ET_AES: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ENCRYPTION_TYPE = 8
WCN_VALUE_ET_TKIP_AES_MIXED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_ENCRYPTION_TYPE = 12
WCN_VALUE_TYPE_MESSAGE_TYPE = Int32
WCN_VALUE_MT_BEACON: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 1
WCN_VALUE_MT_PROBE_REQUEST: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 2
WCN_VALUE_MT_PROBE_RESPONSE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 3
WCN_VALUE_MT_M1: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 4
WCN_VALUE_MT_M2: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 5
WCN_VALUE_MT_M2D: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 6
WCN_VALUE_MT_M3: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 7
WCN_VALUE_MT_M4: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 8
WCN_VALUE_MT_M5: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 9
WCN_VALUE_MT_M6: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 10
WCN_VALUE_MT_M7: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 11
WCN_VALUE_MT_M8: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 12
WCN_VALUE_MT_ACK: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 13
WCN_VALUE_MT_NACK: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 14
WCN_VALUE_MT_DONE: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_MESSAGE_TYPE = 15
class WCN_VALUE_TYPE_PRIMARY_DEVICE_TYPE(Structure):
    Category: UInt16
    SubCategoryOUI: UInt32
    SubCategory: UInt16
    _pack_ = 1
WCN_VALUE_TYPE_REQUEST_TYPE = Int32
WCN_VALUE_ReqT_ENROLLEE_INFO: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_REQUEST_TYPE = 0
WCN_VALUE_ReqT_ENROLLEE_OPEN_1X: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_REQUEST_TYPE = 1
WCN_VALUE_ReqT_REGISTRAR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_REQUEST_TYPE = 2
WCN_VALUE_ReqT_MANAGER_REGISTRAR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_REQUEST_TYPE = 3
WCN_VALUE_TYPE_RESPONSE_TYPE = Int32
WCN_VALUE_RspT_ENROLLEE_INFO: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RESPONSE_TYPE = 0
WCN_VALUE_RspT_ENROLLEE_OPEN_1X: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RESPONSE_TYPE = 1
WCN_VALUE_RspT_REGISTRAR: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RESPONSE_TYPE = 2
WCN_VALUE_RspT_AP: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RESPONSE_TYPE = 3
WCN_VALUE_TYPE_RF_BANDS = Int32
WCN_VALUE_RB_24GHZ: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RF_BANDS = 1
WCN_VALUE_RB_50GHZ: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_RF_BANDS = 2
WCN_VALUE_TYPE_VERSION = Int32
WCN_VALUE_VERSION_1_0: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_VERSION = 16
WCN_VALUE_VERSION_2_0: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_VERSION = 32
WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = Int32
WCN_VALUE_SS_RESERVED00: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 0
WCN_VALUE_SS_NOT_CONFIGURED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 1
WCN_VALUE_SS_CONFIGURED: win32more.Windows.Win32.NetworkManagement.WindowsConnectNow.WCN_VALUE_TYPE_WI_FI_PROTECTED_SETUP_STATE = 2
class WCN_VENDOR_EXTENSION_SPEC(Structure):
    VendorId: UInt32
    SubType: UInt32
    Index: UInt32
    Flags: UInt32


make_ready(__name__)
