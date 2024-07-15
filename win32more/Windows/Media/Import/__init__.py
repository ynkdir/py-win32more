from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Import
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IPhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult'
    _iid_ = Guid('{f4e112f8-843d-428a-a1a6-81510292b0ae}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DeletedItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
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
    DeletedItems = property(get_DeletedItems, None)
    HasSucceeded = property(get_HasSucceeded, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
class IPhotoImportFindItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportFindItemsResult'
    _iid_ = Guid('{3915e647-6c78-492b-844e-8fe5e8f6bfb9}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_FoundItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
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
    def SelectNewAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(22)
    def SetImportMode(self, value: win32more.Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_commethod(23)
    def get_ImportMode(self) -> win32more.Windows.Media.Import.PhotoImportImportMode: ...
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
    def add_SelectionChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_SelectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def ImportItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(37)
    def add_ItemImported(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_ItemImported(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FoundItems = property(get_FoundItems, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportMode = property(get_ImportMode, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SelectionChanged = event()
    ItemImported = event()
class IPhotoImportFindItemsResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportFindItemsResult2'
    _iid_ = Guid('{fbdd6a3b-ecf9-406a-815e-5015625b0a88}')
    @winrt_commethod(6)
    def AddItemsInDateRangeToSelection(self, rangeStart: win32more.Windows.Foundation.DateTime, rangeLength: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class IPhotoImportImportItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportImportItemsResult'
    _iid_ = Guid('{e4d4f478-d419-4443-a84e-f06a850c0b00}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ImportedItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
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
    def DeleteImportedItemsFromSourceAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
class IPhotoImportItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItem'
    _iid_ = Guid('{a9d07e76-9bfc-43b8-b356-633b6a988c9e}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ItemKey(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ContentType(self) -> win32more.Windows.Media.Import.PhotoImportContentType: ...
    @winrt_commethod(9)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Sibling(self) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(12)
    def get_Sidecars(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_commethod(13)
    def get_VideoSegments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_commethod(14)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(17)
    def get_ImportedFileNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(18)
    def get_DeletedFileNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    ContentType = property(get_ContentType, None)
    Date = property(get_Date, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    ItemKey = property(get_ItemKey, None)
    Name = property(get_Name, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Thumbnail = property(get_Thumbnail, None)
    VideoSegments = property(get_VideoSegments, None)
class IPhotoImportItem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItem2'
    _iid_ = Guid('{f1053505-f53b-46a3-9e30-3610791a9110}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPhotoImportItemImportedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItemImportedEventArgs'
    _iid_ = Guid('{42cb2fdd-7d68-47b5-bc7c-ceb73e0c77dc}')
    @winrt_commethod(6)
    def get_ImportedItem(self) -> win32more.Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
class IPhotoImportManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportManagerStatics'
    _iid_ = Guid('{2771903d-a046-4f06-9b9c-bfd662e83287}')
    @winrt_commethod(6)
    def IsSupportedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def FindAllSourcesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_commethod(8)
    def GetPendingOperations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportOperation]: ...
class IPhotoImportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportOperation'
    _iid_ = Guid('{d9f797e4-a09a-4ee4-a4b1-20940277a5be}')
    @winrt_commethod(6)
    def get_Stage(self) -> win32more.Windows.Media.Import.PhotoImportStage: ...
    @winrt_commethod(7)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(8)
    def get_ContinueFindingItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_commethod(9)
    def get_ContinueImportingItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(10)
    def get_ContinueDeletingImportedItemsFromSourceAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    Session = property(get_Session, None)
    Stage = property(get_Stage, None)
class IPhotoImportSelectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSelectionChangedEventArgs'
    _iid_ = Guid('{10461782-fa9d-4c30-8bc9-4d64911572d5}')
    @winrt_commethod(6)
    def get_IsSelectionEmpty(self) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class IPhotoImportSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Import.IPhotoImportSession'
    _iid_ = Guid('{aa63916e-ecdb-4efe-94c6-5f5cafe34cfb}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Media.Import.PhotoImportSource: ...
    @winrt_commethod(7)
    def get_SessionId(self) -> Guid: ...
    @winrt_commethod(8)
    def put_DestinationFolder(self, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_commethod(9)
    def get_DestinationFolder(self) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_commethod(10)
    def put_AppendSessionDateToDestinationFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_AppendSessionDateToDestinationFolder(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SubfolderCreationMode(self, value: win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_commethod(13)
    def get_SubfolderCreationMode(self) -> win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_commethod(14)
    def put_DestinationFileNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_DestinationFileNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def FindItemsAsync(self, contentTypeFilter: win32more.Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: win32more.Windows.Media.Import.PhotoImportItemSelectionMode) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    SessionId = property(get_SessionId, None)
    Source = property(get_Source, None)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
class IPhotoImportSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSession2'
    _iid_ = Guid('{2a526710-3ec6-469d-a375-2b9f4785391e}')
    @winrt_commethod(6)
    def put_SubfolderDateFormat(self, value: win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_commethod(7)
    def get_SubfolderDateFormat(self) -> win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_commethod(8)
    def put_RememberDeselectedItems(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_RememberDeselectedItems(self) -> Boolean: ...
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
class IPhotoImportSidecar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSidecar'
    _iid_ = Guid('{46d7d757-f802-44c7-9c98-7a71f4bc1486}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    Date = property(get_Date, None)
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
class IPhotoImportSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSource'
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
    def get_ConnectionTransport(self) -> win32more.Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_commethod(14)
    def get_Type(self) -> win32more.Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_commethod(15)
    def get_PowerSource(self) -> win32more.Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_commethod(16)
    def get_BatteryLevelPercent(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(17)
    def get_DateTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(18)
    def get_StorageMedia(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_commethod(19)
    def get_IsLocked(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(20)
    def get_IsMassStorage(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(22)
    def CreateImportSession(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    DateTime = property(get_DateTime, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    PowerSource = property(get_PowerSource, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMedia = property(get_StorageMedia, None)
    Thumbnail = property(get_Thumbnail, None)
    Type = property(get_Type, None)
class IPhotoImportSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSourceStatics'
    _iid_ = Guid('{0528e586-32d8-467c-8cee-23a1b2f43e85}')
    @winrt_commethod(6)
    def FromIdAsync(self, sourceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    @winrt_commethod(7)
    def FromFolderAsync(self, sourceRootFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
class IPhotoImportStorageMedium(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportStorageMedium'
    _iid_ = Guid('{f2b9b093-fc85-487f-87c2-58d675d05b07}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_StorageMediumType(self) -> win32more.Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_commethod(10)
    def get_SupportedAccessMode(self) -> win32more.Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_commethod(11)
    def get_CapacityInBytes(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_AvailableSpaceInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def Refresh(self) -> Void: ...
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    Description = property(get_Description, None)
    Name = property(get_Name, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
class IPhotoImportVideoSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportVideoSegment'
    _iid_ = Guid('{623c0289-321a-41d8-9166-8c62a333276c}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Sibling(self) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(10)
    def get_Sidecars(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    Date = property(get_Date, None)
    Name = property(get_Name, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    SizeInBytes = property(get_SizeInBytes, None)
class PhotoImportAccessMode(Enum, Int32):
    ReadWrite = 0
    ReadOnly = 1
    ReadAndDelete = 2
class PhotoImportConnectionTransport(Enum, Int32):
    Unknown = 0
    Usb = 1
    IP = 2
    Bluetooth = 3
class PhotoImportContentType(Enum, Int32):
    Unknown = 0
    Image = 1
    Video = 2
class PhotoImportContentTypeFilter(Enum, Int32):
    OnlyImages = 0
    OnlyVideos = 1
    ImagesAndVideos = 2
    ImagesAndVideosFromCameraRoll = 3
class PhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult
    _classid_ = 'Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeletedItems(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    DeletedItems = property(get_DeletedItems, None)
    HasSucceeded = property(get_HasSucceeded, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
class PhotoImportFindItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportFindItemsResult
    _classid_ = 'Windows.Media.Import.PhotoImportFindItemsResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_FoundItems(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def SelectAll(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNone(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNewAsync(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetImportMode(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_mixinmethod
    def get_ImportMode(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Media.Import.PhotoImportImportMode: ...
    @winrt_mixinmethod
    def get_SelectedPhotosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedPhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedVideosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedVideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedTotalCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedTotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ImportItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def add_ItemImported(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemImported(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddItemsInDateRangeToSelection(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult2, rangeStart: win32more.Windows.Foundation.DateTime, rangeLength: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    FoundItems = property(get_FoundItems, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportMode = property(get_ImportMode, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SelectionChanged = event()
    ItemImported = event()
class PhotoImportImportItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportImportItemsResult
    _classid_ = 'Windows.Media.Import.PhotoImportImportItemsResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ImportedItems(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def DeleteImportedItemsFromSourceAsync(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    Session = property(get_Session, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
class PhotoImportImportMode(Enum, Int32):
    ImportEverything = 0
    IgnoreSidecars = 1
    IgnoreSiblings = 2
    IgnoreSidecarsAndSiblings = 3
class PhotoImportItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportItem
    _classid_ = 'Windows.Media.Import.PhotoImportItem'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ItemKey(self: win32more.Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Media.Import.PhotoImportContentType: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_mixinmethod
    def get_VideoSegments(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.Media.Import.IPhotoImportItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: win32more.Windows.Media.Import.IPhotoImportItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ImportedFileNames(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeletedFileNames(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Media.Import.IPhotoImportItem2) -> WinRT_String: ...
    ContentType = property(get_ContentType, None)
    Date = property(get_Date, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    ItemKey = property(get_ItemKey, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Thumbnail = property(get_Thumbnail, None)
    VideoSegments = property(get_VideoSegments, None)
class PhotoImportItemImportedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportItemImportedEventArgs
    _classid_ = 'Windows.Media.Import.PhotoImportItemImportedEventArgs'
    @winrt_mixinmethod
    def get_ImportedItem(self: win32more.Windows.Media.Import.IPhotoImportItemImportedEventArgs) -> win32more.Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
class PhotoImportItemSelectionMode(Enum, Int32):
    SelectAll = 0
    SelectNone = 1
    SelectNew = 2
class PhotoImportManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportManager'
    @winrt_classmethod
    def IsSupportedAsync(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def FindAllSourcesAsync(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_classmethod
    def GetPendingOperations(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportOperation]: ...
class PhotoImportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportOperation
    _classid_ = 'Windows.Media.Import.PhotoImportOperation'
    @winrt_mixinmethod
    def get_Stage(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Media.Import.PhotoImportStage: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_ContinueFindingItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def get_ContinueImportingItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def get_ContinueDeletingImportedItemsFromSourceAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    Session = property(get_Session, None)
    Stage = property(get_Stage, None)
class PhotoImportPowerSource(Enum, Int32):
    Unknown = 0
    Battery = 1
    External = 2
class PhotoImportProgress(Structure):
    ItemsImported: UInt32
    TotalItemsToImport: UInt32
    BytesImported: UInt64
    TotalBytesToImport: UInt64
    ImportProgress: Double
class PhotoImportSelectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSelectionChangedEventArgs
    _classid_ = 'Windows.Media.Import.PhotoImportSelectionChangedEventArgs'
    @winrt_mixinmethod
    def get_IsSelectionEmpty(self: win32more.Windows.Media.Import.IPhotoImportSelectionChangedEventArgs) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class PhotoImportSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Import.IPhotoImportSession
    _classid_ = 'Windows.Media.Import.PhotoImportSession'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Media.Import.PhotoImportSource: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Media.Import.IPhotoImportSession) -> Guid: ...
    @winrt_mixinmethod
    def put_DestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_mixinmethod
    def put_AppendSessionDateToDestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppendSessionDateToDestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_SubfolderCreationMode(self: win32more.Windows.Media.Import.IPhotoImportSession, value: win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderCreationMode(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_mixinmethod
    def put_DestinationFileNamePrefix(self: win32more.Windows.Media.Import.IPhotoImportSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFileNamePrefix(self: win32more.Windows.Media.Import.IPhotoImportSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def FindItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportSession, contentTypeFilter: win32more.Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: win32more.Windows.Media.Import.PhotoImportItemSelectionMode) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_SubfolderDateFormat(self: win32more.Windows.Media.Import.IPhotoImportSession2, value: win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderDateFormat(self: win32more.Windows.Media.Import.IPhotoImportSession2) -> win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_mixinmethod
    def put_RememberDeselectedItems(self: win32more.Windows.Media.Import.IPhotoImportSession2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RememberDeselectedItems(self: win32more.Windows.Media.Import.IPhotoImportSession2) -> Boolean: ...
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
    SessionId = property(get_SessionId, None)
    Source = property(get_Source, None)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
class PhotoImportSidecar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSidecar
    _classid_ = 'Windows.Media.Import.PhotoImportSidecar'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> win32more.Windows.Foundation.DateTime: ...
    Date = property(get_Date, None)
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
class PhotoImportSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSource
    _classid_ = 'Windows.Media.Import.PhotoImportSource'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Model(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionProtocol(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionTransport(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_mixinmethod
    def get_PowerSource(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_mixinmethod
    def get_BatteryLevelPercent(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_DateTime(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_StorageMedia(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_mixinmethod
    def get_IsLocked(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_IsMassStorage(self: win32more.Windows.Media.Import.IPhotoImportSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def CreateImportSession(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Media.Import.IPhotoImportSourceStatics, sourceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    @winrt_classmethod
    def FromFolderAsync(cls: win32more.Windows.Media.Import.IPhotoImportSourceStatics, sourceRootFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    DateTime = property(get_DateTime, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    PowerSource = property(get_PowerSource, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMedia = property(get_StorageMedia, None)
    Thumbnail = property(get_Thumbnail, None)
    Type = property(get_Type, None)
class PhotoImportSourceType(Enum, Int32):
    Generic = 0
    Camera = 1
    MediaPlayer = 2
    Phone = 3
    Video = 4
    PersonalInfoManager = 5
    AudioRecorder = 6
class PhotoImportStage(Enum, Int32):
    NotStarted = 0
    FindingItems = 1
    ImportingItems = 2
    DeletingImportedItemsFromSource = 3
class PhotoImportStorageMedium(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportStorageMedium
    _classid_ = 'Windows.Media.Import.PhotoImportStorageMedium'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StorageMediumType(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> win32more.Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_mixinmethod
    def get_SupportedAccessMode(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> win32more.Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_mixinmethod
    def get_CapacityInBytes(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def get_AvailableSpaceInBytes(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def Refresh(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> Void: ...
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    Description = property(get_Description, None)
    Name = property(get_Name, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
class PhotoImportStorageMediumType(Enum, Int32):
    Undefined = 0
    Fixed = 1
    Removable = 2
class PhotoImportSubfolderCreationMode(Enum, Int32):
    DoNotCreateSubfolders = 0
    CreateSubfoldersFromFileDate = 1
    CreateSubfoldersFromExifDate = 2
    KeepOriginalFolderStructure = 3
class PhotoImportSubfolderDateFormat(Enum, Int32):
    Year = 0
    YearMonth = 1
    YearMonthDay = 2
class PhotoImportVideoSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportVideoSegment
    _classid_ = 'Windows.Media.Import.PhotoImportVideoSegment'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    Date = property(get_Date, None)
    Name = property(get_Name, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    SizeInBytes = property(get_SizeInBytes, None)


make_ready(__name__)
