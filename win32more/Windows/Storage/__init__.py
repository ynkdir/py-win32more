from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.FileProperties
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AppDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IAppDataPaths
    _classid_ = 'Windows.Storage.AppDataPaths'
    @winrt_mixinmethod
    def get_Cookies(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Desktop(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Documents(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Favorites(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_History(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InternetCache(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppData(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProgramData(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingAppData(self: win32more.Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Storage.IAppDataPathsStatics, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AppDataPaths: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Storage.IAppDataPathsStatics) -> win32more.Windows.Storage.AppDataPaths: ...
    Cookies = property(get_Cookies, None)
    Desktop = property(get_Desktop, None)
    Documents = property(get_Documents, None)
    Favorites = property(get_Favorites, None)
    History = property(get_History, None)
    InternetCache = property(get_InternetCache, None)
    LocalAppData = property(get_LocalAppData, None)
    ProgramData = property(get_ProgramData, None)
    RoamingAppData = property(get_RoamingAppData, None)
class _ApplicationData_Meta_(ComPtr.__class__):
    pass
class ApplicationData(ComPtr, metaclass=_ApplicationData_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.IApplicationData
    _classid_ = 'Windows.Storage.ApplicationData'
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Storage.IApplicationData) -> UInt32: ...
    @winrt_mixinmethod
    def SetVersionAsync(self: win32more.Windows.Storage.IApplicationData, desiredVersion: UInt32, handler: win32more.Windows.Storage.ApplicationDataSetVersionHandler) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearAllAsync(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearAsync(self: win32more.Windows.Storage.IApplicationData, locality: win32more.Windows.Storage.ApplicationDataLocality) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_LocalSettings(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def get_RoamingSettings(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def get_LocalFolder(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_RoamingFolder(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_TemporaryFolder(self: win32more.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_DataChanged(self: win32more.Windows.Storage.IApplicationData, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.ApplicationData, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataChanged(self: win32more.Windows.Storage.IApplicationData, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SignalDataChanged(self: win32more.Windows.Storage.IApplicationData) -> Void: ...
    @winrt_mixinmethod
    def get_RoamingStorageQuota(self: win32more.Windows.Storage.IApplicationData) -> UInt64: ...
    @winrt_mixinmethod
    def get_LocalCacheFolder(self: win32more.Windows.Storage.IApplicationData2) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def GetPublisherCacheFolder(self: win32more.Windows.Storage.IApplicationData3, folderName: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def ClearPublisherCacheFolderAsync(self: win32more.Windows.Storage.IApplicationData3, folderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_SharedLocalFolder(self: win32more.Windows.Storage.IApplicationData3) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetForUserAsync(cls: win32more.Windows.Storage.IApplicationDataStatics2, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.ApplicationData]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Storage.IApplicationDataStatics) -> win32more.Windows.Storage.ApplicationData: ...
    LocalCacheFolder = property(get_LocalCacheFolder, None)
    LocalFolder = property(get_LocalFolder, None)
    LocalSettings = property(get_LocalSettings, None)
    RoamingFolder = property(get_RoamingFolder, None)
    RoamingSettings = property(get_RoamingSettings, None)
    RoamingStorageQuota = property(get_RoamingStorageQuota, None)
    SharedLocalFolder = property(get_SharedLocalFolder, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    Version = property(get_Version, None)
    _ApplicationData_Meta_.Current = property(get_Current, None)
    DataChanged = event()
class ApplicationDataCompositeValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Storage.ApplicationDataCompositeValue'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.ApplicationDataCompositeValue.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.ApplicationDataCompositeValue: ...
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
    MapChanged = event()
class ApplicationDataContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.IApplicationDataContainer
    _classid_ = 'Windows.Storage.ApplicationDataContainer'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Storage.IApplicationDataContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Locality(self: win32more.Windows.Storage.IApplicationDataContainer) -> win32more.Windows.Storage.ApplicationDataLocality: ...
    @winrt_mixinmethod
    def get_Values(self: win32more.Windows.Storage.IApplicationDataContainer) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_Containers(self: win32more.Windows.Storage.IApplicationDataContainer) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.ApplicationDataContainer]: ...
    @winrt_mixinmethod
    def CreateContainer(self: win32more.Windows.Storage.IApplicationDataContainer, name: WinRT_String, disposition: win32more.Windows.Storage.ApplicationDataCreateDisposition) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def DeleteContainer(self: win32more.Windows.Storage.IApplicationDataContainer, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Containers = property(get_Containers, None)
    Locality = property(get_Locality, None)
    Name = property(get_Name, None)
    Values = property(get_Values, None)
class ApplicationDataContainerSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Storage.ApplicationDataContainerSettings'
    @winrt_mixinmethod
    def add_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], vhnd: win32more.Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: win32more.Windows.Foundation.Collections.IObservableMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
    MapChanged = event()
class ApplicationDataCreateDisposition(Enum, Int32):
    Always = 0
    Existing = 1
class ApplicationDataLocality(Enum, Int32):
    Local = 0
    Roaming = 1
    Temporary = 2
    LocalCache = 3
    SharedLocal = 4
class ApplicationDataSetVersionHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a05791e6-cc9f-4687-acab-a364fd785463}')
    @winrt_commethod(3)
    def Invoke(self, setVersionRequest: win32more.Windows.Storage.SetVersionRequest) -> Void: ...
class CachedFileManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.CachedFileManager'
    @winrt_classmethod
    def DeferUpdates(cls: win32more.Windows.Storage.ICachedFileManagerStatics, file: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_classmethod
    def CompleteUpdatesAsync(cls: win32more.Windows.Storage.ICachedFileManagerStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Provider.FileUpdateStatus]: ...
class CreationCollisionOption(Enum, Int32):
    GenerateUniqueName = 0
    ReplaceExisting = 1
    FailIfExists = 2
    OpenIfExists = 3
class DownloadsFolder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.DownloadsFolder'
    @winrt_classmethod
    def CreateFileForUserAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics2, user: win32more.Windows.System.User, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderForUserAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics2, user: win32more.Windows.System.User, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileForUserWithCollisionOptionAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics2, user: win32more.Windows.System.User, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderForUserWithCollisionOptionAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics2, user: win32more.Windows.System.User, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileWithCollisionOptionAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderWithCollisionOptionAsync(cls: win32more.Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class FileAccessMode(Enum, Int32):
    Read = 0
    ReadWrite = 1
class FileAttributes(Enum, UInt32):
    Normal = 0
    ReadOnly = 1
    Directory = 16
    Archive = 32
    Temporary = 256
    LocallyIncomplete = 512
class FileIO(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileIO'
    @winrt_classmethod
    def ReadTextAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReadTextWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def WriteTextAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteTextWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadLinesAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def ReadLinesWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def WriteLinesAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteLinesWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesWithEncodingAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadBufferAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def WriteBufferAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteBytesAsync(cls: win32more.Windows.Storage.IFileIOStatics, file: win32more.Windows.Storage.IStorageFile, buffer: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IAppDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IAppDataPaths'
    _iid_ = Guid('{7301d60a-79a2-48c9-9ec0-3fda092f79e1}')
    @winrt_commethod(6)
    def get_Cookies(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Desktop(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Documents(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Favorites(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_History(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_InternetCache(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_LocalAppData(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_ProgramData(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_RoamingAppData(self) -> WinRT_String: ...
    Cookies = property(get_Cookies, None)
    Desktop = property(get_Desktop, None)
    Documents = property(get_Documents, None)
    Favorites = property(get_Favorites, None)
    History = property(get_History, None)
    InternetCache = property(get_InternetCache, None)
    LocalAppData = property(get_LocalAppData, None)
    ProgramData = property(get_ProgramData, None)
    RoamingAppData = property(get_RoamingAppData, None)
class IAppDataPathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IAppDataPathsStatics'
    _iid_ = Guid('{d8eb2afe-a9d9-4b14-b999-e3921379d903}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.AppDataPaths: ...
    @winrt_commethod(7)
    def GetDefault(self) -> win32more.Windows.Storage.AppDataPaths: ...
class IApplicationData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData'
    _iid_ = Guid('{c3da6fb7-b744-4b45-b0b8-223a0938d0dc}')
    @winrt_commethod(6)
    def get_Version(self) -> UInt32: ...
    @winrt_commethod(7)
    def SetVersionAsync(self, desiredVersion: UInt32, handler: win32more.Windows.Storage.ApplicationDataSetVersionHandler) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ClearAllAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearAsync(self, locality: win32more.Windows.Storage.ApplicationDataLocality) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_LocalSettings(self) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(11)
    def get_RoamingSettings(self) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(12)
    def get_LocalFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(13)
    def get_RoamingFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(14)
    def get_TemporaryFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(15)
    def add_DataChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.ApplicationData, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DataChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def SignalDataChanged(self) -> Void: ...
    @winrt_commethod(18)
    def get_RoamingStorageQuota(self) -> UInt64: ...
    LocalFolder = property(get_LocalFolder, None)
    LocalSettings = property(get_LocalSettings, None)
    RoamingFolder = property(get_RoamingFolder, None)
    RoamingSettings = property(get_RoamingSettings, None)
    RoamingStorageQuota = property(get_RoamingStorageQuota, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    Version = property(get_Version, None)
    DataChanged = event()
class IApplicationData2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData2'
    _iid_ = Guid('{9e65cd69-0ba3-4e32-be29-b02de6607638}')
    @winrt_commethod(6)
    def get_LocalCacheFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    LocalCacheFolder = property(get_LocalCacheFolder, None)
class IApplicationData3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData3'
    _iid_ = Guid('{dc222cf4-2772-4c1d-aa2c-c9f743ade8d1}')
    @winrt_commethod(6)
    def GetPublisherCacheFolder(self, folderName: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def ClearPublisherCacheFolderAsync(self, folderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_SharedLocalFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    SharedLocalFolder = property(get_SharedLocalFolder, None)
class IApplicationDataContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataContainer'
    _iid_ = Guid('{c5aefd1e-f467-40ba-8566-ab640a441e1d}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Locality(self) -> win32more.Windows.Storage.ApplicationDataLocality: ...
    @winrt_commethod(8)
    def get_Values(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def get_Containers(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.ApplicationDataContainer]: ...
    @winrt_commethod(10)
    def CreateContainer(self, name: WinRT_String, disposition: win32more.Windows.Storage.ApplicationDataCreateDisposition) -> win32more.Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(11)
    def DeleteContainer(self, name: WinRT_String) -> Void: ...
    Containers = property(get_Containers, None)
    Locality = property(get_Locality, None)
    Name = property(get_Name, None)
    Values = property(get_Values, None)
class IApplicationDataStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataStatics'
    _iid_ = Guid('{5612147b-e843-45e3-94d8-06169e3c8e17}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Storage.ApplicationData: ...
    Current = property(get_Current, None)
class IApplicationDataStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataStatics2'
    _iid_ = Guid('{cd606211-cf49-40a4-a47c-c7f0dbba8107}')
    @winrt_commethod(6)
    def GetForUserAsync(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.ApplicationData]: ...
class ICachedFileManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ICachedFileManagerStatics'
    _iid_ = Guid('{8ffc224a-e782-495d-b614-654c4f0b2370}')
    @winrt_commethod(6)
    def DeferUpdates(self, file: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(7)
    def CompleteUpdatesAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Provider.FileUpdateStatus]: ...
class IDownloadsFolderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IDownloadsFolderStatics'
    _iid_ = Guid('{27862ed0-404e-47df-a1e2-e37308be7b37}')
    @winrt_commethod(6)
    def CreateFileAsync(self, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFolderAsync(self, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(8)
    def CreateFileWithCollisionOptionAsync(self, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def CreateFolderWithCollisionOptionAsync(self, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IDownloadsFolderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IDownloadsFolderStatics2'
    _iid_ = Guid('{e93045bd-8ef8-4f8e-8d15-ac0e265f390d}')
    @winrt_commethod(6)
    def CreateFileForUserAsync(self, user: win32more.Windows.System.User, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFolderForUserAsync(self, user: win32more.Windows.System.User, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(8)
    def CreateFileForUserWithCollisionOptionAsync(self, user: win32more.Windows.System.User, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def CreateFolderForUserWithCollisionOptionAsync(self, user: win32more.Windows.System.User, desiredName: WinRT_String, option: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IFileIOStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IFileIOStatics'
    _iid_ = Guid('{887411eb-7f54-4732-a5f0-5e43e3b8c2f5}')
    @winrt_commethod(6)
    def ReadTextAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def ReadTextWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def WriteTextAsync(self, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def WriteTextWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def AppendTextAsync(self, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def AppendTextWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReadLinesAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(13)
    def ReadLinesWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(14)
    def WriteLinesAsync(self, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def WriteLinesWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def AppendLinesAsync(self, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AppendLinesWithEncodingAsync(self, file: win32more.Windows.Storage.IStorageFile, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReadBufferAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(19)
    def WriteBufferAsync(self, file: win32more.Windows.Storage.IStorageFile, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def WriteBytesAsync(self, file: win32more.Windows.Storage.IStorageFile, buffer: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IKnownFoldersCameraRollStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersCameraRollStatics'
    _iid_ = Guid('{5d115e66-27e8-492f-b8e5-2f90896cd4cd}')
    @winrt_commethod(6)
    def get_CameraRoll(self) -> win32more.Windows.Storage.StorageFolder: ...
    CameraRoll = property(get_CameraRoll, None)
class IKnownFoldersPlaylistsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersPlaylistsStatics'
    _iid_ = Guid('{dad5ecd6-306f-4d6a-b496-46ba8eb106ce}')
    @winrt_commethod(6)
    def get_Playlists(self) -> win32more.Windows.Storage.StorageFolder: ...
    Playlists = property(get_Playlists, None)
class IKnownFoldersSavedPicturesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersSavedPicturesStatics'
    _iid_ = Guid('{055c93ea-253d-467c-b6ca-a97da1e9a18d}')
    @winrt_commethod(6)
    def get_SavedPictures(self) -> win32more.Windows.Storage.StorageFolder: ...
    SavedPictures = property(get_SavedPictures, None)
class IKnownFoldersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics'
    _iid_ = Guid('{5a2a7520-4802-452d-9ad9-4351ada7ec35}')
    @winrt_commethod(6)
    def get_MusicLibrary(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_PicturesLibrary(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_VideosLibrary(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(9)
    def get_DocumentsLibrary(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(10)
    def get_HomeGroup(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(11)
    def get_RemovableDevices(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(12)
    def get_MediaServerDevices(self) -> win32more.Windows.Storage.StorageFolder: ...
    DocumentsLibrary = property(get_DocumentsLibrary, None)
    HomeGroup = property(get_HomeGroup, None)
    MediaServerDevices = property(get_MediaServerDevices, None)
    MusicLibrary = property(get_MusicLibrary, None)
    PicturesLibrary = property(get_PicturesLibrary, None)
    RemovableDevices = property(get_RemovableDevices, None)
    VideosLibrary = property(get_VideosLibrary, None)
class IKnownFoldersStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics2'
    _iid_ = Guid('{194bd0cd-cf6e-4d07-9d53-e9163a2536e9}')
    @winrt_commethod(6)
    def get_Objects3D(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_AppCaptures(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_RecordedCalls(self) -> win32more.Windows.Storage.StorageFolder: ...
    AppCaptures = property(get_AppCaptures, None)
    Objects3D = property(get_Objects3D, None)
    RecordedCalls = property(get_RecordedCalls, None)
class IKnownFoldersStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics3'
    _iid_ = Guid('{c5194341-9742-4ed5-823d-fc1401148764}')
    @winrt_commethod(6)
    def GetFolderForUserAsync(self, user: win32more.Windows.System.User, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IKnownFoldersStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics4'
    _iid_ = Guid('{1722e6bf-9ff9-4b21-bed5-90ecb13a192e}')
    @winrt_commethod(6)
    def RequestAccessAsync(self, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_commethod(7)
    def RequestAccessForUserAsync(self, user: win32more.Windows.System.User, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_commethod(8)
    def GetFolderAsync(self, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IPathIOStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IPathIOStatics'
    _iid_ = Guid('{0f2f3758-8ec7-4381-922b-8f6c07d288f3}')
    @winrt_commethod(6)
    def ReadTextAsync(self, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def ReadTextWithEncodingAsync(self, absolutePath: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def WriteTextAsync(self, absolutePath: WinRT_String, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def WriteTextWithEncodingAsync(self, absolutePath: WinRT_String, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def AppendTextAsync(self, absolutePath: WinRT_String, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def AppendTextWithEncodingAsync(self, absolutePath: WinRT_String, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReadLinesAsync(self, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(13)
    def ReadLinesWithEncodingAsync(self, absolutePath: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(14)
    def WriteLinesAsync(self, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def WriteLinesWithEncodingAsync(self, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def AppendLinesAsync(self, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AppendLinesWithEncodingAsync(self, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReadBufferAsync(self, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(19)
    def WriteBufferAsync(self, absolutePath: WinRT_String, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def WriteBytesAsync(self, absolutePath: WinRT_String, buffer: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncAction: ...
class ISetVersionDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISetVersionDeferral'
    _iid_ = Guid('{033508a2-781a-437a-b078-3f32badcfe47}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISetVersionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISetVersionRequest'
    _iid_ = Guid('{b9c76b9b-1056-4e69-8330-162619956f9b}')
    @winrt_commethod(6)
    def get_CurrentVersion(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_DesiredVersion(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Storage.SetVersionDeferral: ...
    CurrentVersion = property(get_CurrentVersion, None)
    DesiredVersion = property(get_DesiredVersion, None)
class IStorageFile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFile'
    _iid_ = Guid('{fa3f6186-4214-428c-a64c-14c9ac7315ea}')
    @winrt_commethod(6)
    def get_FileType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def OpenAsync(self, accessMode: win32more.Windows.Storage.FileAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(9)
    def OpenTransactedWriteAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
    @winrt_commethod(10)
    def CopyOverloadDefaultNameAndOptions(self, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def CopyOverloadDefaultOptions(self, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def CopyOverload(self, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(13)
    def CopyAndReplaceAsync(self, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def MoveOverloadDefaultNameAndOptions(self, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def MoveOverloadDefaultOptions(self, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def MoveOverload(self, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def MoveAndReplaceAsync(self, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContentType = property(get_ContentType, None)
    FileType = property(get_FileType, None)
class IStorageFile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFile2'
    _iid_ = Guid('{954e4bcf-0a77-42fb-b777-c2ed58a52e44}')
    @winrt_commethod(6)
    def OpenWithOptionsAsync(self, accessMode: win32more.Windows.Storage.FileAccessMode, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(7)
    def OpenTransactedWriteWithOptionsAsync(self, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
class IStorageFilePropertiesWithAvailability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFilePropertiesWithAvailability'
    _iid_ = Guid('{afcbbe9b-582b-4133-9648-e44ca46ee491}')
    @winrt_commethod(6)
    def get_IsAvailable(self) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class IStorageFileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFileStatics'
    _iid_ = Guid('{5984c710-daf2-43c8-8bb4-a4d3eacfd03f}')
    @winrt_commethod(6)
    def GetFileFromPathAsync(self, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def GetFileFromApplicationUriAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def CreateStreamedFileAsync(self, displayNameWithExtension: WinRT_String, dataRequested: win32more.Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def ReplaceWithStreamedFileAsync(self, fileToReplace: win32more.Windows.Storage.IStorageFile, dataRequested: win32more.Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(10)
    def CreateStreamedFileFromUriAsync(self, displayNameWithExtension: WinRT_String, uri: win32more.Windows.Foundation.Uri, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def ReplaceWithStreamedFileFromUriAsync(self, fileToReplace: win32more.Windows.Storage.IStorageFile, uri: win32more.Windows.Foundation.Uri, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
class IStorageFileStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFileStatics2'
    _iid_ = Guid('{5c76a781-212e-4af9-8f04-740cae108974}')
    @winrt_commethod(6)
    def GetFileFromPathForUserAsync(self, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
class IStorageFolder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder'
    _iid_ = Guid('{72d1cb78-b3ef-4f75-a80b-6fd9dae2944b}')
    @winrt_commethod(6)
    def CreateFileAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFileAsync(self, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def CreateFolderAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def CreateFolderAsync(self, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(10)
    def GetFileAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def GetFolderAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(12)
    def GetItemAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_commethod(13)
    def GetFilesAsyncOverloadDefaultOptionsStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_commethod(14)
    def GetFoldersAsyncOverloadDefaultOptionsStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(15)
    def GetItemsAsyncOverloadDefaultStartAndCount(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
class IStorageFolder2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder2'
    _iid_ = Guid('{e827e8b9-08d9-4a8e-a0ac-fe5ed3cbbbd3}')
    @winrt_commethod(6)
    def TryGetItemAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
class IStorageFolder3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder3'
    _iid_ = Guid('{9f617899-bde1-4124-aeb3-b06ad96f98d4}')
    @winrt_commethod(6)
    def TryGetChangeTracker(self) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
class IStorageFolderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolderStatics'
    _iid_ = Guid('{08f327ff-85d5-48b9-aee9-28511e339f9f}')
    @winrt_commethod(6)
    def GetFolderFromPathAsync(self, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IStorageFolderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolderStatics2'
    _iid_ = Guid('{b4656dc3-71d2-467d-8b29-371f0f62bf6f}')
    @winrt_commethod(6)
    def GetFolderFromPathForUserAsync(self, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
class IStorageItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItem'
    _iid_ = Guid('{4207a996-ca2f-42f7-bde8-8b10457a7f30}')
    @winrt_commethod(6)
    def RenameAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RenameAsync(self, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAsyncOverloadDefaultOptions(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DeleteAsync(self, option: win32more.Windows.Storage.StorageDeleteOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def GetBasicPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_commethod(11)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Attributes(self) -> win32more.Windows.Storage.FileAttributes: ...
    @winrt_commethod(14)
    def get_DateCreated(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def IsOfType(self, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
class IStorageItem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItem2'
    _iid_ = Guid('{53f926d2-083c-4283-b45b-81c007237e44}')
    @winrt_commethod(6)
    def GetParentAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(7)
    def IsEqual(self, item: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
class IStorageItemProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemProperties'
    _iid_ = Guid('{86664478-8029-46fe-a789-1c2f3e2ffb5c}')
    @winrt_commethod(6)
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(7)
    def GetThumbnailAsyncOverloadDefaultOptions(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(8)
    def GetThumbnailAsync(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DisplayType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_FolderRelativeId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Properties(self) -> win32more.Windows.Storage.FileProperties.StorageItemContentProperties: ...
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
class IStorageItemProperties2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemProperties2'
    _iid_ = Guid('{8e86a951-04b9-4bd2-929d-fef3f71621d0}')
    @winrt_commethod(6)
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(7)
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(8)
    def GetScaledImageAsThumbnailAsync(self, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
class IStorageItemPropertiesWithProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemPropertiesWithProvider'
    _iid_ = Guid('{861bf39b-6368-4dee-b40e-74684a5ce714}')
    @winrt_commethod(6)
    def get_Provider(self) -> win32more.Windows.Storage.StorageProvider: ...
    Provider = property(get_Provider, None)
class IStorageLibrary(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary'
    _iid_ = Guid('{1edd7103-0e5e-4d6c-b5e8-9318983d6a03}')
    @winrt_commethod(6)
    def RequestAddFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(7)
    def RequestRemoveFolderAsync(self, folder: win32more.Windows.Storage.StorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Folders(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def get_SaveFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(10)
    def add_DefinitionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.StorageLibrary, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DefinitionChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Folders = property(get_Folders, None)
    SaveFolder = property(get_SaveFolder, None)
    DefinitionChanged = event()
class IStorageLibrary2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary2'
    _iid_ = Guid('{5b0ce348-fcb3-4031-afb0-a68d7bd44534}')
    @winrt_commethod(6)
    def get_ChangeTracker(self) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
    ChangeTracker = property(get_ChangeTracker, None)
class IStorageLibrary3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary3'
    _iid_ = Guid('{8a281291-2154-4201-8113-d2c05ce1ad23}')
    @winrt_commethod(6)
    def AreFolderSuggestionsAvailableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IStorageLibraryChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChange'
    _iid_ = Guid('{00980b23-2be2-4909-aa48-159f5203a51e}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.Storage.StorageLibraryChangeType: ...
    @winrt_commethod(7)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PreviousPath(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def IsOfType(self, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_commethod(10)
    def GetStorageItemAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    ChangeType = property(get_ChangeType, None)
    Path = property(get_Path, None)
    PreviousPath = property(get_PreviousPath, None)
class IStorageLibraryChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeReader'
    _iid_ = Guid('{f205bc83-fca2-41f9-8954-ee2e991eb96f}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageLibraryChange]]: ...
    @winrt_commethod(7)
    def AcceptChangesAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IStorageLibraryChangeReader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeReader2'
    _iid_ = Guid('{abf4868b-fbcc-4a4f-999e-e7ab7c646dbe}')
    @winrt_commethod(6)
    def GetLastChangeId(self) -> UInt64: ...
class IStorageLibraryChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTracker'
    _iid_ = Guid('{9e157316-6073-44f6-9681-7492d1286c90}')
    @winrt_commethod(6)
    def GetChangeReader(self) -> win32more.Windows.Storage.StorageLibraryChangeReader: ...
    @winrt_commethod(7)
    def Enable(self) -> Void: ...
    @winrt_commethod(8)
    def Reset(self) -> Void: ...
class IStorageLibraryChangeTracker2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTracker2'
    _iid_ = Guid('{cd051c3b-0f9f-42f9-8fb3-158d82e13821}')
    @winrt_commethod(6)
    def EnableWithOptions(self, options: win32more.Windows.Storage.StorageLibraryChangeTrackerOptions) -> Void: ...
    @winrt_commethod(7)
    def Disable(self) -> Void: ...
class IStorageLibraryChangeTrackerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTrackerOptions'
    _iid_ = Guid('{bb52bcd4-1a6d-59c0-ad2a-823a20532483}')
    @winrt_commethod(6)
    def get_TrackChangeDetails(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TrackChangeDetails(self, value: Boolean) -> Void: ...
    TrackChangeDetails = property(get_TrackChangeDetails, put_TrackChangeDetails)
class IStorageLibraryLastChangeId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryLastChangeId'
    _iid_ = Guid('{5281826a-bbe1-53bc-82ca-81cc7f039329}')
class IStorageLibraryLastChangeIdStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryLastChangeIdStatics'
    _iid_ = Guid('{81a49128-2ca3-5309-b0d1-cf0788e40762}')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt64: ...
    Unknown = property(get_Unknown, None)
class IStorageLibraryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryStatics'
    _iid_ = Guid('{4208a6db-684a-49c6-9e59-90121ee050d6}')
    @winrt_commethod(6)
    def GetLibraryAsync(self, libraryId: win32more.Windows.Storage.KnownLibraryId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageLibrary]: ...
class IStorageLibraryStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryStatics2'
    _iid_ = Guid('{ffb08ddc-fa75-4695-b9d1-7f81f97832e3}')
    @winrt_commethod(6)
    def GetLibraryForUserAsync(self, user: win32more.Windows.System.User, libraryId: win32more.Windows.Storage.KnownLibraryId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageLibrary]: ...
class IStorageProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageProvider'
    _iid_ = Guid('{e705eed4-d478-47d6-ba46-1a8ebe114a20}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
class IStorageProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageProvider2'
    _iid_ = Guid('{010d1917-3404-414b-9fd7-cd44472eaa39}')
    @winrt_commethod(6)
    def IsPropertySupportedForPartialFileAsync(self, propertyCanonicalName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IStorageStreamTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Storage.IStorageStreamTransaction'
    _iid_ = Guid('{f67cf363-a53d-4d94-ae2c-67232d93acdd}')
    @winrt_commethod(6)
    def get_Stream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(7)
    def CommitAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Stream = property(get_Stream, None)
class IStreamedFileDataRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStreamedFileDataRequest'
    _iid_ = Guid('{1673fcce-dabd-4d50-beee-180b8a8191b6}')
    @winrt_commethod(6)
    def FailAndClose(self, failureMode: win32more.Windows.Storage.StreamedFileFailureMode) -> Void: ...
class ISystemAudioProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemAudioProperties'
    _iid_ = Guid('{3f8f38b7-308c-47e1-924d-8645348e5db7}')
    @winrt_commethod(6)
    def get_EncodingBitrate(self) -> WinRT_String: ...
    EncodingBitrate = property(get_EncodingBitrate, None)
class ISystemDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemDataPaths'
    _iid_ = Guid('{e32abf70-d8fa-45ec-a942-d2e26fb60ba5}')
    @winrt_commethod(6)
    def get_Fonts(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ProgramData(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Public(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PublicDesktop(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_PublicDocuments(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_PublicDownloads(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_PublicMusic(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_PublicPictures(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_PublicVideos(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_System(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_SystemHost(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_SystemX86(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_SystemX64(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_SystemArm(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_UserProfiles(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Windows(self) -> WinRT_String: ...
    Fonts = property(get_Fonts, None)
    ProgramData = property(get_ProgramData, None)
    Public = property(get_Public, None)
    PublicDesktop = property(get_PublicDesktop, None)
    PublicDocuments = property(get_PublicDocuments, None)
    PublicDownloads = property(get_PublicDownloads, None)
    PublicMusic = property(get_PublicMusic, None)
    PublicPictures = property(get_PublicPictures, None)
    PublicVideos = property(get_PublicVideos, None)
    System = property(get_System, None)
    SystemArm = property(get_SystemArm, None)
    SystemHost = property(get_SystemHost, None)
    SystemX64 = property(get_SystemX64, None)
    SystemX86 = property(get_SystemX86, None)
    UserProfiles = property(get_UserProfiles, None)
    Windows = property(get_Windows, None)
class ISystemDataPathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemDataPathsStatics'
    _iid_ = Guid('{e0f96fd0-9920-4bca-b379-f96fdf7caad8}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Storage.SystemDataPaths: ...
class ISystemGPSProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemGPSProperties'
    _iid_ = Guid('{c0f46eb4-c174-481a-bc25-921986f6a6f3}')
    @winrt_commethod(6)
    def get_LatitudeDecimal(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LongitudeDecimal(self) -> WinRT_String: ...
    LatitudeDecimal = property(get_LatitudeDecimal, None)
    LongitudeDecimal = property(get_LongitudeDecimal, None)
class ISystemImageProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemImageProperties'
    _iid_ = Guid('{011b2e30-8b39-4308-bea1-e8aa61e47826}')
    @winrt_commethod(6)
    def get_HorizontalSize(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VerticalSize(self) -> WinRT_String: ...
    HorizontalSize = property(get_HorizontalSize, None)
    VerticalSize = property(get_VerticalSize, None)
class ISystemMediaProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemMediaProperties'
    _iid_ = Guid('{a42b3316-8415-40dc-8c44-98361d235430}')
    @winrt_commethod(6)
    def get_Duration(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Producer(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_SubTitle(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Writer(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Year(self) -> WinRT_String: ...
    Duration = property(get_Duration, None)
    Producer = property(get_Producer, None)
    Publisher = property(get_Publisher, None)
    SubTitle = property(get_SubTitle, None)
    Writer = property(get_Writer, None)
    Year = property(get_Year, None)
class ISystemMusicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemMusicProperties'
    _iid_ = Guid('{b47988d5-67af-4bc3-8d39-5b89022026a1}')
    @winrt_commethod(6)
    def get_AlbumArtist(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AlbumTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Artist(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Composer(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Conductor(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayArtist(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Genre(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_TrackNumber(self) -> WinRT_String: ...
    AlbumArtist = property(get_AlbumArtist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    Artist = property(get_Artist, None)
    Composer = property(get_Composer, None)
    Conductor = property(get_Conductor, None)
    DisplayArtist = property(get_DisplayArtist, None)
    Genre = property(get_Genre, None)
    TrackNumber = property(get_TrackNumber, None)
class ISystemPhotoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemPhotoProperties'
    _iid_ = Guid('{4734fc3d-ab21-4424-b735-f4353a56c8fc}')
    @winrt_commethod(6)
    def get_CameraManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CameraModel(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DateTaken(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Orientation(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_PeopleNames(self) -> WinRT_String: ...
    CameraManufacturer = property(get_CameraManufacturer, None)
    CameraModel = property(get_CameraModel, None)
    DateTaken = property(get_DateTaken, None)
    Orientation = property(get_Orientation, None)
    PeopleNames = property(get_PeopleNames, None)
class ISystemProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemProperties'
    _iid_ = Guid('{917a71c1-85f3-4dd1-b001-a50bfd21c8d2}')
    @winrt_commethod(6)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ItemNameDisplay(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Keywords(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Rating(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Audio(self) -> win32more.Windows.Storage.SystemAudioProperties: ...
    @winrt_commethod(13)
    def get_GPS(self) -> win32more.Windows.Storage.SystemGPSProperties: ...
    @winrt_commethod(14)
    def get_Media(self) -> win32more.Windows.Storage.SystemMediaProperties: ...
    @winrt_commethod(15)
    def get_Music(self) -> win32more.Windows.Storage.SystemMusicProperties: ...
    @winrt_commethod(16)
    def get_Photo(self) -> win32more.Windows.Storage.SystemPhotoProperties: ...
    @winrt_commethod(17)
    def get_Video(self) -> win32more.Windows.Storage.SystemVideoProperties: ...
    @winrt_commethod(18)
    def get_Image(self) -> win32more.Windows.Storage.SystemImageProperties: ...
    Audio = property(get_Audio, None)
    Author = property(get_Author, None)
    Comment = property(get_Comment, None)
    GPS = property(get_GPS, None)
    Image = property(get_Image, None)
    ItemNameDisplay = property(get_ItemNameDisplay, None)
    Keywords = property(get_Keywords, None)
    Media = property(get_Media, None)
    Music = property(get_Music, None)
    Photo = property(get_Photo, None)
    Rating = property(get_Rating, None)
    Title = property(get_Title, None)
    Video = property(get_Video, None)
class ISystemVideoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemVideoProperties'
    _iid_ = Guid('{2040f715-67f8-4322-9b80-4fa9fefb83e8}')
    @winrt_commethod(6)
    def get_Director(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FrameHeight(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FrameWidth(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Orientation(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_TotalBitrate(self) -> WinRT_String: ...
    Director = property(get_Director, None)
    FrameHeight = property(get_FrameHeight, None)
    FrameWidth = property(get_FrameWidth, None)
    Orientation = property(get_Orientation, None)
    TotalBitrate = property(get_TotalBitrate, None)
class IUserDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IUserDataPaths'
    _iid_ = Guid('{f9c53912-abc4-46ff-8a2b-dc9d7fa6e52f}')
    @winrt_commethod(6)
    def get_CameraRoll(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Cookies(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Desktop(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Documents(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Downloads(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Favorites(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_History(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_InternetCache(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_LocalAppData(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_LocalAppDataLow(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Music(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Pictures(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Profile(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Recent(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_RoamingAppData(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_SavedPictures(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Screenshots(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_Templates(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_Videos(self) -> WinRT_String: ...
    CameraRoll = property(get_CameraRoll, None)
    Cookies = property(get_Cookies, None)
    Desktop = property(get_Desktop, None)
    Documents = property(get_Documents, None)
    Downloads = property(get_Downloads, None)
    Favorites = property(get_Favorites, None)
    History = property(get_History, None)
    InternetCache = property(get_InternetCache, None)
    LocalAppData = property(get_LocalAppData, None)
    LocalAppDataLow = property(get_LocalAppDataLow, None)
    Music = property(get_Music, None)
    Pictures = property(get_Pictures, None)
    Profile = property(get_Profile, None)
    Recent = property(get_Recent, None)
    RoamingAppData = property(get_RoamingAppData, None)
    SavedPictures = property(get_SavedPictures, None)
    Screenshots = property(get_Screenshots, None)
    Templates = property(get_Templates, None)
    Videos = property(get_Videos, None)
class IUserDataPathsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IUserDataPathsStatics'
    _iid_ = Guid('{01b29def-e062-48a1-8b0c-f2c7a9ca56c0}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Storage.UserDataPaths: ...
    @winrt_commethod(7)
    def GetDefault(self) -> win32more.Windows.Storage.UserDataPaths: ...
class KnownFolderId(Enum, Int32):
    AppCaptures = 0
    CameraRoll = 1
    DocumentsLibrary = 2
    HomeGroup = 3
    MediaServerDevices = 4
    MusicLibrary = 5
    Objects3D = 6
    PicturesLibrary = 7
    Playlists = 8
    RecordedCalls = 9
    RemovableDevices = 10
    SavedPictures = 11
    Screenshots = 12
    VideosLibrary = 13
    AllAppMods = 14
    CurrentAppMods = 15
    DownloadsFolder = 16
class _KnownFolders_Meta_(ComPtr.__class__):
    pass
class KnownFolders(ComPtr, metaclass=_KnownFolders_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.KnownFolders'
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Storage.IKnownFoldersStatics4, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_classmethod
    def RequestAccessForUserAsync(cls: win32more.Windows.Storage.IKnownFoldersStatics4, user: win32more.Windows.System.User, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_classmethod
    def GetFolderAsync(cls: win32more.Windows.Storage.IKnownFoldersStatics4, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def GetFolderForUserAsync(cls: win32more.Windows.Storage.IKnownFoldersStatics3, user: win32more.Windows.System.User, folderId: win32more.Windows.Storage.KnownFolderId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def get_Objects3D(cls: win32more.Windows.Storage.IKnownFoldersStatics2) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_AppCaptures(cls: win32more.Windows.Storage.IKnownFoldersStatics2) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_RecordedCalls(cls: win32more.Windows.Storage.IKnownFoldersStatics2) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_SavedPictures(cls: win32more.Windows.Storage.IKnownFoldersSavedPicturesStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_CameraRoll(cls: win32more.Windows.Storage.IKnownFoldersCameraRollStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_Playlists(cls: win32more.Windows.Storage.IKnownFoldersPlaylistsStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_MusicLibrary(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_PicturesLibrary(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_VideosLibrary(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_DocumentsLibrary(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_HomeGroup(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_RemovableDevices(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_MediaServerDevices(cls: win32more.Windows.Storage.IKnownFoldersStatics) -> win32more.Windows.Storage.StorageFolder: ...
    _KnownFolders_Meta_.AppCaptures = property(get_AppCaptures, None)
    _KnownFolders_Meta_.CameraRoll = property(get_CameraRoll, None)
    _KnownFolders_Meta_.DocumentsLibrary = property(get_DocumentsLibrary, None)
    _KnownFolders_Meta_.HomeGroup = property(get_HomeGroup, None)
    _KnownFolders_Meta_.MediaServerDevices = property(get_MediaServerDevices, None)
    _KnownFolders_Meta_.MusicLibrary = property(get_MusicLibrary, None)
    _KnownFolders_Meta_.Objects3D = property(get_Objects3D, None)
    _KnownFolders_Meta_.PicturesLibrary = property(get_PicturesLibrary, None)
    _KnownFolders_Meta_.Playlists = property(get_Playlists, None)
    _KnownFolders_Meta_.RecordedCalls = property(get_RecordedCalls, None)
    _KnownFolders_Meta_.RemovableDevices = property(get_RemovableDevices, None)
    _KnownFolders_Meta_.SavedPictures = property(get_SavedPictures, None)
    _KnownFolders_Meta_.VideosLibrary = property(get_VideosLibrary, None)
class KnownFoldersAccessStatus(Enum, Int32):
    DeniedBySystem = 0
    NotDeclaredByApp = 1
    DeniedByUser = 2
    UserPromptRequired = 3
    Allowed = 4
    AllowedPerAppFolder = 5
class KnownLibraryId(Enum, Int32):
    Music = 0
    Pictures = 1
    Videos = 2
    Documents = 3
class NameCollisionOption(Enum, Int32):
    GenerateUniqueName = 0
    ReplaceExisting = 1
    FailIfExists = 2
class PathIO(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.PathIO'
    @winrt_classmethod
    def ReadTextAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReadTextWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def WriteTextAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteTextWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadLinesAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def ReadLinesWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def WriteLinesAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteLinesWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesWithEncodingAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], encoding: win32more.Windows.Storage.Streams.UnicodeEncoding) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadBufferAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def WriteBufferAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteBytesAsync(cls: win32more.Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, buffer: PassArray[Byte]) -> win32more.Windows.Foundation.IAsyncAction: ...
class SetVersionDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISetVersionDeferral
    _classid_ = 'Windows.Storage.SetVersionDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Storage.ISetVersionDeferral) -> Void: ...
class SetVersionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISetVersionRequest
    _classid_ = 'Windows.Storage.SetVersionRequest'
    @winrt_mixinmethod
    def get_CurrentVersion(self: win32more.Windows.Storage.ISetVersionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_DesiredVersion(self: win32more.Windows.Storage.ISetVersionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.ISetVersionRequest) -> win32more.Windows.Storage.SetVersionDeferral: ...
    CurrentVersion = property(get_CurrentVersion, None)
    DesiredVersion = property(get_DesiredVersion, None)
class StorageDeleteOption(Enum, Int32):
    Default = 0
    PermanentDelete = 1
class StorageFile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageFile
    _classid_ = 'Windows.Storage.StorageFile'
    @winrt_mixinmethod
    def get_FileType(self: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.Storage.IStorageFile, accessMode: win32more.Windows.Storage.FileAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteAsync(self: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultNameAndOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverload(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyAndReplaceAsync(self: win32more.Windows.Storage.IStorageFile, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultNameAndOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverload(self: win32more.Windows.Storage.IStorageFile, destinationFolder: win32more.Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveAndReplaceAsync(self: win32more.Windows.Storage.IStorageFile, fileToReplace: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Storage.IStorageItem, option: win32more.Windows.Storage.StorageDeleteOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: win32more.Windows.Storage.IStorageItem, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def OpenReadAsync(self: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def OpenSequentialReadAsync(self: win32more.Windows.Storage.Streams.IInputStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IInputStream]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Storage.IStorageItemProperties) -> win32more.Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetParentAsync(self: win32more.Windows.Storage.IStorageItem2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Storage.IStorageItem2, item: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.Storage.IStorageItemPropertiesWithProvider) -> win32more.Windows.Storage.StorageProvider: ...
    @winrt_mixinmethod
    def get_IsAvailable(self: win32more.Windows.Storage.IStorageFilePropertiesWithAvailability) -> Boolean: ...
    @winrt_mixinmethod
    def OpenWithOptionsAsync(self: win32more.Windows.Storage.IStorageFile2, accessMode: win32more.Windows.Storage.FileAccessMode, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteWithOptionsAsync(self: win32more.Windows.Storage.IStorageFile2, options: win32more.Windows.Storage.StorageOpenOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageStreamTransaction]: ...
    @winrt_classmethod
    def GetFileFromPathForUserAsync(cls: win32more.Windows.Storage.IStorageFileStatics2, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def GetFileFromPathAsync(cls: win32more.Windows.Storage.IStorageFileStatics, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def GetFileFromApplicationUriAsync(cls: win32more.Windows.Storage.IStorageFileStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateStreamedFileAsync(cls: win32more.Windows.Storage.IStorageFileStatics, displayNameWithExtension: WinRT_String, dataRequested: win32more.Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def ReplaceWithStreamedFileAsync(cls: win32more.Windows.Storage.IStorageFileStatics, fileToReplace: win32more.Windows.Storage.IStorageFile, dataRequested: win32more.Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateStreamedFileFromUriAsync(cls: win32more.Windows.Storage.IStorageFileStatics, displayNameWithExtension: WinRT_String, uri: win32more.Windows.Foundation.Uri, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def ReplaceWithStreamedFileFromUriAsync(cls: win32more.Windows.Storage.IStorageFileStatics, fileToReplace: win32more.Windows.Storage.IStorageFile, uri: win32more.Windows.Foundation.Uri, thumbnail: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    Attributes = property(get_Attributes, None)
    ContentType = property(get_ContentType, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FileType = property(get_FileType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    IsAvailable = property(get_IsAvailable, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
class StorageFolder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageFolder
    _classid_ = 'Windows.Storage.StorageFolder'
    @winrt_mixinmethod
    def CreateFileAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFileAsync(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFolderAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def CreateFolderAsync(self: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemAsync(self: win32more.Windows.Storage.IStorageFolder, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultOptionsStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultOptionsStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: win32more.Windows.Storage.IStorageItem, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Storage.IStorageItem, option: win32more.Windows.Storage.StorageDeleteOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: win32more.Windows.Storage.IStorageItem, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def GetIndexedStateAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Search.IndexedState]: ...
    @winrt_mixinmethod
    def CreateFileQueryOverloadDefault(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryOverloadDefault(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQuery(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQueryWithOptions(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> win32more.Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def GetFilesAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultStartAndCount(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def AreQueryOptionsSupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: win32more.Windows.Storage.Search.QueryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFolderQuerySupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFolderQuery) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFileQuerySupported(self: win32more.Windows.Storage.Search.IStorageFolderQueryOperations, query: win32more.Windows.Storage.Search.CommonFileQuery) -> Boolean: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: win32more.Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Storage.IStorageItemProperties) -> win32more.Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsync(self: win32more.Windows.Storage.IStorageItemProperties2, mode: win32more.Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: win32more.Windows.Storage.FileProperties.ThumbnailOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetParentAsync(self: win32more.Windows.Storage.IStorageItem2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Storage.IStorageItem2, item: win32more.Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetItemAsync(self: win32more.Windows.Storage.IStorageFolder2, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.Storage.IStorageItemPropertiesWithProvider) -> win32more.Windows.Storage.StorageProvider: ...
    @winrt_mixinmethod
    def TryGetChangeTracker(self: win32more.Windows.Storage.IStorageFolder3) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
    @winrt_classmethod
    def GetFolderFromPathForUserAsync(cls: win32more.Windows.Storage.IStorageFolderStatics2, user: win32more.Windows.System.User, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def GetFolderFromPathAsync(cls: win32more.Windows.Storage.IStorageFolderStatics, path: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
class StorageItemTypes(Enum, UInt32):
    None_ = 0
    File = 1
    Folder = 2
class StorageLibrary(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibrary
    _classid_ = 'Windows.Storage.StorageLibrary'
    @winrt_mixinmethod
    def RequestAddFolderAsync(self: win32more.Windows.Storage.IStorageLibrary) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def RequestRemoveFolderAsync(self: win32more.Windows.Storage.IStorageLibrary, folder: win32more.Windows.Storage.StorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Folders(self: win32more.Windows.Storage.IStorageLibrary) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def get_SaveFolder(self: win32more.Windows.Storage.IStorageLibrary) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_DefinitionChanged(self: win32more.Windows.Storage.IStorageLibrary, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.StorageLibrary, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DefinitionChanged(self: win32more.Windows.Storage.IStorageLibrary, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: win32more.Windows.Storage.IStorageLibrary2) -> win32more.Windows.Storage.StorageLibraryChangeTracker: ...
    @winrt_mixinmethod
    def AreFolderSuggestionsAvailableAsync(self: win32more.Windows.Storage.IStorageLibrary3) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetLibraryForUserAsync(cls: win32more.Windows.Storage.IStorageLibraryStatics2, user: win32more.Windows.System.User, libraryId: win32more.Windows.Storage.KnownLibraryId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageLibrary]: ...
    @winrt_classmethod
    def GetLibraryAsync(cls: win32more.Windows.Storage.IStorageLibraryStatics, libraryId: win32more.Windows.Storage.KnownLibraryId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageLibrary]: ...
    ChangeTracker = property(get_ChangeTracker, None)
    Folders = property(get_Folders, None)
    SaveFolder = property(get_SaveFolder, None)
    DefinitionChanged = event()
class StorageLibraryChange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibraryChange
    _classid_ = 'Windows.Storage.StorageLibraryChange'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.Storage.IStorageLibraryChange) -> win32more.Windows.Storage.StorageLibraryChangeType: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.IStorageLibraryChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PreviousPath(self: win32more.Windows.Storage.IStorageLibraryChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsOfType(self: win32more.Windows.Storage.IStorageLibraryChange, type: win32more.Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def GetStorageItemAsync(self: win32more.Windows.Storage.IStorageLibraryChange) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.IStorageItem]: ...
    ChangeType = property(get_ChangeType, None)
    Path = property(get_Path, None)
    PreviousPath = property(get_PreviousPath, None)
class StorageLibraryChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibraryChangeReader
    _classid_ = 'Windows.Storage.StorageLibraryChangeReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.Storage.IStorageLibraryChangeReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageLibraryChange]]: ...
    @winrt_mixinmethod
    def AcceptChangesAsync(self: win32more.Windows.Storage.IStorageLibraryChangeReader) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetLastChangeId(self: win32more.Windows.Storage.IStorageLibraryChangeReader2) -> UInt64: ...
class StorageLibraryChangeTracker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibraryChangeTracker
    _classid_ = 'Windows.Storage.StorageLibraryChangeTracker'
    @winrt_mixinmethod
    def GetChangeReader(self: win32more.Windows.Storage.IStorageLibraryChangeTracker) -> win32more.Windows.Storage.StorageLibraryChangeReader: ...
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.Storage.IStorageLibraryChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Storage.IStorageLibraryChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def EnableWithOptions(self: win32more.Windows.Storage.IStorageLibraryChangeTracker2, options: win32more.Windows.Storage.StorageLibraryChangeTrackerOptions) -> Void: ...
    @winrt_mixinmethod
    def Disable(self: win32more.Windows.Storage.IStorageLibraryChangeTracker2) -> Void: ...
class StorageLibraryChangeTrackerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibraryChangeTrackerOptions
    _classid_ = 'Windows.Storage.StorageLibraryChangeTrackerOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.StorageLibraryChangeTrackerOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.StorageLibraryChangeTrackerOptions: ...
    @winrt_mixinmethod
    def get_TrackChangeDetails(self: win32more.Windows.Storage.IStorageLibraryChangeTrackerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_TrackChangeDetails(self: win32more.Windows.Storage.IStorageLibraryChangeTrackerOptions, value: Boolean) -> Void: ...
    TrackChangeDetails = property(get_TrackChangeDetails, put_TrackChangeDetails)
class StorageLibraryChangeType(Enum, Int32):
    Created = 0
    Deleted = 1
    MovedOrRenamed = 2
    ContentsChanged = 3
    MovedOutOfLibrary = 4
    MovedIntoLibrary = 5
    ContentsReplaced = 6
    IndexingStatusChanged = 7
    EncryptionChanged = 8
    ChangeTrackingLost = 9
class _StorageLibraryLastChangeId_Meta_(ComPtr.__class__):
    pass
class StorageLibraryLastChangeId(ComPtr, metaclass=_StorageLibraryLastChangeId_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageLibraryLastChangeId
    _classid_ = 'Windows.Storage.StorageLibraryLastChangeId'
    @winrt_classmethod
    def get_Unknown(cls: win32more.Windows.Storage.IStorageLibraryLastChangeIdStatics) -> UInt64: ...
    _StorageLibraryLastChangeId_Meta_.Unknown = property(get_Unknown, None)
class StorageOpenOptions(Enum, UInt32):
    None_ = 0
    AllowOnlyReaders = 1
    AllowReadersAndWriters = 2
class StorageProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IStorageProvider
    _classid_ = 'Windows.Storage.StorageProvider'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.IStorageProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Storage.IStorageProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPropertySupportedForPartialFileAsync(self: win32more.Windows.Storage.IStorageProvider2, propertyCanonicalName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
class StorageStreamTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.IStorageStreamTransaction
    _classid_ = 'Windows.Storage.StorageStreamTransaction'
    @winrt_mixinmethod
    def get_Stream(self: win32more.Windows.Storage.IStorageStreamTransaction) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def CommitAsync(self: win32more.Windows.Storage.IStorageStreamTransaction) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Stream = property(get_Stream, None)
class StreamedFileDataRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Storage.Streams.IOutputStream
    _classid_ = 'Windows.Storage.StreamedFileDataRequest'
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def FailAndClose(self: win32more.Windows.Storage.IStreamedFileDataRequest, failureMode: win32more.Windows.Storage.StreamedFileFailureMode) -> Void: ...
class StreamedFileDataRequestedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fef6a824-2fe1-4d07-a35b-b77c50b5f4cc}')
    @winrt_commethod(3)
    def Invoke(self, stream: win32more.Windows.Storage.StreamedFileDataRequest) -> Void: ...
class StreamedFileFailureMode(Enum, Int32):
    Failed = 0
    CurrentlyUnavailable = 1
    Incomplete = 2
class SystemAudioProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemAudioProperties
    _classid_ = 'Windows.Storage.SystemAudioProperties'
    @winrt_mixinmethod
    def get_EncodingBitrate(self: win32more.Windows.Storage.ISystemAudioProperties) -> WinRT_String: ...
    EncodingBitrate = property(get_EncodingBitrate, None)
class SystemDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemDataPaths
    _classid_ = 'Windows.Storage.SystemDataPaths'
    @winrt_mixinmethod
    def get_Fonts(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProgramData(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Public(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDesktop(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDocuments(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDownloads(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicMusic(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicPictures(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicVideos(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_System(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHost(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemX86(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemX64(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemArm(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserProfiles(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Windows(self: win32more.Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Storage.ISystemDataPathsStatics) -> win32more.Windows.Storage.SystemDataPaths: ...
    Fonts = property(get_Fonts, None)
    ProgramData = property(get_ProgramData, None)
    Public = property(get_Public, None)
    PublicDesktop = property(get_PublicDesktop, None)
    PublicDocuments = property(get_PublicDocuments, None)
    PublicDownloads = property(get_PublicDownloads, None)
    PublicMusic = property(get_PublicMusic, None)
    PublicPictures = property(get_PublicPictures, None)
    PublicVideos = property(get_PublicVideos, None)
    System = property(get_System, None)
    SystemArm = property(get_SystemArm, None)
    SystemHost = property(get_SystemHost, None)
    SystemX64 = property(get_SystemX64, None)
    SystemX86 = property(get_SystemX86, None)
    UserProfiles = property(get_UserProfiles, None)
    Windows = property(get_Windows, None)
class SystemGPSProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemGPSProperties
    _classid_ = 'Windows.Storage.SystemGPSProperties'
    @winrt_mixinmethod
    def get_LatitudeDecimal(self: win32more.Windows.Storage.ISystemGPSProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LongitudeDecimal(self: win32more.Windows.Storage.ISystemGPSProperties) -> WinRT_String: ...
    LatitudeDecimal = property(get_LatitudeDecimal, None)
    LongitudeDecimal = property(get_LongitudeDecimal, None)
class SystemImageProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemImageProperties
    _classid_ = 'Windows.Storage.SystemImageProperties'
    @winrt_mixinmethod
    def get_HorizontalSize(self: win32more.Windows.Storage.ISystemImageProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VerticalSize(self: win32more.Windows.Storage.ISystemImageProperties) -> WinRT_String: ...
    HorizontalSize = property(get_HorizontalSize, None)
    VerticalSize = property(get_VerticalSize, None)
class SystemMediaProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemMediaProperties
    _classid_ = 'Windows.Storage.SystemMediaProperties'
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Producer(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SubTitle(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Writer(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Year(self: win32more.Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    Duration = property(get_Duration, None)
    Producer = property(get_Producer, None)
    Publisher = property(get_Publisher, None)
    SubTitle = property(get_SubTitle, None)
    Writer = property(get_Writer, None)
    Year = property(get_Year, None)
class SystemMusicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemMusicProperties
    _classid_ = 'Windows.Storage.SystemMusicProperties'
    @winrt_mixinmethod
    def get_AlbumArtist(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumTitle(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Artist(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Composer(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Conductor(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayArtist(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Genre(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackNumber(self: win32more.Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    AlbumArtist = property(get_AlbumArtist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    Artist = property(get_Artist, None)
    Composer = property(get_Composer, None)
    Conductor = property(get_Conductor, None)
    DisplayArtist = property(get_DisplayArtist, None)
    Genre = property(get_Genre, None)
    TrackNumber = property(get_TrackNumber, None)
class SystemPhotoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemPhotoProperties
    _classid_ = 'Windows.Storage.SystemPhotoProperties'
    @winrt_mixinmethod
    def get_CameraManufacturer(self: win32more.Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CameraModel(self: win32more.Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateTaken(self: win32more.Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PeopleNames(self: win32more.Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    CameraManufacturer = property(get_CameraManufacturer, None)
    CameraModel = property(get_CameraModel, None)
    DateTaken = property(get_DateTaken, None)
    Orientation = property(get_Orientation, None)
    PeopleNames = property(get_PeopleNames, None)
class _SystemProperties_Meta_(ComPtr.__class__):
    pass
class SystemProperties(ComPtr, metaclass=_SystemProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.SystemProperties'
    @winrt_classmethod
    def get_Author(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Comment(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_ItemNameDisplay(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Keywords(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rating(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Title(cls: win32more.Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Audio(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemAudioProperties: ...
    @winrt_classmethod
    def get_GPS(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemGPSProperties: ...
    @winrt_classmethod
    def get_Media(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemMediaProperties: ...
    @winrt_classmethod
    def get_Music(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemMusicProperties: ...
    @winrt_classmethod
    def get_Photo(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemPhotoProperties: ...
    @winrt_classmethod
    def get_Video(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemVideoProperties: ...
    @winrt_classmethod
    def get_Image(cls: win32more.Windows.Storage.ISystemProperties) -> win32more.Windows.Storage.SystemImageProperties: ...
    _SystemProperties_Meta_.Audio = property(get_Audio, None)
    _SystemProperties_Meta_.Author = property(get_Author, None)
    _SystemProperties_Meta_.Comment = property(get_Comment, None)
    _SystemProperties_Meta_.GPS = property(get_GPS, None)
    _SystemProperties_Meta_.Image = property(get_Image, None)
    _SystemProperties_Meta_.ItemNameDisplay = property(get_ItemNameDisplay, None)
    _SystemProperties_Meta_.Keywords = property(get_Keywords, None)
    _SystemProperties_Meta_.Media = property(get_Media, None)
    _SystemProperties_Meta_.Music = property(get_Music, None)
    _SystemProperties_Meta_.Photo = property(get_Photo, None)
    _SystemProperties_Meta_.Rating = property(get_Rating, None)
    _SystemProperties_Meta_.Title = property(get_Title, None)
    _SystemProperties_Meta_.Video = property(get_Video, None)
class SystemVideoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.ISystemVideoProperties
    _classid_ = 'Windows.Storage.SystemVideoProperties'
    @winrt_mixinmethod
    def get_Director(self: win32more.Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameHeight(self: win32more.Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameWidth(self: win32more.Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TotalBitrate(self: win32more.Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    Director = property(get_Director, None)
    FrameHeight = property(get_FrameHeight, None)
    FrameWidth = property(get_FrameWidth, None)
    Orientation = property(get_Orientation, None)
    TotalBitrate = property(get_TotalBitrate, None)
class UserDataPaths(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.IUserDataPaths
    _classid_ = 'Windows.Storage.UserDataPaths'
    @winrt_mixinmethod
    def get_CameraRoll(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Cookies(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Desktop(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Documents(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Downloads(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Favorites(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_History(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InternetCache(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppData(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppDataLow(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Music(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Pictures(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Profile(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recent(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingAppData(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SavedPictures(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Screenshots(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Templates(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Videos(self: win32more.Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Storage.IUserDataPathsStatics, user: win32more.Windows.System.User) -> win32more.Windows.Storage.UserDataPaths: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Storage.IUserDataPathsStatics) -> win32more.Windows.Storage.UserDataPaths: ...
    CameraRoll = property(get_CameraRoll, None)
    Cookies = property(get_Cookies, None)
    Desktop = property(get_Desktop, None)
    Documents = property(get_Documents, None)
    Downloads = property(get_Downloads, None)
    Favorites = property(get_Favorites, None)
    History = property(get_History, None)
    InternetCache = property(get_InternetCache, None)
    LocalAppData = property(get_LocalAppData, None)
    LocalAppDataLow = property(get_LocalAppDataLow, None)
    Music = property(get_Music, None)
    Pictures = property(get_Pictures, None)
    Profile = property(get_Profile, None)
    Recent = property(get_Recent, None)
    RoamingAppData = property(get_RoamingAppData, None)
    SavedPictures = property(get_SavedPictures, None)
    Screenshots = property(get_Screenshots, None)
    Templates = property(get_Templates, None)
    Videos = property(get_Videos, None)


make_ready(__name__)
