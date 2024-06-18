from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.DeploymentServices
import win32more.Windows.Win32.System.Registry
WDS_CLI_TRANSFER_ASYNCHRONOUS: UInt32 = 1
WDS_CLI_NO_SPARSE_FILE: UInt32 = 2
PXE_DHCP_SERVER_PORT: UInt32 = 67
PXE_DHCP_CLIENT_PORT: UInt32 = 68
PXE_SERVER_PORT: UInt32 = 4011
PXE_DHCPV6_SERVER_PORT: UInt32 = 547
PXE_DHCPV6_CLIENT_PORT: UInt32 = 546
PXE_DHCP_FILE_SIZE: UInt32 = 128
PXE_DHCP_SERVER_SIZE: UInt32 = 64
PXE_DHCP_HWAADR_SIZE: UInt32 = 16
PXE_DHCP_MAGIC_COOKIE_SIZE: UInt32 = 4
PXE_REG_INDEX_TOP: UInt32 = 0
PXE_REG_INDEX_BOTTOM: UInt32 = 4294967295
PXE_CALLBACK_RECV_REQUEST: UInt32 = 0
PXE_CALLBACK_SHUTDOWN: UInt32 = 1
PXE_CALLBACK_SERVICE_CONTROL: UInt32 = 2
PXE_CALLBACK_MAX: UInt32 = 3
PXE_GSI_TRACE_ENABLED: UInt32 = 1
PXE_GSI_SERVER_DUID: UInt32 = 2
PXE_MAX_ADDRESS: UInt32 = 16
PXE_ADDR_BROADCAST: UInt32 = 1
PXE_ADDR_USE_PORT: UInt32 = 2
PXE_ADDR_USE_ADDR: UInt32 = 4
PXE_ADDR_USE_DHCP_RULES: UInt32 = 8
PXE_DHCPV6_RELAY_HOP_COUNT_LIMIT: UInt32 = 32
PXE_BA_NBP: UInt32 = 1
PXE_BA_CUSTOM: UInt32 = 2
PXE_BA_IGNORE: UInt32 = 3
PXE_BA_REJECTED: UInt32 = 4
PXE_TRACE_VERBOSE: UInt32 = 65536
PXE_TRACE_INFO: UInt32 = 131072
PXE_TRACE_WARNING: UInt32 = 262144
PXE_TRACE_ERROR: UInt32 = 524288
PXE_TRACE_FATAL: UInt32 = 1048576
PXE_PROV_ATTR_FILTER: UInt32 = 0
PXE_PROV_ATTR_FILTER_IPV6: UInt32 = 1
PXE_PROV_ATTR_IPV6_CAPABLE: UInt32 = 2
PXE_PROV_FILTER_ALL: UInt32 = 0
PXE_PROV_FILTER_DHCP_ONLY: UInt32 = 1
PXE_PROV_FILTER_PXE_ONLY: UInt32 = 2
MC_SERVER_CURRENT_VERSION: UInt32 = 1
TRANSPORTPROVIDER_CURRENT_VERSION: UInt32 = 1
WDS_MC_TRACE_VERBOSE: UInt32 = 65536
WDS_MC_TRACE_INFO: UInt32 = 131072
WDS_MC_TRACE_WARNING: UInt32 = 262144
WDS_MC_TRACE_ERROR: UInt32 = 524288
WDS_MC_TRACE_FATAL: UInt32 = 1048576
WDS_TRANSPORTCLIENT_CURRENT_API_VERSION: UInt32 = 1
WDS_TRANSPORTCLIENT_PROTOCOL_MULTICAST: UInt32 = 1
WDS_TRANSPORTCLIENT_NO_CACHE: UInt32 = 0
WDS_TRANSPORTCLIENT_STATUS_IN_PROGRESS: UInt32 = 1
WDS_TRANSPORTCLIENT_STATUS_SUCCESS: UInt32 = 2
WDS_TRANSPORTCLIENT_STATUS_FAILURE: UInt32 = 3
WDSTRANSPORT_RESOURCE_UTILIZATION_UNKNOWN: UInt32 = 255
WDSBP_PK_TYPE_DHCP: UInt32 = 1
WDSBP_PK_TYPE_WDSNBP: UInt32 = 2
WDSBP_PK_TYPE_BCD: UInt32 = 4
WDSBP_PK_TYPE_DHCPV6: UInt32 = 8
WDSBP_OPT_TYPE_NONE: UInt32 = 0
WDSBP_OPT_TYPE_BYTE: UInt32 = 1
WDSBP_OPT_TYPE_USHORT: UInt32 = 2
WDSBP_OPT_TYPE_ULONG: UInt32 = 3
WDSBP_OPT_TYPE_WSTR: UInt32 = 4
WDSBP_OPT_TYPE_STR: UInt32 = 5
WDSBP_OPT_TYPE_IP4: UInt32 = 6
WDSBP_OPT_TYPE_IP6: UInt32 = 7
WDSBP_OPTVAL_ACTION_APPROVAL: UInt32 = 1
WDSBP_OPTVAL_ACTION_REFERRAL: UInt32 = 3
WDSBP_OPTVAL_ACTION_ABORT: UInt32 = 5
WDSBP_OPTVAL_PXE_PROMPT_OPTIN: UInt32 = 1
WDSBP_OPTVAL_PXE_PROMPT_NOPROMPT: UInt32 = 2
WDSBP_OPTVAL_PXE_PROMPT_OPTOUT: UInt32 = 3
WDSBP_OPTVAL_NBP_VER_7: UInt32 = 1792
WDSBP_OPTVAL_NBP_VER_8: UInt32 = 2048
FACILITY_WDSMCSERVER: UInt32 = 289
FACILITY_WDSMCCLIENT: UInt32 = 290
WDSMCSERVER_CATEGORY: win32more.Windows.Win32.Foundation.HRESULT = 1
WDSMCCLIENT_CATEGORY: win32more.Windows.Win32.Foundation.HRESULT = 2
WDSMCS_E_SESSION_SHUTDOWN_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1054801664
WDSMCS_E_REQCALLBACKS_NOT_REG: win32more.Windows.Win32.Foundation.HRESULT = -1054801663
WDSMCS_E_INCOMPATIBLE_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -1054801662
WDSMCS_E_CONTENT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1054801661
WDSMCS_E_CLIENT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1054801660
WDSMCS_E_NAMESPACE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1054801659
WDSMCS_E_CONTENT_PROVIDER_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1054801658
WDSMCS_E_NAMESPACE_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -1054801657
WDSMCS_E_NAMESPACE_SHUTDOWN_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1054801656
WDSMCS_E_NAMESPACE_ALREADY_STARTED: win32more.Windows.Win32.Foundation.HRESULT = -1054801655
WDSMCS_E_NS_START_FAILED_NO_CLIENTS: win32more.Windows.Win32.Foundation.HRESULT = -1054801654
WDSMCS_E_START_TIME_IN_PAST: win32more.Windows.Win32.Foundation.HRESULT = -1054801653
WDSMCS_E_PACKET_NOT_HASHED: win32more.Windows.Win32.Foundation.HRESULT = -1054801652
WDSMCS_E_PACKET_NOT_SIGNED: win32more.Windows.Win32.Foundation.HRESULT = -1054801651
WDSMCS_E_PACKET_HAS_SECURITY: win32more.Windows.Win32.Foundation.HRESULT = -1054801650
WDSMCS_E_PACKET_NOT_CHECKSUMED: win32more.Windows.Win32.Foundation.HRESULT = -1054801649
WDSMCS_E_CLIENT_DOESNOT_SUPPORT_SECURITY_MODE: win32more.Windows.Win32.Foundation.HRESULT = -1054801648
EVT_WDSMCS_S_PARAMETERS_READ: win32more.Windows.Win32.Foundation.HRESULT = 1092682240
EVT_WDSMCS_E_PARAMETERS_READ_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801407
EVT_WDSMCS_E_DUPLICATE_MULTICAST_ADDR: win32more.Windows.Win32.Foundation.HRESULT = -1054801406
EVT_WDSMCS_E_NON_WDS_DUPLICATE_MULTICAST_ADDR: win32more.Windows.Win32.Foundation.HRESULT = -1054801405
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801328
EVT_WDSMCS_E_CP_INIT_FUNC_MISSING: win32more.Windows.Win32.Foundation.HRESULT = -1054801327
EVT_WDSMCS_E_CP_INIT_FUNC_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801326
EVT_WDSMCS_E_CP_INCOMPATIBLE_SERVER_VERSION: win32more.Windows.Win32.Foundation.HRESULT = -1054801325
EVT_WDSMCS_E_CP_CALLBACKS_NOT_REG: win32more.Windows.Win32.Foundation.HRESULT = -1054801324
EVT_WDSMCS_E_CP_SHUTDOWN_FUNC_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801323
EVT_WDSMCS_E_CP_MEMORY_LEAK: win32more.Windows.Win32.Foundation.HRESULT = -1054801322
EVT_WDSMCS_E_CP_OPEN_INSTANCE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801321
EVT_WDSMCS_E_CP_CLOSE_INSTANCE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801320
EVT_WDSMCS_E_CP_OPEN_CONTENT_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1054801319
EVT_WDSMCS_W_CP_DLL_LOAD_FAILED_NOT_CRITICAL: win32more.Windows.Win32.Foundation.HRESULT = -2128543142
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED_CRITICAL: win32more.Windows.Win32.Foundation.HRESULT = -1054801317
EVT_WDSMCS_E_NSREG_START_TIME_IN_PAST: win32more.Windows.Win32.Foundation.HRESULT = -1054801152
EVT_WDSMCS_E_NSREG_CONTENT_PROVIDER_NOT_REG: win32more.Windows.Win32.Foundation.HRESULT = -1054801151
EVT_WDSMCS_E_NSREG_NAMESPACE_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -1054801150
EVT_WDSMCS_E_NSREG_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1054801149
WDSTPC_E_CALLBACKS_NOT_REG: win32more.Windows.Win32.Foundation.HRESULT = -1054735616
WDSTPC_E_ALREADY_COMPLETED: win32more.Windows.Win32.Foundation.HRESULT = -1054735615
WDSTPC_E_ALREADY_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1054735614
WDSTPC_E_UNKNOWN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -1054735613
WDSTPC_E_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -1054735612
WDSTPC_E_KICKED_POLICY_NOT_MET: win32more.Windows.Win32.Foundation.HRESULT = -1054735611
WDSTPC_E_KICKED_FALLBACK: win32more.Windows.Win32.Foundation.HRESULT = -1054735610
WDSTPC_E_KICKED_FAIL: win32more.Windows.Win32.Foundation.HRESULT = -1054735609
WDSTPC_E_KICKED_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -1054735608
WDSTPC_E_MULTISTREAM_NOT_ENABLED: win32more.Windows.Win32.Foundation.HRESULT = -1054735607
WDSTPC_E_ALREADY_IN_LOWEST_SESSION: win32more.Windows.Win32.Foundation.HRESULT = -1054735606
WDSTPC_E_CLIENT_DEMOTE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1054735605
WDSTPC_E_NO_IP4_INTERFACE: win32more.Windows.Win32.Foundation.HRESULT = -1054735604
WDSTPTC_E_WIM_APPLY_REQUIRES_REFERENCE_IMAGE: win32more.Windows.Win32.Foundation.HRESULT = -1054735603
FACILITY_WDSTPTMGMT: UInt32 = 272
WDSTPTMGMT_CATEGORY: win32more.Windows.Win32.Foundation.HRESULT = 1
WDSTPTMGMT_E_INVALID_PROPERTY: win32more.Windows.Win32.Foundation.HRESULT = -1055915776
WDSTPTMGMT_E_INVALID_OPERATION: win32more.Windows.Win32.Foundation.HRESULT = -1055915775
WDSTPTMGMT_E_INVALID_CLASS: win32more.Windows.Win32.Foundation.HRESULT = -1055915774
WDSTPTMGMT_E_CONTENT_PROVIDER_ALREADY_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -1055915773
WDSTPTMGMT_E_CONTENT_PROVIDER_NOT_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -1055915772
WDSTPTMGMT_E_INVALID_CONTENT_PROVIDER_NAME: win32more.Windows.Win32.Foundation.HRESULT = -1055915771
WDSTPTMGMT_E_TRANSPORT_SERVER_ROLE_NOT_CONFIGURED: win32more.Windows.Win32.Foundation.HRESULT = -1055915770
WDSTPTMGMT_E_NAMESPACE_ALREADY_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -1055915769
WDSTPTMGMT_E_NAMESPACE_NOT_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -1055915768
WDSTPTMGMT_E_CANNOT_REINITIALIZE_OBJECT: win32more.Windows.Win32.Foundation.HRESULT = -1055915767
WDSTPTMGMT_E_INVALID_NAMESPACE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -1055915766
WDSTPTMGMT_E_INVALID_NAMESPACE_DATA: win32more.Windows.Win32.Foundation.HRESULT = -1055915765
WDSTPTMGMT_E_NAMESPACE_READ_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -1055915764
WDSTPTMGMT_E_INVALID_NAMESPACE_START_TIME: win32more.Windows.Win32.Foundation.HRESULT = -1055915763
WDSTPTMGMT_E_INVALID_DIAGNOSTICS_COMPONENTS: win32more.Windows.Win32.Foundation.HRESULT = -1055915762
WDSTPTMGMT_E_CANNOT_REFRESH_DIRTY_OBJECT: win32more.Windows.Win32.Foundation.HRESULT = -1055915761
WDSTPTMGMT_E_INVALID_SERVICE_IP_ADDRESS_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -1055915760
WDSTPTMGMT_E_INVALID_SERVICE_PORT_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -1055915759
WDSTPTMGMT_E_INVALID_NAMESPACE_START_PARAMETERS: win32more.Windows.Win32.Foundation.HRESULT = -1055915758
WDSTPTMGMT_E_TRANSPORT_SERVER_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -1055915757
WDSTPTMGMT_E_NAMESPACE_NOT_ON_SERVER: win32more.Windows.Win32.Foundation.HRESULT = -1055915756
WDSTPTMGMT_E_NAMESPACE_REMOVED_FROM_SERVER: win32more.Windows.Win32.Foundation.HRESULT = -1055915755
WDSTPTMGMT_E_INVALID_IP_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -1055915754
WDSTPTMGMT_E_INVALID_IPV4_MULTICAST_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -1055915753
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -1055915752
WDSTPTMGMT_E_IPV6_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915751
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS_SOURCE: win32more.Windows.Win32.Foundation.HRESULT = -1055915750
WDSTPTMGMT_E_INVALID_MULTISTREAM_STREAM_COUNT: win32more.Windows.Win32.Foundation.HRESULT = -1055915749
WDSTPTMGMT_E_INVALID_AUTO_DISCONNECT_THRESHOLD: win32more.Windows.Win32.Foundation.HRESULT = -1055915748
WDSTPTMGMT_E_MULTICAST_SESSION_POLICY_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915747
WDSTPTMGMT_E_INVALID_SLOW_CLIENT_HANDLING_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -1055915746
WDSTPTMGMT_E_NETWORK_PROFILES_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915745
WDSTPTMGMT_E_UDP_PORT_POLICY_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915744
WDSTPTMGMT_E_TFTP_MAX_BLOCKSIZE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915743
WDSTPTMGMT_E_TFTP_VAR_WINDOW_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1055915742
WDSTPTMGMT_E_INVALID_TFTP_MAX_BLOCKSIZE: win32more.Windows.Win32.Foundation.HRESULT = -1055915741
WdsCliFlagEnumFilterVersion: Int32 = 1
WdsCliFlagEnumFilterFirmware: Int32 = 2
WDS_LOG_TYPE_CLIENT_ERROR: Int32 = 1
WDS_LOG_TYPE_CLIENT_STARTED: Int32 = 2
WDS_LOG_TYPE_CLIENT_FINISHED: Int32 = 3
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED: Int32 = 4
WDS_LOG_TYPE_CLIENT_APPLY_STARTED: Int32 = 5
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED: Int32 = 6
WDS_LOG_TYPE_CLIENT_GENERIC_MESSAGE: Int32 = 7
WDS_LOG_TYPE_CLIENT_UNATTEND_MODE: Int32 = 8
WDS_LOG_TYPE_CLIENT_TRANSFER_START: Int32 = 9
WDS_LOG_TYPE_CLIENT_TRANSFER_END: Int32 = 10
WDS_LOG_TYPE_CLIENT_TRANSFER_DOWNGRADE: Int32 = 11
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR: Int32 = 12
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_START: Int32 = 13
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_END: Int32 = 14
WDS_LOG_TYPE_CLIENT_APPLY_STARTED_2: Int32 = 15
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED_2: Int32 = 16
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR_2: Int32 = 17
WDS_LOG_TYPE_CLIENT_DRIVER_PACKAGE_NOT_ACCESSIBLE: Int32 = 18
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_START: Int32 = 19
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_END: Int32 = 20
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_FAILURE: Int32 = 21
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED2: Int32 = 22
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED3: Int32 = 23
WDS_LOG_TYPE_CLIENT_MAX_CODE: Int32 = 24
WDS_LOG_LEVEL_DISABLED: Int32 = 0
WDS_LOG_LEVEL_ERROR: Int32 = 1
WDS_LOG_LEVEL_WARNING: Int32 = 2
WDS_LOG_LEVEL_INFO: Int32 = 3
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliClose(Handle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliRegisterTrace(pfn: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsCliTraceFunction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFreeStringArray(ppwszArray: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindFirstImage(hSession: win32more.Windows.Win32.Foundation.HANDLE, phFindHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindNextImage(Handle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetEnumerationFlags(Handle: win32more.Windows.Win32.Foundation.HANDLE, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromFindHandle(FindHandle: win32more.Windows.Win32.Foundation.HANDLE, phImageHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromTransferHandle(hTransfer: win32more.Windows.Win32.Foundation.HANDLE, phImageHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCreateSession(pwszServer: win32more.Windows.Win32.Foundation.PWSTR, pCred: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_CRED), phSession: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliAuthorizeSession(hSession: win32more.Windows.Win32.Foundation.HANDLE, pCred: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_CRED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliInitializeLog(hSession: win32more.Windows.Win32.Foundation.HANDLE, ulClientArchitecture: win32more.Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE, pwszClientId: win32more.Windows.Win32.Foundation.PWSTR, pwszClientAddress: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('WDSCLIENTAPI.dll', variadic=True)
def WdsCliLog(hSession: win32more.Windows.Win32.Foundation.HANDLE, ulLogLevel: UInt32, ulMessageCode: UInt32, *__arglist) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageName(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageDescription(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageType(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pImageType: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageFiles(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pppwszFiles: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguage(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguages(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pppszValues: POINTER(POINTER(POINTER(SByte))), pdwNumValues: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageVersion(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImagePath(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageIndex(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pdwValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageArchitecture(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pdwValue: POINTER(win32more.Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLastModifiedTime(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppSysTimeValue: POINTER(POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageSize(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHalName(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageGroup(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageNamespace(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageParameter(hIfh: win32more.Windows.Win32.Foundation.HANDLE, ParamType: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE, pResponse: VoidPtr, uResponseLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetTransferSize(hIfh: win32more.Windows.Win32.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliSetTransferBufferSize(ulSizeInBytes: UInt32) -> Void: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferImage(hImage: win32more.Windows.Win32.Foundation.HANDLE, pwszLocalPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: VoidPtr, phTransfer: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferFile(pwszServer: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespace: win32more.Windows.Win32.Foundation.PWSTR, pwszRemoteFilePath: win32more.Windows.Win32.Foundation.PWSTR, pwszLocalFilePath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: VoidPtr, phTransfer: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCancelTransfer(hTransfer: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliWaitForTransfer(hTransfer: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackages(hImage: win32more.Windows.Win32.Foundation.HANDLE, ppwszServerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackagesEx(hSession: win32more.Windows.Win32.Foundation.HANDLE, pwszMachineInfo: win32more.Windows.Win32.Foundation.PWSTR, ppwszServerName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetDriverQueryXml(pwszWinDirPath: win32more.Windows.Win32.Foundation.PWSTR, ppwszDriverQuery: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSPXE.dll')
def PxeProviderRegister(pszProviderName: win32more.Windows.Win32.Foundation.PWSTR, pszModulePath: win32more.Windows.Win32.Foundation.PWSTR, Index: UInt32, bIsCritical: win32more.Windows.Win32.Foundation.BOOL, phProviderKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderUnRegister(pszProviderName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderQueryIndex(pszProviderName: win32more.Windows.Win32.Foundation.PWSTR, puIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumFirst(phEnum: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumNext(hEnum: win32more.Windows.Win32.Foundation.HANDLE, ppProvider: POINTER(POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_PROVIDER))) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumClose(hEnum: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderFreeInfo(pProvider: POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_PROVIDER)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeRegisterCallback(hProvider: win32more.Windows.Win32.Foundation.HANDLE, CallbackType: UInt32, pCallbackFunction: VoidPtr, pContext: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeSendReply(hClientRequest: win32more.Windows.Win32.Foundation.HANDLE, pPacket: VoidPtr, uPacketLen: UInt32, pAddress: POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_ADDRESS)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeAsyncRecvDone(hClientRequest: win32more.Windows.Win32.Foundation.HANDLE, Action: UInt32) -> UInt32: ...
@cfunctype('WDSPXE.dll', variadic=True)
def PxeTrace(hProvider: win32more.Windows.Win32.Foundation.HANDLE, Severity: UInt32, pszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeTraceV(hProvider: win32more.Windows.Win32.Foundation.HANDLE, Severity: UInt32, pszFormat: win32more.Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxePacketAllocate(hProvider: win32more.Windows.Win32.Foundation.HANDLE, hClientRequest: win32more.Windows.Win32.Foundation.HANDLE, uSize: UInt32) -> VoidPtr: ...
@winfunctype('WDSPXE.dll')
def PxePacketFree(hProvider: win32more.Windows.Win32.Foundation.HANDLE, hClientRequest: win32more.Windows.Win32.Foundation.HANDLE, pPacket: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderSetAttribute(hProvider: win32more.Windows.Win32.Foundation.HANDLE, Attribute: UInt32, pParameterBuffer: VoidPtr, uParamLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpInitialize(pRecvPacket: VoidPtr, uRecvPacketLen: UInt32, pReplyPacket: VoidPtr, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6Initialize(pRequest: VoidPtr, cbRequest: UInt32, pReply: VoidPtr, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOption(pReplyPacket: VoidPtr, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), bOption: Byte, bOptionLen: Byte, pValue: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOption(pReply: VoidPtr, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), wOptionType: UInt16, cbOption: UInt16, pOption: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOptionRaw(pReplyPacket: VoidPtr, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), uBufferLen: UInt16, pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOptionRaw(pReply: VoidPtr, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), cbBuffer: UInt16, pBuffer: VoidPtr) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpIsValid(pPacket: VoidPtr, uPacketLen: UInt32, bRequestPacket: win32more.Windows.Win32.Foundation.BOOL, pbPxeOptionPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6IsValid(pPacket: VoidPtr, uPacketLen: UInt32, bRequestPacket: win32more.Windows.Win32.Foundation.BOOL, pbPxeOptionPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetOptionValue(pPacket: VoidPtr, uPacketLen: UInt32, uInstance: UInt32, bOption: Byte, pbOptionLen: POINTER(Byte), ppOptionValue: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetOptionValue(pPacket: VoidPtr, uPacketLen: UInt32, uInstance: UInt32, wOption: UInt16, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetVendorOptionValue(pPacket: VoidPtr, uPacketLen: UInt32, bOption: Byte, uInstance: UInt32, pbOptionLen: POINTER(Byte), ppOptionValue: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetVendorOptionValue(pPacket: VoidPtr, uPacketLen: UInt32, dwEnterpriseNumber: UInt32, wOption: UInt16, uInstance: UInt32, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6ParseRelayForw(pRelayForwPacket: VoidPtr, uRelayForwPacketLen: UInt32, pRelayMessages: POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE), nRelayMessages: UInt32, pnRelayMessages: POINTER(UInt32), ppInnerPacket: POINTER(POINTER(Byte)), pcbInnerPacket: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6CreateRelayRepl(pRelayMessages: POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE), nRelayMessages: UInt32, pInnerPacket: POINTER(Byte), cbInnerPacket: UInt32, pReplyBuffer: VoidPtr, cbReplyBuffer: UInt32, pcbReplyBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfo(uInfoType: UInt32, pBuffer: VoidPtr, uBufferLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfoEx(uInfoType: UInt32, pBuffer: VoidPtr, uBufferLen: UInt32, puBufferUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerRegisterCallback(hProvider: win32more.Windows.Win32.Foundation.HANDLE, CallbackId: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID, pfnCallback: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerCompleteRead(hProvider: win32more.Windows.Win32.Foundation.HANDLE, ulBytesRead: UInt32, pvUserData: VoidPtr, hReadResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('WDSMC.dll', variadic=True)
def WdsTransportServerTrace(hProvider: win32more.Windows.Win32.Foundation.HANDLE, Severity: UInt32, pwszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerTraceV(hProvider: win32more.Windows.Win32.Foundation.HANDLE, Severity: UInt32, pwszFormat: win32more.Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerAllocateBuffer(hProvider: win32more.Windows.Win32.Foundation.HANDLE, ulBufferSize: UInt32) -> VoidPtr: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerFreeBuffer(hProvider: win32more.Windows.Win32.Foundation.HANDLE, pvBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitialize() -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitializeSession(pSessionRequest: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST), pCallerData: VoidPtr, hSessionKey: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientRegisterCallback(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, CallbackId: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID, pfnCallback: VoidPtr) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientStartSession(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCompleteReceive(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, ulSize: UInt32, pullOffset: POINTER(UInt64)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSession(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSessionEx(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, dwErrorCode: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientWaitForCompletion(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, uTimeout: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientQueryStatus(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, puStatus: POINTER(UInt32), puErrorCode: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCloseSession(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientAddRefBuffer(pvBuffer: VoidPtr) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientReleaseBuffer(pvBuffer: VoidPtr) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientShutdown() -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitialize(pPacket: VoidPtr, uPacketLen: UInt32, pbPacketType: POINTER(Byte), phHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitializev6(pPacket: VoidPtr, uPacketLen: UInt32, pbPacketType: POINTER(Byte), phHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpInitialize(bPacketType: Byte, phHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpCloseHandle(hHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpQueryOption(hHandle: win32more.Windows.Win32.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: VoidPtr, puBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpAddOption(hHandle: win32more.Windows.Win32.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: VoidPtr) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpGetOptionBuffer(hHandle: win32more.Windows.Win32.Foundation.HANDLE, uBufferLen: UInt32, pBuffer: VoidPtr, puBytes: POINTER(UInt32)) -> UInt32: ...
CPU_ARCHITECTURE = UInt32
CPU_ARCHITECTURE_AMD64: win32more.Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE = 9
CPU_ARCHITECTURE_IA64: win32more.Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE = 6
CPU_ARCHITECTURE_INTEL: win32more.Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE = 0
class IWdsTransportCacheable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{46ad894b-0bab-47dc-84b2-7b553f1d8f80}')
    @commethod(7)
    def get_Dirty(self, pbDirty: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Discard(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b5dbc93a-cabe-46ca-837f-3e44e93c6545}')
    @commethod(7)
    def get_Session(self, ppWdsTransportSession: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportSession)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MacAddress(self, pbszMacAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddress(self, pbszIpAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PercentCompletion(self, pulPercentCompletion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_JoinDuration(self, pulJoinDuration: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CpuUtilization(self, pulCpuUtilization: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MemoryUtilization(self, pulMemoryUtilization: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_NetworkUtilization(self, pulNetworkUtilization: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_UserIdentity(self, pbszUserIdentity: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Disconnect(self, DisconnectionType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b8ba4b1a-2ff4-43ab-996c-b2b10a91a6eb}')
    @commethod(7)
    def get_Count(self, pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, ulIndex: UInt32, ppVal: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{84cc4779-42dd-4792-891e-1321d6d74b44}')
    @commethod(7)
    def get_ServicePolicy(self, ppWdsTransportServicePolicy: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportServicePolicy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DiagnosticsPolicy(self, ppWdsTransportDiagnosticsPolicy: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportDiagnosticsPolicy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_WdsTransportServicesRunning(self, bRealtimeStatus: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pbServicesRunning: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableWdsTransportServices(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisableWdsTransportServices(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StartWdsTransportServices(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StopWdsTransportServices(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RestartWdsTransportServices(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def NotifyWdsTransportServices(self, ServiceNotification: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager2(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportConfigurationManager
    _iid_ = Guid('{d0d85caf-a153-4f1d-a9dd-96f431c50717}')
    @commethod(16)
    def get_MulticastSessionPolicy(self, ppWdsTransportMulticastSessionPolicy: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportMulticastSessionPolicy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportContent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d405d711-0296-4ab4-a860-ac7d32e65798}')
    @commethod(7)
    def get_Namespace(self, ppWdsTransportNamespace: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetrieveSessions(self, ppWdsTransportSessions: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportContentProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b9489f24-f219-4acf-aad7-265c7c08a6ae}')
    @commethod(7)
    def get_Name(self, pbszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Description(self, pbszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FilePath(self, pbszFilePath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InitializationRoutine(self, pbszInitializationRoutine: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportDiagnosticsPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    _iid_ = Guid('{13b33efc-7856-4f61-9a59-8de67b6b87b6}')
    @commethod(11)
    def get_Enabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enabled(self, bEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Components(self, pulComponents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Components(self, ulComponents: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5b0d35f5-1b13-4afd-b878-6526dc340b5d}')
    @commethod(7)
    def GetWdsTransportServer(self, bszServerName: win32more.Windows.Win32.Foundation.BSTR, ppWdsTransportServer: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportServer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportMulticastSessionPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    _iid_ = Guid('{4e5753cf-68ec-4504-a951-4a003266606b}')
    @commethod(11)
    def get_SlowClientHandling(self, pSlowClientHandling: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SlowClientHandling(self, SlowClientHandling: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AutoDisconnectThreshold(self, pulThreshold: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AutoDisconnectThreshold(self, ulThreshold: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MultistreamStreamCount(self, pulStreamCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MultistreamStreamCount(self, ulStreamCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SlowClientFallback(self, pbClientFallback: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SlowClientFallback(self, bClientFallback: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa561f57-fbef-4ed3-b056-127cb1b33b84}')
    @commethod(7)
    def get_Type(self, pType: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(self, bszName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FriendlyName(self, pbszFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_FriendlyName(self, bszFriendlyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(self, pbszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Description(self, bszDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ContentProvider(self, pbszContentProvider: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ContentProvider(self, bszContentProvider: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Configuration(self, pbszConfiguration: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Configuration(self, bszConfiguration: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Registered(self, pbRegistered: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Tombstoned(self, pbTombstoned: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TombstoneTime(self, pTombstoneTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_TransmissionStarted(self, pbTransmissionStarted: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Register(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Deregister(self, bTerminateSessions: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Clone(self, ppWdsTransportNamespaceClone: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RetrieveContents(self, ppWdsTransportContents: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceAutoCast(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace
    _iid_ = Guid('{ad931a72-c4bd-4c41-8fbc-59c9c748df9e}')
class IWdsTransportNamespaceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3e22d9f6-3777-4d98-83e1-f98696717ba3}')
    @commethod(7)
    def CreateNamespace(self, NamespaceType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE, bszNamespaceName: win32more.Windows.Win32.Foundation.BSTR, bszContentProvider: win32more.Windows.Win32.Foundation.BSTR, bszConfiguration: win32more.Windows.Win32.Foundation.BSTR, ppWdsTransportNamespace: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveNamespace(self, bszNamespaceName: win32more.Windows.Win32.Foundation.BSTR, ppWdsTransportNamespace: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RetrieveNamespaces(self, bszContentProvider: win32more.Windows.Win32.Foundation.BSTR, bszNamespaceName: win32more.Windows.Win32.Foundation.BSTR, bIncludeTombstones: win32more.Windows.Win32.Foundation.VARIANT_BOOL, ppWdsTransportNamespaces: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCast(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespace
    _iid_ = Guid('{3840cecf-d76c-416e-a4cc-31c741d2874b}')
    @commethod(28)
    def StartTransmission(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastAutoStart(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    _iid_ = Guid('{d606af3d-ea9c-4219-961e-7491d618d9b9}')
    @commethod(29)
    def get_MinimumClients(self, pulMinimumClients: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MinimumClients(self, ulMinimumClients: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_StartTime(self, pStartTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_StartTime(self, StartTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastManualStart(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    _iid_ = Guid('{013e6e4c-e6a7-4fb5-b7ff-d9f5da805c31}')
class IWdsTransportServer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{09ccd093-830d-4344-a30a-73ae8e8fca90}')
    @commethod(7)
    def get_Name(self, pbszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SetupManager(self, ppWdsTransportSetupManager: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportSetupManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ConfigurationManager(self, ppWdsTransportConfigurationManager: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportConfigurationManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NamespaceManager(self, ppWdsTransportNamespaceManager: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisconnectClient(self, ulClientId: UInt32, DisconnectionType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServer2(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportServer
    _iid_ = Guid('{256e999f-6df4-4538-81b9-857b9ab8fb47}')
    @commethod(12)
    def get_TftpManager(self, ppWdsTransportTftpManager: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportTftpManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServicePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    _iid_ = Guid('{b9468578-9f2b-48cc-b27a-a60799c2750c}')
    @commethod(11)
    def get_IpAddressSource(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pSourceType: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddressSource(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, SourceType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_StartIpAddress(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszStartIpAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_StartIpAddress(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszStartIpAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EndIpAddress(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszEndIpAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EndIpAddress(self, AddressType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszEndIpAddress: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_StartPort(self, pulStartPort: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_StartPort(self, ulStartPort: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EndPort(self, pulEndPort: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_EndPort(self, ulEndPort: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_NetworkProfile(self, pProfileType: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_NetworkProfile(self, ProfileType: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServicePolicy2(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportServicePolicy
    _iid_ = Guid('{65c19e5c-aa7e-4b91-8944-91e0e5572797}')
    @commethod(23)
    def get_UdpPortPolicy(self, pUdpPortPolicy: POINTER(win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_UdpPortPolicy(self, UdpPortPolicy: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_TftpMaximumBlockSize(self, pulTftpMaximumBlockSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_TftpMaximumBlockSize(self, ulTftpMaximumBlockSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_EnableTftpVariableWindowExtension(self, pbEnableTftpVariableWindowExtension: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_EnableTftpVariableWindowExtension(self, bEnableTftpVariableWindowExtension: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f4efea88-65b1-4f30-a4b9-2793987796fb}')
    @commethod(7)
    def get_Content(self, ppWdsTransportContent: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportContent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NetworkInterfaceName(self, pbszNetworkInterfaceName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkInterfaceAddress(self, pbszNetworkInterfaceAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TransferRate(self, pulTransferRate: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MasterClientId(self, pulMasterClientId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RetrieveClients(self, ppWdsTransportClients: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSetupManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f7238425-efa8-40a4-aef9-c98d969c0b75}')
    @commethod(7)
    def get_Version(self, pullVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InstalledFeatures(self, pulInstalledFeatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Protocols(self, pulProtocols: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterContentProvider(self, bszName: win32more.Windows.Win32.Foundation.BSTR, bszDescription: win32more.Windows.Win32.Foundation.BSTR, bszFilePath: win32more.Windows.Win32.Foundation.BSTR, bszInitializationRoutine: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeregisterContentProvider(self, bszName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSetupManager2(ComPtr):
    extends: win32more.Windows.Win32.System.DeploymentServices.IWdsTransportSetupManager
    _iid_ = Guid('{02be79da-7e9e-4366-8b6e-2aa9a91be47f}')
    @commethod(12)
    def get_TftpCapabilities(self, pulTftpCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ContentProviders(self, ppProviderCollection: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportTftpClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b022d3ae-884d-4d85-b146-53320e76ef62}')
    @commethod(7)
    def get_FileName(self, pbszFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IpAddress(self, pbszIpAddress: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Timeout(self, pulTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentFileOffset(self, pul64CurrentOffset: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FileSize(self, pul64FileSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_BlockSize(self, pulBlockSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_WindowSize(self, pulWindowSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportTftpManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1327a7c8-ae8a-4fb3-8150-136227c37e9a}')
    @commethod(7)
    def RetrieveTftpClients(self, ppWdsTransportTftpClients: POINTER(win32more.Windows.Win32.System.DeploymentServices.IWdsTransportCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PFN_WDS_CLI_CALLBACK_MESSAGE_ID = UInt32
WDS_CLI_MSG_START: win32more.Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 0
WDS_CLI_MSG_COMPLETE: win32more.Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 1
WDS_CLI_MSG_PROGRESS: win32more.Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 2
WDS_CLI_MSG_TEXT: win32more.Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 3
@winfunctype_pointer
def PFN_WdsCliCallback(dwMessageId: win32more.Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pvUserData: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFN_WdsCliTraceFunction(pwszFormat: win32more.Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveContents(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, pContents: VoidPtr, ulSize: UInt32, pullContentOffset: POINTER(UInt64)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveMetadata(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, pMetadata: VoidPtr, ulSize: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionComplete(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, dwError: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionNegotiate(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, pInfo: POINTER(win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO), hNegotiateKey: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStart(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, ullFileSize: POINTER(UInt64)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStartEx(hSessionKey: win32more.Windows.Win32.Foundation.HANDLE, pCallerData: VoidPtr, Info: POINTER(win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO)) -> Void: ...
class PXE_ADDRESS(Structure):
    uFlags: UInt32
    Anonymous: _Anonymous_e__Union
    uAddrLen: UInt32
    uPort: UInt16
    class _Anonymous_e__Union(Union):
        bAddress: Byte * 16
        uIpAddress: UInt32
class PXE_DHCPV6_MESSAGE(Structure):
    MessageType: Byte
    TransactionIDByte1: Byte
    TransactionIDByte2: Byte
    TransactionIDByte3: Byte
    Options: win32more.Windows.Win32.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_DHCPV6_MESSAGE_HEADER(Structure):
    MessageType: Byte
    Message: Byte * 1
    _pack_ = 1
class PXE_DHCPV6_NESTED_RELAY_MESSAGE(Structure):
    pRelayMessage: POINTER(win32more.Windows.Win32.System.DeploymentServices.PXE_DHCPV6_RELAY_MESSAGE)
    cbRelayMessage: UInt32
    pInterfaceIdOption: VoidPtr
    cbInterfaceIdOption: UInt16
class PXE_DHCPV6_OPTION(Structure):
    OptionCode: UInt16
    DataLength: UInt16
    Data: Byte * 1
    _pack_ = 1
class PXE_DHCPV6_RELAY_MESSAGE(Structure):
    MessageType: Byte
    HopCount: Byte
    LinkAddress: Byte * 16
    PeerAddress: Byte * 16
    Options: win32more.Windows.Win32.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_DHCP_MESSAGE(Structure):
    Operation: Byte
    HardwareAddressType: Byte
    HardwareAddressLength: Byte
    HopCount: Byte
    TransactionID: UInt32
    SecondsSinceBoot: UInt16
    Reserved: UInt16
    ClientIpAddress: UInt32
    YourIpAddress: UInt32
    BootstrapServerAddress: UInt32
    RelayAgentIpAddress: UInt32
    HardwareAddress: Byte * 16
    HostName: Byte * 64
    BootFileName: Byte * 128
    Anonymous: _Anonymous_e__Union
    Option: win32more.Windows.Win32.System.DeploymentServices.PXE_DHCP_OPTION
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        bMagicCookie: Byte * 4
        uMagicCookie: UInt32
        _pack_ = 1
class PXE_DHCP_OPTION(Structure):
    OptionType: Byte
    OptionLength: Byte
    OptionValue: Byte * 1
    _pack_ = 1
class PXE_PROVIDER(Structure):
    uSizeOfStruct: UInt32
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    pwszFilePath: win32more.Windows.Win32.Foundation.PWSTR
    bIsCritical: win32more.Windows.Win32.Foundation.BOOL
    uIndex: UInt32
TRANSPORTCLIENT_CALLBACK_ID = Int32
WDS_TRANSPORTCLIENT_SESSION_START: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 0
WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 1
WDS_TRANSPORTCLIENT_SESSION_COMPLETE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 2
WDS_TRANSPORTCLIENT_RECEIVE_METADATA: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 3
WDS_TRANSPORTCLIENT_SESSION_STARTEX: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 4
WDS_TRANSPORTCLIENT_SESSION_NEGOTIATE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 5
WDS_TRANSPORTCLIENT_MAX_CALLBACKS: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID = 6
class TRANSPORTCLIENT_SESSION_INFO(Structure):
    ulStructureLength: UInt32
    ullFileSize: UInt64
    ulBlockSize: UInt32
TRANSPORTPROVIDER_CALLBACK_ID = Int32
WDS_TRANSPORTPROVIDER_CREATE_INSTANCE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 0
WDS_TRANSPORTPROVIDER_COMPARE_CONTENT: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 1
WDS_TRANSPORTPROVIDER_OPEN_CONTENT: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 2
WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 3
WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 4
WDS_TRANSPORTPROVIDER_READ_CONTENT: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 5
WDS_TRANSPORTPROVIDER_CLOSE_CONTENT: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 6
WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 7
WDS_TRANSPORTPROVIDER_SHUTDOWN: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 8
WDS_TRANSPORTPROVIDER_DUMP_STATE: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 9
WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 10
WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 11
WDS_TRANSPORTPROVIDER_MAX_CALLBACKS: win32more.Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID = 12
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = Int32
WdsTptDiagnosticsComponentPxe: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 1
WdsTptDiagnosticsComponentTftp: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 2
WdsTptDiagnosticsComponentImageServer: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 4
WdsTptDiagnosticsComponentMulticast: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 8
WDSTRANSPORT_DISCONNECT_TYPE = Int32
WdsTptDisconnectUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE = 0
WdsTptDisconnectFallback: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE = 1
WdsTptDisconnectAbort: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE = 2
WDSTRANSPORT_FEATURE_FLAGS = Int32
WdsTptFeatureAdminPack: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_FEATURE_FLAGS = 1
WdsTptFeatureTransportServer: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_FEATURE_FLAGS = 2
WdsTptFeatureDeploymentServer: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_FEATURE_FLAGS = 4
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = Int32
WdsTptIpAddressSourceUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 0
WdsTptIpAddressSourceDhcp: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 1
WdsTptIpAddressSourceRange: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 2
WDSTRANSPORT_IP_ADDRESS_TYPE = Int32
WdsTptIpAddressUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE = 0
WdsTptIpAddressIpv4: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE = 1
WdsTptIpAddressIpv6: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE = 2
WDSTRANSPORT_NAMESPACE_TYPE = Int32
WdsTptNamespaceTypeUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE = 0
WdsTptNamespaceTypeAutoCast: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE = 1
WdsTptNamespaceTypeScheduledCastManualStart: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE = 2
WdsTptNamespaceTypeScheduledCastAutoStart: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE = Int32
WdsTptNetworkProfileUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE = 0
WdsTptNetworkProfileCustom: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE = 1
WdsTptNetworkProfile10Mbps: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE = 2
WdsTptNetworkProfile100Mbps: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE = 3
WdsTptNetworkProfile1Gbps: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE = 4
WDSTRANSPORT_PROTOCOL_FLAGS = Int32
WdsTptProtocolUnicast: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_PROTOCOL_FLAGS = 1
WdsTptProtocolMulticast: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_PROTOCOL_FLAGS = 2
WDSTRANSPORT_SERVICE_NOTIFICATION = Int32
WdsTptServiceNotifyUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION = 0
WdsTptServiceNotifyReadSettings: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = Int32
WdsTptSlowClientHandlingUnknown: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 0
WdsTptSlowClientHandlingNone: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 1
WdsTptSlowClientHandlingAutoDisconnect: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 2
WdsTptSlowClientHandlingMultistream: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 3
WDSTRANSPORT_TFTP_CAPABILITY = Int32
WdsTptTftpCapMaximumBlockSize: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_TFTP_CAPABILITY = 1
WdsTptTftpCapVariableWindow: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_TFTP_CAPABILITY = 2
WDSTRANSPORT_UDP_PORT_POLICY = Int32
WdsTptUdpPortPolicyDynamic: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY = 0
WdsTptUdpPortPolicyFixed: win32more.Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY = 1
class WDS_CLI_CRED(Structure):
    pwszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pwszDomain: win32more.Windows.Win32.Foundation.PWSTR
    pwszPassword: win32more.Windows.Win32.Foundation.PWSTR
WDS_CLI_FIRMWARE_TYPE = Int32
WDS_CLI_FIRMWARE_UNKNOWN: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_FIRMWARE_TYPE = 0
WDS_CLI_FIRMWARE_BIOS: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_FIRMWARE_TYPE = 1
WDS_CLI_FIRMWARE_EFI: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_FIRMWARE_TYPE = 2
WDS_CLI_IMAGE_PARAM_TYPE = Int32
WDS_CLI_IMAGE_PARAM_UNKNOWN: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE = 0
WDS_CLI_IMAGE_PARAM_SPARSE_FILE: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE = 1
WDS_CLI_IMAGE_PARAM_SUPPORTED_FIRMWARES: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE = 2
WDS_CLI_IMAGE_TYPE = Int32
WDS_CLI_IMAGE_TYPE_UNKNOWN: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE = 0
WDS_CLI_IMAGE_TYPE_WIM: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE = 1
WDS_CLI_IMAGE_TYPE_VHD: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE = 2
WDS_CLI_IMAGE_TYPE_VHDX: win32more.Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE = 3
class WDS_TRANSPORTCLIENT_CALLBACKS(Structure):
    SessionStart: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionStart
    SessionStartEx: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionStartEx
    ReceiveContents: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientReceiveContents
    ReceiveMetadata: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientReceiveMetadata
    SessionComplete: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionComplete
    SessionNegotiate: win32more.Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionNegotiate
class WDS_TRANSPORTCLIENT_REQUEST(Structure):
    ulLength: UInt32
    ulApiVersion: UInt32
    ulAuthLevel: win32more.Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL
    pwszServer: win32more.Windows.Win32.Foundation.PWSTR
    pwszNamespace: win32more.Windows.Win32.Foundation.PWSTR
    pwszObjectName: win32more.Windows.Win32.Foundation.PWSTR
    ulCacheSize: UInt32
    ulProtocol: UInt32
    pvProtocolData: VoidPtr
    ulProtocolDataLength: UInt32
WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = UInt32
WDS_TRANSPORTCLIENT_AUTH: win32more.Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 1
WDS_TRANSPORTCLIENT_NO_AUTH: win32more.Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 2
class WDS_TRANSPORTPROVIDER_INIT_PARAMS(Structure):
    ulLength: UInt32
    ulMcServerVersion: UInt32
    hRegistryKey: win32more.Windows.Win32.System.Registry.HKEY
    hProvider: win32more.Windows.Win32.Foundation.HANDLE
class WDS_TRANSPORTPROVIDER_SETTINGS(Structure):
    ulLength: UInt32
    ulProviderVersion: UInt32
WdsTransportCacheable = Guid('{70590b16-f146-46bd-bd9d-4aaa90084bf5}')
WdsTransportClient = Guid('{66d2c5e9-0ff6-49ec-9733-dafb1e01df1c}')
WdsTransportCollection = Guid('{c7f18b09-391e-436e-b10b-c3ef46f2c34f}')
WdsTransportConfigurationManager = Guid('{8743f674-904c-47ca-8512-35fe98f6b0ac}')
WdsTransportContent = Guid('{0a891fe7-4a3f-4c65-b6f2-1467619679ea}')
WdsTransportContentProvider = Guid('{e0be741f-5a75-4eb9-8a2d-5e189b45f327}')
WdsTransportDiagnosticsPolicy = Guid('{eb3333e1-a7ad-46f5-80d6-6b740204e509}')
WdsTransportManager = Guid('{f21523f6-837c-4a58-af99-8a7e27f8ff59}')
WdsTransportMulticastSessionPolicy = Guid('{3c6bc3f4-6418-472a-b6f1-52d457195437}')
WdsTransportNamespace = Guid('{d8385768-0732-4ec1-95ea-16da581908a1}')
WdsTransportNamespaceAutoCast = Guid('{b091f5a8-6a99-478d-b23b-09e8fee04574}')
WdsTransportNamespaceManager = Guid('{f08cdb63-85de-4a28-a1a9-5ca3e7efda73}')
WdsTransportNamespaceScheduledCast = Guid('{badc1897-7025-44eb-9108-fb61c4055792}')
WdsTransportNamespaceScheduledCastAutoStart = Guid('{a1107052-122c-4b81-9b7c-386e6855383f}')
WdsTransportNamespaceScheduledCastManualStart = Guid('{d3e1a2aa-caac-460e-b98a-47f9f318a1fa}')
WdsTransportServer = Guid('{ea19b643-4adf-4413-942c-14f379118760}')
WdsTransportServicePolicy = Guid('{65aceadc-2f0b-4f43-9f4d-811865d8cead}')
WdsTransportSession = Guid('{749ac4e0-67bc-4743-bfe5-cacb1f26f57f}')
WdsTransportSetupManager = Guid('{c7beeaad-9f04-4923-9f0c-fbf52bc7590f}')
WdsTransportTftpClient = Guid('{50343925-7c5c-4c8c-96c4-ad9fa5005fba}')
WdsTransportTftpManager = Guid('{c8e9dca2-3241-4e4d-b806-bc74019dfeda}')


make_ready(__name__)
