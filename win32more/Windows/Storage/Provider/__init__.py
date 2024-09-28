from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class CachedFileOptions(Enum, UInt32):
    None_ = 0
    RequireUpdateOnAccess = 1
    UseCachedFileWhenOffline = 2
    DenyAccessWhenOffline = 4
class CachedFileTarget(Enum, Int32):
    Local = 0
    Remote = 1
class CachedFileUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.CachedFileUpdater'
    @winrt_classmethod
    def SetUpdateInformation(cls: win32more.Windows.Storage.Provider.ICachedFileUpdaterStatics, file: win32more.Windows.Storage.IStorageFile, contentId: WinRT_String, readMode: win32more.Windows.Storage.Provider.ReadActivationMode, writeMode: win32more.Windows.Storage.Provider.WriteActivationMode, options: win32more.Windows.Storage.Provider.CachedFileOptions) -> Void: ...
class CachedFileUpdaterUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI
    _classid_ = 'Windows.Storage.Provider.CachedFileUpdaterUI'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateTarget(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI) -> win32more.Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_mixinmethod
    def add_FileUpdateRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Storage.Provider.FileUpdateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileUpdateRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UIRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UIRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_UIStatus(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI) -> win32more.Windows.Storage.Provider.UIStatus: ...
    @winrt_mixinmethod
    def get_UpdateRequest(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI2) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI2) -> win32more.Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    Title = property(get_Title, put_Title)
    UIStatus = property(get_UIStatus, None)
    UpdateRequest = property(get_UpdateRequest, None)
    UpdateTarget = property(get_UpdateTarget, None)
    FileUpdateRequested = event()
    UIRequested = event()
CloudFilesContract: UInt32 = 458752
class FileUpdateRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IFileUpdateRequest
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequest'
    @winrt_mixinmethod
    def get_ContentId(self: win32more.Windows.Storage.Provider.IFileUpdateRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Storage.Provider.IFileUpdateRequest) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Storage.Provider.IFileUpdateRequest) -> win32more.Windows.Storage.Provider.FileUpdateStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Storage.Provider.IFileUpdateRequest, value: win32more.Windows.Storage.Provider.FileUpdateStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.Provider.IFileUpdateRequest) -> win32more.Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    @winrt_mixinmethod
    def UpdateLocalFile(self: win32more.Windows.Storage.Provider.IFileUpdateRequest, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def get_UserInputNeededMessage(self: win32more.Windows.Storage.Provider.IFileUpdateRequest2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserInputNeededMessage(self: win32more.Windows.Storage.Provider.IFileUpdateRequest2, value: WinRT_String) -> Void: ...
    ContentId = property(get_ContentId, None)
    File = property(get_File, None)
    Status = property(get_Status, put_Status)
    UserInputNeededMessage = property(get_UserInputNeededMessage, put_UserInputNeededMessage)
class FileUpdateRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IFileUpdateRequestDeferral
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Storage.Provider.IFileUpdateRequestDeferral) -> Void: ...
class FileUpdateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IFileUpdateRequestedEventArgs
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Storage.Provider.IFileUpdateRequestedEventArgs) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    Request = property(get_Request, None)
class FileUpdateStatus(Enum, Int32):
    Incomplete = 0
    Complete = 1
    UserInputNeeded = 2
    CurrentlyUnavailable = 3
    Failed = 4
    CompleteAndRenamed = 5
class ICachedFileUpdaterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.ICachedFileUpdaterStatics'
    _iid_ = Guid('{9fc90920-7bcf-4888-a81e-102d7034d7ce}')
    @winrt_commethod(6)
    def SetUpdateInformation(self, file: win32more.Windows.Storage.IStorageFile, contentId: WinRT_String, readMode: win32more.Windows.Storage.Provider.ReadActivationMode, writeMode: win32more.Windows.Storage.Provider.WriteActivationMode, options: win32more.Windows.Storage.Provider.CachedFileOptions) -> Void: ...
class ICachedFileUpdaterUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.ICachedFileUpdaterUI'
    _iid_ = Guid('{9e6f41e6-baf2-4a97-b600-9333f5df80fd}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateTarget(self) -> win32more.Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_commethod(9)
    def add_FileUpdateRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Storage.Provider.FileUpdateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_FileUpdateRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_UIRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UIRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_UIStatus(self) -> win32more.Windows.Storage.Provider.UIStatus: ...
    Title = property(get_Title, put_Title)
    UIStatus = property(get_UIStatus, None)
    UpdateTarget = property(get_UpdateTarget, None)
    FileUpdateRequested = event()
    UIRequested = event()
class ICachedFileUpdaterUI2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.ICachedFileUpdaterUI2'
    _iid_ = Guid('{8856a21c-8699-4340-9f49-f7cad7fe8991}')
    @winrt_commethod(6)
    def get_UpdateRequest(self) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    UpdateRequest = property(get_UpdateRequest, None)
class IFileUpdateRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IFileUpdateRequest'
    _iid_ = Guid('{40c82536-c1fe-4d93-a792-1e736bc70837}')
    @winrt_commethod(6)
    def get_ContentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Storage.Provider.FileUpdateStatus: ...
    @winrt_commethod(9)
    def put_Status(self, value: win32more.Windows.Storage.Provider.FileUpdateStatus) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    @winrt_commethod(11)
    def UpdateLocalFile(self, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    ContentId = property(get_ContentId, None)
    File = property(get_File, None)
    Status = property(get_Status, put_Status)
class IFileUpdateRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IFileUpdateRequest2'
    _iid_ = Guid('{82484648-bdbe-447b-a2ee-7afe6a032a94}')
    @winrt_commethod(6)
    def get_UserInputNeededMessage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UserInputNeededMessage(self, value: WinRT_String) -> Void: ...
    UserInputNeededMessage = property(get_UserInputNeededMessage, put_UserInputNeededMessage)
class IFileUpdateRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IFileUpdateRequestDeferral'
    _iid_ = Guid('{ffcedb2b-8ade-44a5-bb00-164c4e72f13a}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IFileUpdateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IFileUpdateRequestedEventArgs'
    _iid_ = Guid('{7b0a9342-3905-438d-aaef-78ae265f8dd2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    Request = property(get_Request, None)
class IStorageProviderFileTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderFileTypeInfo'
    _iid_ = Guid('{1955b9c1-0184-5a88-87df-4544f464365d}')
    @winrt_commethod(6)
    def get_FileExtension(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IconResource(self) -> WinRT_String: ...
    FileExtension = property(get_FileExtension, None)
    IconResource = property(get_IconResource, None)
class IStorageProviderFileTypeInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderFileTypeInfoFactory'
    _iid_ = Guid('{3fa12c6f-cce6-5d5d-80b1-389e7cf92dbf}')
    @winrt_commethod(6)
    def CreateInstance(self, fileExtension: WinRT_String, iconResource: WinRT_String) -> win32more.Windows.Storage.Provider.StorageProviderFileTypeInfo: ...
class IStorageProviderGetContentInfoForPathResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult'
    _iid_ = Guid('{2564711d-aa89-4d12-82e3-f72a92e33966}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_commethod(7)
    def put_Status(self, value: win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_commethod(8)
    def get_ContentUri(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ContentUri(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ContentId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ContentId(self, value: WinRT_String) -> Void: ...
    ContentId = property(get_ContentId, put_ContentId)
    ContentUri = property(get_ContentUri, put_ContentUri)
    Status = property(get_Status, put_Status)
class IStorageProviderGetPathForContentUriResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult'
    _iid_ = Guid('{63711a9d-4118-45a6-acb6-22c49d019f40}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_commethod(7)
    def put_Status(self, value: win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_commethod(8)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Path(self, value: WinRT_String) -> Void: ...
    Path = property(get_Path, put_Path)
    Status = property(get_Status, put_Status)
class IStorageProviderItemPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderItemPropertiesStatics'
    _iid_ = Guid('{2d2c1c97-2704-4729-8fa9-7e6b8e158c2f}')
    @winrt_commethod(6)
    def SetAsync(self, item: win32more.Windows.Storage.IStorageItem, itemProperties: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Provider.StorageProviderItemProperty]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IStorageProviderItemProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderItemProperty'
    _iid_ = Guid('{476cb558-730b-4188-b7b5-63b716ed476d}')
    @winrt_commethod(6)
    def put_Id(self, value: Int32) -> Void: ...
    @winrt_commethod(7)
    def get_Id(self) -> Int32: ...
    @winrt_commethod(8)
    def put_Value(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_IconResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_IconResource(self) -> WinRT_String: ...
    IconResource = property(get_IconResource, put_IconResource)
    Id = property(get_Id, put_Id)
    Value = property(get_Value, put_Value)
class IStorageProviderItemPropertyDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderItemPropertyDefinition'
    _iid_ = Guid('{c5b383bb-ff1f-4298-831e-ff1c08089690}')
    @winrt_commethod(6)
    def get_Id(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Id(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayNameResource(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayNameResource(self, value: WinRT_String) -> Void: ...
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    Id = property(get_Id, put_Id)
class IStorageProviderItemPropertySource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderItemPropertySource'
    _iid_ = Guid('{8f6f9c3e-f632-4a9b-8d99-d2d7a11df56a}')
    @winrt_commethod(6)
    def GetItemProperties(self, itemPath: WinRT_String) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Provider.StorageProviderItemProperty]: ...
class IStorageProviderKnownFolderEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderKnownFolderEntry'
    _iid_ = Guid('{effa7db0-1d44-596b-8464-928800c5e2d8}')
    @winrt_commethod(6)
    def get_KnownFolderId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_KnownFolderId(self, value: Guid) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncStatus: ...
    @winrt_commethod(9)
    def put_Status(self, value: win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncStatus) -> Void: ...
    KnownFolderId = property(get_KnownFolderId, put_KnownFolderId)
    Status = property(get_Status, put_Status)
class IStorageProviderKnownFolderSyncInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo'
    _iid_ = Guid('{98b017ce-ffc1-5b11-ae77-cc17afec1049}')
    @winrt_commethod(6)
    def get_ProviderDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProviderDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_KnownFolderEntries(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderKnownFolderEntry]: ...
    @winrt_commethod(9)
    def get_SyncRequested(self) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestedHandler: ...
    @winrt_commethod(10)
    def put_SyncRequested(self, value: win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestedHandler) -> Void: ...
    KnownFolderEntries = property(get_KnownFolderEntries, None)
    ProviderDisplayName = property(get_ProviderDisplayName, put_ProviderDisplayName)
    SyncRequested = property(get_SyncRequested, put_SyncRequested)
class IStorageProviderKnownFolderSyncInfoSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfoSource'
    _iid_ = Guid('{51359342-f7c0-53d0-bbb6-1cdc098ebda9}')
    @winrt_commethod(6)
    def GetKnownFolderSyncInfo(self) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncInfo: ...
    @winrt_commethod(7)
    def add_KnownFolderSyncInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfoSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_KnownFolderSyncInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    KnownFolderSyncInfoChanged = event()
class IStorageProviderKnownFolderSyncInfoSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfoSourceFactory'
    _iid_ = Guid('{aaee03a7-a7f6-50be-a9b0-8e82d0c81082}')
    @winrt_commethod(6)
    def GetKnownFolderSyncInfoSource(self) -> win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfoSource: ...
class IStorageProviderKnownFolderSyncRequestArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderKnownFolderSyncRequestArgs'
    _iid_ = Guid('{eda6d569-b4e8-542f-ab8d-f3613f250a4a}')
    @winrt_commethod(6)
    def get_KnownFolders(self) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_commethod(7)
    def get_Source(self) -> win32more.Windows.Storage.StorageFolder: ...
    KnownFolders = property(get_KnownFolders, None)
    Source = property(get_Source, None)
class IStorageProviderMoreInfoUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderMoreInfoUI'
    _iid_ = Guid('{ef38e591-a7cb-5e7d-9b5e-22749842697c}')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Command(self) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(9)
    def put_Command(self, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    Command = property(get_Command, put_Command)
    Message = property(get_Message, put_Message)
class IStorageProviderPropertyCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderPropertyCapabilities'
    _iid_ = Guid('{658d2f0e-63b7-4567-acf9-51abe301dda5}')
    @winrt_commethod(6)
    def IsPropertySupported(self, propertyCanonicalName: WinRT_String) -> Boolean: ...
class IStorageProviderQuotaUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderQuotaUI'
    _iid_ = Guid('{ba6295c3-312e-544f-9fd5-1f81b21f3649}')
    @winrt_commethod(6)
    def get_QuotaTotalInBytes(self) -> UInt64: ...
    @winrt_commethod(7)
    def put_QuotaTotalInBytes(self, value: UInt64) -> Void: ...
    @winrt_commethod(8)
    def get_QuotaUsedInBytes(self) -> UInt64: ...
    @winrt_commethod(9)
    def put_QuotaUsedInBytes(self, value: UInt64) -> Void: ...
    @winrt_commethod(10)
    def get_QuotaUsedLabel(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_QuotaUsedLabel(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_QuotaUsedColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_QuotaUsedColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    QuotaTotalInBytes = property(get_QuotaTotalInBytes, put_QuotaTotalInBytes)
    QuotaUsedColor = property(get_QuotaUsedColor, put_QuotaUsedColor)
    QuotaUsedInBytes = property(get_QuotaUsedInBytes, put_QuotaUsedInBytes)
    QuotaUsedLabel = property(get_QuotaUsedLabel, put_QuotaUsedLabel)
class IStorageProviderShareLinkSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderShareLinkSource'
    _iid_ = Guid('{4c6055e2-029c-5539-8e51-a1afc838b5cb}')
    @winrt_commethod(6)
    def CreateLinkAsync(self, storageItemList: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def GetDefaultAccessControlStringAsync(self, storageItemList: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def GetState(self, storageItemList: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Provider.StorageProviderShareLinkState]: ...
class IStorageProviderStatusUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderStatusUI'
    _iid_ = Guid('{d6b6a758-198d-5b80-977f-5ff73da33118}')
    @winrt_commethod(6)
    def get_ProviderState(self) -> win32more.Windows.Storage.Provider.StorageProviderState: ...
    @winrt_commethod(7)
    def put_ProviderState(self, value: win32more.Windows.Storage.Provider.StorageProviderState) -> Void: ...
    @winrt_commethod(8)
    def get_ProviderStateLabel(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ProviderStateLabel(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ProviderStateIcon(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_ProviderStateIcon(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(12)
    def get_SyncStatusCommand(self) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(13)
    def put_SyncStatusCommand(self, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_commethod(14)
    def get_QuotaUI(self) -> win32more.Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_commethod(15)
    def put_QuotaUI(self, value: win32more.Windows.Storage.Provider.StorageProviderQuotaUI) -> Void: ...
    @winrt_commethod(16)
    def get_MoreInfoUI(self) -> win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_commethod(17)
    def put_MoreInfoUI(self, value: win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI) -> Void: ...
    @winrt_commethod(18)
    def get_ProviderPrimaryCommand(self) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(19)
    def put_ProviderPrimaryCommand(self, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_commethod(20)
    def get_ProviderSecondaryCommands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.IStorageProviderUICommand]: ...
    @winrt_commethod(21)
    def put_ProviderSecondaryCommands(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.IStorageProviderUICommand]) -> Void: ...
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
class IStorageProviderStatusUISource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderStatusUISource'
    _iid_ = Guid('{a306c249-3d66-5e70-9007-e43df96051ff}')
    @winrt_commethod(6)
    def GetStatusUI(self) -> win32more.Windows.Storage.Provider.StorageProviderStatusUI: ...
    @winrt_commethod(7)
    def add_StatusUIChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.IStorageProviderStatusUISource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StatusUIChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StatusUIChanged = event()
class IStorageProviderStatusUISourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderStatusUISourceFactory'
    _iid_ = Guid('{12e46b74-4e5a-58d1-a62f-0376e8ee7dd8}')
    @winrt_commethod(6)
    def GetStatusUISource(self, syncRootId: WinRT_String) -> win32more.Windows.Storage.Provider.IStorageProviderStatusUISource: ...
class IStorageProviderSyncRootInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderSyncRootInfo'
    _iid_ = Guid('{7c1305c4-99f9-41ac-8904-ab055d654926}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Context(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Context(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_Path(self) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_commethod(11)
    def put_Path(self, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_commethod(12)
    def get_DisplayNameResource(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_DisplayNameResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IconResource(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_IconResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_HydrationPolicy(self) -> win32more.Windows.Storage.Provider.StorageProviderHydrationPolicy: ...
    @winrt_commethod(17)
    def put_HydrationPolicy(self, value: win32more.Windows.Storage.Provider.StorageProviderHydrationPolicy) -> Void: ...
    @winrt_commethod(18)
    def get_HydrationPolicyModifier(self) -> win32more.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier: ...
    @winrt_commethod(19)
    def put_HydrationPolicyModifier(self, value: win32more.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier) -> Void: ...
    @winrt_commethod(20)
    def get_PopulationPolicy(self) -> win32more.Windows.Storage.Provider.StorageProviderPopulationPolicy: ...
    @winrt_commethod(21)
    def put_PopulationPolicy(self, value: win32more.Windows.Storage.Provider.StorageProviderPopulationPolicy) -> Void: ...
    @winrt_commethod(22)
    def get_InSyncPolicy(self) -> win32more.Windows.Storage.Provider.StorageProviderInSyncPolicy: ...
    @winrt_commethod(23)
    def put_InSyncPolicy(self, value: win32more.Windows.Storage.Provider.StorageProviderInSyncPolicy) -> Void: ...
    @winrt_commethod(24)
    def get_HardlinkPolicy(self) -> win32more.Windows.Storage.Provider.StorageProviderHardlinkPolicy: ...
    @winrt_commethod(25)
    def put_HardlinkPolicy(self, value: win32more.Windows.Storage.Provider.StorageProviderHardlinkPolicy) -> Void: ...
    @winrt_commethod(26)
    def get_ShowSiblingsAsGroup(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_ShowSiblingsAsGroup(self, value: Boolean) -> Void: ...
    @winrt_commethod(28)
    def get_Version(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def put_Version(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(30)
    def get_ProtectionMode(self) -> win32more.Windows.Storage.Provider.StorageProviderProtectionMode: ...
    @winrt_commethod(31)
    def put_ProtectionMode(self, value: win32more.Windows.Storage.Provider.StorageProviderProtectionMode) -> Void: ...
    @winrt_commethod(32)
    def get_AllowPinning(self) -> Boolean: ...
    @winrt_commethod(33)
    def put_AllowPinning(self, value: Boolean) -> Void: ...
    @winrt_commethod(34)
    def get_StorageProviderItemPropertyDefinitions(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderItemPropertyDefinition]: ...
    @winrt_commethod(35)
    def get_RecycleBinUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(36)
    def put_RecycleBinUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    AllowPinning = property(get_AllowPinning, put_AllowPinning)
    Context = property(get_Context, put_Context)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    HardlinkPolicy = property(get_HardlinkPolicy, put_HardlinkPolicy)
    HydrationPolicy = property(get_HydrationPolicy, put_HydrationPolicy)
    HydrationPolicyModifier = property(get_HydrationPolicyModifier, put_HydrationPolicyModifier)
    IconResource = property(get_IconResource, put_IconResource)
    Id = property(get_Id, put_Id)
    InSyncPolicy = property(get_InSyncPolicy, put_InSyncPolicy)
    Path = property(get_Path, put_Path)
    PopulationPolicy = property(get_PopulationPolicy, put_PopulationPolicy)
    ProtectionMode = property(get_ProtectionMode, put_ProtectionMode)
    RecycleBinUri = property(get_RecycleBinUri, put_RecycleBinUri)
    ShowSiblingsAsGroup = property(get_ShowSiblingsAsGroup, put_ShowSiblingsAsGroup)
    StorageProviderItemPropertyDefinitions = property(get_StorageProviderItemPropertyDefinitions, None)
    Version = property(get_Version, put_Version)
class IStorageProviderSyncRootInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderSyncRootInfo2'
    _iid_ = Guid('{cf51b023-7cf1-5166-bdba-efd95f529e31}')
    @winrt_commethod(6)
    def get_ProviderId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_ProviderId(self, value: Guid) -> Void: ...
    ProviderId = property(get_ProviderId, put_ProviderId)
class IStorageProviderSyncRootInfo3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderSyncRootInfo3'
    _iid_ = Guid('{507a6617-bef6-56fd-855e-75ace2e45cf5}')
    @winrt_commethod(6)
    def get_FallbackFileTypeInfo(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderFileTypeInfo]: ...
    FallbackFileTypeInfo = property(get_FallbackFileTypeInfo, None)
class IStorageProviderSyncRootManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics'
    _iid_ = Guid('{3e99fbbf-8fe3-4b40-abc7-f6fc3d74c98e}')
    @winrt_commethod(6)
    def Register(self, syncRootInformation: win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo) -> Void: ...
    @winrt_commethod(7)
    def Unregister(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def GetSyncRootInformationForFolder(self, folder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_commethod(9)
    def GetSyncRootInformationForId(self, id: WinRT_String) -> win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_commethod(10)
    def GetCurrentSyncRoots(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo]: ...
class IStorageProviderSyncRootManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics2'
    _iid_ = Guid('{efb6cfee-1374-544e-9df1-5598d2e9cfdd}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IStorageProviderUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderUICommand'
    _iid_ = Guid('{0c3e0760-d846-568f-9484-105cc57b502b}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Icon(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Storage.Provider.StorageProviderUICommandState: ...
    @winrt_commethod(10)
    def Invoke(self) -> Void: ...
    Description = property(get_Description, None)
    Icon = property(get_Icon, None)
    Label = property(get_Label, None)
    State = property(get_State, None)
class IStorageProviderUriSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderUriSource'
    _iid_ = Guid('{b29806d1-8be0-4962-8bb6-0d4c2e14d47a}')
    @winrt_commethod(6)
    def GetPathForContentUri(self, contentUri: WinRT_String, result: win32more.Windows.Storage.Provider.StorageProviderGetPathForContentUriResult) -> Void: ...
    @winrt_commethod(7)
    def GetContentInfoForPath(self, path: WinRT_String, result: win32more.Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult) -> Void: ...
class ReadActivationMode(Enum, Int32):
    NotNeeded = 0
    BeforeAccess = 1
class StorageProviderFileTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderFileTypeInfo
    _classid_ = 'Windows.Storage.Provider.StorageProviderFileTypeInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderFileTypeInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Storage.Provider.IStorageProviderFileTypeInfoFactory, fileExtension: WinRT_String, iconResource: WinRT_String) -> win32more.Windows.Storage.Provider.StorageProviderFileTypeInfo: ...
    @winrt_mixinmethod
    def get_FileExtension(self: win32more.Windows.Storage.Provider.IStorageProviderFileTypeInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IconResource(self: win32more.Windows.Storage.Provider.IStorageProviderFileTypeInfo) -> WinRT_String: ...
    FileExtension = property(get_FileExtension, None)
    IconResource = property(get_IconResource, None)
class StorageProviderGetContentInfoForPathResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult
    _classid_ = 'Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_ContentUri(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentUri(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentId(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentId(self: win32more.Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: WinRT_String) -> Void: ...
    ContentId = property(get_ContentId, put_ContentId)
    ContentUri = property(get_ContentUri, put_ContentUri)
    Status = property(get_Status, put_Status)
class StorageProviderGetPathForContentUriResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult
    _classid_ = 'Windows.Storage.Provider.StorageProviderGetPathForContentUriResult'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderGetPathForContentUriResult.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderGetPathForContentUriResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult) -> win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult, value: win32more.Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult, value: WinRT_String) -> Void: ...
    Path = property(get_Path, put_Path)
    Status = property(get_Status, put_Status)
class StorageProviderHardlinkPolicy(Enum, UInt32):
    None_ = 0
    Allowed = 1
class StorageProviderHydrationPolicy(Enum, Int32):
    Partial = 0
    Progressive = 1
    Full = 2
    AlwaysFull = 3
class StorageProviderHydrationPolicyModifier(Enum, UInt32):
    None_ = 0
    ValidationRequired = 1
    StreamingAllowed = 2
    AutoDehydrationAllowed = 4
    AllowFullRestartHydration = 8
class StorageProviderInSyncPolicy(Enum, UInt32):
    Default = 0
    FileCreationTime = 1
    FileReadOnlyAttribute = 2
    FileHiddenAttribute = 4
    FileSystemAttribute = 8
    DirectoryCreationTime = 16
    DirectoryReadOnlyAttribute = 32
    DirectoryHiddenAttribute = 64
    DirectorySystemAttribute = 128
    FileLastWriteTime = 256
    DirectoryLastWriteTime = 512
    PreserveInsyncForSyncEngine = 2147483648
class StorageProviderItemProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperties'
    @winrt_classmethod
    def SetAsync(cls: win32more.Windows.Storage.Provider.IStorageProviderItemPropertiesStatics, item: win32more.Windows.Storage.IStorageItem, itemProperties: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Provider.StorageProviderItemProperty]) -> win32more.Windows.Foundation.IAsyncAction: ...
class StorageProviderItemProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderItemProperty
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperty'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderItemProperty.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderItemProperty: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty) -> Int32: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IconResource(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconResource(self: win32more.Windows.Storage.Provider.IStorageProviderItemProperty) -> WinRT_String: ...
    IconResource = property(get_IconResource, put_IconResource)
    Id = property(get_Id, put_Id)
    Value = property(get_Value, put_Value)
class StorageProviderItemPropertyDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemPropertyDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderItemPropertyDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderItemPropertyDefinition: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition) -> Int32: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayNameResource(self: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition, value: WinRT_String) -> Void: ...
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    Id = property(get_Id, put_Id)
class StorageProviderKnownFolderEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderEntry
    _classid_ = 'Windows.Storage.Provider.StorageProviderKnownFolderEntry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderKnownFolderEntry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderEntry: ...
    @winrt_mixinmethod
    def get_KnownFolderId(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderEntry) -> Guid: ...
    @winrt_mixinmethod
    def put_KnownFolderId(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderEntry, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderEntry) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderEntry, value: win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncStatus) -> Void: ...
    KnownFolderId = property(get_KnownFolderId, put_KnownFolderId)
    Status = property(get_Status, put_Status)
class StorageProviderKnownFolderSyncInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo
    _classid_ = 'Windows.Storage.Provider.StorageProviderKnownFolderSyncInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncInfo: ...
    @winrt_mixinmethod
    def get_ProviderDisplayName(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProviderDisplayName(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_KnownFolderEntries(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderKnownFolderEntry]: ...
    @winrt_mixinmethod
    def get_SyncRequested(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo) -> win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestedHandler: ...
    @winrt_mixinmethod
    def put_SyncRequested(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncInfo, value: win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestedHandler) -> Void: ...
    KnownFolderEntries = property(get_KnownFolderEntries, None)
    ProviderDisplayName = property(get_ProviderDisplayName, put_ProviderDisplayName)
    SyncRequested = property(get_SyncRequested, put_SyncRequested)
class StorageProviderKnownFolderSyncRequestArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncRequestArgs
    _classid_ = 'Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestArgs'
    @winrt_mixinmethod
    def get_KnownFolders(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncRequestArgs) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Storage.Provider.IStorageProviderKnownFolderSyncRequestArgs) -> win32more.Windows.Storage.StorageFolder: ...
    KnownFolders = property(get_KnownFolders, None)
    Source = property(get_Source, None)
class StorageProviderKnownFolderSyncRequestedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4cbb4f5-13dd-5c8e-8b96-336fc30c629b}')
    @winrt_commethod(3)
    def Invoke(self, args: win32more.Windows.Storage.Provider.StorageProviderKnownFolderSyncRequestArgs) -> Void: ...
class StorageProviderKnownFolderSyncStatus(Enum, Int32):
    Available = 0
    Enrolling = 1
    Enrolled = 2
class StorageProviderMoreInfoUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderMoreInfoUI'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    Command = property(get_Command, put_Command)
    Message = property(get_Message, put_Message)
class StorageProviderPopulationPolicy(Enum, Int32):
    Full = 1
    AlwaysFull = 2
class StorageProviderProtectionMode(Enum, Int32):
    Unknown = 0
    Personal = 1
class StorageProviderQuotaUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderQuotaUI'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderQuotaUI.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_mixinmethod
    def get_QuotaTotalInBytes(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI) -> UInt64: ...
    @winrt_mixinmethod
    def put_QuotaTotalInBytes(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedInBytes(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI) -> UInt64: ...
    @winrt_mixinmethod
    def put_QuotaUsedInBytes(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedLabel(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_QuotaUsedLabel(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedColor(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_QuotaUsedColor(self: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    QuotaTotalInBytes = property(get_QuotaTotalInBytes, put_QuotaTotalInBytes)
    QuotaUsedColor = property(get_QuotaUsedColor, put_QuotaUsedColor)
    QuotaUsedInBytes = property(get_QuotaUsedInBytes, put_QuotaUsedInBytes)
    QuotaUsedLabel = property(get_QuotaUsedLabel, put_QuotaUsedLabel)
class StorageProviderShareLinkState(Enum, Int32):
    Enabled = 0
    Disabled = 1
class StorageProviderState(Enum, Int32):
    InSync = 0
    Syncing = 1
    Paused = 2
    Error = 3
    Warning = 4
    Offline = 5
class StorageProviderStatusUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderStatusUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderStatusUI'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderStatusUI.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderStatusUI: ...
    @winrt_mixinmethod
    def get_ProviderState(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Storage.Provider.StorageProviderState: ...
    @winrt_mixinmethod
    def put_ProviderState(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Storage.Provider.StorageProviderState) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderStateLabel(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProviderStateLabel(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderStateIcon(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ProviderStateIcon(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_SyncStatusCommand(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_SyncStatusCommand(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUI(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_mixinmethod
    def put_QuotaUI(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Storage.Provider.StorageProviderQuotaUI) -> Void: ...
    @winrt_mixinmethod
    def get_MoreInfoUI(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_mixinmethod
    def put_MoreInfoUI(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Storage.Provider.StorageProviderMoreInfoUI) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderPrimaryCommand(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_ProviderPrimaryCommand(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderSecondaryCommands(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.IStorageProviderUICommand]: ...
    @winrt_mixinmethod
    def put_ProviderSecondaryCommands(self: win32more.Windows.Storage.Provider.IStorageProviderStatusUI, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.IStorageProviderUICommand]) -> Void: ...
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
class StorageProviderSyncRootInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo
    _classid_ = 'Windows.Storage.Provider.StorageProviderSyncRootInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Context(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayNameResource(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconResource(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IconResource(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HydrationPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderHydrationPolicy: ...
    @winrt_mixinmethod
    def put_HydrationPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderHydrationPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_HydrationPolicyModifier(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier: ...
    @winrt_mixinmethod
    def put_HydrationPolicyModifier(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier) -> Void: ...
    @winrt_mixinmethod
    def get_PopulationPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderPopulationPolicy: ...
    @winrt_mixinmethod
    def put_PopulationPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderPopulationPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_InSyncPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderInSyncPolicy: ...
    @winrt_mixinmethod
    def put_InSyncPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderInSyncPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_HardlinkPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderHardlinkPolicy: ...
    @winrt_mixinmethod
    def put_HardlinkPolicy(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderHardlinkPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_ShowSiblingsAsGroup(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowSiblingsAsGroup(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Version(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProtectionMode(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Storage.Provider.StorageProviderProtectionMode: ...
    @winrt_mixinmethod
    def put_ProtectionMode(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Storage.Provider.StorageProviderProtectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AllowPinning(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowPinning(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StorageProviderItemPropertyDefinitions(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderItemPropertyDefinition]: ...
    @winrt_mixinmethod
    def get_RecycleBinUri(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RecycleBinUri(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderId(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo2) -> Guid: ...
    @winrt_mixinmethod
    def put_ProviderId(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo2, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackFileTypeInfo(self: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo3) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Provider.StorageProviderFileTypeInfo]: ...
    AllowPinning = property(get_AllowPinning, put_AllowPinning)
    Context = property(get_Context, put_Context)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    FallbackFileTypeInfo = property(get_FallbackFileTypeInfo, None)
    HardlinkPolicy = property(get_HardlinkPolicy, put_HardlinkPolicy)
    HydrationPolicy = property(get_HydrationPolicy, put_HydrationPolicy)
    HydrationPolicyModifier = property(get_HydrationPolicyModifier, put_HydrationPolicyModifier)
    IconResource = property(get_IconResource, put_IconResource)
    Id = property(get_Id, put_Id)
    InSyncPolicy = property(get_InSyncPolicy, put_InSyncPolicy)
    Path = property(get_Path, put_Path)
    PopulationPolicy = property(get_PopulationPolicy, put_PopulationPolicy)
    ProtectionMode = property(get_ProtectionMode, put_ProtectionMode)
    ProviderId = property(get_ProviderId, put_ProviderId)
    RecycleBinUri = property(get_RecycleBinUri, put_RecycleBinUri)
    ShowSiblingsAsGroup = property(get_ShowSiblingsAsGroup, put_ShowSiblingsAsGroup)
    StorageProviderItemPropertyDefinitions = property(get_StorageProviderItemPropertyDefinitions, None)
    Version = property(get_Version, put_Version)
class StorageProviderSyncRootManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderSyncRootManager'
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def Register(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, syncRootInformation: win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo) -> Void: ...
    @winrt_classmethod
    def Unregister(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, id: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetSyncRootInformationForFolder(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, folder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_classmethod
    def GetSyncRootInformationForId(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, id: WinRT_String) -> win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_classmethod
    def GetCurrentSyncRoots(cls: win32more.Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Provider.StorageProviderSyncRootInfo]: ...
class StorageProviderUICommandState(Enum, Int32):
    Enabled = 0
    Disabled = 1
    Hidden = 2
class StorageProviderUriSourceStatus(Enum, Int32):
    Success = 0
    NoSyncRoot = 1
    FileNotFound = 2
class UIStatus(Enum, Int32):
    Unavailable = 0
    Hidden = 1
    Visible = 2
    Complete = 3
class WriteActivationMode(Enum, Int32):
    ReadOnly = 0
    NotNeeded = 1
    AfterWrite = 2


make_ready(__name__)
