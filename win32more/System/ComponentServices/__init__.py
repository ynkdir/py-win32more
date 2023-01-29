from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.ComponentServices
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
def CoGetDefaultContext(aptType: win32more.System.Com.APTTYPE, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoCreateActivity(pIUnknown: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoEnterServiceDomain(pConfigObject: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def CoLeaveServiceDomain(pUnkStatus: win32more.System.Com.IUnknown_head) -> Void: ...
@winfunctype('comsvcs.dll')
def GetManagedExtensions(dwExts: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@cfunctype('comsvcs.dll')
def SafeRef(rid: POINTER(Guid), pUnk: win32more.System.Com.IUnknown_head) -> c_void_p: ...
@cfunctype('comsvcs.dll')
def RecycleSurrogate(lReasonCode: Int32) -> win32more.Foundation.HRESULT: ...
@winfunctype('comsvcs.dll')
def MTSCreateActivity(riid: POINTER(Guid), ppobj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('MTxDM.dll')
def GetDispenserManager(param0: POINTER(win32more.System.ComponentServices.IDispenserManager_head)) -> win32more.Foundation.HRESULT: ...
class APPDATA(Structure):
    m_idApp: UInt32
    m_szAppGuid: Char * 40
    m_dwAppProcessId: UInt32
    m_AppStatistics: win32more.System.ComponentServices.APPSTATISTICS
AppDomainHelper = Guid('ef24f689-14f8-4d92-b4-af-d7-b1-f0-e7-0f-d4')
class ApplicationProcessRecycleInfo(Structure):
    IsRecyclable: win32more.Foundation.BOOL
    IsRecycled: win32more.Foundation.BOOL
    TimeRecycled: win32more.Foundation.FILETIME
    TimeToTerminate: win32more.Foundation.FILETIME
    RecycleReasonCode: Int32
    IsPendingRecycle: win32more.Foundation.BOOL
    HasAutomaticLifetimeRecycling: win32more.Foundation.BOOL
    TimeForAutomaticRecycling: win32more.Foundation.FILETIME
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
    Type: win32more.System.ComponentServices.COMPLUS_APPTYPE
    ProcessExeName: win32more.Foundation.PWSTR
    IsService: win32more.Foundation.BOOL
    IsPaused: win32more.Foundation.BOOL
    IsRecycled: win32more.Foundation.BOOL
class ApplicationSummary(Structure):
    ApplicationInstanceId: Guid
    PartitionId: Guid
    ApplicationId: Guid
    Type: win32more.System.ComponentServices.COMPLUS_APPTYPE
    ApplicationName: win32more.Foundation.PWSTR
    NumTrackedComponents: UInt32
    NumComponentInstances: UInt32
class APPSTATISTICS(Structure):
    m_cTotalCalls: UInt32
    m_cTotalInstances: UInt32
    m_cTotalClasses: UInt32
    m_cCallsPerSecond: UInt32
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
ByotServerEx = Guid('ecabb0aa-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
ClrAssemblyLocator = Guid('458aa3b5-265a-4b75-bc-05-9b-ea-46-30-cf-18')
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
    m_pwszAppName: win32more.Foundation.PWSTR
    m_pwszCtxName: win32more.Foundation.PWSTR
    m_eAppType: win32more.System.ComponentServices.COMPLUS_APPTYPE
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
COMAdminCatalog = Guid('f618c514-dfb8-11d1-a2-cf-00-80-5f-c7-92-35')
COMAdminCatalogCollection = Guid('f618c516-dfb8-11d1-a2-cf-00-80-5f-c7-92-35')
COMAdminCatalogObject = Guid('f618c515-dfb8-11d1-a2-cf-00-80-5f-c7-92-35')
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
COMEvents = Guid('ecabb0ab-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
COMPLUS_APPTYPE = Int32
APPTYPE_UNKNOWN: COMPLUS_APPTYPE = -1
APPTYPE_SERVER: COMPLUS_APPTYPE = 1
APPTYPE_LIBRARY: COMPLUS_APPTYPE = 0
APPTYPE_SWC: COMPLUS_APPTYPE = 2
class ComponentHangMonitorInfo(Structure):
    IsMonitored: win32more.Foundation.BOOL
    TerminateOnHang: win32more.Foundation.BOOL
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
    ClassName: win32more.Foundation.PWSTR
    ApplicationName: win32more.Foundation.PWSTR
ComServiceEvents = Guid('ecabb0c3-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
class COMSVCSEVENTINFO(Structure):
    cbSize: UInt32
    dwPid: UInt32
    lTime: Int64
    lMicroTime: Int32
    perfCount: Int64
    guidApp: Guid
    sMachineName: win32more.Foundation.PWSTR
ComSystemAppEventData = Guid('ecabb0c6-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
CoMTSLocator = Guid('ecabb0ac-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
class ContextInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('19a5a02c-0ac8-11d2-b2-86-00-c0-4f-8e-f9-34')
    @commethod(7)
    def IsInTransaction(pbIsInTx: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransaction(ppTx: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransactionId(pbstrTxId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityId(pbstrActivityId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetContextId(pbstrCtxId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ContextInfo2(c_void_p):
    extends: win32more.System.ComponentServices.ContextInfo
    Guid = Guid('c99d6e75-2375-11d4-83-31-00-c0-4f-60-55-88')
    @commethod(12)
    def GetPartitionId(__MIDL__ContextInfo20000: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetApplicationId(__MIDL__ContextInfo20001: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetApplicationInstanceId(__MIDL__ContextInfo20002: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
CRMClerk = Guid('ecabb0bd-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
CRMFLAGS = Int32
CRMFLAG_FORGETTARGET: CRMFLAGS = 1
CRMFLAG_WRITTENDURINGPREPARE: CRMFLAGS = 2
CRMFLAG_WRITTENDURINGCOMMIT: CRMFLAGS = 4
CRMFLAG_WRITTENDURINGABORT: CRMFLAGS = 8
CRMFLAG_WRITTENDURINGRECOVERY: CRMFLAGS = 16
CRMFLAG_WRITTENDURINGREPLAY: CRMFLAGS = 32
CRMFLAG_REPLAYINPROGRESS: CRMFLAGS = 64
class CrmLogRecordRead(Structure):
    dwCrmFlags: UInt32
    dwSequenceNumber: UInt32
    blobUserData: win32more.System.Com.BLOB
CRMRecoveryClerk = Guid('ecabb0be-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
CRMREGFLAGS = Int32
CRMREGFLAG_PREPAREPHASE: CRMREGFLAGS = 1
CRMREGFLAG_COMMITPHASE: CRMREGFLAGS = 2
CRMREGFLAG_ABORTPHASE: CRMREGFLAGS = 4
CRMREGFLAG_ALLPHASES: CRMREGFLAGS = 7
CRMREGFLAG_FAILIFINDOUBTSREMAIN: CRMREGFLAGS = 16
CrmTransactionState = Int32
TxState_Active: CrmTransactionState = 0
TxState_Committed: CrmTransactionState = 1
TxState_Aborted: CrmTransactionState = 2
TxState_Indoubt: CrmTransactionState = 3
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
CServiceConfig = Guid('ecabb0c8-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
DispenserManager = Guid('ecabb0c0-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
Dummy30040732 = Guid('ecabb0a9-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
DUMPTYPE = Int32
DUMPTYPE_FULL: DUMPTYPE = 0
DUMPTYPE_MINI: DUMPTYPE = 1
DUMPTYPE_NONE: DUMPTYPE = 2
EventServer = Guid('ecabafbc-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
GetAppTrackerDataFlags = Int32
GATD_INCLUDE_PROCESS_EXE_NAME: GetAppTrackerDataFlags = 1
GATD_INCLUDE_LIBRARY_APPS: GetAppTrackerDataFlags = 2
GATD_INCLUDE_SWC: GetAppTrackerDataFlags = 4
GATD_INCLUDE_CLASS_NAME: GetAppTrackerDataFlags = 8
GATD_INCLUDE_APPLICATION_NAME: GetAppTrackerDataFlags = 16
GetSecurityCallContextAppObject = Guid('ecabb0a8-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
class HANG_INFO(Structure):
    fAppHangMonitorEnabled: win32more.Foundation.BOOL
    fTerminateOnHang: win32more.Foundation.BOOL
    DumpType: win32more.System.ComponentServices.DUMPTYPE
    dwHangTimeout: UInt32
    dwDumpCount: UInt32
    dwInfoMsgCount: UInt32
class IAppDomainHelper(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c7b67079-8255-42c6-9e-c0-69-94-a3-54-87-80')
    @commethod(7)
    def Initialize(pUnkAD: win32more.System.Com.IUnknown_head, __MIDL__IAppDomainHelper0000: IntPtr, pPool: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DoCallback(pUnkAD: win32more.System.Com.IUnknown_head, __MIDL__IAppDomainHelper0001: IntPtr, pPool: c_void_p) -> win32more.Foundation.HRESULT: ...
class IAssemblyLocator(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('391ffbb9-a8ee-432a-ab-c8-ba-a2-38-da-b9-0f')
    @commethod(7)
    def GetModules(applicationDir: win32more.Foundation.BSTR, applicationName: win32more.Foundation.BSTR, assemblyName: win32more.Foundation.BSTR, pModules: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IAsyncErrorNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fe6777fb-a674-4177-8f-32-6d-70-7e-11-34-84')
    @commethod(3)
    def OnError(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class ICatalogCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6eb22872-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def get__NewEnum(ppEnumVariant: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lIndex: Int32, ppCatalogObject: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(plObjectCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(lIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Add(ppCatalogObject: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Populate() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SaveChanges(pcChanges: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetCollection(bstrCollName: win32more.Foundation.BSTR, varObjectKey: win32more.System.Com.VARIANT, ppCatalogCollection: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Name(pVarNamel: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_AddEnabled(pVarBool: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoveEnabled(pVarBool: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetUtilInterface(ppIDispatch: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_DataStoreMajorVersion(plMajorVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_DataStoreMinorVersion(plMinorVersionl: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def PopulateByKey(psaKeys: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def PopulateByQuery(bstrQueryString: win32more.Foundation.BSTR, lQueryType: Int32) -> win32more.Foundation.HRESULT: ...
class ICatalogObject(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6eb22871-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def get_Value(bstrPropName: win32more.Foundation.BSTR, pvarRetVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(bstrPropName: win32more.Foundation.BSTR, val: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Key(pvarRetVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Name(pvarRetVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsPropertyReadOnly(bstrPropName: win32more.Foundation.BSTR, pbRetVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Valid(pbRetVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def IsPropertyWriteOnly(bstrPropName: win32more.Foundation.BSTR, pbRetVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class ICheckSxsConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0ff5a96f-11fc-47d1-ba-a6-25-dd-34-7e-72-42')
    @commethod(3)
    def IsSameSxsConfig(wszSxsName: win32more.Foundation.PWSTR, wszSxsDirectory: win32more.Foundation.PWSTR, wszSxsAppName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IComActivityEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b0-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnActivityCreate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnActivityDestroy(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnActivityEnter(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnActivityTimeout(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidEntered: POINTER(Guid), dwThread: UInt32, dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnActivityReenter(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), dwThread: UInt32, dwCallDepth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnActivityLeave(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), guidLeft: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnActivityLeaveSame(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidCurrent: POINTER(Guid), dwCallDepth: UInt32) -> win32more.Foundation.HRESULT: ...
class ICOMAdminCatalog(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dd662187-dfc2-11d1-a2-cf-00-80-5f-c7-92-35')
    @commethod(7)
    def GetCollection(bstrCollName: win32more.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Connect(bstrCatalogServerName: win32more.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_MajorVersion(plMajorVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MinorVersion(plMinorVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCollectionByQuery(bstrCollName: win32more.Foundation.BSTR, ppsaVarQuery: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppCatalogCollection: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ImportComponent(bstrApplIDOrName: win32more.Foundation.BSTR, bstrCLSIDOrProgID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def InstallComponent(bstrApplIDOrName: win32more.Foundation.BSTR, bstrDLL: win32more.Foundation.BSTR, bstrTLB: win32more.Foundation.BSTR, bstrPSDLL: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ShutdownApplication(bstrApplIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ExportApplication(bstrApplIDOrName: win32more.Foundation.BSTR, bstrApplicationFile: win32more.Foundation.BSTR, lOptions: win32more.System.ComponentServices.COMAdminApplicationExportOptions) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def InstallApplication(bstrApplicationFile: win32more.Foundation.BSTR, bstrDestinationDirectory: win32more.Foundation.BSTR, lOptions: win32more.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserId: win32more.Foundation.BSTR, bstrPassword: win32more.Foundation.BSTR, bstrRSN: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def StopRouter() -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RefreshRouter() -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def StartRouter() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Reserved1() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Reserved2() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def InstallMultipleComponents(bstrApplIDOrName: win32more.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarCLSIDs: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetMultipleComponentsInfo(bstrApplIdOrName: win32more.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarCLSIDs: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarClassNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarFileFlags: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarComponentFlags: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def RefreshComponents() -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def BackupREGDB(bstrBackupFilePath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def RestoreREGDB(bstrBackupFilePath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def QueryApplicationFile(bstrApplicationFile: win32more.Foundation.BSTR, pbstrApplicationName: POINTER(win32more.Foundation.BSTR), pbstrApplicationDescription: POINTER(win32more.Foundation.BSTR), pbHasUsers: POINTER(win32more.Foundation.VARIANT_BOOL), pbIsProxy: POINTER(win32more.Foundation.VARIANT_BOOL), ppsaVarFileNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def StartApplication(bstrApplIdOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def ServiceCheck(lService: Int32, plStatus: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def InstallMultipleEventClasses(bstrApplIdOrName: win32more.Foundation.BSTR, ppsaVarFileNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarCLSIDS: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def InstallEventClass(bstrApplIdOrName: win32more.Foundation.BSTR, bstrDLL: win32more.Foundation.BSTR, bstrTLB: win32more.Foundation.BSTR, bstrPSDLL: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetEventClassesForIID(bstrIID: win32more.Foundation.BSTR, ppsaVarCLSIDs: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarProgIDs: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), ppsaVarDescriptions: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class ICOMAdminCatalog2(c_void_p):
    extends: win32more.System.ComponentServices.ICOMAdminCatalog
    Guid = Guid('790c6e0b-9194-4cc9-94-26-a4-8a-63-18-56-96')
    @commethod(33)
    def GetCollectionByQuery2(bstrCollectionName: win32more.Foundation.BSTR, pVarQueryStrings: POINTER(win32more.System.Com.VARIANT_head), ppCatalogCollection: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetApplicationInstanceIDFromProcessID(lProcessID: Int32, pbstrApplicationInstanceID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def ShutdownApplicationInstances(pVarApplicationInstanceID: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def PauseApplicationInstances(pVarApplicationInstanceID: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def ResumeApplicationInstances(pVarApplicationInstanceID: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def RecycleApplicationInstances(pVarApplicationInstanceID: POINTER(win32more.System.Com.VARIANT_head), lReasonCode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def AreApplicationInstancesPaused(pVarApplicationInstanceID: POINTER(win32more.System.Com.VARIANT_head), pVarBoolPaused: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def DumpApplicationInstance(bstrApplicationInstanceID: win32more.Foundation.BSTR, bstrDirectory: win32more.Foundation.BSTR, lMaxImages: Int32, pbstrDumpFile: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsApplicationInstanceDumpSupported(pVarBoolDumpSupported: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def CreateServiceForApplication(bstrApplicationIDOrName: win32more.Foundation.BSTR, bstrServiceName: win32more.Foundation.BSTR, bstrStartType: win32more.Foundation.BSTR, bstrErrorControl: win32more.Foundation.BSTR, bstrDependencies: win32more.Foundation.BSTR, bstrRunAs: win32more.Foundation.BSTR, bstrPassword: win32more.Foundation.BSTR, bDesktopOk: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def DeleteServiceForApplication(bstrApplicationIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetPartitionID(bstrApplicationIDOrName: win32more.Foundation.BSTR, pbstrPartitionID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def GetPartitionName(bstrApplicationIDOrName: win32more.Foundation.BSTR, pbstrPartitionName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def put_CurrentPartition(bstrPartitionIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def get_CurrentPartitionID(pbstrPartitionID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def get_CurrentPartitionName(pbstrPartitionName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_GlobalPartitionID(pbstrGlobalPartitionID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def FlushPartitionCache() -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def CopyApplications(bstrSourcePartitionIDOrName: win32more.Foundation.BSTR, pVarApplicationID: POINTER(win32more.System.Com.VARIANT_head), bstrDestinationPartitionIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def CopyComponents(bstrSourceApplicationIDOrName: win32more.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.System.Com.VARIANT_head), bstrDestinationApplicationIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def MoveComponents(bstrSourceApplicationIDOrName: win32more.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.System.Com.VARIANT_head), bstrDestinationApplicationIDOrName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def AliasComponent(bstrSrcApplicationIDOrName: win32more.Foundation.BSTR, bstrCLSIDOrProgID: win32more.Foundation.BSTR, bstrDestApplicationIDOrName: win32more.Foundation.BSTR, bstrNewProgId: win32more.Foundation.BSTR, bstrNewClsid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def IsSafeToDelete(bstrDllName: win32more.Foundation.BSTR, pCOMAdminInUse: POINTER(win32more.System.ComponentServices.COMAdminInUse)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def ImportUnconfiguredComponents(bstrApplicationIDOrName: win32more.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.System.Com.VARIANT_head), pVarComponentType: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def PromoteUnconfiguredComponents(bstrApplicationIDOrName: win32more.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.System.Com.VARIANT_head), pVarComponentType: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def ImportComponents(bstrApplicationIDOrName: win32more.Foundation.BSTR, pVarCLSIDOrProgID: POINTER(win32more.System.Com.VARIANT_head), pVarComponentType: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def get_Is64BitCatalogServer(pbIs64Bit: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def ExportPartition(bstrPartitionIDOrName: win32more.Foundation.BSTR, bstrPartitionFileName: win32more.Foundation.BSTR, lOptions: win32more.System.ComponentServices.COMAdminApplicationExportOptions) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def InstallPartition(bstrFileName: win32more.Foundation.BSTR, bstrDestDirectory: win32more.Foundation.BSTR, lOptions: win32more.System.ComponentServices.COMAdminApplicationInstallOptions, bstrUserID: win32more.Foundation.BSTR, bstrPassword: win32more.Foundation.BSTR, bstrRSN: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def QueryApplicationFile2(bstrApplicationFile: win32more.Foundation.BSTR, ppFilesForImport: POINTER(win32more.System.Com.IDispatch_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def GetComponentVersionCount(bstrCLSIDOrProgID: win32more.Foundation.BSTR, plVersionCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IComApp2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1290bc1a-b219-418d-b0-78-59-34-de-d0-82-42')
    @commethod(3)
    def OnAppActivation2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, guidProcess: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnAppPaused2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, bPaused: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnAppRecycle2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid, guidProcess: Guid, lReason: Int32) -> win32more.Foundation.HRESULT: ...
class IComAppEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a6-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnAppActivation(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnAppShutdown(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnAppForceShutdown(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
class IComCRMEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b5-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnCRMRecoveryStart(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnCRMRecoveryDone(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnCRMCheckpoint(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidApp: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnCRMBegin(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, guidActivity: Guid, guidTx: Guid, szProgIdCompensator: win32more.Foundation.PWSTR, szDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnCRMPrepare(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnCRMCommit(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnCRMAbort(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnCRMIndoubt(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def OnCRMDone(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OnCRMRelease(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def OnCRMAnalyze(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, dwCrmRecordType: UInt32, dwRecordSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def OnCRMWrite(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, fVariants: win32more.Foundation.BOOL, dwRecordSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def OnCRMForget(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def OnCRMForce(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def OnCRMDeliver(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidClerkCLSID: Guid, fVariants: win32more.Foundation.BOOL, dwRecordSize: UInt32) -> win32more.Foundation.HRESULT: ...
class IComExceptionEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b3-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnExceptionUser(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), code: UInt32, address: UInt64, pszStackTrace: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IComIdentityEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b1-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnIISRequestInfo(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjId: UInt64, pszClientIP: win32more.Foundation.PWSTR, pszServerIP: win32more.Foundation.PWSTR, pszURL: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IComInstance2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('20e3bf07-b506-4ad5-a5-0c-d2-ca-5b-9c-15-8e')
    @commethod(3)
    def OnObjectCreate2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64, guidPartition: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
class IComInstanceEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a7-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnObjectCreate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), clsid: POINTER(Guid), tsid: POINTER(Guid), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDestroy(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
class ICOMLBArguments(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3a0f150f-8ee5-4b94-b4-0e-ae-f2-f9-e4-2e-d2')
    @commethod(3)
    def GetCLSID(pCLSID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetCLSID(pCLSID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMachineName(cchSvr: UInt32, szServerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetMachineName(cchSvr: UInt32, szServerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IComLTxEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('605cf82c-578e-4298-97-5d-82-ba-bc-d9-e0-53')
    @commethod(3)
    def OnLtxTransactionStart(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, tsid: Guid, fRoot: win32more.Foundation.BOOL, nIsolationLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnLtxTransactionPrepare(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, fVote: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnLtxTransactionAbort(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnLtxTransactionCommit(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnLtxTransactionPromote(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidLtx: Guid, txnId: Guid) -> win32more.Foundation.HRESULT: ...
class IComMethod2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fb388aaa-567d-4024-af-8e-6e-93-ee-74-85-73')
    @commethod(3)
    def OnMethodCall2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32, hresult: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), dwThread: UInt32, iMeth: UInt32) -> win32more.Foundation.HRESULT: ...
class IComMethodEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a9-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnMethodCall(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnMethodReturn(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32, hresult: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnMethodException(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), oid: UInt64, guidCid: POINTER(Guid), guidRid: POINTER(Guid), iMeth: UInt32) -> win32more.Foundation.HRESULT: ...
class IComMtaThreadPoolKnobs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9a76d2e-76a5-43eb-a0-c4-49-be-c8-e4-84-80')
    @commethod(3)
    def MTASetMaxThreadCount(dwMaxThreads: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def MTAGetMaxThreadCount(pdwMaxThreads: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MTASetThrottleValue(dwThrottle: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def MTAGetThrottleValue(pdwThrottle: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IComObjectConstruction2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4b5a7827-8df2-45c0-8f-6f-57-ea-1f-85-6a-9f')
    @commethod(3)
    def OnObjectConstruct2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), sConstructString: win32more.Foundation.PWSTR, oid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IComObjectConstructionEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130af-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnObjectConstruct(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), sConstructString: win32more.Foundation.PWSTR, oid: UInt64) -> win32more.Foundation.HRESULT: ...
class IComObjectEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130aa-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnObjectActivate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjectDeactivate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64, ObjectID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnDisableCommit(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnEnableCommit(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnSetComplete(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnSetAbort(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), CtxtID: UInt64) -> win32more.Foundation.HRESULT: ...
class IComObjectPool2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('65bf6534-85ea-4f64-8c-f4-3d-97-4b-2a-b1-cf')
    @commethod(3)
    def OnObjPoolPutObject2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64, guidPartition: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IComObjectPoolEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130ad-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnObjPoolPutObject(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), nReason: Int32, dwAvailable: UInt32, oid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolGetObject(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), dwAvailable: UInt32, oid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolRecycleToTx(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolGetFromTx(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), guidObject: POINTER(Guid), guidTx: POINTER(Guid), objid: UInt64) -> win32more.Foundation.HRESULT: ...
class IComObjectPoolEvents2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130ae-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnObjPoolCreateObject(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnObjPoolDestroyObject(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwObjsCreated: UInt32, oid: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnObjPoolCreateDecision(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), dwThreadsWaiting: UInt32, dwAvail: UInt32, dwCreated: UInt32, dwMin: UInt32, dwMax: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnObjPoolTimeout(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), guidActivity: POINTER(Guid), dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnObjPoolCreatePool(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidObject: POINTER(Guid), dwMin: UInt32, dwMax: UInt32, dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
class IComQCEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b2-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnQCRecord(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), objid: UInt64, szQueue: win32more.Foundation.PWSTR, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), msmqhr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnQCQueueOpen(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), szQueue: win32more.Foundation.PWSTR, QueueID: UInt64, hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnQCReceive(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), QueueID: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnQCReceiveFail(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), QueueID: UInt64, msmqhr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnQCMoveToReTryQueue(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), RetryIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnQCMoveToDeadQueue(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnQCPlayback(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), objid: UInt64, guidMsgId: POINTER(Guid), guidWorkFlowId: POINTER(Guid), hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IComResourceEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130ab-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnResourceCreate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: win32more.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnResourceAllocate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: win32more.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Foundation.BOOL, NumRated: UInt32, Rating: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnResourceRecycle(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: win32more.Foundation.PWSTR, resId: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnResourceDestroy(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, hr: win32more.Foundation.HRESULT, pszType: win32more.Foundation.PWSTR, resId: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnResourceTrack(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ObjectID: UInt64, pszType: win32more.Foundation.PWSTR, resId: UInt64, enlisted: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IComSecurityEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130ac-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnAuthenticate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: c_char_p_no, cbByteCur: UInt32, pSidCurrentUser: c_char_p_no, bCurrentUserInpersonatingInProc: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnAuthenticateFail(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), ObjectID: UInt64, guidIID: POINTER(Guid), iMeth: UInt32, cbByteOrig: UInt32, pSidOriginalUser: c_char_p_no, cbByteCur: UInt32, pSidCurrentUser: c_char_p_no, bCurrentUserInpersonatingInProc: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('324b64fa-33b6-11d2-98-b7-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def SetMinThreadCount(minThreads: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinThreadCount(minThreads: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreadCount(maxThreads: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxThreadCount(maxThreads: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetActivityPerThread(activitiesPerThread: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetActivityPerThread(activitiesPerThread: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetActivityRatio(activityRatio: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetActivityRatio(activityRatio: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetThreadCount(pdwThreads: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetQueueDepth(pdwQDepth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetQueueDepth(dwQDepth: Int32) -> win32more.Foundation.HRESULT: ...
class IComStaThreadPoolKnobs2(c_void_p):
    extends: win32more.System.ComponentServices.IComStaThreadPoolKnobs
    Guid = Guid('73707523-ff9a-4974-bf-84-21-08-dc-21-37-40')
    @commethod(14)
    def GetMaxCPULoad(pdwLoad: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetMaxCPULoad(pdwLoad: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetCPUMetricEnabled(pbMetricEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetCPUMetricEnabled(bMetricEnabled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetCreateThreadsAggressively(pbMetricEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetCreateThreadsAggressively(bMetricEnabled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaxCSR(pdwCSR: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetMaxCSR(dwCSR: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetWaitTimeForThreadCleanup(pdwThreadCleanupWaitTime: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetWaitTimeForThreadCleanup(dwThreadCleanupWaitTime: Int32) -> win32more.Foundation.HRESULT: ...
class IComThreadEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a5-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnThreadStart(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnThreadTerminate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, dwThread: UInt32, dwTheadCnt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadBindToApartment(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32, dwLowCnt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnThreadUnBind(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, AptID: UInt64, dwActCnt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnThreadWorkEnque(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnThreadWorkPrivate(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnThreadWorkPublic(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnThreadWorkRedirect(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32, ThreadNum: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def OnThreadWorkReject(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), ThreadID: UInt64, MsgWorkID: UInt64, QueueLen: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OnThreadAssignApartment(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidActivity: POINTER(Guid), AptID: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def OnThreadUnassignApartment(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), AptID: UInt64) -> win32more.Foundation.HRESULT: ...
class IComTrackingInfoCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c266c677-c9ad-49ab-9f-d9-d9-66-10-78-58-8a')
    @commethod(3)
    def Type(pType: POINTER(win32more.System.ComponentServices.TRACKING_COLL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Count(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Item(ulIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IComTrackingInfoEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4e6cdcc9-fb25-4fd5-9c-c5-c9-f4-b6-55-9c-ec')
    @commethod(3)
    def OnNewTrackingInfo(pToplevelCollection: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IComTrackingInfoObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('116e42c5-d8b1-47bf-ab-1e-c8-95-ed-3e-23-72')
    @commethod(3)
    def GetValue(szPropertyName: win32more.Foundation.PWSTR, pvarOut: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IComTrackingInfoProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('789b42be-6f6b-443a-89-8e-67-ab-f3-90-aa-14')
    @commethod(3)
    def PropCount(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropName(ulIndex: UInt32, ppszPropName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IComTransaction2Events(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a136f62a-2f94-4288-86-e0-d8-a1-fa-4c-02-99')
    @commethod(3)
    def OnTransactionStart2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: win32more.Foundation.BOOL, nIsolationLevel: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), fVoteYes: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit2(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IComTransactionEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a8-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnTransactionStart(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), tsid: POINTER(Guid), fRoot: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnTransactionPrepare(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid), fVoteYes: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnTransactionAbort(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnTransactionCommit(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), guidTx: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IComUserEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130a4-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def OnUserEvent(pInfo: POINTER(win32more.System.ComponentServices.COMSVCSEVENTINFO_head), pvarEvent: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IContextProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d396da85-bf8f-11d1-bb-ae-00-c0-4f-c2-fa-5f')
    @commethod(3)
    def Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(name: win32more.Foundation.BSTR, pProperty: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(ppenum: POINTER(win32more.System.ComponentServices.IEnumNames_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(name: win32more.Foundation.BSTR, property: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProperty(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IContextSecurityPerimeter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a7549a29-a7c4-42e1-8d-c1-7e-3d-74-8d-c2-4a')
    @commethod(3)
    def GetPerimeterFlag(pFlag: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPerimeterFlag(fFlag: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IContextState(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3c05e54b-a42a-11d2-af-c4-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def SetDeactivateOnReturn(bDeactivate: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeactivateOnReturn(pbDeactivate: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetMyTransactionVote(txVote: win32more.System.ComponentServices.TransactionVote) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMyTransactionVote(ptxVote: POINTER(win32more.System.ComponentServices.TransactionVote)) -> win32more.Foundation.HRESULT: ...
class ICreateWithLocalTransaction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('227ac7a8-8423-42ce-b7-cf-03-06-1e-c9-aa-a3')
    @commethod(3)
    def CreateInstanceWithSysTx(pTransaction: win32more.System.Com.IUnknown_head, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ICreateWithTipTransactionEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('455acf59-5345-11d2-99-cf-00-c0-4f-79-7b-c9')
    @commethod(3)
    def CreateInstance(bstrTipUrl: win32more.Foundation.BSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ICreateWithTransactionEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('455acf57-5345-11d2-99-cf-00-c0-4f-79-7b-c9')
    @commethod(3)
    def CreateInstance(pTransaction: win32more.System.DistributedTransactionCoordinator.ITransaction_head, rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ICrmCompensator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bbc01830-8d3b-11d1-82-ec-00-a0-c9-1e-ed-e9')
    @commethod(3)
    def SetLogControl(pLogControl: win32more.System.ComponentServices.ICrmLogControl_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepare() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecord(crmLogRec: win32more.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepare(pfOkToPrepare: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommit(fRecovery: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecord(crmLogRec: win32more.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommit() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbort(fRecovery: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecord(crmLogRec: win32more.System.ComponentServices.CrmLogRecordRead, pfForget: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbort() -> win32more.Foundation.HRESULT: ...
class ICrmCompensatorVariants(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f0baf8e4-7804-11d1-82-e9-00-a0-c9-1e-ed-e9')
    @commethod(3)
    def SetLogControlVariants(pLogControl: win32more.System.ComponentServices.ICrmLogControl_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BeginPrepareVariants() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PrepareRecordVariants(pLogRecord: POINTER(win32more.System.Com.VARIANT_head), pbForget: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EndPrepareVariants(pbOkToPrepare: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCommitVariants(bRecovery: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CommitRecordVariants(pLogRecord: POINTER(win32more.System.Com.VARIANT_head), pbForget: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EndCommitVariants() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def BeginAbortVariants(bRecovery: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AbortRecordVariants(pLogRecord: POINTER(win32more.System.Com.VARIANT_head), pbForget: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EndAbortVariants() -> win32more.Foundation.HRESULT: ...
class ICrmFormatLogRecords(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9c51d821-c98b-11d1-82-fb-00-a0-c9-1e-ed-e9')
    @commethod(3)
    def GetColumnCount(plColumnCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaders(pHeaders: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetColumn(CrmLogRec: win32more.System.ComponentServices.CrmLogRecordRead, pFormattedLogRecord: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnVariants(LogRecord: win32more.System.Com.VARIANT, pFormattedLogRecord: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ICrmLogControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a0e174b3-d26e-11d2-8f-84-00-80-5f-c7-bc-d9')
    @commethod(3)
    def get_TransactionUOW(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCompensator(lpcwstrProgIdCompensator: win32more.Foundation.PWSTR, lpcwstrDescription: win32more.Foundation.PWSTR, lCrmRegFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def WriteLogRecordVariants(pLogRecord: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ForceLog() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ForgetLogRecord() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ForceTransactionToAbort() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def WriteLogRecord(rgBlob: POINTER(win32more.System.Com.BLOB_head), cBlob: UInt32) -> win32more.Foundation.HRESULT: ...
class ICrmMonitor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70c8e443-c7ed-11d1-82-fb-00-a0-c9-1e-ed-e9')
    @commethod(3)
    def GetClerks(pClerks: POINTER(win32more.System.ComponentServices.ICrmMonitorClerks_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def HoldClerk(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ICrmMonitorClerks(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('70c8e442-c7ed-11d1-82-fb-00-a0-c9-1e-ed-e9')
    @commethod(7)
    def Item(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(pVal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ProgIdCompensator(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Description(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def TransactionUOW(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ActivityId(Index: win32more.System.Com.VARIANT, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ICrmMonitorLogRecords(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70c8e441-c7ed-11d1-82-fb-00-a0-c9-1e-ed-e9')
    @commethod(3)
    def get_Count(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_TransactionState(pVal: POINTER(win32more.System.ComponentServices.CrmTransactionState)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_StructuredRecords(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLogRecord(dwIndex: UInt32, pCrmLogRec: POINTER(win32more.System.ComponentServices.CrmLogRecordRead_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLogRecordVariants(IndexNumber: win32more.System.Com.VARIANT, pLogRecord: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IDispenserDriver(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('208b3651-2b48-11cf-be-10-00-aa-00-a2-fa-25')
    @commethod(3)
    def CreateResource(ResTypId: UIntPtr, pResId: POINTER(UIntPtr), pSecsFreeBeforeDestroy: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RateResource(ResTypId: UIntPtr, ResId: UIntPtr, fRequiresTransactionEnlistment: win32more.Foundation.BOOL, pRating: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnlistResource(ResId: UIntPtr, TransId: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ResetResource(ResId: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyResource(ResId: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DestroyResourceS(ResId: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class IDispenserManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5cb31e10-2b5f-11cf-be-10-00-aa-00-a2-fa-25')
    @commethod(3)
    def RegisterDispenser(__MIDL__IDispenserManager0000: win32more.System.ComponentServices.IDispenserDriver_head, szDispenserName: win32more.Foundation.PWSTR, __MIDL__IDispenserManager0001: POINTER(win32more.System.ComponentServices.IHolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetContext(__MIDL__IDispenserManager0002: POINTER(UIntPtr), __MIDL__IDispenserManager0003: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
class IEnumNames(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372af2-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def Next(celt: UInt32, rgname: POINTER(win32more.Foundation.BSTR), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.ComponentServices.IEnumNames_head)) -> win32more.Foundation.HRESULT: ...
class IEventServerTrace(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('9a9f12b8-80af-47ab-a5-79-35-ea-57-72-53-70')
    @commethod(7)
    def StartTraceGuid(bstrguidEvent: win32more.Foundation.BSTR, bstrguidFilter: win32more.Foundation.BSTR, lPidFilter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def StopTraceGuid(bstrguidEvent: win32more.Foundation.BSTR, bstrguidFilter: win32more.Foundation.BSTR, lPidFilter: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumTraceGuid(plCntGuids: POINTER(Int32), pbstrGuidList: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IGetAppTrackerData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('507c3ac8-3e12-4cb0-93-66-65-3d-3e-05-06-38')
    @commethod(3)
    def GetApplicationProcesses(PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumApplicationProcesses: POINTER(UInt32), ApplicationProcesses: POINTER(POINTER(win32more.System.ComponentServices.ApplicationProcessSummary_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplicationProcessDetails(ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Flags: UInt32, Summary: POINTER(win32more.System.ComponentServices.ApplicationProcessSummary_head), Statistics: POINTER(win32more.System.ComponentServices.ApplicationProcessStatistics_head), RecycleInfo: POINTER(win32more.System.ComponentServices.ApplicationProcessRecycleInfo_head), AnyComponentsHangMonitored: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplicationsInProcess(ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), Flags: UInt32, NumApplicationsInProcess: POINTER(UInt32), Applications: POINTER(POINTER(win32more.System.ComponentServices.ApplicationSummary_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentsInProcess(ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, PartitionId: POINTER(Guid), ApplicationId: POINTER(Guid), Flags: UInt32, NumComponentsInProcess: POINTER(UInt32), Components: POINTER(POINTER(win32more.System.ComponentServices.ComponentSummary_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetComponentDetails(ApplicationInstanceId: POINTER(Guid), ProcessId: UInt32, Clsid: POINTER(Guid), Flags: UInt32, Summary: POINTER(win32more.System.ComponentServices.ComponentSummary_head), Statistics: POINTER(win32more.System.ComponentServices.ComponentStatistics_head), HangMonitorInfo: POINTER(win32more.System.ComponentServices.ComponentHangMonitorInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTrackerDataAsCollectionObject(TopLevelCollection: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSuggestedPollingInterval(PollingIntervalInSeconds: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IGetContextProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372af4-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(name: win32more.Foundation.BSTR, pProperty: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumNames(ppenum: POINTER(win32more.System.ComponentServices.IEnumNames_head)) -> win32more.Foundation.HRESULT: ...
class IGetSecurityCallContext(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cafc823f-b441-11d1-b8-2b-00-00-f8-75-7e-2a')
    @commethod(7)
    def GetSecurityCallContext(ppObject: POINTER(win32more.System.ComponentServices.ISecurityCallContext_head)) -> win32more.Foundation.HRESULT: ...
class IHolder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bf6a1850-2b45-11cf-be-10-00-aa-00-a2-fa-25')
    @commethod(3)
    def AllocResource(__MIDL__IHolder0000: UIntPtr, __MIDL__IHolder0001: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FreeResource(__MIDL__IHolder0002: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TrackResource(__MIDL__IHolder0003: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TrackResourceS(__MIDL__IHolder0004: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UntrackResource(__MIDL__IHolder0005: UIntPtr, __MIDL__IHolder0006: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UntrackResourceS(__MIDL__IHolder0007: POINTER(UInt16), __MIDL__IHolder0008: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RequestDestroyResource(__MIDL__IHolder0009: UIntPtr) -> win32more.Foundation.HRESULT: ...
class ILBEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('683130b4-2e50-11d2-98-a5-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def TargetUp(bstrServerName: win32more.Foundation.BSTR, bstrClsidEng: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TargetDown(bstrServerName: win32more.Foundation.BSTR, bstrClsidEng: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EngineDefined(bstrPropName: win32more.Foundation.BSTR, varPropValue: POINTER(win32more.System.Com.VARIANT_head), bstrClsidEng: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IManagedActivationEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a5f325af-572f-46da-b8-ab-82-7c-3d-95-d9-9e')
    @commethod(3)
    def CreateManagedStub(pInfo: win32more.System.ComponentServices.IManagedObjectInfo_head, fDist: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DestroyManagedStub(pInfo: win32more.System.ComponentServices.IManagedObjectInfo_head) -> win32more.Foundation.HRESULT: ...
class IManagedObjectInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1427c51a-4584-49d8-90-a0-c5-0d-80-86-cb-e9')
    @commethod(3)
    def GetIUnknown(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIObjectControl(pCtrl: POINTER(win32more.System.ComponentServices.IObjectControl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetInPool(bInPool: win32more.Foundation.BOOL, pPooledObj: win32more.System.ComponentServices.IManagedPooledObj_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetWrapperStrength(bStrong: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IManagedPoolAction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('da91b74e-5388-4783-94-9d-c1-cd-5f-b0-05-06')
    @commethod(3)
    def LastRelease() -> win32more.Foundation.HRESULT: ...
class IManagedPooledObj(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c5da4bea-1b42-4437-89-26-b6-a3-88-60-a7-70')
    @commethod(3)
    def SetHeld(m_bHeld: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IMessageMover(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('588a085a-b795-11d1-80-54-00-c0-4f-c3-40-ee')
    @commethod(7)
    def get_SourcePath(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_SourcePath(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_DestPath(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_DestPath(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_CommitBatchSize(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_CommitBatchSize(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def MoveMessages(plMessagesMoved: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMTSActivity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372af0-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def SynchronousCall(pCall: win32more.System.ComponentServices.IMTSCall_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AsyncCall(pCall: win32more.System.ComponentServices.IMTSCall_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reserved1() -> Void: ...
    @commethod(6)
    def BindToCurrentThread() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UnbindFromThread() -> win32more.Foundation.HRESULT: ...
class IMTSCall(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372aef-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def OnCall() -> win32more.Foundation.HRESULT: ...
class IMtsEventInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d56c3dc1-8482-11d0-b1-70-00-aa-00-ba-32-58')
    @commethod(7)
    def get_Names(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_DisplayName(sDisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventID(sGuidEventID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(lCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Value(sKey: win32more.Foundation.BSTR, pVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IMtsEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('bacedf4d-74ab-11d0-b1-62-00-aa-00-ba-32-58')
    @commethod(7)
    def get_PackageName(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PackageGuid(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PostEvent(vEvent: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_FireEvents(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetProcessID(id: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMtsGrp(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('4b2e958c-0393-11d1-b1-ab-00-aa-00-ba-32-58')
    @commethod(7)
    def get_Count(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(lIndex: Int32, ppUnkDispatcher: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh() -> win32more.Foundation.HRESULT: ...
class IMTSLocator(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d19b8bfd-7f88-11d0-b1-6e-00-aa-00-ba-32-58')
    @commethod(7)
    def GetEventDispatcher(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IObjectConstruct(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('41c4f8b3-7439-11d2-98-cb-00-c0-4f-8e-e1-c4')
    @commethod(3)
    def Construct(pCtorObj: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class IObjectConstructString(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('41c4f8b2-7439-11d2-98-cb-00-c0-4f-8e-e1-c4')
    @commethod(7)
    def get_ConstructString(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IObjectContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372ae0-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def CreateInstance(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetComplete() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetAbort() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnableCommit() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def DisableCommit() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsInTransaction() -> win32more.Foundation.BOOL: ...
    @commethod(9)
    def IsSecurityEnabled() -> win32more.Foundation.BOOL: ...
    @commethod(10)
    def IsCallerInRole(bstrRole: win32more.Foundation.BSTR, pfIsInRole: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IObjectContextActivity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372afc-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def GetActivityId(pGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IObjectContextInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('75b52ddb-e8ed-11d1-93-ad-00-aa-00-ba-32-58')
    @commethod(3)
    def IsInTransaction() -> win32more.Foundation.BOOL: ...
    @commethod(4)
    def GetTransaction(pptrans: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransactionId(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetActivityId(pGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetContextId(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IObjectContextInfo2(c_void_p):
    extends: win32more.System.ComponentServices.IObjectContextInfo
    Guid = Guid('594be71a-4bc4-438b-91-97-cf-d1-76-24-8b-09')
    @commethod(8)
    def GetPartitionId(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetApplicationId(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetApplicationInstanceId(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IObjectContextTip(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('92fd41ca-bad9-11d2-9a-2d-00-c0-4f-79-7b-c9')
    @commethod(3)
    def GetTipUrl(pTipUrl: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IObjectControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372aec-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def Activate() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate() -> Void: ...
    @commethod(5)
    def CanBePooled() -> win32more.Foundation.BOOL: ...
class IObjPool(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7d8805a0-2ea7-11d1-b1-cc-00-aa-00-ba-32-58')
    @commethod(3)
    def Reserved1() -> Void: ...
    @commethod(4)
    def Reserved2() -> Void: ...
    @commethod(5)
    def Reserved3() -> Void: ...
    @commethod(6)
    def Reserved4() -> Void: ...
    @commethod(7)
    def PutEndTx(pObj: win32more.System.Com.IUnknown_head) -> Void: ...
    @commethod(8)
    def Reserved5() -> Void: ...
    @commethod(9)
    def Reserved6() -> Void: ...
class IPlaybackControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372afd-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def FinalClientRetry() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FinalServerRetry() -> win32more.Foundation.HRESULT: ...
class IPoolManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0a469861-5a91-43a0-99-b6-d5-e1-79-bb-06-31')
    @commethod(7)
    def ShutdownPool(CLSIDOrProgID: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IProcessInitializer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1113f52d-dc7f-4943-ae-d6-88-d0-40-27-e3-2a')
    @commethod(3)
    def Startup(punkProcessControl: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown() -> win32more.Foundation.HRESULT: ...
class ISecurityCallContext(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cafc823e-b441-11d1-b8-2b-00-00-f8-75-7e-2a')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(name: win32more.Foundation.BSTR, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsCallerInRole(bstrRole: win32more.Foundation.BSTR, pfInRole: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsSecurityEnabled(pfIsEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsUserInRole(pUser: POINTER(win32more.System.Com.VARIANT_head), bstrRole: win32more.Foundation.BSTR, pfInRole: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class ISecurityCallersColl(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cafc823d-b441-11d1-b8-2b-00-00-f8-75-7e-2a')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lIndex: Int32, pObj: POINTER(win32more.System.ComponentServices.ISecurityIdentityColl_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ISecurityIdentityColl(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cafc823c-b441-11d1-b8-2b-00-00-f8-75-7e-2a')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(name: win32more.Foundation.BSTR, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ISecurityProperty(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372aea-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def GetDirectCreatorSID(pSID: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOriginalCreatorSID(pSID: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDirectCallerSID(pSID: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetOriginalCallerSID(pSID: POINTER(win32more.Foundation.PSID)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseSID(pSID: win32more.Foundation.PSID) -> win32more.Foundation.HRESULT: ...
class ISelectCOMLBServer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcf443f4-3f8a-4872-b9-f0-36-9a-79-6d-12-d6')
    @commethod(3)
    def Init() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLBServer(pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class ISendMethodEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2732fd59-b2b4-4d44-87-8c-8b-8f-09-62-60-08')
    @commethod(3)
    def SendMethodCall(pIdentity: c_void_p, riid: POINTER(Guid), dwMeth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SendMethodReturn(pIdentity: c_void_p, riid: POINTER(Guid), dwMeth: UInt32, hrCall: win32more.Foundation.HRESULT, hrServer: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IServiceActivity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('67532e0c-9e2f-4450-a3-54-03-56-33-94-4e-17')
    @commethod(3)
    def SynchronousCall(pIServiceCall: win32more.System.ComponentServices.IServiceCall_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AsynchronousCall(pIServiceCall: win32more.System.ComponentServices.IServiceCall_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BindToCurrentThread() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def UnbindFromThread() -> win32more.Foundation.HRESULT: ...
class IServiceCall(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bd3e2e12-42dd-40f4-a0-9a-95-a5-0c-58-30-4b')
    @commethod(3)
    def OnCall() -> win32more.Foundation.HRESULT: ...
class IServiceComTIIntrinsicsConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('09e6831e-04e1-4ed4-9d-0f-e8-b1-68-ba-fe-af')
    @commethod(3)
    def ComTIIntrinsicsConfig(comtiIntrinsicsConfig: win32more.System.ComponentServices.CSC_COMTIIntrinsicsConfig) -> win32more.Foundation.HRESULT: ...
class IServiceIISIntrinsicsConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1a0cf920-d452-46f4-bc-36-48-11-8d-54-ea-52')
    @commethod(3)
    def IISIntrinsicsConfig(iisIntrinsicsConfig: win32more.System.ComponentServices.CSC_IISIntrinsicsConfig) -> win32more.Foundation.HRESULT: ...
class IServiceInheritanceConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('92186771-d3b4-4d77-a8-ea-ee-84-2d-58-6f-35')
    @commethod(3)
    def ContainingContextTreatment(inheritanceConfig: win32more.System.ComponentServices.CSC_InheritanceConfig) -> win32more.Foundation.HRESULT: ...
class IServicePartitionConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('80182d03-5ea4-4831-ae-97-55-be-ff-c2-e5-90')
    @commethod(3)
    def PartitionConfig(partitionConfig: win32more.System.ComponentServices.CSC_PartitionConfig) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PartitionID(guidPartitionID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IServicePool(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b302df81-ea45-451e-99-a2-09-f9-fd-1b-1e-13')
    @commethod(3)
    def Initialize(pPoolConfig: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown() -> win32more.Foundation.HRESULT: ...
class IServicePoolConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9690656-5bca-470c-84-51-25-0c-1f-43-a3-3e')
    @commethod(3)
    def put_MaxPoolSize(dwMaxPool: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_MaxPoolSize(pdwMaxPool: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def put_MinPoolSize(dwMinPool: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_MinPoolSize(pdwMinPool: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def put_CreationTimeout(dwCreationTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_CreationTimeout(pdwCreationTimeout: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_TransactionAffinity(fTxAffinity: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_TransactionAffinity(pfTxAffinity: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_ClassFactory(pFactory: win32more.System.Com.IClassFactory_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ClassFactory(pFactory: POINTER(win32more.System.Com.IClassFactory_head)) -> win32more.Foundation.HRESULT: ...
class IServiceSxsConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c7cd7379-f3f2-4634-81-1b-70-32-81-d7-3e-08')
    @commethod(3)
    def SxsConfig(scsConfig: win32more.System.ComponentServices.CSC_SxsConfig) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SxsName(szSxsName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SxsDirectory(szSxsDirectory: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IServiceSynchronizationConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fd880e81-6dce-4c58-af-83-a2-08-84-6c-00-30')
    @commethod(3)
    def ConfigureSynchronization(synchConfig: win32more.System.ComponentServices.CSC_SynchronizationConfig) -> win32more.Foundation.HRESULT: ...
class IServiceSysTxnConfig(c_void_p):
    extends: win32more.System.ComponentServices.IServiceTransactionConfig
    Guid = Guid('33caf1a1-fcb8-472b-b4-5e-96-74-48-de-d6-d8')
    @commethod(9)
    def ConfigureBYOTSysTxn(pTxProxy: win32more.System.ComponentServices.ITransactionProxy_head) -> win32more.Foundation.HRESULT: ...
class IServiceThreadPoolConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('186d89bc-f277-4bcc-80-d5-4d-f7-b8-36-ef-4a')
    @commethod(3)
    def SelectThreadPool(threadPool: win32more.System.ComponentServices.CSC_ThreadPool) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetBindingInfo(binding: win32more.System.ComponentServices.CSC_Binding) -> win32more.Foundation.HRESULT: ...
class IServiceTrackerConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6c3a3e1d-0ba6-4036-b7-6f-d0-40-4d-b8-16-c9')
    @commethod(3)
    def TrackerConfig(trackerConfig: win32more.System.ComponentServices.CSC_TrackerConfig, szTrackerAppName: win32more.Foundation.PWSTR, szTrackerCtxName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IServiceTransactionConfig(c_void_p):
    extends: win32more.System.ComponentServices.IServiceTransactionConfigBase
    Guid = Guid('59f4c2a3-d3d7-4a31-b6-e4-6a-b3-17-7c-50-b9')
    @commethod(8)
    def ConfigureBYOT(pITxByot: win32more.System.DistributedTransactionCoordinator.ITransaction_head) -> win32more.Foundation.HRESULT: ...
class IServiceTransactionConfigBase(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('772b3fbe-6ffd-42fb-b5-f8-8f-9b-26-0f-38-10')
    @commethod(3)
    def ConfigureTransaction(transactionConfig: win32more.System.ComponentServices.CSC_TransactionConfig) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsolationLevel(option: win32more.System.ComponentServices.COMAdminTxIsolationLevelOptions) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TransactionTimeout(ulTimeoutSec: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def BringYourOwnTransaction(szTipURL: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NewTransactionDescription(szTxDesc: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class ISharedProperty(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2a005c01-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
    @commethod(7)
    def get_Value(pVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(val: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class ISharedPropertyGroup(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2a005c07-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
    @commethod(7)
    def CreatePropertyByPosition(Index: Int32, fExists: POINTER(win32more.Foundation.VARIANT_BOOL), ppProp: POINTER(win32more.System.ComponentServices.ISharedProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_PropertyByPosition(Index: Int32, ppProperty: POINTER(win32more.System.ComponentServices.ISharedProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateProperty(Name: win32more.Foundation.BSTR, fExists: POINTER(win32more.Foundation.VARIANT_BOOL), ppProp: POINTER(win32more.System.ComponentServices.ISharedProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Property(Name: win32more.Foundation.BSTR, ppProperty: POINTER(win32more.System.ComponentServices.ISharedProperty_head)) -> win32more.Foundation.HRESULT: ...
class ISharedPropertyGroupManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2a005c0d-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
    @commethod(7)
    def CreatePropertyGroup(Name: win32more.Foundation.BSTR, dwIsoMode: POINTER(Int32), dwRelMode: POINTER(Int32), fExists: POINTER(win32more.Foundation.VARIANT_BOOL), ppGroup: POINTER(win32more.System.ComponentServices.ISharedPropertyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Group(Name: win32more.Foundation.BSTR, ppGroup: POINTER(win32more.System.ComponentServices.ISharedPropertyGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retval: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ISystemAppEventData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d6d48a3c-d5c5-49e7-8c-74-99-e4-88-9e-d5-2f')
    @commethod(3)
    def Startup() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataChanged(dwPID: UInt32, dwMask: UInt32, dwNumberSinks: UInt32, bstrDwMethodMask: win32more.Foundation.BSTR, dwReason: UInt32, u64TraceHandle: UInt64) -> win32more.Foundation.HRESULT: ...
class IThreadPoolKnobs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('51372af7-cae7-11cf-be-81-00-aa-00-a2-fa-25')
    @commethod(3)
    def GetMaxThreads(plcMaxThreads: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentThreads(plcCurrentThreads: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetMaxThreads(lcMaxThreads: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDeleteDelay(pmsecDeleteDelay: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetDeleteDelay(msecDeleteDelay: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxQueuedRequests(plcMaxQueuedRequests: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentQueuedRequests(plcCurrentQueuedRequests: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetMaxQueuedRequests(lcMaxQueuedRequests: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetMinThreads(lcMinThreads: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetQueueDepth(lcQueueDepth: Int32) -> win32more.Foundation.HRESULT: ...
class ITransactionContext(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('7999fc21-d3c6-11cf-ac-ab-00-a0-24-a5-5a-ef')
    @commethod(7)
    def CreateInstance(pszProgId: win32more.Foundation.BSTR, pObject: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Abort() -> win32more.Foundation.HRESULT: ...
class ITransactionContextEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7999fc22-d3c6-11cf-ac-ab-00-a0-24-a5-5a-ef')
    @commethod(3)
    def CreateInstance(rclsid: POINTER(Guid), riid: POINTER(Guid), pObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Abort() -> win32more.Foundation.HRESULT: ...
class ITransactionProperty(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('788ea814-87b1-11d1-bb-a6-00-c0-4f-c2-fa-5f')
    @commethod(3)
    def Reserved1() -> Void: ...
    @commethod(4)
    def Reserved2() -> Void: ...
    @commethod(5)
    def Reserved3() -> Void: ...
    @commethod(6)
    def Reserved4() -> Void: ...
    @commethod(7)
    def Reserved5() -> Void: ...
    @commethod(8)
    def Reserved6() -> Void: ...
    @commethod(9)
    def Reserved7() -> Void: ...
    @commethod(10)
    def Reserved8() -> Void: ...
    @commethod(11)
    def Reserved9() -> Void: ...
    @commethod(12)
    def GetTransactionResourcePool(ppTxPool: POINTER(win32more.System.ComponentServices.ITransactionResourcePool_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Reserved10() -> Void: ...
    @commethod(14)
    def Reserved11() -> Void: ...
    @commethod(15)
    def Reserved12() -> Void: ...
    @commethod(16)
    def Reserved13() -> Void: ...
    @commethod(17)
    def Reserved14() -> Void: ...
    @commethod(18)
    def Reserved15() -> Void: ...
    @commethod(19)
    def Reserved16() -> Void: ...
    @commethod(20)
    def Reserved17() -> Void: ...
class ITransactionProxy(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('02558374-df2e-4dae-bd-6b-1d-5c-99-4f-9b-dc')
    @commethod(3)
    def Commit(guid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Abort() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Promote(pTransaction: POINTER(win32more.System.DistributedTransactionCoordinator.ITransaction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateVoter(pTxAsync: win32more.System.DistributedTransactionCoordinator.ITransactionVoterNotifyAsync2_head, ppBallot: POINTER(win32more.System.DistributedTransactionCoordinator.ITransactionVoterBallotAsync2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetIsolationLevel(__MIDL__ITransactionProxy0000: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetIdentifier(pbstrIdentifier: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsReusable(pfIsReusable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITransactionResourcePool(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c5feb7c1-346a-11d1-b1-cc-00-aa-00-ba-32-58')
    @commethod(3)
    def PutResource(pPool: win32more.System.ComponentServices.IObjPool_head, pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetResource(pPool: win32more.System.ComponentServices.IObjPool_head, ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITransactionStatus(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('61f589e8-3724-4898-a0-a4-66-4a-e9-e1-d1-b4')
    @commethod(3)
    def SetTransactionStatus(hrStatus: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransactionStatus(pHrStatus: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
class ITxProxyHolder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('13d86f31-0139-41af-bc-ad-c7-d5-04-35-fe-9f')
    @commethod(3)
    def GetIdentifier(pGuidLtx: POINTER(Guid)) -> Void: ...
LBEvents = Guid('ecabb0c1-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
LockModes = Int32
LockModes_LockSetGet: LockModes = 0
LockModes_LockMethod: LockModes = 1
MessageMover = Guid('ecabb0bf-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
MtsGrp = Guid('4b2e958d-0393-11d1-b1-ab-00-aa-00-ba-32-58')
class ObjectContext(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('74c08646-cedb-11cf-8b-49-00-aa-00-b8-a7-90')
    @commethod(7)
    def CreateInstance(bstrProgID: win32more.Foundation.BSTR, pObject: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetComplete() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetAbort() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EnableCommit() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DisableCommit() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsInTransaction(pbIsInTx: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def IsSecurityEnabled(pbIsEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def IsCallerInRole(bstrRole: win32more.Foundation.BSTR, pbInRole: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Count(plCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Item(name: win32more.Foundation.BSTR, pItem: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Security(ppSecurityProperty: POINTER(win32more.System.ComponentServices.SecurityProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_ContextInfo(ppContextInfo: POINTER(win32more.System.ComponentServices.ContextInfo_head)) -> win32more.Foundation.HRESULT: ...
class ObjectControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7dc41850-0c31-11d0-8b-79-00-aa-00-b8-a7-90')
    @commethod(3)
    def Activate() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CanBePooled(pbPoolable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
PoolMgr = Guid('ecabafb5-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
class RECYCLE_INFO(Structure):
    guidCombaseProcessIdentifier: Guid
    ProcessStartTime: Int64
    dwRecycleLifetimeLimit: UInt32
    dwRecycleMemoryLimit: UInt32
    dwRecycleExpirationTimeout: UInt32
ReleaseModes = Int32
ReleaseModes_Standard: ReleaseModes = 0
ReleaseModes_Process: ReleaseModes = 1
SecurityCallContext = Guid('ecabb0a7-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
SecurityCallers = Guid('ecabb0a6-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
SecurityIdentity = Guid('ecabb0a5-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
class SecurityProperty(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('e74a7215-014d-11d1-a6-3c-00-a0-c9-11-b4-e0')
    @commethod(7)
    def GetDirectCallerName(bstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDirectCreatorName(bstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetOriginalCallerName(bstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetOriginalCreatorName(bstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
ServicePool = Guid('ecabb0c9-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
ServicePoolConfig = Guid('ecabb0ca-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
SharedProperty = Guid('2a005c05-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
SharedPropertyGroup = Guid('2a005c0b-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
SharedPropertyGroupManager = Guid('2a005c11-a5de-11cf-9e-66-00-aa-00-a3-f4-64')
TrackerServer = Guid('ecabafb9-7f19-11d2-97-8e-00-00-f8-75-7e-2a')
TRACKING_COLL_TYPE = Int32
TRKCOLL_PROCESSES: TRACKING_COLL_TYPE = 0
TRKCOLL_APPLICATIONS: TRACKING_COLL_TYPE = 1
TRKCOLL_COMPONENTS: TRACKING_COLL_TYPE = 2
TransactionContext = Guid('7999fc25-d3c6-11cf-ac-ab-00-a0-24-a5-5a-ef')
TransactionContextEx = Guid('5cb66670-d3d4-11cf-ac-ab-00-a0-24-a5-5a-ef')
TransactionVote = Int32
TransactionVote_TxCommit: TransactionVote = 0
TransactionVote_TxAbort: TransactionVote = 1
make_head(_module, 'APPDATA')
make_head(_module, 'ApplicationProcessRecycleInfo')
make_head(_module, 'ApplicationProcessStatistics')
make_head(_module, 'ApplicationProcessSummary')
make_head(_module, 'ApplicationSummary')
make_head(_module, 'APPSTATISTICS')
make_head(_module, 'CLSIDDATA')
make_head(_module, 'CLSIDDATA2')
make_head(_module, 'ComponentHangMonitorInfo')
make_head(_module, 'ComponentStatistics')
make_head(_module, 'ComponentSummary')
make_head(_module, 'COMSVCSEVENTINFO')
make_head(_module, 'ContextInfo')
make_head(_module, 'ContextInfo2')
make_head(_module, 'CrmLogRecordRead')
make_head(_module, 'HANG_INFO')
make_head(_module, 'IAppDomainHelper')
make_head(_module, 'IAssemblyLocator')
make_head(_module, 'IAsyncErrorNotify')
make_head(_module, 'ICatalogCollection')
make_head(_module, 'ICatalogObject')
make_head(_module, 'ICheckSxsConfig')
make_head(_module, 'IComActivityEvents')
make_head(_module, 'ICOMAdminCatalog')
make_head(_module, 'ICOMAdminCatalog2')
make_head(_module, 'IComApp2Events')
make_head(_module, 'IComAppEvents')
make_head(_module, 'IComCRMEvents')
make_head(_module, 'IComExceptionEvents')
make_head(_module, 'IComIdentityEvents')
make_head(_module, 'IComInstance2Events')
make_head(_module, 'IComInstanceEvents')
make_head(_module, 'ICOMLBArguments')
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
make_head(_module, 'IManagedActivationEvents')
make_head(_module, 'IManagedObjectInfo')
make_head(_module, 'IManagedPoolAction')
make_head(_module, 'IManagedPooledObj')
make_head(_module, 'IMessageMover')
make_head(_module, 'IMTSActivity')
make_head(_module, 'IMTSCall')
make_head(_module, 'IMtsEventInfo')
make_head(_module, 'IMtsEvents')
make_head(_module, 'IMtsGrp')
make_head(_module, 'IMTSLocator')
make_head(_module, 'IObjectConstruct')
make_head(_module, 'IObjectConstructString')
make_head(_module, 'IObjectContext')
make_head(_module, 'IObjectContextActivity')
make_head(_module, 'IObjectContextInfo')
make_head(_module, 'IObjectContextInfo2')
make_head(_module, 'IObjectContextTip')
make_head(_module, 'IObjectControl')
make_head(_module, 'IObjPool')
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
__all__ = [
    "APPDATA",
    "APPSTATISTICS",
    "APPTYPE_LIBRARY",
    "APPTYPE_SERVER",
    "APPTYPE_SWC",
    "APPTYPE_UNKNOWN",
    "AppDomainHelper",
    "ApplicationProcessRecycleInfo",
    "ApplicationProcessStatistics",
    "ApplicationProcessSummary",
    "ApplicationSummary",
    "AutoSvcs_Error_Constants",
    "AutoSvcs_Error_Constants_comQCErrApplicationNotQueued",
    "AutoSvcs_Error_Constants_comQCErrNoQueueableInterfaces",
    "AutoSvcs_Error_Constants_comQCErrQueueTransactMismatch",
    "AutoSvcs_Error_Constants_comQCErrQueuingServiceNotAvailable",
    "AutoSvcs_Error_Constants_comqcErrBadMarshaledObject",
    "AutoSvcs_Error_Constants_comqcErrInvalidMessage",
    "AutoSvcs_Error_Constants_comqcErrMarshaledObjSameTxn",
    "AutoSvcs_Error_Constants_comqcErrMsgNotAuthenticated",
    "AutoSvcs_Error_Constants_comqcErrMsmqConnectorUsed",
    "AutoSvcs_Error_Constants_comqcErrMsmqServiceUnavailable",
    "AutoSvcs_Error_Constants_comqcErrMsmqSidUnavailable",
    "AutoSvcs_Error_Constants_comqcErrOutParam",
    "AutoSvcs_Error_Constants_comqcErrPSLoad",
    "AutoSvcs_Error_Constants_comqcErrRecorderMarshalled",
    "AutoSvcs_Error_Constants_comqcErrRecorderNotTrusted",
    "AutoSvcs_Error_Constants_comqcErrWrongMsgExtension",
    "AutoSvcs_Error_Constants_mtsErrCtxAborted",
    "AutoSvcs_Error_Constants_mtsErrCtxAborting",
    "AutoSvcs_Error_Constants_mtsErrCtxNoContext",
    "AutoSvcs_Error_Constants_mtsErrCtxNoSecurity",
    "AutoSvcs_Error_Constants_mtsErrCtxNotRegistered",
    "AutoSvcs_Error_Constants_mtsErrCtxOldReference",
    "AutoSvcs_Error_Constants_mtsErrCtxRoleNotFound",
    "AutoSvcs_Error_Constants_mtsErrCtxSynchTimeout",
    "AutoSvcs_Error_Constants_mtsErrCtxTMNotAvailable",
    "AutoSvcs_Error_Constants_mtsErrCtxWrongThread",
    "ByotServerEx",
    "CLSIDDATA",
    "CLSIDDATA2",
    "COMAdminAccessChecksLevelOptions",
    "COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationComponentLevel",
    "COMAdminAccessChecksLevelOptions_COMAdminAccessChecksApplicationLevel",
    "COMAdminActivationOptions",
    "COMAdminActivationOptions_COMAdminActivationInproc",
    "COMAdminActivationOptions_COMAdminActivationLocal",
    "COMAdminApplicationExportOptions",
    "COMAdminApplicationExportOptions_COMAdminExportApplicationProxy",
    "COMAdminApplicationExportOptions_COMAdminExportForceOverwriteOfFiles",
    "COMAdminApplicationExportOptions_COMAdminExportIn10Format",
    "COMAdminApplicationExportOptions_COMAdminExportNoUsers",
    "COMAdminApplicationExportOptions_COMAdminExportUsers",
    "COMAdminApplicationInstallOptions",
    "COMAdminApplicationInstallOptions_COMAdminInstallForceOverwriteOfFiles",
    "COMAdminApplicationInstallOptions_COMAdminInstallNoUsers",
    "COMAdminApplicationInstallOptions_COMAdminInstallUsers",
    "COMAdminAuthenticationCapabilitiesOptions",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesDynamicCloaking",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesNone",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesSecureReference",
    "COMAdminAuthenticationCapabilitiesOptions_COMAdminAuthenticationCapabilitiesStaticCloaking",
    "COMAdminAuthenticationLevelOptions",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationCall",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationConnect",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationDefault",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationIntegrity",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationNone",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPacket",
    "COMAdminAuthenticationLevelOptions_COMAdminAuthenticationPrivacy",
    "COMAdminCatalog",
    "COMAdminCatalogCollection",
    "COMAdminCatalogObject",
    "COMAdminComponentFlags",
    "COMAdminComponentFlags_COMAdminCompFlagAlreadyInstalled",
    "COMAdminComponentFlags_COMAdminCompFlagCOMPlusPropertiesFound",
    "COMAdminComponentFlags_COMAdminCompFlagInterfacesFound",
    "COMAdminComponentFlags_COMAdminCompFlagNotInApplication",
    "COMAdminComponentFlags_COMAdminCompFlagProxyFound",
    "COMAdminComponentFlags_COMAdminCompFlagTypeInfoFound",
    "COMAdminComponentType",
    "COMAdminComponentType_COMAdmin32BitComponent",
    "COMAdminComponentType_COMAdmin64BitComponent",
    "COMAdminErrorCodes",
    "COMAdminErrorCodes_COMAdminErrAlreadyInstalled",
    "COMAdminErrorCodes_COMAdminErrAppDirNotFound",
    "COMAdminErrorCodes_COMAdminErrAppFileReadFail",
    "COMAdminErrorCodes_COMAdminErrAppFileVersion",
    "COMAdminErrorCodes_COMAdminErrAppFileWriteFail",
    "COMAdminErrorCodes_COMAdminErrAppNotRunning",
    "COMAdminErrorCodes_COMAdminErrApplicationExists",
    "COMAdminErrorCodes_COMAdminErrApplidMatchesClsid",
    "COMAdminErrorCodes_COMAdminErrAuthenticationLevel",
    "COMAdminErrorCodes_COMAdminErrBadPath",
    "COMAdminErrorCodes_COMAdminErrBadRegistryLibID",
    "COMAdminErrorCodes_COMAdminErrBadRegistryProgID",
    "COMAdminErrorCodes_COMAdminErrBasePartitionOnly",
    "COMAdminErrorCodes_COMAdminErrCLSIDOrIIDMismatch",
    "COMAdminErrorCodes_COMAdminErrCanNotExportAppProxy",
    "COMAdminErrorCodes_COMAdminErrCanNotExportSystemApp",
    "COMAdminErrorCodes_COMAdminErrCanNotStartApp",
    "COMAdminErrorCodes_COMAdminErrCanNotSubscribeToComponent",
    "COMAdminErrorCodes_COMAdminErrCannotCopyEventClass",
    "COMAdminErrorCodes_COMAdminErrCantCopyFile",
    "COMAdminErrorCodes_COMAdminErrCantRecycleLibraryApps",
    "COMAdminErrorCodes_COMAdminErrCantRecycleServiceApps",
    "COMAdminErrorCodes_COMAdminErrCatBitnessMismatch",
    "COMAdminErrorCodes_COMAdminErrCatPauseResumeNotSupported",
    "COMAdminErrorCodes_COMAdminErrCatServerFault",
    "COMAdminErrorCodes_COMAdminErrCatUnacceptableBitness",
    "COMAdminErrorCodes_COMAdminErrCatWrongAppBitnessBitness",
    "COMAdminErrorCodes_COMAdminErrCoReqCompInstalled",
    "COMAdminErrorCodes_COMAdminErrCompFileBadTLB",
    "COMAdminErrorCodes_COMAdminErrCompFileClassNotAvail",
    "COMAdminErrorCodes_COMAdminErrCompFileDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrCompFileGetClassObj",
    "COMAdminErrorCodes_COMAdminErrCompFileLoadDLLFail",
    "COMAdminErrorCodes_COMAdminErrCompFileNoRegistrar",
    "COMAdminErrorCodes_COMAdminErrCompFileNotInstallable",
    "COMAdminErrorCodes_COMAdminErrCompMoveBadDest",
    "COMAdminErrorCodes_COMAdminErrCompMoveDest",
    "COMAdminErrorCodes_COMAdminErrCompMoveLocked",
    "COMAdminErrorCodes_COMAdminErrCompMovePrivate",
    "COMAdminErrorCodes_COMAdminErrCompMoveSource",
    "COMAdminErrorCodes_COMAdminErrComponentExists",
    "COMAdminErrorCodes_COMAdminErrDllLoadFailed",
    "COMAdminErrorCodes_COMAdminErrDllRegisterServer",
    "COMAdminErrorCodes_COMAdminErrDuplicatePartitionName",
    "COMAdminErrorCodes_COMAdminErrEventClassCannotBeSubscriber",
    "COMAdminErrorCodes_COMAdminErrImportedComponentsNotAllowed",
    "COMAdminErrorCodes_COMAdminErrInvalidPartition",
    "COMAdminErrorCodes_COMAdminErrInvalidUserids",
    "COMAdminErrorCodes_COMAdminErrKeyMissing",
    "COMAdminErrorCodes_COMAdminErrLibAppProxyIncompatible",
    "COMAdminErrorCodes_COMAdminErrMigSchemaNotFound",
    "COMAdminErrorCodes_COMAdminErrMigVersionNotSupported",
    "COMAdminErrorCodes_COMAdminErrNoRegistryCLSID",
    "COMAdminErrorCodes_COMAdminErrNoServerShare",
    "COMAdminErrorCodes_COMAdminErrNoUser",
    "COMAdminErrorCodes_COMAdminErrNotChangeable",
    "COMAdminErrorCodes_COMAdminErrNotDeletable",
    "COMAdminErrorCodes_COMAdminErrNotInRegistry",
    "COMAdminErrorCodes_COMAdminErrObjectDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrObjectErrors",
    "COMAdminErrorCodes_COMAdminErrObjectExists",
    "COMAdminErrorCodes_COMAdminErrObjectInvalid",
    "COMAdminErrorCodes_COMAdminErrObjectNotPoolable",
    "COMAdminErrorCodes_COMAdminErrObjectParentMissing",
    "COMAdminErrorCodes_COMAdminErrPartitionInUse",
    "COMAdminErrorCodes_COMAdminErrPartitionMsiOnly",
    "COMAdminErrorCodes_COMAdminErrPausedProcessMayNotBeRecycled",
    "COMAdminErrorCodes_COMAdminErrProcessAlreadyRecycled",
    "COMAdminErrorCodes_COMAdminErrPropertyOverflow",
    "COMAdminErrorCodes_COMAdminErrPropertySaveFailed",
    "COMAdminErrorCodes_COMAdminErrQueuingServiceNotAvailable",
    "COMAdminErrorCodes_COMAdminErrRegFileCorrupt",
    "COMAdminErrorCodes_COMAdminErrRegdbAlreadyRunning",
    "COMAdminErrorCodes_COMAdminErrRegdbNotInitialized",
    "COMAdminErrorCodes_COMAdminErrRegdbNotOpen",
    "COMAdminErrorCodes_COMAdminErrRegdbSystemErr",
    "COMAdminErrorCodes_COMAdminErrRegisterTLB",
    "COMAdminErrorCodes_COMAdminErrRegistrarFailed",
    "COMAdminErrorCodes_COMAdminErrRemoteInterface",
    "COMAdminErrorCodes_COMAdminErrRequiresDifferentPlatform",
    "COMAdminErrorCodes_COMAdminErrRoleDoesNotExist",
    "COMAdminErrorCodes_COMAdminErrRoleExists",
    "COMAdminErrorCodes_COMAdminErrServiceNotInstalled",
    "COMAdminErrorCodes_COMAdminErrSession",
    "COMAdminErrorCodes_COMAdminErrStartAppDisabled",
    "COMAdminErrorCodes_COMAdminErrStartAppNeedsComponents",
    "COMAdminErrorCodes_COMAdminErrSystemApp",
    "COMAdminErrorCodes_COMAdminErrUserPasswdNotValid",
    "COMAdminFileFlags",
    "COMAdminFileFlags_COMAdminFileFlagAlreadyInstalled",
    "COMAdminFileFlags_COMAdminFileFlagBadTLB",
    "COMAdminFileFlags_COMAdminFileFlagCOM",
    "COMAdminFileFlags_COMAdminFileFlagClassNotAvailable",
    "COMAdminFileFlags_COMAdminFileFlagContainsComp",
    "COMAdminFileFlags_COMAdminFileFlagContainsPS",
    "COMAdminFileFlags_COMAdminFileFlagContainsTLB",
    "COMAdminFileFlags_COMAdminFileFlagDLLRegsvrFailed",
    "COMAdminFileFlags_COMAdminFileFlagDoesNotExist",
    "COMAdminFileFlags_COMAdminFileFlagError",
    "COMAdminFileFlags_COMAdminFileFlagGetClassObjFailed",
    "COMAdminFileFlags_COMAdminFileFlagLoadable",
    "COMAdminFileFlags_COMAdminFileFlagNoRegistrar",
    "COMAdminFileFlags_COMAdminFileFlagRegTLBFailed",
    "COMAdminFileFlags_COMAdminFileFlagRegistrar",
    "COMAdminFileFlags_COMAdminFileFlagRegistrarFailed",
    "COMAdminFileFlags_COMAdminFileFlagSelfReg",
    "COMAdminFileFlags_COMAdminFileFlagSelfUnReg",
    "COMAdminFileFlags_COMAdminFileFlagUnloadableDLL",
    "COMAdminImpersonationLevelOptions",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationAnonymous",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationDelegate",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationIdentify",
    "COMAdminImpersonationLevelOptions_COMAdminImpersonationImpersonate",
    "COMAdminInUse",
    "COMAdminInUse_COMAdminInUseByCatalog",
    "COMAdminInUse_COMAdminInUseByRegistryClsid",
    "COMAdminInUse_COMAdminInUseByRegistryProxyStub",
    "COMAdminInUse_COMAdminInUseByRegistryTypeLib",
    "COMAdminInUse_COMAdminInUseByRegistryUnknown",
    "COMAdminInUse_COMAdminNotInUse",
    "COMAdminOS",
    "COMAdminOS_COMAdminOSNotInitialized",
    "COMAdminOS_COMAdminOSUnknown",
    "COMAdminOS_COMAdminOSWindows2000",
    "COMAdminOS_COMAdminOSWindows2000AdvancedServer",
    "COMAdminOS_COMAdminOSWindows2000Unknown",
    "COMAdminOS_COMAdminOSWindows3_1",
    "COMAdminOS_COMAdminOSWindows7DatacenterServer",
    "COMAdminOS_COMAdminOSWindows7EnterpriseServer",
    "COMAdminOS_COMAdminOSWindows7Personal",
    "COMAdminOS_COMAdminOSWindows7Professional",
    "COMAdminOS_COMAdminOSWindows7StandardServer",
    "COMAdminOS_COMAdminOSWindows7WebServer",
    "COMAdminOS_COMAdminOSWindows8DatacenterServer",
    "COMAdminOS_COMAdminOSWindows8EnterpriseServer",
    "COMAdminOS_COMAdminOSWindows8Personal",
    "COMAdminOS_COMAdminOSWindows8Professional",
    "COMAdminOS_COMAdminOSWindows8StandardServer",
    "COMAdminOS_COMAdminOSWindows8WebServer",
    "COMAdminOS_COMAdminOSWindows9x",
    "COMAdminOS_COMAdminOSWindowsBlueDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsBlueEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsBluePersonal",
    "COMAdminOS_COMAdminOSWindowsBlueProfessional",
    "COMAdminOS_COMAdminOSWindowsBlueStandardServer",
    "COMAdminOS_COMAdminOSWindowsBlueWebServer",
    "COMAdminOS_COMAdminOSWindowsLonghornDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsLonghornEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsLonghornPersonal",
    "COMAdminOS_COMAdminOSWindowsLonghornProfessional",
    "COMAdminOS_COMAdminOSWindowsLonghornStandardServer",
    "COMAdminOS_COMAdminOSWindowsLonghornWebServer",
    "COMAdminOS_COMAdminOSWindowsNETDatacenterServer",
    "COMAdminOS_COMAdminOSWindowsNETEnterpriseServer",
    "COMAdminOS_COMAdminOSWindowsNETStandardServer",
    "COMAdminOS_COMAdminOSWindowsNETWebServer",
    "COMAdminOS_COMAdminOSWindowsXPPersonal",
    "COMAdminOS_COMAdminOSWindowsXPProfessional",
    "COMAdminQCMessageAuthenticateOptions",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOff",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateOn",
    "COMAdminQCMessageAuthenticateOptions_COMAdminQCMessageAuthenticateSecureApps",
    "COMAdminServiceOptions",
    "COMAdminServiceOptions_COMAdminServiceLoadBalanceRouter",
    "COMAdminServiceStatusOptions",
    "COMAdminServiceStatusOptions_COMAdminServiceContinuePending",
    "COMAdminServiceStatusOptions_COMAdminServicePausePending",
    "COMAdminServiceStatusOptions_COMAdminServicePaused",
    "COMAdminServiceStatusOptions_COMAdminServiceRunning",
    "COMAdminServiceStatusOptions_COMAdminServiceStartPending",
    "COMAdminServiceStatusOptions_COMAdminServiceStopPending",
    "COMAdminServiceStatusOptions_COMAdminServiceStopped",
    "COMAdminServiceStatusOptions_COMAdminServiceUnknownState",
    "COMAdminSynchronizationOptions",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationIgnored",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationNone",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationRequired",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationRequiresNew",
    "COMAdminSynchronizationOptions_COMAdminSynchronizationSupported",
    "COMAdminThreadingModels",
    "COMAdminThreadingModels_COMAdminThreadingModelApartment",
    "COMAdminThreadingModels_COMAdminThreadingModelBoth",
    "COMAdminThreadingModels_COMAdminThreadingModelFree",
    "COMAdminThreadingModels_COMAdminThreadingModelMain",
    "COMAdminThreadingModels_COMAdminThreadingModelNeutral",
    "COMAdminThreadingModels_COMAdminThreadingModelNotSpecified",
    "COMAdminTransactionOptions",
    "COMAdminTransactionOptions_COMAdminTransactionIgnored",
    "COMAdminTransactionOptions_COMAdminTransactionNone",
    "COMAdminTransactionOptions_COMAdminTransactionRequired",
    "COMAdminTransactionOptions_COMAdminTransactionRequiresNew",
    "COMAdminTransactionOptions_COMAdminTransactionSupported",
    "COMAdminTxIsolationLevelOptions",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelAny",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadCommitted",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelReadUnCommitted",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelRepeatableRead",
    "COMAdminTxIsolationLevelOptions_COMAdminTxIsolationLevelSerializable",
    "COMEvents",
    "COMPLUS_APPTYPE",
    "COMSVCSEVENTINFO",
    "CRMClerk",
    "CRMFLAGS",
    "CRMFLAG_FORGETTARGET",
    "CRMFLAG_REPLAYINPROGRESS",
    "CRMFLAG_WRITTENDURINGABORT",
    "CRMFLAG_WRITTENDURINGCOMMIT",
    "CRMFLAG_WRITTENDURINGPREPARE",
    "CRMFLAG_WRITTENDURINGRECOVERY",
    "CRMFLAG_WRITTENDURINGREPLAY",
    "CRMREGFLAGS",
    "CRMREGFLAG_ABORTPHASE",
    "CRMREGFLAG_ALLPHASES",
    "CRMREGFLAG_COMMITPHASE",
    "CRMREGFLAG_FAILIFINDOUBTSREMAIN",
    "CRMREGFLAG_PREPAREPHASE",
    "CRMRecoveryClerk",
    "CRR_ACTIVATION_LIMIT",
    "CRR_CALL_LIMIT",
    "CRR_LIFETIME_LIMIT",
    "CRR_MEMORY_LIMIT",
    "CRR_NO_REASON_SUPPLIED",
    "CRR_RECYCLED_FROM_UI",
    "CSC_BindToPoolThread",
    "CSC_Binding",
    "CSC_COMTIIntrinsicsConfig",
    "CSC_CreateTransactionIfNecessary",
    "CSC_DontUseTracker",
    "CSC_IISIntrinsicsConfig",
    "CSC_IfContainerIsSynchronized",
    "CSC_IfContainerIsTransactional",
    "CSC_Ignore",
    "CSC_Inherit",
    "CSC_InheritCOMTIIntrinsics",
    "CSC_InheritIISIntrinsics",
    "CSC_InheritPartition",
    "CSC_InheritSxs",
    "CSC_InheritanceConfig",
    "CSC_MTAThreadPool",
    "CSC_NewPartition",
    "CSC_NewSxs",
    "CSC_NewSynchronization",
    "CSC_NewSynchronizationIfNecessary",
    "CSC_NewTransaction",
    "CSC_NoBinding",
    "CSC_NoCOMTIIntrinsics",
    "CSC_NoIISIntrinsics",
    "CSC_NoPartition",
    "CSC_NoSxs",
    "CSC_NoSynchronization",
    "CSC_NoTransaction",
    "CSC_PartitionConfig",
    "CSC_STAThreadPool",
    "CSC_SxsConfig",
    "CSC_SynchronizationConfig",
    "CSC_ThreadPool",
    "CSC_ThreadPoolInherit",
    "CSC_ThreadPoolNone",
    "CSC_TrackerConfig",
    "CSC_TransactionConfig",
    "CSC_UseTracker",
    "CServiceConfig",
    "ClrAssemblyLocator",
    "CoCreateActivity",
    "CoEnterServiceDomain",
    "CoGetDefaultContext",
    "CoLeaveServiceDomain",
    "CoMTSLocator",
    "ComServiceEvents",
    "ComSystemAppEventData",
    "ComponentHangMonitorInfo",
    "ComponentStatistics",
    "ComponentSummary",
    "ContextInfo",
    "ContextInfo2",
    "CrmLogRecordRead",
    "CrmTransactionState",
    "DATA_NOT_AVAILABLE",
    "DUMPTYPE",
    "DUMPTYPE_FULL",
    "DUMPTYPE_MINI",
    "DUMPTYPE_NONE",
    "DispenserManager",
    "Dummy30040732",
    "EventServer",
    "GATD_INCLUDE_APPLICATION_NAME",
    "GATD_INCLUDE_CLASS_NAME",
    "GATD_INCLUDE_LIBRARY_APPS",
    "GATD_INCLUDE_PROCESS_EXE_NAME",
    "GATD_INCLUDE_SWC",
    "GUID_STRING_SIZE",
    "GetAppTrackerDataFlags",
    "GetDispenserManager",
    "GetManagedExtensions",
    "GetSecurityCallContextAppObject",
    "HANG_INFO",
    "IAppDomainHelper",
    "IAssemblyLocator",
    "IAsyncErrorNotify",
    "ICOMAdminCatalog",
    "ICOMAdminCatalog2",
    "ICOMLBArguments",
    "ICatalogCollection",
    "ICatalogObject",
    "ICheckSxsConfig",
    "IComActivityEvents",
    "IComApp2Events",
    "IComAppEvents",
    "IComCRMEvents",
    "IComExceptionEvents",
    "IComIdentityEvents",
    "IComInstance2Events",
    "IComInstanceEvents",
    "IComLTxEvents",
    "IComMethod2Events",
    "IComMethodEvents",
    "IComMtaThreadPoolKnobs",
    "IComObjectConstruction2Events",
    "IComObjectConstructionEvents",
    "IComObjectEvents",
    "IComObjectPool2Events",
    "IComObjectPoolEvents",
    "IComObjectPoolEvents2",
    "IComQCEvents",
    "IComResourceEvents",
    "IComSecurityEvents",
    "IComStaThreadPoolKnobs",
    "IComStaThreadPoolKnobs2",
    "IComThreadEvents",
    "IComTrackingInfoCollection",
    "IComTrackingInfoEvents",
    "IComTrackingInfoObject",
    "IComTrackingInfoProperties",
    "IComTransaction2Events",
    "IComTransactionEvents",
    "IComUserEvent",
    "IContextProperties",
    "IContextSecurityPerimeter",
    "IContextState",
    "ICreateWithLocalTransaction",
    "ICreateWithTipTransactionEx",
    "ICreateWithTransactionEx",
    "ICrmCompensator",
    "ICrmCompensatorVariants",
    "ICrmFormatLogRecords",
    "ICrmLogControl",
    "ICrmMonitor",
    "ICrmMonitorClerks",
    "ICrmMonitorLogRecords",
    "IDispenserDriver",
    "IDispenserManager",
    "IEnumNames",
    "IEventServerTrace",
    "IGetAppTrackerData",
    "IGetContextProperties",
    "IGetSecurityCallContext",
    "IHolder",
    "ILBEvents",
    "IMTSActivity",
    "IMTSCall",
    "IMTSLocator",
    "IManagedActivationEvents",
    "IManagedObjectInfo",
    "IManagedPoolAction",
    "IManagedPooledObj",
    "IMessageMover",
    "IMtsEventInfo",
    "IMtsEvents",
    "IMtsGrp",
    "IObjPool",
    "IObjectConstruct",
    "IObjectConstructString",
    "IObjectContext",
    "IObjectContextActivity",
    "IObjectContextInfo",
    "IObjectContextInfo2",
    "IObjectContextTip",
    "IObjectControl",
    "IPlaybackControl",
    "IPoolManager",
    "IProcessInitializer",
    "ISecurityCallContext",
    "ISecurityCallersColl",
    "ISecurityIdentityColl",
    "ISecurityProperty",
    "ISelectCOMLBServer",
    "ISendMethodEvents",
    "IServiceActivity",
    "IServiceCall",
    "IServiceComTIIntrinsicsConfig",
    "IServiceIISIntrinsicsConfig",
    "IServiceInheritanceConfig",
    "IServicePartitionConfig",
    "IServicePool",
    "IServicePoolConfig",
    "IServiceSxsConfig",
    "IServiceSynchronizationConfig",
    "IServiceSysTxnConfig",
    "IServiceThreadPoolConfig",
    "IServiceTrackerConfig",
    "IServiceTransactionConfig",
    "IServiceTransactionConfigBase",
    "ISharedProperty",
    "ISharedPropertyGroup",
    "ISharedPropertyGroupManager",
    "ISystemAppEventData",
    "IThreadPoolKnobs",
    "ITransactionContext",
    "ITransactionContextEx",
    "ITransactionProperty",
    "ITransactionProxy",
    "ITransactionResourcePool",
    "ITransactionStatus",
    "ITxProxyHolder",
    "LBEvents",
    "LockModes",
    "LockModes_LockMethod",
    "LockModes_LockSetGet",
    "MTSCreateActivity",
    "MTXDM_E_ENLISTRESOURCEFAILED",
    "MessageMover",
    "MtsGrp",
    "ObjectContext",
    "ObjectControl",
    "PoolMgr",
    "RECYCLE_INFO",
    "RecycleSurrogate",
    "ReleaseModes",
    "ReleaseModes_Process",
    "ReleaseModes_Standard",
    "SafeRef",
    "SecurityCallContext",
    "SecurityCallers",
    "SecurityIdentity",
    "SecurityProperty",
    "ServicePool",
    "ServicePoolConfig",
    "SharedProperty",
    "SharedPropertyGroup",
    "SharedPropertyGroupManager",
    "TRACKER_INIT_EVENT",
    "TRACKER_STARTSTOP_EVENT",
    "TRACKING_COLL_TYPE",
    "TRKCOLL_APPLICATIONS",
    "TRKCOLL_COMPONENTS",
    "TRKCOLL_PROCESSES",
    "TrackerServer",
    "TransactionContext",
    "TransactionContextEx",
    "TransactionVote",
    "TransactionVote_TxAbort",
    "TransactionVote_TxCommit",
    "TxState_Aborted",
    "TxState_Active",
    "TxState_Committed",
    "TxState_Indoubt",
]
_arch_optional = [
]
