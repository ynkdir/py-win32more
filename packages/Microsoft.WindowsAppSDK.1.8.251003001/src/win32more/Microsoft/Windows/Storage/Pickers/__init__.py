from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI
import win32more.Microsoft.Windows.Storage.Pickers
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class FileOpenPicker(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker
    _classid_ = 'Microsoft.Windows.Storage.Pickers.FileOpenPicker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.Storage.Pickers.FileOpenPicker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPickerFactory, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FileOpenPicker: ...
    @winrt_mixinmethod
    def get_ViewMode(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_mixinmethod
    def put_ViewMode(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker, value: win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def PickSingleFileAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    @winrt_mixinmethod
    def PickMultipleFilesAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class FileSavePicker(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker
    _classid_ = 'Microsoft.Windows.Storage.Pickers.FileSavePicker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.Storage.Pickers.FileSavePicker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePickerFactory, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FileSavePicker: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeChoices(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_DefaultFileExtension(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultFileExtension(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFileName(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuggestedFileName(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PickSaveFileAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    FileTypeChoices = property(get_FileTypeChoices, None)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
class FolderPicker(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker
    _classid_ = 'Microsoft.Windows.Storage.Pickers.FolderPicker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.Storage.Pickers.FolderPicker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Storage.Pickers.IFolderPickerFactory, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FolderPicker: ...
    @winrt_mixinmethod
    def get_ViewMode(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_mixinmethod
    def put_ViewMode(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker, value: win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_mixinmethod
    def put_SuggestedStartLocation(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_mixinmethod
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PickSingleFolderAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class IFileOpenPicker(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileOpenPicker'
    _iid_ = Guid('{9d00f175-c783-51bd-8c93-fb63695d3abc}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_commethod(7)
    def put_ViewMode(self, value: win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_commethod(8)
    def get_SuggestedStartLocation(self) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(9)
    def put_SuggestedStartLocation(self, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(10)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_FileTypeFilter(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def PickSingleFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    @winrt_commethod(14)
    def PickMultipleFilesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class IFileOpenPickerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileOpenPickerFactory'
    _iid_ = Guid('{315e86d7-d7a2-5d81-b379-7af78207b1af}')
    @winrt_commethod(6)
    def CreateInstance(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FileOpenPicker: ...
class IFileSavePicker(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileSavePicker'
    _iid_ = Guid('{79f1f4df-741b-59b2-aa06-fe9ac817b7dd}')
    @winrt_commethod(6)
    def get_SuggestedStartLocation(self) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(7)
    def put_SuggestedStartLocation(self, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(8)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_FileTypeChoices(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Foundation.Collections.IVector[WinRT_String]]: ...
    @winrt_commethod(11)
    def get_DefaultFileExtension(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_DefaultFileExtension(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_SuggestedFileName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_SuggestedFileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_SuggestedFolder(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_SuggestedFolder(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def PickSaveFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    FileTypeChoices = property(get_FileTypeChoices, None)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
class IFileSavePickerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileSavePickerFactory'
    _iid_ = Guid('{2e256696-30b6-5a05-a8f5-c752db6dd268}')
    @winrt_commethod(6)
    def CreateInstance(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FileSavePicker: ...
class IFolderPicker(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFolderPicker'
    _iid_ = Guid('{3ef0d1ca-97c6-5873-8ea2-02c450174290}')
    @winrt_commethod(6)
    def get_ViewMode(self) -> win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode: ...
    @winrt_commethod(7)
    def put_ViewMode(self, value: win32more.Microsoft.Windows.Storage.Pickers.PickerViewMode) -> Void: ...
    @winrt_commethod(8)
    def get_SuggestedStartLocation(self) -> win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId: ...
    @winrt_commethod(9)
    def put_SuggestedStartLocation(self, value: win32more.Microsoft.Windows.Storage.Pickers.PickerLocationId) -> Void: ...
    @winrt_commethod(10)
    def get_CommitButtonText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CommitButtonText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def PickSingleFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class IFolderPickerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFolderPickerFactory'
    _iid_ = Guid('{e1550d89-b389-5886-8395-022b1588d6a8}')
    @winrt_commethod(6)
    def CreateInstance(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Windows.Storage.Pickers.FolderPicker: ...
class IPickFileResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IPickFileResult'
    _iid_ = Guid('{e6f2e3d6-7bb0-5d81-9e7d-6fd35a1f25ab}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPickFolderResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IPickFolderResult'
    _iid_ = Guid('{6f7fd316-fe29-59d1-9343-c49cf5cde680}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class PickFileResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IPickFileResult
    _classid_ = 'Microsoft.Windows.Storage.Pickers.PickFileResult'
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Windows.Storage.Pickers.IPickFileResult) -> WinRT_String: ...
    Path = property(get_Path, None)
class PickFolderResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IPickFolderResult
    _classid_ = 'Microsoft.Windows.Storage.Pickers.PickFolderResult'
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Windows.Storage.Pickers.IPickFolderResult) -> WinRT_String: ...
    Path = property(get_Path, None)
class PickerLocationId(Enum, Int32):
    DocumentsLibrary = 0
    ComputerFolder = 1
    Desktop = 2
    Downloads = 3
    MusicLibrary = 5
    PicturesLibrary = 6
    VideosLibrary = 7
    Objects3D = 8
    Unspecified = 9
class PickerViewMode(Enum, Int32):
    List = 0
    Thumbnail = 1
StoragePickersContract: UInt32 = 65544


make_ready(__name__)
