from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.VirtualDiskService
import win32more.Windows.Win32.Storage.Vss
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
VSS_ASSOC_NO_MAX_SPACE: Int32 = -1
VSS_ASSOC_REMOVE: UInt32 = 0
VSS_E_BAD_STATE: win32more.Windows.Win32.Foundation.HRESULT = -2147212543
VSS_E_UNEXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212542
VSS_E_PROVIDER_ALREADY_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2147212541
VSS_E_PROVIDER_NOT_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2147212540
VSS_E_PROVIDER_VETO: win32more.Windows.Win32.Foundation.HRESULT = -2147212538
VSS_E_PROVIDER_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147212537
VSS_E_OBJECT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147212536
VSS_S_ASYNC_PENDING: win32more.Windows.Win32.Foundation.HRESULT = 271113
VSS_S_ASYNC_FINISHED: win32more.Windows.Win32.Foundation.HRESULT = 271114
VSS_S_ASYNC_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = 271115
VSS_E_VOLUME_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212532
VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2147212530
VSS_E_OBJECT_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147212531
VSS_E_UNEXPECTED_PROVIDER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147212529
VSS_E_CORRUPT_XML_DOCUMENT: win32more.Windows.Win32.Foundation.HRESULT = -2147212528
VSS_E_INVALID_XML_DOCUMENT: win32more.Windows.Win32.Foundation.HRESULT = -2147212527
VSS_E_MAXIMUM_NUMBER_OF_VOLUMES_REACHED: win32more.Windows.Win32.Foundation.HRESULT = -2147212526
VSS_E_FLUSH_WRITES_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212525
VSS_E_HOLD_WRITES_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212524
VSS_E_UNEXPECTED_WRITER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147212523
VSS_E_SNAPSHOT_SET_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2147212522
VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED: win32more.Windows.Win32.Foundation.HRESULT = -2147212521
VSS_E_WRITER_INFRASTRUCTURE: win32more.Windows.Win32.Foundation.HRESULT = -2147212520
VSS_E_WRITER_NOT_RESPONDING: win32more.Windows.Win32.Foundation.HRESULT = -2147212519
VSS_E_WRITER_ALREADY_SUBSCRIBED: win32more.Windows.Win32.Foundation.HRESULT = -2147212518
VSS_E_UNSUPPORTED_CONTEXT: win32more.Windows.Win32.Foundation.HRESULT = -2147212517
VSS_E_VOLUME_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147212515
VSS_E_MAXIMUM_DIFFAREA_ASSOCIATIONS_REACHED: win32more.Windows.Win32.Foundation.HRESULT = -2147212514
VSS_E_INSUFFICIENT_STORAGE: win32more.Windows.Win32.Foundation.HRESULT = -2147212513
VSS_E_NO_SNAPSHOTS_IMPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212512
VSS_S_SOME_SNAPSHOTS_NOT_IMPORTED: win32more.Windows.Win32.Foundation.HRESULT = 271137
VSS_E_SOME_SNAPSHOTS_NOT_IMPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212511
VSS_E_MAXIMUM_NUMBER_OF_REMOTE_MACHINES_REACHED: win32more.Windows.Win32.Foundation.HRESULT = -2147212510
VSS_E_REMOTE_SERVER_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147212509
VSS_E_REMOTE_SERVER_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212508
VSS_E_REVERT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2147212507
VSS_E_REVERT_VOLUME_LOST: win32more.Windows.Win32.Foundation.HRESULT = -2147212506
VSS_E_REBOOT_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2147212505
VSS_E_TRANSACTION_FREEZE_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212504
VSS_E_TRANSACTION_THAW_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212503
VSS_E_VOLUME_NOT_LOCAL: win32more.Windows.Win32.Foundation.HRESULT = -2147212499
VSS_E_CLUSTER_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212498
VSS_E_WRITERERROR_INCONSISTENTSNAPSHOT: win32more.Windows.Win32.Foundation.HRESULT = -2147212304
VSS_E_WRITERERROR_OUTOFRESOURCES: win32more.Windows.Win32.Foundation.HRESULT = -2147212303
VSS_E_WRITERERROR_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212302
VSS_E_WRITERERROR_RETRYABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147212301
VSS_E_WRITERERROR_NONRETRYABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147212300
VSS_E_WRITERERROR_RECOVERY_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147212299
VSS_E_BREAK_REVERT_ID_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147212298
VSS_E_LEGACY_PROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2147212297
VSS_E_MISSING_DISK: win32more.Windows.Win32.Foundation.HRESULT = -2147212296
VSS_E_MISSING_HIDDEN_VOLUME: win32more.Windows.Win32.Foundation.HRESULT = -2147212295
VSS_E_MISSING_VOLUME: win32more.Windows.Win32.Foundation.HRESULT = -2147212294
VSS_E_AUTORECOVERY_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147212293
VSS_E_DYNAMIC_DISK_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147212292
VSS_E_NONTRANSPORTABLE_BCD: win32more.Windows.Win32.Foundation.HRESULT = -2147212291
VSS_E_CANNOT_REVERT_DISKID: win32more.Windows.Win32.Foundation.HRESULT = -2147212290
VSS_E_RESYNC_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2147212289
VSS_E_CLUSTER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147212288
VSS_E_UNSELECTED_VOLUME: win32more.Windows.Win32.Foundation.HRESULT = -2147212502
VSS_E_SNAPSHOT_NOT_IN_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147212501
VSS_E_NESTED_VOLUME_LIMIT: win32more.Windows.Win32.Foundation.HRESULT = -2147212500
VSS_E_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212497
VSS_E_WRITERERROR_PARTIAL_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2147212490
VSS_E_ASRERROR_DISK_ASSIGNMENT_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147212287
VSS_E_ASRERROR_DISK_RECREATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147212286
VSS_E_ASRERROR_NO_ARCPATH: win32more.Windows.Win32.Foundation.HRESULT = -2147212285
VSS_E_ASRERROR_MISSING_DYNDISK: win32more.Windows.Win32.Foundation.HRESULT = -2147212284
VSS_E_ASRERROR_SHARED_CRIDISK: win32more.Windows.Win32.Foundation.HRESULT = -2147212283
VSS_E_ASRERROR_DATADISK_RDISK0: win32more.Windows.Win32.Foundation.HRESULT = -2147212282
VSS_E_ASRERROR_RDISK0_TOOSMALL: win32more.Windows.Win32.Foundation.HRESULT = -2147212281
VSS_E_ASRERROR_CRITICAL_DISKS_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2147212280
VSS_E_WRITER_STATUS_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147212279
VSS_E_ASRERROR_DYNAMIC_VHD_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147212278
VSS_E_CRITICAL_VOLUME_ON_INVALID_DISK: win32more.Windows.Win32.Foundation.HRESULT = -2147212271
VSS_E_ASRERROR_RDISK_FOR_SYSTEM_DISK_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147212270
VSS_E_ASRERROR_NO_PHYSICAL_DISK_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147212269
VSS_E_ASRERROR_FIXED_PHYSICAL_DISK_AVAILABLE_AFTER_DISK_EXCLUSION: win32more.Windows.Win32.Foundation.HRESULT = -2147212268
VSS_E_ASRERROR_CRITICAL_DISK_CANNOT_BE_EXCLUDED: win32more.Windows.Win32.Foundation.HRESULT = -2147212267
VSS_E_ASRERROR_SYSTEM_PARTITION_HIDDEN: win32more.Windows.Win32.Foundation.HRESULT = -2147212266
VSS_E_FSS_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147212265
@winfunctype('VSSAPI.dll')
def CreateVssExpressWriterInternal(ppWriter: POINTER(win32more.Windows.Win32.Storage.Vss.IVssExpressWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssAdmin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{77ed5996-2f63-11d3-8a39-00c04f72d8e3}')
    @commethod(3)
    def RegisterProvider(self, pProviderId: Guid, ClassId: Guid, pwszProviderName: POINTER(UInt16), eProviderType: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE, pwszProviderVersion: POINTER(UInt16), ProviderVersionId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterProvider(self, ProviderId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryProviders(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAllSnapshotsInProgress(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssAdminEx(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssAdmin
    _iid_ = Guid('{7858a9f8-b1fa-41a6-964f-b9b36b8cd8d8}')
    @commethod(7)
    def GetProviderCapability(self, pProviderId: Guid, pllOriginalCapabilityMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProviderContext(self, ProviderId: Guid, plContext: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProviderContext(self, ProviderId: Guid, lContext: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{507c37b4-cf5b-4e95-b0af-14eb9767467e}')
    @commethod(3)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Wait(self, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryStatus(self, pHrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pReserved: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssComponent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2c72c96-c121-4518-b627-e5a93d010ead}')
    @commethod(3)
    def GetLogicalPath(self, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentType(self, pct: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBackupSucceeded(self, pbSucceeded: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAlternateLocationMappingCount(self, pcMappings: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAlternateLocationMapping(self, iMapping: UInt32, ppFiledesc: POINTER(win32more.Windows.Win32.Storage.Vss.IVssWMFiledesc)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackupMetadata(self, wszData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBackupMetadata(self, pbstrData: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddPartialFile(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilename: win32more.Windows.Win32.Foundation.PWSTR, wszRanges: win32more.Windows.Win32.Foundation.PWSTR, wszMetadata: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPartialFileCount(self, pcPartialFiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPartialFile(self, iPartialFile: UInt32, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrFilename: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrRange: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrMetadata: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsSelectedForRestore(self, pbSelectedForRestore: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAdditionalRestores(self, pbAdditionalRestores: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetNewTargetCount(self, pcNewTarget: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNewTarget(self, iNewTarget: UInt32, ppFiledesc: POINTER(win32more.Windows.Win32.Storage.Vss.IVssWMFiledesc)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AddDirectedTarget(self, wszSourcePath: win32more.Windows.Win32.Foundation.PWSTR, wszSourceFilename: win32more.Windows.Win32.Foundation.PWSTR, wszSourceRangeList: win32more.Windows.Win32.Foundation.PWSTR, wszDestinationPath: win32more.Windows.Win32.Foundation.PWSTR, wszDestinationFilename: win32more.Windows.Win32.Foundation.PWSTR, wszDestinationRangeList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDirectedTargetCount(self, pcDirectedTarget: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDirectedTarget(self, iDirectedTarget: UInt32, pbstrSourcePath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrSourceFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrSourceRangeList: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrDestinationPath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrDestinationFilename: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrDestinationRangeList: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetRestoreMetadata(self, wszRestoreMetadata: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRestoreMetadata(self, pbstrRestoreMetadata: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetRestoreTarget(self, target: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetRestoreTarget(self, pTarget: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetPreRestoreFailureMsg(self, wszPreRestoreFailureMsg: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetPreRestoreFailureMsg(self, pbstrPreRestoreFailureMsg: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetPostRestoreFailureMsg(self, wszPostRestoreFailureMsg: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetPostRestoreFailureMsg(self, pbstrPostRestoreFailureMsg: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetBackupStamp(self, wszBackupStamp: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetBackupStamp(self, pbstrBackupStamp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPreviousBackupStamp(self, pbstrBackupStamp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetBackupOptions(self, pbstrBackupOptions: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetRestoreOptions(self, pbstrRestoreOptions: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetRestoreSubcomponentCount(self, pcRestoreSubcomponent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetRestoreSubcomponent(self, iComponent: UInt32, pbstrLogicalPath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrComponentName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbRepair: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetFileRestoreStatus(self, pStatus: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_FILE_RESTORE_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def AddDifferencedFilesByLastModifyTime(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: win32more.Windows.Win32.Foundation.BOOL, ftLastModifyTime: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def AddDifferencedFilesByLastModifyLSN(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: win32more.Windows.Win32.Foundation.BOOL, bstrLsnString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetDifferencedFilesCount(self, pcDifferencedFiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetDifferencedFile(self, iDifferencedFile: UInt32, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrFilespec: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbRecursive: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbstrLsnString: POINTER(win32more.Windows.Win32.Foundation.BSTR), pftLastModifyTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssComponentEx(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssComponent
    _iid_ = Guid('{156c8b5e-f131-4bd7-9c97-d1923be7e1fa}')
    @commethod(41)
    def SetPrepareForBackupFailureMsg(self, wszFailureMsg: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetPostSnapshotFailureMsg(self, wszFailureMsg: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetPrepareForBackupFailureMsg(self, pbstrFailureMsg: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetPostSnapshotFailureMsg(self, pbstrFailureMsg: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetAuthoritativeRestore(self, pbAuth: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetRollForward(self, pRollType: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_ROLLFORWARD_TYPE), pbstrPoint: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetRestoreName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssComponentEx2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssComponentEx
    _iid_ = Guid('{3b5be0f2-07a9-4e4b-bdd3-cfdc8e2c0d2d}')
    @commethod(48)
    def SetFailure(self, hr: win32more.Windows.Win32.Foundation.HRESULT, hrApplication: win32more.Windows.Win32.Foundation.HRESULT, wszApplicationMessage: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetFailure(self, phr: POINTER(win32more.Windows.Win32.Foundation.HRESULT), phrApplication: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pbstrApplicationMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssCreateExpressWriterMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c772e77-b26e-427f-92dd-c996f41ea5e3}')
    @commethod(3)
    def AddExcludeFiles(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddComponent(self, ct: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszComponentName: win32more.Windows.Win32.Foundation.PWSTR, wszCaption: win32more.Windows.Win32.Foundation.PWSTR, pbIcon: POINTER(Byte), cbIcon: UInt32, bRestoreMetadata: Byte, bNotifyOnBackupComplete: Byte, bSelectable: Byte, bSelectableForRestore: Byte, dwComponentFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilesToFileGroup(self, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszGroupName: win32more.Windows.Win32.Foundation.PWSTR, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Windows.Win32.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRestoreMethod(self, method: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM, wszService: win32more.Windows.Win32.Foundation.PWSTR, wszUserProcedure: win32more.Windows.Win32.Foundation.PWSTR, writerRestore: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM, bRebootRequired: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddComponentDependency(self, wszForLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszForComponentName: win32more.Windows.Win32.Foundation.PWSTR, onWriterId: Guid, wszOnLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszOnComponentName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetBackupSchema(self, dwSchemaMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SaveAsXML(self, pbstrXML: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssCreateWriterMetadata(ComPtr):
    extends: None
    @commethod(0)
    def AddIncludeFiles(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def AddExcludeFiles(self, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def AddComponent(self, ct: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszComponentName: win32more.Windows.Win32.Foundation.PWSTR, wszCaption: win32more.Windows.Win32.Foundation.PWSTR, pbIcon: POINTER(Byte), cbIcon: UInt32, bRestoreMetadata: Byte, bNotifyOnBackupComplete: Byte, bSelectable: Byte, bSelectableForRestore: Byte, dwComponentFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(3)
    def AddDatabaseFiles(self, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszDatabaseName: win32more.Windows.Win32.Foundation.PWSTR, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddDatabaseLogFiles(self, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszDatabaseName: win32more.Windows.Win32.Foundation.PWSTR, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFilesToFileGroup(self, wszLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszGroupName: win32more.Windows.Win32.Foundation.PWSTR, wszPath: win32more.Windows.Win32.Foundation.PWSTR, wszFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte, wszAlternateLocation: win32more.Windows.Win32.Foundation.PWSTR, dwBackupTypeMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRestoreMethod(self, method: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM, wszService: win32more.Windows.Win32.Foundation.PWSTR, wszUserProcedure: win32more.Windows.Win32.Foundation.PWSTR, writerRestore: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM, bRebootRequired: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddAlternateLocationMapping(self, wszSourcePath: win32more.Windows.Win32.Foundation.PWSTR, wszSourceFilespec: win32more.Windows.Win32.Foundation.PWSTR, bRecursive: Byte, wszDestination: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddComponentDependency(self, wszForLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszForComponentName: win32more.Windows.Win32.Foundation.PWSTR, onWriterId: Guid, wszOnLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, wszOnComponentName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBackupSchema(self, dwSchemaMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDocument(self, pDoc: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SaveAsXML(self, pbstrXML: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{214a0f28-b737-4026-b847-4f9e37d79529}')
    @commethod(3)
    def AddDiffArea(self, pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangeDiffAreaMaximumSize(self, pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryVolumesSupportedForDiffAreas(self, pwszOriginalVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryDiffAreasForVolume(self, pwszVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryDiffAreasOnVolume(self, pwszVolumeName: POINTER(UInt16), ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryDiffAreasForSnapshot(self, SnapshotId: Guid, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt
    _iid_ = Guid('{949d7353-675f-4275-8969-f044c6277815}')
    @commethod(9)
    def ChangeDiffAreaMaximumSizeEx(self, pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), llMaximumDiffSpace: Int64, bVolatile: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MigrateDiffAreas(self, pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), pwszNewDiffAreaVolumeName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def QueryMigrationStatus(self, pwszVolumeName: POINTER(UInt16), pwszDiffAreaVolumeName: POINTER(UInt16), ppAsync: POINTER(win32more.Windows.Win32.Storage.Vss.IVssAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSnapshotPriority(self, idSnapshot: Guid, priority: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssDifferentialSoftwareSnapshotMgmt3(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt2
    _iid_ = Guid('{383f7e71-a4c5-401f-b27f-f826289f8458}')
    @commethod(13)
    def SetVolumeProtectLevel(self, pwszVolumeName: POINTER(UInt16), protectionLevel: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_LEVEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetVolumeProtectLevel(self, pwszVolumeName: POINTER(UInt16), protectionLevel: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_PROTECTION_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearVolumeProtectFault(self, pwszVolumeName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteUnusedDiffAreas(self, pwszDiffAreaVolumeName: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def QuerySnapshotDeltaBitmap(self, idSnapshotOlder: Guid, idSnapshotYounger: Guid, pcBlockSizePerBit: POINTER(UInt32), pcBitmapLength: POINTER(UInt32), ppbBitmap: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssEnumMgmtObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01954e6b-9254-4e6e-808c-c9e05d007696}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_PROP), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssEnumObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae1c7110-2f60-11d3-8a39-00c04f72d8e3}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_PROP), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssExpressWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e33affdc-59c7-47b1-97d5-4266598f6235}')
    @commethod(3)
    def CreateMetadata(self, writerId: Guid, writerName: win32more.Windows.Win32.Foundation.PWSTR, usageType: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE, versionMajor: UInt32, versionMinor: UInt32, reserved: UInt32, ppMetadata: POINTER(win32more.Windows.Win32.Storage.Vss.IVssCreateExpressWriterMetadata)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadMetadata(self, metadata: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Register(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unregister(self, writerId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssFileShareSnapshotProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8636060-7c2e-11df-8c4a-0800200c9a66}')
    @commethod(3)
    def SetContext(self, lContext: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSnapshotProperties(self, SnapshotId: Guid, pProp: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Query(self, QueriedObjectId: Guid, eQueriedObjectType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, eReturnedObjectsType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteSnapshots(self, SourceObjectId: Guid, eSourceObjectType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, bForceDelete: win32more.Windows.Win32.Foundation.BOOL, plDeletedSnapshots: POINTER(Int32), pNondeletedSnapshotID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginPrepareSnapshot(self, SnapshotSetId: Guid, SnapshotId: Guid, pwszSharePath: POINTER(UInt16), lNewContext: Int32, ProviderId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsPathSupported(self, pwszSharePath: POINTER(UInt16), pbSupportedByThisProvider: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsPathSnapshotted(self, pwszSharePath: POINTER(UInt16), pbSnapshotsPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL), plSnapshotCompatibility: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSnapshotProperty(self, SnapshotId: Guid, eSnapshotPropertyId: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID, vProperty: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssHardwareSnapshotProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9593a157-44e9-4344-bbeb-44fbf9b06b10}')
    @commethod(3)
    def AreLunsSupported(self, lLunCount: Int32, lContext: Int32, rgwszDevices: POINTER(POINTER(UInt16)), pLunInformation: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), pbIsSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FillInLunInfo(self, wszDeviceName: POINTER(UInt16), pLunInfo: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), pbIsSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginPrepareSnapshot(self, SnapshotSetId: Guid, SnapshotId: Guid, lContext: Int32, lLunCount: Int32, rgDeviceNames: POINTER(POINTER(UInt16)), rgLunInformation: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTargetLuns(self, lLunCount: Int32, rgDeviceNames: POINTER(POINTER(UInt16)), rgSourceLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), rgDestinationLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LocateLuns(self, lLunCount: Int32, rgSourceLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnLunEmpty(self, wszDeviceName: POINTER(UInt16), pInformation: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssHardwareSnapshotProviderEx(ComPtr):
    extends: win32more.Windows.Win32.Storage.Vss.IVssHardwareSnapshotProvider
    _iid_ = Guid('{7f5ba925-cdb1-4d11-a71f-339eb7e709fd}')
    @commethod(9)
    def GetProviderCapabilities(self, pllOriginalCapabilityMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnLunStateChange(self, pSnapshotLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), pOriginalLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), dwCount: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResyncLuns(self, pSourceLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), pTargetLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), dwCount: UInt32, ppAsync: POINTER(win32more.Windows.Win32.Storage.Vss.IVssAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnReuseLuns(self, pSnapshotLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), pOriginalLuns: POINTER(win32more.Windows.Win32.Storage.VirtualDiskService.VDS_LUN_INFORMATION), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssProviderCreateSnapshotSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f894e5b-1e39-4778-8e23-9abad9f0e08c}')
    @commethod(3)
    def EndPrepareSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PreCommitSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CommitSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PostCommitSnapshots(self, SnapshotSetId: Guid, lSnapshotsCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PreFinalCommitSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PostFinalCommitSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AbortSnapshots(self, SnapshotSetId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssProviderNotifications(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e561901f-03a5-4afe-86d0-72baeece7004}')
    @commethod(3)
    def OnLoad(self, pCallback: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUnload(self, bForceUnload: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssSnapshotMgmt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa7df749-66e7-4986-a27f-e2f04ae53772}')
    @commethod(3)
    def GetProviderMgmtInterface(self, ProviderId: Guid, InterfaceId: POINTER(Guid), ppItf: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryVolumesSupportedForSnapshots(self, ProviderId: Guid, lContext: Int32, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumMgmtObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QuerySnapshotsByVolume(self, pwszVolumeName: POINTER(UInt16), ProviderId: Guid, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssSnapshotMgmt2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f61ec39-fe82-45f2-a3f0-768b5d427102}')
    @commethod(3)
    def GetMinDiffAreaSize(self, pllMinDiffAreaSize: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssSoftwareSnapshotProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{609e123e-2c5a-44d3-8f01-0b1d9a47d1ff}')
    @commethod(3)
    def SetContext(self, lContext: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSnapshotProperties(self, SnapshotId: Guid, pProp: POINTER(win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Query(self, QueriedObjectId: Guid, eQueriedObjectType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, eReturnedObjectsType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, ppEnum: POINTER(win32more.Windows.Win32.Storage.Vss.IVssEnumObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteSnapshots(self, SourceObjectId: Guid, eSourceObjectType: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE, bForceDelete: win32more.Windows.Win32.Foundation.BOOL, plDeletedSnapshots: POINTER(Int32), pNondeletedSnapshotID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginPrepareSnapshot(self, SnapshotSetId: Guid, SnapshotId: Guid, pwszVolumeName: POINTER(UInt16), lNewContext: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsVolumeSupported(self, pwszVolumeName: POINTER(UInt16), pbSupportedByThisProvider: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsVolumeSnapshotted(self, pwszVolumeName: POINTER(UInt16), pbSnapshotsPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL), plSnapshotCompatibility: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSnapshotProperty(self, SnapshotId: Guid, eSnapshotPropertyId: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID, vProperty: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RevertToSnapshot(self, SnapshotId: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryRevertStatus(self, pwszVolume: POINTER(UInt16), ppAsync: POINTER(win32more.Windows.Win32.Storage.Vss.IVssAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssWMDependency(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetWriterId(self, pWriterId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLogicalPath(self, pbstrLogicalPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetComponentName(self, pbstrComponentName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssWMFiledesc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetPath(self, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFilespec(self, pbstrFilespec: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecursive(self, pbRecursive: POINTER(Boolean)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAlternateLocation(self, pbstrAlternateLocation: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBackupTypeMask(self, pdwTypeMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVssWriterComponents(ComPtr):
    extends: None
    @commethod(0)
    def GetComponentCount(self, pcComponents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def GetWriterInfo(self, pidInstance: POINTER(Guid), pidWriter: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(2)
    def GetComponent(self, iComponent: UInt32, ppComponent: POINTER(win32more.Windows.Win32.Storage.Vss.IVssComponent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
VSSCoordinator = Guid('{e579ab5f-1cc4-44b4-bed9-de0991ff0623}')
VSS_ALTERNATE_WRITER_STATE = Int32
VSS_AWS_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_ALTERNATE_WRITER_STATE = 0
VSS_AWS_NO_ALTERNATE_WRITER: win32more.Windows.Win32.Storage.Vss.VSS_ALTERNATE_WRITER_STATE = 1
VSS_AWS_ALTERNATE_WRITER_EXISTS: win32more.Windows.Win32.Storage.Vss.VSS_ALTERNATE_WRITER_STATE = 2
VSS_AWS_THIS_IS_ALTERNATE_WRITER: win32more.Windows.Win32.Storage.Vss.VSS_ALTERNATE_WRITER_STATE = 3
VSS_APPLICATION_LEVEL = Int32
VSS_APP_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = 0
VSS_APP_SYSTEM: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = 1
VSS_APP_BACK_END: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = 2
VSS_APP_FRONT_END: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = 3
VSS_APP_SYSTEM_RM: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = 4
VSS_APP_AUTO: win32more.Windows.Win32.Storage.Vss.VSS_APPLICATION_LEVEL = -1
VSS_BACKUP_SCHEMA = Int32
VSS_BS_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 0
VSS_BS_DIFFERENTIAL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 1
VSS_BS_INCREMENTAL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 2
VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 4
VSS_BS_LOG: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 8
VSS_BS_COPY: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 16
VSS_BS_TIMESTAMPED: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 32
VSS_BS_LAST_MODIFY: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 64
VSS_BS_LSN: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 128
VSS_BS_WRITER_SUPPORTS_NEW_TARGET: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 256
VSS_BS_WRITER_SUPPORTS_RESTORE_WITH_MOVE: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 512
VSS_BS_INDEPENDENT_SYSTEM_STATE: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 1024
VSS_BS_ROLLFORWARD_RESTORE: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 4096
VSS_BS_RESTORE_RENAME: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 8192
VSS_BS_AUTHORITATIVE_RESTORE: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 16384
VSS_BS_WRITER_SUPPORTS_PARALLEL_RESTORES: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_SCHEMA = 32768
VSS_BACKUP_TYPE = Int32
VSS_BT_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 0
VSS_BT_FULL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 1
VSS_BT_INCREMENTAL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 2
VSS_BT_DIFFERENTIAL: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 3
VSS_BT_LOG: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 4
VSS_BT_COPY: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 5
VSS_BT_OTHER: win32more.Windows.Win32.Storage.Vss.VSS_BACKUP_TYPE = 6
VSS_COMPONENT_FLAGS = Int32
VSS_CF_BACKUP_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_FLAGS = 1
VSS_CF_APP_ROLLBACK_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_FLAGS = 2
VSS_CF_NOT_SYSTEM_STATE: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_FLAGS = 4
VSS_COMPONENT_TYPE = Int32
VSS_CT_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE = 0
VSS_CT_DATABASE: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE = 1
VSS_CT_FILEGROUP: win32more.Windows.Win32.Storage.Vss.VSS_COMPONENT_TYPE = 2
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
VSS_RS_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_RESTORE_STATUS = 0
VSS_RS_NONE: win32more.Windows.Win32.Storage.Vss.VSS_FILE_RESTORE_STATUS = 1
VSS_RS_ALL: win32more.Windows.Win32.Storage.Vss.VSS_FILE_RESTORE_STATUS = 2
VSS_RS_FAILED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_RESTORE_STATUS = 3
VSS_FILE_SPEC_BACKUP_TYPE = Int32
VSS_FSBT_FULL_BACKUP_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 1
VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 2
VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 4
VSS_FSBT_LOG_BACKUP_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 8
VSS_FSBT_FULL_SNAPSHOT_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 256
VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 512
VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 1024
VSS_FSBT_LOG_SNAPSHOT_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 2048
VSS_FSBT_CREATED_DURING_BACKUP: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 65536
VSS_FSBT_ALL_BACKUP_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 15
VSS_FSBT_ALL_SNAPSHOT_REQUIRED: win32more.Windows.Win32.Storage.Vss.VSS_FILE_SPEC_BACKUP_TYPE = 3840
VSS_HARDWARE_OPTIONS = Int32
VSS_BREAKEX_FLAG_MASK_LUNS: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 1
VSS_BREAKEX_FLAG_MAKE_READ_WRITE: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 2
VSS_BREAKEX_FLAG_REVERT_IDENTITY_ALL: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 4
VSS_BREAKEX_FLAG_REVERT_IDENTITY_NONE: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 8
VSS_ONLUNSTATECHANGE_NOTIFY_READ_WRITE: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 256
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_PRE_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 512
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_POST_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 1024
VSS_ONLUNSTATECHANGE_DO_MASK_LUNS: win32more.Windows.Win32.Storage.Vss.VSS_HARDWARE_OPTIONS = 2048
class VSS_MGMT_OBJECT_PROP(Structure):
    Type: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_TYPE
    Obj: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_UNION
VSS_MGMT_OBJECT_TYPE = Int32
VSS_MGMT_OBJECT_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_TYPE = 0
VSS_MGMT_OBJECT_VOLUME: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_TYPE = 1
VSS_MGMT_OBJECT_DIFF_VOLUME: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_TYPE = 2
VSS_MGMT_OBJECT_DIFF_AREA: win32more.Windows.Win32.Storage.Vss.VSS_MGMT_OBJECT_TYPE = 3
class VSS_MGMT_OBJECT_UNION(Union):
    Vol: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_PROP
    DiffVol: win32more.Windows.Win32.Storage.Vss.VSS_DIFF_VOLUME_PROP
    DiffArea: win32more.Windows.Win32.Storage.Vss.VSS_DIFF_AREA_PROP
class VSS_OBJECT_PROP(Structure):
    Type: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE
    Obj: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_UNION
VSS_OBJECT_TYPE = Int32
VSS_OBJECT_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 0
VSS_OBJECT_NONE: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 1
VSS_OBJECT_SNAPSHOT_SET: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 2
VSS_OBJECT_SNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 3
VSS_OBJECT_PROVIDER: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 4
VSS_OBJECT_TYPE_COUNT: win32more.Windows.Win32.Storage.Vss.VSS_OBJECT_TYPE = 5
class VSS_OBJECT_UNION(Union):
    Snap: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROP
    Prov: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_PROP
VSS_PROTECTION_FAULT = Int32
VSS_PROTECTION_FAULT_NONE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 0
VSS_PROTECTION_FAULT_DIFF_AREA_MISSING: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 1
VSS_PROTECTION_FAULT_IO_FAILURE_DURING_ONLINE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 2
VSS_PROTECTION_FAULT_META_DATA_CORRUPTION: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 3
VSS_PROTECTION_FAULT_MEMORY_ALLOCATION_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 4
VSS_PROTECTION_FAULT_MAPPED_MEMORY_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 5
VSS_PROTECTION_FAULT_COW_READ_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 6
VSS_PROTECTION_FAULT_COW_WRITE_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 7
VSS_PROTECTION_FAULT_DIFF_AREA_FULL: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 8
VSS_PROTECTION_FAULT_GROW_TOO_SLOW: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 9
VSS_PROTECTION_FAULT_GROW_FAILED: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 10
VSS_PROTECTION_FAULT_DESTROY_ALL_SNAPSHOTS: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 11
VSS_PROTECTION_FAULT_FILE_SYSTEM_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 12
VSS_PROTECTION_FAULT_IO_FAILURE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 13
VSS_PROTECTION_FAULT_DIFF_AREA_REMOVED: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 14
VSS_PROTECTION_FAULT_EXTERNAL_WRITER_TO_DIFF_AREA: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 15
VSS_PROTECTION_FAULT_MOUNT_DURING_CLUSTER_OFFLINE: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT = 16
VSS_PROTECTION_LEVEL = Int32
VSS_PROTECTION_LEVEL_ORIGINAL_VOLUME: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_LEVEL = 0
VSS_PROTECTION_LEVEL_SNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_LEVEL = 1
VSS_PROVIDER_CAPABILITIES = Int32
VSS_PRV_CAPABILITY_LEGACY: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 1
VSS_PRV_CAPABILITY_COMPLIANT: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 2
VSS_PRV_CAPABILITY_LUN_REPOINT: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 4
VSS_PRV_CAPABILITY_LUN_RESYNC: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 8
VSS_PRV_CAPABILITY_OFFLINE_CREATION: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 16
VSS_PRV_CAPABILITY_MULTIPLE_IMPORT: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 32
VSS_PRV_CAPABILITY_RECYCLING: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 64
VSS_PRV_CAPABILITY_PLEX: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 128
VSS_PRV_CAPABILITY_DIFFERENTIAL: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 256
VSS_PRV_CAPABILITY_CLUSTERED: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_CAPABILITIES = 512
class VSS_PROVIDER_PROP(Structure):
    m_ProviderId: Guid
    m_pwszProviderName: POINTER(UInt16)
    m_eProviderType: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE
    m_pwszProviderVersion: POINTER(UInt16)
    m_ProviderVersionId: Guid
    m_ClassId: Guid
VSS_PROVIDER_TYPE = Int32
VSS_PROV_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE = 0
VSS_PROV_SYSTEM: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE = 1
VSS_PROV_SOFTWARE: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE = 2
VSS_PROV_HARDWARE: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE = 3
VSS_PROV_FILESHARE: win32more.Windows.Win32.Storage.Vss.VSS_PROVIDER_TYPE = 4
VSS_RECOVERY_OPTIONS = Int32
VSS_RECOVERY_REVERT_IDENTITY_ALL: win32more.Windows.Win32.Storage.Vss.VSS_RECOVERY_OPTIONS = 256
VSS_RECOVERY_NO_VOLUME_CHECK: win32more.Windows.Win32.Storage.Vss.VSS_RECOVERY_OPTIONS = 512
VSS_RESTOREMETHOD_ENUM = Int32
VSS_RME_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 0
VSS_RME_RESTORE_IF_NOT_THERE: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 1
VSS_RME_RESTORE_IF_CAN_REPLACE: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 2
VSS_RME_STOP_RESTORE_START: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 3
VSS_RME_RESTORE_TO_ALTERNATE_LOCATION: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 4
VSS_RME_RESTORE_AT_REBOOT: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 5
VSS_RME_RESTORE_AT_REBOOT_IF_CANNOT_REPLACE: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 6
VSS_RME_CUSTOM: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 7
VSS_RME_RESTORE_STOP_START: win32more.Windows.Win32.Storage.Vss.VSS_RESTOREMETHOD_ENUM = 8
VSS_RESTORE_TARGET = Int32
VSS_RT_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET = 0
VSS_RT_ORIGINAL: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET = 1
VSS_RT_ALTERNATE: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET = 2
VSS_RT_DIRECTED: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET = 3
VSS_RT_ORIGINAL_LOCATION: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TARGET = 4
VSS_RESTORE_TYPE = Int32
VSS_RTYPE_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TYPE = 0
VSS_RTYPE_BY_COPY: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TYPE = 1
VSS_RTYPE_IMPORT: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TYPE = 2
VSS_RTYPE_OTHER: win32more.Windows.Win32.Storage.Vss.VSS_RESTORE_TYPE = 3
VSS_ROLLFORWARD_TYPE = Int32
VSS_RF_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_ROLLFORWARD_TYPE = 0
VSS_RF_NONE: win32more.Windows.Win32.Storage.Vss.VSS_ROLLFORWARD_TYPE = 1
VSS_RF_ALL: win32more.Windows.Win32.Storage.Vss.VSS_ROLLFORWARD_TYPE = 2
VSS_RF_PARTIAL: win32more.Windows.Win32.Storage.Vss.VSS_ROLLFORWARD_TYPE = 3
VSS_SNAPSHOT_COMPATIBILITY = Int32
VSS_SC_DISABLE_DEFRAG: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_COMPATIBILITY = 1
VSS_SC_DISABLE_CONTENTINDEX: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_COMPATIBILITY = 2
VSS_SNAPSHOT_CONTEXT = Int32
VSS_CTX_BACKUP: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 0
VSS_CTX_FILE_SHARE_BACKUP: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 16
VSS_CTX_NAS_ROLLBACK: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 25
VSS_CTX_APP_ROLLBACK: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 9
VSS_CTX_CLIENT_ACCESSIBLE: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 29
VSS_CTX_CLIENT_ACCESSIBLE_WRITERS: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = 13
VSS_CTX_ALL: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_CONTEXT = -1
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
    m_eStatus: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE
VSS_SNAPSHOT_PROPERTY_ID = Int32
VSS_SPROPID_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 0
VSS_SPROPID_SNAPSHOT_ID: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 1
VSS_SPROPID_SNAPSHOT_SET_ID: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 2
VSS_SPROPID_SNAPSHOTS_COUNT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 3
VSS_SPROPID_SNAPSHOT_DEVICE: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 4
VSS_SPROPID_ORIGINAL_VOLUME: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 5
VSS_SPROPID_ORIGINATING_MACHINE: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 6
VSS_SPROPID_SERVICE_MACHINE: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 7
VSS_SPROPID_EXPOSED_NAME: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 8
VSS_SPROPID_EXPOSED_PATH: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 9
VSS_SPROPID_PROVIDER_ID: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 10
VSS_SPROPID_SNAPSHOT_ATTRIBUTES: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 11
VSS_SPROPID_CREATION_TIMESTAMP: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 12
VSS_SPROPID_STATUS: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID = 13
VSS_SNAPSHOT_STATE = Int32
VSS_SS_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 0
VSS_SS_PREPARING: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 1
VSS_SS_PROCESSING_PREPARE: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 2
VSS_SS_PREPARED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 3
VSS_SS_PROCESSING_PRECOMMIT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 4
VSS_SS_PRECOMMITTED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 5
VSS_SS_PROCESSING_COMMIT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 6
VSS_SS_COMMITTED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 7
VSS_SS_PROCESSING_POSTCOMMIT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 8
VSS_SS_PROCESSING_PREFINALCOMMIT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 9
VSS_SS_PREFINALCOMMITTED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 10
VSS_SS_PROCESSING_POSTFINALCOMMIT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 11
VSS_SS_CREATED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 12
VSS_SS_ABORTED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 13
VSS_SS_DELETED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 14
VSS_SS_POSTCOMMITTED: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 15
VSS_SS_COUNT: win32more.Windows.Win32.Storage.Vss.VSS_SNAPSHOT_STATE = 16
VSS_SOURCE_TYPE = Int32
VSS_ST_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_SOURCE_TYPE = 0
VSS_ST_TRANSACTEDDB: win32more.Windows.Win32.Storage.Vss.VSS_SOURCE_TYPE = 1
VSS_ST_NONTRANSACTEDDB: win32more.Windows.Win32.Storage.Vss.VSS_SOURCE_TYPE = 2
VSS_ST_OTHER: win32more.Windows.Win32.Storage.Vss.VSS_SOURCE_TYPE = 3
VSS_SUBSCRIBE_MASK = Int32
VSS_SM_POST_SNAPSHOT_FLAG: win32more.Windows.Win32.Storage.Vss.VSS_SUBSCRIBE_MASK = 1
VSS_SM_BACKUP_EVENTS_FLAG: win32more.Windows.Win32.Storage.Vss.VSS_SUBSCRIBE_MASK = 2
VSS_SM_RESTORE_EVENTS_FLAG: win32more.Windows.Win32.Storage.Vss.VSS_SUBSCRIBE_MASK = 4
VSS_SM_IO_THROTTLING_FLAG: win32more.Windows.Win32.Storage.Vss.VSS_SUBSCRIBE_MASK = 8
VSS_SM_ALL_FLAGS: win32more.Windows.Win32.Storage.Vss.VSS_SUBSCRIBE_MASK = -1
VSS_USAGE_TYPE = Int32
VSS_UT_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE = 0
VSS_UT_BOOTABLESYSTEMSTATE: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE = 1
VSS_UT_SYSTEMSERVICE: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE = 2
VSS_UT_USERDATA: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE = 3
VSS_UT_OTHER: win32more.Windows.Win32.Storage.Vss.VSS_USAGE_TYPE = 4
class VSS_VOLUME_PROP(Structure):
    m_pwszVolumeName: POINTER(UInt16)
    m_pwszVolumeDisplayName: POINTER(UInt16)
class VSS_VOLUME_PROTECTION_INFO(Structure):
    m_protectionLevel: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_LEVEL
    m_volumeIsOfflineForProtection: win32more.Windows.Win32.Foundation.BOOL
    m_protectionFault: win32more.Windows.Win32.Storage.Vss.VSS_PROTECTION_FAULT
    m_failureStatus: Int32
    m_volumeHasUnusedDiffArea: win32more.Windows.Win32.Foundation.BOOL
    m_reserved: UInt32
VSS_VOLUME_SNAPSHOT_ATTRIBUTES = Int32
VSS_VOLSNAP_ATTR_PERSISTENT: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 1
VSS_VOLSNAP_ATTR_NO_AUTORECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 2
VSS_VOLSNAP_ATTR_CLIENT_ACCESSIBLE: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 4
VSS_VOLSNAP_ATTR_NO_AUTO_RELEASE: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 8
VSS_VOLSNAP_ATTR_NO_WRITERS: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 16
VSS_VOLSNAP_ATTR_TRANSPORTABLE: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 32
VSS_VOLSNAP_ATTR_NOT_SURFACED: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 64
VSS_VOLSNAP_ATTR_NOT_TRANSACTED: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 128
VSS_VOLSNAP_ATTR_HARDWARE_ASSISTED: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 65536
VSS_VOLSNAP_ATTR_DIFFERENTIAL: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 131072
VSS_VOLSNAP_ATTR_PLEX: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 262144
VSS_VOLSNAP_ATTR_IMPORTED: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 524288
VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 1048576
VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 2097152
VSS_VOLSNAP_ATTR_AUTORECOVER: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 4194304
VSS_VOLSNAP_ATTR_ROLLBACK_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 8388608
VSS_VOLSNAP_ATTR_DELAYED_POSTSNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 16777216
VSS_VOLSNAP_ATTR_TXF_RECOVERY: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 33554432
VSS_VOLSNAP_ATTR_FILE_SHARE: win32more.Windows.Win32.Storage.Vss.VSS_VOLUME_SNAPSHOT_ATTRIBUTES = 67108864
VSS_WRITERRESTORE_ENUM = Int32
VSS_WRE_UNDEFINED: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM = 0
VSS_WRE_NEVER: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM = 1
VSS_WRE_IF_REPLACE_FAILS: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM = 2
VSS_WRE_ALWAYS: win32more.Windows.Win32.Storage.Vss.VSS_WRITERRESTORE_ENUM = 3
VSS_WRITER_STATE = Int32
VSS_WS_UNKNOWN: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 0
VSS_WS_STABLE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 1
VSS_WS_WAITING_FOR_FREEZE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 2
VSS_WS_WAITING_FOR_THAW: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 3
VSS_WS_WAITING_FOR_POST_SNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 4
VSS_WS_WAITING_FOR_BACKUP_COMPLETE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 5
VSS_WS_FAILED_AT_IDENTIFY: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 6
VSS_WS_FAILED_AT_PREPARE_BACKUP: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 7
VSS_WS_FAILED_AT_PREPARE_SNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 8
VSS_WS_FAILED_AT_FREEZE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 9
VSS_WS_FAILED_AT_THAW: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 10
VSS_WS_FAILED_AT_POST_SNAPSHOT: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 11
VSS_WS_FAILED_AT_BACKUP_COMPLETE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 12
VSS_WS_FAILED_AT_PRE_RESTORE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 13
VSS_WS_FAILED_AT_POST_RESTORE: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 14
VSS_WS_FAILED_AT_BACKUPSHUTDOWN: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 15
VSS_WS_COUNT: win32more.Windows.Win32.Storage.Vss.VSS_WRITER_STATE = 16
VssSnapshotMgmt = Guid('{0b5a2c52-3eb9-470a-96e2-6c6d4570e40f}')


make_ready(__name__)
