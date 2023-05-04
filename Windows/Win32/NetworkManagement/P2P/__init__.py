from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.P2P
import Windows.Win32.Networking.WinSock
import Windows.Win32.Security.Cryptography
import Windows.Win32.System.Com
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
NS_PNRPNAME: UInt32 = 38
NS_PNRPCLOUD: UInt32 = 39
PNRPINFO_HINT: UInt32 = 1
NS_PROVIDER_PNRPNAME: Guid = Guid('{03fe89cd-766d-4976-b9c1-bb9bc42c7b4d}')
NS_PROVIDER_PNRPCLOUD: Guid = Guid('{03fe89ce-766d-4976-b9c1-bb9bc42c7b4d}')
SVCID_PNRPCLOUD: Guid = Guid('{c2239ce6-00c0-4fbf-bad6-18139385a49a}')
SVCID_PNRPNAME_V1: Guid = Guid('{c2239ce5-00c0-4fbf-bad6-18139385a49a}')
SVCID_PNRPNAME_V2: Guid = Guid('{c2239ce7-00c0-4fbf-bad6-18139385a49a}')
PNRP_MAX_ENDPOINT_ADDRESSES: UInt32 = 10
WSZ_SCOPE_GLOBAL: String = 'GLOBAL'
WSZ_SCOPE_SITELOCAL: String = 'SITELOCAL'
WSZ_SCOPE_LINKLOCAL: String = 'LINKLOCAL'
PNRP_MAX_EXTENDED_PAYLOAD_BYTES: UInt32 = 4096
PEER_PNRP_ALL_LINK_CLOUDS: String = 'PEER_PNRP_ALL_LINKS'
WSA_PNRP_ERROR_BASE: UInt32 = 11500
WSA_PNRP_CLOUD_NOT_FOUND: UInt32 = 11501
WSA_PNRP_CLOUD_DISABLED: UInt32 = 11502
WSA_PNRP_INVALID_IDENTITY: UInt32 = 11503
WSA_PNRP_TOO_MUCH_LOAD: UInt32 = 11504
WSA_PNRP_CLOUD_IS_SEARCH_ONLY: UInt32 = 11505
WSA_PNRP_CLIENT_INVALID_COMPARTMENT_ID: UInt32 = 11506
WSA_PNRP_DUPLICATE_PEER_NAME: UInt32 = 11508
WSA_PNRP_CLOUD_IS_DEAD: UInt32 = 11509
PEER_E_CLOUD_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147013395
PEER_E_CLOUD_DISABLED: Windows.Win32.Foundation.HRESULT = -2147013394
PEER_E_INVALID_IDENTITY: Windows.Win32.Foundation.HRESULT = -2147013393
PEER_E_TOO_MUCH_LOAD: Windows.Win32.Foundation.HRESULT = -2147013392
PEER_E_CLOUD_IS_SEARCH_ONLY: Windows.Win32.Foundation.HRESULT = -2147013391
PEER_E_CLIENT_INVALID_COMPARTMENT_ID: Windows.Win32.Foundation.HRESULT = -2147013390
PEER_E_DUPLICATE_PEER_NAME: Windows.Win32.Foundation.HRESULT = -2147013388
PEER_E_CLOUD_IS_DEAD: Windows.Win32.Foundation.HRESULT = -2147013387
PEER_E_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147023728
PEER_E_DISK_FULL: Windows.Win32.Foundation.HRESULT = -2147024784
PEER_E_ALREADY_EXISTS: Windows.Win32.Foundation.HRESULT = -2147024713
PEER_GROUP_ROLE_ADMIN: Guid = Guid('{04387127-aa56-450a-8ce5-4f565c6790f4}')
PEER_GROUP_ROLE_MEMBER: Guid = Guid('{f12dc4c7-0857-4ca0-93fc-b1bb19a3d8c2}')
PEER_GROUP_ROLE_INVITING_MEMBER: Guid = Guid('{4370fd89-dc18-4cfb-8dbf-9853a8a9f905}')
PEER_COLLAB_OBJECTID_USER_PICTURE: Guid = Guid('{dd15f41f-fc4e-4922-b035-4c06a754d01d}')
FACILITY_DRT: UInt32 = 98
DRT_E_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2141057023
DRT_E_INVALID_KEY_SIZE: Windows.Win32.Foundation.HRESULT = -2141057022
DRT_E_INVALID_CERT_CHAIN: Windows.Win32.Foundation.HRESULT = -2141057020
DRT_E_INVALID_MESSAGE: Windows.Win32.Foundation.HRESULT = -2141057019
DRT_E_NO_MORE: Windows.Win32.Foundation.HRESULT = -2141057018
DRT_E_INVALID_MAX_ADDRESSES: Windows.Win32.Foundation.HRESULT = -2141057017
DRT_E_SEARCH_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2141057016
DRT_E_INVALID_KEY: Windows.Win32.Foundation.HRESULT = -2141057015
DRT_S_RETRY: Windows.Win32.Foundation.HRESULT = 6426640
DRT_E_INVALID_MAX_ENDPOINTS: Windows.Win32.Foundation.HRESULT = -2141057007
DRT_E_INVALID_SEARCH_RANGE: Windows.Win32.Foundation.HRESULT = -2141057006
DRT_E_INVALID_PORT: Windows.Win32.Foundation.HRESULT = -2141052928
DRT_E_INVALID_TRANSPORT_PROVIDER: Windows.Win32.Foundation.HRESULT = -2141052927
DRT_E_INVALID_SECURITY_PROVIDER: Windows.Win32.Foundation.HRESULT = -2141052926
DRT_E_STILL_IN_USE: Windows.Win32.Foundation.HRESULT = -2141052925
DRT_E_INVALID_BOOTSTRAP_PROVIDER: Windows.Win32.Foundation.HRESULT = -2141052924
DRT_E_INVALID_ADDRESS: Windows.Win32.Foundation.HRESULT = -2141052923
DRT_E_INVALID_SCOPE: Windows.Win32.Foundation.HRESULT = -2141052922
DRT_E_TRANSPORT_SHUTTING_DOWN: Windows.Win32.Foundation.HRESULT = -2141052921
DRT_E_NO_ADDRESSES_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2141052920
DRT_E_DUPLICATE_KEY: Windows.Win32.Foundation.HRESULT = -2141052919
DRT_E_TRANSPORTPROVIDER_IN_USE: Windows.Win32.Foundation.HRESULT = -2141052918
DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED: Windows.Win32.Foundation.HRESULT = -2141052917
DRT_E_SECURITYPROVIDER_IN_USE: Windows.Win32.Foundation.HRESULT = -2141052916
DRT_E_SECURITYPROVIDER_NOT_ATTACHED: Windows.Win32.Foundation.HRESULT = -2141052915
DRT_E_BOOTSTRAPPROVIDER_IN_USE: Windows.Win32.Foundation.HRESULT = -2141052914
DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED: Windows.Win32.Foundation.HRESULT = -2141052913
DRT_E_TRANSPORT_ALREADY_BOUND: Windows.Win32.Foundation.HRESULT = -2141052671
DRT_E_TRANSPORT_NOT_BOUND: Windows.Win32.Foundation.HRESULT = -2141052670
DRT_E_TRANSPORT_UNEXPECTED: Windows.Win32.Foundation.HRESULT = -2141052669
DRT_E_TRANSPORT_INVALID_ARGUMENT: Windows.Win32.Foundation.HRESULT = -2141052668
DRT_E_TRANSPORT_NO_DEST_ADDRESSES: Windows.Win32.Foundation.HRESULT = -2141052667
DRT_E_TRANSPORT_EXECUTING_CALLBACK: Windows.Win32.Foundation.HRESULT = -2141052666
DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE: Windows.Win32.Foundation.HRESULT = -2141052665
DRT_E_INVALID_SETTINGS: Windows.Win32.Foundation.HRESULT = -2141052664
DRT_E_INVALID_SEARCH_INFO: Windows.Win32.Foundation.HRESULT = -2141052663
DRT_E_FAULTED: Windows.Win32.Foundation.HRESULT = -2141052662
DRT_E_TRANSPORT_STILL_BOUND: Windows.Win32.Foundation.HRESULT = -2141052661
DRT_E_INSUFFICIENT_BUFFER: Windows.Win32.Foundation.HRESULT = -2141052660
DRT_E_INVALID_INSTANCE_PREFIX: Windows.Win32.Foundation.HRESULT = -2141052659
DRT_E_INVALID_SECURITY_MODE: Windows.Win32.Foundation.HRESULT = -2141052658
DRT_E_CAPABILITY_MISMATCH: Windows.Win32.Foundation.HRESULT = -2141052657
DRT_PAYLOAD_REVOKED: UInt32 = 1
DRT_MIN_ROUTING_ADDRESSES: UInt32 = 1
DRT_MAX_ROUTING_ADDRESSES: UInt32 = 20
DRT_MAX_PAYLOAD_SIZE: UInt32 = 5120
DRT_MAX_INSTANCE_PREFIX_LEN: UInt32 = 128
DRT_LINK_LOCAL_ISATAP_SCOPEID: UInt32 = 4294967295
PEERDIST_PUBLICATION_OPTIONS_VERSION_1: Int32 = 1
PEERDIST_PUBLICATION_OPTIONS_VERSION: Int32 = 2
PEERDIST_PUBLICATION_OPTIONS_VERSION_2: Int32 = 2
PEERDIST_READ_TIMEOUT_LOCAL_CACHE_ONLY: UInt32 = 0
PEERDIST_READ_TIMEOUT_DEFAULT: UInt32 = 4294967294
@winfunctype('P2PGRAPH.dll')
def PeerGraphStartup(wVersionRequested: UInt16, pVersionData: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_VERSION_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphShutdown() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphFreeData(pvData: c_void_p) -> Void: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetItemCount(hPeerEnum: c_void_p, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNextItem(hPeerEnum: c_void_p, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(c_void_p))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEndEnumeration(hPeerEnum: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCreate(pGraphProperties: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head), pwzDatabaseName: Windows.Win32.Foundation.PWSTR, pSecurityInterface: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head), phGraph: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpen(pwzGraphId: Windows.Win32.Foundation.PWSTR, pwzPeerId: Windows.Win32.Foundation.PWSTR, pwzDatabaseName: Windows.Win32.Foundation.PWSTR, pSecurityInterface: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head), cRecordTypeSyncPrecedence: UInt32, pRecordTypeSyncPrecedence: POINTER(Guid), phGraph: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphListen(hGraph: c_void_p, dwScope: UInt32, dwScopeId: UInt32, wPort: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphConnect(hGraph: c_void_p, pwzPeerId: Windows.Win32.Foundation.PWSTR, pAddress: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphClose(hGraph: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDelete(pwzGraphId: Windows.Win32.Foundation.PWSTR, pwzPeerId: Windows.Win32.Foundation.PWSTR, pwzDatabaseName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetStatus(hGraph: c_void_p, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetProperties(hGraph: c_void_p, ppGraphProperties: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetProperties(hGraph: c_void_p, pGraphProperties: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphRegisterEvent(hGraph: c_void_p, hEvent: Windows.Win32.Foundation.HANDLE, cEventRegistrations: UInt32, pEventRegistrations: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUnregisterEvent(hPeerEvent: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetRecord(hGraph: c_void_p, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphAddRecord(hGraph: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head), pRecordId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUpdateRecord(hGraph: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDeleteRecord(hGraph: c_void_p, pRecordId: POINTER(Guid), fLocal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumRecords(hGraph: c_void_p, pRecordType: POINTER(Guid), pwzPeerId: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSearchRecords(hGraph: c_void_p, pwzCriteria: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphExportDatabase(hGraph: c_void_p, pwzFilePath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphImportDatabase(hGraph: c_void_p, pwzFilePath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphValidateDeferredRecords(hGraph: c_void_p, cRecordIds: UInt32, pRecordIds: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpenDirectConnection(hGraph: c_void_p, pwzPeerId: Windows.Win32.Foundation.PWSTR, pAddress: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSendData(hGraph: c_void_p, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCloseDirectConnection(hGraph: c_void_p, ullConnectionId: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumConnections(hGraph: c_void_p, dwFlags: UInt32, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumNodes(hGraph: c_void_p, pwzPeerId: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetPresence(hGraph: c_void_p, fPresent: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNodeInfo(hGraph: c_void_p, ullNodeId: UInt64, ppNodeInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_NODE_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetNodeAttributes(hGraph: c_void_p, pwzAttributes: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphPeerTimeToUniversalTime(hGraph: c_void_p, pftPeerTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftUniversalTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUniversalTimeToPeerTime(hGraph: c_void_p, pftUniversalTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftPeerTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerFreeData(pvData: c_void_p) -> Void: ...
@winfunctype('P2P.dll')
def PeerGetItemCount(hPeerEnum: c_void_p, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGetNextItem(hPeerEnum: c_void_p, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(c_void_p))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEndEnumeration(hPeerEnum: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupStartup(wVersionRequested: UInt16, pVersionData: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_VERSION_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupShutdown() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreate(pProperties: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head), phGroup: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpen(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzGroupPeerName: Windows.Win32.Foundation.PWSTR, pwzCloud: Windows.Win32.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupJoin(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzInvitation: Windows.Win32.Foundation.PWSTR, pwzCloud: Windows.Win32.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPasswordJoin(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzInvitation: Windows.Win32.Foundation.PWSTR, pwzPassword: Windows.Win32.Foundation.PWSTR, pwzCloud: Windows.Win32.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnect(hGroup: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnectByAddress(hGroup: c_void_p, cAddresses: UInt32, pAddresses: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupClose(hGroup: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDelete(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzGroupPeerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreateInvitation(hGroup: c_void_p, pwzIdentityInfo: Windows.Win32.Foundation.PWSTR, pftExpiration: POINTER(Windows.Win32.Foundation.FILETIME_head), cRoles: UInt32, pRoles: POINTER(Guid), ppwzInvitation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreatePasswordInvitation(hGroup: c_void_p, ppwzInvitation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupParseInvitation(pwzInvitation: Windows.Win32.Foundation.PWSTR, ppInvitationInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetStatus(hGroup: c_void_p, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetProperties(hGroup: c_void_p, ppProperties: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSetProperties(hGroup: c_void_p, pProperties: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumMembers(hGroup: c_void_p, dwFlags: UInt32, pwzIdentity: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpenDirectConnection(hGroup: c_void_p, pwzIdentity: Windows.Win32.Foundation.PWSTR, pAddress: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCloseDirectConnection(hGroup: c_void_p, ullConnectionId: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumConnections(hGroup: c_void_p, dwFlags: UInt32, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSendData(hGroup: c_void_p, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupRegisterEvent(hGroup: c_void_p, hEvent: Windows.Win32.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUnregisterEvent(hPeerEvent: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetRecord(hGroup: c_void_p, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupAddRecord(hGroup: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head), pRecordId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUpdateRecord(hGroup: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDeleteRecord(hGroup: c_void_p, pRecordId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumRecords(hGroup: c_void_p, pRecordType: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSearchRecords(hGroup: c_void_p, pwzCriteria: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportDatabase(hGroup: c_void_p, pwzFilePath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportDatabase(hGroup: c_void_p, pwzFilePath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupIssueCredentials(hGroup: c_void_p, pwzSubjectIdentity: Windows.Win32.Foundation.PWSTR, pCredentialInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head), dwFlags: UInt32, ppwzInvitation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportConfig(hGroup: c_void_p, pwzPassword: Windows.Win32.Foundation.PWSTR, ppwzXML: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportConfig(pwzXML: Windows.Win32.Foundation.PWSTR, pwzPassword: Windows.Win32.Foundation.PWSTR, fOverwrite: Windows.Win32.Foundation.BOOL, ppwzIdentity: POINTER(Windows.Win32.Foundation.PWSTR), ppwzGroup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPeerTimeToUniversalTime(hGroup: c_void_p, pftPeerTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftUniversalTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUniversalTimeToPeerTime(hGroup: c_void_p, pftUniversalTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftPeerTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupResumePasswordAuthentication(hGroup: c_void_p, hPeerEventHandle: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityCreate(pwzClassifier: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, hCryptProv: UIntPtr, ppwzIdentity: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetFriendlyName(pwzIdentity: Windows.Win32.Foundation.PWSTR, ppwzFriendlyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentitySetFriendlyName(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetCryptKey(pwzIdentity: Windows.Win32.Foundation.PWSTR, phCryptProv: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityDelete(pwzIdentity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumIdentities(phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumGroups(pwzIdentity: Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCreatePeerName(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzClassifier: Windows.Win32.Foundation.PWSTR, ppwzPeerName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetXML(pwzIdentity: Windows.Win32.Foundation.PWSTR, ppwzIdentityXML: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityExport(pwzIdentity: Windows.Win32.Foundation.PWSTR, pwzPassword: Windows.Win32.Foundation.PWSTR, ppwzExportXML: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityImport(pwzImportXML: Windows.Win32.Foundation.PWSTR, pwzPassword: Windows.Win32.Foundation.PWSTR, ppwzIdentity: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetDefault(ppwzPeerName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabStartup(wVersionRequested: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabShutdown() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignin(hwndParent: Windows.Win32.Foundation.HWND, dwSigninOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignout(dwSigninOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetSigninOptions(pdwSigninOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteContact(pcContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head), pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_head), hEvent: Windows.Win32.Foundation.HANDLE, phInvitation: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetInvitationResponse(hInvitation: Windows.Win32.Foundation.HANDLE, ppInvitationResponse: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCancelInvitation(hInvitation: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCloseHandle(hInvitation: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteContact(pcContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head), pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_head), ppResponse: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteEndpoint(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_head), hEvent: Windows.Win32.Foundation.HANDLE, phInvitation: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteEndpoint(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_head), ppResponse: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetAppLaunchInfo(ppLaunchInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_APP_LAUNCH_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterApplication(pcApplication: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head), registrationType: Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterApplication(pApplicationId: POINTER(Guid), registrationType: Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetApplicationRegistrationInfo(pApplicationId: POINTER(Guid), registrationType: Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, ppApplication: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplicationRegistrationInfo(registrationType: Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetPresenceInfo(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), ppPresenceInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplications(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pApplicationId: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumObjects(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), pObjectId: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumEndpoints(pcContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head), phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRefreshEndpointData(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteEndpointData(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabQueryContactData(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head), ppwzContactData: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSubscribeEndpointData(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnsubscribeEndpointData(pcEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetPresenceInfo(pcPresenceInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEndpointName(ppwzEndpointName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetEndpointName(pwzEndpointName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetObject(pcObject: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_OBJECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteObject(pObjectId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterEvent(hEvent: Windows.Win32.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterEvent(hPeerEvent: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumPeopleNearMe(phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAddContact(pwzContactData: Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteContact(pwzPeerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetContact(pwzPeerName: Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUpdateContact(pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumContacts(phPeerEnum: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabExportContact(pwzPeerName: Windows.Win32.Foundation.PWSTR, ppwzContactData: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabParseContact(pwzContactData: Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerNameToPeerHostName(pwzPeerName: Windows.Win32.Foundation.PWSTR, ppwzHostName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerHostNameToPeerName(pwzHostName: Windows.Win32.Foundation.PWSTR, ppwzPeerName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartup(wVersionRequested: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpShutdown() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpRegister(pcwzPeerName: Windows.Win32.Foundation.PWSTR, pRegistrationInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head), phRegistration: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUpdateRegistration(hRegistration: c_void_p, pRegistrationInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUnregister(hRegistration: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpResolve(pcwzPeerName: Windows.Win32.Foundation.PWSTR, pcwzCloudName: Windows.Win32.Foundation.PWSTR, pcEndpoints: POINTER(UInt32), ppEndpoints: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartResolve(pcwzPeerName: Windows.Win32.Foundation.PWSTR, pcwzCloudName: Windows.Win32.Foundation.PWSTR, cMaxEndpoints: UInt32, hEvent: Windows.Win32.Foundation.HANDLE, phResolve: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetCloudInfo(pcNumClouds: POINTER(UInt32), ppCloudInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PNRP_CLOUD_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetEndpoint(hResolve: c_void_p, ppEndpoint: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpEndResolve(hResolve: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreatePnrpBootstrapResolver(fPublish: Windows.Win32.Foundation.BOOL, pwzPeerName: Windows.Win32.Foundation.PWSTR, pwzCloudName: Windows.Win32.Foundation.PWSTR, pwzPublishingIdentity: Windows.Win32.Foundation.PWSTR, ppResolver: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeletePnrpBootstrapResolver(pResolver: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateDnsBootstrapResolver(port: UInt16, pwszAddress: Windows.Win32.Foundation.PWSTR, ppModule: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDnsBootstrapResolver(pResolver: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)) -> Void: ...
@winfunctype('drttransport.dll')
def DrtCreateIpv6UdpTransport(scope: Windows.Win32.NetworkManagement.P2P.DRT_SCOPE, dwScopeId: UInt32, dwLocalityThreshold: UInt32, pwPort: POINTER(UInt16), phTransport: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drttransport.dll')
def DrtDeleteIpv6UdpTransport(hTransport: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKeySecurityProvider(pRootCert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), pLocalCert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), ppSecurityProvider: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKey(pLocalCert: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), pKey: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDerivedKeySecurityProvider(pSecurityProvider: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateNullSecurityProvider(ppSecurityProvider: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteNullSecurityProvider(pSecurityProvider: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)) -> Void: ...
@winfunctype('drt.dll')
def DrtOpen(pSettings: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SETTINGS_head), hEvent: Windows.Win32.Foundation.HANDLE, pvContext: c_void_p, phDrt: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtClose(hDrt: c_void_p) -> Void: ...
@winfunctype('drt.dll')
def DrtGetEventDataSize(hDrt: c_void_p, pulEventDataLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetEventData(hDrt: c_void_p, ulEventDataLen: UInt32, pEventData: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_EVENT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtRegisterKey(hDrt: c_void_p, pRegistration: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION_head), pvKeyContext: c_void_p, phKeyRegistration: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUpdateKey(hKeyRegistration: c_void_p, pAppData: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUnregisterKey(hKeyRegistration: c_void_p) -> Void: ...
@winfunctype('drt.dll')
def DrtStartSearch(hDrt: c_void_p, pKey: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_DATA_head), pInfo: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SEARCH_INFO_head), timeout: UInt32, hEvent: Windows.Win32.Foundation.HANDLE, pvContext: c_void_p, hSearchContext: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtContinueSearch(hSearchContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResultSize(hSearchContext: c_void_p, pulSearchResultSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResult(hSearchContext: c_void_p, ulSearchResultSize: UInt32, pSearchResult: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SEARCH_RESULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPathSize(hSearchContext: c_void_p, pulSearchPathSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPath(hSearchContext: c_void_p, ulSearchPathSize: UInt32, pSearchPath: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtEndSearch(hSearchContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceName(hDrt: c_void_p, ulcbInstanceNameSize: UInt32, pwzDrtInstanceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceNameSize(hDrt: c_void_p, pulcbInstanceNameSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PeerDist.dll')
def PeerDistStartup(dwVersionRequested: UInt32, phPeerDist: POINTER(IntPtr), pdwSupportedVersion: POINTER(UInt32)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistShutdown(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatus(hPeerDist: IntPtr, pPeerDistStatus: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotification(hPeerDist: IntPtr, hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), pPeerDistStatus: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistUnregisterForStatusChangeNotification(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishStream(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), cbContentLength: UInt64, pPublishOptions: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_PUBLICATION_OPTIONS_head), hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phStream: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishAddToStream(hPeerDist: IntPtr, hStream: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishCompleteStream(hPeerDist: IntPtr, hStream: IntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseStreamHandle(hPeerDist: IntPtr, hStream: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerUnpublish(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), ullContentOffset: UInt64, cbContentLength: UInt64, hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerRetrieveContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCancelAsyncOperation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientOpenContent(hPeerDist: IntPtr, pContentTag: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head), hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCloseContent(hPeerDist: IntPtr, hContentHandle: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCompleteContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddData(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientBlockRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientStreamRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientFlushContent(hPeerDist: IntPtr, pContentTag: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head), hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCancelAsyncOperation(hPeerDist: IntPtr, hContentHandle: IntPtr, pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatusEx(hPeerDist: IntPtr, pPeerDistStatus: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotificationEx(hPeerDist: IntPtr, hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), pPeerDistStatus: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetOverlappedResult(lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformationEx(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), ullContentOffset: UInt64, cbContentLength: UInt64, pRetrievalOptions: POINTER(Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_head), hCompletionPort: Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientGetInformationByHandle(hPeerDist: IntPtr, hContentHandle: IntPtr, PeerDistClientInfoClass: Windows.Win32.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS, dwBufferSize: UInt32, lpInformation: c_void_p) -> UInt32: ...
class DRT_ADDRESS(EasyCastStructure):
    socketAddress: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    flags: UInt32
    nearness: Int32
    latency: UInt32
DRT_ADDRESS_FLAGS = Int32
DRT_ADDRESS_FLAG_ACCEPTED: DRT_ADDRESS_FLAGS = 1
DRT_ADDRESS_FLAG_REJECTED: DRT_ADDRESS_FLAGS = 2
DRT_ADDRESS_FLAG_UNREACHABLE: DRT_ADDRESS_FLAGS = 4
DRT_ADDRESS_FLAG_LOOP: DRT_ADDRESS_FLAGS = 8
DRT_ADDRESS_FLAG_TOO_BUSY: DRT_ADDRESS_FLAGS = 16
DRT_ADDRESS_FLAG_BAD_VALIDATE_ID: DRT_ADDRESS_FLAGS = 32
DRT_ADDRESS_FLAG_SUSPECT_UNREGISTERED_ID: DRT_ADDRESS_FLAGS = 64
DRT_ADDRESS_FLAG_INQUIRE: DRT_ADDRESS_FLAGS = 128
class DRT_ADDRESS_LIST(EasyCastStructure):
    AddressCount: UInt32
    AddressList: Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS * 1
class DRT_BOOTSTRAP_PROVIDER(EasyCastStructure):
    pvContext: c_void_p
    Attach: IntPtr
    Detach: IntPtr
    InitResolve: IntPtr
    IssueResolve: IntPtr
    EndResolve: IntPtr
    Register: IntPtr
    Unregister: IntPtr
@winfunctype_pointer
def DRT_BOOTSTRAP_RESOLVE_CALLBACK(hr: Windows.Win32.Foundation.HRESULT, pvContext: c_void_p, pAddresses: POINTER(Windows.Win32.Networking.WinSock.SOCKET_ADDRESS_LIST_head), fFatalError: Windows.Win32.Foundation.BOOL) -> Void: ...
class DRT_DATA(EasyCastStructure):
    cb: UInt32
    pb: POINTER(Byte)
class DRT_EVENT_DATA(EasyCastStructure):
    type: Windows.Win32.NetworkManagement.P2P.DRT_EVENT_TYPE
    hr: Windows.Win32.Foundation.HRESULT
    pvContext: c_void_p
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        leafsetKeyChange: _leafsetKeyChange_e__Struct
        registrationStateChange: _registrationStateChange_e__Struct
        statusChange: _statusChange_e__Struct
        class _leafsetKeyChange_e__Struct(EasyCastStructure):
            change: Windows.Win32.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE
            localKey: Windows.Win32.NetworkManagement.P2P.DRT_DATA
            remoteKey: Windows.Win32.NetworkManagement.P2P.DRT_DATA
        class _registrationStateChange_e__Struct(EasyCastStructure):
            state: Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION_STATE
            localKey: Windows.Win32.NetworkManagement.P2P.DRT_DATA
        class _statusChange_e__Struct(EasyCastStructure):
            status: Windows.Win32.NetworkManagement.P2P.DRT_STATUS
            bootstrapAddresses: _bootstrapAddresses_e__Struct
            class _bootstrapAddresses_e__Struct(EasyCastStructure):
                cntAddress: UInt32
                pAddresses: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)
DRT_EVENT_TYPE = Int32
DRT_EVENT_STATUS_CHANGED: DRT_EVENT_TYPE = 0
DRT_EVENT_LEAFSET_KEY_CHANGED: DRT_EVENT_TYPE = 1
DRT_EVENT_REGISTRATION_STATE_CHANGED: DRT_EVENT_TYPE = 2
DRT_LEAFSET_KEY_CHANGE_TYPE = Int32
DRT_LEAFSET_KEY_ADDED: DRT_LEAFSET_KEY_CHANGE_TYPE = 0
DRT_LEAFSET_KEY_DELETED: DRT_LEAFSET_KEY_CHANGE_TYPE = 1
DRT_MATCH_TYPE = Int32
DRT_MATCH_EXACT: DRT_MATCH_TYPE = 0
DRT_MATCH_NEAR: DRT_MATCH_TYPE = 1
DRT_MATCH_INTERMEDIATE: DRT_MATCH_TYPE = 2
class DRT_REGISTRATION(EasyCastStructure):
    key: Windows.Win32.NetworkManagement.P2P.DRT_DATA
    appData: Windows.Win32.NetworkManagement.P2P.DRT_DATA
DRT_REGISTRATION_STATE = Int32
DRT_REGISTRATION_STATE_UNRESOLVEABLE: DRT_REGISTRATION_STATE = 1
DRT_SCOPE = Int32
DRT_GLOBAL_SCOPE: DRT_SCOPE = 1
DRT_SITE_LOCAL_SCOPE: DRT_SCOPE = 2
DRT_LINK_LOCAL_SCOPE: DRT_SCOPE = 3
class DRT_SEARCH_INFO(EasyCastStructure):
    dwSize: UInt32
    fIterative: Windows.Win32.Foundation.BOOL
    fAllowCurrentInstanceMatch: Windows.Win32.Foundation.BOOL
    fAnyMatchInRange: Windows.Win32.Foundation.BOOL
    cMaxEndpoints: UInt32
    pMaximumKey: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_DATA_head)
    pMinimumKey: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_DATA_head)
class DRT_SEARCH_RESULT(EasyCastStructure):
    dwSize: UInt32
    type: Windows.Win32.NetworkManagement.P2P.DRT_MATCH_TYPE
    pvContext: c_void_p
    registration: Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION
DRT_SECURITY_MODE = Int32
DRT_SECURE_RESOLVE: DRT_SECURITY_MODE = 0
DRT_SECURE_MEMBERSHIP: DRT_SECURITY_MODE = 1
DRT_SECURE_CONFIDENTIALPAYLOAD: DRT_SECURITY_MODE = 2
class DRT_SECURITY_PROVIDER(EasyCastStructure):
    pvContext: c_void_p
    Attach: IntPtr
    Detach: IntPtr
    RegisterKey: IntPtr
    UnregisterKey: IntPtr
    ValidateAndUnpackPayload: IntPtr
    SecureAndPackPayload: IntPtr
    FreeData: IntPtr
    EncryptData: IntPtr
    DecryptData: IntPtr
    GetSerializedCredential: IntPtr
    ValidateRemoteCredential: IntPtr
    SignData: IntPtr
    VerifyData: IntPtr
class DRT_SETTINGS(EasyCastStructure):
    dwSize: UInt32
    cbKey: UInt32
    bProtocolMajorVersion: Byte
    bProtocolMinorVersion: Byte
    ulMaxRoutingAddresses: UInt32
    pwzDrtInstancePrefix: Windows.Win32.Foundation.PWSTR
    hTransport: c_void_p
    pSecurityProvider: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)
    pBootstrapProvider: POINTER(Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)
    eSecurityMode: Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_MODE
DRT_STATUS = Int32
DRT_ACTIVE: DRT_STATUS = 0
DRT_ALONE: DRT_STATUS = 1
DRT_NO_NETWORK: DRT_STATUS = 10
DRT_FAULTED: DRT_STATUS = 20
class PEERDIST_CLIENT_BASIC_INFO(EasyCastStructure):
    fFlashCrowd: Windows.Win32.Foundation.BOOL
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = Int32
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_PeerDistClientBasicInfo: PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 0
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_MaximumPeerDistClientInfoByHandlesClass: PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 1
class PEERDIST_CONTENT_TAG(EasyCastStructure):
    Data: Byte * 16
class PEERDIST_PUBLICATION_OPTIONS(EasyCastStructure):
    dwVersion: UInt32
    dwFlags: UInt32
class PEERDIST_RETRIEVAL_OPTIONS(EasyCastStructure):
    cbSize: UInt32
    dwContentInfoMinVersion: UInt32
    dwContentInfoMaxVersion: UInt32
    dwReserved: UInt32
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = UInt32
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_1: PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 1
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_2: PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 2
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION: PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 2
PEERDIST_STATUS = Int32
PEERDIST_STATUS_DISABLED: PEERDIST_STATUS = 0
PEERDIST_STATUS_UNAVAILABLE: PEERDIST_STATUS = 1
PEERDIST_STATUS_AVAILABLE: PEERDIST_STATUS = 2
class PEERDIST_STATUS_INFO(EasyCastStructure):
    cbSize: UInt32
    status: Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS
    dwMinVer: Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
    dwMaxVer: Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
class PEER_ADDRESS(EasyCastStructure):
    dwSize: UInt32
    sin6: Windows.Win32.Networking.WinSock.SOCKADDR_IN6
class PEER_APPLICATION(EasyCastStructure):
    id: Guid
    data: Windows.Win32.NetworkManagement.P2P.PEER_DATA
    pwzDescription: Windows.Win32.Foundation.PWSTR
class PEER_APPLICATION_REGISTRATION_INFO(EasyCastStructure):
    application: Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION
    pwzApplicationToLaunch: Windows.Win32.Foundation.PWSTR
    pwzApplicationArguments: Windows.Win32.Foundation.PWSTR
    dwPublicationScope: UInt32
PEER_APPLICATION_REGISTRATION_TYPE = Int32
PEER_APPLICATION_CURRENT_USER: PEER_APPLICATION_REGISTRATION_TYPE = 0
PEER_APPLICATION_ALL_USERS: PEER_APPLICATION_REGISTRATION_TYPE = 1
class PEER_APP_LAUNCH_INFO(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
    pInvitation: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_head)
PEER_CHANGE_TYPE = Int32
PEER_CHANGE_ADDED: PEER_CHANGE_TYPE = 0
PEER_CHANGE_DELETED: PEER_CHANGE_TYPE = 1
PEER_CHANGE_UPDATED: PEER_CHANGE_TYPE = 2
class PEER_COLLAB_EVENT_DATA(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        watchListChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_WATCHLIST_CHANGED_DATA
        presenceChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_PRESENCE_CHANGED_DATA
        applicationChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_APPLICATION_CHANGED_DATA
        objectChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_OBJECT_CHANGED_DATA
        endpointChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_ENDPOINT_CHANGED_DATA
        peopleNearMeChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA
        requestStatusChangedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_REQUEST_STATUS_CHANGED_DATA
class PEER_COLLAB_EVENT_REGISTRATION(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
    pInstance: POINTER(Guid)
PEER_COLLAB_EVENT_TYPE = Int32
PEER_EVENT_WATCHLIST_CHANGED: PEER_COLLAB_EVENT_TYPE = 1
PEER_EVENT_ENDPOINT_CHANGED: PEER_COLLAB_EVENT_TYPE = 2
PEER_EVENT_ENDPOINT_PRESENCE_CHANGED: PEER_COLLAB_EVENT_TYPE = 3
PEER_EVENT_ENDPOINT_APPLICATION_CHANGED: PEER_COLLAB_EVENT_TYPE = 4
PEER_EVENT_ENDPOINT_OBJECT_CHANGED: PEER_COLLAB_EVENT_TYPE = 5
PEER_EVENT_MY_ENDPOINT_CHANGED: PEER_COLLAB_EVENT_TYPE = 6
PEER_EVENT_MY_PRESENCE_CHANGED: PEER_COLLAB_EVENT_TYPE = 7
PEER_EVENT_MY_APPLICATION_CHANGED: PEER_COLLAB_EVENT_TYPE = 8
PEER_EVENT_MY_OBJECT_CHANGED: PEER_COLLAB_EVENT_TYPE = 9
PEER_EVENT_PEOPLE_NEAR_ME_CHANGED: PEER_COLLAB_EVENT_TYPE = 10
PEER_EVENT_REQUEST_STATUS_CHANGED: PEER_COLLAB_EVENT_TYPE = 11
PEER_CONNECTION_FLAGS = Int32
PEER_CONNECTION_NEIGHBOR: PEER_CONNECTION_FLAGS = 1
PEER_CONNECTION_DIRECT: PEER_CONNECTION_FLAGS = 2
class PEER_CONNECTION_INFO(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    ullConnectionId: UInt64
    ullNodeId: UInt64
    pwzPeerId: Windows.Win32.Foundation.PWSTR
    address: Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS
PEER_CONNECTION_STATUS = Int32
PEER_CONNECTED: PEER_CONNECTION_STATUS = 1
PEER_DISCONNECTED: PEER_CONNECTION_STATUS = 2
PEER_CONNECTION_FAILED: PEER_CONNECTION_STATUS = 3
class PEER_CONTACT(EasyCastStructure):
    pwzPeerName: Windows.Win32.Foundation.PWSTR
    pwzNickName: Windows.Win32.Foundation.PWSTR
    pwzDisplayName: Windows.Win32.Foundation.PWSTR
    pwzEmailAddress: Windows.Win32.Foundation.PWSTR
    fWatch: Windows.Win32.Foundation.BOOL
    WatcherPermissions: Windows.Win32.NetworkManagement.P2P.PEER_WATCH_PERMISSION
    credentials: Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_CREDENTIAL_INFO(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzFriendlyName: Windows.Win32.Foundation.PWSTR
    pPublicKey: POINTER(Windows.Win32.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)
    pwzIssuerPeerName: Windows.Win32.Foundation.PWSTR
    pwzIssuerFriendlyName: Windows.Win32.Foundation.PWSTR
    ftValidityStart: Windows.Win32.Foundation.FILETIME
    ftValidityEnd: Windows.Win32.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
class PEER_DATA(EasyCastStructure):
    cbData: UInt32
    pbData: POINTER(Byte)
class PEER_ENDPOINT(EasyCastStructure):
    address: Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS
    pwzEndpointName: Windows.Win32.Foundation.PWSTR
class PEER_EVENT_APPLICATION_CHANGED_DATA(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pApplication: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_head)
class PEER_EVENT_CONNECTION_CHANGE_DATA(EasyCastStructure):
    dwSize: UInt32
    status: Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_STATUS
    ullConnectionId: UInt64
    ullNodeId: UInt64
    ullNextConnectionId: UInt64
    hrConnectionFailedReason: Windows.Win32.Foundation.HRESULT
class PEER_EVENT_ENDPOINT_CHANGED_DATA(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
class PEER_EVENT_INCOMING_DATA(EasyCastStructure):
    dwSize: UInt32
    ullConnectionId: UInt64
    type: Guid
    data: Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_EVENT_MEMBER_CHANGE_DATA(EasyCastStructure):
    dwSize: UInt32
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE
    pwzIdentity: Windows.Win32.Foundation.PWSTR
class PEER_EVENT_NODE_CHANGE_DATA(EasyCastStructure):
    dwSize: UInt32
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE
    ullNodeId: UInt64
    pwzPeerId: Windows.Win32.Foundation.PWSTR
class PEER_EVENT_OBJECT_CHANGED_DATA(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pObject: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_OBJECT_head)
class PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA(EasyCastStructure):
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPeopleNearMe: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PEOPLE_NEAR_ME_head)
class PEER_EVENT_PRESENCE_CHANGED_DATA(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPresenceInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)
class PEER_EVENT_RECORD_CHANGE_DATA(EasyCastStructure):
    dwSize: UInt32
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE
    recordId: Guid
    recordType: Guid
class PEER_EVENT_REQUEST_STATUS_CHANGED_DATA(EasyCastStructure):
    pEndpoint: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT_head)
    hrChange: Windows.Win32.Foundation.HRESULT
class PEER_EVENT_SYNCHRONIZED_DATA(EasyCastStructure):
    dwSize: UInt32
    recordType: Guid
class PEER_EVENT_WATCHLIST_CHANGED_DATA(EasyCastStructure):
    pContact: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CONTACT_head)
    changeType: Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
class PEER_GRAPH_EVENT_DATA(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        dwStatus: Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS
        incomingData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        nodeChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_NODE_CHANGE_DATA
        synchronizedData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_SYNCHRONIZED_DATA
class PEER_GRAPH_EVENT_REGISTRATION(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
    pType: POINTER(Guid)
PEER_GRAPH_EVENT_TYPE = Int32
PEER_GRAPH_EVENT_STATUS_CHANGED: PEER_GRAPH_EVENT_TYPE = 1
PEER_GRAPH_EVENT_PROPERTY_CHANGED: PEER_GRAPH_EVENT_TYPE = 2
PEER_GRAPH_EVENT_RECORD_CHANGED: PEER_GRAPH_EVENT_TYPE = 3
PEER_GRAPH_EVENT_DIRECT_CONNECTION: PEER_GRAPH_EVENT_TYPE = 4
PEER_GRAPH_EVENT_NEIGHBOR_CONNECTION: PEER_GRAPH_EVENT_TYPE = 5
PEER_GRAPH_EVENT_INCOMING_DATA: PEER_GRAPH_EVENT_TYPE = 6
PEER_GRAPH_EVENT_CONNECTION_REQUIRED: PEER_GRAPH_EVENT_TYPE = 7
PEER_GRAPH_EVENT_NODE_CHANGED: PEER_GRAPH_EVENT_TYPE = 8
PEER_GRAPH_EVENT_SYNCHRONIZED: PEER_GRAPH_EVENT_TYPE = 9
class PEER_GRAPH_PROPERTIES(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    dwScope: UInt32
    dwMaxRecordSize: UInt32
    pwzGraphId: Windows.Win32.Foundation.PWSTR
    pwzCreatorId: Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: Windows.Win32.Foundation.PWSTR
    pwzComment: Windows.Win32.Foundation.PWSTR
    ulPresenceLifetime: UInt32
    cPresenceMax: UInt32
PEER_GRAPH_PROPERTY_FLAGS = Int32
PEER_GRAPH_PROPERTY_HEARTBEATS: PEER_GRAPH_PROPERTY_FLAGS = 1
PEER_GRAPH_PROPERTY_DEFER_EXPIRATION: PEER_GRAPH_PROPERTY_FLAGS = 2
PEER_GRAPH_SCOPE = Int32
PEER_GRAPH_SCOPE_ANY: PEER_GRAPH_SCOPE = 0
PEER_GRAPH_SCOPE_GLOBAL: PEER_GRAPH_SCOPE = 1
PEER_GRAPH_SCOPE_SITELOCAL: PEER_GRAPH_SCOPE = 2
PEER_GRAPH_SCOPE_LINKLOCAL: PEER_GRAPH_SCOPE = 3
PEER_GRAPH_SCOPE_LOOPBACK: PEER_GRAPH_SCOPE = 4
PEER_GRAPH_STATUS_FLAGS = Int32
PEER_GRAPH_STATUS_LISTENING: PEER_GRAPH_STATUS_FLAGS = 1
PEER_GRAPH_STATUS_HAS_CONNECTIONS: PEER_GRAPH_STATUS_FLAGS = 2
PEER_GRAPH_STATUS_SYNCHRONIZED: PEER_GRAPH_STATUS_FLAGS = 4
PEER_GROUP_AUTHENTICATION_SCHEME = Int32
PEER_GROUP_GMC_AUTHENTICATION: PEER_GROUP_AUTHENTICATION_SCHEME = 1
PEER_GROUP_PASSWORD_AUTHENTICATION: PEER_GROUP_AUTHENTICATION_SCHEME = 2
class PEER_GROUP_EVENT_DATA(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        dwStatus: Windows.Win32.NetworkManagement.P2P.PEER_GROUP_STATUS
        incomingData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        memberChangeData: Windows.Win32.NetworkManagement.P2P.PEER_EVENT_MEMBER_CHANGE_DATA
        hrConnectionFailedReason: Windows.Win32.Foundation.HRESULT
class PEER_GROUP_EVENT_REGISTRATION(EasyCastStructure):
    eventType: Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
    pType: POINTER(Guid)
PEER_GROUP_EVENT_TYPE = Int32
PEER_GROUP_EVENT_STATUS_CHANGED: PEER_GROUP_EVENT_TYPE = 1
PEER_GROUP_EVENT_PROPERTY_CHANGED: PEER_GROUP_EVENT_TYPE = 2
PEER_GROUP_EVENT_RECORD_CHANGED: PEER_GROUP_EVENT_TYPE = 3
PEER_GROUP_EVENT_DIRECT_CONNECTION: PEER_GROUP_EVENT_TYPE = 4
PEER_GROUP_EVENT_NEIGHBOR_CONNECTION: PEER_GROUP_EVENT_TYPE = 5
PEER_GROUP_EVENT_INCOMING_DATA: PEER_GROUP_EVENT_TYPE = 6
PEER_GROUP_EVENT_MEMBER_CHANGED: PEER_GROUP_EVENT_TYPE = 8
PEER_GROUP_EVENT_CONNECTION_FAILED: PEER_GROUP_EVENT_TYPE = 10
PEER_GROUP_EVENT_AUTHENTICATION_FAILED: PEER_GROUP_EVENT_TYPE = 11
PEER_GROUP_ISSUE_CREDENTIAL_FLAGS = Int32
PEER_GROUP_STORE_CREDENTIALS: PEER_GROUP_ISSUE_CREDENTIAL_FLAGS = 1
class PEER_GROUP_PROPERTIES(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloud: Windows.Win32.Foundation.PWSTR
    pwzClassifier: Windows.Win32.Foundation.PWSTR
    pwzGroupPeerName: Windows.Win32.Foundation.PWSTR
    pwzCreatorPeerName: Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: Windows.Win32.Foundation.PWSTR
    pwzComment: Windows.Win32.Foundation.PWSTR
    ulMemberDataLifetime: UInt32
    ulPresenceLifetime: UInt32
    dwAuthenticationSchemes: UInt32
    pwzGroupPassword: Windows.Win32.Foundation.PWSTR
    groupPasswordRole: Guid
PEER_GROUP_PROPERTY_FLAGS = Int32
PEER_MEMBER_DATA_OPTIONAL: PEER_GROUP_PROPERTY_FLAGS = 1
PEER_DISABLE_PRESENCE: PEER_GROUP_PROPERTY_FLAGS = 2
PEER_DEFER_EXPIRATION: PEER_GROUP_PROPERTY_FLAGS = 4
PEER_GROUP_STATUS = Int32
PEER_GROUP_STATUS_LISTENING: PEER_GROUP_STATUS = 1
PEER_GROUP_STATUS_HAS_CONNECTIONS: PEER_GROUP_STATUS = 2
class PEER_INVITATION(EasyCastStructure):
    applicationId: Guid
    applicationData: Windows.Win32.NetworkManagement.P2P.PEER_DATA
    pwzMessage: Windows.Win32.Foundation.PWSTR
class PEER_INVITATION_INFO(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloudName: Windows.Win32.Foundation.PWSTR
    dwScope: UInt32
    dwCloudFlags: UInt32
    pwzGroupPeerName: Windows.Win32.Foundation.PWSTR
    pwzIssuerPeerName: Windows.Win32.Foundation.PWSTR
    pwzSubjectPeerName: Windows.Win32.Foundation.PWSTR
    pwzGroupFriendlyName: Windows.Win32.Foundation.PWSTR
    pwzIssuerFriendlyName: Windows.Win32.Foundation.PWSTR
    pwzSubjectFriendlyName: Windows.Win32.Foundation.PWSTR
    ftValidityStart: Windows.Win32.Foundation.FILETIME
    ftValidityEnd: Windows.Win32.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
    cClassifiers: UInt32
    ppwzClassifiers: POINTER(Windows.Win32.Foundation.PWSTR)
    pSubjectPublicKey: POINTER(Windows.Win32.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)
    authScheme: Windows.Win32.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME
class PEER_INVITATION_RESPONSE(EasyCastStructure):
    action: Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE
    pwzMessage: Windows.Win32.Foundation.PWSTR
    hrExtendedInfo: Windows.Win32.Foundation.HRESULT
PEER_INVITATION_RESPONSE_TYPE = Int32
PEER_INVITATION_RESPONSE_DECLINED: PEER_INVITATION_RESPONSE_TYPE = 0
PEER_INVITATION_RESPONSE_ACCEPTED: PEER_INVITATION_RESPONSE_TYPE = 1
PEER_INVITATION_RESPONSE_EXPIRED: PEER_INVITATION_RESPONSE_TYPE = 2
PEER_INVITATION_RESPONSE_ERROR: PEER_INVITATION_RESPONSE_TYPE = 3
class PEER_MEMBER(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzIdentity: Windows.Win32.Foundation.PWSTR
    pwzAttributes: Windows.Win32.Foundation.PWSTR
    ullNodeId: UInt64
    cAddresses: UInt32
    pAddresses: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head)
    pCredentialInfo: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head)
PEER_MEMBER_CHANGE_TYPE = Int32
PEER_MEMBER_CONNECTED: PEER_MEMBER_CHANGE_TYPE = 1
PEER_MEMBER_DISCONNECTED: PEER_MEMBER_CHANGE_TYPE = 2
PEER_MEMBER_UPDATED: PEER_MEMBER_CHANGE_TYPE = 3
PEER_MEMBER_JOINED: PEER_MEMBER_CHANGE_TYPE = 4
PEER_MEMBER_LEFT: PEER_MEMBER_CHANGE_TYPE = 5
PEER_MEMBER_FLAGS = Int32
PEER_MEMBER_PRESENT: PEER_MEMBER_FLAGS = 1
class PEER_NAME_PAIR(EasyCastStructure):
    dwSize: UInt32
    pwzPeerName: Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: Windows.Win32.Foundation.PWSTR
PEER_NODE_CHANGE_TYPE = Int32
PEER_NODE_CHANGE_CONNECTED: PEER_NODE_CHANGE_TYPE = 1
PEER_NODE_CHANGE_DISCONNECTED: PEER_NODE_CHANGE_TYPE = 2
PEER_NODE_CHANGE_UPDATED: PEER_NODE_CHANGE_TYPE = 3
class PEER_NODE_INFO(EasyCastStructure):
    dwSize: UInt32
    ullNodeId: UInt64
    pwzPeerId: Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    pAddresses: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS_head)
    pwzAttributes: Windows.Win32.Foundation.PWSTR
class PEER_OBJECT(EasyCastStructure):
    id: Guid
    data: Windows.Win32.NetworkManagement.P2P.PEER_DATA
    dwPublicationScope: UInt32
class PEER_PEOPLE_NEAR_ME(EasyCastStructure):
    pwzNickName: Windows.Win32.Foundation.PWSTR
    endpoint: Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT
    id: Guid
class PEER_PNRP_CLOUD_INFO(EasyCastStructure):
    pwzCloudName: Windows.Win32.Foundation.PWSTR
    dwScope: Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE
    dwScopeId: UInt32
class PEER_PNRP_ENDPOINT_INFO(EasyCastStructure):
    pwzPeerName: Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head))
    pwzComment: Windows.Win32.Foundation.PWSTR
    payload: Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_PNRP_REGISTRATION_INFO(EasyCastStructure):
    pwzCloudName: Windows.Win32.Foundation.PWSTR
    pwzPublishingIdentity: Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head))
    wPort: UInt16
    pwzComment: Windows.Win32.Foundation.PWSTR
    payload: Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_PRESENCE_INFO(EasyCastStructure):
    status: Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS
    pwzDescriptiveText: Windows.Win32.Foundation.PWSTR
PEER_PRESENCE_STATUS = Int32
PEER_PRESENCE_OFFLINE: PEER_PRESENCE_STATUS = 0
PEER_PRESENCE_OUT_TO_LUNCH: PEER_PRESENCE_STATUS = 1
PEER_PRESENCE_AWAY: PEER_PRESENCE_STATUS = 2
PEER_PRESENCE_BE_RIGHT_BACK: PEER_PRESENCE_STATUS = 3
PEER_PRESENCE_IDLE: PEER_PRESENCE_STATUS = 4
PEER_PRESENCE_BUSY: PEER_PRESENCE_STATUS = 5
PEER_PRESENCE_ON_THE_PHONE: PEER_PRESENCE_STATUS = 6
PEER_PRESENCE_ONLINE: PEER_PRESENCE_STATUS = 7
PEER_PUBLICATION_SCOPE = Int32
PEER_PUBLICATION_SCOPE_NONE: PEER_PUBLICATION_SCOPE = 0
PEER_PUBLICATION_SCOPE_NEAR_ME: PEER_PUBLICATION_SCOPE = 1
PEER_PUBLICATION_SCOPE_INTERNET: PEER_PUBLICATION_SCOPE = 2
PEER_PUBLICATION_SCOPE_ALL: PEER_PUBLICATION_SCOPE = 3
class PEER_RECORD(EasyCastStructure):
    dwSize: UInt32
    type: Guid
    id: Guid
    dwVersion: UInt32
    dwFlags: UInt32
    pwzCreatorId: Windows.Win32.Foundation.PWSTR
    pwzModifiedById: Windows.Win32.Foundation.PWSTR
    pwzAttributes: Windows.Win32.Foundation.PWSTR
    ftCreation: Windows.Win32.Foundation.FILETIME
    ftExpiration: Windows.Win32.Foundation.FILETIME
    ftLastModified: Windows.Win32.Foundation.FILETIME
    securityData: Windows.Win32.NetworkManagement.P2P.PEER_DATA
    data: Windows.Win32.NetworkManagement.P2P.PEER_DATA
PEER_RECORD_CHANGE_TYPE = Int32
PEER_RECORD_ADDED: PEER_RECORD_CHANGE_TYPE = 1
PEER_RECORD_UPDATED: PEER_RECORD_CHANGE_TYPE = 2
PEER_RECORD_DELETED: PEER_RECORD_CHANGE_TYPE = 3
PEER_RECORD_EXPIRED: PEER_RECORD_CHANGE_TYPE = 4
PEER_RECORD_FLAGS = Int32
PEER_RECORD_FLAG_AUTOREFRESH: PEER_RECORD_FLAGS = 1
PEER_RECORD_FLAG_DELETED: PEER_RECORD_FLAGS = 2
class PEER_SECURITY_INTERFACE(EasyCastStructure):
    dwSize: UInt32
    pwzSspFilename: Windows.Win32.Foundation.PWSTR
    pwzPackageName: Windows.Win32.Foundation.PWSTR
    cbSecurityInfo: UInt32
    pbSecurityInfo: POINTER(Byte)
    pvContext: c_void_p
    pfnValidateRecord: Windows.Win32.NetworkManagement.P2P.PFNPEER_VALIDATE_RECORD
    pfnSecureRecord: Windows.Win32.NetworkManagement.P2P.PFNPEER_SECURE_RECORD
    pfnFreeSecurityData: Windows.Win32.NetworkManagement.P2P.PFNPEER_FREE_SECURITY_DATA
    pfnAuthFailed: Windows.Win32.NetworkManagement.P2P.PFNPEER_ON_PASSWORD_AUTH_FAILED
PEER_SIGNIN_FLAGS = Int32
PEER_SIGNIN_NONE: PEER_SIGNIN_FLAGS = 0
PEER_SIGNIN_NEAR_ME: PEER_SIGNIN_FLAGS = 1
PEER_SIGNIN_INTERNET: PEER_SIGNIN_FLAGS = 2
PEER_SIGNIN_ALL: PEER_SIGNIN_FLAGS = 3
class PEER_VERSION_DATA(EasyCastStructure):
    wVersion: UInt16
    wHighestVersion: UInt16
PEER_WATCH_PERMISSION = Int32
PEER_WATCH_BLOCKED: PEER_WATCH_PERMISSION = 0
PEER_WATCH_ALLOWED: PEER_WATCH_PERMISSION = 1
@winfunctype_pointer
def PFNPEER_FREE_SECURITY_DATA(hGraph: c_void_p, pvContext: c_void_p, pSecurityData: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_ON_PASSWORD_AUTH_FAILED(hGraph: c_void_p, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_SECURE_RECORD(hGraph: c_void_p, pvContext: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head), changeType: Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE, ppSecurityData: POINTER(POINTER(Windows.Win32.NetworkManagement.P2P.PEER_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_VALIDATE_RECORD(hGraph: c_void_p, pvContext: c_void_p, pRecord: POINTER(Windows.Win32.NetworkManagement.P2P.PEER_RECORD_head), changeType: Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class PNRPCLOUDINFO(EasyCastStructure):
    dwSize: UInt32
    Cloud: Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_ID
    enCloudState: Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE
    enCloudFlags: Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS
class PNRPINFO_V1(EasyCastStructure):
    dwSize: UInt32
    lpwszIdentity: Windows.Win32.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    enNameState: Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
class PNRPINFO_V2(EasyCastStructure):
    dwSize: UInt32
    lpwszIdentity: Windows.Win32.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    enNameState: Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
    enExtendedPayloadType: Windows.Win32.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        blobPayload: Windows.Win32.System.Com.BLOB
        pwszPayload: Windows.Win32.Foundation.PWSTR
PNRP_CLOUD_FLAGS = Int32
PNRP_CLOUD_NO_FLAGS: PNRP_CLOUD_FLAGS = 0
PNRP_CLOUD_NAME_LOCAL: PNRP_CLOUD_FLAGS = 1
PNRP_CLOUD_RESOLVE_ONLY: PNRP_CLOUD_FLAGS = 2
PNRP_CLOUD_FULL_PARTICIPANT: PNRP_CLOUD_FLAGS = 4
class PNRP_CLOUD_ID(EasyCastStructure):
    AddressFamily: Int32
    Scope: Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE
    ScopeId: UInt32
PNRP_CLOUD_STATE = Int32
PNRP_CLOUD_STATE_VIRTUAL: PNRP_CLOUD_STATE = 0
PNRP_CLOUD_STATE_SYNCHRONISING: PNRP_CLOUD_STATE = 1
PNRP_CLOUD_STATE_ACTIVE: PNRP_CLOUD_STATE = 2
PNRP_CLOUD_STATE_DEAD: PNRP_CLOUD_STATE = 3
PNRP_CLOUD_STATE_DISABLED: PNRP_CLOUD_STATE = 4
PNRP_CLOUD_STATE_NO_NET: PNRP_CLOUD_STATE = 5
PNRP_CLOUD_STATE_ALONE: PNRP_CLOUD_STATE = 6
PNRP_EXTENDED_PAYLOAD_TYPE = Int32
PNRP_EXTENDED_PAYLOAD_TYPE_NONE: PNRP_EXTENDED_PAYLOAD_TYPE = 0
PNRP_EXTENDED_PAYLOAD_TYPE_BINARY: PNRP_EXTENDED_PAYLOAD_TYPE = 1
PNRP_EXTENDED_PAYLOAD_TYPE_STRING: PNRP_EXTENDED_PAYLOAD_TYPE = 2
PNRP_REGISTERED_ID_STATE = Int32
PNRP_REGISTERED_ID_STATE_OK: PNRP_REGISTERED_ID_STATE = 1
PNRP_REGISTERED_ID_STATE_PROBLEM: PNRP_REGISTERED_ID_STATE = 2
PNRP_RESOLVE_CRITERIA = Int32
PNRP_RESOLVE_CRITERIA_DEFAULT: PNRP_RESOLVE_CRITERIA = 0
PNRP_RESOLVE_CRITERIA_REMOTE_PEER_NAME: PNRP_RESOLVE_CRITERIA = 1
PNRP_RESOLVE_CRITERIA_NEAREST_REMOTE_PEER_NAME: PNRP_RESOLVE_CRITERIA = 2
PNRP_RESOLVE_CRITERIA_NON_CURRENT_PROCESS_PEER_NAME: PNRP_RESOLVE_CRITERIA = 3
PNRP_RESOLVE_CRITERIA_NEAREST_NON_CURRENT_PROCESS_PEER_NAME: PNRP_RESOLVE_CRITERIA = 4
PNRP_RESOLVE_CRITERIA_ANY_PEER_NAME: PNRP_RESOLVE_CRITERIA = 5
PNRP_RESOLVE_CRITERIA_NEAREST_PEER_NAME: PNRP_RESOLVE_CRITERIA = 6
PNRP_SCOPE = Int32
PNRP_SCOPE_ANY: PNRP_SCOPE = 0
PNRP_GLOBAL_SCOPE: PNRP_SCOPE = 1
PNRP_SITE_LOCAL_SCOPE: PNRP_SCOPE = 2
PNRP_LINK_LOCAL_SCOPE: PNRP_SCOPE = 3
make_head(_module, 'DRT_ADDRESS')
make_head(_module, 'DRT_ADDRESS_LIST')
make_head(_module, 'DRT_BOOTSTRAP_PROVIDER')
make_head(_module, 'DRT_BOOTSTRAP_RESOLVE_CALLBACK')
make_head(_module, 'DRT_DATA')
make_head(_module, 'DRT_EVENT_DATA')
make_head(_module, 'DRT_REGISTRATION')
make_head(_module, 'DRT_SEARCH_INFO')
make_head(_module, 'DRT_SEARCH_RESULT')
make_head(_module, 'DRT_SECURITY_PROVIDER')
make_head(_module, 'DRT_SETTINGS')
make_head(_module, 'PEERDIST_CLIENT_BASIC_INFO')
make_head(_module, 'PEERDIST_CONTENT_TAG')
make_head(_module, 'PEERDIST_PUBLICATION_OPTIONS')
make_head(_module, 'PEERDIST_RETRIEVAL_OPTIONS')
make_head(_module, 'PEERDIST_STATUS_INFO')
make_head(_module, 'PEER_ADDRESS')
make_head(_module, 'PEER_APPLICATION')
make_head(_module, 'PEER_APPLICATION_REGISTRATION_INFO')
make_head(_module, 'PEER_APP_LAUNCH_INFO')
make_head(_module, 'PEER_COLLAB_EVENT_DATA')
make_head(_module, 'PEER_COLLAB_EVENT_REGISTRATION')
make_head(_module, 'PEER_CONNECTION_INFO')
make_head(_module, 'PEER_CONTACT')
make_head(_module, 'PEER_CREDENTIAL_INFO')
make_head(_module, 'PEER_DATA')
make_head(_module, 'PEER_ENDPOINT')
make_head(_module, 'PEER_EVENT_APPLICATION_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_CONNECTION_CHANGE_DATA')
make_head(_module, 'PEER_EVENT_ENDPOINT_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_INCOMING_DATA')
make_head(_module, 'PEER_EVENT_MEMBER_CHANGE_DATA')
make_head(_module, 'PEER_EVENT_NODE_CHANGE_DATA')
make_head(_module, 'PEER_EVENT_OBJECT_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_PRESENCE_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_RECORD_CHANGE_DATA')
make_head(_module, 'PEER_EVENT_REQUEST_STATUS_CHANGED_DATA')
make_head(_module, 'PEER_EVENT_SYNCHRONIZED_DATA')
make_head(_module, 'PEER_EVENT_WATCHLIST_CHANGED_DATA')
make_head(_module, 'PEER_GRAPH_EVENT_DATA')
make_head(_module, 'PEER_GRAPH_EVENT_REGISTRATION')
make_head(_module, 'PEER_GRAPH_PROPERTIES')
make_head(_module, 'PEER_GROUP_EVENT_DATA')
make_head(_module, 'PEER_GROUP_EVENT_REGISTRATION')
make_head(_module, 'PEER_GROUP_PROPERTIES')
make_head(_module, 'PEER_INVITATION')
make_head(_module, 'PEER_INVITATION_INFO')
make_head(_module, 'PEER_INVITATION_RESPONSE')
make_head(_module, 'PEER_MEMBER')
make_head(_module, 'PEER_NAME_PAIR')
make_head(_module, 'PEER_NODE_INFO')
make_head(_module, 'PEER_OBJECT')
make_head(_module, 'PEER_PEOPLE_NEAR_ME')
make_head(_module, 'PEER_PNRP_CLOUD_INFO')
make_head(_module, 'PEER_PNRP_ENDPOINT_INFO')
make_head(_module, 'PEER_PNRP_REGISTRATION_INFO')
make_head(_module, 'PEER_PRESENCE_INFO')
make_head(_module, 'PEER_RECORD')
make_head(_module, 'PEER_SECURITY_INTERFACE')
make_head(_module, 'PEER_VERSION_DATA')
make_head(_module, 'PFNPEER_FREE_SECURITY_DATA')
make_head(_module, 'PFNPEER_ON_PASSWORD_AUTH_FAILED')
make_head(_module, 'PFNPEER_SECURE_RECORD')
make_head(_module, 'PFNPEER_VALIDATE_RECORD')
make_head(_module, 'PNRPCLOUDINFO')
make_head(_module, 'PNRPINFO_V1')
make_head(_module, 'PNRPINFO_V2')
make_head(_module, 'PNRP_CLOUD_ID')
