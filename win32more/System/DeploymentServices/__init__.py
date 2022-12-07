from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.DeploymentServices
import win32more.System.Registry
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
WDSMCSERVER_CATEGORY: win32more.Foundation.HRESULT = 1
WDSMCCLIENT_CATEGORY: win32more.Foundation.HRESULT = 2
WDSMCS_E_SESSION_SHUTDOWN_IN_PROGRESS: win32more.Foundation.HRESULT = -1054801664
WDSMCS_E_REQCALLBACKS_NOT_REG: win32more.Foundation.HRESULT = -1054801663
WDSMCS_E_INCOMPATIBLE_VERSION: win32more.Foundation.HRESULT = -1054801662
WDSMCS_E_CONTENT_NOT_FOUND: win32more.Foundation.HRESULT = -1054801661
WDSMCS_E_CLIENT_NOT_FOUND: win32more.Foundation.HRESULT = -1054801660
WDSMCS_E_NAMESPACE_NOT_FOUND: win32more.Foundation.HRESULT = -1054801659
WDSMCS_E_CONTENT_PROVIDER_NOT_FOUND: win32more.Foundation.HRESULT = -1054801658
WDSMCS_E_NAMESPACE_ALREADY_EXISTS: win32more.Foundation.HRESULT = -1054801657
WDSMCS_E_NAMESPACE_SHUTDOWN_IN_PROGRESS: win32more.Foundation.HRESULT = -1054801656
WDSMCS_E_NAMESPACE_ALREADY_STARTED: win32more.Foundation.HRESULT = -1054801655
WDSMCS_E_NS_START_FAILED_NO_CLIENTS: win32more.Foundation.HRESULT = -1054801654
WDSMCS_E_START_TIME_IN_PAST: win32more.Foundation.HRESULT = -1054801653
WDSMCS_E_PACKET_NOT_HASHED: win32more.Foundation.HRESULT = -1054801652
WDSMCS_E_PACKET_NOT_SIGNED: win32more.Foundation.HRESULT = -1054801651
WDSMCS_E_PACKET_HAS_SECURITY: win32more.Foundation.HRESULT = -1054801650
WDSMCS_E_PACKET_NOT_CHECKSUMED: win32more.Foundation.HRESULT = -1054801649
WDSMCS_E_CLIENT_DOESNOT_SUPPORT_SECURITY_MODE: win32more.Foundation.HRESULT = -1054801648
EVT_WDSMCS_S_PARAMETERS_READ: win32more.Foundation.HRESULT = 1092682240
EVT_WDSMCS_E_PARAMETERS_READ_FAILED: win32more.Foundation.HRESULT = -1054801407
EVT_WDSMCS_E_DUPLICATE_MULTICAST_ADDR: win32more.Foundation.HRESULT = -1054801406
EVT_WDSMCS_E_NON_WDS_DUPLICATE_MULTICAST_ADDR: win32more.Foundation.HRESULT = -1054801405
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED: win32more.Foundation.HRESULT = -1054801328
EVT_WDSMCS_E_CP_INIT_FUNC_MISSING: win32more.Foundation.HRESULT = -1054801327
EVT_WDSMCS_E_CP_INIT_FUNC_FAILED: win32more.Foundation.HRESULT = -1054801326
EVT_WDSMCS_E_CP_INCOMPATIBLE_SERVER_VERSION: win32more.Foundation.HRESULT = -1054801325
EVT_WDSMCS_E_CP_CALLBACKS_NOT_REG: win32more.Foundation.HRESULT = -1054801324
EVT_WDSMCS_E_CP_SHUTDOWN_FUNC_FAILED: win32more.Foundation.HRESULT = -1054801323
EVT_WDSMCS_E_CP_MEMORY_LEAK: win32more.Foundation.HRESULT = -1054801322
EVT_WDSMCS_E_CP_OPEN_INSTANCE_FAILED: win32more.Foundation.HRESULT = -1054801321
EVT_WDSMCS_E_CP_CLOSE_INSTANCE_FAILED: win32more.Foundation.HRESULT = -1054801320
EVT_WDSMCS_E_CP_OPEN_CONTENT_FAILED: win32more.Foundation.HRESULT = -1054801319
EVT_WDSMCS_W_CP_DLL_LOAD_FAILED_NOT_CRITICAL: win32more.Foundation.HRESULT = -2128543142
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED_CRITICAL: win32more.Foundation.HRESULT = -1054801317
EVT_WDSMCS_E_NSREG_START_TIME_IN_PAST: win32more.Foundation.HRESULT = -1054801152
EVT_WDSMCS_E_NSREG_CONTENT_PROVIDER_NOT_REG: win32more.Foundation.HRESULT = -1054801151
EVT_WDSMCS_E_NSREG_NAMESPACE_EXISTS: win32more.Foundation.HRESULT = -1054801150
EVT_WDSMCS_E_NSREG_FAILURE: win32more.Foundation.HRESULT = -1054801149
WDSTPC_E_CALLBACKS_NOT_REG: win32more.Foundation.HRESULT = -1054735616
WDSTPC_E_ALREADY_COMPLETED: win32more.Foundation.HRESULT = -1054735615
WDSTPC_E_ALREADY_IN_PROGRESS: win32more.Foundation.HRESULT = -1054735614
WDSTPC_E_UNKNOWN_ERROR: win32more.Foundation.HRESULT = -1054735613
WDSTPC_E_NOT_INITIALIZED: win32more.Foundation.HRESULT = -1054735612
WDSTPC_E_KICKED_POLICY_NOT_MET: win32more.Foundation.HRESULT = -1054735611
WDSTPC_E_KICKED_FALLBACK: win32more.Foundation.HRESULT = -1054735610
WDSTPC_E_KICKED_FAIL: win32more.Foundation.HRESULT = -1054735609
WDSTPC_E_KICKED_UNKNOWN: win32more.Foundation.HRESULT = -1054735608
WDSTPC_E_MULTISTREAM_NOT_ENABLED: win32more.Foundation.HRESULT = -1054735607
WDSTPC_E_ALREADY_IN_LOWEST_SESSION: win32more.Foundation.HRESULT = -1054735606
WDSTPC_E_CLIENT_DEMOTE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1054735605
WDSTPC_E_NO_IP4_INTERFACE: win32more.Foundation.HRESULT = -1054735604
WDSTPTC_E_WIM_APPLY_REQUIRES_REFERENCE_IMAGE: win32more.Foundation.HRESULT = -1054735603
FACILITY_WDSTPTMGMT: UInt32 = 272
WDSTPTMGMT_CATEGORY: win32more.Foundation.HRESULT = 1
WDSTPTMGMT_E_INVALID_PROPERTY: win32more.Foundation.HRESULT = -1055915776
WDSTPTMGMT_E_INVALID_OPERATION: win32more.Foundation.HRESULT = -1055915775
WDSTPTMGMT_E_INVALID_CLASS: win32more.Foundation.HRESULT = -1055915774
WDSTPTMGMT_E_CONTENT_PROVIDER_ALREADY_REGISTERED: win32more.Foundation.HRESULT = -1055915773
WDSTPTMGMT_E_CONTENT_PROVIDER_NOT_REGISTERED: win32more.Foundation.HRESULT = -1055915772
WDSTPTMGMT_E_INVALID_CONTENT_PROVIDER_NAME: win32more.Foundation.HRESULT = -1055915771
WDSTPTMGMT_E_TRANSPORT_SERVER_ROLE_NOT_CONFIGURED: win32more.Foundation.HRESULT = -1055915770
WDSTPTMGMT_E_NAMESPACE_ALREADY_REGISTERED: win32more.Foundation.HRESULT = -1055915769
WDSTPTMGMT_E_NAMESPACE_NOT_REGISTERED: win32more.Foundation.HRESULT = -1055915768
WDSTPTMGMT_E_CANNOT_REINITIALIZE_OBJECT: win32more.Foundation.HRESULT = -1055915767
WDSTPTMGMT_E_INVALID_NAMESPACE_NAME: win32more.Foundation.HRESULT = -1055915766
WDSTPTMGMT_E_INVALID_NAMESPACE_DATA: win32more.Foundation.HRESULT = -1055915765
WDSTPTMGMT_E_NAMESPACE_READ_ONLY: win32more.Foundation.HRESULT = -1055915764
WDSTPTMGMT_E_INVALID_NAMESPACE_START_TIME: win32more.Foundation.HRESULT = -1055915763
WDSTPTMGMT_E_INVALID_DIAGNOSTICS_COMPONENTS: win32more.Foundation.HRESULT = -1055915762
WDSTPTMGMT_E_CANNOT_REFRESH_DIRTY_OBJECT: win32more.Foundation.HRESULT = -1055915761
WDSTPTMGMT_E_INVALID_SERVICE_IP_ADDRESS_RANGE: win32more.Foundation.HRESULT = -1055915760
WDSTPTMGMT_E_INVALID_SERVICE_PORT_RANGE: win32more.Foundation.HRESULT = -1055915759
WDSTPTMGMT_E_INVALID_NAMESPACE_START_PARAMETERS: win32more.Foundation.HRESULT = -1055915758
WDSTPTMGMT_E_TRANSPORT_SERVER_UNAVAILABLE: win32more.Foundation.HRESULT = -1055915757
WDSTPTMGMT_E_NAMESPACE_NOT_ON_SERVER: win32more.Foundation.HRESULT = -1055915756
WDSTPTMGMT_E_NAMESPACE_REMOVED_FROM_SERVER: win32more.Foundation.HRESULT = -1055915755
WDSTPTMGMT_E_INVALID_IP_ADDRESS: win32more.Foundation.HRESULT = -1055915754
WDSTPTMGMT_E_INVALID_IPV4_MULTICAST_ADDRESS: win32more.Foundation.HRESULT = -1055915753
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS: win32more.Foundation.HRESULT = -1055915752
WDSTPTMGMT_E_IPV6_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915751
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS_SOURCE: win32more.Foundation.HRESULT = -1055915750
WDSTPTMGMT_E_INVALID_MULTISTREAM_STREAM_COUNT: win32more.Foundation.HRESULT = -1055915749
WDSTPTMGMT_E_INVALID_AUTO_DISCONNECT_THRESHOLD: win32more.Foundation.HRESULT = -1055915748
WDSTPTMGMT_E_MULTICAST_SESSION_POLICY_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915747
WDSTPTMGMT_E_INVALID_SLOW_CLIENT_HANDLING_TYPE: win32more.Foundation.HRESULT = -1055915746
WDSTPTMGMT_E_NETWORK_PROFILES_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915745
WDSTPTMGMT_E_UDP_PORT_POLICY_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915744
WDSTPTMGMT_E_TFTP_MAX_BLOCKSIZE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915743
WDSTPTMGMT_E_TFTP_VAR_WINDOW_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1055915742
WDSTPTMGMT_E_INVALID_TFTP_MAX_BLOCKSIZE: win32more.Foundation.HRESULT = -1055915741
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
def WdsCliClose(Handle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliRegisterTrace(pfn: win32more.System.DeploymentServices.PFN_WdsCliTraceFunction) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFreeStringArray(ppwszArray: POINTER(win32more.Foundation.PWSTR), ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindFirstImage(hSession: win32more.Foundation.HANDLE, phFindHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindNextImage(Handle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetEnumerationFlags(Handle: win32more.Foundation.HANDLE, pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromFindHandle(FindHandle: win32more.Foundation.HANDLE, phImageHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromTransferHandle(hTransfer: win32more.Foundation.HANDLE, phImageHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCreateSession(pwszServer: win32more.Foundation.PWSTR, pCred: POINTER(win32more.System.DeploymentServices.WDS_CLI_CRED_head), phSession: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliAuthorizeSession(hSession: win32more.Foundation.HANDLE, pCred: POINTER(win32more.System.DeploymentServices.WDS_CLI_CRED_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliInitializeLog(hSession: win32more.Foundation.HANDLE, ulClientArchitecture: win32more.System.DeploymentServices.CPU_ARCHITECTURE, pwszClientId: win32more.Foundation.PWSTR, pwszClientAddress: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@cfunctype('WDSCLIENTAPI.dll')
def WdsCliLog(hSession: win32more.Foundation.HANDLE, ulLogLevel: UInt32, ulMessageCode: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageName(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageDescription(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageType(hIfh: win32more.Foundation.HANDLE, pImageType: POINTER(win32more.System.DeploymentServices.WDS_CLI_IMAGE_TYPE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageFiles(hIfh: win32more.Foundation.HANDLE, pppwszFiles: POINTER(POINTER(win32more.Foundation.PWSTR)), pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguage(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguages(hIfh: win32more.Foundation.HANDLE, pppszValues: POINTER(POINTER(POINTER(SByte))), pdwNumValues: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageVersion(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImagePath(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageIndex(hIfh: win32more.Foundation.HANDLE, pdwValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageArchitecture(hIfh: win32more.Foundation.HANDLE, pdwValue: POINTER(win32more.System.DeploymentServices.CPU_ARCHITECTURE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLastModifiedTime(hIfh: win32more.Foundation.HANDLE, ppSysTimeValue: POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageSize(hIfh: win32more.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHalName(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageGroup(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageNamespace(hIfh: win32more.Foundation.HANDLE, ppwszValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageParameter(hIfh: win32more.Foundation.HANDLE, ParamType: win32more.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE, pResponse: c_void_p, uResponseLen: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetTransferSize(hIfh: win32more.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliSetTransferBufferSize(ulSizeInBytes: UInt32) -> Void: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferImage(hImage: win32more.Foundation.HANDLE, pwszLocalPath: win32more.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: win32more.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: c_void_p, phTransfer: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferFile(pwszServer: win32more.Foundation.PWSTR, pwszNamespace: win32more.Foundation.PWSTR, pwszRemoteFilePath: win32more.Foundation.PWSTR, pwszLocalFilePath: win32more.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: win32more.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: c_void_p, phTransfer: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCancelTransfer(hTransfer: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliWaitForTransfer(hTransfer: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackages(hImage: win32more.Foundation.HANDLE, ppwszServerName: POINTER(win32more.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(win32more.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackagesEx(hSession: win32more.Foundation.HANDLE, pwszMachineInfo: win32more.Foundation.PWSTR, ppwszServerName: POINTER(win32more.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(win32more.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetDriverQueryXml(pwszWinDirPath: win32more.Foundation.PWSTR, ppwszDriverQuery: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSPXE.dll')
def PxeProviderRegister(pszProviderName: win32more.Foundation.PWSTR, pszModulePath: win32more.Foundation.PWSTR, Index: UInt32, bIsCritical: win32more.Foundation.BOOL, phProviderKey: POINTER(win32more.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderUnRegister(pszProviderName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderQueryIndex(pszProviderName: win32more.Foundation.PWSTR, puIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumFirst(phEnum: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumNext(hEnum: win32more.Foundation.HANDLE, ppProvider: POINTER(POINTER(win32more.System.DeploymentServices.PXE_PROVIDER_head))) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumClose(hEnum: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderFreeInfo(pProvider: POINTER(win32more.System.DeploymentServices.PXE_PROVIDER_head)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeRegisterCallback(hProvider: win32more.Foundation.HANDLE, CallbackType: UInt32, pCallbackFunction: c_void_p, pContext: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeSendReply(hClientRequest: win32more.Foundation.HANDLE, pPacket: c_void_p, uPacketLen: UInt32, pAddress: POINTER(win32more.System.DeploymentServices.PXE_ADDRESS_head)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeAsyncRecvDone(hClientRequest: win32more.Foundation.HANDLE, Action: UInt32) -> UInt32: ...
@cfunctype('WDSPXE.dll')
def PxeTrace(hProvider: win32more.Foundation.HANDLE, Severity: UInt32, pszFormat: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeTraceV(hProvider: win32more.Foundation.HANDLE, Severity: UInt32, pszFormat: win32more.Foundation.PWSTR, Params: POINTER(SByte)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxePacketAllocate(hProvider: win32more.Foundation.HANDLE, hClientRequest: win32more.Foundation.HANDLE, uSize: UInt32) -> c_void_p: ...
@winfunctype('WDSPXE.dll')
def PxePacketFree(hProvider: win32more.Foundation.HANDLE, hClientRequest: win32more.Foundation.HANDLE, pPacket: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderSetAttribute(hProvider: win32more.Foundation.HANDLE, Attribute: UInt32, pParameterBuffer: c_void_p, uParamLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpInitialize(pRecvPacket: c_void_p, uRecvPacketLen: UInt32, pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6Initialize(pRequest: c_void_p, cbRequest: UInt32, pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOption(pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), bOption: Byte, bOptionLen: Byte, pValue: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOption(pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), wOptionType: UInt16, cbOption: UInt16, pOption: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOptionRaw(pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), uBufferLen: UInt16, pBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOptionRaw(pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), cbBuffer: UInt16, pBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpIsValid(pPacket: c_void_p, uPacketLen: UInt32, bRequestPacket: win32more.Foundation.BOOL, pbPxeOptionPresent: POINTER(win32more.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6IsValid(pPacket: c_void_p, uPacketLen: UInt32, bRequestPacket: win32more.Foundation.BOOL, pbPxeOptionPresent: POINTER(win32more.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetOptionValue(pPacket: c_void_p, uPacketLen: UInt32, uInstance: UInt32, bOption: Byte, pbOptionLen: c_char_p_no, ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetOptionValue(pPacket: c_void_p, uPacketLen: UInt32, uInstance: UInt32, wOption: UInt16, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetVendorOptionValue(pPacket: c_void_p, uPacketLen: UInt32, bOption: Byte, uInstance: UInt32, pbOptionLen: c_char_p_no, ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetVendorOptionValue(pPacket: c_void_p, uPacketLen: UInt32, dwEnterpriseNumber: UInt32, wOption: UInt16, uInstance: UInt32, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6ParseRelayForw(pRelayForwPacket: c_void_p, uRelayForwPacketLen: UInt32, pRelayMessages: POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head), nRelayMessages: UInt32, pnRelayMessages: POINTER(UInt32), ppInnerPacket: POINTER(c_char_p_no), pcbInnerPacket: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6CreateRelayRepl(pRelayMessages: POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head), nRelayMessages: UInt32, pInnerPacket: c_char_p_no, cbInnerPacket: UInt32, pReplyBuffer: c_void_p, cbReplyBuffer: UInt32, pcbReplyBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfo(uInfoType: UInt32, pBuffer: c_void_p, uBufferLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfoEx(uInfoType: UInt32, pBuffer: c_void_p, uBufferLen: UInt32, puBufferUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerRegisterCallback(hProvider: win32more.Foundation.HANDLE, CallbackId: win32more.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID, pfnCallback: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerCompleteRead(hProvider: win32more.Foundation.HANDLE, ulBytesRead: UInt32, pvUserData: c_void_p, hReadResult: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
@cfunctype('WDSMC.dll')
def WdsTransportServerTrace(hProvider: win32more.Foundation.HANDLE, Severity: UInt32, pwszFormat: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerTraceV(hProvider: win32more.Foundation.HANDLE, Severity: UInt32, pwszFormat: win32more.Foundation.PWSTR, Params: POINTER(SByte)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerAllocateBuffer(hProvider: win32more.Foundation.HANDLE, ulBufferSize: UInt32) -> c_void_p: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerFreeBuffer(hProvider: win32more.Foundation.HANDLE, pvBuffer: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitialize() -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitializeSession(pSessionRequest: POINTER(win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_head), pCallerData: c_void_p, hSessionKey: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientRegisterCallback(hSessionKey: win32more.Foundation.HANDLE, CallbackId: win32more.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID, pfnCallback: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientStartSession(hSessionKey: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCompleteReceive(hSessionKey: win32more.Foundation.HANDLE, ulSize: UInt32, pullOffset: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSession(hSessionKey: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSessionEx(hSessionKey: win32more.Foundation.HANDLE, dwErrorCode: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientWaitForCompletion(hSessionKey: win32more.Foundation.HANDLE, uTimeout: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientQueryStatus(hSessionKey: win32more.Foundation.HANDLE, puStatus: POINTER(UInt32), puErrorCode: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCloseSession(hSessionKey: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientAddRefBuffer(pvBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientReleaseBuffer(pvBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientShutdown() -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitialize(pPacket: c_void_p, uPacketLen: UInt32, pbPacketType: c_char_p_no, phHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitializev6(pPacket: c_void_p, uPacketLen: UInt32, pbPacketType: c_char_p_no, phHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpInitialize(bPacketType: Byte, phHandle: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpCloseHandle(hHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpQueryOption(hHandle: win32more.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: c_void_p, puBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpAddOption(hHandle: win32more.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: c_void_p) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpGetOptionBuffer(hHandle: win32more.Foundation.HANDLE, uBufferLen: UInt32, pBuffer: c_void_p, puBytes: POINTER(UInt32)) -> UInt32: ...
CPU_ARCHITECTURE = UInt32
CPU_ARCHITECTURE_AMD64: CPU_ARCHITECTURE = 9
CPU_ARCHITECTURE_IA64: CPU_ARCHITECTURE = 6
CPU_ARCHITECTURE_INTEL: CPU_ARCHITECTURE = 0
class IWdsTransportCacheable(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('46ad894b-0bab-47dc-84-b2-7b-55-3f-1d-8f-80')
    @commethod(7)
    def get_Dirty(pbDirty: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Discard() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Commit() -> win32more.Foundation.HRESULT: ...
class IWdsTransportClient(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b5dbc93a-cabe-46ca-83-7f-3e-44-e9-3c-65-45')
    @commethod(7)
    def get_Session(ppWdsTransportSession: POINTER(win32more.System.DeploymentServices.IWdsTransportSession_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pulId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbszName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MacAddress(pbszMacAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddress(pbszIpAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_PercentCompletion(pulPercentCompletion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_JoinDuration(pulJoinDuration: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_CpuUtilization(pulCpuUtilization: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_MemoryUtilization(pulMemoryUtilization: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_NetworkUtilization(pulNetworkUtilization: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_UserIdentity(pbszUserIdentity: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Disconnect(DisconnectionType: win32more.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> win32more.Foundation.HRESULT: ...
class IWdsTransportCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b8ba4b1a-2ff4-43ab-99-6c-b2-b1-0a-91-a6-eb')
    @commethod(7)
    def get_Count(pulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(ulIndex: UInt32, ppVal: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('84cc4779-42dd-4792-89-1e-13-21-d6-d7-4b-44')
    @commethod(7)
    def get_ServicePolicy(ppWdsTransportServicePolicy: POINTER(win32more.System.DeploymentServices.IWdsTransportServicePolicy_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_DiagnosticsPolicy(ppWdsTransportDiagnosticsPolicy: POINTER(win32more.System.DeploymentServices.IWdsTransportDiagnosticsPolicy_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_WdsTransportServicesRunning(bRealtimeStatus: win32more.Foundation.VARIANT_BOOL, pbServicesRunning: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EnableWdsTransportServices() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DisableWdsTransportServices() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def StartWdsTransportServices() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def StopWdsTransportServices() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def RestartWdsTransportServices() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def NotifyWdsTransportServices(ServiceNotification: win32more.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION) -> win32more.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager2(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportConfigurationManager
    Guid = Guid('d0d85caf-a153-4f1d-a9-dd-96-f4-31-c5-07-17')
    @commethod(16)
    def get_MulticastSessionPolicy(ppWdsTransportMulticastSessionPolicy: POINTER(win32more.System.DeploymentServices.IWdsTransportMulticastSessionPolicy_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportContent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d405d711-0296-4ab4-a8-60-ac-7d-32-e6-57-98')
    @commethod(7)
    def get_Namespace(ppWdsTransportNamespace: POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pulId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbszName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RetrieveSessions(ppWdsTransportSessions: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Terminate() -> win32more.Foundation.HRESULT: ...
class IWdsTransportContentProvider(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b9489f24-f219-4acf-aa-d7-26-5c-7c-08-a6-ae')
    @commethod(7)
    def get_Name(pbszName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Description(pbszDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_FilePath(pbszFilePath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_InitializationRoutine(pbszInitializationRoutine: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportDiagnosticsPolicy(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('13b33efc-7856-4f61-9a-59-8d-e6-7b-6b-87-b6')
    @commethod(11)
    def get_Enabled(pbEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enabled(bEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Components(pulComponents: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Components(ulComponents: UInt32) -> win32more.Foundation.HRESULT: ...
class IWdsTransportManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('5b0d35f5-1b13-4afd-b8-78-65-26-dc-34-0b-5d')
    @commethod(7)
    def GetWdsTransportServer(bszServerName: win32more.Foundation.BSTR, ppWdsTransportServer: POINTER(win32more.System.DeploymentServices.IWdsTransportServer_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportMulticastSessionPolicy(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('4e5753cf-68ec-4504-a9-51-4a-00-32-66-60-6b')
    @commethod(11)
    def get_SlowClientHandling(pSlowClientHandling: POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_SlowClientHandling(SlowClientHandling: win32more.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_AutoDisconnectThreshold(pulThreshold: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_AutoDisconnectThreshold(ulThreshold: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_MultistreamStreamCount(pulStreamCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_MultistreamStreamCount(ulStreamCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_SlowClientFallback(pbClientFallback: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_SlowClientFallback(bClientFallback: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IWdsTransportNamespace(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('fa561f57-fbef-4ed3-b0-56-12-7c-b1-b3-3b-84')
    @commethod(7)
    def get_Type(pType: POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pulId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbszName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(bszName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_FriendlyName(pbszFriendlyName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_FriendlyName(bszFriendlyName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(pbszDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Description(bszDescription: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ContentProvider(pbszContentProvider: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ContentProvider(bszContentProvider: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Configuration(pbszConfiguration: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Configuration(bszConfiguration: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Registered(pbRegistered: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Tombstoned(pbTombstoned: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_TombstoneTime(pTombstoneTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_TransmissionStarted(pbTransmissionStarted: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Register() -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Deregister(bTerminateSessions: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def Clone(ppWdsTransportNamespaceClone: POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def RetrieveContents(ppWdsTransportContents: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportNamespaceAutoCast(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportNamespace
    Guid = Guid('ad931a72-c4bd-4c41-8f-bc-59-c9-c7-48-df-9e')
class IWdsTransportNamespaceManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('3e22d9f6-3777-4d98-83-e1-f9-86-96-71-7b-a3')
    @commethod(7)
    def CreateNamespace(NamespaceType: win32more.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE, bszNamespaceName: win32more.Foundation.BSTR, bszContentProvider: win32more.Foundation.BSTR, bszConfiguration: win32more.Foundation.BSTR, ppWdsTransportNamespace: POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveNamespace(bszNamespaceName: win32more.Foundation.BSTR, ppWdsTransportNamespace: POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RetrieveNamespaces(bszContentProvider: win32more.Foundation.BSTR, bszNamespaceName: win32more.Foundation.BSTR, bIncludeTombstones: win32more.Foundation.VARIANT_BOOL, ppWdsTransportNamespaces: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCast(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportNamespace
    Guid = Guid('3840cecf-d76c-416e-a4-cc-31-c7-41-d2-87-4b')
    @commethod(28)
    def StartTransmission() -> win32more.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastAutoStart(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    Guid = Guid('d606af3d-ea9c-4219-96-1e-74-91-d6-18-d9-b9')
    @commethod(29)
    def get_MinimumClients(pulMinimumClients: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_MinimumClients(ulMinimumClients: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_StartTime(pStartTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_StartTime(StartTime: Double) -> win32more.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastManualStart(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    Guid = Guid('013e6e4c-e6a7-4fb5-b7-ff-d9-f5-da-80-5c-31')
class IWdsTransportServer(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('09ccd093-830d-4344-a3-0a-73-ae-8e-8f-ca-90')
    @commethod(7)
    def get_Name(pbszName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_SetupManager(ppWdsTransportSetupManager: POINTER(win32more.System.DeploymentServices.IWdsTransportSetupManager_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_ConfigurationManager(ppWdsTransportConfigurationManager: POINTER(win32more.System.DeploymentServices.IWdsTransportConfigurationManager_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_NamespaceManager(ppWdsTransportNamespaceManager: POINTER(win32more.System.DeploymentServices.IWdsTransportNamespaceManager_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DisconnectClient(ulClientId: UInt32, DisconnectionType: win32more.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> win32more.Foundation.HRESULT: ...
class IWdsTransportServer2(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportServer
    Guid = Guid('256e999f-6df4-4538-81-b9-85-7b-9a-b8-fb-47')
    @commethod(12)
    def get_TftpManager(ppWdsTransportTftpManager: POINTER(win32more.System.DeploymentServices.IWdsTransportTftpManager_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportServicePolicy(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('b9468578-9f2b-48cc-b2-7a-a6-07-99-c2-75-0c')
    @commethod(11)
    def get_IpAddressSource(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pSourceType: POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddressSource(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, SourceType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_StartIpAddress(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszStartIpAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_StartIpAddress(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszStartIpAddress: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_EndIpAddress(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszEndIpAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_EndIpAddress(AddressType: win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszEndIpAddress: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_StartPort(pulStartPort: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_StartPort(ulStartPort: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_EndPort(pulEndPort: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_EndPort(ulEndPort: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_NetworkProfile(pProfileType: POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_NetworkProfile(ProfileType: win32more.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE) -> win32more.Foundation.HRESULT: ...
class IWdsTransportServicePolicy2(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportServicePolicy
    Guid = Guid('65c19e5c-aa7e-4b91-89-44-91-e0-e5-57-27-97')
    @commethod(23)
    def get_UdpPortPolicy(pUdpPortPolicy: POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_UdpPortPolicy(UdpPortPolicy: win32more.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_TftpMaximumBlockSize(pulTftpMaximumBlockSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_TftpMaximumBlockSize(ulTftpMaximumBlockSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_EnableTftpVariableWindowExtension(pbEnableTftpVariableWindowExtension: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_EnableTftpVariableWindowExtension(bEnableTftpVariableWindowExtension: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IWdsTransportSession(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f4efea88-65b1-4f30-a4-b9-27-93-98-77-96-fb')
    @commethod(7)
    def get_Content(ppWdsTransportContent: POINTER(win32more.System.DeploymentServices.IWdsTransportContent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pulId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_NetworkInterfaceName(pbszNetworkInterfaceName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkInterfaceAddress(pbszNetworkInterfaceAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_TransferRate(pulTransferRate: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_MasterClientId(pulMasterClientId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RetrieveClients(ppWdsTransportClients: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Terminate() -> win32more.Foundation.HRESULT: ...
class IWdsTransportSetupManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f7238425-efa8-40a4-ae-f9-c9-8d-96-9c-0b-75')
    @commethod(7)
    def get_Version(pullVersion: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_InstalledFeatures(pulInstalledFeatures: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Protocols(pulProtocols: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterContentProvider(bszName: win32more.Foundation.BSTR, bszDescription: win32more.Foundation.BSTR, bszFilePath: win32more.Foundation.BSTR, bszInitializationRoutine: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DeregisterContentProvider(bszName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IWdsTransportSetupManager2(c_void_p):
    extends: win32more.System.DeploymentServices.IWdsTransportSetupManager
    Guid = Guid('02be79da-7e9e-4366-8b-6e-2a-a9-a9-1b-e4-7f')
    @commethod(12)
    def get_TftpCapabilities(pulTftpCapabilities: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ContentProviders(ppProviderCollection: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportTftpClient(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b022d3ae-884d-4d85-b1-46-53-32-0e-76-ef-62')
    @commethod(7)
    def get_FileName(pbszFileName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_IpAddress(pbszIpAddress: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Timeout(pulTimeout: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentFileOffset(pul64CurrentOffset: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_FileSize(pul64FileSize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_BlockSize(pulBlockSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_WindowSize(pulWindowSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWdsTransportTftpManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1327a7c8-ae8a-4fb3-81-50-13-62-27-c3-7e-9a')
    @commethod(7)
    def RetrieveTftpClients(ppWdsTransportTftpClients: POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head)) -> win32more.Foundation.HRESULT: ...
PFN_WDS_CLI_CALLBACK_MESSAGE_ID = UInt32
WDS_CLI_MSG_START: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 0
WDS_CLI_MSG_COMPLETE: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 1
WDS_CLI_MSG_PROGRESS: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 2
WDS_CLI_MSG_TEXT: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 3
@winfunctype_pointer
def PFN_WdsCliCallback(dwMessageId: win32more.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pvUserData: c_void_p) -> Void: ...
@winfunctype_pointer
def PFN_WdsCliTraceFunction(pwszFormat: win32more.Foundation.PWSTR, Params: POINTER(SByte)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveContents(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, pContents: c_void_p, ulSize: UInt32, pullContentOffset: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveMetadata(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, pMetadata: c_void_p, ulSize: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionComplete(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, dwError: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionNegotiate(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, pInfo: POINTER(win32more.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head), hNegotiateKey: win32more.Foundation.HANDLE) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStart(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, ullFileSize: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStartEx(hSessionKey: win32more.Foundation.HANDLE, pCallerData: c_void_p, Info: POINTER(win32more.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head)) -> Void: ...
class PXE_ADDRESS(Structure):
    uFlags: UInt32
    Anonymous: _Anonymous_e__Union
    uAddrLen: UInt32
    uPort: UInt16
    class _Anonymous_e__Union(Union):
        bAddress: Byte * 16
        uIpAddress: UInt32
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
    Option: win32more.System.DeploymentServices.PXE_DHCP_OPTION
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
class PXE_DHCPV6_MESSAGE(Structure):
    MessageType: Byte
    TransactionIDByte1: Byte
    TransactionIDByte2: Byte
    TransactionIDByte3: Byte
    Options: win32more.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_DHCPV6_MESSAGE_HEADER(Structure):
    MessageType: Byte
    Message: Byte * 1
    _pack_ = 1
class PXE_DHCPV6_NESTED_RELAY_MESSAGE(Structure):
    pRelayMessage: POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_RELAY_MESSAGE_head)
    cbRelayMessage: UInt32
    pInterfaceIdOption: c_void_p
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
    Options: win32more.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_PROVIDER(Structure):
    uSizeOfStruct: UInt32
    pwszName: win32more.Foundation.PWSTR
    pwszFilePath: win32more.Foundation.PWSTR
    bIsCritical: win32more.Foundation.BOOL
    uIndex: UInt32
TRANSPORTCLIENT_CALLBACK_ID = Int32
WDS_TRANSPORTCLIENT_SESSION_START: TRANSPORTCLIENT_CALLBACK_ID = 0
WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS: TRANSPORTCLIENT_CALLBACK_ID = 1
WDS_TRANSPORTCLIENT_SESSION_COMPLETE: TRANSPORTCLIENT_CALLBACK_ID = 2
WDS_TRANSPORTCLIENT_RECEIVE_METADATA: TRANSPORTCLIENT_CALLBACK_ID = 3
WDS_TRANSPORTCLIENT_SESSION_STARTEX: TRANSPORTCLIENT_CALLBACK_ID = 4
WDS_TRANSPORTCLIENT_SESSION_NEGOTIATE: TRANSPORTCLIENT_CALLBACK_ID = 5
WDS_TRANSPORTCLIENT_MAX_CALLBACKS: TRANSPORTCLIENT_CALLBACK_ID = 6
class TRANSPORTCLIENT_SESSION_INFO(Structure):
    ulStructureLength: UInt32
    ullFileSize: win32more.Foundation.ULARGE_INTEGER
    ulBlockSize: UInt32
TRANSPORTPROVIDER_CALLBACK_ID = Int32
WDS_TRANSPORTPROVIDER_CREATE_INSTANCE: TRANSPORTPROVIDER_CALLBACK_ID = 0
WDS_TRANSPORTPROVIDER_COMPARE_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 1
WDS_TRANSPORTPROVIDER_OPEN_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 2
WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK: TRANSPORTPROVIDER_CALLBACK_ID = 3
WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE: TRANSPORTPROVIDER_CALLBACK_ID = 4
WDS_TRANSPORTPROVIDER_READ_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 5
WDS_TRANSPORTPROVIDER_CLOSE_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 6
WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE: TRANSPORTPROVIDER_CALLBACK_ID = 7
WDS_TRANSPORTPROVIDER_SHUTDOWN: TRANSPORTPROVIDER_CALLBACK_ID = 8
WDS_TRANSPORTPROVIDER_DUMP_STATE: TRANSPORTPROVIDER_CALLBACK_ID = 9
WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS: TRANSPORTPROVIDER_CALLBACK_ID = 10
WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA: TRANSPORTPROVIDER_CALLBACK_ID = 11
WDS_TRANSPORTPROVIDER_MAX_CALLBACKS: TRANSPORTPROVIDER_CALLBACK_ID = 12
class WDS_CLI_CRED(Structure):
    pwszUserName: win32more.Foundation.PWSTR
    pwszDomain: win32more.Foundation.PWSTR
    pwszPassword: win32more.Foundation.PWSTR
WDS_CLI_FIRMWARE_TYPE = Int32
WDS_CLI_FIRMWARE_UNKNOWN: WDS_CLI_FIRMWARE_TYPE = 0
WDS_CLI_FIRMWARE_BIOS: WDS_CLI_FIRMWARE_TYPE = 1
WDS_CLI_FIRMWARE_EFI: WDS_CLI_FIRMWARE_TYPE = 2
WDS_CLI_IMAGE_PARAM_TYPE = Int32
WDS_CLI_IMAGE_PARAM_UNKNOWN: WDS_CLI_IMAGE_PARAM_TYPE = 0
WDS_CLI_IMAGE_PARAM_SPARSE_FILE: WDS_CLI_IMAGE_PARAM_TYPE = 1
WDS_CLI_IMAGE_PARAM_SUPPORTED_FIRMWARES: WDS_CLI_IMAGE_PARAM_TYPE = 2
WDS_CLI_IMAGE_TYPE = Int32
WDS_CLI_IMAGE_TYPE_UNKNOWN: WDS_CLI_IMAGE_TYPE = 0
WDS_CLI_IMAGE_TYPE_WIM: WDS_CLI_IMAGE_TYPE = 1
WDS_CLI_IMAGE_TYPE_VHD: WDS_CLI_IMAGE_TYPE = 2
WDS_CLI_IMAGE_TYPE_VHDX: WDS_CLI_IMAGE_TYPE = 3
class WDS_TRANSPORTCLIENT_CALLBACKS(Structure):
    SessionStart: win32more.System.DeploymentServices.PFN_WdsTransportClientSessionStart
    SessionStartEx: win32more.System.DeploymentServices.PFN_WdsTransportClientSessionStartEx
    ReceiveContents: win32more.System.DeploymentServices.PFN_WdsTransportClientReceiveContents
    ReceiveMetadata: win32more.System.DeploymentServices.PFN_WdsTransportClientReceiveMetadata
    SessionComplete: win32more.System.DeploymentServices.PFN_WdsTransportClientSessionComplete
    SessionNegotiate: win32more.System.DeploymentServices.PFN_WdsTransportClientSessionNegotiate
class WDS_TRANSPORTCLIENT_REQUEST(Structure):
    ulLength: UInt32
    ulApiVersion: UInt32
    ulAuthLevel: win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL
    pwszServer: win32more.Foundation.PWSTR
    pwszNamespace: win32more.Foundation.PWSTR
    pwszObjectName: win32more.Foundation.PWSTR
    ulCacheSize: UInt32
    ulProtocol: UInt32
    pvProtocolData: c_void_p
    ulProtocolDataLength: UInt32
WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = UInt32
WDS_TRANSPORTCLIENT_AUTH: WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 1
WDS_TRANSPORTCLIENT_NO_AUTH: WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 2
class WDS_TRANSPORTPROVIDER_INIT_PARAMS(Structure):
    ulLength: UInt32
    ulMcServerVersion: UInt32
    hRegistryKey: win32more.System.Registry.HKEY
    hProvider: win32more.Foundation.HANDLE
class WDS_TRANSPORTPROVIDER_SETTINGS(Structure):
    ulLength: UInt32
    ulProviderVersion: UInt32
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = Int32
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentPxe: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 1
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentTftp: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 2
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentImageServer: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 4
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentMulticast: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 8
WDSTRANSPORT_DISCONNECT_TYPE = Int32
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectUnknown: WDSTRANSPORT_DISCONNECT_TYPE = 0
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectFallback: WDSTRANSPORT_DISCONNECT_TYPE = 1
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectAbort: WDSTRANSPORT_DISCONNECT_TYPE = 2
WDSTRANSPORT_FEATURE_FLAGS = Int32
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureAdminPack: WDSTRANSPORT_FEATURE_FLAGS = 1
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureTransportServer: WDSTRANSPORT_FEATURE_FLAGS = 2
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureDeploymentServer: WDSTRANSPORT_FEATURE_FLAGS = 4
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceUnknown: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 0
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceDhcp: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 1
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceRange: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 2
WDSTRANSPORT_IP_ADDRESS_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressUnknown: WDSTRANSPORT_IP_ADDRESS_TYPE = 0
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv4: WDSTRANSPORT_IP_ADDRESS_TYPE = 1
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv6: WDSTRANSPORT_IP_ADDRESS_TYPE = 2
WDSTRANSPORT_NAMESPACE_TYPE = Int32
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeUnknown: WDSTRANSPORT_NAMESPACE_TYPE = 0
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeAutoCast: WDSTRANSPORT_NAMESPACE_TYPE = 1
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastManualStart: WDSTRANSPORT_NAMESPACE_TYPE = 2
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastAutoStart: WDSTRANSPORT_NAMESPACE_TYPE = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE = Int32
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileUnknown: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 0
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileCustom: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 1
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile10Mbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 2
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile100Mbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile1Gbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 4
WDSTRANSPORT_PROTOCOL_FLAGS = Int32
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolUnicast: WDSTRANSPORT_PROTOCOL_FLAGS = 1
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolMulticast: WDSTRANSPORT_PROTOCOL_FLAGS = 2
WDSTRANSPORT_SERVICE_NOTIFICATION = Int32
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyUnknown: WDSTRANSPORT_SERVICE_NOTIFICATION = 0
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyReadSettings: WDSTRANSPORT_SERVICE_NOTIFICATION = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = Int32
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingUnknown: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 0
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingNone: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingAutoDisconnect: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 2
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingMultistream: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 3
WDSTRANSPORT_TFTP_CAPABILITY = Int32
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapMaximumBlockSize: WDSTRANSPORT_TFTP_CAPABILITY = 1
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapVariableWindow: WDSTRANSPORT_TFTP_CAPABILITY = 2
WDSTRANSPORT_UDP_PORT_POLICY = Int32
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyDynamic: WDSTRANSPORT_UDP_PORT_POLICY = 0
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyFixed: WDSTRANSPORT_UDP_PORT_POLICY = 1
WdsTransportCacheable = Guid('70590b16-f146-46bd-bd-9d-4a-aa-90-08-4b-f5')
WdsTransportClient = Guid('66d2c5e9-0ff6-49ec-97-33-da-fb-1e-01-df-1c')
WdsTransportCollection = Guid('c7f18b09-391e-436e-b1-0b-c3-ef-46-f2-c3-4f')
WdsTransportConfigurationManager = Guid('8743f674-904c-47ca-85-12-35-fe-98-f6-b0-ac')
WdsTransportContent = Guid('0a891fe7-4a3f-4c65-b6-f2-14-67-61-96-79-ea')
WdsTransportContentProvider = Guid('e0be741f-5a75-4eb9-8a-2d-5e-18-9b-45-f3-27')
WdsTransportDiagnosticsPolicy = Guid('eb3333e1-a7ad-46f5-80-d6-6b-74-02-04-e5-09')
WdsTransportManager = Guid('f21523f6-837c-4a58-af-99-8a-7e-27-f8-ff-59')
WdsTransportMulticastSessionPolicy = Guid('3c6bc3f4-6418-472a-b6-f1-52-d4-57-19-54-37')
WdsTransportNamespace = Guid('d8385768-0732-4ec1-95-ea-16-da-58-19-08-a1')
WdsTransportNamespaceAutoCast = Guid('b091f5a8-6a99-478d-b2-3b-09-e8-fe-e0-45-74')
WdsTransportNamespaceManager = Guid('f08cdb63-85de-4a28-a1-a9-5c-a3-e7-ef-da-73')
WdsTransportNamespaceScheduledCast = Guid('badc1897-7025-44eb-91-08-fb-61-c4-05-57-92')
WdsTransportNamespaceScheduledCastAutoStart = Guid('a1107052-122c-4b81-9b-7c-38-6e-68-55-38-3f')
WdsTransportNamespaceScheduledCastManualStart = Guid('d3e1a2aa-caac-460e-b9-8a-47-f9-f3-18-a1-fa')
WdsTransportServer = Guid('ea19b643-4adf-4413-94-2c-14-f3-79-11-87-60')
WdsTransportServicePolicy = Guid('65aceadc-2f0b-4f43-9f-4d-81-18-65-d8-ce-ad')
WdsTransportSession = Guid('749ac4e0-67bc-4743-bf-e5-ca-cb-1f-26-f5-7f')
WdsTransportSetupManager = Guid('c7beeaad-9f04-4923-9f-0c-fb-f5-2b-c7-59-0f')
WdsTransportTftpClient = Guid('50343925-7c5c-4c8c-96-c4-ad-9f-a5-00-5f-ba')
WdsTransportTftpManager = Guid('c8e9dca2-3241-4e4d-b8-06-bc-74-01-9d-fe-da')
make_head(_module, 'IWdsTransportCacheable')
make_head(_module, 'IWdsTransportClient')
make_head(_module, 'IWdsTransportCollection')
make_head(_module, 'IWdsTransportConfigurationManager')
make_head(_module, 'IWdsTransportConfigurationManager2')
make_head(_module, 'IWdsTransportContent')
make_head(_module, 'IWdsTransportContentProvider')
make_head(_module, 'IWdsTransportDiagnosticsPolicy')
make_head(_module, 'IWdsTransportManager')
make_head(_module, 'IWdsTransportMulticastSessionPolicy')
make_head(_module, 'IWdsTransportNamespace')
make_head(_module, 'IWdsTransportNamespaceAutoCast')
make_head(_module, 'IWdsTransportNamespaceManager')
make_head(_module, 'IWdsTransportNamespaceScheduledCast')
make_head(_module, 'IWdsTransportNamespaceScheduledCastAutoStart')
make_head(_module, 'IWdsTransportNamespaceScheduledCastManualStart')
make_head(_module, 'IWdsTransportServer')
make_head(_module, 'IWdsTransportServer2')
make_head(_module, 'IWdsTransportServicePolicy')
make_head(_module, 'IWdsTransportServicePolicy2')
make_head(_module, 'IWdsTransportSession')
make_head(_module, 'IWdsTransportSetupManager')
make_head(_module, 'IWdsTransportSetupManager2')
make_head(_module, 'IWdsTransportTftpClient')
make_head(_module, 'IWdsTransportTftpManager')
make_head(_module, 'PFN_WdsCliCallback')
make_head(_module, 'PFN_WdsCliTraceFunction')
make_head(_module, 'PFN_WdsTransportClientReceiveContents')
make_head(_module, 'PFN_WdsTransportClientReceiveMetadata')
make_head(_module, 'PFN_WdsTransportClientSessionComplete')
make_head(_module, 'PFN_WdsTransportClientSessionNegotiate')
make_head(_module, 'PFN_WdsTransportClientSessionStart')
make_head(_module, 'PFN_WdsTransportClientSessionStartEx')
make_head(_module, 'PXE_ADDRESS')
make_head(_module, 'PXE_DHCP_MESSAGE')
make_head(_module, 'PXE_DHCP_OPTION')
make_head(_module, 'PXE_DHCPV6_MESSAGE')
make_head(_module, 'PXE_DHCPV6_MESSAGE_HEADER')
make_head(_module, 'PXE_DHCPV6_NESTED_RELAY_MESSAGE')
make_head(_module, 'PXE_DHCPV6_OPTION')
make_head(_module, 'PXE_DHCPV6_RELAY_MESSAGE')
make_head(_module, 'PXE_PROVIDER')
make_head(_module, 'TRANSPORTCLIENT_SESSION_INFO')
make_head(_module, 'WDS_CLI_CRED')
make_head(_module, 'WDS_TRANSPORTCLIENT_CALLBACKS')
make_head(_module, 'WDS_TRANSPORTCLIENT_REQUEST')
make_head(_module, 'WDS_TRANSPORTPROVIDER_INIT_PARAMS')
make_head(_module, 'WDS_TRANSPORTPROVIDER_SETTINGS')
__all__ = [
    "CPU_ARCHITECTURE",
    "CPU_ARCHITECTURE_AMD64",
    "CPU_ARCHITECTURE_IA64",
    "CPU_ARCHITECTURE_INTEL",
    "EVT_WDSMCS_E_CP_CALLBACKS_NOT_REG",
    "EVT_WDSMCS_E_CP_CLOSE_INSTANCE_FAILED",
    "EVT_WDSMCS_E_CP_DLL_LOAD_FAILED",
    "EVT_WDSMCS_E_CP_DLL_LOAD_FAILED_CRITICAL",
    "EVT_WDSMCS_E_CP_INCOMPATIBLE_SERVER_VERSION",
    "EVT_WDSMCS_E_CP_INIT_FUNC_FAILED",
    "EVT_WDSMCS_E_CP_INIT_FUNC_MISSING",
    "EVT_WDSMCS_E_CP_MEMORY_LEAK",
    "EVT_WDSMCS_E_CP_OPEN_CONTENT_FAILED",
    "EVT_WDSMCS_E_CP_OPEN_INSTANCE_FAILED",
    "EVT_WDSMCS_E_CP_SHUTDOWN_FUNC_FAILED",
    "EVT_WDSMCS_E_DUPLICATE_MULTICAST_ADDR",
    "EVT_WDSMCS_E_NON_WDS_DUPLICATE_MULTICAST_ADDR",
    "EVT_WDSMCS_E_NSREG_CONTENT_PROVIDER_NOT_REG",
    "EVT_WDSMCS_E_NSREG_FAILURE",
    "EVT_WDSMCS_E_NSREG_NAMESPACE_EXISTS",
    "EVT_WDSMCS_E_NSREG_START_TIME_IN_PAST",
    "EVT_WDSMCS_E_PARAMETERS_READ_FAILED",
    "EVT_WDSMCS_S_PARAMETERS_READ",
    "EVT_WDSMCS_W_CP_DLL_LOAD_FAILED_NOT_CRITICAL",
    "FACILITY_WDSMCCLIENT",
    "FACILITY_WDSMCSERVER",
    "FACILITY_WDSTPTMGMT",
    "IWdsTransportCacheable",
    "IWdsTransportClient",
    "IWdsTransportCollection",
    "IWdsTransportConfigurationManager",
    "IWdsTransportConfigurationManager2",
    "IWdsTransportContent",
    "IWdsTransportContentProvider",
    "IWdsTransportDiagnosticsPolicy",
    "IWdsTransportManager",
    "IWdsTransportMulticastSessionPolicy",
    "IWdsTransportNamespace",
    "IWdsTransportNamespaceAutoCast",
    "IWdsTransportNamespaceManager",
    "IWdsTransportNamespaceScheduledCast",
    "IWdsTransportNamespaceScheduledCastAutoStart",
    "IWdsTransportNamespaceScheduledCastManualStart",
    "IWdsTransportServer",
    "IWdsTransportServer2",
    "IWdsTransportServicePolicy",
    "IWdsTransportServicePolicy2",
    "IWdsTransportSession",
    "IWdsTransportSetupManager",
    "IWdsTransportSetupManager2",
    "IWdsTransportTftpClient",
    "IWdsTransportTftpManager",
    "MC_SERVER_CURRENT_VERSION",
    "PFN_WDS_CLI_CALLBACK_MESSAGE_ID",
    "PFN_WdsCliCallback",
    "PFN_WdsCliTraceFunction",
    "PFN_WdsTransportClientReceiveContents",
    "PFN_WdsTransportClientReceiveMetadata",
    "PFN_WdsTransportClientSessionComplete",
    "PFN_WdsTransportClientSessionNegotiate",
    "PFN_WdsTransportClientSessionStart",
    "PFN_WdsTransportClientSessionStartEx",
    "PXE_ADDRESS",
    "PXE_ADDR_BROADCAST",
    "PXE_ADDR_USE_ADDR",
    "PXE_ADDR_USE_DHCP_RULES",
    "PXE_ADDR_USE_PORT",
    "PXE_BA_CUSTOM",
    "PXE_BA_IGNORE",
    "PXE_BA_NBP",
    "PXE_BA_REJECTED",
    "PXE_CALLBACK_MAX",
    "PXE_CALLBACK_RECV_REQUEST",
    "PXE_CALLBACK_SERVICE_CONTROL",
    "PXE_CALLBACK_SHUTDOWN",
    "PXE_DHCPV6_CLIENT_PORT",
    "PXE_DHCPV6_MESSAGE",
    "PXE_DHCPV6_MESSAGE_HEADER",
    "PXE_DHCPV6_NESTED_RELAY_MESSAGE",
    "PXE_DHCPV6_OPTION",
    "PXE_DHCPV6_RELAY_HOP_COUNT_LIMIT",
    "PXE_DHCPV6_RELAY_MESSAGE",
    "PXE_DHCPV6_SERVER_PORT",
    "PXE_DHCP_CLIENT_PORT",
    "PXE_DHCP_FILE_SIZE",
    "PXE_DHCP_HWAADR_SIZE",
    "PXE_DHCP_MAGIC_COOKIE_SIZE",
    "PXE_DHCP_MESSAGE",
    "PXE_DHCP_OPTION",
    "PXE_DHCP_SERVER_PORT",
    "PXE_DHCP_SERVER_SIZE",
    "PXE_GSI_SERVER_DUID",
    "PXE_GSI_TRACE_ENABLED",
    "PXE_MAX_ADDRESS",
    "PXE_PROVIDER",
    "PXE_PROV_ATTR_FILTER",
    "PXE_PROV_ATTR_FILTER_IPV6",
    "PXE_PROV_ATTR_IPV6_CAPABLE",
    "PXE_PROV_FILTER_ALL",
    "PXE_PROV_FILTER_DHCP_ONLY",
    "PXE_PROV_FILTER_PXE_ONLY",
    "PXE_REG_INDEX_BOTTOM",
    "PXE_REG_INDEX_TOP",
    "PXE_SERVER_PORT",
    "PXE_TRACE_ERROR",
    "PXE_TRACE_FATAL",
    "PXE_TRACE_INFO",
    "PXE_TRACE_VERBOSE",
    "PXE_TRACE_WARNING",
    "PxeAsyncRecvDone",
    "PxeDhcpAppendOption",
    "PxeDhcpAppendOptionRaw",
    "PxeDhcpGetOptionValue",
    "PxeDhcpGetVendorOptionValue",
    "PxeDhcpInitialize",
    "PxeDhcpIsValid",
    "PxeDhcpv6AppendOption",
    "PxeDhcpv6AppendOptionRaw",
    "PxeDhcpv6CreateRelayRepl",
    "PxeDhcpv6GetOptionValue",
    "PxeDhcpv6GetVendorOptionValue",
    "PxeDhcpv6Initialize",
    "PxeDhcpv6IsValid",
    "PxeDhcpv6ParseRelayForw",
    "PxeGetServerInfo",
    "PxeGetServerInfoEx",
    "PxePacketAllocate",
    "PxePacketFree",
    "PxeProviderEnumClose",
    "PxeProviderEnumFirst",
    "PxeProviderEnumNext",
    "PxeProviderFreeInfo",
    "PxeProviderQueryIndex",
    "PxeProviderRegister",
    "PxeProviderSetAttribute",
    "PxeProviderUnRegister",
    "PxeRegisterCallback",
    "PxeSendReply",
    "PxeTrace",
    "PxeTraceV",
    "TRANSPORTCLIENT_CALLBACK_ID",
    "TRANSPORTCLIENT_SESSION_INFO",
    "TRANSPORTPROVIDER_CALLBACK_ID",
    "TRANSPORTPROVIDER_CURRENT_VERSION",
    "WDSBP_OPTVAL_ACTION_ABORT",
    "WDSBP_OPTVAL_ACTION_APPROVAL",
    "WDSBP_OPTVAL_ACTION_REFERRAL",
    "WDSBP_OPTVAL_NBP_VER_7",
    "WDSBP_OPTVAL_NBP_VER_8",
    "WDSBP_OPTVAL_PXE_PROMPT_NOPROMPT",
    "WDSBP_OPTVAL_PXE_PROMPT_OPTIN",
    "WDSBP_OPTVAL_PXE_PROMPT_OPTOUT",
    "WDSBP_OPT_TYPE_BYTE",
    "WDSBP_OPT_TYPE_IP4",
    "WDSBP_OPT_TYPE_IP6",
    "WDSBP_OPT_TYPE_NONE",
    "WDSBP_OPT_TYPE_STR",
    "WDSBP_OPT_TYPE_ULONG",
    "WDSBP_OPT_TYPE_USHORT",
    "WDSBP_OPT_TYPE_WSTR",
    "WDSBP_PK_TYPE_BCD",
    "WDSBP_PK_TYPE_DHCP",
    "WDSBP_PK_TYPE_DHCPV6",
    "WDSBP_PK_TYPE_WDSNBP",
    "WDSMCCLIENT_CATEGORY",
    "WDSMCSERVER_CATEGORY",
    "WDSMCS_E_CLIENT_DOESNOT_SUPPORT_SECURITY_MODE",
    "WDSMCS_E_CLIENT_NOT_FOUND",
    "WDSMCS_E_CONTENT_NOT_FOUND",
    "WDSMCS_E_CONTENT_PROVIDER_NOT_FOUND",
    "WDSMCS_E_INCOMPATIBLE_VERSION",
    "WDSMCS_E_NAMESPACE_ALREADY_EXISTS",
    "WDSMCS_E_NAMESPACE_ALREADY_STARTED",
    "WDSMCS_E_NAMESPACE_NOT_FOUND",
    "WDSMCS_E_NAMESPACE_SHUTDOWN_IN_PROGRESS",
    "WDSMCS_E_NS_START_FAILED_NO_CLIENTS",
    "WDSMCS_E_PACKET_HAS_SECURITY",
    "WDSMCS_E_PACKET_NOT_CHECKSUMED",
    "WDSMCS_E_PACKET_NOT_HASHED",
    "WDSMCS_E_PACKET_NOT_SIGNED",
    "WDSMCS_E_REQCALLBACKS_NOT_REG",
    "WDSMCS_E_SESSION_SHUTDOWN_IN_PROGRESS",
    "WDSMCS_E_START_TIME_IN_PAST",
    "WDSTPC_E_ALREADY_COMPLETED",
    "WDSTPC_E_ALREADY_IN_LOWEST_SESSION",
    "WDSTPC_E_ALREADY_IN_PROGRESS",
    "WDSTPC_E_CALLBACKS_NOT_REG",
    "WDSTPC_E_CLIENT_DEMOTE_NOT_SUPPORTED",
    "WDSTPC_E_KICKED_FAIL",
    "WDSTPC_E_KICKED_FALLBACK",
    "WDSTPC_E_KICKED_POLICY_NOT_MET",
    "WDSTPC_E_KICKED_UNKNOWN",
    "WDSTPC_E_MULTISTREAM_NOT_ENABLED",
    "WDSTPC_E_NOT_INITIALIZED",
    "WDSTPC_E_NO_IP4_INTERFACE",
    "WDSTPC_E_UNKNOWN_ERROR",
    "WDSTPTC_E_WIM_APPLY_REQUIRES_REFERENCE_IMAGE",
    "WDSTPTMGMT_CATEGORY",
    "WDSTPTMGMT_E_CANNOT_REFRESH_DIRTY_OBJECT",
    "WDSTPTMGMT_E_CANNOT_REINITIALIZE_OBJECT",
    "WDSTPTMGMT_E_CONTENT_PROVIDER_ALREADY_REGISTERED",
    "WDSTPTMGMT_E_CONTENT_PROVIDER_NOT_REGISTERED",
    "WDSTPTMGMT_E_INVALID_AUTO_DISCONNECT_THRESHOLD",
    "WDSTPTMGMT_E_INVALID_CLASS",
    "WDSTPTMGMT_E_INVALID_CONTENT_PROVIDER_NAME",
    "WDSTPTMGMT_E_INVALID_DIAGNOSTICS_COMPONENTS",
    "WDSTPTMGMT_E_INVALID_IPV4_MULTICAST_ADDRESS",
    "WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS",
    "WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS_SOURCE",
    "WDSTPTMGMT_E_INVALID_IP_ADDRESS",
    "WDSTPTMGMT_E_INVALID_MULTISTREAM_STREAM_COUNT",
    "WDSTPTMGMT_E_INVALID_NAMESPACE_DATA",
    "WDSTPTMGMT_E_INVALID_NAMESPACE_NAME",
    "WDSTPTMGMT_E_INVALID_NAMESPACE_START_PARAMETERS",
    "WDSTPTMGMT_E_INVALID_NAMESPACE_START_TIME",
    "WDSTPTMGMT_E_INVALID_OPERATION",
    "WDSTPTMGMT_E_INVALID_PROPERTY",
    "WDSTPTMGMT_E_INVALID_SERVICE_IP_ADDRESS_RANGE",
    "WDSTPTMGMT_E_INVALID_SERVICE_PORT_RANGE",
    "WDSTPTMGMT_E_INVALID_SLOW_CLIENT_HANDLING_TYPE",
    "WDSTPTMGMT_E_INVALID_TFTP_MAX_BLOCKSIZE",
    "WDSTPTMGMT_E_IPV6_NOT_SUPPORTED",
    "WDSTPTMGMT_E_MULTICAST_SESSION_POLICY_NOT_SUPPORTED",
    "WDSTPTMGMT_E_NAMESPACE_ALREADY_REGISTERED",
    "WDSTPTMGMT_E_NAMESPACE_NOT_ON_SERVER",
    "WDSTPTMGMT_E_NAMESPACE_NOT_REGISTERED",
    "WDSTPTMGMT_E_NAMESPACE_READ_ONLY",
    "WDSTPTMGMT_E_NAMESPACE_REMOVED_FROM_SERVER",
    "WDSTPTMGMT_E_NETWORK_PROFILES_NOT_SUPPORTED",
    "WDSTPTMGMT_E_TFTP_MAX_BLOCKSIZE_NOT_SUPPORTED",
    "WDSTPTMGMT_E_TFTP_VAR_WINDOW_NOT_SUPPORTED",
    "WDSTPTMGMT_E_TRANSPORT_SERVER_ROLE_NOT_CONFIGURED",
    "WDSTPTMGMT_E_TRANSPORT_SERVER_UNAVAILABLE",
    "WDSTPTMGMT_E_UDP_PORT_POLICY_NOT_SUPPORTED",
    "WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS",
    "WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentImageServer",
    "WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentMulticast",
    "WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentPxe",
    "WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentTftp",
    "WDSTRANSPORT_DISCONNECT_TYPE",
    "WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectAbort",
    "WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectFallback",
    "WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectUnknown",
    "WDSTRANSPORT_FEATURE_FLAGS",
    "WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureAdminPack",
    "WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureDeploymentServer",
    "WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureTransportServer",
    "WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE",
    "WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceDhcp",
    "WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceRange",
    "WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceUnknown",
    "WDSTRANSPORT_IP_ADDRESS_TYPE",
    "WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv4",
    "WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv6",
    "WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressUnknown",
    "WDSTRANSPORT_NAMESPACE_TYPE",
    "WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeAutoCast",
    "WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastAutoStart",
    "WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastManualStart",
    "WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeUnknown",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile100Mbps",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile10Mbps",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile1Gbps",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileCustom",
    "WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileUnknown",
    "WDSTRANSPORT_PROTOCOL_FLAGS",
    "WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolMulticast",
    "WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolUnicast",
    "WDSTRANSPORT_RESOURCE_UTILIZATION_UNKNOWN",
    "WDSTRANSPORT_SERVICE_NOTIFICATION",
    "WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyReadSettings",
    "WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyUnknown",
    "WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE",
    "WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingAutoDisconnect",
    "WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingMultistream",
    "WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingNone",
    "WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingUnknown",
    "WDSTRANSPORT_TFTP_CAPABILITY",
    "WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapMaximumBlockSize",
    "WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapVariableWindow",
    "WDSTRANSPORT_UDP_PORT_POLICY",
    "WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyDynamic",
    "WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyFixed",
    "WDS_CLI_CRED",
    "WDS_CLI_FIRMWARE_BIOS",
    "WDS_CLI_FIRMWARE_EFI",
    "WDS_CLI_FIRMWARE_TYPE",
    "WDS_CLI_FIRMWARE_UNKNOWN",
    "WDS_CLI_IMAGE_PARAM_SPARSE_FILE",
    "WDS_CLI_IMAGE_PARAM_SUPPORTED_FIRMWARES",
    "WDS_CLI_IMAGE_PARAM_TYPE",
    "WDS_CLI_IMAGE_PARAM_UNKNOWN",
    "WDS_CLI_IMAGE_TYPE",
    "WDS_CLI_IMAGE_TYPE_UNKNOWN",
    "WDS_CLI_IMAGE_TYPE_VHD",
    "WDS_CLI_IMAGE_TYPE_VHDX",
    "WDS_CLI_IMAGE_TYPE_WIM",
    "WDS_CLI_MSG_COMPLETE",
    "WDS_CLI_MSG_PROGRESS",
    "WDS_CLI_MSG_START",
    "WDS_CLI_MSG_TEXT",
    "WDS_CLI_NO_SPARSE_FILE",
    "WDS_CLI_TRANSFER_ASYNCHRONOUS",
    "WDS_LOG_LEVEL_DISABLED",
    "WDS_LOG_LEVEL_ERROR",
    "WDS_LOG_LEVEL_INFO",
    "WDS_LOG_LEVEL_WARNING",
    "WDS_LOG_TYPE_CLIENT_APPLY_FINISHED",
    "WDS_LOG_TYPE_CLIENT_APPLY_FINISHED_2",
    "WDS_LOG_TYPE_CLIENT_APPLY_STARTED",
    "WDS_LOG_TYPE_CLIENT_APPLY_STARTED_2",
    "WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR",
    "WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR_2",
    "WDS_LOG_TYPE_CLIENT_DRIVER_PACKAGE_NOT_ACCESSIBLE",
    "WDS_LOG_TYPE_CLIENT_ERROR",
    "WDS_LOG_TYPE_CLIENT_FINISHED",
    "WDS_LOG_TYPE_CLIENT_GENERIC_MESSAGE",
    "WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED",
    "WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED2",
    "WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED3",
    "WDS_LOG_TYPE_CLIENT_MAX_CODE",
    "WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_END",
    "WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_FAILURE",
    "WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_START",
    "WDS_LOG_TYPE_CLIENT_POST_ACTIONS_END",
    "WDS_LOG_TYPE_CLIENT_POST_ACTIONS_START",
    "WDS_LOG_TYPE_CLIENT_STARTED",
    "WDS_LOG_TYPE_CLIENT_TRANSFER_DOWNGRADE",
    "WDS_LOG_TYPE_CLIENT_TRANSFER_END",
    "WDS_LOG_TYPE_CLIENT_TRANSFER_START",
    "WDS_LOG_TYPE_CLIENT_UNATTEND_MODE",
    "WDS_MC_TRACE_ERROR",
    "WDS_MC_TRACE_FATAL",
    "WDS_MC_TRACE_INFO",
    "WDS_MC_TRACE_VERBOSE",
    "WDS_MC_TRACE_WARNING",
    "WDS_TRANSPORTCLIENT_AUTH",
    "WDS_TRANSPORTCLIENT_CALLBACKS",
    "WDS_TRANSPORTCLIENT_CURRENT_API_VERSION",
    "WDS_TRANSPORTCLIENT_MAX_CALLBACKS",
    "WDS_TRANSPORTCLIENT_NO_AUTH",
    "WDS_TRANSPORTCLIENT_NO_CACHE",
    "WDS_TRANSPORTCLIENT_PROTOCOL_MULTICAST",
    "WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS",
    "WDS_TRANSPORTCLIENT_RECEIVE_METADATA",
    "WDS_TRANSPORTCLIENT_REQUEST",
    "WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL",
    "WDS_TRANSPORTCLIENT_SESSION_COMPLETE",
    "WDS_TRANSPORTCLIENT_SESSION_NEGOTIATE",
    "WDS_TRANSPORTCLIENT_SESSION_START",
    "WDS_TRANSPORTCLIENT_SESSION_STARTEX",
    "WDS_TRANSPORTCLIENT_STATUS_FAILURE",
    "WDS_TRANSPORTCLIENT_STATUS_IN_PROGRESS",
    "WDS_TRANSPORTCLIENT_STATUS_SUCCESS",
    "WDS_TRANSPORTPROVIDER_CLOSE_CONTENT",
    "WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE",
    "WDS_TRANSPORTPROVIDER_COMPARE_CONTENT",
    "WDS_TRANSPORTPROVIDER_CREATE_INSTANCE",
    "WDS_TRANSPORTPROVIDER_DUMP_STATE",
    "WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA",
    "WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE",
    "WDS_TRANSPORTPROVIDER_INIT_PARAMS",
    "WDS_TRANSPORTPROVIDER_MAX_CALLBACKS",
    "WDS_TRANSPORTPROVIDER_OPEN_CONTENT",
    "WDS_TRANSPORTPROVIDER_READ_CONTENT",
    "WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS",
    "WDS_TRANSPORTPROVIDER_SETTINGS",
    "WDS_TRANSPORTPROVIDER_SHUTDOWN",
    "WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK",
    "WdsBpAddOption",
    "WdsBpCloseHandle",
    "WdsBpGetOptionBuffer",
    "WdsBpInitialize",
    "WdsBpParseInitialize",
    "WdsBpParseInitializev6",
    "WdsBpQueryOption",
    "WdsCliAuthorizeSession",
    "WdsCliCancelTransfer",
    "WdsCliClose",
    "WdsCliCreateSession",
    "WdsCliFindFirstImage",
    "WdsCliFindNextImage",
    "WdsCliFlagEnumFilterFirmware",
    "WdsCliFlagEnumFilterVersion",
    "WdsCliFreeStringArray",
    "WdsCliGetDriverQueryXml",
    "WdsCliGetEnumerationFlags",
    "WdsCliGetImageArchitecture",
    "WdsCliGetImageDescription",
    "WdsCliGetImageFiles",
    "WdsCliGetImageGroup",
    "WdsCliGetImageHalName",
    "WdsCliGetImageHandleFromFindHandle",
    "WdsCliGetImageHandleFromTransferHandle",
    "WdsCliGetImageIndex",
    "WdsCliGetImageLanguage",
    "WdsCliGetImageLanguages",
    "WdsCliGetImageLastModifiedTime",
    "WdsCliGetImageName",
    "WdsCliGetImageNamespace",
    "WdsCliGetImageParameter",
    "WdsCliGetImagePath",
    "WdsCliGetImageSize",
    "WdsCliGetImageType",
    "WdsCliGetImageVersion",
    "WdsCliGetTransferSize",
    "WdsCliInitializeLog",
    "WdsCliLog",
    "WdsCliObtainDriverPackages",
    "WdsCliObtainDriverPackagesEx",
    "WdsCliRegisterTrace",
    "WdsCliSetTransferBufferSize",
    "WdsCliTransferFile",
    "WdsCliTransferImage",
    "WdsCliWaitForTransfer",
    "WdsTransportCacheable",
    "WdsTransportClient",
    "WdsTransportClientAddRefBuffer",
    "WdsTransportClientCancelSession",
    "WdsTransportClientCancelSessionEx",
    "WdsTransportClientCloseSession",
    "WdsTransportClientCompleteReceive",
    "WdsTransportClientInitialize",
    "WdsTransportClientInitializeSession",
    "WdsTransportClientQueryStatus",
    "WdsTransportClientRegisterCallback",
    "WdsTransportClientReleaseBuffer",
    "WdsTransportClientShutdown",
    "WdsTransportClientStartSession",
    "WdsTransportClientWaitForCompletion",
    "WdsTransportCollection",
    "WdsTransportConfigurationManager",
    "WdsTransportContent",
    "WdsTransportContentProvider",
    "WdsTransportDiagnosticsPolicy",
    "WdsTransportManager",
    "WdsTransportMulticastSessionPolicy",
    "WdsTransportNamespace",
    "WdsTransportNamespaceAutoCast",
    "WdsTransportNamespaceManager",
    "WdsTransportNamespaceScheduledCast",
    "WdsTransportNamespaceScheduledCastAutoStart",
    "WdsTransportNamespaceScheduledCastManualStart",
    "WdsTransportServer",
    "WdsTransportServerAllocateBuffer",
    "WdsTransportServerCompleteRead",
    "WdsTransportServerFreeBuffer",
    "WdsTransportServerRegisterCallback",
    "WdsTransportServerTrace",
    "WdsTransportServerTraceV",
    "WdsTransportServicePolicy",
    "WdsTransportSession",
    "WdsTransportSetupManager",
    "WdsTransportTftpClient",
    "WdsTransportTftpManager",
]
