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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.DirectX
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Holographic
import Windows.Perception
import Windows.Perception.Spatial
import Windows.UI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HolographicAdapterId(EasyCastStructure):
    LowPart: UInt32
    HighPart: Int32
class HolographicCamera(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicCamera
    _classid_ = 'Windows.Graphics.Holographic.HolographicCamera'
    @winrt_mixinmethod
    def get_RenderTargetSize(self: Windows.Graphics.Holographic.IHolographicCamera) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ViewportScaleFactor(self: Windows.Graphics.Holographic.IHolographicCamera) -> Double: ...
    @winrt_mixinmethod
    def put_ViewportScaleFactor(self: Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Graphics.Holographic.IHolographicCamera) -> Boolean: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Graphics.Holographic.IHolographicCamera) -> UInt32: ...
    @winrt_mixinmethod
    def SetNearPlaneDistance(self: Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def SetFarPlaneDistance(self: Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LeftViewportParameters(self: Windows.Graphics.Holographic.IHolographicCamera2) -> Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_mixinmethod
    def get_RightViewportParameters(self: Windows.Graphics.Holographic.IHolographicCamera2) -> Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_mixinmethod
    def get_Display(self: Windows.Graphics.Holographic.IHolographicCamera2) -> Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_mixinmethod
    def get_IsPrimaryLayerEnabled(self: Windows.Graphics.Holographic.IHolographicCamera3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrimaryLayerEnabled(self: Windows.Graphics.Holographic.IHolographicCamera3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxQuadLayerCount(self: Windows.Graphics.Holographic.IHolographicCamera3) -> UInt32: ...
    @winrt_mixinmethod
    def get_QuadLayers(self: Windows.Graphics.Holographic.IHolographicCamera3) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Holographic.HolographicQuadLayer]: ...
    @winrt_mixinmethod
    def get_CanOverrideViewport(self: Windows.Graphics.Holographic.IHolographicCamera4) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHardwareContentProtectionSupported(self: Windows.Graphics.Holographic.IHolographicCamera5) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHardwareContentProtectionEnabled(self: Windows.Graphics.Holographic.IHolographicCamera5) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHardwareContentProtectionEnabled(self: Windows.Graphics.Holographic.IHolographicCamera5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ViewConfiguration(self: Windows.Graphics.Holographic.IHolographicCamera6) -> Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    RenderTargetSize = property(get_RenderTargetSize, None)
    ViewportScaleFactor = property(get_ViewportScaleFactor, put_ViewportScaleFactor)
    IsStereo = property(get_IsStereo, None)
    Id = property(get_Id, None)
    LeftViewportParameters = property(get_LeftViewportParameters, None)
    RightViewportParameters = property(get_RightViewportParameters, None)
    Display = property(get_Display, None)
    IsPrimaryLayerEnabled = property(get_IsPrimaryLayerEnabled, put_IsPrimaryLayerEnabled)
    MaxQuadLayerCount = property(get_MaxQuadLayerCount, None)
    QuadLayers = property(get_QuadLayers, None)
    CanOverrideViewport = property(get_CanOverrideViewport, None)
    IsHardwareContentProtectionSupported = property(get_IsHardwareContentProtectionSupported, None)
    IsHardwareContentProtectionEnabled = property(get_IsHardwareContentProtectionEnabled, put_IsHardwareContentProtectionEnabled)
    ViewConfiguration = property(get_ViewConfiguration, None)
class HolographicCameraPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicCameraPose
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraPose'
    @winrt_mixinmethod
    def get_HolographicCamera(self: Windows.Graphics.Holographic.IHolographicCameraPose) -> Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_mixinmethod
    def get_Viewport(self: Windows.Graphics.Holographic.IHolographicCameraPose) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def TryGetViewTransform(self: Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Graphics.Holographic.HolographicStereoTransform]: ...
    @winrt_mixinmethod
    def get_ProjectionTransform(self: Windows.Graphics.Holographic.IHolographicCameraPose) -> Windows.Graphics.Holographic.HolographicStereoTransform: ...
    @winrt_mixinmethod
    def TryGetCullingFrustum(self: Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_mixinmethod
    def TryGetVisibleFrustum(self: Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_mixinmethod
    def get_NearPlaneDistance(self: Windows.Graphics.Holographic.IHolographicCameraPose) -> Double: ...
    @winrt_mixinmethod
    def get_FarPlaneDistance(self: Windows.Graphics.Holographic.IHolographicCameraPose) -> Double: ...
    @winrt_mixinmethod
    def OverrideViewTransform(self: Windows.Graphics.Holographic.IHolographicCameraPose2, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, coordinateSystemToViewTransform: Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_mixinmethod
    def OverrideProjectionTransform(self: Windows.Graphics.Holographic.IHolographicCameraPose2, projectionTransform: Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_mixinmethod
    def OverrideViewport(self: Windows.Graphics.Holographic.IHolographicCameraPose2, leftViewport: Windows.Foundation.Rect, rightViewport: Windows.Foundation.Rect) -> Void: ...
    HolographicCamera = property(get_HolographicCamera, None)
    Viewport = property(get_Viewport, None)
    ProjectionTransform = property(get_ProjectionTransform, None)
    NearPlaneDistance = property(get_NearPlaneDistance, None)
    FarPlaneDistance = property(get_FarPlaneDistance, None)
class HolographicCameraRenderingParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraRenderingParameters'
    @winrt_mixinmethod
    def SetFocusPoint(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetFocusPointWithNormal(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetFocusPointWithNormalLinearVelocity(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3, linearVelocity: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_mixinmethod
    def get_Direct3D11BackBuffer(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_ReprojectionMode(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2) -> Windows.Graphics.Holographic.HolographicReprojectionMode: ...
    @winrt_mixinmethod
    def put_ReprojectionMode(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2, value: Windows.Graphics.Holographic.HolographicReprojectionMode) -> Void: ...
    @winrt_mixinmethod
    def CommitDirect3D11DepthBuffer(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2, value: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentProtectionEnabled(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentProtectionEnabled(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DepthReprojectionMethod(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters4) -> Windows.Graphics.Holographic.HolographicDepthReprojectionMethod: ...
    @winrt_mixinmethod
    def put_DepthReprojectionMethod(self: Windows.Graphics.Holographic.IHolographicCameraRenderingParameters4, value: Windows.Graphics.Holographic.HolographicDepthReprojectionMethod) -> Void: ...
    Direct3D11Device = property(get_Direct3D11Device, None)
    Direct3D11BackBuffer = property(get_Direct3D11BackBuffer, None)
    ReprojectionMode = property(get_ReprojectionMode, put_ReprojectionMode)
    IsContentProtectionEnabled = property(get_IsContentProtectionEnabled, put_IsContentProtectionEnabled)
    DepthReprojectionMethod = property(get_DepthReprojectionMethod, put_DepthReprojectionMethod)
class HolographicCameraViewportParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicCameraViewportParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraViewportParameters'
    @winrt_mixinmethod
    def get_HiddenAreaMesh(self: Windows.Graphics.Holographic.IHolographicCameraViewportParameters) -> POINTER(Windows.Foundation.Numerics.Vector2_head): ...
    @winrt_mixinmethod
    def get_VisibleAreaMesh(self: Windows.Graphics.Holographic.IHolographicCameraViewportParameters) -> POINTER(Windows.Foundation.Numerics.Vector2_head): ...
    HiddenAreaMesh = property(get_HiddenAreaMesh, None)
    VisibleAreaMesh = property(get_VisibleAreaMesh, None)
HolographicDepthReprojectionMethod = Int32
HolographicDepthReprojectionMethod_DepthReprojection: HolographicDepthReprojectionMethod = 0
HolographicDepthReprojectionMethod_AutoPlanar: HolographicDepthReprojectionMethod = 1
class HolographicDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicDisplay
    _classid_ = 'Windows.Graphics.Holographic.HolographicDisplay'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Holographic.IHolographicDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxViewportSize(self: Windows.Graphics.Holographic.IHolographicDisplay) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Graphics.Holographic.IHolographicDisplay) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOpaque(self: Windows.Graphics.Holographic.IHolographicDisplay) -> Boolean: ...
    @winrt_mixinmethod
    def get_AdapterId(self: Windows.Graphics.Holographic.IHolographicDisplay) -> Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_mixinmethod
    def get_SpatialLocator(self: Windows.Graphics.Holographic.IHolographicDisplay) -> Windows.Perception.Spatial.SpatialLocator: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: Windows.Graphics.Holographic.IHolographicDisplay2) -> Double: ...
    @winrt_mixinmethod
    def TryGetViewConfiguration(self: Windows.Graphics.Holographic.IHolographicDisplay3, kind: Windows.Graphics.Holographic.HolographicViewConfigurationKind) -> Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Graphics.Holographic.IHolographicDisplayStatics) -> Windows.Graphics.Holographic.HolographicDisplay: ...
    DisplayName = property(get_DisplayName, None)
    MaxViewportSize = property(get_MaxViewportSize, None)
    IsStereo = property(get_IsStereo, None)
    IsOpaque = property(get_IsOpaque, None)
    AdapterId = property(get_AdapterId, None)
    SpatialLocator = property(get_SpatialLocator, None)
    RefreshRate = property(get_RefreshRate, None)
class HolographicFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFrame
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrame'
    @winrt_mixinmethod
    def get_AddedCameras(self: Windows.Graphics.Holographic.IHolographicFrame) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_mixinmethod
    def get_RemovedCameras(self: Windows.Graphics.Holographic.IHolographicFrame) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_mixinmethod
    def GetRenderingParameters(self: Windows.Graphics.Holographic.IHolographicFrame, cameraPose: Windows.Graphics.Holographic.HolographicCameraPose) -> Windows.Graphics.Holographic.HolographicCameraRenderingParameters: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Graphics.Holographic.IHolographicFrame) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_CurrentPrediction(self: Windows.Graphics.Holographic.IHolographicFrame) -> Windows.Graphics.Holographic.HolographicFramePrediction: ...
    @winrt_mixinmethod
    def UpdateCurrentPrediction(self: Windows.Graphics.Holographic.IHolographicFrame) -> Void: ...
    @winrt_mixinmethod
    def PresentUsingCurrentPrediction(self: Windows.Graphics.Holographic.IHolographicFrame) -> Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_mixinmethod
    def PresentUsingCurrentPredictionWithBehavior(self: Windows.Graphics.Holographic.IHolographicFrame, waitBehavior: Windows.Graphics.Holographic.HolographicFramePresentWaitBehavior) -> Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_mixinmethod
    def WaitForFrameToFinish(self: Windows.Graphics.Holographic.IHolographicFrame) -> Void: ...
    @winrt_mixinmethod
    def GetQuadLayerUpdateParameters(self: Windows.Graphics.Holographic.IHolographicFrame2, layer: Windows.Graphics.Holographic.HolographicQuadLayer) -> Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Graphics.Holographic.IHolographicFrame3) -> Windows.Graphics.Holographic.HolographicFrameId: ...
    AddedCameras = property(get_AddedCameras, None)
    RemovedCameras = property(get_RemovedCameras, None)
    Duration = property(get_Duration, None)
    CurrentPrediction = property(get_CurrentPrediction, None)
    Id = property(get_Id, None)
class HolographicFrameId(EasyCastStructure):
    Value: UInt64
class HolographicFramePrediction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFramePrediction
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePrediction'
    @winrt_mixinmethod
    def get_CameraPoses(self: Windows.Graphics.Holographic.IHolographicFramePrediction) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCameraPose]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Graphics.Holographic.IHolographicFramePrediction) -> Windows.Perception.PerceptionTimestamp: ...
    CameraPoses = property(get_CameraPoses, None)
    Timestamp = property(get_Timestamp, None)
HolographicFramePresentResult = Int32
HolographicFramePresentResult_Success: HolographicFramePresentResult = 0
HolographicFramePresentResult_DeviceRemoved: HolographicFramePresentResult = 1
HolographicFramePresentWaitBehavior = Int32
HolographicFramePresentWaitBehavior_WaitForFrameToFinish: HolographicFramePresentWaitBehavior = 0
HolographicFramePresentWaitBehavior_DoNotWaitForFrameToFinish: HolographicFramePresentWaitBehavior = 1
class HolographicFramePresentationMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFramePresentationMonitor
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePresentationMonitor'
    @winrt_mixinmethod
    def ReadReports(self: Windows.Graphics.Holographic.IHolographicFramePresentationMonitor) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicFramePresentationReport]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class HolographicFramePresentationReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFramePresentationReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePresentationReport'
    @winrt_mixinmethod
    def get_CompositorGpuDuration(self: Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_AppGpuDuration(self: Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_AppGpuOverrun(self: Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MissedPresentationOpportunityCount(self: Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_PresentationCount(self: Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> UInt32: ...
    CompositorGpuDuration = property(get_CompositorGpuDuration, None)
    AppGpuDuration = property(get_AppGpuDuration, None)
    AppGpuOverrun = property(get_AppGpuOverrun, None)
    MissedPresentationOpportunityCount = property(get_MissedPresentationOpportunityCount, None)
    PresentationCount = property(get_PresentationCount, None)
class HolographicFrameRenderingReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFrameRenderingReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameRenderingReport'
    @winrt_mixinmethod
    def get_FrameId(self: Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> Windows.Graphics.Holographic.HolographicFrameId: ...
    @winrt_mixinmethod
    def get_MissedLatchCount(self: Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_SystemRelativeFrameReadyTime(self: Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeActualGpuFinishTime(self: Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeTargetLatchTime(self: Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> Windows.Foundation.TimeSpan: ...
    FrameId = property(get_FrameId, None)
    MissedLatchCount = property(get_MissedLatchCount, None)
    SystemRelativeFrameReadyTime = property(get_SystemRelativeFrameReadyTime, None)
    SystemRelativeActualGpuFinishTime = property(get_SystemRelativeActualGpuFinishTime, None)
    SystemRelativeTargetLatchTime = property(get_SystemRelativeTargetLatchTime, None)
class HolographicFrameScanoutMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFrameScanoutMonitor
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameScanoutMonitor'
    @winrt_mixinmethod
    def ReadReports(self: Windows.Graphics.Holographic.IHolographicFrameScanoutMonitor) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Holographic.HolographicFrameScanoutReport]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class HolographicFrameScanoutReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicFrameScanoutReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameScanoutReport'
    @winrt_mixinmethod
    def get_RenderingReport(self: Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> Windows.Graphics.Holographic.HolographicFrameRenderingReport: ...
    @winrt_mixinmethod
    def get_MissedScanoutCount(self: Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_SystemRelativeLatchTime(self: Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeScanoutStartTime(self: Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativePhotonTime(self: Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> Windows.Foundation.TimeSpan: ...
    RenderingReport = property(get_RenderingReport, None)
    MissedScanoutCount = property(get_MissedScanoutCount, None)
    SystemRelativeLatchTime = property(get_SystemRelativeLatchTime, None)
    SystemRelativeScanoutStartTime = property(get_SystemRelativeScanoutStartTime, None)
    SystemRelativePhotonTime = property(get_SystemRelativePhotonTime, None)
class HolographicQuadLayer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicQuadLayer
    _classid_ = 'Windows.Graphics.Holographic.HolographicQuadLayer'
    @winrt_factorymethod
    def Create(cls: Windows.Graphics.Holographic.IHolographicQuadLayerFactory, size: Windows.Foundation.Size) -> Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_factorymethod
    def CreateWithPixelFormat(cls: Windows.Graphics.Holographic.IHolographicQuadLayerFactory, size: Windows.Foundation.Size, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat) -> Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: Windows.Graphics.Holographic.IHolographicQuadLayer) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Graphics.Holographic.IHolographicQuadLayer) -> Windows.Foundation.Size: ...
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class HolographicQuadLayerUpdateParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters'
    @winrt_mixinmethod
    def AcquireBufferToUpdateContent(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def UpdateViewport(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def UpdateContentProtectionEnabled(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def UpdateExtents(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def UpdateLocationWithStationaryMode(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def UpdateLocationWithDisplayRelativeMode(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_CanAcquireWithHardwareProtection(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters2) -> Boolean: ...
    @winrt_mixinmethod
    def AcquireBufferToUpdateContentWithHardwareProtection(self: Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters2) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    CanAcquireWithHardwareProtection = property(get_CanAcquireWithHardwareProtection, None)
HolographicReprojectionMode = Int32
HolographicReprojectionMode_PositionAndOrientation: HolographicReprojectionMode = 0
HolographicReprojectionMode_OrientationOnly: HolographicReprojectionMode = 1
HolographicReprojectionMode_Disabled: HolographicReprojectionMode = 2
class HolographicSpace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicSpace
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpace'
    @winrt_mixinmethod
    def get_PrimaryAdapterId(self: Windows.Graphics.Holographic.IHolographicSpace) -> Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_mixinmethod
    def SetDirect3D11Device(self: Windows.Graphics.Holographic.IHolographicSpace, value: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_mixinmethod
    def add_CameraAdded(self: Windows.Graphics.Holographic.IHolographicSpace, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraAdded(self: Windows.Graphics.Holographic.IHolographicSpace, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraRemoved(self: Windows.Graphics.Holographic.IHolographicSpace, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraRemoved(self: Windows.Graphics.Holographic.IHolographicSpace, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateNextFrame(self: Windows.Graphics.Holographic.IHolographicSpace) -> Windows.Graphics.Holographic.HolographicFrame: ...
    @winrt_mixinmethod
    def get_UserPresence(self: Windows.Graphics.Holographic.IHolographicSpace2) -> Windows.Graphics.Holographic.HolographicSpaceUserPresence: ...
    @winrt_mixinmethod
    def add_UserPresenceChanged(self: Windows.Graphics.Holographic.IHolographicSpace2, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserPresenceChanged(self: Windows.Graphics.Holographic.IHolographicSpace2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def WaitForNextFrameReady(self: Windows.Graphics.Holographic.IHolographicSpace2) -> Void: ...
    @winrt_mixinmethod
    def WaitForNextFrameReadyWithHeadStart(self: Windows.Graphics.Holographic.IHolographicSpace2, requestedHeadStartDuration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def CreateFramePresentationMonitor(self: Windows.Graphics.Holographic.IHolographicSpace2, maxQueuedReports: UInt32) -> Windows.Graphics.Holographic.HolographicFramePresentationMonitor: ...
    @winrt_mixinmethod
    def CreateFrameScanoutMonitor(self: Windows.Graphics.Holographic.IHolographicSpace3, maxQueuedReports: UInt32) -> Windows.Graphics.Holographic.HolographicFrameScanoutMonitor: ...
    @winrt_classmethod
    def get_IsConfigured(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics3) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_IsAvailable(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics2) -> Boolean: ...
    @winrt_classmethod
    def add_IsAvailableChanged(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics2, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsAvailableChanged(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateForCoreWindow(cls: Windows.Graphics.Holographic.IHolographicSpaceStatics, window: Windows.UI.Core.CoreWindow) -> Windows.Graphics.Holographic.HolographicSpace: ...
    PrimaryAdapterId = property(get_PrimaryAdapterId, None)
    UserPresence = property(get_UserPresence, None)
    IsConfigured = property(get_IsConfigured, None)
    IsSupported = property(get_IsSupported, None)
    IsAvailable = property(get_IsAvailable, None)
class HolographicSpaceCameraAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs'
    @winrt_mixinmethod
    def get_Camera(self: Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs) -> Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs) -> Windows.Foundation.Deferral: ...
    Camera = property(get_Camera, None)
class HolographicSpaceCameraRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicSpaceCameraRemovedEventArgs
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs'
    @winrt_mixinmethod
    def get_Camera(self: Windows.Graphics.Holographic.IHolographicSpaceCameraRemovedEventArgs) -> Windows.Graphics.Holographic.HolographicCamera: ...
    Camera = property(get_Camera, None)
HolographicSpaceUserPresence = Int32
HolographicSpaceUserPresence_Absent: HolographicSpaceUserPresence = 0
HolographicSpaceUserPresence_PresentPassive: HolographicSpaceUserPresence = 1
HolographicSpaceUserPresence_PresentActive: HolographicSpaceUserPresence = 2
class HolographicStereoTransform(EasyCastStructure):
    Left: Windows.Foundation.Numerics.Matrix4x4
    Right: Windows.Foundation.Numerics.Matrix4x4
class HolographicViewConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Holographic.IHolographicViewConfiguration
    _classid_ = 'Windows.Graphics.Holographic.HolographicViewConfiguration'
    @winrt_mixinmethod
    def get_NativeRenderTargetSize(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_RenderTargetSize(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def RequestRenderTargetSize(self: Windows.Graphics.Holographic.IHolographicViewConfiguration, size: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SupportedPixelFormats(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_PixelFormat(self: Windows.Graphics.Holographic.IHolographicViewConfiguration, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Double: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Graphics.Holographic.HolographicViewConfigurationKind: ...
    @winrt_mixinmethod
    def get_Display(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.Graphics.Holographic.IHolographicViewConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedDepthReprojectionMethods(self: Windows.Graphics.Holographic.IHolographicViewConfiguration2) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]: ...
    NativeRenderTargetSize = property(get_NativeRenderTargetSize, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    SupportedPixelFormats = property(get_SupportedPixelFormats, None)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    IsStereo = property(get_IsStereo, None)
    RefreshRate = property(get_RefreshRate, None)
    Kind = property(get_Kind, None)
    Display = property(get_Display, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    SupportedDepthReprojectionMethods = property(get_SupportedDepthReprojectionMethods, None)
HolographicViewConfigurationKind = Int32
HolographicViewConfigurationKind_Display: HolographicViewConfigurationKind = 0
HolographicViewConfigurationKind_PhotoVideoCamera: HolographicViewConfigurationKind = 1
class IHolographicCamera(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e4e98445-9bed-4980-9ba0-e87680d1cb74}')
    @winrt_commethod(6)
    def get_RenderTargetSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_ViewportScaleFactor(self) -> Double: ...
    @winrt_commethod(8)
    def put_ViewportScaleFactor(self, value: Double) -> Void: ...
    @winrt_commethod(9)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(11)
    def SetNearPlaneDistance(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def SetFarPlaneDistance(self, value: Double) -> Void: ...
    RenderTargetSize = property(get_RenderTargetSize, None)
    ViewportScaleFactor = property(get_ViewportScaleFactor, put_ViewportScaleFactor)
    IsStereo = property(get_IsStereo, None)
    Id = property(get_Id, None)
class IHolographicCamera2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b55b9f1a-ba8c-4f84-ad79-2e7e1e2450f3}')
    @winrt_commethod(6)
    def get_LeftViewportParameters(self) -> Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_commethod(7)
    def get_RightViewportParameters(self) -> Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_commethod(8)
    def get_Display(self) -> Windows.Graphics.Holographic.HolographicDisplay: ...
    LeftViewportParameters = property(get_LeftViewportParameters, None)
    RightViewportParameters = property(get_RightViewportParameters, None)
    Display = property(get_Display, None)
class IHolographicCamera3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{45aa4fb3-7b59-524e-4a3f-4a6ad6650477}')
    @winrt_commethod(6)
    def get_IsPrimaryLayerEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPrimaryLayerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MaxQuadLayerCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_QuadLayers(self) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Holographic.HolographicQuadLayer]: ...
    IsPrimaryLayerEnabled = property(get_IsPrimaryLayerEnabled, put_IsPrimaryLayerEnabled)
    MaxQuadLayerCount = property(get_MaxQuadLayerCount, None)
    QuadLayers = property(get_QuadLayers, None)
class IHolographicCamera4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9a2531d6-4723-4f39-a9a5-9d05181d9b44}')
    @winrt_commethod(6)
    def get_CanOverrideViewport(self) -> Boolean: ...
    CanOverrideViewport = property(get_CanOverrideViewport, None)
class IHolographicCamera5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{229706f2-628d-4ef5-9c08-a63fdd7787c6}')
    @winrt_commethod(6)
    def get_IsHardwareContentProtectionSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsHardwareContentProtectionEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsHardwareContentProtectionEnabled(self, value: Boolean) -> Void: ...
    IsHardwareContentProtectionSupported = property(get_IsHardwareContentProtectionSupported, None)
    IsHardwareContentProtectionEnabled = property(get_IsHardwareContentProtectionEnabled, put_IsHardwareContentProtectionEnabled)
class IHolographicCamera6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0209194f-632d-5154-ab52-0b5d15b12505}')
    @winrt_commethod(6)
    def get_ViewConfiguration(self) -> Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    ViewConfiguration = property(get_ViewConfiguration, None)
class IHolographicCameraPose(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0d7d7e30-12de-45bd-912b-c7f6561599d1}')
    @winrt_commethod(6)
    def get_HolographicCamera(self) -> Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_commethod(7)
    def get_Viewport(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def TryGetViewTransform(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Graphics.Holographic.HolographicStereoTransform]: ...
    @winrt_commethod(9)
    def get_ProjectionTransform(self) -> Windows.Graphics.Holographic.HolographicStereoTransform: ...
    @winrt_commethod(10)
    def TryGetCullingFrustum(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_commethod(11)
    def TryGetVisibleFrustum(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_commethod(12)
    def get_NearPlaneDistance(self) -> Double: ...
    @winrt_commethod(13)
    def get_FarPlaneDistance(self) -> Double: ...
    HolographicCamera = property(get_HolographicCamera, None)
    Viewport = property(get_Viewport, None)
    ProjectionTransform = property(get_ProjectionTransform, None)
    NearPlaneDistance = property(get_NearPlaneDistance, None)
    FarPlaneDistance = property(get_FarPlaneDistance, None)
class IHolographicCameraPose2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{232be073-5d2d-4560-814e-2697c4fce16b}')
    @winrt_commethod(6)
    def OverrideViewTransform(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, coordinateSystemToViewTransform: Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_commethod(7)
    def OverrideProjectionTransform(self, projectionTransform: Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_commethod(8)
    def OverrideViewport(self, leftViewport: Windows.Foundation.Rect, rightViewport: Windows.Foundation.Rect) -> Void: ...
class IHolographicCameraRenderingParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8eac2ed1-5bf4-4e16-8236-ae0800c11d0d}')
    @winrt_commethod(6)
    def SetFocusPoint(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def SetFocusPointWithNormal(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def SetFocusPointWithNormalLinearVelocity(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, normal: Windows.Foundation.Numerics.Vector3, linearVelocity: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(9)
    def get_Direct3D11Device(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_commethod(10)
    def get_Direct3D11BackBuffer(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    Direct3D11Device = property(get_Direct3D11Device, None)
    Direct3D11BackBuffer = property(get_Direct3D11BackBuffer, None)
class IHolographicCameraRenderingParameters2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{261270e3-b696-4634-94d6-be0681643599}')
    @winrt_commethod(6)
    def get_ReprojectionMode(self) -> Windows.Graphics.Holographic.HolographicReprojectionMode: ...
    @winrt_commethod(7)
    def put_ReprojectionMode(self, value: Windows.Graphics.Holographic.HolographicReprojectionMode) -> Void: ...
    @winrt_commethod(8)
    def CommitDirect3D11DepthBuffer(self, value: Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Void: ...
    ReprojectionMode = property(get_ReprojectionMode, put_ReprojectionMode)
class IHolographicCameraRenderingParameters3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b1aa513f-136d-4b06-b9d4-e4b914cd0683}')
    @winrt_commethod(6)
    def get_IsContentProtectionEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsContentProtectionEnabled(self, value: Boolean) -> Void: ...
    IsContentProtectionEnabled = property(get_IsContentProtectionEnabled, put_IsContentProtectionEnabled)
class IHolographicCameraRenderingParameters4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0878fa4c-e163-57dc-82b7-c406ab3e0537}')
    @winrt_commethod(6)
    def get_DepthReprojectionMethod(self) -> Windows.Graphics.Holographic.HolographicDepthReprojectionMethod: ...
    @winrt_commethod(7)
    def put_DepthReprojectionMethod(self, value: Windows.Graphics.Holographic.HolographicDepthReprojectionMethod) -> Void: ...
    DepthReprojectionMethod = property(get_DepthReprojectionMethod, put_DepthReprojectionMethod)
class IHolographicCameraViewportParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{80cdf3f7-842a-41e1-93ed-5692ab1fbb10}')
    @winrt_commethod(6)
    def get_HiddenAreaMesh(self) -> POINTER(Windows.Foundation.Numerics.Vector2_head): ...
    @winrt_commethod(7)
    def get_VisibleAreaMesh(self) -> POINTER(Windows.Foundation.Numerics.Vector2_head): ...
    HiddenAreaMesh = property(get_HiddenAreaMesh, None)
    VisibleAreaMesh = property(get_VisibleAreaMesh, None)
class IHolographicDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9acea414-1d9f-4090-a388-90c06f6eae9c}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxViewportSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsOpaque(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_AdapterId(self) -> Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_commethod(11)
    def get_SpatialLocator(self) -> Windows.Perception.Spatial.SpatialLocator: ...
    DisplayName = property(get_DisplayName, None)
    MaxViewportSize = property(get_MaxViewportSize, None)
    IsStereo = property(get_IsStereo, None)
    IsOpaque = property(get_IsOpaque, None)
    AdapterId = property(get_AdapterId, None)
    SpatialLocator = property(get_SpatialLocator, None)
class IHolographicDisplay2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{75ac3f82-e755-436c-8d96-4d32d131473e}')
    @winrt_commethod(6)
    def get_RefreshRate(self) -> Double: ...
    RefreshRate = property(get_RefreshRate, None)
class IHolographicDisplay3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fc4c6ac6-6480-5008-b29e-157d77c843f7}')
    @winrt_commethod(6)
    def TryGetViewConfiguration(self, kind: Windows.Graphics.Holographic.HolographicViewConfigurationKind) -> Windows.Graphics.Holographic.HolographicViewConfiguration: ...
class IHolographicDisplayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cb374983-e7b0-4841-8355-3ae5b536e9a4}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Graphics.Holographic.HolographicDisplay: ...
class IHolographicFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c6988eb6-a8b9-3054-a6eb-d624b6536375}')
    @winrt_commethod(6)
    def get_AddedCameras(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_commethod(7)
    def get_RemovedCameras(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_commethod(8)
    def GetRenderingParameters(self, cameraPose: Windows.Graphics.Holographic.HolographicCameraPose) -> Windows.Graphics.Holographic.HolographicCameraRenderingParameters: ...
    @winrt_commethod(9)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_CurrentPrediction(self) -> Windows.Graphics.Holographic.HolographicFramePrediction: ...
    @winrt_commethod(11)
    def UpdateCurrentPrediction(self) -> Void: ...
    @winrt_commethod(12)
    def PresentUsingCurrentPrediction(self) -> Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_commethod(13)
    def PresentUsingCurrentPredictionWithBehavior(self, waitBehavior: Windows.Graphics.Holographic.HolographicFramePresentWaitBehavior) -> Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_commethod(14)
    def WaitForFrameToFinish(self) -> Void: ...
    AddedCameras = property(get_AddedCameras, None)
    RemovedCameras = property(get_RemovedCameras, None)
    Duration = property(get_Duration, None)
    CurrentPrediction = property(get_CurrentPrediction, None)
class IHolographicFrame2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{283f37bf-3bf2-5e91-6633-870574e6f217}')
    @winrt_commethod(6)
    def GetQuadLayerUpdateParameters(self, layer: Windows.Graphics.Holographic.HolographicQuadLayer) -> Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters: ...
class IHolographicFrame3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e5e964c9-8a27-55d3-9f98-94530d369052}')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.Graphics.Holographic.HolographicFrameId: ...
    Id = property(get_Id, None)
class IHolographicFramePrediction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{520f4de1-5c0a-4e79-a81e-6abe02bb2739}')
    @winrt_commethod(6)
    def get_CameraPoses(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicCameraPose]: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Perception.PerceptionTimestamp: ...
    CameraPoses = property(get_CameraPoses, None)
    Timestamp = property(get_Timestamp, None)
class IHolographicFramePresentationMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ca87256c-6fae-428e-bb83-25dfee51136b}')
    @winrt_commethod(6)
    def ReadReports(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicFramePresentationReport]: ...
class IHolographicFramePresentationReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{80baf614-f2f4-4c8a-8de3-065c78f6d5de}')
    @winrt_commethod(6)
    def get_CompositorGpuDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_AppGpuDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_AppGpuOverrun(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MissedPresentationOpportunityCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PresentationCount(self) -> UInt32: ...
    CompositorGpuDuration = property(get_CompositorGpuDuration, None)
    AppGpuDuration = property(get_AppGpuDuration, None)
    AppGpuOverrun = property(get_AppGpuOverrun, None)
    MissedPresentationOpportunityCount = property(get_MissedPresentationOpportunityCount, None)
    PresentationCount = property(get_PresentationCount, None)
class IHolographicFrameRenderingReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{05f32de4-e384-51b3-b934-f0d3a0f78606}')
    @winrt_commethod(6)
    def get_FrameId(self) -> Windows.Graphics.Holographic.HolographicFrameId: ...
    @winrt_commethod(7)
    def get_MissedLatchCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SystemRelativeFrameReadyTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_SystemRelativeActualGpuFinishTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SystemRelativeTargetLatchTime(self) -> Windows.Foundation.TimeSpan: ...
    FrameId = property(get_FrameId, None)
    MissedLatchCount = property(get_MissedLatchCount, None)
    SystemRelativeFrameReadyTime = property(get_SystemRelativeFrameReadyTime, None)
    SystemRelativeActualGpuFinishTime = property(get_SystemRelativeActualGpuFinishTime, None)
    SystemRelativeTargetLatchTime = property(get_SystemRelativeTargetLatchTime, None)
class IHolographicFrameScanoutMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7e83efa9-843c-5401-8095-9bc1b8b08638}')
    @winrt_commethod(6)
    def ReadReports(self) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Holographic.HolographicFrameScanoutReport]: ...
class IHolographicFrameScanoutReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0ebbe606-03a0-5ca0-b46e-bba068d7233f}')
    @winrt_commethod(6)
    def get_RenderingReport(self) -> Windows.Graphics.Holographic.HolographicFrameRenderingReport: ...
    @winrt_commethod(7)
    def get_MissedScanoutCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SystemRelativeLatchTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_SystemRelativeScanoutStartTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SystemRelativePhotonTime(self) -> Windows.Foundation.TimeSpan: ...
    RenderingReport = property(get_RenderingReport, None)
    MissedScanoutCount = property(get_MissedScanoutCount, None)
    SystemRelativeLatchTime = property(get_SystemRelativeLatchTime, None)
    SystemRelativeScanoutStartTime = property(get_SystemRelativeScanoutStartTime, None)
    SystemRelativePhotonTime = property(get_SystemRelativePhotonTime, None)
class IHolographicQuadLayer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{903460c9-c9d9-5d5c-41ac-a2d5ab0fd331}')
    @winrt_commethod(6)
    def get_PixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def get_Size(self) -> Windows.Foundation.Size: ...
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class IHolographicQuadLayerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a67538f3-5a14-5a10-489a-455065b37b76}')
    @winrt_commethod(6)
    def Create(self, size: Windows.Foundation.Size) -> Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_commethod(7)
    def CreateWithPixelFormat(self, size: Windows.Foundation.Size, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat) -> Windows.Graphics.Holographic.HolographicQuadLayer: ...
class IHolographicQuadLayerUpdateParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2b0ea3b0-798d-5bca-55c2-2c0c762ebb08}')
    @winrt_commethod(6)
    def AcquireBufferToUpdateContent(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(7)
    def UpdateViewport(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def UpdateContentProtectionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def UpdateExtents(self, value: Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def UpdateLocationWithStationaryMode(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(11)
    def UpdateLocationWithDisplayRelativeMode(self, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Void: ...
class IHolographicQuadLayerUpdateParameters2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4f33d32d-82c1-46c1-8980-3cb70d98182b}')
    @winrt_commethod(6)
    def get_CanAcquireWithHardwareProtection(self) -> Boolean: ...
    @winrt_commethod(7)
    def AcquireBufferToUpdateContentWithHardwareProtection(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    CanAcquireWithHardwareProtection = property(get_CanAcquireWithHardwareProtection, None)
class IHolographicSpace(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4380dba6-5e78-434f-807c-3433d1efe8b7}')
    @winrt_commethod(6)
    def get_PrimaryAdapterId(self) -> Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_commethod(7)
    def SetDirect3D11Device(self, value: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_commethod(8)
    def add_CameraAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CameraAdded(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CameraRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraRemoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def CreateNextFrame(self) -> Windows.Graphics.Holographic.HolographicFrame: ...
    PrimaryAdapterId = property(get_PrimaryAdapterId, None)
class IHolographicSpace2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4f81a9a8-b7ff-4883-9827-7d677287ea70}')
    @winrt_commethod(6)
    def get_UserPresence(self) -> Windows.Graphics.Holographic.HolographicSpaceUserPresence: ...
    @winrt_commethod(7)
    def add_UserPresenceChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Holographic.HolographicSpace, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_UserPresenceChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def WaitForNextFrameReady(self) -> Void: ...
    @winrt_commethod(10)
    def WaitForNextFrameReadyWithHeadStart(self, requestedHeadStartDuration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def CreateFramePresentationMonitor(self, maxQueuedReports: UInt32) -> Windows.Graphics.Holographic.HolographicFramePresentationMonitor: ...
    UserPresence = property(get_UserPresence, None)
class IHolographicSpace3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{df1733d1-f224-587e-8d71-1e8fc8f07b1f}')
    @winrt_commethod(6)
    def CreateFrameScanoutMonitor(self, maxQueuedReports: UInt32) -> Windows.Graphics.Holographic.HolographicFrameScanoutMonitor: ...
class IHolographicSpaceCameraAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{58f1da35-bbb3-3c8f-993d-6c80e7feb99f}')
    @winrt_commethod(6)
    def get_Camera(self) -> Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Camera = property(get_Camera, None)
class IHolographicSpaceCameraRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{805444a8-f2ae-322e-8da9-836a0a95a4c1}')
    @winrt_commethod(6)
    def get_Camera(self) -> Windows.Graphics.Holographic.HolographicCamera: ...
    Camera = property(get_Camera, None)
class IHolographicSpaceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{364e6064-c8f2-3ba1-8391-66b8489e67fd}')
    @winrt_commethod(6)
    def CreateForCoreWindow(self, window: Windows.UI.Core.CoreWindow) -> Windows.Graphics.Holographic.HolographicSpace: ...
class IHolographicSpaceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0e777088-75fc-48af-8758-0652f6f07c59}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsAvailable(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_IsAvailableChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsAvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    IsAvailable = property(get_IsAvailable, None)
class IHolographicSpaceStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3b00de3d-b1a3-4dfe-8e79-fec5909e6df8}')
    @winrt_commethod(6)
    def get_IsConfigured(self) -> Boolean: ...
    IsConfigured = property(get_IsConfigured, None)
class IHolographicViewConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c1de6e6-67e9-5004-b02c-67a3a122b576}')
    @winrt_commethod(6)
    def get_NativeRenderTargetSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_RenderTargetSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def RequestRenderTargetSize(self, size: Windows.Foundation.Size) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_SupportedPixelFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(10)
    def get_PixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(11)
    def put_PixelFormat(self, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(12)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_RefreshRate(self) -> Double: ...
    @winrt_commethod(14)
    def get_Kind(self) -> Windows.Graphics.Holographic.HolographicViewConfigurationKind: ...
    @winrt_commethod(15)
    def get_Display(self) -> Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_commethod(16)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    NativeRenderTargetSize = property(get_NativeRenderTargetSize, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    SupportedPixelFormats = property(get_SupportedPixelFormats, None)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    IsStereo = property(get_IsStereo, None)
    RefreshRate = property(get_RefreshRate, None)
    Kind = property(get_Kind, None)
    Display = property(get_Display, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IHolographicViewConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e241756e-e0d0-5019-9af5-1b165bc2f54e}')
    @winrt_commethod(6)
    def get_SupportedDepthReprojectionMethods(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]: ...
    SupportedDepthReprojectionMethods = property(get_SupportedDepthReprojectionMethods, None)
make_head(_module, 'HolographicAdapterId')
make_head(_module, 'HolographicCamera')
make_head(_module, 'HolographicCameraPose')
make_head(_module, 'HolographicCameraRenderingParameters')
make_head(_module, 'HolographicCameraViewportParameters')
make_head(_module, 'HolographicDisplay')
make_head(_module, 'HolographicFrame')
make_head(_module, 'HolographicFrameId')
make_head(_module, 'HolographicFramePrediction')
make_head(_module, 'HolographicFramePresentationMonitor')
make_head(_module, 'HolographicFramePresentationReport')
make_head(_module, 'HolographicFrameRenderingReport')
make_head(_module, 'HolographicFrameScanoutMonitor')
make_head(_module, 'HolographicFrameScanoutReport')
make_head(_module, 'HolographicQuadLayer')
make_head(_module, 'HolographicQuadLayerUpdateParameters')
make_head(_module, 'HolographicSpace')
make_head(_module, 'HolographicSpaceCameraAddedEventArgs')
make_head(_module, 'HolographicSpaceCameraRemovedEventArgs')
make_head(_module, 'HolographicStereoTransform')
make_head(_module, 'HolographicViewConfiguration')
make_head(_module, 'IHolographicCamera')
make_head(_module, 'IHolographicCamera2')
make_head(_module, 'IHolographicCamera3')
make_head(_module, 'IHolographicCamera4')
make_head(_module, 'IHolographicCamera5')
make_head(_module, 'IHolographicCamera6')
make_head(_module, 'IHolographicCameraPose')
make_head(_module, 'IHolographicCameraPose2')
make_head(_module, 'IHolographicCameraRenderingParameters')
make_head(_module, 'IHolographicCameraRenderingParameters2')
make_head(_module, 'IHolographicCameraRenderingParameters3')
make_head(_module, 'IHolographicCameraRenderingParameters4')
make_head(_module, 'IHolographicCameraViewportParameters')
make_head(_module, 'IHolographicDisplay')
make_head(_module, 'IHolographicDisplay2')
make_head(_module, 'IHolographicDisplay3')
make_head(_module, 'IHolographicDisplayStatics')
make_head(_module, 'IHolographicFrame')
make_head(_module, 'IHolographicFrame2')
make_head(_module, 'IHolographicFrame3')
make_head(_module, 'IHolographicFramePrediction')
make_head(_module, 'IHolographicFramePresentationMonitor')
make_head(_module, 'IHolographicFramePresentationReport')
make_head(_module, 'IHolographicFrameRenderingReport')
make_head(_module, 'IHolographicFrameScanoutMonitor')
make_head(_module, 'IHolographicFrameScanoutReport')
make_head(_module, 'IHolographicQuadLayer')
make_head(_module, 'IHolographicQuadLayerFactory')
make_head(_module, 'IHolographicQuadLayerUpdateParameters')
make_head(_module, 'IHolographicQuadLayerUpdateParameters2')
make_head(_module, 'IHolographicSpace')
make_head(_module, 'IHolographicSpace2')
make_head(_module, 'IHolographicSpace3')
make_head(_module, 'IHolographicSpaceCameraAddedEventArgs')
make_head(_module, 'IHolographicSpaceCameraRemovedEventArgs')
make_head(_module, 'IHolographicSpaceStatics')
make_head(_module, 'IHolographicSpaceStatics2')
make_head(_module, 'IHolographicSpaceStatics3')
make_head(_module, 'IHolographicViewConfiguration')
make_head(_module, 'IHolographicViewConfiguration2')
