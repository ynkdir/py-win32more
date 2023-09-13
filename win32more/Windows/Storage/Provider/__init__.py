from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CachedFileOptions = UInt32
CachedFileOptions_None: CachedFileOptions = 0
CachedFileOptions_RequireUpdateOnAccess: CachedFileOptions = 1
CachedFileOptions_UseCachedFileWhenOffline: CachedFileOptions = 2
CachedFileOptions_DenyAccessWhenOffline: CachedFileOptions = 4
CachedFileTarget = Int32
CachedFileTarget_Local: CachedFileTarget = 0
CachedFileTarget_Remote: CachedFileTarget = 1
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
    def add_UIRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UIRequested(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_UIStatus(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI) -> win32more.Windows.Storage.Provider.UIStatus: ...
    @winrt_mixinmethod
    def get_UpdateRequest(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI2) -> win32more.Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.Provider.ICachedFileUpdaterUI2) -> win32more.Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    Title = property(get_Title, put_Title)
    UpdateTarget = property(get_UpdateTarget, None)
    UIStatus = property(get_UIStatus, None)
    UpdateRequest = property(get_UpdateRequest, None)
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
FileUpdateStatus = Int32
FileUpdateStatus_Incomplete: FileUpdateStatus = 0
FileUpdateStatus_Complete: FileUpdateStatus = 1
FileUpdateStatus_UserInputNeeded: FileUpdateStatus = 2
FileUpdateStatus_CurrentlyUnavailable: FileUpdateStatus = 3
FileUpdateStatus_Failed: FileUpdateStatus = 4
FileUpdateStatus_CompleteAndRenamed: FileUpdateStatus = 5
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
    def add_UIRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.CachedFileUpdaterUI, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UIRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_UIStatus(self) -> win32more.Windows.Storage.Provider.UIStatus: ...
    Title = property(get_Title, put_Title)
    UpdateTarget = property(get_UpdateTarget, None)
    UIStatus = property(get_UIStatus, None)
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
    Status = property(get_Status, put_Status)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentId = property(get_ContentId, put_ContentId)
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
    Status = property(get_Status, put_Status)
    Path = property(get_Path, put_Path)
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
    Id = property(get_Id, put_Id)
    Value = property(get_Value, put_Value)
    IconResource = property(get_IconResource, put_IconResource)
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
    Id = property(get_Id, put_Id)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
class IStorageProviderItemPropertySource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderItemPropertySource'
    _iid_ = Guid('{8f6f9c3e-f632-4a9b-8d99-d2d7a11df56a}')
    @winrt_commethod(6)
    def GetItemProperties(self, itemPath: WinRT_String) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Provider.StorageProviderItemProperty]: ...
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
    Message = property(get_Message, put_Message)
    Command = property(get_Command, put_Command)
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
    QuotaUsedInBytes = property(get_QuotaUsedInBytes, put_QuotaUsedInBytes)
    QuotaUsedLabel = property(get_QuotaUsedLabel, put_QuotaUsedLabel)
    QuotaUsedColor = property(get_QuotaUsedColor, put_QuotaUsedColor)
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
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
class IStorageProviderStatusUISource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderStatusUISource'
    _iid_ = Guid('{a306c249-3d66-5e70-9007-e43df96051ff}')
    @winrt_commethod(6)
    def GetStatusUI(self) -> win32more.Windows.Storage.Provider.StorageProviderStatusUI: ...
    @winrt_commethod(7)
    def add_StatusUIChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Provider.IStorageProviderStatusUISource, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StatusUIChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    Id = property(get_Id, put_Id)
    Context = property(get_Context, put_Context)
    Path = property(get_Path, put_Path)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    IconResource = property(get_IconResource, put_IconResource)
    HydrationPolicy = property(get_HydrationPolicy, put_HydrationPolicy)
    HydrationPolicyModifier = property(get_HydrationPolicyModifier, put_HydrationPolicyModifier)
    PopulationPolicy = property(get_PopulationPolicy, put_PopulationPolicy)
    InSyncPolicy = property(get_InSyncPolicy, put_InSyncPolicy)
    HardlinkPolicy = property(get_HardlinkPolicy, put_HardlinkPolicy)
    ShowSiblingsAsGroup = property(get_ShowSiblingsAsGroup, put_ShowSiblingsAsGroup)
    Version = property(get_Version, put_Version)
    ProtectionMode = property(get_ProtectionMode, put_ProtectionMode)
    AllowPinning = property(get_AllowPinning, put_AllowPinning)
    StorageProviderItemPropertyDefinitions = property(get_StorageProviderItemPropertyDefinitions, None)
    RecycleBinUri = property(get_RecycleBinUri, put_RecycleBinUri)
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
    Label = property(get_Label, None)
    Description = property(get_Description, None)
    Icon = property(get_Icon, None)
    State = property(get_State, None)
class IStorageProviderUriSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.IStorageProviderUriSource'
    _iid_ = Guid('{b29806d1-8be0-4962-8bb6-0d4c2e14d47a}')
    @winrt_commethod(6)
    def GetPathForContentUri(self, contentUri: WinRT_String, result: win32more.Windows.Storage.Provider.StorageProviderGetPathForContentUriResult) -> Void: ...
    @winrt_commethod(7)
    def GetContentInfoForPath(self, path: WinRT_String, result: win32more.Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult) -> Void: ...
ReadActivationMode = Int32
ReadActivationMode_NotNeeded: ReadActivationMode = 0
ReadActivationMode_BeforeAccess: ReadActivationMode = 1
class StorageProviderFileTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderFileTypeInfo
    _classid_ = 'Windows.Storage.Provider.StorageProviderFileTypeInfo'
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
    Status = property(get_Status, put_Status)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentId = property(get_ContentId, put_ContentId)
class StorageProviderGetPathForContentUriResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult
    _classid_ = 'Windows.Storage.Provider.StorageProviderGetPathForContentUriResult'
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
    Status = property(get_Status, put_Status)
    Path = property(get_Path, put_Path)
StorageProviderHardlinkPolicy = UInt32
StorageProviderHardlinkPolicy_None: StorageProviderHardlinkPolicy = 0
StorageProviderHardlinkPolicy_Allowed: StorageProviderHardlinkPolicy = 1
StorageProviderHydrationPolicy = Int32
StorageProviderHydrationPolicy_Partial: StorageProviderHydrationPolicy = 0
StorageProviderHydrationPolicy_Progressive: StorageProviderHydrationPolicy = 1
StorageProviderHydrationPolicy_Full: StorageProviderHydrationPolicy = 2
StorageProviderHydrationPolicy_AlwaysFull: StorageProviderHydrationPolicy = 3
StorageProviderHydrationPolicyModifier = UInt32
StorageProviderHydrationPolicyModifier_None: StorageProviderHydrationPolicyModifier = 0
StorageProviderHydrationPolicyModifier_ValidationRequired: StorageProviderHydrationPolicyModifier = 1
StorageProviderHydrationPolicyModifier_StreamingAllowed: StorageProviderHydrationPolicyModifier = 2
StorageProviderHydrationPolicyModifier_AutoDehydrationAllowed: StorageProviderHydrationPolicyModifier = 4
StorageProviderHydrationPolicyModifier_AllowFullRestartHydration: StorageProviderHydrationPolicyModifier = 8
StorageProviderInSyncPolicy = UInt32
StorageProviderInSyncPolicy_Default: StorageProviderInSyncPolicy = 0
StorageProviderInSyncPolicy_FileCreationTime: StorageProviderInSyncPolicy = 1
StorageProviderInSyncPolicy_FileReadOnlyAttribute: StorageProviderInSyncPolicy = 2
StorageProviderInSyncPolicy_FileHiddenAttribute: StorageProviderInSyncPolicy = 4
StorageProviderInSyncPolicy_FileSystemAttribute: StorageProviderInSyncPolicy = 8
StorageProviderInSyncPolicy_DirectoryCreationTime: StorageProviderInSyncPolicy = 16
StorageProviderInSyncPolicy_DirectoryReadOnlyAttribute: StorageProviderInSyncPolicy = 32
StorageProviderInSyncPolicy_DirectoryHiddenAttribute: StorageProviderInSyncPolicy = 64
StorageProviderInSyncPolicy_DirectorySystemAttribute: StorageProviderInSyncPolicy = 128
StorageProviderInSyncPolicy_FileLastWriteTime: StorageProviderInSyncPolicy = 256
StorageProviderInSyncPolicy_DirectoryLastWriteTime: StorageProviderInSyncPolicy = 512
StorageProviderInSyncPolicy_PreserveInsyncForSyncEngine: StorageProviderInSyncPolicy = 2147483648
class StorageProviderItemProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperties'
    @winrt_classmethod
    def SetAsync(cls: win32more.Windows.Storage.Provider.IStorageProviderItemPropertiesStatics, item: win32more.Windows.Storage.IStorageItem, itemProperties: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.Provider.StorageProviderItemProperty]) -> win32more.Windows.Foundation.IAsyncAction: ...
class StorageProviderItemProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderItemProperty
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperty'
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
    Id = property(get_Id, put_Id)
    Value = property(get_Value, put_Value)
    IconResource = property(get_IconResource, put_IconResource)
class StorageProviderItemPropertyDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderItemPropertyDefinition
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemPropertyDefinition'
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
    Id = property(get_Id, put_Id)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
class StorageProviderMoreInfoUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderMoreInfoUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderMoreInfoUI'
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
    Message = property(get_Message, put_Message)
    Command = property(get_Command, put_Command)
StorageProviderPopulationPolicy = Int32
StorageProviderPopulationPolicy_Full: StorageProviderPopulationPolicy = 1
StorageProviderPopulationPolicy_AlwaysFull: StorageProviderPopulationPolicy = 2
StorageProviderProtectionMode = Int32
StorageProviderProtectionMode_Unknown: StorageProviderProtectionMode = 0
StorageProviderProtectionMode_Personal: StorageProviderProtectionMode = 1
class StorageProviderQuotaUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderQuotaUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderQuotaUI'
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
    QuotaUsedInBytes = property(get_QuotaUsedInBytes, put_QuotaUsedInBytes)
    QuotaUsedLabel = property(get_QuotaUsedLabel, put_QuotaUsedLabel)
    QuotaUsedColor = property(get_QuotaUsedColor, put_QuotaUsedColor)
StorageProviderState = Int32
StorageProviderState_InSync: StorageProviderState = 0
StorageProviderState_Syncing: StorageProviderState = 1
StorageProviderState_Paused: StorageProviderState = 2
StorageProviderState_Error: StorageProviderState = 3
StorageProviderState_Warning: StorageProviderState = 4
StorageProviderState_Offline: StorageProviderState = 5
class StorageProviderStatusUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderStatusUI
    _classid_ = 'Windows.Storage.Provider.StorageProviderStatusUI'
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
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
class StorageProviderSyncRootInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Provider.IStorageProviderSyncRootInfo
    _classid_ = 'Windows.Storage.Provider.StorageProviderSyncRootInfo'
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
    Id = property(get_Id, put_Id)
    Context = property(get_Context, put_Context)
    Path = property(get_Path, put_Path)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
    IconResource = property(get_IconResource, put_IconResource)
    HydrationPolicy = property(get_HydrationPolicy, put_HydrationPolicy)
    HydrationPolicyModifier = property(get_HydrationPolicyModifier, put_HydrationPolicyModifier)
    PopulationPolicy = property(get_PopulationPolicy, put_PopulationPolicy)
    InSyncPolicy = property(get_InSyncPolicy, put_InSyncPolicy)
    HardlinkPolicy = property(get_HardlinkPolicy, put_HardlinkPolicy)
    ShowSiblingsAsGroup = property(get_ShowSiblingsAsGroup, put_ShowSiblingsAsGroup)
    Version = property(get_Version, put_Version)
    ProtectionMode = property(get_ProtectionMode, put_ProtectionMode)
    AllowPinning = property(get_AllowPinning, put_AllowPinning)
    StorageProviderItemPropertyDefinitions = property(get_StorageProviderItemPropertyDefinitions, None)
    RecycleBinUri = property(get_RecycleBinUri, put_RecycleBinUri)
    ProviderId = property(get_ProviderId, put_ProviderId)
    FallbackFileTypeInfo = property(get_FallbackFileTypeInfo, None)
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
StorageProviderUICommandState = Int32
StorageProviderUICommandState_Enabled: StorageProviderUICommandState = 0
StorageProviderUICommandState_Disabled: StorageProviderUICommandState = 1
StorageProviderUICommandState_Hidden: StorageProviderUICommandState = 2
StorageProviderUriSourceStatus = Int32
StorageProviderUriSourceStatus_Success: StorageProviderUriSourceStatus = 0
StorageProviderUriSourceStatus_NoSyncRoot: StorageProviderUriSourceStatus = 1
StorageProviderUriSourceStatus_FileNotFound: StorageProviderUriSourceStatus = 2
UIStatus = Int32
UIStatus_Unavailable: UIStatus = 0
UIStatus_Hidden: UIStatus = 1
UIStatus_Visible: UIStatus = 2
UIStatus_Complete: UIStatus = 3
WriteActivationMode = Int32
WriteActivationMode_ReadOnly: WriteActivationMode = 0
WriteActivationMode_NotNeeded: WriteActivationMode = 1
WriteActivationMode_AfterWrite: WriteActivationMode = 2
make_head(_module, 'CachedFileUpdater')
make_head(_module, 'CachedFileUpdaterUI')
make_head(_module, 'FileUpdateRequest')
make_head(_module, 'FileUpdateRequestDeferral')
make_head(_module, 'FileUpdateRequestedEventArgs')
make_head(_module, 'ICachedFileUpdaterStatics')
make_head(_module, 'ICachedFileUpdaterUI')
make_head(_module, 'ICachedFileUpdaterUI2')
make_head(_module, 'IFileUpdateRequest')
make_head(_module, 'IFileUpdateRequest2')
make_head(_module, 'IFileUpdateRequestDeferral')
make_head(_module, 'IFileUpdateRequestedEventArgs')
make_head(_module, 'IStorageProviderFileTypeInfo')
make_head(_module, 'IStorageProviderFileTypeInfoFactory')
make_head(_module, 'IStorageProviderGetContentInfoForPathResult')
make_head(_module, 'IStorageProviderGetPathForContentUriResult')
make_head(_module, 'IStorageProviderItemPropertiesStatics')
make_head(_module, 'IStorageProviderItemProperty')
make_head(_module, 'IStorageProviderItemPropertyDefinition')
make_head(_module, 'IStorageProviderItemPropertySource')
make_head(_module, 'IStorageProviderMoreInfoUI')
make_head(_module, 'IStorageProviderPropertyCapabilities')
make_head(_module, 'IStorageProviderQuotaUI')
make_head(_module, 'IStorageProviderStatusUI')
make_head(_module, 'IStorageProviderStatusUISource')
make_head(_module, 'IStorageProviderStatusUISourceFactory')
make_head(_module, 'IStorageProviderSyncRootInfo')
make_head(_module, 'IStorageProviderSyncRootInfo2')
make_head(_module, 'IStorageProviderSyncRootInfo3')
make_head(_module, 'IStorageProviderSyncRootManagerStatics')
make_head(_module, 'IStorageProviderSyncRootManagerStatics2')
make_head(_module, 'IStorageProviderUICommand')
make_head(_module, 'IStorageProviderUriSource')
make_head(_module, 'StorageProviderFileTypeInfo')
make_head(_module, 'StorageProviderGetContentInfoForPathResult')
make_head(_module, 'StorageProviderGetPathForContentUriResult')
make_head(_module, 'StorageProviderItemProperties')
make_head(_module, 'StorageProviderItemProperty')
make_head(_module, 'StorageProviderItemPropertyDefinition')
make_head(_module, 'StorageProviderMoreInfoUI')
make_head(_module, 'StorageProviderQuotaUI')
make_head(_module, 'StorageProviderStatusUI')
make_head(_module, 'StorageProviderSyncRootInfo')
make_head(_module, 'StorageProviderSyncRootManager')
