from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Perception.Spatial
import win32more.Windows.Perception.Spatial.Surfaces
import win32more.Windows.Storage.Streams
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo'
    _iid_ = Guid('{f8e9ebe7-39b7-3962-bb03-57f56e1fb0a1}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_UpdateTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def TryGetBounds(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingOrientedBox]: ...
    @winrt_commethod(9)
    def TryComputeLatestMeshAsync(self, maxTrianglesPerCubicMeter: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    @winrt_commethod(10)
    def TryComputeLatestMeshWithOptionsAsync(self, maxTrianglesPerCubicMeter: Double, options: win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    Id = property(get_Id, None)
    UpdateTime = property(get_UpdateTime, None)
class ISpatialSurfaceMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh'
    _iid_ = Guid('{108f57d9-df0d-3950-a0fd-f972c77c27b4}')
    @winrt_commethod(6)
    def get_SurfaceInfo(self) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo: ...
    @winrt_commethod(7)
    def get_CoordinateSystem(self) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_commethod(8)
    def get_TriangleIndices(self) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_commethod(9)
    def get_VertexPositions(self) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_commethod(10)
    def get_VertexPositionScale(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def get_VertexNormals(self) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    SurfaceInfo = property(get_SurfaceInfo, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    TriangleIndices = property(get_TriangleIndices, None)
    VertexPositions = property(get_VertexPositions, None)
    VertexPositionScale = property(get_VertexPositionScale, None)
    VertexNormals = property(get_VertexNormals, None)
class ISpatialSurfaceMeshBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer'
    _iid_ = Guid('{93cf59e0-871f-33f8-98b2-03d101458f6f}')
    @winrt_commethod(6)
    def get_Format(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def get_Stride(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ElementCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Stride = property(get_Stride, None)
    ElementCount = property(get_ElementCount, None)
    Data = property(get_Data, None)
class ISpatialSurfaceMeshOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions'
    _iid_ = Guid('{d2759f89-3572-3d2d-a10d-5fee9394aa37}')
    @winrt_commethod(6)
    def get_VertexPositionFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def put_VertexPositionFormat(self, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(8)
    def get_TriangleIndexFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def put_TriangleIndexFormat(self, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(10)
    def get_VertexNormalFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(11)
    def put_VertexNormalFormat(self, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(12)
    def get_IncludeVertexNormals(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IncludeVertexNormals(self, value: Boolean) -> Void: ...
    VertexPositionFormat = property(get_VertexPositionFormat, put_VertexPositionFormat)
    TriangleIndexFormat = property(get_TriangleIndexFormat, put_TriangleIndexFormat)
    VertexNormalFormat = property(get_VertexNormalFormat, put_VertexNormalFormat)
    IncludeVertexNormals = property(get_IncludeVertexNormals, put_IncludeVertexNormals)
class ISpatialSurfaceMeshOptionsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics'
    _iid_ = Guid('{9b340abf-9781-4505-8935-013575caae5e}')
    @winrt_commethod(6)
    def get_SupportedVertexPositionFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(7)
    def get_SupportedTriangleIndexFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(8)
    def get_SupportedVertexNormalFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    SupportedVertexPositionFormats = property(get_SupportedVertexPositionFormats, None)
    SupportedTriangleIndexFormats = property(get_SupportedTriangleIndexFormats, None)
    SupportedVertexNormalFormats = property(get_SupportedVertexNormalFormats, None)
class ISpatialSurfaceObserver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver'
    _iid_ = Guid('{10b69819-ddca-3483-ac3a-748fe8c86df5}')
    @winrt_commethod(6)
    def GetObservedSurfaces(self) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo]: ...
    @winrt_commethod(7)
    def SetBoundingVolume(self, bounds: win32more.Windows.Perception.Spatial.SpatialBoundingVolume) -> Void: ...
    @winrt_commethod(8)
    def SetBoundingVolumes(self, bounds: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Perception.Spatial.SpatialBoundingVolume]) -> Void: ...
    @winrt_commethod(9)
    def add_ObservedSurfacesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ObservedSurfacesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISpatialSurfaceObserverStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics'
    _iid_ = Guid('{165951ed-2108-4168-9175-87e027bc9285}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
class ISpatialSurfaceObserverStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics2'
    _iid_ = Guid('{0f534261-c55d-4e6b-a895-a19de69a42e3}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class SpatialSurfaceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_UpdateTime(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def TryGetBounds(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingOrientedBox]: ...
    @winrt_mixinmethod
    def TryComputeLatestMeshAsync(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, maxTrianglesPerCubicMeter: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    @winrt_mixinmethod
    def TryComputeLatestMeshWithOptionsAsync(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceInfo, maxTrianglesPerCubicMeter: Double, options: win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh]: ...
    Id = property(get_Id, None)
    UpdateTime = property(get_UpdateTime, None)
class SpatialSurfaceMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMesh'
    @winrt_mixinmethod
    def get_SurfaceInfo(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo: ...
    @winrt_mixinmethod
    def get_CoordinateSystem(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Perception.Spatial.SpatialCoordinateSystem: ...
    @winrt_mixinmethod
    def get_TriangleIndices(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_mixinmethod
    def get_VertexPositions(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    @winrt_mixinmethod
    def get_VertexPositionScale(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_VertexNormals(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMesh) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer: ...
    SurfaceInfo = property(get_SurfaceInfo, None)
    CoordinateSystem = property(get_CoordinateSystem, None)
    TriangleIndices = property(get_TriangleIndices, None)
    VertexPositions = property(get_VertexPositions, None)
    VertexPositionScale = property(get_VertexPositionScale, None)
    VertexNormals = property(get_VertexNormals, None)
class SpatialSurfaceMeshBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshBuffer'
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Stride(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_ElementCount(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshBuffer) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Stride = property(get_Stride, None)
    ElementCount = property(get_ElementCount, None)
    Data = property(get_Data, None)
class _SpatialSurfaceMeshOptions_Meta_(ComPtr.__class__):
    pass
class SpatialSurfaceMeshOptions(ComPtr, metaclass=_SpatialSurfaceMeshOptions_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceMeshOptions: ...
    @winrt_mixinmethod
    def get_VertexPositionFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_VertexPositionFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_TriangleIndexFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_TriangleIndexFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_VertexNormalFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_VertexNormalFormat(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeVertexNormals(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeVertexNormals(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptions, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_SupportedVertexPositionFormats(cls: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_classmethod
    def get_SupportedTriangleIndexFormats(cls: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_classmethod
    def get_SupportedVertexNormalFormats(cls: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceMeshOptionsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    VertexPositionFormat = property(get_VertexPositionFormat, put_VertexPositionFormat)
    TriangleIndexFormat = property(get_TriangleIndexFormat, put_TriangleIndexFormat)
    VertexNormalFormat = property(get_VertexNormalFormat, put_VertexNormalFormat)
    IncludeVertexNormals = property(get_IncludeVertexNormals, put_IncludeVertexNormals)
    _SpatialSurfaceMeshOptions_Meta_.SupportedVertexPositionFormats = property(get_SupportedVertexPositionFormats.__wrapped__, None)
    _SpatialSurfaceMeshOptions_Meta_.SupportedTriangleIndexFormats = property(get_SupportedTriangleIndexFormats.__wrapped__, None)
    _SpatialSurfaceMeshOptions_Meta_.SupportedVertexNormalFormats = property(get_SupportedVertexNormalFormats.__wrapped__, None)
class SpatialSurfaceObserver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver
    _classid_ = 'Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver: ...
    @winrt_mixinmethod
    def GetObservedSurfaces(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver) -> win32more.Windows.Foundation.Collections.IMapView[Guid, win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceInfo]: ...
    @winrt_mixinmethod
    def SetBoundingVolume(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, bounds: win32more.Windows.Perception.Spatial.SpatialBoundingVolume) -> Void: ...
    @winrt_mixinmethod
    def SetBoundingVolumes(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, bounds: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Perception.Spatial.SpatialBoundingVolume]) -> Void: ...
    @winrt_mixinmethod
    def add_ObservedSurfacesChanged(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Perception.Spatial.Surfaces.SpatialSurfaceObserver, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ObservedSurfacesChanged(self: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics2) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Perception.Spatial.Surfaces.ISpatialSurfaceObserverStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]: ...
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
