from __future__ import annotations
from win32more._prelude import *
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
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> hstr: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeFilter(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.Collections.IVector[hstr]: ...
    @winrt_mixinmethod
    def PickSingleFileAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    @winrt_mixinmethod
    def PickMultipleFilesAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]]: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeChoices(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> win32more.Windows.Foundation.Collections.IMap[hstr, win32more.Windows.Foundation.Collections.IVector[hstr]]: ...
    @winrt_mixinmethod
    def get_InitialFileTypeIndex(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> Int32: ...
    @winrt_mixinmethod
    def put_InitialFileTypeIndex(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileOpenPicker2, value: hstr) -> Void: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeChoices = property(get_FileTypeChoices, None)
    FileTypeFilter = property(get_FileTypeFilter, None)
    InitialFileTypeIndex = property(get_InitialFileTypeIndex, put_InitialFileTypeIndex)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    Title = property(get_Title, put_Title)
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
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> hstr: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypeChoices(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.Collections.IMap[hstr, win32more.Windows.Foundation.Collections.IVector[hstr]]: ...
    @winrt_mixinmethod
    def get_DefaultFileExtension(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> hstr: ...
    @winrt_mixinmethod
    def put_DefaultFileExtension(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFileName(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedFileName(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def PickSaveFileAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_InitialFileTypeIndex(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2) -> Int32: ...
    @winrt_mixinmethod
    def put_InitialFileTypeIndex(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_ShowOverwritePrompt(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowOverwritePrompt(self: win32more.Microsoft.Windows.Storage.Pickers.IFileSavePicker2, value: Boolean) -> Void: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    FileTypeChoices = property(get_FileTypeChoices, None)
    InitialFileTypeIndex = property(get_InitialFileTypeIndex, put_InitialFileTypeIndex)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    ShowOverwritePrompt = property(get_ShowOverwritePrompt, put_ShowOverwritePrompt)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    Title = property(get_Title, put_Title)
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
    def get_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> hstr: ...
    @winrt_mixinmethod
    def put_CommitButtonText(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def PickSingleFolderAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SettingsIdentifier(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2) -> hstr: ...
    @winrt_mixinmethod
    def put_SuggestedStartFolder(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2, value: hstr) -> Void: ...
    @winrt_mixinmethod
    def PickMultipleFoldersAsync(self: win32more.Microsoft.Windows.Storage.Pickers.IFolderPicker2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    Title = property(get_Title, put_Title)
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
    def get_CommitButtonText(self) -> hstr: ...
    @winrt_commethod(11)
    def put_CommitButtonText(self, value: hstr) -> Void: ...
    @winrt_commethod(12)
    def get_FileTypeFilter(self) -> win32more.Windows.Foundation.Collections.IVector[hstr]: ...
    @winrt_commethod(13)
    def PickSingleFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    @winrt_commethod(14)
    def PickMultipleFilesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    FileTypeFilter = property(get_FileTypeFilter, None)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class IFileOpenPicker2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileOpenPicker2'
    _iid_ = Guid('{b77a4106-895b-5af9-91c3-93e5b058706c}')
    @winrt_commethod(6)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Title(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_SettingsIdentifier(self) -> hstr: ...
    @winrt_commethod(9)
    def put_SettingsIdentifier(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_FileTypeChoices(self) -> win32more.Windows.Foundation.Collections.IMap[hstr, win32more.Windows.Foundation.Collections.IVector[hstr]]: ...
    @winrt_commethod(11)
    def get_InitialFileTypeIndex(self) -> Int32: ...
    @winrt_commethod(12)
    def put_InitialFileTypeIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(13)
    def get_SuggestedFolder(self) -> hstr: ...
    @winrt_commethod(14)
    def put_SuggestedFolder(self, value: hstr) -> Void: ...
    @winrt_commethod(15)
    def get_SuggestedStartFolder(self) -> hstr: ...
    @winrt_commethod(16)
    def put_SuggestedStartFolder(self, value: hstr) -> Void: ...
    FileTypeChoices = property(get_FileTypeChoices, None)
    InitialFileTypeIndex = property(get_InitialFileTypeIndex, put_InitialFileTypeIndex)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    Title = property(get_Title, put_Title)
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
    def get_CommitButtonText(self) -> hstr: ...
    @winrt_commethod(9)
    def put_CommitButtonText(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_FileTypeChoices(self) -> win32more.Windows.Foundation.Collections.IMap[hstr, win32more.Windows.Foundation.Collections.IVector[hstr]]: ...
    @winrt_commethod(11)
    def get_DefaultFileExtension(self) -> hstr: ...
    @winrt_commethod(12)
    def put_DefaultFileExtension(self, value: hstr) -> Void: ...
    @winrt_commethod(13)
    def get_SuggestedFileName(self) -> hstr: ...
    @winrt_commethod(14)
    def put_SuggestedFileName(self, value: hstr) -> Void: ...
    @winrt_commethod(15)
    def get_SuggestedFolder(self) -> hstr: ...
    @winrt_commethod(16)
    def put_SuggestedFolder(self, value: hstr) -> Void: ...
    @winrt_commethod(17)
    def PickSaveFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFileResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    DefaultFileExtension = property(get_DefaultFileExtension, put_DefaultFileExtension)
    FileTypeChoices = property(get_FileTypeChoices, None)
    SuggestedFileName = property(get_SuggestedFileName, put_SuggestedFileName)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
class IFileSavePicker2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFileSavePicker2'
    _iid_ = Guid('{a18feba7-3fbc-5ecb-9693-ba876a9c0c27}')
    @winrt_commethod(6)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Title(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_SettingsIdentifier(self) -> hstr: ...
    @winrt_commethod(9)
    def put_SettingsIdentifier(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_InitialFileTypeIndex(self) -> Int32: ...
    @winrt_commethod(11)
    def put_InitialFileTypeIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_SuggestedStartFolder(self) -> hstr: ...
    @winrt_commethod(13)
    def put_SuggestedStartFolder(self, value: hstr) -> Void: ...
    @winrt_commethod(14)
    def get_ShowOverwritePrompt(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_ShowOverwritePrompt(self, value: Boolean) -> Void: ...
    InitialFileTypeIndex = property(get_InitialFileTypeIndex, put_InitialFileTypeIndex)
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    ShowOverwritePrompt = property(get_ShowOverwritePrompt, put_ShowOverwritePrompt)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    Title = property(get_Title, put_Title)
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
    def get_CommitButtonText(self) -> hstr: ...
    @winrt_commethod(11)
    def put_CommitButtonText(self, value: hstr) -> Void: ...
    @winrt_commethod(12)
    def PickSingleFolderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]: ...
    CommitButtonText = property(get_CommitButtonText, put_CommitButtonText)
    SuggestedStartLocation = property(get_SuggestedStartLocation, put_SuggestedStartLocation)
    ViewMode = property(get_ViewMode, put_ViewMode)
class IFolderPicker2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IFolderPicker2'
    _iid_ = Guid('{12647ff3-8cca-5d1f-9ee4-ee4195ee155d}')
    @winrt_commethod(6)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(7)
    def put_Title(self, value: hstr) -> Void: ...
    @winrt_commethod(8)
    def get_SettingsIdentifier(self) -> hstr: ...
    @winrt_commethod(9)
    def put_SettingsIdentifier(self, value: hstr) -> Void: ...
    @winrt_commethod(10)
    def get_SuggestedFolder(self) -> hstr: ...
    @winrt_commethod(11)
    def put_SuggestedFolder(self, value: hstr) -> Void: ...
    @winrt_commethod(12)
    def get_SuggestedStartFolder(self) -> hstr: ...
    @winrt_commethod(13)
    def put_SuggestedStartFolder(self, value: hstr) -> Void: ...
    @winrt_commethod(14)
    def PickMultipleFoldersAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.Storage.Pickers.PickFolderResult]]: ...
    SettingsIdentifier = property(get_SettingsIdentifier, put_SettingsIdentifier)
    SuggestedFolder = property(get_SuggestedFolder, put_SuggestedFolder)
    SuggestedStartFolder = property(get_SuggestedStartFolder, put_SuggestedStartFolder)
    Title = property(get_Title, put_Title)
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
    def get_Path(self) -> hstr: ...
    Path = property(get_Path, None)
class IPickFolderResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Storage.Pickers.IPickFolderResult'
    _iid_ = Guid('{6f7fd316-fe29-59d1-9343-c49cf5cde680}')
    @winrt_commethod(6)
    def get_Path(self) -> hstr: ...
    Path = property(get_Path, None)
class PickFileResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IPickFileResult
    _classid_ = 'Microsoft.Windows.Storage.Pickers.PickFileResult'
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Windows.Storage.Pickers.IPickFileResult) -> hstr: ...
    Path = property(get_Path, None)
class PickFolderResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Storage.Pickers.IPickFolderResult
    _classid_ = 'Microsoft.Windows.Storage.Pickers.PickFolderResult'
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Windows.Storage.Pickers.IPickFolderResult) -> hstr: ...
    Path = property(get_Path, None)
class PickerLocationId(Enum, Int32):
    _name_ = 'Microsoft.Windows.Storage.Pickers.PickerLocationId'
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
    _name_ = 'Microsoft.Windows.Storage.Pickers.PickerViewMode'
    List = 0
    Thumbnail = 1
StoragePickersContract: UInt32 = 131072


make_ready(__name__)
