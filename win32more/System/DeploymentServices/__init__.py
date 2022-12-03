from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.DeploymentServices
import win32more.System.Registry
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WDS_CLI_TRANSFER_ASYNCHRONOUS = 1
WDS_CLI_NO_SPARSE_FILE = 2
PXE_DHCP_SERVER_PORT = 67
PXE_DHCP_CLIENT_PORT = 68
PXE_SERVER_PORT = 4011
PXE_DHCPV6_SERVER_PORT = 547
PXE_DHCPV6_CLIENT_PORT = 546
PXE_DHCP_FILE_SIZE = 128
PXE_DHCP_SERVER_SIZE = 64
PXE_DHCP_HWAADR_SIZE = 16
PXE_DHCP_MAGIC_COOKIE_SIZE = 4
PXE_REG_INDEX_TOP = 0
PXE_REG_INDEX_BOTTOM = 4294967295
PXE_CALLBACK_RECV_REQUEST = 0
PXE_CALLBACK_SHUTDOWN = 1
PXE_CALLBACK_SERVICE_CONTROL = 2
PXE_CALLBACK_MAX = 3
PXE_GSI_TRACE_ENABLED = 1
PXE_GSI_SERVER_DUID = 2
PXE_MAX_ADDRESS = 16
PXE_ADDR_BROADCAST = 1
PXE_ADDR_USE_PORT = 2
PXE_ADDR_USE_ADDR = 4
PXE_ADDR_USE_DHCP_RULES = 8
PXE_DHCPV6_RELAY_HOP_COUNT_LIMIT = 32
PXE_BA_NBP = 1
PXE_BA_CUSTOM = 2
PXE_BA_IGNORE = 3
PXE_BA_REJECTED = 4
PXE_TRACE_VERBOSE = 65536
PXE_TRACE_INFO = 131072
PXE_TRACE_WARNING = 262144
PXE_TRACE_ERROR = 524288
PXE_TRACE_FATAL = 1048576
PXE_PROV_ATTR_FILTER = 0
PXE_PROV_ATTR_FILTER_IPV6 = 1
PXE_PROV_ATTR_IPV6_CAPABLE = 2
PXE_PROV_FILTER_ALL = 0
PXE_PROV_FILTER_DHCP_ONLY = 1
PXE_PROV_FILTER_PXE_ONLY = 2
MC_SERVER_CURRENT_VERSION = 1
TRANSPORTPROVIDER_CURRENT_VERSION = 1
WDS_MC_TRACE_VERBOSE = 65536
WDS_MC_TRACE_INFO = 131072
WDS_MC_TRACE_WARNING = 262144
WDS_MC_TRACE_ERROR = 524288
WDS_MC_TRACE_FATAL = 1048576
WDS_TRANSPORTCLIENT_CURRENT_API_VERSION = 1
WDS_TRANSPORTCLIENT_PROTOCOL_MULTICAST = 1
WDS_TRANSPORTCLIENT_NO_CACHE = 0
WDS_TRANSPORTCLIENT_STATUS_IN_PROGRESS = 1
WDS_TRANSPORTCLIENT_STATUS_SUCCESS = 2
WDS_TRANSPORTCLIENT_STATUS_FAILURE = 3
WDSTRANSPORT_RESOURCE_UTILIZATION_UNKNOWN = 255
WDSBP_PK_TYPE_DHCP = 1
WDSBP_PK_TYPE_WDSNBP = 2
WDSBP_PK_TYPE_BCD = 4
WDSBP_PK_TYPE_DHCPV6 = 8
WDSBP_OPT_TYPE_NONE = 0
WDSBP_OPT_TYPE_BYTE = 1
WDSBP_OPT_TYPE_USHORT = 2
WDSBP_OPT_TYPE_ULONG = 3
WDSBP_OPT_TYPE_WSTR = 4
WDSBP_OPT_TYPE_STR = 5
WDSBP_OPT_TYPE_IP4 = 6
WDSBP_OPT_TYPE_IP6 = 7
WDSBP_OPTVAL_ACTION_APPROVAL = 1
WDSBP_OPTVAL_ACTION_REFERRAL = 3
WDSBP_OPTVAL_ACTION_ABORT = 5
WDSBP_OPTVAL_PXE_PROMPT_OPTIN = 1
WDSBP_OPTVAL_PXE_PROMPT_NOPROMPT = 2
WDSBP_OPTVAL_PXE_PROMPT_OPTOUT = 3
WDSBP_OPTVAL_NBP_VER_7 = 1792
WDSBP_OPTVAL_NBP_VER_8 = 2048
FACILITY_WDSMCSERVER = 289
FACILITY_WDSMCCLIENT = 290
WDSMCSERVER_CATEGORY = 1
WDSMCCLIENT_CATEGORY = 2
WDSMCS_E_SESSION_SHUTDOWN_IN_PROGRESS = -1054801664
WDSMCS_E_REQCALLBACKS_NOT_REG = -1054801663
WDSMCS_E_INCOMPATIBLE_VERSION = -1054801662
WDSMCS_E_CONTENT_NOT_FOUND = -1054801661
WDSMCS_E_CLIENT_NOT_FOUND = -1054801660
WDSMCS_E_NAMESPACE_NOT_FOUND = -1054801659
WDSMCS_E_CONTENT_PROVIDER_NOT_FOUND = -1054801658
WDSMCS_E_NAMESPACE_ALREADY_EXISTS = -1054801657
WDSMCS_E_NAMESPACE_SHUTDOWN_IN_PROGRESS = -1054801656
WDSMCS_E_NAMESPACE_ALREADY_STARTED = -1054801655
WDSMCS_E_NS_START_FAILED_NO_CLIENTS = -1054801654
WDSMCS_E_START_TIME_IN_PAST = -1054801653
WDSMCS_E_PACKET_NOT_HASHED = -1054801652
WDSMCS_E_PACKET_NOT_SIGNED = -1054801651
WDSMCS_E_PACKET_HAS_SECURITY = -1054801650
WDSMCS_E_PACKET_NOT_CHECKSUMED = -1054801649
WDSMCS_E_CLIENT_DOESNOT_SUPPORT_SECURITY_MODE = -1054801648
EVT_WDSMCS_S_PARAMETERS_READ = 1092682240
EVT_WDSMCS_E_PARAMETERS_READ_FAILED = -1054801407
EVT_WDSMCS_E_DUPLICATE_MULTICAST_ADDR = -1054801406
EVT_WDSMCS_E_NON_WDS_DUPLICATE_MULTICAST_ADDR = -1054801405
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED = -1054801328
EVT_WDSMCS_E_CP_INIT_FUNC_MISSING = -1054801327
EVT_WDSMCS_E_CP_INIT_FUNC_FAILED = -1054801326
EVT_WDSMCS_E_CP_INCOMPATIBLE_SERVER_VERSION = -1054801325
EVT_WDSMCS_E_CP_CALLBACKS_NOT_REG = -1054801324
EVT_WDSMCS_E_CP_SHUTDOWN_FUNC_FAILED = -1054801323
EVT_WDSMCS_E_CP_MEMORY_LEAK = -1054801322
EVT_WDSMCS_E_CP_OPEN_INSTANCE_FAILED = -1054801321
EVT_WDSMCS_E_CP_CLOSE_INSTANCE_FAILED = -1054801320
EVT_WDSMCS_E_CP_OPEN_CONTENT_FAILED = -1054801319
EVT_WDSMCS_W_CP_DLL_LOAD_FAILED_NOT_CRITICAL = -2128543142
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED_CRITICAL = -1054801317
EVT_WDSMCS_E_NSREG_START_TIME_IN_PAST = -1054801152
EVT_WDSMCS_E_NSREG_CONTENT_PROVIDER_NOT_REG = -1054801151
EVT_WDSMCS_E_NSREG_NAMESPACE_EXISTS = -1054801150
EVT_WDSMCS_E_NSREG_FAILURE = -1054801149
WDSTPC_E_CALLBACKS_NOT_REG = -1054735616
WDSTPC_E_ALREADY_COMPLETED = -1054735615
WDSTPC_E_ALREADY_IN_PROGRESS = -1054735614
WDSTPC_E_UNKNOWN_ERROR = -1054735613
WDSTPC_E_NOT_INITIALIZED = -1054735612
WDSTPC_E_KICKED_POLICY_NOT_MET = -1054735611
WDSTPC_E_KICKED_FALLBACK = -1054735610
WDSTPC_E_KICKED_FAIL = -1054735609
WDSTPC_E_KICKED_UNKNOWN = -1054735608
WDSTPC_E_MULTISTREAM_NOT_ENABLED = -1054735607
WDSTPC_E_ALREADY_IN_LOWEST_SESSION = -1054735606
WDSTPC_E_CLIENT_DEMOTE_NOT_SUPPORTED = -1054735605
WDSTPC_E_NO_IP4_INTERFACE = -1054735604
WDSTPTC_E_WIM_APPLY_REQUIRES_REFERENCE_IMAGE = -1054735603
FACILITY_WDSTPTMGMT = 272
WDSTPTMGMT_CATEGORY = 1
WDSTPTMGMT_E_INVALID_PROPERTY = -1055915776
WDSTPTMGMT_E_INVALID_OPERATION = -1055915775
WDSTPTMGMT_E_INVALID_CLASS = -1055915774
WDSTPTMGMT_E_CONTENT_PROVIDER_ALREADY_REGISTERED = -1055915773
WDSTPTMGMT_E_CONTENT_PROVIDER_NOT_REGISTERED = -1055915772
WDSTPTMGMT_E_INVALID_CONTENT_PROVIDER_NAME = -1055915771
WDSTPTMGMT_E_TRANSPORT_SERVER_ROLE_NOT_CONFIGURED = -1055915770
WDSTPTMGMT_E_NAMESPACE_ALREADY_REGISTERED = -1055915769
WDSTPTMGMT_E_NAMESPACE_NOT_REGISTERED = -1055915768
WDSTPTMGMT_E_CANNOT_REINITIALIZE_OBJECT = -1055915767
WDSTPTMGMT_E_INVALID_NAMESPACE_NAME = -1055915766
WDSTPTMGMT_E_INVALID_NAMESPACE_DATA = -1055915765
WDSTPTMGMT_E_NAMESPACE_READ_ONLY = -1055915764
WDSTPTMGMT_E_INVALID_NAMESPACE_START_TIME = -1055915763
WDSTPTMGMT_E_INVALID_DIAGNOSTICS_COMPONENTS = -1055915762
WDSTPTMGMT_E_CANNOT_REFRESH_DIRTY_OBJECT = -1055915761
WDSTPTMGMT_E_INVALID_SERVICE_IP_ADDRESS_RANGE = -1055915760
WDSTPTMGMT_E_INVALID_SERVICE_PORT_RANGE = -1055915759
WDSTPTMGMT_E_INVALID_NAMESPACE_START_PARAMETERS = -1055915758
WDSTPTMGMT_E_TRANSPORT_SERVER_UNAVAILABLE = -1055915757
WDSTPTMGMT_E_NAMESPACE_NOT_ON_SERVER = -1055915756
WDSTPTMGMT_E_NAMESPACE_REMOVED_FROM_SERVER = -1055915755
WDSTPTMGMT_E_INVALID_IP_ADDRESS = -1055915754
WDSTPTMGMT_E_INVALID_IPV4_MULTICAST_ADDRESS = -1055915753
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS = -1055915752
WDSTPTMGMT_E_IPV6_NOT_SUPPORTED = -1055915751
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS_SOURCE = -1055915750
WDSTPTMGMT_E_INVALID_MULTISTREAM_STREAM_COUNT = -1055915749
WDSTPTMGMT_E_INVALID_AUTO_DISCONNECT_THRESHOLD = -1055915748
WDSTPTMGMT_E_MULTICAST_SESSION_POLICY_NOT_SUPPORTED = -1055915747
WDSTPTMGMT_E_INVALID_SLOW_CLIENT_HANDLING_TYPE = -1055915746
WDSTPTMGMT_E_NETWORK_PROFILES_NOT_SUPPORTED = -1055915745
WDSTPTMGMT_E_UDP_PORT_POLICY_NOT_SUPPORTED = -1055915744
WDSTPTMGMT_E_TFTP_MAX_BLOCKSIZE_NOT_SUPPORTED = -1055915743
WDSTPTMGMT_E_TFTP_VAR_WINDOW_NOT_SUPPORTED = -1055915742
WDSTPTMGMT_E_INVALID_TFTP_MAX_BLOCKSIZE = -1055915741
WdsCliFlagEnumFilterVersion = 1
WdsCliFlagEnumFilterFirmware = 2
WDS_LOG_TYPE_CLIENT_ERROR = 1
WDS_LOG_TYPE_CLIENT_STARTED = 2
WDS_LOG_TYPE_CLIENT_FINISHED = 3
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED = 4
WDS_LOG_TYPE_CLIENT_APPLY_STARTED = 5
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED = 6
WDS_LOG_TYPE_CLIENT_GENERIC_MESSAGE = 7
WDS_LOG_TYPE_CLIENT_UNATTEND_MODE = 8
WDS_LOG_TYPE_CLIENT_TRANSFER_START = 9
WDS_LOG_TYPE_CLIENT_TRANSFER_END = 10
WDS_LOG_TYPE_CLIENT_TRANSFER_DOWNGRADE = 11
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR = 12
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_START = 13
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_END = 14
WDS_LOG_TYPE_CLIENT_APPLY_STARTED_2 = 15
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED_2 = 16
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR_2 = 17
WDS_LOG_TYPE_CLIENT_DRIVER_PACKAGE_NOT_ACCESSIBLE = 18
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_START = 19
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_END = 20
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_FAILURE = 21
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED2 = 22
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED3 = 23
WDS_LOG_TYPE_CLIENT_MAX_CODE = 24
WDS_LOG_LEVEL_DISABLED = 0
WDS_LOG_LEVEL_ERROR = 1
WDS_LOG_LEVEL_WARNING = 2
WDS_LOG_LEVEL_INFO = 3
def _define_WdsCliClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WdsCliClose', windll['WDSCLIENTAPI.dll']), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliRegisterTrace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.PFN_WdsCliTraceFunction)(('WdsCliRegisterTrace', windll['WDSCLIENTAPI.dll']), ((1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliFreeStringArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32)(('WdsCliFreeStringArray', windll['WDSCLIENTAPI.dll']), ((1, 'ppwszArray'),(1, 'ulCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliFindFirstImage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE))(('WdsCliFindFirstImage', windll['WDSCLIENTAPI.dll']), ((1, 'hSession'),(1, 'phFindHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliFindNextImage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WdsCliFindNextImage', windll['WDSCLIENTAPI.dll']), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetEnumerationFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32))(('WdsCliGetEnumerationFlags', windll['WDSCLIENTAPI.dll']), ((1, 'Handle'),(1, 'pdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageHandleFromFindHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE))(('WdsCliGetImageHandleFromFindHandle', windll['WDSCLIENTAPI.dll']), ((1, 'FindHandle'),(1, 'phImageHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageHandleFromTransferHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE))(('WdsCliGetImageHandleFromTransferHandle', windll['WDSCLIENTAPI.dll']), ((1, 'hTransfer'),(1, 'phImageHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliCreateSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.DeploymentServices.WDS_CLI_CRED_head),POINTER(win32more.Foundation.HANDLE))(('WdsCliCreateSession', windll['WDSCLIENTAPI.dll']), ((1, 'pwszServer'),(1, 'pCred'),(1, 'phSession'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliAuthorizeSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.DeploymentServices.WDS_CLI_CRED_head))(('WdsCliAuthorizeSession', windll['WDSCLIENTAPI.dll']), ((1, 'hSession'),(1, 'pCred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliInitializeLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.System.DeploymentServices.CPU_ARCHITECTURE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('WdsCliInitializeLog', windll['WDSCLIENTAPI.dll']), ((1, 'hSession'),(1, 'ulClientArchitecture'),(1, 'pwszClientId'),(1, 'pwszClientAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliLog():
    try:
        return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,UInt32)(('WdsCliLog', cdll['WDSCLIENTAPI.dll']), ((1, 'hSession'),(1, 'ulLogLevel'),(1, 'ulMessageCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageName', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageDescription', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.DeploymentServices.WDS_CLI_IMAGE_TYPE))(('WdsCliGetImageType', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pImageType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(('WdsCliGetImageFiles', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pppwszFiles'),(1, 'pdwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageLanguage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageLanguage', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageLanguages():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(POINTER(POINTER(SByte))),POINTER(UInt32))(('WdsCliGetImageLanguages', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pppszValues'),(1, 'pdwNumValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageVersion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageVersion', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImagePath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImagePath', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32))(('WdsCliGetImageIndex', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pdwValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageArchitecture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.DeploymentServices.CPU_ARCHITECTURE))(('WdsCliGetImageArchitecture', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pdwValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageLastModifiedTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head)))(('WdsCliGetImageLastModifiedTime', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppSysTimeValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt64))(('WdsCliGetImageSize', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pullValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageHalName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageHalName', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageGroup():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageGroup', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetImageNamespace', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ppwszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetImageParameter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE,c_void_p,UInt32)(('WdsCliGetImageParameter', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'ParamType'),(1, 'pResponse'),(1, 'uResponseLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetTransferSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt64))(('WdsCliGetTransferSize', windll['WDSCLIENTAPI.dll']), ((1, 'hIfh'),(1, 'pullValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliSetTransferBufferSize():
    try:
        return WINFUNCTYPE(Void,UInt32)(('WdsCliSetTransferBufferSize', windll['WDSCLIENTAPI.dll']), ((1, 'ulSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliTransferImage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.System.DeploymentServices.PFN_WdsCliCallback,c_void_p,POINTER(win32more.Foundation.HANDLE))(('WdsCliTransferImage', windll['WDSCLIENTAPI.dll']), ((1, 'hImage'),(1, 'pwszLocalPath'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'pfnWdsCliCallback'),(1, 'pvUserData'),(1, 'phTransfer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliTransferFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.System.DeploymentServices.PFN_WdsCliCallback,c_void_p,POINTER(win32more.Foundation.HANDLE))(('WdsCliTransferFile', windll['WDSCLIENTAPI.dll']), ((1, 'pwszServer'),(1, 'pwszNamespace'),(1, 'pwszRemoteFilePath'),(1, 'pwszLocalFilePath'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'pfnWdsCliCallback'),(1, 'pvUserData'),(1, 'phTransfer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliCancelTransfer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WdsCliCancelTransfer', windll['WDSCLIENTAPI.dll']), ((1, 'hTransfer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliWaitForTransfer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('WdsCliWaitForTransfer', windll['WDSCLIENTAPI.dll']), ((1, 'hTransfer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliObtainDriverPackages():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(('WdsCliObtainDriverPackages', windll['WDSCLIENTAPI.dll']), ((1, 'hImage'),(1, 'ppwszServerName'),(1, 'pppwszDriverPackages'),(1, 'pulCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliObtainDriverPackagesEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(('WdsCliObtainDriverPackagesEx', windll['WDSCLIENTAPI.dll']), ((1, 'hSession'),(1, 'pwszMachineInfo'),(1, 'ppwszServerName'),(1, 'pppwszDriverPackages'),(1, 'pulCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsCliGetDriverQueryXml():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('WdsCliGetDriverQueryXml', windll['WDSCLIENTAPI.dll']), ((1, 'pwszWinDirPath'),(1, 'ppwszDriverQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderRegister():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,POINTER(win32more.System.Registry.HKEY))(('PxeProviderRegister', windll['WDSPXE.dll']), ((1, 'pszProviderName'),(1, 'pszModulePath'),(1, 'Index'),(1, 'bIsCritical'),(1, 'phProviderKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderUnRegister():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR)(('PxeProviderUnRegister', windll['WDSPXE.dll']), ((1, 'pszProviderName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderQueryIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('PxeProviderQueryIndex', windll['WDSPXE.dll']), ((1, 'pszProviderName'),(1, 'puIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderEnumFirst():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE))(('PxeProviderEnumFirst', windll['WDSPXE.dll']), ((1, 'phEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderEnumNext():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.System.DeploymentServices.PXE_PROVIDER_head)))(('PxeProviderEnumNext', windll['WDSPXE.dll']), ((1, 'hEnum'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderEnumClose():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('PxeProviderEnumClose', windll['WDSPXE.dll']), ((1, 'hEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderFreeInfo():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.DeploymentServices.PXE_PROVIDER_head))(('PxeProviderFreeInfo', windll['WDSPXE.dll']), ((1, 'pProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeRegisterCallback():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,c_void_p,c_void_p)(('PxeRegisterCallback', windll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'CallbackType'),(1, 'pCallbackFunction'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeSendReply():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(win32more.System.DeploymentServices.PXE_ADDRESS_head))(('PxeSendReply', windll['WDSPXE.dll']), ((1, 'hClientRequest'),(1, 'pPacket'),(1, 'uPacketLen'),(1, 'pAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeAsyncRecvDone():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32)(('PxeAsyncRecvDone', windll['WDSPXE.dll']), ((1, 'hClientRequest'),(1, 'Action'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeTrace():
    try:
        return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR)(('PxeTrace', cdll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'Severity'),(1, 'pszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeTraceV():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,POINTER(SByte))(('PxeTraceV', windll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'Severity'),(1, 'pszFormat'),(1, 'Params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxePacketAllocate():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32)(('PxePacketAllocate', windll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'hClientRequest'),(1, 'uSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxePacketFree():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_void_p)(('PxePacketFree', windll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'hClientRequest'),(1, 'pPacket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeProviderSetAttribute():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,c_void_p,UInt32)(('PxeProviderSetAttribute', windll['WDSPXE.dll']), ((1, 'hProvider'),(1, 'Attribute'),(1, 'pParameterBuffer'),(1, 'uParamLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpInitialize():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(('PxeDhcpInitialize', windll['WDSPXE.dll']), ((1, 'pRecvPacket'),(1, 'uRecvPacketLen'),(1, 'pReplyPacket'),(1, 'uMaxReplyPacketLen'),(1, 'puReplyPacketLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6Initialize():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32))(('PxeDhcpv6Initialize', windll['WDSPXE.dll']), ((1, 'pRequest'),(1, 'cbRequest'),(1, 'pReply'),(1, 'cbReply'),(1, 'pcbReplyUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpAppendOption():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(UInt32),Byte,Byte,c_void_p)(('PxeDhcpAppendOption', windll['WDSPXE.dll']), ((1, 'pReplyPacket'),(1, 'uMaxReplyPacketLen'),(1, 'puReplyPacketLen'),(1, 'bOption'),(1, 'bOptionLen'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6AppendOption():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(UInt32),UInt16,UInt16,c_void_p)(('PxeDhcpv6AppendOption', windll['WDSPXE.dll']), ((1, 'pReply'),(1, 'cbReply'),(1, 'pcbReplyUsed'),(1, 'wOptionType'),(1, 'cbOption'),(1, 'pOption'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpAppendOptionRaw():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(UInt32),UInt16,c_void_p)(('PxeDhcpAppendOptionRaw', windll['WDSPXE.dll']), ((1, 'pReplyPacket'),(1, 'uMaxReplyPacketLen'),(1, 'puReplyPacketLen'),(1, 'uBufferLen'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6AppendOptionRaw():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(UInt32),UInt16,c_void_p)(('PxeDhcpv6AppendOptionRaw', windll['WDSPXE.dll']), ((1, 'pReply'),(1, 'cbReply'),(1, 'pcbReplyUsed'),(1, 'cbBuffer'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpIsValid():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL))(('PxeDhcpIsValid', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'bRequestPacket'),(1, 'pbPxeOptionPresent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6IsValid():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL))(('PxeDhcpv6IsValid', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'bRequestPacket'),(1, 'pbPxeOptionPresent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpGetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt32,Byte,c_char_p_no,POINTER(c_void_p))(('PxeDhcpGetOptionValue', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'uInstance'),(1, 'bOption'),(1, 'pbOptionLen'),(1, 'ppOptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6GetOptionValue():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt32,UInt16,POINTER(UInt16),POINTER(c_void_p))(('PxeDhcpv6GetOptionValue', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'uInstance'),(1, 'wOption'),(1, 'pwOptionLen'),(1, 'ppOptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpGetVendorOptionValue():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,Byte,UInt32,c_char_p_no,POINTER(c_void_p))(('PxeDhcpGetVendorOptionValue', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'bOption'),(1, 'uInstance'),(1, 'pbOptionLen'),(1, 'ppOptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6GetVendorOptionValue():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt32,UInt16,UInt32,POINTER(UInt16),POINTER(c_void_p))(('PxeDhcpv6GetVendorOptionValue', windll['WDSPXE.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'dwEnterpriseNumber'),(1, 'wOption'),(1, 'uInstance'),(1, 'pwOptionLen'),(1, 'ppOptionValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6ParseRelayForw():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head),UInt32,POINTER(UInt32),POINTER(c_char_p_no),POINTER(UInt32))(('PxeDhcpv6ParseRelayForw', windll['WDSPXE.dll']), ((1, 'pRelayForwPacket'),(1, 'uRelayForwPacketLen'),(1, 'pRelayMessages'),(1, 'nRelayMessages'),(1, 'pnRelayMessages'),(1, 'ppInnerPacket'),(1, 'pcbInnerPacket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeDhcpv6CreateRelayRepl():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head),UInt32,c_char_p_no,UInt32,c_void_p,UInt32,POINTER(UInt32))(('PxeDhcpv6CreateRelayRepl', windll['WDSPXE.dll']), ((1, 'pRelayMessages'),(1, 'nRelayMessages'),(1, 'pInnerPacket'),(1, 'cbInnerPacket'),(1, 'pReplyBuffer'),(1, 'cbReplyBuffer'),(1, 'pcbReplyBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeGetServerInfo():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,UInt32)(('PxeGetServerInfo', windll['WDSPXE.dll']), ((1, 'uInfoType'),(1, 'pBuffer'),(1, 'uBufferLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PxeGetServerInfoEx():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,UInt32,POINTER(UInt32))(('PxeGetServerInfoEx', windll['WDSPXE.dll']), ((1, 'uInfoType'),(1, 'pBuffer'),(1, 'uBufferLen'),(1, 'puBufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerRegisterCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID,c_void_p)(('WdsTransportServerRegisterCallback', windll['WDSMC.dll']), ((1, 'hProvider'),(1, 'CallbackId'),(1, 'pfnCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerCompleteRead():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,c_void_p,win32more.Foundation.HRESULT)(('WdsTransportServerCompleteRead', windll['WDSMC.dll']), ((1, 'hProvider'),(1, 'ulBytesRead'),(1, 'pvUserData'),(1, 'hReadResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerTrace():
    try:
        return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR)(('WdsTransportServerTrace', cdll['WDSMC.dll']), ((1, 'hProvider'),(1, 'Severity'),(1, 'pwszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerTraceV():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,POINTER(SByte))(('WdsTransportServerTraceV', windll['WDSMC.dll']), ((1, 'hProvider'),(1, 'Severity'),(1, 'pwszFormat'),(1, 'Params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerAllocateBuffer():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,UInt32)(('WdsTransportServerAllocateBuffer', windll['WDSMC.dll']), ((1, 'hProvider'),(1, 'ulBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportServerFreeBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,c_void_p)(('WdsTransportServerFreeBuffer', windll['WDSMC.dll']), ((1, 'hProvider'),(1, 'pvBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientInitialize():
    try:
        return WINFUNCTYPE(UInt32,)(('WdsTransportClientInitialize', windll['WDSTPTC.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientInitializeSession():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_head),c_void_p,POINTER(win32more.Foundation.HANDLE))(('WdsTransportClientInitializeSession', windll['WDSTPTC.dll']), ((1, 'pSessionRequest'),(1, 'pCallerData'),(1, 'hSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientRegisterCallback():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID,c_void_p)(('WdsTransportClientRegisterCallback', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),(1, 'CallbackId'),(1, 'pfnCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientStartSession():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('WdsTransportClientStartSession', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientCompleteReceive():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(('WdsTransportClientCompleteReceive', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),(1, 'ulSize'),(1, 'pullOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientCancelSession():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('WdsTransportClientCancelSession', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientCancelSessionEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32)(('WdsTransportClientCancelSessionEx', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),(1, 'dwErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientWaitForCompletion():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32)(('WdsTransportClientWaitForCompletion', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),(1, 'uTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientQueryStatus():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32))(('WdsTransportClientQueryStatus', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),(1, 'puStatus'),(1, 'puErrorCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientCloseSession():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('WdsTransportClientCloseSession', windll['WDSTPTC.dll']), ((1, 'hSessionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientAddRefBuffer():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('WdsTransportClientAddRefBuffer', windll['WDSTPTC.dll']), ((1, 'pvBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientReleaseBuffer():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('WdsTransportClientReleaseBuffer', windll['WDSTPTC.dll']), ((1, 'pvBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsTransportClientShutdown():
    try:
        return WINFUNCTYPE(UInt32,)(('WdsTransportClientShutdown', windll['WDSTPTC.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpParseInitialize():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,c_char_p_no,POINTER(win32more.Foundation.HANDLE))(('WdsBpParseInitialize', windll['WDSBP.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'pbPacketType'),(1, 'phHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpParseInitializev6():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,c_char_p_no,POINTER(win32more.Foundation.HANDLE))(('WdsBpParseInitializev6', windll['WDSBP.dll']), ((1, 'pPacket'),(1, 'uPacketLen'),(1, 'pbPacketType'),(1, 'phHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpInitialize():
    try:
        return WINFUNCTYPE(UInt32,Byte,POINTER(win32more.Foundation.HANDLE))(('WdsBpInitialize', windll['WDSBP.dll']), ((1, 'bPacketType'),(1, 'phHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpCloseHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('WdsBpCloseHandle', windll['WDSBP.dll']), ((1, 'hHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpQueryOption():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,c_void_p,POINTER(UInt32))(('WdsBpQueryOption', windll['WDSBP.dll']), ((1, 'hHandle'),(1, 'uOption'),(1, 'uValueLen'),(1, 'pValue'),(1, 'puBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpAddOption():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt32,c_void_p)(('WdsBpAddOption', windll['WDSBP.dll']), ((1, 'hHandle'),(1, 'uOption'),(1, 'uValueLen'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WdsBpGetOptionBuffer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(UInt32))(('WdsBpGetOptionBuffer', windll['WDSBP.dll']), ((1, 'hHandle'),(1, 'uBufferLen'),(1, 'pBuffer'),(1, 'puBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
CPU_ARCHITECTURE = UInt32
CPU_ARCHITECTURE_AMD64 = 9
CPU_ARCHITECTURE_IA64 = 6
CPU_ARCHITECTURE_INTEL = 0
def _define_IWdsTransportCacheable_head():
    class IWdsTransportCacheable(win32more.System.Com.IDispatch_head):
        Guid = Guid('46ad894b-0bab-47dc-84-b2-7b-55-3f-1d-8f-80')
    return IWdsTransportCacheable
def _define_IWdsTransportCacheable():
    IWdsTransportCacheable = win32more.System.DeploymentServices.IWdsTransportCacheable_head
    IWdsTransportCacheable.get_Dirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_Dirty', ((1, 'pbDirty'),)))
    IWdsTransportCacheable.Discard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Discard', ()))
    IWdsTransportCacheable.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Refresh', ()))
    IWdsTransportCacheable.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Commit', ()))
    win32more.System.Com.IDispatch
    return IWdsTransportCacheable
def _define_IWdsTransportClient_head():
    class IWdsTransportClient(win32more.System.Com.IDispatch_head):
        Guid = Guid('b5dbc93a-cabe-46ca-83-7f-3e-44-e9-3c-65-45')
    return IWdsTransportClient
def _define_IWdsTransportClient():
    IWdsTransportClient = win32more.System.DeploymentServices.IWdsTransportClient_head
    IWdsTransportClient.get_Session = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportSession_head))(7, 'get_Session', ((1, 'ppWdsTransportSession'),)))
    IWdsTransportClient.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_Id', ((1, 'pulId'),)))
    IWdsTransportClient.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pbszName'),)))
    IWdsTransportClient.get_MacAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_MacAddress', ((1, 'pbszMacAddress'),)))
    IWdsTransportClient.get_IpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_IpAddress', ((1, 'pbszIpAddress'),)))
    IWdsTransportClient.get_PercentCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_PercentCompletion', ((1, 'pulPercentCompletion'),)))
    IWdsTransportClient.get_JoinDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_JoinDuration', ((1, 'pulJoinDuration'),)))
    IWdsTransportClient.get_CpuUtilization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'get_CpuUtilization', ((1, 'pulCpuUtilization'),)))
    IWdsTransportClient.get_MemoryUtilization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'get_MemoryUtilization', ((1, 'pulMemoryUtilization'),)))
    IWdsTransportClient.get_NetworkUtilization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(16, 'get_NetworkUtilization', ((1, 'pulNetworkUtilization'),)))
    IWdsTransportClient.get_UserIdentity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_UserIdentity', ((1, 'pbszUserIdentity'),)))
    IWdsTransportClient.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE)(18, 'Disconnect', ((1, 'DisconnectionType'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportClient
def _define_IWdsTransportCollection_head():
    class IWdsTransportCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('b8ba4b1a-2ff4-43ab-99-6c-b2-b1-0a-91-a6-eb')
    return IWdsTransportCollection
def _define_IWdsTransportCollection():
    IWdsTransportCollection = win32more.System.DeploymentServices.IWdsTransportCollection_head
    IWdsTransportCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'get_Count', ((1, 'pulCount'),)))
    IWdsTransportCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IDispatch_head))(8, 'get_Item', ((1, 'ulIndex'),(1, 'ppVal'),)))
    IWdsTransportCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppVal'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportCollection
def _define_IWdsTransportConfigurationManager_head():
    class IWdsTransportConfigurationManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('84cc4779-42dd-4792-89-1e-13-21-d6-d7-4b-44')
    return IWdsTransportConfigurationManager
def _define_IWdsTransportConfigurationManager():
    IWdsTransportConfigurationManager = win32more.System.DeploymentServices.IWdsTransportConfigurationManager_head
    IWdsTransportConfigurationManager.get_ServicePolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportServicePolicy_head))(7, 'get_ServicePolicy', ((1, 'ppWdsTransportServicePolicy'),)))
    IWdsTransportConfigurationManager.get_DiagnosticsPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportDiagnosticsPolicy_head))(8, 'get_DiagnosticsPolicy', ((1, 'ppWdsTransportDiagnosticsPolicy'),)))
    IWdsTransportConfigurationManager.get_WdsTransportServicesRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_WdsTransportServicesRunning', ((1, 'bRealtimeStatus'),(1, 'pbServicesRunning'),)))
    IWdsTransportConfigurationManager.EnableWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'EnableWdsTransportServices', ()))
    IWdsTransportConfigurationManager.DisableWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'DisableWdsTransportServices', ()))
    IWdsTransportConfigurationManager.StartWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'StartWdsTransportServices', ()))
    IWdsTransportConfigurationManager.StopWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'StopWdsTransportServices', ()))
    IWdsTransportConfigurationManager.RestartWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'RestartWdsTransportServices', ()))
    IWdsTransportConfigurationManager.NotifyWdsTransportServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION)(15, 'NotifyWdsTransportServices', ((1, 'ServiceNotification'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportConfigurationManager
def _define_IWdsTransportConfigurationManager2_head():
    class IWdsTransportConfigurationManager2(win32more.System.DeploymentServices.IWdsTransportConfigurationManager_head):
        Guid = Guid('d0d85caf-a153-4f1d-a9-dd-96-f4-31-c5-07-17')
    return IWdsTransportConfigurationManager2
def _define_IWdsTransportConfigurationManager2():
    IWdsTransportConfigurationManager2 = win32more.System.DeploymentServices.IWdsTransportConfigurationManager2_head
    IWdsTransportConfigurationManager2.get_MulticastSessionPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportMulticastSessionPolicy_head))(16, 'get_MulticastSessionPolicy', ((1, 'ppWdsTransportMulticastSessionPolicy'),)))
    win32more.System.DeploymentServices.IWdsTransportConfigurationManager
    return IWdsTransportConfigurationManager2
def _define_IWdsTransportContent_head():
    class IWdsTransportContent(win32more.System.Com.IDispatch_head):
        Guid = Guid('d405d711-0296-4ab4-a8-60-ac-7d-32-e6-57-98')
    return IWdsTransportContent
def _define_IWdsTransportContent():
    IWdsTransportContent = win32more.System.DeploymentServices.IWdsTransportContent_head
    IWdsTransportContent.get_Namespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head))(7, 'get_Namespace', ((1, 'ppWdsTransportNamespace'),)))
    IWdsTransportContent.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_Id', ((1, 'pulId'),)))
    IWdsTransportContent.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pbszName'),)))
    IWdsTransportContent.RetrieveSessions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(10, 'RetrieveSessions', ((1, 'ppWdsTransportSessions'),)))
    IWdsTransportContent.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Terminate', ()))
    win32more.System.Com.IDispatch
    return IWdsTransportContent
def _define_IWdsTransportContentProvider_head():
    class IWdsTransportContentProvider(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9489f24-f219-4acf-aa-d7-26-5c-7c-08-a6-ae')
    return IWdsTransportContentProvider
def _define_IWdsTransportContentProvider():
    IWdsTransportContentProvider = win32more.System.DeploymentServices.IWdsTransportContentProvider_head
    IWdsTransportContentProvider.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pbszName'),)))
    IWdsTransportContentProvider.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Description', ((1, 'pbszDescription'),)))
    IWdsTransportContentProvider.get_FilePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_FilePath', ((1, 'pbszFilePath'),)))
    IWdsTransportContentProvider.get_InitializationRoutine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_InitializationRoutine', ((1, 'pbszInitializationRoutine'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportContentProvider
def _define_IWdsTransportDiagnosticsPolicy_head():
    class IWdsTransportDiagnosticsPolicy(win32more.System.DeploymentServices.IWdsTransportCacheable_head):
        Guid = Guid('13b33efc-7856-4f61-9a-59-8d-e6-7b-6b-87-b6')
    return IWdsTransportDiagnosticsPolicy
def _define_IWdsTransportDiagnosticsPolicy():
    IWdsTransportDiagnosticsPolicy = win32more.System.DeploymentServices.IWdsTransportDiagnosticsPolicy_head
    IWdsTransportDiagnosticsPolicy.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_Enabled', ((1, 'pbEnabled'),)))
    IWdsTransportDiagnosticsPolicy.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_Enabled', ((1, 'bEnabled'),)))
    IWdsTransportDiagnosticsPolicy.get_Components = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_Components', ((1, 'pulComponents'),)))
    IWdsTransportDiagnosticsPolicy.put_Components = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(14, 'put_Components', ((1, 'ulComponents'),)))
    win32more.System.DeploymentServices.IWdsTransportCacheable
    return IWdsTransportDiagnosticsPolicy
def _define_IWdsTransportManager_head():
    class IWdsTransportManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('5b0d35f5-1b13-4afd-b8-78-65-26-dc-34-0b-5d')
    return IWdsTransportManager
def _define_IWdsTransportManager():
    IWdsTransportManager = win32more.System.DeploymentServices.IWdsTransportManager_head
    IWdsTransportManager.GetWdsTransportServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.DeploymentServices.IWdsTransportServer_head))(7, 'GetWdsTransportServer', ((1, 'bszServerName'),(1, 'ppWdsTransportServer'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportManager
def _define_IWdsTransportMulticastSessionPolicy_head():
    class IWdsTransportMulticastSessionPolicy(win32more.System.DeploymentServices.IWdsTransportCacheable_head):
        Guid = Guid('4e5753cf-68ec-4504-a9-51-4a-00-32-66-60-6b')
    return IWdsTransportMulticastSessionPolicy
def _define_IWdsTransportMulticastSessionPolicy():
    IWdsTransportMulticastSessionPolicy = win32more.System.DeploymentServices.IWdsTransportMulticastSessionPolicy_head
    IWdsTransportMulticastSessionPolicy.get_SlowClientHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE))(11, 'get_SlowClientHandling', ((1, 'pSlowClientHandling'),)))
    IWdsTransportMulticastSessionPolicy.put_SlowClientHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE)(12, 'put_SlowClientHandling', ((1, 'SlowClientHandling'),)))
    IWdsTransportMulticastSessionPolicy.get_AutoDisconnectThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_AutoDisconnectThreshold', ((1, 'pulThreshold'),)))
    IWdsTransportMulticastSessionPolicy.put_AutoDisconnectThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(14, 'put_AutoDisconnectThreshold', ((1, 'ulThreshold'),)))
    IWdsTransportMulticastSessionPolicy.get_MultistreamStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'get_MultistreamStreamCount', ((1, 'pulStreamCount'),)))
    IWdsTransportMulticastSessionPolicy.put_MultistreamStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(16, 'put_MultistreamStreamCount', ((1, 'ulStreamCount'),)))
    IWdsTransportMulticastSessionPolicy.get_SlowClientFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_SlowClientFallback', ((1, 'pbClientFallback'),)))
    IWdsTransportMulticastSessionPolicy.put_SlowClientFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_SlowClientFallback', ((1, 'bClientFallback'),)))
    win32more.System.DeploymentServices.IWdsTransportCacheable
    return IWdsTransportMulticastSessionPolicy
def _define_IWdsTransportNamespace_head():
    class IWdsTransportNamespace(win32more.System.Com.IDispatch_head):
        Guid = Guid('fa561f57-fbef-4ed3-b0-56-12-7c-b1-b3-3b-84')
    return IWdsTransportNamespace
def _define_IWdsTransportNamespace():
    IWdsTransportNamespace = win32more.System.DeploymentServices.IWdsTransportNamespace_head
    IWdsTransportNamespace.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE))(7, 'get_Type', ((1, 'pType'),)))
    IWdsTransportNamespace.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_Id', ((1, 'pulId'),)))
    IWdsTransportNamespace.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pbszName'),)))
    IWdsTransportNamespace.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Name', ((1, 'bszName'),)))
    IWdsTransportNamespace.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_FriendlyName', ((1, 'pbszFriendlyName'),)))
    IWdsTransportNamespace.put_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_FriendlyName', ((1, 'bszFriendlyName'),)))
    IWdsTransportNamespace.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Description', ((1, 'pbszDescription'),)))
    IWdsTransportNamespace.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_Description', ((1, 'bszDescription'),)))
    IWdsTransportNamespace.get_ContentProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_ContentProvider', ((1, 'pbszContentProvider'),)))
    IWdsTransportNamespace.put_ContentProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_ContentProvider', ((1, 'bszContentProvider'),)))
    IWdsTransportNamespace.get_Configuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_Configuration', ((1, 'pbszConfiguration'),)))
    IWdsTransportNamespace.put_Configuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_Configuration', ((1, 'bszConfiguration'),)))
    IWdsTransportNamespace.get_Registered = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_Registered', ((1, 'pbRegistered'),)))
    IWdsTransportNamespace.get_Tombstoned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_Tombstoned', ((1, 'pbTombstoned'),)))
    IWdsTransportNamespace.get_TombstoneTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_TombstoneTime', ((1, 'pTombstoneTime'),)))
    IWdsTransportNamespace.get_TransmissionStarted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(22, 'get_TransmissionStarted', ((1, 'pbTransmissionStarted'),)))
    IWdsTransportNamespace.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'Register', ()))
    IWdsTransportNamespace.Deregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(24, 'Deregister', ((1, 'bTerminateSessions'),)))
    IWdsTransportNamespace.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head))(25, 'Clone', ((1, 'ppWdsTransportNamespaceClone'),)))
    IWdsTransportNamespace.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'Refresh', ()))
    IWdsTransportNamespace.RetrieveContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(27, 'RetrieveContents', ((1, 'ppWdsTransportContents'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportNamespace
def _define_IWdsTransportNamespaceAutoCast_head():
    class IWdsTransportNamespaceAutoCast(win32more.System.DeploymentServices.IWdsTransportNamespace_head):
        Guid = Guid('ad931a72-c4bd-4c41-8f-bc-59-c9-c7-48-df-9e')
    return IWdsTransportNamespaceAutoCast
def _define_IWdsTransportNamespaceAutoCast():
    IWdsTransportNamespaceAutoCast = win32more.System.DeploymentServices.IWdsTransportNamespaceAutoCast_head
    win32more.System.DeploymentServices.IWdsTransportNamespace
    return IWdsTransportNamespaceAutoCast
def _define_IWdsTransportNamespaceManager_head():
    class IWdsTransportNamespaceManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('3e22d9f6-3777-4d98-83-e1-f9-86-96-71-7b-a3')
    return IWdsTransportNamespaceManager
def _define_IWdsTransportNamespaceManager():
    IWdsTransportNamespaceManager = win32more.System.DeploymentServices.IWdsTransportNamespaceManager_head
    IWdsTransportNamespaceManager.CreateNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head))(7, 'CreateNamespace', ((1, 'NamespaceType'),(1, 'bszNamespaceName'),(1, 'bszContentProvider'),(1, 'bszConfiguration'),(1, 'ppWdsTransportNamespace'),)))
    IWdsTransportNamespaceManager.RetrieveNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.DeploymentServices.IWdsTransportNamespace_head))(8, 'RetrieveNamespace', ((1, 'bszNamespaceName'),(1, 'ppWdsTransportNamespace'),)))
    IWdsTransportNamespaceManager.RetrieveNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(9, 'RetrieveNamespaces', ((1, 'bszContentProvider'),(1, 'bszNamespaceName'),(1, 'bIncludeTombstones'),(1, 'ppWdsTransportNamespaces'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportNamespaceManager
def _define_IWdsTransportNamespaceScheduledCast_head():
    class IWdsTransportNamespaceScheduledCast(win32more.System.DeploymentServices.IWdsTransportNamespace_head):
        Guid = Guid('3840cecf-d76c-416e-a4-cc-31-c7-41-d2-87-4b')
    return IWdsTransportNamespaceScheduledCast
def _define_IWdsTransportNamespaceScheduledCast():
    IWdsTransportNamespaceScheduledCast = win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast_head
    IWdsTransportNamespaceScheduledCast.StartTransmission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(28, 'StartTransmission', ()))
    win32more.System.DeploymentServices.IWdsTransportNamespace
    return IWdsTransportNamespaceScheduledCast
def _define_IWdsTransportNamespaceScheduledCastAutoStart_head():
    class IWdsTransportNamespaceScheduledCastAutoStart(win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast_head):
        Guid = Guid('d606af3d-ea9c-4219-96-1e-74-91-d6-18-d9-b9')
    return IWdsTransportNamespaceScheduledCastAutoStart
def _define_IWdsTransportNamespaceScheduledCastAutoStart():
    IWdsTransportNamespaceScheduledCastAutoStart = win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCastAutoStart_head
    IWdsTransportNamespaceScheduledCastAutoStart.get_MinimumClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(29, 'get_MinimumClients', ((1, 'pulMinimumClients'),)))
    IWdsTransportNamespaceScheduledCastAutoStart.put_MinimumClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(30, 'put_MinimumClients', ((1, 'ulMinimumClients'),)))
    IWdsTransportNamespaceScheduledCastAutoStart.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(31, 'get_StartTime', ((1, 'pStartTime'),)))
    IWdsTransportNamespaceScheduledCastAutoStart.put_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(32, 'put_StartTime', ((1, 'StartTime'),)))
    win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    return IWdsTransportNamespaceScheduledCastAutoStart
def _define_IWdsTransportNamespaceScheduledCastManualStart_head():
    class IWdsTransportNamespaceScheduledCastManualStart(win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast_head):
        Guid = Guid('013e6e4c-e6a7-4fb5-b7-ff-d9-f5-da-80-5c-31')
    return IWdsTransportNamespaceScheduledCastManualStart
def _define_IWdsTransportNamespaceScheduledCastManualStart():
    IWdsTransportNamespaceScheduledCastManualStart = win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCastManualStart_head
    win32more.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    return IWdsTransportNamespaceScheduledCastManualStart
def _define_IWdsTransportServer_head():
    class IWdsTransportServer(win32more.System.Com.IDispatch_head):
        Guid = Guid('09ccd093-830d-4344-a3-0a-73-ae-8e-8f-ca-90')
    return IWdsTransportServer
def _define_IWdsTransportServer():
    IWdsTransportServer = win32more.System.DeploymentServices.IWdsTransportServer_head
    IWdsTransportServer.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pbszName'),)))
    IWdsTransportServer.get_SetupManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportSetupManager_head))(8, 'get_SetupManager', ((1, 'ppWdsTransportSetupManager'),)))
    IWdsTransportServer.get_ConfigurationManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportConfigurationManager_head))(9, 'get_ConfigurationManager', ((1, 'ppWdsTransportConfigurationManager'),)))
    IWdsTransportServer.get_NamespaceManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportNamespaceManager_head))(10, 'get_NamespaceManager', ((1, 'ppWdsTransportNamespaceManager'),)))
    IWdsTransportServer.DisconnectClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE)(11, 'DisconnectClient', ((1, 'ulClientId'),(1, 'DisconnectionType'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportServer
def _define_IWdsTransportServer2_head():
    class IWdsTransportServer2(win32more.System.DeploymentServices.IWdsTransportServer_head):
        Guid = Guid('256e999f-6df4-4538-81-b9-85-7b-9a-b8-fb-47')
    return IWdsTransportServer2
def _define_IWdsTransportServer2():
    IWdsTransportServer2 = win32more.System.DeploymentServices.IWdsTransportServer2_head
    IWdsTransportServer2.get_TftpManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportTftpManager_head))(12, 'get_TftpManager', ((1, 'ppWdsTransportTftpManager'),)))
    win32more.System.DeploymentServices.IWdsTransportServer
    return IWdsTransportServer2
def _define_IWdsTransportServicePolicy_head():
    class IWdsTransportServicePolicy(win32more.System.DeploymentServices.IWdsTransportCacheable_head):
        Guid = Guid('b9468578-9f2b-48cc-b2-7a-a6-07-99-c2-75-0c')
    return IWdsTransportServicePolicy
def _define_IWdsTransportServicePolicy():
    IWdsTransportServicePolicy = win32more.System.DeploymentServices.IWdsTransportServicePolicy_head
    IWdsTransportServicePolicy.get_IpAddressSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE))(11, 'get_IpAddressSource', ((1, 'AddressType'),(1, 'pSourceType'),)))
    IWdsTransportServicePolicy.put_IpAddressSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE)(12, 'put_IpAddressSource', ((1, 'AddressType'),(1, 'SourceType'),)))
    IWdsTransportServicePolicy.get_StartIpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,POINTER(win32more.Foundation.BSTR))(13, 'get_StartIpAddress', ((1, 'AddressType'),(1, 'pbszStartIpAddress'),)))
    IWdsTransportServicePolicy.put_StartIpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,win32more.Foundation.BSTR)(14, 'put_StartIpAddress', ((1, 'AddressType'),(1, 'bszStartIpAddress'),)))
    IWdsTransportServicePolicy.get_EndIpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,POINTER(win32more.Foundation.BSTR))(15, 'get_EndIpAddress', ((1, 'AddressType'),(1, 'pbszEndIpAddress'),)))
    IWdsTransportServicePolicy.put_EndIpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE,win32more.Foundation.BSTR)(16, 'put_EndIpAddress', ((1, 'AddressType'),(1, 'bszEndIpAddress'),)))
    IWdsTransportServicePolicy.get_StartPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(17, 'get_StartPort', ((1, 'pulStartPort'),)))
    IWdsTransportServicePolicy.put_StartPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(18, 'put_StartPort', ((1, 'ulStartPort'),)))
    IWdsTransportServicePolicy.get_EndPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(19, 'get_EndPort', ((1, 'pulEndPort'),)))
    IWdsTransportServicePolicy.put_EndPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(20, 'put_EndPort', ((1, 'ulEndPort'),)))
    IWdsTransportServicePolicy.get_NetworkProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE))(21, 'get_NetworkProfile', ((1, 'pProfileType'),)))
    IWdsTransportServicePolicy.put_NetworkProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE)(22, 'put_NetworkProfile', ((1, 'ProfileType'),)))
    win32more.System.DeploymentServices.IWdsTransportCacheable
    return IWdsTransportServicePolicy
def _define_IWdsTransportServicePolicy2_head():
    class IWdsTransportServicePolicy2(win32more.System.DeploymentServices.IWdsTransportServicePolicy_head):
        Guid = Guid('65c19e5c-aa7e-4b91-89-44-91-e0-e5-57-27-97')
    return IWdsTransportServicePolicy2
def _define_IWdsTransportServicePolicy2():
    IWdsTransportServicePolicy2 = win32more.System.DeploymentServices.IWdsTransportServicePolicy2_head
    IWdsTransportServicePolicy2.get_UdpPortPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY))(23, 'get_UdpPortPolicy', ((1, 'pUdpPortPolicy'),)))
    IWdsTransportServicePolicy2.put_UdpPortPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY)(24, 'put_UdpPortPolicy', ((1, 'UdpPortPolicy'),)))
    IWdsTransportServicePolicy2.get_TftpMaximumBlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(25, 'get_TftpMaximumBlockSize', ((1, 'pulTftpMaximumBlockSize'),)))
    IWdsTransportServicePolicy2.put_TftpMaximumBlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(26, 'put_TftpMaximumBlockSize', ((1, 'ulTftpMaximumBlockSize'),)))
    IWdsTransportServicePolicy2.get_EnableTftpVariableWindowExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(27, 'get_EnableTftpVariableWindowExtension', ((1, 'pbEnableTftpVariableWindowExtension'),)))
    IWdsTransportServicePolicy2.put_EnableTftpVariableWindowExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(28, 'put_EnableTftpVariableWindowExtension', ((1, 'bEnableTftpVariableWindowExtension'),)))
    win32more.System.DeploymentServices.IWdsTransportServicePolicy
    return IWdsTransportServicePolicy2
def _define_IWdsTransportSession_head():
    class IWdsTransportSession(win32more.System.Com.IDispatch_head):
        Guid = Guid('f4efea88-65b1-4f30-a4-b9-27-93-98-77-96-fb')
    return IWdsTransportSession
def _define_IWdsTransportSession():
    IWdsTransportSession = win32more.System.DeploymentServices.IWdsTransportSession_head
    IWdsTransportSession.get_Content = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportContent_head))(7, 'get_Content', ((1, 'ppWdsTransportContent'),)))
    IWdsTransportSession.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_Id', ((1, 'pulId'),)))
    IWdsTransportSession.get_NetworkInterfaceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_NetworkInterfaceName', ((1, 'pbszNetworkInterfaceName'),)))
    IWdsTransportSession.get_NetworkInterfaceAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_NetworkInterfaceAddress', ((1, 'pbszNetworkInterfaceAddress'),)))
    IWdsTransportSession.get_TransferRate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'get_TransferRate', ((1, 'pulTransferRate'),)))
    IWdsTransportSession.get_MasterClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_MasterClientId', ((1, 'pulMasterClientId'),)))
    IWdsTransportSession.RetrieveClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(13, 'RetrieveClients', ((1, 'ppWdsTransportClients'),)))
    IWdsTransportSession.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Terminate', ()))
    win32more.System.Com.IDispatch
    return IWdsTransportSession
def _define_IWdsTransportSetupManager_head():
    class IWdsTransportSetupManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('f7238425-efa8-40a4-ae-f9-c9-8d-96-9c-0b-75')
    return IWdsTransportSetupManager
def _define_IWdsTransportSetupManager():
    IWdsTransportSetupManager = win32more.System.DeploymentServices.IWdsTransportSetupManager_head
    IWdsTransportSetupManager.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(7, 'get_Version', ((1, 'pullVersion'),)))
    IWdsTransportSetupManager.get_InstalledFeatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_InstalledFeatures', ((1, 'pulInstalledFeatures'),)))
    IWdsTransportSetupManager.get_Protocols = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'get_Protocols', ((1, 'pulProtocols'),)))
    IWdsTransportSetupManager.RegisterContentProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(10, 'RegisterContentProvider', ((1, 'bszName'),(1, 'bszDescription'),(1, 'bszFilePath'),(1, 'bszInitializationRoutine'),)))
    IWdsTransportSetupManager.DeregisterContentProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'DeregisterContentProvider', ((1, 'bszName'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportSetupManager
def _define_IWdsTransportSetupManager2_head():
    class IWdsTransportSetupManager2(win32more.System.DeploymentServices.IWdsTransportSetupManager_head):
        Guid = Guid('02be79da-7e9e-4366-8b-6e-2a-a9-a9-1b-e4-7f')
    return IWdsTransportSetupManager2
def _define_IWdsTransportSetupManager2():
    IWdsTransportSetupManager2 = win32more.System.DeploymentServices.IWdsTransportSetupManager2_head
    IWdsTransportSetupManager2.get_TftpCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_TftpCapabilities', ((1, 'pulTftpCapabilities'),)))
    IWdsTransportSetupManager2.get_ContentProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(13, 'get_ContentProviders', ((1, 'ppProviderCollection'),)))
    win32more.System.DeploymentServices.IWdsTransportSetupManager
    return IWdsTransportSetupManager2
def _define_IWdsTransportTftpClient_head():
    class IWdsTransportTftpClient(win32more.System.Com.IDispatch_head):
        Guid = Guid('b022d3ae-884d-4d85-b1-46-53-32-0e-76-ef-62')
    return IWdsTransportTftpClient
def _define_IWdsTransportTftpClient():
    IWdsTransportTftpClient = win32more.System.DeploymentServices.IWdsTransportTftpClient_head
    IWdsTransportTftpClient.get_FileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_FileName', ((1, 'pbszFileName'),)))
    IWdsTransportTftpClient.get_IpAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_IpAddress', ((1, 'pbszIpAddress'),)))
    IWdsTransportTftpClient.get_Timeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'get_Timeout', ((1, 'pulTimeout'),)))
    IWdsTransportTftpClient.get_CurrentFileOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(10, 'get_CurrentFileOffset', ((1, 'pul64CurrentOffset'),)))
    IWdsTransportTftpClient.get_FileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(11, 'get_FileSize', ((1, 'pul64FileSize'),)))
    IWdsTransportTftpClient.get_BlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_BlockSize', ((1, 'pulBlockSize'),)))
    IWdsTransportTftpClient.get_WindowSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_WindowSize', ((1, 'pulWindowSize'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportTftpClient
def _define_IWdsTransportTftpManager_head():
    class IWdsTransportTftpManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('1327a7c8-ae8a-4fb3-81-50-13-62-27-c3-7e-9a')
    return IWdsTransportTftpManager
def _define_IWdsTransportTftpManager():
    IWdsTransportTftpManager = win32more.System.DeploymentServices.IWdsTransportTftpManager_head
    IWdsTransportTftpManager.RetrieveTftpClients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DeploymentServices.IWdsTransportCollection_head))(7, 'RetrieveTftpClients', ((1, 'ppWdsTransportTftpClients'),)))
    win32more.System.Com.IDispatch
    return IWdsTransportTftpManager
PFN_WDS_CLI_CALLBACK_MESSAGE_ID = UInt32
WDS_CLI_MSG_START = 0
WDS_CLI_MSG_COMPLETE = 1
WDS_CLI_MSG_PROGRESS = 2
WDS_CLI_MSG_TEXT = 3
def _define_PFN_WdsCliCallback():
    return WINFUNCTYPE(Void,win32more.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,c_void_p)
def _define_PFN_WdsCliTraceFunction():
    return WINFUNCTYPE(Void,win32more.Foundation.PWSTR,POINTER(SByte))
def _define_PFN_WdsTransportClientReceiveContents():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,c_void_p,UInt32,POINTER(win32more.Foundation.ULARGE_INTEGER_head))
def _define_PFN_WdsTransportClientReceiveMetadata():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,c_void_p,UInt32)
def _define_PFN_WdsTransportClientSessionComplete():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,UInt32)
def _define_PFN_WdsTransportClientSessionNegotiate():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,POINTER(win32more.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head),win32more.Foundation.HANDLE)
def _define_PFN_WdsTransportClientSessionStart():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,POINTER(win32more.Foundation.ULARGE_INTEGER_head))
def _define_PFN_WdsTransportClientSessionStartEx():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p,POINTER(win32more.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head))
def _define_PXE_ADDRESS_head():
    class PXE_ADDRESS(Structure):
        pass
    return PXE_ADDRESS
def _define_PXE_ADDRESS():
    PXE_ADDRESS = win32more.System.DeploymentServices.PXE_ADDRESS_head
    class PXE_ADDRESS__Anonymous_e__Union(Union):
        pass
    PXE_ADDRESS__Anonymous_e__Union._fields_ = [
        ('bAddress', Byte * 16),
        ('uIpAddress', UInt32),
    ]
    PXE_ADDRESS._anonymous_ = [
        'Anonymous',
    ]
    PXE_ADDRESS._fields_ = [
        ('uFlags', UInt32),
        ('Anonymous', PXE_ADDRESS__Anonymous_e__Union),
        ('uAddrLen', UInt32),
        ('uPort', UInt16),
    ]
    return PXE_ADDRESS
def _define_PXE_DHCP_MESSAGE_head():
    class PXE_DHCP_MESSAGE(Structure):
        pass
    return PXE_DHCP_MESSAGE
def _define_PXE_DHCP_MESSAGE():
    PXE_DHCP_MESSAGE = win32more.System.DeploymentServices.PXE_DHCP_MESSAGE_head
    class PXE_DHCP_MESSAGE__Anonymous_e__Union(Union):
        pass
    PXE_DHCP_MESSAGE__Anonymous_e__Union._pack_ = 1
    PXE_DHCP_MESSAGE__Anonymous_e__Union._fields_ = [
        ('bMagicCookie', Byte * 4),
        ('uMagicCookie', UInt32),
    ]
    PXE_DHCP_MESSAGE._pack_ = 1
    PXE_DHCP_MESSAGE._anonymous_ = [
        'Anonymous',
    ]
    PXE_DHCP_MESSAGE._fields_ = [
        ('Operation', Byte),
        ('HardwareAddressType', Byte),
        ('HardwareAddressLength', Byte),
        ('HopCount', Byte),
        ('TransactionID', UInt32),
        ('SecondsSinceBoot', UInt16),
        ('Reserved', UInt16),
        ('ClientIpAddress', UInt32),
        ('YourIpAddress', UInt32),
        ('BootstrapServerAddress', UInt32),
        ('RelayAgentIpAddress', UInt32),
        ('HardwareAddress', Byte * 16),
        ('HostName', Byte * 64),
        ('BootFileName', Byte * 128),
        ('Anonymous', PXE_DHCP_MESSAGE__Anonymous_e__Union),
        ('Option', win32more.System.DeploymentServices.PXE_DHCP_OPTION),
    ]
    return PXE_DHCP_MESSAGE
def _define_PXE_DHCP_OPTION_head():
    class PXE_DHCP_OPTION(Structure):
        pass
    return PXE_DHCP_OPTION
def _define_PXE_DHCP_OPTION():
    PXE_DHCP_OPTION = win32more.System.DeploymentServices.PXE_DHCP_OPTION_head
    PXE_DHCP_OPTION._pack_ = 1
    PXE_DHCP_OPTION._fields_ = [
        ('OptionType', Byte),
        ('OptionLength', Byte),
        ('OptionValue', Byte * 1),
    ]
    return PXE_DHCP_OPTION
def _define_PXE_DHCPV6_MESSAGE_head():
    class PXE_DHCPV6_MESSAGE(Structure):
        pass
    return PXE_DHCPV6_MESSAGE
def _define_PXE_DHCPV6_MESSAGE():
    PXE_DHCPV6_MESSAGE = win32more.System.DeploymentServices.PXE_DHCPV6_MESSAGE_head
    PXE_DHCPV6_MESSAGE._pack_ = 1
    PXE_DHCPV6_MESSAGE._fields_ = [
        ('MessageType', Byte),
        ('TransactionIDByte1', Byte),
        ('TransactionIDByte2', Byte),
        ('TransactionIDByte3', Byte),
        ('Options', win32more.System.DeploymentServices.PXE_DHCPV6_OPTION * 1),
    ]
    return PXE_DHCPV6_MESSAGE
def _define_PXE_DHCPV6_MESSAGE_HEADER_head():
    class PXE_DHCPV6_MESSAGE_HEADER(Structure):
        pass
    return PXE_DHCPV6_MESSAGE_HEADER
def _define_PXE_DHCPV6_MESSAGE_HEADER():
    PXE_DHCPV6_MESSAGE_HEADER = win32more.System.DeploymentServices.PXE_DHCPV6_MESSAGE_HEADER_head
    PXE_DHCPV6_MESSAGE_HEADER._pack_ = 1
    PXE_DHCPV6_MESSAGE_HEADER._fields_ = [
        ('MessageType', Byte),
        ('Message', Byte * 1),
    ]
    return PXE_DHCPV6_MESSAGE_HEADER
def _define_PXE_DHCPV6_NESTED_RELAY_MESSAGE_head():
    class PXE_DHCPV6_NESTED_RELAY_MESSAGE(Structure):
        pass
    return PXE_DHCPV6_NESTED_RELAY_MESSAGE
def _define_PXE_DHCPV6_NESTED_RELAY_MESSAGE():
    PXE_DHCPV6_NESTED_RELAY_MESSAGE = win32more.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head
    PXE_DHCPV6_NESTED_RELAY_MESSAGE._fields_ = [
        ('pRelayMessage', POINTER(win32more.System.DeploymentServices.PXE_DHCPV6_RELAY_MESSAGE_head)),
        ('cbRelayMessage', UInt32),
        ('pInterfaceIdOption', c_void_p),
        ('cbInterfaceIdOption', UInt16),
    ]
    return PXE_DHCPV6_NESTED_RELAY_MESSAGE
def _define_PXE_DHCPV6_OPTION_head():
    class PXE_DHCPV6_OPTION(Structure):
        pass
    return PXE_DHCPV6_OPTION
def _define_PXE_DHCPV6_OPTION():
    PXE_DHCPV6_OPTION = win32more.System.DeploymentServices.PXE_DHCPV6_OPTION_head
    PXE_DHCPV6_OPTION._pack_ = 1
    PXE_DHCPV6_OPTION._fields_ = [
        ('OptionCode', UInt16),
        ('DataLength', UInt16),
        ('Data', Byte * 1),
    ]
    return PXE_DHCPV6_OPTION
def _define_PXE_DHCPV6_RELAY_MESSAGE_head():
    class PXE_DHCPV6_RELAY_MESSAGE(Structure):
        pass
    return PXE_DHCPV6_RELAY_MESSAGE
def _define_PXE_DHCPV6_RELAY_MESSAGE():
    PXE_DHCPV6_RELAY_MESSAGE = win32more.System.DeploymentServices.PXE_DHCPV6_RELAY_MESSAGE_head
    PXE_DHCPV6_RELAY_MESSAGE._pack_ = 1
    PXE_DHCPV6_RELAY_MESSAGE._fields_ = [
        ('MessageType', Byte),
        ('HopCount', Byte),
        ('LinkAddress', Byte * 16),
        ('PeerAddress', Byte * 16),
        ('Options', win32more.System.DeploymentServices.PXE_DHCPV6_OPTION * 1),
    ]
    return PXE_DHCPV6_RELAY_MESSAGE
def _define_PXE_PROVIDER_head():
    class PXE_PROVIDER(Structure):
        pass
    return PXE_PROVIDER
def _define_PXE_PROVIDER():
    PXE_PROVIDER = win32more.System.DeploymentServices.PXE_PROVIDER_head
    PXE_PROVIDER._fields_ = [
        ('uSizeOfStruct', UInt32),
        ('pwszName', win32more.Foundation.PWSTR),
        ('pwszFilePath', win32more.Foundation.PWSTR),
        ('bIsCritical', win32more.Foundation.BOOL),
        ('uIndex', UInt32),
    ]
    return PXE_PROVIDER
TRANSPORTCLIENT_CALLBACK_ID = Int32
WDS_TRANSPORTCLIENT_SESSION_START = 0
WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS = 1
WDS_TRANSPORTCLIENT_SESSION_COMPLETE = 2
WDS_TRANSPORTCLIENT_RECEIVE_METADATA = 3
WDS_TRANSPORTCLIENT_SESSION_STARTEX = 4
WDS_TRANSPORTCLIENT_SESSION_NEGOTIATE = 5
WDS_TRANSPORTCLIENT_MAX_CALLBACKS = 6
def _define_TRANSPORTCLIENT_SESSION_INFO_head():
    class TRANSPORTCLIENT_SESSION_INFO(Structure):
        pass
    return TRANSPORTCLIENT_SESSION_INFO
def _define_TRANSPORTCLIENT_SESSION_INFO():
    TRANSPORTCLIENT_SESSION_INFO = win32more.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head
    TRANSPORTCLIENT_SESSION_INFO._fields_ = [
        ('ulStructureLength', UInt32),
        ('ullFileSize', win32more.Foundation.ULARGE_INTEGER),
        ('ulBlockSize', UInt32),
    ]
    return TRANSPORTCLIENT_SESSION_INFO
TRANSPORTPROVIDER_CALLBACK_ID = Int32
WDS_TRANSPORTPROVIDER_CREATE_INSTANCE = 0
WDS_TRANSPORTPROVIDER_COMPARE_CONTENT = 1
WDS_TRANSPORTPROVIDER_OPEN_CONTENT = 2
WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK = 3
WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE = 4
WDS_TRANSPORTPROVIDER_READ_CONTENT = 5
WDS_TRANSPORTPROVIDER_CLOSE_CONTENT = 6
WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE = 7
WDS_TRANSPORTPROVIDER_SHUTDOWN = 8
WDS_TRANSPORTPROVIDER_DUMP_STATE = 9
WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS = 10
WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA = 11
WDS_TRANSPORTPROVIDER_MAX_CALLBACKS = 12
def _define_WDS_CLI_CRED_head():
    class WDS_CLI_CRED(Structure):
        pass
    return WDS_CLI_CRED
def _define_WDS_CLI_CRED():
    WDS_CLI_CRED = win32more.System.DeploymentServices.WDS_CLI_CRED_head
    WDS_CLI_CRED._fields_ = [
        ('pwszUserName', win32more.Foundation.PWSTR),
        ('pwszDomain', win32more.Foundation.PWSTR),
        ('pwszPassword', win32more.Foundation.PWSTR),
    ]
    return WDS_CLI_CRED
WDS_CLI_FIRMWARE_TYPE = Int32
WDS_CLI_FIRMWARE_UNKNOWN = 0
WDS_CLI_FIRMWARE_BIOS = 1
WDS_CLI_FIRMWARE_EFI = 2
WDS_CLI_IMAGE_PARAM_TYPE = Int32
WDS_CLI_IMAGE_PARAM_UNKNOWN = 0
WDS_CLI_IMAGE_PARAM_SPARSE_FILE = 1
WDS_CLI_IMAGE_PARAM_SUPPORTED_FIRMWARES = 2
WDS_CLI_IMAGE_TYPE = Int32
WDS_CLI_IMAGE_TYPE_UNKNOWN = 0
WDS_CLI_IMAGE_TYPE_WIM = 1
WDS_CLI_IMAGE_TYPE_VHD = 2
WDS_CLI_IMAGE_TYPE_VHDX = 3
def _define_WDS_TRANSPORTCLIENT_CALLBACKS_head():
    class WDS_TRANSPORTCLIENT_CALLBACKS(Structure):
        pass
    return WDS_TRANSPORTCLIENT_CALLBACKS
def _define_WDS_TRANSPORTCLIENT_CALLBACKS():
    WDS_TRANSPORTCLIENT_CALLBACKS = win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_CALLBACKS_head
    WDS_TRANSPORTCLIENT_CALLBACKS._fields_ = [
        ('SessionStart', win32more.System.DeploymentServices.PFN_WdsTransportClientSessionStart),
        ('SessionStartEx', win32more.System.DeploymentServices.PFN_WdsTransportClientSessionStartEx),
        ('ReceiveContents', win32more.System.DeploymentServices.PFN_WdsTransportClientReceiveContents),
        ('ReceiveMetadata', win32more.System.DeploymentServices.PFN_WdsTransportClientReceiveMetadata),
        ('SessionComplete', win32more.System.DeploymentServices.PFN_WdsTransportClientSessionComplete),
        ('SessionNegotiate', win32more.System.DeploymentServices.PFN_WdsTransportClientSessionNegotiate),
    ]
    return WDS_TRANSPORTCLIENT_CALLBACKS
def _define_WDS_TRANSPORTCLIENT_REQUEST_head():
    class WDS_TRANSPORTCLIENT_REQUEST(Structure):
        pass
    return WDS_TRANSPORTCLIENT_REQUEST
def _define_WDS_TRANSPORTCLIENT_REQUEST():
    WDS_TRANSPORTCLIENT_REQUEST = win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_head
    WDS_TRANSPORTCLIENT_REQUEST._fields_ = [
        ('ulLength', UInt32),
        ('ulApiVersion', UInt32),
        ('ulAuthLevel', win32more.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL),
        ('pwszServer', win32more.Foundation.PWSTR),
        ('pwszNamespace', win32more.Foundation.PWSTR),
        ('pwszObjectName', win32more.Foundation.PWSTR),
        ('ulCacheSize', UInt32),
        ('ulProtocol', UInt32),
        ('pvProtocolData', c_void_p),
        ('ulProtocolDataLength', UInt32),
    ]
    return WDS_TRANSPORTCLIENT_REQUEST
WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = UInt32
WDS_TRANSPORTCLIENT_AUTH = 1
WDS_TRANSPORTCLIENT_NO_AUTH = 2
def _define_WDS_TRANSPORTPROVIDER_INIT_PARAMS_head():
    class WDS_TRANSPORTPROVIDER_INIT_PARAMS(Structure):
        pass
    return WDS_TRANSPORTPROVIDER_INIT_PARAMS
def _define_WDS_TRANSPORTPROVIDER_INIT_PARAMS():
    WDS_TRANSPORTPROVIDER_INIT_PARAMS = win32more.System.DeploymentServices.WDS_TRANSPORTPROVIDER_INIT_PARAMS_head
    WDS_TRANSPORTPROVIDER_INIT_PARAMS._fields_ = [
        ('ulLength', UInt32),
        ('ulMcServerVersion', UInt32),
        ('hRegistryKey', win32more.System.Registry.HKEY),
        ('hProvider', win32more.Foundation.HANDLE),
    ]
    return WDS_TRANSPORTPROVIDER_INIT_PARAMS
def _define_WDS_TRANSPORTPROVIDER_SETTINGS_head():
    class WDS_TRANSPORTPROVIDER_SETTINGS(Structure):
        pass
    return WDS_TRANSPORTPROVIDER_SETTINGS
def _define_WDS_TRANSPORTPROVIDER_SETTINGS():
    WDS_TRANSPORTPROVIDER_SETTINGS = win32more.System.DeploymentServices.WDS_TRANSPORTPROVIDER_SETTINGS_head
    WDS_TRANSPORTPROVIDER_SETTINGS._fields_ = [
        ('ulLength', UInt32),
        ('ulProviderVersion', UInt32),
    ]
    return WDS_TRANSPORTPROVIDER_SETTINGS
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = Int32
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentPxe = 1
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentTftp = 2
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentImageServer = 4
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentMulticast = 8
WDSTRANSPORT_DISCONNECT_TYPE = Int32
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectUnknown = 0
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectFallback = 1
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectAbort = 2
WDSTRANSPORT_FEATURE_FLAGS = Int32
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureAdminPack = 1
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureTransportServer = 2
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureDeploymentServer = 4
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceUnknown = 0
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceDhcp = 1
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceRange = 2
WDSTRANSPORT_IP_ADDRESS_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressUnknown = 0
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv4 = 1
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv6 = 2
WDSTRANSPORT_NAMESPACE_TYPE = Int32
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeUnknown = 0
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeAutoCast = 1
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastManualStart = 2
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastAutoStart = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE = Int32
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileUnknown = 0
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileCustom = 1
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile10Mbps = 2
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile100Mbps = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile1Gbps = 4
WDSTRANSPORT_PROTOCOL_FLAGS = Int32
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolUnicast = 1
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolMulticast = 2
WDSTRANSPORT_SERVICE_NOTIFICATION = Int32
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyUnknown = 0
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyReadSettings = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = Int32
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingUnknown = 0
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingNone = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingAutoDisconnect = 2
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingMultistream = 3
WDSTRANSPORT_TFTP_CAPABILITY = Int32
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapMaximumBlockSize = 1
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapVariableWindow = 2
WDSTRANSPORT_UDP_PORT_POLICY = Int32
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyDynamic = 0
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyFixed = 1
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
