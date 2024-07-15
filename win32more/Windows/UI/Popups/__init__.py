from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Popups
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
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
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    Commands = property(get_Commands, None)
    Content = property(get_Content, put_Content)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    Options = property(get_Options, put_Options)
    Title = property(get_Title, put_Title)
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
    def get_Id(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def put_Id(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Id = property(get_Id, put_Id)
    Invoked = property(get_Invoked, put_Invoked)
    Label = property(get_Label, put_Label)
class IUICommandFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Popups.IUICommandFactory'
    _iid_ = Guid('{a21a8189-26b0-4676-ae94-54041bc125e8}')
    @winrt_commethod(6)
    def Create(self, label: WinRT_String) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_commethod(7)
    def CreateWithHandler(self, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_commethod(8)
    def CreateWithHandlerAndId(self, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler, commandId: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Popups.UICommand: ...
class MessageDialog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IMessageDialog
    _classid_ = 'Windows.UI.Popups.MessageDialog'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Popups.MessageDialog.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Popups.MessageDialog.CreateWithTitle(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.UI.Popups.IMessageDialogFactory, content: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
    @winrt_factorymethod
    def CreateWithTitle(cls: win32more.Windows.UI.Popups.IMessageDialogFactory, content: WinRT_String, title: WinRT_String) -> win32more.Windows.UI.Popups.MessageDialog: ...
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
    CancelCommandIndex = property(get_CancelCommandIndex, put_CancelCommandIndex)
    Commands = property(get_Commands, None)
    Content = property(get_Content, put_Content)
    DefaultCommandIndex = property(get_DefaultCommandIndex, put_DefaultCommandIndex)
    Options = property(get_Options, put_Options)
    Title = property(get_Title, put_Title)
class MessageDialogOptions(Enum, UInt32):
    None_ = 0
    AcceptUserInputAfterDelay = 1
class Placement(Enum, Int32):
    Default = 0
    Above = 1
    Below = 2
    Left = 3
    Right = 4
class PopupMenu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IPopupMenu
    _classid_ = 'Windows.UI.Popups.PopupMenu'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Popups.PopupMenu.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Popups.PopupMenu: ...
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Popups.UICommand.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Popups.UICommand.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Popups.UICommand.CreateWithHandler(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Popups.UICommand.CreateWithHandlerAndId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.UI.Popups.IUICommandFactory, label: WinRT_String) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_factorymethod
    def CreateWithHandler(cls: win32more.Windows.UI.Popups.IUICommandFactory, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_factorymethod
    def CreateWithHandlerAndId(cls: win32more.Windows.UI.Popups.IUICommandFactory, label: WinRT_String, action: win32more.Windows.UI.Popups.UICommandInvokedHandler, commandId: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Popups.UICommand: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Id = property(get_Id, put_Id)
    Invoked = property(get_Invoked, put_Invoked)
    Label = property(get_Label, put_Label)
class UICommandInvokedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{daf77a4f-c27a-4298-9ac6-2922c45e7da6}')
    @winrt_commethod(3)
    def Invoke(self, command: win32more.Windows.UI.Popups.IUICommand) -> Void: ...
class UICommandSeparator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Popups.IUICommand
    _classid_ = 'Windows.UI.Popups.UICommandSeparator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Popups.UICommandSeparator.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Popups.UICommandSeparator: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Popups.IUICommand) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Popups.IUICommand, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Id = property(get_Id, put_Id)
    Invoked = property(get_Invoked, put_Invoked)
    Label = property(get_Label, put_Label)


make_ready(__name__)
