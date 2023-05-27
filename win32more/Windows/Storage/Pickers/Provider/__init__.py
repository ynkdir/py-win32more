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
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.Pickers.Provider
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI
    _classid_ = 'Windows.Storage.Pickers.Provider.FileOpenPickerUI'
    @winrt_mixinmethod
    def AddFile(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Storage.Pickers.Provider.AddFileResult: ...
    @winrt_mixinmethod
    def RemoveFile(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ContainsFile(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, id: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def CanAddFile(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, file: win32more.Windows.Storage.IStorageFile) -> Boolean: ...
    @winrt_mixinmethod
    def get_AllowedFileTypes(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectionMode(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> win32more.Windows.Storage.Pickers.Provider.FileSelectionMode: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_FileRemoved(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI, win32more.Windows.Storage.Pickers.Provider.FileRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileRemoved(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closing(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI, win32more.Windows.Storage.Pickers.Provider.PickerClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closing(self: win32more.Windows.Storage.Pickers.Provider.IFileOpenPickerUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SelectionMode = property(get_SelectionMode, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    Title = property(get_Title, put_Title)
class FileRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IFileRemovedEventArgs
    _classid_ = 'Windows.Storage.Pickers.Provider.FileRemovedEventArgs'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Storage.Pickers.Provider.IFileRemovedEventArgs) -> WinRT_String: ...
    Id = property(get_Id, None)
class FileSavePickerUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI
    _classid_ = 'Windows.Storage.Pickers.Provider.FileSavePickerUI'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedFileTypes(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FileName(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI) -> WinRT_String: ...
    @winrt_mixinmethod
    def TrySetFileName(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, value: WinRT_String) -> win32more.Windows.Storage.Pickers.Provider.SetFileNameResult: ...
    @winrt_mixinmethod
    def add_FileNameChanged(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FileNameChanged(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetFileRequested(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI, win32more.Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetFileRequested(self: win32more.Windows.Storage.Pickers.Provider.IFileSavePickerUI, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Title = property(get_Title, put_Title)
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    FileName = property(get_FileName, None)
FileSelectionMode = Int32
FileSelectionMode_Single: FileSelectionMode = 0
FileSelectionMode_Multiple: FileSelectionMode = 1
class IFileOpenPickerUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IFileOpenPickerUI'
    _iid_ = Guid('{dda45a10-f9d4-40c4-8af5-c5b6b5a61d1d}')
    @winrt_commethod(6)
    def AddFile(self, id: WinRT_String, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Storage.Pickers.Provider.AddFileResult: ...
    @winrt_commethod(7)
    def RemoveFile(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def ContainsFile(self, id: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def CanAddFile(self, file: win32more.Windows.Storage.IStorageFile) -> Boolean: ...
    @winrt_commethod(10)
    def get_AllowedFileTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_SelectionMode(self) -> win32more.Windows.Storage.Pickers.Provider.FileSelectionMode: ...
    @winrt_commethod(12)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def add_FileRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI, win32more.Windows.Storage.Pickers.Provider.FileRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_FileRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Closing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI, win32more.Windows.Storage.Pickers.Provider.PickerClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Closing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SelectionMode = property(get_SelectionMode, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    Title = property(get_Title, put_Title)
class IFileRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IFileRemovedEventArgs'
    _iid_ = Guid('{13043da7-7fca-4c2b-9eca-6890f9f00185}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IFileSavePickerUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IFileSavePickerUI'
    _iid_ = Guid('{9656c1e7-3e56-43cc-8a39-33c73d9d542b}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AllowedFileTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_SettingsIdentifier(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FileName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def TrySetFileName(self, value: WinRT_String) -> win32more.Windows.Storage.Pickers.Provider.SetFileNameResult: ...
    @winrt_commethod(12)
    def add_FileNameChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_FileNameChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_TargetFileRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI, win32more.Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_TargetFileRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Title = property(get_Title, put_Title)
    AllowedFileTypes = property(get_AllowedFileTypes, None)
    SettingsIdentifier = property(get_SettingsIdentifier, None)
    FileName = property(get_FileName, None)
class IPickerClosingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IPickerClosingDeferral'
    _iid_ = Guid('{7af7f71e-1a67-4a31-ae80-e907708a619b}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPickerClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IPickerClosingEventArgs'
    _iid_ = Guid('{7e59f224-b332-4f12-8b9f-a8c2f06b32cd}')
    @winrt_commethod(6)
    def get_ClosingOperation(self) -> win32more.Windows.Storage.Pickers.Provider.PickerClosingOperation: ...
    @winrt_commethod(7)
    def get_IsCanceled(self) -> Boolean: ...
    ClosingOperation = property(get_ClosingOperation, None)
    IsCanceled = property(get_IsCanceled, None)
class IPickerClosingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.IPickerClosingOperation'
    _iid_ = Guid('{4ce9fb84-beee-4e39-a773-fc5f0eae328d}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Storage.Pickers.Provider.PickerClosingDeferral: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class ITargetFileRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.ITargetFileRequest'
    _iid_ = Guid('{42bd3355-7f88-478b-8e81-690b20340678}')
    @winrt_commethod(6)
    def get_TargetFile(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def put_TargetFile(self, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Storage.Pickers.Provider.TargetFileRequestDeferral: ...
    TargetFile = property(get_TargetFile, put_TargetFile)
class ITargetFileRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.ITargetFileRequestDeferral'
    _iid_ = Guid('{4aee9d91-bf15-4da9-95f6-f6b7d558225b}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ITargetFileRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.Pickers.Provider.ITargetFileRequestedEventArgs'
    _iid_ = Guid('{b163dbc1-1b51-4c89-a591-0fd40b3c57c9}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Storage.Pickers.Provider.TargetFileRequest: ...
    Request = property(get_Request, None)
class PickerClosingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IPickerClosingDeferral
    _classid_ = 'Windows.Storage.Pickers.Provider.PickerClosingDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Storage.Pickers.Provider.IPickerClosingDeferral) -> Void: ...
class PickerClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IPickerClosingEventArgs
    _classid_ = 'Windows.Storage.Pickers.Provider.PickerClosingEventArgs'
    @winrt_mixinmethod
    def get_ClosingOperation(self: win32more.Windows.Storage.Pickers.Provider.IPickerClosingEventArgs) -> win32more.Windows.Storage.Pickers.Provider.PickerClosingOperation: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Windows.Storage.Pickers.Provider.IPickerClosingEventArgs) -> Boolean: ...
    ClosingOperation = property(get_ClosingOperation, None)
    IsCanceled = property(get_IsCanceled, None)
class PickerClosingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.IPickerClosingOperation
    _classid_ = 'Windows.Storage.Pickers.Provider.PickerClosingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.Pickers.Provider.IPickerClosingOperation) -> win32more.Windows.Storage.Pickers.Provider.PickerClosingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Storage.Pickers.Provider.IPickerClosingOperation) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
SetFileNameResult = Int32
SetFileNameResult_Succeeded: SetFileNameResult = 0
SetFileNameResult_NotAllowed: SetFileNameResult = 1
SetFileNameResult_Unavailable: SetFileNameResult = 2
class TargetFileRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequest
    _classid_ = 'Windows.Storage.Pickers.Provider.TargetFileRequest'
    @winrt_mixinmethod
    def get_TargetFile(self: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequest) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def put_TargetFile(self: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequest, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequest) -> win32more.Windows.Storage.Pickers.Provider.TargetFileRequestDeferral: ...
    TargetFile = property(get_TargetFile, put_TargetFile)
class TargetFileRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequestDeferral
    _classid_ = 'Windows.Storage.Pickers.Provider.TargetFileRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequestDeferral) -> Void: ...
class TargetFileRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequestedEventArgs
    _classid_ = 'Windows.Storage.Pickers.Provider.TargetFileRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Storage.Pickers.Provider.ITargetFileRequestedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.TargetFileRequest: ...
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
