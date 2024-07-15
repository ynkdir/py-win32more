from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception.Spatial
import win32more.Windows.Perception.Spatial.Preview
import win32more.Windows.Win32.System.WinRT
class ISpatialGraphInteropFrameOfReferencePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Preview.ISpatialGraphInteropFrameOfReferencePreview'
    _iid_ = Guid('{a8271b23-735f-5729-a98e-e64ed189abc5}')
    @winrt_commethod(6)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def get_NodeId(self) -> Guid: ...
    @winrt_commethod(8)
    def get_CoordinateSystemToNodeTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    CoordinateSystemToNodeTransform = property(get_CoordinateSystemToNodeTransform, None)
    NodeId = property(get_NodeId, None)
class ISpatialGraphInteropPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics'
    _iid_ = Guid('{c042644c-20d8-4ed0-aef7-6805b8e53f55}')
    @winrt_commethod(6)
    def CreateCoordinateSystemForNode(self, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(7)
    def CreateCoordinateSystemForNodeWithPosition(self, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(8)
    def CreateCoordinateSystemForNodeWithPositionAndOrientation(self, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(9)
    def CreateLocatorForNode(self, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
class ISpatialGraphInteropPreviewStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2'
    _iid_ = Guid('{2490b15f-6cbd-4b1e-b765-31e462a32df2}')
    @winrt_commethod(6)
    def TryCreateFrameOfReference(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_commethod(7)
    def TryCreateFrameOfReferenceWithPosition(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_commethod(8)
    def TryCreateFrameOfReferenceWithPositionAndOrientation(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
class SpatialGraphInteropFrameOfReferencePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropFrameOfReferencePreview
    _classid_ = 'Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview'
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropFrameOfReferencePreview) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_NodeId(self: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropFrameOfReferencePreview) -> Guid: ...
    @winrt_mixinmethod
    def get_CoordinateSystemToNodeTransform(self: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropFrameOfReferencePreview) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    CoordinateSystem = property(get_CoordinateSystem, None)
    CoordinateSystemToNodeTransform = property(get_CoordinateSystemToNodeTransform, None)
    NodeId = property(get_NodeId, None)
class SpatialGraphInteropPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Preview.SpatialGraphInteropPreview'
    @winrt_classmethod
    def TryCreateFrameOfReference(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def TryCreateFrameOfReferenceWithPosition(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def TryCreateFrameOfReferenceWithPositionAndOrientation(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNode(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNodeWithPosition(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNodeWithPositionAndOrientation(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateLocatorForNode(cls: win32more.Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...


make_ready(__name__)
