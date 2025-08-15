from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Diagnostics
class CompositionDebugHeatMaps(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps
    _classid_ = 'Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps'
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowMemoryUsage(self: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowOverdraw(self: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Windows.UI.Composition.Visual, contentKinds: win32more.Windows.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_mixinmethod
    def ShowRedraw(self: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
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
    extends: IInspectable
    default_interface: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugSettings
    _classid_ = 'Windows.UI.Composition.Diagnostics.CompositionDebugSettings'
    @winrt_mixinmethod
    def get_HeatMaps(self: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugSettings) -> win32more.Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    @winrt_classmethod
    def TryGetSettings(cls: win32more.Windows.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Diagnostics.CompositionDebugSettings: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugHeatMaps(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps'
    _iid_ = Guid('{e49c90ac-2ff3-5805-718c-b725ee07650f}')
    @winrt_commethod(6)
    def Hide(self, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(7)
    def ShowMemoryUsage(self, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def ShowOverdraw(self, subtree: win32more.Windows.UI.Composition.Visual, contentKinds: win32more.Windows.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_commethod(9)
    def ShowRedraw(self, subtree: win32more.Windows.UI.Composition.Visual) -> Void: ...
class ICompositionDebugSettings(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugSettings'
    _iid_ = Guid('{2831987e-1d82-4d38-b7b7-efd11c7bc3d1}')
    @winrt_commethod(6)
    def get_HeatMaps(self) -> win32more.Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugSettingsStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics'
    _iid_ = Guid('{64ec1f1e-6af8-4af8-b814-c870fd5a9505}')
    @winrt_commethod(6)
    def TryGetSettings(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Diagnostics.CompositionDebugSettings: ...


make_ready(__name__)
