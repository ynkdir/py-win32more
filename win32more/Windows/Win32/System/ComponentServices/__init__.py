from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.ComponentServices
import win32more.Windows.Win32.System.DistributedTransactionCoordinator
import win32more.Windows.Win32.System.Variant
class APPDATA(Structure):
    m_idApp: UInt32
    m_szAppGuid: Char * 40
    m_dwAppProcessId: UInt32
    m_AppStatistics: win32more.Windows.Win32.System.ComponentServices.APPSTATISTICS
class APPSTATISTICS(Structure):
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
def CoGetDefaultContext(aptType: win32more.Windows.Win32.System.Com.APTTYPE, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoCreateActivity(pIUnknown: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoEnterServiceDomain(pConfigObject: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoLeaveServiceDomain(pUnkStatus: win32more.Windows.Win32.System.Com.IUnknown) -> Void: ...
@winfunctype('comsvcs.dll')
def GetManagedExtensions(dwExts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('comsvcs.dll')
def SafeRef(rid: POINTER(Guid), pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> VoidPtr: ...
@cfunctype('comsvcs.dll')
def RecycleSurrogate(lReasonCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def MTSCreateActivity(riid: POINTER(Guid), ppobj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('MTxDM.dll')
def GetDispenserManager(param0: POINTER(win32more.Windows.Win32.System.ComponentServices.IDispenserManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AppDomainHelper = Guid('{ef24f689-14f8-4d92-b4af-d7b1f0e70fd4}')
class ApplicationProcessRecycleInfo(Structure):
    IsRecyclable: win32more.Windows.Win32.Foundation.BOOL
    IsRecycled: win32more.Windows.Win32.Foundation.BOOL
    TimeRecycled: win32more.Windows.Win32.Foundation.FILETIME
    TimeToTerminate: win32more.Windows.Win32.Foundation.FILETIME
    RecycleReasonCode: Int32
    IsPendingRecycle: win32more.Windows.Win32.Foundation.BOOL
    HasAutomaticLifetimeRecycling: win32more.Windows.Win32.Foundation.BOOL
    TimeForAutomaticRecycling: win32more.Windows.Win32.Foundation.FILETIME
    MemoryLimitInKB: UInt32
    MemoryUsageInKBLastCheck: UInt32
    ActivationLimit: UInt32
    NumActivationsLastReported: UInt32
    CallLimit: UInt32
    NumCallsLastReported: UInt32
class ApplicationProcessStatistics(Structure):
    NumCallsOutstanding: UInt32
    NumTrackedComponents: UInt32
    NumComponentInstances: UInt32
    AvgCallsPerSecond: UInt32
    Reserved1: UInt32
    Reserved2: UInt32
    Reserved3: UInt32
    Reserved4: UInt32
class ApplicationProcessSummary(Structure):
    PartitionIdPrimaryApplication: Guid
    ApplicationIdPrimaryApplication: Guid
    ApplicationInstanceId: Guid
    ProcessId: UInt32
    Type: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    ProcessExeName: win32more.Windows.Win32.Foundation.PWSTR
    IsService: win32more.Windows.Win32.Foundation.BOOL
    IsPaused: win32more.Windows.Win32.Foundation.BOOL
    IsRecycled: win32more.Windows.Win32.Foundation.BOOL
class ApplicationSummary(Structure):
    ApplicationInstanceId: Guid
    PartitionId: Guid
    ApplicationId: Guid
    Type: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    ApplicationName: win32more.Windows.Win32.Foundation.PWSTR
    NumTrackedComponents: UInt32
    NumComponentInstances: UInt32
AutoSvcs_Error_Constants = UInt32
mtsErrCtxAborted: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803138
mtsErrCtxAborting: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803139
mtsErrCtxNoContext: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803140
mtsErrCtxNotRegistered: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803141
mtsErrCtxSynchTimeout: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803142
mtsErrCtxOldReference: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803143
mtsErrCtxRoleNotFound: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803148
mtsErrCtxNoSecurity: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803149
mtsErrCtxWrongThread: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803150
mtsErrCtxTMNotAvailable: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2147803151
comQCErrApplicationNotQueued: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599296
comQCErrNoQueueableInterfaces: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599297
comQCErrQueuingServiceNotAvailable: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599298
comQCErrQueueTransactMismatch: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599299
comqcErrRecorderMarshalled: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599300
comqcErrOutParam: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599301
comqcErrRecorderNotTrusted: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599302
comqcErrPSLoad: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599303
comqcErrMarshaledObjSameTxn: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599304
comqcErrInvalidMessage: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599376
comqcErrMsmqSidUnavailable: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599377
comqcErrWrongMsgExtension: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599378
comqcErrMsmqServiceUnavailable: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599379
comqcErrMsgNotAuthenticated: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599380
comqcErrMsmqConnectorUsed: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599381
comqcErrBadMarshaledObject: win32more.Windows.Win32.System.ComponentServices.AutoSvcs_Error_Constants = 2148599382
ByotServerEx = Guid('{ecabb0aa-7f19-11d2-978e-0000f8757e2a}')
class CLSIDDATA(Structure):
    m_clsid: Guid
    m_cReferences: UInt32
    m_cBound: UInt32
    m_cPooled: UInt32
    m_cInCall: UInt32
    m_dwRespTime: UInt32
    m_cCallsCompleted: UInt32
    m_cCallsFailed: UInt32
class CLSIDDATA2(Structure):
    m_clsid: Guid
    m_appid: Guid
    m_partid: Guid
    m_pwszAppName: win32more.Windows.Win32.Foundation.PWSTR
    m_pwszCtxName: win32more.Windows.Win32.Foundation.PWSTR
    m_eAppType: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE
    m_cReferences: UInt32
    m_cBound: UInt32
    m_cPooled: UInt32
    m_cInCall: UInt32
    m_dwRespTime: UInt32
    m_cCallsCompleted: UInt32
    m_cCallsFailed: UInt32
COMAdminAccessChecksLevelOptions = Int32
COMAdminAccessChecksApplicationLevel: win32more.Windows.Win32.System.ComponentServices.COMAdminAccessChecksLevelOptions = 0
COMAdminAccessChecksApplicationComponentLevel: win32more.Windows.Win32.System.ComponentServices.COMAdminAccessChecksLevelOptions = 1
COMAdminActivationOptions = Int32
COMAdminActivationInproc: win32more.Windows.Win32.System.ComponentServices.COMAdminActivationOptions = 0
COMAdminActivationLocal: win32more.Windows.Win32.System.ComponentServices.COMAdminActivationOptions = 1
COMAdminApplicationExportOptions = Int32
COMAdminExportNoUsers: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions = 0
COMAdminExportUsers: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions = 1
COMAdminExportApplicationProxy: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions = 2
COMAdminExportForceOverwriteOfFiles: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions = 4
COMAdminExportIn10Format: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions = 16
COMAdminApplicationInstallOptions = Int32
COMAdminInstallNoUsers: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions = 0
COMAdminInstallUsers: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions = 1
COMAdminInstallForceOverwriteOfFiles: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions = 2
COMAdminAuthenticationCapabilitiesOptions = Int32
COMAdminAuthenticationCapabilitiesNone: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationCapabilitiesOptions = 0
COMAdminAuthenticationCapabilitiesSecureReference: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationCapabilitiesOptions = 2
COMAdminAuthenticationCapabilitiesStaticCloaking: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationCapabilitiesOptions = 32
COMAdminAuthenticationCapabilitiesDynamicCloaking: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationCapabilitiesOptions = 64
COMAdminAuthenticationLevelOptions = Int32
COMAdminAuthenticationDefault: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 0
COMAdminAuthenticationNone: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 1
COMAdminAuthenticationConnect: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 2
COMAdminAuthenticationCall: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 3
COMAdminAuthenticationPacket: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 4
COMAdminAuthenticationIntegrity: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 5
COMAdminAuthenticationPrivacy: win32more.Windows.Win32.System.ComponentServices.COMAdminAuthenticationLevelOptions = 6
COMAdminCatalog = Guid('{f618c514-dfb8-11d1-a2cf-00805fc79235}')
COMAdminCatalogCollection = Guid('{f618c516-dfb8-11d1-a2cf-00805fc79235}')
COMAdminCatalogObject = Guid('{f618c515-dfb8-11d1-a2cf-00805fc79235}')
COMAdminComponentFlags = Int32
COMAdminCompFlagTypeInfoFound: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 1
COMAdminCompFlagCOMPlusPropertiesFound: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 2
COMAdminCompFlagProxyFound: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 4
COMAdminCompFlagInterfacesFound: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 8
COMAdminCompFlagAlreadyInstalled: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 16
COMAdminCompFlagNotInApplication: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentFlags = 32
COMAdminComponentType = Int32
COMAdmin32BitComponent: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentType = 1
COMAdmin64BitComponent: win32more.Windows.Win32.System.ComponentServices.COMAdminComponentType = 2
COMAdminErrorCodes = Int32
COMAdminErrObjectErrors: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368511
COMAdminErrObjectInvalid: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368510
COMAdminErrKeyMissing: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368509
COMAdminErrAlreadyInstalled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368508
COMAdminErrAppFileWriteFail: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368505
COMAdminErrAppFileReadFail: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368504
COMAdminErrAppFileVersion: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368503
COMAdminErrBadPath: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368502
COMAdminErrApplicationExists: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368501
COMAdminErrRoleExists: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368500
COMAdminErrCantCopyFile: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368499
COMAdminErrNoUser: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368497
COMAdminErrInvalidUserids: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368496
COMAdminErrNoRegistryCLSID: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368495
COMAdminErrBadRegistryProgID: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368494
COMAdminErrAuthenticationLevel: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368493
COMAdminErrUserPasswdNotValid: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368492
COMAdminErrCLSIDOrIIDMismatch: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368488
COMAdminErrRemoteInterface: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368487
COMAdminErrDllRegisterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368486
COMAdminErrNoServerShare: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368485
COMAdminErrDllLoadFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368483
COMAdminErrBadRegistryLibID: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368482
COMAdminErrAppDirNotFound: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368481
COMAdminErrRegistrarFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368477
COMAdminErrCompFileDoesNotExist: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368476
COMAdminErrCompFileLoadDLLFail: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368475
COMAdminErrCompFileGetClassObj: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368474
COMAdminErrCompFileClassNotAvail: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368473
COMAdminErrCompFileBadTLB: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368472
COMAdminErrCompFileNotInstallable: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368471
COMAdminErrNotChangeable: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368470
COMAdminErrNotDeletable: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368469
COMAdminErrSession: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368468
COMAdminErrCompMoveLocked: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368467
COMAdminErrCompMoveBadDest: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368466
COMAdminErrRegisterTLB: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368464
COMAdminErrSystemApp: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368461
COMAdminErrCompFileNoRegistrar: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368460
COMAdminErrCoReqCompInstalled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368459
COMAdminErrServiceNotInstalled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368458
COMAdminErrPropertySaveFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368457
COMAdminErrObjectExists: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368456
COMAdminErrComponentExists: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368455
COMAdminErrRegFileCorrupt: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368453
COMAdminErrPropertyOverflow: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368452
COMAdminErrNotInRegistry: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368450
COMAdminErrObjectNotPoolable: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368449
COMAdminErrApplidMatchesClsid: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368442
COMAdminErrRoleDoesNotExist: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368441
COMAdminErrStartAppNeedsComponents: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368440
COMAdminErrRequiresDifferentPlatform: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368439
COMAdminErrQueuingServiceNotAvailable: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367998
COMAdminErrObjectParentMissing: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367480
COMAdminErrObjectDoesNotExist: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367479
COMAdminErrCanNotExportAppProxy: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368438
COMAdminErrCanNotStartApp: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368437
COMAdminErrCanNotExportSystemApp: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368436
COMAdminErrCanNotSubscribeToComponent: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368435
COMAdminErrAppNotRunning: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367478
COMAdminErrEventClassCannotBeSubscriber: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368434
COMAdminErrLibAppProxyIncompatible: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368433
COMAdminErrBasePartitionOnly: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368432
COMAdminErrDuplicatePartitionName: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368425
COMAdminErrPartitionInUse: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368423
COMAdminErrImportedComponentsNotAllowed: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368421
COMAdminErrRegdbNotInitialized: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368398
COMAdminErrRegdbNotOpen: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368397
COMAdminErrRegdbSystemErr: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368396
COMAdminErrRegdbAlreadyRunning: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368395
COMAdminErrMigVersionNotSupported: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368384
COMAdminErrMigSchemaNotFound: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368383
COMAdminErrCatBitnessMismatch: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368382
COMAdminErrCatUnacceptableBitness: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368381
COMAdminErrCatWrongAppBitnessBitness: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368380
COMAdminErrCatPauseResumeNotSupported: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368379
COMAdminErrCatServerFault: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368378
COMAdminErrCantRecycleLibraryApps: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367473
COMAdminErrCantRecycleServiceApps: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367471
COMAdminErrProcessAlreadyRecycled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367470
COMAdminErrPausedProcessMayNotBeRecycled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367469
COMAdminErrInvalidPartition: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367477
COMAdminErrPartitionMsiOnly: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367463
COMAdminErrStartAppDisabled: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146368431
COMAdminErrCompMoveSource: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367460
COMAdminErrCompMoveDest: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367459
COMAdminErrCompMovePrivate: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367458
COMAdminErrCannotCopyEventClass: win32more.Windows.Win32.System.ComponentServices.COMAdminErrorCodes = -2146367456
COMAdminFileFlags = Int32
COMAdminFileFlagLoadable: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 1
COMAdminFileFlagCOM: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 2
COMAdminFileFlagContainsPS: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 4
COMAdminFileFlagContainsComp: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 8
COMAdminFileFlagContainsTLB: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 16
COMAdminFileFlagSelfReg: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 32
COMAdminFileFlagSelfUnReg: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 64
COMAdminFileFlagUnloadableDLL: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 128
COMAdminFileFlagDoesNotExist: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 256
COMAdminFileFlagAlreadyInstalled: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 512
COMAdminFileFlagBadTLB: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 1024
COMAdminFileFlagGetClassObjFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 2048
COMAdminFileFlagClassNotAvailable: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 4096
COMAdminFileFlagRegistrar: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 8192
COMAdminFileFlagNoRegistrar: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 16384
COMAdminFileFlagDLLRegsvrFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 32768
COMAdminFileFlagRegTLBFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 65536
COMAdminFileFlagRegistrarFailed: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 131072
COMAdminFileFlagError: win32more.Windows.Win32.System.ComponentServices.COMAdminFileFlags = 262144
COMAdminImpersonationLevelOptions = Int32
COMAdminImpersonationAnonymous: win32more.Windows.Win32.System.ComponentServices.COMAdminImpersonationLevelOptions = 1
COMAdminImpersonationIdentify: win32more.Windows.Win32.System.ComponentServices.COMAdminImpersonationLevelOptions = 2
COMAdminImpersonationImpersonate: win32more.Windows.Win32.System.ComponentServices.COMAdminImpersonationLevelOptions = 3
COMAdminImpersonationDelegate: win32more.Windows.Win32.System.ComponentServices.COMAdminImpersonationLevelOptions = 4
COMAdminInUse = Int32
COMAdminNotInUse: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 0
COMAdminInUseByCatalog: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 1
COMAdminInUseByRegistryUnknown: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 2
COMAdminInUseByRegistryProxyStub: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 3
COMAdminInUseByRegistryTypeLib: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 4
COMAdminInUseByRegistryClsid: win32more.Windows.Win32.System.ComponentServices.COMAdminInUse = 5
COMAdminOS = Int32
COMAdminOSNotInitialized: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 0
COMAdminOSWindows3_1: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 1
COMAdminOSWindows9x: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 2
COMAdminOSWindows2000: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 3
COMAdminOSWindows2000AdvancedServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 4
COMAdminOSWindows2000Unknown: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 5
COMAdminOSUnknown: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 6
COMAdminOSWindowsXPPersonal: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 11
COMAdminOSWindowsXPProfessional: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 12
COMAdminOSWindowsNETStandardServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 13
COMAdminOSWindowsNETEnterpriseServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 14
COMAdminOSWindowsNETDatacenterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 15
COMAdminOSWindowsNETWebServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 16
COMAdminOSWindowsLonghornPersonal: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 17
COMAdminOSWindowsLonghornProfessional: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 18
COMAdminOSWindowsLonghornStandardServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 19
COMAdminOSWindowsLonghornEnterpriseServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 20
COMAdminOSWindowsLonghornDatacenterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 21
COMAdminOSWindowsLonghornWebServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 22
COMAdminOSWindows7Personal: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 23
COMAdminOSWindows7Professional: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 24
COMAdminOSWindows7StandardServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 25
COMAdminOSWindows7EnterpriseServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 26
COMAdminOSWindows7DatacenterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 27
COMAdminOSWindows7WebServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 28
COMAdminOSWindows8Personal: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 29
COMAdminOSWindows8Professional: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 30
COMAdminOSWindows8StandardServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 31
COMAdminOSWindows8EnterpriseServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 32
COMAdminOSWindows8DatacenterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 33
COMAdminOSWindows8WebServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 34
COMAdminOSWindowsBluePersonal: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 35
COMAdminOSWindowsBlueProfessional: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 36
COMAdminOSWindowsBlueStandardServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 37
COMAdminOSWindowsBlueEnterpriseServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 38
COMAdminOSWindowsBlueDatacenterServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 39
COMAdminOSWindowsBlueWebServer: win32more.Windows.Win32.System.ComponentServices.COMAdminOS = 40
COMAdminQCMessageAuthenticateOptions = Int32
COMAdminQCMessageAuthenticateSecureApps: win32more.Windows.Win32.System.ComponentServices.COMAdminQCMessageAuthenticateOptions = 0
COMAdminQCMessageAuthenticateOff: win32more.Windows.Win32.System.ComponentServices.COMAdminQCMessageAuthenticateOptions = 1
COMAdminQCMessageAuthenticateOn: win32more.Windows.Win32.System.ComponentServices.COMAdminQCMessageAuthenticateOptions = 2
COMAdminServiceOptions = Int32
COMAdminServiceLoadBalanceRouter: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceOptions = 1
COMAdminServiceStatusOptions = Int32
COMAdminServiceStopped: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 0
COMAdminServiceStartPending: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 1
COMAdminServiceStopPending: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 2
COMAdminServiceRunning: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 3
COMAdminServiceContinuePending: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 4
COMAdminServicePausePending: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 5
COMAdminServicePaused: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 6
COMAdminServiceUnknownState: win32more.Windows.Win32.System.ComponentServices.COMAdminServiceStatusOptions = 7
COMAdminSynchronizationOptions = Int32
COMAdminSynchronizationIgnored: win32more.Windows.Win32.System.ComponentServices.COMAdminSynchronizationOptions = 0
COMAdminSynchronizationNone: win32more.Windows.Win32.System.ComponentServices.COMAdminSynchronizationOptions = 1
COMAdminSynchronizationSupported: win32more.Windows.Win32.System.ComponentServices.COMAdminSynchronizationOptions = 2
COMAdminSynchronizationRequired: win32more.Windows.Win32.System.ComponentServices.COMAdminSynchronizationOptions = 3
COMAdminSynchronizationRequiresNew: win32more.Windows.Win32.System.ComponentServices.COMAdminSynchronizationOptions = 4
COMAdminThreadingModels = Int32
COMAdminThreadingModelApartment: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 0
COMAdminThreadingModelFree: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 1
COMAdminThreadingModelMain: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 2
COMAdminThreadingModelBoth: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 3
COMAdminThreadingModelNeutral: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 4
COMAdminThreadingModelNotSpecified: win32more.Windows.Win32.System.ComponentServices.COMAdminThreadingModels = 5
COMAdminTransactionOptions = Int32
COMAdminTransactionIgnored: win32more.Windows.Win32.System.ComponentServices.COMAdminTransactionOptions = 0
COMAdminTransactionNone: win32more.Windows.Win32.System.ComponentServices.COMAdminTransactionOptions = 1
COMAdminTransactionSupported: win32more.Windows.Win32.System.ComponentServices.COMAdminTransactionOptions = 2
COMAdminTransactionRequired: win32more.Windows.Win32.System.ComponentServices.COMAdminTransactionOptions = 3
COMAdminTransactionRequiresNew: win32more.Windows.Win32.System.ComponentServices.COMAdminTransactionOptions = 4
COMAdminTxIsolationLevelOptions = Int32
COMAdminTxIsolationLevelAny: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions = 0
COMAdminTxIsolationLevelReadUnCommitted: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions = 1
COMAdminTxIsolationLevelReadCommitted: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions = 2
COMAdminTxIsolationLevelRepeatableRead: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions = 3
COMAdminTxIsolationLevelSerializable: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions = 4
COMEvents = Guid('{ecabb0ab-7f19-11d2-978e-0000f8757e2a}')
COMPLUS_APPTYPE = Int32
APPTYPE_UNKNOWN: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE = -1
APPTYPE_SERVER: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE = 1
APPTYPE_LIBRARY: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE = 0
APPTYPE_SWC: win32more.Windows.Win32.System.ComponentServices.COMPLUS_APPTYPE = 2
class COMSVCSEVENTINFO(Structure):
    cbSize: UInt32
    dwPid: UInt32
    lTime: Int64
    lMicroTime: Int32
    perfCount: Int64
    guidApp: Guid
    sMachineName: win32more.Windows.Win32.Foundation.PWSTR
CRMClerk = Guid('{ecabb0bd-7f19-11d2-978e-0000f8757e2a}')
CRMFLAGS = Int32
CRMFLAG_FORGETTARGET: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 1
CRMFLAG_WRITTENDURINGPREPARE: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 2
CRMFLAG_WRITTENDURINGCOMMIT: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 4
CRMFLAG_WRITTENDURINGABORT: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 8
CRMFLAG_WRITTENDURINGRECOVERY: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 16
CRMFLAG_WRITTENDURINGREPLAY: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 32
CRMFLAG_REPLAYINPROGRESS: win32more.Windows.Win32.System.ComponentServices.CRMFLAGS = 64
CRMREGFLAGS = Int32
CRMREGFLAG_PREPAREPHASE: win32more.Windows.Win32.System.ComponentServices.CRMREGFLAGS = 1
CRMREGFLAG_COMMITPHASE: win32more.Windows.Win32.System.ComponentServices.CRMREGFLAGS = 2
CRMREGFLAG_ABORTPHASE: win32more.Windows.Win32.System.ComponentServices.CRMREGFLAGS = 4
CRMREGFLAG_ALLPHASES: win32more.Windows.Win32.System.ComponentServices.CRMREGFLAGS = 7
CRMREGFLAG_FAILIFINDOUBTSREMAIN: win32more.Windows.Win32.System.ComponentServices.CRMREGFLAGS = 16
CRMRecoveryClerk = Guid('{ecabb0be-7f19-11d2-978e-0000f8757e2a}')
CSC_Binding = Int32
CSC_NoBinding: win32more.Windows.Win32.System.ComponentServices.CSC_Binding = 0
CSC_BindToPoolThread: win32more.Windows.Win32.System.ComponentServices.CSC_Binding = 1
CSC_COMTIIntrinsicsConfig = Int32
CSC_NoCOMTIIntrinsics: win32more.Windows.Win32.System.ComponentServices.CSC_COMTIIntrinsicsConfig = 0
CSC_InheritCOMTIIntrinsics: win32more.Windows.Win32.System.ComponentServices.CSC_COMTIIntrinsicsConfig = 1
CSC_IISIntrinsicsConfig = Int32
CSC_NoIISIntrinsics: win32more.Windows.Win32.System.ComponentServices.CSC_IISIntrinsicsConfig = 0
CSC_InheritIISIntrinsics: win32more.Windows.Win32.System.ComponentServices.CSC_IISIntrinsicsConfig = 1
CSC_InheritanceConfig = Int32
CSC_Inherit: win32more.Windows.Win32.System.ComponentServices.CSC_InheritanceConfig = 0
CSC_Ignore: win32more.Windows.Win32.System.ComponentServices.CSC_InheritanceConfig = 1
CSC_PartitionConfig = Int32
CSC_NoPartition: win32more.Windows.Win32.System.ComponentServices.CSC_PartitionConfig = 0
CSC_InheritPartition: win32more.Windows.Win32.System.ComponentServices.CSC_PartitionConfig = 1
CSC_NewPartition: win32more.Windows.Win32.System.ComponentServices.CSC_PartitionConfig = 2
CSC_SxsConfig = Int32
CSC_NoSxs: win32more.Windows.Win32.System.ComponentServices.CSC_SxsConfig = 0
CSC_InheritSxs: win32more.Windows.Win32.System.ComponentServices.CSC_SxsConfig = 1
CSC_NewSxs: win32more.Windows.Win32.System.ComponentServices.CSC_SxsConfig = 2
CSC_SynchronizationConfig = Int32
CSC_NoSynchronization: win32more.Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig = 0
CSC_IfContainerIsSynchronized: win32more.Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig = 1
CSC_NewSynchronizationIfNecessary: win32more.Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig = 2
CSC_NewSynchronization: win32more.Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig = 3
CSC_ThreadPool = Int32
CSC_ThreadPoolNone: win32more.Windows.Win32.System.ComponentServices.CSC_ThreadPool = 0
CSC_ThreadPoolInherit: win32more.Windows.Win32.System.ComponentServices.CSC_ThreadPool = 1
CSC_STAThreadPool: win32more.Windows.Win32.System.ComponentServices.CSC_ThreadPool = 2
CSC_MTAThreadPool: win32more.Windows.Win32.System.ComponentServices.CSC_ThreadPool = 3
CSC_TrackerConfig = Int32
CSC_DontUseTracker: win32more.Windows.Win32.System.ComponentServices.CSC_TrackerConfig = 0
CSC_UseTracker: win32more.Windows.Win32.System.ComponentServices.CSC_TrackerConfig = 1
CSC_TransactionConfig = Int32
CSC_NoTransaction: win32more.Windows.Win32.System.ComponentServices.CSC_TransactionConfig = 0
CSC_IfContainerIsTransactional: win32more.Windows.Win32.System.ComponentServices.CSC_TransactionConfig = 1
CSC_CreateTransactionIfNecessary: win32more.Windows.Win32.System.ComponentServices.CSC_TransactionConfig = 2
CSC_NewTransaction: win32more.Windows.Win32.System.ComponentServices.CSC_TransactionConfig = 3
CServiceConfig = Guid('{ecabb0c8-7f19-11d2-978e-0000f8757e2a}')
ClrAssemblyLocator = Guid('{458aa3b5-265a-4b75-bc05-9bea4630cf18}')
CoMTSLocator = Guid('{ecabb0ac-7f19-11d2-978e-0000f8757e2a}')
ComServiceEvents = Guid('{ecabb0c3-7f19-11d2-978e-0000f8757e2a}')
ComSystemAppEventData = Guid('{ecabb0c6-7f19-11d2-978e-0000f8757e2a}')
class ComponentHangMonitorInfo(Structure):
    IsMonitored: win32more.Windows.Win32.Foundation.BOOL
    TerminateOnHang: win32more.Windows.Win32.Foundation.BOOL
    AvgCallThresholdInMs: UInt32
class ComponentStatistics(Structure):
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
class ComponentSummary(Structure):
    ApplicationInstanceId: Guid
    PartitionId: Guid
    ApplicationId: Guid
    Clsid: Guid
    ClassName: win32more.Windows.Win32.Foundation.PWSTR
    ApplicationName: win32more.Windows.Win32.Foundation.PWSTR
class ContextInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{19a5a02c-0ac8-11d2-b286-00c04f8ef934}')
    @commethod(7)
    def IsInTransaction(self, pbIsInTx: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransaction(self, ppTx: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransactionId(self, pbstrTxId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityId(self, pbstrActivityId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetContextId(self, pbstrCtxId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ContextInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.ContextInfo
    _iid_ = Guid('{c99d6e75-2375-11d4-8331-00c04f605588}')
    @commethod(12)
    def GetPartitionId(self, __MIDL__ContextInfo20000: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetApplicationId(self, __MIDL__ContextInfo20001: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetApplicationInstanceId(self, __MIDL__ContextInfo20002: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class CrmLogRecordRead(Structure):
    dwCrmFlags: UInt32
    dwSequenceNumber: UInt32
    blobUserData: win32more.Windows.Win32.System.Com.BLOB
CrmTransactionState = Int32
TxState_Active: win32more.Windows.Win32.System.ComponentServices.CrmTransactionState = 0
TxState_Committed: win32more.Windows.Win32.System.ComponentServices.CrmTransactionState = 1
TxState_Aborted: win32more.Windows.Win32.System.ComponentServices.CrmTransactionState = 2
TxState_Indoubt: win32more.Windows.Win32.System.ComponentServices.CrmTransactionState = 3
DUMPTYPE = Int32
DUMPTYPE_FULL: win32more.Windows.Win32.System.ComponentServices.DUMPTYPE = 0
DUMPTYPE_MINI: win32more.Windows.Win32.System.ComponentServices.DUMPTYPE = 1
DUMPTYPE_NONE: win32more.Windows.Win32.System.ComponentServices.DUMPTYPE = 2
DispenserManager = Guid('{ecabb0c0-7f19-11d2-978e-0000f8757e2a}')
Dummy30040732 = Guid('{ecabb0a9-7f19-11d2-978e-0000f8757e2a}')
EventServer = Guid('{ecabafbc-7f19-11d2-978e-0000f8757e2a}')
GetAppTrackerDataFlags = Int32
GATD_INCLUDE_PROCESS_EXE_NAME: win32more.Windows.Win32.System.ComponentServices.GetAppTrackerDataFlags = 1
GATD_INCLUDE_LIBRARY_APPS: win32more.Windows.Win32.System.ComponentServices.GetAppTrackerDataFlags = 2
GATD_INCLUDE_SWC: win32more.Windows.Win32.System.ComponentServices.GetAppTrackerDataFlags = 4
GATD_INCLUDE_CLASS_NAME: win32more.Windows.Win32.System.ComponentServices.GetAppTrackerDataFlags = 8
GATD_INCLUDE_APPLICATION_NAME: win32more.Windows.Win32.System.ComponentServices.GetAppTrackerDataFlags = 16
GetSecurityCallContextAppObject = Guid('{ecabb0a8-7f19-11d2-978e-0000f8757e2a}')
class HANG_INFO(Structure):
    fAppHangMonitorEnabled: win32more.Windows.Win32.Foundation.BOOL
    fTerminateOnHang: win32more.Windows.Win32.Foundation.BOOL
    DumpType: win32more.Windows.Win32.System.ComponentServices.DUMPTYPE
    dwHangTimeout: UInt32
    dwDumpCount: UInt32
    dwInfoMsgCount: UInt32
class IAppDomainHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c7b67079-8255-42c6-9ec0-6994a3548780}')
    @commethod(7)
    def Initialize(self, pUnkAD: win32more.Windows.Win32.System.Com.IUnknown, __MIDL__IAppDomainHelper0000: IntPtr, pPool: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DoCallback(self, pUnkAD: win32more.Windows.Win32.System.Com.IUnknown, __MIDL__IAppDomainHelper0001: IntPtr, pPool: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAssemblyLocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{391ffbb9-a8ee-432a-abc8-baa238dab90f}')
    @commethod(7)
    def GetModules(self, applicationDir: win32more.Windows.Win32.Foundation.BSTR, applicationName: win32more.Windows.Win32.Foundation.BSTR, assemblyName: win32more.Windows.Win32.Foundation.BSTR, pModules: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAsyncErrorNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fe6777fb-a674-4177-8f32-6d707e113484}')
    @commethod(3)
    def OnError(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICOMAdminCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dd662187-dfc2-11d1-a2cf-00805fc79235}')
    @commethod(7)
    def GetCollection(self, bstrCollName: win32more.Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Connect(self, bstrCatalogServerName: win32more.Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MajorVersion(self, plMajorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MinorVersion(self, plMinorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCollectionByQuery(self, bstrCollName: win32more.Windows.Win32.Foundation.BSTR, ppsaVarQuery: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ImportComponent(self, bstrApplIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrCLSIDOrProgID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def InstallComponent(self, bstrApplIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrDLL: win32more.Windows.Win32.Foundation.BSTR, bstrTLB: win32more.Windows.Win32.Foundation.BSTR, bstrPSDLL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ShutdownApplication(self, bstrApplIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExportApplication(self, bstrApplIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrApplicationFile: win32more.Windows.Win32.Foundation.BSTR, lOptions: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InstallApplication(self, bstrApplicationFile: win32more.Windows.Win32.Foundation.BSTR, bstrDestinationDirectory: win32more.Windows.Win32.Foundation.BSTR, lOptions: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserId: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bstrRSN: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def StopRouter(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RefreshRouter(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def StartRouter(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Reserved1(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Reserved2(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def InstallMultipleComponents(self, bstrApplIDOrName: win32more.Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarCLSIDs: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMultipleComponentsInfo(self, bstrApplIdOrName: win32more.Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarCLSIDs: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarClassNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarFileFlags: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarComponentFlags: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RefreshComponents(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def BackupREGDB(self, bstrBackupFilePath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RestoreREGDB(self, bstrBackupFilePath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def QueryApplicationFile(self, bstrApplicationFile: win32more.Windows.Win32.Foundation.BSTR, pbstrApplicationName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrApplicationDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbHasUsers: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), pbIsProxy: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppsaVarFileNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def StartApplication(self, bstrApplIdOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ServiceCheck(self, lService: Int32, plStatus: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def InstallMultipleEventClasses(self, bstrApplIdOrName: win32more.Windows.Win32.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarCLSIDS: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def InstallEventClass(self, bstrApplIdOrName: win32more.Windows.Win32.Foundation.BSTR, bstrDLL: win32more.Windows.Win32.Foundation.BSTR, bstrTLB: win32more.Windows.Win32.Foundation.BSTR, bstrPSDLL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetEventClassesForIID(self, bstrIID: win32more.Windows.Win32.Foundation.BSTR, ppsaVarCLSIDs: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarProgIDs: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppsaVarDescriptions: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICOMAdminCatalog2(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.ICOMAdminCatalog
    _iid_ = Guid('{790c6e0b-9194-4cc9-9426-a48a63185696}')
    @commethod(33)
    def GetCollectionByQuery2(self, bstrCollectionName: win32more.Windows.Win32.Foundation.BSTR, pVarQueryStrings: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetApplicationInstanceIDFromProcessID(self, lProcessID: Int32, pbstrApplicationInstanceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ShutdownApplicationInstances(self, pVarApplicationInstanceID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PauseApplicationInstances(self, pVarApplicationInstanceID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def ResumeApplicationInstances(self, pVarApplicationInstanceID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RecycleApplicationInstances(self, pVarApplicationInstanceID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lReasonCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AreApplicationInstancesPaused(self, pVarApplicationInstanceID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pVarBoolPaused: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def DumpApplicationInstance(self, bstrApplicationInstanceID: win32more.Windows.Win32.Foundation.BSTR, bstrDirectory: win32more.Windows.Win32.Foundation.BSTR, lMaxImages: Int32, pbstrDumpFile: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsApplicationInstanceDumpSupported(self, pVarBoolDumpSupported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def CreateServiceForApplication(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrServiceName: win32more.Windows.Win32.Foundation.BSTR, bstrStartType: win32more.Windows.Win32.Foundation.BSTR, bstrErrorControl: win32more.Windows.Win32.Foundation.BSTR, bstrDependencies: win32more.Windows.Win32.Foundation.BSTR, bstrRunAs: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bDesktopOk: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def DeleteServiceForApplication(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetPartitionID(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pbstrPartitionID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetPartitionName(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pbstrPartitionName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_CurrentPartition(self, bstrPartitionIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_CurrentPartitionID(self, pbstrPartitionID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_CurrentPartitionName(self, pbstrPartitionName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_GlobalPartitionID(self, pbstrGlobalPartitionID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def FlushPartitionCache(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def CopyApplications(self, bstrSourcePartitionIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarApplicationID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrDestinationPartitionIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def CopyComponents(self, bstrSourceApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrDestinationApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def MoveComponents(self, bstrSourceApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrDestinationApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def AliasComponent(self, bstrSrcApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrCLSIDOrProgID: win32more.Windows.Win32.Foundation.BSTR, bstrDestApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrNewProgId: win32more.Windows.Win32.Foundation.BSTR, bstrNewClsid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def IsSafeToDelete(self, bstrDllName: win32more.Windows.Win32.Foundation.BSTR, pCOMAdminInUse: POINTER(win32more.Windows.Win32.System.ComponentServices.COMAdminInUse)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ImportUnconfiguredComponents(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pVarComponentType: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def PromoteUnconfiguredComponents(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pVarComponentType: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def ImportComponents(self, bstrApplicationIDOrName: win32more.Windows.Win32.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pVarComponentType: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_Is64BitCatalogServer(self, pbIs64Bit: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def ExportPartition(self, bstrPartitionIDOrName: win32more.Windows.Win32.Foundation.BSTR, bstrPartitionFileName: win32more.Windows.Win32.Foundation.BSTR, lOptions: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationExportOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def InstallPartition(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, bstrDestDirectory: win32more.Windows.Win32.Foundation.BSTR, lOptions: win32more.Windows.Win32.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserID: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, bstrRSN: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def QueryApplicationFile2(self, bstrApplicationFile: win32more.Windows.Win32.Foundation.BSTR, ppFilesForImport: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetComponentVersionCount(self, bstrCLSIDOrProgID: win32more.Windows.Win32.Foundation.BSTR, plVersionCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICOMLBArguments(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a0f150f-8ee5-4b94-b40e-aef2f9e42ed2}')
    @commethod(3)
    def GetCLSID(self, pCLSID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCLSID(self, pCLSID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMachineName(self, cchSvr: UInt32, szServerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMachineName(self, cchSvr: UInt32, szServerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatalogCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22872-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def get__NewEnum(self, ppEnumVariant: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, ppCatalogObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, plObjectCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, lIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, ppCatalogObject: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Populate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveChanges(self, pcChanges: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCollection(self, bstrCollName: win32more.Windows.Win32.Foundation.BSTR, varObjectKey: win32more.Windows.Win32.System.Variant.VARIANT, ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Name(self, pVarNamel: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_AddEnabled(self, pVarBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoveEnabled(self, pVarBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetUtilInterface(self, ppIDispatch: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DataStoreMajorVersion(self, plMajorVersion: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DataStoreMinorVersion(self, plMinorVersionl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PopulateByKey(self, psaKeys: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def PopulateByQuery(self, bstrQueryString: win32more.Windows.Win32.Foundation.BSTR, lQueryType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatalogObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22871-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def get_Value(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, pvarRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, val: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Key(self, pvarRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Name(self, pvarRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsPropertyReadOnly(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, pbRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Valid(self, pbRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsPropertyWriteOnly(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, pbRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICheckSxsConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ff5a96f-11fc-47d1-baa6-25dd347e7242}')
    @commethod(3)
    def IsSameSxsConfig(self, wszSxsName: win32more.Windows.Win32.Foundation.PWSTR, wszSxsDirectory: win32more.Windows.Win32.Foundation.PWSTR, wszSxsAppName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComActivityEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b0-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnActivityCreate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnActivityDestroy(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnActivityEnter(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnActivityTimeout(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32, dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnActivityReenter(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidCurrent: POINTER(Guid), dwThread: UInt32, dwCallDepth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnActivityLeave(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidCurrent: POINTER(Guid), guidLeft: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnActivityLeaveSame(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidCurrent: POINTER(Guid), dwCallDepth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComApp2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1290bc1a-b219-418d-b078-5934ded08242}')
    @commethod(3)
    def OnAppActivation2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid, guidProcess: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnAppPaused2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid, bPaused: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnAppRecycle2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid, guidProcess: Guid, lReason: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComAppEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a6-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnAppActivation(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComCRMEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b5-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnCRMRecoveryStart(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCRMRecoveryDone(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCRMCheckpoint(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidApp: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnCRMBegin(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid, guidActivity: Guid, guidTx: Guid, szProgIdCompensator: win32more.Windows.Win32.Foundation.PWSTR, szDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnCRMPrepare(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnCRMCommit(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnCRMAbort(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnCRMIndoubt(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnCRMDone(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnCRMRelease(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnCRMAnalyze(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid, dwCrmRecordType: UInt32, dwRecordSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnCRMWrite(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid, fVariants: win32more.Windows.Win32.Foundation.BOOL, dwRecordSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnCRMForget(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnCRMForce(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnCRMDeliver(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidClerkCLSID: Guid, fVariants: win32more.Windows.Win32.Foundation.BOOL, dwRecordSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComExceptionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b3-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnExceptionUser(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), code: UInt32, address: UInt64, pszStackTrace: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComIdentityEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b1-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnIISRequestInfo(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjId: UInt64, pszClientIP: win32more.Windows.Win32.Foundation.PWSTR, pszServerIP: win32more.Windows.Win32.Foundation.PWSTR, pszURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComInstance2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20e3bf07-b506-4ad5-a50c-d2ca5b9c158e}')
    @commethod(3)
    def OnObjectCreate2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64, guidPartition: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComInstanceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a7-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectCreate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComLTxEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{605cf82c-578e-4298-975d-82babcd9e053}')
    @commethod(3)
    def OnLtxTransactionStart(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidLtx: Guid, tsid: Guid, fRoot: win32more.Windows.Win32.Foundation.BOOL, nIsolationLevel: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnLtxTransactionPrepare(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidLtx: Guid, fVote: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLtxTransactionAbort(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidLtx: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnLtxTransactionCommit(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidLtx: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnLtxTransactionPromote(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidLtx: Guid, txnId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComMethod2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb388aaa-567d-4024-af8e-6e93ee748573}')
    @commethod(3)
    def OnMethodCall2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32, hresult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComMethodEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a9-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnMethodCall(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32, hresult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComMtaThreadPoolKnobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9a76d2e-76a5-43eb-a0c4-49bec8e48480}')
    @commethod(3)
    def MTASetMaxThreadCount(self, dwMaxThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MTAGetMaxThreadCount(self, pdwMaxThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MTASetThrottleValue(self, dwThrottle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def MTAGetThrottleValue(self, pdwThrottle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectConstruction2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b5a7827-8df2-45c0-8f6f-57ea1f856a9f}')
    @commethod(3)
    def OnObjectConstruct2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), sConstructString: win32more.Windows.Win32.Foundation.PWSTR, oid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectConstructionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130af-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectConstruct(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), sConstructString: win32more.Windows.Win32.Foundation.PWSTR, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130aa-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjectActivate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDeactivate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDisableCommit(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnEnableCommit(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSetComplete(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnSetAbort(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), CtxtID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectPool2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65bf6534-85ea-4f64-8cf4-3d974b2ab1cf}')
    @commethod(3)
    def OnObjPoolPutObject2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectPoolEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ad-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjPoolPutObject(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComObjectPoolEvents2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ae-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnObjPoolCreateObject(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolDestroyObject(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolCreateDecision(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), dwThreadsWaiting: UInt32, dwAvail: UInt32, dwCreated: UInt32, dwMin: UInt32, dwMax: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolTimeout(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), guidActivity: POINTER(Guid), dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnObjPoolCreatePool(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidObject: POINTER(Guid), dwMin: UInt32, dwMax: UInt32, dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComQCEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b2-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnQCRecord(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), objid: UInt64, szQueue: win32more.Windows.Win32.Foundation.PWSTR, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), msmqhr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnQCQueueOpen(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), szQueue: win32more.Windows.Win32.Foundation.PWSTR, QueueID: UInt64, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnQCReceive(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), QueueID: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnQCReceiveFail(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), QueueID: UInt64, msmqhr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnQCMoveToReTryQueue(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), RetryIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnQCMoveToDeadQueue(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnQCPlayback(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), objid: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComResourceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ab-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnResourceCreate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjectID: UInt64, pszType: win32more.Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnResourceAllocate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjectID: UInt64, pszType: win32more.Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Windows.Win32.Foundation.BOOL, NumRated: UInt32, Rating: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnResourceRecycle(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjectID: UInt64, pszType: win32more.Windows.Win32.Foundation.PWSTR, resId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnResourceDestroy(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjectID: UInt64, hr: win32more.Windows.Win32.Foundation.HRESULT, pszType: win32more.Windows.Win32.Foundation.PWSTR, resId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnResourceTrack(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ObjectID: UInt64, pszType: win32more.Windows.Win32.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComSecurityEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130ac-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnAuthenticate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: POINTER(Byte), cbByteCur: UInt32, pSidCurrentUser: POINTER(Byte), bCurrentUserInpersonatingInProc: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAuthenticateFail(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: POINTER(Byte), cbByteCur: UInt32, pSidCurrentUser: POINTER(Byte), bCurrentUserInpersonatingInProc: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{324b64fa-33b6-11d2-98b7-00c04f8ee1c4}')
    @commethod(3)
    def SetMinThreadCount(self, minThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinThreadCount(self, minThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreadCount(self, maxThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxThreadCount(self, maxThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetActivityPerThread(self, activitiesPerThread: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetActivityPerThread(self, activitiesPerThread: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetActivityRatio(self, activityRatio: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityRatio(self, activityRatio: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetThreadCount(self, pdwThreads: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQueueDepth(self, pdwQDepth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetQueueDepth(self, dwQDepth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs2(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.IComStaThreadPoolKnobs
    _iid_ = Guid('{73707523-ff9a-4974-bf84-2108dc213740}')
    @commethod(14)
    def GetMaxCPULoad(self, pdwLoad: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetMaxCPULoad(self, pdwLoad: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCPUMetricEnabled(self, pbMetricEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetCPUMetricEnabled(self, bMetricEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCreateThreadsAggressively(self, pbMetricEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetCreateThreadsAggressively(self, bMetricEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaxCSR(self, pdwCSR: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetMaxCSR(self, dwCSR: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetWaitTimeForThreadCleanup(self, pdwThreadCleanupWaitTime: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetWaitTimeForThreadCleanup(self, dwThreadCleanupWaitTime: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComThreadEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a5-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnThreadStart(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnThreadTerminate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadBindToApartment(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32, dwLowCnt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnThreadUnBind(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnThreadWorkEnque(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnThreadWorkPrivate(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, MsgWorkID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnThreadWorkPublic(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnThreadWorkRedirect(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32, ThreadNum: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnThreadWorkReject(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnThreadAssignApartment(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidActivity: POINTER(Guid), AptID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnThreadUnassignApartment(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), AptID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c266c677-c9ad-49ab-9fd9-d9661078588a}')
    @commethod(3)
    def Type(self, pType: POINTER(win32more.Windows.Win32.System.ComponentServices.TRACKING_COLL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Count(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, ulIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e6cdcc9-fb25-4fd5-9cc5-c9f4b6559cec}')
    @commethod(3)
    def OnNewTrackingInfo(self, pToplevelCollection: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{116e42c5-d8b1-47bf-ab1e-c895ed3e2372}')
    @commethod(3)
    def GetValue(self, szPropertyName: win32more.Windows.Win32.Foundation.PWSTR, pvarOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTrackingInfoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{789b42be-6f6b-443a-898e-67abf390aa14}')
    @commethod(3)
    def PropCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropName(self, ulIndex: UInt32, ppszPropName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTransaction2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a136f62a-2f94-4288-86e0-d8a1fa4c0299}')
    @commethod(3)
    def OnTransactionStart2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: win32more.Windows.Win32.Foundation.BOOL, nIsolationLevel: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid), fVoteYes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit2(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComTransactionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a8-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnTransactionStart(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid), fVoteYes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), guidTx: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComUserEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130a4-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def OnUserEvent(self, pInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.COMSVCSEVENTINFO), pvarEvent: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d396da85-bf8f-11d1-bbae-00c04fc2fa5f}')
    @commethod(3)
    def Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(self, ppenum: POINTER(win32more.Windows.Win32.System.ComponentServices.IEnumNames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, property: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProperty(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextSecurityPerimeter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7549a29-a7c4-42e1-8dc1-7e3d748dc24a}')
    @commethod(3)
    def GetPerimeterFlag(self, pFlag: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPerimeterFlag(self, fFlag: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c05e54b-a42a-11d2-afc4-00c04f8ee1c4}')
    @commethod(3)
    def SetDeactivateOnReturn(self, bDeactivate: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeactivateOnReturn(self, pbDeactivate: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMyTransactionVote(self, txVote: win32more.Windows.Win32.System.ComponentServices.TransactionVote) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMyTransactionVote(self, ptxVote: POINTER(win32more.Windows.Win32.System.ComponentServices.TransactionVote)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateWithLocalTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{227ac7a8-8423-42ce-b7cf-03061ec9aaa3}')
    @commethod(3)
    def CreateInstanceWithSysTx(self, pTransaction: win32more.Windows.Win32.System.Com.IUnknown, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateWithTipTransactionEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{455acf59-5345-11d2-99cf-00c04f797bc9}')
    @commethod(3)
    def CreateInstance(self, bstrTipUrl: win32more.Windows.Win32.Foundation.BSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateWithTransactionEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{455acf57-5345-11d2-99cf-00c04f797bc9}')
    @commethod(3)
    def CreateInstance(self, pTransaction: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmCompensator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bbc01830-8d3b-11d1-82ec-00a0c91eede9}')
    @commethod(3)
    def SetLogControl(self, pLogControl: win32more.Windows.Win32.System.ComponentServices.ICrmLogControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepare(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecord(self, crmLogRec: win32more.Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepare(self, pfOkToPrepare: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommit(self, fRecovery: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecord(self, crmLogRec: win32more.Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbort(self, fRecovery: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecord(self, crmLogRec: win32more.Windows.Win32.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmCompensatorVariants(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0baf8e4-7804-11d1-82e9-00a0c91eede9}')
    @commethod(3)
    def SetLogControlVariants(self, pLogControl: win32more.Windows.Win32.System.ComponentServices.ICrmLogControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepareVariants(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecordVariants(self, pLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pbForget: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepareVariants(self, pbOkToPrepare: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommitVariants(self, bRecovery: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecordVariants(self, pLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pbForget: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommitVariants(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbortVariants(self, bRecovery: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecordVariants(self, pLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pbForget: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbortVariants(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmFormatLogRecords(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c51d821-c98b-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def GetColumnCount(self, plColumnCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaders(self, pHeaders: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColumn(self, CrmLogRec: win32more.Windows.Win32.System.ComponentServices.CrmLogRecordRead, pFormattedLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnVariants(self, LogRecord: win32more.Windows.Win32.System.Variant.VARIANT, pFormattedLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmLogControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0e174b3-d26e-11d2-8f84-00805fc7bcd9}')
    @commethod(3)
    def get_TransactionUOW(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCompensator(self, lpcwstrProgIdCompensator: win32more.Windows.Win32.Foundation.PWSTR, lpcwstrDescription: win32more.Windows.Win32.Foundation.PWSTR, lCrmRegFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteLogRecordVariants(self, pLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ForceLog(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ForgetLogRecord(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ForceTransactionToAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteLogRecord(self, rgBlob: POINTER(win32more.Windows.Win32.System.Com.BLOB), cBlob: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70c8e443-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def GetClerks(self, pClerks: POINTER(win32more.Windows.Win32.System.ComponentServices.ICrmMonitorClerks)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HoldClerk(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitorClerks(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{70c8e442-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(7)
    def Item(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProgIdCompensator(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Description(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TransactionUOW(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ActivityId(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICrmMonitorLogRecords(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70c8e441-c7ed-11d1-82fb-00a0c91eede9}')
    @commethod(3)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TransactionState(self, pVal: POINTER(win32more.Windows.Win32.System.ComponentServices.CrmTransactionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_StructuredRecords(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLogRecord(self, dwIndex: UInt32, pCrmLogRec: POINTER(win32more.Windows.Win32.System.ComponentServices.CrmLogRecordRead)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLogRecordVariants(self, IndexNumber: win32more.Windows.Win32.System.Variant.VARIANT, pLogRecord: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispenserDriver(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{208b3651-2b48-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def CreateResource(self, ResTypId: UIntPtr, pResId: POINTER(UIntPtr), pSecsFreeBeforeDestroy: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RateResource(self, ResTypId: UIntPtr, ResId: UIntPtr, fRequiresTransactionEnlistment: win32more.Windows.Win32.Foundation.BOOL, pRating: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistResource(self, ResId: UIntPtr, TransId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ResetResource(self, ResId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyResource(self, ResId: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DestroyResourceS(self, ResId: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispenserManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cb31e10-2b5f-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def RegisterDispenser(self, __MIDL__IDispenserManager0000: win32more.Windows.Win32.System.ComponentServices.IDispenserDriver, szDispenserName: win32more.Windows.Win32.Foundation.PWSTR, __MIDL__IDispenserManager0001: POINTER(win32more.Windows.Win32.System.ComponentServices.IHolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContext(self, __MIDL__IDispenserManager0002: POINTER(UIntPtr), __MIDL__IDispenserManager0003: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumNames(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af2-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Next(self, celt: UInt32, rgname: POINTER(win32more.Windows.Win32.Foundation.BSTR), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.ComponentServices.IEnumNames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventServerTrace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9a9f12b8-80af-47ab-a579-35ea57725370}')
    @commethod(7)
    def StartTraceGuid(self, bstrguidEvent: win32more.Windows.Win32.Foundation.BSTR, bstrguidFilter: win32more.Windows.Win32.Foundation.BSTR, lPidFilter: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopTraceGuid(self, bstrguidEvent: win32more.Windows.Win32.Foundation.BSTR, bstrguidFilter: win32more.Windows.Win32.Foundation.BSTR, lPidFilter: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTraceGuid(self, plCntGuids: POINTER(Int32), pbstrGuidList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetAppTrackerData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{507c3ac8-3e12-4cb0-9366-653d3e050638}')
    @commethod(3)
    def GetApplicationProcesses(self, PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumApplicationProcesses: POINTER(UInt32), ApplicationProcesses: POINTER(POINTER(win32more.Windows.Win32.System.ComponentServices.ApplicationProcessSummary))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplicationProcessDetails(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Flags: UInt32, Summary: POINTER(win32more.Windows.Win32.System.ComponentServices.ApplicationProcessSummary), Statistics: POINTER(win32more.Windows.Win32.System.ComponentServices.ApplicationProcessStatistics), RecycleInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.ApplicationProcessRecycleInfo), AnyComponentsHangMonitored: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplicationsInProcess(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), Flags: UInt32, NumApplicationsInProcess: POINTER(UInt32), Applications: POINTER(POINTER(win32more.Windows.Win32.System.ComponentServices.ApplicationSummary))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentsInProcess(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumComponentsInProcess: POINTER(UInt32), Components: POINTER(POINTER(win32more.Windows.Win32.System.ComponentServices.ComponentSummary))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentDetails(self, ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Clsid: POINTER(Guid), Flags: UInt32, Summary: POINTER(win32more.Windows.Win32.System.ComponentServices.ComponentSummary), Statistics: POINTER(win32more.Windows.Win32.System.ComponentServices.ComponentStatistics), HangMonitorInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.ComponentHangMonitorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTrackerDataAsCollectionObject(self, TopLevelCollection: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSuggestedPollingInterval(self, PollingIntervalInSeconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetContextProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af4-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, pProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(self, ppenum: POINTER(win32more.Windows.Win32.System.ComponentServices.IEnumNames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetSecurityCallContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823f-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def GetSecurityCallContext(self, ppObject: POINTER(win32more.Windows.Win32.System.ComponentServices.ISecurityCallContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf6a1850-2b45-11cf-be10-00aa00a2fa25}')
    @commethod(3)
    def AllocResource(self, __MIDL__IHolder0000: UIntPtr, __MIDL__IHolder0001: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeResource(self, __MIDL__IHolder0002: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TrackResource(self, __MIDL__IHolder0003: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TrackResourceS(self, __MIDL__IHolder0004: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UntrackResource(self, __MIDL__IHolder0005: UIntPtr, __MIDL__IHolder0006: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UntrackResourceS(self, __MIDL__IHolder0007: POINTER(UInt16), __MIDL__IHolder0008: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RequestDestroyResource(self, __MIDL__IHolder0009: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILBEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683130b4-2e50-11d2-98a5-00c04f8ee1c4}')
    @commethod(3)
    def TargetUp(self, bstrServerName: win32more.Windows.Win32.Foundation.BSTR, bstrClsidEng: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TargetDown(self, bstrServerName: win32more.Windows.Win32.Foundation.BSTR, bstrClsidEng: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EngineDefined(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, varPropValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrClsidEng: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMTSActivity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af0-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def SynchronousCall(self, pCall: win32more.Windows.Win32.System.ComponentServices.IMTSCall) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AsyncCall(self, pCall: win32more.Windows.Win32.System.ComponentServices.IMTSCall) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reserved1(self) -> Void: ...
    @commethod(6)
    def BindToCurrentThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnbindFromThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMTSCall(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aef-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def OnCall(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMTSLocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d19b8bfd-7f88-11d0-b16e-00aa00ba3258}')
    @commethod(7)
    def GetEventDispatcher(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManagedActivationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5f325af-572f-46da-b8ab-827c3d95d99e}')
    @commethod(3)
    def CreateManagedStub(self, pInfo: win32more.Windows.Win32.System.ComponentServices.IManagedObjectInfo, fDist: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DestroyManagedStub(self, pInfo: win32more.Windows.Win32.System.ComponentServices.IManagedObjectInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManagedObjectInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1427c51a-4584-49d8-90a0-c50d8086cbe9}')
    @commethod(3)
    def GetIUnknown(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIObjectControl(self, pCtrl: POINTER(win32more.Windows.Win32.System.ComponentServices.IObjectControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetInPool(self, bInPool: win32more.Windows.Win32.Foundation.BOOL, pPooledObj: win32more.Windows.Win32.System.ComponentServices.IManagedPooledObj) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetWrapperStrength(self, bStrong: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManagedPoolAction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da91b74e-5388-4783-949d-c1cd5fb00506}')
    @commethod(3)
    def LastRelease(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IManagedPooledObj(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5da4bea-1b42-4437-8926-b6a38860a770}')
    @commethod(3)
    def SetHeld(self, m_bHeld: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMessageMover(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{588a085a-b795-11d1-8054-00c04fc340ee}')
    @commethod(7)
    def get_SourcePath(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SourcePath(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DestPath(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DestPath(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CommitBatchSize(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CommitBatchSize(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def MoveMessages(self, plMessagesMoved: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMtsEventInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d56c3dc1-8482-11d0-b170-00aa00ba3258}')
    @commethod(7)
    def get_Names(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(self, sDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventID(self, sGuidEventID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(self, lCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Value(self, sKey: win32more.Windows.Win32.Foundation.BSTR, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMtsEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bacedf4d-74ab-11d0-b162-00aa00ba3258}')
    @commethod(7)
    def get_PackageName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PackageGuid(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PostEvent(self, vEvent: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FireEvents(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetProcessID(self, id: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMtsGrp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4b2e958c-0393-11d1-b1ab-00aa00ba3258}')
    @commethod(7)
    def get_Count(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, lIndex: Int32, ppUnkDispatcher: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjPool(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
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
    def PutEndTx(self, pObj: win32more.Windows.Win32.System.Com.IUnknown) -> Void: ...
    @commethod(8)
    def Reserved5(self) -> Void: ...
    @commethod(9)
    def Reserved6(self) -> Void: ...
class IObjectConstruct(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41c4f8b3-7439-11d2-98cb-00c04f8ee1c4}')
    @commethod(3)
    def Construct(self, pCtorObj: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectConstructString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{41c4f8b2-7439-11d2-98cb-00c04f8ee1c4}')
    @commethod(7)
    def get_ConstructString(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372ae0-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def CreateInstance(self, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DisableCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsInTransaction(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def IsSecurityEnabled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(10)
    def IsCallerInRole(self, bstrRole: win32more.Windows.Win32.Foundation.BSTR, pfIsInRole: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectContextActivity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372afc-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetActivityId(self, pGUID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectContextInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75b52ddb-e8ed-11d1-93ad-00aa00ba3258}')
    @commethod(3)
    def IsInTransaction(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def GetTransaction(self, pptrans: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransactionId(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetActivityId(self, pGUID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetContextId(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectContextInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.IObjectContextInfo
    _iid_ = Guid('{594be71a-4bc4-438b-9197-cfd176248b09}')
    @commethod(8)
    def GetPartitionId(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetApplicationId(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetApplicationInstanceId(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectContextTip(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92fd41ca-bad9-11d2-9a2d-00c04f797bc9}')
    @commethod(3)
    def GetTipUrl(self, pTipUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aec-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def Activate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> Void: ...
    @commethod(5)
    def CanBePooled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IPlaybackControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372afd-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def FinalClientRetry(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FinalServerRetry(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPoolManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0a469861-5a91-43a0-99b6-d5e179bb0631}')
    @commethod(7)
    def ShutdownPool(self, CLSIDOrProgID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProcessInitializer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1113f52d-dc7f-4943-aed6-88d04027e32a}')
    @commethod(3)
    def Startup(self, punkProcessControl: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityCallContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823e-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, name: win32more.Windows.Win32.Foundation.BSTR, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsCallerInRole(self, bstrRole: win32more.Windows.Win32.Foundation.BSTR, pfInRole: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsSecurityEnabled(self, pfIsEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsUserInRole(self, pUser: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrRole: win32more.Windows.Win32.Foundation.BSTR, pfInRole: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityCallersColl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823d-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, lIndex: Int32, pObj: POINTER(win32more.Windows.Win32.System.ComponentServices.ISecurityIdentityColl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityIdentityColl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cafc823c-b441-11d1-b82b-0000f8757e2a}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, name: win32more.Windows.Win32.Foundation.BSTR, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISecurityProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372aea-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetDirectCreatorSID(self, pSID: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginalCreatorSID(self, pSID: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDirectCallerSID(self, pSID: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOriginalCallerSID(self, pSID: POINTER(win32more.Windows.Win32.Security.PSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseSID(self, pSID: win32more.Windows.Win32.Security.PSID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISelectCOMLBServer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcf443f4-3f8a-4872-b9f0-369a796d12d6}')
    @commethod(3)
    def Init(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLBServer(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISendMethodEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2732fd59-b2b4-4d44-878c-8b8f09626008}')
    @commethod(3)
    def SendMethodCall(self, pIdentity: VoidPtr, riid: POINTER(Guid), dwMeth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendMethodReturn(self, pIdentity: VoidPtr, riid: POINTER(Guid), dwMeth: UInt32, hrCall: win32more.Windows.Win32.Foundation.HRESULT, hrServer: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceActivity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{67532e0c-9e2f-4450-a354-035633944e17}')
    @commethod(3)
    def SynchronousCall(self, pIServiceCall: win32more.Windows.Win32.System.ComponentServices.IServiceCall) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AsynchronousCall(self, pIServiceCall: win32more.Windows.Win32.System.ComponentServices.IServiceCall) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BindToCurrentThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnbindFromThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceCall(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bd3e2e12-42dd-40f4-a09a-95a50c58304b}')
    @commethod(3)
    def OnCall(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceComTIIntrinsicsConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09e6831e-04e1-4ed4-9d0f-e8b168bafeaf}')
    @commethod(3)
    def ComTIIntrinsicsConfig(self, comtiIntrinsicsConfig: win32more.Windows.Win32.System.ComponentServices.CSC_COMTIIntrinsicsConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceIISIntrinsicsConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a0cf920-d452-46f4-bc36-48118d54ea52}')
    @commethod(3)
    def IISIntrinsicsConfig(self, iisIntrinsicsConfig: win32more.Windows.Win32.System.ComponentServices.CSC_IISIntrinsicsConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceInheritanceConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92186771-d3b4-4d77-a8ea-ee842d586f35}')
    @commethod(3)
    def ContainingContextTreatment(self, inheritanceConfig: win32more.Windows.Win32.System.ComponentServices.CSC_InheritanceConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServicePartitionConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{80182d03-5ea4-4831-ae97-55beffc2e590}')
    @commethod(3)
    def PartitionConfig(self, partitionConfig: win32more.Windows.Win32.System.ComponentServices.CSC_PartitionConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PartitionID(self, guidPartitionID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServicePool(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b302df81-ea45-451e-99a2-09f9fd1b1e13}')
    @commethod(3)
    def Initialize(self, pPoolConfig: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServicePoolConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9690656-5bca-470c-8451-250c1f43a33e}')
    @commethod(3)
    def put_MaxPoolSize(self, dwMaxPool: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_MaxPoolSize(self, pdwMaxPool: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def put_MinPoolSize(self, dwMinPool: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_MinPoolSize(self, pdwMinPool: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_CreationTimeout(self, dwCreationTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CreationTimeout(self, pdwCreationTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_TransactionAffinity(self, fTxAffinity: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_TransactionAffinity(self, pfTxAffinity: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ClassFactory(self, pFactory: win32more.Windows.Win32.System.Com.IClassFactory) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClassFactory(self, pFactory: POINTER(win32more.Windows.Win32.System.Com.IClassFactory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceSxsConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7cd7379-f3f2-4634-811b-703281d73e08}')
    @commethod(3)
    def SxsConfig(self, scsConfig: win32more.Windows.Win32.System.ComponentServices.CSC_SxsConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SxsName(self, szSxsName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SxsDirectory(self, szSxsDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceSynchronizationConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd880e81-6dce-4c58-af83-a208846c0030}')
    @commethod(3)
    def ConfigureSynchronization(self, synchConfig: win32more.Windows.Win32.System.ComponentServices.CSC_SynchronizationConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceSysTxnConfig(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.IServiceTransactionConfig
    _iid_ = Guid('{33caf1a1-fcb8-472b-b45e-967448ded6d8}')
    @commethod(9)
    def ConfigureBYOTSysTxn(self, pTxProxy: win32more.Windows.Win32.System.ComponentServices.ITransactionProxy) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceThreadPoolConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{186d89bc-f277-4bcc-80d5-4df7b836ef4a}')
    @commethod(3)
    def SelectThreadPool(self, threadPool: win32more.Windows.Win32.System.ComponentServices.CSC_ThreadPool) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBindingInfo(self, binding: win32more.Windows.Win32.System.ComponentServices.CSC_Binding) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceTrackerConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c3a3e1d-0ba6-4036-b76f-d0404db816c9}')
    @commethod(3)
    def TrackerConfig(self, trackerConfig: win32more.Windows.Win32.System.ComponentServices.CSC_TrackerConfig, szTrackerAppName: win32more.Windows.Win32.Foundation.PWSTR, szTrackerCtxName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceTransactionConfig(ComPtr):
    extends: win32more.Windows.Win32.System.ComponentServices.IServiceTransactionConfigBase
    _iid_ = Guid('{59f4c2a3-d3d7-4a31-b6e4-6ab3177c50b9}')
    @commethod(8)
    def ConfigureBYOT(self, pITxByot: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServiceTransactionConfigBase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{772b3fbe-6ffd-42fb-b5f8-8f9b260f3810}')
    @commethod(3)
    def ConfigureTransaction(self, transactionConfig: win32more.Windows.Win32.System.ComponentServices.CSC_TransactionConfig) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsolationLevel(self, option: win32more.Windows.Win32.System.ComponentServices.COMAdminTxIsolationLevelOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransactionTimeout(self, ulTimeoutSec: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BringYourOwnTransaction(self, szTipURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NewTransactionDescription(self, szTxDesc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISharedProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c01-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def get_Value(self, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, val: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISharedPropertyGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c07-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def CreatePropertyByPosition(self, Index: Int32, fExists: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppProp: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PropertyByPosition(self, Index: Int32, ppProperty: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateProperty(self, Name: win32more.Windows.Win32.Foundation.BSTR, fExists: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppProp: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Property(self, Name: win32more.Windows.Win32.Foundation.BSTR, ppProperty: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISharedPropertyGroupManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2a005c0d-a5de-11cf-9e66-00aa00a3f464}')
    @commethod(7)
    def CreatePropertyGroup(self, Name: win32more.Windows.Win32.Foundation.BSTR, dwIsoMode: POINTER(Int32), dwRelMode: POINTER(Int32), fExists: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppGroup: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedPropertyGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Group(self, Name: win32more.Windows.Win32.Foundation.BSTR, ppGroup: POINTER(win32more.Windows.Win32.System.ComponentServices.ISharedPropertyGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISystemAppEventData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6d48a3c-d5c5-49e7-8c74-99e4889ed52f}')
    @commethod(3)
    def Startup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataChanged(self, dwPID: UInt32, dwMask: UInt32, dwNumberSinks: UInt32, bstrDwMethodMask: win32more.Windows.Win32.Foundation.BSTR, dwReason: UInt32, u64TraceHandle: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThreadPoolKnobs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51372af7-cae7-11cf-be81-00aa00a2fa25}')
    @commethod(3)
    def GetMaxThreads(self, plcMaxThreads: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentThreads(self, plcCurrentThreads: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreads(self, lcMaxThreads: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDeleteDelay(self, pmsecDeleteDelay: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDeleteDelay(self, msecDeleteDelay: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxQueuedRequests(self, plcMaxQueuedRequests: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentQueuedRequests(self, plcCurrentQueuedRequests: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMaxQueuedRequests(self, lcMaxQueuedRequests: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMinThreads(self, lcMinThreads: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetQueueDepth(self, lcQueueDepth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7999fc21-d3c6-11cf-acab-00a024a55aef}')
    @commethod(7)
    def CreateInstance(self, pszProgId: win32more.Windows.Win32.Foundation.BSTR, pObject: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionContextEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7999fc22-d3c6-11cf-acab-00a024a55aef}')
    @commethod(3)
    def CreateInstance(self, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
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
    def GetTransactionResourcePool(self, ppTxPool: POINTER(win32more.Windows.Win32.System.ComponentServices.ITransactionResourcePool)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02558374-df2e-4dae-bd6b-1d5c994f9bdc}')
    @commethod(3)
    def Commit(self, guid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Promote(self, pTransaction: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransaction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateVoter(self, pTxAsync: win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2, ppBallot: POINTER(win32more.Windows.Win32.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIsolationLevel(self, __MIDL__ITransactionProxy0000: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIdentifier(self, pbstrIdentifier: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsReusable(self, pfIsReusable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionResourcePool(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5feb7c1-346a-11d1-b1cc-00aa00ba3258}')
    @commethod(3)
    def PutResource(self, pPool: win32more.Windows.Win32.System.ComponentServices.IObjPool, pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(self, pPool: win32more.Windows.Win32.System.ComponentServices.IObjPool, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransactionStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61f589e8-3724-4898-a0a4-664ae9e1d1b4}')
    @commethod(3)
    def SetTransactionStatus(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionStatus(self, pHrStatus: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITxProxyHolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13d86f31-0139-41af-bcad-c7d50435fe9f}')
    @commethod(3)
    def GetIdentifier(self, pGuidLtx: POINTER(Guid)) -> Void: ...
LBEvents = Guid('{ecabb0c1-7f19-11d2-978e-0000f8757e2a}')
LockModes = Int32
LockSetGet: win32more.Windows.Win32.System.ComponentServices.LockModes = 0
LockMethod: win32more.Windows.Win32.System.ComponentServices.LockModes = 1
MessageMover = Guid('{ecabb0bf-7f19-11d2-978e-0000f8757e2a}')
MtsGrp = Guid('{4b2e958d-0393-11d1-b1ab-00aa00ba3258}')
class ObjectContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{74c08646-cedb-11cf-8b49-00aa00b8a790}')
    @commethod(7)
    def CreateInstance(self, bstrProgID: win32more.Windows.Win32.Foundation.BSTR, pObject: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisableCommit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsInTransaction(self, pbIsInTx: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsSecurityEnabled(self, pbIsEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsCallerInRole(self, bstrRole: win32more.Windows.Win32.Foundation.BSTR, pbInRole: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Item(self, name: win32more.Windows.Win32.Foundation.BSTR, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get__NewEnum(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Security(self, ppSecurityProperty: POINTER(win32more.Windows.Win32.System.ComponentServices.SecurityProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ContextInfo(self, ppContextInfo: POINTER(win32more.Windows.Win32.System.ComponentServices.ContextInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ObjectControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7dc41850-0c31-11d0-8b79-00aa00b8a790}')
    @commethod(3)
    def Activate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CanBePooled(self, pbPoolable: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PoolMgr = Guid('{ecabafb5-7f19-11d2-978e-0000f8757e2a}')
class RECYCLE_INFO(Structure):
    guidCombaseProcessIdentifier: Guid
    ProcessStartTime: Int64
    dwRecycleLifetimeLimit: UInt32
    dwRecycleMemoryLimit: UInt32
    dwRecycleExpirationTimeout: UInt32
ReleaseModes = Int32
Standard: win32more.Windows.Win32.System.ComponentServices.ReleaseModes = 0
Process: win32more.Windows.Win32.System.ComponentServices.ReleaseModes = 1
SecurityCallContext = Guid('{ecabb0a7-7f19-11d2-978e-0000f8757e2a}')
SecurityCallers = Guid('{ecabb0a6-7f19-11d2-978e-0000f8757e2a}')
SecurityIdentity = Guid('{ecabb0a5-7f19-11d2-978e-0000f8757e2a}')
class SecurityProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e74a7215-014d-11d1-a63c-00a0c911b4e0}')
    @commethod(7)
    def GetDirectCallerName(self, bstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDirectCreatorName(self, bstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOriginalCallerName(self, bstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOriginalCreatorName(self, bstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ServicePool = Guid('{ecabb0c9-7f19-11d2-978e-0000f8757e2a}')
ServicePoolConfig = Guid('{ecabb0ca-7f19-11d2-978e-0000f8757e2a}')
SharedProperty = Guid('{2a005c05-a5de-11cf-9e66-00aa00a3f464}')
SharedPropertyGroup = Guid('{2a005c0b-a5de-11cf-9e66-00aa00a3f464}')
SharedPropertyGroupManager = Guid('{2a005c11-a5de-11cf-9e66-00aa00a3f464}')
TRACKING_COLL_TYPE = Int32
TRKCOLL_PROCESSES: win32more.Windows.Win32.System.ComponentServices.TRACKING_COLL_TYPE = 0
TRKCOLL_APPLICATIONS: win32more.Windows.Win32.System.ComponentServices.TRACKING_COLL_TYPE = 1
TRKCOLL_COMPONENTS: win32more.Windows.Win32.System.ComponentServices.TRACKING_COLL_TYPE = 2
TrackerServer = Guid('{ecabafb9-7f19-11d2-978e-0000f8757e2a}')
TransactionContext = Guid('{7999fc25-d3c6-11cf-acab-00a024a55aef}')
TransactionContextEx = Guid('{5cb66670-d3d4-11cf-acab-00a024a55aef}')
TransactionVote = Int32
TxCommit: win32more.Windows.Win32.System.ComponentServices.TransactionVote = 0
TxAbort: win32more.Windows.Win32.System.ComponentServices.TransactionVote = 1


make_ready(__name__)
