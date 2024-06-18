from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.P2P
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.IO
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
PEER_E_CLOUD_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147013395
PEER_E_CLOUD_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147013394
PEER_E_INVALID_IDENTITY: win32more.Windows.Win32.Foundation.HRESULT = -2147013393
PEER_E_TOO_MUCH_LOAD: win32more.Windows.Win32.Foundation.HRESULT = -2147013392
PEER_E_CLOUD_IS_SEARCH_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2147013391
PEER_E_CLIENT_INVALID_COMPARTMENT_ID: win32more.Windows.Win32.Foundation.HRESULT = -2147013390
PEER_E_DUPLICATE_PEER_NAME: win32more.Windows.Win32.Foundation.HRESULT = -2147013388
PEER_E_CLOUD_IS_DEAD: win32more.Windows.Win32.Foundation.HRESULT = -2147013387
PEER_E_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147023728
PEER_E_DISK_FULL: win32more.Windows.Win32.Foundation.HRESULT = -2147024784
PEER_E_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147024713
PEER_GROUP_ROLE_ADMIN: Guid = Guid('{04387127-aa56-450a-8ce5-4f565c6790f4}')
PEER_GROUP_ROLE_MEMBER: Guid = Guid('{f12dc4c7-0857-4ca0-93fc-b1bb19a3d8c2}')
PEER_GROUP_ROLE_INVITING_MEMBER: Guid = Guid('{4370fd89-dc18-4cfb-8dbf-9853a8a9f905}')
PEER_COLLAB_OBJECTID_USER_PICTURE: Guid = Guid('{dd15f41f-fc4e-4922-b035-4c06a754d01d}')
FACILITY_DRT: UInt32 = 98
DRT_E_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2141057023
DRT_E_INVALID_KEY_SIZE: win32more.Windows.Win32.Foundation.HRESULT = -2141057022
DRT_E_INVALID_CERT_CHAIN: win32more.Windows.Win32.Foundation.HRESULT = -2141057020
DRT_E_INVALID_MESSAGE: win32more.Windows.Win32.Foundation.HRESULT = -2141057019
DRT_E_NO_MORE: win32more.Windows.Win32.Foundation.HRESULT = -2141057018
DRT_E_INVALID_MAX_ADDRESSES: win32more.Windows.Win32.Foundation.HRESULT = -2141057017
DRT_E_SEARCH_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2141057016
DRT_E_INVALID_KEY: win32more.Windows.Win32.Foundation.HRESULT = -2141057015
DRT_S_RETRY: win32more.Windows.Win32.Foundation.HRESULT = 6426640
DRT_E_INVALID_MAX_ENDPOINTS: win32more.Windows.Win32.Foundation.HRESULT = -2141057007
DRT_E_INVALID_SEARCH_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2141057006
DRT_E_INVALID_PORT: win32more.Windows.Win32.Foundation.HRESULT = -2141052928
DRT_E_INVALID_TRANSPORT_PROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2141052927
DRT_E_INVALID_SECURITY_PROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2141052926
DRT_E_STILL_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2141052925
DRT_E_INVALID_BOOTSTRAP_PROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2141052924
DRT_E_INVALID_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -2141052923
DRT_E_INVALID_SCOPE: win32more.Windows.Win32.Foundation.HRESULT = -2141052922
DRT_E_TRANSPORT_SHUTTING_DOWN: win32more.Windows.Win32.Foundation.HRESULT = -2141052921
DRT_E_NO_ADDRESSES_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2141052920
DRT_E_DUPLICATE_KEY: win32more.Windows.Win32.Foundation.HRESULT = -2141052919
DRT_E_TRANSPORTPROVIDER_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2141052918
DRT_E_TRANSPORTPROVIDER_NOT_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2141052917
DRT_E_SECURITYPROVIDER_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2141052916
DRT_E_SECURITYPROVIDER_NOT_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2141052915
DRT_E_BOOTSTRAPPROVIDER_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2141052914
DRT_E_BOOTSTRAPPROVIDER_NOT_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2141052913
DRT_E_TRANSPORT_ALREADY_BOUND: win32more.Windows.Win32.Foundation.HRESULT = -2141052671
DRT_E_TRANSPORT_NOT_BOUND: win32more.Windows.Win32.Foundation.HRESULT = -2141052670
DRT_E_TRANSPORT_UNEXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2141052669
DRT_E_TRANSPORT_INVALID_ARGUMENT: win32more.Windows.Win32.Foundation.HRESULT = -2141052668
DRT_E_TRANSPORT_NO_DEST_ADDRESSES: win32more.Windows.Win32.Foundation.HRESULT = -2141052667
DRT_E_TRANSPORT_EXECUTING_CALLBACK: win32more.Windows.Win32.Foundation.HRESULT = -2141052666
DRT_E_TRANSPORT_ALREADY_EXISTS_FOR_SCOPE: win32more.Windows.Win32.Foundation.HRESULT = -2141052665
DRT_E_INVALID_SETTINGS: win32more.Windows.Win32.Foundation.HRESULT = -2141052664
DRT_E_INVALID_SEARCH_INFO: win32more.Windows.Win32.Foundation.HRESULT = -2141052663
DRT_E_FAULTED: win32more.Windows.Win32.Foundation.HRESULT = -2141052662
DRT_E_TRANSPORT_STILL_BOUND: win32more.Windows.Win32.Foundation.HRESULT = -2141052661
DRT_E_INSUFFICIENT_BUFFER: win32more.Windows.Win32.Foundation.HRESULT = -2141052660
DRT_E_INVALID_INSTANCE_PREFIX: win32more.Windows.Win32.Foundation.HRESULT = -2141052659
DRT_E_INVALID_SECURITY_MODE: win32more.Windows.Win32.Foundation.HRESULT = -2141052658
DRT_E_CAPABILITY_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -2141052657
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
def PeerGraphStartup(wVersionRequested: UInt16, pVersionData: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_VERSION_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphShutdown() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphFreeData(pvData: VoidPtr) -> Void: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetItemCount(hPeerEnum: VoidPtr, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNextItem(hPeerEnum: VoidPtr, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(VoidPtr))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEndEnumeration(hPeerEnum: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCreate(pGraphProperties: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES), pwzDatabaseName: win32more.Windows.Win32.Foundation.PWSTR, pSecurityInterface: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_SECURITY_INTERFACE), phGraph: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpen(pwzGraphId: win32more.Windows.Win32.Foundation.PWSTR, pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, pwzDatabaseName: win32more.Windows.Win32.Foundation.PWSTR, pSecurityInterface: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_SECURITY_INTERFACE), cRecordTypeSyncPrecedence: UInt32, pRecordTypeSyncPrecedence: POINTER(Guid), phGraph: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphListen(hGraph: VoidPtr, dwScope: UInt32, dwScopeId: UInt32, wPort: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphConnect(hGraph: VoidPtr, pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, pAddress: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS), pullConnectionId: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphClose(hGraph: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDelete(pwzGraphId: win32more.Windows.Win32.Foundation.PWSTR, pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, pwzDatabaseName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetStatus(hGraph: VoidPtr, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetProperties(hGraph: VoidPtr, ppGraphProperties: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetProperties(hGraph: VoidPtr, pGraphProperties: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphRegisterEvent(hGraph: VoidPtr, hEvent: win32more.Windows.Win32.Foundation.HANDLE, cEventRegistrations: UInt32, pEventRegistrations: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_REGISTRATION), phPeerEvent: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUnregisterEvent(hPeerEvent: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetEventData(hPeerEvent: VoidPtr, ppEventData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_DATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetRecord(hGraph: VoidPtr, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphAddRecord(hGraph: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD), pRecordId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUpdateRecord(hGraph: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphDeleteRecord(hGraph: VoidPtr, pRecordId: POINTER(Guid), fLocal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumRecords(hGraph: VoidPtr, pRecordType: POINTER(Guid), pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSearchRecords(hGraph: VoidPtr, pwzCriteria: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphExportDatabase(hGraph: VoidPtr, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphImportDatabase(hGraph: VoidPtr, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphValidateDeferredRecords(hGraph: VoidPtr, cRecordIds: UInt32, pRecordIds: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphOpenDirectConnection(hGraph: VoidPtr, pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, pAddress: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS), pullConnectionId: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSendData(hGraph: VoidPtr, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphCloseDirectConnection(hGraph: VoidPtr, ullConnectionId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumConnections(hGraph: VoidPtr, dwFlags: UInt32, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphEnumNodes(hGraph: VoidPtr, pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetPresence(hGraph: VoidPtr, fPresent: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphGetNodeInfo(hGraph: VoidPtr, ullNodeId: UInt64, ppNodeInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_NODE_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphSetNodeAttributes(hGraph: VoidPtr, pwzAttributes: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphPeerTimeToUniversalTime(hGraph: VoidPtr, pftPeerTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftUniversalTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2PGRAPH.dll')
def PeerGraphUniversalTimeToPeerTime(hGraph: VoidPtr, pftUniversalTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftPeerTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerFreeData(pvData: VoidPtr) -> Void: ...
@winfunctype('P2P.dll')
def PeerGetItemCount(hPeerEnum: VoidPtr, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGetNextItem(hPeerEnum: VoidPtr, pCount: POINTER(UInt32), pppvItems: POINTER(POINTER(VoidPtr))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEndEnumeration(hPeerEnum: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupStartup(wVersionRequested: UInt16, pVersionData: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_VERSION_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupShutdown() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreate(pProperties: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES), phGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpen(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzGroupPeerName: win32more.Windows.Win32.Foundation.PWSTR, pwzCloud: win32more.Windows.Win32.Foundation.PWSTR, phGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupJoin(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzInvitation: win32more.Windows.Win32.Foundation.PWSTR, pwzCloud: win32more.Windows.Win32.Foundation.PWSTR, phGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPasswordJoin(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzInvitation: win32more.Windows.Win32.Foundation.PWSTR, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR, pwzCloud: win32more.Windows.Win32.Foundation.PWSTR, phGroup: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnect(hGroup: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupConnectByAddress(hGroup: VoidPtr, cAddresses: UInt32, pAddresses: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupClose(hGroup: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDelete(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzGroupPeerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreateInvitation(hGroup: VoidPtr, pwzIdentityInfo: win32more.Windows.Win32.Foundation.PWSTR, pftExpiration: POINTER(win32more.Windows.Win32.Foundation.FILETIME), cRoles: UInt32, pRoles: POINTER(Guid), ppwzInvitation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCreatePasswordInvitation(hGroup: VoidPtr, ppwzInvitation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupParseInvitation(pwzInvitation: win32more.Windows.Win32.Foundation.PWSTR, ppInvitationInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetStatus(hGroup: VoidPtr, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetProperties(hGroup: VoidPtr, ppProperties: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSetProperties(hGroup: VoidPtr, pProperties: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumMembers(hGroup: VoidPtr, dwFlags: UInt32, pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupOpenDirectConnection(hGroup: VoidPtr, pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pAddress: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS), pullConnectionId: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupCloseDirectConnection(hGroup: VoidPtr, ullConnectionId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumConnections(hGroup: VoidPtr, dwFlags: UInt32, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSendData(hGroup: VoidPtr, ullConnectionId: UInt64, pType: POINTER(Guid), cbData: UInt32, pvData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupRegisterEvent(hGroup: VoidPtr, hEvent: win32more.Windows.Win32.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_REGISTRATION), phPeerEvent: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUnregisterEvent(hPeerEvent: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetEventData(hPeerEvent: VoidPtr, ppEventData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_DATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupGetRecord(hGroup: VoidPtr, pRecordId: POINTER(Guid), ppRecord: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupAddRecord(hGroup: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD), pRecordId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUpdateRecord(hGroup: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupDeleteRecord(hGroup: VoidPtr, pRecordId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupEnumRecords(hGroup: VoidPtr, pRecordType: POINTER(Guid), phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupSearchRecords(hGroup: VoidPtr, pwzCriteria: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportDatabase(hGroup: VoidPtr, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportDatabase(hGroup: VoidPtr, pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupIssueCredentials(hGroup: VoidPtr, pwzSubjectIdentity: win32more.Windows.Win32.Foundation.PWSTR, pCredentialInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CREDENTIAL_INFO), dwFlags: UInt32, ppwzInvitation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupExportConfig(hGroup: VoidPtr, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR, ppwzXML: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupImportConfig(pwzXML: win32more.Windows.Win32.Foundation.PWSTR, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR, fOverwrite: win32more.Windows.Win32.Foundation.BOOL, ppwzIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwzGroup: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupPeerTimeToUniversalTime(hGroup: VoidPtr, pftPeerTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftUniversalTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupUniversalTimeToPeerTime(hGroup: VoidPtr, pftUniversalTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftPeerTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerGroupResumePasswordAuthentication(hGroup: VoidPtr, hPeerEventHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityCreate(pwzClassifier: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, hCryptProv: UIntPtr, ppwzIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetFriendlyName(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppwzFriendlyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentitySetFriendlyName(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetCryptKey(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, phCryptProv: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityDelete(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumIdentities(phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerEnumGroups(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCreatePeerName(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzClassifier: win32more.Windows.Win32.Foundation.PWSTR, ppwzPeerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetXML(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppwzIdentityXML: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityExport(pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR, ppwzExportXML: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityImport(pwzImportXML: win32more.Windows.Win32.Foundation.PWSTR, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR, ppwzIdentity: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerIdentityGetDefault(ppwzPeerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabStartup(wVersionRequested: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabShutdown() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignin(hwndParent: win32more.Windows.Win32.Foundation.HWND, dwSigninOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSignout(dwSigninOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetSigninOptions(pdwSigninOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteContact(pcContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT), pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pcInvitation: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION), hEvent: win32more.Windows.Win32.Foundation.HANDLE, phInvitation: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetInvitationResponse(hInvitation: win32more.Windows.Win32.Foundation.HANDLE, ppInvitationResponse: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCancelInvitation(hInvitation: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabCloseHandle(hInvitation: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteContact(pcContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT), pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pcInvitation: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION), ppResponse: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAsyncInviteEndpoint(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pcInvitation: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION), hEvent: win32more.Windows.Win32.Foundation.HANDLE, phInvitation: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabInviteEndpoint(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pcInvitation: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION), ppResponse: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetAppLaunchInfo(ppLaunchInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_APP_LAUNCH_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterApplication(pcApplication: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO), registrationType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterApplication(pApplicationId: POINTER(Guid), registrationType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetApplicationRegistrationInfo(pApplicationId: POINTER(Guid), registrationType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, ppApplication: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplicationRegistrationInfo(registrationType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE, phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetPresenceInfo(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), ppPresenceInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumApplications(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pApplicationId: POINTER(Guid), phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumObjects(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), pObjectId: POINTER(Guid), phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumEndpoints(pcContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT), phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRefreshEndpointData(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteEndpointData(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabQueryContactData(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT), ppwzContactData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSubscribeEndpointData(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnsubscribeEndpointData(pcEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetPresenceInfo(pcPresenceInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEndpointName(ppwzEndpointName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetEndpointName(pwzEndpointName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabSetObject(pcObject: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_OBJECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteObject(pObjectId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabRegisterEvent(hEvent: win32more.Windows.Win32.Foundation.HANDLE, cEventRegistration: UInt32, pEventRegistrations: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_REGISTRATION), phPeerEvent: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetEventData(hPeerEvent: VoidPtr, ppEventData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_DATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUnregisterEvent(hPeerEvent: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumPeopleNearMe(phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabAddContact(pwzContactData: win32more.Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabDeleteContact(pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabGetContact(pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabUpdateContact(pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabEnumContacts(phPeerEnum: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabExportContact(pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, ppwzContactData: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerCollabParseContact(pwzContactData: win32more.Windows.Win32.Foundation.PWSTR, ppContact: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerNameToPeerHostName(pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, ppwzHostName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerHostNameToPeerName(pwzHostName: win32more.Windows.Win32.Foundation.PWSTR, ppwzPeerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartup(wVersionRequested: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpShutdown() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpRegister(pcwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, pRegistrationInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO), phRegistration: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUpdateRegistration(hRegistration: VoidPtr, pRegistrationInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PNRP_REGISTRATION_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpUnregister(hRegistration: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpResolve(pcwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, pcwzCloudName: win32more.Windows.Win32.Foundation.PWSTR, pcEndpoints: POINTER(UInt32), ppEndpoints: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpStartResolve(pcwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, pcwzCloudName: win32more.Windows.Win32.Foundation.PWSTR, cMaxEndpoints: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE, phResolve: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetCloudInfo(pcNumClouds: POINTER(UInt32), ppCloudInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PNRP_CLOUD_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpGetEndpoint(hResolve: VoidPtr, ppEndpoint: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PNRP_ENDPOINT_INFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('P2P.dll')
def PeerPnrpEndResolve(hResolve: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreatePnrpBootstrapResolver(fPublish: win32more.Windows.Win32.Foundation.BOOL, pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR, pwzCloudName: win32more.Windows.Win32.Foundation.PWSTR, pwzPublishingIdentity: win32more.Windows.Win32.Foundation.PWSTR, ppResolver: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeletePnrpBootstrapResolver(pResolver: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateDnsBootstrapResolver(port: UInt16, pwszAddress: win32more.Windows.Win32.Foundation.PWSTR, ppModule: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDnsBootstrapResolver(pResolver: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER)) -> Void: ...
@winfunctype('drttransport.dll')
def DrtCreateIpv6UdpTransport(scope: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SCOPE, dwScopeId: UInt32, dwLocalityThreshold: UInt32, pwPort: POINTER(UInt16), phTransport: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drttransport.dll')
def DrtDeleteIpv6UdpTransport(hTransport: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKeySecurityProvider(pRootCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), pLocalCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), ppSecurityProvider: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtCreateDerivedKey(pLocalCert: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT), pKey: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteDerivedKeySecurityProvider(pSecurityProvider: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER)) -> Void: ...
@winfunctype('drtprov.dll')
def DrtCreateNullSecurityProvider(ppSecurityProvider: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drtprov.dll')
def DrtDeleteNullSecurityProvider(pSecurityProvider: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER)) -> Void: ...
@winfunctype('drt.dll')
def DrtOpen(pSettings: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SETTINGS), hEvent: win32more.Windows.Win32.Foundation.HANDLE, pvContext: VoidPtr, phDrt: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtClose(hDrt: VoidPtr) -> Void: ...
@winfunctype('drt.dll')
def DrtGetEventDataSize(hDrt: VoidPtr, pulEventDataLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetEventData(hDrt: VoidPtr, ulEventDataLen: UInt32, pEventData: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_EVENT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtRegisterKey(hDrt: VoidPtr, pRegistration: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION), pvKeyContext: VoidPtr, phKeyRegistration: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUpdateKey(hKeyRegistration: VoidPtr, pAppData: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtUnregisterKey(hKeyRegistration: VoidPtr) -> Void: ...
@winfunctype('drt.dll')
def DrtStartSearch(hDrt: VoidPtr, pKey: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA), pInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SEARCH_INFO), timeout: UInt32, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pvContext: VoidPtr, hSearchContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtContinueSearch(hSearchContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResultSize(hSearchContext: VoidPtr, pulSearchResultSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchResult(hSearchContext: VoidPtr, ulSearchResultSize: UInt32, pSearchResult: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SEARCH_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPathSize(hSearchContext: VoidPtr, pulSearchPathSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetSearchPath(hSearchContext: VoidPtr, ulSearchPathSize: UInt32, pSearchPath: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtEndSearch(hSearchContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceName(hDrt: VoidPtr, ulcbInstanceNameSize: UInt32, pwzDrtInstanceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('drt.dll')
def DrtGetInstanceNameSize(hDrt: VoidPtr, pulcbInstanceNameSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PeerDist.dll')
def PeerDistStartup(dwVersionRequested: UInt32, phPeerDist: POINTER(IntPtr), pdwSupportedVersion: POINTER(UInt32)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistShutdown(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatus(hPeerDist: IntPtr, pPeerDistStatus: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotification(hPeerDist: IntPtr, hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), pPeerDistStatus: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistUnregisterForStatusChangeNotification(hPeerDist: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishStream(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), cbContentLength: UInt64, pPublishOptions: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_PUBLICATION_OPTIONS), hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phStream: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishAddToStream(hPeerDist: IntPtr, hStream: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerPublishCompleteStream(hPeerDist: IntPtr, hStream: IntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseStreamHandle(hPeerDist: IntPtr, hStream: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerUnpublish(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), ullContentOffset: UInt64, cbContentLength: UInt64, hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerRetrieveContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCloseContentInformation(hPeerDist: IntPtr, hContentInfo: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistServerCancelAsyncOperation(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientOpenContent(hPeerDist: IntPtr, pContentTag: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_CONTENT_TAG), hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentHandle: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCloseContent(hPeerDist: IntPtr, hContentHandle: IntPtr) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCompleteContentInformation(hPeerDist: IntPtr, hContentHandle: IntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientAddData(hPeerDist: IntPtr, hContentHandle: IntPtr, cbNumberOfBytes: UInt32, pBuffer: POINTER(Byte), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientBlockRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientStreamRead(hPeerDist: IntPtr, hContentHandle: IntPtr, cbMaxNumberOfBytes: UInt32, pBuffer: POINTER(Byte), dwTimeoutInMilliseconds: UInt32, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientFlushContent(hPeerDist: IntPtr, pContentTag: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_CONTENT_TAG), hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientCancelAsyncOperation(hPeerDist: IntPtr, hContentHandle: IntPtr, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetStatusEx(hPeerDist: IntPtr, pPeerDistStatus: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS_INFO)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistRegisterForStatusChangeNotificationEx(hPeerDist: IntPtr, hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), pPeerDistStatus: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS_INFO)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistGetOverlappedResult(lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PeerDist.dll')
def PeerDistServerOpenContentInformationEx(hPeerDist: IntPtr, cbContentIdentifier: UInt32, pContentIdentifier: POINTER(Byte), ullContentOffset: UInt64, cbContentLength: UInt64, pRetrievalOptions: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS), hCompletionPort: win32more.Windows.Win32.Foundation.HANDLE, ulCompletionKey: UIntPtr, phContentInfo: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('PeerDist.dll')
def PeerDistClientGetInformationByHandle(hPeerDist: IntPtr, hContentHandle: IntPtr, PeerDistClientInfoClass: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS, dwBufferSize: UInt32, lpInformation: VoidPtr) -> UInt32: ...
class DRT_ADDRESS(Structure):
    socketAddress: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    flags: UInt32
    nearness: Int32
    latency: UInt32
DRT_ADDRESS_FLAGS = Int32
DRT_ADDRESS_FLAG_ACCEPTED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 1
DRT_ADDRESS_FLAG_REJECTED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 2
DRT_ADDRESS_FLAG_UNREACHABLE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 4
DRT_ADDRESS_FLAG_LOOP: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 8
DRT_ADDRESS_FLAG_TOO_BUSY: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 16
DRT_ADDRESS_FLAG_BAD_VALIDATE_ID: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 32
DRT_ADDRESS_FLAG_SUSPECT_UNREGISTERED_ID: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 64
DRT_ADDRESS_FLAG_INQUIRE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS_FLAGS = 128
class DRT_ADDRESS_LIST(Structure):
    AddressCount: UInt32
    AddressList: win32more.Windows.Win32.NetworkManagement.P2P.DRT_ADDRESS * 1
class DRT_BOOTSTRAP_PROVIDER(Structure):
    pvContext: VoidPtr
    Attach: IntPtr
    Detach: IntPtr
    InitResolve: IntPtr
    IssueResolve: IntPtr
    EndResolve: IntPtr
    Register: IntPtr
    Unregister: IntPtr
@winfunctype_pointer
def DRT_BOOTSTRAP_RESOLVE_CALLBACK(hr: win32more.Windows.Win32.Foundation.HRESULT, pvContext: VoidPtr, pAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS_LIST), fFatalError: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class DRT_DATA(Structure):
    cb: UInt32
    pb: POINTER(Byte)
class DRT_EVENT_DATA(Structure):
    type: win32more.Windows.Win32.NetworkManagement.P2P.DRT_EVENT_TYPE
    hr: win32more.Windows.Win32.Foundation.HRESULT
    pvContext: VoidPtr
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        leafsetKeyChange: _leafsetKeyChange_e__Struct
        registrationStateChange: _registrationStateChange_e__Struct
        statusChange: _statusChange_e__Struct
        class _leafsetKeyChange_e__Struct(Structure):
            change: win32more.Windows.Win32.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE
            localKey: win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA
            remoteKey: win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA
        class _registrationStateChange_e__Struct(Structure):
            state: win32more.Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION_STATE
            localKey: win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA
        class _statusChange_e__Struct(Structure):
            status: win32more.Windows.Win32.NetworkManagement.P2P.DRT_STATUS
            bootstrapAddresses: _bootstrapAddresses_e__Struct
            class _bootstrapAddresses_e__Struct(Structure):
                cntAddress: UInt32
                pAddresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE)
DRT_EVENT_TYPE = Int32
DRT_EVENT_STATUS_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_EVENT_TYPE = 0
DRT_EVENT_LEAFSET_KEY_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_EVENT_TYPE = 1
DRT_EVENT_REGISTRATION_STATE_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_EVENT_TYPE = 2
DRT_LEAFSET_KEY_CHANGE_TYPE = Int32
DRT_LEAFSET_KEY_ADDED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE = 0
DRT_LEAFSET_KEY_DELETED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_LEAFSET_KEY_CHANGE_TYPE = 1
DRT_MATCH_TYPE = Int32
DRT_MATCH_EXACT: win32more.Windows.Win32.NetworkManagement.P2P.DRT_MATCH_TYPE = 0
DRT_MATCH_NEAR: win32more.Windows.Win32.NetworkManagement.P2P.DRT_MATCH_TYPE = 1
DRT_MATCH_INTERMEDIATE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_MATCH_TYPE = 2
class DRT_REGISTRATION(Structure):
    key: win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA
    appData: win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA
DRT_REGISTRATION_STATE = Int32
DRT_REGISTRATION_STATE_UNRESOLVEABLE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION_STATE = 1
DRT_SCOPE = Int32
DRT_GLOBAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SCOPE = 1
DRT_SITE_LOCAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SCOPE = 2
DRT_LINK_LOCAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SCOPE = 3
class DRT_SEARCH_INFO(Structure):
    dwSize: UInt32
    fIterative: win32more.Windows.Win32.Foundation.BOOL
    fAllowCurrentInstanceMatch: win32more.Windows.Win32.Foundation.BOOL
    fAnyMatchInRange: win32more.Windows.Win32.Foundation.BOOL
    cMaxEndpoints: UInt32
    pMaximumKey: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA)
    pMinimumKey: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_DATA)
class DRT_SEARCH_RESULT(Structure):
    dwSize: UInt32
    type: win32more.Windows.Win32.NetworkManagement.P2P.DRT_MATCH_TYPE
    pvContext: VoidPtr
    registration: win32more.Windows.Win32.NetworkManagement.P2P.DRT_REGISTRATION
DRT_SECURITY_MODE = Int32
DRT_SECURE_RESOLVE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_MODE = 0
DRT_SECURE_MEMBERSHIP: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_MODE = 1
DRT_SECURE_CONFIDENTIALPAYLOAD: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_MODE = 2
class DRT_SECURITY_PROVIDER(Structure):
    pvContext: VoidPtr
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
    pwzDrtInstancePrefix: win32more.Windows.Win32.Foundation.PWSTR
    hTransport: VoidPtr
    pSecurityProvider: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_PROVIDER)
    pBootstrapProvider: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.DRT_BOOTSTRAP_PROVIDER)
    eSecurityMode: win32more.Windows.Win32.NetworkManagement.P2P.DRT_SECURITY_MODE
DRT_STATUS = Int32
DRT_ACTIVE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_STATUS = 0
DRT_ALONE: win32more.Windows.Win32.NetworkManagement.P2P.DRT_STATUS = 1
DRT_NO_NETWORK: win32more.Windows.Win32.NetworkManagement.P2P.DRT_STATUS = 10
DRT_FAULTED: win32more.Windows.Win32.NetworkManagement.P2P.DRT_STATUS = 20
class PEERDIST_CLIENT_BASIC_INFO(Structure):
    fFlashCrowd: win32more.Windows.Win32.Foundation.BOOL
PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = Int32
PeerDistClientBasicInfo: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 0
MaximumPeerDistClientInfoByHandlesClass: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS = 1
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
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_1: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 1
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_2: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 2
PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE = 2
PEERDIST_STATUS = Int32
PEERDIST_STATUS_DISABLED: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS = 0
PEERDIST_STATUS_UNAVAILABLE: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS = 1
PEERDIST_STATUS_AVAILABLE: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS = 2
class PEERDIST_STATUS_INFO(Structure):
    cbSize: UInt32
    status: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_STATUS
    dwMinVer: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
    dwMaxVer: win32more.Windows.Win32.NetworkManagement.P2P.PEERDIST_RETRIEVAL_OPTIONS_CONTENTINFO_VERSION_VALUE
class PEER_ADDRESS(Structure):
    dwSize: UInt32
    sin6: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_IN6
class PEER_APPLICATION(Structure):
    id: Guid
    data: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
    pwzDescription: win32more.Windows.Win32.Foundation.PWSTR
class PEER_APPLICATION_REGISTRATION_INFO(Structure):
    application: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION
    pwzApplicationToLaunch: win32more.Windows.Win32.Foundation.PWSTR
    pwzApplicationArguments: win32more.Windows.Win32.Foundation.PWSTR
    dwPublicationScope: UInt32
PEER_APPLICATION_REGISTRATION_TYPE = Int32
PEER_APPLICATION_CURRENT_USER: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE = 0
PEER_APPLICATION_ALL_USERS: win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION_REGISTRATION_TYPE = 1
class PEER_APP_LAUNCH_INFO(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
    pInvitation: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION)
PEER_CHANGE_TYPE = Int32
PEER_CHANGE_ADDED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE = 0
PEER_CHANGE_DELETED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE = 1
PEER_CHANGE_UPDATED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE = 2
class PEER_COLLAB_EVENT_DATA(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        watchListChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_WATCHLIST_CHANGED_DATA
        presenceChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_PRESENCE_CHANGED_DATA
        applicationChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_APPLICATION_CHANGED_DATA
        objectChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_OBJECT_CHANGED_DATA
        endpointChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_ENDPOINT_CHANGED_DATA
        peopleNearMeChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA
        requestStatusChangedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_REQUEST_STATUS_CHANGED_DATA
class PEER_COLLAB_EVENT_REGISTRATION(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE
    pInstance: POINTER(Guid)
PEER_COLLAB_EVENT_TYPE = Int32
PEER_EVENT_WATCHLIST_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 1
PEER_EVENT_ENDPOINT_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 2
PEER_EVENT_ENDPOINT_PRESENCE_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 3
PEER_EVENT_ENDPOINT_APPLICATION_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 4
PEER_EVENT_ENDPOINT_OBJECT_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 5
PEER_EVENT_MY_ENDPOINT_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 6
PEER_EVENT_MY_PRESENCE_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 7
PEER_EVENT_MY_APPLICATION_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 8
PEER_EVENT_MY_OBJECT_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 9
PEER_EVENT_PEOPLE_NEAR_ME_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 10
PEER_EVENT_REQUEST_STATUS_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_COLLAB_EVENT_TYPE = 11
PEER_CONNECTION_FLAGS = Int32
PEER_CONNECTION_NEIGHBOR: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_FLAGS = 1
PEER_CONNECTION_DIRECT: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_FLAGS = 2
class PEER_CONNECTION_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    ullConnectionId: UInt64
    ullNodeId: UInt64
    pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR
    address: win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS
PEER_CONNECTION_STATUS = Int32
PEER_CONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_STATUS = 1
PEER_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_STATUS = 2
PEER_CONNECTION_FAILED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_STATUS = 3
class PEER_CONTACT(Structure):
    pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzNickName: win32more.Windows.Win32.Foundation.PWSTR
    pwzDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    pwzEmailAddress: win32more.Windows.Win32.Foundation.PWSTR
    fWatch: win32more.Windows.Win32.Foundation.BOOL
    WatcherPermissions: win32more.Windows.Win32.NetworkManagement.P2P.PEER_WATCH_PERMISSION
    credentials: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_CREDENTIAL_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    pPublicKey: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_PUBLIC_KEY_INFO)
    pwzIssuerPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzIssuerFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    ftValidityStart: win32more.Windows.Win32.Foundation.FILETIME
    ftValidityEnd: win32more.Windows.Win32.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
class PEER_DATA(Structure):
    cbData: UInt32
    pbData: POINTER(Byte)
class PEER_ENDPOINT(Structure):
    address: win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS
    pwzEndpointName: win32more.Windows.Win32.Foundation.PWSTR
class PEER_EVENT_APPLICATION_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pApplication: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_APPLICATION)
class PEER_EVENT_CONNECTION_CHANGE_DATA(Structure):
    dwSize: UInt32
    status: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONNECTION_STATUS
    ullConnectionId: UInt64
    ullNodeId: UInt64
    ullNextConnectionId: UInt64
    hrConnectionFailedReason: win32more.Windows.Win32.Foundation.HRESULT
class PEER_EVENT_ENDPOINT_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
class PEER_EVENT_INCOMING_DATA(Structure):
    dwSize: UInt32
    ullConnectionId: UInt64
    type: Guid
    data: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_EVENT_MEMBER_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE
    pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR
class PEER_EVENT_NODE_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE
    ullNodeId: UInt64
    pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR
class PEER_EVENT_OBJECT_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pObject: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_OBJECT)
class PEER_EVENT_PEOPLE_NEAR_ME_CHANGED_DATA(Structure):
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPeopleNearMe: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PEOPLE_NEAR_ME)
class PEER_EVENT_PRESENCE_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
    pPresenceInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_INFO)
class PEER_EVENT_RECORD_CHANGE_DATA(Structure):
    dwSize: UInt32
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE
    recordId: Guid
    recordType: Guid
class PEER_EVENT_REQUEST_STATUS_CHANGED_DATA(Structure):
    pEndpoint: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT)
    hrChange: win32more.Windows.Win32.Foundation.HRESULT
class PEER_EVENT_SYNCHRONIZED_DATA(Structure):
    dwSize: UInt32
    recordType: Guid
class PEER_EVENT_WATCHLIST_CHANGED_DATA(Structure):
    pContact: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CONTACT)
    changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_CHANGE_TYPE
class PEER_GRAPH_EVENT_DATA(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwStatus: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS
        incomingData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        nodeChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_NODE_CHANGE_DATA
        synchronizedData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_SYNCHRONIZED_DATA
class PEER_GRAPH_EVENT_REGISTRATION(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE
    pType: POINTER(Guid)
PEER_GRAPH_EVENT_TYPE = Int32
PEER_GRAPH_EVENT_STATUS_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 1
PEER_GRAPH_EVENT_PROPERTY_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 2
PEER_GRAPH_EVENT_RECORD_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 3
PEER_GRAPH_EVENT_DIRECT_CONNECTION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 4
PEER_GRAPH_EVENT_NEIGHBOR_CONNECTION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 5
PEER_GRAPH_EVENT_INCOMING_DATA: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 6
PEER_GRAPH_EVENT_CONNECTION_REQUIRED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 7
PEER_GRAPH_EVENT_NODE_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 8
PEER_GRAPH_EVENT_SYNCHRONIZED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_EVENT_TYPE = 9
class PEER_GRAPH_PROPERTIES(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwScope: UInt32
    dwMaxRecordSize: UInt32
    pwzGraphId: win32more.Windows.Win32.Foundation.PWSTR
    pwzCreatorId: win32more.Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    pwzComment: win32more.Windows.Win32.Foundation.PWSTR
    ulPresenceLifetime: UInt32
    cPresenceMax: UInt32
PEER_GRAPH_PROPERTY_FLAGS = Int32
PEER_GRAPH_PROPERTY_HEARTBEATS: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTY_FLAGS = 1
PEER_GRAPH_PROPERTY_DEFER_EXPIRATION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_PROPERTY_FLAGS = 2
PEER_GRAPH_SCOPE = Int32
PEER_GRAPH_SCOPE_ANY: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_SCOPE = 0
PEER_GRAPH_SCOPE_GLOBAL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_SCOPE = 1
PEER_GRAPH_SCOPE_SITELOCAL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_SCOPE = 2
PEER_GRAPH_SCOPE_LINKLOCAL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_SCOPE = 3
PEER_GRAPH_SCOPE_LOOPBACK: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_SCOPE = 4
PEER_GRAPH_STATUS_FLAGS = Int32
PEER_GRAPH_STATUS_LISTENING: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS = 1
PEER_GRAPH_STATUS_HAS_CONNECTIONS: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS = 2
PEER_GRAPH_STATUS_SYNCHRONIZED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GRAPH_STATUS_FLAGS = 4
PEER_GROUP_AUTHENTICATION_SCHEME = Int32
PEER_GROUP_GMC_AUTHENTICATION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME = 1
PEER_GROUP_PASSWORD_AUTHENTICATION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME = 2
class PEER_GROUP_EVENT_DATA(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwStatus: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_STATUS
        incomingData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_INCOMING_DATA
        recordChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_RECORD_CHANGE_DATA
        connectionChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_CONNECTION_CHANGE_DATA
        memberChangeData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_EVENT_MEMBER_CHANGE_DATA
        hrConnectionFailedReason: win32more.Windows.Win32.Foundation.HRESULT
class PEER_GROUP_EVENT_REGISTRATION(Structure):
    eventType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE
    pType: POINTER(Guid)
PEER_GROUP_EVENT_TYPE = Int32
PEER_GROUP_EVENT_STATUS_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 1
PEER_GROUP_EVENT_PROPERTY_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 2
PEER_GROUP_EVENT_RECORD_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 3
PEER_GROUP_EVENT_DIRECT_CONNECTION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 4
PEER_GROUP_EVENT_NEIGHBOR_CONNECTION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 5
PEER_GROUP_EVENT_INCOMING_DATA: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 6
PEER_GROUP_EVENT_MEMBER_CHANGED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 8
PEER_GROUP_EVENT_CONNECTION_FAILED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 10
PEER_GROUP_EVENT_AUTHENTICATION_FAILED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_EVENT_TYPE = 11
PEER_GROUP_ISSUE_CREDENTIAL_FLAGS = Int32
PEER_GROUP_STORE_CREDENTIALS: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_ISSUE_CREDENTIAL_FLAGS = 1
class PEER_GROUP_PROPERTIES(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloud: win32more.Windows.Win32.Foundation.PWSTR
    pwzClassifier: win32more.Windows.Win32.Foundation.PWSTR
    pwzGroupPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzCreatorPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    pwzComment: win32more.Windows.Win32.Foundation.PWSTR
    ulMemberDataLifetime: UInt32
    ulPresenceLifetime: UInt32
    dwAuthenticationSchemes: UInt32
    pwzGroupPassword: win32more.Windows.Win32.Foundation.PWSTR
    groupPasswordRole: Guid
PEER_GROUP_PROPERTY_FLAGS = Int32
PEER_MEMBER_DATA_OPTIONAL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTY_FLAGS = 1
PEER_DISABLE_PRESENCE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTY_FLAGS = 2
PEER_DEFER_EXPIRATION: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_PROPERTY_FLAGS = 4
PEER_GROUP_STATUS = Int32
PEER_GROUP_STATUS_LISTENING: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_STATUS = 1
PEER_GROUP_STATUS_HAS_CONNECTIONS: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_STATUS = 2
class PEER_INVITATION(Structure):
    applicationId: Guid
    applicationData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
    pwzMessage: win32more.Windows.Win32.Foundation.PWSTR
class PEER_INVITATION_INFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzCloudName: win32more.Windows.Win32.Foundation.PWSTR
    dwScope: UInt32
    dwCloudFlags: UInt32
    pwzGroupPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzIssuerPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzSubjectPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzGroupFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    pwzIssuerFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    pwzSubjectFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
    ftValidityStart: win32more.Windows.Win32.Foundation.FILETIME
    ftValidityEnd: win32more.Windows.Win32.Foundation.FILETIME
    cRoles: UInt32
    pRoles: POINTER(Guid)
    cClassifiers: UInt32
    ppwzClassifiers: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    pSubjectPublicKey: POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_PUBLIC_KEY_INFO)
    authScheme: win32more.Windows.Win32.NetworkManagement.P2P.PEER_GROUP_AUTHENTICATION_SCHEME
class PEER_INVITATION_RESPONSE(Structure):
    action: win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE
    pwzMessage: win32more.Windows.Win32.Foundation.PWSTR
    hrExtendedInfo: win32more.Windows.Win32.Foundation.HRESULT
PEER_INVITATION_RESPONSE_TYPE = Int32
PEER_INVITATION_RESPONSE_DECLINED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE = 0
PEER_INVITATION_RESPONSE_ACCEPTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE = 1
PEER_INVITATION_RESPONSE_EXPIRED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE = 2
PEER_INVITATION_RESPONSE_ERROR: win32more.Windows.Win32.NetworkManagement.P2P.PEER_INVITATION_RESPONSE_TYPE = 3
class PEER_MEMBER(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    pwzIdentity: win32more.Windows.Win32.Foundation.PWSTR
    pwzAttributes: win32more.Windows.Win32.Foundation.PWSTR
    ullNodeId: UInt64
    cAddresses: UInt32
    pAddresses: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS)
    pCredentialInfo: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_CREDENTIAL_INFO)
PEER_MEMBER_CHANGE_TYPE = Int32
PEER_MEMBER_CONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE = 1
PEER_MEMBER_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE = 2
PEER_MEMBER_UPDATED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE = 3
PEER_MEMBER_JOINED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE = 4
PEER_MEMBER_LEFT: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_CHANGE_TYPE = 5
PEER_MEMBER_FLAGS = Int32
PEER_MEMBER_PRESENT: win32more.Windows.Win32.NetworkManagement.P2P.PEER_MEMBER_FLAGS = 1
class PEER_NAME_PAIR(Structure):
    dwSize: UInt32
    pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR
    pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
PEER_NODE_CHANGE_TYPE = Int32
PEER_NODE_CHANGE_CONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE = 1
PEER_NODE_CHANGE_DISCONNECTED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE = 2
PEER_NODE_CHANGE_UPDATED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_NODE_CHANGE_TYPE = 3
class PEER_NODE_INFO(Structure):
    dwSize: UInt32
    ullNodeId: UInt64
    pwzPeerId: win32more.Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    pAddresses: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_ADDRESS)
    pwzAttributes: win32more.Windows.Win32.Foundation.PWSTR
class PEER_OBJECT(Structure):
    id: Guid
    data: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
    dwPublicationScope: UInt32
class PEER_PEOPLE_NEAR_ME(Structure):
    pwzNickName: win32more.Windows.Win32.Foundation.PWSTR
    endpoint: win32more.Windows.Win32.NetworkManagement.P2P.PEER_ENDPOINT
    id: Guid
class PEER_PNRP_CLOUD_INFO(Structure):
    pwzCloudName: win32more.Windows.Win32.Foundation.PWSTR
    dwScope: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE
    dwScopeId: UInt32
class PEER_PNRP_ENDPOINT_INFO(Structure):
    pwzPeerName: win32more.Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR))
    pwzComment: win32more.Windows.Win32.Foundation.PWSTR
    payload: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_PNRP_REGISTRATION_INFO(Structure):
    pwzCloudName: win32more.Windows.Win32.Foundation.PWSTR
    pwzPublishingIdentity: win32more.Windows.Win32.Foundation.PWSTR
    cAddresses: UInt32
    ppAddresses: POINTER(POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR))
    wPort: UInt16
    pwzComment: win32more.Windows.Win32.Foundation.PWSTR
    payload: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
class PEER_PRESENCE_INFO(Structure):
    status: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS
    pwzDescriptiveText: win32more.Windows.Win32.Foundation.PWSTR
PEER_PRESENCE_STATUS = Int32
PEER_PRESENCE_OFFLINE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 0
PEER_PRESENCE_OUT_TO_LUNCH: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 1
PEER_PRESENCE_AWAY: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 2
PEER_PRESENCE_BE_RIGHT_BACK: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 3
PEER_PRESENCE_IDLE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 4
PEER_PRESENCE_BUSY: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 5
PEER_PRESENCE_ON_THE_PHONE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 6
PEER_PRESENCE_ONLINE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PRESENCE_STATUS = 7
PEER_PUBLICATION_SCOPE = Int32
PEER_PUBLICATION_SCOPE_NONE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PUBLICATION_SCOPE = 0
PEER_PUBLICATION_SCOPE_NEAR_ME: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PUBLICATION_SCOPE = 1
PEER_PUBLICATION_SCOPE_INTERNET: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PUBLICATION_SCOPE = 2
PEER_PUBLICATION_SCOPE_ALL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_PUBLICATION_SCOPE = 3
class PEER_RECORD(Structure):
    dwSize: UInt32
    type: Guid
    id: Guid
    dwVersion: UInt32
    dwFlags: UInt32
    pwzCreatorId: win32more.Windows.Win32.Foundation.PWSTR
    pwzModifiedById: win32more.Windows.Win32.Foundation.PWSTR
    pwzAttributes: win32more.Windows.Win32.Foundation.PWSTR
    ftCreation: win32more.Windows.Win32.Foundation.FILETIME
    ftExpiration: win32more.Windows.Win32.Foundation.FILETIME
    ftLastModified: win32more.Windows.Win32.Foundation.FILETIME
    securityData: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
    data: win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA
PEER_RECORD_CHANGE_TYPE = Int32
PEER_RECORD_ADDED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE = 1
PEER_RECORD_UPDATED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE = 2
PEER_RECORD_DELETED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE = 3
PEER_RECORD_EXPIRED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE = 4
PEER_RECORD_FLAGS = Int32
PEER_RECORD_FLAG_AUTOREFRESH: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_FLAGS = 1
PEER_RECORD_FLAG_DELETED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_FLAGS = 2
class PEER_SECURITY_INTERFACE(Structure):
    dwSize: UInt32
    pwzSspFilename: win32more.Windows.Win32.Foundation.PWSTR
    pwzPackageName: win32more.Windows.Win32.Foundation.PWSTR
    cbSecurityInfo: UInt32
    pbSecurityInfo: POINTER(Byte)
    pvContext: VoidPtr
    pfnValidateRecord: win32more.Windows.Win32.NetworkManagement.P2P.PFNPEER_VALIDATE_RECORD
    pfnSecureRecord: win32more.Windows.Win32.NetworkManagement.P2P.PFNPEER_SECURE_RECORD
    pfnFreeSecurityData: win32more.Windows.Win32.NetworkManagement.P2P.PFNPEER_FREE_SECURITY_DATA
    pfnAuthFailed: win32more.Windows.Win32.NetworkManagement.P2P.PFNPEER_ON_PASSWORD_AUTH_FAILED
PEER_SIGNIN_FLAGS = Int32
PEER_SIGNIN_NONE: win32more.Windows.Win32.NetworkManagement.P2P.PEER_SIGNIN_FLAGS = 0
PEER_SIGNIN_NEAR_ME: win32more.Windows.Win32.NetworkManagement.P2P.PEER_SIGNIN_FLAGS = 1
PEER_SIGNIN_INTERNET: win32more.Windows.Win32.NetworkManagement.P2P.PEER_SIGNIN_FLAGS = 2
PEER_SIGNIN_ALL: win32more.Windows.Win32.NetworkManagement.P2P.PEER_SIGNIN_FLAGS = 3
class PEER_VERSION_DATA(Structure):
    wVersion: UInt16
    wHighestVersion: UInt16
PEER_WATCH_PERMISSION = Int32
PEER_WATCH_BLOCKED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_WATCH_PERMISSION = 0
PEER_WATCH_ALLOWED: win32more.Windows.Win32.NetworkManagement.P2P.PEER_WATCH_PERMISSION = 1
@winfunctype_pointer
def PFNPEER_FREE_SECURITY_DATA(hGraph: VoidPtr, pvContext: VoidPtr, pSecurityData: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_ON_PASSWORD_AUTH_FAILED(hGraph: VoidPtr, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_SECURE_RECORD(hGraph: VoidPtr, pvContext: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD), changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE, ppSecurityData: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_DATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNPEER_VALIDATE_RECORD(hGraph: VoidPtr, pvContext: VoidPtr, pRecord: POINTER(win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD), changeType: win32more.Windows.Win32.NetworkManagement.P2P.PEER_RECORD_CHANGE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class PNRPCLOUDINFO(Structure):
    dwSize: UInt32
    Cloud: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_ID
    enCloudState: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE
    enCloudFlags: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS
class PNRPINFO_V1(Structure):
    dwSize: UInt32
    lpwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    enNameState: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
class PNRPINFO_V2(Structure):
    dwSize: UInt32
    lpwszIdentity: win32more.Windows.Win32.Foundation.PWSTR
    nMaxResolve: UInt32
    dwTimeout: UInt32
    dwLifetime: UInt32
    enResolveCriteria: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA
    dwFlags: UInt32
    saHint: win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS
    enNameState: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE
    enExtendedPayloadType: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        blobPayload: win32more.Windows.Win32.System.Com.BLOB
        pwszPayload: win32more.Windows.Win32.Foundation.PWSTR
PNRP_CLOUD_FLAGS = Int32
PNRP_CLOUD_NO_FLAGS: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS = 0
PNRP_CLOUD_NAME_LOCAL: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS = 1
PNRP_CLOUD_RESOLVE_ONLY: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS = 2
PNRP_CLOUD_FULL_PARTICIPANT: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_FLAGS = 4
class PNRP_CLOUD_ID(Structure):
    AddressFamily: Int32
    Scope: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE
    ScopeId: UInt32
PNRP_CLOUD_STATE = Int32
PNRP_CLOUD_STATE_VIRTUAL: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 0
PNRP_CLOUD_STATE_SYNCHRONISING: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 1
PNRP_CLOUD_STATE_ACTIVE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 2
PNRP_CLOUD_STATE_DEAD: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 3
PNRP_CLOUD_STATE_DISABLED: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 4
PNRP_CLOUD_STATE_NO_NET: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 5
PNRP_CLOUD_STATE_ALONE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_CLOUD_STATE = 6
PNRP_EXTENDED_PAYLOAD_TYPE = Int32
PNRP_EXTENDED_PAYLOAD_TYPE_NONE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE = 0
PNRP_EXTENDED_PAYLOAD_TYPE_BINARY: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE = 1
PNRP_EXTENDED_PAYLOAD_TYPE_STRING: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_EXTENDED_PAYLOAD_TYPE = 2
PNRP_REGISTERED_ID_STATE = Int32
PNRP_REGISTERED_ID_STATE_OK: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE = 1
PNRP_REGISTERED_ID_STATE_PROBLEM: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_REGISTERED_ID_STATE = 2
PNRP_RESOLVE_CRITERIA = Int32
PNRP_RESOLVE_CRITERIA_DEFAULT: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 0
PNRP_RESOLVE_CRITERIA_REMOTE_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 1
PNRP_RESOLVE_CRITERIA_NEAREST_REMOTE_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 2
PNRP_RESOLVE_CRITERIA_NON_CURRENT_PROCESS_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 3
PNRP_RESOLVE_CRITERIA_NEAREST_NON_CURRENT_PROCESS_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 4
PNRP_RESOLVE_CRITERIA_ANY_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 5
PNRP_RESOLVE_CRITERIA_NEAREST_PEER_NAME: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_RESOLVE_CRITERIA = 6
PNRP_SCOPE = Int32
PNRP_SCOPE_ANY: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE = 0
PNRP_GLOBAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE = 1
PNRP_SITE_LOCAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE = 2
PNRP_LINK_LOCAL_SCOPE: win32more.Windows.Win32.NetworkManagement.P2P.PNRP_SCOPE = 3


make_ready(__name__)
