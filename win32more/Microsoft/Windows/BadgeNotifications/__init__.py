from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.BadgeNotifications
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
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.BadgeNotifications.IBadgeNotificationManager'
    _iid_ = Guid('{11cb6e8f-11ca-53f8-80f6-5330d44ba908}')
    @winrt_commethod(6)
    def SetBadgeAsCount(self, notificationCount: UInt32) -> Void: ...
    @winrt_commethod(7)
    def SetBadgeAsGlyph(self, glyphValue: win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationGlyph) -> Void: ...
    @winrt_commethod(8)
    def ClearBadge(self) -> Void: ...
class IBadgeNotificationManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.BadgeNotifications.IBadgeNotificationManagerStatics'
    _iid_ = Guid('{a6e71616-7c9f-5d22-ad1c-f4ab874087b5}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Microsoft.Windows.BadgeNotifications.BadgeNotificationManager: ...
    Current = property(get_Current, None)


make_ready(__name__)
