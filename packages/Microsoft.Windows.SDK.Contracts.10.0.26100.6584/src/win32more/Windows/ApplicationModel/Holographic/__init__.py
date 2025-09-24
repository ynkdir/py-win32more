from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.Holographic
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception.Spatial
class HolographicKeyboard(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Holographic.IHolographicKeyboard'
    _iid_ = Guid('{07dd0893-aa21-5e6f-a91b-11b2b3fd7be3}')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Holographic.IHolographicKeyboardStatics'
    _iid_ = Guid('{b676c624-63d7-58cf-b06b-08baa032a23f}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.Holographic.HolographicKeyboard: ...


make_ready(__name__)
