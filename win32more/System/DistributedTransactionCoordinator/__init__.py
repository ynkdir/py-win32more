from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.DistributedTransactionCoordinator
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
DTCINSTALL_E_CLIENT_ALREADY_INSTALLED: Int32 = 384
DTCINSTALL_E_SERVER_ALREADY_INSTALLED: Int32 = 385
XA_SWITCH_F_DTC: UInt32 = 1
XA_FMTID_DTC: UInt32 = 4478019
XA_FMTID_DTC_VER1: UInt32 = 21255235
XIDDATASIZE: UInt32 = 128
MAXGTRIDSIZE: UInt32 = 64
MAXBQUALSIZE: UInt32 = 64
RMNAMESZ: UInt32 = 32
MAXINFOSIZE: UInt32 = 256
TMNOFLAGS: Int32 = 0
TMREGISTER: Int32 = 1
TMNOMIGRATE: Int32 = 2
TMUSEASYNC: Int32 = 4
TMASYNC: Int32 = -2147483648
TMONEPHASE: Int32 = 1073741824
TMFAIL: Int32 = 536870912
TMNOWAIT: Int32 = 268435456
TMRESUME: Int32 = 134217728
TMSUCCESS: Int32 = 67108864
TMSUSPEND: Int32 = 33554432
TMSTARTRSCAN: Int32 = 16777216
TMENDRSCAN: Int32 = 8388608
TMMULTIPLE: Int32 = 4194304
TMJOIN: Int32 = 2097152
TMMIGRATE: Int32 = 1048576
TM_JOIN: UInt32 = 2
TM_RESUME: UInt32 = 1
TM_OK: UInt32 = 0
TMER_TMERR: Int32 = -1
TMER_INVAL: Int32 = -2
TMER_PROTO: Int32 = -3
XA_RBBASE: UInt32 = 100
XA_RBROLLBACK: UInt32 = 100
XA_RBCOMMFAIL: UInt32 = 101
XA_RBDEADLOCK: UInt32 = 102
XA_RBINTEGRITY: UInt32 = 103
XA_RBOTHER: UInt32 = 104
XA_RBPROTO: UInt32 = 105
XA_RBTIMEOUT: UInt32 = 106
XA_RBTRANSIENT: UInt32 = 107
XA_RBEND: UInt32 = 107
XA_NOMIGRATE: UInt32 = 9
XA_HEURHAZ: UInt32 = 8
XA_HEURCOM: UInt32 = 7
XA_HEURRB: UInt32 = 6
XA_HEURMIX: UInt32 = 5
XA_RETRY: UInt32 = 4
XA_RDONLY: UInt32 = 3
XA_OK: UInt32 = 0
XAER_ASYNC: Int32 = -2
XAER_RMERR: Int32 = -3
XAER_NOTA: Int32 = -4
XAER_INVAL: Int32 = -5
XAER_PROTO: Int32 = -6
XAER_RMFAIL: Int32 = -7
XAER_DUPID: Int32 = -8
XAER_OUTSIDE: Int32 = -9
DTC_INSTALL_OVERWRITE_CLIENT: UInt32 = 1
DTC_INSTALL_OVERWRITE_SERVER: UInt32 = 2
OLE_TM_CONFIG_VERSION_1: UInt32 = 1
OLE_TM_CONFIG_VERSION_2: UInt32 = 2
OLE_TM_FLAG_NONE: UInt32 = 0
OLE_TM_FLAG_NODEMANDSTART: UInt32 = 1
OLE_TM_FLAG_NOAGILERECOVERY: UInt32 = 2
OLE_TM_FLAG_QUERY_SERVICE_LOCKSTATUS: UInt32 = 2147483648
OLE_TM_FLAG_INTERNAL_TO_TM: UInt32 = 1073741824
CLSID_MSDtcTransactionManager: Guid = Guid('5b18ab61-091d-11d1-97-df-00-c0-4f-b9-61-8a')
CLSID_MSDtcTransaction: Guid = Guid('39f8d76b-0928-11d1-97-df-00-c0-4f-b9-61-8a')
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManager(i_pszHost: win32more.Foundation.PSTR, i_pszTmName: win32more.Foundation.PSTR, i_riid: POINTER(Guid), i_dwReserved1: UInt32, i_wcbReserved2: UInt16, i_pvReserved2: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerC(i_pszHost: win32more.Foundation.PSTR, i_pszTmName: win32more.Foundation.PSTR, i_riid: POINTER(Guid), i_dwReserved1: UInt32, i_wcbReserved2: UInt16, i_pvReserved2: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerExA(i_pszHost: win32more.Foundation.PSTR, i_pszTmName: win32more.Foundation.PSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerExW(i_pwszHost: win32more.Foundation.PWSTR, i_pwszTmName: win32more.Foundation.PWSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
APPLICATIONTYPE = Int32
LOCAL_APPLICATIONTYPE: APPLICATIONTYPE = 0
CLUSTERRESOURCE_APPLICATIONTYPE: APPLICATIONTYPE = 1
AUTHENTICATION_LEVEL = Int32
NO_AUTHENTICATION_REQUIRED: AUTHENTICATION_LEVEL = 0
INCOMING_AUTHENTICATION_REQUIRED: AUTHENTICATION_LEVEL = 1
MUTUAL_AUTHENTICATION_REQUIRED: AUTHENTICATION_LEVEL = 2
class BOID(Structure):
    rgb: Byte * 16
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER(pszHost: win32more.Foundation.PSTR, pszTmName: win32more.Foundation.PSTR, rid: POINTER(Guid), dwReserved1: UInt32, wcbReserved2: UInt16, pvReserved2: c_void_p, ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER_EX_A(i_pszHost: win32more.Foundation.PSTR, i_pszTmName: win32more.Foundation.PSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER_EX_W(i_pwszHost: win32more.Foundation.PWSTR, i_pwszTmName: win32more.Foundation.PWSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: c_void_p, o_ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def DTC_INSTALL_CLIENT(i_pszRemoteTmHostName: POINTER(SByte), i_dwProtocol: UInt32, i_dwOverwrite: UInt32) -> win32more.Foundation.HRESULT: ...
DTC_STATUS_ = Int32
DTC_STATUS_UNKNOWN: DTC_STATUS_ = 0
DTC_STATUS_STARTING: DTC_STATUS_ = 1
DTC_STATUS_STARTED: DTC_STATUS_ = 2
DTC_STATUS_PAUSING: DTC_STATUS_ = 3
DTC_STATUS_PAUSED: DTC_STATUS_ = 4
DTC_STATUS_CONTINUING: DTC_STATUS_ = 5
DTC_STATUS_STOPPING: DTC_STATUS_ = 6
DTC_STATUS_STOPPED: DTC_STATUS_ = 7
DTC_STATUS_E_CANTCONTROL: DTC_STATUS_ = 8
DTC_STATUS_FAILED: DTC_STATUS_ = 9
DTCINITIATEDRECOVERYWORK = Int32
DTCINITIATEDRECOVERYWORK_CHECKLUSTATUS: DTCINITIATEDRECOVERYWORK = 1
DTCINITIATEDRECOVERYWORK_TRANS: DTCINITIATEDRECOVERYWORK = 2
DTCINITIATEDRECOVERYWORK_TMDOWN: DTCINITIATEDRECOVERYWORK = 3
DTCLUCOMPARESTATE = Int32
DTCLUCOMPARESTATE_COMMITTED: DTCLUCOMPARESTATE = 1
DTCLUCOMPARESTATE_HEURISTICCOMMITTED: DTCLUCOMPARESTATE = 2
DTCLUCOMPARESTATE_HEURISTICMIXED: DTCLUCOMPARESTATE = 3
DTCLUCOMPARESTATE_HEURISTICRESET: DTCLUCOMPARESTATE = 4
DTCLUCOMPARESTATE_INDOUBT: DTCLUCOMPARESTATE = 5
DTCLUCOMPARESTATE_RESET: DTCLUCOMPARESTATE = 6
DTCLUCOMPARESTATESCONFIRMATION = Int32
DTCLUCOMPARESTATESCONFIRMATION_CONFIRM: DTCLUCOMPARESTATESCONFIRMATION = 1
DTCLUCOMPARESTATESCONFIRMATION_PROTOCOL: DTCLUCOMPARESTATESCONFIRMATION = 2
DTCLUCOMPARESTATESERROR = Int32
DTCLUCOMPARESTATESERROR_PROTOCOL: DTCLUCOMPARESTATESERROR = 1
DTCLUCOMPARESTATESRESPONSE = Int32
DTCLUCOMPARESTATESRESPONSE_OK: DTCLUCOMPARESTATESRESPONSE = 1
DTCLUCOMPARESTATESRESPONSE_PROTOCOL: DTCLUCOMPARESTATESRESPONSE = 2
DTCLUXLN = Int32
DTCLUXLN_COLD: DTCLUXLN = 1
DTCLUXLN_WARM: DTCLUXLN = 2
DTCLUXLNCONFIRMATION = Int32
DTCLUXLNCONFIRMATION_CONFIRM: DTCLUXLNCONFIRMATION = 1
DTCLUXLNCONFIRMATION_LOGNAMEMISMATCH: DTCLUXLNCONFIRMATION = 2
DTCLUXLNCONFIRMATION_COLDWARMMISMATCH: DTCLUXLNCONFIRMATION = 3
DTCLUXLNCONFIRMATION_OBSOLETE: DTCLUXLNCONFIRMATION = 4
DTCLUXLNERROR = Int32
DTCLUXLNERROR_PROTOCOL: DTCLUXLNERROR = 1
DTCLUXLNERROR_LOGNAMEMISMATCH: DTCLUXLNERROR = 2
DTCLUXLNERROR_COLDWARMMISMATCH: DTCLUXLNERROR = 3
DTCLUXLNRESPONSE = Int32
DTCLUXLNRESPONSE_OK_SENDOURXLNBACK: DTCLUXLNRESPONSE = 1
DTCLUXLNRESPONSE_OK_SENDCONFIRMATION: DTCLUXLNRESPONSE = 2
DTCLUXLNRESPONSE_LOGNAMEMISMATCH: DTCLUXLNRESPONSE = 3
DTCLUXLNRESPONSE_COLDWARMMISMATCH: DTCLUXLNRESPONSE = 4
class IDtcLuConfigure(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e760-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Add(pucLuPair: c_char_p_no, cbLuPair: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(pucLuPair: c_char_p_no, cbLuPair: UInt32) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecovery(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ac2b8ad2-d6f0-11d0-b3-86-00-a0-c9-08-33-65')
class IDtcLuRecoveryFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e762-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Create(pucLuPair: c_char_p_no, cbLuPair: UInt32, ppRecovery: POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRecovery_head)) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtc(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e764-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def GetWork(pWork: POINTER(win32more.System.DistributedTransactionCoordinator.DTCINITIATEDRECOVERYWORK), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtcStatusWork(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e766-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def HandleCheckLuStatus(lRecoverySeqNum: Int32) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtcTransWork(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e765-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def GetLogNameSizes(pcbOurLogName: POINTER(UInt32), pcbRemoteLogName: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOurXln(pXln: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUXLN), pOurLogName: c_char_p_no, pRemoteLogName: c_char_p_no, pdwProtocol: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HandleConfirmationFromOurXln(Confirmation: win32more.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HandleTheirXlnResponse(Xln: win32more.System.DistributedTransactionCoordinator.DTCLUXLN, pRemoteLogName: c_char_p_no, cbRemoteLogName: UInt32, dwProtocol: UInt32, pConfirmation: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def HandleErrorFromOurXln(Error: win32more.System.DistributedTransactionCoordinator.DTCLUXLNERROR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CheckForCompareStates(fCompareStates: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetOurTransIdSize(pcbOurTransId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetOurCompareStates(pOurTransId: c_char_p_no, pCompareState: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def HandleTheirCompareStatesResponse(CompareState: win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE, pConfirmation: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def HandleErrorFromOurCompareStates(Error: win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESERROR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ConversationLost() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecoverySeqNum(plRecoverySeqNum: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ObsoleteRecoverySeqNum(lNewRecoverySeqNum: Int32) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByLu(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e768-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def GetObjectToHandleWorkFromLu(ppWork: POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByLuWork_head)) -> win32more.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByLuWork(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ac2b8ad1-d6f0-11d0-b3-86-00-a0-c9-08-33-65')
    @commethod(3)
    def HandleTheirXln(lRecoverySeqNum: Int32, Xln: win32more.System.DistributedTransactionCoordinator.DTCLUXLN, pRemoteLogName: c_char_p_no, cbRemoteLogName: UInt32, pOurLogName: c_char_p_no, cbOurLogName: UInt32, dwProtocol: UInt32, pResponse: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOurLogNameSize(pcbOurLogName: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetOurXln(pXln: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUXLN), pOurLogName: c_char_p_no, pdwProtocol: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HandleConfirmationOfOurXln(Confirmation: win32more.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def HandleTheirCompareStates(pRemoteTransId: c_char_p_no, cbRemoteTransId: UInt32, CompareState: win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE, pResponse: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESRESPONSE), pCompareState: POINTER(win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def HandleConfirmationOfOurCompareStates(Confirmation: win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def HandleErrorFromOurCompareStates(Error: win32more.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESERROR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ConversationLost() -> win32more.Foundation.HRESULT: ...
class IDtcLuRmEnlistment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e769-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Unplug(fConversationLost: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BackedOut() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BackOut() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Committed() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Forget() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RequestCommit() -> win32more.Foundation.HRESULT: ...
class IDtcLuRmEnlistmentFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e771-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Create(pucLuPair: c_char_p_no, cbLuPair: UInt32, pITransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, pTransId: c_char_p_no, cbTransId: UInt32, pRmEnlistmentSink: win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistmentSink_head, ppRmEnlistment: POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistment_head)) -> win32more.Foundation.HRESULT: ...
class IDtcLuRmEnlistmentSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e770-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def AckUnplug() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TmDown() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SessionLost() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def BackedOut() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BackOut() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Committed() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Forget() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Prepare() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RequestCommit() -> win32more.Foundation.HRESULT: ...
class IDtcLuSubordinateDtc(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e773-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Unplug(fConversationLost: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BackedOut() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BackOut() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Committed() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Forget() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Prepare() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RequestCommit() -> win32more.Foundation.HRESULT: ...
class IDtcLuSubordinateDtcFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e775-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def Create(pucLuPair: c_char_p_no, cbLuPair: UInt32, punkTransactionOuter: win32more.System.Com.IUnknown_head, isoLevel: Int32, isoFlags: UInt32, pOptions: win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head, ppTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), pTransId: c_char_p_no, cbTransId: UInt32, pSubordinateDtcSink: win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtcSink_head, ppSubordinateDtc: POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtc_head)) -> win32more.Foundation.HRESULT: ...
class IDtcLuSubordinateDtcSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4131e774-1aea-11d0-94-4b-00-a0-c9-05-41-6e')
    @commethod(3)
    def AckUnplug() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TmDown() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SessionLost() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def BackedOut() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BackOut() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Committed() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Forget() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RequestCommit() -> win32more.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9797c15d-a428-4291-87-b6-09-95-03-1a-67-8d')
    @commethod(3)
    def GetAnyNetworkAccess(pbAnyNetworkAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetAnyNetworkAccess(bAnyNetworkAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkAdministrationAccess(pbNetworkAdministrationAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetNetworkAdministrationAccess(bNetworkAdministrationAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetNetworkTransactionAccess(pbNetworkTransactionAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetNetworkTransactionAccess(bNetworkTransactionAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkClientAccess(pbNetworkClientAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetNetworkClientAccess(bNetworkClientAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkTIPAccess(pbNetworkTIPAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetNetworkTIPAccess(bNetworkTIPAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetXAAccess(pbXAAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetXAAccess(bXAAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RestartDtcService() -> win32more.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig2(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig
    Guid = Guid('a7aa013b-eb7d-4f42-b4-1c-b2-de-c0-9a-e0-34')
    @commethod(16)
    def GetNetworkInboundAccess(pbInbound: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetNetworkOutboundAccess(pbOutbound: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetNetworkInboundAccess(bInbound: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetNetworkOutboundAccess(bOutbound: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetAuthenticationLevel(pAuthLevel: POINTER(win32more.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetAuthenticationLevel(AuthLevel: win32more.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL) -> win32more.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig3(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig2
    Guid = Guid('76e4b4f3-2ca5-466b-89-d5-fd-21-8e-e7-5b-49')
    @commethod(22)
    def GetLUAccess(pbLUAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetLUAccess(bLUAccess: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IDtcToXaHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9861611-304a-11d1-98-13-00-a0-c9-05-41-6e')
    @commethod(3)
    def Close(i_fDoRecovery: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateTridToXid(pITransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, pguidBqual: POINTER(Guid), pXid: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head)) -> win32more.Foundation.HRESULT: ...
class IDtcToXaHelperFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9861610-304a-11d1-98-13-00-a0-c9-05-41-6e')
    @commethod(3)
    def Create(pszDSN: win32more.Foundation.PSTR, pszClientDllName: win32more.Foundation.PSTR, pguidRm: POINTER(Guid), ppXaHelper: POINTER(win32more.System.DistributedTransactionCoordinator.IDtcToXaHelper_head)) -> win32more.Foundation.HRESULT: ...
class IDtcToXaHelperSinglePipe(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('47ed4971-53b3-11d1-bb-b9-00-c0-4f-d6-58-f6')
    @commethod(3)
    def XARMCreate(pszDSN: win32more.Foundation.PSTR, pszClientDll: win32more.Foundation.PSTR, pdwRMCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertTridToXID(pdwITrans: POINTER(UInt32), dwRMCookie: UInt32, pxid: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistWithRM(dwRMCookie: UInt32, i_pITransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, i_pITransRes: win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head, o_ppITransEnslitment: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseRMCookie(i_dwRMCookie: UInt32, i_fNormal: win32more.Foundation.BOOL) -> Void: ...
class IDtcToXaMapper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('64ffabe0-7ce9-11d0-8c-e6-00-c0-4f-dc-87-7e')
    @commethod(3)
    def RequestNewResourceManager(pszDSN: win32more.Foundation.PSTR, pszClientDllName: win32more.Foundation.PSTR, pdwRMCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateTridToXid(pdwITransaction: POINTER(UInt32), dwRMCookie: UInt32, pXid: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistResourceManager(dwRMCookie: UInt32, pdwITransaction: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseResourceManager(dwRMCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class IGetDispenser(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c23cc370-87ef-11ce-80-81-00-80-c7-58-52-7e')
    @commethod(3)
    def GetDispenser(iid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IKernelTransaction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79427a2b-f895-40e0-be-79-b5-7d-c8-2e-d2-31')
    @commethod(3)
    def GetHandle(pHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
class ILastResourceManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4d964ad4-5b33-11d3-8a-91-00-c0-4f-79-eb-6d')
    @commethod(3)
    def TransactionCommitted(pPrepInfo: c_char_p_no, cbPrepInfo: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RecoveryDone() -> win32more.Foundation.HRESULT: ...
class IPrepareInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('80c7bfd0-87ee-11ce-80-81-00-80-c7-58-52-7e')
    @commethod(3)
    def GetPrepareInfoSize(pcbPrepInfo: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrepareInfo(pPrepInfo: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IPrepareInfo2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5fab2547-9779-11d1-b8-86-00-c0-4f-b9-61-8a')
    @commethod(3)
    def GetPrepareInfoSize(pcbPrepInfo: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrepareInfo(cbPrepareInfo: UInt32, pPrepInfo: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IResourceManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('13741d21-87eb-11ce-80-81-00-80-c7-58-52-7e')
    @commethod(3)
    def Enlist(pTransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, pRes: win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head, pUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), pisoLevel: POINTER(Int32), ppEnlist: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Reenlist(pPrepInfo: c_char_p_no, cbPrepInfo: UInt32, lTimeout: UInt32, pXactStat: POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReenlistmentComplete() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDistributedTransactionManager(iid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IResourceManager2(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.IResourceManager
    Guid = Guid('d136c69a-f749-11d1-8f-47-00-c0-4f-8e-e5-7d')
    @commethod(7)
    def Enlist2(pTransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, pResAsync: win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head, pUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), pisoLevel: POINTER(Int32), pXid: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), ppEnlist: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Reenlist2(pXid: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), dwTimeout: UInt32, pXactStat: POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Foundation.HRESULT: ...
class IResourceManagerFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('13741d20-87eb-11ce-80-81-00-80-c7-58-52-7e')
    @commethod(3)
    def Create(pguidRM: POINTER(Guid), pszRMName: win32more.Foundation.PSTR, pIResMgrSink: win32more.System.DistributedTransactionCoordinator.IResourceManagerSink_head, ppResMgr: POINTER(win32more.System.DistributedTransactionCoordinator.IResourceManager_head)) -> win32more.Foundation.HRESULT: ...
class IResourceManagerFactory2(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.IResourceManagerFactory
    Guid = Guid('6b369c21-fbd2-11d1-8f-47-00-c0-4f-8e-e5-7d')
    @commethod(4)
    def CreateEx(pguidRM: POINTER(Guid), pszRMName: win32more.Foundation.PSTR, pIResMgrSink: win32more.System.DistributedTransactionCoordinator.IResourceManagerSink_head, riidRequested: POINTER(Guid), ppvResMgr: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IResourceManagerRejoinable(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.IResourceManager2
    Guid = Guid('6f6de620-b5df-4f3e-9c-fa-c8-ae-bd-05-17-2b')
    @commethod(9)
    def Rejoin(pPrepInfo: c_char_p_no, cbPrepInfo: UInt32, lTimeout: UInt32, pXactStat: POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Foundation.HRESULT: ...
class IResourceManagerSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0d563181-defb-11ce-ae-d1-00-aa-00-51-e2-c4')
    @commethod(3)
    def TMDown() -> win32more.Foundation.HRESULT: ...
class IRMHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e793f6d1-f53d-11cf-a6-0d-00-a0-c9-05-41-6e')
    @commethod(3)
    def RMCount(dwcTotalNumberOfRMs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RMInfo(pXa_Switch: POINTER(win32more.System.DistributedTransactionCoordinator.xa_switch_t_head), fCDeclCallingConv: win32more.Foundation.BOOL, pszOpenString: win32more.Foundation.PSTR, pszCloseString: win32more.Foundation.PSTR, guidRMRecovery: Guid) -> win32more.Foundation.HRESULT: ...
ISOFLAG = Int32
ISOFLAG_RETAIN_COMMIT_DC: ISOFLAG = 1
ISOFLAG_RETAIN_COMMIT: ISOFLAG = 2
ISOFLAG_RETAIN_COMMIT_NO: ISOFLAG = 3
ISOFLAG_RETAIN_ABORT_DC: ISOFLAG = 4
ISOFLAG_RETAIN_ABORT: ISOFLAG = 8
ISOFLAG_RETAIN_ABORT_NO: ISOFLAG = 12
ISOFLAG_RETAIN_DONTCARE: ISOFLAG = 5
ISOFLAG_RETAIN_BOTH: ISOFLAG = 10
ISOFLAG_RETAIN_NONE: ISOFLAG = 15
ISOFLAG_OPTIMISTIC: ISOFLAG = 16
ISOFLAG_READONLY: ISOFLAG = 32
ISOLATIONLEVEL = Int32
ISOLATIONLEVEL_UNSPECIFIED: ISOLATIONLEVEL = -1
ISOLATIONLEVEL_CHAOS: ISOLATIONLEVEL = 16
ISOLATIONLEVEL_READUNCOMMITTED: ISOLATIONLEVEL = 256
ISOLATIONLEVEL_BROWSE: ISOLATIONLEVEL = 256
ISOLATIONLEVEL_CURSORSTABILITY: ISOLATIONLEVEL = 4096
ISOLATIONLEVEL_READCOMMITTED: ISOLATIONLEVEL = 4096
ISOLATIONLEVEL_REPEATABLEREAD: ISOLATIONLEVEL = 65536
ISOLATIONLEVEL_SERIALIZABLE: ISOLATIONLEVEL = 1048576
ISOLATIONLEVEL_ISOLATED: ISOLATIONLEVEL = 1048576
class ITipHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('17cf72d1-bac5-11d1-b1-bf-00-c0-4f-c2-f3-ef')
    @commethod(3)
    def Pull(i_pszTxUrl: c_char_p_no, o_ppITransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PullAsync(i_pszTxUrl: c_char_p_no, i_pTipPullSink: win32more.System.DistributedTransactionCoordinator.ITipPullSink_head, o_ppITransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocalTmUrl(o_ppszLocalTmUrl: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class ITipPullSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('17cf72d2-bac5-11d1-b1-bf-00-c0-4f-c2-f3-ef')
    @commethod(3)
    def PullComplete(i_hrPull: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class ITipTransaction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('17cf72d0-bac5-11d1-b1-bf-00-c0-4f-c2-f3-ef')
    @commethod(3)
    def Push(i_pszRemoteTmUrl: c_char_p_no, o_ppszRemoteTxUrl: POINTER(win32more.Foundation.PSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionUrl(o_ppszLocalTxUrl: POINTER(win32more.Foundation.PSTR)) -> win32more.Foundation.HRESULT: ...
class ITmNodeName(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('30274f88-6ee4-474e-9b-95-78-07-bc-9e-f8-cf')
    @commethod(3)
    def GetNodeNameSize(pcbNodeNameSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNodeName(cbNodeNameBufferSize: UInt32, pNodeNameBuffer: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class ITransaction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0fb15084-af41-11ce-bd-2b-20-4c-4f-4f-50-20')
    @commethod(3)
    def Commit(fRetaining: win32more.Foundation.BOOL, grfTC: UInt32, grfRM: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), fRetaining: win32more.Foundation.BOOL, fAsync: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransactionInfo(pinfo: POINTER(win32more.System.DistributedTransactionCoordinator.XACTTRANSINFO_head)) -> win32more.Foundation.HRESULT: ...
class ITransaction2(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.ITransactionCloner
    Guid = Guid('34021548-0065-11d3-ba-c1-00-c0-4f-79-7b-e2')
    @commethod(7)
    def GetTransactionInfo2(pinfo: POINTER(win32more.System.DistributedTransactionCoordinator.XACTTRANSINFO_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionCloner(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.ITransaction
    Guid = Guid('02656950-2152-11d0-94-4c-00-a0-c9-05-41-6e')
    @commethod(6)
    def CloneWithCommitDisabled(ppITransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionDispenser(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3a6ad9e1-23b9-11cf-ad-60-00-aa-00-a7-4c-cd')
    @commethod(3)
    def GetOptionsObject(ppOptions: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BeginTransaction(punkOuter: win32more.System.Com.IUnknown_head, isoLevel: Int32, isoFlags: UInt32, pOptions: win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head, ppTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionEnlistmentAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0fb15081-af41-11ce-bd-2b-20-4c-4f-4f-50-20')
    @commethod(3)
    def PrepareRequestDone(hr: win32more.Foundation.HRESULT, pmk: win32more.System.Com.IMoniker_head, pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequestDone(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequestDone(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class ITransactionExport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0141fda5-8fc0-11ce-bd-18-20-4c-4f-4f-50-20')
    @commethod(3)
    def Export(punkTransaction: win32more.System.Com.IUnknown_head, pcbTransactionCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionCookie(punkTransaction: win32more.System.Com.IUnknown_head, cbTransactionCookie: UInt32, rgbTransactionCookie: c_char_p_no, pcbUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITransactionExportFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e1cf9b53-8745-11ce-a9-ba-00-aa-00-6c-37-06')
    @commethod(3)
    def GetRemoteClassId(pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Create(cbWhereabouts: UInt32, rgbWhereabouts: c_char_p_no, ppExport: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionExport_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionImport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e1cf9b5a-8745-11ce-a9-ba-00-aa-00-6c-37-06')
    @commethod(3)
    def Import(cbTransactionCookie: UInt32, rgbTransactionCookie: c_char_p_no, piid: POINTER(Guid), ppvTransaction: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ITransactionImportWhereabouts(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0141fda4-8fc0-11ce-bd-18-20-4c-4f-4f-50-20')
    @commethod(3)
    def GetWhereaboutsSize(pcbWhereabouts: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetWhereabouts(cbWhereabouts: UInt32, rgbWhereabouts: c_char_p_no, pcbUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITransactionLastEnlistmentAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c82bd533-5b30-11d3-8a-91-00-c0-4f-79-eb-6d')
    @commethod(3)
    def TransactionOutcome(XactStat: win32more.System.DistributedTransactionCoordinator.XACTSTAT, pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionLastResourceAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c82bd532-5b30-11d3-8a-91-00-c0-4f-79-eb-6d')
    @commethod(3)
    def DelegateCommit(grfRM: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ForgetRequest(pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3a6ad9e0-23b9-11cf-ad-60-00-aa-00-a7-4c-cd')
    @commethod(3)
    def SetOptions(pOptions: POINTER(win32more.System.DistributedTransactionCoordinator.XACTOPT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptions(pOptions: POINTER(win32more.System.DistributedTransactionCoordinator.XACTOPT_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionOutcomeEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3a6ad9e2-23b9-11cf-ad-60-00-aa-00-a7-4c-cd')
    @commethod(3)
    def Committed(fRetaining: win32more.Foundation.BOOL, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Aborted(pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), fRetaining: win32more.Foundation.BOOL, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HeuristicDecision(dwDecision: UInt32, pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Indoubt() -> win32more.Foundation.HRESULT: ...
class ITransactionPhase0EnlistmentAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('82dc88e1-a954-11d1-8f-88-00-60-08-95-e7-d5')
    @commethod(3)
    def Enable() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForEnlistment() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Phase0Done() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Unenlist() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransaction(ppITransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionPhase0Factory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('82dc88e0-a954-11d1-8f-88-00-60-08-95-e7-d5')
    @commethod(3)
    def Create(pPhase0Notify: win32more.System.DistributedTransactionCoordinator.ITransactionPhase0NotifyAsync_head, ppPhase0Enlistment: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionPhase0EnlistmentAsync_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionPhase0NotifyAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ef081809-0c76-11d2-87-a6-00-c0-4f-99-0f-34')
    @commethod(3)
    def Phase0Request(fAbortingHint: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnlistCompleted(status: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class ITransactionReceiver(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('59313e03-b36c-11cf-a5-39-00-aa-00-68-87-c3')
    @commethod(3)
    def UnmarshalPropagationToken(cbToken: UInt32, rgbToken: c_char_p_no, ppTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetReturnTokenSize(pcbReturnToken: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MarshalReturnToken(cbReturnToken: UInt32, rgbReturnToken: c_char_p_no, pcbUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ITransactionReceiverFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('59313e02-b36c-11cf-a5-39-00-aa-00-68-87-c3')
    @commethod(3)
    def Create(ppReceiver: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionReceiver_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionResource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ee5ff7b3-4572-11d0-94-52-00-a0-c9-05-41-6e')
    @commethod(3)
    def PrepareRequest(fRetaining: win32more.Foundation.BOOL, grfRM: UInt32, fWantMoniker: win32more.Foundation.BOOL, fSinglePhase: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequest(grfRM: UInt32, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequest(pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), fRetaining: win32more.Foundation.BOOL, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TMDown() -> win32more.Foundation.HRESULT: ...
class ITransactionResourceAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('69e971f0-23ce-11cf-ad-60-00-aa-00-a7-4c-cd')
    @commethod(3)
    def PrepareRequest(fRetaining: win32more.Foundation.BOOL, grfRM: UInt32, fWantMoniker: win32more.Foundation.BOOL, fSinglePhase: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequest(grfRM: UInt32, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequest(pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), fRetaining: win32more.Foundation.BOOL, pNewUOW: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TMDown() -> win32more.Foundation.HRESULT: ...
class ITransactionTransmitter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('59313e01-b36c-11cf-a5-39-00-aa-00-68-87-c3')
    @commethod(3)
    def Set(pTransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropagationTokenSize(pcbToken: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MarshalPropagationToken(cbToken: UInt32, rgbToken: c_char_p_no, pcbUsed: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def UnmarshalReturnToken(cbReturnToken: UInt32, rgbReturnToken: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ITransactionTransmitterFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('59313e00-b36c-11cf-a5-39-00-aa-00-68-87-c3')
    @commethod(3)
    def Create(ppTransmitter: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionTransmitter_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionVoterBallotAsync2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5433376c-414d-11d3-b2-06-00-c0-4f-c2-f3-ef')
    @commethod(3)
    def VoteRequestDone(hr: win32more.Foundation.HRESULT, pboidReason: POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionVoterFactory2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5433376a-414d-11d3-b2-06-00-c0-4f-c2-f3-ef')
    @commethod(3)
    def Create(pTransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, pVoterNotify: win32more.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head, ppVoterBallot: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionVoterNotifyAsync2(c_void_p):
    extends: win32more.System.DistributedTransactionCoordinator.ITransactionOutcomeEvents
    Guid = Guid('5433376b-414d-11d3-b2-06-00-c0-4f-c2-f3-ef')
    @commethod(7)
    def VoteRequest() -> win32more.Foundation.HRESULT: ...
class IXAConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c8a6e3a1-9a8c-11cf-a3-08-00-a0-c9-05-41-6e')
    @commethod(3)
    def Initialize(clsidHelperDll: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate() -> win32more.Foundation.HRESULT: ...
class IXAObtainRMInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e793f6d2-f53d-11cf-a6-0d-00-a0-c9-05-41-6e')
    @commethod(3)
    def ObtainRMInfo(pIRMHelper: win32more.System.DistributedTransactionCoordinator.IRMHelper_head) -> win32more.Foundation.HRESULT: ...
class IXATransLookup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f3b1f131-eeda-11ce-ae-d4-00-aa-00-51-e2-c4')
    @commethod(3)
    def Lookup(ppTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
class IXATransLookup2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bf193c85-0d1a-4290-b8-8f-d2-cb-88-73-d1-e7')
    @commethod(3)
    def Lookup(pXID: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), ppTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
class OLE_TM_CONFIG_PARAMS_V1(Structure):
    dwVersion: UInt32
    dwcConcurrencyHint: UInt32
class OLE_TM_CONFIG_PARAMS_V2(Structure):
    dwVersion: UInt32
    dwcConcurrencyHint: UInt32
    applicationType: win32more.System.DistributedTransactionCoordinator.APPLICATIONTYPE
    clusterResourceId: Guid
class PROXY_CONFIG_PARAMS(Structure):
    wcThreadsMax: UInt16
TX_MISC_CONSTANTS = Int32
MAX_TRAN_DESC: TX_MISC_CONSTANTS = 40
@cfunctype_pointer
def XA_CLOSE_EPT(param0: win32more.Foundation.PSTR, param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_COMMIT_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_COMPLETE_EPT(param0: POINTER(Int32), param1: POINTER(Int32), param2: Int32, param3: Int32) -> Int32: ...
@cfunctype_pointer
def XA_END_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_FORGET_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_OPEN_EPT(param0: win32more.Foundation.PSTR, param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_PREPARE_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_RECOVER_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32, param3: Int32) -> Int32: ...
@cfunctype_pointer
def XA_ROLLBACK_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_START_EPT(param0: POINTER(win32more.System.DistributedTransactionCoordinator.XID_head), param1: Int32, param2: Int32) -> Int32: ...
class xa_switch_t(Structure):
    name: win32more.Foundation.CHAR * 32
    flags: Int32
    version: Int32
    xa_open_entry: IntPtr
    xa_close_entry: IntPtr
    xa_start_entry: IntPtr
    xa_end_entry: IntPtr
    xa_rollback_entry: IntPtr
    xa_prepare_entry: IntPtr
    xa_commit_entry: IntPtr
    xa_recover_entry: IntPtr
    xa_forget_entry: IntPtr
    xa_complete_entry: IntPtr
XACT_DTC_CONSTANTS = Int32
XACT_E_CONNECTION_REQUEST_DENIED: XACT_DTC_CONSTANTS = -2147168000
XACT_E_TOOMANY_ENLISTMENTS: XACT_DTC_CONSTANTS = -2147167999
XACT_E_DUPLICATE_GUID: XACT_DTC_CONSTANTS = -2147167998
XACT_E_NOTSINGLEPHASE: XACT_DTC_CONSTANTS = -2147167997
XACT_E_RECOVERYALREADYDONE: XACT_DTC_CONSTANTS = -2147167996
XACT_E_PROTOCOL: XACT_DTC_CONSTANTS = -2147167995
XACT_E_RM_FAILURE: XACT_DTC_CONSTANTS = -2147167994
XACT_E_RECOVERY_FAILED: XACT_DTC_CONSTANTS = -2147167993
XACT_E_LU_NOT_FOUND: XACT_DTC_CONSTANTS = -2147167992
XACT_E_DUPLICATE_LU: XACT_DTC_CONSTANTS = -2147167991
XACT_E_LU_NOT_CONNECTED: XACT_DTC_CONSTANTS = -2147167990
XACT_E_DUPLICATE_TRANSID: XACT_DTC_CONSTANTS = -2147167989
XACT_E_LU_BUSY: XACT_DTC_CONSTANTS = -2147167988
XACT_E_LU_NO_RECOVERY_PROCESS: XACT_DTC_CONSTANTS = -2147167987
XACT_E_LU_DOWN: XACT_DTC_CONSTANTS = -2147167986
XACT_E_LU_RECOVERING: XACT_DTC_CONSTANTS = -2147167985
XACT_E_LU_RECOVERY_MISMATCH: XACT_DTC_CONSTANTS = -2147167984
XACT_E_RM_UNAVAILABLE: XACT_DTC_CONSTANTS = -2147167983
XACT_E_LRMRECOVERYALREADYDONE: XACT_DTC_CONSTANTS = -2147167982
XACT_E_NOLASTRESOURCEINTERFACE: XACT_DTC_CONSTANTS = -2147167981
XACT_S_NONOTIFY: XACT_DTC_CONSTANTS = 315648
XACT_OK_NONOTIFY: XACT_DTC_CONSTANTS = 315649
dwUSER_MS_SQLSERVER: XACT_DTC_CONSTANTS = 65535
XACTCONST = Int32
XACTCONST_TIMEOUTINFINITE: XACTCONST = 0
XACTHEURISTIC = Int32
XACTHEURISTIC_ABORT: XACTHEURISTIC = 1
XACTHEURISTIC_COMMIT: XACTHEURISTIC = 2
XACTHEURISTIC_DAMAGE: XACTHEURISTIC = 3
XACTHEURISTIC_DANGER: XACTHEURISTIC = 4
class XACTOPT(Structure):
    ulTimeout: UInt32
    szDescription: Byte * 40
XACTRM = Int32
XACTRM_OPTIMISTICLASTWINS: XACTRM = 1
XACTRM_NOREADONLYPREPARES: XACTRM = 2
XACTSTAT = Int32
XACTSTAT_NONE: XACTSTAT = 0
XACTSTAT_OPENNORMAL: XACTSTAT = 1
XACTSTAT_OPENREFUSED: XACTSTAT = 2
XACTSTAT_PREPARING: XACTSTAT = 4
XACTSTAT_PREPARED: XACTSTAT = 8
XACTSTAT_PREPARERETAINING: XACTSTAT = 16
XACTSTAT_PREPARERETAINED: XACTSTAT = 32
XACTSTAT_COMMITTING: XACTSTAT = 64
XACTSTAT_COMMITRETAINING: XACTSTAT = 128
XACTSTAT_ABORTING: XACTSTAT = 256
XACTSTAT_ABORTED: XACTSTAT = 512
XACTSTAT_COMMITTED: XACTSTAT = 1024
XACTSTAT_HEURISTIC_ABORT: XACTSTAT = 2048
XACTSTAT_HEURISTIC_COMMIT: XACTSTAT = 4096
XACTSTAT_HEURISTIC_DAMAGE: XACTSTAT = 8192
XACTSTAT_HEURISTIC_DANGER: XACTSTAT = 16384
XACTSTAT_FORCED_ABORT: XACTSTAT = 32768
XACTSTAT_FORCED_COMMIT: XACTSTAT = 65536
XACTSTAT_INDOUBT: XACTSTAT = 131072
XACTSTAT_CLOSED: XACTSTAT = 262144
XACTSTAT_OPEN: XACTSTAT = 3
XACTSTAT_NOTPREPARED: XACTSTAT = 524227
XACTSTAT_ALL: XACTSTAT = 524287
class XACTSTATS(Structure):
    cOpen: UInt32
    cCommitting: UInt32
    cCommitted: UInt32
    cAborting: UInt32
    cAborted: UInt32
    cInDoubt: UInt32
    cHeuristicDecision: UInt32
    timeTransactionsUp: win32more.Foundation.FILETIME
XACTTC = Int32
XACTTC_NONE: XACTTC = 0
XACTTC_SYNC_PHASEONE: XACTTC = 1
XACTTC_SYNC_PHASETWO: XACTTC = 2
XACTTC_SYNC: XACTTC = 2
XACTTC_ASYNC_PHASEONE: XACTTC = 4
XACTTC_ASYNC: XACTTC = 4
class XACTTRANSINFO(Structure):
    uow: win32more.System.DistributedTransactionCoordinator.BOID
    isoLevel: Int32
    isoFlags: UInt32
    grfTCSupported: UInt32
    grfRMSupported: UInt32
    grfTCSupportedRetaining: UInt32
    grfRMSupportedRetaining: UInt32
class XID(Structure):
    formatID: Int32
    gtrid_length: Int32
    bqual_length: Int32
    data: win32more.Foundation.CHAR * 128
make_head(_module, 'BOID')
make_head(_module, 'DTC_GET_TRANSACTION_MANAGER')
make_head(_module, 'DTC_GET_TRANSACTION_MANAGER_EX_A')
make_head(_module, 'DTC_GET_TRANSACTION_MANAGER_EX_W')
make_head(_module, 'DTC_INSTALL_CLIENT')
make_head(_module, 'IDtcLuConfigure')
make_head(_module, 'IDtcLuRecovery')
make_head(_module, 'IDtcLuRecoveryFactory')
make_head(_module, 'IDtcLuRecoveryInitiatedByDtc')
make_head(_module, 'IDtcLuRecoveryInitiatedByDtcStatusWork')
make_head(_module, 'IDtcLuRecoveryInitiatedByDtcTransWork')
make_head(_module, 'IDtcLuRecoveryInitiatedByLu')
make_head(_module, 'IDtcLuRecoveryInitiatedByLuWork')
make_head(_module, 'IDtcLuRmEnlistment')
make_head(_module, 'IDtcLuRmEnlistmentFactory')
make_head(_module, 'IDtcLuRmEnlistmentSink')
make_head(_module, 'IDtcLuSubordinateDtc')
make_head(_module, 'IDtcLuSubordinateDtcFactory')
make_head(_module, 'IDtcLuSubordinateDtcSink')
make_head(_module, 'IDtcNetworkAccessConfig')
make_head(_module, 'IDtcNetworkAccessConfig2')
make_head(_module, 'IDtcNetworkAccessConfig3')
make_head(_module, 'IDtcToXaHelper')
make_head(_module, 'IDtcToXaHelperFactory')
make_head(_module, 'IDtcToXaHelperSinglePipe')
make_head(_module, 'IDtcToXaMapper')
make_head(_module, 'IGetDispenser')
make_head(_module, 'IKernelTransaction')
make_head(_module, 'ILastResourceManager')
make_head(_module, 'IPrepareInfo')
make_head(_module, 'IPrepareInfo2')
make_head(_module, 'IResourceManager')
make_head(_module, 'IResourceManager2')
make_head(_module, 'IResourceManagerFactory')
make_head(_module, 'IResourceManagerFactory2')
make_head(_module, 'IResourceManagerRejoinable')
make_head(_module, 'IResourceManagerSink')
make_head(_module, 'IRMHelper')
make_head(_module, 'ITipHelper')
make_head(_module, 'ITipPullSink')
make_head(_module, 'ITipTransaction')
make_head(_module, 'ITmNodeName')
make_head(_module, 'ITransaction')
make_head(_module, 'ITransaction2')
make_head(_module, 'ITransactionCloner')
make_head(_module, 'ITransactionDispenser')
make_head(_module, 'ITransactionEnlistmentAsync')
make_head(_module, 'ITransactionExport')
make_head(_module, 'ITransactionExportFactory')
make_head(_module, 'ITransactionImport')
make_head(_module, 'ITransactionImportWhereabouts')
make_head(_module, 'ITransactionLastEnlistmentAsync')
make_head(_module, 'ITransactionLastResourceAsync')
make_head(_module, 'ITransactionOptions')
make_head(_module, 'ITransactionOutcomeEvents')
make_head(_module, 'ITransactionPhase0EnlistmentAsync')
make_head(_module, 'ITransactionPhase0Factory')
make_head(_module, 'ITransactionPhase0NotifyAsync')
make_head(_module, 'ITransactionReceiver')
make_head(_module, 'ITransactionReceiverFactory')
make_head(_module, 'ITransactionResource')
make_head(_module, 'ITransactionResourceAsync')
make_head(_module, 'ITransactionTransmitter')
make_head(_module, 'ITransactionTransmitterFactory')
make_head(_module, 'ITransactionVoterBallotAsync2')
make_head(_module, 'ITransactionVoterFactory2')
make_head(_module, 'ITransactionVoterNotifyAsync2')
make_head(_module, 'IXAConfig')
make_head(_module, 'IXAObtainRMInfo')
make_head(_module, 'IXATransLookup')
make_head(_module, 'IXATransLookup2')
make_head(_module, 'OLE_TM_CONFIG_PARAMS_V1')
make_head(_module, 'OLE_TM_CONFIG_PARAMS_V2')
make_head(_module, 'PROXY_CONFIG_PARAMS')
make_head(_module, 'XA_CLOSE_EPT')
make_head(_module, 'XA_COMMIT_EPT')
make_head(_module, 'XA_COMPLETE_EPT')
make_head(_module, 'XA_END_EPT')
make_head(_module, 'XA_FORGET_EPT')
make_head(_module, 'XA_OPEN_EPT')
make_head(_module, 'XA_PREPARE_EPT')
make_head(_module, 'XA_RECOVER_EPT')
make_head(_module, 'XA_ROLLBACK_EPT')
make_head(_module, 'XA_START_EPT')
make_head(_module, 'xa_switch_t')
make_head(_module, 'XACTOPT')
make_head(_module, 'XACTSTATS')
make_head(_module, 'XACTTRANSINFO')
make_head(_module, 'XID')
__all__ = [
    "APPLICATIONTYPE",
    "AUTHENTICATION_LEVEL",
    "BOID",
    "CLSID_MSDtcTransaction",
    "CLSID_MSDtcTransactionManager",
    "CLUSTERRESOURCE_APPLICATIONTYPE",
    "DTCINITIATEDRECOVERYWORK",
    "DTCINITIATEDRECOVERYWORK_CHECKLUSTATUS",
    "DTCINITIATEDRECOVERYWORK_TMDOWN",
    "DTCINITIATEDRECOVERYWORK_TRANS",
    "DTCINSTALL_E_CLIENT_ALREADY_INSTALLED",
    "DTCINSTALL_E_SERVER_ALREADY_INSTALLED",
    "DTCLUCOMPARESTATE",
    "DTCLUCOMPARESTATESCONFIRMATION",
    "DTCLUCOMPARESTATESCONFIRMATION_CONFIRM",
    "DTCLUCOMPARESTATESCONFIRMATION_PROTOCOL",
    "DTCLUCOMPARESTATESERROR",
    "DTCLUCOMPARESTATESERROR_PROTOCOL",
    "DTCLUCOMPARESTATESRESPONSE",
    "DTCLUCOMPARESTATESRESPONSE_OK",
    "DTCLUCOMPARESTATESRESPONSE_PROTOCOL",
    "DTCLUCOMPARESTATE_COMMITTED",
    "DTCLUCOMPARESTATE_HEURISTICCOMMITTED",
    "DTCLUCOMPARESTATE_HEURISTICMIXED",
    "DTCLUCOMPARESTATE_HEURISTICRESET",
    "DTCLUCOMPARESTATE_INDOUBT",
    "DTCLUCOMPARESTATE_RESET",
    "DTCLUXLN",
    "DTCLUXLNCONFIRMATION",
    "DTCLUXLNCONFIRMATION_COLDWARMMISMATCH",
    "DTCLUXLNCONFIRMATION_CONFIRM",
    "DTCLUXLNCONFIRMATION_LOGNAMEMISMATCH",
    "DTCLUXLNCONFIRMATION_OBSOLETE",
    "DTCLUXLNERROR",
    "DTCLUXLNERROR_COLDWARMMISMATCH",
    "DTCLUXLNERROR_LOGNAMEMISMATCH",
    "DTCLUXLNERROR_PROTOCOL",
    "DTCLUXLNRESPONSE",
    "DTCLUXLNRESPONSE_COLDWARMMISMATCH",
    "DTCLUXLNRESPONSE_LOGNAMEMISMATCH",
    "DTCLUXLNRESPONSE_OK_SENDCONFIRMATION",
    "DTCLUXLNRESPONSE_OK_SENDOURXLNBACK",
    "DTCLUXLN_COLD",
    "DTCLUXLN_WARM",
    "DTC_GET_TRANSACTION_MANAGER",
    "DTC_GET_TRANSACTION_MANAGER_EX_A",
    "DTC_GET_TRANSACTION_MANAGER_EX_W",
    "DTC_INSTALL_CLIENT",
    "DTC_INSTALL_OVERWRITE_CLIENT",
    "DTC_INSTALL_OVERWRITE_SERVER",
    "DTC_STATUS_",
    "DTC_STATUS_CONTINUING",
    "DTC_STATUS_E_CANTCONTROL",
    "DTC_STATUS_FAILED",
    "DTC_STATUS_PAUSED",
    "DTC_STATUS_PAUSING",
    "DTC_STATUS_STARTED",
    "DTC_STATUS_STARTING",
    "DTC_STATUS_STOPPED",
    "DTC_STATUS_STOPPING",
    "DTC_STATUS_UNKNOWN",
    "DtcGetTransactionManager",
    "DtcGetTransactionManagerC",
    "DtcGetTransactionManagerExA",
    "DtcGetTransactionManagerExW",
    "IDtcLuConfigure",
    "IDtcLuRecovery",
    "IDtcLuRecoveryFactory",
    "IDtcLuRecoveryInitiatedByDtc",
    "IDtcLuRecoveryInitiatedByDtcStatusWork",
    "IDtcLuRecoveryInitiatedByDtcTransWork",
    "IDtcLuRecoveryInitiatedByLu",
    "IDtcLuRecoveryInitiatedByLuWork",
    "IDtcLuRmEnlistment",
    "IDtcLuRmEnlistmentFactory",
    "IDtcLuRmEnlistmentSink",
    "IDtcLuSubordinateDtc",
    "IDtcLuSubordinateDtcFactory",
    "IDtcLuSubordinateDtcSink",
    "IDtcNetworkAccessConfig",
    "IDtcNetworkAccessConfig2",
    "IDtcNetworkAccessConfig3",
    "IDtcToXaHelper",
    "IDtcToXaHelperFactory",
    "IDtcToXaHelperSinglePipe",
    "IDtcToXaMapper",
    "IGetDispenser",
    "IKernelTransaction",
    "ILastResourceManager",
    "INCOMING_AUTHENTICATION_REQUIRED",
    "IPrepareInfo",
    "IPrepareInfo2",
    "IRMHelper",
    "IResourceManager",
    "IResourceManager2",
    "IResourceManagerFactory",
    "IResourceManagerFactory2",
    "IResourceManagerRejoinable",
    "IResourceManagerSink",
    "ISOFLAG",
    "ISOFLAG_OPTIMISTIC",
    "ISOFLAG_READONLY",
    "ISOFLAG_RETAIN_ABORT",
    "ISOFLAG_RETAIN_ABORT_DC",
    "ISOFLAG_RETAIN_ABORT_NO",
    "ISOFLAG_RETAIN_BOTH",
    "ISOFLAG_RETAIN_COMMIT",
    "ISOFLAG_RETAIN_COMMIT_DC",
    "ISOFLAG_RETAIN_COMMIT_NO",
    "ISOFLAG_RETAIN_DONTCARE",
    "ISOFLAG_RETAIN_NONE",
    "ISOLATIONLEVEL",
    "ISOLATIONLEVEL_BROWSE",
    "ISOLATIONLEVEL_CHAOS",
    "ISOLATIONLEVEL_CURSORSTABILITY",
    "ISOLATIONLEVEL_ISOLATED",
    "ISOLATIONLEVEL_READCOMMITTED",
    "ISOLATIONLEVEL_READUNCOMMITTED",
    "ISOLATIONLEVEL_REPEATABLEREAD",
    "ISOLATIONLEVEL_SERIALIZABLE",
    "ISOLATIONLEVEL_UNSPECIFIED",
    "ITipHelper",
    "ITipPullSink",
    "ITipTransaction",
    "ITmNodeName",
    "ITransaction",
    "ITransaction2",
    "ITransactionCloner",
    "ITransactionDispenser",
    "ITransactionEnlistmentAsync",
    "ITransactionExport",
    "ITransactionExportFactory",
    "ITransactionImport",
    "ITransactionImportWhereabouts",
    "ITransactionLastEnlistmentAsync",
    "ITransactionLastResourceAsync",
    "ITransactionOptions",
    "ITransactionOutcomeEvents",
    "ITransactionPhase0EnlistmentAsync",
    "ITransactionPhase0Factory",
    "ITransactionPhase0NotifyAsync",
    "ITransactionReceiver",
    "ITransactionReceiverFactory",
    "ITransactionResource",
    "ITransactionResourceAsync",
    "ITransactionTransmitter",
    "ITransactionTransmitterFactory",
    "ITransactionVoterBallotAsync2",
    "ITransactionVoterFactory2",
    "ITransactionVoterNotifyAsync2",
    "IXAConfig",
    "IXAObtainRMInfo",
    "IXATransLookup",
    "IXATransLookup2",
    "LOCAL_APPLICATIONTYPE",
    "MAXBQUALSIZE",
    "MAXGTRIDSIZE",
    "MAXINFOSIZE",
    "MAX_TRAN_DESC",
    "MUTUAL_AUTHENTICATION_REQUIRED",
    "NO_AUTHENTICATION_REQUIRED",
    "OLE_TM_CONFIG_PARAMS_V1",
    "OLE_TM_CONFIG_PARAMS_V2",
    "OLE_TM_CONFIG_VERSION_1",
    "OLE_TM_CONFIG_VERSION_2",
    "OLE_TM_FLAG_INTERNAL_TO_TM",
    "OLE_TM_FLAG_NOAGILERECOVERY",
    "OLE_TM_FLAG_NODEMANDSTART",
    "OLE_TM_FLAG_NONE",
    "OLE_TM_FLAG_QUERY_SERVICE_LOCKSTATUS",
    "PROXY_CONFIG_PARAMS",
    "RMNAMESZ",
    "TMASYNC",
    "TMENDRSCAN",
    "TMER_INVAL",
    "TMER_PROTO",
    "TMER_TMERR",
    "TMFAIL",
    "TMJOIN",
    "TMMIGRATE",
    "TMMULTIPLE",
    "TMNOFLAGS",
    "TMNOMIGRATE",
    "TMNOWAIT",
    "TMONEPHASE",
    "TMREGISTER",
    "TMRESUME",
    "TMSTARTRSCAN",
    "TMSUCCESS",
    "TMSUSPEND",
    "TMUSEASYNC",
    "TM_JOIN",
    "TM_OK",
    "TM_RESUME",
    "TX_MISC_CONSTANTS",
    "XACTCONST",
    "XACTCONST_TIMEOUTINFINITE",
    "XACTHEURISTIC",
    "XACTHEURISTIC_ABORT",
    "XACTHEURISTIC_COMMIT",
    "XACTHEURISTIC_DAMAGE",
    "XACTHEURISTIC_DANGER",
    "XACTOPT",
    "XACTRM",
    "XACTRM_NOREADONLYPREPARES",
    "XACTRM_OPTIMISTICLASTWINS",
    "XACTSTAT",
    "XACTSTATS",
    "XACTSTAT_ABORTED",
    "XACTSTAT_ABORTING",
    "XACTSTAT_ALL",
    "XACTSTAT_CLOSED",
    "XACTSTAT_COMMITRETAINING",
    "XACTSTAT_COMMITTED",
    "XACTSTAT_COMMITTING",
    "XACTSTAT_FORCED_ABORT",
    "XACTSTAT_FORCED_COMMIT",
    "XACTSTAT_HEURISTIC_ABORT",
    "XACTSTAT_HEURISTIC_COMMIT",
    "XACTSTAT_HEURISTIC_DAMAGE",
    "XACTSTAT_HEURISTIC_DANGER",
    "XACTSTAT_INDOUBT",
    "XACTSTAT_NONE",
    "XACTSTAT_NOTPREPARED",
    "XACTSTAT_OPEN",
    "XACTSTAT_OPENNORMAL",
    "XACTSTAT_OPENREFUSED",
    "XACTSTAT_PREPARED",
    "XACTSTAT_PREPARERETAINED",
    "XACTSTAT_PREPARERETAINING",
    "XACTSTAT_PREPARING",
    "XACTTC",
    "XACTTC_ASYNC",
    "XACTTC_ASYNC_PHASEONE",
    "XACTTC_NONE",
    "XACTTC_SYNC",
    "XACTTC_SYNC_PHASEONE",
    "XACTTC_SYNC_PHASETWO",
    "XACTTRANSINFO",
    "XACT_DTC_CONSTANTS",
    "XACT_E_CONNECTION_REQUEST_DENIED",
    "XACT_E_DUPLICATE_GUID",
    "XACT_E_DUPLICATE_LU",
    "XACT_E_DUPLICATE_TRANSID",
    "XACT_E_LRMRECOVERYALREADYDONE",
    "XACT_E_LU_BUSY",
    "XACT_E_LU_DOWN",
    "XACT_E_LU_NOT_CONNECTED",
    "XACT_E_LU_NOT_FOUND",
    "XACT_E_LU_NO_RECOVERY_PROCESS",
    "XACT_E_LU_RECOVERING",
    "XACT_E_LU_RECOVERY_MISMATCH",
    "XACT_E_NOLASTRESOURCEINTERFACE",
    "XACT_E_NOTSINGLEPHASE",
    "XACT_E_PROTOCOL",
    "XACT_E_RECOVERYALREADYDONE",
    "XACT_E_RECOVERY_FAILED",
    "XACT_E_RM_FAILURE",
    "XACT_E_RM_UNAVAILABLE",
    "XACT_E_TOOMANY_ENLISTMENTS",
    "XACT_OK_NONOTIFY",
    "XACT_S_NONOTIFY",
    "XAER_ASYNC",
    "XAER_DUPID",
    "XAER_INVAL",
    "XAER_NOTA",
    "XAER_OUTSIDE",
    "XAER_PROTO",
    "XAER_RMERR",
    "XAER_RMFAIL",
    "XA_CLOSE_EPT",
    "XA_COMMIT_EPT",
    "XA_COMPLETE_EPT",
    "XA_END_EPT",
    "XA_FMTID_DTC",
    "XA_FMTID_DTC_VER1",
    "XA_FORGET_EPT",
    "XA_HEURCOM",
    "XA_HEURHAZ",
    "XA_HEURMIX",
    "XA_HEURRB",
    "XA_NOMIGRATE",
    "XA_OK",
    "XA_OPEN_EPT",
    "XA_PREPARE_EPT",
    "XA_RBBASE",
    "XA_RBCOMMFAIL",
    "XA_RBDEADLOCK",
    "XA_RBEND",
    "XA_RBINTEGRITY",
    "XA_RBOTHER",
    "XA_RBPROTO",
    "XA_RBROLLBACK",
    "XA_RBTIMEOUT",
    "XA_RBTRANSIENT",
    "XA_RDONLY",
    "XA_RECOVER_EPT",
    "XA_RETRY",
    "XA_ROLLBACK_EPT",
    "XA_START_EPT",
    "XA_SWITCH_F_DTC",
    "XID",
    "XIDDATASIZE",
    "dwUSER_MS_SQLSERVER",
    "xa_switch_t",
]
_arch_optional = [
]
