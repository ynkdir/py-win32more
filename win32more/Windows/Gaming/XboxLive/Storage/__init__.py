from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
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
import win32more.Windows.Gaming.XboxLive.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GameSaveBlobGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveBlobInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo) -> UInt32: ...
    Name = property(get_Name, None)
    Size = property(get_Size, None)
class GameSaveBlobInfoGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveBlobInfoQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery'
    @winrt_mixinmethod
    def GetBlobInfoAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_mixinmethod
    def GetBlobInfoWithIndexAndMaxAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
class GameSaveContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainer'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    @winrt_mixinmethod
    def SubmitUpdatesAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToWrite: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer], blobsToDelete: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToRead: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def GetAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToRead: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult]: ...
    @winrt_mixinmethod
    def SubmitPropertySetUpdatesAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToWrite: win32more.Windows.Foundation.Collections.IPropertySet, blobsToDelete: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def CreateBlobInfoQuery(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobNamePrefix: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery: ...
    Name = property(get_Name, None)
    Provider = property(get_Provider, None)
class GameSaveContainerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TotalSize(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastModifiedTime(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NeedsSync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> Boolean: ...
    Name = property(get_Name, None)
    TotalSize = property(get_TotalSize, None)
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    NeedsSync = property(get_NeedsSync, None)
class GameSaveContainerInfoGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveContainerInfoQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery'
    @winrt_mixinmethod
    def GetContainerInfoAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_mixinmethod
    def GetContainerInfoWithIndexAndMaxAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
GameSaveErrorStatus = Int32
GameSaveErrorStatus_Ok: GameSaveErrorStatus = 0
GameSaveErrorStatus_Abort: GameSaveErrorStatus = -2147467260
GameSaveErrorStatus_InvalidContainerName: GameSaveErrorStatus = -2138898431
GameSaveErrorStatus_NoAccess: GameSaveErrorStatus = -2138898430
GameSaveErrorStatus_OutOfLocalStorage: GameSaveErrorStatus = -2138898429
GameSaveErrorStatus_UserCanceled: GameSaveErrorStatus = -2138898428
GameSaveErrorStatus_UpdateTooBig: GameSaveErrorStatus = -2138898427
GameSaveErrorStatus_QuotaExceeded: GameSaveErrorStatus = -2138898426
GameSaveErrorStatus_ProvidedBufferTooSmall: GameSaveErrorStatus = -2138898425
GameSaveErrorStatus_BlobNotFound: GameSaveErrorStatus = -2138898424
GameSaveErrorStatus_NoXboxLiveInfo: GameSaveErrorStatus = -2138898423
GameSaveErrorStatus_ContainerNotInSync: GameSaveErrorStatus = -2138898422
GameSaveErrorStatus_ContainerSyncFailed: GameSaveErrorStatus = -2138898421
GameSaveErrorStatus_UserHasNoXboxLiveInfo: GameSaveErrorStatus = -2138898420
GameSaveErrorStatus_ObjectExpired: GameSaveErrorStatus = -2138898419
class GameSaveOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveOperationResult
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveOperationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveOperationResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    Status = property(get_Status, None)
class GameSaveProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveProvider'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def CreateContainer(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider, name: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainer: ...
    @winrt_mixinmethod
    def DeleteContainerAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def CreateContainerInfoQuery(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_mixinmethod
    def CreateContainerInfoQueryWithName(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider, containerNamePrefix: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_mixinmethod
    def GetRemainingBytesInQuotaAsync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> win32more.Windows.Foundation.IAsyncOperation[Int64]: ...
    @winrt_mixinmethod
    def get_ContainersChangedSinceLastSync(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def GetForUserAsync(cls: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProviderStatics, user: win32more.Windows.System.User, serviceConfigId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    @winrt_classmethod
    def GetSyncOnDemandForUserAsync(cls: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProviderStatics, user: win32more.Windows.System.User, serviceConfigId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    User = property(get_User, None)
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
class GameSaveProviderGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult'
    _iid_ = Guid('{917281e0-7201-4953-aa2c-4008f03aef45}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo'
    _iid_ = Guid('{add38034-baf0-4645-b6d0-46edaffb3c2b}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    Name = property(get_Name, None)
    Size = property(get_Size, None)
class IGameSaveBlobInfoGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult'
    _iid_ = Guid('{c7578582-3697-42bf-989c-665d923b5231}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobInfoQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery'
    _iid_ = Guid('{9fdd74b2-eeee-447b-a9d2-7f96c0f83208}')
    @winrt_commethod(6)
    def GetBlobInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_commethod(7)
    def GetBlobInfoWithIndexAndMaxAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_commethod(8)
    def GetItemCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
class IGameSaveContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveContainer'
    _iid_ = Guid('{c3c08f89-563f-4ecd-9c6f-33fd0e323d10}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Provider(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    @winrt_commethod(8)
    def SubmitUpdatesAsync(self, blobsToWrite: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer], blobsToDelete: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(9)
    def ReadAsync(self, blobsToRead: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.IBuffer]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(10)
    def GetAsync(self, blobsToRead: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult]: ...
    @winrt_commethod(11)
    def SubmitPropertySetUpdatesAsync(self, blobsToWrite: win32more.Windows.Foundation.Collections.IPropertySet, blobsToDelete: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(12)
    def CreateBlobInfoQuery(self, blobNamePrefix: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery: ...
    Name = property(get_Name, None)
    Provider = property(get_Provider, None)
class IGameSaveContainerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo'
    _iid_ = Guid('{b7e27300-155d-4bb4-b2ba-930306f391b5}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TotalSize(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_LastModifiedTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_NeedsSync(self) -> Boolean: ...
    Name = property(get_Name, None)
    TotalSize = property(get_TotalSize, None)
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    NeedsSync = property(get_NeedsSync, None)
class IGameSaveContainerInfoGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult'
    _iid_ = Guid('{ffc50d74-c581-4f9d-9e39-30a10c1e4c50}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveContainerInfoQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery'
    _iid_ = Guid('{3c94e863-6f80-4327-9327-ffc11afd42b3}')
    @winrt_commethod(6)
    def GetContainerInfoAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_commethod(7)
    def GetContainerInfoWithIndexAndMaxAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_commethod(8)
    def GetItemCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
class IGameSaveOperationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveOperationResult'
    _iid_ = Guid('{cf0f1a05-24a0-4582-9a55-b1bbbb9388d8}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    Status = property(get_Status, None)
class IGameSaveProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveProvider'
    _iid_ = Guid('{90a60394-80fe-4211-97f8-a5de14dd95d2}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def CreateContainer(self, name: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainer: ...
    @winrt_commethod(8)
    def DeleteContainerAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(9)
    def CreateContainerInfoQuery(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_commethod(10)
    def CreateContainerInfoQueryWithName(self, containerNamePrefix: WinRT_String) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_commethod(11)
    def GetRemainingBytesInQuotaAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Int64]: ...
    @winrt_commethod(12)
    def get_ContainersChangedSinceLastSync(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    User = property(get_User, None)
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
class IGameSaveProviderGetResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult'
    _iid_ = Guid('{3ab90816-d393-4d65-ac16-41c3e67ab945}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.IGameSaveProviderStatics'
    _iid_ = Guid('{d01d3ed0-7b03-449d-8cbd-3402842a1048}')
    @winrt_commethod(6)
    def GetForUserAsync(self, user: win32more.Windows.System.User, serviceConfigId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    @winrt_commethod(7)
    def GetSyncOnDemandForUserAsync(self, user: win32more.Windows.System.User, serviceConfigId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
make_head(_module, 'GameSaveBlobGetResult')
make_head(_module, 'GameSaveBlobInfo')
make_head(_module, 'GameSaveBlobInfoGetResult')
make_head(_module, 'GameSaveBlobInfoQuery')
make_head(_module, 'GameSaveContainer')
make_head(_module, 'GameSaveContainerInfo')
make_head(_module, 'GameSaveContainerInfoGetResult')
make_head(_module, 'GameSaveContainerInfoQuery')
make_head(_module, 'GameSaveOperationResult')
make_head(_module, 'GameSaveProvider')
make_head(_module, 'GameSaveProviderGetResult')
make_head(_module, 'IGameSaveBlobGetResult')
make_head(_module, 'IGameSaveBlobInfo')
make_head(_module, 'IGameSaveBlobInfoGetResult')
make_head(_module, 'IGameSaveBlobInfoQuery')
make_head(_module, 'IGameSaveContainer')
make_head(_module, 'IGameSaveContainerInfo')
make_head(_module, 'IGameSaveContainerInfoGetResult')
make_head(_module, 'IGameSaveContainerInfoQuery')
make_head(_module, 'IGameSaveOperationResult')
make_head(_module, 'IGameSaveProvider')
make_head(_module, 'IGameSaveProviderGetResult')
make_head(_module, 'IGameSaveProviderStatics')
