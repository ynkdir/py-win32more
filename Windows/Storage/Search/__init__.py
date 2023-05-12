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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Data.Text
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.FileProperties
import Windows.Storage.Search
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
CommonFileQuery = Int32
CommonFileQuery_DefaultQuery: CommonFileQuery = 0
CommonFileQuery_OrderByName: CommonFileQuery = 1
CommonFileQuery_OrderByTitle: CommonFileQuery = 2
CommonFileQuery_OrderByMusicProperties: CommonFileQuery = 3
CommonFileQuery_OrderBySearchRank: CommonFileQuery = 4
CommonFileQuery_OrderByDate: CommonFileQuery = 5
CommonFolderQuery = Int32
CommonFolderQuery_DefaultQuery: CommonFolderQuery = 0
CommonFolderQuery_GroupByYear: CommonFolderQuery = 100
CommonFolderQuery_GroupByMonth: CommonFolderQuery = 101
CommonFolderQuery_GroupByArtist: CommonFolderQuery = 102
CommonFolderQuery_GroupByAlbum: CommonFolderQuery = 103
CommonFolderQuery_GroupByAlbumArtist: CommonFolderQuery = 104
CommonFolderQuery_GroupByComposer: CommonFolderQuery = 105
CommonFolderQuery_GroupByGenre: CommonFolderQuery = 106
CommonFolderQuery_GroupByPublishedYear: CommonFolderQuery = 107
CommonFolderQuery_GroupByRating: CommonFolderQuery = 108
CommonFolderQuery_GroupByTag: CommonFolderQuery = 109
CommonFolderQuery_GroupByAuthor: CommonFolderQuery = 110
CommonFolderQuery_GroupByType: CommonFolderQuery = 111
class ContentIndexer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IContentIndexer
    _classid_ = 'Windows.Storage.Search.ContentIndexer'
    @winrt_mixinmethod
    def AddAsync(self: Windows.Storage.Search.IContentIndexer, indexableContent: Windows.Storage.Search.IIndexableContent) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateAsync(self: Windows.Storage.Search.IContentIndexer, indexableContent: Windows.Storage.Search.IIndexableContent) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.Storage.Search.IContentIndexer, contentId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteMultipleAsync(self: Windows.Storage.Search.IContentIndexer, contentIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAllAsync(self: Windows.Storage.Search.IContentIndexer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: Windows.Storage.Search.IContentIndexer, contentId: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def get_Revision(self: Windows.Storage.Search.IContentIndexer) -> UInt64: ...
    @winrt_mixinmethod
    def CreateQueryWithSortOrderAndLanguage(self: Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: Windows.Foundation.Collections.IIterable[Windows.Storage.Search.SortEntry], searchFilterLanguage: WinRT_String) -> Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_mixinmethod
    def CreateQueryWithSortOrder(self: Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: Windows.Foundation.Collections.IIterable[Windows.Storage.Search.SortEntry]) -> Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_mixinmethod
    def CreateQuery(self: Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_classmethod
    def GetIndexerWithName(cls: Windows.Storage.Search.IContentIndexerStatics, indexName: WinRT_String) -> Windows.Storage.Search.ContentIndexer: ...
    @winrt_classmethod
    def GetIndexer(cls: Windows.Storage.Search.IContentIndexerStatics) -> Windows.Storage.Search.ContentIndexer: ...
    Revision = property(get_Revision, None)
class ContentIndexerQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IContentIndexerQuery
    _classid_ = 'Windows.Storage.Search.ContentIndexerQuery'
    @winrt_mixinmethod
    def GetCountAsync(self: Windows.Storage.Search.IContentIndexerQuery) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: Windows.Storage.Search.IContentIndexerQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_mixinmethod
    def GetPropertiesRangeAsync(self: Windows.Storage.Search.IContentIndexerQuery, startIndex: UInt32, maxItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_mixinmethod
    def GetAsync(self: Windows.Storage.Search.IContentIndexerQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_mixinmethod
    def GetRangeAsync(self: Windows.Storage.Search.IContentIndexerQuery, startIndex: UInt32, maxItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_mixinmethod
    def get_QueryFolder(self: Windows.Storage.Search.IContentIndexerQuery) -> Windows.Storage.StorageFolder: ...
    QueryFolder = property(get_QueryFolder, None)
DateStackOption = Int32
DateStackOption_None: DateStackOption = 0
DateStackOption_Year: DateStackOption = 1
DateStackOption_Month: DateStackOption = 2
FolderDepth = Int32
FolderDepth_Shallow: FolderDepth = 0
FolderDepth_Deep: FolderDepth = 1
class IContentIndexer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexer'
    _iid_ = Guid('{b1767f8d-f698-4982-b05f-3a6e8cab01a2}')
    @winrt_commethod(6)
    def AddAsync(self, indexableContent: Windows.Storage.Search.IIndexableContent) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def UpdateAsync(self, indexableContent: Windows.Storage.Search.IIndexableContent) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAsync(self, contentId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DeleteMultipleAsync(self, contentIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def DeleteAllAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def RetrievePropertiesAsync(self, contentId: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_commethod(12)
    def get_Revision(self) -> UInt64: ...
    Revision = property(get_Revision, None)
class IContentIndexerQuery(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerQuery'
    _iid_ = Guid('{70e3b0f8-4bfc-428a-8889-cc51da9a7b9d}')
    @winrt_commethod(6)
    def GetCountAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def GetPropertiesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_commethod(8)
    def GetPropertiesRangeAsync(self, startIndex: UInt32, maxItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_commethod(9)
    def GetAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_commethod(10)
    def GetRangeAsync(self, startIndex: UInt32, maxItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_commethod(11)
    def get_QueryFolder(self) -> Windows.Storage.StorageFolder: ...
    QueryFolder = property(get_QueryFolder, None)
class IContentIndexerQueryOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerQueryOperations'
    _iid_ = Guid('{28823e10-4786-42f1-9730-792b3566b150}')
    @winrt_commethod(6)
    def CreateQueryWithSortOrderAndLanguage(self, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: Windows.Foundation.Collections.IIterable[Windows.Storage.Search.SortEntry], searchFilterLanguage: WinRT_String) -> Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_commethod(7)
    def CreateQueryWithSortOrder(self, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: Windows.Foundation.Collections.IIterable[Windows.Storage.Search.SortEntry]) -> Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_commethod(8)
    def CreateQuery(self, searchFilter: WinRT_String, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Storage.Search.ContentIndexerQuery: ...
class IContentIndexerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerStatics'
    _iid_ = Guid('{8c488375-b37e-4c60-9ba8-b760fda3e59d}')
    @winrt_commethod(6)
    def GetIndexerWithName(self, indexName: WinRT_String) -> Windows.Storage.Search.ContentIndexer: ...
    @winrt_commethod(7)
    def GetIndexer(self) -> Windows.Storage.Search.ContentIndexer: ...
class IIndexableContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IIndexableContent'
    _iid_ = Guid('{ccf1a05f-d4b5-483a-b06e-e0db1ec420e4}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(9)
    def get_Stream(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(10)
    def put_Stream(self, value: Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(11)
    def get_StreamContentType(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_StreamContentType(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    Properties = property(get_Properties, None)
    Stream = property(get_Stream, put_Stream)
    StreamContentType = property(get_StreamContentType, put_StreamContentType)
class IQueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptions'
    _iid_ = Guid('{1e5e46ee-0f45-4838-a8e9-d0479d446c30}')
    @winrt_commethod(6)
    def get_FileTypeFilter(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_FolderDepth(self) -> Windows.Storage.Search.FolderDepth: ...
    @winrt_commethod(8)
    def put_FolderDepth(self, value: Windows.Storage.Search.FolderDepth) -> Void: ...
    @winrt_commethod(9)
    def get_ApplicationSearchFilter(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ApplicationSearchFilter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_UserSearchFilter(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_UserSearchFilter(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_IndexerOption(self) -> Windows.Storage.Search.IndexerOption: ...
    @winrt_commethod(16)
    def put_IndexerOption(self, value: Windows.Storage.Search.IndexerOption) -> Void: ...
    @winrt_commethod(17)
    def get_SortOrder(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]: ...
    @winrt_commethod(18)
    def get_GroupPropertyName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_DateStackOption(self) -> Windows.Storage.Search.DateStackOption: ...
    @winrt_commethod(20)
    def SaveToString(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def LoadFromString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def SetThumbnailPrefetch(self, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Void: ...
    @winrt_commethod(23)
    def SetPropertyPrefetch(self, options: Windows.Storage.FileProperties.PropertyPrefetchOptions, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    FileTypeFilter = property(get_FileTypeFilter, None)
    FolderDepth = property(get_FolderDepth, put_FolderDepth)
    ApplicationSearchFilter = property(get_ApplicationSearchFilter, put_ApplicationSearchFilter)
    UserSearchFilter = property(get_UserSearchFilter, put_UserSearchFilter)
    Language = property(get_Language, put_Language)
    IndexerOption = property(get_IndexerOption, put_IndexerOption)
    SortOrder = property(get_SortOrder, None)
    GroupPropertyName = property(get_GroupPropertyName, None)
    DateStackOption = property(get_DateStackOption, None)
class IQueryOptionsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptionsFactory'
    _iid_ = Guid('{032e1f8c-a9c1-4e71-8011-0dee9d4811a3}')
    @winrt_commethod(6)
    def CreateCommonFileQuery(self, query: Windows.Storage.Search.CommonFileQuery, fileTypeFilter: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_commethod(7)
    def CreateCommonFolderQuery(self, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Storage.Search.QueryOptions: ...
class IQueryOptionsWithProviderFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptionsWithProviderFilter'
    _iid_ = Guid('{5b9d1026-15c4-44dd-b89a-47a59b7d7c4f}')
    @winrt_commethod(6)
    def get_StorageProviderIdFilter(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    StorageProviderIdFilter = property(get_StorageProviderIdFilter, None)
class IStorageFileQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFileQueryResult'
    _iid_ = Guid('{52fda447-2baa-412c-b29f-d4b1778efa1e}')
    @winrt_commethod(6)
    def GetFilesAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_commethod(7)
    def GetFilesAsyncDefaultStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
class IStorageFileQueryResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFileQueryResult2'
    _iid_ = Guid('{4e5db9dd-7141-46c4-8be3-e9dc9e27275c}')
    @winrt_commethod(6)
    def GetMatchingPropertiesWithRanges(self, file: Windows.Storage.StorageFile) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]]: ...
class IStorageFolderQueryOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFolderQueryOperations'
    _iid_ = Guid('{cb43ccc9-446b-4a4f-be97-757771be5203}')
    @winrt_commethod(6)
    def GetIndexedStateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Search.IndexedState]: ...
    @winrt_commethod(7)
    def CreateFileQueryOverloadDefault(self) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(8)
    def CreateFileQuery(self, query: Windows.Storage.Search.CommonFileQuery) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(9)
    def CreateFileQueryWithOptions(self, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(10)
    def CreateFolderQueryOverloadDefault(self) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(11)
    def CreateFolderQuery(self, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(12)
    def CreateFolderQueryWithOptions(self, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(13)
    def CreateItemQuery(self) -> Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_commethod(14)
    def CreateItemQueryWithOptions(self, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_commethod(15)
    def GetFilesAsync(self, query: Windows.Storage.Search.CommonFileQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_commethod(16)
    def GetFilesAsyncOverloadDefaultStartAndCount(self, query: Windows.Storage.Search.CommonFileQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_commethod(17)
    def GetFoldersAsync(self, query: Windows.Storage.Search.CommonFolderQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(18)
    def GetFoldersAsyncOverloadDefaultStartAndCount(self, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(19)
    def GetItemsAsync(self, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_commethod(20)
    def AreQueryOptionsSupported(self, queryOptions: Windows.Storage.Search.QueryOptions) -> Boolean: ...
    @winrt_commethod(21)
    def IsCommonFolderQuerySupported(self, query: Windows.Storage.Search.CommonFolderQuery) -> Boolean: ...
    @winrt_commethod(22)
    def IsCommonFileQuerySupported(self, query: Windows.Storage.Search.CommonFileQuery) -> Boolean: ...
class IStorageFolderQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFolderQueryResult'
    _iid_ = Guid('{6654c911-7d66-46fa-aecf-e4a4baa93ab8}')
    @winrt_commethod(6)
    def GetFoldersAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(7)
    def GetFoldersAsyncDefaultStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
class IStorageItemQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageItemQueryResult'
    _iid_ = Guid('{e8948079-9d58-47b8-b2b2-41b07f4795f9}')
    @winrt_commethod(6)
    def GetItemsAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_commethod(7)
    def GetItemsAsyncDefaultStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
class IStorageLibraryChangeTrackerTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails'
    _iid_ = Guid('{1dc7a369-b7a3-4df2-9d61-eba85a0343d2}')
    @winrt_commethod(6)
    def get_Folder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_ChangeTracker(self) -> Windows.Storage.StorageLibraryChangeTracker: ...
    Folder = property(get_Folder, None)
    ChangeTracker = property(get_ChangeTracker, None)
class IStorageLibraryContentChangedTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails'
    _iid_ = Guid('{2a371977-abbf-4e1d-8aa5-6385d8884799}')
    @winrt_commethod(6)
    def get_Folder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def CreateModifiedSinceQuery(self, lastQueryTime: Windows.Foundation.DateTime) -> Windows.Storage.Search.StorageItemQueryResult: ...
    Folder = property(get_Folder, None)
class IStorageQueryResultBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageQueryResultBase'
    _iid_ = Guid('{c297d70d-7353-47ab-ba58-8c61425dc54b}')
    @winrt_commethod(6)
    def GetItemCountAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def get_Folder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def add_ContentsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ContentsChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_OptionsChanged(self, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OptionsChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def FindStartIndexAsync(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(13)
    def GetCurrentQueryOptions(self) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_commethod(14)
    def ApplyNewQueryOptions(self, newQueryOptions: Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class IValueAndLanguage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IValueAndLanguage'
    _iid_ = Guid('{b9914881-a1ee-4bc4-92a5-466968e30436}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Language = property(get_Language, put_Language)
    Value = property(get_Value, put_Value)
class IndexableContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IIndexableContent
    _classid_ = 'Windows.Storage.Search.IndexableContent'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.IndexableContent: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.Search.IIndexableContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Storage.Search.IIndexableContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Storage.Search.IIndexableContent) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_Stream(self: Windows.Storage.Search.IIndexableContent) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_Stream(self: Windows.Storage.Search.IIndexableContent, value: Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_StreamContentType(self: Windows.Storage.Search.IIndexableContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreamContentType(self: Windows.Storage.Search.IIndexableContent, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    Properties = property(get_Properties, None)
    Stream = property(get_Stream, put_Stream)
    StreamContentType = property(get_StreamContentType, put_StreamContentType)
IndexedState = Int32
IndexedState_Unknown: IndexedState = 0
IndexedState_NotIndexed: IndexedState = 1
IndexedState_PartiallyIndexed: IndexedState = 2
IndexedState_FullyIndexed: IndexedState = 3
IndexerOption = Int32
IndexerOption_UseIndexerWhenAvailable: IndexerOption = 0
IndexerOption_OnlyUseIndexer: IndexerOption = 1
IndexerOption_DoNotUseIndexer: IndexerOption = 2
IndexerOption_OnlyUseIndexerAndOptimizeForIndexedProperties: IndexerOption = 3
class QueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IQueryOptions
    _classid_ = 'Windows.Storage.Search.QueryOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_factorymethod
    def CreateCommonFileQuery(cls: Windows.Storage.Search.IQueryOptionsFactory, query: Windows.Storage.Search.CommonFileQuery, fileTypeFilter: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_factorymethod
    def CreateCommonFolderQuery(cls: Windows.Storage.Search.IQueryOptionsFactory, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: Windows.Storage.Search.IQueryOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_FolderDepth(self: Windows.Storage.Search.IQueryOptions) -> Windows.Storage.Search.FolderDepth: ...
    @winrt_mixinmethod
    def put_FolderDepth(self: Windows.Storage.Search.IQueryOptions, value: Windows.Storage.Search.FolderDepth) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationSearchFilter(self: Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ApplicationSearchFilter(self: Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserSearchFilter(self: Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserSearchFilter(self: Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IndexerOption(self: Windows.Storage.Search.IQueryOptions) -> Windows.Storage.Search.IndexerOption: ...
    @winrt_mixinmethod
    def put_IndexerOption(self: Windows.Storage.Search.IQueryOptions, value: Windows.Storage.Search.IndexerOption) -> Void: ...
    @winrt_mixinmethod
    def get_SortOrder(self: Windows.Storage.Search.IQueryOptions) -> Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]: ...
    @winrt_mixinmethod
    def get_GroupPropertyName(self: Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateStackOption(self: Windows.Storage.Search.IQueryOptions) -> Windows.Storage.Search.DateStackOption: ...
    @winrt_mixinmethod
    def SaveToString(self: Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def LoadFromString(self: Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetThumbnailPrefetch(self: Windows.Storage.Search.IQueryOptions, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Void: ...
    @winrt_mixinmethod
    def SetPropertyPrefetch(self: Windows.Storage.Search.IQueryOptions, options: Windows.Storage.FileProperties.PropertyPrefetchOptions, propertiesToRetrieve: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_StorageProviderIdFilter(self: Windows.Storage.Search.IQueryOptionsWithProviderFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    FileTypeFilter = property(get_FileTypeFilter, None)
    FolderDepth = property(get_FolderDepth, put_FolderDepth)
    ApplicationSearchFilter = property(get_ApplicationSearchFilter, put_ApplicationSearchFilter)
    UserSearchFilter = property(get_UserSearchFilter, put_UserSearchFilter)
    Language = property(get_Language, put_Language)
    IndexerOption = property(get_IndexerOption, put_IndexerOption)
    SortOrder = property(get_SortOrder, None)
    GroupPropertyName = property(get_GroupPropertyName, None)
    DateStackOption = property(get_DateStackOption, None)
    StorageProviderIdFilter = property(get_StorageProviderIdFilter, None)
class SortEntry(EasyCastStructure):
    PropertyName: WinRT_String
    AscendingOrder: Boolean
class SortEntryVector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]
    _classid_ = 'Windows.Storage.Search.SortEntryVector'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], index: UInt32) -> Windows.Storage.Search.SortEntry: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.Search.SortEntry]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], value: Windows.Storage.Search.SortEntry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], index: UInt32, value: Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], index: UInt32, value: Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], value: Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], startIndex: UInt32, items: POINTER(Windows.Storage.Search.SortEntry_head)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.Storage.Search.SortEntry], items: POINTER(Windows.Storage.Search.SortEntry_head)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Storage.Search.SortEntry]) -> Windows.Foundation.Collections.IIterator[Windows.Storage.Search.SortEntry]: ...
    Size = property(get_Size, None)
class StorageFileQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IStorageFileQueryResult
    _classid_ = 'Windows.Storage.Search.StorageFileQueryResult'
    @winrt_mixinmethod
    def GetFilesAsync(self: Windows.Storage.Search.IStorageFileQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncDefaultStartAndCount(self: Windows.Storage.Search.IStorageFileQueryResult) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: Windows.Storage.Search.IStorageQueryResultBase, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: Windows.Storage.Search.QueryOptions) -> Void: ...
    @winrt_mixinmethod
    def GetMatchingPropertiesWithRanges(self: Windows.Storage.Search.IStorageFileQueryResult2, file: Windows.Storage.StorageFile) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Foundation.Collections.IVectorView[Windows.Data.Text.TextSegment]]: ...
    Folder = property(get_Folder, None)
class StorageFolderQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IStorageFolderQueryResult
    _classid_ = 'Windows.Storage.Search.StorageFolderQueryResult'
    @winrt_mixinmethod
    def GetFoldersAsync(self: Windows.Storage.Search.IStorageFolderQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncDefaultStartAndCount(self: Windows.Storage.Search.IStorageFolderQueryResult) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: Windows.Storage.Search.IStorageQueryResultBase, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class StorageItemQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IStorageItemQueryResult
    _classid_ = 'Windows.Storage.Search.StorageItemQueryResult'
    @winrt_mixinmethod
    def GetItemsAsync(self: Windows.Storage.Search.IStorageItemQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncDefaultStartAndCount(self: Windows.Storage.Search.IStorageItemQueryResult) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Storage.Search.IStorageQueryResultBase, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: Windows.Storage.Search.IStorageQueryResultBase, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: Windows.Storage.Search.IStorageQueryResultBase, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class StorageLibraryChangeTrackerTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails
    _classid_ = 'Windows.Storage.Search.StorageLibraryChangeTrackerTriggerDetails'
    @winrt_mixinmethod
    def get_Folder(self: Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails) -> Windows.Storage.StorageLibraryChangeTracker: ...
    Folder = property(get_Folder, None)
    ChangeTracker = property(get_ChangeTracker, None)
class StorageLibraryContentChangedTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails
    _classid_ = 'Windows.Storage.Search.StorageLibraryContentChangedTriggerDetails'
    @winrt_mixinmethod
    def get_Folder(self: Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def CreateModifiedSinceQuery(self: Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails, lastQueryTime: Windows.Foundation.DateTime) -> Windows.Storage.Search.StorageItemQueryResult: ...
    Folder = property(get_Folder, None)
class ValueAndLanguage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Search.IValueAndLanguage
    _classid_ = 'Windows.Storage.Search.ValueAndLanguage'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.ValueAndLanguage: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.Storage.Search.IValueAndLanguage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.Storage.Search.IValueAndLanguage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Storage.Search.IValueAndLanguage) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Storage.Search.IValueAndLanguage, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Language = property(get_Language, put_Language)
    Value = property(get_Value, put_Value)
make_head(_module, 'ContentIndexer')
make_head(_module, 'ContentIndexerQuery')
make_head(_module, 'IContentIndexer')
make_head(_module, 'IContentIndexerQuery')
make_head(_module, 'IContentIndexerQueryOperations')
make_head(_module, 'IContentIndexerStatics')
make_head(_module, 'IIndexableContent')
make_head(_module, 'IQueryOptions')
make_head(_module, 'IQueryOptionsFactory')
make_head(_module, 'IQueryOptionsWithProviderFilter')
make_head(_module, 'IStorageFileQueryResult')
make_head(_module, 'IStorageFileQueryResult2')
make_head(_module, 'IStorageFolderQueryOperations')
make_head(_module, 'IStorageFolderQueryResult')
make_head(_module, 'IStorageItemQueryResult')
make_head(_module, 'IStorageLibraryChangeTrackerTriggerDetails')
make_head(_module, 'IStorageLibraryContentChangedTriggerDetails')
make_head(_module, 'IStorageQueryResultBase')
make_head(_module, 'IValueAndLanguage')
make_head(_module, 'IndexableContent')
make_head(_module, 'QueryOptions')
make_head(_module, 'SortEntry')
make_head(_module, 'SortEntryVector')
make_head(_module, 'StorageFileQueryResult')
make_head(_module, 'StorageFolderQueryResult')
make_head(_module, 'StorageItemQueryResult')
make_head(_module, 'StorageLibraryChangeTrackerTriggerDetails')
make_head(_module, 'StorageLibraryContentChangedTriggerDetails')
make_head(_module, 'ValueAndLanguage')
