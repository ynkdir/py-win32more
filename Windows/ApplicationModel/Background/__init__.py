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
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Background
import Windows.ApplicationModel.Calls.Background
import Windows.Devices.Bluetooth
import Windows.Devices.Bluetooth.Advertisement
import Windows.Devices.Bluetooth.Background
import Windows.Devices.Bluetooth.GenericAttributeProfile
import Windows.Devices.Geolocation
import Windows.Devices.Sensors
import Windows.Devices.SmartCards
import Windows.Devices.Sms
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Sockets
import Windows.Storage
import Windows.Storage.Provider
import Windows.System
import Windows.UI.Notifications
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ActivitySensorTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IActivitySensorTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ActivitySensorTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IActivitySensorTriggerFactory, reportIntervalInMilliseconds: UInt32) -> Windows.ApplicationModel.Background.ActivitySensorTrigger: ...
    @winrt_mixinmethod
    def get_SubscribedActivities(self: Windows.ApplicationModel.Background.IActivitySensorTrigger) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.ApplicationModel.Background.IActivitySensorTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_SupportedActivities(self: Windows.ApplicationModel.Background.IActivitySensorTrigger) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.ApplicationModel.Background.IActivitySensorTrigger) -> UInt32: ...
    SubscribedActivities = property(get_SubscribedActivities, None)
    ReportInterval = property(get_ReportInterval, None)
    SupportedActivities = property(get_SupportedActivities, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
AlarmAccessStatus = Int32
AlarmAccessStatus_Unspecified: AlarmAccessStatus = 0
AlarmAccessStatus_AllowedWithWakeupCapability: AlarmAccessStatus = 1
AlarmAccessStatus_AllowedWithoutWakeupCapability: AlarmAccessStatus = 2
AlarmAccessStatus_Denied: AlarmAccessStatus = 3
class AlarmApplicationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.AlarmApplicationManager'
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.AlarmAccessStatus]: ...
    @winrt_classmethod
    def GetAccessStatus(cls: Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics) -> Windows.ApplicationModel.Background.AlarmAccessStatus: ...
class AppBroadcastTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IAppBroadcastTrigger
    _classid_ = 'Windows.ApplicationModel.Background.AppBroadcastTrigger'
    @winrt_factorymethod
    def CreateAppBroadcastTrigger(cls: Windows.ApplicationModel.Background.IAppBroadcastTriggerFactory, providerKey: WinRT_String) -> Windows.ApplicationModel.Background.AppBroadcastTrigger: ...
    @winrt_mixinmethod
    def put_ProviderInfo(self: Windows.ApplicationModel.Background.IAppBroadcastTrigger, value: Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderInfo(self: Windows.ApplicationModel.Background.IAppBroadcastTrigger) -> Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo: ...
    ProviderInfo = property(get_ProviderInfo, put_ProviderInfo)
class AppBroadcastTriggerProviderInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo
    _classid_ = 'Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo'
    @winrt_mixinmethod
    def put_DisplayNameResource(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LogoResource(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LogoResource(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VideoKeyFrameInterval(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_VideoKeyFrameInterval(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_MaxVideoBitrate(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoBitrate(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxVideoWidth(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoWidth(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxVideoHeight(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxVideoHeight(self: Windows.ApplicationModel.Background.IAppBroadcastTriggerProviderInfo) -> UInt32: ...
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    LogoResource = property(get_LogoResource, put_LogoResource)
    VideoKeyFrameInterval = property(get_VideoKeyFrameInterval, put_VideoKeyFrameInterval)
    MaxVideoBitrate = property(get_MaxVideoBitrate, put_MaxVideoBitrate)
    MaxVideoWidth = property(get_MaxVideoWidth, put_MaxVideoWidth)
    MaxVideoHeight = property(get_MaxVideoHeight, put_MaxVideoHeight)
class ApplicationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IApplicationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ApplicationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ApplicationTrigger: ...
    @winrt_mixinmethod
    def RequestAsync(self: Windows.ApplicationModel.Background.IApplicationTrigger) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IApplicationTrigger, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class ApplicationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IApplicationTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Background.ApplicationTriggerDetails'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Background.IApplicationTriggerDetails) -> Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
ApplicationTriggerResult = Int32
ApplicationTriggerResult_Allowed: ApplicationTriggerResult = 0
ApplicationTriggerResult_CurrentlyRunning: ApplicationTriggerResult = 1
ApplicationTriggerResult_DisabledByPolicy: ApplicationTriggerResult = 2
ApplicationTriggerResult_UnknownError: ApplicationTriggerResult = 3
class AppointmentStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IAppointmentStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger: ...
BackgroundAccessRequestKind = Int32
BackgroundAccessRequestKind_AlwaysAllowed: BackgroundAccessRequestKind = 0
BackgroundAccessRequestKind_AllowedSubjectToSystemPolicy: BackgroundAccessRequestKind = 1
BackgroundAccessStatus = Int32
BackgroundAccessStatus_Unspecified: BackgroundAccessStatus = 0
BackgroundAccessStatus_AllowedWithAlwaysOnRealTimeConnectivity: BackgroundAccessStatus = 1
BackgroundAccessStatus_AllowedMayUseActiveRealTimeConnectivity: BackgroundAccessStatus = 2
BackgroundAccessStatus_Denied: BackgroundAccessStatus = 3
BackgroundAccessStatus_AlwaysAllowed: BackgroundAccessStatus = 4
BackgroundAccessStatus_AllowedSubjectToSystemPolicy: BackgroundAccessStatus = 5
BackgroundAccessStatus_DeniedBySystemPolicy: BackgroundAccessStatus = 6
BackgroundAccessStatus_DeniedByUser: BackgroundAccessStatus = 7
BackgroundAlarmApplicationContract: UInt32 = 65536
class BackgroundExecutionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundExecutionManager'
    @winrt_classmethod
    def RequestAccessKindForModernStandbyAsync(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetAccessStatusForModernStandby(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def GetAccessStatusForModernStandbyForApplication(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def RequestAccessKindAsync(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics2, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_classmethod
    def RequestAccessForApplicationAsync(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_classmethod
    def RemoveAccess(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> Void: ...
    @winrt_classmethod
    def RemoveAccessForApplication(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetAccessStatus(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_classmethod
    def GetAccessStatusForApplication(cls: Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class BackgroundTaskBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskBuilder
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskBuilder'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.BackgroundTaskBuilder: ...
    @winrt_mixinmethod
    def put_TaskEntryPoint(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TaskEntryPoint(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetTrigger(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder, trigger: Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_mixinmethod
    def AddCondition(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder, condition: Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> WinRT_String: ...
    @winrt_mixinmethod
    def Register(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def put_CancelOnConditionLoss(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CancelOnConditionLoss(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsNetworkRequested(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsNetworkRequested(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder3) -> Boolean: ...
    @winrt_mixinmethod
    def get_TaskGroup(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder4) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def put_TaskGroup(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder4, value: Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    @winrt_mixinmethod
    def SetTaskEntryPointClsid(self: Windows.ApplicationModel.Background.IBackgroundTaskBuilder5, TaskEntryPoint: Guid) -> Void: ...
    TaskEntryPoint = property(get_TaskEntryPoint, put_TaskEntryPoint)
    Name = property(get_Name, put_Name)
    CancelOnConditionLoss = property(get_CancelOnConditionLoss, put_CancelOnConditionLoss)
    IsNetworkRequested = property(get_IsNetworkRequested, put_IsNetworkRequested)
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
class BackgroundTaskCanceledEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler'
    _iid_ = Guid('{a6c4bac0-51f8-4c57-ac3f-156dd1680c4f}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.ApplicationModel.Background.IBackgroundTaskInstance, reason: Windows.ApplicationModel.Background.BackgroundTaskCancellationReason) -> Void: ...
BackgroundTaskCancellationReason = Int32
BackgroundTaskCancellationReason_Abort: BackgroundTaskCancellationReason = 0
BackgroundTaskCancellationReason_Terminating: BackgroundTaskCancellationReason = 1
BackgroundTaskCancellationReason_LoggingOff: BackgroundTaskCancellationReason = 2
BackgroundTaskCancellationReason_ServicingUpdate: BackgroundTaskCancellationReason = 3
BackgroundTaskCancellationReason_IdleTask: BackgroundTaskCancellationReason = 4
BackgroundTaskCancellationReason_Uninstall: BackgroundTaskCancellationReason = 5
BackgroundTaskCancellationReason_ConditionLoss: BackgroundTaskCancellationReason = 6
BackgroundTaskCancellationReason_SystemPolicy: BackgroundTaskCancellationReason = 7
BackgroundTaskCancellationReason_QuietHoursEntered: BackgroundTaskCancellationReason = 8
BackgroundTaskCancellationReason_ExecutionTimeExceeded: BackgroundTaskCancellationReason = 9
BackgroundTaskCancellationReason_ResourceRevocation: BackgroundTaskCancellationReason = 10
BackgroundTaskCancellationReason_EnergySaver: BackgroundTaskCancellationReason = 11
class BackgroundTaskCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def CheckResult(self: Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class BackgroundTaskCompletedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler'
    _iid_ = Guid('{5b38e929-a086-46a7-a678-439135822bcf}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs) -> Void: ...
class BackgroundTaskDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskDeferral
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Background.IBackgroundTaskDeferral) -> Void: ...
class BackgroundTaskProgressEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class BackgroundTaskProgressEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler'
    _iid_ = Guid('{46e0683c-8a88-4c99-804c-76897f6277a6}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs) -> Void: ...
class _BackgroundTaskRegistration_Meta_(ComPtr.__class__):
    pass
class BackgroundTaskRegistration(ComPtr, metaclass=_BackgroundTaskRegistration_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskRegistration
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskRegistration'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration, handler: Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration, handler: Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Unregister(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration, cancelTask: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Trigger(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration2) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_TaskGroup(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistration3) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_classmethod
    def get_AllTaskGroups(cls: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup]: ...
    @winrt_classmethod
    def GetTaskGroup(cls: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2, groupId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_classmethod
    def get_AllTasks(cls: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics) -> Windows.Foundation.Collections.IMapView[Guid, Windows.ApplicationModel.Background.IBackgroundTaskRegistration]: ...
    TaskId = property(get_TaskId, None)
    Name = property(get_Name, None)
    Trigger = property(get_Trigger, None)
    TaskGroup = property(get_TaskGroup, None)
    _BackgroundTaskRegistration_Meta_.AllTaskGroups = property(get_AllTaskGroups.__wrapped__, None)
    _BackgroundTaskRegistration_Meta_.AllTasks = property(get_AllTasks.__wrapped__, None)
class BackgroundTaskRegistrationGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory, id: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_factorymethod
    def CreateWithName(cls: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory, id: WinRT_String, name: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_BackgroundActivated(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup, Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BackgroundActivated(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllTasks(self: Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup) -> Windows.Foundation.Collections.IMapView[Guid, Windows.ApplicationModel.Background.BackgroundTaskRegistration]: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    AllTasks = property(get_AllTasks, None)
BackgroundTaskThrottleCounter = Int32
BackgroundTaskThrottleCounter_All: BackgroundTaskThrottleCounter = 0
BackgroundTaskThrottleCounter_Cpu: BackgroundTaskThrottleCounter = 1
BackgroundTaskThrottleCounter_Network: BackgroundTaskThrottleCounter = 2
class _BackgroundWorkCost_Meta_(ComPtr.__class__):
    pass
class BackgroundWorkCost(ComPtr, metaclass=_BackgroundWorkCost_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.BackgroundWorkCost'
    @winrt_classmethod
    def get_CurrentBackgroundWorkCost(cls: Windows.ApplicationModel.Background.IBackgroundWorkCostStatics) -> Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    _BackgroundWorkCost_Meta_.CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost.__wrapped__, None)
BackgroundWorkCostValue = Int32
BackgroundWorkCostValue_Low: BackgroundWorkCostValue = 0
BackgroundWorkCostValue_Medium: BackgroundWorkCostValue = 1
BackgroundWorkCostValue_High: BackgroundWorkCostValue = 2
class BluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger: ...
    @winrt_mixinmethod
    def get_Advertisement(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_PreferredTransmitPowerLevelInDBm(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_PreferredTransmitPowerLevelInDBm(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_UseExtendedFormat(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExtendedFormat(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAnonymous(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeTransmitPowerLevel(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeTransmitPowerLevel(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2, value: Boolean) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedFormat = property(get_UseExtendedFormat, put_UseExtendedFormat)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
class BluetoothLEAdvertisementWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger: ...
    @winrt_mixinmethod
    def get_MinSamplingInterval(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSamplingInterval(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinOutOfRangeTimeout(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxOutOfRangeTimeout(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def put_SignalStrengthFilter(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger, value: Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementFilter(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def put_AdvertisementFilter(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AllowExtendedAdvertisements(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowExtendedAdvertisements(self: Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2, value: Boolean) -> Void: ...
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class CachedFileUpdaterTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ICachedFileUpdaterTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CachedFileUpdaterTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.CachedFileUpdaterTrigger: ...
class CachedFileUpdaterTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Background.CachedFileUpdaterTriggerDetails'
    @winrt_mixinmethod
    def get_UpdateTarget(self: Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_mixinmethod
    def get_UpdateRequest(self: Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_mixinmethod
    def get_CanRequestUserInput(self: Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails) -> Boolean: ...
    UpdateTarget = property(get_UpdateTarget, None)
    UpdateRequest = property(get_UpdateRequest, None)
    CanRequestUserInput = property(get_CanRequestUserInput, None)
class ChatMessageNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IChatMessageNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ChatMessageNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ChatMessageNotificationTrigger: ...
class ChatMessageReceivedNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IChatMessageReceivedNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger: ...
class CommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ICommunicationBlockingAppSetAsActiveTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger: ...
class ContactStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IContactStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ContactStoreNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ContactStoreNotificationTrigger: ...
class ContentPrefetchTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IContentPrefetchTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ContentPrefetchTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IContentPrefetchTriggerFactory, waitInterval: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_mixinmethod
    def get_WaitInterval(self: Windows.ApplicationModel.Background.IContentPrefetchTrigger) -> Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class ConversationalAgentTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ConversationalAgentTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ConversationalAgentTrigger: ...
class CustomSystemEventTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ICustomSystemEventTrigger
    _classid_ = 'Windows.ApplicationModel.Background.CustomSystemEventTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ICustomSystemEventTriggerFactory, triggerId: WinRT_String, recurrence: Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence) -> Windows.ApplicationModel.Background.CustomSystemEventTrigger: ...
    @winrt_mixinmethod
    def get_TriggerId(self: Windows.ApplicationModel.Background.ICustomSystemEventTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recurrence(self: Windows.ApplicationModel.Background.ICustomSystemEventTrigger) -> Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence: ...
    TriggerId = property(get_TriggerId, None)
    Recurrence = property(get_Recurrence, None)
CustomSystemEventTriggerRecurrence = Int32
CustomSystemEventTriggerRecurrence_Once: CustomSystemEventTriggerRecurrence = 0
CustomSystemEventTriggerRecurrence_Always: CustomSystemEventTriggerRecurrence = 1
class DeviceConnectionChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanMaintainConnection(self: Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaintainConnection(self: Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_MaintainConnection(self: Windows.ApplicationModel.Background.IDeviceConnectionChangeTrigger, value: Boolean) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.ApplicationModel.Background.IDeviceConnectionChangeTriggerStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger]: ...
    DeviceId = property(get_DeviceId, None)
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
class DeviceManufacturerNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTriggerFactory, triggerQualifier: WinRT_String, oneShot: Boolean) -> Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger: ...
    @winrt_mixinmethod
    def get_TriggerQualifier(self: Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OneShot(self: Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger) -> Boolean: ...
    TriggerQualifier = property(get_TriggerQualifier, None)
    OneShot = property(get_OneShot, None)
class DeviceServicingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IDeviceServicingTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceServicingTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.DeviceServicingTrigger: ...
    @winrt_mixinmethod
    def RequestAsyncSimple(self: Windows.ApplicationModel.Background.IDeviceServicingTrigger, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IDeviceServicingTrigger, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
DeviceTriggerResult = Int32
DeviceTriggerResult_Allowed: DeviceTriggerResult = 0
DeviceTriggerResult_DeniedByUser: DeviceTriggerResult = 1
DeviceTriggerResult_DeniedBySystem: DeviceTriggerResult = 2
DeviceTriggerResult_LowBattery: DeviceTriggerResult = 3
class DeviceUseTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IDeviceUseTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceUseTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.DeviceUseTrigger: ...
    @winrt_mixinmethod
    def RequestAsyncSimple(self: Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class DeviceWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IDeviceWatcherTrigger
    _classid_ = 'Windows.ApplicationModel.Background.DeviceWatcherTrigger'
class EmailStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IEmailStoreNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.EmailStoreNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.EmailStoreNotificationTrigger: ...
class GattCharacteristicNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory2, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, eventTriggeringMode: Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
    @winrt_mixinmethod
    def get_Characteristic(self: Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    @winrt_mixinmethod
    def get_EventTriggeringMode(self: Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger2) -> Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    Characteristic = property(get_Characteristic, None)
    EventTriggeringMode = property(get_EventTriggeringMode, None)
class GattServiceProviderTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IGattServiceProviderTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GattServiceProviderTrigger'
    @winrt_mixinmethod
    def get_TriggerId(self: Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Service(self: Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def put_AdvertisingParameters(self: Windows.ApplicationModel.Background.IGattServiceProviderTrigger, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisingParameters(self: Windows.ApplicationModel.Background.IGattServiceProviderTrigger) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.ApplicationModel.Background.IGattServiceProviderTriggerStatics, triggerId: WinRT_String, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.GattServiceProviderTriggerResult]: ...
    TriggerId = property(get_TriggerId, None)
    Service = property(get_Service, None)
    AdvertisingParameters = property(get_AdvertisingParameters, put_AdvertisingParameters)
class GattServiceProviderTriggerResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult
    _classid_ = 'Windows.ApplicationModel.Background.GattServiceProviderTriggerResult'
    @winrt_mixinmethod
    def get_Trigger(self: Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Trigger = property(get_Trigger, None)
    Error = property(get_Error, None)
class GeovisitTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IGeovisitTrigger
    _classid_ = 'Windows.ApplicationModel.Background.GeovisitTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.GeovisitTrigger: ...
    @winrt_mixinmethod
    def get_MonitoringScope(self: Windows.ApplicationModel.Background.IGeovisitTrigger) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_mixinmethod
    def put_MonitoringScope(self: Windows.ApplicationModel.Background.IGeovisitTrigger, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class IActivitySensorTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IActivitySensorTrigger'
    _iid_ = Guid('{d0dd4342-e37b-4823-a5fe-6b31dfefdeb0}')
    @winrt_commethod(6)
    def get_SubscribedActivities(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(7)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SupportedActivities(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(9)
    def get_MinimumReportInterval(self) -> UInt32: ...
    SubscribedActivities = property(get_SubscribedActivities, None)
    ReportInterval = property(get_ReportInterval, None)
    SupportedActivities = property(get_SupportedActivities, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
class IActivitySensorTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IActivitySensorTriggerFactory'
    _iid_ = Guid('{a72691c3-3837-44f7-831b-0132cc872bc3}')
    @winrt_commethod(6)
    def Create(self, reportIntervalInMilliseconds: UInt32) -> Windows.ApplicationModel.Background.ActivitySensorTrigger: ...
class IAlarmApplicationManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAlarmApplicationManagerStatics'
    _iid_ = Guid('{ca03fa3b-cce6-4de2-b09b-9628bd33bbbe}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.AlarmAccessStatus]: ...
    @winrt_commethod(7)
    def GetAccessStatus(self) -> Windows.ApplicationModel.Background.AlarmAccessStatus: ...
class IAppBroadcastTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppBroadcastTrigger'
    _iid_ = Guid('{74d4f496-8d37-44ec-9481-2a0b9854eb48}')
    @winrt_commethod(6)
    def put_ProviderInfo(self, value: Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo) -> Void: ...
    @winrt_commethod(7)
    def get_ProviderInfo(self) -> Windows.ApplicationModel.Background.AppBroadcastTriggerProviderInfo: ...
    ProviderInfo = property(get_ProviderInfo, put_ProviderInfo)
class IAppBroadcastTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppBroadcastTriggerFactory'
    _iid_ = Guid('{280b9f44-22f4-4618-a02e-e7e411eb7238}')
    @winrt_commethod(6)
    def CreateAppBroadcastTrigger(self, providerKey: WinRT_String) -> Windows.ApplicationModel.Background.AppBroadcastTrigger: ...
class IAppBroadcastTriggerProviderInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def put_VideoKeyFrameInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def get_VideoKeyFrameInterval(self) -> Windows.Foundation.TimeSpan: ...
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
    VideoKeyFrameInterval = property(get_VideoKeyFrameInterval, put_VideoKeyFrameInterval)
    MaxVideoBitrate = property(get_MaxVideoBitrate, put_MaxVideoBitrate)
    MaxVideoWidth = property(get_MaxVideoWidth, put_MaxVideoWidth)
    MaxVideoHeight = property(get_MaxVideoHeight, put_MaxVideoHeight)
class IApplicationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IApplicationTrigger'
    _iid_ = Guid('{0b468630-9574-492c-9e93-1a3ae6335fe9}')
    @winrt_commethod(6)
    def RequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class IApplicationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IApplicationTriggerDetails'
    _iid_ = Guid('{97dc6ab2-2219-4a9e-9c5e-41d047f76e82}')
    @winrt_commethod(6)
    def get_Arguments(self) -> Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
class IAppointmentStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IAppointmentStoreNotificationTrigger'
    _iid_ = Guid('{64d4040c-c201-42ad-aa2a-e21ba3425b6d}')
class IBackgroundCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundCondition'
    _iid_ = Guid('{ae48a1ee-8951-400a-8302-9c9c9a2a3a3b}')
class IBackgroundExecutionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics'
    _iid_ = Guid('{e826ea58-66a9-4d41-83d4-b4c18c87b846}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_commethod(7)
    def RequestAccessForApplicationAsync(self, applicationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.BackgroundAccessStatus]: ...
    @winrt_commethod(8)
    def RemoveAccess(self) -> Void: ...
    @winrt_commethod(9)
    def RemoveAccessForApplication(self, applicationId: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetAccessStatus(self) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_commethod(11)
    def GetAccessStatusForApplication(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class IBackgroundExecutionManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics2'
    _iid_ = Guid('{469b24ef-9bbb-4e18-999a-fd6512931be9}')
    @winrt_commethod(6)
    def RequestAccessKindAsync(self, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IBackgroundExecutionManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundExecutionManagerStatics3'
    _iid_ = Guid('{98a5d3f6-5a25-5b6c-9192-d77a43dfedc4}')
    @winrt_commethod(6)
    def RequestAccessKindForModernStandbyAsync(self, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def GetAccessStatusForModernStandby(self) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_commethod(8)
    def GetAccessStatusForModernStandbyForApplication(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class IBackgroundTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTask'
    _iid_ = Guid('{7d13d534-fd12-43ce-8c22-ea1ff13c06df}')
    @winrt_commethod(6)
    def Run(self, taskInstance: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class IBackgroundTaskBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder'
    _iid_ = Guid('{0351550e-3e64-4572-a93a-84075a37c917}')
    @winrt_commethod(6)
    def put_TaskEntryPoint(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_TaskEntryPoint(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetTrigger(self, trigger: Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_commethod(9)
    def AddCondition(self, condition: Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_commethod(10)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def Register(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    TaskEntryPoint = property(get_TaskEntryPoint, put_TaskEntryPoint)
    Name = property(get_Name, put_Name)
class IBackgroundTaskBuilder2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder2'
    _iid_ = Guid('{6ae7cfb1-104f-406d-8db6-844a570f42bb}')
    @winrt_commethod(6)
    def put_CancelOnConditionLoss(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_CancelOnConditionLoss(self) -> Boolean: ...
    CancelOnConditionLoss = property(get_CancelOnConditionLoss, put_CancelOnConditionLoss)
class IBackgroundTaskBuilder3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder3'
    _iid_ = Guid('{28c74f4a-8ba9-4c09-a24f-19683e2c924c}')
    @winrt_commethod(6)
    def put_IsNetworkRequested(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsNetworkRequested(self) -> Boolean: ...
    IsNetworkRequested = property(get_IsNetworkRequested, put_IsNetworkRequested)
class IBackgroundTaskBuilder4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder4'
    _iid_ = Guid('{4755e522-cba2-4e35-bd16-a6da7f1c19aa}')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def put_TaskGroup(self, value: Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
class IBackgroundTaskBuilder5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskBuilder5'
    _iid_ = Guid('{077103f6-99f5-4af4-bcad-4731d0330d43}')
    @winrt_commethod(6)
    def SetTaskEntryPointClsid(self, TaskEntryPoint: Guid) -> Void: ...
class IBackgroundTaskCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs'
    _iid_ = Guid('{565d25cf-f209-48f4-9967-2b184f7bfbf0}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def CheckResult(self) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class IBackgroundTaskDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskDeferral'
    _iid_ = Guid('{93cc156d-af27-4dd3-846e-24ee40cadd25}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IBackgroundTaskInstance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance'
    _iid_ = Guid('{865bda7a-21d8-4573-8f32-928a1b0641f6}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Task(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_commethod(8)
    def get_Progress(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_Progress(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_TriggerDetails(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def add_Canceled(self, cancelHandler: Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Canceled(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_SuspendedCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def GetDeferral(self) -> Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    InstanceId = property(get_InstanceId, None)
    Task = property(get_Task, None)
    Progress = property(get_Progress, put_Progress)
    TriggerDetails = property(get_TriggerDetails, None)
    SuspendedCount = property(get_SuspendedCount, None)
class IBackgroundTaskInstance2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance2'
    _iid_ = Guid('{4f7d0176-0c76-4fb4-896d-5de1864122f6}')
    @winrt_commethod(6)
    def GetThrottleCount(self, counter: Windows.ApplicationModel.Background.BackgroundTaskThrottleCounter) -> UInt32: ...
class IBackgroundTaskInstance4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskInstance4'
    _iid_ = Guid('{7f29f23c-aa04-4b08-97b0-06d874cdabf5}')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IBackgroundTaskProgressEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs'
    _iid_ = Guid('{fb1468ac-8332-4d0a-9532-03eae684da31}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Progress(self) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class IBackgroundTaskRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration'
    _iid_ = Guid('{10654cc2-a26e-43bf-8c12-1fb40dbfbfa0}')
    @winrt_commethod(6)
    def get_TaskId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_Progress(self, handler: Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Progress(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Completed(self, handler: Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Completed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Unregister(self, cancelTask: Boolean) -> Void: ...
    TaskId = property(get_TaskId, None)
    Name = property(get_Name, None)
class IBackgroundTaskRegistration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration2'
    _iid_ = Guid('{6138c703-bb86-4112-afc3-7f939b166e3b}')
    @winrt_commethod(6)
    def get_Trigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    Trigger = property(get_Trigger, None)
class IBackgroundTaskRegistration3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistration3'
    _iid_ = Guid('{fe338195-9423-4d8b-830d-b1dd2c7badd5}')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    TaskGroup = property(get_TaskGroup, None)
class IBackgroundTaskRegistrationGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroup'
    _iid_ = Guid('{2ab1919a-871b-4167-8a76-055cd67b5b23}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_BackgroundActivated(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup, Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_BackgroundActivated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_AllTasks(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.ApplicationModel.Background.BackgroundTaskRegistration]: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    AllTasks = property(get_AllTasks, None)
class IBackgroundTaskRegistrationGroupFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationGroupFactory'
    _iid_ = Guid('{83d92b69-44cf-4631-9740-03c7d8741bc5}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def CreateWithName(self, id: WinRT_String, name: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
class IBackgroundTaskRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics'
    _iid_ = Guid('{4c542f69-b000-42ba-a093-6a563c65e3f8}')
    @winrt_commethod(6)
    def get_AllTasks(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.ApplicationModel.Background.IBackgroundTaskRegistration]: ...
    AllTasks = property(get_AllTasks, None)
class IBackgroundTaskRegistrationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTaskRegistrationStatics2'
    _iid_ = Guid('{174b671e-b20d-4fa9-ad9a-e93ad6c71e01}')
    @winrt_commethod(6)
    def get_AllTaskGroups(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup]: ...
    @winrt_commethod(7)
    def GetTaskGroup(self, groupId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    AllTaskGroups = property(get_AllTaskGroups, None)
class IBackgroundTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundTrigger'
    _iid_ = Guid('{84b3a058-6027-4b87-9790-bdf3f757dbd7}')
class IBackgroundWorkCostStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBackgroundWorkCostStatics'
    _iid_ = Guid('{c740a662-c310-4b82-b3e3-3bcfb9e4c77d}')
    @winrt_commethod(6)
    def get_CurrentBackgroundWorkCost(self) -> Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost, None)
class IBluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger'
    _iid_ = Guid('{ab3e2612-25d3-48ae-8724-d81877ae6129}')
    @winrt_commethod(6)
    def get_Advertisement(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    Advertisement = property(get_Advertisement, None)
class IBluetoothLEAdvertisementPublisherTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementPublisherTrigger2'
    _iid_ = Guid('{aa28d064-38f4-597d-b597-4e55588c6503}')
    @winrt_commethod(6)
    def get_PreferredTransmitPowerLevelInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_PreferredTransmitPowerLevelInDBm(self, value: Windows.Foundation.IReference[Int16]) -> Void: ...
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
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedFormat = property(get_UseExtendedFormat, put_UseExtendedFormat)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
class IBluetoothLEAdvertisementWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger'
    _iid_ = Guid('{1aab1819-bce1-48eb-a827-59fb7cee52a6}')
    @winrt_commethod(6)
    def get_MinSamplingInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_MaxSamplingInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinOutOfRangeTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxOutOfRangeTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SignalStrengthFilter(self) -> Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_commethod(11)
    def put_SignalStrengthFilter(self, value: Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_commethod(12)
    def get_AdvertisementFilter(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_commethod(13)
    def put_AdvertisementFilter(self, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
class IBluetoothLEAdvertisementWatcherTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IBluetoothLEAdvertisementWatcherTrigger2'
    _iid_ = Guid('{39b56799-eb39-5ab6-9932-aa9e4549604d}')
    @winrt_commethod(6)
    def get_AllowExtendedAdvertisements(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExtendedAdvertisements(self, value: Boolean) -> Void: ...
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class ICachedFileUpdaterTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICachedFileUpdaterTrigger'
    _iid_ = Guid('{e21caeeb-32f2-4d31-b553-b9e01bde37e0}')
class ICachedFileUpdaterTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICachedFileUpdaterTriggerDetails'
    _iid_ = Guid('{71838c13-1314-47b4-9597-dc7e248c17cc}')
    @winrt_commethod(6)
    def get_UpdateTarget(self) -> Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_commethod(7)
    def get_UpdateRequest(self) -> Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_commethod(8)
    def get_CanRequestUserInput(self) -> Boolean: ...
    UpdateTarget = property(get_UpdateTarget, None)
    UpdateRequest = property(get_UpdateRequest, None)
    CanRequestUserInput = property(get_CanRequestUserInput, None)
class IChatMessageNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IChatMessageNotificationTrigger'
    _iid_ = Guid('{513b43bf-1d40-5c5d-78f5-c923fee3739e}')
class IChatMessageReceivedNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IChatMessageReceivedNotificationTrigger'
    _iid_ = Guid('{3ea3760e-baf5-4077-88e9-060cf6f0c6d5}')
class ICommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICommunicationBlockingAppSetAsActiveTrigger'
    _iid_ = Guid('{fb91f28a-16a5-486d-974c-7835a8477be2}')
class IContactStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContactStoreNotificationTrigger'
    _iid_ = Guid('{c833419b-4705-4571-9a16-06b997bf9c96}')
class IContentPrefetchTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContentPrefetchTrigger'
    _iid_ = Guid('{710627ee-04fa-440b-80c0-173202199e5d}')
    @winrt_commethod(6)
    def get_WaitInterval(self) -> Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class IContentPrefetchTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IContentPrefetchTriggerFactory'
    _iid_ = Guid('{c2643eda-8a03-409e-b8c4-88814c28ccb6}')
    @winrt_commethod(6)
    def Create(self, waitInterval: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
class ICustomSystemEventTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICustomSystemEventTrigger'
    _iid_ = Guid('{f3596798-cf6b-4ef4-a0ca-29cf4a278c87}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Recurrence(self) -> Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence: ...
    TriggerId = property(get_TriggerId, None)
    Recurrence = property(get_Recurrence, None)
class ICustomSystemEventTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ICustomSystemEventTriggerFactory'
    _iid_ = Guid('{6bcb16c5-f2dc-41b2-9efd-b96bdcd13ced}')
    @winrt_commethod(6)
    def Create(self, triggerId: WinRT_String, recurrence: Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence) -> Windows.ApplicationModel.Background.CustomSystemEventTrigger: ...
class IDeviceConnectionChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    DeviceId = property(get_DeviceId, None)
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
class IDeviceConnectionChangeTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceConnectionChangeTriggerStatics'
    _iid_ = Guid('{c3ea246a-4efd-4498-aa60-a4e4e3b17ab9}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger]: ...
class IDeviceManufacturerNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTrigger'
    _iid_ = Guid('{81278ab5-41ab-16da-86c2-7f7bf0912f5b}')
    @winrt_commethod(6)
    def get_TriggerQualifier(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    TriggerQualifier = property(get_TriggerQualifier, None)
    OneShot = property(get_OneShot, None)
class IDeviceManufacturerNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceManufacturerNotificationTriggerFactory'
    _iid_ = Guid('{7955de75-25bb-4153-a1a2-3029fcabb652}')
    @winrt_commethod(6)
    def Create(self, triggerQualifier: WinRT_String, oneShot: Boolean) -> Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger: ...
class IDeviceServicingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceServicingTrigger'
    _iid_ = Guid('{1ab217ad-6e34-49d3-9e6f-17f1b6dfa881}')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceUseTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceUseTrigger'
    _iid_ = Guid('{0da68011-334f-4d57-b6ec-6dca64b412e4}')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IDeviceWatcherTrigger'
    _iid_ = Guid('{a4617fdd-8573-4260-befc-5bec89cb693d}')
class IEmailStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IEmailStoreNotificationTrigger'
    _iid_ = Guid('{986d06da-47eb-4268-a4f2-f3f77188388a}')
class IGattCharacteristicNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger'
    _iid_ = Guid('{e25f8fc8-0696-474f-a732-f292b0cebc5d}')
    @winrt_commethod(6)
    def get_Characteristic(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    Characteristic = property(get_Characteristic, None)
class IGattCharacteristicNotificationTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTrigger2'
    _iid_ = Guid('{9322a2c4-ae0e-42f2-b28c-f51372e69245}')
    @winrt_commethod(6)
    def get_EventTriggeringMode(self) -> Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    EventTriggeringMode = property(get_EventTriggeringMode, None)
class IGattCharacteristicNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory'
    _iid_ = Guid('{57ba1995-b143-4575-9f6b-fd59d93ace1a}')
    @winrt_commethod(6)
    def Create(self, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattCharacteristicNotificationTriggerFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattCharacteristicNotificationTriggerFactory2'
    _iid_ = Guid('{5998e91f-8a53-4e9f-a32c-23cd33664cee}')
    @winrt_commethod(6)
    def CreateWithEventTriggeringMode(self, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, eventTriggeringMode: Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattServiceProviderTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTrigger'
    _iid_ = Guid('{ddc6a3e9-1557-4bd8-8542-468aa0c696f6}')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Service(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(8)
    def put_AdvertisingParameters(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_commethod(9)
    def get_AdvertisingParameters(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    TriggerId = property(get_TriggerId, None)
    Service = property(get_Service, None)
    AdvertisingParameters = property(get_AdvertisingParameters, put_AdvertisingParameters)
class IGattServiceProviderTriggerResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult'
    _iid_ = Guid('{3c4691b1-b198-4e84-bad4-cf4ad299ed3a}')
    @winrt_commethod(6)
    def get_Trigger(self) -> Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Trigger = property(get_Trigger, None)
    Error = property(get_Error, None)
class IGattServiceProviderTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGattServiceProviderTriggerStatics'
    _iid_ = Guid('{b413a36a-e294-4591-a5a6-64891a828153}')
    @winrt_commethod(6)
    def CreateAsync(self, triggerId: WinRT_String, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.GattServiceProviderTriggerResult]: ...
class IGeovisitTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IGeovisitTrigger'
    _iid_ = Guid('{4818edaa-04e1-4127-9a4c-19351b8a80a4}')
    @winrt_commethod(6)
    def get_MonitoringScope(self) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_commethod(7)
    def put_MonitoringScope(self, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class ILocationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ILocationTrigger'
    _iid_ = Guid('{47666a1c-6877-481e-8026-ff7e14a811a0}')
    @winrt_commethod(6)
    def get_TriggerType(self) -> Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ILocationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ILocationTriggerFactory'
    _iid_ = Guid('{1106bb07-ff69-4e09-aa8b-1384ea475e98}')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.ApplicationModel.Background.LocationTriggerType) -> Windows.ApplicationModel.Background.LocationTrigger: ...
class IMaintenanceTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMaintenanceTrigger'
    _iid_ = Guid('{68184c83-fc22-4ce5-841a-7239a9810047}')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class IMaintenanceTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMaintenanceTriggerFactory'
    _iid_ = Guid('{4b3ddb2e-97dd-4629-88b0-b06cf9482ae5}')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.MaintenanceTrigger: ...
class IMediaProcessingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IMediaProcessingTrigger'
    _iid_ = Guid('{9a95be65-8a52-4b30-9011-cf38040ea8b0}')
    @winrt_commethod(6)
    def RequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
class INetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorHotspotAuthenticationTrigger'
    _iid_ = Guid('{e756c791-3001-4de5-83c7-de61d88831d0}')
class INetworkOperatorNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger'
    _iid_ = Guid('{90089cc6-63cd-480c-95d1-6e6aef801e4a}')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class INetworkOperatorNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.INetworkOperatorNotificationTriggerFactory'
    _iid_ = Guid('{0a223e00-27d7-4353-adb9-9265aaea579d}')
    @winrt_commethod(6)
    def Create(self, networkAccountId: WinRT_String) -> Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
class IPhoneTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPhoneTrigger'
    _iid_ = Guid('{8dcfe99b-d4c5-49f1-b7d3-82e87a0e9dde}')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> Windows.ApplicationModel.Calls.Background.PhoneTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class IPhoneTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPhoneTriggerFactory'
    _iid_ = Guid('{a0d93cda-5fc1-48fb-a546-32262040157b}')
    @winrt_commethod(6)
    def Create(self, type: Windows.ApplicationModel.Calls.Background.PhoneTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.PhoneTrigger: ...
class IPushNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IPushNotificationTriggerFactory'
    _iid_ = Guid('{6dd8ed1b-458e-4fc2-bc2e-d5664f77ed19}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class IRcsEndUserMessageAvailableTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IRcsEndUserMessageAvailableTrigger'
    _iid_ = Guid('{986d0d6a-b2f6-467f-a978-a44091c11a66}')
class IRfcommConnectionTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IRfcommConnectionTrigger'
    _iid_ = Guid('{e8c4cae2-0b53-4464-9394-fd875654de64}')
    @winrt_commethod(6)
    def get_InboundConnection(self) -> Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation: ...
    @winrt_commethod(7)
    def get_OutboundConnection(self) -> Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation: ...
    @winrt_commethod(8)
    def get_AllowMultipleConnections(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AllowMultipleConnections(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ProtectionLevel(self) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_commethod(11)
    def put_ProtectionLevel(self, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    @winrt_commethod(12)
    def get_RemoteHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(13)
    def put_RemoteHostName(self, value: Windows.Networking.HostName) -> Void: ...
    InboundConnection = property(get_InboundConnection, None)
    OutboundConnection = property(get_OutboundConnection, None)
    AllowMultipleConnections = property(get_AllowMultipleConnections, put_AllowMultipleConnections)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
class ISecondaryAuthenticationFactorAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISecondaryAuthenticationFactorAuthenticationTrigger'
    _iid_ = Guid('{f237f327-5181-4f24-96a7-700a4e5fac62}')
class ISensorDataThresholdTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISensorDataThresholdTrigger'
    _iid_ = Guid('{5bc0f372-d48b-4b7f-abec-15f9bacc12e2}')
class ISensorDataThresholdTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISensorDataThresholdTriggerFactory'
    _iid_ = Guid('{921fe675-7df0-4da3-97b3-e544ee857fe6}')
    @winrt_commethod(6)
    def Create(self, threshold: Windows.Devices.Sensors.ISensorDataThreshold) -> Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class ISmartCardTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmartCardTrigger'
    _iid_ = Guid('{f53bc5ac-84ca-4972-8ce9-e58f97b37a50}')
    @winrt_commethod(6)
    def get_TriggerType(self) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ISmartCardTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmartCardTriggerFactory'
    _iid_ = Guid('{63bf54c3-89c1-4e00-a9d3-97c629269dad}')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.Devices.SmartCards.SmartCardTriggerType) -> Windows.ApplicationModel.Background.SmartCardTrigger: ...
class ISmsMessageReceivedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISmsMessageReceivedTriggerFactory'
    _iid_ = Guid('{ea3ad8c8-6ba4-4ab2-8d21-bc6b09c77564}')
    @winrt_commethod(6)
    def Create(self, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class ISocketActivityTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISocketActivityTrigger'
    _iid_ = Guid('{a9bbf810-9dde-4f8a-83e3-b0e0e7a50d70}')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IStorageLibraryChangeTrackerTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryChangeTrackerTriggerFactory'
    _iid_ = Guid('{1eb0ffd0-5a85-499e-a888-824607124f50}')
    @winrt_commethod(6)
    def Create(self, tracker: Windows.Storage.StorageLibraryChangeTracker) -> Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class IStorageLibraryContentChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryContentChangedTrigger'
    _iid_ = Guid('{1637e0a7-829c-45bc-929b-a1e7ea78d89b}')
class IStorageLibraryContentChangedTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics'
    _iid_ = Guid('{7f9f1b39-5f90-4e12-914e-a7d8e0bbfb18}')
    @winrt_commethod(6)
    def Create(self, storageLibrary: Windows.Storage.StorageLibrary) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_commethod(7)
    def CreateFromLibraries(self, storageLibraries: Windows.Foundation.Collections.IIterable[Windows.Storage.StorageLibrary]) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class ISystemCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemCondition'
    _iid_ = Guid('{c15fb476-89c5-420b-abd3-fb3030472128}')
    @winrt_commethod(6)
    def get_ConditionType(self) -> Windows.ApplicationModel.Background.SystemConditionType: ...
    ConditionType = property(get_ConditionType, None)
class ISystemConditionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemConditionFactory'
    _iid_ = Guid('{d269d1f1-05a7-49ae-87d7-16b2b8b9a553}')
    @winrt_commethod(6)
    def Create(self, conditionType: Windows.ApplicationModel.Background.SystemConditionType) -> Windows.ApplicationModel.Background.SystemCondition: ...
class ISystemTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemTrigger'
    _iid_ = Guid('{1d80c776-3748-4463-8d7e-276dc139ac1c}')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> Windows.ApplicationModel.Background.SystemTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class ISystemTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ISystemTriggerFactory'
    _iid_ = Guid('{e80423d4-8791-4579-8126-87ec8aaa407a}')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.ApplicationModel.Background.SystemTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.SystemTrigger: ...
class ITimeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ITimeTrigger'
    _iid_ = Guid('{656e5556-0b2a-4377-ba70-3b45a935547f}')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class ITimeTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.ITimeTriggerFactory'
    _iid_ = Guid('{38c682fe-9b54-45e6-b2f3-269b87a6f734}')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.TimeTrigger: ...
class IToastNotificationActionTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IToastNotificationActionTriggerFactory'
    _iid_ = Guid('{b09dfc27-6480-4349-8125-97b3efaa0a3a}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class IToastNotificationHistoryChangedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IToastNotificationHistoryChangedTriggerFactory'
    _iid_ = Guid('{81c6faad-8797-4785-81b4-b0cccb73d1d9}')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class IUserNotificationChangedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Background.IUserNotificationChangedTriggerFactory'
    _iid_ = Guid('{cad4436c-69ab-4e18-a48a-5ed2ac435957}')
    @winrt_commethod(6)
    def Create(self, notificationKinds: Windows.UI.Notifications.NotificationKinds) -> Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class LocationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ILocationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.LocationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ILocationTriggerFactory, triggerType: Windows.ApplicationModel.Background.LocationTriggerType) -> Windows.ApplicationModel.Background.LocationTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.ILocationTrigger) -> Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
LocationTriggerType = Int32
LocationTriggerType_Geofence: LocationTriggerType = 0
class MaintenanceTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IMaintenanceTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MaintenanceTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IMaintenanceTriggerFactory, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.MaintenanceTrigger: ...
    @winrt_mixinmethod
    def get_FreshnessTime(self: Windows.ApplicationModel.Background.IMaintenanceTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_OneShot(self: Windows.ApplicationModel.Background.IMaintenanceTrigger) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class MediaProcessingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IMediaProcessingTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MediaProcessingTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MediaProcessingTrigger: ...
    @winrt_mixinmethod
    def RequestAsync(self: Windows.ApplicationModel.Background.IMediaProcessingTrigger) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IMediaProcessingTrigger, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
MediaProcessingTriggerResult = Int32
MediaProcessingTriggerResult_Allowed: MediaProcessingTriggerResult = 0
MediaProcessingTriggerResult_CurrentlyRunning: MediaProcessingTriggerResult = 1
MediaProcessingTriggerResult_DisabledByPolicy: MediaProcessingTriggerResult = 2
MediaProcessingTriggerResult_UnknownError: MediaProcessingTriggerResult = 3
class MobileBroadbandDeviceServiceNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger: ...
class MobileBroadbandPcoDataChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger: ...
class MobileBroadbandPinLockStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger: ...
class MobileBroadbandRadioStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger: ...
class MobileBroadbandRegistrationStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger: ...
class NetworkOperatorDataUsageTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger: ...
class NetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.INetworkOperatorHotspotAuthenticationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger: ...
class NetworkOperatorNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.INetworkOperatorNotificationTriggerFactory, networkAccountId: WinRT_String) -> Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class PaymentAppCanMakePaymentTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger: ...
class PhoneTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IPhoneTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PhoneTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IPhoneTriggerFactory, type: Windows.ApplicationModel.Calls.Background.PhoneTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.PhoneTrigger: ...
    @winrt_mixinmethod
    def get_OneShot(self: Windows.ApplicationModel.Background.IPhoneTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.IPhoneTrigger) -> Windows.ApplicationModel.Calls.Background.PhoneTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class PushNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.PushNotificationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IPushNotificationTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class RcsEndUserMessageAvailableTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IRcsEndUserMessageAvailableTrigger
    _classid_ = 'Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger: ...
class RfcommConnectionTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IRfcommConnectionTrigger
    _classid_ = 'Windows.ApplicationModel.Background.RfcommConnectionTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.RfcommConnectionTrigger: ...
    @winrt_mixinmethod
    def get_InboundConnection(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Windows.Devices.Bluetooth.Background.RfcommInboundConnectionInformation: ...
    @winrt_mixinmethod
    def get_OutboundConnection(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Windows.Devices.Bluetooth.Background.RfcommOutboundConnectionInformation: ...
    @winrt_mixinmethod
    def get_AllowMultipleConnections(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowMultipleConnections(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Windows.Networking.Sockets.SocketProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: Windows.Networking.Sockets.SocketProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_RemoteHostName(self: Windows.ApplicationModel.Background.IRfcommConnectionTrigger, value: Windows.Networking.HostName) -> Void: ...
    InboundConnection = property(get_InboundConnection, None)
    OutboundConnection = property(get_OutboundConnection, None)
    AllowMultipleConnections = property(get_AllowMultipleConnections, put_AllowMultipleConnections)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
class SecondaryAuthenticationFactorAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ISecondaryAuthenticationFactorAuthenticationTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger: ...
class SensorDataThresholdTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ISensorDataThresholdTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SensorDataThresholdTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISensorDataThresholdTriggerFactory, threshold: Windows.Devices.Sensors.ISensorDataThreshold) -> Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class SmartCardTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ISmartCardTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SmartCardTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISmartCardTriggerFactory, triggerType: Windows.Devices.SmartCards.SmartCardTriggerType) -> Windows.ApplicationModel.Background.SmartCardTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.ISmartCardTrigger) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class SmsMessageReceivedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SmsMessageReceivedTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISmsMessageReceivedTriggerFactory, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class SocketActivityTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SocketActivityTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.SocketActivityTrigger: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: Windows.ApplicationModel.Background.ISocketActivityTrigger) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class StorageLibraryChangeTrackerTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IStorageLibraryChangeTrackerTriggerFactory, tracker: Windows.Storage.StorageLibraryChangeTracker) -> Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class StorageLibraryContentChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IStorageLibraryContentChangedTrigger
    _classid_ = 'Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger'
    @winrt_classmethod
    def Create(cls: Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibrary: Windows.Storage.StorageLibrary) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_classmethod
    def CreateFromLibraries(cls: Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibraries: Windows.Foundation.Collections.IIterable[Windows.Storage.StorageLibrary]) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class SystemCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ISystemCondition
    _classid_ = 'Windows.ApplicationModel.Background.SystemCondition'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISystemConditionFactory, conditionType: Windows.ApplicationModel.Background.SystemConditionType) -> Windows.ApplicationModel.Background.SystemCondition: ...
    @winrt_mixinmethod
    def get_ConditionType(self: Windows.ApplicationModel.Background.ISystemCondition) -> Windows.ApplicationModel.Background.SystemConditionType: ...
    ConditionType = property(get_ConditionType, None)
SystemConditionType = Int32
SystemConditionType_Invalid: SystemConditionType = 0
SystemConditionType_UserPresent: SystemConditionType = 1
SystemConditionType_UserNotPresent: SystemConditionType = 2
SystemConditionType_InternetAvailable: SystemConditionType = 3
SystemConditionType_InternetNotAvailable: SystemConditionType = 4
SystemConditionType_SessionConnected: SystemConditionType = 5
SystemConditionType_SessionDisconnected: SystemConditionType = 6
SystemConditionType_FreeNetworkAvailable: SystemConditionType = 7
SystemConditionType_BackgroundWorkCostNotHigh: SystemConditionType = 8
class SystemTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ISystemTrigger
    _classid_ = 'Windows.ApplicationModel.Background.SystemTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISystemTriggerFactory, triggerType: Windows.ApplicationModel.Background.SystemTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.SystemTrigger: ...
    @winrt_mixinmethod
    def get_OneShot(self: Windows.ApplicationModel.Background.ISystemTrigger) -> Boolean: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.ISystemTrigger) -> Windows.ApplicationModel.Background.SystemTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
SystemTriggerType = Int32
SystemTriggerType_Invalid: SystemTriggerType = 0
SystemTriggerType_SmsReceived: SystemTriggerType = 1
SystemTriggerType_UserPresent: SystemTriggerType = 2
SystemTriggerType_UserAway: SystemTriggerType = 3
SystemTriggerType_NetworkStateChange: SystemTriggerType = 4
SystemTriggerType_ControlChannelReset: SystemTriggerType = 5
SystemTriggerType_InternetAvailable: SystemTriggerType = 6
SystemTriggerType_SessionConnected: SystemTriggerType = 7
SystemTriggerType_ServicingComplete: SystemTriggerType = 8
SystemTriggerType_LockScreenApplicationAdded: SystemTriggerType = 9
SystemTriggerType_LockScreenApplicationRemoved: SystemTriggerType = 10
SystemTriggerType_TimeZoneChange: SystemTriggerType = 11
SystemTriggerType_OnlineIdConnectedStateChange: SystemTriggerType = 12
SystemTriggerType_BackgroundWorkCostChange: SystemTriggerType = 13
SystemTriggerType_PowerStateChange: SystemTriggerType = 14
SystemTriggerType_DefaultSignInAccountChange: SystemTriggerType = 15
class TetheringEntitlementCheckTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger: ...
class TimeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.ITimeTrigger
    _classid_ = 'Windows.ApplicationModel.Background.TimeTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ITimeTriggerFactory, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.TimeTrigger: ...
    @winrt_mixinmethod
    def get_FreshnessTime(self: Windows.ApplicationModel.Background.ITimeTrigger) -> UInt32: ...
    @winrt_mixinmethod
    def get_OneShot(self: Windows.ApplicationModel.Background.ITimeTrigger) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class ToastNotificationActionTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ToastNotificationActionTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IToastNotificationActionTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class ToastNotificationHistoryChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IToastNotificationHistoryChangedTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class UserNotificationChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.UserNotificationChangedTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IUserNotificationChangedTriggerFactory, notificationKinds: Windows.UI.Notifications.NotificationKinds) -> Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class WiFiOnDemandHotspotConnectTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger: ...
class WiFiOnDemandHotspotUpdateMetadataTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Background.IBackgroundTrigger
    _classid_ = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger: ...
make_head(_module, 'ActivitySensorTrigger')
make_head(_module, 'AlarmApplicationManager')
make_head(_module, 'AppBroadcastTrigger')
make_head(_module, 'AppBroadcastTriggerProviderInfo')
make_head(_module, 'ApplicationTrigger')
make_head(_module, 'ApplicationTriggerDetails')
make_head(_module, 'AppointmentStoreNotificationTrigger')
make_head(_module, 'BackgroundExecutionManager')
make_head(_module, 'BackgroundTaskBuilder')
make_head(_module, 'BackgroundTaskCanceledEventHandler')
make_head(_module, 'BackgroundTaskCompletedEventArgs')
make_head(_module, 'BackgroundTaskCompletedEventHandler')
make_head(_module, 'BackgroundTaskDeferral')
make_head(_module, 'BackgroundTaskProgressEventArgs')
make_head(_module, 'BackgroundTaskProgressEventHandler')
make_head(_module, 'BackgroundTaskRegistration')
make_head(_module, 'BackgroundTaskRegistrationGroup')
make_head(_module, 'BackgroundWorkCost')
make_head(_module, 'BluetoothLEAdvertisementPublisherTrigger')
make_head(_module, 'BluetoothLEAdvertisementWatcherTrigger')
make_head(_module, 'CachedFileUpdaterTrigger')
make_head(_module, 'CachedFileUpdaterTriggerDetails')
make_head(_module, 'ChatMessageNotificationTrigger')
make_head(_module, 'ChatMessageReceivedNotificationTrigger')
make_head(_module, 'CommunicationBlockingAppSetAsActiveTrigger')
make_head(_module, 'ContactStoreNotificationTrigger')
make_head(_module, 'ContentPrefetchTrigger')
make_head(_module, 'ConversationalAgentTrigger')
make_head(_module, 'CustomSystemEventTrigger')
make_head(_module, 'DeviceConnectionChangeTrigger')
make_head(_module, 'DeviceManufacturerNotificationTrigger')
make_head(_module, 'DeviceServicingTrigger')
make_head(_module, 'DeviceUseTrigger')
make_head(_module, 'DeviceWatcherTrigger')
make_head(_module, 'EmailStoreNotificationTrigger')
make_head(_module, 'GattCharacteristicNotificationTrigger')
make_head(_module, 'GattServiceProviderTrigger')
make_head(_module, 'GattServiceProviderTriggerResult')
make_head(_module, 'GeovisitTrigger')
make_head(_module, 'IActivitySensorTrigger')
make_head(_module, 'IActivitySensorTriggerFactory')
make_head(_module, 'IAlarmApplicationManagerStatics')
make_head(_module, 'IAppBroadcastTrigger')
make_head(_module, 'IAppBroadcastTriggerFactory')
make_head(_module, 'IAppBroadcastTriggerProviderInfo')
make_head(_module, 'IApplicationTrigger')
make_head(_module, 'IApplicationTriggerDetails')
make_head(_module, 'IAppointmentStoreNotificationTrigger')
make_head(_module, 'IBackgroundCondition')
make_head(_module, 'IBackgroundExecutionManagerStatics')
make_head(_module, 'IBackgroundExecutionManagerStatics2')
make_head(_module, 'IBackgroundExecutionManagerStatics3')
make_head(_module, 'IBackgroundTask')
make_head(_module, 'IBackgroundTaskBuilder')
make_head(_module, 'IBackgroundTaskBuilder2')
make_head(_module, 'IBackgroundTaskBuilder3')
make_head(_module, 'IBackgroundTaskBuilder4')
make_head(_module, 'IBackgroundTaskBuilder5')
make_head(_module, 'IBackgroundTaskCompletedEventArgs')
make_head(_module, 'IBackgroundTaskDeferral')
make_head(_module, 'IBackgroundTaskInstance')
make_head(_module, 'IBackgroundTaskInstance2')
make_head(_module, 'IBackgroundTaskInstance4')
make_head(_module, 'IBackgroundTaskProgressEventArgs')
make_head(_module, 'IBackgroundTaskRegistration')
make_head(_module, 'IBackgroundTaskRegistration2')
make_head(_module, 'IBackgroundTaskRegistration3')
make_head(_module, 'IBackgroundTaskRegistrationGroup')
make_head(_module, 'IBackgroundTaskRegistrationGroupFactory')
make_head(_module, 'IBackgroundTaskRegistrationStatics')
make_head(_module, 'IBackgroundTaskRegistrationStatics2')
make_head(_module, 'IBackgroundTrigger')
make_head(_module, 'IBackgroundWorkCostStatics')
make_head(_module, 'IBluetoothLEAdvertisementPublisherTrigger')
make_head(_module, 'IBluetoothLEAdvertisementPublisherTrigger2')
make_head(_module, 'IBluetoothLEAdvertisementWatcherTrigger')
make_head(_module, 'IBluetoothLEAdvertisementWatcherTrigger2')
make_head(_module, 'ICachedFileUpdaterTrigger')
make_head(_module, 'ICachedFileUpdaterTriggerDetails')
make_head(_module, 'IChatMessageNotificationTrigger')
make_head(_module, 'IChatMessageReceivedNotificationTrigger')
make_head(_module, 'ICommunicationBlockingAppSetAsActiveTrigger')
make_head(_module, 'IContactStoreNotificationTrigger')
make_head(_module, 'IContentPrefetchTrigger')
make_head(_module, 'IContentPrefetchTriggerFactory')
make_head(_module, 'ICustomSystemEventTrigger')
make_head(_module, 'ICustomSystemEventTriggerFactory')
make_head(_module, 'IDeviceConnectionChangeTrigger')
make_head(_module, 'IDeviceConnectionChangeTriggerStatics')
make_head(_module, 'IDeviceManufacturerNotificationTrigger')
make_head(_module, 'IDeviceManufacturerNotificationTriggerFactory')
make_head(_module, 'IDeviceServicingTrigger')
make_head(_module, 'IDeviceUseTrigger')
make_head(_module, 'IDeviceWatcherTrigger')
make_head(_module, 'IEmailStoreNotificationTrigger')
make_head(_module, 'IGattCharacteristicNotificationTrigger')
make_head(_module, 'IGattCharacteristicNotificationTrigger2')
make_head(_module, 'IGattCharacteristicNotificationTriggerFactory')
make_head(_module, 'IGattCharacteristicNotificationTriggerFactory2')
make_head(_module, 'IGattServiceProviderTrigger')
make_head(_module, 'IGattServiceProviderTriggerResult')
make_head(_module, 'IGattServiceProviderTriggerStatics')
make_head(_module, 'IGeovisitTrigger')
make_head(_module, 'ILocationTrigger')
make_head(_module, 'ILocationTriggerFactory')
make_head(_module, 'IMaintenanceTrigger')
make_head(_module, 'IMaintenanceTriggerFactory')
make_head(_module, 'IMediaProcessingTrigger')
make_head(_module, 'INetworkOperatorHotspotAuthenticationTrigger')
make_head(_module, 'INetworkOperatorNotificationTrigger')
make_head(_module, 'INetworkOperatorNotificationTriggerFactory')
make_head(_module, 'IPhoneTrigger')
make_head(_module, 'IPhoneTriggerFactory')
make_head(_module, 'IPushNotificationTriggerFactory')
make_head(_module, 'IRcsEndUserMessageAvailableTrigger')
make_head(_module, 'IRfcommConnectionTrigger')
make_head(_module, 'ISecondaryAuthenticationFactorAuthenticationTrigger')
make_head(_module, 'ISensorDataThresholdTrigger')
make_head(_module, 'ISensorDataThresholdTriggerFactory')
make_head(_module, 'ISmartCardTrigger')
make_head(_module, 'ISmartCardTriggerFactory')
make_head(_module, 'ISmsMessageReceivedTriggerFactory')
make_head(_module, 'ISocketActivityTrigger')
make_head(_module, 'IStorageLibraryChangeTrackerTriggerFactory')
make_head(_module, 'IStorageLibraryContentChangedTrigger')
make_head(_module, 'IStorageLibraryContentChangedTriggerStatics')
make_head(_module, 'ISystemCondition')
make_head(_module, 'ISystemConditionFactory')
make_head(_module, 'ISystemTrigger')
make_head(_module, 'ISystemTriggerFactory')
make_head(_module, 'ITimeTrigger')
make_head(_module, 'ITimeTriggerFactory')
make_head(_module, 'IToastNotificationActionTriggerFactory')
make_head(_module, 'IToastNotificationHistoryChangedTriggerFactory')
make_head(_module, 'IUserNotificationChangedTriggerFactory')
make_head(_module, 'LocationTrigger')
make_head(_module, 'MaintenanceTrigger')
make_head(_module, 'MediaProcessingTrigger')
make_head(_module, 'MobileBroadbandDeviceServiceNotificationTrigger')
make_head(_module, 'MobileBroadbandPcoDataChangeTrigger')
make_head(_module, 'MobileBroadbandPinLockStateChangeTrigger')
make_head(_module, 'MobileBroadbandRadioStateChangeTrigger')
make_head(_module, 'MobileBroadbandRegistrationStateChangeTrigger')
make_head(_module, 'NetworkOperatorDataUsageTrigger')
make_head(_module, 'NetworkOperatorHotspotAuthenticationTrigger')
make_head(_module, 'NetworkOperatorNotificationTrigger')
make_head(_module, 'PaymentAppCanMakePaymentTrigger')
make_head(_module, 'PhoneTrigger')
make_head(_module, 'PushNotificationTrigger')
make_head(_module, 'RcsEndUserMessageAvailableTrigger')
make_head(_module, 'RfcommConnectionTrigger')
make_head(_module, 'SecondaryAuthenticationFactorAuthenticationTrigger')
make_head(_module, 'SensorDataThresholdTrigger')
make_head(_module, 'SmartCardTrigger')
make_head(_module, 'SmsMessageReceivedTrigger')
make_head(_module, 'SocketActivityTrigger')
make_head(_module, 'StorageLibraryChangeTrackerTrigger')
make_head(_module, 'StorageLibraryContentChangedTrigger')
make_head(_module, 'SystemCondition')
make_head(_module, 'SystemTrigger')
make_head(_module, 'TetheringEntitlementCheckTrigger')
make_head(_module, 'TimeTrigger')
make_head(_module, 'ToastNotificationActionTrigger')
make_head(_module, 'ToastNotificationHistoryChangedTrigger')
make_head(_module, 'UserNotificationChangedTrigger')
make_head(_module, 'WiFiOnDemandHotspotConnectTrigger')
make_head(_module, 'WiFiOnDemandHotspotUpdateMetadataTrigger')
