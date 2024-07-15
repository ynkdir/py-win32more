from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Holographic
import win32more.Windows.Perception
import win32more.Windows.Perception.Spatial
import win32more.Windows.UI.Core
import win32more.Windows.Win32.System.WinRT
class HolographicAdapterId(Structure):
    LowPart: UInt32
    HighPart: Int32
class HolographicCamera(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicCamera
    _classid_ = 'Windows.Graphics.Holographic.HolographicCamera'
    @winrt_mixinmethod
    def get_RenderTargetSize(self: win32more.Windows.Graphics.Holographic.IHolographicCamera) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_ViewportScaleFactor(self: win32more.Windows.Graphics.Holographic.IHolographicCamera) -> Double: ...
    @winrt_mixinmethod
    def put_ViewportScaleFactor(self: win32more.Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsStereo(self: win32more.Windows.Graphics.Holographic.IHolographicCamera) -> Boolean: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Graphics.Holographic.IHolographicCamera) -> UInt32: ...
    @winrt_mixinmethod
    def SetNearPlaneDistance(self: win32more.Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def SetFarPlaneDistance(self: win32more.Windows.Graphics.Holographic.IHolographicCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LeftViewportParameters(self: win32more.Windows.Graphics.Holographic.IHolographicCamera2) -> win32more.Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_mixinmethod
    def get_RightViewportParameters(self: win32more.Windows.Graphics.Holographic.IHolographicCamera2) -> win32more.Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_mixinmethod
    def get_Display(self: win32more.Windows.Graphics.Holographic.IHolographicCamera2) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_mixinmethod
    def get_IsPrimaryLayerEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCamera3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrimaryLayerEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCamera3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxQuadLayerCount(self: win32more.Windows.Graphics.Holographic.IHolographicCamera3) -> UInt32: ...
    @winrt_mixinmethod
    def get_QuadLayers(self: win32more.Windows.Graphics.Holographic.IHolographicCamera3) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Holographic.HolographicQuadLayer]: ...
    @winrt_mixinmethod
    def get_CanOverrideViewport(self: win32more.Windows.Graphics.Holographic.IHolographicCamera4) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHardwareContentProtectionSupported(self: win32more.Windows.Graphics.Holographic.IHolographicCamera5) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHardwareContentProtectionEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCamera5) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHardwareContentProtectionEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCamera5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ViewConfiguration(self: win32more.Windows.Graphics.Holographic.IHolographicCamera6) -> win32more.Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    CanOverrideViewport = property(get_CanOverrideViewport, None)
    Display = property(get_Display, None)
    Id = property(get_Id, None)
    IsHardwareContentProtectionEnabled = property(get_IsHardwareContentProtectionEnabled, put_IsHardwareContentProtectionEnabled)
    IsHardwareContentProtectionSupported = property(get_IsHardwareContentProtectionSupported, None)
    IsPrimaryLayerEnabled = property(get_IsPrimaryLayerEnabled, put_IsPrimaryLayerEnabled)
    IsStereo = property(get_IsStereo, None)
    LeftViewportParameters = property(get_LeftViewportParameters, None)
    MaxQuadLayerCount = property(get_MaxQuadLayerCount, None)
    QuadLayers = property(get_QuadLayers, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    RightViewportParameters = property(get_RightViewportParameters, None)
    ViewConfiguration = property(get_ViewConfiguration, None)
    ViewportScaleFactor = property(get_ViewportScaleFactor, put_ViewportScaleFactor)
class HolographicCameraPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicCameraPose
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraPose'
    @winrt_mixinmethod
    def get_HolographicCamera(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_mixinmethod
    def get_Viewport(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def TryGetViewTransform(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Graphics.Holographic.HolographicStereoTransform]: ...
    @winrt_mixinmethod
    def get_ProjectionTransform(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose) -> win32more.Windows.Graphics.Holographic.HolographicStereoTransform: ...
    @winrt_mixinmethod
    def TryGetCullingFrustum(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_mixinmethod
    def TryGetVisibleFrustum(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_mixinmethod
    def get_NearPlaneDistance(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose) -> Double: ...
    @winrt_mixinmethod
    def get_FarPlaneDistance(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose) -> Double: ...
    @winrt_mixinmethod
    def OverrideViewTransform(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose2, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, coordinateSystemToViewTransform: win32more.Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_mixinmethod
    def OverrideProjectionTransform(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose2, projectionTransform: win32more.Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_mixinmethod
    def OverrideViewport(self: win32more.Windows.Graphics.Holographic.IHolographicCameraPose2, leftViewport: win32more.Windows.Foundation.Rect, rightViewport: win32more.Windows.Foundation.Rect) -> Void: ...
    FarPlaneDistance = property(get_FarPlaneDistance, None)
    HolographicCamera = property(get_HolographicCamera, None)
    NearPlaneDistance = property(get_NearPlaneDistance, None)
    ProjectionTransform = property(get_ProjectionTransform, None)
    Viewport = property(get_Viewport, None)
class HolographicCameraRenderingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraRenderingParameters'
    @winrt_mixinmethod
    def SetFocusPoint(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetFocusPointWithNormal(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetFocusPointWithNormalLinearVelocity(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3, linearVelocity: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_mixinmethod
    def get_Direct3D11BackBuffer(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def get_ReprojectionMode(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2) -> win32more.Windows.Graphics.Holographic.HolographicReprojectionMode: ...
    @winrt_mixinmethod
    def put_ReprojectionMode(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2, value: win32more.Windows.Graphics.Holographic.HolographicReprojectionMode) -> Void: ...
    @winrt_mixinmethod
    def CommitDirect3D11DepthBuffer(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2, value: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentProtectionEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentProtectionEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DepthReprojectionMethod(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters4) -> win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod: ...
    @winrt_mixinmethod
    def put_DepthReprojectionMethod(self: win32more.Windows.Graphics.Holographic.IHolographicCameraRenderingParameters4, value: win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod) -> Void: ...
    DepthReprojectionMethod = property(get_DepthReprojectionMethod, put_DepthReprojectionMethod)
    Direct3D11BackBuffer = property(get_Direct3D11BackBuffer, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
    IsContentProtectionEnabled = property(get_IsContentProtectionEnabled, put_IsContentProtectionEnabled)
    ReprojectionMode = property(get_ReprojectionMode, put_ReprojectionMode)
class HolographicCameraViewportParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicCameraViewportParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicCameraViewportParameters'
    @winrt_mixinmethod
    def get_HiddenAreaMesh(self: win32more.Windows.Graphics.Holographic.IHolographicCameraViewportParameters) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_mixinmethod
    def get_VisibleAreaMesh(self: win32more.Windows.Graphics.Holographic.IHolographicCameraViewportParameters) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector2]: ...
    HiddenAreaMesh = property(get_HiddenAreaMesh, None)
    VisibleAreaMesh = property(get_VisibleAreaMesh, None)
class HolographicDepthReprojectionMethod(Enum, Int32):
    DepthReprojection = 0
    AutoPlanar = 1
class HolographicDisplay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicDisplay
    _classid_ = 'Windows.Graphics.Holographic.HolographicDisplay'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxViewportSize(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_IsStereo(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOpaque(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> Boolean: ...
    @winrt_mixinmethod
    def get_AdapterId(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> win32more.Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_mixinmethod
    def get_SpatialLocator(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay2) -> Double: ...
    @winrt_mixinmethod
    def TryGetViewConfiguration(self: win32more.Windows.Graphics.Holographic.IHolographicDisplay3, kind: win32more.Windows.Graphics.Holographic.HolographicViewConfigurationKind) -> win32more.Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Graphics.Holographic.IHolographicDisplayStatics) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
    AdapterId = property(get_AdapterId, None)
    DisplayName = property(get_DisplayName, None)
    IsOpaque = property(get_IsOpaque, None)
    IsStereo = property(get_IsStereo, None)
    MaxViewportSize = property(get_MaxViewportSize, None)
    RefreshRate = property(get_RefreshRate, None)
    SpatialLocator = property(get_SpatialLocator, None)
class HolographicFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFrame
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrame'
    @winrt_mixinmethod
    def get_AddedCameras(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_mixinmethod
    def get_RemovedCameras(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_mixinmethod
    def GetRenderingParameters(self: win32more.Windows.Graphics.Holographic.IHolographicFrame, cameraPose: win32more.Windows.Graphics.Holographic.HolographicCameraPose) -> win32more.Windows.Graphics.Holographic.HolographicCameraRenderingParameters: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_CurrentPrediction(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> win32more.Windows.Graphics.Holographic.HolographicFramePrediction: ...
    @winrt_mixinmethod
    def UpdateCurrentPrediction(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> Void: ...
    @winrt_mixinmethod
    def PresentUsingCurrentPrediction(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_mixinmethod
    def PresentUsingCurrentPredictionWithBehavior(self: win32more.Windows.Graphics.Holographic.IHolographicFrame, waitBehavior: win32more.Windows.Graphics.Holographic.HolographicFramePresentWaitBehavior) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_mixinmethod
    def WaitForFrameToFinish(self: win32more.Windows.Graphics.Holographic.IHolographicFrame) -> Void: ...
    @winrt_mixinmethod
    def GetQuadLayerUpdateParameters(self: win32more.Windows.Graphics.Holographic.IHolographicFrame2, layer: win32more.Windows.Graphics.Holographic.HolographicQuadLayer) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Graphics.Holographic.IHolographicFrame3) -> win32more.Windows.Graphics.Holographic.HolographicFrameId: ...
    AddedCameras = property(get_AddedCameras, None)
    CurrentPrediction = property(get_CurrentPrediction, None)
    Duration = property(get_Duration, None)
    Id = property(get_Id, None)
    RemovedCameras = property(get_RemovedCameras, None)
class HolographicFrameId(Structure):
    Value: UInt64
class HolographicFramePrediction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFramePrediction
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePrediction'
    @winrt_mixinmethod
    def get_CameraPoses(self: win32more.Windows.Graphics.Holographic.IHolographicFramePrediction) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCameraPose]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Graphics.Holographic.IHolographicFramePrediction) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    CameraPoses = property(get_CameraPoses, None)
    Timestamp = property(get_Timestamp, None)
class HolographicFramePresentResult(Enum, Int32):
    Success = 0
    DeviceRemoved = 1
class HolographicFramePresentWaitBehavior(Enum, Int32):
    WaitForFrameToFinish = 0
    DoNotWaitForFrameToFinish = 1
class HolographicFramePresentationMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationMonitor
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePresentationMonitor'
    @winrt_mixinmethod
    def ReadReports(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationMonitor) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicFramePresentationReport]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class HolographicFramePresentationReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFramePresentationReport'
    @winrt_mixinmethod
    def get_CompositorGpuDuration(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_AppGpuDuration(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_AppGpuOverrun(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MissedPresentationOpportunityCount(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_PresentationCount(self: win32more.Windows.Graphics.Holographic.IHolographicFramePresentationReport) -> UInt32: ...
    AppGpuDuration = property(get_AppGpuDuration, None)
    AppGpuOverrun = property(get_AppGpuOverrun, None)
    CompositorGpuDuration = property(get_CompositorGpuDuration, None)
    MissedPresentationOpportunityCount = property(get_MissedPresentationOpportunityCount, None)
    PresentationCount = property(get_PresentationCount, None)
class HolographicFrameRenderingReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameRenderingReport'
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> win32more.Windows.Graphics.Holographic.HolographicFrameId: ...
    @winrt_mixinmethod
    def get_MissedLatchCount(self: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_SystemRelativeFrameReadyTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeActualGpuFinishTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeTargetLatchTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameRenderingReport) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameId = property(get_FrameId, None)
    MissedLatchCount = property(get_MissedLatchCount, None)
    SystemRelativeActualGpuFinishTime = property(get_SystemRelativeActualGpuFinishTime, None)
    SystemRelativeFrameReadyTime = property(get_SystemRelativeFrameReadyTime, None)
    SystemRelativeTargetLatchTime = property(get_SystemRelativeTargetLatchTime, None)
class HolographicFrameScanoutMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutMonitor
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameScanoutMonitor'
    @winrt_mixinmethod
    def ReadReports(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutMonitor) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Holographic.HolographicFrameScanoutReport]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class HolographicFrameScanoutReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport
    _classid_ = 'Windows.Graphics.Holographic.HolographicFrameScanoutReport'
    @winrt_mixinmethod
    def get_RenderingReport(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> win32more.Windows.Graphics.Holographic.HolographicFrameRenderingReport: ...
    @winrt_mixinmethod
    def get_MissedScanoutCount(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_SystemRelativeLatchTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeScanoutStartTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativePhotonTime(self: win32more.Windows.Graphics.Holographic.IHolographicFrameScanoutReport) -> win32more.Windows.Foundation.TimeSpan: ...
    MissedScanoutCount = property(get_MissedScanoutCount, None)
    RenderingReport = property(get_RenderingReport, None)
    SystemRelativeLatchTime = property(get_SystemRelativeLatchTime, None)
    SystemRelativePhotonTime = property(get_SystemRelativePhotonTime, None)
    SystemRelativeScanoutStartTime = property(get_SystemRelativeScanoutStartTime, None)
class HolographicQuadLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicQuadLayer
    _classid_ = 'Windows.Graphics.Holographic.HolographicQuadLayer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Holographic.HolographicQuadLayer.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Graphics.Holographic.HolographicQuadLayer.CreateWithPixelFormat(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerFactory, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_factorymethod
    def CreateWithPixelFormat(cls: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerFactory, size: win32more.Windows.Foundation.Size, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayer) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayer) -> win32more.Windows.Foundation.Size: ...
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class HolographicQuadLayerUpdateParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters
    _classid_ = 'Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters'
    @winrt_mixinmethod
    def AcquireBufferToUpdateContent(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_mixinmethod
    def UpdateViewport(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def UpdateContentProtectionEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def UpdateExtents(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def UpdateLocationWithStationaryMode(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def UpdateLocationWithDisplayRelativeMode(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_CanAcquireWithHardwareProtection(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters2) -> Boolean: ...
    @winrt_mixinmethod
    def AcquireBufferToUpdateContentWithHardwareProtection(self: win32more.Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters2) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    CanAcquireWithHardwareProtection = property(get_CanAcquireWithHardwareProtection, None)
class HolographicReprojectionMode(Enum, Int32):
    PositionAndOrientation = 0
    OrientationOnly = 1
    Disabled = 2
class _HolographicSpace_Meta_(ComPtr.__class__):
    pass
class HolographicSpace(ComPtr, metaclass=_HolographicSpace_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicSpace
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpace'
    @winrt_mixinmethod
    def get_PrimaryAdapterId(self: win32more.Windows.Graphics.Holographic.IHolographicSpace) -> win32more.Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_mixinmethod
    def SetDirect3D11Device(self: win32more.Windows.Graphics.Holographic.IHolographicSpace, value: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_mixinmethod
    def add_CameraAdded(self: win32more.Windows.Graphics.Holographic.IHolographicSpace, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraAdded(self: win32more.Windows.Graphics.Holographic.IHolographicSpace, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraRemoved(self: win32more.Windows.Graphics.Holographic.IHolographicSpace, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraRemoved(self: win32more.Windows.Graphics.Holographic.IHolographicSpace, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateNextFrame(self: win32more.Windows.Graphics.Holographic.IHolographicSpace) -> win32more.Windows.Graphics.Holographic.HolographicFrame: ...
    @winrt_mixinmethod
    def get_UserPresence(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2) -> win32more.Windows.Graphics.Holographic.HolographicSpaceUserPresence: ...
    @winrt_mixinmethod
    def add_UserPresenceChanged(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserPresenceChanged(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def WaitForNextFrameReady(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2) -> Void: ...
    @winrt_mixinmethod
    def WaitForNextFrameReadyWithHeadStart(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2, requestedHeadStartDuration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def CreateFramePresentationMonitor(self: win32more.Windows.Graphics.Holographic.IHolographicSpace2, maxQueuedReports: UInt32) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentationMonitor: ...
    @winrt_mixinmethod
    def CreateFrameScanoutMonitor(self: win32more.Windows.Graphics.Holographic.IHolographicSpace3, maxQueuedReports: UInt32) -> win32more.Windows.Graphics.Holographic.HolographicFrameScanoutMonitor: ...
    @winrt_classmethod
    def get_IsConfigured(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics3) -> Boolean: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics2) -> Boolean: ...
    @winrt_classmethod
    def get_IsAvailable(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics2) -> Boolean: ...
    @winrt_classmethod
    def add_IsAvailableChanged(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsAvailableChanged(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateForCoreWindow(cls: win32more.Windows.Graphics.Holographic.IHolographicSpaceStatics, window: win32more.Windows.UI.Core.CoreWindow) -> win32more.Windows.Graphics.Holographic.HolographicSpace: ...
    PrimaryAdapterId = property(get_PrimaryAdapterId, None)
    UserPresence = property(get_UserPresence, None)
    _HolographicSpace_Meta_.IsAvailable = property(get_IsAvailable, None)
    _HolographicSpace_Meta_.IsConfigured = property(get_IsConfigured, None)
    _HolographicSpace_Meta_.IsSupported = property(get_IsSupported, None)
    CameraAdded = event()
    CameraRemoved = event()
    UserPresenceChanged = event()
class HolographicSpaceCameraAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs'
    @winrt_mixinmethod
    def get_Camera(self: win32more.Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Camera = property(get_Camera, None)
class HolographicSpaceCameraRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicSpaceCameraRemovedEventArgs
    _classid_ = 'Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs'
    @winrt_mixinmethod
    def get_Camera(self: win32more.Windows.Graphics.Holographic.IHolographicSpaceCameraRemovedEventArgs) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    Camera = property(get_Camera, None)
class HolographicSpaceUserPresence(Enum, Int32):
    Absent = 0
    PresentPassive = 1
    PresentActive = 2
class HolographicStereoTransform(Structure):
    Left: win32more.Windows.Foundation.Numerics.Matrix4x4
    Right: win32more.Windows.Foundation.Numerics.Matrix4x4
class HolographicViewConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration
    _classid_ = 'Windows.Graphics.Holographic.HolographicViewConfiguration'
    @winrt_mixinmethod
    def get_NativeRenderTargetSize(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_RenderTargetSize(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def RequestRenderTargetSize(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SupportedPixelFormats(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_PixelFormat(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_IsStereo(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Double: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Graphics.Holographic.HolographicViewConfigurationKind: ...
    @winrt_mixinmethod
    def get_Display(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedDepthReprojectionMethods(self: win32more.Windows.Graphics.Holographic.IHolographicViewConfiguration2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]: ...
    Display = property(get_Display, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    IsStereo = property(get_IsStereo, None)
    Kind = property(get_Kind, None)
    NativeRenderTargetSize = property(get_NativeRenderTargetSize, None)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    RefreshRate = property(get_RefreshRate, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    SupportedDepthReprojectionMethods = property(get_SupportedDepthReprojectionMethods, None)
    SupportedPixelFormats = property(get_SupportedPixelFormats, None)
class HolographicViewConfigurationKind(Enum, Int32):
    Display = 0
    PhotoVideoCamera = 1
class IHolographicCamera(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera'
    _iid_ = Guid('{e4e98445-9bed-4980-9ba0-e87680d1cb74}')
    @winrt_commethod(6)
    def get_RenderTargetSize(self) -> win32more.Windows.Foundation.Size: ...
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
    Id = property(get_Id, None)
    IsStereo = property(get_IsStereo, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    ViewportScaleFactor = property(get_ViewportScaleFactor, put_ViewportScaleFactor)
class IHolographicCamera2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera2'
    _iid_ = Guid('{b55b9f1a-ba8c-4f84-ad79-2e7e1e2450f3}')
    @winrt_commethod(6)
    def get_LeftViewportParameters(self) -> win32more.Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_commethod(7)
    def get_RightViewportParameters(self) -> win32more.Windows.Graphics.Holographic.HolographicCameraViewportParameters: ...
    @winrt_commethod(8)
    def get_Display(self) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
    Display = property(get_Display, None)
    LeftViewportParameters = property(get_LeftViewportParameters, None)
    RightViewportParameters = property(get_RightViewportParameters, None)
class IHolographicCamera3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera3'
    _iid_ = Guid('{45aa4fb3-7b59-524e-4a3f-4a6ad6650477}')
    @winrt_commethod(6)
    def get_IsPrimaryLayerEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPrimaryLayerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MaxQuadLayerCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_QuadLayers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Holographic.HolographicQuadLayer]: ...
    IsPrimaryLayerEnabled = property(get_IsPrimaryLayerEnabled, put_IsPrimaryLayerEnabled)
    MaxQuadLayerCount = property(get_MaxQuadLayerCount, None)
    QuadLayers = property(get_QuadLayers, None)
class IHolographicCamera4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera4'
    _iid_ = Guid('{9a2531d6-4723-4f39-a9a5-9d05181d9b44}')
    @winrt_commethod(6)
    def get_CanOverrideViewport(self) -> Boolean: ...
    CanOverrideViewport = property(get_CanOverrideViewport, None)
class IHolographicCamera5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera5'
    _iid_ = Guid('{229706f2-628d-4ef5-9c08-a63fdd7787c6}')
    @winrt_commethod(6)
    def get_IsHardwareContentProtectionSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsHardwareContentProtectionEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsHardwareContentProtectionEnabled(self, value: Boolean) -> Void: ...
    IsHardwareContentProtectionEnabled = property(get_IsHardwareContentProtectionEnabled, put_IsHardwareContentProtectionEnabled)
    IsHardwareContentProtectionSupported = property(get_IsHardwareContentProtectionSupported, None)
class IHolographicCamera6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCamera6'
    _iid_ = Guid('{0209194f-632d-5154-ab52-0b5d15b12505}')
    @winrt_commethod(6)
    def get_ViewConfiguration(self) -> win32more.Windows.Graphics.Holographic.HolographicViewConfiguration: ...
    ViewConfiguration = property(get_ViewConfiguration, None)
class IHolographicCameraPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraPose'
    _iid_ = Guid('{0d7d7e30-12de-45bd-912b-c7f6561599d1}')
    @winrt_commethod(6)
    def get_HolographicCamera(self) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_commethod(7)
    def get_Viewport(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(8)
    def TryGetViewTransform(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Graphics.Holographic.HolographicStereoTransform]: ...
    @winrt_commethod(9)
    def get_ProjectionTransform(self) -> win32more.Windows.Graphics.Holographic.HolographicStereoTransform: ...
    @winrt_commethod(10)
    def TryGetCullingFrustum(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_commethod(11)
    def TryGetVisibleFrustum(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Perception.Spatial.SpatialBoundingFrustum]: ...
    @winrt_commethod(12)
    def get_NearPlaneDistance(self) -> Double: ...
    @winrt_commethod(13)
    def get_FarPlaneDistance(self) -> Double: ...
    FarPlaneDistance = property(get_FarPlaneDistance, None)
    HolographicCamera = property(get_HolographicCamera, None)
    NearPlaneDistance = property(get_NearPlaneDistance, None)
    ProjectionTransform = property(get_ProjectionTransform, None)
    Viewport = property(get_Viewport, None)
class IHolographicCameraPose2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraPose2'
    _iid_ = Guid('{232be073-5d2d-4560-814e-2697c4fce16b}')
    @winrt_commethod(6)
    def OverrideViewTransform(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, coordinateSystemToViewTransform: win32more.Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_commethod(7)
    def OverrideProjectionTransform(self, projectionTransform: win32more.Windows.Graphics.Holographic.HolographicStereoTransform) -> Void: ...
    @winrt_commethod(8)
    def OverrideViewport(self, leftViewport: win32more.Windows.Foundation.Rect, rightViewport: win32more.Windows.Foundation.Rect) -> Void: ...
class IHolographicCameraRenderingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraRenderingParameters'
    _iid_ = Guid('{8eac2ed1-5bf4-4e16-8236-ae0800c11d0d}')
    @winrt_commethod(6)
    def SetFocusPoint(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def SetFocusPointWithNormal(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(8)
    def SetFocusPointWithNormalLinearVelocity(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, normal: win32more.Windows.Foundation.Numerics.Vector3, linearVelocity: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(9)
    def get_Direct3D11Device(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_commethod(10)
    def get_Direct3D11BackBuffer(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    Direct3D11BackBuffer = property(get_Direct3D11BackBuffer, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
class IHolographicCameraRenderingParameters2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraRenderingParameters2'
    _iid_ = Guid('{261270e3-b696-4634-94d6-be0681643599}')
    @winrt_commethod(6)
    def get_ReprojectionMode(self) -> win32more.Windows.Graphics.Holographic.HolographicReprojectionMode: ...
    @winrt_commethod(7)
    def put_ReprojectionMode(self, value: win32more.Windows.Graphics.Holographic.HolographicReprojectionMode) -> Void: ...
    @winrt_commethod(8)
    def CommitDirect3D11DepthBuffer(self, value: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> Void: ...
    ReprojectionMode = property(get_ReprojectionMode, put_ReprojectionMode)
class IHolographicCameraRenderingParameters3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraRenderingParameters3'
    _iid_ = Guid('{b1aa513f-136d-4b06-b9d4-e4b914cd0683}')
    @winrt_commethod(6)
    def get_IsContentProtectionEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsContentProtectionEnabled(self, value: Boolean) -> Void: ...
    IsContentProtectionEnabled = property(get_IsContentProtectionEnabled, put_IsContentProtectionEnabled)
class IHolographicCameraRenderingParameters4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraRenderingParameters4'
    _iid_ = Guid('{0878fa4c-e163-57dc-82b7-c406ab3e0537}')
    @winrt_commethod(6)
    def get_DepthReprojectionMethod(self) -> win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod: ...
    @winrt_commethod(7)
    def put_DepthReprojectionMethod(self, value: win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod) -> Void: ...
    DepthReprojectionMethod = property(get_DepthReprojectionMethod, put_DepthReprojectionMethod)
class IHolographicCameraViewportParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicCameraViewportParameters'
    _iid_ = Guid('{80cdf3f7-842a-41e1-93ed-5692ab1fbb10}')
    @winrt_commethod(6)
    def get_HiddenAreaMesh(self) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_commethod(7)
    def get_VisibleAreaMesh(self) -> ReceiveArray[win32more.Windows.Foundation.Numerics.Vector2]: ...
    HiddenAreaMesh = property(get_HiddenAreaMesh, None)
    VisibleAreaMesh = property(get_VisibleAreaMesh, None)
class IHolographicDisplay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicDisplay'
    _iid_ = Guid('{9acea414-1d9f-4090-a388-90c06f6eae9c}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxViewportSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsOpaque(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_AdapterId(self) -> win32more.Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_commethod(11)
    def get_SpatialLocator(self) -> win32more.Windows.Perception.Spatial.SpatialLocator: ...
    AdapterId = property(get_AdapterId, None)
    DisplayName = property(get_DisplayName, None)
    IsOpaque = property(get_IsOpaque, None)
    IsStereo = property(get_IsStereo, None)
    MaxViewportSize = property(get_MaxViewportSize, None)
    SpatialLocator = property(get_SpatialLocator, None)
class IHolographicDisplay2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicDisplay2'
    _iid_ = Guid('{75ac3f82-e755-436c-8d96-4d32d131473e}')
    @winrt_commethod(6)
    def get_RefreshRate(self) -> Double: ...
    RefreshRate = property(get_RefreshRate, None)
class IHolographicDisplay3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicDisplay3'
    _iid_ = Guid('{fc4c6ac6-6480-5008-b29e-157d77c843f7}')
    @winrt_commethod(6)
    def TryGetViewConfiguration(self, kind: win32more.Windows.Graphics.Holographic.HolographicViewConfigurationKind) -> win32more.Windows.Graphics.Holographic.HolographicViewConfiguration: ...
class IHolographicDisplayStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicDisplayStatics'
    _iid_ = Guid('{cb374983-e7b0-4841-8355-3ae5b536e9a4}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
class IHolographicFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrame'
    _iid_ = Guid('{c6988eb6-a8b9-3054-a6eb-d624b6536375}')
    @winrt_commethod(6)
    def get_AddedCameras(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_commethod(7)
    def get_RemovedCameras(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCamera]: ...
    @winrt_commethod(8)
    def GetRenderingParameters(self, cameraPose: win32more.Windows.Graphics.Holographic.HolographicCameraPose) -> win32more.Windows.Graphics.Holographic.HolographicCameraRenderingParameters: ...
    @winrt_commethod(9)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_CurrentPrediction(self) -> win32more.Windows.Graphics.Holographic.HolographicFramePrediction: ...
    @winrt_commethod(11)
    def UpdateCurrentPrediction(self) -> Void: ...
    @winrt_commethod(12)
    def PresentUsingCurrentPrediction(self) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_commethod(13)
    def PresentUsingCurrentPredictionWithBehavior(self, waitBehavior: win32more.Windows.Graphics.Holographic.HolographicFramePresentWaitBehavior) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentResult: ...
    @winrt_commethod(14)
    def WaitForFrameToFinish(self) -> Void: ...
    AddedCameras = property(get_AddedCameras, None)
    CurrentPrediction = property(get_CurrentPrediction, None)
    Duration = property(get_Duration, None)
    RemovedCameras = property(get_RemovedCameras, None)
class IHolographicFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrame2'
    _iid_ = Guid('{283f37bf-3bf2-5e91-6633-870574e6f217}')
    @winrt_commethod(6)
    def GetQuadLayerUpdateParameters(self, layer: win32more.Windows.Graphics.Holographic.HolographicQuadLayer) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayerUpdateParameters: ...
class IHolographicFrame3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrame3'
    _iid_ = Guid('{e5e964c9-8a27-55d3-9f98-94530d369052}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.Graphics.Holographic.HolographicFrameId: ...
    Id = property(get_Id, None)
class IHolographicFramePrediction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFramePrediction'
    _iid_ = Guid('{520f4de1-5c0a-4e79-a81e-6abe02bb2739}')
    @winrt_commethod(6)
    def get_CameraPoses(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicCameraPose]: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    CameraPoses = property(get_CameraPoses, None)
    Timestamp = property(get_Timestamp, None)
class IHolographicFramePresentationMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFramePresentationMonitor'
    _iid_ = Guid('{ca87256c-6fae-428e-bb83-25dfee51136b}')
    @winrt_commethod(6)
    def ReadReports(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicFramePresentationReport]: ...
class IHolographicFramePresentationReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFramePresentationReport'
    _iid_ = Guid('{80baf614-f2f4-4c8a-8de3-065c78f6d5de}')
    @winrt_commethod(6)
    def get_CompositorGpuDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_AppGpuDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_AppGpuOverrun(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MissedPresentationOpportunityCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PresentationCount(self) -> UInt32: ...
    AppGpuDuration = property(get_AppGpuDuration, None)
    AppGpuOverrun = property(get_AppGpuOverrun, None)
    CompositorGpuDuration = property(get_CompositorGpuDuration, None)
    MissedPresentationOpportunityCount = property(get_MissedPresentationOpportunityCount, None)
    PresentationCount = property(get_PresentationCount, None)
class IHolographicFrameRenderingReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrameRenderingReport'
    _iid_ = Guid('{05f32de4-e384-51b3-b934-f0d3a0f78606}')
    @winrt_commethod(6)
    def get_FrameId(self) -> win32more.Windows.Graphics.Holographic.HolographicFrameId: ...
    @winrt_commethod(7)
    def get_MissedLatchCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SystemRelativeFrameReadyTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_SystemRelativeActualGpuFinishTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SystemRelativeTargetLatchTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameId = property(get_FrameId, None)
    MissedLatchCount = property(get_MissedLatchCount, None)
    SystemRelativeActualGpuFinishTime = property(get_SystemRelativeActualGpuFinishTime, None)
    SystemRelativeFrameReadyTime = property(get_SystemRelativeFrameReadyTime, None)
    SystemRelativeTargetLatchTime = property(get_SystemRelativeTargetLatchTime, None)
class IHolographicFrameScanoutMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrameScanoutMonitor'
    _iid_ = Guid('{7e83efa9-843c-5401-8095-9bc1b8b08638}')
    @winrt_commethod(6)
    def ReadReports(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Holographic.HolographicFrameScanoutReport]: ...
class IHolographicFrameScanoutReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicFrameScanoutReport'
    _iid_ = Guid('{0ebbe606-03a0-5ca0-b46e-bba068d7233f}')
    @winrt_commethod(6)
    def get_RenderingReport(self) -> win32more.Windows.Graphics.Holographic.HolographicFrameRenderingReport: ...
    @winrt_commethod(7)
    def get_MissedScanoutCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SystemRelativeLatchTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_SystemRelativeScanoutStartTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_SystemRelativePhotonTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    MissedScanoutCount = property(get_MissedScanoutCount, None)
    RenderingReport = property(get_RenderingReport, None)
    SystemRelativeLatchTime = property(get_SystemRelativeLatchTime, None)
    SystemRelativePhotonTime = property(get_SystemRelativePhotonTime, None)
    SystemRelativeScanoutStartTime = property(get_SystemRelativeScanoutStartTime, None)
class IHolographicQuadLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicQuadLayer'
    _iid_ = Guid('{903460c9-c9d9-5d5c-41ac-a2d5ab0fd331}')
    @winrt_commethod(6)
    def get_PixelFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(7)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class IHolographicQuadLayerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicQuadLayerFactory'
    _iid_ = Guid('{a67538f3-5a14-5a10-489a-455065b37b76}')
    @winrt_commethod(6)
    def Create(self, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayer: ...
    @winrt_commethod(7)
    def CreateWithPixelFormat(self, size: win32more.Windows.Foundation.Size, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> win32more.Windows.Graphics.Holographic.HolographicQuadLayer: ...
class IHolographicQuadLayerUpdateParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters'
    _iid_ = Guid('{2b0ea3b0-798d-5bca-55c2-2c0c762ebb08}')
    @winrt_commethod(6)
    def AcquireBufferToUpdateContent(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    @winrt_commethod(7)
    def UpdateViewport(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(8)
    def UpdateContentProtectionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def UpdateExtents(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def UpdateLocationWithStationaryMode(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(11)
    def UpdateLocationWithDisplayRelativeMode(self, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
class IHolographicQuadLayerUpdateParameters2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicQuadLayerUpdateParameters2'
    _iid_ = Guid('{4f33d32d-82c1-46c1-8980-3cb70d98182b}')
    @winrt_commethod(6)
    def get_CanAcquireWithHardwareProtection(self) -> Boolean: ...
    @winrt_commethod(7)
    def AcquireBufferToUpdateContentWithHardwareProtection(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface: ...
    CanAcquireWithHardwareProtection = property(get_CanAcquireWithHardwareProtection, None)
class IHolographicSpace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpace'
    _iid_ = Guid('{4380dba6-5e78-434f-807c-3433d1efe8b7}')
    @winrt_commethod(6)
    def get_PrimaryAdapterId(self) -> win32more.Windows.Graphics.Holographic.HolographicAdapterId: ...
    @winrt_commethod(7)
    def SetDirect3D11Device(self, value: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_commethod(8)
    def add_CameraAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Graphics.Holographic.HolographicSpaceCameraAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CameraAdded(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CameraRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Graphics.Holographic.HolographicSpaceCameraRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraRemoved(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def CreateNextFrame(self) -> win32more.Windows.Graphics.Holographic.HolographicFrame: ...
    PrimaryAdapterId = property(get_PrimaryAdapterId, None)
    CameraAdded = event()
    CameraRemoved = event()
class IHolographicSpace2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpace2'
    _iid_ = Guid('{4f81a9a8-b7ff-4883-9827-7d677287ea70}')
    @winrt_commethod(6)
    def get_UserPresence(self) -> win32more.Windows.Graphics.Holographic.HolographicSpaceUserPresence: ...
    @winrt_commethod(7)
    def add_UserPresenceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Holographic.HolographicSpace, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_UserPresenceChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def WaitForNextFrameReady(self) -> Void: ...
    @winrt_commethod(10)
    def WaitForNextFrameReadyWithHeadStart(self, requestedHeadStartDuration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def CreateFramePresentationMonitor(self, maxQueuedReports: UInt32) -> win32more.Windows.Graphics.Holographic.HolographicFramePresentationMonitor: ...
    UserPresence = property(get_UserPresence, None)
    UserPresenceChanged = event()
class IHolographicSpace3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpace3'
    _iid_ = Guid('{df1733d1-f224-587e-8d71-1e8fc8f07b1f}')
    @winrt_commethod(6)
    def CreateFrameScanoutMonitor(self, maxQueuedReports: UInt32) -> win32more.Windows.Graphics.Holographic.HolographicFrameScanoutMonitor: ...
class IHolographicSpaceCameraAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpaceCameraAddedEventArgs'
    _iid_ = Guid('{58f1da35-bbb3-3c8f-993d-6c80e7feb99f}')
    @winrt_commethod(6)
    def get_Camera(self) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Camera = property(get_Camera, None)
class IHolographicSpaceCameraRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpaceCameraRemovedEventArgs'
    _iid_ = Guid('{805444a8-f2ae-322e-8da9-836a0a95a4c1}')
    @winrt_commethod(6)
    def get_Camera(self) -> win32more.Windows.Graphics.Holographic.HolographicCamera: ...
    Camera = property(get_Camera, None)
class IHolographicSpaceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpaceStatics'
    _iid_ = Guid('{364e6064-c8f2-3ba1-8391-66b8489e67fd}')
    @winrt_commethod(6)
    def CreateForCoreWindow(self, window: win32more.Windows.UI.Core.CoreWindow) -> win32more.Windows.Graphics.Holographic.HolographicSpace: ...
class IHolographicSpaceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpaceStatics2'
    _iid_ = Guid('{0e777088-75fc-48af-8758-0652f6f07c59}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsAvailable(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_IsAvailableChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsAvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsAvailable = property(get_IsAvailable, None)
    IsSupported = property(get_IsSupported, None)
    IsAvailableChanged = event()
class IHolographicSpaceStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicSpaceStatics3'
    _iid_ = Guid('{3b00de3d-b1a3-4dfe-8e79-fec5909e6df8}')
    @winrt_commethod(6)
    def get_IsConfigured(self) -> Boolean: ...
    IsConfigured = property(get_IsConfigured, None)
class IHolographicViewConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicViewConfiguration'
    _iid_ = Guid('{5c1de6e6-67e9-5004-b02c-67a3a122b576}')
    @winrt_commethod(6)
    def get_NativeRenderTargetSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_RenderTargetSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def RequestRenderTargetSize(self, size: win32more.Windows.Foundation.Size) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def get_SupportedPixelFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.DirectXPixelFormat]: ...
    @winrt_commethod(10)
    def get_PixelFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(11)
    def put_PixelFormat(self, value: win32more.Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(12)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_RefreshRate(self) -> Double: ...
    @winrt_commethod(14)
    def get_Kind(self) -> win32more.Windows.Graphics.Holographic.HolographicViewConfigurationKind: ...
    @winrt_commethod(15)
    def get_Display(self) -> win32more.Windows.Graphics.Holographic.HolographicDisplay: ...
    @winrt_commethod(16)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    Display = property(get_Display, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    IsStereo = property(get_IsStereo, None)
    Kind = property(get_Kind, None)
    NativeRenderTargetSize = property(get_NativeRenderTargetSize, None)
    PixelFormat = property(get_PixelFormat, put_PixelFormat)
    RefreshRate = property(get_RefreshRate, None)
    RenderTargetSize = property(get_RenderTargetSize, None)
    SupportedPixelFormats = property(get_SupportedPixelFormats, None)
class IHolographicViewConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Holographic.IHolographicViewConfiguration2'
    _iid_ = Guid('{e241756e-e0d0-5019-9af5-1b165bc2f54e}')
    @winrt_commethod(6)
    def get_SupportedDepthReprojectionMethods(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Holographic.HolographicDepthReprojectionMethod]: ...
    SupportedDepthReprojectionMethods = property(get_SupportedDepthReprojectionMethods, None)


make_ready(__name__)
