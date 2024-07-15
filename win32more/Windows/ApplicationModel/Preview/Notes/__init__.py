from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Preview.Notes
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class INotePlacementChangedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs'
    _iid_ = Guid('{491d57b7-f780-4e7f-a939-9a4caf965214}')
    @winrt_commethod(6)
    def get_ViewId(self) -> Int32: ...
    ViewId = property(get_ViewId, None)
class INoteVisibilityChangedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs'
    _iid_ = Guid('{0e34649e-3815-4ff6-83b3-a14d17120e24}')
    @winrt_commethod(6)
    def get_ViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_IsVisible(self) -> Boolean: ...
    IsVisible = property(get_IsVisible, None)
    ViewId = property(get_ViewId, None)
class INotesWindowManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview'
    _iid_ = Guid('{dc2ac23e-4850-4f13-9cc7-ff487efdfcde}')
    @winrt_commethod(6)
    def get_IsScreenLocked(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowNote(self, noteViewId: Int32) -> Void: ...
    @winrt_commethod(8)
    def ShowNoteRelativeTo(self, noteViewId: Int32, anchorNoteViewId: Int32) -> Void: ...
    @winrt_commethod(9)
    def ShowNoteWithPlacement(self, noteViewId: Int32, data: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def HideNote(self, noteViewId: Int32) -> Void: ...
    @winrt_commethod(11)
    def GetNotePlacement(self, noteViewId: Int32) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def TrySetNoteSize(self, noteViewId: Int32, size: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(13)
    def SetFocusToNextView(self) -> Void: ...
    @winrt_commethod(14)
    def SetNotesThumbnailAsync(self, thumbnail: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def add_SystemLockStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_SystemLockStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_NotePlacementChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_NotePlacementChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_NoteVisibilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_NoteVisibilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsScreenLocked = property(get_IsScreenLocked, None)
    SystemLockStateChanged = event()
    NotePlacementChanged = event()
    NoteVisibilityChanged = event()
class INotesWindowManagerPreview2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2'
    _iid_ = Guid('{edfe864a-1f54-4b09-9823-ff477f6fa3bc}')
    @winrt_commethod(6)
    def ShowNoteRelativeToWithOptions(self, noteViewId: Int32, anchorNoteViewId: Int32, options: win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_commethod(7)
    def ShowNoteWithPlacementWithOptions(self, noteViewId: Int32, data: win32more.Windows.Storage.Streams.IBuffer, options: win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_commethod(8)
    def SetFocusToPreviousView(self) -> Void: ...
    @winrt_commethod(9)
    def SetThumbnailImageForTaskSwitcherAsync(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class INotesWindowManagerPreviewShowNoteOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions'
    _iid_ = Guid('{886b09d6-a6ae-4007-a56d-1ca70c84c0d2}')
    @winrt_commethod(6)
    def get_ShowWithFocus(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ShowWithFocus(self, value: Boolean) -> Void: ...
    ShowWithFocus = property(get_ShowWithFocus, put_ShowWithFocus)
class INotesWindowManagerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewStatics'
    _iid_ = Guid('{6668cc88-0a8e-4127-a38e-995445868a78}')
    @winrt_commethod(6)
    def GetForCurrentApp(self) -> win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview: ...
class NotePlacementChangedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs'
    @winrt_mixinmethod
    def get_ViewId(self: win32more.Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs) -> Int32: ...
    ViewId = property(get_ViewId, None)
class NoteVisibilityChangedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs'
    @winrt_mixinmethod
    def get_ViewId(self: win32more.Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Boolean: ...
    IsVisible = property(get_IsVisible, None)
    ViewId = property(get_ViewId, None)
class NotesWindowManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview'
    @winrt_mixinmethod
    def get_IsScreenLocked(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Boolean: ...
    @winrt_mixinmethod
    def ShowNote(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteRelativeTo(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, anchorNoteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteWithPlacement(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, data: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def HideNote(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def GetNotePlacement(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def TrySetNoteSize(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, size: win32more.Windows.Foundation.Size) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocusToNextView(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Void: ...
    @winrt_mixinmethod
    def SetNotesThumbnailAsync(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, thumbnail: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_SystemLockStateChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemLockStateChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NotePlacementChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotePlacementChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NoteVisibilityChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, win32more.Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NoteVisibilityChanged(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteRelativeToWithOptions(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, anchorNoteViewId: Int32, options: win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteWithPlacementWithOptions(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, data: win32more.Windows.Storage.Streams.IBuffer, options: win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_mixinmethod
    def SetFocusToPreviousView(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2) -> Void: ...
    @winrt_mixinmethod
    def SetThumbnailImageForTaskSwitcherAsync(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewStatics) -> win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview: ...
    IsScreenLocked = property(get_IsScreenLocked, None)
    SystemLockStateChanged = event()
    NotePlacementChanged = event()
    NoteVisibilityChanged = event()
class NotesWindowManagerPreviewShowNoteOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions: ...
    @winrt_mixinmethod
    def get_ShowWithFocus(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowWithFocus(self: win32more.Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions, value: Boolean) -> Void: ...
    ShowWithFocus = property(get_ShowWithFocus, put_ShowWithFocus)
PreviewNotesContract: UInt32 = 131072


make_ready(__name__)
