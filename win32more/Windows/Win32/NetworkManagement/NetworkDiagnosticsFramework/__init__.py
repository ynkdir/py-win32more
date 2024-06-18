from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
ATTRIBUTE_TYPE = Int32
AT_INVALID: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 0
AT_BOOLEAN: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 1
AT_INT8: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 2
AT_UINT8: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 3
AT_INT16: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 4
AT_UINT16: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 5
AT_INT32: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 6
AT_UINT32: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 7
AT_INT64: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 8
AT_UINT64: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 9
AT_STRING: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 10
AT_GUID: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 11
AT_LIFE_TIME: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 12
AT_SOCKADDR: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 13
AT_OCTET_STRING: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE = 14
NDF_ERROR_START: UInt32 = 63744
NDF_E_LENGTH_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2146895616
NDF_E_NOHELPERCLASS: win32more.Windows.Win32.Foundation.HRESULT = -2146895615
NDF_E_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2146895614
NDF_E_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2146895612
NDF_E_BAD_PARAM: win32more.Windows.Win32.Foundation.HRESULT = -2146895611
NDF_E_VALIDATION: win32more.Windows.Win32.Foundation.HRESULT = -2146895610
NDF_E_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -2146895609
NDF_E_PROBLEM_PRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2146895608
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
def NdfCreateIncident(helperClassName: win32more.Windows.Win32.Foundation.PWSTR, celt: UInt32, attributes: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE), handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWinSockIncident(sock: win32more.Windows.Win32.Networking.WinSock.SOCKET, host: win32more.Windows.Win32.Foundation.PWSTR, port: UInt16, appId: win32more.Windows.Win32.Foundation.PWSTR, userId: POINTER(win32more.Windows.Win32.Security.SID), handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncident(url: win32more.Windows.Win32.Foundation.PWSTR, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncidentEx(url: win32more.Windows.Win32.Foundation.PWSTR, useWinHTTP: win32more.Windows.Win32.Foundation.BOOL, moduleName: win32more.Windows.Win32.Foundation.PWSTR, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateSharingIncident(UNCPath: win32more.Windows.Win32.Foundation.PWSTR, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateDNSIncident(hostname: win32more.Windows.Win32.Foundation.PWSTR, queryType: UInt16, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateConnectivityIncident(handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateNetConnectionIncident(handle: POINTER(VoidPtr), id: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreatePnrpIncident(cloudname: win32more.Windows.Win32.Foundation.PWSTR, peername: win32more.Windows.Win32.Foundation.PWSTR, diagnosePublish: win32more.Windows.Win32.Foundation.BOOL, appId: win32more.Windows.Win32.Foundation.PWSTR, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateGroupingIncident(CloudName: win32more.Windows.Win32.Foundation.PWSTR, GroupName: win32more.Windows.Win32.Foundation.PWSTR, Identity: win32more.Windows.Win32.Foundation.PWSTR, Invitation: win32more.Windows.Win32.Foundation.PWSTR, Addresses: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKET_ADDRESS_LIST), appId: win32more.Windows.Win32.Foundation.PWSTR, handle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfExecuteDiagnosis(handle: VoidPtr, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCloseIncident(handle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfDiagnoseIncident(Handle: VoidPtr, RootCauseCount: POINTER(UInt32), RootCauses: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RootCauseInfo)), dwWait: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfRepairIncident(Handle: VoidPtr, RepairEx: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx), dwWait: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCancelIncident(Handle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfGetTraceFile(Handle: VoidPtr, TraceFileLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DIAGNOSIS_STATUS = Int32
DS_NOT_IMPLEMENTED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 0
DS_CONFIRMED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 1
DS_REJECTED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 2
DS_INDETERMINATE: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 3
DS_DEFERRED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 4
DS_PASSTHROUGH: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS = 5
class DIAG_SOCKADDR(Structure):
    family: UInt16
    data: win32more.Windows.Win32.Foundation.CHAR * 126
class DiagnosticsInfo(Structure):
    cost: Int32
    flags: UInt32
class HELPER_ATTRIBUTE(Structure):
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    type: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Boolean: win32more.Windows.Win32.Foundation.BOOL
        Char: Byte
        Byte: Byte
        Short: Int16
        Word: UInt16
        Int: Int32
        DWord: UInt32
        Int64: Int64
        UInt64: UInt64
        PWStr: win32more.Windows.Win32.Foundation.PWSTR
        Guid: Guid
        LifeTime: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME
        Address: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAG_SOCKADDR
        OctetString: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.OCTET_STRING
class HYPOTHESIS(Structure):
    pwszClassName: win32more.Windows.Win32.Foundation.PWSTR
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    celt: UInt32
    rgAttributes: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE)
class HelperAttributeInfo(Structure):
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    type: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
class HypothesisResult(Structure):
    hypothesis: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS
    pathStatus: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS
class INetDiagExtensibleHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0b35748-ebf5-11d8-bbe9-505054503030}')
    @commethod(3)
    def ResolveAttributes(self, celt: UInt32, rgKeyAttributes: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE), pcelt: POINTER(UInt32), prgMatchValues: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0b35746-ebf5-11d8-bbe9-505054503030}')
    @commethod(3)
    def Initialize(self, celt: UInt32, rgAttributes: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDiagnosticsInfo(self, ppInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DiagnosticsInfo))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyAttributes(self, pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LowHealth(self, pwszInstanceDescription: win32more.Windows.Win32.Foundation.PWSTR, ppwszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HighUtilization(self, pwszInstanceDescription: win32more.Windows.Win32.Foundation.PWSTR, ppwszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLowerHypotheses(self, pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDownStreamHypotheses(self, pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHigherHypotheses(self, pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUpStreamHypotheses(self, pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Repair(self, pInfo: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo), pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Validate(self, problem: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pDeferredTime: POINTER(Int32), pStatus: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRepairInfo(self, problem: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pcelt: POINTER(UInt32), ppInfo: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetLifeTime(self, pLifeTime: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetLifeTime(self, lifeTime: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCacheTime(self, pCacheTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAttributes(self, pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Cleanup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{972dab4d-e4e3-4fc6-ae54-5f65ccde4a15}')
    @commethod(3)
    def ReconfirmLowHealth(self, celt: UInt32, pResults: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HypothesisResult), ppwszUpdatedDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pUpdatedStatus: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUtilities(self, pUtilities: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperUtilFactory) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReproduceFailure(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0b35747-ebf5-11d8-bbe9-505054503030}')
    @commethod(3)
    def GetAttributeInfo(self, pcelt: POINTER(UInt32), pprgAttributeInfos: POINTER(POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HelperAttributeInfo))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperUtilFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{104613fb-bc57-4178-95ba-88809698354a}')
    @commethod(3)
    def CreateUtilityInstance(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class LIFE_TIME(Structure):
    startTime: win32more.Windows.Win32.Foundation.FILETIME
    endTime: win32more.Windows.Win32.Foundation.FILETIME
class OCTET_STRING(Structure):
    dwLength: UInt32
    lpValue: POINTER(Byte)
PROBLEM_TYPE = Int32
PT_INVALID: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 0
PT_LOW_HEALTH: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 1
PT_LOWER_HEALTH: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 2
PT_DOWN_STREAM_HEALTH: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 4
PT_HIGH_UTILIZATION: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 8
PT_HIGHER_UTILIZATION: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 16
PT_UP_STREAM_UTILIZATION: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE = 32
REPAIR_RISK = Int32
RR_NOROLLBACK: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK = 0
RR_ROLLBACK: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK = 1
RR_NORISK: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK = 2
REPAIR_SCOPE = Int32
RS_SYSTEM: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE = 0
RS_USER: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE = 1
RS_APPLICATION: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE = 2
RS_PROCESS: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE = 3
REPAIR_STATUS = Int32
RS_NOT_IMPLEMENTED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS = 0
RS_REPAIRED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS = 1
RS_UNREPAIRED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS = 2
RS_DEFERRED: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS = 3
RS_USER_ACTION: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS = 4
class RepairInfo(Structure):
    guid: Guid
    pwszClassName: win32more.Windows.Win32.Foundation.PWSTR
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    sidType: UInt32
    cost: Int32
    flags: UInt32
    scope: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE
    risk: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK
    UiInfo: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UiInfo
    rootCauseIndex: Int32
class RepairInfoEx(Structure):
    repair: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo
    repairRank: UInt16
class RootCauseInfo(Structure):
    pwszDescription: win32more.Windows.Win32.Foundation.PWSTR
    rootCauseID: Guid
    rootCauseFlags: UInt32
    networkInterfaceID: Guid
    pRepairs: POINTER(win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx)
    repairCount: UInt16
class ShellCommandInfo(Structure):
    pwszOperation: win32more.Windows.Win32.Foundation.PWSTR
    pwszFile: win32more.Windows.Win32.Foundation.PWSTR
    pwszParameters: win32more.Windows.Win32.Foundation.PWSTR
    pwszDirectory: win32more.Windows.Win32.Foundation.PWSTR
    nShowCmd: UInt32
UI_INFO_TYPE = Int32
UIT_INVALID: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE = 0
UIT_NONE: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE = 1
UIT_SHELL_COMMAND: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE = 2
UIT_HELP_PANE: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE = 3
UIT_DUI: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE = 4
class UiInfo(Structure):
    type: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pwzNull: win32more.Windows.Win32.Foundation.PWSTR
        ShellInfo: win32more.Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ShellCommandInfo
        pwzHelpUrl: win32more.Windows.Win32.Foundation.PWSTR
        pwzDui: win32more.Windows.Win32.Foundation.PWSTR


make_ready(__name__)
