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
import Windows.Media.Import
import Windows.Storage
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
class IPhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f4e112f8-843d-428a-a1a6-81510292b0ae}')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DeletedItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    DeletedItems = property(get_DeletedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class IPhotoImportFindItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3915e647-6c78-492b-844e-8fe5e8f6bfb9}')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_FoundItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(19)
    def SelectAll(self) -> Void: ...
    @winrt_commethod(20)
    def SelectNone(self) -> Void: ...
    @winrt_commethod(21)
    def SelectNewAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(22)
    def SetImportMode(self, value: Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_commethod(23)
    def get_ImportMode(self) -> Windows.Media.Import.PhotoImportImportMode: ...
    @winrt_commethod(24)
    def get_SelectedPhotosCount(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_SelectedPhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(26)
    def get_SelectedVideosCount(self) -> UInt32: ...
    @winrt_commethod(27)
    def get_SelectedVideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(28)
    def get_SelectedSidecarsCount(self) -> UInt32: ...
    @winrt_commethod(29)
    def get_SelectedSidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(30)
    def get_SelectedSiblingsCount(self) -> UInt32: ...
    @winrt_commethod(31)
    def get_SelectedSiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(32)
    def get_SelectedTotalCount(self) -> UInt32: ...
    @winrt_commethod(33)
    def get_SelectedTotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(34)
    def add_SelectionChanged(self, value: Windows.Foundation.TypedEventHandler[Windows.Media.Import.PhotoImportFindItemsResult, Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_SelectionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def ImportItemsAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportImportItemsResult, Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(37)
    def add_ItemImported(self, value: Windows.Foundation.TypedEventHandler[Windows.Media.Import.PhotoImportFindItemsResult, Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_ItemImported(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    FoundItems = property(get_FoundItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    ImportMode = property(get_ImportMode, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
class IPhotoImportFindItemsResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fbdd6a3b-ecf9-406a-815e-5015625b0a88}')
    @winrt_commethod(6)
    def AddItemsInDateRangeToSelection(self, rangeStart: Windows.Foundation.DateTime, rangeLength: Windows.Foundation.TimeSpan) -> Void: ...
class IPhotoImportImportItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e4d4f478-d419-4443-a84e-f06a850c0b00}')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ImportedItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(19)
    def DeleteImportedItemsFromSourceAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class IPhotoImportItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a9d07e76-9bfc-43b8-b356-633b6a988c9e}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ItemKey(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ContentType(self) -> Windows.Media.Import.PhotoImportContentType: ...
    @winrt_commethod(9)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_Date(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Sibling(self) -> Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(12)
    def get_Sidecars(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_commethod(13)
    def get_VideoSegments(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_commethod(14)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(17)
    def get_ImportedFileNames(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(18)
    def get_DeletedFileNames(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Name = property(get_Name, None)
    ItemKey = property(get_ItemKey, None)
    ContentType = property(get_ContentType, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    VideoSegments = property(get_VideoSegments, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Thumbnail = property(get_Thumbnail, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
class IPhotoImportItem2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f1053505-f53b-46a3-9e30-3610791a9110}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPhotoImportItemImportedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{42cb2fdd-7d68-47b5-bc7c-ceb73e0c77dc}')
    @winrt_commethod(6)
    def get_ImportedItem(self) -> Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
class IPhotoImportManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2771903d-a046-4f06-9b9c-bfd662e83287}')
    @winrt_commethod(6)
    def IsSupportedAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def FindAllSourcesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_commethod(8)
    def GetPendingOperations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportOperation]: ...
class IPhotoImportOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d9f797e4-a09a-4ee4-a4b1-20940277a5be}')
    @winrt_commethod(6)
    def get_Stage(self) -> Windows.Media.Import.PhotoImportStage: ...
    @winrt_commethod(7)
    def get_Session(self) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(8)
    def get_ContinueFindingItemsAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_commethod(9)
    def get_ContinueImportingItemsAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportImportItemsResult, Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(10)
    def get_ContinueDeletingImportedItemsFromSourceAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Stage = property(get_Stage, None)
    Session = property(get_Session, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
class IPhotoImportSelectionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{10461782-fa9d-4c30-8bc9-4d64911572d5}')
    @winrt_commethod(6)
    def get_IsSelectionEmpty(self) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class IPhotoImportSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aa63916e-ecdb-4efe-94c6-5f5cafe34cfb}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.Media.Import.PhotoImportSource: ...
    @winrt_commethod(7)
    def get_SessionId(self) -> Guid: ...
    @winrt_commethod(8)
    def put_DestinationFolder(self, value: Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_commethod(9)
    def get_DestinationFolder(self) -> Windows.Storage.IStorageFolder: ...
    @winrt_commethod(10)
    def put_AppendSessionDateToDestinationFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_AppendSessionDateToDestinationFolder(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SubfolderCreationMode(self, value: Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_commethod(13)
    def get_SubfolderCreationMode(self) -> Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_commethod(14)
    def put_DestinationFileNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_DestinationFileNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def FindItemsAsync(self, contentTypeFilter: Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: Windows.Media.Import.PhotoImportItemSelectionMode) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    Source = property(get_Source, None)
    SessionId = property(get_SessionId, None)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
class IPhotoImportSession2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2a526710-3ec6-469d-a375-2b9f4785391e}')
    @winrt_commethod(6)
    def put_SubfolderDateFormat(self, value: Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_commethod(7)
    def get_SubfolderDateFormat(self) -> Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_commethod(8)
    def put_RememberDeselectedItems(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_RememberDeselectedItems(self) -> Boolean: ...
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
class IPhotoImportSidecar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{46d7d757-f802-44c7-9c98-7a71f4bc1486}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> Windows.Foundation.DateTime: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
class IPhotoImportSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1f8ea35e-145b-4cd6-87f1-54965a982fef}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Manufacturer(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Model(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ConnectionProtocol(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_ConnectionTransport(self) -> Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_commethod(14)
    def get_Type(self) -> Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_commethod(15)
    def get_PowerSource(self) -> Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_commethod(16)
    def get_BatteryLevelPercent(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(17)
    def get_DateTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(18)
    def get_StorageMedia(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_commethod(19)
    def get_IsLocked(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(20)
    def get_IsMassStorage(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(22)
    def CreateImportSession(self) -> Windows.Media.Import.PhotoImportSession: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    SerialNumber = property(get_SerialNumber, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    Type = property(get_Type, None)
    PowerSource = property(get_PowerSource, None)
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    DateTime = property(get_DateTime, None)
    StorageMedia = property(get_StorageMedia, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Thumbnail = property(get_Thumbnail, None)
class IPhotoImportSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0528e586-32d8-467c-8cee-23a1b2f43e85}')
    @winrt_commethod(6)
    def FromIdAsync(self, sourceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Import.PhotoImportSource]: ...
    @winrt_commethod(7)
    def FromFolderAsync(self, sourceRootFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Media.Import.PhotoImportSource]: ...
class IPhotoImportStorageMedium(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f2b9b093-fc85-487f-87c2-58d675d05b07}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_StorageMediumType(self) -> Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_commethod(10)
    def get_SupportedAccessMode(self) -> Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_commethod(11)
    def get_CapacityInBytes(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_AvailableSpaceInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def Refresh(self) -> Void: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
class IPhotoImportVideoSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{623c0289-321a-41d8-9166-8c62a333276c}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Sibling(self) -> Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(10)
    def get_Sidecars(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSidecar]: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
PhotoImportAccessMode = Int32
PhotoImportAccessMode_ReadWrite: PhotoImportAccessMode = 0
PhotoImportAccessMode_ReadOnly: PhotoImportAccessMode = 1
PhotoImportAccessMode_ReadAndDelete: PhotoImportAccessMode = 2
PhotoImportConnectionTransport = Int32
PhotoImportConnectionTransport_Unknown: PhotoImportConnectionTransport = 0
PhotoImportConnectionTransport_Usb: PhotoImportConnectionTransport = 1
PhotoImportConnectionTransport_IP: PhotoImportConnectionTransport = 2
PhotoImportConnectionTransport_Bluetooth: PhotoImportConnectionTransport = 3
PhotoImportContentType = Int32
PhotoImportContentType_Unknown: PhotoImportContentType = 0
PhotoImportContentType_Image: PhotoImportContentType = 1
PhotoImportContentType_Video: PhotoImportContentType = 2
PhotoImportContentTypeFilter = Int32
PhotoImportContentTypeFilter_OnlyImages: PhotoImportContentTypeFilter = 0
PhotoImportContentTypeFilter_OnlyVideos: PhotoImportContentTypeFilter = 1
PhotoImportContentTypeFilter_ImagesAndVideos: PhotoImportContentTypeFilter = 2
PhotoImportContentTypeFilter_ImagesAndVideosFromCameraRoll: PhotoImportContentTypeFilter = 3
class PhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult'
    @winrt_mixinmethod
    def get_Session(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeletedItems(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    DeletedItems = property(get_DeletedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class PhotoImportFindItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportFindItemsResult'
    @winrt_mixinmethod
    def get_Session(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_FoundItems(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def SelectAll(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNone(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNewAsync(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetImportMode(self: Windows.Media.Import.IPhotoImportFindItemsResult, value: Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_mixinmethod
    def get_ImportMode(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Windows.Media.Import.PhotoImportImportMode: ...
    @winrt_mixinmethod
    def get_SelectedPhotosCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedPhotosSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedVideosCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedVideosSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedTotalCount(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedTotalSizeInBytes(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: Windows.Media.Import.IPhotoImportFindItemsResult, value: Windows.Foundation.TypedEventHandler[Windows.Media.Import.PhotoImportFindItemsResult, Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: Windows.Media.Import.IPhotoImportFindItemsResult, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ImportItemsAsync(self: Windows.Media.Import.IPhotoImportFindItemsResult) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportImportItemsResult, Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def add_ItemImported(self: Windows.Media.Import.IPhotoImportFindItemsResult, value: Windows.Foundation.TypedEventHandler[Windows.Media.Import.PhotoImportFindItemsResult, Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemImported(self: Windows.Media.Import.IPhotoImportFindItemsResult, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddItemsInDateRangeToSelection(self: Windows.Media.Import.IPhotoImportFindItemsResult2, rangeStart: Windows.Foundation.DateTime, rangeLength: Windows.Foundation.TimeSpan) -> Void: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    FoundItems = property(get_FoundItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    ImportMode = property(get_ImportMode, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
class PhotoImportImportItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportImportItemsResult'
    @winrt_mixinmethod
    def get_Session(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ImportedItems(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def DeleteImportedItemsFromSourceAsync(self: Windows.Media.Import.IPhotoImportImportItemsResult) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
PhotoImportImportMode = Int32
PhotoImportImportMode_ImportEverything: PhotoImportImportMode = 0
PhotoImportImportMode_IgnoreSidecars: PhotoImportImportMode = 1
PhotoImportImportMode_IgnoreSiblings: PhotoImportImportMode = 2
PhotoImportImportMode_IgnoreSidecarsAndSiblings: PhotoImportImportMode = 3
class PhotoImportItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportItem'
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Import.IPhotoImportItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ItemKey(self: Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Media.Import.PhotoImportContentType: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_mixinmethod
    def get_VideoSegments(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.Media.Import.IPhotoImportItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: Windows.Media.Import.IPhotoImportItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ImportedFileNames(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeletedFileNames(self: Windows.Media.Import.IPhotoImportItem) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Media.Import.IPhotoImportItem2) -> WinRT_String: ...
    Name = property(get_Name, None)
    ItemKey = property(get_ItemKey, None)
    ContentType = property(get_ContentType, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    VideoSegments = property(get_VideoSegments, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Thumbnail = property(get_Thumbnail, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
    Path = property(get_Path, None)
class PhotoImportItemImportedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportItemImportedEventArgs'
    @winrt_mixinmethod
    def get_ImportedItem(self: Windows.Media.Import.IPhotoImportItemImportedEventArgs) -> Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
PhotoImportItemSelectionMode = Int32
PhotoImportItemSelectionMode_SelectAll: PhotoImportItemSelectionMode = 0
PhotoImportItemSelectionMode_SelectNone: PhotoImportItemSelectionMode = 1
PhotoImportItemSelectionMode_SelectNew: PhotoImportItemSelectionMode = 2
class PhotoImportManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportManager'
    @winrt_classmethod
    def IsSupportedAsync(cls: Windows.Media.Import.IPhotoImportManagerStatics) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def FindAllSourcesAsync(cls: Windows.Media.Import.IPhotoImportManagerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_classmethod
    def GetPendingOperations(cls: Windows.Media.Import.IPhotoImportManagerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportOperation]: ...
class PhotoImportOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportOperation'
    @winrt_mixinmethod
    def get_Stage(self: Windows.Media.Import.IPhotoImportOperation) -> Windows.Media.Import.PhotoImportStage: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.Media.Import.IPhotoImportOperation) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_ContinueFindingItemsAsync(self: Windows.Media.Import.IPhotoImportOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def get_ContinueImportingItemsAsync(self: Windows.Media.Import.IPhotoImportOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportImportItemsResult, Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def get_ContinueDeletingImportedItemsFromSourceAsync(self: Windows.Media.Import.IPhotoImportOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Stage = property(get_Stage, None)
    Session = property(get_Session, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
PhotoImportPowerSource = Int32
PhotoImportPowerSource_Unknown: PhotoImportPowerSource = 0
PhotoImportPowerSource_Battery: PhotoImportPowerSource = 1
PhotoImportPowerSource_External: PhotoImportPowerSource = 2
class PhotoImportProgress(EasyCastStructure):
    ItemsImported: UInt32
    TotalItemsToImport: UInt32
    BytesImported: UInt64
    TotalBytesToImport: UInt64
    ImportProgress: Double
class PhotoImportSelectionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportSelectionChangedEventArgs'
    @winrt_mixinmethod
    def get_IsSelectionEmpty(self: Windows.Media.Import.IPhotoImportSelectionChangedEventArgs) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class PhotoImportSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportSession'
    @winrt_mixinmethod
    def get_Source(self: Windows.Media.Import.IPhotoImportSession) -> Windows.Media.Import.PhotoImportSource: ...
    @winrt_mixinmethod
    def get_SessionId(self: Windows.Media.Import.IPhotoImportSession) -> Guid: ...
    @winrt_mixinmethod
    def put_DestinationFolder(self: Windows.Media.Import.IPhotoImportSession, value: Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFolder(self: Windows.Media.Import.IPhotoImportSession) -> Windows.Storage.IStorageFolder: ...
    @winrt_mixinmethod
    def put_AppendSessionDateToDestinationFolder(self: Windows.Media.Import.IPhotoImportSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppendSessionDateToDestinationFolder(self: Windows.Media.Import.IPhotoImportSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_SubfolderCreationMode(self: Windows.Media.Import.IPhotoImportSession, value: Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderCreationMode(self: Windows.Media.Import.IPhotoImportSession) -> Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_mixinmethod
    def put_DestinationFileNamePrefix(self: Windows.Media.Import.IPhotoImportSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFileNamePrefix(self: Windows.Media.Import.IPhotoImportSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def FindItemsAsync(self: Windows.Media.Import.IPhotoImportSession, contentTypeFilter: Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: Windows.Media.Import.PhotoImportItemSelectionMode) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_SubfolderDateFormat(self: Windows.Media.Import.IPhotoImportSession2, value: Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderDateFormat(self: Windows.Media.Import.IPhotoImportSession2) -> Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_mixinmethod
    def put_RememberDeselectedItems(self: Windows.Media.Import.IPhotoImportSession2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RememberDeselectedItems(self: Windows.Media.Import.IPhotoImportSession2) -> Boolean: ...
    Source = property(get_Source, None)
    SessionId = property(get_SessionId, None)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
class PhotoImportSidecar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportSidecar'
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Import.IPhotoImportSidecar) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: Windows.Media.Import.IPhotoImportSidecar) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: Windows.Media.Import.IPhotoImportSidecar) -> Windows.Foundation.DateTime: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
class PhotoImportSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportSource'
    @winrt_mixinmethod
    def get_Id(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Model(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionProtocol(self: Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionTransport(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_mixinmethod
    def get_PowerSource(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_mixinmethod
    def get_BatteryLevelPercent(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_DateTime(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_StorageMedia(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_mixinmethod
    def get_IsLocked(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_IsMassStorage(self: Windows.Media.Import.IPhotoImportSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def CreateImportSession(self: Windows.Media.Import.IPhotoImportSource) -> Windows.Media.Import.PhotoImportSession: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Media.Import.IPhotoImportSourceStatics, sourceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Media.Import.PhotoImportSource]: ...
    @winrt_classmethod
    def FromFolderAsync(cls: Windows.Media.Import.IPhotoImportSourceStatics, sourceRootFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Media.Import.PhotoImportSource]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    SerialNumber = property(get_SerialNumber, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    Type = property(get_Type, None)
    PowerSource = property(get_PowerSource, None)
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    DateTime = property(get_DateTime, None)
    StorageMedia = property(get_StorageMedia, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Thumbnail = property(get_Thumbnail, None)
PhotoImportSourceType = Int32
PhotoImportSourceType_Generic: PhotoImportSourceType = 0
PhotoImportSourceType_Camera: PhotoImportSourceType = 1
PhotoImportSourceType_MediaPlayer: PhotoImportSourceType = 2
PhotoImportSourceType_Phone: PhotoImportSourceType = 3
PhotoImportSourceType_Video: PhotoImportSourceType = 4
PhotoImportSourceType_PersonalInfoManager: PhotoImportSourceType = 5
PhotoImportSourceType_AudioRecorder: PhotoImportSourceType = 6
PhotoImportStage = Int32
PhotoImportStage_NotStarted: PhotoImportStage = 0
PhotoImportStage_FindingItems: PhotoImportStage = 1
PhotoImportStage_ImportingItems: PhotoImportStage = 2
PhotoImportStage_DeletingImportedItemsFromSource: PhotoImportStage = 3
class PhotoImportStorageMedium(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportStorageMedium'
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StorageMediumType(self: Windows.Media.Import.IPhotoImportStorageMedium) -> Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_mixinmethod
    def get_SupportedAccessMode(self: Windows.Media.Import.IPhotoImportStorageMedium) -> Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_mixinmethod
    def get_CapacityInBytes(self: Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def get_AvailableSpaceInBytes(self: Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def Refresh(self: Windows.Media.Import.IPhotoImportStorageMedium) -> Void: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
PhotoImportStorageMediumType = Int32
PhotoImportStorageMediumType_Undefined: PhotoImportStorageMediumType = 0
PhotoImportStorageMediumType_Fixed: PhotoImportStorageMediumType = 1
PhotoImportStorageMediumType_Removable: PhotoImportStorageMediumType = 2
PhotoImportSubfolderCreationMode = Int32
PhotoImportSubfolderCreationMode_DoNotCreateSubfolders: PhotoImportSubfolderCreationMode = 0
PhotoImportSubfolderCreationMode_CreateSubfoldersFromFileDate: PhotoImportSubfolderCreationMode = 1
PhotoImportSubfolderCreationMode_CreateSubfoldersFromExifDate: PhotoImportSubfolderCreationMode = 2
PhotoImportSubfolderCreationMode_KeepOriginalFolderStructure: PhotoImportSubfolderCreationMode = 3
PhotoImportSubfolderDateFormat = Int32
PhotoImportSubfolderDateFormat_Year: PhotoImportSubfolderDateFormat = 0
PhotoImportSubfolderDateFormat_YearMonth: PhotoImportSubfolderDateFormat = 1
PhotoImportSubfolderDateFormat_YearMonthDay: PhotoImportSubfolderDateFormat = 2
class PhotoImportVideoSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportVideoSegment'
    @winrt_mixinmethod
    def get_Name(self: Windows.Media.Import.IPhotoImportVideoSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: Windows.Media.Import.IPhotoImportVideoSegment) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: Windows.Media.Import.IPhotoImportVideoSegment) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: Windows.Media.Import.IPhotoImportVideoSegment) -> Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: Windows.Media.Import.IPhotoImportVideoSegment) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Import.PhotoImportSidecar]: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
make_head(_module, 'IPhotoImportDeleteImportedItemsFromSourceResult')
make_head(_module, 'IPhotoImportFindItemsResult')
make_head(_module, 'IPhotoImportFindItemsResult2')
make_head(_module, 'IPhotoImportImportItemsResult')
make_head(_module, 'IPhotoImportItem')
make_head(_module, 'IPhotoImportItem2')
make_head(_module, 'IPhotoImportItemImportedEventArgs')
make_head(_module, 'IPhotoImportManagerStatics')
make_head(_module, 'IPhotoImportOperation')
make_head(_module, 'IPhotoImportSelectionChangedEventArgs')
make_head(_module, 'IPhotoImportSession')
make_head(_module, 'IPhotoImportSession2')
make_head(_module, 'IPhotoImportSidecar')
make_head(_module, 'IPhotoImportSource')
make_head(_module, 'IPhotoImportSourceStatics')
make_head(_module, 'IPhotoImportStorageMedium')
make_head(_module, 'IPhotoImportVideoSegment')
make_head(_module, 'PhotoImportDeleteImportedItemsFromSourceResult')
make_head(_module, 'PhotoImportFindItemsResult')
make_head(_module, 'PhotoImportImportItemsResult')
make_head(_module, 'PhotoImportItem')
make_head(_module, 'PhotoImportItemImportedEventArgs')
make_head(_module, 'PhotoImportManager')
make_head(_module, 'PhotoImportOperation')
make_head(_module, 'PhotoImportProgress')
make_head(_module, 'PhotoImportSelectionChangedEventArgs')
make_head(_module, 'PhotoImportSession')
make_head(_module, 'PhotoImportSidecar')
make_head(_module, 'PhotoImportSource')
make_head(_module, 'PhotoImportStorageMedium')
make_head(_module, 'PhotoImportVideoSegment')
