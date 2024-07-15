from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI
import win32more.Microsoft.UI.System
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class IThemeSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.System.IThemeSettings'
    _iid_ = Guid('{2228ee7e-6d15-563c-8f3c-e8783ba13846}')
    @winrt_commethod(6)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.System.ThemeSettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_HighContrast(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_HighContrastScheme(self) -> WinRT_String: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
    Changed = event()
class IThemeSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.System.IThemeSettingsStatics'
    _iid_ = Guid('{1586907d-30db-5f97-8fa1-8940c75dccc0}')
    @winrt_commethod(6)
    def CreateForWindowId(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.System.ThemeSettings: ...
class ThemeSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.System.IThemeSettings
    _classid_ = 'Microsoft.UI.System.ThemeSettings'
    @winrt_mixinmethod
    def add_Changed(self: win32more.Microsoft.UI.System.IThemeSettings, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.System.ThemeSettings, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Microsoft.UI.System.IThemeSettings, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrast(self: win32more.Microsoft.UI.System.IThemeSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_HighContrastScheme(self: win32more.Microsoft.UI.System.IThemeSettings) -> WinRT_String: ...
    @winrt_classmethod
    def CreateForWindowId(cls: win32more.Microsoft.UI.System.IThemeSettingsStatics, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.System.ThemeSettings: ...
    HighContrast = property(get_HighContrast, None)
    HighContrastScheme = property(get_HighContrastScheme, None)
    Changed = event()


make_ready(__name__)
