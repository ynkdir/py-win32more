from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.Storage
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class ApplicationData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.Storage.IApplicationData
    _classid_ = 'Microsoft.Windows.Storage.ApplicationData'
    @winrt_mixinmethod
    def get_IsMachinePathSupported(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> Boolean: ...
    @winrt_mixinmethod
    def get_LocalCachePath(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalPath(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MachinePath(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SharedLocalPath(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TemporaryPath(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalCacheFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_LocalFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_MachineFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_SharedLocalFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_TemporaryFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_LocalSettings(self: win32more.Microsoft.Windows.Storage.IApplicationData) -> win32more.Microsoft.Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def ClearAsync(self: win32more.Microsoft.Windows.Storage.IApplicationData, locality: win32more.Microsoft.Windows.Storage.ApplicationDataLocality) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearPublisherCacheFolderAsync(self: win32more.Microsoft.Windows.Storage.IApplicationData, folderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetPublisherCachePath(self: win32more.Microsoft.Windows.Storage.IApplicationData, folderName: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPublisherCacheFolder(self: win32more.Microsoft.Windows.Storage.IApplicationData, folderName: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Microsoft.Windows.Storage.IApplicationDataStatics) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Microsoft.Windows.Storage.IApplicationDataStatics, user: win32more.Windows.System.User) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...
    @winrt_classmethod
    def GetForPackageFamily(cls: win32more.Microsoft.Windows.Storage.IApplicationDataStatics, packageFamilyName: WinRT_String) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...
    IsMachinePathSupported = property(get_IsMachinePathSupported, None)
    LocalCacheFolder = property(get_LocalCacheFolder, None)
    LocalCachePath = property(get_LocalCachePath, None)
    LocalFolder = property(get_LocalFolder, None)
    LocalPath = property(get_LocalPath, None)
    LocalSettings = property(get_LocalSettings, None)
    MachineFolder = property(get_MachineFolder, None)
    MachinePath = property(get_MachinePath, None)
    SharedLocalFolder = property(get_SharedLocalFolder, None)
    SharedLocalPath = property(get_SharedLocalPath, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    TemporaryPath = property(get_TemporaryPath, None)
class ApplicationDataContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.Storage.IApplicationDataContainer
    _classid_ = 'Microsoft.Windows.Storage.ApplicationDataContainer'
    @winrt_mixinmethod
    def get_Containers(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.Windows.Storage.ApplicationDataContainer]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Locality(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer) -> win32more.Microsoft.Windows.Storage.ApplicationDataLocality: ...
    @winrt_mixinmethod
    def get_Values(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def CreateContainer(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer, name: WinRT_String, disposition: win32more.Microsoft.Windows.Storage.ApplicationDataCreateDisposition) -> win32more.Microsoft.Windows.Storage.ApplicationDataContainer: ...
    @winrt_mixinmethod
    def DeleteContainer(self: win32more.Microsoft.Windows.Storage.IApplicationDataContainer, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Containers = property(get_Containers, None)
    Locality = property(get_Locality, None)
    Name = property(get_Name, None)
    Values = property(get_Values, None)
ApplicationDataContract: UInt32 = 131072
class ApplicationDataCreateDisposition(Enum, Int32):
    Always = 0
    Existing = 1
class ApplicationDataLocality(Enum, Int32):
    Local = 0
    LocalCache = 3
    SharedLocal = 4
    Temporary = 2
    Machine = 1000
class IApplicationData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Storage.IApplicationData'
    _iid_ = Guid('{fc073ce2-2f7b-5214-95fa-530a3f9d1ea5}')
    @winrt_commethod(6)
    def get_IsMachinePathSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_LocalCachePath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LocalPath(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MachinePath(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SharedLocalPath(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_TemporaryPath(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_LocalCacheFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(13)
    def get_LocalFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(14)
    def get_MachineFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(15)
    def get_SharedLocalFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(16)
    def get_TemporaryFolder(self) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_commethod(17)
    def get_LocalSettings(self) -> win32more.Microsoft.Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(18)
    def ClearAsync(self, locality: win32more.Microsoft.Windows.Storage.ApplicationDataLocality) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def ClearPublisherCacheFolderAsync(self, folderName: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def GetPublisherCachePath(self, folderName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(21)
    def GetPublisherCacheFolder(self, folderName: WinRT_String) -> win32more.Windows.Storage.StorageFolder: ...
    IsMachinePathSupported = property(get_IsMachinePathSupported, None)
    LocalCacheFolder = property(get_LocalCacheFolder, None)
    LocalCachePath = property(get_LocalCachePath, None)
    LocalFolder = property(get_LocalFolder, None)
    LocalPath = property(get_LocalPath, None)
    LocalSettings = property(get_LocalSettings, None)
    MachineFolder = property(get_MachineFolder, None)
    MachinePath = property(get_MachinePath, None)
    SharedLocalFolder = property(get_SharedLocalFolder, None)
    SharedLocalPath = property(get_SharedLocalPath, None)
    TemporaryFolder = property(get_TemporaryFolder, None)
    TemporaryPath = property(get_TemporaryPath, None)
class IApplicationDataContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Storage.IApplicationDataContainer'
    _iid_ = Guid('{d1fa9c23-2e59-55d8-bd86-88c2fdc9e7c9}')
    @winrt_commethod(6)
    def get_Containers(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.Windows.Storage.ApplicationDataContainer]: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Locality(self) -> win32more.Microsoft.Windows.Storage.ApplicationDataLocality: ...
    @winrt_commethod(9)
    def get_Values(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(10)
    def CreateContainer(self, name: WinRT_String, disposition: win32more.Microsoft.Windows.Storage.ApplicationDataCreateDisposition) -> win32more.Microsoft.Windows.Storage.ApplicationDataContainer: ...
    @winrt_commethod(11)
    def DeleteContainer(self, name: WinRT_String) -> Void: ...
    Containers = property(get_Containers, None)
    Locality = property(get_Locality, None)
    Name = property(get_Name, None)
    Values = property(get_Values, None)
class IApplicationDataStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Storage.IApplicationDataStatics'
    _iid_ = Guid('{6a8b41f8-5560-56fb-86b0-d59e897d4d95}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...
    @winrt_commethod(8)
    def GetForPackageFamily(self, packageFamilyName: WinRT_String) -> win32more.Microsoft.Windows.Storage.ApplicationData: ...


make_ready(__name__)
