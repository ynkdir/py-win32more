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
import win32more.Windows.Phone.System.UserProfile.GameServices.Core
import win32more.Windows.Storage.Streams
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
    _GameService_Meta_.ServiceUri = property(get_ServiceUri.__wrapped__, None)
GameServiceGameOutcome = Int32
GameServiceGameOutcome_None: GameServiceGameOutcome = 0
GameServiceGameOutcome_Win: GameServiceGameOutcome = 1
GameServiceGameOutcome_Loss: GameServiceGameOutcome = 2
GameServiceGameOutcome_Tie: GameServiceGameOutcome = 3
class GameServicePropertyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection'
    @winrt_mixinmethod
    def GetPropertyAsync(self: win32more.Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection, propertyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
GameServiceScoreKind = Int32
GameServiceScoreKind_Number: GameServiceScoreKind = 0
GameServiceScoreKind_Time: GameServiceScoreKind = 1
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
