from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.Search.AppContentIndex
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
AppContentIndexContract: UInt32 = 65536
class AppContentIndexListener(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppContentIndexListener'
    @winrt_mixinmethod
    def add_IndexCapabilitiesChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IndexCapabilitiesChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IndexStatisticsChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Microsoft.Windows.Search.AppContentIndex.IndexStatistics]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IndexStatisticsChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentItemStatusChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Windows.Foundation.Collections.IMapView[hstr, win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult]]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentItemStatusChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContentItemStatusChanged = event(add_ContentItemStatusChanged, remove_ContentItemStatusChanged)
    IndexCapabilitiesChanged = event(add_IndexCapabilitiesChanged, remove_IndexCapabilitiesChanged)
    IndexStatisticsChanged = event(add_IndexStatisticsChanged, remove_IndexStatisticsChanged)
class AppContentIndexer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppContentIndexer'
    @winrt_mixinmethod
    def get_Listener(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexListener: ...
    @winrt_mixinmethod
    def get_IndexName(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> hstr: ...
    @winrt_mixinmethod
    def GetIndexCapabilities(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities: ...
    @winrt_mixinmethod
    def WaitForIndexCapabilitiesAsync(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities, Double]: ...
    @winrt_mixinmethod
    def get_DefaultLanguage(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> hstr: ...
    @winrt_mixinmethod
    def IsContentKindSupported(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, contentKind: win32more.Microsoft.Windows.Search.AppContentIndex.RegionContentKind) -> Boolean: ...
    @winrt_mixinmethod
    def AddOrUpdate(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, indexableContent: win32more.Microsoft.Windows.Search.AppContentIndex.IndexableAppContent) -> Void: ...
    @winrt_mixinmethod
    def CreateTextQuery(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, queryPhrase: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuery: ...
    @winrt_mixinmethod
    def CreateTextQueryWithOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, queryPhrase: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuery: ...
    @winrt_mixinmethod
    def CreateImageQuery(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, queryPhrase: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuery: ...
    @winrt_mixinmethod
    def CreateImageQueryWithOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, queryPhrase: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuery: ...
    @winrt_mixinmethod
    def CreateTextQuerySession(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuerySession: ...
    @winrt_mixinmethod
    def CreateImageQuerySession(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuerySession: ...
    @winrt_mixinmethod
    def RemoveContentItem(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, contentId: hstr) -> Void: ...
    @winrt_mixinmethod
    def RemoveContentItems(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, contentIds: win32more.Windows.Foundation.Collections.IIterable[hstr]) -> Void: ...
    @winrt_mixinmethod
    def RemoveAllContentItems(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> Void: ...
    @winrt_mixinmethod
    def WaitForIndexingIdleAsync(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetIndexStatistics(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexStatistics: ...
    @winrt_mixinmethod
    def GetContentItemStatus(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, contentId: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult: ...
    @winrt_mixinmethod
    def GetContentItemStatuses(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, contentIds: win32more.Windows.Foundation.Collections.IIterable[hstr]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult]: ...
    @winrt_mixinmethod
    def GetContentItemsRequiringReindexing(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    @winrt_mixinmethod
    def GetContentItems(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    @winrt_mixinmethod
    def GetContentItemsWithFilter(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer, filterFlags: win32more.Microsoft.Windows.Search.AppContentIndex.QueryContentItemsFilterFlags) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetIndexCapabilitiesOfCurrentSystem(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilitiesOfCurrentSystem: ...
    @winrt_classmethod
    def GetOrCreateIndex(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics, indexName: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexResult: ...
    @winrt_classmethod
    def GetOrCreateIndexWithOptions(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics, indexName: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexResult: ...
    @winrt_classmethod
    def DeleteIndex(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics, indexName: hstr, deleteIndexWhileInUseBehavior: win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexWhileInUseBehavior) -> win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexResult: ...
    @winrt_classmethod
    def GetExistingIndexes(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    DefaultLanguage = property(get_DefaultLanguage, None)
    IndexName = property(get_IndexName, None)
    Listener = property(get_Listener, None)
class AppIndexContentRegion(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegion
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion'
    @winrt_mixinmethod
    def get_RegionId(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegion) -> hstr: ...
    @winrt_mixinmethod
    def get_ContentKind(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegion) -> win32more.Microsoft.Windows.Search.AppContentIndex.RegionContentKind: ...
    @winrt_classmethod
    def CreateFromString(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, text: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_classmethod
    def CreateFromString2(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, text: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_classmethod
    def CreateFromTextStream(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_classmethod
    def CreateFromTextStream2(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream, options: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_classmethod
    def CreateFromBitmap(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_classmethod
    def CreateFromImageStream(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics, regionId: hstr, contentByteCount: Int32, imageStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    ContentKind = property(get_ContentKind, None)
    RegionId = property(get_RegionId, None)
class AppIndexImageQuery(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuery
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuery'
    @winrt_mixinmethod
    def get_QueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuery) -> hstr: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuery) -> hstr: ...
    @winrt_mixinmethod
    def GetNextMatches(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuery, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch]: ...
    Language = property(get_Language, None)
    QueryPhrase = property(get_QueryPhrase, None)
class _AppIndexImageQuerySession_Meta_(ComPtr.__class__):
    pass
class AppIndexImageQuerySession(ComPtr, metaclass=_AppIndexImageQuerySession_Meta_):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuerySession'
    @winrt_mixinmethod
    def Start(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession) -> Void: ...
    @winrt_mixinmethod
    def StartWithOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions) -> Void: ...
    @winrt_mixinmethod
    def StartWithOptionsAndQuery(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions, firstQueryPhrase: hstr) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession) -> Void: ...
    @winrt_mixinmethod
    def StopWithChosenMatch(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, chosenMatch: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch) -> Void: ...
    @winrt_mixinmethod
    def UpdateQueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, newQueryPhrase: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredMatchesPerResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession) -> Int32: ...
    @winrt_mixinmethod
    def put_DesiredMatchesPerResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def GetResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession) -> win32more.Microsoft.Windows.Search.AppContentIndex.ImageQuerySessionResult: ...
    @winrt_mixinmethod
    def add_ResultChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuerySession, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def get_MaxMatchesPerResult(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySessionStatics) -> Int32: ...
    DesiredMatchesPerResult = property(get_DesiredMatchesPerResult, put_DesiredMatchesPerResult)
    _AppIndexImageQuerySession_Meta_.MaxMatchesPerResult = property(get_MaxMatchesPerResult, None)
    ResultChanged = event(add_ResultChanged, remove_ResultChanged)
class AppIndexQueryMatch(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexQueryMatch'
    @winrt_mixinmethod
    def get_ContentId(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatch) -> hstr: ...
    @winrt_mixinmethod
    def get_RegionId(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatch) -> hstr: ...
    @winrt_mixinmethod
    def get_ContentKind(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatch) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchContentKind: ...
    ContentId = property(get_ContentId, None)
    ContentKind = property(get_ContentKind, None)
    RegionId = property(get_RegionId, None)
class AppIndexTextQuery(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuery
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuery'
    @winrt_mixinmethod
    def get_QueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuery) -> hstr: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuery) -> hstr: ...
    @winrt_mixinmethod
    def GetNextMatches(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuery, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch]: ...
    Language = property(get_Language, None)
    QueryPhrase = property(get_QueryPhrase, None)
class _AppIndexTextQuerySession_Meta_(ComPtr.__class__):
    pass
class AppIndexTextQuerySession(ComPtr, metaclass=_AppIndexTextQuerySession_Meta_):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuerySession'
    @winrt_mixinmethod
    def Start(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession) -> Void: ...
    @winrt_mixinmethod
    def StartWithOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions) -> Void: ...
    @winrt_mixinmethod
    def StartWithOptionsAndQuery(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions, firstQueryPhrase: hstr) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession) -> Void: ...
    @winrt_mixinmethod
    def StopWithChosenMatch(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, chosenMatch: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch) -> Void: ...
    @winrt_mixinmethod
    def UpdateQueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, newQueryPhrase: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredMatchesPerResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession) -> Int32: ...
    @winrt_mixinmethod
    def put_DesiredMatchesPerResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def GetResult(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextQuerySessionResult: ...
    @winrt_mixinmethod
    def add_ResultChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuerySession, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ResultChanged(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def get_MaxMatchesPerResult(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySessionStatics) -> Int32: ...
    DesiredMatchesPerResult = property(get_DesiredMatchesPerResult, put_DesiredMatchesPerResult)
    _AppIndexTextQuerySession_Meta_.MaxMatchesPerResult = property(get_MaxMatchesPerResult, None)
    ResultChanged = event(add_ResultChanged, remove_ResultChanged)
class AppIndexTextStreamEncoding(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding'
    Utf8 = 0
    Utf16_LE = 1
class AppManagedImageQueryMatch(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedImageQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppManagedImageQueryMatch'
    @winrt_mixinmethod
    def get_RegionOfInterest(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedImageQueryMatch) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    RegionOfInterest = property(get_RegionOfInterest, None)
class AppManagedIndexableAppContent(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.IndexableAppContent
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContent
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent'
    @winrt_mixinmethod
    def get_ContentRegions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContent) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion]: ...
    @winrt_classmethod
    def CreateFromString(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, text: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromStringWithOptions(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, text: hstr, regionOptions: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromTextStream(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromTextStreamWithOptions(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream, regionOptions: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromImageStream(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, contentByteCount: Int32, imageStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromBitmap(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, bitmapContent: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_classmethod
    def CreateFromContentRegions(cls: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics, contentId: hstr, contentRegions: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion]) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    ContentRegions = property(get_ContentRegions, None)
class AppManagedOcrTextQueryMatch(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedOcrTextQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppManagedOcrTextQueryMatch'
    @winrt_mixinmethod
    def get_Fragment(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedOcrTextQueryMatch) -> hstr: ...
    @winrt_mixinmethod
    def get_Subregion(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedOcrTextQueryMatch) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    Fragment = property(get_Fragment, None)
    Subregion = property(get_Subregion, None)
class AppManagedTextQueryMatch(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedTextQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.AppManagedTextQueryMatch'
    @winrt_mixinmethod
    def get_TextOffset(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedTextQueryMatch) -> Int32: ...
    @winrt_mixinmethod
    def get_TextLength(self: win32more.Microsoft.Windows.Search.AppContentIndex.IAppManagedTextQueryMatch) -> Int32: ...
    TextLength = property(get_TextLength, None)
    TextOffset = property(get_TextOffset, None)
class ContentItemErrorDetail(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.ContentItemErrorDetail'
    NoError = 0
    UnknownFailure = 1
    UnknownContentId = 2
    ContentRegionErrors = 3
    IndexCorruption = 4
    InsufficientDiskSpace = 5
class ContentItemReader(ComPtr):
    extends: IInspectable
    implements: Tuple[IterableProtocol[hstr]]
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemReader
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ContentItemReader'
    @winrt_mixinmethod
    def GetNextItems(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemReader, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[hstr]) -> win32more.Windows.Foundation.Collections.IIterator[hstr]: ...
class ContentItemReindexingStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.ContentItemReindexingStatus'
    None_ = 0
    Unspecified = 1
    SemanticModelChanged = 2
    ContentUnavailable = 3
    SchemaChanged = 4
    IndexCorruption = 5
class ContentItemStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.ContentItemStatus'
    NotStarted = 0
    InProgress = 1
    Completed = 2
    CompletedWithSomeErrors = 3
    Error = 4
class ContentItemStatusResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ErrorDetail(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemErrorDetail: ...
    @winrt_mixinmethod
    def get_ReindexingStatus(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReindexingStatus: ...
    ErrorDetail = property(get_ErrorDetail, None)
    ExtendedError = property(get_ExtendedError, None)
    ReindexingStatus = property(get_ReindexingStatus, None)
    Status = property(get_Status, None)
class ContentRegionTextOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IContentRegionTextOptions
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentRegionTextOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IContentRegionTextOptions, value: hstr) -> Void: ...
    Language = property(get_Language, put_Language)
class DeleteIndexResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IDeleteIndexResult
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.DeleteIndexResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.Search.AppContentIndex.IDeleteIndexResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.Search.AppContentIndex.IDeleteIndexResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Microsoft.Windows.Search.AppContentIndex.IDeleteIndexResult) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class DeleteIndexStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.DeleteIndexStatus'
    Success = 0
    IndexNotFound = 1
    Deferred = 2
    UnknownFailure = 100
    IndexInUse = 101
class DeleteIndexWhileInUseBehavior(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.DeleteIndexWhileInUseBehavior'
    FailIfInUse = 0
    DeferIfInUse = 1
class GetOrCreateIndexOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexOptions: ...
    @winrt_mixinmethod
    def get_CreateAlways(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CreateAlways(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultLanguage(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_DefaultLanguage(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_TextLexicalRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_mixinmethod
    def put_TextLexicalRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_mixinmethod
    def get_TextSemanticRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_mixinmethod
    def put_TextSemanticRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_mixinmethod
    def get_ImageOcrRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_mixinmethod
    def put_ImageOcrRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_mixinmethod
    def get_ImageSemanticRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_mixinmethod
    def put_ImageSemanticRequirement(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    CreateAlways = property(get_CreateAlways, put_CreateAlways)
    DefaultLanguage = property(get_DefaultLanguage, put_DefaultLanguage)
    ImageOcrRequirement = property(get_ImageOcrRequirement, put_ImageOcrRequirement)
    ImageSemanticRequirement = property(get_ImageSemanticRequirement, put_ImageSemanticRequirement)
    TextLexicalRequirement = property(get_TextLexicalRequirement, put_TextLexicalRequirement)
    TextSemanticRequirement = property(get_TextSemanticRequirement, put_TextSemanticRequirement)
class GetOrCreateIndexResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Indexer(self: win32more.Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer: ...
    ExtendedError = property(get_ExtendedError, None)
    Indexer = property(get_Indexer, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class GetOrCreateIndexStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexStatus'
    CreatedNew = 0
    OpenedExisting = 1
    UnknownFailure = 100
    InvalidOptions = 101
    IncompatibleWithExistingOptions = 102
    UnsupportedDefaultLanguage = 103
    InvalidIndexName = 104
    DeferredDeletionFailed = 105
    LexicalModelsNotAvailable = 106
    SemanticModelsNotAvailable = 107
    OcrModelsNotAvailable = 108
    IndexIsPendingDeletion = 109
    SemanticTextIndexStoreFailure = 110
    SemanticOcrTextIndexStoreFailure = 111
    SemanticImageIndexStoreFailure = 112
    AppContentIndexerFileLockedError = 113
class IAppContentIndexListener(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppContentIndexListener'
    _iid_ = Guid('{2ee89548-521d-510a-893a-1731c6fad619}')
    @winrt_commethod(6)
    def add_IndexCapabilitiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_IndexCapabilitiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_IndexStatisticsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Microsoft.Windows.Search.AppContentIndex.IndexStatistics]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IndexStatisticsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ContentItemStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer, win32more.Windows.Foundation.Collections.IMapView[hstr, win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult]]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ContentItemStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContentItemStatusChanged = event(add_ContentItemStatusChanged, remove_ContentItemStatusChanged)
    IndexCapabilitiesChanged = event(add_IndexCapabilitiesChanged, remove_IndexCapabilitiesChanged)
    IndexStatisticsChanged = event(add_IndexStatisticsChanged, remove_IndexStatisticsChanged)
class IAppContentIndexer(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppContentIndexer'
    _iid_ = Guid('{f246f681-eae8-503b-8723-b1984c8882b0}')
    @winrt_commethod(6)
    def get_Listener(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexListener: ...
    @winrt_commethod(7)
    def get_IndexName(self) -> hstr: ...
    @winrt_commethod(8)
    def GetIndexCapabilities(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities: ...
    @winrt_commethod(9)
    def WaitForIndexCapabilitiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilities, Double]: ...
    @winrt_commethod(10)
    def get_DefaultLanguage(self) -> hstr: ...
    @winrt_commethod(11)
    def IsContentKindSupported(self, contentKind: win32more.Microsoft.Windows.Search.AppContentIndex.RegionContentKind) -> Boolean: ...
    @winrt_commethod(12)
    def AddOrUpdate(self, indexableContent: win32more.Microsoft.Windows.Search.AppContentIndex.IndexableAppContent) -> Void: ...
    @winrt_commethod(13)
    def CreateTextQuery(self, queryPhrase: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuery: ...
    @winrt_commethod(14)
    def CreateTextQueryWithOptions(self, queryPhrase: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuery: ...
    @winrt_commethod(15)
    def CreateImageQuery(self, queryPhrase: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuery: ...
    @winrt_commethod(16)
    def CreateImageQueryWithOptions(self, queryPhrase: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuery: ...
    @winrt_commethod(17)
    def CreateTextQuerySession(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuerySession: ...
    @winrt_commethod(18)
    def CreateImageQuerySession(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuerySession: ...
    @winrt_commethod(19)
    def RemoveContentItem(self, contentId: hstr) -> Void: ...
    @winrt_commethod(20)
    def RemoveContentItems(self, contentIds: win32more.Windows.Foundation.Collections.IIterable[hstr]) -> Void: ...
    @winrt_commethod(21)
    def RemoveAllContentItems(self) -> Void: ...
    @winrt_commethod(22)
    def WaitForIndexingIdleAsync(self, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(23)
    def GetIndexStatistics(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexStatistics: ...
    @winrt_commethod(24)
    def GetContentItemStatus(self, contentId: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult: ...
    @winrt_commethod(25)
    def GetContentItemStatuses(self, contentIds: win32more.Windows.Foundation.Collections.IIterable[hstr]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatusResult]: ...
    @winrt_commethod(26)
    def GetContentItemsRequiringReindexing(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    @winrt_commethod(27)
    def GetContentItems(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    @winrt_commethod(28)
    def GetContentItemsWithFilter(self, filterFlags: win32more.Microsoft.Windows.Search.AppContentIndex.QueryContentItemsFilterFlags) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReader: ...
    DefaultLanguage = property(get_DefaultLanguage, None)
    IndexName = property(get_IndexName, None)
    Listener = property(get_Listener, None)
class IAppContentIndexerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppContentIndexerStatics'
    _iid_ = Guid('{a95dcaa2-4897-522d-a035-950bcb03e49f}')
    @winrt_commethod(6)
    def GetIndexCapabilitiesOfCurrentSystem(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilitiesOfCurrentSystem: ...
    @winrt_commethod(7)
    def GetOrCreateIndex(self, indexName: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexResult: ...
    @winrt_commethod(8)
    def GetOrCreateIndexWithOptions(self, indexName: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexResult: ...
    @winrt_commethod(9)
    def DeleteIndex(self, indexName: hstr, deleteIndexWhileInUseBehavior: win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexWhileInUseBehavior) -> win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexResult: ...
    @winrt_commethod(10)
    def GetExistingIndexes(self) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
class IAppIndexContentRegion(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegion'
    _iid_ = Guid('{b8f55ac8-35cb-5dec-b89e-39ed81907d23}')
    @winrt_commethod(6)
    def get_RegionId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_ContentKind(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.RegionContentKind: ...
    ContentKind = property(get_ContentKind, None)
    RegionId = property(get_RegionId, None)
class IAppIndexContentRegionStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexContentRegionStatics'
    _iid_ = Guid('{55721f32-c445-52d2-a156-461e95f275b2}')
    @winrt_commethod(6)
    def CreateFromString(self, regionId: hstr, text: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_commethod(7)
    def CreateFromString2(self, regionId: hstr, text: hstr, options: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_commethod(8)
    def CreateFromTextStream(self, regionId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_commethod(9)
    def CreateFromTextStream2(self, regionId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream, options: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_commethod(10)
    def CreateFromBitmap(self, regionId: hstr, image: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
    @winrt_commethod(11)
    def CreateFromImageStream(self, regionId: hstr, contentByteCount: Int32, imageStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion: ...
class IAppIndexImageQuery(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuery'
    _iid_ = Guid('{54642613-c596-5bc2-9d0e-7f542e07906f}')
    @winrt_commethod(6)
    def get_QueryPhrase(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(8)
    def GetNextMatches(self, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch]: ...
    Language = property(get_Language, None)
    QueryPhrase = property(get_QueryPhrase, None)
class IAppIndexImageQuerySession(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySession'
    _iid_ = Guid('{62ebf2f4-035b-55ba-8332-86c618cc0783}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def StartWithOptions(self, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions) -> Void: ...
    @winrt_commethod(8)
    def StartWithOptionsAndQuery(self, options: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions, firstQueryPhrase: hstr) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def StopWithChosenMatch(self, chosenMatch: win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch) -> Void: ...
    @winrt_commethod(11)
    def UpdateQueryPhrase(self, newQueryPhrase: hstr) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredMatchesPerResult(self) -> Int32: ...
    @winrt_commethod(13)
    def put_DesiredMatchesPerResult(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def GetResult(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ImageQuerySessionResult: ...
    @winrt_commethod(15)
    def add_ResultChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexImageQuerySession, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ResultChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredMatchesPerResult = property(get_DesiredMatchesPerResult, put_DesiredMatchesPerResult)
    ResultChanged = event(add_ResultChanged, remove_ResultChanged)
class IAppIndexImageQuerySessionStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexImageQuerySessionStatics'
    _iid_ = Guid('{69c6d023-f4d9-5247-a9af-f6c400e22714}')
    @winrt_commethod(6)
    def get_MaxMatchesPerResult(self) -> Int32: ...
    MaxMatchesPerResult = property(get_MaxMatchesPerResult, None)
class IAppIndexQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatch'
    _iid_ = Guid('{95fef777-eb2b-5b23-bcb6-b3b1908116fa}')
    @winrt_commethod(6)
    def get_ContentId(self) -> hstr: ...
    @winrt_commethod(7)
    def get_RegionId(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ContentKind(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchContentKind: ...
    ContentId = property(get_ContentId, None)
    ContentKind = property(get_ContentKind, None)
    RegionId = property(get_RegionId, None)
class IAppIndexQueryMatchFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexQueryMatchFactory'
    _iid_ = Guid('{1c79da3e-6ff0-503c-8934-6ca4baaf5d4e}')
class IAppIndexTextQuery(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuery'
    _iid_ = Guid('{b1993a02-80d1-5cea-97c8-166a60098154}')
    @winrt_commethod(6)
    def get_QueryPhrase(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(8)
    def GetNextMatches(self, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch]: ...
    Language = property(get_Language, None)
    QueryPhrase = property(get_QueryPhrase, None)
class IAppIndexTextQuerySession(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySession'
    _iid_ = Guid('{260cae8c-a16a-5c7d-b8ed-652087ce12ea}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def StartWithOptions(self, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions) -> Void: ...
    @winrt_commethod(8)
    def StartWithOptionsAndQuery(self, options: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions, firstQueryPhrase: hstr) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def StopWithChosenMatch(self, chosenMatch: win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch) -> Void: ...
    @winrt_commethod(11)
    def UpdateQueryPhrase(self, newQueryPhrase: hstr) -> Void: ...
    @winrt_commethod(12)
    def get_DesiredMatchesPerResult(self) -> Int32: ...
    @winrt_commethod(13)
    def put_DesiredMatchesPerResult(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def GetResult(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextQuerySessionResult: ...
    @winrt_commethod(15)
    def add_ResultChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextQuerySession, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ResultChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredMatchesPerResult = property(get_DesiredMatchesPerResult, put_DesiredMatchesPerResult)
    ResultChanged = event(add_ResultChanged, remove_ResultChanged)
class IAppIndexTextQuerySessionStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppIndexTextQuerySessionStatics'
    _iid_ = Guid('{2cd6ae32-60d7-5642-84eb-3efd535ab3f0}')
    @winrt_commethod(6)
    def get_MaxMatchesPerResult(self) -> Int32: ...
    MaxMatchesPerResult = property(get_MaxMatchesPerResult, None)
class IAppManagedImageQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppManagedImageQueryMatch'
    _iid_ = Guid('{3ae41e0b-8968-5353-ae25-044a8450c41c}')
    @winrt_commethod(6)
    def get_RegionOfInterest(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    RegionOfInterest = property(get_RegionOfInterest, None)
class IAppManagedIndexableAppContent(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContent'
    _iid_ = Guid('{39808fa8-95a5-5dd2-90e4-0159cc2252fa}')
    @winrt_commethod(6)
    def get_ContentRegions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion]: ...
    ContentRegions = property(get_ContentRegions, None)
class IAppManagedIndexableAppContentStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppManagedIndexableAppContentStatics'
    _iid_ = Guid('{0b3a7b96-8849-5467-9b95-0af1f02eb425}')
    @winrt_commethod(6)
    def CreateFromString(self, contentId: hstr, text: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(7)
    def CreateFromStringWithOptions(self, contentId: hstr, text: hstr, regionOptions: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(8)
    def CreateFromTextStream(self, contentId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(9)
    def CreateFromTextStreamWithOptions(self, contentId: hstr, contentByteCount: Int32, encoding: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexTextStreamEncoding, textStream: win32more.Windows.Storage.Streams.IInputStream, regionOptions: win32more.Microsoft.Windows.Search.AppContentIndex.ContentRegionTextOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(10)
    def CreateFromImageStream(self, contentId: hstr, contentByteCount: Int32, imageStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(11)
    def CreateFromBitmap(self, contentId: hstr, bitmapContent: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
    @winrt_commethod(12)
    def CreateFromContentRegions(self, contentId: hstr, contentRegions: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexContentRegion]) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppManagedIndexableAppContent: ...
class IAppManagedOcrTextQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppManagedOcrTextQueryMatch'
    _iid_ = Guid('{ef37c172-6677-5996-a75e-ce7e861a789c}')
    @winrt_commethod(6)
    def get_Fragment(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Subregion(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    Fragment = property(get_Fragment, None)
    Subregion = property(get_Subregion, None)
class IAppManagedTextQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IAppManagedTextQueryMatch'
    _iid_ = Guid('{c88506bb-1116-5719-bad1-611dce064e23}')
    @winrt_commethod(6)
    def get_TextOffset(self) -> Int32: ...
    @winrt_commethod(7)
    def get_TextLength(self) -> Int32: ...
    TextLength = property(get_TextLength, None)
    TextOffset = property(get_TextOffset, None)
class IContentItemReader(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IContentItemReader'
    _iid_ = Guid('{87b04a16-0c70-599a-b8f2-9ff19f9fbdba}')
    @winrt_commethod(6)
    def GetNextItems(self, maxCount: Int32) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
class IContentItemStatusResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IContentItemStatusResult'
    _iid_ = Guid('{3b78c653-ef36-5946-8fbe-a36ed97a509f}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_ErrorDetail(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemErrorDetail: ...
    @winrt_commethod(9)
    def get_ReindexingStatus(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ContentItemReindexingStatus: ...
    ErrorDetail = property(get_ErrorDetail, None)
    ExtendedError = property(get_ExtendedError, None)
    ReindexingStatus = property(get_ReindexingStatus, None)
    Status = property(get_Status, None)
class IContentRegionTextOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IContentRegionTextOptions'
    _iid_ = Guid('{e1c7d7ce-03cd-5dd8-ac18-4ba45d2da578}')
    @winrt_commethod(6)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Language(self, value: hstr) -> Void: ...
    Language = property(get_Language, put_Language)
class IDeleteIndexResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IDeleteIndexResult'
    _iid_ = Guid('{f2af9ca5-03a9-521a-8f41-6a14994664a7}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.DeleteIndexStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class IGetOrCreateIndexOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexOptions'
    _iid_ = Guid('{80b59bef-099a-54a1-a101-e6915b5b6bc1}')
    @winrt_commethod(6)
    def get_CreateAlways(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CreateAlways(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultLanguage(self) -> hstr: ...
    @winrt_commethod(9)
    def put_DefaultLanguage(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_TextLexicalRequirement(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_commethod(11)
    def put_TextLexicalRequirement(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_commethod(12)
    def get_TextSemanticRequirement(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_commethod(13)
    def put_TextSemanticRequirement(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_commethod(14)
    def get_ImageOcrRequirement(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_commethod(15)
    def put_ImageOcrRequirement(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    @winrt_commethod(16)
    def get_ImageSemanticRequirement(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement: ...
    @winrt_commethod(17)
    def put_ImageSemanticRequirement(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement) -> Void: ...
    CreateAlways = property(get_CreateAlways, put_CreateAlways)
    DefaultLanguage = property(get_DefaultLanguage, put_DefaultLanguage)
    ImageOcrRequirement = property(get_ImageOcrRequirement, put_ImageOcrRequirement)
    ImageSemanticRequirement = property(get_ImageSemanticRequirement, put_ImageSemanticRequirement)
    TextLexicalRequirement = property(get_TextLexicalRequirement, put_TextLexicalRequirement)
    TextSemanticRequirement = property(get_TextSemanticRequirement, put_TextSemanticRequirement)
class IGetOrCreateIndexResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IGetOrCreateIndexResult'
    _iid_ = Guid('{ebf3f787-2d85-561a-939b-3ebbaf44cf96}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.GetOrCreateIndexStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Indexer(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.AppContentIndexer: ...
    ExtendedError = property(get_ExtendedError, None)
    Indexer = property(get_Indexer, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class IImageQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IImageQueryMatch'
    _iid_ = Guid('{18e69c41-df0b-5c92-852a-4df5501b63c8}')
class IImageQueryMatchFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IImageQueryMatchFactory'
    _iid_ = Guid('{5eb58ac9-085e-55a4-bbc7-5593f9d9af8c}')
class IImageQueryOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions'
    _iid_ = Guid('{8275e054-8ebf-5e50-abab-9bc7b0ce4912}')
    @winrt_commethod(6)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Language(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_MatchScope(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope: ...
    @winrt_commethod(9)
    def put_MatchScope(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope) -> Void: ...
    Language = property(get_Language, put_Language)
    MatchScope = property(get_MatchScope, put_MatchScope)
class IImageQuerySessionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult'
    _iid_ = Guid('{db6564f0-cb24-5cf6-afba-0d21ce25b8fa}')
    @winrt_commethod(6)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_QueryPhrase(self) -> hstr: ...
    @winrt_commethod(8)
    def get_QueryOptions(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions: ...
    @winrt_commethod(9)
    def get_Matches(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch]: ...
    IsValid = property(get_IsValid, None)
    Matches = property(get_Matches, None)
    QueryOptions = property(get_QueryOptions, None)
    QueryPhrase = property(get_QueryPhrase, None)
class IIndexCapabilities(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexCapabilities'
    _iid_ = Guid('{e3eb1595-3b80-5183-8eaa-2aa606e6b290}')
    @winrt_commethod(6)
    def get_HasCapabilitiesWithErrors(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetCapabilityState(self, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityState: ...
    @winrt_commethod(8)
    def GetCapabilitiesWithErrors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability]: ...
    HasCapabilitiesWithErrors = property(get_HasCapabilitiesWithErrors, None)
class IIndexCapabilitiesOfCurrentSystem(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexCapabilitiesOfCurrentSystem'
    _iid_ = Guid('{92274a42-221c-57a0-ace1-711a56e16af0}')
    @winrt_commethod(6)
    def GetIndexCapabilityStatus(self, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityOfCurrentSystemStatus: ...
    @winrt_commethod(7)
    def GetLanguageStatusForIndexCapability(self, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability, language: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityLanguageStatus: ...
class IIndexCapabilityState(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState'
    _iid_ = Guid('{c00c4dbd-e259-5930-bb4f-f1d8a8e8f7cb}')
    @winrt_commethod(6)
    def get_Capability(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability: ...
    @winrt_commethod(7)
    def get_InitializationStatus(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityInitializationStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_ErrorMessage(self) -> hstr: ...
    Capability = property(get_Capability, None)
    ErrorMessage = property(get_ErrorMessage, None)
    ExtendedError = property(get_ExtendedError, None)
    InitializationStatus = property(get_InitializationStatus, None)
class IIndexStatistics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexStatistics'
    _iid_ = Guid('{16475c25-15a2-5e56-bd81-f7abae16993d}')
    @winrt_commethod(6)
    def get_IndexingInProgress(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ItemCount(self) -> Int32: ...
    @winrt_commethod(8)
    def get_CompletedCount(self) -> Int32: ...
    @winrt_commethod(9)
    def get_NotStartedCount(self) -> Int32: ...
    @winrt_commethod(10)
    def get_InProgressCount(self) -> Int32: ...
    @winrt_commethod(11)
    def get_ErrorsCount(self) -> Int32: ...
    @winrt_commethod(12)
    def get_PendingDeletionCount(self) -> Int32: ...
    @winrt_commethod(13)
    def get_RequiringReindexingCount(self) -> Int32: ...
    CompletedCount = property(get_CompletedCount, None)
    ErrorsCount = property(get_ErrorsCount, None)
    InProgressCount = property(get_InProgressCount, None)
    IndexingInProgress = property(get_IndexingInProgress, None)
    ItemCount = property(get_ItemCount, None)
    NotStartedCount = property(get_NotStartedCount, None)
    PendingDeletionCount = property(get_PendingDeletionCount, None)
    RequiringReindexingCount = property(get_RequiringReindexingCount, None)
class IIndexableAppContent(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexableAppContent'
    _iid_ = Guid('{8f8751ce-58a2-569c-a2d5-af9a795a005a}')
    @winrt_commethod(6)
    def get_ContentId(self) -> hstr: ...
    ContentId = property(get_ContentId, None)
class IIndexableAppContentFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IIndexableAppContentFactory'
    _iid_ = Guid('{44fbfe73-232c-593a-9f1b-3e5008ee9bef}')
class ITextQueryMatch(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ITextQueryMatch'
    _iid_ = Guid('{ab1db800-01d1-595f-af66-7a63746610cb}')
class ITextQueryMatchFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ITextQueryMatchFactory'
    _iid_ = Guid('{a2f24864-5094-5606-af67-96aee5564f8b}')
class ITextQueryOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions'
    _iid_ = Guid('{33641046-ee24-5ae1-9999-4f58dca7c1c2}')
    @winrt_commethod(6)
    def get_SuppressSemanticMatches(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SuppressSemanticMatches(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> hstr: ...
    @winrt_commethod(9)
    def put_Language(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_MatchScope(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope: ...
    @winrt_commethod(11)
    def put_MatchScope(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope) -> Void: ...
    @winrt_commethod(12)
    def get_TextMatchType(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextLexicalMatchType: ...
    @winrt_commethod(13)
    def put_TextMatchType(self, value: win32more.Microsoft.Windows.Search.AppContentIndex.TextLexicalMatchType) -> Void: ...
    Language = property(get_Language, put_Language)
    MatchScope = property(get_MatchScope, put_MatchScope)
    SuppressSemanticMatches = property(get_SuppressSemanticMatches, put_SuppressSemanticMatches)
    TextMatchType = property(get_TextMatchType, put_TextMatchType)
class ITextQuerySessionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult'
    _iid_ = Guid('{72b9da3b-b5a8-544e-880f-10998e8c0568}')
    @winrt_commethod(6)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_QueryPhrase(self) -> hstr: ...
    @winrt_commethod(8)
    def get_QueryOptions(self) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions: ...
    @winrt_commethod(9)
    def get_Matches(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch]: ...
    IsValid = property(get_IsValid, None)
    Matches = property(get_Matches, None)
    QueryOptions = property(get_QueryOptions, None)
    QueryPhrase = property(get_QueryPhrase, None)
class ImageQueryMatch(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexQueryMatch
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch'
class ImageQueryOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_MatchScope(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope: ...
    @winrt_mixinmethod
    def put_MatchScope(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQueryOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope) -> Void: ...
    Language = property(get_Language, put_Language)
    MatchScope = property(get_MatchScope, put_MatchScope)
class ImageQuerySessionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.ImageQuerySessionResult'
    @winrt_mixinmethod
    def get_IsValid(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_QueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult) -> hstr: ...
    @winrt_mixinmethod
    def get_QueryOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryOptions: ...
    @winrt_mixinmethod
    def get_Matches(self: win32more.Microsoft.Windows.Search.AppContentIndex.IImageQuerySessionResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.ImageQueryMatch]: ...
    IsValid = property(get_IsValid, None)
    Matches = property(get_Matches, None)
    QueryOptions = property(get_QueryOptions, None)
    QueryPhrase = property(get_QueryPhrase, None)
class IndexCapabilities(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilities
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilities'
    @winrt_mixinmethod
    def get_HasCapabilitiesWithErrors(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def GetCapabilityState(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilities, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityState: ...
    @winrt_mixinmethod
    def GetCapabilitiesWithErrors(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilities) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability]: ...
    HasCapabilitiesWithErrors = property(get_HasCapabilitiesWithErrors, None)
class IndexCapabilitiesOfCurrentSystem(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilitiesOfCurrentSystem
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilitiesOfCurrentSystem'
    @winrt_mixinmethod
    def GetIndexCapabilityStatus(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilitiesOfCurrentSystem, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityOfCurrentSystemStatus: ...
    @winrt_mixinmethod
    def GetLanguageStatusForIndexCapability(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilitiesOfCurrentSystem, capability: win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability, language: hstr) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityLanguageStatus: ...
class IndexCapability(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapability'
    TextLexical = 0
    TextSemantic = 1
    ImageOcr = 2
    ImageSemantic = 3
class IndexCapabilityInitializationStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilityInitializationStatus'
    Unknown = 0
    Initialized = 1
    Initializing = 2
    Suppressed = 3
    NotSupported = 4
    DisabledByPolicy = 5
    InitializationError = 100
class IndexCapabilityLanguageStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilityLanguageStatus'
    Supported = 0
    Partial = 1
    NotSupported = 2
class IndexCapabilityOfCurrentSystemStatus(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilityOfCurrentSystemStatus'
    Ready = 0
    NotReady = 1
    DisabledByPolicy = 2
    NotSupported = 3
class IndexCapabilityRequirement(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilityRequirement'
    Default = 0
    Suppressed = 1
    Required = 2
class IndexCapabilityState(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IndexCapabilityState'
    @winrt_mixinmethod
    def get_Capability(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapability: ...
    @winrt_mixinmethod
    def get_InitializationStatus(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState) -> win32more.Microsoft.Windows.Search.AppContentIndex.IndexCapabilityInitializationStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ErrorMessage(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexCapabilityState) -> hstr: ...
    Capability = property(get_Capability, None)
    ErrorMessage = property(get_ErrorMessage, None)
    ExtendedError = property(get_ExtendedError, None)
    InitializationStatus = property(get_InitializationStatus, None)
class IndexStatistics(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IndexStatistics'
    @winrt_mixinmethod
    def get_IndexingInProgress(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Boolean: ...
    @winrt_mixinmethod
    def get_ItemCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_CompletedCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_NotStartedCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_InProgressCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_ErrorsCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_PendingDeletionCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    @winrt_mixinmethod
    def get_RequiringReindexingCount(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexStatistics) -> Int32: ...
    CompletedCount = property(get_CompletedCount, None)
    ErrorsCount = property(get_ErrorsCount, None)
    InProgressCount = property(get_InProgressCount, None)
    IndexingInProgress = property(get_IndexingInProgress, None)
    ItemCount = property(get_ItemCount, None)
    NotStartedCount = property(get_NotStartedCount, None)
    PendingDeletionCount = property(get_PendingDeletionCount, None)
    RequiringReindexingCount = property(get_RequiringReindexingCount, None)
class IndexableAppContent(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexableAppContent
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.IndexableAppContent'
    @winrt_mixinmethod
    def get_ContentId(self: win32more.Microsoft.Windows.Search.AppContentIndex.IIndexableAppContent) -> hstr: ...
    ContentId = property(get_ContentId, None)
class QueryContentItemsFilterFlags(Enum, UInt32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.QueryContentItemsFilterFlags'
    NotStarted = 1
    InProgress = 2
    Completed = 4
    WithErrors = 8
    PendingDeletion = 16
    RequiringReindexing = 32
class QueryMatchContentKind(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.QueryMatchContentKind'
    AppManagedText = 0
    AppManagedImage = 1
    AppManagedOcrText = 2
class QueryMatchScope(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.QueryMatchScope'
    Unconstrained = 0
    Region = 1
    ContentItem = 2
class RegionContentKind(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.RegionContentKind'
    Text = 0
    Image = 1
class TextLexicalMatchType(Enum, Int32):
    _name_ = 'Microsoft.Windows.Search.AppContentIndex.TextLexicalMatchType'
    Fuzzy = 0
    Exact = 1
class TextQueryMatch(ComPtr):
    extends: win32more.Microsoft.Windows.Search.AppContentIndex.AppIndexQueryMatch
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryMatch
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.TextQueryMatch'
class TextQueryOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.TextQueryOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions: ...
    @winrt_mixinmethod
    def get_SuppressSemanticMatches(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressSemanticMatches(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions) -> hstr: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_MatchScope(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope: ...
    @winrt_mixinmethod
    def put_MatchScope(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.QueryMatchScope) -> Void: ...
    @winrt_mixinmethod
    def get_TextMatchType(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextLexicalMatchType: ...
    @winrt_mixinmethod
    def put_TextMatchType(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQueryOptions, value: win32more.Microsoft.Windows.Search.AppContentIndex.TextLexicalMatchType) -> Void: ...
    Language = property(get_Language, put_Language)
    MatchScope = property(get_MatchScope, put_MatchScope)
    SuppressSemanticMatches = property(get_SuppressSemanticMatches, put_SuppressSemanticMatches)
    TextMatchType = property(get_TextMatchType, put_TextMatchType)
class TextQuerySessionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult
    _classid_ = 'Microsoft.Windows.Search.AppContentIndex.TextQuerySessionResult'
    @winrt_mixinmethod
    def get_IsValid(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_QueryPhrase(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult) -> hstr: ...
    @winrt_mixinmethod
    def get_QueryOptions(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult) -> win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryOptions: ...
    @winrt_mixinmethod
    def get_Matches(self: win32more.Microsoft.Windows.Search.AppContentIndex.ITextQuerySessionResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Search.AppContentIndex.TextQueryMatch]: ...
    IsValid = property(get_IsValid, None)
    Matches = property(get_Matches, None)
    QueryOptions = property(get_QueryOptions, None)
    QueryPhrase = property(get_QueryPhrase, None)


make_ready(__name__)
