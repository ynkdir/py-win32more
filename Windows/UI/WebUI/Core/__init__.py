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
import Windows.UI
import Windows.UI.WebUI.Core
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a4fc0016-dbe5-41ad-8d-7b-14-69-8b-d6-91-1d')
    @winrt_commethod(6)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(9)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ForegroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_ForegroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_BackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_BackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_ClosedDisplayMode(self) -> Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode: ...
    @winrt_commethod(15)
    def put_ClosedDisplayMode(self, value: Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode) -> Void: ...
    @winrt_commethod(16)
    def get_IsOpen(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsOpen(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_Size(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(19)
    def get_PrimaryCommands(self) -> Windows.Foundation.Collections.IObservableVector[Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_commethod(20)
    def get_SecondaryCommands(self) -> Windows.Foundation.Collections.IObservableVector[Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_commethod(21)
    def add_MenuOpened(self, handler: Windows.UI.WebUI.Core.MenuOpenedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_MenuOpened(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_MenuClosed(self, handler: Windows.UI.WebUI.Core.MenuClosedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_MenuClosed(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_SizeChanged(self, handler: Windows.UI.WebUI.Core.SizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_SizeChanged(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('858f4f45-08d8-4a46-81-ec-00-01-5b-0b-1c-6c')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: Windows.Foundation.Uri) -> Void: ...
    Uri = property(get_Uri, put_Uri)
class IWebUICommandBarBitmapIconFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f3f7d78a-7673-444a-be-62-ac-12-d3-1c-22-31')
    @winrt_commethod(6)
    def Create(self, uri: Windows.Foundation.Uri) -> Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
class IWebUICommandBarConfirmationButton(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('86e7824a-e3d5-4eb6-b2-ff-8f-01-8a-17-21-05')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_ItemInvoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton, Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ItemInvoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Text = property(get_Text, put_Text)
class IWebUICommandBarElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c9069ec2-284a-4633-8a-ad-63-7a-27-e2-82-c3')
class IWebUICommandBarIcon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d587655d-2014-42be-96-9a-7d-14-ca-6c-8a-49')
class IWebUICommandBarIconButton(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8f1bc93a-3a7c-4842-a0-cf-af-f6-ea-30-85-86')
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
    def get_Icon(self) -> Windows.UI.WebUI.Core.IWebUICommandBarIcon: ...
    @winrt_commethod(15)
    def put_Icon(self, value: Windows.UI.WebUI.Core.IWebUICommandBarIcon) -> Void: ...
    @winrt_commethod(16)
    def add_ItemInvoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.Core.WebUICommandBarIconButton, Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ItemInvoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Label = property(get_Label, put_Label)
    IsToggleButton = property(get_IsToggleButton, put_IsToggleButton)
    IsChecked = property(get_IsChecked, put_IsChecked)
    Icon = property(get_Icon, put_Icon)
class IWebUICommandBarItemInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('304edbdd-e741-41ef-bd-c4-a4-5c-ea-2a-4f-70')
    @winrt_commethod(6)
    def get_IsPrimaryCommand(self) -> Boolean: ...
    IsPrimaryCommand = property(get_IsPrimaryCommand, None)
class IWebUICommandBarSizeChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fbf1e2f6-3029-4719-83-78-92-f8-2b-87-af-1e')
    @winrt_commethod(6)
    def get_Size(self) -> Windows.Foundation.Size: ...
    Size = property(get_Size, None)
class IWebUICommandBarStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1449cdb9-a506-45be-8f-42-b2-83-7e-2f-e0-c9')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.WebUI.Core.WebUICommandBar: ...
class IWebUICommandBarSymbolIcon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d4935477-fd26-46ed-86-58-1a-3f-44-00-e7-b3')
    @winrt_commethod(6)
    def get_Symbol(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Symbol(self, value: WinRT_String) -> Void: ...
    Symbol = property(get_Symbol, put_Symbol)
class IWebUICommandBarSymbolIconFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('51be1a1f-3730-429e-b6-22-14-e2-b7-bf-6a-07')
    @winrt_commethod(6)
    def Create(self, symbol: WinRT_String) -> Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
class MenuClosedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('435387c8-4dd0-4c52-94-89-d3-90-ce-77-21-d2')
    _classid_ = 'Windows.UI.WebUI.Core.MenuClosedEventHandler'
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class MenuOpenedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('18dc0ad3-678f-4c19-89-63-cc-1c-49-a5-ef-9e')
    _classid_ = 'Windows.UI.WebUI.Core.MenuOpenedEventHandler'
    @winrt_commethod(3)
    def Invoke(self) -> Void: ...
class SizeChangedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d49cfe3c-dd2e-4c28-b6-27-30-3a-7f-91-1a-f5')
    _classid_ = 'Windows.UI.WebUI.Core.SizeChangedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, eventArgs: Windows.UI.WebUI.Core.WebUICommandBarSizeChangedEventArgs) -> Void: ...
class WebUICommandBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBar'
    @winrt_mixinmethod
    def get_Visible(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ClosedDisplayMode(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode: ...
    @winrt_mixinmethod
    def put_ClosedDisplayMode(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.UI.WebUI.Core.WebUICommandBarClosedDisplayMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsOpen(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsOpen(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_PrimaryCommands(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.Foundation.Collections.IObservableVector[Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_mixinmethod
    def get_SecondaryCommands(self: Windows.UI.WebUI.Core.IWebUICommandBar) -> Windows.Foundation.Collections.IObservableVector[Windows.UI.WebUI.Core.IWebUICommandBarElement]: ...
    @winrt_mixinmethod
    def add_MenuOpened(self: Windows.UI.WebUI.Core.IWebUICommandBar, handler: Windows.UI.WebUI.Core.MenuOpenedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MenuOpened(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MenuClosed(self: Windows.UI.WebUI.Core.IWebUICommandBar, handler: Windows.UI.WebUI.Core.MenuClosedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MenuClosed(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SizeChanged(self: Windows.UI.WebUI.Core.IWebUICommandBar, handler: Windows.UI.WebUI.Core.SizeChangedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SizeChanged(self: Windows.UI.WebUI.Core.IWebUICommandBar, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.WebUI.Core.IWebUICommandBarStatics) -> Windows.UI.WebUI.Core.WebUICommandBar: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon'
    @winrt_factorymethod
    def Create(cls: Windows.UI.WebUI.Core.IWebUICommandBarBitmapIconFactory, uri: Windows.Foundation.Uri) -> Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WebUI.Core.WebUICommandBarBitmapIcon: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.UI.WebUI.Core.IWebUICommandBarBitmapIcon, value: Windows.Foundation.Uri) -> Void: ...
    Uri = property(get_Uri, put_Uri)
WebUICommandBarClosedDisplayMode = Int32
WebUICommandBarClosedDisplayMode_Default: WebUICommandBarClosedDisplayMode = 0
WebUICommandBarClosedDisplayMode_Minimal: WebUICommandBarClosedDisplayMode = 1
WebUICommandBarClosedDisplayMode_Compact: WebUICommandBarClosedDisplayMode = 2
class WebUICommandBarConfirmationButton(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_ItemInvoked(self: Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.Core.WebUICommandBarConfirmationButton, Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemInvoked(self: Windows.UI.WebUI.Core.IWebUICommandBarConfirmationButton, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Text = property(get_Text, put_Text)
WebUICommandBarContract: UInt32 = 65536
class WebUICommandBarIconButton(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarIconButton'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WebUI.Core.WebUICommandBarIconButton: ...
    @winrt_mixinmethod
    def get_Enabled(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsToggleButton(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsToggleButton(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsChecked(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsChecked(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton) -> Windows.UI.WebUI.Core.IWebUICommandBarIcon: ...
    @winrt_mixinmethod
    def put_Icon(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, value: Windows.UI.WebUI.Core.IWebUICommandBarIcon) -> Void: ...
    @winrt_mixinmethod
    def add_ItemInvoked(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.Core.WebUICommandBarIconButton, Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemInvoked(self: Windows.UI.WebUI.Core.IWebUICommandBarIconButton, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    Label = property(get_Label, put_Label)
    IsToggleButton = property(get_IsToggleButton, put_IsToggleButton)
    IsChecked = property(get_IsChecked, put_IsChecked)
    Icon = property(get_Icon, put_Icon)
class WebUICommandBarItemInvokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarItemInvokedEventArgs'
    @winrt_mixinmethod
    def get_IsPrimaryCommand(self: Windows.UI.WebUI.Core.IWebUICommandBarItemInvokedEventArgs) -> Boolean: ...
    IsPrimaryCommand = property(get_IsPrimaryCommand, None)
class WebUICommandBarSizeChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarSizeChangedEventArgs'
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.WebUI.Core.IWebUICommandBarSizeChangedEventArgs) -> Windows.Foundation.Size: ...
    Size = property(get_Size, None)
class WebUICommandBarSymbolIcon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon'
    @winrt_factorymethod
    def Create(cls: Windows.UI.WebUI.Core.IWebUICommandBarSymbolIconFactory, symbol: WinRT_String) -> Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.WebUI.Core.WebUICommandBarSymbolIcon: ...
    @winrt_mixinmethod
    def get_Symbol(self: Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Symbol(self: Windows.UI.WebUI.Core.IWebUICommandBarSymbolIcon, value: WinRT_String) -> Void: ...
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
make_head(_module, 'MenuClosedEventHandler')
make_head(_module, 'MenuOpenedEventHandler')
make_head(_module, 'SizeChangedEventHandler')
make_head(_module, 'WebUICommandBar')
make_head(_module, 'WebUICommandBarBitmapIcon')
make_head(_module, 'WebUICommandBarConfirmationButton')
make_head(_module, 'WebUICommandBarIconButton')
make_head(_module, 'WebUICommandBarItemInvokedEventArgs')
make_head(_module, 'WebUICommandBarSizeChangedEventArgs')
make_head(_module, 'WebUICommandBarSymbolIcon')
