from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Preview.Holographic
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception.Spatial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HolographicApplicationPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.HolographicApplicationPreview'
    @winrt_classmethod
    def IsCurrentViewPresentedOnHolographicDisplay(cls: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics) -> Boolean: ...
    @winrt_classmethod
    def IsHolographicActivation(cls: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics, activatedEventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class HolographicKeyboardPlacementOverridePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview'
    @winrt_mixinmethod
    def SetPlacementOverride(self: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetPlacementOverrideWithMaxSize(self: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def ResetPlacementOverride(self: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreviewStatics) -> win32more.Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview: ...
class IHolographicApplicationPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics'
    _iid_ = Guid('{fe038691-2a3a-45a9-a208-7bed691919f3}')
    @winrt_commethod(6)
    def IsCurrentViewPresentedOnHolographicDisplay(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsHolographicActivation(self, activatedEventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class IHolographicKeyboardPlacementOverridePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview'
    _iid_ = Guid('{c8a8ce3a-dfde-5a14-8d5f-182c526dd9c4}')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardPlacementOverridePreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreviewStatics'
    _iid_ = Guid('{202e6039-1ff6-5a06-aac4-a5e24fa3ec4b}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview: ...
make_head(_module, 'HolographicApplicationPreview')
make_head(_module, 'HolographicKeyboardPlacementOverridePreview')
make_head(_module, 'IHolographicApplicationPreviewStatics')
make_head(_module, 'IHolographicKeyboardPlacementOverridePreview')
make_head(_module, 'IHolographicKeyboardPlacementOverridePreviewStatics')
