from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Email
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Phone.Notification.Management
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class _AccessoryManager_Meta_(ComPtr.__class__):
    pass
class AccessoryManager(ComPtr, metaclass=_AccessoryManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.AccessoryManager'
    @winrt_classmethod
    def SnoozeAlarmByInstanceId(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager3, instanceId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def DismissAlarmByInstanceId(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager3, instanceId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def SnoozeReminderByInstanceId(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager3, instanceId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def DismissReminderByInstanceId(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager3, instanceId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RingDevice(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2) -> Void: ...
    @winrt_classmethod
    def get_SpeedDialList(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.SpeedDialEntry]: ...
    @winrt_classmethod
    def ClearToast(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, instanceId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_IsPhonePinLocked(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2) -> Boolean: ...
    @winrt_classmethod
    def IncreaseVolume(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, step: Int32) -> Void: ...
    @winrt_classmethod
    def DecreaseVolume(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, step: Int32) -> Void: ...
    @winrt_classmethod
    def SetMute(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, mute: Boolean) -> Void: ...
    @winrt_classmethod
    def SetRingerVibrate(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, ringer: Boolean, vibrate: Boolean) -> Void: ...
    @winrt_classmethod
    def get_VolumeInfo(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2) -> win32more.Windows.Phone.Notification.Management.VolumeInfo: ...
    @winrt_classmethod
    def GetAllEmailAccounts(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.EmailAccountInfo]: ...
    @winrt_classmethod
    def GetFolders(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, emailAccount: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.EmailFolderInfo]: ...
    @winrt_classmethod
    def EnableEmailNotificationEmailAccount(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, emailAccount: WinRT_String) -> Void: ...
    @winrt_classmethod
    def DisableEmailNotificationEmailAccount(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, emailAccount: WinRT_String) -> Void: ...
    @winrt_classmethod
    def EnableEmailNotificationFolderFilter(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, emailAccount: WinRT_String, folders: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_classmethod
    def UpdateEmailReadStatus(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager2, messageEntryId: win32more.Windows.Phone.Notification.Management.BinaryId, isRead: Boolean) -> Void: ...
    @winrt_classmethod
    def RegisterAccessoryApp(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> WinRT_String: ...
    @winrt_classmethod
    def GetNextTriggerDetails(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails: ...
    @winrt_classmethod
    def ProcessTriggerDetails(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, pDetails: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Void: ...
    @winrt_classmethod
    def get_PhoneLineDetails(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.PhoneLineDetails]: ...
    @winrt_classmethod
    def GetPhoneLineDetails(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneLine: Guid) -> win32more.Windows.Phone.Notification.Management.PhoneLineDetails: ...
    @winrt_classmethod
    def AcceptPhoneCall(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32) -> Void: ...
    @winrt_classmethod
    def AcceptPhoneCallOnEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_classmethod
    def AcceptPhoneCallWithVideo(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32) -> Void: ...
    @winrt_classmethod
    def AcceptPhoneCallWithVideoOnAudioEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_classmethod
    def RejectPhoneCall(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32) -> Void: ...
    @winrt_classmethod
    def RejectPhoneCallWithText(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32, textResponseID: UInt32) -> Void: ...
    @winrt_classmethod
    def MakePhoneCall(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneLine: Guid, phoneNumber: WinRT_String) -> Void: ...
    @winrt_classmethod
    def MakePhoneCallOnAudioEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneLine: Guid, phoneNumber: WinRT_String, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_classmethod
    def MakePhoneCallWithVideo(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneLine: Guid, phoneNumber: WinRT_String) -> Void: ...
    @winrt_classmethod
    def MakePhoneCallWithVideoOnAudioEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneLine: Guid, phoneNumber: WinRT_String, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_classmethod
    def SwapPhoneCalls(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallIdToHold: UInt32, phoneCallIdOnHold: UInt32) -> Void: ...
    @winrt_classmethod
    def HoldPhoneCall(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32, holdCall: Boolean) -> Void: ...
    @winrt_classmethod
    def EndPhoneCall(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, phoneCallId: UInt32) -> Void: ...
    @winrt_classmethod
    def put_PhoneMute(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_PhoneMute(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Boolean: ...
    @winrt_classmethod
    def put_PhoneCallAudioEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, value: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_classmethod
    def get_PhoneCallAudioEndpoint(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint: ...
    @winrt_classmethod
    def SnoozeAlarm(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, alarmId: Guid) -> Void: ...
    @winrt_classmethod
    def SnoozeAlarmForSpecifiedTime(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, alarmId: Guid, timeSpan: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def DismissAlarm(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, alarmId: Guid) -> Void: ...
    @winrt_classmethod
    def SnoozeReminder(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, reminderId: Guid) -> Void: ...
    @winrt_classmethod
    def SnoozeReminderForSpecifiedTime(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, reminderId: Guid, timeSpan: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_classmethod
    def DismissReminder(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, reminderId: Guid) -> Void: ...
    @winrt_classmethod
    def GetMediaMetadata(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Phone.Notification.Management.MediaMetadata: ...
    @winrt_classmethod
    def get_MediaPlaybackCapabilities(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Phone.Notification.Management.PlaybackCapability: ...
    @winrt_classmethod
    def get_MediaPlaybackStatus(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Phone.Notification.Management.PlaybackStatus: ...
    @winrt_classmethod
    def PerformMediaPlaybackCommand(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, command: win32more.Windows.Phone.Notification.Management.PlaybackCommand) -> Void: ...
    @winrt_classmethod
    def get_DoNotDisturbEnabled(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Boolean: ...
    @winrt_classmethod
    def get_DrivingModeEnabled(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Boolean: ...
    @winrt_classmethod
    def get_BatterySaverState(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Boolean: ...
    @winrt_classmethod
    def GetApps(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Phone.Notification.Management.AppNotificationInfo]: ...
    @winrt_classmethod
    def EnableNotificationsForApplication(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, appId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def DisableNotificationsForApplication(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, appId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def IsNotificationEnabledForApplication(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, appId: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def GetEnabledAccessoryNotificationTypes(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Int32: ...
    @winrt_classmethod
    def EnableAccessoryNotificationTypes(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, accessoryNotificationTypes: Int32) -> Void: ...
    @winrt_classmethod
    def DisableAllAccessoryNotificationTypes(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Void: ...
    @winrt_classmethod
    def GetUserConsent(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager) -> Boolean: ...
    @winrt_classmethod
    def GetAppIcon(cls: win32more.Windows.Phone.Notification.Management.IAccessoryManager, appId: WinRT_String) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    _AccessoryManager_Meta_.BatterySaverState = property(get_BatterySaverState, None)
    _AccessoryManager_Meta_.DoNotDisturbEnabled = property(get_DoNotDisturbEnabled, None)
    _AccessoryManager_Meta_.DrivingModeEnabled = property(get_DrivingModeEnabled, None)
    _AccessoryManager_Meta_.IsPhonePinLocked = property(get_IsPhonePinLocked, None)
    _AccessoryManager_Meta_.MediaPlaybackCapabilities = property(get_MediaPlaybackCapabilities, None)
    _AccessoryManager_Meta_.MediaPlaybackStatus = property(get_MediaPlaybackStatus, None)
    _AccessoryManager_Meta_.PhoneCallAudioEndpoint = property(get_PhoneCallAudioEndpoint, put_PhoneCallAudioEndpoint)
    _AccessoryManager_Meta_.PhoneLineDetails = property(get_PhoneLineDetails, None)
    _AccessoryManager_Meta_.PhoneMute = property(get_PhoneMute, put_PhoneMute)
    _AccessoryManager_Meta_.SpeedDialList = property(get_SpeedDialList, None)
    _AccessoryManager_Meta_.VolumeInfo = property(get_VolumeInfo, None)
class AccessoryNotificationType(Enum, UInt32):
    None_ = 0
    Phone = 1
    Email = 2
    Reminder = 4
    Alarm = 8
    Toast = 16
    AppUninstalled = 32
    Dnd = 64
    DrivingMode = 128
    BatterySaver = 256
    Media = 512
    CortanaTile = 1024
    ToastCleared = 2048
    CalendarChanged = 4096
    VolumeChanged = 8192
    EmailReadStatusChanged = 16384
class AlarmNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.AlarmNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_AlarmId(self: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ReminderState(self: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.ReminderState: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails2) -> WinRT_String: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AlarmId = property(get_AlarmId, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    InstanceId = property(get_InstanceId, None)
    ReminderState = property(get_ReminderState, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
class AppNotificationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IAppNotificationInfo
    _classid_ = 'Windows.Phone.Notification.Management.AppNotificationInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.Notification.Management.IAppNotificationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Phone.Notification.Management.IAppNotificationInfo) -> WinRT_String: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
class BinaryId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IBinaryId
    _classid_ = 'Windows.Phone.Notification.Management.BinaryId'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.Notification.Management.IBinaryId) -> Byte: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Phone.Notification.Management.IBinaryId) -> UInt32: ...
    Id = property(get_Id, None)
    Length = property(get_Length, None)
class CalendarChangedEvent(Enum, Int32):
    LostEvents = 0
    AppointmentAdded = 1
    AppointmentChanged = 2
    AppointmentDeleted = 3
    CalendarAdded = 4
    CalendarChanged = 5
    CalendarDeleted = 6
class CalendarChangedNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.ICalendarChangedNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.CalendarChangedNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_EventType(self: win32more.Windows.Phone.Notification.Management.ICalendarChangedNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.CalendarChangedEvent: ...
    @winrt_mixinmethod
    def get_ItemId(self: win32more.Windows.Phone.Notification.Management.ICalendarChangedNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    EventType = property(get_EventType, None)
    ItemId = property(get_ItemId, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
class CortanaTileNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.CortanaTileNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LargeContent1(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LargeContent2(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmphasizedText(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NonWrappedSmallContent1(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NonWrappedSmallContent2(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NonWrappedSmallContent3(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NonWrappedSmallContent4(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    Content = property(get_Content, None)
    EmphasizedText = property(get_EmphasizedText, None)
    LargeContent1 = property(get_LargeContent1, None)
    LargeContent2 = property(get_LargeContent2, None)
    NonWrappedSmallContent1 = property(get_NonWrappedSmallContent1, None)
    NonWrappedSmallContent2 = property(get_NonWrappedSmallContent2, None)
    NonWrappedSmallContent3 = property(get_NonWrappedSmallContent3, None)
    NonWrappedSmallContent4 = property(get_NonWrappedSmallContent4, None)
    Source = property(get_Source, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TileId = property(get_TileId, None)
    TimeCreated = property(get_TimeCreated, None)
class EmailAccountInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IEmailAccountInfo
    _classid_ = 'Windows.Phone.Notification.Management.EmailAccountInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.Notification.Management.IEmailAccountInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsNotificationEnabled(self: win32more.Windows.Phone.Notification.Management.IEmailAccountInfo) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    IsNotificationEnabled = property(get_IsNotificationEnabled, None)
class EmailFolderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IEmailFolderInfo
    _classid_ = 'Windows.Phone.Notification.Management.EmailFolderInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.Notification.Management.IEmailFolderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsNotificationEnabled(self: win32more.Windows.Phone.Notification.Management.IEmailFolderInfo) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    IsNotificationEnabled = property(get_IsNotificationEnabled, None)
class EmailNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.EmailNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_AccountName(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentFolderName(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SenderName(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SenderAddress(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EmailMessage(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> win32more.Windows.ApplicationModel.Email.EmailMessage: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MessageEntryId(self: win32more.Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails2) -> win32more.Windows.Phone.Notification.Management.BinaryId: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AccountName = property(get_AccountName, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    EmailMessage = property(get_EmailMessage, None)
    MessageEntryId = property(get_MessageEntryId, None)
    ParentFolderName = property(get_ParentFolderName, None)
    SenderAddress = property(get_SenderAddress, None)
    SenderName = property(get_SenderName, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
    Timestamp = property(get_Timestamp, None)
class EmailReadNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.EmailReadNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_AccountName(self: win32more.Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParentFolderName(self: win32more.Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MessageEntryId(self: win32more.Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.BinaryId: ...
    @winrt_mixinmethod
    def get_IsRead(self: win32more.Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AccountName = property(get_AccountName, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    IsRead = property(get_IsRead, None)
    MessageEntryId = property(get_MessageEntryId, None)
    ParentFolderName = property(get_ParentFolderName, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
class IAccessoryManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAccessoryManager'
    _iid_ = Guid('{0d04a12c-883d-4aa7-bca7-fa4bb8bffee6}')
    @winrt_commethod(6)
    def RegisterAccessoryApp(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetNextTriggerDetails(self) -> win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails: ...
    @winrt_commethod(8)
    def ProcessTriggerDetails(self, pDetails: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Void: ...
    @winrt_commethod(9)
    def get_PhoneLineDetails(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.PhoneLineDetails]: ...
    @winrt_commethod(10)
    def GetPhoneLineDetails(self, phoneLine: Guid) -> win32more.Windows.Phone.Notification.Management.PhoneLineDetails: ...
    @winrt_commethod(11)
    def AcceptPhoneCall(self, phoneCallId: UInt32) -> Void: ...
    @winrt_commethod(12)
    def AcceptPhoneCallOnEndpoint(self, phoneCallId: UInt32, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_commethod(13)
    def AcceptPhoneCallWithVideo(self, phoneCallId: UInt32) -> Void: ...
    @winrt_commethod(14)
    def AcceptPhoneCallWithVideoOnAudioEndpoint(self, phoneCallId: UInt32, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_commethod(15)
    def RejectPhoneCall(self, phoneCallId: UInt32) -> Void: ...
    @winrt_commethod(16)
    def RejectPhoneCallWithText(self, phoneCallId: UInt32, textResponseID: UInt32) -> Void: ...
    @winrt_commethod(17)
    def MakePhoneCall(self, phoneLine: Guid, phoneNumber: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def MakePhoneCallOnAudioEndpoint(self, phoneLine: Guid, phoneNumber: WinRT_String, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_commethod(19)
    def MakePhoneCallWithVideo(self, phoneLine: Guid, phoneNumber: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def MakePhoneCallWithVideoOnAudioEndpoint(self, phoneLine: Guid, phoneNumber: WinRT_String, endPoint: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_commethod(21)
    def SwapPhoneCalls(self, phoneCallIdToHold: UInt32, phoneCallIdOnHold: UInt32) -> Void: ...
    @winrt_commethod(22)
    def HoldPhoneCall(self, phoneCallId: UInt32, holdCall: Boolean) -> Void: ...
    @winrt_commethod(23)
    def EndPhoneCall(self, phoneCallId: UInt32) -> Void: ...
    @winrt_commethod(24)
    def put_PhoneMute(self, value: Boolean) -> Void: ...
    @winrt_commethod(25)
    def get_PhoneMute(self) -> Boolean: ...
    @winrt_commethod(26)
    def put_PhoneCallAudioEndpoint(self, value: win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint) -> Void: ...
    @winrt_commethod(27)
    def get_PhoneCallAudioEndpoint(self) -> win32more.Windows.Phone.Notification.Management.PhoneCallAudioEndpoint: ...
    @winrt_commethod(28)
    def SnoozeAlarm(self, alarmId: Guid) -> Void: ...
    @winrt_commethod(29)
    def SnoozeAlarmForSpecifiedTime(self, alarmId: Guid, timeSpan: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(30)
    def DismissAlarm(self, alarmId: Guid) -> Void: ...
    @winrt_commethod(31)
    def SnoozeReminder(self, reminderId: Guid) -> Void: ...
    @winrt_commethod(32)
    def SnoozeReminderForSpecifiedTime(self, reminderId: Guid, timeSpan: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(33)
    def DismissReminder(self, reminderId: Guid) -> Void: ...
    @winrt_commethod(34)
    def GetMediaMetadata(self) -> win32more.Windows.Phone.Notification.Management.MediaMetadata: ...
    @winrt_commethod(35)
    def get_MediaPlaybackCapabilities(self) -> win32more.Windows.Phone.Notification.Management.PlaybackCapability: ...
    @winrt_commethod(36)
    def get_MediaPlaybackStatus(self) -> win32more.Windows.Phone.Notification.Management.PlaybackStatus: ...
    @winrt_commethod(37)
    def PerformMediaPlaybackCommand(self, command: win32more.Windows.Phone.Notification.Management.PlaybackCommand) -> Void: ...
    @winrt_commethod(38)
    def get_DoNotDisturbEnabled(self) -> Boolean: ...
    @winrt_commethod(39)
    def get_DrivingModeEnabled(self) -> Boolean: ...
    @winrt_commethod(40)
    def get_BatterySaverState(self) -> Boolean: ...
    @winrt_commethod(41)
    def GetApps(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Phone.Notification.Management.AppNotificationInfo]: ...
    @winrt_commethod(42)
    def EnableNotificationsForApplication(self, appId: WinRT_String) -> Void: ...
    @winrt_commethod(43)
    def DisableNotificationsForApplication(self, appId: WinRT_String) -> Void: ...
    @winrt_commethod(44)
    def IsNotificationEnabledForApplication(self, appId: WinRT_String) -> Boolean: ...
    @winrt_commethod(45)
    def GetEnabledAccessoryNotificationTypes(self) -> Int32: ...
    @winrt_commethod(46)
    def EnableAccessoryNotificationTypes(self, accessoryNotificationTypes: Int32) -> Void: ...
    @winrt_commethod(47)
    def DisableAllAccessoryNotificationTypes(self) -> Void: ...
    @winrt_commethod(48)
    def GetUserConsent(self) -> Boolean: ...
    @winrt_commethod(49)
    def GetAppIcon(self, appId: WinRT_String) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    BatterySaverState = property(get_BatterySaverState, None)
    DoNotDisturbEnabled = property(get_DoNotDisturbEnabled, None)
    DrivingModeEnabled = property(get_DrivingModeEnabled, None)
    MediaPlaybackCapabilities = property(get_MediaPlaybackCapabilities, None)
    MediaPlaybackStatus = property(get_MediaPlaybackStatus, None)
    PhoneCallAudioEndpoint = property(get_PhoneCallAudioEndpoint, put_PhoneCallAudioEndpoint)
    PhoneLineDetails = property(get_PhoneLineDetails, None)
    PhoneMute = property(get_PhoneMute, put_PhoneMute)
class IAccessoryManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAccessoryManager2'
    _iid_ = Guid('{bacad44d-d393-46c6-b80c-15fdf44d5386}')
    @winrt_commethod(6)
    def RingDevice(self) -> Void: ...
    @winrt_commethod(7)
    def get_SpeedDialList(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.SpeedDialEntry]: ...
    @winrt_commethod(8)
    def ClearToast(self, instanceId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_IsPhonePinLocked(self) -> Boolean: ...
    @winrt_commethod(10)
    def IncreaseVolume(self, step: Int32) -> Void: ...
    @winrt_commethod(11)
    def DecreaseVolume(self, step: Int32) -> Void: ...
    @winrt_commethod(12)
    def SetMute(self, mute: Boolean) -> Void: ...
    @winrt_commethod(13)
    def SetRingerVibrate(self, ringer: Boolean, vibrate: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_VolumeInfo(self) -> win32more.Windows.Phone.Notification.Management.VolumeInfo: ...
    @winrt_commethod(15)
    def GetAllEmailAccounts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.EmailAccountInfo]: ...
    @winrt_commethod(16)
    def GetFolders(self, emailAccount: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.EmailFolderInfo]: ...
    @winrt_commethod(17)
    def EnableEmailNotificationEmailAccount(self, emailAccount: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def DisableEmailNotificationEmailAccount(self, emailAccount: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def EnableEmailNotificationFolderFilter(self, emailAccount: WinRT_String, folders: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(20)
    def UpdateEmailReadStatus(self, messageEntryId: win32more.Windows.Phone.Notification.Management.BinaryId, isRead: Boolean) -> Void: ...
    IsPhonePinLocked = property(get_IsPhonePinLocked, None)
    SpeedDialList = property(get_SpeedDialList, None)
    VolumeInfo = property(get_VolumeInfo, None)
class IAccessoryManager3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAccessoryManager3'
    _iid_ = Guid('{81f75137-edc7-47e0-b2f7-7e577c833f7d}')
    @winrt_commethod(6)
    def SnoozeAlarmByInstanceId(self, instanceId: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def DismissAlarmByInstanceId(self, instanceId: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def SnoozeReminderByInstanceId(self, instanceId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def DismissReminderByInstanceId(self, instanceId: WinRT_String) -> Void: ...
class IAccessoryNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails'
    _iid_ = Guid('{6968a7d4-e3ca-49cb-8c87-2c11cdff9646}')
    @winrt_commethod(6)
    def get_TimeCreated(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AppDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_AccessoryNotificationType(self) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_commethod(10)
    def get_StartedProcessing(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_StartedProcessing(self, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
class IAlarmNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails'
    _iid_ = Guid('{38f5fa30-c738-4da2-908c-775d83c36abb}')
    @winrt_commethod(6)
    def get_AlarmId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_ReminderState(self) -> win32more.Windows.Phone.Notification.Management.ReminderState: ...
    AlarmId = property(get_AlarmId, None)
    ReminderState = property(get_ReminderState, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
class IAlarmNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAlarmNotificationTriggerDetails2'
    _iid_ = Guid('{cf16e06a-7155-40fe-a9c2-7bd2127ef853}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> WinRT_String: ...
    InstanceId = property(get_InstanceId, None)
class IAppNotificationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IAppNotificationInfo'
    _iid_ = Guid('{2157bea5-e286-45d3-9bea-f790fc216e0e}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Name = property(get_Name, None)
class IBinaryId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IBinaryId'
    _iid_ = Guid('{4f0da531-5595-44b4-9181-ce4efa3fc168}')
    @winrt_commethod(6)
    def get_Id(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    Id = property(get_Id, None)
    Length = property(get_Length, None)
class ICalendarChangedNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.ICalendarChangedNotificationTriggerDetails'
    _iid_ = Guid('{4b8a3bfc-279d-42ab-9c68-3e87977bf216}')
    @winrt_commethod(6)
    def get_EventType(self) -> win32more.Windows.Phone.Notification.Management.CalendarChangedEvent: ...
    @winrt_commethod(7)
    def get_ItemId(self) -> WinRT_String: ...
    EventType = property(get_EventType, None)
    ItemId = property(get_ItemId, None)
class ICortanaTileNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.ICortanaTileNotificationTriggerDetails'
    _iid_ = Guid('{dc0f01d5-1489-46bb-b73b-7f90067ecf27}')
    @winrt_commethod(6)
    def get_TileId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Content(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LargeContent1(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_LargeContent2(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_EmphasizedText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_NonWrappedSmallContent1(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_NonWrappedSmallContent2(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_NonWrappedSmallContent3(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_NonWrappedSmallContent4(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Source(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    EmphasizedText = property(get_EmphasizedText, None)
    LargeContent1 = property(get_LargeContent1, None)
    LargeContent2 = property(get_LargeContent2, None)
    NonWrappedSmallContent1 = property(get_NonWrappedSmallContent1, None)
    NonWrappedSmallContent2 = property(get_NonWrappedSmallContent2, None)
    NonWrappedSmallContent3 = property(get_NonWrappedSmallContent3, None)
    NonWrappedSmallContent4 = property(get_NonWrappedSmallContent4, None)
    Source = property(get_Source, None)
    TileId = property(get_TileId, None)
class IEmailAccountInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IEmailAccountInfo'
    _iid_ = Guid('{dfbc02ab-bda0-4568-927e-b2ede35818a1}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsNotificationEnabled(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    IsNotificationEnabled = property(get_IsNotificationEnabled, None)
class IEmailFolderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IEmailFolderInfo'
    _iid_ = Guid('{c207150e-e237-46d6-90e6-4f529eeac1e2}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsNotificationEnabled(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, None)
    IsNotificationEnabled = property(get_IsNotificationEnabled, None)
class IEmailNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails'
    _iid_ = Guid('{f3b82612-46cf-4e70-8e0d-7b2e04ab492b}')
    @winrt_commethod(6)
    def get_AccountName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParentFolderName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SenderName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SenderAddress(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_EmailMessage(self) -> win32more.Windows.ApplicationModel.Email.EmailMessage: ...
    @winrt_commethod(11)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    AccountName = property(get_AccountName, None)
    EmailMessage = property(get_EmailMessage, None)
    ParentFolderName = property(get_ParentFolderName, None)
    SenderAddress = property(get_SenderAddress, None)
    SenderName = property(get_SenderName, None)
    Timestamp = property(get_Timestamp, None)
class IEmailNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IEmailNotificationTriggerDetails2'
    _iid_ = Guid('{168067e3-c56f-4ec7-bed1-f734e08de5b2}')
    @winrt_commethod(6)
    def get_MessageEntryId(self) -> win32more.Windows.Phone.Notification.Management.BinaryId: ...
    MessageEntryId = property(get_MessageEntryId, None)
class IEmailReadNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IEmailReadNotificationTriggerDetails'
    _iid_ = Guid('{f5b7a087-06f3-4e3e-8c42-325e67010413}')
    @winrt_commethod(6)
    def get_AccountName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ParentFolderName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MessageEntryId(self) -> win32more.Windows.Phone.Notification.Management.BinaryId: ...
    @winrt_commethod(9)
    def get_IsRead(self) -> Boolean: ...
    AccountName = property(get_AccountName, None)
    IsRead = property(get_IsRead, None)
    MessageEntryId = property(get_MessageEntryId, None)
    ParentFolderName = property(get_ParentFolderName, None)
class IMediaControlsTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IMediaControlsTriggerDetails'
    _iid_ = Guid('{fab4648b-ae45-4548-91ca-4ab0548e33b5}')
    @winrt_commethod(6)
    def get_PlaybackStatus(self) -> win32more.Windows.Phone.Notification.Management.PlaybackStatus: ...
    @winrt_commethod(7)
    def get_MediaMetadata(self) -> win32more.Windows.Phone.Notification.Management.MediaMetadata: ...
    MediaMetadata = property(get_MediaMetadata, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
class IMediaMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IMediaMetadata'
    _iid_ = Guid('{9b50ddf7-bb6c-4330-b3cd-0704a54cdb80}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Subtitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Artist(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Album(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Track(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    Album = property(get_Album, None)
    Artist = property(get_Artist, None)
    Duration = property(get_Duration, None)
    Subtitle = property(get_Subtitle, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
    Track = property(get_Track, None)
class IPhoneCallDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IPhoneCallDetails'
    _iid_ = Guid('{0c1b6f53-f071-483e-bf33-ebd44b724447}')
    @winrt_commethod(6)
    def get_PhoneLine(self) -> Guid: ...
    @winrt_commethod(7)
    def get_CallId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_CallTransport(self) -> win32more.Windows.Phone.Notification.Management.PhoneCallTransport: ...
    @winrt_commethod(9)
    def get_CallMediaType(self) -> win32more.Windows.Phone.Notification.Management.PhoneMediaType: ...
    @winrt_commethod(10)
    def get_CallDirection(self) -> win32more.Windows.Phone.Notification.Management.PhoneCallDirection: ...
    @winrt_commethod(11)
    def get_State(self) -> win32more.Windows.Phone.Notification.Management.PhoneCallState: ...
    @winrt_commethod(12)
    def get_ConferenceCallId(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(14)
    def get_EndTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_ContactName(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_PresetTextResponses(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.TextResponse]: ...
    CallDirection = property(get_CallDirection, None)
    CallId = property(get_CallId, None)
    CallMediaType = property(get_CallMediaType, None)
    CallTransport = property(get_CallTransport, None)
    ConferenceCallId = property(get_ConferenceCallId, None)
    ContactName = property(get_ContactName, None)
    EndTime = property(get_EndTime, None)
    PhoneLine = property(get_PhoneLine, None)
    PhoneNumber = property(get_PhoneNumber, None)
    PresetTextResponses = property(get_PresetTextResponses, None)
    StartTime = property(get_StartTime, None)
    State = property(get_State, None)
class IPhoneLineDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IPhoneLineDetails'
    _iid_ = Guid('{47eb32dc-33ed-49b9-995c-a296bac82b77}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LineNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DefaultOutgoingLine(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_VoicemailCount(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_RegistrationState(self) -> win32more.Windows.Phone.Notification.Management.PhoneLineRegistrationState: ...
    DefaultOutgoingLine = property(get_DefaultOutgoingLine, None)
    DisplayName = property(get_DisplayName, None)
    LineId = property(get_LineId, None)
    LineNumber = property(get_LineNumber, None)
    RegistrationState = property(get_RegistrationState, None)
    VoicemailCount = property(get_VoicemailCount, None)
class IPhoneLineDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IPhoneLineDetails2'
    _iid_ = Guid('{b30cd77d-0147-498c-8241-bf0cabc60a25}')
    @winrt_commethod(6)
    def get_MissedCallCount(self) -> UInt32: ...
    MissedCallCount = property(get_MissedCallCount, None)
class IPhoneNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IPhoneNotificationTriggerDetails'
    _iid_ = Guid('{ccc2fdf7-09c3-4118-91bc-ca6323a8d383}')
    @winrt_commethod(6)
    def get_PhoneNotificationType(self) -> win32more.Windows.Phone.Notification.Management.PhoneNotificationType: ...
    @winrt_commethod(7)
    def get_CallDetails(self) -> win32more.Windows.Phone.Notification.Management.PhoneCallDetails: ...
    @winrt_commethod(8)
    def get_PhoneLineChangedId(self) -> Guid: ...
    CallDetails = property(get_CallDetails, None)
    PhoneLineChangedId = property(get_PhoneLineChangedId, None)
    PhoneNotificationType = property(get_PhoneNotificationType, None)
class IReminderNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails'
    _iid_ = Guid('{5bddaa5d-9f61-4bf0-9feb-10502bc0b0c2}')
    @winrt_commethod(6)
    def get_ReminderId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Details(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Appointment(self) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_commethod(12)
    def get_ReminderState(self) -> win32more.Windows.Phone.Notification.Management.ReminderState: ...
    Appointment = property(get_Appointment, None)
    Description = property(get_Description, None)
    Details = property(get_Details, None)
    ReminderId = property(get_ReminderId, None)
    ReminderState = property(get_ReminderState, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
class IReminderNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails2'
    _iid_ = Guid('{e715f9c0-504d-4c0f-a6b3-bcb9722c6cdd}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> WinRT_String: ...
    InstanceId = property(get_InstanceId, None)
class ISpeedDialEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.ISpeedDialEntry'
    _iid_ = Guid('{9240b6db-872c-46dc-b62a-be4541b166f8}')
    @winrt_commethod(6)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_NumberType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ContactName(self) -> WinRT_String: ...
    ContactName = property(get_ContactName, None)
    NumberType = property(get_NumberType, None)
    PhoneNumber = property(get_PhoneNumber, None)
class ITextResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.ITextResponse'
    _iid_ = Guid('{e9cb74c3-2457-4cdb-8110-72f5e8e883e8}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Content(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    Id = property(get_Id, None)
class IToastNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IToastNotificationTriggerDetails'
    _iid_ = Guid('{c9314895-4e6d-4e9d-afec-9e921b875ae8}')
    @winrt_commethod(6)
    def get_Text1(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Text2(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Text3(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Text4(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SuppressPopup(self) -> Boolean: ...
    SuppressPopup = property(get_SuppressPopup, None)
    Text1 = property(get_Text1, None)
    Text2 = property(get_Text2, None)
    Text3 = property(get_Text3, None)
    Text4 = property(get_Text4, None)
class IToastNotificationTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IToastNotificationTriggerDetails2'
    _iid_ = Guid('{3e0479dd-cac4-4f60-afa3-b925d9d83c93}')
    @winrt_commethod(6)
    def get_InstanceId(self) -> WinRT_String: ...
    InstanceId = property(get_InstanceId, None)
class IVolumeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Notification.Management.IVolumeInfo'
    _iid_ = Guid('{944dd118-7704-4481-b92e-d3ed3ece6322}')
    @winrt_commethod(6)
    def get_SystemVolume(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CallVolume(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MediaVolume(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_IsMuted(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsVibrateEnabled(self) -> win32more.Windows.Phone.Notification.Management.VibrateState: ...
    CallVolume = property(get_CallVolume, None)
    IsMuted = property(get_IsMuted, None)
    IsVibrateEnabled = property(get_IsVibrateEnabled, None)
    MediaVolume = property(get_MediaVolume, None)
    SystemVolume = property(get_SystemVolume, None)
class MediaControlsTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IMediaControlsTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.MediaControlsTriggerDetails'
    @winrt_mixinmethod
    def get_PlaybackStatus(self: win32more.Windows.Phone.Notification.Management.IMediaControlsTriggerDetails) -> win32more.Windows.Phone.Notification.Management.PlaybackStatus: ...
    @winrt_mixinmethod
    def get_MediaMetadata(self: win32more.Windows.Phone.Notification.Management.IMediaControlsTriggerDetails) -> win32more.Windows.Phone.Notification.Management.MediaMetadata: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    MediaMetadata = property(get_MediaMetadata, None)
    PlaybackStatus = property(get_PlaybackStatus, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
class MediaMetadata(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IMediaMetadata
    _classid_ = 'Windows.Phone.Notification.Management.MediaMetadata'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subtitle(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Artist(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Album(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Track(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> UInt32: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Phone.Notification.Management.IMediaMetadata) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    Album = property(get_Album, None)
    Artist = property(get_Artist, None)
    Duration = property(get_Duration, None)
    Subtitle = property(get_Subtitle, None)
    Thumbnail = property(get_Thumbnail, None)
    Title = property(get_Title, None)
    Track = property(get_Track, None)
class PhoneCallAudioEndpoint(Enum, Int32):
    Default = 0
    Speaker = 1
    Handsfree = 2
class PhoneCallDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails
    _classid_ = 'Windows.Phone.Notification.Management.PhoneCallDetails'
    @winrt_mixinmethod
    def get_PhoneLine(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_CallId(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_CallTransport(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Phone.Notification.Management.PhoneCallTransport: ...
    @winrt_mixinmethod
    def get_CallMediaType(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Phone.Notification.Management.PhoneMediaType: ...
    @winrt_mixinmethod
    def get_CallDirection(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Phone.Notification.Management.PhoneCallDirection: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Phone.Notification.Management.PhoneCallState: ...
    @winrt_mixinmethod
    def get_ConferenceCallId(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactName(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PresetTextResponses(self: win32more.Windows.Phone.Notification.Management.IPhoneCallDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.Notification.Management.TextResponse]: ...
    CallDirection = property(get_CallDirection, None)
    CallId = property(get_CallId, None)
    CallMediaType = property(get_CallMediaType, None)
    CallTransport = property(get_CallTransport, None)
    ConferenceCallId = property(get_ConferenceCallId, None)
    ContactName = property(get_ContactName, None)
    EndTime = property(get_EndTime, None)
    PhoneLine = property(get_PhoneLine, None)
    PhoneNumber = property(get_PhoneNumber, None)
    PresetTextResponses = property(get_PresetTextResponses, None)
    StartTime = property(get_StartTime, None)
    State = property(get_State, None)
class PhoneCallDirection(Enum, Int32):
    Incoming = 0
    Outgoing = 1
class PhoneCallState(Enum, Int32):
    Unknown = 0
    Ringing = 1
    Talking = 2
    Held = 3
    Ended = 4
class PhoneCallTransport(Enum, Int32):
    Cellular = 0
    Voip = 1
class PhoneLineDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails
    _classid_ = 'Windows.Phone.Notification.Management.PhoneLineDetails'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LineNumber(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultOutgoingLine(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_VoicemailCount(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_RegistrationState(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails) -> win32more.Windows.Phone.Notification.Management.PhoneLineRegistrationState: ...
    @winrt_mixinmethod
    def get_MissedCallCount(self: win32more.Windows.Phone.Notification.Management.IPhoneLineDetails2) -> UInt32: ...
    DefaultOutgoingLine = property(get_DefaultOutgoingLine, None)
    DisplayName = property(get_DisplayName, None)
    LineId = property(get_LineId, None)
    LineNumber = property(get_LineNumber, None)
    MissedCallCount = property(get_MissedCallCount, None)
    RegistrationState = property(get_RegistrationState, None)
    VoicemailCount = property(get_VoicemailCount, None)
class PhoneLineRegistrationState(Enum, Int32):
    Disconnected = 0
    Home = 1
    Roaming = 2
class PhoneMediaType(Enum, Int32):
    AudioOnly = 0
    AudioVideo = 1
class PhoneNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IPhoneNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.PhoneNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_PhoneNotificationType(self: win32more.Windows.Phone.Notification.Management.IPhoneNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.PhoneNotificationType: ...
    @winrt_mixinmethod
    def get_CallDetails(self: win32more.Windows.Phone.Notification.Management.IPhoneNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.PhoneCallDetails: ...
    @winrt_mixinmethod
    def get_PhoneLineChangedId(self: win32more.Windows.Phone.Notification.Management.IPhoneNotificationTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    CallDetails = property(get_CallDetails, None)
    PhoneLineChangedId = property(get_PhoneLineChangedId, None)
    PhoneNotificationType = property(get_PhoneNotificationType, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
class PhoneNotificationType(Enum, Int32):
    NewCall = 0
    CallChanged = 1
    LineChanged = 2
    PhoneCallAudioEndpointChanged = 3
    PhoneMuteChanged = 4
class PlaybackCapability(Enum, UInt32):
    None_ = 0
    Play = 1
    Pause = 2
    Stop = 4
    Record = 8
    FastForward = 16
    Rewind = 32
    Next = 64
    Previous = 128
    ChannelUp = 256
    ChannelDown = 512
class PlaybackCommand(Enum, Int32):
    Play = 0
    Pause = 1
    Stop = 2
    Record = 3
    FastForward = 4
    Rewind = 5
    Next = 6
    Previous = 7
    ChannelUp = 8
    ChannelDown = 9
class PlaybackStatus(Enum, Int32):
    None_ = 0
    TrackChanged = 1
    Stopped = 2
    Playing = 3
    Paused = 4
class ReminderNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.ReminderNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_ReminderId(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> Guid: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Details(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Appointment(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_ReminderState(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.ReminderState: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.Phone.Notification.Management.IReminderNotificationTriggerDetails2) -> WinRT_String: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    Appointment = property(get_Appointment, None)
    Description = property(get_Description, None)
    Details = property(get_Details, None)
    InstanceId = property(get_InstanceId, None)
    ReminderId = property(get_ReminderId, None)
    ReminderState = property(get_ReminderState, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    TimeCreated = property(get_TimeCreated, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
class ReminderState(Enum, Int32):
    Active = 0
    Snoozed = 1
    Dismissed = 2
class SpeedDialEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.ISpeedDialEntry
    _classid_ = 'Windows.Phone.Notification.Management.SpeedDialEntry'
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.Phone.Notification.Management.ISpeedDialEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NumberType(self: win32more.Windows.Phone.Notification.Management.ISpeedDialEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactName(self: win32more.Windows.Phone.Notification.Management.ISpeedDialEntry) -> WinRT_String: ...
    ContactName = property(get_ContactName, None)
    NumberType = property(get_NumberType, None)
    PhoneNumber = property(get_PhoneNumber, None)
class TextResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.ITextResponse
    _classid_ = 'Windows.Phone.Notification.Management.TextResponse'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.Notification.Management.ITextResponse) -> UInt32: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Phone.Notification.Management.ITextResponse) -> WinRT_String: ...
    Content = property(get_Content, None)
    Id = property(get_Id, None)
class ToastNotificationTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails
    _classid_ = 'Windows.Phone.Notification.Management.ToastNotificationTriggerDetails'
    @winrt_mixinmethod
    def get_Text1(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text2(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text3(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Text4(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SuppressPopup(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_TimeCreated(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccessoryNotificationType(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> win32more.Windows.Phone.Notification.Management.AccessoryNotificationType: ...
    @winrt_mixinmethod
    def get_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails) -> Boolean: ...
    @winrt_mixinmethod
    def put_StartedProcessing(self: win32more.Windows.Phone.Notification.Management.IAccessoryNotificationTriggerDetails, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.Phone.Notification.Management.IToastNotificationTriggerDetails2) -> WinRT_String: ...
    AccessoryNotificationType = property(get_AccessoryNotificationType, None)
    AppDisplayName = property(get_AppDisplayName, None)
    AppId = property(get_AppId, None)
    InstanceId = property(get_InstanceId, None)
    StartedProcessing = property(get_StartedProcessing, put_StartedProcessing)
    SuppressPopup = property(get_SuppressPopup, None)
    Text1 = property(get_Text1, None)
    Text2 = property(get_Text2, None)
    Text3 = property(get_Text3, None)
    Text4 = property(get_Text4, None)
    TimeCreated = property(get_TimeCreated, None)
class VibrateState(Enum, Int32):
    RingerOffVibrateOff = 0
    RingerOffVibrateOn = 1
    RingerOnVibrateOff = 2
    RingerOnVibrateOn = 3
class VolumeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Notification.Management.IVolumeInfo
    _classid_ = 'Windows.Phone.Notification.Management.VolumeInfo'
    @winrt_mixinmethod
    def get_SystemVolume(self: win32more.Windows.Phone.Notification.Management.IVolumeInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_CallVolume(self: win32more.Windows.Phone.Notification.Management.IVolumeInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_MediaVolume(self: win32more.Windows.Phone.Notification.Management.IVolumeInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsMuted(self: win32more.Windows.Phone.Notification.Management.IVolumeInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVibrateEnabled(self: win32more.Windows.Phone.Notification.Management.IVolumeInfo) -> win32more.Windows.Phone.Notification.Management.VibrateState: ...
    CallVolume = property(get_CallVolume, None)
    IsMuted = property(get_IsMuted, None)
    IsVibrateEnabled = property(get_IsVibrateEnabled, None)
    MediaVolume = property(get_MediaVolume, None)
    SystemVolume = property(get_SystemVolume, None)


make_ready(__name__)
