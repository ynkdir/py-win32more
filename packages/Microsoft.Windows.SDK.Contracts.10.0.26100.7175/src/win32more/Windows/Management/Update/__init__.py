from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management.Update
class IPreviewBuildsManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IPreviewBuildsManager'
    _iid_ = Guid('{fa07dd61-7e4f-59f7-7c9f-def9051c5f62}')
    @winrt_commethod(6)
    def get_ArePreviewBuildsAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ArePreviewBuildsAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentState(self) -> win32more.Windows.Management.Update.PreviewBuildsState: ...
    @winrt_commethod(9)
    def SyncAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class IPreviewBuildsManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IPreviewBuildsManagerStatics'
    _iid_ = Guid('{3e422887-b112-5a70-7da1-97d78d32aa29}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
class IPreviewBuildsState(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IPreviewBuildsState'
    _iid_ = Guid('{a2f2903e-b223-5f63-7546-3e8eac070a2e}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class IWindowsSoftwareUpdate(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdate'
    _iid_ = Guid('{d8f19211-98fe-58dd-af0f-470532aa3341}')
    @winrt_commethod(6)
    def get_InstallationType(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType: ...
    @winrt_commethod(7)
    def get_ProviderId(self) -> hstr: ...
    @winrt_commethod(8)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(9)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(10)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(11)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def get_DownloadSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_InstallSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(14)
    def get_SourceVersion(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
    @winrt_commethod(15)
    def get_TargetVersion(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
    @winrt_commethod(16)
    def get_ProductCode(self) -> win32more.Windows.Foundation.IReference[Guid]: ...
    @winrt_commethod(17)
    def get_PackageFamilyName(self) -> hstr: ...
    @winrt_commethod(18)
    def Approve(self, approvalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(19)
    def ApproveCurrentAction(self, approve: Boolean) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(20)
    def get_CurrentAction(self) -> hstr: ...
    @winrt_commethod(21)
    def get_ActionResultInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResultInfo: ...
    @winrt_commethod(22)
    def get_ApprovalInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo: ...
    @winrt_commethod(23)
    def get_ApprovedActions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredInfo(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_commethod(25)
    def get_ActionProgress(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionProgress: ...
    @winrt_commethod(26)
    def get_RestartReason(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason]: ...
    @winrt_commethod(27)
    def get_AppPackageInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo: ...
    @winrt_commethod(28)
    def get_ExecutionInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
    @winrt_commethod(29)
    def get_OptionalInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
    ActionProgress = property(get_ActionProgress, None)
    ActionResultInfo = property(get_ActionResultInfo, None)
    AppPackageInfo = property(get_AppPackageInfo, None)
    ApprovalInfo = property(get_ApprovalInfo, None)
    ApprovedActions = property(get_ApprovedActions, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    CurrentAction = property(get_CurrentAction, None)
    Description = property(get_Description, None)
    DownloadSizeInBytes = property(get_DownloadSizeInBytes, None)
    ExecutionInfo = property(get_ExecutionInfo, None)
    InstallSizeInBytes = property(get_InstallSizeInBytes, None)
    InstallationType = property(get_InstallationType, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    OptionalInfo = property(get_OptionalInfo, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    ProductCode = property(get_ProductCode, None)
    ProviderId = property(get_ProviderId, None)
    RestartReason = property(get_RestartReason, None)
    SourceVersion = property(get_SourceVersion, None)
    TargetVersion = property(get_TargetVersion, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class IWindowsSoftwareUpdateActionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateActionInfo'
    _iid_ = Guid('{2f6723b5-f704-5362-b600-d18808f3973e}')
    @winrt_commethod(6)
    def get_FileName(self) -> hstr: ...
    @winrt_commethod(7)
    def get_FileArguments(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ActionType(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType: ...
    ActionType = property(get_ActionType, None)
    FileArguments = property(get_FileArguments, None)
    FileName = property(get_FileName, None)
class IWindowsSoftwareUpdateActionInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateActionInfoFactory'
    _iid_ = Guid('{5e83b58e-d982-5d93-a7cb-bf6c9b6ee5a6}')
    @winrt_commethod(6)
    def CreateInstance(self, fileName: hstr, fileArguments: hstr, actionType: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
class IWindowsSoftwareUpdateActionProgress(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateActionProgress'
    _iid_ = Guid('{17dc15fd-75f2-522b-b555-359da8de5581}')
    @winrt_commethod(6)
    def get_Action(self) -> hstr: ...
    @winrt_commethod(7)
    def get_CurrentProgress(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_TotalProgress(self) -> UInt64: ...
    Action = property(get_Action, None)
    CurrentProgress = property(get_CurrentProgress, None)
    TotalProgress = property(get_TotalProgress, None)
class IWindowsSoftwareUpdateActionResultInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo'
    _iid_ = Guid('{bcf26fba-98c8-51cb-8b7e-1eedc3d82a69}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ResultCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_Action(self) -> hstr: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
    Timestamp = property(get_Timestamp, None)
class IWindowsSoftwareUpdateAppPackageInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfo'
    _iid_ = Guid('{a5bd59f4-e624-5552-82f9-267a4574a203}')
    @winrt_commethod(6)
    def get_PackageFamilyName(self) -> hstr: ...
    @winrt_commethod(7)
    def get_PackageArchitecture(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateArchitecture: ...
    @winrt_commethod(8)
    def get_InstallUri(self) -> win32more.Windows.Foundation.Uri: ...
    InstallUri = property(get_InstallUri, None)
    PackageArchitecture = property(get_PackageArchitecture, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class IWindowsSoftwareUpdateAppPackageInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfoFactory'
    _iid_ = Guid('{a8bda639-a4f6-5a4a-8a54-26c1c508cd0f}')
    @winrt_commethod(6)
    def CreateInstance(self, packageFamilyName: hstr, packageArchitecture: win32more.Windows.Management.Update.WindowsSoftwareUpdateArchitecture, installUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo: ...
class IWindowsSoftwareUpdateApprovalInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo'
    _iid_ = Guid('{691e6b9e-80af-5882-9404-25437ecb791b}')
    @winrt_commethod(6)
    def get_UserInitiated(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppClosure(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MeteredNetwork(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Seeker(self) -> Boolean: ...
    AppClosure = property(get_AppClosure, None)
    MeteredNetwork = property(get_MeteredNetwork, None)
    Seeker = property(get_Seeker, None)
    UserInitiated = property(get_UserInitiated, None)
class IWindowsSoftwareUpdateApprovalInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfoFactory'
    _iid_ = Guid('{ab291c7c-d29f-5ac5-b447-0bfcabdc2cc3}')
    @winrt_commethod(6)
    def CreateInstance(self, userInitiated: Boolean, appClosure: Boolean, meteredNetwork: Boolean, seeker: Boolean) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo: ...
class IWindowsSoftwareUpdateExecutionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo'
    _iid_ = Guid('{091aea19-9128-5f24-afc1-a62252df55c0}')
    @winrt_commethod(6)
    def get_DownloadInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_commethod(7)
    def get_InstallInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_commethod(8)
    def get_DeployInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_commethod(9)
    def get_OptionalActionInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo: ...
    DeployInfo = property(get_DeployInfo, None)
    DownloadInfo = property(get_DownloadInfo, None)
    InstallInfo = property(get_InstallInfo, None)
    OptionalActionInfo = property(get_OptionalActionInfo, None)
class IWindowsSoftwareUpdateExecutionInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfoFactory'
    _iid_ = Guid('{88596f7e-b9ef-5583-8135-94d62ed66ed4}')
    @winrt_commethod(6)
    def CreateInstance(self, downloadInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, installInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, actions: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
    @winrt_commethod(7)
    def CreateInstance2(self, deployInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, actions: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
class IWindowsSoftwareUpdateFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateFactory'
    _iid_ = Guid('{28e7e01b-4225-52c8-bb51-c68f0b071be5}')
    @winrt_commethod(6)
    def CreateInstance(self, providerId: hstr, installationType: win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType, updateId: hstr, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, downloadSizeInBytes: UInt64, installSizeInBytes: UInt64, sourceVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, targetVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, appPackageInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo, executionInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo, optionalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdate: ...
    @winrt_commethod(7)
    def CreateInstance2(self, providerId: hstr, installationType: win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType, updateId: hstr, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, downloadSizeInBytes: UInt64, installSizeInBytes: UInt64, productCode: win32more.Windows.Foundation.IReference[Guid], packageFamilyName: hstr, sourceVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, targetVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, appPackageInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo, executionInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo, optionalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdate: ...
class IWindowsSoftwareUpdateLocalizationInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo'
    _iid_ = Guid('{adc2de4b-5966-5f9f-ae07-00d4a285d933}')
    @winrt_commethod(6)
    def get_LanguageId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(9)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    Description = property(get_Description, None)
    LanguageId = property(get_LanguageId, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Title = property(get_Title, None)
class IWindowsSoftwareUpdateLocalizationInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfoFactory'
    _iid_ = Guid('{76979b24-f5bd-5c8c-bdb7-a46187374aff}')
    @winrt_commethod(6)
    def CreateInstance(self, languageId: UInt32, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo: ...
class IWindowsSoftwareUpdateOptionalActionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfo'
    _iid_ = Guid('{4ac035d0-e50e-5ccb-bfd8-a303562891d2}')
    @winrt_commethod(6)
    def get_CloseAndDeployInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_commethod(7)
    def get_CloseAndInstallInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_commethod(8)
    def get_CloseAndRestartInfo(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    CloseAndDeployInfo = property(get_CloseAndDeployInfo, None)
    CloseAndInstallInfo = property(get_CloseAndInstallInfo, None)
    CloseAndRestartInfo = property(get_CloseAndRestartInfo, None)
class IWindowsSoftwareUpdateOptionalActionInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfoFactory'
    _iid_ = Guid('{88d2fcc1-4791-51b6-b988-966ef93a180b}')
    @winrt_commethod(6)
    def CreateInstance(self, closeAndDeployInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, closeAndInstallInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, closeAndRestartInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo: ...
class IWindowsSoftwareUpdateOptionalInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfo'
    _iid_ = Guid('{78084a73-50c4-5c33-a751-7a121f5aae70}')
    @winrt_commethod(6)
    def get_LocalizationInfo(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo]: ...
    @winrt_commethod(7)
    def get_ComplianceDeadlineInDays(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(8)
    def get_ComplianceGracePeriodInDays(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, None)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, None)
    LocalizationInfo = property(get_LocalizationInfo, None)
class IWindowsSoftwareUpdateOptionalInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfoFactory'
    _iid_ = Guid('{d837deed-a5f2-5c89-8beb-852d2897b2ef}')
    @winrt_commethod(6)
    def CreateInstance(self, complianceDeadlineInDays: win32more.Windows.Foundation.IReference[Int32], complianceGracePeriodInDays: win32more.Windows.Foundation.IReference[Int32]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
    @winrt_commethod(7)
    def CreateInstance2(self, localizationInfo: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo], complianceDeadlineInDays: win32more.Windows.Foundation.IReference[Int32], complianceGracePeriodInDays: win32more.Windows.Foundation.IReference[Int32]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
class IWindowsSoftwareUpdateProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProvider'
    _iid_ = Guid('{20b67f4a-e28e-5d20-9c00-bf249922efbe}')
    @winrt_commethod(6)
    def Register(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(7)
    def Unregister(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(8)
    def Validate(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(9)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(10)
    def get_Version(self) -> hstr: ...
    @winrt_commethod(11)
    def get_FolderPath(self) -> hstr: ...
    @winrt_commethod(12)
    def get_CatalogFile(self) -> hstr: ...
    @winrt_commethod(13)
    def get_ScanFileName(self) -> hstr: ...
    @winrt_commethod(14)
    def get_ScanFileArguments(self) -> hstr: ...
    @winrt_commethod(15)
    def get_Type(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderType: ...
    @winrt_commethod(16)
    def get_PayloadFiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderPayloadFileInfo]: ...
    @winrt_commethod(17)
    def get_TrustState(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderTrustState: ...
    @winrt_commethod(18)
    def get_RegistrationType(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderRegistrationType: ...
    @winrt_commethod(19)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.PropertySet: ...
    @winrt_commethod(20)
    def GetPropertyValue(self, name: hstr) -> IInspectable: ...
    CatalogFile = property(get_CatalogFile, None)
    FolderPath = property(get_FolderPath, None)
    Id = property(get_Id, None)
    PayloadFiles = property(get_PayloadFiles, None)
    Properties = property(get_Properties, None)
    RegistrationType = property(get_RegistrationType, None)
    ScanFileArguments = property(get_ScanFileArguments, None)
    ScanFileName = property(get_ScanFileName, None)
    TrustState = property(get_TrustState, None)
    Type = property(get_Type, None)
    Version = property(get_Version, None)
class IWindowsSoftwareUpdateProviderActionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult'
    _iid_ = Guid('{afd92b50-6bb9-54de-bdda-9dfb6cc17c16}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResult: ...
    @winrt_commethod(7)
    def get_RestartReason(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason: ...
    @winrt_commethod(8)
    def get_ResultCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> UInt64: ...
    ExtendedError = property(get_ExtendedError, None)
    RestartReason = property(get_RestartReason, None)
    Result = property(get_Result, None)
    ResultCode = property(get_ResultCode, None)
class IWindowsSoftwareUpdateProviderActionResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResultFactory'
    _iid_ = Guid('{0c002684-30c9-59e9-b53f-8846a85d2dc6}')
    @winrt_commethod(6)
    def CreateInstance(self, actionResult: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResult, restartReason: win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult: ...
class IWindowsSoftwareUpdateProviderFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderFactory'
    _iid_ = Guid('{fc0d5fc4-e15e-5116-b2ed-db0a64997ffa}')
    @winrt_commethod(6)
    def CreateInstance(self, folderPath: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProvider: ...
class IWindowsSoftwareUpdateProviderPayloadFileInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo'
    _iid_ = Guid('{f1da16da-1b01-5367-b4ae-20db8cae1e9b}')
    @winrt_commethod(6)
    def get_Filename(self) -> hstr: ...
    @winrt_commethod(7)
    def get_FileHash(self) -> hstr: ...
    @winrt_commethod(8)
    def get_CatalogFile(self) -> hstr: ...
    @winrt_commethod(9)
    def get_TrustState(self) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderTrustState: ...
    CatalogFile = property(get_CatalogFile, None)
    FileHash = property(get_FileHash, None)
    Filename = property(get_Filename, None)
    TrustState = property(get_TrustState, None)
class IWindowsSoftwareUpdateProviderStatus(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus'
    _iid_ = Guid('{076741b8-7a8e-53b6-9fb7-e290b13c52e9}')
    @winrt_commethod(6)
    def add_CancelRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderStatus, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CancelRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def SetScanResult(self, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(9)
    def SetActionProgress(self, current: UInt64, total: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(10)
    def SetActionResult(self, actionResult: win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    CancelRequested = event(add_CancelRequested, remove_CancelRequested)
class IWindowsSoftwareUpdateProviderStatusFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateProviderStatusFactory'
    _iid_ = Guid('{d1e1b416-7dfd-55ef-9e3c-18d1459e3123}')
    @winrt_commethod(6)
    def CreateInstance(self, providerId: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderStatus: ...
class IWindowsSoftwareUpdateResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateResult'
    _iid_ = Guid('{a6d7ed98-6212-5ad3-aa9d-15e83bb85ee4}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CancelRequested(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ResultCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> UInt64: ...
    CancelRequested = property(get_CancelRequested, None)
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
class IWindowsSoftwareUpdateResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateResultFactory'
    _iid_ = Guid('{512ce0bf-9977-5301-9b29-9e5042c8cf7d}')
    @winrt_commethod(6)
    def CreateInstance(self, succeeded: Boolean, resultCode: UInt32) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(7)
    def CreateInstance2(self, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_commethod(8)
    def CreateInstance3(self, succeeded: Boolean, cancelRequested: Boolean, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
class IWindowsSoftwareUpdateScanResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateScanResult'
    _iid_ = Guid('{43ca6d96-3e6d-56da-a903-65d4ab729299}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ResultCode(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_Updates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdate]: ...
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
    Updates = property(get_Updates, None)
class IWindowsSoftwareUpdateScanResultFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateScanResultFactory'
    _iid_ = Guid('{21148e4c-e7ce-574e-bfa7-69dc77457d21}')
    @winrt_commethod(6)
    def CreateInstance(self, succeeded: Boolean, resultCode: UInt32, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
    @winrt_commethod(7)
    def CreateInstance2(self, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
class IWindowsSoftwareUpdateVersion(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateVersion'
    _iid_ = Guid('{215e22e7-6d57-5305-9c79-4ecd4a4d7871}')
    @winrt_commethod(6)
    def get_Major(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Minor(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_RevisionMajor(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_RevisionMinor(self) -> UInt32: ...
    Major = property(get_Major, None)
    Minor = property(get_Minor, None)
    RevisionMajor = property(get_RevisionMajor, None)
    RevisionMinor = property(get_RevisionMinor, None)
class IWindowsSoftwareUpdateVersionFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsSoftwareUpdateVersionFactory'
    _iid_ = Guid('{650ed994-0858-5528-a1f2-f73ca64dabc9}')
    @winrt_commethod(6)
    def CreateInstance(self, major: UInt32, minor: UInt32, revisionMajor: UInt32, revisionMinor: UInt32) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
class IWindowsUpdate(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdate'
    _iid_ = Guid('{c3c88dd7-0ef3-52b2-a9ad-66bfc6bd9582}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(9)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(10)
    def get_IsFeatureUpdate(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsMinorImpact(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsSecurity(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsCritical(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsForOS(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsDriver(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsMandatory(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsUrgent(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsSeeker(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(20)
    def get_SupportUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(21)
    def get_IsEulaAccepted(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_EulaText(self) -> hstr: ...
    @winrt_commethod(23)
    def get_Deadline(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredInfo(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_commethod(25)
    def get_ActionResult(self) -> win32more.Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_commethod(26)
    def get_CurrentAction(self) -> hstr: ...
    @winrt_commethod(27)
    def get_ActionProgress(self) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_commethod(28)
    def GetPropertyValue(self, propertyName: hstr) -> IInspectable: ...
    @winrt_commethod(29)
    def AcceptEula(self) -> Void: ...
    ActionProgress = property(get_ActionProgress, None)
    ActionResult = property(get_ActionResult, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    CurrentAction = property(get_CurrentAction, None)
    Deadline = property(get_Deadline, None)
    Description = property(get_Description, None)
    EulaText = property(get_EulaText, None)
    IsCritical = property(get_IsCritical, None)
    IsDriver = property(get_IsDriver, None)
    IsEulaAccepted = property(get_IsEulaAccepted, None)
    IsFeatureUpdate = property(get_IsFeatureUpdate, None)
    IsForOS = property(get_IsForOS, None)
    IsMandatory = property(get_IsMandatory, None)
    IsMinorImpact = property(get_IsMinorImpact, None)
    IsSecurity = property(get_IsSecurity, None)
    IsSeeker = property(get_IsSeeker, None)
    IsUrgent = property(get_IsUrgent, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    ProviderId = property(get_ProviderId, None)
    SupportUrl = property(get_SupportUrl, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class IWindowsUpdateActionCompletedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs'
    _iid_ = Guid('{2c44b950-a655-5321-aec1-aee762922131}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Action(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    Succeeded = property(get_Succeeded, None)
    Update = property(get_Update, None)
class IWindowsUpdateActionProgress(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionProgress'
    _iid_ = Guid('{83b22d8a-4bb0-549f-ba39-59724882d137}')
    @winrt_commethod(6)
    def get_Action(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Progress(self) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class IWindowsUpdateActionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionResult'
    _iid_ = Guid('{e6692c62-f697-51b7-ab7f-e73e5e688f12}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Action(self) -> hstr: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    Succeeded = property(get_Succeeded, None)
    Timestamp = property(get_Timestamp, None)
class IWindowsUpdateAdministrator(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAdministrator'
    _iid_ = Guid('{7a60181c-ba1e-5cf9-aa65-304120b73d72}')
    @winrt_commethod(6)
    def StartAdministratorScan(self) -> Void: ...
    @winrt_commethod(7)
    def ApproveWindowsUpdateAction(self, updateId: hstr, action: hstr) -> Void: ...
    @winrt_commethod(8)
    def RevokeWindowsUpdateActionApproval(self, updateId: hstr, action: hstr) -> Void: ...
    @winrt_commethod(9)
    def ApproveWindowsUpdate(self, updateId: hstr, approvalData: win32more.Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_commethod(10)
    def RevokeWindowsUpdateApproval(self, updateId: hstr) -> Void: ...
    @winrt_commethod(11)
    def GetUpdates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
class IWindowsUpdateAdministratorStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAdministratorStatics'
    _iid_ = Guid('{013e6d36-ef69-53bc-8db8-c403bca550ed}')
    @winrt_commethod(6)
    def GetRegisteredAdministrator(self, organizationName: hstr) -> win32more.Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_commethod(7)
    def RegisterForAdministration(self, organizationName: hstr, options: win32more.Windows.Management.Update.WindowsUpdateAdministratorOptions) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(8)
    def UnregisterForAdministration(self, organizationName: hstr) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(9)
    def GetRegisteredAdministratorName(self) -> hstr: ...
    @winrt_commethod(10)
    def RequestRestart(self, restartOptions: win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> hstr: ...
    @winrt_commethod(11)
    def CancelRestartRequest(self, requestRestartToken: hstr) -> Void: ...
class IWindowsUpdateApprovalData(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateApprovalData'
    _iid_ = Guid('{aadf5bfd-84db-59bc-85e2-ad4fc1f62f7c}')
    @winrt_commethod(6)
    def get_Seeker(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(7)
    def put_Seeker(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(8)
    def get_AllowDownloadOnMetered(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(9)
    def put_AllowDownloadOnMetered(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(10)
    def get_ComplianceDeadlineInDays(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_ComplianceDeadlineInDays(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(12)
    def get_ComplianceGracePeriodInDays(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def put_ComplianceGracePeriodInDays(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(14)
    def get_OptOutOfAutoReboot(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(15)
    def put_OptOutOfAutoReboot(self, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
    Seeker = property(get_Seeker, put_Seeker)
class IWindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo'
    _iid_ = Guid('{44df2579-74d3-5ffa-b6ce-09e187e1e0ed}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Reason = property(get_Reason, None)
    Timestamp = property(get_Timestamp, None)
class IWindowsUpdateAttentionRequiredReasonChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs'
    _iid_ = Guid('{0627abca-dbb8-524a-b1d2-d9df004eeb31}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Reason(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Reason = property(get_Reason, None)
    Update = property(get_Update, None)
class IWindowsUpdateGetAdministratorResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateGetAdministratorResult'
    _iid_ = Guid('{bb39ffc4-2c42-5b1c-8995-343341c92c50}')
    @winrt_commethod(6)
    def get_Administrator(self) -> win32more.Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class IWindowsUpdateItem(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateItem'
    _iid_ = Guid('{b222e44a-49b6-59bf-a033-ef617cd73a98}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_UpdateId(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(10)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(11)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def get_Category(self) -> hstr: ...
    @winrt_commethod(13)
    def get_Operation(self) -> hstr: ...
    Category = property(get_Category, None)
    Description = property(get_Description, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Operation = property(get_Operation, None)
    ProviderId = property(get_ProviderId, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class IWindowsUpdateManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManager'
    _iid_ = Guid('{5dd966c0-a71a-5602-bbd0-09a70e4573fa}')
    @winrt_commethod(6)
    def add_ScanningStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScanningStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_WorkingStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_WorkingStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ProgressChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateProgressChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ProgressChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_AttentionRequiredReasonChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_AttentionRequiredReasonChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ActionCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateActionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ActionCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ScanCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateScanCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ScanCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def get_IsScanning(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsWorking(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_LastSuccessfulScanTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(21)
    def GetApplicableUpdates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    @winrt_commethod(22)
    def GetMostRecentCompletedUpdates(self, count: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdateItem]: ...
    @winrt_commethod(23)
    def GetMostRecentCompletedUpdatesAsync(self, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdateItem]]: ...
    @winrt_commethod(24)
    def StartScan(self, userInitiated: Boolean) -> Void: ...
    IsScanning = property(get_IsScanning, None)
    IsWorking = property(get_IsWorking, None)
    LastSuccessfulScanTimestamp = property(get_LastSuccessfulScanTimestamp, None)
    ActionCompleted = event(add_ActionCompleted, remove_ActionCompleted)
    AttentionRequiredReasonChanged = event(add_AttentionRequiredReasonChanged, remove_AttentionRequiredReasonChanged)
    ProgressChanged = event(add_ProgressChanged, remove_ProgressChanged)
    ScanCompleted = event(add_ScanCompleted, remove_ScanCompleted)
    ScanningStateChanged = event(add_ScanningStateChanged, remove_ScanningStateChanged)
    WorkingStateChanged = event(add_WorkingStateChanged, remove_WorkingStateChanged)
class IWindowsUpdateManager2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManager2'
    _iid_ = Guid('{564e7683-bd21-57a4-b17f-7bf6350f4c75}')
    @winrt_commethod(6)
    def GetProvider(self, id: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProvider: ...
    @winrt_commethod(7)
    def get_ProviderIds(self) -> ReceiveArray[hstr]: ...
    @winrt_commethod(8)
    def GetApplicableSoftwareUpdates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdate]: ...
    @winrt_commethod(9)
    def PerformScan(self, options: win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
    ProviderIds = property(get_ProviderIds, None)
class IWindowsUpdateManagerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManagerFactory'
    _iid_ = Guid('{1b394df8-decb-5f44-b47c-6ccf3bcfdb37}')
    @winrt_commethod(6)
    def CreateInstance(self, clientId: hstr) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
class IWindowsUpdateManagerFactory2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManagerFactory2'
    _iid_ = Guid('{ba08d663-d160-59b9-9898-97a186ad52ea}')
    @winrt_commethod(6)
    def CreateInstance(self, clientId: hstr, providerIdFilter: PassArray[hstr]) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
class IWindowsUpdateManagerScanOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManagerScanOptions'
    _iid_ = Guid('{b7c30113-5e4b-59d8-99ad-f58d67b2aefc}')
    @winrt_commethod(6)
    def get_IsUserInitiated(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsUserInitiated(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AllowBypassThrottling(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AllowBypassThrottling(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PerformUpdateActions(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_PerformUpdateActions(self, value: Boolean) -> Void: ...
    AllowBypassThrottling = property(get_AllowBypassThrottling, put_AllowBypassThrottling)
    IsUserInitiated = property(get_IsUserInitiated, put_IsUserInitiated)
    PerformUpdateActions = property(get_PerformUpdateActions, put_PerformUpdateActions)
class IWindowsUpdateManagerScanOptionsFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManagerScanOptionsFactory'
    _iid_ = Guid('{1a0f9198-f18d-5cfd-8cb9-08f3fb74da70}')
    @winrt_commethod(6)
    def CreateInstance(self, isUserInitiated: Boolean) -> win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions: ...
class IWindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs'
    _iid_ = Guid('{bbfbdeeb-94c8-5aa7-b0fb-66c67c233b0a}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_ActionProgress(self) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    ActionProgress = property(get_ActionProgress, None)
    Update = property(get_Update, None)
class IWindowsUpdateRestartRequestOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateRestartRequestOptions'
    _iid_ = Guid('{38cfb7d3-4188-5222-905c-6c4443c951ee}')
    @winrt_commethod(6)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Title(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> hstr: ...
    @winrt_commethod(9)
    def put_Description(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_MoreInfoUrl(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(12)
    def get_ComplianceDeadlineInDays(self) -> Int32: ...
    @winrt_commethod(13)
    def put_ComplianceDeadlineInDays(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_ComplianceGracePeriodInDays(self) -> Int32: ...
    @winrt_commethod(15)
    def put_ComplianceGracePeriodInDays(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_OrganizationName(self) -> hstr: ...
    @winrt_commethod(17)
    def put_OrganizationName(self, value: hstr) -> Void: ...
    @winrt_commethod(18)
    def get_OptOutOfAutoReboot(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_OptOutOfAutoReboot(self, value: Boolean) -> Void: ...
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    Description = property(get_Description, put_Description)
    MoreInfoUrl = property(get_MoreInfoUrl, put_MoreInfoUrl)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
    OrganizationName = property(get_OrganizationName, put_OrganizationName)
    Title = property(get_Title, put_Title)
class IWindowsUpdateRestartRequestOptionsFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateRestartRequestOptionsFactory'
    _iid_ = Guid('{75f41d04-0e17-50d0-8c15-6b9d0539b3a9}')
    @winrt_commethod(6)
    def CreateInstance(self, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
class IWindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs'
    _iid_ = Guid('{95b6953e-ba5c-5fe8-b115-12de184a6bb0}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Updates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    ExtendedError = property(get_ExtendedError, None)
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    Updates = property(get_Updates, None)
class PreviewBuildsManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IPreviewBuildsManager
    _classid_ = 'Windows.Management.Update.PreviewBuildsManager'
    @winrt_mixinmethod
    def get_ArePreviewBuildsAllowed(self: win32more.Windows.Management.Update.IPreviewBuildsManager) -> Boolean: ...
    @winrt_mixinmethod
    def put_ArePreviewBuildsAllowed(self: win32more.Windows.Management.Update.IPreviewBuildsManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: win32more.Windows.Management.Update.IPreviewBuildsManager) -> win32more.Windows.Management.Update.PreviewBuildsState: ...
    @winrt_mixinmethod
    def SyncAsync(self: win32more.Windows.Management.Update.IPreviewBuildsManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Management.Update.IPreviewBuildsManagerStatics) -> win32more.Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Management.Update.IPreviewBuildsManagerStatics) -> Boolean: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class PreviewBuildsState(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IPreviewBuildsState
    _classid_ = 'Windows.Management.Update.PreviewBuildsState'
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Management.Update.IPreviewBuildsState) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class WindowsSoftwareUpdate(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdate
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdate'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 13:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdate.CreateInstance(*args))
        elif len(args) == 15:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdate.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateFactory, providerId: hstr, installationType: win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType, updateId: hstr, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, downloadSizeInBytes: UInt64, installSizeInBytes: UInt64, sourceVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, targetVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, appPackageInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo, executionInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo, optionalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdate: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateFactory, providerId: hstr, installationType: win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType, updateId: hstr, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, downloadSizeInBytes: UInt64, installSizeInBytes: UInt64, productCode: win32more.Windows.Foundation.IReference[Guid], packageFamilyName: hstr, sourceVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, targetVersion: win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion, appPackageInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo, executionInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo, optionalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdate: ...
    @winrt_mixinmethod
    def get_InstallationType(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateInstallationType: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_DownloadSizeInBytes(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> UInt64: ...
    @winrt_mixinmethod
    def get_InstallSizeInBytes(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> UInt64: ...
    @winrt_mixinmethod
    def get_SourceVersion(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
    @winrt_mixinmethod
    def get_TargetVersion(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
    @winrt_mixinmethod
    def get_ProductCode(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Foundation.IReference[Guid]: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def Approve(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate, approvalInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def ApproveCurrentAction(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate, approve: Boolean) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def get_CurrentAction(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_ActionResultInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResultInfo: ...
    @winrt_mixinmethod
    def get_ApprovalInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo: ...
    @winrt_mixinmethod
    def get_ApprovedActions(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType]: ...
    @winrt_mixinmethod
    def get_AttentionRequiredInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionProgress: ...
    @winrt_mixinmethod
    def get_RestartReason(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Foundation.IReference[win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason]: ...
    @winrt_mixinmethod
    def get_AppPackageInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo: ...
    @winrt_mixinmethod
    def get_ExecutionInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
    @winrt_mixinmethod
    def get_OptionalInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdate) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
    ActionProgress = property(get_ActionProgress, None)
    ActionResultInfo = property(get_ActionResultInfo, None)
    AppPackageInfo = property(get_AppPackageInfo, None)
    ApprovalInfo = property(get_ApprovalInfo, None)
    ApprovedActions = property(get_ApprovedActions, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    CurrentAction = property(get_CurrentAction, None)
    Description = property(get_Description, None)
    DownloadSizeInBytes = property(get_DownloadSizeInBytes, None)
    ExecutionInfo = property(get_ExecutionInfo, None)
    InstallSizeInBytes = property(get_InstallSizeInBytes, None)
    InstallationType = property(get_InstallationType, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    OptionalInfo = property(get_OptionalInfo, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    ProductCode = property(get_ProductCode, None)
    ProviderId = property(get_ProviderId, None)
    RestartReason = property(get_RestartReason, None)
    SourceVersion = property(get_SourceVersion, None)
    TargetVersion = property(get_TargetVersion, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class WindowsSoftwareUpdateActionInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateActionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionInfoFactory, fileName: hstr, fileArguments: hstr, actionType: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_FileName(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_FileArguments(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_ActionType(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionType: ...
    ActionType = property(get_ActionType, None)
    FileArguments = property(get_FileArguments, None)
    FileName = property(get_FileName, None)
class WindowsSoftwareUpdateActionProgress(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionProgress
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateActionProgress'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionProgress) -> hstr: ...
    @winrt_mixinmethod
    def get_CurrentProgress(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionProgress) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalProgress(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionProgress) -> UInt64: ...
    Action = property(get_Action, None)
    CurrentProgress = property(get_CurrentProgress, None)
    TotalProgress = property(get_TotalProgress, None)
class WindowsSoftwareUpdateActionResult(Enum, Int32):
    Succeeded = 0
    Continue = 1
    Failed = 2
    Canceled = 3
    Removed = 4
class WindowsSoftwareUpdateActionResultInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateActionResultInfo'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResultCode(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateActionResultInfo) -> hstr: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
    Timestamp = property(get_Timestamp, None)
class WindowsSoftwareUpdateActionType(Enum, Int32):
    Download = 0
    Install = 1
    Deploy = 2
    Reboot = 3
    AppRestart = 4
class WindowsSoftwareUpdateAppPackageInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfoFactory, packageFamilyName: hstr, packageArchitecture: win32more.Windows.Management.Update.WindowsSoftwareUpdateArchitecture, installUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateAppPackageInfo: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_PackageArchitecture(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateArchitecture: ...
    @winrt_mixinmethod
    def get_InstallUri(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateAppPackageInfo) -> win32more.Windows.Foundation.Uri: ...
    InstallUri = property(get_InstallUri, None)
    PackageArchitecture = property(get_PackageArchitecture, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class WindowsSoftwareUpdateApprovalInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfoFactory, userInitiated: Boolean, appClosure: Boolean, meteredNetwork: Boolean, seeker: Boolean) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateApprovalInfo: ...
    @winrt_mixinmethod
    def get_UserInitiated(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppClosure(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_MeteredNetwork(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_Seeker(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateApprovalInfo) -> Boolean: ...
    AppClosure = property(get_AppClosure, None)
    MeteredNetwork = property(get_MeteredNetwork, None)
    Seeker = property(get_Seeker, None)
    UserInitiated = property(get_UserInitiated, None)
class WindowsSoftwareUpdateArchitecture(Enum, Int32):
    Neutral = 0
    X86 = 1
    X64 = 2
    Arm = 3
    Arm64 = 4
class WindowsSoftwareUpdateExecutionInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo.CreateInstance2(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfoFactory, deployInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, actions: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfoFactory, downloadInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, installInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, actions: win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateExecutionInfo: ...
    @winrt_mixinmethod
    def get_DownloadInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_InstallInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_DeployInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_OptionalActionInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateExecutionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo: ...
    DeployInfo = property(get_DeployInfo, None)
    DownloadInfo = property(get_DownloadInfo, None)
    InstallInfo = property(get_InstallInfo, None)
    OptionalActionInfo = property(get_OptionalActionInfo, None)
class WindowsSoftwareUpdateInstallationType(Enum, Int32):
    WindowsUpdate = 0
    AppPackage = 1
    Executable = 2
    Powershell = 3
class WindowsSoftwareUpdateLocalizationInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfoFactory, languageId: UInt32, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo: ...
    @winrt_mixinmethod
    def get_LanguageId(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateLocalizationInfo) -> win32more.Windows.Foundation.Uri: ...
    Description = property(get_Description, None)
    LanguageId = property(get_LanguageId, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Title = property(get_Title, None)
class WindowsSoftwareUpdateOptionalActionInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfoFactory, closeAndDeployInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, closeAndInstallInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo, closeAndRestartInfo: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalActionInfo: ...
    @winrt_mixinmethod
    def get_CloseAndDeployInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_CloseAndInstallInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    @winrt_mixinmethod
    def get_CloseAndRestartInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalActionInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionInfo: ...
    CloseAndDeployInfo = property(get_CloseAndDeployInfo, None)
    CloseAndInstallInfo = property(get_CloseAndInstallInfo, None)
    CloseAndRestartInfo = property(get_CloseAndRestartInfo, None)
class WindowsSoftwareUpdateOptionalInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfoFactory, complianceDeadlineInDays: win32more.Windows.Foundation.IReference[Int32], complianceGracePeriodInDays: win32more.Windows.Foundation.IReference[Int32]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfoFactory, localizationInfo: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo], complianceDeadlineInDays: win32more.Windows.Foundation.IReference[Int32], complianceGracePeriodInDays: win32more.Windows.Foundation.IReference[Int32]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateOptionalInfo: ...
    @winrt_mixinmethod
    def get_LocalizationInfo(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateLocalizationInfo]: ...
    @winrt_mixinmethod
    def get_ComplianceDeadlineInDays(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def get_ComplianceGracePeriodInDays(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateOptionalInfo) -> win32more.Windows.Foundation.IReference[Int32]: ...
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, None)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, None)
    LocalizationInfo = property(get_LocalizationInfo, None)
class WindowsSoftwareUpdateProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateProvider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateProvider.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderFactory, folderPath: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProvider: ...
    @winrt_mixinmethod
    def Register(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def Validate(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_FolderPath(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_CatalogFile(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_ScanFileName(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_ScanFileArguments(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderType: ...
    @winrt_mixinmethod
    def get_PayloadFiles(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderPayloadFileInfo]: ...
    @winrt_mixinmethod
    def get_TrustState(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderTrustState: ...
    @winrt_mixinmethod
    def get_RegistrationType(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderRegistrationType: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider) -> win32more.Windows.Foundation.Collections.PropertySet: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProvider, name: hstr) -> IInspectable: ...
    CatalogFile = property(get_CatalogFile, None)
    FolderPath = property(get_FolderPath, None)
    Id = property(get_Id, None)
    PayloadFiles = property(get_PayloadFiles, None)
    Properties = property(get_Properties, None)
    RegistrationType = property(get_RegistrationType, None)
    ScanFileArguments = property(get_ScanFileArguments, None)
    ScanFileName = property(get_ScanFileName, None)
    TrustState = property(get_TrustState, None)
    Type = property(get_Type, None)
    Version = property(get_Version, None)
class WindowsSoftwareUpdateProviderActionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResultFactory, actionResult: win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResult, restartReason: win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateActionResult: ...
    @winrt_mixinmethod
    def get_RestartReason(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateRestartReason: ...
    @winrt_mixinmethod
    def get_ResultCode(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderActionResult) -> UInt64: ...
    ExtendedError = property(get_ExtendedError, None)
    RestartReason = property(get_RestartReason, None)
    Result = property(get_Result, None)
    ResultCode = property(get_ResultCode, None)
class WindowsSoftwareUpdateProviderPayloadFileInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateProviderPayloadFileInfo'
    @winrt_mixinmethod
    def get_Filename(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_FileHash(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_CatalogFile(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_TrustState(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderPayloadFileInfo) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderTrustState: ...
    CatalogFile = property(get_CatalogFile, None)
    FileHash = property(get_FileHash, None)
    Filename = property(get_Filename, None)
    TrustState = property(get_TrustState, None)
class WindowsSoftwareUpdateProviderRegistrationType(Enum, Int32):
    None_ = 0
    System = 1
    Windows = 2
    Pending = 3
    Registered = 4
    Unregistered = 5
class WindowsSoftwareUpdateProviderStatus(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateProviderStatus'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderStatus.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatusFactory, providerId: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderStatus: ...
    @winrt_mixinmethod
    def add_CancelRequested(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderStatus, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CancelRequested(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetScanResult(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def SetActionProgress(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus, current: UInt64, total: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def SetActionResult(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateProviderStatus, actionResult: win32more.Windows.Management.Update.WindowsSoftwareUpdateProviderActionResult) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    CancelRequested = event(add_CancelRequested, remove_CancelRequested)
class WindowsSoftwareUpdateProviderTrustState(Enum, Int32):
    SignedTrusted = 0
    SignedUntrusted = 1
    Unsigned = 2
class WindowsSoftwareUpdateProviderType(Enum, Int32):
    WindowsUpdate = 0
    Executable = 1
    Powershell = 2
class WindowsSoftwareUpdateRestartReason(Enum, Int32):
    None_ = 0
    System = 1
    AppClose = 2
    AppRestart = 3
class WindowsSoftwareUpdateResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResult
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateResult.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateResult.CreateInstance2(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateResult.CreateInstance3(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResultFactory, succeeded: Boolean, resultCode: UInt32) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResultFactory, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_factorymethod
    def CreateInstance3(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResultFactory, succeeded: Boolean, cancelRequested: Boolean, resultCode: UInt32, extendedError: UInt64) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateResult: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_CancelRequested(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResultCode(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateResult) -> UInt64: ...
    CancelRequested = property(get_CancelRequested, None)
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
class WindowsSoftwareUpdateScanResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResult
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateScanResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult.CreateInstance(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult.CreateInstance2(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResultFactory, succeeded: Boolean, resultCode: UInt32, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
    @winrt_factorymethod
    def CreateInstance2(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResultFactory, succeeded: Boolean, resultCode: UInt32, extendedError: UInt64, updates: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.Update.WindowsSoftwareUpdate]) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResultCode(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_Updates(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateScanResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdate]: ...
    ExtendedError = property(get_ExtendedError, None)
    ResultCode = property(get_ResultCode, None)
    Succeeded = property(get_Succeeded, None)
    Updates = property(get_Updates, None)
class WindowsSoftwareUpdateVersion(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersion
    _classid_ = 'Windows.Management.Update.WindowsSoftwareUpdateVersion'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersionFactory, major: UInt32, minor: UInt32, revisionMajor: UInt32, revisionMinor: UInt32) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateVersion: ...
    @winrt_mixinmethod
    def get_Major(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersion) -> UInt32: ...
    @winrt_mixinmethod
    def get_Minor(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersion) -> UInt32: ...
    @winrt_mixinmethod
    def get_RevisionMajor(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersion) -> UInt32: ...
    @winrt_mixinmethod
    def get_RevisionMinor(self: win32more.Windows.Management.Update.IWindowsSoftwareUpdateVersion) -> UInt32: ...
    Major = property(get_Major, None)
    Minor = property(get_Minor, None)
    RevisionMajor = property(get_RevisionMajor, None)
    RevisionMinor = property(get_RevisionMinor, None)
class WindowsUpdate(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdate
    _classid_ = 'Windows.Management.Update.WindowsUpdate'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_IsFeatureUpdate(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMinorImpact(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSecurity(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCritical(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsForOS(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDriver(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMandatory(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUrgent(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSeeker(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsEulaAccepted(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_EulaText(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_AttentionRequiredInfo(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_mixinmethod
    def get_ActionResult(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_mixinmethod
    def get_CurrentAction(self: win32more.Windows.Management.Update.IWindowsUpdate) -> hstr: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: win32more.Windows.Management.Update.IWindowsUpdate, propertyName: hstr) -> IInspectable: ...
    @winrt_mixinmethod
    def AcceptEula(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Void: ...
    ActionProgress = property(get_ActionProgress, None)
    ActionResult = property(get_ActionResult, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    CurrentAction = property(get_CurrentAction, None)
    Deadline = property(get_Deadline, None)
    Description = property(get_Description, None)
    EulaText = property(get_EulaText, None)
    IsCritical = property(get_IsCritical, None)
    IsDriver = property(get_IsDriver, None)
    IsEulaAccepted = property(get_IsEulaAccepted, None)
    IsFeatureUpdate = property(get_IsFeatureUpdate, None)
    IsForOS = property(get_IsForOS, None)
    IsMandatory = property(get_IsMandatory, None)
    IsMinorImpact = property(get_IsMinorImpact, None)
    IsSecurity = property(get_IsSecurity, None)
    IsSeeker = property(get_IsSeeker, None)
    IsUrgent = property(get_IsUrgent, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    ProviderId = property(get_ProviderId, None)
    SupportUrl = property(get_SupportUrl, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class WindowsUpdateActionCompletedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionCompletedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> hstr: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    Succeeded = property(get_Succeeded, None)
    Update = property(get_Update, None)
class WindowsUpdateActionProgress(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionProgress
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionProgress'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionProgress) -> hstr: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.Management.Update.IWindowsUpdateActionProgress) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class WindowsUpdateActionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionResult
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionResult'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> hstr: ...
    Action = property(get_Action, None)
    ExtendedError = property(get_ExtendedError, None)
    Succeeded = property(get_Succeeded, None)
    Timestamp = property(get_Timestamp, None)
class WindowsUpdateAdministrator(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAdministrator
    _classid_ = 'Windows.Management.Update.WindowsUpdateAdministrator'
    @winrt_mixinmethod
    def StartAdministratorScan(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdateAction(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: hstr, action: hstr) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateActionApproval(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: hstr, action: hstr) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdate(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: hstr, approvalData: win32more.Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateApproval(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: hstr) -> Void: ...
    @winrt_mixinmethod
    def GetUpdates(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    @winrt_classmethod
    def GetRegisteredAdministrator(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: hstr) -> win32more.Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_classmethod
    def RegisterForAdministration(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: hstr, options: win32more.Windows.Management.Update.WindowsUpdateAdministratorOptions) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def UnregisterForAdministration(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: hstr) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def GetRegisteredAdministratorName(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics) -> hstr: ...
    @winrt_classmethod
    def RequestRestart(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, restartOptions: win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> hstr: ...
    @winrt_classmethod
    def CancelRestartRequest(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, requestRestartToken: hstr) -> Void: ...
class WindowsUpdateAdministratorOptions(Enum, UInt32):
    None_ = 0
    RequireAdministratorApprovalForScans = 1
    RequireAdministratorApprovalForUpdates = 2
    RequireAdministratorApprovalForActions = 4
class WindowsUpdateAdministratorStatus(Enum, Int32):
    Succeeded = 0
    NoAdministratorRegistered = 1
    OtherAdministratorIsRegistered = 2
class WindowsUpdateApprovalData(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateApprovalData
    _classid_ = 'Windows.Management.Update.WindowsUpdateApprovalData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateApprovalData.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.Update.WindowsUpdateApprovalData: ...
    @winrt_mixinmethod
    def get_Seeker(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_Seeker(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowDownloadOnMetered(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_AllowDownloadOnMetered(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceDeadlineInDays(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_ComplianceDeadlineInDays(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceGracePeriodInDays(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_ComplianceGracePeriodInDays(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateApprovalData, value: win32more.Windows.Foundation.IReference[Boolean]) -> Void: ...
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
    Seeker = property(get_Seeker, put_Seeker)
class WindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredInfo'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Reason = property(get_Reason, None)
    Timestamp = property(get_Timestamp, None)
class WindowsUpdateAttentionRequiredReason(Enum, Int32):
    None_ = 0
    SeekerUpdate = 1
    ReadyToReboot = 2
    NeedNonMeteredNetwork = 3
    NeedUserAgreementForMeteredNetwork = 4
    NeedNetwork = 5
    NeedMoreSpace = 6
    BatterySaverEnabled = 7
    NeedUserInteraction = 8
    NeedUserAgreementForPolicy = 9
    CompatibilityError = 10
    NeedUserInteractionForEula = 11
    NeedUserInteractionForCta = 12
    Regulated = 13
    ExternalReboot = 14
    OtherUpdate = 15
    BlockedByProvider = 16
    BlockedByPostRebootFailure = 17
    UserEngaged = 18
    BlockedByBattery = 19
    Exclusivity = 20
    BlockedBySerialization = 21
    ConflictClass = 22
    BlockedByAdminApproval = 23
    BlockedByTooManyAttempts = 24
    BlockedByFailure = 25
    Demotion = 26
    BlockedByActiveHours = 27
    ScheduledForMaintenance = 28
    PolicyScheduledInstallTime = 29
    BlockedByOobe = 30
    DeferredDuringOobe = 31
    DeferredForSustainableTime = 32
    BlockedByAppClose = 33
    BlockedByAppRestart = 34
    OtherUpdateReverting = 35
class WindowsUpdateAttentionRequiredReasonChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Reason = property(get_Reason, None)
    Update = property(get_Update, None)
WindowsUpdateContract: UInt32 = 131073
class WindowsUpdateGetAdministratorResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult
    _classid_ = 'Windows.Management.Update.WindowsUpdateGetAdministratorResult'
    @winrt_mixinmethod
    def get_Administrator(self: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> win32more.Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class WindowsUpdateItem(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateItem
    _classid_ = 'Windows.Management.Update.WindowsUpdateItem'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> hstr: ...
    Category = property(get_Category, None)
    Description = property(get_Description, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Operation = property(get_Operation, None)
    ProviderId = property(get_ProviderId, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    UpdateId = property(get_UpdateId, None)
class WindowsUpdateManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateManager
    _classid_ = 'Windows.Management.Update.WindowsUpdateManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateManager.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateManager.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateManagerFactory, clientId: hstr) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateManagerFactory2, clientId: hstr, providerIdFilter: PassArray[hstr]) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
    @winrt_mixinmethod
    def add_ScanningStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScanningStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WorkingStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WorkingStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProgressChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateProgressChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProgressChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AttentionRequiredReasonChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AttentionRequiredReasonChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActionCompleted(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateActionCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActionCompleted(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScanCompleted(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Management.Update.WindowsUpdateScanCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScanCompleted(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsScanning(self: win32more.Windows.Management.Update.IWindowsUpdateManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsWorking(self: win32more.Windows.Management.Update.IWindowsUpdateManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_LastSuccessfulScanTimestamp(self: win32more.Windows.Management.Update.IWindowsUpdateManager) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def GetApplicableUpdates(self: win32more.Windows.Management.Update.IWindowsUpdateManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    @winrt_mixinmethod
    def GetMostRecentCompletedUpdates(self: win32more.Windows.Management.Update.IWindowsUpdateManager, count: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdateItem]: ...
    @winrt_mixinmethod
    def GetMostRecentCompletedUpdatesAsync(self: win32more.Windows.Management.Update.IWindowsUpdateManager, count: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdateItem]]: ...
    @winrt_mixinmethod
    def StartScan(self: win32more.Windows.Management.Update.IWindowsUpdateManager, userInitiated: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetProvider(self: win32more.Windows.Management.Update.IWindowsUpdateManager2, id: hstr) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateProvider: ...
    @winrt_mixinmethod
    def get_ProviderIds(self: win32more.Windows.Management.Update.IWindowsUpdateManager2) -> ReceiveArray[hstr]: ...
    @winrt_mixinmethod
    def GetApplicableSoftwareUpdates(self: win32more.Windows.Management.Update.IWindowsUpdateManager2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsSoftwareUpdate]: ...
    @winrt_mixinmethod
    def PerformScan(self: win32more.Windows.Management.Update.IWindowsUpdateManager2, options: win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions) -> win32more.Windows.Management.Update.WindowsSoftwareUpdateScanResult: ...
    IsScanning = property(get_IsScanning, None)
    IsWorking = property(get_IsWorking, None)
    LastSuccessfulScanTimestamp = property(get_LastSuccessfulScanTimestamp, None)
    ProviderIds = property(get_ProviderIds, None)
    ActionCompleted = event(add_ActionCompleted, remove_ActionCompleted)
    AttentionRequiredReasonChanged = event(add_AttentionRequiredReasonChanged, remove_AttentionRequiredReasonChanged)
    ProgressChanged = event(add_ProgressChanged, remove_ProgressChanged)
    ScanCompleted = event(add_ScanCompleted, remove_ScanCompleted)
    ScanningStateChanged = event(add_ScanningStateChanged, remove_ScanningStateChanged)
    WorkingStateChanged = event(add_WorkingStateChanged, remove_WorkingStateChanged)
class WindowsUpdateManagerScanOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions
    _classid_ = 'Windows.Management.Update.WindowsUpdateManagerScanOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptionsFactory, isUserInitiated: Boolean) -> win32more.Windows.Management.Update.WindowsUpdateManagerScanOptions: ...
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsUserInitiated(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowBypassThrottling(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowBypassThrottling(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PerformUpdateActions(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_PerformUpdateActions(self: win32more.Windows.Management.Update.IWindowsUpdateManagerScanOptions, value: Boolean) -> Void: ...
    AllowBypassThrottling = property(get_AllowBypassThrottling, put_AllowBypassThrottling)
    IsUserInitiated = property(get_IsUserInitiated, put_IsUserInitiated)
    PerformUpdateActions = property(get_PerformUpdateActions, put_PerformUpdateActions)
class WindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateProgressChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    ActionProgress = property(get_ActionProgress, None)
    Update = property(get_Update, None)
class WindowsUpdateRestartRequestOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions
    _classid_ = 'Windows.Management.Update.WindowsUpdateRestartRequestOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions.CreateInstance(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptionsFactory, title: hstr, description: hstr, moreInfoUrl: win32more.Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceDeadlineInDays(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_ComplianceDeadlineInDays(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceGracePeriodInDays(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_ComplianceGracePeriodInDays(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_OrganizationName(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_OrganizationName(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Boolean) -> Void: ...
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    Description = property(get_Description, put_Description)
    MoreInfoUrl = property(get_MoreInfoUrl, put_MoreInfoUrl)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
    OrganizationName = property(get_OrganizationName, put_OrganizationName)
    Title = property(get_Title, put_Title)
class WindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateScanCompletedEventArgs'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> hstr: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Updates(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    ExtendedError = property(get_ExtendedError, None)
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    Updates = property(get_Updates, None)


make_ready(__name__)
