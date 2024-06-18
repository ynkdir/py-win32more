from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.DistributedTransactionCoordinator
APPLICATIONTYPE = Int32
LOCAL_APPLICATIONTYPE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.APPLICATIONTYPE = 0
CLUSTERRESOURCE_APPLICATIONTYPE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.APPLICATIONTYPE = 1
AUTHENTICATION_LEVEL = Int32
NO_AUTHENTICATION_REQUIRED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL = 0
INCOMING_AUTHENTICATION_REQUIRED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL = 1
MUTUAL_AUTHENTICATION_REQUIRED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL = 2
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
CLSID_MSDtcTransactionManager: Guid = Guid('{5b18ab61-091d-11d1-97df-00c04fb9618a}')
CLSID_MSDtcTransaction: Guid = Guid('{39f8d76b-0928-11d1-97df-00c04fb9618a}')
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManager(i_pszHost: win32more.Windows.Win32.Foundation.PSTR, i_pszTmName: win32more.Windows.Win32.Foundation.PSTR, i_riid: POINTER(Guid), i_dwReserved1: UInt32, i_wcbReserved2: UInt16, i_pvReserved2: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerC(i_pszHost: win32more.Windows.Win32.Foundation.PSTR, i_pszTmName: win32more.Windows.Win32.Foundation.PSTR, i_riid: POINTER(Guid), i_dwReserved1: UInt32, i_wcbReserved2: UInt16, i_pvReserved2: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerExA(i_pszHost: win32more.Windows.Win32.Foundation.PSTR, i_pszTmName: win32more.Windows.Win32.Foundation.PSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('XOLEHLP.dll')
def DtcGetTransactionManagerExW(i_pwszHost: win32more.Windows.Win32.Foundation.PWSTR, i_pwszTmName: win32more.Windows.Win32.Foundation.PWSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DtcGetTransactionManagerEx = UnicodeAlias('DtcGetTransactionManagerExW')
class BOID(Structure):
    rgb: Byte * 16
DTCINITIATEDRECOVERYWORK = Int32
DTCINITIATEDRECOVERYWORK_CHECKLUSTATUS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCINITIATEDRECOVERYWORK = 1
DTCINITIATEDRECOVERYWORK_TRANS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCINITIATEDRECOVERYWORK = 2
DTCINITIATEDRECOVERYWORK_TMDOWN: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCINITIATEDRECOVERYWORK = 3
DTCLUCOMPARESTATE = Int32
DTCLUCOMPARESTATE_COMMITTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 1
DTCLUCOMPARESTATE_HEURISTICCOMMITTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 2
DTCLUCOMPARESTATE_HEURISTICMIXED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 3
DTCLUCOMPARESTATE_HEURISTICRESET: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 4
DTCLUCOMPARESTATE_INDOUBT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 5
DTCLUCOMPARESTATE_RESET: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE = 6
DTCLUCOMPARESTATESCONFIRMATION = Int32
DTCLUCOMPARESTATESCONFIRMATION_CONFIRM: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION = 1
DTCLUCOMPARESTATESCONFIRMATION_PROTOCOL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION = 2
DTCLUCOMPARESTATESERROR = Int32
DTCLUCOMPARESTATESERROR_PROTOCOL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESERROR = 1
DTCLUCOMPARESTATESRESPONSE = Int32
DTCLUCOMPARESTATESRESPONSE_OK: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESRESPONSE = 1
DTCLUCOMPARESTATESRESPONSE_PROTOCOL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESRESPONSE = 2
DTCLUXLN = Int32
DTCLUXLN_COLD: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN = 1
DTCLUXLN_WARM: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN = 2
DTCLUXLNCONFIRMATION = Int32
DTCLUXLNCONFIRMATION_CONFIRM: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION = 1
DTCLUXLNCONFIRMATION_LOGNAMEMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION = 2
DTCLUXLNCONFIRMATION_COLDWARMMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION = 3
DTCLUXLNCONFIRMATION_OBSOLETE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION = 4
DTCLUXLNERROR = Int32
DTCLUXLNERROR_PROTOCOL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNERROR = 1
DTCLUXLNERROR_LOGNAMEMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNERROR = 2
DTCLUXLNERROR_COLDWARMMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNERROR = 3
DTCLUXLNRESPONSE = Int32
DTCLUXLNRESPONSE_OK_SENDOURXLNBACK: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE = 1
DTCLUXLNRESPONSE_OK_SENDCONFIRMATION: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE = 2
DTCLUXLNRESPONSE_LOGNAMEMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE = 3
DTCLUXLNRESPONSE_COLDWARMMISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE = 4
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER(pszHost: win32more.Windows.Win32.Foundation.PSTR, pszTmName: win32more.Windows.Win32.Foundation.PSTR, rid: POINTER(Guid), dwReserved1: UInt32, wcbReserved2: UInt16, pvReserved2: VoidPtr, ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER_EX_A(i_pszHost: win32more.Windows.Win32.Foundation.PSTR, i_pszTmName: win32more.Windows.Win32.Foundation.PSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype_pointer
def DTC_GET_TRANSACTION_MANAGER_EX_W(i_pwszHost: win32more.Windows.Win32.Foundation.PWSTR, i_pwszTmName: win32more.Windows.Win32.Foundation.PWSTR, i_riid: POINTER(Guid), i_grfOptions: UInt32, i_pvConfigParams: VoidPtr, o_ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DTC_GET_TRANSACTION_MANAGER_EX = UnicodeAlias('DTC_GET_TRANSACTION_MANAGER_EX_W')
@winfunctype_pointer
def DTC_INSTALL_CLIENT(i_pszRemoteTmHostName: POINTER(SByte), i_dwProtocol: UInt32, i_dwOverwrite: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DTC_STATUS_ = Int32
DTC_STATUS_UNKNOWN: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 0
DTC_STATUS_STARTING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 1
DTC_STATUS_STARTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 2
DTC_STATUS_PAUSING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 3
DTC_STATUS_PAUSED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 4
DTC_STATUS_CONTINUING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 5
DTC_STATUS_STOPPING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 6
DTC_STATUS_STOPPED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 7
DTC_STATUS_E_CANTCONTROL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 8
DTC_STATUS_FAILED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTC_STATUS_ = 9
class IDtcLuConfigure(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e760-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Add(self, pucLuPair: POINTER(Byte), cbLuPair: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, pucLuPair: POINTER(Byte), cbLuPair: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecovery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ac2b8ad2-d6f0-11d0-b386-00a0c9083365}')
class IDtcLuRecoveryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e762-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Create(self, pucLuPair: POINTER(Byte), cbLuPair: UInt32, ppRecovery: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuRecovery)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e764-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def GetWork(self, pWork: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCINITIATEDRECOVERYWORK), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtcStatusWork(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e766-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def HandleCheckLuStatus(self, lRecoverySeqNum: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByDtcTransWork(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e765-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def GetLogNameSizes(self, pcbOurLogName: POINTER(UInt32), pcbRemoteLogName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOurXln(self, pXln: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN), pOurLogName: POINTER(Byte), pRemoteLogName: POINTER(Byte), pdwProtocol: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HandleConfirmationFromOurXln(self, Confirmation: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HandleTheirXlnResponse(self, Xln: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN, pRemoteLogName: POINTER(Byte), cbRemoteLogName: UInt32, dwProtocol: UInt32, pConfirmation: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HandleErrorFromOurXln(self, Error: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNERROR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CheckForCompareStates(self, fCompareStates: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOurTransIdSize(self, pcbOurTransId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOurCompareStates(self, pOurTransId: POINTER(Byte), pCompareState: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def HandleTheirCompareStatesResponse(self, CompareState: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE, pConfirmation: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def HandleErrorFromOurCompareStates(self, Error: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESERROR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ConversationLost(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRecoverySeqNum(self, plRecoverySeqNum: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ObsoleteRecoverySeqNum(self, lNewRecoverySeqNum: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByLu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e768-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def GetObjectToHandleWorkFromLu(self, ppWork: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByLuWork)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRecoveryInitiatedByLuWork(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ac2b8ad1-d6f0-11d0-b386-00a0c9083365}')
    @commethod(3)
    def HandleTheirXln(self, lRecoverySeqNum: Int32, Xln: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN, pRemoteLogName: POINTER(Byte), cbRemoteLogName: UInt32, pOurLogName: POINTER(Byte), cbOurLogName: UInt32, dwProtocol: UInt32, pResponse: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNRESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOurLogNameSize(self, pcbOurLogName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOurXln(self, pXln: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLN), pOurLogName: POINTER(Byte), pdwProtocol: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HandleConfirmationOfOurXln(self, Confirmation: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUXLNCONFIRMATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HandleTheirCompareStates(self, pRemoteTransId: POINTER(Byte), cbRemoteTransId: UInt32, CompareState: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE, pResponse: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESRESPONSE), pCompareState: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def HandleConfirmationOfOurCompareStates(self, Confirmation: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESCONFIRMATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HandleErrorFromOurCompareStates(self, Error: win32more.Windows.Win32.System.DistributedTransactionCoordinator.DTCLUCOMPARESTATESERROR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ConversationLost(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRmEnlistment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e769-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Unplug(self, fConversationLost: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BackedOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BackOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Committed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Forget(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRmEnlistmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e771-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Create(self, pucLuPair: POINTER(Byte), cbLuPair: UInt32, pITransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, pTransId: POINTER(Byte), cbTransId: UInt32, pRmEnlistmentSink: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuRmEnlistmentSink, ppRmEnlistment: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuRmEnlistment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuRmEnlistmentSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e770-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def AckUnplug(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TmDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SessionLost(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BackedOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BackOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Committed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Forget(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Prepare(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuSubordinateDtc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e773-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Unplug(self, fConversationLost: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BackedOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BackOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Committed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Forget(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Prepare(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuSubordinateDtcFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e775-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def Create(self, pucLuPair: POINTER(Byte), cbLuPair: UInt32, punkTransactionOuter: win32more.Windows.Win32.System.Com.IUnknown, isoLevel: Int32, isoFlags: UInt32, pOptions: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionOptions, ppTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction), pTransId: POINTER(Byte), cbTransId: UInt32, pSubordinateDtcSink: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtcSink, ppSubordinateDtc: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtc)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcLuSubordinateDtcSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4131e774-1aea-11d0-944b-00a0c905416e}')
    @commethod(3)
    def AckUnplug(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TmDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SessionLost(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BackedOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BackOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Committed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Forget(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9797c15d-a428-4291-87b6-0995031a678d}')
    @commethod(3)
    def GetAnyNetworkAccess(self, pbAnyNetworkAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAnyNetworkAccess(self, bAnyNetworkAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNetworkAdministrationAccess(self, pbNetworkAdministrationAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNetworkAdministrationAccess(self, bNetworkAdministrationAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNetworkTransactionAccess(self, pbNetworkTransactionAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetNetworkTransactionAccess(self, bNetworkTransactionAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNetworkClientAccess(self, pbNetworkClientAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetNetworkClientAccess(self, bNetworkClientAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetNetworkTIPAccess(self, pbNetworkTIPAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetNetworkTIPAccess(self, bNetworkTIPAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetXAAccess(self, pbXAAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetXAAccess(self, bXAAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RestartDtcService(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig2(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig
    _iid_ = Guid('{a7aa013b-eb7d-4f42-b41c-b2dec09ae034}')
    @commethod(16)
    def GetNetworkInboundAccess(self, pbInbound: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNetworkOutboundAccess(self, pbOutbound: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetNetworkInboundAccess(self, bInbound: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetNetworkOutboundAccess(self, bOutbound: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetAuthenticationLevel(self, pAuthLevel: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetAuthenticationLevel(self, AuthLevel: win32more.Windows.Win32.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcNetworkAccessConfig3(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig2
    _iid_ = Guid('{76e4b4f3-2ca5-466b-89d5-fd218ee75b49}')
    @commethod(22)
    def GetLUAccess(self, pbLUAccess: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetLUAccess(self, bLUAccess: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcToXaHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9861611-304a-11d1-9813-00a0c905416e}')
    @commethod(3)
    def Close(self, i_fDoRecovery: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateTridToXid(self, pITransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, pguidBqual: POINTER(Guid), pXid: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcToXaHelperFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9861610-304a-11d1-9813-00a0c905416e}')
    @commethod(3)
    def Create(self, pszDSN: win32more.Windows.Win32.Foundation.PSTR, pszClientDllName: win32more.Windows.Win32.Foundation.PSTR, pguidRm: POINTER(Guid), ppXaHelper: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IDtcToXaHelper)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDtcToXaHelperSinglePipe(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{47ed4971-53b3-11d1-bbb9-00c04fd658f6}')
    @commethod(3)
    def XARMCreate(self, pszDSN: win32more.Windows.Win32.Foundation.PSTR, pszClientDll: win32more.Windows.Win32.Foundation.PSTR, pdwRMCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertTridToXID(self, pdwITrans: POINTER(UInt32), dwRMCookie: UInt32, pxid: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistWithRM(self, dwRMCookie: UInt32, i_pITransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, i_pITransRes: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionResourceAsync, o_ppITransEnslitment: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseRMCookie(self, i_dwRMCookie: UInt32, i_fNormal: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class IDtcToXaMapper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64ffabe0-7ce9-11d0-8ce6-00c04fdc877e}')
    @commethod(3)
    def RequestNewResourceManager(self, pszDSN: win32more.Windows.Win32.Foundation.PSTR, pszClientDllName: win32more.Windows.Win32.Foundation.PSTR, pdwRMCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateTridToXid(self, pdwITransaction: POINTER(UInt32), dwRMCookie: UInt32, pXid: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistResourceManager(self, dwRMCookie: UInt32, pdwITransaction: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseResourceManager(self, dwRMCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetDispenser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c23cc370-87ef-11ce-8081-0080c758527e}')
    @commethod(3)
    def GetDispenser(self, iid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IKernelTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79427a2b-f895-40e0-be79-b57dc82ed231}')
    @commethod(3)
    def GetHandle(self, pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILastResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d964ad4-5b33-11d3-8a91-00c04f79eb6d}')
    @commethod(3)
    def TransactionCommitted(self, pPrepInfo: POINTER(Byte), cbPrepInfo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RecoveryDone(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrepareInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80c7bfd0-87ee-11ce-8081-0080c758527e}')
    @commethod(3)
    def GetPrepareInfoSize(self, pcbPrepInfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrepareInfo(self, pPrepInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrepareInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5fab2547-9779-11d1-b886-00c04fb9618a}')
    @commethod(3)
    def GetPrepareInfoSize(self, pcbPrepInfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrepareInfo(self, cbPrepareInfo: UInt32, pPrepInfo: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRMHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e793f6d1-f53d-11cf-a60d-00a0c905416e}')
    @commethod(3)
    def RMCount(self, dwcTotalNumberOfRMs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RMInfo(self, pXa_Switch: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.xa_switch_t), fCDeclCallingConv: win32more.Windows.Win32.Foundation.BOOL, pszOpenString: win32more.Windows.Win32.Foundation.PSTR, pszCloseString: win32more.Windows.Win32.Foundation.PSTR, guidRMRecovery: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13741d21-87eb-11ce-8081-0080c758527e}')
    @commethod(3)
    def Enlist(self, pTransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, pRes: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionResourceAsync, pUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), pisoLevel: POINTER(Int32), ppEnlist: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reenlist(self, pPrepInfo: POINTER(Byte), cbPrepInfo: UInt32, lTimeout: UInt32, pXactStat: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReenlistmentComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDistributedTransactionManager(self, iid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManager2(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManager
    _iid_ = Guid('{d136c69a-f749-11d1-8f47-00c04f8ee57d}')
    @commethod(7)
    def Enlist2(self, pTransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, pResAsync: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionResourceAsync, pUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), pisoLevel: POINTER(Int32), pXid: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), ppEnlist: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reenlist2(self, pXid: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), dwTimeout: UInt32, pXactStat: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13741d20-87eb-11ce-8081-0080c758527e}')
    @commethod(3)
    def Create(self, pguidRM: POINTER(Guid), pszRMName: win32more.Windows.Win32.Foundation.PSTR, pIResMgrSink: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManagerSink, ppResMgr: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManagerFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManagerFactory
    _iid_ = Guid('{6b369c21-fbd2-11d1-8f47-00c04f8ee57d}')
    @commethod(4)
    def CreateEx(self, pguidRM: POINTER(Guid), pszRMName: win32more.Windows.Win32.Foundation.PSTR, pIResMgrSink: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManagerSink, riidRequested: POINTER(Guid), ppvResMgr: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManagerRejoinable(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IResourceManager2
    _iid_ = Guid('{6f6de620-b5df-4f3e-9cfa-c8aebd05172b}')
    @commethod(9)
    def Rejoin(self, pPrepInfo: POINTER(Byte), cbPrepInfo: UInt32, lTimeout: UInt32, pXactStat: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResourceManagerSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d563181-defb-11ce-aed1-00aa0051e2c4}')
    @commethod(3)
    def TMDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ISOFLAG = Int32
ISOFLAG_RETAIN_COMMIT_DC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 1
ISOFLAG_RETAIN_COMMIT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 2
ISOFLAG_RETAIN_COMMIT_NO: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 3
ISOFLAG_RETAIN_ABORT_DC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 4
ISOFLAG_RETAIN_ABORT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 8
ISOFLAG_RETAIN_ABORT_NO: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 12
ISOFLAG_RETAIN_DONTCARE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 5
ISOFLAG_RETAIN_BOTH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 10
ISOFLAG_RETAIN_NONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 15
ISOFLAG_OPTIMISTIC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 16
ISOFLAG_READONLY: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOFLAG = 32
ISOLATIONLEVEL = Int32
ISOLATIONLEVEL_UNSPECIFIED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = -1
ISOLATIONLEVEL_CHAOS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 16
ISOLATIONLEVEL_READUNCOMMITTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 256
ISOLATIONLEVEL_BROWSE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 256
ISOLATIONLEVEL_CURSORSTABILITY: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 4096
ISOLATIONLEVEL_READCOMMITTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 4096
ISOLATIONLEVEL_REPEATABLEREAD: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 65536
ISOLATIONLEVEL_SERIALIZABLE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 1048576
ISOLATIONLEVEL_ISOLATED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ISOLATIONLEVEL = 1048576
class ITipHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17cf72d1-bac5-11d1-b1bf-00c04fc2f3ef}')
    @commethod(3)
    def Pull(self, i_pszTxUrl: POINTER(Byte), o_ppITransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PullAsync(self, i_pszTxUrl: POINTER(Byte), i_pTipPullSink: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITipPullSink, o_ppITransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocalTmUrl(self, o_ppszLocalTmUrl: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITipPullSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17cf72d2-bac5-11d1-b1bf-00c04fc2f3ef}')
    @commethod(3)
    def PullComplete(self, i_hrPull: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITipTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17cf72d0-bac5-11d1-b1bf-00c04fc2f3ef}')
    @commethod(3)
    def Push(self, i_pszRemoteTmUrl: POINTER(Byte), o_ppszRemoteTxUrl: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionUrl(self, o_ppszLocalTxUrl: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITmNodeName(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30274f88-6ee4-474e-9b95-7807bc9ef8cf}')
    @commethod(3)
    def GetNodeNameSize(self, pcbNodeNameSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNodeName(self, cbNodeNameBufferSize: UInt32, pNodeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransaction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0fb15084-af41-11ce-bd2b-204c4f4f5020}')
    @commethod(3)
    def Commit(self, fRetaining: win32more.Windows.Win32.Foundation.BOOL, grfTC: UInt32, grfRM: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(self, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), fRetaining: win32more.Windows.Win32.Foundation.BOOL, fAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransactionInfo(self, pinfo: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTRANSINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransaction2(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionCloner
    _iid_ = Guid('{34021548-0065-11d3-bac1-00c04f797be2}')
    @commethod(7)
    def GetTransactionInfo2(self, pinfo: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTRANSINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionCloner(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction
    _iid_ = Guid('{02656950-2152-11d0-944c-00a0c905416e}')
    @commethod(6)
    def CloneWithCommitDisabled(self, ppITransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionDispenser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a6ad9e1-23b9-11cf-ad60-00aa00a74ccd}')
    @commethod(3)
    def GetOptionsObject(self, ppOptions: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginTransaction(self, punkOuter: win32more.Windows.Win32.System.Com.IUnknown, isoLevel: Int32, isoFlags: UInt32, pOptions: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionOptions, ppTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionEnlistmentAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0fb15081-af41-11ce-bd2b-204c4f4f5020}')
    @commethod(3)
    def PrepareRequestDone(self, hr: win32more.Windows.Win32.Foundation.HRESULT, pmk: win32more.Windows.Win32.System.Com.IMoniker, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequestDone(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequestDone(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionExport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0141fda5-8fc0-11ce-bd18-204c4f4f5020}')
    @commethod(3)
    def Export(self, punkTransaction: win32more.Windows.Win32.System.Com.IUnknown, pcbTransactionCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionCookie(self, punkTransaction: win32more.Windows.Win32.System.Com.IUnknown, cbTransactionCookie: UInt32, rgbTransactionCookie: POINTER(Byte), pcbUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionExportFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1cf9b53-8745-11ce-a9ba-00aa006c3706}')
    @commethod(3)
    def GetRemoteClassId(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Create(self, cbWhereabouts: UInt32, rgbWhereabouts: POINTER(Byte), ppExport: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionExport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionImport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1cf9b5a-8745-11ce-a9ba-00aa006c3706}')
    @commethod(3)
    def Import(self, cbTransactionCookie: UInt32, rgbTransactionCookie: POINTER(Byte), piid: POINTER(Guid), ppvTransaction: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionImportWhereabouts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0141fda4-8fc0-11ce-bd18-204c4f4f5020}')
    @commethod(3)
    def GetWhereaboutsSize(self, pcbWhereabouts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWhereabouts(self, cbWhereabouts: UInt32, rgbWhereabouts: POINTER(Byte), pcbUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionLastEnlistmentAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c82bd533-5b30-11d3-8a91-00c04f79eb6d}')
    @commethod(3)
    def TransactionOutcome(self, XactStat: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionLastResourceAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c82bd532-5b30-11d3-8a91-00c04f79eb6d}')
    @commethod(3)
    def DelegateCommit(self, grfRM: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ForgetRequest(self, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a6ad9e0-23b9-11cf-ad60-00aa00a74ccd}')
    @commethod(3)
    def SetOptions(self, pOptions: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTOPT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptions(self, pOptions: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTOPT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionOutcomeEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a6ad9e2-23b9-11cf-ad60-00aa00a74ccd}')
    @commethod(3)
    def Committed(self, fRetaining: win32more.Windows.Win32.Foundation.BOOL, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Aborted(self, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), fRetaining: win32more.Windows.Win32.Foundation.BOOL, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HeuristicDecision(self, dwDecision: UInt32, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Indoubt(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionPhase0EnlistmentAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82dc88e1-a954-11d1-8f88-00600895e7d5}')
    @commethod(3)
    def Enable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForEnlistment(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Phase0Done(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unenlist(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransaction(self, ppITransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionPhase0Factory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82dc88e0-a954-11d1-8f88-00600895e7d5}')
    @commethod(3)
    def Create(self, pPhase0Notify: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionPhase0NotifyAsync, ppPhase0Enlistment: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionPhase0EnlistmentAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionPhase0NotifyAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ef081809-0c76-11d2-87a6-00c04f990f34}')
    @commethod(3)
    def Phase0Request(self, fAbortingHint: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnlistCompleted(self, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59313e03-b36c-11cf-a539-00aa006887c3}')
    @commethod(3)
    def UnmarshalPropagationToken(self, cbToken: UInt32, rgbToken: POINTER(Byte), ppTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReturnTokenSize(self, pcbReturnToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MarshalReturnToken(self, cbReturnToken: UInt32, rgbReturnToken: POINTER(Byte), pcbUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionReceiverFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59313e02-b36c-11cf-a539-00aa006887c3}')
    @commethod(3)
    def Create(self, ppReceiver: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionReceiver)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionResource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee5ff7b3-4572-11d0-9452-00a0c905416e}')
    @commethod(3)
    def PrepareRequest(self, fRetaining: win32more.Windows.Win32.Foundation.BOOL, grfRM: UInt32, fWantMoniker: win32more.Windows.Win32.Foundation.BOOL, fSinglePhase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequest(self, grfRM: UInt32, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequest(self, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), fRetaining: win32more.Windows.Win32.Foundation.BOOL, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TMDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionResourceAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{69e971f0-23ce-11cf-ad60-00aa00a74ccd}')
    @commethod(3)
    def PrepareRequest(self, fRetaining: win32more.Windows.Win32.Foundation.BOOL, grfRM: UInt32, fWantMoniker: win32more.Windows.Win32.Foundation.BOOL, fSinglePhase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CommitRequest(self, grfRM: UInt32, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AbortRequest(self, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID), fRetaining: win32more.Windows.Win32.Foundation.BOOL, pNewUOW: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TMDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionTransmitter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59313e01-b36c-11cf-a539-00aa006887c3}')
    @commethod(3)
    def Set(self, pTransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropagationTokenSize(self, pcbToken: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MarshalPropagationToken(self, cbToken: UInt32, rgbToken: POINTER(Byte), pcbUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnmarshalReturnToken(self, cbReturnToken: UInt32, rgbReturnToken: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionTransmitterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59313e00-b36c-11cf-a539-00aa006887c3}')
    @commethod(3)
    def Create(self, ppTransmitter: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionTransmitter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionVoterBallotAsync2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5433376c-414d-11d3-b206-00c04fc2f3ef}')
    @commethod(3)
    def VoteRequestDone(self, hr: win32more.Windows.Win32.Foundation.HRESULT, pboidReason: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionVoterFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5433376a-414d-11d3-b206-00c04fc2f3ef}')
    @commethod(3)
    def Create(self, pTransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, pVoterNotify: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2, ppVoterBallot: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionVoterNotifyAsync2(ComPtr):
    extends: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionOutcomeEvents
    _iid_ = Guid('{5433376b-414d-11d3-b206-00c04fc2f3ef}')
    @commethod(7)
    def VoteRequest(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXAConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8a6e3a1-9a8c-11cf-a308-00a0c905416e}')
    @commethod(3)
    def Initialize(self, clsidHelperDll: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXAObtainRMInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e793f6d2-f53d-11cf-a60d-00a0c905416e}')
    @commethod(3)
    def ObtainRMInfo(self, pIRMHelper: win32more.Windows.Win32.System.DistributedTransactionCoordinator.IRMHelper) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXATransLookup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f3b1f131-eeda-11ce-aed4-00aa0051e2c4}')
    @commethod(3)
    def Lookup(self, ppTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXATransLookup2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf193c85-0d1a-4290-b88f-d2cb8873d1e7}')
    @commethod(3)
    def Lookup(self, pXID: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), ppTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OLE_TM_CONFIG_PARAMS_V1(Structure):
    dwVersion: UInt32
    dwcConcurrencyHint: UInt32
class OLE_TM_CONFIG_PARAMS_V2(Structure):
    dwVersion: UInt32
    dwcConcurrencyHint: UInt32
    applicationType: win32more.Windows.Win32.System.DistributedTransactionCoordinator.APPLICATIONTYPE
    clusterResourceId: Guid
class PROXY_CONFIG_PARAMS(Structure):
    wcThreadsMax: UInt16
TX_MISC_CONSTANTS = Int32
MAX_TRAN_DESC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.TX_MISC_CONSTANTS = 40
XACTCONST = Int32
XACTCONST_TIMEOUTINFINITE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTCONST = 0
XACTHEURISTIC = Int32
XACTHEURISTIC_ABORT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTHEURISTIC = 1
XACTHEURISTIC_COMMIT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTHEURISTIC = 2
XACTHEURISTIC_DAMAGE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTHEURISTIC = 3
XACTHEURISTIC_DANGER: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTHEURISTIC = 4
class XACTOPT(Structure):
    ulTimeout: UInt32
    szDescription: Byte * 40
XACTRM = Int32
XACTRM_OPTIMISTICLASTWINS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTRM = 1
XACTRM_NOREADONLYPREPARES: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTRM = 2
XACTSTAT = Int32
XACTSTAT_NONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 0
XACTSTAT_OPENNORMAL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 1
XACTSTAT_OPENREFUSED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 2
XACTSTAT_PREPARING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 4
XACTSTAT_PREPARED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 8
XACTSTAT_PREPARERETAINING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 16
XACTSTAT_PREPARERETAINED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 32
XACTSTAT_COMMITTING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 64
XACTSTAT_COMMITRETAINING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 128
XACTSTAT_ABORTING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 256
XACTSTAT_ABORTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 512
XACTSTAT_COMMITTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 1024
XACTSTAT_HEURISTIC_ABORT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 2048
XACTSTAT_HEURISTIC_COMMIT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 4096
XACTSTAT_HEURISTIC_DAMAGE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 8192
XACTSTAT_HEURISTIC_DANGER: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 16384
XACTSTAT_FORCED_ABORT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 32768
XACTSTAT_FORCED_COMMIT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 65536
XACTSTAT_INDOUBT: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 131072
XACTSTAT_CLOSED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 262144
XACTSTAT_OPEN: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 3
XACTSTAT_NOTPREPARED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 524227
XACTSTAT_ALL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTSTAT = 524287
class XACTSTATS(Structure):
    cOpen: UInt32
    cCommitting: UInt32
    cCommitted: UInt32
    cAborting: UInt32
    cAborted: UInt32
    cInDoubt: UInt32
    cHeuristicDecision: UInt32
    timeTransactionsUp: win32more.Windows.Win32.Foundation.FILETIME
XACTTC = Int32
XACTTC_NONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 0
XACTTC_SYNC_PHASEONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 1
XACTTC_SYNC_PHASETWO: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 2
XACTTC_SYNC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 2
XACTTC_ASYNC_PHASEONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 4
XACTTC_ASYNC: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACTTC = 4
class XACTTRANSINFO(Structure):
    uow: win32more.Windows.Win32.System.DistributedTransactionCoordinator.BOID
    isoLevel: Int32
    isoFlags: UInt32
    grfTCSupported: UInt32
    grfRMSupported: UInt32
    grfTCSupportedRetaining: UInt32
    grfRMSupportedRetaining: UInt32
XACT_DTC_CONSTANTS = Int32
XACT_E_CONNECTION_REQUEST_DENIED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147168000
XACT_E_TOOMANY_ENLISTMENTS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167999
XACT_E_DUPLICATE_GUID: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167998
XACT_E_NOTSINGLEPHASE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167997
XACT_E_RECOVERYALREADYDONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167996
XACT_E_PROTOCOL: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167995
XACT_E_RM_FAILURE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167994
XACT_E_RECOVERY_FAILED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167993
XACT_E_LU_NOT_FOUND: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167992
XACT_E_DUPLICATE_LU: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167991
XACT_E_LU_NOT_CONNECTED: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167990
XACT_E_DUPLICATE_TRANSID: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167989
XACT_E_LU_BUSY: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167988
XACT_E_LU_NO_RECOVERY_PROCESS: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167987
XACT_E_LU_DOWN: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167986
XACT_E_LU_RECOVERING: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167985
XACT_E_LU_RECOVERY_MISMATCH: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167984
XACT_E_RM_UNAVAILABLE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167983
XACT_E_LRMRECOVERYALREADYDONE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167982
XACT_E_NOLASTRESOURCEINTERFACE: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = -2147167981
XACT_S_NONOTIFY: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = 315648
XACT_OK_NONOTIFY: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = 315649
dwUSER_MS_SQLSERVER: win32more.Windows.Win32.System.DistributedTransactionCoordinator.XACT_DTC_CONSTANTS = 65535
@cfunctype_pointer
def XA_CLOSE_EPT(param0: win32more.Windows.Win32.Foundation.PSTR, param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_COMMIT_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_COMPLETE_EPT(param0: POINTER(Int32), param1: POINTER(Int32), param2: Int32, param3: Int32) -> Int32: ...
@cfunctype_pointer
def XA_END_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_FORGET_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_OPEN_EPT(param0: win32more.Windows.Win32.Foundation.PSTR, param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_PREPARE_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_RECOVER_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32, param3: Int32) -> Int32: ...
@cfunctype_pointer
def XA_ROLLBACK_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
@cfunctype_pointer
def XA_START_EPT(param0: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.XID), param1: Int32, param2: Int32) -> Int32: ...
class XID(Structure):
    formatID: Int32
    gtrid_length: Int32
    bqual_length: Int32
    data: win32more.Windows.Win32.Foundation.CHAR * 128
class xa_switch_t(Structure):
    name: win32more.Windows.Win32.Foundation.CHAR * 32
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


make_ready(__name__)
