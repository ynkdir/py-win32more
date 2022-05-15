from win32more import *
import win32more.System.DistributedTransactionCoordinator
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.DistributedTransactionCoordinator, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.DistributedTransactionCoordinator, name)
def __dir__():
    return __all__
DTCINSTALL_E_CLIENT_ALREADY_INSTALLED = 384
DTCINSTALL_E_SERVER_ALREADY_INSTALLED = 385
XA_SWITCH_F_DTC = 1
XA_FMTID_DTC = 4478019
XA_FMTID_DTC_VER1 = 21255235
XIDDATASIZE = 128
MAXGTRIDSIZE = 64
MAXBQUALSIZE = 64
RMNAMESZ = 32
MAXINFOSIZE = 256
TMNOFLAGS = 0
TMREGISTER = 1
TMNOMIGRATE = 2
TMUSEASYNC = 4
TMASYNC = -2147483648
TMONEPHASE = 1073741824
TMFAIL = 536870912
TMNOWAIT = 268435456
TMRESUME = 134217728
TMSUCCESS = 67108864
TMSUSPEND = 33554432
TMSTARTRSCAN = 16777216
TMENDRSCAN = 8388608
TMMULTIPLE = 4194304
TMJOIN = 2097152
TMMIGRATE = 1048576
TM_JOIN = 2
TM_RESUME = 1
TM_OK = 0
TMER_TMERR = -1
TMER_INVAL = -2
TMER_PROTO = -3
XA_RBBASE = 100
XA_RBROLLBACK = 100
XA_RBCOMMFAIL = 101
XA_RBDEADLOCK = 102
XA_RBINTEGRITY = 103
XA_RBOTHER = 104
XA_RBPROTO = 105
XA_RBTIMEOUT = 106
XA_RBTRANSIENT = 107
XA_RBEND = 107
XA_NOMIGRATE = 9
XA_HEURHAZ = 8
XA_HEURCOM = 7
XA_HEURRB = 6
XA_HEURMIX = 5
XA_RETRY = 4
XA_RDONLY = 3
XA_OK = 0
XAER_ASYNC = -2
XAER_RMERR = -3
XAER_NOTA = -4
XAER_INVAL = -5
XAER_PROTO = -6
XAER_RMFAIL = -7
XAER_DUPID = -8
XAER_OUTSIDE = -9
DTC_INSTALL_OVERWRITE_CLIENT = 1
DTC_INSTALL_OVERWRITE_SERVER = 2
OLE_TM_CONFIG_VERSION_1 = 1
OLE_TM_CONFIG_VERSION_2 = 2
OLE_TM_FLAG_NONE = 0
OLE_TM_FLAG_NODEMANDSTART = 1
OLE_TM_FLAG_NOAGILERECOVERY = 2
OLE_TM_FLAG_QUERY_SERVICE_LOCKSTATUS = 2147483648
OLE_TM_FLAG_INTERNAL_TO_TM = 1073741824
CLSID_MSDtcTransactionManager = '5b18ab61-091d-11d1-97df-00c04fb9618a'
CLSID_MSDtcTransaction = '39f8d76b-0928-11d1-97df-00c04fb9618a'
DTC_STATUS_ = Int32
DTC_STATUS_UNKNOWN = 0
DTC_STATUS_STARTING = 1
DTC_STATUS_STARTED = 2
DTC_STATUS_PAUSING = 3
DTC_STATUS_PAUSED = 4
DTC_STATUS_CONTINUING = 5
DTC_STATUS_STOPPING = 6
DTC_STATUS_STOPPED = 7
DTC_STATUS_E_CANTCONTROL = 8
DTC_STATUS_FAILED = 9
def _define_DTC_GET_TRANSACTION_MANAGER():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32,UInt16,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_DTC_GET_TRANSACTION_MANAGER_EX_A():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_DTC_GET_TRANSACTION_MANAGER_EX_W():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_DTC_INSTALL_CLIENT():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),UInt32,UInt32, use_last_error=False)
def _define_BOID_head():
    class BOID(Structure):
        pass
    return BOID
def _define_BOID():
    BOID = win32more.System.DistributedTransactionCoordinator.BOID_head
    BOID._fields_ = [
        ("rgb", Byte * 16),
    ]
    return BOID
TX_MISC_CONSTANTS = Int32
MAX_TRAN_DESC = 40
ISOLATIONLEVEL = Int32
ISOLATIONLEVEL_UNSPECIFIED = -1
ISOLATIONLEVEL_CHAOS = 16
ISOLATIONLEVEL_READUNCOMMITTED = 256
ISOLATIONLEVEL_BROWSE = 256
ISOLATIONLEVEL_CURSORSTABILITY = 4096
ISOLATIONLEVEL_READCOMMITTED = 4096
ISOLATIONLEVEL_REPEATABLEREAD = 65536
ISOLATIONLEVEL_SERIALIZABLE = 1048576
ISOLATIONLEVEL_ISOLATED = 1048576
def _define_XACTTRANSINFO_head():
    class XACTTRANSINFO(Structure):
        pass
    return XACTTRANSINFO
def _define_XACTTRANSINFO():
    XACTTRANSINFO = win32more.System.DistributedTransactionCoordinator.XACTTRANSINFO_head
    XACTTRANSINFO._fields_ = [
        ("uow", win32more.System.DistributedTransactionCoordinator.BOID),
        ("isoLevel", Int32),
        ("isoFlags", UInt32),
        ("grfTCSupported", UInt32),
        ("grfRMSupported", UInt32),
        ("grfTCSupportedRetaining", UInt32),
        ("grfRMSupportedRetaining", UInt32),
    ]
    return XACTTRANSINFO
def _define_XACTSTATS_head():
    class XACTSTATS(Structure):
        pass
    return XACTSTATS
def _define_XACTSTATS():
    XACTSTATS = win32more.System.DistributedTransactionCoordinator.XACTSTATS_head
    XACTSTATS._fields_ = [
        ("cOpen", UInt32),
        ("cCommitting", UInt32),
        ("cCommitted", UInt32),
        ("cAborting", UInt32),
        ("cAborted", UInt32),
        ("cInDoubt", UInt32),
        ("cHeuristicDecision", UInt32),
        ("timeTransactionsUp", win32more.Foundation.FILETIME),
    ]
    return XACTSTATS
ISOFLAG = Int32
ISOFLAG_RETAIN_COMMIT_DC = 1
ISOFLAG_RETAIN_COMMIT = 2
ISOFLAG_RETAIN_COMMIT_NO = 3
ISOFLAG_RETAIN_ABORT_DC = 4
ISOFLAG_RETAIN_ABORT = 8
ISOFLAG_RETAIN_ABORT_NO = 12
ISOFLAG_RETAIN_DONTCARE = 5
ISOFLAG_RETAIN_BOTH = 10
ISOFLAG_RETAIN_NONE = 15
ISOFLAG_OPTIMISTIC = 16
ISOFLAG_READONLY = 32
XACTTC = Int32
XACTTC_NONE = 0
XACTTC_SYNC_PHASEONE = 1
XACTTC_SYNC_PHASETWO = 2
XACTTC_SYNC = 2
XACTTC_ASYNC_PHASEONE = 4
XACTTC_ASYNC = 4
XACTRM = Int32
XACTRM_OPTIMISTICLASTWINS = 1
XACTRM_NOREADONLYPREPARES = 2
XACTCONST = Int32
XACTCONST_TIMEOUTINFINITE = 0
XACTHEURISTIC = Int32
XACTHEURISTIC_ABORT = 1
XACTHEURISTIC_COMMIT = 2
XACTHEURISTIC_DAMAGE = 3
XACTHEURISTIC_DANGER = 4
XACTSTAT = Int32
XACTSTAT_NONE = 0
XACTSTAT_OPENNORMAL = 1
XACTSTAT_OPENREFUSED = 2
XACTSTAT_PREPARING = 4
XACTSTAT_PREPARED = 8
XACTSTAT_PREPARERETAINING = 16
XACTSTAT_PREPARERETAINED = 32
XACTSTAT_COMMITTING = 64
XACTSTAT_COMMITRETAINING = 128
XACTSTAT_ABORTING = 256
XACTSTAT_ABORTED = 512
XACTSTAT_COMMITTED = 1024
XACTSTAT_HEURISTIC_ABORT = 2048
XACTSTAT_HEURISTIC_COMMIT = 4096
XACTSTAT_HEURISTIC_DAMAGE = 8192
XACTSTAT_HEURISTIC_DANGER = 16384
XACTSTAT_FORCED_ABORT = 32768
XACTSTAT_FORCED_COMMIT = 65536
XACTSTAT_INDOUBT = 131072
XACTSTAT_CLOSED = 262144
XACTSTAT_OPEN = 3
XACTSTAT_NOTPREPARED = 524227
XACTSTAT_ALL = 524287
def _define_XACTOPT_head():
    class XACTOPT(Structure):
        pass
    return XACTOPT
def _define_XACTOPT():
    XACTOPT = win32more.System.DistributedTransactionCoordinator.XACTOPT_head
    XACTOPT._fields_ = [
        ("ulTimeout", UInt32),
        ("szDescription", Byte * 40),
    ]
    return XACTOPT
def _define_ITransaction_head():
    class ITransaction(win32more.System.Com.IUnknown_head):
        Guid = Guid('0fb15084-af41-11ce-bd2b-204c4f4f5020')
    return ITransaction
def _define_ITransaction():
    ITransaction = win32more.System.DistributedTransactionCoordinator.ITransaction_head
    ITransaction.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(3, 'Commit', ((1, 'fRetaining'),(1, 'grfTC'),(1, 'grfRM'),)))
    ITransaction.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(4, 'Abort', ((1, 'pboidReason'),(1, 'fRetaining'),(1, 'fAsync'),)))
    ITransaction.GetTransactionInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.XACTTRANSINFO_head), use_last_error=False)(5, 'GetTransactionInfo', ((1, 'pinfo'),)))
    return ITransaction
def _define_ITransactionCloner_head():
    class ITransactionCloner(win32more.System.DistributedTransactionCoordinator.ITransaction_head):
        Guid = Guid('02656950-2152-11d0-944c-00a0c905416e')
    return ITransactionCloner
def _define_ITransactionCloner():
    ITransactionCloner = win32more.System.DistributedTransactionCoordinator.ITransactionCloner_head
    ITransactionCloner.CloneWithCommitDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(6, 'CloneWithCommitDisabled', ((1, 'ppITransaction'),)))
    return ITransactionCloner
def _define_ITransaction2_head():
    class ITransaction2(win32more.System.DistributedTransactionCoordinator.ITransactionCloner_head):
        Guid = Guid('34021548-0065-11d3-bac1-00c04f797be2')
    return ITransaction2
def _define_ITransaction2():
    ITransaction2 = win32more.System.DistributedTransactionCoordinator.ITransaction2_head
    ITransaction2.GetTransactionInfo2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.XACTTRANSINFO_head), use_last_error=False)(7, 'GetTransactionInfo2', ((1, 'pinfo'),)))
    return ITransaction2
def _define_ITransactionDispenser_head():
    class ITransactionDispenser(win32more.System.Com.IUnknown_head):
        Guid = Guid('3a6ad9e1-23b9-11cf-ad60-00aa00a74ccd')
    return ITransactionDispenser
def _define_ITransactionDispenser():
    ITransactionDispenser = win32more.System.DistributedTransactionCoordinator.ITransactionDispenser_head
    ITransactionDispenser.GetOptionsObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head), use_last_error=False)(3, 'GetOptionsObject', ((1, 'ppOptions'),)))
    ITransactionDispenser.BeginTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Int32,UInt32,win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(4, 'BeginTransaction', ((1, 'punkOuter'),(1, 'isoLevel'),(1, 'isoFlags'),(1, 'pOptions'),(1, 'ppTransaction'),)))
    return ITransactionDispenser
def _define_ITransactionOptions_head():
    class ITransactionOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('3a6ad9e0-23b9-11cf-ad60-00aa00a74ccd')
    return ITransactionOptions
def _define_ITransactionOptions():
    ITransactionOptions = win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head
    ITransactionOptions.SetOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.XACTOPT_head), use_last_error=False)(3, 'SetOptions', ((1, 'pOptions'),)))
    ITransactionOptions.GetOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.XACTOPT_head), use_last_error=False)(4, 'GetOptions', ((1, 'pOptions'),)))
    return ITransactionOptions
def _define_ITransactionOutcomeEvents_head():
    class ITransactionOutcomeEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('3a6ad9e2-23b9-11cf-ad60-00aa00a74ccd')
    return ITransactionOutcomeEvents
def _define_ITransactionOutcomeEvents():
    ITransactionOutcomeEvents = win32more.System.DistributedTransactionCoordinator.ITransactionOutcomeEvents_head
    ITransactionOutcomeEvents.Committed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.HRESULT, use_last_error=False)(3, 'Committed', ((1, 'fRetaining'),(1, 'pNewUOW'),(1, 'hr'),)))
    ITransactionOutcomeEvents.Aborted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.BOOL,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.HRESULT, use_last_error=False)(4, 'Aborted', ((1, 'pboidReason'),(1, 'fRetaining'),(1, 'pNewUOW'),(1, 'hr'),)))
    ITransactionOutcomeEvents.HeuristicDecision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.HRESULT, use_last_error=False)(5, 'HeuristicDecision', ((1, 'dwDecision'),(1, 'pboidReason'),(1, 'hr'),)))
    ITransactionOutcomeEvents.Indoubt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Indoubt', ()))
    return ITransactionOutcomeEvents
def _define_ITmNodeName_head():
    class ITmNodeName(win32more.System.Com.IUnknown_head):
        Guid = Guid('30274f88-6ee4-474e-9b95-7807bc9ef8cf')
    return ITmNodeName
def _define_ITmNodeName():
    ITmNodeName = win32more.System.DistributedTransactionCoordinator.ITmNodeName_head
    ITmNodeName.GetNodeNameSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetNodeNameSize', ((1, 'pcbNodeNameSize'),)))
    ITmNodeName.GetNodeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'GetNodeName', ((1, 'cbNodeNameBufferSize'),(1, 'pNodeNameBuffer'),)))
    return ITmNodeName
def _define_IKernelTransaction_head():
    class IKernelTransaction(win32more.System.Com.IUnknown_head):
        Guid = Guid('79427a2b-f895-40e0-be79-b57dc82ed231')
    return IKernelTransaction
def _define_IKernelTransaction():
    IKernelTransaction = win32more.System.DistributedTransactionCoordinator.IKernelTransaction_head
    IKernelTransaction.GetHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'GetHandle', ((1, 'pHandle'),)))
    return IKernelTransaction
def _define_ITransactionResourceAsync_head():
    class ITransactionResourceAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('69e971f0-23ce-11cf-ad60-00aa00a74ccd')
    return ITransactionResourceAsync
def _define_ITransactionResourceAsync():
    ITransactionResourceAsync = win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head
    ITransactionResourceAsync.PrepareRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(3, 'PrepareRequest', ((1, 'fRetaining'),(1, 'grfRM'),(1, 'fWantMoniker'),(1, 'fSinglePhase'),)))
    ITransactionResourceAsync.CommitRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(4, 'CommitRequest', ((1, 'grfRM'),(1, 'pNewUOW'),)))
    ITransactionResourceAsync.AbortRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.BOOL,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(5, 'AbortRequest', ((1, 'pboidReason'),(1, 'fRetaining'),(1, 'pNewUOW'),)))
    ITransactionResourceAsync.TMDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'TMDown', ()))
    return ITransactionResourceAsync
def _define_ITransactionLastResourceAsync_head():
    class ITransactionLastResourceAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('c82bd532-5b30-11d3-8a91-00c04f79eb6d')
    return ITransactionLastResourceAsync
def _define_ITransactionLastResourceAsync():
    ITransactionLastResourceAsync = win32more.System.DistributedTransactionCoordinator.ITransactionLastResourceAsync_head
    ITransactionLastResourceAsync.DelegateCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'DelegateCommit', ((1, 'grfRM'),)))
    ITransactionLastResourceAsync.ForgetRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(4, 'ForgetRequest', ((1, 'pNewUOW'),)))
    return ITransactionLastResourceAsync
def _define_ITransactionResource_head():
    class ITransactionResource(win32more.System.Com.IUnknown_head):
        Guid = Guid('ee5ff7b3-4572-11d0-9452-00a0c905416e')
    return ITransactionResource
def _define_ITransactionResource():
    ITransactionResource = win32more.System.DistributedTransactionCoordinator.ITransactionResource_head
    ITransactionResource.PrepareRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(3, 'PrepareRequest', ((1, 'fRetaining'),(1, 'grfRM'),(1, 'fWantMoniker'),(1, 'fSinglePhase'),)))
    ITransactionResource.CommitRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(4, 'CommitRequest', ((1, 'grfRM'),(1, 'pNewUOW'),)))
    ITransactionResource.AbortRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),win32more.Foundation.BOOL,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(5, 'AbortRequest', ((1, 'pboidReason'),(1, 'fRetaining'),(1, 'pNewUOW'),)))
    ITransactionResource.TMDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'TMDown', ()))
    return ITransactionResource
def _define_ITransactionEnlistmentAsync_head():
    class ITransactionEnlistmentAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('0fb15081-af41-11ce-bd2b-204c4f4f5020')
    return ITransactionEnlistmentAsync
def _define_ITransactionEnlistmentAsync():
    ITransactionEnlistmentAsync = win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head
    ITransactionEnlistmentAsync.PrepareRequestDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(3, 'PrepareRequestDone', ((1, 'hr'),(1, 'pmk'),(1, 'pboidReason'),)))
    ITransactionEnlistmentAsync.CommitRequestDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'CommitRequestDone', ((1, 'hr'),)))
    ITransactionEnlistmentAsync.AbortRequestDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(5, 'AbortRequestDone', ((1, 'hr'),)))
    return ITransactionEnlistmentAsync
def _define_ITransactionLastEnlistmentAsync_head():
    class ITransactionLastEnlistmentAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('c82bd533-5b30-11d3-8a91-00c04f79eb6d')
    return ITransactionLastEnlistmentAsync
def _define_ITransactionLastEnlistmentAsync():
    ITransactionLastEnlistmentAsync = win32more.System.DistributedTransactionCoordinator.ITransactionLastEnlistmentAsync_head
    ITransactionLastEnlistmentAsync.TransactionOutcome = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.XACTSTAT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(3, 'TransactionOutcome', ((1, 'XactStat'),(1, 'pboidReason'),)))
    return ITransactionLastEnlistmentAsync
def _define_ITransactionExportFactory_head():
    class ITransactionExportFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1cf9b53-8745-11ce-a9ba-00aa006c3706')
    return ITransactionExportFactory
def _define_ITransactionExportFactory():
    ITransactionExportFactory = win32more.System.DistributedTransactionCoordinator.ITransactionExportFactory_head
    ITransactionExportFactory.GetRemoteClassId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetRemoteClassId', ((1, 'pclsid'),)))
    ITransactionExportFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionExport_head), use_last_error=False)(4, 'Create', ((1, 'cbWhereabouts'),(1, 'rgbWhereabouts'),(1, 'ppExport'),)))
    return ITransactionExportFactory
def _define_ITransactionImportWhereabouts_head():
    class ITransactionImportWhereabouts(win32more.System.Com.IUnknown_head):
        Guid = Guid('0141fda4-8fc0-11ce-bd18-204c4f4f5020')
    return ITransactionImportWhereabouts
def _define_ITransactionImportWhereabouts():
    ITransactionImportWhereabouts = win32more.System.DistributedTransactionCoordinator.ITransactionImportWhereabouts_head
    ITransactionImportWhereabouts.GetWhereaboutsSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetWhereaboutsSize', ((1, 'pcbWhereabouts'),)))
    ITransactionImportWhereabouts.GetWhereabouts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(4, 'GetWhereabouts', ((1, 'cbWhereabouts'),(1, 'rgbWhereabouts'),(1, 'pcbUsed'),)))
    return ITransactionImportWhereabouts
def _define_ITransactionExport_head():
    class ITransactionExport(win32more.System.Com.IUnknown_head):
        Guid = Guid('0141fda5-8fc0-11ce-bd18-204c4f4f5020')
    return ITransactionExport
def _define_ITransactionExport():
    ITransactionExport = win32more.System.DistributedTransactionCoordinator.ITransactionExport_head
    ITransactionExport.Export = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(3, 'Export', ((1, 'punkTransaction'),(1, 'pcbTransactionCookie'),)))
    ITransactionExport.GetTransactionCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(4, 'GetTransactionCookie', ((1, 'punkTransaction'),(1, 'cbTransactionCookie'),(1, 'rgbTransactionCookie'),(1, 'pcbUsed'),)))
    return ITransactionExport
def _define_ITransactionImport_head():
    class ITransactionImport(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1cf9b5a-8745-11ce-a9ba-00aa006c3706')
    return ITransactionImport
def _define_ITransactionImport():
    ITransactionImport = win32more.System.DistributedTransactionCoordinator.ITransactionImport_head
    ITransactionImport.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'Import', ((1, 'cbTransactionCookie'),(1, 'rgbTransactionCookie'),(1, 'piid'),(1, 'ppvTransaction'),)))
    return ITransactionImport
def _define_ITipTransaction_head():
    class ITipTransaction(win32more.System.Com.IUnknown_head):
        Guid = Guid('17cf72d0-bac5-11d1-b1bf-00c04fc2f3ef')
    return ITipTransaction
def _define_ITipTransaction():
    ITipTransaction = win32more.System.DistributedTransactionCoordinator.ITipTransaction_head
    ITipTransaction.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.Foundation.PSTR), use_last_error=False)(3, 'Push', ((1, 'i_pszRemoteTmUrl'),(1, 'o_ppszRemoteTxUrl'),)))
    ITipTransaction.GetTransactionUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSTR), use_last_error=False)(4, 'GetTransactionUrl', ((1, 'o_ppszLocalTxUrl'),)))
    return ITipTransaction
def _define_ITipHelper_head():
    class ITipHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('17cf72d1-bac5-11d1-b1bf-00c04fc2f3ef')
    return ITipHelper
def _define_ITipHelper():
    ITipHelper = win32more.System.DistributedTransactionCoordinator.ITipHelper_head
    ITipHelper.Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(3, 'Pull', ((1, 'i_pszTxUrl'),(1, 'o_ppITransaction'),)))
    ITipHelper.PullAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,win32more.System.DistributedTransactionCoordinator.ITipPullSink_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(4, 'PullAsync', ((1, 'i_pszTxUrl'),(1, 'i_pTipPullSink'),(1, 'o_ppITransaction'),)))
    ITipHelper.GetLocalTmUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no), use_last_error=False)(5, 'GetLocalTmUrl', ((1, 'o_ppszLocalTmUrl'),)))
    return ITipHelper
def _define_ITipPullSink_head():
    class ITipPullSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('17cf72d2-bac5-11d1-b1bf-00c04fc2f3ef')
    return ITipPullSink
def _define_ITipPullSink():
    ITipPullSink = win32more.System.DistributedTransactionCoordinator.ITipPullSink_head
    ITipPullSink.PullComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'PullComplete', ((1, 'i_hrPull'),)))
    return ITipPullSink
def _define_IDtcNetworkAccessConfig_head():
    class IDtcNetworkAccessConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('9797c15d-a428-4291-87b6-0995031a678d')
    return IDtcNetworkAccessConfig
def _define_IDtcNetworkAccessConfig():
    IDtcNetworkAccessConfig = win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig_head
    IDtcNetworkAccessConfig.GetAnyNetworkAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetAnyNetworkAccess', ((1, 'pbAnyNetworkAccess'),)))
    IDtcNetworkAccessConfig.SetAnyNetworkAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetAnyNetworkAccess', ((1, 'bAnyNetworkAccess'),)))
    IDtcNetworkAccessConfig.GetNetworkAdministrationAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetNetworkAdministrationAccess', ((1, 'pbNetworkAdministrationAccess'),)))
    IDtcNetworkAccessConfig.SetNetworkAdministrationAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'SetNetworkAdministrationAccess', ((1, 'bNetworkAdministrationAccess'),)))
    IDtcNetworkAccessConfig.GetNetworkTransactionAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'GetNetworkTransactionAccess', ((1, 'pbNetworkTransactionAccess'),)))
    IDtcNetworkAccessConfig.SetNetworkTransactionAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(8, 'SetNetworkTransactionAccess', ((1, 'bNetworkTransactionAccess'),)))
    IDtcNetworkAccessConfig.GetNetworkClientAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'GetNetworkClientAccess', ((1, 'pbNetworkClientAccess'),)))
    IDtcNetworkAccessConfig.SetNetworkClientAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'SetNetworkClientAccess', ((1, 'bNetworkClientAccess'),)))
    IDtcNetworkAccessConfig.GetNetworkTIPAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'GetNetworkTIPAccess', ((1, 'pbNetworkTIPAccess'),)))
    IDtcNetworkAccessConfig.SetNetworkTIPAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(12, 'SetNetworkTIPAccess', ((1, 'bNetworkTIPAccess'),)))
    IDtcNetworkAccessConfig.GetXAAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetXAAccess', ((1, 'pbXAAccess'),)))
    IDtcNetworkAccessConfig.SetXAAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(14, 'SetXAAccess', ((1, 'bXAAccess'),)))
    IDtcNetworkAccessConfig.RestartDtcService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'RestartDtcService', ()))
    return IDtcNetworkAccessConfig
AUTHENTICATION_LEVEL = Int32
NO_AUTHENTICATION_REQUIRED = 0
INCOMING_AUTHENTICATION_REQUIRED = 1
MUTUAL_AUTHENTICATION_REQUIRED = 2
def _define_IDtcNetworkAccessConfig2_head():
    class IDtcNetworkAccessConfig2(win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig_head):
        Guid = Guid('a7aa013b-eb7d-4f42-b41c-b2dec09ae034')
    return IDtcNetworkAccessConfig2
def _define_IDtcNetworkAccessConfig2():
    IDtcNetworkAccessConfig2 = win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig2_head
    IDtcNetworkAccessConfig2.GetNetworkInboundAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'GetNetworkInboundAccess', ((1, 'pbInbound'),)))
    IDtcNetworkAccessConfig2.GetNetworkOutboundAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'GetNetworkOutboundAccess', ((1, 'pbOutbound'),)))
    IDtcNetworkAccessConfig2.SetNetworkInboundAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(18, 'SetNetworkInboundAccess', ((1, 'bInbound'),)))
    IDtcNetworkAccessConfig2.SetNetworkOutboundAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(19, 'SetNetworkOutboundAccess', ((1, 'bOutbound'),)))
    IDtcNetworkAccessConfig2.GetAuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL), use_last_error=False)(20, 'GetAuthenticationLevel', ((1, 'pAuthLevel'),)))
    IDtcNetworkAccessConfig2.SetAuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.AUTHENTICATION_LEVEL, use_last_error=False)(21, 'SetAuthenticationLevel', ((1, 'AuthLevel'),)))
    return IDtcNetworkAccessConfig2
def _define_IDtcNetworkAccessConfig3_head():
    class IDtcNetworkAccessConfig3(win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig2_head):
        Guid = Guid('76e4b4f3-2ca5-466b-89d5-fd218ee75b49')
    return IDtcNetworkAccessConfig3
def _define_IDtcNetworkAccessConfig3():
    IDtcNetworkAccessConfig3 = win32more.System.DistributedTransactionCoordinator.IDtcNetworkAccessConfig3_head
    IDtcNetworkAccessConfig3.GetLUAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(22, 'GetLUAccess', ((1, 'pbLUAccess'),)))
    IDtcNetworkAccessConfig3.SetLUAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(23, 'SetLUAccess', ((1, 'bLUAccess'),)))
    return IDtcNetworkAccessConfig3
def _define_xid_t_head():
    class xid_t(Structure):
        pass
    return xid_t
def _define_xid_t():
    xid_t = win32more.System.DistributedTransactionCoordinator.xid_t_head
    xid_t._fields_ = [
        ("formatID", Int32),
        ("gtrid_length", Int32),
        ("bqual_length", Int32),
        ("data", win32more.Foundation.CHAR * 128),
    ]
    return xid_t
def _define_xa_switch_t_head():
    class xa_switch_t(Structure):
        pass
    return xa_switch_t
def _define_xa_switch_t():
    xa_switch_t = win32more.System.DistributedTransactionCoordinator.xa_switch_t_head
    xa_switch_t._fields_ = [
        ("name", win32more.Foundation.CHAR * 32),
        ("flags", Int32),
        ("version", Int32),
        ("xa_open_entry", IntPtr),
        ("xa_close_entry", IntPtr),
        ("xa_start_entry", IntPtr),
        ("xa_end_entry", IntPtr),
        ("xa_rollback_entry", IntPtr),
        ("xa_prepare_entry", IntPtr),
        ("xa_commit_entry", IntPtr),
        ("xa_recover_entry", IntPtr),
        ("xa_forget_entry", IntPtr),
        ("xa_complete_entry", IntPtr),
    ]
    return xa_switch_t
def _define_XA_OPEN_EPT():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32,Int32, use_last_error=False)
def _define_XA_CLOSE_EPT():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32,Int32, use_last_error=False)
def _define_XA_START_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_END_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_ROLLBACK_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_PREPARE_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_COMMIT_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_RECOVER_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32,Int32, use_last_error=False)
def _define_XA_FORGET_EPT():
    return CFUNCTYPE(Int32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),Int32,Int32, use_last_error=False)
def _define_XA_COMPLETE_EPT():
    return CFUNCTYPE(Int32,POINTER(Int32),POINTER(Int32),Int32,Int32, use_last_error=False)
def _define_IDtcToXaMapper_head():
    class IDtcToXaMapper(win32more.System.Com.IUnknown_head):
        Guid = Guid('64ffabe0-7ce9-11d0-8ce6-00c04fdc877e')
    return IDtcToXaMapper
def _define_IDtcToXaMapper():
    IDtcToXaMapper = win32more.System.DistributedTransactionCoordinator.IDtcToXaMapper_head
    IDtcToXaMapper.RequestNewResourceManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(3, 'RequestNewResourceManager', ((1, 'pszDSN'),(1, 'pszClientDllName'),(1, 'pdwRMCookie'),)))
    IDtcToXaMapper.TranslateTridToXid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head), use_last_error=False)(4, 'TranslateTridToXid', ((1, 'pdwITransaction'),(1, 'dwRMCookie'),(1, 'pXid'),)))
    IDtcToXaMapper.EnlistResourceManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'EnlistResourceManager', ((1, 'dwRMCookie'),(1, 'pdwITransaction'),)))
    IDtcToXaMapper.ReleaseResourceManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'ReleaseResourceManager', ((1, 'dwRMCookie'),)))
    return IDtcToXaMapper
def _define_IDtcToXaHelperFactory_head():
    class IDtcToXaHelperFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9861610-304a-11d1-9813-00a0c905416e')
    return IDtcToXaHelperFactory
def _define_IDtcToXaHelperFactory():
    IDtcToXaHelperFactory = win32more.System.DistributedTransactionCoordinator.IDtcToXaHelperFactory_head
    IDtcToXaHelperFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),POINTER(win32more.System.DistributedTransactionCoordinator.IDtcToXaHelper_head), use_last_error=False)(3, 'Create', ((1, 'pszDSN'),(1, 'pszClientDllName'),(1, 'pguidRm'),(1, 'ppXaHelper'),)))
    return IDtcToXaHelperFactory
def _define_IDtcToXaHelper_head():
    class IDtcToXaHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9861611-304a-11d1-9813-00a0c905416e')
    return IDtcToXaHelper
def _define_IDtcToXaHelper():
    IDtcToXaHelper = win32more.System.DistributedTransactionCoordinator.IDtcToXaHelper_head
    IDtcToXaHelper.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'Close', ((1, 'i_fDoRecovery'),)))
    IDtcToXaHelper.TranslateTridToXid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head,POINTER(Guid),POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head), use_last_error=False)(4, 'TranslateTridToXid', ((1, 'pITransaction'),(1, 'pguidBqual'),(1, 'pXid'),)))
    return IDtcToXaHelper
def _define_IDtcToXaHelperSinglePipe_head():
    class IDtcToXaHelperSinglePipe(win32more.System.Com.IUnknown_head):
        Guid = Guid('47ed4971-53b3-11d1-bbb9-00c04fd658f6')
    return IDtcToXaHelperSinglePipe
def _define_IDtcToXaHelperSinglePipe():
    IDtcToXaHelperSinglePipe = win32more.System.DistributedTransactionCoordinator.IDtcToXaHelperSinglePipe_head
    IDtcToXaHelperSinglePipe.XARMCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(3, 'XARMCreate', ((1, 'pszDSN'),(1, 'pszClientDll'),(1, 'pdwRMCookie'),)))
    IDtcToXaHelperSinglePipe.ConvertTridToXID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head), use_last_error=False)(4, 'ConvertTridToXID', ((1, 'pdwITrans'),(1, 'dwRMCookie'),(1, 'pxid'),)))
    IDtcToXaHelperSinglePipe.EnlistWithRM = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.DistributedTransactionCoordinator.ITransaction_head,win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head), use_last_error=False)(5, 'EnlistWithRM', ((1, 'dwRMCookie'),(1, 'i_pITransaction'),(1, 'i_pITransRes'),(1, 'o_ppITransEnslitment'),)))
    IDtcToXaHelperSinglePipe.ReleaseRMCookie = COMMETHOD(WINFUNCTYPE(Void,UInt32,win32more.Foundation.BOOL, use_last_error=False)(6, 'ReleaseRMCookie', ((1, 'i_dwRMCookie'),(1, 'i_fNormal'),)))
    return IDtcToXaHelperSinglePipe
APPLICATIONTYPE = Int32
LOCAL_APPLICATIONTYPE = 0
CLUSTERRESOURCE_APPLICATIONTYPE = 1
def _define_OLE_TM_CONFIG_PARAMS_V1_head():
    class OLE_TM_CONFIG_PARAMS_V1(Structure):
        pass
    return OLE_TM_CONFIG_PARAMS_V1
def _define_OLE_TM_CONFIG_PARAMS_V1():
    OLE_TM_CONFIG_PARAMS_V1 = win32more.System.DistributedTransactionCoordinator.OLE_TM_CONFIG_PARAMS_V1_head
    OLE_TM_CONFIG_PARAMS_V1._fields_ = [
        ("dwVersion", UInt32),
        ("dwcConcurrencyHint", UInt32),
    ]
    return OLE_TM_CONFIG_PARAMS_V1
def _define_OLE_TM_CONFIG_PARAMS_V2_head():
    class OLE_TM_CONFIG_PARAMS_V2(Structure):
        pass
    return OLE_TM_CONFIG_PARAMS_V2
def _define_OLE_TM_CONFIG_PARAMS_V2():
    OLE_TM_CONFIG_PARAMS_V2 = win32more.System.DistributedTransactionCoordinator.OLE_TM_CONFIG_PARAMS_V2_head
    OLE_TM_CONFIG_PARAMS_V2._fields_ = [
        ("dwVersion", UInt32),
        ("dwcConcurrencyHint", UInt32),
        ("applicationType", win32more.System.DistributedTransactionCoordinator.APPLICATIONTYPE),
        ("clusterResourceId", Guid),
    ]
    return OLE_TM_CONFIG_PARAMS_V2
XACT_DTC_CONSTANTS = Int32
XACT_E_CONNECTION_REQUEST_DENIED = -2147168000
XACT_E_TOOMANY_ENLISTMENTS = -2147167999
XACT_E_DUPLICATE_GUID = -2147167998
XACT_E_NOTSINGLEPHASE = -2147167997
XACT_E_RECOVERYALREADYDONE = -2147167996
XACT_E_PROTOCOL = -2147167995
XACT_E_RM_FAILURE = -2147167994
XACT_E_RECOVERY_FAILED = -2147167993
XACT_E_LU_NOT_FOUND = -2147167992
XACT_E_DUPLICATE_LU = -2147167991
XACT_E_LU_NOT_CONNECTED = -2147167990
XACT_E_DUPLICATE_TRANSID = -2147167989
XACT_E_LU_BUSY = -2147167988
XACT_E_LU_NO_RECOVERY_PROCESS = -2147167987
XACT_E_LU_DOWN = -2147167986
XACT_E_LU_RECOVERING = -2147167985
XACT_E_LU_RECOVERY_MISMATCH = -2147167984
XACT_E_RM_UNAVAILABLE = -2147167983
XACT_E_LRMRECOVERYALREADYDONE = -2147167982
XACT_E_NOLASTRESOURCEINTERFACE = -2147167981
XACT_S_NONOTIFY = 315648
XACT_OK_NONOTIFY = 315649
dwUSER_MS_SQLSERVER = 65535
def _define_IXATransLookup_head():
    class IXATransLookup(win32more.System.Com.IUnknown_head):
        Guid = Guid('f3b1f131-eeda-11ce-aed4-00aa0051e2c4')
    return IXATransLookup
def _define_IXATransLookup():
    IXATransLookup = win32more.System.DistributedTransactionCoordinator.IXATransLookup_head
    IXATransLookup.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(3, 'Lookup', ((1, 'ppTransaction'),)))
    return IXATransLookup
def _define_IXATransLookup2_head():
    class IXATransLookup2(win32more.System.Com.IUnknown_head):
        Guid = Guid('bf193c85-0d1a-4290-b88f-d2cb8873d1e7')
    return IXATransLookup2
def _define_IXATransLookup2():
    IXATransLookup2 = win32more.System.DistributedTransactionCoordinator.IXATransLookup2_head
    IXATransLookup2.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(3, 'Lookup', ((1, 'pXID'),(1, 'ppTransaction'),)))
    return IXATransLookup2
def _define_IResourceManagerSink_head():
    class IResourceManagerSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d563181-defb-11ce-aed1-00aa0051e2c4')
    return IResourceManagerSink
def _define_IResourceManagerSink():
    IResourceManagerSink = win32more.System.DistributedTransactionCoordinator.IResourceManagerSink_head
    IResourceManagerSink.TMDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'TMDown', ()))
    return IResourceManagerSink
def _define_IResourceManager_head():
    class IResourceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('13741d21-87eb-11ce-8081-0080c758527e')
    return IResourceManager
def _define_IResourceManager():
    IResourceManager = win32more.System.DistributedTransactionCoordinator.IResourceManager_head
    IResourceManager.Enlist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head,win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),POINTER(Int32),POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head), use_last_error=False)(3, 'Enlist', ((1, 'pTransaction'),(1, 'pRes'),(1, 'pUOW'),(1, 'pisoLevel'),(1, 'ppEnlist'),)))
    IResourceManager.Reenlist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT), use_last_error=False)(4, 'Reenlist', ((1, 'pPrepInfo'),(1, 'cbPrepInfo'),(1, 'lTimeout'),(1, 'pXactStat'),)))
    IResourceManager.ReenlistmentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ReenlistmentComplete', ()))
    IResourceManager.GetDistributedTransactionManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetDistributedTransactionManager', ((1, 'iid'),(1, 'ppvObject'),)))
    return IResourceManager
def _define_ILastResourceManager_head():
    class ILastResourceManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('4d964ad4-5b33-11d3-8a91-00c04f79eb6d')
    return ILastResourceManager
def _define_ILastResourceManager():
    ILastResourceManager = win32more.System.DistributedTransactionCoordinator.ILastResourceManager_head
    ILastResourceManager.TransactionCommitted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'TransactionCommitted', ((1, 'pPrepInfo'),(1, 'cbPrepInfo'),)))
    ILastResourceManager.RecoveryDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'RecoveryDone', ()))
    return ILastResourceManager
def _define_IResourceManager2_head():
    class IResourceManager2(win32more.System.DistributedTransactionCoordinator.IResourceManager_head):
        Guid = Guid('d136c69a-f749-11d1-8f47-00c04f8ee57d')
    return IResourceManager2
def _define_IResourceManager2():
    IResourceManager2 = win32more.System.DistributedTransactionCoordinator.IResourceManager2_head
    IResourceManager2.Enlist2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head,win32more.System.DistributedTransactionCoordinator.ITransactionResourceAsync_head,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head),POINTER(Int32),POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionEnlistmentAsync_head), use_last_error=False)(7, 'Enlist2', ((1, 'pTransaction'),(1, 'pResAsync'),(1, 'pUOW'),(1, 'pisoLevel'),(1, 'pXid'),(1, 'ppEnlist'),)))
    IResourceManager2.Reenlist2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.xid_t_head),UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT), use_last_error=False)(8, 'Reenlist2', ((1, 'pXid'),(1, 'dwTimeout'),(1, 'pXactStat'),)))
    return IResourceManager2
def _define_IResourceManagerRejoinable_head():
    class IResourceManagerRejoinable(win32more.System.DistributedTransactionCoordinator.IResourceManager2_head):
        Guid = Guid('6f6de620-b5df-4f3e-9cfa-c8aebd05172b')
    return IResourceManagerRejoinable
def _define_IResourceManagerRejoinable():
    IResourceManagerRejoinable = win32more.System.DistributedTransactionCoordinator.IResourceManagerRejoinable_head
    IResourceManagerRejoinable.Rejoin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.XACTSTAT), use_last_error=False)(9, 'Rejoin', ((1, 'pPrepInfo'),(1, 'cbPrepInfo'),(1, 'lTimeout'),(1, 'pXactStat'),)))
    return IResourceManagerRejoinable
def _define_IXAConfig_head():
    class IXAConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8a6e3a1-9a8c-11cf-a308-00a0c905416e')
    return IXAConfig
def _define_IXAConfig():
    IXAConfig = win32more.System.DistributedTransactionCoordinator.IXAConfig_head
    IXAConfig.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(3, 'Initialize', ((1, 'clsidHelperDll'),)))
    IXAConfig.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Terminate', ()))
    return IXAConfig
def _define_IRMHelper_head():
    class IRMHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('e793f6d1-f53d-11cf-a60d-00a0c905416e')
    return IRMHelper
def _define_IRMHelper():
    IRMHelper = win32more.System.DistributedTransactionCoordinator.IRMHelper_head
    IRMHelper.RMCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'RMCount', ((1, 'dwcTotalNumberOfRMs'),)))
    IRMHelper.RMInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.xa_switch_t_head),win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Guid, use_last_error=False)(4, 'RMInfo', ((1, 'pXa_Switch'),(1, 'fCDeclCallingConv'),(1, 'pszOpenString'),(1, 'pszCloseString'),(1, 'guidRMRecovery'),)))
    return IRMHelper
def _define_IXAObtainRMInfo_head():
    class IXAObtainRMInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('e793f6d2-f53d-11cf-a60d-00a0c905416e')
    return IXAObtainRMInfo
def _define_IXAObtainRMInfo():
    IXAObtainRMInfo = win32more.System.DistributedTransactionCoordinator.IXAObtainRMInfo_head
    IXAObtainRMInfo.ObtainRMInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.IRMHelper_head, use_last_error=False)(3, 'ObtainRMInfo', ((1, 'pIRMHelper'),)))
    return IXAObtainRMInfo
def _define_IResourceManagerFactory_head():
    class IResourceManagerFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('13741d20-87eb-11ce-8081-0080c758527e')
    return IResourceManagerFactory
def _define_IResourceManagerFactory():
    IResourceManagerFactory = win32more.System.DistributedTransactionCoordinator.IResourceManagerFactory_head
    IResourceManagerFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PSTR,win32more.System.DistributedTransactionCoordinator.IResourceManagerSink_head,POINTER(win32more.System.DistributedTransactionCoordinator.IResourceManager_head), use_last_error=False)(3, 'Create', ((1, 'pguidRM'),(1, 'pszRMName'),(1, 'pIResMgrSink'),(1, 'ppResMgr'),)))
    return IResourceManagerFactory
def _define_IResourceManagerFactory2_head():
    class IResourceManagerFactory2(win32more.System.DistributedTransactionCoordinator.IResourceManagerFactory_head):
        Guid = Guid('6b369c21-fbd2-11d1-8f47-00c04f8ee57d')
    return IResourceManagerFactory2
def _define_IResourceManagerFactory2():
    IResourceManagerFactory2 = win32more.System.DistributedTransactionCoordinator.IResourceManagerFactory2_head
    IResourceManagerFactory2.CreateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PSTR,win32more.System.DistributedTransactionCoordinator.IResourceManagerSink_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'CreateEx', ((1, 'pguidRM'),(1, 'pszRMName'),(1, 'pIResMgrSink'),(1, 'riidRequested'),(1, 'ppvResMgr'),)))
    return IResourceManagerFactory2
def _define_IPrepareInfo_head():
    class IPrepareInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('80c7bfd0-87ee-11ce-8081-0080c758527e')
    return IPrepareInfo
def _define_IPrepareInfo():
    IPrepareInfo = win32more.System.DistributedTransactionCoordinator.IPrepareInfo_head
    IPrepareInfo.GetPrepareInfoSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPrepareInfoSize', ((1, 'pcbPrepInfo'),)))
    IPrepareInfo.GetPrepareInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(4, 'GetPrepareInfo', ((1, 'pPrepInfo'),)))
    return IPrepareInfo
def _define_IPrepareInfo2_head():
    class IPrepareInfo2(win32more.System.Com.IUnknown_head):
        Guid = Guid('5fab2547-9779-11d1-b886-00c04fb9618a')
    return IPrepareInfo2
def _define_IPrepareInfo2():
    IPrepareInfo2 = win32more.System.DistributedTransactionCoordinator.IPrepareInfo2_head
    IPrepareInfo2.GetPrepareInfoSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetPrepareInfoSize', ((1, 'pcbPrepInfo'),)))
    IPrepareInfo2.GetPrepareInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte), use_last_error=False)(4, 'GetPrepareInfo', ((1, 'cbPrepareInfo'),(1, 'pPrepInfo'),)))
    return IPrepareInfo2
def _define_IGetDispenser_head():
    class IGetDispenser(win32more.System.Com.IUnknown_head):
        Guid = Guid('c23cc370-87ef-11ce-8081-0080c758527e')
    return IGetDispenser
def _define_IGetDispenser():
    IGetDispenser = win32more.System.DistributedTransactionCoordinator.IGetDispenser_head
    IGetDispenser.GetDispenser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetDispenser', ((1, 'iid'),(1, 'ppvObject'),)))
    return IGetDispenser
def _define_ITransactionVoterBallotAsync2_head():
    class ITransactionVoterBallotAsync2(win32more.System.Com.IUnknown_head):
        Guid = Guid('5433376c-414d-11d3-b206-00c04fc2f3ef')
    return ITransactionVoterBallotAsync2
def _define_ITransactionVoterBallotAsync2():
    ITransactionVoterBallotAsync2 = win32more.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head
    ITransactionVoterBallotAsync2.VoteRequestDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.BOID_head), use_last_error=False)(3, 'VoteRequestDone', ((1, 'hr'),(1, 'pboidReason'),)))
    return ITransactionVoterBallotAsync2
def _define_ITransactionVoterNotifyAsync2_head():
    class ITransactionVoterNotifyAsync2(win32more.System.DistributedTransactionCoordinator.ITransactionOutcomeEvents_head):
        Guid = Guid('5433376b-414d-11d3-b206-00c04fc2f3ef')
    return ITransactionVoterNotifyAsync2
def _define_ITransactionVoterNotifyAsync2():
    ITransactionVoterNotifyAsync2 = win32more.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head
    ITransactionVoterNotifyAsync2.VoteRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'VoteRequest', ()))
    return ITransactionVoterNotifyAsync2
def _define_ITransactionVoterFactory2_head():
    class ITransactionVoterFactory2(win32more.System.Com.IUnknown_head):
        Guid = Guid('5433376a-414d-11d3-b206-00c04fc2f3ef')
    return ITransactionVoterFactory2
def _define_ITransactionVoterFactory2():
    ITransactionVoterFactory2 = win32more.System.DistributedTransactionCoordinator.ITransactionVoterFactory2_head
    ITransactionVoterFactory2.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head,win32more.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head), use_last_error=False)(3, 'Create', ((1, 'pTransaction'),(1, 'pVoterNotify'),(1, 'ppVoterBallot'),)))
    return ITransactionVoterFactory2
def _define_ITransactionPhase0EnlistmentAsync_head():
    class ITransactionPhase0EnlistmentAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('82dc88e1-a954-11d1-8f88-00600895e7d5')
    return ITransactionPhase0EnlistmentAsync
def _define_ITransactionPhase0EnlistmentAsync():
    ITransactionPhase0EnlistmentAsync = win32more.System.DistributedTransactionCoordinator.ITransactionPhase0EnlistmentAsync_head
    ITransactionPhase0EnlistmentAsync.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Enable', ()))
    ITransactionPhase0EnlistmentAsync.WaitForEnlistment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'WaitForEnlistment', ()))
    ITransactionPhase0EnlistmentAsync.Phase0Done = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Phase0Done', ()))
    ITransactionPhase0EnlistmentAsync.Unenlist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Unenlist', ()))
    ITransactionPhase0EnlistmentAsync.GetTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(7, 'GetTransaction', ((1, 'ppITransaction'),)))
    return ITransactionPhase0EnlistmentAsync
def _define_ITransactionPhase0NotifyAsync_head():
    class ITransactionPhase0NotifyAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('ef081809-0c76-11d2-87a6-00c04f990f34')
    return ITransactionPhase0NotifyAsync
def _define_ITransactionPhase0NotifyAsync():
    ITransactionPhase0NotifyAsync = win32more.System.DistributedTransactionCoordinator.ITransactionPhase0NotifyAsync_head
    ITransactionPhase0NotifyAsync.Phase0Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'Phase0Request', ((1, 'fAbortingHint'),)))
    ITransactionPhase0NotifyAsync.EnlistCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'EnlistCompleted', ((1, 'status'),)))
    return ITransactionPhase0NotifyAsync
def _define_ITransactionPhase0Factory_head():
    class ITransactionPhase0Factory(win32more.System.Com.IUnknown_head):
        Guid = Guid('82dc88e0-a954-11d1-8f88-00600895e7d5')
    return ITransactionPhase0Factory
def _define_ITransactionPhase0Factory():
    ITransactionPhase0Factory = win32more.System.DistributedTransactionCoordinator.ITransactionPhase0Factory_head
    ITransactionPhase0Factory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransactionPhase0NotifyAsync_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionPhase0EnlistmentAsync_head), use_last_error=False)(3, 'Create', ((1, 'pPhase0Notify'),(1, 'ppPhase0Enlistment'),)))
    return ITransactionPhase0Factory
def _define_ITransactionTransmitter_head():
    class ITransactionTransmitter(win32more.System.Com.IUnknown_head):
        Guid = Guid('59313e01-b36c-11cf-a539-00aa006887c3')
    return ITransactionTransmitter
def _define_ITransactionTransmitter():
    ITransactionTransmitter = win32more.System.DistributedTransactionCoordinator.ITransactionTransmitter_head
    ITransactionTransmitter.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head, use_last_error=False)(3, 'Set', ((1, 'pTransaction'),)))
    ITransactionTransmitter.GetPropagationTokenSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetPropagationTokenSize', ((1, 'pcbToken'),)))
    ITransactionTransmitter.MarshalPropagationToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'MarshalPropagationToken', ((1, 'cbToken'),(1, 'rgbToken'),(1, 'pcbUsed'),)))
    ITransactionTransmitter.UnmarshalReturnToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte), use_last_error=False)(6, 'UnmarshalReturnToken', ((1, 'cbReturnToken'),(1, 'rgbReturnToken'),)))
    ITransactionTransmitter.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    return ITransactionTransmitter
def _define_ITransactionTransmitterFactory_head():
    class ITransactionTransmitterFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('59313e00-b36c-11cf-a539-00aa006887c3')
    return ITransactionTransmitterFactory
def _define_ITransactionTransmitterFactory():
    ITransactionTransmitterFactory = win32more.System.DistributedTransactionCoordinator.ITransactionTransmitterFactory_head
    ITransactionTransmitterFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionTransmitter_head), use_last_error=False)(3, 'Create', ((1, 'ppTransmitter'),)))
    return ITransactionTransmitterFactory
def _define_ITransactionReceiver_head():
    class ITransactionReceiver(win32more.System.Com.IUnknown_head):
        Guid = Guid('59313e03-b36c-11cf-a539-00aa006887c3')
    return ITransactionReceiver
def _define_ITransactionReceiver():
    ITransactionReceiver = win32more.System.DistributedTransactionCoordinator.ITransactionReceiver_head
    ITransactionReceiver.UnmarshalPropagationToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(3, 'UnmarshalPropagationToken', ((1, 'cbToken'),(1, 'rgbToken'),(1, 'ppTransaction'),)))
    ITransactionReceiver.GetReturnTokenSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetReturnTokenSize', ((1, 'pcbReturnToken'),)))
    ITransactionReceiver.MarshalReturnToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'MarshalReturnToken', ((1, 'cbReturnToken'),(1, 'rgbReturnToken'),(1, 'pcbUsed'),)))
    ITransactionReceiver.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Reset', ()))
    return ITransactionReceiver
def _define_ITransactionReceiverFactory_head():
    class ITransactionReceiverFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('59313e02-b36c-11cf-a539-00aa006887c3')
    return ITransactionReceiverFactory
def _define_ITransactionReceiverFactory():
    ITransactionReceiverFactory = win32more.System.DistributedTransactionCoordinator.ITransactionReceiverFactory_head
    ITransactionReceiverFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionReceiver_head), use_last_error=False)(3, 'Create', ((1, 'ppReceiver'),)))
    return ITransactionReceiverFactory
def _define__ProxyConfigParams_head():
    class _ProxyConfigParams(Structure):
        pass
    return _ProxyConfigParams
def _define__ProxyConfigParams():
    _ProxyConfigParams = win32more.System.DistributedTransactionCoordinator._ProxyConfigParams_head
    _ProxyConfigParams._fields_ = [
        ("wcThreadsMax", UInt16),
    ]
    return _ProxyConfigParams
def _define_IDtcLuConfigure_head():
    class IDtcLuConfigure(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e760-1aea-11d0-944b-00a0c905416e')
    return IDtcLuConfigure
def _define_IDtcLuConfigure():
    IDtcLuConfigure = win32more.System.DistributedTransactionCoordinator.IDtcLuConfigure_head
    IDtcLuConfigure.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'Add', ((1, 'pucLuPair'),(1, 'cbLuPair'),)))
    IDtcLuConfigure.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(4, 'Delete', ((1, 'pucLuPair'),(1, 'cbLuPair'),)))
    return IDtcLuConfigure
def _define_IDtcLuRecovery_head():
    class IDtcLuRecovery(win32more.System.Com.IUnknown_head):
        Guid = Guid('ac2b8ad2-d6f0-11d0-b386-00a0c9083365')
    return IDtcLuRecovery
def _define_IDtcLuRecovery():
    IDtcLuRecovery = win32more.System.DistributedTransactionCoordinator.IDtcLuRecovery_head
    return IDtcLuRecovery
def _define_IDtcLuRecoveryFactory_head():
    class IDtcLuRecoveryFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e762-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRecoveryFactory
def _define_IDtcLuRecoveryFactory():
    IDtcLuRecoveryFactory = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryFactory_head
    IDtcLuRecoveryFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRecovery_head), use_last_error=False)(3, 'Create', ((1, 'pucLuPair'),(1, 'cbLuPair'),(1, 'ppRecovery'),)))
    return IDtcLuRecoveryFactory
_DtcLu_LocalRecovery_Work = Int32
DTCINITIATEDRECOVERYWORK_CHECKLUSTATUS = 1
DTCINITIATEDRECOVERYWORK_TRANS = 2
DTCINITIATEDRECOVERYWORK_TMDOWN = 3
_DtcLu_Xln = Int32
DTCLUXLN_COLD = 1
DTCLUXLN_WARM = 2
_DtcLu_Xln_Confirmation = Int32
DTCLUXLNCONFIRMATION_CONFIRM = 1
DTCLUXLNCONFIRMATION_LOGNAMEMISMATCH = 2
DTCLUXLNCONFIRMATION_COLDWARMMISMATCH = 3
DTCLUXLNCONFIRMATION_OBSOLETE = 4
_DtcLu_Xln_Response = Int32
DTCLUXLNRESPONSE_OK_SENDOURXLNBACK = 1
DTCLUXLNRESPONSE_OK_SENDCONFIRMATION = 2
DTCLUXLNRESPONSE_LOGNAMEMISMATCH = 3
DTCLUXLNRESPONSE_COLDWARMMISMATCH = 4
_DtcLu_Xln_Error = Int32
DTCLUXLNERROR_PROTOCOL = 1
DTCLUXLNERROR_LOGNAMEMISMATCH = 2
DTCLUXLNERROR_COLDWARMMISMATCH = 3
_DtcLu_CompareState = Int32
DTCLUCOMPARESTATE_COMMITTED = 1
DTCLUCOMPARESTATE_HEURISTICCOMMITTED = 2
DTCLUCOMPARESTATE_HEURISTICMIXED = 3
DTCLUCOMPARESTATE_HEURISTICRESET = 4
DTCLUCOMPARESTATE_INDOUBT = 5
DTCLUCOMPARESTATE_RESET = 6
_DtcLu_CompareStates_Confirmation = Int32
DTCLUCOMPARESTATESCONFIRMATION_CONFIRM = 1
DTCLUCOMPARESTATESCONFIRMATION_PROTOCOL = 2
_DtcLu_CompareStates_Error = Int32
DTCLUCOMPARESTATESERROR_PROTOCOL = 1
_DtcLu_CompareStates_Response = Int32
DTCLUCOMPARESTATESRESPONSE_OK = 1
DTCLUCOMPARESTATESRESPONSE_PROTOCOL = 2
def _define_IDtcLuRecoveryInitiatedByDtcTransWork_head():
    class IDtcLuRecoveryInitiatedByDtcTransWork(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e765-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRecoveryInitiatedByDtcTransWork
def _define_IDtcLuRecoveryInitiatedByDtcTransWork():
    IDtcLuRecoveryInitiatedByDtcTransWork = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByDtcTransWork_head
    IDtcLuRecoveryInitiatedByDtcTransWork.GetLogNameSizes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetLogNameSizes', ((1, 'pcbOurLogName'),(1, 'pcbRemoteLogName'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.GetOurXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_Xln),c_char_p_no,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'GetOurXln', ((1, 'pXln'),(1, 'pOurLogName'),(1, 'pRemoteLogName'),(1, 'pdwProtocol'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.HandleConfirmationFromOurXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_Xln_Confirmation, use_last_error=False)(5, 'HandleConfirmationFromOurXln', ((1, 'Confirmation'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.HandleTheirXlnResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_Xln,c_char_p_no,UInt32,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_Xln_Confirmation), use_last_error=False)(6, 'HandleTheirXlnResponse', ((1, 'Xln'),(1, 'pRemoteLogName'),(1, 'cbRemoteLogName'),(1, 'dwProtocol'),(1, 'pConfirmation'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.HandleErrorFromOurXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_Xln_Error, use_last_error=False)(7, 'HandleErrorFromOurXln', ((1, 'Error'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.CheckForCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'CheckForCompareStates', ((1, 'fCompareStates'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.GetOurTransIdSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetOurTransIdSize', ((1, 'pcbOurTransId'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.GetOurCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_CompareState), use_last_error=False)(10, 'GetOurCompareStates', ((1, 'pOurTransId'),(1, 'pCompareState'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.HandleTheirCompareStatesResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_CompareState,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_CompareStates_Confirmation), use_last_error=False)(11, 'HandleTheirCompareStatesResponse', ((1, 'CompareState'),(1, 'pConfirmation'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.HandleErrorFromOurCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_CompareStates_Error, use_last_error=False)(12, 'HandleErrorFromOurCompareStates', ((1, 'Error'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.ConversationLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'ConversationLost', ()))
    IDtcLuRecoveryInitiatedByDtcTransWork.GetRecoverySeqNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetRecoverySeqNum', ((1, 'plRecoverySeqNum'),)))
    IDtcLuRecoveryInitiatedByDtcTransWork.ObsoleteRecoverySeqNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'ObsoleteRecoverySeqNum', ((1, 'lNewRecoverySeqNum'),)))
    return IDtcLuRecoveryInitiatedByDtcTransWork
def _define_IDtcLuRecoveryInitiatedByDtcStatusWork_head():
    class IDtcLuRecoveryInitiatedByDtcStatusWork(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e766-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRecoveryInitiatedByDtcStatusWork
def _define_IDtcLuRecoveryInitiatedByDtcStatusWork():
    IDtcLuRecoveryInitiatedByDtcStatusWork = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByDtcStatusWork_head
    IDtcLuRecoveryInitiatedByDtcStatusWork.HandleCheckLuStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'HandleCheckLuStatus', ((1, 'lRecoverySeqNum'),)))
    return IDtcLuRecoveryInitiatedByDtcStatusWork
def _define_IDtcLuRecoveryInitiatedByDtc_head():
    class IDtcLuRecoveryInitiatedByDtc(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e764-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRecoveryInitiatedByDtc
def _define_IDtcLuRecoveryInitiatedByDtc():
    IDtcLuRecoveryInitiatedByDtc = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByDtc_head
    IDtcLuRecoveryInitiatedByDtc.GetWork = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_LocalRecovery_Work),POINTER(c_void_p), use_last_error=False)(3, 'GetWork', ((1, 'pWork'),(1, 'ppv'),)))
    return IDtcLuRecoveryInitiatedByDtc
def _define_IDtcLuRecoveryInitiatedByLuWork_head():
    class IDtcLuRecoveryInitiatedByLuWork(win32more.System.Com.IUnknown_head):
        Guid = Guid('ac2b8ad1-d6f0-11d0-b386-00a0c9083365')
    return IDtcLuRecoveryInitiatedByLuWork
def _define_IDtcLuRecoveryInitiatedByLuWork():
    IDtcLuRecoveryInitiatedByLuWork = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByLuWork_head
    IDtcLuRecoveryInitiatedByLuWork.HandleTheirXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.DistributedTransactionCoordinator._DtcLu_Xln,c_char_p_no,UInt32,c_char_p_no,UInt32,UInt32,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_Xln_Response), use_last_error=False)(3, 'HandleTheirXln', ((1, 'lRecoverySeqNum'),(1, 'Xln'),(1, 'pRemoteLogName'),(1, 'cbRemoteLogName'),(1, 'pOurLogName'),(1, 'cbOurLogName'),(1, 'dwProtocol'),(1, 'pResponse'),)))
    IDtcLuRecoveryInitiatedByLuWork.GetOurLogNameSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetOurLogNameSize', ((1, 'pcbOurLogName'),)))
    IDtcLuRecoveryInitiatedByLuWork.GetOurXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_Xln),c_char_p_no,POINTER(UInt32), use_last_error=False)(5, 'GetOurXln', ((1, 'pXln'),(1, 'pOurLogName'),(1, 'pdwProtocol'),)))
    IDtcLuRecoveryInitiatedByLuWork.HandleConfirmationOfOurXln = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_Xln_Confirmation, use_last_error=False)(6, 'HandleConfirmationOfOurXln', ((1, 'Confirmation'),)))
    IDtcLuRecoveryInitiatedByLuWork.HandleTheirCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,win32more.System.DistributedTransactionCoordinator._DtcLu_CompareState,POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_CompareStates_Response),POINTER(win32more.System.DistributedTransactionCoordinator._DtcLu_CompareState), use_last_error=False)(7, 'HandleTheirCompareStates', ((1, 'pRemoteTransId'),(1, 'cbRemoteTransId'),(1, 'CompareState'),(1, 'pResponse'),(1, 'pCompareState'),)))
    IDtcLuRecoveryInitiatedByLuWork.HandleConfirmationOfOurCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_CompareStates_Confirmation, use_last_error=False)(8, 'HandleConfirmationOfOurCompareStates', ((1, 'Confirmation'),)))
    IDtcLuRecoveryInitiatedByLuWork.HandleErrorFromOurCompareStates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator._DtcLu_CompareStates_Error, use_last_error=False)(9, 'HandleErrorFromOurCompareStates', ((1, 'Error'),)))
    IDtcLuRecoveryInitiatedByLuWork.ConversationLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'ConversationLost', ()))
    return IDtcLuRecoveryInitiatedByLuWork
def _define_IDtcLuRecoveryInitiatedByLu_head():
    class IDtcLuRecoveryInitiatedByLu(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e768-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRecoveryInitiatedByLu
def _define_IDtcLuRecoveryInitiatedByLu():
    IDtcLuRecoveryInitiatedByLu = win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByLu_head
    IDtcLuRecoveryInitiatedByLu.GetObjectToHandleWorkFromLu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRecoveryInitiatedByLuWork_head), use_last_error=False)(3, 'GetObjectToHandleWorkFromLu', ((1, 'ppWork'),)))
    return IDtcLuRecoveryInitiatedByLu
def _define_IDtcLuRmEnlistment_head():
    class IDtcLuRmEnlistment(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e769-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRmEnlistment
def _define_IDtcLuRmEnlistment():
    IDtcLuRmEnlistment = win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistment_head
    IDtcLuRmEnlistment.Unplug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'Unplug', ((1, 'fConversationLost'),)))
    IDtcLuRmEnlistment.BackedOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BackedOut', ()))
    IDtcLuRmEnlistment.BackOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'BackOut', ()))
    IDtcLuRmEnlistment.Committed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Committed', ()))
    IDtcLuRmEnlistment.Forget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Forget', ()))
    IDtcLuRmEnlistment.RequestCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'RequestCommit', ()))
    return IDtcLuRmEnlistment
def _define_IDtcLuRmEnlistmentSink_head():
    class IDtcLuRmEnlistmentSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e770-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRmEnlistmentSink
def _define_IDtcLuRmEnlistmentSink():
    IDtcLuRmEnlistmentSink = win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistmentSink_head
    IDtcLuRmEnlistmentSink.AckUnplug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'AckUnplug', ()))
    IDtcLuRmEnlistmentSink.TmDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'TmDown', ()))
    IDtcLuRmEnlistmentSink.SessionLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SessionLost', ()))
    IDtcLuRmEnlistmentSink.BackedOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'BackedOut', ()))
    IDtcLuRmEnlistmentSink.BackOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'BackOut', ()))
    IDtcLuRmEnlistmentSink.Committed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Committed', ()))
    IDtcLuRmEnlistmentSink.Forget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Forget', ()))
    IDtcLuRmEnlistmentSink.Prepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Prepare', ()))
    IDtcLuRmEnlistmentSink.RequestCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RequestCommit', ()))
    return IDtcLuRmEnlistmentSink
def _define_IDtcLuRmEnlistmentFactory_head():
    class IDtcLuRmEnlistmentFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e771-1aea-11d0-944b-00a0c905416e')
    return IDtcLuRmEnlistmentFactory
def _define_IDtcLuRmEnlistmentFactory():
    IDtcLuRmEnlistmentFactory = win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistmentFactory_head
    IDtcLuRmEnlistmentFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,win32more.System.DistributedTransactionCoordinator.ITransaction_head,c_char_p_no,UInt32,win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistmentSink_head,POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuRmEnlistment_head), use_last_error=False)(3, 'Create', ((1, 'pucLuPair'),(1, 'cbLuPair'),(1, 'pITransaction'),(1, 'pTransId'),(1, 'cbTransId'),(1, 'pRmEnlistmentSink'),(1, 'ppRmEnlistment'),)))
    return IDtcLuRmEnlistmentFactory
def _define_IDtcLuSubordinateDtc_head():
    class IDtcLuSubordinateDtc(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e773-1aea-11d0-944b-00a0c905416e')
    return IDtcLuSubordinateDtc
def _define_IDtcLuSubordinateDtc():
    IDtcLuSubordinateDtc = win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtc_head
    IDtcLuSubordinateDtc.Unplug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'Unplug', ((1, 'fConversationLost'),)))
    IDtcLuSubordinateDtc.BackedOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BackedOut', ()))
    IDtcLuSubordinateDtc.BackOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'BackOut', ()))
    IDtcLuSubordinateDtc.Committed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Committed', ()))
    IDtcLuSubordinateDtc.Forget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Forget', ()))
    IDtcLuSubordinateDtc.Prepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Prepare', ()))
    IDtcLuSubordinateDtc.RequestCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'RequestCommit', ()))
    return IDtcLuSubordinateDtc
def _define_IDtcLuSubordinateDtcSink_head():
    class IDtcLuSubordinateDtcSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e774-1aea-11d0-944b-00a0c905416e')
    return IDtcLuSubordinateDtcSink
def _define_IDtcLuSubordinateDtcSink():
    IDtcLuSubordinateDtcSink = win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtcSink_head
    IDtcLuSubordinateDtcSink.AckUnplug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'AckUnplug', ()))
    IDtcLuSubordinateDtcSink.TmDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'TmDown', ()))
    IDtcLuSubordinateDtcSink.SessionLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SessionLost', ()))
    IDtcLuSubordinateDtcSink.BackedOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'BackedOut', ()))
    IDtcLuSubordinateDtcSink.BackOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'BackOut', ()))
    IDtcLuSubordinateDtcSink.Committed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Committed', ()))
    IDtcLuSubordinateDtcSink.Forget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Forget', ()))
    IDtcLuSubordinateDtcSink.RequestCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'RequestCommit', ()))
    return IDtcLuSubordinateDtcSink
def _define_IDtcLuSubordinateDtcFactory_head():
    class IDtcLuSubordinateDtcFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('4131e775-1aea-11d0-944b-00a0c905416e')
    return IDtcLuSubordinateDtcFactory
def _define_IDtcLuSubordinateDtcFactory():
    IDtcLuSubordinateDtcFactory = win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtcFactory_head
    IDtcLuSubordinateDtcFactory.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,win32more.System.Com.IUnknown_head,Int32,UInt32,win32more.System.DistributedTransactionCoordinator.ITransactionOptions_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head),c_char_p_no,UInt32,win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtcSink_head,POINTER(win32more.System.DistributedTransactionCoordinator.IDtcLuSubordinateDtc_head), use_last_error=False)(3, 'Create', ((1, 'pucLuPair'),(1, 'cbLuPair'),(1, 'punkTransactionOuter'),(1, 'isoLevel'),(1, 'isoFlags'),(1, 'pOptions'),(1, 'ppTransaction'),(1, 'pTransId'),(1, 'cbTransId'),(1, 'pSubordinateDtcSink'),(1, 'ppSubordinateDtc'),)))
    return IDtcLuSubordinateDtcFactory
def _define_DtcGetTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32,UInt16,c_void_p,POINTER(c_void_p), use_last_error=False)(("DtcGetTransactionManager", windll["XOLEHLP"]), ((1, 'i_pszHost'),(1, 'i_pszTmName'),(1, 'i_riid'),(1, 'i_dwReserved1'),(1, 'i_wcbReserved2'),(1, 'i_pvReserved2'),(1, 'o_ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DtcGetTransactionManagerC():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32,UInt16,c_void_p,POINTER(c_void_p), use_last_error=False)(("DtcGetTransactionManagerC", windll["XOLEHLP"]), ((1, 'i_pszHost'),(1, 'i_pszTmName'),(1, 'i_riid'),(1, 'i_dwReserved1'),(1, 'i_wcbReserved2'),(1, 'i_pvReserved2'),(1, 'o_ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DtcGetTransactionManagerExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(Guid),UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(("DtcGetTransactionManagerExA", windll["XOLEHLP"]), ((1, 'i_pszHost'),(1, 'i_pszTmName'),(1, 'i_riid'),(1, 'i_grfOptions'),(1, 'i_pvConfigParams'),(1, 'o_ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DtcGetTransactionManagerExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(("DtcGetTransactionManagerExW", windll["XOLEHLP"]), ((1, 'i_pwszHost'),(1, 'i_pwszTmName'),(1, 'i_riid'),(1, 'i_grfOptions'),(1, 'i_pvConfigParams'),(1, 'o_ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DtcGetTransactionManagerEx():
    return win32more.System.DistributedTransactionCoordinator.DtcGetTransactionManagerExW
__all__ = [
    "DTCINSTALL_E_CLIENT_ALREADY_INSTALLED",
    "DTCINSTALL_E_SERVER_ALREADY_INSTALLED",
    "XA_SWITCH_F_DTC",
    "XA_FMTID_DTC",
    "XA_FMTID_DTC_VER1",
    "XIDDATASIZE",
    "MAXGTRIDSIZE",
    "MAXBQUALSIZE",
    "RMNAMESZ",
    "MAXINFOSIZE",
    "TMNOFLAGS",
    "TMREGISTER",
    "TMNOMIGRATE",
    "TMUSEASYNC",
    "TMASYNC",
    "TMONEPHASE",
    "TMFAIL",
    "TMNOWAIT",
    "TMRESUME",
    "TMSUCCESS",
    "TMSUSPEND",
    "TMSTARTRSCAN",
    "TMENDRSCAN",
    "TMMULTIPLE",
    "TMJOIN",
    "TMMIGRATE",
    "TM_JOIN",
    "TM_RESUME",
    "TM_OK",
    "TMER_TMERR",
    "TMER_INVAL",
    "TMER_PROTO",
    "XA_RBBASE",
    "XA_RBROLLBACK",
    "XA_RBCOMMFAIL",
    "XA_RBDEADLOCK",
    "XA_RBINTEGRITY",
    "XA_RBOTHER",
    "XA_RBPROTO",
    "XA_RBTIMEOUT",
    "XA_RBTRANSIENT",
    "XA_RBEND",
    "XA_NOMIGRATE",
    "XA_HEURHAZ",
    "XA_HEURCOM",
    "XA_HEURRB",
    "XA_HEURMIX",
    "XA_RETRY",
    "XA_RDONLY",
    "XA_OK",
    "XAER_ASYNC",
    "XAER_RMERR",
    "XAER_NOTA",
    "XAER_INVAL",
    "XAER_PROTO",
    "XAER_RMFAIL",
    "XAER_DUPID",
    "XAER_OUTSIDE",
    "DTC_INSTALL_OVERWRITE_CLIENT",
    "DTC_INSTALL_OVERWRITE_SERVER",
    "OLE_TM_CONFIG_VERSION_1",
    "OLE_TM_CONFIG_VERSION_2",
    "OLE_TM_FLAG_NONE",
    "OLE_TM_FLAG_NODEMANDSTART",
    "OLE_TM_FLAG_NOAGILERECOVERY",
    "OLE_TM_FLAG_QUERY_SERVICE_LOCKSTATUS",
    "OLE_TM_FLAG_INTERNAL_TO_TM",
    "CLSID_MSDtcTransactionManager",
    "CLSID_MSDtcTransaction",
    "DTC_STATUS_",
    "DTC_STATUS_UNKNOWN",
    "DTC_STATUS_STARTING",
    "DTC_STATUS_STARTED",
    "DTC_STATUS_PAUSING",
    "DTC_STATUS_PAUSED",
    "DTC_STATUS_CONTINUING",
    "DTC_STATUS_STOPPING",
    "DTC_STATUS_STOPPED",
    "DTC_STATUS_E_CANTCONTROL",
    "DTC_STATUS_FAILED",
    "DTC_GET_TRANSACTION_MANAGER",
    "DTC_GET_TRANSACTION_MANAGER_EX_A",
    "DTC_GET_TRANSACTION_MANAGER_EX_W",
    "DTC_INSTALL_CLIENT",
    "BOID",
    "TX_MISC_CONSTANTS",
    "MAX_TRAN_DESC",
    "ISOLATIONLEVEL",
    "ISOLATIONLEVEL_UNSPECIFIED",
    "ISOLATIONLEVEL_CHAOS",
    "ISOLATIONLEVEL_READUNCOMMITTED",
    "ISOLATIONLEVEL_BROWSE",
    "ISOLATIONLEVEL_CURSORSTABILITY",
    "ISOLATIONLEVEL_READCOMMITTED",
    "ISOLATIONLEVEL_REPEATABLEREAD",
    "ISOLATIONLEVEL_SERIALIZABLE",
    "ISOLATIONLEVEL_ISOLATED",
    "XACTTRANSINFO",
    "XACTSTATS",
    "ISOFLAG",
    "ISOFLAG_RETAIN_COMMIT_DC",
    "ISOFLAG_RETAIN_COMMIT",
    "ISOFLAG_RETAIN_COMMIT_NO",
    "ISOFLAG_RETAIN_ABORT_DC",
    "ISOFLAG_RETAIN_ABORT",
    "ISOFLAG_RETAIN_ABORT_NO",
    "ISOFLAG_RETAIN_DONTCARE",
    "ISOFLAG_RETAIN_BOTH",
    "ISOFLAG_RETAIN_NONE",
    "ISOFLAG_OPTIMISTIC",
    "ISOFLAG_READONLY",
    "XACTTC",
    "XACTTC_NONE",
    "XACTTC_SYNC_PHASEONE",
    "XACTTC_SYNC_PHASETWO",
    "XACTTC_SYNC",
    "XACTTC_ASYNC_PHASEONE",
    "XACTTC_ASYNC",
    "XACTRM",
    "XACTRM_OPTIMISTICLASTWINS",
    "XACTRM_NOREADONLYPREPARES",
    "XACTCONST",
    "XACTCONST_TIMEOUTINFINITE",
    "XACTHEURISTIC",
    "XACTHEURISTIC_ABORT",
    "XACTHEURISTIC_COMMIT",
    "XACTHEURISTIC_DAMAGE",
    "XACTHEURISTIC_DANGER",
    "XACTSTAT",
    "XACTSTAT_NONE",
    "XACTSTAT_OPENNORMAL",
    "XACTSTAT_OPENREFUSED",
    "XACTSTAT_PREPARING",
    "XACTSTAT_PREPARED",
    "XACTSTAT_PREPARERETAINING",
    "XACTSTAT_PREPARERETAINED",
    "XACTSTAT_COMMITTING",
    "XACTSTAT_COMMITRETAINING",
    "XACTSTAT_ABORTING",
    "XACTSTAT_ABORTED",
    "XACTSTAT_COMMITTED",
    "XACTSTAT_HEURISTIC_ABORT",
    "XACTSTAT_HEURISTIC_COMMIT",
    "XACTSTAT_HEURISTIC_DAMAGE",
    "XACTSTAT_HEURISTIC_DANGER",
    "XACTSTAT_FORCED_ABORT",
    "XACTSTAT_FORCED_COMMIT",
    "XACTSTAT_INDOUBT",
    "XACTSTAT_CLOSED",
    "XACTSTAT_OPEN",
    "XACTSTAT_NOTPREPARED",
    "XACTSTAT_ALL",
    "XACTOPT",
    "ITransaction",
    "ITransactionCloner",
    "ITransaction2",
    "ITransactionDispenser",
    "ITransactionOptions",
    "ITransactionOutcomeEvents",
    "ITmNodeName",
    "IKernelTransaction",
    "ITransactionResourceAsync",
    "ITransactionLastResourceAsync",
    "ITransactionResource",
    "ITransactionEnlistmentAsync",
    "ITransactionLastEnlistmentAsync",
    "ITransactionExportFactory",
    "ITransactionImportWhereabouts",
    "ITransactionExport",
    "ITransactionImport",
    "ITipTransaction",
    "ITipHelper",
    "ITipPullSink",
    "IDtcNetworkAccessConfig",
    "AUTHENTICATION_LEVEL",
    "NO_AUTHENTICATION_REQUIRED",
    "INCOMING_AUTHENTICATION_REQUIRED",
    "MUTUAL_AUTHENTICATION_REQUIRED",
    "IDtcNetworkAccessConfig2",
    "IDtcNetworkAccessConfig3",
    "xid_t",
    "xa_switch_t",
    "XA_OPEN_EPT",
    "XA_CLOSE_EPT",
    "XA_START_EPT",
    "XA_END_EPT",
    "XA_ROLLBACK_EPT",
    "XA_PREPARE_EPT",
    "XA_COMMIT_EPT",
    "XA_RECOVER_EPT",
    "XA_FORGET_EPT",
    "XA_COMPLETE_EPT",
    "IDtcToXaMapper",
    "IDtcToXaHelperFactory",
    "IDtcToXaHelper",
    "IDtcToXaHelperSinglePipe",
    "APPLICATIONTYPE",
    "LOCAL_APPLICATIONTYPE",
    "CLUSTERRESOURCE_APPLICATIONTYPE",
    "OLE_TM_CONFIG_PARAMS_V1",
    "OLE_TM_CONFIG_PARAMS_V2",
    "XACT_DTC_CONSTANTS",
    "XACT_E_CONNECTION_REQUEST_DENIED",
    "XACT_E_TOOMANY_ENLISTMENTS",
    "XACT_E_DUPLICATE_GUID",
    "XACT_E_NOTSINGLEPHASE",
    "XACT_E_RECOVERYALREADYDONE",
    "XACT_E_PROTOCOL",
    "XACT_E_RM_FAILURE",
    "XACT_E_RECOVERY_FAILED",
    "XACT_E_LU_NOT_FOUND",
    "XACT_E_DUPLICATE_LU",
    "XACT_E_LU_NOT_CONNECTED",
    "XACT_E_DUPLICATE_TRANSID",
    "XACT_E_LU_BUSY",
    "XACT_E_LU_NO_RECOVERY_PROCESS",
    "XACT_E_LU_DOWN",
    "XACT_E_LU_RECOVERING",
    "XACT_E_LU_RECOVERY_MISMATCH",
    "XACT_E_RM_UNAVAILABLE",
    "XACT_E_LRMRECOVERYALREADYDONE",
    "XACT_E_NOLASTRESOURCEINTERFACE",
    "XACT_S_NONOTIFY",
    "XACT_OK_NONOTIFY",
    "dwUSER_MS_SQLSERVER",
    "IXATransLookup",
    "IXATransLookup2",
    "IResourceManagerSink",
    "IResourceManager",
    "ILastResourceManager",
    "IResourceManager2",
    "IResourceManagerRejoinable",
    "IXAConfig",
    "IRMHelper",
    "IXAObtainRMInfo",
    "IResourceManagerFactory",
    "IResourceManagerFactory2",
    "IPrepareInfo",
    "IPrepareInfo2",
    "IGetDispenser",
    "ITransactionVoterBallotAsync2",
    "ITransactionVoterNotifyAsync2",
    "ITransactionVoterFactory2",
    "ITransactionPhase0EnlistmentAsync",
    "ITransactionPhase0NotifyAsync",
    "ITransactionPhase0Factory",
    "ITransactionTransmitter",
    "ITransactionTransmitterFactory",
    "ITransactionReceiver",
    "ITransactionReceiverFactory",
    "_ProxyConfigParams",
    "IDtcLuConfigure",
    "IDtcLuRecovery",
    "IDtcLuRecoveryFactory",
    "_DtcLu_LocalRecovery_Work",
    "DTCINITIATEDRECOVERYWORK_CHECKLUSTATUS",
    "DTCINITIATEDRECOVERYWORK_TRANS",
    "DTCINITIATEDRECOVERYWORK_TMDOWN",
    "_DtcLu_Xln",
    "DTCLUXLN_COLD",
    "DTCLUXLN_WARM",
    "_DtcLu_Xln_Confirmation",
    "DTCLUXLNCONFIRMATION_CONFIRM",
    "DTCLUXLNCONFIRMATION_LOGNAMEMISMATCH",
    "DTCLUXLNCONFIRMATION_COLDWARMMISMATCH",
    "DTCLUXLNCONFIRMATION_OBSOLETE",
    "_DtcLu_Xln_Response",
    "DTCLUXLNRESPONSE_OK_SENDOURXLNBACK",
    "DTCLUXLNRESPONSE_OK_SENDCONFIRMATION",
    "DTCLUXLNRESPONSE_LOGNAMEMISMATCH",
    "DTCLUXLNRESPONSE_COLDWARMMISMATCH",
    "_DtcLu_Xln_Error",
    "DTCLUXLNERROR_PROTOCOL",
    "DTCLUXLNERROR_LOGNAMEMISMATCH",
    "DTCLUXLNERROR_COLDWARMMISMATCH",
    "_DtcLu_CompareState",
    "DTCLUCOMPARESTATE_COMMITTED",
    "DTCLUCOMPARESTATE_HEURISTICCOMMITTED",
    "DTCLUCOMPARESTATE_HEURISTICMIXED",
    "DTCLUCOMPARESTATE_HEURISTICRESET",
    "DTCLUCOMPARESTATE_INDOUBT",
    "DTCLUCOMPARESTATE_RESET",
    "_DtcLu_CompareStates_Confirmation",
    "DTCLUCOMPARESTATESCONFIRMATION_CONFIRM",
    "DTCLUCOMPARESTATESCONFIRMATION_PROTOCOL",
    "_DtcLu_CompareStates_Error",
    "DTCLUCOMPARESTATESERROR_PROTOCOL",
    "_DtcLu_CompareStates_Response",
    "DTCLUCOMPARESTATESRESPONSE_OK",
    "DTCLUCOMPARESTATESRESPONSE_PROTOCOL",
    "IDtcLuRecoveryInitiatedByDtcTransWork",
    "IDtcLuRecoveryInitiatedByDtcStatusWork",
    "IDtcLuRecoveryInitiatedByDtc",
    "IDtcLuRecoveryInitiatedByLuWork",
    "IDtcLuRecoveryInitiatedByLu",
    "IDtcLuRmEnlistment",
    "IDtcLuRmEnlistmentSink",
    "IDtcLuRmEnlistmentFactory",
    "IDtcLuSubordinateDtc",
    "IDtcLuSubordinateDtcSink",
    "IDtcLuSubordinateDtcFactory",
    "DtcGetTransactionManager",
    "DtcGetTransactionManagerC",
    "DtcGetTransactionManagerExA",
    "DtcGetTransactionManagerExW",
    "DtcGetTransactionManagerEx",
]
