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
import Windows.Storage
import Windows.Storage.AccessCache
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
AccessCacheOptions = UInt32
AccessCacheOptions_None: AccessCacheOptions = 0
AccessCacheOptions_DisallowUserInput: AccessCacheOptions = 1
AccessCacheOptions_FastLocationsOnly: AccessCacheOptions = 2
AccessCacheOptions_UseReadOnlyCachedCopy: AccessCacheOptions = 4
AccessCacheOptions_SuppressAccessTimeUpdate: AccessCacheOptions = 8
class AccessListEntry(EasyCastStructure):
    Token: WinRT_String
    Metadata: WinRT_String
class AccessListEntryView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVectorView[Windows.Storage.AccessCache.AccessListEntry]
    _classid_ = 'Windows.Storage.AccessCache.AccessListEntryView'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Storage.AccessCache.AccessListEntry], index: UInt32) -> Windows.Storage.AccessCache.AccessListEntry: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Storage.AccessCache.AccessListEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Storage.AccessCache.AccessListEntry], value: Windows.Storage.AccessCache.AccessListEntry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Storage.AccessCache.AccessListEntry], startIndex: UInt32, items: POINTER(Windows.Storage.AccessCache.AccessListEntry_head)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Storage.AccessCache.AccessListEntry]) -> Windows.Foundation.Collections.IIterator[Windows.Storage.AccessCache.AccessListEntry]: ...
    Size = property(get_Size, None)
class IItemRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IItemRemovedEventArgs'
    _iid_ = Guid('{59677e5c-55be-4c66-ba66-5eaea79d2631}')
    @winrt_commethod(6)
    def get_RemovedEntry(self) -> Windows.Storage.AccessCache.AccessListEntry: ...
    RemovedEntry = property(get_RemovedEntry, None)
class IStorageApplicationPermissionsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics'
    _iid_ = Guid('{4391dfaa-d033-48f9-8060-3ec847d2e3f1}')
    @winrt_commethod(6)
    def get_FutureAccessList(self) -> Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_commethod(7)
    def get_MostRecentlyUsedList(self) -> Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    FutureAccessList = property(get_FutureAccessList, None)
    MostRecentlyUsedList = property(get_MostRecentlyUsedList, None)
class IStorageApplicationPermissionsStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2'
    _iid_ = Guid('{072716ec-aa05-4294-9a11-1a3d04519ad0}')
    @winrt_commethod(6)
    def GetFutureAccessListForUser(self, user: Windows.System.User) -> Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_commethod(7)
    def GetMostRecentlyUsedListForUser(self, user: Windows.System.User) -> Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
class IStorageItemAccessList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemAccessList'
    _iid_ = Guid('{2caff6ad-de90-47f5-b2c3-dd36c9fdd453}')
    @winrt_commethod(6)
    def AddOverloadDefaultMetadata(self, file: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_commethod(7)
    def Add(self, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def AddOrReplaceOverloadDefaultMetadata(self, token: WinRT_String, file: Windows.Storage.IStorageItem) -> Void: ...
    @winrt_commethod(9)
    def AddOrReplace(self, token: WinRT_String, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetItemAsync(self, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_commethod(11)
    def GetFileAsync(self, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(12)
    def GetFolderAsync(self, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(13)
    def GetItemWithOptionsAsync(self, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_commethod(14)
    def GetFileWithOptionsAsync(self, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(15)
    def GetFolderWithOptionsAsync(self, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_commethod(16)
    def Remove(self, token: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def ContainsItem(self, token: WinRT_String) -> Boolean: ...
    @winrt_commethod(18)
    def Clear(self) -> Void: ...
    @winrt_commethod(19)
    def CheckAccess(self, file: Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_commethod(20)
    def get_Entries(self) -> Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_commethod(21)
    def get_MaximumItemsAllowed(self) -> UInt32: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
class IStorageItemMostRecentlyUsedList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList'
    _iid_ = Guid('{016239d5-510d-411e-8cf1-c3d1effa4c33}')
    @winrt_commethod(6)
    def add_ItemRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList, Windows.Storage.AccessCache.ItemRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemRemoved(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IStorageItemMostRecentlyUsedList2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2'
    _iid_ = Guid('{da481ea0-ed8d-4731-a1db-e44ee2204093}')
    @winrt_commethod(6)
    def AddWithMetadataAndVisibility(self, file: Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: Windows.Storage.AccessCache.RecentStorageItemVisibility) -> WinRT_String: ...
    @winrt_commethod(7)
    def AddOrReplaceWithMetadataAndVisibility(self, token: WinRT_String, file: Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: Windows.Storage.AccessCache.RecentStorageItemVisibility) -> Void: ...
class ItemRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.AccessCache.IItemRemovedEventArgs
    _classid_ = 'Windows.Storage.AccessCache.ItemRemovedEventArgs'
    @winrt_mixinmethod
    def get_RemovedEntry(self: Windows.Storage.AccessCache.IItemRemovedEventArgs) -> Windows.Storage.AccessCache.AccessListEntry: ...
    RemovedEntry = property(get_RemovedEntry, None)
RecentStorageItemVisibility = Int32
RecentStorageItemVisibility_AppOnly: RecentStorageItemVisibility = 0
RecentStorageItemVisibility_AppAndSystem: RecentStorageItemVisibility = 1
class _StorageApplicationPermissions_Meta_(ComPtr.__class__):
    pass
class StorageApplicationPermissions(ComPtr, metaclass=_StorageApplicationPermissions_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.AccessCache.StorageApplicationPermissions'
    @winrt_classmethod
    def GetFutureAccessListForUser(cls: Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2, user: Windows.System.User) -> Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_classmethod
    def GetMostRecentlyUsedListForUser(cls: Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics2, user: Windows.System.User) -> Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    @winrt_classmethod
    def get_FutureAccessList(cls: Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics) -> Windows.Storage.AccessCache.StorageItemAccessList: ...
    @winrt_classmethod
    def get_MostRecentlyUsedList(cls: Windows.Storage.AccessCache.IStorageApplicationPermissionsStatics) -> Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList: ...
    _StorageApplicationPermissions_Meta_.FutureAccessList = property(get_FutureAccessList.__wrapped__, None)
    _StorageApplicationPermissions_Meta_.MostRecentlyUsedList = property(get_MostRecentlyUsedList.__wrapped__, None)
class StorageItemAccessList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.AccessCache.IStorageItemAccessList
    _classid_ = 'Windows.Storage.AccessCache.StorageItemAccessList'
    @winrt_mixinmethod
    def AddOverloadDefaultMetadata(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def Add(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceOverloadDefaultMetadata(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: Windows.Storage.IStorageItem) -> Void: ...
    @winrt_mixinmethod
    def AddOrReplace(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetItemAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsItem(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> Void: ...
    @winrt_mixinmethod
    def CheckAccess(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Entries(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_mixinmethod
    def get_MaximumItemsAllowed(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> UInt32: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
class StorageItemMostRecentlyUsedList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList
    _classid_ = 'Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList'
    @winrt_mixinmethod
    def add_ItemRemoved(self: Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.AccessCache.StorageItemMostRecentlyUsedList, Windows.Storage.AccessCache.ItemRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemRemoved(self: Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddOverloadDefaultMetadata(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def Add(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceOverloadDefaultMetadata(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: Windows.Storage.IStorageItem) -> Void: ...
    @winrt_mixinmethod
    def AddOrReplace(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, file: Windows.Storage.IStorageItem, metadata: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetItemAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def GetItemWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def GetFileWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def GetFolderWithOptionsAsync(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String, options: Windows.Storage.AccessCache.AccessCacheOptions) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFolder]: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsItem(self: Windows.Storage.AccessCache.IStorageItemAccessList, token: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> Void: ...
    @winrt_mixinmethod
    def CheckAccess(self: Windows.Storage.AccessCache.IStorageItemAccessList, file: Windows.Storage.IStorageItem) -> Boolean: ...
    @winrt_mixinmethod
    def get_Entries(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> Windows.Storage.AccessCache.AccessListEntryView: ...
    @winrt_mixinmethod
    def get_MaximumItemsAllowed(self: Windows.Storage.AccessCache.IStorageItemAccessList) -> UInt32: ...
    @winrt_mixinmethod
    def AddWithMetadataAndVisibility(self: Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2, file: Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: Windows.Storage.AccessCache.RecentStorageItemVisibility) -> WinRT_String: ...
    @winrt_mixinmethod
    def AddOrReplaceWithMetadataAndVisibility(self: Windows.Storage.AccessCache.IStorageItemMostRecentlyUsedList2, token: WinRT_String, file: Windows.Storage.IStorageItem, metadata: WinRT_String, visibility: Windows.Storage.AccessCache.RecentStorageItemVisibility) -> Void: ...
    Entries = property(get_Entries, None)
    MaximumItemsAllowed = property(get_MaximumItemsAllowed, None)
make_head(_module, 'AccessListEntry')
make_head(_module, 'AccessListEntryView')
make_head(_module, 'IItemRemovedEventArgs')
make_head(_module, 'IStorageApplicationPermissionsStatics')
make_head(_module, 'IStorageApplicationPermissionsStatics2')
make_head(_module, 'IStorageItemAccessList')
make_head(_module, 'IStorageItemMostRecentlyUsedList')
make_head(_module, 'IStorageItemMostRecentlyUsedList2')
make_head(_module, 'ItemRemovedEventArgs')
make_head(_module, 'StorageApplicationPermissions')
make_head(_module, 'StorageItemAccessList')
make_head(_module, 'StorageItemMostRecentlyUsedList')
