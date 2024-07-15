from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management.Setup
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AgentProvisioningProgressReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport
    _classid_ = 'Windows.Management.Setup.AgentProvisioningProgressReport'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Management.Setup.AgentProvisioningProgressReport.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.Setup.AgentProvisioningProgressReport: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> win32more.Windows.Management.Setup.DeploymentAgentProgressState: ...
    @winrt_mixinmethod
    def put_State(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: win32more.Windows.Management.Setup.DeploymentAgentProgressState) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressPercentage(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> Double: ...
    @winrt_mixinmethod
    def put_ProgressPercentage(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_EstimatedTimeRemaining(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_EstimatedTimeRemaining(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayProgress(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayProgress(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayProgressSecondary(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayProgressSecondary(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Batches(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Management.Setup.DeploymentWorkloadBatch]: ...
    @winrt_mixinmethod
    def get_CurrentBatchIndex(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport) -> UInt32: ...
    @winrt_mixinmethod
    def put_CurrentBatchIndex(self: win32more.Windows.Management.Setup.IAgentProvisioningProgressReport, value: UInt32) -> Void: ...
    Batches = property(get_Batches, None)
    CurrentBatchIndex = property(get_CurrentBatchIndex, put_CurrentBatchIndex)
    DisplayProgress = property(get_DisplayProgress, put_DisplayProgress)
    DisplayProgressSecondary = property(get_DisplayProgressSecondary, put_DisplayProgressSecondary)
    EstimatedTimeRemaining = property(get_EstimatedTimeRemaining, put_EstimatedTimeRemaining)
    ProgressPercentage = property(get_ProgressPercentage, put_ProgressPercentage)
    State = property(get_State, put_State)
class DeploymentAgentProgressState(Enum, Int32):
    NotStarted = 0
    Initializing = 1
    InProgress = 2
    Completed = 3
    ErrorOccurred = 4
    RebootRequired = 5
    Canceled = 6
class DeploymentSessionConnectionChange(Enum, Int32):
    NoChange = 0
    HostConnectionLost = 1
    HostConnectionRestored = 2
    AgentConnectionLost = 3
    AgentConnectionRestored = 4
    InternetConnectionLost = 5
    InternetConnectionRestored = 6
class DeploymentSessionConnectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDeploymentSessionConnectionChangedEventArgs
    _classid_ = 'Windows.Management.Setup.DeploymentSessionConnectionChangedEventArgs'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Management.Setup.IDeploymentSessionConnectionChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Change(self: win32more.Windows.Management.Setup.IDeploymentSessionConnectionChangedEventArgs) -> win32more.Windows.Management.Setup.DeploymentSessionConnectionChange: ...
    Change = property(get_Change, None)
    SessionId = property(get_SessionId, None)
class DeploymentSessionHeartbeatRequested(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c94a770b-5b05-4595-9e69-79070484377e}')
    @winrt_commethod(3)
    def Invoke(self, eventArgs: win32more.Windows.Management.Setup.DeploymentSessionHeartbeatRequestedEventArgs) -> Void: ...
class DeploymentSessionHeartbeatRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDeploymentSessionHeartbeatRequestedEventArgs
    _classid_ = 'Windows.Management.Setup.DeploymentSessionHeartbeatRequestedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Management.Setup.IDeploymentSessionHeartbeatRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Management.Setup.IDeploymentSessionHeartbeatRequestedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class DeploymentSessionStateChange(Enum, Int32):
    NoChange = 0
    CancelRequestedByUser = 1
    RetryRequestedByUser = 2
class DeploymentSessionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDeploymentSessionStateChangedEventArgs
    _classid_ = 'Windows.Management.Setup.DeploymentSessionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Management.Setup.IDeploymentSessionStateChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Change(self: win32more.Windows.Management.Setup.IDeploymentSessionStateChangedEventArgs) -> win32more.Windows.Management.Setup.DeploymentSessionStateChange: ...
    Change = property(get_Change, None)
    SessionId = property(get_SessionId, None)
class DeploymentWorkload(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDeploymentWorkload
    _classid_ = 'Windows.Management.Setup.DeploymentWorkload'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Setup.DeploymentWorkload.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Setup.IDeploymentWorkloadFactory, id: WinRT_String) -> win32more.Windows.Management.Setup.DeploymentWorkload: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayFriendlyName(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayFriendlyName(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StartTime(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_EndTime(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> UInt32: ...
    @winrt_mixinmethod
    def put_ErrorCode(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorMessage(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ErrorMessage(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PossibleCause(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PossibleCause(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PossibleResolution(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PossibleResolution(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> win32more.Windows.Management.Setup.DeploymentWorkloadState: ...
    @winrt_mixinmethod
    def put_State(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: win32more.Windows.Management.Setup.DeploymentWorkloadState) -> Void: ...
    @winrt_mixinmethod
    def get_StateDetails(self: win32more.Windows.Management.Setup.IDeploymentWorkload) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StateDetails(self: win32more.Windows.Management.Setup.IDeploymentWorkload, value: WinRT_String) -> Void: ...
    DisplayFriendlyName = property(get_DisplayFriendlyName, put_DisplayFriendlyName)
    EndTime = property(get_EndTime, put_EndTime)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    ErrorMessage = property(get_ErrorMessage, put_ErrorMessage)
    Id = property(get_Id, None)
    PossibleCause = property(get_PossibleCause, put_PossibleCause)
    PossibleResolution = property(get_PossibleResolution, put_PossibleResolution)
    StartTime = property(get_StartTime, put_StartTime)
    State = property(get_State, put_State)
    StateDetails = property(get_StateDetails, put_StateDetails)
class DeploymentWorkloadBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDeploymentWorkloadBatch
    _classid_ = 'Windows.Management.Setup.DeploymentWorkloadBatch'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Management.Setup.DeploymentWorkloadBatch.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Management.Setup.IDeploymentWorkloadBatchFactory, id: UInt32) -> win32more.Windows.Management.Setup.DeploymentWorkloadBatch: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Management.Setup.IDeploymentWorkloadBatch) -> UInt32: ...
    @winrt_mixinmethod
    def get_DisplayCategoryTitle(self: win32more.Windows.Management.Setup.IDeploymentWorkloadBatch) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayCategoryTitle(self: win32more.Windows.Management.Setup.IDeploymentWorkloadBatch, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BatchWorkloads(self: win32more.Windows.Management.Setup.IDeploymentWorkloadBatch) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Management.Setup.DeploymentWorkload]: ...
    BatchWorkloads = property(get_BatchWorkloads, None)
    DisplayCategoryTitle = property(get_DisplayCategoryTitle, put_DisplayCategoryTitle)
    Id = property(get_Id, None)
class DeploymentWorkloadState(Enum, Int32):
    NotStarted = 0
    InProgress = 1
    Completed = 2
    Failed = 3
    Canceled = 4
    Skipped = 5
    Uninstalled = 6
    RebootRequired = 7
class DevicePreparationExecutionContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IDevicePreparationExecutionContext
    _classid_ = 'Windows.Management.Setup.DevicePreparationExecutionContext'
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Management.Setup.IDevicePreparationExecutionContext) -> WinRT_String: ...
    Context = property(get_Context, None)
class IAgentProvisioningProgressReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IAgentProvisioningProgressReport'
    _iid_ = Guid('{5097398a-70cc-5181-a7af-d31c167323d1}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Management.Setup.DeploymentAgentProgressState: ...
    @winrt_commethod(7)
    def put_State(self, value: win32more.Windows.Management.Setup.DeploymentAgentProgressState) -> Void: ...
    @winrt_commethod(8)
    def get_ProgressPercentage(self) -> Double: ...
    @winrt_commethod(9)
    def put_ProgressPercentage(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_EstimatedTimeRemaining(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_EstimatedTimeRemaining(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_DisplayProgress(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_DisplayProgress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_DisplayProgressSecondary(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_DisplayProgressSecondary(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Batches(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Management.Setup.DeploymentWorkloadBatch]: ...
    @winrt_commethod(17)
    def get_CurrentBatchIndex(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_CurrentBatchIndex(self, value: UInt32) -> Void: ...
    Batches = property(get_Batches, None)
    CurrentBatchIndex = property(get_CurrentBatchIndex, put_CurrentBatchIndex)
    DisplayProgress = property(get_DisplayProgress, put_DisplayProgress)
    DisplayProgressSecondary = property(get_DisplayProgressSecondary, put_DisplayProgressSecondary)
    EstimatedTimeRemaining = property(get_EstimatedTimeRemaining, put_EstimatedTimeRemaining)
    ProgressPercentage = property(get_ProgressPercentage, put_ProgressPercentage)
    State = property(get_State, put_State)
class IDeploymentSessionConnectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentSessionConnectionChangedEventArgs'
    _iid_ = Guid('{8d40c631-6e4b-5d59-92f8-0de54c2a3c6b}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Change(self) -> win32more.Windows.Management.Setup.DeploymentSessionConnectionChange: ...
    Change = property(get_Change, None)
    SessionId = property(get_SessionId, None)
class IDeploymentSessionHeartbeatRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentSessionHeartbeatRequestedEventArgs'
    _iid_ = Guid('{09d81fa0-1036-58e6-b63b-fe343c45005f}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IDeploymentSessionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentSessionStateChangedEventArgs'
    _iid_ = Guid('{fbd3b7f3-88cb-5703-b8a5-0218de8fed81}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Change(self) -> win32more.Windows.Management.Setup.DeploymentSessionStateChange: ...
    Change = property(get_Change, None)
    SessionId = property(get_SessionId, None)
class IDeploymentWorkload(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentWorkload'
    _iid_ = Guid('{1cefd3d4-456c-50d1-9312-cc5c818fc12e}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayFriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayFriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_StartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(10)
    def put_StartTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(11)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(12)
    def put_EndTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(13)
    def get_ErrorCode(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_ErrorCode(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_ErrorMessage(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_ErrorMessage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_PossibleCause(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_PossibleCause(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def get_PossibleResolution(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_PossibleResolution(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_State(self) -> win32more.Windows.Management.Setup.DeploymentWorkloadState: ...
    @winrt_commethod(22)
    def put_State(self, value: win32more.Windows.Management.Setup.DeploymentWorkloadState) -> Void: ...
    @winrt_commethod(23)
    def get_StateDetails(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def put_StateDetails(self, value: WinRT_String) -> Void: ...
    DisplayFriendlyName = property(get_DisplayFriendlyName, put_DisplayFriendlyName)
    EndTime = property(get_EndTime, put_EndTime)
    ErrorCode = property(get_ErrorCode, put_ErrorCode)
    ErrorMessage = property(get_ErrorMessage, put_ErrorMessage)
    Id = property(get_Id, None)
    PossibleCause = property(get_PossibleCause, put_PossibleCause)
    PossibleResolution = property(get_PossibleResolution, put_PossibleResolution)
    StartTime = property(get_StartTime, put_StartTime)
    State = property(get_State, put_State)
    StateDetails = property(get_StateDetails, put_StateDetails)
class IDeploymentWorkloadBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentWorkloadBatch'
    _iid_ = Guid('{5e56e3df-b9c0-5fee-ba3f-e89d800a9bf2}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_DisplayCategoryTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayCategoryTitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_BatchWorkloads(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Management.Setup.DeploymentWorkload]: ...
    BatchWorkloads = property(get_BatchWorkloads, None)
    DisplayCategoryTitle = property(get_DisplayCategoryTitle, put_DisplayCategoryTitle)
    Id = property(get_Id, None)
class IDeploymentWorkloadBatchFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentWorkloadBatchFactory'
    _iid_ = Guid('{d0209697-9560-5a05-bdf6-f1af535cb0d4}')
    @winrt_commethod(6)
    def CreateInstance(self, id: UInt32) -> win32more.Windows.Management.Setup.DeploymentWorkloadBatch: ...
class IDeploymentWorkloadFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDeploymentWorkloadFactory'
    _iid_ = Guid('{41426c72-22a3-5339-bdf1-51268169aa61}')
    @winrt_commethod(6)
    def CreateInstance(self, id: WinRT_String) -> win32more.Windows.Management.Setup.DeploymentWorkload: ...
class IDevicePreparationExecutionContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IDevicePreparationExecutionContext'
    _iid_ = Guid('{084f221b-2484-5e81-a4e7-83f6caf19dc4}')
    @winrt_commethod(6)
    def get_Context(self) -> WinRT_String: ...
    Context = property(get_Context, None)
class IMachineProvisioningProgressReporter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IMachineProvisioningProgressReporter'
    _iid_ = Guid('{ebd8677f-dfd2-59da-ac3d-753ee1667cbb}')
    @winrt_commethod(6)
    def get_SessionId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_SessionConnection(self) -> win32more.Windows.Management.Setup.DeploymentSessionConnectionChange: ...
    @winrt_commethod(8)
    def get_SessionState(self) -> win32more.Windows.Management.Setup.DeploymentSessionStateChange: ...
    @winrt_commethod(9)
    def add_SessionStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Setup.MachineProvisioningProgressReporter, win32more.Windows.Management.Setup.DeploymentSessionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_SessionStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_SessionConnectionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Setup.MachineProvisioningProgressReporter, win32more.Windows.Management.Setup.DeploymentSessionConnectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_SessionConnectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def ReportProgress(self, updateReport: win32more.Windows.Management.Setup.AgentProvisioningProgressReport) -> Void: ...
    @winrt_commethod(14)
    def GetDevicePreparationExecutionContextAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Management.Setup.DevicePreparationExecutionContext]: ...
    SessionConnection = property(get_SessionConnection, None)
    SessionId = property(get_SessionId, None)
    SessionState = property(get_SessionState, None)
    SessionStateChanged = event()
    SessionConnectionChanged = event()
class IMachineProvisioningProgressReporterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Setup.IMachineProvisioningProgressReporterStatics'
    _iid_ = Guid('{77682c17-5da3-51fc-a042-c7b53458ddb5}')
    @winrt_commethod(6)
    def GetForLaunchUri(self, launchUri: win32more.Windows.Foundation.Uri, heartbeatHandler: win32more.Windows.Management.Setup.DeploymentSessionHeartbeatRequested) -> win32more.Windows.Management.Setup.MachineProvisioningProgressReporter: ...
class MachineProvisioningProgressReporter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter
    _classid_ = 'Windows.Management.Setup.MachineProvisioningProgressReporter'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter) -> Guid: ...
    @winrt_mixinmethod
    def get_SessionConnection(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter) -> win32more.Windows.Management.Setup.DeploymentSessionConnectionChange: ...
    @winrt_mixinmethod
    def get_SessionState(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter) -> win32more.Windows.Management.Setup.DeploymentSessionStateChange: ...
    @winrt_mixinmethod
    def add_SessionStateChanged(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Setup.MachineProvisioningProgressReporter, win32more.Windows.Management.Setup.DeploymentSessionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionStateChanged(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionConnectionChanged(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Setup.MachineProvisioningProgressReporter, win32more.Windows.Management.Setup.DeploymentSessionConnectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionConnectionChanged(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReportProgress(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter, updateReport: win32more.Windows.Management.Setup.AgentProvisioningProgressReport) -> Void: ...
    @winrt_mixinmethod
    def GetDevicePreparationExecutionContextAsync(self: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Management.Setup.DevicePreparationExecutionContext]: ...
    @winrt_classmethod
    def GetForLaunchUri(cls: win32more.Windows.Management.Setup.IMachineProvisioningProgressReporterStatics, launchUri: win32more.Windows.Foundation.Uri, heartbeatHandler: win32more.Windows.Management.Setup.DeploymentSessionHeartbeatRequested) -> win32more.Windows.Management.Setup.MachineProvisioningProgressReporter: ...
    SessionConnection = property(get_SessionConnection, None)
    SessionId = property(get_SessionId, None)
    SessionState = property(get_SessionState, None)
    SessionStateChanged = event()
    SessionConnectionChanged = event()


make_ready(__name__)
