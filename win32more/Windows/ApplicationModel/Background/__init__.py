from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.ApplicationModel.Calls.Background
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.Advertisement
import win32more.Windows.Devices.Bluetooth.Background
import win32more.Windows.Devices.Bluetooth.GenericAttributeProfile
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Devices.Sensors
import win32more.Windows.Devices.SmartCards
import win32more.Windows.Devices.Sms
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Sockets
import win32more.Windows.Storage
import win32more.Windows.Storage.Provider
import win32more.Windows.System
import win32more.Windows.UI.Notifications
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class ActivitySensorTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IActivitySensorTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ActivitySensorTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ActivitySensorTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IActivitySensorTriggerFactory, reportIntervalInMilliseconds: UInt32) -> win32more.Windows.ApplicationModel.Background.ActivitySensorTrigger: ...
    @winrt_mixinmethod
    def get_SubscribedActivities(self: win32more.Windows.ApplicationModel.Background.IActivitySensorTrigger) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: win32more.Windows.ApplicationModel.Background.IActivitySensorTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_SupportedActivities(self: win32more.Windows.ApplicationModel.Background.IActivitySensorTrigger) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: win32more.Windows.ApplicationModel.Background.IActivitySensorTrigger) -> UInt32: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, None)
    SubscribedActivities = property(get_SubscribedActivities, None)
    SupportedActivities = property(get_SupportedActivities, None)
class AlarmAccessStatus(Enum, Int32):
    Unspecified = 0
    AllowedWithWakeupCapability = 1
    AllowedWithoutWakeupCapability = 2
    Denied = 3
class AlarmApplicationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.AlarmApplicationManager'
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.AlarmAccessStatus]: ...
    @winrt_classmethod
    def GetAccessStatus(cls: win32more.Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics) -> win32more.Windows.ApplicationModel.Background.AlarmAccessStatus: ...
class AppBroadcastTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IAppBroadcastTrigger
    _classid_ = 'Windows.ApplicationModel.Background.AppBroadcastTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.AppBroadcastTrigger.CreateAppBroadcastTrigger(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateAppBroadcastTrigger(cls: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerFactory, providerKey: WinRT_String) -> win32more.Windows.ApplicationModel.Background.AppBroadcastTrigger: ...
    @winrt_mixinmethod
    def put_ProviderInfo(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTrigger, value: win32more.Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderInfo(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTrigger) -> win32more.Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo: ...
    ProviderInfo = property(get_ProviderInfo, put_ProviderInfo)
class AppBroadcastTriggerProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo
    _classid_ = 'Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo'
    @winrt_mixinmethod
    def put_DisplayNameResource(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LogoResource(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LogoResource(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VideoKeyFrameInterval(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_VideoKeyFrameInterval(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_MaxVideoBitrate(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoBitrate(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxVideoWidth(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoWidth(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxVideoHeight(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoHeight(self: win32more.Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    LogoResource = property(get_LogoResource, put_LogoResource)
    MaxVideoBitrate = property(get_MaxVideoBitrate, put_MaxVideoBitrate)
    MaxVideoHeight = property(get_MaxVideoHeight, put_MaxVideoHeight)
    MaxVideoWidth = property(get_MaxVideoWidth, put_MaxVideoWidth)
    VideoKeyFrameInterval = property(get_VideoKeyFrameInterval, put_VideoKeyFrameInterval)
class ApplicationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IApplicationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ApplicationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ApplicationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ApplicationTrigger: ...
    @winrt_mixinmethod
    def RequestAsync(self: win32more.Windows.ApplicationModel.Background.IApplicationTrigger) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: win32more.Windows.ApplicationModel.Background.IApplicationTrigger, arguments: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class ApplicationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IApplicationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Background.ApplicationTriggerDetails'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Background.IApplicationTriggerDetails) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
class ApplicationTriggerResult(Enum, Int32):
    Allowed = 0
    CurrentlyRunning = 1
    DisabledByPolicy = 2
    UnknownError = 3
class AppointmentStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IAppointmentStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger: ...
class BackgroundAccessRequestKind(Enum, Int32):
    AlwaysAllowed = 0
    AllowedSubjectToSystemPolicy = 1
class BackgroundAccessStatus(Enum, Int32):
    Unspecified = 0
    AllowedWithAlwaysOnRealTimeConnectivity = 1
    AllowedMayUseActiveRealTimeConnectivity = 2
    Denied = 3
    AlwaysAllowed = 4
    AllowedSubjectToSystemPolicy = 5
    DeniedBySystemPolicy = 6
    DeniedByUser = 7
BackgroundAlarmApplicationContract: UInt32 = 65536
class BackgroundExecutionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundExecutionManager'
    @winrt_classmethod
    def RequestAccessKindForModernStandbyAsync(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3, requestedAccess: win32more.Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetAccessStatusForModernStandby(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def GetAccessStatusForModernStandbyForApplication(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def RequestAccessKindAsync(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics2, requestedAccess: win32more.Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_classmethod
    def RequestAccessForApplicationAsync(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_classmethod
    def RemoveAccess(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> Void: ...
    @winrt_classmethod
    def RemoveAccessForApplication(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetAccessStatus(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def GetAccessStatusForApplication(cls: win32more.Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class _BackgroundTaskBuilder_Meta_(ComPtr.__class__):
    pass
class BackgroundTaskBuilder(ComPtr, metaclass=_BackgroundTaskBuilder_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskBuilder'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.BackgroundTaskBuilder.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskBuilder: ...
    @winrt_mixinmethod
    def put_TaskEntryPoint(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TaskEntryPoint(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetTrigger(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, trigger: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_mixinmethod
    def AddCondition(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, condition: win32more.Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> WinRT_String: ...
    @winrt_overload
    @winrt_mixinmethod
    def Register(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def put_CancelOnConditionLoss(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CancelOnConditionLoss(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsNetworkRequested(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsNetworkRequested(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder3) -> Boolean: ...
    @winrt_mixinmethod
    def get_TaskGroup(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder4) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def put_TaskGroup(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder4, value: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    @winrt_mixinmethod
    def SetTaskEntryPointClsid(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder5, TaskEntryPoint: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_AllowRunningTaskInStandby(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder6) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowRunningTaskInStandby(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Validate(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder6) -> Boolean: ...
    @Register.register
    @winrt_mixinmethod
    def Register(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilder6, taskName: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_classmethod
    def get_IsRunningTaskInStandbySupported(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskBuilderStatics) -> Boolean: ...
    AllowRunningTaskInStandby = property(get_AllowRunningTaskInStandby, put_AllowRunningTaskInStandby)
    CancelOnConditionLoss = property(get_CancelOnConditionLoss, put_CancelOnConditionLoss)
    IsNetworkRequested = property(get_IsNetworkRequested, put_IsNetworkRequested)
    Name = property(get_Name, put_Name)
    TaskEntryPoint = property(get_TaskEntryPoint, put_TaskEntryPoint)
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
    _BackgroundTaskBuilder_Meta_.IsRunningTaskInStandbySupported = property(get_IsRunningTaskInStandbySupported, None)
class BackgroundTaskCanceledEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6c4bac0-51f8-4c57-ac3f-156dd1680c4f}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, reason: win32more.Windows.ApplicationModel.Background.BackgroundTaskCancellationReason) -> Void: ...
class BackgroundTaskCancellationReason(Enum, Int32):
    Abort = 0
    Terminating = 1
    LoggingOff = 2
    ServicingUpdate = 3
    IdleTask = 4
    Uninstall = 5
    ConditionLoss = 6
    SystemPolicy = 7
    QuietHoursEntered = 8
    ExecutionTimeExceeded = 9
    ResourceRevocation = 10
    EnergySaver = 11
class BackgroundTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def CheckResult(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class BackgroundTaskCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b38e929-a086-46a7-a678-439135822bcf}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: win32more.Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs) -> Void: ...
class BackgroundTaskDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskDeferral
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskDeferral) -> Void: ...
class BackgroundTaskProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class BackgroundTaskProgressEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{46e0683c-8a88-4c99-804c-76897f6277a6}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: win32more.Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs) -> Void: ...
class _BackgroundTaskRegistration_Meta_(ComPtr.__class__):
    pass
class BackgroundTaskRegistration(ComPtr, metaclass=_BackgroundTaskRegistration_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskRegistration'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cancelTask: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Trigger(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration2) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_TaskGroup(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration3) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def get_TaskLastThrottledInStandbyTimestamp(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration4) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppEnergyUsePredictionContribution(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration4) -> Double: ...
    @winrt_classmethod
    def get_AllTaskGroups(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup]: ...
    @winrt_classmethod
    def GetTaskGroup(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2, groupId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_classmethod
    def get_AllTasks(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration]: ...
    AppEnergyUsePredictionContribution = property(get_AppEnergyUsePredictionContribution, None)
    Name = property(get_Name, None)
    TaskGroup = property(get_TaskGroup, None)
    TaskId = property(get_TaskId, None)
    TaskLastThrottledInStandbyTimestamp = property(get_TaskLastThrottledInStandbyTimestamp, None)
    Trigger = property(get_Trigger, None)
    _BackgroundTaskRegistration_Meta_.AllTaskGroups = property(get_AllTaskGroups, None)
    _BackgroundTaskRegistration_Meta_.AllTasks = property(get_AllTasks, None)
    Progress = event()
    Completed = event()
class BackgroundTaskRegistrationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup.CreateWithName(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory, id: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_factorymethod
    def CreateWithName(cls: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory, id: WinRT_String, name: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_BackgroundActivated(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup, win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BackgroundActivated(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllTasks(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration]: ...
    AllTasks = property(get_AllTasks, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    BackgroundActivated = event()
class BackgroundTaskThrottleCounter(Enum, Int32):
    All = 0
    Cpu = 1
    Network = 2
class _BackgroundWorkCost_Meta_(ComPtr.__class__):
    pass
class BackgroundWorkCost(ComPtr, metaclass=_BackgroundWorkCost_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundWorkCost'
    @winrt_classmethod
    def get_AppEnergyUseLevel(cls: win32more.Windows.ApplicationModel.Background.IBackgroundWorkCostStatics2) -> win32more.Windows.ApplicationModel.Background.EnergyUseLevel: ...
    @winrt_classmethod
    def get_AppEnergyUsePrediction(cls: win32more.Windows.ApplicationModel.Background.IBackgroundWorkCostStatics2) -> win32more.Windows.ApplicationModel.Background.EnergyUseLevel: ...
    @winrt_classmethod
    def get_AppLastThrottledInStandbyTimestamp(cls: win32more.Windows.ApplicationModel.Background.IBackgroundWorkCostStatics2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_classmethod
    def get_CurrentBackgroundWorkCost(cls: win32more.Windows.ApplicationModel.Background.IBackgroundWorkCostStatics) -> win32more.Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    _BackgroundWorkCost_Meta_.AppEnergyUseLevel = property(get_AppEnergyUseLevel, None)
    _BackgroundWorkCost_Meta_.AppEnergyUsePrediction = property(get_AppEnergyUsePrediction, None)
    _BackgroundWorkCost_Meta_.AppLastThrottledInStandbyTimestamp = property(get_AppLastThrottledInStandbyTimestamp, None)
    _BackgroundWorkCost_Meta_.CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost, None)
class BackgroundWorkCostValue(Enum, Int32):
    Low = 0
    Medium = 1
    High = 2
class BluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger: ...
    @winrt_mixinmethod
    def get_Advertisement(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_PreferredTransmitPowerLevelInDBm(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_PreferredTransmitPowerLevelInDBm(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_UseExtendedFormat(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExtendedFormat(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAnonymous(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeTransmitPowerLevel(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeTransmitPowerLevel(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedFormat = property(get_UseExtendedFormat, put_UseExtendedFormat)
class BluetoothLEAdvertisementWatcherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger: ...
    @winrt_mixinmethod
    def get_MinSamplingInterval(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSamplingInterval(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinOutOfRangeTimeout(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxOutOfRangeTimeout(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def put_SignalStrengthFilter(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger, value: win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementFilter(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def put_AdvertisementFilter(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AllowExtendedAdvertisements(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowExtendedAdvertisements(self: win32more.Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2, value: Boolean) -> Void: ...
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
class CachedFileUpdaterTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ICachedFileUpdaterTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CachedFileUpdaterTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.CachedFileUpdaterTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.CachedFileUpdaterTrigger: ...
class CachedFileUpdaterTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Background.CachedFileUpdaterTriggerDetails'
    @winrt_mixinmethod
    def get_UpdateTarget(self: win32more.Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> win32more.Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_mixinmethod
    def get_UpdateRequest(self: win32more.Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_mixinmethod
    def get_CanRequestUserInput(self: win32more.Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> Boolean: ...
    CanRequestUserInput = property(get_CanRequestUserInput, None)
    UpdateRequest = property(get_UpdateRequest, None)
    UpdateTarget = property(get_UpdateTarget, None)
class ChatMessageNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IChatMessageNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ChatMessageNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ChatMessageNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ChatMessageNotificationTrigger: ...
class ChatMessageReceivedNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IChatMessageReceivedNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger: ...
class CommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ICommunicationBlockingAppSetAsActiveTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger: ...
class ContactStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IContactStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ContactStoreNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ContactStoreNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ContactStoreNotificationTrigger: ...
class ContentPrefetchTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IContentPrefetchTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ContentPrefetchTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ContentPrefetchTrigger.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ContentPrefetchTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IContentPrefetchTriggerFactory, waitInterval: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_mixinmethod
    def get_WaitInterval(self: win32more.Windows.ApplicationModel.Background.IContentPrefetchTrigger) -> win32more.Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class ConversationalAgentTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ConversationalAgentTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ConversationalAgentTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ConversationalAgentTrigger: ...
class CustomSystemEventTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ICustomSystemEventTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CustomSystemEventTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.CustomSystemEventTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ICustomSystemEventTriggerFactory, triggerId: WinRT_String, recurrence: win32more.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence) -> win32more.Windows.ApplicationModel.Background.CustomSystemEventTrigger: ...
    @winrt_mixinmethod
    def get_TriggerId(self: win32more.Windows.ApplicationModel.Background.ICustomSystemEventTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recurrence(self: win32more.Windows.ApplicationModel.Background.ICustomSystemEventTrigger) -> win32more.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence: ...
    Recurrence = property(get_Recurrence, None)
    TriggerId = property(get_TriggerId, None)
class CustomSystemEventTriggerRecurrence(Enum, Int32):
    Once = 0
    Always = 1
class DeviceConnectionChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanMaintainConnection(self: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaintainConnection(self: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_MaintainConnection(self: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger, value: Boolean) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.ApplicationModel.Background.IDeviceConnectionChangeTriggerStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger]: ...
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    DeviceId = property(get_DeviceId, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
class DeviceManufacturerNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTriggerFactory, triggerQualifier: WinRT_String, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger: ...
    @winrt_mixinmethod
    def get_TriggerQualifier(self: win32more.Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OneShot(self: win32more.Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger) -> Boolean: ...
    OneShot = property(get_OneShot, None)
    TriggerQualifier = property(get_TriggerQualifier, None)
class DeviceServicingTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IDeviceServicingTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceServicingTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.DeviceServicingTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.DeviceServicingTrigger: ...
    @winrt_mixinmethod
    def RequestAsyncSimple(self: win32more.Windows.ApplicationModel.Background.IDeviceServicingTrigger, deviceId: WinRT_String, expectedDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: win32more.Windows.ApplicationModel.Background.IDeviceServicingTrigger, deviceId: WinRT_String, expectedDuration: win32more.Windows.Foundation.TimeSpan, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class DeviceTriggerResult(Enum, Int32):
    Allowed = 0
    DeniedByUser = 1
    DeniedBySystem = 2
    LowBattery = 3
class DeviceUseTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IDeviceUseTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceUseTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.DeviceUseTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.DeviceUseTrigger: ...
    @winrt_mixinmethod
    def RequestAsyncSimple(self: win32more.Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: win32more.Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class DeviceWatcherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IDeviceWatcherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceWatcherTrigger'
class EmailStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IEmailStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.EmailStoreNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.EmailStoreNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.EmailStoreNotificationTrigger: ...
class EnergyUseLevel(Enum, Int32):
    Unknown = 0
    UnderHalfOfBudget = 1
    OverHalfOfBudget = 2
    OverBudget = 3
class GattCharacteristicNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger.CreateWithEventTriggeringMode(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic) -> win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
    @winrt_factorymethod
    def CreateWithEventTriggeringMode(cls: win32more.Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory2, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, eventTriggeringMode: win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode) -> win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
    @winrt_mixinmethod
    def get_Characteristic(self: win32more.Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_mixinmethod
    def get_EventTriggeringMode(self: win32more.Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger2) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    Characteristic = property(get_Characteristic, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
class GattServiceProviderTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GattServiceProviderTrigger'
    @winrt_mixinmethod
    def get_TriggerId(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def put_AdvertisingParameters(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTrigger, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisingParameters(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTriggerStatics, triggerId: WinRT_String, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.GattServiceProviderTriggerResult]: ...
    AdvertisingParameters = property(get_AdvertisingParameters, put_AdvertisingParameters)
    Service = property(get_Service, None)
    TriggerId = property(get_TriggerId, None)
class GattServiceProviderTriggerResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult
    _classid_ = 'Windows.ApplicationModel.Background.GattServiceProviderTriggerResult'
    @winrt_mixinmethod
    def get_Trigger(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> win32more.Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    Trigger = property(get_Trigger, None)
class GeovisitTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IGeovisitTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GeovisitTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.GeovisitTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.GeovisitTrigger: ...
    @winrt_mixinmethod
    def get_MonitoringScope(self: win32more.Windows.ApplicationModel.Background.IGeovisitTrigger) -> win32more.Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_mixinmethod
    def put_MonitoringScope(self: win32more.Windows.ApplicationModel.Background.IGeovisitTrigger, value: win32more.Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class IActivitySensorTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IActivitySensorTrigger'
    _iid_ = Guid('{d0dd4342-e37b-4823-a5fe-6b31dfefdeb0}')
    @winrt_commethod(6)
    def get_SubscribedActivities(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(7)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SupportedActivities(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(9)
    def get_MinimumReportInterval(self) -> UInt32: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, None)
    SubscribedActivities = property(get_SubscribedActivities, None)
    SupportedActivities = property(get_SupportedActivities, None)
class IActivitySensorTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IActivitySensorTriggerFactory'
    _iid_ = Guid('{a72691c3-3837-44f7-831b-0132cc872bc3}')
    @winrt_commethod(6)
    def Create(self, reportIntervalInMilliseconds: UInt32) -> win32more.Windows.ApplicationModel.Background.ActivitySensorTrigger: ...
class IAlarmApplicationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics'
    _iid_ = Guid('{ca03fa3b-cce6-4de2-b09b-9628bd33bbbe}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.AlarmAccessStatus]: ...
    @winrt_commethod(7)
    def GetAccessStatus(self) -> win32more.Windows.ApplicationModel.Background.AlarmAccessStatus: ...
class IAppBroadcastTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppBroadcastTrigger'
    _iid_ = Guid('{74d4f496-8d37-44ec-9481-2a0b9854eb48}')
    @winrt_commethod(6)
    def put_ProviderInfo(self, value: win32more.Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo) -> Void: ...
    @winrt_commethod(7)
    def get_ProviderInfo(self) -> win32more.Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo: ...
    ProviderInfo = property(get_ProviderInfo, put_ProviderInfo)
class IAppBroadcastTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppBroadcastTriggerFactory'
    _iid_ = Guid('{280b9f44-22f4-4618-a02e-e7e411eb7238}')
    @winrt_commethod(6)
    def CreateAppBroadcastTrigger(self, providerKey: WinRT_String) -> win32more.Windows.ApplicationModel.Background.AppBroadcastTrigger: ...
class IAppBroadcastTriggerProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo'
    _iid_ = Guid('{f219352d-9de8-4420-9ce2-5eff8f17376b}')
    @winrt_commethod(6)
    def put_DisplayNameResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayNameResource(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_LogoResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_LogoResource(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_VideoKeyFrameInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def get_VideoKeyFrameInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_MaxVideoBitrate(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_MaxVideoBitrate(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_MaxVideoWidth(self, value: UInt32) -> Void: ...
    @winrt_commethod(15)
    def get_MaxVideoWidth(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_MaxVideoHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_MaxVideoHeight(self) -> UInt32: ...
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    LogoResource = property(get_LogoResource, put_LogoResource)
    MaxVideoBitrate = property(get_MaxVideoBitrate, put_MaxVideoBitrate)
    MaxVideoHeight = property(get_MaxVideoHeight, put_MaxVideoHeight)
    MaxVideoWidth = property(get_MaxVideoWidth, put_MaxVideoWidth)
    VideoKeyFrameInterval = property(get_VideoKeyFrameInterval, put_VideoKeyFrameInterval)
class IApplicationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IApplicationTrigger'
    _iid_ = Guid('{0b468630-9574-492c-9e93-1a3ae6335fe9}')
    @winrt_commethod(6)
    def RequestAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class IApplicationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IApplicationTriggerDetails'
    _iid_ = Guid('{97dc6ab2-2219-4a9e-9c5e-41d047f76e82}')
    @winrt_commethod(6)
    def get_Arguments(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
class IAppointmentStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppointmentStoreNotificationTrigger'
    _iid_ = Guid('{64d4040c-c201-42ad-aa2a-e21ba3425b6d}')
class IBackgroundCondition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundCondition'
    _iid_ = Guid('{ae48a1ee-8951-400a-8302-9c9c9a2a3a3b}')
class IBackgroundExecutionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics'
    _iid_ = Guid('{e826ea58-66a9-4d41-83d4-b4c18c87b846}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_commethod(7)
    def RequestAccessForApplicationAsync(self, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_commethod(8)
    def RemoveAccess(self) -> Void: ...
    @winrt_commethod(9)
    def RemoveAccessForApplication(self, applicationId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetAccessStatus(self) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_commethod(11)
    def GetAccessStatusForApplication(self, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class IBackgroundExecutionManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics2'
    _iid_ = Guid('{469b24ef-9bbb-4e18-999a-fd6512931be9}')
    @winrt_commethod(6)
    def RequestAccessKindAsync(self, requestedAccess: win32more.Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IBackgroundExecutionManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3'
    _iid_ = Guid('{98a5d3f6-5a25-5b6c-9192-d77a43dfedc4}')
    @winrt_commethod(6)
    def RequestAccessKindForModernStandbyAsync(self, requestedAccess: win32more.Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def GetAccessStatusForModernStandby(self) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_commethod(8)
    def GetAccessStatusForModernStandbyForApplication(self, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class IBackgroundTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTask'
    _iid_ = Guid('{7d13d534-fd12-43ce-8c22-ea1ff13c06df}')
    @winrt_commethod(6)
    def Run(self, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class IBackgroundTaskBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder'
    _iid_ = Guid('{0351550e-3e64-4572-a93a-84075a37c917}')
    @winrt_commethod(6)
    def put_TaskEntryPoint(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_TaskEntryPoint(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTrigger(self, trigger: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_commethod(9)
    def AddCondition(self, condition: win32more.Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_commethod(10)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def Register(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    Name = property(get_Name, put_Name)
    TaskEntryPoint = property(get_TaskEntryPoint, put_TaskEntryPoint)
class IBackgroundTaskBuilder2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder2'
    _iid_ = Guid('{6ae7cfb1-104f-406d-8db6-844a570f42bb}')
    @winrt_commethod(6)
    def put_CancelOnConditionLoss(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_CancelOnConditionLoss(self) -> Boolean: ...
    CancelOnConditionLoss = property(get_CancelOnConditionLoss, put_CancelOnConditionLoss)
class IBackgroundTaskBuilder3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder3'
    _iid_ = Guid('{28c74f4a-8ba9-4c09-a24f-19683e2c924c}')
    @winrt_commethod(6)
    def put_IsNetworkRequested(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsNetworkRequested(self) -> Boolean: ...
    IsNetworkRequested = property(get_IsNetworkRequested, put_IsNetworkRequested)
class IBackgroundTaskBuilder4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder4'
    _iid_ = Guid('{4755e522-cba2-4e35-bd16-a6da7f1c19aa}')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def put_TaskGroup(self, value: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
class IBackgroundTaskBuilder5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder5'
    _iid_ = Guid('{077103f6-99f5-4af4-bcad-4731d0330d43}')
    @winrt_commethod(6)
    def SetTaskEntryPointClsid(self, TaskEntryPoint: Guid) -> Void: ...
class IBackgroundTaskBuilder6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder6'
    _iid_ = Guid('{80b47b17-ec8b-5653-850b-7508a01f52e7}')
    @winrt_commethod(6)
    def get_AllowRunningTaskInStandby(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowRunningTaskInStandby(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def Validate(self) -> Boolean: ...
    @winrt_commethod(9)
    def Register(self, taskName: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    AllowRunningTaskInStandby = property(get_AllowRunningTaskInStandby, put_AllowRunningTaskInStandby)
class IBackgroundTaskBuilderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilderStatics'
    _iid_ = Guid('{d1eb5046-06f2-55b4-9bb7-a6457ebf3300}')
    @winrt_commethod(6)
    def get_IsRunningTaskInStandbySupported(self) -> Boolean: ...
    IsRunningTaskInStandbySupported = property(get_IsRunningTaskInStandbySupported, None)
class IBackgroundTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs'
    _iid_ = Guid('{565d25cf-f209-48f4-9967-2b184f7bfbf0}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def CheckResult(self) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class IBackgroundTaskDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskDeferral'
    _iid_ = Guid('{93cc156d-af27-4dd3-846e-24ee40cadd25}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IBackgroundTaskInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance'
    _iid_ = Guid('{865bda7a-21d8-4573-8f32-928a1b0641f6}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Task(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_commethod(8)
    def get_Progress(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_Progress(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_TriggerDetails(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def add_Canceled(self, cancelHandler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Canceled(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_SuspendedCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, put_Progress)
    SuspendedCount = property(get_SuspendedCount, None)
    Task = property(get_Task, None)
    TriggerDetails = property(get_TriggerDetails, None)
    Canceled = event()
class IBackgroundTaskInstance2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance2'
    _iid_ = Guid('{4f7d0176-0c76-4fb4-896d-5de1864122f6}')
    @winrt_commethod(6)
    def GetThrottleCount(self, counter: win32more.Windows.ApplicationModel.Background.BackgroundTaskThrottleCounter) -> UInt32: ...
class IBackgroundTaskInstance4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance4'
    _iid_ = Guid('{7f29f23c-aa04-4b08-97b0-06d874cdabf5}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IBackgroundTaskProgressEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs'
    _iid_ = Guid('{fb1468ac-8332-4d0a-9532-03eae684da31}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Progress(self) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class IBackgroundTaskRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration'
    _iid_ = Guid('{10654cc2-a26e-43bf-8c12-1fb40dbfbfa0}')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_Progress(self, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Progress(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Completed(self, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Completed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Unregister(self, cancelTask: Boolean) -> Void: ...
    Name = property(get_Name, None)
    TaskId = property(get_TaskId, None)
    Progress = event()
    Completed = event()
class IBackgroundTaskRegistration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration2'
    _iid_ = Guid('{6138c703-bb86-4112-afc3-7f939b166e3b}')
    @winrt_commethod(6)
    def get_Trigger(self) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    Trigger = property(get_Trigger, None)
class IBackgroundTaskRegistration3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration3'
    _iid_ = Guid('{fe338195-9423-4d8b-830d-b1dd2c7badd5}')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    TaskGroup = property(get_TaskGroup, None)
class IBackgroundTaskRegistration4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration4'
    _iid_ = Guid('{169c09c9-b0de-5576-a05b-a02067989879}')
    @winrt_commethod(6)
    def get_TaskLastThrottledInStandbyTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AppEnergyUsePredictionContribution(self) -> Double: ...
    AppEnergyUsePredictionContribution = property(get_AppEnergyUsePredictionContribution, None)
    TaskLastThrottledInStandbyTimestamp = property(get_TaskLastThrottledInStandbyTimestamp, None)
class IBackgroundTaskRegistrationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup'
    _iid_ = Guid('{2ab1919a-871b-4167-8a76-055cd67b5b23}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_BackgroundActivated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup, win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_BackgroundActivated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_AllTasks(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration]: ...
    AllTasks = property(get_AllTasks, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    BackgroundActivated = event()
class IBackgroundTaskRegistrationGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory'
    _iid_ = Guid('{83d92b69-44cf-4631-9740-03c7d8741bc5}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def CreateWithName(self, id: WinRT_String, name: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
class IBackgroundTaskRegistrationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics'
    _iid_ = Guid('{4c542f69-b000-42ba-a093-6a563c65e3f8}')
    @winrt_commethod(6)
    def get_AllTasks(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.ApplicationModel.Background.IBackgroundTaskRegistration]: ...
    AllTasks = property(get_AllTasks, None)
class IBackgroundTaskRegistrationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2'
    _iid_ = Guid('{174b671e-b20d-4fa9-ad9a-e93ad6c71e01}')
    @winrt_commethod(6)
    def get_AllTaskGroups(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup]: ...
    @winrt_commethod(7)
    def GetTaskGroup(self, groupId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    AllTaskGroups = property(get_AllTaskGroups, None)
class IBackgroundTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTrigger'
    _iid_ = Guid('{84b3a058-6027-4b87-9790-bdf3f757dbd7}')
class IBackgroundWorkCostStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundWorkCostStatics'
    _iid_ = Guid('{c740a662-c310-4b82-b3e3-3bcfb9e4c77d}')
    @winrt_commethod(6)
    def get_CurrentBackgroundWorkCost(self) -> win32more.Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost, None)
class IBackgroundWorkCostStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundWorkCostStatics2'
    _iid_ = Guid('{d868c976-81f6-57c8-ab2b-400b749e21d6}')
    @winrt_commethod(6)
    def get_AppEnergyUseLevel(self) -> win32more.Windows.ApplicationModel.Background.EnergyUseLevel: ...
    @winrt_commethod(7)
    def get_AppEnergyUsePrediction(self) -> win32more.Windows.ApplicationModel.Background.EnergyUseLevel: ...
    @winrt_commethod(8)
    def get_AppLastThrottledInStandbyTimestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    AppEnergyUseLevel = property(get_AppEnergyUseLevel, None)
    AppEnergyUsePrediction = property(get_AppEnergyUsePrediction, None)
    AppLastThrottledInStandbyTimestamp = property(get_AppLastThrottledInStandbyTimestamp, None)
class IBluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger'
    _iid_ = Guid('{ab3e2612-25d3-48ae-8724-d81877ae6129}')
    @winrt_commethod(6)
    def get_Advertisement(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    Advertisement = property(get_Advertisement, None)
class IBluetoothLEAdvertisementPublisherTrigger2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2'
    _iid_ = Guid('{aa28d064-38f4-597d-b597-4e55588c6503}')
    @winrt_commethod(6)
    def get_PreferredTransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_PreferredTransmitPowerLevelInDBm(self, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(8)
    def get_UseExtendedFormat(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_UseExtendedFormat(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsAnonymous(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAnonymous(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IncludeTransmitPowerLevel(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IncludeTransmitPowerLevel(self, value: Boolean) -> Void: ...
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedFormat = property(get_UseExtendedFormat, put_UseExtendedFormat)
class IBluetoothLEAdvertisementWatcherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger'
    _iid_ = Guid('{1aab1819-bce1-48eb-a827-59fb7cee52a6}')
    @winrt_commethod(6)
    def get_MinSamplingInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_MaxSamplingInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinOutOfRangeTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxOutOfRangeTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SignalStrengthFilter(self) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_commethod(11)
    def put_SignalStrengthFilter(self, value: win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_commethod(12)
    def get_AdvertisementFilter(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_commethod(13)
    def put_AdvertisementFilter(self, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
class IBluetoothLEAdvertisementWatcherTrigger2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2'
    _iid_ = Guid('{39b56799-eb39-5ab6-9932-aa9e4549604d}')
    @winrt_commethod(6)
    def get_AllowExtendedAdvertisements(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExtendedAdvertisements(self, value: Boolean) -> Void: ...
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class ICachedFileUpdaterTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICachedFileUpdaterTrigger'
    _iid_ = Guid('{e21caeeb-32f2-4d31-b553-b9e01bde37e0}')
class ICachedFileUpdaterTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails'
    _iid_ = Guid('{71838c13-1314-47b4-9597-dc7e248c17cc}')
    @winrt_commethod(6)
    def get_UpdateTarget(self) -> win32more.Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_commethod(7)
    def get_UpdateRequest(self) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_commethod(8)
    def get_CanRequestUserInput(self) -> Boolean: ...
    CanRequestUserInput = property(get_CanRequestUserInput, None)
    UpdateRequest = property(get_UpdateRequest, None)
    UpdateTarget = property(get_UpdateTarget, None)
class IChatMessageNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IChatMessageNotificationTrigger'
    _iid_ = Guid('{513b43bf-1d40-5c5d-78f5-c923fee3739e}')
class IChatMessageReceivedNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IChatMessageReceivedNotificationTrigger'
    _iid_ = Guid('{3ea3760e-baf5-4077-88e9-060cf6f0c6d5}')
class ICommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICommunicationBlockingAppSetAsActiveTrigger'
    _iid_ = Guid('{fb91f28a-16a5-486d-974c-7835a8477be2}')
class IContactStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContactStoreNotificationTrigger'
    _iid_ = Guid('{c833419b-4705-4571-9a16-06b997bf9c96}')
class IContentPrefetchTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContentPrefetchTrigger'
    _iid_ = Guid('{710627ee-04fa-440b-80c0-173202199e5d}')
    @winrt_commethod(6)
    def get_WaitInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class IContentPrefetchTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContentPrefetchTriggerFactory'
    _iid_ = Guid('{c2643eda-8a03-409e-b8c4-88814c28ccb6}')
    @winrt_commethod(6)
    def Create(self, waitInterval: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
class ICustomSystemEventTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICustomSystemEventTrigger'
    _iid_ = Guid('{f3596798-cf6b-4ef4-a0ca-29cf4a278c87}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Recurrence(self) -> win32more.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence: ...
    Recurrence = property(get_Recurrence, None)
    TriggerId = property(get_TriggerId, None)
class ICustomSystemEventTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICustomSystemEventTriggerFactory'
    _iid_ = Guid('{6bcb16c5-f2dc-41b2-9efd-b96bdcd13ced}')
    @winrt_commethod(6)
    def Create(self, triggerId: WinRT_String, recurrence: win32more.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence) -> win32more.Windows.ApplicationModel.Background.CustomSystemEventTrigger: ...
class IDeviceConnectionChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger'
    _iid_ = Guid('{90875e64-3cdd-4efb-ab1c-5b3b6a60ce34}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CanMaintainConnection(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MaintainConnection(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_MaintainConnection(self, value: Boolean) -> Void: ...
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    DeviceId = property(get_DeviceId, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
class IDeviceConnectionChangeTriggerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceConnectionChangeTriggerStatics'
    _iid_ = Guid('{c3ea246a-4efd-4498-aa60-a4e4e3b17ab9}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger]: ...
class IDeviceManufacturerNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger'
    _iid_ = Guid('{81278ab5-41ab-16da-86c2-7f7bf0912f5b}')
    @winrt_commethod(6)
    def get_TriggerQualifier(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    OneShot = property(get_OneShot, None)
    TriggerQualifier = property(get_TriggerQualifier, None)
class IDeviceManufacturerNotificationTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTriggerFactory'
    _iid_ = Guid('{7955de75-25bb-4153-a1a2-3029fcabb652}')
    @winrt_commethod(6)
    def Create(self, triggerQualifier: WinRT_String, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger: ...
class IDeviceServicingTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceServicingTrigger'
    _iid_ = Guid('{1ab217ad-6e34-49d3-9e6f-17f1b6dfa881}')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String, expectedDuration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, expectedDuration: win32more.Windows.Foundation.TimeSpan, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceUseTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceUseTrigger'
    _iid_ = Guid('{0da68011-334f-4d57-b6ec-6dca64b412e4}')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceWatcherTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceWatcherTrigger'
    _iid_ = Guid('{a4617fdd-8573-4260-befc-5bec89cb693d}')
class IEmailStoreNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IEmailStoreNotificationTrigger'
    _iid_ = Guid('{986d06da-47eb-4268-a4f2-f3f77188388a}')
class IGattCharacteristicNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger'
    _iid_ = Guid('{e25f8fc8-0696-474f-a732-f292b0cebc5d}')
    @winrt_commethod(6)
    def get_Characteristic(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    Characteristic = property(get_Characteristic, None)
class IGattCharacteristicNotificationTrigger2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger2'
    _iid_ = Guid('{9322a2c4-ae0e-42f2-b28c-f51372e69245}')
    @winrt_commethod(6)
    def get_EventTriggeringMode(self) -> win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    EventTriggeringMode = property(get_EventTriggeringMode, None)
class IGattCharacteristicNotificationTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory'
    _iid_ = Guid('{57ba1995-b143-4575-9f6b-fd59d93ace1a}')
    @winrt_commethod(6)
    def Create(self, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic) -> win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattCharacteristicNotificationTriggerFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory2'
    _iid_ = Guid('{5998e91f-8a53-4e9f-a32c-23cd33664cee}')
    @winrt_commethod(6)
    def CreateWithEventTriggeringMode(self, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, eventTriggeringMode: win32more.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode) -> win32more.Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattServiceProviderTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTrigger'
    _iid_ = Guid('{ddc6a3e9-1557-4bd8-8542-468aa0c696f6}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Service(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(8)
    def put_AdvertisingParameters(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_commethod(9)
    def get_AdvertisingParameters(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    AdvertisingParameters = property(get_AdvertisingParameters, put_AdvertisingParameters)
    Service = property(get_Service, None)
    TriggerId = property(get_TriggerId, None)
class IGattServiceProviderTriggerResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult'
    _iid_ = Guid('{3c4691b1-b198-4e84-bad4-cf4ad299ed3a}')
    @winrt_commethod(6)
    def get_Trigger(self) -> win32more.Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    Trigger = property(get_Trigger, None)
class IGattServiceProviderTriggerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTriggerStatics'
    _iid_ = Guid('{b413a36a-e294-4591-a5a6-64891a828153}')
    @winrt_commethod(6)
    def CreateAsync(self, triggerId: WinRT_String, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.GattServiceProviderTriggerResult]: ...
class IGeovisitTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGeovisitTrigger'
    _iid_ = Guid('{4818edaa-04e1-4127-9a4c-19351b8a80a4}')
    @winrt_commethod(6)
    def get_MonitoringScope(self) -> win32more.Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_commethod(7)
    def put_MonitoringScope(self, value: win32more.Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class ILocationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ILocationTrigger'
    _iid_ = Guid('{47666a1c-6877-481e-8026-ff7e14a811a0}')
    @winrt_commethod(6)
    def get_TriggerType(self) -> win32more.Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ILocationTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ILocationTriggerFactory'
    _iid_ = Guid('{1106bb07-ff69-4e09-aa8b-1384ea475e98}')
    @winrt_commethod(6)
    def Create(self, triggerType: win32more.Windows.ApplicationModel.Background.LocationTriggerType) -> win32more.Windows.ApplicationModel.Background.LocationTrigger: ...
class IMaintenanceTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMaintenanceTrigger'
    _iid_ = Guid('{68184c83-fc22-4ce5-841a-7239a9810047}')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class IMaintenanceTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMaintenanceTriggerFactory'
    _iid_ = Guid('{4b3ddb2e-97dd-4629-88b0-b06cf9482ae5}')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.MaintenanceTrigger: ...
class IMediaProcessingTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMediaProcessingTrigger'
    _iid_ = Guid('{9a95be65-8a52-4b30-9011-cf38040ea8b0}')
    @winrt_commethod(6)
    def RequestAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
class INetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorHotspotAuthenticationTrigger'
    _iid_ = Guid('{e756c791-3001-4de5-83c7-de61d88831d0}')
class INetworkOperatorNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger'
    _iid_ = Guid('{90089cc6-63cd-480c-95d1-6e6aef801e4a}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class INetworkOperatorNotificationTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorNotificationTriggerFactory'
    _iid_ = Guid('{0a223e00-27d7-4353-adb9-9265aaea579d}')
    @winrt_commethod(6)
    def Create(self, networkAccountId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
class IPhoneTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPhoneTrigger'
    _iid_ = Guid('{8dcfe99b-d4c5-49f1-b7d3-82e87a0e9dde}')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class IPhoneTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPhoneTriggerFactory'
    _iid_ = Guid('{a0d93cda-5fc1-48fb-a546-32262040157b}')
    @winrt_commethod(6)
    def Create(self, type: win32more.Windows.ApplicationModel.Calls.Background.PhoneTriggerType, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.PhoneTrigger: ...
class IPushNotificationTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPushNotificationTriggerFactory'
    _iid_ = Guid('{6dd8ed1b-458e-4fc2-bc2e-d5664f77ed19}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class IRcsEndUserMessageAvailableTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IRcsEndUserMessageAvailableTrigger'
    _iid_ = Guid('{986d0d6a-b2f6-467f-a978-a44091c11a66}')
class IRfcommConnectionTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IRfcommConnectionTrigger'
    _iid_ = Guid('{e8c4cae2-0b53-4464-9394-fd875654de64}')
    @winrt_commethod(6)
    def get_InboundConnection(self) -> win32more.Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation: ...
    @winrt_commethod(7)
    def get_OutboundConnection(self) -> win32more.Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation: ...
    @winrt_commethod(8)
    def get_AllowMultipleConnections(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AllowMultipleConnections(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ProtectionLevel(self) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(11)
    def put_ProtectionLevel(self, value: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    @winrt_commethod(12)
    def get_RemoteHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(13)
    def put_RemoteHostName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    AllowMultipleConnections = property(get_AllowMultipleConnections, put_AllowMultipleConnections)
    InboundConnection = property(get_InboundConnection, None)
    OutboundConnection = property(get_OutboundConnection, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
class ISecondaryAuthenticationFactorAuthenticationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISecondaryAuthenticationFactorAuthenticationTrigger'
    _iid_ = Guid('{f237f327-5181-4f24-96a7-700a4e5fac62}')
class ISensorDataThresholdTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISensorDataThresholdTrigger'
    _iid_ = Guid('{5bc0f372-d48b-4b7f-abec-15f9bacc12e2}')
class ISensorDataThresholdTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISensorDataThresholdTriggerFactory'
    _iid_ = Guid('{921fe675-7df0-4da3-97b3-e544ee857fe6}')
    @winrt_commethod(6)
    def Create(self, threshold: win32more.Windows.Devices.Sensors.ISensorDataThreshold) -> win32more.Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class ISmartCardTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmartCardTrigger'
    _iid_ = Guid('{f53bc5ac-84ca-4972-8ce9-e58f97b37a50}')
    @winrt_commethod(6)
    def get_TriggerType(self) -> win32more.Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ISmartCardTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmartCardTriggerFactory'
    _iid_ = Guid('{63bf54c3-89c1-4e00-a9d3-97c629269dad}')
    @winrt_commethod(6)
    def Create(self, triggerType: win32more.Windows.Devices.SmartCards.SmartCardTriggerType) -> win32more.Windows.ApplicationModel.Background.SmartCardTrigger: ...
class ISmsMessageReceivedTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmsMessageReceivedTriggerFactory'
    _iid_ = Guid('{ea3ad8c8-6ba4-4ab2-8d21-bc6b09c77564}')
    @winrt_commethod(6)
    def Create(self, filterRules: win32more.Windows.Devices.Sms.SmsFilterRules) -> win32more.Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class ISocketActivityTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISocketActivityTrigger'
    _iid_ = Guid('{a9bbf810-9dde-4f8a-83e3-b0e0e7a50d70}')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IStorageLibraryChangeTrackerTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryChangeTrackerTriggerFactory'
    _iid_ = Guid('{1eb0ffd0-5a85-499e-a888-824607124f50}')
    @winrt_commethod(6)
    def Create(self, tracker: win32more.Windows.Storage.StorageLibraryChangeTracker) -> win32more.Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class IStorageLibraryContentChangedTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryContentChangedTrigger'
    _iid_ = Guid('{1637e0a7-829c-45bc-929b-a1e7ea78d89b}')
class IStorageLibraryContentChangedTriggerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics'
    _iid_ = Guid('{7f9f1b39-5f90-4e12-914e-a7d8e0bbfb18}')
    @winrt_commethod(6)
    def Create(self, storageLibrary: win32more.Windows.Storage.StorageLibrary) -> win32more.Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_commethod(7)
    def CreateFromLibraries(self, storageLibraries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.StorageLibrary]) -> win32more.Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class ISystemCondition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemCondition'
    _iid_ = Guid('{c15fb476-89c5-420b-abd3-fb3030472128}')
    @winrt_commethod(6)
    def get_ConditionType(self) -> win32more.Windows.ApplicationModel.Background.SystemConditionType: ...
    ConditionType = property(get_ConditionType, None)
class ISystemConditionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemConditionFactory'
    _iid_ = Guid('{d269d1f1-05a7-49ae-87d7-16b2b8b9a553}')
    @winrt_commethod(6)
    def Create(self, conditionType: win32more.Windows.ApplicationModel.Background.SystemConditionType) -> win32more.Windows.ApplicationModel.Background.SystemCondition: ...
class ISystemTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemTrigger'
    _iid_ = Guid('{1d80c776-3748-4463-8d7e-276dc139ac1c}')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> win32more.Windows.ApplicationModel.Background.SystemTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class ISystemTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemTriggerFactory'
    _iid_ = Guid('{e80423d4-8791-4579-8126-87ec8aaa407a}')
    @winrt_commethod(6)
    def Create(self, triggerType: win32more.Windows.ApplicationModel.Background.SystemTriggerType, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.SystemTrigger: ...
class ITimeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ITimeTrigger'
    _iid_ = Guid('{656e5556-0b2a-4377-ba70-3b45a935547f}')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class ITimeTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ITimeTriggerFactory'
    _iid_ = Guid('{38c682fe-9b54-45e6-b2f3-269b87a6f734}')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.TimeTrigger: ...
class IToastNotificationActionTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IToastNotificationActionTriggerFactory'
    _iid_ = Guid('{b09dfc27-6480-4349-8125-97b3efaa0a3a}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class IToastNotificationHistoryChangedTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IToastNotificationHistoryChangedTriggerFactory'
    _iid_ = Guid('{81c6faad-8797-4785-81b4-b0cccb73d1d9}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class IUserNotificationChangedTriggerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IUserNotificationChangedTriggerFactory'
    _iid_ = Guid('{cad4436c-69ab-4e18-a48a-5ed2ac435957}')
    @winrt_commethod(6)
    def Create(self, notificationKinds: win32more.Windows.UI.Notifications.NotificationKinds) -> win32more.Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class LocationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ILocationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.LocationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.LocationTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ILocationTriggerFactory, triggerType: win32more.Windows.ApplicationModel.Background.LocationTriggerType) -> win32more.Windows.ApplicationModel.Background.LocationTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: win32more.Windows.ApplicationModel.Background.ILocationTrigger) -> win32more.Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class LocationTriggerType(Enum, Int32):
    Geofence = 0
class MaintenanceTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IMaintenanceTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MaintenanceTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MaintenanceTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IMaintenanceTriggerFactory, freshnessTime: UInt32, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.MaintenanceTrigger: ...
    @winrt_mixinmethod
    def get_FreshnessTime(self: win32more.Windows.ApplicationModel.Background.IMaintenanceTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_OneShot(self: win32more.Windows.ApplicationModel.Background.IMaintenanceTrigger) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class MediaProcessingTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IMediaProcessingTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MediaProcessingTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MediaProcessingTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MediaProcessingTrigger: ...
    @winrt_mixinmethod
    def RequestAsync(self: win32more.Windows.ApplicationModel.Background.IMediaProcessingTrigger) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: win32more.Windows.ApplicationModel.Background.IMediaProcessingTrigger, arguments: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
class MediaProcessingTriggerResult(Enum, Int32):
    Allowed = 0
    CurrentlyRunning = 1
    DisabledByPolicy = 2
    UnknownError = 3
class MobileBroadbandDeviceServiceNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger: ...
class MobileBroadbandPcoDataChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger: ...
class MobileBroadbandPinLockStateChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger: ...
class MobileBroadbandRadioStateChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger: ...
class MobileBroadbandRegistrationStateChangeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger: ...
class NetworkOperatorDataUsageTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger: ...
class NetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.INetworkOperatorHotspotAuthenticationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger: ...
class NetworkOperatorNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.INetworkOperatorNotificationTriggerFactory, networkAccountId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: win32more.Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class PaymentAppCanMakePaymentTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger: ...
class PhoneTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IPhoneTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PhoneTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.PhoneTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IPhoneTriggerFactory, type: win32more.Windows.ApplicationModel.Calls.Background.PhoneTriggerType, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.PhoneTrigger: ...
    @winrt_mixinmethod
    def get_OneShot(self: win32more.Windows.ApplicationModel.Background.IPhoneTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_TriggerType(self: win32more.Windows.ApplicationModel.Background.IPhoneTrigger) -> win32more.Windows.ApplicationModel.Calls.Background.PhoneTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class PushNotificationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PushNotificationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.PushNotificationTrigger.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.PushNotificationTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.PushNotificationTrigger: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IPushNotificationTriggerFactory, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class RcsEndUserMessageAvailableTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IRcsEndUserMessageAvailableTrigger
    _classid_ = 'Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger: ...
class RfcommConnectionTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger
    _classid_ = 'Windows.ApplicationModel.Background.RfcommConnectionTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.RfcommConnectionTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.RfcommConnectionTrigger: ...
    @winrt_mixinmethod
    def get_InboundConnection(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> win32more.Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation: ...
    @winrt_mixinmethod
    def get_OutboundConnection(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> win32more.Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation: ...
    @winrt_mixinmethod
    def get_AllowMultipleConnections(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowMultipleConnections(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> win32more.Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: win32more.Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_RemoteHostName(self: win32more.Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: win32more.Windows.Networking.HostName) -> Void: ...
    AllowMultipleConnections = property(get_AllowMultipleConnections, put_AllowMultipleConnections)
    InboundConnection = property(get_InboundConnection, None)
    OutboundConnection = property(get_OutboundConnection, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
class SecondaryAuthenticationFactorAuthenticationTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ISecondaryAuthenticationFactorAuthenticationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger: ...
class SensorDataThresholdTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ISensorDataThresholdTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SensorDataThresholdTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SensorDataThresholdTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ISensorDataThresholdTriggerFactory, threshold: win32more.Windows.Devices.Sensors.ISensorDataThreshold) -> win32more.Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class SmartCardTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ISmartCardTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SmartCardTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SmartCardTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ISmartCardTriggerFactory, triggerType: win32more.Windows.Devices.SmartCards.SmartCardTriggerType) -> win32more.Windows.ApplicationModel.Background.SmartCardTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: win32more.Windows.ApplicationModel.Background.ISmartCardTrigger) -> win32more.Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class SmsMessageReceivedTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SmsMessageReceivedTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SmsMessageReceivedTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ISmsMessageReceivedTriggerFactory, filterRules: win32more.Windows.Devices.Sms.SmsFilterRules) -> win32more.Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class SocketActivityTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SocketActivityTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SocketActivityTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.SocketActivityTrigger: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: win32more.Windows.ApplicationModel.Background.ISocketActivityTrigger) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class StorageLibraryChangeTrackerTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IStorageLibraryChangeTrackerTriggerFactory, tracker: win32more.Windows.Storage.StorageLibraryChangeTracker) -> win32more.Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class StorageLibraryContentChangedTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IStorageLibraryContentChangedTrigger
    _classid_ = 'Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger'
    @winrt_classmethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibrary: win32more.Windows.Storage.StorageLibrary) -> win32more.Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_classmethod
    def CreateFromLibraries(cls: win32more.Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibraries: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.StorageLibrary]) -> win32more.Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class SystemCondition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ISystemCondition
    _classid_ = 'Windows.ApplicationModel.Background.SystemCondition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SystemCondition.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ISystemConditionFactory, conditionType: win32more.Windows.ApplicationModel.Background.SystemConditionType) -> win32more.Windows.ApplicationModel.Background.SystemCondition: ...
    @winrt_mixinmethod
    def get_ConditionType(self: win32more.Windows.ApplicationModel.Background.ISystemCondition) -> win32more.Windows.ApplicationModel.Background.SystemConditionType: ...
    ConditionType = property(get_ConditionType, None)
class SystemConditionType(Enum, Int32):
    Invalid = 0
    UserPresent = 1
    UserNotPresent = 2
    InternetAvailable = 3
    InternetNotAvailable = 4
    SessionConnected = 5
    SessionDisconnected = 6
    FreeNetworkAvailable = 7
    BackgroundWorkCostNotHigh = 8
class SystemTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ISystemTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SystemTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.SystemTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ISystemTriggerFactory, triggerType: win32more.Windows.ApplicationModel.Background.SystemTriggerType, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.SystemTrigger: ...
    @winrt_mixinmethod
    def get_OneShot(self: win32more.Windows.ApplicationModel.Background.ISystemTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_TriggerType(self: win32more.Windows.ApplicationModel.Background.ISystemTrigger) -> win32more.Windows.ApplicationModel.Background.SystemTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class SystemTriggerType(Enum, Int32):
    Invalid = 0
    SmsReceived = 1
    UserPresent = 2
    UserAway = 3
    NetworkStateChange = 4
    ControlChannelReset = 5
    InternetAvailable = 6
    SessionConnected = 7
    ServicingComplete = 8
    LockScreenApplicationAdded = 9
    LockScreenApplicationRemoved = 10
    TimeZoneChange = 11
    OnlineIdConnectedStateChange = 12
    BackgroundWorkCostChange = 13
    PowerStateChange = 14
    DefaultSignInAccountChange = 15
class TetheringEntitlementCheckTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger: ...
class TimeTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.ITimeTrigger
    _classid_ = 'Windows.ApplicationModel.Background.TimeTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.TimeTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.ITimeTriggerFactory, freshnessTime: UInt32, oneShot: Boolean) -> win32more.Windows.ApplicationModel.Background.TimeTrigger: ...
    @winrt_mixinmethod
    def get_FreshnessTime(self: win32more.Windows.ApplicationModel.Background.ITimeTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_OneShot(self: win32more.Windows.ApplicationModel.Background.ITimeTrigger) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class ToastNotificationActionTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ToastNotificationActionTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ToastNotificationActionTrigger.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ToastNotificationActionTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IToastNotificationActionTriggerFactory, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class ToastNotificationHistoryChangedTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IToastNotificationHistoryChangedTriggerFactory, applicationId: WinRT_String) -> win32more.Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class UserNotificationChangedTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.UserNotificationChangedTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.UserNotificationChangedTrigger.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.Background.IUserNotificationChangedTriggerFactory, notificationKinds: win32more.Windows.UI.Notifications.NotificationKinds) -> win32more.Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class WiFiOnDemandHotspotConnectTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger: ...
class WiFiOnDemandHotspotUpdateMetadataTrigger(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger: ...


make_ready(__name__)
