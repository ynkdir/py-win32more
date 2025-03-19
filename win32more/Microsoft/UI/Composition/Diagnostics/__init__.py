from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.Diagnostics
import win32more.Windows.Win32.System.WinRT
class CompositionDebugHeatMaps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps'
    @winrt_mixinmethod
    def ShowRedraw(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowMemoryUsage(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowOverdraw(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual, contentKinds: win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
class CompositionDebugOverdrawContentKinds(Enum, UInt32):
    None_ = 0
    OffscreenRendered = 1
    Colors = 2
    Effects = 4
    Shadows = 8
    Lights = 16
    Surfaces = 32
    SwapChains = 64
    All = 4294967295
class CompositionDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings'
    @winrt_mixinmethod
    def get_HeatMaps(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    @winrt_classmethod
    def TryGetSettings(cls: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugHeatMaps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps'
    _iid_ = Guid('{815016b8-f645-5c55-87b5-fe2167282b6f}')
    @winrt_commethod(6)
    def Hide(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(7)
    def ShowMemoryUsage(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def ShowOverdraw(self, subtree: win32more.Microsoft.UI.Composition.Visual, contentKinds: win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_commethod(9)
    def ShowRedraw(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
class ICompositionDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings'
    _iid_ = Guid('{f4c0c0f6-7f5f-5014-a0d6-c8c7eeecace6}')
    @winrt_commethod(6)
    def get_HeatMaps(self) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics'
    _iid_ = Guid('{b56f8aab-2b8c-51aa-b974-10e5c517f50e}')
    @winrt_commethod(6)
    def TryGetSettings(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings: ...


make_ready(__name__)
