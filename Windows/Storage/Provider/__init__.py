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
import Windows.Storage.Provider
import Windows.Storage.Streams
import Windows.UI
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.CachedFileUpdater'
    @winrt_classmethod
    def SetUpdateInformation(cls: Windows.Storage.Provider.ICachedFileUpdaterStatics, file: Windows.Storage.IStorageFile, contentId: WinRT_String, readMode: Windows.Storage.Provider.ReadActivationMode, writeMode: Windows.Storage.Provider.WriteActivationMode, options: Windows.Storage.Provider.CachedFileOptions) -> Void: ...
class CachedFileUpdaterUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.CachedFileUpdaterUI'
    @winrt_mixinmethod
    def get_Title(self: Windows.Storage.Provider.ICachedFileUpdaterUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Storage.Provider.ICachedFileUpdaterUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateTarget(self: Windows.Storage.Provider.ICachedFileUpdaterUI) -> Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_mixinmethod
    def add_FileUpdateRequested(self: Windows.Storage.Provider.ICachedFileUpdaterUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Provider.CachedFileUpdaterUI, Windows.Storage.Provider.FileUpdateRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileUpdateRequested(self: Windows.Storage.Provider.ICachedFileUpdaterUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UIRequested(self: Windows.Storage.Provider.ICachedFileUpdaterUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Provider.CachedFileUpdaterUI, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UIRequested(self: Windows.Storage.Provider.ICachedFileUpdaterUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_UIStatus(self: Windows.Storage.Provider.ICachedFileUpdaterUI) -> Windows.Storage.Provider.UIStatus: ...
    @winrt_mixinmethod
    def get_UpdateRequest(self: Windows.Storage.Provider.ICachedFileUpdaterUI2) -> Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Storage.Provider.ICachedFileUpdaterUI2) -> Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    Title = property(get_Title, put_Title)
    UpdateTarget = property(get_UpdateTarget, None)
    UIStatus = property(get_UIStatus, None)
    UpdateRequest = property(get_UpdateRequest, None)
CloudFilesContract: UInt32 = 458752
class FileUpdateRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequest'
    @winrt_mixinmethod
    def get_ContentId(self: Windows.Storage.Provider.IFileUpdateRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Storage.Provider.IFileUpdateRequest) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Storage.Provider.IFileUpdateRequest) -> Windows.Storage.Provider.FileUpdateStatus: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Storage.Provider.IFileUpdateRequest, value: Windows.Storage.Provider.FileUpdateStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Storage.Provider.IFileUpdateRequest) -> Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    @winrt_mixinmethod
    def UpdateLocalFile(self: Windows.Storage.Provider.IFileUpdateRequest, value: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def get_UserInputNeededMessage(self: Windows.Storage.Provider.IFileUpdateRequest2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserInputNeededMessage(self: Windows.Storage.Provider.IFileUpdateRequest2, value: WinRT_String) -> Void: ...
    ContentId = property(get_ContentId, None)
    File = property(get_File, None)
    Status = property(get_Status, put_Status)
    UserInputNeededMessage = property(get_UserInputNeededMessage, put_UserInputNeededMessage)
class FileUpdateRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Storage.Provider.IFileUpdateRequestDeferral) -> Void: ...
class FileUpdateRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.FileUpdateRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Storage.Provider.IFileUpdateRequestedEventArgs) -> Windows.Storage.Provider.FileUpdateRequest: ...
    Request = property(get_Request, None)
FileUpdateStatus = Int32
FileUpdateStatus_Incomplete: FileUpdateStatus = 0
FileUpdateStatus_Complete: FileUpdateStatus = 1
FileUpdateStatus_UserInputNeeded: FileUpdateStatus = 2
FileUpdateStatus_CurrentlyUnavailable: FileUpdateStatus = 3
FileUpdateStatus_Failed: FileUpdateStatus = 4
FileUpdateStatus_CompleteAndRenamed: FileUpdateStatus = 5
class ICachedFileUpdaterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9fc90920-7bcf-4888-a8-1e-10-2d-70-34-d7-ce')
    @winrt_commethod(6)
    def SetUpdateInformation(self, file: Windows.Storage.IStorageFile, contentId: WinRT_String, readMode: Windows.Storage.Provider.ReadActivationMode, writeMode: Windows.Storage.Provider.WriteActivationMode, options: Windows.Storage.Provider.CachedFileOptions) -> Void: ...
class ICachedFileUpdaterUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e6f41e6-baf2-4a97-b6-00-93-33-f5-df-80-fd')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateTarget(self) -> Windows.Storage.Provider.CachedFileTarget: ...
    @winrt_commethod(9)
    def add_FileUpdateRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Provider.CachedFileUpdaterUI, Windows.Storage.Provider.FileUpdateRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_FileUpdateRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_UIRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Provider.CachedFileUpdaterUI, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UIRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_UIStatus(self) -> Windows.Storage.Provider.UIStatus: ...
    Title = property(get_Title, put_Title)
    UpdateTarget = property(get_UpdateTarget, None)
    UIStatus = property(get_UIStatus, None)
class ICachedFileUpdaterUI2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8856a21c-8699-4340-9f-49-f7-ca-d7-fe-89-91')
    @winrt_commethod(6)
    def get_UpdateRequest(self) -> Windows.Storage.Provider.FileUpdateRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    UpdateRequest = property(get_UpdateRequest, None)
class IFileUpdateRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('40c82536-c1fe-4d93-a7-92-1e-73-6b-c7-08-37')
    @winrt_commethod(6)
    def get_ContentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Storage.Provider.FileUpdateStatus: ...
    @winrt_commethod(9)
    def put_Status(self, value: Windows.Storage.Provider.FileUpdateStatus) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.Storage.Provider.FileUpdateRequestDeferral: ...
    @winrt_commethod(11)
    def UpdateLocalFile(self, value: Windows.Storage.IStorageFile) -> Void: ...
    ContentId = property(get_ContentId, None)
    File = property(get_File, None)
    Status = property(get_Status, put_Status)
class IFileUpdateRequest2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('82484648-bdbe-447b-a2-ee-7a-fe-6a-03-2a-94')
    @winrt_commethod(6)
    def get_UserInputNeededMessage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UserInputNeededMessage(self, value: WinRT_String) -> Void: ...
    UserInputNeededMessage = property(get_UserInputNeededMessage, put_UserInputNeededMessage)
class IFileUpdateRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ffcedb2b-8ade-44a5-bb-00-16-4c-4e-72-f1-3a')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IFileUpdateRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7b0a9342-3905-438d-aa-ef-78-ae-26-5f-8d-d2')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Storage.Provider.FileUpdateRequest: ...
    Request = property(get_Request, None)
class IStorageProviderFileTypeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1955b9c1-0184-5a88-87-df-45-44-f4-64-36-5d')
    @winrt_commethod(6)
    def get_FileExtension(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IconResource(self) -> WinRT_String: ...
    FileExtension = property(get_FileExtension, None)
    IconResource = property(get_IconResource, None)
class IStorageProviderFileTypeInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3fa12c6f-cce6-5d5d-80-b1-38-9e-7c-f9-2d-bf')
    @winrt_commethod(6)
    def CreateInstance(self, fileExtension: WinRT_String, iconResource: WinRT_String) -> Windows.Storage.Provider.StorageProviderFileTypeInfo: ...
class IStorageProviderGetContentInfoForPathResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2564711d-aa89-4d12-82-e3-f7-2a-92-e3-39-66')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_commethod(7)
    def put_Status(self, value: Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('63711a9d-4118-45a6-ac-b6-22-c4-9d-01-9f-40')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_commethod(7)
    def put_Status(self, value: Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_commethod(8)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Path(self, value: WinRT_String) -> Void: ...
    Status = property(get_Status, put_Status)
    Path = property(get_Path, put_Path)
class IStorageProviderItemPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2d2c1c97-2704-4729-8f-a9-7e-6b-8e-15-8c-2f')
    @winrt_commethod(6)
    def SetAsync(self, item: Windows.Storage.IStorageItem, itemProperties: Windows.Foundation.Collections.IIterable[Windows.Storage.Provider.StorageProviderItemProperty]) -> Windows.Foundation.IAsyncAction: ...
class IStorageProviderItemProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('476cb558-730b-4188-b7-b5-63-b7-16-ed-47-6d')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c5b383bb-ff1f-4298-83-1e-ff-1c-08-08-96-90')
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8f6f9c3e-f632-4a9b-8d-99-d2-d7-a1-1d-f5-6a')
    @winrt_commethod(6)
    def GetItemProperties(self, itemPath: WinRT_String) -> Windows.Foundation.Collections.IIterable[Windows.Storage.Provider.StorageProviderItemProperty]: ...
class IStorageProviderMoreInfoUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ef38e591-a7cb-5e7d-9b-5e-22-74-98-42-69-7c')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Command(self) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(9)
    def put_Command(self, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    Message = property(get_Message, put_Message)
    Command = property(get_Command, put_Command)
class IStorageProviderPropertyCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('658d2f0e-63b7-4567-ac-f9-51-ab-e3-01-dd-a5')
    @winrt_commethod(6)
    def IsPropertySupported(self, propertyCanonicalName: WinRT_String) -> Boolean: ...
class IStorageProviderQuotaUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ba6295c3-312e-544f-9f-d5-1f-81-b2-1f-36-49')
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
    def get_QuotaUsedColor(self) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_commethod(13)
    def put_QuotaUsedColor(self, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
    QuotaTotalInBytes = property(get_QuotaTotalInBytes, put_QuotaTotalInBytes)
    QuotaUsedInBytes = property(get_QuotaUsedInBytes, put_QuotaUsedInBytes)
    QuotaUsedLabel = property(get_QuotaUsedLabel, put_QuotaUsedLabel)
    QuotaUsedColor = property(get_QuotaUsedColor, put_QuotaUsedColor)
class IStorageProviderStatusUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d6b6a758-198d-5b80-97-7f-5f-f7-3d-a3-31-18')
    @winrt_commethod(6)
    def get_ProviderState(self) -> Windows.Storage.Provider.StorageProviderState: ...
    @winrt_commethod(7)
    def put_ProviderState(self, value: Windows.Storage.Provider.StorageProviderState) -> Void: ...
    @winrt_commethod(8)
    def get_ProviderStateLabel(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_ProviderStateLabel(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ProviderStateIcon(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_ProviderStateIcon(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(12)
    def get_SyncStatusCommand(self) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(13)
    def put_SyncStatusCommand(self, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_commethod(14)
    def get_QuotaUI(self) -> Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_commethod(15)
    def put_QuotaUI(self, value: Windows.Storage.Provider.StorageProviderQuotaUI) -> Void: ...
    @winrt_commethod(16)
    def get_MoreInfoUI(self) -> Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_commethod(17)
    def put_MoreInfoUI(self, value: Windows.Storage.Provider.StorageProviderMoreInfoUI) -> Void: ...
    @winrt_commethod(18)
    def get_ProviderPrimaryCommand(self) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_commethod(19)
    def put_ProviderPrimaryCommand(self, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_commethod(20)
    def get_ProviderSecondaryCommands(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.IStorageProviderUICommand]: ...
    @winrt_commethod(21)
    def put_ProviderSecondaryCommands(self, value: Windows.Foundation.Collections.IVector[Windows.Storage.Provider.IStorageProviderUICommand]) -> Void: ...
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
class IStorageProviderStatusUISource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a306c249-3d66-5e70-90-07-e4-3d-f9-60-51-ff')
    @winrt_commethod(6)
    def GetStatusUI(self) -> Windows.Storage.Provider.StorageProviderStatusUI: ...
    @winrt_commethod(7)
    def add_StatusUIChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Provider.IStorageProviderStatusUISource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StatusUIChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IStorageProviderStatusUISourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('12e46b74-4e5a-58d1-a6-2f-03-76-e8-ee-7d-d8')
    @winrt_commethod(6)
    def GetStatusUISource(self, syncRootId: WinRT_String) -> Windows.Storage.Provider.IStorageProviderStatusUISource: ...
class IStorageProviderSyncRootInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7c1305c4-99f9-41ac-89-04-ab-05-5d-65-49-26')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Context(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Context(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_Path(self) -> Windows.Storage.IStorageFolder: ...
    @winrt_commethod(11)
    def put_Path(self, value: Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_commethod(12)
    def get_DisplayNameResource(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_DisplayNameResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_IconResource(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_IconResource(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_HydrationPolicy(self) -> Windows.Storage.Provider.StorageProviderHydrationPolicy: ...
    @winrt_commethod(17)
    def put_HydrationPolicy(self, value: Windows.Storage.Provider.StorageProviderHydrationPolicy) -> Void: ...
    @winrt_commethod(18)
    def get_HydrationPolicyModifier(self) -> Windows.Storage.Provider.StorageProviderHydrationPolicyModifier: ...
    @winrt_commethod(19)
    def put_HydrationPolicyModifier(self, value: Windows.Storage.Provider.StorageProviderHydrationPolicyModifier) -> Void: ...
    @winrt_commethod(20)
    def get_PopulationPolicy(self) -> Windows.Storage.Provider.StorageProviderPopulationPolicy: ...
    @winrt_commethod(21)
    def put_PopulationPolicy(self, value: Windows.Storage.Provider.StorageProviderPopulationPolicy) -> Void: ...
    @winrt_commethod(22)
    def get_InSyncPolicy(self) -> Windows.Storage.Provider.StorageProviderInSyncPolicy: ...
    @winrt_commethod(23)
    def put_InSyncPolicy(self, value: Windows.Storage.Provider.StorageProviderInSyncPolicy) -> Void: ...
    @winrt_commethod(24)
    def get_HardlinkPolicy(self) -> Windows.Storage.Provider.StorageProviderHardlinkPolicy: ...
    @winrt_commethod(25)
    def put_HardlinkPolicy(self, value: Windows.Storage.Provider.StorageProviderHardlinkPolicy) -> Void: ...
    @winrt_commethod(26)
    def get_ShowSiblingsAsGroup(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_ShowSiblingsAsGroup(self, value: Boolean) -> Void: ...
    @winrt_commethod(28)
    def get_Version(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def put_Version(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(30)
    def get_ProtectionMode(self) -> Windows.Storage.Provider.StorageProviderProtectionMode: ...
    @winrt_commethod(31)
    def put_ProtectionMode(self, value: Windows.Storage.Provider.StorageProviderProtectionMode) -> Void: ...
    @winrt_commethod(32)
    def get_AllowPinning(self) -> Boolean: ...
    @winrt_commethod(33)
    def put_AllowPinning(self, value: Boolean) -> Void: ...
    @winrt_commethod(34)
    def get_StorageProviderItemPropertyDefinitions(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.StorageProviderItemPropertyDefinition]: ...
    @winrt_commethod(35)
    def get_RecycleBinUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(36)
    def put_RecycleBinUri(self, value: Windows.Foundation.Uri) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cf51b023-7cf1-5166-bd-ba-ef-d9-5f-52-9e-31')
    @winrt_commethod(6)
    def get_ProviderId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_ProviderId(self, value: Guid) -> Void: ...
    ProviderId = property(get_ProviderId, put_ProviderId)
class IStorageProviderSyncRootInfo3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('507a6617-bef6-56fd-85-5e-75-ac-e2-e4-5c-f5')
    @winrt_commethod(6)
    def get_FallbackFileTypeInfo(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.StorageProviderFileTypeInfo]: ...
    FallbackFileTypeInfo = property(get_FallbackFileTypeInfo, None)
class IStorageProviderSyncRootManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3e99fbbf-8fe3-4b40-ab-c7-f6-fc-3d-74-c9-8e')
    @winrt_commethod(6)
    def Register(self, syncRootInformation: Windows.Storage.Provider.StorageProviderSyncRootInfo) -> Void: ...
    @winrt_commethod(7)
    def Unregister(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def GetSyncRootInformationForFolder(self, folder: Windows.Storage.IStorageFolder) -> Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_commethod(9)
    def GetSyncRootInformationForId(self, id: WinRT_String) -> Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_commethod(10)
    def GetCurrentSyncRoots(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.Provider.StorageProviderSyncRootInfo]: ...
class IStorageProviderSyncRootManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('efb6cfee-1374-544e-9d-f1-55-98-d2-e9-cf-dd')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IStorageProviderUICommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0c3e0760-d846-568f-94-84-10-5c-c5-7b-50-2b')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Icon(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Storage.Provider.StorageProviderUICommandState: ...
    @winrt_commethod(10)
    def Invoke(self) -> Void: ...
    Label = property(get_Label, None)
    Description = property(get_Description, None)
    Icon = property(get_Icon, None)
    State = property(get_State, None)
class IStorageProviderUriSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b29806d1-8be0-4962-8b-b6-0d-4c-2e-14-d4-7a')
    @winrt_commethod(6)
    def GetPathForContentUri(self, contentUri: WinRT_String, result: Windows.Storage.Provider.StorageProviderGetPathForContentUriResult) -> Void: ...
    @winrt_commethod(7)
    def GetContentInfoForPath(self, path: WinRT_String, result: Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult) -> Void: ...
ReadActivationMode = Int32
ReadActivationMode_NotNeeded: ReadActivationMode = 0
ReadActivationMode_BeforeAccess: ReadActivationMode = 1
class StorageProviderFileTypeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderFileTypeInfo'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Storage.Provider.IStorageProviderFileTypeInfoFactory, fileExtension: WinRT_String, iconResource: WinRT_String) -> Windows.Storage.Provider.StorageProviderFileTypeInfo: ...
    @winrt_mixinmethod
    def get_FileExtension(self: Windows.Storage.Provider.IStorageProviderFileTypeInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IconResource(self: Windows.Storage.Provider.IStorageProviderFileTypeInfo) -> WinRT_String: ...
    FileExtension = property(get_FileExtension, None)
    IconResource = property(get_IconResource, None)
class StorageProviderGetContentInfoForPathResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderGetContentInfoForPathResult: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_ContentUri(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentUri(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentId(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentId(self: Windows.Storage.Provider.IStorageProviderGetContentInfoForPathResult, value: WinRT_String) -> Void: ...
    Status = property(get_Status, put_Status)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentId = property(get_ContentId, put_ContentId)
class StorageProviderGetPathForContentUriResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderGetPathForContentUriResult'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderGetPathForContentUriResult: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult) -> Windows.Storage.Provider.StorageProviderUriSourceStatus: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult, value: Windows.Storage.Provider.StorageProviderUriSourceStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.Storage.Provider.IStorageProviderGetPathForContentUriResult, value: WinRT_String) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperties'
    @winrt_classmethod
    def SetAsync(cls: Windows.Storage.Provider.IStorageProviderItemPropertiesStatics, item: Windows.Storage.IStorageItem, itemProperties: Windows.Foundation.Collections.IIterable[Windows.Storage.Provider.StorageProviderItemProperty]) -> Windows.Foundation.IAsyncAction: ...
class StorageProviderItemProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemProperty'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderItemProperty: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Storage.Provider.IStorageProviderItemProperty, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.Provider.IStorageProviderItemProperty) -> Int32: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Storage.Provider.IStorageProviderItemProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Storage.Provider.IStorageProviderItemProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IconResource(self: Windows.Storage.Provider.IStorageProviderItemProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconResource(self: Windows.Storage.Provider.IStorageProviderItemProperty) -> WinRT_String: ...
    Id = property(get_Id, put_Id)
    Value = property(get_Value, put_Value)
    IconResource = property(get_IconResource, put_IconResource)
class StorageProviderItemPropertyDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderItemPropertyDefinition'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderItemPropertyDefinition: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.Provider.IStorageProviderItemPropertyDefinition) -> Int32: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Storage.Provider.IStorageProviderItemPropertyDefinition, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: Windows.Storage.Provider.IStorageProviderItemPropertyDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayNameResource(self: Windows.Storage.Provider.IStorageProviderItemPropertyDefinition, value: WinRT_String) -> Void: ...
    Id = property(get_Id, put_Id)
    DisplayNameResource = property(get_DisplayNameResource, put_DisplayNameResource)
class StorageProviderMoreInfoUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderMoreInfoUI'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Storage.Provider.IStorageProviderMoreInfoUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: Windows.Storage.Provider.IStorageProviderMoreInfoUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Command(self: Windows.Storage.Provider.IStorageProviderMoreInfoUI) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_Command(self: Windows.Storage.Provider.IStorageProviderMoreInfoUI, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    Message = property(get_Message, put_Message)
    Command = property(get_Command, put_Command)
StorageProviderPopulationPolicy = Int32
StorageProviderPopulationPolicy_Full: StorageProviderPopulationPolicy = 1
StorageProviderPopulationPolicy_AlwaysFull: StorageProviderPopulationPolicy = 2
StorageProviderProtectionMode = Int32
StorageProviderProtectionMode_Unknown: StorageProviderProtectionMode = 0
StorageProviderProtectionMode_Personal: StorageProviderProtectionMode = 1
class StorageProviderQuotaUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderQuotaUI'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_mixinmethod
    def get_QuotaTotalInBytes(self: Windows.Storage.Provider.IStorageProviderQuotaUI) -> UInt64: ...
    @winrt_mixinmethod
    def put_QuotaTotalInBytes(self: Windows.Storage.Provider.IStorageProviderQuotaUI, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedInBytes(self: Windows.Storage.Provider.IStorageProviderQuotaUI) -> UInt64: ...
    @winrt_mixinmethod
    def put_QuotaUsedInBytes(self: Windows.Storage.Provider.IStorageProviderQuotaUI, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedLabel(self: Windows.Storage.Provider.IStorageProviderQuotaUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_QuotaUsedLabel(self: Windows.Storage.Provider.IStorageProviderQuotaUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUsedColor(self: Windows.Storage.Provider.IStorageProviderQuotaUI) -> Windows.Foundation.IReference[Windows.UI.Color]: ...
    @winrt_mixinmethod
    def put_QuotaUsedColor(self: Windows.Storage.Provider.IStorageProviderQuotaUI, value: Windows.Foundation.IReference[Windows.UI.Color]) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderStatusUI'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderStatusUI: ...
    @winrt_mixinmethod
    def get_ProviderState(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Storage.Provider.StorageProviderState: ...
    @winrt_mixinmethod
    def put_ProviderState(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Storage.Provider.StorageProviderState) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderStateLabel(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProviderStateLabel(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderStateIcon(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ProviderStateIcon(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_SyncStatusCommand(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_SyncStatusCommand(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_mixinmethod
    def get_QuotaUI(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Storage.Provider.StorageProviderQuotaUI: ...
    @winrt_mixinmethod
    def put_QuotaUI(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Storage.Provider.StorageProviderQuotaUI) -> Void: ...
    @winrt_mixinmethod
    def get_MoreInfoUI(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Storage.Provider.StorageProviderMoreInfoUI: ...
    @winrt_mixinmethod
    def put_MoreInfoUI(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Storage.Provider.StorageProviderMoreInfoUI) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderPrimaryCommand(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Storage.Provider.IStorageProviderUICommand: ...
    @winrt_mixinmethod
    def put_ProviderPrimaryCommand(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Storage.Provider.IStorageProviderUICommand) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderSecondaryCommands(self: Windows.Storage.Provider.IStorageProviderStatusUI) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.IStorageProviderUICommand]: ...
    @winrt_mixinmethod
    def put_ProviderSecondaryCommands(self: Windows.Storage.Provider.IStorageProviderStatusUI, value: Windows.Foundation.Collections.IVector[Windows.Storage.Provider.IStorageProviderUICommand]) -> Void: ...
    ProviderState = property(get_ProviderState, put_ProviderState)
    ProviderStateLabel = property(get_ProviderStateLabel, put_ProviderStateLabel)
    ProviderStateIcon = property(get_ProviderStateIcon, put_ProviderStateIcon)
    SyncStatusCommand = property(get_SyncStatusCommand, put_SyncStatusCommand)
    QuotaUI = property(get_QuotaUI, put_QuotaUI)
    MoreInfoUI = property(get_MoreInfoUI, put_MoreInfoUI)
    ProviderPrimaryCommand = property(get_ProviderPrimaryCommand, put_ProviderPrimaryCommand)
    ProviderSecondaryCommands = property(get_ProviderSecondaryCommands, put_ProviderSecondaryCommands)
class StorageProviderSyncRootInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderSyncRootInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Context(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Context(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.IStorageFolder: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayNameResource(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayNameResource(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IconResource(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IconResource(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HydrationPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderHydrationPolicy: ...
    @winrt_mixinmethod
    def put_HydrationPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderHydrationPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_HydrationPolicyModifier(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderHydrationPolicyModifier: ...
    @winrt_mixinmethod
    def put_HydrationPolicyModifier(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderHydrationPolicyModifier) -> Void: ...
    @winrt_mixinmethod
    def get_PopulationPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderPopulationPolicy: ...
    @winrt_mixinmethod
    def put_PopulationPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderPopulationPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_InSyncPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderInSyncPolicy: ...
    @winrt_mixinmethod
    def put_InSyncPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderInSyncPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_HardlinkPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderHardlinkPolicy: ...
    @winrt_mixinmethod
    def put_HardlinkPolicy(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderHardlinkPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_ShowSiblingsAsGroup(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowSiblingsAsGroup(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Version(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProtectionMode(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Storage.Provider.StorageProviderProtectionMode: ...
    @winrt_mixinmethod
    def put_ProtectionMode(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Storage.Provider.StorageProviderProtectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_AllowPinning(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowPinning(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StorageProviderItemPropertyDefinitions(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.StorageProviderItemPropertyDefinition]: ...
    @winrt_mixinmethod
    def get_RecycleBinUri(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_RecycleBinUri(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProviderId(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo2) -> Guid: ...
    @winrt_mixinmethod
    def put_ProviderId(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo2, value: Guid) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackFileTypeInfo(self: Windows.Storage.Provider.IStorageProviderSyncRootInfo3) -> Windows.Foundation.Collections.IVector[Windows.Storage.Provider.StorageProviderFileTypeInfo]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Provider.StorageProviderSyncRootManager'
    @winrt_classmethod
    def IsSupported(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def Register(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, syncRootInformation: Windows.Storage.Provider.StorageProviderSyncRootInfo) -> Void: ...
    @winrt_classmethod
    def Unregister(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, id: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetSyncRootInformationForFolder(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, folder: Windows.Storage.IStorageFolder) -> Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_classmethod
    def GetSyncRootInformationForId(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics, id: WinRT_String) -> Windows.Storage.Provider.StorageProviderSyncRootInfo: ...
    @winrt_classmethod
    def GetCurrentSyncRoots(cls: Windows.Storage.Provider.IStorageProviderSyncRootManagerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.Provider.StorageProviderSyncRootInfo]: ...
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
