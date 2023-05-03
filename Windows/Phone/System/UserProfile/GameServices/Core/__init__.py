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
import Windows.Phone.System.UserProfile.GameServices.Core
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GameService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.GameService'
    @winrt_classmethod
    def NotifyPartnerTokenExpired(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService2, audienceUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def GetAuthenticationStatus(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService2) -> UInt32: ...
    @winrt_classmethod
    def get_ServiceUri(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> Windows.Foundation.Uri: ...
    @winrt_classmethod
    def GetGamerProfileAsync(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> Windows.Foundation.IAsyncOperation[Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_classmethod
    def GetInstalledGameItemsAsync(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> Windows.Foundation.IAsyncOperation[Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_classmethod
    def GetPartnerTokenAsync(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService, audienceUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetPrivilegesAsync(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GrantAchievement(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService, achievementId: UInt32) -> Void: ...
    @winrt_classmethod
    def GrantAvatarAward(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService, avatarAwardId: UInt32) -> Void: ...
    @winrt_classmethod
    def PostResult(cls: Windows.Phone.System.UserProfile.GameServices.Core.IGameService, gameVariant: UInt32, scoreKind: Windows.Phone.System.UserProfile.GameServices.Core.GameServiceScoreKind, scoreValue: Int64, gameOutcome: Windows.Phone.System.UserProfile.GameServices.Core.GameServiceGameOutcome, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    ServiceUri = property(get_ServiceUri, None)
GameServiceGameOutcome = Int32
GameServiceGameOutcome_None: GameServiceGameOutcome = 0
GameServiceGameOutcome_Win: GameServiceGameOutcome = 1
GameServiceGameOutcome_Loss: GameServiceGameOutcome = 2
GameServiceGameOutcome_Tie: GameServiceGameOutcome = 3
class GameServicePropertyCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection'
    @winrt_mixinmethod
    def GetPropertyAsync(self: Windows.Phone.System.UserProfile.GameServices.Core.IGameServicePropertyCollection, propertyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
GameServiceScoreKind = Int32
GameServiceScoreKind_Number: GameServiceScoreKind = 0
GameServiceScoreKind_Time: GameServiceScoreKind = 1
class IGameService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2e2d5098-48a9-4efc-af-d6-8e-6d-a0-90-03-fb')
    @winrt_commethod(6)
    def get_ServiceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetGamerProfileAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_commethod(8)
    def GetInstalledGameItemsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Phone.System.UserProfile.GameServices.Core.GameServicePropertyCollection]: ...
    @winrt_commethod(9)
    def GetPartnerTokenAsync(self, audienceUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def GetPrivilegesAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def GrantAchievement(self, achievementId: UInt32) -> Void: ...
    @winrt_commethod(12)
    def GrantAvatarAward(self, avatarAwardId: UInt32) -> Void: ...
    @winrt_commethod(13)
    def PostResult(self, gameVariant: UInt32, scoreKind: Windows.Phone.System.UserProfile.GameServices.Core.GameServiceScoreKind, scoreValue: Int64, gameOutcome: Windows.Phone.System.UserProfile.GameServices.Core.GameServiceGameOutcome, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    ServiceUri = property(get_ServiceUri, None)
class IGameService2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d2364ef6-ea17-4be5-8d-8a-c8-60-88-5e-05-1f')
    @winrt_commethod(6)
    def NotifyPartnerTokenExpired(self, audienceUri: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def GetAuthenticationStatus(self) -> UInt32: ...
class IGameServicePropertyCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('07e57fc8-debb-4609-9c-c8-52-9d-16-bc-2b-d9')
    @winrt_commethod(6)
    def GetPropertyAsync(self, propertyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
make_head(_module, 'GameService')
make_head(_module, 'GameServicePropertyCollection')
make_head(_module, 'IGameService')
make_head(_module, 'IGameService2')
make_head(_module, 'IGameServicePropertyCollection')
