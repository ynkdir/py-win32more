from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.System.Diagnostics
import win32more.Windows.System.RemoteSystems
import win32more.Windows.UI.Popups
import win32more.Windows.UI.ViewManagement
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AppActivationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppActivationResult
    _classid_ = 'Windows.System.AppActivationResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.System.IAppActivationResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: win32more.Windows.System.IAppActivationResult) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
    ExtendedError = property(get_ExtendedError, None)
class AppDiagnosticInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppDiagnosticInfo
    _classid_ = 'Windows.System.AppDiagnosticInfo'
    @winrt_mixinmethod
    def get_AppInfo(self: win32more.Windows.System.IAppDiagnosticInfo) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def GetResourceGroups(self: win32more.Windows.System.IAppDiagnosticInfo2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppResourceGroupInfo]: ...
    @winrt_mixinmethod
    def CreateResourceGroupWatcher(self: win32more.Windows.System.IAppDiagnosticInfo2) -> win32more.Windows.System.AppResourceGroupInfoWatcher: ...
    @winrt_mixinmethod
    def LaunchAsync(self: win32more.Windows.System.IAppDiagnosticInfo3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppActivationResult]: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.System.IAppDiagnosticInfoStatics2) -> win32more.Windows.System.AppDiagnosticInfoWatcher: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.System.IAppDiagnosticInfoStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.DiagnosticAccessStatus]: ...
    @winrt_classmethod
    def RequestInfoForPackageAsync(cls: win32more.Windows.System.IAppDiagnosticInfoStatics2, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoForAppAsync(cls: win32more.Windows.System.IAppDiagnosticInfoStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoForAppUserModelId(cls: win32more.Windows.System.IAppDiagnosticInfoStatics2, appUserModelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoAsync(cls: win32more.Windows.System.IAppDiagnosticInfoStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    AppInfo = property(get_AppInfo, None)
class AppDiagnosticInfoWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppDiagnosticInfoWatcher
    _classid_ = 'Windows.System.AppDiagnosticInfoWatcher'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.System.IAppDiagnosticInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.IAppDiagnosticInfoWatcher) -> win32more.Windows.System.AppDiagnosticInfoWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.IAppDiagnosticInfoWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.IAppDiagnosticInfoWatcher) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()
class AppDiagnosticInfoWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppDiagnosticInfoWatcherEventArgs
    _classid_ = 'Windows.System.AppDiagnosticInfoWatcherEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfo(self: win32more.Windows.System.IAppDiagnosticInfoWatcherEventArgs) -> win32more.Windows.System.AppDiagnosticInfo: ...
    AppDiagnosticInfo = property(get_AppDiagnosticInfo, None)
class AppDiagnosticInfoWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class AppExecutionStateChangeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppExecutionStateChangeResult
    _classid_ = 'Windows.System.AppExecutionStateChangeResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.System.IAppExecutionStateChangeResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class AppMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppMemoryReport
    _classid_ = 'Windows.System.AppMemoryReport'
    @winrt_mixinmethod
    def get_PrivateCommitUsage(self: win32more.Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakPrivateCommitUsage(self: win32more.Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitUsage(self: win32more.Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitLimit(self: win32more.Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_ExpectedTotalCommitLimit(self: win32more.Windows.System.IAppMemoryReport2) -> UInt64: ...
    ExpectedTotalCommitLimit = property(get_ExpectedTotalCommitLimit, None)
    PeakPrivateCommitUsage = property(get_PeakPrivateCommitUsage, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitLimit = property(get_TotalCommitLimit, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class AppMemoryUsageLevel(Enum, Int32):
    Low = 0
    Medium = 1
    High = 2
    OverLimit = 3
class AppMemoryUsageLimitChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppMemoryUsageLimitChangingEventArgs
    _classid_ = 'Windows.System.AppMemoryUsageLimitChangingEventArgs'
    @winrt_mixinmethod
    def get_OldLimit(self: win32more.Windows.System.IAppMemoryUsageLimitChangingEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_NewLimit(self: win32more.Windows.System.IAppMemoryUsageLimitChangingEventArgs) -> UInt64: ...
    NewLimit = property(get_NewLimit, None)
    OldLimit = property(get_OldLimit, None)
class AppResourceGroupBackgroundTaskReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupBackgroundTaskReport
    _classid_ = 'Windows.System.AppResourceGroupBackgroundTaskReport'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.System.IAppResourceGroupBackgroundTaskReport) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Trigger(self: win32more.Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EntryPoint(self: win32more.Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    EntryPoint = property(get_EntryPoint, None)
    Name = property(get_Name, None)
    TaskId = property(get_TaskId, None)
    Trigger = property(get_Trigger, None)
class AppResourceGroupEnergyQuotaState(Enum, Int32):
    Unknown = 0
    Over = 1
    Under = 2
class AppResourceGroupExecutionState(Enum, Int32):
    Unknown = 0
    Running = 1
    Suspending = 2
    Suspended = 3
    NotRunning = 4
class AppResourceGroupInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupInfo
    _classid_ = 'Windows.System.AppResourceGroupInfo'
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.System.IAppResourceGroupInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_IsShared(self: win32more.Windows.System.IAppResourceGroupInfo) -> Boolean: ...
    @winrt_mixinmethod
    def GetBackgroundTaskReports(self: win32more.Windows.System.IAppResourceGroupInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppResourceGroupBackgroundTaskReport]: ...
    @winrt_mixinmethod
    def GetMemoryReport(self: win32more.Windows.System.IAppResourceGroupInfo) -> win32more.Windows.System.AppResourceGroupMemoryReport: ...
    @winrt_mixinmethod
    def GetProcessDiagnosticInfos(self: win32more.Windows.System.IAppResourceGroupInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_mixinmethod
    def GetStateReport(self: win32more.Windows.System.IAppResourceGroupInfo) -> win32more.Windows.System.AppResourceGroupStateReport: ...
    @winrt_mixinmethod
    def StartSuspendAsync(self: win32more.Windows.System.IAppResourceGroupInfo2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_mixinmethod
    def StartResumeAsync(self: win32more.Windows.System.IAppResourceGroupInfo2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_mixinmethod
    def StartTerminateAsync(self: win32more.Windows.System.IAppResourceGroupInfo2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
    InstanceId = property(get_InstanceId, None)
    IsShared = property(get_IsShared, None)
class AppResourceGroupInfoWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupInfoWatcher
    _classid_ = 'Windows.System.AppResourceGroupInfoWatcher'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ExecutionStateChanged(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExecutionStateChanged(self: win32more.Windows.System.IAppResourceGroupInfoWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.IAppResourceGroupInfoWatcher) -> win32more.Windows.System.AppResourceGroupInfoWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.IAppResourceGroupInfoWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.IAppResourceGroupInfoWatcher) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()
    ExecutionStateChanged = event()
class AppResourceGroupInfoWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupInfoWatcherEventArgs
    _classid_ = 'Windows.System.AppResourceGroupInfoWatcherEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfos(self: win32more.Windows.System.IAppResourceGroupInfoWatcherEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.AppDiagnosticInfo]: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: win32more.Windows.System.IAppResourceGroupInfoWatcherEventArgs) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class AppResourceGroupInfoWatcherExecutionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs
    _classid_ = 'Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfos(self: win32more.Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.AppDiagnosticInfo]: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: win32more.Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class AppResourceGroupInfoWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class AppResourceGroupMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupMemoryReport
    _classid_ = 'Windows.System.AppResourceGroupMemoryReport'
    @winrt_mixinmethod
    def get_CommitUsageLimit(self: win32more.Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_CommitUsageLevel(self: win32more.Windows.System.IAppResourceGroupMemoryReport) -> win32more.Windows.System.AppMemoryUsageLevel: ...
    @winrt_mixinmethod
    def get_PrivateCommitUsage(self: win32more.Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitUsage(self: win32more.Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    CommitUsageLevel = property(get_CommitUsageLevel, None)
    CommitUsageLimit = property(get_CommitUsageLimit, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class AppResourceGroupStateReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppResourceGroupStateReport
    _classid_ = 'Windows.System.AppResourceGroupStateReport'
    @winrt_mixinmethod
    def get_ExecutionState(self: win32more.Windows.System.IAppResourceGroupStateReport) -> win32more.Windows.System.AppResourceGroupExecutionState: ...
    @winrt_mixinmethod
    def get_EnergyQuotaState(self: win32more.Windows.System.IAppResourceGroupStateReport) -> win32more.Windows.System.AppResourceGroupEnergyQuotaState: ...
    EnergyQuotaState = property(get_EnergyQuotaState, None)
    ExecutionState = property(get_ExecutionState, None)
class AppUriHandlerHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppUriHandlerHost
    _classid_ = 'Windows.System.AppUriHandlerHost'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.AppUriHandlerHost.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.System.AppUriHandlerHost.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.AppUriHandlerHost: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.IAppUriHandlerHostFactory, name: WinRT_String) -> win32more.Windows.System.AppUriHandlerHost: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.System.IAppUriHandlerHost) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.System.IAppUriHandlerHost, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.System.IAppUriHandlerHost2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.System.IAppUriHandlerHost2, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Name = property(get_Name, put_Name)
class AppUriHandlerRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppUriHandlerRegistration
    _classid_ = 'Windows.System.AppUriHandlerRegistration'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.System.IAppUriHandlerRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.IAppUriHandlerRegistration) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def GetAppAddedHostsAsync(self: win32more.Windows.System.IAppUriHandlerRegistration) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppUriHandlerHost]]: ...
    @winrt_mixinmethod
    def SetAppAddedHostsAsync(self: win32more.Windows.System.IAppUriHandlerRegistration, hosts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.AppUriHandlerHost]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetAllHosts(self: win32more.Windows.System.IAppUriHandlerRegistration2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppUriHandlerHost]: ...
    @winrt_mixinmethod
    def UpdateHosts(self: win32more.Windows.System.IAppUriHandlerRegistration2, hosts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.AppUriHandlerHost]) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.System.IAppUriHandlerRegistration2) -> WinRT_String: ...
    Name = property(get_Name, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    User = property(get_User, None)
class AppUriHandlerRegistrationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IAppUriHandlerRegistrationManager
    _classid_ = 'Windows.System.AppUriHandlerRegistrationManager'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.IAppUriHandlerRegistrationManager) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetRegistration(self: win32more.Windows.System.IAppUriHandlerRegistrationManager, name: WinRT_String) -> win32more.Windows.System.AppUriHandlerRegistration: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.System.IAppUriHandlerRegistrationManager2) -> WinRT_String: ...
    @winrt_classmethod
    def GetForPackage(cls: win32more.Windows.System.IAppUriHandlerRegistrationManagerStatics2, packageFamilyName: WinRT_String) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetForPackageForUser(cls: win32more.Windows.System.IAppUriHandlerRegistrationManagerStatics2, packageFamilyName: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.System.IAppUriHandlerRegistrationManagerStatics) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.System.IAppUriHandlerRegistrationManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
    User = property(get_User, None)
class AutoUpdateTimeZoneStatus(Enum, Int32):
    Attempted = 0
    TimedOut = 1
    Failed = 2
class DateTimeSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.DateTimeSettings'
    @winrt_classmethod
    def SetSystemDateTime(cls: win32more.Windows.System.IDateTimeSettingsStatics, utcDateTime: win32more.Windows.Foundation.DateTime) -> Void: ...
class DiagnosticAccessStatus(Enum, Int32):
    Unspecified = 0
    Denied = 1
    Limited = 2
    Allowed = 3
class DispatcherQueue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IDispatcherQueue
    _classid_ = 'Windows.System.DispatcherQueue'
    @winrt_mixinmethod
    def CreateTimer(self: win32more.Windows.System.IDispatcherQueue) -> win32more.Windows.System.DispatcherQueueTimer: ...
    @winrt_mixinmethod
    def TryEnqueue(self: win32more.Windows.System.IDispatcherQueue, callback: win32more.Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnqueueWithPriority(self: win32more.Windows.System.IDispatcherQueue, priority: win32more.Windows.System.DispatcherQueuePriority, callback: win32more.Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def add_ShutdownStarting(self: win32more.Windows.System.IDispatcherQueue, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueue, win32more.Windows.System.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShutdownStarting(self: win32more.Windows.System.IDispatcherQueue, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShutdownCompleted(self: win32more.Windows.System.IDispatcherQueue, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShutdownCompleted(self: win32more.Windows.System.IDispatcherQueue, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HasThreadAccess(self: win32more.Windows.System.IDispatcherQueue2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: win32more.Windows.System.IDispatcherQueueStatics) -> win32more.Windows.System.DispatcherQueue: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
    ShutdownStarting = event()
    ShutdownCompleted = event()
class DispatcherQueueController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IDispatcherQueueController
    _classid_ = 'Windows.System.DispatcherQueueController'
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.System.IDispatcherQueueController) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def ShutdownQueueAsync(self: win32more.Windows.System.IDispatcherQueueController) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateOnDedicatedThread(cls: win32more.Windows.System.IDispatcherQueueControllerStatics) -> win32more.Windows.System.DispatcherQueueController: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class DispatcherQueueHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfa2dc9c-1a2d-4917-98f2-939af1d6e0c8}')
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class DispatcherQueuePriority(Enum, Int32):
    Low = -10
    Normal = 0
    High = 10
class DispatcherQueueShutdownStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IDispatcherQueueShutdownStartingEventArgs
    _classid_ = 'Windows.System.DispatcherQueueShutdownStartingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.System.IDispatcherQueueShutdownStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class DispatcherQueueTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IDispatcherQueueTimer
    _classid_ = 'Windows.System.DispatcherQueueTimer'
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.System.IDispatcherQueueTimer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Windows.System.IDispatcherQueueTimer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsRunning(self: win32more.Windows.System.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRepeating(self: win32more.Windows.System.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRepeating(self: win32more.Windows.System.IDispatcherQueueTimer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def add_Tick(self: win32more.Windows.System.IDispatcherQueueTimer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueueTimer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tick(self: win32more.Windows.System.IDispatcherQueueTimer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
    IsRunning = property(get_IsRunning, None)
    Tick = event()
class FolderLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IFolderLauncherOptions
    _classid_ = 'Windows.System.FolderLauncherOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.FolderLauncherOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.FolderLauncherOptions: ...
    @winrt_mixinmethod
    def get_ItemsToSelect(self: win32more.Windows.System.IFolderLauncherOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_DesiredRemainingView(self: win32more.Windows.System.ILauncherViewOptions) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_DesiredRemainingView(self: win32more.Windows.System.ILauncherViewOptions, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
    ItemsToSelect = property(get_ItemsToSelect, None)
class IAppActivationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppActivationResult'
    _iid_ = Guid('{6b528900-f46e-4eb0-aa6c-38af557cf9ed}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
    ExtendedError = property(get_ExtendedError, None)
class IAppDiagnosticInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfo'
    _iid_ = Guid('{e348a69a-8889-4ca3-be07-d5ffff5f0804}')
    @winrt_commethod(6)
    def get_AppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    AppInfo = property(get_AppInfo, None)
class IAppDiagnosticInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfo2'
    _iid_ = Guid('{df46fbd7-191a-446c-9473-8fbc2374a354}')
    @winrt_commethod(6)
    def GetResourceGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppResourceGroupInfo]: ...
    @winrt_commethod(7)
    def CreateResourceGroupWatcher(self) -> win32more.Windows.System.AppResourceGroupInfoWatcher: ...
class IAppDiagnosticInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfo3'
    _iid_ = Guid('{c895c63d-dd61-4c65-babd-81a10b4f9815}')
    @winrt_commethod(6)
    def LaunchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppActivationResult]: ...
class IAppDiagnosticInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfoStatics'
    _iid_ = Guid('{ce6925bf-10ca-40c8-a9ca-c5c96501866e}')
    @winrt_commethod(6)
    def RequestInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
class IAppDiagnosticInfoStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfoStatics2'
    _iid_ = Guid('{05b24b86-1000-4c90-bb9f-7235071c50fe}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.System.AppDiagnosticInfoWatcher: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.DiagnosticAccessStatus]: ...
    @winrt_commethod(8)
    def RequestInfoForPackageAsync(self, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    @winrt_commethod(9)
    def RequestInfoForAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
    @winrt_commethod(10)
    def RequestInfoForAppUserModelId(self, appUserModelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppDiagnosticInfo]]: ...
class IAppDiagnosticInfoWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfoWatcher'
    _iid_ = Guid('{75575070-01d3-489a-9325-52f9cc6ede0a}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppDiagnosticInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> win32more.Windows.System.AppDiagnosticInfoWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()
class IAppDiagnosticInfoWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppDiagnosticInfoWatcherEventArgs'
    _iid_ = Guid('{7017c716-e1da-4c65-99df-046dff5be71a}')
    @winrt_commethod(6)
    def get_AppDiagnosticInfo(self) -> win32more.Windows.System.AppDiagnosticInfo: ...
    AppDiagnosticInfo = property(get_AppDiagnosticInfo, None)
class IAppExecutionStateChangeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppExecutionStateChangeResult'
    _iid_ = Guid('{6f039bf0-f91b-4df8-ae77-3033ccb69114}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAppMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppMemoryReport'
    _iid_ = Guid('{6d65339b-4d6f-45bc-9c5e-e49b3ff2758d}')
    @winrt_commethod(6)
    def get_PrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_PeakPrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_TotalCommitUsage(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_TotalCommitLimit(self) -> UInt64: ...
    PeakPrivateCommitUsage = property(get_PeakPrivateCommitUsage, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitLimit = property(get_TotalCommitLimit, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class IAppMemoryReport2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppMemoryReport2'
    _iid_ = Guid('{5f7f3738-51b7-42dc-b7ed-79ba46d28857}')
    @winrt_commethod(6)
    def get_ExpectedTotalCommitLimit(self) -> UInt64: ...
    ExpectedTotalCommitLimit = property(get_ExpectedTotalCommitLimit, None)
class IAppMemoryUsageLimitChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppMemoryUsageLimitChangingEventArgs'
    _iid_ = Guid('{79f86664-feca-4da5-9e40-2bc63efdc979}')
    @winrt_commethod(6)
    def get_OldLimit(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_NewLimit(self) -> UInt64: ...
    NewLimit = property(get_NewLimit, None)
    OldLimit = property(get_OldLimit, None)
class IAppResourceGroupBackgroundTaskReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupBackgroundTaskReport'
    _iid_ = Guid('{2566e74e-b05d-40c2-9dc1-1a4f039ea120}')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Trigger(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_EntryPoint(self) -> WinRT_String: ...
    EntryPoint = property(get_EntryPoint, None)
    Name = property(get_Name, None)
    TaskId = property(get_TaskId, None)
    Trigger = property(get_Trigger, None)
class IAppResourceGroupInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupInfo'
    _iid_ = Guid('{b913f77a-e807-49f4-845e-7b8bdcfe8ee7}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_IsShared(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetBackgroundTaskReports(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppResourceGroupBackgroundTaskReport]: ...
    @winrt_commethod(9)
    def GetMemoryReport(self) -> win32more.Windows.System.AppResourceGroupMemoryReport: ...
    @winrt_commethod(10)
    def GetProcessDiagnosticInfos(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_commethod(11)
    def GetStateReport(self) -> win32more.Windows.System.AppResourceGroupStateReport: ...
    InstanceId = property(get_InstanceId, None)
    IsShared = property(get_IsShared, None)
class IAppResourceGroupInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupInfo2'
    _iid_ = Guid('{ee9b236d-d305-4d6b-92f7-6afdad72dedc}')
    @winrt_commethod(6)
    def StartSuspendAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_commethod(7)
    def StartResumeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_commethod(8)
    def StartTerminateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AppExecutionStateChangeResult]: ...
class IAppResourceGroupInfoWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupInfoWatcher'
    _iid_ = Guid('{d9b0a0fd-6e5a-4c72-8b17-09fec4a212bd}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ExecutionStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.AppResourceGroupInfoWatcher, win32more.Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ExecutionStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> win32more.Windows.System.AppResourceGroupInfoWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    EnumerationCompleted = event()
    Stopped = event()
    ExecutionStateChanged = event()
class IAppResourceGroupInfoWatcherEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupInfoWatcherEventArgs'
    _iid_ = Guid('{7a787637-6302-4d2f-bf89-1c12d0b2a6b9}')
    @winrt_commethod(6)
    def get_AppDiagnosticInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.AppDiagnosticInfo]: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs'
    _iid_ = Guid('{1bdbedd7-fee6-4fd4-98dd-e92a2cc299f3}')
    @winrt_commethod(6)
    def get_AppDiagnosticInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.AppDiagnosticInfo]: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> win32more.Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class IAppResourceGroupMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupMemoryReport'
    _iid_ = Guid('{2c8c06b1-7db1-4c51-a225-7fae2d49e431}')
    @winrt_commethod(6)
    def get_CommitUsageLimit(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_CommitUsageLevel(self) -> win32more.Windows.System.AppMemoryUsageLevel: ...
    @winrt_commethod(8)
    def get_PrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_TotalCommitUsage(self) -> UInt64: ...
    CommitUsageLevel = property(get_CommitUsageLevel, None)
    CommitUsageLimit = property(get_CommitUsageLimit, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class IAppResourceGroupStateReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppResourceGroupStateReport'
    _iid_ = Guid('{52849f18-2f70-4236-ab40-d04db0c7b931}')
    @winrt_commethod(6)
    def get_ExecutionState(self) -> win32more.Windows.System.AppResourceGroupExecutionState: ...
    @winrt_commethod(7)
    def get_EnergyQuotaState(self) -> win32more.Windows.System.AppResourceGroupEnergyQuotaState: ...
    EnergyQuotaState = property(get_EnergyQuotaState, None)
    ExecutionState = property(get_ExecutionState, None)
class IAppUriHandlerHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerHost'
    _iid_ = Guid('{5d50cac5-92d2-5409-b56f-7f73e10ea4c3}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
class IAppUriHandlerHost2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerHost2'
    _iid_ = Guid('{3a0bee95-29e4-51bf-8095-a3c068e3c72a}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IAppUriHandlerHostFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerHostFactory'
    _iid_ = Guid('{257c3c96-ce04-5f98-96bb-3ebd3e9275bb}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String) -> win32more.Windows.System.AppUriHandlerHost: ...
class IAppUriHandlerRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistration'
    _iid_ = Guid('{6f73aeb1-4569-5c3f-9ba0-99123eea32c3}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(8)
    def GetAppAddedHostsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppUriHandlerHost]]: ...
    @winrt_commethod(9)
    def SetAppAddedHostsAsync(self, hosts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.AppUriHandlerHost]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Name = property(get_Name, None)
    User = property(get_User, None)
class IAppUriHandlerRegistration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistration2'
    _iid_ = Guid('{d54dac97-cb39-5f1f-883e-01853730bd6d}')
    @winrt_commethod(6)
    def GetAllHosts(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.AppUriHandlerHost]: ...
    @winrt_commethod(7)
    def UpdateHosts(self, hosts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.System.AppUriHandlerHost]) -> Void: ...
    @winrt_commethod(8)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppUriHandlerRegistrationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistrationManager'
    _iid_ = Guid('{e62c9a52-ac94-5750-ac1b-6cfb6f250263}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def TryGetRegistration(self, name: WinRT_String) -> win32more.Windows.System.AppUriHandlerRegistration: ...
    User = property(get_User, None)
class IAppUriHandlerRegistrationManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistrationManager2'
    _iid_ = Guid('{bddfcaf1-b51a-5e69-aefd-7088d9f2b123}')
    @winrt_commethod(6)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppUriHandlerRegistrationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistrationManagerStatics'
    _iid_ = Guid('{d5cedd9f-5729-5b76-a1d4-0285f295c124}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
class IAppUriHandlerRegistrationManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IAppUriHandlerRegistrationManagerStatics2'
    _iid_ = Guid('{14f78379-6890-5080-90a7-98824a7f079e}')
    @winrt_commethod(6)
    def GetForPackage(self, packageFamilyName: WinRT_String) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_commethod(7)
    def GetForPackageForUser(self, packageFamilyName: WinRT_String, user: win32more.Windows.System.User) -> win32more.Windows.System.AppUriHandlerRegistrationManager: ...
class IDateTimeSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDateTimeSettingsStatics'
    _iid_ = Guid('{5d2150d1-47ee-48ab-a52b-9f1954278d82}')
    @winrt_commethod(6)
    def SetSystemDateTime(self, utcDateTime: win32more.Windows.Foundation.DateTime) -> Void: ...
class IDispatcherQueue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueue'
    _iid_ = Guid('{603e88e4-a338-4ffe-a457-a5cfb9ceb899}')
    @winrt_commethod(6)
    def CreateTimer(self) -> win32more.Windows.System.DispatcherQueueTimer: ...
    @winrt_commethod(7)
    def TryEnqueue(self, callback: win32more.Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(8)
    def TryEnqueueWithPriority(self, priority: win32more.Windows.System.DispatcherQueuePriority, callback: win32more.Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(9)
    def add_ShutdownStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueue, win32more.Windows.System.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ShutdownStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_ShutdownCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ShutdownCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ShutdownStarting = event()
    ShutdownCompleted = event()
class IDispatcherQueue2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueue2'
    _iid_ = Guid('{c822c647-30ef-506e-bd1e-a647ae6675ff}')
    @winrt_commethod(6)
    def get_HasThreadAccess(self) -> Boolean: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class IDispatcherQueueController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueueController'
    _iid_ = Guid('{22f34e66-50db-4e36-a98d-61c01b384d20}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_commethod(7)
    def ShutdownQueueAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IDispatcherQueueControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueueControllerStatics'
    _iid_ = Guid('{0a6c98e0-5198-49a2-a313-3f70d1f13c27}')
    @winrt_commethod(6)
    def CreateOnDedicatedThread(self) -> win32more.Windows.System.DispatcherQueueController: ...
class IDispatcherQueueShutdownStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueueShutdownStartingEventArgs'
    _iid_ = Guid('{c4724c4c-ff97-40c0-a226-cc0aaa545e89}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IDispatcherQueueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueueStatics'
    _iid_ = Guid('{a96d83d7-9371-4517-9245-d0824ac12c74}')
    @winrt_commethod(6)
    def GetForCurrentThread(self) -> win32more.Windows.System.DispatcherQueue: ...
class IDispatcherQueueTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IDispatcherQueueTimer'
    _iid_ = Guid('{5feabb1d-a31c-4727-b1ac-37454649d56a}')
    @winrt_commethod(6)
    def get_Interval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Interval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_IsRunning(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsRepeating(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsRepeating(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    @winrt_commethod(13)
    def add_Tick(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.DispatcherQueueTimer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Tick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
    IsRunning = property(get_IsRunning, None)
    Tick = event()
class IFolderLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IFolderLauncherOptions'
    _iid_ = Guid('{bb91c27d-6b87-432a-bd04-776c6f5fb2ab}')
    @winrt_commethod(6)
    def get_ItemsToSelect(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.IStorageItem]: ...
    ItemsToSelect = property(get_ItemsToSelect, None)
class IKnownUserPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IKnownUserPropertiesStatics'
    _iid_ = Guid('{7755911a-70c5-48e5-b637-5ba3441e4ee4}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FirstName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LastName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ProviderName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AccountName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_GuestHost(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_PrincipalName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_DomainName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_SessionInitiationProtocolUri(self) -> WinRT_String: ...
    AccountName = property(get_AccountName, None)
    DisplayName = property(get_DisplayName, None)
    DomainName = property(get_DomainName, None)
    FirstName = property(get_FirstName, None)
    GuestHost = property(get_GuestHost, None)
    LastName = property(get_LastName, None)
    PrincipalName = property(get_PrincipalName, None)
    ProviderName = property(get_ProviderName, None)
    SessionInitiationProtocolUri = property(get_SessionInitiationProtocolUri, None)
class IKnownUserPropertiesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IKnownUserPropertiesStatics2'
    _iid_ = Guid('{5b450782-f620-577e-b1b3-dd56644d79b1}')
    @winrt_commethod(6)
    def get_AgeEnforcementRegion(self) -> WinRT_String: ...
    AgeEnforcementRegion = property(get_AgeEnforcementRegion, None)
class ILaunchUriResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILaunchUriResult'
    _iid_ = Guid('{ec27a8df-f6d5-45ca-913a-70a40c5c8221}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.System.LaunchUriStatus: ...
    @winrt_commethod(7)
    def get_Result(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class ILauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherOptions'
    _iid_ = Guid('{bafa21d8-b071-4cd8-853e-341203e557d3}')
    @winrt_commethod(6)
    def get_TreatAsUntrusted(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TreatAsUntrusted(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayApplicationPicker(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_DisplayApplicationPicker(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_UI(self) -> win32more.Windows.System.LauncherUIOptions: ...
    @winrt_commethod(11)
    def get_PreferredApplicationPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_PreferredApplicationPackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_PreferredApplicationDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_PreferredApplicationDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_FallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_FallbackUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_ContentType(self, value: WinRT_String) -> Void: ...
    ContentType = property(get_ContentType, put_ContentType)
    DisplayApplicationPicker = property(get_DisplayApplicationPicker, put_DisplayApplicationPicker)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    PreferredApplicationDisplayName = property(get_PreferredApplicationDisplayName, put_PreferredApplicationDisplayName)
    PreferredApplicationPackageFamilyName = property(get_PreferredApplicationPackageFamilyName, put_PreferredApplicationPackageFamilyName)
    TreatAsUntrusted = property(get_TreatAsUntrusted, put_TreatAsUntrusted)
    UI = property(get_UI, None)
class ILauncherOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherOptions2'
    _iid_ = Guid('{3ba08eb4-6e40-4dce-a1a3-2f53950afb49}')
    @winrt_commethod(6)
    def get_TargetApplicationPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetApplicationPackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_NeighboringFilesQuery(self) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(9)
    def put_NeighboringFilesQuery(self, value: win32more.Windows.Storage.Search.StorageFileQueryResult) -> Void: ...
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, put_NeighboringFilesQuery)
    TargetApplicationPackageFamilyName = property(get_TargetApplicationPackageFamilyName, put_TargetApplicationPackageFamilyName)
class ILauncherOptions3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherOptions3'
    _iid_ = Guid('{f0770655-4b63-4e3a-9107-4e687841923a}')
    @winrt_commethod(6)
    def get_IgnoreAppUriHandlers(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IgnoreAppUriHandlers(self, value: Boolean) -> Void: ...
    IgnoreAppUriHandlers = property(get_IgnoreAppUriHandlers, put_IgnoreAppUriHandlers)
class ILauncherOptions4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherOptions4'
    _iid_ = Guid('{ef6fd10e-e6fb-4814-a44e-57e8b9d9a01b}')
    @winrt_commethod(6)
    def get_LimitPickerToCurrentAppAndAppUriHandlers(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_LimitPickerToCurrentAppAndAppUriHandlers(self, value: Boolean) -> Void: ...
    LimitPickerToCurrentAppAndAppUriHandlers = property(get_LimitPickerToCurrentAppAndAppUriHandlers, put_LimitPickerToCurrentAppAndAppUriHandlers)
class ILauncherStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherStatics'
    _iid_ = Guid('{277151c3-9e3e-42f6-91a4-5dfdeb232451}')
    @winrt_commethod(6)
    def LaunchFileAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFileWithOptionsAsync(self, file: win32more.Windows.Storage.IStorageFile, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def LaunchUriAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def LaunchUriWithOptionsAsync(self, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherStatics2'
    _iid_ = Guid('{59ba2fbb-24cb-4c02-a4c4-8294569d54f1}')
    @winrt_commethod(6)
    def LaunchUriForResultsAsync(self, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_commethod(7)
    def LaunchUriForResultsWithDataAsync(self, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_commethod(8)
    def LaunchUriWithDataAsync(self, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def QueryUriSupportAsync(self, uri: win32more.Windows.Foundation.Uri, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(10)
    def QueryUriSupportWithPackageFamilyNameAsync(self, uri: win32more.Windows.Foundation.Uri, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(11)
    def QueryFileSupportAsync(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(12)
    def QueryFileSupportWithPackageFamilyNameAsync(self, file: win32more.Windows.Storage.StorageFile, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(13)
    def FindUriSchemeHandlersAsync(self, scheme: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(14)
    def FindUriSchemeHandlersWithLaunchUriTypeAsync(self, scheme: WinRT_String, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(15)
    def FindFileHandlersAsync(self, extension: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
class ILauncherStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherStatics3'
    _iid_ = Guid('{234261a8-9db3-4683-aa42-dc6f51d33847}')
    @winrt_commethod(6)
    def LaunchFolderAsync(self, folder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFolderWithOptionsAsync(self, folder: win32more.Windows.Storage.IStorageFolder, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherStatics4'
    _iid_ = Guid('{b9ec819f-b5a5-41c6-b3b3-dd1b3178bcf2}')
    @winrt_commethod(6)
    def QueryAppUriSupportAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(7)
    def QueryAppUriSupportWithPackageFamilyNameAsync(self, uri: win32more.Windows.Foundation.Uri, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(8)
    def FindAppUriHandlersAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(9)
    def LaunchUriForUserAsync(self, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(10)
    def LaunchUriWithOptionsForUserAsync(self, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(11)
    def LaunchUriWithDataForUserAsync(self, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(12)
    def LaunchUriForResultsForUserAsync(self, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_commethod(13)
    def LaunchUriForResultsWithDataForUserAsync(self, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
class ILauncherStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherStatics5'
    _iid_ = Guid('{5b24ef84-d895-5fea-9153-1ac49aed9ba9}')
    @winrt_commethod(6)
    def LaunchFolderPathAsync(self, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFolderPathWithOptionsAsync(self, path: WinRT_String, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def LaunchFolderPathForUserAsync(self, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def LaunchFolderPathWithOptionsForUserAsync(self, user: win32more.Windows.System.User, path: WinRT_String, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherUIOptions'
    _iid_ = Guid('{1b25da6e-8aa6-41e9-8251-4165f5985f49}')
    @winrt_commethod(6)
    def get_InvocationPoint(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_InvocationPoint(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_SelectionRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_SelectionRect(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_commethod(10)
    def get_PreferredPlacement(self) -> win32more.Windows.UI.Popups.Placement: ...
    @winrt_commethod(11)
    def put_PreferredPlacement(self, value: win32more.Windows.UI.Popups.Placement) -> Void: ...
    InvocationPoint = property(get_InvocationPoint, put_InvocationPoint)
    PreferredPlacement = property(get_PreferredPlacement, put_PreferredPlacement)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
class ILauncherViewOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ILauncherViewOptions'
    _iid_ = Guid('{8a9b29f1-7ca7-49de-9bd3-3c5b7184f616}')
    @winrt_commethod(6)
    def get_DesiredRemainingView(self) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_commethod(7)
    def put_DesiredRemainingView(self, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class IMemoryManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IMemoryManagerStatics'
    _iid_ = Guid('{5c6c279c-d7ca-4779-9188-4057219ce64c}')
    @winrt_commethod(6)
    def get_AppMemoryUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_AppMemoryUsageLimit(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_AppMemoryUsageLevel(self) -> win32more.Windows.System.AppMemoryUsageLevel: ...
    @winrt_commethod(9)
    def add_AppMemoryUsageIncreased(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_AppMemoryUsageIncreased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AppMemoryUsageDecreased(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AppMemoryUsageDecreased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_AppMemoryUsageLimitChanging(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.System.AppMemoryUsageLimitChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AppMemoryUsageLimitChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppMemoryUsage = property(get_AppMemoryUsage, None)
    AppMemoryUsageLevel = property(get_AppMemoryUsageLevel, None)
    AppMemoryUsageLimit = property(get_AppMemoryUsageLimit, None)
    AppMemoryUsageIncreased = event()
    AppMemoryUsageDecreased = event()
    AppMemoryUsageLimitChanging = event()
class IMemoryManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IMemoryManagerStatics2'
    _iid_ = Guid('{6eee351f-6d62-423f-9479-b01f9c9f7669}')
    @winrt_commethod(6)
    def GetAppMemoryReport(self) -> win32more.Windows.System.AppMemoryReport: ...
    @winrt_commethod(7)
    def GetProcessMemoryReport(self) -> win32more.Windows.System.ProcessMemoryReport: ...
class IMemoryManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IMemoryManagerStatics3'
    _iid_ = Guid('{149b59ce-92ad-4e35-89eb-50dfb4c0d91c}')
    @winrt_commethod(6)
    def TrySetAppMemoryUsageLimit(self, value: UInt64) -> Boolean: ...
class IMemoryManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IMemoryManagerStatics4'
    _iid_ = Guid('{c5a94828-e84e-4886-8a0d-44b3190e3b72}')
    @winrt_commethod(6)
    def get_ExpectedAppMemoryUsageLimit(self) -> UInt64: ...
    ExpectedAppMemoryUsageLimit = property(get_ExpectedAppMemoryUsageLimit, None)
class IProcessLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IProcessLauncherOptions'
    _iid_ = Guid('{3080b9cf-f444-4a83-beaf-a549a0f3229c}')
    @winrt_commethod(6)
    def get_StandardInput(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(7)
    def put_StandardInput(self, value: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(8)
    def get_StandardOutput(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def put_StandardOutput(self, value: win32more.Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_commethod(10)
    def get_StandardError(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(11)
    def put_StandardError(self, value: win32more.Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_commethod(12)
    def get_WorkingDirectory(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_WorkingDirectory(self, value: WinRT_String) -> Void: ...
    StandardError = property(get_StandardError, put_StandardError)
    StandardInput = property(get_StandardInput, put_StandardInput)
    StandardOutput = property(get_StandardOutput, put_StandardOutput)
    WorkingDirectory = property(get_WorkingDirectory, put_WorkingDirectory)
class IProcessLauncherResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IProcessLauncherResult'
    _iid_ = Guid('{544c8934-86d8-4991-8e75-ece8a43b6b6d}')
    @winrt_commethod(6)
    def get_ExitCode(self) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class IProcessLauncherStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IProcessLauncherStatics'
    _iid_ = Guid('{33ab66e7-2d0e-448b-a6a0-c13c3836d09c}')
    @winrt_commethod(6)
    def RunToCompletionAsync(self, fileName: WinRT_String, args: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.ProcessLauncherResult]: ...
    @winrt_commethod(7)
    def RunToCompletionAsyncWithOptions(self, fileName: WinRT_String, args: WinRT_String, options: win32more.Windows.System.ProcessLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.ProcessLauncherResult]: ...
class IProcessMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IProcessMemoryReport'
    _iid_ = Guid('{087305a8-9b70-4782-8741-3a982b6ce5e4}')
    @winrt_commethod(6)
    def get_PrivateWorkingSetUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_TotalWorkingSetUsage(self) -> UInt64: ...
    PrivateWorkingSetUsage = property(get_PrivateWorkingSetUsage, None)
    TotalWorkingSetUsage = property(get_TotalWorkingSetUsage, None)
class IProtocolForResultsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IProtocolForResultsOperation'
    _iid_ = Guid('{d581293a-6de9-4d28-9378-f86782e182bb}')
    @winrt_commethod(6)
    def ReportCompleted(self, data: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
class IRemoteLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IRemoteLauncherOptions'
    _iid_ = Guid('{9e3a2788-2891-4cdf-a2d6-9dff7d02e693}')
    @winrt_commethod(6)
    def get_FallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_FallbackUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_PreferredAppIds(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    PreferredAppIds = property(get_PreferredAppIds, None)
class IRemoteLauncherStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IRemoteLauncherStatics'
    _iid_ = Guid('{d7db7a93-a30c-48b7-9f21-051026a4e517}')
    @winrt_commethod(6)
    def LaunchUriAsync(self, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_commethod(7)
    def LaunchUriWithOptionsAsync(self, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.RemoteLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_commethod(8)
    def LaunchUriWithDataAsync(self, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.RemoteLauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
class IShutdownManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IShutdownManagerStatics'
    _iid_ = Guid('{72e247ed-dd5b-4d6c-b1d0-c57a7bbb5f94}')
    @winrt_commethod(6)
    def BeginShutdown(self, shutdownKind: win32more.Windows.System.ShutdownKind, timeout: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def CancelShutdown(self) -> Void: ...
class IShutdownManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IShutdownManagerStatics2'
    _iid_ = Guid('{0f69a02f-9c34-43c7-a8c3-70b30a7f7504}')
    @winrt_commethod(6)
    def IsPowerStateSupported(self, powerState: win32more.Windows.System.PowerState) -> Boolean: ...
    @winrt_commethod(7)
    def EnterPowerState(self, powerState: win32more.Windows.System.PowerState) -> Void: ...
    @winrt_commethod(8)
    def EnterPowerStateWithTimeSpan(self, powerState: win32more.Windows.System.PowerState, wakeUpAfter: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class ITimeZoneSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ITimeZoneSettingsStatics'
    _iid_ = Guid('{9b3b2bea-a101-41ae-9fbd-028728bab73d}')
    @winrt_commethod(6)
    def get_CurrentTimeZoneDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedTimeZoneDisplayNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_CanChangeTimeZone(self) -> Boolean: ...
    @winrt_commethod(9)
    def ChangeTimeZoneByDisplayName(self, timeZoneDisplayName: WinRT_String) -> Void: ...
    CanChangeTimeZone = property(get_CanChangeTimeZone, None)
    CurrentTimeZoneDisplayName = property(get_CurrentTimeZoneDisplayName, None)
    SupportedTimeZoneDisplayNames = property(get_SupportedTimeZoneDisplayNames, None)
class ITimeZoneSettingsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ITimeZoneSettingsStatics2'
    _iid_ = Guid('{555c0db8-39a8-49fa-b4f6-a2c7fc2842ec}')
    @winrt_commethod(6)
    def AutoUpdateTimeZoneAsync(self, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AutoUpdateTimeZoneStatus]: ...
class IUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUser'
    _iid_ = Guid('{df9a26c6-e746-4bcd-b5d4-120103c4209b}')
    @winrt_commethod(6)
    def get_NonRoamableId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AuthenticationStatus(self) -> win32more.Windows.System.UserAuthenticationStatus: ...
    @winrt_commethod(8)
    def get_Type(self) -> win32more.Windows.System.UserType: ...
    @winrt_commethod(9)
    def GetPropertyAsync(self, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(10)
    def GetPropertiesAsync(self, values: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_commethod(11)
    def GetPictureAsync(self, desiredSize: win32more.Windows.System.UserPictureSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    AuthenticationStatus = property(get_AuthenticationStatus, None)
    NonRoamableId = property(get_NonRoamableId, None)
    Type = property(get_Type, None)
class IUser2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUser2'
    _iid_ = Guid('{98ba5628-a6e3-518e-89d9-d3b2b1991a10}')
    @winrt_commethod(6)
    def CheckUserAgeConsentGroupAsync(self, consentGroup: win32more.Windows.System.UserAgeConsentGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserAgeConsentResult]: ...
class IUserAuthenticationStatusChangeDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserAuthenticationStatusChangeDeferral'
    _iid_ = Guid('{88b59568-bb30-42fb-a270-e9902e40efa7}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IUserAuthenticationStatusChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserAuthenticationStatusChangingEventArgs'
    _iid_ = Guid('{8c030f28-a711-4c1e-ab48-04179c15938f}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.System.UserAuthenticationStatusChangeDeferral: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(8)
    def get_NewStatus(self) -> win32more.Windows.System.UserAuthenticationStatus: ...
    @winrt_commethod(9)
    def get_CurrentStatus(self) -> win32more.Windows.System.UserAuthenticationStatus: ...
    CurrentStatus = property(get_CurrentStatus, None)
    NewStatus = property(get_NewStatus, None)
    User = property(get_User, None)
class IUserChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserChangedEventArgs'
    _iid_ = Guid('{086459dc-18c6-48db-bc99-724fb9203ccc}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IUserChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserChangedEventArgs2'
    _iid_ = Guid('{6b2ccb44-6f01-560c-97ad-fc7f32ec581f}')
    @winrt_commethod(6)
    def get_ChangedPropertyKinds(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.UserWatcherUpdateKind]: ...
    ChangedPropertyKinds = property(get_ChangedPropertyKinds, None)
class IUserDeviceAssociationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserDeviceAssociationChangedEventArgs'
    _iid_ = Guid('{bd1f6f6c-bb5d-4d7b-a5f0-c8cd11a38d42}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_NewUser(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(8)
    def get_OldUser(self) -> win32more.Windows.System.User: ...
    DeviceId = property(get_DeviceId, None)
    NewUser = property(get_NewUser, None)
    OldUser = property(get_OldUser, None)
class IUserDeviceAssociationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserDeviceAssociationStatics'
    _iid_ = Guid('{7e491e14-f85a-4c07-8da9-7fe3d0542343}')
    @winrt_commethod(6)
    def FindUserFromDeviceId(self, deviceId: WinRT_String) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def add_UserDeviceAssociationChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.System.UserDeviceAssociationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_UserDeviceAssociationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    UserDeviceAssociationChanged = event()
class IUserPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserPicker'
    _iid_ = Guid('{7d548008-f1e3-4a6c-8ddc-a9bb0f488aed}')
    @winrt_commethod(6)
    def get_AllowGuestAccounts(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowGuestAccounts(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SuggestedSelectedUser(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(9)
    def put_SuggestedSelectedUser(self, value: win32more.Windows.System.User) -> Void: ...
    @winrt_commethod(10)
    def PickSingleUserAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.User]: ...
    AllowGuestAccounts = property(get_AllowGuestAccounts, put_AllowGuestAccounts)
    SuggestedSelectedUser = property(get_SuggestedSelectedUser, put_SuggestedSelectedUser)
class IUserPickerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserPickerStatics'
    _iid_ = Guid('{de3290dc-7e73-4df6-a1ae-4d7eca82b40d}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IUserStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserStatics'
    _iid_ = Guid('{155eb23b-242a-45e0-a2e9-3171fc6a7fdd}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.System.UserWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_commethod(8)
    def FindAllAsyncByType(self, type: win32more.Windows.System.UserType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_commethod(9)
    def FindAllAsyncByTypeAndStatus(self, type: win32more.Windows.System.UserType, status: win32more.Windows.System.UserAuthenticationStatus) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_commethod(10)
    def GetFromId(self, nonRoamableId: WinRT_String) -> win32more.Windows.System.User: ...
class IUserStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserStatics2'
    _iid_ = Guid('{74a37e11-2eb5-4487-b0d5-2c6790e013e9}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.User: ...
class IUserWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.IUserWatcher'
    _iid_ = Guid('{155eb23b-242a-45e0-a2e9-3171fc6a7fbb}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.System.UserWatcherStatus: ...
    @winrt_commethod(7)
    def Start(self) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_AuthenticationStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AuthenticationStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_AuthenticationStatusChanging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserAuthenticationStatusChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_AuthenticationStatusChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    Updated = event()
    AuthenticationStatusChanged = event()
    AuthenticationStatusChanging = event()
    EnumerationCompleted = event()
    Stopped = event()
class _KnownUserProperties_Meta_(ComPtr.__class__):
    pass
class KnownUserProperties(ComPtr, metaclass=_KnownUserProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.KnownUserProperties'
    @winrt_classmethod
    def get_AgeEnforcementRegion(cls: win32more.Windows.System.IKnownUserPropertiesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FirstName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_LastName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProviderName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AccountName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GuestHost(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrincipalName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DomainName(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SessionInitiationProtocolUri(cls: win32more.Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    _KnownUserProperties_Meta_.AccountName = property(get_AccountName, None)
    _KnownUserProperties_Meta_.AgeEnforcementRegion = property(get_AgeEnforcementRegion, None)
    _KnownUserProperties_Meta_.DisplayName = property(get_DisplayName, None)
    _KnownUserProperties_Meta_.DomainName = property(get_DomainName, None)
    _KnownUserProperties_Meta_.FirstName = property(get_FirstName, None)
    _KnownUserProperties_Meta_.GuestHost = property(get_GuestHost, None)
    _KnownUserProperties_Meta_.LastName = property(get_LastName, None)
    _KnownUserProperties_Meta_.PrincipalName = property(get_PrincipalName, None)
    _KnownUserProperties_Meta_.ProviderName = property(get_ProviderName, None)
    _KnownUserProperties_Meta_.SessionInitiationProtocolUri = property(get_SessionInitiationProtocolUri, None)
class LaunchFileStatus(Enum, Int32):
    Success = 0
    AppUnavailable = 1
    DeniedByPolicy = 2
    FileTypeNotSupported = 3
    Unknown = 4
class LaunchQuerySupportStatus(Enum, Int32):
    Available = 0
    AppNotInstalled = 1
    AppUnavailable = 2
    NotSupported = 3
    Unknown = 4
class LaunchQuerySupportType(Enum, Int32):
    Uri = 0
    UriForResults = 1
class LaunchUriResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.ILaunchUriResult
    _classid_ = 'Windows.System.LaunchUriResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.ILaunchUriResult) -> win32more.Windows.System.LaunchUriStatus: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.System.ILaunchUriResult) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Result = property(get_Result, None)
    Status = property(get_Status, None)
class LaunchUriStatus(Enum, Int32):
    Success = 0
    AppUnavailable = 1
    ProtocolUnavailable = 2
    Unknown = 3
class Launcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Launcher'
    @winrt_classmethod
    def LaunchFolderPathAsync(cls: win32more.Windows.System.ILauncherStatics5, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathWithOptionsAsync(cls: win32more.Windows.System.ILauncherStatics5, path: WinRT_String, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathForUserAsync(cls: win32more.Windows.System.ILauncherStatics5, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathWithOptionsForUserAsync(cls: win32more.Windows.System.ILauncherStatics5, user: win32more.Windows.System.User, path: WinRT_String, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def QueryAppUriSupportAsync(cls: win32more.Windows.System.ILauncherStatics4, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryAppUriSupportWithPackageFamilyNameAsync(cls: win32more.Windows.System.ILauncherStatics4, uri: win32more.Windows.Foundation.Uri, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def FindAppUriHandlersAsync(cls: win32more.Windows.System.ILauncherStatics4, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def LaunchUriForUserAsync(cls: win32more.Windows.System.ILauncherStatics4, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsForUserAsync(cls: win32more.Windows.System.ILauncherStatics4, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithDataForUserAsync(cls: win32more.Windows.System.ILauncherStatics4, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriForResultsForUserAsync(cls: win32more.Windows.System.ILauncherStatics4, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriForResultsWithDataForUserAsync(cls: win32more.Windows.System.ILauncherStatics4, user: win32more.Windows.System.User, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchFileAsync(cls: win32more.Windows.System.ILauncherStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFileWithOptionsAsync(cls: win32more.Windows.System.ILauncherStatics, file: win32more.Windows.Storage.IStorageFile, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriAsync(cls: win32more.Windows.System.ILauncherStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsAsync(cls: win32more.Windows.System.ILauncherStatics, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderAsync(cls: win32more.Windows.System.ILauncherStatics3, folder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderWithOptionsAsync(cls: win32more.Windows.System.ILauncherStatics3, folder: win32more.Windows.Storage.IStorageFolder, options: win32more.Windows.System.FolderLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriForResultsAsync(cls: win32more.Windows.System.ILauncherStatics2, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriForResultsWithDataAsync(cls: win32more.Windows.System.ILauncherStatics2, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriWithDataAsync(cls: win32more.Windows.System.ILauncherStatics2, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.LauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def QueryUriSupportAsync(cls: win32more.Windows.System.ILauncherStatics2, uri: win32more.Windows.Foundation.Uri, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryUriSupportWithPackageFamilyNameAsync(cls: win32more.Windows.System.ILauncherStatics2, uri: win32more.Windows.Foundation.Uri, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryFileSupportAsync(cls: win32more.Windows.System.ILauncherStatics2, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryFileSupportWithPackageFamilyNameAsync(cls: win32more.Windows.System.ILauncherStatics2, file: win32more.Windows.Storage.StorageFile, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def FindUriSchemeHandlersAsync(cls: win32more.Windows.System.ILauncherStatics2, scheme: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def FindUriSchemeHandlersWithLaunchUriTypeAsync(cls: win32more.Windows.System.ILauncherStatics2, scheme: WinRT_String, launchQuerySupportType: win32more.Windows.System.LaunchQuerySupportType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def FindFileHandlersAsync(cls: win32more.Windows.System.ILauncherStatics2, extension: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.AppInfo]]: ...
class LauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.ILauncherOptions
    _classid_ = 'Windows.System.LauncherOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.LauncherOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.LauncherOptions: ...
    @winrt_mixinmethod
    def get_TargetApplicationPackageFamilyName(self: win32more.Windows.System.ILauncherOptions2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetApplicationPackageFamilyName(self: win32more.Windows.System.ILauncherOptions2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: win32more.Windows.System.ILauncherOptions2) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def put_NeighboringFilesQuery(self: win32more.Windows.System.ILauncherOptions2, value: win32more.Windows.Storage.Search.StorageFileQueryResult) -> Void: ...
    @winrt_mixinmethod
    def get_TreatAsUntrusted(self: win32more.Windows.System.ILauncherOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_TreatAsUntrusted(self: win32more.Windows.System.ILauncherOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayApplicationPicker(self: win32more.Windows.System.ILauncherOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayApplicationPicker(self: win32more.Windows.System.ILauncherOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_UI(self: win32more.Windows.System.ILauncherOptions) -> win32more.Windows.System.LauncherUIOptions: ...
    @winrt_mixinmethod
    def get_PreferredApplicationPackageFamilyName(self: win32more.Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreferredApplicationPackageFamilyName(self: win32more.Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredApplicationDisplayName(self: win32more.Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreferredApplicationDisplayName(self: win32more.Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: win32more.Windows.System.ILauncherOptions) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: win32more.Windows.System.ILauncherOptions, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentType(self: win32more.Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreAppUriHandlers(self: win32more.Windows.System.ILauncherOptions3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreAppUriHandlers(self: win32more.Windows.System.ILauncherOptions3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LimitPickerToCurrentAppAndAppUriHandlers(self: win32more.Windows.System.ILauncherOptions4) -> Boolean: ...
    @winrt_mixinmethod
    def put_LimitPickerToCurrentAppAndAppUriHandlers(self: win32more.Windows.System.ILauncherOptions4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRemainingView(self: win32more.Windows.System.ILauncherViewOptions) -> win32more.Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_DesiredRemainingView(self: win32more.Windows.System.ILauncherViewOptions, value: win32more.Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    ContentType = property(get_ContentType, put_ContentType)
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
    DisplayApplicationPicker = property(get_DisplayApplicationPicker, put_DisplayApplicationPicker)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    IgnoreAppUriHandlers = property(get_IgnoreAppUriHandlers, put_IgnoreAppUriHandlers)
    LimitPickerToCurrentAppAndAppUriHandlers = property(get_LimitPickerToCurrentAppAndAppUriHandlers, put_LimitPickerToCurrentAppAndAppUriHandlers)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, put_NeighboringFilesQuery)
    PreferredApplicationDisplayName = property(get_PreferredApplicationDisplayName, put_PreferredApplicationDisplayName)
    PreferredApplicationPackageFamilyName = property(get_PreferredApplicationPackageFamilyName, put_PreferredApplicationPackageFamilyName)
    TargetApplicationPackageFamilyName = property(get_TargetApplicationPackageFamilyName, put_TargetApplicationPackageFamilyName)
    TreatAsUntrusted = property(get_TreatAsUntrusted, put_TreatAsUntrusted)
    UI = property(get_UI, None)
class LauncherUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.ILauncherUIOptions
    _classid_ = 'Windows.System.LauncherUIOptions'
    @winrt_mixinmethod
    def get_InvocationPoint(self: win32more.Windows.System.ILauncherUIOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_InvocationPoint(self: win32more.Windows.System.ILauncherUIOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionRect(self: win32more.Windows.System.ILauncherUIOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_SelectionRect(self: win32more.Windows.System.ILauncherUIOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredPlacement(self: win32more.Windows.System.ILauncherUIOptions) -> win32more.Windows.UI.Popups.Placement: ...
    @winrt_mixinmethod
    def put_PreferredPlacement(self: win32more.Windows.System.ILauncherUIOptions, value: win32more.Windows.UI.Popups.Placement) -> Void: ...
    InvocationPoint = property(get_InvocationPoint, put_InvocationPoint)
    PreferredPlacement = property(get_PreferredPlacement, put_PreferredPlacement)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
class _MemoryManager_Meta_(ComPtr.__class__):
    pass
class MemoryManager(ComPtr, metaclass=_MemoryManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.MemoryManager'
    @winrt_classmethod
    def get_ExpectedAppMemoryUsageLimit(cls: win32more.Windows.System.IMemoryManagerStatics4) -> UInt64: ...
    @winrt_classmethod
    def TrySetAppMemoryUsageLimit(cls: win32more.Windows.System.IMemoryManagerStatics3, value: UInt64) -> Boolean: ...
    @winrt_classmethod
    def GetAppMemoryReport(cls: win32more.Windows.System.IMemoryManagerStatics2) -> win32more.Windows.System.AppMemoryReport: ...
    @winrt_classmethod
    def GetProcessMemoryReport(cls: win32more.Windows.System.IMemoryManagerStatics2) -> win32more.Windows.System.ProcessMemoryReport: ...
    @winrt_classmethod
    def get_AppMemoryUsage(cls: win32more.Windows.System.IMemoryManagerStatics) -> UInt64: ...
    @winrt_classmethod
    def get_AppMemoryUsageLimit(cls: win32more.Windows.System.IMemoryManagerStatics) -> UInt64: ...
    @winrt_classmethod
    def get_AppMemoryUsageLevel(cls: win32more.Windows.System.IMemoryManagerStatics) -> win32more.Windows.System.AppMemoryUsageLevel: ...
    @winrt_classmethod
    def add_AppMemoryUsageIncreased(cls: win32more.Windows.System.IMemoryManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageIncreased(cls: win32more.Windows.System.IMemoryManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_AppMemoryUsageDecreased(cls: win32more.Windows.System.IMemoryManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageDecreased(cls: win32more.Windows.System.IMemoryManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_AppMemoryUsageLimitChanging(cls: win32more.Windows.System.IMemoryManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.System.AppMemoryUsageLimitChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageLimitChanging(cls: win32more.Windows.System.IMemoryManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _MemoryManager_Meta_.AppMemoryUsage = property(get_AppMemoryUsage, None)
    _MemoryManager_Meta_.AppMemoryUsageLevel = property(get_AppMemoryUsageLevel, None)
    _MemoryManager_Meta_.AppMemoryUsageLimit = property(get_AppMemoryUsageLimit, None)
    _MemoryManager_Meta_.ExpectedAppMemoryUsageLimit = property(get_ExpectedAppMemoryUsageLimit, None)
class PowerState(Enum, Int32):
    ConnectedStandby = 0
    SleepS3 = 1
class ProcessLauncher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ProcessLauncher'
    @winrt_classmethod
    def RunToCompletionAsync(cls: win32more.Windows.System.IProcessLauncherStatics, fileName: WinRT_String, args: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.ProcessLauncherResult]: ...
    @winrt_classmethod
    def RunToCompletionAsyncWithOptions(cls: win32more.Windows.System.IProcessLauncherStatics, fileName: WinRT_String, args: WinRT_String, options: win32more.Windows.System.ProcessLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.ProcessLauncherResult]: ...
class ProcessLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IProcessLauncherOptions
    _classid_ = 'Windows.System.ProcessLauncherOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.ProcessLauncherOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.ProcessLauncherOptions: ...
    @winrt_mixinmethod
    def get_StandardInput(self: win32more.Windows.System.IProcessLauncherOptions) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def put_StandardInput(self: win32more.Windows.System.IProcessLauncherOptions, value: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def get_StandardOutput(self: win32more.Windows.System.IProcessLauncherOptions) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def put_StandardOutput(self: win32more.Windows.System.IProcessLauncherOptions, value: win32more.Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_mixinmethod
    def get_StandardError(self: win32more.Windows.System.IProcessLauncherOptions) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def put_StandardError(self: win32more.Windows.System.IProcessLauncherOptions, value: win32more.Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_mixinmethod
    def get_WorkingDirectory(self: win32more.Windows.System.IProcessLauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_WorkingDirectory(self: win32more.Windows.System.IProcessLauncherOptions, value: WinRT_String) -> Void: ...
    StandardError = property(get_StandardError, put_StandardError)
    StandardInput = property(get_StandardInput, put_StandardInput)
    StandardOutput = property(get_StandardOutput, put_StandardOutput)
    WorkingDirectory = property(get_WorkingDirectory, put_WorkingDirectory)
class ProcessLauncherResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IProcessLauncherResult
    _classid_ = 'Windows.System.ProcessLauncherResult'
    @winrt_mixinmethod
    def get_ExitCode(self: win32more.Windows.System.IProcessLauncherResult) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class ProcessMemoryReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IProcessMemoryReport
    _classid_ = 'Windows.System.ProcessMemoryReport'
    @winrt_mixinmethod
    def get_PrivateWorkingSetUsage(self: win32more.Windows.System.IProcessMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalWorkingSetUsage(self: win32more.Windows.System.IProcessMemoryReport) -> UInt64: ...
    PrivateWorkingSetUsage = property(get_PrivateWorkingSetUsage, None)
    TotalWorkingSetUsage = property(get_TotalWorkingSetUsage, None)
class ProcessorArchitecture(Enum, Int32):
    X86 = 0
    Arm = 5
    X64 = 9
    Neutral = 11
    Arm64 = 12
    X86OnArm64 = 14
    Unknown = 65535
class ProtocolForResultsOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IProtocolForResultsOperation
    _classid_ = 'Windows.System.ProtocolForResultsOperation'
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.System.IProtocolForResultsOperation, data: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
class RemoteLaunchUriStatus(Enum, Int32):
    Unknown = 0
    Success = 1
    AppUnavailable = 2
    ProtocolUnavailable = 3
    RemoteSystemUnavailable = 4
    ValueSetTooLarge = 5
    DeniedByLocalSystem = 6
    DeniedByRemoteSystem = 7
class RemoteLauncher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteLauncher'
    @winrt_classmethod
    def LaunchUriAsync(cls: win32more.Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsAsync(cls: win32more.Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.RemoteLauncherOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithDataAsync(cls: win32more.Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: win32more.Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: win32more.Windows.Foundation.Uri, options: win32more.Windows.System.RemoteLauncherOptions, inputData: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.RemoteLaunchUriStatus]: ...
class RemoteLauncherOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IRemoteLauncherOptions
    _classid_ = 'Windows.System.RemoteLauncherOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.RemoteLauncherOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.RemoteLauncherOptions: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: win32more.Windows.System.IRemoteLauncherOptions) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: win32more.Windows.System.IRemoteLauncherOptions, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredAppIds(self: win32more.Windows.System.IRemoteLauncherOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    PreferredAppIds = property(get_PreferredAppIds, None)
class ShutdownKind(Enum, Int32):
    Shutdown = 0
    Restart = 1
class ShutdownManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.ShutdownManager'
    @winrt_classmethod
    def IsPowerStateSupported(cls: win32more.Windows.System.IShutdownManagerStatics2, powerState: win32more.Windows.System.PowerState) -> Boolean: ...
    @winrt_classmethod
    def EnterPowerState(cls: win32more.Windows.System.IShutdownManagerStatics2, powerState: win32more.Windows.System.PowerState) -> Void: ...
    @winrt_classmethod
    def EnterPowerStateWithTimeSpan(cls: win32more.Windows.System.IShutdownManagerStatics2, powerState: win32more.Windows.System.PowerState, wakeUpAfter: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def BeginShutdown(cls: win32more.Windows.System.IShutdownManagerStatics, shutdownKind: win32more.Windows.System.ShutdownKind, timeout: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def CancelShutdown(cls: win32more.Windows.System.IShutdownManagerStatics) -> Void: ...
SystemManagementContract: UInt32 = 458752
class _TimeZoneSettings_Meta_(ComPtr.__class__):
    pass
class TimeZoneSettings(ComPtr, metaclass=_TimeZoneSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.TimeZoneSettings'
    @winrt_classmethod
    def AutoUpdateTimeZoneAsync(cls: win32more.Windows.System.ITimeZoneSettingsStatics2, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.AutoUpdateTimeZoneStatus]: ...
    @winrt_classmethod
    def get_CurrentTimeZoneDisplayName(cls: win32more.Windows.System.ITimeZoneSettingsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SupportedTimeZoneDisplayNames(cls: win32more.Windows.System.ITimeZoneSettingsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_CanChangeTimeZone(cls: win32more.Windows.System.ITimeZoneSettingsStatics) -> Boolean: ...
    @winrt_classmethod
    def ChangeTimeZoneByDisplayName(cls: win32more.Windows.System.ITimeZoneSettingsStatics, timeZoneDisplayName: WinRT_String) -> Void: ...
    _TimeZoneSettings_Meta_.CanChangeTimeZone = property(get_CanChangeTimeZone, None)
    _TimeZoneSettings_Meta_.CurrentTimeZoneDisplayName = property(get_CurrentTimeZoneDisplayName, None)
    _TimeZoneSettings_Meta_.SupportedTimeZoneDisplayNames = property(get_SupportedTimeZoneDisplayNames, None)
class User(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUser
    _classid_ = 'Windows.System.User'
    @winrt_mixinmethod
    def get_NonRoamableId(self: win32more.Windows.System.IUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AuthenticationStatus(self: win32more.Windows.System.IUser) -> win32more.Windows.System.UserAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.System.IUser) -> win32more.Windows.System.UserType: ...
    @winrt_mixinmethod
    def GetPropertyAsync(self: win32more.Windows.System.IUser, value: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.System.IUser, values: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_mixinmethod
    def GetPictureAsync(self: win32more.Windows.System.IUser, desiredSize: win32more.Windows.System.UserPictureSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def CheckUserAgeConsentGroupAsync(self: win32more.Windows.System.IUser2, consentGroup: win32more.Windows.System.UserAgeConsentGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserAgeConsentResult]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.System.IUserStatics2) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.System.IUserStatics) -> win32more.Windows.System.UserWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.System.IUserStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_classmethod
    def FindAllAsyncByType(cls: win32more.Windows.System.IUserStatics, type: win32more.Windows.System.UserType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_classmethod
    def FindAllAsyncByTypeAndStatus(cls: win32more.Windows.System.IUserStatics, type: win32more.Windows.System.UserType, status: win32more.Windows.System.UserAuthenticationStatus) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.User]]: ...
    @winrt_classmethod
    def GetFromId(cls: win32more.Windows.System.IUserStatics, nonRoamableId: WinRT_String) -> win32more.Windows.System.User: ...
    AuthenticationStatus = property(get_AuthenticationStatus, None)
    NonRoamableId = property(get_NonRoamableId, None)
    Type = property(get_Type, None)
class UserAgeConsentGroup(Enum, Int32):
    Child = 0
    Minor = 1
    Adult = 2
class UserAgeConsentResult(Enum, Int32):
    NotEnforced = 0
    Included = 1
    NotIncluded = 2
    Unknown = 3
    Ambiguous = 4
class UserAuthenticationStatus(Enum, Int32):
    Unauthenticated = 0
    LocallyAuthenticated = 1
    RemotelyAuthenticated = 2
class UserAuthenticationStatusChangeDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserAuthenticationStatusChangeDeferral
    _classid_ = 'Windows.System.UserAuthenticationStatusChangeDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.System.IUserAuthenticationStatusChangeDeferral) -> Void: ...
class UserAuthenticationStatusChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserAuthenticationStatusChangingEventArgs
    _classid_ = 'Windows.System.UserAuthenticationStatusChangingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.System.IUserAuthenticationStatusChangingEventArgs) -> win32more.Windows.System.UserAuthenticationStatusChangeDeferral: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.IUserAuthenticationStatusChangingEventArgs) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_NewStatus(self: win32more.Windows.System.IUserAuthenticationStatusChangingEventArgs) -> win32more.Windows.System.UserAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_CurrentStatus(self: win32more.Windows.System.IUserAuthenticationStatusChangingEventArgs) -> win32more.Windows.System.UserAuthenticationStatus: ...
    CurrentStatus = property(get_CurrentStatus, None)
    NewStatus = property(get_NewStatus, None)
    User = property(get_User, None)
class UserChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserChangedEventArgs
    _classid_ = 'Windows.System.UserChangedEventArgs'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.IUserChangedEventArgs) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ChangedPropertyKinds(self: win32more.Windows.System.IUserChangedEventArgs2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.UserWatcherUpdateKind]: ...
    ChangedPropertyKinds = property(get_ChangedPropertyKinds, None)
    User = property(get_User, None)
class UserDeviceAssociation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserDeviceAssociation'
    @winrt_classmethod
    def FindUserFromDeviceId(cls: win32more.Windows.System.IUserDeviceAssociationStatics, deviceId: WinRT_String) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def add_UserDeviceAssociationChanged(cls: win32more.Windows.System.IUserDeviceAssociationStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.System.UserDeviceAssociationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UserDeviceAssociationChanged(cls: win32more.Windows.System.IUserDeviceAssociationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class UserDeviceAssociationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserDeviceAssociationChangedEventArgs
    _classid_ = 'Windows.System.UserDeviceAssociationChangedEventArgs'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.System.IUserDeviceAssociationChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewUser(self: win32more.Windows.System.IUserDeviceAssociationChangedEventArgs) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_OldUser(self: win32more.Windows.System.IUserDeviceAssociationChangedEventArgs) -> win32more.Windows.System.User: ...
    DeviceId = property(get_DeviceId, None)
    NewUser = property(get_NewUser, None)
    OldUser = property(get_OldUser, None)
class UserPicker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserPicker
    _classid_ = 'Windows.System.UserPicker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.UserPicker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.UserPicker: ...
    @winrt_mixinmethod
    def get_AllowGuestAccounts(self: win32more.Windows.System.IUserPicker) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowGuestAccounts(self: win32more.Windows.System.IUserPicker, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedSelectedUser(self: win32more.Windows.System.IUserPicker) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def put_SuggestedSelectedUser(self: win32more.Windows.System.IUserPicker, value: win32more.Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def PickSingleUserAsync(self: win32more.Windows.System.IUserPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.User]: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.System.IUserPickerStatics) -> Boolean: ...
    AllowGuestAccounts = property(get_AllowGuestAccounts, put_AllowGuestAccounts)
    SuggestedSelectedUser = property(get_SuggestedSelectedUser, put_SuggestedSelectedUser)
class UserPictureSize(Enum, Int32):
    Size64x64 = 0
    Size208x208 = 1
    Size424x424 = 2
    Size1080x1080 = 3
class UserType(Enum, Int32):
    LocalUser = 0
    RemoteUser = 1
    LocalGuest = 2
    RemoteGuest = 3
    SystemManaged = 4
class UserWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.IUserWatcher
    _classid_ = 'Windows.System.UserWatcher'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.IUserWatcher) -> win32more.Windows.System.UserWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.IUserWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.IUserWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationStatusChanged(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationStatusChanged(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationStatusChanging(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.System.UserAuthenticationStatusChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationStatusChanging(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.System.IUserWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.UserWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.System.IUserWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    Added = event()
    Removed = event()
    Updated = event()
    AuthenticationStatusChanged = event()
    AuthenticationStatusChanging = event()
    EnumerationCompleted = event()
    Stopped = event()
class UserWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    EnumerationCompleted = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class UserWatcherUpdateKind(Enum, Int32):
    Properties = 0
    Picture = 1
class VirtualKey(Enum, Int32):
    None_ = 0
    LeftButton = 1
    RightButton = 2
    Cancel = 3
    MiddleButton = 4
    XButton1 = 5
    XButton2 = 6
    Back = 8
    Tab = 9
    Clear = 12
    Enter = 13
    Shift = 16
    Control = 17
    Menu = 18
    Pause = 19
    CapitalLock = 20
    Kana = 21
    Hangul = 21
    ImeOn = 22
    Junja = 23
    Final = 24
    Hanja = 25
    Kanji = 25
    ImeOff = 26
    Escape = 27
    Convert = 28
    NonConvert = 29
    Accept = 30
    ModeChange = 31
    Space = 32
    PageUp = 33
    PageDown = 34
    End = 35
    Home = 36
    Left = 37
    Up = 38
    Right = 39
    Down = 40
    Select = 41
    Print = 42
    Execute = 43
    Snapshot = 44
    Insert = 45
    Delete = 46
    Help = 47
    Number0 = 48
    Number1 = 49
    Number2 = 50
    Number3 = 51
    Number4 = 52
    Number5 = 53
    Number6 = 54
    Number7 = 55
    Number8 = 56
    Number9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    LeftWindows = 91
    RightWindows = 92
    Application = 93
    Sleep = 95
    NumberPad0 = 96
    NumberPad1 = 97
    NumberPad2 = 98
    NumberPad3 = 99
    NumberPad4 = 100
    NumberPad5 = 101
    NumberPad6 = 102
    NumberPad7 = 103
    NumberPad8 = 104
    NumberPad9 = 105
    Multiply = 106
    Add = 107
    Separator = 108
    Subtract = 109
    Decimal = 110
    Divide = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    NavigationView = 136
    NavigationMenu = 137
    NavigationUp = 138
    NavigationDown = 139
    NavigationLeft = 140
    NavigationRight = 141
    NavigationAccept = 142
    NavigationCancel = 143
    NumberKeyLock = 144
    Scroll = 145
    LeftShift = 160
    RightShift = 161
    LeftControl = 162
    RightControl = 163
    LeftMenu = 164
    RightMenu = 165
    GoBack = 166
    GoForward = 167
    Refresh = 168
    Stop = 169
    Search = 170
    Favorites = 171
    GoHome = 172
    GamepadA = 195
    GamepadB = 196
    GamepadX = 197
    GamepadY = 198
    GamepadRightShoulder = 199
    GamepadLeftShoulder = 200
    GamepadLeftTrigger = 201
    GamepadRightTrigger = 202
    GamepadDPadUp = 203
    GamepadDPadDown = 204
    GamepadDPadLeft = 205
    GamepadDPadRight = 206
    GamepadMenu = 207
    GamepadView = 208
    GamepadLeftThumbstickButton = 209
    GamepadRightThumbstickButton = 210
    GamepadLeftThumbstickUp = 211
    GamepadLeftThumbstickDown = 212
    GamepadLeftThumbstickRight = 213
    GamepadLeftThumbstickLeft = 214
    GamepadRightThumbstickUp = 215
    GamepadRightThumbstickDown = 216
    GamepadRightThumbstickRight = 217
    GamepadRightThumbstickLeft = 218
class VirtualKeyModifiers(Enum, UInt32):
    None_ = 0
    Control = 1
    Menu = 2
    Shift = 4
    Windows = 8


make_ready(__name__)
