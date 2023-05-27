from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Data.Text
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.FileProperties
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IContentIndexer
    _classid_ = 'Windows.Storage.Search.ContentIndexer'
    @winrt_mixinmethod
    def AddAsync(self: win32more.Windows.Storage.Search.IContentIndexer, indexableContent: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateAsync(self: win32more.Windows.Storage.Search.IContentIndexer, indexableContent: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Storage.Search.IContentIndexer, contentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteMultipleAsync(self: win32more.Windows.Storage.Search.IContentIndexer, contentIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAllAsync(self: win32more.Windows.Storage.Search.IContentIndexer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.Search.IContentIndexer, contentId: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def get_Revision(self: win32more.Windows.Storage.Search.IContentIndexer) -> UInt64: ...
    @winrt_mixinmethod
    def CreateQueryWithSortOrderAndLanguage(self: win32more.Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Search.SortEntry], searchFilterLanguage: WinRT_String) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_mixinmethod
    def CreateQueryWithSortOrder(self: win32more.Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Search.SortEntry]) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_mixinmethod
    def CreateQuery(self: win32more.Windows.Storage.Search.IContentIndexerQueryOperations, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_classmethod
    def GetIndexerWithName(cls: Windows.Storage.Search.IContentIndexerStatics, indexName: WinRT_String) -> win32more.Windows.Storage.Search.ContentIndexer: ...
    @winrt_classmethod
    def GetIndexer(cls: Windows.Storage.Search.IContentIndexerStatics) -> win32more.Windows.Storage.Search.ContentIndexer: ...
    Revision = property(get_Revision, None)
class ContentIndexerQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IContentIndexerQuery
    _classid_ = 'Windows.Storage.Search.ContentIndexerQuery'
    @winrt_mixinmethod
    def GetCountAsync(self: win32more.Windows.Storage.Search.IContentIndexerQuery) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.Storage.Search.IContentIndexerQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_mixinmethod
    def GetPropertiesRangeAsync(self: win32more.Windows.Storage.Search.IContentIndexerQuery, startIndex: UInt32, maxItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_mixinmethod
    def GetAsync(self: win32more.Windows.Storage.Search.IContentIndexerQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_mixinmethod
    def GetRangeAsync(self: win32more.Windows.Storage.Search.IContentIndexerQuery, startIndex: UInt32, maxItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_mixinmethod
    def get_QueryFolder(self: win32more.Windows.Storage.Search.IContentIndexerQuery) -> win32more.Windows.Storage.StorageFolder: ...
    QueryFolder = property(get_QueryFolder, None)
DateStackOption = Int32
DateStackOption_None: DateStackOption = 0
DateStackOption_Year: DateStackOption = 1
DateStackOption_Month: DateStackOption = 2
FolderDepth = Int32
FolderDepth_Shallow: FolderDepth = 0
FolderDepth_Deep: FolderDepth = 1
class IContentIndexer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexer'
    _iid_ = Guid('{b1767f8d-f698-4982-b05f-3a6e8cab01a2}')
    @winrt_commethod(6)
    def AddAsync(self, indexableContent: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def UpdateAsync(self, indexableContent: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAsync(self, contentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DeleteMultipleAsync(self, contentIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def DeleteAllAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def RetrievePropertiesAsync(self, contentId: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_commethod(12)
    def get_Revision(self) -> UInt64: ...
    Revision = property(get_Revision, None)
class IContentIndexerQuery(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerQuery'
    _iid_ = Guid('{70e3b0f8-4bfc-428a-8889-cc51da9a7b9d}')
    @winrt_commethod(6)
    def GetCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def GetPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_commethod(8)
    def GetPropertiesRangeAsync(self, startIndex: UInt32, maxItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]]: ...
    @winrt_commethod(9)
    def GetAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_commethod(10)
    def GetRangeAsync(self, startIndex: UInt32, maxItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Search.IIndexableContent]]: ...
    @winrt_commethod(11)
    def get_QueryFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    QueryFolder = property(get_QueryFolder, None)
class IContentIndexerQueryOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerQueryOperations'
    _iid_ = Guid('{28823e10-4786-42f1-9730-792b3566b150}')
    @winrt_commethod(6)
    def CreateQueryWithSortOrderAndLanguage(self, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Search.SortEntry], searchFilterLanguage: WinRT_String) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_commethod(7)
    def CreateQueryWithSortOrder(self, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], sortOrder: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Search.SortEntry]) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
    @winrt_commethod(8)
    def CreateQuery(self, searchFilter: WinRT_String, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Search.ContentIndexerQuery: ...
class IContentIndexerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IContentIndexerStatics'
    _iid_ = Guid('{8c488375-b37e-4c60-9ba8-b760fda3e59d}')
    @winrt_commethod(6)
    def GetIndexerWithName(self, indexName: WinRT_String) -> win32more.Windows.Storage.Search.ContentIndexer: ...
    @winrt_commethod(7)
    def GetIndexer(self) -> win32more.Windows.Storage.Search.ContentIndexer: ...
class IIndexableContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IIndexableContent'
    _iid_ = Guid('{ccf1a05f-d4b5-483a-b06e-e0db1ec420e4}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(9)
    def get_Stream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(10)
    def put_Stream(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(11)
    def get_StreamContentType(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_StreamContentType(self, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    Properties = property(get_Properties, None)
    Stream = property(get_Stream, put_Stream)
    StreamContentType = property(get_StreamContentType, put_StreamContentType)
class IQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptions'
    _iid_ = Guid('{1e5e46ee-0f45-4838-a8e9-d0479d446c30}')
    @winrt_commethod(6)
    def get_FileTypeFilter(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_FolderDepth(self) -> win32more.Windows.Storage.Search.FolderDepth: ...
    @winrt_commethod(8)
    def put_FolderDepth(self, value: win32more.Windows.Storage.Search.FolderDepth) -> Void: ...
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
    def get_IndexerOption(self) -> win32more.Windows.Storage.Search.IndexerOption: ...
    @winrt_commethod(16)
    def put_IndexerOption(self, value: win32more.Windows.Storage.Search.IndexerOption) -> Void: ...
    @winrt_commethod(17)
    def get_SortOrder(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]: ...
    @winrt_commethod(18)
    def get_GroupPropertyName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_DateStackOption(self) -> win32more.Windows.Storage.Search.DateStackOption: ...
    @winrt_commethod(20)
    def SaveToString(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def LoadFromString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def SetThumbnailPrefetch(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> Void: ...
    @winrt_commethod(23)
    def SetPropertyPrefetch(self, options: win32more.Windows.Storage.FileProperties.PropertyPrefetchOptions, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptionsFactory'
    _iid_ = Guid('{032e1f8c-a9c1-4e71-8011-0dee9d4811a3}')
    @winrt_commethod(6)
    def CreateCommonFileQuery(self, query: win32more.Windows.Storage.Search.CommonFileQuery, fileTypeFilter: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_commethod(7)
    def CreateCommonFolderQuery(self, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Storage.Search.QueryOptions: ...
class IQueryOptionsWithProviderFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IQueryOptionsWithProviderFilter'
    _iid_ = Guid('{5b9d1026-15c4-44dd-b89a-47a59b7d7c4f}')
    @winrt_commethod(6)
    def get_StorageProviderIdFilter(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    StorageProviderIdFilter = property(get_StorageProviderIdFilter, None)
class IStorageFileQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFileQueryResult'
    _iid_ = Guid('{52fda447-2baa-412c-b29f-d4b1778efa1e}')
    @winrt_commethod(6)
    def GetFilesAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_commethod(7)
    def GetFilesAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
class IStorageFileQueryResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFileQueryResult2'
    _iid_ = Guid('{4e5db9dd-7141-46c4-8be3-e9dc9e27275c}')
    @winrt_commethod(6)
    def GetMatchingPropertiesWithRanges(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]]: ...
class IStorageFolderQueryOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFolderQueryOperations'
    _iid_ = Guid('{cb43ccc9-446b-4a4f-be97-757771be5203}')
    @winrt_commethod(6)
    def GetIndexedStateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Search.IndexedState]: ...
    @winrt_commethod(7)
    def CreateFileQueryOverloadDefault(self) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(8)
    def CreateFileQuery(self, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(9)
    def CreateFileQueryWithOptions(self, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_commethod(10)
    def CreateFolderQueryOverloadDefault(self) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(11)
    def CreateFolderQuery(self, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(12)
    def CreateFolderQueryWithOptions(self, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_commethod(13)
    def CreateItemQuery(self) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_commethod(14)
    def CreateItemQueryWithOptions(self, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_commethod(15)
    def GetFilesAsync(self, query: win32more.Windows.Storage.Search.CommonFileQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_commethod(16)
    def GetFilesAsyncOverloadDefaultStartAndCount(self, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_commethod(17)
    def GetFoldersAsync(self, query: win32more.Windows.Storage.Search.CommonFolderQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(18)
    def GetFoldersAsyncOverloadDefaultStartAndCount(self, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(19)
    def GetItemsAsync(self, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_commethod(20)
    def AreQueryOptionsSupported(self, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Boolean: ...
    @winrt_commethod(21)
    def IsCommonFolderQuerySupported(self, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> Boolean: ...
    @winrt_commethod(22)
    def IsCommonFileQuerySupported(self, query: win32more.Windows.Storage.Search.CommonFileQuery) -> Boolean: ...
class IStorageFolderQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageFolderQueryResult'
    _iid_ = Guid('{6654c911-7d66-46fa-aecf-e4a4baa93ab8}')
    @winrt_commethod(6)
    def GetFoldersAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(7)
    def GetFoldersAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
class IStorageItemQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageItemQueryResult'
    _iid_ = Guid('{e8948079-9d58-47b8-b2b2-41b07f4795f9}')
    @winrt_commethod(6)
    def GetItemsAsync(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_commethod(7)
    def GetItemsAsyncDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
class IStorageLibraryChangeTrackerTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails'
    _iid_ = Guid('{1dc7a369-b7a3-4df2-9d61-eba85a0343d2}')
    @winrt_commethod(6)
    def get_Folder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_ChangeTracker(self) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
    Folder = property(get_Folder, None)
    ChangeTracker = property(get_ChangeTracker, None)
class IStorageLibraryContentChangedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails'
    _iid_ = Guid('{2a371977-abbf-4e1d-8aa5-6385d8884799}')
    @winrt_commethod(6)
    def get_Folder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def CreateModifiedSinceQuery(self, lastQueryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    Folder = property(get_Folder, None)
class IStorageQueryResultBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IStorageQueryResultBase'
    _iid_ = Guid('{c297d70d-7353-47ab-ba58-8c61425dc54b}')
    @winrt_commethod(6)
    def GetItemCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def get_Folder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def add_ContentsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ContentsChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_OptionsChanged(self, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OptionsChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def FindStartIndexAsync(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(13)
    def GetCurrentQueryOptions(self) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_commethod(14)
    def ApplyNewQueryOptions(self, newQueryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class IValueAndLanguage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Search.IValueAndLanguage'
    _iid_ = Guid('{b9914881-a1ee-4bc4-92a5-466968e30436}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Language = property(get_Language, put_Language)
    Value = property(get_Value, put_Value)
class IndexableContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IIndexableContent
    _classid_ = 'Windows.Storage.Search.IndexableContent'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.IndexableContent: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.Search.IIndexableContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Storage.Search.IIndexableContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_Stream(self: win32more.Windows.Storage.Search.IIndexableContent) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_Stream(self: win32more.Windows.Storage.Search.IIndexableContent, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_StreamContentType(self: win32more.Windows.Storage.Search.IIndexableContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreamContentType(self: win32more.Windows.Storage.Search.IIndexableContent, value: WinRT_String) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IQueryOptions
    _classid_ = 'Windows.Storage.Search.QueryOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.QueryOptions: ...
    @winrt_factorymethod
    def CreateCommonFileQuery(cls: Windows.Storage.Search.IQueryOptionsFactory, query: win32more.Windows.Storage.Search.CommonFileQuery, fileTypeFilter: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_factorymethod
    def CreateCommonFolderQuery(cls: Windows.Storage.Search.IQueryOptionsFactory, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: win32more.Windows.Storage.Search.IQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_FolderDepth(self: win32more.Windows.Storage.Search.IQueryOptions) -> win32more.Windows.Storage.Search.FolderDepth: ...
    @winrt_mixinmethod
    def put_FolderDepth(self: win32more.Windows.Storage.Search.IQueryOptions, value: win32more.Windows.Storage.Search.FolderDepth) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationSearchFilter(self: win32more.Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ApplicationSearchFilter(self: win32more.Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserSearchFilter(self: win32more.Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserSearchFilter(self: win32more.Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IndexerOption(self: win32more.Windows.Storage.Search.IQueryOptions) -> win32more.Windows.Storage.Search.IndexerOption: ...
    @winrt_mixinmethod
    def put_IndexerOption(self: win32more.Windows.Storage.Search.IQueryOptions, value: win32more.Windows.Storage.Search.IndexerOption) -> Void: ...
    @winrt_mixinmethod
    def get_SortOrder(self: win32more.Windows.Storage.Search.IQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]: ...
    @winrt_mixinmethod
    def get_GroupPropertyName(self: win32more.Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateStackOption(self: win32more.Windows.Storage.Search.IQueryOptions) -> win32more.Windows.Storage.Search.DateStackOption: ...
    @winrt_mixinmethod
    def SaveToString(self: win32more.Windows.Storage.Search.IQueryOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def LoadFromString(self: win32more.Windows.Storage.Search.IQueryOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetThumbnailPrefetch(self: win32more.Windows.Storage.Search.IQueryOptions, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> Void: ...
    @winrt_mixinmethod
    def SetPropertyPrefetch(self: win32more.Windows.Storage.Search.IQueryOptions, options: win32more.Windows.Storage.FileProperties.PropertyPrefetchOptions, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_StorageProviderIdFilter(self: win32more.Windows.Storage.Search.IQueryOptionsWithProviderFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]
    _classid_ = 'Windows.Storage.Search.SortEntryVector'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], index: UInt32) -> win32more.Windows.Storage.Search.SortEntry: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Search.SortEntry]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], value: win32more.Windows.Storage.Search.SortEntry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], index: UInt32, value: win32more.Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], index: UInt32, value: win32more.Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], value: win32more.Windows.Storage.Search.SortEntry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.Storage.Search.SortEntry], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Search.SortEntry], items: Annotated[SZArray[win32more.Windows.Storage.Search.SortEntry], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Search.SortEntry]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Storage.Search.SortEntry]: ...
    Size = property(get_Size, None)
class StorageFileQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IStorageFileQueryResult
    _classid_ = 'Windows.Storage.Search.StorageFileQueryResult'
    @winrt_mixinmethod
    def GetFilesAsync(self: win32more.Windows.Storage.Search.IStorageFileQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFileQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Void: ...
    @winrt_mixinmethod
    def GetMatchingPropertiesWithRanges(self: win32more.Windows.Storage.Search.IStorageFileQueryResult2, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Data.Text.TextSegment]]: ...
    Folder = property(get_Folder, None)
class StorageFolderQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IStorageFolderQueryResult
    _classid_ = 'Windows.Storage.Search.StorageFolderQueryResult'
    @winrt_mixinmethod
    def GetFoldersAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFolderQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class StorageItemQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IStorageItemQueryResult
    _classid_ = 'Windows.Storage.Search.StorageItemQueryResult'
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.Storage.Search.IStorageItemQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageItemQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetItemCountAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Search.IStorageQueryResultBase, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionsChanged(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindStartIndexAsync(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase) -> win32more.Windows.Storage.Search.QueryOptions: ...
    @winrt_mixinmethod
    def ApplyNewQueryOptions(self: win32more.Windows.Storage.Search.IStorageQueryResultBase, newQueryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Void: ...
    Folder = property(get_Folder, None)
class StorageLibraryChangeTrackerTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails
    _classid_ = 'Windows.Storage.Search.StorageLibraryChangeTrackerTriggerDetails'
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.Storage.Search.IStorageLibraryChangeTrackerTriggerDetails) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
    Folder = property(get_Folder, None)
    ChangeTracker = property(get_ChangeTracker, None)
class StorageLibraryContentChangedTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails
    _classid_ = 'Windows.Storage.Search.StorageLibraryContentChangedTriggerDetails'
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def CreateModifiedSinceQuery(self: win32more.Windows.Storage.Search.IStorageLibraryContentChangedTriggerDetails, lastQueryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    Folder = property(get_Folder, None)
class ValueAndLanguage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Search.IValueAndLanguage
    _classid_ = 'Windows.Storage.Search.ValueAndLanguage'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.Search.ValueAndLanguage: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Storage.Search.IValueAndLanguage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Storage.Search.IValueAndLanguage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Storage.Search.IValueAndLanguage) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Storage.Search.IValueAndLanguage, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
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
