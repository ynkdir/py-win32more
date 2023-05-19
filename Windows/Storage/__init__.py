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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.FileProperties
import Windows.Storage.Provider
import Windows.Storage.Search
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
class AppDataPaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IAppDataPaths
    _classid_ = 'Windows.Storage.AppDataPaths'
    @winrt_mixinmethod
    def get_Cookies(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Desktop(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Documents(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Favorites(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_History(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InternetCache(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppData(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProgramData(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingAppData(self: Windows.Storage.IAppDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.Storage.IAppDataPathsStatics, user: Windows.System.User) -> Windows.Storage.AppDataPaths: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Storage.IAppDataPathsStatics) -> Windows.Storage.AppDataPaths: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IApplicationData
    _classid_ = 'Windows.Storage.ApplicationData'
    @winrt_mixinmethod
    def get_Version(self: Windows.Storage.IApplicationData) -> UInt32: ...
    @winrt_mixinmethod
    def SetVersionAsync(self: Windows.Storage.IApplicationData, desiredVersion: UInt32, handler: Windows.Storage.ApplicationDataSetVersionHandler) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearAllAsync(self: Windows.Storage.IApplicationData) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearAsync(self: Windows.Storage.IApplicationData, locality: Windows.Storage.ApplicationDataLocality) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_LocalSettings(self: Windows.Storage.IApplicationData) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def get_RoamingSettings(self: Windows.Storage.IApplicationData) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def get_LocalFolder(self: Windows.Storage.IApplicationData) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_RoamingFolder(self: Windows.Storage.IApplicationData) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_TemporaryFolder(self: Windows.Storage.IApplicationData) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_DataChanged(self: Windows.Storage.IApplicationData, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.ApplicationData, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataChanged(self: Windows.Storage.IApplicationData, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SignalDataChanged(self: Windows.Storage.IApplicationData) -> Void: ...
    @winrt_mixinmethod
    def get_RoamingStorageQuota(self: Windows.Storage.IApplicationData) -> UInt64: ...
    @winrt_mixinmethod
    def get_LocalCacheFolder(self: Windows.Storage.IApplicationData2) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def GetPublisherCacheFolder(self: Windows.Storage.IApplicationData3, folderName: WinRT_String) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def ClearPublisherCacheFolderAsync(self: Windows.Storage.IApplicationData3, folderName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_SharedLocalFolder(self: Windows.Storage.IApplicationData3) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetForUserAsync(cls: Windows.Storage.IApplicationDataStatics2, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Storage.ApplicationData]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.Storage.IApplicationDataStatics) -> Windows.Storage.ApplicationData: ...
    Version = property(get_Version, None)
    LocalSettings = property(get_LocalSettings, None)
    RoamingSettings = property(get_RoamingSettings, None)
    LocalFolder = property(get_LocalFolder, None)
    RoamingFolder = property(get_RoamingFolder, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    RoamingStorageQuota = property(get_RoamingStorageQuota, None)
    LocalCacheFolder = property(get_LocalCacheFolder, None)
    SharedLocalFolder = property(get_SharedLocalFolder, None)
    _ApplicationData_Meta_.Current = property(get_Current.__wrapped__, None)
class ApplicationDataCompositeValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Storage.ApplicationDataCompositeValue'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.ApplicationDataCompositeValue: ...
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class ApplicationDataContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IApplicationDataContainer
    _classid_ = 'Windows.Storage.ApplicationDataContainer'
    @winrt_mixinmethod
    def get_Name(self: Windows.Storage.IApplicationDataContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Locality(self: Windows.Storage.IApplicationDataContainer) -> Windows.Storage.ApplicationDataLocality: ...
    @winrt_mixinmethod
    def get_Values(self: Windows.Storage.IApplicationDataContainer) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_Containers(self: Windows.Storage.IApplicationDataContainer) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.ApplicationDataContainer]: ...
    @winrt_mixinmethod
    def CreateContainer(self: Windows.Storage.IApplicationDataContainer, name: WinRT_String, disposition: Windows.Storage.ApplicationDataCreateDisposition) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def DeleteContainer(self: Windows.Storage.IApplicationDataContainer, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Name = property(get_Name, None)
    Locality = property(get_Locality, None)
    Values = property(get_Values, None)
    Containers = property(get_Containers, None)
class ApplicationDataContainerSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IPropertySet
    _classid_ = 'Windows.Storage.ApplicationDataContainerSettings'
    @winrt_mixinmethod
    def add_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], vhnd: Windows.Foundation.Collections.MapChangedEventHandler[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapChanged(self: Windows.Foundation.Collections.IObservableMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
ApplicationDataCreateDisposition = Int32
ApplicationDataCreateDisposition_Always: ApplicationDataCreateDisposition = 0
ApplicationDataCreateDisposition_Existing: ApplicationDataCreateDisposition = 1
ApplicationDataLocality = Int32
ApplicationDataLocality_Local: ApplicationDataLocality = 0
ApplicationDataLocality_Roaming: ApplicationDataLocality = 1
ApplicationDataLocality_Temporary: ApplicationDataLocality = 2
ApplicationDataLocality_LocalCache: ApplicationDataLocality = 3
ApplicationDataLocality_SharedLocal: ApplicationDataLocality = 4
class ApplicationDataSetVersionHandler(MulticastDelegate):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a05791e6-cc9f-4687-acab-a364fd785463}')
    def Invoke(self, setVersionRequest: Windows.Storage.SetVersionRequest) -> Void: ...
class CachedFileManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.CachedFileManager'
    @winrt_classmethod
    def DeferUpdates(cls: Windows.Storage.ICachedFileManagerStatics, file: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_classmethod
    def CompleteUpdatesAsync(cls: Windows.Storage.ICachedFileManagerStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Provider.FileUpdateStatus]: ...
CreationCollisionOption = Int32
CreationCollisionOption_GenerateUniqueName: CreationCollisionOption = 0
CreationCollisionOption_ReplaceExisting: CreationCollisionOption = 1
CreationCollisionOption_FailIfExists: CreationCollisionOption = 2
CreationCollisionOption_OpenIfExists: CreationCollisionOption = 3
class DownloadsFolder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.DownloadsFolder'
    @winrt_classmethod
    def CreateFileForUserAsync(cls: Windows.Storage.IDownloadsFolderStatics2, user: Windows.System.User, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderForUserAsync(cls: Windows.Storage.IDownloadsFolderStatics2, user: Windows.System.User, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileForUserWithCollisionOptionAsync(cls: Windows.Storage.IDownloadsFolderStatics2, user: Windows.System.User, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderForUserWithCollisionOptionAsync(cls: Windows.Storage.IDownloadsFolderStatics2, user: Windows.System.User, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileAsync(cls: Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderAsync(cls: Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def CreateFileWithCollisionOptionAsync(cls: Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateFolderWithCollisionOptionAsync(cls: Windows.Storage.IDownloadsFolderStatics, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
FileAccessMode = Int32
FileAccessMode_Read: FileAccessMode = 0
FileAccessMode_ReadWrite: FileAccessMode = 1
FileAttributes = UInt32
FileAttributes_Normal: FileAttributes = 0
FileAttributes_ReadOnly: FileAttributes = 1
FileAttributes_Directory: FileAttributes = 16
FileAttributes_Archive: FileAttributes = 32
FileAttributes_Temporary: FileAttributes = 256
FileAttributes_LocallyIncomplete: FileAttributes = 512
class FileIO(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileIO'
    @winrt_classmethod
    def ReadTextAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReadTextWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def WriteTextAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteTextWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadLinesAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def ReadLinesWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def WriteLinesAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteLinesWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesWithEncodingAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadBufferAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def WriteBufferAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteBytesAsync(cls: Windows.Storage.IFileIOStatics, file: Windows.Storage.IStorageFile, buffer: POINTER(Byte)) -> Windows.Foundation.IAsyncAction: ...
class IAppDataPaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IAppDataPathsStatics'
    _iid_ = Guid('{d8eb2afe-a9d9-4b14-b999-e3921379d903}')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.Storage.AppDataPaths: ...
    @winrt_commethod(7)
    def GetDefault(self) -> Windows.Storage.AppDataPaths: ...
class IApplicationData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData'
    _iid_ = Guid('{c3da6fb7-b744-4b45-b0b8-223a0938d0dc}')
    @winrt_commethod(6)
    def get_Version(self) -> UInt32: ...
    @winrt_commethod(7)
    def SetVersionAsync(self, desiredVersion: UInt32, handler: Windows.Storage.ApplicationDataSetVersionHandler) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ClearAllAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ClearAsync(self, locality: Windows.Storage.ApplicationDataLocality) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def get_LocalSettings(self) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(11)
    def get_RoamingSettings(self) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(12)
    def get_LocalFolder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(13)
    def get_RoamingFolder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(14)
    def get_TemporaryFolder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(15)
    def add_DataChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.ApplicationData, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_DataChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def SignalDataChanged(self) -> Void: ...
    @winrt_commethod(18)
    def get_RoamingStorageQuota(self) -> UInt64: ...
    Version = property(get_Version, None)
    LocalSettings = property(get_LocalSettings, None)
    RoamingSettings = property(get_RoamingSettings, None)
    LocalFolder = property(get_LocalFolder, None)
    RoamingFolder = property(get_RoamingFolder, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    RoamingStorageQuota = property(get_RoamingStorageQuota, None)
class IApplicationData2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData2'
    _iid_ = Guid('{9e65cd69-0ba3-4e32-be29-b02de6607638}')
    @winrt_commethod(6)
    def get_LocalCacheFolder(self) -> Windows.Storage.StorageFolder: ...
    LocalCacheFolder = property(get_LocalCacheFolder, None)
class IApplicationData3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationData3'
    _iid_ = Guid('{dc222cf4-2772-4c1d-aa2c-c9f743ade8d1}')
    @winrt_commethod(6)
    def GetPublisherCacheFolder(self, folderName: WinRT_String) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def ClearPublisherCacheFolderAsync(self, folderName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_SharedLocalFolder(self) -> Windows.Storage.StorageFolder: ...
    SharedLocalFolder = property(get_SharedLocalFolder, None)
class IApplicationDataContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataContainer'
    _iid_ = Guid('{c5aefd1e-f467-40ba-8566-ab640a441e1d}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Locality(self) -> Windows.Storage.ApplicationDataLocality: ...
    @winrt_commethod(8)
    def get_Values(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def get_Containers(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.ApplicationDataContainer]: ...
    @winrt_commethod(10)
    def CreateContainer(self, name: WinRT_String, disposition: Windows.Storage.ApplicationDataCreateDisposition) -> Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(11)
    def DeleteContainer(self, name: WinRT_String) -> Void: ...
    Name = property(get_Name, None)
    Locality = property(get_Locality, None)
    Values = property(get_Values, None)
    Containers = property(get_Containers, None)
class IApplicationDataStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataStatics'
    _iid_ = Guid('{5612147b-e843-45e3-94d8-06169e3c8e17}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Storage.ApplicationData: ...
    Current = property(get_Current, None)
class IApplicationDataStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IApplicationDataStatics2'
    _iid_ = Guid('{cd606211-cf49-40a4-a47c-c7f0dbba8107}')
    @winrt_commethod(6)
    def GetForUserAsync(self, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Windows.Storage.ApplicationData]: ...
class ICachedFileManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ICachedFileManagerStatics'
    _iid_ = Guid('{8ffc224a-e782-495d-b614-654c4f0b2370}')
    @winrt_commethod(6)
    def DeferUpdates(self, file: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(7)
    def CompleteUpdatesAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Provider.FileUpdateStatus]: ...
class IDownloadsFolderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IDownloadsFolderStatics'
    _iid_ = Guid('{27862ed0-404e-47df-a1e2-e37308be7b37}')
    @winrt_commethod(6)
    def CreateFileAsync(self, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFolderAsync(self, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(8)
    def CreateFileWithCollisionOptionAsync(self, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def CreateFolderWithCollisionOptionAsync(self, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IDownloadsFolderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IDownloadsFolderStatics2'
    _iid_ = Guid('{e93045bd-8ef8-4f8e-8d15-ac0e265f390d}')
    @winrt_commethod(6)
    def CreateFileForUserAsync(self, user: Windows.System.User, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFolderForUserAsync(self, user: Windows.System.User, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(8)
    def CreateFileForUserWithCollisionOptionAsync(self, user: Windows.System.User, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def CreateFolderForUserWithCollisionOptionAsync(self, user: Windows.System.User, desiredName: WinRT_String, option: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IFileIOStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IFileIOStatics'
    _iid_ = Guid('{887411eb-7f54-4732-a5f0-5e43e3b8c2f5}')
    @winrt_commethod(6)
    def ReadTextAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def ReadTextWithEncodingAsync(self, file: Windows.Storage.IStorageFile, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def WriteTextAsync(self, file: Windows.Storage.IStorageFile, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def WriteTextWithEncodingAsync(self, file: Windows.Storage.IStorageFile, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def AppendTextAsync(self, file: Windows.Storage.IStorageFile, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def AppendTextWithEncodingAsync(self, file: Windows.Storage.IStorageFile, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReadLinesAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(13)
    def ReadLinesWithEncodingAsync(self, file: Windows.Storage.IStorageFile, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(14)
    def WriteLinesAsync(self, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def WriteLinesWithEncodingAsync(self, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def AppendLinesAsync(self, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AppendLinesWithEncodingAsync(self, file: Windows.Storage.IStorageFile, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReadBufferAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(19)
    def WriteBufferAsync(self, file: Windows.Storage.IStorageFile, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def WriteBytesAsync(self, file: Windows.Storage.IStorageFile, buffer: POINTER(Byte)) -> Windows.Foundation.IAsyncAction: ...
class IKnownFoldersCameraRollStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersCameraRollStatics'
    _iid_ = Guid('{5d115e66-27e8-492f-b8e5-2f90896cd4cd}')
    @winrt_commethod(6)
    def get_CameraRoll(self) -> Windows.Storage.StorageFolder: ...
    CameraRoll = property(get_CameraRoll, None)
class IKnownFoldersPlaylistsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersPlaylistsStatics'
    _iid_ = Guid('{dad5ecd6-306f-4d6a-b496-46ba8eb106ce}')
    @winrt_commethod(6)
    def get_Playlists(self) -> Windows.Storage.StorageFolder: ...
    Playlists = property(get_Playlists, None)
class IKnownFoldersSavedPicturesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersSavedPicturesStatics'
    _iid_ = Guid('{055c93ea-253d-467c-b6ca-a97da1e9a18d}')
    @winrt_commethod(6)
    def get_SavedPictures(self) -> Windows.Storage.StorageFolder: ...
    SavedPictures = property(get_SavedPictures, None)
class IKnownFoldersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics'
    _iid_ = Guid('{5a2a7520-4802-452d-9ad9-4351ada7ec35}')
    @winrt_commethod(6)
    def get_MusicLibrary(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_PicturesLibrary(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_VideosLibrary(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(9)
    def get_DocumentsLibrary(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(10)
    def get_HomeGroup(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(11)
    def get_RemovableDevices(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(12)
    def get_MediaServerDevices(self) -> Windows.Storage.StorageFolder: ...
    MusicLibrary = property(get_MusicLibrary, None)
    PicturesLibrary = property(get_PicturesLibrary, None)
    VideosLibrary = property(get_VideosLibrary, None)
    DocumentsLibrary = property(get_DocumentsLibrary, None)
    HomeGroup = property(get_HomeGroup, None)
    RemovableDevices = property(get_RemovableDevices, None)
    MediaServerDevices = property(get_MediaServerDevices, None)
class IKnownFoldersStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics2'
    _iid_ = Guid('{194bd0cd-cf6e-4d07-9d53-e9163a2536e9}')
    @winrt_commethod(6)
    def get_Objects3D(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(7)
    def get_AppCaptures(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(8)
    def get_RecordedCalls(self) -> Windows.Storage.StorageFolder: ...
    Objects3D = property(get_Objects3D, None)
    AppCaptures = property(get_AppCaptures, None)
    RecordedCalls = property(get_RecordedCalls, None)
class IKnownFoldersStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics3'
    _iid_ = Guid('{c5194341-9742-4ed5-823d-fc1401148764}')
    @winrt_commethod(6)
    def GetFolderForUserAsync(self, user: Windows.System.User, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IKnownFoldersStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IKnownFoldersStatics4'
    _iid_ = Guid('{1722e6bf-9ff9-4b21-bed5-90ecb13a192e}')
    @winrt_commethod(6)
    def RequestAccessAsync(self, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_commethod(7)
    def RequestAccessForUserAsync(self, user: Windows.System.User, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_commethod(8)
    def GetFolderAsync(self, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IPathIOStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IPathIOStatics'
    _iid_ = Guid('{0f2f3758-8ec7-4381-922b-8f6c07d288f3}')
    @winrt_commethod(6)
    def ReadTextAsync(self, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def ReadTextWithEncodingAsync(self, absolutePath: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def WriteTextAsync(self, absolutePath: WinRT_String, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def WriteTextWithEncodingAsync(self, absolutePath: WinRT_String, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def AppendTextAsync(self, absolutePath: WinRT_String, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def AppendTextWithEncodingAsync(self, absolutePath: WinRT_String, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReadLinesAsync(self, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(13)
    def ReadLinesWithEncodingAsync(self, absolutePath: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(14)
    def WriteLinesAsync(self, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def WriteLinesWithEncodingAsync(self, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def AppendLinesAsync(self, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def AppendLinesWithEncodingAsync(self, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReadBufferAsync(self, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(19)
    def WriteBufferAsync(self, absolutePath: WinRT_String, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def WriteBytesAsync(self, absolutePath: WinRT_String, buffer: POINTER(Byte)) -> Windows.Foundation.IAsyncAction: ...
class ISetVersionDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISetVersionDeferral'
    _iid_ = Guid('{033508a2-781a-437a-b078-3f32badcfe47}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISetVersionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISetVersionRequest'
    _iid_ = Guid('{b9c76b9b-1056-4e69-8330-162619956f9b}')
    @winrt_commethod(6)
    def get_CurrentVersion(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_DesiredVersion(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Storage.SetVersionDeferral: ...
    CurrentVersion = property(get_CurrentVersion, None)
    DesiredVersion = property(get_DesiredVersion, None)
class IStorageFile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFile'
    _iid_ = Guid('{fa3f6186-4214-428c-a64c-14c9ac7315ea}')
    @winrt_commethod(6)
    def get_FileType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def OpenAsync(self, accessMode: Windows.Storage.FileAccessMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(9)
    def OpenTransactedWriteAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageStreamTransaction]: ...
    @winrt_commethod(10)
    def CopyOverloadDefaultNameAndOptions(self, destinationFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def CopyOverloadDefaultOptions(self, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def CopyOverload(self, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(13)
    def CopyAndReplaceAsync(self, fileToReplace: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def MoveOverloadDefaultNameAndOptions(self, destinationFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def MoveOverloadDefaultOptions(self, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def MoveOverload(self, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def MoveAndReplaceAsync(self, fileToReplace: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    FileType = property(get_FileType, None)
    ContentType = property(get_ContentType, None)
class IStorageFile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFile2'
    _iid_ = Guid('{954e4bcf-0a77-42fb-b777-c2ed58a52e44}')
    @winrt_commethod(6)
    def OpenWithOptionsAsync(self, accessMode: Windows.Storage.FileAccessMode, options: Windows.Storage.StorageOpenOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(7)
    def OpenTransactedWriteWithOptionsAsync(self, options: Windows.Storage.StorageOpenOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageStreamTransaction]: ...
class IStorageFilePropertiesWithAvailability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFilePropertiesWithAvailability'
    _iid_ = Guid('{afcbbe9b-582b-4133-9648-e44ca46ee491}')
    @winrt_commethod(6)
    def get_IsAvailable(self) -> Boolean: ...
    IsAvailable = property(get_IsAvailable, None)
class IStorageFileStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFileStatics'
    _iid_ = Guid('{5984c710-daf2-43c8-8bb4-a4d3eacfd03f}')
    @winrt_commethod(6)
    def GetFileFromPathAsync(self, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def GetFileFromApplicationUriAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def CreateStreamedFileAsync(self, displayNameWithExtension: WinRT_String, dataRequested: Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def ReplaceWithStreamedFileAsync(self, fileToReplace: Windows.Storage.IStorageFile, dataRequested: Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(10)
    def CreateStreamedFileFromUriAsync(self, displayNameWithExtension: WinRT_String, uri: Windows.Foundation.Uri, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def ReplaceWithStreamedFileFromUriAsync(self, fileToReplace: Windows.Storage.IStorageFile, uri: Windows.Foundation.Uri, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
class IStorageFileStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFileStatics2'
    _iid_ = Guid('{5c76a781-212e-4af9-8f04-740cae108974}')
    @winrt_commethod(6)
    def GetFileFromPathForUserAsync(self, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
class IStorageFolder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder'
    _iid_ = Guid('{72d1cb78-b3ef-4f75-a80b-6fd9dae2944b}')
    @winrt_commethod(6)
    def CreateFileAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def CreateFileAsync(self, desiredName: WinRT_String, options: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def CreateFolderAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def CreateFolderAsync(self, desiredName: WinRT_String, options: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(10)
    def GetFileAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(11)
    def GetFolderAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(12)
    def GetItemAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_commethod(13)
    def GetFilesAsyncOverloadDefaultOptionsStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_commethod(14)
    def GetFoldersAsyncOverloadDefaultOptionsStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_commethod(15)
    def GetItemsAsyncOverloadDefaultStartAndCount(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
class IStorageFolder2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder2'
    _iid_ = Guid('{e827e8b9-08d9-4a8e-a0ac-fe5ed3cbbbd3}')
    @winrt_commethod(6)
    def TryGetItemAsync(self, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
class IStorageFolder3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolder3'
    _iid_ = Guid('{9f617899-bde1-4124-aeb3-b06ad96f98d4}')
    @winrt_commethod(6)
    def TryGetChangeTracker(self) -> Windows.Storage.StorageLibraryChangeTracker: ...
class IStorageFolderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolderStatics'
    _iid_ = Guid('{08f327ff-85d5-48b9-aee9-28511e339f9f}')
    @winrt_commethod(6)
    def GetFolderFromPathAsync(self, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IStorageFolderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageFolderStatics2'
    _iid_ = Guid('{b4656dc3-71d2-467d-8b29-371f0f62bf6f}')
    @winrt_commethod(6)
    def GetFolderFromPathForUserAsync(self, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
class IStorageItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItem'
    _iid_ = Guid('{4207a996-ca2f-42f7-bde8-8b10457a7f30}')
    @winrt_commethod(6)
    def RenameAsyncOverloadDefaultOptions(self, desiredName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RenameAsync(self, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAsyncOverloadDefaultOptions(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DeleteAsync(self, option: Windows.Storage.StorageDeleteOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def GetBasicPropertiesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_commethod(11)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Attributes(self) -> Windows.Storage.FileAttributes: ...
    @winrt_commethod(14)
    def get_DateCreated(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(15)
    def IsOfType(self, type: Windows.Storage.StorageItemTypes) -> Boolean: ...
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
class IStorageItem2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItem2'
    _iid_ = Guid('{53f926d2-083c-4283-b45b-81c007237e44}')
    @winrt_commethod(6)
    def GetParentAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(7)
    def IsEqual(self, item: Windows.Storage.IStorageItem) -> Boolean: ...
class IStorageItemProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemProperties'
    _iid_ = Guid('{86664478-8029-46fe-a789-1c2f3e2ffb5c}')
    @winrt_commethod(6)
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(7)
    def GetThumbnailAsyncOverloadDefaultOptions(self, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(8)
    def GetThumbnailAsync(self, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DisplayType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_FolderRelativeId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Properties(self) -> Windows.Storage.FileProperties.StorageItemContentProperties: ...
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
class IStorageItemProperties2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemProperties2'
    _iid_ = Guid('{8e86a951-04b9-4bd2-929d-fef3f71621d0}')
    @winrt_commethod(6)
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(7)
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_commethod(8)
    def GetScaledImageAsThumbnailAsync(self, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
class IStorageItemPropertiesWithProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageItemPropertiesWithProvider'
    _iid_ = Guid('{861bf39b-6368-4dee-b40e-74684a5ce714}')
    @winrt_commethod(6)
    def get_Provider(self) -> Windows.Storage.StorageProvider: ...
    Provider = property(get_Provider, None)
class IStorageLibrary(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary'
    _iid_ = Guid('{1edd7103-0e5e-4d6c-b5e8-9318983d6a03}')
    @winrt_commethod(6)
    def RequestAddFolderAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(7)
    def RequestRemoveFolderAsync(self, folder: Windows.Storage.StorageFolder) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def get_Folders(self) -> Windows.Foundation.Collections.IObservableVector[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(9)
    def get_SaveFolder(self) -> Windows.Storage.StorageFolder: ...
    @winrt_commethod(10)
    def add_DefinitionChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.StorageLibrary, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DefinitionChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Folders = property(get_Folders, None)
    SaveFolder = property(get_SaveFolder, None)
class IStorageLibrary2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary2'
    _iid_ = Guid('{5b0ce348-fcb3-4031-afb0-a68d7bd44534}')
    @winrt_commethod(6)
    def get_ChangeTracker(self) -> Windows.Storage.StorageLibraryChangeTracker: ...
    ChangeTracker = property(get_ChangeTracker, None)
class IStorageLibrary3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibrary3'
    _iid_ = Guid('{8a281291-2154-4201-8113-d2c05ce1ad23}')
    @winrt_commethod(6)
    def AreFolderSuggestionsAvailableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IStorageLibraryChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChange'
    _iid_ = Guid('{00980b23-2be2-4909-aa48-159f5203a51e}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> Windows.Storage.StorageLibraryChangeType: ...
    @winrt_commethod(7)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PreviousPath(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def IsOfType(self, type: Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_commethod(10)
    def GetStorageItemAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    ChangeType = property(get_ChangeType, None)
    Path = property(get_Path, None)
    PreviousPath = property(get_PreviousPath, None)
class IStorageLibraryChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeReader'
    _iid_ = Guid('{f205bc83-fca2-41f9-8954-ee2e991eb96f}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageLibraryChange]]: ...
    @winrt_commethod(7)
    def AcceptChangesAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IStorageLibraryChangeReader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeReader2'
    _iid_ = Guid('{abf4868b-fbcc-4a4f-999e-e7ab7c646dbe}')
    @winrt_commethod(6)
    def GetLastChangeId(self) -> UInt64: ...
class IStorageLibraryChangeTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTracker'
    _iid_ = Guid('{9e157316-6073-44f6-9681-7492d1286c90}')
    @winrt_commethod(6)
    def GetChangeReader(self) -> Windows.Storage.StorageLibraryChangeReader: ...
    @winrt_commethod(7)
    def Enable(self) -> Void: ...
    @winrt_commethod(8)
    def Reset(self) -> Void: ...
class IStorageLibraryChangeTracker2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTracker2'
    _iid_ = Guid('{cd051c3b-0f9f-42f9-8fb3-158d82e13821}')
    @winrt_commethod(6)
    def EnableWithOptions(self, options: Windows.Storage.StorageLibraryChangeTrackerOptions) -> Void: ...
    @winrt_commethod(7)
    def Disable(self) -> Void: ...
class IStorageLibraryChangeTrackerOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryChangeTrackerOptions'
    _iid_ = Guid('{bb52bcd4-1a6d-59c0-ad2a-823a20532483}')
    @winrt_commethod(6)
    def get_TrackChangeDetails(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_TrackChangeDetails(self, value: Boolean) -> Void: ...
    TrackChangeDetails = property(get_TrackChangeDetails, put_TrackChangeDetails)
class IStorageLibraryLastChangeId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryLastChangeId'
    _iid_ = Guid('{5281826a-bbe1-53bc-82ca-81cc7f039329}')
class IStorageLibraryLastChangeIdStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryLastChangeIdStatics'
    _iid_ = Guid('{81a49128-2ca3-5309-b0d1-cf0788e40762}')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt64: ...
    Unknown = property(get_Unknown, None)
class IStorageLibraryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryStatics'
    _iid_ = Guid('{4208a6db-684a-49c6-9e59-90121ee050d6}')
    @winrt_commethod(6)
    def GetLibraryAsync(self, libraryId: Windows.Storage.KnownLibraryId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageLibrary]: ...
class IStorageLibraryStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageLibraryStatics2'
    _iid_ = Guid('{ffb08ddc-fa75-4695-b9d1-7f81f97832e3}')
    @winrt_commethod(6)
    def GetLibraryForUserAsync(self, user: Windows.System.User, libraryId: Windows.Storage.KnownLibraryId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageLibrary]: ...
class IStorageProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageProvider'
    _iid_ = Guid('{e705eed4-d478-47d6-ba46-1a8ebe114a20}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
class IStorageProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageProvider2'
    _iid_ = Guid('{010d1917-3404-414b-9fd7-cd44472eaa39}')
    @winrt_commethod(6)
    def IsPropertySupportedForPartialFileAsync(self, propertyCanonicalName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IStorageStreamTransaction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStorageStreamTransaction'
    _iid_ = Guid('{f67cf363-a53d-4d94-ae2c-67232d93acdd}')
    @winrt_commethod(6)
    def get_Stream(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(7)
    def CommitAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Stream = property(get_Stream, None)
class IStreamedFileDataRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IStreamedFileDataRequest'
    _iid_ = Guid('{1673fcce-dabd-4d50-beee-180b8a8191b6}')
    @winrt_commethod(6)
    def FailAndClose(self, failureMode: Windows.Storage.StreamedFileFailureMode) -> Void: ...
class ISystemAudioProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemAudioProperties'
    _iid_ = Guid('{3f8f38b7-308c-47e1-924d-8645348e5db7}')
    @winrt_commethod(6)
    def get_EncodingBitrate(self) -> WinRT_String: ...
    EncodingBitrate = property(get_EncodingBitrate, None)
class ISystemDataPaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    SystemHost = property(get_SystemHost, None)
    SystemX86 = property(get_SystemX86, None)
    SystemX64 = property(get_SystemX64, None)
    SystemArm = property(get_SystemArm, None)
    UserProfiles = property(get_UserProfiles, None)
    Windows = property(get_Windows, None)
class ISystemDataPathsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemDataPathsStatics'
    _iid_ = Guid('{e0f96fd0-9920-4bca-b379-f96fdf7caad8}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Storage.SystemDataPaths: ...
class ISystemGPSProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemGPSProperties'
    _iid_ = Guid('{c0f46eb4-c174-481a-bc25-921986f6a6f3}')
    @winrt_commethod(6)
    def get_LatitudeDecimal(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LongitudeDecimal(self) -> WinRT_String: ...
    LatitudeDecimal = property(get_LatitudeDecimal, None)
    LongitudeDecimal = property(get_LongitudeDecimal, None)
class ISystemImageProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.ISystemImageProperties'
    _iid_ = Guid('{011b2e30-8b39-4308-bea1-e8aa61e47826}')
    @winrt_commethod(6)
    def get_HorizontalSize(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VerticalSize(self) -> WinRT_String: ...
    HorizontalSize = property(get_HorizontalSize, None)
    VerticalSize = property(get_VerticalSize, None)
class ISystemMediaProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_Audio(self) -> Windows.Storage.SystemAudioProperties: ...
    @winrt_commethod(13)
    def get_GPS(self) -> Windows.Storage.SystemGPSProperties: ...
    @winrt_commethod(14)
    def get_Media(self) -> Windows.Storage.SystemMediaProperties: ...
    @winrt_commethod(15)
    def get_Music(self) -> Windows.Storage.SystemMusicProperties: ...
    @winrt_commethod(16)
    def get_Photo(self) -> Windows.Storage.SystemPhotoProperties: ...
    @winrt_commethod(17)
    def get_Video(self) -> Windows.Storage.SystemVideoProperties: ...
    @winrt_commethod(18)
    def get_Image(self) -> Windows.Storage.SystemImageProperties: ...
    Author = property(get_Author, None)
    Comment = property(get_Comment, None)
    ItemNameDisplay = property(get_ItemNameDisplay, None)
    Keywords = property(get_Keywords, None)
    Rating = property(get_Rating, None)
    Title = property(get_Title, None)
    Audio = property(get_Audio, None)
    GPS = property(get_GPS, None)
    Media = property(get_Media, None)
    Music = property(get_Music, None)
    Photo = property(get_Photo, None)
    Video = property(get_Video, None)
    Image = property(get_Image, None)
class ISystemVideoProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.IUserDataPathsStatics'
    _iid_ = Guid('{01b29def-e062-48a1-8b0c-f2c7a9ca56c0}')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.Storage.UserDataPaths: ...
    @winrt_commethod(7)
    def GetDefault(self) -> Windows.Storage.UserDataPaths: ...
KnownFolderId = Int32
KnownFolderId_AppCaptures: KnownFolderId = 0
KnownFolderId_CameraRoll: KnownFolderId = 1
KnownFolderId_DocumentsLibrary: KnownFolderId = 2
KnownFolderId_HomeGroup: KnownFolderId = 3
KnownFolderId_MediaServerDevices: KnownFolderId = 4
KnownFolderId_MusicLibrary: KnownFolderId = 5
KnownFolderId_Objects3D: KnownFolderId = 6
KnownFolderId_PicturesLibrary: KnownFolderId = 7
KnownFolderId_Playlists: KnownFolderId = 8
KnownFolderId_RecordedCalls: KnownFolderId = 9
KnownFolderId_RemovableDevices: KnownFolderId = 10
KnownFolderId_SavedPictures: KnownFolderId = 11
KnownFolderId_Screenshots: KnownFolderId = 12
KnownFolderId_VideosLibrary: KnownFolderId = 13
KnownFolderId_AllAppMods: KnownFolderId = 14
KnownFolderId_CurrentAppMods: KnownFolderId = 15
KnownFolderId_DownloadsFolder: KnownFolderId = 16
class _KnownFolders_Meta_(ComPtr.__class__):
    pass
class KnownFolders(ComPtr, metaclass=_KnownFolders_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.KnownFolders'
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Storage.IKnownFoldersStatics4, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_classmethod
    def RequestAccessForUserAsync(cls: Windows.Storage.IKnownFoldersStatics4, user: Windows.System.User, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.KnownFoldersAccessStatus]: ...
    @winrt_classmethod
    def GetFolderAsync(cls: Windows.Storage.IKnownFoldersStatics4, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def GetFolderForUserAsync(cls: Windows.Storage.IKnownFoldersStatics3, user: Windows.System.User, folderId: Windows.Storage.KnownFolderId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def get_Objects3D(cls: Windows.Storage.IKnownFoldersStatics2) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_AppCaptures(cls: Windows.Storage.IKnownFoldersStatics2) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_RecordedCalls(cls: Windows.Storage.IKnownFoldersStatics2) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_SavedPictures(cls: Windows.Storage.IKnownFoldersSavedPicturesStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_CameraRoll(cls: Windows.Storage.IKnownFoldersCameraRollStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_Playlists(cls: Windows.Storage.IKnownFoldersPlaylistsStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_MusicLibrary(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_PicturesLibrary(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_VideosLibrary(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_DocumentsLibrary(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_HomeGroup(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_RemovableDevices(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    @winrt_classmethod
    def get_MediaServerDevices(cls: Windows.Storage.IKnownFoldersStatics) -> Windows.Storage.StorageFolder: ...
    _KnownFolders_Meta_.Objects3D = property(get_Objects3D.__wrapped__, None)
    _KnownFolders_Meta_.AppCaptures = property(get_AppCaptures.__wrapped__, None)
    _KnownFolders_Meta_.RecordedCalls = property(get_RecordedCalls.__wrapped__, None)
    _KnownFolders_Meta_.SavedPictures = property(get_SavedPictures.__wrapped__, None)
    _KnownFolders_Meta_.CameraRoll = property(get_CameraRoll.__wrapped__, None)
    _KnownFolders_Meta_.Playlists = property(get_Playlists.__wrapped__, None)
    _KnownFolders_Meta_.MusicLibrary = property(get_MusicLibrary.__wrapped__, None)
    _KnownFolders_Meta_.PicturesLibrary = property(get_PicturesLibrary.__wrapped__, None)
    _KnownFolders_Meta_.VideosLibrary = property(get_VideosLibrary.__wrapped__, None)
    _KnownFolders_Meta_.DocumentsLibrary = property(get_DocumentsLibrary.__wrapped__, None)
    _KnownFolders_Meta_.HomeGroup = property(get_HomeGroup.__wrapped__, None)
    _KnownFolders_Meta_.RemovableDevices = property(get_RemovableDevices.__wrapped__, None)
    _KnownFolders_Meta_.MediaServerDevices = property(get_MediaServerDevices.__wrapped__, None)
KnownFoldersAccessStatus = Int32
KnownFoldersAccessStatus_DeniedBySystem: KnownFoldersAccessStatus = 0
KnownFoldersAccessStatus_NotDeclaredByApp: KnownFoldersAccessStatus = 1
KnownFoldersAccessStatus_DeniedByUser: KnownFoldersAccessStatus = 2
KnownFoldersAccessStatus_UserPromptRequired: KnownFoldersAccessStatus = 3
KnownFoldersAccessStatus_Allowed: KnownFoldersAccessStatus = 4
KnownFoldersAccessStatus_AllowedPerAppFolder: KnownFoldersAccessStatus = 5
KnownLibraryId = Int32
KnownLibraryId_Music: KnownLibraryId = 0
KnownLibraryId_Pictures: KnownLibraryId = 1
KnownLibraryId_Videos: KnownLibraryId = 2
KnownLibraryId_Documents: KnownLibraryId = 3
NameCollisionOption = Int32
NameCollisionOption_GenerateUniqueName: NameCollisionOption = 0
NameCollisionOption_ReplaceExisting: NameCollisionOption = 1
NameCollisionOption_FailIfExists: NameCollisionOption = 2
class PathIO(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.PathIO'
    @winrt_classmethod
    def ReadTextAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def ReadTextWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def WriteTextAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteTextWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendTextWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, contents: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadLinesAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def ReadLinesWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_classmethod
    def WriteLinesAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteLinesWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AppendLinesWithEncodingAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, lines: Windows.Foundation.Collections.IIterable[WinRT_String], encoding: Windows.Storage.Streams.UnicodeEncoding) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ReadBufferAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_classmethod
    def WriteBufferAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def WriteBytesAsync(cls: Windows.Storage.IPathIOStatics, absolutePath: WinRT_String, buffer: POINTER(Byte)) -> Windows.Foundation.IAsyncAction: ...
class SetVersionDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISetVersionDeferral
    _classid_ = 'Windows.Storage.SetVersionDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Storage.ISetVersionDeferral) -> Void: ...
class SetVersionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISetVersionRequest
    _classid_ = 'Windows.Storage.SetVersionRequest'
    @winrt_mixinmethod
    def get_CurrentVersion(self: Windows.Storage.ISetVersionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_DesiredVersion(self: Windows.Storage.ISetVersionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Storage.ISetVersionRequest) -> Windows.Storage.SetVersionDeferral: ...
    CurrentVersion = property(get_CurrentVersion, None)
    DesiredVersion = property(get_DesiredVersion, None)
StorageDeleteOption = Int32
StorageDeleteOption_Default: StorageDeleteOption = 0
StorageDeleteOption_PermanentDelete: StorageDeleteOption = 1
class StorageFile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageFile
    _classid_ = 'Windows.Storage.StorageFile'
    @winrt_mixinmethod
    def get_FileType(self: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def OpenAsync(self: Windows.Storage.IStorageFile, accessMode: Windows.Storage.FileAccessMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteAsync(self: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageStreamTransaction]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultNameAndOptions(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverloadDefaultOptions(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyOverload(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CopyAndReplaceAsync(self: Windows.Storage.IStorageFile, fileToReplace: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultNameAndOptions(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverloadDefaultOptions(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveOverload(self: Windows.Storage.IStorageFile, destinationFolder: Windows.Storage.IStorageFolder, desiredNewName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MoveAndReplaceAsync(self: Windows.Storage.IStorageFile, fileToReplace: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItem, desiredName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: Windows.Storage.IStorageItem, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.Storage.IStorageItem, option: Windows.Storage.StorageDeleteOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: Windows.Storage.IStorageItem) -> Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: Windows.Storage.IStorageItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: Windows.Storage.IStorageItem, type: Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def OpenReadAsync(self: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def OpenSequentialReadAsync(self: Windows.Storage.Streams.IInputStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IInputStream]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Storage.IStorageItemProperties) -> Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsync(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetParentAsync(self: Windows.Storage.IStorageItem2) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Storage.IStorageItem2, item: Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Provider(self: Windows.Storage.IStorageItemPropertiesWithProvider) -> Windows.Storage.StorageProvider: ...
    @winrt_mixinmethod
    def get_IsAvailable(self: Windows.Storage.IStorageFilePropertiesWithAvailability) -> Boolean: ...
    @winrt_mixinmethod
    def OpenWithOptionsAsync(self: Windows.Storage.IStorageFile2, accessMode: Windows.Storage.FileAccessMode, options: Windows.Storage.StorageOpenOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def OpenTransactedWriteWithOptionsAsync(self: Windows.Storage.IStorageFile2, options: Windows.Storage.StorageOpenOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageStreamTransaction]: ...
    @winrt_classmethod
    def GetFileFromPathForUserAsync(cls: Windows.Storage.IStorageFileStatics2, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def GetFileFromPathAsync(cls: Windows.Storage.IStorageFileStatics, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def GetFileFromApplicationUriAsync(cls: Windows.Storage.IStorageFileStatics, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateStreamedFileAsync(cls: Windows.Storage.IStorageFileStatics, displayNameWithExtension: WinRT_String, dataRequested: Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def ReplaceWithStreamedFileAsync(cls: Windows.Storage.IStorageFileStatics, fileToReplace: Windows.Storage.IStorageFile, dataRequested: Windows.Storage.StreamedFileDataRequestedHandler, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def CreateStreamedFileFromUriAsync(cls: Windows.Storage.IStorageFileStatics, displayNameWithExtension: WinRT_String, uri: Windows.Foundation.Uri, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def ReplaceWithStreamedFileFromUriAsync(cls: Windows.Storage.IStorageFileStatics, fileToReplace: Windows.Storage.IStorageFile, uri: Windows.Foundation.Uri, thumbnail: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    FileType = property(get_FileType, None)
    ContentType = property(get_ContentType, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
    IsAvailable = property(get_IsAvailable, None)
class StorageFolder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageFolder
    _classid_ = 'Windows.Storage.StorageFolder'
    @winrt_mixinmethod
    def CreateFileAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFileAsync(self: Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def CreateFolderAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageFolder, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def CreateFolderAsync(self: Windows.Storage.IStorageFolder, desiredName: WinRT_String, options: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: Windows.Storage.IStorageFolder, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: Windows.Storage.IStorageFolder, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemAsync(self: Windows.Storage.IStorageFolder, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultOptionsStartAndCount(self: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultOptionsStartAndCount(self: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsyncOverloadDefaultStartAndCount(self: Windows.Storage.IStorageFolder) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def RenameAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItem, desiredName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RenameAsync(self: Windows.Storage.IStorageItem, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.Storage.IStorageItem, option: Windows.Storage.StorageDeleteOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetBasicPropertiesAsync(self: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.BasicProperties]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Attributes(self: Windows.Storage.IStorageItem) -> Windows.Storage.FileAttributes: ...
    @winrt_mixinmethod
    def get_DateCreated(self: Windows.Storage.IStorageItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def IsOfType(self: Windows.Storage.IStorageItem, type: Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def GetIndexedStateAsync(self: Windows.Storage.Search.IStorageFolderQueryOperations) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Search.IndexedState]: ...
    @winrt_mixinmethod
    def CreateFileQueryOverloadDefault(self: Windows.Storage.Search.IStorageFolderQueryOperations) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQuery(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFileQuery) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFileQueryWithOptions(self: Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryOverloadDefault(self: Windows.Storage.Search.IStorageFolderQueryOperations) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQuery(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateFolderQueryWithOptions(self: Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageFolderQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQuery(self: Windows.Storage.Search.IStorageFolderQueryOperations) -> Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def CreateItemQueryWithOptions(self: Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: Windows.Storage.Search.QueryOptions) -> Windows.Storage.Search.StorageItemQueryResult: ...
    @winrt_mixinmethod
    def GetFilesAsync(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFileQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFilesAsyncOverloadDefaultStartAndCount(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFileQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]]: ...
    @winrt_mixinmethod
    def GetFoldersAsync(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFolderQuery, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetFoldersAsyncOverloadDefaultStartAndCount(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFolderQuery) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFolder]]: ...
    @winrt_mixinmethod
    def GetItemsAsync(self: Windows.Storage.Search.IStorageFolderQueryOperations, startIndex: UInt32, maxItemsToRetrieve: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def AreQueryOptionsSupported(self: Windows.Storage.Search.IStorageFolderQueryOperations, queryOptions: Windows.Storage.Search.QueryOptions) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFolderQuerySupported(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFolderQuery) -> Boolean: ...
    @winrt_mixinmethod
    def IsCommonFileQuerySupported(self: Windows.Storage.Search.IStorageFolderQueryOperations, query: Windows.Storage.Search.CommonFileQuery) -> Boolean: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetThumbnailAsync(self: Windows.Storage.IStorageItemProperties, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayType(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FolderRelativeId(self: Windows.Storage.IStorageItemProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Storage.IStorageItemProperties) -> Windows.Storage.FileProperties.StorageItemContentProperties: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsyncOverloadDefaultOptions(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetScaledImageAsThumbnailAsync(self: Windows.Storage.IStorageItemProperties2, mode: Windows.Storage.FileProperties.ThumbnailMode, requestedSize: UInt32, options: Windows.Storage.FileProperties.ThumbnailOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.FileProperties.StorageItemThumbnail]: ...
    @winrt_mixinmethod
    def GetParentAsync(self: Windows.Storage.IStorageItem2) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Storage.IStorageItem2, item: Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetItemAsync(self: Windows.Storage.IStorageFolder2, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Provider(self: Windows.Storage.IStorageItemPropertiesWithProvider) -> Windows.Storage.StorageProvider: ...
    @winrt_mixinmethod
    def TryGetChangeTracker(self: Windows.Storage.IStorageFolder3) -> Windows.Storage.StorageLibraryChangeTracker: ...
    @winrt_classmethod
    def GetFolderFromPathForUserAsync(cls: Windows.Storage.IStorageFolderStatics2, user: Windows.System.User, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_classmethod
    def GetFolderFromPathAsync(cls: Windows.Storage.IStorageFolderStatics, path: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    Attributes = property(get_Attributes, None)
    DateCreated = property(get_DateCreated, None)
    DisplayName = property(get_DisplayName, None)
    DisplayType = property(get_DisplayType, None)
    FolderRelativeId = property(get_FolderRelativeId, None)
    Properties = property(get_Properties, None)
    Provider = property(get_Provider, None)
StorageItemTypes = UInt32
StorageItemTypes_None: StorageItemTypes = 0
StorageItemTypes_File: StorageItemTypes = 1
StorageItemTypes_Folder: StorageItemTypes = 2
class StorageLibrary(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibrary
    _classid_ = 'Windows.Storage.StorageLibrary'
    @winrt_mixinmethod
    def RequestAddFolderAsync(self: Windows.Storage.IStorageLibrary) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def RequestRemoveFolderAsync(self: Windows.Storage.IStorageLibrary, folder: Windows.Storage.StorageFolder) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Folders(self: Windows.Storage.IStorageLibrary) -> Windows.Foundation.Collections.IObservableVector[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def get_SaveFolder(self: Windows.Storage.IStorageLibrary) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def add_DefinitionChanged(self: Windows.Storage.IStorageLibrary, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.StorageLibrary, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DefinitionChanged(self: Windows.Storage.IStorageLibrary, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ChangeTracker(self: Windows.Storage.IStorageLibrary2) -> Windows.Storage.StorageLibraryChangeTracker: ...
    @winrt_mixinmethod
    def AreFolderSuggestionsAvailableAsync(self: Windows.Storage.IStorageLibrary3) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetLibraryForUserAsync(cls: Windows.Storage.IStorageLibraryStatics2, user: Windows.System.User, libraryId: Windows.Storage.KnownLibraryId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageLibrary]: ...
    @winrt_classmethod
    def GetLibraryAsync(cls: Windows.Storage.IStorageLibraryStatics, libraryId: Windows.Storage.KnownLibraryId) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageLibrary]: ...
    Folders = property(get_Folders, None)
    SaveFolder = property(get_SaveFolder, None)
    ChangeTracker = property(get_ChangeTracker, None)
class StorageLibraryChange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibraryChange
    _classid_ = 'Windows.Storage.StorageLibraryChange'
    @winrt_mixinmethod
    def get_ChangeType(self: Windows.Storage.IStorageLibraryChange) -> Windows.Storage.StorageLibraryChangeType: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Storage.IStorageLibraryChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PreviousPath(self: Windows.Storage.IStorageLibraryChange) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsOfType(self: Windows.Storage.IStorageLibraryChange, type: Windows.Storage.StorageItemTypes) -> Boolean: ...
    @winrt_mixinmethod
    def GetStorageItemAsync(self: Windows.Storage.IStorageLibraryChange) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    ChangeType = property(get_ChangeType, None)
    Path = property(get_Path, None)
    PreviousPath = property(get_PreviousPath, None)
class StorageLibraryChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibraryChangeReader
    _classid_ = 'Windows.Storage.StorageLibraryChangeReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.Storage.IStorageLibraryChangeReader) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageLibraryChange]]: ...
    @winrt_mixinmethod
    def AcceptChangesAsync(self: Windows.Storage.IStorageLibraryChangeReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetLastChangeId(self: Windows.Storage.IStorageLibraryChangeReader2) -> UInt64: ...
class StorageLibraryChangeTracker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibraryChangeTracker
    _classid_ = 'Windows.Storage.StorageLibraryChangeTracker'
    @winrt_mixinmethod
    def GetChangeReader(self: Windows.Storage.IStorageLibraryChangeTracker) -> Windows.Storage.StorageLibraryChangeReader: ...
    @winrt_mixinmethod
    def Enable(self: Windows.Storage.IStorageLibraryChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def Reset(self: Windows.Storage.IStorageLibraryChangeTracker) -> Void: ...
    @winrt_mixinmethod
    def EnableWithOptions(self: Windows.Storage.IStorageLibraryChangeTracker2, options: Windows.Storage.StorageLibraryChangeTrackerOptions) -> Void: ...
    @winrt_mixinmethod
    def Disable(self: Windows.Storage.IStorageLibraryChangeTracker2) -> Void: ...
class StorageLibraryChangeTrackerOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibraryChangeTrackerOptions
    _classid_ = 'Windows.Storage.StorageLibraryChangeTrackerOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Storage.StorageLibraryChangeTrackerOptions: ...
    @winrt_mixinmethod
    def get_TrackChangeDetails(self: Windows.Storage.IStorageLibraryChangeTrackerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_TrackChangeDetails(self: Windows.Storage.IStorageLibraryChangeTrackerOptions, value: Boolean) -> Void: ...
    TrackChangeDetails = property(get_TrackChangeDetails, put_TrackChangeDetails)
StorageLibraryChangeType = Int32
StorageLibraryChangeType_Created: StorageLibraryChangeType = 0
StorageLibraryChangeType_Deleted: StorageLibraryChangeType = 1
StorageLibraryChangeType_MovedOrRenamed: StorageLibraryChangeType = 2
StorageLibraryChangeType_ContentsChanged: StorageLibraryChangeType = 3
StorageLibraryChangeType_MovedOutOfLibrary: StorageLibraryChangeType = 4
StorageLibraryChangeType_MovedIntoLibrary: StorageLibraryChangeType = 5
StorageLibraryChangeType_ContentsReplaced: StorageLibraryChangeType = 6
StorageLibraryChangeType_IndexingStatusChanged: StorageLibraryChangeType = 7
StorageLibraryChangeType_EncryptionChanged: StorageLibraryChangeType = 8
StorageLibraryChangeType_ChangeTrackingLost: StorageLibraryChangeType = 9
class _StorageLibraryLastChangeId_Meta_(ComPtr.__class__):
    pass
class StorageLibraryLastChangeId(ComPtr, metaclass=_StorageLibraryLastChangeId_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageLibraryLastChangeId
    _classid_ = 'Windows.Storage.StorageLibraryLastChangeId'
    @winrt_classmethod
    def get_Unknown(cls: Windows.Storage.IStorageLibraryLastChangeIdStatics) -> UInt64: ...
    _StorageLibraryLastChangeId_Meta_.Unknown = property(get_Unknown.__wrapped__, None)
StorageOpenOptions = UInt32
StorageOpenOptions_None: StorageOpenOptions = 0
StorageOpenOptions_AllowOnlyReaders: StorageOpenOptions = 1
StorageOpenOptions_AllowReadersAndWriters: StorageOpenOptions = 2
class StorageProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageProvider
    _classid_ = 'Windows.Storage.StorageProvider'
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.IStorageProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Storage.IStorageProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPropertySupportedForPartialFileAsync(self: Windows.Storage.IStorageProvider2, propertyCanonicalName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
class StorageStreamTransaction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IStorageStreamTransaction
    _classid_ = 'Windows.Storage.StorageStreamTransaction'
    @winrt_mixinmethod
    def get_Stream(self: Windows.Storage.IStorageStreamTransaction) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def CommitAsync(self: Windows.Storage.IStorageStreamTransaction) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Stream = property(get_Stream, None)
class StreamedFileDataRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.Streams.IOutputStream
    _classid_ = 'Windows.Storage.StreamedFileDataRequest'
    @winrt_mixinmethod
    def WriteAsync(self: Windows.Storage.Streams.IOutputStream, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def FailAndClose(self: Windows.Storage.IStreamedFileDataRequest, failureMode: Windows.Storage.StreamedFileFailureMode) -> Void: ...
class StreamedFileDataRequestedHandler(MulticastDelegate):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fef6a824-2fe1-4d07-a35b-b77c50b5f4cc}')
    def Invoke(self, stream: Windows.Storage.StreamedFileDataRequest) -> Void: ...
StreamedFileFailureMode = Int32
StreamedFileFailureMode_Failed: StreamedFileFailureMode = 0
StreamedFileFailureMode_CurrentlyUnavailable: StreamedFileFailureMode = 1
StreamedFileFailureMode_Incomplete: StreamedFileFailureMode = 2
class SystemAudioProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemAudioProperties
    _classid_ = 'Windows.Storage.SystemAudioProperties'
    @winrt_mixinmethod
    def get_EncodingBitrate(self: Windows.Storage.ISystemAudioProperties) -> WinRT_String: ...
    EncodingBitrate = property(get_EncodingBitrate, None)
class SystemDataPaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemDataPaths
    _classid_ = 'Windows.Storage.SystemDataPaths'
    @winrt_mixinmethod
    def get_Fonts(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProgramData(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Public(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDesktop(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDocuments(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicDownloads(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicMusic(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicPictures(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicVideos(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_System(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemHost(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemX86(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemX64(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SystemArm(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserProfiles(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Windows(self: Windows.Storage.ISystemDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Storage.ISystemDataPathsStatics) -> Windows.Storage.SystemDataPaths: ...
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
    SystemHost = property(get_SystemHost, None)
    SystemX86 = property(get_SystemX86, None)
    SystemX64 = property(get_SystemX64, None)
    SystemArm = property(get_SystemArm, None)
    UserProfiles = property(get_UserProfiles, None)
    Windows = property(get_Windows, None)
class SystemGPSProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemGPSProperties
    _classid_ = 'Windows.Storage.SystemGPSProperties'
    @winrt_mixinmethod
    def get_LatitudeDecimal(self: Windows.Storage.ISystemGPSProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LongitudeDecimal(self: Windows.Storage.ISystemGPSProperties) -> WinRT_String: ...
    LatitudeDecimal = property(get_LatitudeDecimal, None)
    LongitudeDecimal = property(get_LongitudeDecimal, None)
class SystemImageProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemImageProperties
    _classid_ = 'Windows.Storage.SystemImageProperties'
    @winrt_mixinmethod
    def get_HorizontalSize(self: Windows.Storage.ISystemImageProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VerticalSize(self: Windows.Storage.ISystemImageProperties) -> WinRT_String: ...
    HorizontalSize = property(get_HorizontalSize, None)
    VerticalSize = property(get_VerticalSize, None)
class SystemMediaProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemMediaProperties
    _classid_ = 'Windows.Storage.SystemMediaProperties'
    @winrt_mixinmethod
    def get_Duration(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Producer(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SubTitle(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Writer(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Year(self: Windows.Storage.ISystemMediaProperties) -> WinRT_String: ...
    Duration = property(get_Duration, None)
    Producer = property(get_Producer, None)
    Publisher = property(get_Publisher, None)
    SubTitle = property(get_SubTitle, None)
    Writer = property(get_Writer, None)
    Year = property(get_Year, None)
class SystemMusicProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemMusicProperties
    _classid_ = 'Windows.Storage.SystemMusicProperties'
    @winrt_mixinmethod
    def get_AlbumArtist(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AlbumTitle(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Artist(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Composer(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Conductor(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayArtist(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Genre(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TrackNumber(self: Windows.Storage.ISystemMusicProperties) -> WinRT_String: ...
    AlbumArtist = property(get_AlbumArtist, None)
    AlbumTitle = property(get_AlbumTitle, None)
    Artist = property(get_Artist, None)
    Composer = property(get_Composer, None)
    Conductor = property(get_Conductor, None)
    DisplayArtist = property(get_DisplayArtist, None)
    Genre = property(get_Genre, None)
    TrackNumber = property(get_TrackNumber, None)
class SystemPhotoProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemPhotoProperties
    _classid_ = 'Windows.Storage.SystemPhotoProperties'
    @winrt_mixinmethod
    def get_CameraManufacturer(self: Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CameraModel(self: Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateTaken(self: Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PeopleNames(self: Windows.Storage.ISystemPhotoProperties) -> WinRT_String: ...
    CameraManufacturer = property(get_CameraManufacturer, None)
    CameraModel = property(get_CameraModel, None)
    DateTaken = property(get_DateTaken, None)
    Orientation = property(get_Orientation, None)
    PeopleNames = property(get_PeopleNames, None)
class _SystemProperties_Meta_(ComPtr.__class__):
    pass
class SystemProperties(ComPtr, metaclass=_SystemProperties_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.SystemProperties'
    @winrt_classmethod
    def get_Author(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Comment(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_ItemNameDisplay(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Keywords(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rating(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Title(cls: Windows.Storage.ISystemProperties) -> WinRT_String: ...
    @winrt_classmethod
    def get_Audio(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemAudioProperties: ...
    @winrt_classmethod
    def get_GPS(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemGPSProperties: ...
    @winrt_classmethod
    def get_Media(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemMediaProperties: ...
    @winrt_classmethod
    def get_Music(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemMusicProperties: ...
    @winrt_classmethod
    def get_Photo(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemPhotoProperties: ...
    @winrt_classmethod
    def get_Video(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemVideoProperties: ...
    @winrt_classmethod
    def get_Image(cls: Windows.Storage.ISystemProperties) -> Windows.Storage.SystemImageProperties: ...
    _SystemProperties_Meta_.Author = property(get_Author.__wrapped__, None)
    _SystemProperties_Meta_.Comment = property(get_Comment.__wrapped__, None)
    _SystemProperties_Meta_.ItemNameDisplay = property(get_ItemNameDisplay.__wrapped__, None)
    _SystemProperties_Meta_.Keywords = property(get_Keywords.__wrapped__, None)
    _SystemProperties_Meta_.Rating = property(get_Rating.__wrapped__, None)
    _SystemProperties_Meta_.Title = property(get_Title.__wrapped__, None)
    _SystemProperties_Meta_.Audio = property(get_Audio.__wrapped__, None)
    _SystemProperties_Meta_.GPS = property(get_GPS.__wrapped__, None)
    _SystemProperties_Meta_.Media = property(get_Media.__wrapped__, None)
    _SystemProperties_Meta_.Music = property(get_Music.__wrapped__, None)
    _SystemProperties_Meta_.Photo = property(get_Photo.__wrapped__, None)
    _SystemProperties_Meta_.Video = property(get_Video.__wrapped__, None)
    _SystemProperties_Meta_.Image = property(get_Image.__wrapped__, None)
class SystemVideoProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.ISystemVideoProperties
    _classid_ = 'Windows.Storage.SystemVideoProperties'
    @winrt_mixinmethod
    def get_Director(self: Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameHeight(self: Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameWidth(self: Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TotalBitrate(self: Windows.Storage.ISystemVideoProperties) -> WinRT_String: ...
    Director = property(get_Director, None)
    FrameHeight = property(get_FrameHeight, None)
    FrameWidth = property(get_FrameWidth, None)
    Orientation = property(get_Orientation, None)
    TotalBitrate = property(get_TotalBitrate, None)
class UserDataPaths(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.IUserDataPaths
    _classid_ = 'Windows.Storage.UserDataPaths'
    @winrt_mixinmethod
    def get_CameraRoll(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Cookies(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Desktop(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Documents(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Downloads(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Favorites(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_History(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InternetCache(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppData(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalAppDataLow(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Music(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Pictures(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Profile(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Recent(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingAppData(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SavedPictures(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Screenshots(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Templates(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Videos(self: Windows.Storage.IUserDataPaths) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.Storage.IUserDataPathsStatics, user: Windows.System.User) -> Windows.Storage.UserDataPaths: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Storage.IUserDataPathsStatics) -> Windows.Storage.UserDataPaths: ...
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
make_head(_module, 'AppDataPaths')
make_head(_module, 'ApplicationData')
make_head(_module, 'ApplicationDataCompositeValue')
make_head(_module, 'ApplicationDataContainer')
make_head(_module, 'ApplicationDataContainerSettings')
make_head(_module, 'CachedFileManager')
make_head(_module, 'DownloadsFolder')
make_head(_module, 'FileIO')
make_head(_module, 'IAppDataPaths')
make_head(_module, 'IAppDataPathsStatics')
make_head(_module, 'IApplicationData')
make_head(_module, 'IApplicationData2')
make_head(_module, 'IApplicationData3')
make_head(_module, 'IApplicationDataContainer')
make_head(_module, 'IApplicationDataStatics')
make_head(_module, 'IApplicationDataStatics2')
make_head(_module, 'ICachedFileManagerStatics')
make_head(_module, 'IDownloadsFolderStatics')
make_head(_module, 'IDownloadsFolderStatics2')
make_head(_module, 'IFileIOStatics')
make_head(_module, 'IKnownFoldersCameraRollStatics')
make_head(_module, 'IKnownFoldersPlaylistsStatics')
make_head(_module, 'IKnownFoldersSavedPicturesStatics')
make_head(_module, 'IKnownFoldersStatics')
make_head(_module, 'IKnownFoldersStatics2')
make_head(_module, 'IKnownFoldersStatics3')
make_head(_module, 'IKnownFoldersStatics4')
make_head(_module, 'IPathIOStatics')
make_head(_module, 'ISetVersionDeferral')
make_head(_module, 'ISetVersionRequest')
make_head(_module, 'IStorageFile')
make_head(_module, 'IStorageFile2')
make_head(_module, 'IStorageFilePropertiesWithAvailability')
make_head(_module, 'IStorageFileStatics')
make_head(_module, 'IStorageFileStatics2')
make_head(_module, 'IStorageFolder')
make_head(_module, 'IStorageFolder2')
make_head(_module, 'IStorageFolder3')
make_head(_module, 'IStorageFolderStatics')
make_head(_module, 'IStorageFolderStatics2')
make_head(_module, 'IStorageItem')
make_head(_module, 'IStorageItem2')
make_head(_module, 'IStorageItemProperties')
make_head(_module, 'IStorageItemProperties2')
make_head(_module, 'IStorageItemPropertiesWithProvider')
make_head(_module, 'IStorageLibrary')
make_head(_module, 'IStorageLibrary2')
make_head(_module, 'IStorageLibrary3')
make_head(_module, 'IStorageLibraryChange')
make_head(_module, 'IStorageLibraryChangeReader')
make_head(_module, 'IStorageLibraryChangeReader2')
make_head(_module, 'IStorageLibraryChangeTracker')
make_head(_module, 'IStorageLibraryChangeTracker2')
make_head(_module, 'IStorageLibraryChangeTrackerOptions')
make_head(_module, 'IStorageLibraryLastChangeId')
make_head(_module, 'IStorageLibraryLastChangeIdStatics')
make_head(_module, 'IStorageLibraryStatics')
make_head(_module, 'IStorageLibraryStatics2')
make_head(_module, 'IStorageProvider')
make_head(_module, 'IStorageProvider2')
make_head(_module, 'IStorageStreamTransaction')
make_head(_module, 'IStreamedFileDataRequest')
make_head(_module, 'ISystemAudioProperties')
make_head(_module, 'ISystemDataPaths')
make_head(_module, 'ISystemDataPathsStatics')
make_head(_module, 'ISystemGPSProperties')
make_head(_module, 'ISystemImageProperties')
make_head(_module, 'ISystemMediaProperties')
make_head(_module, 'ISystemMusicProperties')
make_head(_module, 'ISystemPhotoProperties')
make_head(_module, 'ISystemProperties')
make_head(_module, 'ISystemVideoProperties')
make_head(_module, 'IUserDataPaths')
make_head(_module, 'IUserDataPathsStatics')
make_head(_module, 'KnownFolders')
make_head(_module, 'PathIO')
make_head(_module, 'SetVersionDeferral')
make_head(_module, 'SetVersionRequest')
make_head(_module, 'StorageFile')
make_head(_module, 'StorageFolder')
make_head(_module, 'StorageLibrary')
make_head(_module, 'StorageLibraryChange')
make_head(_module, 'StorageLibraryChangeReader')
make_head(_module, 'StorageLibraryChangeTracker')
make_head(_module, 'StorageLibraryChangeTrackerOptions')
make_head(_module, 'StorageLibraryLastChangeId')
make_head(_module, 'StorageProvider')
make_head(_module, 'StorageStreamTransaction')
make_head(_module, 'StreamedFileDataRequest')
make_head(_module, 'SystemAudioProperties')
make_head(_module, 'SystemDataPaths')
make_head(_module, 'SystemGPSProperties')
make_head(_module, 'SystemImageProperties')
make_head(_module, 'SystemMediaProperties')
make_head(_module, 'SystemMusicProperties')
make_head(_module, 'SystemPhotoProperties')
make_head(_module, 'SystemProperties')
make_head(_module, 'SystemVideoProperties')
make_head(_module, 'UserDataPaths')
