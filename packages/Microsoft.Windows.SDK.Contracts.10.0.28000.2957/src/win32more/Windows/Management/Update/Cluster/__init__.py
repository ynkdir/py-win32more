from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management.Update.Cluster
class AcquireEnvironmentInfoResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResult
    _classid_ = 'Windows.Management.Update.Cluster.AcquireEnvironmentInfoResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.AcquireEnvironmentInfoResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, environmentInfo: hstr) -> win32more.Windows.Management.Update.Cluster.AcquireEnvironmentInfoResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_EnvironmentInfo(self: win32more.Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResult) -> hstr: ...
    EnvironmentInfo = property(get_EnvironmentInfo, None)
    Result = property(get_Result, None)
class AreRebootsPendingResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IAreRebootsPendingResult
    _classid_ = 'Windows.Management.Update.Cluster.AreRebootsPendingResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.AreRebootsPendingResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IAreRebootsPendingResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateOperationResult, isRebootPending: Boolean) -> win32more.Windows.Management.Update.Cluster.AreRebootsPendingResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IAreRebootsPendingResult) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_mixinmethod
    def get_IsRebootPending(self: win32more.Windows.Management.Update.Cluster.IAreRebootsPendingResult) -> Boolean: ...
    IsRebootPending = property(get_IsRebootPending, None)
    Result = property(get_Result, None)
class ClusterNativeUpdateCompletionStatus(Enum, Int32):
    _name_ = 'Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus'
    Completed = 0
    Failed = 1
    Canceled = 2
class ClusterNativeUpdateCredentialStatus(Enum, Int32):
    _name_ = 'Windows.Management.Update.Cluster.ClusterNativeUpdateCredentialStatus'
    Success = 0
    NoSuchCredential = 1
    ErrorRetrievingCredential = 2
class ClusterNativeUpdateEnvironmentValidationStatus(Enum, Int32):
    _name_ = 'Windows.Management.Update.Cluster.ClusterNativeUpdateEnvironmentValidationStatus'
    Approved = 0
    ApprovedWithWarnings = 1
    Rejected = 2
class ClusterNativeUpdateLogLevel(Enum, Int32):
    _name_ = 'Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel'
    Debug = 0
    Verbose = 1
    Info = 2
    Warning = 3
    Error = 4
class ClusterNativeUpdateOperationStatus(Enum, Int32):
    _name_ = 'Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus'
    Success = 0
    Failed = 1
    Pending = 2
    Canceled = 3
ClusterNativeUpdatingContract: UInt32 = 65536
class ClusterUpdateServices(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices
    _classid_ = 'Windows.Management.Update.Cluster.ClusterUpdateServices'
    @winrt_mixinmethod
    def WriteLogEntry(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices, level: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel, message: hstr) -> Void: ...
    @winrt_mixinmethod
    def ReportProgress(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices, currentStep: Int32, maxSteps: Int32, message: hstr) -> Void: ...
    @winrt_mixinmethod
    def GetPluginCredential(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices, credentialId: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateCredential: ...
    @winrt_mixinmethod
    def IsOperationMarkedAsCanceled(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices) -> Boolean: ...
    @winrt_mixinmethod
    def SaveRunStateInformation(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices, persistentInformation: hstr) -> Void: ...
    @winrt_mixinmethod
    def GetRunStateInformation(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices) -> hstr: ...
    @winrt_mixinmethod
    def SaveRunIndependentInformation(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices, persistentInformation: hstr) -> Void: ...
    @winrt_mixinmethod
    def GetRunIndependentInformation(self: win32more.Windows.Management.Update.Cluster.IClusterUpdateServices) -> hstr: ...
class IAcquireEnvironmentInfoResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResult'
    _iid_ = Guid('{b720e3a4-9a34-51c1-a1fa-0c6673bef689}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_EnvironmentInfo(self) -> hstr: ...
    EnvironmentInfo = property(get_EnvironmentInfo, None)
    Result = property(get_Result, None)
class IAcquireEnvironmentInfoResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IAcquireEnvironmentInfoResultFactory'
    _iid_ = Guid('{bbe87f45-0125-5b6d-b9de-05effc98becb}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, environmentInfo: hstr) -> win32more.Windows.Management.Update.Cluster.AcquireEnvironmentInfoResult: ...
class IAreRebootsPendingResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IAreRebootsPendingResult'
    _iid_ = Guid('{a0c93ffd-8409-5fe1-876b-d59d5d9951b5}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(7)
    def get_IsRebootPending(self) -> Boolean: ...
    IsRebootPending = property(get_IsRebootPending, None)
    Result = property(get_Result, None)
class IAreRebootsPendingResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IAreRebootsPendingResultFactory'
    _iid_ = Guid('{801c7304-1fdf-59b4-9ef6-adbd0544d98f}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateOperationResult, isRebootPending: Boolean) -> win32more.Windows.Management.Update.Cluster.AreRebootsPendingResult: ...
class IClusterNativeEnvironmentOperations(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IClusterNativeEnvironmentOperations'
    _iid_ = Guid('{a6d3d05e-1cfe-5363-b745-c6981d0e6b25}')
    @winrt_commethod(6)
    def AcquireNodeEnvironmentInfo(self) -> win32more.Windows.Management.Update.Cluster.AcquireEnvironmentInfoResult: ...
    @winrt_commethod(7)
    def ValidateClusterEnvironment(self, nodeEnvironmentInfo: win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]) -> win32more.Windows.Management.Update.Cluster.ValidateClusterEnvironmentResult: ...
    @winrt_commethod(8)
    def StartPreUpdateRunOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(9)
    def IsPreUpdateRunOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(10)
    def StartPostUpdateRunOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(11)
    def IsPostUpdateRunOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
class IClusterNativeEnvironmentOperationsPlugin(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IClusterNativeEnvironmentOperationsPlugin'
    _iid_ = Guid('{534b9984-3201-5a90-a42b-42d9c98c961a}')
    @winrt_commethod(6)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(7)
    def get_FriendlyName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(9)
    def get_Version(self) -> win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo: ...
    @winrt_commethod(10)
    def get_DefaultOptions(self) -> win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]: ...
    @winrt_commethod(11)
    def CreateEnvironmentOperations(self, clusterName: hstr, runId: hstr, options: win32more.Windows.Foundation.Collections.IMap[hstr, hstr], updateServices: win32more.Windows.Management.Update.Cluster.ClusterUpdateServices) -> win32more.Windows.Management.Update.Cluster.IClusterNativeEnvironmentOperations: ...
    DefaultOptions = property(get_DefaultOptions, None)
    Description = property(get_Description, None)
    FriendlyName = property(get_FriendlyName, None)
    Name = property(get_Name, None)
    Version = property(get_Version, None)
class IClusterNativeNodeOperations(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IClusterNativeNodeOperations'
    _iid_ = Guid('{ce23db69-b72b-5204-9d1c-c53d0b2d803d}')
    @winrt_commethod(6)
    def AreAdditionalRebootsPending(self) -> win32more.Windows.Management.Update.Cluster.AreRebootsPendingResult: ...
    @winrt_commethod(7)
    def StartPreRebootOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(8)
    def IsPreRebootOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(9)
    def StartPostRebootOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(10)
    def IsPostRebootOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(11)
    def StartPreDrainOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(12)
    def IsPreDrainOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(13)
    def StartPostResumeOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(14)
    def IsPostResumeOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(15)
    def StartPreUpdateRunOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(16)
    def IsPreUpdateRunOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_commethod(17)
    def StartPostUpdateRunOperation(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(18)
    def IsPostUpdateRunOperationComplete(self) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
class IClusterNativeNodeOperationsPlugin(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IClusterNativeNodeOperationsPlugin'
    _iid_ = Guid('{5f7a457c-e9d3-5cec-a967-0da9d95fd6f4}')
    @winrt_commethod(6)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(7)
    def get_FriendlyName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(9)
    def get_Version(self) -> win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo: ...
    @winrt_commethod(10)
    def get_DefaultOptions(self) -> win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]: ...
    @winrt_commethod(11)
    def CreateNodeOperations(self, clusterName: hstr, runId: hstr, options: win32more.Windows.Foundation.Collections.IMap[hstr, hstr], updateServices: win32more.Windows.Management.Update.Cluster.ClusterUpdateServices) -> win32more.Windows.Management.Update.Cluster.IClusterNativeNodeOperations: ...
    DefaultOptions = property(get_DefaultOptions, None)
    Description = property(get_Description, None)
    FriendlyName = property(get_FriendlyName, None)
    Name = property(get_Name, None)
    Version = property(get_Version, None)
class IClusterUpdateServices(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IClusterUpdateServices'
    _iid_ = Guid('{38461e68-1445-53e3-b914-ce19e3b730c4}')
    @winrt_commethod(6)
    def WriteLogEntry(self, level: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel, message: hstr) -> Void: ...
    @winrt_commethod(7)
    def ReportProgress(self, currentStep: Int32, maxSteps: Int32, message: hstr) -> Void: ...
    @winrt_commethod(8)
    def GetPluginCredential(self, credentialId: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateCredential: ...
    @winrt_commethod(9)
    def IsOperationMarkedAsCanceled(self) -> Boolean: ...
    @winrt_commethod(10)
    def SaveRunStateInformation(self, persistentInformation: hstr) -> Void: ...
    @winrt_commethod(11)
    def GetRunStateInformation(self) -> hstr: ...
    @winrt_commethod(12)
    def SaveRunIndependentInformation(self, persistentInformation: hstr) -> Void: ...
    @winrt_commethod(13)
    def GetRunIndependentInformation(self) -> hstr: ...
class IInstallUpdateTaskResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IInstallUpdateTaskResult'
    _iid_ = Guid('{d519090a-4e93-5916-92bb-9356da52344b}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_InstallRecords(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]: ...
    @winrt_commethod(8)
    def get_ShouldRollback(self) -> Boolean: ...
    InstallRecords = property(get_InstallRecords, None)
    Result = property(get_Result, None)
    ShouldRollback = property(get_ShouldRollback, None)
class IInstallUpdateTaskResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IInstallUpdateTaskResultFactory'
    _iid_ = Guid('{07473356-1a87-554d-9c14-489c0d69b258}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, installRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord], shouldRollback: Boolean) -> win32more.Windows.Management.Update.Cluster.InstallUpdateTaskResult: ...
class IRollbackUpdateTaskResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IRollbackUpdateTaskResult'
    _iid_ = Guid('{477e2a95-bcb6-5044-ad3d-e4180efcf1be}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_InstallRecords(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]: ...
    InstallRecords = property(get_InstallRecords, None)
    Result = property(get_Result, None)
class IRollbackUpdateTaskResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IRollbackUpdateTaskResultFactory'
    _iid_ = Guid('{2dbd5bc3-efdf-5046-8954-78981796f016}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, installRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]) -> win32more.Windows.Management.Update.Cluster.RollbackUpdateTaskResult: ...
class IScanUpdateTaskResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IScanUpdateTaskResult'
    _iid_ = Guid('{24e9f302-a976-5148-b109-5100ac1a50ed}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_ScanRecords(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]: ...
    Result = property(get_Result, None)
    ScanRecords = property(get_ScanRecords, None)
class IScanUpdateTaskResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IScanUpdateTaskResultFactory'
    _iid_ = Guid('{12594ad2-5312-5f8a-8fa2-2da4a34e3319}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, scanRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.ScanUpdateTaskResult: ...
class IStageUpdateTaskResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IStageUpdateTaskResult'
    _iid_ = Guid('{c926add1-335c-57f7-8dac-1ce2fce65060}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_StageRecords(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateStageRecord]: ...
    Result = property(get_Result, None)
    StageRecords = property(get_StageRecords, None)
class IStageUpdateTaskResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IStageUpdateTaskResultFactory'
    _iid_ = Guid('{2256548a-f175-5143-888a-f49f27a34ed3}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, stageRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateStageRecord]) -> win32more.Windows.Management.Update.Cluster.StageUpdateTaskResult: ...
class IUpdateCredential(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateCredential'
    _iid_ = Guid('{de6d09b1-bcdb-5d6d-9d46-7250b853fffe}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCredentialStatus: ...
    @winrt_commethod(7)
    def get_UserName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Password(self) -> hstr: ...
    Password = property(get_Password, None)
    Status = property(get_Status, None)
    UserName = property(get_UserName, None)
class IUpdateCredentialFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateCredentialFactory'
    _iid_ = Guid('{e251a298-44b1-5455-8b44-5971bd516f09}')
    @winrt_commethod(6)
    def CreateInstance(self, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCredentialStatus, userName: hstr, password: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateCredential: ...
class IUpdateInstallRecord(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateInstallRecord'
    _iid_ = Guid('{38118797-dc5d-5727-89ff-5b8a44b3f53b}')
    @winrt_commethod(6)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_IsRebootRequired(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus: ...
    @winrt_commethod(9)
    def get_FailureMessage(self) -> hstr: ...
    FailureMessage = property(get_FailureMessage, None)
    IsRebootRequired = property(get_IsRebootRequired, None)
    Status = property(get_Status, None)
    UpdateId = property(get_UpdateId, None)
class IUpdateInstallRecordFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateInstallRecordFactory'
    _iid_ = Guid('{9b6c54b5-d229-5147-9d6e-16e47f2317db}')
    @winrt_commethod(6)
    def CreateInstance(self, updateId: hstr, isRebootRequired: Boolean, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateInstallRecord: ...
class IUpdateInstaller(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateInstaller'
    _iid_ = Guid('{c8cfe973-daaf-57d3-8d3b-59eec0b082ea}')
    @winrt_commethod(6)
    def Scan(self) -> win32more.Windows.Management.Update.Cluster.ScanUpdateTaskResult: ...
    @winrt_commethod(7)
    def Stage(self, updatesToStage: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.StageUpdateTaskResult: ...
    @winrt_commethod(8)
    def Install(self, updatesToInstall: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.InstallUpdateTaskResult: ...
    @winrt_commethod(9)
    def Rollback(self, updatesToRollback: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.RollbackUpdateTaskResult: ...
    @winrt_commethod(10)
    def ShouldUsePluginSpecificReboot(self, usePluginReboot: POINTER(Boolean)) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(11)
    def RebootNode(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(12)
    def AcquireUpdateListValidationInfo(self, recipeValidationInfo: POINTER(hstr)) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(13)
    def ValidateAllNodesUpdateRecipe(self, allNodesRecipeValidationInfo: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateRecipeNodeValidationInfoRecord]) -> win32more.Windows.Management.Update.Cluster.ValidateAllNodesUpdateRecipeResult: ...
class IUpdateInstallerPlugin(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateInstallerPlugin'
    _iid_ = Guid('{61122faa-0cd8-5a98-8938-5c1f88c632c6}')
    @winrt_commethod(6)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(7)
    def get_FriendlyName(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(9)
    def get_Version(self) -> win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo: ...
    @winrt_commethod(10)
    def get_IsUpdateRollbackSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_DefaultOptions(self) -> win32more.Windows.Foundation.Collections.IMapView[hstr, hstr]: ...
    @winrt_commethod(12)
    def CreateUpdateInstaller(self, clusterName: hstr, runId: hstr, options: win32more.Windows.Foundation.Collections.IMap[hstr, hstr], updateServices: win32more.Windows.Management.Update.Cluster.ClusterUpdateServices) -> win32more.Windows.Management.Update.Cluster.IUpdateInstaller: ...
    DefaultOptions = property(get_DefaultOptions, None)
    Description = property(get_Description, None)
    FriendlyName = property(get_FriendlyName, None)
    IsUpdateRollbackSupported = property(get_IsUpdateRollbackSupported, None)
    Name = property(get_Name, None)
    Version = property(get_Version, None)
class IUpdateOperationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateOperationResult'
    _iid_ = Guid('{9fc35275-3eb7-5785-bb32-0e37bb52cf41}')
    @winrt_commethod(6)
    def get_StatusCode(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus: ...
    @winrt_commethod(7)
    def get_Reason(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Reason = property(get_Reason, None)
    StatusCode = property(get_StatusCode, None)
class IUpdateOperationResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateOperationResultFactory'
    _iid_ = Guid('{ff53c580-e92c-50a9-8811-a057d5a2a523}')
    @winrt_commethod(6)
    def CreateInstance(self, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus, reason: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(7)
    def CreateInstance2(self, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus, reason: hstr, errorCode: Int32) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
class IUpdatePendingOperationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdatePendingOperationResult'
    _iid_ = Guid('{0f83b557-e96a-5f19-9492-99fc8bd83c5d}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_commethod(7)
    def get_SuggestedRecheckInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Result = property(get_Result, None)
    SuggestedRecheckInterval = property(get_SuggestedRecheckInterval, None)
class IUpdatePendingOperationResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdatePendingOperationResultFactory'
    _iid_ = Guid('{45a3b731-d513-5baf-bb44-68b97a938308}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateOperationResult, suggestedRecheckInterval: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
class IUpdatePluginVersionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdatePluginVersionInfo'
    _iid_ = Guid('{0901af2e-b340-5e7e-9898-516fc96add89}')
    @winrt_commethod(6)
    def get_MajorVersion(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MinorVersion(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_PatchLevel(self) -> UInt32: ...
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
    PatchLevel = property(get_PatchLevel, None)
class IUpdatePluginVersionInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdatePluginVersionInfoFactory'
    _iid_ = Guid('{56bb98ce-543c-59f2-810d-4d2cf84ee40e}')
    @winrt_commethod(6)
    def CreateInstance(self, majorVersion: UInt32, minorVersion: UInt32, patchLevel: UInt32) -> win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo: ...
class IUpdateRecipeNodeValidationInfoRecord(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecord'
    _iid_ = Guid('{55dfff15-5556-51c4-80c2-af03f385d429}')
    @winrt_commethod(6)
    def get_NodeName(self) -> hstr: ...
    @winrt_commethod(7)
    def get_RecipeValidationInfo(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ScanResults(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]: ...
    NodeName = property(get_NodeName, None)
    RecipeValidationInfo = property(get_RecipeValidationInfo, None)
    ScanResults = property(get_ScanResults, None)
class IUpdateRecipeNodeValidationInfoRecordFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecordFactory'
    _iid_ = Guid('{e0fa2776-dd6c-5139-a93e-23e2188921af}')
    @winrt_commethod(6)
    def CreateInstance(self, nodeName: hstr, recipeValidationInfo: hstr, scanResults: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.UpdateRecipeNodeValidationInfoRecord: ...
class IUpdateScanRecord(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateScanRecord'
    _iid_ = Guid('{c54af4fb-d316-5480-954f-d1eb51961de5}')
    @winrt_commethod(6)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_UpdateTitle(self) -> hstr: ...
    @winrt_commethod(8)
    def get_UpdateDescription(self) -> hstr: ...
    @winrt_commethod(9)
    def get_IsRebootRequired(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_PluginSpecificData(self) -> hstr: ...
    IsRebootRequired = property(get_IsRebootRequired, None)
    PluginSpecificData = property(get_PluginSpecificData, None)
    UpdateDescription = property(get_UpdateDescription, None)
    UpdateId = property(get_UpdateId, None)
    UpdateTitle = property(get_UpdateTitle, None)
class IUpdateScanRecordFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateScanRecordFactory'
    _iid_ = Guid('{d9a3860e-a05a-58c3-b368-07bb350072d0}')
    @winrt_commethod(6)
    def CreateInstance(self, updateId: hstr, updateTitle: hstr, updateDescription: hstr, isRebootRequired: Boolean, pluginSpecificData: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateScanRecord: ...
class IUpdateStageRecord(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateStageRecord'
    _iid_ = Guid('{60d8edf9-eb18-59d1-badb-5d862f9352e9}')
    @winrt_commethod(6)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus: ...
    @winrt_commethod(8)
    def get_FailureMessage(self) -> hstr: ...
    @winrt_commethod(9)
    def get_UpdatedPluginSpecificData(self) -> hstr: ...
    FailureMessage = property(get_FailureMessage, None)
    Status = property(get_Status, None)
    UpdateId = property(get_UpdateId, None)
    UpdatedPluginSpecificData = property(get_UpdatedPluginSpecificData, None)
class IUpdateStageRecordFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateStageRecordFactory'
    _iid_ = Guid('{b5c12a84-ebf5-505b-872f-4de71fdda7e8}')
    @winrt_commethod(6)
    def CreateInstance(self, updateId: hstr, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateStageRecord: ...
    @winrt_commethod(7)
    def CreateInstance2(self, updateId: hstr, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr, updatedPluginSpecificData: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateStageRecord: ...
class IUpdateTaskResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateTaskResult'
    _iid_ = Guid('{3fdd9274-7686-5cb9-89e4-6d618ed3a47a}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Reason(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Reason = property(get_Reason, None)
    Succeeded = property(get_Succeeded, None)
class IUpdateTaskResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateTaskResultFactory'
    _iid_ = Guid('{c5ae4ce3-7d1e-50bf-a64a-95f34783fc8c}')
    @winrt_commethod(6)
    def CreateInstance(self, succeeded: Boolean, reason: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def CreateInstance2(self, succeeded: Boolean, reason: hstr, errorCode: Int32) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
class IUpdateValidationLogMessage(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateValidationLogMessage'
    _iid_ = Guid('{1e55bbd5-648f-584c-904d-ae6a053e80c8}')
    @winrt_commethod(6)
    def get_Severity(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel: ...
    @winrt_commethod(7)
    def get_Message(self) -> hstr: ...
    Message = property(get_Message, None)
    Severity = property(get_Severity, None)
class IUpdateValidationLogMessageFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IUpdateValidationLogMessageFactory'
    _iid_ = Guid('{9005a873-4c0b-5c78-a433-be5095b0226e}')
    @winrt_commethod(6)
    def CreateInstance(self, severity: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel, message: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage: ...
class IValidateAllNodesUpdateRecipeResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResult'
    _iid_ = Guid('{4a6adcd4-b621-5ca6-b82e-6ce96d2a3b93}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_AreUpdatesApproved(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ValidationMessages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]: ...
    AreUpdatesApproved = property(get_AreUpdatesApproved, None)
    Result = property(get_Result, None)
    ValidationMessages = property(get_ValidationMessages, None)
class IValidateAllNodesUpdateRecipeResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResultFactory'
    _iid_ = Guid('{00a73e76-0643-5793-ba1c-6e7aa89fdba6}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, areUpdatesApproved: Boolean, validationMessages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]) -> win32more.Windows.Management.Update.Cluster.ValidateAllNodesUpdateRecipeResult: ...
class IValidateClusterEnvironmentResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IValidateClusterEnvironmentResult'
    _iid_ = Guid('{4df22928-9fde-5c16-961c-aab26f4a7780}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_commethod(7)
    def get_ApprovalStatus(self) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateEnvironmentValidationStatus: ...
    @winrt_commethod(8)
    def get_ValidationMessages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]: ...
    ApprovalStatus = property(get_ApprovalStatus, None)
    Result = property(get_Result, None)
    ValidationMessages = property(get_ValidationMessages, None)
class IValidateClusterEnvironmentResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.Cluster.IValidateClusterEnvironmentResultFactory'
    _iid_ = Guid('{9222e2a5-7106-5dc4-860e-6634e47299fc}')
    @winrt_commethod(6)
    def CreateInstance(self, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, approvalStatus: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateEnvironmentValidationStatus, validationMessages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]) -> win32more.Windows.Management.Update.Cluster.ValidateClusterEnvironmentResult: ...
class InstallUpdateTaskResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IInstallUpdateTaskResult
    _classid_ = 'Windows.Management.Update.Cluster.InstallUpdateTaskResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.InstallUpdateTaskResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IInstallUpdateTaskResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, installRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord], shouldRollback: Boolean) -> win32more.Windows.Management.Update.Cluster.InstallUpdateTaskResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IInstallUpdateTaskResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_InstallRecords(self: win32more.Windows.Management.Update.Cluster.IInstallUpdateTaskResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]: ...
    @winrt_mixinmethod
    def get_ShouldRollback(self: win32more.Windows.Management.Update.Cluster.IInstallUpdateTaskResult) -> Boolean: ...
    InstallRecords = property(get_InstallRecords, None)
    Result = property(get_Result, None)
    ShouldRollback = property(get_ShouldRollback, None)
class RollbackUpdateTaskResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IRollbackUpdateTaskResult
    _classid_ = 'Windows.Management.Update.Cluster.RollbackUpdateTaskResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.RollbackUpdateTaskResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IRollbackUpdateTaskResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, installRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]) -> win32more.Windows.Management.Update.Cluster.RollbackUpdateTaskResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IRollbackUpdateTaskResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_InstallRecords(self: win32more.Windows.Management.Update.Cluster.IRollbackUpdateTaskResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateInstallRecord]: ...
    InstallRecords = property(get_InstallRecords, None)
    Result = property(get_Result, None)
class ScanUpdateTaskResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IScanUpdateTaskResult
    _classid_ = 'Windows.Management.Update.Cluster.ScanUpdateTaskResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.ScanUpdateTaskResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IScanUpdateTaskResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, scanRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.ScanUpdateTaskResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IScanUpdateTaskResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_ScanRecords(self: win32more.Windows.Management.Update.Cluster.IScanUpdateTaskResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]: ...
    Result = property(get_Result, None)
    ScanRecords = property(get_ScanRecords, None)
class StageUpdateTaskResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IStageUpdateTaskResult
    _classid_ = 'Windows.Management.Update.Cluster.StageUpdateTaskResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.StageUpdateTaskResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IStageUpdateTaskResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, stageRecords: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateStageRecord]) -> win32more.Windows.Management.Update.Cluster.StageUpdateTaskResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IStageUpdateTaskResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_StageRecords(self: win32more.Windows.Management.Update.Cluster.IStageUpdateTaskResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateStageRecord]: ...
    Result = property(get_Result, None)
    StageRecords = property(get_StageRecords, None)
class UpdateCredential(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateCredential
    _classid_ = 'Windows.Management.Update.Cluster.UpdateCredential'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateCredential.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateCredentialFactory, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCredentialStatus, userName: hstr, password: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateCredential: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.Update.Cluster.IUpdateCredential) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCredentialStatus: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Management.Update.Cluster.IUpdateCredential) -> hstr: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Windows.Management.Update.Cluster.IUpdateCredential) -> hstr: ...
    Password = property(get_Password, None)
    Status = property(get_Status, None)
    UserName = property(get_UserName, None)
class UpdateInstallRecord(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecord
    _classid_ = 'Windows.Management.Update.Cluster.UpdateInstallRecord'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateInstallRecord.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecordFactory, updateId: hstr, isRebootRequired: Boolean, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateInstallRecord: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_IsRebootRequired(self: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecord) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecord) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus: ...
    @winrt_mixinmethod
    def get_FailureMessage(self: win32more.Windows.Management.Update.Cluster.IUpdateInstallRecord) -> hstr: ...
    FailureMessage = property(get_FailureMessage, None)
    IsRebootRequired = property(get_IsRebootRequired, None)
    Status = property(get_Status, None)
    UpdateId = property(get_UpdateId, None)
class UpdateOperationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateOperationResult
    _classid_ = 'Windows.Management.Update.Cluster.UpdateOperationResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateOperationResult.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateOperationResult.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateOperationResultFactory, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus, reason: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.Cluster.IUpdateOperationResultFactory, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus, reason: hstr, errorCode: Int32) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Windows.Management.Update.Cluster.IUpdateOperationResult) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateOperationStatus: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.Cluster.IUpdateOperationResult) -> hstr: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Management.Update.Cluster.IUpdateOperationResult) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Reason = property(get_Reason, None)
    StatusCode = property(get_StatusCode, None)
class UpdatePendingOperationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdatePendingOperationResult
    _classid_ = 'Windows.Management.Update.Cluster.UpdatePendingOperationResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdatePendingOperationResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateOperationResult, suggestedRecheckInterval: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Management.Update.Cluster.UpdatePendingOperationResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IUpdatePendingOperationResult) -> win32more.Windows.Management.Update.Cluster.UpdateOperationResult: ...
    @winrt_mixinmethod
    def get_SuggestedRecheckInterval(self: win32more.Windows.Management.Update.Cluster.IUpdatePendingOperationResult) -> win32more.Windows.Foundation.TimeSpan: ...
    Result = property(get_Result, None)
    SuggestedRecheckInterval = property(get_SuggestedRecheckInterval, None)
class UpdatePluginVersionInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdatePluginVersionInfo
    _classid_ = 'Windows.Management.Update.Cluster.UpdatePluginVersionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdatePluginVersionInfoFactory, majorVersion: UInt32, minorVersion: UInt32, patchLevel: UInt32) -> win32more.Windows.Management.Update.Cluster.UpdatePluginVersionInfo: ...
    @winrt_mixinmethod
    def get_MajorVersion(self: win32more.Windows.Management.Update.Cluster.IUpdatePluginVersionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_MinorVersion(self: win32more.Windows.Management.Update.Cluster.IUpdatePluginVersionInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_PatchLevel(self: win32more.Windows.Management.Update.Cluster.IUpdatePluginVersionInfo) -> UInt32: ...
    MajorVersion = property(get_MajorVersion, None)
    MinorVersion = property(get_MinorVersion, None)
    PatchLevel = property(get_PatchLevel, None)
class UpdateRecipeNodeValidationInfoRecord(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecord
    _classid_ = 'Windows.Management.Update.Cluster.UpdateRecipeNodeValidationInfoRecord'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateRecipeNodeValidationInfoRecord.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecordFactory, nodeName: hstr, recipeValidationInfo: hstr, scanResults: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]) -> win32more.Windows.Management.Update.Cluster.UpdateRecipeNodeValidationInfoRecord: ...
    @winrt_mixinmethod
    def get_NodeName(self: win32more.Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_RecipeValidationInfo(self: win32more.Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_ScanResults(self: win32more.Windows.Management.Update.Cluster.IUpdateRecipeNodeValidationInfoRecord) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateScanRecord]: ...
    NodeName = property(get_NodeName, None)
    RecipeValidationInfo = property(get_RecipeValidationInfo, None)
    ScanResults = property(get_ScanResults, None)
class UpdateScanRecord(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord
    _classid_ = 'Windows.Management.Update.Cluster.UpdateScanRecord'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateScanRecord.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateScanRecordFactory, updateId: hstr, updateTitle: hstr, updateDescription: hstr, isRebootRequired: Boolean, pluginSpecificData: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateScanRecord: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdateTitle(self: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdateDescription(self: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_IsRebootRequired(self: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord) -> Boolean: ...
    @winrt_mixinmethod
    def get_PluginSpecificData(self: win32more.Windows.Management.Update.Cluster.IUpdateScanRecord) -> hstr: ...
    IsRebootRequired = property(get_IsRebootRequired, None)
    PluginSpecificData = property(get_PluginSpecificData, None)
    UpdateDescription = property(get_UpdateDescription, None)
    UpdateId = property(get_UpdateId, None)
    UpdateTitle = property(get_UpdateTitle, None)
class UpdateStageRecord(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateStageRecord
    _classid_ = 'Windows.Management.Update.Cluster.UpdateStageRecord'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateStageRecord.CreateInstance(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateStageRecord.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateStageRecordFactory, updateId: hstr, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateStageRecord: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.Cluster.IUpdateStageRecordFactory, updateId: hstr, status: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus, failureMessage: hstr, updatedPluginSpecificData: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateStageRecord: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.Cluster.IUpdateStageRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.Update.Cluster.IUpdateStageRecord) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateCompletionStatus: ...
    @winrt_mixinmethod
    def get_FailureMessage(self: win32more.Windows.Management.Update.Cluster.IUpdateStageRecord) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdatedPluginSpecificData(self: win32more.Windows.Management.Update.Cluster.IUpdateStageRecord) -> hstr: ...
    FailureMessage = property(get_FailureMessage, None)
    Status = property(get_Status, None)
    UpdateId = property(get_UpdateId, None)
    UpdatedPluginSpecificData = property(get_UpdatedPluginSpecificData, None)
class UpdateTaskResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateTaskResult
    _classid_ = 'Windows.Management.Update.Cluster.UpdateTaskResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateTaskResult.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateTaskResult.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateTaskResultFactory, succeeded: Boolean, reason: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.Cluster.IUpdateTaskResultFactory, succeeded: Boolean, reason: hstr, errorCode: Int32) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.Cluster.IUpdateTaskResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.Cluster.IUpdateTaskResult) -> hstr: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Management.Update.Cluster.IUpdateTaskResult) -> Int32: ...
    ErrorCode = property(get_ErrorCode, None)
    Reason = property(get_Reason, None)
    Succeeded = property(get_Succeeded, None)
class UpdateValidationLogMessage(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IUpdateValidationLogMessage
    _classid_ = 'Windows.Management.Update.Cluster.UpdateValidationLogMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IUpdateValidationLogMessageFactory, severity: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel, message: hstr) -> win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage: ...
    @winrt_mixinmethod
    def get_Severity(self: win32more.Windows.Management.Update.Cluster.IUpdateValidationLogMessage) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateLogLevel: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Management.Update.Cluster.IUpdateValidationLogMessage) -> hstr: ...
    Message = property(get_Message, None)
    Severity = property(get_Severity, None)
class ValidateAllNodesUpdateRecipeResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResult
    _classid_ = 'Windows.Management.Update.Cluster.ValidateAllNodesUpdateRecipeResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.ValidateAllNodesUpdateRecipeResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, areUpdatesApproved: Boolean, validationMessages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]) -> win32more.Windows.Management.Update.Cluster.ValidateAllNodesUpdateRecipeResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_AreUpdatesApproved(self: win32more.Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValidationMessages(self: win32more.Windows.Management.Update.Cluster.IValidateAllNodesUpdateRecipeResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]: ...
    AreUpdatesApproved = property(get_AreUpdatesApproved, None)
    Result = property(get_Result, None)
    ValidationMessages = property(get_ValidationMessages, None)
class ValidateClusterEnvironmentResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.Cluster.IValidateClusterEnvironmentResult
    _classid_ = 'Windows.Management.Update.Cluster.ValidateClusterEnvironmentResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.Cluster.ValidateClusterEnvironmentResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.Cluster.IValidateClusterEnvironmentResultFactory, result: win32more.Windows.Management.Update.Cluster.UpdateTaskResult, approvalStatus: win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateEnvironmentValidationStatus, validationMessages: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]) -> win32more.Windows.Management.Update.Cluster.ValidateClusterEnvironmentResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.Cluster.IValidateClusterEnvironmentResult) -> win32more.Windows.Management.Update.Cluster.UpdateTaskResult: ...
    @winrt_mixinmethod
    def get_ApprovalStatus(self: win32more.Windows.Management.Update.Cluster.IValidateClusterEnvironmentResult) -> win32more.Windows.Management.Update.Cluster.ClusterNativeUpdateEnvironmentValidationStatus: ...
    @winrt_mixinmethod
    def get_ValidationMessages(self: win32more.Windows.Management.Update.Cluster.IValidateClusterEnvironmentResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.Cluster.UpdateValidationLogMessage]: ...
    ApprovalStatus = property(get_ApprovalStatus, None)
    Result = property(get_Result, None)
    ValidationMessages = property(get_ValidationMessages, None)


make_ready(__name__)
