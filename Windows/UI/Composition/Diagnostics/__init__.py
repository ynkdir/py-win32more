from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.UI.Composition
import Windows.UI.Composition.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CompositionDebugHeatMaps(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps
    _classid_ = 'Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps'
    @winrt_mixinmethod
    def Hide(self: Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowMemoryUsage(self: Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowOverdraw(self: Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: Windows.UI.Composition.Visual, contentKinds: Windows.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_mixinmethod
    def ShowRedraw(self: Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: Windows.UI.Composition.Visual) -> Void: ...
CompositionDebugOverdrawContentKinds = UInt32
CompositionDebugOverdrawContentKinds_None: CompositionDebugOverdrawContentKinds = 0
CompositionDebugOverdrawContentKinds_OffscreenRendered: CompositionDebugOverdrawContentKinds = 1
CompositionDebugOverdrawContentKinds_Colors: CompositionDebugOverdrawContentKinds = 2
CompositionDebugOverdrawContentKinds_Effects: CompositionDebugOverdrawContentKinds = 4
CompositionDebugOverdrawContentKinds_Shadows: CompositionDebugOverdrawContentKinds = 8
CompositionDebugOverdrawContentKinds_Lights: CompositionDebugOverdrawContentKinds = 16
CompositionDebugOverdrawContentKinds_Surfaces: CompositionDebugOverdrawContentKinds = 32
CompositionDebugOverdrawContentKinds_SwapChains: CompositionDebugOverdrawContentKinds = 64
CompositionDebugOverdrawContentKinds_All: CompositionDebugOverdrawContentKinds = 4294967295
class CompositionDebugSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.Diagnostics.ICompositionDebugSettings
    _classid_ = 'Windows.UI.Composition.Diagnostics.CompositionDebugSettings'
    @winrt_mixinmethod
    def get_HeatMaps(self: Windows.UI.Composition.Diagnostics.ICompositionDebugSettings) -> Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    @winrt_classmethod
    def TryGetSettings(cls: Windows.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Diagnostics.CompositionDebugSettings: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugHeatMaps(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugHeatMaps'
    _iid_ = Guid('{e49c90ac-2ff3-5805-718c-b725ee07650f}')
    @winrt_commethod(6)
    def Hide(self, subtree: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(7)
    def ShowMemoryUsage(self, subtree: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def ShowOverdraw(self, subtree: Windows.UI.Composition.Visual, contentKinds: Windows.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_commethod(9)
    def ShowRedraw(self, subtree: Windows.UI.Composition.Visual) -> Void: ...
class ICompositionDebugSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugSettings'
    _iid_ = Guid('{2831987e-1d82-4d38-b7b7-efd11c7bc3d1}')
    @winrt_commethod(6)
    def get_HeatMaps(self) -> Windows.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics'
    _iid_ = Guid('{64ec1f1e-6af8-4af8-b814-c870fd5a9505}')
    @winrt_commethod(6)
    def TryGetSettings(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Diagnostics.CompositionDebugSettings: ...
make_head(_module, 'CompositionDebugHeatMaps')
make_head(_module, 'CompositionDebugSettings')
make_head(_module, 'ICompositionDebugHeatMaps')
make_head(_module, 'ICompositionDebugSettings')
make_head(_module, 'ICompositionDebugSettingsStatics')
