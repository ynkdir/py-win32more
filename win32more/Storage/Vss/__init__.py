from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Storage.VirtualDiskService
import win32more.Storage.Vss
import win32more.System.Com
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
VSS_ASSOC_NO_MAX_SPACE: Int32 = -1
VSS_ASSOC_REMOVE: UInt32 = 0
VSS_E_BAD_STATE: win32more.Foundation.HRESULT = -2147212543
VSS_E_UNEXPECTED: win32more.Foundation.HRESULT = -2147212542
VSS_E_PROVIDER_ALREADY_REGISTERED: win32more.Foundation.HRESULT = -2147212541
VSS_E_PROVIDER_NOT_REGISTERED: win32more.Foundation.HRESULT = -2147212540
VSS_E_PROVIDER_VETO: win32more.Foundation.HRESULT = -2147212538
VSS_E_PROVIDER_IN_USE: win32more.Foundation.HRESULT = -2147212537
VSS_E_OBJECT_NOT_FOUND: win32more.Foundation.HRESULT = -2147212536
VSS_S_ASYNC_PENDING: win32more.Foundation.HRESULT = 271113
VSS_S_ASYNC_FINISHED: win32more.Foundation.HRESULT = 271114
VSS_S_ASYNC_CANCELLED: win32more.Foundation.HRESULT = 271115
VSS_E_VOLUME_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147212532
VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER: win32more.Foundation.HRESULT = -2147212530
VSS_E_OBJECT_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147212531
VSS_E_UNEXPECTED_PROVIDER_ERROR: win32more.Foundation.HRESULT = -2147212529
VSS_E_CORRUPT_XML_DOCUMENT: win32more.Foundation.HRESULT = -2147212528
VSS_E_INVALID_XML_DOCUMENT: win32more.Foundation.HRESULT = -2147212527
VSS_E_MAXIMUM_NUMBER_OF_VOLUMES_REACHED: win32more.Foundation.HRESULT = -2147212526
VSS_E_FLUSH_WRITES_TIMEOUT: win32more.Foundation.HRESULT = -2147212525
VSS_E_HOLD_WRITES_TIMEOUT: win32more.Foundation.HRESULT = -2147212524
VSS_E_UNEXPECTED_WRITER_ERROR: win32more.Foundation.HRESULT = -2147212523
VSS_E_SNAPSHOT_SET_IN_PROGRESS: win32more.Foundation.HRESULT = -2147212522
VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED: win32more.Foundation.HRESULT = -2147212521
VSS_E_WRITER_INFRASTRUCTURE: win32more.Foundation.HRESULT = -2147212520
VSS_E_WRITER_NOT_RESPONDING: win32more.Foundation.HRESULT = -2147212519
VSS_E_WRITER_ALREADY_SUBSCRIBED: win32more.Foundation.HRESULT = -2147212518
VSS_E_UNSUPPORTED_CONTEXT: win32more.Foundation.HRESULT = -2147212517
VSS_E_VOLUME_IN_USE: win32more.Foundation.HRESULT = -2147212515
VSS_E_MAXIMUM_DIFFAREA_ASSOCIATIONS_REACHED: win32more.Foundation.HRESULT = -2147212514
VSS_E_INSUFFICIENT_STORAGE: win32more.Foundation.HRESULT = -2147212513
VSS_E_NO_SNAPSHOTS_IMPORTED: win32more.Foundation.HRESULT = -2147212512
VSS_S_SOME_SNAPSHOTS_NOT_IMPORTED: win32more.Foundation.HRESULT = 271137
VSS_E_SOME_SNAPSHOTS_NOT_IMPORTED: win32more.Foundation.HRESULT = -2147212511
VSS_E_MAXIMUM_NUMBER_OF_REMOTE_MACHINES_REACHED: win32more.Foundation.HRESULT = -2147212510
VSS_E_REMOTE_SERVER_UNAVAILABLE: win32more.Foundation.HRESULT = -2147212509
VSS_E_REMOTE_SERVER_UNSUPPORTED: win32more.Foundation.HRESULT = -2147212508
VSS_E_REVERT_IN_PROGRESS: win32more.Foundation.HRESULT = -2147212507
VSS_E_REVERT_VOLUME_LOST: win32more.Foundation.HRESULT = -2147212506
VSS_E_REBOOT_REQUIRED: win32more.Foundation.HRESULT = -2147212505
VSS_E_TRANSACTION_FREEZE_TIMEOUT: win32more.Foundation.HRESULT = -2147212504
VSS_E_TRANSACTION_THAW_TIMEOUT: win32more.Foundation.HRESULT = -2147212503
VSS_E_VOLUME_NOT_LOCAL: win32more.Foundation.HRESULT = -2147212499
VSS_E_CLUSTER_TIMEOUT: win32more.Foundation.HRESULT = -2147212498
VSS_E_WRITERERROR_INCONSISTENTSNAPSHOT: win32more.Foundation.HRESULT = -2147212304
VSS_E_WRITERERROR_OUTOFRESOURCES: win32more.Foundation.HRESULT = -2147212303
VSS_E_WRITERERROR_TIMEOUT: win32more.Foundation.HRESULT = -2147212302
VSS_E_WRITERERROR_RETRYABLE: win32more.Foundation.HRESULT = -2147212301
VSS_E_WRITERERROR_NONRETRYABLE: win32more.Foundation.HRESULT = -2147212300
VSS_E_WRITERERROR_RECOVERY_FAILED: win32more.Foundation.HRESULT = -2147212299
VSS_E_BREAK_REVERT_ID_FAILED: win32more.Foundation.HRESULT = -2147212298
VSS_E_LEGACY_PROVIDER: win32more.Foundation.HRESULT = -2147212297
VSS_E_MISSING_DISK: win32more.Foundation.HRESULT = -2147212296
VSS_E_MISSING_HIDDEN_VOLUME: win32more.Foundation.HRESULT = -2147212295
VSS_E_MISSING_VOLUME: win32more.Foundation.HRESULT = -2147212294
VSS_E_AUTORECOVERY_FAILED: win32more.Foundation.HRESULT = -2147212293
VSS_E_DYNAMIC_DISK_ERROR: win32more.Foundation.HRESULT = -2147212292
VSS_E_NONTRANSPORTABLE_BCD: win32more.Foundation.HRESULT = -2147212291
VSS_E_CANNOT_REVERT_DISKID: win32more.Foundation.HRESULT = -2147212290
VSS_E_RESYNC_IN_PROGRESS: win32more.Foundation.HRESULT = -2147212289
VSS_E_CLUSTER_ERROR: win32more.Foundation.HRESULT = -2147212288
VSS_E_UNSELECTED_VOLUME: win32more.Foundation.HRESULT = -2147212502
VSS_E_SNAPSHOT_NOT_IN_SET: win32more.Foundation.HRESULT = -2147212501
VSS_E_NESTED_VOLUME_LIMIT: win32more.Foundation.HRESULT = -2147212500
VSS_E_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147212497
VSS_E_WRITERERROR_PARTIAL_FAILURE: win32more.Foundation.HRESULT = -2147212490
VSS_E_ASRERROR_DISK_ASSIGNMENT_FAILED: win32more.Foundation.HRESULT = -2147212287
VSS_E_ASRERROR_DISK_RECREATION_FAILED: win32more.Foundation.HRESULT = -2147212286
VSS_E_ASRERROR_NO_ARCPATH: win32more.Foundation.HRESULT = -2147212285
VSS_E_ASRERROR_MISSING_DYNDISK: win32more.Foundation.HRESULT = -2147212284
VSS_E_ASRERROR_SHARED_CRIDISK: win32more.Foundation.HRESULT = -2147212283
VSS_E_ASRERROR_DATADISK_RDISK0: win32more.Foundation.HRESULT = -2147212282
VSS_E_ASRERROR_RDISK0_TOOSMALL: win32more.Foundation.HRESULT = -2147212281
VSS_E_ASRERROR_CRITICAL_DISKS_TOO_SMALL: win32more.Foundation.HRESULT = -2147212280
VSS_E_WRITER_STATUS_NOT_AVAILABLE: win32more.Foundation.HRESULT = -2147212279
VSS_E_ASRERROR_DYNAMIC_VHD_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2147212278
VSS_E_CRITICAL_VOLUME_ON_INVALID_DISK: win32more.Foundation.HRESULT = -2147212271
VSS_E_ASRERROR_RDISK_FOR_SYSTEM_DISK_NOT_FOUND: win32more.Foundation.HRESULT = -2147212270
VSS_E_ASRERROR_NO_PHYSICAL_DISK_AVAILABLE: win32more.Foundation.HRESULT = -2147212269
VSS_E_ASRERROR_FIXED_PHYSICAL_DISK_AVAILABLE_AFTER_DISK_EXCLUSION: win32more.Foundation.HRESULT = -2147212268
VSS_E_ASRERROR_CRITICAL_DISK_CANNOT_BE_EXCLUDED: win32more.Foundation.HRESULT = -2147212267
VSS_E_ASRERROR_SYSTEM_PARTITION_HIDDEN: win32more.Foundation.HRESULT = -2147212266
VSS_E_FSS_TIMEOUT: win32more.Foundation.HRESULT = -2147212265
@winfunctype('VSSAPI.dll')
def CreateVssExpressWriterInternal(ppWriter: POINTER(win32more.Storage.Vss.IVssExpressWriter_head)) -> win32more.Foundation.HRESULT: ...
class IVssAdmin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('77ed5996-2f63-11d3-8a-39-00-c0-4f-72-d8-e3')
    @commethod(3)
    def RegisterProvider(pProviderId: Guid, ClassId: Guid, pwszProviderName: POINTER(UInt16), eProviderType: win32more.Storage.Vss.VSS_PROVIDER_TYPE, pwszProviderVersion: POINTER(UInt16), ProviderVersionId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterProvider(ProviderId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryProviders(ppEnum: POINTER(win32more.Storage.Vss.IVssEnumObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAllSnapshotsInProgress() -> win32more.Foundation.HRESULT: ...
class IVssAdminEx(c_void_p):
    extends: win32more.Storage.Vss.IVssAdmin
    Guid = Guid('7858a9f8-b1fa-41a6-96-4f-b9-b3-6b-8c-d8-d8')
    @commethod(7)
    def GetProviderCapability(pProviderId: Guid, pllOriginalCapabilityMask: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetProviderContext(ProviderId: Guid, plContext: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetProviderContext(ProviderId: Guid, lContext: Int32) -> win32more.Foundation.HRESULT: ...
class IVssAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('507c37b4-cf5b-4e95-b0-af-14-eb-97-67-46-7e')
    @commethod(3)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Wait(dwMilliseconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryStatus(pHrResult: POINTER(win32more.Foundation.HRESULT), pReserved: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IVssComponent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2c72c96-c121-4518-b6-27-e5-a9-3d-01-0e-ad')
    @commethod(3)
    def GetLogicalPath(pbstrPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentType(pct: POINTER(win32more.Storage.Vss.VSS_COMPONENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBackupSucceeded(pbSucceeded: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAlternateLocationMappingCount(pcMappings: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAlternateLocationMapping(iMapping: UInt32, ppFiledesc: POINTER(win32more.Storage.Vss.IVssWMFiledesc_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackupMetadata(wszData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackupMetadata(pbstrData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AddPartialFile(wszPath: win32more.Foundation.PWSTR, wszFilename: win32more.Foundation.PWSTR, wszRanges: win32more.Foundation.PWSTR, wszMetadata: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetPartialFileCount(pcPartialFiles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetPartialFile(iPartialFile: UInt32, pbstrPath: POINTER(win32more.Foundation.BSTR), pbstrFilename: POINTER(win32more.Foundation.BSTR), pbstrRange: POINTER(win32more.Foundation.BSTR), pbstrMetadata: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def IsSelectedForRestore(pbSelectedForRestore: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetAdditionalRestores(pbAdditionalRestores: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetNewTargetCount(pcNewTarget: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetNewTarget(iNewTarget: UInt32, ppFiledesc: POINTER(win32more.Storage.Vss.IVssWMFiledesc_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def AddDirectedTarget(wszSourcePath: win32more.Foundation.PWSTR, wszSourceFilename: win32more.Foundation.PWSTR, wszSourceRangeList: win32more.Foundation.PWSTR, wszDestinationPath: win32more.Foundation.PWSTR, wszDestinationFilename: win32more.Foundation.PWSTR, wszDestinationRangeList: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDirectedTargetCount(pcDirectedTarget: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetDirectedTarget(iDirectedTarget: UInt32, pbstrSourcePath: POINTER(win32more.Foundation.BSTR), pbstrSourceFileName: POINTER(win32more.Foundation.BSTR), pbstrSourceRangeList: POINTER(win32more.Foundation.BSTR), pbstrDestinationPath: POINTER(win32more.Foundation.BSTR), pbstrDestinationFilename: POINTER(win32more.Foundation.BSTR), pbstrDestinationRangeList: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetRestoreMetadata(wszRestoreMetadata: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestoreMetadata(pbstrRestoreMetadata: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetRestoreTarget(target: win32more.Storage.Vss.VSS_RESTORE_TARGET) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetRestoreTarget(pTarget: POINTER(win32more.Storage.Vss.VSS_RESTORE_TARGET)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetPreRestoreFailureMsg(wszPreRestoreFailureMsg: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetPreRestoreFailureMsg(pbstrPreRestoreFailureMsg: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetPostRestoreFailureMsg(wszPostRestoreFailureMsg: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetPostRestoreFailureMsg(pbstrPostRestoreFailureMsg: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetBackupStamp(wszBackupStamp: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetBackupStamp(pbstrBackupStamp: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetPreviousBackupStamp(pbstrBackupStamp: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetBackupOptions(pbstrBackupOptions: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetRestoreOptions(pbstrRestoreOptions: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetRestoreSubcomponentCount(pcRestoreSubcomponent: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetRestoreSubcomponent(iComponent: UInt32, pbstrLogicalPath: POINTER(win32more.Foundation.BSTR), pbstrComponentName: POINTER(win32more.Foundation.BSTR), pbRepair: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetFileRestoreStatus(pStatus: POINTER(win32more.Storage.Vss.VSS_FILE_RESTORE_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def AddDifferencedFilesByLastModifyTime(wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: win32more.Foundation.BOOL, ftLastModifyTime: win32more.Foundation.FILETIME) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def AddDifferencedFilesByLastModifyLSN(wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: win32more.Foundation.BOOL, bstrLsnString: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetDifferencedFilesCount(pcDifferencedFiles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetDifferencedFile(iDifferencedFile: UInt32, pbstrPath: POINTER(win32more.Foundation.BSTR), pbstrFilespec: POINTER(win32more.Foundation.BSTR), pbRecursive: POINTER(win32more.Foundation.BOOL), pbstrLsnString: POINTER(win32more.Foundation.BSTR), pftLastModifyTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
class IVssComponentEx(c_void_p):
    extends: win32more.Storage.Vss.IVssComponent
    Guid = Guid('156c8b5e-f131-4bd7-9c-97-d1-92-3b-e7-e1-fa')
    @commethod(41)
    def SetPrepareForBackupFailureMsg(wszFailureMsg: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SetPostSnapshotFailureMsg(wszFailureMsg: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetPrepareForBackupFailureMsg(pbstrFailureMsg: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetPostSnapshotFailureMsg(pbstrFailureMsg: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def GetAuthoritativeRestore(pbAuth: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetRollForward(pRollType: POINTER(win32more.Storage.Vss.VSS_ROLLFORWARD_TYPE), pbstrPoint: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def GetRestoreName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IVssComponentEx2(c_void_p):
    extends: win32more.Storage.Vss.IVssComponentEx
    Guid = Guid('3b5be0f2-07a9-4e4b-bd-d3-cf-dc-8e-2c-0d-2d')
    @commethod(48)
    def SetFailure(hr: win32more.Foundation.HRESULT, hrApplication: win32more.Foundation.HRESULT, wszApplicationMessage: win32more.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def GetFailure(phr: POINTER(win32more.Foundation.HRESULT), phrApplication: POINTER(win32more.Foundation.HRESULT), pbstrApplicationMessage: POINTER(win32more.Foundation.BSTR), pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVssCreateExpressWriterMetadata(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9c772e77-b26e-427f-92-dd-c9-96-f4-1e-a5-e3')
    @commethod(3)
    def AddExcludeFiles(wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddComponent(ct: win32more.Storage.Vss.VSS_COMPONENT_TYPE, wszLogicalPath: win32more.Foundation.PWSTR, wszComponentName: win32more.Foundation.PWSTR, wszCaption: win32more.Foundation.PWSTR, pbIcon: c_char_p_no, cbIcon: UInt32, bRestoreMetadata: Byte, bNotifyOnBackupComplete: Byte, bSelectable: Byte, bSelectableForRestore: Byte, dwComponentFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilesToFileGroup(wszLogicalPath: win32more.Foundation.PWSTR, wszGroupName: win32more.Foundation.PWSTR, wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRestoreMethod(method: win32more.Storage.Vss.VSS_RESTOREMETHOD_ENUM, wszService: win32more.Foundation.PWSTR, wszUserProcedure: win32more.Foundation.PWSTR, writerRestore: win32more.Storage.Vss.VSS_WRITERRESTORE_ENUM, bRebootRequired: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddComponentDependency(wszForLogicalPath: win32more.Foundation.PWSTR, wszForComponentName: win32more.Foundation.PWSTR, onWriterId: Guid, wszOnLogicalPath: win32more.Foundation.PWSTR, wszOnComponentName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetBackupSchema(dwSchemaMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SaveAsXML(pbstrXML: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IVssCreateWriterMetadata(c_void_p):
    extends: None
    @commethod(0)
    def AddIncludeFiles(wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(1)
    def AddExcludeFiles(wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(2)
    def AddComponent(ct: win32more.Storage.Vss.VSS_COMPONENT_TYPE, wszLogicalPath: win32more.Foundation.PWSTR, wszComponentName: win32more.Foundation.PWSTR, wszCaption: win32more.Foundation.PWSTR, pbIcon: c_char_p_no, cbIcon: UInt32, bRestoreMetadata: Byte, bNotifyOnBackupComplete: Byte, bSelectable: Byte, bSelectableForRestore: Byte, dwComponentFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(3)
    def AddDatabaseFiles(wszLogicalPath: win32more.Foundation.PWSTR, wszDatabaseName: win32more.Foundation.PWSTR, wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddDatabaseLogFiles(wszLogicalPath: win32more.Foundation.PWSTR, wszDatabaseName: win32more.Foundation.PWSTR, wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilesToFileGroup(wszLogicalPath: win32more.Foundation.PWSTR, wszGroupName: win32more.Foundation.PWSTR, wszPath: win32more.Foundation.PWSTR, wszFilespec: win32more.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRestoreMethod(method: win32more.Storage.Vss.VSS_RESTOREMETHOD_ENUM, wszService: win32more.Foundation.PWSTR, wszUserProcedure: win32more.Foundation.PWSTR, writerRestore: win32more.Storage.Vss.VSS_WRITERRESTORE_ENUM, bRebootRequired: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddAlternateLocationMapping(wszSourcePath: win32more.Foundation.PWSTR, wszSourceFilespec: win32more.Foundation.PWSTR, bRecursive: Byte, wszDestination: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def AddComponentDependency(wszForLogicalPath: win32more.Foundation.PWSTR, wszForComponentName: win32more.Foundation.PWSTR, onWriterId: Guid, wszOnLogicalPath: win32more.Foundation.PWSTR, wszOnComponentName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackupSchema(dwSchemaMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDocument(pDoc: POINTER(win32more.Data.Xml.MsXml.IXMLDOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SaveAsXML(pbstrXML: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('214a0f28-b737-4026-b8-47-4f-9e-37-d7-95-29')
    @commethod(3)
    def AddDiffArea(pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ChangeDiffAreaMaximumSize(pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryVolumesSupportedForDiffAreas(pwszOriginalVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def QueryDiffAreasForVolume(pwszVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def QueryDiffAreasOnVolume(pwszVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def QueryDiffAreasForSnapshot(SnapshotId: Guid, ppEnum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt2(c_void_p):
    extends: win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt
    Guid = Guid('949d7353-675f-4275-89-69-f0-44-c6-27-78-15')
    @commethod(9)
    def ChangeDiffAreaMaximumSizeEx(pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64, bVolatile: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def MigrateDiffAreas(pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), pwszNewDiffAreaVolumeName: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def QueryMigrationStatus(pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), ppAsync: POINTER(win32more.Storage.Vss.IVssAsync_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetSnapshotPriority(idSnapshot: Guid, priority: Byte) -> win32more.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt3(c_void_p):
    extends: win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt2
    Guid = Guid('383f7e71-a4c5-401f-b2-7f-f8-26-28-9f-84-58')
    @commethod(13)
    def SetVolumeProtectLevel(pwszVolumeName: POINTER(UInt16), protectionLevel: win32more.Storage.Vss.VSS_PROTECTION_LEVEL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetVolumeProtectLevel(pwszVolumeName: POINTER(UInt16), protectionLevel: POINTER(win32more.Storage.Vss.VSS_VOLUME_PROTECTION_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ClearVolumeProtectFault(pwszVolumeName: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteUnusedDiffAreas(pwszDiffAreaVolumeName: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def QuerySnapshotDeltaBitmap(idSnapshotOlder: Guid, idSnapshotYounger: Guid, pcBlockSizePerBit: POINTER(UInt32), pcBitmapLength: POINTER(UInt32), ppbBitmap: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IVssEnumMgmtObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('01954e6b-9254-4e6e-80-8c-c9-e0-5d-00-76-96')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Storage.Vss.VSS_MGMT_OBJECT_PROP_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
class IVssEnumObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ae1c7110-2f60-11d3-8a-39-00-c0-4f-72-d8-e3')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Storage.Vss.VSS_OBJECT_PROP_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.Storage.Vss.IVssEnumObject_head)) -> win32more.Foundation.HRESULT: ...
class IVssExamineWriterMetadata(Structure):
    pass
class IVssExpressWriter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e33affdc-59c7-47b1-97-d5-42-66-59-8f-62-35')
    @commethod(3)
    def CreateMetadata(writerId: Guid, writerName: win32more.Foundation.PWSTR, usageType: win32more.Storage.Vss.VSS_USAGE_TYPE, versionMajor: UInt32, versionMinor: UInt32, reserved: UInt32, ppMetadata: POINTER(win32more.Storage.Vss.IVssCreateExpressWriterMetadata_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LoadMetadata(metadata: win32more.Foundation.PWSTR, reserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Register() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Unregister(writerId: Guid) -> win32more.Foundation.HRESULT: ...
class IVssFileShareSnapshotProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c8636060-7c2e-11df-8c-4a-08-00-20-0c-9a-66')
    @commethod(3)
    def SetContext(lContext: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSnapshotProperties(SnapshotId: Guid, pProp: POINTER(win32more.Storage.Vss.VSS_SNAPSHOT_PROP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Query(QueriedObjectId: Guid, eQueriedObjectType: win32more.Storage.Vss.VSS_OBJECT_TYPE, eReturnedObjectsType: win32more.Storage.Vss.VSS_OBJECT_TYPE, ppEnum: POINTER(win32more.Storage.Vss.IVssEnumObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteSnapshots(SourceObjectId: Guid, eSourceObjectType: win32more.Storage.Vss.VSS_OBJECT_TYPE, bForceDelete: win32more.Foundation.BOOL, plDeletedSnapshots: POINTER(Int32), pNondeletedSnapshotID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginPrepareSnapshot(SnapshotSetId: Guid, SnapshotId: Guid, pwszSharePath: POINTER(UInt16), lNewContext: Int32, ProviderId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsPathSupported(pwszSharePath: POINTER(UInt16), pbSupportedByThisProvider: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsPathSnapshotted(pwszSharePath: POINTER(UInt16), pbSnapshotsPresent: POINTER(win32more.Foundation.BOOL), plSnapshotCompatibility: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetSnapshotProperty(SnapshotId: Guid, eSnapshotPropertyId: win32more.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID, vProperty: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IVssHardwareSnapshotProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9593a157-44e9-4344-bb-eb-44-fb-f9-b0-6b-10')
    @commethod(3)
    def AreLunsSupported(lLunCount: Int32, lContext: Int32, rgwszDevices: POINTER(POINTER(UInt16)), pLunInformation: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), pbIsSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FillInLunInfo(wszDeviceName: POINTER(UInt16), pLunInfo: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), pbIsSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BeginPrepareSnapshot(SnapshotSetId: Guid, SnapshotId: Guid, lContext: Int32, lLunCount: Int32, rgDeviceNames: POINTER(POINTER(UInt16)), rgLunInformation: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTargetLuns(lLunCount: Int32, rgDeviceNames: POINTER(POINTER(UInt16)), rgSourceLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), rgDestinationLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def LocateLuns(lLunCount: Int32, rgSourceLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnLunEmpty(wszDeviceName: POINTER(UInt16), pInformation: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head)) -> win32more.Foundation.HRESULT: ...
class IVssHardwareSnapshotProviderEx(c_void_p):
    extends: win32more.Storage.Vss.IVssHardwareSnapshotProvider
    Guid = Guid('7f5ba925-cdb1-4d11-a7-1f-33-9e-b7-e7-09-fd')
    @commethod(9)
    def GetProviderCapabilities(pllOriginalCapabilityMask: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnLunStateChange(pSnapshotLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), pOriginalLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), dwCount: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ResyncLuns(pSourceLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), pTargetLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), dwCount: UInt32, ppAsync: POINTER(win32more.Storage.Vss.IVssAsync_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OnReuseLuns(pSnapshotLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), pOriginalLuns: POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), dwCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IVssProviderCreateSnapshotSet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5f894e5b-1e39-4778-8e-23-9a-ba-d9-f0-e0-8c')
    @commethod(3)
    def EndPrepareSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PreCommitSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CommitSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PostCommitSnapshots(SnapshotSetId: Guid, lSnapshotsCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def PreFinalCommitSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def PostFinalCommitSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AbortSnapshots(SnapshotSetId: Guid) -> win32more.Foundation.HRESULT: ...
class IVssProviderNotifications(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e561901f-03a5-4afe-86-d0-72-ba-ee-ce-70-04')
    @commethod(3)
    def OnLoad(pCallback: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnUnload(bForceUnload: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IVssSnapshotMgmt(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fa7df749-66e7-4986-a2-7f-e2-f0-4a-e5-37-72')
    @commethod(3)
    def GetProviderMgmtInterface(ProviderId: Guid, InterfaceId: POINTER(Guid), ppItf: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def QueryVolumesSupportedForSnapshots(ProviderId: Guid, lContext: Int32, ppEnum: POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QuerySnapshotsByVolume(pwszVolumeName: POINTER(UInt16), ProviderId: Guid, ppEnum: POINTER(win32more.Storage.Vss.IVssEnumObject_head)) -> win32more.Foundation.HRESULT: ...
class IVssSnapshotMgmt2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0f61ec39-fe82-45f2-a3-f0-76-8b-5d-42-71-02')
    @commethod(3)
    def GetMinDiffAreaSize(pllMinDiffAreaSize: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
class IVssSoftwareSnapshotProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('609e123e-2c5a-44d3-8f-01-0b-1d-9a-47-d1-ff')
    @commethod(3)
    def SetContext(lContext: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSnapshotProperties(SnapshotId: Guid, pProp: POINTER(win32more.Storage.Vss.VSS_SNAPSHOT_PROP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Query(QueriedObjectId: Guid, eQueriedObjectType: win32more.Storage.Vss.VSS_OBJECT_TYPE, eReturnedObjectsType: win32more.Storage.Vss.VSS_OBJECT_TYPE, ppEnum: POINTER(win32more.Storage.Vss.IVssEnumObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteSnapshots(SourceObjectId: Guid, eSourceObjectType: win32more.Storage.Vss.VSS_OBJECT_TYPE, bForceDelete: win32more.Foundation.BOOL, plDeletedSnapshots: POINTER(Int32), pNondeletedSnapshotID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginPrepareSnapshot(SnapshotSetId: Guid, SnapshotId: Guid, pwszVolumeName: POINTER(UInt16), lNewContext: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsVolumeSupported(pwszVolumeName: POINTER(UInt16), pbSupportedByThisProvider: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsVolumeSnapshotted(pwszVolumeName: POINTER(UInt16), pbSnapshotsPresent: POINTER(win32more.Foundation.BOOL), plSnapshotCompatibility: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetSnapshotProperty(SnapshotId: Guid, eSnapshotPropertyId: win32more.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID, vProperty: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RevertToSnapshot(SnapshotId: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def QueryRevertStatus(pwszVolume: POINTER(UInt16), ppAsync: POINTER(win32more.Storage.Vss.IVssAsync_head)) -> win32more.Foundation.HRESULT: ...
class IVssWMDependency(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetWriterId(pWriterId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLogicalPath(pbstrLogicalPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentName(pbstrComponentName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IVssWMFiledesc(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetPath(pbstrPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFilespec(pbstrFilespec: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecursive(pbRecursive: POINTER(Boolean)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAlternateLocation(pbstrAlternateLocation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetBackupTypeMask(pdwTypeMask: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IVssWriterComponents(c_void_p):
    extends: None
    @commethod(0)
    def GetComponentCount(pcComponents: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(1)
    def GetWriterInfo(pidInstance: POINTER(Guid), pidWriter: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(2)
    def GetComponent(iComponent: UInt32, ppComponent: POINTER(win32more.Storage.Vss.IVssComponent_head)) -> win32more.Foundation.HRESULT: ...
class IVssWriterImpl(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def Initialize(writerId: Guid, wszWriterName: win32more.Foundation.PWSTR, wszWriterInstanceName: win32more.Foundation.PWSTR, dwMajorVersion: UInt32, dwMinorVersion: UInt32, ut: win32more.Storage.Vss.VSS_USAGE_TYPE, st: win32more.Storage.Vss.VSS_SOURCE_TYPE, nLevel: win32more.Storage.Vss.VSS_APPLICATION_LEVEL, dwTimeout: UInt32, aws: win32more.Storage.Vss.VSS_ALTERNATE_WRITER_STATE, bIOThrottlingOnly: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Subscribe(dwSubscribeTimeout: UInt32, dwEventFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Unsubscribe() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Uninitialize() -> Void: ...
    @commethod(7)
    def GetCurrentVolumeArray() -> POINTER(win32more.Foundation.PWSTR): ...
    @commethod(8)
    def GetCurrentVolumeCount() -> UInt32: ...
    @commethod(9)
    def GetSnapshotDeviceName(wszOriginalVolume: win32more.Foundation.PWSTR, ppwszSnapshotDevice: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentSnapshotSetId() -> Guid: ...
    @commethod(11)
    def GetContext() -> Int32: ...
    @commethod(12)
    def GetCurrentLevel() -> win32more.Storage.Vss.VSS_APPLICATION_LEVEL: ...
    @commethod(13)
    def IsPathAffected(wszPath: win32more.Foundation.PWSTR) -> Boolean: ...
    @commethod(14)
    def IsBootableSystemStateBackedUp() -> Boolean: ...
    @commethod(15)
    def AreComponentsSelected() -> Boolean: ...
    @commethod(16)
    def GetBackupType() -> win32more.Storage.Vss.VSS_BACKUP_TYPE: ...
    @commethod(17)
    def GetRestoreType() -> win32more.Storage.Vss.VSS_RESTORE_TYPE: ...
    @commethod(18)
    def SetWriterFailure(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def IsPartialFileSupportEnabled() -> Boolean: ...
    @commethod(20)
    def InstallAlternateWriter(idWriter: Guid, clsid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetIdentityInformation() -> POINTER(win32more.Storage.Vss.IVssExamineWriterMetadata_head): ...
    @commethod(22)
    def SetWriterFailureEx(hr: win32more.Foundation.HRESULT, hrApplication: win32more.Foundation.HRESULT, wszApplicationMessage: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetSessionId(idSession: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def IsWriterShuttingDown() -> Boolean: ...
VSSCoordinator = Guid('e579ab5f-1cc4-44b4-be-d9-de-09-91-ff-06-23')
VSS_ALTERNATE_WRITER_STATE = Int32
VSS_AWS_UNDEFINED: VSS_ALTERNATE_WRITER_STATE = 0
VSS_AWS_NO_ALTERNATE_WRITER: VSS_ALTERNATE_WRITER_STATE = 1
VSS_AWS_ALTERNATE_WRITER_EXISTS: VSS_ALTERNATE_WRITER_STATE = 2
VSS_AWS_THIS_IS_ALTERNATE_WRITER: VSS_ALTERNATE_WRITER_STATE = 3
VSS_APPLICATION_LEVEL = Int32
VSS_APP_UNKNOWN: VSS_APPLICATION_LEVEL = 0
VSS_APP_SYSTEM: VSS_APPLICATION_LEVEL = 1
VSS_APP_BACK_END: VSS_APPLICATION_LEVEL = 2
VSS_APP_FRONT_END: VSS_APPLICATION_LEVEL = 3
VSS_APP_SYSTEM_RM: VSS_APPLICATION_LEVEL = 4
VSS_APP_AUTO: VSS_APPLICATION_LEVEL = -1
VSS_BACKUP_SCHEMA = Int32
VSS_BS_UNDEFINED: VSS_BACKUP_SCHEMA = 0
VSS_BS_DIFFERENTIAL: VSS_BACKUP_SCHEMA = 1
VSS_BS_INCREMENTAL: VSS_BACKUP_SCHEMA = 2
VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL: VSS_BACKUP_SCHEMA = 4
VSS_BS_LOG: VSS_BACKUP_SCHEMA = 8
VSS_BS_COPY: VSS_BACKUP_SCHEMA = 16
VSS_BS_TIMESTAMPED: VSS_BACKUP_SCHEMA = 32
VSS_BS_LAST_MODIFY: VSS_BACKUP_SCHEMA = 64
VSS_BS_LSN: VSS_BACKUP_SCHEMA = 128
VSS_BS_WRITER_SUPPORTS_NEW_TARGET: VSS_BACKUP_SCHEMA = 256
VSS_BS_WRITER_SUPPORTS_RESTORE_WITH_MOVE: VSS_BACKUP_SCHEMA = 512
VSS_BS_INDEPENDENT_SYSTEM_STATE: VSS_BACKUP_SCHEMA = 1024
VSS_BS_ROLLFORWARD_RESTORE: VSS_BACKUP_SCHEMA = 4096
VSS_BS_RESTORE_RENAME: VSS_BACKUP_SCHEMA = 8192
VSS_BS_AUTHORITATIVE_RESTORE: VSS_BACKUP_SCHEMA = 16384
VSS_BS_WRITER_SUPPORTS_PARALLEL_RESTORES: VSS_BACKUP_SCHEMA = 32768
VSS_BACKUP_TYPE = Int32
VSS_BT_UNDEFINED: VSS_BACKUP_TYPE = 0
VSS_BT_FULL: VSS_BACKUP_TYPE = 1
VSS_BT_INCREMENTAL: VSS_BACKUP_TYPE = 2
VSS_BT_DIFFERENTIAL: VSS_BACKUP_TYPE = 3
VSS_BT_LOG: VSS_BACKUP_TYPE = 4
VSS_BT_COPY: VSS_BACKUP_TYPE = 5
VSS_BT_OTHER: VSS_BACKUP_TYPE = 6
VSS_COMPONENT_FLAGS = Int32
VSS_CF_BACKUP_RECOVERY: VSS_COMPONENT_FLAGS = 1
VSS_CF_APP_ROLLBACK_RECOVERY: VSS_COMPONENT_FLAGS = 2
VSS_CF_NOT_SYSTEM_STATE: VSS_COMPONENT_FLAGS = 4
VSS_COMPONENT_TYPE = Int32
VSS_CT_UNDEFINED: VSS_COMPONENT_TYPE = 0
VSS_CT_DATABASE: VSS_COMPONENT_TYPE = 1
VSS_CT_FILEGROUP: VSS_COMPONENT_TYPE = 2
class VSS_DIFF_AREA_PROP(Structure):
    m_pwszVolumeName: POINTER(UInt16)
    m_pwszDiffAreaVolumeName: POINTER(UInt16)
    m_llMaximumDiffSpace: Int64
    m_llAllocatedDiffSpace: Int64
    m_llUsedDiffSpace: Int64
class VSS_DIFF_VOLUME_PROP(Structure):
    m_pwszVolumeName: POINTER(UInt16)
    m_pwszVolumeDisplayName: POINTER(UInt16)
    m_llVolumeFreeSpace: Int64
    m_llVolumeTotalSpace: Int64
VSS_FILE_RESTORE_STATUS = Int32
VSS_RS_UNDEFINED: VSS_FILE_RESTORE_STATUS = 0
VSS_RS_NONE: VSS_FILE_RESTORE_STATUS = 1
VSS_RS_ALL: VSS_FILE_RESTORE_STATUS = 2
VSS_RS_FAILED: VSS_FILE_RESTORE_STATUS = 3
VSS_FILE_SPEC_BACKUP_TYPE = Int32
VSS_FSBT_FULL_BACKUP_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 1
VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 2
VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 4
VSS_FSBT_LOG_BACKUP_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 8
VSS_FSBT_FULL_SNAPSHOT_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 256
VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 512
VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 1024
VSS_FSBT_LOG_SNAPSHOT_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 2048
VSS_FSBT_CREATED_DURING_BACKUP: VSS_FILE_SPEC_BACKUP_TYPE = 65536
VSS_FSBT_ALL_BACKUP_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 15
VSS_FSBT_ALL_SNAPSHOT_REQUIRED: VSS_FILE_SPEC_BACKUP_TYPE = 3840
VSS_HARDWARE_OPTIONS = Int32
VSS_BREAKEX_FLAG_MASK_LUNS: VSS_HARDWARE_OPTIONS = 1
VSS_BREAKEX_FLAG_MAKE_READ_WRITE: VSS_HARDWARE_OPTIONS = 2
VSS_BREAKEX_FLAG_REVERT_IDENTITY_ALL: VSS_HARDWARE_OPTIONS = 4
VSS_BREAKEX_FLAG_REVERT_IDENTITY_NONE: VSS_HARDWARE_OPTIONS = 8
VSS_ONLUNSTATECHANGE_NOTIFY_READ_WRITE: VSS_HARDWARE_OPTIONS = 256
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_PRE_RECOVERY: VSS_HARDWARE_OPTIONS = 512
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_POST_RECOVERY: VSS_HARDWARE_OPTIONS = 1024
VSS_ONLUNSTATECHANGE_DO_MASK_LUNS: VSS_HARDWARE_OPTIONS = 2048
class VSS_MGMT_OBJECT_PROP(Structure):
    Type: win32more.Storage.Vss.VSS_MGMT_OBJECT_TYPE
    Obj: win32more.Storage.Vss.VSS_MGMT_OBJECT_UNION
VSS_MGMT_OBJECT_TYPE = Int32
VSS_MGMT_OBJECT_UNKNOWN: VSS_MGMT_OBJECT_TYPE = 0
VSS_MGMT_OBJECT_VOLUME: VSS_MGMT_OBJECT_TYPE = 1
VSS_MGMT_OBJECT_DIFF_VOLUME: VSS_MGMT_OBJECT_TYPE = 2
VSS_MGMT_OBJECT_DIFF_AREA: VSS_MGMT_OBJECT_TYPE = 3
class VSS_MGMT_OBJECT_UNION(Union):
    Vol: win32more.Storage.Vss.VSS_VOLUME_PROP
    DiffVol: win32more.Storage.Vss.VSS_DIFF_VOLUME_PROP
    DiffArea: win32more.Storage.Vss.VSS_DIFF_AREA_PROP
class VSS_OBJECT_PROP(Structure):
    Type: win32more.Storage.Vss.VSS_OBJECT_TYPE
    Obj: win32more.Storage.Vss.VSS_OBJECT_UNION
VSS_OBJECT_TYPE = Int32
VSS_OBJECT_UNKNOWN: VSS_OBJECT_TYPE = 0
VSS_OBJECT_NONE: VSS_OBJECT_TYPE = 1
VSS_OBJECT_SNAPSHOT_SET: VSS_OBJECT_TYPE = 2
VSS_OBJECT_SNAPSHOT: VSS_OBJECT_TYPE = 3
VSS_OBJECT_PROVIDER: VSS_OBJECT_TYPE = 4
VSS_OBJECT_TYPE_COUNT: VSS_OBJECT_TYPE = 5
class VSS_OBJECT_UNION(Union):
    Snap: win32more.Storage.Vss.VSS_SNAPSHOT_PROP
    Prov: win32more.Storage.Vss.VSS_PROVIDER_PROP
VSS_PROTECTION_FAULT = Int32
VSS_PROTECTION_FAULT_NONE: VSS_PROTECTION_FAULT = 0
VSS_PROTECTION_FAULT_DIFF_AREA_MISSING: VSS_PROTECTION_FAULT = 1
VSS_PROTECTION_FAULT_IO_FAILURE_DURING_ONLINE: VSS_PROTECTION_FAULT = 2
VSS_PROTECTION_FAULT_META_DATA_CORRUPTION: VSS_PROTECTION_FAULT = 3
VSS_PROTECTION_FAULT_MEMORY_ALLOCATION_FAILURE: VSS_PROTECTION_FAULT = 4
VSS_PROTECTION_FAULT_MAPPED_MEMORY_FAILURE: VSS_PROTECTION_FAULT = 5
VSS_PROTECTION_FAULT_COW_READ_FAILURE: VSS_PROTECTION_FAULT = 6
VSS_PROTECTION_FAULT_COW_WRITE_FAILURE: VSS_PROTECTION_FAULT = 7
VSS_PROTECTION_FAULT_DIFF_AREA_FULL: VSS_PROTECTION_FAULT = 8
VSS_PROTECTION_FAULT_GROW_TOO_SLOW: VSS_PROTECTION_FAULT = 9
VSS_PROTECTION_FAULT_GROW_FAILED: VSS_PROTECTION_FAULT = 10
VSS_PROTECTION_FAULT_DESTROY_ALL_SNAPSHOTS: VSS_PROTECTION_FAULT = 11
VSS_PROTECTION_FAULT_FILE_SYSTEM_FAILURE: VSS_PROTECTION_FAULT = 12
VSS_PROTECTION_FAULT_IO_FAILURE: VSS_PROTECTION_FAULT = 13
VSS_PROTECTION_FAULT_DIFF_AREA_REMOVED: VSS_PROTECTION_FAULT = 14
VSS_PROTECTION_FAULT_EXTERNAL_WRITER_TO_DIFF_AREA: VSS_PROTECTION_FAULT = 15
VSS_PROTECTION_FAULT_MOUNT_DURING_CLUSTER_OFFLINE: VSS_PROTECTION_FAULT = 16
VSS_PROTECTION_LEVEL = Int32
VSS_PROTECTION_LEVEL_ORIGINAL_VOLUME: VSS_PROTECTION_LEVEL = 0
VSS_PROTECTION_LEVEL_SNAPSHOT: VSS_PROTECTION_LEVEL = 1
VSS_PROVIDER_CAPABILITIES = Int32
VSS_PRV_CAPABILITY_LEGACY: VSS_PROVIDER_CAPABILITIES = 1
VSS_PRV_CAPABILITY_COMPLIANT: VSS_PROVIDER_CAPABILITIES = 2
VSS_PRV_CAPABILITY_LUN_REPOINT: VSS_PROVIDER_CAPABILITIES = 4
VSS_PRV_CAPABILITY_LUN_RESYNC: VSS_PROVIDER_CAPABILITIES = 8
VSS_PRV_CAPABILITY_OFFLINE_CREATION: VSS_PROVIDER_CAPABILITIES = 16
VSS_PRV_CAPABILITY_MULTIPLE_IMPORT: VSS_PROVIDER_CAPABILITIES = 32
VSS_PRV_CAPABILITY_RECYCLING: VSS_PROVIDER_CAPABILITIES = 64
VSS_PRV_CAPABILITY_PLEX: VSS_PROVIDER_CAPABILITIES = 128
VSS_PRV_CAPABILITY_DIFFERENTIAL: VSS_PROVIDER_CAPABILITIES = 256
VSS_PRV_CAPABILITY_CLUSTERED: VSS_PROVIDER_CAPABILITIES = 512
class VSS_PROVIDER_PROP(Structure):
    m_ProviderId: Guid
    m_pwszProviderName: POINTER(UInt16)
    m_eProviderType: win32more.Storage.Vss.VSS_PROVIDER_TYPE
    m_pwszProviderVersion: POINTER(UInt16)
    m_ProviderVersionId: Guid
    m_ClassId: Guid
VSS_PROVIDER_TYPE = Int32
VSS_PROV_UNKNOWN: VSS_PROVIDER_TYPE = 0
VSS_PROV_SYSTEM: VSS_PROVIDER_TYPE = 1
VSS_PROV_SOFTWARE: VSS_PROVIDER_TYPE = 2
VSS_PROV_HARDWARE: VSS_PROVIDER_TYPE = 3
VSS_PROV_FILESHARE: VSS_PROVIDER_TYPE = 4
VSS_RECOVERY_OPTIONS = Int32
VSS_RECOVERY_REVERT_IDENTITY_ALL: VSS_RECOVERY_OPTIONS = 256
VSS_RECOVERY_NO_VOLUME_CHECK: VSS_RECOVERY_OPTIONS = 512
VSS_RESTOREMETHOD_ENUM = Int32
VSS_RME_UNDEFINED: VSS_RESTOREMETHOD_ENUM = 0
VSS_RME_RESTORE_IF_NOT_THERE: VSS_RESTOREMETHOD_ENUM = 1
VSS_RME_RESTORE_IF_CAN_REPLACE: VSS_RESTOREMETHOD_ENUM = 2
VSS_RME_STOP_RESTORE_START: VSS_RESTOREMETHOD_ENUM = 3
VSS_RME_RESTORE_TO_ALTERNATE_LOCATION: VSS_RESTOREMETHOD_ENUM = 4
VSS_RME_RESTORE_AT_REBOOT: VSS_RESTOREMETHOD_ENUM = 5
VSS_RME_RESTORE_AT_REBOOT_IF_CANNOT_REPLACE: VSS_RESTOREMETHOD_ENUM = 6
VSS_RME_CUSTOM: VSS_RESTOREMETHOD_ENUM = 7
VSS_RME_RESTORE_STOP_START: VSS_RESTOREMETHOD_ENUM = 8
VSS_RESTORE_TARGET = Int32
VSS_RT_UNDEFINED: VSS_RESTORE_TARGET = 0
VSS_RT_ORIGINAL: VSS_RESTORE_TARGET = 1
VSS_RT_ALTERNATE: VSS_RESTORE_TARGET = 2
VSS_RT_DIRECTED: VSS_RESTORE_TARGET = 3
VSS_RT_ORIGINAL_LOCATION: VSS_RESTORE_TARGET = 4
VSS_RESTORE_TYPE = Int32
VSS_RTYPE_UNDEFINED: VSS_RESTORE_TYPE = 0
VSS_RTYPE_BY_COPY: VSS_RESTORE_TYPE = 1
VSS_RTYPE_IMPORT: VSS_RESTORE_TYPE = 2
VSS_RTYPE_OTHER: VSS_RESTORE_TYPE = 3
VSS_ROLLFORWARD_TYPE = Int32
VSS_RF_UNDEFINED: VSS_ROLLFORWARD_TYPE = 0
VSS_RF_NONE: VSS_ROLLFORWARD_TYPE = 1
VSS_RF_ALL: VSS_ROLLFORWARD_TYPE = 2
VSS_RF_PARTIAL: VSS_ROLLFORWARD_TYPE = 3
VSS_SNAPSHOT_COMPATIBILITY = Int32
VSS_SC_DISABLE_DEFRAG: VSS_SNAPSHOT_COMPATIBILITY = 1
VSS_SC_DISABLE_CONTENTINDEX: VSS_SNAPSHOT_COMPATIBILITY = 2
VSS_SNAPSHOT_CONTEXT = Int32
VSS_CTX_BACKUP: VSS_SNAPSHOT_CONTEXT = 0
VSS_CTX_FILE_SHARE_BACKUP: VSS_SNAPSHOT_CONTEXT = 16
VSS_CTX_NAS_ROLLBACK: VSS_SNAPSHOT_CONTEXT = 25
VSS_CTX_APP_ROLLBACK: VSS_SNAPSHOT_CONTEXT = 9
VSS_CTX_CLIENT_ACCESSIBLE: VSS_SNAPSHOT_CONTEXT = 29
VSS_CTX_CLIENT_ACCESSIBLE_WRITERS: VSS_SNAPSHOT_CONTEXT = 13
VSS_CTX_ALL: VSS_SNAPSHOT_CONTEXT = -1
class VSS_SNAPSHOT_PROP(Structure):
    m_SnapshotId: Guid
    m_SnapshotSetId: Guid
    m_lSnapshotsCount: Int32
    m_pwszSnapshotDeviceObject: POINTER(UInt16)
    m_pwszOriginalVolumeName: POINTER(UInt16)
    m_pwszOriginatingMachine: POINTER(UInt16)
    m_pwszServiceMachine: POINTER(UInt16)
    m_pwszExposedName: POINTER(UInt16)
    m_pwszExposedPath: POINTER(UInt16)
    m_ProviderId: Guid
    m_lSnapshotAttributes: Int32
    m_tsCreationTimestamp: Int64
    m_eStatus: win32more.Storage.Vss.VSS_SNAPSHOT_STATE
VSS_SNAPSHOT_PROPERTY_ID = Int32
VSS_SPROPID_UNKNOWN: VSS_SNAPSHOT_PROPERTY_ID = 0
VSS_SPROPID_SNAPSHOT_ID: VSS_SNAPSHOT_PROPERTY_ID = 1
VSS_SPROPID_SNAPSHOT_SET_ID: VSS_SNAPSHOT_PROPERTY_ID = 2
VSS_SPROPID_SNAPSHOTS_COUNT: VSS_SNAPSHOT_PROPERTY_ID = 3
VSS_SPROPID_SNAPSHOT_DEVICE: VSS_SNAPSHOT_PROPERTY_ID = 4
VSS_SPROPID_ORIGINAL_VOLUME: VSS_SNAPSHOT_PROPERTY_ID = 5
VSS_SPROPID_ORIGINATING_MACHINE: VSS_SNAPSHOT_PROPERTY_ID = 6
VSS_SPROPID_SERVICE_MACHINE: VSS_SNAPSHOT_PROPERTY_ID = 7
VSS_SPROPID_EXPOSED_NAME: VSS_SNAPSHOT_PROPERTY_ID = 8
VSS_SPROPID_EXPOSED_PATH: VSS_SNAPSHOT_PROPERTY_ID = 9
VSS_SPROPID_PROVIDER_ID: VSS_SNAPSHOT_PROPERTY_ID = 10
VSS_SPROPID_SNAPSHOT_ATTRIBUTES: VSS_SNAPSHOT_PROPERTY_ID = 11
VSS_SPROPID_CREATION_TIMESTAMP: VSS_SNAPSHOT_PROPERTY_ID = 12
VSS_SPROPID_STATUS: VSS_SNAPSHOT_PROPERTY_ID = 13
VSS_SNAPSHOT_STATE = Int32
VSS_SS_UNKNOWN: VSS_SNAPSHOT_STATE = 0
VSS_SS_PREPARING: VSS_SNAPSHOT_STATE = 1
VSS_SS_PROCESSING_PREPARE: VSS_SNAPSHOT_STATE = 2
VSS_SS_PREPARED: VSS_SNAPSHOT_STATE = 3
VSS_SS_PROCESSING_PRECOMMIT: VSS_SNAPSHOT_STATE = 4
VSS_SS_PRECOMMITTED: VSS_SNAPSHOT_STATE = 5
VSS_SS_PROCESSING_COMMIT: VSS_SNAPSHOT_STATE = 6
VSS_SS_COMMITTED: VSS_SNAPSHOT_STATE = 7
VSS_SS_PROCESSING_POSTCOMMIT: VSS_SNAPSHOT_STATE = 8
VSS_SS_PROCESSING_PREFINALCOMMIT: VSS_SNAPSHOT_STATE = 9
VSS_SS_PREFINALCOMMITTED: VSS_SNAPSHOT_STATE = 10
VSS_SS_PROCESSING_POSTFINALCOMMIT: VSS_SNAPSHOT_STATE = 11
VSS_SS_CREATED: VSS_SNAPSHOT_STATE = 12
VSS_SS_ABORTED: VSS_SNAPSHOT_STATE = 13
VSS_SS_DELETED: VSS_SNAPSHOT_STATE = 14
VSS_SS_POSTCOMMITTED: VSS_SNAPSHOT_STATE = 15
VSS_SS_COUNT: VSS_SNAPSHOT_STATE = 16
VSS_SOURCE_TYPE = Int32
VSS_ST_UNDEFINED: VSS_SOURCE_TYPE = 0
VSS_ST_TRANSACTEDDB: VSS_SOURCE_TYPE = 1
VSS_ST_NONTRANSACTEDDB: VSS_SOURCE_TYPE = 2
VSS_ST_OTHER: VSS_SOURCE_TYPE = 3
VSS_SUBSCRIBE_MASK = Int32
VSS_SM_POST_SNAPSHOT_FLAG: VSS_SUBSCRIBE_MASK = 1
VSS_SM_BACKUP_EVENTS_FLAG: VSS_SUBSCRIBE_MASK = 2
VSS_SM_RESTORE_EVENTS_FLAG: VSS_SUBSCRIBE_MASK = 4
VSS_SM_IO_THROTTLING_FLAG: VSS_SUBSCRIBE_MASK = 8
VSS_SM_ALL_FLAGS: VSS_SUBSCRIBE_MASK = -1
VSS_USAGE_TYPE = Int32
VSS_UT_UNDEFINED: VSS_USAGE_TYPE = 0
VSS_UT_BOOTABLESYSTEMSTATE: VSS_USAGE_TYPE = 1
VSS_UT_SYSTEMSERVICE: VSS_USAGE_TYPE = 2
VSS_UT_USERDATA: VSS_USAGE_TYPE = 3
VSS_UT_OTHER: VSS_USAGE_TYPE = 4
class VSS_VOLUME_PROP(Structure):
    m_pwszVolumeName: POINTER(UInt16)
    m_pwszVolumeDisplayName: POINTER(UInt16)
class VSS_VOLUME_PROTECTION_INFO(Structure):
    m_protectionLevel: win32more.Storage.Vss.VSS_PROTECTION_LEVEL
    m_volumeIsOfflineForProtection: win32more.Foundation.BOOL
    m_protectionFault: win32more.Storage.Vss.VSS_PROTECTION_FAULT
    m_failureStatus: Int32
    m_volumeHasUnusedDiffArea: win32more.Foundation.BOOL
    m_reserved: UInt32
VSS_VOLUME_SNAPSHOT_ATTRIBUTES = Int32
VSS_VOLSNAP_ATTR_PERSISTENT: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 1
VSS_VOLSNAP_ATTR_NO_AUTORECOVERY: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 2
VSS_VOLSNAP_ATTR_CLIENT_ACCESSIBLE: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 4
VSS_VOLSNAP_ATTR_NO_AUTO_RELEASE: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 8
VSS_VOLSNAP_ATTR_NO_WRITERS: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 16
VSS_VOLSNAP_ATTR_TRANSPORTABLE: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 32
VSS_VOLSNAP_ATTR_NOT_SURFACED: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 64
VSS_VOLSNAP_ATTR_NOT_TRANSACTED: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 128
VSS_VOLSNAP_ATTR_HARDWARE_ASSISTED: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 65536
VSS_VOLSNAP_ATTR_DIFFERENTIAL: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 131072
VSS_VOLSNAP_ATTR_PLEX: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 262144
VSS_VOLSNAP_ATTR_IMPORTED: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 524288
VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 1048576
VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 2097152
VSS_VOLSNAP_ATTR_AUTORECOVER: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 4194304
VSS_VOLSNAP_ATTR_ROLLBACK_RECOVERY: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 8388608
VSS_VOLSNAP_ATTR_DELAYED_POSTSNAPSHOT: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 16777216
VSS_VOLSNAP_ATTR_TXF_RECOVERY: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 33554432
VSS_VOLSNAP_ATTR_FILE_SHARE: VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 67108864
VSS_WRITERRESTORE_ENUM = Int32
VSS_WRE_UNDEFINED: VSS_WRITERRESTORE_ENUM = 0
VSS_WRE_NEVER: VSS_WRITERRESTORE_ENUM = 1
VSS_WRE_IF_REPLACE_FAILS: VSS_WRITERRESTORE_ENUM = 2
VSS_WRE_ALWAYS: VSS_WRITERRESTORE_ENUM = 3
VSS_WRITER_STATE = Int32
VSS_WS_UNKNOWN: VSS_WRITER_STATE = 0
VSS_WS_STABLE: VSS_WRITER_STATE = 1
VSS_WS_WAITING_FOR_FREEZE: VSS_WRITER_STATE = 2
VSS_WS_WAITING_FOR_THAW: VSS_WRITER_STATE = 3
VSS_WS_WAITING_FOR_POST_SNAPSHOT: VSS_WRITER_STATE = 4
VSS_WS_WAITING_FOR_BACKUP_COMPLETE: VSS_WRITER_STATE = 5
VSS_WS_FAILED_AT_IDENTIFY: VSS_WRITER_STATE = 6
VSS_WS_FAILED_AT_PREPARE_BACKUP: VSS_WRITER_STATE = 7
VSS_WS_FAILED_AT_PREPARE_SNAPSHOT: VSS_WRITER_STATE = 8
VSS_WS_FAILED_AT_FREEZE: VSS_WRITER_STATE = 9
VSS_WS_FAILED_AT_THAW: VSS_WRITER_STATE = 10
VSS_WS_FAILED_AT_POST_SNAPSHOT: VSS_WRITER_STATE = 11
VSS_WS_FAILED_AT_BACKUP_COMPLETE: VSS_WRITER_STATE = 12
VSS_WS_FAILED_AT_PRE_RESTORE: VSS_WRITER_STATE = 13
VSS_WS_FAILED_AT_POST_RESTORE: VSS_WRITER_STATE = 14
VSS_WS_FAILED_AT_BACKUPSHUTDOWN: VSS_WRITER_STATE = 15
VSS_WS_COUNT: VSS_WRITER_STATE = 16
VssSnapshotMgmt = Guid('0b5a2c52-3eb9-470a-96-e2-6c-6d-45-70-e4-0f')
make_head(_module, 'IVssAdmin')
make_head(_module, 'IVssAdminEx')
make_head(_module, 'IVssAsync')
make_head(_module, 'IVssComponent')
make_head(_module, 'IVssComponentEx')
make_head(_module, 'IVssComponentEx2')
make_head(_module, 'IVssCreateExpressWriterMetadata')
make_head(_module, 'IVssCreateWriterMetadata')
make_head(_module, 'IVssDifferentialSoftwareSnapshotMgmt')
make_head(_module, 'IVssDifferentialSoftwareSnapshotMgmt2')
make_head(_module, 'IVssDifferentialSoftwareSnapshotMgmt3')
make_head(_module, 'IVssEnumMgmtObject')
make_head(_module, 'IVssEnumObject')
make_head(_module, 'IVssExamineWriterMetadata')
make_head(_module, 'IVssExpressWriter')
make_head(_module, 'IVssFileShareSnapshotProvider')
make_head(_module, 'IVssHardwareSnapshotProvider')
make_head(_module, 'IVssHardwareSnapshotProviderEx')
make_head(_module, 'IVssProviderCreateSnapshotSet')
make_head(_module, 'IVssProviderNotifications')
make_head(_module, 'IVssSnapshotMgmt')
make_head(_module, 'IVssSnapshotMgmt2')
make_head(_module, 'IVssSoftwareSnapshotProvider')
make_head(_module, 'IVssWMDependency')
make_head(_module, 'IVssWMFiledesc')
make_head(_module, 'IVssWriterComponents')
make_head(_module, 'IVssWriterImpl')
make_head(_module, 'VSS_DIFF_AREA_PROP')
make_head(_module, 'VSS_DIFF_VOLUME_PROP')
make_head(_module, 'VSS_MGMT_OBJECT_PROP')
make_head(_module, 'VSS_MGMT_OBJECT_UNION')
make_head(_module, 'VSS_OBJECT_PROP')
make_head(_module, 'VSS_OBJECT_UNION')
make_head(_module, 'VSS_PROVIDER_PROP')
make_head(_module, 'VSS_SNAPSHOT_PROP')
make_head(_module, 'VSS_VOLUME_PROP')
make_head(_module, 'VSS_VOLUME_PROTECTION_INFO')
__all__ = [
    "CreateVssExpressWriterInternal",
    "IVssAdmin",
    "IVssAdminEx",
    "IVssAsync",
    "IVssComponent",
    "IVssComponentEx",
    "IVssComponentEx2",
    "IVssCreateExpressWriterMetadata",
    "IVssCreateWriterMetadata",
    "IVssDifferentialSoftwareSnapshotMgmt",
    "IVssDifferentialSoftwareSnapshotMgmt2",
    "IVssDifferentialSoftwareSnapshotMgmt3",
    "IVssEnumMgmtObject",
    "IVssEnumObject",
    "IVssExamineWriterMetadata",
    "IVssExpressWriter",
    "IVssFileShareSnapshotProvider",
    "IVssHardwareSnapshotProvider",
    "IVssHardwareSnapshotProviderEx",
    "IVssProviderCreateSnapshotSet",
    "IVssProviderNotifications",
    "IVssSnapshotMgmt",
    "IVssSnapshotMgmt2",
    "IVssSoftwareSnapshotProvider",
    "IVssWMDependency",
    "IVssWMFiledesc",
    "IVssWriterComponents",
    "IVssWriterImpl",
    "VSSCoordinator",
    "VSS_ALTERNATE_WRITER_STATE",
    "VSS_APPLICATION_LEVEL",
    "VSS_APP_AUTO",
    "VSS_APP_BACK_END",
    "VSS_APP_FRONT_END",
    "VSS_APP_SYSTEM",
    "VSS_APP_SYSTEM_RM",
    "VSS_APP_UNKNOWN",
    "VSS_ASSOC_NO_MAX_SPACE",
    "VSS_ASSOC_REMOVE",
    "VSS_AWS_ALTERNATE_WRITER_EXISTS",
    "VSS_AWS_NO_ALTERNATE_WRITER",
    "VSS_AWS_THIS_IS_ALTERNATE_WRITER",
    "VSS_AWS_UNDEFINED",
    "VSS_BACKUP_SCHEMA",
    "VSS_BACKUP_TYPE",
    "VSS_BREAKEX_FLAG_MAKE_READ_WRITE",
    "VSS_BREAKEX_FLAG_MASK_LUNS",
    "VSS_BREAKEX_FLAG_REVERT_IDENTITY_ALL",
    "VSS_BREAKEX_FLAG_REVERT_IDENTITY_NONE",
    "VSS_BS_AUTHORITATIVE_RESTORE",
    "VSS_BS_COPY",
    "VSS_BS_DIFFERENTIAL",
    "VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL",
    "VSS_BS_INCREMENTAL",
    "VSS_BS_INDEPENDENT_SYSTEM_STATE",
    "VSS_BS_LAST_MODIFY",
    "VSS_BS_LOG",
    "VSS_BS_LSN",
    "VSS_BS_RESTORE_RENAME",
    "VSS_BS_ROLLFORWARD_RESTORE",
    "VSS_BS_TIMESTAMPED",
    "VSS_BS_UNDEFINED",
    "VSS_BS_WRITER_SUPPORTS_NEW_TARGET",
    "VSS_BS_WRITER_SUPPORTS_PARALLEL_RESTORES",
    "VSS_BS_WRITER_SUPPORTS_RESTORE_WITH_MOVE",
    "VSS_BT_COPY",
    "VSS_BT_DIFFERENTIAL",
    "VSS_BT_FULL",
    "VSS_BT_INCREMENTAL",
    "VSS_BT_LOG",
    "VSS_BT_OTHER",
    "VSS_BT_UNDEFINED",
    "VSS_CF_APP_ROLLBACK_RECOVERY",
    "VSS_CF_BACKUP_RECOVERY",
    "VSS_CF_NOT_SYSTEM_STATE",
    "VSS_COMPONENT_FLAGS",
    "VSS_COMPONENT_TYPE",
    "VSS_CTX_ALL",
    "VSS_CTX_APP_ROLLBACK",
    "VSS_CTX_BACKUP",
    "VSS_CTX_CLIENT_ACCESSIBLE",
    "VSS_CTX_CLIENT_ACCESSIBLE_WRITERS",
    "VSS_CTX_FILE_SHARE_BACKUP",
    "VSS_CTX_NAS_ROLLBACK",
    "VSS_CT_DATABASE",
    "VSS_CT_FILEGROUP",
    "VSS_CT_UNDEFINED",
    "VSS_DIFF_AREA_PROP",
    "VSS_DIFF_VOLUME_PROP",
    "VSS_E_ASRERROR_CRITICAL_DISKS_TOO_SMALL",
    "VSS_E_ASRERROR_CRITICAL_DISK_CANNOT_BE_EXCLUDED",
    "VSS_E_ASRERROR_DATADISK_RDISK0",
    "VSS_E_ASRERROR_DISK_ASSIGNMENT_FAILED",
    "VSS_E_ASRERROR_DISK_RECREATION_FAILED",
    "VSS_E_ASRERROR_DYNAMIC_VHD_NOT_SUPPORTED",
    "VSS_E_ASRERROR_FIXED_PHYSICAL_DISK_AVAILABLE_AFTER_DISK_EXCLUSION",
    "VSS_E_ASRERROR_MISSING_DYNDISK",
    "VSS_E_ASRERROR_NO_ARCPATH",
    "VSS_E_ASRERROR_NO_PHYSICAL_DISK_AVAILABLE",
    "VSS_E_ASRERROR_RDISK0_TOOSMALL",
    "VSS_E_ASRERROR_RDISK_FOR_SYSTEM_DISK_NOT_FOUND",
    "VSS_E_ASRERROR_SHARED_CRIDISK",
    "VSS_E_ASRERROR_SYSTEM_PARTITION_HIDDEN",
    "VSS_E_AUTORECOVERY_FAILED",
    "VSS_E_BAD_STATE",
    "VSS_E_BREAK_REVERT_ID_FAILED",
    "VSS_E_CANNOT_REVERT_DISKID",
    "VSS_E_CLUSTER_ERROR",
    "VSS_E_CLUSTER_TIMEOUT",
    "VSS_E_CORRUPT_XML_DOCUMENT",
    "VSS_E_CRITICAL_VOLUME_ON_INVALID_DISK",
    "VSS_E_DYNAMIC_DISK_ERROR",
    "VSS_E_FLUSH_WRITES_TIMEOUT",
    "VSS_E_FSS_TIMEOUT",
    "VSS_E_HOLD_WRITES_TIMEOUT",
    "VSS_E_INSUFFICIENT_STORAGE",
    "VSS_E_INVALID_XML_DOCUMENT",
    "VSS_E_LEGACY_PROVIDER",
    "VSS_E_MAXIMUM_DIFFAREA_ASSOCIATIONS_REACHED",
    "VSS_E_MAXIMUM_NUMBER_OF_REMOTE_MACHINES_REACHED",
    "VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED",
    "VSS_E_MAXIMUM_NUMBER_OF_VOLUMES_REACHED",
    "VSS_E_MISSING_DISK",
    "VSS_E_MISSING_HIDDEN_VOLUME",
    "VSS_E_MISSING_VOLUME",
    "VSS_E_NESTED_VOLUME_LIMIT",
    "VSS_E_NONTRANSPORTABLE_BCD",
    "VSS_E_NOT_SUPPORTED",
    "VSS_E_NO_SNAPSHOTS_IMPORTED",
    "VSS_E_OBJECT_ALREADY_EXISTS",
    "VSS_E_OBJECT_NOT_FOUND",
    "VSS_E_PROVIDER_ALREADY_REGISTERED",
    "VSS_E_PROVIDER_IN_USE",
    "VSS_E_PROVIDER_NOT_REGISTERED",
    "VSS_E_PROVIDER_VETO",
    "VSS_E_REBOOT_REQUIRED",
    "VSS_E_REMOTE_SERVER_UNAVAILABLE",
    "VSS_E_REMOTE_SERVER_UNSUPPORTED",
    "VSS_E_RESYNC_IN_PROGRESS",
    "VSS_E_REVERT_IN_PROGRESS",
    "VSS_E_REVERT_VOLUME_LOST",
    "VSS_E_SNAPSHOT_NOT_IN_SET",
    "VSS_E_SNAPSHOT_SET_IN_PROGRESS",
    "VSS_E_SOME_SNAPSHOTS_NOT_IMPORTED",
    "VSS_E_TRANSACTION_FREEZE_TIMEOUT",
    "VSS_E_TRANSACTION_THAW_TIMEOUT",
    "VSS_E_UNEXPECTED",
    "VSS_E_UNEXPECTED_PROVIDER_ERROR",
    "VSS_E_UNEXPECTED_WRITER_ERROR",
    "VSS_E_UNSELECTED_VOLUME",
    "VSS_E_UNSUPPORTED_CONTEXT",
    "VSS_E_VOLUME_IN_USE",
    "VSS_E_VOLUME_NOT_LOCAL",
    "VSS_E_VOLUME_NOT_SUPPORTED",
    "VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER",
    "VSS_E_WRITERERROR_INCONSISTENTSNAPSHOT",
    "VSS_E_WRITERERROR_NONRETRYABLE",
    "VSS_E_WRITERERROR_OUTOFRESOURCES",
    "VSS_E_WRITERERROR_PARTIAL_FAILURE",
    "VSS_E_WRITERERROR_RECOVERY_FAILED",
    "VSS_E_WRITERERROR_RETRYABLE",
    "VSS_E_WRITERERROR_TIMEOUT",
    "VSS_E_WRITER_ALREADY_SUBSCRIBED",
    "VSS_E_WRITER_INFRASTRUCTURE",
    "VSS_E_WRITER_NOT_RESPONDING",
    "VSS_E_WRITER_STATUS_NOT_AVAILABLE",
    "VSS_FILE_RESTORE_STATUS",
    "VSS_FILE_SPEC_BACKUP_TYPE",
    "VSS_FSBT_ALL_BACKUP_REQUIRED",
    "VSS_FSBT_ALL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_CREATED_DURING_BACKUP",
    "VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED",
    "VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_FULL_BACKUP_REQUIRED",
    "VSS_FSBT_FULL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED",
    "VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_LOG_BACKUP_REQUIRED",
    "VSS_FSBT_LOG_SNAPSHOT_REQUIRED",
    "VSS_HARDWARE_OPTIONS",
    "VSS_MGMT_OBJECT_DIFF_AREA",
    "VSS_MGMT_OBJECT_DIFF_VOLUME",
    "VSS_MGMT_OBJECT_PROP",
    "VSS_MGMT_OBJECT_TYPE",
    "VSS_MGMT_OBJECT_UNION",
    "VSS_MGMT_OBJECT_UNKNOWN",
    "VSS_MGMT_OBJECT_VOLUME",
    "VSS_OBJECT_NONE",
    "VSS_OBJECT_PROP",
    "VSS_OBJECT_PROVIDER",
    "VSS_OBJECT_SNAPSHOT",
    "VSS_OBJECT_SNAPSHOT_SET",
    "VSS_OBJECT_TYPE",
    "VSS_OBJECT_TYPE_COUNT",
    "VSS_OBJECT_UNION",
    "VSS_OBJECT_UNKNOWN",
    "VSS_ONLUNSTATECHANGE_DO_MASK_LUNS",
    "VSS_ONLUNSTATECHANGE_NOTIFY_LUN_POST_RECOVERY",
    "VSS_ONLUNSTATECHANGE_NOTIFY_LUN_PRE_RECOVERY",
    "VSS_ONLUNSTATECHANGE_NOTIFY_READ_WRITE",
    "VSS_PROTECTION_FAULT",
    "VSS_PROTECTION_FAULT_COW_READ_FAILURE",
    "VSS_PROTECTION_FAULT_COW_WRITE_FAILURE",
    "VSS_PROTECTION_FAULT_DESTROY_ALL_SNAPSHOTS",
    "VSS_PROTECTION_FAULT_DIFF_AREA_FULL",
    "VSS_PROTECTION_FAULT_DIFF_AREA_MISSING",
    "VSS_PROTECTION_FAULT_DIFF_AREA_REMOVED",
    "VSS_PROTECTION_FAULT_EXTERNAL_WRITER_TO_DIFF_AREA",
    "VSS_PROTECTION_FAULT_FILE_SYSTEM_FAILURE",
    "VSS_PROTECTION_FAULT_GROW_FAILED",
    "VSS_PROTECTION_FAULT_GROW_TOO_SLOW",
    "VSS_PROTECTION_FAULT_IO_FAILURE",
    "VSS_PROTECTION_FAULT_IO_FAILURE_DURING_ONLINE",
    "VSS_PROTECTION_FAULT_MAPPED_MEMORY_FAILURE",
    "VSS_PROTECTION_FAULT_MEMORY_ALLOCATION_FAILURE",
    "VSS_PROTECTION_FAULT_META_DATA_CORRUPTION",
    "VSS_PROTECTION_FAULT_MOUNT_DURING_CLUSTER_OFFLINE",
    "VSS_PROTECTION_FAULT_NONE",
    "VSS_PROTECTION_LEVEL",
    "VSS_PROTECTION_LEVEL_ORIGINAL_VOLUME",
    "VSS_PROTECTION_LEVEL_SNAPSHOT",
    "VSS_PROVIDER_CAPABILITIES",
    "VSS_PROVIDER_PROP",
    "VSS_PROVIDER_TYPE",
    "VSS_PROV_FILESHARE",
    "VSS_PROV_HARDWARE",
    "VSS_PROV_SOFTWARE",
    "VSS_PROV_SYSTEM",
    "VSS_PROV_UNKNOWN",
    "VSS_PRV_CAPABILITY_CLUSTERED",
    "VSS_PRV_CAPABILITY_COMPLIANT",
    "VSS_PRV_CAPABILITY_DIFFERENTIAL",
    "VSS_PRV_CAPABILITY_LEGACY",
    "VSS_PRV_CAPABILITY_LUN_REPOINT",
    "VSS_PRV_CAPABILITY_LUN_RESYNC",
    "VSS_PRV_CAPABILITY_MULTIPLE_IMPORT",
    "VSS_PRV_CAPABILITY_OFFLINE_CREATION",
    "VSS_PRV_CAPABILITY_PLEX",
    "VSS_PRV_CAPABILITY_RECYCLING",
    "VSS_RECOVERY_NO_VOLUME_CHECK",
    "VSS_RECOVERY_OPTIONS",
    "VSS_RECOVERY_REVERT_IDENTITY_ALL",
    "VSS_RESTOREMETHOD_ENUM",
    "VSS_RESTORE_TARGET",
    "VSS_RESTORE_TYPE",
    "VSS_RF_ALL",
    "VSS_RF_NONE",
    "VSS_RF_PARTIAL",
    "VSS_RF_UNDEFINED",
    "VSS_RME_CUSTOM",
    "VSS_RME_RESTORE_AT_REBOOT",
    "VSS_RME_RESTORE_AT_REBOOT_IF_CANNOT_REPLACE",
    "VSS_RME_RESTORE_IF_CAN_REPLACE",
    "VSS_RME_RESTORE_IF_NOT_THERE",
    "VSS_RME_RESTORE_STOP_START",
    "VSS_RME_RESTORE_TO_ALTERNATE_LOCATION",
    "VSS_RME_STOP_RESTORE_START",
    "VSS_RME_UNDEFINED",
    "VSS_ROLLFORWARD_TYPE",
    "VSS_RS_ALL",
    "VSS_RS_FAILED",
    "VSS_RS_NONE",
    "VSS_RS_UNDEFINED",
    "VSS_RTYPE_BY_COPY",
    "VSS_RTYPE_IMPORT",
    "VSS_RTYPE_OTHER",
    "VSS_RTYPE_UNDEFINED",
    "VSS_RT_ALTERNATE",
    "VSS_RT_DIRECTED",
    "VSS_RT_ORIGINAL",
    "VSS_RT_ORIGINAL_LOCATION",
    "VSS_RT_UNDEFINED",
    "VSS_SC_DISABLE_CONTENTINDEX",
    "VSS_SC_DISABLE_DEFRAG",
    "VSS_SM_ALL_FLAGS",
    "VSS_SM_BACKUP_EVENTS_FLAG",
    "VSS_SM_IO_THROTTLING_FLAG",
    "VSS_SM_POST_SNAPSHOT_FLAG",
    "VSS_SM_RESTORE_EVENTS_FLAG",
    "VSS_SNAPSHOT_COMPATIBILITY",
    "VSS_SNAPSHOT_CONTEXT",
    "VSS_SNAPSHOT_PROP",
    "VSS_SNAPSHOT_PROPERTY_ID",
    "VSS_SNAPSHOT_STATE",
    "VSS_SOURCE_TYPE",
    "VSS_SPROPID_CREATION_TIMESTAMP",
    "VSS_SPROPID_EXPOSED_NAME",
    "VSS_SPROPID_EXPOSED_PATH",
    "VSS_SPROPID_ORIGINAL_VOLUME",
    "VSS_SPROPID_ORIGINATING_MACHINE",
    "VSS_SPROPID_PROVIDER_ID",
    "VSS_SPROPID_SERVICE_MACHINE",
    "VSS_SPROPID_SNAPSHOTS_COUNT",
    "VSS_SPROPID_SNAPSHOT_ATTRIBUTES",
    "VSS_SPROPID_SNAPSHOT_DEVICE",
    "VSS_SPROPID_SNAPSHOT_ID",
    "VSS_SPROPID_SNAPSHOT_SET_ID",
    "VSS_SPROPID_STATUS",
    "VSS_SPROPID_UNKNOWN",
    "VSS_SS_ABORTED",
    "VSS_SS_COMMITTED",
    "VSS_SS_COUNT",
    "VSS_SS_CREATED",
    "VSS_SS_DELETED",
    "VSS_SS_POSTCOMMITTED",
    "VSS_SS_PRECOMMITTED",
    "VSS_SS_PREFINALCOMMITTED",
    "VSS_SS_PREPARED",
    "VSS_SS_PREPARING",
    "VSS_SS_PROCESSING_COMMIT",
    "VSS_SS_PROCESSING_POSTCOMMIT",
    "VSS_SS_PROCESSING_POSTFINALCOMMIT",
    "VSS_SS_PROCESSING_PRECOMMIT",
    "VSS_SS_PROCESSING_PREFINALCOMMIT",
    "VSS_SS_PROCESSING_PREPARE",
    "VSS_SS_UNKNOWN",
    "VSS_ST_NONTRANSACTEDDB",
    "VSS_ST_OTHER",
    "VSS_ST_TRANSACTEDDB",
    "VSS_ST_UNDEFINED",
    "VSS_SUBSCRIBE_MASK",
    "VSS_S_ASYNC_CANCELLED",
    "VSS_S_ASYNC_FINISHED",
    "VSS_S_ASYNC_PENDING",
    "VSS_S_SOME_SNAPSHOTS_NOT_IMPORTED",
    "VSS_USAGE_TYPE",
    "VSS_UT_BOOTABLESYSTEMSTATE",
    "VSS_UT_OTHER",
    "VSS_UT_SYSTEMSERVICE",
    "VSS_UT_UNDEFINED",
    "VSS_UT_USERDATA",
    "VSS_VOLSNAP_ATTR_AUTORECOVER",
    "VSS_VOLSNAP_ATTR_CLIENT_ACCESSIBLE",
    "VSS_VOLSNAP_ATTR_DELAYED_POSTSNAPSHOT",
    "VSS_VOLSNAP_ATTR_DIFFERENTIAL",
    "VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY",
    "VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY",
    "VSS_VOLSNAP_ATTR_FILE_SHARE",
    "VSS_VOLSNAP_ATTR_HARDWARE_ASSISTED",
    "VSS_VOLSNAP_ATTR_IMPORTED",
    "VSS_VOLSNAP_ATTR_NOT_SURFACED",
    "VSS_VOLSNAP_ATTR_NOT_TRANSACTED",
    "VSS_VOLSNAP_ATTR_NO_AUTORECOVERY",
    "VSS_VOLSNAP_ATTR_NO_AUTO_RELEASE",
    "VSS_VOLSNAP_ATTR_NO_WRITERS",
    "VSS_VOLSNAP_ATTR_PERSISTENT",
    "VSS_VOLSNAP_ATTR_PLEX",
    "VSS_VOLSNAP_ATTR_ROLLBACK_RECOVERY",
    "VSS_VOLSNAP_ATTR_TRANSPORTABLE",
    "VSS_VOLSNAP_ATTR_TXF_RECOVERY",
    "VSS_VOLUME_PROP",
    "VSS_VOLUME_PROTECTION_INFO",
    "VSS_VOLUME_SNAPSHOT_ATTRIBUTES",
    "VSS_WRE_ALWAYS",
    "VSS_WRE_IF_REPLACE_FAILS",
    "VSS_WRE_NEVER",
    "VSS_WRE_UNDEFINED",
    "VSS_WRITERRESTORE_ENUM",
    "VSS_WRITER_STATE",
    "VSS_WS_COUNT",
    "VSS_WS_FAILED_AT_BACKUPSHUTDOWN",
    "VSS_WS_FAILED_AT_BACKUP_COMPLETE",
    "VSS_WS_FAILED_AT_FREEZE",
    "VSS_WS_FAILED_AT_IDENTIFY",
    "VSS_WS_FAILED_AT_POST_RESTORE",
    "VSS_WS_FAILED_AT_POST_SNAPSHOT",
    "VSS_WS_FAILED_AT_PREPARE_BACKUP",
    "VSS_WS_FAILED_AT_PREPARE_SNAPSHOT",
    "VSS_WS_FAILED_AT_PRE_RESTORE",
    "VSS_WS_FAILED_AT_THAW",
    "VSS_WS_STABLE",
    "VSS_WS_UNKNOWN",
    "VSS_WS_WAITING_FOR_BACKUP_COMPLETE",
    "VSS_WS_WAITING_FOR_FREEZE",
    "VSS_WS_WAITING_FOR_POST_SNAPSHOT",
    "VSS_WS_WAITING_FOR_THAW",
    "VssSnapshotMgmt",
]
_arch_optional = [
]
