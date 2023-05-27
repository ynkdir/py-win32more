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
import win32more.Windows.ApplicationModel.Holographic
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
class HolographicKeyboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Holographic.IHolographicKeyboard
    _classid_ = 'Windows.ApplicationModel.Holographic.HolographicKeyboard'
    @winrt_mixinmethod
    def SetPlacementOverride(self: win32more.Windows.ApplicationModel.Holographic.IHolographicKeyboard, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def SetPlacementOverrideWithMaxSize(self: win32more.Windows.ApplicationModel.Holographic.IHolographicKeyboard, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def ResetPlacementOverride(self: win32more.Windows.ApplicationModel.Holographic.IHolographicKeyboard) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.Holographic.IHolographicKeyboardStatics) -> win32more.Windows.ApplicationModel.Holographic.HolographicKeyboard: ...
class IHolographicKeyboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Holographic.IHolographicKeyboard'
    _iid_ = Guid('{07dd0893-aa21-5e6f-a91b-11b2b3fd7be3}')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Holographic.IHolographicKeyboardStatics'
    _iid_ = Guid('{b676c624-63d7-58cf-b06b-08baa032a23f}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.Holographic.HolographicKeyboard: ...
make_head(_module, 'HolographicKeyboard')
make_head(_module, 'IHolographicKeyboard')
make_head(_module, 'IHolographicKeyboardStatics')
