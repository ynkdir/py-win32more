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
import Windows.Foundation.Collections
import Windows.Gaming.XboxLive.Storage
import Windows.Storage.Streams
import Windows.System
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobGetResult) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveBlobInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo'
    @winrt_mixinmethod
    def get_Name(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfo) -> UInt32: ...
    Name = property(get_Name, None)
    Size = property(get_Size, None)
class GameSaveBlobInfoGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoGetResult) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveBlobInfoQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery'
    @winrt_mixinmethod
    def GetBlobInfoAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_mixinmethod
    def GetBlobInfoWithIndexAndMaxAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveBlobInfoQuery) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
class GameSaveContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainer'
    @winrt_mixinmethod
    def get_Name(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Provider(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer) -> Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    @winrt_mixinmethod
    def SubmitUpdatesAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToWrite: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer], blobsToDelete: Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def ReadAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToRead: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer]) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def GetAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToRead: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult]: ...
    @winrt_mixinmethod
    def SubmitPropertySetUpdatesAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobsToWrite: Windows.Foundation.Collections.IPropertySet, blobsToDelete: Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def CreateBlobInfoQuery(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainer, blobNamePrefix: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery: ...
    Name = property(get_Name, None)
    Provider = property(get_Provider, None)
class GameSaveContainerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo'
    @winrt_mixinmethod
    def get_Name(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TotalSize(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastModifiedTime(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NeedsSync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfo) -> Boolean: ...
    Name = property(get_Name, None)
    TotalSize = property(get_TotalSize, None)
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    NeedsSync = property(get_NeedsSync, None)
class GameSaveContainerInfoGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoGetResult) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GameSaveContainerInfoQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery'
    @winrt_mixinmethod
    def GetContainerInfoAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_mixinmethod
    def GetContainerInfoWithIndexAndMaxAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveContainerInfoQuery) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveOperationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.XboxLive.Storage.IGameSaveOperationResult) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    Status = property(get_Status, None)
class GameSaveProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveProvider'
    @winrt_mixinmethod
    def get_User(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> Windows.System.User: ...
    @winrt_mixinmethod
    def CreateContainer(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider, name: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveContainer: ...
    @winrt_mixinmethod
    def DeleteContainerAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_mixinmethod
    def CreateContainerInfoQuery(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_mixinmethod
    def CreateContainerInfoQueryWithName(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider, containerNamePrefix: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_mixinmethod
    def GetRemainingBytesInQuotaAsync(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> Windows.Foundation.IAsyncOperation[Int64]: ...
    @winrt_mixinmethod
    def get_ContainersChangedSinceLastSync(self: Windows.Gaming.XboxLive.Storage.IGameSaveProvider) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def GetForUserAsync(cls: Windows.Gaming.XboxLive.Storage.IGameSaveProviderStatics, user: Windows.System.User, serviceConfigId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    @winrt_classmethod
    def GetSyncOnDemandForUserAsync(cls: Windows.Gaming.XboxLive.Storage.IGameSaveProviderStatics, user: Windows.System.User, serviceConfigId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    User = property(get_User, None)
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
class GameSaveProviderGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Gaming.XboxLive.Storage.IGameSaveProviderGetResult) -> Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('917281e0-7201-4953-aa-2c-40-08-f0-3a-ef-45')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('add38034-baf0-4645-b6-d0-46-ed-af-fb-3c-2b')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Size(self) -> UInt32: ...
    Name = property(get_Name, None)
    Size = property(get_Size, None)
class IGameSaveBlobInfoGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c7578582-3697-42bf-98-9c-66-5d-92-3b-52-31')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveBlobInfoQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9fdd74b2-eeee-447b-a9-d2-7f-96-c0-f8-32-08')
    @winrt_commethod(6)
    def GetBlobInfoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_commethod(7)
    def GetBlobInfoWithIndexAndMaxAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoGetResult]: ...
    @winrt_commethod(8)
    def GetItemCountAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
class IGameSaveContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c3c08f89-563f-4ecd-9c-6f-33-fd-0e-32-3d-10')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Provider(self) -> Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    @winrt_commethod(8)
    def SubmitUpdatesAsync(self, blobsToWrite: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer], blobsToDelete: Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(9)
    def ReadAsync(self, blobsToRead: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.IBuffer]) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(10)
    def GetAsync(self, blobsToRead: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveBlobGetResult]: ...
    @winrt_commethod(11)
    def SubmitPropertySetUpdatesAsync(self, blobsToWrite: Windows.Foundation.Collections.IPropertySet, blobsToDelete: Windows.Foundation.Collections.IIterable[WinRT_String], displayName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(12)
    def CreateBlobInfoQuery(self, blobNamePrefix: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveBlobInfoQuery: ...
    Name = property(get_Name, None)
    Provider = property(get_Provider, None)
class IGameSaveContainerInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b7e27300-155d-4bb4-b2-ba-93-03-06-f3-91-b5')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TotalSize(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_LastModifiedTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_NeedsSync(self) -> Boolean: ...
    Name = property(get_Name, None)
    TotalSize = property(get_TotalSize, None)
    DisplayName = property(get_DisplayName, None)
    LastModifiedTime = property(get_LastModifiedTime, None)
    NeedsSync = property(get_NeedsSync, None)
class IGameSaveContainerInfoGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ffc50d74-c581-4f9d-9e-39-30-a1-0c-1e-4c-50')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Foundation.Collections.IVectorView[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfo]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveContainerInfoQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3c94e863-6f80-4327-93-27-ff-c1-1a-fd-42-b3')
    @winrt_commethod(6)
    def GetContainerInfoAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_commethod(7)
    def GetContainerInfoWithIndexAndMaxAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoGetResult]: ...
    @winrt_commethod(8)
    def GetItemCountAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
class IGameSaveOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cf0f1a05-24a0-4582-9a-55-b1-bb-bb-93-88-d8')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    Status = property(get_Status, None)
class IGameSaveProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('90a60394-80fe-4211-97-f8-a5-de-14-dd-95-d2')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def CreateContainer(self, name: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveContainer: ...
    @winrt_commethod(8)
    def DeleteContainerAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveOperationResult]: ...
    @winrt_commethod(9)
    def CreateContainerInfoQuery(self) -> Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_commethod(10)
    def CreateContainerInfoQueryWithName(self, containerNamePrefix: WinRT_String) -> Windows.Gaming.XboxLive.Storage.GameSaveContainerInfoQuery: ...
    @winrt_commethod(11)
    def GetRemainingBytesInQuotaAsync(self) -> Windows.Foundation.IAsyncOperation[Int64]: ...
    @winrt_commethod(12)
    def get_ContainersChangedSinceLastSync(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    User = property(get_User, None)
    ContainersChangedSinceLastSync = property(get_ContainersChangedSinceLastSync, None)
class IGameSaveProviderGetResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3ab90816-d393-4d65-ac-16-41-c3-e6-7a-b9-45')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Gaming.XboxLive.Storage.GameSaveProvider: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGameSaveProviderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d01d3ed0-7b03-449d-8c-bd-34-02-84-2a-10-48')
    @winrt_commethod(6)
    def GetForUserAsync(self, user: Windows.System.User, serviceConfigId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
    @winrt_commethod(7)
    def GetSyncOnDemandForUserAsync(self, user: Windows.System.User, serviceConfigId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Gaming.XboxLive.Storage.GameSaveProviderGetResult]: ...
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
