from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Notifications
import win32more.Windows.UI.Notifications.Management
import win32more.Windows.Win32.System.WinRT
class IUserNotificationListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Management.IUserNotificationListener'
    _iid_ = Guid('{62553e41-8a06-4cef-8215-6033a5be4b03}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]: ...
    @winrt_commethod(7)
    def GetAccessStatus(self) -> win32more.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus: ...
    @winrt_commethod(8)
    def add_NotificationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.Management.UserNotificationListener, win32more.Windows.UI.Notifications.UserNotificationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_NotificationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetNotificationsAsync(self, kinds: win32more.Windows.UI.Notifications.NotificationKinds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.UserNotification]]: ...
    @winrt_commethod(11)
    def GetNotification(self, notificationId: UInt32) -> win32more.Windows.UI.Notifications.UserNotification: ...
    @winrt_commethod(12)
    def ClearNotifications(self) -> Void: ...
    @winrt_commethod(13)
    def RemoveNotification(self, notificationId: UInt32) -> Void: ...
    NotificationChanged = event()
class IUserNotificationListenerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Management.IUserNotificationListenerStatics'
    _iid_ = Guid('{ff6123cf-4386-4aa3-b73d-b804e5b63b23}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.Notifications.Management.UserNotificationListener: ...
    Current = property(get_Current, None)
class _UserNotificationListener_Meta_(ComPtr.__class__):
    pass
class UserNotificationListener(ComPtr, metaclass=_UserNotificationListener_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.Management.IUserNotificationListener
    _classid_ = 'Windows.UI.Notifications.Management.UserNotificationListener'
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]: ...
    @winrt_mixinmethod
    def GetAccessStatus(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener) -> win32more.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus: ...
    @winrt_mixinmethod
    def add_NotificationChanged(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.Management.UserNotificationListener, win32more.Windows.UI.Notifications.UserNotificationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationChanged(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetNotificationsAsync(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener, kinds: win32more.Windows.UI.Notifications.NotificationKinds) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.UserNotification]]: ...
    @winrt_mixinmethod
    def GetNotification(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener, notificationId: UInt32) -> win32more.Windows.UI.Notifications.UserNotification: ...
    @winrt_mixinmethod
    def ClearNotifications(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener) -> Void: ...
    @winrt_mixinmethod
    def RemoveNotification(self: win32more.Windows.UI.Notifications.Management.IUserNotificationListener, notificationId: UInt32) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.Notifications.Management.IUserNotificationListenerStatics) -> win32more.Windows.UI.Notifications.Management.UserNotificationListener: ...
    _UserNotificationListener_Meta_.Current = property(get_Current, None)
    NotificationChanged = event()
class UserNotificationListenerAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    Denied = 2


make_ready(__name__)
