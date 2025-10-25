from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Preview.Holographic
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception.Spatial
class HolographicApplicationPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.HolographicApplicationPreview'
    @winrt_classmethod
    def IsCurrentViewPresentedOnHolographicDisplay(cls: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics) -> Boolean: ...
    @winrt_classmethod
    def IsHolographicActivation(cls: win32more.Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics, activatedEventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class HolographicKeyboardPlacementOverridePreview(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicApplicationPreviewStatics'
    _iid_ = Guid('{fe038691-2a3a-45a9-a208-7bed691919f3}')
    @winrt_commethod(6)
    def IsCurrentViewPresentedOnHolographicDisplay(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsHolographicActivation(self, activatedEventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Boolean: ...
class IHolographicKeyboardPlacementOverridePreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreview'
    _iid_ = Guid('{c8a8ce3a-dfde-5a14-8d5f-182c526dd9c4}')
    @winrt_commethod(6)
    def SetPlacementOverride(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def SetPlacementOverrideWithMaxSize(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, topCenterPosition: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3, maxSize: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def ResetPlacementOverride(self) -> Void: ...
class IHolographicKeyboardPlacementOverridePreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.Holographic.IHolographicKeyboardPlacementOverridePreviewStatics'
    _iid_ = Guid('{202e6039-1ff6-5a06-aac4-a5e24fa3ec4b}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.Preview.Holographic.HolographicKeyboardPlacementOverridePreview: ...


make_ready(__name__)
