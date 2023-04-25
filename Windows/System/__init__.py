from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.Search
import Windows.Storage.Streams
import Windows.System
import Windows.System.Diagnostics
import Windows.System.RemoteSystems
import Windows.UI.Popups
import Windows.UI.ViewManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppActivationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppActivationResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.System.IAppActivationResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: Windows.System.IAppActivationResult) -> Windows.System.AppResourceGroupInfo: ...
    ExtendedError = property(get_ExtendedError, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class AppDiagnosticInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppDiagnosticInfo'
    @winrt_mixinmethod
    def get_AppInfo(self: Windows.System.IAppDiagnosticInfo) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def GetResourceGroups(self: Windows.System.IAppDiagnosticInfo2) -> Windows.Foundation.Collections.IVector[Windows.System.AppResourceGroupInfo]: ...
    @winrt_mixinmethod
    def CreateResourceGroupWatcher(self: Windows.System.IAppDiagnosticInfo2) -> Windows.System.AppResourceGroupInfoWatcher: ...
    @winrt_mixinmethod
    def LaunchAsync(self: Windows.System.IAppDiagnosticInfo3) -> Windows.Foundation.IAsyncOperation[Windows.System.AppActivationResult]: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.IAppDiagnosticInfoStatics2) -> Windows.System.AppDiagnosticInfoWatcher: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.System.IAppDiagnosticInfoStatics2) -> Windows.Foundation.IAsyncOperation[Windows.System.DiagnosticAccessStatus]: ...
    @winrt_classmethod
    def RequestInfoForPackageAsync(cls: Windows.System.IAppDiagnosticInfoStatics2, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoForAppAsync(cls: Windows.System.IAppDiagnosticInfoStatics2) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoForAppUserModelId(cls: Windows.System.IAppDiagnosticInfoStatics2, appUserModelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    @winrt_classmethod
    def RequestInfoAsync(cls: Windows.System.IAppDiagnosticInfoStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    AppInfo = property(get_AppInfo, None)
class AppDiagnosticInfoWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppDiagnosticInfoWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.System.IAppDiagnosticInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.System.IAppDiagnosticInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.System.IAppDiagnosticInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.System.IAppDiagnosticInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.System.IAppDiagnosticInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.System.IAppDiagnosticInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.System.IAppDiagnosticInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.System.IAppDiagnosticInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.System.IAppDiagnosticInfoWatcher) -> Windows.System.AppDiagnosticInfoWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.System.IAppDiagnosticInfoWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.IAppDiagnosticInfoWatcher) -> Void: ...
    Status = property(get_Status, None)
class AppDiagnosticInfoWatcherEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppDiagnosticInfoWatcherEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfo(self: Windows.System.IAppDiagnosticInfoWatcherEventArgs) -> Windows.System.AppDiagnosticInfo: ...
    AppDiagnosticInfo = property(get_AppDiagnosticInfo, None)
AppDiagnosticInfoWatcherStatus = Int32
AppDiagnosticInfoWatcherStatus_Created: AppDiagnosticInfoWatcherStatus = 0
AppDiagnosticInfoWatcherStatus_Started: AppDiagnosticInfoWatcherStatus = 1
AppDiagnosticInfoWatcherStatus_EnumerationCompleted: AppDiagnosticInfoWatcherStatus = 2
AppDiagnosticInfoWatcherStatus_Stopping: AppDiagnosticInfoWatcherStatus = 3
AppDiagnosticInfoWatcherStatus_Stopped: AppDiagnosticInfoWatcherStatus = 4
AppDiagnosticInfoWatcherStatus_Aborted: AppDiagnosticInfoWatcherStatus = 5
class AppExecutionStateChangeResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppExecutionStateChangeResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.System.IAppExecutionStateChangeResult) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class AppMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppMemoryReport'
    @winrt_mixinmethod
    def get_PrivateCommitUsage(self: Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakPrivateCommitUsage(self: Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitUsage(self: Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitLimit(self: Windows.System.IAppMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_ExpectedTotalCommitLimit(self: Windows.System.IAppMemoryReport2) -> UInt64: ...
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    PeakPrivateCommitUsage = property(get_PeakPrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
    TotalCommitLimit = property(get_TotalCommitLimit, None)
    ExpectedTotalCommitLimit = property(get_ExpectedTotalCommitLimit, None)
AppMemoryUsageLevel = Int32
AppMemoryUsageLevel_Low: AppMemoryUsageLevel = 0
AppMemoryUsageLevel_Medium: AppMemoryUsageLevel = 1
AppMemoryUsageLevel_High: AppMemoryUsageLevel = 2
AppMemoryUsageLevel_OverLimit: AppMemoryUsageLevel = 3
class AppMemoryUsageLimitChangingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppMemoryUsageLimitChangingEventArgs'
    @winrt_mixinmethod
    def get_OldLimit(self: Windows.System.IAppMemoryUsageLimitChangingEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_NewLimit(self: Windows.System.IAppMemoryUsageLimitChangingEventArgs) -> UInt64: ...
    OldLimit = property(get_OldLimit, None)
    NewLimit = property(get_NewLimit, None)
class AppResourceGroupBackgroundTaskReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupBackgroundTaskReport'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.System.IAppResourceGroupBackgroundTaskReport) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Trigger(self: Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EntryPoint(self: Windows.System.IAppResourceGroupBackgroundTaskReport) -> WinRT_String: ...
    TaskId = property(get_TaskId, None)
    Name = property(get_Name, None)
    Trigger = property(get_Trigger, None)
    EntryPoint = property(get_EntryPoint, None)
AppResourceGroupEnergyQuotaState = Int32
AppResourceGroupEnergyQuotaState_Unknown: AppResourceGroupEnergyQuotaState = 0
AppResourceGroupEnergyQuotaState_Over: AppResourceGroupEnergyQuotaState = 1
AppResourceGroupEnergyQuotaState_Under: AppResourceGroupEnergyQuotaState = 2
AppResourceGroupExecutionState = Int32
AppResourceGroupExecutionState_Unknown: AppResourceGroupExecutionState = 0
AppResourceGroupExecutionState_Running: AppResourceGroupExecutionState = 1
AppResourceGroupExecutionState_Suspending: AppResourceGroupExecutionState = 2
AppResourceGroupExecutionState_Suspended: AppResourceGroupExecutionState = 3
AppResourceGroupExecutionState_NotRunning: AppResourceGroupExecutionState = 4
class AppResourceGroupInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupInfo'
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.System.IAppResourceGroupInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_IsShared(self: Windows.System.IAppResourceGroupInfo) -> Boolean: ...
    @winrt_mixinmethod
    def GetBackgroundTaskReports(self: Windows.System.IAppResourceGroupInfo) -> Windows.Foundation.Collections.IVector[Windows.System.AppResourceGroupBackgroundTaskReport]: ...
    @winrt_mixinmethod
    def GetMemoryReport(self: Windows.System.IAppResourceGroupInfo) -> Windows.System.AppResourceGroupMemoryReport: ...
    @winrt_mixinmethod
    def GetProcessDiagnosticInfos(self: Windows.System.IAppResourceGroupInfo) -> Windows.Foundation.Collections.IVector[Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_mixinmethod
    def GetStateReport(self: Windows.System.IAppResourceGroupInfo) -> Windows.System.AppResourceGroupStateReport: ...
    @winrt_mixinmethod
    def StartSuspendAsync(self: Windows.System.IAppResourceGroupInfo2) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_mixinmethod
    def StartResumeAsync(self: Windows.System.IAppResourceGroupInfo2) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_mixinmethod
    def StartTerminateAsync(self: Windows.System.IAppResourceGroupInfo2) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
    InstanceId = property(get_InstanceId, None)
    IsShared = property(get_IsShared, None)
class AppResourceGroupInfoWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupInfoWatcher'
    @winrt_mixinmethod
    def add_Added(self: Windows.System.IAppResourceGroupInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.System.IAppResourceGroupInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.System.IAppResourceGroupInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.System.IAppResourceGroupInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.System.IAppResourceGroupInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.System.IAppResourceGroupInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.System.IAppResourceGroupInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.System.IAppResourceGroupInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ExecutionStateChanged(self: Windows.System.IAppResourceGroupInfoWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExecutionStateChanged(self: Windows.System.IAppResourceGroupInfoWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.System.IAppResourceGroupInfoWatcher) -> Windows.System.AppResourceGroupInfoWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.System.IAppResourceGroupInfoWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.IAppResourceGroupInfoWatcher) -> Void: ...
    Status = property(get_Status, None)
class AppResourceGroupInfoWatcherEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupInfoWatcherEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfos(self: Windows.System.IAppResourceGroupInfoWatcherEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.System.AppDiagnosticInfo]: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: Windows.System.IAppResourceGroupInfoWatcherEventArgs) -> Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class AppResourceGroupInfoWatcherExecutionStateChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_AppDiagnosticInfos(self: Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.System.AppDiagnosticInfo]: ...
    @winrt_mixinmethod
    def get_AppResourceGroupInfo(self: Windows.System.IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs) -> Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
AppResourceGroupInfoWatcherStatus = Int32
AppResourceGroupInfoWatcherStatus_Created: AppResourceGroupInfoWatcherStatus = 0
AppResourceGroupInfoWatcherStatus_Started: AppResourceGroupInfoWatcherStatus = 1
AppResourceGroupInfoWatcherStatus_EnumerationCompleted: AppResourceGroupInfoWatcherStatus = 2
AppResourceGroupInfoWatcherStatus_Stopping: AppResourceGroupInfoWatcherStatus = 3
AppResourceGroupInfoWatcherStatus_Stopped: AppResourceGroupInfoWatcherStatus = 4
AppResourceGroupInfoWatcherStatus_Aborted: AppResourceGroupInfoWatcherStatus = 5
class AppResourceGroupMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupMemoryReport'
    @winrt_mixinmethod
    def get_CommitUsageLimit(self: Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_CommitUsageLevel(self: Windows.System.IAppResourceGroupMemoryReport) -> Windows.System.AppMemoryUsageLevel: ...
    @winrt_mixinmethod
    def get_PrivateCommitUsage(self: Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCommitUsage(self: Windows.System.IAppResourceGroupMemoryReport) -> UInt64: ...
    CommitUsageLimit = property(get_CommitUsageLimit, None)
    CommitUsageLevel = property(get_CommitUsageLevel, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class AppResourceGroupStateReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppResourceGroupStateReport'
    @winrt_mixinmethod
    def get_ExecutionState(self: Windows.System.IAppResourceGroupStateReport) -> Windows.System.AppResourceGroupExecutionState: ...
    @winrt_mixinmethod
    def get_EnergyQuotaState(self: Windows.System.IAppResourceGroupStateReport) -> Windows.System.AppResourceGroupEnergyQuotaState: ...
    ExecutionState = property(get_ExecutionState, None)
    EnergyQuotaState = property(get_EnergyQuotaState, None)
class AppUriHandlerHost(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppUriHandlerHost'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.System.IAppUriHandlerHostFactory, name: WinRT_String) -> Windows.System.AppUriHandlerHost: ...
    @winrt_activatemethod
    def New(cls) -> Windows.System.AppUriHandlerHost: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.System.IAppUriHandlerHost) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.System.IAppUriHandlerHost, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.System.IAppUriHandlerHost2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.System.IAppUriHandlerHost2, value: Boolean) -> Void: ...
    Name = property(get_Name, put_Name)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class AppUriHandlerRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppUriHandlerRegistration'
    @winrt_mixinmethod
    def get_Name(self: Windows.System.IAppUriHandlerRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.IAppUriHandlerRegistration) -> Windows.System.User: ...
    @winrt_mixinmethod
    def GetAppAddedHostsAsync(self: Windows.System.IAppUriHandlerRegistration) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppUriHandlerHost]]: ...
    @winrt_mixinmethod
    def SetAppAddedHostsAsync(self: Windows.System.IAppUriHandlerRegistration, hosts: Windows.Foundation.Collections.IIterable[Windows.System.AppUriHandlerHost]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetAllHosts(self: Windows.System.IAppUriHandlerRegistration2) -> Windows.Foundation.Collections.IVector[Windows.System.AppUriHandlerHost]: ...
    @winrt_mixinmethod
    def UpdateHosts(self: Windows.System.IAppUriHandlerRegistration2, hosts: Windows.Foundation.Collections.IIterable[Windows.System.AppUriHandlerHost]) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.System.IAppUriHandlerRegistration2) -> WinRT_String: ...
    Name = property(get_Name, None)
    User = property(get_User, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class AppUriHandlerRegistrationManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.AppUriHandlerRegistrationManager'
    @winrt_mixinmethod
    def get_User(self: Windows.System.IAppUriHandlerRegistrationManager) -> Windows.System.User: ...
    @winrt_mixinmethod
    def TryGetRegistration(self: Windows.System.IAppUriHandlerRegistrationManager, name: WinRT_String) -> Windows.System.AppUriHandlerRegistration: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.System.IAppUriHandlerRegistrationManager2) -> WinRT_String: ...
    @winrt_classmethod
    def GetForPackage(cls: Windows.System.IAppUriHandlerRegistrationManagerStatics2, packageFamilyName: WinRT_String) -> Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetForPackageForUser(cls: Windows.System.IAppUriHandlerRegistrationManagerStatics2, packageFamilyName: WinRT_String, user: Windows.System.User) -> Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.IAppUriHandlerRegistrationManagerStatics) -> Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.IAppUriHandlerRegistrationManagerStatics, user: Windows.System.User) -> Windows.System.AppUriHandlerRegistrationManager: ...
    User = property(get_User, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
AutoUpdateTimeZoneStatus = Int32
AutoUpdateTimeZoneStatus_Attempted: AutoUpdateTimeZoneStatus = 0
AutoUpdateTimeZoneStatus_TimedOut: AutoUpdateTimeZoneStatus = 1
AutoUpdateTimeZoneStatus_Failed: AutoUpdateTimeZoneStatus = 2
class DateTimeSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.DateTimeSettings'
    @winrt_classmethod
    def SetSystemDateTime(cls: Windows.System.IDateTimeSettingsStatics, utcDateTime: Windows.Foundation.DateTime) -> Void: ...
DiagnosticAccessStatus = Int32
DiagnosticAccessStatus_Unspecified: DiagnosticAccessStatus = 0
DiagnosticAccessStatus_Denied: DiagnosticAccessStatus = 1
DiagnosticAccessStatus_Limited: DiagnosticAccessStatus = 2
DiagnosticAccessStatus_Allowed: DiagnosticAccessStatus = 3
class DispatcherQueue(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.DispatcherQueue'
    @winrt_mixinmethod
    def CreateTimer(self: Windows.System.IDispatcherQueue) -> Windows.System.DispatcherQueueTimer: ...
    @winrt_mixinmethod
    def TryEnqueue(self: Windows.System.IDispatcherQueue, callback: Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnqueueWithPriority(self: Windows.System.IDispatcherQueue, priority: Windows.System.DispatcherQueuePriority, callback: Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def add_ShutdownStarting(self: Windows.System.IDispatcherQueue, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueue, Windows.System.DispatcherQueueShutdownStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShutdownStarting(self: Windows.System.IDispatcherQueue, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShutdownCompleted(self: Windows.System.IDispatcherQueue, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueue, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShutdownCompleted(self: Windows.System.IDispatcherQueue, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HasThreadAccess(self: Windows.System.IDispatcherQueue2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: Windows.System.IDispatcherQueueStatics) -> Windows.System.DispatcherQueue: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class DispatcherQueueController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.DispatcherQueueController'
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.System.IDispatcherQueueController) -> Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def ShutdownQueueAsync(self: Windows.System.IDispatcherQueueController) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def CreateOnDedicatedThread(cls: Windows.System.IDispatcherQueueControllerStatics) -> Windows.System.DispatcherQueueController: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class DispatcherQueueHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfa2dc9c-1a2d-4917-98-f2-93-9a-f1-d6-e0-c8')
    ClassId = 'Windows.System.DispatcherQueueHandler'
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
DispatcherQueuePriority = Int32
DispatcherQueuePriority_Low: DispatcherQueuePriority = -10
DispatcherQueuePriority_Normal: DispatcherQueuePriority = 0
DispatcherQueuePriority_High: DispatcherQueuePriority = 10
class DispatcherQueueShutdownStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.DispatcherQueueShutdownStartingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.System.IDispatcherQueueShutdownStartingEventArgs) -> Windows.Foundation.Deferral: ...
class DispatcherQueueTimer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.DispatcherQueueTimer'
    @winrt_mixinmethod
    def get_Interval(self: Windows.System.IDispatcherQueueTimer) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Interval(self: Windows.System.IDispatcherQueueTimer, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsRunning(self: Windows.System.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRepeating(self: Windows.System.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRepeating(self: Windows.System.IDispatcherQueueTimer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.System.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def add_Tick(self: Windows.System.IDispatcherQueueTimer, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueueTimer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tick(self: Windows.System.IDispatcherQueueTimer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRunning = property(get_IsRunning, None)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
class FolderLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.FolderLauncherOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.System.FolderLauncherOptions: ...
    @winrt_mixinmethod
    def get_ItemsToSelect(self: Windows.System.IFolderLauncherOptions) -> Windows.Foundation.Collections.IVector[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_DesiredRemainingView(self: Windows.System.ILauncherViewOptions) -> Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_DesiredRemainingView(self: Windows.System.ILauncherViewOptions, value: Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    ItemsToSelect = property(get_ItemsToSelect, None)
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class IAppActivationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b528900-f46e-4eb0-aa-6c-38-af-55-7c-f9-ed')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> Windows.System.AppResourceGroupInfo: ...
    ExtendedError = property(get_ExtendedError, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class IAppDiagnosticInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e348a69a-8889-4ca3-be-07-d5-ff-ff-5f-08-04')
    @winrt_commethod(6)
    def get_AppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    AppInfo = property(get_AppInfo, None)
class IAppDiagnosticInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df46fbd7-191a-446c-94-73-8f-bc-23-74-a3-54')
    @winrt_commethod(6)
    def GetResourceGroups(self) -> Windows.Foundation.Collections.IVector[Windows.System.AppResourceGroupInfo]: ...
    @winrt_commethod(7)
    def CreateResourceGroupWatcher(self) -> Windows.System.AppResourceGroupInfoWatcher: ...
class IAppDiagnosticInfo3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c895c63d-dd61-4c65-ba-bd-81-a1-0b-4f-98-15')
    @winrt_commethod(6)
    def LaunchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.AppActivationResult]: ...
class IAppDiagnosticInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce6925bf-10ca-40c8-a9-ca-c5-c9-65-01-86-6e')
    @winrt_commethod(6)
    def RequestInfoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
class IAppDiagnosticInfoStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05b24b86-1000-4c90-bb-9f-72-35-07-1c-50-fe')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.System.AppDiagnosticInfoWatcher: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.DiagnosticAccessStatus]: ...
    @winrt_commethod(8)
    def RequestInfoForPackageAsync(self, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    @winrt_commethod(9)
    def RequestInfoForAppAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
    @winrt_commethod(10)
    def RequestInfoForAppUserModelId(self, appUserModelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]]: ...
class IAppDiagnosticInfoWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75575070-01d3-489a-93-25-52-f9-cc-6e-de-0a')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.System.AppDiagnosticInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppDiagnosticInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> Windows.System.AppDiagnosticInfoWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IAppDiagnosticInfoWatcherEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7017c716-e1da-4c65-99-df-04-6d-ff-5b-e7-1a')
    @winrt_commethod(6)
    def get_AppDiagnosticInfo(self) -> Windows.System.AppDiagnosticInfo: ...
    AppDiagnosticInfo = property(get_AppDiagnosticInfo, None)
class IAppExecutionStateChangeResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f039bf0-f91b-4df8-ae-77-30-33-cc-b6-91-14')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IAppMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6d65339b-4d6f-45bc-9c-5e-e4-9b-3f-f2-75-8d')
    @winrt_commethod(6)
    def get_PrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_PeakPrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_TotalCommitUsage(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_TotalCommitLimit(self) -> UInt64: ...
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    PeakPrivateCommitUsage = property(get_PeakPrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
    TotalCommitLimit = property(get_TotalCommitLimit, None)
class IAppMemoryReport2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f7f3738-51b7-42dc-b7-ed-79-ba-46-d2-88-57')
    @winrt_commethod(6)
    def get_ExpectedTotalCommitLimit(self) -> UInt64: ...
    ExpectedTotalCommitLimit = property(get_ExpectedTotalCommitLimit, None)
class IAppMemoryUsageLimitChangingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79f86664-feca-4da5-9e-40-2b-c6-3e-fd-c9-79')
    @winrt_commethod(6)
    def get_OldLimit(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_NewLimit(self) -> UInt64: ...
    OldLimit = property(get_OldLimit, None)
    NewLimit = property(get_NewLimit, None)
class IAppResourceGroupBackgroundTaskReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2566e74e-b05d-40c2-9d-c1-1a-4f-03-9e-a1-20')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Trigger(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_EntryPoint(self) -> WinRT_String: ...
    TaskId = property(get_TaskId, None)
    Name = property(get_Name, None)
    Trigger = property(get_Trigger, None)
    EntryPoint = property(get_EntryPoint, None)
class IAppResourceGroupInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b913f77a-e807-49f4-84-5e-7b-8b-dc-fe-8e-e7')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_IsShared(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetBackgroundTaskReports(self) -> Windows.Foundation.Collections.IVector[Windows.System.AppResourceGroupBackgroundTaskReport]: ...
    @winrt_commethod(9)
    def GetMemoryReport(self) -> Windows.System.AppResourceGroupMemoryReport: ...
    @winrt_commethod(10)
    def GetProcessDiagnosticInfos(self) -> Windows.Foundation.Collections.IVector[Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_commethod(11)
    def GetStateReport(self) -> Windows.System.AppResourceGroupStateReport: ...
    InstanceId = property(get_InstanceId, None)
    IsShared = property(get_IsShared, None)
class IAppResourceGroupInfo2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ee9b236d-d305-4d6b-92-f7-6a-fd-ad-72-de-dc')
    @winrt_commethod(6)
    def StartSuspendAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_commethod(7)
    def StartResumeAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
    @winrt_commethod(8)
    def StartTerminateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.AppExecutionStateChangeResult]: ...
class IAppResourceGroupInfoWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d9b0a0fd-6e5a-4c72-8b-17-09-fe-c4-a2-12-bd')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ExecutionStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.AppResourceGroupInfoWatcher, Windows.System.AppResourceGroupInfoWatcherExecutionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ExecutionStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Status(self) -> Windows.System.AppResourceGroupInfoWatcherStatus: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IAppResourceGroupInfoWatcherEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a787637-6302-4d2f-bf-89-1c-12-d0-b2-a6-b9')
    @winrt_commethod(6)
    def get_AppDiagnosticInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.AppDiagnosticInfo]: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1bdbedd7-fee6-4fd4-98-dd-e9-2a-2c-c2-99-f3')
    @winrt_commethod(6)
    def get_AppDiagnosticInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.AppDiagnosticInfo]: ...
    @winrt_commethod(7)
    def get_AppResourceGroupInfo(self) -> Windows.System.AppResourceGroupInfo: ...
    AppDiagnosticInfos = property(get_AppDiagnosticInfos, None)
    AppResourceGroupInfo = property(get_AppResourceGroupInfo, None)
class IAppResourceGroupMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c8c06b1-7db1-4c51-a2-25-7f-ae-2d-49-e4-31')
    @winrt_commethod(6)
    def get_CommitUsageLimit(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_CommitUsageLevel(self) -> Windows.System.AppMemoryUsageLevel: ...
    @winrt_commethod(8)
    def get_PrivateCommitUsage(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_TotalCommitUsage(self) -> UInt64: ...
    CommitUsageLimit = property(get_CommitUsageLimit, None)
    CommitUsageLevel = property(get_CommitUsageLevel, None)
    PrivateCommitUsage = property(get_PrivateCommitUsage, None)
    TotalCommitUsage = property(get_TotalCommitUsage, None)
class IAppResourceGroupStateReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('52849f18-2f70-4236-ab-40-d0-4d-b0-c7-b9-31')
    @winrt_commethod(6)
    def get_ExecutionState(self) -> Windows.System.AppResourceGroupExecutionState: ...
    @winrt_commethod(7)
    def get_EnergyQuotaState(self) -> Windows.System.AppResourceGroupEnergyQuotaState: ...
    ExecutionState = property(get_ExecutionState, None)
    EnergyQuotaState = property(get_EnergyQuotaState, None)
class IAppUriHandlerHost(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d50cac5-92d2-5409-b5-6f-7f-73-e1-0e-a4-c3')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
class IAppUriHandlerHost2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3a0bee95-29e4-51bf-80-95-a3-c0-68-e3-c7-2a')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IAppUriHandlerHostFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('257c3c96-ce04-5f98-96-bb-3e-bd-3e-92-75-bb')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String) -> Windows.System.AppUriHandlerHost: ...
class IAppUriHandlerRegistration(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f73aeb1-4569-5c3f-9b-a0-99-12-3e-ea-32-c3')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(8)
    def GetAppAddedHostsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.System.AppUriHandlerHost]]: ...
    @winrt_commethod(9)
    def SetAppAddedHostsAsync(self, hosts: Windows.Foundation.Collections.IIterable[Windows.System.AppUriHandlerHost]) -> Windows.Foundation.IAsyncAction: ...
    Name = property(get_Name, None)
    User = property(get_User, None)
class IAppUriHandlerRegistration2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d54dac97-cb39-5f1f-88-3e-01-85-37-30-bd-6d')
    @winrt_commethod(6)
    def GetAllHosts(self) -> Windows.Foundation.Collections.IVector[Windows.System.AppUriHandlerHost]: ...
    @winrt_commethod(7)
    def UpdateHosts(self, hosts: Windows.Foundation.Collections.IIterable[Windows.System.AppUriHandlerHost]) -> Void: ...
    @winrt_commethod(8)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppUriHandlerRegistrationManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e62c9a52-ac94-5750-ac-1b-6c-fb-6f-25-02-63')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def TryGetRegistration(self, name: WinRT_String) -> Windows.System.AppUriHandlerRegistration: ...
    User = property(get_User, None)
class IAppUriHandlerRegistrationManager2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bddfcaf1-b51a-5e69-ae-fd-70-88-d9-f2-b1-23')
    @winrt_commethod(6)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
class IAppUriHandlerRegistrationManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d5cedd9f-5729-5b76-a1-d4-02-85-f2-95-c1-24')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.AppUriHandlerRegistrationManager: ...
class IAppUriHandlerRegistrationManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('14f78379-6890-5080-90-a7-98-82-4a-7f-07-9e')
    @winrt_commethod(6)
    def GetForPackage(self, packageFamilyName: WinRT_String) -> Windows.System.AppUriHandlerRegistrationManager: ...
    @winrt_commethod(7)
    def GetForPackageForUser(self, packageFamilyName: WinRT_String, user: Windows.System.User) -> Windows.System.AppUriHandlerRegistrationManager: ...
class IDateTimeSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d2150d1-47ee-48ab-a5-2b-9f-19-54-27-8d-82')
    @winrt_commethod(6)
    def SetSystemDateTime(self, utcDateTime: Windows.Foundation.DateTime) -> Void: ...
class IDispatcherQueue(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('603e88e4-a338-4ffe-a4-57-a5-cf-b9-ce-b8-99')
    @winrt_commethod(6)
    def CreateTimer(self) -> Windows.System.DispatcherQueueTimer: ...
    @winrt_commethod(7)
    def TryEnqueue(self, callback: Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(8)
    def TryEnqueueWithPriority(self, priority: Windows.System.DispatcherQueuePriority, callback: Windows.System.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(9)
    def add_ShutdownStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueue, Windows.System.DispatcherQueueShutdownStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ShutdownStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_ShutdownCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueue, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ShutdownCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDispatcherQueue2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c822c647-30ef-506e-bd-1e-a6-47-ae-66-75-ff')
    @winrt_commethod(6)
    def get_HasThreadAccess(self) -> Boolean: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class IDispatcherQueueController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('22f34e66-50db-4e36-a9-8d-61-c0-1b-38-4d-20')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    @winrt_commethod(7)
    def ShutdownQueueAsync(self) -> Windows.Foundation.IAsyncAction: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IDispatcherQueueControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0a6c98e0-5198-49a2-a3-13-3f-70-d1-f1-3c-27')
    @winrt_commethod(6)
    def CreateOnDedicatedThread(self) -> Windows.System.DispatcherQueueController: ...
class IDispatcherQueueShutdownStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c4724c4c-ff97-40c0-a2-26-cc-0a-aa-54-5e-89')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IDispatcherQueueStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a96d83d7-9371-4517-92-45-d0-82-4a-c1-2c-74')
    @winrt_commethod(6)
    def GetForCurrentThread(self) -> Windows.System.DispatcherQueue: ...
class IDispatcherQueueTimer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5feabb1d-a31c-4727-b1-ac-37-45-46-49-d5-6a')
    @winrt_commethod(6)
    def get_Interval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Interval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
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
    def add_Tick(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.DispatcherQueueTimer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Tick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRunning = property(get_IsRunning, None)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
class IFolderLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bb91c27d-6b87-432a-bd-04-77-6c-6f-5f-b2-ab')
    @winrt_commethod(6)
    def get_ItemsToSelect(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.IStorageItem]: ...
    ItemsToSelect = property(get_ItemsToSelect, None)
class IKnownUserPropertiesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7755911a-70c5-48e5-b6-37-5b-a3-44-1e-4e-e4')
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
    DisplayName = property(get_DisplayName, None)
    FirstName = property(get_FirstName, None)
    LastName = property(get_LastName, None)
    ProviderName = property(get_ProviderName, None)
    AccountName = property(get_AccountName, None)
    GuestHost = property(get_GuestHost, None)
    PrincipalName = property(get_PrincipalName, None)
    DomainName = property(get_DomainName, None)
    SessionInitiationProtocolUri = property(get_SessionInitiationProtocolUri, None)
class IKnownUserPropertiesStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5b450782-f620-577e-b1-b3-dd-56-64-4d-79-b1')
    @winrt_commethod(6)
    def get_AgeEnforcementRegion(self) -> WinRT_String: ...
    AgeEnforcementRegion = property(get_AgeEnforcementRegion, None)
class ILaunchUriResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ec27a8df-f6d5-45ca-91-3a-70-a4-0c-5c-82-21')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.System.LaunchUriStatus: ...
    @winrt_commethod(7)
    def get_Result(self) -> Windows.Foundation.Collections.ValueSet: ...
    Status = property(get_Status, None)
    Result = property(get_Result, None)
class ILauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bafa21d8-b071-4cd8-85-3e-34-12-03-e5-57-d3')
    @winrt_commethod(6)
    def get_TreatAsUntrusted(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TreatAsUntrusted(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayApplicationPicker(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_DisplayApplicationPicker(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_UI(self) -> Windows.System.LauncherUIOptions: ...
    @winrt_commethod(11)
    def get_PreferredApplicationPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_PreferredApplicationPackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_PreferredApplicationDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_PreferredApplicationDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_FallbackUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_FallbackUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_ContentType(self, value: WinRT_String) -> Void: ...
    TreatAsUntrusted = property(get_TreatAsUntrusted, put_TreatAsUntrusted)
    DisplayApplicationPicker = property(get_DisplayApplicationPicker, put_DisplayApplicationPicker)
    UI = property(get_UI, None)
    PreferredApplicationPackageFamilyName = property(get_PreferredApplicationPackageFamilyName, put_PreferredApplicationPackageFamilyName)
    PreferredApplicationDisplayName = property(get_PreferredApplicationDisplayName, put_PreferredApplicationDisplayName)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    ContentType = property(get_ContentType, put_ContentType)
class ILauncherOptions2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3ba08eb4-6e40-4dce-a1-a3-2f-53-95-0a-fb-49')
    @winrt_commethod(6)
    def get_TargetApplicationPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TargetApplicationPackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_NeighboringFilesQuery(self) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(9)
    def put_NeighboringFilesQuery(self, value: Windows.Storage.Search.StorageFileQueryResult) -> Void: ...
    TargetApplicationPackageFamilyName = property(get_TargetApplicationPackageFamilyName, put_TargetApplicationPackageFamilyName)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, put_NeighboringFilesQuery)
class ILauncherOptions3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f0770655-4b63-4e3a-91-07-4e-68-78-41-92-3a')
    @winrt_commethod(6)
    def get_IgnoreAppUriHandlers(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IgnoreAppUriHandlers(self, value: Boolean) -> Void: ...
    IgnoreAppUriHandlers = property(get_IgnoreAppUriHandlers, put_IgnoreAppUriHandlers)
class ILauncherOptions4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef6fd10e-e6fb-4814-a4-4e-57-e8-b9-d9-a0-1b')
    @winrt_commethod(6)
    def get_LimitPickerToCurrentAppAndAppUriHandlers(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_LimitPickerToCurrentAppAndAppUriHandlers(self, value: Boolean) -> Void: ...
    LimitPickerToCurrentAppAndAppUriHandlers = property(get_LimitPickerToCurrentAppAndAppUriHandlers, put_LimitPickerToCurrentAppAndAppUriHandlers)
class ILauncherStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('277151c3-9e3e-42f6-91-a4-5d-fd-eb-23-24-51')
    @winrt_commethod(6)
    def LaunchFileAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFileWithOptionsAsync(self, file: Windows.Storage.IStorageFile, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def LaunchUriAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def LaunchUriWithOptionsAsync(self, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59ba2fbb-24cb-4c02-a4-c4-82-94-56-9d-54-f1')
    @winrt_commethod(6)
    def LaunchUriForResultsAsync(self, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_commethod(7)
    def LaunchUriForResultsWithDataAsync(self, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_commethod(8)
    def LaunchUriWithDataAsync(self, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def QueryUriSupportAsync(self, uri: Windows.Foundation.Uri, launchQuerySupportType: Windows.System.LaunchQuerySupportType) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(10)
    def QueryUriSupportWithPackageFamilyNameAsync(self, uri: Windows.Foundation.Uri, launchQuerySupportType: Windows.System.LaunchQuerySupportType, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(11)
    def QueryFileSupportAsync(self, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(12)
    def QueryFileSupportWithPackageFamilyNameAsync(self, file: Windows.Storage.StorageFile, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(13)
    def FindUriSchemeHandlersAsync(self, scheme: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(14)
    def FindUriSchemeHandlersWithLaunchUriTypeAsync(self, scheme: WinRT_String, launchQuerySupportType: Windows.System.LaunchQuerySupportType) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(15)
    def FindFileHandlersAsync(self, extension: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
class ILauncherStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('234261a8-9db3-4683-aa-42-dc-6f-51-d3-38-47')
    @winrt_commethod(6)
    def LaunchFolderAsync(self, folder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFolderWithOptionsAsync(self, folder: Windows.Storage.IStorageFolder, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherStatics4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b9ec819f-b5a5-41c6-b3-b3-dd-1b-31-78-bc-f2')
    @winrt_commethod(6)
    def QueryAppUriSupportAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(7)
    def QueryAppUriSupportWithPackageFamilyNameAsync(self, uri: Windows.Foundation.Uri, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_commethod(8)
    def FindAppUriHandlersAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_commethod(9)
    def LaunchUriForUserAsync(self, user: Windows.System.User, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(10)
    def LaunchUriWithOptionsForUserAsync(self, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(11)
    def LaunchUriWithDataForUserAsync(self, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_commethod(12)
    def LaunchUriForResultsForUserAsync(self, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_commethod(13)
    def LaunchUriForResultsWithDataForUserAsync(self, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
class ILauncherStatics5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5b24ef84-d895-5fea-91-53-1a-c4-9a-ed-9b-a9')
    @winrt_commethod(6)
    def LaunchFolderPathAsync(self, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LaunchFolderPathWithOptionsAsync(self, path: WinRT_String, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def LaunchFolderPathForUserAsync(self, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def LaunchFolderPathWithOptionsForUserAsync(self, user: Windows.System.User, path: WinRT_String, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ILauncherUIOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1b25da6e-8aa6-41e9-82-51-41-65-f5-98-5f-49')
    @winrt_commethod(6)
    def get_InvocationPoint(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(7)
    def put_InvocationPoint(self, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def get_SelectionRect(self) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_SelectionRect(self, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    @winrt_commethod(10)
    def get_PreferredPlacement(self) -> Windows.UI.Popups.Placement: ...
    @winrt_commethod(11)
    def put_PreferredPlacement(self, value: Windows.UI.Popups.Placement) -> Void: ...
    InvocationPoint = property(get_InvocationPoint, put_InvocationPoint)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
    PreferredPlacement = property(get_PreferredPlacement, put_PreferredPlacement)
class ILauncherViewOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8a9b29f1-7ca7-49de-9b-d3-3c-5b-71-84-f6-16')
    @winrt_commethod(6)
    def get_DesiredRemainingView(self) -> Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_commethod(7)
    def put_DesiredRemainingView(self, value: Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class IMemoryManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c6c279c-d7ca-4779-91-88-40-57-21-9c-e6-4c')
    @winrt_commethod(6)
    def get_AppMemoryUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_AppMemoryUsageLimit(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_AppMemoryUsageLevel(self) -> Windows.System.AppMemoryUsageLevel: ...
    @winrt_commethod(9)
    def add_AppMemoryUsageIncreased(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_AppMemoryUsageIncreased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AppMemoryUsageDecreased(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AppMemoryUsageDecreased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_AppMemoryUsageLimitChanging(self, handler: Windows.Foundation.EventHandler[Windows.System.AppMemoryUsageLimitChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AppMemoryUsageLimitChanging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AppMemoryUsage = property(get_AppMemoryUsage, None)
    AppMemoryUsageLimit = property(get_AppMemoryUsageLimit, None)
    AppMemoryUsageLevel = property(get_AppMemoryUsageLevel, None)
class IMemoryManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6eee351f-6d62-423f-94-79-b0-1f-9c-9f-76-69')
    @winrt_commethod(6)
    def GetAppMemoryReport(self) -> Windows.System.AppMemoryReport: ...
    @winrt_commethod(7)
    def GetProcessMemoryReport(self) -> Windows.System.ProcessMemoryReport: ...
class IMemoryManagerStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('149b59ce-92ad-4e35-89-eb-50-df-b4-c0-d9-1c')
    @winrt_commethod(6)
    def TrySetAppMemoryUsageLimit(self, value: UInt64) -> Boolean: ...
class IMemoryManagerStatics4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c5a94828-e84e-4886-8a-0d-44-b3-19-0e-3b-72')
    @winrt_commethod(6)
    def get_ExpectedAppMemoryUsageLimit(self) -> UInt64: ...
    ExpectedAppMemoryUsageLimit = property(get_ExpectedAppMemoryUsageLimit, None)
class IProcessLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3080b9cf-f444-4a83-be-af-a5-49-a0-f3-22-9c')
    @winrt_commethod(6)
    def get_StandardInput(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(7)
    def put_StandardInput(self, value: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(8)
    def get_StandardOutput(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(9)
    def put_StandardOutput(self, value: Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_commethod(10)
    def get_StandardError(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(11)
    def put_StandardError(self, value: Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_commethod(12)
    def get_WorkingDirectory(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_WorkingDirectory(self, value: WinRT_String) -> Void: ...
    StandardInput = property(get_StandardInput, put_StandardInput)
    StandardOutput = property(get_StandardOutput, put_StandardOutput)
    StandardError = property(get_StandardError, put_StandardError)
    WorkingDirectory = property(get_WorkingDirectory, put_WorkingDirectory)
class IProcessLauncherResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('544c8934-86d8-4991-8e-75-ec-e8-a4-3b-6b-6d')
    @winrt_commethod(6)
    def get_ExitCode(self) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class IProcessLauncherStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33ab66e7-2d0e-448b-a6-a0-c1-3c-38-36-d0-9c')
    @winrt_commethod(6)
    def RunToCompletionAsync(self, fileName: WinRT_String, args: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.ProcessLauncherResult]: ...
    @winrt_commethod(7)
    def RunToCompletionAsyncWithOptions(self, fileName: WinRT_String, args: WinRT_String, options: Windows.System.ProcessLauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.ProcessLauncherResult]: ...
class IProcessMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('087305a8-9b70-4782-87-41-3a-98-2b-6c-e5-e4')
    @winrt_commethod(6)
    def get_PrivateWorkingSetUsage(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_TotalWorkingSetUsage(self) -> UInt64: ...
    PrivateWorkingSetUsage = property(get_PrivateWorkingSetUsage, None)
    TotalWorkingSetUsage = property(get_TotalWorkingSetUsage, None)
class IProtocolForResultsOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d581293a-6de9-4d28-93-78-f8-67-82-e1-82-bb')
    @winrt_commethod(6)
    def ReportCompleted(self, data: Windows.Foundation.Collections.ValueSet) -> Void: ...
class IRemoteLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9e3a2788-2891-4cdf-a2-d6-9d-ff-7d-02-e6-93')
    @winrt_commethod(6)
    def get_FallbackUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_FallbackUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_PreferredAppIds(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    PreferredAppIds = property(get_PreferredAppIds, None)
class IRemoteLauncherStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d7db7a93-a30c-48b7-9f-21-05-10-26-a4-e5-17')
    @winrt_commethod(6)
    def LaunchUriAsync(self, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_commethod(7)
    def LaunchUriWithOptionsAsync(self, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri, options: Windows.System.RemoteLauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_commethod(8)
    def LaunchUriWithDataAsync(self, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri, options: Windows.System.RemoteLauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
class IShutdownManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72e247ed-dd5b-4d6c-b1-d0-c5-7a-7b-bb-5f-94')
    @winrt_commethod(6)
    def BeginShutdown(self, shutdownKind: Windows.System.ShutdownKind, timeout: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def CancelShutdown(self) -> Void: ...
class IShutdownManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0f69a02f-9c34-43c7-a8-c3-70-b3-0a-7f-75-04')
    @winrt_commethod(6)
    def IsPowerStateSupported(self, powerState: Windows.System.PowerState) -> Boolean: ...
    @winrt_commethod(7)
    def EnterPowerState(self, powerState: Windows.System.PowerState) -> Void: ...
    @winrt_commethod(8)
    def EnterPowerStateWithTimeSpan(self, powerState: Windows.System.PowerState, wakeUpAfter: Windows.Foundation.TimeSpan) -> Void: ...
class ITimeZoneSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b3b2bea-a101-41ae-9f-bd-02-87-28-ba-b7-3d')
    @winrt_commethod(6)
    def get_CurrentTimeZoneDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedTimeZoneDisplayNames(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_CanChangeTimeZone(self) -> Boolean: ...
    @winrt_commethod(9)
    def ChangeTimeZoneByDisplayName(self, timeZoneDisplayName: WinRT_String) -> Void: ...
    CurrentTimeZoneDisplayName = property(get_CurrentTimeZoneDisplayName, None)
    SupportedTimeZoneDisplayNames = property(get_SupportedTimeZoneDisplayNames, None)
    CanChangeTimeZone = property(get_CanChangeTimeZone, None)
class ITimeZoneSettingsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('555c0db8-39a8-49fa-b4-f6-a2-c7-fc-28-42-ec')
    @winrt_commethod(6)
    def AutoUpdateTimeZoneAsync(self, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.System.AutoUpdateTimeZoneStatus]: ...
class IUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df9a26c6-e746-4bcd-b5-d4-12-01-03-c4-20-9b')
    @winrt_commethod(6)
    def get_NonRoamableId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AuthenticationStatus(self) -> Windows.System.UserAuthenticationStatus: ...
    @winrt_commethod(8)
    def get_Type(self) -> Windows.System.UserType: ...
    @winrt_commethod(9)
    def GetPropertyAsync(self, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(10)
    def GetPropertiesAsync(self, values: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_commethod(11)
    def GetPictureAsync(self, desiredSize: Windows.System.UserPictureSize) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    NonRoamableId = property(get_NonRoamableId, None)
    AuthenticationStatus = property(get_AuthenticationStatus, None)
    Type = property(get_Type, None)
class IUser2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('98ba5628-a6e3-518e-89-d9-d3-b2-b1-99-1a-10')
    @winrt_commethod(6)
    def CheckUserAgeConsentGroupAsync(self, consentGroup: Windows.System.UserAgeConsentGroup) -> Windows.Foundation.IAsyncOperation[Windows.System.UserAgeConsentResult]: ...
class IUserAuthenticationStatusChangeDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88b59568-bb30-42fb-a2-70-e9-90-2e-40-ef-a7')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IUserAuthenticationStatusChangingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8c030f28-a711-4c1e-ab-48-04-17-9c-15-93-8f')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.System.UserAuthenticationStatusChangeDeferral: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(8)
    def get_NewStatus(self) -> Windows.System.UserAuthenticationStatus: ...
    @winrt_commethod(9)
    def get_CurrentStatus(self) -> Windows.System.UserAuthenticationStatus: ...
    User = property(get_User, None)
    NewStatus = property(get_NewStatus, None)
    CurrentStatus = property(get_CurrentStatus, None)
class IUserChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('086459dc-18c6-48db-bc-99-72-4f-b9-20-3c-cc')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IUserChangedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b2ccb44-6f01-560c-97-ad-fc-7f-32-ec-58-1f')
    @winrt_commethod(6)
    def get_ChangedPropertyKinds(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.UserWatcherUpdateKind]: ...
    ChangedPropertyKinds = property(get_ChangedPropertyKinds, None)
class IUserDeviceAssociationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bd1f6f6c-bb5d-4d7b-a5-f0-c8-cd-11-a3-8d-42')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_NewUser(self) -> Windows.System.User: ...
    @winrt_commethod(8)
    def get_OldUser(self) -> Windows.System.User: ...
    DeviceId = property(get_DeviceId, None)
    NewUser = property(get_NewUser, None)
    OldUser = property(get_OldUser, None)
class IUserDeviceAssociationStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e491e14-f85a-4c07-8d-a9-7f-e3-d0-54-23-43')
    @winrt_commethod(6)
    def FindUserFromDeviceId(self, deviceId: WinRT_String) -> Windows.System.User: ...
    @winrt_commethod(7)
    def add_UserDeviceAssociationChanged(self, handler: Windows.Foundation.EventHandler[Windows.System.UserDeviceAssociationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_UserDeviceAssociationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserPicker(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d548008-f1e3-4a6c-8d-dc-a9-bb-0f-48-8a-ed')
    @winrt_commethod(6)
    def get_AllowGuestAccounts(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowGuestAccounts(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_SuggestedSelectedUser(self) -> Windows.System.User: ...
    @winrt_commethod(9)
    def put_SuggestedSelectedUser(self, value: Windows.System.User) -> Void: ...
    @winrt_commethod(10)
    def PickSingleUserAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.User]: ...
    AllowGuestAccounts = property(get_AllowGuestAccounts, put_AllowGuestAccounts)
    SuggestedSelectedUser = property(get_SuggestedSelectedUser, put_SuggestedSelectedUser)
class IUserPickerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('de3290dc-7e73-4df6-a1-ae-4d-7e-ca-82-b4-0d')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IUserStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('155eb23b-242a-45e0-a2-e9-31-71-fc-6a-7f-dd')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.System.UserWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_commethod(8)
    def FindAllAsyncByType(self, type: Windows.System.UserType) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_commethod(9)
    def FindAllAsyncByTypeAndStatus(self, type: Windows.System.UserType, status: Windows.System.UserAuthenticationStatus) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_commethod(10)
    def GetFromId(self, nonRoamableId: WinRT_String) -> Windows.System.User: ...
class IUserStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('74a37e11-2eb5-4487-b0-d5-2c-67-90-e0-13-e9')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.User: ...
class IUserWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('155eb23b-242a-45e0-a2-e9-31-71-fc-6a-7f-bb')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.System.UserWatcherStatus: ...
    @winrt_commethod(7)
    def Start(self) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_AuthenticationStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AuthenticationStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_AuthenticationStatusChanging(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserAuthenticationStatusChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_AuthenticationStatusChanging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class KnownUserProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.KnownUserProperties'
    @winrt_classmethod
    def get_AgeEnforcementRegion(cls: Windows.System.IKnownUserPropertiesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_DisplayName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FirstName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_LastName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ProviderName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AccountName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GuestHost(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrincipalName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DomainName(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SessionInitiationProtocolUri(cls: Windows.System.IKnownUserPropertiesStatics) -> WinRT_String: ...
    AgeEnforcementRegion = property(get_AgeEnforcementRegion, None)
    DisplayName = property(get_DisplayName, None)
    FirstName = property(get_FirstName, None)
    LastName = property(get_LastName, None)
    ProviderName = property(get_ProviderName, None)
    AccountName = property(get_AccountName, None)
    GuestHost = property(get_GuestHost, None)
    PrincipalName = property(get_PrincipalName, None)
    DomainName = property(get_DomainName, None)
    SessionInitiationProtocolUri = property(get_SessionInitiationProtocolUri, None)
LaunchFileStatus = Int32
LaunchFileStatus_Success: LaunchFileStatus = 0
LaunchFileStatus_AppUnavailable: LaunchFileStatus = 1
LaunchFileStatus_DeniedByPolicy: LaunchFileStatus = 2
LaunchFileStatus_FileTypeNotSupported: LaunchFileStatus = 3
LaunchFileStatus_Unknown: LaunchFileStatus = 4
LaunchQuerySupportStatus = Int32
LaunchQuerySupportStatus_Available: LaunchQuerySupportStatus = 0
LaunchQuerySupportStatus_AppNotInstalled: LaunchQuerySupportStatus = 1
LaunchQuerySupportStatus_AppUnavailable: LaunchQuerySupportStatus = 2
LaunchQuerySupportStatus_NotSupported: LaunchQuerySupportStatus = 3
LaunchQuerySupportStatus_Unknown: LaunchQuerySupportStatus = 4
LaunchQuerySupportType = Int32
LaunchQuerySupportType_Uri: LaunchQuerySupportType = 0
LaunchQuerySupportType_UriForResults: LaunchQuerySupportType = 1
class LaunchUriResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.LaunchUriResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.System.ILaunchUriResult) -> Windows.System.LaunchUriStatus: ...
    @winrt_mixinmethod
    def get_Result(self: Windows.System.ILaunchUriResult) -> Windows.Foundation.Collections.ValueSet: ...
    Status = property(get_Status, None)
    Result = property(get_Result, None)
LaunchUriStatus = Int32
LaunchUriStatus_Success: LaunchUriStatus = 0
LaunchUriStatus_AppUnavailable: LaunchUriStatus = 1
LaunchUriStatus_ProtocolUnavailable: LaunchUriStatus = 2
LaunchUriStatus_Unknown: LaunchUriStatus = 3
class Launcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Launcher'
    @winrt_classmethod
    def LaunchFolderPathAsync(cls: Windows.System.ILauncherStatics5, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathWithOptionsAsync(cls: Windows.System.ILauncherStatics5, path: WinRT_String, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathForUserAsync(cls: Windows.System.ILauncherStatics5, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderPathWithOptionsForUserAsync(cls: Windows.System.ILauncherStatics5, user: Windows.System.User, path: WinRT_String, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def QueryAppUriSupportAsync(cls: Windows.System.ILauncherStatics4, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryAppUriSupportWithPackageFamilyNameAsync(cls: Windows.System.ILauncherStatics4, uri: Windows.Foundation.Uri, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def FindAppUriHandlersAsync(cls: Windows.System.ILauncherStatics4, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def LaunchUriForUserAsync(cls: Windows.System.ILauncherStatics4, user: Windows.System.User, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsForUserAsync(cls: Windows.System.ILauncherStatics4, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithDataForUserAsync(cls: Windows.System.ILauncherStatics4, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriForResultsForUserAsync(cls: Windows.System.ILauncherStatics4, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriForResultsWithDataForUserAsync(cls: Windows.System.ILauncherStatics4, user: Windows.System.User, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchFileAsync(cls: Windows.System.ILauncherStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFileWithOptionsAsync(cls: Windows.System.ILauncherStatics, file: Windows.Storage.IStorageFile, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriAsync(cls: Windows.System.ILauncherStatics, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsAsync(cls: Windows.System.ILauncherStatics, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderAsync(cls: Windows.System.ILauncherStatics3, folder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchFolderWithOptionsAsync(cls: Windows.System.ILauncherStatics3, folder: Windows.Storage.IStorageFolder, options: Windows.System.FolderLauncherOptions) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LaunchUriForResultsAsync(cls: Windows.System.ILauncherStatics2, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriForResultsWithDataAsync(cls: Windows.System.ILauncherStatics2, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchUriResult]: ...
    @winrt_classmethod
    def LaunchUriWithDataAsync(cls: Windows.System.ILauncherStatics2, uri: Windows.Foundation.Uri, options: Windows.System.LauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def QueryUriSupportAsync(cls: Windows.System.ILauncherStatics2, uri: Windows.Foundation.Uri, launchQuerySupportType: Windows.System.LaunchQuerySupportType) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryUriSupportWithPackageFamilyNameAsync(cls: Windows.System.ILauncherStatics2, uri: Windows.Foundation.Uri, launchQuerySupportType: Windows.System.LaunchQuerySupportType, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryFileSupportAsync(cls: Windows.System.ILauncherStatics2, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def QueryFileSupportWithPackageFamilyNameAsync(cls: Windows.System.ILauncherStatics2, file: Windows.Storage.StorageFile, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.LaunchQuerySupportStatus]: ...
    @winrt_classmethod
    def FindUriSchemeHandlersAsync(cls: Windows.System.ILauncherStatics2, scheme: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def FindUriSchemeHandlersWithLaunchUriTypeAsync(cls: Windows.System.ILauncherStatics2, scheme: WinRT_String, launchQuerySupportType: Windows.System.LaunchQuerySupportType) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
    @winrt_classmethod
    def FindFileHandlersAsync(cls: Windows.System.ILauncherStatics2, extension: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.AppInfo]]: ...
class LauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.LauncherOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.System.LauncherOptions: ...
    @winrt_mixinmethod
    def get_TargetApplicationPackageFamilyName(self: Windows.System.ILauncherOptions2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetApplicationPackageFamilyName(self: Windows.System.ILauncherOptions2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: Windows.System.ILauncherOptions2) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def put_NeighboringFilesQuery(self: Windows.System.ILauncherOptions2, value: Windows.Storage.Search.StorageFileQueryResult) -> Void: ...
    @winrt_mixinmethod
    def get_TreatAsUntrusted(self: Windows.System.ILauncherOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_TreatAsUntrusted(self: Windows.System.ILauncherOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayApplicationPicker(self: Windows.System.ILauncherOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayApplicationPicker(self: Windows.System.ILauncherOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_UI(self: Windows.System.ILauncherOptions) -> Windows.System.LauncherUIOptions: ...
    @winrt_mixinmethod
    def get_PreferredApplicationPackageFamilyName(self: Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreferredApplicationPackageFamilyName(self: Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredApplicationDisplayName(self: Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PreferredApplicationDisplayName(self: Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: Windows.System.ILauncherOptions) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: Windows.System.ILauncherOptions, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.System.ILauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentType(self: Windows.System.ILauncherOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreAppUriHandlers(self: Windows.System.ILauncherOptions3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreAppUriHandlers(self: Windows.System.ILauncherOptions3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LimitPickerToCurrentAppAndAppUriHandlers(self: Windows.System.ILauncherOptions4) -> Boolean: ...
    @winrt_mixinmethod
    def put_LimitPickerToCurrentAppAndAppUriHandlers(self: Windows.System.ILauncherOptions4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredRemainingView(self: Windows.System.ILauncherViewOptions) -> Windows.UI.ViewManagement.ViewSizePreference: ...
    @winrt_mixinmethod
    def put_DesiredRemainingView(self: Windows.System.ILauncherViewOptions, value: Windows.UI.ViewManagement.ViewSizePreference) -> Void: ...
    TargetApplicationPackageFamilyName = property(get_TargetApplicationPackageFamilyName, put_TargetApplicationPackageFamilyName)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, put_NeighboringFilesQuery)
    TreatAsUntrusted = property(get_TreatAsUntrusted, put_TreatAsUntrusted)
    DisplayApplicationPicker = property(get_DisplayApplicationPicker, put_DisplayApplicationPicker)
    UI = property(get_UI, None)
    PreferredApplicationPackageFamilyName = property(get_PreferredApplicationPackageFamilyName, put_PreferredApplicationPackageFamilyName)
    PreferredApplicationDisplayName = property(get_PreferredApplicationDisplayName, put_PreferredApplicationDisplayName)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    ContentType = property(get_ContentType, put_ContentType)
    IgnoreAppUriHandlers = property(get_IgnoreAppUriHandlers, put_IgnoreAppUriHandlers)
    LimitPickerToCurrentAppAndAppUriHandlers = property(get_LimitPickerToCurrentAppAndAppUriHandlers, put_LimitPickerToCurrentAppAndAppUriHandlers)
    DesiredRemainingView = property(get_DesiredRemainingView, put_DesiredRemainingView)
class LauncherUIOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.LauncherUIOptions'
    @winrt_mixinmethod
    def get_InvocationPoint(self: Windows.System.ILauncherUIOptions) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def put_InvocationPoint(self: Windows.System.ILauncherUIOptions, value: Windows.Foundation.IReference[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionRect(self: Windows.System.ILauncherUIOptions) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_SelectionRect(self: Windows.System.ILauncherUIOptions, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredPlacement(self: Windows.System.ILauncherUIOptions) -> Windows.UI.Popups.Placement: ...
    @winrt_mixinmethod
    def put_PreferredPlacement(self: Windows.System.ILauncherUIOptions, value: Windows.UI.Popups.Placement) -> Void: ...
    InvocationPoint = property(get_InvocationPoint, put_InvocationPoint)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
    PreferredPlacement = property(get_PreferredPlacement, put_PreferredPlacement)
class MemoryManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.MemoryManager'
    @winrt_classmethod
    def get_ExpectedAppMemoryUsageLimit(cls: Windows.System.IMemoryManagerStatics4) -> UInt64: ...
    @winrt_classmethod
    def TrySetAppMemoryUsageLimit(cls: Windows.System.IMemoryManagerStatics3, value: UInt64) -> Boolean: ...
    @winrt_classmethod
    def GetAppMemoryReport(cls: Windows.System.IMemoryManagerStatics2) -> Windows.System.AppMemoryReport: ...
    @winrt_classmethod
    def GetProcessMemoryReport(cls: Windows.System.IMemoryManagerStatics2) -> Windows.System.ProcessMemoryReport: ...
    @winrt_classmethod
    def get_AppMemoryUsage(cls: Windows.System.IMemoryManagerStatics) -> UInt64: ...
    @winrt_classmethod
    def get_AppMemoryUsageLimit(cls: Windows.System.IMemoryManagerStatics) -> UInt64: ...
    @winrt_classmethod
    def get_AppMemoryUsageLevel(cls: Windows.System.IMemoryManagerStatics) -> Windows.System.AppMemoryUsageLevel: ...
    @winrt_classmethod
    def add_AppMemoryUsageIncreased(cls: Windows.System.IMemoryManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageIncreased(cls: Windows.System.IMemoryManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_AppMemoryUsageDecreased(cls: Windows.System.IMemoryManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageDecreased(cls: Windows.System.IMemoryManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_AppMemoryUsageLimitChanging(cls: Windows.System.IMemoryManagerStatics, handler: Windows.Foundation.EventHandler[Windows.System.AppMemoryUsageLimitChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AppMemoryUsageLimitChanging(cls: Windows.System.IMemoryManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExpectedAppMemoryUsageLimit = property(get_ExpectedAppMemoryUsageLimit, None)
    AppMemoryUsage = property(get_AppMemoryUsage, None)
    AppMemoryUsageLimit = property(get_AppMemoryUsageLimit, None)
    AppMemoryUsageLevel = property(get_AppMemoryUsageLevel, None)
PowerState = Int32
PowerState_ConnectedStandby: PowerState = 0
PowerState_SleepS3: PowerState = 1
class ProcessLauncher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ProcessLauncher'
    @winrt_classmethod
    def RunToCompletionAsync(cls: Windows.System.IProcessLauncherStatics, fileName: WinRT_String, args: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.System.ProcessLauncherResult]: ...
    @winrt_classmethod
    def RunToCompletionAsyncWithOptions(cls: Windows.System.IProcessLauncherStatics, fileName: WinRT_String, args: WinRT_String, options: Windows.System.ProcessLauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.ProcessLauncherResult]: ...
class ProcessLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ProcessLauncherOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.System.ProcessLauncherOptions: ...
    @winrt_mixinmethod
    def get_StandardInput(self: Windows.System.IProcessLauncherOptions) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def put_StandardInput(self: Windows.System.IProcessLauncherOptions, value: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def get_StandardOutput(self: Windows.System.IProcessLauncherOptions) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def put_StandardOutput(self: Windows.System.IProcessLauncherOptions, value: Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_mixinmethod
    def get_StandardError(self: Windows.System.IProcessLauncherOptions) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def put_StandardError(self: Windows.System.IProcessLauncherOptions, value: Windows.Storage.Streams.IOutputStream) -> Void: ...
    @winrt_mixinmethod
    def get_WorkingDirectory(self: Windows.System.IProcessLauncherOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_WorkingDirectory(self: Windows.System.IProcessLauncherOptions, value: WinRT_String) -> Void: ...
    StandardInput = property(get_StandardInput, put_StandardInput)
    StandardOutput = property(get_StandardOutput, put_StandardOutput)
    StandardError = property(get_StandardError, put_StandardError)
    WorkingDirectory = property(get_WorkingDirectory, put_WorkingDirectory)
class ProcessLauncherResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ProcessLauncherResult'
    @winrt_mixinmethod
    def get_ExitCode(self: Windows.System.IProcessLauncherResult) -> UInt32: ...
    ExitCode = property(get_ExitCode, None)
class ProcessMemoryReport(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ProcessMemoryReport'
    @winrt_mixinmethod
    def get_PrivateWorkingSetUsage(self: Windows.System.IProcessMemoryReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalWorkingSetUsage(self: Windows.System.IProcessMemoryReport) -> UInt64: ...
    PrivateWorkingSetUsage = property(get_PrivateWorkingSetUsage, None)
    TotalWorkingSetUsage = property(get_TotalWorkingSetUsage, None)
ProcessorArchitecture = Int32
ProcessorArchitecture_X86: ProcessorArchitecture = 0
ProcessorArchitecture_Arm: ProcessorArchitecture = 5
ProcessorArchitecture_X64: ProcessorArchitecture = 9
ProcessorArchitecture_Neutral: ProcessorArchitecture = 11
ProcessorArchitecture_Arm64: ProcessorArchitecture = 12
ProcessorArchitecture_X86OnArm64: ProcessorArchitecture = 14
ProcessorArchitecture_Unknown: ProcessorArchitecture = 65535
class ProtocolForResultsOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ProtocolForResultsOperation'
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.System.IProtocolForResultsOperation, data: Windows.Foundation.Collections.ValueSet) -> Void: ...
RemoteLaunchUriStatus = Int32
RemoteLaunchUriStatus_Unknown: RemoteLaunchUriStatus = 0
RemoteLaunchUriStatus_Success: RemoteLaunchUriStatus = 1
RemoteLaunchUriStatus_AppUnavailable: RemoteLaunchUriStatus = 2
RemoteLaunchUriStatus_ProtocolUnavailable: RemoteLaunchUriStatus = 3
RemoteLaunchUriStatus_RemoteSystemUnavailable: RemoteLaunchUriStatus = 4
RemoteLaunchUriStatus_ValueSetTooLarge: RemoteLaunchUriStatus = 5
RemoteLaunchUriStatus_DeniedByLocalSystem: RemoteLaunchUriStatus = 6
RemoteLaunchUriStatus_DeniedByRemoteSystem: RemoteLaunchUriStatus = 7
class RemoteLauncher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteLauncher'
    @winrt_classmethod
    def LaunchUriAsync(cls: Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithOptionsAsync(cls: Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri, options: Windows.System.RemoteLauncherOptions) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
    @winrt_classmethod
    def LaunchUriWithDataAsync(cls: Windows.System.IRemoteLauncherStatics, remoteSystemConnectionRequest: Windows.System.RemoteSystems.RemoteSystemConnectionRequest, uri: Windows.Foundation.Uri, options: Windows.System.RemoteLauncherOptions, inputData: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.System.RemoteLaunchUriStatus]: ...
class RemoteLauncherOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteLauncherOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.System.RemoteLauncherOptions: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: Windows.System.IRemoteLauncherOptions) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: Windows.System.IRemoteLauncherOptions, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredAppIds(self: Windows.System.IRemoteLauncherOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    PreferredAppIds = property(get_PreferredAppIds, None)
ShutdownKind = Int32
ShutdownKind_Shutdown: ShutdownKind = 0
ShutdownKind_Restart: ShutdownKind = 1
class ShutdownManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.ShutdownManager'
    @winrt_classmethod
    def IsPowerStateSupported(cls: Windows.System.IShutdownManagerStatics2, powerState: Windows.System.PowerState) -> Boolean: ...
    @winrt_classmethod
    def EnterPowerState(cls: Windows.System.IShutdownManagerStatics2, powerState: Windows.System.PowerState) -> Void: ...
    @winrt_classmethod
    def EnterPowerStateWithTimeSpan(cls: Windows.System.IShutdownManagerStatics2, powerState: Windows.System.PowerState, wakeUpAfter: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def BeginShutdown(cls: Windows.System.IShutdownManagerStatics, shutdownKind: Windows.System.ShutdownKind, timeout: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def CancelShutdown(cls: Windows.System.IShutdownManagerStatics) -> Void: ...
SystemManagementContract: UInt32 = 458752
class TimeZoneSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.TimeZoneSettings'
    @winrt_classmethod
    def AutoUpdateTimeZoneAsync(cls: Windows.System.ITimeZoneSettingsStatics2, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.System.AutoUpdateTimeZoneStatus]: ...
    @winrt_classmethod
    def get_CurrentTimeZoneDisplayName(cls: Windows.System.ITimeZoneSettingsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SupportedTimeZoneDisplayNames(cls: Windows.System.ITimeZoneSettingsStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_CanChangeTimeZone(cls: Windows.System.ITimeZoneSettingsStatics) -> Boolean: ...
    @winrt_classmethod
    def ChangeTimeZoneByDisplayName(cls: Windows.System.ITimeZoneSettingsStatics, timeZoneDisplayName: WinRT_String) -> Void: ...
    CurrentTimeZoneDisplayName = property(get_CurrentTimeZoneDisplayName, None)
    SupportedTimeZoneDisplayNames = property(get_SupportedTimeZoneDisplayNames, None)
    CanChangeTimeZone = property(get_CanChangeTimeZone, None)
class User(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.User'
    @winrt_mixinmethod
    def get_NonRoamableId(self: Windows.System.IUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AuthenticationStatus(self: Windows.System.IUser) -> Windows.System.UserAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.System.IUser) -> Windows.System.UserType: ...
    @winrt_mixinmethod
    def GetPropertyAsync(self: Windows.System.IUser, value: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: Windows.System.IUser, values: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IPropertySet]: ...
    @winrt_mixinmethod
    def GetPictureAsync(self: Windows.System.IUser, desiredSize: Windows.System.UserPictureSize) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def CheckUserAgeConsentGroupAsync(self: Windows.System.IUser2, consentGroup: Windows.System.UserAgeConsentGroup) -> Windows.Foundation.IAsyncOperation[Windows.System.UserAgeConsentResult]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.IUserStatics2) -> Windows.System.User: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.System.IUserStatics) -> Windows.System.UserWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.System.IUserStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_classmethod
    def FindAllAsyncByType(cls: Windows.System.IUserStatics, type: Windows.System.UserType) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_classmethod
    def FindAllAsyncByTypeAndStatus(cls: Windows.System.IUserStatics, type: Windows.System.UserType, status: Windows.System.UserAuthenticationStatus) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.System.User]]: ...
    @winrt_classmethod
    def GetFromId(cls: Windows.System.IUserStatics, nonRoamableId: WinRT_String) -> Windows.System.User: ...
    NonRoamableId = property(get_NonRoamableId, None)
    AuthenticationStatus = property(get_AuthenticationStatus, None)
    Type = property(get_Type, None)
UserAgeConsentGroup = Int32
UserAgeConsentGroup_Child: UserAgeConsentGroup = 0
UserAgeConsentGroup_Minor: UserAgeConsentGroup = 1
UserAgeConsentGroup_Adult: UserAgeConsentGroup = 2
UserAgeConsentResult = Int32
UserAgeConsentResult_NotEnforced: UserAgeConsentResult = 0
UserAgeConsentResult_Included: UserAgeConsentResult = 1
UserAgeConsentResult_NotIncluded: UserAgeConsentResult = 2
UserAgeConsentResult_Unknown: UserAgeConsentResult = 3
UserAgeConsentResult_Ambiguous: UserAgeConsentResult = 4
UserAuthenticationStatus = Int32
UserAuthenticationStatus_Unauthenticated: UserAuthenticationStatus = 0
UserAuthenticationStatus_LocallyAuthenticated: UserAuthenticationStatus = 1
UserAuthenticationStatus_RemotelyAuthenticated: UserAuthenticationStatus = 2
class UserAuthenticationStatusChangeDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserAuthenticationStatusChangeDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.System.IUserAuthenticationStatusChangeDeferral) -> Void: ...
class UserAuthenticationStatusChangingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserAuthenticationStatusChangingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.System.IUserAuthenticationStatusChangingEventArgs) -> Windows.System.UserAuthenticationStatusChangeDeferral: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.IUserAuthenticationStatusChangingEventArgs) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_NewStatus(self: Windows.System.IUserAuthenticationStatusChangingEventArgs) -> Windows.System.UserAuthenticationStatus: ...
    @winrt_mixinmethod
    def get_CurrentStatus(self: Windows.System.IUserAuthenticationStatusChangingEventArgs) -> Windows.System.UserAuthenticationStatus: ...
    User = property(get_User, None)
    NewStatus = property(get_NewStatus, None)
    CurrentStatus = property(get_CurrentStatus, None)
class UserChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserChangedEventArgs'
    @winrt_mixinmethod
    def get_User(self: Windows.System.IUserChangedEventArgs) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ChangedPropertyKinds(self: Windows.System.IUserChangedEventArgs2) -> Windows.Foundation.Collections.IVectorView[Windows.System.UserWatcherUpdateKind]: ...
    User = property(get_User, None)
    ChangedPropertyKinds = property(get_ChangedPropertyKinds, None)
class UserDeviceAssociation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserDeviceAssociation'
    @winrt_classmethod
    def FindUserFromDeviceId(cls: Windows.System.IUserDeviceAssociationStatics, deviceId: WinRT_String) -> Windows.System.User: ...
    @winrt_classmethod
    def add_UserDeviceAssociationChanged(cls: Windows.System.IUserDeviceAssociationStatics, handler: Windows.Foundation.EventHandler[Windows.System.UserDeviceAssociationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UserDeviceAssociationChanged(cls: Windows.System.IUserDeviceAssociationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class UserDeviceAssociationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserDeviceAssociationChangedEventArgs'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.System.IUserDeviceAssociationChangedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewUser(self: Windows.System.IUserDeviceAssociationChangedEventArgs) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_OldUser(self: Windows.System.IUserDeviceAssociationChangedEventArgs) -> Windows.System.User: ...
    DeviceId = property(get_DeviceId, None)
    NewUser = property(get_NewUser, None)
    OldUser = property(get_OldUser, None)
class UserPicker(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserPicker'
    @winrt_activatemethod
    def New(cls) -> Windows.System.UserPicker: ...
    @winrt_mixinmethod
    def get_AllowGuestAccounts(self: Windows.System.IUserPicker) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowGuestAccounts(self: Windows.System.IUserPicker, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedSelectedUser(self: Windows.System.IUserPicker) -> Windows.System.User: ...
    @winrt_mixinmethod
    def put_SuggestedSelectedUser(self: Windows.System.IUserPicker, value: Windows.System.User) -> Void: ...
    @winrt_mixinmethod
    def PickSingleUserAsync(self: Windows.System.IUserPicker) -> Windows.Foundation.IAsyncOperation[Windows.System.User]: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.System.IUserPickerStatics) -> Boolean: ...
    AllowGuestAccounts = property(get_AllowGuestAccounts, put_AllowGuestAccounts)
    SuggestedSelectedUser = property(get_SuggestedSelectedUser, put_SuggestedSelectedUser)
UserPictureSize = Int32
UserPictureSize_Size64x64: UserPictureSize = 0
UserPictureSize_Size208x208: UserPictureSize = 1
UserPictureSize_Size424x424: UserPictureSize = 2
UserPictureSize_Size1080x1080: UserPictureSize = 3
UserType = Int32
UserType_LocalUser: UserType = 0
UserType_RemoteUser: UserType = 1
UserType_LocalGuest: UserType = 2
UserType_RemoteGuest: UserType = 3
UserType_SystemManaged: UserType = 4
class UserWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserWatcher'
    @winrt_mixinmethod
    def get_Status(self: Windows.System.IUserWatcher) -> Windows.System.UserWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.System.IUserWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.System.IUserWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Added(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationStatusChanged(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationStatusChanged(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AuthenticationStatusChanging(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.System.UserAuthenticationStatusChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AuthenticationStatusChanging(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.System.IUserWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.System.UserWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.System.IUserWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
UserWatcherStatus = Int32
UserWatcherStatus_Created: UserWatcherStatus = 0
UserWatcherStatus_Started: UserWatcherStatus = 1
UserWatcherStatus_EnumerationCompleted: UserWatcherStatus = 2
UserWatcherStatus_Stopping: UserWatcherStatus = 3
UserWatcherStatus_Stopped: UserWatcherStatus = 4
UserWatcherStatus_Aborted: UserWatcherStatus = 5
UserWatcherUpdateKind = Int32
UserWatcherUpdateKind_Properties: UserWatcherUpdateKind = 0
UserWatcherUpdateKind_Picture: UserWatcherUpdateKind = 1
VirtualKey = Int32
VirtualKey_None: VirtualKey = 0
VirtualKey_LeftButton: VirtualKey = 1
VirtualKey_RightButton: VirtualKey = 2
VirtualKey_Cancel: VirtualKey = 3
VirtualKey_MiddleButton: VirtualKey = 4
VirtualKey_XButton1: VirtualKey = 5
VirtualKey_XButton2: VirtualKey = 6
VirtualKey_Back: VirtualKey = 8
VirtualKey_Tab: VirtualKey = 9
VirtualKey_Clear: VirtualKey = 12
VirtualKey_Enter: VirtualKey = 13
VirtualKey_Shift: VirtualKey = 16
VirtualKey_Control: VirtualKey = 17
VirtualKey_Menu: VirtualKey = 18
VirtualKey_Pause: VirtualKey = 19
VirtualKey_CapitalLock: VirtualKey = 20
VirtualKey_Kana: VirtualKey = 21
VirtualKey_Hangul: VirtualKey = 21
VirtualKey_ImeOn: VirtualKey = 22
VirtualKey_Junja: VirtualKey = 23
VirtualKey_Final: VirtualKey = 24
VirtualKey_Hanja: VirtualKey = 25
VirtualKey_Kanji: VirtualKey = 25
VirtualKey_ImeOff: VirtualKey = 26
VirtualKey_Escape: VirtualKey = 27
VirtualKey_Convert: VirtualKey = 28
VirtualKey_NonConvert: VirtualKey = 29
VirtualKey_Accept: VirtualKey = 30
VirtualKey_ModeChange: VirtualKey = 31
VirtualKey_Space: VirtualKey = 32
VirtualKey_PageUp: VirtualKey = 33
VirtualKey_PageDown: VirtualKey = 34
VirtualKey_End: VirtualKey = 35
VirtualKey_Home: VirtualKey = 36
VirtualKey_Left: VirtualKey = 37
VirtualKey_Up: VirtualKey = 38
VirtualKey_Right: VirtualKey = 39
VirtualKey_Down: VirtualKey = 40
VirtualKey_Select: VirtualKey = 41
VirtualKey_Print: VirtualKey = 42
VirtualKey_Execute: VirtualKey = 43
VirtualKey_Snapshot: VirtualKey = 44
VirtualKey_Insert: VirtualKey = 45
VirtualKey_Delete: VirtualKey = 46
VirtualKey_Help: VirtualKey = 47
VirtualKey_Number0: VirtualKey = 48
VirtualKey_Number1: VirtualKey = 49
VirtualKey_Number2: VirtualKey = 50
VirtualKey_Number3: VirtualKey = 51
VirtualKey_Number4: VirtualKey = 52
VirtualKey_Number5: VirtualKey = 53
VirtualKey_Number6: VirtualKey = 54
VirtualKey_Number7: VirtualKey = 55
VirtualKey_Number8: VirtualKey = 56
VirtualKey_Number9: VirtualKey = 57
VirtualKey_A: VirtualKey = 65
VirtualKey_B: VirtualKey = 66
VirtualKey_C: VirtualKey = 67
VirtualKey_D: VirtualKey = 68
VirtualKey_E: VirtualKey = 69
VirtualKey_F: VirtualKey = 70
VirtualKey_G: VirtualKey = 71
VirtualKey_H: VirtualKey = 72
VirtualKey_I: VirtualKey = 73
VirtualKey_J: VirtualKey = 74
VirtualKey_K: VirtualKey = 75
VirtualKey_L: VirtualKey = 76
VirtualKey_M: VirtualKey = 77
VirtualKey_N: VirtualKey = 78
VirtualKey_O: VirtualKey = 79
VirtualKey_P: VirtualKey = 80
VirtualKey_Q: VirtualKey = 81
VirtualKey_R: VirtualKey = 82
VirtualKey_S: VirtualKey = 83
VirtualKey_T: VirtualKey = 84
VirtualKey_U: VirtualKey = 85
VirtualKey_V: VirtualKey = 86
VirtualKey_W: VirtualKey = 87
VirtualKey_X: VirtualKey = 88
VirtualKey_Y: VirtualKey = 89
VirtualKey_Z: VirtualKey = 90
VirtualKey_LeftWindows: VirtualKey = 91
VirtualKey_RightWindows: VirtualKey = 92
VirtualKey_Application: VirtualKey = 93
VirtualKey_Sleep: VirtualKey = 95
VirtualKey_NumberPad0: VirtualKey = 96
VirtualKey_NumberPad1: VirtualKey = 97
VirtualKey_NumberPad2: VirtualKey = 98
VirtualKey_NumberPad3: VirtualKey = 99
VirtualKey_NumberPad4: VirtualKey = 100
VirtualKey_NumberPad5: VirtualKey = 101
VirtualKey_NumberPad6: VirtualKey = 102
VirtualKey_NumberPad7: VirtualKey = 103
VirtualKey_NumberPad8: VirtualKey = 104
VirtualKey_NumberPad9: VirtualKey = 105
VirtualKey_Multiply: VirtualKey = 106
VirtualKey_Add: VirtualKey = 107
VirtualKey_Separator: VirtualKey = 108
VirtualKey_Subtract: VirtualKey = 109
VirtualKey_Decimal: VirtualKey = 110
VirtualKey_Divide: VirtualKey = 111
VirtualKey_F1: VirtualKey = 112
VirtualKey_F2: VirtualKey = 113
VirtualKey_F3: VirtualKey = 114
VirtualKey_F4: VirtualKey = 115
VirtualKey_F5: VirtualKey = 116
VirtualKey_F6: VirtualKey = 117
VirtualKey_F7: VirtualKey = 118
VirtualKey_F8: VirtualKey = 119
VirtualKey_F9: VirtualKey = 120
VirtualKey_F10: VirtualKey = 121
VirtualKey_F11: VirtualKey = 122
VirtualKey_F12: VirtualKey = 123
VirtualKey_F13: VirtualKey = 124
VirtualKey_F14: VirtualKey = 125
VirtualKey_F15: VirtualKey = 126
VirtualKey_F16: VirtualKey = 127
VirtualKey_F17: VirtualKey = 128
VirtualKey_F18: VirtualKey = 129
VirtualKey_F19: VirtualKey = 130
VirtualKey_F20: VirtualKey = 131
VirtualKey_F21: VirtualKey = 132
VirtualKey_F22: VirtualKey = 133
VirtualKey_F23: VirtualKey = 134
VirtualKey_F24: VirtualKey = 135
VirtualKey_NavigationView: VirtualKey = 136
VirtualKey_NavigationMenu: VirtualKey = 137
VirtualKey_NavigationUp: VirtualKey = 138
VirtualKey_NavigationDown: VirtualKey = 139
VirtualKey_NavigationLeft: VirtualKey = 140
VirtualKey_NavigationRight: VirtualKey = 141
VirtualKey_NavigationAccept: VirtualKey = 142
VirtualKey_NavigationCancel: VirtualKey = 143
VirtualKey_NumberKeyLock: VirtualKey = 144
VirtualKey_Scroll: VirtualKey = 145
VirtualKey_LeftShift: VirtualKey = 160
VirtualKey_RightShift: VirtualKey = 161
VirtualKey_LeftControl: VirtualKey = 162
VirtualKey_RightControl: VirtualKey = 163
VirtualKey_LeftMenu: VirtualKey = 164
VirtualKey_RightMenu: VirtualKey = 165
VirtualKey_GoBack: VirtualKey = 166
VirtualKey_GoForward: VirtualKey = 167
VirtualKey_Refresh: VirtualKey = 168
VirtualKey_Stop: VirtualKey = 169
VirtualKey_Search: VirtualKey = 170
VirtualKey_Favorites: VirtualKey = 171
VirtualKey_GoHome: VirtualKey = 172
VirtualKey_GamepadA: VirtualKey = 195
VirtualKey_GamepadB: VirtualKey = 196
VirtualKey_GamepadX: VirtualKey = 197
VirtualKey_GamepadY: VirtualKey = 198
VirtualKey_GamepadRightShoulder: VirtualKey = 199
VirtualKey_GamepadLeftShoulder: VirtualKey = 200
VirtualKey_GamepadLeftTrigger: VirtualKey = 201
VirtualKey_GamepadRightTrigger: VirtualKey = 202
VirtualKey_GamepadDPadUp: VirtualKey = 203
VirtualKey_GamepadDPadDown: VirtualKey = 204
VirtualKey_GamepadDPadLeft: VirtualKey = 205
VirtualKey_GamepadDPadRight: VirtualKey = 206
VirtualKey_GamepadMenu: VirtualKey = 207
VirtualKey_GamepadView: VirtualKey = 208
VirtualKey_GamepadLeftThumbstickButton: VirtualKey = 209
VirtualKey_GamepadRightThumbstickButton: VirtualKey = 210
VirtualKey_GamepadLeftThumbstickUp: VirtualKey = 211
VirtualKey_GamepadLeftThumbstickDown: VirtualKey = 212
VirtualKey_GamepadLeftThumbstickRight: VirtualKey = 213
VirtualKey_GamepadLeftThumbstickLeft: VirtualKey = 214
VirtualKey_GamepadRightThumbstickUp: VirtualKey = 215
VirtualKey_GamepadRightThumbstickDown: VirtualKey = 216
VirtualKey_GamepadRightThumbstickRight: VirtualKey = 217
VirtualKey_GamepadRightThumbstickLeft: VirtualKey = 218
VirtualKeyModifiers = UInt32
VirtualKeyModifiers_None: VirtualKeyModifiers = 0
VirtualKeyModifiers_Control: VirtualKeyModifiers = 1
VirtualKeyModifiers_Menu: VirtualKeyModifiers = 2
VirtualKeyModifiers_Shift: VirtualKeyModifiers = 4
VirtualKeyModifiers_Windows: VirtualKeyModifiers = 8
make_head(_module, 'AppActivationResult')
make_head(_module, 'AppDiagnosticInfo')
make_head(_module, 'AppDiagnosticInfoWatcher')
make_head(_module, 'AppDiagnosticInfoWatcherEventArgs')
make_head(_module, 'AppExecutionStateChangeResult')
make_head(_module, 'AppMemoryReport')
make_head(_module, 'AppMemoryUsageLimitChangingEventArgs')
make_head(_module, 'AppResourceGroupBackgroundTaskReport')
make_head(_module, 'AppResourceGroupInfo')
make_head(_module, 'AppResourceGroupInfoWatcher')
make_head(_module, 'AppResourceGroupInfoWatcherEventArgs')
make_head(_module, 'AppResourceGroupInfoWatcherExecutionStateChangedEventArgs')
make_head(_module, 'AppResourceGroupMemoryReport')
make_head(_module, 'AppResourceGroupStateReport')
make_head(_module, 'AppUriHandlerHost')
make_head(_module, 'AppUriHandlerRegistration')
make_head(_module, 'AppUriHandlerRegistrationManager')
make_head(_module, 'DateTimeSettings')
make_head(_module, 'DispatcherQueue')
make_head(_module, 'DispatcherQueueController')
make_head(_module, 'DispatcherQueueHandler')
make_head(_module, 'DispatcherQueueShutdownStartingEventArgs')
make_head(_module, 'DispatcherQueueTimer')
make_head(_module, 'FolderLauncherOptions')
make_head(_module, 'IAppActivationResult')
make_head(_module, 'IAppDiagnosticInfo')
make_head(_module, 'IAppDiagnosticInfo2')
make_head(_module, 'IAppDiagnosticInfo3')
make_head(_module, 'IAppDiagnosticInfoStatics')
make_head(_module, 'IAppDiagnosticInfoStatics2')
make_head(_module, 'IAppDiagnosticInfoWatcher')
make_head(_module, 'IAppDiagnosticInfoWatcherEventArgs')
make_head(_module, 'IAppExecutionStateChangeResult')
make_head(_module, 'IAppMemoryReport')
make_head(_module, 'IAppMemoryReport2')
make_head(_module, 'IAppMemoryUsageLimitChangingEventArgs')
make_head(_module, 'IAppResourceGroupBackgroundTaskReport')
make_head(_module, 'IAppResourceGroupInfo')
make_head(_module, 'IAppResourceGroupInfo2')
make_head(_module, 'IAppResourceGroupInfoWatcher')
make_head(_module, 'IAppResourceGroupInfoWatcherEventArgs')
make_head(_module, 'IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs')
make_head(_module, 'IAppResourceGroupMemoryReport')
make_head(_module, 'IAppResourceGroupStateReport')
make_head(_module, 'IAppUriHandlerHost')
make_head(_module, 'IAppUriHandlerHost2')
make_head(_module, 'IAppUriHandlerHostFactory')
make_head(_module, 'IAppUriHandlerRegistration')
make_head(_module, 'IAppUriHandlerRegistration2')
make_head(_module, 'IAppUriHandlerRegistrationManager')
make_head(_module, 'IAppUriHandlerRegistrationManager2')
make_head(_module, 'IAppUriHandlerRegistrationManagerStatics')
make_head(_module, 'IAppUriHandlerRegistrationManagerStatics2')
make_head(_module, 'IDateTimeSettingsStatics')
make_head(_module, 'IDispatcherQueue')
make_head(_module, 'IDispatcherQueue2')
make_head(_module, 'IDispatcherQueueController')
make_head(_module, 'IDispatcherQueueControllerStatics')
make_head(_module, 'IDispatcherQueueShutdownStartingEventArgs')
make_head(_module, 'IDispatcherQueueStatics')
make_head(_module, 'IDispatcherQueueTimer')
make_head(_module, 'IFolderLauncherOptions')
make_head(_module, 'IKnownUserPropertiesStatics')
make_head(_module, 'IKnownUserPropertiesStatics2')
make_head(_module, 'ILaunchUriResult')
make_head(_module, 'ILauncherOptions')
make_head(_module, 'ILauncherOptions2')
make_head(_module, 'ILauncherOptions3')
make_head(_module, 'ILauncherOptions4')
make_head(_module, 'ILauncherStatics')
make_head(_module, 'ILauncherStatics2')
make_head(_module, 'ILauncherStatics3')
make_head(_module, 'ILauncherStatics4')
make_head(_module, 'ILauncherStatics5')
make_head(_module, 'ILauncherUIOptions')
make_head(_module, 'ILauncherViewOptions')
make_head(_module, 'IMemoryManagerStatics')
make_head(_module, 'IMemoryManagerStatics2')
make_head(_module, 'IMemoryManagerStatics3')
make_head(_module, 'IMemoryManagerStatics4')
make_head(_module, 'IProcessLauncherOptions')
make_head(_module, 'IProcessLauncherResult')
make_head(_module, 'IProcessLauncherStatics')
make_head(_module, 'IProcessMemoryReport')
make_head(_module, 'IProtocolForResultsOperation')
make_head(_module, 'IRemoteLauncherOptions')
make_head(_module, 'IRemoteLauncherStatics')
make_head(_module, 'IShutdownManagerStatics')
make_head(_module, 'IShutdownManagerStatics2')
make_head(_module, 'ITimeZoneSettingsStatics')
make_head(_module, 'ITimeZoneSettingsStatics2')
make_head(_module, 'IUser')
make_head(_module, 'IUser2')
make_head(_module, 'IUserAuthenticationStatusChangeDeferral')
make_head(_module, 'IUserAuthenticationStatusChangingEventArgs')
make_head(_module, 'IUserChangedEventArgs')
make_head(_module, 'IUserChangedEventArgs2')
make_head(_module, 'IUserDeviceAssociationChangedEventArgs')
make_head(_module, 'IUserDeviceAssociationStatics')
make_head(_module, 'IUserPicker')
make_head(_module, 'IUserPickerStatics')
make_head(_module, 'IUserStatics')
make_head(_module, 'IUserStatics2')
make_head(_module, 'IUserWatcher')
make_head(_module, 'KnownUserProperties')
make_head(_module, 'LaunchUriResult')
make_head(_module, 'Launcher')
make_head(_module, 'LauncherOptions')
make_head(_module, 'LauncherUIOptions')
make_head(_module, 'MemoryManager')
make_head(_module, 'ProcessLauncher')
make_head(_module, 'ProcessLauncherOptions')
make_head(_module, 'ProcessLauncherResult')
make_head(_module, 'ProcessMemoryReport')
make_head(_module, 'ProtocolForResultsOperation')
make_head(_module, 'RemoteLauncher')
make_head(_module, 'RemoteLauncherOptions')
make_head(_module, 'ShutdownManager')
make_head(_module, 'TimeZoneSettings')
make_head(_module, 'User')
make_head(_module, 'UserAuthenticationStatusChangeDeferral')
make_head(_module, 'UserAuthenticationStatusChangingEventArgs')
make_head(_module, 'UserChangedEventArgs')
make_head(_module, 'UserDeviceAssociation')
make_head(_module, 'UserDeviceAssociationChangedEventArgs')
make_head(_module, 'UserPicker')
make_head(_module, 'UserWatcher')
