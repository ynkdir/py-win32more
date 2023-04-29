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
import Windows.Storage.Pickers.Provider
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AddFileResult = Int32
AddFileResult_Added: AddFileResult = 0
AddFileResult_AlreadyAdded: AddFileResult = 1
AddFileResult_NotAllowed: AddFileResult = 2
AddFileResult_Unavailable: AddFileResult = 3
class FileOpenPickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.FileOpenPickerUI'
    @winrt_mixinmethod
    def AddFile(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String, file: Windows.Storage.IStorageFile) -> Windows.Storage.Pickers.Provider.AddFileResult: ...
    @winrt_mixinmethod
    def RemoveFile(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsFile(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def CanAddFile(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, file: Windows.Storage.IStorageFile) -> Boolean: ...
    @winrt_mixinmethod
    def get_AllowedFileTypes(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectionMode(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> Windows.Storage.Pickers.Provider.FileSelectionMode: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_FileRemoved(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileOpenPickerUI, Windows.Storage.Pickers.Provider.FileRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileRemoved(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closing(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileOpenPickerUI, Windows.Storage.Pickers.Provider.PickerClosingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closing(self: Windows.Storage.Pickers.Provider.IFileOpenPickerUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SelectionMode = property(get_SelectionMode, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    Title = property(get_Title, put_Title)
class FileRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.FileRemovedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: Windows.Storage.Pickers.Provider.IFileRemovedEventArgs) -> WinRT_String: ...
    Id = property(get_Id, None)
class FileSavePickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.FileSavePickerUI'
    @winrt_mixinmethod
    def get_Title(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedFileTypes(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FileName(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def TrySetFileName(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, value: WinRT_String) -> Windows.Storage.Pickers.Provider.SetFileNameResult: ...
    @winrt_mixinmethod
    def add_FileNameChanged(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileSavePickerUI, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileNameChanged(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetFileRequested(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileSavePickerUI, Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetFileRequested(self: Windows.Storage.Pickers.Provider.IFileSavePickerUI, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Title = property(get_Title, put_Title)
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    FileName = property(get_FileName, None)
FileSelectionMode = Int32
FileSelectionMode_Single: FileSelectionMode = 0
FileSelectionMode_Multiple: FileSelectionMode = 1
class IFileOpenPickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dda45a10-f9d4-40c4-8a-f5-c5-b6-b5-a6-1d-1d')
    @winrt_commethod(6)
    def AddFile(self, id: WinRT_String, file: Windows.Storage.IStorageFile) -> Windows.Storage.Pickers.Provider.AddFileResult: ...
    @winrt_commethod(7)
    def RemoveFile(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ContainsFile(self, id: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def CanAddFile(self, file: Windows.Storage.IStorageFile) -> Boolean: ...
    @winrt_commethod(10)
    def get_AllowedFileTypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_SelectionMode(self) -> Windows.Storage.Pickers.Provider.FileSelectionMode: ...
    @winrt_commethod(12)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def add_FileRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileOpenPickerUI, Windows.Storage.Pickers.Provider.FileRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_FileRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Closing(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileOpenPickerUI, Windows.Storage.Pickers.Provider.PickerClosingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Closing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SelectionMode = property(get_SelectionMode, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    Title = property(get_Title, put_Title)
class IFileRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('13043da7-7fca-4c2b-9e-ca-68-90-f9-f0-01-85')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IFileSavePickerUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9656c1e7-3e56-43cc-8a-39-33-c7-3d-9d-54-2b')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AllowedFileTypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FileName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def TrySetFileName(self, value: WinRT_String) -> Windows.Storage.Pickers.Provider.SetFileNameResult: ...
    @winrt_commethod(12)
    def add_FileNameChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileSavePickerUI, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_FileNameChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_TargetFileRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Storage.Pickers.Provider.FileSavePickerUI, Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_TargetFileRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Title = property(get_Title, put_Title)
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    FileName = property(get_FileName, None)
class IPickerClosingDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7af7f71e-1a67-4a31-ae-80-e9-07-70-8a-61-9b')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPickerClosingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e59f224-b332-4f12-8b-9f-a8-c2-f0-6b-32-cd')
    @winrt_commethod(6)
    def get_ClosingOperation(self) -> Windows.Storage.Pickers.Provider.PickerClosingOperation: ...
    @winrt_commethod(7)
    def get_IsCanceled(self) -> Boolean: ...
    ClosingOperation = property(get_ClosingOperation, None)
    IsCanceled = property(get_IsCanceled, None)
class IPickerClosingOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4ce9fb84-beee-4e39-a7-73-fc-5f-0e-ae-32-8d')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Storage.Pickers.Provider.PickerClosingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class ITargetFileRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('42bd3355-7f88-478b-8e-81-69-0b-20-34-06-78')
    @winrt_commethod(6)
    def get_TargetFile(self) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def put_TargetFile(self, value: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Storage.Pickers.Provider.TargetFileRequestDeferral: ...
    TargetFile = property(get_TargetFile, put_TargetFile)
class ITargetFileRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4aee9d91-bf15-4da9-95-f6-f6-b7-d5-58-22-5b')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ITargetFileRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b163dbc1-1b51-4c89-a5-91-0f-d4-0b-3c-57-c9')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Storage.Pickers.Provider.TargetFileRequest: ...
    Request = property(get_Request, None)
class PickerClosingDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.PickerClosingDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Storage.Pickers.Provider.IPickerClosingDeferral) -> Void: ...
class PickerClosingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.PickerClosingEventArgs'
    @winrt_mixinmethod
    def get_ClosingOperation(self: Windows.Storage.Pickers.Provider.IPickerClosingEventArgs) -> Windows.Storage.Pickers.Provider.PickerClosingOperation: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: Windows.Storage.Pickers.Provider.IPickerClosingEventArgs) -> Boolean: ...
    ClosingOperation = property(get_ClosingOperation, None)
    IsCanceled = property(get_IsCanceled, None)
class PickerClosingOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.PickerClosingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Storage.Pickers.Provider.IPickerClosingOperation) -> Windows.Storage.Pickers.Provider.PickerClosingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Storage.Pickers.Provider.IPickerClosingOperation) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
SetFileNameResult = Int32
SetFileNameResult_Succeeded: SetFileNameResult = 0
SetFileNameResult_NotAllowed: SetFileNameResult = 1
SetFileNameResult_Unavailable: SetFileNameResult = 2
class TargetFileRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.TargetFileRequest'
    @winrt_mixinmethod
    def get_TargetFile(self: Windows.Storage.Pickers.Provider.ITargetFileRequest) -> Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def put_TargetFile(self: Windows.Storage.Pickers.Provider.ITargetFileRequest, value: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Storage.Pickers.Provider.ITargetFileRequest) -> Windows.Storage.Pickers.Provider.TargetFileRequestDeferral: ...
    TargetFile = property(get_TargetFile, put_TargetFile)
class TargetFileRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.TargetFileRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Storage.Pickers.Provider.ITargetFileRequestDeferral) -> Void: ...
class TargetFileRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Storage.Pickers.Provider.ITargetFileRequestedEventArgs) -> Windows.Storage.Pickers.Provider.TargetFileRequest: ...
    Request = property(get_Request, None)
make_head(_module, 'FileOpenPickerUI')
make_head(_module, 'FileRemovedEventArgs')
make_head(_module, 'FileSavePickerUI')
make_head(_module, 'IFileOpenPickerUI')
make_head(_module, 'IFileRemovedEventArgs')
make_head(_module, 'IFileSavePickerUI')
make_head(_module, 'IPickerClosingDeferral')
make_head(_module, 'IPickerClosingEventArgs')
make_head(_module, 'IPickerClosingOperation')
make_head(_module, 'ITargetFileRequest')
make_head(_module, 'ITargetFileRequestDeferral')
make_head(_module, 'ITargetFileRequestedEventArgs')
make_head(_module, 'PickerClosingDeferral')
make_head(_module, 'PickerClosingEventArgs')
make_head(_module, 'PickerClosingOperation')
make_head(_module, 'TargetFileRequest')
make_head(_module, 'TargetFileRequestDeferral')
make_head(_module, 'TargetFileRequestedEventArgs')
