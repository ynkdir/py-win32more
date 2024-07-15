from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.XboxLive.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
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
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    Name = property(get_Name, None)
    NeedsSync = property(get_NeedsSync, None)
    TotalSize = property(get_TotalSize, None)
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
class GameSaveErrorStatus(Enum, Int32):
    Ok = 0
    Abort = -2147467260
    InvalidContainerName = -2138898431
    NoAccess = -2138898430
    OutOfLocalStorage = -2138898429
    UserCanceled = -2138898428
    UpdateTooBig = -2138898427
    QuotaExceeded = -2138898426
    ProvidedBufferTooSmall = -2138898425
    BlobNotFound = -2138898424
    NoXboxLiveInfo = -2138898423
    ContainerNotInSync = -2138898422
    ContainerSyncFailed = -2138898421
    UserHasNoXboxLiveInfo = -2138898420
    ObjectExpired = -2138898419
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
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
    User = property(get_User, None)
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
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    Name = property(get_Name, None)
    NeedsSync = property(get_NeedsSync, None)
    TotalSize = property(get_TotalSize, None)
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
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
    User = property(get_User, None)
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


make_ready(__name__)
