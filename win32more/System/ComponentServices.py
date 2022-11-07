from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.ComponentServices
import win32more.System.DistributedTransactionCoordinator

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
GUID_STRING_SIZE = 40
DATA_NOT_AVAILABLE = 4294967295
MTXDM_E_ENLISTRESOURCEFAILED = 2147803392
CRR_NO_REASON_SUPPLIED = 0
CRR_LIFETIME_LIMIT = 4294967295
CRR_ACTIVATION_LIMIT = 4294967294
CRR_CALL_LIMIT = 4294967293
CRR_MEMORY_LIMIT = 4294967292
CRR_RECYCLED_FROM_UI = 4294967291
SecurityIdentity = Guid('ecabb0a5-7f19-11d2-978e-0000f8757e2a')
SecurityCallers = Guid('ecabb0a6-7f19-11d2-978e-0000f8757e2a')
SecurityCallContext = Guid('ecabb0a7-7f19-11d2-978e-0000f8757e2a')
GetSecurityCallContextAppObject = Guid('ecabb0a8-7f19-11d2-978e-0000f8757e2a')
Dummy30040732 = Guid('ecabb0a9-7f19-11d2-978e-0000f8757e2a')
TransactionContext = Guid('7999fc25-d3c6-11cf-acab-00a024a55aef')
TransactionContextEx = Guid('5cb66670-d3d4-11cf-acab-00a024a55aef')
ByotServerEx = Guid('ecabb0aa-7f19-11d2-978e-0000f8757e2a')
CServiceConfig = Guid('ecabb0c8-7f19-11d2-978e-0000f8757e2a')
ServicePool = Guid('ecabb0c9-7f19-11d2-978e-0000f8757e2a')
ServicePoolConfig = Guid('ecabb0ca-7f19-11d2-978e-0000f8757e2a')
SharedProperty = Guid('2a005c05-a5de-11cf-9e66-00aa00a3f464')
SharedPropertyGroup = Guid('2a005c0b-a5de-11cf-9e66-00aa00a3f464')
SharedPropertyGroupManager = Guid('2a005c11-a5de-11cf-9e66-00aa00a3f464')
COMEvents = Guid('ecabb0ab-7f19-11d2-978e-0000f8757e2a')
CoMTSLocator = Guid('ecabb0ac-7f19-11d2-978e-0000f8757e2a')
MtsGrp = Guid('4b2e958d-0393-11d1-b1ab-00aa00ba3258')
ComServiceEvents = Guid('ecabb0c3-7f19-11d2-978e-0000f8757e2a')
ComSystemAppEventData = Guid('ecabb0c6-7f19-11d2-978e-0000f8757e2a')
CRMClerk = Guid('ecabb0bd-7f19-11d2-978e-0000f8757e2a')
CRMRecoveryClerk = Guid('ecabb0be-7f19-11d2-978e-0000f8757e2a')
LBEvents = Guid('ecabb0c1-7f19-11d2-978e-0000f8757e2a')
MessageMover = Guid('ecabb0bf-7f19-11d2-978e-0000f8757e2a')
DispenserManager = Guid('ecabb0c0-7f19-11d2-978e-0000f8757e2a')
PoolMgr = Guid('ecabafb5-7f19-11d2-978e-0000f8757e2a')
EventServer = Guid('ecabafbc-7f19-11d2-978e-0000f8757e2a')
TrackerServer = Guid('ecabafb9-7f19-11d2-978e-0000f8757e2a')
AppDomainHelper = Guid('ef24f689-14f8-4d92-b4af-d7b1f0e70fd4')
ClrAssemblyLocator = Guid('458aa3b5-265a-4b75-bc05-9bea4630cf18')
COMAdminCatalog = Guid('f618c514-dfb8-11d1-a2cf-00805fc79235')
COMAdminCatalogObject = Guid('f618c515-dfb8-11d1-a2cf-00805fc79235')
COMAdminCatalogCollection = Guid('f618c516-dfb8-11d1-a2cf-00805fc79235')
def _define_ICOMAdminCatalog_head():
    class ICOMAdminCatalog(win32more.System.Com.IDispatch_head):
        Guid = Guid('dd662187-dfc2-11d1-a2cf-00805fc79235')
    return ICOMAdminCatalog
def _define_ICOMAdminCatalog():
    ICOMAdminCatalog = win32more.System.ComponentServices.ICOMAdminCatalog_head
    ICOMAdminCatalog.GetCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'GetCollection', ((1, 'bstrCollName'),(1, 'ppCatalogCollection'),)))
    ICOMAdminCatalog.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'Connect', ((1, 'bstrCatalogServerName'),(1, 'ppCatalogCollection'),)))
    ICOMAdminCatalog.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_MajorVersion', ((1, 'plMajorVersion'),)))
    ICOMAdminCatalog.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_MinorVersion', ((1, 'plMinorVersion'),)))
    ICOMAdminCatalog.GetCollectionByQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(11, 'GetCollectionByQuery', ((1, 'bstrCollName'),(1, 'ppsaVarQuery'),(1, 'ppCatalogCollection'),)))
    ICOMAdminCatalog.ImportComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(12, 'ImportComponent', ((1, 'bstrApplIDOrName'),(1, 'bstrCLSIDOrProgID'),)))
    ICOMAdminCatalog.InstallComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(13, 'InstallComponent', ((1, 'bstrApplIDOrName'),(1, 'bstrDLL'),(1, 'bstrTLB'),(1, 'bstrPSDLL'),)))
    ICOMAdminCatalog.ShutdownApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'ShutdownApplication', ((1, 'bstrApplIDOrName'),)))
    ICOMAdminCatalog.ExportApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.ComponentServices.COMAdminApplicationExportOptions, use_last_error=False)(15, 'ExportApplication', ((1, 'bstrApplIDOrName'),(1, 'bstrApplicationFile'),(1, 'lOptions'),)))
    ICOMAdminCatalog.InstallApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.ComponentServices.COMAdminApplicationInstallOptions,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(16, 'InstallApplication', ((1, 'bstrApplicationFile'),(1, 'bstrDestinationDirectory'),(1, 'lOptions'),(1, 'bstrUserId'),(1, 'bstrPassword'),(1, 'bstrRSN'),)))
    ICOMAdminCatalog.StopRouter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'StopRouter', ()))
    ICOMAdminCatalog.RefreshRouter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'RefreshRouter', ()))
    ICOMAdminCatalog.StartRouter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'StartRouter', ()))
    ICOMAdminCatalog.Reserved1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Reserved1', ()))
    ICOMAdminCatalog.Reserved2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Reserved2', ()))
    ICOMAdminCatalog.InstallMultipleComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(22, 'InstallMultipleComponents', ((1, 'bstrApplIDOrName'),(1, 'ppsaVarFileNames'),(1, 'ppsaVarCLSIDs'),)))
    ICOMAdminCatalog.GetMultipleComponentsInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(23, 'GetMultipleComponentsInfo', ((1, 'bstrApplIdOrName'),(1, 'ppsaVarFileNames'),(1, 'ppsaVarCLSIDs'),(1, 'ppsaVarClassNames'),(1, 'ppsaVarFileFlags'),(1, 'ppsaVarComponentFlags'),)))
    ICOMAdminCatalog.RefreshComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'RefreshComponents', ()))
    ICOMAdminCatalog.BackupREGDB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'BackupREGDB', ((1, 'bstrBackupFilePath'),)))
    ICOMAdminCatalog.RestoreREGDB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'RestoreREGDB', ((1, 'bstrBackupFilePath'),)))
    ICOMAdminCatalog.QueryApplicationFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(Int16),POINTER(Int16),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(27, 'QueryApplicationFile', ((1, 'bstrApplicationFile'),(1, 'pbstrApplicationName'),(1, 'pbstrApplicationDescription'),(1, 'pbHasUsers'),(1, 'pbIsProxy'),(1, 'ppsaVarFileNames'),)))
    ICOMAdminCatalog.StartApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'StartApplication', ((1, 'bstrApplIdOrName'),)))
    ICOMAdminCatalog.ServiceCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(29, 'ServiceCheck', ((1, 'lService'),(1, 'plStatus'),)))
    ICOMAdminCatalog.InstallMultipleEventClasses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(30, 'InstallMultipleEventClasses', ((1, 'bstrApplIdOrName'),(1, 'ppsaVarFileNames'),(1, 'ppsaVarCLSIDS'),)))
    ICOMAdminCatalog.InstallEventClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(31, 'InstallEventClass', ((1, 'bstrApplIdOrName'),(1, 'bstrDLL'),(1, 'bstrTLB'),(1, 'bstrPSDLL'),)))
    ICOMAdminCatalog.GetEventClassesForIID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(32, 'GetEventClassesForIID', ((1, 'bstrIID'),(1, 'ppsaVarCLSIDs'),(1, 'ppsaVarProgIDs'),(1, 'ppsaVarDescriptions'),)))
    win32more.System.Com.IDispatch
    return ICOMAdminCatalog
COMAdminInUse = Int32
COMAdminInUse_COMAdminNotInUse = 0
COMAdminInUse_COMAdminInUseByCatalog = 1
COMAdminInUse_COMAdminInUseByRegistryUnknown = 2
COMAdminInUse_COMAdminInUseByRegistryProxyStub = 3
COMAdminInUse_COMAdminInUseByRegistryTypeLib = 4
COMAdminInUse_COMAdminInUseByRegistryClsid = 5
def _define_ICOMAdminCatalog2_head():
    class ICOMAdminCatalog2(win32more.System.ComponentServices.ICOMAdminCatalog_head):
        Guid = Guid('790c6e0b-9194-4cc9-9426-a48a63185696')
    return ICOMAdminCatalog2
def _define_ICOMAdminCatalog2():
    ICOMAdminCatalog2 = win32more.System.ComponentServices.ICOMAdminCatalog2_head
    ICOMAdminCatalog2.GetCollectionByQuery2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(33, 'GetCollectionByQuery2', ((1, 'bstrCollectionName'),(1, 'pVarQueryStrings'),(1, 'ppCatalogCollection'),)))
    ICOMAdminCatalog2.GetApplicationInstanceIDFromProcessID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'GetApplicationInstanceIDFromProcessID', ((1, 'lProcessID'),(1, 'pbstrApplicationInstanceID'),)))
    ICOMAdminCatalog2.ShutdownApplicationInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(35, 'ShutdownApplicationInstances', ((1, 'pVarApplicationInstanceID'),)))
    ICOMAdminCatalog2.PauseApplicationInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(36, 'PauseApplicationInstances', ((1, 'pVarApplicationInstanceID'),)))
    ICOMAdminCatalog2.ResumeApplicationInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(37, 'ResumeApplicationInstances', ((1, 'pVarApplicationInstanceID'),)))
    ICOMAdminCatalog2.RecycleApplicationInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(38, 'RecycleApplicationInstances', ((1, 'pVarApplicationInstanceID'),(1, 'lReasonCode'),)))
    ICOMAdminCatalog2.AreApplicationInstancesPaused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(39, 'AreApplicationInstancesPaused', ((1, 'pVarApplicationInstanceID'),(1, 'pVarBoolPaused'),)))
    ICOMAdminCatalog2.DumpApplicationInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'DumpApplicationInstance', ((1, 'bstrApplicationInstanceID'),(1, 'bstrDirectory'),(1, 'lMaxImages'),(1, 'pbstrDumpFile'),)))
    ICOMAdminCatalog2.get_IsApplicationInstanceDumpSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(41, 'get_IsApplicationInstanceDumpSupported', ((1, 'pVarBoolDumpSupported'),)))
    ICOMAdminCatalog2.CreateServiceForApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16, use_last_error=False)(42, 'CreateServiceForApplication', ((1, 'bstrApplicationIDOrName'),(1, 'bstrServiceName'),(1, 'bstrStartType'),(1, 'bstrErrorControl'),(1, 'bstrDependencies'),(1, 'bstrRunAs'),(1, 'bstrPassword'),(1, 'bDesktopOk'),)))
    ICOMAdminCatalog2.DeleteServiceForApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(43, 'DeleteServiceForApplication', ((1, 'bstrApplicationIDOrName'),)))
    ICOMAdminCatalog2.GetPartitionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'GetPartitionID', ((1, 'bstrApplicationIDOrName'),(1, 'pbstrPartitionID'),)))
    ICOMAdminCatalog2.GetPartitionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'GetPartitionName', ((1, 'bstrApplicationIDOrName'),(1, 'pbstrPartitionName'),)))
    ICOMAdminCatalog2.put_CurrentPartition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(46, 'put_CurrentPartition', ((1, 'bstrPartitionIDOrName'),)))
    ICOMAdminCatalog2.get_CurrentPartitionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(47, 'get_CurrentPartitionID', ((1, 'pbstrPartitionID'),)))
    ICOMAdminCatalog2.get_CurrentPartitionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_CurrentPartitionName', ((1, 'pbstrPartitionName'),)))
    ICOMAdminCatalog2.get_GlobalPartitionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(49, 'get_GlobalPartitionID', ((1, 'pbstrGlobalPartitionID'),)))
    ICOMAdminCatalog2.FlushPartitionCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(50, 'FlushPartitionCache', ()))
    ICOMAdminCatalog2.CopyApplications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR, use_last_error=False)(51, 'CopyApplications', ((1, 'bstrSourcePartitionIDOrName'),(1, 'pVarApplicationID'),(1, 'bstrDestinationPartitionIDOrName'),)))
    ICOMAdminCatalog2.CopyComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR, use_last_error=False)(52, 'CopyComponents', ((1, 'bstrSourceApplicationIDOrName'),(1, 'pVarCLSIDOrProgID'),(1, 'bstrDestinationApplicationIDOrName'),)))
    ICOMAdminCatalog2.MoveComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR, use_last_error=False)(53, 'MoveComponents', ((1, 'bstrSourceApplicationIDOrName'),(1, 'pVarCLSIDOrProgID'),(1, 'bstrDestinationApplicationIDOrName'),)))
    ICOMAdminCatalog2.AliasComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(54, 'AliasComponent', ((1, 'bstrSrcApplicationIDOrName'),(1, 'bstrCLSIDOrProgID'),(1, 'bstrDestApplicationIDOrName'),(1, 'bstrNewProgId'),(1, 'bstrNewClsid'),)))
    ICOMAdminCatalog2.IsSafeToDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.ComponentServices.COMAdminInUse), use_last_error=False)(55, 'IsSafeToDelete', ((1, 'bstrDllName'),(1, 'pCOMAdminInUse'),)))
    ICOMAdminCatalog2.ImportUnconfiguredComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(56, 'ImportUnconfiguredComponents', ((1, 'bstrApplicationIDOrName'),(1, 'pVarCLSIDOrProgID'),(1, 'pVarComponentType'),)))
    ICOMAdminCatalog2.PromoteUnconfiguredComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(57, 'PromoteUnconfiguredComponents', ((1, 'bstrApplicationIDOrName'),(1, 'pVarCLSIDOrProgID'),(1, 'pVarComponentType'),)))
    ICOMAdminCatalog2.ImportComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(58, 'ImportComponents', ((1, 'bstrApplicationIDOrName'),(1, 'pVarCLSIDOrProgID'),(1, 'pVarComponentType'),)))
    ICOMAdminCatalog2.get_Is64BitCatalogServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(59, 'get_Is64BitCatalogServer', ((1, 'pbIs64Bit'),)))
    ICOMAdminCatalog2.ExportPartition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.ComponentServices.COMAdminApplicationExportOptions, use_last_error=False)(60, 'ExportPartition', ((1, 'bstrPartitionIDOrName'),(1, 'bstrPartitionFileName'),(1, 'lOptions'),)))
    ICOMAdminCatalog2.InstallPartition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.ComponentServices.COMAdminApplicationInstallOptions,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(61, 'InstallPartition', ((1, 'bstrFileName'),(1, 'bstrDestDirectory'),(1, 'lOptions'),(1, 'bstrUserID'),(1, 'bstrPassword'),(1, 'bstrRSN'),)))
    ICOMAdminCatalog2.QueryApplicationFile2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(62, 'QueryApplicationFile2', ((1, 'bstrApplicationFile'),(1, 'ppFilesForImport'),)))
    ICOMAdminCatalog2.GetComponentVersionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(63, 'GetComponentVersionCount', ((1, 'bstrCLSIDOrProgID'),(1, 'plVersionCount'),)))
    win32more.System.ComponentServices.ICOMAdminCatalog
    return ICOMAdminCatalog2
def _define_ICatalogObject_head():
    class ICatalogObject(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22871-8a19-11d0-81b6-00a0c9231c29')
    return ICatalogObject
def _define_ICatalogObject():
    ICatalogObject = win32more.System.ComponentServices.ICatalogObject_head
    ICatalogObject.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'bstrPropName'),(1, 'pvarRetVal'),)))
    ICatalogObject.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Value', ((1, 'bstrPropName'),(1, 'val'),)))
    ICatalogObject.get_Key = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Key', ((1, 'pvarRetVal'),)))
    ICatalogObject.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_Name', ((1, 'pvarRetVal'),)))
    ICatalogObject.IsPropertyReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(11, 'IsPropertyReadOnly', ((1, 'bstrPropName'),(1, 'pbRetVal'),)))
    ICatalogObject.get_Valid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_Valid', ((1, 'pbRetVal'),)))
    ICatalogObject.IsPropertyWriteOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(13, 'IsPropertyWriteOnly', ((1, 'bstrPropName'),(1, 'pbRetVal'),)))
    win32more.System.Com.IDispatch
    return ICatalogObject
def _define_ICatalogCollection_head():
    class ICatalogCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22872-8a19-11d0-81b6-00a0c9231c29')
    return ICatalogCollection
def _define_ICatalogCollection():
    ICatalogCollection = win32more.System.ComponentServices.ICatalogCollection_head
    ICatalogCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppEnumVariant'),)))
    ICatalogCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'get_Item', ((1, 'lIndex'),(1, 'ppCatalogObject'),)))
    ICatalogCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'plObjectCount'),)))
    ICatalogCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'Remove', ((1, 'lIndex'),)))
    ICatalogCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(11, 'Add', ((1, 'ppCatalogObject'),)))
    ICatalogCollection.Populate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Populate', ()))
    ICatalogCollection.SaveChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'SaveChanges', ((1, 'pcChanges'),)))
    ICatalogCollection.GetCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(14, 'GetCollection', ((1, 'bstrCollName'),(1, 'varObjectKey'),(1, 'ppCatalogCollection'),)))
    ICatalogCollection.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_Name', ((1, 'pVarNamel'),)))
    ICatalogCollection.get_AddEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_AddEnabled', ((1, 'pVarBool'),)))
    ICatalogCollection.get_RemoveEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_RemoveEnabled', ((1, 'pVarBool'),)))
    ICatalogCollection.GetUtilInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(18, 'GetUtilInterface', ((1, 'ppIDispatch'),)))
    ICatalogCollection.get_DataStoreMajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_DataStoreMajorVersion', ((1, 'plMajorVersion'),)))
    ICatalogCollection.get_DataStoreMinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_DataStoreMinorVersion', ((1, 'plMinorVersionl'),)))
    ICatalogCollection.PopulateByKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(21, 'PopulateByKey', ((1, 'psaKeys'),)))
    ICatalogCollection.PopulateByQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(22, 'PopulateByQuery', ((1, 'bstrQueryString'),(1, 'lQueryType'),)))
    win32more.System.Com.IDispatch
    return ICatalogCollection
COMAdminComponentType = Int32
COMAdminComponentType_COMAdmin32BitComponent = 1
COMAdminComponentType_COMAdmin64BitComponent = 2
COMAdminApplicationInstallOptions = Int32
COMAdminApplicationInstallOptions_COMAdminInstallNoUsers = 0
COMAdminApplicationInstallOptions_COMAdminInstallUsers = 1
COMAdminApplicationInstallOptions_COMAdminInstallForceOverwriteOfFiles = 2
COMAdminApplicationExportOptions = Int32
COMAdminApplicationExportOptions_COMAdminExportNoUsers = 0
COMAdminApplicationExportOptions_COMAdminExportUsers = 1
COMAdminApplicationExportOptions_COMAdminExportApplicationProxy = 2
COMAdminApplicationExportOptions_COMAdminExportForceOverwriteOfFiles = 4
COMAdminApplicationExportOptions_COMAdminExportIn10Format = 16
COMAdminThreadingModels = Int32
COMAdminThreadingModels_COMAdminThreadingModelApartment = 0
COMAdminThreadingModels_COMAdminThreadingModelFree = 1
COMAdminThreadingModels_COMAdminThreadingModelMain = 2
COMAdminThreadingModels_COMAdminThreadingModelBoth = 3
COMAdminThreadingModels_COMAdminThreadingModelNeutral = 4
COMAdminThreadingModels_COMAdminThreadingModelNotSpecified = 5
COMAdminTransactionOptions = Int32
COMAdminTransactionOptions_COMAdminTransactionIgnored = 0
COMAdminTransactionOptions_COMAdminTransactionNone = 1
COMAdminTransactionOptions_COMAdminTransactionSupported = 2
COMAdminTransactionOptions_COMAdminTransactionRequired = 3
COMAdminTransactionOptions_COMAdminTransactionRequiresNew = 4
COMAdminTxIsolationLevelOptions = Int32
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelAny = 0
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadUnCommitted = 1
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadCommitted = 2
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelRepeatableRead = 3
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelSerializable = 4
COMAdminSynchronizationOptions = Int32
COMAdminSynchronizationOptions_COMAdminSynchronizationIgnored = 0
COMAdminSynchronizationOptions_COMAdminSynchronizationNone = 1
COMAdminSynchronizationOptions_COMAdminSynchronizationSupported = 2
COMAdminSynchronizationOptions_COMAdminSynchronizationRequired = 3
COMAdminSynchronizationOptions_COMAdminSynchronizationRequiresNew = 4
COMAdminActivationOptions = Int32
COMAdminActivationOptions_COMAdminActivationInproc = 0
COMAdminActivationOptions_COMAdminActivationLocal = 1
COMAdminAccessChecksLevelOptions = Int32
COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationLevel = 0
COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationComponentLevel = 1
COMAdminAuthenticationLevelOptions = Int32
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationDefault = 0
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationNone = 1
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationConnect = 2
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationCall = 3
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPacket = 4
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationIntegrity = 5
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPrivacy = 6
COMAdminImpersonationLevelOptions = Int32
COMAdminImpersonationLevelOptions_COMAdminImpersonationAnonymous = 1
COMAdminImpersonationLevelOptions_COMAdminImpersonationIdentify = 2
COMAdminImpersonationLevelOptions_COMAdminImpersonationImpersonate = 3
COMAdminImpersonationLevelOptions_COMAdminImpersonationDelegate = 4
COMAdminAuthenticationCapabilitiesOptions = Int32
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesNone = 0
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesSecureReference = 2
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesStaticCloaking = 32
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesDynamicCloaking = 64
COMAdminOS = Int32
COMAdminOS_COMAdminOSNotInitialized = 0
COMAdminOS_COMAdminOSWindows3_1 = 1
COMAdminOS_COMAdminOSWindows9x = 2
COMAdminOS_COMAdminOSWindows2000 = 3
COMAdminOS_COMAdminOSWindows2000AdvancedServer = 4
COMAdminOS_COMAdminOSWindows2000Unknown = 5
COMAdminOS_COMAdminOSUnknown = 6
COMAdminOS_COMAdminOSWindowsXPPersonal = 11
COMAdminOS_COMAdminOSWindowsXPProfessional = 12
COMAdminOS_COMAdminOSWindowsNETStandardServer = 13
COMAdminOS_COMAdminOSWindowsNETEnterpriseServer = 14
COMAdminOS_COMAdminOSWindowsNETDatacenterServer = 15
COMAdminOS_COMAdminOSWindowsNETWebServer = 16
COMAdminOS_COMAdminOSWindowsLonghornPersonal = 17
COMAdminOS_COMAdminOSWindowsLonghornProfessional = 18
COMAdminOS_COMAdminOSWindowsLonghornStandardServer = 19
COMAdminOS_COMAdminOSWindowsLonghornEnterpriseServer = 20
COMAdminOS_COMAdminOSWindowsLonghornDatacenterServer = 21
COMAdminOS_COMAdminOSWindowsLonghornWebServer = 22
COMAdminOS_COMAdminOSWindows7Personal = 23
COMAdminOS_COMAdminOSWindows7Professional = 24
COMAdminOS_COMAdminOSWindows7StandardServer = 25
COMAdminOS_COMAdminOSWindows7EnterpriseServer = 26
COMAdminOS_COMAdminOSWindows7DatacenterServer = 27
COMAdminOS_COMAdminOSWindows7WebServer = 28
COMAdminOS_COMAdminOSWindows8Personal = 29
COMAdminOS_COMAdminOSWindows8Professional = 30
COMAdminOS_COMAdminOSWindows8StandardServer = 31
COMAdminOS_COMAdminOSWindows8EnterpriseServer = 32
COMAdminOS_COMAdminOSWindows8DatacenterServer = 33
COMAdminOS_COMAdminOSWindows8WebServer = 34
COMAdminOS_COMAdminOSWindowsBluePersonal = 35
COMAdminOS_COMAdminOSWindowsBlueProfessional = 36
COMAdminOS_COMAdminOSWindowsBlueStandardServer = 37
COMAdminOS_COMAdminOSWindowsBlueEnterpriseServer = 38
COMAdminOS_COMAdminOSWindowsBlueDatacenterServer = 39
COMAdminOS_COMAdminOSWindowsBlueWebServer = 40
COMAdminServiceOptions = Int32
COMAdminServiceOptions_COMAdminServiceLoadBalanceRouter = 1
COMAdminServiceStatusOptions = Int32
COMAdminServiceStatusOptions_COMAdminServiceStopped = 0
COMAdminServiceStatusOptions_COMAdminServiceStartPending = 1
COMAdminServiceStatusOptions_COMAdminServiceStopPending = 2
COMAdminServiceStatusOptions_COMAdminServiceRunning = 3
COMAdminServiceStatusOptions_COMAdminServiceContinuePending = 4
COMAdminServiceStatusOptions_COMAdminServicePausePending = 5
COMAdminServiceStatusOptions_COMAdminServicePaused = 6
COMAdminServiceStatusOptions_COMAdminServiceUnknownState = 7
COMAdminQCMessageAuthenticateOptions = Int32
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateSecureApps = 0
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOff = 1
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOn = 2
COMAdminFileFlags = Int32
COMAdminFileFlags_COMAdminFileFlagLoadable = 1
COMAdminFileFlags_COMAdminFileFlagCOM = 2
COMAdminFileFlags_COMAdminFileFlagContainsPS = 4
COMAdminFileFlags_COMAdminFileFlagContainsComp = 8
COMAdminFileFlags_COMAdminFileFlagContainsTLB = 16
COMAdminFileFlags_COMAdminFileFlagSelfReg = 32
COMAdminFileFlags_COMAdminFileFlagSelfUnReg = 64
COMAdminFileFlags_COMAdminFileFlagUnloadableDLL = 128
COMAdminFileFlags_COMAdminFileFlagDoesNotExist = 256
COMAdminFileFlags_COMAdminFileFlagAlreadyInstalled = 512
COMAdminFileFlags_COMAdminFileFlagBadTLB = 1024
COMAdminFileFlags_COMAdminFileFlagGetClassObjFailed = 2048
COMAdminFileFlags_COMAdminFileFlagClassNotAvailable = 4096
COMAdminFileFlags_COMAdminFileFlagRegistrar = 8192
COMAdminFileFlags_COMAdminFileFlagNoRegistrar = 16384
COMAdminFileFlags_COMAdminFileFlagDLLRegsvrFailed = 32768
COMAdminFileFlags_COMAdminFileFlagRegTLBFailed = 65536
COMAdminFileFlags_COMAdminFileFlagRegistrarFailed = 131072
COMAdminFileFlags_COMAdminFileFlagError = 262144
COMAdminComponentFlags = Int32
COMAdminComponentFlags_COMAdminCompFlagTypeInfoFound = 1
COMAdminComponentFlags_COMAdminCompFlagCOMPlusPropertiesFound = 2
COMAdminComponentFlags_COMAdminCompFlagProxyFound = 4
COMAdminComponentFlags_COMAdminCompFlagInterfacesFound = 8
COMAdminComponentFlags_COMAdminCompFlagAlreadyInstalled = 16
COMAdminComponentFlags_COMAdminCompFlagNotInApplication = 32
COMAdminErrorCodes = Int32
COMAdminErrorCodes_COMAdminErrObjectErrors = -2146368511
COMAdminErrorCodes_COMAdminErrObjectInvalid = -2146368510
COMAdminErrorCodes_COMAdminErrKeyMissing = -2146368509
COMAdminErrorCodes_COMAdminErrAlreadyInstalled = -2146368508
COMAdminErrorCodes_COMAdminErrAppFileWriteFail = -2146368505
COMAdminErrorCodes_COMAdminErrAppFileReadFail = -2146368504
COMAdminErrorCodes_COMAdminErrAppFileVersion = -2146368503
COMAdminErrorCodes_COMAdminErrBadPath = -2146368502
COMAdminErrorCodes_COMAdminErrApplicationExists = -2146368501
COMAdminErrorCodes_COMAdminErrRoleExists = -2146368500
COMAdminErrorCodes_COMAdminErrCantCopyFile = -2146368499
COMAdminErrorCodes_COMAdminErrNoUser = -2146368497
COMAdminErrorCodes_COMAdminErrInvalidUserids = -2146368496
COMAdminErrorCodes_COMAdminErrNoRegistryCLSID = -2146368495
COMAdminErrorCodes_COMAdminErrBadRegistryProgID = -2146368494
COMAdminErrorCodes_COMAdminErrAuthenticationLevel = -2146368493
COMAdminErrorCodes_COMAdminErrUserPasswdNotValid = -2146368492
COMAdminErrorCodes_COMAdminErrCLSIDOrIIDMismatch = -2146368488
COMAdminErrorCodes_COMAdminErrRemoteInterface = -2146368487
COMAdminErrorCodes_COMAdminErrDllRegisterServer = -2146368486
COMAdminErrorCodes_COMAdminErrNoServerShare = -2146368485
COMAdminErrorCodes_COMAdminErrDllLoadFailed = -2146368483
COMAdminErrorCodes_COMAdminErrBadRegistryLibID = -2146368482
COMAdminErrorCodes_COMAdminErrAppDirNotFound = -2146368481
COMAdminErrorCodes_COMAdminErrRegistrarFailed = -2146368477
COMAdminErrorCodes_COMAdminErrCompFileDoesNotExist = -2146368476
COMAdminErrorCodes_COMAdminErrCompFileLoadDLLFail = -2146368475
COMAdminErrorCodes_COMAdminErrCompFileGetClassObj = -2146368474
COMAdminErrorCodes_COMAdminErrCompFileClassNotAvail = -2146368473
COMAdminErrorCodes_COMAdminErrCompFileBadTLB = -2146368472
COMAdminErrorCodes_COMAdminErrCompFileNotInstallable = -2146368471
COMAdminErrorCodes_COMAdminErrNotChangeable = -2146368470
COMAdminErrorCodes_COMAdminErrNotDeletable = -2146368469
COMAdminErrorCodes_COMAdminErrSession = -2146368468
COMAdminErrorCodes_COMAdminErrCompMoveLocked = -2146368467
COMAdminErrorCodes_COMAdminErrCompMoveBadDest = -2146368466
COMAdminErrorCodes_COMAdminErrRegisterTLB = -2146368464
COMAdminErrorCodes_COMAdminErrSystemApp = -2146368461
COMAdminErrorCodes_COMAdminErrCompFileNoRegistrar = -2146368460
COMAdminErrorCodes_COMAdminErrCoReqCompInstalled = -2146368459
COMAdminErrorCodes_COMAdminErrServiceNotInstalled = -2146368458
COMAdminErrorCodes_COMAdminErrPropertySaveFailed = -2146368457
COMAdminErrorCodes_COMAdminErrObjectExists = -2146368456
COMAdminErrorCodes_COMAdminErrComponentExists = -2146368455
COMAdminErrorCodes_COMAdminErrRegFileCorrupt = -2146368453
COMAdminErrorCodes_COMAdminErrPropertyOverflow = -2146368452
COMAdminErrorCodes_COMAdminErrNotInRegistry = -2146368450
COMAdminErrorCodes_COMAdminErrObjectNotPoolable = -2146368449
COMAdminErrorCodes_COMAdminErrApplidMatchesClsid = -2146368442
COMAdminErrorCodes_COMAdminErrRoleDoesNotExist = -2146368441
COMAdminErrorCodes_COMAdminErrStartAppNeedsComponents = -2146368440
COMAdminErrorCodes_COMAdminErrRequiresDifferentPlatform = -2146368439
COMAdminErrorCodes_COMAdminErrQueuingServiceNotAvailable = -2146367998
COMAdminErrorCodes_COMAdminErrObjectParentMissing = -2146367480
COMAdminErrorCodes_COMAdminErrObjectDoesNotExist = -2146367479
COMAdminErrorCodes_COMAdminErrCanNotExportAppProxy = -2146368438
COMAdminErrorCodes_COMAdminErrCanNotStartApp = -2146368437
COMAdminErrorCodes_COMAdminErrCanNotExportSystemApp = -2146368436
COMAdminErrorCodes_COMAdminErrCanNotSubscribeToComponent = -2146368435
COMAdminErrorCodes_COMAdminErrAppNotRunning = -2146367478
COMAdminErrorCodes_COMAdminErrEventClassCannotBeSubscriber = -2146368434
COMAdminErrorCodes_COMAdminErrLibAppProxyIncompatible = -2146368433
COMAdminErrorCodes_COMAdminErrBasePartitionOnly = -2146368432
COMAdminErrorCodes_COMAdminErrDuplicatePartitionName = -2146368425
COMAdminErrorCodes_COMAdminErrPartitionInUse = -2146368423
COMAdminErrorCodes_COMAdminErrImportedComponentsNotAllowed = -2146368421
COMAdminErrorCodes_COMAdminErrRegdbNotInitialized = -2146368398
COMAdminErrorCodes_COMAdminErrRegdbNotOpen = -2146368397
COMAdminErrorCodes_COMAdminErrRegdbSystemErr = -2146368396
COMAdminErrorCodes_COMAdminErrRegdbAlreadyRunning = -2146368395
COMAdminErrorCodes_COMAdminErrMigVersionNotSupported = -2146368384
COMAdminErrorCodes_COMAdminErrMigSchemaNotFound = -2146368383
COMAdminErrorCodes_COMAdminErrCatBitnessMismatch = -2146368382
COMAdminErrorCodes_COMAdminErrCatUnacceptableBitness = -2146368381
COMAdminErrorCodes_COMAdminErrCatWrongAppBitnessBitness = -2146368380
COMAdminErrorCodes_COMAdminErrCatPauseResumeNotSupported = -2146368379
COMAdminErrorCodes_COMAdminErrCatServerFault = -2146368378
COMAdminErrorCodes_COMAdminErrCantRecycleLibraryApps = -2146367473
COMAdminErrorCodes_COMAdminErrCantRecycleServiceApps = -2146367471
COMAdminErrorCodes_COMAdminErrProcessAlreadyRecycled = -2146367470
COMAdminErrorCodes_COMAdminErrPausedProcessMayNotBeRecycled = -2146367469
COMAdminErrorCodes_COMAdminErrInvalidPartition = -2146367477
COMAdminErrorCodes_COMAdminErrPartitionMsiOnly = -2146367463
COMAdminErrorCodes_COMAdminErrStartAppDisabled = -2146368431
COMAdminErrorCodes_COMAdminErrCompMoveSource = -2146367460
COMAdminErrorCodes_COMAdminErrCompMoveDest = -2146367459
COMAdminErrorCodes_COMAdminErrCompMovePrivate = -2146367458
COMAdminErrorCodes_COMAdminErrCannotCopyEventClass = -2146367456
def _define_ISecurityIdentityColl_head():
    class ISecurityIdentityColl(win32more.System.Com.IDispatch_head):
        Guid = Guid('cafc823c-b441-11d1-b82b-0000f8757e2a')
    return ISecurityIdentityColl
def _define_ISecurityIdentityColl():
    ISecurityIdentityColl = win32more.System.ComponentServices.ISecurityIdentityColl_head
    ISecurityIdentityColl.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    ISecurityIdentityColl.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'name'),(1, 'pItem'),)))
    ISecurityIdentityColl.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    win32more.System.Com.IDispatch
    return ISecurityIdentityColl
def _define_ISecurityCallersColl_head():
    class ISecurityCallersColl(win32more.System.Com.IDispatch_head):
        Guid = Guid('cafc823d-b441-11d1-b82b-0000f8757e2a')
    return ISecurityCallersColl
def _define_ISecurityCallersColl():
    ISecurityCallersColl = win32more.System.ComponentServices.ISecurityCallersColl_head
    ISecurityCallersColl.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    ISecurityCallersColl.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.ComponentServices.ISecurityIdentityColl_head), use_last_error=False)(8, 'get_Item', ((1, 'lIndex'),(1, 'pObj'),)))
    ISecurityCallersColl.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    win32more.System.Com.IDispatch
    return ISecurityCallersColl
def _define_ISecurityCallContext_head():
    class ISecurityCallContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('cafc823e-b441-11d1-b82b-0000f8757e2a')
    return ISecurityCallContext
def _define_ISecurityCallContext():
    ISecurityCallContext = win32more.System.ComponentServices.ISecurityCallContext_head
    ISecurityCallContext.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    ISecurityCallContext.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'name'),(1, 'pItem'),)))
    ISecurityCallContext.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    ISecurityCallContext.IsCallerInRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(10, 'IsCallerInRole', ((1, 'bstrRole'),(1, 'pfInRole'),)))
    ISecurityCallContext.IsSecurityEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'IsSecurityEnabled', ((1, 'pfIsEnabled'),)))
    ISecurityCallContext.IsUserInRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(12, 'IsUserInRole', ((1, 'pUser'),(1, 'bstrRole'),(1, 'pfInRole'),)))
    win32more.System.Com.IDispatch
    return ISecurityCallContext
def _define_IGetSecurityCallContext_head():
    class IGetSecurityCallContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('cafc823f-b441-11d1-b82b-0000f8757e2a')
    return IGetSecurityCallContext
def _define_IGetSecurityCallContext():
    IGetSecurityCallContext = win32more.System.ComponentServices.IGetSecurityCallContext_head
    IGetSecurityCallContext.GetSecurityCallContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.ISecurityCallContext_head), use_last_error=False)(7, 'GetSecurityCallContext', ((1, 'ppObject'),)))
    win32more.System.Com.IDispatch
    return IGetSecurityCallContext
def _define_SecurityProperty_head():
    class SecurityProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('e74a7215-014d-11d1-a63c-00a0c911b4e0')
    return SecurityProperty
def _define_SecurityProperty():
    SecurityProperty = win32more.System.ComponentServices.SecurityProperty_head
    SecurityProperty.GetDirectCallerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetDirectCallerName', ((1, 'bstrUserName'),)))
    SecurityProperty.GetDirectCreatorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetDirectCreatorName', ((1, 'bstrUserName'),)))
    SecurityProperty.GetOriginalCallerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetOriginalCallerName', ((1, 'bstrUserName'),)))
    SecurityProperty.GetOriginalCreatorName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetOriginalCreatorName', ((1, 'bstrUserName'),)))
    win32more.System.Com.IDispatch
    return SecurityProperty
def _define_ContextInfo_head():
    class ContextInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('19a5a02c-0ac8-11d2-b286-00c04f8ef934')
    return ContextInfo
def _define_ContextInfo():
    ContextInfo = win32more.System.ComponentServices.ContextInfo_head
    ContextInfo.IsInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'IsInTransaction', ((1, 'pbIsInTx'),)))
    ContextInfo.GetTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'GetTransaction', ((1, 'ppTx'),)))
    ContextInfo.GetTransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetTransactionId', ((1, 'pbstrTxId'),)))
    ContextInfo.GetActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetActivityId', ((1, 'pbstrActivityId'),)))
    ContextInfo.GetContextId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetContextId', ((1, 'pbstrCtxId'),)))
    win32more.System.Com.IDispatch
    return ContextInfo
def _define_ContextInfo2_head():
    class ContextInfo2(win32more.System.ComponentServices.ContextInfo_head):
        Guid = Guid('c99d6e75-2375-11d4-8331-00c04f605588')
    return ContextInfo2
def _define_ContextInfo2():
    ContextInfo2 = win32more.System.ComponentServices.ContextInfo2_head
    ContextInfo2.GetPartitionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetPartitionId', ((1, '__MIDL__ContextInfo20000'),)))
    ContextInfo2.GetApplicationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetApplicationId', ((1, '__MIDL__ContextInfo20001'),)))
    ContextInfo2.GetApplicationInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetApplicationInstanceId', ((1, '__MIDL__ContextInfo20002'),)))
    win32more.System.ComponentServices.ContextInfo
    return ContextInfo2
def _define_ObjectContext_head():
    class ObjectContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('74c08646-cedb-11cf-8b49-00aa00b8a790')
    return ObjectContext
def _define_ObjectContext():
    ObjectContext = win32more.System.ComponentServices.ObjectContext_head
    ObjectContext.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'CreateInstance', ((1, 'bstrProgID'),(1, 'pObject'),)))
    ObjectContext.SetComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'SetComplete', ()))
    ObjectContext.SetAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'SetAbort', ()))
    ObjectContext.EnableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'EnableCommit', ()))
    ObjectContext.DisableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'DisableCommit', ()))
    ObjectContext.IsInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'IsInTransaction', ((1, 'pbIsInTx'),)))
    ObjectContext.IsSecurityEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'IsSecurityEnabled', ((1, 'pbIsEnabled'),)))
    ObjectContext.IsCallerInRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(14, 'IsCallerInRole', ((1, 'bstrRole'),(1, 'pbInRole'),)))
    ObjectContext.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Count', ((1, 'plCount'),)))
    ObjectContext.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(16, 'get_Item', ((1, 'name'),(1, 'pItem'),)))
    ObjectContext.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(17, 'get__NewEnum', ((1, 'ppEnum'),)))
    ObjectContext.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.SecurityProperty_head), use_last_error=False)(18, 'get_Security', ((1, 'ppSecurityProperty'),)))
    ObjectContext.get_ContextInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.ContextInfo_head), use_last_error=False)(19, 'get_ContextInfo', ((1, 'ppContextInfo'),)))
    win32more.System.Com.IDispatch
    return ObjectContext
def _define_ITransactionContextEx_head():
    class ITransactionContextEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('7999fc22-d3c6-11cf-acab-00a024a55aef')
    return ITransactionContextEx
def _define_ITransactionContextEx():
    ITransactionContextEx = win32more.System.ComponentServices.ITransactionContextEx_head
    ITransactionContextEx.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateInstance', ((1, 'rclsid'),(1, 'riid'),(1, 'pObject'),)))
    ITransactionContextEx.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Commit', ()))
    ITransactionContextEx.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Abort', ()))
    win32more.System.Com.IUnknown
    return ITransactionContextEx
def _define_ITransactionContext_head():
    class ITransactionContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('7999fc21-d3c6-11cf-acab-00a024a55aef')
    return ITransactionContext
def _define_ITransactionContext():
    ITransactionContext = win32more.System.ComponentServices.ITransactionContext_head
    ITransactionContext.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'CreateInstance', ((1, 'pszProgId'),(1, 'pObject'),)))
    ITransactionContext.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Commit', ()))
    ITransactionContext.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Abort', ()))
    win32more.System.Com.IDispatch
    return ITransactionContext
def _define_ICreateWithTransactionEx_head():
    class ICreateWithTransactionEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('455acf57-5345-11d2-99cf-00c04f797bc9')
    return ICreateWithTransactionEx
def _define_ICreateWithTransactionEx():
    ICreateWithTransactionEx = win32more.System.ComponentServices.ICreateWithTransactionEx_head
    ICreateWithTransactionEx.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateInstance', ((1, 'pTransaction'),(1, 'rclsid'),(1, 'riid'),(1, 'pObject'),)))
    win32more.System.Com.IUnknown
    return ICreateWithTransactionEx
def _define_ICreateWithLocalTransaction_head():
    class ICreateWithLocalTransaction(win32more.System.Com.IUnknown_head):
        Guid = Guid('227ac7a8-8423-42ce-b7cf-03061ec9aaa3')
    return ICreateWithLocalTransaction
def _define_ICreateWithLocalTransaction():
    ICreateWithLocalTransaction = win32more.System.ComponentServices.ICreateWithLocalTransaction_head
    ICreateWithLocalTransaction.CreateInstanceWithSysTx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateInstanceWithSysTx', ((1, 'pTransaction'),(1, 'rclsid'),(1, 'riid'),(1, 'pObject'),)))
    win32more.System.Com.IUnknown
    return ICreateWithLocalTransaction
def _define_ICreateWithTipTransactionEx_head():
    class ICreateWithTipTransactionEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('455acf59-5345-11d2-99cf-00c04f797bc9')
    return ICreateWithTipTransactionEx
def _define_ICreateWithTipTransactionEx():
    ICreateWithTipTransactionEx = win32more.System.ComponentServices.ICreateWithTipTransactionEx_head
    ICreateWithTipTransactionEx.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateInstance', ((1, 'bstrTipUrl'),(1, 'rclsid'),(1, 'riid'),(1, 'pObject'),)))
    win32more.System.Com.IUnknown
    return ICreateWithTipTransactionEx
def _define_COMSVCSEVENTINFO_head():
    class COMSVCSEVENTINFO(Structure):
        pass
    return COMSVCSEVENTINFO
def _define_COMSVCSEVENTINFO():
    COMSVCSEVENTINFO = win32more.System.ComponentServices.COMSVCSEVENTINFO_head
    COMSVCSEVENTINFO._fields_ = [
        ("cbSize", UInt32),
        ("dwPid", UInt32),
        ("lTime", Int64),
        ("lMicroTime", Int32),
        ("perfCount", Int64),
        ("guidApp", Guid),
        ("sMachineName", win32more.Foundation.PWSTR),
    ]
    return COMSVCSEVENTINFO
def _define_IComLTxEvents_head():
    class IComLTxEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('605cf82c-578e-4298-975d-82babcd9e053')
    return IComLTxEvents
def _define_IComLTxEvents():
    IComLTxEvents = win32more.System.ComponentServices.IComLTxEvents_head
    IComLTxEvents.OnLtxTransactionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,Guid,win32more.Foundation.BOOL,Int32, use_last_error=False)(3, 'OnLtxTransactionStart', ((1, 'pInfo'),(1, 'guidLtx'),(1, 'tsid'),(1, 'fRoot'),(1, 'nIsolationLevel'),)))
    IComLTxEvents.OnLtxTransactionPrepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,win32more.Foundation.BOOL, use_last_error=False)(4, 'OnLtxTransactionPrepare', ((1, 'pInfo'),(1, 'guidLtx'),(1, 'fVote'),)))
    IComLTxEvents.OnLtxTransactionAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(5, 'OnLtxTransactionAbort', ((1, 'pInfo'),(1, 'guidLtx'),)))
    IComLTxEvents.OnLtxTransactionCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(6, 'OnLtxTransactionCommit', ((1, 'pInfo'),(1, 'guidLtx'),)))
    IComLTxEvents.OnLtxTransactionPromote = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,Guid, use_last_error=False)(7, 'OnLtxTransactionPromote', ((1, 'pInfo'),(1, 'guidLtx'),(1, 'txnId'),)))
    win32more.System.Com.IUnknown
    return IComLTxEvents
def _define_IComUserEvent_head():
    class IComUserEvent(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a4-2e50-11d2-98a5-00c04f8ee1c4')
    return IComUserEvent
def _define_IComUserEvent():
    IComUserEvent = win32more.System.ComponentServices.IComUserEvent_head
    IComUserEvent.OnUserEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'OnUserEvent', ((1, 'pInfo'),(1, 'pvarEvent'),)))
    win32more.System.Com.IUnknown
    return IComUserEvent
def _define_IComThreadEvents_head():
    class IComThreadEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a5-2e50-11d2-98a5-00c04f8ee1c4')
    return IComThreadEvents
def _define_IComThreadEvents():
    IComThreadEvents = win32more.System.ComponentServices.IComThreadEvents_head
    IComThreadEvents.OnThreadStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt32,UInt32, use_last_error=False)(3, 'OnThreadStart', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'dwThread'),(1, 'dwTheadCnt'),)))
    IComThreadEvents.OnThreadTerminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt32,UInt32, use_last_error=False)(4, 'OnThreadTerminate', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'dwThread'),(1, 'dwTheadCnt'),)))
    IComThreadEvents.OnThreadBindToApartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32,UInt32, use_last_error=False)(5, 'OnThreadBindToApartment', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'AptID'),(1, 'dwActCnt'),(1, 'dwLowCnt'),)))
    IComThreadEvents.OnThreadUnBind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32, use_last_error=False)(6, 'OnThreadUnBind', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'AptID'),(1, 'dwActCnt'),)))
    IComThreadEvents.OnThreadWorkEnque = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32, use_last_error=False)(7, 'OnThreadWorkEnque', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'MsgWorkID'),(1, 'QueueLen'),)))
    IComThreadEvents.OnThreadWorkPrivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64, use_last_error=False)(8, 'OnThreadWorkPrivate', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'MsgWorkID'),)))
    IComThreadEvents.OnThreadWorkPublic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32, use_last_error=False)(9, 'OnThreadWorkPublic', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'MsgWorkID'),(1, 'QueueLen'),)))
    IComThreadEvents.OnThreadWorkRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32,UInt64, use_last_error=False)(10, 'OnThreadWorkRedirect', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'MsgWorkID'),(1, 'QueueLen'),(1, 'ThreadNum'),)))
    IComThreadEvents.OnThreadWorkReject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64,UInt32, use_last_error=False)(11, 'OnThreadWorkReject', ((1, 'pInfo'),(1, 'ThreadID'),(1, 'MsgWorkID'),(1, 'QueueLen'),)))
    IComThreadEvents.OnThreadAssignApartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt64, use_last_error=False)(12, 'OnThreadAssignApartment', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'AptID'),)))
    IComThreadEvents.OnThreadUnassignApartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(13, 'OnThreadUnassignApartment', ((1, 'pInfo'),(1, 'AptID'),)))
    win32more.System.Com.IUnknown
    return IComThreadEvents
def _define_IComAppEvents_head():
    class IComAppEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a6-2e50-11d2-98a5-00c04f8ee1c4')
    return IComAppEvents
def _define_IComAppEvents():
    IComAppEvents = win32more.System.ComponentServices.IComAppEvents_head
    IComAppEvents.OnAppActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(3, 'OnAppActivation', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComAppEvents.OnAppShutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(4, 'OnAppShutdown', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComAppEvents.OnAppForceShutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(5, 'OnAppForceShutdown', ((1, 'pInfo'),(1, 'guidApp'),)))
    win32more.System.Com.IUnknown
    return IComAppEvents
def _define_IComInstanceEvents_head():
    class IComInstanceEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a7-2e50-11d2-98a5-00c04f8ee1c4')
    return IComInstanceEvents
def _define_IComInstanceEvents():
    IComInstanceEvents = win32more.System.ComponentServices.IComInstanceEvents_head
    IComInstanceEvents.OnObjectCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64,UInt64, use_last_error=False)(3, 'OnObjectCreate', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'clsid'),(1, 'tsid'),(1, 'CtxtID'),(1, 'ObjectID'),)))
    IComInstanceEvents.OnObjectDestroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(4, 'OnObjectDestroy', ((1, 'pInfo'),(1, 'CtxtID'),)))
    win32more.System.Com.IUnknown
    return IComInstanceEvents
def _define_IComTransactionEvents_head():
    class IComTransactionEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a8-2e50-11d2-98a5-00c04f8ee1c4')
    return IComTransactionEvents
def _define_IComTransactionEvents():
    IComTransactionEvents = win32more.System.ComponentServices.IComTransactionEvents_head
    IComTransactionEvents.OnTransactionStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(3, 'OnTransactionStart', ((1, 'pInfo'),(1, 'guidTx'),(1, 'tsid'),(1, 'fRoot'),)))
    IComTransactionEvents.OnTransactionPrepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(4, 'OnTransactionPrepare', ((1, 'pInfo'),(1, 'guidTx'),(1, 'fVoteYes'),)))
    IComTransactionEvents.OnTransactionAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(5, 'OnTransactionAbort', ((1, 'pInfo'),(1, 'guidTx'),)))
    IComTransactionEvents.OnTransactionCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(6, 'OnTransactionCommit', ((1, 'pInfo'),(1, 'guidTx'),)))
    win32more.System.Com.IUnknown
    return IComTransactionEvents
def _define_IComMethodEvents_head():
    class IComMethodEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130a9-2e50-11d2-98a5-00c04f8ee1c4')
    return IComMethodEvents
def _define_IComMethodEvents():
    IComMethodEvents = win32more.System.ComponentServices.IComMethodEvents_head
    IComMethodEvents.OnMethodCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(3, 'OnMethodCall', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'iMeth'),)))
    IComMethodEvents.OnMethodReturn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnMethodReturn', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'iMeth'),(1, 'hresult'),)))
    IComMethodEvents.OnMethodException = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(5, 'OnMethodException', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'iMeth'),)))
    win32more.System.Com.IUnknown
    return IComMethodEvents
def _define_IComObjectEvents_head():
    class IComObjectEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130aa-2e50-11d2-98a5-00c04f8ee1c4')
    return IComObjectEvents
def _define_IComObjectEvents():
    IComObjectEvents = win32more.System.ComponentServices.IComObjectEvents_head
    IComObjectEvents.OnObjectActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64, use_last_error=False)(3, 'OnObjectActivate', ((1, 'pInfo'),(1, 'CtxtID'),(1, 'ObjectID'),)))
    IComObjectEvents.OnObjectDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,UInt64, use_last_error=False)(4, 'OnObjectDeactivate', ((1, 'pInfo'),(1, 'CtxtID'),(1, 'ObjectID'),)))
    IComObjectEvents.OnDisableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(5, 'OnDisableCommit', ((1, 'pInfo'),(1, 'CtxtID'),)))
    IComObjectEvents.OnEnableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(6, 'OnEnableCommit', ((1, 'pInfo'),(1, 'CtxtID'),)))
    IComObjectEvents.OnSetComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(7, 'OnSetComplete', ((1, 'pInfo'),(1, 'CtxtID'),)))
    IComObjectEvents.OnSetAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(8, 'OnSetAbort', ((1, 'pInfo'),(1, 'CtxtID'),)))
    win32more.System.Com.IUnknown
    return IComObjectEvents
def _define_IComResourceEvents_head():
    class IComResourceEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130ab-2e50-11d2-98a5-00c04f8ee1c4')
    return IComResourceEvents
def _define_IComResourceEvents():
    IComResourceEvents = win32more.System.ComponentServices.IComResourceEvents_head
    IComResourceEvents.OnResourceCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.PWSTR,UInt64,win32more.Foundation.BOOL, use_last_error=False)(3, 'OnResourceCreate', ((1, 'pInfo'),(1, 'ObjectID'),(1, 'pszType'),(1, 'resId'),(1, 'enlisted'),)))
    IComResourceEvents.OnResourceAllocate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.PWSTR,UInt64,win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(4, 'OnResourceAllocate', ((1, 'pInfo'),(1, 'ObjectID'),(1, 'pszType'),(1, 'resId'),(1, 'enlisted'),(1, 'NumRated'),(1, 'Rating'),)))
    IComResourceEvents.OnResourceRecycle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.PWSTR,UInt64, use_last_error=False)(5, 'OnResourceRecycle', ((1, 'pInfo'),(1, 'ObjectID'),(1, 'pszType'),(1, 'resId'),)))
    IComResourceEvents.OnResourceDestroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64, use_last_error=False)(6, 'OnResourceDestroy', ((1, 'pInfo'),(1, 'ObjectID'),(1, 'hr'),(1, 'pszType'),(1, 'resId'),)))
    IComResourceEvents.OnResourceTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.PWSTR,UInt64,win32more.Foundation.BOOL, use_last_error=False)(7, 'OnResourceTrack', ((1, 'pInfo'),(1, 'ObjectID'),(1, 'pszType'),(1, 'resId'),(1, 'enlisted'),)))
    win32more.System.Com.IUnknown
    return IComResourceEvents
def _define_IComSecurityEvents_head():
    class IComSecurityEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130ac-2e50-11d2-98a5-00c04f8ee1c4')
    return IComSecurityEvents
def _define_IComSecurityEvents():
    IComSecurityEvents = win32more.System.ComponentServices.IComSecurityEvents_head
    IComSecurityEvents.OnAuthenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt64,POINTER(Guid),UInt32,UInt32,POINTER(Byte),UInt32,POINTER(Byte),win32more.Foundation.BOOL, use_last_error=False)(3, 'OnAuthenticate', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'ObjectID'),(1, 'guidIID'),(1, 'iMeth'),(1, 'cbByteOrig'),(1, 'pSidOriginalUser'),(1, 'cbByteCur'),(1, 'pSidCurrentUser'),(1, 'bCurrentUserInpersonatingInProc'),)))
    IComSecurityEvents.OnAuthenticateFail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt64,POINTER(Guid),UInt32,UInt32,POINTER(Byte),UInt32,POINTER(Byte),win32more.Foundation.BOOL, use_last_error=False)(4, 'OnAuthenticateFail', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'ObjectID'),(1, 'guidIID'),(1, 'iMeth'),(1, 'cbByteOrig'),(1, 'pSidOriginalUser'),(1, 'cbByteCur'),(1, 'pSidCurrentUser'),(1, 'bCurrentUserInpersonatingInProc'),)))
    win32more.System.Com.IUnknown
    return IComSecurityEvents
def _define_IComObjectPoolEvents_head():
    class IComObjectPoolEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130ad-2e50-11d2-98a5-00c04f8ee1c4')
    return IComObjectPoolEvents
def _define_IComObjectPoolEvents():
    IComObjectPoolEvents = win32more.System.ComponentServices.IComObjectPoolEvents_head
    IComObjectPoolEvents.OnObjPoolPutObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),Int32,UInt32,UInt64, use_last_error=False)(3, 'OnObjPoolPutObject', ((1, 'pInfo'),(1, 'guidObject'),(1, 'nReason'),(1, 'dwAvailable'),(1, 'oid'),)))
    IComObjectPoolEvents.OnObjPoolGetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32,UInt64, use_last_error=False)(4, 'OnObjPoolGetObject', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'dwAvailable'),(1, 'oid'),)))
    IComObjectPoolEvents.OnObjPoolRecycleToTx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64, use_last_error=False)(5, 'OnObjPoolRecycleToTx', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'guidTx'),(1, 'objid'),)))
    IComObjectPoolEvents.OnObjPoolGetFromTx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64, use_last_error=False)(6, 'OnObjPoolGetFromTx', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'guidTx'),(1, 'objid'),)))
    win32more.System.Com.IUnknown
    return IComObjectPoolEvents
def _define_IComObjectPoolEvents2_head():
    class IComObjectPoolEvents2(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130ae-2e50-11d2-98a5-00c04f8ee1c4')
    return IComObjectPoolEvents2
def _define_IComObjectPoolEvents2():
    IComObjectPoolEvents2 = win32more.System.ComponentServices.IComObjectPoolEvents2_head
    IComObjectPoolEvents2.OnObjPoolCreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt32,UInt64, use_last_error=False)(3, 'OnObjPoolCreateObject', ((1, 'pInfo'),(1, 'guidObject'),(1, 'dwObjsCreated'),(1, 'oid'),)))
    IComObjectPoolEvents2.OnObjPoolDestroyObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt32,UInt64, use_last_error=False)(4, 'OnObjPoolDestroyObject', ((1, 'pInfo'),(1, 'guidObject'),(1, 'dwObjsCreated'),(1, 'oid'),)))
    IComObjectPoolEvents2.OnObjPoolCreateDecision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt32,UInt32,UInt32,UInt32,UInt32, use_last_error=False)(5, 'OnObjPoolCreateDecision', ((1, 'pInfo'),(1, 'dwThreadsWaiting'),(1, 'dwAvail'),(1, 'dwCreated'),(1, 'dwMin'),(1, 'dwMax'),)))
    IComObjectPoolEvents2.OnObjPoolTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(6, 'OnObjPoolTimeout', ((1, 'pInfo'),(1, 'guidObject'),(1, 'guidActivity'),(1, 'dwTimeout'),)))
    IComObjectPoolEvents2.OnObjPoolCreatePool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt32,UInt32,UInt32, use_last_error=False)(7, 'OnObjPoolCreatePool', ((1, 'pInfo'),(1, 'guidObject'),(1, 'dwMin'),(1, 'dwMax'),(1, 'dwTimeout'),)))
    win32more.System.Com.IUnknown
    return IComObjectPoolEvents2
def _define_IComObjectConstructionEvents_head():
    class IComObjectConstructionEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130af-2e50-11d2-98a5-00c04f8ee1c4')
    return IComObjectConstructionEvents
def _define_IComObjectConstructionEvents():
    IComObjectConstructionEvents = win32more.System.ComponentServices.IComObjectConstructionEvents_head
    IComObjectConstructionEvents.OnObjectConstruct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),win32more.Foundation.PWSTR,UInt64, use_last_error=False)(3, 'OnObjectConstruct', ((1, 'pInfo'),(1, 'guidObject'),(1, 'sConstructString'),(1, 'oid'),)))
    win32more.System.Com.IUnknown
    return IComObjectConstructionEvents
def _define_IComActivityEvents_head():
    class IComActivityEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b0-2e50-11d2-98a5-00c04f8ee1c4')
    return IComActivityEvents
def _define_IComActivityEvents():
    IComActivityEvents = win32more.System.ComponentServices.IComActivityEvents_head
    IComActivityEvents.OnActivityCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(3, 'OnActivityCreate', ((1, 'pInfo'),(1, 'guidActivity'),)))
    IComActivityEvents.OnActivityDestroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(4, 'OnActivityDestroy', ((1, 'pInfo'),(1, 'guidActivity'),)))
    IComActivityEvents.OnActivityEnter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(5, 'OnActivityEnter', ((1, 'pInfo'),(1, 'guidCurrent'),(1, 'guidEntered'),(1, 'dwThread'),)))
    IComActivityEvents.OnActivityTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32,UInt32, use_last_error=False)(6, 'OnActivityTimeout', ((1, 'pInfo'),(1, 'guidCurrent'),(1, 'guidEntered'),(1, 'dwThread'),(1, 'dwTimeout'),)))
    IComActivityEvents.OnActivityReenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt32,UInt32, use_last_error=False)(7, 'OnActivityReenter', ((1, 'pInfo'),(1, 'guidCurrent'),(1, 'dwThread'),(1, 'dwCallDepth'),)))
    IComActivityEvents.OnActivityLeave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid), use_last_error=False)(8, 'OnActivityLeave', ((1, 'pInfo'),(1, 'guidCurrent'),(1, 'guidLeft'),)))
    IComActivityEvents.OnActivityLeaveSame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),UInt32, use_last_error=False)(9, 'OnActivityLeaveSame', ((1, 'pInfo'),(1, 'guidCurrent'),(1, 'dwCallDepth'),)))
    win32more.System.Com.IUnknown
    return IComActivityEvents
def _define_IComIdentityEvents_head():
    class IComIdentityEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b1-2e50-11d2-98a5-00c04f8ee1c4')
    return IComIdentityEvents
def _define_IComIdentityEvents():
    IComIdentityEvents = win32more.System.ComponentServices.IComIdentityEvents_head
    IComIdentityEvents.OnIISRequestInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'OnIISRequestInfo', ((1, 'pInfo'),(1, 'ObjId'),(1, 'pszClientIP'),(1, 'pszServerIP'),(1, 'pszURL'),)))
    win32more.System.Com.IUnknown
    return IComIdentityEvents
def _define_IComQCEvents_head():
    class IComQCEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b2-2e50-11d2-98a5-00c04f8ee1c4')
    return IComQCEvents
def _define_IComQCEvents():
    IComQCEvents = win32more.System.ComponentServices.IComQCEvents_head
    IComQCEvents.OnQCRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Char),POINTER(Guid),POINTER(Guid),win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnQCRecord', ((1, 'pInfo'),(1, 'objid'),(1, 'szQueue'),(1, 'guidMsgId'),(1, 'guidWorkFlowId'),(1, 'msmqhr'),)))
    IComQCEvents.OnQCQueueOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Char),UInt64,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnQCQueueOpen', ((1, 'pInfo'),(1, 'szQueue'),(1, 'QueueID'),(1, 'hr'),)))
    IComQCEvents.OnQCReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),win32more.Foundation.HRESULT, use_last_error=False)(5, 'OnQCReceive', ((1, 'pInfo'),(1, 'QueueID'),(1, 'guidMsgId'),(1, 'guidWorkFlowId'),(1, 'hr'),)))
    IComQCEvents.OnQCReceiveFail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnQCReceiveFail', ((1, 'pInfo'),(1, 'QueueID'),(1, 'msmqhr'),)))
    IComQCEvents.OnQCMoveToReTryQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(7, 'OnQCMoveToReTryQueue', ((1, 'pInfo'),(1, 'guidMsgId'),(1, 'guidWorkFlowId'),(1, 'RetryIndex'),)))
    IComQCEvents.OnQCMoveToDeadQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid), use_last_error=False)(8, 'OnQCMoveToDeadQueue', ((1, 'pInfo'),(1, 'guidMsgId'),(1, 'guidWorkFlowId'),)))
    IComQCEvents.OnQCPlayback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),win32more.Foundation.HRESULT, use_last_error=False)(9, 'OnQCPlayback', ((1, 'pInfo'),(1, 'objid'),(1, 'guidMsgId'),(1, 'guidWorkFlowId'),(1, 'hr'),)))
    win32more.System.Com.IUnknown
    return IComQCEvents
def _define_IComExceptionEvents_head():
    class IComExceptionEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b3-2e50-11d2-98a5-00c04f8ee1c4')
    return IComExceptionEvents
def _define_IComExceptionEvents():
    IComExceptionEvents = win32more.System.ComponentServices.IComExceptionEvents_head
    IComExceptionEvents.OnExceptionUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt32,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(3, 'OnExceptionUser', ((1, 'pInfo'),(1, 'code'),(1, 'address'),(1, 'pszStackTrace'),)))
    win32more.System.Com.IUnknown
    return IComExceptionEvents
def _define_ILBEvents_head():
    class ILBEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b4-2e50-11d2-98a5-00c04f8ee1c4')
    return ILBEvents
def _define_ILBEvents():
    ILBEvents = win32more.System.ComponentServices.ILBEvents_head
    ILBEvents.TargetUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(3, 'TargetUp', ((1, 'bstrServerName'),(1, 'bstrClsidEng'),)))
    ILBEvents.TargetDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(4, 'TargetDown', ((1, 'bstrServerName'),(1, 'bstrClsidEng'),)))
    ILBEvents.EngineDefined = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR, use_last_error=False)(5, 'EngineDefined', ((1, 'bstrPropName'),(1, 'varPropValue'),(1, 'bstrClsidEng'),)))
    win32more.System.Com.IUnknown
    return ILBEvents
def _define_IComCRMEvents_head():
    class IComCRMEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('683130b5-2e50-11d2-98a5-00c04f8ee1c4')
    return IComCRMEvents
def _define_IComCRMEvents():
    IComCRMEvents = win32more.System.ComponentServices.IComCRMEvents_head
    IComCRMEvents.OnCRMRecoveryStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(3, 'OnCRMRecoveryStart', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComCRMEvents.OnCRMRecoveryDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(4, 'OnCRMRecoveryDone', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComCRMEvents.OnCRMCheckpoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(5, 'OnCRMCheckpoint', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComCRMEvents.OnCRMBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,Guid,Guid,POINTER(Char),POINTER(Char), use_last_error=False)(6, 'OnCRMBegin', ((1, 'pInfo'),(1, 'guidClerkCLSID'),(1, 'guidActivity'),(1, 'guidTx'),(1, 'szProgIdCompensator'),(1, 'szDescription'),)))
    IComCRMEvents.OnCRMPrepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(7, 'OnCRMPrepare', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(8, 'OnCRMCommit', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(9, 'OnCRMAbort', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMIndoubt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(10, 'OnCRMIndoubt', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(11, 'OnCRMDone', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMRelease = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(12, 'OnCRMRelease', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMAnalyze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,UInt32,UInt32, use_last_error=False)(13, 'OnCRMAnalyze', ((1, 'pInfo'),(1, 'guidClerkCLSID'),(1, 'dwCrmRecordType'),(1, 'dwRecordSize'),)))
    IComCRMEvents.OnCRMWrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,win32more.Foundation.BOOL,UInt32, use_last_error=False)(14, 'OnCRMWrite', ((1, 'pInfo'),(1, 'guidClerkCLSID'),(1, 'fVariants'),(1, 'dwRecordSize'),)))
    IComCRMEvents.OnCRMForget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(15, 'OnCRMForget', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMForce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(16, 'OnCRMForce', ((1, 'pInfo'),(1, 'guidClerkCLSID'),)))
    IComCRMEvents.OnCRMDeliver = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,win32more.Foundation.BOOL,UInt32, use_last_error=False)(17, 'OnCRMDeliver', ((1, 'pInfo'),(1, 'guidClerkCLSID'),(1, 'fVariants'),(1, 'dwRecordSize'),)))
    win32more.System.Com.IUnknown
    return IComCRMEvents
def _define_IComMethod2Events_head():
    class IComMethod2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb388aaa-567d-4024-af8e-6e93ee748573')
    return IComMethod2Events
def _define_IComMethod2Events():
    IComMethod2Events = win32more.System.ComponentServices.IComMethod2Events_head
    IComMethod2Events.OnMethodCall2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32,UInt32, use_last_error=False)(3, 'OnMethodCall2', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'dwThread'),(1, 'iMeth'),)))
    IComMethod2Events.OnMethodReturn2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32,UInt32,win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnMethodReturn2', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'dwThread'),(1, 'iMeth'),(1, 'hresult'),)))
    IComMethod2Events.OnMethodException2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64,POINTER(Guid),POINTER(Guid),UInt32,UInt32, use_last_error=False)(5, 'OnMethodException2', ((1, 'pInfo'),(1, 'oid'),(1, 'guidCid'),(1, 'guidRid'),(1, 'dwThread'),(1, 'iMeth'),)))
    win32more.System.Com.IUnknown
    return IComMethod2Events
def _define_IComTrackingInfoEvents_head():
    class IComTrackingInfoEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e6cdcc9-fb25-4fd5-9cc5-c9f4b6559cec')
    return IComTrackingInfoEvents
def _define_IComTrackingInfoEvents():
    IComTrackingInfoEvents = win32more.System.ComponentServices.IComTrackingInfoEvents_head
    IComTrackingInfoEvents.OnNewTrackingInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'OnNewTrackingInfo', ((1, 'pToplevelCollection'),)))
    win32more.System.Com.IUnknown
    return IComTrackingInfoEvents
TRACKING_COLL_TYPE = Int32
TRKCOLL_PROCESSES = 0
TRKCOLL_APPLICATIONS = 1
TRKCOLL_COMPONENTS = 2
def _define_IComTrackingInfoCollection_head():
    class IComTrackingInfoCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c266c677-c9ad-49ab-9fd9-d9661078588a')
    return IComTrackingInfoCollection
def _define_IComTrackingInfoCollection():
    IComTrackingInfoCollection = win32more.System.ComponentServices.IComTrackingInfoCollection_head
    IComTrackingInfoCollection.Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.TRACKING_COLL_TYPE), use_last_error=False)(3, 'Type', ((1, 'pType'),)))
    IComTrackingInfoCollection.Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'Count', ((1, 'pCount'),)))
    IComTrackingInfoCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'Item', ((1, 'ulIndex'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IComTrackingInfoCollection
def _define_IComTrackingInfoObject_head():
    class IComTrackingInfoObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('116e42c5-d8b1-47bf-ab1e-c895ed3e2372')
    return IComTrackingInfoObject
def _define_IComTrackingInfoObject():
    IComTrackingInfoObject = win32more.System.ComponentServices.IComTrackingInfoObject_head
    IComTrackingInfoObject.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'GetValue', ((1, 'szPropertyName'),(1, 'pvarOut'),)))
    win32more.System.Com.IUnknown
    return IComTrackingInfoObject
def _define_IComTrackingInfoProperties_head():
    class IComTrackingInfoProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('789b42be-6f6b-443a-898e-67abf390aa14')
    return IComTrackingInfoProperties
def _define_IComTrackingInfoProperties():
    IComTrackingInfoProperties = win32more.System.ComponentServices.IComTrackingInfoProperties_head
    IComTrackingInfoProperties.PropCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'PropCount', ((1, 'pCount'),)))
    IComTrackingInfoProperties.GetPropName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetPropName', ((1, 'ulIndex'),(1, 'ppszPropName'),)))
    win32more.System.Com.IUnknown
    return IComTrackingInfoProperties
def _define_IComApp2Events_head():
    class IComApp2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('1290bc1a-b219-418d-b078-5934ded08242')
    return IComApp2Events
def _define_IComApp2Events():
    IComApp2Events = win32more.System.ComponentServices.IComApp2Events_head
    IComApp2Events.OnAppActivation2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,Guid, use_last_error=False)(3, 'OnAppActivation2', ((1, 'pInfo'),(1, 'guidApp'),(1, 'guidProcess'),)))
    IComApp2Events.OnAppShutdown2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(4, 'OnAppShutdown2', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComApp2Events.OnAppForceShutdown2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid, use_last_error=False)(5, 'OnAppForceShutdown2', ((1, 'pInfo'),(1, 'guidApp'),)))
    IComApp2Events.OnAppPaused2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,win32more.Foundation.BOOL, use_last_error=False)(6, 'OnAppPaused2', ((1, 'pInfo'),(1, 'guidApp'),(1, 'bPaused'),)))
    IComApp2Events.OnAppRecycle2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),Guid,Guid,Int32, use_last_error=False)(7, 'OnAppRecycle2', ((1, 'pInfo'),(1, 'guidApp'),(1, 'guidProcess'),(1, 'lReason'),)))
    win32more.System.Com.IUnknown
    return IComApp2Events
def _define_IComTransaction2Events_head():
    class IComTransaction2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('a136f62a-2f94-4288-86e0-d8a1fa4c0299')
    return IComTransaction2Events
def _define_IComTransaction2Events():
    IComTransaction2Events = win32more.System.ComponentServices.IComTransaction2Events_head
    IComTransaction2Events.OnTransactionStart2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),win32more.Foundation.BOOL,Int32, use_last_error=False)(3, 'OnTransactionStart2', ((1, 'pInfo'),(1, 'guidTx'),(1, 'tsid'),(1, 'fRoot'),(1, 'nIsolationLevel'),)))
    IComTransaction2Events.OnTransactionPrepare2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(4, 'OnTransactionPrepare2', ((1, 'pInfo'),(1, 'guidTx'),(1, 'fVoteYes'),)))
    IComTransaction2Events.OnTransactionAbort2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(5, 'OnTransactionAbort2', ((1, 'pInfo'),(1, 'guidTx'),)))
    IComTransaction2Events.OnTransactionCommit2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid), use_last_error=False)(6, 'OnTransactionCommit2', ((1, 'pInfo'),(1, 'guidTx'),)))
    win32more.System.Com.IUnknown
    return IComTransaction2Events
def _define_IComInstance2Events_head():
    class IComInstance2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('20e3bf07-b506-4ad5-a50c-d2ca5b9c158e')
    return IComInstance2Events
def _define_IComInstance2Events():
    IComInstance2Events = win32more.System.ComponentServices.IComInstance2Events_head
    IComInstance2Events.OnObjectCreate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64,UInt64,POINTER(Guid), use_last_error=False)(3, 'OnObjectCreate2', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'clsid'),(1, 'tsid'),(1, 'CtxtID'),(1, 'ObjectID'),(1, 'guidPartition'),)))
    IComInstance2Events.OnObjectDestroy2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),UInt64, use_last_error=False)(4, 'OnObjectDestroy2', ((1, 'pInfo'),(1, 'CtxtID'),)))
    win32more.System.Com.IUnknown
    return IComInstance2Events
def _define_IComObjectPool2Events_head():
    class IComObjectPool2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('65bf6534-85ea-4f64-8cf4-3d974b2ab1cf')
    return IComObjectPool2Events
def _define_IComObjectPool2Events():
    IComObjectPool2Events = win32more.System.ComponentServices.IComObjectPool2Events_head
    IComObjectPool2Events.OnObjPoolPutObject2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),Int32,UInt32,UInt64, use_last_error=False)(3, 'OnObjPoolPutObject2', ((1, 'pInfo'),(1, 'guidObject'),(1, 'nReason'),(1, 'dwAvailable'),(1, 'oid'),)))
    IComObjectPool2Events.OnObjPoolGetObject2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),UInt32,UInt64,POINTER(Guid), use_last_error=False)(4, 'OnObjPoolGetObject2', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'dwAvailable'),(1, 'oid'),(1, 'guidPartition'),)))
    IComObjectPool2Events.OnObjPoolRecycleToTx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64, use_last_error=False)(5, 'OnObjPoolRecycleToTx2', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'guidTx'),(1, 'objid'),)))
    IComObjectPool2Events.OnObjPoolGetFromTx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),POINTER(Guid),POINTER(Guid),UInt64,POINTER(Guid), use_last_error=False)(6, 'OnObjPoolGetFromTx2', ((1, 'pInfo'),(1, 'guidActivity'),(1, 'guidObject'),(1, 'guidTx'),(1, 'objid'),(1, 'guidPartition'),)))
    win32more.System.Com.IUnknown
    return IComObjectPool2Events
def _define_IComObjectConstruction2Events_head():
    class IComObjectConstruction2Events(win32more.System.Com.IUnknown_head):
        Guid = Guid('4b5a7827-8df2-45c0-8f6f-57ea1f856a9f')
    return IComObjectConstruction2Events
def _define_IComObjectConstruction2Events():
    IComObjectConstruction2Events = win32more.System.ComponentServices.IComObjectConstruction2Events_head
    IComObjectConstruction2Events.OnObjectConstruct2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head),POINTER(Guid),win32more.Foundation.PWSTR,UInt64,POINTER(Guid), use_last_error=False)(3, 'OnObjectConstruct2', ((1, 'pInfo'),(1, 'guidObject'),(1, 'sConstructString'),(1, 'oid'),(1, 'guidPartition'),)))
    win32more.System.Com.IUnknown
    return IComObjectConstruction2Events
def _define_ISystemAppEventData_head():
    class ISystemAppEventData(win32more.System.Com.IUnknown_head):
        Guid = Guid('d6d48a3c-d5c5-49e7-8c74-99e4889ed52f')
    return ISystemAppEventData
def _define_ISystemAppEventData():
    ISystemAppEventData = win32more.System.ComponentServices.ISystemAppEventData_head
    ISystemAppEventData.Startup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Startup', ()))
    ISystemAppEventData.OnDataChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Foundation.BSTR,UInt32,UInt64, use_last_error=False)(4, 'OnDataChanged', ((1, 'dwPID'),(1, 'dwMask'),(1, 'dwNumberSinks'),(1, 'bstrDwMethodMask'),(1, 'dwReason'),(1, 'u64TraceHandle'),)))
    win32more.System.Com.IUnknown
    return ISystemAppEventData
def _define_IMtsEvents_head():
    class IMtsEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('bacedf4d-74ab-11d0-b162-00aa00ba3258')
    return IMtsEvents
def _define_IMtsEvents():
    IMtsEvents = win32more.System.ComponentServices.IMtsEvents_head
    IMtsEvents.get_PackageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_PackageName', ((1, 'pVal'),)))
    IMtsEvents.get_PackageGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_PackageGuid', ((1, 'pVal'),)))
    IMtsEvents.PostEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'PostEvent', ((1, 'vEvent'),)))
    IMtsEvents.get_FireEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_FireEvents', ((1, 'pVal'),)))
    IMtsEvents.GetProcessID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'GetProcessID', ((1, 'id'),)))
    win32more.System.Com.IDispatch
    return IMtsEvents
def _define_IMtsEventInfo_head():
    class IMtsEventInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('d56c3dc1-8482-11d0-b170-00aa00ba3258')
    return IMtsEventInfo
def _define_IMtsEventInfo():
    IMtsEventInfo = win32more.System.ComponentServices.IMtsEventInfo_head
    IMtsEventInfo.get_Names = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get_Names', ((1, 'pUnk'),)))
    IMtsEventInfo.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_DisplayName', ((1, 'sDisplayName'),)))
    IMtsEventInfo.get_EventID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_EventID', ((1, 'sGuidEventID'),)))
    IMtsEventInfo.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Count', ((1, 'lCount'),)))
    IMtsEventInfo.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'get_Value', ((1, 'sKey'),(1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IMtsEventInfo
def _define_IMTSLocator_head():
    class IMTSLocator(win32more.System.Com.IDispatch_head):
        Guid = Guid('d19b8bfd-7f88-11d0-b16e-00aa00ba3258')
    return IMTSLocator
def _define_IMTSLocator():
    IMTSLocator = win32more.System.ComponentServices.IMTSLocator_head
    IMTSLocator.GetEventDispatcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'GetEventDispatcher', ((1, 'pUnk'),)))
    win32more.System.Com.IDispatch
    return IMTSLocator
def _define_IMtsGrp_head():
    class IMtsGrp(win32more.System.Com.IDispatch_head):
        Guid = Guid('4b2e958c-0393-11d1-b1ab-00aa00ba3258')
    return IMtsGrp
def _define_IMtsGrp():
    IMtsGrp = win32more.System.ComponentServices.IMtsGrp_head
    IMtsGrp.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'pVal'),)))
    IMtsGrp.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'Item', ((1, 'lIndex'),(1, 'ppUnkDispatcher'),)))
    IMtsGrp.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Refresh', ()))
    win32more.System.Com.IDispatch
    return IMtsGrp
def _define_IMessageMover_head():
    class IMessageMover(win32more.System.Com.IDispatch_head):
        Guid = Guid('588a085a-b795-11d1-8054-00c04fc340ee')
    return IMessageMover
def _define_IMessageMover():
    IMessageMover = win32more.System.ComponentServices.IMessageMover_head
    IMessageMover.get_SourcePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_SourcePath', ((1, 'pVal'),)))
    IMessageMover.put_SourcePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_SourcePath', ((1, 'newVal'),)))
    IMessageMover.get_DestPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DestPath', ((1, 'pVal'),)))
    IMessageMover.put_DestPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_DestPath', ((1, 'newVal'),)))
    IMessageMover.get_CommitBatchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_CommitBatchSize', ((1, 'pVal'),)))
    IMessageMover.put_CommitBatchSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_CommitBatchSize', ((1, 'newVal'),)))
    IMessageMover.MoveMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'MoveMessages', ((1, 'plMessagesMoved'),)))
    win32more.System.Com.IDispatch
    return IMessageMover
def _define_IEventServerTrace_head():
    class IEventServerTrace(win32more.System.Com.IDispatch_head):
        Guid = Guid('9a9f12b8-80af-47ab-a579-35ea57725370')
    return IEventServerTrace
def _define_IEventServerTrace():
    IEventServerTrace = win32more.System.ComponentServices.IEventServerTrace_head
    IEventServerTrace.StartTraceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(7, 'StartTraceGuid', ((1, 'bstrguidEvent'),(1, 'bstrguidFilter'),(1, 'lPidFilter'),)))
    IEventServerTrace.StopTraceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(8, 'StopTraceGuid', ((1, 'bstrguidEvent'),(1, 'bstrguidFilter'),(1, 'lPidFilter'),)))
    IEventServerTrace.EnumTraceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'EnumTraceGuid', ((1, 'plCntGuids'),(1, 'pbstrGuidList'),)))
    win32more.System.Com.IDispatch
    return IEventServerTrace
def _define_RECYCLE_INFO_head():
    class RECYCLE_INFO(Structure):
        pass
    return RECYCLE_INFO
def _define_RECYCLE_INFO():
    RECYCLE_INFO = win32more.System.ComponentServices.RECYCLE_INFO_head
    RECYCLE_INFO._fields_ = [
        ("guidCombaseProcessIdentifier", Guid),
        ("ProcessStartTime", Int64),
        ("dwRecycleLifetimeLimit", UInt32),
        ("dwRecycleMemoryLimit", UInt32),
        ("dwRecycleExpirationTimeout", UInt32),
    ]
    return RECYCLE_INFO
DUMPTYPE = Int32
DUMPTYPE_FULL = 0
DUMPTYPE_MINI = 1
DUMPTYPE_NONE = 2
def _define_HANG_INFO_head():
    class HANG_INFO(Structure):
        pass
    return HANG_INFO
def _define_HANG_INFO():
    HANG_INFO = win32more.System.ComponentServices.HANG_INFO_head
    HANG_INFO._fields_ = [
        ("fAppHangMonitorEnabled", win32more.Foundation.BOOL),
        ("fTerminateOnHang", win32more.Foundation.BOOL),
        ("DumpType", win32more.System.ComponentServices.DUMPTYPE),
        ("dwHangTimeout", UInt32),
        ("dwDumpCount", UInt32),
        ("dwInfoMsgCount", UInt32),
    ]
    return HANG_INFO
COMPLUS_APPTYPE = Int32
APPTYPE_UNKNOWN = -1
APPTYPE_SERVER = 1
APPTYPE_LIBRARY = 0
APPTYPE_SWC = 2
def _define_CAppStatistics_head():
    class CAppStatistics(Structure):
        pass
    return CAppStatistics
def _define_CAppStatistics():
    CAppStatistics = win32more.System.ComponentServices.CAppStatistics_head
    CAppStatistics._fields_ = [
        ("m_cTotalCalls", UInt32),
        ("m_cTotalInstances", UInt32),
        ("m_cTotalClasses", UInt32),
        ("m_cCallsPerSecond", UInt32),
    ]
    return CAppStatistics
def _define_CAppData_head():
    class CAppData(Structure):
        pass
    return CAppData
def _define_CAppData():
    CAppData = win32more.System.ComponentServices.CAppData_head
    CAppData._fields_ = [
        ("m_idApp", UInt32),
        ("m_szAppGuid", Char * 40),
        ("m_dwAppProcessId", UInt32),
        ("m_AppStatistics", win32more.System.ComponentServices.CAppStatistics),
    ]
    return CAppData
def _define_CCLSIDData_head():
    class CCLSIDData(Structure):
        pass
    return CCLSIDData
def _define_CCLSIDData():
    CCLSIDData = win32more.System.ComponentServices.CCLSIDData_head
    CCLSIDData._fields_ = [
        ("m_clsid", Guid),
        ("m_cReferences", UInt32),
        ("m_cBound", UInt32),
        ("m_cPooled", UInt32),
        ("m_cInCall", UInt32),
        ("m_dwRespTime", UInt32),
        ("m_cCallsCompleted", UInt32),
        ("m_cCallsFailed", UInt32),
    ]
    return CCLSIDData
def _define_CCLSIDData2_head():
    class CCLSIDData2(Structure):
        pass
    return CCLSIDData2
def _define_CCLSIDData2():
    CCLSIDData2 = win32more.System.ComponentServices.CCLSIDData2_head
    CCLSIDData2._fields_ = [
        ("m_clsid", Guid),
        ("m_appid", Guid),
        ("m_partid", Guid),
        ("m_pwszAppName", win32more.Foundation.PWSTR),
        ("m_pwszCtxName", win32more.Foundation.PWSTR),
        ("m_eAppType", win32more.System.ComponentServices.COMPLUS_APPTYPE),
        ("m_cReferences", UInt32),
        ("m_cBound", UInt32),
        ("m_cPooled", UInt32),
        ("m_cInCall", UInt32),
        ("m_dwRespTime", UInt32),
        ("m_cCallsCompleted", UInt32),
        ("m_cCallsFailed", UInt32),
    ]
    return CCLSIDData2
GetAppTrackerDataFlags = Int32
GATD_INCLUDE_PROCESS_EXE_NAME = 1
GATD_INCLUDE_LIBRARY_APPS = 2
GATD_INCLUDE_SWC = 4
GATD_INCLUDE_CLASS_NAME = 8
GATD_INCLUDE_APPLICATION_NAME = 16
def _define_ApplicationProcessSummary_head():
    class ApplicationProcessSummary(Structure):
        pass
    return ApplicationProcessSummary
def _define_ApplicationProcessSummary():
    ApplicationProcessSummary = win32more.System.ComponentServices.ApplicationProcessSummary_head
    ApplicationProcessSummary._fields_ = [
        ("PartitionIdPrimaryApplication", Guid),
        ("ApplicationIdPrimaryApplication", Guid),
        ("ApplicationInstanceId", Guid),
        ("ProcessId", UInt32),
        ("Type", win32more.System.ComponentServices.COMPLUS_APPTYPE),
        ("ProcessExeName", win32more.Foundation.PWSTR),
        ("IsService", win32more.Foundation.BOOL),
        ("IsPaused", win32more.Foundation.BOOL),
        ("IsRecycled", win32more.Foundation.BOOL),
    ]
    return ApplicationProcessSummary
def _define_ApplicationProcessStatistics_head():
    class ApplicationProcessStatistics(Structure):
        pass
    return ApplicationProcessStatistics
def _define_ApplicationProcessStatistics():
    ApplicationProcessStatistics = win32more.System.ComponentServices.ApplicationProcessStatistics_head
    ApplicationProcessStatistics._fields_ = [
        ("NumCallsOutstanding", UInt32),
        ("NumTrackedComponents", UInt32),
        ("NumComponentInstances", UInt32),
        ("AvgCallsPerSecond", UInt32),
        ("Reserved1", UInt32),
        ("Reserved2", UInt32),
        ("Reserved3", UInt32),
        ("Reserved4", UInt32),
    ]
    return ApplicationProcessStatistics
def _define_ApplicationProcessRecycleInfo_head():
    class ApplicationProcessRecycleInfo(Structure):
        pass
    return ApplicationProcessRecycleInfo
def _define_ApplicationProcessRecycleInfo():
    ApplicationProcessRecycleInfo = win32more.System.ComponentServices.ApplicationProcessRecycleInfo_head
    ApplicationProcessRecycleInfo._fields_ = [
        ("IsRecyclable", win32more.Foundation.BOOL),
        ("IsRecycled", win32more.Foundation.BOOL),
        ("TimeRecycled", win32more.Foundation.FILETIME),
        ("TimeToTerminate", win32more.Foundation.FILETIME),
        ("RecycleReasonCode", Int32),
        ("IsPendingRecycle", win32more.Foundation.BOOL),
        ("HasAutomaticLifetimeRecycling", win32more.Foundation.BOOL),
        ("TimeForAutomaticRecycling", win32more.Foundation.FILETIME),
        ("MemoryLimitInKB", UInt32),
        ("MemoryUsageInKBLastCheck", UInt32),
        ("ActivationLimit", UInt32),
        ("NumActivationsLastReported", UInt32),
        ("CallLimit", UInt32),
        ("NumCallsLastReported", UInt32),
    ]
    return ApplicationProcessRecycleInfo
def _define_ApplicationSummary_head():
    class ApplicationSummary(Structure):
        pass
    return ApplicationSummary
def _define_ApplicationSummary():
    ApplicationSummary = win32more.System.ComponentServices.ApplicationSummary_head
    ApplicationSummary._fields_ = [
        ("ApplicationInstanceId", Guid),
        ("PartitionId", Guid),
        ("ApplicationId", Guid),
        ("Type", win32more.System.ComponentServices.COMPLUS_APPTYPE),
        ("ApplicationName", win32more.Foundation.PWSTR),
        ("NumTrackedComponents", UInt32),
        ("NumComponentInstances", UInt32),
    ]
    return ApplicationSummary
def _define_ComponentSummary_head():
    class ComponentSummary(Structure):
        pass
    return ComponentSummary
def _define_ComponentSummary():
    ComponentSummary = win32more.System.ComponentServices.ComponentSummary_head
    ComponentSummary._fields_ = [
        ("ApplicationInstanceId", Guid),
        ("PartitionId", Guid),
        ("ApplicationId", Guid),
        ("Clsid", Guid),
        ("ClassName", win32more.Foundation.PWSTR),
        ("ApplicationName", win32more.Foundation.PWSTR),
    ]
    return ComponentSummary
def _define_ComponentStatistics_head():
    class ComponentStatistics(Structure):
        pass
    return ComponentStatistics
def _define_ComponentStatistics():
    ComponentStatistics = win32more.System.ComponentServices.ComponentStatistics_head
    ComponentStatistics._fields_ = [
        ("NumInstances", UInt32),
        ("NumBoundReferences", UInt32),
        ("NumPooledObjects", UInt32),
        ("NumObjectsInCall", UInt32),
        ("AvgResponseTimeInMs", UInt32),
        ("NumCallsCompletedRecent", UInt32),
        ("NumCallsFailedRecent", UInt32),
        ("NumCallsCompletedTotal", UInt32),
        ("NumCallsFailedTotal", UInt32),
        ("Reserved1", UInt32),
        ("Reserved2", UInt32),
        ("Reserved3", UInt32),
        ("Reserved4", UInt32),
    ]
    return ComponentStatistics
def _define_ComponentHangMonitorInfo_head():
    class ComponentHangMonitorInfo(Structure):
        pass
    return ComponentHangMonitorInfo
def _define_ComponentHangMonitorInfo():
    ComponentHangMonitorInfo = win32more.System.ComponentServices.ComponentHangMonitorInfo_head
    ComponentHangMonitorInfo._fields_ = [
        ("IsMonitored", win32more.Foundation.BOOL),
        ("TerminateOnHang", win32more.Foundation.BOOL),
        ("AvgCallThresholdInMs", UInt32),
    ]
    return ComponentHangMonitorInfo
def _define_IGetAppTrackerData_head():
    class IGetAppTrackerData(win32more.System.Com.IUnknown_head):
        Guid = Guid('507c3ac8-3e12-4cb0-9366-653d3e050638')
    return IGetAppTrackerData
def _define_IGetAppTrackerData():
    IGetAppTrackerData = win32more.System.ComponentServices.IGetAppTrackerData_head
    IGetAppTrackerData.GetApplicationProcesses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.ComponentServices.ApplicationProcessSummary_head)), use_last_error=False)(3, 'GetApplicationProcesses', ((1, 'PartitionId'),(1, 'ApplicationId'),(1, 'Flags'),(1, 'NumApplicationProcesses'),(1, 'ApplicationProcesses'),)))
    IGetAppTrackerData.GetApplicationProcessDetails = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.ComponentServices.ApplicationProcessSummary_head),POINTER(win32more.System.ComponentServices.ApplicationProcessStatistics_head),POINTER(win32more.System.ComponentServices.ApplicationProcessRecycleInfo_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetApplicationProcessDetails', ((1, 'ApplicationInstanceId'),(1, 'ProcessId'),(1, 'Flags'),(1, 'Summary'),(1, 'Statistics'),(1, 'RecycleInfo'),(1, 'AnyComponentsHangMonitored'),)))
    IGetAppTrackerData.GetApplicationsInProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.ComponentServices.ApplicationSummary_head)), use_last_error=False)(5, 'GetApplicationsInProcess', ((1, 'ApplicationInstanceId'),(1, 'ProcessId'),(1, 'PartitionId'),(1, 'Flags'),(1, 'NumApplicationsInProcess'),(1, 'Applications'),)))
    IGetAppTrackerData.GetComponentsInProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.ComponentServices.ComponentSummary_head)), use_last_error=False)(6, 'GetComponentsInProcess', ((1, 'ApplicationInstanceId'),(1, 'ProcessId'),(1, 'PartitionId'),(1, 'ApplicationId'),(1, 'Flags'),(1, 'NumComponentsInProcess'),(1, 'Components'),)))
    IGetAppTrackerData.GetComponentDetails = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),UInt32,POINTER(win32more.System.ComponentServices.ComponentSummary_head),POINTER(win32more.System.ComponentServices.ComponentStatistics_head),POINTER(win32more.System.ComponentServices.ComponentHangMonitorInfo_head), use_last_error=False)(7, 'GetComponentDetails', ((1, 'ApplicationInstanceId'),(1, 'ProcessId'),(1, 'Clsid'),(1, 'Flags'),(1, 'Summary'),(1, 'Statistics'),(1, 'HangMonitorInfo'),)))
    IGetAppTrackerData.GetTrackerDataAsCollectionObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'GetTrackerDataAsCollectionObject', ((1, 'TopLevelCollection'),)))
    IGetAppTrackerData.GetSuggestedPollingInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetSuggestedPollingInterval', ((1, 'PollingIntervalInSeconds'),)))
    win32more.System.Com.IUnknown
    return IGetAppTrackerData
def _define_IDispenserManager_head():
    class IDispenserManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('5cb31e10-2b5f-11cf-be10-00aa00a2fa25')
    return IDispenserManager
def _define_IDispenserManager():
    IDispenserManager = win32more.System.ComponentServices.IDispenserManager_head
    IDispenserManager.RegisterDispenser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IDispenserDriver_head,win32more.Foundation.PWSTR,POINTER(win32more.System.ComponentServices.IHolder_head), use_last_error=False)(3, 'RegisterDispenser', ((1, '__MIDL__IDispenserManager0000'),(1, 'szDispenserName'),(1, '__MIDL__IDispenserManager0001'),)))
    IDispenserManager.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=False)(4, 'GetContext', ((1, '__MIDL__IDispenserManager0002'),(1, '__MIDL__IDispenserManager0003'),)))
    win32more.System.Com.IUnknown
    return IDispenserManager
def _define_IHolder_head():
    class IHolder(win32more.System.Com.IUnknown_head):
        Guid = Guid('bf6a1850-2b45-11cf-be10-00aa00a2fa25')
    return IHolder
def _define_IHolder():
    IHolder = win32more.System.ComponentServices.IHolder_head
    IHolder.AllocResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(UIntPtr), use_last_error=False)(3, 'AllocResource', ((1, '__MIDL__IHolder0000'),(1, '__MIDL__IHolder0001'),)))
    IHolder.FreeResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(4, 'FreeResource', ((1, '__MIDL__IHolder0002'),)))
    IHolder.TrackResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(5, 'TrackResource', ((1, '__MIDL__IHolder0003'),)))
    IHolder.TrackResourceS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(6, 'TrackResourceS', ((1, '__MIDL__IHolder0004'),)))
    IHolder.UntrackResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.Foundation.BOOL, use_last_error=False)(7, 'UntrackResource', ((1, '__MIDL__IHolder0005'),(1, '__MIDL__IHolder0006'),)))
    IHolder.UntrackResourceS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),win32more.Foundation.BOOL, use_last_error=False)(8, 'UntrackResourceS', ((1, '__MIDL__IHolder0007'),(1, '__MIDL__IHolder0008'),)))
    IHolder.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Close', ()))
    IHolder.RequestDestroyResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(10, 'RequestDestroyResource', ((1, '__MIDL__IHolder0009'),)))
    win32more.System.Com.IUnknown
    return IHolder
def _define_IDispenserDriver_head():
    class IDispenserDriver(win32more.System.Com.IUnknown_head):
        Guid = Guid('208b3651-2b48-11cf-be10-00aa00a2fa25')
    return IDispenserDriver
def _define_IDispenserDriver():
    IDispenserDriver = win32more.System.ComponentServices.IDispenserDriver_head
    IDispenserDriver.CreateResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(UIntPtr),POINTER(Int32), use_last_error=False)(3, 'CreateResource', ((1, 'ResTypId'),(1, 'pResId'),(1, 'pSecsFreeBeforeDestroy'),)))
    IDispenserDriver.RateResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(4, 'RateResource', ((1, 'ResTypId'),(1, 'ResId'),(1, 'fRequiresTransactionEnlistment'),(1, 'pRating'),)))
    IDispenserDriver.EnlistResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr, use_last_error=False)(5, 'EnlistResource', ((1, 'ResId'),(1, 'TransId'),)))
    IDispenserDriver.ResetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(6, 'ResetResource', ((1, 'ResId'),)))
    IDispenserDriver.DestroyResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(7, 'DestroyResource', ((1, 'ResId'),)))
    IDispenserDriver.DestroyResourceS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(8, 'DestroyResourceS', ((1, 'ResId'),)))
    win32more.System.Com.IUnknown
    return IDispenserDriver
def _define_ITransactionProxy_head():
    class ITransactionProxy(win32more.System.Com.IUnknown_head):
        Guid = Guid('02558374-df2e-4dae-bd6b-1d5c994f9bdc')
    return ITransactionProxy
def _define_ITransactionProxy():
    ITransactionProxy = win32more.System.ComponentServices.ITransactionProxy_head
    ITransactionProxy.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(3, 'Commit', ((1, 'guid'),)))
    ITransactionProxy.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Abort', ()))
    ITransactionProxy.Promote = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head), use_last_error=False)(5, 'Promote', ((1, 'pTransaction'),)))
    ITransactionProxy.CreateVoter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head,POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head), use_last_error=False)(6, 'CreateVoter', ((1, 'pTxAsync'),(1, 'ppBallot'),)))
    ITransactionProxy.GetIsolationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'GetIsolationLevel', ((1, '__MIDL__ITransactionProxy0000'),)))
    ITransactionProxy.GetIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'GetIdentifier', ((1, 'pbstrIdentifier'),)))
    ITransactionProxy.IsReusable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'IsReusable', ((1, 'pfIsReusable'),)))
    win32more.System.Com.IUnknown
    return ITransactionProxy
def _define_IContextSecurityPerimeter_head():
    class IContextSecurityPerimeter(win32more.System.Com.IUnknown_head):
        Guid = Guid('a7549a29-a7c4-42e1-8dc1-7e3d748dc24a')
    return IContextSecurityPerimeter
def _define_IContextSecurityPerimeter():
    IContextSecurityPerimeter = win32more.System.ComponentServices.IContextSecurityPerimeter_head
    IContextSecurityPerimeter.GetPerimeterFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetPerimeterFlag', ((1, 'pFlag'),)))
    IContextSecurityPerimeter.SetPerimeterFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetPerimeterFlag', ((1, 'fFlag'),)))
    win32more.System.Com.IUnknown
    return IContextSecurityPerimeter
def _define_ITxProxyHolder_head():
    class ITxProxyHolder(win32more.System.Com.IUnknown_head):
        Guid = Guid('13d86f31-0139-41af-bcad-c7d50435fe9f')
    return ITxProxyHolder
def _define_ITxProxyHolder():
    ITxProxyHolder = win32more.System.ComponentServices.ITxProxyHolder_head
    ITxProxyHolder.GetIdentifier = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid), use_last_error=False)(3, 'GetIdentifier', ((1, 'pGuidLtx'),)))
    win32more.System.Com.IUnknown
    return ITxProxyHolder
def _define_IObjectContext_head():
    class IObjectContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372ae0-cae7-11cf-be81-00aa00a2fa25')
    return IObjectContext
def _define_IObjectContext():
    IObjectContext = win32more.System.ComponentServices.IObjectContext_head
    IObjectContext.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateInstance', ((1, 'rclsid'),(1, 'riid'),(1, 'ppv'),)))
    IObjectContext.SetComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'SetComplete', ()))
    IObjectContext.SetAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'SetAbort', ()))
    IObjectContext.EnableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'EnableCommit', ()))
    IObjectContext.DisableCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'DisableCommit', ()))
    IObjectContext.IsInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(8, 'IsInTransaction', ()))
    IObjectContext.IsSecurityEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(9, 'IsSecurityEnabled', ()))
    IObjectContext.IsCallerInRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsCallerInRole', ((1, 'bstrRole'),(1, 'pfIsInRole'),)))
    win32more.System.Com.IUnknown
    return IObjectContext
def _define_IObjectControl_head():
    class IObjectControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372aec-cae7-11cf-be81-00aa00a2fa25')
    return IObjectControl
def _define_IObjectControl():
    IObjectControl = win32more.System.ComponentServices.IObjectControl_head
    IObjectControl.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Activate', ()))
    IObjectControl.Deactivate = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'Deactivate', ()))
    IObjectControl.CanBePooled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(5, 'CanBePooled', ()))
    win32more.System.Com.IUnknown
    return IObjectControl
def _define_IEnumNames_head():
    class IEnumNames(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372af2-cae7-11cf-be81-00aa00a2fa25')
    return IEnumNames
def _define_IEnumNames():
    IEnumNames = win32more.System.ComponentServices.IEnumNames_head
    IEnumNames.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgname'),(1, 'pceltFetched'),)))
    IEnumNames.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNames.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNames.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.IEnumNames_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNames
def _define_ISecurityProperty_head():
    class ISecurityProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372aea-cae7-11cf-be81-00aa00a2fa25')
    return ISecurityProperty
def _define_ISecurityProperty():
    ISecurityProperty = win32more.System.ComponentServices.ISecurityProperty_head
    ISecurityProperty.GetDirectCreatorSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSID), use_last_error=False)(3, 'GetDirectCreatorSID', ((1, 'pSID'),)))
    ISecurityProperty.GetOriginalCreatorSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSID), use_last_error=False)(4, 'GetOriginalCreatorSID', ((1, 'pSID'),)))
    ISecurityProperty.GetDirectCallerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSID), use_last_error=False)(5, 'GetDirectCallerSID', ((1, 'pSID'),)))
    ISecurityProperty.GetOriginalCallerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSID), use_last_error=False)(6, 'GetOriginalCallerSID', ((1, 'pSID'),)))
    ISecurityProperty.ReleaseSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID, use_last_error=False)(7, 'ReleaseSID', ((1, 'pSID'),)))
    win32more.System.Com.IUnknown
    return ISecurityProperty
def _define_ObjectControl_head():
    class ObjectControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('7dc41850-0c31-11d0-8b79-00aa00b8a790')
    return ObjectControl
def _define_ObjectControl():
    ObjectControl = win32more.System.ComponentServices.ObjectControl_head
    ObjectControl.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Activate', ()))
    ObjectControl.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Deactivate', ()))
    ObjectControl.CanBePooled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(5, 'CanBePooled', ((1, 'pbPoolable'),)))
    win32more.System.Com.IUnknown
    return ObjectControl
def _define_ISharedProperty_head():
    class ISharedProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('2a005c01-a5de-11cf-9e66-00aa00a3f464')
    return ISharedProperty
def _define_ISharedProperty():
    ISharedProperty = win32more.System.ComponentServices.ISharedProperty_head
    ISharedProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'pVal'),)))
    ISharedProperty.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Value', ((1, 'val'),)))
    win32more.System.Com.IDispatch
    return ISharedProperty
def _define_ISharedPropertyGroup_head():
    class ISharedPropertyGroup(win32more.System.Com.IDispatch_head):
        Guid = Guid('2a005c07-a5de-11cf-9e66-00aa00a3f464')
    return ISharedPropertyGroup
def _define_ISharedPropertyGroup():
    ISharedPropertyGroup = win32more.System.ComponentServices.ISharedPropertyGroup_head
    ISharedPropertyGroup.CreatePropertyByPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int16),POINTER(win32more.System.ComponentServices.ISharedProperty_head), use_last_error=False)(7, 'CreatePropertyByPosition', ((1, 'Index'),(1, 'fExists'),(1, 'ppProp'),)))
    ISharedPropertyGroup.get_PropertyByPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.ComponentServices.ISharedProperty_head), use_last_error=False)(8, 'get_PropertyByPosition', ((1, 'Index'),(1, 'ppProperty'),)))
    ISharedPropertyGroup.CreateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16),POINTER(win32more.System.ComponentServices.ISharedProperty_head), use_last_error=False)(9, 'CreateProperty', ((1, 'Name'),(1, 'fExists'),(1, 'ppProp'),)))
    ISharedPropertyGroup.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.ComponentServices.ISharedProperty_head), use_last_error=False)(10, 'get_Property', ((1, 'Name'),(1, 'ppProperty'),)))
    win32more.System.Com.IDispatch
    return ISharedPropertyGroup
def _define_ISharedPropertyGroupManager_head():
    class ISharedPropertyGroupManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('2a005c0d-a5de-11cf-9e66-00aa00a3f464')
    return ISharedPropertyGroupManager
def _define_ISharedPropertyGroupManager():
    ISharedPropertyGroupManager = win32more.System.ComponentServices.ISharedPropertyGroupManager_head
    ISharedPropertyGroupManager.CreatePropertyGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(Int32),POINTER(Int16),POINTER(win32more.System.ComponentServices.ISharedPropertyGroup_head), use_last_error=False)(7, 'CreatePropertyGroup', ((1, 'Name'),(1, 'dwIsoMode'),(1, 'dwRelMode'),(1, 'fExists'),(1, 'ppGroup'),)))
    ISharedPropertyGroupManager.get_Group = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.ComponentServices.ISharedPropertyGroup_head), use_last_error=False)(8, 'get_Group', ((1, 'Name'),(1, 'ppGroup'),)))
    ISharedPropertyGroupManager.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ISharedPropertyGroupManager
def _define_IObjectConstruct_head():
    class IObjectConstruct(win32more.System.Com.IUnknown_head):
        Guid = Guid('41c4f8b3-7439-11d2-98cb-00c04f8ee1c4')
    return IObjectConstruct
def _define_IObjectConstruct():
    IObjectConstruct = win32more.System.ComponentServices.IObjectConstruct_head
    IObjectConstruct.Construct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(3, 'Construct', ((1, 'pCtorObj'),)))
    win32more.System.Com.IUnknown
    return IObjectConstruct
def _define_IObjectConstructString_head():
    class IObjectConstructString(win32more.System.Com.IDispatch_head):
        Guid = Guid('41c4f8b2-7439-11d2-98cb-00c04f8ee1c4')
    return IObjectConstructString
def _define_IObjectConstructString():
    IObjectConstructString = win32more.System.ComponentServices.IObjectConstructString_head
    IObjectConstructString.get_ConstructString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ConstructString', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IObjectConstructString
def _define_IObjectContextActivity_head():
    class IObjectContextActivity(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372afc-cae7-11cf-be81-00aa00a2fa25')
    return IObjectContextActivity
def _define_IObjectContextActivity():
    IObjectContextActivity = win32more.System.ComponentServices.IObjectContextActivity_head
    IObjectContextActivity.GetActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetActivityId', ((1, 'pGUID'),)))
    win32more.System.Com.IUnknown
    return IObjectContextActivity
def _define_IObjectContextInfo_head():
    class IObjectContextInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('75b52ddb-e8ed-11d1-93ad-00aa00ba3258')
    return IObjectContextInfo
def _define_IObjectContextInfo():
    IObjectContextInfo = win32more.System.ComponentServices.IObjectContextInfo_head
    IObjectContextInfo.IsInTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(3, 'IsInTransaction', ()))
    IObjectContextInfo.GetTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'GetTransaction', ((1, 'pptrans'),)))
    IObjectContextInfo.GetTransactionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetTransactionId', ((1, 'pGuid'),)))
    IObjectContextInfo.GetActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'GetActivityId', ((1, 'pGUID'),)))
    IObjectContextInfo.GetContextId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'GetContextId', ((1, 'pGuid'),)))
    win32more.System.Com.IUnknown
    return IObjectContextInfo
def _define_IObjectContextInfo2_head():
    class IObjectContextInfo2(win32more.System.ComponentServices.IObjectContextInfo_head):
        Guid = Guid('594be71a-4bc4-438b-9197-cfd176248b09')
    return IObjectContextInfo2
def _define_IObjectContextInfo2():
    IObjectContextInfo2 = win32more.System.ComponentServices.IObjectContextInfo2_head
    IObjectContextInfo2.GetPartitionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'GetPartitionId', ((1, 'pGuid'),)))
    IObjectContextInfo2.GetApplicationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(9, 'GetApplicationId', ((1, 'pGuid'),)))
    IObjectContextInfo2.GetApplicationInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'GetApplicationInstanceId', ((1, 'pGuid'),)))
    win32more.System.ComponentServices.IObjectContextInfo
    return IObjectContextInfo2
def _define_ITransactionStatus_head():
    class ITransactionStatus(win32more.System.Com.IUnknown_head):
        Guid = Guid('61f589e8-3724-4898-a0a4-664ae9e1d1b4')
    return ITransactionStatus
def _define_ITransactionStatus():
    ITransactionStatus = win32more.System.ComponentServices.ITransactionStatus_head
    ITransactionStatus.SetTransactionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'SetTransactionStatus', ((1, 'hrStatus'),)))
    ITransactionStatus.GetTransactionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(4, 'GetTransactionStatus', ((1, 'pHrStatus'),)))
    win32more.System.Com.IUnknown
    return ITransactionStatus
def _define_IObjectContextTip_head():
    class IObjectContextTip(win32more.System.Com.IUnknown_head):
        Guid = Guid('92fd41ca-bad9-11d2-9a2d-00c04f797bc9')
    return IObjectContextTip
def _define_IObjectContextTip():
    IObjectContextTip = win32more.System.ComponentServices.IObjectContextTip_head
    IObjectContextTip.GetTipUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetTipUrl', ((1, 'pTipUrl'),)))
    win32more.System.Com.IUnknown
    return IObjectContextTip
def _define_IPlaybackControl_head():
    class IPlaybackControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372afd-cae7-11cf-be81-00aa00a2fa25')
    return IPlaybackControl
def _define_IPlaybackControl():
    IPlaybackControl = win32more.System.ComponentServices.IPlaybackControl_head
    IPlaybackControl.FinalClientRetry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'FinalClientRetry', ()))
    IPlaybackControl.FinalServerRetry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'FinalServerRetry', ()))
    win32more.System.Com.IUnknown
    return IPlaybackControl
def _define_IGetContextProperties_head():
    class IGetContextProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372af4-cae7-11cf-be81-00aa00a2fa25')
    return IGetContextProperties
def _define_IGetContextProperties():
    IGetContextProperties = win32more.System.ComponentServices.IGetContextProperties_head
    IGetContextProperties.Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'Count', ((1, 'plCount'),)))
    IGetContextProperties.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'GetProperty', ((1, 'name'),(1, 'pProperty'),)))
    IGetContextProperties.EnumNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.IEnumNames_head), use_last_error=False)(5, 'EnumNames', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IGetContextProperties
TransactionVote = Int32
TransactionVote_TxCommit = 0
TransactionVote_TxAbort = 1
def _define_IContextState_head():
    class IContextState(win32more.System.Com.IUnknown_head):
        Guid = Guid('3c05e54b-a42a-11d2-afc4-00c04f8ee1c4')
    return IContextState
def _define_IContextState():
    IContextState = win32more.System.ComponentServices.IContextState_head
    IContextState.SetDeactivateOnReturn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(3, 'SetDeactivateOnReturn', ((1, 'bDeactivate'),)))
    IContextState.GetDeactivateOnReturn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(4, 'GetDeactivateOnReturn', ((1, 'pbDeactivate'),)))
    IContextState.SetMyTransactionVote = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.TransactionVote, use_last_error=False)(5, 'SetMyTransactionVote', ((1, 'txVote'),)))
    IContextState.GetMyTransactionVote = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.TransactionVote), use_last_error=False)(6, 'GetMyTransactionVote', ((1, 'ptxVote'),)))
    win32more.System.Com.IUnknown
    return IContextState
def _define_IPoolManager_head():
    class IPoolManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('0a469861-5a91-43a0-99b6-d5e179bb0631')
    return IPoolManager
def _define_IPoolManager():
    IPoolManager = win32more.System.ComponentServices.IPoolManager_head
    IPoolManager.ShutdownPool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'ShutdownPool', ((1, 'CLSIDOrProgID'),)))
    win32more.System.Com.IDispatch
    return IPoolManager
def _define_ISelectCOMLBServer_head():
    class ISelectCOMLBServer(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcf443f4-3f8a-4872-b9f0-369a796d12d6')
    return ISelectCOMLBServer
def _define_ISelectCOMLBServer():
    ISelectCOMLBServer = win32more.System.ComponentServices.ISelectCOMLBServer_head
    ISelectCOMLBServer.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Init', ()))
    ISelectCOMLBServer.GetLBServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'GetLBServer', ((1, 'pUnk'),)))
    win32more.System.Com.IUnknown
    return ISelectCOMLBServer
def _define_ICOMLBArguments_head():
    class ICOMLBArguments(win32more.System.Com.IUnknown_head):
        Guid = Guid('3a0f150f-8ee5-4b94-b40e-aef2f9e42ed2')
    return ICOMLBArguments
def _define_ICOMLBArguments():
    ICOMLBArguments = win32more.System.ComponentServices.ICOMLBArguments_head
    ICOMLBArguments.GetCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetCLSID', ((1, 'pCLSID'),)))
    ICOMLBArguments.SetCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'SetCLSID', ((1, 'pCLSID'),)))
    ICOMLBArguments.GetMachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char), use_last_error=False)(5, 'GetMachineName', ((1, 'cchSvr'),(1, 'szServerName'),)))
    ICOMLBArguments.SetMachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char), use_last_error=False)(6, 'SetMachineName', ((1, 'cchSvr'),(1, 'szServerName'),)))
    win32more.System.Com.IUnknown
    return ICOMLBArguments
def _define_ICrmLogControl_head():
    class ICrmLogControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('a0e174b3-d26e-11d2-8f84-00805fc7bcd9')
    return ICrmLogControl
def _define_ICrmLogControl():
    ICrmLogControl = win32more.System.ComponentServices.ICrmLogControl_head
    ICrmLogControl.get_TransactionUOW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_TransactionUOW', ((1, 'pVal'),)))
    ICrmLogControl.RegisterCompensator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(4, 'RegisterCompensator', ((1, 'lpcwstrProgIdCompensator'),(1, 'lpcwstrDescription'),(1, 'lCrmRegFlags'),)))
    ICrmLogControl.WriteLogRecordVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'WriteLogRecordVariants', ((1, 'pLogRecord'),)))
    ICrmLogControl.ForceLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'ForceLog', ()))
    ICrmLogControl.ForgetLogRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ForgetLogRecord', ()))
    ICrmLogControl.ForceTransactionToAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'ForceTransactionToAbort', ()))
    ICrmLogControl.WriteLogRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.BLOB),UInt32, use_last_error=False)(9, 'WriteLogRecord', ((1, 'rgBlob'),(1, 'cBlob'),)))
    win32more.System.Com.IUnknown
    return ICrmLogControl
def _define_ICrmCompensatorVariants_head():
    class ICrmCompensatorVariants(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0baf8e4-7804-11d1-82e9-00a0c91eede9')
    return ICrmCompensatorVariants
def _define_ICrmCompensatorVariants():
    ICrmCompensatorVariants = win32more.System.ComponentServices.ICrmCompensatorVariants_head
    ICrmCompensatorVariants.SetLogControlVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.ICrmLogControl_head, use_last_error=False)(3, 'SetLogControlVariants', ((1, 'pLogControl'),)))
    ICrmCompensatorVariants.BeginPrepareVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BeginPrepareVariants', ()))
    ICrmCompensatorVariants.PrepareRecordVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(5, 'PrepareRecordVariants', ((1, 'pLogRecord'),(1, 'pbForget'),)))
    ICrmCompensatorVariants.EndPrepareVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(6, 'EndPrepareVariants', ((1, 'pbOkToPrepare'),)))
    ICrmCompensatorVariants.BeginCommitVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(7, 'BeginCommitVariants', ((1, 'bRecovery'),)))
    ICrmCompensatorVariants.CommitRecordVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(8, 'CommitRecordVariants', ((1, 'pLogRecord'),(1, 'pbForget'),)))
    ICrmCompensatorVariants.EndCommitVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'EndCommitVariants', ()))
    ICrmCompensatorVariants.BeginAbortVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'BeginAbortVariants', ((1, 'bRecovery'),)))
    ICrmCompensatorVariants.AbortRecordVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(11, 'AbortRecordVariants', ((1, 'pLogRecord'),(1, 'pbForget'),)))
    ICrmCompensatorVariants.EndAbortVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'EndAbortVariants', ()))
    win32more.System.Com.IUnknown
    return ICrmCompensatorVariants
def _define_CrmLogRecordRead_head():
    class CrmLogRecordRead(Structure):
        pass
    return CrmLogRecordRead
def _define_CrmLogRecordRead():
    CrmLogRecordRead = win32more.System.ComponentServices.CrmLogRecordRead_head
    CrmLogRecordRead._fields_ = [
        ("dwCrmFlags", UInt32),
        ("dwSequenceNumber", UInt32),
        ("blobUserData", win32more.System.Com.BLOB),
    ]
    return CrmLogRecordRead
def _define_ICrmCompensator_head():
    class ICrmCompensator(win32more.System.Com.IUnknown_head):
        Guid = Guid('bbc01830-8d3b-11d1-82ec-00a0c91eede9')
    return ICrmCompensator
def _define_ICrmCompensator():
    ICrmCompensator = win32more.System.ComponentServices.ICrmCompensator_head
    ICrmCompensator.SetLogControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.ICrmLogControl_head, use_last_error=False)(3, 'SetLogControl', ((1, 'pLogControl'),)))
    ICrmCompensator.BeginPrepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BeginPrepare', ()))
    ICrmCompensator.PrepareRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CrmLogRecordRead,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'PrepareRecord', ((1, 'crmLogRec'),(1, 'pfForget'),)))
    ICrmCompensator.EndPrepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'EndPrepare', ((1, 'pfOkToPrepare'),)))
    ICrmCompensator.BeginCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'BeginCommit', ((1, 'fRecovery'),)))
    ICrmCompensator.CommitRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CrmLogRecordRead,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'CommitRecord', ((1, 'crmLogRec'),(1, 'pfForget'),)))
    ICrmCompensator.EndCommit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'EndCommit', ()))
    ICrmCompensator.BeginAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'BeginAbort', ((1, 'fRecovery'),)))
    ICrmCompensator.AbortRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CrmLogRecordRead,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'AbortRecord', ((1, 'crmLogRec'),(1, 'pfForget'),)))
    ICrmCompensator.EndAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'EndAbort', ()))
    win32more.System.Com.IUnknown
    return ICrmCompensator
CrmTransactionState = Int32
TxState_Active = 0
TxState_Committed = 1
TxState_Aborted = 2
TxState_Indoubt = 3
def _define_ICrmMonitorLogRecords_head():
    class ICrmMonitorLogRecords(win32more.System.Com.IUnknown_head):
        Guid = Guid('70c8e441-c7ed-11d1-82fb-00a0c91eede9')
    return ICrmMonitorLogRecords
def _define_ICrmMonitorLogRecords():
    ICrmMonitorLogRecords = win32more.System.ComponentServices.ICrmMonitorLogRecords_head
    ICrmMonitorLogRecords.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Count', ((1, 'pVal'),)))
    ICrmMonitorLogRecords.get_TransactionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.CrmTransactionState), use_last_error=False)(4, 'get_TransactionState', ((1, 'pVal'),)))
    ICrmMonitorLogRecords.get_StructuredRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(5, 'get_StructuredRecords', ((1, 'pVal'),)))
    ICrmMonitorLogRecords.GetLogRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.ComponentServices.CrmLogRecordRead_head), use_last_error=False)(6, 'GetLogRecord', ((1, 'dwIndex'),(1, 'pCrmLogRec'),)))
    ICrmMonitorLogRecords.GetLogRecordVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'GetLogRecordVariants', ((1, 'IndexNumber'),(1, 'pLogRecord'),)))
    win32more.System.Com.IUnknown
    return ICrmMonitorLogRecords
def _define_ICrmMonitorClerks_head():
    class ICrmMonitorClerks(win32more.System.Com.IDispatch_head):
        Guid = Guid('70c8e442-c7ed-11d1-82fb-00a0c91eede9')
    return ICrmMonitorClerks
def _define_ICrmMonitorClerks():
    ICrmMonitorClerks = win32more.System.ComponentServices.ICrmMonitorClerks_head
    ICrmMonitorClerks.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'pItem'),)))
    ICrmMonitorClerks.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'pVal'),)))
    ICrmMonitorClerks.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'pVal'),)))
    ICrmMonitorClerks.ProgIdCompensator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'ProgIdCompensator', ((1, 'Index'),(1, 'pItem'),)))
    ICrmMonitorClerks.Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'Description', ((1, 'Index'),(1, 'pItem'),)))
    ICrmMonitorClerks.TransactionUOW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'TransactionUOW', ((1, 'Index'),(1, 'pItem'),)))
    ICrmMonitorClerks.ActivityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'ActivityId', ((1, 'Index'),(1, 'pItem'),)))
    win32more.System.Com.IDispatch
    return ICrmMonitorClerks
def _define_ICrmMonitor_head():
    class ICrmMonitor(win32more.System.Com.IUnknown_head):
        Guid = Guid('70c8e443-c7ed-11d1-82fb-00a0c91eede9')
    return ICrmMonitor
def _define_ICrmMonitor():
    ICrmMonitor = win32more.System.ComponentServices.ICrmMonitor_head
    ICrmMonitor.GetClerks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.ICrmMonitorClerks_head), use_last_error=False)(3, 'GetClerks', ((1, 'pClerks'),)))
    ICrmMonitor.HoldClerk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'HoldClerk', ((1, 'Index'),(1, 'pItem'),)))
    win32more.System.Com.IUnknown
    return ICrmMonitor
def _define_ICrmFormatLogRecords_head():
    class ICrmFormatLogRecords(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c51d821-c98b-11d1-82fb-00a0c91eede9')
    return ICrmFormatLogRecords
def _define_ICrmFormatLogRecords():
    ICrmFormatLogRecords = win32more.System.ComponentServices.ICrmFormatLogRecords_head
    ICrmFormatLogRecords.GetColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'GetColumnCount', ((1, 'plColumnCount'),)))
    ICrmFormatLogRecords.GetColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'GetColumnHeaders', ((1, 'pHeaders'),)))
    ICrmFormatLogRecords.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CrmLogRecordRead,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'GetColumn', ((1, 'CrmLogRec'),(1, 'pFormattedLogRecord'),)))
    ICrmFormatLogRecords.GetColumnVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(6, 'GetColumnVariants', ((1, 'LogRecord'),(1, 'pFormattedLogRecord'),)))
    win32more.System.Com.IUnknown
    return ICrmFormatLogRecords
CSC_InheritanceConfig = Int32
CSC_Inherit = 0
CSC_Ignore = 1
CSC_ThreadPool = Int32
CSC_ThreadPoolNone = 0
CSC_ThreadPoolInherit = 1
CSC_STAThreadPool = 2
CSC_MTAThreadPool = 3
CSC_Binding = Int32
CSC_NoBinding = 0
CSC_BindToPoolThread = 1
CSC_TransactionConfig = Int32
CSC_NoTransaction = 0
CSC_IfContainerIsTransactional = 1
CSC_CreateTransactionIfNecessary = 2
CSC_NewTransaction = 3
CSC_SynchronizationConfig = Int32
CSC_NoSynchronization = 0
CSC_IfContainerIsSynchronized = 1
CSC_NewSynchronizationIfNecessary = 2
CSC_NewSynchronization = 3
CSC_TrackerConfig = Int32
CSC_DontUseTracker = 0
CSC_UseTracker = 1
CSC_PartitionConfig = Int32
CSC_NoPartition = 0
CSC_InheritPartition = 1
CSC_NewPartition = 2
CSC_IISIntrinsicsConfig = Int32
CSC_NoIISIntrinsics = 0
CSC_InheritIISIntrinsics = 1
CSC_COMTIIntrinsicsConfig = Int32
CSC_NoCOMTIIntrinsics = 0
CSC_InheritCOMTIIntrinsics = 1
CSC_SxsConfig = Int32
CSC_NoSxs = 0
CSC_InheritSxs = 1
CSC_NewSxs = 2
def _define_IServiceIISIntrinsicsConfig_head():
    class IServiceIISIntrinsicsConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a0cf920-d452-46f4-bc36-48118d54ea52')
    return IServiceIISIntrinsicsConfig
def _define_IServiceIISIntrinsicsConfig():
    IServiceIISIntrinsicsConfig = win32more.System.ComponentServices.IServiceIISIntrinsicsConfig_head
    IServiceIISIntrinsicsConfig.IISIntrinsicsConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_IISIntrinsicsConfig, use_last_error=False)(3, 'IISIntrinsicsConfig', ((1, 'iisIntrinsicsConfig'),)))
    win32more.System.Com.IUnknown
    return IServiceIISIntrinsicsConfig
def _define_IServiceComTIIntrinsicsConfig_head():
    class IServiceComTIIntrinsicsConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('09e6831e-04e1-4ed4-9d0f-e8b168bafeaf')
    return IServiceComTIIntrinsicsConfig
def _define_IServiceComTIIntrinsicsConfig():
    IServiceComTIIntrinsicsConfig = win32more.System.ComponentServices.IServiceComTIIntrinsicsConfig_head
    IServiceComTIIntrinsicsConfig.ComTIIntrinsicsConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_COMTIIntrinsicsConfig, use_last_error=False)(3, 'ComTIIntrinsicsConfig', ((1, 'comtiIntrinsicsConfig'),)))
    win32more.System.Com.IUnknown
    return IServiceComTIIntrinsicsConfig
def _define_IServiceSxsConfig_head():
    class IServiceSxsConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7cd7379-f3f2-4634-811b-703281d73e08')
    return IServiceSxsConfig
def _define_IServiceSxsConfig():
    IServiceSxsConfig = win32more.System.ComponentServices.IServiceSxsConfig_head
    IServiceSxsConfig.SxsConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_SxsConfig, use_last_error=False)(3, 'SxsConfig', ((1, 'scsConfig'),)))
    IServiceSxsConfig.SxsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SxsName', ((1, 'szSxsName'),)))
    IServiceSxsConfig.SxsDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SxsDirectory', ((1, 'szSxsDirectory'),)))
    win32more.System.Com.IUnknown
    return IServiceSxsConfig
def _define_ICheckSxsConfig_head():
    class ICheckSxsConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ff5a96f-11fc-47d1-baa6-25dd347e7242')
    return ICheckSxsConfig
def _define_ICheckSxsConfig():
    ICheckSxsConfig = win32more.System.ComponentServices.ICheckSxsConfig_head
    ICheckSxsConfig.IsSameSxsConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'IsSameSxsConfig', ((1, 'wszSxsName'),(1, 'wszSxsDirectory'),(1, 'wszSxsAppName'),)))
    win32more.System.Com.IUnknown
    return ICheckSxsConfig
def _define_IServiceInheritanceConfig_head():
    class IServiceInheritanceConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('92186771-d3b4-4d77-a8ea-ee842d586f35')
    return IServiceInheritanceConfig
def _define_IServiceInheritanceConfig():
    IServiceInheritanceConfig = win32more.System.ComponentServices.IServiceInheritanceConfig_head
    IServiceInheritanceConfig.ContainingContextTreatment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_InheritanceConfig, use_last_error=False)(3, 'ContainingContextTreatment', ((1, 'inheritanceConfig'),)))
    win32more.System.Com.IUnknown
    return IServiceInheritanceConfig
def _define_IServiceThreadPoolConfig_head():
    class IServiceThreadPoolConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('186d89bc-f277-4bcc-80d5-4df7b836ef4a')
    return IServiceThreadPoolConfig
def _define_IServiceThreadPoolConfig():
    IServiceThreadPoolConfig = win32more.System.ComponentServices.IServiceThreadPoolConfig_head
    IServiceThreadPoolConfig.SelectThreadPool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_ThreadPool, use_last_error=False)(3, 'SelectThreadPool', ((1, 'threadPool'),)))
    IServiceThreadPoolConfig.SetBindingInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_Binding, use_last_error=False)(4, 'SetBindingInfo', ((1, 'binding'),)))
    win32more.System.Com.IUnknown
    return IServiceThreadPoolConfig
def _define_IServiceTransactionConfigBase_head():
    class IServiceTransactionConfigBase(win32more.System.Com.IUnknown_head):
        Guid = Guid('772b3fbe-6ffd-42fb-b5f8-8f9b260f3810')
    return IServiceTransactionConfigBase
def _define_IServiceTransactionConfigBase():
    IServiceTransactionConfigBase = win32more.System.ComponentServices.IServiceTransactionConfigBase_head
    IServiceTransactionConfigBase.ConfigureTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_TransactionConfig, use_last_error=False)(3, 'ConfigureTransaction', ((1, 'transactionConfig'),)))
    IServiceTransactionConfigBase.IsolationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.COMAdminTxIsolationLevelOptions, use_last_error=False)(4, 'IsolationLevel', ((1, 'option'),)))
    IServiceTransactionConfigBase.TransactionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'TransactionTimeout', ((1, 'ulTimeoutSec'),)))
    IServiceTransactionConfigBase.BringYourOwnTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'BringYourOwnTransaction', ((1, 'szTipURL'),)))
    IServiceTransactionConfigBase.NewTransactionDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'NewTransactionDescription', ((1, 'szTxDesc'),)))
    win32more.System.Com.IUnknown
    return IServiceTransactionConfigBase
def _define_IServiceTransactionConfig_head():
    class IServiceTransactionConfig(win32more.System.ComponentServices.IServiceTransactionConfigBase_head):
        Guid = Guid('59f4c2a3-d3d7-4a31-b6e4-6ab3177c50b9')
    return IServiceTransactionConfig
def _define_IServiceTransactionConfig():
    IServiceTransactionConfig = win32more.System.ComponentServices.IServiceTransactionConfig_head
    IServiceTransactionConfig.ConfigureBYOT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DistributedTransactionCoordinator.ITransaction_head, use_last_error=False)(8, 'ConfigureBYOT', ((1, 'pITxByot'),)))
    win32more.System.ComponentServices.IServiceTransactionConfigBase
    return IServiceTransactionConfig
def _define_IServiceSysTxnConfig_head():
    class IServiceSysTxnConfig(win32more.System.ComponentServices.IServiceTransactionConfig_head):
        Guid = Guid('33caf1a1-fcb8-472b-b45e-967448ded6d8')
    return IServiceSysTxnConfig
def _define_IServiceSysTxnConfig():
    IServiceSysTxnConfig = win32more.System.ComponentServices.IServiceSysTxnConfig_head
    IServiceSysTxnConfig.ConfigureBYOTSysTxn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.ITransactionProxy_head, use_last_error=False)(9, 'ConfigureBYOTSysTxn', ((1, 'pTxProxy'),)))
    win32more.System.ComponentServices.IServiceTransactionConfig
    return IServiceSysTxnConfig
def _define_IServiceSynchronizationConfig_head():
    class IServiceSynchronizationConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd880e81-6dce-4c58-af83-a208846c0030')
    return IServiceSynchronizationConfig
def _define_IServiceSynchronizationConfig():
    IServiceSynchronizationConfig = win32more.System.ComponentServices.IServiceSynchronizationConfig_head
    IServiceSynchronizationConfig.ConfigureSynchronization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_SynchronizationConfig, use_last_error=False)(3, 'ConfigureSynchronization', ((1, 'synchConfig'),)))
    win32more.System.Com.IUnknown
    return IServiceSynchronizationConfig
def _define_IServiceTrackerConfig_head():
    class IServiceTrackerConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('6c3a3e1d-0ba6-4036-b76f-d0404db816c9')
    return IServiceTrackerConfig
def _define_IServiceTrackerConfig():
    IServiceTrackerConfig = win32more.System.ComponentServices.IServiceTrackerConfig_head
    IServiceTrackerConfig.TrackerConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_TrackerConfig,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'TrackerConfig', ((1, 'trackerConfig'),(1, 'szTrackerAppName'),(1, 'szTrackerCtxName'),)))
    win32more.System.Com.IUnknown
    return IServiceTrackerConfig
def _define_IServicePartitionConfig_head():
    class IServicePartitionConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('80182d03-5ea4-4831-ae97-55beffc2e590')
    return IServicePartitionConfig
def _define_IServicePartitionConfig():
    IServicePartitionConfig = win32more.System.ComponentServices.IServicePartitionConfig_head
    IServicePartitionConfig.PartitionConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.CSC_PartitionConfig, use_last_error=False)(3, 'PartitionConfig', ((1, 'partitionConfig'),)))
    IServicePartitionConfig.PartitionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'PartitionID', ((1, 'guidPartitionID'),)))
    win32more.System.Com.IUnknown
    return IServicePartitionConfig
def _define_IServiceCall_head():
    class IServiceCall(win32more.System.Com.IUnknown_head):
        Guid = Guid('bd3e2e12-42dd-40f4-a09a-95a50c58304b')
    return IServiceCall
def _define_IServiceCall():
    IServiceCall = win32more.System.ComponentServices.IServiceCall_head
    IServiceCall.OnCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnCall', ()))
    win32more.System.Com.IUnknown
    return IServiceCall
def _define_IAsyncErrorNotify_head():
    class IAsyncErrorNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('fe6777fb-a674-4177-8f32-6d707e113484')
    return IAsyncErrorNotify
def _define_IAsyncErrorNotify():
    IAsyncErrorNotify = win32more.System.ComponentServices.IAsyncErrorNotify_head
    IAsyncErrorNotify.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnError', ((1, 'hr'),)))
    win32more.System.Com.IUnknown
    return IAsyncErrorNotify
def _define_IServiceActivity_head():
    class IServiceActivity(win32more.System.Com.IUnknown_head):
        Guid = Guid('67532e0c-9e2f-4450-a354-035633944e17')
    return IServiceActivity
def _define_IServiceActivity():
    IServiceActivity = win32more.System.ComponentServices.IServiceActivity_head
    IServiceActivity.SynchronousCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IServiceCall_head, use_last_error=False)(3, 'SynchronousCall', ((1, 'pIServiceCall'),)))
    IServiceActivity.AsynchronousCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IServiceCall_head, use_last_error=False)(4, 'AsynchronousCall', ((1, 'pIServiceCall'),)))
    IServiceActivity.BindToCurrentThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'BindToCurrentThread', ()))
    IServiceActivity.UnbindFromThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'UnbindFromThread', ()))
    win32more.System.Com.IUnknown
    return IServiceActivity
def _define_IThreadPoolKnobs_head():
    class IThreadPoolKnobs(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372af7-cae7-11cf-be81-00aa00a2fa25')
    return IThreadPoolKnobs
def _define_IThreadPoolKnobs():
    IThreadPoolKnobs = win32more.System.ComponentServices.IThreadPoolKnobs_head
    IThreadPoolKnobs.GetMaxThreads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'GetMaxThreads', ((1, 'plcMaxThreads'),)))
    IThreadPoolKnobs.GetCurrentThreads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'GetCurrentThreads', ((1, 'plcCurrentThreads'),)))
    IThreadPoolKnobs.SetMaxThreads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(5, 'SetMaxThreads', ((1, 'lcMaxThreads'),)))
    IThreadPoolKnobs.GetDeleteDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'GetDeleteDelay', ((1, 'pmsecDeleteDelay'),)))
    IThreadPoolKnobs.SetDeleteDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'SetDeleteDelay', ((1, 'msecDeleteDelay'),)))
    IThreadPoolKnobs.GetMaxQueuedRequests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetMaxQueuedRequests', ((1, 'plcMaxQueuedRequests'),)))
    IThreadPoolKnobs.GetCurrentQueuedRequests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetCurrentQueuedRequests', ((1, 'plcCurrentQueuedRequests'),)))
    IThreadPoolKnobs.SetMaxQueuedRequests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'SetMaxQueuedRequests', ((1, 'lcMaxQueuedRequests'),)))
    IThreadPoolKnobs.SetMinThreads = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'SetMinThreads', ((1, 'lcMinThreads'),)))
    IThreadPoolKnobs.SetQueueDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'SetQueueDepth', ((1, 'lcQueueDepth'),)))
    win32more.System.Com.IUnknown
    return IThreadPoolKnobs
def _define_IComStaThreadPoolKnobs_head():
    class IComStaThreadPoolKnobs(win32more.System.Com.IUnknown_head):
        Guid = Guid('324b64fa-33b6-11d2-98b7-00c04f8ee1c4')
    return IComStaThreadPoolKnobs
def _define_IComStaThreadPoolKnobs():
    IComStaThreadPoolKnobs = win32more.System.ComponentServices.IComStaThreadPoolKnobs_head
    IComStaThreadPoolKnobs.SetMinThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetMinThreadCount', ((1, 'minThreads'),)))
    IComStaThreadPoolKnobs.GetMinThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetMinThreadCount', ((1, 'minThreads'),)))
    IComStaThreadPoolKnobs.SetMaxThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetMaxThreadCount', ((1, 'maxThreads'),)))
    IComStaThreadPoolKnobs.GetMaxThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetMaxThreadCount', ((1, 'maxThreads'),)))
    IComStaThreadPoolKnobs.SetActivityPerThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'SetActivityPerThread', ((1, 'activitiesPerThread'),)))
    IComStaThreadPoolKnobs.GetActivityPerThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetActivityPerThread', ((1, 'activitiesPerThread'),)))
    IComStaThreadPoolKnobs.SetActivityRatio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(9, 'SetActivityRatio', ((1, 'activityRatio'),)))
    IComStaThreadPoolKnobs.GetActivityRatio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'GetActivityRatio', ((1, 'activityRatio'),)))
    IComStaThreadPoolKnobs.GetThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetThreadCount', ((1, 'pdwThreads'),)))
    IComStaThreadPoolKnobs.GetQueueDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetQueueDepth', ((1, 'pdwQDepth'),)))
    IComStaThreadPoolKnobs.SetQueueDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'SetQueueDepth', ((1, 'dwQDepth'),)))
    win32more.System.Com.IUnknown
    return IComStaThreadPoolKnobs
def _define_IComMtaThreadPoolKnobs_head():
    class IComMtaThreadPoolKnobs(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9a76d2e-76a5-43eb-a0c4-49bec8e48480')
    return IComMtaThreadPoolKnobs
def _define_IComMtaThreadPoolKnobs():
    IComMtaThreadPoolKnobs = win32more.System.ComponentServices.IComMtaThreadPoolKnobs_head
    IComMtaThreadPoolKnobs.MTASetMaxThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'MTASetMaxThreadCount', ((1, 'dwMaxThreads'),)))
    IComMtaThreadPoolKnobs.MTAGetMaxThreadCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'MTAGetMaxThreadCount', ((1, 'pdwMaxThreads'),)))
    IComMtaThreadPoolKnobs.MTASetThrottleValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'MTASetThrottleValue', ((1, 'dwThrottle'),)))
    IComMtaThreadPoolKnobs.MTAGetThrottleValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'MTAGetThrottleValue', ((1, 'pdwThrottle'),)))
    win32more.System.Com.IUnknown
    return IComMtaThreadPoolKnobs
def _define_IComStaThreadPoolKnobs2_head():
    class IComStaThreadPoolKnobs2(win32more.System.ComponentServices.IComStaThreadPoolKnobs_head):
        Guid = Guid('73707523-ff9a-4974-bf84-2108dc213740')
    return IComStaThreadPoolKnobs2
def _define_IComStaThreadPoolKnobs2():
    IComStaThreadPoolKnobs2 = win32more.System.ComponentServices.IComStaThreadPoolKnobs2_head
    IComStaThreadPoolKnobs2.GetMaxCPULoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetMaxCPULoad', ((1, 'pdwLoad'),)))
    IComStaThreadPoolKnobs2.SetMaxCPULoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'SetMaxCPULoad', ((1, 'pdwLoad'),)))
    IComStaThreadPoolKnobs2.GetCPUMetricEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'GetCPUMetricEnabled', ((1, 'pbMetricEnabled'),)))
    IComStaThreadPoolKnobs2.SetCPUMetricEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(17, 'SetCPUMetricEnabled', ((1, 'bMetricEnabled'),)))
    IComStaThreadPoolKnobs2.GetCreateThreadsAggressively = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(18, 'GetCreateThreadsAggressively', ((1, 'pbMetricEnabled'),)))
    IComStaThreadPoolKnobs2.SetCreateThreadsAggressively = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(19, 'SetCreateThreadsAggressively', ((1, 'bMetricEnabled'),)))
    IComStaThreadPoolKnobs2.GetMaxCSR = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(20, 'GetMaxCSR', ((1, 'pdwCSR'),)))
    IComStaThreadPoolKnobs2.SetMaxCSR = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(21, 'SetMaxCSR', ((1, 'dwCSR'),)))
    IComStaThreadPoolKnobs2.GetWaitTimeForThreadCleanup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(22, 'GetWaitTimeForThreadCleanup', ((1, 'pdwThreadCleanupWaitTime'),)))
    IComStaThreadPoolKnobs2.SetWaitTimeForThreadCleanup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(23, 'SetWaitTimeForThreadCleanup', ((1, 'dwThreadCleanupWaitTime'),)))
    win32more.System.ComponentServices.IComStaThreadPoolKnobs
    return IComStaThreadPoolKnobs2
def _define_IProcessInitializer_head():
    class IProcessInitializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('1113f52d-dc7f-4943-aed6-88d04027e32a')
    return IProcessInitializer
def _define_IProcessInitializer():
    IProcessInitializer = win32more.System.ComponentServices.IProcessInitializer_head
    IProcessInitializer.Startup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Startup', ((1, 'punkProcessControl'),)))
    IProcessInitializer.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Shutdown', ()))
    win32more.System.Com.IUnknown
    return IProcessInitializer
def _define_IServicePoolConfig_head():
    class IServicePoolConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9690656-5bca-470c-8451-250c1f43a33e')
    return IServicePoolConfig
def _define_IServicePoolConfig():
    IServicePoolConfig = win32more.System.ComponentServices.IServicePoolConfig_head
    IServicePoolConfig.put_MaxPoolSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'put_MaxPoolSize', ((1, 'dwMaxPool'),)))
    IServicePoolConfig.get_MaxPoolSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'get_MaxPoolSize', ((1, 'pdwMaxPool'),)))
    IServicePoolConfig.put_MinPoolSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'put_MinPoolSize', ((1, 'dwMinPool'),)))
    IServicePoolConfig.get_MinPoolSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_MinPoolSize', ((1, 'pdwMinPool'),)))
    IServicePoolConfig.put_CreationTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'put_CreationTimeout', ((1, 'dwCreationTimeout'),)))
    IServicePoolConfig.get_CreationTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'get_CreationTimeout', ((1, 'pdwCreationTimeout'),)))
    IServicePoolConfig.put_TransactionAffinity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'put_TransactionAffinity', ((1, 'fTxAffinity'),)))
    IServicePoolConfig.get_TransactionAffinity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'get_TransactionAffinity', ((1, 'pfTxAffinity'),)))
    IServicePoolConfig.put_ClassFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IClassFactory_head, use_last_error=False)(11, 'put_ClassFactory', ((1, 'pFactory'),)))
    IServicePoolConfig.get_ClassFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IClassFactory_head), use_last_error=False)(12, 'get_ClassFactory', ((1, 'pFactory'),)))
    win32more.System.Com.IUnknown
    return IServicePoolConfig
def _define_IServicePool_head():
    class IServicePool(win32more.System.Com.IUnknown_head):
        Guid = Guid('b302df81-ea45-451e-99a2-09f9fd1b1e13')
    return IServicePool
def _define_IServicePool():
    IServicePool = win32more.System.ComponentServices.IServicePool_head
    IServicePool.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Initialize', ((1, 'pPoolConfig'),)))
    IServicePool.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetObject', ((1, 'riid'),(1, 'ppv'),)))
    IServicePool.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Shutdown', ()))
    win32more.System.Com.IUnknown
    return IServicePool
def _define_IManagedPooledObj_head():
    class IManagedPooledObj(win32more.System.Com.IUnknown_head):
        Guid = Guid('c5da4bea-1b42-4437-8926-b6a38860a770')
    return IManagedPooledObj
def _define_IManagedPooledObj():
    IManagedPooledObj = win32more.System.ComponentServices.IManagedPooledObj_head
    IManagedPooledObj.SetHeld = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'SetHeld', ((1, 'm_bHeld'),)))
    win32more.System.Com.IUnknown
    return IManagedPooledObj
def _define_IManagedPoolAction_head():
    class IManagedPoolAction(win32more.System.Com.IUnknown_head):
        Guid = Guid('da91b74e-5388-4783-949d-c1cd5fb00506')
    return IManagedPoolAction
def _define_IManagedPoolAction():
    IManagedPoolAction = win32more.System.ComponentServices.IManagedPoolAction_head
    IManagedPoolAction.LastRelease = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'LastRelease', ()))
    win32more.System.Com.IUnknown
    return IManagedPoolAction
def _define_IManagedObjectInfo_head():
    class IManagedObjectInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('1427c51a-4584-49d8-90a0-c50d8086cbe9')
    return IManagedObjectInfo
def _define_IManagedObjectInfo():
    IManagedObjectInfo = win32more.System.ComponentServices.IManagedObjectInfo_head
    IManagedObjectInfo.GetIUnknown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetIUnknown', ((1, 'pUnk'),)))
    IManagedObjectInfo.GetIObjectControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.IObjectControl_head), use_last_error=False)(4, 'GetIObjectControl', ((1, 'pCtrl'),)))
    IManagedObjectInfo.SetInPool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.System.ComponentServices.IManagedPooledObj_head, use_last_error=False)(5, 'SetInPool', ((1, 'bInPool'),(1, 'pPooledObj'),)))
    IManagedObjectInfo.SetWrapperStrength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'SetWrapperStrength', ((1, 'bStrong'),)))
    win32more.System.Com.IUnknown
    return IManagedObjectInfo
def _define_IAppDomainHelper_head():
    class IAppDomainHelper(win32more.System.Com.IDispatch_head):
        Guid = Guid('c7b67079-8255-42c6-9ec0-6994a3548780')
    return IAppDomainHelper
def _define_IAppDomainHelper():
    IAppDomainHelper = win32more.System.ComponentServices.IAppDomainHelper_head
    IAppDomainHelper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,IntPtr,c_void_p, use_last_error=False)(7, 'Initialize', ((1, 'pUnkAD'),(1, '__MIDL__IAppDomainHelper0000'),(1, 'pPool'),)))
    IAppDomainHelper.DoCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,IntPtr,c_void_p, use_last_error=False)(8, 'DoCallback', ((1, 'pUnkAD'),(1, '__MIDL__IAppDomainHelper0001'),(1, 'pPool'),)))
    win32more.System.Com.IDispatch
    return IAppDomainHelper
def _define_IAssemblyLocator_head():
    class IAssemblyLocator(win32more.System.Com.IDispatch_head):
        Guid = Guid('391ffbb9-a8ee-432a-abc8-baa238dab90f')
    return IAssemblyLocator
def _define_IAssemblyLocator():
    IAssemblyLocator = win32more.System.ComponentServices.IAssemblyLocator_head
    IAssemblyLocator.GetModules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(7, 'GetModules', ((1, 'applicationDir'),(1, 'applicationName'),(1, 'assemblyName'),(1, 'pModules'),)))
    win32more.System.Com.IDispatch
    return IAssemblyLocator
def _define_IManagedActivationEvents_head():
    class IManagedActivationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('a5f325af-572f-46da-b8ab-827c3d95d99e')
    return IManagedActivationEvents
def _define_IManagedActivationEvents():
    IManagedActivationEvents = win32more.System.ComponentServices.IManagedActivationEvents_head
    IManagedActivationEvents.CreateManagedStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IManagedObjectInfo_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'CreateManagedStub', ((1, 'pInfo'),(1, 'fDist'),)))
    IManagedActivationEvents.DestroyManagedStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IManagedObjectInfo_head, use_last_error=False)(4, 'DestroyManagedStub', ((1, 'pInfo'),)))
    win32more.System.Com.IUnknown
    return IManagedActivationEvents
def _define_ISendMethodEvents_head():
    class ISendMethodEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('2732fd59-b2b4-4d44-878c-8b8f09626008')
    return ISendMethodEvents
def _define_ISendMethodEvents():
    ISendMethodEvents = win32more.System.ComponentServices.ISendMethodEvents_head
    ISendMethodEvents.SendMethodCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),UInt32, use_last_error=False)(3, 'SendMethodCall', ((1, 'pIdentity'),(1, 'riid'),(1, 'dwMeth'),)))
    ISendMethodEvents.SendMethodReturn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Guid),UInt32,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(4, 'SendMethodReturn', ((1, 'pIdentity'),(1, 'riid'),(1, 'dwMeth'),(1, 'hrCall'),(1, 'hrServer'),)))
    win32more.System.Com.IUnknown
    return ISendMethodEvents
def _define_ITransactionResourcePool_head():
    class ITransactionResourcePool(win32more.System.Com.IUnknown_head):
        Guid = Guid('c5feb7c1-346a-11d1-b1cc-00aa00ba3258')
    return ITransactionResourcePool
def _define_ITransactionResourcePool():
    ITransactionResourcePool = win32more.System.ComponentServices.ITransactionResourcePool_head
    ITransactionResourcePool.PutResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IObjPool_head,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'PutResource', ((1, 'pPool'),(1, 'pUnk'),)))
    ITransactionResourcePool.GetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IObjPool_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'GetResource', ((1, 'pPool'),(1, 'ppUnk'),)))
    win32more.System.Com.IUnknown
    return ITransactionResourcePool
def _define_IMTSCall_head():
    class IMTSCall(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372aef-cae7-11cf-be81-00aa00a2fa25')
    return IMTSCall
def _define_IMTSCall():
    IMTSCall = win32more.System.ComponentServices.IMTSCall_head
    IMTSCall.OnCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnCall', ()))
    win32more.System.Com.IUnknown
    return IMTSCall
def _define_IContextProperties_head():
    class IContextProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('d396da85-bf8f-11d1-bbae-00c04fc2fa5f')
    return IContextProperties
def _define_IContextProperties():
    IContextProperties = win32more.System.ComponentServices.IContextProperties_head
    IContextProperties.Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'Count', ((1, 'plCount'),)))
    IContextProperties.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'GetProperty', ((1, 'name'),(1, 'pProperty'),)))
    IContextProperties.EnumNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.IEnumNames_head), use_last_error=False)(5, 'EnumNames', ((1, 'ppenum'),)))
    IContextProperties.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(6, 'SetProperty', ((1, 'name'),(1, 'property'),)))
    IContextProperties.RemoveProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'RemoveProperty', ((1, 'name'),)))
    win32more.System.Com.IUnknown
    return IContextProperties
def _define_IObjPool_head():
    class IObjPool(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d8805a0-2ea7-11d1-b1cc-00aa00ba3258')
    return IObjPool
def _define_IObjPool():
    IObjPool = win32more.System.ComponentServices.IObjPool_head
    IObjPool.Reserved1 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(3, 'Reserved1', ()))
    IObjPool.Reserved2 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'Reserved2', ()))
    IObjPool.Reserved3 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'Reserved3', ()))
    IObjPool.Reserved4 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(6, 'Reserved4', ()))
    IObjPool.PutEndTx = COMMETHOD(WINFUNCTYPE(Void,win32more.System.Com.IUnknown_head, use_last_error=False)(7, 'PutEndTx', ((1, 'pObj'),)))
    IObjPool.Reserved5 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(8, 'Reserved5', ()))
    IObjPool.Reserved6 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(9, 'Reserved6', ()))
    win32more.System.Com.IUnknown
    return IObjPool
def _define_ITransactionProperty_head():
    class ITransactionProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('788ea814-87b1-11d1-bba6-00c04fc2fa5f')
    return ITransactionProperty
def _define_ITransactionProperty():
    ITransactionProperty = win32more.System.ComponentServices.ITransactionProperty_head
    ITransactionProperty.Reserved1 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(3, 'Reserved1', ()))
    ITransactionProperty.Reserved2 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'Reserved2', ()))
    ITransactionProperty.Reserved3 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'Reserved3', ()))
    ITransactionProperty.Reserved4 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(6, 'Reserved4', ()))
    ITransactionProperty.Reserved5 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(7, 'Reserved5', ()))
    ITransactionProperty.Reserved6 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(8, 'Reserved6', ()))
    ITransactionProperty.Reserved7 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(9, 'Reserved7', ()))
    ITransactionProperty.Reserved8 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(10, 'Reserved8', ()))
    ITransactionProperty.Reserved9 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(11, 'Reserved9', ()))
    ITransactionProperty.GetTransactionResourcePool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.ITransactionResourcePool_head), use_last_error=False)(12, 'GetTransactionResourcePool', ((1, 'ppTxPool'),)))
    ITransactionProperty.Reserved10 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(13, 'Reserved10', ()))
    ITransactionProperty.Reserved11 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(14, 'Reserved11', ()))
    ITransactionProperty.Reserved12 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(15, 'Reserved12', ()))
    ITransactionProperty.Reserved13 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(16, 'Reserved13', ()))
    ITransactionProperty.Reserved14 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(17, 'Reserved14', ()))
    ITransactionProperty.Reserved15 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(18, 'Reserved15', ()))
    ITransactionProperty.Reserved16 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(19, 'Reserved16', ()))
    ITransactionProperty.Reserved17 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(20, 'Reserved17', ()))
    win32more.System.Com.IUnknown
    return ITransactionProperty
def _define_IMTSActivity_head():
    class IMTSActivity(win32more.System.Com.IUnknown_head):
        Guid = Guid('51372af0-cae7-11cf-be81-00aa00a2fa25')
    return IMTSActivity
def _define_IMTSActivity():
    IMTSActivity = win32more.System.ComponentServices.IMTSActivity_head
    IMTSActivity.SynchronousCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IMTSCall_head, use_last_error=False)(3, 'SynchronousCall', ((1, 'pCall'),)))
    IMTSActivity.AsyncCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ComponentServices.IMTSCall_head, use_last_error=False)(4, 'AsyncCall', ((1, 'pCall'),)))
    IMTSActivity.Reserved1 = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'Reserved1', ()))
    IMTSActivity.BindToCurrentThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'BindToCurrentThread', ()))
    IMTSActivity.UnbindFromThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'UnbindFromThread', ()))
    win32more.System.Com.IUnknown
    return IMTSActivity
AutoSvcs_Error_Constants = UInt32
AutoSvcs_Error_Constants_mtsErrCtxAborted = 2147803138
AutoSvcs_Error_Constants_mtsErrCtxAborting = 2147803139
AutoSvcs_Error_Constants_mtsErrCtxNoContext = 2147803140
AutoSvcs_Error_Constants_mtsErrCtxNotRegistered = 2147803141
AutoSvcs_Error_Constants_mtsErrCtxSynchTimeout = 2147803142
AutoSvcs_Error_Constants_mtsErrCtxOldReference = 2147803143
AutoSvcs_Error_Constants_mtsErrCtxRoleNotFound = 2147803148
AutoSvcs_Error_Constants_mtsErrCtxNoSecurity = 2147803149
AutoSvcs_Error_Constants_mtsErrCtxWrongThread = 2147803150
AutoSvcs_Error_Constants_mtsErrCtxTMNotAvailable = 2147803151
AutoSvcs_Error_Constants_comQCErrApplicationNotQueued = 2148599296
AutoSvcs_Error_Constants_comQCErrNoQueueableInterfaces = 2148599297
AutoSvcs_Error_Constants_comQCErrQueuingServiceNotAvailable = 2148599298
AutoSvcs_Error_Constants_comQCErrQueueTransactMismatch = 2148599299
AutoSvcs_Error_Constants_comqcErrRecorderMarshalled = 2148599300
AutoSvcs_Error_Constants_comqcErrOutParam = 2148599301
AutoSvcs_Error_Constants_comqcErrRecorderNotTrusted = 2148599302
AutoSvcs_Error_Constants_comqcErrPSLoad = 2148599303
AutoSvcs_Error_Constants_comqcErrMarshaledObjSameTxn = 2148599304
AutoSvcs_Error_Constants_comqcErrInvalidMessage = 2148599376
AutoSvcs_Error_Constants_comqcErrMsmqSidUnavailable = 2148599377
AutoSvcs_Error_Constants_comqcErrWrongMsgExtension = 2148599378
AutoSvcs_Error_Constants_comqcErrMsmqServiceUnavailable = 2148599379
AutoSvcs_Error_Constants_comqcErrMsgNotAuthenticated = 2148599380
AutoSvcs_Error_Constants_comqcErrMsmqConnectorUsed = 2148599381
AutoSvcs_Error_Constants_comqcErrBadMarshaledObject = 2148599382
LockModes = Int32
LockModes_LockSetGet = 0
LockModes_LockMethod = 1
ReleaseModes = Int32
ReleaseModes_Standard = 0
ReleaseModes_Process = 1
CRMFLAGS = Int32
CRMFLAG_FORGETTARGET = 1
CRMFLAG_WRITTENDURINGPREPARE = 2
CRMFLAG_WRITTENDURINGCOMMIT = 4
CRMFLAG_WRITTENDURINGABORT = 8
CRMFLAG_WRITTENDURINGRECOVERY = 16
CRMFLAG_WRITTENDURINGREPLAY = 32
CRMFLAG_REPLAYINPROGRESS = 64
CRMREGFLAGS = Int32
CRMREGFLAG_PREPAREPHASE = 1
CRMREGFLAG_COMMITPHASE = 2
CRMREGFLAG_ABORTPHASE = 4
CRMREGFLAG_ALLPHASES = 7
CRMREGFLAG_FAILIFINDOUBTSREMAIN = 16
def _define_CoGetDefaultContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.APTTYPE,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CoGetDefaultContext", windll["OLE32"]), ((1, 'aptType'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateActivity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CoCreateActivity", windll["comsvcs"]), ((1, 'pIUnknown'),(1, 'riid'),(1, 'ppObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoEnterServiceDomain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(("CoEnterServiceDomain", windll["comsvcs"]), ((1, 'pConfigObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoLeaveServiceDomain():
    try:
        return WINFUNCTYPE(Void,win32more.System.Com.IUnknown_head, use_last_error=False)(("CoLeaveServiceDomain", windll["comsvcs"]), ((1, 'pUnkStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetManagedExtensions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(("GetManagedExtensions", windll["comsvcs"]), ((1, 'dwExts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeRef():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(("SafeRef", windll["comsvcs"]), ((1, 'rid'),(1, 'pUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecycleSurrogate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(("RecycleSurrogate", windll["comsvcs"]), ((1, 'lReasonCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MTSCreateActivity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("MTSCreateActivity", windll["comsvcs"]), ((1, 'riid'),(1, 'ppobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDispenserManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.ComponentServices.IDispenserManager_head), use_last_error=False)(("GetDispenserManager", windll["MTxDM"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "GUID_STRING_SIZE",
    "DATA_NOT_AVAILABLE",
    "MTXDM_E_ENLISTRESOURCEFAILED",
    "CRR_NO_REASON_SUPPLIED",
    "CRR_LIFETIME_LIMIT",
    "CRR_ACTIVATION_LIMIT",
    "CRR_CALL_LIMIT",
    "CRR_MEMORY_LIMIT",
    "CRR_RECYCLED_FROM_UI",
    "SecurityIdentity",
    "SecurityCallers",
    "SecurityCallContext",
    "GetSecurityCallContextAppObject",
    "Dummy30040732",
    "TransactionContext",
    "TransactionContextEx",
    "ByotServerEx",
    "CServiceConfig",
    "ServicePool",
    "ServicePoolConfig",
    "SharedProperty",
    "SharedPropertyGroup",
    "SharedPropertyGroupManager",
    "COMEvents",
    "CoMTSLocator",
    "MtsGrp",
    "ComServiceEvents",
    "ComSystemAppEventData",
    "CRMClerk",
    "CRMRecoveryClerk",
    "LBEvents",
    "MessageMover",
    "DispenserManager",
    "PoolMgr",
    "EventServer",
    "TrackerServer",
    "AppDomainHelper",
    "ClrAssemblyLocator",
    "COMAdminCatalog",
    "COMAdminCatalogObject",
    "COMAdminCatalogCollection",
    "ICOMAdminCatalog",
    "COMAdminInUse",
    "COMAdminInUse_COMAdminNotInUse",
    "COMAdminInUse_COMAdminInUseByCatalog",
    "COMAdminInUse_COMAdminInUseByRegistryUnknown",
    "COMAdminInUse_COMAdminInUseByRegistryProxyStub",
    "COMAdminInUse_COMAdminInUseByRegistryTypeLib",
    "COMAdminInUse_COMAdminInUseByRegistryClsid",
    "ICOMAdminCatalog2",
    "ICatalogObject",
    "ICatalogCollection",
    "COMAdminComponentType",
    "COMAdminComponentType_COMAdmin32BitComponent",
    "COMAdminComponentType_COMAdmin64BitComponent",
    "COMAdminApplicationInstallOptions",
    "COMAdminApplicationInstallOptions_COMAdminInstallNoUsers",
    "COMAdminApplicationInstallOptions_COMAdminInstallUsers",
    "COMAdminApplicationInstallOptions_COMAdminInstallForceOverwriteOfFiles",
    "COMAdminApplicationExportOptions",
    "COMAdminApplicationExportOptions_COMAdminExportNoUsers",
    "COMAdminApplicationExportOptions_COMAdminExportUsers",
    "COMAdminApplicationExportOptions_COMAdminExportApplicationProxy",
    "COMAdminApplicationExportOptions_COMAdminExportForceOverwriteOfFiles",
    "COMAdminApplicationExportOptions_COMAdminExportIn10Format",
    "COMAdminThreadingModels",
    "COMAdminThreadingModels_COMAdminThreadingModelApartment",
    "COMAdminThreadingModels_COMAdminThreadingModelFree",
    "COMAdminThreadingModels_COMAdminThreadingModelMain",
    "COMAdminThreadingModels_COMAdminThreadingModelBoth",
    "COMAdminThreadingModels_COMAdminThreadingModelNeutral",
    "COMAdminThreadingModels_COMAdminThreadingModelNotSpecified",
    "COMAdminTransactionOptions",
    "COMAdminTransactionOptions_COMAdminTransactionIgnored",
    "COMAdminTransactionOptions_COMAdminTransactionNone",
    "COMAdminTransactionOptions_COMAdminTransactionSupported",
    "COMAdminTransactionOptions_COMAdminTransactionRequired",
    "COMAdminTransactionOptions_COMAdminTransactionRequiresNew",
    "COMAdminTxIsolationLevelOptions",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelAny",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadUnCommitted",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadCommitted",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelRepeatableRead",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelSerializable",
    "COMAdminSynchronizationOptions",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationIgnored",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationNone",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationSupported",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationRequired",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationRequiresNew",
    "COMAdminActivationOptions",
    "COMAdminActivationOptions_COMAdminActivationInproc",
    "COMAdminActivationOptions_COMAdminActivationLocal",
    "COMAdminAccessChecksLevelOptions",
    "COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationLevel",
    "COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationComponentLevel",
    "COMAdminAuthenticationLevelOptions",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationDefault",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationNone",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationConnect",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationCall",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPacket",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationIntegrity",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPrivacy",
    "COMAdminImpersonationLevelOptions",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationAnonymous",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationIdentify",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationImpersonate",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationDelegate",
    "COMAdminAuthenticationCapabilitiesOptions",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesNone",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesSecureReference",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesStaticCloaking",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesDynamicCloaking",
    "COMAdminOS",
    "COMAdminOS_COMAdminOSNotInitialized",
    "COMAdminOS_COMAdminOSWindows3_1",
    "COMAdminOS_COMAdminOSWindows9x",
    "COMAdminOS_COMAdminOSWindows2000",
    "COMAdminOS_COMAdminOSWindows2000AdvancedServer",
    "COMAdminOS_COMAdminOSWindows2000Unknown",
    "COMAdminOS_COMAdminOSUnknown",
    "COMAdminOS_COMAdminOSWindowsXPPersonal",
    "COMAdminOS_COMAdminOSWindowsXPProfessional",
    "COMAdminOS_COMAdminOSWindowsNETStandardServer",
    "COMAdminOS_COMAdminOSWindowsNETEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsNETDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsNETWebServer",
    "COMAdminOS_COMAdminOSWindowsLonghornPersonal",
    "COMAdminOS_COMAdminOSWindowsLonghornProfessional",
    "COMAdminOS_COMAdminOSWindowsLonghornStandardServer",
    "COMAdminOS_COMAdminOSWindowsLonghornEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsLonghornDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsLonghornWebServer",
    "COMAdminOS_COMAdminOSWindows7Personal",
    "COMAdminOS_COMAdminOSWindows7Professional",
    "COMAdminOS_COMAdminOSWindows7StandardServer",
    "COMAdminOS_COMAdminOSWindows7EnterpriseServer",
    "COMAdminOS_COMAdminOSWindows7DatacenterServer",
    "COMAdminOS_COMAdminOSWindows7WebServer",
    "COMAdminOS_COMAdminOSWindows8Personal",
    "COMAdminOS_COMAdminOSWindows8Professional",
    "COMAdminOS_COMAdminOSWindows8StandardServer",
    "COMAdminOS_COMAdminOSWindows8EnterpriseServer",
    "COMAdminOS_COMAdminOSWindows8DatacenterServer",
    "COMAdminOS_COMAdminOSWindows8WebServer",
    "COMAdminOS_COMAdminOSWindowsBluePersonal",
    "COMAdminOS_COMAdminOSWindowsBlueProfessional",
    "COMAdminOS_COMAdminOSWindowsBlueStandardServer",
    "COMAdminOS_COMAdminOSWindowsBlueEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsBlueDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsBlueWebServer",
    "COMAdminServiceOptions",
    "COMAdminServiceOptions_COMAdminServiceLoadBalanceRouter",
    "COMAdminServiceStatusOptions",
    "COMAdminServiceStatusOptions_COMAdminServiceStopped",
    "COMAdminServiceStatusOptions_COMAdminServiceStartPending",
    "COMAdminServiceStatusOptions_COMAdminServiceStopPending",
    "COMAdminServiceStatusOptions_COMAdminServiceRunning",
    "COMAdminServiceStatusOptions_COMAdminServiceContinuePending",
    "COMAdminServiceStatusOptions_COMAdminServicePausePending",
    "COMAdminServiceStatusOptions_COMAdminServicePaused",
    "COMAdminServiceStatusOptions_COMAdminServiceUnknownState",
    "COMAdminQCMessageAuthenticateOptions",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateSecureApps",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOff",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOn",
    "COMAdminFileFlags",
    "COMAdminFileFlags_COMAdminFileFlagLoadable",
    "COMAdminFileFlags_COMAdminFileFlagCOM",
    "COMAdminFileFlags_COMAdminFileFlagContainsPS",
    "COMAdminFileFlags_COMAdminFileFlagContainsComp",
    "COMAdminFileFlags_COMAdminFileFlagContainsTLB",
    "COMAdminFileFlags_COMAdminFileFlagSelfReg",
    "COMAdminFileFlags_COMAdminFileFlagSelfUnReg",
    "COMAdminFileFlags_COMAdminFileFlagUnloadableDLL",
    "COMAdminFileFlags_COMAdminFileFlagDoesNotExist",
    "COMAdminFileFlags_COMAdminFileFlagAlreadyInstalled",
    "COMAdminFileFlags_COMAdminFileFlagBadTLB",
    "COMAdminFileFlags_COMAdminFileFlagGetClassObjFailed",
    "COMAdminFileFlags_COMAdminFileFlagClassNotAvailable",
    "COMAdminFileFlags_COMAdminFileFlagRegistrar",
    "COMAdminFileFlags_COMAdminFileFlagNoRegistrar",
    "COMAdminFileFlags_COMAdminFileFlagDLLRegsvrFailed",
    "COMAdminFileFlags_COMAdminFileFlagRegTLBFailed",
    "COMAdminFileFlags_COMAdminFileFlagRegistrarFailed",
    "COMAdminFileFlags_COMAdminFileFlagError",
    "COMAdminComponentFlags",
    "COMAdminComponentFlags_COMAdminCompFlagTypeInfoFound",
    "COMAdminComponentFlags_COMAdminCompFlagCOMPlusPropertiesFound",
    "COMAdminComponentFlags_COMAdminCompFlagProxyFound",
    "COMAdminComponentFlags_COMAdminCompFlagInterfacesFound",
    "COMAdminComponentFlags_COMAdminCompFlagAlreadyInstalled",
    "COMAdminComponentFlags_COMAdminCompFlagNotInApplication",
    "COMAdminErrorCodes",
    "COMAdminErrorCodes_COMAdminErrObjectErrors",
    "COMAdminErrorCodes_COMAdminErrObjectInvalid",
    "COMAdminErrorCodes_COMAdminErrKeyMissing",
    "COMAdminErrorCodes_COMAdminErrAlreadyInstalled",
    "COMAdminErrorCodes_COMAdminErrAppFileWriteFail",
    "COMAdminErrorCodes_COMAdminErrAppFileReadFail",
    "COMAdminErrorCodes_COMAdminErrAppFileVersion",
    "COMAdminErrorCodes_COMAdminErrBadPath",
    "COMAdminErrorCodes_COMAdminErrApplicationExists",
    "COMAdminErrorCodes_COMAdminErrRoleExists",
    "COMAdminErrorCodes_COMAdminErrCantCopyFile",
    "COMAdminErrorCodes_COMAdminErrNoUser",
    "COMAdminErrorCodes_COMAdminErrInvalidUserids",
    "COMAdminErrorCodes_COMAdminErrNoRegistryCLSID",
    "COMAdminErrorCodes_COMAdminErrBadRegistryProgID",
    "COMAdminErrorCodes_COMAdminErrAuthenticationLevel",
    "COMAdminErrorCodes_COMAdminErrUserPasswdNotValid",
    "COMAdminErrorCodes_COMAdminErrCLSIDOrIIDMismatch",
    "COMAdminErrorCodes_COMAdminErrRemoteInterface",
    "COMAdminErrorCodes_COMAdminErrDllRegisterServer",
    "COMAdminErrorCodes_COMAdminErrNoServerShare",
    "COMAdminErrorCodes_COMAdminErrDllLoadFailed",
    "COMAdminErrorCodes_COMAdminErrBadRegistryLibID",
    "COMAdminErrorCodes_COMAdminErrAppDirNotFound",
    "COMAdminErrorCodes_COMAdminErrRegistrarFailed",
    "COMAdminErrorCodes_COMAdminErrCompFileDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrCompFileLoadDLLFail",
    "COMAdminErrorCodes_COMAdminErrCompFileGetClassObj",
    "COMAdminErrorCodes_COMAdminErrCompFileClassNotAvail",
    "COMAdminErrorCodes_COMAdminErrCompFileBadTLB",
    "COMAdminErrorCodes_COMAdminErrCompFileNotInstallable",
    "COMAdminErrorCodes_COMAdminErrNotChangeable",
    "COMAdminErrorCodes_COMAdminErrNotDeletable",
    "COMAdminErrorCodes_COMAdminErrSession",
    "COMAdminErrorCodes_COMAdminErrCompMoveLocked",
    "COMAdminErrorCodes_COMAdminErrCompMoveBadDest",
    "COMAdminErrorCodes_COMAdminErrRegisterTLB",
    "COMAdminErrorCodes_COMAdminErrSystemApp",
    "COMAdminErrorCodes_COMAdminErrCompFileNoRegistrar",
    "COMAdminErrorCodes_COMAdminErrCoReqCompInstalled",
    "COMAdminErrorCodes_COMAdminErrServiceNotInstalled",
    "COMAdminErrorCodes_COMAdminErrPropertySaveFailed",
    "COMAdminErrorCodes_COMAdminErrObjectExists",
    "COMAdminErrorCodes_COMAdminErrComponentExists",
    "COMAdminErrorCodes_COMAdminErrRegFileCorrupt",
    "COMAdminErrorCodes_COMAdminErrPropertyOverflow",
    "COMAdminErrorCodes_COMAdminErrNotInRegistry",
    "COMAdminErrorCodes_COMAdminErrObjectNotPoolable",
    "COMAdminErrorCodes_COMAdminErrApplidMatchesClsid",
    "COMAdminErrorCodes_COMAdminErrRoleDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrStartAppNeedsComponents",
    "COMAdminErrorCodes_COMAdminErrRequiresDifferentPlatform",
    "COMAdminErrorCodes_COMAdminErrQueuingServiceNotAvailable",
    "COMAdminErrorCodes_COMAdminErrObjectParentMissing",
    "COMAdminErrorCodes_COMAdminErrObjectDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrCanNotExportAppProxy",
    "COMAdminErrorCodes_COMAdminErrCanNotStartApp",
    "COMAdminErrorCodes_COMAdminErrCanNotExportSystemApp",
    "COMAdminErrorCodes_COMAdminErrCanNotSubscribeToComponent",
    "COMAdminErrorCodes_COMAdminErrAppNotRunning",
    "COMAdminErrorCodes_COMAdminErrEventClassCannotBeSubscriber",
    "COMAdminErrorCodes_COMAdminErrLibAppProxyIncompatible",
    "COMAdminErrorCodes_COMAdminErrBasePartitionOnly",
    "COMAdminErrorCodes_COMAdminErrDuplicatePartitionName",
    "COMAdminErrorCodes_COMAdminErrPartitionInUse",
    "COMAdminErrorCodes_COMAdminErrImportedComponentsNotAllowed",
    "COMAdminErrorCodes_COMAdminErrRegdbNotInitialized",
    "COMAdminErrorCodes_COMAdminErrRegdbNotOpen",
    "COMAdminErrorCodes_COMAdminErrRegdbSystemErr",
    "COMAdminErrorCodes_COMAdminErrRegdbAlreadyRunning",
    "COMAdminErrorCodes_COMAdminErrMigVersionNotSupported",
    "COMAdminErrorCodes_COMAdminErrMigSchemaNotFound",
    "COMAdminErrorCodes_COMAdminErrCatBitnessMismatch",
    "COMAdminErrorCodes_COMAdminErrCatUnacceptableBitness",
    "COMAdminErrorCodes_COMAdminErrCatWrongAppBitnessBitness",
    "COMAdminErrorCodes_COMAdminErrCatPauseResumeNotSupported",
    "COMAdminErrorCodes_COMAdminErrCatServerFault",
    "COMAdminErrorCodes_COMAdminErrCantRecycleLibraryApps",
    "COMAdminErrorCodes_COMAdminErrCantRecycleServiceApps",
    "COMAdminErrorCodes_COMAdminErrProcessAlreadyRecycled",
    "COMAdminErrorCodes_COMAdminErrPausedProcessMayNotBeRecycled",
    "COMAdminErrorCodes_COMAdminErrInvalidPartition",
    "COMAdminErrorCodes_COMAdminErrPartitionMsiOnly",
    "COMAdminErrorCodes_COMAdminErrStartAppDisabled",
    "COMAdminErrorCodes_COMAdminErrCompMoveSource",
    "COMAdminErrorCodes_COMAdminErrCompMoveDest",
    "COMAdminErrorCodes_COMAdminErrCompMovePrivate",
    "COMAdminErrorCodes_COMAdminErrCannotCopyEventClass",
    "ISecurityIdentityColl",
    "ISecurityCallersColl",
    "ISecurityCallContext",
    "IGetSecurityCallContext",
    "SecurityProperty",
    "ContextInfo",
    "ContextInfo2",
    "ObjectContext",
    "ITransactionContextEx",
    "ITransactionContext",
    "ICreateWithTransactionEx",
    "ICreateWithLocalTransaction",
    "ICreateWithTipTransactionEx",
    "COMSVCSEVENTINFO",
    "IComLTxEvents",
    "IComUserEvent",
    "IComThreadEvents",
    "IComAppEvents",
    "IComInstanceEvents",
    "IComTransactionEvents",
    "IComMethodEvents",
    "IComObjectEvents",
    "IComResourceEvents",
    "IComSecurityEvents",
    "IComObjectPoolEvents",
    "IComObjectPoolEvents2",
    "IComObjectConstructionEvents",
    "IComActivityEvents",
    "IComIdentityEvents",
    "IComQCEvents",
    "IComExceptionEvents",
    "ILBEvents",
    "IComCRMEvents",
    "IComMethod2Events",
    "IComTrackingInfoEvents",
    "TRACKING_COLL_TYPE",
    "TRKCOLL_PROCESSES",
    "TRKCOLL_APPLICATIONS",
    "TRKCOLL_COMPONENTS",
    "IComTrackingInfoCollection",
    "IComTrackingInfoObject",
    "IComTrackingInfoProperties",
    "IComApp2Events",
    "IComTransaction2Events",
    "IComInstance2Events",
    "IComObjectPool2Events",
    "IComObjectConstruction2Events",
    "ISystemAppEventData",
    "IMtsEvents",
    "IMtsEventInfo",
    "IMTSLocator",
    "IMtsGrp",
    "IMessageMover",
    "IEventServerTrace",
    "RECYCLE_INFO",
    "DUMPTYPE",
    "DUMPTYPE_FULL",
    "DUMPTYPE_MINI",
    "DUMPTYPE_NONE",
    "HANG_INFO",
    "COMPLUS_APPTYPE",
    "APPTYPE_UNKNOWN",
    "APPTYPE_SERVER",
    "APPTYPE_LIBRARY",
    "APPTYPE_SWC",
    "CAppStatistics",
    "CAppData",
    "CCLSIDData",
    "CCLSIDData2",
    "GetAppTrackerDataFlags",
    "GATD_INCLUDE_PROCESS_EXE_NAME",
    "GATD_INCLUDE_LIBRARY_APPS",
    "GATD_INCLUDE_SWC",
    "GATD_INCLUDE_CLASS_NAME",
    "GATD_INCLUDE_APPLICATION_NAME",
    "ApplicationProcessSummary",
    "ApplicationProcessStatistics",
    "ApplicationProcessRecycleInfo",
    "ApplicationSummary",
    "ComponentSummary",
    "ComponentStatistics",
    "ComponentHangMonitorInfo",
    "IGetAppTrackerData",
    "IDispenserManager",
    "IHolder",
    "IDispenserDriver",
    "ITransactionProxy",
    "IContextSecurityPerimeter",
    "ITxProxyHolder",
    "IObjectContext",
    "IObjectControl",
    "IEnumNames",
    "ISecurityProperty",
    "ObjectControl",
    "ISharedProperty",
    "ISharedPropertyGroup",
    "ISharedPropertyGroupManager",
    "IObjectConstruct",
    "IObjectConstructString",
    "IObjectContextActivity",
    "IObjectContextInfo",
    "IObjectContextInfo2",
    "ITransactionStatus",
    "IObjectContextTip",
    "IPlaybackControl",
    "IGetContextProperties",
    "TransactionVote",
    "TransactionVote_TxCommit",
    "TransactionVote_TxAbort",
    "IContextState",
    "IPoolManager",
    "ISelectCOMLBServer",
    "ICOMLBArguments",
    "ICrmLogControl",
    "ICrmCompensatorVariants",
    "CrmLogRecordRead",
    "ICrmCompensator",
    "CrmTransactionState",
    "TxState_Active",
    "TxState_Committed",
    "TxState_Aborted",
    "TxState_Indoubt",
    "ICrmMonitorLogRecords",
    "ICrmMonitorClerks",
    "ICrmMonitor",
    "ICrmFormatLogRecords",
    "CSC_InheritanceConfig",
    "CSC_Inherit",
    "CSC_Ignore",
    "CSC_ThreadPool",
    "CSC_ThreadPoolNone",
    "CSC_ThreadPoolInherit",
    "CSC_STAThreadPool",
    "CSC_MTAThreadPool",
    "CSC_Binding",
    "CSC_NoBinding",
    "CSC_BindToPoolThread",
    "CSC_TransactionConfig",
    "CSC_NoTransaction",
    "CSC_IfContainerIsTransactional",
    "CSC_CreateTransactionIfNecessary",
    "CSC_NewTransaction",
    "CSC_SynchronizationConfig",
    "CSC_NoSynchronization",
    "CSC_IfContainerIsSynchronized",
    "CSC_NewSynchronizationIfNecessary",
    "CSC_NewSynchronization",
    "CSC_TrackerConfig",
    "CSC_DontUseTracker",
    "CSC_UseTracker",
    "CSC_PartitionConfig",
    "CSC_NoPartition",
    "CSC_InheritPartition",
    "CSC_NewPartition",
    "CSC_IISIntrinsicsConfig",
    "CSC_NoIISIntrinsics",
    "CSC_InheritIISIntrinsics",
    "CSC_COMTIIntrinsicsConfig",
    "CSC_NoCOMTIIntrinsics",
    "CSC_InheritCOMTIIntrinsics",
    "CSC_SxsConfig",
    "CSC_NoSxs",
    "CSC_InheritSxs",
    "CSC_NewSxs",
    "IServiceIISIntrinsicsConfig",
    "IServiceComTIIntrinsicsConfig",
    "IServiceSxsConfig",
    "ICheckSxsConfig",
    "IServiceInheritanceConfig",
    "IServiceThreadPoolConfig",
    "IServiceTransactionConfigBase",
    "IServiceTransactionConfig",
    "IServiceSysTxnConfig",
    "IServiceSynchronizationConfig",
    "IServiceTrackerConfig",
    "IServicePartitionConfig",
    "IServiceCall",
    "IAsyncErrorNotify",
    "IServiceActivity",
    "IThreadPoolKnobs",
    "IComStaThreadPoolKnobs",
    "IComMtaThreadPoolKnobs",
    "IComStaThreadPoolKnobs2",
    "IProcessInitializer",
    "IServicePoolConfig",
    "IServicePool",
    "IManagedPooledObj",
    "IManagedPoolAction",
    "IManagedObjectInfo",
    "IAppDomainHelper",
    "IAssemblyLocator",
    "IManagedActivationEvents",
    "ISendMethodEvents",
    "ITransactionResourcePool",
    "IMTSCall",
    "IContextProperties",
    "IObjPool",
    "ITransactionProperty",
    "IMTSActivity",
    "AutoSvcs_Error_Constants",
    "AutoSvcs_Error_Constants_mtsErrCtxAborted",
    "AutoSvcs_Error_Constants_mtsErrCtxAborting",
    "AutoSvcs_Error_Constants_mtsErrCtxNoContext",
    "AutoSvcs_Error_Constants_mtsErrCtxNotRegistered",
    "AutoSvcs_Error_Constants_mtsErrCtxSynchTimeout",
    "AutoSvcs_Error_Constants_mtsErrCtxOldReference",
    "AutoSvcs_Error_Constants_mtsErrCtxRoleNotFound",
    "AutoSvcs_Error_Constants_mtsErrCtxNoSecurity",
    "AutoSvcs_Error_Constants_mtsErrCtxWrongThread",
    "AutoSvcs_Error_Constants_mtsErrCtxTMNotAvailable",
    "AutoSvcs_Error_Constants_comQCErrApplicationNotQueued",
    "AutoSvcs_Error_Constants_comQCErrNoQueueableInterfaces",
    "AutoSvcs_Error_Constants_comQCErrQueuingServiceNotAvailable",
    "AutoSvcs_Error_Constants_comQCErrQueueTransactMismatch",
    "AutoSvcs_Error_Constants_comqcErrRecorderMarshalled",
    "AutoSvcs_Error_Constants_comqcErrOutParam",
    "AutoSvcs_Error_Constants_comqcErrRecorderNotTrusted",
    "AutoSvcs_Error_Constants_comqcErrPSLoad",
    "AutoSvcs_Error_Constants_comqcErrMarshaledObjSameTxn",
    "AutoSvcs_Error_Constants_comqcErrInvalidMessage",
    "AutoSvcs_Error_Constants_comqcErrMsmqSidUnavailable",
    "AutoSvcs_Error_Constants_comqcErrWrongMsgExtension",
    "AutoSvcs_Error_Constants_comqcErrMsmqServiceUnavailable",
    "AutoSvcs_Error_Constants_comqcErrMsgNotAuthenticated",
    "AutoSvcs_Error_Constants_comqcErrMsmqConnectorUsed",
    "AutoSvcs_Error_Constants_comqcErrBadMarshaledObject",
    "LockModes",
    "LockModes_LockSetGet",
    "LockModes_LockMethod",
    "ReleaseModes",
    "ReleaseModes_Standard",
    "ReleaseModes_Process",
    "CRMFLAGS",
    "CRMFLAG_FORGETTARGET",
    "CRMFLAG_WRITTENDURINGPREPARE",
    "CRMFLAG_WRITTENDURINGCOMMIT",
    "CRMFLAG_WRITTENDURINGABORT",
    "CRMFLAG_WRITTENDURINGRECOVERY",
    "CRMFLAG_WRITTENDURINGREPLAY",
    "CRMFLAG_REPLAYINPROGRESS",
    "CRMREGFLAGS",
    "CRMREGFLAG_PREPAREPHASE",
    "CRMREGFLAG_COMMITPHASE",
    "CRMREGFLAG_ABORTPHASE",
    "CRMREGFLAG_ALLPHASES",
    "CRMREGFLAG_FAILIFINDOUBTSREMAIN",
    "CoGetDefaultContext",
    "CoCreateActivity",
    "CoEnterServiceDomain",
    "CoLeaveServiceDomain",
    "GetManagedExtensions",
    "SafeRef",
    "RecycleSurrogate",
    "MTSCreateActivity",
    "GetDispenserManager",
]
