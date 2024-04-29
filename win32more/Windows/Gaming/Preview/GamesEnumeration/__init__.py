from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.Preview.GamesEnumeration
import win32more.Windows.Storage
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class GameList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameList'
    @winrt_classmethod
    def MergeEntriesAsync(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2, left: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry, right: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]: ...
    @winrt_classmethod
    def UnmergeEntryAsync(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2, mergedEntry: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def FindAllAsyncPackageFamilyName(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_classmethod
    def add_GameAdded(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameAdded(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GameRemoved(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListRemovedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameRemoved(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_GameUpdated(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_GameUpdated(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class GameListCategory(Int32):  # enum
    Candidate = 0
    ConfirmedBySystem = 1
    ConfirmedByUser = 2
class GameListChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25f6a421-d8f5-4d91-b40e-53d5e86fde64}')
    def Invoke(self, game: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> Void: ...
class GameListEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameListEntry'
    @winrt_mixinmethod
    def get_DisplayInfo(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def LaunchAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameListCategory: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def SetCategoryAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry, value: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListCategory) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_LaunchableState(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntryLaunchableState: ...
    @winrt_mixinmethod
    def get_LauncherExecutable(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_LaunchParameters(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetLauncherExecutableFileAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, executableFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetLauncherExecutableFileWithParamsAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, executableFile: win32more.Windows.Storage.IStorageFile, launchParams: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TitleId(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetTitleIdAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_GameModeConfiguration(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration: ...
    Category = property(get_Category, None)
    DisplayInfo = property(get_DisplayInfo, None)
    GameModeConfiguration = property(get_GameModeConfiguration, None)
    LaunchParameters = property(get_LaunchParameters, None)
    LaunchableState = property(get_LaunchableState, None)
    LauncherExecutable = property(get_LauncherExecutable, None)
    Properties = property(get_Properties, None)
    TitleId = property(get_TitleId, None)
class GameListEntryLaunchableState(Int32):  # enum
    NotLaunchable = 0
    ByLastRunningFullPath = 1
    ByUserProvidedPath = 2
    ByTile = 3
class GameListRemovedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10c5648f-6c8f-4712-9b38-474bc22e76d8}')
    def Invoke(self, identifier: WinRT_String) -> Void: ...
class GameModeConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RelatedProcessNames(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_PercentGpuTimeAllocatedToGame(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuTimeAllocatedToGame(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_PercentGpuMemoryAllocatedToGame(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuMemoryAllocatedToGame(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_PercentGpuMemoryAllocatedToSystemCompositor(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_PercentGpuMemoryAllocatedToSystemCompositor(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_MaxCpuCount(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_MaxCpuCount(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_CpuExclusivityMaskLow(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_CpuExclusivityMaskLow(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_CpuExclusivityMaskHigh(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_CpuExclusivityMaskHigh(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_AffinitizeToExclusiveCpus(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_AffinitizeToExclusiveCpus(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    AffinitizeToExclusiveCpus = property(get_AffinitizeToExclusiveCpus, put_AffinitizeToExclusiveCpus)
    CpuExclusivityMaskHigh = property(get_CpuExclusivityMaskHigh, put_CpuExclusivityMaskHigh)
    CpuExclusivityMaskLow = property(get_CpuExclusivityMaskLow, put_CpuExclusivityMaskLow)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MaxCpuCount = property(get_MaxCpuCount, put_MaxCpuCount)
    PercentGpuMemoryAllocatedToGame = property(get_PercentGpuMemoryAllocatedToGame, put_PercentGpuMemoryAllocatedToGame)
    PercentGpuMemoryAllocatedToSystemCompositor = property(get_PercentGpuMemoryAllocatedToSystemCompositor, put_PercentGpuMemoryAllocatedToSystemCompositor)
    PercentGpuTimeAllocatedToGame = property(get_PercentGpuTimeAllocatedToGame, put_PercentGpuTimeAllocatedToGame)
    RelatedProcessNames = property(get_RelatedProcessNames, None)
class GameModeUserConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration'
    @winrt_mixinmethod
    def get_GamingRelatedProcessNames(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfigurationStatics) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration: ...
    GamingRelatedProcessNames = property(get_GamingRelatedProcessNames, None)
class IGameListEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListEntry'
    _iid_ = Guid('{735924d3-811f-4494-b69c-c641a0c61543}')
    @winrt_commethod(6)
    def get_DisplayInfo(self) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(7)
    def LaunchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Category(self) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameListCategory: ...
    @winrt_commethod(9)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(10)
    def SetCategoryAsync(self, value: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListCategory) -> win32more.Windows.Foundation.IAsyncAction: ...
    Category = property(get_Category, None)
    DisplayInfo = property(get_DisplayInfo, None)
    Properties = property(get_Properties, None)
class IGameListEntry2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListEntry2'
    _iid_ = Guid('{d84a8f8b-8749-4a25-90d3-f6c5a427886d}')
    @winrt_commethod(6)
    def get_LaunchableState(self) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntryLaunchableState: ...
    @winrt_commethod(7)
    def get_LauncherExecutable(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(8)
    def get_LaunchParameters(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def SetLauncherExecutableFileAsync(self, executableFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def SetLauncherExecutableFileWithParamsAsync(self, executableFile: win32more.Windows.Storage.IStorageFile, launchParams: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_TitleId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def SetTitleIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_GameModeConfiguration(self) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameModeConfiguration: ...
    GameModeConfiguration = property(get_GameModeConfiguration, None)
    LaunchParameters = property(get_LaunchParameters, None)
    LaunchableState = property(get_LaunchableState, None)
    LauncherExecutable = property(get_LauncherExecutable, None)
    TitleId = property(get_TitleId, None)
class IGameListStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListStatics'
    _iid_ = Guid('{2ddd0f6f-9c66-4b05-945c-d6ed78491b8c}')
    @winrt_commethod(6)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_commethod(7)
    def FindAllAsyncPackageFamilyName(self, packageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
    @winrt_commethod(8)
    def add_GameAdded(self, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GameAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GameRemoved(self, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListRemovedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GameRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_GameUpdated(self, handler: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_GameUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IGameListStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameListStatics2'
    _iid_ = Guid('{395f2098-ea1a-45aa-9268-a83905686f27}')
    @winrt_commethod(6)
    def MergeEntriesAsync(self, left: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry, right: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]: ...
    @winrt_commethod(7)
    def UnmergeEntryAsync(self, mergedEntry: win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.Preview.GamesEnumeration.GameListEntry]]: ...
class IGameModeConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeConfiguration'
    _iid_ = Guid('{78e591af-b142-4ef0-8830-55bc2be4f5ea}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_RelatedProcessNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_PercentGpuTimeAllocatedToGame(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(10)
    def put_PercentGpuTimeAllocatedToGame(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(11)
    def get_PercentGpuMemoryAllocatedToGame(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(12)
    def put_PercentGpuMemoryAllocatedToGame(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(13)
    def get_PercentGpuMemoryAllocatedToSystemCompositor(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(14)
    def put_PercentGpuMemoryAllocatedToSystemCompositor(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(15)
    def get_MaxCpuCount(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(16)
    def put_MaxCpuCount(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(17)
    def get_CpuExclusivityMaskLow(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(18)
    def put_CpuExclusivityMaskLow(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(19)
    def get_CpuExclusivityMaskHigh(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(20)
    def put_CpuExclusivityMaskHigh(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(21)
    def get_AffinitizeToExclusiveCpus(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_AffinitizeToExclusiveCpus(self, value: Boolean) -> Void: ...
    @winrt_commethod(23)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AffinitizeToExclusiveCpus = property(get_AffinitizeToExclusiveCpus, put_AffinitizeToExclusiveCpus)
    CpuExclusivityMaskHigh = property(get_CpuExclusivityMaskHigh, put_CpuExclusivityMaskHigh)
    CpuExclusivityMaskLow = property(get_CpuExclusivityMaskLow, put_CpuExclusivityMaskLow)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MaxCpuCount = property(get_MaxCpuCount, put_MaxCpuCount)
    PercentGpuMemoryAllocatedToGame = property(get_PercentGpuMemoryAllocatedToGame, put_PercentGpuMemoryAllocatedToGame)
    PercentGpuMemoryAllocatedToSystemCompositor = property(get_PercentGpuMemoryAllocatedToSystemCompositor, put_PercentGpuMemoryAllocatedToSystemCompositor)
    PercentGpuTimeAllocatedToGame = property(get_PercentGpuTimeAllocatedToGame, put_PercentGpuTimeAllocatedToGame)
    RelatedProcessNames = property(get_RelatedProcessNames, None)
class IGameModeUserConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfiguration'
    _iid_ = Guid('{72d34af4-756b-470f-a0c2-ba62a90795db}')
    @winrt_commethod(6)
    def get_GamingRelatedProcessNames(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    GamingRelatedProcessNames = property(get_GamingRelatedProcessNames, None)
class IGameModeUserConfigurationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Preview.GamesEnumeration.IGameModeUserConfigurationStatics'
    _iid_ = Guid('{6e50d97c-66ea-478e-a4a1-f57c0e8d00e7}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Gaming.Preview.GamesEnumeration.GameModeUserConfiguration: ...


make_ready(__name__)
