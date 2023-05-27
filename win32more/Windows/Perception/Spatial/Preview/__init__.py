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
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception.Spatial
import win32more.Windows.Perception.Spatial.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
    NodeId = property(get_NodeId, None)
    CoordinateSystemToNodeTransform = property(get_CoordinateSystemToNodeTransform, None)
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
    NodeId = property(get_NodeId, None)
    CoordinateSystemToNodeTransform = property(get_CoordinateSystemToNodeTransform, None)
class SpatialGraphInteropPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Preview.SpatialGraphInteropPreview'
    @winrt_classmethod
    def TryCreateFrameOfReference(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def TryCreateFrameOfReferenceWithPosition(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def TryCreateFrameOfReferenceWithPositionAndOrientation(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.Preview.SpatialGraphInteropFrameOfReferencePreview: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNode(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNodeWithPosition(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateCoordinateSystemForNodeWithPositionAndOrientation(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid, relativePosition: win32more.Windows.Foundation.Numerics.Vector3, relativeOrientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_classmethod
    def CreateLocatorForNode(cls: Windows.Perception.Spatial.Preview.ISpatialGraphInteropPreviewStatics, nodeId: Guid) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
make_head(_module, 'ISpatialGraphInteropFrameOfReferencePreview')
make_head(_module, 'ISpatialGraphInteropPreviewStatics')
make_head(_module, 'ISpatialGraphInteropPreviewStatics2')
make_head(_module, 'SpatialGraphInteropFrameOfReferencePreview')
make_head(_module, 'SpatialGraphInteropPreview')
