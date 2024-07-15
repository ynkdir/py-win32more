from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Perception
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Media.Devices.Core
import win32more.Windows.Win32.System.WinRT
class IKnownCameraIntrinsicsPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de4b}')
    @winrt_commethod(6)
    def get_Exposure(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AutoExposureEnabled(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExposureCompensation(self) -> WinRT_String: ...
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
class IKnownPerceptionDepthFrameSourcePropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics'
    _iid_ = Guid('{5df1cca2-01f8-4a87-b859-d5e5b7e1de4a}')
    @winrt_commethod(6)
    def get_MinDepth(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxDepth(self) -> WinRT_String: ...
    MaxDepth = property(get_MaxDepth, None)
    MinDepth = property(get_MinDepth, None)
class IKnownPerceptionFrameSourcePropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    DeviceModelVersion = property(get_DeviceModelVersion, None)
    EnclosureLocation = property(get_EnclosureLocation, None)
    FrameKind = property(get_FrameKind, None)
    Id = property(get_Id, None)
    PhysicalDeviceIds = property(get_PhysicalDeviceIds, None)
class IKnownPerceptionFrameSourcePropertiesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics2'
    _iid_ = Guid('{a9c86871-05dc-4a4d-8a5c-a4ecf26bbc46}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IKnownPerceptionInfraredFrameSourcePropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    ActiveIlluminationEnabled = property(get_ActiveIlluminationEnabled, None)
    AmbientSubtractionEnabled = property(get_AmbientSubtractionEnabled, None)
    AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    Exposure = property(get_Exposure, None)
    ExposureCompensation = property(get_ExposureCompensation, None)
    InterleavedIlluminationEnabled = property(get_InterleavedIlluminationEnabled, None)
    StructureLightPatternEnabled = property(get_StructureLightPatternEnabled, None)
class IKnownPerceptionVideoFrameSourcePropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    IsMirrored = property(get_IsMirrored, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
class IKnownPerceptionVideoProfilePropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    FrameDuration = property(get_FrameDuration, None)
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class IPerceptionColorFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrame'
    _iid_ = Guid('{fe621549-2cbf-4f94-9861-f817ea317747}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionColorFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs'
    _iid_ = Guid('{8fad02d5-86f7-4d8d-b966-5a3761ba9f59}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionColorFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameReader'
    _iid_ = Guid('{7650f56e-b9f5-461b-83ad-f222af2aaadc}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameReader, win32more.Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrame: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class IPerceptionColorFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSource'
    _iid_ = Guid('{dc6dba7c-0b58-468d-9ca1-6db04cc0477c}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, correlatedDepthFrameSource: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetSourceId: WinRT_String, correlatedDepthFrameSource: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrameReader: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class IPerceptionColorFrameSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSource2'
    _iid_ = Guid('{f88008e5-5631-45ed-ad98-8c6aa04cfb91}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionColorFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs'
    _iid_ = Guid('{d16bf4e6-da24-442c-bbd5-55549b5b94f3}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionColorFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs'
    _iid_ = Guid('{d277fa69-eb4c-42ef-ba4f-288f615c93c1}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionColorFrameSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de49}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionColorFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionColorFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionColorFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher'
    _iid_ = Guid('{96bd1392-e667-40c4-89f9-1462dea6a9cc}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class IPerceptionControlSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionControlSession'
    _iid_ = Guid('{99998653-5a3d-417f-9239-f1889e548b48}')
    @winrt_commethod(6)
    def add_ControlLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionControlSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ControlLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def TrySetPropertyAsync(self, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    ControlLost = event()
class IPerceptionDepthCorrelatedCameraIntrinsics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics'
    _iid_ = Guid('{6548ca01-86de-5be1-6582-807fcf4c95cf}')
    @winrt_commethod(6)
    def UnprojectPixelAtCorrelatedDepth(self, pixelCoordinate: win32more.Windows.Foundation.Point, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def UnprojectPixelsAtCorrelatedDepth(self, sourceCoordinates: PassArray[win32more.Windows.Foundation.Point], depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(8)
    def UnprojectRegionPixelsAtCorrelatedDepthAsync(self, region: win32more.Windows.Foundation.Rect, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UnprojectAllPixelsAtCorrelatedDepthAsync(self, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPerceptionDepthCorrelatedCoordinateMapper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper'
    _iid_ = Guid('{5b4d9d1d-b5f6-469c-b8c2-b97a45e6863b}')
    @winrt_commethod(6)
    def MapPixelToTarget(self, sourcePixelCoordinate: win32more.Windows.Foundation.Point, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def MapPixelsToTarget(self, sourceCoordinates: PassArray[win32more.Windows.Foundation.Point], depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_commethod(8)
    def MapRegionOfPixelsToTargetAsync(self, region: win32more.Windows.Foundation.Rect, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: FillArray[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def MapAllPixelsToTargetAsync(self, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: FillArray[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPerceptionDepthFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrame'
    _iid_ = Guid('{a37b81fc-9906-4ffd-9161-0024b360b657}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionDepthFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs'
    _iid_ = Guid('{443d25b2-b282-4637-9173-ac978435c985}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionDepthFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameReader'
    _iid_ = Guid('{b1a3c09f-299b-4612-a4f7-270f25a096ec}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameReader, win32more.Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrame: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class IPerceptionDepthFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSource'
    _iid_ = Guid('{79d433d6-47fb-4df1-bfc9-f01d40bd9942}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, target: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetId: WinRT_String, depthFrameSourceToMapWith: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameReader: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class IPerceptionDepthFrameSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSource2'
    _iid_ = Guid('{e3d23d2e-6e2c-4e6d-91d9-704cd8dff79d}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionDepthFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs'
    _iid_ = Guid('{93a48168-8bf8-45d2-a2f8-4ac0931cc7a6}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionDepthFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs'
    _iid_ = Guid('{a0c0cc4d-e96c-4d81-86dd-38b95e49c6df}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionDepthFrameSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de48}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionDepthFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher'
    _iid_ = Guid('{780e96d1-8d02-4d2b-ada4-5ba624a0eb10}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class IPerceptionFrameSourcePropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs'
    _iid_ = Guid('{6c68e068-bcf1-4ecc-b891-7625d1244b6b}')
    @winrt_commethod(6)
    def get_CollectionChange(self) -> win32more.Windows.Foundation.Collections.CollectionChange: ...
    @winrt_commethod(7)
    def get_Key(self) -> WinRT_String: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class IPerceptionFrameSourcePropertyChangeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult'
    _iid_ = Guid('{1e33390a-3c90-4d22-b898-f42bba6418ff}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_commethod(7)
    def get_NewValue(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    NewValue = property(get_NewValue, None)
    Status = property(get_Status, None)
class IPerceptionInfraredFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrame'
    _iid_ = Guid('{b0886276-849e-4c7a-8ae6-b56064532153}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IPerceptionInfraredFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs'
    _iid_ = Guid('{9f77fac7-b4bd-4857-9d50-be8ef075daef}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def TryOpenFrame(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class IPerceptionInfraredFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameReader'
    _iid_ = Guid('{7960ce18-d39b-4fc8-a04a-929734c6756c}')
    @winrt_commethod(6)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameReader, win32more.Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    @winrt_commethod(9)
    def get_IsPaused(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsPaused(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def TryReadLatestFrame(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrame: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class IPerceptionInfraredFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSource'
    _iid_ = Guid('{55b08742-1808-494e-9e30-9d2a7be8f700}')
    @winrt_commethod(6)
    def add_AvailableChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AvailableChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PropertiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PropertiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_VideoProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_VideoProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CameraIntrinsicsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CameraIntrinsicsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
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
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_commethod(23)
    def get_SupportedVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(24)
    def get_AvailableVideoProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_commethod(25)
    def get_VideoProfile(self) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_commethod(26)
    def get_CameraIntrinsics(self) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_commethod(27)
    def AcquireControlSession(self) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_commethod(28)
    def CanControlIndependentlyFrom(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(29)
    def IsCorrelatedWith(self, targetId: WinRT_String) -> Boolean: ...
    @winrt_commethod(30)
    def TryGetTransformTo(self, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_commethod(31)
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self, target: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_commethod(32)
    def TryGetDepthCorrelatedCoordinateMapperAsync(self, targetId: WinRT_String, depthFrameSourceToMapWith: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_commethod(33)
    def TrySetVideoProfileAsync(self, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_commethod(34)
    def OpenReader(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameReader: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class IPerceptionInfraredFrameSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSource2'
    _iid_ = Guid('{dcd4d798-4b0b-4300-8d85-410817faa032}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IPerceptionInfraredFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs'
    _iid_ = Guid('{6d334120-95ce-4660-907a-d98035aa2b7c}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionInfraredFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs'
    _iid_ = Guid('{ea1a8071-7a70-4a61-af94-07303853f695}')
    @winrt_commethod(6)
    def get_FrameSource(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class IPerceptionInfraredFrameSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics'
    _iid_ = Guid('{5df3cca2-01f8-4a87-b859-d5e5b7e1de47}')
    @winrt_commethod(6)
    def CreateWatcher(self) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher: ...
    @winrt_commethod(7)
    def FindAllAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource]]: ...
    @winrt_commethod(8)
    def FromIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource]: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
class IPerceptionInfraredFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher'
    _iid_ = Guid('{383cff99-d70c-444d-a8b0-720c2e66fe3b}')
    @winrt_commethod(6)
    def add_SourceAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def Stop(self) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class IPerceptionVideoProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.IPerceptionVideoProfile'
    _iid_ = Guid('{75763ea3-011a-470e-8225-6f05ade25648}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(8)
    def get_Width(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Height(self) -> Int32: ...
    @winrt_commethod(10)
    def get_FrameDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def IsEqual(self, other: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> Boolean: ...
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    FrameDuration = property(get_FrameDuration, None)
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class _KnownCameraIntrinsicsProperties_Meta_(ComPtr.__class__):
    pass
class KnownCameraIntrinsicsProperties(ComPtr, metaclass=_KnownCameraIntrinsicsProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownCameraIntrinsicsProperties'
    @winrt_classmethod
    def get_FocalLength(cls: win32more.Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrincipalPoint(cls: win32more.Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RadialDistortion(cls: win32more.Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TangentialDistortion(cls: win32more.Windows.Devices.Perception.IKnownCameraIntrinsicsPropertiesStatics) -> WinRT_String: ...
    _KnownCameraIntrinsicsProperties_Meta_.FocalLength = property(get_FocalLength, None)
    _KnownCameraIntrinsicsProperties_Meta_.PrincipalPoint = property(get_PrincipalPoint, None)
    _KnownCameraIntrinsicsProperties_Meta_.RadialDistortion = property(get_RadialDistortion, None)
    _KnownCameraIntrinsicsProperties_Meta_.TangentialDistortion = property(get_TangentialDistortion, None)
class _KnownPerceptionColorFrameSourceProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionColorFrameSourceProperties(ComPtr, metaclass=_KnownPerceptionColorFrameSourceProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionColorFrameSourceProperties'
    @winrt_classmethod
    def get_Exposure(cls: win32more.Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AutoExposureEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ExposureCompensation(cls: win32more.Windows.Devices.Perception.IKnownPerceptionColorFrameSourcePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionColorFrameSourceProperties_Meta_.AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    _KnownPerceptionColorFrameSourceProperties_Meta_.Exposure = property(get_Exposure, None)
    _KnownPerceptionColorFrameSourceProperties_Meta_.ExposureCompensation = property(get_ExposureCompensation, None)
class _KnownPerceptionDepthFrameSourceProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionDepthFrameSourceProperties(ComPtr, metaclass=_KnownPerceptionDepthFrameSourceProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionDepthFrameSourceProperties'
    @winrt_classmethod
    def get_MinDepth(cls: win32more.Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MaxDepth(cls: win32more.Windows.Devices.Perception.IKnownPerceptionDepthFrameSourcePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionDepthFrameSourceProperties_Meta_.MaxDepth = property(get_MaxDepth, None)
    _KnownPerceptionDepthFrameSourceProperties_Meta_.MinDepth = property(get_MinDepth, None)
class _KnownPerceptionFrameSourceProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionFrameSourceProperties(ComPtr, metaclass=_KnownPerceptionFrameSourceProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionFrameSourceProperties'
    @winrt_classmethod
    def get_DeviceId(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Id(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PhysicalDeviceIds(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrameKind(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DeviceModelVersion(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EnclosureLocation(cls: win32more.Windows.Devices.Perception.IKnownPerceptionFrameSourcePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionFrameSourceProperties_Meta_.DeviceId = property(get_DeviceId, None)
    _KnownPerceptionFrameSourceProperties_Meta_.DeviceModelVersion = property(get_DeviceModelVersion, None)
    _KnownPerceptionFrameSourceProperties_Meta_.EnclosureLocation = property(get_EnclosureLocation, None)
    _KnownPerceptionFrameSourceProperties_Meta_.FrameKind = property(get_FrameKind, None)
    _KnownPerceptionFrameSourceProperties_Meta_.Id = property(get_Id, None)
    _KnownPerceptionFrameSourceProperties_Meta_.PhysicalDeviceIds = property(get_PhysicalDeviceIds, None)
class _KnownPerceptionInfraredFrameSourceProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionInfraredFrameSourceProperties(ComPtr, metaclass=_KnownPerceptionInfraredFrameSourceProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionInfraredFrameSourceProperties'
    @winrt_classmethod
    def get_Exposure(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AutoExposureEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ExposureCompensation(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ActiveIlluminationEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AmbientSubtractionEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StructureLightPatternEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_InterleavedIlluminationEnabled(cls: win32more.Windows.Devices.Perception.IKnownPerceptionInfraredFrameSourcePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.ActiveIlluminationEnabled = property(get_ActiveIlluminationEnabled, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.AmbientSubtractionEnabled = property(get_AmbientSubtractionEnabled, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.AutoExposureEnabled = property(get_AutoExposureEnabled, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.Exposure = property(get_Exposure, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.ExposureCompensation = property(get_ExposureCompensation, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.InterleavedIlluminationEnabled = property(get_InterleavedIlluminationEnabled, None)
    _KnownPerceptionInfraredFrameSourceProperties_Meta_.StructureLightPatternEnabled = property(get_StructureLightPatternEnabled, None)
class _KnownPerceptionVideoFrameSourceProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionVideoFrameSourceProperties(ComPtr, metaclass=_KnownPerceptionVideoFrameSourceProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionVideoFrameSourceProperties'
    @winrt_classmethod
    def get_VideoProfile(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SupportedVideoProfiles(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AvailableVideoProfiles(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IsMirrored(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CameraIntrinsics(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoFrameSourcePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionVideoFrameSourceProperties_Meta_.AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    _KnownPerceptionVideoFrameSourceProperties_Meta_.CameraIntrinsics = property(get_CameraIntrinsics, None)
    _KnownPerceptionVideoFrameSourceProperties_Meta_.IsMirrored = property(get_IsMirrored, None)
    _KnownPerceptionVideoFrameSourceProperties_Meta_.SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    _KnownPerceptionVideoFrameSourceProperties_Meta_.VideoProfile = property(get_VideoProfile, None)
class _KnownPerceptionVideoProfileProperties_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionVideoProfileProperties(ComPtr, metaclass=_KnownPerceptionVideoProfileProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.KnownPerceptionVideoProfileProperties'
    @winrt_classmethod
    def get_BitmapPixelFormat(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BitmapAlphaMode(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Width(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Height(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FrameDuration(cls: win32more.Windows.Devices.Perception.IKnownPerceptionVideoProfilePropertiesStatics) -> WinRT_String: ...
    _KnownPerceptionVideoProfileProperties_Meta_.BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    _KnownPerceptionVideoProfileProperties_Meta_.BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    _KnownPerceptionVideoProfileProperties_Meta_.FrameDuration = property(get_FrameDuration, None)
    _KnownPerceptionVideoProfileProperties_Meta_.Height = property(get_Height, None)
    _KnownPerceptionVideoProfileProperties_Meta_.Width = property(get_Width, None)
class PerceptionColorFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: win32more.Windows.Devices.Perception.IPerceptionColorFrame) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionColorFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameArrivedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionColorFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionColorFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameReader, win32more.Windows.Devices.Perception.PerceptionColorFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameReader) -> win32more.Windows.Devices.Perception.PerceptionColorFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class PerceptionColorFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, correlatedDepthFrameSource: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, targetSourceId: WinRT_String, correlatedDepthFrameSource: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource) -> win32more.Windows.Devices.Perception.PerceptionColorFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionColorFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionColorFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class PerceptionColorFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceAddedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionColorFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceRemovedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionColorFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionColorFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionColorFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionColorFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionColorFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionColorFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Perception.IPerceptionColorFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class PerceptionControlSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionControlSession
    _classid_ = 'Windows.Devices.Perception.PerceptionControlSession'
    @winrt_mixinmethod
    def add_ControlLost(self: win32more.Windows.Devices.Perception.IPerceptionControlSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionControlSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ControlLost(self: win32more.Windows.Devices.Perception.IPerceptionControlSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TrySetPropertyAsync(self: win32more.Windows.Devices.Perception.IPerceptionControlSession, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ControlLost = event()
class PerceptionDepthCorrelatedCameraIntrinsics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics'
    @winrt_mixinmethod
    def UnprojectPixelAtCorrelatedDepth(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, pixelCoordinate: win32more.Windows.Foundation.Point, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def UnprojectPixelsAtCorrelatedDepth(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, sourceCoordinates: PassArray[win32more.Windows.Foundation.Point], depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def UnprojectRegionPixelsAtCorrelatedDepthAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, region: win32more.Windows.Foundation.Rect, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnprojectAllPixelsAtCorrelatedDepthAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCameraIntrinsics, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Numerics.Vector3]) -> win32more.Windows.Foundation.IAsyncAction: ...
class PerceptionDepthCorrelatedCoordinateMapper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper'
    @winrt_mixinmethod
    def MapPixelToTarget(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, sourcePixelCoordinate: win32more.Windows.Foundation.Point, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def MapPixelsToTarget(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, sourceCoordinates: PassArray[win32more.Windows.Foundation.Point], depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, results: FillArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def MapRegionOfPixelsToTargetAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, region: win32more.Windows.Foundation.Rect, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: FillArray[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def MapAllPixelsToTargetAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthCorrelatedCoordinateMapper, depthFrame: win32more.Windows.Devices.Perception.PerceptionDepthFrame, targetCoordinates: FillArray[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.IAsyncAction: ...
class PerceptionDepthFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrame) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionDepthFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameArrivedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionDepthFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionDepthFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameReader, win32more.Windows.Devices.Perception.PerceptionDepthFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameReader) -> win32more.Windows.Devices.Perception.PerceptionDepthFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class PerceptionDepthFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, target: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, targetId: WinRT_String, depthFrameSourceToMapWith: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class PerceptionDepthFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceAddedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionDepthFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceRemovedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionDepthFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionDepthFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionDepthFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Perception.IPerceptionDepthFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class PerceptionFrameSourceAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    DeniedByUser = 2
    DeniedBySystem = 3
class PerceptionFrameSourcePropertiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs'
    @winrt_mixinmethod
    def get_CollectionChange(self: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs) -> win32more.Windows.Foundation.Collections.CollectionChange: ...
    @winrt_mixinmethod
    def get_Key(self: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertiesChangedEventArgs) -> WinRT_String: ...
    CollectionChange = property(get_CollectionChange, None)
    Key = property(get_Key, None)
class PerceptionFrameSourcePropertyChangeResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult
    _classid_ = 'Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult) -> win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_mixinmethod
    def get_NewValue(self: win32more.Windows.Devices.Perception.IPerceptionFrameSourcePropertyChangeResult) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    NewValue = property(get_NewValue, None)
    Status = property(get_Status, None)
class PerceptionFrameSourcePropertyChangeStatus(Enum, Int32):
    Unknown = 0
    Accepted = 1
    LostControl = 2
    PropertyNotSupported = 3
    PropertyReadOnly = 4
    ValueOutOfRange = 5
class PerceptionInfraredFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrame
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrame'
    @winrt_mixinmethod
    def get_VideoFrame(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrame) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    VideoFrame = property(get_VideoFrame, None)
class PerceptionInfraredFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs'
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def TryOpenFrame(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameArrivedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrame: ...
    RelativeTime = property(get_RelativeTime, None)
class PerceptionInfraredFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameReader'
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameReader, win32more.Windows.Devices.Perception.PerceptionInfraredFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    @winrt_mixinmethod
    def get_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPaused(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryReadLatestFrame(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameReader) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    IsPaused = property(get_IsPaused, put_IsPaused)
    Source = property(get_Source, None)
    FrameArrived = event()
class PerceptionInfraredFrameSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSource'
    @winrt_mixinmethod
    def add_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailableChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActiveChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PropertiesChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VideoProfileChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CameraIntrinsicsChanged(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Available(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Active(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsControlled(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_SupportedVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_AvailableVideoProfiles(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionVideoProfile]: ...
    @winrt_mixinmethod
    def get_VideoProfile(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Devices.Perception.PerceptionVideoProfile: ...
    @winrt_mixinmethod
    def get_CameraIntrinsics(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Media.Devices.Core.CameraIntrinsics: ...
    @winrt_mixinmethod
    def AcquireControlSession(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Devices.Perception.PerceptionControlSession: ...
    @winrt_mixinmethod
    def CanControlIndependentlyFrom(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def IsCorrelatedWith(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetTransformTo(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String, result: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCameraIntrinsicsAsync(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, target: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCameraIntrinsics]: ...
    @winrt_mixinmethod
    def TryGetDepthCorrelatedCoordinateMapperAsync(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, targetId: WinRT_String, depthFrameSourceToMapWith: win32more.Windows.Devices.Perception.PerceptionDepthFrameSource) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionDepthCorrelatedCoordinateMapper]: ...
    @winrt_mixinmethod
    def TrySetVideoProfileAsync(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource, controlSession: win32more.Windows.Devices.Perception.PerceptionControlSession, profile: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeResult]: ...
    @winrt_mixinmethod
    def OpenReader(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameReader: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSource2) -> WinRT_String: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher: ...
    @winrt_classmethod
    def FindAllAsync(cls: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource]]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]: ...
    Active = property(get_Active, None)
    Available = property(get_Available, None)
    AvailableVideoProfiles = property(get_AvailableVideoProfiles, None)
    CameraIntrinsics = property(get_CameraIntrinsics, None)
    DeviceId = property(get_DeviceId, None)
    DeviceKind = property(get_DeviceKind, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    IsControlled = property(get_IsControlled, None)
    Properties = property(get_Properties, None)
    SupportedVideoProfiles = property(get_SupportedVideoProfiles, None)
    VideoProfile = property(get_VideoProfile, None)
    AvailableChanged = event()
    ActiveChanged = event()
    PropertiesChanged = event()
    VideoProfileChanged = event()
    CameraIntrinsicsChanged = event()
class PerceptionInfraredFrameSourceAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceAddedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionInfraredFrameSourceRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs'
    @winrt_mixinmethod
    def get_FrameSource(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceRemovedEventArgs) -> win32more.Windows.Devices.Perception.PerceptionInfraredFrameSource: ...
    FrameSource = property(get_FrameSource, None)
class PerceptionInfraredFrameSourceWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher
    _classid_ = 'Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher'
    @winrt_mixinmethod
    def add_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceAdded(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRemoved(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Perception.PerceptionInfraredFrameSourceWatcher, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> win32more.Windows.Devices.Enumeration.DeviceWatcherStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Perception.IPerceptionInfraredFrameSourceWatcher) -> Void: ...
    Status = property(get_Status, None)
    SourceAdded = event()
    SourceRemoved = event()
    Stopped = event()
    EnumerationCompleted = event()
class PerceptionVideoProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.IPerceptionVideoProfile
    _classid_ = 'Windows.Devices.Perception.PerceptionVideoProfile'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile) -> Int32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile) -> Int32: ...
    @winrt_mixinmethod
    def get_FrameDuration(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Devices.Perception.IPerceptionVideoProfile, other: win32more.Windows.Devices.Perception.PerceptionVideoProfile) -> Boolean: ...
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    FrameDuration = property(get_FrameDuration, None)
    Height = property(get_Height, None)
    Width = property(get_Width, None)


make_ready(__name__)
