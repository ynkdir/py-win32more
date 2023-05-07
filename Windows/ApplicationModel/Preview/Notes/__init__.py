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
import Windows.ApplicationModel.Preview.Notes
import Windows.Foundation
import Windows.Graphics.Imaging
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class INotePlacementChangedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs'
    _iid_ = Guid('{491d57b7-f780-4e7f-a939-9a4caf965214}')
    @winrt_commethod(6)
    def get_ViewId(self: Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs) -> Int32: ...
    ViewId = property(get_ViewId, None)
class INoteVisibilityChangedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs'
    _iid_ = Guid('{0e34649e-3815-4ff6-83b3-a14d17120e24}')
    @winrt_commethod(6)
    def get_ViewId(self: Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Int32: ...
    @winrt_commethod(7)
    def get_IsVisible(self: Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Boolean: ...
    ViewId = property(get_ViewId, None)
    IsVisible = property(get_IsVisible, None)
class INotesWindowManagerPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview'
    _iid_ = Guid('{dc2ac23e-4850-4f13-9cc7-ff487efdfcde}')
    @winrt_commethod(6)
    def get_IsScreenLocked(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Boolean: ...
    @winrt_commethod(7)
    def ShowNote(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_commethod(8)
    def ShowNoteRelativeTo(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, anchorNoteViewId: Int32) -> Void: ...
    @winrt_commethod(9)
    def ShowNoteWithPlacement(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, data: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def HideNote(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_commethod(11)
    def GetNotePlacement(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def TrySetNoteSize(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, size: Windows.Foundation.Size) -> Boolean: ...
    @winrt_commethod(13)
    def SetFocusToNextView(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Void: ...
    @winrt_commethod(14)
    def SetNotesThumbnailAsync(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, thumbnail: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def add_SystemLockStateChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_SystemLockStateChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_NotePlacementChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_NotePlacementChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_NoteVisibilityChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_NoteVisibilityChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsScreenLocked = property(get_IsScreenLocked, None)
class INotesWindowManagerPreview2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2'
    _iid_ = Guid('{edfe864a-1f54-4b09-9823-ff477f6fa3bc}')
    @winrt_commethod(6)
    def ShowNoteRelativeToWithOptions(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, anchorNoteViewId: Int32, options: Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_commethod(7)
    def ShowNoteWithPlacementWithOptions(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, data: Windows.Storage.Streams.IBuffer, options: Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_commethod(8)
    def SetFocusToPreviousView(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2) -> Void: ...
    @winrt_commethod(9)
    def SetThumbnailImageForTaskSwitcherAsync(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncAction: ...
class INotesWindowManagerPreviewShowNoteOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions'
    _iid_ = Guid('{886b09d6-a6ae-4007-a56d-1ca70c84c0d2}')
    @winrt_commethod(6)
    def get_ShowWithFocus(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions) -> Boolean: ...
    @winrt_commethod(7)
    def put_ShowWithFocus(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions, value: Boolean) -> Void: ...
    ShowWithFocus = property(get_ShowWithFocus, put_ShowWithFocus)
class INotesWindowManagerPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewStatics'
    _iid_ = Guid('{6668cc88-0a8e-4127-a38e-995445868a78}')
    @winrt_commethod(6)
    def GetForCurrentApp(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewStatics) -> Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview: ...
class NotePlacementChangedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs'
    @winrt_mixinmethod
    def get_ViewId(self: Windows.ApplicationModel.Preview.Notes.INotePlacementChangedPreviewEventArgs) -> Int32: ...
    ViewId = property(get_ViewId, None)
class NoteVisibilityChangedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs'
    @winrt_mixinmethod
    def get_ViewId(self: Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.ApplicationModel.Preview.Notes.INoteVisibilityChangedPreviewEventArgs) -> Boolean: ...
    ViewId = property(get_ViewId, None)
    IsVisible = property(get_IsVisible, None)
class NotesWindowManagerPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview'
    @winrt_mixinmethod
    def get_IsScreenLocked(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Boolean: ...
    @winrt_mixinmethod
    def ShowNote(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteRelativeTo(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, anchorNoteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteWithPlacement(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, data: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def HideNote(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Void: ...
    @winrt_mixinmethod
    def GetNotePlacement(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def TrySetNoteSize(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, noteViewId: Int32, size: Windows.Foundation.Size) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocusToNextView(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview) -> Void: ...
    @winrt_mixinmethod
    def SetNotesThumbnailAsync(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, thumbnail: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_SystemLockStateChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemLockStateChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NotePlacementChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.ApplicationModel.Preview.Notes.NotePlacementChangedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotePlacementChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NoteVisibilityChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview, Windows.ApplicationModel.Preview.Notes.NoteVisibilityChangedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NoteVisibilityChanged(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteRelativeToWithOptions(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, anchorNoteViewId: Int32, options: Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_mixinmethod
    def ShowNoteWithPlacementWithOptions(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, noteViewId: Int32, data: Windows.Storage.Streams.IBuffer, options: Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions) -> Void: ...
    @winrt_mixinmethod
    def SetFocusToPreviousView(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2) -> Void: ...
    @winrt_mixinmethod
    def SetThumbnailImageForTaskSwitcherAsync(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreview2, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewStatics) -> Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreview: ...
    IsScreenLocked = property(get_IsScreenLocked, None)
class NotesWindowManagerPreviewShowNoteOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions
    _classid_ = 'Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.Preview.Notes.NotesWindowManagerPreviewShowNoteOptions: ...
    @winrt_mixinmethod
    def get_ShowWithFocus(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowWithFocus(self: Windows.ApplicationModel.Preview.Notes.INotesWindowManagerPreviewShowNoteOptions, value: Boolean) -> Void: ...
    ShowWithFocus = property(get_ShowWithFocus, put_ShowWithFocus)
PreviewNotesContract: UInt32 = 131072
make_head(_module, 'INotePlacementChangedPreviewEventArgs')
make_head(_module, 'INoteVisibilityChangedPreviewEventArgs')
make_head(_module, 'INotesWindowManagerPreview')
make_head(_module, 'INotesWindowManagerPreview2')
make_head(_module, 'INotesWindowManagerPreviewShowNoteOptions')
make_head(_module, 'INotesWindowManagerPreviewStatics')
make_head(_module, 'NotePlacementChangedPreviewEventArgs')
make_head(_module, 'NoteVisibilityChangedPreviewEventArgs')
make_head(_module, 'NotesWindowManagerPreview')
make_head(_module, 'NotesWindowManagerPreviewShowNoteOptions')
