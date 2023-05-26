from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.ComponentServices
import Windows.Win32.System.DistributedTransactionCoordinator
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class APPDATA(EasyCastStructure):
    m_idApp: UInt32
    m_szAppGuid: Char * 40
    m_dwAppProcessId: UInt32
    m_AppStatistics: Windows.Win32.System.ComponentServices.APPSTATISTICS
class APPSTATISTICS(EasyCastStructure):
    m_cTotalCalls: UInt32
    m_cTotalInstances: UInt32
    m_cTotalClasses: UInt32
    m_cCallsPerSecond: UInt32
TRACKER_STARTSTOP_EVENT: String = 'Global\\COM+ Tracker Push Event'
TRACKER_INIT_EVENT: String = 'Global\\COM+ Tracker Init Event'
GUID_STRING_SIZE: UInt32 = 40
DATA_NOT_AVAILABLE: UInt32 = 4294967295
MTXDM_E_ENLISTRESOURCEFAILED: UInt32 = 2147803392
CRR_NO_REASON_SUPPLIED: UInt32 = 0
CRR_LIFETIME_LIMIT: UInt32 = 4294967295
CRR_ACTIVATION_LIMIT: UInt32 = 4294967294
CRR_CALL_LIMIT: UInt32 = 4294967293
CRR_MEMORY_LIMIT: UInt32 = 4294967292
CRR_RECYCLED_FROM_UI: UInt32 = 4294967291
@winfunctype('OLE32.dll')
def CoGetDefaultContext(aptType: Windows.Win32.System.Com.APTTYPE, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoCreateActivity(pIUnknown: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppObj: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoEnterServiceDomain(pConfigObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoLeaveServiceDomain(pUnkStatus: Windows.Win32.System.Com.IUnknown_head) -> Void: ...
@winfunctype('comsvcs.dll')
def GetManagedExtensions(dwExts: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('comsvcs.dll')
def SafeRef(rid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head) -> VoidPtr: ...
@cfunctype('comsvcs.dll')
def RecycleSurrogate(lReasonCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def MTSCreateActivity(riid: POINTER(Guid), ppobj: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('MTxDM.dll')
def GetDispenserManager(param0: POINTER(Windows.Win32.System.ComponentServices.IDispenserManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
AppDomainHelper = Guid('{ef24f689-14f8-4d92-b4af-d7b1f0e70fd4}')
class ApplicationProcessRecycleInfo(EasyCastStructure):
    IsRecyclable: Windows.Win32.Foundation.BOOL
    IsRecycled: Windows.Win32.Foundation.BOOL
    TimeRecycled: Windows.Win32.Foundation.FILETIME
    TimeToTerminate: Windows.Win32.Foundation.FILETIME
    RecycleReasonCode: Int32
    IsPendingRecycle: Windows.Win32.Foundation.BOOL
    HasAutomaticLifetimeRecycling: Windows.Win32.Foundation.BOOL
    TimeForAutomaticRecycling: Windows.Win32.Foundation.FILETIME
    MemoryLimitInKB: UInt32
    MemoryUsageInKBLastCheck: UInt32
    ActivationLimit: UInt32
    NumActivationsLastReported: UInt32
    CallLimit: UInt32
    NumCallsLastReported: UInt32
class ApplicationProcessStatistics(EasyCastStructure):
    NumCallsOutstanding: UInt32
    NumTrackedComponents: UInt32
    NumComponentInstances: UInt32
    AvgCallsPerSecond: UInt32
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: UInt32
    Reserved4: UInt32
class ApplicationProcessSummary(EasyCastStructure):
    PartitionIdPrimaryApplication: Guid
    ApplicationIdPrimaryApplication: Guid
    ApplicationInstanceId: Guid
    ProcessId: UInt32
    Type: Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    ProcessExeName: Windows.Win32.Foundation.PWSTR
    IsService: Windows.Win32.Foundation.BOOL
    IsPaused: Windows.Win32.Foundation.BOOL
    IsRecycled: Windows.Win32.Foundation.BOOL
class ApplicationSummary(EasyCastStructure):
    ApplicationInstanceId: Guid
    PartitionId: Guid
    ApplicationId: Guid
    Type: Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    ApplicationName: Windows.Win32.Foundation.PWSTR
    NumTrackedComponents: UInt32
    NumComponentInstances: UInt32
AutoSvcs_Error_Constants = UInt32
AutoSvcs_Error_Constants_mtsErrCtxAborted: AutoSvcs_Error_Constants = 2147803138
AutoSvcs_Error_Constants_mtsErrCtxAborting: AutoSvcs_Error_Constants = 2147803139
AutoSvcs_Error_Constants_mtsErrCtxNoContext: AutoSvcs_Error_Constants = 2147803140
AutoSvcs_Error_Constants_mtsErrCtxNotRegistered: AutoSvcs_Error_Constants = 2147803141
AutoSvcs_Error_Constants_mtsErrCtxSynchTimeout: AutoSvcs_Error_Constants = 2147803142
AutoSvcs_Error_Constants_mtsErrCtxOldReference: AutoSvcs_Error_Constants = 2147803143
AutoSvcs_Error_Constants_mtsErrCtxRoleNotFound: AutoSvcs_Error_Constants = 2147803148
AutoSvcs_Error_Constants_mtsErrCtxNoSecurity: AutoSvcs_Error_Constants = 2147803149
AutoSvcs_Error_Constants_mtsErrCtxWrongThread: AutoSvcs_Error_Constants = 2147803150
AutoSvcs_Error_Constants_mtsErrCtxTMNotAvailable: AutoSvcs_Error_Constants = 2147803151
AutoSvcs_Error_Constants_comQCErrApplicationNotQueued: AutoSvcs_Error_Constants = 2148599296
AutoSvcs_Error_Constants_comQCErrNoQueueableInterfaces: AutoSvcs_Error_Constants = 2148599297
AutoSvcs_Error_Constants_comQCErrQueuingServiceNotAvailable: AutoSvcs_Error_Constants = 2148599298
AutoSvcs_Error_Constants_comQCErrQueueTransactMismatch: AutoSvcs_Error_Constants = 2148599299
AutoSvcs_Error_Constants_comqcErrRecorderMarshalled: AutoSvcs_Error_Constants = 2148599300
AutoSvcs_Error_Constants_comqcErrOutParam: AutoSvcs_Error_Constants = 2148599301
AutoSvcs_Error_Constants_comqcErrRecorderNotTrusted: AutoSvcs_Error_Constants = 2148599302
AutoSvcs_Error_Constants_comqcErrPSLoad: AutoSvcs_Error_Constants = 2148599303
AutoSvcs_Error_Constants_comqcErrMarshaledObjSameTxn: AutoSvcs_Error_Constants = 2148599304
AutoSvcs_Error_Constants_comqcErrInvalidMessage: AutoSvcs_Error_Constants = 2148599376
AutoSvcs_Error_Constants_comqcErrMsmqSidUnavailable: AutoSvcs_Error_Constants = 2148599377
AutoSvcs_Error_Constants_comqcErrWrongMsgExtension: AutoSvcs_Error_Constants = 2148599378
AutoSvcs_Error_Constants_comqcErrMsmqServiceUnavailable: AutoSvcs_Error_Constants = 2148599379
AutoSvcs_Error_Constants_comqcErrMsgNotAuthenticated: AutoSvcs_Error_Constants = 2148599380
AutoSvcs_Error_Constants_comqcErrMsmqConnectorUsed: AutoSvcs_Error_Constants = 2148599381
AutoSvcs_Error_Constants_comqcErrBadMarshaledObject: AutoSvcs_Error_Constants = 2148599382
ByotServerEx = Guid('{ecabb0aa-7f19-11d2-978e-0000f8757e2a}')
class CLSIDDATA(EasyCastStructure):
    m_clsid: Guid
    m_cReferences: UInt32
    m_cBound: UInt32
    m_cPooled: UInt32
    m_cInCall: UInt32
    m_dwRespTime: UInt32
    m_cCallsCompleted: UInt32
    m_cCallsFailed: UInt32
class CLSIDDATA2(EasyCastStructure):
    m_clsid: Guid
    m_appid: Guid
    m_partid: Guid
    m_pwszAppName: Windows.Win32.Foundation.PWSTR
    m_pwszCtxName: Windows.Win32.Foundation.PWSTR
    m_eAppType: Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    m_cReferences: UInt32
    m_cBound: UInt32
    m_cPooled: UInt32
    m_cInCall: UInt32
    m_dwRespTime: UInt32
    m_cCallsCompleted: UInt32
    m_cCallsFailed: UInt32
COMAdminAccessChecksLevelOptions = Int32
COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationLevel: COMAdminAccessChecksLevelOptions = 0
COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationComponentLevel: COMAdminAccessChecksLevelOptions = 1
COMAdminActivationOptions = Int32
COMAdminActivationOptions_COMAdminActivationInproc: COMAdminActivationOptions = 0
COMAdminActivationOptions_COMAdminActivationLocal: COMAdminActivationOptions = 1
COMAdminApplicationExportOptions = Int32
COMAdminApplicationExportOptions_COMAdminExportNoUsers: COMAdminApplicationExportOptions = 0
COMAdminApplicationExportOptions_COMAdminExportUsers: COMAdminApplicationExportOptions = 1
COMAdminApplicationExportOptions_COMAdminExportApplicationProxy: COMAdminApplicationExportOptions = 2
COMAdminApplicationExportOptions_COMAdminExportForceOverwriteOfFiles: COMAdminApplicationExportOptions = 4
COMAdminApplicationExportOptions_COMAdminExportIn10Format: COMAdminApplicationExportOptions = 16
COMAdminApplicationInstallOptions = Int32
COMAdminApplicationInstallOptions_COMAdminInstallNoUsers: COMAdminApplicationInstallOptions = 0
COMAdminApplicationInstallOptions_COMAdminInstallUsers: COMAdminApplicationInstallOptions = 1
COMAdminApplicationInstallOptions_COMAdminInstallForceOverwriteOfFiles: COMAdminApplicationInstallOptions = 2
COMAdminAuthenticationCapabilitiesOptions = Int32
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesNone: COMAdminAuthenticationCapabilitiesOptions = 0
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesSecureReference: COMAdminAuthenticationCapabilitiesOptions = 2
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesStaticCloaking: COMAdminAuthenticationCapabilitiesOptions = 32
COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesDynamicCloaking: COMAdminAuthenticationCapabilitiesOptions = 64
COMAdminAuthenticationLevelOptions = Int32
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationDefault: COMAdminAuthenticationLevelOptions = 0
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationNone: COMAdminAuthenticationLevelOptions = 1
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationConnect: COMAdminAuthenticationLevelOptions = 2
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationCall: COMAdminAuthenticationLevelOptions = 3
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPacket: COMAdminAuthenticationLevelOptions = 4
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationIntegrity: COMAdminAuthenticationLevelOptions = 5
COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPrivacy: COMAdminAuthenticationLevelOptions = 6
COMAdminCatalog = Guid('{f618c514-dfb8-11d1-a2cf-00805fc79235}')
COMAdminCatalogCollection = Guid('{f618c516-dfb8-11d1-a2cf-00805fc79235}')
COMAdminCatalogObject = Guid('{f618c515-dfb8-11d1-a2cf-00805fc79235}')
COMAdminComponentFlags = Int32
COMAdminComponentFlags_COMAdminCompFlagTypeInfoFound: COMAdminComponentFlags = 1
COMAdminComponentFlags_COMAdminCompFlagCOMPlusPropertiesFound: COMAdminComponentFlags = 2
COMAdminComponentFlags_COMAdminCompFlagProxyFound: COMAdminComponentFlags = 4
COMAdminComponentFlags_COMAdminCompFlagInterfacesFound: COMAdminComponentFlags = 8
COMAdminComponentFlags_COMAdminCompFlagAlreadyInstalled: COMAdminComponentFlags = 16
COMAdminComponentFlags_COMAdminCompFlagNotInApplication: COMAdminComponentFlags = 32
COMAdminComponentType = Int32
COMAdminComponentType_COMAdmin32BitComponent: COMAdminComponentType = 1
COMAdminComponentType_COMAdmin64BitComponent: COMAdminComponentType = 2
COMAdminErrorCodes = Int32
COMAdminErrorCodes_COMAdminErrObjectErrors: COMAdminErrorCodes = -2146368511
COMAdminErrorCodes_COMAdminErrObjectInvalid: COMAdminErrorCodes = -2146368510
COMAdminErrorCodes_COMAdminErrKeyMissing: COMAdminErrorCodes = -2146368509
COMAdminErrorCodes_COMAdminErrAlreadyInstalled: COMAdminErrorCodes = -2146368508
COMAdminErrorCodes_COMAdminErrAppFileWriteFail: COMAdminErrorCodes = -2146368505
COMAdminErrorCodes_COMAdminErrAppFileReadFail: COMAdminErrorCodes = -2146368504
COMAdminErrorCodes_COMAdminErrAppFileVersion: COMAdminErrorCodes = -2146368503
COMAdminErrorCodes_COMAdminErrBadPath: COMAdminErrorCodes = -2146368502
COMAdminErrorCodes_COMAdminErrApplicationExists: COMAdminErrorCodes = -2146368501
COMAdminErrorCodes_COMAdminErrRoleExists: COMAdminErrorCodes = -2146368500
COMAdminErrorCodes_COMAdminErrCantCopyFile: COMAdminErrorCodes = -2146368499
COMAdminErrorCodes_COMAdminErrNoUser: COMAdminErrorCodes = -2146368497
COMAdminErrorCodes_COMAdminErrInvalidUserids: COMAdminErrorCodes = -2146368496
COMAdminErrorCodes_COMAdminErrNoRegistryCLSID: COMAdminErrorCodes = -2146368495
COMAdminErrorCodes_COMAdminErrBadRegistryProgID: COMAdminErrorCodes = -2146368494
COMAdminErrorCodes_COMAdminErrAuthenticationLevel: COMAdminErrorCodes = -2146368493
COMAdminErrorCodes_COMAdminErrUserPasswdNotValid: COMAdminErrorCodes = -2146368492
COMAdminErrorCodes_COMAdminErrCLSIDOrIIDMismatch: COMAdminErrorCodes = -2146368488
COMAdminErrorCodes_COMAdminErrRemoteInterface: COMAdminErrorCodes = -2146368487
COMAdminErrorCodes_COMAdminErrDllRegisterServer: COMAdminErrorCodes = -2146368486
COMAdminErrorCodes_COMAdminErrNoServerShare: COMAdminErrorCodes = -2146368485
COMAdminErrorCodes_COMAdminErrDllLoadFailed: COMAdminErrorCodes = -2146368483
COMAdminErrorCodes_COMAdminErrBadRegistryLibID: COMAdminErrorCodes = -2146368482
COMAdminErrorCodes_COMAdminErrAppDirNotFound: COMAdminErrorCodes = -2146368481
COMAdminErrorCodes_COMAdminErrRegistrarFailed: COMAdminErrorCodes = -2146368477
COMAdminErrorCodes_COMAdminErrCompFileDoesNotExist: COMAdminErrorCodes = -2146368476
COMAdminErrorCodes_COMAdminErrCompFileLoadDLLFail: COMAdminErrorCodes = -2146368475
COMAdminErrorCodes_COMAdminErrCompFileGetClassObj: COMAdminErrorCodes = -2146368474
COMAdminErrorCodes_COMAdminErrCompFileClassNotAvail: COMAdminErrorCodes = -2146368473
COMAdminErrorCodes_COMAdminErrCompFileBadTLB: COMAdminErrorCodes = -2146368472
COMAdminErrorCodes_COMAdminErrCompFileNotInstallable: COMAdminErrorCodes = -2146368471
COMAdminErrorCodes_COMAdminErrNotChangeable: COMAdminErrorCodes = -2146368470
COMAdminErrorCodes_COMAdminErrNotDeletable: COMAdminErrorCodes = -2146368469
COMAdminErrorCodes_COMAdminErrSession: COMAdminErrorCodes = -2146368468
COMAdminErrorCodes_COMAdminErrCompMoveLocked: COMAdminErrorCodes = -2146368467
COMAdminErrorCodes_COMAdminErrCompMoveBadDest: COMAdminErrorCodes = -2146368466
COMAdminErrorCodes_COMAdminErrRegisterTLB: COMAdminErrorCodes = -2146368464
COMAdminErrorCodes_COMAdminErrSystemApp: COMAdminErrorCodes = -2146368461
COMAdminErrorCodes_COMAdminErrCompFileNoRegistrar: COMAdminErrorCodes = -2146368460
COMAdminErrorCodes_COMAdminErrCoReqCompInstalled: COMAdminErrorCodes = -2146368459
COMAdminErrorCodes_COMAdminErrServiceNotInstalled: COMAdminErrorCodes = -2146368458
COMAdminErrorCodes_COMAdminErrPropertySaveFailed: COMAdminErrorCodes = -2146368457
COMAdminErrorCodes_COMAdminErrObjectExists: COMAdminErrorCodes = -2146368456
COMAdminErrorCodes_COMAdminErrComponentExists: COMAdminErrorCodes = -2146368455
COMAdminErrorCodes_COMAdminErrRegFileCorrupt: COMAdminErrorCodes = -2146368453
COMAdminErrorCodes_COMAdminErrPropertyOverflow: COMAdminErrorCodes = -2146368452
COMAdminErrorCodes_COMAdminErrNotInRegistry: COMAdminErrorCodes = -2146368450
COMAdminErrorCodes_COMAdminErrObjectNotPoolable: COMAdminErrorCodes = -2146368449
COMAdminErrorCodes_COMAdminErrApplidMatchesClsid: COMAdminErrorCodes = -2146368442
COMAdminErrorCodes_COMAdminErrRoleDoesNotExist: COMAdminErrorCodes = -2146368441
COMAdminErrorCodes_COMAdminErrStartAppNeedsComponents: COMAdminErrorCodes = -2146368440
COMAdminErrorCodes_COMAdminErrRequiresDifferentPlatform: COMAdminErrorCodes = -2146368439
COMAdminErrorCodes_COMAdminErrQueuingServiceNotAvailable: COMAdminErrorCodes = -2146367998
COMAdminErrorCodes_COMAdminErrObjectParentMissing: COMAdminErrorCodes = -2146367480
COMAdminErrorCodes_COMAdminErrObjectDoesNotExist: COMAdminErrorCodes = -2146367479
COMAdminErrorCodes_COMAdminErrCanNotExportAppProxy: COMAdminErrorCodes = -2146368438
COMAdminErrorCodes_COMAdminErrCanNotStartApp: COMAdminErrorCodes = -2146368437
COMAdminErrorCodes_COMAdminErrCanNotExportSystemApp: COMAdminErrorCodes = -2146368436
COMAdminErrorCodes_COMAdminErrCanNotSubscribeToComponent: COMAdminErrorCodes = -2146368435
COMAdminErrorCodes_COMAdminErrAppNotRunning: COMAdminErrorCodes = -2146367478
COMAdminErrorCodes_COMAdminErrEventClassCannotBeSubscriber: COMAdminErrorCodes = -2146368434
COMAdminErrorCodes_COMAdminErrLibAppProxyIncompatible: COMAdminErrorCodes = -2146368433
COMAdminErrorCodes_COMAdminErrBasePartitionOnly: COMAdminErrorCodes = -2146368432
COMAdminErrorCodes_COMAdminErrDuplicatePartitionName: COMAdminErrorCodes = -2146368425
COMAdminErrorCodes_COMAdminErrPartitionInUse: COMAdminErrorCodes = -2146368423
COMAdminErrorCodes_COMAdminErrImportedComponentsNotAllowed: COMAdminErrorCodes = -2146368421
COMAdminErrorCodes_COMAdminErrRegdbNotInitialized: COMAdminErrorCodes = -2146368398
COMAdminErrorCodes_COMAdminErrRegdbNotOpen: COMAdminErrorCodes = -2146368397
COMAdminErrorCodes_COMAdminErrRegdbSystemErr: COMAdminErrorCodes = -2146368396
COMAdminErrorCodes_COMAdminErrRegdbAlreadyRunning: COMAdminErrorCodes = -2146368395
COMAdminErrorCodes_COMAdminErrMigVersionNotSupported: COMAdminErrorCodes = -2146368384
COMAdminErrorCodes_COMAdminErrMigSchemaNotFound: COMAdminErrorCodes = -2146368383
COMAdminErrorCodes_COMAdminErrCatBitnessMismatch: COMAdminErrorCodes = -2146368382
COMAdminErrorCodes_COMAdminErrCatUnacceptableBitness: COMAdminErrorCodes = -2146368381
COMAdminErrorCodes_COMAdminErrCatWrongAppBitnessBitness: COMAdminErrorCodes = -2146368380
COMAdminErrorCodes_COMAdminErrCatPauseResumeNotSupported: COMAdminErrorCodes = -2146368379
COMAdminErrorCodes_COMAdminErrCatServerFault: COMAdminErrorCodes = -2146368378
COMAdminErrorCodes_COMAdminErrCantRecycleLibraryApps: COMAdminErrorCodes = -2146367473
COMAdminErrorCodes_COMAdminErrCantRecycleServiceApps: COMAdminErrorCodes = -2146367471
COMAdminErrorCodes_COMAdminErrProcessAlreadyRecycled: COMAdminErrorCodes = -2146367470
COMAdminErrorCodes_COMAdminErrPausedProcessMayNotBeRecycled: COMAdminErrorCodes = -2146367469
COMAdminErrorCodes_COMAdminErrInvalidPartition: COMAdminErrorCodes = -2146367477
COMAdminErrorCodes_COMAdminErrPartitionMsiOnly: COMAdminErrorCodes = -2146367463
COMAdminErrorCodes_COMAdminErrStartAppDisabled: COMAdminErrorCodes = -2146368431
COMAdminErrorCodes_COMAdminErrCompMoveSource: COMAdminErrorCodes = -2146367460
COMAdminErrorCodes_COMAdminErrCompMoveDest: COMAdminErrorCodes = -2146367459
COMAdminErrorCodes_COMAdminErrCompMovePrivate: COMAdminErrorCodes = -2146367458
COMAdminErrorCodes_COMAdminErrCannotCopyEventClass: COMAdminErrorCodes = -2146367456
COMAdminFileFlags = Int32
COMAdminFileFlags_COMAdminFileFlagLoadable: COMAdminFileFlags = 1
COMAdminFileFlags_COMAdminFileFlagCOM: COMAdminFileFlags = 2
COMAdminFileFlags_COMAdminFileFlagContainsPS: COMAdminFileFlags = 4
COMAdminFileFlags_COMAdminFileFlagContainsComp: COMAdminFileFlags = 8
COMAdminFileFlags_COMAdminFileFlagContainsTLB: COMAdminFileFlags = 16
COMAdminFileFlags_COMAdminFileFlagSelfReg: COMAdminFileFlags = 32
COMAdminFileFlags_COMAdminFileFlagSelfUnReg: COMAdminFileFlags = 64
COMAdminFileFlags_COMAdminFileFlagUnloadableDLL: COMAdminFileFlags = 128
COMAdminFileFlags_COMAdminFileFlagDoesNotExist: COMAdminFileFlags = 256
COMAdminFileFlags_COMAdminFileFlagAlreadyInstalled: COMAdminFileFlags = 512
COMAdminFileFlags_COMAdminFileFlagBadTLB: COMAdminFileFlags = 1024
COMAdminFileFlags_COMAdminFileFlagGetClassObjFailed: COMAdminFileFlags = 2048
COMAdminFileFlags_COMAdminFileFlagClassNotAvailable: COMAdminFileFlags = 4096
COMAdminFileFlags_COMAdminFileFlagRegistrar: COMAdminFileFlags = 8192
COMAdminFileFlags_COMAdminFileFlagNoRegistrar: COMAdminFileFlags = 16384
COMAdminFileFlags_COMAdminFileFlagDLLRegsvrFailed: COMAdminFileFlags = 32768
COMAdminFileFlags_COMAdminFileFlagRegTLBFailed: COMAdminFileFlags = 65536
COMAdminFileFlags_COMAdminFileFlagRegistrarFailed: COMAdminFileFlags = 131072
COMAdminFileFlags_COMAdminFileFlagError: COMAdminFileFlags = 262144
COMAdminImpersonationLevelOptions = Int32
COMAdminImpersonationLevelOptions_COMAdminImpersonationAnonymous: COMAdminImpersonationLevelOptions = 1
COMAdminImpersonationLevelOptions_COMAdminImpersonationIdentify: COMAdminImpersonationLevelOptions = 2
COMAdminImpersonationLevelOptions_COMAdminImpersonationImpersonate: COMAdminImpersonationLevelOptions = 3
COMAdminImpersonationLevelOptions_COMAdminImpersonationDelegate: COMAdminImpersonationLevelOptions = 4
COMAdminInUse = Int32
COMAdminInUse_COMAdminNotInUse: COMAdminInUse = 0
COMAdminInUse_COMAdminInUseByCatalog: COMAdminInUse = 1
COMAdminInUse_COMAdminInUseByRegistryUnknown: COMAdminInUse = 2
COMAdminInUse_COMAdminInUseByRegistryProxyStub: COMAdminInUse = 3
COMAdminInUse_COMAdminInUseByRegistryTypeLib: COMAdminInUse = 4
COMAdminInUse_COMAdminInUseByRegistryClsid: COMAdminInUse = 5
COMAdminOS = Int32
COMAdminOS_COMAdminOSNotInitialized: COMAdminOS = 0
COMAdminOS_COMAdminOSWindows3_1: COMAdminOS = 1
COMAdminOS_COMAdminOSWindows9x: COMAdminOS = 2
COMAdminOS_COMAdminOSWindows2000: COMAdminOS = 3
COMAdminOS_COMAdminOSWindows2000AdvancedServer: COMAdminOS = 4
COMAdminOS_COMAdminOSWindows2000Unknown: COMAdminOS = 5
COMAdminOS_COMAdminOSUnknown: COMAdminOS = 6
COMAdminOS_COMAdminOSWindowsXPPersonal: COMAdminOS = 11
COMAdminOS_COMAdminOSWindowsXPProfessional: COMAdminOS = 12
COMAdminOS_COMAdminOSWindowsNETStandardServer: COMAdminOS = 13
COMAdminOS_COMAdminOSWindowsNETEnterpriseServer: COMAdminOS = 14
COMAdminOS_COMAdminOSWindowsNETDatacenterServer: COMAdminOS = 15
COMAdminOS_COMAdminOSWindowsNETWebServer: COMAdminOS = 16
COMAdminOS_COMAdminOSWindowsLonghornPersonal: COMAdminOS = 17
COMAdminOS_COMAdminOSWindowsLonghornProfessional: COMAdminOS = 18
COMAdminOS_COMAdminOSWindowsLonghornStandardServer: COMAdminOS = 19
COMAdminOS_COMAdminOSWindowsLonghornEnterpriseServer: COMAdminOS = 20
COMAdminOS_COMAdminOSWindowsLonghornDatacenterServer: COMAdminOS = 21
COMAdminOS_COMAdminOSWindowsLonghornWebServer: COMAdminOS = 22
COMAdminOS_COMAdminOSWindows7Personal: COMAdminOS = 23
COMAdminOS_COMAdminOSWindows7Professional: COMAdminOS = 24
COMAdminOS_COMAdminOSWindows7StandardServer: COMAdminOS = 25
COMAdminOS_COMAdminOSWindows7EnterpriseServer: COMAdminOS = 26
COMAdminOS_COMAdminOSWindows7DatacenterServer: COMAdminOS = 27
COMAdminOS_COMAdminOSWindows7WebServer: COMAdminOS = 28
COMAdminOS_COMAdminOSWindows8Personal: COMAdminOS = 29
COMAdminOS_COMAdminOSWindows8Professional: COMAdminOS = 30
COMAdminOS_COMAdminOSWindows8StandardServer: COMAdminOS = 31
COMAdminOS_COMAdminOSWindows8EnterpriseServer: COMAdminOS = 32
COMAdminOS_COMAdminOSWindows8DatacenterServer: COMAdminOS = 33
COMAdminOS_COMAdminOSWindows8WebServer: COMAdminOS = 34
COMAdminOS_COMAdminOSWindowsBluePersonal: COMAdminOS = 35
COMAdminOS_COMAdminOSWindowsBlueProfessional: COMAdminOS = 36
COMAdminOS_COMAdminOSWindowsBlueStandardServer: COMAdminOS = 37
COMAdminOS_COMAdminOSWindowsBlueEnterpriseServer: COMAdminOS = 38
COMAdminOS_COMAdminOSWindowsBlueDatacenterServer: COMAdminOS = 39
COMAdminOS_COMAdminOSWindowsBlueWebServer: COMAdminOS = 40
COMAdminQCMessageAuthenticateOptions = Int32
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateSecureApps: COMAdminQCMessageAuthenticateOptions = 0
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOff: COMAdminQCMessageAuthenticateOptions = 1
COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOn: COMAdminQCMessageAuthenticateOptions = 2
COMAdminServiceOptions = Int32
COMAdminServiceOptions_COMAdminServiceLoadBalanceRouter: COMAdminServiceOptions = 1
COMAdminServiceStatusOptions = Int32
COMAdminServiceStatusOptions_COMAdminServiceStopped: COMAdminServiceStatusOptions = 0
COMAdminServiceStatusOptions_COMAdminServiceStartPending: COMAdminServiceStatusOptions = 1
COMAdminServiceStatusOptions_COMAdminServiceStopPending: COMAdminServiceStatusOptions = 2
COMAdminServiceStatusOptions_COMAdminServiceRunning: COMAdminServiceStatusOptions = 3
COMAdminServiceStatusOptions_COMAdminServiceContinuePending: COMAdminServiceStatusOptions = 4
COMAdminServiceStatusOptions_COMAdminServicePausePending: COMAdminServiceStatusOptions = 5
COMAdminServiceStatusOptions_COMAdminServicePaused: COMAdminServiceStatusOptions = 6
COMAdminServiceStatusOptions_COMAdminServiceUnknownState: COMAdminServiceStatusOptions = 7
COMAdminSynchronizationOptions = Int32
COMAdminSynchronizationOptions_COMAdminSynchronizationIgnored: COMAdminSynchronizationOptions = 0
COMAdminSynchronizationOptions_COMAdminSynchronizationNone: COMAdminSynchronizationOptions = 1
COMAdminSynchronizationOptions_COMAdminSynchronizationSupported: COMAdminSynchronizationOptions = 2
COMAdminSynchronizationOptions_COMAdminSynchronizationRequired: COMAdminSynchronizationOptions = 3
COMAdminSynchronizationOptions_COMAdminSynchronizationRequiresNew: COMAdminSynchronizationOptions = 4
COMAdminThreadingModels = Int32
COMAdminThreadingModels_COMAdminThreadingModelApartment: COMAdminThreadingModels = 0
COMAdminThreadingModels_COMAdminThreadingModelFree: COMAdminThreadingModels = 1
COMAdminThreadingModels_COMAdminThreadingModelMain: COMAdminThreadingModels = 2
COMAdminThreadingModels_COMAdminThreadingModelBoth: COMAdminThreadingModels = 3
COMAdminThreadingModels_COMAdminThreadingModelNeutral: COMAdminThreadingModels = 4
COMAdminThreadingModels_COMAdminThreadingModelNotSpecified: COMAdminThreadingModels = 5
COMAdminTransactionOptions = Int32
COMAdminTransactionOptions_COMAdminTransactionIgnored: COMAdminTransactionOptions = 0
COMAdminTransactionOptions_COMAdminTransactionNone: COMAdminTransactionOptions = 1
COMAdminTransactionOptions_COMAdminTransactionSupported: COMAdminTransactionOptions = 2
COMAdminTransactionOptions_COMAdminTransactionRequired: COMAdminTransactionOptions = 3
COMAdminTransactionOptions_COMAdminTransactionRequiresNew: COMAdminTransactionOptions = 4
COMAdminTxIsolationLevelOptions = Int32
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelAny: COMAdminTxIsolationLevelOptions = 0
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadUnCommitted: COMAdminTxIsolationLevelOptions = 1
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadCommitted: COMAdminTxIsolationLevelOptions = 2
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelRepeatableRead: COMAdminTxIsolationLevelOptions = 3
COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelSerializable: COMAdminTxIsolationLevelOptions = 4
COMEvents = Guid('{ecabb0ab-7f19-11d2-978e-0000f8757e2a}')
COMPLUS_APPTYPE = Int32
APPTYPE_UNKNOWN: COMPLUS_APPTYPE = -1
APPTYPE_SERVER: COMPLUS_APPTYPE = 1
APPTYPE_LIBRARY: COMPLUS_APPTYPE = 0
APPTYPE_SWC: COMPLUS_APPTYPE = 2
class COMSVCSEVENTINFO(EasyCastStructure):
    cbSize: UInt32
    dwPid: UInt32
    lTime: Int64
    lMicroTime: Int32
    perfCount: Int64
    guidApp: Guid
    sMachineName: Windows.Win32.Foundation.PWSTR
CRMClerk = Guid('{ecabb0bd-7f19-11d2-978e-0000f8757e2a}')
CRMFLAGS = Int32
CRMFLAG_FORGETTARGET: CRMFLAGS = 1
CRMFLAG_WRITTENDURINGPREPARE: CRMFLAGS = 2
CRMFLAG_WRITTENDURINGCOMMIT: CRMFLAGS = 4
CRMFLAG_WRITTENDURINGABORT: CRMFLAGS = 8
CRMFLAG_WRITTENDURINGRECOVERY: CRMFLAGS = 16
CRMFLAG_WRITTENDURINGREPLAY: CRMFLAGS = 32
CRMFLAG_REPLAYINPROGRESS: CRMFLAGS = 64
CRMREGFLAGS = Int32
CRMREGFLAG_PREPAREPHASE: CRMREGFLAGS = 1
CRMREGFLAG_COMMITPHASE: CRMREGFLAGS = 2
CRMREGFLAG_ABORTPHASE: CRMREGFLAGS = 4
CRMREGFLAG_ALLPHASES: CRMREGFLAGS = 7
CRMREGFLAG_FAILIFINDOUBTSREMAIN: CRMREGFLAGS = 16
CRMRecoveryClerk = Guid('{ecabb0be-7f19-11d2-978e-0000f8757e2a}')
CSC_Binding = Int32
CSC_NoBinding: CSC_Binding = 0
CSC_BindToPoolThread: CSC_Binding = 1
CSC_COMTIIntrinsicsConfig = Int32
CSC_NoCOMTIIntrinsics: CSC_COMTIIntrinsicsConfig = 0
CSC_InheritCOMTIIntrinsics: CSC_COMTIIntrinsicsConfig = 1
CSC_IISIntrinsicsConfig = Int32
CSC_NoIISIntrinsics: CSC_IISIntrinsicsConfig = 0
CSC_InheritIISIntrinsics: CSC_IISIntrinsicsConfig = 1
CSC_InheritanceConfig = Int32
CSC_Inherit: CSC_InheritanceConfig = 0
CSC_Ignore: CSC_InheritanceConfig = 1
CSC_PartitionConfig = Int32
CSC_NoPartition: CSC_PartitionConfig = 0
CSC_InheritPartition: CSC_PartitionConfig = 1
CSC_NewPartition: CSC_PartitionConfig = 2
CSC_SxsConfig = Int32
CSC_NoSxs: CSC_SxsConfig = 0
CSC_InheritSxs: CSC_SxsConfig = 1
CSC_NewSxs: CSC_SxsConfig = 2
CSC_SynchronizationConfig = Int32
CSC_NoSynchronization: CSC_SynchronizationConfig = 0
CSC_IfContainerIsSynchronized: CSC_SynchronizationConfig = 1
CSC_NewSynchronizationIfNecessary: CSC_SynchronizationConfig = 2
CSC_NewSynchronization: CSC_SynchronizationConfig = 3
CSC_ThreadPool = Int32
CSC_ThreadPoolNone: CSC_ThreadPool = 0
CSC_ThreadPoolInherit: CSC_ThreadPool = 1
CSC_STAThreadPool: CSC_ThreadPool = 2
CSC_MTAThreadPool: CSC_ThreadPool = 3
CSC_TrackerConfig = Int32
CSC_DontUseTracker: CSC_TrackerConfig = 0
CSC_UseTracker: CSC_TrackerConfig = 1
CSC_TransactionConfig = Int32
CSC_NoTransaction: CSC_TransactionConfig = 0
CSC_IfContainerIsTransactional: CSC_TransactionConfig = 1
CSC_CreateTransactionIfNecessary: CSC_TransactionConfig = 2
CSC_NewTransaction: CSC_TransactionConfig = 3
CServiceConfig = Guid('{ecabb0c8-7f19-11d2-978e-0000f8757e2a}')
ClrAssemblyLocator = Guid('{458aa3b5-265a-4b75-bc05-9bea4630cf18}')
CoMTSLocator = Guid('{ecabb0ac-7f19-11d2-978e-0000f8757e2a}')
ComServiceEvents = Guid('{ecabb0c3-7f19-11d2-978e-0000f8757e2a}')
ComSystemAppEventData = Guid('{ecabb0c6-7f19-11d2-978e-0000f8757e2a}')
class ComponentHangMonitorInfo(EasyCastStructure):
    IsMonitored: Windows.Win32.Foundation.BOOL
    TerminateOnHang: Windows.Win32.Foundation.BOOL
    AvgCallThresholdInMs: UInt32
class ComponentStatistics(EasyCastStructure):
    NumInstances: UInt32
    NumBoundReferences: UInt32
    NumPooledObjects: UInt32
    NumObjectsInCall: UInt32
    AvgResponseTimeInMs: UInt32
    NumCallsCompletedRecent: UInt32
    NumCallsFailedRecent: UInt32
    NumCallsCompletedTotal: UInt32
    NumCallsFailedTotal: UInt32
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: UInt32
    Reserved4: UInt32
class ComponentSummary(EasyCastStructure):
    ApplicationInstanceId: Guid
    PartitionId: Guid
    ApplicationId: Guid
    Clsid: Guid
    ClassName: Windows.Win32.Foundation.PWSTR
    ApplicationName: Windows.Win32.Foundation.PWSTR
class ContextInfo(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{19a5a02c-0ac8-11d2-b286-00c04f8ef934}')
    @commethod(7)
    def IsInTransaction(self, pbIsInTx: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransaction(self, ppTx: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransactionId(self, pbstrTxId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityId(self, pbstrActivityId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetContextId(self, pbstrCtxId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ContextInfo2(ComPtr):
    extends: Windows.Win32.System.ComponentServices.ContextInfo
    _iid_ = Guid('{c99d6e75-2375-11d4-8331-00c04f605588}')
    @commethod(12)
    def GetPartitionId(self, __MIDL__ContextInfo20000: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetApplicationId(self, __MIDL__ContextInfo20001: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetApplicationInstanceId(self, __MIDL__ContextInfo20002: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class CrmLogRecordRead(EasyCastStructure):
    dwCrmFlags: UInt32
    dwSequenceNumber: UInt32
    blobUserData: Windows.Win32.System.Com.BLOB
CrmTransactionState = Int32
TxState_Active: CrmTransactionState = 0
TxState_Committed: CrmTransactionState = 1
TxState_Aborted: CrmTransactionState = 2
TxState_Indoubt: CrmTransactionState = 3
DUMPTYPE = Int32
DUMPTYPE_FULL: DUMPTYPE = 0
DUMPTYPE_MINI: DUMPTYPE = 1
DUMPTYPE_NONE: DUMPTYPE = 2
DispenserManager = Guid('{ecabb0c0-7f19-11d2-978e-0000f8757e2a}')
Dummy30040732 = Guid('{ecabb0a9-7f19-11d2-978e-0000f8757e2a}')
EventServer = Guid('{ecabafbc-7f19-11d2-978e-0000f8757e2a}')
GetAppTrackerDataFlags = Int32
GATD_INCLUDE_PROCESS_EXE_NAME: GetAppTrackerDataFlags = 1
GATD_INCLUDE_LIBRARY_APPS: GetAppTrackerDataFlags = 2
GATD_INCLUDE_SWC: GetAppTrackerDataFlags = 4
GATD_INCLUDE_CLASS_NAME: GetAppTrackerDataFlags = 8
GATD_INCLUDE_APPLICATION_NAME: GetAppTrackerDataFlags = 16
GetSecurityCallContextAppObject = Guid('{ecabb0a8-7f19-11d2-978e-0000f8757e2a}')
class HANG_INFO(EasyCastStructure):
    fAppHangMonitorEnabled: Windows.Win32.Foundation.BOOL
    fTerminateOnHang: Windows.Win32.Foundation.BOOL
    DumpType: Windows.Win32.System.ComponentServices.DUMPTYPE
    dwHangTimeout: UInt32
    dwDumpCount: UInt32
    dwInfoMsgCount: UInt32
class IAppDomainHelper(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c7b67079-8255-42c6-9ec0-6994a3548780}')
    @commethod(7)
    def Initialize(self, pUnkAD: Windows.Win32.System.Com.IUnknown_head, __MIDL__IAppDomainHelper0000: IntPtr, pPool: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DoCallback(self, pUnkAD: Windows.Win32.System.Com.IUnknown_head, __MIDL__IAppDomainHelper0001: IntPtr, pPool: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IAssemblyLocator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{391ffbb9-a8ee-432a-abc8-baa238dab90f}')
    @commethod(7)
    def GetModules(self, applicationDir: Windows.Win32.Foundation.BSTR, applicationName: Windows.Win32.Foundation.BSTR, assemblyName: Windows.Win32.Foundation.BSTR, pModules: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IAsyncErrorNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fe6777fb-a674-4177-8f32-6d707e113484}')
    @commethod(3)
    def OnError(self, hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class ICOMAdminCatalog(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dd662187-dfc2-11d1-a2cf-00805fc79235}')
    @commethod(7)
    def GetCollection(self, bstrCollName: Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Connect(self, bstrCatalogServerName: Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCollectionByQuery(self, bstrCollName: Windows.Win32.Foundation.BSTR, ppsaVarQuery: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ImportComponent(self, bstrApplIDOrName: Windows.Win32.Foundation.BSTR, bstrCLSIDOrProgID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def InstallComponent(self, bstrApplIDOrName: Windows.Win32.Foundation.BSTR, bstrDLL: Windows.Win32.Foundation.BSTR, bstrTLB: Windows.Win32.Foundation.BSTR, bstrPSDLL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ShutdownApplication(self, bstrApplIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExportApplication(self, bstrApplIDOrName: Windows.Win32.Foundation.BSTR, bstrApplicationFile: Windows.Win32.Foundation.BSTR, lOptions: Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InstallApplication(self, bstrApplicationFile: Windows.Win32.Foundation.BSTR, bstrDestinationDirectory: Windows.Win32.Foundation.BSTR, lOptions: Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserId: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrRSN: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def StopRouter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RefreshRouter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def StartRouter(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Reserved1(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Reserved2(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def InstallMultipleComponents(self, bstrApplIDOrName: Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarCLSIDs: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMultipleComponentsInfo(self, bstrApplIdOrName: Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarCLSIDs: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarClassNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarFileFlags: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarComponentFlags: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RefreshComponents(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def BackupREGDB(self, bstrBackupFilePath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RestoreREGDB(self, bstrBackupFilePath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def QueryApplicationFile(self, bstrApplicationFile: Windows.Win32.Foundation.BSTR, pbstrApplicationName: POINTER(Windows.Win32.Foundation.BSTR), pbstrApplicationDescription: POINTER(Windows.Win32.Foundation.BSTR), pbHasUsers: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), pbIsProxy: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppsaVarFileNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def StartApplication(self, bstrApplIdOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ServiceCheck(self, lService: Int32, plStatus: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def InstallMultipleEventClasses(self, bstrApplIdOrName: Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarCLSIDS: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def InstallEventClass(self, bstrApplIdOrName: Windows.Win32.Foundation.BSTR, bstrDLL: Windows.Win32.Foundation.BSTR, bstrTLB: Windows.Win32.Foundation.BSTR, bstrPSDLL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetEventClassesForIID(self, bstrIID: Windows.Win32.Foundation.BSTR, ppsaVarCLSIDs: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarProgIDs: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppsaVarDescriptions: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ICOMAdminCatalog2(ComPtr):
    extends: Windows.Win32.System.ComponentServices.ICOMAdminCatalog
    _iid_ = Guid('{790c6e0b-9194-4cc9-9426-a48a63185696}')
    @commethod(33)
    def GetCollectionByQuery2(self, bstrCollectionName: Windows.Win32.Foundation.BSTR, pVarQueryStrings: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetApplicationInstanceIDFromProcessID(self, lProcessID: Int32, pbstrApplicationInstanceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ShutdownApplicationInstances(self, pVarApplicationInstanceID: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PauseApplicationInstances(self, pVarApplicationInstanceID: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def ResumeApplicationInstances(self, pVarApplicationInstanceID: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RecycleApplicationInstances(self, pVarApplicationInstanceID: POINTER(Windows.Win32.System.Variant.VARIANT_head), lReasonCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AreApplicationInstancesPaused(self, pVarApplicationInstanceID: POINTER(Windows.Win32.System.Variant.VARIANT_head), pVarBoolPaused: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DumpApplicationInstance(self, bstrApplicationInstanceID: Windows.Win32.Foundation.BSTR, bstrDirectory: Windows.Win32.Foundation.BSTR, lMaxImages: Int32, pbstrDumpFile: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsApplicationInstanceDumpSupported(self, pVarBoolDumpSupported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def CreateServiceForApplication(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, bstrServiceName: Windows.Win32.Foundation.BSTR, bstrStartType: Windows.Win32.Foundation.BSTR, bstrErrorControl: Windows.Win32.Foundation.BSTR, bstrDependencies: Windows.Win32.Foundation.BSTR, bstrRunAs: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bDesktopOk: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def DeleteServiceForApplication(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetPartitionID(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, pbstrPartitionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetPartitionName(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, pbstrPartitionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_CurrentPartition(self, bstrPartitionIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_CurrentPartitionID(self, pbstrPartitionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_CurrentPartitionName(self, pbstrPartitionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_GlobalPartitionID(self, pbstrGlobalPartitionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def FlushPartitionCache(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def CopyApplications(self, bstrSourcePartitionIDOrName: Windows.Win32.Foundation.BSTR, pVarApplicationID: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrDestinationPartitionIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def CopyComponents(self, bstrSourceApplicationIDOrName: Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrDestinationApplicationIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def MoveComponents(self, bstrSourceApplicationIDOrName: Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrDestinationApplicationIDOrName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def AliasComponent(self, bstrSrcApplicationIDOrName: Windows.Win32.Foundation.BSTR, bstrCLSIDOrProgID: Windows.Win32.Foundation.BSTR, bstrDestApplicationIDOrName: Windows.Win32.Foundation.BSTR, bstrNewProgId: Windows.Win32.Foundation.BSTR, bstrNewClsid: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def IsSafeToDelete(self, bstrDllName: Windows.Win32.Foundation.BSTR, pCOMAdminInUse: POINTER(Windows.Win32.System.ComponentServices.COMAdminInUse)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ImportUnconfiguredComponents(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(Windows.Win32.System.Variant.VARIANT_head), pVarComponentType: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def PromoteUnconfiguredComponents(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(Windows.Win32.System.Variant.VARIANT_head), pVarComponentType: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def ImportComponents(self, bstrApplicationIDOrName: Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(Windows.Win32.System.Variant.VARIANT_head), pVarComponentType: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_Is64BitCatalogServer(self, pbIs64Bit: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def ExportPartition(self, bstrPartitionIDOrName: Windows.Win32.Foundation.BSTR, bstrPartitionFileName: Windows.Win32.Foundation.BSTR, lOptions: Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def InstallPartition(self, bstrFileName: Windows.Win32.Foundation.BSTR, bstrDestDirectory: Windows.Win32.Foundation.BSTR, lOptions: Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserID: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, bstrRSN: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def QueryApplicationFile2(self, bstrApplicationFile: Windows.Win32.Foundation.BSTR, ppFilesForImport: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetComponentVersionCount(self, bstrCLSIDOrProgID: Windows.Win32.Foundation.BSTR, plVersionCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICOMLBArguments(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a0f150f-8ee5-4b94-b40e-aef2f9e42ed2}')
    @commethod(3)
    def GetCLSID(self, pCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCLSID(self, pCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMachineName(self, cchSvr: UInt32, szServerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMachineName(self, cchSvr: UInt32, szServerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICatalogCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22872-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def get__NewEnum(self, ppEnumVariant: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, ppCatalogObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plObjectCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, lIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, ppCatalogObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Populate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveChanges(self, pcChanges: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCollection(self, bstrCollName: Windows.Win32.Foundation.BSTR, varObjectKey: Windows.Win32.System.Variant.VARIANT, ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Name(self, pVarNamel: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AddEnabled(self, pVarBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoveEnabled(self, pVarBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetUtilInterface(self, ppIDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DataStoreMajorVersion(self, plMajorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DataStoreMinorVersion(self, plMinorVersionl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PopulateByKey(self, psaKeys: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def PopulateByQuery(self, bstrQueryString: Windows.Win32.Foundation.BSTR, lQueryType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ICatalogObject(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22871-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def get_Value(self, bstrPropName: Windows.Win32.Foundation.BSTR, pvarRetVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, bstrPropName: Windows.Win32.Foundation.BSTR, val: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Key(self, pvarRetVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Name(self, pvarRetVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsPropertyReadOnly(self, bstrPropName: Windows.Win32.Foundation.BSTR, pbRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Valid(self, pbRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsPropertyWriteOnly(self, bstrPropName: Windows.Win32.Foundation.BSTR, pbRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ICheckSxsConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ff5a96f-11fc-47d1-baa6-25dd347e7242}')
    @commethod(3)
    def IsSameSxsConfig(self, wszSxsName: Windows.Win32.Foundation.PWSTR, wszSxsDirectory: Windows.Win32.Foundation.PWSTR, wszSxsAppName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IComActivityEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b0-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnActivityCreate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnActivityDestroy(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnActivityEnter(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnActivityTimeout(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32, dwTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnActivityReenter(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), dwThread: UInt32, dwCallDepth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnActivityLeave(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidLeft: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnActivityLeaveSame(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), dwCallDepth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IComApp2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1290bc1a-b219-418d-b078-5934ded08242}')
    @commethod(3)
    def OnAppActivation2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, guidProcess: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnAppPaused2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, bPaused: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnAppRecycle2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, guidProcess: Guid, lReason: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IComAppEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a6-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnAppActivation(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IComCRMEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b5-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnCRMRecoveryStart(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCRMRecoveryDone(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCRMCheckpoint(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnCRMBegin(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, guidActivity: Guid, guidTx: Guid, szProgIdCompensator: Windows.Win32.Foundation.PWSTR, szDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnCRMPrepare(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnCRMCommit(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnCRMAbort(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnCRMIndoubt(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnCRMDone(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnCRMRelease(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnCRMAnalyze(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, dwCrmRecordType: UInt32, dwRecordSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnCRMWrite(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, fVariants: Windows.Win32.Foundation.BOOL, dwRecordSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnCRMForget(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnCRMForce(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnCRMDeliver(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, fVariants: Windows.Win32.Foundation.BOOL, dwRecordSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IComExceptionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b3-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnExceptionUser(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), code: UInt32, address: UInt64, pszStackTrace: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IComIdentityEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b1-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnIISRequestInfo(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjId: UInt64, pszClientIP: Windows.Win32.Foundation.PWSTR, pszServerIP: Windows.Win32.Foundation.PWSTR, pszURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IComInstance2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20e3bf07-b506-4ad5-a50c-d2ca5b9c158e}')
    @commethod(3)
    def OnObjectCreate2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64, guidPartition: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComInstanceEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a7-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectCreate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComLTxEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{605cf82c-578e-4298-975d-82babcd9e053}')
    @commethod(3)
    def OnLtxTransactionStart(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, tsid: Guid, fRoot: Windows.Win32.Foundation.BOOL, nIsolationLevel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnLtxTransactionPrepare(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, fVote: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLtxTransactionAbort(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnLtxTransactionCommit(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnLtxTransactionPromote(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, txnId: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IComMethod2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb388aaa-567d-4024-af8e-6e93ee748573}')
    @commethod(3)
    def OnMethodCall2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32, hresult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IComMethodEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a9-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnMethodCall(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32, hresult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IComMtaThreadPoolKnobs(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9a76d2e-76a5-43eb-a0c4-49bec8e48480}')
    @commethod(3)
    def MTASetMaxThreadCount(self, dwMaxThreads: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MTAGetMaxThreadCount(self, pdwMaxThreads: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MTASetThrottleValue(self, dwThrottle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def MTAGetThrottleValue(self, pdwThrottle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectConstruction2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b5a7827-8df2-45c0-8f6f-57ea1f856a9f}')
    @commethod(3)
    def OnObjectConstruct2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), sConstructString: Windows.Win32.Foundation.PWSTR, oid: UInt64, guidPartition: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectConstructionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130af-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectConstruct(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), sConstructString: Windows.Win32.Foundation.PWSTR, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130aa-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectActivate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64, ObjectID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDeactivate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64, ObjectID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDisableCommit(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnEnableCommit(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSetComplete(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnSetAbort(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectPool2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65bf6534-85ea-4f64-8cf4-3d974b2ab1cf}')
    @commethod(3)
    def OnObjPoolPutObject2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64, guidPartition: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64, guidPartition: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectPoolEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ad-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjPoolPutObject(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComObjectPoolEvents2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ae-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjPoolCreateObject(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolDestroyObject(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolCreateDecision(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), dwThreadsWaiting: UInt32, dwAvail: UInt32, dwCreated: UInt32, dwMin: UInt32, dwMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolTimeout(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), guidActivity: POINTER(Guid), dwTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnObjPoolCreatePool(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwMin: UInt32, dwMax: UInt32, dwTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IComQCEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b2-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnQCRecord(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), objid: UInt64, szQueue: Windows.Win32.Foundation.PWSTR, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), msmqhr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnQCQueueOpen(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), szQueue: Windows.Win32.Foundation.PWSTR, QueueID: UInt64, hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnQCReceive(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), QueueID: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnQCReceiveFail(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), QueueID: UInt64, msmqhr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnQCMoveToReTryQueue(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), RetryIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnQCMoveToDeadQueue(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnQCPlayback(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), objid: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IComResourceEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ab-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnResourceCreate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnResourceAllocate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: Windows.Win32.Foundation.BOOL, NumRated: UInt32, Rating: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnResourceRecycle(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: Windows.Win32.Foundation.PWSTR, resId: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnResourceDestroy(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, hr: Windows.Win32.Foundation.HRESULT, pszType: Windows.Win32.Foundation.PWSTR, resId: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnResourceTrack(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IComSecurityEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ac-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnAuthenticate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: POINTER(Byte), cbByteCur: UInt32, pSidCurrentUser: POINTER(Byte), bCurrentUserInpersonatingInProc: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAuthenticateFail(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: POINTER(Byte), cbByteCur: UInt32, pSidCurrentUser: POINTER(Byte), bCurrentUserInpersonatingInProc: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{324b64fa-33b6-11d2-98b7-00c04f8ee1c4}')
    @commethod(3)
    def SetMinThreadCount(self, minThreads: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinThreadCount(self, minThreads: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreadCount(self, maxThreads: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxThreadCount(self, maxThreads: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetActivityPerThread(self, activitiesPerThread: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetActivityPerThread(self, activitiesPerThread: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetActivityRatio(self, activityRatio: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityRatio(self, activityRatio: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetThreadCount(self, pdwThreads: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQueueDepth(self, pdwQDepth: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetQueueDepth(self, dwQDepth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs2(ComPtr):
    extends: Windows.Win32.System.ComponentServices.IComStaThreadPoolKnobs
    _iid_ = Guid('{73707523-ff9a-4974-bf84-2108dc213740}')
    @commethod(14)
    def GetMaxCPULoad(self, pdwLoad: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetMaxCPULoad(self, pdwLoad: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCPUMetricEnabled(self, pbMetricEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetCPUMetricEnabled(self, bMetricEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCreateThreadsAggressively(self, pbMetricEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetCreateThreadsAggressively(self, bMetricEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaxCSR(self, pdwCSR: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetMaxCSR(self, dwCSR: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetWaitTimeForThreadCleanup(self, pdwThreadCleanupWaitTime: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWaitTimeForThreadCleanup(self, dwThreadCleanupWaitTime: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IComThreadEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a5-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnThreadStart(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnThreadTerminate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadBindToApartment(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32, dwLowCnt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnThreadUnBind(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnThreadWorkEnque(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnThreadWorkPrivate(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnThreadWorkPublic(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnThreadWorkRedirect(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32, ThreadNum: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnThreadWorkReject(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnThreadAssignApartment(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), AptID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnThreadUnassignApartment(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), AptID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c266c677-c9ad-49ab-9fd9-d9661078588a}')
    @commethod(3)
    def Type(self, pType: POINTER(Windows.Win32.System.ComponentServices.TRACKING_COLL_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Count(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, ulIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e6cdcc9-fb25-4fd5-9cc5-c9f4b6559cec}')
    @commethod(3)
    def OnNewTrackingInfo(self, pToplevelCollection: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{116e42c5-d8b1-47bf-ab1e-c895ed3e2372}')
    @commethod(3)
    def GetValue(self, szPropertyName: Windows.Win32.Foundation.PWSTR, pvarOut: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{789b42be-6f6b-443a-898e-67abf390aa14}')
    @commethod(3)
    def PropCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropName(self, ulIndex: UInt32, ppszPropName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IComTransaction2Events(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a136f62a-2f94-4288-86e0-d8a1fa4c0299}')
    @commethod(3)
    def OnTransactionStart2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: Windows.Win32.Foundation.BOOL, nIsolationLevel: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), fVoteYes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit2(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IComTransactionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a8-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnTransactionStart(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), fVoteYes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IComUserEvent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a4-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnUserEvent(self, pInfo: POINTER(Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO_head), pvarEvent: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d396da85-bf8f-11d1-bbae-00c04fc2fa5f}')
    @commethod(3)
    def Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, name: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(self, ppenum: POINTER(Windows.Win32.System.ComponentServices.IEnumNames_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(self, name: Windows.Win32.Foundation.BSTR, property: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProperty(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IContextSecurityPerimeter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7549a29-a7c4-42e1-8dc1-7e3d748dc24a}')
    @commethod(3)
    def GetPerimeterFlag(self, pFlag: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPerimeterFlag(self, fFlag: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IContextState(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c05e54b-a42a-11d2-afc4-00c04f8ee1c4}')
    @commethod(3)
    def SetDeactivateOnReturn(self, bDeactivate: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeactivateOnReturn(self, pbDeactivate: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMyTransactionVote(self, txVote: Windows.Win32.System.ComponentServices.TransactionVote) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMyTransactionVote(self, ptxVote: POINTER(Windows.Win32.System.ComponentServices.TransactionVote)) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateWithLocalTransaction(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{227ac7a8-8423-42ce-b7cf-03061ec9aaa3}')
    @commethod(3)
    def CreateInstanceWithSysTx(self, pTransaction: Windows.Win32.System.Com.IUnknown_head, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateWithTipTransactionEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{455acf59-5345-11d2-99cf-00c04f797bc9}')
    @commethod(3)
    def CreateInstance(self, bstrTipUrl: Windows.Win32.Foundation.BSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateWithTransactionEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{455acf57-5345-11d2-99cf-00c04f797bc9}')
    @commethod(3)
    def CreateInstance(self, pTransaction: Windows.Win32.System.DistributedTransactionCoordinator.ITransaction_head, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmCompensator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bbc01830-8d3b-11d1-82ec-00a0c91eede9}')
    @commethod(3)
    def SetLogControl(self, pLogControl: Windows.Win32.System.ComponentServices.ICrmLogControl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepare(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecord(self, crmLogRec: Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepare(self, pfOkToPrepare: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommit(self, fRecovery: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecord(self, crmLogRec: Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbort(self, fRecovery: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecord(self, crmLogRec: Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbort(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmCompensatorVariants(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0baf8e4-7804-11d1-82e9-00a0c91eede9}')
    @commethod(3)
    def SetLogControlVariants(self, pLogControl: Windows.Win32.System.ComponentServices.ICrmLogControl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepareVariants(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecordVariants(self, pLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head), pbForget: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepareVariants(self, pbOkToPrepare: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommitVariants(self, bRecovery: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecordVariants(self, pLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head), pbForget: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommitVariants(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbortVariants(self, bRecovery: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecordVariants(self, pLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head), pbForget: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbortVariants(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmFormatLogRecords(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c51d821-c98b-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def GetColumnCount(self, plColumnCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaders(self, pHeaders: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColumn(self, CrmLogRec: Windows.Win32.System.ComponentServices.CrmLogRecordRead, pFormattedLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnVariants(self, LogRecord: Windows.Win32.System.Variant.VARIANT, pFormattedLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmLogControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0e174b3-d26e-11d2-8f84-00805fc7bcd9}')
    @commethod(3)
    def get_TransactionUOW(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCompensator(self, lpcwstrProgIdCompensator: Windows.Win32.Foundation.PWSTR, lpcwstrDescription: Windows.Win32.Foundation.PWSTR, lCrmRegFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteLogRecordVariants(self, pLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ForceLog(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ForgetLogRecord(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ForceTransactionToAbort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteLogRecord(self, rgBlob: POINTER(Windows.Win32.System.Com.BLOB_head), cBlob: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70c8e443-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def GetClerks(self, pClerks: POINTER(Windows.Win32.System.ComponentServices.ICrmMonitorClerks_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HoldClerk(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitorClerks(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{70c8e442-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(7)
    def Item(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProgIdCompensator(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Description(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TransactionUOW(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ActivityId(self, Index: Windows.Win32.System.Variant.VARIANT, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitorLogRecords(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70c8e441-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TransactionState(self, pVal: POINTER(Windows.Win32.System.ComponentServices.CrmTransactionState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_StructuredRecords(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLogRecord(self, dwIndex: UInt32, pCrmLogRec: POINTER(Windows.Win32.System.ComponentServices.CrmLogRecordRead_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLogRecordVariants(self, IndexNumber: Windows.Win32.System.Variant.VARIANT, pLogRecord: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispenserDriver(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{208b3651-2b48-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def CreateResource(self, ResTypId: UIntPtr, pResId: POINTER(UIntPtr), pSecsFreeBeforeDestroy: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RateResource(self, ResTypId: UIntPtr, ResId: UIntPtr, fRequiresTransactionEnlistment: Windows.Win32.Foundation.BOOL, pRating: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistResource(self, ResId: UIntPtr, TransId: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ResetResource(self, ResId: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyResource(self, ResId: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DestroyResourceS(self, ResId: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispenserManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cb31e10-2b5f-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def RegisterDispenser(self, __MIDL__IDispenserManager0000: Windows.Win32.System.ComponentServices.IDispenserDriver_head, szDispenserName: Windows.Win32.Foundation.PWSTR, __MIDL__IDispenserManager0001: POINTER(Windows.Win32.System.ComponentServices.IHolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContext(self, __MIDL__IDispenserManager0002: POINTER(UIntPtr), __MIDL__IDispenserManager0003: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNames(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af2-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Next(self, celt: UInt32, rgname: POINTER(Windows.Win32.Foundation.BSTR), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.ComponentServices.IEnumNames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventServerTrace(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9a9f12b8-80af-47ab-a579-35ea57725370}')
    @commethod(7)
    def StartTraceGuid(self, bstrguidEvent: Windows.Win32.Foundation.BSTR, bstrguidFilter: Windows.Win32.Foundation.BSTR, lPidFilter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopTraceGuid(self, bstrguidEvent: Windows.Win32.Foundation.BSTR, bstrguidFilter: Windows.Win32.Foundation.BSTR, lPidFilter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTraceGuid(self, plCntGuids: POINTER(Int32), pbstrGuidList: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetAppTrackerData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{507c3ac8-3e12-4cb0-9366-653d3e050638}')
    @commethod(3)
    def GetApplicationProcesses(self, PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumApplicationProcesses: POINTER(UInt32), ApplicationProcesses: POINTER(POINTER(Windows.Win32.System.ComponentServices.ApplicationProcessSummary_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplicationProcessDetails(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Flags: UInt32, Summary: POINTER(Windows.Win32.System.ComponentServices.ApplicationProcessSummary_head), Statistics: POINTER(Windows.Win32.System.ComponentServices.ApplicationProcessStatistics_head), RecycleInfo: POINTER(Windows.Win32.System.ComponentServices.ApplicationProcessRecycleInfo_head), AnyComponentsHangMonitored: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplicationsInProcess(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), Flags: UInt32, NumApplicationsInProcess: POINTER(UInt32), Applications: POINTER(POINTER(Windows.Win32.System.ComponentServices.ApplicationSummary_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentsInProcess(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumComponentsInProcess: POINTER(UInt32), Components: POINTER(POINTER(Windows.Win32.System.ComponentServices.ComponentSummary_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentDetails(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Clsid: POINTER(Guid), Flags: UInt32, Summary: POINTER(Windows.Win32.System.ComponentServices.ComponentSummary_head), Statistics: POINTER(Windows.Win32.System.ComponentServices.ComponentStatistics_head), HangMonitorInfo: POINTER(Windows.Win32.System.ComponentServices.ComponentHangMonitorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTrackerDataAsCollectionObject(self, TopLevelCollection: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSuggestedPollingInterval(self, PollingIntervalInSeconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetContextProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af4-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, name: Windows.Win32.Foundation.BSTR, pProperty: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(self, ppenum: POINTER(Windows.Win32.System.ComponentServices.IEnumNames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetSecurityCallContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823f-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def GetSecurityCallContext(self, ppObject: POINTER(Windows.Win32.System.ComponentServices.ISecurityCallContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IHolder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf6a1850-2b45-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def AllocResource(self, __MIDL__IHolder0000: UIntPtr, __MIDL__IHolder0001: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeResource(self, __MIDL__IHolder0002: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TrackResource(self, __MIDL__IHolder0003: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TrackResourceS(self, __MIDL__IHolder0004: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UntrackResource(self, __MIDL__IHolder0005: UIntPtr, __MIDL__IHolder0006: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UntrackResourceS(self, __MIDL__IHolder0007: POINTER(UInt16), __MIDL__IHolder0008: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestDestroyResource(self, __MIDL__IHolder0009: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ILBEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b4-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def TargetUp(self, bstrServerName: Windows.Win32.Foundation.BSTR, bstrClsidEng: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TargetDown(self, bstrServerName: Windows.Win32.Foundation.BSTR, bstrClsidEng: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EngineDefined(self, bstrPropName: Windows.Win32.Foundation.BSTR, varPropValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrClsidEng: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMTSActivity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af0-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def SynchronousCall(self, pCall: Windows.Win32.System.ComponentServices.IMTSCall_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AsyncCall(self, pCall: Windows.Win32.System.ComponentServices.IMTSCall_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reserved1(self) -> Void: ...
    @commethod(6)
    def BindToCurrentThread(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnbindFromThread(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMTSCall(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aef-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def OnCall(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMTSLocator(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d19b8bfd-7f88-11d0-b16e-00aa00ba3258}')
    @commethod(7)
    def GetEventDispatcher(self, pUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IManagedActivationEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5f325af-572f-46da-b8ab-827c3d95d99e}')
    @commethod(3)
    def CreateManagedStub(self, pInfo: Windows.Win32.System.ComponentServices.IManagedObjectInfo_head, fDist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DestroyManagedStub(self, pInfo: Windows.Win32.System.ComponentServices.IManagedObjectInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IManagedObjectInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1427c51a-4584-49d8-90a0-c50d8086cbe9}')
    @commethod(3)
    def GetIUnknown(self, pUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIObjectControl(self, pCtrl: POINTER(Windows.Win32.System.ComponentServices.IObjectControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetInPool(self, bInPool: Windows.Win32.Foundation.BOOL, pPooledObj: Windows.Win32.System.ComponentServices.IManagedPooledObj_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetWrapperStrength(self, bStrong: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IManagedPoolAction(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da91b74e-5388-4783-949d-c1cd5fb00506}')
    @commethod(3)
    def LastRelease(self) -> Windows.Win32.Foundation.HRESULT: ...
class IManagedPooledObj(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5da4bea-1b42-4437-8926-b6a38860a770}')
    @commethod(3)
    def SetHeld(self, m_bHeld: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMessageMover(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{588a085a-b795-11d1-8054-00c04fc340ee}')
    @commethod(7)
    def get_SourcePath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SourcePath(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DestPath(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DestPath(self, newVal: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CommitBatchSize(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CommitBatchSize(self, newVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def MoveMessages(self, plMessagesMoved: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMtsEventInfo(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d56c3dc1-8482-11d0-b170-00aa00ba3258}')
    @commethod(7)
    def get_Names(self, pUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(self, sDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventID(self, sGuidEventID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(self, lCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Value(self, sKey: Windows.Win32.Foundation.BSTR, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMtsEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bacedf4d-74ab-11d0-b162-00aa00ba3258}')
    @commethod(7)
    def get_PackageName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PackageGuid(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PostEvent(self, vEvent: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FireEvents(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProcessID(self, id: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMtsGrp(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4b2e958c-0393-11d1-b1ab-00aa00ba3258}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, lIndex: Int32, ppUnkDispatcher: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
class IObjPool(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d8805a0-2ea7-11d1-b1cc-00aa00ba3258}')
    @commethod(3)
    def Reserved1(self) -> Void: ...
    @commethod(4)
    def Reserved2(self) -> Void: ...
    @commethod(5)
    def Reserved3(self) -> Void: ...
    @commethod(6)
    def Reserved4(self) -> Void: ...
    @commethod(7)
    def PutEndTx(self, pObj: Windows.Win32.System.Com.IUnknown_head) -> Void: ...
    @commethod(8)
    def Reserved5(self) -> Void: ...
    @commethod(9)
    def Reserved6(self) -> Void: ...
class IObjectConstruct(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41c4f8b3-7439-11d2-98cb-00c04f8ee1c4}')
    @commethod(3)
    def Construct(self, pCtorObj: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectConstructString(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{41c4f8b2-7439-11d2-98cb-00c04f8ee1c4}')
    @commethod(7)
    def get_ConstructString(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372ae0-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def CreateInstance(self, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAbort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableCommit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DisableCommit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsInTransaction(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def IsSecurityEnabled(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(10)
    def IsCallerInRole(self, bstrRole: Windows.Win32.Foundation.BSTR, pfIsInRole: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectContextActivity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372afc-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetActivityId(self, pGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectContextInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75b52ddb-e8ed-11d1-93ad-00aa00ba3258}')
    @commethod(3)
    def IsInTransaction(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def GetTransaction(self, pptrans: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransactionId(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetActivityId(self, pGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetContextId(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectContextInfo2(ComPtr):
    extends: Windows.Win32.System.ComponentServices.IObjectContextInfo
    _iid_ = Guid('{594be71a-4bc4-438b-9197-cfd176248b09}')
    @commethod(8)
    def GetPartitionId(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetApplicationId(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetApplicationInstanceId(self, pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectContextTip(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92fd41ca-bad9-11d2-9a2d-00c04f797bc9}')
    @commethod(3)
    def GetTipUrl(self, pTipUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aec-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Activate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> Void: ...
    @commethod(5)
    def CanBePooled(self) -> Windows.Win32.Foundation.BOOL: ...
class IPlaybackControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372afd-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def FinalClientRetry(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FinalServerRetry(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPoolManager(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0a469861-5a91-43a0-99b6-d5e179bb0631}')
    @commethod(7)
    def ShutdownPool(self, CLSIDOrProgID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IProcessInitializer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1113f52d-dc7f-4943-aed6-88d04027e32a}')
    @commethod(3)
    def Startup(self, punkProcessControl: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityCallContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823e-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, name: Windows.Win32.Foundation.BSTR, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsCallerInRole(self, bstrRole: Windows.Win32.Foundation.BSTR, pfInRole: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsSecurityEnabled(self, pfIsEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsUserInRole(self, pUser: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrRole: Windows.Win32.Foundation.BSTR, pfInRole: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityCallersColl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823d-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pObj: POINTER(Windows.Win32.System.ComponentServices.ISecurityIdentityColl_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityIdentityColl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823c-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, name: Windows.Win32.Foundation.BSTR, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISecurityProperty(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aea-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetDirectCreatorSID(self, pSID: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginalCreatorSID(self, pSID: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDirectCallerSID(self, pSID: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOriginalCallerSID(self, pSID: POINTER(Windows.Win32.Foundation.PSID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseSID(self, pSID: Windows.Win32.Foundation.PSID) -> Windows.Win32.Foundation.HRESULT: ...
class ISelectCOMLBServer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcf443f4-3f8a-4872-b9f0-369a796d12d6}')
    @commethod(3)
    def Init(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLBServer(self, pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISendMethodEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2732fd59-b2b4-4d44-878c-8b8f09626008}')
    @commethod(3)
    def SendMethodCall(self, pIdentity: VoidPtr, riid: POINTER(Guid), dwMeth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendMethodReturn(self, pIdentity: VoidPtr, riid: POINTER(Guid), dwMeth: UInt32, hrCall: Windows.Win32.Foundation.HRESULT, hrServer: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceActivity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{67532e0c-9e2f-4450-a354-035633944e17}')
    @commethod(3)
    def SynchronousCall(self, pIServiceCall: Windows.Win32.System.ComponentServices.IServiceCall_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AsynchronousCall(self, pIServiceCall: Windows.Win32.System.ComponentServices.IServiceCall_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BindToCurrentThread(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnbindFromThread(self) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceCall(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bd3e2e12-42dd-40f4-a09a-95a50c58304b}')
    @commethod(3)
    def OnCall(self) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceComTIIntrinsicsConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09e6831e-04e1-4ed4-9d0f-e8b168bafeaf}')
    @commethod(3)
    def ComTIIntrinsicsConfig(self, comtiIntrinsicsConfig: Windows.Win32.System.ComponentServices.CSC_COMTIIntrinsicsConfig) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceIISIntrinsicsConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a0cf920-d452-46f4-bc36-48118d54ea52}')
    @commethod(3)
    def IISIntrinsicsConfig(self, iisIntrinsicsConfig: Windows.Win32.System.ComponentServices.CSC_IISIntrinsicsConfig) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceInheritanceConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92186771-d3b4-4d77-a8ea-ee842d586f35}')
    @commethod(3)
    def ContainingContextTreatment(self, inheritanceConfig: Windows.Win32.System.ComponentServices.CSC_InheritanceConfig) -> Windows.Win32.Foundation.HRESULT: ...
class IServicePartitionConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80182d03-5ea4-4831-ae97-55beffc2e590}')
    @commethod(3)
    def PartitionConfig(self, partitionConfig: Windows.Win32.System.ComponentServices.CSC_PartitionConfig) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PartitionID(self, guidPartitionID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IServicePool(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b302df81-ea45-451e-99a2-09f9fd1b1e13}')
    @commethod(3)
    def Initialize(self, pPoolConfig: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IServicePoolConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9690656-5bca-470c-8451-250c1f43a33e}')
    @commethod(3)
    def put_MaxPoolSize(self, dwMaxPool: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_MaxPoolSize(self, pdwMaxPool: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_MinPoolSize(self, dwMinPool: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_MinPoolSize(self, pdwMinPool: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_CreationTimeout(self, dwCreationTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CreationTimeout(self, pdwCreationTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_TransactionAffinity(self, fTxAffinity: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TransactionAffinity(self, pfTxAffinity: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ClassFactory(self, pFactory: Windows.Win32.System.Com.IClassFactory_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClassFactory(self, pFactory: POINTER(Windows.Win32.System.Com.IClassFactory_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceSxsConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7cd7379-f3f2-4634-811b-703281d73e08}')
    @commethod(3)
    def SxsConfig(self, scsConfig: Windows.Win32.System.ComponentServices.CSC_SxsConfig) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SxsName(self, szSxsName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SxsDirectory(self, szSxsDirectory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceSynchronizationConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd880e81-6dce-4c58-af83-a208846c0030}')
    @commethod(3)
    def ConfigureSynchronization(self, synchConfig: Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceSysTxnConfig(ComPtr):
    extends: Windows.Win32.System.ComponentServices.IServiceTransactionConfig
    _iid_ = Guid('{33caf1a1-fcb8-472b-b45e-967448ded6d8}')
    @commethod(9)
    def ConfigureBYOTSysTxn(self, pTxProxy: Windows.Win32.System.ComponentServices.ITransactionProxy_head) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceThreadPoolConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{186d89bc-f277-4bcc-80d5-4df7b836ef4a}')
    @commethod(3)
    def SelectThreadPool(self, threadPool: Windows.Win32.System.ComponentServices.CSC_ThreadPool) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBindingInfo(self, binding: Windows.Win32.System.ComponentServices.CSC_Binding) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceTrackerConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c3a3e1d-0ba6-4036-b76f-d0404db816c9}')
    @commethod(3)
    def TrackerConfig(self, trackerConfig: Windows.Win32.System.ComponentServices.CSC_TrackerConfig, szTrackerAppName: Windows.Win32.Foundation.PWSTR, szTrackerCtxName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceTransactionConfig(ComPtr):
    extends: Windows.Win32.System.ComponentServices.IServiceTransactionConfigBase
    _iid_ = Guid('{59f4c2a3-d3d7-4a31-b6e4-6ab3177c50b9}')
    @commethod(8)
    def ConfigureBYOT(self, pITxByot: Windows.Win32.System.DistributedTransactionCoordinator.ITransaction_head) -> Windows.Win32.Foundation.HRESULT: ...
class IServiceTransactionConfigBase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{772b3fbe-6ffd-42fb-b5f8-8f9b260f3810}')
    @commethod(3)
    def ConfigureTransaction(self, transactionConfig: Windows.Win32.System.ComponentServices.CSC_TransactionConfig) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsolationLevel(self, option: Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransactionTimeout(self, ulTimeoutSec: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BringYourOwnTransaction(self, szTipURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NewTransactionDescription(self, szTxDesc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISharedProperty(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c01-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def get_Value(self, pVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, val: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class ISharedPropertyGroup(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c07-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def CreatePropertyByPosition(self, Index: Int32, fExists: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppProp: POINTER(Windows.Win32.System.ComponentServices.ISharedProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PropertyByPosition(self, Index: Int32, ppProperty: POINTER(Windows.Win32.System.ComponentServices.ISharedProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateProperty(self, Name: Windows.Win32.Foundation.BSTR, fExists: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppProp: POINTER(Windows.Win32.System.ComponentServices.ISharedProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Property(self, Name: Windows.Win32.Foundation.BSTR, ppProperty: POINTER(Windows.Win32.System.ComponentServices.ISharedProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISharedPropertyGroupManager(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c0d-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def CreatePropertyGroup(self, Name: Windows.Win32.Foundation.BSTR, dwIsoMode: POINTER(Int32), dwRelMode: POINTER(Int32), fExists: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppGroup: POINTER(Windows.Win32.System.ComponentServices.ISharedPropertyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Group(self, Name: Windows.Win32.Foundation.BSTR, ppGroup: POINTER(Windows.Win32.System.ComponentServices.ISharedPropertyGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISystemAppEventData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6d48a3c-d5c5-49e7-8c74-99e4889ed52f}')
    @commethod(3)
    def Startup(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataChanged(self, dwPID: UInt32, dwMask: UInt32, dwNumberSinks: UInt32, bstrDwMethodMask: Windows.Win32.Foundation.BSTR, dwReason: UInt32, u64TraceHandle: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IThreadPoolKnobs(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af7-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetMaxThreads(self, plcMaxThreads: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentThreads(self, plcCurrentThreads: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreads(self, lcMaxThreads: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDeleteDelay(self, pmsecDeleteDelay: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDeleteDelay(self, msecDeleteDelay: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxQueuedRequests(self, plcMaxQueuedRequests: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentQueuedRequests(self, plcCurrentQueuedRequests: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMaxQueuedRequests(self, lcMaxQueuedRequests: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMinThreads(self, lcMinThreads: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetQueueDepth(self, lcQueueDepth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ITransactionContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7999fc21-d3c6-11cf-acab-00a024a55aef}')
    @commethod(7)
    def CreateInstance(self, pszProgId: Windows.Win32.Foundation.BSTR, pObject: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
class ITransactionContextEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7999fc22-d3c6-11cf-acab-00a024a55aef}')
    @commethod(3)
    def CreateInstance(self, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
class ITransactionProperty(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{788ea814-87b1-11d1-bba6-00c04fc2fa5f}')
    @commethod(3)
    def Reserved1(self) -> Void: ...
    @commethod(4)
    def Reserved2(self) -> Void: ...
    @commethod(5)
    def Reserved3(self) -> Void: ...
    @commethod(6)
    def Reserved4(self) -> Void: ...
    @commethod(7)
    def Reserved5(self) -> Void: ...
    @commethod(8)
    def Reserved6(self) -> Void: ...
    @commethod(9)
    def Reserved7(self) -> Void: ...
    @commethod(10)
    def Reserved8(self) -> Void: ...
    @commethod(11)
    def Reserved9(self) -> Void: ...
    @commethod(12)
    def GetTransactionResourcePool(self, ppTxPool: POINTER(Windows.Win32.System.ComponentServices.ITransactionResourcePool_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Reserved10(self) -> Void: ...
    @commethod(14)
    def Reserved11(self) -> Void: ...
    @commethod(15)
    def Reserved12(self) -> Void: ...
    @commethod(16)
    def Reserved13(self) -> Void: ...
    @commethod(17)
    def Reserved14(self) -> Void: ...
    @commethod(18)
    def Reserved15(self) -> Void: ...
    @commethod(19)
    def Reserved16(self) -> Void: ...
    @commethod(20)
    def Reserved17(self) -> Void: ...
class ITransactionProxy(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02558374-df2e-4dae-bd6b-1d5c994f9bdc}')
    @commethod(3)
    def Commit(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Promote(self, pTransaction: POINTER(Windows.Win32.System.DistributedTransactionCoordinator.ITransaction_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateVoter(self, pTxAsync: Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head, ppBallot: POINTER(Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIsolationLevel(self, __MIDL__ITransactionProxy0000: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIdentifier(self, pbstrIdentifier: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsReusable(self, pfIsReusable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransactionResourcePool(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5feb7c1-346a-11d1-b1cc-00aa00ba3258}')
    @commethod(3)
    def PutResource(self, pPool: Windows.Win32.System.ComponentServices.IObjPool_head, pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(self, pPool: Windows.Win32.System.ComponentServices.IObjPool_head, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransactionStatus(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61f589e8-3724-4898-a0a4-664ae9e1d1b4}')
    @commethod(3)
    def SetTransactionStatus(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionStatus(self, pHrStatus: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class ITxProxyHolder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13d86f31-0139-41af-bcad-c7d50435fe9f}')
    @commethod(3)
    def GetIdentifier(self, pGuidLtx: POINTER(Guid)) -> Void: ...
LBEvents = Guid('{ecabb0c1-7f19-11d2-978e-0000f8757e2a}')
LockModes = Int32
LockModes_LockSetGet: LockModes = 0
LockModes_LockMethod: LockModes = 1
MessageMover = Guid('{ecabb0bf-7f19-11d2-978e-0000f8757e2a}')
MtsGrp = Guid('{4b2e958d-0393-11d1-b1ab-00aa00ba3258}')
class ObjectContext(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{74c08646-cedb-11cf-8b49-00aa00b8a790}')
    @commethod(7)
    def CreateInstance(self, bstrProgID: Windows.Win32.Foundation.BSTR, pObject: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAbort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableCommit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisableCommit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsInTransaction(self, pbIsInTx: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsSecurityEnabled(self, pbIsEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsCallerInRole(self, bstrRole: Windows.Win32.Foundation.BSTR, pbInRole: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Count(self, plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Item(self, name: Windows.Win32.Foundation.BSTR, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get__NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Security(self, ppSecurityProperty: POINTER(Windows.Win32.System.ComponentServices.SecurityProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ContextInfo(self, ppContextInfo: POINTER(Windows.Win32.System.ComponentServices.ContextInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ObjectControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7dc41850-0c31-11d0-8b79-00aa00b8a790}')
    @commethod(3)
    def Activate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CanBePooled(self, pbPoolable: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
PoolMgr = Guid('{ecabafb5-7f19-11d2-978e-0000f8757e2a}')
class RECYCLE_INFO(EasyCastStructure):
    guidCombaseProcessIdentifier: Guid
    ProcessStartTime: Int64
    dwRecycleLifetimeLimit: UInt32
    dwRecycleMemoryLimit: UInt32
    dwRecycleExpirationTimeout: UInt32
ReleaseModes = Int32
ReleaseModes_Standard: ReleaseModes = 0
ReleaseModes_Process: ReleaseModes = 1
SecurityCallContext = Guid('{ecabb0a7-7f19-11d2-978e-0000f8757e2a}')
SecurityCallers = Guid('{ecabb0a6-7f19-11d2-978e-0000f8757e2a}')
SecurityIdentity = Guid('{ecabb0a5-7f19-11d2-978e-0000f8757e2a}')
class SecurityProperty(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e74a7215-014d-11d1-a63c-00a0c911b4e0}')
    @commethod(7)
    def GetDirectCallerName(self, bstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDirectCreatorName(self, bstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOriginalCallerName(self, bstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOriginalCreatorName(self, bstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
ServicePool = Guid('{ecabb0c9-7f19-11d2-978e-0000f8757e2a}')
ServicePoolConfig = Guid('{ecabb0ca-7f19-11d2-978e-0000f8757e2a}')
SharedProperty = Guid('{2a005c05-a5de-11cf-9e66-00aa00a3f464}')
SharedPropertyGroup = Guid('{2a005c0b-a5de-11cf-9e66-00aa00a3f464}')
SharedPropertyGroupManager = Guid('{2a005c11-a5de-11cf-9e66-00aa00a3f464}')
TRACKING_COLL_TYPE = Int32
TRKCOLL_PROCESSES: TRACKING_COLL_TYPE = 0
TRKCOLL_APPLICATIONS: TRACKING_COLL_TYPE = 1
TRKCOLL_COMPONENTS: TRACKING_COLL_TYPE = 2
TrackerServer = Guid('{ecabafb9-7f19-11d2-978e-0000f8757e2a}')
TransactionContext = Guid('{7999fc25-d3c6-11cf-acab-00a024a55aef}')
TransactionContextEx = Guid('{5cb66670-d3d4-11cf-acab-00a024a55aef}')
TransactionVote = Int32
TransactionVote_TxCommit: TransactionVote = 0
TransactionVote_TxAbort: TransactionVote = 1
make_head(_module, 'APPDATA')
make_head(_module, 'APPSTATISTICS')
make_head(_module, 'ApplicationProcessRecycleInfo')
make_head(_module, 'ApplicationProcessStatistics')
make_head(_module, 'ApplicationProcessSummary')
make_head(_module, 'ApplicationSummary')
make_head(_module, 'CLSIDDATA')
make_head(_module, 'CLSIDDATA2')
make_head(_module, 'COMSVCSEVENTINFO')
make_head(_module, 'ComponentHangMonitorInfo')
make_head(_module, 'ComponentStatistics')
make_head(_module, 'ComponentSummary')
make_head(_module, 'ContextInfo')
make_head(_module, 'ContextInfo2')
make_head(_module, 'CrmLogRecordRead')
make_head(_module, 'HANG_INFO')
make_head(_module, 'IAppDomainHelper')
make_head(_module, 'IAssemblyLocator')
make_head(_module, 'IAsyncErrorNotify')
make_head(_module, 'ICOMAdminCatalog')
make_head(_module, 'ICOMAdminCatalog2')
make_head(_module, 'ICOMLBArguments')
make_head(_module, 'ICatalogCollection')
make_head(_module, 'ICatalogObject')
make_head(_module, 'ICheckSxsConfig')
make_head(_module, 'IComActivityEvents')
make_head(_module, 'IComApp2Events')
make_head(_module, 'IComAppEvents')
make_head(_module, 'IComCRMEvents')
make_head(_module, 'IComExceptionEvents')
make_head(_module, 'IComIdentityEvents')
make_head(_module, 'IComInstance2Events')
make_head(_module, 'IComInstanceEvents')
make_head(_module, 'IComLTxEvents')
make_head(_module, 'IComMethod2Events')
make_head(_module, 'IComMethodEvents')
make_head(_module, 'IComMtaThreadPoolKnobs')
make_head(_module, 'IComObjectConstruction2Events')
make_head(_module, 'IComObjectConstructionEvents')
make_head(_module, 'IComObjectEvents')
make_head(_module, 'IComObjectPool2Events')
make_head(_module, 'IComObjectPoolEvents')
make_head(_module, 'IComObjectPoolEvents2')
make_head(_module, 'IComQCEvents')
make_head(_module, 'IComResourceEvents')
make_head(_module, 'IComSecurityEvents')
make_head(_module, 'IComStaThreadPoolKnobs')
make_head(_module, 'IComStaThreadPoolKnobs2')
make_head(_module, 'IComThreadEvents')
make_head(_module, 'IComTrackingInfoCollection')
make_head(_module, 'IComTrackingInfoEvents')
make_head(_module, 'IComTrackingInfoObject')
make_head(_module, 'IComTrackingInfoProperties')
make_head(_module, 'IComTransaction2Events')
make_head(_module, 'IComTransactionEvents')
make_head(_module, 'IComUserEvent')
make_head(_module, 'IContextProperties')
make_head(_module, 'IContextSecurityPerimeter')
make_head(_module, 'IContextState')
make_head(_module, 'ICreateWithLocalTransaction')
make_head(_module, 'ICreateWithTipTransactionEx')
make_head(_module, 'ICreateWithTransactionEx')
make_head(_module, 'ICrmCompensator')
make_head(_module, 'ICrmCompensatorVariants')
make_head(_module, 'ICrmFormatLogRecords')
make_head(_module, 'ICrmLogControl')
make_head(_module, 'ICrmMonitor')
make_head(_module, 'ICrmMonitorClerks')
make_head(_module, 'ICrmMonitorLogRecords')
make_head(_module, 'IDispenserDriver')
make_head(_module, 'IDispenserManager')
make_head(_module, 'IEnumNames')
make_head(_module, 'IEventServerTrace')
make_head(_module, 'IGetAppTrackerData')
make_head(_module, 'IGetContextProperties')
make_head(_module, 'IGetSecurityCallContext')
make_head(_module, 'IHolder')
make_head(_module, 'ILBEvents')
make_head(_module, 'IMTSActivity')
make_head(_module, 'IMTSCall')
make_head(_module, 'IMTSLocator')
make_head(_module, 'IManagedActivationEvents')
make_head(_module, 'IManagedObjectInfo')
make_head(_module, 'IManagedPoolAction')
make_head(_module, 'IManagedPooledObj')
make_head(_module, 'IMessageMover')
make_head(_module, 'IMtsEventInfo')
make_head(_module, 'IMtsEvents')
make_head(_module, 'IMtsGrp')
make_head(_module, 'IObjPool')
make_head(_module, 'IObjectConstruct')
make_head(_module, 'IObjectConstructString')
make_head(_module, 'IObjectContext')
make_head(_module, 'IObjectContextActivity')
make_head(_module, 'IObjectContextInfo')
make_head(_module, 'IObjectContextInfo2')
make_head(_module, 'IObjectContextTip')
make_head(_module, 'IObjectControl')
make_head(_module, 'IPlaybackControl')
make_head(_module, 'IPoolManager')
make_head(_module, 'IProcessInitializer')
make_head(_module, 'ISecurityCallContext')
make_head(_module, 'ISecurityCallersColl')
make_head(_module, 'ISecurityIdentityColl')
make_head(_module, 'ISecurityProperty')
make_head(_module, 'ISelectCOMLBServer')
make_head(_module, 'ISendMethodEvents')
make_head(_module, 'IServiceActivity')
make_head(_module, 'IServiceCall')
make_head(_module, 'IServiceComTIIntrinsicsConfig')
make_head(_module, 'IServiceIISIntrinsicsConfig')
make_head(_module, 'IServiceInheritanceConfig')
make_head(_module, 'IServicePartitionConfig')
make_head(_module, 'IServicePool')
make_head(_module, 'IServicePoolConfig')
make_head(_module, 'IServiceSxsConfig')
make_head(_module, 'IServiceSynchronizationConfig')
make_head(_module, 'IServiceSysTxnConfig')
make_head(_module, 'IServiceThreadPoolConfig')
make_head(_module, 'IServiceTrackerConfig')
make_head(_module, 'IServiceTransactionConfig')
make_head(_module, 'IServiceTransactionConfigBase')
make_head(_module, 'ISharedProperty')
make_head(_module, 'ISharedPropertyGroup')
make_head(_module, 'ISharedPropertyGroupManager')
make_head(_module, 'ISystemAppEventData')
make_head(_module, 'IThreadPoolKnobs')
make_head(_module, 'ITransactionContext')
make_head(_module, 'ITransactionContextEx')
make_head(_module, 'ITransactionProperty')
make_head(_module, 'ITransactionProxy')
make_head(_module, 'ITransactionResourcePool')
make_head(_module, 'ITransactionStatus')
make_head(_module, 'ITxProxyHolder')
make_head(_module, 'ObjectContext')
make_head(_module, 'ObjectControl')
make_head(_module, 'RECYCLE_INFO')
make_head(_module, 'SecurityProperty')
