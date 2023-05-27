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
import win32more.Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IMessageDialog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IMessageDialog'
    _iid_ = Guid('{33f59b01-5325-43ab-9ab3-bdae440e4121}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Commands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(9)
    def get_DefaultCommandIndex(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_DefaultCommandIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_CancelCommandIndex(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_CancelCommandIndex(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_Content(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Content(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def ShowAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(16)
    def get_Options(self) -> win32more.Windows.UI.Popups.MessageDialogOptions: ...
    @winrt_commethod(17)
    def put_Options(self, value: win32more.Windows.UI.Popups.MessageDialogOptions) -> Void: ...
    Title = property(get_Title, put_Title)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    Content = property(get_Content, put_Content)
    Options = property(get_Options, put_Options)
class IMessageDialogFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IMessageDialogFactory'
    _iid_ = Guid('{2d161777-a66f-4ea5-bb87-793ffa4941f2}')
    @winrt_commethod(6)
    def Create(self, content: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
    @winrt_commethod(7)
    def CreateWithTitle(self, content: WinRT_String, title: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
class IPopupMenu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IPopupMenu'
    _iid_ = Guid('{4e9bc6dc-880d-47fc-a0a1-72b639e62559}')
    @winrt_commethod(6)
    def get_Commands(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(7)
    def ShowAsync(self, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(8)
    def ShowAsyncWithRect(self, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_commethod(9)
    def ShowAsyncWithRectAndPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    Commands = property(get_Commands, None)
class IUICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IUICommand'
    _iid_ = Guid('{4ff93a75-4145-47ff-ac7f-dff1c1fa5b0f}')
    @winrt_commethod(6)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Invoked(self) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_commethod(9)
    def put_Invoked(self, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_commethod(10)
    def get_Id(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def put_Id(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Label = property(get_Label, put_Label)
    Invoked = property(get_Invoked, put_Invoked)
    Id = property(get_Id, put_Id)
class IUICommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IUICommandFactory'
    _iid_ = Guid('{a21a8189-26b0-4676-ae94-54041bc125e8}')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_commethod(7)
    def CreateWithHandler(self, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_commethod(8)
    def CreateWithHandlerAndId(self, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler, commandId: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.UI.Popups.UICommand: ...
class MessageDialog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IMessageDialog
    _classid_ = 'Windows.UI.Popups.MessageDialog'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Popups.IMessageDialogFactory, content: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
    @winrt_factorymethod
    def CreateWithTitle(cls: Windows.UI.Popups.IMessageDialogFactory, content: WinRT_String, title: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.Popups.IMessageDialog) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.UI.Popups.IMessageDialog, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Commands(self: win32more.Windows.UI.Popups.IMessageDialog) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def get_DefaultCommandIndex(self: win32more.Windows.UI.Popups.IMessageDialog) -> UInt32: ...
    @winrt_mixinmethod
    def put_DefaultCommandIndex(self: win32more.Windows.UI.Popups.IMessageDialog, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CancelCommandIndex(self: win32more.Windows.UI.Popups.IMessageDialog) -> UInt32: ...
    @winrt_mixinmethod
    def put_CancelCommandIndex(self: win32more.Windows.UI.Popups.IMessageDialog, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Popups.IMessageDialog) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.UI.Popups.IMessageDialog, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ShowAsync(self: win32more.Windows.UI.Popups.IMessageDialog) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.UI.Popups.IMessageDialog) -> win32more.Windows.UI.Popups.MessageDialogOptions: ...
    @winrt_mixinmethod
    def put_Options(self: win32more.Windows.UI.Popups.IMessageDialog, value: win32more.Windows.UI.Popups.MessageDialogOptions) -> Void: ...
    Title = property(get_Title, put_Title)
    Commands = property(get_Commands, None)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    Content = property(get_Content, put_Content)
    Options = property(get_Options, put_Options)
MessageDialogOptions = UInt32
MessageDialogOptions_None: MessageDialogOptions = 0
MessageDialogOptions_AcceptUserInputAfterDelay: MessageDialogOptions = 1
Placement = Int32
Placement_Default: Placement = 0
Placement_Above: Placement = 1
Placement_Below: Placement = 2
Placement_Left: Placement = 3
Placement_Right: Placement = 4
class PopupMenu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IPopupMenu
    _classid_ = 'Windows.UI.Popups.PopupMenu'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Popups.PopupMenu: ...
    @winrt_mixinmethod
    def get_Commands(self: win32more.Windows.UI.Popups.IPopupMenu) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def ShowAsync(self: win32more.Windows.UI.Popups.IPopupMenu, invocationPoint: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def ShowAsyncWithRect(self: win32more.Windows.UI.Popups.IPopupMenu, selection: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    @winrt_mixinmethod
    def ShowAsyncWithRectAndPlacement(self: win32more.Windows.UI.Popups.IPopupMenu, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Popups.IUICommand]: ...
    Commands = property(get_Commands, None)
class UICommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IUICommand
    _classid_ = 'Windows.UI.Popups.UICommand'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Popups.IUICommandFactory, label: WinRT_String) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_factorymethod
    def CreateWithHandler(cls: Windows.UI.Popups.IUICommandFactory, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_factorymethod
    def CreateWithHandlerAndId(cls: Windows.UI.Popups.IUICommandFactory, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler, commandId: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Popups.UICommand: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Label = property(get_Label, put_Label)
    Invoked = property(get_Invoked, put_Invoked)
    Id = property(get_Id, put_Id)
class UICommandInvokedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{daf77a4f-c27a-4298-9ac6-2922c45e7da6}')
    def Invoke(self, command: win32more.Windows.UI.Popups.IUICommand) -> Void: ...
class UICommandSeparator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IUICommand
    _classid_ = 'Windows.UI.Popups.UICommandSeparator'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Popups.UICommandSeparator: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Label = property(get_Label, put_Label)
    Invoked = property(get_Invoked, put_Invoked)
    Id = property(get_Id, put_Id)
make_head(_module, 'IMessageDialog')
make_head(_module, 'IMessageDialogFactory')
make_head(_module, 'IPopupMenu')
make_head(_module, 'IUICommand')
make_head(_module, 'IUICommandFactory')
make_head(_module, 'MessageDialog')
make_head(_module, 'PopupMenu')
make_head(_module, 'UICommand')
make_head(_module, 'UICommandSeparator')
