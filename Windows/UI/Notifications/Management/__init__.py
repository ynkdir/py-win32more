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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI.Notifications
import Windows.UI.Notifications.Management
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUserNotificationListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Management.IUserNotificationListener'
    _iid_ = Guid('{62553e41-8a06-4cef-8215-6033a5be4b03}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]: ...
    @winrt_commethod(7)
    def GetAccessStatus(self) -> Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus: ...
    @winrt_commethod(8)
    def add_NotificationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.Management.UserNotificationListener, Windows.UI.Notifications.UserNotificationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_NotificationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetNotificationsAsync(self, kinds: Windows.UI.Notifications.NotificationKinds) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.UserNotification]]: ...
    @winrt_commethod(11)
    def GetNotification(self, notificationId: UInt32) -> Windows.UI.Notifications.UserNotification: ...
    @winrt_commethod(12)
    def ClearNotifications(self) -> Void: ...
    @winrt_commethod(13)
    def RemoveNotification(self, notificationId: UInt32) -> Void: ...
class IUserNotificationListenerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Management.IUserNotificationListenerStatics'
    _iid_ = Guid('{ff6123cf-4386-4aa3-b73d-b804e5b63b23}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.UI.Notifications.Management.UserNotificationListener: ...
    Current = property(get_Current, None)
class UserNotificationListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Notifications.Management.IUserNotificationListener
    _classid_ = 'Windows.UI.Notifications.Management.UserNotificationListener'
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.UI.Notifications.Management.IUserNotificationListener) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]: ...
    @winrt_mixinmethod
    def GetAccessStatus(self: Windows.UI.Notifications.Management.IUserNotificationListener) -> Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus: ...
    @winrt_mixinmethod
    def add_NotificationChanged(self: Windows.UI.Notifications.Management.IUserNotificationListener, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.Management.UserNotificationListener, Windows.UI.Notifications.UserNotificationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationChanged(self: Windows.UI.Notifications.Management.IUserNotificationListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetNotificationsAsync(self: Windows.UI.Notifications.Management.IUserNotificationListener, kinds: Windows.UI.Notifications.NotificationKinds) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.UserNotification]]: ...
    @winrt_mixinmethod
    def GetNotification(self: Windows.UI.Notifications.Management.IUserNotificationListener, notificationId: UInt32) -> Windows.UI.Notifications.UserNotification: ...
    @winrt_mixinmethod
    def ClearNotifications(self: Windows.UI.Notifications.Management.IUserNotificationListener) -> Void: ...
    @winrt_mixinmethod
    def RemoveNotification(self: Windows.UI.Notifications.Management.IUserNotificationListener, notificationId: UInt32) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: Windows.UI.Notifications.Management.IUserNotificationListenerStatics) -> Windows.UI.Notifications.Management.UserNotificationListener: ...
    Current = property(get_Current, None)
UserNotificationListenerAccessStatus = Int32
UserNotificationListenerAccessStatus_Unspecified: UserNotificationListenerAccessStatus = 0
UserNotificationListenerAccessStatus_Allowed: UserNotificationListenerAccessStatus = 1
UserNotificationListenerAccessStatus_Denied: UserNotificationListenerAccessStatus = 2
make_head(_module, 'IUserNotificationListener')
make_head(_module, 'IUserNotificationListenerStatics')
make_head(_module, 'UserNotificationListener')
