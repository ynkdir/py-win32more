from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Phone.System.UserProfile.GameServices.Core
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class _GameService_Meta_(ComPtr.__class__):
    pass
class GameService(ComPtr, metaclass=_GameService_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.GameService'
    @winrt_classmethod
    def NotifyPartnerTokenExpired(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService2, audienceUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def GetAuthenticationStatus(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService2) -> UInt32: ...
    @winrt_classmethod
    def get_ServiceUri(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def GetGamerProfileAsync(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_classmethod
    def GetInstalledGameItemsAsync(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_classmethod
    def GetPartnerTokenAsync(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService, audienceUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetPrivilegesAsync(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GrantAchievement(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService, achievementId: UInt32) -> Void: ...
    @winrt_classmethod
    def GrantAvatarAward(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService, avatarAwardId: UInt32) -> Void: ...
    @winrt_classmethod
    def PostResult(cls: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameService, gameVariant: UInt32, scoreKind: win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServiceScoreKind, scoreValue: Int64, gameOutcome: win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServiceGameOutcome, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    _GameService_Meta_.ServiceUri = property(get_ServiceUri, None)
class GameServiceGameOutcome(Enum, Int32):
    None_ = 0
    Win = 1
    Loss = 2
    Tie = 3
class GameServicePropertyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection'
    @winrt_mixinmethod
    def GetPropertyAsync(self: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection, propertyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
class GameServiceScoreKind(Enum, Int32):
    Number = 0
    Time = 1
class IGameService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.IGameService'
    _iid_ = Guid('{2e2d5098-48a9-4efc-afd6-8e6da09003fb}')
    @winrt_commethod(6)
    def get_ServiceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetGamerProfileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_commethod(8)
    def GetInstalledGameItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_commethod(9)
    def GetPartnerTokenAsync(self, audienceUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def GetPrivilegesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def GrantAchievement(self, achievementId: UInt32) -> Void: ...
    @winrt_commethod(12)
    def GrantAvatarAward(self, avatarAwardId: UInt32) -> Void: ...
    @winrt_commethod(13)
    def PostResult(self, gameVariant: UInt32, scoreKind: win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServiceScoreKind, scoreValue: Int64, gameOutcome: win32more.Windows.Phone.System.UserProfile.GameServices.Core.GameServiceGameOutcome, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    ServiceUri = property(get_ServiceUri, None)
class IGameService2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.IGameService2'
    _iid_ = Guid('{d2364ef6-ea17-4be5-8d8a-c860885e051f}')
    @winrt_commethod(6)
    def NotifyPartnerTokenExpired(self, audienceUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def GetAuthenticationStatus(self) -> UInt32: ...
class IGameServicePropertyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection'
    _iid_ = Guid('{07e57fc8-debb-4609-9cc8-529d16bc2bd9}')
    @winrt_commethod(6)
    def GetPropertyAsync(self, propertyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...


make_ready(__name__)
