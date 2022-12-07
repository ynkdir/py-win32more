from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.P2P
import win32more.Networking.WinSock
import win32more.Security.Cryptography
import win32more.System.Com
import win32more.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
NS_PNRPNAME: UInt32 = 38
NS_PNRPCLOUD: UInt32 = 39
PNRPINFO_HINT: UInt32 = 1
NS_PROVIDER_PNRPNAME: Guid = Guid('03fe89cd-766d-4976-b9-c1-bb-9b-c4-2c-7b-4d')
NS_PROVIDER_PNRPCLOUD: Guid = Guid('03fe89ce-766d-4976-b9-c1-bb-9b-c4-2c-7b-4d')
SVCID_PNRPCLOUD: Guid = Guid('c2239ce6-00c0-4fbf-ba-d6-18-13-93-85-a4-9a')
SVCID_PNRPNAME_V1: Guid = Guid('c2239ce5-00c0-4fbf-ba-d6-18-13-93-85-a4-9a')
SVCID_PNRPNAME_V2: Guid = Guid('c2239ce7-00c0-4fbf-ba-d6-18-13-93-85-a4-9a')
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
PEER_E_CLOUD_NOT_FOUND: win32more.Foundation.HRESULT = -2147013395
PEER_E_CLOUD_DISABLED: win32more.Foundation.HRESULT = -2147013394
PEER_E_INVALID_IDENTITY: win32more.Foundation.HRESULT = -2147013393
PEER_E_TOO_MUCH_LOAD: win32more.Foundation.HRESULT = -2147013392
PEER_E_CLOUD_IS_SEARCH_ONLY: win32more.Foundation.HRESULT = -2147013391
PEER_E_CLIENT_INVALID_COMPARTMENT_ID: win32more.Foundation.HRESULT = -2147013390
PEER_E_DUPLICATE_PEER_NAME: win32more.Foundation.HRESULT = -2147013388
PEER_E_CLOUD_IS_DEAD: win32more.Foundation.HRESULT = -2147013387
PEER_E_NOT_FOUND: win32more.Foundation.HRESULT = -2147023728
PEER_E_DISK_FULL: win32more.Foundation.HRESULT = -2147024784
PEER_E_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147024713
PEER_GROUP_ROLE_ADMIN: Guid = Guid('04387127-aa56-450a-8c-e5-4f-56-5c-67-90-f4')
PEER_GROUP_ROLE_MEMBER: Guid = Guid('f12dc4c7-0857-4ca0-93-fc-b1-bb-19-a3-d8-c2')
PEER_GROUP_ROLE_INVITING_MEMBER: Guid = Guid('4370fd89-dc18-4cfb-8d-bf-98-53-a8-a9-f9-05')
PEER_COLLAB_OBJECTID_USER_PICTURE: Guid = Guid('dd15f41f-fc4e-4922-b0-35-4c-06-a7-54-d0-1d')
FACILITY_DRT: UInt32 = 98
DRT_E_TIMEOUT: win32more.Foundation.HRESULT = -2141057023
DRT_E_INVALID_KEY_SIZE: win32more.Foundation.HRESULT = -2141057022
DRT_E_INVALID_CERT_CHAIN: win32more.Foundation.HRESULT = -2141057020
DRT_E_INVALID_MESSAGE: win32more.Foundation.HRESULT = -2141057019
DRT_E_NO_MORE: win32more.Foundation.HRESULT = -2141057018
DRT_E_INVALID_MAX_ADDRESSES: win32more.Foundation.HRESULT = -2141057017
DRT_E_SEARCH_IN_PROGRESS: win32more.Foundation.HRESULT = -2141057016
DRT_E_INVALID_KEY: win32more.Foundation.HRESULT = -2141057015
DRT_S_RETRY: win32more.Foundation.HRESULT = 6426640
DRT_E_INVALID_MAX_ENDPOINTS: win32more.Foundation.HRESULT = -2141057007
DRT_E_INVALID_SEARCH_RANGE: win32more.Foundation.HRESULT = -2141057006
DRT_E_INVALID_PORT: win32more.Foundation.HRESULT = -2141052928
DRT_E_INVALID_TRANSPORT_PROVIDER: win32more.Foundation.HRESULT = -2141052927
DRT_E_INVALID_SECURITY_PROVIDER: win32more.Foundation.HRESULT = -2141052926
DRT_E_STILL_IN_USE: win32more.Foundation.HRESULT = -2141052925
DRT_E_INVALID_BOOTSTRAP_PROVIDER: win32more.Foundation.HRESULT = -2141052924
DRT_E_INVALID_ADDRESS: win32more.Foundation.HRESULT = -2141052923
DRT_E_INVALID_SCOPE: win32more.Foundation.HRESULT = -2141052922
DRT_E_TRANSPORT_SHUTTING_DOWN: win32more.Foundation.HRESULT = -2141052921
DRT_E_NO_ADDRESSES_AVAILABLE: win32more.Foundation.HRESULT = -2141052920
DRT_E_DUPLICATE_KEY: win32more.Foundation.HRESULT = -2141052919
DRT_E_TRANSPORTPROVIDER_IN_USE: win32more.Foundation.HRESULT = -2141052918
DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED: win32more.Foundation.HRESULT = -2141052917
DRT_E_SECURITYPROVIDER_IN_USE: win32more.Foundation.HRESULT = -2141052916
DRT_E_SECURITYPROVIDER_NOT_ATTACHED: win32more.Foundation.HRESULT = -2141052915
DRT_E_BOOTSTRAPPROVIDER_IN_USE: win32more.Foundation.HRESULT = -2141052914
DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED: win32more.Foundation.HRESULT = -2141052913
DRT_E_TRANSPORT_ALREADY_BOUND: win32more.Foundation.HRESULT = -2141052671
DRT_E_TRANSPORT_NOT_BOUND: win32more.Foundation.HRESULT = -2141052670
DRT_E_TRANSPORT_UNEXPECTED: win32more.Foundation.HRESULT = -2141052669
DRT_E_TRANSPORT_INVALID_ARGUMENT: win32more.Foundation.HRESULT = -2141052668
DRT_E_TRANSPORT_NO_DEST_ADDRESSES: win32more.Foundation.HRESULT = -2141052667
DRT_E_TRANSPORT_EXECUTING_CALLBACK: win32more.Foundation.HRESULT = -2141052666
DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE: win32more.Foundation.HRESULT = -2141052665
DRT_E_INVALID_SETTINGS: win32more.Foundation.HRESULT = -2141052664
DRT_E_INVALID_SEARCH_INFO: win32more.Foundation.HRESULT = -2141052663
DRT_E_FAULTED: win32more.Foundation.HRESULT = -2141052662
DRT_E_TRANSPORT_STILL_BOUND: win32more.Foundation.HRESULT = -2141052661
DRT_E_INSUFFICIENT_BUFFER: win32more.Foundation.HRESULT = -2141052660
DRT_E_INVALID_INSTANCE_PREFIX: win32more.Foundation.HRESULT = -2141052659
DRT_E_INVALID_SECURITY_MODE: win32more.Foundation.HRESULT = -2141052658
DRT_E_CAPABILITY_MISMATCH: win32more.Foundation.HRESULT = -2141052657
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
def PeerGraphStartup(wVersionRequested: UInt16, pVersionData: POINTER(win32more.NetworkManagement.P2P.PEER_VERSION_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphShutdown() -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphFreeData(pvData: c_void_p) -> Void: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetItemCount(hPeerEnum: c_void_p, pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNextItem(hPeerEnum: c_void_p, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(c_void_p))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEndEnumeration(hPeerEnum: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCreate(pGraphProperties: POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head), pwzDatabaseName: win32more.Foundation.PWSTR, pSecurityInterface: POINTER(win32more.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head), phGraph: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpen(pwzGraphId: win32more.Foundation.PWSTR, pwzPeerId: win32more.Foundation.PWSTR, pwzDatabaseName: win32more.Foundation.PWSTR, pSecurityInterface: POINTER(win32more.NetworkManagement.P2P.PEER_SECURITY_INTERFACE_head), cRecordTypeSyncPrecedence: UInt32, pRecordTypeSyncPrecedence: POINTER(Guid), phGraph: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphListen(hGraph: c_void_p, dwScope: UInt32, dwScopeId: UInt32, wPort: UInt16) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphConnect(hGraph: c_void_p, pwzPeerId: win32more.Foundation.PWSTR, pAddress: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphClose(hGraph: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDelete(pwzGraphId: win32more.Foundation.PWSTR, pwzPeerId: win32more.Foundation.PWSTR, pwzDatabaseName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetStatus(hGraph: c_void_p, pdwStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetProperties(hGraph: c_void_p, ppGraphProperties: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetProperties(hGraph: c_void_p, pGraphProperties: POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphRegisterEvent(hGraph: c_void_p, hEvent: win32more.Foundation.HANDLE, cEventRegistrations: UInt32, pEventRegistrations: POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUnregisterEvent(hPeerEvent: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_DATA_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetRecord(hGraph: c_void_p, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphAddRecord(hGraph: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), pRecordId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUpdateRecord(hGraph: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDeleteRecord(hGraph: c_void_p, pRecordId: POINTER(Guid), fLocal: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumRecords(hGraph: c_void_p, pRecordType: POINTER(Guid), pwzPeerId: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSearchRecords(hGraph: c_void_p, pwzCriteria: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphExportDatabase(hGraph: c_void_p, pwzFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphImportDatabase(hGraph: c_void_p, pwzFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphValidateDeferredRecords(hGraph: c_void_p, cRecordIds: UInt32, pRecordIds: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpenDirectConnection(hGraph: c_void_p, pwzPeerId: win32more.Foundation.PWSTR, pAddress: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSendData(hGraph: c_void_p, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCloseDirectConnection(hGraph: c_void_p, ullConnectionId: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumConnections(hGraph: c_void_p, dwFlags: UInt32, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumNodes(hGraph: c_void_p, pwzPeerId: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetPresence(hGraph: c_void_p, fPresent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNodeInfo(hGraph: c_void_p, ullNodeId: UInt64, ppNodeInfo: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_NODE_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetNodeAttributes(hGraph: c_void_p, pwzAttributes: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphPeerTimeToUniversalTime(hGraph: c_void_p, pftPeerTime: POINTER(win32more.Foundation.FILETIME_head), pftUniversalTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUniversalTimeToPeerTime(hGraph: c_void_p, pftUniversalTime: POINTER(win32more.Foundation.FILETIME_head), pftPeerTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerFreeData(pvData: c_void_p) -> Void: ...
@winfunctype('P2P.dll')
def PeerGetItemCount(hPeerEnum: c_void_p, pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGetNextItem(hPeerEnum: c_void_p, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(c_void_p))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEndEnumeration(hPeerEnum: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupStartup(wVersionRequested: UInt16, pVersionData: POINTER(win32more.NetworkManagement.P2P.PEER_VERSION_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupShutdown() -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreate(pProperties: POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head), phGroup: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpen(pwzIdentity: win32more.Foundation.PWSTR, pwzGroupPeerName: win32more.Foundation.PWSTR, pwzCloud: win32more.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupJoin(pwzIdentity: win32more.Foundation.PWSTR, pwzInvitation: win32more.Foundation.PWSTR, pwzCloud: win32more.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPasswordJoin(pwzIdentity: win32more.Foundation.PWSTR, pwzInvitation: win32more.Foundation.PWSTR, pwzPassword: win32more.Foundation.PWSTR, pwzCloud: win32more.Foundation.PWSTR, phGroup: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnect(hGroup: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnectByAddress(hGroup: c_void_p, cAddresses: UInt32, pAddresses: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupClose(hGroup: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDelete(pwzIdentity: win32more.Foundation.PWSTR, pwzGroupPeerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreateInvitation(hGroup: c_void_p, pwzIdentityInfo: win32more.Foundation.PWSTR, pftExpiration: POINTER(win32more.Foundation.FILETIME_head), cRoles: UInt32, pRoles: POINTER(Guid), ppwzInvitation: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreatePasswordInvitation(hGroup: c_void_p, ppwzInvitation: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupParseInvitation(pwzInvitation: win32more.Foundation.PWSTR, ppInvitationInfo: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetStatus(hGroup: c_void_p, pdwStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetProperties(hGroup: c_void_p, ppProperties: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSetProperties(hGroup: c_void_p, pProperties: POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_PROPERTIES_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumMembers(hGroup: c_void_p, dwFlags: UInt32, pwzIdentity: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpenDirectConnection(hGroup: c_void_p, pwzIdentity: win32more.Foundation.PWSTR, pAddress: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head), pullConnectionId: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCloseDirectConnection(hGroup: c_void_p, ullConnectionId: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumConnections(hGroup: c_void_p, dwFlags: UInt32, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSendData(hGroup: c_void_p, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupRegisterEvent(hGroup: c_void_p, hEvent: win32more.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUnregisterEvent(hPeerEvent: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_DATA_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetRecord(hGroup: c_void_p, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupAddRecord(hGroup: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), pRecordId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUpdateRecord(hGroup: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDeleteRecord(hGroup: c_void_p, pRecordId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumRecords(hGroup: c_void_p, pRecordType: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSearchRecords(hGroup: c_void_p, pwzCriteria: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportDatabase(hGroup: c_void_p, pwzFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportDatabase(hGroup: c_void_p, pwzFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupIssueCredentials(hGroup: c_void_p, pwzSubjectIdentity: win32more.Foundation.PWSTR, pCredentialInfo: POINTER(win32more.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head), dwFlags: UInt32, ppwzInvitation: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportConfig(hGroup: c_void_p, pwzPassword: win32more.Foundation.PWSTR, ppwzXML: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportConfig(pwzXML: win32more.Foundation.PWSTR, pwzPassword: win32more.Foundation.PWSTR, fOverwrite: win32more.Foundation.BOOL, ppwzIdentity: POINTER(win32more.Foundation.PWSTR), ppwzGroup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPeerTimeToUniversalTime(hGroup: c_void_p, pftPeerTime: POINTER(win32more.Foundation.FILETIME_head), pftUniversalTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUniversalTimeToPeerTime(hGroup: c_void_p, pftUniversalTime: POINTER(win32more.Foundation.FILETIME_head), pftPeerTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupResumePasswordAuthentication(hGroup: c_void_p, hPeerEventHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityCreate(pwzClassifier: win32more.Foundation.PWSTR, pwzFriendlyName: win32more.Foundation.PWSTR, hCryptProv: UIntPtr, ppwzIdentity: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetFriendlyName(pwzIdentity: win32more.Foundation.PWSTR, ppwzFriendlyName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentitySetFriendlyName(pwzIdentity: win32more.Foundation.PWSTR, pwzFriendlyName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetCryptKey(pwzIdentity: win32more.Foundation.PWSTR, phCryptProv: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityDelete(pwzIdentity: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumIdentities(phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumGroups(pwzIdentity: win32more.Foundation.PWSTR, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCreatePeerName(pwzIdentity: win32more.Foundation.PWSTR, pwzClassifier: win32more.Foundation.PWSTR, ppwzPeerName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetXML(pwzIdentity: win32more.Foundation.PWSTR, ppwzIdentityXML: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityExport(pwzIdentity: win32more.Foundation.PWSTR, pwzPassword: win32more.Foundation.PWSTR, ppwzExportXML: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityImport(pwzImportXML: win32more.Foundation.PWSTR, pwzPassword: win32more.Foundation.PWSTR, ppwzIdentity: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetDefault(ppwzPeerName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabStartup(wVersionRequested: UInt16) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabShutdown() -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignin(hwndParent: win32more.Foundation.HWND, dwSigninOptions: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignout(dwSigninOptions: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetSigninOptions(pdwSigninOptions: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteContact(pcContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head), pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head), hEvent: win32more.Foundation.HANDLE, phInvitation: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetInvitationResponse(hInvitation: win32more.Foundation.HANDLE, ppInvitationResponse: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCancelInvitation(hInvitation: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCloseHandle(hInvitation: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteContact(pcContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head), pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head), ppResponse: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteEndpoint(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head), hEvent: win32more.Foundation.HANDLE, phInvitation: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteEndpoint(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pcInvitation: POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head), ppResponse: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetAppLaunchInfo(ppLaunchInfo: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_APP_LAUNCH_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterApplication(pcApplication: POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head), registrationType: win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterApplication(pApplicationId: POINTER(Guid), registrationType: win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetApplicationRegistrationInfo(pApplicationId: POINTER(Guid), registrationType: win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, ppApplication: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplicationRegistrationInfo(registrationType: win32more.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetPresenceInfo(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), ppPresenceInfo: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplications(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pApplicationId: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumObjects(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), pObjectId: POINTER(Guid), phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumEndpoints(pcContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head), phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRefreshEndpointData(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteEndpointData(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabQueryContactData(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head), ppwzContactData: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSubscribeEndpointData(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnsubscribeEndpointData(pcEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetPresenceInfo(pcPresenceInfo: POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEndpointName(ppwzEndpointName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetEndpointName(pwzEndpointName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetObject(pcObject: POINTER(win32more.NetworkManagement.P2P.PEER_OBJECT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteObject(pObjectId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterEvent(hEvent: win32more.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_REGISTRATION_head), phPeerEvent: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEventData(hPeerEvent: c_void_p, ppEventData: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_DATA_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterEvent(hPeerEvent: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumPeopleNearMe(phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAddContact(pwzContactData: win32more.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteContact(pwzPeerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetContact(pwzPeerName: win32more.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUpdateContact(pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumContacts(phPeerEnum: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabExportContact(pwzPeerName: win32more.Foundation.PWSTR, ppwzContactData: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabParseContact(pwzContactData: win32more.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerNameToPeerHostName(pwzPeerName: win32more.Foundation.PWSTR, ppwzHostName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerHostNameToPeerName(pwzHostName: win32more.Foundation.PWSTR, ppwzPeerName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartup(wVersionRequested: UInt16) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpShutdown() -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpRegister(pcwzPeerName: win32more.Foundation.PWSTR, pRegistrationInfo: POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head), phRegistration: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUpdateRegistration(hRegistration: c_void_p, pRegistrationInfo: POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUnregister(hRegistration: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpResolve(pcwzPeerName: win32more.Foundation.PWSTR, pcwzCloudName: win32more.Foundation.PWSTR, pcEndpoints: POINTER(UInt32), ppEndpoints: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartResolve(pcwzPeerName: win32more.Foundation.PWSTR, pcwzCloudName: win32more.Foundation.PWSTR, cMaxEndpoints: UInt32, hEvent: win32more.Foundation.HANDLE, phResolve: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetCloudInfo(pcNumClouds: POINTER(UInt32), ppCloudInfo: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_CLOUD_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetEndpoint(hResolve: c_void_p, ppEndpoint: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpEndResolve(hResolve: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreatePnrpBootstrapResolver(fPublish: win32more.Foundation.BOOL, pwzPeerName: win32more.Foundation.PWSTR, pwzCloudName: win32more.Foundation.PWSTR, pwzPublishingIdentity: win32more.Foundation.PWSTR, ppResolver: POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeletePnrpBootstrapResolver(pResolver: POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateDnsBootstrapResolver(port: UInt16, pwszAddress: win32more.Foundation.PWSTR, ppModule: POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDnsBootstrapResolver(pResolver: POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)) -> Void: ...
@winfunctype('drttransport.dll')
def DrtCreateIpv6UdpTransport(scope: win32more.NetworkManagement.P2P.DRT_SCOPE, dwScopeId: UInt32, dwLocalityThreshold: UInt32, pwPort: POINTER(UInt16), phTransport: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drttransport.dll')
def DrtDeleteIpv6UdpTransport(hTransport: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKeySecurityProvider(pRootCert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), pLocalCert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), ppSecurityProvider: POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKey(pLocalCert: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), pKey: POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDerivedKeySecurityProvider(pSecurityProvider: POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateNullSecurityProvider(ppSecurityProvider: POINTER(POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteNullSecurityProvider(pSecurityProvider: POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)) -> Void: ...
@winfunctype('drt.dll')
def DrtOpen(pSettings: POINTER(win32more.NetworkManagement.P2P.DRT_SETTINGS_head), hEvent: win32more.Foundation.HANDLE, pvContext: c_void_p, phDrt: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtClose(hDrt: c_void_p) -> Void: ...
@winfunctype('drt.dll')
def DrtGetEventDataSize(hDrt: c_void_p, pulEventDataLen: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetEventData(hDrt: c_void_p, ulEventDataLen: UInt32, pEventData: POINTER(win32more.NetworkManagement.P2P.DRT_EVENT_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtRegisterKey(hDrt: c_void_p, pRegistration: POINTER(win32more.NetworkManagement.P2P.DRT_REGISTRATION_head), pvKeyContext: c_void_p, phKeyRegistration: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUpdateKey(hKeyRegistration: c_void_p, pAppData: POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUnregisterKey(hKeyRegistration: c_void_p) -> Void: ...
@winfunctype('drt.dll')
def DrtStartSearch(hDrt: c_void_p, pKey: POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head), pInfo: POINTER(win32more.NetworkManagement.P2P.DRT_SEARCH_INFO_head), timeout: UInt32, hEvent: win32more.Foundation.HANDLE, pvContext: c_void_p, hSearchContext: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtContinueSearch(hSearchContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResultSize(hSearchContext: c_void_p, pulSearchResultSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResult(hSearchContext: c_void_p, ulSearchResultSize: UInt32, pSearchResult: POINTER(win32more.NetworkManagement.P2P.DRT_SEARCH_RESULT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPathSize(hSearchContext: c_void_p, pulSearchPathSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPath(hSearchContext: c_void_p, ulSearchPathSize: UInt32, pSearchPath: POINTER(win32more.NetworkManagement.P2P.DRT_ADDRESS_LIST_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtEndSearch(hSearchContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceName(hDrt: c_void_p, ulcbInstanceNameSize: UInt32, pwzDrtInstanceName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceNameSize(hDrt: c_void_p, pulcbInstanceNameSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PeerDist.dll')
def PeerDistStartup(dwVersionRequested: UInt32, phPeerDist: POINTER(IntPtr), pdwSupportedVersion: POINTER(UInt32)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistShutdown(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatus(hPeerDist: IntPtr, pPeerDistStatus: POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotification(hPeerDist: IntPtr, hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head), pPeerDistStatus: POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistUnregisterForStatusChangeNotification(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishStream(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: c_char_p_no, cbContentLength: UInt64, pPublishOptions: POINTER(win32more.NetworkManagement.P2P.PEERDIST_PUBLICATION_OPTIONS_head), hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, phStream: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishAddToStream(hPeerDist: IntPtr, hStream: IntPtr, cbNumberOfBytes: UInt32, pBuffer: c_char_p_no, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishCompleteStream(hPeerDist: IntPtr, hStream: IntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseStreamHandle(hPeerDist: IntPtr, hStream: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerUnpublish(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: c_char_p_no) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: c_char_p_no, ullContentOffset: UInt64, cbContentLength: UInt64, hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerRetrieveContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: c_char_p_no, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCancelAsyncOperation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: c_char_p_no, pOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientOpenContent(hPeerDist: IntPtr, pContentTag: POINTER(win32more.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head), hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCloseContent(hPeerDist: IntPtr, hContentHandle: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: c_char_p_no, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCompleteContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddData(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: c_char_p_no, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientBlockRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: c_char_p_no, dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientStreamRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: c_char_p_no, dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientFlushContent(hPeerDist: IntPtr, pContentTag: POINTER(win32more.NetworkManagement.P2P.PEERDIST_CONTENT_TAG_head), hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCancelAsyncOperation(hPeerDist: IntPtr, hContentHandle: IntPtr, pOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatusEx(hPeerDist: IntPtr, pPeerDistStatus: POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotificationEx(hPeerDist: IntPtr, hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head), pPeerDistStatus: POINTER(win32more.NetworkManagement.P2P.PEERDIST_STATUS_INFO_head)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetOverlappedResult(lpOverlapped: POINTER(win32more.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformationEx(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: c_char_p_no, ullContentOffset: UInt64, cbContentLength: UInt64, pRetrievalOptions: POINTER(win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_head), hCompletionPort: win32more.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientGetInformationByHandle(hPeerDist: IntPtr, hContentHandle: IntPtr, PeerDistClientInfoClass: win32more.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS, dwBufferSize: UInt32, lpInformation: c_void_p) -> UInt32: ...
class DRT_ADDRESS(Structure):
    socketAddress: win32more.Networking.WinSock.SOCKADDR_STORAGE
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
class DRT_ADDRESS_LIST(Structure):
    AddressCount: UInt32
    AddressList: win32more.NetworkManagement.P2P.DRT_ADDRESS * 1
class DRT_BOOTSTRAP_PROVIDER(Structure):
    pvContext: c_void_p
    Attach: IntPtr
    Detach: IntPtr
    InitResolve: IntPtr
    IssueResolve: IntPtr
    EndResolve: IntPtr
    Register: IntPtr
    Unregister: IntPtr
@winfunctype_pointer
def DRT_BOOTSTRAP_RESOLVE_CALLBACK(hr: win32more.Foundation.HRESULT, pvContext: c_void_p, pAddresses: POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_LIST_head), fFatalError: win32more.Foundation.BOOL) -> Void: ...
class DRT_DATA(Structure):
    cb: UInt32
    pb: c_char_p_no
class DRT_EVENT_DATA(Structure):
    type: win32more.NetworkManagement.P2P.DRT_EVENT_TYPE
    hr: win32more.Foundation.HRESULT
    pvContext: c_void_p
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        leafsetKeyChange: _leafsetKeyChange_e__Struct
        registrationStateChange: _registrationStateChange_e__Struct
        statusChange: _statusChange_e__Struct
        class _leafsetKeyChange_e__Struct(Structure):
            change: win32more.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE
            localKey: win32more.NetworkManagement.P2P.DRT_DATA
            remoteKey: win32more.NetworkManagement.P2P.DRT_DATA
        class _registrationStateChange_e__Struct(Structure):
            state: win32more.NetworkManagement.P2P.DRT_REGISTRATION_STATE
            localKey: win32more.NetworkManagement.P2P.DRT_DATA
        class _statusChange_e__Struct(Structure):
            status: win32more.NetworkManagement.P2P.DRT_STATUS
            bootstrapAddresses: _bootstrapAddresses_e__Struct
            class _bootstrapAddresses_e__Struct(Structure):
                cntAddress: UInt32
                pAddresses: POINTER(win32more.Networking.WinSock.SOCKADDR_STORAGE_head)
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
class DRT_REGISTRATION(Structure):
    key: win32more.NetworkManagement.P2P.DRT_DATA
    appData: win32more.NetworkManagement.P2P.DRT_DATA
DRT_REGISTRATION_STATE = Int32
DRT_REGISTRATION_STATE_UNRESOLVEABLE: DRT_REGISTRATION_STATE = 1
DRT_SCOPE = Int32
DRT_GLOBAL_SCOPE: DRT_SCOPE = 1
DRT_SITE_LOCAL_SCOPE: DRT_SCOPE = 2
DRT_LINK_LOCAL_SCOPE: DRT_SCOPE = 3
class DRT_SEARCH_INFO(Structure):
    dwSize: UInt32
    fIterative: win32more.Foundation.BOOL
    fAllowCurrentInstanceMatch: win32more.Foundation.BOOL
    fAnyMatchInRange: win32more.Foundation.BOOL
    cMaxEndpoints: UInt32
    pMaximumKey: POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)
    pMinimumKey: POINTER(win32more.NetworkManagement.P2P.DRT_DATA_head)
class DRT_SEARCH_RESULT(Structure):
    dwSize: UInt32
    type: win32more.NetworkManagement.P2P.DRT_MATCH_TYPE
    pvContext: c_void_p
    registration: win32more.NetworkManagement.P2P.DRT_REGISTRATION
DRT_SECURITY_MODE = Int32
DRT_SECURE_RESOLVE: DRT_SECURITY_MODE = 0
DRT_SECURE_MEMBERSHIP: DRT_SECURITY_MODE = 1
DRT_SECURE_CONFIDENTIALPAYLOAD: DRT_SECURITY_MODE = 2
class DRT_SECURITY_PROVIDER(Structure):
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
class DRT_SETTINGS(Structure):
    dwSize: UInt32
    cbKey: UInt32
    bProtocolMajorVersion: Byte
    bProtocolMinorVersion: Byte
    ulMaxRoutingAddresses: UInt32
    pwzDrtInstancePrefix: win32more.Foundation.PWSTR
    hTransport: c_void_p
    pSecurityProvider: POINTER(win32more.NetworkManagement.P2P.DRT_SECURITY_PROVIDER_head)
    pBootstrapProvider: POINTER(win32more.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER_head)
    eSecurityMode: win32more.NetworkManagement.P2P.DRT_SECURITY_MODE
DRT_STATUS = Int32
DRT_ACTIVE: DRT_STATUS = 0
DRT_ALONE: DRT_STATUS = 1
DRT_NO_NETWORK: DRT_STATUS = 10
DRT_FAULTED: DRT_STATUS = 20
class PEER_ADDRESS(Structure):
    dwSize: UInt32
    sin6: win32more.Networking.WinSock.SOCKADDR_IN6
class PEER_APP_LAUNCH_INFO(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
    pInvitation: POINTER(win32more.NetworkManagement.P2P.PEER_INVITATION_head)
class PEER_APPLICATION(Structure):
    id: Guid
    data: win32more.NetworkManagement.P2P.PEER_DATA
    pwzDescription: win32more.Foundation.PWSTR
class PEER_APPLICATION_REGISTRATION_INFO(Structure):
    application: win32more.NetworkManagement.P2P.PEER_APPLICATION
    pwzApplicationToLaunch: win32more.Foundation.PWSTR
    pwzApplicationArguments: win32more.Foundation.PWSTR
    dwPublicationScope: UInt32
PEER_APPLICATION_REGISTRATION_TYPE = Int32
PEER_APPLICATION_CURRENT_USER: PEER_APPLICATION_REGISTRATION_TYPE = 0
PEER_APPLICATION_ALL_USERS: PEER_APPLICATION_REGISTRATION_TYPE = 1
PEER_CHANGE_TYPE = Int32
PEER_CHANGE_ADDED: PEER_CHANGE_TYPE = 0
PEER_CHANGE_DELETED: PEER_CHANGE_TYPE = 1
PEER_CHANGE_UPDATED: PEER_CHANGE_TYPE = 2
class PEER_COLLAB_EVENT_DATA(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        watchListChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_WATCHLIST_CHANGED_DATA
        presenceChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_PRESENCE_CHANGED_DATA
        applicationChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_APPLICATION_CHANGED_DATA
        objectChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_OBJECT_CHANGED_DATA
        endpointChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_ENDPOINT_CHANGED_DATA
        peopleNearMeChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA
        requestStatusChangedData: win32more.NetworkManagement.P2P.PEER_EVENT_REQUEST_STATUS_CHANGED_DATA
class PEER_COLLAB_EVENT_REGISTRATION(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
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
class PEER_CONNECTION_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    ullConnectionId: UInt64
    ullNodeId: UInt64
    pwzPeerId: win32more.Foundation.PWSTR
    address: win32more.NetworkManagement.P2P.PEER_ADDRESS
PEER_CONNECTION_STATUS = Int32
PEER_CONNECTED: PEER_CONNECTION_STATUS = 1
PEER_DISCONNECTED: PEER_CONNECTION_STATUS = 2
PEER_CONNECTION_FAILED: PEER_CONNECTION_STATUS = 3
class PEER_CONTACT(Structure):
    pwzPeerName: win32more.Foundation.PWSTR
    pwzNickName: win32more.Foundation.PWSTR
    pwzDisplayName: win32more.Foundation.PWSTR
    pwzEmailAddress: win32more.Foundation.PWSTR
    fWatch: win32more.Foundation.BOOL
    WatcherPermissions: win32more.NetworkManagement.P2P.PEER_WATCH_PERMISSION
    credentials: win32more.NetworkManagement.P2P.PEER_DATA
class PEER_CREDENTIAL_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzFriendlyName: win32more.Foundation.PWSTR
    pPublicKey: POINTER(win32more.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)
    pwzIssuerPeerName: win32more.Foundation.PWSTR
    pwzIssuerFriendlyName: win32more.Foundation.PWSTR
    ftValidityStart: win32more.Foundation.FILETIME
    ftValidityEnd: win32more.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
class PEER_DATA(Structure):
    cbData: UInt32
    pbData: c_char_p_no
class PEER_ENDPOINT(Structure):
    address: win32more.NetworkManagement.P2P.PEER_ADDRESS
    pwzEndpointName: win32more.Foundation.PWSTR
class PEER_EVENT_APPLICATION_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pApplication: POINTER(win32more.NetworkManagement.P2P.PEER_APPLICATION_head)
class PEER_EVENT_CONNECTION_CHANGE_DATA(Structure):
    dwSize: UInt32
    status: win32more.NetworkManagement.P2P.PEER_CONNECTION_STATUS
    ullConnectionId: UInt64
    ullNodeId: UInt64
    ullNextConnectionId: UInt64
    hrConnectionFailedReason: win32more.Foundation.HRESULT
class PEER_EVENT_ENDPOINT_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
class PEER_EVENT_INCOMING_DATA(Structure):
    dwSize: UInt32
    ullConnectionId: UInt64
    type: Guid
    data: win32more.NetworkManagement.P2P.PEER_DATA
class PEER_EVENT_MEMBER_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE
    pwzIdentity: win32more.Foundation.PWSTR
class PEER_EVENT_NODE_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE
    ullNodeId: UInt64
    pwzPeerId: win32more.Foundation.PWSTR
class PEER_EVENT_OBJECT_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pObject: POINTER(win32more.NetworkManagement.P2P.PEER_OBJECT_head)
class PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA(Structure):
    changeType: win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPeopleNearMe: POINTER(win32more.NetworkManagement.P2P.PEER_PEOPLE_NEAR_ME_head)
class PEER_EVENT_PRESENCE_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
    changeType: win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPresenceInfo: POINTER(win32more.NetworkManagement.P2P.PEER_PRESENCE_INFO_head)
class PEER_EVENT_RECORD_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE
    recordId: Guid
    recordType: Guid
class PEER_EVENT_REQUEST_STATUS_CHANGED_DATA(Structure):
    pEndpoint: POINTER(win32more.NetworkManagement.P2P.PEER_ENDPOINT_head)
    hrChange: win32more.Foundation.HRESULT
class PEER_EVENT_SYNCHRONIZED_DATA(Structure):
    dwSize: UInt32
    recordType: Guid
class PEER_EVENT_WATCHLIST_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.NetworkManagement.P2P.PEER_CONTACT_head)
    changeType: win32more.NetworkManagement.P2P.PEER_CHANGE_TYPE
class PEER_GRAPH_EVENT_DATA(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwStatus: win32more.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS
        incomingData: win32more.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        nodeChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_NODE_CHANGE_DATA
        synchronizedData: win32more.NetworkManagement.P2P.PEER_EVENT_SYNCHRONIZED_DATA
class PEER_GRAPH_EVENT_REGISTRATION(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
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
class PEER_GRAPH_PROPERTIES(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwScope: UInt32
    dwMaxRecordSize: UInt32
    pwzGraphId: win32more.Foundation.PWSTR
    pwzCreatorId: win32more.Foundation.PWSTR
    pwzFriendlyName: win32more.Foundation.PWSTR
    pwzComment: win32more.Foundation.PWSTR
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
class PEER_GROUP_EVENT_DATA(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwStatus: win32more.NetworkManagement.P2P.PEER_GROUP_STATUS
        incomingData: win32more.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        memberChangeData: win32more.NetworkManagement.P2P.PEER_EVENT_MEMBER_CHANGE_DATA
        hrConnectionFailedReason: win32more.Foundation.HRESULT
class PEER_GROUP_EVENT_REGISTRATION(Structure):
    eventType: win32more.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
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
class PEER_GROUP_PROPERTIES(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloud: win32more.Foundation.PWSTR
    pwzClassifier: win32more.Foundation.PWSTR
    pwzGroupPeerName: win32more.Foundation.PWSTR
    pwzCreatorPeerName: win32more.Foundation.PWSTR
    pwzFriendlyName: win32more.Foundation.PWSTR
    pwzComment: win32more.Foundation.PWSTR
    ulMemberDataLifetime: UInt32
    ulPresenceLifetime: UInt32
    dwAuthenticationSchemes: UInt32
    pwzGroupPassword: win32more.Foundation.PWSTR
    groupPasswordRole: Guid
PEER_GROUP_PROPERTY_FLAGS = Int32
PEER_MEMBER_DATA_OPTIONAL: PEER_GROUP_PROPERTY_FLAGS = 1
PEER_DISABLE_PRESENCE: PEER_GROUP_PROPERTY_FLAGS = 2
PEER_DEFER_EXPIRATION: PEER_GROUP_PROPERTY_FLAGS = 4
PEER_GROUP_STATUS = Int32
PEER_GROUP_STATUS_LISTENING: PEER_GROUP_STATUS = 1
PEER_GROUP_STATUS_HAS_CONNECTIONS: PEER_GROUP_STATUS = 2
class PEER_INVITATION(Structure):
    applicationId: Guid
    applicationData: win32more.NetworkManagement.P2P.PEER_DATA
    pwzMessage: win32more.Foundation.PWSTR
class PEER_INVITATION_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloudName: win32more.Foundation.PWSTR
    dwScope: UInt32
    dwCloudFlags: UInt32
    pwzGroupPeerName: win32more.Foundation.PWSTR
    pwzIssuerPeerName: win32more.Foundation.PWSTR
    pwzSubjectPeerName: win32more.Foundation.PWSTR
    pwzGroupFriendlyName: win32more.Foundation.PWSTR
    pwzIssuerFriendlyName: win32more.Foundation.PWSTR
    pwzSubjectFriendlyName: win32more.Foundation.PWSTR
    ftValidityStart: win32more.Foundation.FILETIME
    ftValidityEnd: win32more.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
    cClassifiers: UInt32
    ppwzClassifiers: POINTER(win32more.Foundation.PWSTR)
    pSubjectPublicKey: POINTER(win32more.Security.Cryptography.CERT_PUBLIC_KEY_INFO_head)
    authScheme: win32more.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME
class PEER_INVITATION_RESPONSE(Structure):
    action: win32more.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE
    pwzMessage: win32more.Foundation.PWSTR
    hrExtendedInfo: win32more.Foundation.HRESULT
PEER_INVITATION_RESPONSE_TYPE = Int32
PEER_INVITATION_RESPONSE_DECLINED: PEER_INVITATION_RESPONSE_TYPE = 0
PEER_INVITATION_RESPONSE_ACCEPTED: PEER_INVITATION_RESPONSE_TYPE = 1
PEER_INVITATION_RESPONSE_EXPIRED: PEER_INVITATION_RESPONSE_TYPE = 2
PEER_INVITATION_RESPONSE_ERROR: PEER_INVITATION_RESPONSE_TYPE = 3
class PEER_MEMBER(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzIdentity: win32more.Foundation.PWSTR
    pwzAttributes: win32more.Foundation.PWSTR
    ullNodeId: UInt64
    cAddresses: UInt32
    pAddresses: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head)
    pCredentialInfo: POINTER(win32more.NetworkManagement.P2P.PEER_CREDENTIAL_INFO_head)
PEER_MEMBER_CHANGE_TYPE = Int32
PEER_MEMBER_CONNECTED: PEER_MEMBER_CHANGE_TYPE = 1
PEER_MEMBER_DISCONNECTED: PEER_MEMBER_CHANGE_TYPE = 2
PEER_MEMBER_UPDATED: PEER_MEMBER_CHANGE_TYPE = 3
PEER_MEMBER_JOINED: PEER_MEMBER_CHANGE_TYPE = 4
PEER_MEMBER_LEFT: PEER_MEMBER_CHANGE_TYPE = 5
PEER_MEMBER_FLAGS = Int32
PEER_MEMBER_PRESENT: PEER_MEMBER_FLAGS = 1
class PEER_NAME_PAIR(Structure):
    dwSize: UInt32
    pwzPeerName: win32more.Foundation.PWSTR
    pwzFriendlyName: win32more.Foundation.PWSTR
PEER_NODE_CHANGE_TYPE = Int32
PEER_NODE_CHANGE_CONNECTED: PEER_NODE_CHANGE_TYPE = 1
PEER_NODE_CHANGE_DISCONNECTED: PEER_NODE_CHANGE_TYPE = 2
PEER_NODE_CHANGE_UPDATED: PEER_NODE_CHANGE_TYPE = 3
class PEER_NODE_INFO(Structure):
    dwSize: UInt32
    ullNodeId: UInt64
    pwzPeerId: win32more.Foundation.PWSTR
    cAddresses: UInt32
    pAddresses: POINTER(win32more.NetworkManagement.P2P.PEER_ADDRESS_head)
    pwzAttributes: win32more.Foundation.PWSTR
class PEER_OBJECT(Structure):
    id: Guid
    data: win32more.NetworkManagement.P2P.PEER_DATA
    dwPublicationScope: UInt32
class PEER_PEOPLE_NEAR_ME(Structure):
    pwzNickName: win32more.Foundation.PWSTR
    endpoint: win32more.NetworkManagement.P2P.PEER_ENDPOINT
    id: Guid
class PEER_PNRP_CLOUD_INFO(Structure):
    pwzCloudName: win32more.Foundation.PWSTR
    dwScope: win32more.NetworkManagement.P2P.PNRP_SCOPE
    dwScopeId: UInt32
class PEER_PNRP_ENDPOINT_INFO(Structure):
    pwzPeerName: win32more.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(win32more.Networking.WinSock.SOCKADDR_head))
    pwzComment: win32more.Foundation.PWSTR
    payload: win32more.NetworkManagement.P2P.PEER_DATA
class PEER_PNRP_REGISTRATION_INFO(Structure):
    pwzCloudName: win32more.Foundation.PWSTR
    pwzPublishingIdentity: win32more.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(win32more.Networking.WinSock.SOCKADDR_head))
    wPort: UInt16
    pwzComment: win32more.Foundation.PWSTR
    payload: win32more.NetworkManagement.P2P.PEER_DATA
class PEER_PRESENCE_INFO(Structure):
    status: win32more.NetworkManagement.P2P.PEER_PRESENCE_STATUS
    pwzDescriptiveText: win32more.Foundation.PWSTR
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
class PEER_RECORD(Structure):
    dwSize: UInt32
    type: Guid
    id: Guid
    dwVersion: UInt32
    dwFlags: UInt32
    pwzCreatorId: win32more.Foundation.PWSTR
    pwzModifiedById: win32more.Foundation.PWSTR
    pwzAttributes: win32more.Foundation.PWSTR
    ftCreation: win32more.Foundation.FILETIME
    ftExpiration: win32more.Foundation.FILETIME
    ftLastModified: win32more.Foundation.FILETIME
    securityData: win32more.NetworkManagement.P2P.PEER_DATA
    data: win32more.NetworkManagement.P2P.PEER_DATA
PEER_RECORD_CHANGE_TYPE = Int32
PEER_RECORD_ADDED: PEER_RECORD_CHANGE_TYPE = 1
PEER_RECORD_UPDATED: PEER_RECORD_CHANGE_TYPE = 2
PEER_RECORD_DELETED: PEER_RECORD_CHANGE_TYPE = 3
PEER_RECORD_EXPIRED: PEER_RECORD_CHANGE_TYPE = 4
PEER_RECORD_FLAGS = Int32
PEER_RECORD_FLAG_AUTOREFRESH: PEER_RECORD_FLAGS = 1
PEER_RECORD_FLAG_DELETED: PEER_RECORD_FLAGS = 2
class PEER_SECURITY_INTERFACE(Structure):
    dwSize: UInt32
    pwzSspFilename: win32more.Foundation.PWSTR
    pwzPackageName: win32more.Foundation.PWSTR
    cbSecurityInfo: UInt32
    pbSecurityInfo: c_char_p_no
    pvContext: c_void_p
    pfnValidateRecord: win32more.NetworkManagement.P2P.PFNPEER_VALIDATE_RECORD
    pfnSecureRecord: win32more.NetworkManagement.P2P.PFNPEER_SECURE_RECORD
    pfnFreeSecurityData: win32more.NetworkManagement.P2P.PFNPEER_FREE_SECURITY_DATA
    pfnAuthFailed: win32more.NetworkManagement.P2P.PFNPEER_ON_PASSWORD_AUTH_FAILED
PEER_SIGNIN_FLAGS = Int32
PEER_SIGNIN_NONE: PEER_SIGNIN_FLAGS = 0
PEER_SIGNIN_NEAR_ME: PEER_SIGNIN_FLAGS = 1
PEER_SIGNIN_INTERNET: PEER_SIGNIN_FLAGS = 2
PEER_SIGNIN_ALL: PEER_SIGNIN_FLAGS = 3
class PEER_VERSION_DATA(Structure):
    wVersion: UInt16
    wHighestVersion: UInt16
PEER_WATCH_PERMISSION = Int32
PEER_WATCH_BLOCKED: PEER_WATCH_PERMISSION = 0
PEER_WATCH_ALLOWED: PEER_WATCH_PERMISSION = 1
class PEERDIST_CLIENT_BASIC_INFO(Structure):
    fFlashCrowd: win32more.Foundation.BOOL
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = Int32
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_PeerDistClientBasicInfo: PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 0
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_MaximumPeerDistClientInfoByHandlesClass: PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 1
class PEERDIST_CONTENT_TAG(Structure):
    Data: Byte * 16
class PEERDIST_PUBLICATION_OPTIONS(Structure):
    dwVersion: UInt32
    dwFlags: UInt32
class PEERDIST_RETRIEVAL_OPTIONS(Structure):
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
class PEERDIST_STATUS_INFO(Structure):
    cbSize: UInt32
    status: win32more.NetworkManagement.P2P.PEERDIST_STATUS
    dwMinVer: win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
    dwMaxVer: win32more.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
@winfunctype_pointer
def PFNPEER_FREE_SECURITY_DATA(hGraph: c_void_p, pvContext: c_void_p, pSecurityData: POINTER(win32more.NetworkManagement.P2P.PEER_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_ON_PASSWORD_AUTH_FAILED(hGraph: c_void_p, pvContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_SECURE_RECORD(hGraph: c_void_p, pvContext: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), changeType: win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE, ppSecurityData: POINTER(POINTER(win32more.NetworkManagement.P2P.PEER_DATA_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_VALIDATE_RECORD(hGraph: c_void_p, pvContext: c_void_p, pRecord: POINTER(win32more.NetworkManagement.P2P.PEER_RECORD_head), changeType: win32more.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE) -> win32more.Foundation.HRESULT: ...
PNRP_CLOUD_FLAGS = Int32
PNRP_CLOUD_NO_FLAGS: PNRP_CLOUD_FLAGS = 0
PNRP_CLOUD_NAME_LOCAL: PNRP_CLOUD_FLAGS = 1
PNRP_CLOUD_RESOLVE_ONLY: PNRP_CLOUD_FLAGS = 2
PNRP_CLOUD_FULL_PARTICIPANT: PNRP_CLOUD_FLAGS = 4
class PNRP_CLOUD_ID(Structure):
    AddressFamily: Int32
    Scope: win32more.NetworkManagement.P2P.PNRP_SCOPE
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
class PNRPCLOUDINFO(Structure):
    dwSize: UInt32
    Cloud: win32more.NetworkManagement.P2P.PNRP_CLOUD_ID
    enCloudState: win32more.NetworkManagement.P2P.PNRP_CLOUD_STATE
    enCloudFlags: win32more.NetworkManagement.P2P.PNRP_CLOUD_FLAGS
class PNRPINFO_V1(Structure):
    dwSize: UInt32
    lpwszIdentity: win32more.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: win32more.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: win32more.Networking.WinSock.SOCKET_ADDRESS
    enNameState: win32more.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
class PNRPINFO_V2(Structure):
    dwSize: UInt32
    lpwszIdentity: win32more.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: win32more.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: win32more.Networking.WinSock.SOCKET_ADDRESS
    enNameState: win32more.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
    enExtendedPayloadType: win32more.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        blobPayload: win32more.System.Com.BLOB
        pwszPayload: win32more.Foundation.PWSTR
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
make_head(_module, 'PEER_ADDRESS')
make_head(_module, 'PEER_APP_LAUNCH_INFO')
make_head(_module, 'PEER_APPLICATION')
make_head(_module, 'PEER_APPLICATION_REGISTRATION_INFO')
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
make_head(_module, 'PEERDIST_CLIENT_BASIC_INFO')
make_head(_module, 'PEERDIST_CONTENT_TAG')
make_head(_module, 'PEERDIST_PUBLICATION_OPTIONS')
make_head(_module, 'PEERDIST_RETRIEVAL_OPTIONS')
make_head(_module, 'PEERDIST_STATUS_INFO')
make_head(_module, 'PFNPEER_FREE_SECURITY_DATA')
make_head(_module, 'PFNPEER_ON_PASSWORD_AUTH_FAILED')
make_head(_module, 'PFNPEER_SECURE_RECORD')
make_head(_module, 'PFNPEER_VALIDATE_RECORD')
make_head(_module, 'PNRP_CLOUD_ID')
make_head(_module, 'PNRPCLOUDINFO')
make_head(_module, 'PNRPINFO_V1')
make_head(_module, 'PNRPINFO_V2')
__all__ = [
    "DRT_ACTIVE",
    "DRT_ADDRESS",
    "DRT_ADDRESS_FLAGS",
    "DRT_ADDRESS_FLAG_ACCEPTED",
    "DRT_ADDRESS_FLAG_BAD_VALIDATE_ID",
    "DRT_ADDRESS_FLAG_INQUIRE",
    "DRT_ADDRESS_FLAG_LOOP",
    "DRT_ADDRESS_FLAG_REJECTED",
    "DRT_ADDRESS_FLAG_SUSPECT_UNREGISTERED_ID",
    "DRT_ADDRESS_FLAG_TOO_BUSY",
    "DRT_ADDRESS_FLAG_UNREACHABLE",
    "DRT_ADDRESS_LIST",
    "DRT_ALONE",
    "DRT_BOOTSTRAP_PROVIDER",
    "DRT_BOOTSTRAP_RESOLVE_CALLBACK",
    "DRT_DATA",
    "DRT_EVENT_DATA",
    "DRT_EVENT_LEAFSET_KEY_CHANGED",
    "DRT_EVENT_REGISTRATION_STATE_CHANGED",
    "DRT_EVENT_STATUS_CHANGED",
    "DRT_EVENT_TYPE",
    "DRT_E_BOOTSTRAPPROVIDER_IN_USE",
    "DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED",
    "DRT_E_CAPABILITY_MISMATCH",
    "DRT_E_DUPLICATE_KEY",
    "DRT_E_FAULTED",
    "DRT_E_INSUFFICIENT_BUFFER",
    "DRT_E_INVALID_ADDRESS",
    "DRT_E_INVALID_BOOTSTRAP_PROVIDER",
    "DRT_E_INVALID_CERT_CHAIN",
    "DRT_E_INVALID_INSTANCE_PREFIX",
    "DRT_E_INVALID_KEY",
    "DRT_E_INVALID_KEY_SIZE",
    "DRT_E_INVALID_MAX_ADDRESSES",
    "DRT_E_INVALID_MAX_ENDPOINTS",
    "DRT_E_INVALID_MESSAGE",
    "DRT_E_INVALID_PORT",
    "DRT_E_INVALID_SCOPE",
    "DRT_E_INVALID_SEARCH_INFO",
    "DRT_E_INVALID_SEARCH_RANGE",
    "DRT_E_INVALID_SECURITY_MODE",
    "DRT_E_INVALID_SECURITY_PROVIDER",
    "DRT_E_INVALID_SETTINGS",
    "DRT_E_INVALID_TRANSPORT_PROVIDER",
    "DRT_E_NO_ADDRESSES_AVAILABLE",
    "DRT_E_NO_MORE",
    "DRT_E_SEARCH_IN_PROGRESS",
    "DRT_E_SECURITYPROVIDER_IN_USE",
    "DRT_E_SECURITYPROVIDER_NOT_ATTACHED",
    "DRT_E_STILL_IN_USE",
    "DRT_E_TIMEOUT",
    "DRT_E_TRANSPORTPROVIDER_IN_USE",
    "DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED",
    "DRT_E_TRANSPORT_ALREADY_BOUND",
    "DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE",
    "DRT_E_TRANSPORT_EXECUTING_CALLBACK",
    "DRT_E_TRANSPORT_INVALID_ARGUMENT",
    "DRT_E_TRANSPORT_NOT_BOUND",
    "DRT_E_TRANSPORT_NO_DEST_ADDRESSES",
    "DRT_E_TRANSPORT_SHUTTING_DOWN",
    "DRT_E_TRANSPORT_STILL_BOUND",
    "DRT_E_TRANSPORT_UNEXPECTED",
    "DRT_FAULTED",
    "DRT_GLOBAL_SCOPE",
    "DRT_LEAFSET_KEY_ADDED",
    "DRT_LEAFSET_KEY_CHANGE_TYPE",
    "DRT_LEAFSET_KEY_DELETED",
    "DRT_LINK_LOCAL_ISATAP_SCOPEID",
    "DRT_LINK_LOCAL_SCOPE",
    "DRT_MATCH_EXACT",
    "DRT_MATCH_INTERMEDIATE",
    "DRT_MATCH_NEAR",
    "DRT_MATCH_TYPE",
    "DRT_MAX_INSTANCE_PREFIX_LEN",
    "DRT_MAX_PAYLOAD_SIZE",
    "DRT_MAX_ROUTING_ADDRESSES",
    "DRT_MIN_ROUTING_ADDRESSES",
    "DRT_NO_NETWORK",
    "DRT_PAYLOAD_REVOKED",
    "DRT_REGISTRATION",
    "DRT_REGISTRATION_STATE",
    "DRT_REGISTRATION_STATE_UNRESOLVEABLE",
    "DRT_SCOPE",
    "DRT_SEARCH_INFO",
    "DRT_SEARCH_RESULT",
    "DRT_SECURE_CONFIDENTIALPAYLOAD",
    "DRT_SECURE_MEMBERSHIP",
    "DRT_SECURE_RESOLVE",
    "DRT_SECURITY_MODE",
    "DRT_SECURITY_PROVIDER",
    "DRT_SETTINGS",
    "DRT_SITE_LOCAL_SCOPE",
    "DRT_STATUS",
    "DRT_S_RETRY",
    "DrtClose",
    "DrtContinueSearch",
    "DrtCreateDerivedKey",
    "DrtCreateDerivedKeySecurityProvider",
    "DrtCreateDnsBootstrapResolver",
    "DrtCreateIpv6UdpTransport",
    "DrtCreateNullSecurityProvider",
    "DrtCreatePnrpBootstrapResolver",
    "DrtDeleteDerivedKeySecurityProvider",
    "DrtDeleteDnsBootstrapResolver",
    "DrtDeleteIpv6UdpTransport",
    "DrtDeleteNullSecurityProvider",
    "DrtDeletePnrpBootstrapResolver",
    "DrtEndSearch",
    "DrtGetEventData",
    "DrtGetEventDataSize",
    "DrtGetInstanceName",
    "DrtGetInstanceNameSize",
    "DrtGetSearchPath",
    "DrtGetSearchPathSize",
    "DrtGetSearchResult",
    "DrtGetSearchResultSize",
    "DrtOpen",
    "DrtRegisterKey",
    "DrtStartSearch",
    "DrtUnregisterKey",
    "DrtUpdateKey",
    "FACILITY_DRT",
    "NS_PNRPCLOUD",
    "NS_PNRPNAME",
    "NS_PROVIDER_PNRPCLOUD",
    "NS_PROVIDER_PNRPNAME",
    "PEERDIST_CLIENT_BASIC_INFO",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_MaximumPeerDistClientInfoByHandlesClass",
    "PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS_PeerDistClientBasicInfo",
    "PEERDIST_CONTENT_TAG",
    "PEERDIST_PUBLICATION_OPTIONS",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION_1",
    "PEERDIST_PUBLICATION_OPTIONS_VERSION_2",
    "PEERDIST_READ_TIMEOUT_DEFAULT",
    "PEERDIST_READ_TIMEOUT_LOCAL_CACHE_ONLY",
    "PEERDIST_RETRIEVAL_OPTIONS",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_1",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_2",
    "PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE",
    "PEERDIST_STATUS",
    "PEERDIST_STATUS_AVAILABLE",
    "PEERDIST_STATUS_DISABLED",
    "PEERDIST_STATUS_INFO",
    "PEERDIST_STATUS_UNAVAILABLE",
    "PEER_ADDRESS",
    "PEER_APPLICATION",
    "PEER_APPLICATION_ALL_USERS",
    "PEER_APPLICATION_CURRENT_USER",
    "PEER_APPLICATION_REGISTRATION_INFO",
    "PEER_APPLICATION_REGISTRATION_TYPE",
    "PEER_APP_LAUNCH_INFO",
    "PEER_CHANGE_ADDED",
    "PEER_CHANGE_DELETED",
    "PEER_CHANGE_TYPE",
    "PEER_CHANGE_UPDATED",
    "PEER_COLLAB_EVENT_DATA",
    "PEER_COLLAB_EVENT_REGISTRATION",
    "PEER_COLLAB_EVENT_TYPE",
    "PEER_COLLAB_OBJECTID_USER_PICTURE",
    "PEER_CONNECTED",
    "PEER_CONNECTION_DIRECT",
    "PEER_CONNECTION_FAILED",
    "PEER_CONNECTION_FLAGS",
    "PEER_CONNECTION_INFO",
    "PEER_CONNECTION_NEIGHBOR",
    "PEER_CONNECTION_STATUS",
    "PEER_CONTACT",
    "PEER_CREDENTIAL_INFO",
    "PEER_DATA",
    "PEER_DEFER_EXPIRATION",
    "PEER_DISABLE_PRESENCE",
    "PEER_DISCONNECTED",
    "PEER_ENDPOINT",
    "PEER_EVENT_APPLICATION_CHANGED_DATA",
    "PEER_EVENT_CONNECTION_CHANGE_DATA",
    "PEER_EVENT_ENDPOINT_APPLICATION_CHANGED",
    "PEER_EVENT_ENDPOINT_CHANGED",
    "PEER_EVENT_ENDPOINT_CHANGED_DATA",
    "PEER_EVENT_ENDPOINT_OBJECT_CHANGED",
    "PEER_EVENT_ENDPOINT_PRESENCE_CHANGED",
    "PEER_EVENT_INCOMING_DATA",
    "PEER_EVENT_MEMBER_CHANGE_DATA",
    "PEER_EVENT_MY_APPLICATION_CHANGED",
    "PEER_EVENT_MY_ENDPOINT_CHANGED",
    "PEER_EVENT_MY_OBJECT_CHANGED",
    "PEER_EVENT_MY_PRESENCE_CHANGED",
    "PEER_EVENT_NODE_CHANGE_DATA",
    "PEER_EVENT_OBJECT_CHANGED_DATA",
    "PEER_EVENT_PEOPLE_NEAR_ME_CHANGED",
    "PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA",
    "PEER_EVENT_PRESENCE_CHANGED_DATA",
    "PEER_EVENT_RECORD_CHANGE_DATA",
    "PEER_EVENT_REQUEST_STATUS_CHANGED",
    "PEER_EVENT_REQUEST_STATUS_CHANGED_DATA",
    "PEER_EVENT_SYNCHRONIZED_DATA",
    "PEER_EVENT_WATCHLIST_CHANGED",
    "PEER_EVENT_WATCHLIST_CHANGED_DATA",
    "PEER_E_ALREADY_EXISTS",
    "PEER_E_CLIENT_INVALID_COMPARTMENT_ID",
    "PEER_E_CLOUD_DISABLED",
    "PEER_E_CLOUD_IS_DEAD",
    "PEER_E_CLOUD_IS_SEARCH_ONLY",
    "PEER_E_CLOUD_NOT_FOUND",
    "PEER_E_DISK_FULL",
    "PEER_E_DUPLICATE_PEER_NAME",
    "PEER_E_INVALID_IDENTITY",
    "PEER_E_NOT_FOUND",
    "PEER_E_TOO_MUCH_LOAD",
    "PEER_GRAPH_EVENT_CONNECTION_REQUIRED",
    "PEER_GRAPH_EVENT_DATA",
    "PEER_GRAPH_EVENT_DIRECT_CONNECTION",
    "PEER_GRAPH_EVENT_INCOMING_DATA",
    "PEER_GRAPH_EVENT_NEIGHBOR_CONNECTION",
    "PEER_GRAPH_EVENT_NODE_CHANGED",
    "PEER_GRAPH_EVENT_PROPERTY_CHANGED",
    "PEER_GRAPH_EVENT_RECORD_CHANGED",
    "PEER_GRAPH_EVENT_REGISTRATION",
    "PEER_GRAPH_EVENT_STATUS_CHANGED",
    "PEER_GRAPH_EVENT_SYNCHRONIZED",
    "PEER_GRAPH_EVENT_TYPE",
    "PEER_GRAPH_PROPERTIES",
    "PEER_GRAPH_PROPERTY_DEFER_EXPIRATION",
    "PEER_GRAPH_PROPERTY_FLAGS",
    "PEER_GRAPH_PROPERTY_HEARTBEATS",
    "PEER_GRAPH_SCOPE",
    "PEER_GRAPH_SCOPE_ANY",
    "PEER_GRAPH_SCOPE_GLOBAL",
    "PEER_GRAPH_SCOPE_LINKLOCAL",
    "PEER_GRAPH_SCOPE_LOOPBACK",
    "PEER_GRAPH_SCOPE_SITELOCAL",
    "PEER_GRAPH_STATUS_FLAGS",
    "PEER_GRAPH_STATUS_HAS_CONNECTIONS",
    "PEER_GRAPH_STATUS_LISTENING",
    "PEER_GRAPH_STATUS_SYNCHRONIZED",
    "PEER_GROUP_AUTHENTICATION_SCHEME",
    "PEER_GROUP_EVENT_AUTHENTICATION_FAILED",
    "PEER_GROUP_EVENT_CONNECTION_FAILED",
    "PEER_GROUP_EVENT_DATA",
    "PEER_GROUP_EVENT_DIRECT_CONNECTION",
    "PEER_GROUP_EVENT_INCOMING_DATA",
    "PEER_GROUP_EVENT_MEMBER_CHANGED",
    "PEER_GROUP_EVENT_NEIGHBOR_CONNECTION",
    "PEER_GROUP_EVENT_PROPERTY_CHANGED",
    "PEER_GROUP_EVENT_RECORD_CHANGED",
    "PEER_GROUP_EVENT_REGISTRATION",
    "PEER_GROUP_EVENT_STATUS_CHANGED",
    "PEER_GROUP_EVENT_TYPE",
    "PEER_GROUP_GMC_AUTHENTICATION",
    "PEER_GROUP_ISSUE_CREDENTIAL_FLAGS",
    "PEER_GROUP_PASSWORD_AUTHENTICATION",
    "PEER_GROUP_PROPERTIES",
    "PEER_GROUP_PROPERTY_FLAGS",
    "PEER_GROUP_ROLE_ADMIN",
    "PEER_GROUP_ROLE_INVITING_MEMBER",
    "PEER_GROUP_ROLE_MEMBER",
    "PEER_GROUP_STATUS",
    "PEER_GROUP_STATUS_HAS_CONNECTIONS",
    "PEER_GROUP_STATUS_LISTENING",
    "PEER_GROUP_STORE_CREDENTIALS",
    "PEER_INVITATION",
    "PEER_INVITATION_INFO",
    "PEER_INVITATION_RESPONSE",
    "PEER_INVITATION_RESPONSE_ACCEPTED",
    "PEER_INVITATION_RESPONSE_DECLINED",
    "PEER_INVITATION_RESPONSE_ERROR",
    "PEER_INVITATION_RESPONSE_EXPIRED",
    "PEER_INVITATION_RESPONSE_TYPE",
    "PEER_MEMBER",
    "PEER_MEMBER_CHANGE_TYPE",
    "PEER_MEMBER_CONNECTED",
    "PEER_MEMBER_DATA_OPTIONAL",
    "PEER_MEMBER_DISCONNECTED",
    "PEER_MEMBER_FLAGS",
    "PEER_MEMBER_JOINED",
    "PEER_MEMBER_LEFT",
    "PEER_MEMBER_PRESENT",
    "PEER_MEMBER_UPDATED",
    "PEER_NAME_PAIR",
    "PEER_NODE_CHANGE_CONNECTED",
    "PEER_NODE_CHANGE_DISCONNECTED",
    "PEER_NODE_CHANGE_TYPE",
    "PEER_NODE_CHANGE_UPDATED",
    "PEER_NODE_INFO",
    "PEER_OBJECT",
    "PEER_PEOPLE_NEAR_ME",
    "PEER_PNRP_ALL_LINK_CLOUDS",
    "PEER_PNRP_CLOUD_INFO",
    "PEER_PNRP_ENDPOINT_INFO",
    "PEER_PNRP_REGISTRATION_INFO",
    "PEER_PRESENCE_AWAY",
    "PEER_PRESENCE_BE_RIGHT_BACK",
    "PEER_PRESENCE_BUSY",
    "PEER_PRESENCE_IDLE",
    "PEER_PRESENCE_INFO",
    "PEER_PRESENCE_OFFLINE",
    "PEER_PRESENCE_ONLINE",
    "PEER_PRESENCE_ON_THE_PHONE",
    "PEER_PRESENCE_OUT_TO_LUNCH",
    "PEER_PRESENCE_STATUS",
    "PEER_PUBLICATION_SCOPE",
    "PEER_PUBLICATION_SCOPE_ALL",
    "PEER_PUBLICATION_SCOPE_INTERNET",
    "PEER_PUBLICATION_SCOPE_NEAR_ME",
    "PEER_PUBLICATION_SCOPE_NONE",
    "PEER_RECORD",
    "PEER_RECORD_ADDED",
    "PEER_RECORD_CHANGE_TYPE",
    "PEER_RECORD_DELETED",
    "PEER_RECORD_EXPIRED",
    "PEER_RECORD_FLAGS",
    "PEER_RECORD_FLAG_AUTOREFRESH",
    "PEER_RECORD_FLAG_DELETED",
    "PEER_RECORD_UPDATED",
    "PEER_SECURITY_INTERFACE",
    "PEER_SIGNIN_ALL",
    "PEER_SIGNIN_FLAGS",
    "PEER_SIGNIN_INTERNET",
    "PEER_SIGNIN_NEAR_ME",
    "PEER_SIGNIN_NONE",
    "PEER_VERSION_DATA",
    "PEER_WATCH_ALLOWED",
    "PEER_WATCH_BLOCKED",
    "PEER_WATCH_PERMISSION",
    "PFNPEER_FREE_SECURITY_DATA",
    "PFNPEER_ON_PASSWORD_AUTH_FAILED",
    "PFNPEER_SECURE_RECORD",
    "PFNPEER_VALIDATE_RECORD",
    "PNRPCLOUDINFO",
    "PNRPINFO_HINT",
    "PNRPINFO_V1",
    "PNRPINFO_V2",
    "PNRP_CLOUD_FLAGS",
    "PNRP_CLOUD_FULL_PARTICIPANT",
    "PNRP_CLOUD_ID",
    "PNRP_CLOUD_NAME_LOCAL",
    "PNRP_CLOUD_NO_FLAGS",
    "PNRP_CLOUD_RESOLVE_ONLY",
    "PNRP_CLOUD_STATE",
    "PNRP_CLOUD_STATE_ACTIVE",
    "PNRP_CLOUD_STATE_ALONE",
    "PNRP_CLOUD_STATE_DEAD",
    "PNRP_CLOUD_STATE_DISABLED",
    "PNRP_CLOUD_STATE_NO_NET",
    "PNRP_CLOUD_STATE_SYNCHRONISING",
    "PNRP_CLOUD_STATE_VIRTUAL",
    "PNRP_EXTENDED_PAYLOAD_TYPE",
    "PNRP_EXTENDED_PAYLOAD_TYPE_BINARY",
    "PNRP_EXTENDED_PAYLOAD_TYPE_NONE",
    "PNRP_EXTENDED_PAYLOAD_TYPE_STRING",
    "PNRP_GLOBAL_SCOPE",
    "PNRP_LINK_LOCAL_SCOPE",
    "PNRP_MAX_ENDPOINT_ADDRESSES",
    "PNRP_MAX_EXTENDED_PAYLOAD_BYTES",
    "PNRP_REGISTERED_ID_STATE",
    "PNRP_REGISTERED_ID_STATE_OK",
    "PNRP_REGISTERED_ID_STATE_PROBLEM",
    "PNRP_RESOLVE_CRITERIA",
    "PNRP_RESOLVE_CRITERIA_ANY_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_DEFAULT",
    "PNRP_RESOLVE_CRITERIA_NEAREST_NON_CURRENT_PROCESS_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NEAREST_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NEAREST_REMOTE_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_NON_CURRENT_PROCESS_PEER_NAME",
    "PNRP_RESOLVE_CRITERIA_REMOTE_PEER_NAME",
    "PNRP_SCOPE",
    "PNRP_SCOPE_ANY",
    "PNRP_SITE_LOCAL_SCOPE",
    "PeerCollabAddContact",
    "PeerCollabAsyncInviteContact",
    "PeerCollabAsyncInviteEndpoint",
    "PeerCollabCancelInvitation",
    "PeerCollabCloseHandle",
    "PeerCollabDeleteContact",
    "PeerCollabDeleteEndpointData",
    "PeerCollabDeleteObject",
    "PeerCollabEnumApplicationRegistrationInfo",
    "PeerCollabEnumApplications",
    "PeerCollabEnumContacts",
    "PeerCollabEnumEndpoints",
    "PeerCollabEnumObjects",
    "PeerCollabEnumPeopleNearMe",
    "PeerCollabExportContact",
    "PeerCollabGetAppLaunchInfo",
    "PeerCollabGetApplicationRegistrationInfo",
    "PeerCollabGetContact",
    "PeerCollabGetEndpointName",
    "PeerCollabGetEventData",
    "PeerCollabGetInvitationResponse",
    "PeerCollabGetPresenceInfo",
    "PeerCollabGetSigninOptions",
    "PeerCollabInviteContact",
    "PeerCollabInviteEndpoint",
    "PeerCollabParseContact",
    "PeerCollabQueryContactData",
    "PeerCollabRefreshEndpointData",
    "PeerCollabRegisterApplication",
    "PeerCollabRegisterEvent",
    "PeerCollabSetEndpointName",
    "PeerCollabSetObject",
    "PeerCollabSetPresenceInfo",
    "PeerCollabShutdown",
    "PeerCollabSignin",
    "PeerCollabSignout",
    "PeerCollabStartup",
    "PeerCollabSubscribeEndpointData",
    "PeerCollabUnregisterApplication",
    "PeerCollabUnregisterEvent",
    "PeerCollabUnsubscribeEndpointData",
    "PeerCollabUpdateContact",
    "PeerCreatePeerName",
    "PeerDistClientAddContentInformation",
    "PeerDistClientAddData",
    "PeerDistClientBlockRead",
    "PeerDistClientCancelAsyncOperation",
    "PeerDistClientCloseContent",
    "PeerDistClientCompleteContentInformation",
    "PeerDistClientFlushContent",
    "PeerDistClientGetInformationByHandle",
    "PeerDistClientOpenContent",
    "PeerDistClientStreamRead",
    "PeerDistGetOverlappedResult",
    "PeerDistGetStatus",
    "PeerDistGetStatusEx",
    "PeerDistRegisterForStatusChangeNotification",
    "PeerDistRegisterForStatusChangeNotificationEx",
    "PeerDistServerCancelAsyncOperation",
    "PeerDistServerCloseContentInformation",
    "PeerDistServerCloseStreamHandle",
    "PeerDistServerOpenContentInformation",
    "PeerDistServerOpenContentInformationEx",
    "PeerDistServerPublishAddToStream",
    "PeerDistServerPublishCompleteStream",
    "PeerDistServerPublishStream",
    "PeerDistServerRetrieveContentInformation",
    "PeerDistServerUnpublish",
    "PeerDistShutdown",
    "PeerDistStartup",
    "PeerDistUnregisterForStatusChangeNotification",
    "PeerEndEnumeration",
    "PeerEnumGroups",
    "PeerEnumIdentities",
    "PeerFreeData",
    "PeerGetItemCount",
    "PeerGetNextItem",
    "PeerGraphAddRecord",
    "PeerGraphClose",
    "PeerGraphCloseDirectConnection",
    "PeerGraphConnect",
    "PeerGraphCreate",
    "PeerGraphDelete",
    "PeerGraphDeleteRecord",
    "PeerGraphEndEnumeration",
    "PeerGraphEnumConnections",
    "PeerGraphEnumNodes",
    "PeerGraphEnumRecords",
    "PeerGraphExportDatabase",
    "PeerGraphFreeData",
    "PeerGraphGetEventData",
    "PeerGraphGetItemCount",
    "PeerGraphGetNextItem",
    "PeerGraphGetNodeInfo",
    "PeerGraphGetProperties",
    "PeerGraphGetRecord",
    "PeerGraphGetStatus",
    "PeerGraphImportDatabase",
    "PeerGraphListen",
    "PeerGraphOpen",
    "PeerGraphOpenDirectConnection",
    "PeerGraphPeerTimeToUniversalTime",
    "PeerGraphRegisterEvent",
    "PeerGraphSearchRecords",
    "PeerGraphSendData",
    "PeerGraphSetNodeAttributes",
    "PeerGraphSetPresence",
    "PeerGraphSetProperties",
    "PeerGraphShutdown",
    "PeerGraphStartup",
    "PeerGraphUniversalTimeToPeerTime",
    "PeerGraphUnregisterEvent",
    "PeerGraphUpdateRecord",
    "PeerGraphValidateDeferredRecords",
    "PeerGroupAddRecord",
    "PeerGroupClose",
    "PeerGroupCloseDirectConnection",
    "PeerGroupConnect",
    "PeerGroupConnectByAddress",
    "PeerGroupCreate",
    "PeerGroupCreateInvitation",
    "PeerGroupCreatePasswordInvitation",
    "PeerGroupDelete",
    "PeerGroupDeleteRecord",
    "PeerGroupEnumConnections",
    "PeerGroupEnumMembers",
    "PeerGroupEnumRecords",
    "PeerGroupExportConfig",
    "PeerGroupExportDatabase",
    "PeerGroupGetEventData",
    "PeerGroupGetProperties",
    "PeerGroupGetRecord",
    "PeerGroupGetStatus",
    "PeerGroupImportConfig",
    "PeerGroupImportDatabase",
    "PeerGroupIssueCredentials",
    "PeerGroupJoin",
    "PeerGroupOpen",
    "PeerGroupOpenDirectConnection",
    "PeerGroupParseInvitation",
    "PeerGroupPasswordJoin",
    "PeerGroupPeerTimeToUniversalTime",
    "PeerGroupRegisterEvent",
    "PeerGroupResumePasswordAuthentication",
    "PeerGroupSearchRecords",
    "PeerGroupSendData",
    "PeerGroupSetProperties",
    "PeerGroupShutdown",
    "PeerGroupStartup",
    "PeerGroupUniversalTimeToPeerTime",
    "PeerGroupUnregisterEvent",
    "PeerGroupUpdateRecord",
    "PeerHostNameToPeerName",
    "PeerIdentityCreate",
    "PeerIdentityDelete",
    "PeerIdentityExport",
    "PeerIdentityGetCryptKey",
    "PeerIdentityGetDefault",
    "PeerIdentityGetFriendlyName",
    "PeerIdentityGetXML",
    "PeerIdentityImport",
    "PeerIdentitySetFriendlyName",
    "PeerNameToPeerHostName",
    "PeerPnrpEndResolve",
    "PeerPnrpGetCloudInfo",
    "PeerPnrpGetEndpoint",
    "PeerPnrpRegister",
    "PeerPnrpResolve",
    "PeerPnrpShutdown",
    "PeerPnrpStartResolve",
    "PeerPnrpStartup",
    "PeerPnrpUnregister",
    "PeerPnrpUpdateRegistration",
    "SVCID_PNRPCLOUD",
    "SVCID_PNRPNAME_V1",
    "SVCID_PNRPNAME_V2",
    "WSA_PNRP_CLIENT_INVALID_COMPARTMENT_ID",
    "WSA_PNRP_CLOUD_DISABLED",
    "WSA_PNRP_CLOUD_IS_DEAD",
    "WSA_PNRP_CLOUD_IS_SEARCH_ONLY",
    "WSA_PNRP_CLOUD_NOT_FOUND",
    "WSA_PNRP_DUPLICATE_PEER_NAME",
    "WSA_PNRP_ERROR_BASE",
    "WSA_PNRP_INVALID_IDENTITY",
    "WSA_PNRP_TOO_MUCH_LOAD",
    "WSZ_SCOPE_GLOBAL",
    "WSZ_SCOPE_LINKLOCAL",
    "WSZ_SCOPE_SITELOCAL",
]
