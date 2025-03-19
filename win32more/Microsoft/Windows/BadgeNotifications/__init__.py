from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.BadgeNotifications
import win32more.Windows.Win32.System.WinRT
class BadgeNotificationGlyph(Enum, Int32):
    None_ = 0
    Activity = 1
    Alarm = 2
    Alert = 3
    Attention = 4
    Available = 5
    Away = 6
    Busy = 7
    Error = 8
    NewMessage = 9
    Paused = 10
    Playing = 11
    Unavailable = 12
class _BadgeNotificationManager_Meta_(ComPtr.__class__):
    pass
class BadgeNotificationManager(ComPtr, metaclass=_BadgeNotificationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager
    _classid_ = 'Microsoft.Windows.BadgeNotifications.BadgeNotificationManager'
    @winrt_mixinmethod
    def SetBadgeAsCount(self: win32more.Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager, notificationCount: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetBadgeAsGlyph(self: win32more.Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager, glyphValue: win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationGlyph) -> Void: ...
    @winrt_mixinmethod
    def ClearBadge(self: win32more.Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Microsoft.Windows.BadgeNotifications.IBadgeNotificationManagerStatics) -> win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationManager: ...
    _BadgeNotificationManager_Meta_.Current = property(get_Current, None)
BadgeNotificationsContract: UInt32 = 65536
class IBadgeNotificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager'
    _iid_ = Guid('{11cb6e8f-11ca-53f8-80f6-5330d44ba908}')
    @winrt_commethod(6)
    def SetBadgeAsCount(self, notificationCount: UInt32) -> Void: ...
    @winrt_commethod(7)
    def SetBadgeAsGlyph(self, glyphValue: win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationGlyph) -> Void: ...
    @winrt_commethod(8)
    def ClearBadge(self) -> Void: ...
class IBadgeNotificationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.BadgeNotifications.IBadgeNotificationManagerStatics'
    _iid_ = Guid('{a6e71616-7c9f-5d22-ad1c-f4ab874087b5}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationManager: ...
    Current = property(get_Current, None)


make_ready(__name__)
