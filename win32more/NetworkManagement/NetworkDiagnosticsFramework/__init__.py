from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.NetworkDiagnosticsFramework
import win32more.Networking.WinSock
import win32more.Security
import win32more.System.Com
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
NDF_ERROR_START: UInt32 = 63744
NDF_E_LENGTH_EXCEEDED: win32more.Foundation.HRESULT = -2146895616
NDF_E_NOHELPERCLASS: win32more.Foundation.HRESULT = -2146895615
NDF_E_CANCELLED: win32more.Foundation.HRESULT = -2146895614
NDF_E_DISABLED: win32more.Foundation.HRESULT = -2146895612
NDF_E_BAD_PARAM: win32more.Foundation.HRESULT = -2146895611
NDF_E_VALIDATION: win32more.Foundation.HRESULT = -2146895610
NDF_E_UNKNOWN: win32more.Foundation.HRESULT = -2146895609
NDF_E_PROBLEM_PRESENT: win32more.Foundation.HRESULT = -2146895608
RF_WORKAROUND: UInt32 = 536870912
RF_USER_ACTION: UInt32 = 268435456
RF_USER_CONFIRMATION: UInt32 = 134217728
RF_INFORMATION_ONLY: UInt32 = 33554432
RF_UI_ONLY: UInt32 = 16777216
RF_SHOW_EVENTS: UInt32 = 8388608
RF_VALIDATE_HELPTOPIC: UInt32 = 4194304
RF_REPRO: UInt32 = 2097152
RF_CONTACT_ADMIN: UInt32 = 131072
RF_RESERVED: UInt32 = 1073741824
RF_RESERVED_CA: UInt32 = 2147483648
RF_RESERVED_LNI: UInt32 = 65536
RCF_ISLEAF: UInt32 = 1
RCF_ISCONFIRMED: UInt32 = 2
RCF_ISTHIRDPARTY: UInt32 = 4
DF_IMPERSONATION: UInt32 = 2147483648
DF_TRACELESS: UInt32 = 1073741824
NDF_INBOUND_FLAG_EDGETRAVERSAL: UInt32 = 1
NDF_INBOUND_FLAG_HEALTHCHECK: UInt32 = 2
NDF_ADD_CAPTURE_TRACE: UInt32 = 1
NDF_APPLY_INCLUSION_LIST_FILTER: UInt32 = 2
@winfunctype('NDFAPI.dll')
def NdfCreateIncident(helperClassName: win32more.Foundation.PWSTR, celt: UInt32, attributes: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head), handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWinSockIncident(sock: win32more.Networking.WinSock.SOCKET, host: win32more.Foundation.PWSTR, port: UInt16, appId: win32more.Foundation.PWSTR, userId: POINTER(win32more.Security.SID_head), handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncident(url: win32more.Foundation.PWSTR, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncidentEx(url: win32more.Foundation.PWSTR, useWinHTTP: win32more.Foundation.BOOL, moduleName: win32more.Foundation.PWSTR, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateSharingIncident(UNCPath: win32more.Foundation.PWSTR, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateDNSIncident(hostname: win32more.Foundation.PWSTR, queryType: UInt16, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateConnectivityIncident(handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateNetConnectionIncident(handle: POINTER(c_void_p), id: Guid) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreatePnrpIncident(cloudname: win32more.Foundation.PWSTR, peername: win32more.Foundation.PWSTR, diagnosePublish: win32more.Foundation.BOOL, appId: win32more.Foundation.PWSTR, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateGroupingIncident(CloudName: win32more.Foundation.PWSTR, GroupName: win32more.Foundation.PWSTR, Identity: win32more.Foundation.PWSTR, Invitation: win32more.Foundation.PWSTR, Addresses: POINTER(win32more.Networking.WinSock.SOCKET_ADDRESS_LIST_head), appId: win32more.Foundation.PWSTR, handle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfExecuteDiagnosis(handle: c_void_p, hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCloseIncident(handle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfDiagnoseIncident(Handle: c_void_p, RootCauseCount: POINTER(UInt32), RootCauses: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RootCauseInfo_head)), dwWait: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfRepairIncident(Handle: c_void_p, RepairEx: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head), dwWait: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCancelIncident(Handle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfGetTraceFile(Handle: c_void_p, TraceFileLocation: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
ATTRIBUTE_TYPE = Int32
AT_INVALID: ATTRIBUTE_TYPE = 0
AT_BOOLEAN: ATTRIBUTE_TYPE = 1
AT_INT8: ATTRIBUTE_TYPE = 2
AT_UINT8: ATTRIBUTE_TYPE = 3
AT_INT16: ATTRIBUTE_TYPE = 4
AT_UINT16: ATTRIBUTE_TYPE = 5
AT_INT32: ATTRIBUTE_TYPE = 6
AT_UINT32: ATTRIBUTE_TYPE = 7
AT_INT64: ATTRIBUTE_TYPE = 8
AT_UINT64: ATTRIBUTE_TYPE = 9
AT_STRING: ATTRIBUTE_TYPE = 10
AT_GUID: ATTRIBUTE_TYPE = 11
AT_LIFE_TIME: ATTRIBUTE_TYPE = 12
AT_SOCKADDR: ATTRIBUTE_TYPE = 13
AT_OCTET_STRING: ATTRIBUTE_TYPE = 14
class DIAG_SOCKADDR(Structure):
    family: UInt16
    data: win32more.Foundation.CHAR * 126
DIAGNOSIS_STATUS = Int32
DS_NOT_IMPLEMENTED: DIAGNOSIS_STATUS = 0
DS_CONFIRMED: DIAGNOSIS_STATUS = 1
DS_REJECTED: DIAGNOSIS_STATUS = 2
DS_INDETERMINATE: DIAGNOSIS_STATUS = 3
DS_DEFERRED: DIAGNOSIS_STATUS = 4
DS_PASSTHROUGH: DIAGNOSIS_STATUS = 5
class DiagnosticsInfo(Structure):
    cost: Int32
    flags: UInt32
class HELPER_ATTRIBUTE(Structure):
    pwszName: win32more.Foundation.PWSTR
    type: win32more.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Boolean: win32more.Foundation.BOOL
        Char: Byte
        Byte: Byte
        Short: Int16
        Word: UInt16
        Int: Int32
        DWord: UInt32
        Int64: Int64
        UInt64: UInt64
        PWStr: win32more.Foundation.PWSTR
        Guid: Guid
        LifeTime: win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME
        Address: win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAG_SOCKADDR
        OctetString: win32more.NetworkManagement.NetworkDiagnosticsFramework.OCTET_STRING
class HelperAttributeInfo(Structure):
    pwszName: win32more.Foundation.PWSTR
    type: win32more.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
class HYPOTHESIS(Structure):
    pwszClassName: win32more.Foundation.PWSTR
    pwszDescription: win32more.Foundation.PWSTR
    celt: UInt32
    rgAttributes: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)
class HypothesisResult(Structure):
    hypothesis: win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS
    pathStatus: win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS
class INetDiagExtensibleHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0b35748-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def ResolveAttributes(celt: UInt32, rgKeyAttributes: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head), pcelt: POINTER(UInt32), prgMatchValues: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> win32more.Foundation.HRESULT: ...
class INetDiagHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0b35746-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def Initialize(celt: UInt32, rgAttributes: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDiagnosticsInfo(ppInfo: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DiagnosticsInfo_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyAttributes(pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def LowHealth(pwszInstanceDescription: win32more.Foundation.PWSTR, ppwszDescription: POINTER(win32more.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def HighUtilization(pwszInstanceDescription: win32more.Foundation.PWSTR, ppwszDescription: POINTER(win32more.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetLowerHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDownStreamHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetHigherHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetUpStreamHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Repair(pInfo: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Validate(problem: win32more.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRepairInfo(problem: win32more.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pcelt: POINTER(UInt32), ppInfo: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetLifeTime(pLifeTime: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetLifeTime(lifeTime: win32more.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetCacheTime(pCacheTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetAttributes(pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Cleanup() -> win32more.Foundation.HRESULT: ...
class INetDiagHelperEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('972dab4d-e4e3-4fc6-ae-54-5f-65-cc-de-4a-15')
    @commethod(3)
    def ReconfirmLowHealth(celt: UInt32, pResults: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HypothesisResult_head), ppwszUpdatedDescription: POINTER(win32more.Foundation.PWSTR), pUpdatedStatus: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetUtilities(pUtilities: win32more.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperUtilFactory_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReproduceFailure() -> win32more.Foundation.HRESULT: ...
class INetDiagHelperInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0b35747-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def GetAttributeInfo(pcelt: POINTER(UInt32), pprgAttributeInfos: POINTER(POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.HelperAttributeInfo_head))) -> win32more.Foundation.HRESULT: ...
class INetDiagHelperUtilFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('104613fb-bc57-4178-95-ba-88-80-96-98-35-4a')
    @commethod(3)
    def CreateUtilityInstance(riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class LIFE_TIME(Structure):
    startTime: win32more.Foundation.FILETIME
    endTime: win32more.Foundation.FILETIME
class OCTET_STRING(Structure):
    dwLength: UInt32
    lpValue: c_char_p_no
PROBLEM_TYPE = Int32
PT_INVALID: PROBLEM_TYPE = 0
PT_LOW_HEALTH: PROBLEM_TYPE = 1
PT_LOWER_HEALTH: PROBLEM_TYPE = 2
PT_DOWN_STREAM_HEALTH: PROBLEM_TYPE = 4
PT_HIGH_UTILIZATION: PROBLEM_TYPE = 8
PT_HIGHER_UTILIZATION: PROBLEM_TYPE = 16
PT_UP_STREAM_UTILIZATION: PROBLEM_TYPE = 32
REPAIR_RISK = Int32
RR_NOROLLBACK: REPAIR_RISK = 0
RR_ROLLBACK: REPAIR_RISK = 1
RR_NORISK: REPAIR_RISK = 2
REPAIR_SCOPE = Int32
RS_SYSTEM: REPAIR_SCOPE = 0
RS_USER: REPAIR_SCOPE = 1
RS_APPLICATION: REPAIR_SCOPE = 2
RS_PROCESS: REPAIR_SCOPE = 3
REPAIR_STATUS = Int32
RS_NOT_IMPLEMENTED: REPAIR_STATUS = 0
RS_REPAIRED: REPAIR_STATUS = 1
RS_UNREPAIRED: REPAIR_STATUS = 2
RS_DEFERRED: REPAIR_STATUS = 3
RS_USER_ACTION: REPAIR_STATUS = 4
class RepairInfo(Structure):
    guid: Guid
    pwszClassName: win32more.Foundation.PWSTR
    pwszDescription: win32more.Foundation.PWSTR
    sidType: UInt32
    cost: Int32
    flags: UInt32
    scope: win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE
    risk: win32more.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK
    UiInfo: win32more.NetworkManagement.NetworkDiagnosticsFramework.UiInfo
    rootCauseIndex: Int32
class RepairInfoEx(Structure):
    repair: win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo
    repairRank: UInt16
class RootCauseInfo(Structure):
    pwszDescription: win32more.Foundation.PWSTR
    rootCauseID: Guid
    rootCauseFlags: UInt32
    networkInterfaceID: Guid
    pRepairs: POINTER(win32more.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head)
    repairCount: UInt16
class ShellCommandInfo(Structure):
    pwszOperation: win32more.Foundation.PWSTR
    pwszFile: win32more.Foundation.PWSTR
    pwszParameters: win32more.Foundation.PWSTR
    pwszDirectory: win32more.Foundation.PWSTR
    nShowCmd: UInt32
UI_INFO_TYPE = Int32
UIT_INVALID: UI_INFO_TYPE = 0
UIT_NONE: UI_INFO_TYPE = 1
UIT_SHELL_COMMAND: UI_INFO_TYPE = 2
UIT_HELP_PANE: UI_INFO_TYPE = 3
UIT_DUI: UI_INFO_TYPE = 4
class UiInfo(Structure):
    type: win32more.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pwzNull: win32more.Foundation.PWSTR
        ShellInfo: win32more.NetworkManagement.NetworkDiagnosticsFramework.ShellCommandInfo
        pwzHelpUrl: win32more.Foundation.PWSTR
        pwzDui: win32more.Foundation.PWSTR
make_head(_module, 'DIAG_SOCKADDR')
make_head(_module, 'DiagnosticsInfo')
make_head(_module, 'HELPER_ATTRIBUTE')
make_head(_module, 'HelperAttributeInfo')
make_head(_module, 'HYPOTHESIS')
make_head(_module, 'HypothesisResult')
make_head(_module, 'INetDiagExtensibleHelper')
make_head(_module, 'INetDiagHelper')
make_head(_module, 'INetDiagHelperEx')
make_head(_module, 'INetDiagHelperInfo')
make_head(_module, 'INetDiagHelperUtilFactory')
make_head(_module, 'LIFE_TIME')
make_head(_module, 'OCTET_STRING')
make_head(_module, 'RepairInfo')
make_head(_module, 'RepairInfoEx')
make_head(_module, 'RootCauseInfo')
make_head(_module, 'ShellCommandInfo')
make_head(_module, 'UiInfo')
__all__ = [
    "ATTRIBUTE_TYPE",
    "AT_BOOLEAN",
    "AT_GUID",
    "AT_INT16",
    "AT_INT32",
    "AT_INT64",
    "AT_INT8",
    "AT_INVALID",
    "AT_LIFE_TIME",
    "AT_OCTET_STRING",
    "AT_SOCKADDR",
    "AT_STRING",
    "AT_UINT16",
    "AT_UINT32",
    "AT_UINT64",
    "AT_UINT8",
    "DF_IMPERSONATION",
    "DF_TRACELESS",
    "DIAGNOSIS_STATUS",
    "DIAG_SOCKADDR",
    "DS_CONFIRMED",
    "DS_DEFERRED",
    "DS_INDETERMINATE",
    "DS_NOT_IMPLEMENTED",
    "DS_PASSTHROUGH",
    "DS_REJECTED",
    "DiagnosticsInfo",
    "HELPER_ATTRIBUTE",
    "HYPOTHESIS",
    "HelperAttributeInfo",
    "HypothesisResult",
    "INetDiagExtensibleHelper",
    "INetDiagHelper",
    "INetDiagHelperEx",
    "INetDiagHelperInfo",
    "INetDiagHelperUtilFactory",
    "LIFE_TIME",
    "NDF_ADD_CAPTURE_TRACE",
    "NDF_APPLY_INCLUSION_LIST_FILTER",
    "NDF_ERROR_START",
    "NDF_E_BAD_PARAM",
    "NDF_E_CANCELLED",
    "NDF_E_DISABLED",
    "NDF_E_LENGTH_EXCEEDED",
    "NDF_E_NOHELPERCLASS",
    "NDF_E_PROBLEM_PRESENT",
    "NDF_E_UNKNOWN",
    "NDF_E_VALIDATION",
    "NDF_INBOUND_FLAG_EDGETRAVERSAL",
    "NDF_INBOUND_FLAG_HEALTHCHECK",
    "NdfCancelIncident",
    "NdfCloseIncident",
    "NdfCreateConnectivityIncident",
    "NdfCreateDNSIncident",
    "NdfCreateGroupingIncident",
    "NdfCreateIncident",
    "NdfCreateNetConnectionIncident",
    "NdfCreatePnrpIncident",
    "NdfCreateSharingIncident",
    "NdfCreateWebIncident",
    "NdfCreateWebIncidentEx",
    "NdfCreateWinSockIncident",
    "NdfDiagnoseIncident",
    "NdfExecuteDiagnosis",
    "NdfGetTraceFile",
    "NdfRepairIncident",
    "OCTET_STRING",
    "PROBLEM_TYPE",
    "PT_DOWN_STREAM_HEALTH",
    "PT_HIGHER_UTILIZATION",
    "PT_HIGH_UTILIZATION",
    "PT_INVALID",
    "PT_LOWER_HEALTH",
    "PT_LOW_HEALTH",
    "PT_UP_STREAM_UTILIZATION",
    "RCF_ISCONFIRMED",
    "RCF_ISLEAF",
    "RCF_ISTHIRDPARTY",
    "REPAIR_RISK",
    "REPAIR_SCOPE",
    "REPAIR_STATUS",
    "RF_CONTACT_ADMIN",
    "RF_INFORMATION_ONLY",
    "RF_REPRO",
    "RF_RESERVED",
    "RF_RESERVED_CA",
    "RF_RESERVED_LNI",
    "RF_SHOW_EVENTS",
    "RF_UI_ONLY",
    "RF_USER_ACTION",
    "RF_USER_CONFIRMATION",
    "RF_VALIDATE_HELPTOPIC",
    "RF_WORKAROUND",
    "RR_NORISK",
    "RR_NOROLLBACK",
    "RR_ROLLBACK",
    "RS_APPLICATION",
    "RS_DEFERRED",
    "RS_NOT_IMPLEMENTED",
    "RS_PROCESS",
    "RS_REPAIRED",
    "RS_SYSTEM",
    "RS_UNREPAIRED",
    "RS_USER",
    "RS_USER_ACTION",
    "RepairInfo",
    "RepairInfoEx",
    "RootCauseInfo",
    "ShellCommandInfo",
    "UIT_DUI",
    "UIT_HELP_PANE",
    "UIT_INVALID",
    "UIT_NONE",
    "UIT_SHELL_COMMAND",
    "UI_INFO_TYPE",
    "UiInfo",
]
