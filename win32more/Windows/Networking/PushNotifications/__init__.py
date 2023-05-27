from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.PushNotifications
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI.Notifications
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannel'
    _iid_ = Guid('{2b28102e-ef0b-4f39-9b8a-a3c194de7081}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def Close(self) -> Void: ...
    @winrt_commethod(9)
    def add_PushNotificationReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.PushNotifications.PushNotificationChannel, win32more.Windows.Networking.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PushNotificationReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Uri = property(get_Uri, None)
    ExpirationTime = property(get_ExpirationTime, None)
class IPushNotificationChannelManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser'
    _iid_ = Guid('{a4c45704-1182-42c7-8890-f563c4890dc4}')
    @winrt_commethod(6)
    def CreatePushNotificationChannelForApplicationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(7)
    def CreatePushNotificationChannelForApplicationAsyncWithId(self, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(8)
    def CreatePushNotificationChannelForSecondaryTileAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(9)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IPushNotificationChannelManagerForUser2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser2'
    _iid_ = Guid('{c38b066a-7cc1-4dac-87fd-be6e920414a4}')
    @winrt_commethod(6)
    def CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync(self, appServerKey: win32more.Windows.Storage.Streams.IBuffer, channelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(7)
    def CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsyncWithId(self, appServerKey: win32more.Windows.Storage.Streams.IBuffer, channelId: WinRT_String, appId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
class IPushNotificationChannelManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics'
    _iid_ = Guid('{8baf9b65-77a1-4588-bd19-861529a9dcf0}')
    @winrt_commethod(6)
    def CreatePushNotificationChannelForApplicationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(7)
    def CreatePushNotificationChannelForApplicationAsyncWithId(self, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_commethod(8)
    def CreatePushNotificationChannelForSecondaryTileAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
class IPushNotificationChannelManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics2'
    _iid_ = Guid('{b444a65d-a7e9-4b28-950e-f375a907f9df}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Networking.PushNotifications.PushNotificationChannelManagerForUser: ...
class IPushNotificationChannelManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics3'
    _iid_ = Guid('{4701fefe-0ede-4a3f-ae78-bfa471496925}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Networking.PushNotifications.PushNotificationChannelManagerForUser: ...
class IPushNotificationChannelManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics4'
    _iid_ = Guid('{bc540efb-7820-5a5b-9c01-b4757f774025}')
    @winrt_commethod(6)
    def add_ChannelsRevoked(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Networking.PushNotifications.PushNotificationChannelsRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ChannelsRevoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPushNotificationChannelsRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationChannelsRevokedEventArgs'
    _iid_ = Guid('{20e1a24c-1a34-5beb-aae2-40c232c8c140}')
class IPushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs'
    _iid_ = Guid('{d1065e0c-36cd-484c-b935-0a99b753cf00}')
    @winrt_commethod(6)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_NotificationType(self) -> win32more.Windows.Networking.PushNotifications.PushNotificationType: ...
    @winrt_commethod(9)
    def get_ToastNotification(self) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(10)
    def get_TileNotification(self) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(11)
    def get_BadgeNotification(self) -> win32more.Windows.UI.Notifications.BadgeNotification: ...
    @winrt_commethod(12)
    def get_RawNotification(self) -> win32more.Windows.Networking.PushNotifications.RawNotification: ...
    Cancel = property(get_Cancel, put_Cancel)
    NotificationType = property(get_NotificationType, None)
    ToastNotification = property(get_ToastNotification, None)
    TileNotification = property(get_TileNotification, None)
    BadgeNotification = property(get_BadgeNotification, None)
    RawNotification = property(get_RawNotification, None)
class IRawNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IRawNotification'
    _iid_ = Guid('{1a227281-3b79-42ac-9963-22ab00d4f0b7}')
    @winrt_commethod(6)
    def get_Content(self) -> WinRT_String: ...
    Content = property(get_Content, None)
class IRawNotification2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IRawNotification2'
    _iid_ = Guid('{e6d0cf19-0c6f-4cdd-9424-eec5be014d26}')
    @winrt_commethod(6)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def get_ChannelId(self) -> WinRT_String: ...
    Headers = property(get_Headers, None)
    ChannelId = property(get_ChannelId, None)
class IRawNotification3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.IRawNotification3'
    _iid_ = Guid('{62737dde-8a73-424c-ab44-5635f40a96e5}')
    @winrt_commethod(6)
    def get_ContentBytes(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ContentBytes = property(get_ContentBytes, None)
class PushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel
    _classid_ = 'Windows.Networking.PushNotifications.PushNotificationChannel'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel) -> Void: ...
    @winrt_mixinmethod
    def add_PushNotificationReceived(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.PushNotifications.PushNotificationChannel, win32more.Windows.Networking.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PushNotificationReceived(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Uri = property(get_Uri, None)
    ExpirationTime = property(get_ExpirationTime, None)
class PushNotificationChannelManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.PushNotifications.PushNotificationChannelManager'
    @winrt_classmethod
    def add_ChannelsRevoked(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics4, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Networking.PushNotifications.PushNotificationChannelsRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ChannelsRevoked(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics3) -> win32more.Windows.Networking.PushNotifications.PushNotificationChannelManagerForUser: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.Networking.PushNotifications.PushNotificationChannelManagerForUser: ...
    @winrt_classmethod
    def CreatePushNotificationChannelForApplicationAsync(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_classmethod
    def CreatePushNotificationChannelForApplicationAsyncWithId(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_classmethod
    def CreatePushNotificationChannelForSecondaryTileAsync(cls: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerStatics, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
class PushNotificationChannelManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser
    _classid_ = 'Windows.Networking.PushNotifications.PushNotificationChannelManagerForUser'
    @winrt_mixinmethod
    def CreatePushNotificationChannelForApplicationAsync(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_mixinmethod
    def CreatePushNotificationChannelForApplicationAsyncWithId(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser, applicationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_mixinmethod
    def CreatePushNotificationChannelForSecondaryTileAsync(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser2, appServerKey: win32more.Windows.Storage.Streams.IBuffer, channelId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    @winrt_mixinmethod
    def CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsyncWithId(self: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelManagerForUser2, appServerKey: win32more.Windows.Storage.Streams.IBuffer, channelId: WinRT_String, appId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.PushNotifications.PushNotificationChannel]: ...
    User = property(get_User, None)
class PushNotificationChannelsRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.PushNotifications.IPushNotificationChannelsRevokedEventArgs
    _classid_ = 'Windows.Networking.PushNotifications.PushNotificationChannelsRevokedEventArgs'
class PushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs
    _classid_ = 'Windows.Networking.PushNotifications.PushNotificationReceivedEventArgs'
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotificationType(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.Networking.PushNotifications.PushNotificationType: ...
    @winrt_mixinmethod
    def get_ToastNotification(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def get_TileNotification(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def get_BadgeNotification(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.UI.Notifications.BadgeNotification: ...
    @winrt_mixinmethod
    def get_RawNotification(self: win32more.Windows.Networking.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.Networking.PushNotifications.RawNotification: ...
    Cancel = property(get_Cancel, put_Cancel)
    NotificationType = property(get_NotificationType, None)
    ToastNotification = property(get_ToastNotification, None)
    TileNotification = property(get_TileNotification, None)
    BadgeNotification = property(get_BadgeNotification, None)
    RawNotification = property(get_RawNotification, None)
PushNotificationType = Int32
PushNotificationType_Toast: PushNotificationType = 0
PushNotificationType_Tile: PushNotificationType = 1
PushNotificationType_Badge: PushNotificationType = 2
PushNotificationType_Raw: PushNotificationType = 3
PushNotificationType_TileFlyout: PushNotificationType = 4
class RawNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.PushNotifications.IRawNotification
    _classid_ = 'Windows.Networking.PushNotifications.RawNotification'
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Networking.PushNotifications.IRawNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Networking.PushNotifications.IRawNotification2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_ChannelId(self: win32more.Windows.Networking.PushNotifications.IRawNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentBytes(self: win32more.Windows.Networking.PushNotifications.IRawNotification3) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Content = property(get_Content, None)
    Headers = property(get_Headers, None)
    ChannelId = property(get_ChannelId, None)
    ContentBytes = property(get_ContentBytes, None)
make_head(_module, 'IPushNotificationChannel')
make_head(_module, 'IPushNotificationChannelManagerForUser')
make_head(_module, 'IPushNotificationChannelManagerForUser2')
make_head(_module, 'IPushNotificationChannelManagerStatics')
make_head(_module, 'IPushNotificationChannelManagerStatics2')
make_head(_module, 'IPushNotificationChannelManagerStatics3')
make_head(_module, 'IPushNotificationChannelManagerStatics4')
make_head(_module, 'IPushNotificationChannelsRevokedEventArgs')
make_head(_module, 'IPushNotificationReceivedEventArgs')
make_head(_module, 'IRawNotification')
make_head(_module, 'IRawNotification2')
make_head(_module, 'IRawNotification3')
make_head(_module, 'PushNotificationChannel')
make_head(_module, 'PushNotificationChannelManager')
make_head(_module, 'PushNotificationChannelManagerForUser')
make_head(_module, 'PushNotificationChannelsRevokedEventArgs')
make_head(_module, 'PushNotificationReceivedEventArgs')
make_head(_module, 'RawNotification')
