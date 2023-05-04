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
import Windows.ApplicationModel.Holographic
import Windows.Foundation.Numerics
import Windows.Perception.Spatial
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Holographic.IHolographicKeyboard
    _classid_ = 'Windows.ApplicationModel.Holographic.HolographicKeyboard'
    @winrt_mixinmethod
    def SetPlacementOverride(self: Windows.ApplicationModel.Holographic.IHolographicKeyboard, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def SetPlacementOverrideWithMaxSize(self: Windows.ApplicationModel.Holographic.IHolographicKeyboard, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion, maxSize: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def ResetPlacementOverride(self: Windows.ApplicationModel.Holographic.IHolographicKeyboard) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.ApplicationModel.Holographic.IHolographicKeyboardStatics) -> Windows.ApplicationModel.Holographic.HolographicKeyboard: ...
class IHolographicKeyboard(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{07dd0893-aa21-5e6f-a91b-11b2b3fd7be3}')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion, maxSize: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b676c624-63d7-58cf-b06b-08baa032a23f}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.ApplicationModel.Holographic.HolographicKeyboard: ...
make_head(_module, 'HolographicKeyboard')
make_head(_module, 'IHolographicKeyboard')
make_head(_module, 'IHolographicKeyboardStatics')
