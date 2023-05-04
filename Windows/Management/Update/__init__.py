from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Management.Update
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPreviewBuildsManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fa07dd61-7e4f-59f7-7c9f-def9051c5f62}')
    @winrt_commethod(6)
    def get_ArePreviewBuildsAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ArePreviewBuildsAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentState(self) -> Windows.Management.Update.PreviewBuildsState: ...
    @winrt_commethod(9)
    def SyncAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class IPreviewBuildsManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3e422887-b112-5a70-7da1-97d78d32aa29}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
class IPreviewBuildsState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a2f2903e-b223-5f63-7546-3e8eac070a2e}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class IWindowsUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_MoreInfoUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(20)
    def get_SupportUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(21)
    def get_IsEulaAccepted(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_EulaText(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_Deadline(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredInfo(self) -> Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_commethod(25)
    def get_ActionResult(self) -> Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_commethod(26)
    def get_CurrentAction(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_ActionProgress(self) -> Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_commethod(28)
    def GetPropertyValue(self, propertyName: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2c44b950-a655-5321-aec1-aee762922131}')
    @winrt_commethod(6)
    def get_Update(self) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Action(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Update = property(get_Update, None)
    Action = property(get_Action, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
class IWindowsUpdateActionProgress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{83b22d8a-4bb0-549f-ba39-59724882d137}')
    @winrt_commethod(6)
    def get_Action(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Progress(self) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class IWindowsUpdateActionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6692c62-f697-51b7-ab7f-e73e5e688f12}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Action(self) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Action = property(get_Action, None)
class IWindowsUpdateAdministrator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7a60181c-ba1e-5cf9-aa65-304120b73d72}')
    @winrt_commethod(6)
    def StartAdministratorScan(self) -> Void: ...
    @winrt_commethod(7)
    def ApproveWindowsUpdateAction(self, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def RevokeWindowsUpdateActionApproval(self, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def ApproveWindowsUpdate(self, updateId: WinRT_String, approvalData: Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_commethod(10)
    def RevokeWindowsUpdateApproval(self, updateId: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def GetUpdates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
class IWindowsUpdateAdministratorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{013e6d36-ef69-53bc-8db8-c403bca550ed}')
    @winrt_commethod(6)
    def GetRegisteredAdministrator(self, organizationName: WinRT_String) -> Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_commethod(7)
    def RegisterForAdministration(self, organizationName: WinRT_String, options: Windows.Management.Update.WindowsUpdateAdministratorOptions) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(8)
    def UnregisterForAdministration(self, organizationName: WinRT_String) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_commethod(9)
    def GetRegisteredAdministratorName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def RequestRestart(self, restartOptions: Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_commethod(11)
    def CancelRestartRequest(self, requestRestartToken: WinRT_String) -> Void: ...
class IWindowsUpdateApprovalData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aadf5bfd-84db-59bc-85e2-ad4fc1f62f7c}')
    @winrt_commethod(6)
    def get_Seeker(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(7)
    def put_Seeker(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(8)
    def get_AllowDownloadOnMetered(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(9)
    def put_AllowDownloadOnMetered(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(10)
    def get_ComplianceDeadlineInDays(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(11)
    def put_ComplianceDeadlineInDays(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(12)
    def get_ComplianceGracePeriodInDays(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(13)
    def put_ComplianceGracePeriodInDays(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(14)
    def get_OptOutOfAutoReboot(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(15)
    def put_OptOutOfAutoReboot(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    Seeker = property(get_Seeker, put_Seeker)
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class IWindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{44df2579-74d3-5ffa-b6ce-09e187e1e0ed}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Reason = property(get_Reason, None)
    Timestamp = property(get_Timestamp, None)
class IWindowsUpdateAttentionRequiredReasonChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0627abca-dbb8-524a-b1d2-d9df004eeb31}')
    @winrt_commethod(6)
    def get_Update(self) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_Reason(self) -> Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Update = property(get_Update, None)
    Reason = property(get_Reason, None)
class IWindowsUpdateGetAdministratorResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bb39ffc4-2c42-5b1c-8995-343341c92c50}')
    @winrt_commethod(6)
    def get_Administrator(self) -> Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class IWindowsUpdateItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b222e44a-49b6-59bf-a033-ef617cd73a98}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UpdateId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_MoreInfoUrl(self) -> Windows.Foundation.Uri: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5dd966c0-a71a-5602-bbd0-09a70e4573fa}')
    @winrt_commethod(6)
    def add_ScanningStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScanningStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_WorkingStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_WorkingStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ProgressChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateProgressChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ProgressChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_AttentionRequiredReasonChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_AttentionRequiredReasonChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ActionCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateActionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ActionCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ScanCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateScanCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ScanCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def get_IsScanning(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsWorking(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_LastSuccessfulScanTimestamp(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(21)
    def GetApplicableUpdates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
    @winrt_commethod(22)
    def GetMostRecentCompletedUpdates(self, count: Int32) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdateItem]: ...
    @winrt_commethod(23)
    def GetMostRecentCompletedUpdatesAsync(self, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdateItem]]: ...
    @winrt_commethod(24)
    def StartScan(self, userInitiated: Boolean) -> Void: ...
    IsScanning = property(get_IsScanning, None)
    IsWorking = property(get_IsWorking, None)
    LastSuccessfulScanTimestamp = property(get_LastSuccessfulScanTimestamp, None)
class IWindowsUpdateManagerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1b394df8-decb-5f44-b47c-6ccf3bcfdb37}')
    @winrt_commethod(6)
    def CreateInstance(self, clientId: WinRT_String) -> Windows.Management.Update.WindowsUpdateManager: ...
class IWindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bbfbdeeb-94c8-5aa7-b0fb-66c67c233b0a}')
    @winrt_commethod(6)
    def get_Update(self) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_commethod(7)
    def get_ActionProgress(self) -> Windows.Management.Update.WindowsUpdateActionProgress: ...
    Update = property(get_Update, None)
    ActionProgress = property(get_ActionProgress, None)
class IWindowsUpdateRestartRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_MoreInfoUrl(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_MoreInfoUrl(self, value: Windows.Foundation.Uri) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{75f41d04-0e17-50d0-8c15-6b9d0539b3a9}')
    @winrt_commethod(6)
    def CreateInstance(self, title: WinRT_String, description: WinRT_String, moreInfoUrl: Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
class IWindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{95b6953e-ba5c-5fe8-b115-12de184a6bb0}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Updates(self) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Updates = property(get_Updates, None)
class PreviewBuildsManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.PreviewBuildsManager'
    @winrt_mixinmethod
    def get_ArePreviewBuildsAllowed(self: Windows.Management.Update.IPreviewBuildsManager) -> Boolean: ...
    @winrt_mixinmethod
    def put_ArePreviewBuildsAllowed(self: Windows.Management.Update.IPreviewBuildsManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: Windows.Management.Update.IPreviewBuildsManager) -> Windows.Management.Update.PreviewBuildsState: ...
    @winrt_mixinmethod
    def SyncAsync(self: Windows.Management.Update.IPreviewBuildsManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Management.Update.IPreviewBuildsManagerStatics) -> Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Management.Update.IPreviewBuildsManagerStatics) -> Boolean: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class PreviewBuildsState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.PreviewBuildsState'
    @winrt_mixinmethod
    def get_Properties(self: Windows.Management.Update.IPreviewBuildsState) -> Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class WindowsUpdate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdate'
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UpdateId(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsFeatureUpdate(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMinorImpact(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSecurity(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCritical(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsForOS(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDriver(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMandatory(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUrgent(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSeeker(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_SupportUrl(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsEulaAccepted(self: Windows.Management.Update.IWindowsUpdate) -> Boolean: ...
    @winrt_mixinmethod
    def get_EulaText(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_AttentionRequiredInfo(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Management.Update.WindowsUpdateAttentionRequiredInfo: ...
    @winrt_mixinmethod
    def get_ActionResult(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Management.Update.WindowsUpdateActionResult: ...
    @winrt_mixinmethod
    def get_CurrentAction(self: Windows.Management.Update.IWindowsUpdate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: Windows.Management.Update.IWindowsUpdate) -> Windows.Management.Update.WindowsUpdateActionProgress: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: Windows.Management.Update.IWindowsUpdate, propertyName: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def AcceptEula(self: Windows.Management.Update.IWindowsUpdate) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionCompletedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Action(self: Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Management.Update.IWindowsUpdateActionCompletedEventArgs) -> Windows.Foundation.HResult: ...
    Update = property(get_Update, None)
    Action = property(get_Action, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
class WindowsUpdateActionProgress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionProgress'
    @winrt_mixinmethod
    def get_Action(self: Windows.Management.Update.IWindowsUpdateActionProgress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.Management.Update.IWindowsUpdateActionProgress) -> Double: ...
    Action = property(get_Action, None)
    Progress = property(get_Progress, None)
class WindowsUpdateActionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateActionResult'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Management.Update.IWindowsUpdateActionResult) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Management.Update.IWindowsUpdateActionResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Management.Update.IWindowsUpdateActionResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Action(self: Windows.Management.Update.IWindowsUpdateActionResult) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Action = property(get_Action, None)
class WindowsUpdateAdministrator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateAdministrator'
    @winrt_mixinmethod
    def StartAdministratorScan(self: Windows.Management.Update.IWindowsUpdateAdministrator) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdateAction(self: Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateActionApproval(self: Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, action: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ApproveWindowsUpdate(self: Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String, approvalData: Windows.Management.Update.WindowsUpdateApprovalData) -> Void: ...
    @winrt_mixinmethod
    def RevokeWindowsUpdateApproval(self: Windows.Management.Update.IWindowsUpdateAdministrator, updateId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetUpdates(self: Windows.Management.Update.IWindowsUpdateAdministrator) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
    @winrt_classmethod
    def GetRegisteredAdministrator(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String) -> Windows.Management.Update.WindowsUpdateGetAdministratorResult: ...
    @winrt_classmethod
    def RegisterForAdministration(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String, options: Windows.Management.Update.WindowsUpdateAdministratorOptions) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def UnregisterForAdministration(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics, organizationName: WinRT_String) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    @winrt_classmethod
    def GetRegisteredAdministratorName(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def RequestRestart(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics, restartOptions: Windows.Management.Update.WindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_classmethod
    def CancelRestartRequest(cls: Windows.Management.Update.IWindowsUpdateAdministratorStatics, requestRestartToken: WinRT_String) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateApprovalData'
    @winrt_activatemethod
    def New(cls) -> Windows.Management.Update.WindowsUpdateApprovalData: ...
    @winrt_mixinmethod
    def get_Seeker(self: Windows.Management.Update.IWindowsUpdateApprovalData) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_Seeker(self: Windows.Management.Update.IWindowsUpdateApprovalData, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowDownloadOnMetered(self: Windows.Management.Update.IWindowsUpdateApprovalData) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_AllowDownloadOnMetered(self: Windows.Management.Update.IWindowsUpdateApprovalData, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceDeadlineInDays(self: Windows.Management.Update.IWindowsUpdateApprovalData) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_ComplianceDeadlineInDays(self: Windows.Management.Update.IWindowsUpdateApprovalData, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceGracePeriodInDays(self: Windows.Management.Update.IWindowsUpdateApprovalData) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_ComplianceGracePeriodInDays(self: Windows.Management.Update.IWindowsUpdateApprovalData, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_OptOutOfAutoReboot(self: Windows.Management.Update.IWindowsUpdateApprovalData) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_OptOutOfAutoReboot(self: Windows.Management.Update.IWindowsUpdateApprovalData, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    Seeker = property(get_Seeker, put_Seeker)
    AllowDownloadOnMetered = property(get_AllowDownloadOnMetered, put_AllowDownloadOnMetered)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class WindowsUpdateAttentionRequiredInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredInfo'
    @winrt_mixinmethod
    def get_Reason(self: Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Management.Update.IWindowsUpdateAttentionRequiredInfo) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Management.Update.IWindowsUpdateAttentionRequiredReasonChangedEventArgs) -> Windows.Management.Update.WindowsUpdateAttentionRequiredReason: ...
    Update = property(get_Update, None)
    Reason = property(get_Reason, None)
WindowsUpdateContract: UInt32 = 65536
class WindowsUpdateGetAdministratorResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateGetAdministratorResult'
    @winrt_mixinmethod
    def get_Administrator(self: Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> Windows.Management.Update.WindowsUpdateAdministrator: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Management.Update.IWindowsUpdateGetAdministratorResult) -> Windows.Management.Update.WindowsUpdateAdministratorStatus: ...
    Administrator = property(get_Administrator, None)
    Status = property(get_Status, None)
class WindowsUpdateItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateItem'
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UpdateId(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Management.Update.IWindowsUpdateItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: Windows.Management.Update.IWindowsUpdateItem) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Operation(self: Windows.Management.Update.IWindowsUpdateItem) -> WinRT_String: ...
    ProviderId = property(get_ProviderId, None)
    UpdateId = property(get_UpdateId, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    MoreInfoUrl = property(get_MoreInfoUrl, None)
    Category = property(get_Category, None)
    Operation = property(get_Operation, None)
class WindowsUpdateManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateManager'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Management.Update.IWindowsUpdateManagerFactory, clientId: WinRT_String) -> Windows.Management.Update.WindowsUpdateManager: ...
    @winrt_mixinmethod
    def add_ScanningStateChanged(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScanningStateChanged(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WorkingStateChanged(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WorkingStateChanged(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProgressChanged(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateProgressChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProgressChanged(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AttentionRequiredReasonChanged(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateAttentionRequiredReasonChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AttentionRequiredReasonChanged(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActionCompleted(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateActionCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActionCompleted(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScanCompleted(self: Windows.Management.Update.IWindowsUpdateManager, handler: Windows.Foundation.TypedEventHandler[Windows.Management.Update.WindowsUpdateManager, Windows.Management.Update.WindowsUpdateScanCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScanCompleted(self: Windows.Management.Update.IWindowsUpdateManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsScanning(self: Windows.Management.Update.IWindowsUpdateManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsWorking(self: Windows.Management.Update.IWindowsUpdateManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_LastSuccessfulScanTimestamp(self: Windows.Management.Update.IWindowsUpdateManager) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def GetApplicableUpdates(self: Windows.Management.Update.IWindowsUpdateManager) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
    @winrt_mixinmethod
    def GetMostRecentCompletedUpdates(self: Windows.Management.Update.IWindowsUpdateManager, count: Int32) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdateItem]: ...
    @winrt_mixinmethod
    def GetMostRecentCompletedUpdatesAsync(self: Windows.Management.Update.IWindowsUpdateManager, count: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdateItem]]: ...
    @winrt_mixinmethod
    def StartScan(self: Windows.Management.Update.IWindowsUpdateManager, userInitiated: Boolean) -> Void: ...
    IsScanning = property(get_IsScanning, None)
    IsWorking = property(get_IsWorking, None)
    LastSuccessfulScanTimestamp = property(get_LastSuccessfulScanTimestamp, None)
class WindowsUpdateProgressChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateProgressChangedEventArgs'
    @winrt_mixinmethod
    def get_Update(self: Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> Windows.Management.Update.WindowsUpdate: ...
    @winrt_mixinmethod
    def get_ActionProgress(self: Windows.Management.Update.IWindowsUpdateProgressChangedEventArgs) -> Windows.Management.Update.WindowsUpdateActionProgress: ...
    Update = property(get_Update, None)
    ActionProgress = property(get_ActionProgress, None)
class WindowsUpdateRestartRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateRestartRequestOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Management.Update.IWindowsUpdateRestartRequestOptionsFactory, title: WinRT_String, description: WinRT_String, moreInfoUrl: Windows.Foundation.Uri, complianceDeadlineInDays: Int32, complianceGracePeriodInDays: Int32) -> Windows.Management.Update.WindowsUpdateRestartRequestOptions: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MoreInfoUrl(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_MoreInfoUrl(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceDeadlineInDays(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_ComplianceDeadlineInDays(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ComplianceGracePeriodInDays(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_ComplianceGracePeriodInDays(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_OrganizationName(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_OrganizationName(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_OptOutOfAutoReboot(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_OptOutOfAutoReboot(self: Windows.Management.Update.IWindowsUpdateRestartRequestOptions, value: Boolean) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    MoreInfoUrl = property(get_MoreInfoUrl, put_MoreInfoUrl)
    ComplianceDeadlineInDays = property(get_ComplianceDeadlineInDays, put_ComplianceDeadlineInDays)
    ComplianceGracePeriodInDays = property(get_ComplianceGracePeriodInDays, put_ComplianceGracePeriodInDays)
    OrganizationName = property(get_OrganizationName, put_OrganizationName)
    OptOutOfAutoReboot = property(get_OptOutOfAutoReboot, put_OptOutOfAutoReboot)
class WindowsUpdateScanCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.WindowsUpdateScanCompletedEventArgs'
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Updates(self: Windows.Management.Update.IWindowsUpdateScanCompletedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Management.Update.WindowsUpdate]: ...
    ProviderId = property(get_ProviderId, None)
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Updates = property(get_Updates, None)
make_head(_module, 'IPreviewBuildsManager')
make_head(_module, 'IPreviewBuildsManagerStatics')
make_head(_module, 'IPreviewBuildsState')
make_head(_module, 'IWindowsUpdate')
make_head(_module, 'IWindowsUpdateActionCompletedEventArgs')
make_head(_module, 'IWindowsUpdateActionProgress')
make_head(_module, 'IWindowsUpdateActionResult')
make_head(_module, 'IWindowsUpdateAdministrator')
make_head(_module, 'IWindowsUpdateAdministratorStatics')
make_head(_module, 'IWindowsUpdateApprovalData')
make_head(_module, 'IWindowsUpdateAttentionRequiredInfo')
make_head(_module, 'IWindowsUpdateAttentionRequiredReasonChangedEventArgs')
make_head(_module, 'IWindowsUpdateGetAdministratorResult')
make_head(_module, 'IWindowsUpdateItem')
make_head(_module, 'IWindowsUpdateManager')
make_head(_module, 'IWindowsUpdateManagerFactory')
make_head(_module, 'IWindowsUpdateProgressChangedEventArgs')
make_head(_module, 'IWindowsUpdateRestartRequestOptions')
make_head(_module, 'IWindowsUpdateRestartRequestOptionsFactory')
make_head(_module, 'IWindowsUpdateScanCompletedEventArgs')
make_head(_module, 'PreviewBuildsManager')
make_head(_module, 'PreviewBuildsState')
make_head(_module, 'WindowsUpdate')
make_head(_module, 'WindowsUpdateActionCompletedEventArgs')
make_head(_module, 'WindowsUpdateActionProgress')
make_head(_module, 'WindowsUpdateActionResult')
make_head(_module, 'WindowsUpdateAdministrator')
make_head(_module, 'WindowsUpdateApprovalData')
make_head(_module, 'WindowsUpdateAttentionRequiredInfo')
make_head(_module, 'WindowsUpdateAttentionRequiredReasonChangedEventArgs')
make_head(_module, 'WindowsUpdateGetAdministratorResult')
make_head(_module, 'WindowsUpdateItem')
make_head(_module, 'WindowsUpdateManager')
make_head(_module, 'WindowsUpdateProgressChangedEventArgs')
make_head(_module, 'WindowsUpdateRestartRequestOptions')
make_head(_module, 'WindowsUpdateScanCompletedEventArgs')
