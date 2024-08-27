from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Nfc
import win32more.Windows.Win32.Foundation
GUID_DEVINTERFACE_NFCDTA: Guid = Guid('{7fd3f30b-5e49-4be1-b3aa-af06260d236a}')
IOCTL_NFCDTA_CONFIG_RF_DISCOVERY: UInt32 = 2233344
IOCTL_NFCDTA_REMOTE_DEV_GET_NEXT: UInt32 = 2233348
IOCTL_NFCDTA_REMOTE_DEV_CONNECT: UInt32 = 2233352
IOCTL_NFCDTA_REMOTE_DEV_DISCONNECT: UInt32 = 2233356
IOCTL_NFCDTA_REMOTE_DEV_TRANSCEIVE: UInt32 = 2233360
IOCTL_NFCDTA_REMOTE_DEV_RECV: UInt32 = 2233364
IOCTL_NFCDTA_REMOTE_DEV_SEND: UInt32 = 2233368
IOCTL_NFCDTA_REMOTE_DEV_CHECK_PRESENCE: UInt32 = 2233372
IOCTL_NFCDTA_CONFIG_P2P_PARAM: UInt32 = 2233376
IOCTL_NFCDTA_SET_RF_CONFIG: UInt32 = 2233380
IOCTL_NFCDTA_REMOTE_DEV_NDEF_WRITE: UInt32 = 2233408
IOCTL_NFCDTA_REMOTE_DEV_NDEF_READ: UInt32 = 2233412
IOCTL_NFCDTA_REMOTE_DEV_NDEF_CONVERT_READ_ONLY: UInt32 = 2233416
IOCTL_NFCDTA_REMOTE_DEV_NDEF_CHECK: UInt32 = 2233420
IOCTL_NFCDTA_LLCP_CONFIG: UInt32 = 2233472
IOCTL_NFCDTA_LLCP_ACTIVATE: UInt32 = 2233476
IOCTL_NFCDTA_LLCP_DEACTIVATE: UInt32 = 2233480
IOCTL_NFCDTA_LLCP_DISCOVER_SERVICES: UInt32 = 2233484
IOCTL_NFCDTA_LLCP_LINK_STATUS_CHECK: UInt32 = 2233488
IOCTL_NFCDTA_LLCP_GET_NEXT_LINK_STATUS: UInt32 = 2233492
IOCTL_NFCDTA_LLCP_SOCKET_CREATE: UInt32 = 2233496
IOCTL_NFCDTA_LLCP_SOCKET_CLOSE: UInt32 = 2233500
IOCTL_NFCDTA_LLCP_SOCKET_BIND: UInt32 = 2233504
IOCTL_NFCDTA_LLCP_SOCKET_LISTEN: UInt32 = 2233508
IOCTL_NFCDTA_LLCP_SOCKET_ACCEPT: UInt32 = 2233512
IOCTL_NFCDTA_LLCP_SOCKET_CONNECT: UInt32 = 2233516
IOCTL_NFCDTA_LLCP_SOCKET_DISCONNECT: UInt32 = 2233520
IOCTL_NFCDTA_LLCP_SOCKET_RECV: UInt32 = 2233524
IOCTL_NFCDTA_LLCP_SOCKET_RECV_FROM: UInt32 = 2233528
IOCTL_NFCDTA_LLCP_SOCKET_SEND: UInt32 = 2233532
IOCTL_NFCDTA_LLCP_SOCKET_SNED_TO: UInt32 = 2233536
IOCTL_NFCDTA_LLCP_SOCKET_GET_NEXT_ERROR: UInt32 = 2233540
IOCTL_NFCDTA_SNEP_INIT_SERVER: UInt32 = 2233600
IOCTL_NFCDTA_SNEP_DEINIT_SERVER: UInt32 = 2233604
IOCTL_NFCDTA_SNEP_SERVER_GET_NEXT_CONNECTION: UInt32 = 2233608
IOCTL_NFCDTA_SNEP_SERVER_ACCEPT: UInt32 = 2233612
IOCTL_NFCDTA_SNEP_SERVER_GET_NEXT_REQUEST: UInt32 = 2233616
IOCTL_NFCDTA_SNEP_SERVER_SEND_RESPONSE: UInt32 = 2233620
IOCTL_NFCDTA_SNEP_INIT_CLIENT: UInt32 = 2233664
IOCTL_NFCDTA_SNEP_DEINIT_CLIENT: UInt32 = 2233668
IOCTL_NFCDTA_SNEP_CLIENT_PUT: UInt32 = 2233672
IOCTL_NFCDTA_SNEP_CLIENT_GET: UInt32 = 2233676
IOCTL_NFCDTA_SE_ENUMERATE: UInt32 = 2233728
IOCTL_NFCDTA_SE_SET_EMULATION_MODE: UInt32 = 2233732
IOCTL_NFCDTA_SE_SET_ROUTING_TABLE: UInt32 = 2233736
IOCTL_NFCDTA_SE_GET_NEXT_EVENT: UInt32 = 2233740
MAX_ATR_LENGTH: UInt32 = 48
MAX_UID_SIZE: UInt32 = 16
MAX_LLCP_SERVICE_NAME_SIZE: UInt32 = 256
MAX_SNEP_SERVER_NAME_SIZE: UInt32 = 256
GUID_NFC_RADIO_MEDIA_DEVICE_INTERFACE: Guid = Guid('{4d51e930-750d-4a36-a9f7-91dc540fcd30}')
GUID_NFCSE_RADIO_MEDIA_DEVICE_INTERFACE: Guid = Guid('{ef8ba08f-148d-4116-83ef-a2679dfc3fa5}')
NFCRMDDI_IOCTL_BASE: UInt32 = 80
IOCTL_NFCRM_SET_RADIO_STATE: UInt32 = 5308804
IOCTL_NFCRM_QUERY_RADIO_STATE: UInt32 = 5308808
IOCTL_NFCSERM_SET_RADIO_STATE: UInt32 = 5308812
IOCTL_NFCSERM_QUERY_RADIO_STATE: UInt32 = 5308816
GUID_DEVINTERFACE_NFCSE: Guid = Guid('{8dc7c854-f5e5-4bed-815d-0c85ad047725}')
IOCTL_NFCSE_ENUM_ENDPOINTS: UInt32 = 2230272
IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT: UInt32 = 2230276
IOCTL_NFCSE_GET_NEXT_EVENT: UInt32 = 2230280
IOCTL_NFCSE_SET_CARD_EMULATION_MODE: UInt32 = 2230284
IOCTL_NFCSE_GET_NFCC_CAPABILITIES: UInt32 = 2230288
IOCTL_NFCSE_GET_ROUTING_TABLE: UInt32 = 2230292
IOCTL_NFCSE_SET_ROUTING_TABLE: UInt32 = 2230296
IOCTL_NFCSE_HCE_REMOTE_RECV: UInt32 = 2230592
IOCTL_NFCSE_HCE_REMOTE_SEND: UInt32 = 2230596
IOCTL_NFCSE_SET_POWER_MODE: UInt32 = 2230600
EVT_TRANSACTION_TAG_AID: UInt32 = 129
EVT_TRANSACTION_TAG_PARAMETERS: UInt32 = 130
EVT_TRANSACTION_PARAMETER_MAX_LEN: UInt32 = 255
ISO_7816_MINIMUM_AID_LENGTH: UInt32 = 5
ISO_7816_MAXIMUM_AID_LENGTH: UInt32 = 16
class NFCRM_RADIO_STATE(Structure):
    MediaRadioOn: win32more.Windows.Win32.Foundation.BOOLEAN
class NFCRM_SET_RADIO_STATE(Structure):
    SystemStateUpdate: win32more.Windows.Win32.Foundation.BOOLEAN
    MediaRadioOn: win32more.Windows.Win32.Foundation.BOOLEAN
class NFC_DATA_BUFFER(Structure):
    cbBuffer: UInt16
    pbBuffer: Byte * 1
NFC_DEVICE_TYPE = Int32
NfcType1Tag: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 0
NfcType2Tag: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 1
NfcType3Tag: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 2
NfcType4Tag: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 3
NfcIP1Target: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 4
NfcIP1Initiator: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 5
NfcReader: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE = 6
class NFC_LLCP_CONFIG(Structure):
    uMIU: UInt16
    uWKS: UInt16
    bLTO: Byte
    bOptions: Byte
    fAutoActivate: win32more.Windows.Win32.Foundation.BOOLEAN
NFC_LLCP_LINK_STATUS = Int32
LinkActivated: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_LINK_STATUS = 0
LinkDeactivated: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_LINK_STATUS = 1
class NFC_LLCP_SERVICE_DISCOVER_REQUEST(Structure):
    hRemoteDev: IntPtr
    NumberOfEntries: UInt32
    ServiceNameEntries: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SERVICE_NAME_ENTRY * 1
class NFC_LLCP_SERVICE_DISCOVER_SAP(Structure):
    NumberOfEntries: UInt32
    SAPEntries: Byte * 1
class NFC_LLCP_SERVICE_NAME_ENTRY(Structure):
    cbServiceName: UInt32
    pbServiceName: Byte * 1
class NFC_LLCP_SOCKET_ACCEPT_INFO(Structure):
    hSocket: IntPtr
    sSocketOption: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_OPTION
class NFC_LLCP_SOCKET_CL_PAYLOAD(Structure):
    hSocket: IntPtr
    bSAP: Byte
    sPayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_LLCP_SOCKET_CONNECT_INFO(Structure):
    hRemoteDev: IntPtr
    hSocket: IntPtr
    eConnectType: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_CONNECT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        bSAP: Byte
        sServiceName: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SERVICE_NAME_ENTRY
NFC_LLCP_SOCKET_CONNECT_TYPE = Int32
NfcConnectBySap: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_CONNECT_TYPE = 0
NfcConnectByUri: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_CONNECT_TYPE = 1
NFC_LLCP_SOCKET_ERROR = Int32
NfcLlcpErrorDisconnected: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_ERROR = 0
NfcLlcpErrorFrameRejected: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_ERROR = 1
NfcLlcpErrorBusyCondition: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_ERROR = 2
NfcLlcpErrorNotBusyCondition: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_ERROR = 3
class NFC_LLCP_SOCKET_ERROR_INFO(Structure):
    hSocket: IntPtr
    eSocketError: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_ERROR
class NFC_LLCP_SOCKET_INFO(Structure):
    eSocketType: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_TYPE
    sSocketOption: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_OPTION
class NFC_LLCP_SOCKET_OPTION(Structure):
    uMIUX: UInt16
    bRW: Byte
class NFC_LLCP_SOCKET_PAYLOAD(Structure):
    hSocket: IntPtr
    bSAP: Byte
    sPayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_LLCP_SOCKET_SERVICE_INFO(Structure):
    hSocket: IntPtr
    bSAP: Byte
    sServiceName: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SERVICE_NAME_ENTRY
NFC_LLCP_SOCKET_TYPE = Int32
ConnectionOriented: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_TYPE = 0
Connectionless: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_TYPE = 1
class NFC_NDEF_INFO(Structure):
    fIsNdefFormatted: win32more.Windows.Win32.Foundation.BOOLEAN
    fIsReadOnly: win32more.Windows.Win32.Foundation.BOOLEAN
    dwActualMessageLength: UInt32
    dwMaxMessageLength: UInt32
NFC_P2P_MODE = Int32
NfcDepDefault: win32more.Windows.Win32.Devices.Nfc.NFC_P2P_MODE = 0
NfcDepPoll: win32more.Windows.Win32.Devices.Nfc.NFC_P2P_MODE = 1
NfcDepListen: win32more.Windows.Win32.Devices.Nfc.NFC_P2P_MODE = 2
class NFC_P2P_PARAM_CONFIG(Structure):
    eP2pMode: win32more.Windows.Win32.Devices.Nfc.NFC_P2P_MODE
    cbGeneralBytes: Byte
    pbGeneralBytes: Byte * 48
NFC_RELEASE_TYPE = Int32
IdleMode: win32more.Windows.Win32.Devices.Nfc.NFC_RELEASE_TYPE = 0
SleepMode: win32more.Windows.Win32.Devices.Nfc.NFC_RELEASE_TYPE = 1
Discovery: win32more.Windows.Win32.Devices.Nfc.NFC_RELEASE_TYPE = 2
class NFC_REMOTE_DEVICE_DISCONNET(Structure):
    hRemoteDev: IntPtr
    eReleaseType: win32more.Windows.Win32.Devices.Nfc.NFC_RELEASE_TYPE
class NFC_REMOTE_DEV_INFO(Structure):
    hRemoteDev: IntPtr
    eType: win32more.Windows.Win32.Devices.Nfc.NFC_DEVICE_TYPE
    eRFTech: Byte
    eProtocol: Byte
    cbUid: Byte
    pbUid: Byte * 16
class NFC_REMOTE_DEV_RECV_INFO(Structure):
    hRemoteDev: IntPtr
    sRecvBuffer: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_REMOTE_DEV_SEND_INFO(Structure):
    hRemoteDev: IntPtr
    usTimeOut: UInt16
    sSendBuffer: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_RF_DISCOVERY_CONFIG(Structure):
    usTotalDuration: UInt16
    ulPollConfig: UInt32
    fDisableCardEmulation: win32more.Windows.Win32.Foundation.BOOLEAN
    ucNfcIPMode: Byte
    fNfcIPTgtModeDisable: win32more.Windows.Win32.Foundation.BOOLEAN
    ucNfcIPTgtMode: Byte
    ucNfcCEMode: Byte
    ucBailoutConfig: Byte
    ucSystemCode: Byte * 2
    ucRequestCode: Byte
    ucTimeSlotNumber: Byte
    eRfDiscoveryMode: win32more.Windows.Win32.Devices.Nfc.NFC_RF_DISCOVERY_MODE
NFC_RF_DISCOVERY_MODE = Int32
RfDiscoveryConfig: win32more.Windows.Win32.Devices.Nfc.NFC_RF_DISCOVERY_MODE = 0
RfDiscoveryStart: win32more.Windows.Win32.Devices.Nfc.NFC_RF_DISCOVERY_MODE = 1
RFDiscoveryResume: win32more.Windows.Win32.Devices.Nfc.NFC_RF_DISCOVERY_MODE = 2
class NFC_SE_AID_ROUTING_INFO(Structure):
    hSecureElement: IntPtr
    bPowerState: Byte
    cbAid: UInt32
    pbAid: Byte * 16
NFC_SE_EMULATION_MODE = Int32
EmulationDisabled: win32more.Windows.Win32.Devices.Nfc.NFC_SE_EMULATION_MODE = 0
EmulationEnabled: win32more.Windows.Win32.Devices.Nfc.NFC_SE_EMULATION_MODE = 1
class NFC_SE_EMULATION_MODE_INFO(Structure):
    hSecureElement: IntPtr
    eMode: win32more.Windows.Win32.Devices.Nfc.NFC_SE_EMULATION_MODE
class NFC_SE_EVENT_INFO(Structure):
    hSecureElement: IntPtr
    eEventType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE
    cbEventData: UInt32
    pbEventData: Byte * 1
class NFC_SE_INFO(Structure):
    hSecureElement: IntPtr
    eSecureElementType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TYPE
class NFC_SE_LIST(Structure):
    NumberOfEndpoints: UInt32
    EndpointList: win32more.Windows.Win32.Devices.Nfc.NFC_SE_INFO * 1
class NFC_SE_PROTO_ROUTING_INFO(Structure):
    hSecureElement: IntPtr
    bPowerState: Byte
    eRfProtocolType: Byte
class NFC_SE_ROUTING_TABLE(Structure):
    NumberOfEntries: UInt32
    TableEntries: win32more.Windows.Win32.Devices.Nfc.NFC_SE_ROUTING_TABLE_ENTRY * 1
class NFC_SE_ROUTING_TABLE_ENTRY(Structure):
    eRoutingType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        TechRoutingInfo: win32more.Windows.Win32.Devices.Nfc.NFC_SE_TECH_ROUTING_INFO
        ProtoRoutingInfo: win32more.Windows.Win32.Devices.Nfc.NFC_SE_PROTO_ROUTING_INFO
        AidRoutingInfo: win32more.Windows.Win32.Devices.Nfc.NFC_SE_AID_ROUTING_INFO
class NFC_SE_TECH_ROUTING_INFO(Structure):
    hSecureElement: IntPtr
    bPowerState: Byte
    eRfTechType: Byte
class NFC_SNEP_CLIENT_GET_INFO(Structure):
    hSnepClient: IntPtr
    sGetPayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_SNEP_CLIENT_INFO(Structure):
    hRemoteDev: IntPtr
    eServerType: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_SERVER_TYPE
    sSocketOption: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_OPTION
    sService: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SERVICE_NAME_ENTRY
class NFC_SNEP_CLIENT_PUT_INFO(Structure):
    hSnepClient: IntPtr
    sPutPayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
NFC_SNEP_REQUEST_TYPE = Int32
SnepRequestGet: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_REQUEST_TYPE = 0
SnepRequestPut: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_REQUEST_TYPE = 1
class NFC_SNEP_SERVER_ACCEPT_INFO(Structure):
    hSnepServer: IntPtr
    hConnection: IntPtr
    sSocketOption: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_OPTION
class NFC_SNEP_SERVER_INFO(Structure):
    eServerType: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_SERVER_TYPE
    sSocketOption: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SOCKET_OPTION
    usInboxSize: UInt16
    bSAP: Byte
    sService: win32more.Windows.Win32.Devices.Nfc.NFC_LLCP_SERVICE_NAME_ENTRY
class NFC_SNEP_SERVER_REQUEST(Structure):
    hSnepServer: IntPtr
    hConnection: IntPtr
    eRequestType: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_REQUEST_TYPE
    sRequestPayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
class NFC_SNEP_SERVER_RESPONSE_INFO(Structure):
    hSnepServer: IntPtr
    hConnection: IntPtr
    dwResponseStatus: UInt32
    sResponsePayload: win32more.Windows.Win32.Devices.Nfc.NFC_DATA_BUFFER
NFC_SNEP_SERVER_TYPE = Int32
DefaultSnepServer: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_SERVER_TYPE = 0
ExtendedSnepServer: win32more.Windows.Win32.Devices.Nfc.NFC_SNEP_SERVER_TYPE = 1
class SECURE_ELEMENT_AID_ROUTING_INFO(Structure):
    guidSecureElementId: Guid
    cbAid: UInt32
    pbAid: Byte * 16
SECURE_ELEMENT_CARD_EMULATION_MODE = Int32
EmulationOff: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_CARD_EMULATION_MODE = 0
EmulationOnPowerIndependent: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_CARD_EMULATION_MODE = 1
EmulationOnPowerDependent: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_CARD_EMULATION_MODE = 2
EmulationStealthListen: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_CARD_EMULATION_MODE = 3
class SECURE_ELEMENT_ENDPOINT_INFO(Structure):
    guidSecureElementId: Guid
    eSecureElementType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TYPE
class SECURE_ELEMENT_ENDPOINT_LIST(Structure):
    NumberOfEndpoints: UInt32
    EndpointList: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ENDPOINT_INFO * 1
class SECURE_ELEMENT_EVENT_INFO(Structure):
    guidSecureElementId: Guid
    eEventType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE
    cbEventData: UInt32
    pbEventData: Byte * 1
class SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO(Structure):
    guidSecureElementId: Guid
    eEventType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE
SECURE_ELEMENT_EVENT_TYPE = Int32
ExternalReaderArrival: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 0
ExternalReaderDeparture: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 1
ApplicationSelected: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 2
Transaction: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 3
HceActivated: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 4
HceDeactivated: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 5
ExternalFieldEnter: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 6
ExternalFieldExit: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_EVENT_TYPE = 7
class SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD(Structure):
    bConnectionId: UInt16
    eRfTechType: Byte
    eRfProtocolType: Byte
class SECURE_ELEMENT_HCE_DATA_PACKET(Structure):
    bConnectionId: UInt16
    cbPayload: UInt16
    pbPayload: Byte * 1
class SECURE_ELEMENT_NFCC_CAPABILITIES(Structure):
    cbMaxRoutingTableSize: UInt16
    IsAidRoutingSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    IsProtocolRoutingSupported: win32more.Windows.Win32.Foundation.BOOLEAN
    IsTechRoutingSupported: win32more.Windows.Win32.Foundation.BOOLEAN
SECURE_ELEMENT_POWER_MODE = Int32
SEPowerMode_ForceOn: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_POWER_MODE = 0
SEPowerMode_AllowOff: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_POWER_MODE = 1
class SECURE_ELEMENT_PROTO_ROUTING_INFO(Structure):
    guidSecureElementId: Guid
    eRfProtocolType: Byte
class SECURE_ELEMENT_ROUTING_TABLE(Structure):
    NumberOfEntries: UInt32
    TableEntries: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TABLE_ENTRY * 1
class SECURE_ELEMENT_ROUTING_TABLE_ENTRY(Structure):
    eRoutingType: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        TechRoutingInfo: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TECH_ROUTING_INFO
        ProtoRoutingInfo: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_PROTO_ROUTING_INFO
        AidRoutingInfo: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_AID_ROUTING_INFO
SECURE_ELEMENT_ROUTING_TYPE = Int32
RoutingTypeTech: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TYPE = 0
RoutingTypeProtocol: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TYPE = 1
RoutingTypeAid: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_ROUTING_TYPE = 2
class SECURE_ELEMENT_SET_CARD_EMULATION_MODE_INFO(Structure):
    guidSecureElementId: Guid
    eMode: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_CARD_EMULATION_MODE
class SECURE_ELEMENT_SET_POWER_MODE_INFO(Structure):
    guidSecureElementId: Guid
    powerMode: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_POWER_MODE
class SECURE_ELEMENT_TECH_ROUTING_INFO(Structure):
    guidSecureElementId: Guid
    eRfTechType: Byte
SECURE_ELEMENT_TYPE = Int32
Integrated: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TYPE = 0
External: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TYPE = 1
DeviceHost: win32more.Windows.Win32.Devices.Nfc.SECURE_ELEMENT_TYPE = 2


make_ready(__name__)
