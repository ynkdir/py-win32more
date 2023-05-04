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
import Windows.Devices.Enumeration
import Windows.Devices.Perception
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.Imaging
import Windows.Media
import Windows.Media.Devices.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IKnownCameraIntrinsicsPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics'
    _iid_ = Guid('{08c03978-437a-4d97-a663-fd3195600249}')
    @winrt_commethod(6)
    def get_FocalLength(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PrincipalPoint(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RadialDistortion(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TangentialDistortion(self) -> WinRT_String: ...
    FocalLength = property(get_FocalLength, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
class IKnownPerceptionColorFrameSourcePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de4b}')
    @winrt_commethod(6)
    def get_Exposure(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AutoExposureEnabled(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExposureCompensation(self) -> WinRT_String: ...
    Exposure = property(get_Exposure, None)
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
class IKnownPerceptionDepthFrameSourcePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de4a}')
    @winrt_commethod(6)
    def get_MinDepth(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxDepth(self) -> WinRT_String: ...
    MinDepth = property(get_MinDepth, None)
    MaxDepth = property(get_MaxDepth, None)
class IKnownPerceptionFrameSourcePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de47}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PhysicalDeviceIds(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FrameKind(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DeviceModelVersion(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_EnclosureLocation(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    PhysicalDeviceIds = property(get_PhysicalDeviceIds, None)
    FrameKind = property(get_FrameKind, None)
    DeviceModelVersion = property(get_DeviceModelVersion, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
class IKnownPerceptionFrameSourcePropertiesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics2'
    _iid_ = Guid('{a9c86871-05dc-4a4d-8a5c-a4ecf26bbc46}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IKnownPerceptionInfraredFrameSourcePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de49}')
    @winrt_commethod(6)
    def get_Exposure(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AutoExposureEnabled(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExposureCompensation(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ActiveIlluminationEnabled(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_AmbientSubtractionEnabled(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_StructureLightPatternEnabled(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_InterleavedIlluminationEnabled(self) -> WinRT_String: ...
    Exposure = property(get_Exposure, None)
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    ActiveIlluminationEnabled = property(get_ActiveIlluminationEnabled, None)
    AmbientSubtractionEnabled = property(get_AmbientSubtractionEnabled, None)
    StructureLightPatternEnabled = property(get_StructureLightPatternEnabled, None)
    InterleavedIlluminationEnabled = property(get_InterleavedIlluminationEnabled, None)
class IKnownPerceptionVideoFrameSourcePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de48}')
    @winrt_commethod(6)
    def get_VideoProfile(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedVideoProfiles(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AvailableVideoProfiles(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_IsMirrored(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CameraIntrinsics(self) -> WinRT_String: ...
    VideoProfile = property(get_VideoProfile, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    IsMirrored = property(get_IsMirrored, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
class IKnownPerceptionVideoProfilePropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics'
    _iid_ = Guid('{8f08e2e7-5a76-43e3-a13a-da3d91a9ef98}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Width(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Height(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FrameDuration(self) -> WinRT_String: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameDuration = property(get_FrameDuration, None)
class IPerceptionColorFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrame'
    _iid_ = Guid('{fe621549-2cbf-4f94-9861-f817ea317747}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionColorFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs'
    _iid_ = Guid('{8fad02d5-86f7-4d8d-b966-5a3761ba9f59}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> Windows.Devices.Perception.PerceptionColorFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionColorFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameReader'
    _iid_ = Guid('{7650f56e-b9f5-461b-83ad-f222af2aaadc}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameReader, Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> Windows.Devices.Perception.PerceptionColorFrame: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class IPerceptionColorFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSource'
    _iid_ = Guid('{dc6dba7c-0b58-468d-9ca1-6db04cc0477c}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_DeviceKind(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Available(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_Active(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsControlled(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, correlatedDepthFrameSource: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetSourceId: WinRT_String, correlatedDepthFrameSource: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> Windows.Devices.Perception.PerceptionColorFrameReader: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
class IPerceptionColorFrameSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSource2'
    _iid_ = Guid('{f88008e5-5631-45ed-ad98-8c6aa04cfb91}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionColorFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs'
    _iid_ = Guid('{d16bf4e6-da24-442c-bbd5-55549b5b94f3}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionColorFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs'
    _iid_ = Guid('{d277fa69-eb4c-42ef-ba4f-288f615c93c1}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionColorFrameSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de49}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.Devices.Perception.PerceptionColorFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionColorFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionColorFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionColorFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher'
    _iid_ = Guid('{96bd1392-e667-40c4-89f9-1462dea6a9cc}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IPerceptionControlSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionControlSession'
    _iid_ = Guid('{99998653-5a3d-417f-9239-f1889e548b48}')
    @winrt_commethod(6)
    def add_ControlLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionControlSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ControlLost(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TrySetPropertyAsync(self, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
class IPerceptionDepthCorrelatedCameraIntrinsics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics'
    _iid_ = Guid('{6548ca01-86de-5be1-6582-807fcf4c95cf}')
    @winrt_commethod(6)
    def UnprojectPixelAtCorrelatedDepth(self, pixelCoordinate: Windows.Foundation.Point, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def UnprojectPixelsAtCorrelatedDepth(self, sourceCoordinates: POINTER(Windows.Foundation.Point_head), depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Void: ...
    @winrt_commethod(8)
    def UnprojectRegionPixelsAtCorrelatedDepthAsync(self, region: Windows.Foundation.Rect, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UnprojectAllPixelsAtCorrelatedDepthAsync(self, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.Foundation.IAsyncAction: ...
class IPerceptionDepthCorrelatedCoordinateMapper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper'
    _iid_ = Guid('{5b4d9d1d-b5f6-469c-b8c2-b97a45e6863b}')
    @winrt_commethod(6)
    def MapPixelToTarget(self, sourcePixelCoordinate: Windows.Foundation.Point, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def MapPixelsToTarget(self, sourceCoordinates: POINTER(Windows.Foundation.Point_head), depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_commethod(8)
    def MapRegionOfPixelsToTargetAsync(self, region: Windows.Foundation.Rect, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: POINTER(Windows.Foundation.Point_head)) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def MapAllPixelsToTargetAsync(self, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: POINTER(Windows.Foundation.Point_head)) -> Windows.Foundation.IAsyncAction: ...
class IPerceptionDepthFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrame'
    _iid_ = Guid('{a37b81fc-9906-4ffd-9161-0024b360b657}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionDepthFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs'
    _iid_ = Guid('{443d25b2-b282-4637-9173-ac978435c985}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> Windows.Devices.Perception.PerceptionDepthFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionDepthFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameReader'
    _iid_ = Guid('{b1a3c09f-299b-4612-a4f7-270f25a096ec}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameReader, Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> Windows.Devices.Perception.PerceptionDepthFrame: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class IPerceptionDepthFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSource'
    _iid_ = Guid('{79d433d6-47fb-4df1-bfc9-f01d40bd9942}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_DeviceKind(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Available(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_Active(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsControlled(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, target: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetId: WinRT_String, depthFrameSourceToMapWith: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> Windows.Devices.Perception.PerceptionDepthFrameReader: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
class IPerceptionDepthFrameSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSource2'
    _iid_ = Guid('{e3d23d2e-6e2c-4e6d-91d9-704cd8dff79d}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionDepthFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs'
    _iid_ = Guid('{93a48168-8bf8-45d2-a2f8-4ac0931cc7a6}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionDepthFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs'
    _iid_ = Guid('{a0c0cc4d-e96c-4d81-86dd-38b95e49c6df}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionDepthFrameSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de48}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionDepthFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionDepthFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher'
    _iid_ = Guid('{780e96d1-8d02-4d2b-ada4-5ba624a0eb10}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IPerceptionFrameSourcePropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs'
    _iid_ = Guid('{6c68e068-bcf1-4ecc-b891-7625d1244b6b}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Key(self) -> WinRT_String: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class IPerceptionFrameSourcePropertyChangeResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult'
    _iid_ = Guid('{1e33390a-3c90-4d22-b898-f42bba6418ff}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    NewValue = property(get_NewValue, None)
class IPerceptionInfraredFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrame'
    _iid_ = Guid('{b0886276-849e-4c7a-8ae6-b56064532153}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionInfraredFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs'
    _iid_ = Guid('{9f77fac7-b4bd-4857-9d50-be8ef075daef}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> Windows.Devices.Perception.PerceptionInfraredFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionInfraredFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameReader'
    _iid_ = Guid('{7960ce18-d39b-4fc8-a04a-929734c6756c}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameReader, Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> Windows.Devices.Perception.PerceptionInfraredFrame: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class IPerceptionInfraredFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSource'
    _iid_ = Guid('{55b08742-1808-494e-9e30-9d2a7be8f700}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_DeviceKind(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Available(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_Active(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsControlled(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, target: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetId: WinRT_String, depthFrameSourceToMapWith: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> Windows.Devices.Perception.PerceptionInfraredFrameReader: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
class IPerceptionInfraredFrameSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSource2'
    _iid_ = Guid('{dcd4d798-4b0b-4300-8d85-410817faa032}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionInfraredFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs'
    _iid_ = Guid('{6d334120-95ce-4660-907a-d98035aa2b7c}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionInfraredFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs'
    _iid_ = Guid('{ea1a8071-7a70-4a61-af94-07303853f695}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionInfraredFrameSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de47}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionInfraredFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionInfraredFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionInfraredFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher'
    _iid_ = Guid('{383cff99-d70c-444d-a8b0-720c2e66fe3b}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
class IPerceptionVideoProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionVideoProfile'
    _iid_ = Guid('{75763ea3-011a-470e-8225-6f05ade25648}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(8)
    def get_Width(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Height(self) -> Int32: ...
    @winrt_commethod(10)
    def get_FrameDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def IsEqual(self, other: Windows.Devices.Perception.PerceptionVideoProfile) -> Boolean: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameDuration = property(get_FrameDuration, None)
class KnownCameraIntrinsicsProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownCameraIntrinsicsProperties'
    @winrt_classmethod
    def get_FocalLength(cls: Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrincipalPoint(cls: Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RadialDistortion(cls: Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TangentialDistortion(cls: Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    FocalLength = property(get_FocalLength, None)
    PrincipalPoint = property(get_PrincipalPoint, None)
    RadialDistortion = property(get_RadialDistortion, None)
    TangentialDistortion = property(get_TangentialDistortion, None)
class KnownPerceptionColorFrameSourceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionColorFrameSourceProperties'
    @winrt_classmethod
    def get_Exposure(cls: Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AutoExposureEnabled(cls: Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ExposureCompensation(cls: Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    Exposure = property(get_Exposure, None)
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
class KnownPerceptionDepthFrameSourceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionDepthFrameSourceProperties'
    @winrt_classmethod
    def get_MinDepth(cls: Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MaxDepth(cls: Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics) -> WinRT_String: ...
    MinDepth = property(get_MinDepth, None)
    MaxDepth = property(get_MaxDepth, None)
class KnownPerceptionFrameSourceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionFrameSourceProperties'
    @winrt_classmethod
    def get_DeviceId(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Id(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PhysicalDeviceIds(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrameKind(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DeviceModelVersion(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EnclosureLocation(cls: Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Id = property(get_Id, None)
    PhysicalDeviceIds = property(get_PhysicalDeviceIds, None)
    FrameKind = property(get_FrameKind, None)
    DeviceModelVersion = property(get_DeviceModelVersion, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
class KnownPerceptionInfraredFrameSourceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionInfraredFrameSourceProperties'
    @winrt_classmethod
    def get_Exposure(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AutoExposureEnabled(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ExposureCompensation(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ActiveIlluminationEnabled(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AmbientSubtractionEnabled(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StructureLightPatternEnabled(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_InterleavedIlluminationEnabled(cls: Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    Exposure = property(get_Exposure, None)
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    ActiveIlluminationEnabled = property(get_ActiveIlluminationEnabled, None)
    AmbientSubtractionEnabled = property(get_AmbientSubtractionEnabled, None)
    StructureLightPatternEnabled = property(get_StructureLightPatternEnabled, None)
    InterleavedIlluminationEnabled = property(get_InterleavedIlluminationEnabled, None)
class KnownPerceptionVideoFrameSourceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionVideoFrameSourceProperties'
    @winrt_classmethod
    def get_VideoProfile(cls: Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SupportedVideoProfiles(cls: Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AvailableVideoProfiles(cls: Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsMirrored(cls: Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CameraIntrinsics(cls: Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    VideoProfile = property(get_VideoProfile, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    IsMirrored = property(get_IsMirrored, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
class KnownPerceptionVideoProfileProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionVideoProfileProperties'
    @winrt_classmethod
    def get_BitmapPixelFormat(cls: Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BitmapAlphaMode(cls: Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Width(cls: Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Height(cls: Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrameDuration(cls: Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameDuration = property(get_FrameDuration, None)
class PerceptionColorFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: Windows.Devices.Perception.IPerceptionColorFrame) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionColorFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs) -> Windows.Devices.Perception.PerceptionColorFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionColorFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Devices.Perception.IPerceptionColorFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameReader, Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Devices.Perception.IPerceptionColorFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Devices.Perception.IPerceptionColorFrameReader) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: Windows.Devices.Perception.IPerceptionColorFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: Windows.Devices.Perception.IPerceptionColorFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: Windows.Devices.Perception.IPerceptionColorFrameReader) -> Windows.Devices.Perception.PerceptionColorFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class PerceptionColorFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionColorFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: Windows.Devices.Perception.IPerceptionColorFrameSource, correlatedDepthFrameSource: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: Windows.Devices.Perception.IPerceptionColorFrameSource, targetSourceId: WinRT_String, correlatedDepthFrameSource: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: Windows.Devices.Perception.IPerceptionColorFrameSource, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: Windows.Devices.Perception.IPerceptionColorFrameSource) -> Windows.Devices.Perception.PerceptionColorFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Perception.IPerceptionColorFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> Windows.Devices.Perception.PerceptionColorFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionColorFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Perception.IPerceptionColorFrameSourceStatics, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionColorFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
class PerceptionColorFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionColorFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs) -> Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionColorFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
class PerceptionControlSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionControlSession
    _classid_ = 'Windows.Devices.Perception.PerceptionControlSession'
    @winrt_mixinmethod
    def add_ControlLost(self: Windows.Devices.Perception.IPerceptionControlSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionControlSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlLost(self: Windows.Devices.Perception.IPerceptionControlSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TrySetPropertyAsync(self: Windows.Devices.Perception.IPerceptionControlSession, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class PerceptionDepthCorrelatedCameraIntrinsics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics'
    @winrt_mixinmethod
    def UnprojectPixelAtCorrelatedDepth(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, pixelCoordinate: Windows.Foundation.Point, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def UnprojectPixelsAtCorrelatedDepth(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, sourceCoordinates: POINTER(Windows.Foundation.Point_head), depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Void: ...
    @winrt_mixinmethod
    def UnprojectRegionPixelsAtCorrelatedDepthAsync(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, region: Windows.Foundation.Rect, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnprojectAllPixelsAtCorrelatedDepthAsync(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Numerics.Vector3_head)) -> Windows.Foundation.IAsyncAction: ...
class PerceptionDepthCorrelatedCoordinateMapper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper'
    @winrt_mixinmethod
    def MapPixelToTarget(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, sourcePixelCoordinate: Windows.Foundation.Point, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def MapPixelsToTarget(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, sourceCoordinates: POINTER(Windows.Foundation.Point_head), depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, results: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def MapRegionOfPixelsToTargetAsync(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, region: Windows.Foundation.Rect, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: POINTER(Windows.Foundation.Point_head)) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MapAllPixelsToTargetAsync(self: Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, depthFrame: Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: POINTER(Windows.Foundation.Point_head)) -> Windows.Foundation.IAsyncAction: ...
class PerceptionDepthFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: Windows.Devices.Perception.IPerceptionDepthFrame) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionDepthFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs) -> Windows.Devices.Perception.PerceptionDepthFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionDepthFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Devices.Perception.IPerceptionDepthFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameReader, Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Devices.Perception.IPerceptionDepthFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Devices.Perception.IPerceptionDepthFrameReader) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: Windows.Devices.Perception.IPerceptionDepthFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: Windows.Devices.Perception.IPerceptionDepthFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: Windows.Devices.Perception.IPerceptionDepthFrameReader) -> Windows.Devices.Perception.PerceptionDepthFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class PerceptionDepthFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, target: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String, depthFrameSourceToMapWith: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: Windows.Devices.Perception.IPerceptionDepthFrameSource, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Windows.Devices.Perception.PerceptionDepthFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Perception.IPerceptionDepthFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionDepthFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
class PerceptionDepthFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionDepthFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs) -> Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionDepthFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
PerceptionFrameSourceAccessStatus = Int32
PerceptionFrameSourceAccessStatus_Unspecified: PerceptionFrameSourceAccessStatus = 0
PerceptionFrameSourceAccessStatus_Allowed: PerceptionFrameSourceAccessStatus = 1
PerceptionFrameSourceAccessStatus_DeniedByUser: PerceptionFrameSourceAccessStatus = 2
PerceptionFrameSourceAccessStatus_DeniedBySystem: PerceptionFrameSourceAccessStatus = 3
class PerceptionFrameSourcePropertiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs'
    @winrt_mixinmethod
    def get_CollectionChange(self: Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs) -> Windows.Foundation.Collections.CollectionChange: ...
    @winrt_mixinmethod
    def get_Key(self: Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs) -> WinRT_String: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class PerceptionFrameSourcePropertyChangeResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult
    _classid_ = 'Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult) -> Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_mixinmethod
    def get_NewValue(self: Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    NewValue = property(get_NewValue, None)
PerceptionFrameSourcePropertyChangeStatus = Int32
PerceptionFrameSourcePropertyChangeStatus_Unknown: PerceptionFrameSourcePropertyChangeStatus = 0
PerceptionFrameSourcePropertyChangeStatus_Accepted: PerceptionFrameSourcePropertyChangeStatus = 1
PerceptionFrameSourcePropertyChangeStatus_LostControl: PerceptionFrameSourcePropertyChangeStatus = 2
PerceptionFrameSourcePropertyChangeStatus_PropertyNotSupported: PerceptionFrameSourcePropertyChangeStatus = 3
PerceptionFrameSourcePropertyChangeStatus_PropertyReadOnly: PerceptionFrameSourcePropertyChangeStatus = 4
PerceptionFrameSourcePropertyChangeStatus_ValueOutOfRange: PerceptionFrameSourcePropertyChangeStatus = 5
class PerceptionInfraredFrame(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: Windows.Devices.Perception.IPerceptionInfraredFrame) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionInfraredFrameArrivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs) -> Windows.Devices.Perception.PerceptionInfraredFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionInfraredFrameReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameReader, Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> Windows.Devices.Perception.PerceptionInfraredFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Source = property(get_Source, None)
    IsPaused = property(get_IsPaused, put_IsPaused)
class PerceptionInfraredFrameSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String, result: POINTER(Windows.Foundation.Numerics.Matrix4x4_head)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, target: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String, depthFrameSourceToMapWith: Windows.Devices.Perception.PerceptionDepthFrameSource) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource, controlSession: Windows.Devices.Perception.PerceptionControlSession, profile: Windows.Devices.Perception.PerceptionVideoProfile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Windows.Devices.Perception.PerceptionInfraredFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Perception.IPerceptionInfraredFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.PerceptionInfraredFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics, id: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionInfraredFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    DeviceKind = property(get_DeviceKind, None)
    Available = property(get_Available, None)
    Active = property(get_Active, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
class PerceptionInfraredFrameSourceAddedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionInfraredFrameSourceRemovedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs) -> Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionInfraredFrameSourceWatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
class PerceptionVideoProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Perception.IPerceptionVideoProfile
    _classid_ = 'Windows.Devices.Perception.PerceptionVideoProfile'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.Devices.Perception.IPerceptionVideoProfile) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: Windows.Devices.Perception.IPerceptionVideoProfile) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Devices.Perception.IPerceptionVideoProfile) -> Int32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Devices.Perception.IPerceptionVideoProfile) -> Int32: ...
    @winrt_mixinmethod
    def get_FrameDuration(self: Windows.Devices.Perception.IPerceptionVideoProfile) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Devices.Perception.IPerceptionVideoProfile, other: Windows.Devices.Perception.PerceptionVideoProfile) -> Boolean: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    FrameDuration = property(get_FrameDuration, None)
make_head(_module, 'IKnownCameraIntrinsicsPropertiesStatics')
make_head(_module, 'IKnownPerceptionColorFrameSourcePropertiesStatics')
make_head(_module, 'IKnownPerceptionDepthFrameSourcePropertiesStatics')
make_head(_module, 'IKnownPerceptionFrameSourcePropertiesStatics')
make_head(_module, 'IKnownPerceptionFrameSourcePropertiesStatics2')
make_head(_module, 'IKnownPerceptionInfraredFrameSourcePropertiesStatics')
make_head(_module, 'IKnownPerceptionVideoFrameSourcePropertiesStatics')
make_head(_module, 'IKnownPerceptionVideoProfilePropertiesStatics')
make_head(_module, 'IPerceptionColorFrame')
make_head(_module, 'IPerceptionColorFrameArrivedEventArgs')
make_head(_module, 'IPerceptionColorFrameReader')
make_head(_module, 'IPerceptionColorFrameSource')
make_head(_module, 'IPerceptionColorFrameSource2')
make_head(_module, 'IPerceptionColorFrameSourceAddedEventArgs')
make_head(_module, 'IPerceptionColorFrameSourceRemovedEventArgs')
make_head(_module, 'IPerceptionColorFrameSourceStatics')
make_head(_module, 'IPerceptionColorFrameSourceWatcher')
make_head(_module, 'IPerceptionControlSession')
make_head(_module, 'IPerceptionDepthCorrelatedCameraIntrinsics')
make_head(_module, 'IPerceptionDepthCorrelatedCoordinateMapper')
make_head(_module, 'IPerceptionDepthFrame')
make_head(_module, 'IPerceptionDepthFrameArrivedEventArgs')
make_head(_module, 'IPerceptionDepthFrameReader')
make_head(_module, 'IPerceptionDepthFrameSource')
make_head(_module, 'IPerceptionDepthFrameSource2')
make_head(_module, 'IPerceptionDepthFrameSourceAddedEventArgs')
make_head(_module, 'IPerceptionDepthFrameSourceRemovedEventArgs')
make_head(_module, 'IPerceptionDepthFrameSourceStatics')
make_head(_module, 'IPerceptionDepthFrameSourceWatcher')
make_head(_module, 'IPerceptionFrameSourcePropertiesChangedEventArgs')
make_head(_module, 'IPerceptionFrameSourcePropertyChangeResult')
make_head(_module, 'IPerceptionInfraredFrame')
make_head(_module, 'IPerceptionInfraredFrameArrivedEventArgs')
make_head(_module, 'IPerceptionInfraredFrameReader')
make_head(_module, 'IPerceptionInfraredFrameSource')
make_head(_module, 'IPerceptionInfraredFrameSource2')
make_head(_module, 'IPerceptionInfraredFrameSourceAddedEventArgs')
make_head(_module, 'IPerceptionInfraredFrameSourceRemovedEventArgs')
make_head(_module, 'IPerceptionInfraredFrameSourceStatics')
make_head(_module, 'IPerceptionInfraredFrameSourceWatcher')
make_head(_module, 'IPerceptionVideoProfile')
make_head(_module, 'KnownCameraIntrinsicsProperties')
make_head(_module, 'KnownPerceptionColorFrameSourceProperties')
make_head(_module, 'KnownPerceptionDepthFrameSourceProperties')
make_head(_module, 'KnownPerceptionFrameSourceProperties')
make_head(_module, 'KnownPerceptionInfraredFrameSourceProperties')
make_head(_module, 'KnownPerceptionVideoFrameSourceProperties')
make_head(_module, 'KnownPerceptionVideoProfileProperties')
make_head(_module, 'PerceptionColorFrame')
make_head(_module, 'PerceptionColorFrameArrivedEventArgs')
make_head(_module, 'PerceptionColorFrameReader')
make_head(_module, 'PerceptionColorFrameSource')
make_head(_module, 'PerceptionColorFrameSourceAddedEventArgs')
make_head(_module, 'PerceptionColorFrameSourceRemovedEventArgs')
make_head(_module, 'PerceptionColorFrameSourceWatcher')
make_head(_module, 'PerceptionControlSession')
make_head(_module, 'PerceptionDepthCorrelatedCameraIntrinsics')
make_head(_module, 'PerceptionDepthCorrelatedCoordinateMapper')
make_head(_module, 'PerceptionDepthFrame')
make_head(_module, 'PerceptionDepthFrameArrivedEventArgs')
make_head(_module, 'PerceptionDepthFrameReader')
make_head(_module, 'PerceptionDepthFrameSource')
make_head(_module, 'PerceptionDepthFrameSourceAddedEventArgs')
make_head(_module, 'PerceptionDepthFrameSourceRemovedEventArgs')
make_head(_module, 'PerceptionDepthFrameSourceWatcher')
make_head(_module, 'PerceptionFrameSourcePropertiesChangedEventArgs')
make_head(_module, 'PerceptionFrameSourcePropertyChangeResult')
make_head(_module, 'PerceptionInfraredFrame')
make_head(_module, 'PerceptionInfraredFrameArrivedEventArgs')
make_head(_module, 'PerceptionInfraredFrameReader')
make_head(_module, 'PerceptionInfraredFrameSource')
make_head(_module, 'PerceptionInfraredFrameSourceAddedEventArgs')
make_head(_module, 'PerceptionInfraredFrameSourceRemovedEventArgs')
make_head(_module, 'PerceptionInfraredFrameSourceWatcher')
make_head(_module, 'PerceptionVideoProfile')
