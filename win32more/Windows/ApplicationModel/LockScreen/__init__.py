from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.LockScreen
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ILockApplicationHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockApplicationHost'
    _iid_ = Guid('{38ee31ad-d94f-4e7c-81fa-4f4436506281}')
    @winrt_commethod(6)
    def RequestUnlock(self) -> Void: ...
    @winrt_commethod(7)
    def add_Unlocking(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockApplicationHost, win32more.Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Unlocking(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Unlocking = event()
class ILockApplicationHostStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockApplicationHostStatics'
    _iid_ = Guid('{f48fab8e-23d7-4e63-96a1-666ff52d3b2c}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.LockScreen.LockApplicationHost: ...
class ILockScreenBadge(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockScreenBadge'
    _iid_ = Guid('{e95105d9-2bff-4db0-9b4f-3824778b9c9a}')
    @winrt_commethod(6)
    def get_Logo(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(7)
    def get_Glyph(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def get_Number(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_AutomationName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def LaunchApp(self) -> Void: ...
    AutomationName = property(get_AutomationName, None)
    Glyph = property(get_Glyph, None)
    Logo = property(get_Logo, None)
    Number = property(get_Number, None)
class ILockScreenInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockScreenInfo'
    _iid_ = Guid('{f59aa65c-9711-4dc9-a630-95b6cb8cdad0}')
    @winrt_commethod(6)
    def add_LockScreenImageChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LockScreenImageChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_LockScreenImage(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(9)
    def add_BadgesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_BadgesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_Badges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.LockScreen.LockScreenBadge]: ...
    @winrt_commethod(12)
    def add_DetailTextChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DetailTextChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_DetailText(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(15)
    def add_AlarmIconChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AlarmIconChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def get_AlarmIcon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    AlarmIcon = property(get_AlarmIcon, None)
    Badges = property(get_Badges, None)
    DetailText = property(get_DetailText, None)
    LockScreenImage = property(get_LockScreenImage, None)
    LockScreenImageChanged = event()
    BadgesChanged = event()
    DetailTextChanged = event()
    AlarmIconChanged = event()
class ILockScreenUnlockingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockScreenUnlockingDeferral'
    _iid_ = Guid('{7e7d1ad6-5203-43e7-9bd6-7c3947d1e3fe}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ILockScreenUnlockingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs'
    _iid_ = Guid('{44e6c007-75fb-4abb-9f8b-824748900c71}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class LockApplicationHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.LockScreen.ILockApplicationHost
    _classid_ = 'Windows.ApplicationModel.LockScreen.LockApplicationHost'
    @winrt_mixinmethod
    def RequestUnlock(self: win32more.Windows.ApplicationModel.LockScreen.ILockApplicationHost) -> Void: ...
    @winrt_mixinmethod
    def add_Unlocking(self: win32more.Windows.ApplicationModel.LockScreen.ILockApplicationHost, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockApplicationHost, win32more.Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Unlocking(self: win32more.Windows.ApplicationModel.LockScreen.ILockApplicationHost, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.LockScreen.ILockApplicationHostStatics) -> win32more.Windows.ApplicationModel.LockScreen.LockApplicationHost: ...
    Unlocking = event()
class LockScreenBadge(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge
    _classid_ = 'Windows.ApplicationModel.LockScreen.LockScreenBadge'
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_Glyph(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_Number(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_AutomationName(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> WinRT_String: ...
    @winrt_mixinmethod
    def LaunchApp(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenBadge) -> Void: ...
    AutomationName = property(get_AutomationName, None)
    Glyph = property(get_Glyph, None)
    Logo = property(get_Logo, None)
    Number = property(get_Number, None)
class LockScreenInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo
    _classid_ = 'Windows.ApplicationModel.LockScreen.LockScreenInfo'
    @winrt_mixinmethod
    def add_LockScreenImageChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LockScreenImageChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_LockScreenImage(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def add_BadgesChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BadgesChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Badges(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.LockScreen.LockScreenBadge]: ...
    @winrt_mixinmethod
    def add_DetailTextChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DetailTextChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DetailText(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def add_AlarmIconChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.LockScreen.LockScreenInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AlarmIconChanged(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AlarmIcon(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenInfo) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    AlarmIcon = property(get_AlarmIcon, None)
    Badges = property(get_Badges, None)
    DetailText = property(get_DetailText, None)
    LockScreenImage = property(get_LockScreenImage, None)
    LockScreenImageChanged = event()
    BadgesChanged = event()
    DetailTextChanged = event()
    AlarmIconChanged = event()
class LockScreenUnlockingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.LockScreen.ILockScreenUnlockingDeferral
    _classid_ = 'Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenUnlockingDeferral) -> Void: ...
class LockScreenUnlockingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs
    _classid_ = 'Windows.ApplicationModel.LockScreen.LockScreenUnlockingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs) -> win32more.Windows.ApplicationModel.LockScreen.LockScreenUnlockingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.LockScreen.ILockScreenUnlockingEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)


make_ready(__name__)
