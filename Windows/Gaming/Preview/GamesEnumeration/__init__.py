from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Gaming.Preview.GamesEnumeration
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GameList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameList'
    @winrt_classmethod
    def MergeEntriesAsync(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2, left: Windows.Gaming.Preview.GamesEnumeration.GameListEntry, right: Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]: ...
    @winrt_classmethod
    def UnmergeEntryAsync(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2, mergedEntry: Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def FindAllAsyncPackageFamilyName(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def add_GameAdded(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameAdded(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GameRemoved(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: Windows.Gaming.Preview.GamesEnumeration.GameListRemovedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameRemoved(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GameUpdated(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameUpdated(cls: Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
GameListCategory = Int32
GameListCategory_Candidate: GameListCategory = 0
GameListCategory_ConfirmedBySystem: GameListCategory = 1
GameListCategory_ConfirmedByUser: GameListCategory = 2
class GameListChangedEventHandler(MulticastDelegate):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25f6a421-d8f5-4d91-b40e-53d5e86fde64}')
    def Invoke(self, game: Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Void: ...
class GameListEntry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameListEntry'
    @winrt_mixinmethod
    def get_DisplayInfo(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def LaunchAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> Windows.Gaming.Preview.GamesEnumeration.GameListCategory: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def SetCategoryAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry, value: Windows.Gaming.Preview.GamesEnumeration.GameListCategory) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_LaunchableState(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> Windows.Gaming.Preview.GamesEnumeration.GameListEntryLaunchableState: ...
    @winrt_mixinmethod
    def get_LauncherExecutable(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_LaunchParameters(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetLauncherExecutableFileAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, executableFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetLauncherExecutableFileWithParamsAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, executableFile: Windows.Storage.IStorageFile, launchParams: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TitleId(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetTitleIdAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_GameModeConfiguration(self: Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration: ...
    DisplayInfo = property(get_DisplayInfo, None)
    Category = property(get_Category, None)
    Properties = property(get_Properties, None)
    LaunchableState = property(get_LaunchableState, None)
    LauncherExecutable = property(get_LauncherExecutable, None)
    LaunchParameters = property(get_LaunchParameters, None)
    TitleId = property(get_TitleId, None)
    GameModeConfiguration = property(get_GameModeConfiguration, None)
GameListEntryLaunchableState = Int32
GameListEntryLaunchableState_NotLaunchable: GameListEntryLaunchableState = 0
GameListEntryLaunchableState_ByLastRunningFullPath: GameListEntryLaunchableState = 1
GameListEntryLaunchableState_ByUserProvidedPath: GameListEntryLaunchableState = 2
GameListEntryLaunchableState_ByTile: GameListEntryLaunchableState = 3
class GameListRemovedEventHandler(MulticastDelegate):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10c5648f-6c8f-4712-9b38-474bc22e76d8}')
    def Invoke(self, identifier: WinRT_String) -> Void: ...
class GameModeConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RelatedProcessNames(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PercentGpuTimeAllocatedToGame(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuTimeAllocatedToGame(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_PercentGpuMemoryAllocatedToGame(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuMemoryAllocatedToGame(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_PercentGpuMemoryAllocatedToSystemCompositor(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuMemoryAllocatedToSystemCompositor(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxCpuCount(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxCpuCount(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_CpuExclusivityMaskLow(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_CpuExclusivityMaskLow(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_CpuExclusivityMaskHigh(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_CpuExclusivityMaskHigh(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_AffinitizeToExclusiveCpus(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_AffinitizeToExclusiveCpus(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Windows.Foundation.IAsyncAction: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    RelatedProcessNames = property(get_RelatedProcessNames, None)
    PercentGpuTimeAllocatedToGame = property(get_PercentGpuTimeAllocatedToGame, put_PercentGpuTimeAllocatedToGame)
    PercentGpuMemoryAllocatedToGame = property(get_PercentGpuMemoryAllocatedToGame, put_PercentGpuMemoryAllocatedToGame)
    PercentGpuMemoryAllocatedToSystemCompositor = property(get_PercentGpuMemoryAllocatedToSystemCompositor, put_PercentGpuMemoryAllocatedToSystemCompositor)
    MaxCpuCount = property(get_MaxCpuCount, put_MaxCpuCount)
    CpuExclusivityMaskLow = property(get_CpuExclusivityMaskLow, put_CpuExclusivityMaskLow)
    CpuExclusivityMaskHigh = property(get_CpuExclusivityMaskHigh, put_CpuExclusivityMaskHigh)
    AffinitizeToExclusiveCpus = property(get_AffinitizeToExclusiveCpus, put_AffinitizeToExclusiveCpus)
class GameModeUserConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration'
    @winrt_mixinmethod
    def get_GamingRelatedProcessNames(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfigurationStatics) -> Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration: ...
    GamingRelatedProcessNames = property(get_GamingRelatedProcessNames, None)
class IGameListEntry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListEntry'
    _iid_ = Guid('{735924d3-811f-4494-b69c-c641a0c61543}')
    @winrt_commethod(6)
    def get_DisplayInfo(self) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(7)
    def LaunchAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Category(self) -> Windows.Gaming.Preview.GamesEnumeration.GameListCategory: ...
    @winrt_commethod(9)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(10)
    def SetCategoryAsync(self, value: Windows.Gaming.Preview.GamesEnumeration.GameListCategory) -> Windows.Foundation.IAsyncAction: ...
    DisplayInfo = property(get_DisplayInfo, None)
    Category = property(get_Category, None)
    Properties = property(get_Properties, None)
class IGameListEntry2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2'
    _iid_ = Guid('{d84a8f8b-8749-4a25-90d3-f6c5a427886d}')
    @winrt_commethod(6)
    def get_LaunchableState(self) -> Windows.Gaming.Preview.GamesEnumeration.GameListEntryLaunchableState: ...
    @winrt_commethod(7)
    def get_LauncherExecutable(self) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(8)
    def get_LaunchParameters(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def SetLauncherExecutableFileAsync(self, executableFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SetLauncherExecutableFileWithParamsAsync(self, executableFile: Windows.Storage.IStorageFile, launchParams: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_TitleId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def SetTitleIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_GameModeConfiguration(self) -> Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration: ...
    LaunchableState = property(get_LaunchableState, None)
    LauncherExecutable = property(get_LauncherExecutable, None)
    LaunchParameters = property(get_LaunchParameters, None)
    TitleId = property(get_TitleId, None)
    GameModeConfiguration = property(get_GameModeConfiguration, None)
class IGameListStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListStatics'
    _iid_ = Guid('{2ddd0f6f-9c66-4b05-945c-d6ed78491b8c}')
    @winrt_commethod(6)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_commethod(7)
    def FindAllAsyncPackageFamilyName(self, packageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_commethod(8)
    def add_GameAdded(self, handler: Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GameAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GameRemoved(self, handler: Windows.Gaming.Preview.GamesEnumeration.GameListRemovedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GameRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_GameUpdated(self, handler: Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_GameUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IGameListStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2'
    _iid_ = Guid('{395f2098-ea1a-45aa-9268-a83905686f27}')
    @winrt_commethod(6)
    def MergeEntriesAsync(self, left: Windows.Gaming.Preview.GamesEnumeration.GameListEntry, right: Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]: ...
    @winrt_commethod(7)
    def UnmergeEntryAsync(self, mergedEntry: Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
class IGameModeConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration'
    _iid_ = Guid('{78e591af-b142-4ef0-8830-55bc2be4f5ea}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_RelatedProcessNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_PercentGpuTimeAllocatedToGame(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def put_PercentGpuTimeAllocatedToGame(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(11)
    def get_PercentGpuMemoryAllocatedToGame(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(12)
    def put_PercentGpuMemoryAllocatedToGame(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(13)
    def get_PercentGpuMemoryAllocatedToSystemCompositor(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(14)
    def put_PercentGpuMemoryAllocatedToSystemCompositor(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(15)
    def get_MaxCpuCount(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(16)
    def put_MaxCpuCount(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(17)
    def get_CpuExclusivityMaskLow(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(18)
    def put_CpuExclusivityMaskLow(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(19)
    def get_CpuExclusivityMaskHigh(self) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(20)
    def put_CpuExclusivityMaskHigh(self, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(21)
    def get_AffinitizeToExclusiveCpus(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_AffinitizeToExclusiveCpus(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    RelatedProcessNames = property(get_RelatedProcessNames, None)
    PercentGpuTimeAllocatedToGame = property(get_PercentGpuTimeAllocatedToGame, put_PercentGpuTimeAllocatedToGame)
    PercentGpuMemoryAllocatedToGame = property(get_PercentGpuMemoryAllocatedToGame, put_PercentGpuMemoryAllocatedToGame)
    PercentGpuMemoryAllocatedToSystemCompositor = property(get_PercentGpuMemoryAllocatedToSystemCompositor, put_PercentGpuMemoryAllocatedToSystemCompositor)
    MaxCpuCount = property(get_MaxCpuCount, put_MaxCpuCount)
    CpuExclusivityMaskLow = property(get_CpuExclusivityMaskLow, put_CpuExclusivityMaskLow)
    CpuExclusivityMaskHigh = property(get_CpuExclusivityMaskHigh, put_CpuExclusivityMaskHigh)
    AffinitizeToExclusiveCpus = property(get_AffinitizeToExclusiveCpus, put_AffinitizeToExclusiveCpus)
class IGameModeUserConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration'
    _iid_ = Guid('{72d34af4-756b-470f-a0c2-ba62a90795db}')
    @winrt_commethod(6)
    def get_GamingRelatedProcessNames(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    GamingRelatedProcessNames = property(get_GamingRelatedProcessNames, None)
class IGameModeUserConfigurationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfigurationStatics'
    _iid_ = Guid('{6e50d97c-66ea-478e-a4a1-f57c0e8d00e7}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration: ...
make_head(_module, 'GameList')
make_head(_module, 'GameListEntry')
make_head(_module, 'GameModeConfiguration')
make_head(_module, 'GameModeUserConfiguration')
make_head(_module, 'IGameListEntry')
make_head(_module, 'IGameListEntry2')
make_head(_module, 'IGameListStatics')
make_head(_module, 'IGameListStatics2')
make_head(_module, 'IGameModeConfiguration')
make_head(_module, 'IGameModeUserConfiguration')
make_head(_module, 'IGameModeUserConfigurationStatics')
