from __future__ import annotations
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management.Update
class IPreviewBuildsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IPreviewBuildsManagerStatics'
    _iid_ = Guid('{3e422887-b112-5a70-7da1-97d78d32aa29}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
class IPreviewBuildsState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IPreviewBuildsState'
    _iid_ = Guid('{a2f2903e-b223-5f63-7546-3e8eac070a2e}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class IWindowsUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdate'
    _iid_ = Guid('{c3c88dd7-0ef3-52b2-a9ad-66bfc6bd9582}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UpdateId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
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
    def get_EulaText(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_Deadline(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredInfo(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_commethod(25)
    def get_ActionResult(self) -> win32more.Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_commethod(26)
    def get_CurrentAction(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_ActionProgress(self) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_commethod(28)
    def GetPropertyValue(self, propertyName: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(29)
    def AcceptEula(self) -> Void: ...
    ProviderId = property(get_ProviderId, None)
    UpdateId = property(get_UpdateId, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    IsFeatureUpdate = property(get_IsFeatureUpdate, None)
    IsMinorImpact = property(get_IsMinorImpact, None)
    IsSecurity = property(get_IsSecurity, None)
    IsCritical = property(get_IsCritical, None)
    IsForOS = property(get_IsForOS, None)
    IsDriver = property(get_IsDriver, None)
    IsMandatory = property(get_IsMandatory, None)
    IsUrgent = property(get_IsUrgent, None)
    IsSeeker = property(get_IsSeeker, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    SupportUrl = property(get_SupportUrl, None)
    IsEulaAccepted = property(get_IsEulaAccepted, None)
    EulaText = property(get_EulaText, None)
    Deadline = property(get_Deadline, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    ActionResult = property(get_ActionResult, None)
    CurrentAction = property(get_CurrentAction, None)
    ActionProgress = property(get_ActionProgress, None)
class IWindowsUpdateActionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs'
    _iid_ = Guid('{2c44b950-a655-5321-aec1-aee762922131}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Action(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Update = property(get_Update, None)
    Action = property(get_Action, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
class IWindowsUpdateActionProgress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionProgress'
    _iid_ = Guid('{83b22d8a-4bb0-549f-ba39-59724882d137}')
    @winrt_commethod(6)
    def get_Action(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Progress(self) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class IWindowsUpdateActionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateActionResult'
    _iid_ = Guid('{e6692c62-f697-51b7-ab7f-e73e5e688f12}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Action(self) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Action = property(get_Action, None)
class IWindowsUpdateAdministrator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAdministrator'
    _iid_ = Guid('{7a60181c-ba1e-5cf9-aa65-304120b73d72}')
    @winrt_commethod(6)
    def StartAdministratorScan(self) -> Void: ...
    @winrt_commethod(7)
    def ApproveWindowsUpdateAction(self, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def RevokeWindowsUpdateActionApproval(self, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def ApproveWindowsUpdate(self, updateId: WinRT_String, approvalData: win32more.Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_commethod(10)
    def RevokeWindowsUpdateApproval(self, updateId: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def GetUpdates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
class IWindowsUpdateAdministratorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAdministratorStatics'
    _iid_ = Guid('{013e6d36-ef69-53bc-8db8-c403bca550ed}')
    @winrt_commethod(6)
    def GetRegisteredAdministrator(self, organizationName: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_commethod(7)
    def RegisterForAdministration(self, organizationName: WinRT_String, options: win32more.Windows.Management.Update.WindowsUpdateAdministratorOptions) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(8)
    def UnregisterForAdministration(self, organizationName: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(9)
    def GetRegisteredAdministratorName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def RequestRestart(self, restartOptions: win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_commethod(11)
    def CancelRestartRequest(self, requestRestartToken: WinRT_String) -> Void: ...
class IWindowsUpdateApprovalData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    Seeker = property(get_Seeker, put_Seeker)
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class IWindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo'
    _iid_ = Guid('{44df2579-74d3-5ffa-b6ce-09e187e1e0ed}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Reason = property(get_Reason, None)
    Timestamp = property(get_Timestamp, None)
class IWindowsUpdateAttentionRequiredReasonChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs'
    _iid_ = Guid('{0627abca-dbb8-524a-b1d2-d9df004eeb31}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Reason(self) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Update = property(get_Update, None)
    Reason = property(get_Reason, None)
class IWindowsUpdateGetAdministratorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateGetAdministratorResult'
    _iid_ = Guid('{bb39ffc4-2c42-5b1c-8995-343341c92c50}')
    @winrt_commethod(6)
    def get_Administrator(self) -> win32more.Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class IWindowsUpdateItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateItem'
    _iid_ = Guid('{b222e44a-49b6-59bf-a033-ef617cd73a98}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UpdateId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_MoreInfoUrl(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def get_Category(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Operation(self) -> WinRT_String: ...
    ProviderId = property(get_ProviderId, None)
    UpdateId = property(get_UpdateId, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Category = property(get_Category, None)
    Operation = property(get_Operation, None)
class IWindowsUpdateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManager'
    _iid_ = Guid('{5dd966c0-a71a-5602-bbd0-09a70e4573fa}')
    @winrt_commethod(6)
    def add_ScanningStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScanningStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_WorkingStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
class IWindowsUpdateManagerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateManagerFactory'
    _iid_ = Guid('{1b394df8-decb-5f44-b47c-6ccf3bcfdb37}')
    @winrt_commethod(6)
    def CreateInstance(self, clientId: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
class IWindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs'
    _iid_ = Guid('{bbfbdeeb-94c8-5aa7-b0fb-66c67c233b0a}')
    @winrt_commethod(6)
    def get_Update(self) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_ActionProgress(self) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    Update = property(get_Update, None)
    ActionProgress = property(get_ActionProgress, None)
class IWindowsUpdateRestartRequestOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateRestartRequestOptions'
    _iid_ = Guid('{38cfb7d3-4188-5222-905c-6c4443c951ee}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
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
    def get_OrganizationName(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_OrganizationName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_OptOutOfAutoReboot(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_OptOutOfAutoReboot(self, value: Boolean) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    MoreInfoUrl = property(get_MoreInfoUrl, put_MoreInfoUrl)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OrganizationName = property(get_OrganizationName, put_OrganizationName)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class IWindowsUpdateRestartRequestOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateRestartRequestOptionsFactory'
    _iid_ = Guid('{75f41d04-0e17-50d0-8c15-6b9d0539b3a9}')
    @winrt_commethod(6)
    def CreateInstance(self, title: WinRT_String, description: WinRT_String, moreInfoUrl: win32more.Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
class IWindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs'
    _iid_ = Guid('{95b6953e-ba5c-5fe8-b115-12de184a6bb0}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Updates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Updates = property(get_Updates, None)
class PreviewBuildsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IPreviewBuildsState
    _classid_ = 'Windows.Management.Update.PreviewBuildsState'
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Management.Update.IPreviewBuildsState) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class WindowsUpdate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdate
    _classid_ = 'Windows.Management.Update.WindowsUpdate'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
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
    def get_EulaText(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_AttentionRequiredInfo(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_mixinmethod
    def get_ActionResult(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_mixinmethod
    def get_CurrentAction(self: win32more.Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: win32more.Windows.Management.Update.IWindowsUpdate) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: win32more.Windows.Management.Update.IWindowsUpdate, propertyName: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def AcceptEula(self: win32more.Windows.Management.Update.IWindowsUpdate) -> Void: ...
    ProviderId = property(get_ProviderId, None)
    UpdateId = property(get_UpdateId, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    IsFeatureUpdate = property(get_IsFeatureUpdate, None)
    IsMinorImpact = property(get_IsMinorImpact, None)
    IsSecurity = property(get_IsSecurity, None)
    IsCritical = property(get_IsCritical, None)
    IsForOS = property(get_IsForOS, None)
    IsDriver = property(get_IsDriver, None)
    IsMandatory = property(get_IsMandatory, None)
    IsUrgent = property(get_IsUrgent, None)
    IsSeeker = property(get_IsSeeker, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    SupportUrl = property(get_SupportUrl, None)
    IsEulaAccepted = property(get_IsEulaAccepted, None)
    EulaText = property(get_EulaText, None)
    Deadline = property(get_Deadline, None)
    AttentionRequiredInfo = property(get_AttentionRequiredInfo, None)
    ActionResult = property(get_ActionResult, None)
    CurrentAction = property(get_CurrentAction, None)
    ActionProgress = property(get_ActionProgress, None)
class WindowsUpdateActionCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionCompletedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    Update = property(get_Update, None)
    Action = property(get_Action, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
class WindowsUpdateActionProgress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionProgress
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionProgress'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionProgress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.Management.Update.IWindowsUpdateActionProgress) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class WindowsUpdateActionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateActionResult
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionResult'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Management.Update.IWindowsUpdateActionResult) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Action = property(get_Action, None)
class WindowsUpdateAdministrator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAdministrator
    _classid_ = 'Windows.Management.Update.WindowsUpdateAdministrator'
    @winrt_mixinmethod
    def StartAdministratorScan(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdateAction(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateActionApproval(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdate(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, approvalData: win32more.Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateApproval(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetUpdates(self: win32more.Windows.Management.Update.IWindowsUpdateAdministrator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    @winrt_classmethod
    def GetRegisteredAdministrator(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_classmethod
    def RegisterForAdministration(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String, options: win32more.Windows.Management.Update.WindowsUpdateAdministratorOptions) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def UnregisterForAdministration(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def GetRegisteredAdministratorName(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def RequestRestart(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, restartOptions: win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_classmethod
    def CancelRestartRequest(cls: win32more.Windows.Management.Update.IWindowsUpdateAdministratorStatics, requestRestartToken: WinRT_String) -> Void: ...
WindowsUpdateAdministratorOptions = UInt32
WindowsUpdateAdministratorOptions_None: WindowsUpdateAdministratorOptions = 0
WindowsUpdateAdministratorOptions_RequireAdministratorApprovalForScans: WindowsUpdateAdministratorOptions = 1
WindowsUpdateAdministratorOptions_RequireAdministratorApprovalForUpdates: WindowsUpdateAdministratorOptions = 2
WindowsUpdateAdministratorOptions_RequireAdministratorApprovalForActions: WindowsUpdateAdministratorOptions = 4
WindowsUpdateAdministratorStatus = Int32
WindowsUpdateAdministratorStatus_Succeeded: WindowsUpdateAdministratorStatus = 0
WindowsUpdateAdministratorStatus_NoAdministratorRegistered: WindowsUpdateAdministratorStatus = 1
WindowsUpdateAdministratorStatus_OtherAdministratorIsRegistered: WindowsUpdateAdministratorStatus = 2
class WindowsUpdateApprovalData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateApprovalData
    _classid_ = 'Windows.Management.Update.WindowsUpdateApprovalData'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Management.Update.WindowsUpdateApprovalData.CreateInstance(*args)
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
    Seeker = property(get_Seeker, put_Seeker)
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class WindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredInfo'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Reason = property(get_Reason, None)
    Timestamp = property(get_Timestamp, None)
WindowsUpdateAttentionRequiredReason = Int32
WindowsUpdateAttentionRequiredReason_None: WindowsUpdateAttentionRequiredReason = 0
WindowsUpdateAttentionRequiredReason_SeekerUpdate: WindowsUpdateAttentionRequiredReason = 1
WindowsUpdateAttentionRequiredReason_ReadyToReboot: WindowsUpdateAttentionRequiredReason = 2
WindowsUpdateAttentionRequiredReason_NeedNonMeteredNetwork: WindowsUpdateAttentionRequiredReason = 3
WindowsUpdateAttentionRequiredReason_NeedUserAgreementForMeteredNetwork: WindowsUpdateAttentionRequiredReason = 4
WindowsUpdateAttentionRequiredReason_NeedNetwork: WindowsUpdateAttentionRequiredReason = 5
WindowsUpdateAttentionRequiredReason_NeedMoreSpace: WindowsUpdateAttentionRequiredReason = 6
WindowsUpdateAttentionRequiredReason_BatterySaverEnabled: WindowsUpdateAttentionRequiredReason = 7
WindowsUpdateAttentionRequiredReason_NeedUserInteraction: WindowsUpdateAttentionRequiredReason = 8
WindowsUpdateAttentionRequiredReason_NeedUserAgreementForPolicy: WindowsUpdateAttentionRequiredReason = 9
WindowsUpdateAttentionRequiredReason_CompatibilityError: WindowsUpdateAttentionRequiredReason = 10
WindowsUpdateAttentionRequiredReason_NeedUserInteractionForEula: WindowsUpdateAttentionRequiredReason = 11
WindowsUpdateAttentionRequiredReason_NeedUserInteractionForCta: WindowsUpdateAttentionRequiredReason = 12
WindowsUpdateAttentionRequiredReason_Regulated: WindowsUpdateAttentionRequiredReason = 13
WindowsUpdateAttentionRequiredReason_ExternalReboot: WindowsUpdateAttentionRequiredReason = 14
WindowsUpdateAttentionRequiredReason_OtherUpdate: WindowsUpdateAttentionRequiredReason = 15
WindowsUpdateAttentionRequiredReason_BlockedByProvider: WindowsUpdateAttentionRequiredReason = 16
WindowsUpdateAttentionRequiredReason_BlockedByPostRebootFailure: WindowsUpdateAttentionRequiredReason = 17
WindowsUpdateAttentionRequiredReason_UserEngaged: WindowsUpdateAttentionRequiredReason = 18
WindowsUpdateAttentionRequiredReason_BlockedByBattery: WindowsUpdateAttentionRequiredReason = 19
WindowsUpdateAttentionRequiredReason_Exclusivity: WindowsUpdateAttentionRequiredReason = 20
WindowsUpdateAttentionRequiredReason_BlockedBySerialization: WindowsUpdateAttentionRequiredReason = 21
WindowsUpdateAttentionRequiredReason_ConflictClass: WindowsUpdateAttentionRequiredReason = 22
WindowsUpdateAttentionRequiredReason_BlockedByAdminApproval: WindowsUpdateAttentionRequiredReason = 23
WindowsUpdateAttentionRequiredReason_BlockedByTooManyAttempts: WindowsUpdateAttentionRequiredReason = 24
WindowsUpdateAttentionRequiredReason_BlockedByFailure: WindowsUpdateAttentionRequiredReason = 25
WindowsUpdateAttentionRequiredReason_Demotion: WindowsUpdateAttentionRequiredReason = 26
WindowsUpdateAttentionRequiredReason_BlockedByActiveHours: WindowsUpdateAttentionRequiredReason = 27
WindowsUpdateAttentionRequiredReason_ScheduledForMaintenance: WindowsUpdateAttentionRequiredReason = 28
WindowsUpdateAttentionRequiredReason_PolicyScheduledInstallTime: WindowsUpdateAttentionRequiredReason = 29
WindowsUpdateAttentionRequiredReason_BlockedByOobe: WindowsUpdateAttentionRequiredReason = 30
WindowsUpdateAttentionRequiredReason_DeferredDuringOobe: WindowsUpdateAttentionRequiredReason = 31
WindowsUpdateAttentionRequiredReason_DeferredForSustainableTime: WindowsUpdateAttentionRequiredReason = 32
class WindowsUpdateAttentionRequiredReasonChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Update = property(get_Update, None)
    Reason = property(get_Reason, None)
WindowsUpdateContract: UInt32 = 65536
class WindowsUpdateGetAdministratorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult
    _classid_ = 'Windows.Management.Update.WindowsUpdateGetAdministratorResult'
    @winrt_mixinmethod
    def get_Administrator(self: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> win32more.Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> win32more.Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class WindowsUpdateItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateItem
    _classid_ = 'Windows.Management.Update.WindowsUpdateItem'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UpdateId(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    ProviderId = property(get_ProviderId, None)
    UpdateId = property(get_UpdateId, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Category = property(get_Category, None)
    Operation = property(get_Operation, None)
class WindowsUpdateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateManager
    _classid_ = 'Windows.Management.Update.WindowsUpdateManager'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Management.Update.WindowsUpdateManager.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateManagerFactory, clientId: WinRT_String) -> win32more.Windows.Management.Update.WindowsUpdateManager: ...
    @winrt_mixinmethod
    def add_ScanningStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScanningStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WorkingStateChanged(self: win32more.Windows.Management.Update.IWindowsUpdateManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Update.WindowsUpdateManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    IsScanning = property(get_IsScanning, None)
    IsWorking = property(get_IsWorking, None)
    LastSuccessfulScanTimestamp = property(get_LastSuccessfulScanTimestamp, None)
class WindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateProgressChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: win32more.Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> win32more.Windows.Management.Update.WindowsUpdateActionProgress: ...
    Update = property(get_Update, None)
    ActionProgress = property(get_ActionProgress, None)
class WindowsUpdateRestartRequestOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions
    _classid_ = 'Windows.Management.Update.WindowsUpdateRestartRequestOptions'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions.CreateInstance(*args)
        elif len(args) == 5:
            return win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptionsFactory, title: WinRT_String, description: WinRT_String, moreInfoUrl: win32more.Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> win32more.Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
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
    def get_OrganizationName(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OrganizationName(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_OptOutOfAutoReboot(self: win32more.Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Boolean) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    MoreInfoUrl = property(get_MoreInfoUrl, put_MoreInfoUrl)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OrganizationName = property(get_OrganizationName, put_OrganizationName)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class WindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs
    _classid_ = 'Windows.Management.Update.WindowsUpdateScanCompletedEventArgs'
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Updates(self: win32more.Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.Update.WindowsUpdate]: ...
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Updates = property(get_Updates, None)


make_ready(__name__)
