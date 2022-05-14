from win32more import *
import win32more.NetworkManagement.NetworkDiagnosticsFramework
import win32more.Foundation
import win32more.Networking.WinSock
import win32more.Security
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.NetworkManagement.NetworkDiagnosticsFramework, name, eval(f"_define_{name}()"))
    return getattr(win32more.NetworkManagement.NetworkDiagnosticsFramework, name)
NDF_ERROR_START = 63744
NDF_E_LENGTH_EXCEEDED = -2146895616
NDF_E_NOHELPERCLASS = -2146895615
NDF_E_CANCELLED = -2146895614
NDF_E_DISABLED = -2146895612
NDF_E_BAD_PARAM = -2146895611
NDF_E_VALIDATION = -2146895610
NDF_E_UNKNOWN = -2146895609
NDF_E_PROBLEM_PRESENT = -2146895608
RF_WORKAROUND = 536870912
RF_USER_ACTION = 268435456
RF_USER_CONFIRMATION = 134217728
RF_INFORMATION_ONLY = 33554432
RF_UI_ONLY = 16777216
RF_SHOW_EVENTS = 8388608
RF_VALIDATE_HELPTOPIC = 4194304
RF_REPRO = 2097152
RF_CONTACT_ADMIN = 131072
RF_RESERVED = 1073741824
RF_RESERVED_CA = 2147483648
RF_RESERVED_LNI = 65536
RCF_ISLEAF = 1
RCF_ISCONFIRMED = 2
RCF_ISTHIRDPARTY = 4
DF_IMPERSONATION = 2147483648
DF_TRACELESS = 1073741824
NDF_INBOUND_FLAG_EDGETRAVERSAL = 1
NDF_INBOUND_FLAG_HEALTHCHECK = 2
NDF_ADD_CAPTURE_TRACE = 1
NDF_APPLY_INCLUSION_LIST_FILTER = 2
ATTRIBUTE_TYPE = Int32
AT_INVALID = 0
AT_BOOLEAN = 1
AT_INT8 = 2
AT_UINT8 = 3
AT_INT16 = 4
AT_UINT16 = 5
AT_INT32 = 6
AT_UINT32 = 7
AT_INT64 = 8
AT_UINT64 = 9
AT_STRING = 10
AT_GUID = 11
AT_LIFE_TIME = 12
AT_SOCKADDR = 13
AT_OCTET_STRING = 14
def _define_OCTET_STRING_head():
    class OCTET_STRING(Structure):
        pass
    return OCTET_STRING
def _define_OCTET_STRING():
    OCTET_STRING = win32more.NetworkManagement.NetworkDiagnosticsFramework.OCTET_STRING_head
    OCTET_STRING._fields_ = [
        ("dwLength", UInt32),
        ("lpValue", c_char_p_no),
    ]
    return OCTET_STRING
def _define_LIFE_TIME_head():
    class LIFE_TIME(Structure):
        pass
    return LIFE_TIME
def _define_LIFE_TIME():
    LIFE_TIME = win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME_head
    LIFE_TIME._fields_ = [
        ("startTime", win32more.Foundation.FILETIME),
        ("endTime", win32more.Foundation.FILETIME),
    ]
    return LIFE_TIME
def _define_DIAG_SOCKADDR_head():
    class DIAG_SOCKADDR(Structure):
        pass
    return DIAG_SOCKADDR
def _define_DIAG_SOCKADDR():
    DIAG_SOCKADDR = win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAG_SOCKADDR_head
    DIAG_SOCKADDR._fields_ = [
        ("family", UInt16),
        ("data", win32more.Foundation.CHAR * 126),
    ]
    return DIAG_SOCKADDR
def _define_HELPER_ATTRIBUTE_head():
    class HELPER_ATTRIBUTE(Structure):
        pass
    return HELPER_ATTRIBUTE
def _define_HELPER_ATTRIBUTE():
    HELPER_ATTRIBUTE = win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head
    class HELPER_ATTRIBUTE__Anonymous_e__Union(Union):
        pass
    HELPER_ATTRIBUTE__Anonymous_e__Union._fields_ = [
        ("Boolean", win32more.Foundation.BOOL),
        ("Char", Byte),
        ("Byte", Byte),
        ("Short", Int16),
        ("Word", UInt16),
        ("Int", Int32),
        ("DWord", UInt32),
        ("Int64", Int64),
        ("UInt64", UInt64),
        ("PWStr", win32more.Foundation.PWSTR),
        ("Guid", Guid),
        ("LifeTime", win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME),
        ("Address", win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAG_SOCKADDR),
        ("OctetString", win32more.NetworkManagement.NetworkDiagnosticsFramework.OCTET_STRING),
    ]
    HELPER_ATTRIBUTE._anonymous_ = [
        'Anonymous',
    ]
    HELPER_ATTRIBUTE._fields_ = [
        ("pwszName", win32more.Foundation.PWSTR),
        ("type", win32more.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE),
        ("Anonymous", HELPER_ATTRIBUTE__Anonymous_e__Union),
    ]
    return HELPER_ATTRIBUTE
REPAIR_SCOPE = Int32
RS_SYSTEM = 0
RS_USER = 1
RS_APPLICATION = 2
RS_PROCESS = 3
REPAIR_RISK = Int32
RR_NOROLLBACK = 0
RR_ROLLBACK = 1
RR_NORISK = 2
UI_INFO_TYPE = Int32
UIT_INVALID = 0
UIT_NONE = 1
UIT_SHELL_COMMAND = 2
UIT_HELP_PANE = 3
UIT_DUI = 4
def _define_ShellCommandInfo_head():
    class ShellCommandInfo(Structure):
        pass
    return ShellCommandInfo
def _define_ShellCommandInfo():
    ShellCommandInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.ShellCommandInfo_head
    ShellCommandInfo._fields_ = [
        ("pwszOperation", win32more.Foundation.PWSTR),
        ("pwszFile", win32more.Foundation.PWSTR),
        ("pwszParameters", win32more.Foundation.PWSTR),
        ("pwszDirectory", win32more.Foundation.PWSTR),
        ("nShowCmd", UInt32),
    ]
    return ShellCommandInfo
def _define_UiInfo_head():
    class UiInfo(Structure):
        pass
    return UiInfo
def _define_UiInfo():
    UiInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.UiInfo_head
    class UiInfo__Anonymous_e__Union(Union):
        pass
    UiInfo__Anonymous_e__Union._fields_ = [
        ("pwzNull", win32more.Foundation.PWSTR),
        ("ShellInfo", win32more.NetworkManagement.NetworkDiagnosticsFramework.ShellCommandInfo),
        ("pwzHelpUrl", win32more.Foundation.PWSTR),
        ("pwzDui", win32more.Foundation.PWSTR),
    ]
    UiInfo._anonymous_ = [
        'Anonymous',
    ]
    UiInfo._fields_ = [
        ("type", win32more.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE),
        ("Anonymous", UiInfo__Anonymous_e__Union),
    ]
    return UiInfo
def _define_RepairInfo_head():
    class RepairInfo(Structure):
        pass
    return RepairInfo
def _define_RepairInfo():
    RepairInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head
    RepairInfo._fields_ = [
        ("guid", Guid),
        ("pwszClassName", win32more.Foundation.PWSTR),
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("sidType", UInt32),
        ("cost", Int32),
        ("flags", UInt32),
        ("scope", win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE),
        ("risk", win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK),
        ("UiInfo", win32more.NetworkManagement.NetworkDiagnosticsFramework.UiInfo),
        ("rootCauseIndex", Int32),
    ]
    return RepairInfo
def _define_RepairInfoEx_head():
    class RepairInfoEx(Structure):
        pass
    return RepairInfoEx
def _define_RepairInfoEx():
    RepairInfoEx = win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head
    RepairInfoEx._fields_ = [
        ("repair", win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo),
        ("repairRank", UInt16),
    ]
    return RepairInfoEx
def _define_RootCauseInfo_head():
    class RootCauseInfo(Structure):
        pass
    return RootCauseInfo
def _define_RootCauseInfo():
    RootCauseInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.RootCauseInfo_head
    RootCauseInfo._fields_ = [
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("rootCauseID", Guid),
        ("rootCauseFlags", UInt32),
        ("networkInterfaceID", Guid),
        ("pRepairs", POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head)),
        ("repairCount", UInt16),
    ]
    return RootCauseInfo
DIAGNOSIS_STATUS = Int32
DS_NOT_IMPLEMENTED = 0
DS_CONFIRMED = 1
DS_REJECTED = 2
DS_INDETERMINATE = 3
DS_DEFERRED = 4
DS_PASSTHROUGH = 5
REPAIR_STATUS = Int32
RS_NOT_IMPLEMENTED = 0
RS_REPAIRED = 1
RS_UNREPAIRED = 2
RS_DEFERRED = 3
RS_USER_ACTION = 4
PROBLEM_TYPE = Int32
PT_INVALID = 0
PT_LOW_HEALTH = 1
PT_LOWER_HEALTH = 2
PT_DOWN_STREAM_HEALTH = 4
PT_HIGH_UTILIZATION = 8
PT_HIGHER_UTILIZATION = 16
PT_UP_STREAM_UTILIZATION = 32
def _define_HYPOTHESIS_head():
    class HYPOTHESIS(Structure):
        pass
    return HYPOTHESIS
def _define_HYPOTHESIS():
    HYPOTHESIS = win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head
    HYPOTHESIS._fields_ = [
        ("pwszClassName", win32more.Foundation.PWSTR),
        ("pwszDescription", win32more.Foundation.PWSTR),
        ("celt", UInt32),
        ("rgAttributes", POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)),
    ]
    return HYPOTHESIS
def _define_HelperAttributeInfo_head():
    class HelperAttributeInfo(Structure):
        pass
    return HelperAttributeInfo
def _define_HelperAttributeInfo():
    HelperAttributeInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.HelperAttributeInfo_head
    HelperAttributeInfo._fields_ = [
        ("pwszName", win32more.Foundation.PWSTR),
        ("type", win32more.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE),
    ]
    return HelperAttributeInfo
def _define_DiagnosticsInfo_head():
    class DiagnosticsInfo(Structure):
        pass
    return DiagnosticsInfo
def _define_DiagnosticsInfo():
    DiagnosticsInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.DiagnosticsInfo_head
    DiagnosticsInfo._fields_ = [
        ("cost", Int32),
        ("flags", UInt32),
    ]
    return DiagnosticsInfo
def _define_INetDiagHelper_head():
    class INetDiagHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0b35746-ebf5-11d8-bbe9-505054503030')
    return INetDiagHelper
def _define_INetDiagHelper():
    INetDiagHelper = win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelper_head
    INetDiagHelper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE), use_last_error=False)(3, 'Initialize', ((1, 'celt'),(1, 'rgAttributes'),)))
    INetDiagHelper.GetDiagnosticsInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DiagnosticsInfo_head)), use_last_error=False)(4, 'GetDiagnosticsInfo', ((1, 'ppInfo'),)))
    INetDiagHelper.GetKeyAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)), use_last_error=False)(5, 'GetKeyAttributes', ((1, 'pcelt'),(1, 'pprgAttributes'),)))
    INetDiagHelper.LowHealth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(Int32),POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS), use_last_error=False)(6, 'LowHealth', ((1, 'pwszInstanceDescription'),(1, 'ppwszDescription'),(1, 'pDeferredTime'),(1, 'pStatus'),)))
    INetDiagHelper.HighUtilization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(Int32),POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS), use_last_error=False)(7, 'HighUtilization', ((1, 'pwszInstanceDescription'),(1, 'ppwszDescription'),(1, 'pDeferredTime'),(1, 'pStatus'),)))
    INetDiagHelper.GetLowerHypotheses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head)), use_last_error=False)(8, 'GetLowerHypotheses', ((1, 'pcelt'),(1, 'pprgHypotheses'),)))
    INetDiagHelper.GetDownStreamHypotheses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head)), use_last_error=False)(9, 'GetDownStreamHypotheses', ((1, 'pcelt'),(1, 'pprgHypotheses'),)))
    INetDiagHelper.GetHigherHypotheses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head)), use_last_error=False)(10, 'GetHigherHypotheses', ((1, 'pcelt'),(1, 'pprgHypotheses'),)))
    INetDiagHelper.GetUpStreamHypotheses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head)), use_last_error=False)(11, 'GetUpStreamHypotheses', ((1, 'pcelt'),(1, 'pprgHypotheses'),)))
    INetDiagHelper.Repair = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head),POINTER(Int32),POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS), use_last_error=False)(12, 'Repair', ((1, 'pInfo'),(1, 'pDeferredTime'),(1, 'pStatus'),)))
    INetDiagHelper.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE,POINTER(Int32),POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS), use_last_error=False)(13, 'Validate', ((1, 'problem'),(1, 'pDeferredTime'),(1, 'pStatus'),)))
    INetDiagHelper.GetRepairInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head)), use_last_error=False)(14, 'GetRepairInfo', ((1, 'problem'),(1, 'pcelt'),(1, 'ppInfo'),)))
    INetDiagHelper.GetLifeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME_head), use_last_error=False)(15, 'GetLifeTime', ((1, 'pLifeTime'),)))
    INetDiagHelper.SetLifeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME, use_last_error=False)(16, 'SetLifeTime', ((1, 'lifeTime'),)))
    INetDiagHelper.GetCacheTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(17, 'GetCacheTime', ((1, 'pCacheTime'),)))
    INetDiagHelper.GetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)), use_last_error=False)(18, 'GetAttributes', ((1, 'pcelt'),(1, 'pprgAttributes'),)))
    INetDiagHelper.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'Cancel', ()))
    INetDiagHelper.Cleanup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Cleanup', ()))
    return INetDiagHelper
def _define_HypothesisResult_head():
    class HypothesisResult(Structure):
        pass
    return HypothesisResult
def _define_HypothesisResult():
    HypothesisResult = win32more.NetworkManagement.NetworkDiagnosticsFramework.HypothesisResult_head
    HypothesisResult._fields_ = [
        ("hypothesis", win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS),
        ("pathStatus", win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS),
    ]
    return HypothesisResult
def _define_INetDiagHelperUtilFactory_head():
    class INetDiagHelperUtilFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('104613fb-bc57-4178-95ba-88809698354a')
    return INetDiagHelperUtilFactory
def _define_INetDiagHelperUtilFactory():
    INetDiagHelperUtilFactory = win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperUtilFactory_head
    INetDiagHelperUtilFactory.CreateUtilityInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateUtilityInstance', ((1, 'riid'),(1, 'ppvObject'),)))
    return INetDiagHelperUtilFactory
def _define_INetDiagHelperEx_head():
    class INetDiagHelperEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('972dab4d-e4e3-4fc6-ae54-5f65ccde4a15')
    return INetDiagHelperEx
def _define_INetDiagHelperEx():
    INetDiagHelperEx = win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperEx_head
    INetDiagHelperEx.ReconfirmLowHealth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HypothesisResult),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS), use_last_error=False)(3, 'ReconfirmLowHealth', ((1, 'celt'),(1, 'pResults'),(1, 'ppwszUpdatedDescription'),(1, 'pUpdatedStatus'),)))
    INetDiagHelperEx.SetUtilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperUtilFactory_head, use_last_error=False)(4, 'SetUtilities', ((1, 'pUtilities'),)))
    INetDiagHelperEx.ReproduceFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ReproduceFailure', ()))
    return INetDiagHelperEx
def _define_INetDiagHelperInfo_head():
    class INetDiagHelperInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0b35747-ebf5-11d8-bbe9-505054503030')
    return INetDiagHelperInfo
def _define_INetDiagHelperInfo():
    INetDiagHelperInfo = win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperInfo_head
    INetDiagHelperInfo.GetAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HelperAttributeInfo_head)), use_last_error=False)(3, 'GetAttributeInfo', ((1, 'pcelt'),(1, 'pprgAttributeInfos'),)))
    return INetDiagHelperInfo
def _define_INetDiagExtensibleHelper_head():
    class INetDiagExtensibleHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0b35748-ebf5-11d8-bbe9-505054503030')
    return INetDiagExtensibleHelper
def _define_INetDiagExtensibleHelper():
    INetDiagExtensibleHelper = win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagExtensibleHelper_head
    INetDiagExtensibleHelper.ResolveAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE),POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)), use_last_error=False)(3, 'ResolveAttributes', ((1, 'celt'),(1, 'rgKeyAttributes'),(1, 'pcelt'),(1, 'prgMatchValues'),)))
    return INetDiagExtensibleHelper
def _define_NdfCreateIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE),POINTER(c_void_p), use_last_error=False)(("NdfCreateIncident", windll["NDFAPI"]), ((1, 'helperClassName'),(1, 'celt'),(1, 'attributes'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateWinSockIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WinSock.SOCKET,win32more.Foundation.PWSTR,UInt16,win32more.Foundation.PWSTR,POINTER(win32more.Security.SID_head),POINTER(c_void_p), use_last_error=False)(("NdfCreateWinSockIncident", windll["NDFAPI"]), ((1, 'sock'),(1, 'host'),(1, 'port'),(1, 'appId'),(1, 'userId'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateWebIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("NdfCreateWebIncident", windll["NDFAPI"]), ((1, 'url'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateWebIncidentEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("NdfCreateWebIncidentEx", windll["NDFAPI"]), ((1, 'url'),(1, 'useWinHTTP'),(1, 'moduleName'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateSharingIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("NdfCreateSharingIncident", windll["NDFAPI"]), ((1, 'UNCPath'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateDNSIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,POINTER(c_void_p), use_last_error=False)(("NdfCreateDNSIncident", windll["NDFAPI"]), ((1, 'hostname'),(1, 'queryType'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateConnectivityIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(("NdfCreateConnectivityIncident", windll["NDFAPI"]), ((1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateNetConnectionIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p),Guid, use_last_error=False)(("NdfCreateNetConnectionIncident", windll["NDFAPI"]), ((1, 'handle'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreatePnrpIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("NdfCreatePnrpIncident", windll["NDFAPI"]), ((1, 'cloudname'),(1, 'peername'),(1, 'diagnosePublish'),(1, 'appId'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCreateGroupingIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_LIST_head),win32more.Foundation.PWSTR,POINTER(c_void_p), use_last_error=False)(("NdfCreateGroupingIncident", windll["NDFAPI"]), ((1, 'CloudName'),(1, 'GroupName'),(1, 'Identity'),(1, 'Invitation'),(1, 'Addresses'),(1, 'appId'),(1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfExecuteDiagnosis():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.HWND, use_last_error=False)(("NdfExecuteDiagnosis", windll["NDFAPI"]), ((1, 'handle'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCloseIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("NdfCloseIncident", windll["NDFAPI"]), ((1, 'handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfDiagnoseIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RootCauseInfo_head)),UInt32,UInt32, use_last_error=False)(("NdfDiagnoseIncident", windll["NDFAPI"]), ((1, 'Handle'),(1, 'RootCauseCount'),(1, 'RootCauses'),(1, 'dwWait'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfRepairIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head),UInt32, use_last_error=False)(("NdfRepairIncident", windll["NDFAPI"]), ((1, 'Handle'),(1, 'RepairEx'),(1, 'dwWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfCancelIncident():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("NdfCancelIncident", windll["NDFAPI"]), ((1, 'Handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NdfGetTraceFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("NdfGetTraceFile", windll["NDFAPI"]), ((1, 'Handle'),(1, 'TraceFileLocation'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NDF_ERROR_START",
    "NDF_E_LENGTH_EXCEEDED",
    "NDF_E_NOHELPERCLASS",
    "NDF_E_CANCELLED",
    "NDF_E_DISABLED",
    "NDF_E_BAD_PARAM",
    "NDF_E_VALIDATION",
    "NDF_E_UNKNOWN",
    "NDF_E_PROBLEM_PRESENT",
    "RF_WORKAROUND",
    "RF_USER_ACTION",
    "RF_USER_CONFIRMATION",
    "RF_INFORMATION_ONLY",
    "RF_UI_ONLY",
    "RF_SHOW_EVENTS",
    "RF_VALIDATE_HELPTOPIC",
    "RF_REPRO",
    "RF_CONTACT_ADMIN",
    "RF_RESERVED",
    "RF_RESERVED_CA",
    "RF_RESERVED_LNI",
    "RCF_ISLEAF",
    "RCF_ISCONFIRMED",
    "RCF_ISTHIRDPARTY",
    "DF_IMPERSONATION",
    "DF_TRACELESS",
    "NDF_INBOUND_FLAG_EDGETRAVERSAL",
    "NDF_INBOUND_FLAG_HEALTHCHECK",
    "NDF_ADD_CAPTURE_TRACE",
    "NDF_APPLY_INCLUSION_LIST_FILTER",
    "ATTRIBUTE_TYPE",
    "AT_INVALID",
    "AT_BOOLEAN",
    "AT_INT8",
    "AT_UINT8",
    "AT_INT16",
    "AT_UINT16",
    "AT_INT32",
    "AT_UINT32",
    "AT_INT64",
    "AT_UINT64",
    "AT_STRING",
    "AT_GUID",
    "AT_LIFE_TIME",
    "AT_SOCKADDR",
    "AT_OCTET_STRING",
    "OCTET_STRING",
    "LIFE_TIME",
    "DIAG_SOCKADDR",
    "HELPER_ATTRIBUTE",
    "REPAIR_SCOPE",
    "RS_SYSTEM",
    "RS_USER",
    "RS_APPLICATION",
    "RS_PROCESS",
    "REPAIR_RISK",
    "RR_NOROLLBACK",
    "RR_ROLLBACK",
    "RR_NORISK",
    "UI_INFO_TYPE",
    "UIT_INVALID",
    "UIT_NONE",
    "UIT_SHELL_COMMAND",
    "UIT_HELP_PANE",
    "UIT_DUI",
    "ShellCommandInfo",
    "UiInfo",
    "RepairInfo",
    "RepairInfoEx",
    "RootCauseInfo",
    "DIAGNOSIS_STATUS",
    "DS_NOT_IMPLEMENTED",
    "DS_CONFIRMED",
    "DS_REJECTED",
    "DS_INDETERMINATE",
    "DS_DEFERRED",
    "DS_PASSTHROUGH",
    "REPAIR_STATUS",
    "RS_NOT_IMPLEMENTED",
    "RS_REPAIRED",
    "RS_UNREPAIRED",
    "RS_DEFERRED",
    "RS_USER_ACTION",
    "PROBLEM_TYPE",
    "PT_INVALID",
    "PT_LOW_HEALTH",
    "PT_LOWER_HEALTH",
    "PT_DOWN_STREAM_HEALTH",
    "PT_HIGH_UTILIZATION",
    "PT_HIGHER_UTILIZATION",
    "PT_UP_STREAM_UTILIZATION",
    "HYPOTHESIS",
    "HelperAttributeInfo",
    "DiagnosticsInfo",
    "INetDiagHelper",
    "HypothesisResult",
    "INetDiagHelperUtilFactory",
    "INetDiagHelperEx",
    "INetDiagHelperInfo",
    "INetDiagExtensibleHelper",
    "NdfCreateIncident",
    "NdfCreateWinSockIncident",
    "NdfCreateWebIncident",
    "NdfCreateWebIncidentEx",
    "NdfCreateSharingIncident",
    "NdfCreateDNSIncident",
    "NdfCreateConnectivityIncident",
    "NdfCreateNetConnectionIncident",
    "NdfCreatePnrpIncident",
    "NdfCreateGroupingIncident",
    "NdfExecuteDiagnosis",
    "NdfCloseIncident",
    "NdfDiagnoseIncident",
    "NdfRepairIncident",
    "NdfCancelIncident",
    "NdfGetTraceFile",
]
