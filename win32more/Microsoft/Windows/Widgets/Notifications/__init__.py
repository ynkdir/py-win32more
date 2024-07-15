from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.Widgets.Notifications
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class AnnouncementActionKind(Enum, Int32):
    Shown = 0
    Engaged = 1
class AnnouncementTextColor(Enum, Int32):
    Default = 0
    Dark = 1
    Light = 2
    Accent = 3
    Good = 4
    Warning = 5
    Attention = 6
class FeedAnnouncement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement
    _classid_ = 'Microsoft.Windows.Widgets.Notifications.FeedAnnouncement'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 5:
            super().__init__(move=win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncement.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementFactory, id: WinRT_String, primaryText: WinRT_String, secondaryText: WinRT_String, lightModeIcon: win32more.Windows.Foundation.Uri, darkModeIcon: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncement: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PrimaryText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrimaryText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SecondaryText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SecondaryText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LightModeIconUri(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_LightModeIconUri(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DarkModeIconUri(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_DarkModeIconUri(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_PrimaryTextColor(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor: ...
    @winrt_mixinmethod
    def put_PrimaryTextColor(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor) -> Void: ...
    @winrt_mixinmethod
    def get_SecondaryTextColor(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor: ...
    @winrt_mixinmethod
    def put_SecondaryTextColor(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor) -> Void: ...
    @winrt_mixinmethod
    def get_CustomAccessibilityText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CustomAccessibilityText(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsSecondaryTextSubtle(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSecondaryTextSubtle(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowBadgeIfUserNotEngaged(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowBadgeIfUserNotEngaged(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    CustomAccessibilityText = property(get_CustomAccessibilityText, put_CustomAccessibilityText)
    DarkModeIconUri = property(get_DarkModeIconUri, put_DarkModeIconUri)
    Duration = property(get_Duration, put_Duration)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Id = property(get_Id, put_Id)
    IsSecondaryTextSubtle = property(get_IsSecondaryTextSubtle, put_IsSecondaryTextSubtle)
    LightModeIconUri = property(get_LightModeIconUri, put_LightModeIconUri)
    PrimaryText = property(get_PrimaryText, put_PrimaryText)
    PrimaryTextColor = property(get_PrimaryTextColor, put_PrimaryTextColor)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    SecondaryTextColor = property(get_SecondaryTextColor, put_SecondaryTextColor)
    ShowBadgeIfUserNotEngaged = property(get_ShowBadgeIfUserNotEngaged, put_ShowBadgeIfUserNotEngaged)
class FeedAnnouncementInvokedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Notifications.FeedAnnouncementInvokedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AnnouncementId(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: win32more.Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementActionKind: ...
    ActionKind = property(get_ActionKind, None)
    AnnouncementId = property(get_AnnouncementId, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedAnnouncement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Notifications.IFeedAnnouncement'
    _iid_ = Guid('{b88e8c2c-d251-5344-acc2-8cf9ba07ec15}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_PrimaryText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_PrimaryText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SecondaryText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_SecondaryText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_LightModeIconUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_LightModeIconUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(14)
    def get_DarkModeIconUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(15)
    def put_DarkModeIconUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(16)
    def get_PrimaryTextColor(self) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor: ...
    @winrt_commethod(17)
    def put_PrimaryTextColor(self, value: win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor) -> Void: ...
    @winrt_commethod(18)
    def get_SecondaryTextColor(self) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor: ...
    @winrt_commethod(19)
    def put_SecondaryTextColor(self, value: win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementTextColor) -> Void: ...
    @winrt_commethod(20)
    def get_CustomAccessibilityText(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_CustomAccessibilityText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_IsSecondaryTextSubtle(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_IsSecondaryTextSubtle(self, value: Boolean) -> Void: ...
    @winrt_commethod(24)
    def get_ShowBadgeIfUserNotEngaged(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_ShowBadgeIfUserNotEngaged(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(27)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(28)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(29)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    CustomAccessibilityText = property(get_CustomAccessibilityText, put_CustomAccessibilityText)
    DarkModeIconUri = property(get_DarkModeIconUri, put_DarkModeIconUri)
    Duration = property(get_Duration, put_Duration)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Id = property(get_Id, put_Id)
    IsSecondaryTextSubtle = property(get_IsSecondaryTextSubtle, put_IsSecondaryTextSubtle)
    LightModeIconUri = property(get_LightModeIconUri, put_LightModeIconUri)
    PrimaryText = property(get_PrimaryText, put_PrimaryText)
    PrimaryTextColor = property(get_PrimaryTextColor, put_PrimaryTextColor)
    SecondaryText = property(get_SecondaryText, put_SecondaryText)
    SecondaryTextColor = property(get_SecondaryTextColor, put_SecondaryTextColor)
    ShowBadgeIfUserNotEngaged = property(get_ShowBadgeIfUserNotEngaged, put_ShowBadgeIfUserNotEngaged)
class IFeedAnnouncementFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementFactory'
    _iid_ = Guid('{22074243-46d8-5af2-8715-1c76d1cb774c}')
    @winrt_commethod(6)
    def CreateInstance(self, id: WinRT_String, primaryText: WinRT_String, secondaryText: WinRT_String, lightModeIcon: win32more.Windows.Foundation.Uri, darkModeIcon: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncement: ...
class IFeedAnnouncementInvokedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Notifications.IFeedAnnouncementInvokedArgs'
    _iid_ = Guid('{70a48d98-323d-5f19-a1e1-b63fe36edbf2}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AnnouncementId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ActionKind(self) -> win32more.Microsoft.Windows.Widgets.Notifications.AnnouncementActionKind: ...
    ActionKind = property(get_ActionKind, None)
    AnnouncementId = property(get_AnnouncementId, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)


make_ready(__name__)
