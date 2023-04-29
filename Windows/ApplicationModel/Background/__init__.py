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
    ClassId = 'Windows.ApplicationModel.Background.ActivitySensorTrigger'
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
class ApplicationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ApplicationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ApplicationTrigger: ...
    @winrt_mixinmethod
    def RequestAsync(self: Windows.ApplicationModel.Background.IApplicationTrigger) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IApplicationTrigger, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class ApplicationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ApplicationTriggerDetails'
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
    ClassId = 'Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.AppointmentStoreNotificationTrigger: ...
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
class BackgroundExecutionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundExecutionManager'
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
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskBuilder'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.BackgroundTaskBuilder: ...
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
    Guid = Guid('a6c4bac0-51f8-4c57-ac-3f-15-6d-d1-68-0c-4f')
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler'
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
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def CheckResult(self: Windows.ApplicationModel.Background.IBackgroundTaskCompletedEventArgs) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class BackgroundTaskCompletedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b38e929-a086-46a7-a6-78-43-91-35-82-2b-cf')
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskCompletedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: Windows.ApplicationModel.Background.BackgroundTaskCompletedEventArgs) -> Void: ...
class BackgroundTaskDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.Background.IBackgroundTaskDeferral) -> Void: ...
class BackgroundTaskProgressEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs'
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskProgressEventArgs) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class BackgroundTaskProgressEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('46e0683c-8a88-4c99-80-4c-76-89-7f-62-77-a6')
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskProgressEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.ApplicationModel.Background.BackgroundTaskRegistration, args: Windows.ApplicationModel.Background.BackgroundTaskProgressEventArgs) -> Void: ...
class BackgroundTaskRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskRegistration'
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
    AllTaskGroups = property(get_AllTaskGroups, None)
    AllTasks = property(get_AllTasks, None)
class BackgroundTaskRegistrationGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup'
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
class BackgroundWorkCost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BackgroundWorkCost'
    @winrt_classmethod
    def get_CurrentBackgroundWorkCost(cls: Windows.ApplicationModel.Background.IBackgroundWorkCostStatics) -> Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost, None)
BackgroundWorkCostValue = Int32
BackgroundWorkCostValue_Low: BackgroundWorkCostValue = 0
BackgroundWorkCostValue_Medium: BackgroundWorkCostValue = 1
BackgroundWorkCostValue_High: BackgroundWorkCostValue = 2
class BluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.BluetoothLEAdvertisementPublisherTrigger: ...
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
    ClassId = 'Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.BluetoothLEAdvertisementWatcherTrigger: ...
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
    ClassId = 'Windows.ApplicationModel.Background.CachedFileUpdaterTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.CachedFileUpdaterTrigger: ...
class CachedFileUpdaterTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.CachedFileUpdaterTriggerDetails'
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
    ClassId = 'Windows.ApplicationModel.Background.ChatMessageNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ChatMessageNotificationTrigger: ...
class ChatMessageReceivedNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ChatMessageReceivedNotificationTrigger: ...
class CommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.CommunicationBlockingAppSetAsActiveTrigger: ...
class ContactStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ContactStoreNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ContactStoreNotificationTrigger: ...
class ContentPrefetchTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ContentPrefetchTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IContentPrefetchTriggerFactory, waitInterval: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
    @winrt_mixinmethod
    def get_WaitInterval(self: Windows.ApplicationModel.Background.IContentPrefetchTrigger) -> Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class ConversationalAgentTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ConversationalAgentTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ConversationalAgentTrigger: ...
class CustomSystemEventTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.CustomSystemEventTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.DeviceServicingTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.DeviceServicingTrigger: ...
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
    ClassId = 'Windows.ApplicationModel.Background.DeviceUseTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.DeviceUseTrigger: ...
    @winrt_mixinmethod
    def RequestAsyncSimple(self: Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_mixinmethod
    def RequestAsyncWithArguments(self: Windows.ApplicationModel.Background.IDeviceUseTrigger, deviceId: WinRT_String, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class DeviceWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.DeviceWatcherTrigger'
class EmailStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.EmailStoreNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.EmailStoreNotificationTrigger: ...
class GattCharacteristicNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.GattServiceProviderTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.GattServiceProviderTriggerResult'
    @winrt_mixinmethod
    def get_Trigger(self: Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.ApplicationModel.Background.IGattServiceProviderTriggerResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Trigger = property(get_Trigger, None)
    Error = property(get_Error, None)
class GeovisitTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.GeovisitTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.GeovisitTrigger: ...
    @winrt_mixinmethod
    def get_MonitoringScope(self: Windows.ApplicationModel.Background.IGeovisitTrigger) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_mixinmethod
    def put_MonitoringScope(self: Windows.ApplicationModel.Background.IGeovisitTrigger, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class IActivitySensorTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0dd4342-e37b-4823-a5-fe-6b-31-df-ef-de-b0')
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
    Guid = Guid('a72691c3-3837-44f7-83-1b-01-32-cc-87-2b-c3')
    @winrt_commethod(6)
    def Create(self, reportIntervalInMilliseconds: UInt32) -> Windows.ApplicationModel.Background.ActivitySensorTrigger: ...
class IApplicationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0b468630-9574-492c-9e-93-1a-3a-e6-33-5f-e9')
    @winrt_commethod(6)
    def RequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.ApplicationTriggerResult]: ...
class IApplicationTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('97dc6ab2-2219-4a9e-9c-5e-41-d0-47-f7-6e-82')
    @winrt_commethod(6)
    def get_Arguments(self) -> Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
class IAppointmentStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64d4040c-c201-42ad-aa-2a-e2-1b-a3-42-5b-6d')
class IBackgroundCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae48a1ee-8951-400a-83-02-9c-9c-9a-2a-3a-3b')
class IBackgroundExecutionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e826ea58-66a9-4d41-83-d4-b4-c1-8c-87-b8-46')
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
    Guid = Guid('469b24ef-9bbb-4e18-99-9a-fd-65-12-93-1b-e9')
    @winrt_commethod(6)
    def RequestAccessKindAsync(self, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IBackgroundExecutionManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('98a5d3f6-5a25-5b6c-91-92-d7-7a-43-df-ed-c4')
    @winrt_commethod(6)
    def RequestAccessKindForModernStandbyAsync(self, requestedAccess: Windows.ApplicationModel.Background.BackgroundAccessRequestKind, reason: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def GetAccessStatusForModernStandby(self) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
    @winrt_commethod(8)
    def GetAccessStatusForModernStandbyForApplication(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundAccessStatus: ...
class IBackgroundTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d13d534-fd12-43ce-8c-22-ea-1f-f1-3c-06-df')
    @winrt_commethod(6)
    def Run(self, taskInstance: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class IBackgroundTaskBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0351550e-3e64-4572-a9-3a-84-07-5a-37-c9-17')
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
    Guid = Guid('6ae7cfb1-104f-406d-8d-b6-84-4a-57-0f-42-bb')
    @winrt_commethod(6)
    def put_CancelOnConditionLoss(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_CancelOnConditionLoss(self) -> Boolean: ...
    CancelOnConditionLoss = property(get_CancelOnConditionLoss, put_CancelOnConditionLoss)
class IBackgroundTaskBuilder3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('28c74f4a-8ba9-4c09-a2-4f-19-68-3e-2c-92-4c')
    @winrt_commethod(6)
    def put_IsNetworkRequested(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsNetworkRequested(self) -> Boolean: ...
    IsNetworkRequested = property(get_IsNetworkRequested, put_IsNetworkRequested)
class IBackgroundTaskBuilder4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4755e522-cba2-4e35-bd-16-a6-da-7f-1c-19-aa')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def put_TaskGroup(self, value: Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
class IBackgroundTaskBuilder5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('077103f6-99f5-4af4-bc-ad-47-31-d0-33-0d-43')
    @winrt_commethod(6)
    def SetTaskEntryPointClsid(self, TaskEntryPoint: Guid) -> Void: ...
class IBackgroundTaskCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('565d25cf-f209-48f4-99-67-2b-18-4f-7b-fb-f0')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def CheckResult(self) -> Void: ...
    InstanceId = property(get_InstanceId, None)
class IBackgroundTaskDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93cc156d-af27-4dd3-84-6e-24-ee-40-ca-dd-25')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IBackgroundTaskInstance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('865bda7a-21d8-4573-8f-32-92-8a-1b-06-41-f6')
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
    Guid = Guid('4f7d0176-0c76-4fb4-89-6d-5d-e1-86-41-22-f6')
    @winrt_commethod(6)
    def GetThrottleCount(self, counter: Windows.ApplicationModel.Background.BackgroundTaskThrottleCounter) -> UInt32: ...
class IBackgroundTaskInstance4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7f29f23c-aa04-4b08-97-b0-06-d8-74-cd-ab-f5')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IBackgroundTaskProgressEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb1468ac-8332-4d0a-95-32-03-ea-e6-84-da-31')
    @winrt_commethod(6)
    def get_InstanceId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Progress(self) -> UInt32: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, None)
class IBackgroundTaskRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('10654cc2-a26e-43bf-8c-12-1f-b4-0d-bf-bf-a0')
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
    Guid = Guid('6138c703-bb86-4112-af-c3-7f-93-9b-16-6e-3b')
    @winrt_commethod(6)
    def get_Trigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    Trigger = property(get_Trigger, None)
class IBackgroundTaskRegistration3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe338195-9423-4d8b-83-0d-b1-dd-2c-7b-ad-d5')
    @winrt_commethod(6)
    def get_TaskGroup(self) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    TaskGroup = property(get_TaskGroup, None)
class IBackgroundTaskRegistrationGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2ab1919a-871b-4167-8a-76-05-5c-d6-7b-5b-23')
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
    Guid = Guid('83d92b69-44cf-4631-97-40-03-c7-d8-74-1b-c5')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(7)
    def CreateWithName(self, id: WinRT_String, name: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
class IBackgroundTaskRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4c542f69-b000-42ba-a0-93-6a-56-3c-65-e3-f8')
    @winrt_commethod(6)
    def get_AllTasks(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.ApplicationModel.Background.IBackgroundTaskRegistration]: ...
    AllTasks = property(get_AllTasks, None)
class IBackgroundTaskRegistrationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('174b671e-b20d-4fa9-ad-9a-e9-3a-d6-c7-1e-01')
    @winrt_commethod(6)
    def get_AllTaskGroups(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup]: ...
    @winrt_commethod(7)
    def GetTaskGroup(self, groupId: WinRT_String) -> Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    AllTaskGroups = property(get_AllTaskGroups, None)
class IBackgroundTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('84b3a058-6027-4b87-97-90-bd-f3-f7-57-db-d7')
class IBackgroundWorkCostStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c740a662-c310-4b82-b3-e3-3b-cf-b9-e4-c7-7d')
    @winrt_commethod(6)
    def get_CurrentBackgroundWorkCost(self) -> Windows.ApplicationModel.Background.BackgroundWorkCostValue: ...
    CurrentBackgroundWorkCost = property(get_CurrentBackgroundWorkCost, None)
class IBluetoothLEAdvertisementPublisherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab3e2612-25d3-48ae-87-24-d8-18-77-ae-61-29')
    @winrt_commethod(6)
    def get_Advertisement(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    Advertisement = property(get_Advertisement, None)
class IBluetoothLEAdvertisementPublisherTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa28d064-38f4-597d-b5-97-4e-55-58-8c-65-03')
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
    Guid = Guid('1aab1819-bce1-48eb-a8-27-59-fb-7c-ee-52-a6')
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
    Guid = Guid('39b56799-eb39-5ab6-99-32-aa-9e-45-49-60-4d')
    @winrt_commethod(6)
    def get_AllowExtendedAdvertisements(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExtendedAdvertisements(self, value: Boolean) -> Void: ...
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class ICachedFileUpdaterTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e21caeeb-32f2-4d31-b5-53-b9-e0-1b-de-37-e0')
class ICachedFileUpdaterTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71838c13-1314-47b4-95-97-dc-7e-24-8c-17-cc')
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
    Guid = Guid('513b43bf-1d40-5c5d-78-f5-c9-23-fe-e3-73-9e')
class IChatMessageReceivedNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3ea3760e-baf5-4077-88-e9-06-0c-f6-f0-c6-d5')
class ICommunicationBlockingAppSetAsActiveTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb91f28a-16a5-486d-97-4c-78-35-a8-47-7b-e2')
class IContactStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c833419b-4705-4571-9a-16-06-b9-97-bf-9c-96')
class IContentPrefetchTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('710627ee-04fa-440b-80-c0-17-32-02-19-9e-5d')
    @winrt_commethod(6)
    def get_WaitInterval(self) -> Windows.Foundation.TimeSpan: ...
    WaitInterval = property(get_WaitInterval, None)
class IContentPrefetchTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c2643eda-8a03-409e-b8-c4-88-81-4c-28-cc-b6')
    @winrt_commethod(6)
    def Create(self, waitInterval: Windows.Foundation.TimeSpan) -> Windows.ApplicationModel.Background.ContentPrefetchTrigger: ...
class ICustomSystemEventTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f3596798-cf6b-4ef4-a0-ca-29-cf-4a-27-8c-87')
    @winrt_commethod(6)
    def get_TriggerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Recurrence(self) -> Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence: ...
    TriggerId = property(get_TriggerId, None)
    Recurrence = property(get_Recurrence, None)
class ICustomSystemEventTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6bcb16c5-f2dc-41b2-9e-fd-b9-6b-dc-d1-3c-ed')
    @winrt_commethod(6)
    def Create(self, triggerId: WinRT_String, recurrence: Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence) -> Windows.ApplicationModel.Background.CustomSystemEventTrigger: ...
class IDeviceConnectionChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('90875e64-3cdd-4efb-ab-1c-5b-3b-6a-60-ce-34')
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
    Guid = Guid('c3ea246a-4efd-4498-aa-60-a4-e4-e3-b1-7a-b9')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceConnectionChangeTrigger]: ...
class IDeviceManufacturerNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('81278ab5-41ab-16da-86-c2-7f-7b-f0-91-2f-5b')
    @winrt_commethod(6)
    def get_TriggerQualifier(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    TriggerQualifier = property(get_TriggerQualifier, None)
    OneShot = property(get_OneShot, None)
class IDeviceManufacturerNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7955de75-25bb-4153-a1-a2-30-29-fc-ab-b6-52')
    @winrt_commethod(6)
    def Create(self, triggerQualifier: WinRT_String, oneShot: Boolean) -> Windows.ApplicationModel.Background.DeviceManufacturerNotificationTrigger: ...
class IDeviceServicingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1ab217ad-6e34-49d3-9e-6f-17-f1-b6-df-a8-81')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, expectedDuration: Windows.Foundation.TimeSpan, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceUseTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0da68011-334f-4d57-b6-ec-6d-ca-64-b4-12-e4')
    @winrt_commethod(6)
    def RequestAsyncSimple(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, deviceId: WinRT_String, arguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.DeviceTriggerResult]: ...
class IDeviceWatcherTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4617fdd-8573-4260-be-fc-5b-ec-89-cb-69-3d')
class IEmailStoreNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('986d06da-47eb-4268-a4-f2-f3-f7-71-88-38-8a')
class IGattCharacteristicNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e25f8fc8-0696-474f-a7-32-f2-92-b0-ce-bc-5d')
    @winrt_commethod(6)
    def get_Characteristic(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic: ...
    Characteristic = property(get_Characteristic, None)
class IGattCharacteristicNotificationTrigger2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9322a2c4-ae0e-42f2-b2-8c-f5-13-72-e6-92-45')
    @winrt_commethod(6)
    def get_EventTriggeringMode(self) -> Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode: ...
    EventTriggeringMode = property(get_EventTriggeringMode, None)
class IGattCharacteristicNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('57ba1995-b143-4575-9f-6b-fd-59-d9-3a-ce-1a')
    @winrt_commethod(6)
    def Create(self, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattCharacteristicNotificationTriggerFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5998e91f-8a53-4e9f-a3-2c-23-cd-33-66-4c-ee')
    @winrt_commethod(6)
    def CreateWithEventTriggeringMode(self, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, eventTriggeringMode: Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode) -> Windows.ApplicationModel.Background.GattCharacteristicNotificationTrigger: ...
class IGattServiceProviderTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ddc6a3e9-1557-4bd8-85-42-46-8a-a0-c6-96-f6')
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
    Guid = Guid('3c4691b1-b198-4e84-ba-d4-cf-4a-d2-99-ed-3a')
    @winrt_commethod(6)
    def get_Trigger(self) -> Windows.ApplicationModel.Background.GattServiceProviderTrigger: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Trigger = property(get_Trigger, None)
    Error = property(get_Error, None)
class IGattServiceProviderTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b413a36a-e294-4591-a5-a6-64-89-1a-82-81-53')
    @winrt_commethod(6)
    def CreateAsync(self, triggerId: WinRT_String, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.GattServiceProviderTriggerResult]: ...
class IGeovisitTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4818edaa-04e1-4127-9a-4c-19-35-1b-8a-80-a4')
    @winrt_commethod(6)
    def get_MonitoringScope(self) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_commethod(7)
    def put_MonitoringScope(self, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, put_MonitoringScope)
class ILocationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47666a1c-6877-481e-80-26-ff-7e-14-a8-11-a0')
    @winrt_commethod(6)
    def get_TriggerType(self) -> Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ILocationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1106bb07-ff69-4e09-aa-8b-13-84-ea-47-5e-98')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.ApplicationModel.Background.LocationTriggerType) -> Windows.ApplicationModel.Background.LocationTrigger: ...
class IMaintenanceTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('68184c83-fc22-4ce5-84-1a-72-39-a9-81-00-47')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class IMaintenanceTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4b3ddb2e-97dd-4629-88-b0-b0-6c-f9-48-2a-e5')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.MaintenanceTrigger: ...
class IMediaProcessingTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9a95be65-8a52-4b30-90-11-cf-38-04-0e-a8-b0')
    @winrt_commethod(6)
    def RequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
    @winrt_commethod(7)
    def RequestAsyncWithArguments(self, arguments: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Background.MediaProcessingTriggerResult]: ...
class INetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e756c791-3001-4de5-83-c7-de-61-d8-88-31-d0')
class INetworkOperatorNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('90089cc6-63cd-480c-95-d1-6e-6a-ef-80-1e-4a')
    @winrt_commethod(6)
    def get_NetworkAccountId(self) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class INetworkOperatorNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0a223e00-27d7-4353-ad-b9-92-65-aa-ea-57-9d')
    @winrt_commethod(6)
    def Create(self, networkAccountId: WinRT_String) -> Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
class IPhoneTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8dcfe99b-d4c5-49f1-b7-d3-82-e8-7a-0e-9d-de')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> Windows.ApplicationModel.Calls.Background.PhoneTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class IPhoneTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a0d93cda-5fc1-48fb-a5-46-32-26-20-40-15-7b')
    @winrt_commethod(6)
    def Create(self, type: Windows.ApplicationModel.Calls.Background.PhoneTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.PhoneTrigger: ...
class IPushNotificationTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6dd8ed1b-458e-4fc2-bc-2e-d5-66-4f-77-ed-19')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class IRcsEndUserMessageAvailableTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('986d0d6a-b2f6-467f-a9-78-a4-40-91-c1-1a-66')
class IRfcommConnectionTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e8c4cae2-0b53-4464-93-94-fd-87-56-54-de-64')
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
    Guid = Guid('f237f327-5181-4f24-96-a7-70-0a-4e-5f-ac-62')
class ISensorDataThresholdTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5bc0f372-d48b-4b7f-ab-ec-15-f9-ba-cc-12-e2')
class ISensorDataThresholdTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('921fe675-7df0-4da3-97-b3-e5-44-ee-85-7f-e6')
    @winrt_commethod(6)
    def Create(self, threshold: Windows.Devices.Sensors.ISensorDataThreshold) -> Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class ISmartCardTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f53bc5ac-84ca-4972-8c-e9-e5-8f-97-b3-7a-50')
    @winrt_commethod(6)
    def get_TriggerType(self) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class ISmartCardTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63bf54c3-89c1-4e00-a9-d3-97-c6-29-26-9d-ad')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.Devices.SmartCards.SmartCardTriggerType) -> Windows.ApplicationModel.Background.SmartCardTrigger: ...
class ISmsMessageReceivedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ea3ad8c8-6ba4-4ab2-8d-21-bc-6b-09-c7-75-64')
    @winrt_commethod(6)
    def Create(self, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class ISocketActivityTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9bbf810-9dde-4f8a-83-e3-b0-e0-e7-a5-0d-70')
    @winrt_commethod(6)
    def get_IsWakeFromLowPowerSupported(self) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class IStorageLibraryChangeTrackerTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1eb0ffd0-5a85-499e-a8-88-82-46-07-12-4f-50')
    @winrt_commethod(6)
    def Create(self, tracker: Windows.Storage.StorageLibraryChangeTracker) -> Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class IStorageLibraryContentChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1637e0a7-829c-45bc-92-9b-a1-e7-ea-78-d8-9b')
class IStorageLibraryContentChangedTriggerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7f9f1b39-5f90-4e12-91-4e-a7-d8-e0-bb-fb-18')
    @winrt_commethod(6)
    def Create(self, storageLibrary: Windows.Storage.StorageLibrary) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_commethod(7)
    def CreateFromLibraries(self, storageLibraries: Windows.Foundation.Collections.IIterable[Windows.Storage.StorageLibrary]) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class ISystemCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c15fb476-89c5-420b-ab-d3-fb-30-30-47-21-28')
    @winrt_commethod(6)
    def get_ConditionType(self) -> Windows.ApplicationModel.Background.SystemConditionType: ...
    ConditionType = property(get_ConditionType, None)
class ISystemConditionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d269d1f1-05a7-49ae-87-d7-16-b2-b8-b9-a5-53')
    @winrt_commethod(6)
    def Create(self, conditionType: Windows.ApplicationModel.Background.SystemConditionType) -> Windows.ApplicationModel.Background.SystemCondition: ...
class ISystemTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d80c776-3748-4463-8d-7e-27-6d-c1-39-ac-1c')
    @winrt_commethod(6)
    def get_OneShot(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TriggerType(self) -> Windows.ApplicationModel.Background.SystemTriggerType: ...
    OneShot = property(get_OneShot, None)
    TriggerType = property(get_TriggerType, None)
class ISystemTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e80423d4-8791-4579-81-26-87-ec-8a-aa-40-7a')
    @winrt_commethod(6)
    def Create(self, triggerType: Windows.ApplicationModel.Background.SystemTriggerType, oneShot: Boolean) -> Windows.ApplicationModel.Background.SystemTrigger: ...
class ITimeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('656e5556-0b2a-4377-ba-70-3b-45-a9-35-54-7f')
    @winrt_commethod(6)
    def get_FreshnessTime(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OneShot(self) -> Boolean: ...
    FreshnessTime = property(get_FreshnessTime, None)
    OneShot = property(get_OneShot, None)
class ITimeTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('38c682fe-9b54-45e6-b2-f3-26-9b-87-a6-f7-34')
    @winrt_commethod(6)
    def Create(self, freshnessTime: UInt32, oneShot: Boolean) -> Windows.ApplicationModel.Background.TimeTrigger: ...
class IToastNotificationActionTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b09dfc27-6480-4349-81-25-97-b3-ef-aa-0a-3a')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class IToastNotificationHistoryChangedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('81c6faad-8797-4785-81-b4-b0-cc-cb-73-d1-d9')
    @winrt_commethod(6)
    def Create(self, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class IUserNotificationChangedTriggerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cad4436c-69ab-4e18-a4-8a-5e-d2-ac-43-59-57')
    @winrt_commethod(6)
    def Create(self, notificationKinds: Windows.UI.Notifications.NotificationKinds) -> Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class LocationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.LocationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ILocationTriggerFactory, triggerType: Windows.ApplicationModel.Background.LocationTriggerType) -> Windows.ApplicationModel.Background.LocationTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.ILocationTrigger) -> Windows.ApplicationModel.Background.LocationTriggerType: ...
    TriggerType = property(get_TriggerType, None)
LocationTriggerType = Int32
LocationTriggerType_Geofence: LocationTriggerType = 0
class MaintenanceTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.MaintenanceTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.MediaProcessingTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MediaProcessingTrigger: ...
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
    ClassId = 'Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MobileBroadbandDeviceServiceNotificationTrigger: ...
class MobileBroadbandPcoDataChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MobileBroadbandPcoDataChangeTrigger: ...
class MobileBroadbandPinLockStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MobileBroadbandPinLockStateChangeTrigger: ...
class MobileBroadbandRadioStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MobileBroadbandRadioStateChangeTrigger: ...
class MobileBroadbandRegistrationStateChangeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.MobileBroadbandRegistrationStateChangeTrigger: ...
class NetworkOperatorDataUsageTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.NetworkOperatorDataUsageTrigger: ...
class NetworkOperatorHotspotAuthenticationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.NetworkOperatorHotspotAuthenticationTrigger: ...
class NetworkOperatorNotificationTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.INetworkOperatorNotificationTriggerFactory, networkAccountId: WinRT_String) -> Windows.ApplicationModel.Background.NetworkOperatorNotificationTrigger: ...
    @winrt_mixinmethod
    def get_NetworkAccountId(self: Windows.ApplicationModel.Background.INetworkOperatorNotificationTrigger) -> WinRT_String: ...
    NetworkAccountId = property(get_NetworkAccountId, None)
class PaymentAppCanMakePaymentTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.PaymentAppCanMakePaymentTrigger: ...
class PhoneTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.PhoneTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.PushNotificationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IPushNotificationTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.PushNotificationTrigger: ...
class RcsEndUserMessageAvailableTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.RcsEndUserMessageAvailableTrigger: ...
class RfcommConnectionTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.RfcommConnectionTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.RfcommConnectionTrigger: ...
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
    ClassId = 'Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.SecondaryAuthenticationFactorAuthenticationTrigger: ...
class SensorDataThresholdTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.SensorDataThresholdTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISensorDataThresholdTriggerFactory, threshold: Windows.Devices.Sensors.ISensorDataThreshold) -> Windows.ApplicationModel.Background.SensorDataThresholdTrigger: ...
class SmartCardTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.SmartCardTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISmartCardTriggerFactory, triggerType: Windows.Devices.SmartCards.SmartCardTriggerType) -> Windows.ApplicationModel.Background.SmartCardTrigger: ...
    @winrt_mixinmethod
    def get_TriggerType(self: Windows.ApplicationModel.Background.ISmartCardTrigger) -> Windows.Devices.SmartCards.SmartCardTriggerType: ...
    TriggerType = property(get_TriggerType, None)
class SmsMessageReceivedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.SmsMessageReceivedTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.ISmsMessageReceivedTriggerFactory, filterRules: Windows.Devices.Sms.SmsFilterRules) -> Windows.ApplicationModel.Background.SmsMessageReceivedTrigger: ...
class SocketActivityTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.SocketActivityTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.SocketActivityTrigger: ...
    @winrt_mixinmethod
    def get_IsWakeFromLowPowerSupported(self: Windows.ApplicationModel.Background.ISocketActivityTrigger) -> Boolean: ...
    IsWakeFromLowPowerSupported = property(get_IsWakeFromLowPowerSupported, None)
class StorageLibraryChangeTrackerTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IStorageLibraryChangeTrackerTriggerFactory, tracker: Windows.Storage.StorageLibraryChangeTracker) -> Windows.ApplicationModel.Background.StorageLibraryChangeTrackerTrigger: ...
class StorageLibraryContentChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger'
    @winrt_classmethod
    def Create(cls: Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibrary: Windows.Storage.StorageLibrary) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
    @winrt_classmethod
    def CreateFromLibraries(cls: Windows.ApplicationModel.Background.IStorageLibraryContentChangedTriggerStatics, storageLibraries: Windows.Foundation.Collections.IIterable[Windows.Storage.StorageLibrary]) -> Windows.ApplicationModel.Background.StorageLibraryContentChangedTrigger: ...
class SystemCondition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.SystemCondition'
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
    ClassId = 'Windows.ApplicationModel.Background.SystemTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.TetheringEntitlementCheckTrigger: ...
class TimeTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.TimeTrigger'
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
    ClassId = 'Windows.ApplicationModel.Background.ToastNotificationActionTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IToastNotificationActionTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ToastNotificationActionTrigger: ...
class ToastNotificationHistoryChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IToastNotificationHistoryChangedTriggerFactory, applicationId: WinRT_String) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.ToastNotificationHistoryChangedTrigger: ...
class UserNotificationChangedTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.UserNotificationChangedTrigger'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.Background.IUserNotificationChangedTriggerFactory, notificationKinds: Windows.UI.Notifications.NotificationKinds) -> Windows.ApplicationModel.Background.UserNotificationChangedTrigger: ...
class WiFiOnDemandHotspotConnectTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.WiFiOnDemandHotspotConnectTrigger: ...
class WiFiOnDemandHotspotUpdateMetadataTrigger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Background.WiFiOnDemandHotspotUpdateMetadataTrigger: ...
make_head(_module, 'ActivitySensorTrigger')
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
