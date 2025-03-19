from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.AppNotifications
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class AppNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppNotifications.IAppNotification
    _classid_ = 'Microsoft.Windows.AppNotifications.AppNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AppNotifications.AppNotification.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AppNotifications.IAppNotificationFactory, payload: WinRT_String) -> win32more.Microsoft.Windows.AppNotifications.AppNotification: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> UInt32: ...
    @winrt_mixinmethod
    def get_Payload(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData) -> Void: ...
    @winrt_mixinmethod
    def get_Expiration(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Expiration(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_ExpiresOnReboot(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExpiresOnReboot(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: win32more.Microsoft.Windows.AppNotifications.AppNotificationPriority) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressDisplay(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressDisplay(self: win32more.Microsoft.Windows.AppNotifications.IAppNotification, value: Boolean) -> Void: ...
    Expiration = property(get_Expiration, put_Expiration)
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
    Group = property(get_Group, put_Group)
    Id = property(get_Id, None)
    Payload = property(get_Payload, None)
    Priority = property(get_Priority, put_Priority)
    Progress = property(get_Progress, put_Progress)
    SuppressDisplay = property(get_SuppressDisplay, put_SuppressDisplay)
    Tag = property(get_Tag, put_Tag)
class AppNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs
    _classid_ = 'Microsoft.Windows.AppNotifications.AppNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs2) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Argument = property(get_Argument, None)
    Arguments = property(get_Arguments, None)
    UserInput = property(get_UserInput, None)
class _AppNotificationManager_Meta_(ComPtr.__class__):
    pass
class AppNotificationManager(ComPtr, metaclass=_AppNotificationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager
    _classid_ = 'Microsoft.Windows.AppNotifications.AppNotificationManager'
    @winrt_overload
    @winrt_mixinmethod
    def Register(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def UnregisterAll(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def add_NotificationInvoked(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.AppNotifications.AppNotificationManager, win32more.Microsoft.Windows.AppNotifications.AppNotificationActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationInvoked(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Show(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, notification: win32more.Microsoft.Windows.AppNotifications.AppNotification) -> Void: ...
    @winrt_mixinmethod
    def UpdateAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, data: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]: ...
    @winrt_mixinmethod
    def UpdateAsync2(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, data: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData, tag: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]: ...
    @winrt_mixinmethod
    def get_Setting(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationSetting: ...
    @winrt_mixinmethod
    def RemoveByIdAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, notificationId: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveByTagAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, tag: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveByTagAndGroupAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveByGroupAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveAllAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetAllAsync(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AppNotifications.AppNotification]]: ...
    @Register.register
    @winrt_mixinmethod
    def Register(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManager2, displayName: WinRT_String, iconUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_Default(cls: win32more.Microsoft.Windows.AppNotifications.IAppNotificationManagerStatics) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationManager: ...
    Setting = property(get_Setting, None)
    _AppNotificationManager_Meta_.Default = property(get_Default, None)
    NotificationInvoked = event()
class AppNotificationPriority(Enum, Int32):
    Default = 0
    High = 1
class AppNotificationProgressData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData
    _classid_ = 'Microsoft.Windows.AppNotifications.AppNotificationProgressData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressDataFactory, sequenceNumber: UInt32) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData: ...
    @winrt_mixinmethod
    def get_SequenceNumber(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData) -> UInt32: ...
    @winrt_mixinmethod
    def put_SequenceNumber(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData) -> Double: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ValueStringOverride(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ValueStringOverride(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Microsoft.Windows.AppNotifications.IAppNotificationProgressData, value: WinRT_String) -> Void: ...
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
    Status = property(get_Status, put_Status)
    Title = property(get_Title, put_Title)
    Value = property(get_Value, put_Value)
    ValueStringOverride = property(get_ValueStringOverride, put_ValueStringOverride)
class AppNotificationProgressResult(Enum, Int32):
    Succeeded = 0
    AppNotificationNotFound = 1
    Unsupported = 2
class AppNotificationSetting(Enum, Int32):
    Enabled = 0
    DisabledForApplication = 1
    DisabledForUser = 2
    DisabledByGroupPolicy = 3
    DisabledByManifest = 4
    Unsupported = 5
AppNotificationsContract: UInt32 = 262144
class IAppNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotification'
    _iid_ = Guid('{373a6917-4116-5657-936a-15f99afdd667}')
    @winrt_commethod(6)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Group(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Payload(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Progress(self) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData: ...
    @winrt_commethod(13)
    def put_Progress(self, value: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData) -> Void: ...
    @winrt_commethod(14)
    def get_Expiration(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def put_Expiration(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(16)
    def get_ExpiresOnReboot(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_ExpiresOnReboot(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_Priority(self) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationPriority: ...
    @winrt_commethod(19)
    def put_Priority(self, value: win32more.Microsoft.Windows.AppNotifications.AppNotificationPriority) -> Void: ...
    @winrt_commethod(20)
    def get_SuppressDisplay(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_SuppressDisplay(self, value: Boolean) -> Void: ...
    Expiration = property(get_Expiration, put_Expiration)
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
    Group = property(get_Group, put_Group)
    Id = property(get_Id, None)
    Payload = property(get_Payload, None)
    Priority = property(get_Priority, put_Priority)
    Progress = property(get_Progress, put_Progress)
    SuppressDisplay = property(get_SuppressDisplay, put_SuppressDisplay)
    Tag = property(get_Tag, put_Tag)
class IAppNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs'
    _iid_ = Guid('{7a8afaf9-31cb-51d5-82be-db6bd5878b77}')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IAppNotificationActivatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationActivatedEventArgs2'
    _iid_ = Guid('{52c06b9b-2c50-5037-9416-a3be47b9d5bd}')
    @winrt_commethod(6)
    def get_Arguments(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Arguments = property(get_Arguments, None)
class IAppNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationFactory'
    _iid_ = Guid('{9ffee485-184a-5c65-87a9-c1d94469dbe7}')
    @winrt_commethod(6)
    def CreateInstance(self, payload: WinRT_String) -> win32more.Microsoft.Windows.AppNotifications.AppNotification: ...
class IAppNotificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationManager'
    _iid_ = Guid('{55129688-b4bd-550b-ae6b-c24061954d91}')
    @winrt_commethod(6)
    def Register(self) -> Void: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def UnregisterAll(self) -> Void: ...
    @winrt_commethod(9)
    def add_NotificationInvoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.AppNotifications.AppNotificationManager, win32more.Microsoft.Windows.AppNotifications.AppNotificationActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_NotificationInvoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Show(self, notification: win32more.Microsoft.Windows.AppNotifications.AppNotification) -> Void: ...
    @winrt_commethod(12)
    def UpdateAsync(self, data: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]: ...
    @winrt_commethod(13)
    def UpdateAsync2(self, data: win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData, tag: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]: ...
    @winrt_commethod(14)
    def get_Setting(self) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationSetting: ...
    @winrt_commethod(15)
    def RemoveByIdAsync(self, notificationId: UInt32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def RemoveByTagAsync(self, tag: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def RemoveByTagAndGroupAsync(self, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def RemoveByGroupAsync(self, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def RemoveAllAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def GetAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AppNotifications.AppNotification]]: ...
    Setting = property(get_Setting, None)
    NotificationInvoked = event()
class IAppNotificationManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationManager2'
    _iid_ = Guid('{38ba268d-e0c7-522e-a79d-8a29dcdd7135}')
    @winrt_commethod(6)
    def Register(self, displayName: WinRT_String, iconUri: win32more.Windows.Foundation.Uri) -> Void: ...
class IAppNotificationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationManagerStatics'
    _iid_ = Guid('{6cfc0d8d-84a3-5592-b4c6-e3e7e7c680e4}')
    @winrt_commethod(6)
    def get_Default(self) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationManager: ...
    Default = property(get_Default, None)
class IAppNotificationManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationManagerStatics2'
    _iid_ = Guid('{6eb42a35-e82f-5732-98f1-129705602f2e}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IAppNotificationProgressData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationProgressData'
    _iid_ = Guid('{4debfac0-809d-55cb-b879-924821876b97}')
    @winrt_commethod(6)
    def get_SequenceNumber(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_SequenceNumber(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> Double: ...
    @winrt_commethod(11)
    def put_Value(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_ValueStringOverride(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_ValueStringOverride(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Status(self, value: WinRT_String) -> Void: ...
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
    Status = property(get_Status, put_Status)
    Title = property(get_Title, put_Title)
    Value = property(get_Value, put_Value)
    ValueStringOverride = property(get_ValueStringOverride, put_ValueStringOverride)
class IAppNotificationProgressDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppNotifications.IAppNotificationProgressDataFactory'
    _iid_ = Guid('{c08e4a0f-3a75-55d6-8c3e-14f03ae46046}')
    @winrt_commethod(6)
    def CreateInstance(self, sequenceNumber: UInt32) -> win32more.Microsoft.Windows.AppNotifications.AppNotificationProgressData: ...


make_ready(__name__)
