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
import win32more.Windows.UI
import win32more.Windows.UI.WebUI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWebUICommandBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBar'
    _iid_ = Guid('{a4fc0016-dbe5-41ad-8d7b-14698bd6911d}')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(9)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_ForegroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_ClosedDisplayMode(self) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode: ...
    @winrt_commethod(15)
    def put_ClosedDisplayMode(self, value: win32more.Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode) -> Void: ...
    @winrt_commethod(16)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsOpen(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(19)
    def get_PrimaryCommands(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_commethod(20)
    def get_SecondaryCommands(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_commethod(21)
    def add_MenuOpened(self, handler: win32more.Windows.UI.WebUI.Core.MenuOpenedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_MenuOpened(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_MenuClosed(self, handler: win32more.Windows.UI.WebUI.Core.MenuClosedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_MenuClosed(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_SizeChanged(self, handler: win32more.Windows.UI.WebUI.Core.SizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_SizeChanged(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Visible = property(get_Visible, put_Visible)
    Opacity = property(get_Opacity, put_Opacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ClosedDisplayMode = property(get_ClosedDisplayMode, put_ClosedDisplayMode)
    IsOpen = property(get_IsOpen, put_IsOpen)
    Size = property(get_Size, None)
    PrimaryCommands = property(get_PrimaryCommands, None)
    SecondaryCommands = property(get_SecondaryCommands, None)
class IWebUICommandBarBitmapIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon'
    _iid_ = Guid('{858f4f45-08d8-4a46-81ec-00015b0b1c6c}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Uri = property(get_Uri, put_Uri)
class IWebUICommandBarBitmapIconFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarBitmapIconFactory'
    _iid_ = Guid('{f3f7d78a-7673-444a-be62-ac12d31c2231}')
    @winrt_commethod(6)
    def Create(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
class IWebUICommandBarConfirmationButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton'
    _iid_ = Guid('{86e7824a-e3d5-4eb6-b2ff-8f018a172105}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_ItemInvoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton, win32more.Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ItemInvoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Text = property(get_Text, put_Text)
class IWebUICommandBarElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarElement'
    _iid_ = Guid('{c9069ec2-284a-4633-8aad-637a27e282c3}')
class IWebUICommandBarIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarIcon'
    _iid_ = Guid('{d587655d-2014-42be-969a-7d14ca6c8a49}')
class IWebUICommandBarIconButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarIconButton'
    _iid_ = Guid('{8f1bc93a-3a7c-4842-a0cf-aff6ea308586}')
    @winrt_commethod(6)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_IsToggleButton(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsToggleButton(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsChecked(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsChecked(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_Icon(self) -> win32more.Windows.UI.WebUI.Core.IWebUICommandBarIcon: ...
    @winrt_commethod(15)
    def put_Icon(self, value: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIcon) -> Void: ...
    @winrt_commethod(16)
    def add_ItemInvoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.Core.WebUICommandBarIconButton, win32more.Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ItemInvoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Label = property(get_Label, put_Label)
    IsToggleButton = property(get_IsToggleButton, put_IsToggleButton)
    IsChecked = property(get_IsChecked, put_IsChecked)
    Icon = property(get_Icon, put_Icon)
class IWebUICommandBarItemInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarItemInvokedEventArgs'
    _iid_ = Guid('{304edbdd-e741-41ef-bdc4-a45cea2a4f70}')
    @winrt_commethod(6)
    def get_IsPrimaryCommand(self) -> Boolean: ...
    IsPrimaryCommand = property(get_IsPrimaryCommand, None)
class IWebUICommandBarSizeChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarSizeChangedEventArgs'
    _iid_ = Guid('{fbf1e2f6-3029-4719-8378-92f82b87af1e}')
    @winrt_commethod(6)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    Size = property(get_Size, None)
class IWebUICommandBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarStatics'
    _iid_ = Guid('{1449cdb9-a506-45be-8f42-b2837e2fe0c9}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.WebUI.Core.WebUICommandBar: ...
class IWebUICommandBarSymbolIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon'
    _iid_ = Guid('{d4935477-fd26-46ed-8658-1a3f4400e7b3}')
    @winrt_commethod(6)
    def get_Symbol(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Symbol(self, value: WinRT_String) -> Void: ...
    Symbol = property(get_Symbol, put_Symbol)
class IWebUICommandBarSymbolIconFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.IWebUICommandBarSymbolIconFactory'
    _iid_ = Guid('{51be1a1f-3730-429e-b622-14e2b7bf6a07}')
    @winrt_commethod(6)
    def Create(self, symbol: WinRT_String) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
class MenuClosedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{435387c8-4dd0-4c52-9489-d390ce7721d2}')
    def Invoke(self) -> Void: ...
class MenuOpenedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18dc0ad3-678f-4c19-8963-cc1c49a5ef9e}')
    def Invoke(self) -> Void: ...
class SizeChangedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d49cfe3c-dd2e-4c28-b627-303a7f911af5}')
    def Invoke(self, eventArgs: win32more.Windows.UI.WebUI.Core.WebUICommandBarSizeChangedEventArgs) -> Void: ...
class WebUICommandBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBar
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBar'
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedDisplayMode(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode: ...
    @winrt_mixinmethod
    def put_ClosedDisplayMode(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOpen(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_PrimaryCommands(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_mixinmethod
    def get_SecondaryCommands(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_mixinmethod
    def add_MenuOpened(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, handler: win32more.Windows.UI.WebUI.Core.MenuOpenedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MenuOpened(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MenuClosed(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, handler: win32more.Windows.UI.WebUI.Core.MenuClosedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MenuClosed(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, handler: win32more.Windows.UI.WebUI.Core.SizeChangedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBar, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.WebUI.Core.IWebUICommandBarStatics) -> win32more.Windows.UI.WebUI.Core.WebUICommandBar: ...
    Visible = property(get_Visible, put_Visible)
    Opacity = property(get_Opacity, put_Opacity)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ClosedDisplayMode = property(get_ClosedDisplayMode, put_ClosedDisplayMode)
    IsOpen = property(get_IsOpen, put_IsOpen)
    Size = property(get_Size, None)
    PrimaryCommands = property(get_PrimaryCommands, None)
    SecondaryCommands = property(get_SecondaryCommands, None)
class WebUICommandBarBitmapIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon'
    @winrt_factorymethod
    def Create(cls: Windows.UI.WebUI.Core.IWebUICommandBarBitmapIconFactory, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Uri = property(get_Uri, put_Uri)
WebUICommandBarClosedDisplayMode = Int32
WebUICommandBarClosedDisplayMode_Default: WebUICommandBarClosedDisplayMode = 0
WebUICommandBarClosedDisplayMode_Minimal: WebUICommandBarClosedDisplayMode = 1
WebUICommandBarClosedDisplayMode_Compact: WebUICommandBarClosedDisplayMode = 2
class WebUICommandBarConfirmationButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_ItemInvoked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton, win32more.Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemInvoked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Text = property(get_Text, put_Text)
WebUICommandBarContract: UInt32 = 65536
class WebUICommandBarIconButton(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarIconButton'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.WebUI.Core.WebUICommandBarIconButton: ...
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsToggleButton(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsToggleButton(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsChecked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsChecked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> win32more.Windows.UI.WebUI.Core.IWebUICommandBarIcon: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIcon) -> Void: ...
    @winrt_mixinmethod
    def add_ItemInvoked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.Core.WebUICommandBarIconButton, win32more.Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemInvoked(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarIconButton, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Label = property(get_Label, put_Label)
    IsToggleButton = property(get_IsToggleButton, put_IsToggleButton)
    IsChecked = property(get_IsChecked, put_IsChecked)
    Icon = property(get_Icon, put_Icon)
class WebUICommandBarItemInvokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarItemInvokedEventArgs
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs'
    @winrt_mixinmethod
    def get_IsPrimaryCommand(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarItemInvokedEventArgs) -> Boolean: ...
    IsPrimaryCommand = property(get_IsPrimaryCommand, None)
class WebUICommandBarSizeChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarSizeChangedEventArgs
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarSizeChangedEventArgs'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarSizeChangedEventArgs) -> win32more.Windows.Foundation.Size: ...
    Size = property(get_Size, None)
class WebUICommandBarSymbolIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon'
    @winrt_factorymethod
    def Create(cls: Windows.UI.WebUI.Core.IWebUICommandBarSymbolIconFactory, symbol: WinRT_String) -> win32more.Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
    @winrt_mixinmethod
    def get_Symbol(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Symbol(self: win32more.Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon, value: WinRT_String) -> Void: ...
    Symbol = property(get_Symbol, put_Symbol)
make_head(_module, 'IWebUICommandBar')
make_head(_module, 'IWebUICommandBarBitmapIcon')
make_head(_module, 'IWebUICommandBarBitmapIconFactory')
make_head(_module, 'IWebUICommandBarConfirmationButton')
make_head(_module, 'IWebUICommandBarElement')
make_head(_module, 'IWebUICommandBarIcon')
make_head(_module, 'IWebUICommandBarIconButton')
make_head(_module, 'IWebUICommandBarItemInvokedEventArgs')
make_head(_module, 'IWebUICommandBarSizeChangedEventArgs')
make_head(_module, 'IWebUICommandBarStatics')
make_head(_module, 'IWebUICommandBarSymbolIcon')
make_head(_module, 'IWebUICommandBarSymbolIconFactory')
make_head(_module, 'WebUICommandBar')
make_head(_module, 'WebUICommandBarBitmapIcon')
make_head(_module, 'WebUICommandBarConfirmationButton')
make_head(_module, 'WebUICommandBarIconButton')
make_head(_module, 'WebUICommandBarItemInvokedEventArgs')
make_head(_module, 'WebUICommandBarSizeChangedEventArgs')
make_head(_module, 'WebUICommandBarSymbolIcon')
