from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Notifications
import win32more.Windows.UI.Notifications.Management
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
    _UserNotificationListener_Meta_.Current = property(get_Current.__wrapped__, None)
UserNotificationListenerAccessStatus = Int32
UserNotificationListenerAccessStatus_Unspecified: UserNotificationListenerAccessStatus = 0
UserNotificationListenerAccessStatus_Allowed: UserNotificationListenerAccessStatus = 1
UserNotificationListenerAccessStatus_Denied: UserNotificationListenerAccessStatus = 2
make_ready(__name__)
