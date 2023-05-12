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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.DirectX
import Windows.Perception.Spatial
import Windows.Perception.Spatial.Surfaces
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISpatialSurfaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo'
    _iid_ = Guid('{f8e9ebe7-39b7-3962-bb03-57f56e1fb0a1}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_UpdateTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def TryGetBounds(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingOrientedBox]: ...
    @winrt_commethod(9)
    def TryComputeLatestMeshAsync(self, maxTrianglesPerCubicMeter: Double) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    @winrt_commethod(10)
    def TryComputeLatestMeshWithOptionsAsync(self, maxTrianglesPerCubicMeter: Double, options: Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    Id = property(get_Id, None)
    UpdateTime = property(get_UpdateTime, None)
class ISpatialSurfaceMesh(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh'
    _iid_ = Guid('{108f57d9-df0d-3950-a0fd-f972c77c27b4}')
    @winrt_commethod(6)
    def get_SurfaceInfo(self) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo: ...
    @winrt_commethod(7)
    def get_CoordinateSystem(self) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(8)
    def get_TriangleIndices(self) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_commethod(9)
    def get_VertexPositions(self) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_commethod(10)
    def get_VertexPositionScale(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def get_VertexNormals(self) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    SurfaceInfo = property(get_SurfaceInfo, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    TriangleIndices = property(get_TriangleIndices, None)
    VertexPositions = property(get_VertexPositions, None)
    VertexPositionScale = property(get_VertexPositionScale, None)
    VertexNormals = property(get_VertexNormals, None)
class ISpatialSurfaceMeshBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer'
    _iid_ = Guid('{93cf59e0-871f-33f8-98b2-03d101458f6f}')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def get_Stride(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ElementCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Stride = property(get_Stride, None)
    ElementCount = property(get_ElementCount, None)
    Data = property(get_Data, None)
class ISpatialSurfaceMeshOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions'
    _iid_ = Guid('{d2759f89-3572-3d2d-a10d-5fee9394aa37}')
    @winrt_commethod(6)
    def get_VertexPositionFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def put_VertexPositionFormat(self, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(8)
    def get_TriangleIndexFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def put_TriangleIndexFormat(self, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(10)
    def get_VertexNormalFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(11)
    def put_VertexNormalFormat(self, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(12)
    def get_IncludeVertexNormals(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IncludeVertexNormals(self, value: Boolean) -> Void: ...
    VertexPositionFormat = property(get_VertexPositionFormat, put_VertexPositionFormat)
    TriangleIndexFormat = property(get_TriangleIndexFormat, put_TriangleIndexFormat)
    VertexNormalFormat = property(get_VertexNormalFormat, put_VertexNormalFormat)
    IncludeVertexNormals = property(get_IncludeVertexNormals, put_IncludeVertexNormals)
class ISpatialSurfaceMeshOptionsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics'
    _iid_ = Guid('{9b340abf-9781-4505-8935-013575caae5e}')
    @winrt_commethod(6)
    def get_SupportedVertexPositionFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(7)
    def get_SupportedTriangleIndexFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(8)
    def get_SupportedVertexNormalFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    SupportedVertexPositionFormats = property(get_SupportedVertexPositionFormats, None)
    SupportedTriangleIndexFormats = property(get_SupportedTriangleIndexFormats, None)
    SupportedVertexNormalFormats = property(get_SupportedVertexNormalFormats, None)
class ISpatialSurfaceObserver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver'
    _iid_ = Guid('{10b69819-ddca-3483-ac3a-748fe8c86df5}')
    @winrt_commethod(6)
    def GetObservedSurfaces(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo]: ...
    @winrt_commethod(7)
    def SetBoundingVolume(self, bounds: Windows.Perception.Spatial.SpatialBoundingVolume) -> Void: ...
    @winrt_commethod(8)
    def SetBoundingVolumes(self, bounds: Windows.Foundation.Collections.IIterable[Windows.Perception.Spatial.SpatialBoundingVolume]) -> Void: ...
    @winrt_commethod(9)
    def add_ObservedSurfacesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ObservedSurfacesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISpatialSurfaceObserverStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics'
    _iid_ = Guid('{165951ed-2108-4168-9175-87e027bc9285}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialSurfaceObserverStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics2'
    _iid_ = Guid('{0f534261-c55d-4e6b-a895-a19de69a42e3}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class SpatialSurfaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo'
    @winrt_mixinmethod
    def get_Id(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_UpdateTime(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def TryGetBounds(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingOrientedBox]: ...
    @winrt_mixinmethod
    def TryComputeLatestMeshAsync(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, maxTrianglesPerCubicMeter: Double) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    @winrt_mixinmethod
    def TryComputeLatestMeshWithOptionsAsync(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, maxTrianglesPerCubicMeter: Double, options: Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    Id = property(get_Id, None)
    UpdateTime = property(get_UpdateTime, None)
class SpatialSurfaceMesh(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh'
    @winrt_mixinmethod
    def get_SurfaceInfo(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_TriangleIndices(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_mixinmethod
    def get_VertexPositions(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_mixinmethod
    def get_VertexPositionScale(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_VertexNormals(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    SurfaceInfo = property(get_SurfaceInfo, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    TriangleIndices = property(get_TriangleIndices, None)
    VertexPositions = property(get_VertexPositions, None)
    VertexPositionScale = property(get_VertexPositionScale, None)
    VertexNormals = property(get_VertexNormals, None)
class SpatialSurfaceMeshBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer'
    @winrt_mixinmethod
    def get_Format(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Stride(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_ElementCount(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Stride = property(get_Stride, None)
    ElementCount = property(get_ElementCount, None)
    Data = property(get_Data, None)
class _SpatialSurfaceMeshOptions_Meta_(ComPtr.__class__):
    pass
class SpatialSurfaceMeshOptions(ComPtr, metaclass=_SpatialSurfaceMeshOptions_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions: ...
    @winrt_mixinmethod
    def get_VertexPositionFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_VertexPositionFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_TriangleIndexFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_TriangleIndexFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_VertexNormalFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_VertexNormalFormat(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeVertexNormals(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeVertexNormals(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_SupportedVertexPositionFormats(cls: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_classmethod
    def get_SupportedTriangleIndexFormats(cls: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_classmethod
    def get_SupportedVertexNormalFormats(cls: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    VertexPositionFormat = property(get_VertexPositionFormat, put_VertexPositionFormat)
    TriangleIndexFormat = property(get_TriangleIndexFormat, put_TriangleIndexFormat)
    VertexNormalFormat = property(get_VertexNormalFormat, put_VertexNormalFormat)
    IncludeVertexNormals = property(get_IncludeVertexNormals, put_IncludeVertexNormals)
    _SpatialSurfaceMeshOptions_Meta_.SupportedVertexPositionFormats = property(get_SupportedVertexPositionFormats.__wrapped__, None)
    _SpatialSurfaceMeshOptions_Meta_.SupportedTriangleIndexFormats = property(get_SupportedTriangleIndexFormats.__wrapped__, None)
    _SpatialSurfaceMeshOptions_Meta_.SupportedVertexNormalFormats = property(get_SupportedVertexNormalFormats.__wrapped__, None)
class SpatialSurfaceObserver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver: ...
    @winrt_mixinmethod
    def GetObservedSurfaces(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo]: ...
    @winrt_mixinmethod
    def SetBoundingVolume(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, bounds: Windows.Perception.Spatial.SpatialBoundingVolume) -> Void: ...
    @winrt_mixinmethod
    def SetBoundingVolumes(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, bounds: Windows.Foundation.Collections.IIterable[Windows.Perception.Spatial.SpatialBoundingVolume]) -> Void: ...
    @winrt_mixinmethod
    def add_ObservedSurfacesChanged(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, handler: Windows.Foundation.TypedEventHandler[Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ObservedSurfacesChanged(self: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics2) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics) -> Windows.Foundation.IAsyncOperation[Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
make_head(_module, 'ISpatialSurfaceInfo')
make_head(_module, 'ISpatialSurfaceMesh')
make_head(_module, 'ISpatialSurfaceMeshBuffer')
make_head(_module, 'ISpatialSurfaceMeshOptions')
make_head(_module, 'ISpatialSurfaceMeshOptionsStatics')
make_head(_module, 'ISpatialSurfaceObserver')
make_head(_module, 'ISpatialSurfaceObserverStatics')
make_head(_module, 'ISpatialSurfaceObserverStatics2')
make_head(_module, 'SpatialSurfaceInfo')
make_head(_module, 'SpatialSurfaceMesh')
make_head(_module, 'SpatialSurfaceMeshBuffer')
make_head(_module, 'SpatialSurfaceMeshOptions')
make_head(_module, 'SpatialSurfaceObserver')
